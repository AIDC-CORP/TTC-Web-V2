# -*- coding: utf-8 -*-
"""
Section 5: Selected Project Portfolio & 06 Case Studies (Pages 20 - 27) — 简体中文版
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
        {\faBuilding\quad 新成功建筑科技股份公司 \textbullet\ TTC JSC};
      \node[anchor=east,text=TTCCyan,font=\fontsize{7.5}{9}\selectfont\bfseries] at (198,-5)
        {重点工业项目清单 • 01--08};
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
        {第20页};
    \end{tikzpicture}%
  }%
}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{重点工业建筑工程项目清单}{八座代表性工业工程 • 关键参数明晰 • 易于查阅核对}

{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
工程规模 • 建设地点 • TTC 承包履约范围\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
项目清单按统一技术框架编排，便于业主迅速了解 TTC 在各个大型项目中的总包角色与核心贡献。\par}
\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,188);
  \fill[white,rounded corners=3pt] (0,0) rectangle (186,188);
  \draw[TTCBorder,rounded corners=3pt,line width=.7pt] (0,0) rectangle (186,188);

  % 表头
  \fill[TTCDeepNavy,rounded corners=3pt] (0,176) rectangle (186,188);
  \node[text=white,font=\fontsize{6.5}{7.5}\selectfont\bfseries] at (5,182) {序号};
  \node[anchor=west,text=white,font=\fontsize{6.5}{7.5}\selectfont\bfseries] at (14,182) {工程项目 / 投资业主};
  \node[text=white,font=\fontsize{6.5}{7.5}\selectfont\bfseries] at (84,182) {建筑规模};
  \node[anchor=west,text=white,font=\fontsize{6.5}{7.5}\selectfont\bfseries] at (96,182) {建设地点};
  \node[anchor=west,text=white,font=\fontsize{6.5}{7.5}\selectfont\bfseries] at (129,182) {TTC 承包范围};

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

  \projectrowa{165}{01}{鸿庄制砖工厂综合体}{鸿庄股份公司 • 越南}{100,000 m$^2$}{永福省\\立石县}{EPC总承包 • 6.5个月快速交付}{TTCLightBlue}
  \projectrowa{143}{02}{红河第七制衣厂}{红河制衣集团 • 越南}{68,000 m$^2$}{南定省\\海后县}{设计与施工 • 双层重载工业地坪}{white}
  \projectrowa{121}{03}{Japfa Comfeed 饲料厂}{Japfa 集团 • 印度尼西亚}{50,000 m$^2$}{永福省\\太平省}{45米高耸筒仓群 • 精密车间}{TTCLightBlue}
  \projectrowa{99}{04}{正大 CP 饲料生产厂}{正大集团 • 泰国}{35,000 m$^2$}{河南省\\同文工业区}{重载生产车间 • 自动化恒温仓库}{white}
  \projectrowa{77}{05}{大润科技 DAEYUN 厂房}{大润集团 • 韩国}{20,000 m$^2$}{永福省\\霸善二期工业区}{Class 10,000无尘车间 • ESD防静电地坪}{TTCLightBlue}
  \projectrowa{55}{06}{住友电工 SUMIDENSO 线束厂}{住友电工 • 日本}{15,015 m$^2$}{后江省\\后江工业区}{汽车线束厂房 • 国际标准消防与水处理}{white}
  \projectrowa{33}{07}{富士康 FOXCONN 生产车间}{富士康科技集团 • 中国台湾}{12,000 m$^2$}{北宁省\\桂武工业区}{大跨度钢结构 • 高层工业厂房安装}{TTCLightBlue}
  \projectrowa{11}{08}{BW 工业智慧物流仓储}{BW Industrial • 新加坡}{45,000 m$^2$}{北宁省\\安丰工业区}{智慧物流仓储总包 • 超平地坪}{white}
\end{tikzpicture}

\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,35);
  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,35);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.2}{7.2}\selectfont\bfseries]
    at (7,29) {经大型工程检验的核心能力矩阵};
  \foreach \x in {46.5,93,139.5}{\draw[white!25!gray] (\x,5) -- (\x,23);}
  \node[align=center,text width=40mm] at (23.25,14) {
    {\fontsize{8.2}{9.5}\selectfont\bfseries\color{white} EPC / 设计施工一体化}\\[-.2mm]
    {\fontsize{5.9}{7.1}\selectfont\color{white!75!gray}单一责任主体贯穿全程}
  };
  \node[align=center,text width=40mm] at (69.75,14) {
    {\fontsize{8.2}{9.5}\selectfont\bfseries\color{white} 结构与 PEB 制造}\\[-.2mm]
    {\fontsize{5.9}{7.1}\selectfont\color{white!75!gray}大跨度 • 重荷载 • 筒仓}
  };
  \node[align=center,text width=40mm] at (116.25,14) {
    {\fontsize{8.2}{9.5}\selectfont\bfseries\color{white} 特种工业地坪}\\[-.2mm]
    {\fontsize{5.9}{7.1}\selectfont\color{white!75!gray}重载地坪 • 超平地坪}
  };
  \node[align=center,text width=40mm] at (162.75,14) {
    {\fontsize{8.2}{9.5}\selectfont\bfseries\color{white} 机电 MEP / 消防}\\[-.2mm]
    {\fontsize{5.9}{7.1}\selectfont\color{white!75!gray}基于工艺需求深度集成}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_21 = r"""% ============================================================
% TRANG 21: SỔ DANH MỤC DỰ ÁN TIÊU BIỂU 09--16
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\pageheaderbar{重点工业项目清单 • 09--16}{第21页}
\pagefooterbar{第21页}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{国际 FDI 及配套工业代表性项目清单}{八座标杆工程 • 跨国投资企业 • 专业严苛标准}

{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
跨国业主 • 行业领域 • EPC 解决方案\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
全面展示 TTC 在食品加工、精密电子、机械制造、智慧物流及新能源领域的总包实战业绩。\par}
\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,188);
  \fill[white,rounded corners=3pt] (0,0) rectangle (186,188);
  \draw[TTCBorder,rounded corners=3pt,line width=.7pt] (0,0) rectangle (186,188);

  \fill[TTCDeepNavy,rounded corners=3pt] (0,176) rectangle (186,188);
  \node[text=white,font=\fontsize{6.5}{7.5}\selectfont\bfseries] at (5,182) {序号};
  \node[anchor=west,text=white,font=\fontsize{6.5}{7.5}\selectfont\bfseries] at (14,182) {工程项目 / 投资业主};
  \node[text=white,font=\fontsize{6.5}{7.5}\selectfont\bfseries] at (84,182) {建筑规模};
  \node[anchor=west,text=white,font=\fontsize{6.5}{7.5}\selectfont\bfseries] at (96,182) {建设地点};
  \node[anchor=west,text=white,font=\fontsize{6.5}{7.5}\selectfont\bfseries] at (129,182) {TTC 承包范围};

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

  \projectrowb{165}{09}{新希望 NEW HOPE 饲料厂}{新希望六和 • 新加坡/中国}{32,000 m$^2$}{北江省\\光州工业区}{粮食筒仓群 • 22kV变电站及重载道路}{TTCLightBlue}
  \projectrowb{143}{10}{新城 SHINJO 精密机械厂}{Shinjo 精密 • 日本}{18,500 m$^2$}{北宁省\\VSIP 工业区}{精密机加工车间 • 15T行车梁结构}{white}
  \projectrowb{121}{11}{东和田 TOWADA 电子厂}{Towada 电子 • 日本}{16,000 m$^2$}{海阳省\\福田工业区}{芯片精密贴片车间 • ISO无尘室}{TTCLightBlue}
  \projectrowb{99}{12}{东洋制罐 TOYO SEIKAN 厂房}{Toyo Seikan • 日本}{22,000 m$^2$}{北宁省\\仙山工业区}{EPC总承包 • 自动化包装车间 • 超平地坪}{white}
  \projectrowb{77}{13}{花美 FAMI 服饰制造厂}{Fami Garment • 韩国}{28,000 m$^2$}{富寿省\\瑞云工业区}{双层大型制衣厂房 • 工业暖通空调系统}{TTCLightBlue}
  \projectrowb{55}{14}{邮船 YUSEN 国际物流中心}{Yusen Logistics • 日本}{25,000 m$^2$}{海防市\\亭武工业区}{保税立体仓库 • 自动液压升降调节板}{white}
  \projectrowb{33}{15}{味王 A-ONE 食品生产基地}{味王股份 • 中国台湾}{30,000 m$^2$}{平阳省\\神浪二期工业区}{食品洁净加工车间 • HACCP标准系统}{TTCLightBlue}
  \projectrowb{11}{16}{山河 SON HA 新能源装备厂}{山河集团 • 越南}{24,000 m$^2$}{北宁省\\顺成工业区}{大型储罐车间 • 屋顶太阳能光伏系统}{white}
\end{tikzpicture}

\vspace{3mm}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,35);
  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,35);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.2}{7.2}\selectfont\bfseries]
    at (7,29) {精选 6 大经典工程案例深度剖析 • 第 22--27 页};
  \foreach \x in {62,124}{\draw[white!25!gray] (\x,5) -- (\x,23);}
  \node[align=center,text width=53mm] at (31,14) {
    {\fontsize{7.8}{9.2}\selectfont\bfseries\color{white} 鸿庄制砖 • 红河第七制衣}\\[-.2mm]
    {\fontsize{6}{7.2}\selectfont\color{white!75!gray}超大跨度EPC • 双层重载厂房}
  };
  \node[align=center,text width=53mm] at (93,14) {
    {\fontsize{7.8}{9.2}\selectfont\bfseries\color{white} JAPFA 饲料 • 大润科技}\\[-.2mm]
    {\fontsize{6.2}{7.2}\selectfont\color{white!75!gray}工艺装置高耸筒仓 • 无尘洁净室}
  };
  \node[align=center,text width=53mm] at (155,14) {
    {\fontsize{7.8}{9.2}\selectfont\bfseries\color{white} 住友电工 • 富士康}\\[-.2mm]
    {\fontsize{6}{7.2}\selectfont\color{white!75!gray}日系严苛品控 • 电子装配厂房}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_22 = r"""% ============================================================
% TRANG 22: FLAGSHIP CASE -- NHÀ MÁY GẠCH HỒNG TRANG
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{经典案例 • 鸿庄制砖工厂}{第22页}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{经典工程案例 01: 鸿庄制砖工厂综合体}{Flagship EPC case • Large-span industrial facility • Lập Thạch, Vĩnh Phúc}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);

  % 现场实景照片
  \begin{scope}
    \clip[rounded corners=4pt] (0,150) rectangle (70,220);
    \node[inner sep=0pt] at (35,185)
      {\includegraphics[width=70mm,height=70mm]{../../public/project-assets/hongtrang.jpg}};
    \fill[TTCDeepNavy,opacity=.88] (0,150) rectangle (70,161);
    \node[anchor=west,text=white,font=\fontsize{7}{8}\selectfont\bfseries]
      at (4,155.5) {工程实景 • 永福省立石县};
  \end{scope}
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,150) rectangle (70,220);

  % 概况数据
  \fill[TTCLightBlue,rounded corners=4pt] (74,150) rectangle (186,220);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (74,150) rectangle (186,220);
  \node[anchor=north west,text=TTCRed,font=\fontsize{7.5}{9}\selectfont\bfseries]
    at (80,214) {EPC 总承包模式};
  \node[anchor=north west,text width=99mm,align=left,text=TTCBlue,
        font=\fontsize{14}{16}\selectfont\bfseries]
    at (80,207) {100,000 m$^2$ 规划总面积};
  \draw[TTCBorder,line width=.55pt] (80,190) -- (180,190);
  \foreach \x in {113.3,146.6}{\draw[TTCBorder,line width=.5pt] (\x,163) -- (\x,186);}
  \node[align=center,text width=29mm] at (96.5,176) {
    {\fontsize{11}{12}\selectfont\bfseries\color{TTCRed}75,000 m$^2$}\\[-.5mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}车间建筑面积}};
  \node[align=center,text width=29mm] at (130,176) {
    {\fontsize{11}{12}\selectfont\bfseries\color{TTCBlue}跨度 42米}\\[-.5mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}无中柱开敞空间}};
  \node[align=center,text width=29mm] at (163.5,176) {
    {\fontsize{11}{12}\selectfont\bfseries\color{TTCBlue}6.5 个月}\\[-.5mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}快速完工交付}};
  \node[anchor=south west,text width=99mm,align=left,text=TTCTextDark,
        font=\fontsize{7.4}{9}\selectfont]
    at (80,153) {\textbf{TTC承包范围：} EPC总承包；统筹地质勘探、方案设计、PEB制造、重型地坪、机电及Fast-track快速施工。};

  % 案例故事
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (0,143) {核心技术攻坚 • 挑战、方案与成效};

  \fill[white,rounded corners=4pt] (0,79) rectangle (58,137);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,79) rectangle (58,137);
  \fill[TTCRed,rounded corners=2pt] (5,124) rectangle (16,133);
  \node[text=white,font=\fontsize{7}{8}\selectfont\bfseries] at (10.5,128.5) {01};
  \node[anchor=north west,text=TTCBlue,font=\fontsize{9}{10.5}\selectfont\bfseries]
    at (5,120) {技术挑战};
  \node[anchor=north west,text width=48mm,align=left,text=TTCTextDark,
        font=\fontsize{7.2}{9}\selectfont]
    at (5,110) {窑炉连续生产线要求全长无立柱阻隔，柱网跨度达42米；同时超长车间须具备高效自然排烟散热能力。};

  \draw[-{Latex[length=2.5mm]},TTCCyan,line width=1pt] (59.5,108) -- (63,108);
  \fill[TTCDeepNavy,rounded corners=4pt] (64,79) rectangle (122,137);
  \node[text=TTCDeepNavy,fill=white,rounded corners=2pt,font=\fontsize{7}{8}\selectfont\bfseries,
        minimum width=11mm,minimum height=9mm] at (74.5,128.5) {02};
  \node[anchor=north west,text=white,font=\fontsize{9}{10.5}\selectfont\bfseries]
    at (69,120) {TTC 解决方案};
  \node[anchor=north west,text width=48mm,align=left,text=white,
        font=\fontsize{7.2}{9}\selectfont]
    at (69,110) {采用42米变截面高强门式刚架；屋脊设置通长自吸式通风气楼；设计、制造与土建各工序穿插并行。};

  \draw[-{Latex[length=2.5mm]},TTCCyan,line width=1pt] (123.5,108) -- (127,108);
  \fill[TTCLightBlue,rounded corners=4pt] (128,79) rectangle (186,137);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (128,79) rectangle (186,137);
  \fill[TTCBlue,rounded corners=2pt] (133,124) rectangle (144,133);
  \node[text=white,font=\fontsize{7}{8}\selectfont\bfseries] at (138.5,128.5) {03};
  \node[anchor=north west,text=TTCBlue,font=\fontsize{9}{10.5}\selectfont\bfseries]
    at (133,120) {交付成效};
  \node[anchor=north west,text width=48mm,align=left,text=TTCTextDark,
        font=\fontsize{7.2}{9}\selectfont]
    at (133,110) {仅历时6.5个月完成75,000 m$^2$建筑安装，比合同原定节点提前20天高品质交付投产。};

  % 总结记忆
  \fill[white,rounded corners=4pt] (0,20) rectangle (186,70);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,20) rectangle (186,70);
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (7,61) {核心价值亮点总结};
  \draw[TTCBorder] (62,27) -- (62,58);
  \draw[TTCBorder] (124,27) -- (124,58);
  \node[align=center,text width=52mm] at (31,42) {
    {\fontsize{12}{13}\selectfont\bfseries\color{TTCRed}42 米跨度}\\[-.5mm]
    {\fontsize{6.6}{8}\selectfont\color{TTCTextMuted}通畅开阔无中柱生产车间}};
  \node[align=center,text width=52mm] at (93,42) {
    {\fontsize{12}{13}\selectfont\bfseries\color{TTCBlue}并行穿插}\\[-.5mm]
    {\fontsize{6.6}{8}\selectfont\color{TTCTextMuted}设计 • 制造 • 土建协同实施}};
  \node[align=center,text width=52mm] at (155,42) {
    {\fontsize{12}{13}\selectfont\bfseries\color{TTCBlue}提前 20 天}\\[-.5mm]
    {\fontsize{6.6}{8}\selectfont\color{TTCTextMuted}助力业主抢占市场投产先机}};

  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,14);
  \node[anchor=west,text=white,font=\fontsize{7.4}{9}\selectfont\bfseries]
    at (7,7) {核心价值：超大开敞生产空间 • 严格受控的高速履约};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_23 = r"""% ============================================================
% TRANG 23: ENGINEERING CASE -- NHÀ MÁY MAY SÔNG HỒNG 7
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{工程结构方案 • 红河第七制衣厂}{第23页}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{经典工程案例 02: 红河第七制衣厂}{Engineering anatomy • Two-storey heavy-duty factory • Hải Hậu, Nam Định}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);

  % 实景
  \begin{scope}
    \clip[rounded corners=4pt] (0,148) rectangle (104,220);
    \node[inner sep=0pt] at (52,184)
      {\includegraphics[width=104mm,height=77.5mm]{../../public/project-assets/songhong7.jpg}};
    \fill[TTCDeepNavy,opacity=.88] (0,148) rectangle (104,160);
    \node[anchor=west,text=white,font=\fontsize{7}{8}\selectfont\bfseries]
      at (4,154) {实景效果 • 南定省海后县};
  \end{scope}
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,148) rectangle (104,220);

  \fill[TTCDeepNavy,rounded corners=4pt] (108,148) rectangle (186,220);
  \node[anchor=north west,text=TTCCyan,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (114,214) {项目核心参数};
  \node[anchor=north west,text=white,font=\fontsize{15}{16}\selectfont\bfseries]
    at (114,205) {68,000 m$^2$};
  \node[anchor=north west,text=white!75!gray,font=\fontsize{6.5}{8}\selectfont]
    at (114,190) {总建筑面积};
  \draw[white!25!gray] (114,183) -- (180,183);
  \node[anchor=north west,text width=62mm,align=left,text=white,
        font=\fontsize{7.2}{9}\selectfont]
    at (114,178) {\textbf{建筑形式：} 双层重型钢结构工业厂房\\[1mm]
                  \textbf{楼面荷载：} 1,200 kg/m$^2$ (重载设计)\\[1mm]
                  \textbf{建设工期：} 180 天完工\\[1mm]
                  \textbf{承包范围：} 方案深化设计与施工总承包};

  % 结构剖面原理图
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (0,140) {结构受力与减振剖面原理图};
  \fill[TTCLightBlue,rounded corners=4pt] (0,53) rectangle (186,134);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,53) rectangle (186,134);

  % 框架示意
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
    at (16,112) {二层密集成组设备动荷载};
  \draw[TTCCyan,line width=1.2pt,dashed] (17,87) -- (127,87);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.3}{7.5}\selectfont\bfseries]
    at (19,82) {楼板下部预留机电/暖通管道夹层};
  \draw[<->,>=Latex,TTCBlue,line width=.8pt] (16,60) -- (128,60);
  \node[fill=TTCLightBlue,text=TTCBlue,font=\fontsize{6.5}{8}\selectfont\bfseries]
    at (72,60) {双层开阔高效生产作业面};

  % 右侧设计要点
  \draw[TTCBorder] (138,60) -- (138,127);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (145,124) {三大关键设计决策};
  \node[anchor=north west,text width=34mm,align=left,text=TTCTextDark,
        font=\fontsize{6.7}{8.3}\selectfont]
    at (145,114) {\textbf{01 • 组合楼板}\newline
                  压型钢板组合楼板浇筑混凝土，承载 1.2 吨/m$^2$。};
  \node[anchor=north west,text width=34mm,align=left,text=TTCTextDark,
        font=\fontsize{6.7}{8.3}\selectfont]
    at (145,92) {\textbf{02 • 减振控制}\newline
                  合理布置次梁与刚性支撑，有效吸收设备微振动。};
  \node[anchor=north west,text width=34mm,align=left,text=TTCTextDark,
        font=\fontsize{6.7}{8.3}\selectfont]
    at (145,70) {\textbf{03 • 综合管线}\newline
                  预留机电与暖通管线空间，保证一层净高与美观。};

  % 总结卡片
  \fill[white,rounded corners=3pt] (0,9) rectangle (58,45);
  \draw[TTCBorder,rounded corners=3pt] (0,9) rectangle (58,45);
  \node[anchor=north west,text=TTCRed,font=\fontsize{8}{9}\selectfont\bfseries]
    at (5,39) {01 • 超重荷载};
  \node[anchor=north west,text width=48mm,text=TTCTextDark,font=\fontsize{6.8}{8.4}\selectfont]
    at (5,30) {二层高标准承载设计，满足成套自动化缝纫机组安全运转。};

  \fill[white,rounded corners=3pt] (64,9) rectangle (122,45);
  \draw[TTCBorder,rounded corners=3pt] (64,9) rectangle (122,45);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9}\selectfont\bfseries]
    at (69,39) {02 • 专业协同};
  \node[anchor=north west,text width=48mm,text=TTCTextDark,font=\fontsize{6.8}{8.4}\selectfont]
    at (69,30) {结构预留洞口与MEP管线在BIM中100\%对齐，零现场开凿。};

  \fill[white,rounded corners=3pt] (128,9) rectangle (186,45);
  \draw[TTCBorder,rounded corners=3pt] (128,9) rectangle (186,45);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9}\selectfont\bfseries]
    at (133,39) {03 • 高效节拍};
  \node[anchor=north west,text width=48mm,text=TTCTextDark,font=\fontsize{6.8}{8.4}\selectfont]
    at (133,30) {钢构安装、楼板浇筑与机电安装流水作业，180天竣工。};

  \fill[TTCDeepNavy,rounded corners=2pt] (0,0) rectangle (186,6);
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_24 = r"""% ============================================================
% TRANG 24: PROCESS CASE -- TỔ HỢP JAPFA COMFEED
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{工业工艺装置 • JAPFA COMFEED 饲料厂}{第24页}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{经典工程案例 03: JAPFA COMFEED 饲料生产基地}{Process-industry case • High-rise silo • Dynamic-load and dust control}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);

  % 照片与指标
  \begin{scope}
    \clip[rounded corners=4pt] (0,151) rectangle (68,219);
    \node[inner sep=0pt] at (34,185)
      {\includegraphics[width=68mm,height=68mm]{../../public/project-assets/japfa.jpg}};
    \fill[TTCDeepNavy,opacity=.9] (0,151) rectangle (68,162);
    \node[anchor=west,text=white,font=\fontsize{7}{8}\selectfont\bfseries]
      at (4,156.5) {实景 • JAPFA COMFEED};
  \end{scope}
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,151) rectangle (68,219);

  \fill[TTCLightBlue,rounded corners=4pt] (72,151) rectangle (186,219);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (72,151) rectangle (186,219);
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (78,211) {永福省 / 太平省 基地项目};
  \draw[TTCBorder] (129,158) -- (129,204);
  \draw[TTCBorder] (78,181) -- (180,181);
  \node[align=center,text width=45mm] at (103.5,193) {
    {\fontsize{12}{13}\selectfont\bfseries\color{TTCRed}50,000 m$^2$}\\[-.5mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}规划总用地}};
  \node[align=center,text width=45mm] at (154.5,193) {
    {\fontsize{12}{13}\selectfont\bfseries\color{TTCBlue}筒仓高 45米}\\[-.5mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}高耸塔架群}};
  \node[align=center,text width=45mm] at (103.5,169) {
    {\fontsize{12}{13}\selectfont\bfseries\color{TTCBlue}2,800 吨}\\[-.5mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}PEB 钢结构总量}};
  \node[align=center,text width=45mm] at (154.5,169) {
    {\fontsize{12}{13}\selectfont\bfseries\color{TTCBlue}165 天}\\[-.5mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}施工安装工期}};

  % 筒仓示意
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (0,143) {工程攻坚故事 • 从深桩动荷载基础到45米高空筒仓};
  \fill[TTCLightBlue,rounded corners=4pt] (0,56) rectangle (54,137);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,56) rectangle (54,137);

  \fill[TTCBlue!10!white] (19,69) rectangle (42,123);
  \draw[TTCBlue,line width=1.1pt] (19,69) rectangle (42,123);
  \foreach \y in {80,91,102,113}{\draw[TTCBorder] (19,\y) -- (42,\y);}
  \draw[TTCBlue,line width=1.1pt] (16,69) -- (45,69);
  \fill[TTCDeepNavy] (12,62) rectangle (49,69);
  \draw[<->,>=Latex,TTCRed,line width=.9pt] (9,69) -- (9,123);
  \node[rotate=90,text=TTCRed,font=\fontsize{9}{10}\selectfont\bfseries]
    at (4,96) {45 米高度};
  \node[text=TTCBlue,font=\fontsize{6.5}{7.5}\selectfont\bfseries]
    at (30.5,129) {筒仓塔架群};
  \node[text=white,font=\fontsize{6.2}{7.2}\selectfont\bfseries]
    at (30.5,65.5) {D800 灌注桩};

  % 三大应对措施
  \fill[white,rounded corners=3pt] (60,108) rectangle (186,137);
  \draw[TTCBorder,rounded corners=3pt] (60,108) rectangle (186,137);
  \fill[TTCRed] (60,108) rectangle (63,137);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9}\selectfont\bfseries]
    at (69,132) {01 • 粉碎机组动荷载减振};
  \node[anchor=north west,text width=108mm,text=TTCTextDark,font=\fontsize{6.9}{8.4}\selectfont]
    at (69,122) {采用 D800 深孔灌注桩基础与阻尼隔振垫层，精准吸收重型旋转机械动力冲击波。};

  \fill[white,rounded corners=3pt] (60,76) rectangle (186,105);
  \draw[TTCBorder,rounded corners=3pt] (60,76) rectangle (186,105);
  \fill[TTCBlue] (60,76) rectangle (63,105);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9}\selectfont\bfseries]
    at (69,100) {02 • 45米高空分段精准吊装};
  \node[anchor=north west,text width=108mm,text=TTCTextDark,font=\fontsize{6.9}{8.4}\selectfont]
    at (69,90) {塔架结构分段预拼装，激光测距仪全程监控垂直度与法兰平整度，误差控制在 2mm 内。};

  \fill[white,rounded corners=3pt] (60,44) rectangle (186,73);
  \draw[TTCBorder,rounded corners=3pt] (60,44) rectangle (186,73);
  \fill[TTCBlue] (60,44) rectangle (63,73);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9}\selectfont\bfseries]
    at (69,68) {03 • 粉尘防爆与消防安全};
  \node[anchor=north west,text width=108mm,text=TTCTextDark,font=\fontsize{6.9}{8.4}\selectfont]
    at (69,58) {全面集成旋风除尘、负压通风及泄爆阀门装置，达到粮食饲料行业严苛的防爆安全标准。};

  % 实施范围
  \fill[TTCDeepNavy,rounded corners=4pt] (0,0) rectangle (186,35);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.5}{8}\selectfont\bfseries]
    at (7,28) {TTC 实施范围};
  \foreach \x in {46.5,93,139.5}{\draw[white!25!gray] (\x,6) -- (\x,25);}
  \node[align=center,text width=39mm,text=white,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (23.25,15) {深桩基础工程\\[-.5mm]{\fontsize{5.8}{7}\selectfont\color{white!70!gray}静载+动载复合验算}};
  \node[align=center,text width=39mm,text=white,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (69.75,15) {PEB 钢结构制造\\[-.5mm]{\fontsize{5.8}{7}\selectfont\color{white!70!gray}高耸塔架精密加工}};
  \node[align=center,text width=39mm,text=white,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (116.25,15) {筒仓高空安装\\[-.5mm]{\fontsize{5.8}{7}\selectfont\color{white!70!gray}高精度垂直度控制}};
  \node[align=center,text width=39mm,text=white,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (162.75,15) {工艺配套系统\\[-.5mm]{\fontsize{5.8}{7}\selectfont\color{white!70!gray}防爆 • 除尘 • 变配电}};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_25 = r"""% ============================================================
% TRANG 25: CLEANROOM CASE -- DAEYUN ST VINA
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{高等级无尘车间 • 大润科技 DAEYUN ST VINA}{第25页}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{经典工程案例 04: 大润科技 DAEYUN ST VINA 厂房}{Integrated cleanroom systems • KCN Bá Thiện 2, Vĩnh Phúc}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);

  % 实景
  \begin{scope}
    \clip[rounded corners=4pt] (0,157) rectangle (118,219);
    \node[inner sep=0pt] at (59,188)
      {\includegraphics[width=118mm]{../../public/project-assets/daeyun.jpg}};
    \fill[TTCDeepNavy,opacity=.88] (0,157) rectangle (118,168);
    \node[anchor=west,text=white,font=\fontsize{7}{8}\selectfont\bfseries]
      at (4,162.5) {工程实景 • 永福省霸善二期工业区};
  \end{scope}
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,157) rectangle (118,219);

  \fill[TTCDeepNavy,rounded corners=4pt] (122,157) rectangle (186,219);
  \node[anchor=north west,text=TTCCyan,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (128,213) {工程基本信息};
  \node[anchor=north west,text=white,font=\fontsize{13}{14}\selectfont\bfseries]
    at (128,203) {20,000 m$^2$};
  \node[anchor=north west,text=white!70!gray,font=\fontsize{6}{7.2}\selectfont]
    at (128,190) {洁净车间面积};
  \draw[white!25!gray] (128,184) -- (180,184);
  \node[anchor=north west,text width=48mm,align=left,text=white,
        font=\fontsize{6.8}{8.4}\selectfont]
    at (128,180) {\textbf{洁净等级：} Class 10,000\\
                  \textbf{特殊要求：} ESD 防静电\\
                  \textbf{建设工期：} 140 天};

  % 系统图
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (0,149) {四大子系统高度集成 • 确保洁净度稳定达标};
  \fill[TTCLightBlue,rounded corners=4pt] (0,57) rectangle (186,143);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,57) rectangle (186,143);

  % 核心区
  \fill[TTCDeepNavy,rounded corners=4pt] (68,88) rectangle (118,116);
  \node[align=center,text=white,text width=42mm,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (93,102) {核心洁净生产区\\[-.5mm]
    {\fontsize{6}{7.2}\selectfont\color{white!70!gray}恒温恒湿 • 密闭 • 防静电}};

  % 四个外围模块
  \fill[white,rounded corners=3pt] (7,108) rectangle (58,136);
  \draw[TTCBorder,rounded corners=3pt] (7,108) rectangle (58,136);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{7.5}{8.5}\selectfont\bfseries]
    at (12,131) {01 • 洁净密闭围护};
  \node[anchor=north west,text width=41mm,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont]
    at (12,121) {高精度气密彩钢夹芯板与吊顶系统，确保正压梯度与无尘环境。};

  \fill[white,rounded corners=3pt] (128,108) rectangle (179,136);
  \draw[TTCBorder,rounded corners=3pt] (128,108) rectangle (179,136);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{7.5}{8.5}\selectfont\bfseries]
    at (133,131) {02 • AHU / HEPA 空调};
  \node[anchor=north west,text width=41mm,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont]
    at (133,121) {初中高效三级过滤送风与高效回风系统，精确控制换气次数。};

  \fill[white,rounded corners=3pt] (7,64) rectangle (58,92);
  \draw[TTCBorder,rounded corners=3pt] (7,64) rectangle (58,92);
  \node[anchor=north west,text=TTCRed,font=\fontsize{7.5}{8.5}\selectfont\bfseries]
    at (12,87) {03 • 精密温湿度控制};
  \node[anchor=north west,text width=41mm,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont]
    at (12,77) {温度 $\pm1^\circ$C、湿度 $\pm5\%$ 恒定控制，满足精密贴片工艺。};

  \fill[white,rounded corners=3pt] (128,64) rectangle (179,92);
  \draw[TTCBorder,rounded corners=3pt] (128,64) rectangle (179,92);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{7.5}{8.5}\selectfont\bfseries]
    at (133,87) {04 • ESD 防静电地坪};
  \node[anchor=north west,text width=41mm,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont]
    at (133,77) {导静电 PVC 地板与接地铜网系统，彻底杜绝静电对元器件损伤。};

  \draw[-{Latex[length=2mm]},TTCCyan,line width=.9pt] (58,122) -- (68,108);
  \draw[-{Latex[length=2mm]},TTCCyan,line width=.9pt] (128,122) -- (118,108);
  \draw[-{Latex[length=2mm]},TTCCyan,line width=.9pt] (58,78) -- (68,94);
  \draw[-{Latex[length=2mm]},TTCCyan,line width=.9pt] (128,78) -- (118,94);

  % 总结
  \fill[white,rounded corners=3pt] (0,10) rectangle (58,48);
  \draw[TTCBorder,rounded corners=3pt] (0,10) rectangle (58,48);
  \node[align=center,text width=48mm] at (29,29) {
    {\fontsize{10}{11}\selectfont\bfseries\color{TTCRed}Class 10,000}\\[-.5mm]
    {\fontsize{6.4}{7.6}\selectfont\color{TTCTextMuted}万级无尘车间标准}};

  \fill[white,rounded corners=3pt] (64,10) rectangle (122,48);
  \draw[TTCBorder,rounded corners=3pt] (64,10) rectangle (122,48);
  \node[align=center,text width=48mm] at (93,29) {
    {\fontsize{10}{11}\selectfont\bfseries\color{TTCBlue}ESD 防静电}\\[-.5mm]
    {\fontsize{6.4}{7.6}\selectfont\color{TTCTextMuted}电子元器件全方位保护}};

  \fill[white,rounded corners=3pt] (128,10) rectangle (186,48);
  \draw[TTCBorder,rounded corners=3pt] (128,10) rectangle (186,48);
  \node[align=center,text width=48mm] at (157,29) {
    {\fontsize{10}{11}\selectfont\bfseries\color{TTCBlue}140 天完工}\\[-.5mm]
    {\fontsize{6.4}{7.6}\selectfont\color{TTCTextMuted}高效准时履约交付}};

  \fill[TTCDeepNavy,rounded corners=2pt] (0,0) rectangle (186,6);
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_26 = r"""% ============================================================
% TRANG 26: QUALITY DELIVERY -- SUMIDENSO VINA
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{高品质履约交付 • 住友电工 SUMIDENSO}{第26页}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{经典工程案例 05: 住友电工 SUMIDENSO 汽车线束工厂}{Quality-led delivery • Automotive wire harness plant • KCN Sông Hậu, Hậu Giang}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);

  % 厂区照片与概况
  \begin{scope}
    \clip[rounded corners=4pt] (0,155) rectangle (64,219);
    \node[inner sep=0pt] at (32,187)
      {\includegraphics[width=64mm,height=64mm]{../../public/project-assets/sumidenso.jpg}};
    \fill[TTCDeepNavy,opacity=.88] (0,155) rectangle (64,166);
    \node[anchor=west,text=white,font=\fontsize{6.8}{8}\selectfont\bfseries]
      at (4,160.5) {厂区厂房实景};
  \end{scope}
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,155) rectangle (64,219);

  \fill[TTCLightBlue,rounded corners=4pt] (68,155) rectangle (186,219);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (68,155) rectangle (186,219);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (75,212) {项目档案概览};
  \node[anchor=north west,text width=48mm,text=TTCTextDark,font=\fontsize{7.1}{8.8}\selectfont]
    at (75,201) {\textbf{投资业主：} 住友电工 (Sumitomo)\\
                  \textbf{建筑面积：} 15,015 m$^2$\\
                  \textbf{建设工期：} 150 天};
  \draw[TTCBorder] (129,161) -- (129,208);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (136,212) {重点交付保障};
  \node[anchor=north west,text width=43mm,text=TTCTextDark,font=\fontsize{6.9}{8.5}\selectfont]
    at (136,201) {\textbullet\quad 快速响应式自动喷淋系统\\[1mm]
                  \textbullet\quad 达标工业污水处理站\\[1mm]
                  \textbullet\quad 日企严苛的验收归档管理};

  % 四道质量关口
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (0,147) {日系精细化 4 级质量控制关口};
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
    {\fontsize{7.3}{8.5}\selectfont\bfseries\color{TTCBlue}进场材料检验}\\[-.3mm]
    {\fontsize{5.9}{7.1}\selectfont\color{TTCTextMuted}CO/CQ • 封样比对 • 批次溯源}};
  \node[align=center,text width=38mm] at (69,101) {
    {\fontsize{7.3}{8.5}\selectfont\bfseries\color{TTCBlue}过程 ITP 检验}\\[-.3mm]
    {\fontsize{5.9}{7.1}\selectfont\color{TTCTextMuted}见证点 • 停止点 • 逐项验收}};
  \node[align=center,text width=38mm] at (117,101) {
    {\fontsize{7.3}{8.5}\selectfont\bfseries\color{TTCBlue}系统联合调试}\\[-.3mm]
    {\fontsize{5.9}{7.1}\selectfont\color{TTCTextMuted}消防联动 • 污水达标 • 试运转}};
  \node[align=center,text width=38mm] at (163,101) {
    {\fontsize{7.3}{8.5}\selectfont\bfseries\color{TTCBlue}档案移交培训}\\[-.3mm]
    {\fontsize{5.9}{7.1}\selectfont\color{TTCTextMuted}竣工图 • 操作手册 • 维保培训}};

  % 表格
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (0,80) {技术需求、质量控制点与交付凭证对照表};
  \fill[TTCDeepNavy,rounded corners=3pt] (0,62) rectangle (186,75);
  \node[anchor=west,text=white,font=\fontsize{6.5}{7.8}\selectfont\bfseries] at (6,68.5) {工程分项};
  \node[anchor=west,text=white,font=\fontsize{6.5}{7.8}\selectfont\bfseries] at (55,68.5) {关键控制节点};
  \node[anchor=west,text=white,font=\fontsize{6.5}{7.8}\selectfont\bfseries] at (126,68.5) {移交凭据与报告};

  \fill[TTCLightBlue] (0,47) rectangle (186,62);
  \fill[white] (0,32) rectangle (186,47);
  \fill[TTCLightBlue] (0,17) rectangle (186,32);
  \draw[TTCBorder] (49,17) -- (49,75);
  \draw[TTCBorder] (120,17) -- (120,75);
  \foreach \y in {17,32,47,62}{\draw[TTCBorder] (0,\y) -- (186,\y);}
  \node[anchor=west,text=TTCBlue,font=\fontsize{6.6}{8}\selectfont\bfseries] at (6,54.5) {消防喷淋系统};
  \node[anchor=west,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont] at (55,54.5) {压力试验 • 水流量 • 联动报警};
  \node[anchor=west,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont] at (126,54.5) {消防局官方验收合格批文};
  \node[anchor=west,text=TTCBlue,font=\fontsize{6.6}{8}\selectfont\bfseries] at (6,39.5) {污水处理系统};
  \node[anchor=west,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont] at (55,39.5) {试运行出水水质检测};
  \node[anchor=west,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont] at (126,39.5) {QCVN 40 A级第三方水质报告};
  \node[anchor=west,text=TTCBlue,font=\fontsize{6.6}{8}\selectfont\bfseries] at (6,24.5) {装饰装修工程};
  \node[anchor=west,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont] at (55,24.5) {平整度 • 收口细节 • 深度清洁};
  \node[anchor=west,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont] at (126,24.5) {Punch List 缺陷清零签署单};

  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,11);
  \node[anchor=west,text=white,font=\fontsize{7}{8.5}\selectfont\bfseries]
    at (7,5.5) {15,015 m$^2$};
  \node[text=white!35!gray] at (49,5.5) {|};
  \node[anchor=west,text=white,font=\fontsize{7}{8.5}\selectfont\bfseries]
    at (57,5.5) {150 天交付};
  \node[text=white!35!gray] at (95,5.5) {|};
  \node[anchor=west,text=white,font=\fontsize{7}{8.5}\selectfont\bfseries]
    at (103,5.5) {消防与污水处理系统一次性通过日方验收};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_27 = r"""% ============================================================
% TRANG 27: PROJECT SPOTLIGHT -- XƯỞNG SẢN XUẤT FOXCONN
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{高精密电子厂房 • 富士康 FOXCONN}{第27页}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{经典工程案例 06: 富士康 FOXCONN 生产车间}{Electronics manufacturing facility • KCN Quế Võ, Bắc Ninh}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);

  % 实景
  \begin{scope}
    \clip[rounded corners=4pt] (0,151) rectangle (186,219);
    \node[inner sep=0pt] at (93,185)
      {\includegraphics[width=186mm]{../../public/project-assets/foxcon.png}};
    \fill[TTCDeepNavy,opacity=.9] (0,151) rectangle (78,168);
    \node[anchor=west,text=white,font=\fontsize{7}{8}\selectfont\bfseries]
      at (5,159.5) {工程实景 • 北宁省桂武工业区};
    \fill[TTCDeepNavy,opacity=.92] (127,151) rectangle (186,219);
    \node[anchor=north west,text=TTCCyan,font=\fontsize{6.8}{8}\selectfont\bfseries]
      at (133,212) {项目档案概览};
    \node[anchor=north west,text=white,font=\fontsize{14}{15}\selectfont\bfseries]
      at (133,201) {12,000 m$^2$};
    \node[anchor=north west,text=white!70!gray,font=\fontsize{6}{7.2}\selectfont]
      at (133,187) {车间建筑面积};
    \draw[white!25!gray] (133,181) -- (180,181);
    \node[anchor=north west,text width=43mm,text=white,font=\fontsize{6.5}{8}\selectfont]
      at (133,177) {\textbf{投资业主：} 富士康 (Foxconn)\\
                    \textbf{企业背景：} 中国台湾知名跨国集团\\
                    \textbf{承包范围：} 钢结构制造与高空安装};
  \end{scope}
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,151) rectangle (186,219);

  % 施工流
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (0,143) {安装前锁定关键技术接口 • 分区流水高效推进};
  \fill[TTCLightBlue,rounded corners=4pt] (0,68) rectangle (186,137);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,68) rectangle (186,137);

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
    at (9,115) {设计模型\\接口锁定};
  \node[anchor=north west,text width=29mm,align=left,text=TTCTextMuted,
        font=\fontsize{6.1}{7.4}\selectfont]
    at (9,96) {锁定轴线标高及钢结构与MEP接口。};

  \fill[TTCBlue] (56,122) circle (3.5mm);
  \node[text=white,font=\fontsize{6}{7}\selectfont\bfseries] at (56,122) {02};
  \node[anchor=north west,text width=29mm,align=left,text=TTCBlue,
        font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (55,115) {工厂预制\\精密加工};
  \node[anchor=north west,text width=29mm,align=left,text=TTCTextMuted,
        font=\fontsize{6.1}{7.4}\selectfont]
    at (55,96) {数控下料与驻厂QC严控构件精度。};

  \fill[TTCBlue] (102,122) circle (3.5mm);
  \node[text=white,font=\fontsize{6}{7}\selectfont\bfseries] at (102,122) {03};
  \node[anchor=north west,text width=29mm,align=left,text=TTCBlue,
        font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (101,115) {分区流水\\安全吊装};
  \node[anchor=north west,text width=29mm,align=left,text=TTCTextMuted,
        font=\fontsize{6.1}{7.4}\selectfont]
    at (101,96) {形成稳定空间刚度单元，流水推进。};

  \fill[TTCBlue] (148,122) circle (3.5mm);
  \node[text=white,font=\fontsize{6}{7}\selectfont\bfseries] at (148,122) {04};
  \node[anchor=north west,text width=29mm,align=left,text=TTCBlue,
        font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (147,115) {工序交接\\验收放行};
  \node[anchor=north west,text width=29mm,align=left,text=TTCTextMuted,
        font=\fontsize{6.1}{7.4}\selectfont]
    at (147,96) {几何尺寸与高强螺栓终拧100\%复验。};

  % 两大核心要点
  \fill[white,rounded corners=4pt] (0,19) rectangle (90,60);
  \draw[TTCBorder,rounded corners=4pt] (0,19) rectangle (90,60);
  \node[anchor=north west,text=TTCRed,font=\fontsize{8}{9}\selectfont\bfseries]
    at (6,54) {项目核心难点};
  \node[anchor=north west,text width=77mm,align=left,text=TTCTextDark,
        font=\fontsize{6.9}{8.5}\selectfont]
    at (6,44) {电子厂房空间开阔、机电管网密集，且要求施工吊装绝不能干扰毗邻既有车间的正常生产运作。};

  \fill[TTCLightBlue,rounded corners=4pt] (96,19) rectangle (186,60);
  \draw[TTCBorder,rounded corners=4pt] (96,19) rectangle (186,60);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (102,54) {TTC 实施策略};
  \node[anchor=north west,text width=77mm,align=left,text=TTCTextDark,
        font=\fontsize{6.9}{8.5}\selectfont]
    at (102,44) {采用模块化分区施工方案，后方基地精确预制，现场夜间错峰吊装并逐段移交安装作业面。};

  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,12);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.2}{7.4}\selectfont\bfseries]
    at (7,6) {实施原则};
  \draw[white!28!gray] (47,3) -- (47,9);
  \node[anchor=west,text=white,font=\fontsize{7}{8.5}\selectfont\bfseries]
    at (54,6) {锁定技术接口 → 分区流水作业 → 严密工序验收};
\end{tikzpicture}
\end{minipage}
\newpage
"""

print("Section 5 (Pages 20-27) Chinese version loaded successfully.")
