#!/usr/bin/env python3
"""Generate the English profile from the final Vietnamese LaTeX layout.

The script intentionally translates the assembled production file instead of
rebuilding pages.  Every TikZ coordinate, image, crop, table and page break is
therefore inherited from the approved Vietnamese edition.

Translation requires a local CTranslate2 Vietnamese-English model.  The
generated ``05-company-profile-en.tex`` is committed as a release artifact, so
normal PDF rebuilds do not require the model.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import ctranslate2
import sentencepiece as spm


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / "05-company-profile" / "05-company-profile.tex"
OUTPUT = ROOT / "05-company-profile-en.tex"

VIETNAMESE = re.compile(
    r"[ăâđêôơưĂÂĐÊÔƠƯáàảãạấầẩẫậắằẳẵặéèẻẽẹếềểễệíìỉĩị"
    r"óòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ"
    r"ÁÀẢÃẠẤẦẨẪẬẮẰẲẴẶÉÈẺẼẸẾỀỂỄỆÍÌỈĨỊÓÒỎÕỌỐỒỔỖỘỚỜỞỠỢ"
    r"ÚÙỦŨỤỨỪỬỮỰÝỲỶỸỴ]"
)

# Exact, client-facing terminology takes priority over machine translation.
# Entries are also used as protected phrases inside longer sentences.
GLOSSARY = {
    "CÔNG TY CỔ PHẦN CÔNG NGHỆ XÂY DỰNG TÂN THÀNH CÔNG":
        "TAN THANH CONG TECHNOLOGY CONSTRUCTION JOINT STOCK COMPANY",
    "Công ty Cổ phần Công nghệ Xây dựng Tân Thành Công":
        "Tan Thanh Cong Technology Construction Joint Stock Company",
    "Tân Thành Công": "Tan Thanh Cong",
    "TÂN THÀNH CÔNG JSC": "TAN THANH CONG JSC",
    "Ông PHẠM HUY TÂN": "Mr. PHAM HUY TAN",
    "PHẠM HUY TÂN": "PHAM HUY TAN",
    "Hà Nội": "Hanoi",
    "Đại Kim": "Dai Kim",
    "Kim Giang": "Kim Giang",
    "Trung Hòa Nhân Chính": "Trung Hoa Nhan Chinh",
    "TỔNG GIÁM ĐỐC": "CHIEF EXECUTIVE OFFICER",
    "Tổng Giám Đốc": "Chief Executive Officer",
    "Tổng Giám đốc": "Chief Executive Officer",
    "MỤC LỤC & THÔNG TIN PHÁP NHÂN": "CONTENTS & CORPORATE INFORMATION",
    "MỤC LỤC": "CONTENTS",
    "THÔNG TIN PHÁP NHÂN": "CORPORATE INFORMATION",
    "Mục Lục Tổng Quan": "Executive Contents",
    "THÔNG ĐIỆP TỪ TỔNG GIÁM ĐỐC": "MESSAGE FROM THE CEO",
    "Thông Điệp Từ Tổng Giám Đốc": "Message from the CEO",
    "HÀNH TRÌNH PHÁT TRIỂN & GIÁ TRỊ CỐT LÕI": "MILESTONES & CORE VALUES",
    "Hành Trình Kiến Tạo": "Our Development Journey",
    "HỆ SINH THÁI THIẾT KẾ & THI CÔNG TÍCH HỢP": "INTEGRATED DESIGN & BUILD ECOSYSTEM",
    "Hệ Sinh Thái Thiết Kế & Thi Công Tích Hợp": "Integrated Design & Build Ecosystem",
    "QUẢN TRỊ & NĂNG LỰC XÂY DỰNG HẠNG II": "GOVERNANCE & CONSTRUCTION CAPABILITY",
    "QUẢN TRỊ": "GOVERNANCE",
    "NĂNG LỰC XÂY DỰNG HẠNG II": "CONSTRUCTION CAPABILITY",
    "Quản Trị Tinh Gọn & Nền Tảng Tuân Thủ": "Lean Governance & Compliance Framework",
    "NĂNG LỰC NHÂN SỰ TRIỂN KHAI EPC": "EPC DELIVERY TEAM",
    "Đội Ngũ Tích Hợp Theo Vòng Đời Dự Án": "Integrated Team Across the Project Lifecycle",
    "QUẢN TRỊ TÀI CHÍNH DỰ ÁN & KỶ LUẬT DÒNG TIỀN": "PROJECT FINANCIAL GOVERNANCE & CASH-FLOW DISCIPLINE",
    "QUẢN TRỊ TÀI CHÍNH DỰ ÁN": "PROJECT FINANCE",
    "KỶ LUẬT DÒNG TIỀN": "CASH-FLOW DISCIPLINE",
    "Quản Trị Tài Chính Dự Án & Kỷ Luật Dòng Tiền": "Project Financial Governance & Cash-Flow Discipline",
    "BẢO LÃNH HỢP ĐỒNG & HUY ĐỘNG NGUỒN LỰC": "CONTRACT GUARANTEES & RESOURCE MOBILIZATION",
    "BẢO LÃNH HỢP ĐỒNG": "CONTRACT GUARANTEES",
    "HUY ĐỘNG NGUỒN LỰC": "RESOURCE MOBILIZATION",
    "Năng Lực Bảo Lãnh & Huy Động Cho Dự Án": "Guarantee Capacity & Project Mobilization",
    "ĐÀO TẠO NĂNG LỰC & VĂN HÓA AN TOÀN": "CAPABILITY DEVELOPMENT & SAFETY CULTURE",
    "ĐÀO TẠO NĂNG LỰC": "CAPABILITY DEVELOPMENT",
    "VĂN HÓA AN TOÀN": "SAFETY CULTURE",
    "Hành Trình Phát Triển Năng Lực": "Capability Development Pathway",
    "CHUỖI ĐỐI TÁC SẢN XUẤT PEB 30.000T": "30,000-TONNE PEB FABRICATION NETWORK",
    "Chuỗi Cung Ứng Nhà Thép Tiền Chế Được Kiểm Soát": "Controlled Pre-Engineered Steel Supply Chain",
    "THIẾT BỊ CƠ GIỚI & HUY ĐỘNG HIỆN TRƯỜNG": "CONSTRUCTION EQUIPMENT & SITE MOBILIZATION",
    "THIẾT BỊ CƠ GIỚI": "CONSTRUCTION EQUIPMENT",
    "HUY ĐỘNG HIỆN TRƯỜNG": "SITE MOBILIZATION",
    "Năng Lực Thiết Bị Theo Gói Huy Động": "Equipment Capacity by Mobilization Package",
    "QUẢN TRỊ DỰ ÁN EPC THEO STAGE-GATE": "STAGE-GATE EPC PROJECT GOVERNANCE",
    "Quản Trị Dự Án EPC Theo 4 Pha Kiểm Soát": "EPC Governance Through Four Control Phases",
    "GIẢI PHÁP TỔNG THẦU EPC & VALUE ENGINEERING": "EPC DELIVERY & VALUE ENGINEERING",
    "GIẢI PHÁP TỔNG THẦU EPC": "EPC DELIVERY",
    "Mô Hình Tổng Thầu EPC Tạo Giá Trị": "Value-Creating EPC Delivery Model",
    "MÔ HÌNH THÔNG TIN & DỮ LIỆU CÔNG TRÌNH": "BUILDING INFORMATION & PROJECT DATA",
    "MÔ HÌNH THÔNG TIN": "BUILDING INFORMATION MODEL",
    "DỮ LIỆU CÔNG TRÌNH": "PROJECT DATA",
    "Một Luồng Dữ Liệu Xuyên Suốt Vòng Đời Nhà Máy": "One Data Flow Across the Facility Lifecycle",
    "CÔNG TRÌNH XANH ESG & MÁI SOLAR-READY": "GREEN BUILDINGS & SOLAR-READY ROOFS",
    "CÔNG TRÌNH XANH ESG": "GREEN BUILDINGS",
    "MÁI SOLAR-READY": "SOLAR-READY ROOFS",
    "Nhà Máy Xanh Được Thiết Kế Như Một Bài Toán Kinh Doanh": "Green Factories Designed as a Business Case",
    "TRUNG TÂM ĐIỀU HÀNH CÔNG TRƯỜNG SỐ": "DIGITAL SITE CONTROL CENTRE",
    "Trung Tâm Điều Hành Công Trường Số": "Digital Site Control Centre",
    "HỆ THỐNG QUẢN LÝ CHẤT LƯỢNG QA/QC": "QA/QC MANAGEMENT SYSTEM",
    "Hộ Chiếu Chất Lượng Cho Từng Gói Công Việc": "A Quality Passport for Every Work Package",
    "AN TOÀN LAO ĐỘNG HSE & STOP WORK AUTHORITY": "HSE & STOP-WORK AUTHORITY",
    "AN TOÀN LAO ĐỘNG HSE": "HSE",
    "An Toàn Là Một Hệ Quyết Định — Không Chỉ Là PPE": "Safety Is a Decision System — Not Just PPE",
    "TOÀN CẢNH DANH MỤC DỰ ÁN": "PROJECT PORTFOLIO OVERVIEW",
    "Dấu Chân Dự Án Công Nghiệp": "Industrial Project Footprint",
    "CÔNG TRÌNH ĐẠI DIỆN": "REPRESENTATIVE PROJECTS",
    "Bằng Chứng Từ Công Trình Đã Triển Khai": "Evidence from Delivered Projects",
    "Danh Mục Dự Án Công Nghiệp Tiêu Biểu": "Selected Industrial Projects",
    "DANH MỤC DỰ ÁN TIÊU BIỂU": "SELECTED PROJECTS",
    "Danh Mục Dự Án Quốc Tế Và Công Nghiệp Phụ Trợ": "International & Supporting-Industry Projects",
    "DỰ ÁN TIÊU BIỂU • NHÀ MÁY CÔNG NGHỆ 2M": "SELECTED PROJECT • 2M TECHNOLOGY FACTORY",
    "GIẢI PHÁP KỸ THUẬT • NHÀ MÁY SƠN ALO": "ENGINEERING SOLUTION • ALO PAINT FACTORY",
    "GIẢI PHÁP KỸ THUẬT • NHÀ MÁY NHỰA SENDAI": "ENGINEERING SOLUTION • SENDAI PLASTICS FACTORY",
    "GIẢI PHÁP KỸ THUẬT • NHÀ MÁY MAY LÀO CAI": "ENGINEERING SOLUTION • LAO CAI GARMENT FACTORY",
    "GIẢI PHÁP KỸ THUẬT • TẬP ĐOÀN NHỰA DHL": "ENGINEERING SOLUTION • DHL PLASTICS GROUP",
    "GIẢI PHÁP KỸ THUẬT • NHÔM QUANG THỊNH": "ENGINEERING SOLUTION • QUANG THINH ALUMINIUM",
    "Hồ Sơ Dự Án": "Project Profile",
    "Nhà Máy Sản Xuất": "Manufacturing Plant",
    "Nhà Máy": "Factory",
    "Tổ Hợp Nhà Máy": "Factory Complex",
    "CHUỖI CUNG ỨNG • KIỂM SOÁT VẬT TƯ": "SUPPLY CHAIN • MATERIAL CONTROL",
    "Chuỗi Cung Ứng Được Kiểm Soát Theo Từng Lô": "Lot-Controlled Supply Chain",
    "HỆ SINH THÁI DỰ ÁN • 6 NHÓM NGÀNH": "PROJECT ECOSYSTEM • SIX SECTORS",
    "Sáu Hệ Công Trình — Một Năng Lực Tích Hợp": "Six Facility Types — One Integrated Capability",
    "BẰNG CHỨNG BÀN GIAO • CLOSEOUT DOSSIER": "HANDOVER EVIDENCE • CLOSEOUT DOSSIER",
    "Bộ Hồ Sơ Bàn Giao Có Thể Truy Xuất": "Traceable Handover Dossier",
    "NỀN TẢNG PHÁP LÝ • HỆ QUẢN TRỊ": "LEGAL FOUNDATION • GOVERNANCE SYSTEM",
    "Hồ Sơ Pháp Lý Sẵn Sàng Cho Thẩm Định": "Due-Diligence-Ready Corporate Records",
    "BẢN ĐỒ HIỆN DIỆN • CỤM CÔNG NGHIỆP": "PROJECT FOOTPRINT • INDUSTRIAL CLUSTERS",
    "Hiện Diện Theo Các Hành Lang Công Nghiệp Trọng Điểm": "Presence Along Vietnam's Key Industrial Corridors",
    "LỘ TRÌNH 2026--2030 • TĂNG TRƯỞNG CÓ KIỂM SOÁT": "2026--2030 ROADMAP • CONTROLLED GROWTH",
    "Lộ Trình Phát Triển Chọn Lọc Và Bền Vững": "Selective & Sustainable Development Roadmap",
    "BẢO HÀNH • HẬU MÃI • HỖ TRỢ VẬN HÀNH": "WARRANTY • AFTERCARE • OPERATIONAL SUPPORT",
    "Hỗ Trợ Sau Bàn Giao Theo Một Đầu Mối": "Single-Point Post-Handover Support",
    "HỆ SINH THÁI • THAM CHIẾU • HỢP TÁC": "ECOSYSTEM • REFERENCES • COLLABORATION",
    "Hệ Sinh Thái Và Các Bên Tham Chiếu": "Ecosystem & Corporate References",
    "HỒ SƠ NĂNG LỰC": "COMPANY PROFILE",
    "HỒ SƠ": "COMPANY",
    "NĂNG LỰC": "PROFILE",
    "ĐỒNG HÀNH KIẾN TẠO": "BUILDING TOGETHER",
    "GIÁ TRỊ BỀN VỮNG": "LASTING VALUE",
    "CHẤT LƯỢNG LÀ DANH DỰ.": "QUALITY IS OUR HONOUR.",
    "AN TOÀN LÀ SINH MỆNH.": "SAFETY IS OUR LIFELINE.",
    "TIẾN ĐỘ LÀ CAM KẾT.": "SCHEDULE IS OUR COMMITMENT.",
    "THÔNG ĐIỆP NHẤT QUÁN CỦA TTC": "TTC'S ENDURING MESSAGE",
    "Kính gửi Quý Chủ đầu tư, Quý Khách hàng và Quý Đối tác,": "Dear Clients and Partners,",
    "MỘT ĐẦU MỐI": "ONE CONTRACT",
    "KỸ THUẬT GIÁ TRỊ": "VALUE ENGINEERING",
    "AN TOÀN TỪ THIẾT KẾ": "SAFETY BY DESIGN",
    "KIẾN TẠO GIÁ TRỊ DÀI HẠN": "CREATING LONG-TERM VALUE",
    "TỪ NỀN TẢNG CƠ KHÍ ĐẾN TỔNG THẦU EPC THẾ HỆ MỚI": "FROM MECHANICAL FOUNDATIONS TO NEXT-GENERATION EPC",
    "5 GIÁ TRỊ — NỀN MÓNG CỦA MỌI CÔNG TRÌNH": "FIVE VALUES — THE FOUNDATION OF EVERY PROJECT",
    "CHI TIẾT CHỨNG NHẬN:": "CERTIFICATE DETAILS:",
    "HỆ THỐNG QUẢN LÝ ISO": "ISO MANAGEMENT SYSTEMS",
    "TÍCH HỢP": "INTEGRATED",
    "TÍN": "TRUST",
    "TÂM": "DEDICATION",
    "TẦM": "VISION",
    "TỐC": "SPEED",
    "AN": "SAFETY",
    "KHỞI TẠO": "FOUNDATION",
    "MỞ RỘNG": "EXPAND",
    "BỨT PHÁ": "BREAKTHROUGH",
    "CHUYỂN ĐỔI": "TRANSFORM",
    "VƯƠN TẦM": "REGIONAL GROWTH",
    "VẬT TƯ CHỈ ĐƯỢC LẮP ĐẶT SAU KHI ĐỦ HỒ SƠ": "MATERIALS ARE INSTALLED ONLY AFTER APPROVAL",
    "THIẾT KẾ BẮT ĐẦU TỪ CÁCH NHÀ MÁY VẬN HÀNH": "DESIGN STARTS WITH HOW THE PLANT OPERATES",
    "BÀN GIAO CÔNG TRÌNH — ĐỒNG THỜI BÀN GIAO BẰNG CHỨNG": "HANDOVER THE FACILITY — AND THE EVIDENCE",
    "MỘT BỘ HỒ SƠ — BỐN LỚP NĂNG LỰC CÓ THỂ ĐỐI CHIẾU": "ONE DOSSIER — FOUR VERIFIABLE CAPABILITY LAYERS",
    "BẢN ĐỒ KINH NGHIỆM TRIỂN KHAI TẠI VIỆT NAM": "PROJECT DELIVERY EXPERIENCE ACROSS VIETNAM",
    "MỞ RỘNG SAU KHI NĂNG LỰC QUẢN TRỊ ĐÃ SẴN SÀNG": "EXPAND ONLY WHEN GOVERNANCE IS READY",
    "BÀN GIAO KHÔNG PHẢI LÀ ĐIỂM KẾT THÚC": "HANDOVER IS NOT THE END",
    "KẾT NỐI NĂNG LỰC • CỘNG HƯỞNG GIÁ TRỊ": "CONNECTING CAPABILITIES • CREATING SHARED VALUE",
    "TỔNG THẦU CÔNG NGHIỆP TÍCH HỢP": "INTEGRATED INDUSTRIAL CONTRACTOR",
    "TỔNG THẦU CÔNG NGHIỆP": "INDUSTRIAL GENERAL CONTRACTOR",
    "NĂNG LỰC HẠNG II": "GRADE II CONSTRUCTION CAPABILITY",
    "HỆ THỐNG QUẢN LÝ ISO": "ISO MANAGEMENT SYSTEMS",
    "Chủ đầu tư": "Client",
    "chủ đầu tư": "client",
    "Tư vấn giám sát": "Supervision Consultant",
    "tư vấn giám sát": "supervision consultant",
    "Nhà thầu": "Contractor",
    "nhà thầu": "contractor",
    "Phòng cháy chữa cháy": "Fire Prevention & Fighting",
    "phòng cháy chữa cháy": "fire prevention & fighting",
    "kết cấu thép": "steel structure",
    "nhà thép tiền chế": "pre-engineered steel building",
    "bàn giao": "handover",
    "an toàn": "safety",
    "chất lượng": "quality",
    "tiến độ": "schedule",
    "Trang": "Page",
}

# Exact title casing and technical usage corrections applied after translation.
NORMALIZE = {
    "progress": "schedule",
    "fire protection": "fire prevention and fighting",
    "investor": "client",
    "the Investor": "the Client",
    "construction information model": "building information model",
    "labour safety": "occupational safety",
    "labor safety": "occupational safety",
    "acceptance": "inspection and acceptance",
}

TOKEN = re.compile(r"(\\[A-Za-z@]+\*?|\\.|[{}\[\]&%])")


class OfflineTranslator:
    def __init__(self, model_dir: Path):
        self.sp = spm.SentencePieceProcessor(
            model_file=str(model_dir / "sentencepiece.model")
        )
        self.engine = ctranslate2.Translator(
            str(model_dir / "model"), device="cpu", compute_type="int8"
        )

    def translate_many(self, texts: list[str]) -> list[str]:
        if not texts:
            return []
        encoded = [self.sp.encode(text, out_type=str) for text in texts]
        results = self.engine.translate_batch(
            encoded,
            beam_size=4,
            replace_unknowns=True,
            max_batch_size=32,
            batch_type="tokens",
        )
        return [
            self.sp.decode_pieces(result.hypotheses[0])
            .replace("▁", " ")
            .replace("_", " ")
            .strip()
            for result in results
        ]


class MyMemoryTranslator:
    """Small batched client used only while generating the release source."""

    endpoint = "https://api.mymemory.translated.net/get"
    delimiter = "\nZXQSPLITQXZ\n"

    def __init__(self, email: str, cache_file: Path):
        self.email = email
        self.cache_file = cache_file
        if cache_file.exists():
            self.cache = json.loads(cache_file.read_text(encoding="utf-8"))
        else:
            self.cache = {}

    def _request(self, texts: list[str]) -> list[str]:
        query = self.delimiter.join(texts)
        params = urllib.parse.urlencode(
            {"q": query, "langpair": "vi|en", "de": self.email}
        )
        request = urllib.request.Request(
            f"{self.endpoint}?{params}",
            headers={"User-Agent": "TTC-Profile-Translation/1.0"},
        )
        last_error: Exception | None = None
        for attempt in range(4):
            try:
                with urllib.request.urlopen(request, timeout=45) as response:
                    payload = json.load(response)
                if payload.get("responseStatus") != 200:
                    raise RuntimeError(payload.get("responseDetails", payload))
                translated = html.unescape(payload["responseData"]["translatedText"])
                parts = translated.split(self.delimiter)
                if len(parts) != len(texts):
                    raise RuntimeError("translation delimiter was not preserved")
                return [part.strip() for part in parts]
            except Exception as exc:  # transient public endpoint errors
                last_error = exc
                time.sleep(2 ** attempt)
        raise RuntimeError(f"MyMemory translation failed: {last_error}")

    @staticmethod
    def _groups(texts: list[str], limit: int = 430) -> list[list[str]]:
        groups: list[list[str]] = []
        current: list[str] = []
        size = 0
        for text in texts:
            extra = len(text) + (len(MyMemoryTranslator.delimiter) if current else 0)
            if current and size + extra > limit:
                groups.append(current)
                current = []
                size = 0
            current.append(text)
            size += len(text) + (len(MyMemoryTranslator.delimiter) if len(current) > 1 else 0)
        if current:
            groups.append(current)
        return groups

    def translate_many(self, texts: list[str]) -> list[str]:
        missing = list(dict.fromkeys(text for text in texts if text not in self.cache))
        groups = self._groups(missing)
        if groups:
            with ThreadPoolExecutor(max_workers=4) as pool:
                translated_groups = list(pool.map(self._request, groups))
            for group, translations in zip(groups, translated_groups):
                self.cache.update(zip(group, translations))
            self.cache_file.write_text(
                json.dumps(self.cache, ensure_ascii=False, indent=2), encoding="utf-8"
            )
        return [self.cache[text] for text in texts]


def protect_terms(text: str) -> tuple[str, dict[str, str]]:
    protected: dict[str, str] = {}
    for source, target in sorted(GLOSSARY.items(), key=lambda item: -len(item[0])):
        pattern = re.compile(r"(?<!\w)" + re.escape(source) + r"(?!\w)")
        if not pattern.search(text):
            continue
        marker = f"ZXQ{len(protected):03d}QXZ"
        text = pattern.sub(marker, text)
        protected[marker] = target
    return text, protected


def restore_terms(text: str, protected: dict[str, str]) -> str:
    for marker, target in protected.items():
        text = re.sub(re.escape(marker), lambda _: target, text, flags=re.IGNORECASE)
        # Some models insert spaces inside an unfamiliar marker.
        spaced = " ".join(marker)
        text = re.sub(re.escape(spaced), lambda _: target, text, flags=re.IGNORECASE)
    for source, target in NORMALIZE.items():
        text = text.replace(source, target)
    return text


def latex_escape_generated(text: str) -> str:
    # Translation chunks never include existing LaTeX commands; escape only
    # characters newly produced by the model.
    text = text.replace("\\", "")
    text = text.replace("&", r"\&")
    text = text.replace("%", r"\%")
    text = text.replace("#", r"\#")
    text = text.replace("_", r"\_")
    return text


def split_translatable_chunks(source: str) -> tuple[list[str], list[tuple[int, int]]]:
    chunks: list[str] = []
    spans: list[tuple[int, int]] = []
    offset = 0
    for line in source.splitlines(keepends=True):
        stripped = line.lstrip()
        if stripped.startswith("%") or not VIETNAMESE.search(line):
            offset += len(line)
            continue
        # Keep comments intact if a content line has a trailing TeX comment.
        content_end = len(line)
        escaped = False
        for index, char in enumerate(line):
            if char == "%" and not escaped:
                content_end = index
                break
            escaped = char == "\\" and not escaped
            if char != "\\":
                escaped = False
        content = line[:content_end]
        cursor = 0
        for match in TOKEN.finditer(content):
            candidate = content[cursor:match.start()]
            if VIETNAMESE.search(candidate):
                chunks.append(candidate)
                spans.append((offset + cursor, offset + match.start()))
            cursor = match.end()
        candidate = content[cursor:]
        if VIETNAMESE.search(candidate):
            chunks.append(candidate)
            spans.append((offset + cursor, offset + len(content)))
        offset += len(line)
    return chunks, spans


def translate_source(source: str, translator: OfflineTranslator) -> str:
    chunks, spans = split_translatable_chunks(source)
    prepared: list[str] = []
    metadata: list[tuple[str, str, dict[str, str]]] = []
    for chunk in chunks:
        leading = chunk[: len(chunk) - len(chunk.lstrip())]
        trailing = chunk[len(chunk.rstrip()):] if chunk.rstrip() else ""
        core = chunk.strip()
        if core in GLOSSARY:
            prepared.append("")
            metadata.append((leading, trailing, {"__EXACT__": GLOSSARY[core]}))
            continue
        protected_core, protected = protect_terms(core)
        prepared.append(protected_core)
        metadata.append((leading, trailing, protected))

    pending_indexes = [i for i, text in enumerate(prepared) if text]
    translated_pending: list[str] = []
    for start in range(0, len(pending_indexes), 128):
        batch_ids = pending_indexes[start:start + 128]
        translated_pending.extend(
            translator.translate_many([prepared[index] for index in batch_ids])
        )

    translated: list[str] = [""] * len(chunks)
    pending_iter = iter(translated_pending)
    for index, (leading, trailing, protected) in enumerate(metadata):
        if "__EXACT__" in protected:
            result = protected["__EXACT__"]
        else:
            result = restore_terms(next(pending_iter), protected)
        translated[index] = leading + latex_escape_generated(result) + trailing

    pieces: list[str] = []
    cursor = 0
    for (start, end), replacement in zip(spans, translated):
        pieces.append(source[cursor:start])
        pieces.append(replacement)
        cursor = end
    pieces.append(source[cursor:])
    result = "".join(pieces)
    result = result.replace(r"\usepackage[vietnamese]{babel}", r"\usepackage[english]{babel}")
    result = result.replace(
        "05-company-profile", "05-company-profile-en"
    )
    result = result.replace(
        "{assets/milestones_engineer_hero.jpg}",
        "{../05-company-profile/assets/milestones_engineer_hero.jpg}",
    )
    result = re.sub(r"\bTRANG\b", "PAGE", result)
    result = result.replace("{TÍN}", "{TRUST}")
    result = result.replace("{TÂM}", "{DEDICATION}")
    result = result.replace("{TẦM}", "{VISION}")
    result = result.replace("{TỐC}", "{SPEED}")
    result = result.replace("{AN}", "{SAFETY}")
    result = re.sub(r"\bTrang\b", "Page", result)

    # Editorial polish for the leadership page. These replacements are kept
    # here (rather than hand-edited in the generated TeX) so regeneration is
    # deterministic.
    release_replacements = {
        "SCHEDULE IS OUR COMMITMENT.": "WE DELIVER AS PROMISED.",
        "On behalf of the Board of Directors and all employees ":
            "On behalf of the Board of Directors and all employees of ",
        ", I would like to thank you for your trust and companionship throughout the development journey of TTC.":
            ", I sincerely thank you for your trust and partnership throughout TTC's development journey.",
        "More than a decade in the industrial construction sector helps us understand that a successful project must simultaneously meet the ":
            "More than a decade in industrial construction has taught us that every successful project must achieve ",
        ". Therefore, Tan Thanh Cong is consistent with the model ":
            ". Tan Thanh Cong therefore operates through ",
        "a design focal point--procurement--compliance":
            "a single point of responsibility for design--procurement--construction",
        ", combining value engineering, building information modeling and controlled field administration.":
            ", supported by value engineering, building information modelling and disciplined site management.",
        "With the steel structure manufacturing partner ecosystem and a team of field engineers, we are committed to providing the right solution for each factory, transparent control from design, construction to handover and warranty.":
            "Through our steel-fabrication partner network and experienced field engineers, we provide fit-for-purpose solutions with transparent control from design and construction through handover and warranty.",
        "TTC aspires to be not just a contractor, but a ":
            "TTC aims to be more than a contractor: a ",
        "long-term value-creating partners": "long-term value-creation partner",
        " same Client per building.": " for every client and every project.",
        "Technology Joint Stock Company\\Construction of Tan Thanh Cong":
            "Tan Thanh Cong Technology\\Construction Joint Stock Company",
        "Technology Joint Stock Company Construction of Tan Thanh Cong":
            "Tan Thanh Cong Technology Construction Joint Stock Company",
        "TAN SUCCEED": "TAN THANH CONG",
        "\\bfseries AN}": "\\bfseries SAFETY}",
        "A development journey supported by execution capability, technology and immutable values.":
            "A development journey built on delivery capability, technology and enduring values.",
        "Certificate of Competency Class II": "Construction capability certification",
        "and the general contractor of industrial park infrastructure.":
            "and industrial infrastructure delivery.",
        "Standardization of project management": "Standardized project management",
        "and data system of the works.": "and project data systems.",
        "Prioritize handover capacity, iterate customer, and quality administration before expansion rate.":
            "Prioritize delivery capability, repeat clients and governance quality before the pace of expansion.",
        "EXPAND PROFILE": "EXPAND CAPABILITY",
        "Customer iteration": "Repeat clients",
        "Multi-project administration": "Multi-project governance",
        "FOUR FILTERS BEFORE GETTING MORE SCALE": "FOUR FILTERS BEFORE SCALING",
        "CONSTRUCTION OF COVERAGE": "SCOPE FIT",
        "PROWER READY": "RESOURCES READY",
        "POWER HANDOVER": "HANDOVER CAPACITY",
        "PROFILE GRADE II CONSTRUCTION ACTIVITIES": "CONSTRUCTION CAPABILITY",
        "COLLABORATE FOR BETTER IMPLEMENTATION": "COLLABORATE FOR BETTER DELIVERY",
        "SONG SONG": "PARALLEL DELIVERY",
        "INDUSTRIAL GENERAL CONTRACTOR\\\\INTEGRATED": "INTEGRATED INDUSTRIAL\\\\CONTRACTOR",
        "Design, construction capacity and handover industrial works":
            "Design, build and handover of industrial facilities",
        "INDUSTRIAL GENERAL CONTRACTOR \\qquad GRADE II CONSTRUCTION CAPABILITY \\qquad ISO MANAGEMENT SYSTEMS":
            "INDUSTRIAL CONTRACTOR \\qquad GRADE II CAPABILITY \\qquad ISO SYSTEMS",
        r"\casepagebars{ENGINEERING SOLUTION • ALO PAINT FACTORY}":
            r"\casepagebars{ALO PAINT FACTORY}",
        r"\casepagebars{ENGINEERING SOLUTION • SENDAI PLASTICS FACTORY}":
            r"\casepagebars{SENDAI PLASTICS FACTORY}",
        r"\casepagebars{ENGINEERING SOLUTION • LAO CAI GARMENT FACTORY}":
            r"\casepagebars{LAO CAI GARMENT FACTORY}",
        r"\casepagebars{ENGINEERING SOLUTION • DHL PLASTICS GROUP}":
            r"\casepagebars{DHL PLASTICS FACTORY}",
        r"\casepagebars{ENGINEERING SOLUTION • QUANG THINH ALUMINIUM}":
            r"\casepagebars{QUANG THINH ALUMINIUM FACTORY}",
        "COMPANY/CO--CQ • MTC • catalog • warranty":
            "DOCUMENT CONTROL/CO--CQ • MTC • catalogue • warranty",
        "TRACEABILITY OF INSTALLATION/Lot of materials associated with the area and inspection and acceptance minutes":
            "INSTALLATION TRACEABILITY/Lot linked to area and inspection record",
        "SON \\& CHEMICALS": "PAINTS \\& CHEMICALS",
        "ELECTRICITY \\& MEP": "ELECTRICAL \\& MEP",
        "HVAC \\& Fire": "HVAC \\& FIRE PROTECTION",
        "in ACCORDANCE WITH QUALITY": "COMPLIANT QUALITY",
        "Tan Thanh Cong is ready to accompany Client from concept, design to construction and handover industrial works.":
            "Tan Thanh Cong partners with clients from concept and design through construction and handover.",
        "PHOTO OF COMMENCEMENT CEREMONY": "SITE CEREMONY",
        "STIRRING TANK\\\\PHA SON NATIONAL PARK": "PAINT-MIXING\\\\TANK",
        "LINES\\\\PACKAGING": "PACKAGING\\\\LINE",
        "Complex of 2 workshops \\& VP": "Two workshops \\& office",
        "PROGRESS OF GENERAL CONTRACTOR": "TURNKEY DELIVERY",
        "Project Profile 05: Manufacturing Plant DHL Plastic":
            "Project Profile 05: DHL Plastics Factory",
        "High-grade plastic packaging plant • PE/PP film extrusion":
            "PE/PP packaging film • Blown-film extrusion",
        "PRINCIPLE DIAGRAM • PLASTIC FILM BLOWING EXTRUSION LINE \\& MEP BACKEND SYSTEM":
            "PROCESS DIAGRAM • FILM EXTRUSION \\& UTILITIES",
        "BLOWING EXTRUSION TOWER\\\\MULTILAYER MEMBRANE\\\\CASCADE COMPARTMENT":
            "BLOWN-FILM TOWER\\\\MULTILAYER FILM",
        "GRAVURE PRINTER \\&\\\\AUTOMATIC FILM REEL":
            "GRAVURE PRINTING\\\\\\& REWINDING",
        "SPEED MULTI-COLOR PRINTING HEIGHT": "MULTICOLOUR PRINTING",
        "FINISHED GOODS WAREHOUSE \\&\\\\PROTOPLASTIC BEADS":
            "RESIN \\& FINISHED-GOODS\\\\STORAGE",
        "AXLE COOLING CHILLER PIPE \\& MEDIUM COMPRESSED AIR DEDICATION":
            "CHILLED WATER • COMPRESSED AIR",
        "HARDENED POLISHED CONCRETE FLOOR HARDENER AGAINST DUST":
            "HARDENED, DUST-RESISTANT CONCRETE FLOOR",
        "WORKSHOP COMPLEX \\& VP": "FACTORY \\& OFFICE",
        "HIGH POWER MEP": "PROCESS UTILITIES",
        "CORE VALUES: HIGH-GRADE PLASTIC PACKAGING PRODUCTION INFRASTRUCTURE • ACTUAL HANDOVER QUALITY":
            "CORE VALUE: INTEGRATED PACKAGING-FILM PRODUCTION INFRASTRUCTURE",
        "1ST FLOOR: RAW MATERIAL WAREHOUSE \\& EXPORT AND IMPORT OF FINISHED PRODUCTS":
            "1ST FLOOR: RAW MATERIALS • FINISHED-GOODS LOGISTICS",
        "2ND FLOOR: CUTTING WORKSHOP \\& SEWING SAMPLE":
            "2ND FLOOR: CUTTING \\& SAMPLE SEWING",
        "5TH FLOOR: FINISHING, COMFORTING \\& PACKAGING":
            "5TH FLOOR: FINISHING \\& PACKAGING",
        "Project Profile 06: Manufacturing Plant Quang Thinh Aluminum":
            "Project Profile 06: Quang Thinh Aluminium Plant",
        "High-grade aluminum profiles plant": "High-grade aluminium profiles",
        "ACTUAL CONSTRUCTION PHOTOS": "SITE PHOTO",
        "QUANG THINH ALUMINUM FACTORY": "QUANG THINH ALUMINIUM PLANT",
        "EXTRUSION FACTORY COMPLEX \\& POWDER COATING":
            "EXTRUSION \\& POWDER-COATING COMPLEX",
        "Quang Thinh Aluminum Joint Stock Company": "Quang Thinh Aluminium JSC",
        "Extrusion workshop complex \\& Executive office building":
            "Extrusion plant \\& office building",
        "Tan Thanh Cong JSC: PEB General Contractor \\& Electromechanical MEP":
            "TTC JSC: PEB general contractor \\& MEP",
        "PRINCIPLE DIAGRAM • ALUMINUM PROFILE EXTRUSION LINE \\& SURFACE TREATMENT":
            "PROCESS DIAGRAM • ALUMINIUM EXTRUSION \\& FINISHING",
        "Heavy duty extruder foundation": "Press foundation",
        "The large block reinforced concrete foundation is designed according to the dynamic load of the hydraulic press.":
            "A reinforced block foundation is designed for hydraulic-press dynamic loads.",
        "Closed spray booth, high temperature oven and Anode plating wastewater treatment station.":
            "Closed spray booth, curing oven and anodising wastewater treatment.",
        "Wear-Resistant Hardener Flooring": "Hardened floor",
        "The grinding concrete surface is hardened, dustproof and designed according to the load of the workpiece forklift.":
            "A dustproof surface is designed for forklift and workpiece loads.",
        "CRANE GIRDER FOR ALUMINUM WORKPIECE LIFTING \\& CHANGE EXTRUSION MOLD":
            "OVERHEAD CRANE • BILLET \\& DIE HANDLING",
        "ALUMINUM BLAST FURNACE \\&\\\\HYDRAULIC EXTRUDER":
            "BILLET HEATING\\\\HYDRAULIC EXTRUSION",
        "EXTRUSION BY LINE": "PROFILE EXTRUSION",
        "COOLING STRETCHING TABLE \\&\\\\HOMOGENIZING FURNACE":
            "COOLING TABLE\\\\AGEING FURNACE",
        "CONFIGURE LONG PROFILE": "PROFILE SIZING",
        "POWDER COATING LINE\\\\\\& FINISHED PRODUCT PACKAGING":
            "POWDER COATING\\\\\\& PACKING",
        "ANODE PLATING • HANGING PAINT": "ANODISING • COATING",
        "EXTRUSION MOLD COOLING WATER SYSTEM \\& MEDIUM COMPRESSED AIR DEDICATION":
            "DIE COOLING WATER • COMPRESSED AIR",
        "FLOOR CONCRETE GRINDING HARDENER HARDENER ABRASION RESISTANT":
            "HARDENED, ABRASION-RESISTANT CONCRETE FLOOR",
        "EXTRUSION OF HEAVY LOADS": "HEAVY-DUTY EXTRUSION",
        "SURFACE TREATMENT \\& MEP": "FINISHING \\& MEP",
        "LUMP-SUM GENERAL CONTRACTOR": "TURNKEY DELIVERY",
        "CORE VALUES: HIGH-TECH ALUMINUM PROFILE PRODUCTION INFRASTRUCTURE • SYNCHRONOUS GENERAL CONTRACTOR SOLUTION":
            "CORE VALUE: INTEGRATED ALUMINIUM EXTRUSION INFRASTRUCTURE",
    }
    for old, new in release_replacements.items():
        result = result.replace(old, new)

    # The Vietnamese master uses very small micro-copy in dense diagrams.
    # Raise every sub-6pt label for the English release while retaining the
    # original coordinates and hierarchy.
    microtype_upgrades = {
        r"\fontsize{4.6}{5.4}": r"\fontsize{5.8}{6.8}",
        r"\fontsize{4.7}{5.5}": r"\fontsize{5.8}{6.8}",
        r"\fontsize{4.8}{5.6}": r"\fontsize{5.9}{6.9}",
        r"\fontsize{4.8}{5.8}": r"\fontsize{5.9}{7}",
        r"\fontsize{5}{5.5}": r"\fontsize{6}{7}",
        r"\fontsize{5.1}{6.1}": r"\fontsize{6}{7}",
        r"\fontsize{5.2}{6.2}": r"\fontsize{6.1}{7.2}",
        r"\fontsize{5.4}{6.5}": r"\fontsize{6.2}{7.3}",
        r"\fontsize{5.5}{6}": r"\fontsize{6.2}{7.2}",
        r"\fontsize{5.5}{6.6}": r"\fontsize{6.2}{7.3}",
        r"\fontsize{5.5}{6.7}": r"\fontsize{6.2}{7.4}",
        r"\fontsize{5.5}{6.8}": r"\fontsize{6.2}{7.4}",
        r"\fontsize{5.6}{6.7}": r"\fontsize{6.2}{7.4}",
        r"\fontsize{5.6}{6.8}": r"\fontsize{6.2}{7.4}",
        r"\fontsize{5.7}{6.7}": r"\fontsize{6.3}{7.4}",
        r"\fontsize{5.7}{6.8}": r"\fontsize{6.3}{7.5}",
        r"\fontsize{5.8}{6.5}": r"\fontsize{6.3}{7.4}",
        r"\fontsize{5.8}{6.8}": r"\fontsize{6.3}{7.5}",
        r"\fontsize{5.8}{7}": r"\fontsize{6.3}{7.5}",
        r"\fontsize{5.8}{7.2}": r"\fontsize{6.3}{7.6}",
        r"\fontsize{5.9}{7.1}": r"\fontsize{6.4}{7.6}",
        r"\fontsize{5.9}{7.2}": r"\fontsize{6.4}{7.7}",
    }
    for old, new in microtype_upgrades.items():
        result = result.replace(old, new)

    # Keep all supporting copy at a practical print minimum. English strings
    # are often wider than Vietnamese ones, so the leading is also increased
    # slightly to preserve legibility without changing the page geometry.
    def enforce_minimum_type(match: re.Match[str]) -> str:
        size = float(match.group(1))
        leading = float(match.group(2))
        if size >= 6.5:
            return match.group(0)
        return rf"\fontsize{{6.5}}{{{max(leading, 7.7):g}}}"

    result = re.sub(
        r"\\fontsize\{([0-9]+(?:\.[0-9]+)?)\}\{([0-9]+(?:\.[0-9]+)?)\}",
        enforce_minimum_type,
        result,
    )

    # The supplied raster logo contains a Vietnamese descriptor. Build a
    # clean English lock-up from the untouched TTC symbol and live type.
    logo_macro_anchor = r"\definecolor{TTCBorder}{RGB}{203, 213, 225}"
    logo_macro = r"""

% English TTC lock-up: symbol from the official asset, descriptor in live type.
\newcommand{\ttcenglishlogo}[1]{%
  \begin{tikzpicture}[x=1mm,y=1mm,baseline=(word.base)]
    \node[anchor=west,inner sep=0pt] at (0,0)
      {\includegraphics[height=#1,trim=0 0 188 0,clip]{../../public/logo-ttc-removebg-DNXrVdJp.png}};
    \node[anchor=west,align=left,inner sep=0pt,text=TTCRed] (word) at (13,0)
      {{\fontsize{11}{12.5}\selectfont\bfseries TAN THANH CONG}\\[-0.3mm]
       {\fontsize{6.5}{7.7}\selectfont\bfseries\color{TTCBlue} TECHNOLOGY CONSTRUCTION JSC}};
  \end{tikzpicture}%
}
"""
    result = result.replace(logo_macro_anchor, logo_macro_anchor + logo_macro)

    result = result.replace(
        r"\includegraphics[width=48mm]{../../public/logo-ttc-removebg-DNXrVdJp.png}",
        r"\ttcenglishlogo{14mm}",
    )
    result = result.replace(
        r"\includegraphics[width=57mm]{../../public/logo-ttc-removebg-DNXrVdJp.png}",
        r"\ttcenglishlogo{16mm}",
    )

    # A few project photographs contain Vietnamese labels baked into the
    # pixels. Preserve the photographs and cover only those label areas with
    # concise English captions.
    embedded_label_overlays = {
        r"{\includegraphics[width=28mm,height=36mm]{../../public/project-assets/son_alo_1.jpg}};":
            r"""{\includegraphics[width=28mm,height=36mm]{../../public/project-assets/son_alo_1.jpg}};
    \fill[TTCDeepNavy,opacity=.94] (73,198) rectangle (101,217);
    \node[anchor=west,text=white,font=\fontsize{6.5}{7.7}\selectfont\bfseries]
      at (75,209) {GROUNDBREAKING};
    \node[anchor=west,text=white!78!gray,font=\fontsize{6.5}{7.7}\selectfont]
      at (75,203) {PROJECT MILESTONE};""",
        r"{\includegraphics[width=128mm]{../../public/project-assets/laocai_4.jpg}};":
            r"""{\includegraphics[width=128mm]{../../public/project-assets/laocai_4.jpg}};
    \fill[TTCDeepNavy,opacity=.94] (0,216) rectangle (40,220);
    \node[anchor=west,text=white,font=\fontsize{6.5}{7.7}\selectfont\bfseries]
      at (2,218) {LAO CAI FACTORY};""",
        r"{\includegraphics[width=42mm,height=32mm]{../../public/project-assets/laocai_3.jpg}};":
            r"""{\includegraphics[width=42mm,height=32mm]{../../public/project-assets/laocai_3.jpg}};
    \fill[white,opacity=.94] (70,212.5) rectangle (101,216);
    \node[anchor=west,text=TTCBlue,font=\fontsize{6.5}{7.7}\selectfont\bfseries]
      at (72,214.2) {SITE PLAN};""",
        r"{\includegraphics[width=104mm]{../../public/project-assets/dhl_2.jpg}};":
            r"""{\includegraphics[width=104mm]{../../public/project-assets/dhl_2.jpg}};
    \fill[TTCDeepNavy,opacity=.94] (80,212) rectangle (104,220);
    \node[anchor=west,text=white,font=\fontsize{6.5}{7.7}\selectfont\bfseries]
      at (84,216) {HA NAM};""",
    }
    for original_image, english_overlay in embedded_label_overlays.items():
        result = result.replace(original_image, english_overlay)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--provider", choices=("offline", "mymemory"), default="offline"
    )
    parser.add_argument(
        "--model-dir",
        type=Path,
        help="Directory containing model/ and sentencepiece.model",
    )
    parser.add_argument("--email", help="Contact email for MyMemory quota")
    parser.add_argument(
        "--cache-file", type=Path, default=Path("/tmp/ttc-profile-translation-cache.json")
    )
    args = parser.parse_args()
    source = SOURCE.read_text(encoding="utf-8")
    if args.provider == "mymemory":
        if not args.email:
            parser.error("--email is required with --provider mymemory")
        translator = MyMemoryTranslator(args.email, args.cache_file)
    else:
        if not args.model_dir:
            parser.error("--model-dir is required with --provider offline")
        translator = OfflineTranslator(args.model_dir)
    translated = translate_source(source, translator)
    OUTPUT.write_text(translated, encoding="utf-8")
    print(f"Generated {OUTPUT}")


if __name__ == "__main__":
    main()
