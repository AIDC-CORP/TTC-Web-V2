# -*- coding: utf-8 -*-
"""
Section 2: Financial Governance, Credit Capacity & Talent Development (Pages 08 - 10) — 简体中文版
"""

PAGE_08 = r"""% ============================================================
% TRANG 08: QUẢN TRỊ TÀI CHÍNH DỰ ÁN & KỶ LUẬT DÒNG TIỀN
% ============================================================
\pageheaderbar{项目成本、合同与记录治理}{第08页}
\pagefooterbar{第08页}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.025, scale=2.6, font=\bfseries\sffamily, text=TTCBlue]
    at ([yshift=-12mm]current page.center) {FINANCIAL GOVERNANCE \& DISCIPLINE};
  \draw[TTCBlue!6!white, line width=0.45pt]
    ([xshift=15mm, yshift=20mm]current page.south west)
    grid[step=8mm]
    ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{项目成本、合同与记录治理}{Project Cost Governance • Contract Discipline • Verified \& Traceable Records}

\vspace{1mm}
{\fontsize{14.5}{16.5}\selectfont\bfseries\color{TTCBlue}
从投标决策到竣工结算的全流程闭环资金风控\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
每个工程均设立独立核算代码，严格执行四道管控关口与定期财务对账，确保资金安全与履约保障。\par}
\vspace{3.5mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,86);

  % KHỐI TRÁI: 4 CỔNG KIỂM SOÁT
  \fill[white, rounded corners=4pt] (0,0) rectangle (126,86);
  \draw[TTCBorder, line width=0.7pt, rounded corners=4pt] (0,0) rectangle (126,86);

  \node[anchor=west, text=TTCCyan, font=\fontsize{7}{8}\selectfont\bfseries]
    at (6,79.5) {FOUR FINANCIAL CONTROL GATES};
  \node[anchor=west, text=TTCBlue, font=\fontsize{10}{12}\selectfont\bfseries]
    at (6,72.5) {项目财务四道管控关口体系};

  % Timeline connector bar
  \draw[TTCBlue!30!white, line width=1pt] (15,50) -- (111,50);

  % Cổng 01
  \fill[TTCRed] (15,50) circle (4.8);
  \node[text=white, font=\fontsize{7}{8}\selectfont\bfseries] at (15,50) {01};
  \node[anchor=south, align=center, text width=26mm, text=TTCRed, font=\fontsize{7}{8.2}\selectfont\bfseries]
    at (15,57.5) {合同审查\\与风险评估};
  \node[anchor=north, align=center, text width=27mm, text=TTCTextDark, font=\fontsize{6.2}{7.6}\selectfont]
    at (15,42.5) {商务范围核对\\支付与结算条款\\保留款与合同风险};

  % Cổng 02
  \fill[white] (47,50) circle (4.8);
  \draw[TTCBlue, line width=0.85pt] (47,50) circle (4.8);
  \node[text=TTCBlue, font=\fontsize{7}{8}\selectfont\bfseries] at (47,50) {02};
  \node[anchor=south, align=center, text width=26mm, text=TTCBlue, font=\fontsize{7}{8.2}\selectfont\bfseries]
    at (47,57.5) {项目基准\\预算锁定};
  \node[anchor=north, align=center, text width=27mm, text=TTCTextDark, font=\fontsize{6.2}{7.6}\selectfont]
    at (47,42.5) {WBS成本基准\\阶段资金计划\\资源配置计划};

  % Cổng 03
  \fill[white] (79,50) circle (4.8);
  \draw[TTCBlue, line width=0.85pt] (79,50) circle (4.8);
  \node[text=TTCBlue, font=\fontsize{7}{8}\selectfont\bfseries] at (79,50) {03};
  \node[anchor=south, align=center, text width=26mm, text=TTCBlue, font=\fontsize{7}{8.2}\selectfont\bfseries]
    at (79,57.5) {过程执行\\动态监控};
  \node[anchor=north, align=center, text width=27mm, text=TTCTextDark, font=\fontsize{6.2}{7.6}\selectfont]
    at (79,42.5) {周度成本偏差分析\\工程变更(VO)审批\\竣工成本预测(EAC)};

  % Cổng 04
  \fill[white] (111,50) circle (4.8);
  \draw[TTCBlue, line width=0.85pt] (111,50) circle (4.8);
  \node[text=TTCBlue, font=\fontsize{7}{8}\selectfont\bfseries] at (111,50) {04};
  \node[anchor=south, align=center, text width=26mm, text=TTCBlue, font=\fontsize{7}{8.2}\selectfont\bfseries]
    at (111,57.5) {竣工验收\\与财务决算};
  \node[anchor=north, align=center, text width=27mm, text=TTCTextDark, font=\fontsize{6.2}{7.6}\selectfont]
    at (111,42.5) {竣工工程量档案\\应收账款回收清盘\\关闭项目成本账户};

  % Dải cam kết phía dưới khối trái
  \fill[TTCDeepNavy, rounded corners=3pt] (5,5.5) rectangle (121,18.5);
  \node[anchor=west, text=TTCCyan, font=\fontsize{6.8}{8}\selectfont\bfseries]
    at (8,12) {\faShield*\quad CONTROL BEFORE COMMITMENT};
  \node[anchor=east, text=white, font=\fontsize{6.5}{7.8}\selectfont\bfseries]
    at (118,12) {预算与资源计划获批后方可承诺};

  % KHỐI PHẢI: NGUYÊN TẮC QUẢN TRỊ
  \fill[TTCLightBlue, rounded corners=4pt] (131,0) rectangle (186,86);
  \draw[TTCBorder, line width=0.7pt, rounded corners=4pt] (131,0) rectangle (186,86);

  \node[anchor=north west, text=TTCCyan, font=\fontsize{7}{8}\selectfont\bfseries]
    at (136,79.5) {CONTROL PRINCIPLE};
  \node[anchor=north west, text width=46mm, text=TTCBlue, font=\fontsize{9.5}{11.5}\selectfont\bfseries]
    at (136,73) {严禁超能力盲目承揽};
  \fill[TTCRed] (136,61.5) rectangle (152,63);

  \node[anchor=north west, text width=45mm, text=TTCTextDark, font=\fontsize{6.8}{8.6}\selectfont]
    at (136,56) {
    \textcolor{TTCRed}{\faCheckCircle}\ \textbf{预算锁定：} 调配资源前完成成本基准审批。\\[2.4mm]
    \textcolor{TTCRed}{\faCheckCircle}\ \textbf{变更受控：} 额外支出必须有对应资金来源弥补。\\[2.4mm]
    \textcolor{TTCRed}{\faCheckCircle}\ \textbf{审慎承接：} 仅在交付资源与合同风险可控时扩大规模。
  };

  \fill[white, rounded corners=2.5pt, draw=TTCBorder, line width=0.55pt] (136,6) rectangle (181,18);
  \node[anchor=center, text=TTCBlue, font=\fontsize{6.6}{8}\selectfont\bfseries, align=center]
    at (158.5,12) {\faLock\quad 每个项目采用独立成本代码};
\end{tikzpicture}

\vspace{3.5mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,58);

  % Card 1: Cost Control
  \fill[white, rounded corners=4pt] (0,0) rectangle (58,58);
  \draw[TTCBorder, line width=0.65pt, rounded corners=4pt] (0,0) rectangle (58,58);
  \fill[TTCRed, rounded corners=1pt] (5,50.5) rectangle (22,52.5);
  \node[anchor=north west, text width=50mm, align=left] at (5,47.5) {
    {\fontsize{7}{8.2}\selectfont\bfseries\color{TTCRed}\faCalculator\quad COST CONTROL}\\[1.2mm]
    {\fontsize{9.8}{11.5}\selectfont\bfseries\color{TTCBlue} 成本动态精控}\\[2mm]
    {\fontsize{6.6}{8.2}\selectfont\color{TTCTextDark}
    \textbullet\ 按WBS建立基准预算 (Baseline)。\newline
    \textbullet\ 周度对比与成本偏差追踪预警。\newline
    \textbullet\ 完工总成本预测模型 (EAC)。}
  };

  % Card 2: Receivable Control
  \fill[white, rounded corners=4pt] (64,0) rectangle (122,58);
  \draw[TTCBorder, line width=0.65pt, rounded corners=4pt] (64,0) rectangle (122,58);
  \fill[TTCCyan, rounded corners=1pt] (69,50.5) rectangle (86,52.5);
  \node[anchor=north west, text width=50mm, align=left] at (69,47.5) {
    {\fontsize{7}{8.2}\selectfont\bfseries\color{TTCCyan}\faFileInvoiceDollar\quad RECEIVABLE CONTROL}\\[1.2mm]
    {\fontsize{9.8}{11.5}\selectfont\bfseries\color{TTCBlue} 账款严密管控}\\[2mm]
    {\fontsize{6.6}{8.2}\selectfont\color{TTCTextDark}
    \textbullet\ 紧跟4级ITP检验批节点请款。\newline
    \textbullet\ 实时监控预付款与工程进度款。\newline
    \textbullet\ 质保金与供应链付款全周期联动。}
  };

  % Card 3: Verified Reporting
  \fill[white, rounded corners=4pt] (128,0) rectangle (186,58);
  \draw[TTCBorder, line width=0.65pt, rounded corners=4pt] (128,0) rectangle (186,58);
  \fill[TTCBlue, rounded corners=1pt] (133,50.5) rectangle (150,52.5);
  \node[anchor=north west, text width=50mm, align=left] at (133,47.5) {
    {\fontsize{7}{8.2}\selectfont\bfseries\color{TTCBlue}\faClipboardCheck\quad VERIFIED REPORTING}\\[1.2mm]
    {\fontsize{9.8}{11.5}\selectfont\bfseries\color{TTCBlue} 溯源核验档案}\\[2mm]
    {\fontsize{6.6}{8.2}\selectfont\color{TTCTextDark}
    \textbullet\ 项目成本数据实时云端同步。\newline
    \textbullet\ 符合国际标准的管理会计月报。\newline
    \textbullet\ 随时接受业主委托独立三方审计。}
  };
\end{tikzpicture}

\vspace{3.5mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,46);

  % Outer Card
  \fill[white, rounded corners=4pt] (0,0) rectangle (186,46);
  \draw[TTCBorder, line width=0.65pt, rounded corners=4pt] (0,0) rectangle (186,46);

  % Left Navy Brand Anchor
  \fill[TTCDeepNavy, rounded corners=4pt] (0,0) rectangle (48,46);
  \node[anchor=west, text width=40mm, align=left] at (6,23) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} DISCLOSURE POLICY}\\[1.2mm]
    {\fontsize{9}{11}\selectfont\bfseries\color{white} 受控透明与\\合规披露}\\[1.8mm]
    {\fontsize{6}{7.2}\selectfont\color{white!75!gray}Verified data \textbullet\ Right audience}
  };

  % 4 Pill Cards
  \foreach \xa/\xb/\num/\label/\sub in {
    53/81/01/财务审计报告/独立三方审计,
    85/113/02/完税证明文件/依法足额纳税,
    117/145/03/供应链往来对账/供应商与分包商核对,
    149/181/04/项目管理报告/项目资金计划}{
    \fill[TTCLightBlue, rounded corners=3pt] (\xa,14) rectangle (\xb,40);
    \draw[TTCBorder, line width=0.5pt, rounded corners=3pt] (\xa,14) rectangle (\xb,40);
    \node[text=TTCRed, font=\fontsize{8}{9.5}\selectfont\bfseries] at ({(\xa+\xb)/2},34.5) {\num};
    \node[align=center, text width=26mm, text=TTCBlue, font=\fontsize{6.5}{7.8}\selectfont\bfseries]
      at ({(\xa+\xb)/2},26) {\label};
    \node[align=center, text width=26mm, text=TTCTextMuted, font=\fontsize{5.8}{7}\selectfont]
      at ({(\xa+\xb)/2},18.5) {\sub};
  }

  % Bottom Notice
  \draw[TTCBorder, line width=0.5pt] (53,9.5) -- (181,9.5);
  \node[anchor=south west, text=TTCTextMuted, font=\fontsize{6}{7.3}\selectfont\itshape]
    at (53,3) {\faLock\quad 详细财务与税务数据可在招标阶段或签署双向保密协议 (NDA) 后正式提供。};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_09 = r"""% ============================================================
% TRANG 09: NĂNG LỰC HUY ĐỘNG CHO DỰ ÁN EPC
% ============================================================
\pageheaderbar{合同保函与项目资源调配能力}{第09页}
\pagefooterbar{第09页}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.02, scale=2.4, font=\bfseries\sffamily, text=TTCBlue]
    at ([yshift=-12mm]current page.center) {BANKING CAPACITY \& SITE MOBILIZATION};
  \draw[TTCBlue!6!white, line width=0.45pt]
    ([xshift=15mm, yshift=20mm]current page.south west)
    grid[step=8mm]
    ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{保函文件与项目资源调配能力}{Banking Readiness, Contract Security \& Workforce Mobilization}

\vspace{1mm}
{\fontsize{14.5}{16.5}\selectfont\bfseries\color{TTCBlue}
双重履约引擎 • 一套经批准的综合调配计划\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
保函文件准备与多专业实施团队按合同阶段和关键作业面进行配置。\par}
\vspace{3.5mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,80);

  % KHỐI TRÁI: FINANCIAL ENGINE
  \fill[white, rounded corners=4pt] (0,0) rectangle (90,80);
  \draw[TTCBorder, line width=0.7pt, rounded corners=4pt] (0,0) rectangle (90,80);

  \node[anchor=north west, text=TTCCyan, font=\fontsize{7}{8}\selectfont\bfseries]
    at (6,73.5) {FINANCIAL ENGINE};
  \node[anchor=north west, text=TTCBlue, font=\fontsize{10}{12}\selectfont\bfseries]
    at (6,67) {银行授信与履约保函能力};

  \node[anchor=west] at (6,54) {
    {\fontsize{20}{22}\selectfont\bfseries\color{TTCRed} 文件就绪}\quad
    {\fontsize{7.5}{9}\selectfont\bfseries\color{TTCTextMuted} 按合同要求提交}
  };

  % Bank Badges
  \fill[TTCLightBlue, rounded corners=2.5pt, draw=TTCBorder, line width=0.5pt] (5,38) rectangle (85,46);
  \node[anchor=center, text=TTCBlue, font=\fontsize{6.2}{7.4}\selectfont\bfseries]
    at (45,42) {Vietcombank \textbullet\ BIDV \textbullet\ VietinBank \textbullet\ TPBank \textbullet\ ACB \textbullet\ MB};

  \node[anchor=north west, text width=80mm, text=TTCTextDark, font=\fontsize{6.8}{8.6}\selectfont]
    at (6,33.5) {
    \textcolor{TTCRed}{\faCheckCircle}\ \textbf{全类型保函：} 投标保函、履约保函、预付款保函与质保函。\\[1.4mm]
    \textcolor{TTCRed}{\faCheckCircle}\ \textbf{受控签发：} 保函须满足银行审批与合同条件。\\[1.4mm]
    \textcolor{TTCRed}{\faCheckCircle}\ \textbf{国际合同：} 可按项目要求协调FIDIC条款及信用证文件。
  };

  % KHỐI PHẢI: DELIVERY ENGINE
  \fill[white, rounded corners=4pt] (96,0) rectangle (186,80);
  \draw[TTCBorder, line width=0.7pt, rounded corners=4pt] (96,0) rectangle (186,80);

  \node[anchor=north west, text=TTCCyan, font=\fontsize{7}{8}\selectfont\bfseries]
    at (102,73.5) {DELIVERY ENGINE};
  \node[anchor=north west, text=TTCBlue, font=\fontsize{10}{12}\selectfont\bfseries]
    at (102,67) {实战型专业技术施工队伍};

  \node[anchor=west] at (102,54) {
    {\fontsize{20}{22}\selectfont\bfseries\color{TTCBlue} 按工种配置}\quad
    {\fontsize{7.5}{9}\selectfont\bfseries\color{TTCTextMuted} 依据工作包调配团队}
  };

  % Visual Distribution Bar
  \fill[TTCBlue, rounded corners=1.5pt] (102,41) rectangle (114,45);
  \fill[TTCCyan, rounded corners=1.5pt] (115,41) rectangle (180,45);
  \node[anchor=west, text=TTCBlue, font=\fontsize{6.2}{7.4}\selectfont\bfseries] at (102,47.5) {项目管理与专业工程师};
  \node[anchor=east, text=TTCCyan, font=\fontsize{6.6}{7.6}\selectfont\bfseries] at (180,47.5) {持证专业施工班组};

  \node[anchor=north west, text width=78mm, text=TTCTextDark, font=\fontsize{6.8}{8.6}\selectfont]
    at (102,33.5) {
    \textcolor{TTCBlue}{\faCheckCircle}\ \textbf{关键岗位：} 项目管理、BIM协调、质量与安全人员按项目任命。\\[1.4mm]
    \textcolor{TTCCyan}{\faCheckCircle}\ \textbf{专业班组：} 持证焊工、钢结构安装与机电施工人员按工序调配。\\[1.4mm]
    \textcolor{TTCTextMuted}{\faCheckCircle}\ \textbf{多作业面管理：} 依据关键路径、场地条件与获批施工方案组织作业。
  };

  % Joining Connector Pill
  \fill[white] (93,54) circle (4);
  \draw[TTCCyan, line width=0.8pt] (93,54) circle (4);
  \node[text=TTCRed, font=\fontsize{10}{11}\selectfont\bfseries] at (93,54) {+};
\end{tikzpicture}

\vspace{3.5mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,84);

  \node[anchor=west] at (0,79) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} CONTRACT LIFECYCLE}\quad
    {\fontsize{9.8}{11.5}\selectfont\bfseries\color{TTCBlue} 项目各生命周期阶段的资源精准配置}
  };

  % 4 Stages
  % Stage 01: Tender
  \fill[white, rounded corners=3.5pt] (0,0) rectangle (42,72);
  \draw[TTCBorder, line width=0.65pt, rounded corners=3.5pt] (0,0) rectangle (42,72);
  \fill[TTCLightBlue, rounded corners=3.5pt] (0,59) rectangle (42,72);
  \node[anchor=west] at (4,65.5) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} 01 / TENDER}
  };
  \node[anchor=north west, text width=34mm, align=left] at (4,53) {
    {\fontsize{9.8}{11.5}\selectfont\bfseries\color{TTCBlue} 投标筹备}\\[2.2mm]
    {\fontsize{6.5}{7.8}\selectfont\bfseries\color{TTCTextMuted} 财务资源}\\[0.7mm]
    {\fontsize{6.8}{8.2}\selectfont\color{TTCTextDark}按招标文件确认投标保函与资信材料。}\\[2mm]
    {\fontsize{6.5}{7.8}\selectfont\bfseries\color{TTCTextMuted} 人员配置}\\[0.7mm]
    {\fontsize{6.8}{8.2}\selectfont\color{TTCTextDark}造价师、价值工程与商务谈判专家。}
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
    {\fontsize{9.8}{11.5}\selectfont\bfseries\color{TTCBlue} 合同签署}\\[2.2mm]
    {\fontsize{6.5}{7.8}\selectfont\bfseries\color{TTCTextMuted} 财务资源}\\[0.7mm]
    {\fontsize{6.8}{8.2}\selectfont\color{TTCTextDark}按合同及银行审批条件办理履约与预付款保函。}\\[2mm]
    {\fontsize{6.5}{7.8}\selectfont\bfseries\color{TTCTextMuted} 人员配置}\\[0.7mm]
    {\fontsize{6.8}{8.2}\selectfont\color{TTCTextDark}任命项目总监、项目经理及骨干团队。}
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
    {\fontsize{9.8}{11.5}\selectfont\bfseries\color{TTCBlue} 现场施工}\\[2.2mm]
    {\fontsize{6.5}{7.8}\selectfont\bfseries\color{TTCTextMuted} 财务资源}\\[0.7mm]
    {\fontsize{6.8}{8.2}\selectfont\color{TTCTextDark}按获批项目资金计划、采购条件与结算节点执行。}\\[2mm]
    {\fontsize{6.5}{7.8}\selectfont\bfseries\color{TTCTextMuted} 人员配置}\\[0.7mm]
    {\fontsize{6.8}{8.2}\selectfont\color{TTCTextDark}常驻指挥部、专业工程师与多班组作业。}
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
    {\fontsize{9.8}{11.5}\selectfont\bfseries\color{TTCBlue} 竣工交付}\\[2.2mm]
    {\fontsize{6.5}{7.8}\selectfont\bfseries\color{TTCTextMuted} 财务资源}\\[0.7mm]
    {\fontsize{6.8}{8.2}\selectfont\color{TTCTextDark}保修保函与期限按具体合同确定。}\\[2mm]
    {\fontsize{6.5}{7.8}\selectfont\bfseries\color{TTCTextMuted} 人员配置}\\[0.7mm]
    {\fontsize{6.8}{8.2}\selectfont\color{TTCTextDark}联合调试、竣工资料交付与合同约定保修。}
  };
  \fill[TTCRed, rounded corners=2pt] (150,3.5) rectangle (180,10);
  \node[anchor=center] at (165,6.75) {
    {\fontsize{6.4}{7.8}\selectfont\bfseries\color{white} O\&M-READY}
  };
\end{tikzpicture}

\vspace{3.5mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,43);

  % Outer Card
  \fill[white, rounded corners=4pt] (0,0) rectangle (186,43);
  \draw[TTCBorder, line width=0.65pt, rounded corners=4pt] (0,0) rectangle (186,43);

  % Left Navy Anchor
  \fill[TTCDeepNavy, rounded corners=4pt] (0,0) rectangle (48,43);
  \node[anchor=west, text width=40mm, align=left] at (6,21.5) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} ASSURANCE}\\[1mm]
    {\fontsize{8.8}{10.5}\selectfont\bfseries\color{white} 履约保障\\条件就绪}\\[1.5mm]
    {\fontsize{6}{7.2}\selectfont\color{white!75!gray}Financial \textbullet\ Technical \textbullet\ HSE}
  };

  % 4 Metric Badges
  \foreach \xa/\xb/\val/\title/\sub in {
    53/81/资料/资信文件/受控文件可提供,
    85/113/培训/岗前安全/按岗位要求实施,
    117/145/证书/专业人员/按工作包核验,
    149/181/语言/沟通支持/越语 • 英语 • 中文}{
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
\pageheaderbar{人才培训战略与企业安全文化}{第10页}
\pagefooterbar{第10页}

\begin{tikzpicture}[remember picture, overlay]
  \node[opacity=0.02, scale=2.4, font=\bfseries\sffamily, text=TTCBlue]
    at ([yshift=-12mm]current page.center) {TALENT DEVELOPMENT \& SAFETY CULTURE};
  \draw[TTCBlue!6!white, line width=0.45pt]
    ([xshift=15mm, yshift=20mm]current page.south west)
    grid[step=8mm]
    ([xshift=195mm, yshift=45mm]current page.south west);
\end{tikzpicture}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{人才培养与安全文化建设}{Talent Development, Technical Certification \& Safety-First Culture}

\vspace{1mm}
{\fontsize{14.5}{16.5}\selectfont\bfseries\color{TTCBlue}
实战训战结合 • 国际认证引领 • 驱动高质量项目交付\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
坚持将培训深度扎根于施工一线，将专业技能转化为安全、优质、高效的现场执行力。\par}
\vspace{3.5mm}

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
    {\fontsize{15}{17}\selectfont\bfseries 现场即课堂\\实战铸专才}\\[1.8mm]
    {\fontsize{7}{8.6}\selectfont\color{white!82!gray}
    紧扣实际工况与专业设备实操，全员坚决行使安全隐患“一票停工权”。}
  };
  \node[
    anchor=south east, rounded corners=3pt,
    fill=white, fill opacity=0.94, text opacity=1,
    draw=TTCCyan, line width=0.65pt,
    minimum width=52mm, minimum height=13mm, align=center
  ] at (179,7) {
    {\fontsize{8.2}{9.5}\selectfont\bfseries\color{TTCBlue} SAFETY BEFORE PRODUCTIVITY}\\[0.6mm]
    {\fontsize{6.4}{7.8}\selectfont\color{TTCTextDark}安全生产是一切施工作业不可逾越的前提}
  };
  \draw[white, line width=1pt, rounded corners=3pt] (0.6,0.6) rectangle (185.4,64.4);
  \draw[TTCBorder, line width=0.65pt, rounded corners=3pt] (0,0) rectangle (186,65);
\end{tikzpicture}

\vspace{3.5mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,53);
  \node[anchor=west] at (0,48) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} DEVELOPMENT JOURNEY}\quad
    {\fontsize{9.5}{11}\selectfont\bfseries\color{TTCBlue} 从现场工程师到工程领军人才的晋升发展路径}
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
    {\fontsize{6.5}{7.8}\selectfont 进场前必须完成安全培训}
  };
  \node[align=center, text width=36mm] at (69,13) {
    {\fontsize{8.8}{10}\selectfont\bfseries\color{TTCBlue} TECHNICAL MASTERY}\\[0.7mm]
    {\fontsize{6.5}{7.8}\selectfont BIM • Tekla • MEP • PEB • QA/QC}
  };
  \node[align=center, text width=36mm] at (117,13) {
    {\fontsize{8.8}{10}\selectfont\bfseries\color{TTCBlue} CERTIFIED PRO}\\[0.7mm]
    {\fontsize{6.5}{7.8}\selectfont 二级能力 • AWS D1.1 • PMP • FIDIC}
  };
  \node[align=center, text width=36mm] at (164,13) {
    {\fontsize{8.8}{10}\selectfont\bfseries\color{TTCRed} PROJECT LEADER}\\[0.7mm]
    {\fontsize{6.5}{7.8}\selectfont 指挥、培训并带领项目团队}
  };
\end{tikzpicture}

\vspace{3.5mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,49);
  \fill[white, rounded corners=4pt] (0,0) rectangle (91,49);
  \draw[TTCBorder, line width=0.65pt, rounded corners=4pt] (0,0) rectangle (91,49);
  \node[anchor=north west, text width=79mm, align=left] at (6,43) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCCyan} TTC TECHNICAL ACADEMY}\\[0.8mm]
    {\fontsize{10}{11.5}\selectfont\bfseries\color{TTCBlue} TTC 建筑科技学院}\\[1.5mm]
    {\fontsize{6.8}{8.4}\selectfont\color{TTCTextDark}
    \textcolor{TTCCyan}{\faCheckCircle}\ \textbf{ConTech \& BIM:} Revit, Tekla LOD 400, Navisworks, CDE。\\[0.8mm]
    \textcolor{TTCCyan}{\faCheckCircle}\ \textbf{专项技能：} AWS D1.1、机电消防、高空作业持证培训。\\[0.8mm]
    \textcolor{TTCCyan}{\faCheckCircle}\ \textbf{项目管理：} PMP、FIDIC 合同管理与工程量造价控制。}
  };

  \fill[TTCLightBlue, rounded corners=4pt] (95,0) rectangle (186,49);
  \draw[TTCBorder, line width=0.65pt, rounded corners=4pt] (95,0) rectangle (186,49);
  \node[anchor=north west, text width=79mm, align=left] at (101,43) {
    {\fontsize{7}{8}\selectfont\bfseries\color{TTCRed} SAFETY \& CULTURE SYSTEM}\\[0.8mm]
    {\fontsize{10}{11.5}\selectfont\bfseries\color{TTCBlue} 职业安全与人文关怀体系}\\[1.5mm]
    {\fontsize{6.8}{8.4}\selectfont\color{TTCTextDark}
    \textcolor{TTCRed}{\faCheckCircle}\ 每日工前会 (Toolbox Talk) 与常态化消防救援演练。\\[0.8mm]
    \textcolor{TTCRed}{\faCheckCircle}\ 按规定配置意外保险并实施定期健康检查。\\[0.8mm]
    \textcolor{TTCRed}{\faCheckCircle}\ 透明 KPI 激励体系、清晰晋升通道与停工保护机制。}
  };
\end{tikzpicture}

\vspace{3.5mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,28);
  \fill[white, rounded corners=4pt] (0,0) rectangle (186,28);
  \draw[TTCBorder, line width=0.65pt, rounded corners=4pt] (0,0) rectangle (186,28);
  \foreach \x in {46.5,93,139.5}{
    \draw[TTCBorder, line width=0.5pt] (\x,5) -- (\x,23);
  }
  \node[align=center] at (23.25,14) {
    {\fontsize{13.5}{15}\selectfont\bfseries\color{TTCRed} 定期开展}\\[0.7mm]
    {\fontsize{6.6}{7.8}\selectfont\bfseries 按岗位组织培训}
  };
  \node[align=center] at (69.75,14) {
    {\fontsize{13.5}{15}\selectfont\bfseries\color{TTCBlue} 强制要求}\\[0.7mm]
    {\fontsize{6.6}{7.8}\selectfont\bfseries 有效安全资格}
  };
  \node[align=center] at (116.25,14) {
    {\fontsize{13.5}{15}\selectfont\bfseries\color{TTCCyan} 依法配置}\\[0.7mm]
    {\fontsize{6.6}{7.8}\selectfont\bfseries 保险与健康保障}
  };
  \node[align=center] at (162.75,14) {
    {\fontsize{13.5}{15}\selectfont\bfseries\color{TTCBlue} STOP WORK}\\[0.7mm]
    {\fontsize{6.6}{7.8}\selectfont\bfseries 停工授权机制}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

print("Section 2 (Pages 08-10) Chinese version loaded successfully.")
