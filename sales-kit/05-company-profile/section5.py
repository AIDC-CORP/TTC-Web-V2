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
  \node[anchor=west,text=white,font=\fontsize{6.5}{7.5}\selectfont\bfseries] at (129,182) {PHẠM VI TTC};

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

  \projectrowa{165}{01}{Tổ hợp NM Gạch Hồng Trang}{Gạch Hồng Trang • Việt Nam}{100.000 m$^2$}{Lập Thạch\\Vĩnh Phúc}{Tổng thầu EPC • Fast-track 6,5 tháng}{TTCLightBlue}
  \projectrowa{143}{02}{Nhà máy May Sông Hồng 7}{May Sông Hồng • Việt Nam}{68.000 m$^2$}{Hải Hậu\\Nam Định}{Thiết kế và thi công • Sàn hai tầng tải nặng}{white}
  \projectrowa{121}{03}{Tổ hợp NM Japfa Comfeed}{Japfa • Indonesia}{50.000 m$^2$}{Vĩnh Phúc\\Thái Bình}{Kết cấu silo cao 45 m • Xưởng CNC}{TTCLightBlue}
  \projectrowa{99}{04}{NM Thức Ăn Chăn Nuôi CP}{C.P • Thái Lan}{35.000 m$^2$}{Đồng Văn\\Hà Nam}{Xưởng sản xuất • Kho bảo quản}{white}
  \projectrowa{77}{05}{Nhà máy Daeyun ST Vina}{Daeyun • Hàn Quốc}{20.000 m$^2$}{Bá Thiện 2\\Vĩnh Phúc}{Xưởng sạch • Sàn chống tĩnh điện}{TTCLightBlue}
  \projectrowa{55}{06}{Nhà máy Dây Cáp Sumidenso}{Sumitomo • Nhật Bản}{15.015 m$^2$}{Sông Hậu\\Hậu Giang}{Nhà máy dây cáp ô tô • Hệ PCCC}{white}
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
\secbrand{Danh Mục Dự Án FDI Và Công Nghiệp Phụ Trợ}{Tám công trình tiếp theo • Nhà đầu tư đa quốc gia • Yêu cầu chuyên biệt}

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
  \node[anchor=west,text=white,font=\fontsize{6.5}{7.5}\selectfont\bfseries] at (129,182) {PHẠM VI TTC};

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

  \projectrowb{165}{09}{NM Chăn Nuôi New Hope}{New Hope • Singapore}{32.000 m$^2$}{Quang Châu\\Bắc Giang}{Silo ngũ cốc • Trạm điện biến áp}{TTCLightBlue}
  \projectrowb{143}{10}{NM Cơ Khí Shinjo Vina}{Shinjo • Nhật Bản}{18.500 m$^2$}{VSIP\\Bắc Ninh}{Xưởng cơ khí chính xác • Dầm cầu trục 15T}{white}
  \projectrowb{121}{11}{NM Điện Tử Towada}{Towada • Nhật Bản}{16.000 m$^2$}{Phúc Điền\\Hải Dương}{Lắp ráp vi mạch • Phòng sạch ISO}{TTCLightBlue}
  \projectrowb{99}{12}{NM Bao Bì Toyo Seikan}{Toyo Seikan • Nhật Bản}{22.000 m$^2$}{Tiên Sơn\\Bắc Ninh}{Tổng thầu EPC • Xưởng bao bì • Sàn phẳng}{white}
  \projectrowb{77}{13}{Xưởng May Fami Vina}{Fami Garment • Hàn Quốc}{28.000 m$^2$}{Thụy Vân\\Phú Thọ}{Nhà xưởng may hai tầng • Hệ HVAC}{TTCLightBlue}
  \projectrowb{55}{14}{Kho Logistics Yusen}{Yusen • Nhật Bản}{25.000 m$^2$}{Đình Vũ\\Hải Phòng}{Kho ngoại quan • Cụm sàn nâng hàng}{white}
  \projectrowb{33}{15}{NM Thực Phẩm A-One}{Saigon Ve Wong • Đài Loan}{30.000 m$^2$}{Sóng Thần 2\\Bình Dương}{Xưởng chế biến thực phẩm • Chuẩn HACCP}{TTCLightBlue}
  \projectrowb{11}{16}{NM Năng Lượng Sơn Hà}{Sơn Hà • Việt Nam}{24.000 m$^2$}{Thuận Thành\\Bắc Ninh}{Xưởng sản xuất bồn • Pin mặt trời}{white}
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
    {\fontsize{7.8}{9.2}\selectfont\bfseries\color{white} HỒNG TRANG • SÔNG HỒNG 7}\\[-.2mm]
    {\fontsize{6}{7.2}\selectfont\color{white!75!gray}EPC nhịp lớn • nhà xưởng hai tầng}
  };
  \node[align=center,text width=53mm] at (93,14) {
    {\fontsize{7.8}{9.2}\selectfont\bfseries\color{white} JAPFA • DAEYUN}\\[-.2mm]
    {\fontsize{6}{7.2}\selectfont\color{white!75!gray}Công trình process • phòng sạch}
  };
  \node[align=center,text width=53mm] at (155,14) {
    {\fontsize{7.8}{9.2}\selectfont\bfseries\color{white} SUMIDENSO • FOXCONN}\\[-.2mm]
    {\fontsize{6}{7.2}\selectfont\color{white!75!gray}Bàn giao chất lượng • nhà xưởng điện tử}
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
% TRANG 22: FLAGSHIP CASE -- NHÀ MÁY GẠCH HỒNG TRANG
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{DỰ ÁN TIÊU BIỂU • HỒNG TRANG}{Trang 22}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Hồ Sơ Dự Án 01: Nhà Máy Gạch Hồng Trang}{Flagship EPC case • Large-span industrial facility • Lập Thạch, Vĩnh Phúc}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);

  % Ảnh dự án nhỏ gọn, đúng với độ phân giải nguồn
  \begin{scope}
    \clip[rounded corners=4pt] (0,150) rectangle (70,220);
    \node[inner sep=0pt] at (35,185)
      {\includegraphics[width=70mm,height=70mm]{../../public/project-assets/hongtrang.jpg}};
    \fill[TTCDeepNavy,opacity=.88] (0,150) rectangle (70,161);
    \node[anchor=west,text=white,font=\fontsize{7}{8}\selectfont\bfseries]
      at (4,155.5) {ẢNH DỰ ÁN • LẬP THẠCH, VĨNH PHÚC};
  \end{scope}
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,150) rectangle (70,220);

  % Tóm tắt điều hành
  \fill[TTCLightBlue,rounded corners=4pt] (74,150) rectangle (186,220);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (74,150) rectangle (186,220);
  \node[anchor=north west,text=TTCRed,font=\fontsize{7.5}{9}\selectfont\bfseries]
    at (80,214) {TỔNG THẦU EPC};
  \node[anchor=north west,text width=99mm,align=left,text=TTCBlue,
        font=\fontsize{14}{16}\selectfont\bfseries]
    at (80,207) {100.000 m$^2$ QUY HOẠCH};
  \draw[TTCBorder,line width=.55pt] (80,190) -- (180,190);
  \foreach \x in {113.3,146.6}{\draw[TTCBorder,line width=.5pt] (\x,163) -- (\x,186);}
  \node[align=center,text width=29mm] at (96.5,176) {
    {\fontsize{11}{12}\selectfont\bfseries\color{TTCRed}75.000 m$^2$}\\[-.5mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}DIỆN TÍCH SÀN}};
  \node[align=center,text width=29mm] at (130,176) {
    {\fontsize{11}{12}\selectfont\bfseries\color{TTCBlue}NHỊP 42M}\\[-.5mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}KHÔNG CỘT GIỮA}};
  \node[align=center,text width=29mm] at (163.5,176) {
    {\fontsize{11}{12}\selectfont\bfseries\color{TTCBlue}6,5 THÁNG}\\[-.5mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}TIẾN ĐỘ THI CÔNG}};
  \node[anchor=south west,text width=99mm,align=left,text=TTCTextDark,
        font=\fontsize{7.4}{9}\selectfont]
    at (80,153) {\textbf{Phạm vi TTC:} Tổng thầu EPC; phối hợp thiết kế, kết cấu thép, hạ tầng và tổ chức thi công fast-track.};

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
    at (5,110) {Dây chuyền lò nung cần mặt bằng liên tục, không bị chia cắt bởi cột giữa; đồng thời nhà xưởng phải thoát nhiệt hiệu quả.};

  \draw[-{Latex[length=2.5mm]},TTCCyan,line width=1pt] (59.5,108) -- (63,108);
  \fill[TTCDeepNavy,rounded corners=4pt] (64,79) rectangle (122,137);
  \node[text=TTCDeepNavy,fill=white,rounded corners=2pt,font=\fontsize{7}{8}\selectfont\bfseries,
        minimum width=11mm,minimum height=9mm] at (74.5,128.5) {02};
  \node[anchor=north west,text=white,font=\fontsize{9}{10.5}\selectfont\bfseries]
    at (69,120) {GIẢI PHÁP TTC};
  \node[anchor=north west,text width=48mm,align=left,text=white,
        font=\fontsize{7.2}{9}\selectfont]
    at (69,110) {Khung thép tiết diện thay đổi vượt nhịp 42 m; thông gió đối lưu đỉnh mái; các gói EPC được triển khai song song.};

  \draw[-{Latex[length=2.5mm]},TTCCyan,line width=1pt] (123.5,108) -- (127,108);
  \fill[TTCLightBlue,rounded corners=4pt] (128,79) rectangle (186,137);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (128,79) rectangle (186,137);
  \fill[TTCBlue,rounded corners=2pt] (133,124) rectangle (144,133);
  \node[text=white,font=\fontsize{7}{8}\selectfont\bfseries] at (138.5,128.5) {03};
  \node[anchor=north west,text=TTCBlue,font=\fontsize{9}{10.5}\selectfont\bfseries]
    at (133,120) {KẾT QUẢ};
  \node[anchor=north west,text width=48mm,align=left,text=TTCTextDark,
        font=\fontsize{7.2}{9}\selectfont]
    at (133,110) {Hoàn thành 75.000 m$^2$ sàn trong 6,5 tháng; bàn giao sớm 20 ngày theo hồ sơ năng lực hiện tại.};

  % Băng ghi nhớ
  \fill[white,rounded corners=4pt] (0,20) rectangle (186,70);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,20) rectangle (186,70);
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (7,61) {BA ĐIỂM NGƯỜI ĐỌC CẦN NHỚ};
  \draw[TTCBorder] (62,27) -- (62,58);
  \draw[TTCBorder] (124,27) -- (124,58);
  \node[align=center,text width=52mm] at (31,42) {
    {\fontsize{12}{13}\selectfont\bfseries\color{TTCRed}42 MÉT}\\[-.5mm]
    {\fontsize{6.6}{8}\selectfont\color{TTCTextMuted}MẶT BẰNG SẢN XUẤT KHÔNG CỘT GIỮA}};
  \node[align=center,text width=52mm] at (93,42) {
    {\fontsize{12}{13}\selectfont\bfseries\color{TTCBlue}EPC SONG SONG}\\[-.5mm]
    {\fontsize{6.6}{8}\selectfont\color{TTCTextMuted}THIẾT KẾ • SẢN XUẤT • THI CÔNG}};
  \node[align=center,text width=52mm] at (155,42) {
    {\fontsize{12}{13}\selectfont\bfseries\color{TTCBlue}SỚM 20 NGÀY}\\[-.5mm]
    {\fontsize{6.6}{8}\selectfont\color{TTCTextMuted}SO VỚI MỐC CAM KẾT}};

  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,14);
  \node[anchor=west,text=white,font=\fontsize{7.4}{9}\selectfont\bfseries]
    at (7,7) {GIÁ TRỊ CỐT LÕI: KHÔNG GIAN SẢN XUẤT LIÊN TỤC • TIẾN ĐỘ CÓ KIỂM SOÁT};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_23 = r"""% ============================================================
% TRANG 23: ENGINEERING CASE -- NHÀ MÁY MAY SÔNG HỒNG 7
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{GIẢI PHÁP KỸ THUẬT • SÔNG HỒNG 7}{Trang 23}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Hồ Sơ Dự Án 02: Nhà Máy May Sông Hồng 7}{Engineering anatomy • Two-storey heavy-duty factory • Hải Hậu, Nam Định}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);

  % Phối cảnh và thẻ dữ liệu
  \begin{scope}
    \clip[rounded corners=4pt] (0,148) rectangle (104,220);
    \node[inner sep=0pt] at (52,184)
      {\includegraphics[width=104mm,height=77.5mm]{../../public/project-assets/songhong7.jpg}};
    \fill[TTCDeepNavy,opacity=.88] (0,148) rectangle (104,160);
    \node[anchor=west,text=white,font=\fontsize{7}{8}\selectfont\bfseries]
      at (4,154) {PHỐI CẢNH DỰ ÁN • HẢI HẬU, NAM ĐỊNH};
  \end{scope}
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,148) rectangle (104,220);

  \fill[TTCDeepNavy,rounded corners=4pt] (108,148) rectangle (186,220);
  \node[anchor=north west,text=TTCCyan,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (114,214) {TÓM TẮT DỰ ÁN};
  \node[anchor=north west,text=white,font=\fontsize{15}{16}\selectfont\bfseries]
    at (114,205) {68.000 m$^2$};
  \node[anchor=north west,text=white!75!gray,font=\fontsize{6.5}{8}\selectfont]
    at (114,190) {TỔNG DIỆN TÍCH SÀN};
  \draw[white!25!gray] (114,183) -- (180,183);
  \node[anchor=north west,text width=62mm,align=left,text=white,
        font=\fontsize{7.2}{9}\selectfont]
    at (114,178) {\textbf{Kết cấu:} Nhà xưởng hai tầng\\[1mm]
                  \textbf{Tải trọng thiết kế:} 1.200 kg/m$^2$\\[1mm]
                  \textbf{Tiến độ:} 180 ngày\\[1mm]
                  \textbf{Vai trò TTC:} Thiết kế và thi công};

  % Sơ đồ kỹ thuật khác biệt với trang trước
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (0,140) {SƠ ĐỒ NGUYÊN LÝ • ĐƯỜNG TRUYỀN TẢI VÀ KIỂM SOÁT RUNG};
  \fill[TTCLightBlue,rounded corners=4pt] (0,53) rectangle (186,134);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,53) rectangle (186,134);

  % Khung hai tầng
  \draw[TTCBlue,line width=1.2pt] (10,67) -- (132,67);
  \draw[TTCBlue,line width=2pt] (12,94) -- (130,94);
  \draw[TTCBlue,line width=1.2pt] (12,122) -- (71,130) -- (130,122);
  \foreach \x in {16,44,72,100,128}{
    \draw[TTCBlue,line width=1.2pt] (\x,67) -- (\x,122);
  }
  \foreach \x in {26,54,82,110}{
    \fill[white] (\x,98) rectangle +(15,7);
    \draw[TTCBorder] (\x,98) rectangle +(15,7);
    \draw[-{Latex[length=2mm]},TTCRed,line width=.8pt] (\x+7.5,108) -- (\x+7.5,96);
  }
  \node[anchor=west,text=TTCRed,font=\fontsize{6.5}{8}\selectfont\bfseries]
    at (16,112) {TẢI TRỌNG ĐỘNG TỪ CỤM MÁY SẢN XUẤT};
  \draw[TTCCyan,line width=1.2pt,dashed] (17,87) -- (127,87);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.3}{7.5}\selectfont\bfseries]
    at (19,82) {TUYẾN MEP / HVAC PHỐI HỢP DƯỚI SÀN};
  \draw[<->,>=Latex,TTCBlue,line width=.8pt] (16,60) -- (128,60);
  \node[fill=TTCLightBlue,text=TTCBlue,font=\fontsize{6.5}{8}\selectfont\bfseries]
    at (72,60) {KHÔNG GIAN SẢN XUẤT HAI TẦNG};

  % Chú giải bên phải
  \draw[TTCBorder] (138,60) -- (138,127);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (145,124) {3 QUYẾT ĐỊNH THIẾT KẾ};
  \node[anchor=north west,text width=34mm,align=left,text=TTCTextDark,
        font=\fontsize{6.7}{8.3}\selectfont]
    at (145,114) {\textbf{01 • Sàn liên hợp}\newline
                  Deck mạ kẽm và bê tông cốt thép tạo mặt sàn tải nặng.};
  \node[anchor=north west,text width=34mm,align=left,text=TTCTextDark,
        font=\fontsize{6.7}{8.3}\selectfont]
    at (145,92) {\textbf{02 • Kiểm soát rung}\newline
                  Phân vùng tải và đường truyền lực rõ ràng theo khu máy.};
  \node[anchor=north west,text width=34mm,align=left,text=TTCTextDark,
        font=\fontsize{6.7}{8.3}\selectfont]
    at (145,70) {\textbf{03 • Phối hợp MEP}\newline
                  Dành trước không gian HVAC và tuyến kỹ thuật dưới sàn.};

  % Ba ý ghi nhớ
  \fill[white,rounded corners=3pt] (0,9) rectangle (58,45);
  \draw[TTCBorder,rounded corners=3pt] (0,9) rectangle (58,45);
  \node[anchor=north west,text=TTCRed,font=\fontsize{8}{9}\selectfont\bfseries]
    at (5,39) {01 • TẢI NẶNG};
  \node[anchor=north west,text width=48mm,text=TTCTextDark,font=\fontsize{6.8}{8.4}\selectfont]
    at (5,30) {Sàn tầng hai được tổ chức theo khu vực tải và thiết bị.};

  \fill[white,rounded corners=3pt] (64,9) rectangle (122,45);
  \draw[TTCBorder,rounded corners=3pt] (64,9) rectangle (122,45);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9}\selectfont\bfseries]
    at (69,39) {02 • PHỐI HỢP};
  \node[anchor=north west,text width=48mm,text=TTCTextDark,font=\fontsize{6.8}{8.4}\selectfont]
    at (69,30) {Kết cấu và MEP được khóa giao diện trước khi triển khai.};

  \fill[white,rounded corners=3pt] (128,9) rectangle (186,45);
  \draw[TTCBorder,rounded corners=3pt] (128,9) rectangle (186,45);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9}\selectfont\bfseries]
    at (133,39) {03 • TIẾN ĐỘ};
  \node[anchor=north west,text width=48mm,text=TTCTextDark,font=\fontsize{6.8}{8.4}\selectfont]
    at (133,30) {Chu kỳ kết cấu, sàn và cơ điện được triển khai theo nhịp lặp.};

  \fill[TTCDeepNavy,rounded corners=2pt] (0,0) rectangle (186,6);
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_24 = r"""% ============================================================
% TRANG 24: PROCESS CASE -- TỔ HỢP JAPFA COMFEED
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{CÔNG TRÌNH CÔNG NGHỆ • JAPFA COMFEED}{Trang 24}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Hồ Sơ Dự Án 03: Tổ Hợp Japfa Comfeed}{Process-industry case • High-rise silo • Dynamic-load and dust control}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);

  % Ảnh nhỏ và bảng số liệu 2x2
  \begin{scope}
    \clip[rounded corners=4pt] (0,151) rectangle (68,219);
    \node[inner sep=0pt] at (34,185)
      {\includegraphics[width=68mm,height=68mm]{../../public/project-assets/japfa.jpg}};
    \fill[TTCDeepNavy,opacity=.9] (0,151) rectangle (68,162);
    \node[anchor=west,text=white,font=\fontsize{7}{8}\selectfont\bfseries]
      at (4,156.5) {ẢNH DỰ ÁN • JAPFA COMFEED};
  \end{scope}
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,151) rectangle (68,219);

  \fill[TTCLightBlue,rounded corners=4pt] (72,151) rectangle (186,219);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (72,151) rectangle (186,219);
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (78,211) {CỤM DỰ ÁN VĨNH PHÚC / THÁI BÌNH};
  \draw[TTCBorder] (129,158) -- (129,204);
  \draw[TTCBorder] (78,181) -- (180,181);
  \node[align=center,text width=45mm] at (103.5,193) {
    {\fontsize{12}{13}\selectfont\bfseries\color{TTCRed}50.000 m$^2$}\\[-.5mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}DIỆN TÍCH QUY HOẠCH}};
  \node[align=center,text width=45mm] at (154.5,193) {
    {\fontsize{12}{13}\selectfont\bfseries\color{TTCBlue}SILO 45M}\\[-.5mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}CHIỀU CAO CỤM THÁP}};
  \node[align=center,text width=45mm] at (103.5,169) {
    {\fontsize{12}{13}\selectfont\bfseries\color{TTCBlue}2.800 TẤN}\\[-.5mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}KẾT CẤU THÉP PEB}};
  \node[align=center,text width=45mm] at (154.5,169) {
    {\fontsize{12}{13}\selectfont\bfseries\color{TTCBlue}165 NGÀY}\\[-.5mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}TIẾN ĐỘ THI CÔNG}};

  % Câu chuyện theo chiều cao
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (0,143) {CÂU CHUYỆN KỸ THUẬT • TỪ MÓNG ĐỘNG LỰC ĐẾN ĐỈNH SILO};
  \fill[TTCLightBlue,rounded corners=4pt] (0,56) rectangle (54,137);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,56) rectangle (54,137);

  % Tháp silo mô phỏng
  \fill[TTCBlue!10!white] (19,69) rectangle (42,123);
  \draw[TTCBlue,line width=1.1pt] (19,69) rectangle (42,123);
  \foreach \y in {80,91,102,113}{\draw[TTCBorder] (19,\y) -- (42,\y);}
  \draw[TTCBlue,line width=1.1pt] (16,69) -- (45,69);
  \fill[TTCDeepNavy] (12,62) rectangle (49,69);
  \draw[<->,>=Latex,TTCRed,line width=.9pt] (9,69) -- (9,123);
  \node[rotate=90,text=TTCRed,font=\fontsize{9}{10}\selectfont\bfseries]
    at (4,96) {45 MÉT};
  \node[text=TTCBlue,font=\fontsize{6.5}{7.5}\selectfont\bfseries]
    at (30.5,129) {CỤM SILO};
  \node[text=white,font=\fontsize{6.2}{7.2}\selectfont\bfseries]
    at (30.5,65.5) {MÓNG D800};

  % Ba rủi ro -- ba phản hồi
  \fill[white,rounded corners=3pt] (60,108) rectangle (186,137);
  \draw[TTCBorder,rounded corners=3pt] (60,108) rectangle (186,137);
  \fill[TTCRed] (60,108) rectangle (63,137);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9}\selectfont\bfseries]
    at (69,132) {01 • TẢI ĐỘNG MÁY NGHIỀN};
  \node[anchor=north west,text width=108mm,text=TTCTextDark,font=\fontsize{6.9}{8.4}\selectfont]
    at (69,122) {Móng cọc khoan nhồi sâu D800 kết hợp lớp giảm chấn để kiểm soát rung truyền sang khu vực lân cận.};

  \fill[white,rounded corners=3pt] (60,76) rectangle (186,105);
  \draw[TTCBorder,rounded corners=3pt] (60,76) rectangle (186,105);
  \fill[TTCBlue] (60,76) rectangle (63,105);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9}\selectfont\bfseries]
    at (69,100) {02 • LẮP DỰNG THEO CAO ĐỘ};
  \node[anchor=north west,text width=108mm,text=TTCTextDark,font=\fontsize{6.9}{8.4}\selectfont]
    at (69,90) {Chia tháp thành các phân đoạn lắp dựng; kiểm soát cao độ, độ thẳng đứng và liên kết tại từng điểm dừng kỹ thuật.};

  \fill[white,rounded corners=3pt] (60,44) rectangle (186,73);
  \draw[TTCBorder,rounded corners=3pt] (60,44) rectangle (186,73);
  \fill[TTCBlue] (60,44) rectangle (63,73);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9}\selectfont\bfseries]
    at (69,68) {03 • BỤI VÀ AN TOÀN QUY TRÌNH};
  \node[anchor=north west,text width=108mm,text=TTCTextDark,font=\fontsize{6.9}{8.4}\selectfont]
    at (69,58) {Tích hợp thu gom bụi, thông gió và giải pháp xả áp theo yêu cầu vận hành ATEX / HACCP của dây chuyền.};

  % Chuỗi phạm vi TTC
  \fill[TTCDeepNavy,rounded corners=4pt] (0,0) rectangle (186,35);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.5}{8}\selectfont\bfseries]
    at (7,28) {PHẠM VI TRIỂN KHAI};
  \foreach \x in {46.5,93,139.5}{\draw[white!25!gray] (\x,6) -- (\x,25);}
  \node[align=center,text width=39mm,text=white,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (23.25,15) {MÓNG SÂU\\[-.5mm]{\fontsize{5.8}{7}\selectfont\color{white!70!gray}TẢI TĨNH + TẢI ĐỘNG}};
  \node[align=center,text width=39mm,text=white,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (69.75,15) {KẾT CẤU PEB\\[-.5mm]{\fontsize{5.8}{7}\selectfont\color{white!70!gray}SẢN XUẤT \& LẮP DỰNG}};
  \node[align=center,text width=39mm,text=white,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (116.25,15) {CỤM SILO\\[-.5mm]{\fontsize{5.8}{7}\selectfont\color{white!70!gray}KIỂM SOÁT CAO ĐỘ}};
  \node[align=center,text width=39mm,text=white,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (162.75,15) {HỆ THỐNG PHỤ TRỢ\\[-.5mm]{\fontsize{5.8}{7}\selectfont\color{white!70!gray}BỤI • ĐIỆN • AN TOÀN}};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_25 = r"""% ============================================================
% TRANG 25: CLEANROOM CASE -- DAEYUN ST VINA
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{HỆ THỐNG PHÒNG SẠCH • DAEYUN ST VINA}{Trang 25}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Hồ Sơ Dự Án 04: Nhà Máy Daeyun ST Vina}{Integrated cleanroom systems • KCN Bá Thiện 2, Vĩnh Phúc}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);

  % Phối cảnh ngang + thẻ dữ liệu dọc
  \begin{scope}
    \clip[rounded corners=4pt] (0,157) rectangle (118,219);
    \node[inner sep=0pt] at (59,188)
      {\includegraphics[width=118mm]{../../public/project-assets/daeyun.jpg}};
    \fill[TTCDeepNavy,opacity=.88] (0,157) rectangle (118,168);
    \node[anchor=west,text=white,font=\fontsize{7}{8}\selectfont\bfseries]
      at (4,162.5) {PHỐI CẢNH DỰ ÁN • KCN BÁ THIỆN 2};
  \end{scope}
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,157) rectangle (118,219);

  \fill[TTCDeepNavy,rounded corners=4pt] (122,157) rectangle (186,219);
  \node[anchor=north west,text=TTCCyan,font=\fontsize{7}{8}\selectfont\bfseries]
    at (128,213) {THÔNG TIN DỰ ÁN};
  \node[anchor=north west,text=white,font=\fontsize{13}{14}\selectfont\bfseries]
    at (128,203) {20.000 m$^2$};
  \node[anchor=north west,text=white!70!gray,font=\fontsize{6}{7.2}\selectfont]
    at (128,190) {DIỆN TÍCH SÀN};
  \draw[white!25!gray] (128,184) -- (180,184);
  \node[anchor=north west,text width=48mm,align=left,text=white,
        font=\fontsize{6.8}{8.4}\selectfont]
    at (128,180) {\textbf{Phân loại:} Xưởng sạch\\
                  \textbf{Yêu cầu:} Class 10.000\\
                  \textbf{Tiến độ:} 140 ngày};

  % Bản đồ hệ thống
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (0,149) {BẢN ĐỒ HỆ THỐNG • BỐN LỚP PHẢI HOẠT ĐỘNG NHƯ MỘT};
  \fill[TTCLightBlue,rounded corners=4pt] (0,57) rectangle (186,143);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,57) rectangle (186,143);

  % Trung tâm sản xuất
  \fill[TTCDeepNavy,rounded corners=4pt] (68,88) rectangle (118,116);
  \node[align=center,text=white,text width=42mm,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (93,102) {VÙNG SẢN XUẤT SẠCH\\[-.5mm]
    {\fontsize{6}{7.2}\selectfont\color{white!70!gray}ỔN ĐỊNH • KÍN • CHỐNG TĨNH ĐIỆN}};

  % Bốn mô-đun xung quanh
  \fill[white,rounded corners=3pt] (7,108) rectangle (58,136);
  \draw[TTCBorder,rounded corners=3pt] (7,108) rectangle (58,136);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{7.5}{8.5}\selectfont\bfseries]
    at (12,131) {01 • BAO CHE KÍN};
  \node[anchor=north west,text width=41mm,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont]
    at (12,121) {Panel vách và trần hạn chế xâm nhập bụi, duy trì phân vùng áp suất.};

  \fill[white,rounded corners=3pt] (128,108) rectangle (179,136);
  \draw[TTCBorder,rounded corners=3pt] (128,108) rectangle (179,136);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{7.5}{8.5}\selectfont\bfseries]
    at (133,131) {02 • AHU / HEPA};
  \node[anchor=north west,text width=41mm,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont]
    at (133,121) {Cấp và hồi khí có lọc; cân bằng lưu lượng theo từng khu vực chức năng.};

  \fill[white,rounded corners=3pt] (7,64) rectangle (58,92);
  \draw[TTCBorder,rounded corners=3pt] (7,64) rectangle (58,92);
  \node[anchor=north west,text=TTCRed,font=\fontsize{7.5}{8.5}\selectfont\bfseries]
    at (12,87) {03 • NHIỆT / ẨM};
  \node[anchor=north west,text width=41mm,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont]
    at (12,77) {Kiểm soát mục tiêu $\pm1^\circ$C và $\pm5\%$ theo yêu cầu dây chuyền.};

  \fill[white,rounded corners=3pt] (128,64) rectangle (179,92);
  \draw[TTCBorder,rounded corners=3pt] (128,64) rectangle (179,92);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{7.5}{8.5}\selectfont\bfseries]
    at (133,87) {04 • SÀN ESD};
  \node[anchor=north west,text width=41mm,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont]
    at (133,77) {Vinyl dẫn điện và mạng tiếp địa hỗ trợ kiểm soát phóng tĩnh điện.};

  \draw[-{Latex[length=2mm]},TTCCyan,line width=.9pt] (58,122) -- (68,108);
  \draw[-{Latex[length=2mm]},TTCCyan,line width=.9pt] (128,122) -- (118,108);
  \draw[-{Latex[length=2mm]},TTCCyan,line width=.9pt] (58,78) -- (68,94);
  \draw[-{Latex[length=2mm]},TTCCyan,line width=.9pt] (128,78) -- (118,94);

  % Kết quả ghi nhớ
  \fill[white,rounded corners=3pt] (0,10) rectangle (58,48);
  \draw[TTCBorder,rounded corners=3pt] (0,10) rectangle (58,48);
  \node[align=center,text width=48mm] at (29,29) {
    {\fontsize{10}{11}\selectfont\bfseries\color{TTCRed}CLASS 10.000}\\[-.5mm]
    {\fontsize{6.4}{7.6}\selectfont\color{TTCTextMuted}YÊU CẦU MÔI TRƯỜNG SẠCH}};

  \fill[white,rounded corners=3pt] (64,10) rectangle (122,48);
  \draw[TTCBorder,rounded corners=3pt] (64,10) rectangle (122,48);
  \node[align=center,text width=48mm] at (93,29) {
    {\fontsize{10}{11}\selectfont\bfseries\color{TTCBlue}ESD VINYL}\\[-.5mm]
    {\fontsize{6.4}{7.6}\selectfont\color{TTCTextMuted}BẢO VỆ LINH KIỆN ĐIỆN TỬ}};

  \fill[white,rounded corners=3pt] (128,10) rectangle (186,48);
  \draw[TTCBorder,rounded corners=3pt] (128,10) rectangle (186,48);
  \node[align=center,text width=48mm] at (157,29) {
    {\fontsize{10}{11}\selectfont\bfseries\color{TTCBlue}140 NGÀY}\\[-.5mm]
    {\fontsize{6.4}{7.6}\selectfont\color{TTCTextMuted}TIẾN ĐỘ THEO HỒ SƠ HIỆN TẠI}};

  \fill[TTCDeepNavy,rounded corners=2pt] (0,0) rectangle (186,6);
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_26 = r"""% ============================================================
% TRANG 26: QUALITY DELIVERY -- SUMIDENSO VINA
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{BÀN GIAO CHẤT LƯỢNG • SUMIDENSO VINA}{Trang 26}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Hồ Sơ Dự Án 05: Nhà Máy Dây Cáp Sumidenso}{Quality-led delivery • Automotive wire harness plant • KCN Sông Hậu, Hậu Giang}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);

  % Ảnh và tóm tắt dự án
  \begin{scope}
    \clip[rounded corners=4pt] (0,155) rectangle (64,219);
    \node[inner sep=0pt] at (32,187)
      {\includegraphics[width=64mm,height=64mm]{../../public/project-assets/sumidenso.jpg}};
    \fill[TTCDeepNavy,opacity=.88] (0,155) rectangle (64,166);
    \node[anchor=west,text=white,font=\fontsize{6.8}{8}\selectfont\bfseries]
      at (4,160.5) {ẢNH KHU NHÀ XƯỞNG};
  \end{scope}
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,155) rectangle (64,219);

  \fill[TTCLightBlue,rounded corners=4pt] (68,155) rectangle (186,219);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (68,155) rectangle (186,219);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (75,212) {HỒ SƠ DỰ ÁN};
  \node[anchor=north west,text width=48mm,text=TTCTextDark,font=\fontsize{7.1}{8.8}\selectfont]
    at (75,201) {\textbf{Chủ đầu tư:} Sumitomo Electric\\
                  \textbf{Quy mô:} 15.015 m$^2$\\
                  \textbf{Tiến độ:} 150 ngày};
  \draw[TTCBorder] (129,161) -- (129,208);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (136,212) {TRỌNG TÂM BÀN GIAO};
  \node[anchor=north west,text width=43mm,text=TTCTextDark,font=\fontsize{6.9}{8.5}\selectfont]
    at (136,201) {\textbullet\quad Sprinkler phản ứng nhanh\\[1mm]
                  \textbullet\quad Trạm xử lý nước thải\\[1mm]
                  \textbullet\quad Kiểm soát hồ sơ theo chuẩn quản lý Nhật Bản};

  % Quality gates
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (0,147) {BỐN CỔNG KIỂM SOÁT • CHỈ CHUYỂN BƯỚC KHI ĐỦ BẰNG CHỨNG};
  \fill[white,rounded corners=4pt] (0,88) rectangle (186,141);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,88) rectangle (186,141);
  \draw[TTCBlue,line width=.8pt] (23,122) -- (163,122);

  \foreach \x/\n in {23/01,69/02,117/03,163/04}{
    \fill[white] (\x,122) circle (6mm);
    \draw[TTCBlue,line width=.9pt] (\x,122) circle (6mm);
    \node[text=TTCBlue,font=\fontsize{7}{8}\selectfont\bfseries] at (\x,122) {\n};
  }
  \fill[TTCRed] (23,122) circle (3.2mm);
  \node[text=white,font=\fontsize{6.2}{7}\selectfont\bfseries] at (23,122) {01};

  \node[align=center,text width=38mm] at (23,101) {
    {\fontsize{7.3}{8.5}\selectfont\bfseries\color{TTCBlue}VẬT LIỆU ĐẦU VÀO}\\[-.3mm]
    {\fontsize{5.9}{7.1}\selectfont\color{TTCTextMuted}CO/CQ • mẫu duyệt • truy xuất lô}};
  \node[align=center,text width=38mm] at (69,101) {
    {\fontsize{7.3}{8.5}\selectfont\bfseries\color{TTCBlue}THI CÔNG / ITP}\\[-.3mm]
    {\fontsize{5.9}{7.1}\selectfont\color{TTCTextMuted}Checklist • hold point • nghiệm thu}};
  \node[align=center,text width=38mm] at (117,101) {
    {\fontsize{7.3}{8.5}\selectfont\bfseries\color{TTCBlue}CHẠY THỬ HỆ THỐNG}\\[-.3mm]
    {\fontsize{5.9}{7.1}\selectfont\color{TTCTextMuted}PCCC • xử lý nước thải • liên động}};
  \node[align=center,text width=38mm] at (163,101) {
    {\fontsize{7.3}{8.5}\selectfont\bfseries\color{TTCBlue}HỒ SƠ HOÀN CÔNG}\\[-.3mm]
    {\fontsize{5.9}{7.1}\selectfont\color{TTCTextMuted}As-built • biên bản • hướng dẫn O\&M}};

  % Ma trận yêu cầu -- kiểm soát -- bằng chứng
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (0,80) {TỪ YÊU CẦU ĐẾN HỒ SƠ BÀN GIAO};
  \fill[TTCDeepNavy,rounded corners=3pt] (0,62) rectangle (186,75);
  \node[anchor=west,text=white,font=\fontsize{6.5}{7.8}\selectfont\bfseries] at (6,68.5) {HẠNG MỤC};
  \node[anchor=west,text=white,font=\fontsize{6.5}{7.8}\selectfont\bfseries] at (55,68.5) {ĐIỂM KIỂM SOÁT};
  \node[anchor=west,text=white,font=\fontsize{6.5}{7.8}\selectfont\bfseries] at (126,68.5) {BẰNG CHỨNG BÀN GIAO};

  \fill[TTCLightBlue] (0,47) rectangle (186,62);
  \fill[white] (0,32) rectangle (186,47);
  \fill[TTCLightBlue] (0,17) rectangle (186,32);
  \draw[TTCBorder] (49,17) -- (49,75);
  \draw[TTCBorder] (120,17) -- (120,75);
  \foreach \y in {17,32,47,62}{\draw[TTCBorder] (0,\y) -- (186,\y);}
  \node[anchor=west,text=TTCBlue,font=\fontsize{6.6}{8}\selectfont\bfseries] at (6,54.5) {PCCC SPRINKLER};
  \node[anchor=west,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont] at (55,54.5) {Áp lực • lưu lượng • liên động};
  \node[anchor=west,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont] at (126,54.5) {Biên bản thử và chứng từ thiết bị};
  \node[anchor=west,text=TTCBlue,font=\fontsize{6.6}{8}\selectfont\bfseries] at (6,39.5) {NƯỚC THẢI};
  \node[anchor=west,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont] at (55,39.5) {Vận hành thử • mẫu đầu ra};
  \node[anchor=west,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont] at (126,39.5) {Kết quả thử theo yêu cầu QCVN};
  \node[anchor=west,text=TTCBlue,font=\fontsize{6.6}{8}\selectfont\bfseries] at (6,24.5) {HOÀN THIỆN};
  \node[anchor=west,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont] at (55,24.5) {Mẫu duyệt • punch list • vệ sinh};
  \node[anchor=west,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont] at (126,24.5) {Checklist đóng việc và ảnh nghiệm thu};

  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,11);
  \node[anchor=west,text=white,font=\fontsize{7}{8.5}\selectfont\bfseries]
    at (7,5.5) {15.015 m$^2$};
  \node[text=white!35!gray] at (49,5.5) {|};
  \node[anchor=west,text=white,font=\fontsize{7}{8.5}\selectfont\bfseries]
    at (57,5.5) {150 NGÀY};
  \node[text=white!35!gray] at (95,5.5) {|};
  \node[anchor=west,text=white,font=\fontsize{7}{8.5}\selectfont\bfseries]
    at (103,5.5) {HỆ THỐNG PCCC + XỬ LÝ NƯỚC THẢI};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_27 = r"""% ============================================================
% TRANG 27: PROJECT SPOTLIGHT -- XƯỞNG SẢN XUẤT FOXCONN
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{NHÀ XƯỞNG ĐIỆN TỬ • FOXCONN}{Trang 27}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Hồ Sơ Dự Án 06: Xưởng Sản Xuất Foxconn}{Electronics manufacturing facility • KCN Quế Võ, Bắc Ninh}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);

  % Hero ngang, dùng đúng ảnh Foxconn
  \begin{scope}
    \clip[rounded corners=4pt] (0,151) rectangle (186,219);
    \node[inner sep=0pt] at (93,185)
      {\includegraphics[width=186mm]{../../public/project-assets/foxcon.png}};
    \fill[TTCDeepNavy,opacity=.9] (0,151) rectangle (78,168);
    \node[anchor=west,text=white,font=\fontsize{7}{8}\selectfont\bfseries]
      at (5,159.5) {ẢNH DỰ ÁN • KCN QUẾ VÕ, BẮC NINH};
    \fill[TTCDeepNavy,opacity=.92] (127,151) rectangle (186,219);
    \node[anchor=north west,text=TTCCyan,font=\fontsize{6.8}{8}\selectfont\bfseries]
      at (133,212) {THÔNG TIN DỰ ÁN};
    \node[anchor=north west,text=white,font=\fontsize{14}{15}\selectfont\bfseries]
      at (133,201) {12.000 m$^2$};
    \node[anchor=north west,text=white!70!gray,font=\fontsize{6}{7.2}\selectfont]
      at (133,187) {DIỆN TÍCH NHÀ XƯỞNG};
    \draw[white!25!gray] (133,181) -- (180,181);
    \node[anchor=north west,text width=43mm,text=white,font=\fontsize{6.5}{8}\selectfont]
      at (133,177) {\textbf{Chủ đầu tư:} Foxconn\\
                    \textbf{Quốc gia:} Đài Loan\\
                    \textbf{Vai trò TTC:} Kết cấu thép và lắp dựng};
  \end{scope}
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,151) rectangle (186,219);

  % Luồng triển khai theo zone -- hình thức khác 5 trang trước
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (0,143) {LUỒNG TRIỂN KHAI • KHÓA GIAO DIỆN TRƯỚC KHI LẮP DỰNG};
  \fill[TTCLightBlue,rounded corners=4pt] (0,68) rectangle (186,137);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,68) rectangle (186,137);

  % Bốn thẻ quy trình độc lập; mũi tên chỉ nằm trong khe giữa các thẻ
  \foreach \xa/\xb in {4/43,50/89,96/135,142/182}{
    \fill[white,rounded corners=3pt] (\xa,74) rectangle (\xb,132);
    \draw[TTCBorder,rounded corners=3pt,line width=.65pt] (\xa,74) rectangle (\xb,132);
    \draw[TTCBlue,line width=1.2pt] ({\xa+4},128) -- ({\xb-4},128);
  }
  \foreach \xa/\xb in {43/50,89/96,135/142}{
    \draw[-{Latex[length=2mm]},TTCBlue!65!white,line width=.8pt]
      ({\xa+1},103) -- ({\xb-1},103);
  }

  \fill[TTCRed] (10,122) circle (3.5mm);
  \node[text=white,font=\fontsize{6}{7}\selectfont\bfseries] at (10,122) {01};
  \node[anchor=north west,text width=29mm,align=left,text=TTCBlue,
        font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (9,115) {PHỐI HỢP\\THIẾT KẾ};
  \node[anchor=north west,text width=29mm,align=left,text=TTCTextMuted,
        font=\fontsize{6.1}{7.4}\selectfont]
    at (9,96) {Chốt trục, cao độ và giao diện kết cấu--MEP.};

  \fill[TTCBlue] (56,122) circle (3.5mm);
  \node[text=white,font=\fontsize{6}{7}\selectfont\bfseries] at (56,122) {02};
  \node[anchor=north west,text width=29mm,align=left,text=TTCBlue,
        font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (55,115) {SẢN XUẤT\\CẤU KIỆN};
  \node[anchor=north west,text width=29mm,align=left,text=TTCTextMuted,
        font=\fontsize{6.1}{7.4}\selectfont]
    at (55,96) {Kiểm soát vật liệu, kích thước và liên kết tại xưởng.};

  \fill[TTCBlue] (102,122) circle (3.5mm);
  \node[text=white,font=\fontsize{6}{7}\selectfont\bfseries] at (102,122) {03};
  \node[anchor=north west,text width=29mm,align=left,text=TTCBlue,
        font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (101,115) {LẮP DỰNG\\THEO ZONE};
  \node[anchor=north west,text width=29mm,align=left,text=TTCTextMuted,
        font=\fontsize{6.1}{7.4}\selectfont]
    at (101,96) {Ổn định khung và mở mặt bằng cuốn chiếu.};

  \fill[TTCBlue] (148,122) circle (3.5mm);
  \node[text=white,font=\fontsize{6}{7}\selectfont\bfseries] at (148,122) {04};
  \node[anchor=north west,text width=29mm,align=left,text=TTCBlue,
        font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (147,115) {NGHIỆM THU\\CHUYỂN BƯỚC};
  \node[anchor=north west,text width=29mm,align=left,text=TTCTextMuted,
        font=\fontsize{6.1}{7.4}\selectfont]
    at (147,96) {Kiểm tra hình học, liên kết và hồ sơ trước bao che.};

  % Hai khối nội dung cô đọng
  \fill[white,rounded corners=4pt] (0,19) rectangle (90,60);
  \draw[TTCBorder,rounded corners=4pt] (0,19) rectangle (90,60);
  \node[anchor=north west,text=TTCRed,font=\fontsize{8}{9}\selectfont\bfseries]
    at (6,54) {BÀI TOÁN DỰ ÁN};
  \node[anchor=north west,text width=77mm,align=left,text=TTCTextDark,
        font=\fontsize{6.9}{8.5}\selectfont]
    at (6,44) {Nhà xưởng điện tử yêu cầu mặt bằng lớn, giao diện kết cấu--MEP rõ ràng và trình tự lắp dựng không làm gián đoạn các khu vực kế cận.};

  \fill[TTCLightBlue,rounded corners=4pt] (96,19) rectangle (186,60);
  \draw[TTCBorder,rounded corners=4pt] (96,19) rectangle (186,60);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9}\selectfont\bfseries]
    at (102,54) {PHẢN HỒI CỦA TTC};
  \node[anchor=north west,text width=77mm,align=left,text=TTCTextDark,
        font=\fontsize{6.9}{8.5}\selectfont]
    at (102,44) {Chia zone thi công, kiểm soát cấu kiện từ xưởng và nghiệm thu từng bước để bàn giao mặt bằng theo trình tự rõ ràng.};

  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,12);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.2}{7.4}\selectfont\bfseries]
    at (7,6) {NGUYÊN TẮC TRIỂN KHAI};
  \draw[white!28!gray] (47,3) -- (47,9);
  \node[anchor=west,text=white,font=\fontsize{7}{8.5}\selectfont\bfseries]
    at (54,6) {KHÓA GIAO DIỆN → CHIA ZONE → NGHIỆM THU CHUYỂN BƯỚC};
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
