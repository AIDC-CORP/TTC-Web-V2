# -*- coding: utf-8 -*-
"""
Section 3: PEB Strategic Network, Equipment Fleet & FIDIC Project Governance (Pages 11 - 13) — 简体中文版
"""

PAGE_11 = r"""% ============================================================
% TRANG 11: PEB SUPPLY & QUALITY GATES
% ============================================================
\pageheaderbar{PEB战略制造网络与品控体系}{第11页}
\pagefooterbar{第11页}

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
\secbrand{TTC 受控 PEB 钢结构制造网络}{Strategic Fabrication Network, Resident QA/QC \& Traceable Quality Gates}

\vspace{1mm}
{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
TTC深化设计 • 战略基地制造 • 常驻QC全过程品控\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
Flexible fabrication capacity with TTC-controlled engineering, inspection and release authority.\par}
\vspace{3mm}

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
    {\fontsize{19}{21}\selectfont\bfseries 30,000 吨}\\[-0.4mm]
    {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCCyan} 年钢结构供应产能}\\[1.8mm]
    {\fontsize{7}{8.6}\selectfont\color{white!82!gray}
    TTC 全程主导方案设计、加工详图 (Shop Drawing) 及出厂审批。}
  };
  \node[
    anchor=south east, rounded corners=3pt,
    fill=white, fill opacity=0.94, text opacity=1,
    draw=TTCCyan, line width=0.65pt,
    minimum width=55mm, minimum height=14mm, align=center
  ] at (179,7) {
    {\fontsize{9.5}{11}\selectfont\bfseries\color{TTCBlue} >20,000 m\textsuperscript{2} • 常驻 QC 监理}\\[0.6mm]
    {\fontsize{6.5}{7.8}\selectfont\color{TTCTextDark}Partner factory footprint • TTC supervision}
  };
  \draw[white, line width=1pt, rounded corners=3pt] (0.6,0.6) rectangle (185.4,63.4);
  \draw[TTCBorder, line width=0.65pt, rounded corners=3pt] (0,0) rectangle (186,64);
\end{tikzpicture}

\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,53);
  \node[anchor=west] at (0,48) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} FABRICATION FLOW}\quad
    {\fontsize{9.5}{11}\selectfont\bfseries\color{TTCBlue} 六道全闭环精密加工工序}
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
    {\fontsize{8}{9.2}\selectfont\bfseries\color{TTCBlue} CNC 下料}\\[0.6mm]
    {\fontsize{6.3}{7.5}\selectfont 等离子坡口切割}
  };
  \node[align=center, text width=25mm] at (46,13) {
    {\fontsize{8}{9.2}\selectfont\bfseries\color{TTCBlue} 液压组立}\\[0.6mm]
    {\fontsize{6.3}{7.5}\selectfont 自动定位对中}
  };
  \node[align=center, text width=25mm] at (77,13) {
    {\fontsize{8}{9.2}\selectfont\bfseries\color{TTCBlue} 埋弧焊(SAW)}\\[0.6mm]
    {\fontsize{6.3}{7.5}\selectfont AWS D1.1标准}
  };
  \node[align=center, text width=25mm] at (108,13) {
    {\fontsize{8}{9.2}\selectfont\bfseries\color{TTCBlue} 液压矫正}\\[0.6mm]
    {\fontsize{6.3}{7.5}\selectfont 消除焊接热变形}
  };
  \node[align=center, text width=25mm] at (139,13) {
    {\fontsize{8}{9.2}\selectfont\bfseries\color{TTCBlue} 抛丸除锈}\\[0.6mm]
    {\fontsize{6.3}{7.5}\selectfont 达到 Sa 2.5 级}
  };
  \node[align=center, text width=25mm] at (171,13) {
    {\fontsize{8}{9.2}\selectfont\bfseries\color{TTCRed} 涂装防护}\\[0.6mm]
    {\fontsize{6.3}{7.5}\selectfont 环氧与防火涂料}
  };
\end{tikzpicture}

\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,53);

  \fill[white, rounded corners=4pt] (0,0) rectangle (58,53);
  \draw[TTCBorder, line width=0.65pt, rounded corners=4pt] (0,0) rectangle (58,53);
  \node[anchor=north west, text width=48mm, align=left] at (5,47) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} QUALITY GATE 01}\\[0.8mm]
    {\fontsize{10}{11.5}\selectfont\bfseries\color{TTCBlue} 原材料放行关}\\[1.3mm]
    {\fontsize{7}{8.5}\selectfont\color{TTCTextDark}
    \textcolor{TTCCyan}{\faCheckCircle}\ 100\% 钢板 MTC 与质保书追溯。\\[0.7mm]
    \textcolor{TTCCyan}{\faCheckCircle}\ Q345B • SS400 • ASTM A572。\\[0.7mm]
    \textcolor{TTCCyan}{\faCheckCircle}\ 独立第三方力学拉伸与冲击试验。}
  };

  \fill[TTCLightBlue, rounded corners=4pt] (64,0) rectangle (122,53);
  \draw[TTCBlue!50!white, line width=0.7pt, rounded corners=4pt] (64,0) rectangle (122,53);
  \node[anchor=north west, text width=48mm, align=left] at (69,47) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} QUALITY GATE 02}\\[0.8mm]
    {\fontsize{10}{11.5}\selectfont\bfseries\color{TTCBlue} 焊接质量检验关}\\[1.3mm]
    {\fontsize{7}{8.5}\selectfont\color{TTCTextDark}
    \textcolor{TTCBlue}{\faCheckCircle}\ 严格执行核准的 WPS/PQR 规程。\\[0.7mm]
    \textcolor{TTCBlue}{\faCheckCircle}\ 焊工全员持 3G/4G/6G 专业资格证。\\[0.7mm]
    \textcolor{TTCBlue}{\faCheckCircle}\ 关键受力焊缝 100\% UT/MT 超声探伤。}
  };

  \fill[white, rounded corners=4pt] (128,0) rectangle (186,53);
  \draw[TTCRed!65!white, line width=0.75pt, rounded corners=4pt] (128,0) rectangle (186,53);
  \node[anchor=north west, text width=48mm, align=left] at (133,47) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCRed} QUALITY GATE 03}\\[0.8mm]
    {\fontsize{10}{11.5}\selectfont\bfseries\color{TTCBlue} 表面涂装与出厂关}\\[1.3mm]
    {\fontsize{7}{8.5}\selectfont\color{TTCTextDark}
    \textcolor{TTCRed}{\faCheckCircle}\ ISO 8501-1 抛丸除锈 Sa 2.5 级。\\[0.7mm]
    \textcolor{TTCRed}{\faCheckCircle}\ Elcometer 数字仪器检测干膜厚度 (DFT)。\\[0.7mm]
    \textcolor{TTCRed}{\faCheckCircle}\ 环氧重防腐与公安消防认证防火涂层。}
  };
\end{tikzpicture}

\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,30);
  \fill[TTCLightBlue, rounded corners=4pt] (0,0) rectangle (186,30);
  \draw[TTCBorder, line width=0.65pt, rounded corners=4pt] (0,0) rectangle (186,30);
  \node[anchor=west, align=left] at (6,15) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} TTC CONTROL MODEL}\\[0.7mm]
    {\fontsize{9.3}{10.8}\selectfont\bfseries\color{TTCBlue} TTC 独家出厂放行权}
  };
  \node[text=TTCRed] at (55,15) {\faChevronRight};
  \node[align=center] at (76,15) {
    {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCBlue} 设计与详图}\\[0.5mm]
    {\fontsize{6.3}{7.5}\selectfont TTC 统一出图}
  };
  \node[text=TTCRed] at (97,15) {\faChevronRight};
  \node[align=center] at (117,15) {
    {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCBlue} 驻厂 QA/QC}\\[0.5mm]
    {\fontsize{6.3}{7.5}\selectfont 全工序旁站监督}
  };
  \node[text=TTCRed] at (138,15) {\faChevronRight};
  \node[align=center] at (162,15) {
    {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCRed} 签发质保放行}\\[0.5mm]
    {\fontsize{6.3}{7.5}\selectfont 无签字严禁发货}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_12 = r"""% ============================================================
% TRANG 12: THIẾT BỊ THEO GÓI HUY ĐỘNG
% ============================================================
\pageheaderbar{现场重型机械设备与调度能力}{第12页}
\pagefooterbar{第12页}

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
    \draw[TTCBlue!20!white, line width=.85pt] (151,13) -- (151,51);
    \draw[TTCBlue!18!white] (146,13) -- (151,51) -- (156,13);
    \draw[TTCBlue!20!white, line width=.85pt] (151,48) -- (198,48);
    \draw[TTCBlue!17!white] (151,48) -- (177,39) -- (198,48);
    \draw[TTCRed!22!white, line width=.7pt] (184,48) -- (184,25);
    \draw[TTCRed!22!white] (181,25) -- (187,25);
  \end{scope}
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{施工机械配置与现场调度保障}{Right Equipment, Right Workfront, Right Time}

{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
43+ 重型机械 • 4 大作业包 • 统筹高效调度\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
设备按施工关键线路与实战工况精准匹配，全部经法定检测合格，杜绝现场窝工与等待。\par}
\vspace{3mm}

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
    {\fontsize{9}{10.5}\selectfont\bfseries 重型施工机械就绪}\\[1.7mm]
    {\fontsize{7}{8.5}\selectfont\color{white!82!gray}
    按项目进度关键线路科学调配，保障施工作业面高效运转。}
  };
  \node[rounded corners=2pt, fill=white, text=TTCBlue, align=center,
        minimum width=31mm, minimum height=16mm] at (129,17) {
    {\fontsize{13}{14}\selectfont\bfseries 100T}\\[-0.4mm]
    {\fontsize{6.2}{7.4}\selectfont 最大汽车吊起重量}
  };
  \node[rounded corners=2pt, fill=TTCRed, text=white, align=center,
        minimum width=35mm, minimum height=16mm] at (167,17) {
    {\fontsize{11}{12}\selectfont\bfseries 100\%}\\[-0.4mm]
    {\fontsize{6.2}{7.4}\selectfont 特种设备年检合格}
  };
\end{tikzpicture}

\vspace{3mm}

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
    {\fontsize{7.4}{8.5}\selectfont\bfseries\color{TTCBlue} 起重吊装与高空作业}\\[1mm]
    {\fontsize{6.6}{8}\selectfont\color{TTCTextDark}
    06台 25--100T 汽车吊\newline
    14台 18--28m 高空作业车\newline
    用于钢结构、屋面及机电安装。}
  };
  \node[anchor=north west, text width=35mm, align=left] at (51.5,43) {
    {\fontsize{15}{16}\selectfont\bfseries\color{TTCCyan} 12}\\[-.5mm]
    {\fontsize{7.4}{8.5}\selectfont\bfseries\color{TTCBlue} 地基开挖与混凝土}\\[1mm]
    {\fontsize{6.6}{8}\selectfont\color{TTCTextDark}
    08台 挖掘机与压路机\newline
    04台 泵车与搅拌运输车\newline
    用于基础管网与工业地坪施工。}
  };
  \node[anchor=north west, text width=35mm, align=left] at (99,43) {
    {\fontsize{15}{16}\selectfont\bfseries\color{TTCBlue} 02}\\[-.5mm]
    {\fontsize{7.4}{8.5}\selectfont\bfseries\color{TTCBlue} 现场移动压瓦机组}\\[1mm]
    {\fontsize{6.6}{8}\selectfont\color{TTCTextDark}
    02套 移动式压型成型机\newline
    现场直压 Cliplock/Seamlock\newline
    超长板通长无搭接，杜绝渗水。}
  };
  \node[anchor=north west, text width=35mm, align=left] at (146.5,43) {
    {\fontsize{15}{16}\selectfont\bfseries\color{TTCGold} 09}\\[-.5mm]
    {\fontsize{7.4}{8.5}\selectfont\bfseries\color{TTCBlue} 精密测量与检测仪器}\\[1mm]
    {\fontsize{6.6}{8}\selectfont\color{TTCTextDark}
    09套 徕卡全站仪/3D激光仪\newline
    控制轴线、标高与垂直度\newline
    测量误差目标控制在 2mm 内。}
  };
\end{tikzpicture}

\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,42);
  \fill[TTCLightBlue, rounded corners=3pt] (0,0) rectangle (186,42);
  \draw[TTCBorder, rounded corners=3pt, line width=.6pt] (0,0) rectangle (186,42);
  \node[anchor=west, font=\fontsize{8}{9.5}\selectfont\bfseries, text=TTCBlue] at (7,35)
    {\faClock\quad 紧扣关键线路的设备分步进场节拍};
  \draw[TTCBlue!35!white, line width=1pt] (19,19) -- (167,19);
  \foreach \x/\n/\t/\s in {
    21/01/基础工程/勘察 • 土方开挖 • 混凝土,
    69/02/主体结构/钢柱梁吊装 • 高空拼接,
    117/03/屋面围护/现场压型 • 屋面板 • 装修,
    165/04/调试验收/系统检测 • 试运转 • 交付}{
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

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,29);
  \fill[TTCDeepNavy, rounded corners=3pt] (0,0) rectangle (186,29);
  \foreach \x in {46.5,93,139.5}{\draw[white!35!gray] (\x,6) -- (\x,23);}
  \node[align=center, text=white] at (23.25,15) {{\fontsize{9}{10}\selectfont\bfseries\color{TTCRed} 12 小时}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont 紧急调配响应}};
  \node[align=center, text=white] at (69.75,15) {{\fontsize{9}{10}\selectfont\bfseries\color{TTCCyan} 100\% 持证}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont 特种作业持证上岗}};
  \node[align=center, text=white] at (116.25,15) {{\fontsize{9}{10}\selectfont\bfseries 原厂维保}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont 定期检修保养}};
  \node[align=center, text=white] at (162.75,15) {{\fontsize{9}{10}\selectfont\bfseries\color{TTCGold} 电子台账}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont 动态运行监测}};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_13 = r"""% ============================================================
% TRANG 13: QUẢN TRỊ DỰ ÁN STAGE-GATE
% ============================================================
\pageheaderbar{FIDIC标准八阶段项目管理流程}{第13页}
\pagefooterbar{第13页}

\begin{tikzpicture}[remember picture, overlay]
  \fill[TTCLightBlue]
    ([xshift=118mm,yshift=-32mm]current page.north west) --
    ([xshift=210mm,yshift=-32mm]current page.north west) --
    ([xshift=210mm,yshift=-118mm]current page.north west) -- cycle;
  \node[opacity=.035, font=\fontsize{62}{64}\selectfont\bfseries, text=TTCBlue,
        rotate=90] at ([xshift=-10mm,yshift=18mm]current page.east) {GATE};
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
\secbrand{EPC项目 Stage-Gate 四阶段管控体系}{FIDIC Turnkey Governance, Decision Gates \& Single-Point Accountability}

{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
各阶段必有交付成果 • 阶段转换必经核准放行\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
将八项核心工作整合为四大管控阶段，使业主对决策节点、责任分工及工程状态一目了然。\par}
\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,103);

  % PHASE 01
  \fill[white, rounded corners=2pt] (0,0) rectangle (43.5,103);
  \draw[TTCBorder, rounded corners=2pt, line width=.65pt] (0,0) rectangle (43.5,103);
  \fill[TTCDeepNavy, rounded corners=2pt] (0,84) rectangle (43.5,103);
  \node[anchor=west, text=white] at (4,94) {{\fontsize{7}{8}\selectfont 01}\quad{\fontsize{10}{11}\selectfont\bfseries DEFINE 定义}};
  \node[anchor=north west, text width=35.5mm, align=left] at (4,79) {
    {\fontsize{7}{8.5}\selectfont\bfseries\color{TTCRed} 01 • 勘察与需求确认}\\[.7mm]
    {\fontsize{6.2}{7.5}\selectfont\color{TTCTextDark}地质勘探、3D地形测绘、业主功能需求分析与可行性研究报告。\\[3mm]}
    {\fontsize{7}{8.5}\selectfont\bfseries\color{TTCBlue} 02 • 合规与规划报批}\\[.7mm]
    {\fontsize{6.2}{7.5}\selectfont\color{TTCTextDark}1/500 总平规划、环评(ĐTM)、消防审批、施工许可及设计基准。}
  };
  \fill[TTCRed!8!white] (3.5,5) rectangle (40,17);
  \node[align=center, text=TTCRed] at (21.75,11) {{\fontsize{6}{7}\selectfont\bfseries 关口 A (GATE A)}\\[-.2mm]{\fontsize{5.7}{6.7}\selectfont 基准核准放行}};

  % PHASE 02
  \fill[white, rounded corners=2pt] (47.5,0) rectangle (91,103);
  \draw[TTCBorder, rounded corners=2pt, line width=.65pt] (47.5,0) rectangle (91,103);
  \fill[TTCBlue, rounded corners=2pt] (47.5,84) rectangle (91,103);
  \node[anchor=west, text=white] at (51.5,94) {{\fontsize{7}{8}\selectfont 02}\quad{\fontsize{10}{11}\selectfont\bfseries ENGINEER 深化}};
  \node[anchor=north west, text width=35.5mm, align=left] at (51.5,79) {
    {\fontsize{7}{8.5}\selectfont\bfseries\color{TTCCyan} 03 • 价值工程与BIM}\\[.7mm]
    {\fontsize{6.2}{7.5}\selectfont\color{TTCTextDark}BIM LOD 400 建模、结构截面优化、全专业协同与碰撞检测。\\[3mm]}
    {\fontsize{7}{8.5}\selectfont\bfseries\color{TTCBlue} 04 • 采购与PEB制造}\\[.7mm]
    {\fontsize{6.2}{7.5}\selectfont\color{TTCTextDark}Tier-1材料锁定、加工详图(Shop Drawing)、排产与驻厂QC监督。}
  };
  \fill[TTCCyan!10!white] (51,5) rectangle (87.5,17);
  \node[align=center, text=TTCBlue] at (69.25,11) {{\fontsize{6}{7}\selectfont\bfseries 关口 B (GATE B)}\\[-.2mm]{\fontsize{5.7}{6.7}\selectfont 设计冻结确认}};

  % PHASE 03
  \fill[white, rounded corners=2pt] (95,0) rectangle (138.5,103);
  \draw[TTCBorder, rounded corners=2pt, line width=.65pt] (95,0) rectangle (138.5,103);
  \fill[TTCCyan!85!TTCBlue, rounded corners=2pt] (95,84) rectangle (138.5,103);
  \node[anchor=west, text=white] at (99,94) {{\fontsize{7}{8}\selectfont 03}\quad{\fontsize{10}{11}\selectfont\bfseries BUILD 施工}};
  \node[anchor=north west, text width=35.5mm, align=left] at (99,79) {
    {\fontsize{7}{8.5}\selectfont\bfseries\color{TTCRed} 05 • 地基与园区基建}\\[.7mm]
    {\fontsize{6.2}{7.5}\selectfont\color{TTCTextDark}桩基、承台地梁、工业地坪及室外管网按ITP标准移交作业面。\\[3mm]}
    {\fontsize{7}{8.5}\selectfont\bfseries\color{TTCBlue} 06 • 钢结构与MEP安装}\\[.7mm]
    {\fontsize{6.2}{7.5}\selectfont\color{TTCTextDark}主体钢构吊装、屋面围护、暖通机电、消防及关键线路管控。}
  };
  \fill[TTCBlue!8!white] (98.5,5) rectangle (135,17);
  \node[align=center, text=TTCBlue] at (116.75,11) {{\fontsize{6}{7}\selectfont\bfseries 关口 C (GATE C)}\\[-.2mm]{\fontsize{5.7}{6.7}\selectfont 调试就绪确认}};

  % PHASE 04
  \fill[white, rounded corners=2pt] (142.5,0) rectangle (186,103);
  \draw[TTCBorder, rounded corners=2pt, line width=.65pt] (142.5,0) rectangle (186,103);
  \fill[TTCGold, rounded corners=2pt] (142.5,84) rectangle (186,103);
  \node[anchor=west, text=white] at (146.5,94) {{\fontsize{7}{8}\selectfont 04}\quad{\fontsize{10}{11}\selectfont\bfseries HANDOVER 交付}};
  \node[anchor=north west, text width=35.5mm, align=left] at (146.5,79) {
    {\fontsize{7}{8.5}\selectfont\bfseries\color{TTCRed} 07 • 调试与官方验收}\\[.7mm]
    {\fontsize{6.2}{7.5}\selectfont\color{TTCTextDark}ITP四层验收、消防验收、单机试车及系统联动试运转。\\[3mm]}
    {\fontsize{7}{8.5}\selectfont\bfseries\color{TTCBlue} 08 • 移交与全寿命运维}\\[.7mm]
    {\fontsize{6.2}{7.5}\selectfont\color{TTCTextDark}竣工档案、数字孪生交付、操作人员培训、24个月保修与运维。}
  };
  \fill[TTCGold!12!white] (146,5) rectangle (182.5,17);
  \node[align=center, text=TTCGold!80!black] at (164.25,11) {{\fontsize{6}{7}\selectfont\bfseries 关口 D (GATE D)}\\[-.2mm]{\fontsize{5.7}{6.7}\selectfont 投产运营确认}};

  % Markers
  \foreach \x/\l in {45.5/A,93/B,140.5/C}{
    \fill[white] (\x,51) circle (3.8);
    \draw[TTCRed, line width=.8pt] (\x,51) circle (3.8);
    \node[text=TTCRed, font=\fontsize{5.5}{6}\selectfont\bfseries] at (\x,51) {\l};
  }
\end{tikzpicture}

\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,43);
  \fill[TTCLightBlue, rounded corners=3pt] (0,0) rectangle (186,43);
  \draw[TTCBorder, rounded corners=3pt, line width=.6pt] (0,0) rectangle (186,43);
  \node[anchor=west, text=TTCBlue, font=\fontsize{8}{9.5}\selectfont\bfseries] at (7,35)
    {\faProjectDiagram\quad GOVERNANCE SPINE — 一体化全贯穿管理主线};
  \foreach \x in {46.5,93,139.5}{\draw[TTCBorder] (\x,6) -- (\x,28);}
  \node[align=center, text width=39mm] at (23.25,17) {{\fontsize{7}{8}\selectfont\bfseries\color{TTCRed} 项目总监负责制}\\[-.2mm]{\fontsize{5.8}{7}\selectfont\color{TTCTextMuted}单一接口对最终结果负责}};
  \node[align=center, text width=39mm] at (69.75,17) {{\fontsize{7}{8}\selectfont\bfseries\color{TTCBlue} CPM 关键线路}\\[-.2mm]{\fontsize{5.8}{7}\selectfont\color{TTCTextMuted}周滚动前瞻排程控制}};
  \node[align=center, text width=39mm] at (116.25,17) {{\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} CDE 协同平台}\\[-.2mm]{\fontsize{5.8}{7}\selectfont\color{TTCTextMuted}图纸、RFI与ITP全程可溯}};
  \node[align=center, text width=39mm] at (162.75,17) {{\fontsize{7}{8}\selectfont\bfseries\color{TTCGold} FIDIC 履约风控}\\[-.2mm]{\fontsize{5.8}{7}\selectfont\color{TTCTextMuted}严控范围、变更与法律风险}};
\end{tikzpicture}

\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,29);
  \fill[TTCDeepNavy, rounded corners=3pt] (0,0) rectangle (186,29);
  \foreach \x in {46.5,93,139.5}{\draw[white!35!gray] (\x,6) -- (\x,23);}
  \node[align=center, text=white] at (23.25,15) {{\fontsize{9}{10}\selectfont\bfseries\color{TTCRed} 8 个步骤}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont 整合为4大管控阶段}};
  \node[align=center, text=white] at (69.75,15) {{\fontsize{9}{10}\selectfont\bfseries\color{TTCCyan} 4 个关口}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont 严苛条件放行}};
  \node[align=center, text=white] at (116.25,15) {{\fontsize{9}{10}\selectfont\bfseries FIDIC EPC}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont 国际通用合同标准}};
  \node[align=center, text=white] at (162.75,15) {{\fontsize{9}{10}\selectfont\bfseries\color{TTCGold} 24 个月}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont 结构全面品质保修}};
\end{tikzpicture}
\end{minipage}
\newpage
"""

print("Section 3 (Pages 11-13) Chinese version loaded successfully.")
