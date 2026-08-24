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
\secbrand{重点工业建筑工程项目清单}{八座代表性工程 • 信息精炼 • 便于核验}

{\fontsize{15}{17}\selectfont\bfseries\color{TTCBlue}
工程规模 • 建设地点 • TTC 承包履约范围\par}
\vspace{1mm}
{\fontsize{7.5}{9}\selectfont\color{TTCTextMuted}
项目清单按统一框架编排，便于读者快速了解新成功建筑科技股份公司在各项目中的实施角色与工作范围。\par}
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

  \projectrowa{165}{01}{2M 科技模具制造厂}{2M Technocom • 越南}{模具与工程塑料}{兴安省\\安美二期工业区}{设计咨询与施工总承包}{TTCLightBlue}
  \projectrowa{143}{02}{ALO 越南涂料制造厂}{ALO Paint • 越南}{涂料与化工}{河内市\\富义工业区}{EPC总承包 • 厂房与化学品仓库}{white}
  \projectrowa{121}{03}{Sendai 塑料制造厂}{Sendai Plastics • 越南}{工程塑料}{兴安省\\恩施县}{施工总承包 • 两座厂房与办公楼}{TTCLightBlue}
  \projectrowa{99}{04}{老街制衣厂综合体}{Lao Cai Garment • 越南}{多层制衣厂房}{老街市\\铺买区}{建筑设计与整体施工}{white}
  \projectrowa{77}{05}{DHL 塑料制造厂}{DHL Plastics Group • 越南}{包装与塑料薄膜}{河南省\\太河工业区}{施工总承包 • 厂房与办公楼}{TTCLightBlue}
  \projectrowa{55}{06}{广盛铝型材制造厂}{Quang Thinh Aluminium • 越南}{铝挤压型材}{北宁省\\顺成市}{施工总承包 • 钢结构厂房与办公楼}{white}
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
\secbrand{国际及配套工业代表性项目清单}{八座后续工程 • 跨国投资业主 • 专业化要求}

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

  \projectrowb{165}{09}{Towada 电子制造厂}{Towada • 日本}{18,500 m$^2$}{海阳省\\福田工业区}{电子装配车间 • 机电系统}{TTCLightBlue}
  \projectrowb{143}{10}{Yusen 冷链物流仓库}{Yusen • 日本}{22,000 m$^2$}{海防市\\亭武工业区}{低温仓库 • 自动装卸口}{white}
  \projectrowb{121}{11}{Shinjo Vina 电缆厂}{Shinjo • 韩国}{14,000 m$^2$}{永福省\\霸善二期工业区}{电缆生产车间 • 大跨度钢结构}{TTCLightBlue}
  \projectrowb{99}{12}{东洋制罐 TOYO SEIKAN 厂房}{Toyo Seikan • 日本}{22,000 m$^2$}{北宁省\\仙山工业区}{EPC总承包 • 自动化包装车间 • 超平地坪}{white}
  \projectrowb{77}{13}{前锋塑料制造厂}{Tien Phong Plastics • 越南}{18,000 m$^2$}{海防市\\安阳县}{塑料管挤出车间 • 地坪按设计荷载实施}{TTCLightBlue}
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
    {\fontsize{7.8}{9.2}\selectfont\bfseries\color{white} 2M 科技 • ALO 涂料}\\[-.2mm]
    {\fontsize{6}{7.2}\selectfont\color{white!75!gray}精密模具 • 涂料与化工厂房}
  };
  \node[align=center,text width=53mm] at (93,14) {
    {\fontsize{7.8}{9.2}\selectfont\bfseries\color{white} SENDAI • 老街制衣}\\[-.2mm]
    {\fontsize{6.2}{7.2}\selectfont\color{white!75!gray}工程塑料 • 多层制衣厂房}
  };
  \node[align=center,text width=53mm] at (155,14) {
    {\fontsize{7.8}{9.2}\selectfont\bfseries\color{white} DHL 塑料 • 广盛铝业}\\[-.2mm]
    {\fontsize{6}{7.2}\selectfont\color{white!75!gray}塑料薄膜包装 • 铝挤压型材}
  };
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_22 = r"""% ============================================================
% TRANG 22: PROJECT CASE -- NHÀ MÁY CÔNG NGHỆ 2M
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{代表性项目 • 2M 科技模具制造厂}{第22页}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{项目案例 01：2M 越南模具制造厂}{Precision mold \& parts facility • Yên Mỹ II Industrial Park, Hưng Yên}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);

  % 现场实景照片
  \begin{scope}
    \clip[rounded corners=4pt] (0,150) rectangle (70,220);
    \node[inner sep=0pt] at (35,185)
      {\includegraphics[width=70mm,height=70mm]{../../public/project-assets/2m1.jpg}};
    \node[inner sep=0pt,draw=white,line width=1.1pt] at (52,185)
      {\includegraphics[width=31mm,height=21mm]{../../public/project-assets/2m5.jpg}};
    \fill[TTCDeepNavy,opacity=.88] (0,150) rectangle (70,161);
    \node[anchor=west,text=white,font=\fontsize{7}{8}\selectfont\bfseries]
      at (4,155.5) {概念效果与现场实景 • 兴安省安美二期工业区};
  \end{scope}
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,150) rectangle (70,220);

  % 概况数据
  \fill[TTCLightBlue,rounded corners=4pt] (74,150) rectangle (186,220);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (74,150) rectangle (186,220);
  \node[anchor=north west,text=TTCRed,font=\fontsize{7.5}{9}\selectfont\bfseries]
    at (80,214) {设计与施工协同};
  \node[anchor=north west,text width=99mm,align=left,text=TTCBlue,
        font=\fontsize{14}{16}\selectfont\bfseries]
    at (80,207) {精密模具与工程零部件生产设施};
  \draw[TTCBorder,line width=.55pt] (80,190) -- (180,190);
  \foreach \x in {113.3,146.6}{\draw[TTCBorder,line width=.5pt] (\x,163) -- (\x,186);}
  \node[align=center,text width=29mm] at (96.5,176) {
    {\fontsize{9}{10}\selectfont\bfseries\color{TTCRed}业主}\\[-.5mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}2M Technocom}};
  \node[align=center,text width=29mm] at (130,176) {
    {\fontsize{9}{10}\selectfont\bfseries\color{TTCBlue}地点}\\[-.5mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}兴安省安美二期}};
  \node[align=center,text width=29mm] at (163.5,176) {
    {\fontsize{9}{10}\selectfont\bfseries\color{TTCBlue}范围}\\[-.5mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}设计咨询与施工}};
  \node[anchor=south west,text width=99mm,align=left,text=TTCTextDark,
        font=\fontsize{7.4}{9}\selectfont]
    at (80,153) {\textbf{实施单位：} 新成功建筑科技股份公司（TTC JSC）——设计咨询、钢结构施工、受控工业地坪及技术基础设施。};

  % 案例故事
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (0,143) {项目需求、实施方案与交付价值};

  \fill[white,rounded corners=4pt] (0,79) rectangle (58,137);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,79) rectangle (58,137);
  \fill[TTCRed,rounded corners=2pt] (5,124) rectangle (16,133);
  \node[text=white,font=\fontsize{7}{8}\selectfont\bfseries] at (10.5,128.5) {01};
  \node[anchor=north west,text=TTCBlue,font=\fontsize{9}{10.5}\selectfont\bfseries]
    at (5,120) {技术挑战};
  \node[anchor=north west,text width=48mm,align=left,text=TTCTextDark,
        font=\fontsize{7.2}{9}\selectfont]
    at (5,110) {精密模具与工程零部件生产对基础稳定性、设备布置及机电接口提出较高要求。};

  \draw[-{Latex[length=2.5mm]},TTCCyan,line width=1pt] (59.5,108) -- (63,108);
  \fill[TTCDeepNavy,rounded corners=4pt] (64,79) rectangle (122,137);
  \node[text=TTCDeepNavy,fill=white,rounded corners=2pt,font=\fontsize{7}{8}\selectfont\bfseries,
        minimum width=11mm,minimum height=9mm] at (74.5,128.5) {02};
  \node[anchor=north west,text=white,font=\fontsize{9}{10.5}\selectfont\bfseries]
    at (69,120) {TTC 解决方案};
  \node[anchor=north west,text width=48mm,align=left,text=white,
        font=\fontsize{7.2}{9}\selectfont]
    at (69,110) {在设计阶段协同结构、设备基础与机电路由；钢结构、地坪及技术基础设施按受控工作包实施。};

  \draw[-{Latex[length=2.5mm]},TTCCyan,line width=1pt] (123.5,108) -- (127,108);
  \fill[TTCLightBlue,rounded corners=4pt] (128,79) rectangle (186,137);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (128,79) rectangle (186,137);
  \fill[TTCBlue,rounded corners=2pt] (133,124) rectangle (144,133);
  \node[text=white,font=\fontsize{7}{8}\selectfont\bfseries] at (138.5,128.5) {03};
  \node[anchor=north west,text=TTCBlue,font=\fontsize{9}{10.5}\selectfont\bfseries]
    at (133,120) {交付成效};
  \node[anchor=north west,text width=48mm,align=left,text=TTCTextDark,
        font=\fontsize{7.2}{9}\selectfont]
    at (133,110) {形成适配生产工艺的稳定空间，并为设备安装、调试及后续维护保留清晰接口。};

  % 总结记忆
  \fill[white,rounded corners=4pt] (0,20) rectangle (186,70);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,20) rectangle (186,70);
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (7,61) {核心价值亮点总结};
  \draw[TTCBorder] (62,27) -- (62,58);
  \draw[TTCBorder] (124,27) -- (124,58);
  \node[align=center,text width=52mm] at (31,42) {
    {\fontsize{11}{12}\selectfont\bfseries\color{TTCRed}精密工艺适配}\\[-.5mm]
    {\fontsize{6.6}{8}\selectfont\color{TTCTextMuted}设备基础与地坪协同设计}};
  \node[align=center,text width=52mm] at (93,42) {
    {\fontsize{11}{12}\selectfont\bfseries\color{TTCBlue}界面协同}\\[-.5mm]
    {\fontsize{6.6}{8}\selectfont\color{TTCTextMuted}结构 • 机电 • 设备安装}};
  \node[align=center,text width=52mm] at (155,42) {
    {\fontsize{11}{12}\selectfont\bfseries\color{TTCBlue}受控交付}\\[-.5mm]
    {\fontsize{6.6}{8}\selectfont\color{TTCTextMuted}记录完整并支持调试移交}};

  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,14);
  \node[anchor=west,text=white,font=\fontsize{7.4}{9}\selectfont\bfseries]
    at (7,7) {核心价值：精密生产适配 • 多专业协同 • 可追溯交付};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_23 = r"""% ============================================================
% TRANG 23: ENGINEERING CASE -- NHÀ MÁY SƠN ALO
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{技术解决方案 • ALO 涂料制造厂}{第23页}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{项目案例 02：ALO 越南涂料制造厂}{Paint \& chemical manufacturing complex • Phú Nghĩa Industrial Park, Hà Nội}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);

  % 实景
  \begin{scope}
    \clip[rounded corners=4pt] (0,148) rectangle (104,220);
    \node[inner sep=0pt] at (52,184)
      {\includegraphics[width=104mm,height=77.5mm]{../../public/project-assets/son_alo_2.jpg}};
    \node[inner sep=0pt,draw=white,line width=1.1pt] at (84,176)
      {\includegraphics[width=33mm,height=25mm]{../../public/project-assets/son_alo_1.jpg}};
    \fill[TTCDeepNavy,opacity=.88] (0,148) rectangle (104,160);
    \node[anchor=west,text=white,font=\fontsize{7}{8}\selectfont\bfseries]
      at (4,154) {概念效果与开工实景 • 河内市富义工业区};
  \end{scope}
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,148) rectangle (104,220);

  \fill[TTCDeepNavy,rounded corners=4pt] (108,148) rectangle (186,220);
  \node[anchor=north west,text=TTCCyan,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (114,214) {项目档案};
  \node[anchor=north west,text=white,font=\fontsize{15}{16}\selectfont\bfseries]
    at (114,205) {ALO PAINT};
  \node[anchor=north west,text=white!75!gray,font=\fontsize{6.5}{8}\selectfont]
    at (114,190) {涂料与化工生产设施};
  \draw[white!25!gray] (114,183) -- (180,183);
  \node[anchor=north west,text width=62mm,align=left,text=white,
        font=\fontsize{7.2}{9}\selectfont]
    at (114,178) {\textbf{业主：} ALO 越南投资股份公司\\[1mm]
                  \textbf{地点：} 富义工业区 CN1 地块，河内\\[1mm]
                  \textbf{功能：} 生产厂房与化学品仓库\\[1mm]
                  \textbf{实施单位：} 新成功建筑科技股份公司（TTC JSC）——EPC总承包};

  % 结构剖面原理图
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (0,140) {生产分区、机电与安全界面协同示意};
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
    at (16,112) {生产设备、配料区与仓储界面};
  \draw[TTCCyan,line width=1.2pt,dashed] (17,87) -- (127,87);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.3}{7.5}\selectfont\bfseries]
    at (19,82) {机电、通风与消防管线受控路由};
  \draw[<->,>=Latex,TTCBlue,line width=.8pt] (16,60) -- (128,60);
  \node[fill=TTCLightBlue,text=TTCBlue,font=\fontsize{6.5}{8}\selectfont\bfseries]
    at (72,60) {生产区与化学品仓库按工艺分隔};

  % 右侧设计要点
  \draw[TTCBorder] (138,60) -- (138,127);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (145,124) {三大关键设计界面};
  \node[anchor=north west,text width=34mm,align=left,text=TTCTextDark,
        font=\fontsize{6.7}{8.3}\selectfont]
    at (145,114) {\textbf{01 • 功能分区}\newline
                  按工艺与材料特性组织生产、仓储及辅助空间。};
  \node[anchor=north west,text width=34mm,align=left,text=TTCTextDark,
        font=\fontsize{6.7}{8.3}\selectfont]
    at (145,92) {\textbf{02 • 通风消防}\newline
                  通风、消防与电气方案依据获批设计协同实施。};
  \node[anchor=north west,text width=34mm,align=left,text=TTCTextDark,
        font=\fontsize{6.7}{8.3}\selectfont]
    at (145,70) {\textbf{03 • 材料控制}\newline
                  化学品相关材料按报审、验收与追溯程序管理。};

  % 总结卡片
  \fill[white,rounded corners=3pt] (0,9) rectangle (58,45);
  \draw[TTCBorder,rounded corners=3pt] (0,9) rectangle (58,45);
  \node[anchor=north west,text=TTCRed,font=\fontsize{8}{9}\selectfont\bfseries]
    at (5,39) {01 • 工艺适配};
  \node[anchor=north west,text width=48mm,text=TTCTextDark,font=\fontsize{6.8}{8.4}\selectfont]
    at (5,30) {建筑与结构方案围绕涂料生产及仓储流程进行协调。};

  \fill[white,rounded corners=3pt] (64,9) rectangle (122,45);
  \draw[TTCBorder,rounded corners=3pt] (64,9) rectangle (122,45);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9}\selectfont\bfseries]
    at (69,39) {02 • 安全界面};
  \node[anchor=north west,text width=48mm,text=TTCTextDark,font=\fontsize{6.8}{8.4}\selectfont]
    at (69,30) {机电、通风与消防接口在施工前完成综合校核。};

  \fill[white,rounded corners=3pt] (128,9) rectangle (186,45);
  \draw[TTCBorder,rounded corners=3pt] (128,9) rectangle (186,45);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9}\selectfont\bfseries]
    at (133,39) {03 • 受控交付};
  \node[anchor=north west,text width=48mm,text=TTCTextDark,font=\fontsize{6.8}{8.4}\selectfont]
    at (133,30) {材料、检验与系统调试记录纳入项目移交卷宗。};

  \fill[TTCDeepNavy,rounded corners=2pt] (0,0) rectangle (186,6);
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_24 = r"""% ============================================================
% TRANG 24: PROCESS CASE -- NHÀ MÁY NHỰA SENDAI
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{技术解决方案 • SENDAI 塑料制造厂}{第24页}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{项目案例 03：Sendai 越南塑料制造厂}{Engineering plastics facility • Injection molding • Industrial Park No. 3, Hưng Yên}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);

  % 照片与指标
  \begin{scope}
    \clip[rounded corners=4pt] (0,151) rectangle (68,219);
    \node[inner sep=0pt] at (34,185)
      {\includegraphics[width=68mm,height=68mm]{../../public/project-assets/sendai_1.jpg}};
    \fill[TTCDeepNavy,opacity=.9] (0,151) rectangle (68,162);
    \node[anchor=west,text=white,font=\fontsize{7}{8}\selectfont\bfseries]
      at (4,156.5) {项目实景 • SENDAI PLASTICS};
  \end{scope}
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,151) rectangle (68,219);

  \fill[TTCLightBlue,rounded corners=4pt] (72,151) rectangle (186,219);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (72,151) rectangle (186,219);
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (78,211) {兴安省恩施县第三工业区};
  \draw[TTCBorder] (129,158) -- (129,204);
  \draw[TTCBorder] (78,181) -- (180,181);
  \node[align=center,text width=45mm] at (103.5,193) {
    {\fontsize{10}{11}\selectfont\bfseries\color{TTCRed}业主}\\[-.5mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}Sendai Plastics}};
  \node[align=center,text width=45mm] at (154.5,193) {
    {\fontsize{10}{11}\selectfont\bfseries\color{TTCBlue}两座厂房}\\[-.5mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}塑料注塑生产}};
  \node[align=center,text width=45mm] at (103.5,169) {
    {\fontsize{10}{11}\selectfont\bfseries\color{TTCBlue}办公楼}\\[-.5mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}三层配套空间}};
  \node[align=center,text width=45mm] at (154.5,169) {
    {\fontsize{10}{11}\selectfont\bfseries\color{TTCBlue}总承包}\\[-.5mm]
    {\fontsize{6.2}{7.4}\selectfont\color{TTCTextMuted}建筑与机电施工}};

  % 筒仓示意
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (0,143) {工程实施重点 • 从注塑设备基础到厂房与办公协同};
  \fill[TTCLightBlue,rounded corners=4pt] (0,56) rectangle (54,137);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,56) rectangle (54,137);

  \fill[TTCBlue!10!white] (19,69) rectangle (42,123);
  \draw[TTCBlue,line width=1.1pt] (19,69) rectangle (42,123);
  \foreach \y in {80,91,102,113}{\draw[TTCBorder] (19,\y) -- (42,\y);}
  \draw[TTCBlue,line width=1.1pt] (16,69) -- (45,69);
  \fill[TTCDeepNavy] (12,62) rectangle (49,69);
  \draw[<->,>=Latex,TTCRed,line width=.9pt] (9,69) -- (9,123);
  \node[rotate=90,text=TTCRed,font=\fontsize{9}{10}\selectfont\bfseries]
    at (4,96) {三层办公配套};
  \node[text=TTCBlue,font=\fontsize{6.5}{7.5}\selectfont\bfseries]
    at (30.5,129) {办公与辅助空间};
  \node[text=white,font=\fontsize{6.2}{7.2}\selectfont\bfseries]
    at (30.5,65.5) {受控基础与结构};

  % 三大应对措施
  \fill[white,rounded corners=3pt] (60,108) rectangle (186,137);
  \draw[TTCBorder,rounded corners=3pt] (60,108) rectangle (186,137);
  \fill[TTCRed] (60,108) rectangle (63,137);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9}\selectfont\bfseries]
    at (69,132) {01 • 注塑设备基础与地坪};
  \node[anchor=north west,text width=108mm,text=TTCTextDark,font=\fontsize{6.9}{8.4}\selectfont]
    at (69,122) {依据经批准的设备资料协调基础、预埋与地坪做法，保留安装和维护空间。};

  \fill[white,rounded corners=3pt] (60,76) rectangle (186,105);
  \draw[TTCBorder,rounded corners=3pt] (60,76) rectangle (186,105);
  \fill[TTCBlue] (60,76) rectangle (63,105);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9}\selectfont\bfseries]
    at (69,100) {02 • 厂房与办公楼界面协同};
  \node[anchor=north west,text width=108mm,text=TTCTextDark,font=\fontsize{6.9}{8.4}\selectfont]
    at (69,90) {结构、围护及机电系统按工作面分区推进，统一管理连接节点与移交条件。};

  \fill[white,rounded corners=3pt] (60,44) rectangle (186,73);
  \draw[TTCBorder,rounded corners=3pt] (60,44) rectangle (186,73);
  \fill[TTCBlue] (60,44) rectangle (63,73);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9}\selectfont\bfseries]
    at (69,68) {03 • 机电与消防系统集成};
  \node[anchor=north west,text width=108mm,text=TTCTextDark,font=\fontsize{6.9}{8.4}\selectfont]
    at (69,58) {电气、给排水、通风与消防依据获批设计实施，并按检验计划完成调试与移交。};

  % 实施范围
  \fill[TTCDeepNavy,rounded corners=4pt] (0,0) rectangle (186,35);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.5}{8}\selectfont\bfseries]
    at (7,28) {TTC 实施范围};
  \foreach \x in {46.5,93,139.5}{\draw[white!25!gray] (\x,6) -- (\x,25);}
  \node[align=center,text width=39mm,text=white,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (23.25,15) {设备基础与地坪\\[-.5mm]{\fontsize{5.8}{7}\selectfont\color{white!70!gray}依据工艺资料协调}};
  \node[align=center,text width=39mm,text=white,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (69.75,15) {PEB 钢结构施工\\[-.5mm]{\fontsize{5.8}{7}\selectfont\color{white!70!gray}厂房主体与围护}};
  \node[align=center,text width=39mm,text=white,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (116.25,15) {多工作面协同\\[-.5mm]{\fontsize{5.8}{7}\selectfont\color{white!70!gray}厂房与办公楼界面}};
  \node[align=center,text width=39mm,text=white,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (162.75,15) {机电配套系统\\[-.5mm]{\fontsize{5.8}{7}\selectfont\color{white!70!gray}电气 • 给排水 • 消防}};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_25 = r"""% ============================================================
% TRANG 25: MULTI-STOREY GARMENT CASE -- LÀO CAI
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{技术解决方案 • 老街制衣厂综合体}{第25页}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{项目案例 04：老街制衣厂综合体}{Multi-storey garment manufacturing • Phố Mới, Lào Cai City}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);

  % 实景
  \begin{scope}
    \clip[rounded corners=4pt] (0,157) rectangle (118,219);
    \node[inner sep=0pt] at (59,188)
      {\includegraphics[width=118mm]{../../public/project-assets/laocai_4.jpg}};
    \fill[TTCDeepNavy,opacity=.88] (0,157) rectangle (118,168);
    \node[anchor=west,text=white,font=\fontsize{7}{8}\selectfont\bfseries]
      at (4,162.5) {项目实景 • 老街市铺买区};
  \end{scope}
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,157) rectangle (118,219);

  \fill[TTCDeepNavy,rounded corners=4pt] (122,157) rectangle (186,219);
  \node[anchor=north west,text=TTCCyan,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (128,213) {项目基本信息};
  \node[anchor=north west,text=white,font=\fontsize{13}{14}\selectfont\bfseries]
    at (128,203) {3 座厂房};
  \node[anchor=north west,text=white!70!gray,font=\fontsize{6}{7.2}\selectfont]
    at (128,190) {多层制衣生产综合体};
  \draw[white!25!gray] (128,184) -- (180,184);
  \node[anchor=north west,text width=48mm,align=left,text=white,
        font=\fontsize{6.8}{8.4}\selectfont]
    at (128,180) {\textbf{业主：} 老街制衣公司\\
                  \textbf{形式：} 五层生产厂房\\
                  \textbf{实施单位：} 新成功建筑科技股份公司（TTC JSC）——建筑设计与施工总承包};

  % 系统图
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (0,149) {多层生产空间、物流与环境系统协同组织};
  \fill[TTCLightBlue,rounded corners=4pt] (0,57) rectangle (186,143);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,57) rectangle (186,143);

  % 核心区
  \fill[TTCDeepNavy,rounded corners=4pt] (68,88) rectangle (118,116);
  \node[align=center,text=white,text width=42mm,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (93,102) {多层制衣生产区\\[-.5mm]
    {\fontsize{6}{7.2}\selectfont\color{white!70!gray}生产 • 物流 • 人流协同}};

  % 四个外围模块
  \fill[white,rounded corners=3pt] (7,108) rectangle (58,136);
  \draw[TTCBorder,rounded corners=3pt] (7,108) rectangle (58,136);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{7.5}{8.5}\selectfont\bfseries]
    at (12,131) {01 • 垂直功能分区};
  \node[anchor=north west,text width=41mm,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont]
    at (12,121) {按生产工序组织楼层功能，并协调人员、物料及成品流线。};

  \fill[white,rounded corners=3pt] (128,108) rectangle (179,136);
  \draw[TTCBorder,rounded corners=3pt] (128,108) rectangle (179,136);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{7.5}{8.5}\selectfont\bfseries]
    at (133,131) {02 • 环境与通风};
  \node[anchor=north west,text width=41mm,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont]
    at (133,121) {结合工艺需求配置通风与降温方案，改善高密度生产空间环境。};

  \fill[white,rounded corners=3pt] (7,64) rectangle (58,92);
  \draw[TTCBorder,rounded corners=3pt] (7,64) rectangle (58,92);
  \node[anchor=north west,text=TTCRed,font=\fontsize{7.5}{8.5}\selectfont\bfseries]
    at (12,87) {03 • 结构与地坪};
  \node[anchor=north west,text width=41mm,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont]
    at (12,77) {楼板、设备区及运输路线依据获批设计荷载统一协调。};

  \fill[white,rounded corners=3pt] (128,64) rectangle (179,92);
  \draw[TTCBorder,rounded corners=3pt] (128,64) rectangle (179,92);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{7.5}{8.5}\selectfont\bfseries]
    at (133,87) {04 • 消防与疏散};
  \node[anchor=north west,text width=41mm,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont]
    at (133,77) {消防系统与多层疏散路径按获批文件实施并完成联动调试。};

  \draw[-{Latex[length=2mm]},TTCCyan,line width=.9pt] (58,122) -- (68,108);
  \draw[-{Latex[length=2mm]},TTCCyan,line width=.9pt] (128,122) -- (118,108);
  \draw[-{Latex[length=2mm]},TTCCyan,line width=.9pt] (58,78) -- (68,94);
  \draw[-{Latex[length=2mm]},TTCCyan,line width=.9pt] (128,78) -- (118,94);

  % 总结
  \fill[white,rounded corners=3pt] (0,10) rectangle (58,48);
  \draw[TTCBorder,rounded corners=3pt] (0,10) rectangle (58,48);
  \node[align=center,text width=48mm] at (29,29) {
    {\fontsize{10}{11}\selectfont\bfseries\color{TTCRed}多层生产}\\[-.5mm]
    {\fontsize{6.4}{7.6}\selectfont\color{TTCTextMuted}垂直组织生产与物流}};

  \fill[white,rounded corners=3pt] (64,10) rectangle (122,48);
  \draw[TTCBorder,rounded corners=3pt] (64,10) rectangle (122,48);
  \node[align=center,text width=48mm] at (93,29) {
    {\fontsize{10}{11}\selectfont\bfseries\color{TTCBlue}环境协同}\\[-.5mm]
    {\fontsize{6.4}{7.6}\selectfont\color{TTCTextMuted}通风、采光与生产需求}};

  \fill[white,rounded corners=3pt] (128,10) rectangle (186,48);
  \draw[TTCBorder,rounded corners=3pt] (128,10) rectangle (186,48);
  \node[align=center,text width=48mm] at (157,29) {
    {\fontsize{10}{11}\selectfont\bfseries\color{TTCBlue}整体实施}\\[-.5mm]
    {\fontsize{6.4}{7.6}\selectfont\color{TTCTextMuted}建筑设计与施工总承包}};

  \fill[TTCDeepNavy,rounded corners=2pt] (0,0) rectangle (186,6);
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_26 = r"""% ============================================================
% TRANG 26: QUALITY DELIVERY -- NHÀ MÁY NHỰA DHL
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{技术解决方案 • DHL 塑料制造厂}{第26页}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{项目案例 05：DHL 塑料制造厂}{Plastic packaging \& PE/PP film facility • Thái Hà Industrial Park, Hà Nam}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);

  % 厂区照片与概况
  \begin{scope}
    \clip[rounded corners=4pt] (0,155) rectangle (64,219);
    \node[inner sep=0pt] at (32,187)
      {\includegraphics[width=64mm,height=64mm]{../../public/project-assets/dhl_2.jpg}};
    \fill[TTCDeepNavy,opacity=.88] (0,155) rectangle (64,166);
    \node[anchor=west,text=white,font=\fontsize{6.8}{8}\selectfont\bfseries]
      at (4,160.5) {项目实景 • DHL PLASTICS};
  \end{scope}
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,155) rectangle (64,219);

  \fill[TTCLightBlue,rounded corners=4pt] (68,155) rectangle (186,219);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (68,155) rectangle (186,219);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (75,212) {项目档案概览};
  \node[anchor=north west,text width=48mm,text=TTCTextDark,font=\fontsize{7.1}{8.8}\selectfont]
    at (75,201) {\textbf{业主：} DHL 塑料集团股份公司\\
                  \textbf{地点：} 太河工业区 CN02 地块，河南省\\
                  \textbf{功能：} PE/PP 薄膜厂房与三层办公楼};
  \draw[TTCBorder] (129,161) -- (129,208);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (136,212) {重点交付保障};
  \node[anchor=north west,text width=43mm,text=TTCTextDark,font=\fontsize{6.9}{8.5}\selectfont]
    at (136,201) {\textbullet\quad PEB 钢结构与围护系统\\[1mm]
                  \textbullet\quad 生产设备基础及机电接口\\[1mm]
                  \textbullet\quad 检验、调试与移交资料};

  % 四道质量关口
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (0,147) {塑料薄膜生产厂房四级质量控制关口};
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
    at (0,80) {主要工程分项、质量控制点与交付记录};
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
  \node[anchor=west,text=TTCBlue,font=\fontsize{6.6}{8}\selectfont\bfseries] at (6,54.5) {PEB 钢结构};
  \node[anchor=west,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont] at (55,54.5) {材料批次 • 焊接 • 几何尺寸};
  \node[anchor=west,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont] at (126,54.5) {检验记录与竣工图};
  \node[anchor=west,text=TTCBlue,font=\fontsize{6.6}{8}\selectfont\bfseries] at (6,39.5) {机电与消防};
  \node[anchor=west,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont] at (55,39.5) {压力试验 • 联动 • 试运转};
  \node[anchor=west,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont] at (126,39.5) {调试报告与验收记录};
  \node[anchor=west,text=TTCBlue,font=\fontsize{6.6}{8}\selectfont\bfseries] at (6,24.5) {设备基础与地坪};
  \node[anchor=west,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont] at (55,24.5) {轴线 • 标高 • 平整度 • 预埋};
  \node[anchor=west,text=TTCTextDark,font=\fontsize{6.4}{7.8}\selectfont] at (126,24.5) {测量记录与移交清单};

  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,11);
  \node[anchor=west,text=white,font=\fontsize{7}{8.5}\selectfont\bfseries]
    at (7,5.5) {DHL PLASTICS};
  \node[text=white!35!gray] at (49,5.5) {|};
  \node[anchor=west,text=white,font=\fontsize{7}{8.5}\selectfont\bfseries]
    at (57,5.5) {PEB 与机电协同};
  \node[text=white!35!gray] at (95,5.5) {|};
  \node[anchor=west,text=white,font=\fontsize{7}{8.5}\selectfont\bfseries]
    at (103,5.5) {实施单位：新成功建筑科技股份公司（TTC JSC）};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_27 = r"""% ============================================================
% TRANG 27: PROJECT SPOTLIGHT -- NHÀ MÁY NHÔM QUANG THỊNH
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{技术解决方案 • 广盛铝型材制造厂}{第27页}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{项目案例 06：广盛铝型材制造厂}{Aluminium profiles facility • Extrusion production • Thuận Thành, Bắc Ninh}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);

  % 实景
  \begin{scope}
    \clip[rounded corners=4pt] (0,151) rectangle (186,219);
    \node[inner sep=0pt] at (93,185)
      {\includegraphics[width=186mm]{../../public/project-assets/quangthinh_1.jpg}};
    \node[inner sep=0pt,draw=white,line width=1.1pt] at (102,183)
      {\includegraphics[width=38mm,height=27mm]{../../public/project-assets/quangthinh_3.jpg}};
    \fill[TTCDeepNavy,opacity=.9] (0,151) rectangle (78,168);
    \node[anchor=west,text=white,font=\fontsize{7}{8}\selectfont\bfseries]
      at (5,159.5) {概念效果与施工实景 • 北宁省顺成市};
    \fill[TTCDeepNavy,opacity=.92] (127,151) rectangle (186,219);
    \node[anchor=north west,text=TTCCyan,font=\fontsize{6.8}{8}\selectfont\bfseries]
      at (133,212) {项目档案概览};
    \node[anchor=north west,text=white,font=\fontsize{14}{15}\selectfont\bfseries]
      at (133,201) {铝型材厂房};
    \node[anchor=north west,text=white!70!gray,font=\fontsize{6}{7.2}\selectfont]
      at (133,187) {挤压生产与办公配套};
    \draw[white!25!gray] (133,181) -- (180,181);
    \node[anchor=north west,text width=43mm,text=white,font=\fontsize{6.5}{8}\selectfont]
      at (133,177) {\textbf{业主：} 广盛铝业股份公司\\
                    \textbf{地点：} 北宁省顺成市\\
                    \textbf{实施单位：} 新成功建筑科技股份公司（TTC JSC）——PEB与机电施工总承包};
  \end{scope}
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,151) rectangle (186,219);

  % 施工流
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (0,143) {锁定挤压生产线技术接口 • 分区组织结构与机电施工};
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
    at (9,96) {锁定设备轴线、标高及结构与机电接口。};

  \fill[TTCBlue] (56,122) circle (3.5mm);
  \node[text=white,font=\fontsize{6}{7}\selectfont\bfseries] at (56,122) {02};
  \node[anchor=north west,text width=29mm,align=left,text=TTCBlue,
        font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (55,115) {工厂预制\\精密加工};
  \node[anchor=north west,text width=29mm,align=left,text=TTCTextMuted,
        font=\fontsize{6.1}{7.4}\selectfont]
    at (55,96) {数控加工与驻厂QC执行材料和构件检验。};

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
    at (147,96) {按检验计划复核几何尺寸与高强螺栓终拧。};

  % 两大核心要点
  \fill[white,rounded corners=4pt] (0,19) rectangle (90,60);
  \draw[TTCBorder,rounded corners=4pt] (0,19) rectangle (90,60);
  \node[anchor=north west,text=TTCRed,font=\fontsize{8}{9}\selectfont\bfseries]
    at (6,54) {项目核心难点};
  \node[anchor=north west,text width=77mm,align=left,text=TTCTextDark,
        font=\fontsize{6.9}{8.5}\selectfont]
    at (6,44) {铝挤压生产线对设备布置、物流通道、结构空间及机电接口的协调要求较高。};

  \fill[TTCLightBlue,rounded corners=4pt] (96,19) rectangle (186,60);
  \draw[TTCBorder,rounded corners=4pt] (96,19) rectangle (186,60);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{8}{9.5}\selectfont\bfseries]
    at (102,54) {TTC 实施策略};
  \node[anchor=north west,text width=77mm,align=left,text=TTCTextDark,
        font=\fontsize{6.9}{8.5}\selectfont]
    at (102,44) {采用分区施工与构件预制方案，围绕设备基础、钢结构、围护和机电工作面逐段移交。};

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
