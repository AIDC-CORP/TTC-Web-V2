# -*- coding: utf-8 -*-
"""
Section 4: EPC Solutions, ConTech, ESG & QA/QC/HSE (Pages 14 - 19) — 简体中文版
"""

PAGE_14 = r"""% ============================================================
% TRANG 14: EPC VALUE MODEL — ONE CONTRACT, ONE ACCOUNTABILITY
% ============================================================
\pageheaderbar{EPC总承包模式与价值工程}{第14页}
\pagefooterbar{第14页}

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
  \begin{scope}[shift={(current page.south west)},x=1mm,y=1mm,opacity=.42]
    \draw[TTCBlue!17!white, line width=.7pt] (12,13) -- (198,13);
    \draw[TTCBlue!16!white] (17,13) -- (17,37) -- (47,50) -- (77,37) --
      (107,50) -- (137,37) -- (167,50) -- (197,37) -- (197,13);
    \foreach \x in {17,47,77,107,137,167,197}{\draw[TTCBlue!12!white] (\x,13) -- (\x,42);}
    \draw[TTCRed!18!white, line width=.7pt] (17,20) -- (197,20);
  \end{scope}
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{EPC总承包模式与价值工程}{Fast-Track Delivery, Value Engineering \& Single-Point Accountability}

{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
工期更短 • 流程更精简 • 投资风险更低\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
TTC将法定报批、工程设计、材料采购与施工安装整合于一份总包合同，全流程聚焦业主投资效益。\par}
\vspace{3mm}

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
    单一总包主体严密管控工程范围、投资预算、施工进度与交付质量。}
  };
  \node[rounded corners=2pt, fill=white, align=center, minimum width=29mm,
        minimum height=15mm] at (113,15) {
    {\fontsize{11}{12}\selectfont\bfseries\color{TTCRed} -15\%}\\[-.3mm]
    {\fontsize{5.8}{7}\selectfont\color{TTCBlue} 优化用钢量}
  };
  \node[rounded corners=2pt, fill=white, align=center, minimum width=29mm,
        minimum height=15mm] at (145,15) {
    {\fontsize{11}{12}\selectfont\bfseries\color{TTCCyan} -60 天}\\[-.3mm]
    {\fontsize{5.8}{7}\selectfont\color{TTCBlue} 缩短项目工期}
  };
  \node[rounded corners=2pt, fill=TTCGold, text=white, align=center,
        minimum width=29mm, minimum height=15mm] at (177,15) {
    {\fontsize{11}{12}\selectfont\bfseries 0}\\[-.3mm]
    {\fontsize{5.8}{7}\selectfont MEP机电碰撞}
  };
\end{tikzpicture}

\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,48);
  \fill[TTCLightBlue, rounded corners=3pt] (0,0) rectangle (186,48);
  \draw[TTCBorder, rounded corners=3pt, line width=.6pt] (0,0) rectangle (186,48);
  \node[anchor=west, text=TTCBlue, font=\fontsize{8}{9.5}\selectfont\bfseries] at (7,40)
    {\faProjectDiagram\quad 六大业务工作流 — 一体化价值链};
  \draw[TTCBlue!35!white, line width=1pt] (14,23) -- (172,23);
  \foreach \x/\n/\t/\s in {
    16/01/DEFINE/报批与需求,
    47/02/OPTIMIZE/VE与BIM 5D,
    78/03/ENGINEER/加工详图深化,
    109/04/FABRICATE/PEB制造供应,
    140/05/BUILD/基础与机电,
    171/06/OPERATE/数字孪生运维}{
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

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,49);
  \foreach \x/\c in {0/TTCRed,63/TTCCyan,126/TTCGold}{
    \fill[white, rounded corners=2pt] (\x,0) rectangle +(60,49);
    \draw[TTCBorder, rounded corners=2pt, line width=.6pt] (\x,0) rectangle +(60,49);
    \fill[\c, rounded corners=2pt] (\x,45) rectangle +(60,4);
  }
  \node[anchor=north west, text width=50mm] at (5,40) {
    {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCRed} 01 • 精益设计}\\[1mm]
    {\fontsize{10}{11}\selectfont\bfseries\color{TTCBlue} 结构截面优化}\\[1mm]
    {\fontsize{6.8}{8.2}\selectfont\color{TTCTextDark}
    按受力包络线采用变截面门架，减轻基础荷载同时确保安全储备。}
  };
  \node[anchor=north west, text width=50mm] at (68,40) {
    {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCCyan} 02 • 提前穿插}\\[1mm]
    {\fontsize{10}{11}\selectfont\bfseries\color{TTCBlue} 并行交叉推进}\\[1mm]
    {\fontsize{6.8}{8.2}\selectfont\color{TTCTextDark}
    方案设计、PEB构件排产与现场桩基土建按关键线路并行实施。}
  };
  \node[anchor=north west, text width=50mm] at (131,40) {
    {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCGold} 03 • 锁定风控}\\[1mm]
    {\fontsize{10}{11}\selectfont\bfseries\color{TTCBlue} 严控变更与造价}\\[1mm]
    {\fontsize{6.8}{8.2}\selectfont\color{TTCTextDark}
    BIM碰撞检测、出厂关口放行与总价包干合同有效杜绝额外签证。}
  };
\end{tikzpicture}

\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,29);
  \fill[TTCDeepNavy, rounded corners=3pt] (0,0) rectangle (186,29);
  \foreach \x in {46.5,93,139.5}{\draw[white!35!gray] (\x,6) -- (\x,23);}
  \node[align=center,text=white] at (23.25,15) {{\fontsize{9}{10}\selectfont\bfseries\color{TTCRed} 成本优化}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont 价值工程 (VE)}};
  \node[align=center,text=white] at (69.75,15) {{\fontsize{9}{10}\selectfont\bfseries\color{TTCCyan} 45--60 天}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont Fast-Track 快速建造}};
  \node[align=center,text=white] at (116.25,15) {{\fontsize{9}{10}\selectfont\bfseries 0 碰撞}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont BIM 全专业协同}};
  \node[align=center,text=white] at (162.75,15) {{\fontsize{9}{10}\selectfont\bfseries\color{TTCGold} 总价包干}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont 预算确定性保障}};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_15 = r"""% ============================================================
% TRANG 15: DIGITAL THREAD — BIM, AI, DIGITAL TWIN
% ============================================================
\pageheaderbar{建筑科技：BIM 5D、AI与智能数字孪生}{第15页}
\pagefooterbar{第15页}

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

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{贯穿工厂全生命周期的数字孪生数据流}{BIM 5D, AI Structural Optimization \& Smart Digital Twin}

{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
统一数据模型 • 三维智能决策 • 赋能全生命周期\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
设计数据不再停留在图纸上：它直接指导采购制造、现场施工、竣工验收以及长达30+年的智慧运维。\par}
\vspace{3mm}

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
    {\fontsize{17}{19}\selectfont\bfseries 数据驱动}\\[-.3mm]
    {\fontsize{17}{19}\selectfont\bfseries\color{TTCRed!85!white} 科学决策}\\[1.8mm]
    {\fontsize{7}{8.5}\selectfont\color{white!82!gray}
    为设计院、施工指挥部与业主运营团队提供唯一可信数据源。}
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

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,62);
  \foreach \x/\c in {0/TTCRed,63/TTCCyan,126/TTCGold}{
    \fill[white,rounded corners=2pt] (\x,0) rectangle +(60,62);
    \draw[TTCBorder,rounded corners=2pt,line width=.6pt] (\x,0) rectangle +(60,62);
    \fill[\c,rounded corners=2pt] (\x,58) rectangle +(60,4);
  }
  \node[anchor=north west,text width=50mm] at (5,53) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCRed} 01 / 协同深化}\\[1mm]
    {\fontsize{11}{12}\selectfont\bfseries\color{TTCBlue} BIM 5D 全专业}\\[1.2mm]
    {\fontsize{6.8}{8.2}\selectfont\color{TTCTextDark}
    \textbf{输入：} 建筑 • 结构 • 机电MEP\newline
    \textbf{决策：} 碰撞检测与4D施工模拟\newline
    \textbf{输出：} 加工详图、精确BOQ清单}\\[1mm]
    {\fontsize{6.2}{7.3}\selectfont\bfseries\color{TTCTextMuted} TEKLA • REVIT • NAVISWORKS}
  };
  \node[anchor=north west,text width=50mm] at (68,53) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} 02 / 智能优化}\\[1mm]
    {\fontsize{11}{12}\selectfont\bfseries\color{TTCBlue} AI 结构计算}\\[1.2mm]
    {\fontsize{6.8}{8.2}\selectfont\color{TTCTextDark}
    \textbf{输入：} 荷载 • 柱网跨度 • 内力包络\newline
    \textbf{决策：} 遗传算法多变量截面迭代\newline
    \textbf{输出：} 结构成本优化 10--15\% 最优方案}\\[1mm]
    {\fontsize{6.2}{7.3}\selectfont\bfseries\color{TTCTextMuted} AISC 360 • EUROCODE • AIDC R\&D}
  };
  \node[anchor=north west,text width=50mm] at (131,53) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCGold} 03 / 智慧运营}\\[1mm]
    {\fontsize{11}{12}\selectfont\bfseries\color{TTCBlue} 数字孪生资产}\\[1.2mm]
    {\fontsize{6.8}{8.2}\selectfont\color{TTCTextDark}
    \textbf{输入：} 竣工模型 • 设备台账 • IoT传感\newline
    \textbf{决策：} 基于设备状态的预测性维保\newline
    \textbf{输出：} 30+年可追溯资产数字档案}\\[1mm]
    {\fontsize{6.2}{7.3}\selectfont\bfseries\color{TTCTextMuted} CDE • BMS • SCADA READY}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_16 = r"""% ============================================================
% TRANG 16: ESG BUSINESS CASE — GREEN FACTORY
% ============================================================
\pageheaderbar{绿色ESG建筑与屋顶光伏就绪}{第16页}
\pagefooterbar{第16页}

\begin{tikzpicture}[remember picture, overlay]
  \fill[TTCLightBlue]
    ([xshift=125mm,yshift=-30mm]current page.north west) --
    ([xshift=210mm,yshift=-30mm]current page.north west) --
    ([xshift=210mm,yshift=-112mm]current page.north west) -- cycle;
  \node[opacity=.03,text=TTCBlue,font=\fontsize{64}{66}\selectfont\bfseries,
        rotate=90] at ([xshift=-11mm,yshift=2mm]current page.east) {ESG};
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
\secbrand{将绿色低碳理念融入工程商业价值模型}{Solar-Ready, Low-Energy Envelope, Water Circularity \& Green Certification}

{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
削减OPEX运营成本 • 顺应碳关税合规 • 提升资产价值\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
绿色ESG设计从前期结构载荷与围护系统深度集成，避免投产后再行改造带来的高昂成本。\par}
\vspace{3mm}

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
    屋顶荷载、能耗模拟、水资源循环与绿色认证协同设计。}
  };
  \node[rounded corners=2pt,fill=white,align=center,minimum width=31mm,
        minimum height=15mm] at (121,15) {
    {\fontsize{10}{11}\selectfont\bfseries\color{TTCRed} 1--5 MWp}\\[-.2mm]
    {\fontsize{5.8}{7}\selectfont\color{TTCBlue} 光伏就绪屋面}
  };
  \node[rounded corners=2pt,fill=TTCCyan,align=center,text=white,
        minimum width=31mm,minimum height=15mm] at (155,15) {
    {\fontsize{10}{11}\selectfont\bfseries -20\%}\\[-.2mm]
    {\fontsize{5.8}{7}\selectfont 暖通能耗降低}
  };
\end{tikzpicture}

\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,51);
  \foreach \x/\c in {0/TTCRed,47.5/TTCCyan,95/TTCBlue,142.5/TTCGold}{
    \fill[white,rounded corners=2pt] (\x,0) rectangle +(43.5,51);
    \draw[TTCBorder,rounded corners=2pt,line width=.6pt] (\x,0) rectangle +(43.5,51);
    \fill[\c,rounded corners=2pt] (\x,47) rectangle +(43.5,4);
  }
  \node[anchor=north west,text width=35mm] at (4,43) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCRed} 01 / 清洁能源}\\[1mm]
    {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCBlue} 光伏系统就绪}\\[1mm]
    {\fontsize{6.5}{7.8}\selectfont\color{TTCTextDark}
    预留屋顶荷载与直锁式立缝咬合件，可即装 1--5MWp 光伏。}
  };
  \node[anchor=north west,text width=35mm] at (51.5,43) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} 02 / 节能围护}\\[1mm]
    {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCBlue} 高效隔热系统}\\[1mm]
    {\fontsize{6.5}{7.8}\selectfont\color{TTCTextDark}
    PIR/岩棉夹芯板与高反射涂层屋面大幅降低暖通空调能耗。}
  };
  \node[anchor=north west,text width=35mm] at (99,43) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCBlue} 03 / 水循环}\\[1mm]
    {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCBlue} 循环回用系统}\\[1mm]
    {\fontsize{6.5}{7.8}\selectfont\color{TTCTextDark}
    QCVN 40 A级污水处理站与雨水收集回用系统用于绿化灌溉。}
  };
  \node[anchor=north west,text width=35mm] at (146.5,43) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCGold} 04 / 绿色认证}\\[1mm]
    {\fontsize{8.5}{10}\selectfont\bfseries\color{TTCBlue} LEED / LOTUS}\\[1mm]
    {\fontsize{6.5}{7.8}\selectfont\color{TTCTextDark}
    能耗模拟分析、Low-VOC低挥发材料及全套绿色认证申报支持。}
  };
\end{tikzpicture}

\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,47);
  \fill[TTCLightBlue,rounded corners=3pt] (0,0) rectangle (186,47);
  \draw[TTCBorder,rounded corners=3pt,line width=.6pt] (0,0) rectangle (186,47);
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries] at (7,39)
    {\faGlobeAmericas\quad 赋能外资跨国企业 (FDI) 核心诉求};
  \foreach \x in {62,124}{\draw[TTCBorder] (\x,6) -- (\x,31);}
  \node[align=left,text width=50mm,anchor=north west] at (6,30) {
    {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCRed} 绿色金融准入}\\[.7mm]
    {\fontsize{6.5}{7.8}\selectfont\color{TTCTextDark}
    助力企业轻松对接绿色低息信贷与跨国供应链ESG评级准入标准。}
  };
  \node[align=left,text width=50mm,anchor=north west] at (68,30) {
    {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCCyan} 应对碳关税壁垒}\\[.7mm]
    {\fontsize{6.5}{7.8}\selectfont\color{TTCTextDark}
    精准采集能耗数据，满足欧盟CBAM碳关税、I-REC绿证与零碳路线图。}
  };
  \node[align=left,text width=50mm,anchor=north west] at (130,30) {
    {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCGold} 显著降低OPEX}\\[.7mm]
    {\fontsize{6.5}{7.8}\selectfont\color{TTCTextDark}
    自发自用降低电费支出，优化中水利用，长效提升工厂资产残值。}
  };
\end{tikzpicture}

\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,29);
  \fill[TTCDeepNavy, rounded corners=3pt] (0,0) rectangle (186,29);
  \foreach \x in {46.5,93,139.5}{\draw[white!35!gray] (\x,6) -- (\x,23);}
  \node[align=center,text=white] at (23.25,15) {{\fontsize{9}{10}\selectfont\bfseries\color{TTCRed} 1--5 MWp}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont 光伏就绪屋顶}};
  \node[align=center,text=white] at (69.75,15) {{\fontsize{9}{10}\selectfont\bfseries\color{TTCCyan} -20\% 电耗}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont 暖通节能优化}};
  \node[align=center,text=white] at (116.25,15) {{\fontsize{9}{10}\selectfont\bfseries LEED / LOTUS}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont 国际绿色建筑标准}};
  \node[align=center,text=white] at (162.75,15) {{\fontsize{9}{10}\selectfont\bfseries\color{TTCGold} 100\% A级水}\\[-.3mm]{\fontsize{6.2}{7.4}\selectfont 污水达标循环利用}};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_17 = r"""% ============================================================
% TRANG 17: DIGITAL SITE CONTROL CENTER
% ============================================================
\pageheaderbar{数字化智慧工地与AI智能监控}{第17页}
\pagefooterbar{第17页}

\begin{tikzpicture}[remember picture, overlay]
  \fill[TTCLightBlue]
    ([xshift=131mm,yshift=-30mm]current page.north west) --
    ([xshift=210mm,yshift=-30mm]current page.north west) --
    ([xshift=210mm,yshift=-115mm]current page.north west) -- cycle;
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
\secbrand{数字化智慧工地指挥中心}{数据集中交互 • 风险即时预警 • 过程全程追溯}

{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
单一智慧工地 • 三大实时数据源 • 一体化指挥调度\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
全面聚合人员实名制、安全监控及工程档案数据，赋能现场项目经理精准处置与高效把控。\par}
\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,101);
  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,101);
  \draw[TTCCyan!65!white,rounded corners=3pt,line width=.8pt] (0,0) rectangle (186,101);

  \node[anchor=west,text=white,font=\fontsize{8}{9.5}\selectfont\bfseries] at (8,93)
    {\faDesktop\quad 数字化智慧工地指挥中心};
  \node[anchor=east,text=TTCCyan,font=\fontsize{6.3}{7.5}\selectfont\bfseries] at (121,93)
    {真实数据 • 留痕管控};

  % Status row
  \foreach \x/\c in {8/TTCRed,47/TTCCyan,86/TTCGold}{
    \fill[white!7!TTCDeepNavy,rounded corners=2pt] (\x,63) rectangle +(34,21);
    \draw[\c!70!white,rounded corners=2pt,line width=.55pt] (\x,63) rectangle +(34,21);
  }
  \node[anchor=west,text=TTCRed,font=\fontsize{6.2}{7.3}\selectfont\bfseries] at (11,78) {实名制门禁};
  \node[anchor=west,text=white,font=\fontsize{9.2}{10.5}\selectfont\bfseries] at (11,70) {持证精准准入};
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.2}{7.3}\selectfont\bfseries] at (50,78) {AI 视频安监};
  \node[anchor=west,text=white,font=\fontsize{9.2}{10.5}\selectfont\bfseries] at (50,70) {隐患智能识别};
  \node[anchor=west,text=TTCGold,font=\fontsize{6.2}{7.3}\selectfont\bfseries] at (89,78) {云端工程档案};
  \node[anchor=west,text=white,font=\fontsize{9.2}{10.5}\selectfont\bfseries] at (89,70) {版本唯一受控};

  % Three data streams
  \fill[white,rounded corners=2pt] (8,29) rectangle (40,55);
  \fill[white,rounded corners=2pt] (47,29) rectangle (79,55);
  \fill[white,rounded corners=2pt] (86,29) rectangle (118,55);
  \node[align=center,text width=27mm] at (24,42) {
    {\fontsize{7.5}{9}\selectfont\bfseries\color{TTCRed} 人力数据}\\[-.2mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}人脸识别 • 技能证书\\入场安全培训}
  };
  \node[align=center,text width=27mm] at (63,42) {
    {\fontsize{7.5}{9}\selectfont\bfseries\color{TTCCyan} 智能安防}\\[-.2mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}AI摄像头 • PPE违规\\危险区域闯入}
  };
  \node[align=center,text width=27mm] at (102,42) {
    {\fontsize{7.5}{9}\selectfont\bfseries\color{TTCGold} 数字档案}\\[-.2mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}CDE平台 • ITP验收\\电子施工日志}
  };
  \draw[-{Stealth[length=2mm]},TTCCyan,line width=.8pt] (40.5,42) -- (46,42);
  \draw[-{Stealth[length=2mm]},TTCCyan,line width=.8pt] (79.5,42) -- (85,42);

  % Decision layer
  \fill[TTCCyan!12!TTCDeepNavy,rounded corners=2pt] (8,7) rectangle (118,21);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6}{7}\selectfont\bfseries] at (12,14)
    {指挥控制流};
  \node[anchor=west,text=white,font=\fontsize{7}{8.5}\selectfont\bfseries] at (36,14)
    {AI报警触发 → 派单责任人 → 现场整改 → 留痕归档};

  % Site photo
  \begin{scope}
    \clip[rounded corners=2pt] (126,16) rectangle (179,86);
    \node[anchor=center,inner sep=0pt] at (152.5,51)
      {\includegraphics[height=70mm]{../../public/c_level_site_inspection.jpg}};
  \end{scope}
  \draw[white!45!gray,rounded corners=2pt,line width=.6pt] (126,16) rectangle (179,86);
  \fill[TTCBlue] (126,7) rectangle (179,15);
  \node[text=white,font=\fontsize{6.4}{7.5}\selectfont\bfseries] at (152.5,11)
    {管理层一线巡检现场};
\end{tikzpicture}

\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,49);
  \fill[white,rounded corners=3pt] (0,0) rectangle (186,49);
  \draw[TTCBorder,rounded corners=3pt,line width=.6pt] (0,0) rectangle (186,49);
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries] at (7,41)
    {\faMobile*\quad 赋能业主与监理透明决策};
  \foreach \x in {62,124}{\draw[TTCBorder] (\x,7) -- (\x,33);}
  \node[anchor=north west,text width=50mm] at (6,31) {
    {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCRed} 劳务出勤透明}\\[.7mm]
    {\fontsize{6.6}{8}\selectfont\color{TTCTextDark}
    实时掌握在场工人总数、工种分布与特殊工种资格状态。}
  };
  \node[anchor=north west,text width=50mm] at (68,31) {
    {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCCyan} 安全态势可视化}\\[.7mm]
    {\fontsize{6.6}{8}\selectfont\color{TTCTextDark}
    未戴安全帽/反光背心等违规行为自动抓拍并推送整改。}
  };
  \node[anchor=north west,text width=50mm] at (130,31) {
    {\fontsize{8}{9.5}\selectfont\bfseries\color{TTCGold} 验收档案完备}\\[.7mm]
    {\fontsize{6.6}{8}\selectfont\color{TTCTextDark}
    电子日志、RFI与ITP检验记录带时间戳与数字签名可追溯。}
  };
\end{tikzpicture}

\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,43);
  \fill[TTCLightBlue,rounded corners=3pt] (0,0) rectangle (186,43);
  \draw[TTCBorder,rounded corners=3pt,line width=.6pt] (0,0) rectangle (186,43);
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries] at (7,35)
    {\faCheckCircle\quad 每日数字化管理执行闭环};
  \foreach \x/\n/\t in {23/01/数据采集,69/02/智能预警,115/03/现场处置,161/04/归档留痕}{
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
\pageheaderbar{全面QA/QC质量体系与AWS D1.1标准}{第18页}
\pagefooterbar{第18页}

\begin{tikzpicture}[remember picture, overlay]
  \fill[TTCLightBlue]
    ([xshift=121mm,yshift=-31mm]current page.north west) --
    ([xshift=210mm,yshift=-31mm]current page.north west) --
    ([xshift=210mm,yshift=-118mm]current page.north west) -- cycle;
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
\secbrand{各专业分项工程质量通行证体系}{4级 ITP 严格受控 • 凭齐备数据凭据逐级放行}

{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
凭充分检验凭据方可转入下一道工序\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
每批原材料、每条焊缝及每道分项工程均须经过检验、签署并归档，方可放行进入下一道工序。\par}
\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,122);

  % Left ladder
  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (57,122);
  \node[anchor=west,text=TTCCyan,font=\fontsize{7}{8}\selectfont\bfseries] at (6,113)
    {4 级品控管理};
  \node[anchor=west,text=white,font=\fontsize{11}{12}\selectfont\bfseries] at (6,106.5)
    {ITP 检验关口};

  \foreach \y/\n/\c in {78/01/TTCRed,52/02/TTCBlue,26/03/TTCCyan,0/04/TTCGold}{
    \fill[white,rounded corners=2pt] (6,\y+6) rectangle (51,\y+25);
    \draw[\c,rounded corners=2pt,line width=.7pt] (6,\y+6) rectangle (51,\y+25);
    \fill[\c] (6,\y+6) rectangle (13,\y+25);
    \node[text=white,font=\fontsize{6.5}{7}\selectfont\bfseries] at (9.5,\y+15.5) {\n};
  }
  \node[anchor=west,text width=33mm] at (16,93.5) {
    {\fontsize{7.2}{8.5}\selectfont\bfseries\color{TTCRed} 班组自检}\\[-.2mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}内部自查与交接单}
  };
  \node[anchor=west,text width=33mm] at (16,67.5) {
    {\fontsize{7.2}{8.5}\selectfont\bfseries\color{TTCBlue} 专业工程师复核}\\[-.2mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}对照施工图纸与ITP}
  };
  \node[anchor=west,text width=33mm] at (16,41.5) {
    {\fontsize{7.2}{8.5}\selectfont\bfseries\color{TTCCyan} 独立专职 QA/QC}\\[-.2mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}NDT报告与试验数据}
  };
  \node[anchor=west,text width=33mm] at (16,15.5) {
    {\fontsize{7.2}{8.5}\selectfont\bfseries\color{TTCGold} 监理 / 业主确认}\\[-.2mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}最终签字验收放行}
  };
  \draw[-{Stealth[length=2mm]},white!55!gray,line width=.8pt] (28.5,83) -- (28.5,78);
  \draw[-{Stealth[length=2mm]},white!55!gray,line width=.8pt] (28.5,57) -- (28.5,52);
  \draw[-{Stealth[length=2mm]},white!55!gray,line width=.8pt] (28.5,31) -- (28.5,26);

  % Right passport
  \fill[white,rounded corners=3pt] (62,0) rectangle (186,122);
  \draw[TTCBorder,rounded corners=3pt,line width=.7pt] (62,0) rectangle (186,122);
  \fill[TTCLightBlue,rounded corners=3pt] (62,101) rectangle (186,122);
  \node[anchor=west,text=TTCBlue,font=\fontsize{10}{11.5}\selectfont\bfseries] at (68,113)
    {\faClipboardCheck\quad 分项工程质量通行证};
  \node[anchor=east,text=TTCTextMuted,font=\fontsize{6}{7}\selectfont\bfseries] at (180,113)
    {任务包代码 / 全程追溯};

  \foreach \y/\n/\c in {78/01/TTCRed,55/02/TTCBlue,32/03/TTCCyan,9/04/TTCGold}{
    \fill[\c!6!white,rounded corners=1.5pt] (68,\y) rectangle (180,\y+18);
    \node[anchor=west,text=\c,font=\fontsize{7}{8}\selectfont\bfseries] at (72,\y+12) {\n};
    \fill[\c] (165,\y+5) circle (2.3);
    \node[text=white,font=\fontsize{5}{5.5}\selectfont\bfseries] at (165,\y+5) {\faCheck};
    \node[anchor=west,text=TTCTextMuted,font=\fontsize{6.1}{7.2}\selectfont\bfseries] at (170,\y+5) {合格};
  }
  \node[anchor=west,text=TTCBlue,font=\fontsize{7.4}{8.7}\selectfont\bfseries] at (81,90) {原材料质量溯源};
  \node[anchor=west,text=TTCTextDark,font=\fontsize{6.3}{7.5}\selectfont] at (81,84) {CO/CQ 原产地证明 • 炉批号 • 出厂质保书 • 进场复验报告};
  \node[anchor=west,text=TTCBlue,font=\fontsize{7.4}{8.7}\selectfont\bfseries] at (81,67) {钢构焊接工艺控制};
  \node[anchor=west,text=TTCTextDark,font=\fontsize{6.3}{7.5}\selectfont] at (81,61) {WPS/PQR 规程 • 焊工钢印 • 美国 AWS D1.1 • 焊缝追踪排布图};
  \node[anchor=west,text=TTCBlue,font=\fontsize{7.4}{8.7}\selectfont\bfseries] at (81,44) {无损探伤无缝检验};
  \node[anchor=west,text=TTCTextDark,font=\fontsize{6.3}{7.5}\selectfont] at (81,38) {外观VT • 超声UT • 磁粉MT/渗透PT • 第三方检测机构报告};
  \node[anchor=west,text=TTCBlue,font=\fontsize{7.4}{8.7}\selectfont\bfseries] at (81,21) {竣工档案与数字闭环};
  \node[anchor=west,text=TTCTextDark,font=\fontsize{6.3}{7.5}\selectfont] at (81,15) {签署ITP检验批 • 闭环NCR • 竣工图纸 • CDE云端永久留存};
\end{tikzpicture}

\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,46);
  \fill[TTCLightBlue,rounded corners=3pt] (0,0) rectangle (186,46);
  \draw[TTCBorder,rounded corners=3pt,line width=.6pt] (0,0) rectangle (186,46);
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries] at (7,38)
    {\faCheckDouble\quad NDT 无损探伤与物理力学检测方法};
  \foreach \x in {46.5,93,139.5}{\draw[TTCBorder] (\x,6) -- (\x,31);}
  \node[align=center,text width=38mm] at (23.25,18) {
    {\fontsize{9}{10}\selectfont\bfseries\color{TTCRed} VT 目视检测}\\[-.2mm]
    {\fontsize{6.1}{7.3}\selectfont 几何尺寸 • 咬边 • 焊脚高度}
  };
  \node[align=center,text width=38mm] at (69.75,18) {
    {\fontsize{9}{10}\selectfont\bfseries\color{TTCCyan} UT 超声探伤}\\[-.2mm]
    {\fontsize{6.3}{7.5}\selectfont 内部夹渣 • 气孔 • 未熔合}
  };
  \node[align=center,text width=38mm] at (116.25,18) {
    {\fontsize{9}{10}\selectfont\bfseries\color{TTCBlue} MT / PT 磁粉渗透}\\[-.2mm]
    {\fontsize{6.3}{7.5}\selectfont 表面微裂纹与角焊缝缺陷}
  };
  \node[align=center,text width=38mm] at (162.75,18) {
    {\fontsize{9}{10}\selectfont\bfseries\color{TTCGold} LAS-XD 试验室}\\[-.2mm]
    {\fontsize{6.3}{7.5}\selectfont 国家资质试验室力学拉拔}
  };
\end{tikzpicture}

\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,30);
  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,30);
  \node[anchor=west,text=TTCCyan,font=\fontsize{7}{8}\selectfont\bfseries] at (8,20)
    {质量放行铁律};
  \node[anchor=west,text=white,font=\fontsize{10}{11.5}\selectfont\bfseries] at (8,11)
    {检验合格 → 数据齐全 → 签字核准 → 全程可溯};
  \node[anchor=east,text=TTCGold,font=\fontsize{12}{13}\selectfont\bfseries] at (178,15)
    {AWS D1.1 • ISO 9001};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_19 = r"""% ============================================================
% TRANG 19: HSE DECISION SYSTEM & STOP WORK AUTHORITY
% ============================================================
\pageheaderbar{HSE职业健康安全与零事故文化}{第19页}
\pagefooterbar{第19页}

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
\secbrand{安全是一套严密的管理决策机制 — 不仅仅是劳保装备}{Risk Elimination, Daily Control Cycle \& Stop Work Authority}

{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
洞察隐患 • 事前管控 • 遇险立即行使停工权\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
工期进度绝不能成为容忍不安全作业环境的借口；人的生命安全永远高于一切。\par}
\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,149);

  % Left manifesto
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
    任何员工在发现安全条件不具备时，均有权且必须立即下达停工指令。}\\[2mm]
    {\fontsize{7}{8.5}\selectfont\bfseries\color{TTCGold}
    生命安全高于一切生产效益}
  };

  % Right — hierarchy of controls
  \fill[white,rounded corners=3pt] (63,86) rectangle (186,149);
  \draw[TTCBorder,rounded corners=3pt,line width=.6pt] (63,86) rectangle (186,149);
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries] at (69,141)
    {\faShield*\quad 风险控制四级优先层级};

  \fill[TTCRed] (69,124) rectangle (180,136);
  \fill[TTCBlue] (74,111) rectangle (175,123);
  \fill[TTCCyan] (79,98) rectangle (170,110);
  \fill[TTCGold] (84,85) rectangle (165,97);
  \node[anchor=west,text=white,font=\fontsize{7}{8}\selectfont\bfseries] at (73,130) {01 • 消除 (ELIMINATE) — 优化工艺从源头根除危险};
  \node[anchor=west,text=white,font=\fontsize{7}{8}\selectfont\bfseries] at (78,117) {02 • 工程防护 (ENGINEER) — 临边护栏、安全网与生命线};
  \node[anchor=west,text=white,font=\fontsize{7}{8}\selectfont\bfseries] at (83,104) {03 • 管理许可 (PERMIT) — JSA风险分析与动火作业票};
  \node[anchor=west,text=white,font=\fontsize{7}{8}\selectfont\bfseries] at (88,91) {04 • 劳保防护 (PPE) — 个人最后一道被动安全屏障};

  % Right — daily cycle
  \fill[TTCLightBlue,rounded corners=3pt] (63,29) rectangle (186,81);
  \draw[TTCBorder,rounded corners=3pt,line width=.6pt] (63,29) rectangle (186,81);
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries] at (69,73)
    {\faClock\quad 每日安全闭环控制流程};
  \draw[TTCBlue!35!white,line width=1pt] (76,50) -- (175,50);
  \foreach \x/\n/\t in {77/01/策划,102/02/交底,127/03/核查,152/04/作业,175/05/收工}{
    \fill[white] (\x,50) circle (4.5);
    \draw[TTCBlue,line width=.75pt] (\x,50) circle (4.5);
    \node[text=TTCRed,font=\fontsize{5.8}{6.5}\selectfont\bfseries] at (\x,50) {\n};
    \node[anchor=north,align=center,text width=22mm] at (\x,42)
      {{\fontsize{6}{7.2}\selectfont\bfseries\color{TTCBlue} \t}};
  }
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{6}{7.3}\selectfont] at (70,33)
    {JSA安全分析 → 班前会 (Toolbox) → 装备核查 → 旁站监督 → 现场清场};

  % Emergency row
  \fill[white,rounded corners=3pt] (63,0) rectangle (186,24);
  \draw[TTCBorder,rounded corners=3pt,line width=.6pt] (63,0) rectangle (186,24);
  \node[anchor=west,text=TTCRed,font=\fontsize{8}{9.5}\selectfont\bfseries] at (69,16)
    {\faFireExtinguisher\quad 应急响应保障机制};
  \node[anchor=west,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont] at (69,7)
    {即时警报 • 隔离现场 • 紧急疏散 • 现场急救 • 事故溯源调查 • 制定防范措施};
\end{tikzpicture}

\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,48);
  \fill[white,rounded corners=3pt] (0,0) rectangle (186,48);
  \draw[TTCBorder,rounded corners=3pt,line width=.6pt] (0,0) rectangle (186,48);
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries] at (7,40)
    {\faHandPaper\quad 现场五大保命安全法则};
  \foreach \x in {37.2,74.4,111.6,148.8}{\draw[TTCBorder] (\x,6) -- (\x,31);}
  \node[align=center,text width=32mm] at (18.6,18) {
    {\fontsize{7.3}{8.5}\selectfont\bfseries\color{TTCRed} 高空作业}\\[-.2mm]
    {\fontsize{5.8}{7}\selectfont 双大钩 • 生命绳 • 防坠网}
  };
  \node[align=center,text width=32mm] at (55.8,18) {
    {\fontsize{7.3}{8.5}\selectfont\bfseries\color{TTCBlue} 起重吊装}\\[-.2mm]
    {\fontsize{5.8}{7}\selectfont 警戒区 • 专职指挥 • 吊具核验}
  };
  \node[align=center,text width=32mm] at (93,18) {
    {\fontsize{7.3}{8.5}\selectfont\bfseries\color{TTCCyan} 施工用电}\\[-.2mm]
    {\fontsize{5.8}{7}\selectfont 漏保开关 • 可靠接地 • 上锁挂牌}
  };
  \node[align=center,text width=32mm] at (130.2,18) {
    {\fontsize{7.3}{8.5}\selectfont\bfseries\color{TTCGold} 动火作业}\\[-.2mm]
    {\fontsize{5.8}{7}\selectfont 专人看火 • 灭火器材 • 动火票}
  };
  \node[align=center,text width=32mm] at (167.4,18) {
    {\fontsize{7.3}{8.5}\selectfont\bfseries\color{TTCBlue} 基坑开挖}\\[-.2mm]
    {\fontsize{5.8}{7}\selectfont 规范放坡 • 临边护栏 • 逃生通道}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

print("Section 4 (Pages 14-19) Chinese version loaded successfully.")
