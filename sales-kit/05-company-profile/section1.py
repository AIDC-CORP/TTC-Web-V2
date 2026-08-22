# -*- coding: utf-8 -*-
"""
Section 1: Overview, Legal Entity, Leadership & Governance (Pages 01 - 07)
"""

PAGE_01 = r"""% ============================================================
% TRANG 01: TRANG BÌA CHÍNH — COMPANY PROFILE 2026
% Hướng art direction: công trường thực tế toàn trang, navy / đỏ / trắng.
% ============================================================
\thispagestyle{empty}
\begin{tikzpicture}[remember picture, overlay]
  % 1. Hero image: the active construction site is the proof of capability.
  \node[anchor=center, inner sep=0pt] at (current page.center) {
    \includegraphics[height=\paperheight]{../../public/executive-cover-hero.jpg}
  };

  % 2. A dark-to-clear gradient protects the copy without hiding the construction image.
  \shade[
    left color=TTCDeepNavy!96!black,
    right color=transparent,
    opacity=0.70
  ] (current page.south west) rectangle (current page.north east);

  % 3. TTC recognition bar and compact logo lock-up.
  \fill[TTCRed] (current page.north west) rectangle ++(\paperwidth, -2.2mm);
  \node[anchor=north west, fill=white, fill opacity=0.96, text opacity=1,
        rounded corners=1.5pt, inner xsep=5mm, inner ysep=3.8mm]
    at ([xshift=15mm,yshift=-13mm]current page.north west) {
      \includegraphics[width=48mm]{../../public/logo-ttc-removebg-DNXrVdJp.png}
    };
  \node[anchor=north east, text=white, inner sep=0pt] at ([xshift=-15mm,yshift=-15mm]current page.north east) {
    {\fontsize{8}{10}\selectfont\bfseries COMPANY PROFILE \;|\; 2026}
  };

  % 4. Large left-aligned title fills the visual centre; the clear right side shows the site.
  \node[anchor=west, align=left, text width=128mm, inner sep=0pt]
    at ([xshift=16mm,yshift=160mm]current page.south west) {
      {\fontsize{7.8}{9.6}\selectfont\bfseries\color{TTCRed} TAN THANH CONG TECHNOLOGY CONSTRUCTION JOINT STOCK COMPANY}\\[6mm]
      {\fontsize{43}{49}\selectfont\bfseries\color{white} HỒ SƠ}\\[-2mm]
      {\fontsize{43}{49}\selectfont\bfseries\color{white} NĂNG LỰC}\\[4mm]
      {\color{TTCRed}\rule{73mm}{2.8pt}}\\[5mm]
      {\fontsize{17}{20}\selectfont\bfseries\color{white} COMPANY PROFILE}\\[10mm]
      {\fontsize{14}{17}\selectfont\bfseries\color{white} TỔNG THẦU EPC CÔNG NGHIỆP\\THẾ HỆ MỚI}\\[3mm]
      {\fontsize{9.5}{12}\selectfont\color{white!88!gray} Turnkey Industrial EPC General Contractor}
    };

  % 5. Proof points: compact, scannable and placed above the contact footer.
  \node[anchor=south west, align=left, fill=TTCDeepNavy!92!black, fill opacity=0.84,
        text=white, text opacity=1, rounded corners=1.5pt, inner xsep=6mm, inner ysep=4mm]
    at ([xshift=15mm,yshift=31mm]current page.south west) {
      {\fontsize{12}{14}\selectfont\bfseries 150+ DỰ ÁN \qquad HẠNG II BXD \qquad ISO 9001 / 14001 / 45001}\\[1.2mm]
      {\fontsize{7}{8.5}\selectfont\color{white!82!gray}Năng lực tổng thầu công nghiệp đã được chứng minh tại hiện trường}
    };

  % 6. Legal identity stays quiet; the cover remains a visual statement.
  \node[anchor=south west, text=white, inner sep=0pt] at ([xshift=15mm,yshift=19mm]current page.south west) {
    {\fontsize{6.6}{8.2}\selectfont\bfseries CÔNG TY CỔ PHẦN CÔNG NGHỆ XÂY DỰNG TÂN THÀNH CÔNG}
  };

  % 7. Persistent contact footer.
  \fill[TTCDeepNavy!97!black] (current page.south west) rectangle ++(\paperwidth, 11mm);
  \fill[TTCRed] ([yshift=11mm]current page.south west) rectangle ++(\paperwidth, 1.2mm);
  \node[anchor=south, text=white, inner sep=0pt] at ([yshift=3.4mm]current page.south) {
    {\fontsize{6.8}{8.2}\selectfont
      \faPhone\ +84 976 447 766 \quad\textbullet\quad
      \faEnvelope\ info@tanthanhcongjsc.com \quad\textbullet\quad
      \faGlobe\ tanthanhcongjsc.com \quad\textbullet\quad
      \faAward\ NĂNG LỰC HẠNG II BXD}
  };
\end{tikzpicture}
\mbox{}% Anchor the overlay to a physical page before advancing to page 02.
\newpage
"""

PAGE_02 = r"""% ============================================================
% TRANG 02: MỤC LỤC ĐIỀU HƯỚNG & THÔNG TIN PHÁP NHÂN TÓM TẮT
% ============================================================
\pageheaderbar{MỤC LỤC \& THÔNG TIN PHÁP NHÂN}{Trang 02}
\pagefooterbar{Trang 02}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.025, scale=4.2, font=\bfseries\sffamily, text=TTCBlue]
    at ([xshift=30mm,yshift=-8mm]current page.center) {TTC};
  \fill[TTCRed, opacity=0.05] ([xshift=12mm,yshift=18mm]current page.south west)
    rectangle ([xshift=18mm,yshift=248mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Mục Lục Tổng Quan}{Executive Contents — 06 Chuyên Mục Trọng Tâm}

{\fontsize{9.2}{11.5}\selectfont\color{TTCTextMuted}
Hồ sơ được tổ chức theo 06 nhóm năng lực để Chủ đầu tư tra cứu nhanh; chi tiết từng hạng mục được trình bày tại các trang chuyên đề.}\\[3mm]

% Navigation cards: inspired by section-based contents, without repeating every page title.
\newcommand{\toccard}[5]{%
  \begin{tikzpicture}
    \node[rounded corners=3pt, fill=white, draw=TTCBorder, line width=0.8pt,
          minimum width=90mm, minimum height=52mm, text width=79mm, inner sep=5.5mm, align=left] {
      {\fontsize{18}{19}\selectfont\bfseries\color{TTCRed} #1}\hspace{3mm}
      {\fontsize{8.2}{9.5}\selectfont\bfseries\color{TTCRed} TRANG #2}\\[1.5mm]
      {\fontsize{11.2}{13.2}\selectfont\bfseries\color{TTCBlue} #3}\\[0.3mm]
      {\fontsize{7.2}{8.8}\selectfont\itshape\color{TTCTextMuted} #4}\\[3mm]
      {\fontsize{8.2}{10.5}\selectfont\color{TTCTextDark} #5}
    };
  \end{tikzpicture}%
}

\noindent
\begin{tabular}{@{}p{91mm}@{\hspace{4mm}}p{91mm}@{}}
\toccard{I}{01--07}{GIỚI THIỆU \& NĂNG LỰC}{Company profile \& credentials}{Thư ngỏ \textbullet\ Tầm nhìn và giá trị \textbullet\ Hệ sinh thái \textbullet\ Pháp nhân \& lãnh đạo} &
\toccard{IV}{14--19}{GIẢI PHÁP EPC \& CÔNG NGHỆ}{EPC, ConTech \& ESG}{Fast-track EPC \textbullet\ BIM / AI \textbullet\ ESG \textbullet\ QA/QC \& HSE} \\[3.5mm]
\toccard{II}{08--10}{TÀI CHÍNH \& NHÂN SỰ}{Financial capacity \& people}{Doanh thu \textbullet\ Bảo lãnh tín dụng \textbullet\ Nguồn lực \textbullet\ Văn hóa an toàn} &
\toccard{V}{20--30}{DỰ ÁN \& KHÁCH HÀNG}{Projects \& valued partners}{Danh mục dự án \textbullet\ 06 case studies \textbullet\ Chuỗi cung ứng \textbullet\ Đối tác FDI} \\[3.5mm]
\toccard{III}{11--13}{SẢN XUẤT \& QUẢN TRỊ}{PEB \& project control}{Đối tác PEB \textbullet\ Thiết bị cơ giới \textbullet\ Quy trình quản trị FIDIC} &
\toccard{VI}{31--36}{CAM KẾT \& ĐỒNG HÀNH}{Commitments \& support}{Chứng nhận \textbullet\ Phủ sóng thi công \textbullet\ Chiến lược \textbullet\ Bảo hành \& liên hệ}
\end{tabular}

\vspace{4.5mm}

% Compact legal snapshot: details remain on the legal-credentials spread (page 06).
\noindent
\begin{tikzpicture}
  \node[rounded corners=3pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.8pt,
        minimum width=186mm, text width=172mm, inner sep=7.5mm] {
    {\fontsize{10.5}{12.5}\selectfont\bfseries\color{TTCBlue} \faIdCard\quad HỒ SƠ PHÁP NHÂN TÓM TẮT}
    \hfill {\fontsize{7.2}{8.8}\selectfont\color{TTCRed}\bfseries CHI TIẾT CHỨNG NHẬN: TRANG 06}\\[1.5mm]
    {\fontsize{6.2}{7.5}\selectfont\color{TTCTextMuted}\bfseries
    TAN THANH CONG TECHNOLOGY CONSTRUCTION JOINT STOCK COMPANY}\\[3mm]
    \renewcommand{\arraystretch}{1.28}
    {\fontsize{8.2}{10.2}\selectfont
    \begin{tabularx}{\linewidth}{@{}p{32mm}X@{\hspace{5mm}}p{28mm}X@{}}
      \textbf{Tên doanh nghiệp} & \textbf{CÔNG TY CỔ PHẦN CÔNG NGHỆ XÂY DỰNG TÂN THÀNH CÔNG} &
      \textbf{Mã số thuế} & \textbf{0107090447} \\
      \textbf{Đại diện pháp luật} & \textbf{Ông PHẠM HUY TÂN} — Tổng Giám Đốc &
      \textbf{Năng lực} & Hạng II BXD \textbullet\ ISO 9001 / 14001 / 45001 \\
      \textbf{Trụ sở đăng ký} & Số 39, ngõ 292 Kim Giang, Đại Kim, Hà Nội &
      \textbf{Văn phòng giao dịch} & Số 19N7B, KĐT Trung Hòa Nhân Chính, Hà Nội \\
      \textbf{Liên hệ} & +84 976 447 766 \textbullet\ info@tanthanhcongjsc.com &
      \textbf{Website} & tanthanhcongjsc.com
    \end{tabularx}}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_03 = r"""% ============================================================
% TRANG 03: THÔNG ĐIỆP TỪ TỔNG GIÁM ĐỐC — LEADERSHIP MESSAGE
% ============================================================
\pageheaderbar{THÔNG ĐIỆP TỪ TỔNG GIÁM ĐỐC}{Trang 03}
\pagefooterbar{Trang 03}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.025, scale=4.0, font=\bfseries\sffamily, text=TTCBlue]
    at ([xshift=-25mm,yshift=-25mm]current page.center) {LEADERSHIP};
  \fill[TTCRed, opacity=0.045] ([xshift=12mm,yshift=18mm]current page.south west)
    rectangle ([xshift=18mm,yshift=248mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Thông Điệp Từ Tổng Giám Đốc}{Leadership Message — Building Trust Through Every Commitment}

\vspace{2mm}

% Main editorial spread: concise letter on the left, authentic CEO portrait on the right.
\noindent
\begin{tabular}{@{}p{106mm}@{\hspace{4mm}}p{76mm}@{}}
  \begin{tikzpicture}
    \path[use as bounding box] (0,0) rectangle (106mm,170mm);
    \draw[TTCRed, line width=2.2pt] (0,169mm) -- (26mm,169mm);
    \node[anchor=north west, align=left, text width=98mm, inner sep=0pt] at (0,165mm) {
      {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCRed} THÔNG ĐIỆP NHẤT QUÁN CỦA TTC}\\[4mm]
      {\fontsize{19}{23}\selectfont\bfseries\color{TTCBlue}
      ``CHẤT LƯỢNG LÀ DANH DỰ.\\
      AN TOÀN LÀ SINH MỆNH.\\
      TIẾN ĐỘ LÀ CAM KẾT.''}\\[6mm]
      {\fontsize{10}{12}\selectfont\bfseries\color{TTCBlue}
      Kính gửi Quý Chủ đầu tư, Quý Khách hàng và Quý Đối tác,}\\[3mm]
      {\fontsize{9.2}{13.2}\selectfont\color{TTCTextDark}
      Thay mặt Ban Lãnh đạo và toàn thể cán bộ công nhân viên \textbf{Công ty Cổ phần Công nghệ Xây dựng Tân Thành Công}, tôi trân trọng cảm ơn sự tin tưởng và đồng hành của Quý vị trong suốt chặng đường phát triển của TTC.\\[3mm]

      Hơn một thập kỷ hoạt động trong lĩnh vực xây dựng công nghiệp giúp chúng tôi thấu hiểu rằng: một dự án thành công phải đồng thời đáp ứng \textbf{chất lượng, an toàn, tiến độ và hiệu quả đầu tư}. Vì vậy, TTC kiên định với mô hình \textbf{Tổng thầu EPC một đầu mối}, kết hợp Value Engineering, BIM 5D và năng lực quản trị hiện trường theo tiêu chuẩn quốc tế.\\[3mm]

      Với hệ sinh thái đối tác PEB công suất 30.000 tấn/năm và đội ngũ kỹ sư thực chiến, chúng tôi cam kết cung cấp giải pháp phù hợp nhất cho từng nhà máy, kiểm soát minh bạch từ thiết kế, thi công đến bàn giao và bảo hành.\\[3mm]

      TTC mong muốn không chỉ là một nhà thầu, mà là \textbf{đối tác kiến tạo giá trị dài hạn} cùng Chủ đầu tư trên mỗi công trình.}\\[5mm]
      {\fontsize{9}{11}\selectfont\itshape\color{TTCTextMuted} Trân trọng,}
    };
  \end{tikzpicture}
  &
  \begin{tikzpicture}
    \path[use as bounding box] (0,0) rectangle (76mm,170mm);
    \fill[TTCLightBlue] (0,0) rectangle (76mm,170mm);
    \draw[TTCBorder, line width=0.8pt] (0,0) rectangle (76mm,170mm);
    \fill[TTCRed] (0,0) rectangle (3mm,170mm);

    \node[anchor=north, inner sep=0pt] at (39.5mm,168mm) {
      \includegraphics[trim=90 0 90 0,clip,height=116mm]{../tan_avatar.jpg}
    };

    \fill[TTCDeepNavy!97!black] (3mm,0) rectangle (76mm,54mm);
    \fill[TTCRed] (3mm,54mm) rectangle (76mm,56mm);
    \node[anchor=north west, align=left, text width=62mm, inner sep=0pt]
      at (10mm,46mm) {
        {\fontsize{7}{8.5}\selectfont\bfseries\color{TTCRed} TỔNG GIÁM ĐỐC / CEO}\\[2mm]
        {\fontsize{14}{17}\selectfont\bfseries\color{white} PHẠM HUY TÂN}\\[2mm]
        {\fontsize{7.5}{9.5}\selectfont\color{white!78!gray}
        Công ty Cổ phần Công nghệ\\Xây dựng Tân Thành Công}\\[4mm]
        {\fontsize{7.2}{9}\selectfont\bfseries\color{white!68!gray} TÂN THÀNH CÔNG \textbullet\ TTC JSC}
      };
  \end{tikzpicture}
\end{tabular}

\vspace{5mm}

% Three commitments replace the duplicated vision/mission content.
\noindent
\begin{tabular}{@{}p{58mm}@{\hspace{6mm}}p{58mm}@{\hspace{6mm}}p{58mm}@{}}
  \begin{tikzpicture}
    \node[rounded corners=3pt, fill=TTCDeepNavy!97!black, minimum width=58mm,
          minimum height=43mm, text width=48mm, align=center, inner sep=5mm] {
      {\fontsize{17}{19}\selectfont\bfseries\color{white} 01}\\[1mm]
      {\fontsize{9}{11}\selectfont\bfseries\color{TTCRed} ĐẦU MỐI EPC}\\[2mm]
      {\fontsize{7.3}{9}\selectfont\color{white!78!gray}Design \textbullet\ Build \textbullet\ Turnkey}
    };
  \end{tikzpicture}
  &
  \begin{tikzpicture}
    \node[rounded corners=3pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.8pt,
          minimum width=58mm, minimum height=43mm, text width=48mm, align=center, inner sep=5mm] {
      {\fontsize{17}{19}\selectfont\bfseries\color{TTCRed} 10--15\%}\\[1mm]
      {\fontsize{9}{11}\selectfont\bfseries\color{TTCBlue} TỐI ƯU CHI PHÍ}\\[2mm]
      {\fontsize{7.3}{9}\selectfont\color{TTCTextMuted}Value Engineering}
    };
  \end{tikzpicture}
  &
  \begin{tikzpicture}
    \node[rounded corners=3pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.8pt,
          minimum width=58mm, minimum height=43mm, text width=48mm, align=center, inner sep=5mm] {
      {\fontsize{15}{18}\selectfont\bfseries\color{TTCRed} ZERO}\\[1mm]
      {\fontsize{9}{11}\selectfont\bfseries\color{TTCBlue} ACCIDENT}\\[2mm]
      {\fontsize{7.3}{9}\selectfont\color{TTCTextMuted}HSE Commitment}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{6mm}

\noindent
\begin{tikzpicture}
  \node[rounded corners=2pt, fill=white, draw=TTCRed, line width=0.9pt,
        minimum width=186mm, minimum height=15mm, align=center, inner sep=3mm] {
    {\fontsize{10}{12}\selectfont\bfseries\color{TTCBlue}
    KIẾN TẠO GIÁ TRỊ DÀI HẠN \quad\textbullet\quad BUILDING ENDURING VALUE}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_04 = r"""% ============================================================
% TRANG 04: KẾT CẤU VƯƠN CAO — HÀNH TRÌNH & GIÁ TRỊ CỐT LÕI
% ============================================================
\pageheaderbar{HÀNH TRÌNH PHÁT TRIỂN \& GIÁ TRỊ CỐT LÕI}{Trang 04}
\pagefooterbar{Trang 04}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.022, scale=4.0, font=\bfseries\sffamily, text=TTCBlue]
    at ([xshift=15mm,yshift=-18mm]current page.center) {BUILDING THE FUTURE};
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Hành Trình Kiến Tạo}{From Mechanical Foundations to a Next-Generation EPC General Contractor}

\vspace{1mm}

\noindent
\begin{tikzpicture}
  \node[anchor=west, align=left, inner sep=0pt] at (0,7mm) {
    {\fontsize{16}{19}\selectfont\bfseries\color{TTCBlue}
    TỪ NỀN TẢNG CƠ KHÍ ĐẾN TỔNG THẦU EPC THẾ HỆ MỚI}\\[1.5mm]
    {\fontsize{7.8}{9.5}\selectfont\color{TTCTextMuted}
    Một hành trình phát triển được nâng đỡ bởi năng lực thực thi, công nghệ và những giá trị bất biến.}
  };
  \fill[TTCRed] (0,0) rectangle (52mm,1.4mm);
\end{tikzpicture}

\vspace{3mm}

% Diagonal growth spine — a steel-beam metaphor for TTC's development.
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,112);
  \fill[TTCLightBlue!55!white] (0,0) rectangle (186,112);
  \draw[TTCBorder, line width=0.8pt, rounded corners=3pt] (0,0) rectangle (186,112);
  \draw[TTCBlue!7!white, line width=0.35pt] (0,0) grid[step=10mm] (186,112);

  % Stepped structural spine: horizontal floor plates linked by rising steel members.
  \draw[TTCBlue!10!white, line width=7pt, line join=round]
    (16,19) -- (44,19) -- (52,40) -- (76,40) -- (84,61) --
    (116,61) -- (124,82) -- (155,82) -- (163,105) -- (180,105);
  \draw[TTCBlue!28!white, line width=1pt, line join=round]
    (12,14) -- (41,14) -- (49,35) -- (73,35) -- (81,56) --
    (113,56) -- (121,77) -- (152,77) -- (160,100) -- (177,100);
  \draw[TTCRed, line width=3.2pt, line join=round]
    (16,19) -- (44,19) -- (52,40) -- (76,40) -- (84,61) --
    (116,61) -- (124,82) -- (155,82) -- (163,105) -- (180,105);
  \draw[TTCRed, line width=1.1pt, -{Stealth[length=4mm]}] (180,105) -- (184,109);

  % 2015
  \fill[white] (16,19) circle (3.4);
  \draw[TTCRed, line width=1.5pt] (16,19) circle (3.4);
  \fill[TTCRed] (16,19) circle (1.35);
  \node[anchor=south west, align=left, text width=38mm, fill=TTCLightBlue!86!white,
        fill opacity=0.94, text opacity=1, rounded corners=1.5pt, inner sep=1mm] at (7,25) {
    {\fontsize{18}{20}\selectfont\bfseries\color{TTCRed} 2015}\\[-0.5mm]
    {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCBlue} KHỞI TẠO}\\[1mm]
    {\fontsize{7.2}{9}\selectfont\color{TTCTextDark}Nền tảng cơ khí chính xác\\và kỹ thuật kết cấu thép.}
  };

  % 2018
  \fill[white] (55,40) circle (3.4);
  \draw[TTCRed, line width=1.5pt] (55,40) circle (3.4);
  \fill[TTCRed] (55,40) circle (1.35);
  \node[anchor=north west, align=left, text width=38mm, fill=TTCLightBlue!86!white,
        fill opacity=0.94, text opacity=1, rounded corners=1.5pt, inner sep=1mm] at (38,29) {
    {\fontsize{18}{20}\selectfont\bfseries\color{TTCRed} 2018}\\[-0.5mm]
    {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCBlue} MỞ RỘNG}\\[1mm]
    {\fontsize{7.2}{9}\selectfont\color{TTCTextDark}Liên kết sản xuất PEB\\và tổng thầu hạ tầng KCN.}
  };

  % 2022
  \fill[white] (94,61) circle (3.4);
  \draw[TTCRed, line width=1.5pt] (94,61) circle (3.4);
  \fill[TTCRed] (94,61) circle (1.35);
  \node[anchor=south west, align=left, text width=39mm, fill=TTCLightBlue!86!white,
        fill opacity=0.94, text opacity=1, rounded corners=1.5pt, inner sep=1mm] at (71,67) {
    {\fontsize{18}{20}\selectfont\bfseries\color{TTCRed} 2022}\\[-0.5mm]
    {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCBlue} BỨT PHÁ}\\[1mm]
    {\fontsize{7.2}{9}\selectfont\color{TTCTextDark}Hạng II Bộ Xây Dựng\\và các dự án FDI quy mô lớn.}
  };

  % 2026
  \fill[white] (134,82) circle (3.4);
  \draw[TTCRed, line width=1.5pt] (134,82) circle (3.4);
  \fill[TTCRed] (134,82) circle (1.35);
  \node[anchor=north west, align=left, text width=42mm, fill=TTCLightBlue!86!white,
        fill opacity=0.94, text opacity=1, rounded corners=1.5pt, inner sep=1mm] at (119,68) {
    {\fontsize{18}{20}\selectfont\bfseries\color{TTCRed} 2026}\\[-0.5mm]
    {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCBlue} CHUYỂN ĐỔI}\\[1mm]
    {\fontsize{7.2}{9}\selectfont\color{TTCTextDark}150+ dự án \textbullet\ 20+ tỉnh thành\\PEB 30.000 tấn/năm.}
  };

  % 2030
  \fill[white] (176,105) circle (3.4);
  \draw[TTCRed, line width=1.5pt] (176,105) circle (3.4);
  \fill[TTCRed] (176,105) circle (1.35);
  \node[anchor=north east, align=right, text width=40mm, fill=TTCLightBlue!86!white,
        fill opacity=0.94, text opacity=1, rounded corners=1.5pt, inner sep=1mm] at (178,98) {
    {\fontsize{18}{20}\selectfont\bfseries\color{TTCRed} 2030}\\[-0.5mm]
    {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCBlue} VƯƠN TẦM}\\[1mm]
    {\fontsize{7.2}{9}\selectfont\color{TTCTextDark}ConTech \textbullet\ ESG\\Mở rộng Đông Nam Á.}
  };
\end{tikzpicture}

\vspace{4mm}

% Photo foundation: five core values become the structural base of the journey.
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,112);
  \clip[rounded corners=3pt] (0,0) rectangle (186,112);
  \node[anchor=center, inner sep=0pt] at (93,56) {
    \includegraphics[height=112mm]{assets/milestones_engineer_hero.jpg}
  };
  \shade[left color=TTCDeepNavy!98!black, right color=transparent, opacity=0.82]
    (0,31) rectangle (142,112);
  \node[anchor=north west, align=left, text width=112mm, inner sep=0pt] at (8,104) {
    {\fontsize{12}{14}\selectfont\bfseries\color{white}5 GIÁ TRỊ — NỀN MÓNG CỦA MỌI CÔNG TRÌNH}\\[1.5mm]
    {\fontsize{7.5}{9}\selectfont\color{white!82!gray}The values that sustain every commitment and every project.}
  };

  \fill[TTCDeepNavy!97!black, opacity=0.96] (0,0) rectangle (37.2,31);
  \fill[TTCDeepNavy!91!black, opacity=0.96] (37.2,0) rectangle (74.4,31);
  \fill[TTCDeepNavy!97!black, opacity=0.96] (74.4,0) rectangle (111.6,31);
  \fill[TTCDeepNavy!91!black, opacity=0.96] (111.6,0) rectangle (148.8,31);
  \fill[TTCDeepNavy!97!black, opacity=0.96] (148.8,0) rectangle (186,31);
  \fill[TTCRed] (0,31) rectangle (186,32.3);

  \node[align=center, text=white] at (18.6,15.5) {
    {\fontsize{14}{16}\selectfont\bfseries TÍN}\\[1mm]
    {\fontsize{6.8}{8}\selectfont\color{white!72!gray}TRUST \& INTEGRITY}
  };
  \node[align=center, text=white] at (55.8,15.5) {
    {\fontsize{14}{16}\selectfont\bfseries TÂM}\\[1mm]
    {\fontsize{6.8}{8}\selectfont\color{white!72!gray}DEDICATION}
  };
  \node[align=center, text=white] at (93,15.5) {
    {\fontsize{14}{16}\selectfont\bfseries TRÍ}\\[1mm]
    {\fontsize{6.8}{8}\selectfont\color{white!72!gray}INNOVATION}
  };
  \node[align=center, text=white] at (130.2,15.5) {
    {\fontsize{14}{16}\selectfont\bfseries TỐC}\\[1mm]
    {\fontsize{6.8}{8}\selectfont\color{white!72!gray}FAST-TRACK}
  };
  \node[align=center, text=white] at (167.4,15.5) {
    {\fontsize{14}{16}\selectfont\bfseries AN}\\[1mm]
    {\fontsize{6.8}{8}\selectfont\color{white!72!gray}HSE \& SAFETY}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_05_LEGACY = r"""% ============================================================
% TRANG 05: HỆ SINH THÁI TỔNG THẦU & ĐỐI TÁC CÔNG NGHỆ AIDC
% ============================================================
\pageheaderbar{HỆ SINH THÁI DOANH NGHIỆP \& R\&D CÔNG NGHỆ}{Trang 05}
\pagefooterbar{Trang 05}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.03, scale=2.8, font=\bfseries\sffamily, text=TTCBlue] at ([yshift=-10mm]current page.center) {INTEGRATED INDUSTRIAL ECOSYSTEM};
  \draw[TTCBlue!6!white, line width=0.5pt] ([xshift=15mm, yshift=20mm]current page.south west) grid[step=8mm] ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Hệ Sinh Thái Tổng Thầu EPC \& R\&D Công Nghệ AIDC}{Integrated Industrial Ecosystem \& Advanced AI ConTech Collaboration}

% TẦNG 1: SƠ ĐỒ HỆ SINH THÁI CUNG TRÒN TIKZ (Single Canvas)
\noindent
\begin{tikzpicture}
  % Outer Frame
  \draw[TTCBlue!40!white, line width=0.9pt, fill=white, rounded corners=6pt] (0,0) rectangle (18.6, 9.8);
  
  % Large Orbit Disc (Right)
  \fill[TTCDeepNavy!95!black] (15.0, 4.9) circle (4.2cm);
  \draw[TTCRed, line width=3.5pt] (15.0, 4.9) circle (4.2cm);
  \draw[TTCCyan!60!white, line width=1pt, dashed] (15.0, 4.9) circle (4.6cm);
  
  % Core Hub Text inside Orbit Disc
  \node[align=center, text=white] at (14.6, 5.3) {
    {\fontsize{13}{15}\selectfont\bfseries TÂN THÀNH CÔNG}\\[3pt]
    {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCCyan} TTC ECOSYSTEM}
  };
  
  % Orbit Satellite 01: ĐỐI TÁC PEB
  \draw[TTCRed, line width=1.5pt] (15.0, 4.9) -- (9.4, 7.8);
  \fill[white] (9.4, 7.8) circle (0.85cm);
  \draw[TTCRed, line width=1.8pt] (9.4, 7.8) circle (0.85cm);
  \node[align=center] at (9.4, 7.8) {
    \faIndustry\\[1pt]
    {\fontsize{6.2}{7.5}\selectfont\bfseries ĐỐI TÁC PEB}
  };
  
  % Orbit Satellite 02: AIDC AI
  \draw[TTCCyan, line width=1.5pt] (15.0, 4.9) -- (8.2, 4.9);
  \fill[white] (8.2, 4.9) circle (0.85cm);
  \draw[TTCCyan, line width=1.8pt] (8.2, 4.9) circle (0.85cm);
  \node[align=center] at (8.2, 4.9) {
    \faMicrochip\\[1pt]
    {\fontsize{6.2}{7.5}\selectfont\bfseries AIDC AI}
  };
  
  % Orbit Satellite 03: TTC MEP
  \draw[TTCBlue, line width=1.5pt] (15.0, 4.9) -- (9.4, 2.0);
  \fill[white] (9.4, 2.0) circle (0.85cm);
  \draw[TTCBlue, line width=1.8pt] (9.4, 2.0) circle (0.85cm);
  \node[align=center] at (9.4, 2.0) {
    \faCogs\\[1pt]
    {\fontsize{6.2}{7.5}\selectfont\bfseries TTC MEP}
  };
  
  % Orbit Satellite 04: INFRA
  \draw[TTCGold, line width=1.5pt] (15.0, 4.9) -- (11.9, 0.9);
  \fill[white] (11.9, 0.9) circle (0.85cm);
  \draw[TTCGold, line width=1.8pt] (11.9, 0.9) circle (0.85cm);
  \node[align=center] at (11.9, 0.9) {
    \faBuilding\\[1pt]
    {\fontsize{6.2}{7.5}\selectfont\bfseries INFRA}
  };
  
  % 4 Explanatory Cards (Left Column)
  % Card 1: PEB Partner
  \node[anchor=north west, inner sep=0pt] at (0.4, 9.4) {
    \begin{tikzpicture}
      \node[
        rounded corners=4pt, fill=white, draw=TTCRed!80!white, line width=0.8pt,
        minimum width=6.8cm, minimum height=1.9cm, text width=6.4cm, inner sep=4pt, align=left
      ] {
        {\fontsize{8}{10}\selectfont\bfseries\color{TTCRed} 01. ĐỐI TÁC SẢN XUẤT KẾT CẤU THÉP PEB}\\[2pt]
        {\fontsize{6.8}{8.5}\selectfont\color{TTCTextDark}
        Liên kết sản xuất 30.000 Tấn/năm, xưởng $> 20.000$ m$^2$, gia công CNC tự động, hàn SAW đạt chuẩn Mỹ AWS D1.1 dưới giám sát QC trực tiếp của TTC.}
      };
    \end{tikzpicture}
  };
  
  % Card 2: AIDC R&D
  \node[anchor=north west, inner sep=0pt] at (0.4, 7.2) {
    \begin{tikzpicture}
      \node[
        rounded corners=4pt, fill=white, draw=TTCCyan!90!white, line width=0.8pt,
        minimum width=6.8cm, minimum height=1.9cm, text width=6.4cm, inner sep=4pt, align=left
      ] {
        {\fontsize{8}{10}\selectfont\bfseries\color{TTCCyan} 02. ĐỐI TÁC CÔNG NGHỆ R\&D AIDC}\\[2pt]
        {\fontsize{6.8}{8.5}\selectfont\color{TTCTextDark}
        Đơn vị R\&D chuyên sâu công nghệ số: thuật toán AI tối ưu 10--15\% kết cấu dầm thép, mô hình BIM 5D và bản sao số Smart Digital Twin.}
      };
    \end{tikzpicture}
  };
  
  % Card 3: MEP & PCCC
  \node[anchor=north west, inner sep=0pt] at (0.4, 5.0) {
    \begin{tikzpicture}
      \node[
        rounded corners=4pt, fill=white, draw=TTCBlue!80!white, line width=0.8pt,
        minimum width=6.8cm, minimum height=1.9cm, text width=6.4cm, inner sep=4pt, align=left
      ] {
        {\fontsize{8}{10}\selectfont\bfseries\color{TTCBlue} 03. CƠ ĐIỆN MEP \& PCCC CHUYÊN SÂU}\\[2pt]
        {\fontsize{6.8}{8.5}\selectfont\color{TTCTextDark}
        Trạm biến áp trung thế 22kV, HVAC phòng sạch, PCCC tự động, trạm xử lý nước thải Cột A QCVN 40.}
      };
    \end{tikzpicture}
  };
  
  % Card 4: Infra
  \node[anchor=north west, inner sep=0pt] at (0.4, 2.8) {
    \begin{tikzpicture}
      \node[
        rounded corners=4pt, fill=white, draw=TTCGold!90!white, line width=0.8pt,
        minimum width=6.8cm, minimum height=1.9cm, text width=6.4cm, inner sep=4pt, align=left
      ] {
        {\fontsize{8}{10}\selectfont\bfseries\color{TTCGold} 04. HẠ TẦNG KỸ THUẬT KCN XANH}\\[2pt]
        {\fontsize{6.8}{8.5}\selectfont\color{TTCTextDark}
        Thi công san lấp, giao thông nội bộ, móng cọc tải trọng nặng và cảnh quan sinh thái chuẩn ESG.}
      };
    \end{tikzpicture}
  };
\end{tikzpicture}

\vspace{2mm}

% TẦNG 2: 4 CARD LỢI THẾ CẠNH TRANH
\noindent
\begin{tabular}{@{}p{42.5mm}@{\hspace{3mm}}p{42.5mm}@{\hspace{3mm}}p{42.5mm}@{\hspace{3mm}}p{42.5mm}@{}}
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=42.5mm, minimum height=50mm, inner sep=4pt, text width=38mm, align=left] {
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCRed} \faAward\ Trách Nhiệm 1 Đầu Mối}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ Đại diện Tổng thầu EPC duy nhất.\newline
      \textbullet\ Quản lý thiết kế, pháp lý DTM/PCCC.\newline
      \textbullet\ Thi công nền móng, kết cấu, MEP.\newline
      \textbullet\ Triệt tiêu mọi rủi ro đùn đẩy trách nhiệm.\newline
      \textbullet\ Bàn giao As-Built chìa khóa trao tay.}
    };
  \end{tikzpicture} &
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=42.5mm, minimum height=50mm, inner sep=4pt, text width=38mm, align=left] {
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCCyan} \faMicrochip\ Công Nghệ Bảo Trợ}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ AIDC đồng hành R\&D công nghệ số.\newline
      \textbullet\ Thuật toán AI tối ưu tiết diện dầm.\newline
      \textbullet\ Mô hình BIM 5D tiết kiệm 10--15\%.\newline
      \textbullet\ Bàn giao Digital Twin 3D hoàn công.\newline
      \textbullet\ Quản trị dữ liệu đám mây CDE.}
    };
  \end{tikzpicture} &
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=42.5mm, minimum height=50mm, inner sep=4pt, text width=38mm, align=left] {
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCBlue} \faIndustry\ Chủ Động Nguồn Cung}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ Đối tác nhà máy PEB 30.000T/năm.\newline
      \textbullet\ Dây chuyền CNC Plasma/Hàn SAW.\newline
      \textbullet\ 100\% dầm thép ổn định chất lượng.\newline
      \textbullet\ Không phụ thuộc gia công thầu phụ.\newline
      \textbullet\ Làm chủ hoàn toàn tiến độ dự án.}
    };
  \end{tikzpicture} &
  \begin{tikzpicture}
    \node[rounded corners=4pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.6pt, minimum width=42.5mm, minimum height=50mm, inner sep=4pt, text width=38mm, align=left] {
      {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCGold} \faShield*\ Bảo Hành Cấp Tốc}\\[2pt]
      {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}
      \textbullet\ Phản ứng kỹ thuật tại chỗ trong 4h.\newline
      \textbullet\ Đội bảo trì chuyên trách 24/7.\newline
      \textbullet\ Bảo hành kết cấu 24 tháng toàn diện.\newline
      \textbullet\ Kiểm tra định kỳ 6 tháng/lần miễn phí.\newline
      \textbullet\ Đồng hành trọn đời cùng nhà máy.}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{2mm}

% TẦNG 3: BĂNG THÔNG ĐIỆP
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
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCRed} 1 ĐẦU MỐI} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCCyan} 30.000 TẤN} &
      {\fontsize{14}{16}\selectfont\bfseries\color{white} -15\% THÉP} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCGold} 100\% KHÉP KÍN} \\
      {\fontsize{7.2}{8.5}\selectfont Trách Nhiệm Toàn Diện} &
      {\fontsize{7.2}{8.5}\selectfont Năng Lực Cung Ứng PEB} &
      {\fontsize{7.2}{8.5}\selectfont Tối Ưu Hóa Chi Phí AI} &
      {\fontsize{7.2}{8.5}\selectfont Chuỗi Giá Trị Tổng Thầu}
    \end{tabularx}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_05 = r"""% ============================================================
% TRANG 05: INTEGRATED FACTORY BLUEPRINT
% ============================================================
\pageheaderbar{HỆ SINH THÁI TỔNG THẦU EPC \& R\&D CÔNG NGHỆ}{Trang 05}
\pagefooterbar{Trang 05}

\begin{tikzpicture}[remember picture, overlay]
  \draw[TTCBlue!6!white, line width=0.45pt]
    ([xshift=15mm,yshift=18mm]current page.south west)
    grid[step=8mm]
    ([xshift=195mm,yshift=42mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Hệ Sinh Thái Tổng Thầu EPC}{Integrated Factory Blueprint \& AIDC ConTech Collaboration}

\vspace{1mm}
{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
MỘT HỆ SINH THÁI • MỘT HỢP ĐỒNG • MỘT TRÁCH NHIỆM\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
One integrated ecosystem. One accountable EPC partner from concept to handover.\par}
\vspace{3mm}

% HERO: NHÀ MÁY LÀ TRUNG TÂM, NĂNG LỰC LÀ CÁC LỚP TÍCH HỢP
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,118);
  \clip[rounded corners=3pt] (0,0) rectangle (186,118);
  \node[anchor=center, inner sep=0pt] at (93,59)
    {\includegraphics[height=118mm]{../../public/factory-tech-3d.jpg}};
  \fill[white, opacity=0.10] (0,0) rectangle (186,118);

  % Connectors — thin and quiet
  \draw[TTCBlue!55!white, line width=0.65pt] (55,91) -- (80,72);
  \draw[TTCBlue!55!white, line width=0.65pt] (55,38) -- (81,57);
  \draw[TTCBlue!55!white, line width=0.65pt] (131,91) -- (107,72);
  \draw[TTCRed!72!white, line width=0.75pt] (131,38) -- (106,57);

  % 01 — AIDC ConTech
  \node[
    anchor=north west, rounded corners=3pt,
    fill=white, fill opacity=0.94, text opacity=1,
    draw=TTCCyan!70!white, line width=0.65pt,
    minimum width=53mm, minimum height=29mm,
    text width=47mm, inner sep=3mm, align=left
  ] at (5,113) {
    {\fontsize{7.3}{8.5}\selectfont\bfseries\color{TTCCyan} 01 / AIDC CONTECH}\\[1mm]
    {\fontsize{10}{11.5}\selectfont\bfseries\color{TTCBlue} BIM 5D • AI • VALUE ENGINEERING}\\[1mm]
    {\fontsize{7}{8.6}\selectfont\color{TTCTextDark}Tối ưu thiết kế và dữ liệu dự án; tiết kiệm 10--15\% chi phí đầu tư.}
  };

  % 02 — MEP & PCCC
  \node[
    anchor=south west, rounded corners=3pt,
    fill=white, fill opacity=0.94, text opacity=1,
    draw=TTCBlue!42!white, line width=0.65pt,
    minimum width=53mm, minimum height=29mm,
    text width=47mm, inner sep=3mm, align=left
  ] at (5,5) {
    {\fontsize{7.3}{8.5}\selectfont\bfseries\color{TTCBlue} 02 / MEP \& PCCC}\\[1mm]
    {\fontsize{10}{11.5}\selectfont\bfseries\color{TTCBlue} HỆ THỐNG ĐỒNG BỘ TRÊN BIM}\\[1mm]
    {\fontsize{7}{8.6}\selectfont\color{TTCTextDark}Điện • HVAC • cấp thoát nước • phòng cháy, phối hợp xuyên suốt một mô hình.}
  };

  % 03 — Hạ tầng
  \node[
    anchor=north east, rounded corners=3pt,
    fill=white, fill opacity=0.94, text opacity=1,
    draw=TTCBlue!42!white, line width=0.65pt,
    minimum width=53mm, minimum height=29mm,
    text width=47mm, inner sep=3mm, align=left
  ] at (181,113) {
    {\fontsize{7.3}{8.5}\selectfont\bfseries\color{TTCBlue} 03 / HẠ TẦNG KCN}\\[1mm]
    {\fontsize{10}{11.5}\selectfont\bfseries\color{TTCBlue} NỀN MÓNG • ĐƯỜNG • THOÁT NƯỚC}\\[1mm]
    {\fontsize{7}{8.6}\selectfont\color{TTCTextDark}Hạ tầng kỹ thuật sẵn sàng vận hành, kết nối đồng bộ với tổng mặt bằng nhà máy.}
  };

  % 04 — PEB LAST
  \node[
    anchor=south east, rounded corners=3pt,
    fill=white, fill opacity=0.96, text opacity=1,
    draw=TTCRed!78!white, line width=0.8pt,
    minimum width=53mm, minimum height=29mm,
    text width=47mm, inner sep=3mm, align=left
  ] at (181,5) {
    {\fontsize{7.3}{8.5}\selectfont\bfseries\color{TTCRed} 04 / PEB MANUFACTURING}\\[1mm]
    {\fontsize{10}{11.5}\selectfont\bfseries\color{TTCBlue} SẢN XUẤT KẾT CẤU THÉP}\\[1mm]
    {\fontsize{7}{8.6}\selectfont\color{TTCTextDark}CNC • SAW • AWS D1.1 • NDT; năng lực cung ứng 30.000 tấn/năm.}
  };

  % Central accountability hub
  \node[
    rounded corners=3pt, fill=TTCDeepNavy!96!black,
    draw=TTCCyan!75!white, line width=0.9pt,
    minimum width=50mm, minimum height=28mm,
    text=white, align=center, inner sep=2.5mm
  ] at (93,64) {
    {\fontsize{11}{12.5}\selectfont\bfseries TÂN THÀNH CÔNG}\\[1mm]
    {\fontsize{7.5}{9}\selectfont\bfseries\color{TTCCyan} EPC SYSTEM INTEGRATOR}\\[1mm]
    {\fontsize{6.8}{8}\selectfont\color{white!78!gray}One contract • One accountability}
  };

  \draw[white, line width=1.2pt, rounded corners=3pt] (0.6,0.6) rectangle (185.4,117.4);
  \draw[TTCBorder, line width=0.65pt, rounded corners=3pt] (0,0) rectangle (186,118);
\end{tikzpicture}

\vspace{3mm}

% DELIVERY FLOW — PEB NẰM CUỐI TRONG CHUỖI NĂNG LỰC
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,31);
  \fill[TTCLightBlue, rounded corners=4pt] (0,0) rectangle (186,31);
  \draw[TTCBorder, line width=0.65pt, rounded corners=4pt] (0,0) rectangle (186,31);

  \node[align=center] at (18,15.5) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCTextMuted} 01}\\[0.7mm]
    {\fontsize{9.2}{10.5}\selectfont\bfseries\color{TTCBlue} KHẢO SÁT}\\[0.7mm]
    {\fontsize{6.6}{8}\selectfont Hiện trạng \& yêu cầu}
  };
  \node[align=center] at (55.5,15.5) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCTextMuted} 02}\\[0.7mm]
    {\fontsize{9.2}{10.5}\selectfont\bfseries\color{TTCBlue} THIẾT KẾ}\\[0.7mm]
    {\fontsize{6.6}{8}\selectfont BIM • AI • VE}
  };
  \node[align=center] at (93,15.5) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCTextMuted} 03}\\[0.7mm]
    {\fontsize{9.2}{10.5}\selectfont\bfseries\color{TTCBlue} HẠ TẦNG}\\[0.7mm]
    {\fontsize{6.6}{8}\selectfont Nền móng • tiện ích}
  };
  \node[align=center] at (130.5,15.5) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCTextMuted} 04}\\[0.7mm]
    {\fontsize{9.2}{10.5}\selectfont\bfseries\color{TTCBlue} MEP \& PCCC}\\[0.7mm]
    {\fontsize{6.6}{8}\selectfont Tích hợp hệ thống}
  };
  \node[align=center] at (168,15.5) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCRed} 05}\\[0.7mm]
    {\fontsize{9.2}{10.5}\selectfont\bfseries\color{TTCRed} PEB}\\[0.7mm]
    {\fontsize{6.6}{8}\selectfont Sản xuất • lắp dựng}
  };

  \foreach \x in {36.75,74.25,111.75,149.25}{
    \node[text=TTCRed, font=\fontsize{8}{9}\selectfont] at (\x,15.5) {\faChevronRight};
  }
\end{tikzpicture}

\vspace{3mm}

% THREE BUSINESS OUTCOMES — LIGHTER THAN THE OLD DARK KPI BAND
\noindent
\begin{tabular}{@{}p{58mm}@{\hspace{6mm}}p{58mm}@{\hspace{6mm}}p{58mm}@{}}
  \begin{tikzpicture}
    \node[
      rounded corners=4pt, fill=white, draw=TTCBorder,
      line width=0.65pt, minimum width=58mm, minimum height=35mm,
      text width=50mm, inner sep=4mm, align=left
    ] {
      {\fontsize{7}{8}\selectfont\bfseries\color{TTCRed} 01 / ACCOUNTABILITY}\\[1mm]
      {\fontsize{14}{15.5}\selectfont\bfseries\color{TTCBlue} 01 ĐẦU MỐI}\\[1mm]
      {\fontsize{7}{8.5}\selectfont\color{TTCTextDark}Một tổng thầu chịu trách nhiệm xuyên suốt từ thiết kế đến bàn giao.}
    };
  \end{tikzpicture}
  &
  \begin{tikzpicture}
    \node[
      rounded corners=4pt, fill=white, draw=TTCBorder,
      line width=0.65pt, minimum width=58mm, minimum height=35mm,
      text width=50mm, inner sep=4mm, align=left
    ] {
      {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} 02 / OPTIMIZATION}\\[1mm]
      {\fontsize{14}{15.5}\selectfont\bfseries\color{TTCBlue} TỐI ƯU CHI PHÍ}\\[1mm]
      {\fontsize{7}{8.5}\selectfont\color{TTCTextDark}AI và Value Engineering tối ưu giải pháp kỹ thuật, tiết kiệm 10--15\% chi phí đầu tư.}
    };
  \end{tikzpicture}
  &
  \begin{tikzpicture}
    \node[
      rounded corners=4pt, fill=white, draw=TTCBorder,
      line width=0.65pt, minimum width=58mm, minimum height=35mm,
      text width=50mm, inner sep=4mm, align=left
    ] {
      {\fontsize{7}{8}\selectfont\bfseries\color{TTCBlue} 03 / INTEGRATION}\\[1mm]
      {\fontsize{14}{15.5}\selectfont\bfseries\color{TTCBlue} 100\% KHÉP KÍN}\\[1mm]
      {\fontsize{7}{8.5}\selectfont\color{TTCTextDark}Dữ liệu, kỹ thuật và thi công cùng vận hành trong một hệ sinh thái.}
    };
  \end{tikzpicture}
\end{tabular}

\vspace{3mm}

% TRUST STRIP — INTERNATIONAL CONTROL STANDARDS
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,24);
  \fill[white, rounded corners=4pt] (0,0) rectangle (186,24);
  \draw[TTCBorder, line width=0.65pt, rounded corners=4pt] (0,0) rectangle (186,24);
  \fill[TTCLightBlue, rounded corners=4pt] (0,0) rectangle (43,24);
  \draw[TTCBorder, line width=0.55pt] (43,3) -- (43,21);

  \node[anchor=west, align=left] at (5,12) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} DELIVERY ASSURANCE}\\[0.8mm]
    {\fontsize{9}{10.5}\selectfont\bfseries\color{TTCBlue} NỀN TẢNG KIỂM SOÁT}\\[0.6mm]
    {\fontsize{6.4}{7.8}\selectfont\color{TTCTextMuted} Standards behind every project}
  };
  \node[align=center] at (61,12) {
    {\fontsize{11}{12.5}\selectfont\bfseries\color{TTCBlue} ISO 9001}\\[0.8mm]
    {\fontsize{6.5}{8}\selectfont\color{TTCTextMuted} Quality}
  };
  \node[align=center] at (94,12) {
    {\fontsize{11}{12.5}\selectfont\bfseries\color{TTCBlue} ISO 14001}\\[0.8mm]
    {\fontsize{6.5}{8}\selectfont\color{TTCTextMuted} Environment}
  };
  \node[align=center] at (130,12) {
    {\fontsize{11}{12.5}\selectfont\bfseries\color{TTCBlue} ISO 45001}\\[0.8mm]
    {\fontsize{6.5}{8}\selectfont\color{TTCTextMuted} Health \& Safety}
  };
  \node[align=center] at (167,12) {
    {\fontsize{11}{12.5}\selectfont\bfseries\color{TTCRed} HẠNG II}\\[0.8mm]
    {\fontsize{6.5}{8}\selectfont\color{TTCTextMuted} Bộ Xây Dựng}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_06_LEGACY = r"""% ============================================================
% TRANG 06: CƠ CẤU TỔ CHỨC & HỒ SƠ PHÁP LÝ HẠNG II
% ============================================================
\pageheaderbar{CƠ CẤU TỔ CHỨC \& PHÁP LÝ HẠNG II BXD}{Trang 06}
\pagefooterbar{Trang 06}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.03, scale=2.8, font=\bfseries\sffamily, text=TTCBlue] at ([yshift=-10mm]current page.center) {ORGANIZATIONAL STRUCTURE \& GRADE II LICENCE};
  \draw[TTCBlue!6!white, line width=0.5pt] ([xshift=15mm, yshift=20mm]current page.south west) grid[step=8mm] ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Sơ Đồ Cơ Cấu Tổ Chức \& Hồ Sơ Năng Lực Pháp Lý Hạng II}{Corporate Governance Structure, Grade II Construction License \& International ISO Systems}

% TẦNG 1: SƠ ĐỒ CƠ CẤU TỔ CHỨC TIKZ
\noindent
\begin{tikzpicture}[
  box/.style={rounded corners=3pt, align=center, inner sep=3pt, font=\fontsize{6.8}{8}\selectfont},
  cbox/.style={box, text=white, font=\fontsize{7.2}{8.5}\selectfont\bfseries},
  line/.style={draw=TTCBlue, line width=0.9pt}
]
  \draw[TTCBlue!40!white, line width=0.9pt, fill=white, rounded corners=6pt] (-9.3,-4.2) rectangle (9.3, 4.4);

  % Root BOD
  \node[cbox, fill=TTCDeepNavy, draw=TTCCyan!80!white, minimum width=72mm, minimum height=8mm] (bod) at (0, 3.7) {
    \faUsers\quad ĐẠI HỘI ĐỒNG CỔ ĐÔNG \& HỘI ĐỒNG QUẢN TRỊ
  };

  % CEO
  \node[cbox, fill=TTCRed, draw=white, minimum width=62mm, minimum height=8mm] (ceo) at (0, 2.4) {
    \faUserTie\quad TỔNG GIÁM ĐỐC (Ông PHẠM HUY TÂN)
  };

  % Advisors
  \node[box, fill=TTCLightBlue, draw=TTCBorder, text=TTCBlue, minimum width=42mm] (adv) at (-6.5, 2.4) {
    \textbf{Hội Đồng Cố Vấn Quốc Tế}
  };
  \node[box, fill=TTCLightBlue, draw=TTCCyan, text=TTCBlue, minimum width=42mm] (aidc) at (6.5, 2.4) {
    \textbf{R\&D Công Nghệ AIDC}
  };

  % 3 VPs
  \node[cbox, fill=TTCBlue, draw=white, minimum width=52mm] (d1) at (0, 1.1) {\textbf{P.TGĐ KỸ THUẬT \& BIM}};
  \node[cbox, fill=TTCLightBlue, draw=TTCBlue!60!white, text=TTCBlue, minimum width=52mm, left=4mm of d1] (d2) {\textbf{P.TGĐ DỰ ÁN \& QL THI CÔNG}};
  \node[cbox, fill=TTCLightBlue, draw=TTCBlue!60!white, text=TTCBlue, minimum width=52mm, right=4mm of d1] (d3) {\textbf{P.TGĐ TÀI CHÍNH \& FIDIC}};

  % Department Nodes
  \node[box, fill=white, draw=TTCBorder, text width=48mm, align=left] (f2) at (-5.6, -0.6) {
    \textbf{\color{TTCBlue}\faTools\ Khối Dự Án \& Thi Công:}\newline
    {\fontsize{6.2}{7.5}\selectfont
    \textbullet\ Ban Điều hành Dự án FDI\newline
    \textbullet\ Phòng Quản lý Thi công \& Cơ giới\newline
    \textbullet\ Phòng An toàn HSE \& QA/QC}
  };

  \node[box, fill=white, draw=TTCBorder, text width=48mm, align=left] (f1) at (0, -0.6) {
    \textbf{\color{TTCBlue}\faDraftingCompass\ Khối Kỹ Thuật \& BIM:}\newline
    {\fontsize{6.2}{7.5}\selectfont
    \textbullet\ Phòng Thiết kế VE \& Kết cấu thép\newline
    \textbullet\ Ban Mô hình BIM 5D \& Số hóa\newline
    \textbullet\ Phòng Pháp lý, Quy hoạch \& PCCC}
  };

  \node[box, fill=white, draw=TTCBorder, text width=48mm, align=left] (f3) at (5.6, -0.6) {
    \textbf{\color{TTCBlue}\faFileInvoiceDollar\ Khối Tài Chính \& Hợp Đồng:}\newline
    {\fontsize{6.2}{7.5}\selectfont
    \textbullet\ Phòng Đấu thầu \& Hợp đồng FIDIC\newline
    \textbullet\ Ban Tài chính \& Dòng tiền EPC\newline
    \textbullet\ Phòng Chuỗi cung ứng Tier-1}
  };

  % Site Command Board
  \node[cbox, fill=TTCDeepNavy!95!black, draw=TTCCyan!80!white, minimum width=172mm, minimum height=14mm] (bch) at (0, -2.8) {
    \textbf{\color{TTCCyan}\faHardHat\ BAN CHỈ HUY CÔNG TRƯỜNG THỰC CHIẾN (DỰ ÁN FDI \& TRONG NƯỚC)}\\[2pt]
    {\fontsize{6.5}{8}\selectfont\color{white!90!gray}
    Chỉ Huy Trưởng Hạng II \textbullet\ Kỹ Sư Giám Sát Kết Cấu \textbullet\ Kỹ Sư Cơ Điện MEP \textbullet\ Đội Ngũ HSE \& QA/QC Thường Trú}
  };

  % Lines
  \draw[line] (bod) -- (ceo);
  \draw[line, dashed] (adv) -- (ceo);
  \draw[line, dashed] (aidc) -- (ceo);
  \draw[line] (ceo) -- (d1);
  \draw[line] (d1) -| (d2);
  \draw[line] (d1) -| (d3);
  \draw[line] (d2) -- (f2);
  \draw[line] (d1) -- (f1);
  \draw[line] (d3) -- (f3);
  \draw[line] (f2.south) |- (bch.west);
  \draw[line] (f1.south) -- (bch.north);
  \draw[line] (f3.south) |- (bch.east);
\end{tikzpicture}

\vspace{2mm}

% TẦNG 2: BẢNG HỒ SƠ PHÁP LÝ HẠNG II & CHỨNG NHẬN QUỐC TẾ
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
    {\fontsize{9}{11}\selectfont\bfseries\color{TTCBlue} \faCertificate\quad BẢNG QUY CHUẨN PHÁP LÝ NĂNG LỰC HẠNG II \& HỆ THỐNG ISO QUỐC TẾ:}\\[3pt]
    \begin{tabularx}{\linewidth}{@{}p{86mm}@{\hspace{4mm}}p{86mm}@{}}
      \textbf{\color{TTCRed}1. CHỨNG CHỈ NĂNG LỰC HOẠT ĐỘNG HẠNG II (BXD):} &
      \textbf{\color{TTCBlue}3. HỆ THỐNG QUẢN LÝ MÔI TRƯỜNG ISO 14001:2015:} \\
      {\fontsize{6.8}{8.5}\selectfont
      \textbullet\ Do Bộ Xây Dựng cấp phép chính thức.\newline
      \textbullet\ Năng lực Tổng thầu Thiết kế \& Thi công công trình công nghiệp quy mô sàn không giới hạn ($>100.000$ m$^2$).\newline
      \textbullet\ Năng lực thi công dầm thép vượt nhịp khẩu độ lớn $>60$m.} &
      {\fontsize{6.8}{8.5}\selectfont
      \textbullet\ Kiểm soát bụi, tiếng ồn, nước thải thi công đạt chuẩn.\newline
      \textbullet\ Ưu tiên vật liệu Low-Carbon và công nghệ xanh ESG.\newline
      \textbullet\ Đồng hành đạt chứng chỉ LEED Gold/Platinum.} \\[3pt]
      \textbf{\color{TTCBlue}2. HỆ THỐNG QUẢN LÝ CHẤT LƯỢNG ISO 9001:2015:} &
      \textbf{\color{TTCGold}4. AN TOÀN \& SỨC KHỎE NGHỀ NGHIỆP ISO 45001:2018:} \\
      {\fontsize{6.8}{8.5}\selectfont
      \textbullet\ Kiểm soát chất lượng thiết kế VE, chuỗi gia công PEB và thi công.\newline
      \textbullet\ Quy trình nghiệm thu 4 tầng ITP chặt chẽ hiện trường.\newline
      \textbullet\ 100\% cấu kiện có chứng chỉ xuất xưởng CO/CQ gốc.} &
      {\fontsize{6.8}{8.5}\selectfont
      \textbullet\ Chính sách Zero Accident tại 100\% công trường.\newline
      \textbullet\ Cấp thẻ an toàn nhóm 3 và khám sức khỏe định kỳ.\newline
      \textbullet\ Trang bị 100\% bảo hộ lao động tiêu chuẩn Châu Âu 3M.}
    \end{tabularx}
  };
\end{tikzpicture}

\vspace{2mm}

% TẦNG 3: BĂNG HUY HIỆU
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
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCCyan} ISO 9001:2015} &
      {\fontsize{14}{16}\selectfont\bfseries\color{white} ISO 14001:2015} &
      {\fontsize{14}{16}\selectfont\bfseries\color{TTCGold} ISO 45001:2018} \\
      {\fontsize{7.2}{9}\selectfont Tổng Thầu EPC Cấp II} &
      {\fontsize{7.2}{9}\selectfont Quản Lý Chất Lượng} &
      {\fontsize{7.2}{9}\selectfont Quản Lý Môi Trường} &
      {\fontsize{7.2}{9}\selectfont An Toàn Sức Khỏe LĐ}
    \end{tabularx}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_06 = r"""% ============================================================
% TRANG 06: GOVERNANCE & COMPLIANCE DASHBOARD
% ============================================================
\pageheaderbar{CƠ CẤU TỔ CHỨC \& PHÁP LÝ HẠNG II BXD}{Trang 06}
\pagefooterbar{Trang 06}

\begin{tikzpicture}[remember picture, overlay]
  \draw[TTCBlue!6!white, line width=0.45pt]
    ([xshift=15mm,yshift=18mm]current page.south west)
    grid[step=8mm]
    ([xshift=195mm,yshift=42mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Quản Trị Tinh Gọn \& Nền Tảng Tuân Thủ}{Governance Structure, Grade II Construction License \& International ISO Systems}

\vspace{1mm}
{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
QUYỀN HẠN RÕ RÀNG • TRÁCH NHIỆM XUYÊN SUỐT DỰ ÁN\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
An execution-led governance model connecting board oversight directly to every project site.\par}
\vspace{3mm}

% GOVERNANCE MAP
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,105);
  \fill[white, rounded corners=4pt] (0,0) rectangle (186,105);
  \draw[TTCBorder, line width=0.7pt, rounded corners=4pt] (0,0) rectangle (186,105);

  \node[anchor=west, align=left] at (6,99) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} DELIVERY GOVERNANCE}\\[-0.2mm]
    {\fontsize{9.5}{11}\selectfont\bfseries\color{TTCBlue} CẤU TRÚC ĐIỀU HÀNH THEO DÒNG TRÁCH NHIỆM}
  };
  \draw[TTCBorder, line width=0.5pt] (6,91.5) -- (180,91.5);

  % Connector architecture, drawn behind nodes
  \draw[TTCBlue!65!white, line width=0.75pt] (93,83) -- (93,75);
  \draw[TTCBlue!65!white, line width=0.75pt] (93,66) -- (93,61);
  \draw[TTCBlue!65!white, line width=0.75pt] (32,61) -- (154,61);
  \draw[TTCBlue!65!white, line width=0.75pt] (32,61) -- (32,57);
  \draw[TTCBlue!65!white, line width=0.75pt] (93,61) -- (93,57);
  \draw[TTCBlue!65!white, line width=0.75pt] (154,61) -- (154,57);
  \draw[TTCBlue!65!white, line width=0.75pt] (32,48) -- (32,43);
  \draw[TTCBlue!65!white, line width=0.75pt] (93,48) -- (93,43);
  \draw[TTCBlue!65!white, line width=0.75pt] (154,48) -- (154,43);
  \draw[TTCBlue!55!white, line width=0.65pt] (32,21) -- (32,16);
  \draw[TTCBlue!55!white, line width=0.65pt] (93,21) -- (93,16);
  \draw[TTCBlue!55!white, line width=0.65pt] (154,21) -- (154,16);
  \draw[TTCBlue!55!white, line width=0.65pt] (32,16) -- (154,16);
  \draw[TTCBlue!55!white, line width=0.65pt] (93,16) -- (93,13);
  \draw[TTCBlue!42!white, line width=0.6pt, dashed] (46,70.5) -- (62,70.5);
  \draw[TTCCyan!80!white, line width=0.6pt, dashed] (124,70.5) -- (140,70.5);

  % Board & executive leadership
  \node[
    rounded corners=3pt, fill=TTCDeepNavy, text=white,
    minimum width=78mm, minimum height=10mm, align=center
  ] at (93,83) {
    {\fontsize{7.8}{9.2}\selectfont\bfseries
    \faUsers\quad ĐẠI HỘI ĐỒNG CỔ ĐÔNG \& HỘI ĐỒNG QUẢN TRỊ}
  };
  \node[
    rounded corners=3pt, fill=TTCLightBlue, draw=TTCBorder,
    minimum width=42mm, minimum height=9mm, align=center
  ] at (25,70.5) {
    {\fontsize{7}{8.3}\selectfont\bfseries\color{TTCBlue} HỘI ĐỒNG CỐ VẤN QUỐC TẾ}
  };
  \node[
    rounded corners=3pt, fill=TTCRed, text=white,
    minimum width=62mm, minimum height=11mm, align=center
  ] at (93,70.5) {
    {\fontsize{8.2}{9.5}\selectfont\bfseries
    \faUserTie\quad TỔNG GIÁM ĐỐC}\\[0.5mm]
    {\fontsize{6.7}{8}\selectfont Ông PHẠM HUY TÂN}
  };
  \node[
    rounded corners=3pt, fill=TTCLightBlue, draw=TTCCyan,
    minimum width=42mm, minimum height=9mm, align=center
  ] at (161,70.5) {
    {\fontsize{7}{8.3}\selectfont\bfseries\color{TTCBlue}
    \faMicrochip\quad R\&D CÔNG NGHỆ AIDC}
  };

  % Three accountable executive streams
  \node[
    rounded corners=3pt, fill=TTCBlue, text=white,
    minimum width=54mm, minimum height=10mm, align=center
  ] at (32,52.5) {
    {\fontsize{7.4}{8.8}\selectfont\bfseries P.TGĐ DỰ ÁN \& THI CÔNG}
  };
  \node[
    rounded corners=3pt, fill=TTCBlue, text=white,
    minimum width=54mm, minimum height=10mm, align=center
  ] at (93,52.5) {
    {\fontsize{7.4}{8.8}\selectfont\bfseries P.TGĐ KỸ THUẬT \& BIM}
  };
  \node[
    rounded corners=3pt, fill=TTCBlue, text=white,
    minimum width=54mm, minimum height=10mm, align=center
  ] at (154,52.5) {
    {\fontsize{7.4}{8.8}\selectfont\bfseries P.TGĐ TÀI CHÍNH \& FIDIC}
  };

  % Functional teams
  \node[
    rounded corners=3pt, fill=white, draw=TTCBorder,
    minimum width=54mm, minimum height=22mm,
    text width=47mm, inner sep=3mm, align=left
  ] at (32,32) {
    {\fontsize{7.1}{8.4}\selectfont\bfseries\color{TTCBlue}\faHardHat\ PROJECT DELIVERY}\\[1mm]
    {\fontsize{6.7}{8.2}\selectfont\color{TTCTextDark}
    • Ban điều hành dự án FDI\\
    • Quản lý thi công \& cơ giới\\
    • HSE \& QA/QC hiện trường}
  };
  \node[
    rounded corners=3pt, fill=white, draw=TTCBorder,
    minimum width=54mm, minimum height=22mm,
    text width=47mm, inner sep=3mm, align=left
  ] at (93,32) {
    {\fontsize{7.1}{8.4}\selectfont\bfseries\color{TTCBlue}\faDraftingCompass\ ENGINEERING}\\[1mm]
    {\fontsize{6.7}{8.2}\selectfont\color{TTCTextDark}
    • Value Engineering \& kết cấu\\
    • BIM 5D \& quản trị dữ liệu\\
    • Quy hoạch, pháp lý \& PCCC}
  };
  \node[
    rounded corners=3pt, fill=white, draw=TTCBorder,
    minimum width=54mm, minimum height=22mm,
    text width=47mm, inner sep=3mm, align=left
  ] at (154,32) {
    {\fontsize{7.1}{8.4}\selectfont\bfseries\color{TTCBlue}\faFileInvoiceDollar\ COMMERCIAL}\\[1mm]
    {\fontsize{6.7}{8.2}\selectfont\color{TTCTextDark}
    • Đấu thầu \& hợp đồng FIDIC\\
    • Tài chính \& dòng tiền EPC\\
    • Chuỗi cung ứng Tier-1}
  };

  % Site execution layer
  \node[
    rounded corners=3pt, fill=TTCDeepNavy, draw=TTCCyan,
    line width=0.75pt, text=white,
    minimum width=174mm, minimum height=12mm, align=center
  ] at (93,8) {
    {\fontsize{7.7}{9}\selectfont\bfseries\color{TTCCyan}
    \faHardHat\quad BAN CHỈ HUY CÔNG TRƯỜNG — QUYỀN HẠN TẠI ĐIỂM THỰC THI}\\[0.6mm]
    {\fontsize{6.5}{7.8}\selectfont\color{white!82!gray}
    Chỉ huy trưởng Hạng II • Kỹ sư kết cấu • MEP • HSE • QA/QC thường trú}
  };
\end{tikzpicture}

\vspace{3mm}

% COMPLIANCE PASSPORT
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,72);
  \fill[TTCLightBlue, rounded corners=4pt] (0,0) rectangle (186,72);
  \draw[TTCBorder, line width=0.7pt, rounded corners=4pt] (0,0) rectangle (186,72);

  \node[anchor=west, align=left] at (6,66) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} COMPLIANCE PASSPORT}\\[-0.2mm]
    {\fontsize{9.5}{11}\selectfont\bfseries\color{TTCBlue}
    NĂNG LỰC PHÁP LÝ \& HỆ THỐNG QUẢN LÝ ĐƯỢC KIỂM CHỨNG}
  };

  % Grade II anchor card
  \fill[white, rounded corners=3pt] (5,7) rectangle (58,57);
  \draw[TTCRed, line width=0.9pt, rounded corners=3pt] (5,7) rectangle (58,57);
  \node[align=center] at (31.5,45) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCRed} CONSTRUCTION LICENSE}\\[1mm]
    {\fontsize{22}{24}\selectfont\bfseries\color{TTCRed} HẠNG II}\\[-0.2mm]
    {\fontsize{9}{10.5}\selectfont\bfseries\color{TTCBlue} BỘ XÂY DỰNG}
  };
  \draw[TTCBorder, line width=0.5pt] (11,29) -- (52,29);
  \node[text width=42mm, align=left] at (31.5,18) {
    {\fontsize{6.6}{8.2}\selectfont\color{TTCTextDark}
    \textcolor{TTCRed}{\faCheckCircle}\ Tổng thầu thiết kế \& thi công\\
    \textcolor{TTCRed}{\faCheckCircle}\ Công trình công nghiệp quy mô lớn\\
    \textcolor{TTCRed}{\faCheckCircle}\ Kết cấu vượt nhịp lớn}
  };

  % ISO 9001
  \fill[white, rounded corners=3pt] (62,7) rectangle (100,57);
  \draw[TTCBorder, line width=0.6pt, rounded corners=3pt] (62,7) rectangle (100,57);
  \node[align=center] at (81,45) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} QUALITY}\\[1mm]
    {\fontsize{13}{14.5}\selectfont\bfseries\color{TTCBlue} ISO 9001}\\
    {\fontsize{7}{8.5}\selectfont\bfseries\color{TTCTextMuted} 2015}
  };
  \node[text width=30mm, align=center] at (81,20) {
    {\fontsize{6.6}{8.2}\selectfont\color{TTCTextDark}
    Kiểm soát thiết kế, vật tư, thi công và nghiệm thu theo ITP.}
  };

  % ISO 14001
  \fill[white, rounded corners=3pt] (103,7) rectangle (141,57);
  \draw[TTCBorder, line width=0.6pt, rounded corners=3pt] (103,7) rectangle (141,57);
  \node[align=center] at (122,45) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} ENVIRONMENT}\\[1mm]
    {\fontsize{13}{14.5}\selectfont\bfseries\color{TTCBlue} ISO 14001}\\
    {\fontsize{7}{8.5}\selectfont\bfseries\color{TTCTextMuted} 2015}
  };
  \node[text width=30mm, align=center] at (122,20) {
    {\fontsize{6.6}{8.2}\selectfont\color{TTCTextDark}
    Kiểm soát chất thải, tiếng ồn và ưu tiên giải pháp Low-Carbon.}
  };

  % ISO 45001
  \fill[white, rounded corners=3pt] (144,7) rectangle (182,57);
  \draw[TTCGold, line width=0.75pt, rounded corners=3pt] (144,7) rectangle (182,57);
  \node[align=center] at (163,45) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCGold} HEALTH \& SAFETY}\\[1mm]
    {\fontsize{13}{14.5}\selectfont\bfseries\color{TTCBlue} ISO 45001}\\
    {\fontsize{7}{8.5}\selectfont\bfseries\color{TTCTextMuted} 2018}
  };
  \node[text width=30mm, align=center] at (163,20) {
    {\fontsize{6.6}{8.2}\selectfont\color{TTCTextDark}
    Chính sách Zero Accident, đào tạo và kiểm soát an toàn tại chỗ.}
  };
\end{tikzpicture}

\vspace{3mm}

% PRE-QUALIFICATION CLOSING STRIP
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,24);
  \fill[white, rounded corners=4pt] (0,0) rectangle (186,24);
  \draw[TTCBorder, line width=0.7pt, rounded corners=4pt] (0,0) rectangle (186,24);
  \fill[TTCDeepNavy, rounded corners=4pt] (0,0) rectangle (47,24);
  \node[align=left, anchor=west] at (6,12) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} PRE-QUALIFICATION}\\[0.8mm]
    {\fontsize{10}{11.5}\selectfont\bfseries\color{white} READY FOR FDI}\\[0.5mm]
    {\fontsize{6.3}{7.6}\selectfont\color{white!72!gray}Legal • Quality • HSE}
  };
  \node[align=center] at (72,12) {
    {\fontsize{11}{12.5}\selectfont\bfseries\color{TTCBlue} 01}\\[0.6mm]
    {\fontsize{7}{8.3}\selectfont\bfseries\color{TTCTextDark} ĐẦU MỐI PHÁP LÝ}
  };
  \node[align=center] at (113,12) {
    {\fontsize{11}{12.5}\selectfont\bfseries\color{TTCBlue} 04}\\[0.6mm]
    {\fontsize{7}{8.3}\selectfont\bfseries\color{TTCTextDark} LỚP KIỂM SOÁT ITP}
  };
  \node[align=center] at (160,12) {
    {\fontsize{11}{12.5}\selectfont\bfseries\color{TTCRed} 100\%}\\[0.6mm]
    {\fontsize{7}{8.3}\selectfont\bfseries\color{TTCTextDark} CO/CQ TRUY XUẤT}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""




PAGE_07 = r"""% ============================================================
% TRANG 07: NĂNG LỰC NHÂN SỰ TRIỂN KHAI EPC
% ============================================================
\pageheaderbar{NĂNG LỰC NHÂN SỰ TRIỂN KHAI EPC}{Trang 07}
\pagefooterbar{Trang 07}

\begin{tikzpicture}[remember picture, overlay]
  \draw[TTCBlue!6!white, line width=0.45pt]
    ([xshift=15mm,yshift=18mm]current page.south west)
    grid[step=8mm]
    ([xshift=195mm,yshift=42mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{Đội Ngũ Tích Hợp Theo Vòng Đời Dự Án}{Integrated Project Team, Clear Accountability \& Site-Ready Mobilization}

\vspace{1mm}
{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
ĐÚNG NGƯỜI • ĐÚNG VAI TRÒ • ĐÚNG THỜI ĐIỂM\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
One accountable team mobilized from pre-construction through commissioning and warranty.\par}
\vspace{3mm}

% PEOPLE HERO
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,72);
  \clip[rounded corners=3pt] (0,0) rectangle (186,72);
  \node[anchor=center, inner sep=0pt] at (93,36)
    {\includegraphics[width=186mm]{../../public/engineer-team-site.jpg}};
  \fill[TTCDeepNavy, opacity=0.82] (0,0) rectangle (68,72);
  \fill[TTCDeepNavy, opacity=0.38] (68,0) rectangle (92,72);

  \node[anchor=west, text width=54mm, align=left, text=white] at (8,48) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} PEOPLE AT THE POINT OF EXECUTION}\\[1.5mm]
    {\fontsize{16}{18}\selectfont\bfseries CON NGƯỜI TẠI\\ĐIỂM THỰC THI}\\[2mm]
    {\fontsize{7.2}{9}\selectfont\color{white!84!gray}
    Đội ngũ dự án được tổ chức theo nhiệm vụ, có quyền hạn rõ ràng và một tuyến báo cáo duy nhất.}
  };

  \node[
    anchor=south east, rounded corners=3pt,
    fill=white, fill opacity=0.93, text opacity=1,
    draw=TTCCyan, line width=0.7pt,
    minimum width=52mm, minimum height=14mm, align=center
  ] at (179,7) {
    {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCBlue} FIELD-LED DECISION MAKING}\\[0.7mm]
    {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}Quyết định kỹ thuật được đưa đến gần hiện trường}
  };
  \draw[white, line width=1pt, rounded corners=3pt] (0.6,0.6) rectangle (185.4,71.4);
  \draw[TTCBorder, line width=0.65pt, rounded corners=3pt] (0,0) rectangle (186,72);
\end{tikzpicture}

\vspace{3mm}

% ACCOUNTABLE ROLES BY PROJECT PHASE
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,67);
  \node[anchor=west, align=left] at (0,62) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} PROJECT TEAM BY PHASE}\quad
    {\fontsize{9.5}{11}\selectfont\bfseries\color{TTCBlue} VAI TRÒ CHỊU TRÁCH NHIỆM THEO GIAI ĐOẠN}
  };

  % Phase 01
  \fill[white, rounded corners=3pt] (0,0) rectangle (58,55);
  \draw[TTCBorder, line width=0.65pt, rounded corners=3pt] (0,0) rectangle (58,55);
  \fill[TTCLightBlue, rounded corners=3pt] (0,43) rectangle (58,55);
  \node[anchor=west] at (5,49) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} 01 / PRE-CONSTRUCTION}
  };
  \node[anchor=north west, text width=48mm, align=left] at (5,39) {
    {\fontsize{9.5}{11}\selectfont\bfseries\color{TTCBlue} CHUẨN BỊ \& THIẾT KẾ}\\[1.2mm]
    {\fontsize{7}{8.6}\selectfont\color{TTCTextDark}
    \textbf{Project Director}\\
    Đầu mối duy nhất với Chủ đầu tư.\\[0.8mm]
    \textbf{Design \& BIM Lead}\\
    Điều phối thiết kế, VE và mô hình.\\[0.8mm]
    \textbf{Planning / QS / FIDIC}\\
    Khóa phạm vi, tiến độ và ngân sách.}
  };
  \node[anchor=south, align=center] at (29,3.5) {
    {\fontsize{6.5}{7.8}\selectfont\bfseries\color{TTCRed} OUTPUT: APPROVED BASELINE}
  };

  % Phase 02
  \fill[white, rounded corners=3pt] (64,0) rectangle (122,55);
  \draw[TTCBlue!55!white, line width=0.75pt, rounded corners=3pt] (64,0) rectangle (122,55);
  \fill[TTCBlue, rounded corners=3pt] (64,43) rectangle (122,55);
  \node[anchor=west] at (69,49) {
    {\fontsize{7}{8}\selectfont\bfseries\color{white} 02 / CONSTRUCTION}
  };
  \node[anchor=north west, text width=48mm, align=left] at (69,39) {
    {\fontsize{9.5}{11}\selectfont\bfseries\color{TTCBlue} THI CÔNG HIỆN TRƯỜNG}\\[1.2mm]
    {\fontsize{7}{8.6}\selectfont\color{TTCTextDark}
    \textbf{Construction / Site Manager}\\
    Nguồn lực • mặt bằng • mũi thi công.\\[0.5mm]
    \textbf{Discipline Engineers}\\
    Kết cấu • Hạ tầng • MEP • PCCC.\\[0.5mm]
    \textbf{HSE \& QA/QC Managers}\\
    Quyền kiểm soát độc lập.}
  };
  \node[anchor=south, align=center] at (93,2.5) {
    {\fontsize{6.5}{7.8}\selectfont\bfseries\color{TTCRed} OUTPUT: CONTROLLED EXECUTION}
  };

  % Phase 03
  \fill[white, rounded corners=3pt] (128,0) rectangle (186,55);
  \draw[TTCBorder, line width=0.65pt, rounded corners=3pt] (128,0) rectangle (186,55);
  \fill[TTCLightBlue, rounded corners=3pt] (128,43) rectangle (186,55);
  \node[anchor=west] at (133,49) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} 03 / HANDOVER \& O\&M}
  };
  \node[anchor=north west, text width=48mm, align=left] at (133,39) {
    {\fontsize{9.5}{11}\selectfont\bfseries\color{TTCBlue} BÀN GIAO \& VẬN HÀNH}\\[1.2mm]
    {\fontsize{7}{8.6}\selectfont\color{TTCTextDark}
    \textbf{Commissioning Manager}\\
    Điều phối thử nghiệm liên động.\\[0.8mm]
    \textbf{As-built \& Digital Twin Team}\\
    Chuẩn hóa hồ sơ và dữ liệu tài sản.\\[0.8mm]
    \textbf{Warranty Response Team}\\
    Tiếp nhận và xử lý kỹ thuật 24/7.}
  };
  \node[anchor=south, align=center] at (157,3.5) {
    {\fontsize{6.5}{7.8}\selectfont\bfseries\color{TTCRed} OUTPUT: READY FOR OPERATION}
  };
\end{tikzpicture}

\vspace{3mm}

% MOBILIZATION CHAIN — CLARIFIES HIERARCHY WITHOUT PORTRAIT PLACEHOLDERS
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,29);
  \fill[TTCLightBlue, rounded corners=4pt] (0,0) rectangle (186,29);
  \draw[TTCBorder, line width=0.65pt, rounded corners=4pt] (0,0) rectangle (186,29);

  \node[align=center] at (22,14.5) {
    {\fontsize{6.5}{7.8}\selectfont\bfseries\color{TTCTextMuted} GOVERNANCE}\\[0.7mm]
    {\fontsize{9.2}{10.5}\selectfont\bfseries\color{TTCBlue} PMO TRỤ SỞ}\\[0.5mm]
    {\fontsize{6.4}{7.6}\selectfont Portfolio control}
  };
  \node[text=TTCRed] at (45,14.5) {\faChevronRight};
  \node[align=center] at (68,14.5) {
    {\fontsize{6.5}{7.8}\selectfont\bfseries\color{TTCTextMuted} ACCOUNTABILITY}\\[0.7mm]
    {\fontsize{9.2}{10.5}\selectfont\bfseries\color{TTCBlue} PROJECT DIRECTOR}\\[0.5mm]
    {\fontsize{6.4}{7.6}\selectfont Single point}
  };
  \node[text=TTCRed] at (93,14.5) {\faChevronRight};
  \node[align=center] at (118,14.5) {
    {\fontsize{6.5}{7.8}\selectfont\bfseries\color{TTCTextMuted} SITE AUTHORITY}\\[0.7mm]
    {\fontsize{9.2}{10.5}\selectfont\bfseries\color{TTCBlue} BAN CHỈ HUY}\\[0.5mm]
    {\fontsize{6.4}{7.6}\selectfont Daily execution}
  };
  \node[text=TTCRed] at (141,14.5) {\faChevronRight};
  \node[align=center] at (164,14.5) {
    {\fontsize{6.5}{7.8}\selectfont\bfseries\color{TTCTextMuted} DELIVERY}\\[0.7mm]
    {\fontsize{9.2}{10.5}\selectfont\bfseries\color{TTCRed} ĐỘI CHUYÊN MÔN}\\[0.5mm]
    {\fontsize{6.4}{7.6}\selectfont Task-based crews}
  };
\end{tikzpicture}

\vspace{3mm}

% CAPACITY SNAPSHOT
\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,27);
  \fill[white, rounded corners=4pt] (0,0) rectangle (186,27);
  \draw[TTCBorder, line width=0.65pt, rounded corners=4pt] (0,0) rectangle (186,27);
  \foreach \x in {46.5,93,139.5}{
    \draw[TTCBorder, line width=0.5pt] (\x,5) -- (\x,22);
  }
  \node[align=center] at (23.25,13.5) {
    {\fontsize{14}{15.5}\selectfont\bfseries\color{TTCRed} 350+}\\[0.8mm]
    {\fontsize{6.8}{8}\selectfont\bfseries\color{TTCTextDark} QUẢN LÝ \& KỸ SƯ}
  };
  \node[align=center] at (69.75,13.5) {
    {\fontsize{14}{15.5}\selectfont\bfseries\color{TTCBlue} 2.500+}\\[0.8mm]
    {\fontsize{6.8}{8}\selectfont\bfseries\color{TTCTextDark} CÔNG NHÂN KỸ THUẬT}
  };
  \node[align=center] at (116.25,13.5) {
    {\fontsize{14}{15.5}\selectfont\bfseries\color{TTCCyan} 85+}\\[0.8mm]
    {\fontsize{6.8}{8}\selectfont\bfseries\color{TTCTextDark} CHỈ HUY \& GIÁM SÁT}
  };
  \node[align=center] at (162.75,13.5) {
    {\fontsize{14}{15.5}\selectfont\bfseries\color{TTCBlue} 60+}\\[0.8mm]
    {\fontsize{6.8}{8}\selectfont\bfseries\color{TTCTextDark} KỸ SƯ BIM \& SỐ HÓA}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

print("Section 1 code rewritten cleanly with compact Page 7.")
