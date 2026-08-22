#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translation script: Vietnamese → Simplified Chinese
Reads original section*.py files, replaces Vietnamese text with Chinese,
and writes to section*_zh.py files.
"""

import re
import os

# ============================================================
# TRANSLATION MAP: Vietnamese → Chinese
# Order matters: longer strings first to avoid partial matches
# ============================================================

TRANSLATIONS = [
    # ===== HEADER / FOOTER / MACRO LEVEL =====
    ("CÔNG TY CỔ PHẦN CÔNG NGHỆ XÂY DỰNG TÂN THÀNH CÔNG", "新成功建筑科技股份公司"),
    ("Công ty Cổ phần Công nghệ Xây dựng Tân Thành Công", "新成功建筑科技股份公司"),
    ("Công ty Cổ phần Công nghệ\\\\Xây dựng Tân Thành Công", "新成功建筑科技股份公司"),
    
    # ===== PAGE 01: COVER =====
    ("TAN THANH CONG TECHNOLOGY CONSTRUCTION JOINT STOCK COMPANY", "TAN THANH CONG TECHNOLOGY CONSTRUCTION JOINT STOCK COMPANY"),
    ("HỒ SƠ", "企业"),
    ("NĂNG LỰC", "能力简介"),
    ("TỔNG THẦU EPC CÔNG NGHIỆP\\\\THẾ HỆ MỚI", "新一代工业EPC总承包商"),
    ("Turnkey Industrial EPC General Contractor", "Turnkey Industrial EPC General Contractor"),
    ("150+ DỰ ÁN", "150+ 项目"),
    ("HẠNG I BXD", "一级建筑资质"),
    ("Năng lực tổng thầu công nghiệp đã được chứng minh tại hiện trường", "经现场验证的工业总承包能力"),
    ("NĂNG LỰC HẠNG I BXD", "一级建筑资质"),
    
    # ===== PAGE 02: TABLE OF CONTENTS =====
    ("MỤC LỤC \\& THÔNG TIN PHÁP NHÂN", "目录与法人信息"),
    ("Mục Lục Tổng Quan", "总目录"),
    ("Executive Contents — 06 Chuyên Mục Trọng Tâm", "Executive Contents — 06 Core Sections"),
    ("Hồ sơ được tổ chức theo 06 nhóm năng lực để Chủ đầu tư tra cứu nhanh; chi tiết từng hạng mục được trình bày tại các trang chuyên đề.", 
     "本简介按06大能力板块编排，便于业主快速查阅；各专题详见对应页面。"),
    ("TRANG", "第"),
    ("GIỚI THIỆU \\& NĂNG LỰC", "公司概况与资质"),
    ("Company profile \\& credentials", "Company profile \\& credentials"),
    ("Thư ngỏ", "致辞"),
    ("Tầm nhìn và giá trị", "愿景与价值观"),
    ("Hệ sinh thái", "生态系统"),
    ("Pháp nhân \\& lãnh đạo", "法人与领导层"),
    ("GIẢI PHÁP EPC \\& CÔNG NGHỆ", "EPC解决方案与技术"),
    ("EPC, ConTech \\& ESG", "EPC, ConTech \\& ESG"),
    ("Fast-track EPC", "快速推进EPC"),
    ("QA/QC \\& HSE", "QA/QC \\& HSE"),
    ("TÀI CHÍNH \\& NHÂN SỰ", "财务与人力资源"),
    ("Financial capacity \\& people", "Financial capacity \\& people"),
    ("Doanh thu", "营收"),
    ("Bảo lãnh tín dụng", "信用担保"),
    ("Nguồn lực", "人力资源"),
    ("Văn hóa an toàn", "安全文化"),
    ("DỰ ÁN \\& KHÁCH HÀNG", "项目与客户"),
    ("Projects \\& valued partners", "Projects \\& valued partners"),
    ("Danh mục dự án", "项目清单"),
    ("06 case studies", "06 经典案例"),
    ("Chuỗi cung ứng", "供应链"),
    ("Đối tác FDI", "FDI合作伙伴"),
    ("SẢN XUẤT \\& QUẢN TRỊ", "生产与管理"),
    ("PEB \\& project control", "PEB \\& project control"),
    ("Đối tác PEB", "PEB合作伙伴"),
    ("Thiết bị cơ giới", "机械设备"),
    ("Quy trình quản trị FIDIC", "FIDIC管理流程"),
    ("CAM KẾT \\& ĐỒNG HÀNH", "承诺与同行"),
    ("Commitments \\& support", "Commitments \\& support"),
    ("Chứng nhận", "资质认证"),
    ("Phủ sóng thi công", "施工覆盖"),
    ("Chiến lược", "战略"),
    ("Bảo hành \\& liên hệ", "保修与联系"),
    
    # Legal entity box
    ("HỒ SƠ PHÁP NHÂN TÓM TẮT", "法人信息摘要"),
    ("CHI TIẾT CHỨNG NHẬN: TRANG 06", "详细资质认证：第06页"),
    ("Tên doanh nghiệp", "企业名称"),
    ("Mã số thuế", "税务登记号"),
    ("Đại diện pháp luật", "法定代表人"),
    ("Ông PHẠM HUY TÂN", "范辉新 先生"),
    ("Tổng Giám Đốc", "总经理"),
    ("Năng lực", "资质"),
    ("Hạng I BXD", "建设部一级"),
    ("Trụ sở đăng ký", "注册地址"),
    ("Số 39, ngõ 292 Kim Giang, Đại Kim, Hà Nội", "河内市大金郡金江路292巷39号"),
    ("Văn phòng giao dịch", "办公地址"),
    ("Số 19N7B, KĐT Trung Hòa Nhân Chính, Hà Nội", "河内市中和仁政新城区19N7B号"),
    ("Liên hệ", "联系方式"),
    ("Website", "网站"),
    
    # ===== PAGE 03: CEO MESSAGE =====
    ("THÔNG ĐIỆP TỪ TỔNG GIÁM ĐỐC", "总经理致辞"),
    ("Thông Điệp Từ Tổng Giám Đốc", "总经理致辞"),
    ("Leadership Message — Building Trust Through Every Commitment", "Leadership Message — Building Trust Through Every Commitment"),
    ("THÔNG ĐIỆP NHẤT QUÁN CỦA TTC", "TTC的核心理念"),
    ("CHẤT LƯỢNG LÀ DANH DỰ.", "质量即荣誉。"),
    ("AN TOÀN LÀ SINH MỆNH.", "安全即生命。"),
    ("TIẾN ĐỘ LÀ CAM KẾT.", "进度即承诺。"),
    ("Kính gửi Quý Chủ đầu tư, Quý Khách hàng và Quý Đối tác,", "尊敬的投资方、客户及合作伙伴："),
    ("Thay mặt Ban Lãnh đạo và toàn thể cán bộ công nhân viên", "我谨代表公司全体领导班子和员工"),
    (", tôi trân trọng cảm ơn sự tin tưởng và đồng hành của Quý vị trong suốt chặng đường phát triển của TTC.", "，衷心感谢各位一路以来对TTC发展的信任与支持。"),
    ("Hơn một thập kỷ hoạt động trong lĩnh vực xây dựng công nghiệp giúp chúng tôi thấu hiểu rằng: một dự án thành công phải đồng thời đáp ứng", 
     "十余年的工业建筑领域深耕让我们深刻认识到：一个成功的项目必须同时满足"),
    ("chất lượng, an toàn, tiến độ và hiệu quả đầu tư", "质量、安全、进度与投资效益"),
    (". Vì vậy, TTC kiên định với mô hình", "。因此，TTC始终坚持"),
    ("Tổng thầu EPC một đầu mối", "EPC一站式总承包"),
    (", kết hợp Value Engineering, BIM 5D và năng lực quản trị hiện trường theo tiêu chuẩn quốc tế.", "模式，结合价值工程、BIM 5D以及国际标准的现场管理能力。"),
    ("Với hệ sinh thái đối tác PEB công suất 30.000 tấn/năm và đội ngũ kỹ sư thực chiến, chúng tôi cam kết cung cấp giải pháp phù hợp nhất cho từng nhà máy, kiểm soát minh bạch từ thiết kế, thi công đến bàn giao và bảo hành.",
     "凭借年产能30,000吨的PEB合作伙伴生态系统和实战型工程师团队，我们承诺为每座工厂提供最优解决方案，从设计、施工到交付和保修进行全程透明管控。"),
    ("TTC mong muốn không chỉ là một nhà thầu, mà là", "TTC不仅仅是一个承包商，更是"),
    ("đối tác kiến tạo giá trị dài hạn", "共创长期价值的合作伙伴"),
    ("cùng Chủ đầu tư trên mỗi công trình.", "，与业主携手共建每一项工程。"),
    ("Trân trọng,", "此致敬礼，"),
    ("TỔNG GIÁM ĐỐC / CEO", "总经理 / CEO"),
    ("PHẠM HUY TÂN", "范辉新"),
    ("Công ty Cổ phần Công nghệ", "新成功建筑科技"),
    ("Xây dựng Tân Thành Công", "股份公司"),
    ("TÂN THÀNH CÔNG", "新成功"),
    ("ĐẦU MỐI EPC", "EPC一站式"),
    ("TỐI ƯU CHI PHÍ", "成本优化"),
    ("KIẾN TẠO GIÁ TRỊ DÀI HẠN", "共创长期价值"),
    ("BUILDING ENDURING VALUE", "BUILDING ENDURING VALUE"),
    
    # ===== PAGE 04: MILESTONES & CORE VALUES =====
    ("HÀNH TRÌNH PHÁT TRIỂN \\& GIÁ TRỊ CỐT LÕI", "发展历程与核心价值观"),
    ("Hành Trình Kiến Tạo", "建设之路"),
    ("From Mechanical Foundations to a Next-Generation EPC General Contractor", "From Mechanical Foundations to a Next-Generation EPC General Contractor"),
    ("TỪ NỀN TẢNG CƠ KHÍ ĐẾN TỔNG THẦU EPC THẾ HỆ MỚI", "从机械基础到新一代EPC总承包商"),
    ("Một hành trình phát triển được nâng đỡ bởi năng lực thực thi, công nghệ và những giá trị bất biến.", "一段由执行力、技术和永恒价值观支撑的发展之路。"),
    ("KHỞI TẠO", "创立"),
    ("Nền tảng cơ khí chính xác\\\\và kỹ thuật kết cấu thép.", "精密机械基础\\\\与钢结构技术。"),
    ("MỞ RỘNG", "扩张"),
    ("Liên kết sản xuất PEB\\\\và tổng thầu hạ tầng KCN.", "PEB联合生产\\\\与园区基建总承包。"),
    ("BỨT PHÁ", "突破"),
    ("Hạng I Bộ Xây Dựng\\\\và các dự án FDI quy mô lớn.", "建设部一级资质\\\\与大型FDI项目。"),
    ("CHUYỂN ĐỔI", "转型"),
    ("150+ dự án", "150+ 项目"),
    ("20+ tỉnh thành", "覆盖20+省市"),
    ("PEB 30.000 tấn/năm.", "PEB年产30,000吨。"),
    ("VƯƠN TẦM", "腾飞"),
    ("ConTech", "ConTech"),
    ("Mở rộng Đông Nam Á.", "拓展东南亚市场。"),
    ("5 GIÁ TRỊ — NỀN MÓNG CỦA MỌI CÔNG TRÌNH", "五大价值观 — 每项工程的基石"),
    ("The values that sustain every commitment and every project.", "The values that sustain every commitment and every project."),
    ("TÍN", "信"),
    ("TRUST \\& INTEGRITY", "TRUST \\& INTEGRITY"),
    ("TÂM", "心"),
    ("DEDICATION", "DEDICATION"),
    ("TRÍ", "智"),
    ("INNOVATION", "INNOVATION"),
    ("TỐC", "速"),
    ("FAST-TRACK", "FAST-TRACK"),
    ("AN", "安"),
    ("HSE \\& SAFETY", "HSE \\& SAFETY"),
    
    # ===== PAGE 05: ECOSYSTEM =====
    ("HỆ SINH THÁI TỔNG THẦU EPC \\& R\\&D CÔNG NGHỆ", "EPC总承包生态系统与研发技术"),
    ("HỆ SINH THÁI DOANH NGHIỆP \\& R\\&D CÔNG NGHỆ", "企业生态系统与研发技术"),
    ("Hệ Sinh Thái Tổng Thầu EPC", "EPC总承包生态系统"),
    ("Integrated Factory Blueprint \\& AIDC ConTech Collaboration", "Integrated Factory Blueprint \\& AIDC ConTech Collaboration"),
    ("MỘT HỆ SINH THÁI • MỘT HỢP ĐỒNG • MỘT TRÁCH NHIỆM", "一个生态系统 • 一份合同 • 一个责任"),
    ("One integrated ecosystem. One accountable EPC partner from concept to handover.", "One integrated ecosystem. One accountable EPC partner from concept to handover."),
    ("Tối ưu thiết kế và dữ liệu dự án; giảm 10--15\\% khối lượng thép.", "优化设计与项目数据；减少10-15%用钢量。"),
    ("HỆ THỐNG ĐỒNG BỘ TRÊN BIM", "BIM协同系统"),
    ("Điện • HVAC • cấp thoát nước • phòng cháy, phối hợp xuyên suốt một mô hình.", "电气 • 暖通 • 给排水 • 消防，全程协同一个模型。"),
    ("HẠ TẦNG KCN", "园区基建"),
    ("NỀN MÓNG • ĐƯỜNG • THOÁT NƯỚC", "地基 • 道路 • 排水"),
    ("Hạ tầng kỹ thuật sẵn sàng vận hành, kết nối đồng bộ với tổng mặt bằng nhà máy.", "技术基础设施运营就绪，与工厂总平面图同步衔接。"),
    ("SẢN XUẤT KẾT CẤU THÉP", "钢结构生产"),
    ("CNC • SAW • AWS D1.1 • NDT; năng lực cung ứng 30.000 tấn/năm.", "CNC • SAW • AWS D1.1 • NDT；年供应能力30,000吨。"),
    ("One contract • One accountability", "One contract • One accountability"),
    ("KHẢO SÁT", "勘察"),
    ("Hiện trạng \\& yêu cầu", "现状与需求"),
    ("THIẾT KẾ", "设计"),
    ("BIM • AI • VE", "BIM • AI • VE"),
    ("HẠ TẦNG", "基建"),
    ("Nền móng • tiện ích", "地基 • 配套"),
    ("Tích hợp hệ thống", "系统集成"),
    ("Sản xuất • lắp dựng", "生产 • 安装"),
    ("01 ĐẦU MỐI", "01 一站式"),
    ("Một tổng thầu chịu trách nhiệm xuyên suốt từ thiết kế đến bàn giao.", "一个总承包商全程负责，从设计到交付。"),
    ("-15\\% THÉP", "-15\\% 用钢量"),
    ("AI và Value Engineering tối ưu tiết diện, chi phí và tiến độ.", "AI与价值工程优化截面、成本与进度。"),
    ("ZERO ACCIDENT", "零事故"),
    ("Duy trì thành tích", "保持"),
    ("triệu giờ làm việc an toàn liên tục.", "百万安全工时记录。"),
    
    # Ecosystem cards
    ("ĐỐI TÁC SẢN XUẤT KẾT CẤU THÉP PEB", "PEB钢结构生产合作伙伴"),
    ("ĐỐI TÁC CÔNG NGHỆ R\\&D AIDC", "AIDC研发技术合作伙伴"),
    ("CƠ ĐIỆN MEP \\& PCCC CHUYÊN SÂU", "专业机电MEP与消防"),
    ("HẠ TẦNG KỸ THUẬT KCN XANH", "绿色园区技术基建"),
    ("Trách Nhiệm 1 Đầu Mối", "一站式责任"),
    ("Công Nghệ Bảo Trợ", "技术支撑"),
    ("Chủ Động Nguồn Cung", "自主供应"),
    ("Bảo Hành Cấp Tốc", "快速保修"),
    ("Trách Nhiệm Toàn Diện", "全面责任"),
    ("Năng Lực Cung Ứng PEB", "PEB供应能力"),
    ("Tối Ưu Hóa Chi Phí AI", "AI成本优化"),
    ("Chuỗi Giá Trị Tổng Thầu", "总承包价值链"),
    ("ĐỐI TÁC PEB", "PEB合作"),
    
    # ===== PAGE 06: ORG CHART & LEGAL =====
    ("CƠ CẤU TỔ CHỨC \\& CHỨNG NHẬN PHÁP LÝ HẠNG I", "组织架构与一级法律资质认证"),
    ("Cơ Cấu Quản Trị Dự Án", "项目管理架构"),
    
    # ===== PAGE 07: HR CAPABILITIES =====
    ("NĂNG LỰC NHÂN SỰ TRIỂN KHAI EPC", "EPC实施人力资源能力"),
    ("Đội Ngũ Tích Hợp Theo Vòng Đời Dự Án", "项目全生命周期集成团队"),
    ("Integrated Project Team, Clear Accountability \\& Site-Ready Mobilization", "Integrated Project Team, Clear Accountability \\& Site-Ready Mobilization"),
    ("ĐÚNG NGƯỜI • ĐÚNG VAI TRÒ • ĐÚNG THỜI ĐIỂM", "合适的人 • 合适的岗位 • 合适的时间"),
    ("One accountable team mobilized from pre-construction through commissioning and warranty.", "One accountable team mobilized from pre-construction through commissioning and warranty."),
    ("CON NGƯỜI TẠI\\\\ĐIỂM THỰC THI", "执行前线的\\\\团队力量"),
    ("Đội ngũ dự án được tổ chức theo nhiệm vụ, có quyền hạn rõ ràng và một tuyến báo cáo duy nhất.", "项目团队按任务编制，职权明确，实行单线汇报制度。"),
    ("Quyết định kỹ thuật được đưa đến gần hiện trường", "技术决策贴近施工现场"),
    ("VAI TRÒ CHỊU TRÁCH NHIỆM THEO GIAI ĐOẠN", "各阶段责任角色分配"),
    ("CHUẨN BỊ \\& THIẾT KẾ", "准备与设计"),
    ("Đầu mối duy nhất với Chủ đầu tư.", "与业主的唯一对接窗口。"),
    ("Điều phối thiết kế, VE và mô hình.", "协调设计、VE与模型。"),
    ("Khóa phạm vi, tiến độ và ngân sách.", "锁定范围、进度和预算。"),
    ("THI CÔNG HIỆN TRƯỜNG", "现场施工"),
    ("Nguồn lực • mặt bằng • mũi thi công.", "资源 • 场地 • 施工面。"),
    ("Kết cấu • Hạ tầng • MEP • PCCC.", "结构 • 基建 • MEP • 消防。"),
    ("Quyền kiểm soát độc lập.", "独立管控权。"),
    ("BÀN GIAO \\& VẬN HÀNH", "交付与运维"),
    ("Điều phối thử nghiệm liên động.", "协调联动测试。"),
    ("Chuẩn hóa hồ sơ và dữ liệu tài sản.", "标准化档案与资产数据。"),
    ("Tiếp nhận và xử lý kỹ thuật 24/7.", "24/7技术接收与处理。"),
    ("PMO TRỤ SỞ", "总部PMO"),
    ("Portfolio control", "组合管控"),
    ("Single point", "唯一责任人"),
    ("BAN CHỈ HUY", "现场指挥部"),
    ("Daily execution", "日常执行"),
    ("ĐỘI CHUYÊN MÔN", "专业团队"),
    ("Task-based crews", "任务驱动班组"),
    ("QUẢN LÝ \\& KỸ SƯ", "管理人员与工程师"),
    ("CÔNG NHÂN KỸ THUẬT", "技术工人"),
    ("CHỈ HUY \\& GIÁM SÁT", "指挥与监理"),
    ("KỸ SƯ BIM \\& SỐ HÓA", "BIM与数字化工程师"),
    
    # ===== PAGE 08: FINANCIAL GOVERNANCE =====
    ("QUẢN TRỊ TÀI CHÍNH DỰ ÁN \\& KỶ LUẬT DÒNG TIỀN", "项目财务管理与现金流纪律"),
    ("Quản Trị Tài Chính Dự Án \\& Kỷ Luật Dòng Tiền", "项目财务管理与现金流纪律"),
    ("Project Financial Governance • Cost Discipline • Verified \\& Traceable Records", "Project Financial Governance • Cost Discipline • Verified \\& Traceable Records"),
    ("KIỂM SOÁT TỪ QUYẾT ĐỊNH NHẬN THẦU ĐẾN QUYẾT TOÁN CÔNG TRÌNH", "从投标决策到竣工结算的全程管控"),
    ("Mỗi dự án được thiết lập ngân sách độc lập, kiểm soát 4 cổng và đối chiếu định kỳ trước khi huy động nguồn lực.", 
     "每个项目均建立独立预算，实行四道关口管控，在调动资源前进行定期核对。"),
    ("BỐN CỔNG KIỂM SOÁT TÀI CHÍNH DỰ ÁN", "项目财务四道管控关口"),
    ("FOUR FINANCIAL CONTROL GATES", "FOUR FINANCIAL CONTROL GATES"),
    ("THẨM ĐỊNH", "审查"),
    ("HỢP ĐỒNG", "合同"),
    ("NGÂN SÁCH", "预算"),
    ("DỰ ÁN", "项目"),
    ("THỰC HIỆN", "执行"),
    ("NGHIỆM THU", "验收"),
    ("QUYẾT TOÁN", "结算"),
    
    # ===== PAGE 09: CREDIT & HR =====
    ("HẠN MỨC TÍN DỤNG 250 TỶ \\& NGUỒN NHÂN LỰC TINH NHUỆ", "2500亿越盾信用额度与精英人力资源"),
    ("NGÂN HÀNG ĐỐI TÁC TÀI TRỢ DỰ ÁN", "项目融资合作银行"),
    ("NĂNG LỰC PHÁT HÀNH BẢO LÃNH", "担保函签发能力"),
    ("KHỐI QUẢN LÝ \\& KỸ SƯ", "管理层与工程师"),
    ("KHỐI CÔNG NHÂN KỸ THUẬT", "技术工人队伍"),
    
    # ===== PAGE 10: TALENT DEVELOPMENT =====
    ("ĐÀO TẠO NHÂN LỰC \\& VĂN HÓA AN TOÀN", "人才培训与安全文化"),
    
    # ===== PAGE 11-13: PEB, EQUIPMENT, FIDIC =====
    ("CHUỖI ĐỐI TÁC SẢN XUẤT PEB 30.000T", "PEB合作伙伴网络30,000吨"),
    ("ĐỘI XE MÁY CƠ GIỚI HIỆN TRƯỜNG", "现场机械设备车队"),
    ("QUY TRÌNH QUẢN TRỊ DỰ ÁN 8 GIAI ĐOẠN CHUẨN FIDIC", "FIDIC标准八阶段项目管理流程"),
    
    # ===== PAGES 14-19: EPC, CONTECH, ESG, QA =====
    ("GIẢI PHÁP TỔNG THẦU EPC \\& VALUE ENGINEERING", "EPC总承包解决方案与价值工程"),
    ("CONTECH: BIM 5D, AI \\& SMART DIGITAL TWIN", "建筑科技：BIM 5D、AI与智能数字孪生"),
    ("CÔNG TRÌNH XANH ESG \\& SOLAR-READY", "绿色ESG建筑与光伏就绪"),
    ("CHUYỂN ĐỔI SỐ HIỆN TRƯỜNG", "数字化工地管理"),
    ("HỆ THỐNG QA/QC TOÀN DIỆN", "全面质量管理体系"),
    ("AN TOÀN LAO ĐỘNG HSE \\& ZERO ACCIDENT", "HSE劳动安全与零事故"),
    
    # ===== PAGES 20-27: PROJECTS & CASE STUDIES =====
    ("DANH MỤC ĐẠI DỰ ÁN TIÊU BIỂU", "重点大型项目清单"),
    ("DANH MỤC DỰ ÁN CÔNG NGHIỆP TRỌNG ĐIỂM", "重点工业项目清单"),
    
    # ===== PAGES 28-36: CLOSING =====
    ("CHUỖI CUNG ỨNG • KIỂM SOÁT VẬT TƯ", "供应链 • 物资管控"),
    ("CHUỖI CUNG ỨNG KIỂM SOÁT", "受控供应链"),
    ("KHÁCH HÀNG QUỐC TẾ FDI", "国际FDI客户"),
    ("ĐÁNH GIÁ TỪ KHÁCH HÀNG FDI", "FDI客户评价"),
    ("BẰNG KHEN \\& CHỨNG NHẬN NĂNG LỰC", "荣誉证书与资质认证"),
    ("BẢN ĐỒ THI CÔNG \\& 4 CAM KẾT VÀNG", "施工覆盖地图与四大金牌承诺"),
    ("TẦM NHÌN CHIẾN LƯỢC 2026–2030", "2026-2030战略愿景"),
    ("BẢO HÀNH 24 THÁNG \\& ĐỒNG HÀNH 30+ NĂM", "24个月保修与30+年运维服务"),
    ("PHIẾU KHẢO SÁT NHU CẦU DỰ ÁN", "项目需求调查表"),
    ("HOTLINE 24/7 \\& LIÊN HỆ HỢP TÁC", "24/7热线与合作联系"),
    
    # ===== GENERIC VIETNAMESE → CHINESE =====
    ("Trang ", "第"),
    ("trang ", "第"),
]

# Page number translation for headers/footers
PAGE_NUMS = {f"Trang {i:02d}": f"第{i:02d}页" for i in range(1, 37)}


def translate_text(content):
    """Apply all translations to the content."""
    # First do page numbers
    for vi, zh in PAGE_NUMS.items():
        content = content.replace(vi, zh)
    
    # Then do main translations
    for vi, zh in TRANSLATIONS:
        content = content.replace(vi, zh)
    
    return content


def process_section(input_file, output_file, module_suffix="_zh"):
    """Read a section file, translate text, write to new file."""
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Translate content
    translated = translate_text(content)
    
    # Update module docstring to indicate Chinese version
    translated = translated.replace("# -*- coding: utf-8 -*-", "# -*- coding: utf-8 -*-\n# 简体中文版 — Chinese Simplified Translation", 1)
    
    # Remove LEGACY pages (they contain unused Vietnamese names)
    # Remove PAGE_XX_LEGACY definitions
    import re
    translated = re.sub(r'PAGE_\d+_LEGACY\s*=\s*r""".*?"""', '', translated, flags=re.DOTALL)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(translated)
    
    print(f"  ✓ {os.path.basename(input_file)} → {os.path.basename(output_file)}")


def main():
    src_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '05-company-profile')
    dst_dir = os.path.dirname(os.path.abspath(__file__))
    
    sections = [
        ('section1.py', 'section1_zh.py'),
        ('section2.py', 'section2_zh.py'),
        ('section3.py', 'section3_zh.py'),
        ('section4.py', 'section4_zh.py'),
        ('section5.py', 'section5_zh.py'),
        ('section_closing.py', 'section_closing_zh.py'),
    ]
    
    # Note: section6.py content is imported via section_closing in original build
    # Check if section6 is needed
    if os.path.exists(os.path.join(src_dir, 'section6.py')):
        sections.append(('section6.py', 'section6_zh.py'))
    
    print("=" * 60)
    print("TTC Company Profile — Vietnamese → 简体中文 Translation")
    print("=" * 60)
    
    for src_name, dst_name in sections:
        src_path = os.path.join(src_dir, src_name)
        dst_path = os.path.join(dst_dir, dst_name)
        if os.path.exists(src_path):
            process_section(src_path, dst_path)
        else:
            print(f"  ⚠ {src_name} not found, skipping")
    
    print("\n✅ Translation complete!")
    print(f"Output directory: {dst_dir}")
    print("\nNext steps:")
    print("  1. Review translated files")
    print("  2. Run: python3 build_36_pages.py")
    print("  3. Run: xelatex -interaction=nonstopmode 05-company-profile-zh.tex")


if __name__ == "__main__":
    main()
