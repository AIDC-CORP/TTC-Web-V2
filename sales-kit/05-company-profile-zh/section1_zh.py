# -*- coding: utf-8 -*-
"""
Section 1: Overview, Legal Entity, Leadership & Governance (Pages 01 - 07) — 简体中文版
"""

PAGE_01 = r"""% ============================================================
% TRANG 01: TRANG BÌA CHÍNH — COMPANY PROFILE 2026
% ============================================================
\thispagestyle{empty}
\begin{tikzpicture}[remember picture, overlay]
  % 1. Hero image
  \node[anchor=center, inner sep=0pt] at (current page.center) {
    \includegraphics[height=\paperheight]{../../public/executive-cover-hero.jpg}
  };

  % 2. Gradient overlay
  \shade[
    left color=TTCDeepNavy!96!black,
    right color=transparent,
    opacity=0.70
  ] (current page.south west) rectangle (current page.north east);

  % 3. TTC recognition bar and logo lock-up
  \fill[TTCRed] (current page.north west) rectangle ++(\paperwidth, -2.2mm);
  \node[anchor=north west, fill=white, fill opacity=0.96, text opacity=1,
        rounded corners=1.5pt, inner xsep=5mm, inner ysep=3.8mm]
    at ([xshift=15mm,yshift=-13mm]current page.north west) {
      \includegraphics[width=48mm]{../../public/logo-ttc-removebg-DNXrVdJp.png}
    };
  \node[anchor=north east, text=white, inner sep=0pt] at ([xshift=-15mm,yshift=-15mm]current page.north east) {
    {\fontsize{8}{10}\selectfont\bfseries COMPANY PROFILE \;|\; 2026}
  };

  % 4. Title block
  \node[anchor=west, align=left, text width=135mm, inner sep=0pt]
    at ([xshift=16mm,yshift=160mm]current page.south west) {
      {\fontsize{7.8}{9.6}\selectfont\bfseries\color{TTCRed} TAN THANH CONG TECHNOLOGY CONSTRUCTION JOINT STOCK COMPANY}\\[6mm]
      {\fontsize{42}{50}\selectfont\bfseries\color{white} 企业能力简介}\\[5mm]
      {\color{TTCRed}\rule{73mm}{2.8pt}}\\[5mm]
      {\fontsize{17}{20}\selectfont\bfseries\color{white} COMPANY PROFILE}\\[8mm]
      {\fontsize{15}{18}\selectfont\bfseries\color{white} 新一代工业 EPC 总承包商}\\[3mm]
      {\fontsize{9.5}{12}\selectfont\color{white!88!gray} Turnkey Industrial EPC General Contractor}
    };

  % 5. Proof points
  \node[anchor=south west, align=left, fill=TTCDeepNavy!92!black, fill opacity=0.84,
        text=white, text opacity=1, rounded corners=1.5pt, inner xsep=6mm, inner ysep=4mm]
    at ([xshift=15mm,yshift=31mm]current page.south west) {
      {\fontsize{12}{14}\selectfont\bfseries 150+ 工业项目 \qquad 建设部二级资质 \qquad ISO 9001 / 14001 / 45001}\\[1.2mm]
      {\fontsize{7}{8.5}\selectfont\color{white!82!gray}经现场验证的工业总承包综合实力}
    };

  % 6. Legal identity
  \node[anchor=south west, text=white, inner sep=0pt] at ([xshift=15mm,yshift=19mm]current page.south west) {
    {\fontsize{6.6}{8.2}\selectfont\bfseries 新成功建筑科技股份公司 \textbullet\ TAN THANH CONG TECH JSC}
  };

  % 7. Persistent contact footer
  \fill[TTCDeepNavy!97!black] (current page.south west) rectangle ++(\paperwidth, 11mm);
  \fill[TTCRed] ([yshift=11mm]current page.south west) rectangle ++(\paperwidth, 1.2mm);
  \node[anchor=south, text=white, inner sep=0pt] at ([yshift=3.4mm]current page.south) {
    {\fontsize{6.8}{8.2}\selectfont
      \faPhone\ +84 976 447 766 \quad\textbullet\quad
      \faEnvelope\ info@tanthanhcongjsc.com \quad\textbullet\quad
      \faGlobe\ tanthanhcongjsc.com \quad\textbullet\quad
      \faAward\ 越南建设部二级施工资质}
  };
\end{tikzpicture}
\mbox{}
\newpage
"""

PAGE_02 = r"""% ============================================================
% TRANG 02: MỤC LỤC ĐIỀU HƯỚNG & THÔNG TIN PHÁP NHÂN TÓM TẮT
% ============================================================
\pageheaderbar{总目录概览与法人信息}{第02页}
\pagefooterbar{第02页}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.025, scale=4.2, font=\bfseries\sffamily, text=TTCBlue]
    at ([xshift=30mm,yshift=-8mm]current page.center) {TTC};
  \fill[TTCRed, opacity=0.05] ([xshift=12mm,yshift=18mm]current page.south west)
    rectangle ([xshift=18mm,yshift=248mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{总目录概览}{Executive Contents — 06 Core Sections}

{\fontsize{9.2}{11.5}\selectfont\color{TTCTextMuted}
本报告按06大核心板块编排，便于业主快速查阅；各专题详见对应页面。}\\[3mm]

\newcommand{\toccard}[5]{%
  \begin{tikzpicture}
    \node[rounded corners=3pt, fill=white, draw=TTCBorder, line width=0.8pt,
          minimum width=90mm, minimum height=52mm, text width=79mm, inner sep=5.5mm, align=left] {
      {\fontsize{18}{19}\selectfont\bfseries\color{TTCRed} #1}\hspace{3mm}
      {\fontsize{8.2}{9.5}\selectfont\bfseries\color{TTCRed} 第 #2 页}\\[1.5mm]
      {\fontsize{11.2}{13.2}\selectfont\bfseries\color{TTCBlue} #3}\\[0.3mm]
      {\fontsize{7.2}{8.8}\selectfont\itshape\color{TTCTextMuted} #4}\\[3mm]
      {\fontsize{8.2}{10.5}\selectfont\color{TTCTextDark} #5}
    };
  \end{tikzpicture}%
}

\noindent
\begin{tabular}{@{}p{91mm}@{\hspace{4mm}}p{91mm}@{}}
\toccard{I}{01--07}{公司概况与核心能力}{Company profile \& credentials}{总经理致辞 \textbullet\ 愿景与价值观 \textbullet\ 产业生态 \textbullet\ 法人与管理团队} &
\toccard{IV}{14--19}{EPC解决方案与建筑科技}{EPC, ConTech \& ESG}{Fast-track快速推进 \textbullet\ BIM 5D/AI \textbullet\ ESG低碳 \textbullet\ QA/QC与HSE} \\[3.5mm]
\toccard{II}{08--10}{财务实力与精英团队}{Financial capacity \& people}{独立预算管控 \textbullet\ 2500亿授信担保 \textbullet\ 2850+人才 \textbullet\ 安全文化} &
\toccard{V}{20--30}{重点项目与国际客户}{Projects \& valued partners}{150+工业项目 \textbullet\ 06大经典案例 \textbullet\ 严控供应链 \textbullet\ FDI伙伴} \\[3.5mm]
\toccard{III}{11--13}{生产制造与FIDIC管理}{PEB \& project control}{3万吨PEB制造网络 \textbullet\ 3000亿重型机械 \textbullet\ FIDIC八阶段流程} &
\toccard{VI}{31--36}{金牌承诺与长期合作}{Commitments \& support}{资质荣誉 \textbullet\ 20+省市施工覆盖 \textbullet\ 战略愿景 \textbullet\ 24个月保修与联系}
\end{tabular}

\vspace{4.5mm}

\noindent
\begin{tikzpicture}
  \node[rounded corners=3pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.8pt,
        minimum width=186mm, text width=172mm, inner sep=7.5mm] {
    {\fontsize{10.5}{12.5}\selectfont\bfseries\color{TTCBlue} \faIdCard\quad 企业法人信息摘要}
    \hfill {\fontsize{7.2}{8.8}\selectfont\color{TTCRed}\bfseries 详细资质认证：第 06 页}\\[1.5mm]
    {\fontsize{6.2}{7.5}\selectfont\color{TTCTextMuted}\bfseries
    TAN THANH CONG TECHNOLOGY CONSTRUCTION JOINT STOCK COMPANY}\\[3mm]
    \renewcommand{\arraystretch}{1.28}
    {\fontsize{8.2}{10.2}\selectfont
    \begin{tabularx}{\linewidth}{@{}p{30mm}X@{\hspace{5mm}}p{28mm}X@{}}
      \textbf{企业名称} & \textbf{新成功建筑科技股份公司} (TTC JSC) &
      \textbf{税务登记号} & \textbf{0107090447} \\
      \textbf{法定代表人} & \textbf{范辉新 (PHẠM HUY TÂN)} — 总经理 &
      \textbf{资质等级} & 越南建设部二级资质 \textbullet\ ISO 9001/14001/45001 \\
      \textbf{注册地址} & Số 39, ngõ 292 Kim Giang, Đại Kim, Hà Nội &
      \textbf{办公地址} & Số 19N7B, KĐT Trung Hòa Nhân Chính, Hà Nội \\
      \textbf{联系电话} & +84 976 447 766 \textbullet\ info@tanthanhcongjsc.com &
      \textbf{官方网站} & tanthanhcongjsc.com
    \end{tabularx}}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_03 = r"""% ============================================================
% TRANG 03: THÔNG ĐIỆP TỪ TỔNG GIÁM ĐỐC — LEADERSHIP MESSAGE
% ============================================================
\pageheaderbar{总经理致辞}{第03页}
\pagefooterbar{第03页}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.025, scale=4.0, font=\bfseries\sffamily, text=TTCBlue]
    at ([xshift=-25mm,yshift=-25mm]current page.center) {LEADERSHIP};
  \fill[TTCRed, opacity=0.045] ([xshift=12mm,yshift=18mm]current page.south west)
    rectangle ([xshift=18mm,yshift=248mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{总经理致辞}{Leadership Message — Building Trust Through Every Commitment}

\vspace{2mm}

\noindent
\begin{tabular}{@{}p{106mm}@{\hspace{4mm}}p{76mm}@{}}
  \begin{tikzpicture}
    \path[use as bounding box] (0,0) rectangle (106mm,170mm);
    \draw[TTCRed, line width=2.2pt] (0,169mm) -- (26mm,169mm);
    \node[anchor=north west, align=left, text width=98mm, inner sep=0pt] at (0,165mm) {
      {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCRed} TTC 的核心经营理念}\\[4mm]
      {\fontsize{18}{22}\selectfont\bfseries\color{TTCBlue}
      “质量即荣誉。\\
      安全即生命。\\
      进度即承诺。”}\\[6mm]
      {\fontsize{10}{12}\selectfont\bfseries\color{TTCBlue}
      尊敬的投资方、客户及合作伙伴：}\\[3mm]
      {\fontsize{9}{13}\selectfont\color{TTCTextDark}
      我谨代表\textbf{新成功建筑科技股份公司}（TTC JSC）全体管理团队及员工，衷心感谢各位在TTC发展历程中所给予的坚定信任与支持。\\[3mm]

      十余年深耕工业建筑领域，让我们深刻理解：一个卓越的工程必须同时满足\textbf{质量、安全、进度与投资效益}。因此，TTC始终践行\textbf{EPC一站式总承包模式}，深度融合价值工程（Value Engineering）、BIM 5D协同与国际标准现场管理体系。\\[3mm]

      依托年产能30,000吨的PEB战略制造网络与实战型工程师团队，我们承诺为每座工厂量身定制最优技术方案，从方案设计、施工装配到竣工交付与全寿命运维实行全程透明管控。\\[3mm]

      TTC不仅是总承包商，更是与业主\textbf{共创长期价值的战略合作伙伴}。}\\[5mm]
      {\fontsize{9}{11}\selectfont\itshape\color{TTCTextMuted} 此致敬礼，}
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
        {\fontsize{7}{8.5}\selectfont\bfseries\color{TTCRed} 总经理 / CEO}\\[2mm]
        {\fontsize{14}{17}\selectfont\bfseries\color{white} 范辉新}\\[2mm]
        {\fontsize{7.5}{9.5}\selectfont\color{white!78!gray}
        新成功建筑科技股份公司}\\[4mm]
        {\fontsize{7.2}{9}\selectfont\bfseries\color{white!68!gray} TÂN THÀNH CÔNG \textbullet\ TTC JSC}
      };
  \end{tikzpicture}
\end{tabular}

\vspace{5mm}

\noindent
\begin{tabular}{@{}p{58mm}@{\hspace{6mm}}p{58mm}@{\hspace{6mm}}p{58mm}@{}}
  \begin{tikzpicture}
    \node[rounded corners=3pt, fill=TTCDeepNavy!97!black, minimum width=58mm,
          minimum height=43mm, text width=48mm, align=center, inner sep=5mm] {
      {\fontsize{17}{19}\selectfont\bfseries\color{white} 01}\\[1mm]
      {\fontsize{9}{11}\selectfont\bfseries\color{TTCRed} EPC一站式总包}\\[2mm]
      {\fontsize{7.3}{9}\selectfont\color{white!78!gray}Design \textbullet\ Build \textbullet\ Turnkey}
    };
  \end{tikzpicture}
  &
  \begin{tikzpicture}
    \node[rounded corners=3pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.8pt,
          minimum width=58mm, minimum height=43mm, text width=48mm, align=center, inner sep=5mm] {
      {\fontsize{17}{19}\selectfont\bfseries\color{TTCRed} 10--15\%}\\[1mm]
      {\fontsize{9}{11}\selectfont\bfseries\color{TTCBlue} 优化投资成本}\\[2mm]
      {\fontsize{7.3}{9}\selectfont\color{TTCTextMuted}Value Engineering}
    };
  \end{tikzpicture}
  &
  \begin{tikzpicture}
    \node[rounded corners=3pt, fill=TTCLightBlue, draw=TTCBorder, line width=0.8pt,
          minimum width=58mm, minimum height=43mm, text width=48mm, align=center, inner sep=5mm] {
      {\fontsize{15}{18}\selectfont\bfseries\color{TTCRed} ZERO}\\[1mm]
      {\fontsize{9}{11}\selectfont\bfseries\color{TTCBlue} 零事故安全}\\[2mm]
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
    共创长期价值 \quad\textbullet\quad BUILDING ENDURING VALUE}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_04 = r"""% ============================================================
% TRANG 04: KẾT CẤU VƯƠN CAO — HÀNH TRÌNH & GIÁ TRỊ CỐT LÕI
% ============================================================
\pageheaderbar{发展历程与核心价值观}{第04页}
\pagefooterbar{第04页}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.022, scale=4.0, font=\bfseries\sffamily, text=TTCBlue]
    at ([xshift=15mm,yshift=-18mm]current page.center) {BUILDING THE FUTURE};
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{发展历程与核心价值观}{From Mechanical Foundations to a Next-Generation EPC General Contractor}

\vspace{1mm}

\noindent
\begin{tikzpicture}
  \node[anchor=west, align=left, inner sep=0pt] at (0,7mm) {
    {\fontsize{16}{19}\selectfont\bfseries\color{TTCBlue}
    从精密机械基础到新一代工业EPC总承包商}\\[1.5mm]
    {\fontsize{7.8}{9.5}\selectfont\color{TTCTextMuted}
    以坚实执行力、数字化技术与永恒核心价值观铸就的发展之路。}
  };
  \fill[TTCRed] (0,0) rectangle (52mm,1.4mm);
\end{tikzpicture}

\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,112);
  \fill[TTCLightBlue!55!white] (0,0) rectangle (186,112);
  \draw[TTCBorder, line width=0.8pt, rounded corners=3pt] (0,0) rectangle (186,112);
  \draw[TTCBlue!7!white, line width=0.35pt] (0,0) grid[step=10mm] (186,112);

  % Stepped structural spine
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
    {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCBlue} 创立起步}\\[1mm]
    {\fontsize{7.2}{9}\selectfont\color{TTCTextDark}精密机械加工与钢结构\\工程安装技术积累。}
  };

  % 2018
  \fill[white] (55,40) circle (3.4);
  \draw[TTCRed, line width=1.5pt] (55,40) circle (3.4);
  \fill[TTCRed] (55,40) circle (1.35);
  \node[anchor=north west, align=left, text width=38mm, fill=TTCLightBlue!86!white,
        fill opacity=0.94, text opacity=1, rounded corners=1.5pt, inner sep=1mm] at (38,29) {
    {\fontsize{18}{20}\selectfont\bfseries\color{TTCRed} 2018}\\[-0.5mm]
    {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCBlue} 扩张跨越}\\[1mm]
    {\fontsize{7.2}{9}\selectfont\color{TTCTextDark}PEB联合制造网络与\\工业园区基建总承包。}
  };

  % 2022
  \fill[white] (94,61) circle (3.4);
  \draw[TTCRed, line width=1.5pt] (94,61) circle (3.4);
  \fill[TTCRed] (94,61) circle (1.35);
  \node[anchor=south west, align=left, text width=39mm, fill=TTCLightBlue!86!white,
        fill opacity=0.94, text opacity=1, rounded corners=1.5pt, inner sep=1mm] at (71,67) {
    {\fontsize{18}{20}\selectfont\bfseries\color{TTCRed} 2022}\\[-0.5mm]
    {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCBlue} 资质突破}\\[1mm]
    {\fontsize{7.2}{9}\selectfont\color{TTCTextDark}获建设部二级总包资质，\\承建多座大型FDI厂房。}
  };

  % 2026
  \fill[white] (134,82) circle (3.4);
  \draw[TTCRed, line width=1.5pt] (134,82) circle (3.4);
  \fill[TTCRed] (134,82) circle (1.35);
  \node[anchor=north west, align=left, text width=42mm, fill=TTCLightBlue!86!white,
        fill opacity=0.94, text opacity=1, rounded corners=1.5pt, inner sep=1mm] at (119,68) {
    {\fontsize{18}{20}\selectfont\bfseries\color{TTCRed} 2026}\\[-0.5mm]
    {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCBlue} 科技转型}\\[1mm]
    {\fontsize{7.2}{9}\selectfont\color{TTCTextDark}150+工业项目 \textbullet\ 20+省市\\PEB年产能达30,000吨。}
  };

  % 2030
  \fill[white] (176,105) circle (3.4);
  \draw[TTCRed, line width=1.5pt] (176,105) circle (3.4);
  \fill[TTCRed] (176,105) circle (1.35);
  \node[anchor=north east, align=right, text width=40mm, fill=TTCLightBlue!86!white,
        fill opacity=0.94, text opacity=1, rounded corners=1.5pt, inner sep=1mm] at (178,98) {
    {\fontsize{18}{20}\selectfont\bfseries\color{TTCRed} 2030}\\[-0.5mm]
    {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCBlue} 国际愿景}\\[1mm]
    {\fontsize{7.2}{9}\selectfont\color{TTCTextDark}ConTech建筑科技 \textbullet\ ESG\\进军东南亚国际市场。}
  };
\end{tikzpicture}

\vspace{4mm}

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
    {\fontsize{12}{14}\selectfont\bfseries\color{white}五大核心价值观 — 铸就每一项工程的基石}\\[1.5mm]
    {\fontsize{7.5}{9}\selectfont\color{white!82!gray}The core values that sustain every commitment and project.}
  };

  \fill[TTCDeepNavy!97!black, opacity=0.96] (0,0) rectangle (37.2,31);
  \fill[TTCDeepNavy!91!black, opacity=0.96] (37.2,0) rectangle (74.4,31);
  \fill[TTCDeepNavy!97!black, opacity=0.96] (74.4,0) rectangle (111.6,31);
  \fill[TTCDeepNavy!91!black, opacity=0.96] (111.6,0) rectangle (148.8,31);
  \fill[TTCDeepNavy!97!black, opacity=0.96] (148.8,0) rectangle (186,31);
  \fill[TTCRed] (0,31) rectangle (186,32.3);

  \node[align=center, text=white] at (18.6,15.5) {
    {\fontsize{14}{16}\selectfont\bfseries 信}\\[1mm]
    {\fontsize{6.8}{8}\selectfont\color{white!72!gray}TRUST \& INTEGRITY}
  };
  \node[align=center, text=white] at (55.8,15.5) {
    {\fontsize{14}{16}\selectfont\bfseries 心}\\[1mm]
    {\fontsize{6.8}{8}\selectfont\color{white!72!gray}DEDICATION}
  };
  \node[align=center, text=white] at (93,15.5) {
    {\fontsize{14}{16}\selectfont\bfseries 智}\\[1mm]
    {\fontsize{6.8}{8}\selectfont\color{white!72!gray}INNOVATION}
  };
  \node[align=center, text=white] at (130.2,15.5) {
    {\fontsize{14}{16}\selectfont\bfseries 速}\\[1mm]
    {\fontsize{6.8}{8}\selectfont\color{white!72!gray}FAST-TRACK}
  };
  \node[align=center, text=white] at (167.4,15.5) {
    {\fontsize{14}{16}\selectfont\bfseries 安}\\[1mm]
    {\fontsize{6.8}{8}\selectfont\color{white!72!gray}HSE \& SAFETY}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_05 = r"""% ============================================================
% TRANG 05: INTEGRATED FACTORY BLUEPRINT
% ============================================================
\pageheaderbar{EPC总承包生态系统与研发技术}{第05页}
\pagefooterbar{第05页}

\begin{tikzpicture}[remember picture, overlay]
  \draw[TTCBlue!6!white, line width=0.45pt]
    ([xshift=15mm,yshift=18mm]current page.south west)
    grid[step=8mm]
    ([xshift=195mm,yshift=42mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{EPC总承包生态系统}{Integrated Factory Blueprint \& AIDC ConTech Collaboration}

\vspace{1mm}
{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
一个生态系统 • 一份总包合同 • 一体化全责管控\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
One integrated ecosystem. One accountable EPC partner from concept to handover.\par}
\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,118);
  \clip[rounded corners=3pt] (0,0) rectangle (186,118);
  \node[anchor=center, inner sep=0pt] at (93,59)
    {\includegraphics[height=118mm]{../../public/factory-tech-3d.jpg}};
  \fill[white, opacity=0.10] (0,0) rectangle (186,118);

  % Connectors
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
    {\fontsize{10}{11.5}\selectfont\bfseries\color{TTCBlue} BIM 5D • AI • 价值工程}\\[1mm]
    {\fontsize{7}{8.6}\selectfont\color{TTCTextDark}优化设计与数据模型，节省 10--15\% 投资成本。}
  };

  % 02 — MEP & PCCC
  \node[
    anchor=south west, rounded corners=3pt,
    fill=white, fill opacity=0.94, text opacity=1,
    draw=TTCBlue!42!white, line width=0.65pt,
    minimum width=53mm, minimum height=29mm,
    text width=47mm, inner sep=3mm, align=left
  ] at (5,5) {
    {\fontsize{7.3}{8.5}\selectfont\bfseries\color{TTCBlue} 02 / MEP 机电与消防}\\[1mm]
    {\fontsize{10}{11.5}\selectfont\bfseries\color{TTCBlue} 基于BIM的全专业协同}\\[1mm]
    {\fontsize{7}{8.6}\selectfont\color{TTCTextDark}电气、暖通、给排水与自动消防系统统一模型无缝集成。}
  };

  % 03 — Infrastructure
  \node[
    anchor=north east, rounded corners=3pt,
    fill=white, fill opacity=0.94, text opacity=1,
    draw=TTCBlue!42!white, line width=0.65pt,
    minimum width=53mm, minimum height=29mm,
    text width=47mm, inner sep=3mm, align=left
  ] at (181,113) {
    {\fontsize{7.3}{8.5}\selectfont\bfseries\color{TTCBlue} 03 / 园区配套基建}\\[1mm]
    {\fontsize{10}{11.5}\selectfont\bfseries\color{TTCBlue} 重载地基 • 道路 • 排水}\\[1mm]
    {\fontsize{7}{8.6}\selectfont\color{TTCTextDark}高标准园区基础设施，与厂区总平面布置完美对接。}
  };

  % 04 — PEB
  \node[
    anchor=south east, rounded corners=3pt,
    fill=white, fill opacity=0.96, text opacity=1,
    draw=TTCRed!78!white, line width=0.8pt,
    minimum width=53mm, minimum height=29mm,
    text width=47mm, inner sep=3mm, align=left
  ] at (181,5) {
    {\fontsize{7.3}{8.5}\selectfont\bfseries\color{TTCRed} 04 / PEB 钢结构制造}\\[1mm]
    {\fontsize{10}{11.5}\selectfont\bfseries\color{TTCBlue} 精密智造与品控}\\[1mm]
    {\fontsize{7}{8.6}\selectfont\color{TTCTextDark}CNC • SAW • AWS D1.1 • NDT；年供货能力达 30,000 吨。}
  };

  % Central hub
  \node[
    rounded corners=3pt, fill=TTCDeepNavy!96!black,
    draw=TTCCyan!75!white, line width=0.9pt,
    minimum width=50mm, minimum height=28mm,
    text=white, align=center, inner sep=2.5mm
  ] at (93,64) {
    {\fontsize{11}{12.5}\selectfont\bfseries 新成功 TTC}\\[1mm]
    {\fontsize{7.5}{9}\selectfont\bfseries\color{TTCCyan} EPC SYSTEM INTEGRATOR}\\[1mm]
    {\fontsize{6.8}{8}\selectfont\color{white!78!gray}One contract • One accountability}
  };

  \draw[white, line width=1.2pt, rounded corners=3pt] (0.6,0.6) rectangle (185.4,117.4);
  \draw[TTCBorder, line width=0.65pt, rounded corners=3pt] (0,0) rectangle (186,118);
\end{tikzpicture}

\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,31);
  \fill[TTCLightBlue, rounded corners=4pt] (0,0) rectangle (186,31);
  \draw[TTCBorder, line width=0.65pt, rounded corners=4pt] (0,0) rectangle (186,31);

  \node[align=center] at (18,15.5) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCTextMuted} 01}\\[0.7mm]
    {\fontsize{9.2}{10.5}\selectfont\bfseries\color{TTCBlue} 现场勘察}\\[0.7mm]
    {\fontsize{6.6}{8}\selectfont 现状与需求分析}
  };
  \node[align=center] at (55.5,15.5) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCTextMuted} 02}\\[0.7mm]
    {\fontsize{9.2}{10.5}\selectfont\bfseries\color{TTCBlue} 方案设计}\\[0.7mm]
    {\fontsize{6.6}{8}\selectfont BIM • AI • VE}
  };
  \node[align=center] at (93,15.5) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCTextMuted} 03}\\[0.7mm]
    {\fontsize{9.2}{10.5}\selectfont\bfseries\color{TTCBlue} 基础工程}\\[0.7mm]
    {\fontsize{6.6}{8}\selectfont 地基与管网}
  };
  \node[align=center] at (130.5,15.5) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCTextMuted} 04}\\[0.7mm]
    {\fontsize{9.2}{10.5}\selectfont\bfseries\color{TTCBlue} 机电与消防}\\[0.7mm]
    {\fontsize{6.6}{8}\selectfont 系统集成安装}
  };
  \node[align=center] at (168,15.5) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCRed} 05}\\[0.7mm]
    {\fontsize{9.2}{10.5}\selectfont\bfseries\color{TTCRed} PEB制造}\\[0.7mm]
    {\fontsize{6.6}{8}\selectfont 构件加工与吊装}
  };

  \foreach \x in {36.75,74.25,111.75,149.25}{
    \node[text=TTCRed, font=\fontsize{8}{9}\selectfont] at (\x,15.5) {\faChevronRight};
  }
\end{tikzpicture}

\vspace{3mm}

\noindent
\begin{tabular}{@{}p{58mm}@{\hspace{6mm}}p{58mm}@{\hspace{6mm}}p{58mm}@{}}
  \begin{tikzpicture}
    \node[
      rounded corners=4pt, fill=white, draw=TTCBorder,
      line width=0.65pt, minimum width=58mm, minimum height=35mm,
      text width=50mm, inner sep=4mm, align=left
    ] {
      {\fontsize{7}{8}\selectfont\bfseries\color{TTCRed} 01 / ACCOUNTABILITY}\\[1mm]
      {\fontsize{14}{15.5}\selectfont\bfseries\color{TTCBlue} 01 责任总包}\\[1mm]
      {\fontsize{7}{8.5}\selectfont\color{TTCTextDark}单一总包主体对项目从设计到交付承担全过程责任。}
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
      {\fontsize{14}{15.5}\selectfont\bfseries\color{TTCBlue} 成本优化}\\[1mm]
      {\fontsize{7}{8.5}\selectfont\color{TTCTextDark}AI与价值工程优化技术方案，节省10--15\%投资成本。}
    };
  \end{tikzpicture}
  &
  \begin{tikzpicture}
    \node[
      rounded corners=4pt, fill=white, draw=TTCBorder,
      line width=0.65pt, minimum width=58mm, minimum height=35mm,
      text width=50mm, inner sep=4mm, align=left
    ] {
      {\fontsize{7}{8}\selectfont\bfseries\color{TTCGold} 03 / RELIABILITY}\\[1mm]
      {\fontsize{14}{15.5}\selectfont\bfseries\color{TTCBlue} 100\% 按期交付}\\[1mm]
      {\fontsize{7}{8.5}\selectfont\color{TTCTextDark}自控重机与制造产能，保障项目关键节点绝对准时。}
    };
  \end{tikzpicture}
\end{tabular}
\end{minipage}
\newpage
"""

PAGE_06 = r"""% ============================================================
% TRANG 06: GOVERNANCE & COMPLIANCE DASHBOARD
% ============================================================
\pageheaderbar{组织架构与建设部二级资质认证}{第06页}
\pagefooterbar{第06页}

\begin{tikzpicture}[remember picture, overlay]
  \draw[TTCBlue!6!white, line width=0.45pt]
    ([xshift=15mm,yshift=18mm]current page.south west)
    grid[step=8mm]
    ([xshift=195mm,yshift=42mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{精益治理与合规体系}{Governance Structure, Grade II Construction License \& International ISO Systems}

\vspace{1mm}
{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
权责分明 • 执行高效 • 全程闭环合规管理\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
An execution-led governance model connecting board oversight directly to every project site.\par}
\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,105);
  \fill[white, rounded corners=4pt] (0,0) rectangle (186,105);
  \draw[TTCBorder, line width=0.7pt, rounded corners=4pt] (0,0) rectangle (186,105);

  \node[anchor=west, align=left] at (6,99) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} DELIVERY GOVERNANCE}\\[-0.2mm]
    {\fontsize{9.5}{11}\selectfont\bfseries\color{TTCBlue} 矩阵式扁平化项目指挥与管理架构}
  };
  \draw[TTCBorder, line width=0.5pt] (6,91.5) -- (180,91.5);

  % Connectors
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

  % Board & executive
  \node[
    rounded corners=3pt, fill=TTCDeepNavy, text=white,
    minimum width=78mm, minimum height=10mm, align=center
  ] at (93,83) {
    {\fontsize{7.8}{9.2}\selectfont\bfseries
    \faUsers\quad 股东大会与董事会 (Board of Directors)}
  };
  \node[
    rounded corners=3pt, fill=TTCLightBlue, draw=TTCBorder,
    minimum width=42mm, minimum height=9mm, align=center
  ] at (25,70.5) {
    {\fontsize{7}{8.3}\selectfont\bfseries\color{TTCBlue} 国际工程专家顾问委员会}
  };
  \node[
    rounded corners=3pt, fill=TTCRed, text=white,
    minimum width=62mm, minimum height=11mm, align=center
  ] at (93,70.5) {
    {\fontsize{8.2}{9.5}\selectfont\bfseries
    \faUserTie\quad 总经理 (CEO)}\\[0.5mm]
    {\fontsize{6.7}{8}\selectfont 范辉新 (PHẠM HUY TÂN)}
  };
  \node[
    rounded corners=3pt, fill=TTCLightBlue, draw=TTCCyan,
    minimum width=42mm, minimum height=9mm, align=center
  ] at (161,70.5) {
    {\fontsize{7}{8.3}\selectfont\bfseries\color{TTCBlue}
    \faMicrochip\quad AIDC 建筑科技研发中心}
  };

  % Three executive streams
  \node[
    rounded corners=3pt, fill=TTCBlue, text=white,
    minimum width=54mm, minimum height=10mm, align=center
  ] at (32,52.5) {
    {\fontsize{7.4}{8.8}\selectfont\bfseries 项目工程副总经理 (COO)}
  };
  \node[
    rounded corners=3pt, fill=TTCBlue, text=white,
    minimum width=54mm, minimum height=10mm, align=center
  ] at (93,52.5) {
    {\fontsize{7.4}{8.8}\selectfont\bfseries 技术总工 \& BIM中心 (CTO)}
  };
  \node[
    rounded corners=3pt, fill=TTCBlue, text=white,
    minimum width=54mm, minimum height=10mm, align=center
  ] at (154,52.5) {
    {\fontsize{7.4}{8.8}\selectfont\bfseries 财务与商务合约副总 (CFO)}
  };

  % Functional teams
  \node[
    rounded corners=3pt, fill=white, draw=TTCBorder,
    minimum width=54mm, minimum height=22mm,
    text width=47mm, inner sep=3mm, align=left
  ] at (32,32) {
    {\fontsize{7.1}{8.4}\selectfont\bfseries\color{TTCBlue}\faHardHat\ PROJECT DELIVERY}\\[1mm]
    {\fontsize{6.7}{8.2}\selectfont\color{TTCTextDark}
    • FDI项目指挥部\\
    • 施工统筹与机械调度\\
    • 现场 HSE \& QA/QC 管控}
  };
  \node[
    rounded corners=3pt, fill=white, draw=TTCBorder,
    minimum width=54mm, minimum height=22mm,
    text width=47mm, inner sep=3mm, align=left
  ] at (93,32) {
    {\fontsize{7.1}{8.4}\selectfont\bfseries\color{TTCBlue}\faDraftingCompass\ ENGINEERING}\\[1mm]
    {\fontsize{6.7}{8.2}\selectfont\color{TTCTextDark}
    • 价值工程与结构优化\\
    • BIM 5D 与全生命周期数据\\
    • 规划、合规与消防审查}
  };
  \node[
    rounded corners=3pt, fill=white, draw=TTCBorder,
    minimum width=54mm, minimum height=22mm,
    text width=47mm, inner sep=3mm, align=left
  ] at (154,32) {
    {\fontsize{7.1}{8.4}\selectfont\bfseries\color{TTCBlue}\faFileInvoiceDollar\ COMMERCIAL}\\[1mm]
    {\fontsize{6.7}{8.2}\selectfont\color{TTCTextDark}
    • 招投标与FIDIC合同谈判\\
    • EPC现金流与资金风控\\
    • Tier-1 核心供应链采购}
  };

  % Site execution
  \node[
    rounded corners=3pt, fill=TTCDeepNavy, draw=TTCCyan,
    line width=0.75pt, text=white,
    minimum width=174mm, minimum height=12mm, align=center
  ] at (93,8) {
    {\fontsize{7.7}{9}\selectfont\bfseries\color{TTCCyan}
    \faHardHat\quad 现场项目指挥部 — 赋权一线，即时响应}\\[0.6mm]
    {\fontsize{6.5}{7.8}\selectfont\color{white!82!gray}
    项目经理 (PM) • 结构工程师 • MEP机电 • 常驻 HSE 与 QA/QC 工程师}
  };
\end{tikzpicture}

\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,72);
  \fill[TTCLightBlue, rounded corners=4pt] (0,0) rectangle (186,72);
  \draw[TTCBorder, line width=0.7pt, rounded corners=4pt] (0,0) rectangle (186,72);

  \node[anchor=west, align=left] at (6,66) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} COMPLIANCE PASSPORT}\\[-0.2mm]
    {\fontsize{9.5}{11}\selectfont\bfseries\color{TTCBlue}
    法定资质与国际化质量认证体系}
  };

  % Grade II card
  \fill[white, rounded corners=3pt] (5,7) rectangle (58,57);
  \draw[TTCRed, line width=0.9pt, rounded corners=3pt] (5,7) rectangle (58,57);
  \node[align=center] at (31.5,45) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCRed} CONSTRUCTION LICENSE}\\[1mm]
    {\fontsize{20}{22}\selectfont\bfseries\color{TTCRed} 二级资质}\\[-0.2mm]
    {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCBlue} 越南建设部颁发}
  };
  \draw[TTCBorder, line width=0.5pt] (11,29) -- (52,29);
  \node[text width=42mm, align=left] at (31.5,18) {
    {\fontsize{6.6}{8.2}\selectfont\color{TTCTextDark}
    \textcolor{TTCRed}{\faCheckCircle}\ 工业建筑设计与施工总承包\\
    \textcolor{TTCRed}{\faCheckCircle}\ 无建筑面积与楼层上限限制\\
    \textcolor{TTCRed}{\faCheckCircle}\ 超大跨度重型工业厂房资质}
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
    全流程质量管理，材料、施工及验收执行4层ITP标准。}
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
    环境管理体系，严控废弃物与噪音，优先低碳建造方案。}
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
    职业健康安全体系，坚持零事故政策与全员安全培训。}
  };
\end{tikzpicture}

\vspace{3mm}

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
    {\fontsize{7}{8.3}\selectfont\bfseries\color{TTCTextDark} 一站式法人责任}
  };
  \node[align=center] at (113,12) {
    {\fontsize{11}{12.5}\selectfont\bfseries\color{TTCBlue} 04}\\[0.6mm]
    {\fontsize{7}{8.3}\selectfont\bfseries\color{TTCTextDark} 4级 ITP 品控体系}
  };
  \node[align=center] at (160,12) {
    {\fontsize{11}{12.5}\selectfont\bfseries\color{TTCRed} 100\%}\\[0.6mm]
    {\fontsize{7}{8.3}\selectfont\bfseries\color{TTCTextDark} CO/CQ 材料溯源}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_07 = r"""% ============================================================
% TRANG 07: NĂNG LỰC NHÂN SỰ TRIỂN KHAI EPC
% ============================================================
\pageheaderbar{EPC项目实施人力资源能力}{第07页}
\pagefooterbar{第07页}

\begin{tikzpicture}[remember picture, overlay]
  \draw[TTCBlue!6!white, line width=0.45pt]
    ([xshift=15mm,yshift=18mm]current page.south west)
    grid[step=8mm]
    ([xshift=195mm,yshift=42mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{全生命周期集成化项目团队}{Integrated Project Team, Clear Accountability \& Site-Ready Mobilization}

\vspace{1mm}
{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
合适的人选 • 明确的角色 • 精准的时机\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
One accountable team mobilized from pre-construction through commissioning and warranty.\par}
\vspace{3mm}

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
    {\fontsize{15}{17}\selectfont\bfseries 现场执行一线的\\专业力量}\\[2mm]
    {\fontsize{7.2}{9}\selectfont\color{white!84!gray}
    项目团队按任务单元编制，职权清晰明确，执行单一指挥线的高效汇报机制。}
  };

  \node[
    anchor=south east, rounded corners=3pt,
    fill=white, fill opacity=0.93, text opacity=1,
    draw=TTCCyan, line width=0.7pt,
    minimum width=52mm, minimum height=14mm, align=center
  ] at (179,7) {
    {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCBlue} FIELD-LED DECISION MAKING}\\[0.7mm]
    {\fontsize{6.5}{8}\selectfont\color{TTCTextDark}技术与管理决策直接贴近施工现场一线}
  };
  \draw[white, line width=1pt, rounded corners=3pt] (0.6,0.6) rectangle (185.4,71.4);
  \draw[TTCBorder, line width=0.65pt, rounded corners=3pt] (0,0) rectangle (186,72);
\end{tikzpicture}

\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,67);
  \node[anchor=west, align=left] at (0,62) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} PROJECT TEAM BY PHASE}\quad
    {\fontsize{9.5}{11}\selectfont\bfseries\color{TTCBlue} 项目各阶段核心责任角色分工}
  };

  % Phase 01
  \fill[white, rounded corners=3pt] (0,0) rectangle (58,55);
  \draw[TTCBorder, line width=0.65pt, rounded corners=3pt] (0,0) rectangle (58,55);
  \fill[TTCLightBlue, rounded corners=3pt] (0,43) rectangle (58,55);
  \node[anchor=west] at (5,49) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} 01 / PRE-CONSTRUCTION}
  };
  \node[anchor=north west, text width=48mm, align=left] at (5,39) {
    {\fontsize{9.5}{11}\selectfont\bfseries\color{TTCBlue} 前期准备与设计}\\[1.2mm]
    {\fontsize{7}{8.6}\selectfont\color{TTCTextDark}
    \textbf{Project Director}\\
    与业主对接的单一总责任人。\\[0.8mm]
    \textbf{Design \& BIM Lead}\\
    设计统筹、价值工程与模型深化。\\[0.8mm]
    \textbf{Planning / QS / FIDIC}\\
    锁定工程范围、进度总计划与预算。}
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
    {\fontsize{9.5}{11}\selectfont\bfseries\color{TTCBlue} 现场施工装配}\\[1.2mm]
    {\fontsize{7}{8.6}\selectfont\color{TTCTextDark}
    \textbf{Construction / Site Manager}\\
    资源调配 • 作业面统筹 • 施工班组。\\[0.5mm]
    \textbf{Discipline Engineers}\\
    结构 • 园区基建 • MEP • 消防。\\[0.5mm]
    \textbf{HSE \& QA/QC Managers}\\
    独立行使安全与质量一票否决权。}
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
    {\fontsize{9.5}{11}\selectfont\bfseries\color{TTCBlue} 竣工交付与运维}\\[1.2mm]
    {\fontsize{7}{8.6}\selectfont\color{TTCTextDark}
    \textbf{Commissioning Manager}\\
    统筹系统联合调试与试运行。\\[0.8mm]
    \textbf{As-built \& Digital Twin Team}\\
    标准化竣工图纸与数字资产交付。\\[0.8mm]
    \textbf{Warranty Response Team}\\
    24/7 快速技术支持与质保服务。}
  };
  \node[anchor=south, align=center] at (157,3.5) {
    {\fontsize{6.5}{7.8}\selectfont\bfseries\color{TTCRed} OUTPUT: READY FOR OPERATION}
  };
\end{tikzpicture}

\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,29);
  \fill[TTCLightBlue, rounded corners=4pt] (0,0) rectangle (186,29);
  \draw[TTCBorder, line width=0.65pt, rounded corners=4pt] (0,0) rectangle (186,29);

  \node[align=center] at (22,14.5) {
    {\fontsize{6.5}{7.8}\selectfont\bfseries\color{TTCTextMuted} GOVERNANCE}\\[0.7mm]
    {\fontsize{9.2}{10.5}\selectfont\bfseries\color{TTCBlue} 总部 PMO}\\[0.5mm]
    {\fontsize{6.4}{7.6}\selectfont 项目组合管控}
  };
  \node[text=TTCRed] at (45,14.5) {\faChevronRight};
  \node[align=center] at (68,14.5) {
    {\fontsize{6.5}{7.8}\selectfont\bfseries\color{TTCTextMuted} ACCOUNTABILITY}\\[0.7mm]
    {\fontsize{9.2}{10.5}\selectfont\bfseries\color{TTCBlue} 项目总监}\\[0.5mm]
    {\fontsize{6.4}{7.6}\selectfont 单一责任主体}
  };
  \node[text=TTCRed] at (93,14.5) {\faChevronRight};
  \node[align=center] at (118,14.5) {
    {\fontsize{6.5}{7.8}\selectfont\bfseries\color{TTCTextMuted} SITE AUTHORITY}\\[0.7mm]
    {\fontsize{9.2}{10.5}\selectfont\bfseries\color{TTCBlue} 现场指挥部}\\[0.5mm]
    {\fontsize{6.4}{7.6}\selectfont 一线执行决策}
  };
  \node[text=TTCRed] at (141,14.5) {\faChevronRight};
  \node[align=center] at (164,14.5) {
    {\fontsize{6.5}{7.8}\selectfont\bfseries\color{TTCTextMuted} DELIVERY}\\[0.7mm]
    {\fontsize{9.2}{10.5}\selectfont\bfseries\color{TTCRed} 专业施工班组}\\[0.5mm]
    {\fontsize{6.4}{7.6}\selectfont 专业任务交付}
  };
\end{tikzpicture}

\vspace{3mm}

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
    {\fontsize{6.8}{8}\selectfont\bfseries\color{TTCTextDark} 管理人员与工程师}
  };
  \node[align=center] at (69.75,13.5) {
    {\fontsize{14}{15.5}\selectfont\bfseries\color{TTCBlue} 2,500+}\\[0.8mm]
    {\fontsize{6.8}{8}\selectfont\bfseries\color{TTCTextDark} 专业技术工人}
  };
  \node[align=center] at (116.25,13.5) {
    {\fontsize{14}{15.5}\selectfont\bfseries\color{TTCCyan} 85+}\\[0.8mm]
    {\fontsize{6.8}{8}\selectfont\bfseries\color{TTCTextDark} 注册监理与施工队长}
  };
  \node[align=center] at (162.75,13.5) {
    {\fontsize{14}{15.5}\selectfont\bfseries\color{TTCBlue} 60+}\\[0.8mm]
    {\fontsize{6.8}{8}\selectfont\bfseries\color{TTCTextDark} BIM与数字化专家}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

print("Section 1 (Pages 01-07) Chinese version loaded successfully.")
