# -*- coding: utf-8 -*-
"""
Section 4: EPC Solutions, ConTech AI, ESG Standards & QA/HSE (Pages 14 - 19)
"""

PAGE_14_LEGACY = r"""% ============================================================
% TRANG 14: QUY TRÌNH 6 BƯỚC EPC FAST-TRACK & VALUE ENGINEERING
% ============================================================
\pageheaderbar{GIẢI PHÁP TỔNG THẦU EPC \& VALUE ENGINEERING}{Trang 14}
\pagefooterbar{Trang 14}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.03, scale=2.8, font=\bfseries\sffamily, text=TTCBlue] at ([yshift=-10mm]current page.center) {EPC FAST-TRACK \& VALUE ENGINEERING};
  \draw[TTCBlue!6!white, line width=0.5pt] ([xshift=15mm, yshift=20mm]current page.south west) grid[step=8mm] ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Quy Trình EPC Fast-Track \& Kỹ Thuật Giá Trị (VE)}{Optimized Fast-Track EPC Delivery, Value Engineering (10--15\% Savings) \& FIDIC Turnkey}

% TẦNG 1: 6 BƯỚC CHUỖI GIÁ TRỊ EPC FAST-TRACK
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
    {\fontsize{9.5}{11.5}\selectfont\bfseries\color{TTCBlue} \faProjectDiagram\quad 6 BƯỚC TRIỂN KHAI TỔNG THẦU EPC FAST-TRACK:}\\[3pt]
    \begin{tabularx}{\linewidth}{@{}p{56mm}@{\hspace{4mm}}p{56mm}@{\hspace{4mm}}p{56mm}@{}}
      \textbf{\color{TTCBlue}01. Tư Vấn Pháp Lý \& Quy Hoạch}\newline
      {\fontsize{6.8}{8.5}\selectfont Khảo sát địa chất, xin giấy phép đầu tư IRC, ERC, phê duyệt ĐTM, PCCC và GPXD trong 30--45 ngày.} &
      \textbf{\color{TTCRed}02. Thiết Kế VE \& BIM 5D}\newline
      {\fontsize{6.8}{8.5}\selectfont Tối ưu hóa mô hình kết cấu dầm thép bằng thuật toán AI, rà soát 100\% xung đột trên Navisworks.} &
      \textbf{\color{TTCBlue}03. Phối Hợp Sản Xuất PEB}\newline
      {\fontsize{6.8}{8.5}\selectfont TTC thiết kế Shop Drawing, điều phối gia công song song tại xưởng đối tác trong khi thi công móng.} \\[3pt]
      \textbf{\color{TTCBlue}04. Thi Công Nền Móng Tải Nặng}\newline
      {\fontsize{6.8}{8.5}\selectfont Ép cọc ly tâm, đài móng tải trọng nặng và hoàn thiện sàn siêu phẳng Laser Screed chất lượng cao.} &
      \textbf{\color{TTCBlue}05. Lắp Dựng Thép \& Cơ Điện MEP}\newline
      {\fontsize{6.8}{8.5}\selectfont Lắp dựng dầm kèo nhịp lớn bằng cẩu 100T, thi công trạm biến áp, điều hòa HVAC và PCCC tự động.} &
      \textbf{\color{TTCRed}06. Bàn Giao Digital Twin \& O\&M}\newline
      {\fontsize{6.8}{8.5}\selectfont Bàn giao mô hình nhà máy số 3D hoàn công, bảo hành kết cấu 24 tháng và bảo trì vòng đời 30+ năm.}
    \end{tabularx}
  };
\end{tikzpicture}

\vspace{2mm}

% TẦNG 2: BẢNG SO SÁNH VALUE ENGINEERING (VE)
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
    {\fontsize{9}{11}\selectfont\bfseries\color{TTCBlue} \faCalculator\quad BẢNG PHÂN TÍCH HIỆU QUẢ KỸ THUẬT GIÁ TRỊ (VALUE ENGINEERING -- VE):}\\[3pt]
    \renewcommand{\arraystretch}{1.12}
    {\fontsize{7.2}{9.2}\selectfont
    \begin{tabularx}{\linewidth}{@{}p{38mm}p{45mm}p{45mm}X@{}}
      \toprule
      \textbf{Hạng Mục} & \textbf{Thiết Kế Cơ Sở Truyền Thống} & \textbf{Giải Pháp VE Của TTC} & \textbf{Hiệu Quả Đột Phá} \\
      \midrule
      \textbf{Kết Cấu Dầm Thép} & Dầm chữ H cán nóng đồng nhất tiết diện & Dầm tổ hợp Tapered tối ưu mô-men AI & \textbf{\color{TTCRed}Tiết kiệm 10--15\% chi phí} \\
      \textbf{Giải Pháp Nền Móng} & Móng cọc đại trà chịu tải trọng lớn & Giảm tải dầm thép, tối ưu sơ đồ cọc & \textbf{\color{TTCBlue}Tiết giảm 8.5\% chi phí móng} \\
      \textbf{Tiến Độ Xây Dựng} & Tuần tự (Thiết kế $\rightarrow$ Móng $\rightarrow$ Thép) & Fast-track: Sản xuất PEB song song làm móng & \textbf{\color{TTCCyan}Rút ngắn 45--60 ngày} \\
      \textbf{Phối Hợp Cơ Điện MEP} & Xử lý xung đột thủ công tại hiện trường & Rà soát xung đột không gian 3D Navisworks & \textbf{\color{TTCGold}Triệt tiêu 100\% xung đột} \\
      \bottomrule
    \end{tabularx}}
  };
\end{tikzpicture}

\vspace{2mm}

% TẦNG 3: BĂNG KPI EPC
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
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCRed} TỐI ƯU CHI PHÍ} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCCyan} -60 NGÀY} &
      {\fontsize{14}{16}\selectfont\bfseries\color{white} 0 XUNG ĐỘT} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCGold} 0 PHÁT SINH} \\
      {\fontsize{7.2}{9}\selectfont Tiết Giảm Chi Phí Kết Cấu} &
      {\fontsize{7.2}{9}\selectfont Rút Ngắn Tiến Độ Dự Án} &
      {\fontsize{7.2}{9}\selectfont Mô Hình 3D Navisworks} &
      {\fontsize{7.2}{9}\selectfont Hợp Đồng Lump-sum Trọn Gói}
    \end{tabularx}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_15_LEGACY = r"""% ============================================================
% TRANG 15: TIÊN PHONG CONTECH: BIM 5D, AI TỐI ƯU THÉP & DIGITAL TWIN
% ============================================================
\pageheaderbar{TIÊN PHONG CÔNG NGHỆ CONTECH \& BIM 5D}{Trang 15}
\pagefooterbar{Trang 15}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.03, scale=2.8, font=\bfseries\sffamily, text=TTCBlue] at ([yshift=-10mm]current page.center) {CONTECH AI OPTIMIZATION \& BIM 5D};
  \draw[TTCBlue!6!white, line width=0.5pt] ([xshift=15mm, yshift=20mm]current page.south west) grid[step=8mm] ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Tiên Phong ConTech: BIM 5D, AI Tối Ưu Thép \& Digital Twin}{Next-Gen Construction Technology: 5D BIM Coordination, AI Structural Optimization \& Smart Digital Twin}

% TẦNG 1: 3 TRỤ CỘT CONTECH
\noindent
\begin{tabular}{@{}p{59mm}@{\hspace{3.5mm}}p{59mm}@{\hspace{3.5mm}}p{59mm}@{}}
  % Trụ cột 1: BIM 5D
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt, minimum width=59mm, minimum height=95mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8.5}{10.5}\selectfont\bfseries\color{TTCRed} \faCubes\ 01. BIM 5D TOÀN DIỆN}\\[3pt]
      {\fontsize{6.8}{8.5}\selectfont\color{TTCTextDark}
      \textbullet\ \textbf{Tekla Structures LOD 400:} Mô hình hóa chi tiết dầm, cột, bản mã, bu-lông; xuất Shop Drawing tự động.\newline
      \textbullet\ \textbf{Navisworks Zero-Clash:} Rà soát 100\% va chạm giữa dầm thép và hệ cơ điện MEP (ống gió, ống PCCC, máng cáp).\newline
      \textbullet\ \textbf{BIM 4D Tiến Độ:} Mô phỏng 3D trình tự lắp dựng dầm kèo và chuỗi cung ứng vật tư.\newline
      \textbullet\ \textbf{BIM 5D Chi Phí:} Đồng bộ dự toán \& thanh quyết toán theo khối lượng thực tế.}
    };
  \end{tikzpicture} &
  % Trụ cột 2: AI Tối ưu thép
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt, minimum width=59mm, minimum height=95mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8.5}{10.5}\selectfont\bfseries\color{TTCCyan} \faMicrochip\ 02. AI TỐI ƯU KẾT CẤU}\\[3pt]
      {\fontsize{6.8}{8.5}\selectfont\color{TTCTextDark}
      \textbullet\ \textbf{Thuật Toán Tối Ưu Đa Biến:} Tự động lặp hàng ngàn kịch bản tiết diện dầm Tapered theo biểu đồ mô-men uốn.\newline
      \textbullet\ \textbf{Tiết Kiệm 10--15\% Chi Phí:} Giảm đáng kể chi phí nhờ giải thuật AI tối ưu tiết diện dầm và kết cấu chịu lực.\newline
      \textbullet\ \textbf{Tuân Thủ AISC 360 / TCVN:} Đảm bảo 100\% tiêu chuẩn an toàn chịu lực của Mỹ và Việt Nam.\newline
      \textbullet\ \textbf{R\&D Độc Quyền AIDC:} Đơn vị tiên phong số hóa ngành kết cấu thép tại Việt Nam.}
    };
  \end{tikzpicture} &
  % Trụ cột 3: Smart Digital Twin
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt, minimum width=59mm, minimum height=95mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8.5}{10.5}\selectfont\bfseries\color{TTCBlue} \faDesktop\ 03. SMART DIGITAL TWIN}\\[3pt]
      {\fontsize{6.8}{8.5}\selectfont\color{TTCTextDark}
      \textbullet\ \textbf{Bản Sao Số 3D As-Built:} Bàn giao toàn bộ dữ liệu thuộc tính hình học và thông số kỹ thuật 100\% thiết bị MEP.\newline
      \textbullet\ \textbf{Cảm Biến IoT Thời Gian Thực:} Theo dõi độ võng dầm mái, rung chấn và nhiệt độ bề mặt.\newline
      \textbullet\ \textbf{Bảo Trì Dự Đoán:} Cảnh báo sớm nguy cơ ăn mòn hoặc xuống cấp kết cấu trước khi xảy ra sự cố.\newline
      \textbullet\ \textbf{Đồng Hành O\&M 30+ Năm:} Tối ưu hóa chi phí vận hành trọn đời nhà máy.}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{2mm}

% TẦNG 2: BẢNG SO SÁNH CÔNG NGHỆ CONTECH
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
    {\fontsize{9}{11}\selectfont\bfseries\color{TTCBlue} \faChartBar\quad HIỆU QUẢ ĐỘT PHÁ TỪ HỆ SINH THÁI CÔNG NGHỆ CONTECH AIDC:}\\[3pt]
    \begin{tabularx}{\linewidth}{@{}p{56mm}@{\hspace{4mm}}p{56mm}@{\hspace{4mm}}p{56mm}@{}}
      \textbf{\color{TTCRed}1. Tối Ưu Trọng Lượng Dầm:}\newline
      {\fontsize{6.8}{8.5}\selectfont Giảm 3--5 kg thép/$m^2$ sàn xây dựng, giảm tải trọng bản thân công trình truyền xuống móng cọc, tiết kiệm 8.5\% chi phí đài cọc.} &
      \textbf{\color{TTCCyan}2. Triệt Tiêu Lãng Phí:}\newline
      {\fontsize{6.8}{8.5}\selectfont Xuất phôi cắt CNC tự động từ mô hình Tekla giúp giảm hao hụt thép tấm từ 6\% xuống dưới 1.5\%, bảo vệ dòng tiền đầu tư.} &
      \textbf{\color{TTCBlue}3. Vận Hành Thông Minh:}\newline
      {\fontsize{6.8}{8.5}\selectfont Bản sao số Digital Twin kết nối trực tiếp hệ thống SCADA/BMS giúp ban quản lý nhà máy FDI dễ dàng định vị tài sản và bảo trì.}
    \end{tabularx}
  };
\end{tikzpicture}

\vspace{2mm}

% TẦNG 3: BĂNG KPI CONTECH
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
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCRed} LOD 400} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCCyan} 10--15\%} &
      {\fontsize{14}{16}\selectfont\bfseries\color{white} 100\% CLASH-FREE} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCGold} 30+ NĂM} \\
      {\fontsize{7.2}{9}\selectfont Chi Tiết Bản Vẽ Tekla} &
      {\fontsize{7.2}{9}\selectfont Tiết Kiệm Thép Bằng AI} &
      {\fontsize{7.2}{9}\selectfont Rà Soát Không Gian 3D} &
      {\fontsize{7.2}{9}\selectfont Vận Hành Smart Digital Twin}
    \end{tabularx}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_16_LEGACY = r"""% ============================================================
% TRANG 16: CÔNG TRÌNH XANH BỀN VỮNG ESG & MÁI SOLAR-READY
% ============================================================
\pageheaderbar{CÔNG TRÌNH XANH ESG \& MÁI SOLAR-READY}{Trang 16}
\pagefooterbar{Trang 16}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.03, scale=2.8, font=\bfseries\sffamily, text=TTCBlue] at ([yshift=-10mm]current page.center) {ESG SUSTAINABILITY \& SOLAR-READY ROOF};
  \draw[TTCBlue!6!white, line width=0.5pt] ([xshift=15mm, yshift=20mm]current page.south west) grid[step=8mm] ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Tiêu Chuẩn Công Trình Xanh ESG \& Mái Sẵn Sàng Điện Mặt Trời}{Sustainable Green Facilities, Net-Zero Ready, Solar-Ready Roofing (1--5MWp) \& LEED/LOTUS Compliance}

% TẦNG 1: 4 GIẢI PHÁP CÔNG TRÌNH XANH ESG
\noindent
\begin{tabular}{@{}p{91mm}@{\hspace{4mm}}p{91mm}@{}}
  % Giải pháp 1: Mái Solar-Ready
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=48mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCRed} \faSolarPanel\quad 1. KẾT CẤU MÁI SOLAR-READY (1--5MWp):}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      \textbullet\ Tính toán dự phòng tải trọng pin mặt trời ($+15$ đến $+20$ kg/m$^2$) ngay từ giai đoạn thiết kế dầm kèo.\newline
      \textbullet\ Hệ xà gồ Z và đai kẹp Seamlock chuyên dụng, sẵn sàng lắp đặt hệ thống pin áp mái mà không cần gia cố.\newline
      \textbullet\ Giúp Chủ đầu tư FDI nhanh chóng đạt chứng chỉ năng lượng tái tạo quốc tế RECs/I-REC.}
    };
  \end{tikzpicture} &
  % Giải pháp 2: Vỏ bao che cách nhiệt
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=48mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCCyan} \faLeaf\quad 2. VỎ BAO CHE CÁCH NHIỆT \& TIẾT KIỆM NĂNG LƯỢNG:}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      \textbullet\ Sử dụng panel PIR / Rockwool chống cháy lan, hệ số dẫn nhiệt cực thấp ($K \le 0.022$ W/m.K).\newline
      \textbullet\ Tôn mái phản xạ nhiệt Cool-Roof giảm 5--8$^\circ$C nhiệt độ bề mặt nhà xưởng.\newline
      \textbullet\ Tiết kiệm 20--25\% chi phí điện năng tiêu thụ cho hệ thống điều hòa không khí HVAC.}
    };
  \end{tikzpicture}
  \\[2mm]
  % Giải pháp 3: Tư vấn LEED / LOTUS
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=48mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCBlue} \faAward\quad 3. TƯ VẤN CHỨNG CHỈ XANH (LEED/LOTUS):}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      \textbullet\ Đội ngũ chuyên gia hỗ trợ trọn gói hồ sơ kỹ thuật, mô phỏng năng lượng và lựa chọn vật liệu Low-VOC.\newline
      \textbullet\ Tối ưu hóa chu trình vòng đời vật liệu, hướng tới tiêu chuẩn phát thải ròng bằng 0 (Net-Zero Carbon).\newline
      \textbullet\ Tăng giá trị tài sản nhà máy và nâng cao uy tín thương hiệu trong chuỗi cung ứng toàn cầu.}
    };
  \end{tikzpicture} &
  % Giải pháp 4: Xử lý nước thải Cột A
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=48mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCGold} \faRecycle\quad 4. XỬ LÝ NƯỚC THẢI \& TUẦN HOÀN:}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      \textbullet\ Trạm xử lý nước thải sinh hoạt \& sản xuất công nghiệp đạt chuẩn Cột A theo QCVN 40:2011/BTNMT.\newline
      \textbullet\ Tích hợp hệ thống thu gom nước mưa tuần hoàn tưới mát cảnh quan xanh.\newline
      \textbullet\ Phân loại và tái chế 100\% rác thải xây dựng trong suốt quá trình thi công.}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{2mm}

% TẦNG 2: BẢNG LỢI ÍCH ESG CHO CHỦ ĐẦU TƯ
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
    {\fontsize{9}{11}\selectfont\bfseries\color{TTCBlue} \faGlobeAmericas\quad GIÁ TRỊ VƯỢT TRỘI CHO CHỦ ĐẦU TƯ FDI KHI ĐẦU TƯ NHÀ MÁY XANH ESG:}\\[3pt]
    \begin{tabularx}{\linewidth}{@{}p{56mm}@{\hspace{4mm}}p{56mm}@{\hspace{4mm}}p{56mm}@{}}
      \textbf{\color{TTCRed}1. Dễ Dàng Vay Vốn Xanh:}\newline
      {\fontsize{6.8}{8.5}\selectfont Đạt tiêu chuẩn ESG giúp doanh nghiệp FDI dễ dàng tiếp cận các gói tín dụng xanh ưu đãi lãi suất từ các ngân hàng quốc tế.} &
      \textbf{\color{TTCCyan}2. Vượt Rào Cản Thuế Carbon:}\newline
      {\fontsize{6.8}{8.5}\selectfont Sẵn sàng đáp ứng cơ chế điều chỉnh biên giới carbon (CBAM) của EU và các yêu cầu khắt khe từ thị trường Mỹ.} &
      \textbf{\color{TTCBlue}3. Tối Ưu Chi Phí Vận Hành:}\newline
      {\fontsize{6.8}{8.5}\selectfont Tiết kiệm hàng tỷ đồng tiền điện mỗi năm nhờ điện mặt trời áp mái và giải pháp vỏ bao che cách nhiệt tối ưu.}
    \end{tabularx}
  };
\end{tikzpicture}

\vspace{2mm}

% TẦNG 3: BĂNG KPI ESG
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
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCRed} 1--5 MWp} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCCyan} -20\% ĐIỆN} &
      {\fontsize{14}{16}\selectfont\bfseries\color{white} CỘT A} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCGold} LEED READY} \\
      {\fontsize{7.2}{9}\selectfont Công Suất Mái Solar-Ready} &
      {\fontsize{7.2}{9}\selectfont Tiết Kiệm Năng Lượng HVAC} &
      {\fontsize{7.2}{9}\selectfont Xử Lý Nước Thải QCVN 40} &
      {\fontsize{7.2}{9}\selectfont Tiêu Chuẩn Công Trình Xanh}
    \end{tabularx}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_14 = r"""% ============================================================
% TRANG 14: EPC VALUE MODEL — ONE CONTRACT, ONE ACCOUNTABILITY
% ============================================================
\begin{tikzpicture}[remember picture, overlay]
  \fill[TTCLightBlue]
    ([xshift=132mm,yshift=-30mm]current page.north west) --
    ([xshift=210mm,yshift=-30mm]current page.north west) --
    ([xshift=210mm,yshift=-104mm]current page.north west) -- cycle;
  \draw[TTCBlue!7!white, line width=12pt]
    ([xshift=154mm,yshift=37mm]current page.south west) --
    ([xshift=205mm,yshift=88mm]current page.south west);
  \draw[TTCRed!8!white, line width=3pt]
    ([xshift=162mm,yshift=37mm]current page.south west) --
    ([xshift=205mm,yshift=80mm]current page.south west);
  % A light structural frame at the bottom — no square grid
  \begin{scope}[shift={(current page.south west)},x=1mm,y=1mm,opacity=.42]
    \draw[TTCBlue!17!white, line width=.7pt] (12,13) -- (198,13);
    \draw[TTCBlue!16!white] (17,13) -- (17,37) -- (47,50) -- (77,37) --
      (107,50) -- (137,37) -- (167,50) -- (197,37) -- (197,13);
    \foreach \x in {17,47,77,107,137,167,197}{\draw[TTCBlue!12!white] (\x,13) -- (\x,42);}
    \draw[TTCRed!18!white, line width=.7pt] (17,20) -- (197,20);
  \end{scope}
\end{tikzpicture}

\pagefooterbar{Trang 14}
\begin{minipage}[t][246mm]{\textwidth}
\pageheaderbar{GIẢI PHÁP TỔNG THẦU EPC \& VALUE ENGINEERING}{Trang 14}
\vspace{6mm}
\secbrand{Mô Hình Tổng Thầu EPC Tạo Giá Trị}{Fast-Track Delivery, Value Engineering \& Single-Point Accountability}

{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
NHANH HƠN • GỌN HƠN • ÍT RỦI RO HƠN\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
TTC tích hợp pháp lý, thiết kế, mua sắm và thi công trong một hợp đồng — mọi quyết định cùng hướng tới hiệu quả đầu tư cuối cùng.\par}
\vspace{3mm}

% HERO — THE FACILITY AS ONE INTEGRATED SYSTEM
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,66);
  \clip[rounded corners=3pt] (0,0) rectangle (186,66);
  \node[anchor=center, inner sep=0pt] at (93,33)
    {\includegraphics[width=186mm]{../../public/factory-tech-3d.jpg}};
  \fill[TTCDeepNavy, opacity=.88] (0,0) rectangle (66,66);
  \fill[TTCDeepNavy, opacity=.26] (66,0) rectangle (92,66);
  \node[anchor=west, text width=52mm, align=left, text=white] at (8,43) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} TTC EPC VALUE MODEL}\\[1.3mm]
    {\fontsize{17}{19}\selectfont\bfseries ONE CONTRACT}\\[-.2mm]
    {\fontsize{10}{12}\selectfont\bfseries\color{TTCRed!85!white} ONE ACCOUNTABILITY}\\[1.7mm]
    {\fontsize{7}{8.5}\selectfont\color{white!82!gray}
    Một đầu mối kiểm soát phạm vi, ngân sách, tiến độ và chất lượng bàn giao.}
  };
  \node[rounded corners=2pt, fill=white, align=center, minimum width=29mm,
        minimum height=15mm] at (113,15) {
    {\fontsize{9}{10}\selectfont\bfseries\color{TTCRed} REVIEWED}\\[-.3mm]
    {\fontsize{5.8}{7}\selectfont\color{TTCBlue} STRUCTURAL OPTION}
  };
  \node[rounded corners=2pt, fill=white, align=center, minimum width=29mm,
        minimum height=15mm] at (145,15) {
    {\fontsize{9}{10}\selectfont\bfseries\color{TTCCyan} PARALLEL}\\[-.3mm]
    {\fontsize{5.8}{7}\selectfont\color{TTCBlue} WORKSTREAMS}
  };
  \node[rounded corners=2pt, fill=TTCGold, text=white, align=center,
        minimum width=29mm, minimum height=15mm] at (177,15) {
    {\fontsize{9}{10}\selectfont\bfseries ALIGNED}\\[-.3mm]
    {\fontsize{5.8}{7}\selectfont MODEL CHECK}
  };
\end{tikzpicture}

\vspace{3mm}

% SIX WORKSTREAMS — SIMPLE MEMORY LINE
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,48);
  \fill[TTCLightBlue, rounded corners=3pt] (0,0) rectangle (186,48);
  \draw[TTCBorder, rounded corners=3pt, line width=.6pt] (0,0) rectangle (186,48);
  \node[anchor=west, text=TTCBlue, font=\fontsize{8}{9.5}\selectfont\bfseries] at (7,40)
    {\faProjectDiagram\quad SÁU DÒNG CÔNG VIỆC — MỘT CHUỖI GIÁ TRỊ};
  \draw[TTCBlue!35!white, line width=1pt] (14,23) -- (172,23);
  \foreach \x/\n/\t/\s in {
    16/01/DEFINE/Pháp lý \& brief,
    47/02/OPTIMIZE/VE \& BIM 5D,
    78/03/ENGINEER/Shop Drawing,
    109/04/FABRICATE/PEB \& supply,
    140/05/BUILD/Foundation \& MEP,
    171/06/OPERATE/Twin \& O\&M}{
      \fill[white] (\x,23) circle (4.6);
      \draw[TTCBlue, line width=.75pt] (\x,23) circle (4.6);
      \node[text=TTCRed,font=\fontsize{6.4}{7}\selectfont\bfseries] at (\x,23) {\n};
      \node[anchor=north,align=center,text width=27mm] at (\x,16) {
        {\fontsize{6.6}{7.8}\selectfont\bfseries\color{TTCBlue} \t}\\[-.2mm]
        {\fontsize{5.7}{6.8}\selectfont\color{TTCTextMuted} \s}
      };
  }
\end{tikzpicture}

\vspace{3mm}

% THREE SOURCES OF VALUE
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,49);
  \foreach \x/\c in {0/TTCRed,63/TTCCyan,126/TTCGold}{
    \fill[white, rounded corners=2pt] (\x,0) rectangle +(60,49);
    \draw[TTCBorder, rounded corners=2pt, line width=.6pt] (\x,0) rectangle +(60,49);
    \fill[\c, rounded corners=2pt] (\x,45) rectangle +(60,4);
  }
  \node[anchor=north west, text width=50mm] at (5,40) {
    {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCRed} 01 • DESIGN LESS}\\[1mm]
    {\fontsize{10}{11}\selectfont\bfseries\color{TTCBlue} TỐI ƯU KẾT CẤU}\\[1mm]
    {\fontsize{6.8}{8.2}\selectfont\color{TTCTextDark}
    Dầm Tapered theo nội lực, giảm tải xuống móng và bảo toàn hệ số an toàn.}
  };
  \node[anchor=north west, text width=50mm] at (68,40) {
    {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCCyan} 02 • BUILD EARLIER}\\[1mm]
    {\fontsize{10}{11}\selectfont\bfseries\color{TTCBlue} CHẠY SONG SONG}\\[1mm]
    {\fontsize{6.8}{8.2}\selectfont\color{TTCTextDark}
    Thiết kế, gia công PEB và nền móng triển khai đồng thời theo đường găng.}
  };
  \node[anchor=north west, text width=50mm] at (131,40) {
    {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCGold} 03 • CONTROL RISK}\\[1mm]
    {\fontsize{10}{11}\selectfont\bfseries\color{TTCBlue} KHÓA PHẠM VI}\\[1mm]
    {\fontsize{6.8}{8.2}\selectfont\color{TTCTextDark}
    BIM clash-check, release gate và hợp đồng Lump-sum hạn chế phát sinh.}
  };
\end{tikzpicture}

\vspace{3mm}

% KPI MEMORY STRIP
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,29);
  \fill[TTCDeepNavy, rounded corners=3pt] (0,0) rectangle (186,29);
  \foreach \x in {46.5,93,139.5}{\draw[white!35!gray] (\x,6) -- (\x,23);}
  \node[align=center,text=white] at (23.25,15) {{\fontsize{9}{10}\selectfont\bfseries\color{TTCRed} TỐI ƯU CHI PHÍ}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont Value Engineering}};
  \node[align=center,text=white] at (69.75,15) {{\fontsize{9}{10}\selectfont\bfseries\color{TTCCyan} SONG SONG}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont Controlled Fast-Track}};
  \node[align=center,text=white] at (116.25,15) {{\fontsize{9}{10}\selectfont\bfseries CLASH CHECK}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont Model Coordination}};
  \node[align=center,text=white] at (162.75,15) {{\fontsize{9}{10}\selectfont\bfseries\color{TTCGold} CHANGE CONTROL}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont Scope Discipline}};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_15 = r"""% ============================================================
% TRANG 15: DIGITAL THREAD — BIM, AI, DIGITAL TWIN
% ============================================================
\begin{tikzpicture}[remember picture, overlay]
  \fill[TTCLightBlue]
    ([xshift=122mm,yshift=-31mm]current page.north west) --
    ([xshift=210mm,yshift=-31mm]current page.north west) --
    ([xshift=210mm,yshift=-111mm]current page.north west) -- cycle;
  \node[opacity=.03, text=TTCBlue, font=\fontsize{62}{64}\selectfont\bfseries,
        rotate=90] at ([xshift=-11mm,yshift=7mm]current page.east) {DATA};
  \begin{scope}[shift={(current page.south west)},x=1mm,y=1mm,opacity=.40]
    \draw[TTCBlue!17!white, line width=.8pt] (14,15) -- (196,15);
    \foreach \x in {22,58,94,130,166}{
      \draw[TTCBlue!15!white] (\x,15) -- (\x+12,36) -- (\x+24,15);
      \fill[TTCCyan!10!white] (\x+12,36) circle (2.2);
    }
    \draw[TTCRed!18!white, line width=.7pt] (22,23) -- (190,23);
  \end{scope}
\end{tikzpicture}

\pagefooterbar{Trang 15}
\begin{minipage}[t][246mm]{\textwidth}
\pageheaderbar{MÔ HÌNH THÔNG TIN \& DỮ LIỆU CÔNG TRÌNH}{Trang 15}
\vspace{6mm}
\secbrand{Một Luồng Dữ Liệu Xuyên Suốt Vòng Đời Nhà Máy}{Building Information Modeling, Engineering Review \& Handover Data}

{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
MỘT MÔ HÌNH • BA QUYẾT ĐỊNH • XUYÊN SUỐT VÒNG ĐỜI\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
Dữ liệu thiết kế không dừng ở bản vẽ: nó dẫn dắt mua sắm, thi công, nghiệm thu và vận hành tài sản.\par}
\vspace{3mm}

% HERO — BIM AS DECISION ENVIRONMENT
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,68);
  \clip[rounded corners=3pt] (0,0) rectangle (186,68);
  \node[anchor=center,inner sep=0pt] at (93,34)
    {\includegraphics[width=186mm]{../../public/bim-model-3d.jpg}};
  \fill[TTCDeepNavy,opacity=.88] (0,0) rectangle (61,68);
  \fill[TTCDeepNavy,opacity=.24] (61,0) rectangle (86,68);
  \node[anchor=west,text width=48mm,align=left,text=white] at (8,44) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} TTC DIGITAL THREAD}\\[1.4mm]
    {\fontsize{19}{21}\selectfont\bfseries DATA TO}\\[-.3mm]
    {\fontsize{19}{21}\selectfont\bfseries\color{TTCRed!85!white} DECISION}\\[1.8mm]
    {\fontsize{7}{8.5}\selectfont\color{white!82!gray}
    Một nguồn dữ liệu tin cậy cho thiết kế, công trường và đội vận hành.}
  };
  \node[rounded corners=2pt,fill=white,align=center,minimum width=27mm,
        minimum height=15mm] at (111,15) {
    {\fontsize{9}{10}\selectfont\bfseries\color{TTCBlue} DESIGN}\\[-.2mm]
    {\fontsize{5.8}{7}\selectfont LOD 400 • 5D}
  };
  \node[rounded corners=2pt,fill=TTCCyan,align=center,text=white,
        minimum width=27mm,minimum height=15mm] at (143,15) {
    {\fontsize{9}{10}\selectfont\bfseries BUILD}\\[-.2mm]
    {\fontsize{5.8}{7}\selectfont Clash • 4D}
  };
  \node[rounded corners=2pt,fill=TTCGold,align=center,text=white,
        minimum width=27mm,minimum height=15mm] at (172,15) {
    {\fontsize{9}{10}\selectfont\bfseries OPERATE}\\[-.2mm]
    {\fontsize{5.8}{7}\selectfont Twin • O\&M}
  };
\end{tikzpicture}

\vspace{3mm}

% THREE DECISION ENGINES
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,62);
  \foreach \x/\c in {0/TTCRed,63/TTCCyan,126/TTCGold}{
    \fill[white,rounded corners=2pt] (\x,0) rectangle +(60,62);
    \draw[TTCBorder,rounded corners=2pt,line width=.6pt] (\x,0) rectangle +(60,62);
    \fill[\c,rounded corners=2pt] (\x,58) rectangle +(60,4);
  }
  \node[anchor=north west,text width=50mm] at (5,53) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCRed} 01 / COORDINATE}\\[1mm]
    {\fontsize{11}{12}\selectfont\bfseries\color{TTCBlue} BIM 5D}\\[1.2mm]
    {\fontsize{6.8}{8.2}\selectfont\color{TTCTextDark}
    \textbf{Input:} Kiến trúc • Kết cấu • MEP\newline
    \textbf{Decision:} Clash-check và sequence\newline
    \textbf{Output:} Shop Drawing, BOQ, 4D plan}\\[1mm]
    {\fontsize{6.2}{7.3}\selectfont\bfseries\color{TTCTextMuted} TEKLA • REVIT • NAVISWORKS}
  };
  \node[anchor=north west,text width=50mm] at (68,53) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} 02 / OPTIMIZE}\\[1mm]
    {\fontsize{11}{12}\selectfont\bfseries\color{TTCBlue} AI STRUCTURE}\\[1.2mm]
    {\fontsize{6.8}{8.2}\selectfont\color{TTCTextDark}
    \textbf{Input:} Tải trọng • nhịp • nội lực\newline
    \textbf{Decision:} Lặp phương án tiết diện\newline
    \textbf{Output:} Phương án tiết diện để kỹ sư kiểm tra}\\[1mm]
    {\fontsize{6.2}{7.3}\selectfont\bfseries\color{TTCTextMuted} AISC 360 • TCVN • AIDC R\&D}
  };
  \node[anchor=north west,text width=50mm] at (131,53) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCGold} 03 / OPERATE}\\[1mm]
    {\fontsize{11}{12}\selectfont\bfseries\color{TTCBlue} DIGITAL TWIN}\\[1.2mm]
    {\fontsize{6.8}{8.2}\selectfont\color{TTCTextDark}
    \textbf{Input:} As-built • tài sản • IoT\newline
    \textbf{Decision:} Bảo trì theo trạng thái\newline
    \textbf{Output:} Hồ sơ vận hành có thể truy vết}\\[1mm]
    {\fontsize{6.2}{7.3}\selectfont\bfseries\color{TTCTextMuted} CDE • BMS • SCADA READY}
  };
\end{tikzpicture}

\vspace{3mm}

% DIGITAL THREAD FLOW
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,42);
  \fill[TTCLightBlue,rounded corners=3pt] (0,0) rectangle (186,42);
  \draw[TTCBorder,rounded corners=3pt,line width=.6pt] (0,0) rectangle (186,42);
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries] at (7,34)
    {\faDatabase\quad DIGITAL THREAD — DỮ LIỆU KHÔNG BỊ ĐỨT GÃY};
  \foreach \x/\n/\t in {24/01/MODEL,70/02/APPROVE,116/03/BUILD,162/04/OPERATE}{
    \fill[white] (\x,17) circle (5);
    \draw[TTCBlue,line width=.8pt] (\x,17) circle (5);
    \node[text=TTCRed,font=\fontsize{6.4}{7}\selectfont\bfseries] at (\x,17) {\n};
    \node[anchor=north,align=center,text width=34mm] at (\x,9) {
      {\fontsize{6.7}{8}\selectfont\bfseries\color{TTCBlue} \t}
    };
  }
  \draw[-{Stealth[length=2.2mm]},TTCBlue!45!white,line width=.9pt] (30,17) -- (64,17);
  \draw[-{Stealth[length=2.2mm]},TTCBlue!45!white,line width=.9pt] (76,17) -- (110,17);
  \draw[-{Stealth[length=2.2mm]},TTCBlue!45!white,line width=.9pt] (122,17) -- (156,17);
\end{tikzpicture}

\vspace{3mm}

% KPI MEMORY STRIP
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,29);
  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,29);
  \foreach \x in {46.5,93,139.5}{\draw[white!35!gray] (\x,6) -- (\x,23);}
  \node[align=center,text=white] at (23.25,15) {{\fontsize{9}{10}\selectfont\bfseries\color{TTCRed} LOD 400}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont Fabrication Detail}};
  \node[align=center,text=white] at (69.75,15) {{\fontsize{9}{10}\selectfont\bfseries\color{TTCCyan} REVIEWED}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont Engineering Options}};
  \node[align=center,text=white] at (116.25,15) {{\fontsize{9}{10}\selectfont\bfseries COORDINATED}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont Model Interfaces}};
  \node[align=center,text=white] at (162.75,15) {{\fontsize{9}{10}\selectfont\bfseries\color{TTCGold} TRACEABLE}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont Handover Data}};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_16 = r"""% ============================================================
% TRANG 16: ESG BUSINESS CASE — GREEN FACTORY
% ============================================================
\pageheaderbar{CÔNG TRÌNH XANH ESG \& MÁI SOLAR-READY}{Trang 16}
\pagefooterbar{Trang 16}

\begin{tikzpicture}[remember picture, overlay]
  \fill[TTCLightBlue]
    ([xshift=125mm,yshift=-30mm]current page.north west) --
    ([xshift=210mm,yshift=-30mm]current page.north west) --
    ([xshift=210mm,yshift=-112mm]current page.north west) -- cycle;
  \node[opacity=.03,text=TTCBlue,font=\fontsize{64}{66}\selectfont\bfseries,
        rotate=90] at ([xshift=-11mm,yshift=2mm]current page.east) {ESG};
  % Solar roof rhythm at the bottom
  \begin{scope}[shift={(current page.south west)},x=1mm,y=1mm,opacity=.43]
    \draw[TTCBlue!17!white,line width=.7pt] (14,13) -- (196,13);
    \foreach \x in {18,48,78,108,138,168}{
      \fill[TTCBlue!3!white] (\x,14) -- ++(24,0) -- ++(-5,17) -- ++(-24,0) -- cycle;
      \draw[TTCBlue!16!white] (\x,14) -- ++(24,0) -- ++(-5,17) -- ++(-24,0) -- cycle;
      \draw[TTCBlue!11!white] (\x+4,14) -- (\x-1,31);
      \draw[TTCBlue!11!white] (\x+12,14) -- (\x+7,31);
    }
    \draw[TTCCyan!22!white,line width=.8pt] (24,38) arc[start angle=210,end angle=330,radius=10mm];
    \draw[TTCRed!18!white,line width=.7pt] (24,38) -- (24,45);
  \end{scope}
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Nhà Máy Xanh Được Thiết Kế Như Một Bài Toán Kinh Doanh}{Solar-Ready, Low-Energy Envelope, Water Circularity \& Green Certification}

{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
GIẢM OPEX • SẴN SÀNG CARBON • TĂNG GIÁ TRỊ TÀI SẢN\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
ESG được tích hợp từ kết cấu và vỏ bao che — không phải bổ sung tốn kém sau khi nhà máy đã vận hành.\par}
\vspace{3mm}

% HERO — GREEN FACTORY
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,70);
  \clip[rounded corners=3pt] (0,0) rectangle (186,70);
  \node[anchor=center,inner sep=0pt] at (93,35)
    {\includegraphics[width=186mm]{../../public/bim-esg-factory-3d.jpg}};
  \fill[TTCDeepNavy,opacity=.84] (0,0) rectangle (61,70);
  \fill[TTCDeepNavy,opacity=.22] (61,0) rectangle (87,70);
  \node[anchor=west,text width=48mm,align=left,text=white] at (8,46) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} ESG-BY-DESIGN}\\[1.3mm]
    {\fontsize{17}{19}\selectfont\bfseries NET-ZERO}\\[-.2mm]
    {\fontsize{17}{19}\selectfont\bfseries\color{TTCRed!85!white} READY}\\[1.8mm]
    {\fontsize{7}{8.5}\selectfont\color{white!82!gray}
    Kết cấu, năng lượng, nước và vận hành được chuẩn bị trong cùng một mô hình.}
  };
  \node[rounded corners=2pt,fill=white,align=center,minimum width=31mm,
        minimum height=15mm] at (121,15) {
    {\fontsize{10}{11}\selectfont\bfseries\color{TTCRed} SOLAR}\\[-.2mm]
    {\fontsize{5.8}{7}\selectfont\color{TTCBlue} SOLAR-READY}
  };
  \node[rounded corners=2pt,fill=TTCCyan,align=center,text=white,
        minimum width=31mm,minimum height=15mm] at (155,15) {
    {\fontsize{10}{11}\selectfont\bfseries PASSIVE}\\[-.2mm]
    {\fontsize{5.8}{7}\selectfont ENVELOPE DESIGN}
  };
\end{tikzpicture}

\vspace{3mm}

% FOUR ESG LEVERS
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,51);
  \foreach \x/\c in {0/TTCRed,47.5/TTCCyan,95/TTCBlue,142.5/TTCGold}{
    \fill[white,rounded corners=2pt] (\x,0) rectangle +(43.5,51);
    \draw[TTCBorder,rounded corners=2pt,line width=.6pt] (\x,0) rectangle +(43.5,51);
    \fill[\c,rounded corners=2pt] (\x,47) rectangle +(43.5,4);
  }
  \node[anchor=north west,text width=35mm] at (4,43) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCRed} 01 / ENERGY}\\[1mm]
    {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCBlue} SOLAR-READY}\\[1mm]
    {\fontsize{6.5}{7.8}\selectfont\color{TTCTextDark}
    Dự phòng tải mái, xà gồ và giao diện lắp đặt theo dữ liệu hệ pin được duyệt.}
  };
  \node[anchor=north west,text width=35mm] at (51.5,43) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} 02 / ENVELOPE}\\[1mm]
    {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCBlue} COOL ROOF}\\[1mm]
    {\fontsize{6.5}{7.8}\selectfont\color{TTCTextDark}
    Panel PIR/Rockwool và mái phản xạ nhiệt giảm tải HVAC.}
  };
  \node[anchor=north west,text width=35mm] at (99,43) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCBlue} 03 / WATER}\\[1mm]
    {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCBlue} CIRCULARITY}\\[1mm]
    {\fontsize{6.5}{7.8}\selectfont\color{TTCTextDark}
    Nước thải Cột A, thu nước mưa và tái sử dụng cho cảnh quan.}
  };
  \node[anchor=north west,text width=35mm] at (146.5,43) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCGold} 04 / STANDARD}\\[1mm]
    {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCBlue} LEED / LOTUS}\\[1mm]
    {\fontsize{6.5}{7.8}\selectfont\color{TTCTextDark}
    Mô phỏng năng lượng, vật liệu Low-VOC và hồ sơ chứng nhận.}
  };
\end{tikzpicture}

\vspace{3mm}

% ESG BUSINESS CASE
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,47);
  \fill[TTCLightBlue,rounded corners=3pt] (0,0) rectangle (186,47);
  \draw[TTCBorder,rounded corners=3pt,line width=.6pt] (0,0) rectangle (186,47);
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries] at (7,39)
    {\faGlobeAmericas\quad GIÁ TRỊ CHO CHỦ ĐẦU TƯ QUỐC TẾ};
  \foreach \x in {62,124}{\draw[TTCBorder] (\x,6) -- (\x,31);}
  \node[align=left,text width=50mm,anchor=north west] at (6,30) {
    {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCRed} GREEN FINANCE}\\[.7mm]
    {\fontsize{6.5}{7.8}\selectfont\color{TTCTextDark}
    Tăng khả năng tiếp cận nguồn vốn xanh và tiêu chí chuỗi cung ứng quốc tế.}
  };
  \node[align=left,text width=50mm,anchor=north west] at (68,30) {
    {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCCyan} CARBON READY}\\[.7mm]
    {\fontsize{6.5}{7.8}\selectfont\color{TTCTextDark}
    Chuẩn bị dữ liệu năng lượng, vật liệu và lộ trình giảm phát thải theo yêu cầu dự án.}
  };
  \node[align=left,text width=50mm,anchor=north west] at (130,30) {
    {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCGold} LOWER OPEX}\\[.7mm]
    {\fontsize{6.5}{7.8}\selectfont\color{TTCTextDark}
    Giảm điện HVAC, tối ưu nước vận hành và nâng giá trị khai thác tài sản.}
  };
\end{tikzpicture}

\vspace{3mm}

% KPI MEMORY STRIP
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,29);
  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,29);
  \foreach \x in {46.5,93,139.5}{\draw[white!35!gray] (\x,6) -- (\x,23);}
  \node[align=center,text=white] at (23.25,15) {{\fontsize{9}{10}\selectfont\bfseries\color{TTCRed} SOLAR-READY}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont Approved System Data}};
  \node[align=center,text=white] at (69.75,15) {{\fontsize{9}{10}\selectfont\bfseries\color{TTCCyan} LOW-ENERGY}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont Envelope Strategy}};
  \node[align=center,text=white] at (116.25,15) {{\fontsize{9}{10}\selectfont\bfseries WATER}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont Project Requirements}};
  \node[align=center,text=white] at (162.75,15) {{\fontsize{9}{10}\selectfont\bfseries\color{TTCGold} GREEN DOSSIER}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont Certification Support}};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_17_LEGACY = r"""% ============================================================
% TRANG 17: CHUYỂN ĐỔI SỐ HIỆN TRƯỜNG: FACEID & CAMERA AI 24/7
% ============================================================
\pageheaderbar{CHUYỂN ĐỔI SỐ HIỆN TRƯỜNG \& CAMERA AI}{Trang 17}
\pagefooterbar{Trang 17}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.03, scale=2.8, font=\bfseries\sffamily, text=TTCBlue] at ([yshift=-10mm]current page.center) {SMART SITE DIGITIZATION \& AI CAMERAS};
  \draw[TTCBlue!6!white, line width=0.5pt] ([xshift=15mm, yshift=20mm]current page.south west) grid[step=8mm] ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Chuyển Đổi Số Hiện Trường: Cổng FaceID, Camera AI \& Nhật Ký Số}{Smart Site Monitoring: AI-Powered Computer Vision, Biometric FaceID \& Cloud CDE Collaboration}

% TẦNG 1: 4 CÔNG NGHỆ QUẢN LÝ THI CÔNG THÔNG MINH
\noindent
\begin{tabular}{@{}p{91mm}@{\hspace{4mm}}p{91mm}@{}}
  % Công nghệ 1: FaceID
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=48mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCRed} \faUserCheck\quad 1. CỔNG KIỂM SOÁT FACEID \& THẺ SỐ HÓA:}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      \textbullet\ Điểm danh nhận diện khuôn mặt AI, đối soát 100\% danh sách công nhân đã qua đào tạo an toàn HSE.\newline
      \textbullet\ Tự động từ chối vào cổng đối với nhân sự chưa học an toàn hoặc thiếu chứng chỉ nghề hợp lệ.\newline
      \textbullet\ Dữ liệu quân số công trường được cập nhật thời gian thực lên Dashboard quản trị của Chủ đầu tư.}
    };
  \end{tikzpicture} &
  % Công nghệ 2: Camera AI
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=48mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCCyan} \faVideo\quad 2. HỆ THỐNG CAMERA AI GIÁM SÁT 24/7:}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      \textbullet\ Thuật toán thị giác máy tính tự động phát hiện vi phạm bảo hộ (không đội mũ, không đeo dây an toàn).\newline
      \textbullet\ Cảnh báo xâm nhập vùng nguy cơ cao (dưới bán kính quay của cẩu 100T, khu vực đào hố sâu).\newline
      \textbullet\ Phát còi cảnh báo tức thì tại hiện trường và gửi thông báo khẩn cấp tới Chỉ huy trưởng.}
    };
  \end{tikzpicture}
  \\[2mm]
  % Công nghệ 3: Nhật ký số & CDE
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=48mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCBlue} \faCloud\quad 3. NHẬT KÝ THI CÔNG SỐ \& CDE CLOUD:}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      \textbullet\ Ký số nhật ký công trường trực tuyến hàng ngày kèm hình ảnh định vị GPS và thông số thời tiết.\newline
      \textbullet\ Đồng bộ toàn bộ hồ sơ nghiệm thu ITP, kết quả thí nghiệm Las-XD lên môi trường dữ liệu chung CDE.\newline
      \textbullet\ Triệt tiêu hoàn toàn rủi ro thất lạc hồ sơ và tăng tốc độ giải ngân thanh toán.}
    };
  \end{tikzpicture} &
  % Công nghệ 4: Báo cáo tiến độ & phê duyệt số
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=48mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCGold} \faChartLine\quad 4. BÁO CÁO TIẾN ĐỘ \& PHÊ DUYỆT SỐ:}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      \textbullet\ Hình ảnh hiện trường được cập nhật định kỳ, có thời gian và vị trí để kiểm chứng tiến độ.\newline
      \textbullet\ So sánh trực tiếp giữa mô hình thiết kế BIM và hiện trạng thi công để phát hiện sai lệch kịp thời.\newline
      \textbullet\ Báo cáo tiến độ trực quan gửi cho Ban Lãnh đạo Chủ đầu tư tại nước ngoài.}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{2mm}

% TẦNG 2: BẢNG TRẢI NGHIỆM QUẢN TRỊ TỪ XA CHO FDI
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
    {\fontsize{9}{11}\selectfont\bfseries\color{TTCBlue} \faMobile*\quad TRẢI NGHIỆM QUẢN TRỊ DỰ ÁN TỪ XA CHO CHỦ ĐẦU TƯ FDI:}\\[3pt]
    \begin{tabularx}{\linewidth}{@{}p{56mm}@{\hspace{4mm}}p{56mm}@{\hspace{4mm}}p{56mm}@{}}
      \textbf{\color{TTCRed}1. Xem Trực Tiếp Mọi Lúc:}\newline
      {\fontsize{6.8}{8.5}\selectfont Ban Giám đốc tại Tokyo, Seoul hay Đài Bắc có thể theo dõi trực tiếp hình ảnh thi công qua ứng dụng di động 24/7.} &
      \textbf{\color{TTCCyan}2. Minh Bạch Dữ Liệu 100\%:}\newline
      {\fontsize{6.8}{8.5}\selectfont Mọi thông số về quân số, vật tư nhập công trường và tiến độ CPM đều được cập nhật thời gian thực không độ trễ.} &
      \textbf{\color{TTCBlue}3. Phê Duyệt RFI Nhanh Chóng:}\newline
      {\fontsize{6.8}{8.5}\selectfont Xử lý phiếu yêu cầu thông tin RFI và bản vẽ Shop Drawing trực tuyến trên CDE, rút ngắn thời gian chờ đợi.}
    \end{tabularx}
  };
\end{tikzpicture}

\vspace{2mm}

% TẦNG 3: BĂNG KPI DIGITAL SITE
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
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCRed} 100\% FACEID} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCCyan} 24/7 AI} &
      {\fontsize{14}{16}\selectfont\bfseries\color{white} CDE CLOUD} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCGold} RFI ONLINE} \\
      {\fontsize{7.2}{9}\selectfont Điểm Danh Quân Số} &
      {\fontsize{7.2}{9}\selectfont Camera Nhận Diện Vi Phạm} &
      {\fontsize{7.2}{9}\selectfont Dữ Liệu Thi Công Số} &
      {\fontsize{7.2}{9}\selectfont Phê Duyệt Trực Tuyến}
    \end{tabularx}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_18_LEGACY = r"""% ============================================================
% TRANG 18: HỆ THỐNG QA/QC 4 TẦNG & CHUẨN HÀN MỸ AWS D1.1
% ============================================================
\pageheaderbar{HỆ THỐNG QUẢN LÝ CHẤT LƯỢNG QA/QC}{Trang 18}
\pagefooterbar{Trang 18}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.03, scale=2.8, font=\bfseries\sffamily, text=TTCBlue] at ([yshift=-10mm]current page.center) {QUALITY ASSURANCE \& AWS D1.1 STANDARDS};
  \draw[TTCBlue!6!white, line width=0.5pt] ([xshift=15mm, yshift=20mm]current page.south west) grid[step=8mm] ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Hệ Thống Quản Lý Chất Lượng QA/QC \& Kiểm Soát Mối Hàn AWS D1.1}{Comprehensive 4-Tier ITP Inspection, Non-Destructive Testing (NDT) \& AWS D1.1 Certification}

% TẦNG 1: QUY TRÌNH NGHIỆM THU 4 TẦNG (ITP)
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
    {\fontsize{9.5}{11.5}\selectfont\bfseries\color{TTCBlue} \faCheckDouble\quad QUY TRÌNH NGHIỆM THU 4 TẦNG CHẶT CHẼ (INSPECTION \& TEST PLAN -- ITP):}\\[3pt]
    \begin{tabularx}{\linewidth}{@{}p{86mm}@{\hspace{4mm}}p{86mm}@{}}
      \textbf{\color{TTCRed}TẦNG 1: TỰ KIỂM SOÁT TỔ ĐỘI THI CÔNG} &
      \textbf{\color{TTCCyan}TẦNG 3: BỘ PHẬN QA/QC CHUYÊN TRÁCH TTC} \\
      {\fontsize{6.8}{8.5}\selectfont
      \textbullet\ Tổ trưởng và thợ chính tự kiểm tra kích thước hình học, độ phẳng và mối hàn trước khi báo nghiệm thu.\newline
      \textbullet\ Lập phiếu tự kiểm tra nội bộ theo biểu mẫu chuẩn ISO.} &
      {\fontsize{6.8}{8.5}\selectfont
      \textbullet\ Kỹ sư QA/QC độc lập kiểm tra lại toàn bộ thông số kỹ thuật, lập biên bản nghiệm thu nội bộ.\newline
      \textbullet\ Thực hiện thí nghiệm phá hủy/không phá hủy (NDT) trước khi mời Tư vấn giám sát.} \\[3pt]
      \textbf{\color{TTCBlue}TẦNG 2: KỸ SƯ HIỆN TRƯỜNG GIÁM SÁT} &
      \textbf{\color{TTCGold}TẦNG 4: TƯ VẤN GIÁM SÁT \& CHỦ ĐẦU TƯ} \\
      {\fontsize{6.8}{8.5}\selectfont
      \textbullet\ Kỹ sư giám sát khu vực kiểm tra đối chiếu bản vẽ Shop Drawing và tiêu chuẩn kỹ thuật.\newline
      \textbullet\ Ký xác nhận đủ điều kiện chuyển bước thi công.} &
      {\fontsize{6.8}{8.5}\selectfont
      \textbullet\ Tổ chức nghiệm thu chính thức cùng Tư vấn giám sát và Đại diện Chủ đầu tư.\newline
      \textbullet\ Ký biên bản nghiệm thu ITP và số hóa lưu trữ trên hệ thống CDE.}
    \end{tabularx}
  };
\end{tikzpicture}

\vspace{2mm}

% TẦNG 2: 4 PHƯƠNG PHÁP KIỂM TRA MỐI HÀN SIÊU ÂM (NDT)
\noindent
\begin{tabular}{@{}p{42.5mm}@{\hspace{3mm}}p{42.5mm}@{\hspace{3mm}}p{42.5mm}@{\hspace{3mm}}p{42.5mm}@{}}
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=42.5mm, minimum height=48mm, inner sep=4pt, text width=38mm, align=left] {
      {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCRed} \faEye\ Kiểm Tra Mắt (VT)}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ 100\% mối hàn kiểm tra ngoại quan bề mặt.\newline
      \textbullet\ Đo kích thước cạnh hàn, độ ngấu, độ lồi lõm.\newline
      \textbullet\ Phát hiện rỗ khí, nứt bề mặt và khuyết tật cháy chân.}
    };
  \end{tikzpicture} &
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=42.5mm, minimum height=48mm, inner sep=4pt, text width=38mm, align=left] {
      {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCCyan} \faWaveSquare\ Siêu Âm Mối Hàn (UT)}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ Kiểm tra siêu âm 100\% mối hàn chịu lực chính dầm cột.\newline
      \textbullet\ Phát hiện khuyết tật ngầm bên trong (nứt, xỉ hàn, ngậm khí).\newline
      \textbullet\ Đạt chuẩn chấp nhận khắt khe của AWS D1.1.}
    };
  \end{tikzpicture} &
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=42.5mm, minimum height=48mm, inner sep=4pt, text width=38mm, align=left] {
      {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCBlue} \faMagnet\ Hạt Từ \& Thẩm Thấu}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ Thử hạt từ (MT) phát hiện nứt vi mô sát bề mặt.\newline
      \textbullet\ Thẩm thấu chất lỏng (PT) kiểm tra mối hàn góc.\newline
      \textbullet\ Đảm bảo tính liên tục tuyệt đối của kim loại hàn.}
    };
  \end{tikzpicture} &
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=42.5mm, minimum height=48mm, inner sep=4pt, text width=38mm, align=left] {
      {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCGold} \faAward\ Thí Nghiệm Độc Lập}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ Phòng thí nghiệm Las-XD độc lập cấp chứng nhận.\newline
      \textbullet\ Kéo thử tải bu-lông cường độ cao 8.8 / 10.9.\newline
      \textbullet\ Nén mẫu bê tông móng cọc 7 ngày, 28 ngày.}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{2mm}

% TẦNG 3: BĂNG KPI QA/QC
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
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCRed} 100\%} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCCyan} AWS D1.1} &
      {\fontsize{14}{16}\selectfont\bfseries\color{white} ISO 9001} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCGold} 0 DEFECT} \\
      {\fontsize{7.2}{9}\selectfont Siêu Âm Mối Hàn Chịu Lực} &
      {\fontsize{7.2}{9}\selectfont Chuẩn Hàn Kết Cấu Mỹ} &
      {\fontsize{7.2}{9}\selectfont Hệ Thống Quản Lý Chất Lượng} &
      {\fontsize{7.2}{9}\selectfont Mục Tiêu Nghiệm Thu Bàn Giao}
    \end{tabularx}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_19_LEGACY = r"""% ============================================================
% TRANG 19: AN TOÀN LAO ĐỘNG HSE & CHÍNH SÁCH ZERO ACCIDENT
% ============================================================
\pageheaderbar{AN TOÀN LAO ĐỘNG HSE \& ZERO ACCIDENT}{Trang 19}
\pagefooterbar{Trang 19}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.03, scale=2.8, font=\bfseries\sffamily, text=TTCBlue] at ([yshift=-10mm]current page.center) {HEALTH SAFETY ENVIRONMENT \& ZERO ACCIDENT};
  \draw[TTCBlue!6!white, line width=0.5pt] ([xshift=15mm, yshift=20mm]current page.south west) grid[step=8mm] ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Chính Sách An Toàn HSE \& Cam Kết Tuyệt Đối Zero Accident}{Health, Safety \& Environment (HSE), ISO 45001:2018 \& Uncompromising Zero Accident Culture}

% TẦNG 1: 4 NGUYÊN TẮC VÀNG HSE
\noindent
\begin{tabular}{@{}p{91mm}@{\hspace{4mm}}p{91mm}@{}}
  % Nguyên tắc 1: Zero Accident
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=48mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCRed} \faShield*\quad 1. CHÍNH SÁCH ZERO ACCIDENT:}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      \textbullet\ Mọi tai nạn lao động đều có thể phòng ngừa nếu tuân thủ đúng quy trình.\newline
      \textbullet\ An toàn tính mạng con người luôn được ưu tiên cao hơn tiến độ và chi phí.\newline
      \textbullet\ Quyền dừng công việc (Stop Work Authority): Bất kỳ công nhân nào cũng có quyền dừng thi công khi phát hiện nguy cơ mất an toàn.}
    };
  \end{tikzpicture} &
  % Nguyên tắc 2: PPE chuẩn 3M
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=48mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCCyan} \faHardHat\quad 2. 100\% BẢO HỘ ĐẠT CHUẨN QUỐC TẾ:}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      \textbullet\ Trang bị 100\% bảo hộ lao động tiêu chuẩn Châu Âu: Mũ bảo hộ chống va đập, kính bảo vệ mắt, giày mũi thép chống đinh.\newline
      \textbullet\ Dây an toàn toàn thân 2 móc giảm chấn (chuẩn CE/ANSI) bắt buộc khi làm việc trên độ cao từ 2m trở lên.\newline
      \textbullet\ Lưới an toàn hứng rơi toàn bộ chu vi dầm mái trong suốt quá trình lợp tôn.}
    };
  \end{tikzpicture}
  \\[2mm]
  % Nguyên tắc 3: Huấn luyện an toàn
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=48mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCBlue} \faUsers\quad 3. HUẤN LUYỆN \& ĐIỂM DANH FACEID:}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      \textbullet\ Huấn luyện an toàn đầu giờ (Toolbox Talk) 15 phút mỗi sáng trước khi bắt đầu ca làm việc.\newline
      \textbullet\ Phổ biến cụ thể các biện pháp phòng ngừa rủi ro cho từng hạng mục công việc trong ngày.\newline
      \textbullet\ Điểm danh nhận diện khuôn mặt FaceID đảm bảo 100\% nhân sự đã tham gia Toolbox Talk.}
    };
  \end{tikzpicture} &
  % Nguyên tắc 4: PCCC & Cứu nạn
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=48mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCGold} \faFireExtinguisher\quad 4. PCCC \& PHẢN ỨNG KHẨN CẤP 24/7:}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      \textbullet\ Bố trí bình chữa cháy xách tay, họng nước vách tường tại mọi vị trí có nguy cơ phát sinh tia lửa hàn.\newline
      \textbullet\ Thành lập đội PCCC và cứu hộ cứu nạn cơ sở thường trực tại công trường.\newline
      \textbullet\ Diễn tập định kỳ phương án sơ tán khẩn cấp và xử lý sự cố hàng quý.}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{2mm}

% TẦNG 2: BẢNG 5 NGUYÊN TẮC VÀNG AN TOÀN HIỆN TRƯỜNG
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
    {\fontsize{9}{11}\selectfont\bfseries\color{TTCBlue} \faHandPaper\quad 5 NGUYÊN TẮC VÀNG BẮT BUỘC TUÂN THỦ TẠI MỌI CÔNG TRƯỜNG TTC:}\\[3pt]
    \begin{tabularx}{\linewidth}{@{}Y|Y|Y|Y|Y@{}}
      \textbf{\color{TTCRed}1. Làm Việc Trên Cao} &
      \textbf{\color{TTCBlue}2. Nâng Hạ Cẩu 100T} &
      \textbf{\color{TTCCyan}3. An Toàn Điện} &
      \textbf{\color{TTCGold}4. Công Tác Hàn Cắt} &
      \textbf{\color{TTCBlue}5. Hố Móng Sâu} \\[2pt]
      {\fontsize{6.8}{8.5}\selectfont Đeo dây an toàn 2 móc, có dây cứu sinh \& lưới hứng rơi.} &
      {\fontsize{6.8}{8.5}\selectfont Cấm tuyệt đối đứng dưới bán kính quay của cẩu.} &
      {\fontsize{6.8}{8.5}\selectfont Tủ điện có aptomat chống giật ELCB 30mA.} &
      {\fontsize{6.8}{8.5}\selectfont Có bạt chắn xỉ hàn chống cháy \& bình PCCC bên cạnh.} &
      {\fontsize{6.8}{8.5}\selectfont Có rào chắn an toàn, biển cảnh báo \& đèn chiếu sáng đêm.}
    \end{tabularx}
  };
\end{tikzpicture}

\vspace{2mm}

% TẦNG 3: BĂNG KPI HSE
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
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCRed} >3.5M GIỜ} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCCyan} 0 TAI NẠN} &
      {\fontsize{14}{16}\selectfont\bfseries\color{white} ISO 45001} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCGold} 100\% PPE} \\
      {\fontsize{7.2}{9}\selectfont Giờ Công An Toàn Tích Lũy} &
      {\fontsize{7.2}{9}\selectfont Tai Nạn Nghiêm Trọng} &
      {\fontsize{7.2}{9}\selectfont An Toàn Sức Khỏe LĐ} &
      {\fontsize{7.2}{9}\selectfont Trang Bị Bảo Hộ Chuẩn}
    \end{tabularx}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_17 = r"""% ============================================================
% TRANG 17: DIGITAL SITE CONTROL CENTER
% ============================================================
\pageheaderbar{TRUNG TÂM ĐIỀU HÀNH CÔNG TRƯỜNG SỐ}{Trang 17}
\pagefooterbar{Trang 17}

\begin{tikzpicture}[remember picture, overlay]
  \fill[TTCLightBlue]
    ([xshift=131mm,yshift=-30mm]current page.north west) --
    ([xshift=210mm,yshift=-30mm]current page.north west) --
    ([xshift=210mm,yshift=-115mm]current page.north west) -- cycle;
  % Data pulse background — deliberately different from the previous pages
  \begin{scope}[shift={(current page.south west)},x=1mm,y=1mm,opacity=.45]
    \draw[TTCBlue!18!white,line width=.8pt] (13,17) -- (197,17);
    \draw[TTCBlue!15!white] (20,17) -- (38,35) -- (62,25) -- (86,45) --
      (112,29) -- (139,42) -- (164,26) -- (191,38);
    \foreach \x/\y in {20/17,38/35,62/25,86/45,112/29,139/42,164/26,191/38}{
      \fill[TTCCyan!20!white] (\x,\y) circle (1.7);
      \draw[TTCBlue!20!white] (\x,\y) circle (3.1);
    }
  \end{scope}
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Trung Tâm Điều Hành Công Trường Số}{Dữ liệu tập trung • Cảnh báo tức thời • Hồ sơ truy xuất được}

{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
MỘT CÔNG TRƯỜNG • BA NGUỒN DỮ LIỆU • MỘT ĐẦU MỐI ĐIỀU HÀNH\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
Tập trung dữ liệu con người, an toàn và hồ sơ thi công để Chỉ huy trưởng xử lý đúng việc, đúng thời điểm.\par}
\vspace{3mm}

% CONTROL CENTER DASHBOARD
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,101);
  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,101);
  \draw[TTCCyan!65!white,rounded corners=3pt,line width=.8pt] (0,0) rectangle (186,101);

  \node[anchor=west,text=white,font=\fontsize{8}{9.5}\selectfont\bfseries] at (8,93)
    {\faDesktop\quad TRUNG TÂM ĐIỀU HÀNH};
  \node[anchor=east,text=TTCCyan,font=\fontsize{6.3}{7.5}\selectfont\bfseries] at (121,93)
    {DỮ LIỆU THẬT • HÀNH ĐỘNG CÓ LƯU VẾT};

  % Status row
  \foreach \x/\c in {8/TTCRed,47/TTCCyan,86/TTCGold}{
    \fill[white!7!TTCDeepNavy,rounded corners=2pt] (\x,63) rectangle +(34,21);
    \draw[\c!70!white,rounded corners=2pt,line width=.55pt] (\x,63) rectangle +(34,21);
  }
  \node[anchor=west,text=TTCRed,font=\fontsize{6.2}{7.3}\selectfont\bfseries] at (11,78) {KIỂM SOÁT RA VÀO};
  \node[anchor=west,text=white,font=\fontsize{9.2}{10.5}\selectfont\bfseries] at (11,70) {ĐÚNG NGƯỜI};
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.2}{7.3}\selectfont\bfseries] at (50,78) {GIÁM SÁT AN TOÀN};
  \node[anchor=west,text=white,font=\fontsize{9.2}{10.5}\selectfont\bfseries] at (50,70) {ĐÚNG QUY TẮC};
  \node[anchor=west,text=TTCGold,font=\fontsize{6.2}{7.3}\selectfont\bfseries] at (89,78) {HỒ SƠ HIỆN TRƯỜNG};
  \node[anchor=west,text=white,font=\fontsize{9.2}{10.5}\selectfont\bfseries] at (89,70) {ĐÚNG PHIÊN BẢN};

  % Three real data streams
  \fill[white,rounded corners=2pt] (8,29) rectangle (40,55);
  \fill[white,rounded corners=2pt] (47,29) rectangle (79,55);
  \fill[white,rounded corners=2pt] (86,29) rectangle (118,55);
  \node[align=center,text width=27mm] at (24,42) {
    {\fontsize{7.5}{9}\selectfont\bfseries\color{TTCRed} NHÂN SỰ}\\[-.2mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}FaceID • đào tạo\\chứng chỉ vào cổng}
  };
  \node[align=center,text width=27mm] at (63,42) {
    {\fontsize{7.5}{9}\selectfont\bfseries\color{TTCCyan} AN TOÀN}\\[-.2mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}Camera AI • PPE\\vùng nguy hiểm}
  };
  \node[align=center,text width=27mm] at (102,42) {
    {\fontsize{7.5}{9}\selectfont\bfseries\color{TTCGold} HỒ SƠ}\\[-.2mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}CDE • ITP • RFI\\nhật ký số}
  };
  \draw[-{Stealth[length=2mm]},TTCCyan,line width=.8pt] (40.5,42) -- (46,42);
  \draw[-{Stealth[length=2mm]},TTCCyan,line width=.8pt] (79.5,42) -- (85,42);

  % Decision layer
  \fill[TTCCyan!12!TTCDeepNavy,rounded corners=2pt] (8,7) rectangle (118,21);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6}{7}\selectfont\bfseries] at (12,14)
    {LỚP ĐIỀU HÀNH};
  \node[anchor=west,text=white,font=\fontsize{7}{8.5}\selectfont\bfseries] at (40,14)
    {Cảnh báo → Phân công → Phê duyệt → Lưu bằng chứng};

  % Ảnh hiện trường có vùng chú thích riêng, không đặt chữ lên ảnh
  \begin{scope}
    \clip[rounded corners=2pt] (126,16) rectangle (179,86);
    \node[anchor=center,inner sep=0pt] at (152.5,51)
      {\includegraphics[height=70mm]{../../public/c_level_site_inspection.jpg}};
  \end{scope}
  \draw[white!45!gray,rounded corners=2pt,line width=.6pt] (126,16) rectangle (179,86);
  \fill[TTCBlue] (126,7) rectangle (179,15);
  \node[text=white,font=\fontsize{6.4}{7.5}\selectfont\bfseries] at (152.5,11)
    {HÌNH ẢNH HIỆN TRƯỜNG};
\end{tikzpicture}

\vspace{3mm}

% OWNER VIEW — THREE OUTCOMES
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,49);
  \fill[white,rounded corners=3pt] (0,0) rectangle (186,49);
  \draw[TTCBorder,rounded corners=3pt,line width=.6pt] (0,0) rectangle (186,49);
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries] at (7,41)
    {\faMobile*\quad THÔNG TIN ĐỦ ĐỂ RA QUYẾT ĐỊNH};
  \foreach \x in {62,124}{\draw[TTCBorder] (\x,7) -- (\x,33);}
  \node[anchor=north west,text width=50mm] at (6,31) {
    {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCRed} QUÂN SỐ SẴN SÀNG}\\[.7mm]
    {\fontsize{6.6}{8}\selectfont\color{TTCTextDark}
    Biết ai đang ở công trường và điều kiện vào cổng của từng người.}
  };
  \node[anchor=north west,text width=50mm] at (68,31) {
    {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCCyan} AN TOÀN HIỂN THỊ}\\[.7mm]
    {\fontsize{6.6}{8}\selectfont\color{TTCTextDark}
    Cảnh báo vi phạm PPE và xâm nhập vùng nguy hiểm để xử lý tức thời.}
  };
  \node[anchor=north west,text width=50mm] at (130,31) {
    {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCGold} HỒ SƠ ĐẦY ĐỦ}\\[.7mm]
    {\fontsize{6.6}{8}\selectfont\color{TTCTextDark}
    Nhật ký, RFI và hồ sơ ITP có thời gian, người duyệt và bằng chứng.}
  };
\end{tikzpicture}

\vspace{3mm}

% ACTION LOOP — NO KPI GRID
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,43);
  \fill[TTCLightBlue,rounded corners=3pt] (0,0) rectangle (186,43);
  \draw[TTCBorder,rounded corners=3pt,line width=.6pt] (0,0) rectangle (186,43);
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries] at (7,35)
    {\faCheckCircle\quad VÒNG LẶP HÀNH ĐỘNG TRONG NGÀY};
  \foreach \x/\n/\t in {23/01/GHI NHẬN,69/02/CẢNH BÁO,115/03/XỬ LÝ,161/04/LƯU VẾT}{
    \fill[white] (\x,17) circle (5);
    \draw[TTCBlue,line width=.8pt] (\x,17) circle (5);
    \node[text=TTCRed,font=\fontsize{6.3}{7}\selectfont\bfseries] at (\x,17) {\n};
    \node[anchor=north,align=center,text width=34mm] at (\x,9)
      {{\fontsize{6.7}{8}\selectfont\bfseries\color{TTCBlue} \t}};
  }
  \draw[-{Stealth[length=2mm]},TTCBlue!45!white,line width=.9pt] (29,17) -- (63,17);
  \draw[-{Stealth[length=2mm]},TTCBlue!45!white,line width=.9pt] (75,17) -- (109,17);
  \draw[-{Stealth[length=2mm]},TTCBlue!45!white,line width=.9pt] (121,17) -- (155,17);
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_18 = r"""% ============================================================
% TRANG 18: QUALITY PASSPORT & RELEASE GATES
% ============================================================
\pageheaderbar{HỆ THỐNG QUẢN LÝ CHẤT LƯỢNG QA/QC}{Trang 18}
\pagefooterbar{Trang 18}

\begin{tikzpicture}[remember picture, overlay]
  \fill[TTCLightBlue]
    ([xshift=121mm,yshift=-31mm]current page.north west) --
    ([xshift=210mm,yshift=-31mm]current page.north west) --
    ([xshift=210mm,yshift=-118mm]current page.north west) -- cycle;
  % document trace lines at the bottom
  \begin{scope}[shift={(current page.south west)},x=1mm,y=1mm,opacity=.43]
    \draw[TTCBlue!17!white,line width=.7pt] (14,15) -- (196,15);
    \foreach \x in {18,56,94,132,170}{
      \draw[TTCBlue!15!white,rounded corners=1pt] (\x,15) rectangle +(25,28);
      \draw[TTCRed!14!white] (\x+5,35) -- (\x+20,35);
      \draw[TTCBlue!11!white] (\x+5,29) -- (\x+20,29);
      \draw[TTCBlue!11!white] (\x+5,23) -- (\x+16,23);
    }
  \end{scope}
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Hộ Chiếu Chất Lượng Cho Từng Gói Công Việc}{Kiểm soát ITP bốn cấp • Đủ bằng chứng mới chuyển bước}

{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
CHỈ CHUYỂN BƯỚC KHI ĐÃ CÓ ĐỦ BẰNG CHỨNG\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
Mỗi vật liệu, mối hàn và hạng mục được kiểm tra, ký xác nhận và lưu vết trước khi phát hành cho bước tiếp theo.\par}
\vspace{3mm}

% QUALITY GATES + PASSPORT
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,122);

  % Left release ladder
  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (57,122);
  \node[anchor=west,text=TTCCyan,font=\fontsize{7}{8}\selectfont\bfseries] at (6,113)
    {4 CẤP KIỂM SOÁT};
  \node[anchor=west,text=white,font=\fontsize{11}{12}\selectfont\bfseries] at (6,106.5)
    {CỔNG ITP};

  \foreach \y/\n/\c in {78/01/TTCRed,52/02/TTCBlue,26/03/TTCCyan,0/04/TTCGold}{
    \fill[white,rounded corners=2pt] (6,\y+6) rectangle (51,\y+25);
    \draw[\c,rounded corners=2pt,line width=.7pt] (6,\y+6) rectangle (51,\y+25);
    \fill[\c] (6,\y+6) rectangle (13,\y+25);
    \node[text=white,font=\fontsize{6.5}{7}\selectfont\bfseries] at (9.5,\y+15.5) {\n};
  }
  \node[anchor=west,text width=33mm] at (16,93.5) {
    {\fontsize{7.2}{8.5}\selectfont\bfseries\color{TTCRed} TỔ ĐỘI TỰ KIỂM}\\[-.2mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}Phiếu tự kiểm nội bộ}
  };
  \node[anchor=west,text width=33mm] at (16,67.5) {
    {\fontsize{7.2}{8.5}\selectfont\bfseries\color{TTCBlue} KỸ SƯ HIỆN TRƯỜNG}\\[-.2mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}Bản vẽ thi công • ITP}
  };
  \node[anchor=west,text width=33mm] at (16,41.5) {
    {\fontsize{7.2}{8.5}\selectfont\bfseries\color{TTCCyan} QA/QC ĐỘC LẬP}\\[-.2mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}Biên bản NDT • kết quả thử}
  };
  \node[anchor=west,text width=33mm] at (16,15.5) {
    {\fontsize{7.2}{8.5}\selectfont\bfseries\color{TTCGold} TVGS / CHỦ ĐẦU TƯ}\\[-.2mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}Chấp thuận cuối}
  };
  \draw[-{Stealth[length=2mm]},white!55!gray,line width=.8pt] (28.5,83) -- (28.5,78);
  \draw[-{Stealth[length=2mm]},white!55!gray,line width=.8pt] (28.5,57) -- (28.5,52);
  \draw[-{Stealth[length=2mm]},white!55!gray,line width=.8pt] (28.5,31) -- (28.5,26);

  % Right quality passport
  \fill[white,rounded corners=3pt] (62,0) rectangle (186,122);
  \draw[TTCBorder,rounded corners=3pt,line width=.7pt] (62,0) rectangle (186,122);
  \fill[TTCLightBlue,rounded corners=3pt] (62,101) rectangle (186,122);
  \node[anchor=west,text=TTCBlue,font=\fontsize{10}{11.5}\selectfont\bfseries] at (68,113)
    {\faClipboardCheck\quad HỒ SƠ CHẤT LƯỢNG HẠNG MỤC};
  \node[anchor=east,text=TTCTextMuted,font=\fontsize{6}{7}\selectfont\bfseries] at (180,113)
    {MÃ GÓI VIỆC / HỒ SƠ TRUY XUẤT};

  \foreach \y/\n/\c in {78/01/TTCRed,55/02/TTCBlue,32/03/TTCCyan,9/04/TTCGold}{
    \fill[\c!6!white,rounded corners=1.5pt] (68,\y) rectangle (180,\y+18);
    \node[anchor=west,text=\c,font=\fontsize{7}{8}\selectfont\bfseries] at (72,\y+12) {\n};
    \fill[\c] (165,\y+5) circle (2.3);
    \node[text=white,font=\fontsize{5}{5.5}\selectfont\bfseries] at (165,\y+5) {\faCheck};
    \node[anchor=west,text=TTCTextMuted,font=\fontsize{6.1}{7.2}\selectfont\bfseries] at (170,\y+5) {ĐẠT};
  }
  \node[anchor=west,text=TTCBlue,font=\fontsize{7.4}{8.7}\selectfont\bfseries] at (81,90) {NGUỒN GỐC VẬT LIỆU};
  \node[anchor=west,text=TTCTextDark,font=\fontsize{6.3}{7.5}\selectfont] at (81,84) {CO/CQ • số lô • chứng chỉ xuất xưởng • kiểm tra đầu vào};
  \node[anchor=west,text=TTCBlue,font=\fontsize{7.4}{8.7}\selectfont\bfseries] at (81,67) {KIỂM SOÁT HÀN};
  \node[anchor=west,text=TTCTextDark,font=\fontsize{6.3}{7.5}\selectfont] at (81,61) {WPS/PQR • mã thợ hàn • AWS D1.1 • sơ đồ mối hàn};
  \node[anchor=west,text=TTCBlue,font=\fontsize{7.4}{8.7}\selectfont\bfseries] at (81,44) {BẰNG CHỨNG KIỂM TRA};
  \node[anchor=west,text=TTCTextDark,font=\fontsize{6.3}{7.5}\selectfont] at (81,38) {VT • UT • MT/PT • biên bản kiểm tra độc lập};
  \node[anchor=west,text=TTCBlue,font=\fontsize{7.4}{8.7}\selectfont\bfseries] at (81,21) {HỒ SƠ HOÀN CÔNG};
  \node[anchor=west,text=TTCTextDark,font=\fontsize{6.3}{7.5}\selectfont] at (81,15) {ITP đã ký • NCR đã đóng • bản vẽ hoàn công • lưu CDE};
\end{tikzpicture}

\vspace{3mm}

% NDT TOOLBOX
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,46);
  \fill[TTCLightBlue,rounded corners=3pt] (0,0) rectangle (186,46);
  \draw[TTCBorder,rounded corners=3pt,line width=.6pt] (0,0) rectangle (186,46);
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries] at (7,38)
    {\faCheckDouble\quad PHƯƠNG PHÁP KIỂM TRA NDT};
  \foreach \x in {46.5,93,139.5}{\draw[TTCBorder] (\x,6) -- (\x,31);}
  \node[align=center,text width=38mm] at (23.25,18) {
    {\fontsize{9}{10}\selectfont\bfseries\color{TTCRed} VT}\\[-.2mm]
    {\fontsize{6.1}{7.3}\selectfont Ngoại quan • kích thước • bề mặt}
  };
  \node[align=center,text width=38mm] at (69.75,18) {
    {\fontsize{9}{10}\selectfont\bfseries\color{TTCCyan} UT}\\[-.2mm]
    {\fontsize{6.3}{7.5}\selectfont Siêu âm kiểm tra mối hàn}
  };
  \node[align=center,text width=38mm] at (116.25,18) {
    {\fontsize{9}{10}\selectfont\bfseries\color{TTCBlue} MT / PT}\\[-.2mm]
    {\fontsize{6.3}{7.5}\selectfont Kiểm tra nứt bề mặt và mối góc}
  };
  \node[align=center,text width=38mm] at (162.75,18) {
    {\fontsize{9}{10}\selectfont\bfseries\color{TTCGold} LAS-XD}\\[-.2mm]
    {\fontsize{6.3}{7.5}\selectfont Kiểm chứng tại phòng thí nghiệm}
  };
\end{tikzpicture}

\vspace{3mm}

% RELEASE OUTCOME
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,30);
  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,30);
  \node[anchor=west,text=TTCCyan,font=\fontsize{7}{8}\selectfont\bfseries] at (8,20)
    {NGUYÊN TẮC PHÁT HÀNH};
  \node[anchor=west,text=white,font=\fontsize{10}{11.5}\selectfont\bfseries] at (8,11)
    {ĐÃ KIỂM TRA → ĐỦ BẰNG CHỨNG → ĐÃ DUYỆT → TRUY XUẤT ĐƯỢC};
  \node[anchor=east,text=TTCGold,font=\fontsize{12}{13}\selectfont\bfseries] at (178,15)
    {AWS D1.1 • ISO 9001};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_19 = r"""% ============================================================
% TRANG 19: HSE DECISION SYSTEM & STOP WORK AUTHORITY
% ============================================================
\pageheaderbar{AN TOÀN LAO ĐỘNG HSE \& STOP WORK AUTHORITY}{Trang 19}
\pagefooterbar{Trang 19}

\begin{tikzpicture}[remember picture, overlay]
  \fill[TTCRed!4!white]
    ([xshift=0mm,yshift=-210mm]current page.north west) --
    ([xshift=67mm,yshift=-248mm]current page.north west) --
    ([xshift=0mm,yshift=-278mm]current page.north west) -- cycle;
  \fill[TTCLightBlue]
    ([xshift=148mm,yshift=-31mm]current page.north west) --
    ([xshift=210mm,yshift=-31mm]current page.north west) --
    ([xshift=210mm,yshift=-108mm]current page.north west) -- cycle;
  \node[opacity=.035,text=TTCRed,font=\fontsize{66}{68}\selectfont\bfseries,
        rotate=90] at ([xshift=-11mm,yshift=-2mm]current page.east) {STOP};
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{An Toàn Là Một Hệ Quyết Định — Không Chỉ Là PPE}{Risk Elimination, Daily Control Cycle \& Stop Work Authority}

{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
NHÌN THẤY NGUY CƠ • KIỂM SOÁT TRƯỚC VIỆC • DỪNG KHI KHÔNG AN TOÀN\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
Tiến độ không bao giờ là lý do để chấp nhận một điều kiện làm việc chưa được kiểm soát.\par}
\vspace{3mm}

% MANIFESTO + RISK HIERARCHY + DAILY LOOP
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,149);

  % Left manifesto rail
  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (58,149);
  \begin{scope}
    \clip[rounded corners=3pt] (0,87) rectangle (58,149);
    \node[anchor=center,inner sep=0pt] at (29,118)
      {\includegraphics[height=62mm]{../../public/engineer-team-site.jpg}};
    \fill[TTCDeepNavy,opacity=.28] (0,87) rectangle (58,149);
  \end{scope}
  \node[anchor=west,text=TTCCyan,font=\fontsize{7}{8}\selectfont\bfseries] at (7,78)
    {STOP WORK AUTHORITY};
  \node[anchor=west,text=white,font=\fontsize{22}{23}\selectfont\bfseries] at (7,63)
    {STOP};
  \node[anchor=west,text=TTCRed!85!white,font=\fontsize{22}{23}\selectfont\bfseries] at (7,48)
    {WORK};
  \node[anchor=north west,text width=44mm,align=left] at (7,37) {
    {\fontsize{6.8}{8.3}\selectfont\color{white!85!gray}
    Bất kỳ ai cũng có quyền dừng công việc khi điều kiện an toàn chưa đầy đủ.}\\[2mm]
    {\fontsize{7}{8.5}\selectfont\bfseries\color{TTCGold}
    PEOPLE BEFORE PRODUCTION}
  };

  % Right — hierarchy of controls
  \fill[white,rounded corners=3pt] (63,86) rectangle (186,149);
  \draw[TTCBorder,rounded corners=3pt,line width=.6pt] (63,86) rectangle (186,149);
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries] at (69,141)
    {\faShield*\quad THỨ TỰ ƯU TIÊN KIỂM SOÁT RỦI RO};

  \fill[TTCRed] (69,124) rectangle (180,136);
  \fill[TTCBlue] (74,111) rectangle (175,123);
  \fill[TTCCyan] (79,98) rectangle (170,110);
  \fill[TTCGold] (84,85) rectangle (165,97);
  \node[anchor=west,text=white,font=\fontsize{7}{8}\selectfont\bfseries] at (73,130) {01 • ELIMINATE — Loại bỏ nguy cơ ngay từ biện pháp};
  \node[anchor=west,text=white,font=\fontsize{7}{8}\selectfont\bfseries] at (78,117) {02 • ENGINEER — Rào chắn, sàn thao tác, chống rơi};
  \node[anchor=west,text=white,font=\fontsize{7}{8}\selectfont\bfseries] at (83,104) {03 • PERMIT — JSA, giấy phép và người giám sát};
  \node[anchor=west,text=white,font=\fontsize{7}{8}\selectfont\bfseries] at (88,91) {04 • PPE — Lớp bảo vệ cuối cùng};

  % Right — daily safety cycle
  \fill[TTCLightBlue,rounded corners=3pt] (63,29) rectangle (186,81);
  \draw[TTCBorder,rounded corners=3pt,line width=.6pt] (63,29) rectangle (186,81);
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries] at (69,73)
    {\faClock\quad DAILY SAFETY CONTROL CYCLE};
  \draw[TTCBlue!35!white,line width=1pt] (76,50) -- (175,50);
  \foreach \x/\n/\t in {77/01/PLAN,102/02/TALK,127/03/VERIFY,152/04/WORK,175/05/CLOSE}{
    \fill[white] (\x,50) circle (4.5);
    \draw[TTCBlue,line width=.75pt] (\x,50) circle (4.5);
    \node[text=TTCRed,font=\fontsize{5.8}{6.5}\selectfont\bfseries] at (\x,50) {\n};
    \node[anchor=north,align=center,text width=22mm] at (\x,42)
      {{\fontsize{6}{7.2}\selectfont\bfseries\color{TTCBlue} \t}};
  }
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{6}{7.3}\selectfont] at (70,33)
    {JSA / Method → Toolbox Talk → PPE \& thiết bị → Giám sát → Đóng hành động};

  % Emergency row
  \fill[white,rounded corners=3pt] (63,0) rectangle (186,24);
  \draw[TTCBorder,rounded corners=3pt,line width=.6pt] (63,0) rectangle (186,24);
  \node[anchor=west,text=TTCRed,font=\fontsize{8}{9.5}\selectfont\bfseries] at (69,16)
    {\faFireExtinguisher\quad EMERGENCY READY};
  \node[anchor=west,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont] at (69,7)
    {Báo động • Cô lập • Sơ tán • Sơ cứu • Điều tra • Phòng ngừa tái diễn};
\end{tikzpicture}

\vspace{3mm}

% LIFE-SAVING RULES
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,48);
  \fill[white,rounded corners=3pt] (0,0) rectangle (186,48);
  \draw[TTCBorder,rounded corners=3pt,line width=.6pt] (0,0) rectangle (186,48);
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries] at (7,40)
    {\faHandPaper\quad 5 LIFE-SAVING RULES};
  \foreach \x in {37.2,74.4,111.6,148.8}{\draw[TTCBorder] (\x,6) -- (\x,31);}
  \node[align=center,text width=32mm] at (18.6,18) {
    {\fontsize{7.3}{8.5}\selectfont\bfseries\color{TTCRed} TRÊN CAO}\\[-.2mm]
    {\fontsize{5.8}{7}\selectfont 2 móc • lifeline • lưới hứng}
  };
  \node[align=center,text width=32mm] at (55.8,18) {
    {\fontsize{7.3}{8.5}\selectfont\bfseries\color{TTCBlue} NÂNG HẠ}\\[-.2mm]
    {\fontsize{5.8}{7}\selectfont Vùng cấm • tín hiệu • rigging}
  };
  \node[align=center,text width=32mm] at (93,18) {
    {\fontsize{7.3}{8.5}\selectfont\bfseries\color{TTCCyan} ĐIỆN}\\[-.2mm]
    {\fontsize{5.8}{7}\selectfont ELCB • tiếp địa • lock-out}
  };
  \node[align=center,text width=32mm] at (130.2,18) {
    {\fontsize{7.3}{8.5}\selectfont\bfseries\color{TTCGold} HÀN CẮT}\\[-.2mm]
    {\fontsize{5.8}{7}\selectfont Fire watch • chắn xỉ • permit}
  };
  \node[align=center,text width=32mm] at (167.4,18) {
    {\fontsize{7.3}{8.5}\selectfont\bfseries\color{TTCBlue} HỐ ĐÀO}\\[-.2mm]
    {\fontsize{5.8}{7}\selectfont Rào chắn • chống sạt • lối thoát}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

print("Section 4 code rewritten cleanly.")
