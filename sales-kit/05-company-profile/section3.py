# -*- coding: utf-8 -*-
"""
Section 3: PEB Strategic Network, Equipment Fleet & FIDIC Project Governance (Pages 11 - 13)
"""

PAGE_11_LEGACY = r"""% ============================================================
% TRANG 11: CHUỖI ĐỐI TÁC SẢN XUẤT PEB 30.000T & KIỂM SOÁT QC
% ============================================================
\pageheaderbar{CHUỖI ĐỐI TÁC SẢN XUẤT PEB 30.000T}{Trang 11}
\pagefooterbar{Trang 11}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.03, scale=2.8, font=\bfseries\sffamily, text=TTCBlue] at ([yshift=-10mm]current page.center) {STRATEGIC PEB PARTNER NETWORK 30000T};
  \draw[TTCBlue!6!white, line width=0.5pt] ([xshift=15mm, yshift=20mm]current page.south west) grid[step=8mm] ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Năng Lực Chuỗi Đối Tác Sản Xuất PEB \& Kiểm Soát Chất Lượng}{Strategic PEB Fabrication Network, Resident QA/QC Supervision \& AWS D1.1 Standards}

% TẦNG 1: MÔ HÌNH HỢP TÁC SẢN XUẤT PEB CHIẾN LƯỢC (Trái) & 6 CÔNG ĐOẠN CNC (Phải)
\noindent
\begin{tabular}{@{}p{86mm}@{\hspace{4mm}}p{96mm}@{}}
  % Cột Trái: Mô hình hợp tác & Kiểm soát
  \begin{tikzpicture}
    \node[
      rounded corners=6pt,
      fill=white,
      draw=TTCBlue!40!white,
      line width=0.9pt,
      minimum width=86mm,
      minimum height=96mm,
      inner sep=6pt,
      text width=78mm,
      align=left
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCBlue} \faHandshake\quad MÔ HÌNH LIÊN KẾT SẢN XUẤT PEB:}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      Tân Thành Công thiết lập mạng lưới đối tác nhà máy gia công kết cấu thép tiền chế (PEB) chiến lược với \textbf{quy mô $>20.000$ m$^2$} tại Hà Nội, đạt \textbf{năng lực cung ứng 30.000 Tấn/năm}.\newline
      \textbullet\ \textbf{TTC Chủ Trì Thiết Kế \& Shop Drawing:} Sử dụng Tekla LOD 400 và AI tối ưu tiết diện dầm trước khi chuyển giao sản xuất.\newline
      \textbullet\ \textbf{Kỹ Sư QC Thường Trú 100\%:} Đội ngũ QA/QC của TTC giám sát trực tiếp tại xưởng đối tác từ phôi thép đầu vào đến nghiệm thu xuất xưởng.\newline
      \textbullet\ \textbf{Chuẩn Hàn Quốc Tế AWS D1.1:} 100\% đường hàn chịu lực được kiểm tra siêu âm NDT (UT/MT) độc lập.\newline
      \textbullet\ \textbf{Lợi Ích Cho Khách Hàng:} Linh hoạt điều phối công suất, không chịu gánh nặng chi phí cố định, tối ưu giá thành 10--15\%.}
    };
  \end{tikzpicture}
  &
  % Cột Phải: 6 Công đoạn gia công CNC khép kín
  \begin{tikzpicture}
    \node[
      rounded corners=6pt,
      fill=TTCLightBlue,
      draw=TTCBorder,
      line width=0.8pt,
      minimum width=96mm,
      minimum height=96mm,
      inner sep=6pt,
      text width=88mm,
      align=left
    ] {
      {\fontsize{8.8}{10.8}\selectfont\bfseries\color{TTCBlue} \faCogs\quad QUY TRÌNH 6 BƯỚC GIA CÔNG CNC KHÉP KÍN:}\\[3pt]
      {\fontsize{7.2}{9.2}\selectfont\color{TTCTextDark}
      \textbf{\color{TTCRed}01. Cắt Plasma CNC:} Cắt phôi thép tự động độ chính xác $\pm 0.5$mm, vát mép dầm chữ V/K tự động.\newline
      \textbf{\color{TTCBlue}02. Gá Đính Thủy Lực:} Máy gá đính tự động, định vị cánh \& bụng dầm chữ H/I với lực ép 20T.\newline
      \textbf{\color{TTCCyan}03. Hàn Hồ Quang Chìm SAW:} Hàn tự động ngấu sâu 100\% đạt chuẩn AWS D1.1, thuốc hàn \& dây hàn chất lượng cao.\newline
      \textbf{\color{TTCBlue}04. Nắn Thẳng Thủy Lực:} Khử triệt để biến dạng nhiệt sau hàn, sai số độ thẳng $<1/1000$ chiều dài.\newline
      \textbf{\color{TTCGold}05. Phun Bi Làm Sạch Sa 2.5:} 8 đầu phun bi thép tự động, tạo độ nhám bám sơn hoàn hảo theo ISO 8501-1.\newline
      \textbf{\color{TTCRed}06. Sơn Hoàn Thiện PCCC:} Phun sơn không có khí Airless, hệ sơn Epoxy Jotun + sơn chống cháy kiểm định PCCC.}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{2mm}

% TẦNG 2: BẢNG TIÊU CHUẨN KỸ THUẬT KIỂM ĐỊNH PEB
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
    {\fontsize{9}{11}\selectfont\bfseries\color{TTCBlue} \faClipboardCheck\quad HỆ THỐNG TIÊU CHUẨN KỸ THUẬT KIỂM ĐỊNH CHẤT LƯỢNG GIA CÔNG PEB:}\\[3pt]
    \begin{tabularx}{\linewidth}{@{}p{56mm}@{\hspace{4mm}}p{56mm}@{\hspace{4mm}}p{56mm}@{}}
      \textbf{\color{TTCRed}1. Tiêu Chuẩn Thép \& Phôi:}\newline
      {\fontsize{6.8}{8.5}\selectfont Phôi thép Q345B, SS400, ASTM A572 Gr.50 nhập khẩu chính hãng Posco, Hòa Phát; đầy đủ chứng chỉ xuất xưởng MTC \& thí nghiệm Las-XD.} &
      \textbf{\color{TTCCyan}2. Tiêu Chuẩn Hàn AWS D1.1:}\newline
      {\fontsize{6.8}{8.5}\selectfont Quy trình hàn WPS/PQR được phê duyệt bởi chuyên gia quốc tế; 100\% thợ hàn có chứng chỉ 3G/4G/6G; kiểm tra siêu âm NDT 100\% mối hàn.} &
      \textbf{\color{TTCBlue}3. Sơn Chống Cháy \& Sa 2.5:}\newline
      {\fontsize{6.8}{8.5}\selectfont Bề mặt làm sạch chuẩn Sa 2.5 SIS 055900; đo chiều dày màng sơn DFT bằng máy Elcometer; thử độ bám dính theo chuẩn ASTM D4541.}
    \end{tabularx}
  };
\end{tikzpicture}

\vspace{2mm}

% TẦNG 3: BĂNG KPI PEB
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
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCRed} 30.000 TẤN} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCCyan} Sa 2.5 SIS} &
      {\fontsize{14}{16}\selectfont\bfseries\color{white} AWS D1.1} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCGold} 100\% NDT} \\
      {\fontsize{7.2}{9}\selectfont Năng Lực Cung Ứng / Năm} &
      {\fontsize{7.2}{9}\selectfont Độ Sạch Bề Mặt Phun Bi} &
      {\fontsize{7.2}{9}\selectfont Chuẩn Hàn Kết Cấu Mỹ} &
      {\fontsize{7.2}{9}\selectfont Siêu Âm Mối Hàn Chịu Lực}
    \end{tabularx}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_11 = r"""% ============================================================
% TRANG 11: PEB SUPPLY & QUALITY GATES
% ============================================================
\begin{tikzpicture}[remember picture, overlay]
  \fill[TTCLightBlue]
    ([xshift=118mm,yshift=-24mm]current page.north west) --
    ([xshift=210mm,yshift=-24mm]current page.north west) --
    ([xshift=210mm,yshift=-108mm]current page.north west) --
    ([xshift=162mm,yshift=-79mm]current page.north west) -- cycle;
  \fill[TTCRed!4!white]
    ([xshift=0mm,yshift=-224mm]current page.north west) --
    ([xshift=62mm,yshift=-254mm]current page.north west) --
    ([xshift=0mm,yshift=-274mm]current page.north west) -- cycle;
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\noindent\makebox[\linewidth][c]{%
  \begin{tikzpicture}[x=1mm,y=1mm]
    \path[use as bounding box] (0,0) rectangle (210,11);
    \fill[TTCDeepNavy] (0,1) rectangle (210,11);
    \fill[TTCRed] (0,0) rectangle (210,1);
    \node[anchor=west, text=white, font=\fontsize{7.5}{9}\selectfont\bfseries]
      at (12,6) {\faBuilding\quad CÔNG TY CỔ PHẦN CÔNG NGHỆ XÂY DỰNG TÂN THÀNH CÔNG \textbullet\ TTC JSC};
    \node[anchor=east, text=TTCCyan, font=\fontsize{7.5}{9}\selectfont\bfseries]
      at (198,6) {CHUỖI CUNG ỨNG PEB \& KIỂM SOÁT CHẤT LƯỢNG};
  \end{tikzpicture}%
}
\vspace{6mm}
\secbrand{Chuỗi Cung Ứng PEB Được Kiểm Soát Bởi TTC}{Strategic Fabrication Network, Resident QA/QC \& Traceable Quality Gates}

\vspace{1mm}
{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
THIẾT KẾ TTC • SẢN XUẤT ĐỐI TÁC • QC THƯỜNG TRÚ\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
Flexible fabrication capacity with TTC-controlled engineering, inspection and release authority.\par}
\vspace{3mm}

% PEB HERO
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,64);
  \clip[rounded corners=3pt] (0,0) rectangle (186,64);
  \node[anchor=center, inner sep=0pt] at (93,32)
    {\includegraphics[width=186mm]{../../public/about1.jpg}};
  \fill[TTCDeepNavy, opacity=0.86] (0,0) rectangle (68,64);
  \fill[TTCDeepNavy, opacity=0.28] (68,0) rectangle (92,64);
  \node[anchor=west, text width=54mm, align=left, text=white] at (8,42) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} STRATEGIC PEB NETWORK}\\[1.3mm]
    {\fontsize{19}{21}\selectfont\bfseries 30.000 TẤN}\\[-0.4mm]
    {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCCyan} NĂNG LỰC CUNG ỨNG / NĂM}\\[1.8mm]
    {\fontsize{7}{8.6}\selectfont\color{white!82!gray}
    TTC làm chủ thiết kế, Shop Drawing và quyền phê duyệt xuất xưởng.}
  };
  \node[
    anchor=south east, rounded corners=3pt,
    fill=white, fill opacity=0.94, text opacity=1,
    draw=TTCCyan, line width=0.65pt,
    minimum width=55mm, minimum height=14mm, align=center
  ] at (179,7) {
    {\fontsize{9.5}{11}\selectfont\bfseries\color{TTCBlue} >20.000 m\textsuperscript{2} • RESIDENT QC}\\[0.6mm]
    {\fontsize{6.5}{7.8}\selectfont\color{TTCTextDark}Partner factory footprint • TTC supervision}
  };
  \draw[white, line width=1pt, rounded corners=3pt] (0.6,0.6) rectangle (185.4,63.4);
  \draw[TTCBorder, line width=0.65pt, rounded corners=3pt] (0,0) rectangle (186,64);
\end{tikzpicture}

\vspace{3mm}

% SIX-STAGE FABRICATION FLOW
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,53);
  \node[anchor=west] at (0,48) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} FABRICATION FLOW}\quad
    {\fontsize{9.5}{11}\selectfont\bfseries\color{TTCBlue} SÁU CÔNG ĐOẠN GIA CÔNG KHÉP KÍN}
  };
  \draw[TTCBlue!30!white, line width=0.85pt] (15,31) -- (171,31);

  \foreach \x/\num in {15/01,46/02,77/03,108/04,139/05,171/06}{
    \fill[white] (\x,31) circle (4.8);
    \draw[TTCBlue!48!white, line width=0.75pt] (\x,31) circle (4.8);
    \node[text=TTCBlue, font=\fontsize{6.8}{8}\selectfont\bfseries] at (\x,31) {\num};
  }
  \fill[TTCRed] (171,31) circle (4.8);
  \node[text=white, font=\fontsize{6.8}{8}\selectfont\bfseries] at (171,31) {06};

  \node[align=center, text width=25mm] at (15,13) {
    {\fontsize{8}{9.2}\selectfont\bfseries\color{TTCBlue} CNC CUTTING}\\[0.6mm]
    {\fontsize{6.3}{7.5}\selectfont Plasma • bevel}
  };
  \node[align=center, text width=25mm] at (46,13) {
    {\fontsize{8}{9.2}\selectfont\bfseries\color{TTCBlue} FIT-UP}\\[0.6mm]
    {\fontsize{6.3}{7.5}\selectfont Hydraulic jig}
  };
  \node[align=center, text width=25mm] at (77,13) {
    {\fontsize{8}{9.2}\selectfont\bfseries\color{TTCBlue} SAW WELD}\\[0.6mm]
    {\fontsize{6.3}{7.5}\selectfont AWS D1.1}
  };
  \node[align=center, text width=25mm] at (108,13) {
    {\fontsize{8}{9.2}\selectfont\bfseries\color{TTCBlue} STRAIGHTEN}\\[0.6mm]
    {\fontsize{6.3}{7.5}\selectfont Hydraulic press}
  };
  \node[align=center, text width=25mm] at (139,13) {
    {\fontsize{8}{9.2}\selectfont\bfseries\color{TTCBlue} BLASTING}\\[0.6mm]
    {\fontsize{6.3}{7.5}\selectfont Sa 2.5}
  };
  \node[align=center, text width=25mm] at (171,13) {
    {\fontsize{8}{9.2}\selectfont\bfseries\color{TTCRed} COATING}\\[0.6mm]
    {\fontsize{6.3}{7.5}\selectfont Epoxy • fireproof}
  };
\end{tikzpicture}

\vspace{3mm}

% QUALITY GATES
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,53);

  \fill[white, rounded corners=4pt] (0,0) rectangle (58,53);
  \draw[TTCBorder, line width=0.65pt, rounded corners=4pt] (0,0) rectangle (58,53);
  \node[anchor=north west, text width=48mm, align=left] at (5,47) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} QUALITY GATE 01}\\[0.8mm]
    {\fontsize{10}{11.5}\selectfont\bfseries\color{TTCBlue} MATERIAL RELEASE}\\[1.3mm]
    {\fontsize{7}{8.5}\selectfont\color{TTCTextDark}
    \textcolor{TTCCyan}{\faCheckCircle}\ MTC, CO/CQ và truy xuất lô thép.\\[0.7mm]
    \textcolor{TTCCyan}{\faCheckCircle}\ Q345B • SS400 • ASTM A572 Gr.50.\\[0.7mm]
    \textcolor{TTCCyan}{\faCheckCircle}\ Thí nghiệm cơ lý độc lập.}
  };

  \fill[TTCLightBlue, rounded corners=4pt] (64,0) rectangle (122,53);
  \draw[TTCBlue!50!white, line width=0.7pt, rounded corners=4pt] (64,0) rectangle (122,53);
  \node[anchor=north west, text width=48mm, align=left] at (69,47) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} QUALITY GATE 02}\\[0.8mm]
    {\fontsize{10}{11.5}\selectfont\bfseries\color{TTCBlue} WELD ACCEPTANCE}\\[1.3mm]
    {\fontsize{7}{8.5}\selectfont\color{TTCTextDark}
    \textcolor{TTCBlue}{\faCheckCircle}\ WPS/PQR được phê duyệt.\\[0.7mm]
    \textcolor{TTCBlue}{\faCheckCircle}\ Thợ hàn chứng chỉ 3G/4G/6G.\\[0.7mm]
    \textcolor{TTCBlue}{\faCheckCircle}\ NDT UT/MT mối hàn chịu lực.}
  };

  \fill[white, rounded corners=4pt] (128,0) rectangle (186,53);
  \draw[TTCRed!65!white, line width=0.75pt, rounded corners=4pt] (128,0) rectangle (186,53);
  \node[anchor=north west, text width=48mm, align=left] at (133,47) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCRed} QUALITY GATE 03}\\[0.8mm]
    {\fontsize{10}{11.5}\selectfont\bfseries\color{TTCBlue} FINISH \& RELEASE}\\[1.3mm]
    {\fontsize{7}{8.5}\selectfont\color{TTCTextDark}
    \textcolor{TTCRed}{\faCheckCircle}\ Làm sạch Sa 2.5 theo ISO 8501-1.\\[0.7mm]
    \textcolor{TTCRed}{\faCheckCircle}\ DFT bằng Elcometer.\\[0.7mm]
    \textcolor{TTCRed}{\faCheckCircle}\ Sơn Epoxy và chống cháy PCCC.}
  };
\end{tikzpicture}

\vspace{3mm}

% TTC RELEASE AUTHORITY
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,30);
  \fill[TTCLightBlue, rounded corners=4pt] (0,0) rectangle (186,30);
  \draw[TTCBorder, line width=0.65pt, rounded corners=4pt] (0,0) rectangle (186,30);
  \node[anchor=west, align=left] at (6,15) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} TTC CONTROL MODEL}\\[0.7mm]
    {\fontsize{9.3}{10.8}\selectfont\bfseries\color{TTCBlue} QUYỀN PHÊ DUYỆT XUẤT XƯỞNG}
  };
  \node[text=TTCRed] at (55,15) {\faChevronRight};
  \node[align=center] at (76,15) {
    {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCBlue} DESIGN \& SHOP}\\[0.5mm]
    {\fontsize{6.3}{7.5}\selectfont TTC engineering}
  };
  \node[text=TTCRed] at (97,15) {\faChevronRight};
  \node[align=center] at (117,15) {
    {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCBlue} RESIDENT QC}\\[0.5mm]
    {\fontsize{6.3}{7.5}\selectfont At partner factory}
  };
  \node[text=TTCRed] at (137,15) {\faChevronRight};
  \node[align=center] at (158,15) {
    {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCRed} RELEASE NOTE}\\[0.5mm]
    {\fontsize{6.3}{7.5}\selectfont Ready for erection}
  };
\end{tikzpicture}
\vfill
\noindent\makebox[\linewidth][c]{%
  \begin{tikzpicture}[x=1mm,y=1mm]
    \path[use as bounding box] (0,0) rectangle (210,9);
    \begin{scope}[yshift=-20mm]
    \fill[TTCDeepNavy] (0,0) rectangle (210,8);
    \fill[TTCCyan] (0,8) rectangle (210,9);
    \node[anchor=west, text=white, font=\fontsize{6.8}{8}\selectfont]
      at (12,4) {\faPhone*\ +84 976 447 766 \quad\textbullet\quad \faEnvelope\ info@tanthanhcongjsc.com \quad\textbullet\quad \faGlobe\ https://tanthanhcongjsc.com};
    \node[anchor=east, text=white, font=\fontsize{7}{8}\selectfont\bfseries]
      at (198,4) {Trang 11};
    \end{scope}
  \end{tikzpicture}%
}
\end{minipage}
\newpage
"""

PAGE_12_LEGACY = r"""% ============================================================
% TRANG 12: ĐỘI XE MÁY THIẾT BỊ CƠ GIỚI >300 TỶ & CẨU NÂNG 100T
% ============================================================
\pageheaderbar{ĐỘI XE MÁY \& THIẾT BỊ CƠ GIỚI}{Trang 12}
\pagefooterbar{Trang 12}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.03, scale=2.8, font=\bfseries\sffamily, text=TTCBlue] at ([yshift=-10mm]current page.center) {HEAVY MACHINERY FLEET \& EQUIPMENT};
  \draw[TTCBlue!6!white, line width=0.5pt] ([xshift=15mm, yshift=20mm]current page.south west) grid[step=8mm] ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Đội Xe Máy Cơ Giới Hiện Trường $>300$ Tỷ VNĐ}{Directly Owned Heavy Machinery Fleet, 100T Cranes, Aerial Platforms \& Mobile Roll-Forming Lines}

% TẦNG 1: BẢNG DANH MỤC THIẾT BỊ CƠ GIỚI
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
    {\fontsize{9.5}{11.5}\selectfont\bfseries\color{TTCBlue} \faTruckLoading\quad DANH MỤC XE MÁY \& THIẾT BỊ CƠ GIỚI HIỆN TRƯỜNG CHUYÊN DỤNG:}\\[3pt]
    \renewcommand{\arraystretch}{1.12}
    {\fontsize{7.5}{9.5}\selectfont
    \begin{tabularx}{\linewidth}{@{}p{38mm}p{48mm}|c|X@{}}
      \toprule
      \textbf{Nhóm Thiết Bị} & \textbf{Chủng Loại / Thương Hiệu} & \textbf{Số Lượng} & \textbf{Năng Lực Phục Vụ Hiện Trường} \\
      \midrule
      \textbf{Cẩu Bánh Lốp \& Tự Hành} & Kato, Tadano, Sany (25T -- 100T) & \textbf{12 Chiếc} & Lắp dựng dầm kèo thép nhịp lớn $>60$m an toàn \\
      \textbf{Xe Nâng Người Boomlift} & Genie, JLG (Chiều cao 18m -- 28m) & \textbf{28 Chiếc} & Thi công tôn mái Seamlock, panel vách, MEP trên cao \\
      \textbf{San Lấp \& Nền Móng} & Máy xúc Komatsu, máy lu rung Sakai 14T & \textbf{16 Chiếc} & Thi công hạ tầng KCN, ép cọc chịu tải nặng \\
      \textbf{Bơm Bê Tông \& Bồn} & Putzmeister cần 38m--52m, xe bồn chuyên dụng & \textbf{08 Chiếc} & Đổ sàn bê tông phẳng Laser Screed liên tục \\
      \textbf{Máy Cán Tôn Hiện Trường} & Máy cán tôn Cliplock / Seamlock di động & \textbf{04 Dàn} & Cán dải tôn dài $>100$m trực tiếp, triệt tiêu dột \\
      \textbf{Máy Trắc Đạc Laser 3D} & Toàn đạc điện tử Leica, cân bằng Laser 3D & \textbf{18 Bộ} & Định vị tim trục móng, độ thẳng bu-lông sai số $<2$mm \\
      \bottomrule
    \end{tabularx}}
  };
\end{tikzpicture}

\vspace{2mm}

% TẦNG 2: 3 CARD ƯU THẾ LÀM CHỦ CƠ GIỚI
\noindent
\begin{tabular}{@{}p{59mm}@{\hspace{3.5mm}}p{59mm}@{\hspace{3.5mm}}p{59mm}@{}}
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=59mm, minimum height=48mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCRed} \faClock\ Làm Chủ Tiến Độ 24/7}\\[2pt]
      {\fontsize{6.8}{8.5}\selectfont\color{TTCTextDark}
      \textbullet\ Không phụ thuộc đơn vị cho thuê ngoài.\newline
      \textbullet\ Sẵn sàng thi công 3 ca liên tục kể cả ban đêm.\newline
      \textbullet\ Điều động thiết bị khẩn cấp tới mọi công trường trong vòng 12h.\newline
      \textbullet\ Rút ngắn 30\% thời gian lắp dựng dầm kèo.}
    };
  \end{tikzpicture} &
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=59mm, minimum height=48mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCCyan} \faShield*\ 100\% Kiểm Định An Toàn}\\[2pt]
      {\fontsize{6.8}{8.5}\selectfont\color{TTCTextDark}
      \textbullet\ 100\% thiết bị có giấy kiểm định kỹ thuật an toàn còn hiệu lực.\newline
      \textbullet\ Lái cẩu, thợ vận hành có chứng chỉ nghề chuẩn quốc gia.\newline
      \textbullet\ Bảo dưỡng định kỳ theo tiêu chuẩn khuyến nghị của hãng sản xuất.\newline
      \textbullet\ Triệt tiêu mọi nguy cơ sự cố rơi cẩu.}
    };
  \end{tikzpicture} &
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=59mm, minimum height=48mm, inner sep=4pt, text width=53mm, align=left] {
      {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCBlue} \faTools\ Cán Tôn Mái Di Động}\\[2pt]
      {\fontsize{6.8}{8.5}\selectfont\color{TTCTextDark}
      \textbullet\ Dàn máy cán tôn Seamlock đưa thẳng lên sàn mái thi công.\newline
      \textbullet\ Cán tấm tôn dài không mối nối lên đến 120m.\newline
      \textbullet\ Đai kẹp seamlock ẩn không xuyên thủng bề mặt tôn.\newline
      \textbullet\ Chống thấm dột 100\% tuyệt đối dưới bão cấp 12.}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{2mm}

% TẦNG 3: BĂNG KPI THIẾT BỊ
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
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCRed} >300 TỶ} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCCyan} 85+ THIẾT BỊ} &
      {\fontsize{14}{16}\selectfont\bfseries\color{white} 100 TẤN} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCGold} 100\% KIỂM ĐỊNH} \\
      {\fontsize{7.2}{9}\selectfont Giá Trị Đội Xe Máy} &
      {\fontsize{7.2}{9}\selectfont Xe Máy Chuyên Dụng} &
      {\fontsize{7.2}{9}\selectfont Sức Nâng Cẩu Lớn Nhất} &
      {\fontsize{7.2}{9}\selectfont Đạt Chuẩn An Toàn}
    \end{tabularx}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_13_LEGACY = r"""% ============================================================
% TRANG 13: QUY TRÌNH QUẢN TRỊ DỰ ÁN CHUẨN FIDIC 8 GIAI ĐOẠN [TRANG MỚI]
% ============================================================
\pageheaderbar{QUY TRÌNH QUẢN TRỊ DỰ ÁN FIDIC}{Trang 13}
\pagefooterbar{Trang 13}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.03, scale=2.8, font=\bfseries\sffamily, text=TTCBlue] at ([yshift=-10mm]current page.center) {FIDIC TURNKEY PROJECT GOVERNANCE};
  \draw[TTCBlue!6!white, line width=0.5pt] ([xshift=15mm, yshift=20mm]current page.south west) grid[step=8mm] ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Quy Trình Quản Trị Dự Án Chuẩn FIDIC Silver Book 8 Giai Đoạn}{Turnkey EPC Fast-Track Methodology, Stage-Gate Governance \& Single-Point Accountability}

% TẦNG 1: SƠ ĐỒ FLOWCHART 8 GIAI ĐOẠN TIKZ (Single Canvas)
\noindent
\begin{tikzpicture}[
  box/.style={rounded corners=4pt, fill=white, draw=TTCBlue!60!white, line width=0.8pt, align=left, inner sep=3.5pt, font=\fontsize{6.5}{7.8}\selectfont},
  title/.style={font=\fontsize{7.2}{8.5}\selectfont\bfseries},
  arrow/.style={-{Stealth[scale=0.9]}, TTCBlue, line width=1pt}
]
  \draw[TTCBlue!40!white, line width=0.9pt, fill=white, rounded corners=6pt] (0,0) rectangle (18.6, 10.2);

  % Row 1: Giai đoạn 1 to 4
  \node[box, text width=38mm] (g1) at (2.4, 8.8) {
    {\color{TTCRed}\title GĐ 01: Tiếp Nhận \& Khảo Sát}\newline
    \textbullet\ Khảo sát địa chất, địa hình 3D.\newline
    \textbullet\ Thu thập nhu cầu công năng FDI.\newline
    \textbullet\ Lập báo cáo tiền khả thi FS.
  };

  \node[box, text width=38mm] (g2) at (7.0, 8.8) {
    {\color{TTCBlue}\title GĐ 02: Pháp Lý \& Quy Hoạch}\newline
    \textbullet\ Tư vấn cấp phép IRC, ERC.\newline
    \textbullet\ Lập quy hoạch 1/500, ĐTM.\newline
    \textbullet\ Thẩm duyệt thiết kế PCCC \& GPXD.
  };

  \node[box, text width=38mm] (g3) at (11.6, 8.8) {
    {\color{TTCCyan}\title GĐ 03: Thiết Kế VE \& BIM 5D}\newline
    \textbullet\ Thiết kế Tekla LOD 400.\newline
    \textbullet\ AI tối ưu tiết diện dầm Tapered.\newline
    \textbullet\ Rà soát xung đột Zero-Clash.
  };

  \node[box, text width=38mm] (g4) at (16.2, 8.8) {
    {\color{TTCGold}\title GĐ 04: Chuỗi Cung Ứng \& PEB}\newline
    \textbullet\ Đấu thầu vật tư chiến lược Tier-1.\newline
    \textbullet\ Điều phối gia công xưởng đối tác.\newline
    \textbullet\ QC thường trú kiểm tra AWS D1.1.
  };

  % Row 2: Giai đoạn 5 to 8
  \node[box, text width=38mm] (g5) at (16.2, 5.0) {
    {\color{TTCBlue}\title GĐ 05: Thi Công Nền Móng}\newline
    \textbullet\ Ép cọc ly tâm / khoan nhồi.\newline
    \textbullet\ Thi công đài giằng, móng chịu tải.\newline
    \textbullet\ Triển khai hạ tầng cấp thoát nước.
  };

  \node[box, text width=38mm] (g6) at (11.6, 5.0) {
    {\color{TTCRed}\title GĐ 06: Lắp Dựng \& Cơ Điện}\newline
    \textbullet\ Lắp dựng kết cấu thép dàn cẩu 100T.\newline
    \textbullet\ Lợp tôn Seamlock \& panel vách.\newline
    \textbullet\ Lắp đặt trạm biến áp, HVAC, PCCC.
  };

  \node[box, text width=38mm] (g7) at (7.0, 5.0) {
    {\color{TTCCyan}\title GĐ 07: Nghiệm Thu \& PCCC}\newline
    \textbullet\ Nghiệm thu ITP 4 tầng cùng TVGS.\newline
    \textbullet\ Nghiệm thu PCCC Cảnh sát PCCC.\newline
    \textbullet\ Chạy thử liên động hệ thống MEP.
  };

  \node[box, text width=38mm] (g8) at (2.4, 5.0) {
    {\color{TTCGold}\title GĐ 08: Bàn Giao \& O\&M}\newline
    \textbullet\ Chìa khóa trao tay As-Built 3D.\newline
    \textbullet\ Chuyển giao Smart Digital Twin.\newline
    \textbullet\ Bảo hành 24T \& bảo trì O\&M 30+ năm.
  };

  % Connecting Arrows
  \draw[arrow] (g1) -- (g2);
  \draw[arrow] (g2) -- (g3);
  \draw[arrow] (g3) -- (g4);
  \draw[arrow] (g4) -- (g5);
  \draw[arrow] (g5) -- (g6);
  \draw[arrow] (g6) -- (g7);
  \draw[arrow] (g7) -- (g8);

  % Bottom summary ribbon inside canvas
  \node[anchor=south, rounded corners=4pt, fill=TTCDeepNavy!95!black, draw=TTCCyan!80!white, line width=0.8pt, text=white, minimum width=176mm, minimum height=14mm, inner sep=4pt] at (9.3, 0.4) {
    \begin{tabularx}{170mm}{@{}Y|Y|Y|Y@{}}
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCRed} FAST-TRACK} &
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCCyan} FIDIC SILVER} &
      {\fontsize{8}{9.5}\selectfont\bfseries\color{white} 0 PHÁT SINH} &
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCGold} DIGITAL TWIN} \\
      {\fontsize{6.5}{7.8}\selectfont Rút Ngắn 30\% Tiến Độ} &
      {\fontsize{6.5}{7.8}\selectfont Chuẩn Mực Hợp Đồng} &
      {\fontsize{6.5}{7.8}\selectfont Hợp Đồng Lump-sum} &
      {\fontsize{6.5}{7.8}\selectfont Bàn Giao Bản Sao Số}
    \end{tabularx}
  };
\end{tikzpicture}

\vspace{2mm}

% TẦNG 2: 3 NGUYÊN TẮC QUẢN TRỊ DỰ ÁN FIDIC
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
    {\fontsize{9}{11}\selectfont\bfseries\color{TTCBlue} \faShield*\quad 3 NGUYÊN TẮC QUẢN TRỊ BẤT BIẾN THEO CHUẨN FIDIC TURNKEY:}\\[3pt]
    \begin{tabularx}{\linewidth}{@{}p{56mm}@{\hspace{4mm}}p{56mm}@{\hspace{4mm}}p{56mm}@{}}
      \textbf{\color{TTCRed}1. Quản Trị Đường Găng (CPM):}\newline
      {\fontsize{6.8}{8.5}\selectfont Lập tiến độ tổng thể bằng Primavera P6 / MS Project, kiểm soát đường găng hàng tuần, kích hoạt biện pháp tăng ca ngay khi có nguy cơ trễ dù chỉ 1 ngày.} &
      \textbf{\color{TTCCyan}2. Môi Trường Dữ Liệu Chung (CDE):}\newline
      {\fontsize{6.8}{8.5}\selectfont 100\% bản vẽ, hồ sơ RFI, biên bản nghiệm thu ITP được đồng bộ trực tuyến trên nền tảng đám mây, minh bạch tuyệt đối giữa Chủ đầu tư, TVGS và TTC.} &
      \textbf{\color{TTCBlue}3. Cam Kết Trọn Gói 0 Phát Sinh:}\newline
      {\fontsize{6.8}{8.5}\selectfont Hợp đồng Lump-sum Turnkey bảo vệ tối đa ngân sách của Chủ đầu tư; mọi rủi ro kỹ thuật và trượt giá vật tư do TTC hoàn toàn chịu trách nhiệm.}
    \end{tabularx}
  };
\end{tikzpicture}

\vspace{2mm}

% TẦNG 3: BĂNG KPI QUẢN TRỊ
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
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCRed} 8 GIAI ĐOẠN} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCCyan} 100\% CDE} &
      {\fontsize{14}{16}\selectfont\bfseries\color{white} FIDIC TURNKEY} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCGold} 24 THÁNG} \\
      {\fontsize{7.2}{9}\selectfont Quy Trình Khép Kín} &
      {\fontsize{7.2}{9}\selectfont Quản Trị Đám Mây} &
      {\fontsize{7.2}{9}\selectfont Chuẩn Hợp Đồng Quốc Tế} &
      {\fontsize{7.2}{9}\selectfont Bảo Hành Toàn Diện}
    \end{tabularx}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_12 = r"""% ============================================================
% TRANG 12: THIẾT BỊ THEO GÓI HUY ĐỘNG
% ============================================================
\pageheaderbar{THIẾT BỊ CƠ GIỚI \& HUY ĐỘNG HIỆN TRƯỜNG}{Trang 12}
\pagefooterbar{Trang 12}

\begin{tikzpicture}[remember picture, overlay]
  \fill[TTCLightBlue]
    ([xshift=137mm,yshift=-31mm]current page.north west) --
    ([xshift=210mm,yshift=-31mm]current page.north west) --
    ([xshift=210mm,yshift=-104mm]current page.north west) -- cycle;
  \draw[TTCBlue!8!white, line width=12pt]
    ([xshift=151mm,yshift=42mm]current page.south west) --
    ([xshift=205mm,yshift=96mm]current page.south west);
  \draw[TTCRed!8!white, line width=3pt]
    ([xshift=160mm,yshift=42mm]current page.south west) --
    ([xshift=205mm,yshift=87mm]current page.south west);
  % Faint industrial mobilization silhouette — replaces the old square grid
  \begin{scope}[shift={(current page.south west)},x=1mm,y=1mm,opacity=.48]
    \draw[TTCBlue!18!white, line width=.7pt] (12,13) -- (198,13);
    \fill[TTCBlue!2!white] (14,13) -- (14,34) -- (34,43) -- (54,34) --
      (54,13) -- cycle;
    \draw[TTCBlue!17!white, line width=.65pt] (14,13) -- (14,34) -- (34,43) --
      (54,34) -- (54,13);
    \foreach \x in {19,27,35,43,51}{\draw[TTCBlue!13!white] (\x,13) -- (\x,34);}
    \fill[TTCBlue!2!white] (61,13) rectangle (133,31);
    \draw[TTCBlue!17!white, line width=.65pt] (61,13) rectangle (133,31);
    \foreach \x in {73,85,97,109,121}{\draw[TTCBlue!12!white] (\x,13) -- (\x,31);}
    \draw[TTCBlue!17!white] (61,22) -- (133,22);
    % tower crane / lifting cue
    \draw[TTCBlue!20!white, line width=.85pt] (151,13) -- (151,51);
    \draw[TTCBlue!18!white] (146,13) -- (151,51) -- (156,13);
    \draw[TTCBlue!20!white, line width=.85pt] (151,48) -- (198,48);
    \draw[TTCBlue!17!white] (151,48) -- (177,39) -- (198,48);
    \draw[TTCRed!22!white, line width=.7pt] (184,48) -- (184,25);
    \draw[TTCRed!22!white] (181,25) -- (187,25);
  \end{scope}
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Năng Lực Thiết Bị Theo Gói Huy Động}{Right Equipment, Right Workfront, Right Time}

{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
43+ THIẾT BỊ • 4 GÓI NHIỆM VỤ • MỘT ĐẦU MỐI ĐIỀU PHỐI\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
Danh mục được tinh gọn theo năng lực thực thi, ưu tiên khả năng điều động, kiểm định và hiệu suất tại công trường.\par}
\vspace{3mm}

% HERO — SITE MOBILIZATION
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,58);
  \clip[rounded corners=3pt] (0,0) rectangle (186,58);
  \node[anchor=center, inner sep=0pt] at (93,29)
    {\includegraphics[width=186mm]{../../public/c_level_site_inspection.jpg}};
  \fill[TTCDeepNavy, opacity=0.88] (0,0) rectangle (68,58);
  \fill[TTCDeepNavy, opacity=0.35] (68,0) rectangle (94,58);
  \node[anchor=west, text width=54mm, align=left, text=white] at (8,38) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} MOBILIZATION CONTROL}\\[1.5mm]
    {\fontsize{21}{22}\selectfont\bfseries 43+}\\[-0.5mm]
    {\fontsize{9}{10.5}\selectfont\bfseries THIẾT BỊ SẴN SÀNG}\\[1.7mm]
    {\fontsize{7}{8.5}\selectfont\color{white!82!gray}
    Điều phối theo đường găng và mặt bằng thi công, không dàn trải nguồn lực.}
  };
  \node[rounded corners=2pt, fill=white, text=TTCBlue, align=center,
        minimum width=31mm, minimum height=16mm] at (129,17) {
    {\fontsize{13}{14}\selectfont\bfseries 100T}\\[-0.4mm]
    {\fontsize{6.2}{7.4}\selectfont SỨC NÂNG TỐI ĐA}
  };
  \node[rounded corners=2pt, fill=TTCRed, text=white, align=center,
        minimum width=35mm, minimum height=16mm] at (167,17) {
    {\fontsize{11}{12}\selectfont\bfseries 100\%}\\[-0.4mm]
    {\fontsize{6.2}{7.4}\selectfont KIỂM ĐỊNH HIỆU LỰC}
  };
\end{tikzpicture}

\vspace{3mm}

% FOUR MISSION PACKAGES
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,50);
  \foreach \x/\accent in {0/TTCRed,47.5/TTCCyan,95/TTCBlue,142.5/TTCGold}{
    \fill[white, rounded corners=2pt] (\x,0) rectangle +(43.5,50);
    \draw[TTCBorder, rounded corners=2pt, line width=.55pt] (\x,0) rectangle +(43.5,50);
    \fill[\accent, rounded corners=2pt] (\x,46) rectangle +(43.5,4);
  }
  \node[anchor=north west, text width=35mm, align=left] at (4,43) {
    {\fontsize{15}{16}\selectfont\bfseries\color{TTCRed} 20}\\[-.5mm]
    {\fontsize{7.4}{8.5}\selectfont\bfseries\color{TTCBlue} NÂNG HẠ \& TIẾP CẬN}\\[1mm]
    {\fontsize{6.6}{8}\selectfont\color{TTCTextDark}
    06 cẩu tự hành 25--100T\newline
    14 xe Boomlift 18--28m\newline
    Lắp dựng thép, mái và MEP trên cao.}
  };
  \node[anchor=north west, text width=35mm, align=left] at (51.5,43) {
    {\fontsize{15}{16}\selectfont\bfseries\color{TTCCyan} 12}\\[-.5mm]
    {\fontsize{7.4}{8.5}\selectfont\bfseries\color{TTCBlue} NỀN \& BÊ TÔNG}\\[1mm]
    {\fontsize{6.6}{8}\selectfont\color{TTCTextDark}
    08 máy xúc, lu nền\newline
    04 bơm và xe bồn bê tông\newline
    Hạ tầng, nền móng và sàn công nghiệp.}
  };
  \node[anchor=north west, text width=35mm, align=left] at (99,43) {
    {\fontsize{15}{16}\selectfont\bfseries\color{TTCBlue} 02}\\[-.5mm]
    {\fontsize{7.4}{8.5}\selectfont\bfseries\color{TTCBlue} MÁI \& BAO CHE}\\[1mm]
    {\fontsize{6.6}{8}\selectfont\color{TTCTextDark}
    02 dàn cán tôn di động\newline
    Cliplock / Seamlock tại chỗ\newline
    Dải tôn dài, hạn chế mối nối và thấm dột.}
  };
  \node[anchor=north west, text width=35mm, align=left] at (146.5,43) {
    {\fontsize{15}{16}\selectfont\bfseries\color{TTCGold} 09}\\[-.5mm]
    {\fontsize{7.4}{8.5}\selectfont\bfseries\color{TTCBlue} TRẮC ĐẠC \& QA}\\[1mm]
    {\fontsize{6.6}{8}\selectfont\color{TTCTextDark}
    09 bộ Leica / Laser 3D\newline
    Kiểm soát tim trục và cao độ\newline
    Sai số mục tiêu dưới 2mm.}
  };
\end{tikzpicture}

\vspace{3mm}

% DEPLOYMENT SEQUENCE
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,42);
  \fill[TTCLightBlue, rounded corners=3pt] (0,0) rectangle (186,42);
  \draw[TTCBorder, rounded corners=3pt, line width=.6pt] (0,0) rectangle (186,42);
  \node[anchor=west, font=\fontsize{8}{9.5}\selectfont\bfseries, text=TTCBlue] at (7,35)
    {\faClock\quad NHỊP HUY ĐỘNG THEO ĐƯỜNG GĂNG DỰ ÁN};
  \draw[TTCBlue!35!white, line width=1pt] (19,19) -- (167,19);
  \foreach \x/\n/\t/\s in {
    21/01/NỀN MÓNG/Khảo sát • đào đắp • bê tông,
    69/02/KẾT CẤU/Cẩu lắp • tiếp cận trên cao,
    117/03/BAO CHE/Cán tôn • mái • hoàn thiện,
    165/04/NGHIỆM THU/Trắc đạc • kiểm định • bàn giao}{
      \fill[white] (\x,19) circle (4.7);
      \draw[TTCBlue, line width=.8pt] (\x,19) circle (4.7);
      \node[font=\fontsize{6.8}{8}\selectfont\bfseries, text=TTCRed] at (\x,19) {\n};
      \node[anchor=north, align=center, text width=38mm] at (\x,12) {
        {\fontsize{6.8}{8}\selectfont\bfseries\color{TTCBlue} \t}\\[-.3mm]
        {\fontsize{5.8}{7}\selectfont\color{TTCTextMuted} \s}
      };
  }
\end{tikzpicture}

\vspace{3mm}

% ASSURANCE STRIP
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,29);
  \fill[TTCDeepNavy, rounded corners=3pt] (0,0) rectangle (186,29);
  \foreach \x in {46.5,93,139.5}{\draw[white!35!gray] (\x,6) -- (\x,23);}
  \node[align=center, text=white] at (23.25,15) {{\fontsize{9}{10}\selectfont\bfseries\color{TTCRed} 12 GIỜ}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont Điều Động Khẩn Cấp}};
  \node[align=center, text=white] at (69.75,15) {{\fontsize{9}{10}\selectfont\bfseries\color{TTCCyan} CHỨNG CHỈ}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont Vận Hành Đúng Chuẩn}};
  \node[align=center, text=white] at (116.25,15) {{\fontsize{9}{10}\selectfont\bfseries BẢO DƯỠNG}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont Theo Khuyến Nghị Hãng}};
  \node[align=center, text=white] at (162.75,15) {{\fontsize{9}{10}\selectfont\bfseries\color{TTCGold} NHẬT KÝ SỐ}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont Trạng Thái Theo Thời Gian}};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_13 = r"""% ============================================================
% TRANG 13: QUẢN TRỊ DỰ ÁN STAGE-GATE
% ============================================================
\pagefooterbar{Trang 13}

\begin{tikzpicture}[remember picture, overlay]
  \fill[TTCLightBlue]
    ([xshift=118mm,yshift=-32mm]current page.north west) --
    ([xshift=210mm,yshift=-32mm]current page.north west) --
    ([xshift=210mm,yshift=-118mm]current page.north west) -- cycle;
  \node[opacity=.035, font=\fontsize{62}{64}\selectfont\bfseries, text=TTCBlue,
        rotate=90] at ([xshift=-10mm,yshift=18mm]current page.east) {GATE};
  % Four translucent decision chevrons continue the process into the footer
  \begin{scope}[shift={(current page.south west)},x=1mm,y=1mm,opacity=.42]
    \foreach \x/\c in {15/TTCRed,60/TTCCyan,105/TTCBlue,150/TTCGold}{
      \fill[\c!7!white] (\x,14) -- ++(31,0) -- ++(10,14) -- ++(-10,14) --
        ++(-31,0) -- ++(10,-14) -- cycle;
    }
    \node[text=TTCRed!35!white,font=\fontsize{7}{8}\selectfont\bfseries] at (35,28) {DEFINE};
    \node[text=TTCCyan!40!white,font=\fontsize{7}{8}\selectfont\bfseries] at (80,28) {ENGINEER};
    \node[text=TTCBlue!35!white,font=\fontsize{7}{8}\selectfont\bfseries] at (125,28) {BUILD};
    \node[text=TTCGold!40!white,font=\fontsize{7}{8}\selectfont\bfseries] at (170,28) {HANDOVER};
  \end{scope}
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\pageheaderbar{QUẢN TRỊ DỰ ÁN EPC THEO STAGE-GATE}{Trang 13}
\secbrand{Quản Trị Dự Án EPC Theo 4 Pha Kiểm Soát}{FIDIC Turnkey Governance, Decision Gates \& Single-Point Accountability}

{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
MỖI GIAI ĐOẠN CÓ ĐẦU RA • MỖI CHUYỂN PHA CÓ PHÊ DUYỆT\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
Tám bước triển khai được gom thành bốn pha quản trị, giúp Chủ đầu tư nhìn rõ quyết định, trách nhiệm và trạng thái dự án.\par}
\vspace{3mm}

% FOUR PHASES / FOUR GATES
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,103);

  % PHASE 01
  \fill[white, rounded corners=2pt] (0,0) rectangle (43.5,103);
  \draw[TTCBorder, rounded corners=2pt, line width=.65pt] (0,0) rectangle (43.5,103);
  \fill[TTCDeepNavy, rounded corners=2pt] (0,84) rectangle (43.5,103);
  \node[anchor=west, text=white] at (4,94) {{\fontsize{7}{8}\selectfont 01}\quad{\fontsize{10}{11}\selectfont\bfseries DEFINE}};
  \node[anchor=north west, text width=35.5mm, align=left] at (4,79) {
    {\fontsize{7}{8.5}\selectfont\bfseries\color{TTCRed} 01 • KHẢO SÁT \& BRIEF}\\[.7mm]
    {\fontsize{6.2}{7.5}\selectfont\color{TTCTextDark}Địa chất, địa hình 3D; yêu cầu công năng và báo cáo tiền khả thi.}\\[3mm]
    {\fontsize{7}{8.5}\selectfont\bfseries\color{TTCBlue} 02 • PHÁP LÝ \& QUY HOẠCH}\\[.7mm]
    {\fontsize{6.2}{7.5}\selectfont\color{TTCTextDark}Quy hoạch 1/500, ĐTM, PCCC, giấy phép xây dựng và cơ sở thiết kế.}
  };
  \fill[TTCRed!8!white] (3.5,5) rectangle (40,17);
  \node[align=center, text=TTCRed] at (21.75,11) {{\fontsize{6}{7}\selectfont\bfseries GATE A}\\[-.2mm]{\fontsize{5.7}{6.7}\selectfont Basis Approved}};

  % PHASE 02
  \fill[white, rounded corners=2pt] (47.5,0) rectangle (91,103);
  \draw[TTCBorder, rounded corners=2pt, line width=.65pt] (47.5,0) rectangle (91,103);
  \fill[TTCBlue, rounded corners=2pt] (47.5,84) rectangle (91,103);
  \node[anchor=west, text=white] at (51.5,94) {{\fontsize{7}{8}\selectfont 02}\quad{\fontsize{10}{11}\selectfont\bfseries ENGINEER}};
  \node[anchor=north west, text width=35.5mm, align=left] at (51.5,79) {
    {\fontsize{7}{8.5}\selectfont\bfseries\color{TTCCyan} 03 • VALUE ENGINEERING}\\[.7mm]
    {\fontsize{6.2}{7.5}\selectfont\color{TTCTextDark}BIM LOD 400, tối ưu kết cấu, phối hợp bộ môn và kiểm soát xung đột.}\\[3mm]
    {\fontsize{7}{8.5}\selectfont\bfseries\color{TTCBlue} 04 • PROCUREMENT \& PEB}\\[.7mm]
    {\fontsize{6.2}{7.5}\selectfont\color{TTCTextDark}Vật tư Tier-1, Shop Drawing, kế hoạch mua sắm và QC thường trú tại xưởng.}
  };
  \fill[TTCCyan!10!white] (51,5) rectangle (87.5,17);
  \node[align=center, text=TTCBlue] at (69.25,11) {{\fontsize{6}{7}\selectfont\bfseries GATE B}\\[-.2mm]{\fontsize{5.7}{6.7}\selectfont Design Freeze}};

  % PHASE 03
  \fill[white, rounded corners=2pt] (95,0) rectangle (138.5,103);
  \draw[TTCBorder, rounded corners=2pt, line width=.65pt] (95,0) rectangle (138.5,103);
  \fill[TTCCyan!85!TTCBlue, rounded corners=2pt] (95,84) rectangle (138.5,103);
  \node[anchor=west, text=white] at (99,94) {{\fontsize{7}{8}\selectfont 03}\quad{\fontsize{10}{11}\selectfont\bfseries BUILD}};
  \node[anchor=north west, text width=35.5mm, align=left] at (99,79) {
    {\fontsize{7}{8.5}\selectfont\bfseries\color{TTCRed} 05 • GROUND \& INFRA}\\[.7mm]
    {\fontsize{6.2}{7.5}\selectfont\color{TTCTextDark}Cọc, móng, nền, hạ tầng kỹ thuật và các workfront bàn giao theo ITP.}\\[3mm]
    {\fontsize{7}{8.5}\selectfont\bfseries\color{TTCBlue} 06 • STRUCTURE \& MEP}\\[.7mm]
    {\fontsize{6.2}{7.5}\selectfont\color{TTCTextDark}Kết cấu thép, bao che, MEP, PCCC và kiểm soát tiến độ đường găng.}
  };
  \fill[TTCBlue!8!white] (98.5,5) rectangle (135,17);
  \node[align=center, text=TTCBlue] at (116.75,11) {{\fontsize{6}{7}\selectfont\bfseries GATE C}\\[-.2mm]{\fontsize{5.7}{6.7}\selectfont Ready To Test}};

  % PHASE 04
  \fill[white, rounded corners=2pt] (142.5,0) rectangle (186,103);
  \draw[TTCBorder, rounded corners=2pt, line width=.65pt] (142.5,0) rectangle (186,103);
  \fill[TTCGold, rounded corners=2pt] (142.5,84) rectangle (186,103);
  \node[anchor=west, text=white] at (146.5,94) {{\fontsize{7}{8}\selectfont 04}\quad{\fontsize{10}{11}\selectfont\bfseries HANDOVER}};
  \node[anchor=north west, text width=35.5mm, align=left] at (146.5,79) {
    {\fontsize{7}{8.5}\selectfont\bfseries\color{TTCRed} 07 • TEST \& APPROVAL}\\[.7mm]
    {\fontsize{6.2}{7.5}\selectfont\color{TTCTextDark}Nghiệm thu ITP, PCCC, chạy thử đơn động và liên động hệ thống.}\\[3mm]
    {\fontsize{7}{8.5}\selectfont\bfseries\color{TTCBlue} 08 • HANDOVER \& O\&M}\\[.7mm]
    {\fontsize{6.2}{7.5}\selectfont\color{TTCTextDark}As-built, Digital Twin, đào tạo vận hành, bảo hành và kế hoạch bảo trì.}
  };
  \fill[TTCGold!12!white] (146,5) rectangle (182.5,17);
  \node[align=center, text=TTCGold!80!black] at (164.25,11) {{\fontsize{6}{7}\selectfont\bfseries GATE D}\\[-.2mm]{\fontsize{5.7}{6.7}\selectfont Ready To Operate}};

  % TRANSITION MARKERS
  \foreach \x/\l in {45.5/A,93/B,140.5/C}{
    \fill[white] (\x,51) circle (3.8);
    \draw[TTCRed, line width=.8pt] (\x,51) circle (3.8);
    \node[text=TTCRed, font=\fontsize{5.5}{6}\selectfont\bfseries] at (\x,51) {\l};
  }
\end{tikzpicture}

\vspace{3mm}

% GOVERNANCE SPINE
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,43);
  \fill[TTCLightBlue, rounded corners=3pt] (0,0) rectangle (186,43);
  \draw[TTCBorder, rounded corners=3pt, line width=.6pt] (0,0) rectangle (186,43);
  \node[anchor=west, text=TTCBlue, font=\fontsize{8}{9.5}\selectfont\bfseries] at (7,35)
    {\faProjectDiagram\quad GOVERNANCE SPINE — MỘT HỆ QUẢN TRỊ XUYÊN SUỐT};
  \foreach \x in {46.5,93,139.5}{\draw[TTCBorder] (\x,6) -- (\x,28);}
  \node[align=center, text width=39mm] at (23.25,17) {{\fontsize{7}{8}\selectfont\bfseries\color{TTCRed} PROJECT DIRECTOR}\\[-.2mm]{\fontsize{5.8}{7}\selectfont\color{TTCTextMuted}Một đầu mối chịu trách nhiệm đầu ra}};
  \node[align=center, text width=39mm] at (69.75,17) {{\fontsize{7}{8}\selectfont\bfseries\color{TTCBlue} CPM BASELINE}\\[-.2mm]{\fontsize{5.8}{7}\selectfont\color{TTCTextMuted}Đường găng và look-ahead hàng tuần}};
  \node[align=center, text width=39mm] at (116.25,17) {{\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} COMMON DATA ENV.}\\[-.2mm]{\fontsize{5.8}{7}\selectfont\color{TTCTextMuted}Bản vẽ, RFI, ITP có truy vết}};
  \node[align=center, text width=39mm] at (162.75,17) {{\fontsize{7}{8}\selectfont\bfseries\color{TTCGold} FIDIC CONTROL}\\[-.2mm]{\fontsize{5.8}{7}\selectfont\color{TTCTextMuted}Scope, change và rủi ro hợp đồng}};
\end{tikzpicture}

\vspace{3mm}

% OUTCOME STRIP
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,29);
  \fill[TTCDeepNavy, rounded corners=3pt] (0,0) rectangle (186,29);
  \foreach \x in {46.5,93,139.5}{\draw[white!35!gray] (\x,6) -- (\x,23);}
  \node[align=center, text=white] at (23.25,15) {{\fontsize{9}{10}\selectfont\bfseries\color{TTCRed} 8 BƯỚC}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont Trong 4 Pha Kiểm Soát}};
  \node[align=center, text=white] at (69.75,15) {{\fontsize{9}{10}\selectfont\bfseries\color{TTCCyan} 4 GATES}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont Quyết Định Có Điều Kiện}};
  \node[align=center, text=white] at (116.25,15) {{\fontsize{9}{10}\selectfont\bfseries FIDIC EPC}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont Chuẩn Hợp Đồng Quốc Tế}};
  \node[align=center, text=white] at (162.75,15) {{\fontsize{9}{10}\selectfont\bfseries\color{TTCGold} 24 THÁNG}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont Bảo Hành Toàn Diện}};
\end{tikzpicture}
\end{minipage}
\newpage
"""

print("Section 3 code rewritten cleanly.")
