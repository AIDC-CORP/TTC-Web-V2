# -*- coding: utf-8 -*-
"""
Section 2: Financial Governance, Credit Capacity & Talent Development (Pages 08 - 10)
"""

PAGE_08 = r"""% ============================================================
% TRANG 08: QUẢN TRỊ TÀI CHÍNH DỰ ÁN & KỶ LUẬT DÒNG TIỀN
% ============================================================
\pageheaderbar{QUẢN TRỊ TÀI CHÍNH DỰ ÁN \& KỶ LUẬT DÒNG TIỀN}{Trang 08}
\pagefooterbar{Trang 08}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.025, scale=2.6, font=\bfseries\sffamily, text=TTCBlue]
    at ([yshift=-12mm]current page.center) {FINANCIAL GOVERNANCE \& DISCIPLINE};
  \draw[TTCBlue!6!white, line width=0.45pt]
    ([xshift=15mm, yshift=20mm]current page.south west)
    grid[step=8mm]
    ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Quản Trị Tài Chính Dự Án \& Kỷ Luật Dòng Tiền}{Project Financial Governance • Cost Discipline • Verified \& Traceable Records}

\vspace{1mm}
{\fontsize{14.5}{16.5}\selectfont\bfseries\color{TTCBlue}
KIỂM SOÁT TỪ QUYẾT ĐỊNH NHẬN THẦU ĐẾN QUYẾT TOÁN CÔNG TRÌNH\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
Mỗi dự án được thiết lập ngân sách độc lập, kiểm soát 4 cổng và đối chiếu định kỳ trước khi huy động nguồn lực.\par}
\vspace{3.5mm}

% ============================================================
% TẦNG 1: BỐN CỔNG KIỂM SOÁT TÀI CHÍNH + NGUYÊN TẮC QUẢN TRỊ
% ============================================================
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,86);

  % KHỐI TRÁI: 4 CỔNG KIỂM SOÁT (126mm x 86mm)
  \fill[white, rounded corners=4pt] (0,0) rectangle (126,86);
  \draw[TTCBorder, line width=0.7pt, rounded corners=4pt] (0,0) rectangle (126,86);

  \node[anchor=west, text=TTCCyan, font=\fontsize{7}{8}\selectfont\bfseries]
    at (6,79.5) {FOUR FINANCIAL CONTROL GATES};
  \node[anchor=west, text=TTCBlue, font=\fontsize{10}{12}\selectfont\bfseries]
    at (6,72.5) {BỐN CỔNG KIỂM SOÁT TÀI CHÍNH DỰ ÁN};

  % Timeline connector bar
  \draw[TTCBlue!30!white, line width=1pt] (15,50) -- (111,50);

  % 4 Cổng Nodes & Contents
  % Cổng 01
  \fill[TTCRed] (15,50) circle (4.8);
  \node[text=white, font=\fontsize{7}{8}\selectfont\bfseries] at (15,50) {01};
  \node[anchor=south, align=center, text width=26mm, text=TTCRed, font=\fontsize{7}{8.2}\selectfont\bfseries]
    at (15,57.5) {THẨM ĐỊNH\\HỢP ĐỒNG};
  \node[anchor=north, align=center, text width=27mm, text=TTCTextDark, font=\fontsize{6.2}{7.6}\selectfont]
    at (15,42.5) {Biên lợi nhuận\\Điều khoản thanh toán\\Rủi ro giữ lại};

  % Cổng 02
  \fill[white] (47,50) circle (4.8);
  \draw[TTCBlue, line width=0.85pt] (47,50) circle (4.8);
  \node[text=TTCBlue, font=\fontsize{7}{8}\selectfont\bfseries] at (47,50) {02};
  \node[anchor=south, align=center, text width=26mm, text=TTCBlue, font=\fontsize{7}{8.2}\selectfont\bfseries]
    at (47,57.5) {NGÂN SÁCH\\DỰ ÁN};
  \node[anchor=north, align=center, text width=27mm, text=TTCTextDark, font=\fontsize{6.2}{7.6}\selectfont]
    at (47,42.5) {Chi phí cơ sở (Baseline)\\Kế hoạch dòng tiền\\Hạn mức giải ngân};

  % Cổng 03
  \fill[white] (79,50) circle (4.8);
  \draw[TTCBlue, line width=0.85pt] (79,50) circle (4.8);
  \node[text=TTCBlue, font=\fontsize{7}{8}\selectfont\bfseries] at (79,50) {03};
  \node[anchor=south, align=center, text width=26mm, text=TTCBlue, font=\fontsize{7}{8.2}\selectfont\bfseries]
    at (79,57.5) {KIỂM SOÁT\\THỰC HIỆN};
  \node[anchor=north, align=center, text width=27mm, text=TTCTextDark, font=\fontsize{6.2}{7.6}\selectfont]
    at (79,42.5) {So sánh Kế hoạch - Thực tế\\Duyệt phát sinh (VO)\\Dự báo hoàn thành (EAC)};

  % Cổng 04
  \fill[white] (111,50) circle (4.8);
  \draw[TTCBlue, line width=0.85pt] (111,50) circle (4.8);
  \node[text=TTCBlue, font=\fontsize{7}{8}\selectfont\bfseries] at (111,50) {04};
  \node[anchor=south, align=center, text width=26mm, text=TTCBlue, font=\fontsize{7}{8.2}\selectfont\bfseries]
    at (111,57.5) {NGHIỆM THU\\QUYẾT TOÁN};
  \node[anchor=north, align=center, text width=27mm, text=TTCTextDark, font=\fontsize{6.2}{7.6}\selectfont]
    at (111,42.5) {Hồ sơ khối lượng hoàn công\\Thu hồi công nợ\\Đóng mã chi phí dự án};

  % Dải cam kết phía dưới khối trái
  \fill[TTCDeepNavy, rounded corners=3pt] (5,5.5) rectangle (121,18.5);
  \node[anchor=west, text=TTCCyan, font=\fontsize{6.8}{8}\selectfont\bfseries]
    at (8,12) {\faShield*\quad CONTROL BEFORE COMMITMENT};
  \node[anchor=east, text=white, font=\fontsize{6.5}{7.8}\selectfont\bfseries]
    at (118,12) {Chỉ cam kết khi ngân sách \& dòng tiền đã phê duyệt};

  % KHỐI PHẢI: NGUYÊN TẮC QUẢN TRỊ (55mm x 86mm)
  \fill[TTCLightBlue, rounded corners=4pt] (131,0) rectangle (186,86);
  \draw[TTCBorder, line width=0.7pt, rounded corners=4pt] (131,0) rectangle (186,86);

  \node[anchor=north west, text=TTCCyan, font=\fontsize{7}{8}\selectfont\bfseries]
    at (136,79.5) {CONTROL PRINCIPLE};
  \node[anchor=north west, text width=46mm, text=TTCBlue, font=\fontsize{9.5}{11.5}\selectfont\bfseries]
    at (136,73) {KHÔNG NHẬN THẦU VƯỢT NĂNG LỰC};
  \fill[TTCRed] (136,61.5) rectangle (152,63);

  \node[anchor=north west, text width=45mm, text=TTCTextDark, font=\fontsize{6.8}{8.6}\selectfont]
    at (136,56) {
    \textcolor{TTCRed}{\faCheckCircle}\ \textbf{Khóa ngân sách:} Duyệt 100\% trước khi huy động nguồn lực.\\[2.4mm]
    \textcolor{TTCRed}{\faCheckCircle}\ \textbf{Kiểm soát phát sinh:} Mọi chi phí ngoài HĐ phải có nguồn bù.\\[2.4mm]
    \textcolor{TTCRed}{\faCheckCircle}\ \textbf{Tăng trưởng an toàn:} Quy mô chỉ mở rộng khi bàn giao sẵn sàng.
  };

  \fill[white, rounded corners=2.5pt, draw=TTCBorder, line width=0.55pt] (136,6) rectangle (181,18);
  \node[anchor=center, text=TTCBlue, font=\fontsize{6.6}{8}\selectfont\bfseries, align=center]
    at (158.5,12) {\faLock\quad 100\% DỰ ÁN CÓ MÃ CHI PHÍ RIÊNG};
\end{tikzpicture}

\vspace{3.5mm}

% ============================================================
% TẦNG 2: BA TRỤ CỘT QUẢN TRỊ TÀI CHÍNH
% ============================================================
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,58);

  % 3 Cột: Kiểm soát chi phí | Kiểm soát công nợ | Hồ sơ truy xuất (58mm mỗi cột)
  % Card 1: Cost Control
  \fill[white, rounded corners=4pt] (0,0) rectangle (58,58);
  \draw[TTCBorder, line width=0.65pt, rounded corners=4pt] (0,0) rectangle (58,58);
  \fill[TTCRed, rounded corners=1pt] (5,50.5) rectangle (22,52.5);
  \node[anchor=north west, text width=50mm, align=left] at (5,47.5) {
    {\fontsize{7}{8.2}\selectfont\bfseries\color{TTCRed}\faCalculator\quad COST CONTROL}\\[1.2mm]
    {\fontsize{9.8}{11.5}\selectfont\bfseries\color{TTCBlue} KIỂM SOÁT CHI PHÍ}\\[2mm]
    {\fontsize{6.6}{8.2}\selectfont\color{TTCTextDark}
    \textbullet\ Thiết lập ngân sách cơ sở (Baseline) theo WBS.\newline
    \textbullet\ Báo cáo phương sai chi phí hàng tuần.\newline
    \textbullet\ Dự báo tổng chi phí hoàn thành (EAC).}
  };

  % Card 2: Receivable Control
  \fill[white, rounded corners=4pt] (64,0) rectangle (122,58);
  \draw[TTCBorder, line width=0.65pt, rounded corners=4pt] (64,0) rectangle (122,58);
  \fill[TTCCyan, rounded corners=1pt] (69,50.5) rectangle (86,52.5);
  \node[anchor=north west, text width=50mm, align=left] at (69,47.5) {
    {\fontsize{7}{8.2}\selectfont\bfseries\color{TTCCyan}\faFileInvoiceDollar\quad RECEIVABLE CONTROL}\\[1.2mm]
    {\fontsize{9.8}{11.5}\selectfont\bfseries\color{TTCBlue} KIỂM SOÁT CÔNG NỢ}\\[2mm]
    {\fontsize{6.6}{8.2}\selectfont\color{TTCTextDark}
    \textbullet\ Bám sát mốc nghiệm thu khối lượng ITP.\newline
    \textbullet\ Theo dõi dòng tiền thanh toán \& tạm ứng.\newline
    \textbullet\ Quản trị chặt chẽ khoản giữ lại bảo hành.}
  };

  % Card 3: Verified Reporting
  \fill[white, rounded corners=4pt] (128,0) rectangle (186,58);
  \draw[TTCBorder, line width=0.65pt, rounded corners=4pt] (128,0) rectangle (186,58);
  \fill[TTCBlue, rounded corners=1pt] (133,50.5) rectangle (150,52.5);
  \node[anchor=north west, text width=50mm, align=left] at (133,47.5) {
    {\fontsize{7}{8.2}\selectfont\bfseries\color{TTCBlue}\faClipboardCheck\quad VERIFIED REPORTING}\\[1.2mm]
    {\fontsize{9.8}{11.5}\selectfont\bfseries\color{TTCBlue} HỒ SƠ TRUY XUẤT}\\[2mm]
    {\fontsize{6.6}{8.2}\selectfont\color{TTCTextDark}
    \textbullet\ Dữ liệu chi phí đồng bộ thời gian thực.\newline
    \textbullet\ Báo cáo quản trị đa kỳ theo chuẩn quốc tế.\newline
    \textbullet\ Sẵn sàng kiểm toán độc lập theo yêu cầu CĐT.}
  };
\end{tikzpicture}

\vspace{3.5mm}

% ============================================================
% TẦNG 3: GÓI HỒ SƠ MINH CHỨNG & CHÍNH SÁCH BẢO MẬT
% ============================================================
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,46);

  % Outer Card
  \fill[white, rounded corners=4pt] (0,0) rectangle (186,46);
  \draw[TTCBorder, line width=0.65pt, rounded corners=4pt] (0,0) rectangle (186,46);

  % Left Navy Brand Anchor (48mm x 46mm)
  \fill[TTCDeepNavy, rounded corners=4pt] (0,0) rectangle (48,46);
  \node[anchor=west, text width=40mm, align=left] at (6,23) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} DISCLOSURE POLICY}\\[1.2mm]
    {\fontsize{9}{11}\selectfont\bfseries\color{white} MINH BẠCH CÓ\\KIỂM SOÁT}\\[1.8mm]
    {\fontsize{6}{7.2}\selectfont\color{white!75!gray}Verified data \textbullet\ Right audience}
  };

  % 4 Pill Cards on the Right
  \foreach \xa/\xb/\num/\label/\sub in {
    53/81/01/BÁO CÁO TÀI CHÍNH/Kiểm toán độc lập,
    85/113/02/HỒ SƠ THUẾ/Nghĩa vụ Nhà nước,
    117/145/03/ĐỐI CHIẾU CÔNG NỢ/0 nợ đọng NCC,
    149/181/04/BÁO CÁO QUẢN TRỊ/Dòng tiền dự án}{
    \fill[TTCLightBlue, rounded corners=3pt] (\xa,14) rectangle (\xb,40);
    \draw[TTCBorder, line width=0.5pt, rounded corners=3pt] (\xa,14) rectangle (\xb,40);
    \node[text=TTCRed, font=\fontsize{8}{9.5}\selectfont\bfseries] at ({(\xa+\xb)/2},34.5) {\num};
    \node[align=center, text width=26mm, text=TTCBlue, font=\fontsize{6.5}{7.8}\selectfont\bfseries]
      at ({(\xa+\xb)/2},26) {\label};
    \node[align=center, text width=26mm, text=TTCTextMuted, font=\fontsize{5.8}{7}\selectfont]
      at ({(\xa+\xb)/2},18.5) {\sub};
  }

  % Bottom Security Notice
  \draw[TTCBorder, line width=0.5pt] (53,9.5) -- (181,9.5);
  \node[anchor=south west, text=TTCTextMuted, font=\fontsize{6}{7.3}\selectfont\itshape]
    at (53,3) {\faLock\quad Số liệu chi tiết được cung cấp theo hồ sơ mời thầu hoặc thỏa thuận bảo mật NDA với Chủ đầu tư.};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_09 = r"""% ============================================================
% TRANG 09: NĂNG LỰC HUY ĐỘNG CHO DỰ ÁN EPC
% ============================================================
\pageheaderbar{HẠN MỨC TÍN DỤNG \& NGUỒN LỰC TRIỂN KHAI}{Trang 09}
\pagefooterbar{Trang 09}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.02, scale=2.4, font=\bfseries\sffamily, text=TTCBlue]
    at ([yshift=-12mm]current page.center) {BANKING CAPACITY \& SITE MOBILIZATION};
  \draw[TTCBlue!6!white, line width=0.45pt]
    ([xshift=15mm, yshift=20mm]current page.south west)
    grid[step=8mm]
    ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Năng Lực Huy Động Cho Dự Án EPC}{Banking Capacity, Performance Bonds \& Site-Ready Workforce Mobilization}

\vspace{1mm}
{\fontsize{14.5}{16.5}\selectfont\bfseries\color{TTCBlue}
HAI NGUỒN LỰC • MỘT KẾ HOẠCH HUY ĐỘNG TOÀN DIỆN\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
Công cụ tài chính vững chắc kết hợp lực lượng thi công tinh nhuệ, sẵn sàng kích hoạt theo từng mốc hợp đồng.\par}
\vspace{3.5mm}

% ============================================================
% TẦNG 1: HAI ĐỘNG CƠ HUY ĐỘNG (FINANCIAL ENGINE & DELIVERY ENGINE)
% ============================================================
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,80);

  % KHỐI TRÁI: FINANCIAL ENGINE (HẠN MỨC TÍN DỤNG 250 TỶ)
  \fill[white, rounded corners=4pt] (0,0) rectangle (90,80);
  \draw[TTCBorder, line width=0.7pt, rounded corners=4pt] (0,0) rectangle (90,80);

  \node[anchor=north west, text=TTCCyan, font=\fontsize{7}{8}\selectfont\bfseries]
    at (6,73.5) {FINANCIAL ENGINE};
  \node[anchor=north west, text=TTCBlue, font=\fontsize{10}{12}\selectfont\bfseries]
    at (6,67) {NĂNG LỰC TÍN DỤNG \& BẢO LÃNH};

  \node[anchor=west] at (6,54) {
    {\fontsize{25}{27}\selectfont\bfseries\color{TTCRed} 250 TỶ}\quad
    {\fontsize{7.5}{9}\selectfont\bfseries\color{TTCTextMuted} HẠN MỨC TÍN DỤNG}
  };

  % Bank Badges
  \fill[TTCLightBlue, rounded corners=2.5pt, draw=TTCBorder, line width=0.5pt] (5,38) rectangle (85,46);
  \node[anchor=center, text=TTCBlue, font=\fontsize{6.2}{7.4}\selectfont\bfseries]
    at (45,42) {Vietcombank \textbullet\ BIDV \textbullet\ VietinBank \textbullet\ TPBank \textbullet\ ACB \textbullet\ MB};

  \node[anchor=north west, text width=80mm, text=TTCTextDark, font=\fontsize{6.8}{8.6}\selectfont]
    at (6,33.5) {
    \textcolor{TTCRed}{\faCheckCircle}\ \textbf{Bảo lãnh hợp đồng:} Dự thầu, thực hiện, tạm ứng \& bảo hành.\\[1.4mm]
    \textcolor{TTCRed}{\faCheckCircle}\ \textbf{Tốc độ phát hành:} Cấp thư bảo lãnh ngân hàng trong 24--48h.\\[1.4mm]
    \textcolor{TTCRed}{\faCheckCircle}\ \textbf{Chuẩn quốc tế:} Tuân thủ điều ước FIDIC Silver Book \& Mở L/C thép.
  };

  % KHỐI PHẢI: DELIVERY ENGINE (NGUỒN LỰC 2.850+ NHÂN SỰ)
  \fill[white, rounded corners=4pt] (96,0) rectangle (186,80);
  \draw[TTCBorder, line width=0.7pt, rounded corners=4pt] (96,0) rectangle (186,80);

  \node[anchor=north west, text=TTCCyan, font=\fontsize{7}{8}\selectfont\bfseries]
    at (102,73.5) {DELIVERY ENGINE};
  \node[anchor=north west, text=TTCBlue, font=\fontsize{10}{12}\selectfont\bfseries]
    at (102,67) {LỰC LƯỢNG TRIỂN KHAI THỰC CHIẾN};

  \node[anchor=west] at (102,54) {
    {\fontsize{25}{27}\selectfont\bfseries\color{TTCBlue} 2.850+}\quad
    {\fontsize{7.5}{9}\selectfont\bfseries\color{TTCTextMuted} NHÂN SỰ ĐA CHUYÊN NGÀNH}
  };

  % Visual Distribution Bar
  \fill[TTCBlue, rounded corners=1.5pt] (102,41) rectangle (114,45);
  \fill[TTCCyan, rounded corners=1.5pt] (115,41) rectangle (180,45);
  \node[anchor=west, text=TTCBlue, font=\fontsize{6.2}{7.4}\selectfont\bfseries] at (102,47.5) {350+ Kỹ sư (12\%)};
  \node[anchor=east, text=TTCCyan, font=\fontsize{6.6}{7.6}\selectfont\bfseries] at (180,47.5) {2.500+ Công nhân xây lắp (88\%)};

  \node[anchor=north west, text width=78mm, text=TTCTextDark, font=\fontsize{6.8}{8.6}\selectfont]
    at (102,33.5) {
    \textcolor{TTCBlue}{\faCheckCircle}\ \textbf{350+ Quản lý \& Kỹ sư:} CCHN Hạng II, BIM/Tekla LOD 400, QA/QC \& HSE.\\[1.4mm]
    \textcolor{TTCCyan}{\faCheckCircle}\ \textbf{2.500+ Thợ lành nghề:} Hàn AWS D1.1 (3G-6G), Lắp dựng PEB, MEP/PCCC.\\[1.4mm]
    \textcolor{TTCTextMuted}{\faCheckCircle}\ \textbf{Tổ chức thi công:} 3 ca liên tục, sẵn sàng điều động đồng thời 5--8 dự án.
  };

  % Joining Connector Pill
  \fill[white] (93,54) circle (4);
  \draw[TTCCyan, line width=0.8pt] (93,54) circle (4);
  \node[text=TTCRed, font=\fontsize{10}{11}\selectfont\bfseries] at (93,54) {+};
\end{tikzpicture}

\vspace{3.5mm}

% ============================================================
% TẦNG 2: 4 GIAI ĐOẠN KÍCH HOẠT HỢP ĐỒNG (CONTRACT LIFECYCLE)
% ============================================================
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,84);

  \node[anchor=west] at (0,79) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} CONTRACT LIFECYCLE}\quad
    {\fontsize{9.8}{11.5}\selectfont\bfseries\color{TTCBlue} NGUỒN LỰC ĐƯỢC KÍCH HOẠT THEO TỪNG GIAI ĐOẠN}
  };

  % 4 Stages: 01 Tender | 02 Award | 03 Delivery | 04 Handover (42.5mm mỗi card)
  % Stage 01: Tender
  \fill[white, rounded corners=3.5pt] (0,0) rectangle (42,72);
  \draw[TTCBorder, line width=0.65pt, rounded corners=3.5pt] (0,0) rectangle (42,72);
  \fill[TTCLightBlue, rounded corners=3.5pt] (0,59) rectangle (42,72);
  \node[anchor=west] at (4,65.5) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} 01 / TENDER}
  };
  \node[anchor=north west, text width=34mm, align=left] at (4,53) {
    {\fontsize{9.8}{11.5}\selectfont\bfseries\color{TTCBlue} DỰ THẦU}\\[2.2mm]
    {\fontsize{6.5}{7.8}\selectfont\bfseries\color{TTCTextMuted} TÀI CHÍNH}\\[0.7mm]
    {\fontsize{6.8}{8.2}\selectfont\color{TTCTextDark}Bảo lãnh dự thầu 1--3\% \& hạn mức tín dụng.}\\[2mm]
    {\fontsize{6.5}{7.8}\selectfont\bfseries\color{TTCTextMuted} NHÂN LỰC}\\[0.7mm]
    {\fontsize{6.8}{8.2}\selectfont\color{TTCTextDark}Đấu thầu, QS, Kỹ thuật VE \& hợp đồng FIDIC.}
  };
  \fill[TTCLightBlue, rounded corners=2pt, draw=TTCBorder, line width=0.5pt] (6,3.5) rectangle (36,10);
  \node[anchor=center] at (21,6.75) {
    {\fontsize{6.4}{7.8}\selectfont\bfseries\color{TTCBlue} BID-READY}
  };

  % Chevron 1 -> 2
  \node[text=TTCRed] at (45,36) {\faChevronRight};

  % Stage 02: Award
  \fill[white, rounded corners=3.5pt] (48,0) rectangle (90,72);
  \draw[TTCBorder, line width=0.65pt, rounded corners=3.5pt] (48,0) rectangle (90,72);
  \fill[TTCLightBlue, rounded corners=3.5pt] (48,59) rectangle (90,72);
  \node[anchor=west] at (52,65.5) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} 02 / AWARD}
  };
  \node[anchor=north west, text width=34mm, align=left] at (52,53) {
    {\fontsize{9.8}{11.5}\selectfont\bfseries\color{TTCBlue} KÝ HỢP ĐỒNG}\\[2.2mm]
    {\fontsize{6.5}{7.8}\selectfont\bfseries\color{TTCTextMuted} TÀI CHÍNH}\\[0.7mm]
    {\fontsize{6.8}{8.2}\selectfont\color{TTCTextDark}Bảo lãnh thực hiện 5--10\% \& tạm ứng 10--20\%.}\\[2mm]
    {\fontsize{6.5}{7.8}\selectfont\bfseries\color{TTCTextMuted} NHÂN LỰC}\\[0.7mm]
    {\fontsize{6.8}{8.2}\selectfont\color{TTCTextDark}Bổ nhiệm Project Director, PMO \& Core Team.}
  };
  \fill[TTCLightBlue, rounded corners=2pt, draw=TTCBorder, line width=0.5pt] (54,3.5) rectangle (84,10);
  \node[anchor=center] at (69,6.75) {
    {\fontsize{6.4}{7.8}\selectfont\bfseries\color{TTCBlue} CONTRACT-READY}
  };

  % Chevron 2 -> 3
  \node[text=TTCRed] at (93,36) {\faChevronRight};

  % Stage 03: Delivery
  \fill[white, rounded corners=3.5pt] (96,0) rectangle (138,72);
  \draw[TTCBlue!60!white, line width=0.75pt, rounded corners=3.5pt] (96,0) rectangle (138,72);
  \fill[TTCBlue, rounded corners=3.5pt] (96,59) rectangle (138,72);
  \node[anchor=west] at (100,65.5) {
    {\fontsize{7}{8}\selectfont\bfseries\color{white} 03 / DELIVERY}
  };
  \node[anchor=north west, text width=34mm, align=left] at (100,53) {
    {\fontsize{9.8}{11.5}\selectfont\bfseries\color{TTCBlue} TRIỂN KHAI}\\[2.2mm]
    {\fontsize{6.5}{7.8}\selectfont\bfseries\color{TTCTextMuted} TÀI CHÍNH}\\[0.7mm]
    {\fontsize{6.8}{8.2}\selectfont\color{TTCTextDark}Vốn lưu động, L/C vật tư \& thanh toán NCC.}\\[2mm]
    {\fontsize{6.5}{7.8}\selectfont\bfseries\color{TTCTextMuted} NHÂN LỰC}\\[0.7mm]
    {\fontsize{6.8}{8.2}\selectfont\color{TTCTextDark}Ban chỉ huy, Kỹ sư hiện trường \& Đội thợ 3 ca.}
  };
  \fill[TTCBlue, rounded corners=2pt] (102,3.5) rectangle (132,10);
  \node[anchor=center] at (117,6.75) {
    {\fontsize{6.4}{7.8}\selectfont\bfseries\color{white} SITE-READY}
  };

  % Chevron 3 -> 4
  \node[text=TTCRed] at (141,36) {\faChevronRight};

  % Stage 04: Handover
  \fill[white, rounded corners=3.5pt] (144,0) rectangle (186,72);
  \draw[TTCRed!70!white, line width=0.75pt, rounded corners=3.5pt] (144,0) rectangle (186,72);
  \fill[TTCRed, rounded corners=3.5pt] (144,59) rectangle (186,72);
  \node[anchor=west] at (148,65.5) {
    {\fontsize{7}{8}\selectfont\bfseries\color{white} 04 / HANDOVER}
  };
  \node[anchor=north west, text width=34mm, align=left] at (148,53) {
    {\fontsize{9.8}{11.5}\selectfont\bfseries\color{TTCBlue} BÀN GIAO}\\[2.2mm]
    {\fontsize{6.5}{7.8}\selectfont\bfseries\color{TTCTextMuted} TÀI CHÍNH}\\[0.7mm]
    {\fontsize{6.8}{8.2}\selectfont\color{TTCTextDark}Bảo lãnh bảo hành 5\%, duy trì trọn 24 tháng.}\\[2mm]
    {\fontsize{6.5}{7.8}\selectfont\bfseries\color{TTCTextMuted} NHÂN LỰC}\\[0.7mm]
    {\fontsize{6.8}{8.2}\selectfont\color{TTCTextDark}Commissioning, As-Built \& Bảo hành 24/7.}
  };
  \fill[TTCRed, rounded corners=2pt] (150,3.5) rectangle (180,10);
  \node[anchor=center] at (165,6.75) {
    {\fontsize{6.4}{7.8}\selectfont\bfseries\color{white} O\&M-READY}
  };
\end{tikzpicture}

\vspace{3.5mm}

% ============================================================
% TẦNG 3: BĂNG CAM KẾT SẴN SÀNG HUY ĐỘNG (MOBILIZATION ASSURANCE)
% ============================================================
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,43);

  % Outer Card
  \fill[white, rounded corners=4pt] (0,0) rectangle (186,43);
  \draw[TTCBorder, line width=0.65pt, rounded corners=4pt] (0,0) rectangle (186,43);

  % Left Navy Brand Anchor (48mm x 43mm)
  \fill[TTCDeepNavy, rounded corners=4pt] (0,0) rectangle (48,43);
  \node[anchor=west, text width=40mm, align=left] at (6,21.5) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} ASSURANCE}\\[1mm]
    {\fontsize{8.8}{10.5}\selectfont\bfseries\color{white} ĐIỀU KIỆN\\SẴN SÀNG}\\[1.5mm]
    {\fontsize{6}{7.2}\selectfont\color{white!75!gray}Financial \textbullet\ Technical \textbullet\ HSE}
  };

  % 4 Metric Badges on Right
  \foreach \xa/\xb/\val/\title/\sub in {
    53/81/0/NỢ QUÁ HẠN/Bảo toàn dòng tiền,
    85/113/100\%/ĐÀO TẠO HSE/Thẻ an toàn Nhóm 3,
    117/145/AWS D1.1/THỢ HÀN 3G-6G/Sát hạch quốc tế,
    149/181/FDI READY/ĐA NGÔN NGỮ/Anh • Hàn • Trung}{
    \fill[TTCLightBlue, rounded corners=3pt] (\xa,4.5) rectangle (\xb,38.5);
    \draw[TTCBorder, line width=0.5pt, rounded corners=3pt] (\xa,4.5) rectangle (\xb,38.5);
    \node[text=TTCRed, font=\fontsize{11}{13}\selectfont\bfseries] at ({(\xa+\xb)/2},29.5) {\val};
    \node[align=center, text width=26mm, text=TTCBlue, font=\fontsize{6.4}{7.6}\selectfont\bfseries]
      at ({(\xa+\xb)/2},19.5) {\title};
    \node[align=center, text width=26mm, text=TTCTextMuted, font=\fontsize{5.8}{7}\selectfont]
      at ({(\xa+\xb)/2},11) {\sub};
  }
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_10 = r"""% ============================================================
% TRANG 10: TALENT DEVELOPMENT JOURNEY & SAFETY CULTURE
% ============================================================
\pageheaderbar{ĐÀO TẠO NĂNG LỰC \& VĂN HÓA AN TOÀN}{Trang 10}
\pagefooterbar{Trang 10}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.02, scale=2.4, font=\bfseries\sffamily, text=TTCBlue]
    at ([yshift=-12mm]current page.center) {TALENT DEVELOPMENT \& SAFETY CULTURE};
  \draw[TTCBlue!6!white, line width=0.45pt]
    ([xshift=15mm, yshift=20mm]current page.south west)
    grid[step=8mm]
    ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Hành Trình Phát Triển Năng Lực}{Talent Development, Technical Certification \& Safety-First Culture}

\vspace{1mm}
{\fontsize{14.5}{16.5}\selectfont\bfseries\color{TTCBlue}
HỌC ĐÚNG VIỆC • CHỨNG NHẬN ĐÚNG CHUẨN • DẪN DẮT DỰ ÁN\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
Hệ thống đào tạo gắn liền thực chiến hiện trường, biến tri thức chuyên môn thành kết quả thi công an toàn.\par}
\vspace{3.5mm}

% ============================================================
% TRAINING HERO BANNER
% ============================================================
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,65);
  \clip[rounded corners=3pt] (0,0) rectangle (186,65);
  \node[anchor=center, inner sep=0pt] at (93,32.5)
    {\includegraphics[width=186mm]{../../public/introsection1.jpg}};
  \fill[TTCDeepNavy, opacity=0.84] (0,0) rectangle (74,65);
  \fill[TTCDeepNavy, opacity=0.28] (74,0) rectangle (98,65);
  \node[anchor=west, text width=60mm, align=left, text=white] at (8,43) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} FIELD-BASED LEARNING}\\[1.4mm]
    {\fontsize{15}{17}\selectfont\bfseries HỌC TẠI\\ĐIỂM THỰC THI}\\[1.8mm]
    {\fontsize{7}{8.6}\selectfont\color{white!82!gray}
    Đào tạo gắn với tình huống thật, thiết bị thật và quyền dừng công việc khi không an toàn.}
  };
  \node[
    anchor=south east, rounded corners=3pt,
    fill=white, fill opacity=0.94, text opacity=1,
    draw=TTCCyan, line width=0.65pt,
    minimum width=52mm, minimum height=13mm, align=center
  ] at (179,7) {
    {\fontsize{8.2}{9.5}\selectfont\bfseries\color{TTCBlue} SAFETY BEFORE PRODUCTIVITY}\\[0.6mm]
    {\fontsize{6.4}{7.8}\selectfont\color{TTCTextDark}An toàn là điều kiện tiên quyết để bắt đầu công việc}
  };
  \draw[white, line width=1pt, rounded corners=3pt] (0.6,0.6) rectangle (185.4,64.4);
  \draw[TTCBorder, line width=0.65pt, rounded corners=3pt] (0,0) rectangle (186,65);
\end{tikzpicture}

\vspace{3.5mm}

% ============================================================
% DEVELOPMENT JOURNEY (LỘ TRÌNH NĂNG LỰC)
% ============================================================
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,53);
  \node[anchor=west] at (0,48) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} DEVELOPMENT JOURNEY}\quad
    {\fontsize{9.5}{11}\selectfont\bfseries\color{TTCBlue} LỘ TRÌNH NĂNG LỰC TỪ HIỆN TRƯỜNG ĐẾN LÃNH ĐẠO}
  };
  \draw[TTCBlue!28!white, line width=0.8pt] (22,30) -- (164,30);

  \foreach \x/\num in {22/01,69/02,117/03,164/04}{
    \fill[white] (\x,30) circle (5);
    \draw[TTCBlue!45!white, line width=0.75pt] (\x,30) circle (5);
    \node[text=TTCBlue, font=\fontsize{7}{8}\selectfont\bfseries] at (\x,30) {\num};
  }
  \fill[TTCRed] (164,30) circle (5);
  \node[text=white, font=\fontsize{7}{8}\selectfont\bfseries] at (164,30) {04};

  \node[align=center, text width=36mm] at (22,13) {
    {\fontsize{8.8}{10}\selectfont\bfseries\color{TTCBlue} HSE READY}\\[0.7mm]
    {\fontsize{6.5}{7.8}\selectfont 100\% huấn luyện trước khi vào công trường}
  };
  \node[align=center, text width=36mm] at (69,13) {
    {\fontsize{8.8}{10}\selectfont\bfseries\color{TTCBlue} TECHNICAL MASTERY}\\[0.7mm]
    {\fontsize{6.5}{7.8}\selectfont BIM • Tekla • MEP • PEB • QA/QC}
  };
  \node[align=center, text width=36mm] at (117,13) {
    {\fontsize{8.8}{10}\selectfont\bfseries\color{TTCBlue} CERTIFIED PRO}\\[0.7mm]
    {\fontsize{6.5}{7.8}\selectfont Hạng II • AWS D1.1 • PMP • FIDIC}
  };
  \node[align=center, text width=36mm] at (164,13) {
    {\fontsize{8.8}{10}\selectfont\bfseries\color{TTCRed} PROJECT LEADER}\\[0.7mm]
    {\fontsize{6.5}{7.8}\selectfont Chỉ huy, huấn luyện và dẫn dắt đội ngũ}
  };
\end{tikzpicture}

\vspace{3.5mm}

% ============================================================
% TWO DEVELOPMENT SYSTEMS
% ============================================================
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,49);
  \fill[white, rounded corners=4pt] (0,0) rectangle (91,49);
  \draw[TTCBorder, line width=0.65pt, rounded corners=4pt] (0,0) rectangle (91,49);
  \node[anchor=north west, text width=79mm, align=left] at (6,43) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} TTC TECHNICAL ACADEMY}\\[0.8mm]
    {\fontsize{10}{11.5}\selectfont\bfseries\color{TTCBlue} NĂNG LỰC CHUYÊN MÔN}\\[1.5mm]
    {\fontsize{6.8}{8.4}\selectfont\color{TTCTextDark}
    \textcolor{TTCCyan}{\faCheckCircle}\ \textbf{ConTech \& BIM:} Revit, Tekla LOD 400, Navisworks, CDE.\\[0.8mm]
    \textcolor{TTCCyan}{\faCheckCircle}\ \textbf{Technical trades:} AWS D1.1, MEP/PCCC, làm việc trên cao.\\[0.8mm]
    \textcolor{TTCCyan}{\faCheckCircle}\ \textbf{Project control:} PMP, FIDIC, QS và kế hoạch tiến độ.}
  };

  \fill[TTCLightBlue, rounded corners=4pt] (95,0) rectangle (186,49);
  \draw[TTCBorder, line width=0.65pt, rounded corners=4pt] (95,0) rectangle (186,49);
  \node[anchor=north west, text width=79mm, align=left] at (101,43) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCRed} SAFETY \& CULTURE SYSTEM}\\[0.8mm]
    {\fontsize{10}{11.5}\selectfont\bfseries\color{TTCBlue} HÀNH VI \& PHÚC LỢI}\\[1.5mm]
    {\fontsize{6.8}{8.4}\selectfont\color{TTCTextDark}
    \textcolor{TTCRed}{\faCheckCircle}\ Toolbox Talk, diễn tập PCCC và cứu nạn định kỳ.\\[0.8mm]
    \textcolor{TTCRed}{\faCheckCircle}\ Bảo hiểm tai nạn 24/7 và khám sức khỏe định kỳ.\\[0.8mm]
    \textcolor{TTCRed}{\faCheckCircle}\ KPI minh bạch, lộ trình thăng tiến và quyền Stop Work.}
  };
\end{tikzpicture}

\vspace{3.5mm}

% ============================================================
% TRAINING KPI STRIP
% ============================================================
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,28);
  \fill[white, rounded corners=4pt] (0,0) rectangle (186,28);
  \draw[TTCBorder, line width=0.65pt, rounded corners=4pt] (0,0) rectangle (186,28);
  \foreach \x in {46.5,93,139.5}{
    \draw[TTCBorder, line width=0.5pt] (\x,5) -- (\x,23);
  }
  \node[align=center] at (23.25,14) {
    {\fontsize{13.5}{15}\selectfont\bfseries\color{TTCRed} >120 GIỜ}\\[0.7mm]
    {\fontsize{6.6}{7.8}\selectfont\bfseries ĐÀO TẠO/NĂM/KỸ SƯ}
  };
  \node[align=center] at (69.75,14) {
    {\fontsize{13.5}{15}\selectfont\bfseries\color{TTCBlue} 100\%}\\[0.7mm]
    {\fontsize{6.6}{7.8}\selectfont\bfseries CẤP THẺ AN TOÀN}
  };
  \node[align=center] at (116.25,14) {
    {\fontsize{13.5}{15}\selectfont\bfseries\color{TTCCyan} 100\%}\\[0.7mm]
    {\fontsize{6.6}{7.8}\selectfont\bfseries BẢO HIỂM 24/7}
  };
  \node[align=center] at (162.75,14) {
    {\fontsize{13.5}{15}\selectfont\bfseries\color{TTCBlue} ZERO}\\[0.7mm]
    {\fontsize{6.6}{7.8}\selectfont\bfseries ACCIDENT MINDSET}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

print("Section 2 code loaded successfully.")
