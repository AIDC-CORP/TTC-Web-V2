# -*- coding: utf-8 -*-
"""Redesigned closing section for the 36-page TTC company profile (pages 28--36)."""

PAGE_28 = r"""% ============================================================
% TRANG 28: CHUỖI CUNG ỨNG KIỂM SOÁT
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{CHUỖI CUNG ỨNG • KIỂM SOÁT VẬT TƯ}{Trang 28}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Chuỗi Cung Ứng Được Kiểm Soát Theo Từng Lô}{Approved sources • Material submittal • CO/CQ/MTC • Lot traceability}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);

  \node[anchor=west,text=TTCBlue,font=\fontsize{15}{17}\selectfont\bfseries]
    at (0,211) {VẬT TƯ CHỈ ĐƯỢC LẮP ĐẶT SAU KHI ĐỦ HỒ SƠ};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{7.2}{8.8}\selectfont]
    at (0,201) {Một luồng phê duyệt thống nhất giúp khóa chất lượng, nguồn gốc và khả năng thay thế trước khi mua hàng.};

  % Cột quy trình 4 cổng kiểm soát
  \fill[TTCDeepNavy,rounded corners=4pt] (0,79) rectangle (62,192);
  \node[anchor=west,text=TTCCyan,font=\fontsize{7}{8.3}\selectfont\bfseries]
    at (7,184) {4 CỔNG KIỂM SOÁT};
  \draw[white!18!gray] (7,178) -- (55,178);

  \foreach \y/\n/\title/\desc in {
    158/01/PHÊ DUYỆT NGUỒN/Nhà sản xuất • mẫu • dữ liệu kỹ thuật,
    134/02/KHÓA HỒ SƠ/CO--CQ • MTC • catalogue • bảo hành,
    110/03/KIỂM TRA ĐẦU VÀO/Nhãn lô • kích thước • tình trạng • thí nghiệm,
    88/04/TRUY XUẤT LẮP ĐẶT/Lô vật tư gắn với khu vực và biên bản nghiệm thu}
  {
    \fill[white,rounded corners=2pt] (7,{\y-8}) rectangle (55,{\y+8});
    \fill[TTCRed] (7,{\y-8}) rectangle (16,{\y+8});
    \node[text=white,font=\fontsize{6.2}{7}\selectfont\bfseries] at (11.5,\y) {\n};
    \node[anchor=north west,text width=34mm,text=TTCBlue,
          font=\fontsize{6.7}{7.8}\selectfont\bfseries] at (19,{\y+5}) {\title};
    \node[anchor=north west,text width=34mm,text=TTCTextMuted,
          font=\fontsize{5.6}{6.7}\selectfont] at (19,{\y-1}) {\desc};
  }

  % Ma trận nhóm vật tư
  \fill[white,rounded corners=4pt] (67,79) rectangle (186,192);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (67,79) rectangle (186,192);
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.4}\selectfont\bfseries]
    at (74,184) {NHÓM VẬT TƯ / THƯƠNG HIỆU THAM CHIẾU};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{5.8}{7}\selectfont]
    at (74,176) {Lựa chọn cuối cùng tuân theo hồ sơ phê duyệt vật liệu của từng dự án.};

  \foreach \y/\n/\name/\brands/\control in {
    157/01/THÉP \& BAO CHE/POSCO • Hòa Phát • BlueScope/MTC • mác thép • lớp mạ,
    134/02/SƠN \& HÓA CHẤT/Jotun • KCC • Sika/Batch • DFT • chứng nhận PCCC,
    111/03/ĐIỆN \& MEP/Schneider • ABB • LS Vina/Catalogue • test • xuất xứ,
    88/04/HVAC \& PCCC/Daikin • Grundfos • Tyco/Submittal • UL--FM khi yêu cầu}
  {
    \fill[TTCLightBlue,rounded corners=2pt] (73,{\y-9}) rectangle (180,{\y+9});
    \node[anchor=west,text=TTCRed,font=\fontsize{6.4}{7.5}\selectfont\bfseries]
      at (78,{\y+4}) {\n};
    \node[anchor=west,text=TTCBlue,font=\fontsize{7}{8.2}\selectfont\bfseries]
      at (91,{\y+4}) {\name};
    \node[anchor=west,text=TTCTextDark,font=\fontsize{6.2}{7.3}\selectfont]
      at (91,{\y-2}) {\brands};
    \node[anchor=east,text=TTCTextMuted,font=\fontsize{5.6}{6.7}\selectfont]
      at (176,{\y-7}) {Kiểm soát: \control};
  }

  % Ba lớp bảo chứng
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.4}\selectfont\bfseries]
    at (0,68) {BA LỚP BẢO CHỨNG TRƯỚC KHI LẮP ĐẶT};
  \foreach \xa/\xb/\n/\title/\desc in {
    0/58/01/ĐÚNG NGUỒN/Hồ sơ phê duyệt khớp nhà sản xuất và xuất xứ,
    64/122/02/ĐÚNG CHẤT LƯỢNG/Chỉ tiêu kỹ thuật khớp mẫu và tiêu chuẩn dự án,
    128/186/03/ĐÚNG VỊ TRÍ/Mỗi lô gắn với biên bản và khu vực sử dụng}
  {
    \fill[white,rounded corners=3pt] (\xa,25) rectangle (\xb,60);
    \draw[TTCBorder,rounded corners=3pt] (\xa,25) rectangle (\xb,60);
    \node[anchor=west,text=TTCRed,font=\fontsize{7}{8}\selectfont\bfseries]
      at ({\xa+6},52) {\n};
    \node[anchor=west,text=TTCBlue,font=\fontsize{7.4}{8.7}\selectfont\bfseries]
      at ({\xa+17},52) {\title};
    \node[anchor=north west,text width=46mm,text=TTCTextMuted,
          font=\fontsize{6.2}{7.5}\selectfont] at ({\xa+6},43) {\desc};
  }

  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,16);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.3}{7.5}\selectfont\bfseries]
    at (7,8) {MATERIAL ASSURANCE};
  \node[anchor=east,text=white,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (179,8) {APPROVED SOURCE → VERIFIED LOT → TRACEABLE INSTALLATION};
\end{tikzpicture}
\end{minipage}
\newpage
"""


PAGE_29 = r"""% ============================================================
% TRANG 29: HỆ SINH THÁI CÔNG TRÌNH THEO NGÀNH
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{HỆ SINH THÁI DỰ ÁN • 6 NHÓM NGÀNH}{Trang 29}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Sáu Hệ Công Trình — Một Năng Lực Tích Hợp}{Representative sectors • Different operating demands • One coordinated EPC workflow}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);
  \node[anchor=west,text=TTCBlue,font=\fontsize{15}{17}\selectfont\bfseries]
    at (0,211) {THIẾT KẾ BẮT ĐẦU TỪ CÁCH NHÀ MÁY VẬN HÀNH};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{7.2}{8.8}\selectfont]
    at (0,201) {Mỗi nhóm ngành có một rủi ro cốt lõi; giải pháp kết cấu, MEP và trình tự thi công phải trả lời đúng rủi ro đó.};

  % Hàng 1
  \begin{scope}
    \clip[rounded corners=3pt] (0,132) rectangle (59,190);
    \node[inner sep=0pt] at (29.5,165) {\includegraphics[width=60mm]{../../public/project-assets/japfa.jpg}};
    \fill[TTCDeepNavy,opacity=.9] (0,132) rectangle (59,151);
  \end{scope}
  \draw[TTCBorder,rounded corners=3pt] (0,132) rectangle (59,190);
  \node[anchor=west,text=white,font=\fontsize{7.5}{8.8}\selectfont\bfseries] at (5,144) {THỰC PHẨM \& AGRIFOOD};
  \node[anchor=west,text=white!75!gray,font=\fontsize{5.8}{7}\selectfont] at (5,137) {Silo • process • vệ sinh • PCCC};

  \begin{scope}
    \clip[rounded corners=3pt] (63.5,132) rectangle (122.5,190);
    \node[inner sep=0pt] at (93,167) {\includegraphics[height=41mm]{../../public/project-assets/daeyun.jpg}};
    \fill[TTCDeepNavy,opacity=.9] (63.5,132) rectangle (122.5,151);
  \end{scope}
  \draw[TTCBorder,rounded corners=3pt] (63.5,132) rectangle (122.5,190);
  \node[anchor=west,text=white,font=\fontsize{7.5}{8.8}\selectfont\bfseries] at (68.5,144) {ĐIỆN TỬ \& PHÒNG SẠCH};
  \node[anchor=west,text=white!75!gray,font=\fontsize{5.8}{7}\selectfont] at (68.5,137) {HVAC • ESD • kiểm soát môi trường};

  \begin{scope}
    \clip[rounded corners=3pt] (127,132) rectangle (186,190);
    \node[inner sep=0pt] at (156.5,168) {\includegraphics[height=41mm]{../../public/project-assets/foxcon.png}};
    \fill[TTCDeepNavy,opacity=.9] (127,132) rectangle (186,151);
  \end{scope}
  \draw[TTCBorder,rounded corners=3pt] (127,132) rectangle (186,190);
  \node[anchor=west,text=white,font=\fontsize{7.5}{8.8}\selectfont\bfseries] at (132,144) {NHÀ XƯỞNG ĐIỆN TỬ};
  \node[anchor=west,text=white!75!gray,font=\fontsize{5.8}{7}\selectfont] at (132,137) {Giao diện MEP • lắp dựng theo zone};

  % Hàng 2
  \begin{scope}
    \clip[rounded corners=3pt] (0,69) rectangle (59,127);
    \node[inner sep=0pt] at (29.5,103) {\includegraphics[height=42mm]{../../public/project-assets/songhong7.jpg}};
    \fill[TTCDeepNavy,opacity=.9] (0,69) rectangle (59,88);
  \end{scope}
  \draw[TTCBorder,rounded corners=3pt] (0,69) rectangle (59,127);
  \node[anchor=west,text=white,font=\fontsize{7.5}{8.8}\selectfont\bfseries] at (5,81) {DỆT MAY NHIỀU TẦNG};
  \node[anchor=west,text=white!75!gray,font=\fontsize{5.8}{7}\selectfont] at (5,74) {Sàn tải nặng • nhịp lớn • thoát nạn};

  \begin{scope}
    \clip[rounded corners=3pt] (63.5,69) rectangle (122.5,127);
    \node[inner sep=0pt] at (93,104) {\includegraphics[width=60mm]{../../public/project-assets/yusen.jpg}};
    \fill[TTCDeepNavy,opacity=.9] (63.5,69) rectangle (122.5,88);
  \end{scope}
  \draw[TTCBorder,rounded corners=3pt] (63.5,69) rectangle (122.5,127);
  \node[anchor=west,text=white,font=\fontsize{7.5}{8.8}\selectfont\bfseries] at (68.5,81) {LOGISTICS \& KHO VẬN};
  \node[anchor=west,text=white!75!gray,font=\fontsize{5.8}{7}\selectfont] at (68.5,74) {Sàn phẳng • dock • luồng xe hàng};

  \begin{scope}
    \clip[rounded corners=3pt] (127,69) rectangle (186,127);
    \node[inner sep=0pt] at (156.5,104) {\includegraphics[width=60mm]{../../public/project-assets/sumidenso.jpg}};
    \fill[TTCDeepNavy,opacity=.9] (127,69) rectangle (186,88);
  \end{scope}
  \draw[TTCBorder,rounded corners=3pt] (127,69) rectangle (186,127);
  \node[anchor=west,text=white,font=\fontsize{7.5}{8.8}\selectfont\bfseries] at (132,81) {LINH KIỆN Ô TÔ};
  \node[anchor=west,text=white!75!gray,font=\fontsize{5.8}{7}\selectfont] at (132,74) {Chất lượng ổn định • bàn giao theo gate};

  % Ba năng lực dùng chung
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.3}\selectfont\bfseries]
    at (0,58) {NĂNG LỰC XUYÊN SUỐT MỌI NHÓM NGÀNH};
  \foreach \xa/\xb/\title/\desc in {
    0/58/COORDINATION/Khóa giao diện kiến trúc • kết cấu • MEP,
    64/122/CONSTRUCTABILITY/Thiết kế bám biện pháp và trình tự thi công,
    128/186/HANDOVER/Đủ bằng chứng trước mỗi bước chuyển giao}
  {
    \fill[TTCLightBlue,rounded corners=3pt] (\xa,20) rectangle (\xb,50);
    \node[anchor=west,text=TTCBlue,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
      at ({\xa+6},41) {\title};
    \node[anchor=north west,text width=46mm,text=TTCTextMuted,
          font=\fontsize{6.1}{7.3}\selectfont] at ({\xa+6},34) {\desc};
  }
  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,12);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.2}{7.4}\selectfont\bfseries] at (7,6) {SECTOR FIT};
  \node[anchor=east,text=white,font=\fontsize{7}{8.3}\selectfont\bfseries]
    at (179,6) {GIẢI PHÁP ĐƯỢC THIẾT KẾ THEO NHU CẦU VẬN HÀNH};
\end{tikzpicture}
\end{minipage}
\newpage
"""


PAGE_30 = r"""% ============================================================
% TRANG 30: BỘ HỒ SƠ BÀN GIAO
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{BẰNG CHỨNG BÀN GIAO • CLOSEOUT DOSSIER}{Trang 30}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Bộ Hồ Sơ Bàn Giao Có Thể Truy Xuất}{Evidence chain from approved material to as-built and commissioning records}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);
  \node[anchor=west,text=TTCBlue,font=\fontsize{15}{17}\selectfont\bfseries]
    at (0,211) {BÀN GIAO CÔNG TRÌNH — ĐỒNG THỜI BÀN GIAO BẰNG CHỨNG};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{7.2}{8.8}\selectfont]
    at (0,201) {Mỗi bước chỉ được đóng khi hồ sơ kỹ thuật, biên bản và bằng chứng hiện trường đã khớp nhau.};

  % Dòng 5 cổng bằng chứng
  \fill[TTCLightBlue,rounded corners=4pt] (0,139) rectangle (186,190);
  \draw[TTCBorder,rounded corners=4pt] (0,139) rectangle (186,190);
  \draw[TTCBlue!40!white,line width=.8pt] (18,165) -- (168,165);
  \foreach \x/\n/\title in {
    18/01/VẬT TƯ,
    55.5/02/SHOP DRAWING,
    93/03/NGHIỆM THU,
    130.5/04/AS-BUILT,
    168/05/COMMISSIONING}
  {
    \fill[white] (\x,165) circle (5mm);
    \draw[TTCBlue,line width=.8pt] (\x,165) circle (5mm);
    \node[text=TTCBlue,font=\fontsize{6}{7}\selectfont\bfseries] at (\x,165) {\n};
    \node[anchor=north,align=center,text width=29mm,text=TTCBlue,
          font=\fontsize{6.5}{7.7}\selectfont\bfseries] at (\x,155) {\title};
  }
  \fill[TTCRed] (18,165) circle (3.5mm);
  \node[text=white,font=\fontsize{5.8}{6.8}\selectfont\bfseries] at (18,165) {01};

  % Minh họa tập hồ sơ
  \fill[TTCDeepNavy,rounded corners=4pt] (0,48) rectangle (70,130);
  \node[anchor=west,text=TTCCyan,font=\fontsize{7}{8.2}\selectfont\bfseries]
    at (7,121) {CLOSEOUT DOSSIER};
  \fill[white!15!gray,rounded corners=2pt] (15,61) rectangle (61,111);
  \fill[white!45!gray,rounded corners=2pt] (12,65) rectangle (58,115);
  \fill[white,rounded corners=2pt] (9,69) rectangle (55,119);
  \fill[TTCRed] (9,112) rectangle (55,119);
  \node[anchor=west,text=TTCBlue,font=\fontsize{7.4}{8.6}\selectfont\bfseries]
    at (15,103) {HỒ SƠ HOÀN CÔNG};
  \draw[TTCBorder] (15,96) -- (49,96);
  \draw[TTCBorder] (15,90) -- (49,90);
  \draw[TTCBorder] (15,84) -- (42,84);
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{5.8}{7}\selectfont]
    at (15,76) {CDE index • revision • approval};
  \node[anchor=west,text=white,font=\fontsize{6.1}{7.3}\selectfont\bfseries]
    at (7,55) {01 BỘ CHỈ MỤC • NHIỀU NHÓM HỒ SƠ};

  % Checklist bên phải
  \fill[white,rounded corners=4pt] (76,48) rectangle (186,130);
  \draw[TTCBorder,rounded corners=4pt] (76,48) rectangle (186,130);
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.4}\selectfont\bfseries]
    at (83,120) {CẤU TRÚC BÀN GIAO TỐI THIỂU};
  \foreach \y/\n/\title/\desc in {
    104/01/HỒ SƠ VẬT LIỆU/Approved submittal • CO/CQ • MTC • test,
    90/02/HỒ SƠ THI CÔNG/ITP • checklist • biên bản nghiệm thu,
    76/03/HỒ SƠ HOÀN CÔNG/Bản vẽ as-built • revision • xác nhận,
    62/04/HỒ SƠ VẬN HÀNH/O\&M manual • bảo hành • danh mục thiết bị}
  {
    \fill[TTCLightBlue,rounded corners=2pt] (83,{\y-6}) rectangle (179,{\y+6});
    \node[anchor=west,text=TTCRed,font=\fontsize{6.2}{7.2}\selectfont\bfseries]
      at (88,\y) {\n};
    \node[anchor=west,text=TTCBlue,font=\fontsize{6.6}{7.7}\selectfont\bfseries]
      at (101,{\y+2}) {\title};
    \node[anchor=west,text=TTCTextMuted,font=\fontsize{5.6}{6.7}\selectfont]
      at (101,{\y-4}) {\desc};
  }

  % Nguyên tắc phát hành
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.3}\selectfont\bfseries]
    at (0,37) {NGUYÊN TẮC PHÁT HÀNH};
  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,29);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.2}{7.4}\selectfont\bfseries]
    at (7,20) {RELEASE CONTROL};
  \node[anchor=west,text=white,font=\fontsize{9}{10.5}\selectfont\bfseries]
    at (7,10) {ĐÃ KIỂM TRA → ĐỦ BẰNG CHỨNG → ĐÃ DUYỆT → TRUY XUẤT ĐƯỢC};
  \node[anchor=east,text=white!70!gray,font=\fontsize{6.1}{7.3}\selectfont]
    at (179,20) {Một phiên bản hiệu lực • Một chỉ mục bàn giao};
\end{tikzpicture}
\end{minipage}
\newpage
"""


PAGE_31 = r"""% ============================================================
% TRANG 31: NỀN TẢNG PHÁP LÝ VÀ HỆ QUẢN TRỊ
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{NỀN TẢNG PHÁP LÝ • HỆ QUẢN TRỊ}{Trang 31}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Hồ Sơ Pháp Lý Sẵn Sàng Cho Thẩm Định}{Corporate identity • Construction capability • ISO systems • Key-person credentials}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);
  \node[anchor=west,text=TTCBlue,font=\fontsize{15}{17}\selectfont\bfseries]
    at (0,211) {MỘT BỘ HỒ SƠ — BỐN LỚP NĂNG LỰC CÓ THỂ ĐỐI CHIẾU};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{7.2}{8.8}\selectfont]
    at (0,201) {Thông tin pháp nhân, phạm vi hoạt động và hệ thống quản trị được tổ chức theo đúng logic của vòng thẩm định nhà thầu.};

  % Hồ sơ pháp nhân lớn bên trái
  \fill[TTCDeepNavy,rounded corners=4pt] (0,57) rectangle (67,191);
  \node[anchor=west,text=TTCCyan,font=\fontsize{7}{8.3}\selectfont\bfseries]
    at (7,182) {CORPORATE IDENTITY};
  \node[anchor=north west,text width=53mm,text=white,
        font=\fontsize{12}{14}\selectfont\bfseries]
    at (7,169) {CÔNG TY CỔ PHẦN\\CÔNG NGHỆ XÂY DỰNG\\TÂN THÀNH CÔNG};
  \draw[white!20!gray] (7,125) -- (60,125);
  \node[anchor=north west,text width=53mm,text=white!82!gray,
        font=\fontsize{6.5}{8.2}\selectfont]
    at (7,116) {\textbf{Tên viết tắt:} TTC JSC\\[2mm]
                 \textbf{Mã số thuế:} 0107090447\\[2mm]
                 \textbf{Trụ sở:} Hà Nội, Việt Nam\\[2mm]
                 \textbf{Lĩnh vực:} Tổng thầu công nghiệp, kết cấu thép, cơ điện và quản lý dự án};
  \fill[TTCRed,rounded corners=2pt] (7,67) rectangle (60,82);
  \node[text=white,font=\fontsize{7}{8.2}\selectfont\bfseries] at (33.5,74.5)
    {LEGAL • TRACEABLE • BID-READY};

  % Bốn lớp hồ sơ bên phải
  \foreach \y/\n/\title/\desc in {
    166/01/NĂNG LỰC HOẠT ĐỘNG XÂY DỰNG HẠNG II/Phạm vi công việc được đối chiếu trực tiếp theo chứng chỉ còn hiệu lực; bản sao cung cấp trong hồ sơ pháp lý.,
    134/02/HỆ THỐNG QUẢN LÝ ISO/ISO 9001 • ISO 14001 • ISO 45001 được trình bày cùng phạm vi áp dụng và kỳ đánh giá.,
    102/03/NHÂN SỰ CHỦ CHỐT/Chứng chỉ hành nghề của Giám đốc dự án • Chỉ huy trưởng • chủ trì thiết kế.,
    70/04/HỒ SƠ THƯƠNG MẠI/Đăng ký doanh nghiệp • thuế • ngân hàng • bảo hiểm • biểu mẫu hồ sơ dự thầu.}
  {
    \fill[white,rounded corners=3pt] (73,{\y-13}) rectangle (186,{\y+13});
    \draw[TTCBorder,rounded corners=3pt] (73,{\y-13}) rectangle (186,{\y+13});
    \fill[TTCLightBlue,rounded corners=2pt] (79,{\y-7}) rectangle (94,{\y+7});
    \node[text=TTCRed,font=\fontsize{7}{8}\selectfont\bfseries] at (86.5,\y) {\n};
    \node[anchor=west,text=TTCBlue,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
      at (101,{\y+5}) {\title};
    \node[anchor=north west,text width=76mm,text=TTCTextMuted,
          font=\fontsize{6.1}{7.4}\selectfont] at (101,{\y-1}) {\desc};
  }

  % Checklist hồ sơ thầu
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.3}\selectfont\bfseries]
    at (0,46) {BỘ CHỈ MỤC PHỤC VỤ SƠ TUYỂN / DỰ THẦU};
  \foreach \xa/\xb/\label in {
    0/34/PHÁP NHÂN,
    38/72/NĂNG LỰC,
    76/110/ISO,
    114/148/NHÂN SỰ,
    152/186/TÀI CHÍNH}
  {
    \fill[TTCLightBlue,rounded corners=2pt] (\xa,20) rectangle (\xb,38);
    \node[text=TTCBlue,font=\fontsize{6.6}{7.8}\selectfont\bfseries]
      at ({(\xa+\xb)/2},29) {\label};
  }
  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,12);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.2}{7.4}\selectfont\bfseries] at (7,6) {DUE DILIGENCE};
  \node[anchor=east,text=white,font=\fontsize{7}{8.3}\selectfont\bfseries]
    at (179,6) {THÔNG TIN CÓ CHỈ MỤC • BẢN SAO CÓ KIỂM SOÁT • DỄ ĐỐI CHIẾU};
\end{tikzpicture}
\end{minipage}
\newpage
"""


PAGE_32 = r"""% ============================================================
% TRANG 32: BẢN ĐỒ HIỆN DIỆN DỰ ÁN
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{BẢN ĐỒ HIỆN DIỆN • CỤM CÔNG NGHIỆP}{Trang 32}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Hiện Diện Theo Các Hành Lang Công Nghiệp Trọng Điểm}{Northern manufacturing belt • Central corridor • Southern FDI and logistics cluster}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);
  \node[anchor=west,text=TTCBlue,font=\fontsize{15}{17}\selectfont\bfseries]
    at (0,211) {BẢN ĐỒ KINH NGHIỆM TRIỂN KHAI TẠI VIỆT NAM};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{7.2}{8.8}\selectfont]
    at (0,201) {Các điểm nhấn phản ánh cụm địa bàn xuất hiện trong danh mục dự án; không biểu diễn số lượng dự án theo tỷ lệ.};

  % Khung bản đồ
  \fill[white,rounded corners=4pt] (0,24) rectangle (103,191);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,24) rectangle (103,191);
  \node[inner sep=0pt] at (51.5,107.5)
    {\includegraphics[height=164mm,trim=150 10 150 10,clip]{../../public/project-assets/vietnam-provinces.pdf}};

  % Highlight các cụm, vị trí chỉ báo gần đúng trên bản đồ nền
  \fill[TTCRed,opacity=.16] (62,151) circle (12mm);
  \draw[TTCRed,line width=1pt] (62,151) circle (6mm);
  \fill[TTCRed] (62,151) circle (2.2mm);
  \node[anchor=west,text=TTCRed,font=\fontsize{6.5}{7.6}\selectfont\bfseries] at (70,157) {CỤM BẮC BỘ};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{5.5}{6.6}\selectfont] at (70,150) {Hà Nội • Vĩnh Phúc • Bắc Ninh};

  \fill[TTCBlue,opacity=.14] (62,94) circle (10mm);
  \draw[TTCBlue,line width=1pt] (62,94) circle (5mm);
  \fill[TTCBlue] (62,94) circle (2mm);
  \node[anchor=west,text=TTCBlue,font=\fontsize{6.5}{7.6}\selectfont\bfseries] at (69,100) {HÀNH LANG MIỀN TRUNG};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{5.5}{6.6}\selectfont] at (69,93) {Đà Nẵng • Quảng Nam • duyên hải};

  \fill[TTCCyan,opacity=.16] (51,51) circle (10mm);
  \draw[TTCCyan,line width=1pt] (51,51) circle (5mm);
  \fill[TTCCyan] (51,51) circle (2mm);
  \node[anchor=west,text=TTCBlue,font=\fontsize{6.5}{7.6}\selectfont\bfseries] at (59,57) {CỤM PHÍA NAM};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{5.5}{6.6}\selectfont] at (59,50) {Bình Dương • TP.HCM • Hậu Giang};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{4.8}{5.8}\selectfont]
    at (5,29) {Bản đồ nền CC0: Wikimedia Commons / Thomson Walt};

  % Ba cụm thông tin bên phải
  \fill[TTCDeepNavy,rounded corners=4pt] (109,133) rectangle (186,191);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.2}{7.4}\selectfont\bfseries]
    at (116,183) {01 • TRỌNG TÂM HIỆN TẠI};
  \node[anchor=north west,text width=62mm,text=white,
        font=\fontsize{9.5}{11}\selectfont\bfseries] at (116,173) {VÀNH ĐAI CÔNG NGHIỆP BẮC BỘ};
  \node[anchor=north west,text width=62mm,text=white!75!gray,
        font=\fontsize{6.2}{7.6}\selectfont] at (116,153) {Mật độ dự án cao quanh các KCN Hà Nội, Vĩnh Phúc, Bắc Ninh, Bắc Giang, Hải Dương, Hải Phòng và Nam Định.};

  \fill[TTCLightBlue,rounded corners=4pt] (109,73) rectangle (186,127);
  \node[anchor=west,text=TTCRed,font=\fontsize{6.2}{7.4}\selectfont\bfseries]
    at (116,119) {02 • NĂNG LỰC CƠ ĐỘNG};
  \node[anchor=north west,text width=62mm,text=TTCBlue,
        font=\fontsize{8.5}{10}\selectfont\bfseries] at (116,109) {ĐỘI NGŨ THEO CỤM DỰ ÁN};
  \node[anchor=north west,text width=62mm,text=TTCTextMuted,
        font=\fontsize{6.2}{7.6}\selectfont] at (116,92) {Bố trí quản lý dự án, QA/QC và HSE theo địa bàn; kế hoạch huy động thiết bị được khóa theo từng gói công việc.};

  \fill[white,rounded corners=4pt] (109,24) rectangle (186,67);
  \draw[TTCBorder,rounded corners=4pt] (109,24) rectangle (186,67);
  \node[anchor=west,text=TTCBlue,font=\fontsize{6.2}{7.4}\selectfont\bfseries]
    at (116,59) {03 • HƯỚNG MỞ RỘNG};
  \node[anchor=north west,text width=62mm,text=TTCTextDark,
        font=\fontsize{6.3}{7.7}\selectfont] at (116,49) {Mở rộng có chọn lọc tại miền Trung và phía Nam, ưu tiên dự án có yêu cầu EPC công nghiệp, logistics và nhà máy công nghệ cao.};

  \fill[TTCDeepNavy,rounded corners=3pt] (109,0) rectangle (186,16);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.1}{7.2}\selectfont\bfseries]
    at (116,8) {PROJECT FOOTPRINT};
  \node[anchor=east,text=white,font=\fontsize{6.5}{7.7}\selectfont\bfseries]
    at (179,8) {3 CỤM TRIỂN KHAI};
\end{tikzpicture}
\end{minipage}
\newpage
"""


PAGE_33 = r"""% ============================================================
% TRANG 33: LỘ TRÌNH 2026--2030
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{LỘ TRÌNH 2026--2030 • TĂNG TRƯỞNG CÓ KIỂM SOÁT}{Trang 33}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Lộ Trình Phát Triển Chọn Lọc Và Bền Vững}{Controlled development • Repeat clients • High-tech capability • Delivery discipline}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);
  \node[anchor=west,text=TTCBlue,font=\fontsize{15}{17}\selectfont\bfseries]
    at (0,211) {MỞ RỘNG SAU KHI NĂNG LỰC QUẢN TRỊ ĐÃ SẴN SÀNG};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{7.2}{8.8}\selectfont]
    at (0,201) {Ưu tiên năng lực bàn giao, khách hàng lặp lại và chất lượng quản trị trước tốc độ mở rộng.};

  % Ba horizon cards
  \foreach \xa/\xb/\year/\value/\focus/\desc in {
    0/58/2026/CHUẨN HÓA/CỦNG CỐ NỀN TẢNG/Môi trường dữ liệu chung • kiểm soát chi phí • củng cố năng lực miền Bắc,
    64/122/2027--2028/CHỌN LỌC/MỞ RỘNG NĂNG LỰC/Dự án công nghệ cao • phòng sạch • khách hàng lặp lại,
    128/186/2029--2030/BỀN VỮNG/PHÁT TRIỂN CÓ ĐIỀU KIỆN/Mở rộng địa bàn có kiểm soát • ưu tiên năng lực tích hợp}
  {
    \fill[white,rounded corners=4pt] (\xa,68) rectangle (\xb,190);
    \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (\xa,68) rectangle (\xb,190);
    \fill[TTCDeepNavy,rounded corners=4pt] (\xa,165) rectangle (\xb,190);
    \node[anchor=west,text=TTCCyan,font=\fontsize{7}{8.3}\selectfont\bfseries]
      at ({\xa+6},181) {\year};
    \node[anchor=west,text=white,font=\fontsize{13}{15}\selectfont\bfseries]
      at ({\xa+6},171) {\value};
    \fill[TTCRed] ({\xa+6},153) rectangle ({\xa+22},155);
    \node[anchor=west,text=TTCBlue,font=\fontsize{7.6}{9}\selectfont\bfseries]
      at ({\xa+6},143) {\focus};
    \node[anchor=north west,text width=46mm,text=TTCTextMuted,
          font=\fontsize{6.3}{7.7}\selectfont] at ({\xa+6},133) {\desc};
    \node[anchor=south west,text width=46mm,text=TTCTextDark,
          font=\fontsize{6.1}{7.5}\selectfont] at ({\xa+6},78)
      {\textbf{Điều kiện chuyển bước:} nguồn lực chủ chốt, rủi ro hợp đồng và khả năng bàn giao đạt ngưỡng kiểm soát nội bộ.};
  }

  % Các ưu tiên cụ thể để lấp đầy khoảng giữa và tăng khả năng ghi nhớ
  \foreach \y/\label in {116/Dữ liệu được chuẩn hóa,104/Ngân sách cơ sở,92/Năng lực miền Bắc}{
    \fill[TTCRed] (6,\y) circle (1.2mm);
    \node[anchor=west,text=TTCTextDark,font=\fontsize{6.2}{7.4}\selectfont] at (11,\y) {\label};
  }
  \foreach \y/\label in {116/Phòng sạch \& công nghệ cao,104/Khách hàng lặp lại,92/Quản trị đa dự án}{
    \fill[TTCRed] (70,\y) circle (1.2mm);
    \node[anchor=west,text=TTCTextDark,font=\fontsize{6.2}{7.4}\selectfont] at (75,\y) {\label};
  }
  \foreach \y/\label in {116/Tổng thầu chọn lọc,104/Địa bàn có điều kiện,92/Chuỗi cung ứng xanh}{
    \fill[TTCRed] (134,\y) circle (1.2mm);
    \node[anchor=west,text=TTCTextDark,font=\fontsize{6.2}{7.4}\selectfont] at (139,\y) {\label};
  }

  % Bốn bộ lọc tăng trưởng
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.3}\selectfont\bfseries]
    at (0,57) {BỐN BỘ LỌC TRƯỚC KHI NHẬN THÊM QUY MÔ};
  \foreach \xa/\xb/\n/\label in {
    0/43.5/01/PHẠM VI PHÙ HỢP,
    47.5/91/02/NGUỒN LỰC SẴN SÀNG,
    95/138.5/03/RỦI RO HỢP ĐỒNG,
    142.5/186/04/KHẢ NĂNG BÀN GIAO}
  {
    \fill[TTCLightBlue,rounded corners=3pt] (\xa,25) rectangle (\xb,49);
    \node[anchor=west,text=TTCRed,font=\fontsize{6}{7}\selectfont\bfseries]
      at ({\xa+5},40) {\n};
    \node[anchor=west,text=TTCBlue,font=\fontsize{6.2}{7.4}\selectfont\bfseries]
      at ({\xa+5},32) {\label};
  }
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{5.4}{6.5}\selectfont\itshape]
    at (0,14) {Lộ trình mang tính định hướng; từng bước mở rộng phụ thuộc năng lực, nhu cầu thị trường và phê duyệt quản trị.};
  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,10);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6}{7.2}\selectfont\bfseries] at (7,5) {CONTROLLED GROWTH};
  \node[anchor=east,text=white,font=\fontsize{6.8}{8}\selectfont\bfseries]
    at (179,5) {CHẤT LƯỢNG BÀN GIAO QUAN TRỌNG HƠN TỐC ĐỘ};
\end{tikzpicture}
\end{minipage}
\newpage
"""


PAGE_34 = r"""% ============================================================
% TRANG 34: BẢO HÀNH VÀ HẬU MÃI
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{BẢO HÀNH • HẬU MÃI • HỖ TRỢ VẬN HÀNH}{Trang 34}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Hỗ Trợ Sau Bàn Giao Theo Một Đầu Mối}{Centralized intake • Contract-based response • Field verification • Closed-loop records}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);
  \node[anchor=west,text=TTCBlue,font=\fontsize{15}{17}\selectfont\bfseries]
    at (0,211) {BÀN GIAO KHÔNG PHẢI LÀ ĐIỂM KẾT THÚC};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{7.2}{8.8}\selectfont]
    at (0,201) {Mọi yêu cầu sau bàn giao được ghi nhận, phân loại, xử lý và đóng hồ sơ bằng cùng một chuỗi trách nhiệm.};

  % Hero warranty promise
  \fill[TTCDeepNavy,rounded corners=4pt] (0,141) rectangle (54,190);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.4}{7.6}\selectfont\bfseries]
    at (7,181) {ĐIỀU KIỆN BẢO HÀNH};
  \node[anchor=center,align=center,text=white,font=\fontsize{18}{20}\selectfont\bfseries]
    at (27,163) {THEO\\HỢP ĐỒNG};
  \node[anchor=center,align=center,text width=42mm,text=white!72!gray,font=\fontsize{5.5}{6.7}\selectfont]
    at (27,148) {Thời hạn và phạm vi xác lập trong từng hợp đồng};

  \fill[TTCLightBlue,rounded corners=4pt] (60,141) rectangle (186,190);
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.3}\selectfont\bfseries]
    at (67,181) {MỘT ĐẦU MỐI TIẾP NHẬN — MỘT HỒ SƠ THEO DÕI};
  \node[anchor=north west,text width=104mm,text=TTCTextDark,
        font=\fontsize{6.7}{8.2}\selectfont] at (67,171)
    {Hotline và email kỹ thuật là kênh tiếp nhận tập trung. Thời gian phản hồi, kiểm tra hiện trường và khắc phục được xác định theo mức độ ưu tiên, điều kiện hợp đồng và khả năng tiếp cận công trình.};
  \node[anchor=west,text=TTCRed,font=\fontsize{6.4}{7.6}\selectfont\bfseries]
    at (67,149) {KHÔNG CAM KẾT MƠ HỒ • KHÔNG ĐÓNG SỰ CỐ KHI CHƯA CÓ XÁC NHẬN};

  % Quy trình bốn bước
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.3}\selectfont\bfseries]
    at (0,130) {QUY TRÌNH HỖ TRỢ SAU BÀN GIAO};
  \foreach \xa/\xb/\n/\title/\desc in {
    0/42/01/TIẾP NHẬN/Ghi nhận hiện tượng • ảnh • mức độ ảnh hưởng,
    48/90/02/PHÂN LOẠI/Xác định phạm vi bảo hành và mức ưu tiên,
    96/138/03/KIỂM TRA/Đánh giá từ xa hoặc bố trí kiểm tra hiện trường,
    144/186/04/ĐÓNG HỒ SƠ/Khắc phục • nghiệm thu • cập nhật lịch sử}
  {
    \fill[white,rounded corners=3pt] (\xa,78) rectangle (\xb,121);
    \draw[TTCBorder,rounded corners=3pt] (\xa,78) rectangle (\xb,121);
    \fill[TTCRed,rounded corners=1pt] ({\xa+5},109) rectangle ({\xa+16},118);
    \node[text=white,font=\fontsize{6}{7}\selectfont\bfseries] at ({\xa+10.5},113.5) {\n};
    \node[anchor=west,text=TTCBlue,font=\fontsize{7}{8.2}\selectfont\bfseries]
      at ({\xa+5},101) {\title};
    \node[anchor=north west,text width=31mm,text=TTCTextMuted,
          font=\fontsize{5.9}{7.2}\selectfont] at ({\xa+5},94) {\desc};
  }
  \foreach \xa/\xb in {42/48,90/96,138/144}{
    \draw[-{Latex[length=2mm]},TTCBlue!65!white,line width=.8pt]
      ({\xa+1},99) -- ({\xb-1},99);
  }

  % Phạm vi theo nhóm
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.3}\selectfont\bfseries]
    at (0,67) {PHẠM VI ĐƯỢC XÁC ĐỊNH THEO HỢP ĐỒNG VÀ BIÊN BẢN BÀN GIAO};
  \foreach \xa/\xb/\title/\desc in {
    0/58/KẾT CẤU/Khung • liên kết • lớp bảo vệ,
    64/122/BAO CHE/Mái • tường • thoát nước • khe,
    128/186/CƠ ĐIỆN \& PCCC/Thiết bị • hệ thống • hồ sơ vận hành}
  {
    \fill[TTCLightBlue,rounded corners=3pt] (\xa,25) rectangle (\xb,58);
    \node[anchor=west,text=TTCBlue,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
      at ({\xa+6},48) {\title};
    \node[anchor=north west,text width=46mm,text=TTCTextMuted,
          font=\fontsize{6}{7.3}\selectfont] at ({\xa+6},40) {\desc};
  }
  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,16);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.1}{7.3}\selectfont\bfseries] at (7,8) {CENTRAL SERVICE DESK};
  \node[anchor=east,text=white,font=\fontsize{6.8}{8}\selectfont\bfseries]
    at (179,8) {TIẾP NHẬN → XỬ LÝ → XÁC NHẬN → LƯU VẾT};
\end{tikzpicture}
\end{minipage}
\newpage
"""


PAGE_35 = r"""% ============================================================
% TRANG 35: HỆ SINH THÁI ĐỐI TÁC — LOGO WALL
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{HỆ SINH THÁI • THAM CHIẾU • HỢP TÁC}{Trang 35}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Hệ Sinh Thái Và Các Bên Tham Chiếu}{Selected corporate ecosystem and financial references}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);

  \node[anchor=west,text=TTCBlue,font=\fontsize{15}{17}\selectfont\bfseries]
    at (0,211) {KẾT NỐI NĂNG LỰC • CỘNG HƯỞNG GIÁ TRỊ};
  \node[anchor=west,text width=178mm,text=TTCTextMuted,
        font=\fontsize{7.2}{8.8}\selectfont]
    at (0,199) {Các thương hiệu được trình bày để tham chiếu hệ sinh thái; quan hệ và trạng thái hợp tác được đối chiếu theo hồ sơ hiện hành.};

  % Nhóm doanh nghiệp: card lớn để giữ nhận diện của các logo dạng biểu tượng.
  \fill[TTCLightBlue,rounded corners=3pt] (0,177) rectangle (186,191);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.2}{7.4}\selectfont\bfseries]
    at (7,184) {CORPORATE ECOSYSTEM};
  \node[anchor=east,text=TTCBlue,font=\fontsize{7.2}{8.6}\selectfont\bfseries]
    at (179,184) {HỆ SINH THÁI DOANH NGHIỆP};

  \newcommand{\corporatelogoclosing}[3]{%
    \fill[white,rounded corners=3pt] (#1,#2) rectangle ({#1+43.5},{#2+31});
    \draw[TTCBorder,rounded corners=3pt,line width=.6pt]
      (#1,#2) rectangle ({#1+43.5},{#2+31});
    \fill[TTCRed] ({#1+4},{#2+25.5}) rectangle ({#1+12},{#2+27});
    \node[inner sep=0pt] at ({#1+21.75},{#2+15})
      {\includegraphics[width=29mm,height=23mm,keepaspectratio]{#3}};
  }

  \corporatelogoclosing{0}{139}{../../public/logo/Food-logo.png}
  \corporatelogoclosing{47.5}{139}{../../public/logo/aidc_logo.png}
  \corporatelogoclosing{95}{139}{../../public/logo/alo-logo.png}
  \corporatelogoclosing{142.5}{139}{../../public/logo/company-minhphu.png}
  \corporatelogoclosing{0}{103}{../../public/logo/dieuphuong-logo.png}
  \corporatelogoclosing{47.5}{103}{../../public/logo/par5.png}
  \corporatelogoclosing{95}{103}{../../public/logo/y2y.png}
  \corporatelogoclosing{142.5}{103}{../../public/logo/company-sinchi.png}

  % Nhóm ngân hàng: 06 logo đúng với danh sách năng lực tín dụng trong hồ sơ.
  \fill[TTCLightBlue,rounded corners=3pt] (0,82) rectangle (186,96);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.2}{7.4}\selectfont\bfseries]
    at (7,89) {FINANCIAL REFERENCES};
  \node[anchor=east,text=TTCBlue,font=\fontsize{7.2}{8.6}\selectfont\bfseries]
    at (179,89) {TỔ CHỨC TÀI CHÍNH THAM CHIẾU};

  \newcommand{\banklogoclosing}[2]{%
    \fill[white,rounded corners=3pt] (#1,39) rectangle ({#1+28.5},75);
    \draw[TTCBorder,rounded corners=3pt,line width=.55pt]
      (#1,39) rectangle ({#1+28.5},75);
    \node[inner sep=0pt] at ({#1+14.25},57)
      {\includegraphics[width=23mm,height=17mm,keepaspectratio]{#2}};
  }
  \banklogoclosing{0}{../../public/logo/bank-acb.pdf}
  \banklogoclosing{31.5}{../../public/logo/bank-tpbank.pdf}
  \banklogoclosing{63}{../../public/logo/bank-vietcombank.pdf}
  \banklogoclosing{94.5}{../../public/logo/bank-bidv.pdf}
  \banklogoclosing{126}{../../public/logo/bank-vietinbank.png}
  \banklogoclosing{157.5}{../../public/logo/bank-mb.png}

  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,24);
  \fill[TTCRed,rounded corners=1pt] (7,7) rectangle (9,17);
  \node[anchor=west,text=white,font=\fontsize{8.4}{10}\selectfont\bfseries]
    at (15,15) {HỢP TÁC ĐỂ TRIỂN KHAI TỐT HƠN};
  \node[anchor=west,text=white!70!gray,font=\fontsize{6.1}{7.4}\selectfont]
    at (15,7) {Kết nối chuyên môn, nguồn lực và khả năng tài chính cho dự án.};
  \node[anchor=east,text=TTCCyan,font=\fontsize{6.4}{7.6}\selectfont\bfseries]
    at (179,12) {PARTNERSHIP BUILT ON TRUST};
\end{tikzpicture}
\end{minipage}
\newpage
"""


PAGE_36 = r"""% ============================================================
% TRANG 36: BÌA SAU — NHẬN DIỆN THƯƠNG HIỆU
% ============================================================
\thispagestyle{empty}
\begin{tikzpicture}[remember picture,overlay]
  % Cùng hệ màu với bìa trước, không sử dụng ảnh.
  \fill[TTCDeepNavy] (current page.south west) rectangle (current page.north east);
  \fill[TTCRed] (current page.north west) rectangle ([yshift=-3mm]current page.north east);
  \fill[TTCRed] (current page.south west) rectangle ([yshift=3mm]current page.south east);

  % Hình học công nghiệp chìm tạo chiều sâu nhưng không cạnh tranh với nội dung.
  \begin{scope}[opacity=.075]
    \draw[white,line width=.8pt]
      ([xshift=16mm,yshift=122mm]current page.south west)
      -- ([xshift=16mm,yshift=146mm]current page.south west)
      -- ([xshift=52mm,yshift=168mm]current page.south west)
      -- ([xshift=88mm,yshift=146mm]current page.south west)
      -- ([xshift=124mm,yshift=178mm]current page.south west)
      -- ([xshift=158mm,yshift=146mm]current page.south west)
      -- ([xshift=194mm,yshift=166mm]current page.south west)
      -- ([xshift=194mm,yshift=122mm]current page.south west);
    \foreach \x in {28,40,64,76,100,112,136,148,172,184}{
      \draw[white,line width=.4pt]
        ([xshift=\x mm,yshift=122mm]current page.south west)
        -- ([xshift=\x mm,yshift=147mm]current page.south west);
    }
  \end{scope}
  \node[text=white,opacity=.025,font=\fontsize{92}{96}\selectfont\bfseries]
    at ([yshift=8mm]current page.center) {TTC};

  % Logo và nhận diện đầu trang.
  \node[anchor=north west,fill=white,rounded corners=4pt,
        inner xsep=7mm,inner ysep=4mm]
    at ([xshift=17mm,yshift=-20mm]current page.north west)
    {\includegraphics[width=57mm]{../../public/logo-ttc-removebg-DNXrVdJp.png}};
  \node[anchor=north east,text=white!75!gray,font=\fontsize{6.5}{7.8}\selectfont\bfseries]
    at ([xshift=-17mm,yshift=-24mm]current page.north east) {COMPANY PROFILE • 2026};

  \node[anchor=north west,text=TTCCyan,font=\fontsize{7.5}{9}\selectfont\bfseries]
    at ([xshift=18mm,yshift=-78mm]current page.north west) {INDUSTRIAL DESIGN • BUILD • DELIVERY};
  \node[anchor=north west,text width=174mm,text=white,
        font=\fontsize{28}{31}\selectfont\bfseries]
    at ([xshift=18mm,yshift=-94mm]current page.north west)
    {ĐỒNG HÀNH KIẾN TẠO\\GIÁ TRỊ BỀN VỮNG};
  \fill[TTCRed] ([xshift=18mm,yshift=-164mm]current page.north west)
    rectangle ([xshift=60mm,yshift=-167mm]current page.north west);
  \node[anchor=north west,text width=170mm,text=white!78!gray,
        font=\fontsize{8.2}{10.6}\selectfont]
    at ([xshift=18mm,yshift=-178mm]current page.north west)
    {Tân Thành Công sẵn sàng đồng hành cùng Chủ đầu tư từ ý tưởng, thiết kế đến thi công và bàn giao công trình công nghiệp.};

  % Khối thông tin sáng, rõ và nhận diện ngay khi lật tới bìa cuối.
  \fill[white,rounded corners=5pt]
    ([xshift=17mm,yshift=25mm]current page.south west)
    rectangle ([xshift=-17mm,yshift=104mm]current page.south east);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{9.2}{11}\selectfont\bfseries]
    at ([xshift=26mm,yshift=94mm]current page.south west)
    {CÔNG TY CỔ PHẦN CÔNG NGHỆ XÂY DỰNG TÂN THÀNH CÔNG};
  \node[anchor=north west,text=TTCTextMuted,font=\fontsize{5.8}{7}\selectfont\bfseries]
    at ([xshift=26mm,yshift=83mm]current page.south west)
    {TAN THANH CONG TECHNOLOGY CONSTRUCTION JOINT STOCK COMPANY};
  \draw[TTCBorder,line width=.6pt]
    ([xshift=26mm,yshift=75mm]current page.south west)
    -- ([xshift=-26mm,yshift=75mm]current page.south east);

  \node[anchor=north west,text width=148mm,text=TTCTextDark,
        font=\fontsize{7}{9.2}\selectfont]
    at ([xshift=26mm,yshift=69mm]current page.south west)
    {\textcolor{TTCRed}{\faMapMarker*}\quad
     \textbf{Trụ sở đăng ký:} Số 39, ngõ 292 Kim Giang, Đại Kim, Hà Nội\\[2.3mm]
     \textcolor{TTCRed}{\faBuilding}\quad
     \textbf{Văn phòng giao dịch:} Số 19N7B, KĐT Trung Hòa Nhân Chính, Hà Nội\\[2.3mm]
     \textcolor{TTCRed}{\faPhone*}\quad 0976 447 766
     \hspace{12mm}\textcolor{TTCRed}{\faEnvelope}\quad info@tanthanhcongjsc.com
     \hspace{12mm}\textcolor{TTCRed}{\faGlobe}\quad tanthanhcongjsc.com};

  \node[anchor=south west,text=white!65!gray,font=\fontsize{5.6}{6.8}\selectfont]
    at ([xshift=17mm,yshift=8mm]current page.south west)
    {\textcopyright\ 2026 TÂN THÀNH CÔNG JSC};
  \node[anchor=south east,text=TTCCyan,font=\fontsize{6.2}{7.4}\selectfont\bfseries]
    at ([xshift=-17mm,yshift=8mm]current page.south east)
    {TANTHANHCONGJSC.COM};
\end{tikzpicture}
"""


print("Closing section code loaded.")
