# -*- coding: utf-8 -*-
"""
Section 5: Project Portfolio, Case Studies, Supply Chain & Client Testimonials (Pages 20 - 30)
"""

PAGE_20_LEGACY = r"""% ============================================================
% TRANG 20: DANH MỤC ĐẠI DỰ ÁN CÔNG NGHIỆP TIÊU BIỂU THEO NGÀNH (BẢNG 1)
% ============================================================
\pageheaderbar{DANH MỤC ĐẠI DỰ ÁN TIÊU BIỂU (BẢNG 1)}{Trang 20}
\pagefooterbar{Trang 20}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.03, scale=2.8, font=\bfseries\sffamily, text=TTCBlue] at ([yshift=-10mm]current page.center) {SELECTED INDUSTRIAL MEGA PROJECTS};
  \draw[TTCBlue!6!white, line width=0.5pt] ([xshift=15mm, yshift=20mm]current page.south west) grid[step=8mm] ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Danh Mục 150+ Đại Dự Án Công Nghiệp Trọng Điểm (Bảng 1)}{Selected Flagship Industrial EPC Projects Across Diverse Manufacturing Sectors}

% TẦNG 1: BẢNG 8 ĐẠI DỰ ÁN TRỌNG ĐIỂM
\noindent
\begin{tikzpicture}
  \node[
    rounded corners=6pt,
    fill=white,
    draw=TTCBlue!40!white,
    line width=0.9pt,
    minimum width=186mm,
    inner sep=5pt,
    text width=176mm
  ] {
    \renewcommand{\arraystretch}{1.08}
    {\fontsize{6.8}{8.5}\selectfont
    \begin{tabularx}{\linewidth}{@{}c|p{36mm}|p{34mm}|c|p{26mm}|X@{}}
      \toprule
      \textbf{STT} & \textbf{Tên Dự Án / Nhà Máy} & \textbf{Chủ Đầu Tư / Quốc Gia} & \textbf{Quy Mô} & \textbf{Địa Điểm} & \textbf{Vai Trò Của TTC} \\
      \midrule
      \textbf{01} & \textbf{Tổ hợp NM Gạch Hồng Trang} & Cty Gạch Hồng Trang (VN) & \textbf{100.000 m$^2$} & Lập Thạch, Vĩnh Phúc & Tổng thầu EPC (Fast-track 6.5 tháng, nhịp 42m) \\
      \textbf{02} & \textbf{Nhà máy May Sông Hồng 7} & Tập đoàn May Sông Hồng (VN) & \textbf{68.000 m$^2$} & Hải Hậu, Nam Định & Tổng thầu Thiết kế \& Thi công Sàn 2 tầng tải nặng \\
      \textbf{03} & \textbf{Tổ hợp NM Japfa Comfeed} & Tập đoàn Japfa (Indonesia) & \textbf{50.000 m$^2$} & Vĩnh Phúc / Thái Bình & Tổng thầu Kết cấu Silo cao 45m \& Xưởng CNC \\
      \textbf{04} & \textbf{NM Thức Ăn Chăn Nuôi CP} & Tập đoàn C.P (Thái Lan) & \textbf{35.000 m$^2$} & KCN Đồng Văn, Hà Nam & Xưởng sản xuất thức ăn \& Kho bảo quản \\
      \textbf{05} & \textbf{Nhà máy Daeyun ST Vina} & Daeyun Group (Hàn Quốc) & \textbf{20.000 m$^2$} & KCN Bá Thiện 2, Vĩnh Phúc & Xưởng sạch Class 10.000 \& Sàn Vinyl kháng tĩnh điện \\
      \textbf{06} & \textbf{Nhà máy Dây Cáp Sumidenso} & Sumitomo Electric (Nhật Bản) & \textbf{15.015 m$^2$} & KCN Sông Hậu, Hậu Giang & Nhà máy sản xuất dây cáp ô tô \& Hệ thống PCCC \\
      \textbf{07} & \textbf{Xưởng Sản Xuất Foxconn} & Tập đoàn Foxconn (Đài Loan) & \textbf{12.000 m$^2$} & KCN Quế Võ, Bắc Ninh & Kết cấu thép vượt nhịp \& Lắp dựng nhà xưởng cao \\
      \textbf{08} & \textbf{Tổ hợp Logistics BW Industrial} & BW Industrial (Singapore) & \textbf{45.000 m$^2$} & KCN Yên Phong, Bắc Ninh & Tổng thầu EPC Kho thông minh, Sàn Laser Screed \\
      \bottomrule
    \end{tabularx}}
  };
\end{tikzpicture}

\vspace{2mm}

% TẦNG 2: 3 PHÂN KHÚC NGÀNH NGHỀ TRỌNG TÂM
\noindent
\begin{tabular}{@{}p{59mm}@{\hspace{3.5mm}}p{59mm}@{\hspace{3.5mm}}p{59mm}@{}}
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=59mm, minimum height=48mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCRed} \faTshirt\ Dệt May \& Da Giày}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ Nhà xưởng cao tầng chịu rung động máy may.\newline
      \textbullet\ Hệ thống điều hòa thông gió làm mát áp suất âm.\newline
      \textbullet\ Kết cấu mái sẵn sàng điện mặt trời 2--3MWp.\newline
      \textbullet\ Đạt chuẩn kiểm toán trách nhiệm xã hội WRAP/SEDEX.}
    };
  \end{tikzpicture} &
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=59mm, minimum height=48mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCCyan} \faApple\ Điện Tử \& Phòng Sạch}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ Phòng sạch Cleanroom ISO Class 1.000 -- 100.000.\newline
      \textbullet\ Sàn Vinyl/Epoxy tự san phẳng kháng tĩnh điện ESD.\newline
      \textbullet\ Kiểm soát chính xác nhiệt độ $\pm 1^\circ$C và độ ẩm $\pm 5\%$.\newline
      \textbullet\ Hệ thống khí nén, nước RO và PCCC khí sạch FM200.}
    };
  \end{tikzpicture} &
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=59mm, minimum height=48mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCBlue} \faWarehouse\ Logistics \& Kho Lạnh}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ Sàn siêu phẳng tiêu chuẩn quốc tế DIN 18202 / TR34.\newline
      \textbullet\ Cụm sàn nâng tự động Dock Leveler \& cửa trượt cuốn nhanh.\newline
      \textbullet\ Kết cấu xà gồ Z nhịp lớn tối ưu diện tích lưu kho.\newline
      \textbullet\ Hệ thống giá kệ tự động cao tầng AS/RS.}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{2mm}

% TẦNG 3: BĂNG KPI DỰ ÁN
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
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCRed} 150+ DỰ ÁN} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCCyan} >500.000 m$^2$} &
      {\fontsize{14}{16}\selectfont\bfseries\color{white} 65\% FDI} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCGold} 100\% ĐÚNG HẠN} \\
      {\fontsize{7.2}{9}\selectfont Tổng Công Trình Đã Bàn Giao} &
      {\fontsize{7.2}{9}\selectfont Tổng Diện Tích Sàn} &
      {\fontsize{7.2}{9}\selectfont Tỷ Trọng Vốn Quốc Tế} &
      {\fontsize{7.2}{9}\selectfont Cam Kết Tiến Độ Hợp Đồng}
    \end{tabularx}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_21_LEGACY = r"""% ============================================================
% TRANG 21: DANH MỤC DỰ ÁN FDI \& CÔNG NGHIỆP PHỤ TRỢ (BẢNG 2) [TRANG MỚI]
% ============================================================
\pageheaderbar{DANH MỤC ĐẠI DỰ ÁN TIÊU BIỂU (BẢNG 2)}{Trang 21}
\pagefooterbar{Trang 21}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.03, scale=2.8, font=\bfseries\sffamily, text=TTCBlue] at ([yshift=-10mm]current page.center) {FDI \& SPECIALIZED INDUSTRIAL PROJECTS};
  \draw[TTCBlue!6!white, line width=0.5pt] ([xshift=15mm, yshift=20mm]current page.south west) grid[step=8mm] ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Danh Mục Dự Án FDI \& Công Nghiệp Phụ Trợ (Bảng 2)}{Specialized Manufacturing Facilities, Food Processing, Automotive Supply \& Cold Storage}

% TẦNG 1: BẢNG 8 DỰ ÁN FDI \& PHỤ TRỢ
\noindent
\begin{tikzpicture}
  \node[
    rounded corners=6pt,
    fill=white,
    draw=TTCBlue!40!white,
    line width=0.9pt,
    minimum width=186mm,
    inner sep=5pt,
    text width=176mm
  ] {
    \renewcommand{\arraystretch}{1.08}
    {\fontsize{6.8}{8.5}\selectfont
    \begin{tabularx}{\linewidth}{@{}c|p{36mm}|p{34mm}|c|p{26mm}|X@{}}
      \toprule
      \textbf{STT} & \textbf{Tên Dự Án / Nhà Máy} & \textbf{Chủ Đầu Tư / Quốc Gia} & \textbf{Quy Mô} & \textbf{Địa Điểm} & \textbf{Vai Trò Của TTC} \\
      \midrule
      \textbf{09} & \textbf{NM Chăn Nuôi New Hope} & Tập đoàn New Hope (Singapore) & \textbf{32.000 m$^2$} & KCN Quang Châu, Bắc Giang \& Tổng thầu Silo ngũ cốc \& Trạm điện biến áp \\
      \textbf{10} & \textbf{NM Cơ Khí Shinjo Vina} & Shinjo Corp (Nhật Bản) & \textbf{18.500 m$^2$} & KCN VSIP Bắc Ninh \& Xưởng cơ khí chính xác, Dầm cầu trục 15T \\
      \textbf{11} & \textbf{NM Điện Tử Towada} & Towada Electronic (Nhật Bản) & \textbf{16.000 m$^2$} & KCN Phúc Điền, Hải Dương \& Xưởng lắp ráp vi mạch \& Phòng sạch ISO \\
      \textbf{12} & \textbf{NM Bao Bì Toyo Seikan} & Toyo Seikan (Nhật Bản) & \textbf{22.000 m$^2$} & KCN Tiên Sơn, Bắc Ninh \& Tổng thầu EPC Xưởng bao bì \& Sàn phẳng \\
      \textbf{13} & \textbf{Xưởng May Fami Vina} & Fami Garment (Hàn Quốc) & \textbf{28.000 m$^2$} & KCN Thụy Vân, Phú Thọ \& Nhà xưởng may 2 tầng \& Hệ thống HVAC \\
      \textbf{14} & \textbf{Kho Logistics Yusen} & Yusen Logistics (Nhật Bản) & \textbf{25.000 m$^2$} & KCN Đình Vũ, Hải Phòng \& Tổng thầu Kho ngoại quan, Cụm Dock Leveler \\
      \textbf{15} & \textbf{NM Thực Phẩm A-One} & Saigon Ve Wong (Đài Loan) & \textbf{30.000 m$^2$} & KCN Sóng Thần 2, Bình Dương \& Xưởng chế biến thực phẩm chuẩn HACCP \\
      \textbf{16} & \textbf{NM Năng Lượng Sơn Hà} & Tập đoàn Sơn Hà (VN) & \textbf{24.000 m$^2$} & KCN Thuận Thành, Bắc Ninh \& Tổng thầu Xưởng sản xuất bồn \& Pin mặt trời \\
      \bottomrule
    \end{tabularx}}
  };
\end{tikzpicture}

\vspace{2mm}

% TẦNG 2: 3 PHÂN KHÚC CHUYÊN SÂU
\noindent
\begin{tabular}{@{}p{59mm}@{\hspace{3.5mm}}p{59mm}@{\hspace{3.5mm}}p{59mm}@{}}
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=59mm, minimum height=48mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCRed} \faUtensils\ Thực Phẩm \& Thức Ăn CN}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ Kết cấu tháp Silo cao $>40$m chịu tải trọng động.\newline
      \textbullet\ Hệ thống thông gió chống nổ bụi ngũ cốc ATEX.\newline
      \textbullet\ Sơn Epoxy kháng hóa chất và vi sinh chuẩn HACCP.\newline
      \textbullet\ Hệ thống xử lý nước thải sinh học công suất lớn.}
    };
  \end{tikzpicture} &
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=59mm, minimum height=48mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCCyan} \faCar\ Ô Tô \& Cơ Khí Phụ Trợ}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ Dầm cầu trục tải nặng 10T--30T vận hành êm ái.\newline
      \textbullet\ Móng máy gia công CNC cách ly rung động chuyên dụng.\newline
      \textbullet\ Hệ thống cấp khí nén trung tâm \& rãnh kỹ thuật ngầm.\newline
      \textbullet\ Lưới cột lớn $>24$m thuận tiện bố trí dây chuyền.}
    };
  \end{tikzpicture} &
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=59mm, minimum height=48mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCBlue} \faSolarPanel\ Năng Lượng \& Vật Liệu Mới}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ Xưởng sản xuất thiết bị năng lượng sạch quy mô lớn.\newline
      \textbullet\ Mái tôn Seamlock tích hợp hệ thống pin năng lượng mặt trời.\newline
      \textbullet\ Hệ thống chiếu sáng LED tiết kiệm điện \& cảm biến tự động.\newline
      \textbullet\ Cảnh quan cây xanh sinh thái tiêu chuẩn khu công nghiệp xanh.}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{2mm}

% TẦNG 3: BĂNG KPI DỰ ÁN 2
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
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCRed} 8 QUỐC GIA} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCCyan} 100\% FAST-TRACK} &
      {\fontsize{14}{16}\selectfont\bfseries\color{white} 0 KHIẾU NẠI} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCGold} 98.8\%} \\
      {\fontsize{7.2}{9}\selectfont Khách Hàng Quốc Tế FDI} &
      {\fontsize{7.2}{9}\selectfont Tiến Độ Thi Công Thần Tốc} &
      {\fontsize{7.2}{9}\selectfont Tranh Chấp Hợp Đồng} &
      {\fontsize{7.2}{9}\selectfont Tỷ Lệ Khách Hàng Hài Lòng}
    \end{tabularx}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_20_VISUAL = r"""% ============================================================
% TRANG 20: TOÀN CẢNH DANH MỤC DỰ ÁN — DATA-LED PORTFOLIO
% ============================================================
\AddToHookNext{shipout/foreground}{%
  \pageheaderbar{TOÀN CẢNH DANH MỤC DỰ ÁN}{Trang 20}%
  \pagefooterbar{Trang 20}%
}
\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Dấu Chân Dự Án Công Nghiệp}{Danh mục chọn lọc • Quy mô kiểm chứng được • Năng lực theo ngành}

{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
MỘT DANH MỤC • NHIỀU BÀI TOÁN CÔNG NGHIỆP\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
Từ nhà máy sản xuất, phòng sạch đến logistics và năng lượng — mỗi dự án phản ánh một năng lực triển khai khác nhau.\par}
\vspace{3mm}

% BA CHỈ SỐ ĐƯỢC TÍNH TRỰC TIẾP TỪ DANH MỤC 16 DỰ ÁN
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,24);
  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,24);
  \foreach \x in {62,124}{\draw[white!35!gray,line width=.6pt] (\x,4) -- (\x,20);}
  \node[align=center,text width=54mm] at (31,12) {
    {\fontsize{14}{15}\selectfont\bfseries\color{TTCRed} 16 DỰ ÁN}\\[-.4mm]
    {\fontsize{6.5}{7.5}\selectfont\color{white!82!gray}Danh mục đại diện được chọn lọc}
  };
  \node[align=center,text width=54mm] at (93,12) {
    {\fontsize{14}{15}\selectfont\bfseries\color{TTCCyan} >540.000 m$^2$}\\[-.4mm]
    {\fontsize{6.5}{7.5}\selectfont\color{white!82!gray}Tổng diện tích từ danh mục}
  };
  \node[align=center,text width=54mm] at (155,12) {
    {\fontsize{14}{15}\selectfont\bfseries\color{TTCGold} 6 NHÓM NGÀNH}\\[-.4mm]
    {\fontsize{6.5}{7.5}\selectfont\color{white!82!gray}Nhiều yêu cầu kỹ thuật đặc thù}
  };
\end{tikzpicture}

\vspace{3mm}

% ẢNH ĐIỂM NEO + SÁU NHÓM NGÀNH
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,100);

  % Cột ảnh: ảnh, chú thích và phạm vi được tách riêng
  \fill[white,rounded corners=3pt] (0,0) rectangle (70,100);
  \draw[TTCBorder,rounded corners=3pt,line width=.7pt] (0,0) rectangle (70,100);
  \begin{scope}
    \clip[rounded corners=3pt] (0,42) rectangle (70,100);
    \node[anchor=center,inner sep=0pt] at (35,71)
      {\includegraphics[height=58mm]{../../public/project-assets/foxcon.png}};
  \end{scope}
  \fill[white] (0,24) rectangle (70,41);
  \node[anchor=west,text=TTCRed,font=\fontsize{6.2}{7.2}\selectfont\bfseries] at (5,36)
    {DỰ ÁN TIÊU BIỂU};
  \node[anchor=west,text=TTCBlue,font=\fontsize{9}{10.5}\selectfont\bfseries] at (5,29)
    {FOXCONN — BẮC NINH};
  \fill[TTCLightBlue] (0,0) rectangle (70,23);
  \node[anchor=north west,text width=59mm] at (5,18) {
    {\fontsize{7.2}{8.5}\selectfont\bfseries\color{TTCBlue} 12.000 m$^2$}\\[.8mm]
    {\fontsize{6.4}{7.7}\selectfont\color{TTCTextDark}Kết cấu thép vượt nhịp • Lắp dựng nhà xưởng cao}
  };

  % Ma trận nhóm ngành — không dùng các hộp nội dung dài
  \fill[white,rounded corners=3pt] (75,0) rectangle (186,100);
  \draw[TTCBorder,rounded corners=3pt,line width=.7pt] (75,0) rectangle (186,100);
  \node[anchor=west,text=TTCBlue,font=\fontsize{8.5}{10}\selectfont\bfseries] at (81,93)
    {6 NHÓM NGÀNH TRỌNG TÂM};
  \node[anchor=east,text=TTCTextMuted,font=\fontsize{5.8}{7}\selectfont] at (180,93)
    {DỰ ÁN ĐẠI DIỆN};
  \draw[TTCBorder] (130.5,8) -- (130.5,86);
  \foreach \y in {34,60}{\draw[TTCBorder] (81,\y) -- (180,\y);}

  \fill[TTCRed] (81,63) rectangle (82.5,84);
  \node[anchor=north west,text width=43mm] at (86,82) {
    {\fontsize{7.4}{8.7}\selectfont\bfseries\color{TTCRed} DỆT MAY}\\[.5mm]
    {\fontsize{6.1}{7.3}\selectfont\color{TTCTextDark}Sông Hồng 7 • Fami Vina}
  };
  \fill[TTCCyan] (136,63) rectangle (137.5,84);
  \node[anchor=north west,text width=41mm] at (141,82) {
    {\fontsize{7.4}{8.7}\selectfont\bfseries\color{TTCCyan} ĐIỆN TỬ}\\[.5mm]
    {\fontsize{6.1}{7.3}\selectfont\color{TTCTextDark}Foxconn • Towada • Daeyun}
  };

  \fill[TTCGold] (81,37) rectangle (82.5,58);
  \node[anchor=north west,text width=43mm] at (86,56) {
    {\fontsize{7.4}{8.7}\selectfont\bfseries\color{TTCGold} THỰC PHẨM}\\[.5mm]
    {\fontsize{6.1}{7.3}\selectfont\color{TTCTextDark}Japfa • CP • New Hope • A-One}
  };
  \fill[TTCBlue] (136,37) rectangle (137.5,58);
  \node[anchor=north west,text width=41mm] at (141,56) {
    {\fontsize{7.4}{8.7}\selectfont\bfseries\color{TTCBlue} LOGISTICS}\\[.5mm]
    {\fontsize{6.1}{7.3}\selectfont\color{TTCTextDark}BW Industrial • Yusen}
  };

  \fill[TTCCyan!75!TTCBlue] (81,11) rectangle (82.5,32);
  \node[anchor=north west,text width=43mm] at (86,30) {
    {\fontsize{7.4}{8.7}\selectfont\bfseries\color{TTCBlue} CƠ KHÍ • Ô TÔ}\\[.5mm]
    {\fontsize{6.1}{7.3}\selectfont\color{TTCTextDark}Shinjo • Sumidenso}
  };
  \fill[TTCGold!80!TTCRed] (136,11) rectangle (137.5,32);
  \node[anchor=north west,text width=41mm] at (141,30) {
    {\fontsize{7.4}{8.7}\selectfont\bfseries\color{TTCGold} VẬT LIỆU • NL}\\[.5mm]
    {\fontsize{6.1}{7.3}\selectfont\color{TTCTextDark}Hồng Trang • Toyo • Sơn Hà}
  };
\end{tikzpicture}

\vspace{3mm}

% PHỔ QUY MÔ — THAY CHO BẢNG SÁU CỘT
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,76);
  \fill[TTCLightBlue,rounded corners=3pt] (0,0) rectangle (186,76);
  \draw[TTCBorder,rounded corners=3pt,line width=.7pt] (0,0) rectangle (186,76);
  \node[anchor=west,text=TTCBlue,font=\fontsize{8.5}{10}\selectfont\bfseries] at (7,68)
    {PHỔ QUY MÔ 8 DỰ ÁN LỚN NHẤT};
  \node[anchor=east,text=TTCTextMuted,font=\fontsize{6}{7}\selectfont] at (179,68)
    {Đơn vị: m$^2$};
  \draw[TTCBorder] (93,7) -- (93,60);

  % Cột trái
  \foreach \y/\name/\w/\value/\c in {
    53/Hồng Trang/45/100.000/TTCRed,
    41/Sông Hồng 7/31/68.000/TTCBlue,
    29/Japfa/23/50.000/TTCCyan,
    17/BW Logistics/20/45.000/TTCGold}{
    \node[anchor=east,text=TTCTextDark,font=\fontsize{6.2}{7.2}\selectfont\bfseries] at (29,\y) {\name};
    \fill[white] (32,\y-2) rectangle (79,\y+2);
    \fill[\c] (32,\y-2) rectangle +(\w,4);
    \node[anchor=west,text=TTCTextMuted,font=\fontsize{5.9}{7}\selectfont] at (81,\y) {\value};
  }

  % Cột phải
  \foreach \y/\name/\w/\value/\c in {
    53/CP/17/35.000/TTCGold,
    41/New Hope/15/32.000/TTCRed,
    29/A-One/14/30.000/TTCCyan,
    17/Fami Vina/13/28.000/TTCBlue}{
    \node[anchor=east,text=TTCTextDark,font=\fontsize{6.2}{7.2}\selectfont\bfseries] at (121,\y) {\name};
    \fill[white] (124,\y-2) rectangle (170,\y+2);
    \fill[\c] (124,\y-2) rectangle +(\w,4);
    \node[anchor=west,text=TTCTextMuted,font=\fontsize{5.9}{7}\selectfont] at (172,\y) {\value};
  }
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_21_VISUAL = r"""% ============================================================
% TRANG 21: BỨC TƯỜNG BẰNG CHỨNG DỰ ÁN
% ============================================================
\AddToHookNext{shipout/foreground}{%
  \pageheaderbar{CÔNG TRÌNH ĐẠI DIỆN}{Trang 21}%
  \pagefooterbar{Trang 21}%
}
\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Bằng Chứng Từ Công Trình Đã Triển Khai}{Hình ảnh dự án • Quy mô • Phạm vi công việc của TTC}

{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
MỖI DỰ ÁN • MỘT BÀI TOÁN • MỘT GIẢI PHÁP\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
Tám công trình đại diện cho khả năng thích ứng với nhiều ngành sản xuất, yêu cầu kỹ thuật và điều kiện triển khai khác nhau.\par}
\vspace{3mm}

% PROJECT EVIDENCE WALL — CHÚ THÍCH LUÔN NẰM NGOÀI ẢNH
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,158);

  % Hai dự án điểm neo
  \fill[white,rounded corners=3pt] (0,86) rectangle (91,158);
  \draw[TTCBorder,rounded corners=3pt,line width=.7pt] (0,86) rectangle (91,158);
  \begin{scope}
    \clip[rounded corners=3pt] (0,106) rectangle (91,158);
    \node[anchor=center,inner sep=0pt] at (45.5,132)
      {\includegraphics[width=91mm]{../../public/project-assets/songhong7.jpg}};
  \end{scope}
  \node[anchor=west,text=TTCBlue,font=\fontsize{8.5}{10}\selectfont\bfseries] at (5,99)
    {MAY SÔNG HỒNG 7};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{6.2}{7.4}\selectfont] at (5,91)
    {68.000 m$^2$ • Nam Định • Nhà xưởng hai tầng};

  \fill[white,rounded corners=3pt] (95,86) rectangle (186,158);
  \draw[TTCBorder,rounded corners=3pt,line width=.7pt] (95,86) rectangle (186,158);
  \begin{scope}
    \clip[rounded corners=3pt] (95,106) rectangle (186,158);
    \node[anchor=center,inner sep=0pt] at (140.5,132)
      {\includegraphics[width=92mm]{../../public/project-assets/foxcon.png}};
  \end{scope}
  \node[anchor=west,text=TTCBlue,font=\fontsize{8.5}{10}\selectfont\bfseries] at (100,99)
    {FOXCONN};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{6.2}{7.4}\selectfont] at (100,91)
    {12.000 m$^2$ • Bắc Ninh • Kết cấu vượt nhịp};

  % Sáu dự án bổ trợ — hàng trên
  \fill[white,rounded corners=2pt] (0,43) rectangle (59,82);
  \draw[TTCBorder,rounded corners=2pt] (0,43) rectangle (59,82);
  \begin{scope}\clip[rounded corners=2pt] (0,57) rectangle (59,82);
    \node[anchor=center,inner sep=0pt] at (29.5,69.5)
      {\includegraphics[width=59mm]{../../public/project-assets/japfa.jpg}};
  \end{scope}
  \node[anchor=west,text=TTCBlue,font=\fontsize{6.8}{8}\selectfont\bfseries] at (4,52) {JAPFA COMFEED};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{5.5}{6.5}\selectfont] at (4,47) {50.000 m$^2$ • Thức ăn chăn nuôi};

  \fill[white,rounded corners=2pt] (63.5,43) rectangle (122.5,82);
  \draw[TTCBorder,rounded corners=2pt] (63.5,43) rectangle (122.5,82);
  \begin{scope}\clip[rounded corners=2pt] (63.5,57) rectangle (122.5,82);
    \node[anchor=center,inner sep=0pt] at (93,69.5)
      {\includegraphics[width=59mm]{../../public/project-assets/daeyun.jpg}};
  \end{scope}
  \node[anchor=west,text=TTCBlue,font=\fontsize{6.8}{8}\selectfont\bfseries] at (67.5,52) {DAEYUN ST VINA};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{5.5}{6.5}\selectfont] at (67.5,47) {20.000 m$^2$ • Xưởng sạch};

  \fill[white,rounded corners=2pt] (127,43) rectangle (186,82);
  \draw[TTCBorder,rounded corners=2pt] (127,43) rectangle (186,82);
  \begin{scope}\clip[rounded corners=2pt] (127,57) rectangle (186,82);
    \node[anchor=center,inner sep=0pt] at (156.5,69.5)
      {\includegraphics[width=59mm]{../../public/project-assets/yusen.jpg}};
  \end{scope}
  \node[anchor=west,text=TTCBlue,font=\fontsize{6.8}{8}\selectfont\bfseries] at (131,52) {YUSEN LOGISTICS};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{5.5}{6.5}\selectfont] at (131,47) {25.000 m$^2$ • Kho ngoại quan};

  % Sáu dự án bổ trợ — hàng dưới
  \fill[white,rounded corners=2pt] (0,0) rectangle (59,39);
  \draw[TTCBorder,rounded corners=2pt] (0,0) rectangle (59,39);
  \begin{scope}\clip[rounded corners=2pt] (0,14) rectangle (59,39);
    \node[anchor=center,inner sep=0pt] at (29.5,26.5)
      {\includegraphics[width=59mm]{../../public/project-assets/towada.jpg}};
  \end{scope}
  \node[anchor=west,text=TTCBlue,font=\fontsize{6.8}{8}\selectfont\bfseries] at (4,9) {TOWADA ELECTRONIC};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{5.5}{6.5}\selectfont] at (4,4) {16.000 m$^2$ • Lắp ráp điện tử};

  \fill[white,rounded corners=2pt] (63.5,0) rectangle (122.5,39);
  \draw[TTCBorder,rounded corners=2pt] (63.5,0) rectangle (122.5,39);
  \begin{scope}\clip[rounded corners=2pt] (63.5,14) rectangle (122.5,39);
    \node[anchor=center,inner sep=0pt] at (93,26.5)
      {\includegraphics[width=59mm]{../../public/project-assets/newhope.jpg}};
  \end{scope}
  \node[anchor=west,text=TTCBlue,font=\fontsize{6.8}{8}\selectfont\bfseries] at (67.5,9) {NEW HOPE};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{5.5}{6.5}\selectfont] at (67.5,4) {32.000 m$^2$ • Silo và trạm điện};

  \fill[white,rounded corners=2pt] (127,0) rectangle (186,39);
  \draw[TTCBorder,rounded corners=2pt] (127,0) rectangle (186,39);
  \begin{scope}\clip[rounded corners=2pt] (127,14) rectangle (186,39);
    \node[anchor=center,inner sep=0pt] at (156.5,26.5)
      {\includegraphics[width=59mm]{../../public/project-assets/sumidenso.jpg}};
  \end{scope}
  \node[anchor=west,text=TTCBlue,font=\fontsize{6.8}{8}\selectfont\bfseries] at (131,9) {SUMIDENSO};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{5.5}{6.5}\selectfont] at (131,4) {15.015 m$^2$ • Dây cáp ô tô};
\end{tikzpicture}

\vspace{3mm}

% KHỐI KẾT LUẬN — BỐN BÀI TOÁN KHÁCH HÀNG NHỚ ĐƯỢC
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,52);
  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,52);
  \node[anchor=west,text=TTCCyan,font=\fontsize{8}{9.5}\selectfont\bfseries] at (7,44)
    {4 BÀI TOÁN TTC GIẢI QUYẾT};
  \foreach \x in {46.5,93,139.5}{\draw[white!28!gray] (\x,7) -- (\x,36);}

  \node[anchor=north,align=center,text width=38mm] at (23.25,32) {
    {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCRed} VƯỢT NHỊP}\\[1mm]
    {\fontsize{6.2}{7.5}\selectfont\color{white!82!gray}Không gian sản xuất lớn, giảm cột giữa nhà}
  };
  \node[anchor=north,align=center,text width=38mm] at (69.75,32) {
    {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCCyan} SÀN TẢI NẶNG}\\[1mm]
    {\fontsize{6.2}{7.5}\selectfont\color{white!82!gray}Đáp ứng máy móc, kho vận và chống rung}
  };
  \node[anchor=north,align=center,text width=38mm] at (116.25,32) {
    {\fontsize{8}{9.5}\selectfont\bfseries\color{white} MÔI TRƯỜNG KIỂM SOÁT}\\[1mm]
    {\fontsize{6.2}{7.5}\selectfont\color{white!82!gray}Phòng sạch, HVAC và chống tĩnh điện}
  };
  \node[anchor=north,align=center,text width=38mm] at (162.75,32) {
    {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCGold} TIẾN ĐỘ GẤP}\\[1mm]
    {\fontsize{6.2}{7.5}\selectfont\color{white!82!gray}Thiết kế, mua sắm và thi công đồng bộ}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_20 = r"""% ============================================================
% TRANG 20: SỔ DANH MỤC DỰ ÁN TIÊU BIỂU 01--08
% ============================================================
\AddToShipoutPictureFG*{%
  \AtPageUpperLeft{%
    \begin{tikzpicture}[x=1mm,y=1mm]
      \path[use as bounding box] (0,0) rectangle (0,0);
      \fill[TTCDeepNavy] (0,0) rectangle (210,-10);
      \fill[TTCRed] (0,-10) rectangle (210,-11);
      \node[anchor=west,text=white,font=\fontsize{7.5}{9}\selectfont\bfseries] at (12,-5)
        {\faBuilding\quad CÔNG TY CỔ PHẦN CÔNG NGHỆ XÂY DỰNG TÂN THÀNH CÔNG \textbullet\ TTC JSC};
      \node[anchor=east,text=TTCCyan,font=\fontsize{7.5}{9}\selectfont\bfseries] at (198,-5)
        {DANH MỤC DỰ ÁN TIÊU BIỂU • 01--08};
    \end{tikzpicture}%
  }%
  \AtPageLowerLeft{%
    \begin{tikzpicture}[x=1mm,y=1mm]
      \path[use as bounding box] (0,0) rectangle (0,0);
      \fill[TTCDeepNavy] (0,0) rectangle (210,8);
      \fill[TTCCyan] (0,8) rectangle (210,8.8);
      \node[anchor=west,text=white,font=\fontsize{6.8}{8}\selectfont] at (12,4)
        {\faPhone*\ +84 976 447 766 \quad\textbullet\quad \faEnvelope\ info@tanthanhcongjsc.com \quad\textbullet\quad \faGlobe\ https://tanthanhcongjsc.com};
      \node[anchor=east,text=white,font=\fontsize{7}{8}\selectfont\bfseries] at (198,4)
        {Trang 20};
    \end{tikzpicture}%
  }%
}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Danh Mục Dự Án Công Nghiệp Tiêu Biểu}{Tám công trình đại diện • Thông tin cô đọng • Dễ đối chiếu}

{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
QUY MÔ • ĐỊA ĐIỂM • PHẠM VI CÔNG VIỆC\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
Danh sách được trình bày theo một cấu trúc thống nhất để người đọc nhận biết nhanh vai trò của TTC tại từng dự án.\par}
\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,188);
  \fill[white,rounded corners=3pt] (0,0) rectangle (186,188);
  \draw[TTCBorder,rounded corners=3pt,line width=.7pt] (0,0) rectangle (186,188);

  % Tiêu đề cột
  \fill[TTCDeepNavy,rounded corners=3pt] (0,176) rectangle (186,188);
  \node[text=white,font=\fontsize{6.5}{7.5}\selectfont\bfseries] at (5,182) {STT};
  \node[anchor=west,text=white,font=\fontsize{6.5}{7.5}\selectfont\bfseries] at (14,182) {DỰ ÁN / CHỦ ĐẦU TƯ};
  \node[text=white,font=\fontsize{6.5}{7.5}\selectfont\bfseries] at (84,182) {QUY MÔ};
  \node[anchor=west,text=white,font=\fontsize{6.5}{7.5}\selectfont\bfseries] at (96,182) {ĐỊA ĐIỂM};
  \node[anchor=west,text=white,font=\fontsize{6.5}{7.5}\selectfont\bfseries] at (129,182) {PHẠM VI CÔNG VIỆC};

  \newcommand{\projectrowa}[8]{%
    \fill[#8] (0,{#1-11}) rectangle (186,{#1+11});
    \fill[TTCBlue] (0,{#1-11}) rectangle (10,{#1+11});
    \node[text=white,font=\fontsize{7}{8}\selectfont\bfseries] at (5,#1) {#2};
    \node[anchor=west,text width=53mm,align=left] at (14,#1) {
      {\fontsize{7.2}{8.4}\selectfont\bfseries\color{TTCBlue} #3}\\[-.2mm]
      {\fontsize{5.8}{7}\selectfont\color{TTCTextMuted} #4}
    };
    \node[align=center,text width=20mm] at (84,#1)
      {{\fontsize{7}{8.2}\selectfont\bfseries\color{TTCTextDark} #5}};
    \node[anchor=west,text width=29mm,align=left] at (96,#1)
      {{\fontsize{5.9}{7.1}\selectfont\color{TTCTextDark} #6}};
    \node[anchor=west,text width=50mm,align=left] at (129,#1)
      {{\fontsize{6}{7.2}\selectfont\color{TTCTextDark} #7}};
    \draw[TTCBorder,line width=.45pt] (10,{#1-11}) -- (186,{#1-11});
  }

  \projectrowa{165}{01}{Nhà máy Công nghệ 2M}{2M Technocom • Việt Nam}{Khuôn mẫu \& Nhựa}{Yên Mỹ II\\Hưng Yên}{Tư vấn thiết kế \& Tổng thầu thi công}{TTCLightBlue}
  \projectrowa{143}{02}{Nhà máy Sơn ALO Việt Nam}{Sơn ALO • Việt Nam}{Sơn \& Hóa chất}{Phú Nghĩa\\Hà Nội}{Tổng thầu EPC • Xưởng \& Kho hóa chất}{white}
  \projectrowa{121}{03}{Nhà máy Nhựa Sendai}{Sendai Plastics • Việt Nam}{Nhựa kỹ thuật}{Ân Thi\\Hưng Yên}{Tổng thầu thi công • Hai xưởng \& văn phòng}{TTCLightBlue}
  \projectrowa{99}{04}{Tổ hợp Nhà máy May Lào Cai}{May Lào Cai • Việt Nam}{Dệt may cao tầng}{Phố Mới\\Lào Cai}{Tư vấn thiết kế \& thi công trọn gói}{white}
  \projectrowa{77}{05}{Nhà máy Nhựa DHL}{Tập đoàn Nhựa DHL • Việt Nam}{Bao bì \& màng nhựa}{Thái Hà\\Hà Nam}{Tổng thầu thi công • Xưởng \& văn phòng}{TTCLightBlue}
  \projectrowa{55}{06}{Nhà máy Nhôm Quang Thịnh}{CP Nhôm Quang Thịnh • Việt Nam}{Nhôm định hình}{Thuận Thành\\Bắc Ninh}{Tổng thầu thi công • Xưởng thép \& văn phòng}{white}
  \projectrowa{33}{07}{Xưởng Sản Xuất Foxconn}{Foxconn • Đài Loan}{12.000 m$^2$}{Quế Võ\\Bắc Ninh}{Kết cấu vượt nhịp • Lắp dựng nhà xưởng cao}{TTCLightBlue}
  \projectrowa{11}{08}{Tổ hợp Logistics BW Industrial}{BW Industrial • Singapore}{45.000 m$^2$}{Yên Phong\\Bắc Ninh}{Tổng thầu kho thông minh • Sàn siêu phẳng}{white}
\end{tikzpicture}

\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,35);
  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,35);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.2}{7.2}\selectfont\bfseries]
    at (7,29) {NĂNG LỰC ĐƯỢC CHỨNG MINH QUA DANH MỤC};
  \foreach \x in {46.5,93,139.5}{\draw[white!25!gray] (\x,5) -- (\x,23);}
  \node[align=center,text width=40mm] at (23.25,14) {
    {\fontsize{8.2}{9.5}\selectfont\bfseries\color{white} EPC / DESIGN--BUILD}\\[-.2mm]
    {\fontsize{5.9}{7.1}\selectfont\color{white!75!gray}Một đầu mối xuyên suốt}
  };
  \node[align=center,text width=40mm] at (69.75,14) {
    {\fontsize{8.2}{9.5}\selectfont\bfseries\color{white} KẾT CẤU \& PEB}\\[-.2mm]
    {\fontsize{5.9}{7.1}\selectfont\color{white!75!gray}Nhịp lớn • tải nặng • silo}
  };
  \node[align=center,text width=40mm] at (116.25,14) {
    {\fontsize{8.2}{9.5}\selectfont\bfseries\color{white} SÀN CÔNG NGHIỆP}\\[-.2mm]
    {\fontsize{5.9}{7.1}\selectfont\color{white!75!gray}Sàn tải nặng • sàn phẳng}
  };
  \node[align=center,text width=40mm] at (162.75,14) {
    {\fontsize{8.2}{9.5}\selectfont\bfseries\color{white} MEP / PCCC}\\[-.2mm]
    {\fontsize{5.9}{7.1}\selectfont\color{white!75!gray}Tích hợp theo vận hành}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_21 = r"""% ============================================================
% TRANG 21: SỔ DANH MỤC DỰ ÁN TIÊU BIỂU 09--16
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\pageheaderbar{DANH MỤC DỰ ÁN TIÊU BIỂU • 09--16}{Trang 21}
\pagefooterbar{Trang 21}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Danh Mục Dự Án Quốc Tế Và Công Nghiệp Phụ Trợ}{Tám công trình tiếp theo • Nhà đầu tư đa quốc gia • Yêu cầu chuyên biệt}

{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
NHÀ ĐẦU TƯ • CHUYÊN NGÀNH • GIẢI PHÁP TRIỂN KHAI\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
Danh mục thể hiện kinh nghiệm triển khai nhà máy thực phẩm, điện tử, cơ khí, logistics và năng lượng.\par}
\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,188);
  \fill[white,rounded corners=3pt] (0,0) rectangle (186,188);
  \draw[TTCBorder,rounded corners=3pt,line width=.7pt] (0,0) rectangle (186,188);

  \fill[TTCDeepNavy,rounded corners=3pt] (0,176) rectangle (186,188);
  \node[text=white,font=\fontsize{6.5}{7.5}\selectfont\bfseries] at (5,182) {STT};
  \node[anchor=west,text=white,font=\fontsize{6.5}{7.5}\selectfont\bfseries] at (14,182) {DỰ ÁN / CHỦ ĐẦU TƯ};
  \node[text=white,font=\fontsize{6.5}{7.5}\selectfont\bfseries] at (84,182) {QUY MÔ};
  \node[anchor=west,text=white,font=\fontsize{6.5}{7.5}\selectfont\bfseries] at (96,182) {ĐỊA ĐIỂM};
  \node[anchor=west,text=white,font=\fontsize{6.5}{7.5}\selectfont\bfseries] at (129,182) {PHẠM VI CÔNG VIỆC};

  \newcommand{\projectrowb}[8]{%
    \fill[#8] (0,{#1-11}) rectangle (186,{#1+11});
    \fill[TTCBlue] (0,{#1-11}) rectangle (10,{#1+11});
    \node[text=white,font=\fontsize{7}{8}\selectfont\bfseries] at (5,#1) {#2};
    \node[anchor=west,text width=53mm,align=left] at (14,#1) {
      {\fontsize{7.2}{8.4}\selectfont\bfseries\color{TTCBlue} #3}\\[-.2mm]
      {\fontsize{5.8}{7}\selectfont\color{TTCTextMuted} #4}
    };
    \node[align=center,text width=20mm] at (84,#1)
      {{\fontsize{7}{8.2}\selectfont\bfseries\color{TTCTextDark} #5}};
    \node[anchor=west,text width=29mm,align=left] at (96,#1)
      {{\fontsize{5.9}{7.1}\selectfont\color{TTCTextDark} #6}};
    \node[anchor=west,text width=50mm,align=left] at (129,#1)
      {{\fontsize{6}{7.2}\selectfont\color{TTCTextDark} #7}};
    \draw[TTCBorder,line width=.45pt] (10,{#1-11}) -- (186,{#1-11});
  }

  \projectrowb{165}{09}{Nhà máy Điện tử Towada}{Towada • Nhật Bản}{18.500 m$^2$}{Phúc Điền\\Hải Dương}{Xưởng lắp ráp linh kiện • Cơ điện MEP}{TTCLightBlue}
  \projectrowb{143}{10}{Kho Lạnh Logistics Yusen}{Yusen • Nhật Bản}{22.000 m$^2$}{Đình Vũ\\Hải Phòng}{Kho lạnh $-25^\circ$C • Cửa xuất nhập tự động}{white}
  \projectrowb{121}{11}{Nhà máy Dây Cáp Shinjo Vina}{Shinjo • Hàn Quốc}{14.000 m$^2$}{Bá Thiện 2\\Vĩnh Phúc}{Xưởng sản xuất cáp • Khung thép khẩu độ lớn}{TTCLightBlue}
  \projectrowb{99}{12}{Nhà máy Bao Bì Toyo Seikan}{Toyo Seikan • Nhật Bản}{22.000 m$^2$}{Tiên Sơn\\Bắc Ninh}{Tổng thầu EPC • Xưởng bao bì • Sàn phẳng}{white}
  \projectrowb{77}{13}{Nhà máy Nhựa Tiền Phong}{Tiền Phong • Việt Nam}{18.000 m$^2$}{An Dương\\Hải Phòng}{Xưởng đùn ống nhựa • Sàn theo tải thiết kế}{TTCLightBlue}
  \projectrowb{55}{14}{Kho Logistics Yusen}{Yusen • Nhật Bản}{25.000 m$^2$}{Đình Vũ\\Hải Phòng}{Kho ngoại quan • Cụm sàn nâng hàng}{white}
  \projectrowb{33}{15}{Nhà máy Thực Phẩm A-One}{Saigon Ve Wong • Đài Loan}{30.000 m$^2$}{Sóng Thần 2\\Bình Dương}{Xưởng chế biến thực phẩm • Chuẩn HACCP}{TTCLightBlue}
  \projectrowb{11}{16}{Nhà máy Năng Lượng Sơn Hà}{Sơn Hà • Việt Nam}{24.000 m$^2$}{Thuận Thành\\Bắc Ninh}{Xưởng sản xuất bồn • Pin mặt trời}{white}
\end{tikzpicture}

\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,35);
  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,35);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.2}{7.2}\selectfont\bfseries]
    at (7,29) {TỪ DANH MỤC ĐẾN 6 HỒ SƠ DỰ ÁN • TRANG 22--27};
  \foreach \x in {62,124}{\draw[white!25!gray] (\x,5) -- (\x,23);}
  \node[align=center,text width=53mm] at (31,14) {
    {\fontsize{7.8}{9.2}\selectfont\bfseries\color{white} CÔNG NGHỆ 2M • SƠN ALO}\\[-.2mm]
    {\fontsize{6}{7.2}\selectfont\color{white!75!gray}Khuôn mẫu chính xác • xưởng sơn \& hóa chất}
  };
  \node[align=center,text width=53mm] at (93,14) {
    {\fontsize{7.8}{9.2}\selectfont\bfseries\color{white} SENDAI • MAY LÀO CAI}\\[-.2mm]
    {\fontsize{6}{7.2}\selectfont\color{white!75!gray}Nhựa kỹ thuật • may xưởng nhiều tầng}
  };
  \node[align=center,text width=53mm] at (155,14) {
    {\fontsize{7.8}{9.2}\selectfont\bfseries\color{white} NHỰA DHL • NHÔM QUANG THỊNH}\\[-.2mm]
    {\fontsize{6}{7.2}\selectfont\color{white!75!gray}Bao bì nhựa màng • nhôm đùn ép định hình}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_22_LEGACY = r"""% ============================================================
% TRANG 22: CASE STUDY 01 -- NHÀ MÁY DỆT MAY HỒNG TRANG
% ============================================================
\pageheaderbar{SELECTED CASE STUDY 01 -- HỒNG TRANG PLANT}{Trang 22}
\pagefooterbar{Trang 22}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.03, scale=2.8, font=\bfseries\sffamily, text=TTCBlue] at ([yshift=-10mm]current page.center) {HONG TRANG INDUSTRIAL TEXTILE PLANT};
  \draw[TTCBlue!6!white, line width=0.5pt] ([xshift=15mm, yshift=20mm]current page.south west) grid[step=8mm] ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Case Study 01: Tổ Hợp Nhà Máy Gạch Hồng Trang (100.000 m$^2$)}{Hong Trang Garment \& Industrial Complex \textbullet\ 75,000 m$^2$ Floor \textbullet\ 42m Clear Span \textbullet\ Fast-Track 150 Days}

% TẦNG 1: ẢNH HIỆN TRƯỜNG DỰ ÁN (Trái) \& THÔNG SỐ KỸ THUẬT (Phải)
\noindent
\begin{tabular}{@{}p{100mm}@{\hspace{4mm}}p{82mm}@{}}
  % Ảnh dự án
  \begin{tikzpicture}
    \clip[rounded corners=6pt] (0,0) rectangle (10.0, 9.2);
    \node[anchor=center, inner sep=0pt] at (5.0, 4.6) {
      \includegraphics[width=100mm, height=92mm]{../../public/project-assets/hongtrang.jpg}
    };
    \fill[TTCDeepNavy, opacity=0.85] (0, 0) rectangle (10.0, 1.4);
    \node[anchor=west, text=white, font=\fontsize{7.5}{9}\selectfont\bfseries] at (0.3, 0.7) {
      \faIndustry\quad TỔ HỢP NHÀ MÁY GẠCH HỒNG TRANG -- VĨNH PHÚC
    };
  \end{tikzpicture} &
  % Thông số kỹ thuật
  \begin{tikzpicture}
    \node[
      rounded corners=6pt,
      fill=TTCDeepNavy!95!black,
      draw=TTCCyan!80!white,
      line width=0.9pt,
      minimum width=82mm,
      minimum height=92mm,
      inner sep=6pt,
      text width=74mm,
      align=left
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCCyan} \faInfoCircle\quad THÔNG TIN TỔNG QUAN DỰ ÁN:}\\[4pt]
      {\fontsize{7.2}{9.5}\selectfont\color{white}
      \textbf{Chủ đầu tư:} Công ty Cổ phần Gạch Hồng Trang\newline
      \textbf{Địa điểm:} Huyện Lập Thạch, Tỉnh Vĩnh Phúc\newline
      \textbf{Diện tích quy hoạch:} \textbf{\color{TTCGold}100.000 m$^2$}\newline
      \textbf{Diện tích sàn xây dựng:} \textbf{\color{TTCCyan}75.000 m$^2$}\newline
      \textbf{Khẩu độ vượt nhịp:} \textbf{\color{white}42 mét (không cột giữa)}\newline
      \textbf{Thời gian thi công:} \textbf{\color{TTCRed}150 ngày (Fast-track)}\newline
      \textbf{Khối lượng kết cấu thép:} \textbf{2.200 Tấn PEB}\newline
      \textbf{Phạm vi hợp đồng:} Tổng thầu EPC trọn gói (Thiết kế BIM, Sản xuất PEB, Móng cọc, Lắp dựng kết cấu, Hạ tầng KCN \& PCCC tự động).}\\[6pt]
      \rule{\linewidth}{0.4pt}\\[4pt]
      {\fontsize{6.8}{8.5}\selectfont\color{white!80!gray}
      Bàn giao đúng tiến độ, đạt chuẩn kiểm toán khắt khe của các nhãn hàng thời trang xuất khẩu Châu Âu.}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{2mm}

% TẦNG 2: 3 ĐIỂM NỔI BẬT KỸ THUẬT
\noindent
\begin{tabular}{@{}p{59mm}@{\hspace{3.5mm}}p{59mm}@{\hspace{3.5mm}}p{59mm}@{}}
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=59mm, minimum height=50mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCRed} \faDraftingCompass\ Vượt Nhịp 42m Tối Ưu}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ Thiết kế dầm thép tiết diện thay đổi vượt nhịp 42m.\newline
      \textbullet\ Tăng 18\% diện tích bố trí dây chuyền may tự động.\newline
      \textbullet\ Tối ưu hóa không gian cho Chủ đầu tư.}
    };
  \end{tikzpicture} &
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=59mm, minimum height=50mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCCyan} \faBolt\ Tiến Độ Fast-Track 150 Ngày}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ Triển khai thi công 3 ca liên tục.\newline
      \textbullet\ Sản xuất 2.200 tấn dầm thép tại xưởng đồng thời ép cọc.\newline
      \textbullet\ Rút ngắn 45 ngày so với tiến độ cam kết.}
    };
  \end{tikzpicture} &
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=59mm, minimum height=50mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCBlue} \faLeaf\ Sàn Chống Bụi \& Mái Mát}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ Sàn bê tông phẳng Laser Screed tăng cứng Hardener Sika.\newline
      \textbullet\ Mái tôn Seamlock cách nhiệt Rockwool chống dột.\newline
      \textbullet\ Giảm 6$^\circ$C nhiệt độ làm việc trong nhà xưởng.}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{2mm}

% TẦNG 3: BĂNG KPI CASE STUDY
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
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCRed} 75.000 m$^2$} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCCyan} 150 NGÀY} &
      {\fontsize{14}{16}\selectfont\bfseries\color{white} NHỊP 42M} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCGold} 2.200 TẤN} \\
      {\fontsize{7.2}{9}\selectfont Sàn Xây Dựng Hoàn Thành} &
      {\fontsize{7.2}{9}\selectfont Tiến Độ Thi Công Thần Tốc} &
      {\fontsize{7.2}{9}\selectfont Khẩu Độ Không Cột Giữa} &
      {\fontsize{7.2}{9}\selectfont Thép Kết Cấu Chế Tạo}
    \end{tabularx}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_23_LEGACY = r"""% ============================================================
% TRANG 23: CASE STUDY 02 -- NHÀ MÁY DỆT MAY SÔNG HỒNG 7
% ============================================================
\pageheaderbar{SELECTED CASE STUDY 02 -- SÔNG HỒNG 7 PLANT}{Trang 23}
\pagefooterbar{Trang 23}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.03, scale=2.8, font=\bfseries\sffamily, text=TTCBlue] at ([yshift=-10mm]current page.center) {SONG HONG 7 GARMENT MANUFACTURING PLANT};
  \draw[TTCBlue!6!white, line width=0.5pt] ([xshift=15mm, yshift=20mm]current page.south west) grid[step=8mm] ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Case Study 02: Nhà Máy May Sông Hồng 7 (68.000 m$^2$ Sàn 2 Tầng)}{Song Hong 7 Garment Plant \textbullet\ 68,000 m$^2$ Multi-Story Floor \textbullet\ 1,200 kg/m$^2$ Load \textbullet\ Solar-Ready 2.5MWp}

% TẦNG 1: ẢNH HIỆN TRƯỜNG DỰ ÁN (Trái) \& THÔNG SỐ KỸ THUẬT (Phải)
\noindent
\begin{tabular}{@{}p{100mm}@{\hspace{4mm}}p{82mm}@{}}
  % Ảnh dự án
  \begin{tikzpicture}
    \clip[rounded corners=6pt] (0,0) rectangle (10.0, 9.2);
    \node[anchor=center, inner sep=0pt] at (5.0, 4.6) {
      \includegraphics[width=100mm, height=92mm]{../../public/project-assets/songhong7.jpg}
    };
    \fill[TTCDeepNavy, opacity=0.85] (0, 0) rectangle (10.0, 1.4);
    \node[anchor=west, text=white, font=\fontsize{7.5}{9}\selectfont\bfseries] at (0.3, 0.7) {
      \faIndustry\quad NHÀ MÁY MAY SÔNG HỒNG 7 -- NAM ĐỊNH
    };
  \end{tikzpicture} &
  % Thông số kỹ thuật
  \begin{tikzpicture}
    \node[
      rounded corners=6pt,
      fill=TTCDeepNavy!95!black,
      draw=TTCCyan!80!white,
      line width=0.9pt,
      minimum width=82mm,
      minimum height=92mm,
      inner sep=6pt,
      text width=74mm,
      align=left
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCCyan} \faInfoCircle\quad THÔNG TIN TỔNG QUAN DỰ ÁN:}\\[4pt]
      {\fontsize{7.2}{9.5}\selectfont\color{white}
      \textbf{Chủ đầu tư:} Công ty Cổ phần May Sông Hồng\newline
      \textbf{Địa điểm:} Huyện Hải Hậu, Tỉnh Nam Định\newline
      \textbf{Diện tích sàn:} \textbf{\color{TTCCyan}68.000 m$^2$ (Xưởng 2 tầng BTCT)}\newline
      \textbf{Tải trọng sàn tầng 2:} \textbf{\color{TTCGold}1.200 kg/m$^2$}\newline
      \textbf{Hệ thống điện mặt trời:} \textbf{\color{white}Solar-Ready 2.5MWp}\newline
      \textbf{Thời gian thi công:} \textbf{\color{TTCRed}180 ngày (Sớm 30 ngày)}\newline
      \textbf{Khối lượng kết cấu thép:} \textbf{3.800 Tấn PEB}\newline
      \textbf{Phạm vi hợp đồng:} Tổng thầu Thiết kế \& Thi công Kết cấu dầm sàn 2 tầng, MEP công nghiệp, PCCC tự động \& Hạ tầng xanh.}\\[6pt]
      \rule{\linewidth}{0.4pt}\\[4pt]
      {\fontsize{6.8}{8.5}\selectfont\color{white!80!gray}
      Dự án trọng điểm kiểu mẫu ngành dệt may Việt Nam, đáp ứng tiêu chuẩn xanh LEED của các thị trường Mỹ \& EU.}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{2mm}

% TẦNG 2: 3 ĐIỂM NỔI BẬT KỸ THUẬT
\noindent
\begin{tabular}{@{}p{59mm}@{\hspace{3.5mm}}p{59mm}@{\hspace{3.5mm}}p{59mm}@{}}
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=59mm, minimum height=50mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCRed} \faLayerGroup\ Sàn 2 Tầng Tải Trọng Nặng}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ Kết cấu sàn liên hợp thép -- bê tông cốt thép.\newline
      \textbullet\ Chịu tải trọng động máy may công nghiệp 1.200 kg/m$^2$.\newline
      \textbullet\ Triệt tiêu độ rung truyền qua kết cấu cột.}
    };
  \end{tikzpicture} &
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=59mm, minimum height=50mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCCyan} \faSolarPanel\ Sẵn Sàng Điện Mặt Trời}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ Vì kèo thép gia cường chịu tải thêm 20 kg/m$^2$.\newline
      \textbullet\ Lắp đặt hệ thống pin mặt trời áp mái 2.5MWp.\newline
      \textbullet\ Tiết kiệm 30\% chi phí năng lượng vận hành.}
    };
  \end{tikzpicture} &
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=59mm, minimum height=50mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCBlue} \faCubes\ Ứng Dụng Mô Hình BIM 5D}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ Đồng bộ hệ kết cấu dầm sàn và cơ điện HVAC.\newline
      \textbullet\ Kiểm soát xung đột không gian tuyệt đối 100\%.\newline
      \textbullet\ Bàn giao công trình sớm 30 ngày so với hợp đồng.}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{2mm}

% TẦNG 3: BĂNG KPI CASE STUDY 2
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
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCRed} 68.000 m$^2$} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCCyan} 1.200 kg/m$^2$} &
      {\fontsize{14}{16}\selectfont\bfseries\color{white} 2.5 MWp} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCGold} 3.800 TẤN} \\
      {\fontsize{7.2}{9}\selectfont Sàn Xây Dựng 2 Tầng} &
      {\fontsize{7.2}{9}\selectfont Tải Trọng Động Sàn Tầng 2} &
      {\fontsize{7.2}{9}\selectfont Điện Mặt Trời Áp Mái} &
      {\fontsize{7.2}{9}\selectfont Thép Kết Cấu PEB}
    \end{tabularx}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_24_LEGACY = r"""% ============================================================
% TRANG 24: CASE STUDY 03 -- TỔ HỢP JAPFA COMFEED [TRANG MỚI TÁCH RIÊNG]
% ============================================================
\pageheaderbar{SELECTED CASE STUDY 03 -- JAPFA COMFEED COMPLEX}{Trang 24}
\pagefooterbar{Trang 24}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.03, scale=2.8, font=\bfseries\sffamily, text=TTCBlue] at ([yshift=-10mm]current page.center) {JAPFA COMFEED AGRO-INDUSTRIAL COMPLEX};
  \draw[TTCBlue!6!white, line width=0.5pt] ([xshift=15mm, yshift=20mm]current page.south west) grid[step=8mm] ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Case Study 03: Tổ Hợp Nhà Máy Thức Ăn Chăn Nuôi Japfa Comfeed}{Japfa Comfeed Agro-Industrial Complex \textbullet\ 50,000 m$^2$ \textbullet\ 45m Silo Tower \textbullet\ Heavy Dynamic Load Foundations}

% TẦNG 1: ẢNH HIỆN TRƯỜNG DỰ ÁN (Trái) \& THÔNG SỐ KỸ THUẬT (Phải)
\noindent
\begin{tabular}{@{}p{100mm}@{\hspace{4mm}}p{82mm}@{}}
  % Ảnh dự án
  \begin{tikzpicture}
    \clip[rounded corners=6pt] (0,0) rectangle (10.0, 9.2);
    \node[anchor=center, inner sep=0pt] at (5.0, 4.6) {
      \includegraphics[width=100mm, height=92mm]{../../public/project-assets/japfa.jpg}
    };
    \fill[TTCDeepNavy, opacity=0.85] (0, 0) rectangle (10.0, 1.4);
    \node[anchor=west, text=white, font=\fontsize{7.5}{9}\selectfont\bfseries] at (0.3, 0.7) {
      \faIndustry\quad TỔ HỢP NHÀ MÁY JAPFA COMFEED -- VĨNH PHÚC / THÁI BÌNH
    };
  \end{tikzpicture} &
  % Thông số kỹ thuật
  \begin{tikzpicture}
    \node[
      rounded corners=6pt,
      fill=TTCDeepNavy!95!black,
      draw=TTCCyan!80!white,
      line width=0.9pt,
      minimum width=82mm,
      minimum height=92mm,
      inner sep=6pt,
      text width=74mm,
      align=left
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCCyan} \faInfoCircle\quad THÔNG TIN TỔNG QUAN DỰ ÁN:}\\[4pt]
      {\fontsize{7.2}{9.5}\selectfont\color{white}
      \textbf{Chủ đầu tư:} Tập đoàn Japfa Comfeed (Indonesia)\newline
      \textbf{Địa điểm:} Tỉnh Vĩnh Phúc \& Tỉnh Thái Bình\newline
      \textbf{Diện tích quy hoạch:} \textbf{\color{TTCGold}50.000 m$^2$}\newline
      \textbf{Chiều cao tháp Silo:} \textbf{\color{TTCCyan}45 mét (Kết cấu thép Silo)}\newline
      \textbf{Khối lượng kết cấu thép:} \textbf{\color{white}2.800 Tấn PEB}\newline
      \textbf{Thời gian thi công:} \textbf{\color{TTCRed}165 ngày (Fast-track)}\newline
      \textbf{Tiêu chuẩn an toàn:} \textbf{OHSAS 18001 / HACCP}\newline
      \textbf{Phạm vi hợp đồng:} Tổng thầu EPC Xây dựng xưởng sản xuất cám, cụm tháp Silo chứa ngũ cốc 45m, móng sâu chịu động lực máy nghiền \& Trạm điện 22kV.}\\[6pt]
      \rule{\linewidth}{0.4pt}\\[4pt]
      {\fontsize{6.8}{8.5}\selectfont\color{white!80!gray}
      Dự án vốn FDI Indonesia đạt chuẩn quốc tế khắt khe về an toàn thực phẩm, chống nổ bụi và vận hành liên tục 24/7.}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{2mm}

% TẦNG 2: 3 ĐIỂM NỔI BẬT KỸ THUẬT
\noindent
\begin{tabular}{@{}p{59mm}@{\hspace{3.5mm}}p{59mm}@{\hspace{3.5mm}}p{59mm}@{}}
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=59mm, minimum height=50mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCRed} \faBuilding\ Tháp Silo Kết Cấu Cao 45m}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ Thi công lắp dựng tháp Silo thép cao 45m an toàn tuyệt đối.\newline
      \textbullet\ Sử dụng cẩu 100T tự hành lắp dựng các phân đoạn siêu trọng.\newline
      \textbullet\ Kiểm tra 100\% bu-lông cường độ cao 10.9 bằng cờ lê lực.}
    };
  \end{tikzpicture} &
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=59mm, minimum height=50mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCCyan} \faShield*\ Chống Nổ Bụi \& Thông Gió}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ Thiết kế hệ thống thu gom và lọc bụi túi vải đạt chuẩn ATEX.\newline
      \textbullet\ Cửa xả áp lực nổ tự động trên mái và vách tháp Silo.\newline
      \textbullet\ Đảm bảo môi trường làm việc sạch bụi đạt chuẩn HACCP.}
    };
  \end{tikzpicture} &
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=59mm, minimum height=50mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCBlue} \faHammer\ Móng Chịu Tải Động Lực}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ Móng cọc khoan nhồi sâu D800 chịu tải trọng động máy nghiền.\newline
      \textbullet\ Đệm cao su giảm chấn triệt tiêu rung động lan truyền.\newline
      \textbullet\ Đổ bê tông khối lớn liên tục không để lại mạch ngừng nhiệt.}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{2mm}

% TẦNG 3: BĂNG KPI CASE STUDY 3
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
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCRed} 50.000 m$^2$} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCCyan} SILO 45M} &
      {\fontsize{14}{16}\selectfont\bfseries\color{white} 2.800 TẤN} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCGold} 0 SỰ CỐ} \\
      {\fontsize{7.2}{9}\selectfont Diện Tích Quy Hoạch} &
      {\fontsize{7.2}{9}\selectfont Chiều Cao Tháp Thép} &
      {\fontsize{7.2}{9}\selectfont Khối Lượng Thép PEB} &
      {\fontsize{7.2}{9}\selectfont An Toàn Tuyệt Đối}
    \end{tabularx}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_25_LEGACY = r"""% ============================================================
% TRANG 25: CASE STUDY 04 -- NHÀ MÁY DAEYUN ST VINA [TRANG MỚI TÁCH RIÊNG]
% ============================================================
\pageheaderbar{SELECTED CASE STUDY 04 -- DAEYUN ST VINA}{Trang 25}
\pagefooterbar{Trang 25}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.03, scale=2.8, font=\bfseries\sffamily, text=TTCBlue] at ([yshift=-10mm]current page.center) {DAEYUN ST VINA PRECISION \& CLEANROOM};
  \draw[TTCBlue!6!white, line width=0.5pt] ([xshift=15mm, yshift=20mm]current page.south west) grid[step=8mm] ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Case Study 04: Nhà Máy Daeyun ST Vina (20.000 m$^2$ Phòng Sạch)}{Daeyun ST Vina Precision Plant \textbullet\ 20,000 m$^2$ \textbullet\ Cleanroom Class 10,000 ISO 14644-1 \textbullet\ ESD Vinyl Floor}

% TẦNG 1: ẢNH HIỆN TRƯỜNG DỰ ÁN (Trái) \& THÔNG SỐ KỸ THUẬT (Phải)
\noindent
\begin{tabular}{@{}p{100mm}@{\hspace{4mm}}p{82mm}@{}}
  % Ảnh dự án
  \begin{tikzpicture}
    \clip[rounded corners=6pt] (0,0) rectangle (10.0, 9.2);
    \node[anchor=center, inner sep=0pt] at (5.0, 4.6) {
      \includegraphics[width=100mm, height=92mm]{../../public/project-assets/daeyun.jpg}
    };
    \fill[TTCDeepNavy, opacity=0.85] (0, 0) rectangle (10.0, 1.4);
    \node[anchor=west, text=white, font=\fontsize{7.5}{9}\selectfont\bfseries] at (0.3, 0.7) {
      \faIndustry\quad NHÀ MÁY DAEYUN ST VINA -- KCN BÁ THIỆN 2
    };
  \end{tikzpicture} &
  % Thông số kỹ thuật
  \begin{tikzpicture}
    \node[
      rounded corners=6pt,
      fill=TTCDeepNavy!95!black,
      draw=TTCCyan!80!white,
      line width=0.9pt,
      minimum width=82mm,
      minimum height=92mm,
      inner sep=6pt,
      text width=74mm,
      align=left
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCCyan} \faInfoCircle\quad THÔNG TIN TỔNG QUAN DỰ ÁN:}\\[4pt]
      {\fontsize{7.2}{9.5}\selectfont\color{white}
      \textbf{Chủ đầu tư:} Daeyun Group (Hàn Quốc)\newline
      \textbf{Địa điểm:} KCN Bá Thiện 2, Tỉnh Vĩnh Phúc\newline
      \textbf{Diện tích quy hoạch:} \textbf{\color{TTCGold}20.000 m$^2$}\newline
      \textbf{Cấp độ phòng sạch:} \textbf{\color{TTCCyan}Class 10.000 (ISO 14644-1)}\newline
      \textbf{Kiểm soát môi trường:} \textbf{\color{white}$\pm 1^\circ$C nhiệt độ / $\pm 5\%$ độ ẩm}\newline
      \textbf{Thời gian thi công:} \textbf{\color{TTCRed}135 ngày (Fast-track)}\newline
      \textbf{Sàn hoàn thiện:} \textbf{Vinyl Conductive kháng tĩnh điện ESD}\newline
      \textbf{Phạm vi hợp đồng:} Tổng thầu EPC Kết cấu nhà xưởng, Khu phòng sạch linh kiện điện tử, Hệ thống điều hòa chính xác AHU/HEPA \& Hệ thống cấp điện trung thế.}\\[6pt]
      \rule{\linewidth}{0.4pt}\\[4pt]
      {\fontsize{6.8}{8.5}\selectfont\color{white!80!gray}
      Dự án phụ trợ điện tử cao cấp vốn FDI Hàn Quốc, bàn giao nghiệm thu 100\% đạt chuẩn phòng sạch quốc tế ngay lần đánh giá đầu tiên.}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{2mm}

% TẦNG 2: 3 ĐIỂM NỔI BẬT KỸ THUẬT
\noindent
\begin{tabular}{@{}p{59mm}@{\hspace{3.5mm}}p{59mm}@{\hspace{3.5mm}}p{59mm}@{}}
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=59mm, minimum height=50mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCRed} \faWind\ Phòng Sạch Class 10.000}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ Vách panel Sandwich EPS/PU chống cháy lan kín khít.\newline
      \textbullet\ Trần panel chịu tải kết hợp phin lọc HEPA H14 hiệu suất 99.99\%.\newline
      \textbullet\ Duy trì áp suất dương ngăn chặn bụi xâm nhập từ ngoài.}
    };
  \end{tikzpicture} &
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=59mm, minimum height=50mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCCyan} \faBolt\ Sàn Vinyl Kháng Tĩnh Điện}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ Lưới đồng tiếp địa ngầm nối đất điện trở $<10\,\Omega$.\newline
      \textbullet\ Tấm Vinyl dẫn điện tiêu tán tĩnh điện bảo vệ linh kiện điện tử.\newline
      \textbullet\ Bề mặt kháng hóa chất, không sinh bụi, dễ dàng vệ sinh.}
    };
  \end{tikzpicture} &
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=59mm, minimum height=50mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCBlue} \faThermometerHalf\ Điều Hòa Chính Xác AHU}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ Cụm xử lý không khí AHU điều khiển biến tần tự động.\newline
      \textbullet\ Kiểm soát nhiệt độ $\pm 1^\circ$C và độ ẩm $\pm 5\%$ ổn định 24/7.\newline
      \textbullet\ Hệ thống Chiller làm lạnh giải nhiệt gió tiết kiệm điện.}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{2mm}

% TẦNG 3: BĂNG KPI CASE STUDY 4
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
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCRed} 20.000 m$^2$} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCCyan} CLASS 10.000} &
      {\fontsize{14}{16}\selectfont\bfseries\color{white} $\pm 1^\circ$C} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCGold} ESD VINYL} \\
      {\fontsize{7.2}{9}\selectfont Diện Tích Xây Dựng} &
      {\fontsize{7.2}{9}\selectfont Tiêu Chuẩn Phòng Sạch} &
      {\fontsize{7.2}{9}\selectfont Độ Chính Xác Nhiệt Độ} &
      {\fontsize{7.2}{9}\selectfont Sàn Kháng Tĩnh Điện}
    \end{tabularx}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_26_LEGACY = r"""% ============================================================
% TRANG 26: CASE STUDY 05 -- NHÀ MÁY SUMIDENSO VINA [TRANG MỚI TÁCH RIÊNG]
% ============================================================
\pageheaderbar{SELECTED CASE STUDY 05 -- SUMIDENSO VINA}{Trang 26}
\pagefooterbar{Trang 26}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.03, scale=2.8, font=\bfseries\sffamily, text=TTCBlue] at ([yshift=-10mm]current page.center) {SUMIDENSO AUTOMOTIVE WIRE HARNESS};
  \draw[TTCBlue!6!white, line width=0.5pt] ([xshift=15mm, yshift=20mm]current page.south west) grid[step=8mm] ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Case Study 05: Nhà Máy Dây Cáp Sumidenso (Sumitomo Group Nhật Bản)}{Sumidenso Automotive Wire Harness Plant \textbullet\ 15,015 m$^2$ \textbullet\ Japanese Quality Standards \textbullet\ Laser Screed FM2 Floor}

% TẦNG 1: ẢNH HIỆN TRƯỜNG DỰ ÁN (Trái) \& THÔNG SỐ KỸ THUẬT (Phải)
\noindent
\begin{tabular}{@{}p{100mm}@{\hspace{4mm}}p{82mm}@{}}
  % Ảnh dự án
  \begin{tikzpicture}
    \clip[rounded corners=6pt] (0,0) rectangle (10.0, 9.2);
    \node[anchor=center, inner sep=0pt] at (5.0, 4.6) {
      \includegraphics[width=100mm, height=92mm]{../../public/project-assets/sumidenso.jpg}
    };
    \fill[TTCDeepNavy, opacity=0.85] (0, 0) rectangle (10.0, 1.4);
    \node[anchor=west, text=white, font=\fontsize{7.5}{9}\selectfont\bfseries] at (0.3, 0.7) {
      \faIndustry\quad NHÀ MÁY DÂY CÁP SUMIDENSO -- KCN SÔNG HẬU
    };
  \end{tikzpicture} &
  % Thông số kỹ thuật
  \begin{tikzpicture}
    \node[
      rounded corners=6pt,
      fill=TTCDeepNavy!95!black,
      draw=TTCCyan!80!white,
      line width=0.9pt,
      minimum width=82mm,
      minimum height=92mm,
      inner sep=6pt,
      text width=74mm,
      align=left
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCCyan} \faInfoCircle\quad THÔNG TIN TỔNG QUAN DỰ ÁN:}\\[4pt]
      {\fontsize{7.2}{9.5}\selectfont\color{white}
      \textbf{Chủ đầu tư:} Sumitomo Electric Group (Nhật Bản)\newline
      \textbf{Địa điểm:} KCN Sông Hậu, Tỉnh Hậu Giang\newline
      \textbf{Diện tích sàn:} \textbf{\color{TTCCyan}15.015 m$^2$}\newline
      \textbf{Tiêu chuẩn độ phẳng sàn:} \textbf{\color{TTCGold}Laser Screed FM2 (TR34)}\newline
      \textbf{Thời gian thi công:} \textbf{\color{TTCRed}120 ngày (Fast-track)}\newline
      \textbf{Hệ thống PCCC:} \textbf{\color{white}Sprinkler tự động phản ứng nhanh}\newline
      \textbf{Chất lượng quản lý:} \textbf{Chuẩn mực 5S \& Kaizen Nhật Bản}\newline
      \textbf{Phạm vi hợp đồng:} Tổng thầu EPC Xây dựng nhà máy sản xuất mạng dây điện ô tô, Hệ thống cơ điện MEP, Trạm xử lý nước thải \& Cảnh quan.}\\[6pt]
      \rule{\linewidth}{0.4pt}\\[4pt]
      {\fontsize{6.8}{8.5}\selectfont\color{white!80!gray}
      Dự án FDI Nhật Bản khắt khe về độ sạch, thẩm mỹ kiến trúc và an toàn tuyệt đối. Bàn giao đúng hẹn với thư khen từ Tổng Giám Đốc Sumidenso.}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{2mm}

% TẦNG 2: 3 ĐIỂM NỔI BẬT KỸ THUẬT
\noindent
\begin{tabular}{@{}p{59mm}@{\hspace{3.5mm}}p{59mm}@{\hspace{3.5mm}}p{59mm}@{}}
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=59mm, minimum height=50mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCRed} \faLevelDown*\ Sàn Phẳng Laser Screed}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ Máy san gạt Laser Screed Somero tự động độ chính xác cao.\newline
      \textbullet\ Đạt chuẩn độ phẳng siêu phẳng FM2 theo tiêu chuẩn TR34.\newline
      \textbullet\ Đảm bảo xe nâng tự động AGV vận hành êm ái 100\%.}
    };
  \end{tikzpicture} &
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=59mm, minimum height=50mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCCyan} \faFireExtinguisher\ PCCC Tự Động Chuẩn NFPA}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ Mạng lưới đầu phun Sprinkler phản ứng nhanh độ nhạy cao.\newline
      \textbullet\ Bơm chữa cháy Grundfos chứng chỉ UL/FM công suất 2.500 GPM.\newline
      \textbullet\ Màng ngăn cháy cách nhiệt và hệ thống hút khói tự động.}
    };
  \end{tikzpicture} &
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=59mm, minimum height=50mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCBlue} \faFlag\ Quản Lý Chuẩn Nhật Bản}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ Áp dụng triệt để văn hóa 5S và phương pháp Kaizen hiện trường.\newline
      \textbullet\ Báo cáo tiến độ và chất lượng bằng tiếng Nhật \& tiếng Anh hàng ngày.\newline
      \textbullet\ 100\% hạng mục nghiệm thu không có lỗi tồn đọng (Zero-Defect).}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{2mm}

% TẦNG 3: BĂNG KPI CASE STUDY 5
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
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCRed} 15.015 m$^2$} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCCyan} FM2 TR34} &
      {\fontsize{14}{16}\selectfont\bfseries\color{white} 120 NGÀY} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCGold} 0 DEFECT} \\
      {\fontsize{7.2}{9}\selectfont Sàn Xây Dựng Hoàn Thành} &
      {\fontsize{7.2}{9}\selectfont Chuẩn Độ Phẳng Sàn} &
      {\fontsize{7.2}{9}\selectfont Tiến Độ Fast-Track} &
      {\fontsize{7.2}{9}\selectfont Nghiệm Thu Không Lỗi}
    \end{tabularx}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_27_LEGACY = r"""% ============================================================
% TRANG 27: CASE STUDY 06 -- KHO BW INDUSTRIAL \& FOXCONN [TRANG MỚI TÁCH RIÊNG]
% ============================================================
\pageheaderbar{SELECTED CASE STUDY 06 -- BW INDUSTRIAL \& FOXCONN}{Trang 27}
\pagefooterbar{Trang 27}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.03, scale=2.8, font=\bfseries\sffamily, text=TTCBlue] at ([yshift=-10mm]current page.center) {BW INDUSTRIAL \& FOXCONN LOGISTICS HUB};
  \draw[TTCBlue!6!white, line width=0.5pt] ([xshift=15mm, yshift=20mm]current page.south west) grid[step=8mm] ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Case Study 06: Tổ Hợp Logistics BW Industrial \& Xưởng Foxconn}{BW Industrial \& Foxconn Smart Logistics \textbullet\ 45,000 m$^2$ \textbullet\ 5,000 kg/m$^2$ Heavy Floor Load \textbullet\ Automated Dock Levelers}

% TẦNG 1: ẢNH HIỆN TRƯỜNG DỰ ÁN (Trái) \& THÔNG SỐ KỸ THUẬT (Phải)
\noindent
\begin{tabular}{@{}p{100mm}@{\hspace{4mm}}p{82mm}@{}}
  % Ảnh dự án
  \begin{tikzpicture}
    \clip[rounded corners=6pt] (0,0) rectangle (10.0, 9.2);
    \node[anchor=center, inner sep=0pt] at (5.0, 4.6) {
      \includegraphics[width=100mm, height=92mm]{../../public/project-assets/foxcon.png}
    };
    \fill[TTCDeepNavy, opacity=0.85] (0, 0) rectangle (10.0, 1.4);
    \node[anchor=west, text=white, font=\fontsize{7.5}{9}\selectfont\bfseries] at (0.3, 0.7) {
      \faWarehouse\quad TỔ HỢP LOGISTICS BW INDUSTRIAL \& XƯỞNG FOXCONN
    };
  \end{tikzpicture} &
  % Thông số kỹ thuật
  \begin{tikzpicture}
    \node[
      rounded corners=6pt,
      fill=TTCDeepNavy!95!black,
      draw=TTCCyan!80!white,
      line width=0.9pt,
      minimum width=82mm,
      minimum height=92mm,
      inner sep=6pt,
      text width=74mm,
      align=left
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCCyan} \faInfoCircle\quad THÔNG TIN TỔNG QUAN DỰ ÁN:}\\[4pt]
      {\fontsize{7.2}{9.5}\selectfont\color{white}
      \textbf{Chủ đầu tư:} BW Industrial (Singapore) / Foxconn (Đài Loan)\newline
      \textbf{Địa điểm:} KCN Yên Phong \& KCN Quế Võ, Bắc Ninh\newline
      \textbf{Diện tích sàn:} \textbf{\color{TTCCyan}45.000 m$^2$ (Kho thông minh cao tầng)}\newline
      \textbf{Tải trọng sàn chịu lực:} \textbf{\color{TTCGold}5.000 kg/m$^2$ (5 Tấn/m$^2$)}\newline
      \textbf{Chiều cao thông thủy:} \textbf{\color{white}12.5 mét (Tối ưu xếp 6 tầng kệ)}\newline
      \textbf{Thời gian thi công:} \textbf{\color{TTCRed}150 ngày (Fast-track)}\newline
      \textbf{Trang thiết bị bốc dỡ:} \textbf{24 Cụm Dock Leveler thủy lực}\newline
      \textbf{Phạm vi hợp đồng:} Tổng thầu EPC Kết cấu thép nhịp lớn, Sàn chịu tải nặng mài bóng Liquid Hardener, Hệ thống PCCC màng ngăn cháy \& Đường nội bộ xe container.}\\[6pt]
      \rule{\linewidth}{0.4pt}\\[4pt]
      {\fontsize{6.8}{8.5}\selectfont\color{white!80!gray}
      Tổ hợp logistics thông minh đạt chuẩn quốc tế phục vụ chuỗi cung ứng linh kiện điện tử cho tập đoàn Foxconn \& Apple.}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{2mm}

% TẦNG 2: 3 ĐIỂM NỔI BẬT KỸ THUẬT
\noindent
\begin{tabular}{@{}p{59mm}@{\hspace{3.5mm}}p{59mm}@{\hspace{3.5mm}}p{59mm}@{}}
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=59mm, minimum height=50mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCRed} \faWeightHanging\ Sàn Tải Nặng 5 Tấn/m$^2$}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ Móng cọc ép bê tông ly tâm sâu chịu tải trọng tĩnh cực lớn.\newline
      \textbullet\ Bê tông sàn cốt sợi thép kháng nứt dày 250mm.\newline
      \textbullet\ Tăng cứng bề mặt Liquid Hardener chống mài mòn vĩnh cửu.}
    };
  \end{tikzpicture} &
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=59mm, minimum height=50mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCCyan} \faTruckLoading\ Hệ Thống Dock Leveler}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ 24 cụm sàn nâng tự động Dock Leveler nhập khẩu Châu Âu.\newline
      \textbullet\ Cửa trượt trần cuốn nhanh tốc độ cao cách nhiệt.\newline
      \textbullet\ Đệm chắn va đập xe container và bạt che kín khít thời tiết.}
    };
  \end{tikzpicture} &
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=59mm, minimum height=50mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCBlue} \faRulerCombined\ Nhịp Lớn \& Chiều Cao 12.5m}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ Khung thép dầm tổ hợp Tapered tối ưu chiều cao thông thủy.\newline
      \textbullet\ Tối ưu không gian lắp đặt hệ thống kệ tự động cao 6 tầng.\newline
      \textbullet\ Tăng 35\% dung lượng chứa hàng so với thiết kế kho thông thường.}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{2mm}

% TẦNG 3: BĂNG KPI CASE STUDY 6
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
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCRed} 45.000 m$^2$} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCCyan} 5 TẤN/m$^2$} &
      {\fontsize{14}{16}\selectfont\bfseries\color{white} 24 DOCK} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCGold} 12.5 MÉT} \\
      {\fontsize{7.2}{9}\selectfont Sàn Logistics Hoàn Thành} &
      {\fontsize{7.2}{9}\selectfont Tải Trọng Sàn Chịu Lực} &
      {\fontsize{7.2}{9}\selectfont Sàn Nâng Tự Động} &
      {\fontsize{7.2}{9}\selectfont Chiều Cao Thông Thủy}
    \end{tabularx}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_22 = r"""% ============================================================
% TRANG 22: FLAGSHIP CASE -- NHÀ MÁY CÔNG NGHỆ 2M VIỆT NAM
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{DỰ ÁN TIÊU BIỂU • NHÀ MÁY CÔNG NGHỆ 2M}{Trang 22}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Hồ Sơ Dự Án 01: Nhà Máy Sản Xuất Khuôn Mẫu 2M Việt Nam}{High-tech precision facility • Mold \& Parts manufacturing • KCN Yên Mỹ II, Hưng Yên}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);

  % Cụm ảnh theo tiến trình: phối cảnh + ảnh thi công + ảnh hoàn thiện
  \begin{scope}
    \clip[rounded corners=4pt] (0,174) rectangle (70,220);
    \node[inner sep=0pt] at (35,197)
      {\includegraphics[width=70mm,height=46mm]{../../public/project-assets/2m1.jpg}};
    \fill[TTCDeepNavy,opacity=.88] (0,174) rectangle (70,185);
    \node[anchor=west,text=white,font=\fontsize{7}{8}\selectfont\bfseries]
      at (4,179.5) {PHỐI CẢNH THIẾT KẾ};
  \end{scope}
  \begin{scope}
    \clip[rounded corners=2pt] (0,150) rectangle (34,172);
    \node[inner sep=0pt] at (17,161)
      {\includegraphics[width=34mm,height=22mm]{../../public/project-assets/2m3.jpg}};
  \end{scope}
  \begin{scope}
    \clip[rounded corners=2pt] (36,150) rectangle (70,172);
    \node[inner sep=0pt] at (53,161)
      {\includegraphics[width=34mm,height=22mm]{../../public/project-assets/2m5.jpg}};
  \end{scope}
  \fill[TTCDeepNavy,opacity=.82] (0,150) rectangle (34,156);
  \fill[TTCDeepNavy,opacity=.82] (36,150) rectangle (70,156);
  \node[anchor=west,text=white,font=\fontsize{4.8}{5.6}\selectfont\bfseries] at (2,153) {ẢNH THI CÔNG};
  \node[anchor=west,text=white,font=\fontsize{4.8}{5.6}\selectfont\bfseries] at (38,153) {ẢNH HOÀN THIỆN};
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,150) rectangle (70,220);

  % Tóm tắt điều hành
  \fill[TTCLightBlue,rounded corners=4pt] (74,150) rectangle (186,220);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (74,150) rectangle (186,220);
  \node[anchor=north west,text=TTCRed,font=\fontsize{7.5}{9}\selectfont\bfseries]
    at (80,214) {TƯ VẤN THIẾT KẾ \& TỔNG THẦU THI CÔNG};
  \node[anchor=north west,text width=99mm,align=left,text=TTCBlue,
        font=\fontsize{13}{15}\selectfont\bfseries]
    at (80,207) {TỔ HỢP NHÀ MÁY CÔNG NGHỆ 2M};
  \draw[TTCBorder,line width=.55pt] (80,190) -- (180,190);
  \foreach \x in {113.3,146.6}{\draw[TTCBorder,line width=.5pt] (\x,163) -- (\x,186);}
  \node[align=center,text width=29mm] at (96.5,176) {
    {\fontsize{9.5}{11}\selectfont\bfseries\color{TTCRed}CƠ KHÍ CHÍNH XÁC}\\[-.5mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}KHUÔN MẪU \& NHỰA}};
  \node[align=center,text width=29mm] at (130,176) {
    {\fontsize{9.5}{11}\selectfont\bfseries\color{TTCBlue}KẾT CẤU THÉP}\\[-.5mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}XƯỞNG \& VP 3 TẦNG}};
  \node[align=center,text width=29mm] at (163.5,176) {
    {\fontsize{9.5}{11}\selectfont\bfseries\color{TTCBlue}CHỐNG RUNG}\\[-.5mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}CHO DÀN MÁY CNC}};
  \node[anchor=south west,text width=99mm,align=left,text=TTCTextDark,
        font=\fontsize{7.4}{9}\selectfont]
    at (80,153) {\textbf{Chủ đầu tư:} Công ty Cổ phần Công nghệ 2M Việt Nam (2M TECHNOCOM., JSC) \textbullet\ \textbf{Đơn vị thực hiện:} Tân Thành Công JSC -- tư vấn thiết kế, thi công kết cấu thép, sàn chịu lực và hạ tầng kỹ thuật.};

  % Câu chuyện dự án: bài toán -- giải pháp -- kết quả
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (0,143) {CÂU CHUYỆN DỰ ÁN • CHỈ GIỮ BA Ý CHÍNH};

  \fill[white,rounded corners=4pt] (0,79) rectangle (58,137);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,79) rectangle (58,137);
  \fill[TTCRed,rounded corners=2pt] (5,124) rectangle (16,133);
  \node[text=white,font=\fontsize{7}{8}\selectfont\bfseries] at (10.5,128.5) {01};
  \node[anchor=north west,text=TTCBlue,font=\fontsize{9}{10.5}\selectfont\bfseries]
    at (5,120) {BÀI TOÁN};
  \node[anchor=north west,text width=48mm,align=left,text=TTCTextDark,
        font=\fontsize{7.2}{9}\selectfont]
    at (5,110) {Chủ đầu tư cần xây dựng nhà máy sản xuất khuôn mẫu chính xác cao và linh kiện kỹ thuật, đòi hỏi nền sàn xưởng ổn định chống rung cho máy CNC \& máy ép nhựa.};

  \draw[-{Latex[length=2.5mm]},TTCCyan,line width=1pt] (59.5,108) -- (63,108);
  \fill[TTCDeepNavy,rounded corners=4pt] (64,79) rectangle (122,137);
  \node[text=TTCDeepNavy,fill=white,rounded corners=2pt,font=\fontsize{7}{8}\selectfont\bfseries,
        minimum width=11mm,minimum height=9mm] at (74.5,128.5) {02};
  \node[anchor=north west,text=white,font=\fontsize{9}{10.5}\selectfont\bfseries]
    at (69,120) {GIẢI PHÁP TTC};
  \node[anchor=north west,text width=48mm,align=left,text=white,
        font=\fontsize{7.2}{9}\selectfont]
    at (69,110) {Tư vấn thiết kế tối ưu nhịp xưởng thông thoáng; gia cường móng \& sàn bê tông chịu tải chống rung; tích hợp đồng bộ hệ MEP, chiếu sáng và trạm biến áp KCN.};

  \draw[-{Latex[length=2.5mm]},TTCCyan,line width=1pt] (123.5,108) -- (127,108);
  \fill[TTCLightBlue,rounded corners=4pt] (128,79) rectangle (186,137);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (128,79) rectangle (186,137);
  \fill[TTCBlue,rounded corners=2pt] (133,124) rectangle (144,133);
  \node[text=white,font=\fontsize{7}{8}\selectfont\bfseries] at (138.5,128.5) {03};
  \node[anchor=north west,text=TTCBlue,font=\fontsize{9}{10.5}\selectfont\bfseries]
    at (133,120) {KẾT QUẢ};
  \node[anchor=north west,text width=48mm,align=left,text=TTCTextDark,
        font=\fontsize{7.2}{9}\selectfont]
    at (133,110) {Bàn giao công trình hoàn chỉnh đúng tiến độ, đáp ứng chuẩn kỹ thuật khắt khe của ngành sản xuất khuôn mẫu công nghệ cao, đưa vào vận hành hiệu quả.};

  % Băng ghi nhớ
  \fill[white,rounded corners=4pt] (0,20) rectangle (186,70);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,20) rectangle (186,70);
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (7,61) {BA ĐIỂM NGƯỜI ĐỌC CẦN NHỚ};
  \draw[TTCBorder] (62,27) -- (62,58);
  \draw[TTCBorder] (124,27) -- (124,58);
  \node[align=center,text width=52mm] at (31,42) {
    {\fontsize{11}{12}\selectfont\bfseries\color{TTCRed}CHỐNG RUNG ĐỘNG}\\[-.5mm]
    {\fontsize{6.6}{8}\selectfont\color{TTCTextMuted}SÀN GIA CƯỜNG CHO DÀN MÁY CNC}};
  \node[align=center,text width=52mm] at (93,42) {
    {\fontsize{11}{12}\selectfont\bfseries\color{TTCBlue}TỔNG THẦU TRỌN GÓI}\\[-.5mm]
    {\fontsize{6.6}{8}\selectfont\color{TTCTextMuted}TƯ VẤN THIẾT KẾ • KẾT CẤU • MEP}};
  \node[align=center,text width=52mm] at (155,42) {
    {\fontsize{11}{12}\selectfont\bfseries\color{TTCBlue}CHUẨN TIẾN ĐỘ}\\[-.5mm]
    {\fontsize{6.6}{8}\selectfont\color{TTCTextMuted}BÀN GIAO CHÌA KHÓA TRAO TAY}};

  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,14);
  \node[anchor=west,text=white,font=\fontsize{7.4}{9}\selectfont\bfseries]
    at (7,7) {GIÁ TRỊ CỐT LÕI: KHÔNG GIAN CÔNG NGHỆ CHÍNH XÁC • TỔNG THẦU ĐỒNG BỘ TRỌN GÓI};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_23 = r"""% ============================================================
% TRANG 23: ENGINEERING CASE -- NHÀ MÁY SƠN ALO VIỆT NAM
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{GIẢI PHÁP KỸ THUẬT • NHÀ MÁY SƠN ALO}{Trang 23}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Hồ Sơ Dự Án 02: Nhà Máy Sản Xuất Sơn ALO Việt Nam}{Chemical \& Paint manufacturing complex • PCCC ATEX standard • KCN Phú Nghĩa, Hà Nội}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);

  % Phối cảnh và thẻ dữ liệu
  \begin{scope}
    \clip[rounded corners=4pt] (0,148) rectangle (104,220);
    \node[inner sep=0pt] at (52,184)
      {\includegraphics[width=104mm,height=77.5mm]{../../public/project-assets/son_alo_2.jpg}};
    \fill[TTCDeepNavy,opacity=.88] (0,148) rectangle (104,160);
    \node[anchor=west,text=white,font=\fontsize{7}{8}\selectfont\bfseries]
      at (4,154) {PHỐI CẢNH TỔNG THỂ • KCN PHÚ NGHĨA, HÀ NỘI};
  \end{scope}
  % Ảnh thực tế tại mốc khởi công, trình bày như bằng chứng tiến trình
  \begin{scope}
    \clip[rounded corners=2pt] (73,181) rectangle (101,217);
    \node[inner sep=0pt] at (87,199)
      {\includegraphics[width=28mm,height=36mm]{../../public/project-assets/son_alo_1.jpg}};
  \end{scope}
  \draw[white,line width=1.2pt,rounded corners=2pt] (73,181) rectangle (101,217);
  \fill[TTCDeepNavy,opacity=.88] (73,181) rectangle (101,188);
  \node[anchor=west,text=white,font=\fontsize{4.7}{5.5}\selectfont\bfseries]
    at (75,184.5) {ẢNH LỄ KHỞI CÔNG};
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,148) rectangle (104,220);

  \fill[TTCDeepNavy,rounded corners=4pt] (108,148) rectangle (186,220);
  \node[anchor=north west,text=TTCCyan,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (114,214) {TỔNG THẦU EPC};
  \node[anchor=north west,text=white,font=\fontsize{13.5}{15}\selectfont\bfseries]
    at (114,206) {TỔ HỢP SƠN ALO};
  \node[anchor=north west,text=white!75!gray,font=\fontsize{6.5}{8}\selectfont]
    at (114,192) {CỤM 4 PHÂN XƯỞNG \& KHO HÓA CHẤT};
  \draw[white!25!gray] (114,184) -- (180,184);
  \node[anchor=north west,text width=66mm,align=left,text=white,
        font=\fontsize{7.2}{9}\selectfont]
    at (114,179) {\textbf{Chủ đầu tư:} Cty CP Đầu tư ALO Việt Nam\\[1mm]
                  \textbf{Địa điểm:} Lô CN1, KCN Phú Nghĩa, Hà Nội\\[1mm]
                  \textbf{Tiêu chuẩn:} An toàn PCCC \& Kháng hóa chất\\[1mm]
                  \textbf{Tân Thành Công JSC:} Tổng thầu EPC (Thiết kế \& Thi công)};

  % Sơ đồ kỹ thuật: Nhà xưởng hóa chất sơn & kiểm soát môi trường
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (0,140) {SƠ ĐỒ NGUYÊN LÝ • GIẢI PHÁP AN TOÀN CHÁY NỔ \& KHÁNG HÓA CHẤT};
  \fill[TTCLightBlue,rounded corners=4pt] (0,53) rectangle (186,134);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,53) rectangle (186,134);

  % Bản vẽ sơ đồ phân xưởng hóa chất
  % Mái dốc + Cửa trời thông gió
  \draw[TTCBlue,line width=1.4pt] (12,118) -- (68,126) -- (128,118);
  \draw[TTCRed,line width=1pt] (58,126) -- (58,130) -- (78,130) -- (78,126);
  \node[anchor=south,text=TTCRed,font=\fontsize{5.8}{7}\selectfont\bfseries] at (68,130.5) {CỬA TRỜI THOÁT HƠI DUNG MÔI};

  % Khung cột thép
  \draw[TTCBlue,line width=1.4pt] (12,67) -- (12,118);
  \draw[TTCBlue,line width=1.4pt] (128,67) -- (128,118);
  \foreach \x in {41,70,99}{
    \draw[TTCBlue,line width=1pt,dashed] (\x,67) -- (\x,122);
  }

  % Tuyến PCCC Sprinkler & Foam
  \draw[TTCRed,line width=1.2pt,dashed] (15,108) -- (125,108);
  \foreach \x in {25,50,75,100,120}{
    \fill[TTCRed] (\x,108) circle (1.2mm);
    \draw[-{Latex[length=1.5mm]},TTCRed,line width=.6pt] (\x,106) -- (\x,100);
  }
  \node[anchor=west,text=TTCRed,font=\fontsize{6.3}{7.5}\selectfont\bfseries]
    at (16,112) {MẠNG LƯỚI CHỮA CHÁY TỰ ĐỘNG FOAM \& SPRINKLER};

  % Bồn khuấy & Dây chuyền sản xuất
  \fill[white] (22,72) rectangle (40,94);
  \draw[TTCBorder,line width=.7pt] (22,72) rectangle (40,94);
  \node[align=center,text=TTCBlue,font=\fontsize{6}{7.2}\selectfont\bfseries] at (31,83) {BỒN KHUẤY\\PHA SƠN};

  \fill[white] (50,72) rectangle (72,94);
  \draw[TTCBorder,line width=.7pt] (50,72) rectangle (72,94);
  \node[align=center,text=TTCBlue,font=\fontsize{6}{7.2}\selectfont\bfseries] at (61,83) {DÂY CHUYỀN\\ĐÓNG THÙNG};

  \fill[white] (82,72) rectangle (120,94);
  \draw[TTCBorder,line width=.7pt] (82,72) rectangle (120,94);
  \node[align=center,text=TTCBlue,font=\fontsize{6}{7.2}\selectfont\bfseries] at (101,83) {KHO THÀNH PHẨM \&\\NGUYÊN LIỆU HÓA CHẤT};

  % Sàn Epoxy
  \fill[TTCDeepNavy!85!black] (10,64) rectangle (130,68);
  \node[anchor=north west,text=TTCDeepNavy,font=\fontsize{6.2}{7.5}\selectfont\bfseries]
    at (12,63) {SÀN BÊ TÔNG PHỦ EPOXY TỰ PHẲNG KHÁNG HÓA CHẤT};

  % Chú giải bên phải
  \draw[TTCBorder] (136,58) -- (136,128);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (141,126) {3 QUYẾT ĐỊNH KỸ THUẬT};
  \node[anchor=north west,text width=40mm,align=left,text=TTCTextDark,
        font=\fontsize{6.5}{8.1}\selectfont]
    at (141,117) {\textbf{01 • Kháng hóa chất}\newline
                  Sàn bê tông liên hợp phủ Epoxy tự phẳng kháng dung môi hữu cơ.};
  \node[anchor=north west,text width=40mm,align=left,text=TTCTextDark,
        font=\fontsize{6.5}{8.1}\selectfont]
    at (141,94) {\textbf{02 • An toàn PCCC}\newline
                  Tường ngăn cháy lan Rockwool, hệ thống bọt Foam \& báo cháy theo hồ sơ được duyệt.};
  \node[anchor=north west,text width=40mm,align=left,text=TTCTextDark,
        font=\fontsize{6.5}{8.1}\selectfont]
    at (141,71) {\textbf{03 • Thông gió vi khí hậu}\newline
                  Cửa Louver đối lưu khí tự nhiên liên tục giải phóng nồng độ hơi dung môi.};

  % Ba ý ghi nhớ
  \fill[white,rounded corners=3pt] (0,20) rectangle (58,52);
  \draw[TTCBorder,rounded corners=3pt,line width=.7pt] (0,20) rectangle (58,52);
  \node[anchor=north west,text=TTCRed,font=\fontsize{8}{9}\selectfont\bfseries]
    at (5,47) {01 • PCCC CHUYÊN DỤNG};
  \node[anchor=north west,text width=48mm,text=TTCTextDark,font=\fontsize{6.8}{8.4}\selectfont]
    at (5,38) {Hệ thống chữa cháy bọt Foam và giải pháp ngăn cháy lan theo hồ sơ được duyệt.};

  \fill[white,rounded corners=3pt] (64,20) rectangle (122,52);
  \draw[TTCBorder,rounded corners=3pt,line width=.7pt] (64,20) rectangle (122,52);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9}\selectfont\bfseries]
    at (69,47) {02 • SÀN KHÁNG ĂN MÒN};
  \node[anchor=north west,text width=48mm,text=TTCTextDark,font=\fontsize{6.8}{8.4}\selectfont]
    at (69,38) {Bê tông cốt thép phủ Epoxy kháng dung môi và hóa chất theo yêu cầu vận hành.};

  \fill[white,rounded corners=3pt] (128,20) rectangle (186,52);
  \draw[TTCBorder,rounded corners=3pt,line width=.7pt] (128,20) rectangle (186,52);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9}\selectfont\bfseries]
    at (133,47) {03 • TIẾN ĐỘ EPC};
  \node[anchor=north west,text width=48mm,text=TTCTextDark,font=\fontsize{6.8}{8.4}\selectfont]
    at (133,38) {Bàn giao trọn gói đồng bộ cụm xưởng sản xuất, kho và khu điều hành.};

  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,14);
  \node[anchor=west,text=white,font=\fontsize{7.4}{9}\selectfont\bfseries]
    at (7,7) {GIÁ TRỊ CỐT LÕI: AN TOÀN CHÁY NỔ HÓA CHẤT • SÀN BỀN VỮNG KHÁNG ĂN MÒN};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_24 = r"""% ============================================================
% TRANG 24: INJECTION MOLDING CASE -- NHÀ MÁY NHỰA SENDAI VIỆT NAM
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{GIẢI PHÁP KỸ THUẬT • NHÀ MÁY NHỰA SENDAI}{Trang 24}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Hồ Sơ Dự Án 03: Nhà Máy Sản Xuất Nhựa Sendai Việt Nam}{High-tech plastics manufacturing plant • Injection molding facility • KCN Số 3, Hưng Yên}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);

  % Phối cảnh và thẻ dữ liệu
  \begin{scope}
    \clip[rounded corners=4pt] (0,148) rectangle (104,220);
    \node[inner sep=0pt] at (52,184)
      {\includegraphics[width=104mm,height=77.5mm]{../../public/project-assets/sendai_1.jpg}};
    \fill[TTCDeepNavy,opacity=.88] (0,148) rectangle (104,160);
    \node[anchor=west,text=white,font=\fontsize{7}{8}\selectfont\bfseries]
      at (4,154) {PHỐI CẢNH TỔNG THỂ • KCN SỐ 03, HƯNG YÊN};
  \end{scope}
  % Không có ảnh hiện trường trong bộ nguồn: dùng góc phối cảnh thứ hai và ghi nhãn rõ
  \begin{scope}
    \clip[rounded corners=2pt] (68,190) rectangle (101,216);
    \node[inner sep=0pt] at (84.5,203)
      {\includegraphics[width=50mm,height=26mm]{../../public/project-assets/sendai_3.jpg}};
  \end{scope}
  \draw[white,line width=1.2pt,rounded corners=2pt] (68,190) rectangle (101,216);
  \fill[TTCDeepNavy,opacity=.88] (68,190) rectangle (101,197);
  \node[anchor=west,text=white,font=\fontsize{4.6}{5.4}\selectfont\bfseries]
    at (70,193.5) {PHỐI CẢNH MẶT ĐỨNG};
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,148) rectangle (104,220);

  \fill[TTCDeepNavy,rounded corners=4pt] (108,148) rectangle (186,220);
  \node[anchor=north west,text=TTCCyan,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (114,214) {TỔNG THẦU THI CÔNG};
  \node[anchor=north west,text=white,font=\fontsize{13.5}{15}\selectfont\bfseries]
    at (114,206) {TỔ HỢP NHỰA SENDAI};
  \node[anchor=north west,text=white!75!gray,font=\fontsize{6.5}{8}\selectfont]
    at (114,192) {CỤM 2 PHÂN XƯỞNG \& KHỐI VĂN PHÒNG};
  \draw[white!25!gray] (114,184) -- (180,184);
  \node[anchor=north west,text width=66mm,align=left,text=white,
        font=\fontsize{7.2}{9}\selectfont]
    at (114,179) {\textbf{Chủ đầu tư:} Cty CP Nhựa Sendai Việt Nam\\[1mm]
                  \textbf{Địa điểm:} Lô C7, KCN Số 3, Ân Thi, Hưng Yên\\[1mm]
                  \textbf{Quy mô:} 2 Xưởng đúc ép \& Nhà VP 3 tầng\\[1mm]
                  \textbf{Tân Thành Công JSC:} Tổng thầu thi công xây dựng \& MEP};

  % Sơ đồ kỹ thuật: Nhà xưởng đúc ép nhựa & mạng lưới phụ trợ MEP
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (0,140) {SƠ ĐỒ NGUYÊN LÝ • DÂY CHUYỀN ĐÚC ÉP NHỰA \& HỆ THỐNG PHỤ TRỢ MEP};
  \fill[TTCLightBlue,rounded corners=4pt] (0,53) rectangle (186,134);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,53) rectangle (186,134);

  % Bản vẽ sơ đồ phân xưởng đúc ép
  % Mái dốc kết cấu thép PEB
  \draw[TTCBlue,line width=1.4pt] (12,122) -- (68,130) -- (128,122);

  % Khung cột thép
  \draw[TTCBlue,line width=1.4pt] (12,67) -- (12,122);
  \draw[TTCBlue,line width=1.4pt] (128,67) -- (128,122);
  \foreach \x in {41,70,99}{
    \draw[TTCBlue,line width=1pt,dashed] (\x,67) -- (\x,125);
  }

  % Dầm cầu trục chạy trên cao (Overhead Crane)
  \draw[TTCRed,line width=1.4pt] (14,112) -- (126,112);
  \fill[TTCRed] (44,110) rectangle (58,114);
  \node[anchor=south,text=TTCRed,font=\fontsize{5.8}{7}\selectfont\bfseries] at (51,114.8) {CẦU TRỤC PHỤC VỤ THAY KHUÔN};
  \draw[-{Latex[length=1.5mm]},TTCRed,line width=.8pt] (51,110) -- (51,96);

  % Tuyến đường ống Chiller / Nước giải nhiệt & Khí nén
  \draw[TTCCyan,line width=1.2pt,dashed] (15,102) -- (125,102);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.3}{7.5}\selectfont\bfseries]
    at (16,105) {ĐƯỜNG ỐNG CHILLER LÀM MÁT KHUÔN \& KHÍ NÉN TRUNG TÂM};

  % Cụm máy ép phun thủy lực (Injection Molding Machines)
  \foreach \x/\label in {20/{MÁY ÉP 01\\350 TẤN}, 56/{MÁY ÉP 02\\650 TẤN}, 92/{MÁY ÉP 03\\850 TẤN}}{
    \fill[white] (\x,72) rectangle +(28,22);
    \draw[TTCBorder,line width=.7pt] (\x,72) rectangle +(28,22);
    \node[align=center,text=TTCBlue,font=\fontsize{6}{7.2}\selectfont\bfseries] at (\x+14,83) {\label};
    % Mũi tên cấp Chiller
    \draw[-{Latex[length=1.2mm]},TTCCyan,line width=.6pt] (\x+14,102) -- (\x+14,94);
  }

  % Sàn bê tông gia cường chịu tải máy ép
  \fill[TTCDeepNavy!85!black] (10,64) rectangle (130,68);
  \node[anchor=north west,text=TTCDeepNavy,font=\fontsize{6.2}{7.5}\selectfont\bfseries]
    at (12,63) {SÀN BÊ TÔNG GIA CƯỜNG CHỐNG RUNG ĐỘNG CHU KỲ ÉP};

  % Chú giải bên phải
  \draw[TTCBorder] (136,58) -- (136,128);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (141,126) {3 QUYẾT ĐỊNH KỸ THUẬT};
  \node[anchor=north west,text width=40mm,align=left,text=TTCTextDark,
        font=\fontsize{6.5}{8.1}\selectfont]
    at (141,117) {\textbf{01 • Sàn chịu tải máy ép}\newline
                  Bê tông cốt thép mác cao chống lún lệch và triệt tiêu rung động máy ép.};
  \node[anchor=north west,text width=40mm,align=left,text=TTCTextDark,
        font=\fontsize{6.5}{8.1}\selectfont]
    at (141,94) {\textbf{02 • Hạ tầng Chiller}\newline
                  Mạng lưới nước làm mát tuần hoàn khép kín cấp trực tiếp đến từng khuôn.};
  \node[anchor=north west,text width=40mm,align=left,text=TTCTextDark,
        font=\fontsize{6.5}{8.1}\selectfont]
    at (141,71) {\textbf{03 • Tổ hợp 2 xưởng \& VP}\newline
                  Quy hoạch giao thông nội bộ kết nối nhịp nhàng giữa xưởng và điều hành.};

  % Ba ý ghi nhớ
  \fill[white,rounded corners=3pt] (0,20) rectangle (58,52);
  \draw[TTCBorder,rounded corners=3pt,line width=.7pt] (0,20) rectangle (58,52);
  \node[anchor=north west,text=TTCRed,font=\fontsize{8}{9}\selectfont\bfseries]
    at (5,47) {01 • ĐÚC ÉP KỸ THUẬT};
  \node[anchor=north west,text width=48mm,text=TTCTextDark,font=\fontsize{6.8}{8.4}\selectfont]
    at (5,38) {Nhà xưởng khẩu độ lớn tích hợp cầu trục thay khuôn theo dữ liệu thiết bị.};

  \fill[white,rounded corners=3pt] (64,20) rectangle (122,52);
  \draw[TTCBorder,rounded corners=3pt,line width=.7pt] (64,20) rectangle (122,52);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9}\selectfont\bfseries]
    at (69,47) {02 • MEP LÀM MÁT};
  \node[anchor=north west,text width=48mm,text=TTCTextDark,font=\fontsize{6.8}{8.4}\selectfont]
    at (69,38) {Hệ thống Chiller giải nhiệt, khí nén trung tâm và trạm điện đồng bộ.};

  \fill[white,rounded corners=3pt] (128,20) rectangle (186,52);
  \draw[TTCBorder,rounded corners=3pt,line width=.7pt] (128,20) rectangle (186,52);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9}\selectfont\bfseries]
    at (133,47) {03 • TIẾN ĐỘ TỔNG THẦU};
  \node[anchor=north west,text width=48mm,text=TTCTextDark,font=\fontsize{6.8}{8.4}\selectfont]
    at (133,38) {Thi công trọn gói 2 xưởng sản xuất, kho và khối nhà văn phòng 3 tầng.};

  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,14);
  \node[anchor=west,text=white,font=\fontsize{7.4}{9}\selectfont\bfseries]
    at (7,7) {GIÁ TRỊ CỐT LÕI: HẠ TẦNG SẢN XUẤT NHỰA KỸ THUẬT • HỆ THỐNG PHỤ TRỢ MEP ĐỒNG BỘ};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_25 = r"""% ============================================================
% TRANG 25: CASE STUDY 04 -- NHÀ MÁY MAY LÀO CAI
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{GIẢI PHÁP KỸ THUẬT • NHÀ MÁY MAY LÀO CAI}{Trang 25}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Hồ Sơ Dự Án 04: Tổ Hợp Nhà Máy May Lào Cai}{Multi-storey garment manufacturing complex • Negative pressure cooling • Phố Mới, TP. Lào Cai}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);

  % Phối cảnh dự án (trái)
  \begin{scope}
    \clip[rounded corners=4pt] (0,148) rectangle (104,220);
    \node[inner sep=0pt] at (52,175)
      {\includegraphics[width=128mm]{../../public/project-assets/laocai_4.jpg}};
    \fill[TTCDeepNavy,opacity=.92] (0,148) rectangle (104,158);
    \node[anchor=west,text=white,font=\fontsize{6.8}{8}\selectfont\bfseries]
      at (4,153) {PHỐI CẢNH TỔNG THỂ • ĐƯỜNG PHỐ MỚI, TP. LÀO CAI};
  \end{scope}
  % Góc quy hoạch bổ sung để làm rõ tổ chức ba khối xưởng
  \begin{scope}
    \clip[rounded corners=2pt] (70,184) rectangle (101,216);
    \node[inner sep=0pt] at (85.5,200)
      {\includegraphics[width=42mm,height=32mm]{../../public/project-assets/laocai_3.jpg}};
  \end{scope}
  \draw[white,line width=1.2pt,rounded corners=2pt] (70,184) rectangle (101,216);
  \fill[TTCDeepNavy,opacity=.88] (70,184) rectangle (101,191);
  \node[anchor=west,text=white,font=\fontsize{4.6}{5.4}\selectfont\bfseries]
    at (72,187.5) {MẶT BẰNG QUY HOẠCH};
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,148) rectangle (104,220);

  % Thẻ dữ liệu dự án (phải)
  \fill[TTCDeepNavy,rounded corners=4pt] (108,148) rectangle (186,220);
  \node[anchor=north west,text=TTCCyan,font=\fontsize{6.8}{8}\selectfont\bfseries]
    at (114,214) {TƯ VẤN THIẾT KẾ \& THI CÔNG};
  \node[anchor=north west,text=white,font=\fontsize{11.5}{13}\selectfont\bfseries]
    at (114,204) {NHÀ MÁY MAY LÀO CAI};
  \node[anchor=north west,text=white!75!gray,font=\fontsize{6}{7.2}\selectfont]
    at (114,192) {TỔ HỢP 3 KHỐI NHÀ XƯỞNG 5 TẦNG};
  \draw[white!25!gray] (114,186) -- (180,186);
  \node[anchor=north west,text width=66mm,align=left,text=white,
        font=\fontsize{6.5}{8.5}\selectfont]
    at (114,181) {\textbf{Chủ đầu tư:} Công ty May Lào Cai\\[1mm]
                  \textbf{Địa điểm:} Đ. Phố Mới, TP. Lào Cai\\[1mm]
                  \textbf{Quy mô:} 3 Khối xưởng 5 tầng • Khu xuất nhập\\[1mm]
                  \textbf{Tân Thành Công JSC:} Thiết kế kiến trúc \& Tổng thầu thi công};

  % Khung sơ đồ kỹ thuật
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (0,141) {SƠ ĐỒ NGUYÊN LÝ • XƯỞNG MAY CAO TẦNG \& VI KHÍ HẬU ÁP SUẤT ÂM};
  \fill[TTCLightBlue,rounded corners=4pt] (0,53) rectangle (186,134);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,53) rectangle (186,134);

  % Vùng phân tích kỹ thuật bên phải sơ đồ
  \fill[white,rounded corners=3pt] (130,58) rectangle (181,129);
  \draw[TTCBorder,rounded corners=3pt,line width=.6pt] (130,58) rectangle (181,129);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (134,125) {3 QUYẾT ĐỊNH KỸ THUẬT};

  \node[anchor=north west,text width=44mm,font=\fontsize{5.8}{7.2}\selectfont]
    at (134,117) {\textbf{01 • Sàn nhiều tầng chịu tải}\\[.3mm]
    \color{TTCTextDark}Hệ dầm sàn liên hợp triệt tiêu rung động cộng hưởng từ hàng ngàn máy may.};

  \node[anchor=north west,text width=44mm,font=\fontsize{5.8}{7.2}\selectfont]
    at (134,94) {\textbf{02 • Vi khí hậu áp suất âm}\\[.3mm]
    \color{TTCTextDark}Cooling Pad \& quạt hút đối lưu, lọc sạch bụi bông và cấp khí tươi liên tục.};

  \node[anchor=north west,text width=44mm,font=\fontsize{5.8}{7.2}\selectfont]
    at (134,71) {\textbf{03 • Cụm 3 khối xưởng}\\[.3mm]
    \color{TTCTextDark}Quy hoạch luồng xuất nhập hàng container và thang nâng theo yêu cầu vận hành.};

  % Bản vẽ mặt cắt nhà xưởng may nhiều tầng (Multi-storey Garment Factory Cross-section)
  % Khung kết cấu bao che
  \draw[TTCBlue,line width=1.4pt] (10,65) -- (10,123) -- (67,130) -- (124,123) -- (124,65);

  % Cột chịu lực giữa (mờ để không rối text)
  \draw[TTCBlue!40,line width=.8pt,dashed] (48,65) -- (48,127);
  \draw[TTCBlue!40,line width=.8pt,dashed] (86,65) -- (86,127);

  % Trục thang nâng hàng tải nặng (Freight Elevator Shaft) bên trái
  \fill[TTCDeepNavy!15] (10,65) rectangle (24,123);
  \draw[TTCBlue,line width=1.1pt] (24,65) -- (24,123);
  \node[rotate=90,align=center,text=TTCDeepNavy,font=\fontsize{5.2}{6.2}\selectfont\bfseries] at (17,94) {THANG HÀNG 3--5 TẤN};

  % Các tầng sàn dầm thép liên hợp (Floor slabs)
  \draw[TTCBlue,line width=1.2pt] (24,78) -- (124,78);
  \draw[TTCBlue,line width=1.2pt] (24,91) -- (124,91);
  \draw[TTCBlue,line width=1.2pt] (24,104) -- (124,104);
  \draw[TTCBlue,line width=1.2pt] (24,117) -- (124,117);

  % Text nhãn từng tầng
  \node[anchor=west,text=TTCBlue,font=\fontsize{5.2}{6.2}\selectfont\bfseries] at (26,74) {TẦNG 1: KHO NGUYÊN PHỤ LIỆU \& XUẤT NHẬP THÀNH PHẨM};
  \node[anchor=west,text=TTCBlue,font=\fontsize{5.2}{6.2}\selectfont\bfseries] at (26,87) {TẦNG 2: PHÂN XƯỞNG CẮT \& MAY MẪU};
  \node[anchor=west,text=TTCBlue,font=\fontsize{5.2}{6.2}\selectfont\bfseries] at (26,100) {TẦNG 3: DÂY CHUYỀN MAY XUẤT KHẨU 01};
  \node[anchor=west,text=TTCBlue,font=\fontsize{5.2}{6.2}\selectfont\bfseries] at (26,113) {TẦNG 4: DÂY CHUYỀN MAY XUẤT KHẨU 02};
  \node[anchor=west,text=TTCBlue,font=\fontsize{5.2}{6.2}\selectfont\bfseries] at (26,122.5) {TẦNG 5: HOÀN THIỆN, ỦI \& ĐÓNG GÓI};

  % Biểu tượng máy may trên các tầng 2, 3, 4
  \foreach \y in {78, 91, 104}{
    \foreach \x in {34, 58, 74, 98, 114}{
      \fill[white] (\x-3.5,\y+1.5) rectangle +(6.5,4);
      \draw[TTCBorder,line width=.4pt] (\x-3.5,\y+1.5) rectangle +(6.5,4);
      \draw[TTCRed,line width=.5pt] (\x-1.5,\y+2.5) -- (\x+1.5,\y+2.5);
    }
  }

  % Tuyến làm mát áp suất âm & Hút bụi vải (Cooling & Exhaust airflow)
  \foreach \y in {70, 82.5, 95.5, 108.5}{
    \draw[TTCCyan,line width=.8pt,dash pattern=on 3pt off 2pt] (26,\y) -- (122,\y);
    \draw[-{Latex[length=1.1mm]},TTCCyan,line width=.7pt] (62,\y) -- (70,\y);
    \draw[-{Latex[length=1.1mm]},TTCCyan,line width=.7pt] (98,\y) -- (106,\y);
  }

  % Móng & Sàn liên hợp đáy
  \fill[TTCDeepNavy] (9,58) rectangle (125,65);
  \node[anchor=center,text=white,font=\fontsize{5.4}{6.5}\selectfont\bfseries]
    at (67,61.5) {HỆ DẦM SÀN LIÊN HỢP CHỊU TẢI ĐỘNG DÀN MÁY MAY};

  % 3 Thẻ ghi nhớ dưới
  \fill[white,rounded corners=3pt] (0,20) rectangle (58,52);
  \draw[TTCBorder,rounded corners=3pt,line width=.7pt] (0,20) rectangle (58,52);
  \node[anchor=north west,text=TTCRed,font=\fontsize{8}{9}\selectfont\bfseries]
    at (5,47) {01 • XƯỞNG MAY CAO TẦNG};
  \node[anchor=north west,text width=48mm,text=TTCTextDark,font=\fontsize{6.8}{8.4}\selectfont]
    at (5,38) {Tổ hợp 3 khối xưởng 5 tầng tối ưu mật độ sử dụng đất và bố trí dây chuyền.};

  \fill[white,rounded corners=3pt] (64,20) rectangle (122,52);
  \draw[TTCBorder,rounded corners=3pt,line width=.7pt] (64,20) rectangle (122,52);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9}\selectfont\bfseries]
    at (69,47) {02 • VI KHÍ HẬU DỆT MAY};
  \node[anchor=north west,text width=48mm,text=TTCTextDark,font=\fontsize{6.8}{8.4}\selectfont]
    at (69,38) {Làm mát áp suất âm, lọc bụi bông và cấp khí tươi đạt chuẩn kiểm toán xuất khẩu.};

  \fill[white,rounded corners=3pt] (128,20) rectangle (186,52);
  \draw[TTCBorder,rounded corners=3pt,line width=.7pt] (128,20) rectangle (186,52);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9}\selectfont\bfseries]
    at (133,47) {03 • TỔNG THẦU D\&B};
  \node[anchor=north west,text width=48mm,text=TTCTextDark,font=\fontsize{6.8}{8.4}\selectfont]
    at (133,38) {Tư vấn thiết kế kiến trúc, kết cấu liên hợp và thi công hoàn thiện trọn gói.};

  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,14);
  \node[anchor=west,text=white,font=\fontsize{7.4}{9}\selectfont\bfseries]
    at (7,7) {GIÁ TRỊ CỐT LÕI: GIẢI PHÁP NHÀ XƯỞNG CAO TẦNG • MÔI TRƯỜNG LÀM VIỆC CHUẨN XUẤT KHẨU};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_26 = r"""% ============================================================
% TRANG 26: CASE STUDY 05 -- NHÀ MÁY NHỰA DHL
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{GIẢI PHÁP KỸ THUẬT • TẬP ĐOÀN NHỰA DHL}{Trang 26}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Hồ Sơ Dự Án 05: Nhà Máy Sản Xuất Nhựa DHL}{High-grade plastic packaging plant • PE/PP film extrusion • KCN Thái Hà, Hà Nam}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);

  % Ảnh hoàn thiện làm hình chính; phối cảnh thiết kế làm hình đối chiếu
  \begin{scope}
    \clip[rounded corners=4pt] (0,148) rectangle (104,220);
    \node[inner sep=0pt] at (52,184)
      {\includegraphics[width=104mm]{../../public/project-assets/dhl_2.jpg}};
    \fill[TTCDeepNavy,opacity=.92] (0,148) rectangle (104,158);
    \node[anchor=west,text=white,font=\fontsize{6.8}{8}\selectfont\bfseries]
      at (4,153) {ẢNH THỰC TẾ HOÀN THIỆN • KCN THÁI HÀ, HÀ NAM};
  \end{scope}
  \begin{scope}
    \clip[rounded corners=2pt] (71,184) rectangle (101,216);
    \node[inner sep=0pt] at (86,200)
      {\includegraphics[width=42mm,height=32mm]{../../public/project-assets/dhl_4.jpg}};
  \end{scope}
  \draw[white,line width=1.2pt,rounded corners=2pt] (71,184) rectangle (101,216);
  \fill[TTCDeepNavy,opacity=.88] (71,184) rectangle (101,191);
  \node[anchor=west,text=white,font=\fontsize{4.6}{5.4}\selectfont\bfseries]
    at (73,187.5) {PHỐI CẢNH THIẾT KẾ};
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,148) rectangle (104,220);

  % Thẻ dữ liệu dự án (phải)
  \fill[TTCDeepNavy,rounded corners=4pt] (108,148) rectangle (186,220);
  \node[anchor=north west,text=TTCCyan,font=\fontsize{6.8}{8}\selectfont\bfseries]
    at (114,214) {TỔNG THẦU THI CÔNG};
  \node[anchor=north west,text=white,font=\fontsize{11.5}{13}\selectfont\bfseries]
    at (114,204) {NHÀ MÁY NHỰA DHL};
  \node[anchor=north west,text=white!75!gray,font=\fontsize{6}{7.2}\selectfont]
    at (114,192) {TỔ HỢP XƯỞNG SẢN XUẤT \& KHỐI VĂN PHÒNG};
  \draw[white!25!gray] (114,186) -- (180,186);
  \node[anchor=north west,text width=66mm,align=left,text=white,
        font=\fontsize{6.5}{8.5}\selectfont]
    at (114,181) {\textbf{Chủ đầu tư:} Cty CP Tập đoàn Nhựa DHL\\[1mm]
                  \textbf{Địa điểm:} Lô CN02, KCN Thái Hà, Hà Nam\\[1mm]
                  \textbf{Quy mô:} Tổ hợp xưởng màng PE/PP \& VP 3 tầng\\[1mm]
                  \textbf{Tân Thành Công JSC:} Tổng thầu thi công PEB \& Cơ điện MEP};

  % Khung sơ đồ kỹ thuật
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (0,141) {SƠ ĐỒ NGUYÊN LÝ • DÂY CHUYỀN ĐÙN THỔI MÀNG NHỰA \& HỆ PHỤ TRỢ MEP};
  \fill[TTCLightBlue,rounded corners=4pt] (0,53) rectangle (186,134);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,53) rectangle (186,134);

  % Vùng phân tích kỹ thuật bên phải sơ đồ
  \fill[white,rounded corners=3pt] (130,58) rectangle (181,129);
  \draw[TTCBorder,rounded corners=3pt,line width=.6pt] (130,58) rectangle (181,129);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (134,125) {3 QUYẾT ĐỊNH KỸ THUẬT};

  \node[anchor=north west,text width=44mm,font=\fontsize{5.8}{7.2}\selectfont]
    at (134,117) {\textbf{01 • Vượt nhịp thông tầng}\\[.3mm]
    \color{TTCTextDark}Khung nhà thép tiền chế khẩu độ lớn tích hợp khoang thông tầng cho tháp đùn màng.};

  \node[anchor=north west,text width=44mm,font=\fontsize{5.8}{7.2}\selectfont]
    at (134,94) {\textbf{02 • Hạ tầng Chiller đùn ép}\\[.3mm]
    \color{TTCTextDark}Hệ thống nước lạnh tuần hoàn giữ nhiệt độ ổn định định hình màng mỏng.};

  \node[anchor=north west,text width=44mm,font=\fontsize{5.8}{7.2}\selectfont]
    at (134,71) {\textbf{03 • Sàn Hardener chịu tải}\\[.3mm]
    \color{TTCTextDark}Bề mặt bê tông mài bóng tăng cứng, chống bụi và được thiết kế theo tải xe nâng.};

  % Bản vẽ sơ đồ phân xưởng đùn màng & in bao bì
  % Khung kết cấu nhà xưởng có tháp cao thông tầng
  \draw[TTCBlue,line width=1.4pt] (10,65) -- (10,128) -- (48,128) -- (48,118) -- (124,118) -- (124,65);
  \draw[TTCBlue!40,line width=.8pt,dashed] (86,65) -- (86,118);

  % Tháp đùn thổi màng (Blown Film Tower)
  \fill[white] (15,70) rectangle (43,124);
  \draw[TTCBlue,line width=.9pt] (15,70) rectangle (43,124);
  \draw[TTCRed,line width=1pt] (29,74) -- (29,114);
  \draw[TTCCyan,line width=.8pt] (24,74) .. controls (19,94) and (21,110) .. (29,114);
  \draw[TTCCyan,line width=.8pt] (34,74) .. controls (39,94) and (37,110) .. (29,114);
  \fill[TTCBlue] (26,114) rectangle (32,118);
  \node[align=center,text=TTCBlue,font=\fontsize{5.2}{6.2}\selectfont\bfseries]
    at (29,84) {THÁP ĐÙN THỔI\\MÀNG ĐA LỚP\\KHOANG THÔNG TẦNG};

  % Cụm máy in ấn ống đồng & cuộn màng
  \fill[white] (52,70) rectangle (82,94);
  \draw[TTCBorder,line width=.7pt] (52,70) rectangle (82,94);
  \fill[TTCLightBlue] (55,73) rectangle (79,83);
  \draw[TTCBlue,line width=.6pt] (55,73) rectangle (79,83);
  \node[align=center,text=TTCBlue,font=\fontsize{5.2}{6.2}\selectfont\bfseries]
    at (67,88) {MÁY IN ỐNG ĐỒNG \&\\CUỘN MÀNG TỰ ĐỘNG};
  \node[align=center,text=TTCTextDark,font=\fontsize{4.8}{5.8}\selectfont]
    at (67,78) {IN ĐA MÀU TỐC ĐỘ CAO};

  % Cụm lưu trữ nguyên liệu & kho thành phẩm
  \fill[white] (88,70) rectangle (120,94);
  \draw[TTCBorder,line width=.7pt] (88,70) rectangle (120,94);
  \node[align=center,text=TTCBlue,font=\fontsize{5.2}{6.2}\selectfont\bfseries]
    at (104,88) {KHO THÀNH PHẨM \&\\HẠT NHỰA NGUYÊN SINH};
  \foreach \x in {93, 104, 115}{
    \fill[TTCDeepNavy!20] (\x-3,73) rectangle +(6,8);
    \draw[TTCDeepNavy,line width=.4pt] (\x-3,73) rectangle +(6,8);
  }

  % Tuyến đường ống Chiller tuần hoàn & Khí nén
  \draw[TTCCyan,line width=1.1pt,dashed] (12,104) -- (122,104);
  \node[anchor=west,text=TTCCyan,font=\fontsize{5.8}{7}\selectfont\bfseries]
    at (50,107.5) {ĐƯỜNG ỐNG CHILLER LÀM MÁT TRỤC LÔ \& KHÍ NÉN TRUNG TÂM};
  \draw[-{Latex[length=1.2mm]},TTCCyan,line width=.7pt] (29,104) -- (29,95);
  \draw[-{Latex[length=1.2mm]},TTCCyan,line width=.7pt] (67,104) -- (67,96);

  % Móng & Sàn bê tông Hardener
  \fill[TTCDeepNavy] (9,58) rectangle (125,65);
  \node[anchor=center,text=white,font=\fontsize{5.4}{6.5}\selectfont\bfseries]
    at (67,61.5) {SÀN BÊ TÔNG MÀI BÓNG TĂNG CỨNG HARDENER CHỐNG BỤI};

  % 3 Thẻ ghi nhớ dưới
  \fill[white,rounded corners=3pt] (0,20) rectangle (58,52);
  \draw[TTCBorder,rounded corners=3pt,line width=.7pt] (0,20) rectangle (58,52);
  \node[anchor=north west,text=TTCRed,font=\fontsize{8}{9}\selectfont\bfseries]
    at (5,47) {01 • TỔ HỢP XƯỞNG \& VP};
  \node[anchor=north west,text width=48mm,text=TTCTextDark,font=\fontsize{6.8}{8.4}\selectfont]
    at (5,38) {Khối văn phòng 3 tầng mặt kính hiện đại kết hợp phân xưởng đùn thổi màng quy mô lớn.};

  \fill[white,rounded corners=3pt] (64,20) rectangle (122,52);
  \draw[TTCBorder,rounded corners=3pt,line width=.7pt] (64,20) rectangle (122,52);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9}\selectfont\bfseries]
    at (69,47) {02 • MEP CÔNG SUẤT CAO};
  \node[anchor=north west,text width=48mm,text=TTCTextDark,font=\fontsize{6.8}{8.4}\selectfont]
    at (69,38) {Tích hợp trạm biến áp, tháp Chiller làm mát trục đùn và khí nén trung tâm đồng bộ.};

  \fill[white,rounded corners=3pt] (128,20) rectangle (186,52);
  \draw[TTCBorder,rounded corners=3pt,line width=.7pt] (128,20) rectangle (186,52);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9}\selectfont\bfseries]
    at (133,47) {03 • BÀN GIAO THỰC TẾ};
  \node[anchor=north west,text width=48mm,text=TTCTextDark,font=\fontsize{6.8}{8.4}\selectfont]
    at (133,38) {Thi công chuẩn xác, nghiệm thu an toàn PCCC và đưa vào vận hành thương mại 2025.};

  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,14);
  \node[anchor=west,text=white,font=\fontsize{7.4}{9}\selectfont\bfseries]
    at (7,7) {GIÁ TRỊ CỐT LÕI: HẠ TẦNG SẢN XUẤT BAO BÌ NHỰA CAO CẤP • CHẤT LƯỢNG BÀN GIAO THỰC TẾ};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_27 = r"""% ============================================================
% TRANG 27: CASE STUDY 06 -- NHÀ MÁY NHÔM QUANG THỊNH
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{GIẢI PHÁP KỸ THUẬT • NHÔM QUANG THỊNH}{Trang 27}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Hồ Sơ Dự Án 06: Nhà Máy Sản Xuất Nhôm Quang Thịnh}{High-grade aluminum profiles plant • Heavy extrusion lines • Thuận Thành, Bắc Ninh}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);

  % Ảnh phối cảnh dự án (trái)
  \begin{scope}
    \clip[rounded corners=4pt] (0,148) rectangle (104,220);
    \node[inner sep=0pt] at (52,198)
      {\includegraphics[width=185mm]{../../public/project-assets/quangthinh_1.jpg}};
    \fill[TTCDeepNavy,opacity=.92] (0,148) rectangle (104,158);
    \node[anchor=west,text=white,font=\fontsize{6.8}{8}\selectfont\bfseries]
      at (4,153) {PHỐI CẢNH DỰ ÁN • THUẬN THÀNH, BẮC NINH};
  \end{scope}
  % Ảnh hiện trường bổ sung giúp phân biệt phối cảnh với tiến độ thi công thực tế
  \begin{scope}
    \clip[rounded corners=2pt] (70,181) rectangle (101,216);
    \node[inner sep=0pt] at (85.5,198.5)
      {\includegraphics[width=46mm,height=35mm]{../../public/project-assets/quangthinh_3.jpg}};
  \end{scope}
  \draw[white,line width=1.2pt,rounded corners=2pt] (70,181) rectangle (101,216);
  \fill[TTCDeepNavy,opacity=.88] (70,181) rectangle (101,188);
  \node[anchor=west,text=white,font=\fontsize{4.6}{5.4}\selectfont\bfseries]
    at (72,184.5) {ẢNH THI CÔNG THỰC TẾ};
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,148) rectangle (104,220);

  % Thẻ dữ liệu dự án (phải)
  \fill[TTCDeepNavy,rounded corners=4pt] (108,148) rectangle (186,220);
  \node[anchor=north west,text=TTCCyan,font=\fontsize{6.8}{8}\selectfont\bfseries]
    at (114,214) {TỔNG THẦU THI CÔNG};
  \node[anchor=north west,text=white,font=\fontsize{11.2}{13}\selectfont\bfseries]
    at (114,204) {NHÀ MÁY NHÔM QUANG THỊNH};
  \node[anchor=north west,text=white!75!gray,font=\fontsize{6}{7.2}\selectfont]
    at (114,192) {TỔ HỢP XƯỞNG ĐÙN ÉP \& SƠN TĨNH ĐIỆN};
  \draw[white!25!gray] (114,186) -- (180,186);
  \node[anchor=north west,text width=66mm,align=left,text=white,
        font=\fontsize{6.5}{8.5}\selectfont]
    at (114,181) {\textbf{Chủ đầu tư:} Cty CP Nhôm Quang Thịnh\\[1mm]
                  \textbf{Địa điểm:} Thuận Thành, Bắc Ninh\\[1mm]
                  \textbf{Quy mô:} Tổ hợp xưởng đùn ép \& Nhà VP điều hành\\[1mm]
                  \textbf{Tân Thành Công JSC:} Tổng thầu thi công PEB \& Cơ điện MEP};

  % Khung sơ đồ kỹ thuật
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (0,141) {SƠ ĐỒ NGUYÊN LÝ • DÂY CHUYỀN ĐÙN ÉP NHÔM ĐỊNH HÌNH \& XỬ LÝ BỀ MẶT};
  \fill[TTCLightBlue,rounded corners=4pt] (0,53) rectangle (186,134);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,53) rectangle (186,134);

  % Vùng phân tích kỹ thuật bên phải sơ đồ
  \fill[white,rounded corners=3pt] (130,58) rectangle (181,129);
  \draw[TTCBorder,rounded corners=3pt,line width=.6pt] (130,58) rectangle (181,129);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (134,125) {3 QUYẾT ĐỊNH KỸ THUẬT};

  \node[anchor=north west,text width=44mm,font=\fontsize{5.8}{7.2}\selectfont]
    at (134,117) {\textbf{01 • Móng máy đùn ép tải nặng}\\[.3mm]
    \color{TTCTextDark}Bệ móng bê tông cốt thép khối lớn được thiết kế theo tải động của máy ép thủy lực.};

  \node[anchor=north west,text width=44mm,font=\fontsize{5.8}{7.2}\selectfont]
    at (134,94) {\textbf{02 • Dây chuyền sơn tĩnh điện}\\[.3mm]
    \color{TTCTextDark}Buồng phun sơn khép kín, lò sấy nhiệt độ cao và trạm xử lý nước thải xi mạ Anode.};

  \node[anchor=north west,text width=44mm,font=\fontsize{5.8}{7.2}\selectfont]
    at (134,71) {\textbf{03 • Sàn Hardener chịu mài mòn}\\[.3mm]
    \color{TTCTextDark}Bề mặt bê tông mài bóng tăng cứng, chống bụi và được thiết kế theo tải xe nâng phôi.};

  % Bản vẽ sơ đồ phân xưởng đùn ép nhôm định hình
  % Khung kết cấu nhà xưởng PEB
  \draw[TTCBlue,line width=1.4pt] (10,65) -- (10,126) -- (67,126) -- (124,126) -- (124,65);
  \draw[TTCBlue!40,line width=.8pt,dashed] (48,65) -- (48,126);
  \draw[TTCBlue!40,line width=.8pt,dashed] (86,65) -- (86,126);

  % Dầm cầu trục phục vụ dây chuyền
  \draw[TTCBlue,line width=1pt] (10,113) -- (124,113);
  \fill[TTCBlue] (26,111) rectangle (36,115);
  \fill[TTCBlue] (70,111) rectangle (80,115);
  \node[anchor=west,text=TTCBlue,font=\fontsize{5.2}{6.2}\selectfont\bfseries]
    at (14,118) {DẦM CẦU TRỤC PHỤC VỤ NÂNG HẠ PHÔI NHÔM \& THAY KHUÔN ĐÙN};

  % Zone 1: Lò nung phôi nhôm & Máy đùn ép thủy lực
  \fill[white] (13,70) rectangle (46,96);
  \draw[TTCBorder,line width=.7pt] (13,70) rectangle (46,96);
  \fill[TTCRed!15] (16,73) rectangle (43,83);
  \draw[TTCRed,line width=.6pt] (16,73) rectangle (43,83);
  \node[align=center,text=TTCBlue,font=\fontsize{5.1}{6.1}\selectfont\bfseries]
    at (29.5,90) {LÒ NUNG PHÔI NHÔM \&\\MÁY ĐÙN ÉP THỦY LỰC};
  \node[align=center,text=TTCRed,font=\fontsize{4.8}{5.8}\selectfont\bfseries]
    at (29.5,78) {ÉP ĐÙN THEO DÂY CHUYỀN};

  % Zone 2: Dàn làm nguội & Bàn kéo dài thanh nhôm
  \fill[white] (49,70) rectangle (84,96);
  \draw[TTCBorder,line width=.7pt] (49,70) rectangle (84,96);
  \fill[TTCLightBlue] (52,73) rectangle (81,83);
  \draw[TTCBlue,line width=.6pt] (52,73) rectangle (81,83);
  \node[align=center,text=TTCBlue,font=\fontsize{5.1}{6.1}\selectfont\bfseries]
    at (66.5,90) {BÀN KÉO GIÃN LÀM NGUỘI \&\\LÒ Ủ NHIỆT ĐỒNG HÓA};
  \node[align=center,text=TTCTextDark,font=\fontsize{4.8}{5.8}\selectfont]
    at (66.5,78) {ĐỊNH HÌNH PROFILE DÀI};

  % Zone 3: Dây chuyền sơn tĩnh điện & Đóng gói
  \fill[white] (87,70) rectangle (121,96);
  \draw[TTCBorder,line width=.7pt] (87,70) rectangle (121,96);
  \fill[TTCDeepNavy!15] (90,73) rectangle (118,83);
  \draw[TTCDeepNavy,line width=.6pt] (90,73) rectangle (118,83);
  \node[align=center,text=TTCBlue,font=\fontsize{5.1}{6.1}\selectfont\bfseries]
    at (104,90) {DÂY CHUYỀN SƠN TĨNH ĐIỆN\\\& ĐÓNG GÓI THÀNH PHẨM};
  \node[align=center,text=TTCTextDark,font=\fontsize{4.8}{5.8}\selectfont]
    at (104,78) {XI MẠ ANODE • SƠN TREO};

  % Mũi tên chuyển bước dây chuyền
  \draw[-{Latex[length=1.4mm]},TTCBlue,line width=1pt] (46,83) -- (49,83);
  \draw[-{Latex[length=1.4mm]},TTCBlue,line width=1pt] (84,83) -- (87,83);

  % Tuyến đường ống Chiller giải nhiệt khuôn đùn ép & Khí nén
  \draw[TTCCyan,line width=1.1pt,dashed] (12,103) -- (122,103);
  \node[anchor=west,text=TTCCyan,font=\fontsize{5.8}{7}\selectfont\bfseries]
    at (36,106.5) {HỆ NƯỚC LÀM MÁT KHUÔN ĐÙN ÉP \& KHÍ NÉN TRUNG TÂM};
  \draw[-{Latex[length=1.2mm]},TTCCyan,line width=.7pt] (29.5,103) -- (29.5,97);
  \draw[-{Latex[length=1.2mm]},TTCCyan,line width=.7pt] (66.5,103) -- (66.5,97);

  % Móng & Sàn bê tông Hardener
  \fill[TTCDeepNavy] (9,58) rectangle (125,65);
  \node[anchor=center,text=white,font=\fontsize{5.4}{6.5}\selectfont\bfseries]
    at (67,61.5) {SÀN BÊ TÔNG MÀI BÓNG TĂNG CỨNG HARDENER CHỊU MÀI MÒN};

  % 3 Thẻ ghi nhớ dưới
  \fill[white,rounded corners=3pt] (0,20) rectangle (58,52);
  \draw[TTCBorder,rounded corners=3pt,line width=.7pt] (0,20) rectangle (58,52);
  \node[anchor=north west,text=TTCRed,font=\fontsize{8}{9}\selectfont\bfseries]
    at (5,47) {01 • ĐÙN ÉP TẢI NẶNG};
  \node[anchor=north west,text width=48mm,text=TTCTextDark,font=\fontsize{6.8}{8.4}\selectfont]
    at (5,38) {Khung xưởng nhịp lớn tích hợp móng máy ép thủy lực và cầu trục dầm đôi.};

  \fill[white,rounded corners=3pt] (64,20) rectangle (122,52);
  \draw[TTCBorder,rounded corners=3pt,line width=.7pt] (64,20) rectangle (122,52);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9}\selectfont\bfseries]
    at (69,47) {02 • XỬ LÝ BỀ MẶT \& MEP};
  \node[anchor=north west,text width=48mm,text=TTCTextDark,font=\fontsize{6.8}{8.4}\selectfont]
    at (69,38) {Hệ thống sơn tĩnh điện tự động, trạm xử lý nước thải xi mạ và khí nén trung tâm.};

  \fill[white,rounded corners=3pt] (128,20) rectangle (186,52);
  \draw[TTCBorder,rounded corners=3pt,line width=.7pt] (128,20) rectangle (186,52);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9}\selectfont\bfseries]
    at (133,47) {03 • TỔNG THẦU TRỌN GÓI};
  \node[anchor=north west,text width=48mm,text=TTCTextDark,font=\fontsize{6.8}{8.4}\selectfont]
    at (133,38) {Quản lý thi công đồng bộ từ kết cấu PEB, hoàn thiện kiến trúc đến MEP vận hành.};

  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,14);
  \node[anchor=west,text=white,font=\fontsize{7.4}{9}\selectfont\bfseries]
    at (7,7) {GIÁ TRỊ CỐT LÕI: HẠ TẦNG SẢN XUẤT NHÔM ĐỊNH HÌNH CÔNG NGHỆ CAO • GIẢI PHÁP TỔNG THẦU ĐỒNG BỘ};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_28 = r"""% ============================================================
% TRANG 28: MẠNG LƯỚI CHUỖI CUNG ỨNG CHIẾN LƯỢC CẤP 1 TOÀN CẦU
% ============================================================
\pageheaderbar{CHUỖI CUNG ỨNG CHIẾN LƯỢC TIER-1}{Trang 28}
\pagefooterbar{Trang 28}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.03, scale=2.8, font=\bfseries\sffamily, text=TTCBlue] at ([yshift=-10mm]current page.center) {TIER-1 GLOBAL STRATEGIC SUPPLY CHAIN};
  \draw[TTCBlue!6!white, line width=0.5pt] ([xshift=15mm, yshift=20mm]current page.south west) grid[step=8mm] ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Mạng Lưới Chuỗi Cung Ứng Vật Tư Chiến Lược Cấp 1 Toàn Cầu}{Direct Global Tier-1 Partnerships, Premium Raw Materials, Audited Quality \& Guaranteed Logistics}

% TẦNG 1: 4 KHỐI ĐỐI TÁC CUNG ỨNG CHIẾN LƯỢC
\noindent
\begin{tabular}{@{}p{91mm}@{\hspace{4mm}}p{91mm}@{}}
  % Khối 1: Thép kết cấu \& Tôn lợp
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=48mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCRed} \faIndustry\quad 1. THÉP KẾT CẤU \& TÔN LỢP CAO CẤP:}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      \textbullet\ \textbf{Thép tấm cán nóng:} Hợp tác trực tiếp cùng \textbf{Posco (Hàn Quốc), Hòa Phát, Hyundai Steel} cung cấp phôi Q345B, A572 Gr.50 đầy đủ chứng chỉ Mill Test Certificate (MTC).\newline
      \textbullet\ \textbf{Tôn mạ hợp kim nhôm kẽm:} \textbf{BlueScope Steel (Colorbond/Zincalume)}, Tôn Đông Á, Tôn Phương Nam với chính sách bảo hành chống ăn mòn lên đến 30+ năm.}
    };
  \end{tikzpicture} &
  % Khối 2: Sơn công nghiệp \& Cách nhiệt
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=48mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCCyan} \faPaintRoller\quad 2. SƠN CÔNG NGHIỆP \& HÓA CHẤT XÂY DỰNG:}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      \textbullet\ \textbf{Sơn công nghiệp cao cấp:} Đối tác cấp 1 của \textbf{Jotun (Na Uy), Chugoku (Nhật Bản), KCC (Hàn Quốc)} cung cấp sơn Epoxy, sơn Polyurethane và sơn chống cháy đạt kiểm định PCCC.\newline
      \textbullet\ \textbf{Hóa chất \& Panel chống cháy:} \textbf{Sika (Thụy Sĩ), BASF, Panel Rockwool} chống cháy lan đạt quy chuẩn QCVN 06:2022/BXD.}
    };
  \end{tikzpicture}
  \\[2mm]
  % Khối 3: Thiết bị cơ điện MEP
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=48mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCBlue} \faBolt\quad 3. THIẾT BỊ ĐIỆN \& CƠ ĐIỆN MEP:}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      \textbullet\ \textbf{Hệ thống tủ điện \& Máy cắt:} Đối tác chiến lược \textbf{Schneider Electric (Pháp), ABB (Thụy Sĩ), Mitsubishi Electric (Nhật Bản)} bảo đảm an toàn điện năng tuyệt đối.\newline
      \textbullet\ \textbf{Cáp điện lực \& Chiếu sáng:} \textbf{Cadivi, LS Vina, Philips} cung cấp cáp chống cháy và đèn LED công nghiệp tiết kiệm 40\% điện năng.}
    };
  \end{tikzpicture} &
  % Khối 4: HVAC \& PCCC
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=48mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCGold} \faFan\quad 4. ĐIỀU HÒA HVAC \& PCCC TỰ ĐỘNG:}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      \textbullet\ \textbf{Hệ thống HVAC trung tâm:} \textbf{Daikin (Nhật Bản), Panasonic, Trane (Mỹ)} cung cấp hệ VRV/Chiller và cụm xử lý không khí phòng sạch AHU.\newline
      \textbullet\ \textbf{Bơm PCCC \& Van tự động:} \textbf{Grundfos (Đan Mạch), Ebara (Nhật Bản), Tyco} cung cấp bơm chữa cháy và đầu phun Sprinkler chứng chỉ quốc tế UL/FM.}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{2mm}

% TẦNG 2: 3 CAM KẾT CHUỖI CUNG ỨNG
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
    {\fontsize{9}{11}\selectfont\bfseries\color{TTCBlue} \faShield*\quad 3 CAM KẾT BẢO CHỨNG CHẤT LƯỢNG VẬT TƯ CỦA TÂN THÀNH CÔNG:}\\[3pt]
    \begin{tabularx}{\linewidth}{@{}p{56mm}@{\hspace{4mm}}p{56mm}@{\hspace{4mm}}p{56mm}@{}}
      \textbf{\color{TTCRed}1. 100\% CO/CQ Gốc Chính Hãng:}\newline
      {\fontsize{6.8}{8.5}\selectfont Mọi lô vật tư nhập về công trường đều có chứng chỉ xuất xứ (CO) và chứng chỉ chất lượng (CQ) bản gốc từ nhà sản xuất; thí nghiệm kiểm định Las-XD trước khi lắp đặt.} &
      \textbf{\color{TTCCyan}2. Giá Gốc Trực Tiếp Từ Nhà Máy:}\newline
      {\fontsize{6.8}{8.5}\selectfont Mua hàng trực tiếp số lượng lớn từ nhà sản xuất giúp TTC tối ưu hóa chi phí đầu vào và giữ giá cố định không phát sinh cho Chủ đầu tư.} &
      \textbf{\color{TTCBlue}3. Dự Trữ An Toàn Đảm Bảo Tiến Độ:}\newline
      {\fontsize{6.8}{8.5}\selectfont Duy trì kho dự trữ phôi thép $>3.000$ Tấn tại xưởng đối tác, sẵn sàng ứng phó biến động chuỗi cung ứng toàn cầu.}
    \end{tabularx}
  };
\end{tikzpicture}

\vspace{2mm}

% TẦNG 3: BĂNG KPI CHUỖI CUNG ỨNG
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
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCRed} TIER-1} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCCyan} 100\% CO/CQ} &
      {\fontsize{14}{16}\selectfont\bfseries\color{white} 30+ NĂM} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCGold} UL / FM} \\
      {\fontsize{7.2}{9}\selectfont Đối Tác Trực Tiếp} &
      {\fontsize{7.2}{9}\selectfont Nguồn Gốc Xuất Xứ} &
      {\fontsize{7.2}{9}\selectfont Bảo Hành Tôn BlueScope} &
      {\fontsize{7.2}{9}\selectfont Chuẩn PCCC Quốc Tế}
    \end{tabularx}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_29 = r"""% ============================================================
% TRANG 29: LOGO WALL ĐỐI TÁC \& KHÁCH HÀNG CHIẾN LƯỢC [TRANG MỚI]
% ============================================================
\pageheaderbar{ĐỐI TÁC \& KHÁCH HÀNG CHIẾN LƯỢC}{Trang 29}
\pagefooterbar{Trang 29}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.03, scale=2.8, font=\bfseries\sffamily, text=TTCBlue] at ([yshift=-10mm]current page.center) {STRATEGIC CLIENTS \& PARTNERS LOGO WALL};
  \draw[TTCBlue!6!white, line width=0.5pt] ([xshift=15mm, yshift=20mm]current page.south west) grid[step=8mm] ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Mạng Lưới Khách Hàng Quốc Tế \& Đối Tác Chiến Lược}{Trusted by Global Multinational Corporations \& Premier Vietnamese Industrial Leaders}

% TẦNG 1: 4 KHỐI ĐỐI TÁC THEO QUỐC GIA \& PHÂN KHÚC
\noindent
\begin{tabular}{@{}p{91mm}@{\hspace{4mm}}p{91mm}@{}}
  % Khối 1: Nhật Bản \& Hàn Quốc
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=48mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCRed} \faFlag\quad 1. TẬP ĐOÀN NHẬT BẢN \& HÀN QUỐC:}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      \textbullet\ \textbf{Sumitomo Electric (Nhật Bản):} NM dây cáp điện tử 15.015 m$^2$.\newline
      \textbullet\ \textbf{Daeyun Group (Hàn Quốc):} NM phòng sạch linh kiện 20.000 m$^2$.\newline
      \textbullet\ \textbf{Towada Electronic (Nhật Bản):} Xưởng lắp ráp bản mạch điện tử.\newline
      \textbullet\ \textbf{Toyo Seikan \& Shinjo Corp (Nhật Bản):} NM bao bì \& cơ khí chính xác.}
    };
  \end{tikzpicture} &
  % Khối 2: Đài Loan \& Singapore
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=48mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCCyan} \faGlobeAsia\quad 2. TẬP ĐOÀN ĐÀI LOAN \& SINGAPORE:}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      \textbullet\ \textbf{Foxconn Technology Group (Đài Loan):} Xưởng sản xuất linh kiện 12.000 m$^2$.\newline
      \textbullet\ \textbf{BW Industrial (Singapore):} Tổ hợp logistics thông minh 45.000 m$^2$.\newline
      \textbullet\ \textbf{Saigon Ve Wong / A-One (Đài Loan):} NM chế biến thực phẩm 30.000 m$^2$.\newline
      \textbullet\ \textbf{New Hope Group (Singapore):} Cụm tháp Silo thức ăn chăn nuôi 32.000 m$^2$.}
    };
  \end{tikzpicture}
  \\[2mm]
  % Khối 3: Đa quốc gia \& ASEAN
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=48mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCBlue} \faGlobe\quad 3. TẬP ĐOÀN ĐA QUỐC GIA \& ASEAN:}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      \textbullet\ \textbf{Japfa Comfeed (Indonesia):} Tổ hợp Silo nông nghiệp công nghệ cao 50.000 m$^2$.\newline
      \textbullet\ \textbf{C.P Group (Thái Lan):} NM chế biến thức ăn chăn nuôi Đồng Văn 35.000 m$^2$.\newline
      \textbullet\ \textbf{Yusen Logistics (Nhật Bản):} Kho lạnh và logistics ngoại quan Đình Vũ.\newline
      \textbullet\ \textbf{Fami Garment (Hàn Quốc):} Xưởng may xuất khẩu Thụy Vân 28.000 m$^2$.}
    };
  \end{tikzpicture} &
  % Khối 4: Doanh nghiệp lớn Việt Nam
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=48mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCGold} \faBuilding\quad 4. TẬP ĐOÀN HÀNG ĐẦU VIỆT NAM:}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      \textbullet\ \textbf{Tập đoàn May Sông Hồng:} NM may xuất khẩu Sông Hồng 7 (68.000 m$^2$).\newline
      \textbullet\ \textbf{Công ty Cổ phần Gạch Hồng Trang:} Tổ hợp nhà máy 100.000 m$^2$.\newline
      \textbullet\ \textbf{Tập đoàn Sơn Hà:} NM thiết bị năng lượng và bồn nước Thuận Thành 24.000 m$^2$.\newline
      \textbullet\ \textbf{Tập đoàn Hòa Phát:} Đối tác cung cấp thép và hạ tầng công nghiệp.}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{2mm}

% TẦNG 2: BẢNG LÝ DO KHÁCH HÀNG FDI LỰA CHỌN TTC
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
    {\fontsize{9}{11}\selectfont\bfseries\color{TTCBlue} \faHandshake\quad LÝ DO CÁC TẬP ĐOÀN FDI TOÀN CẦU CHỌN TÂN THÀNH CÔNG:}\\[3pt]
    \begin{tabularx}{\linewidth}{@{}p{56mm}@{\hspace{4mm}}p{56mm}@{\hspace{4mm}}p{56mm}@{}}
      \textbf{\color{TTCRed}1. Pháp Lý FDI Trọn Gói:}\newline
      {\fontsize{6.8}{8.5}\selectfont Am hiểu sâu sắc thủ tục cấp phép đầu tư, thẩm duyệt ĐTM, PCCC và nghiệm thu xây dựng tại hơn 20 tỉnh thành.} &
      \textbf{\color{TTCCyan}2. Giao Tiếp Đa Ngôn Ngữ:}\newline
      {\fontsize{6.8}{8.5}\selectfont Đội ngũ kỹ sư làm việc thành thạo tiếng Anh, tiếng Nhật, tiếng Hàn và tiếng Trung; xử lý hồ sơ chuẩn quốc tế.} &
      \textbf{\color{TTCBlue}3. Cam Kết FIDIC Chặt Chẽ:}\newline
      {\fontsize{6.8}{8.5}\selectfont Áp dụng chuẩn hợp đồng FIDIC Silver Book, bảo lãnh ngân hàng uy tín 250 tỷ, cam kết 0 phát sinh chi phí.}
    \end{tabularx}
  };
\end{tikzpicture}

\vspace{2mm}

% TẦNG 3: BĂNG KPI LOGO WALL
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
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCRed} 65\% FDI} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCCyan} 85\% KH LẶP LẠI} &
      {\fontsize{14}{16}\selectfont\bfseries\color{white} 4 NGÔN NGỮ} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCGold} 100\% HÀI LÒNG} \\
      {\fontsize{7.2}{9}\selectfont Tỷ Trọng Dự Án Quốc Tế} &
      {\fontsize{7.2}{9}\selectfont Khách Hàng Giao Dự Án Tiếp} &
      {\fontsize{7.2}{9}\selectfont Giao Tiếp \& Hồ Sơ} &
      {\fontsize{7.2}{9}\selectfont Đánh Giá Chất Lượng EPC}
    \end{tabularx}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_30 = r"""% ============================================================
% TRANG 30: THƯ KHEN NGỢI \& ĐÁNH GIÁ TỪ CHỦ ĐẦU TƯ FDI (TESTIMONIALS)
% ============================================================
\pageheaderbar{ĐÁNH GIÁ TỪ CÁC CHỦ ĐẦU TƯ FDI}{Trang 30}
\pagefooterbar{Trang 30}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.03, scale=2.8, font=\bfseries\sffamily, text=TTCBlue] at ([yshift=-10mm]current page.center) {FDI CLIENT TESTIMONIALS \& COMMENDATIONS};
  \draw[TTCBlue!6!white, line width=0.5pt] ([xshift=15mm, yshift=20mm]current page.south west) grid[step=8mm] ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Chứng Thực \& Đánh Giá Từ Các Tập Đoàn Đa Quốc Gia FDI}{Formal Letters of Commendation, Client Satisfaction Endorsements \& Long-Term Partnerships}

% TẦNG 1: 4 KHỐI TESTIMONIALS CHÍNH THỨC
\noindent
\begin{tabular}{@{}p{91mm}@{\hspace{4mm}}p{91mm}@{}}
  % Testimonial 1: May Sông Hồng
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=50mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.5}{10.5}\selectfont\bfseries\color{TTCBlue} \faQuoteLeft\quad TẬP ĐOÀN MAY SÔNG HỒNG}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\itshape\color{TTCTextDark}
      ``Tân Thành Công đã chứng minh năng lực vượt trội của một Tổng thầu EPC thế hệ mới trong dự án Sông Hồng 7 (68.000 m$^2$ sàn 2 tầng). Khả năng xử lý kết cấu dầm sàn chịu tải 1.200 kg/m$^2$, ứng dụng mô hình BIM 5D triệt tiêu xung đột và tiến độ về đích sớm 30 ngày đã mang lại hiệu quả đầu tư rất lớn cho chúng tôi.''}\\[4pt]
      \raggedleft
      {\fontsize{7.2}{8.5}\selectfont\bfseries\color{TTCRed} Ông BÙI ĐỨC THỊNH}\newline
      {\fontsize{6.5}{7.8}\selectfont\color{TTCTextMuted} Chủ Tịch HĐQT -- Công Ty CP May Sông Hồng}
    };
  \end{tikzpicture} &
  % Testimonial 2: Japfa Comfeed
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=50mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.5}{10.5}\selectfont\bfseries\color{TTCBlue} \faQuoteLeft\quad TẬP ĐOÀN JAPFA COMFEED (INDONESIA)}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\itshape\color{TTCTextDark}
      ``TTC JSC là một trong số ít nhà thầu tại Việt Nam có năng lực thi công tháp Silo thép cao 45m với độ chính xác cao và an toàn tuyệt đối. Đội ngũ kỹ sư làm việc chuyên nghiệp, tuân thủ nghiêm ngặt chuẩn an toàn OHSAS và cam kết tài chính minh bạch, không phát sinh chi phí.''}\\[4pt]
      \raggedleft
      {\fontsize{7.2}{8.5}\selectfont\bfseries\color{TTCRed} Mr. BUDI SANTOSO}\newline
      {\fontsize{6.5}{7.8}\selectfont\color{TTCTextMuted} Project Director -- Japfa Comfeed Vietnam}
    };
  \end{tikzpicture}
  \\[2mm]
  % Testimonial 3: Gạch Hồng Trang
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=50mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.5}{10.5}\selectfont\bfseries\color{TTCBlue} \faQuoteLeft\quad CÔNG TY CỔ PHẦN GẠCH HỒNG TRANG}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\itshape\color{TTCTextDark}
      ``Dự án tổ hợp 100.000 m$^2$ của chúng tôi với khẩu độ vượt nhịp 42m không cột giữa được Tân Thành Công hoàn thành chỉ trong 150 ngày. Đội xe máy cơ giới $>300$ tỷ và sự chủ động chuỗi cung ứng của TTC là yếu tố quyết định giúp nhà máy đi vào sản xuất đúng hẹn.''}\\[4pt]
      \raggedleft
      {\fontsize{7.2}{8.5}\selectfont\bfseries\color{TTCRed} Ông NGUYỄN VĂN TRANG}\newline
      {\fontsize{6.5}{7.8}\selectfont\color{TTCTextMuted} Tổng Giám Đốc -- Công Ty CP Gạch Hồng Trang}
    };
  \end{tikzpicture} &
  % Testimonial 4: Daeyun Group Hàn Quốc
  \begin{tikzpicture}
    \node[
      rounded corners=6pt, fill=white, draw=TTCBlue!40!white, line width=0.8pt,
      minimum width=91mm, minimum height=50mm, inner sep=6pt, align=left, text width=83mm
    ] {
      {\fontsize{8.5}{10.5}\selectfont\bfseries\color{TTCBlue} \faQuoteLeft\quad DAEYUN GROUP (HÀN QUỐC)}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\itshape\color{TTCTextDark}
      ``Tân Thành Công đã đáp ứng hoàn hảo các yêu cầu kỹ thuật cực kỳ khắt khe về phòng sạch Cleanroom Class 10.000 và sàn kháng tĩnh điện ESD. Chúng tôi đặc biệt đánh giá cao sự hỗ trợ pháp lý tận tâm và khả năng giao tiếp tiếng Hàn chuyên nghiệp của đội ngũ kỹ sư TTC.''}\\[4pt]
      \raggedleft
      {\fontsize{7.2}{8.5}\selectfont\bfseries\color{TTCRed} Mr. KIM JUNG HOON}\newline
      {\fontsize{6.5}{7.8}\selectfont\color{TTCTextMuted} Technical Director -- Daeyun ST Vina}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{2mm}

% TẦNG 2: BẢNG KHẢO SÁT HÀI LÒNG KHÁCH HÀNG
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
    {\fontsize{9}{11}\selectfont\bfseries\color{TTCBlue} \faStar\quad KẾT QUẢ KHẢO SÁT HÀI LÒNG KHÁCH HÀNG FDI NĂM 2024 -- 2025:}\\[3pt]
    \begin{tabularx}{\linewidth}{@{}p{56mm}@{\hspace{4mm}}p{56mm}@{\hspace{4mm}}p{56mm}@{}}
      \textbf{\color{TTCRed}Chất Lượng Công Trình (QA):}\newline
      {\fontsize{13}{15}\selectfont\bfseries\color{TTCRed} 99.2\% Hài Lòng}\newline
      {\fontsize{6.8}{8.5}\selectfont 100\% cấu kiện dầm thép đạt chuẩn kiểm tra NDT AWS D1.1 và không xảy ra sự cố thấm dột.} &
      \textbf{\color{TTCCyan}Tiến Độ Bàn Giao (Fast-Track):}\newline
      {\fontsize{13}{15}\selectfont\bfseries\color{TTCCyan} 100\% Đúng / Sớm Hạn}\newline
      {\fontsize{6.8}{8.5}\selectfont Không có dự án nào bị trễ tiến độ; trung bình bàn giao sớm từ 15--45 ngày so với hợp đồng.} &
      \textbf{\color{TTCBlue}An Toàn Lao Động (HSE):}\newline
      {\fontsize{13}{15}\selectfont\bfseries\color{TTCBlue} 100\% Zero Accident}\newline
      {\fontsize{6.8}{8.5}\selectfont Duy trì tuyệt đối không có tai nạn lao động mất thời gian (LTI Free) trên mọi công trường.}
    \end{tabularx}
  };
\end{tikzpicture}

\vspace{2mm}

% TẦNG 3: BĂNG KPI TESTIMONIALS
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
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCRed} 100\% THƯ KHEN} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCCyan} 99.2\%} &
      {\fontsize{14}{16}\selectfont\bfseries\color{white} 85\% TÁI HỢP TÁC} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCGold} 5 SAO} \\
      {\fontsize{7.2}{9}\selectfont Đánh Giá Tích Cực} &
      {\fontsize{7.2}{9}\selectfont Tỷ Lệ Đạt Chất Lượng} &
      {\fontsize{7.2}{9}\selectfont Khách Hàng Giao Gói 2} &
      {\fontsize{7.2}{9}\selectfont Mức Độ Uy Tín Tổng Thầu}
    \end{tabularx}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

print("Section 5 code loaded.")
