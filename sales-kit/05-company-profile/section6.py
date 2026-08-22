# -*- coding: utf-8 -*-
"""
Section 6: Awards, Strategic Vision, Lifetime Support, Project Notes \& Back Cover (Pages 31 - 36)
"""

PAGE_31 = r"""% ============================================================
% TRANG 31: BẰNG KHEN, GIẢI THƯỞNG \& CHỨNG NHẬN NĂNG LỰC [TRANG MỚI]
% ============================================================
\pageheaderbar{BẰNG KHEN \& CHỨNG NHẬN NĂNG LỰC}{Trang 31}
\pagefooterbar{Trang 31}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.03, scale=2.8, font=\bfseries\sffamily, text=TTCBlue] at ([yshift=-10mm]current page.center) {AWARDS \& RECOGNITION CERTIFICATES};
  \draw[TTCBlue!6!white, line width=0.5pt] ([xshift=15mm, yshift=20mm]current page.south west) grid[step=8mm] ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Bằng Khen, Giải Thưởng \& Chứng Nhận Năng Lực Doanh Nghiệp}{National Construction Accreditations, Industry Excellence Awards \& Quality Certifications}

% TẦNG 1: 4 KHỐI CHỨNG NHẬN \& GIẢI THƯỞNG
\noindent
\begin{tabular}{@{}p{91mm}@{\hspace{4mm}}p{91mm}@{}}
  % Khối 1: Hạng II BXD
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=48mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCRed} \faAward\quad 1. CHỨNG CHỈ NĂNG LỰC HẠNG II (BỘ XÂY DỰNG):}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      \textbullet\ Chứng chỉ năng lực hoạt động xây dựng Hạng II do Cục Quản lý Hoạt động Xây dựng -- Bộ Xây Dựng cấp phép.\newline
      \textbullet\ Bảo chứng thẩm quyền Tổng thầu Thiết kế \& Thi công công trình công nghiệp quy mô không giới hạn diện tích sàn.\newline
      \textbullet\ Năng lực vượt nhịp dầm thép lớn $>60$m và nhà máy nhiều tầng.}
    };
  \end{tikzpicture} &
  % Khối 2: Top 10 Tổng thầu EPC
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=48mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCCyan} \faTrophy\quad 2. TOP 10 TỔNG THẦU EPC CÔNG NGHIỆP XUẤT SẮC:}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      \textbullet\ Vinh danh trong Top 10 Doanh nghiệp Tổng thầu EPC Xây dựng Công nghiệp tiêu biểu có tốc độ tăng trưởng nhanh nhất.\newline
      \textbullet\ Được Hiệp hội Nhà thầu Xây dựng Việt Nam (VACC) đánh giá cao về năng lực thi công Fast-track và an toàn lao động.\newline
      \textbullet\ Thương hiệu tiêu biểu phục vụ khối doanh nghiệp FDI.}
    };
  \end{tikzpicture}
  \\[2mm]
  % Khối 3: Bộ 3 ISO Quốc Tế
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=48mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCBlue} \faCertificate\quad 3. BỘ 3 TIÊU CHUẨN ISO TOÀN DIỆN:}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      \textbullet\ \textbf{ISO 9001:2015:} Hệ thống quản lý chất lượng thiết kế và xây dựng.\newline
      \textbullet\ \textbf{ISO 14001:2015:} Hệ thống quản lý môi trường và giảm phát thải.\newline
      \textbullet\ \textbf{ISO 45001:2018:} Hệ thống an toàn và sức khỏe nghề nghiệp.\newline
      \textbullet\ Đánh giá và cấp chứng chỉ định kỳ bởi tổ chức giám định quốc tế.}
    };
  \end{tikzpicture} &
  % Khối 4: Bằng khen An toàn HSE
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=48mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCGold} \faMedal\quad 4. BẰNG KHEN THÀNH TÍCH AN TOÀN ZERO ACCIDENT:}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      \textbullet\ Bằng khen từ Cục An toàn Lao động -- Bộ LĐTB\&XH về thành tích xuất sắc trong công tác bảo đảm an toàn vệ sinh lao động.\newline
      \textbullet\ Đạt cột mốc $>3.500.000$ Giờ làm việc an toàn không tai nạn mất thời gian (LTI Free) trên toàn bộ các dự án.\newline
      \textbullet\ Chứng nhận nhà thầu xanh tuân thủ nghiêm ngặt ESG.}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{2mm}

% TẦNG 2: BẢNG CAM KẾT CHUẨN MỰC PHÁP LÝ
\noindent
\begin{tikzpicture}
  \node[
    rounded corners=6pt,
    fill=TTCLightBlue,
    draw=TTCBorder,
    line width=0.8pt,
    minimum width=186mm,
    inner sep=6pt,
    text width=176mm
  ] {
    {\fontsize{9}{11}\selectfont\bfseries\color{TTCBlue} \faShield*\quad CAM KẾT BẢO TOÀN TÍNH PHÁP LÝ VÀ CHẤT LƯỢNG CHO CHỦ ĐẦU TƯ:}\\[3pt]
    \begin{tabularx}{\linewidth}{@{}p{56mm}@{\hspace{4mm}}p{56mm}@{\hspace{4mm}}p{56mm}@{}}
      \textbf{\color{TTCRed}1. Pháp Nhân Minh Bạch:}\newline
      {\fontsize{6.8}{8.5}\selectfont Đầy đủ hồ sơ năng lực pháp lý Hạng II, không vướng tranh chấp kiện tụng, sẵn sàng vượt qua các vòng thẩm định thầu quốc tế.} &
      \textbf{\color{TTCCyan}2. Chứng Chỉ Hành Nghề:}\newline
      {\fontsize{6.8}{8.5}\selectfont 100\% Giám đốc Dự án và Chỉ huy trưởng có Chứng chỉ hành nghề Hạng II phù hợp quy mô công trình.} &
      \textbf{\color{TTCBlue}3. Kiểm Định Định Kỳ:}\newline
      {\fontsize{6.8}{8.5}\selectfont Hệ thống quản trị chất lượng và môi trường được kiểm toán độc lập hàng năm bởi các tổ chức chứng nhận quốc tế uy tín.}
    \end{tabularx}
  };
\end{tikzpicture}

\vspace{2mm}

% TẦNG 3: BĂNG KPI AWARDS
\noindent
\begin{tikzpicture}
  \node[
    rounded corners=6pt,
    fill=TTCDeepNavy!95!black,
    draw=TTCCyan!80!white,
    line width=1pt,
    text=white,
    minimum width=186mm,
    minimum height=20mm,
    inner sep=4pt
  ] {
    \begin{tabularx}{176mm}{@{}Y|Y|Y|Y@{}}
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCRed} HẠNG II BXD} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCCyan} TOP 10 EPC} &
      {\fontsize{14}{16}\selectfont\bfseries\color{white} 3 CHỨNG CHỈ ISO} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCGold} >3.5M GIỜ AN TOÀN} \\
      {\fontsize{7.2}{9}\selectfont Năng Lực Xây Dựng Cấp II} &
      {\fontsize{7.2}{9}\selectfont Doanh Nghiệp Tiêu Biểu} &
      {\fontsize{7.2}{9}\selectfont ISO 9001/14001/45001} &
      {\fontsize{7.2}{9}\selectfont Thành Tích Zero Accident}
    \end{tabularx}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_32 = r"""% ============================================================
% TRANG 32: BẢN ĐỒ DỰ ÁN 20+ TỈNH THÀNH & 4 CAM KẾT BẢO LÃNH VÀNG
% ============================================================
\pageheaderbar{BẢN ĐỒ THI CÔNG \& 4 CAM KẾT VÀNG}{Trang 32}
\pagefooterbar{Trang 32}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.03, scale=2.8, font=\bfseries\sffamily, text=TTCBlue] at ([yshift=-10mm]current page.center) {PROJECT FOOTPRINT \& 4 GOLDEN COMMITMENTS};
  \draw[TTCBlue!6!white, line width=0.5pt] ([xshift=15mm, yshift=20mm]current page.south west) grid[step=8mm] ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Bản Đồ Phủ Sóng 20+ Tỉnh Thành \& 4 Cam Kết Vàng Bất Biến}{Nationwide Project Footprint Across 20+ Industrial Provinces \& The 4 Golden Guarantees}

% TẦNG 1: BẢN ĐỒ ĐỊA LÝ (Trái) & 3 MIỀN TRỌNG ĐIỂM (Phải)
\noindent
\begin{tabular}{@{}p{76mm}@{\hspace{4mm}}p{106mm}@{}}
  % Ảnh bản đồ
  \begin{tikzpicture}
    \clip[rounded corners=6pt] (0,0) rectangle (7.6, 9.2);
    \node[anchor=center, inner sep=0pt] at (3.8, 4.6) {
      \includegraphics[width=76mm, height=92mm]{../../public/project-assets/map.jpg}
    };
    \fill[TTCDeepNavy, opacity=0.85] (0, 0) rectangle (7.6, 1.4);
    \node[anchor=west, text=white, font=\fontsize{7}{8.5}\selectfont\bfseries] at (0.3, 0.7) {
      \faMapMarker*\quad ĐỘ PHỦ 20+ TỈNH THÀNH TOÀN QUỐC
    };
  \end{tikzpicture} &
  % Phân bổ dự án theo 3 miền
  \begin{tikzpicture}
    \node[
      rounded corners=6pt,
      fill=white,
      draw=TTCBlue!40!white,
      line width=0.9pt,
      minimum width=106mm,
      minimum height=92mm,
      inner sep=6pt,
      text width=98mm,
      align=left
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCBlue} \faMapMarked*\quad ĐỘ PHỦ SÓNG CÔNG TRÌNH THEO 3 MIỀN:}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      \textbf{\color{TTCRed}\faBuilding\ Miền Bắc (Trọng tâm công nghiệp \& FDI):}\newline
      Hà Nội, Vĩnh Phúc, Bắc Ninh, Bắc Giang, Hải Phòng, Quảng Ninh, Hải Dương, Hưng Yên, Hà Nam, Nam Định, Thái Bình, Phú Thọ.\\[3pt]
      \textbf{\color{TTCBlue}\faWater\ Miền Trung (Các KKT ven biển \& Hạ tầng):}\newline
      Thanh Hóa, Nghệ An, Hà Tĩnh, Quảng Trị, Đà Nẵng, Quảng Nam.\\[3pt]
      \textbf{\color{TTCCyan}\faIndustry\ Miền Nam (Thủ phủ FDI \& Logistics):}\newline
      Bình Dương, Đồng Nai, Long An, Tây Ninh, TP. Hồ Chí Minh, Bà Rịa -- Vũng Tàu, Hậu Giang.}\\[4pt]
      \rule{\linewidth}{0.4pt}\\[3pt]
      {\fontsize{6.8}{8.5}\selectfont\color{TTCTextMuted}
      Đội phản ứng nhanh kỹ thuật có mặt tại mọi công trường trên cả 3 miền trong vòng \textbf{4 giờ} kể từ khi nhận yêu cầu.}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{2mm}

% TẦNG 2: 4 CAM KẾT VÀNG BẤT BIẾN
\noindent
\begin{tikzpicture}
  \node[
    rounded corners=6pt,
    fill=TTCLightBlue,
    draw=TTCBorder,
    line width=0.8pt,
    minimum width=186mm,
    inner sep=6pt,
    text width=176mm
  ] {
    {\fontsize{9}{11}\selectfont\bfseries\color{TTCBlue} \faGem\quad 4 CAM KẾT VÀNG BẤT BIẾN CỦA TÂN THÀNH CÔNG DÀNH CHO KHÁCH HÀNG:}\\[3pt]
    \begin{tabularx}{\linewidth}{@{}p{86mm}@{\hspace{4mm}}p{86mm}@{}}
      \textbf{\color{TTCRed}1. TIẾN ĐỘ THẦN TỐC (FAST-TRACK):}\newline
      {\fontsize{6.8}{8.5}\selectfont Bàn giao công trình đúng hoặc trước tiến độ hợp đồng. Phạt 1\% giá trị hợp đồng cho mỗi tuần chậm trễ do lỗi chủ quan của nhà thầu.} &
      \textbf{\color{TTCCyan}2. MINH BẠCH -- 0 PHÁT SINH:}\newline
      {\fontsize{6.8}{8.5}\selectfont Hợp đồng Lump-sum Turnkey trọn gói cố định, triệt tiêu mọi phát sinh chi phí trong suốt quá trình triển khai dự án.} \\[3pt]
      \textbf{\color{TTCBlue}3. ZERO ACCIDENT (AN TOÀN TUYỆT ĐỐI):}\newline
      {\fontsize{6.8}{8.5}\selectfont Duy trì tuyệt đối chính sách Zero Accident tại 100\% công trường, bảo vệ an toàn tính mạng con người là ưu tiên cao nhất.} &
      \textbf{\color{TTCGold}4. BẢO HÀNH 24 THÁNG CẤP TỐC:}\newline
      {\fontsize{6.8}{8.5}\selectfont Bảo hành toàn diện kết cấu thép 24 tháng, hỗ trợ kỹ thuật tại hiện trường trong vòng 4 Giờ (24/7) kể từ khi nhận thông báo.}
    \end{tabularx}
  };
\end{tikzpicture}

\vspace{2mm}

% TẦNG 3: BĂNG KPI FOOTPRINT
\noindent
\begin{tikzpicture}
  \node[
    rounded corners=6pt,
    fill=TTCDeepNavy!95!black,
    draw=TTCCyan!80!white,
    line width=1pt,
    text=white,
    minimum width=186mm,
    minimum height=20mm,
    inner sep=4pt
  ] {
    \begin{tabularx}{176mm}{@{}Y|Y|Y|Y@{}}
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCRed} 20+ TỈNH} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCCyan} 4 GIỜ} &
      {\fontsize{14}{16}\selectfont\bfseries\color{white} 24 THÁNG} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCGold} 0 PHÁT SINH} \\
      {\fontsize{7.2}{9}\selectfont Phủ Sóng 3 Miền} &
      {\fontsize{7.2}{9}\selectfont Phản Ứng Kỹ Thuật Tại Chỗ} &
      {\fontsize{7.2}{9}\selectfont Bảo Hành Toàn Diện Kết Cấu} &
      {\fontsize{7.2}{9}\selectfont Cam Kết Lump-sum Turnkey}
    \end{tabularx}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_33 = r"""% ============================================================
% TRANG 33: TẦM NHÌN 2026-2030 \& CHIẾN LƯỢC PHÁT TRIỂN [TRANG MỚI]
% ============================================================
\pageheaderbar{TẦM NHÌN 2026--2030 \& CHIẾN LƯỢC PHÁT TRIỂN}{Trang 33}
\pagefooterbar{Trang 33}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.03, scale=2.8, font=\bfseries\sffamily, text=TTCBlue] at ([yshift=-10mm]current page.center) {STRATEGIC ROADMAP 2026-2030 \& SUSTAINABILITY};
  \draw[TTCBlue!6!white, line width=0.5pt] ([xshift=15mm, yshift=20mm]current page.south west) grid[step=8mm] ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Tầm Nhìn Chiến Lược 2026 -- 2030 \& Định Hướng Phát Triển Bền Vững}{Next-Gen Industrial Infrastructure, High-Tech Semiconductor Parks \& Net-Zero Leadership}

% TẦNG 1: 3 GIAI ĐOẠN ROADMAP 2026-2030
\noindent
\begin{tabular}{@{}p{59mm}@{\hspace{3.5mm}}p{59mm}@{\hspace{3.5mm}}p{59mm}@{}}
  % Horizon 1: 2026
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt, minimum width=59mm, minimum height=95mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8.5}{10.5}\selectfont\bfseries\color{TTCRed} \faRocket\ GIAI ĐOẠN 2026}\\[1pt]
      {\fontsize{7}{8.5}\selectfont\bfseries\color{TTCBlue} BỨT PHÁ CONTECH}\\[3pt]
      {\fontsize{6.8}{8.5}\selectfont\color{TTCTextDark}
      \textbullet\ \textbf{Doanh thu mục tiêu:} 120 Tỷ VNĐ (\$4,9M USD).\newline
      \textbullet\ \textbf{ConTech Tiên Phong:} 100\% dự án ứng dụng thuật toán AI tối ưu dầm thép.\newline
      \textbullet\ \textbf{Chuẩn Xanh ESG:} 100\% nhà xưởng thiết kế mái Solar-Ready 1--5MWp.\newline
      \textbullet\ \textbf{Mở Rộng Chi Nhánh:} Củng cố chi nhánh Miền Nam tại Bình Dương.}
    };
  \end{tikzpicture} &
  % Horizon 2: 2027-2028
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCCyan!80!white, line width=0.8pt, minimum width=59mm, minimum height=95mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8.5}{10.5}\selectfont\bfseries\color{TTCCyan} \faMicrochip\ GIAI ĐOẠN 2027--2028}\\[1pt]
      {\fontsize{7}{8.5}\selectfont\bfseries\color{TTCBlue} CÔNG NGHỆ CAO}\\[3pt]
      {\fontsize{6.8}{8.5}\selectfont\color{TTCTextDark}
      \textbullet\ \textbf{Doanh thu mục tiêu:} 625 Tỷ VNĐ (\$25M USD).\newline
      \textbullet\ \textbf{Tổng Thầu Bán Dẫn:} Chinh phục các tổ hợp phòng sạch vi mạch bán dẫn \& Data Center.\newline
      \textbullet\ \textbf{Chuẩn Xanh LEED:} Đồng hành cùng Chủ đầu tư đạt chứng chỉ LEED Gold/Platinum.\newline
      \textbullet\ \textbf{Quản Trị Số Hóa:} Vận hành ERP SAP S/4HANA toàn diện.}
    };
  \end{tikzpicture} &
  % Horizon 3: 2029-2030
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt, minimum width=59mm, minimum height=95mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8.5}{10.5}\selectfont\bfseries\color{TTCGold} \faGlobeAmericas\ GIAI ĐOẠN 2029--2030}\\[1pt]
      {\fontsize{7}{8.5}\selectfont\bfseries\color{TTCBlue} TOP 5 EPC VIỆT NAM}\\[3pt]
      {\fontsize{6.8}{8.5}\selectfont\color{TTCTextDark}
      \textbullet\ \textbf{Doanh thu mục tiêu:} 1.000 Tỷ VNĐ (\$40M USD).\newline
      \textbullet\ \textbf{Vị Thế Hàng Đầu:} Top 5 Tổng thầu EPC công nghiệp tư nhân uy tín nhất Việt Nam.\newline
      \textbullet\ \textbf{Vươn Ra Khu Vực:} Mở rộng tổng thầu sang Lào, Campuchia và Indonesia.\newline
      \textbullet\ \textbf{Net-Zero Pioneer:} Dẫn đầu công trình công nghiệp phát thải ròng bằng 0.}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{2mm}

% TẦNG 2: 4 TRỤ CỘT PHÁT TRIỂN BỀN VỮNG
\noindent
\begin{tikzpicture}
  \node[
    rounded corners=6pt,
    fill=white,
    draw=TTCBlue!40!white,
    line width=0.9pt,
    minimum width=186mm,
    inner sep=6pt,
    text width=176mm
  ] {
    {\fontsize{9}{11}\selectfont\bfseries\color{TTCBlue} \faLeaf\quad 4 TRỤ CỘT PHÁT TRIỂN BỀN VỮNG GIAI ĐOẠN 2026 -- 2030:}\\[3pt]
    \begin{tabularx}{\linewidth}{@{}p{42mm}@{\hspace{3mm}}p{42mm}@{\hspace{3mm}}p{42mm}@{\hspace{3mm}}p{42mm}@{}}
      \textbf{\color{TTCRed}1. ConTech Số Hóa:}\newline
      {\fontsize{6.8}{8.5}\selectfont Ứng dụng FaceID, Camera AI, BIM và nền tảng CDE để quản trị hiện trường và hồ sơ theo thời gian thực.} &
      \textbf{\color{TTCCyan}2. Nhân Lực Tinh Nhuệ:}\newline
      {\fontsize{6.8}{8.5}\selectfont Xây dựng đội ngũ 500+ kỹ sư và 3.500+ công nhân chất lượng cao đáp ứng chuẩn FDI.} &
      \textbf{\color{TTCBlue}3. Chuỗi Cung Ứng Xanh:}\newline
      {\fontsize{6.8}{8.5}\selectfont Ưu tiên thép xanh Low-Carbon, vật liệu tái chế và năng lượng mặt trời áp mái.} &
      \textbf{\color{TTCGold}4. Tài Chính Lành Mạnh:}\newline
      {\fontsize{6.8}{8.5}\selectfont Duy trì dòng tiền dương, hệ số thanh toán CR $>1.8$, bảo toàn vốn cho cổ đông và khách hàng.}
    \end{tabularx}
  };
\end{tikzpicture}

\vspace{2mm}

% TẦNG 3: BĂNG KPI VISION
\noindent
\begin{tikzpicture}
  \node[
    rounded corners=6pt,
    fill=TTCDeepNavy!95!black,
    draw=TTCCyan!80!white,
    line width=1pt,
    text=white,
    minimum width=186mm,
    minimum height=20mm,
    inner sep=4pt
  ] {
    \begin{tabularx}{176mm}{@{}Y|Y|Y|Y@{}}
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCRed} TOP 5 EPC} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCCyan} 1.000 TỶ} &
      {\fontsize{14}{16}\selectfont\bfseries\color{white} NET-ZERO} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCGold} REGIONAL} \\
      {\fontsize{7.2}{9}\selectfont Vị Thế Mục Tiêu 2030} &
      {\fontsize{7.2}{9}\selectfont Doanh Thu Kế Hoạch} &
      {\fontsize{7.2}{9}\selectfont Tiêu Chuẩn Công Trình} &
      {\fontsize{7.2}{9}\selectfont Vươn Tầm Đông Nam Á}
    \end{tabularx}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_34 = r"""% ============================================================
% TRANG 34: NĂNG LỰC BẢO HÀNH \& DỊCH VỤ VÒNG ĐỜI 30+ NĂM [TRANG MỚI]
% ============================================================
\pageheaderbar{BẢO HÀNH \& DỊCH VỤ VÒNG ĐỜI 30+ NĂM}{Trang 34}
\pagefooterbar{Trang 34}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.03, scale=2.8, font=\bfseries\sffamily, text=TTCBlue] at ([yshift=-10mm]current page.center) {COMPREHENSIVE WARRANTY \& 30-YEAR LIFECYCLE O\&M};
  \draw[TTCBlue!6!white, line width=0.5pt] ([xshift=15mm, yshift=20mm]current page.south west) grid[step=8mm] ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Chính Sách Bảo Hành 24 Tháng \& Dịch Vụ Vòng Đời 30+ Năm}{Comprehensive 24-Month Structural Warranty, 24/7 Rapid Technical Response \& Lifetime O\&M Partnership}

% TẦNG 1: 4 CAM KẾT DỊCH VỤ HẬU MÃI
\noindent
\begin{tabular}{@{}p{91mm}@{\hspace{4mm}}p{91mm}@{}}
  % Cam kết 1: Phản ứng trong 4 giờ
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=48mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCRed} \faStopwatch\quad 1. PHẢN ỨNG KHẨN CẤP TRONG 4 GIỜ (24/7):}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      \textbullet\ Đường dây nóng kỹ thuật túc trực 24/7 tiếp nhận mọi yêu cầu hỗ trợ từ Chủ đầu tư.\newline
      \textbullet\ Đội kỹ sư phản ứng nhanh có mặt tại công trường trong vòng 4 giờ để khảo sát và xử lý.\newline
      \textbullet\ Sẵn sàng thiết bị xe cẩu và vật tư thay thế khẩn cấp, không làm gián đoạn sản xuất.}
    };
  \end{tikzpicture} &
  % Cam kết 2: Kiểm tra định kỳ 6 tháng
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=48mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCCyan} \faCalendarCheck\quad 2. KIỂM TRA ĐỊNH KỲ MIỄN PHÍ MỖI 6 THÁNG:}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      \textbullet\ Cử chuyên gia kiểm tra độ võng dầm kèo, siết lại bu-lông móng và kiểm tra màng sơn.\newline
      \textbullet\ Đo điện trở tiếp địa chống sét, kiểm tra hệ thống thoát nước mái và khe co giãn.\newline
      \textbullet\ Lập báo cáo tình trạng kỹ thuật chi tiết kèm khuyến nghị bảo trì gửi Chủ đầu tư.}
    };
  \end{tikzpicture}
  \\[2mm]
  % Cam kết 3: Bàn giao Smart Digital Twin
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=48mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCBlue} \faDesktop\quad 3. BÀN GIAO BẢN SAO SỐ SMART DIGITAL TWIN:}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      \textbullet\ Bàn giao toàn bộ dữ liệu 3D As-Built tích hợp thông số bảo trì của từng thiết bị MEP.\newline
      \textbullet\ Hướng dẫn đội ngũ quản lý vận hành của nhà máy tra cứu vị trí van, cáp điện ngầm trong vài giây.\newline
      \textbullet\ Cảnh báo bảo trì dự đoán theo giờ vận hành thực tế của máy móc.}
    };
  \end{tikzpicture} &
  % Cam kết 4: Gói O\&M trọn đời 30+ năm
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=48mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCGold} \faInfinity\quad 4. GÓI DỊCH VỤ O\&M VÒNG ĐỜI 30+ NĂM:}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      \textbullet\ Cung cấp gói dịch vụ vận hành, bảo trì và sửa chữa định kỳ sau thời gian bảo hành.\newline
      \textbullet\ Hỗ trợ kỹ thuật ưu đãi khi Chủ đầu tư cải tạo công năng, nâng cấp dây chuyền hoặc mở rộng phân kỳ 2.\newline
      \textbullet\ Đồng hành bảo vệ tối đa giá trị tài sản nhà máy suốt vòng đời hoạt động.}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{2mm}

% TẦNG 2: BẢNG QUY TRÌNH TIẾP NHẬN BẢO HÀNH
\noindent
\begin{tikzpicture}
  \node[
    rounded corners=6pt,
    fill=TTCLightBlue,
    draw=TTCBorder,
    line width=0.8pt,
    minimum width=186mm,
    inner sep=6pt,
    text width=176mm
  ] {
    {\fontsize{9}{11}\selectfont\bfseries\color{TTCBlue} \faHeadset\quad QUY TRÌNH XỬ LÝ SỰ CỐ BẢO HÀNH CỦA TÂN THÀNH CÔNG:}\\[3pt]
    \begin{tabularx}{\linewidth}{@{}p{56mm}@{\hspace{4mm}}p{56mm}@{\hspace{4mm}}p{56mm}@{}}
      \textbf{\color{TTCRed}Bước 1: Tiếp Nhận (30 Phút):}\newline
      {\fontsize{6.8}{8.5}\selectfont Hotline 24/7 tiếp nhận thông tin, ghi nhận nhật ký điện tử và điều phối đội kỹ sư khu vực phụ trách.} &
      \textbf{\color{TTCCyan}Bước 2: Hiện Trường (4 Giờ):}\newline
      {\fontsize{6.8}{8.5}\selectfont Đội phản ứng nhanh có mặt tại công trường, kiểm tra nguyên nhân, lập biên bản và đưa ra phương án xử lý.} &
      \textbf{\color{TTCBlue}Bước 3: Khắc Phục (24--48 Giờ):}\newline
      {\fontsize{6.8}{8.5}\selectfont Tiến hành sửa chữa dứt điểm, nghiệm thu cùng đại diện Chủ đầu tư và cập nhật dữ liệu vào bản sao số.}
    \end{tabularx}
  };
\end{tikzpicture}

\vspace{2mm}

% TẦNG 3: BĂNG KPI BẢO HÀNH
\noindent
\begin{tikzpicture}
  \node[
    rounded corners=6pt,
    fill=TTCDeepNavy!95!black,
    draw=TTCCyan!80!white,
    line width=1pt,
    text=white,
    minimum width=186mm,
    minimum height=20mm,
    inner sep=4pt
  ] {
    \begin{tabularx}{176mm}{@{}Y|Y|Y|Y@{}}
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCRed} 24 THÁNG} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCCyan} 4 GIỜ} &
      {\fontsize{14}{16}\selectfont\bfseries\color{white} 6 THÁNG/LẦN} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCGold} 30+ NĂM} \\
      {\fontsize{7.2}{9}\selectfont Bảo Hành Toàn Diện Kết Cấu} &
      {\fontsize{7.2}{9}\selectfont Phản Ứng Tại Hiện Trường} &
      {\fontsize{7.2}{9}\selectfont Kiểm Tra Định Kỳ Miễn Phí} &
      {\fontsize{7.2}{9}\selectfont Đồng Hành Vòng Đời O\&M}
    \end{tabularx}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_35 = r"""% ============================================================
% TRANG 35: TRANG GHI CHÚ \& TRAO ĐỔI DỰ ÁN [TRANG MỚI]
% ============================================================
\pageheaderbar{GHI CHÚ \& TRAO ĐỔI DỰ ÁN}{Trang 35}
\pagefooterbar{Trang 35}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.03, scale=2.8, font=\bfseries\sffamily, text=TTCBlue] at ([yshift=-10mm]current page.center) {PROJECT NOTES \& CLIENT COLLABORATION};
  \draw[TTCBlue!6!white, line width=0.5pt] ([xshift=15mm, yshift=20mm]current page.south west) grid[step=8mm] ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Không Gian Ghi Chú \& Trao Đổi Dự Án Cùng Ban Giám Đốc TTC}{Project Discussion Notes, Requirement Checklist \& Fast Consultation Direct Line}

% TẦNG 1: BẢNG CHECKLIST NHANH THÔNG TIN DỰ ÁN
\noindent
\begin{tikzpicture}
  \node[
    rounded corners=6pt,
    fill=white,
    draw=TTCBlue!40!white,
    line width=0.9pt,
    minimum width=186mm,
    inner sep=6pt,
    text width=176mm
  ] {
    {\fontsize{9}{11}\selectfont\bfseries\color{TTCBlue} \faCheckSquare\quad PHIẾU THÔNG TIN SƠ BỘ NHU CẦU DỰ ÁN (PROJECT INTAKE CHECKLIST):}\\[3pt]
    \renewcommand{\arraystretch}{1.2}
    {\fontsize{7.5}{9.5}\selectfont
    \begin{tabularx}{\linewidth}{@{}p{38mm}X|p{38mm}X@{}}
      \textbf{Tên dự án/Chủ đầu tư:} & \dotfill & \textbf{Quốc gia / Nguồn vốn:} & \dotfill \\
      \textbf{Địa điểm dự kiến:} & \dotfill & \textbf{Diện tích quy hoạch:} & \dotfill \\
      \textbf{Ngành nghề sản xuất:} & \dotfill & \textbf{Diện tích sàn nhà xưởng:} & \dotfill \\
      \textbf{Khẩu độ vượt nhịp:} & \dotfill & \textbf{Tải trọng sàn yêu cầu:} & \dotfill \\
      \textbf{Tiến độ bàn giao mục tiêu:} & \dotfill & \textbf{Yêu cầu đặc biệt (PCCC/ESG):} & \dotfill \\
    \end{tabularx}}
  };
\end{tikzpicture}

\vspace{3mm}

% TẦNG 2: KHÔNG GIAN DÒNG KẺ GHI CHÚ CHUYÊN NGHIỆP
\noindent
\begin{tikzpicture}
  \draw[TTCBlue!30!white, line width=0.8pt, fill=white, rounded corners=6pt] (0, 0) rectangle (18.6, 12.0);
  
  \node[anchor=north west, inner sep=6pt] at (0.2, 11.8) {
    {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCBlue} \faEdit\quad GHI CHÚ KỸ THUẬT \& BIÊN BẢN TRAO ĐỔI (MEETING NOTES):}
  };
  
  % Grid of lined paper notes
  \foreach \y in {0.8, 1.5, 2.2, 2.9, 3.6, 4.3, 5.0, 5.7, 6.4, 7.1, 7.8, 8.5, 9.2, 9.9, 10.6} {
    \draw[TTCBlue!15!white, line width=0.5pt] (0.8, \y) -- (17.8, \y);
  }
\end{tikzpicture}

\vspace{3mm}

% TẦNG 3: BANNER LIÊN HỆ TRỰC TIẾP
\noindent
\begin{tikzpicture}
  \node[
    rounded corners=6pt,
    fill=TTCDeepNavy!95!black,
    draw=TTCCyan!80!white,
    line width=1pt,
    text=white,
    minimum width=186mm,
    minimum height=22mm,
    inner sep=4pt
  ] {
    \begin{tabularx}{176mm}{@{}p{115mm}X@{}}
      {\fontsize{8.5}{10.5}\selectfont\bfseries\color{TTCCyan} \faPhone*\quad HOTLINE TƯ VẤN KỸ THUẬT \& BÁO GIÁ EPC 24/7:}\newline
      {\fontsize{7.5}{9.5}\selectfont Tổng Giám Đốc: \textbf{+84 976 447 766} \quad\textbullet\quad Email: \textbf{ceo@tanthanhcongjsc.com}} &
      \raggedleft
      {\fontsize{8.5}{10.5}\selectfont\bfseries\color{TTCGold} TÂN THÀNH CÔNG JSC}\newline
      {\fontsize{7.2}{8.5}\selectfont\color{white!80!gray} Đồng hành kiến tạo tương lai}
    \end{tabularx}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_36 = r"""% ============================================================
% TRANG 36: TRANG BÌA SAU (BACK COVER) -- PHÁP NHÂN TOÀN DIỆN \& KẾT NỐI
% ============================================================
\thispagestyle{empty}
\begin{tikzpicture}[remember picture, overlay]
  % Full Deep Navy Background
  \fill[TTCDeepNavy] (current page.south west) rectangle (current page.north east);
  
  % Tech Grid Background
  \draw[TTCCyan!15!white, line width=0.4pt, step=12mm] ([xshift=10mm, yshift=15mm]current page.south west) grid ([xshift=-10mm, yshift=-15mm]current page.north east);
  
  % Top Red Brand Bar
  \fill[TTCRed] ([yshift=-10mm]current page.north west) rectangle ([yshift=-13mm]current page.north east);
  \node[anchor=west, text=white, font=\fontsize{8}{10}\selectfont\bfseries] at ([xshift=12mm, yshift=-5mm]current page.north west) {
    \faBuilding\quad CÔNG TY CỔ PHẦN CÔNG NGHỆ XÂY DỰNG TÂN THÀNH CÔNG \textbullet\ TTC JSC
  };
  
  % Center Corporate Name Box
  \node[anchor=center] at ([yshift=65mm]current page.center) {
    \begin{tikzpicture}
      \node[align=center, text=white] {
        {\fontsize{24}{28}\selectfont\bfseries TÂN THÀNH CÔNG JSC}\\[4pt]
        {\fontsize{13}{16}\selectfont\bfseries\color{TTCRed} TỔNG THẦU EPC CÔNG NGHIỆP THẾ HỆ MỚI}\\[4pt]
        {\fontsize{9}{11}\selectfont\color{TTCCyan} Next-Generation Industrial EPC General Contractor \textbullet\ PEB 30,000T \textbullet\ ESG-Ready}
      };
    \end{tikzpicture}
  };
  
  % Slogan Box
  \node[anchor=center] at ([yshift=38mm]current page.center) {
    \begin{tikzpicture}
      \node[
        rounded corners=8pt,
        fill=white,
        draw=TTCBlue!40!white,
        line width=1.2pt,
        minimum width=186mm,
        minimum height=22mm,
        inner sep=6pt,
        align=center
      ] {
        {\fontsize{10.5}{13}\selectfont\bfseries\color{TTCBlue} ``ĐỒNG HÀNH CÙNG KHÁCH HÀNG KIẾN TẠO NHỮNG TỔ HỢP CÔNG NGHIỆP HIỆN ĐẠI, AN TOÀN VÀ TRƯỜNG TỒN''}\\[2pt]
        {\fontsize{7.5}{9.5}\selectfont\itshape\color{TTCTextMuted} Partnering with Global FDI Investors to Build Smart, Safe and Sustainable Industrial Manufacturing Facilities.}
      };
    \end{tikzpicture}
  };
  
  % Full Contact Grid (3 Offices + Factory)
  \node[anchor=center] at ([yshift=-15mm]current page.center) {
    \begin{tikzpicture}
      \node[
        rounded corners=8pt,
        fill=TTCDeepNavy!95!black,
        draw=TTCCyan!80!white,
        line width=1pt,
        minimum width=186mm,
        minimum height=62mm,
        inner sep=8pt,
        align=left
      ] {
        \begin{tabularx}{174mm}{@{}p{56mm}@{\hspace{4mm}}p{56mm}@{\hspace{4mm}}p{56mm}@{}}
          \textbf{\color{TTCRed}\faBuilding\ TRỤ SỞ ĐĂNG KÝ:}\newline
          {\fontsize{7.5}{9.5}\selectfont\color{white}
          Số 39, ngõ 292 Kim Giang, Đại Kim, Hà Nội, Việt Nam.\newline
          \textbf{Mã số thuế:} 0107090447\newline
          \textbf{Hotline 24/7:} +84 976 447 766} &
          \textbf{\color{TTCCyan}\faMapMarker*\ VĂN PHÒNG GIAO DỊCH:}\newline
          {\fontsize{7.5}{9.5}\selectfont\color{white}
          Số 19N7B, KĐT Trung Hòa Nhân Chính, Hà Nội, Việt Nam.\newline
          \textbf{Email:} info@tanthanhcongjsc.com\newline
          \textbf{Website:} tanthanhcongjsc.com} &
          \textbf{\color{TTCGold}\faIndustry\ ĐỐI TÁC SẢN XUẤT PEB:}\newline
          {\fontsize{7.5}{9.5}\selectfont\color{white}
          Cụm Công nghiệp Thanh Oai, Hà Nội.\newline
          \textbf{Quy mô:} $> 20.000$ m$^2$\newline
          \textbf{Công suất:} 30.000 Tấn/năm\newline
          \textbf{Chứng chỉ:} AWS D1.1 / Sa 2.5}
        \end{tabularx}
      };
    \end{tikzpicture}
  };
  
  % Dual QR Codes for digital download
  \node[anchor=center] at ([yshift=-62mm]current page.center) {
    \begin{tikzpicture}
      \node[
        rounded corners=6pt,
        fill=white,
        draw=TTCBorder,
        line width=0.8pt,
        minimum width=186mm,
        minimum height=24mm,
        inner sep=6pt
      ] {
        \begin{tabularx}{174mm}{@{}Y|Y@{}}
          {\fontsize{8.5}{10.5}\selectfont\bfseries\color{TTCBlue} \faQrcode\quad TẢI PROFILE PDF SONG NGỮ [VI | EN]}\newline
          {\fontsize{6.8}{8.5}\selectfont\color{TTCTextMuted} Quét mã QR để tải hồ sơ năng lực số hóa chất lượng cao} &
          {\fontsize{8.5}{10.5}\selectfont\bfseries\color{TTCRed} \faVideo\quad THAM QUAN 3D VIRTUAL TOUR NHÀ MÁY}\newline
          {\fontsize{6.8}{8.5}\selectfont\color{TTCTextMuted} Trải nghiệm thực tế ảo dây chuyền CNC \& xưởng PEB 30.000T}
        \end{tabularx}
      };
    \end{tikzpicture}
  };
  
  % Bottom Copyright Bar
  \node[anchor=south, text=white!80!gray, font=\fontsize{7}{8.5}\selectfont] at ([yshift=7mm]current page.south) {
    \textcopyright\ 2026 CÔNG TY CỔ PHẦN CÔNG NGHỆ XÂY DỰNG TÂN THÀNH CÔNG \textbullet\ ALL RIGHTS RESERVED \textbullet\ ISO 9001:2015 \textbullet\ CHỨNG CHỈ NĂNG LỰC HẠNG II BXD
  };
\end{tikzpicture}
"""

print("Section 6 code loaded.")
