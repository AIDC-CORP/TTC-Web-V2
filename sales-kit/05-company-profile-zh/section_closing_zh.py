# -*- coding: utf-8 -*-
"""
Section Closing: Supply Chain, Sector Ecosystem, Closeout Dossier, Legal & Governance,
Footprint Map, Roadmap 2026-2030, Warranty, Partners, Back Cover (Pages 28 - 36) — 简体中文版
"""

PAGE_28 = r"""% ============================================================
% TRANG 28: CHUỖI CUNG ỨNG KIỂM SOÁT
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{严格受控的战略供应链体系}{第28页}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{按批次严格受控的战略供应链}{Approved sources • Material submittal • CO/CQ/MTC • Lot traceability}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);

  \node[anchor=west,text=TTCBlue,font=\fontsize{15}{17}\selectfont\bfseries]
    at (0,211) {全套质检文件齐备方获准进场安装};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{7.2}{8.8}\selectfont]
    at (0,201) {统一严密的物资审批报审流程，确保采购前锁定品牌源头、技术指标与替代可行性。};

  % 4道把关
  \fill[TTCDeepNavy,rounded corners=4pt] (0,79) rectangle (62,192);
  \node[anchor=west,text=TTCCyan,font=\fontsize{7}{8.3}\selectfont\bfseries]
    at (7,184) {4 级物资把关关口};
  \draw[white!18!gray] (7,178) -- (55,178);

  \foreach \y/\n/\title/\desc in {
    158/01/厂家源头报审/厂家资质 • 样品封存 • 技术规格书,
    134/02/文件闭环核验/CO-CQ • MTC质保书 • 产品型录,
    110/03/进场严格复检/批次标签 • 外观尺寸 • 试验室复验,
    88/04/安装可溯追踪/物资批次绑定施工部位与检验批单}
  {
    \fill[white,rounded corners=2pt] (7,{\y-8}) rectangle (55,{\y+8});
    \fill[TTCRed] (7,{\y-8}) rectangle (16,{\y+8});
    \node[text=white,font=\fontsize{6.2}{7}\selectfont\bfseries] at (11.5,\y) {\n};
    \node[anchor=north west,text width=34mm,text=TTCBlue,
          font=\fontsize{6.7}{7.8}\selectfont\bfseries] at (19,{\y+5}) {\title};
    \node[anchor=north west,text width=34mm,text=TTCTextMuted,
          font=\fontsize{5.6}{6.7}\selectfont] at (19,{\y-1}) {\desc};
  }

  % 材料矩阵
  \fill[white,rounded corners=4pt] (67,79) rectangle (186,192);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (67,79) rectangle (186,192);
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.4}\selectfont\bfseries]
    at (74,184) {核心材料品类 / 国际基准品牌库};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{5.8}{7}\selectfont]
    at (74,176) {实际选用品牌严格遵循各工程经业主与监理批准的材料报审表。};

  \foreach \y/\n/\name/\brands/\control in {
    157/01/钢材与围护板材/POSCO • 和发 (Hoa Phat) • 烨辉 (BlueScope)/MTC • 钢号 • 镀锌铝层,
    134/02/工业涂料与化学建材/佐敦 (Jotun) • KCC • 西卡 (Sika)/批次 • DFT漆膜 • 防火认证,
    111/03/电气与配电系统/施耐德 (Schneider) • ABB • LS Vina/型录 • 试验报告 • 原产地,
    88/04/暖通与消防系统/大金 (Daikin) • 格兰富 (Grundfos) • 泰科 (Tyco)/报审 • UL-FM 认证要求}
  {
    \fill[TTCLightBlue,rounded corners=2pt] (73,{\y-9}) rectangle (180,{\y+9});
    \node[anchor=west,text=TTCRed,font=\fontsize{6.4}{7.5}\selectfont\bfseries]
      at (78,{\y+4}) {\n};
    \node[anchor=west,text=TTCBlue,font=\fontsize{7}{8.2}\selectfont\bfseries]
      at (91,{\y+4}) {\name};
    \node[anchor=west,text=TTCTextDark,font=\fontsize{6.2}{7.3}\selectfont]
      at (91,{\y-2}) {\brands};
    \node[anchor=east,text=TTCTextMuted,font=\fontsize{5.6}{6.7}\selectfont]
      at (176,{\y-7}) {控制点：\control};
  }

  % 三大保证
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.4}\selectfont\bfseries]
    at (0,68) {进场安装前三大质量保证屏障};
  \foreach \xa/\xb/\n/\title/\desc in {
    0/58/01/正品正源/报审文件与厂家实际出厂来源相互对应,
    64/122/02/指标达标/物理力学指标完全符合封样及工程技术规范,
    128/186/03/位批对应/每批进场材料精准对应具体构件编号与施工区域}
  {
    \fill[white,rounded corners=3pt] (\xa,25) rectangle (\xb,60);
    \draw[TTCBorder,rounded corners=3pt] (\xa,25) rectangle (\xb,60);
    \node[anchor=west,text=TTCRed,font=\fontsize{7}{8}\selectfont\bfseries]
      at ({\xa+6},52) {\n};
    \node[anchor=west,text=TTCBlue,font=\fontsize{7.4}{8.7}\selectfont\bfseries]
      at ({\xa+17},52) {\title};
    \node[anchor=north west,text width=46mm,text=TTCTextMuted,
          font=\fontsize{6.2}{7.5}\selectfont] at ({\xa+6},43) {\desc};
  }

  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,16);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.3}{7.5}\selectfont\bfseries]
    at (7,8) {MATERIAL ASSURANCE};
  \node[anchor=east,text=white,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
    at (179,8) {核准源头 → 逐批复检 → 全程可溯安装};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_29 = r"""% ============================================================
% TRANG 29: HỆ SINH THÁI CÔNG TRÌNH THEO NGÀNH
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{六大行业工业建筑生态体系}{第29页}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{六大行业定制化工程 — 一体化综合总包能力}{Representative sectors • Different operating demands • One coordinated EPC workflow}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);
  \node[anchor=west,text=TTCBlue,font=\fontsize{15}{17}\selectfont\bfseries]
    at (0,211) {工程设计始于对工厂工艺生产流程的深刻理解};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{7.2}{8.8}\selectfont]
    at (0,201) {每个工业领域都有其独特的运营难点；结构、机电与施工部署必须精准契合工艺安全。};

  % 行 1
  \begin{scope}
    \clip[rounded corners=3pt] (0,132) rectangle (59,190);
    \node[inner sep=0pt] at (29.5,165) {\includegraphics[width=60mm]{../../public/project-assets/japfa.jpg}};
    \fill[TTCDeepNavy,opacity=.9] (0,132) rectangle (59,151);
  \end{scope}
  \draw[TTCBorder,rounded corners=3pt] (0,132) rectangle (59,190);
  \node[anchor=west,text=white,font=\fontsize{7.5}{8.8}\selectfont\bfseries] at (5,144) {食品加工与农牧饲料};
  \node[anchor=west,text=white!75!gray,font=\fontsize{5.8}{7}\selectfont] at (5,137) {筒仓 • 工艺管网 • 洁净防尘 • 防爆};

  \begin{scope}
    \clip[rounded corners=3pt] (63.5,132) rectangle (122.5,190);
    \node[inner sep=0pt] at (93,167) {\includegraphics[height=41mm]{../../public/project-assets/daeyun.jpg}};
    \fill[TTCDeepNavy,opacity=.9] (63.5,132) rectangle (122.5,151);
  \end{scope}
  \draw[TTCBorder,rounded corners=3pt] (63.5,132) rectangle (122.5,190);
  \node[anchor=west,text=white,font=\fontsize{7.5}{8.8}\selectfont\bfseries] at (68.5,144) {半导体电子与无尘室};
  \node[anchor=west,text=white!75!gray,font=\fontsize{5.8}{7}\selectfont] at (68.5,137) {洁净空调 • ESD 防静电 • 恒温恒湿};

  \begin{scope}
    \clip[rounded corners=3pt] (127,132) rectangle (186,190);
    \node[inner sep=0pt] at (156.5,168) {\includegraphics[height=41mm]{../../public/project-assets/foxcon.png}};
    \fill[TTCDeepNavy,opacity=.9] (127,132) rectangle (186,151);
  \end{scope}
  \draw[TTCBorder,rounded corners=3pt] (127,132) rectangle (186,190);
  \node[anchor=west,text=white,font=\fontsize{7.5}{8.8}\selectfont\bfseries] at (132,144) {精密电子组装厂房};
  \node[anchor=west,text=white!75!gray,font=\fontsize{5.8}{7}\selectfont] at (132,137) {MEP 接口锁定 • 模块化分区吊装};

  % 行 2
  \begin{scope}
    \clip[rounded corners=3pt] (0,69) rectangle (59,127);
    \node[inner sep=0pt] at (29.5,103) {\includegraphics[height=42mm]{../../public/project-assets/songhong7.jpg}};
    \fill[TTCDeepNavy,opacity=.9] (0,69) rectangle (59,88);
  \end{scope}
  \draw[TTCBorder,rounded corners=3pt] (0,69) rectangle (59,127);
  \node[anchor=west,text=white,font=\fontsize{7.5}{8.8}\selectfont\bfseries] at (5,81) {纺织服装多层厂房};
  \node[anchor=west,text=white!75!gray,font=\fontsize{5.8}{7}\selectfont] at (5,74) {双层重荷载 • 大跨度 • 消防疏散};

  \begin{scope}
    \clip[rounded corners=3pt] (63.5,69) rectangle (122.5,127);
    \node[inner sep=0pt] at (93,104) {\includegraphics[width=60mm]{../../public/project-assets/yusen.jpg}};
    \fill[TTCDeepNavy,opacity=.9] (63.5,69) rectangle (122.5,88);
  \end{scope}
  \draw[TTCBorder,rounded corners=3pt] (63.5,69) rectangle (122.5,127);
  \node[anchor=west,text=white,font=\fontsize{7.5}{8.8}\selectfont\bfseries] at (68.5,81) {智慧物流仓储中心};
  \node[anchor=west,text=white!75!gray,font=\fontsize{5.8}{7}\selectfont] at (68.5,74) {超平地坪 • 升降卸货平台 • 动线优化};

  \begin{scope}
    \clip[rounded corners=3pt] (127,69) rectangle (186,127);
    \node[inner sep=0pt] at (156.5,104) {\includegraphics[width=60mm]{../../public/project-assets/sumidenso.jpg}};
    \fill[TTCDeepNavy,opacity=.9] (127,69) rectangle (186,88);
  \end{scope}
  \draw[TTCBorder,rounded corners=3pt] (127,69) rectangle (186,127);
  \node[anchor=west,text=white,font=\fontsize{7.5}{8.8}\selectfont\bfseries] at (132,81) {汽车零部件制造};
  \node[anchor=west,text=white!75!gray,font=\fontsize{5.8}{7}\selectfont] at (132,74) {日系精益品控 • 逐级放行验收};

  % 三大能力
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.3}\selectfont\bfseries]
    at (0,58) {贯穿所有行业的核心 EPC 总包能力};
  \foreach \xa/\xb/\title/\desc in {
    0/58/COORDINATION 全专业深化/建筑 • 结构 • 机电BIM全流程接口锁定,
    64/122/CONSTRUCTABILITY 可施工性/以现场施工工序反向指导工程深化设计,
    128/186/HANDOVER 严谨移交/凭齐备数据与实测报告逐级签署移交}
  {
    \fill[TTCLightBlue,rounded corners=3pt] (\xa,20) rectangle (\xb,50);
    \node[anchor=west,text=TTCBlue,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
      at ({\xa+6},41) {\title};
    \node[anchor=north west,text width=46mm,text=TTCTextMuted,
          font=\fontsize{6.1}{7.3}\selectfont] at ({\xa+6},34) {\desc};
  }
  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,12);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.2}{7.4}\selectfont\bfseries] at (7,6) {SECTOR FIT};
  \node[anchor=east,text=white,font=\fontsize{7}{8.3}\selectfont\bfseries]
    at (179,6) {解决方案因工艺需求而定制 • 履约保障因专业而可靠};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_30 = r"""% ============================================================
% TRANG 30: BỘ HỒ SƠ BÀN GIAO
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{竣工交付档案与可溯数据凭据}{第30页}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{全程可追溯的标准化竣工移交档案卷宗}{Evidence chain from approved material to as-built and commissioning records}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);
  \node[anchor=west,text=TTCBlue,font=\fontsize{15}{17}\selectfont\bfseries]
    at (0,211) {交付实体工程，同时交付完整合规的数字档案};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{7.2}{8.8}\selectfont]
    at (0,201) {每道工序只有在技术图纸、试验报告与现场影像三方一致后方可闭环归档。};

  % 5个门禁
  \fill[TTCLightBlue,rounded corners=4pt] (0,139) rectangle (186,190);
  \draw[TTCBorder,rounded corners=4pt] (0,139) rectangle (186,190);
  \draw[TTCBlue!40!white,line width=.8pt] (18,165) -- (168,165);
  \foreach \x/\n/\title in {
    18/01/材料进场,
    55.5/02/深化详图,
    93/03/工序验收,
    130.5/04/竣工图纸,
    168/05/联调联试}
  {
    \fill[white] (\x,165) circle (5mm);
    \draw[TTCBlue,line width=.8pt] (\x,165) circle (5mm);
    \node[text=TTCBlue,font=\fontsize{6}{7}\selectfont\bfseries] at (\x,165) {\n};
    \node[anchor=north,align=center,text width=29mm,text=TTCBlue,
          font=\fontsize{6.5}{7.7}\selectfont\bfseries] at (\x,155) {\title};
  }
  \fill[TTCRed] (18,165) circle (3.5mm);
  \node[text=white,font=\fontsize{5.8}{6.8}\selectfont\bfseries] at (18,165) {01};

  % 左侧卷宗
  \fill[TTCDeepNavy,rounded corners=4pt] (0,48) rectangle (70,130);
  \node[anchor=west,text=TTCCyan,font=\fontsize{7}{8.2}\selectfont\bfseries]
    at (7,121) {CLOSEOUT DOSSIER};
  \fill[white!15!gray,rounded corners=2pt] (15,61) rectangle (61,111);
  \fill[white!45!gray,rounded corners=2pt] (12,65) rectangle (58,115);
  \fill[white,rounded corners=2pt] (9,69) rectangle (55,119);
  \fill[TTCRed] (9,112) rectangle (55,119);
  \node[anchor=west,text=TTCBlue,font=\fontsize{7.4}{8.6}\selectfont\bfseries]
    at (15,103) {竣工档案卷宗};
  \draw[TTCBorder] (15,96) -- (49,96);
  \draw[TTCBorder] (15,90) -- (49,90);
  \draw[TTCBorder] (15,84) -- (42,84);
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{5.8}{7}\selectfont]
    at (15,76) {CDE 统一索引 • 版本审批};
  \node[anchor=west,text=white,font=\fontsize{6.1}{7.3}\selectfont\bfseries]
    at (7,55) {单一索引库 • 模块化卷宗};

  % 右侧清单
  \fill[white,rounded corners=4pt] (76,48) rectangle (186,130);
  \draw[TTCBorder,rounded corners=4pt] (76,48) rectangle (186,130);
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.4}\selectfont\bfseries]
    at (83,120) {标准竣工移交档案清单架构};
  \foreach \y/\n/\title/\desc in {
    104/01/物资凭证卷宗/核准报审单 • CO/CQ 产地证 • MTC 质保书 • 试验报告,
    90/02/施工质检卷宗/ITP 检验批 • 旁站记录 • 隐蔽工程验收单,
    76/03/竣工图纸卷宗/As-built 竣工图 • 版本变动记录 • 监理业主签章,
    62/04/运维指导卷宗/O\&M 操作维保手册 • 质保承诺书 • 设备备品备件清单}
  {
    \fill[TTCLightBlue,rounded corners=2pt] (83,{\y-6}) rectangle (179,{\y+6});
    \node[anchor=west,text=TTCRed,font=\fontsize{6.2}{7.2}\selectfont\bfseries]
      at (88,\y) {\n};
    \node[anchor=west,text=TTCBlue,font=\fontsize{6.6}{7.7}\selectfont\bfseries]
      at (101,{\y+2}) {\title};
    \node[anchor=west,text=TTCTextMuted,font=\fontsize{5.6}{6.7}\selectfont]
      at (101,{\y-4}) {\desc};
  }

  % 原则
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.3}\selectfont\bfseries]
    at (0,37) {档案放行与移交铁律};
  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,29);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.2}{7.4}\selectfont\bfseries]
    at (7,20) {RELEASE CONTROL};
  \node[anchor=west,text=white,font=\fontsize{9}{10.5}\selectfont\bfseries]
    at (7,10) {严格检验 → 数据完整 → 逐级签章 → 全程可溯};
  \node[anchor=east,text=white!70!gray,font=\fontsize{6.1}{7.3}\selectfont]
    at (179,20) {唯一生效版本 • 数字化云端永久存储};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_31 = r"""% ============================================================
% TRANG 31: NỀN TẢNG PHÁP LÝ VÀ HỆ QUẢN TRỊ
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{法定资质、管理体系与履约能力}{第31页}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{随时响应严格资审的法定资质与治理体系}{Corporate identity • Construction capability • ISO systems • Key-person credentials}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);
  \node[anchor=west,text=TTCBlue,font=\fontsize{15}{17}\selectfont\bfseries]
    at (0,211) {透明可核验的企业法人身份与四类资审资料};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{7.2}{8.8}\selectfont]
    at (0,201) {企业法人信息、建设活动能力二级证书及 ISO 管理体系资料可按资审要求提供。};

  % 企业基本信息
  \fill[TTCDeepNavy,rounded corners=4pt] (0,57) rectangle (67,191);
  \node[anchor=west,text=TTCCyan,font=\fontsize{7}{8.3}\selectfont\bfseries]
    at (7,182) {CORPORATE IDENTITY};
  \node[anchor=north west,text width=53mm,text=white,
        font=\fontsize{12}{14}\selectfont\bfseries]
    at (7,169) {新成功建筑科技\\股份公司};
  \draw[white!20!gray] (7,135) -- (60,135);
  \node[anchor=north west,text width=53mm,text=white!82!gray,
        font=\fontsize{6.5}{8.2}\selectfont]
    at (7,126) {\textbf{简称：} TTC JSC\\[2mm]
                 \textbf{税号：} 0107090447\\[2mm]
                 \textbf{总部：} Hà Nội, Việt Nam\\[2mm]
                 \textbf{核心业务：} 工业建筑EPC总承包、PEB钢结构制造安装、机电MEP及综合项目管理};
  \fill[TTCRed,rounded corners=2pt] (7,67) rectangle (60,82);
  \node[text=white,font=\fontsize{7}{8.2}\selectfont\bfseries] at (33.5,74.5)
    {合规 • 可溯 • 随时投标};

  % 4层能力
  \foreach \y/\n/\title/\desc in {
    166/01/建设活动能力二级证书/业务范围以当前有效证书为准；受控副本随法定资质卷宗提供。,
    134/02/ISO 国际三体系认证/ISO 9001 质量 • ISO 14001 环境 • ISO 45001 职业安全健康国际认证齐全。,
    102/03/核心技术管理团队/项目负责人、结构工程师及安全管理人员资料按资审要求提供。,
    70/04/商务与资信证明材料/营业执照 • 完税资料 • 银行与保函资料 • 标准投标卷宗。}
  {
    \fill[white,rounded corners=3pt] (73,{\y-13}) rectangle (186,{\y+13});
    \draw[TTCBorder,rounded corners=3pt] (73,{\y-13}) rectangle (186,{\y+13});
    \fill[TTCLightBlue,rounded corners=2pt] (79,{\y-7}) rectangle (94,{\y+7});
    \node[text=TTCRed,font=\fontsize{7}{8}\selectfont\bfseries] at (86.5,\y) {\n};
    \node[anchor=west,text=TTCBlue,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
      at (101,{\y+5}) {\title};
    \node[anchor=north west,text width=76mm,text=TTCTextMuted,
          font=\fontsize{6.1}{7.4}\selectfont] at (101,{\y-1}) {\desc};
  }

  % 索引
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.3}\selectfont\bfseries]
    at (0,46) {资审与投标文件标准核验清单 (PRE-QUALIFICATION)};
  \foreach \xa/\xb/\label in {
    0/34/法人资格,
    38/72/施工资质,
    76/110/ISO体系,
    114/148/人员证书,
    152/186/财务资信}
  {
    \fill[TTCLightBlue,rounded corners=2pt] (\xa,20) rectangle (\xb,38);
    \node[text=TTCBlue,font=\fontsize{6.6}{7.8}\selectfont\bfseries]
      at ({(\xa+\xb)/2},29) {\label};
  }
  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,12);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.2}{7.4}\selectfont\bfseries] at (7,6) {DUE DILIGENCE};
  \node[anchor=east,text=white,font=\fontsize{7}{8.3}\selectfont\bfseries]
    at (179,6) {索引清晰 • 受控副本 • 快速响应跨国背调};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_32 = r"""% ============================================================
% TRANG 32: BẢN ĐỒ HIỆN DIỆN DỰ ÁN
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{全国重点工业走廊业务布局图}{第32页}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{深耕越南核心经济带三大重点工业走廊}{Northern manufacturing belt • Central corridor • Southern industrial and logistics cluster}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);
  \node[anchor=west,text=TTCBlue,font=\fontsize{15}{17}\selectfont\bfseries]
    at (0,211) {TTC 在越南全境的工业项目分布版图};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{7.2}{8.8}\selectfont]
    at (0,201) {业务重点辐射北部高科技制造圈、中部经济走廊及南部外资与现代物流基地。};

  % 地图
  \fill[white,rounded corners=4pt] (0,24) rectangle (103,191);
  \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (0,24) rectangle (103,191);
  \node[inner sep=0pt] at (51.5,107.5)
    {\includegraphics[height=164mm,trim=150 10 150 10,clip]{../../public/project-assets/vietnam-provinces.pdf}};

  % 圈注
  \fill[TTCRed,opacity=.16] (62,151) circle (12mm);
  \draw[TTCRed,line width=1pt] (62,151) circle (6mm);
  \fill[TTCRed] (62,151) circle (2.2mm);
  \node[anchor=west,text=TTCRed,font=\fontsize{6.5}{7.6}\selectfont\bfseries] at (70,157) {北部制造集群};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{5.5}{6.6}\selectfont] at (70,150) {河内 • 永福 • 北宁 • 北江};

  \fill[TTCBlue,opacity=.14] (62,94) circle (10mm);
  \draw[TTCBlue,line width=1pt] (62,94) circle (5mm);
  \fill[TTCBlue] (62,94) circle (2mm);
  \node[anchor=west,text=TTCBlue,font=\fontsize{6.5}{7.6}\selectfont\bfseries] at (69,100) {中部工业走廊};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{5.5}{6.6}\selectfont] at (69,93) {岘港 • 广南 • 沿海经济区};

  \fill[TTCCyan,opacity=.16] (51,51) circle (10mm);
  \draw[TTCCyan,line width=1pt] (51,51) circle (5mm);
  \fill[TTCCyan] (51,51) circle (2mm);
  \node[anchor=west,text=TTCBlue,font=\fontsize{6.5}{7.6}\selectfont\bfseries] at (59,57) {南部外资集群};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{5.5}{6.6}\selectfont] at (59,50) {平阳 • 胡志明市 • 后江};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{4.8}{5.8}\selectfont]
    at (5,29) {地图数据参考 CC0: Wikimedia Commons / Thomson Walt};

  % 右侧说明
  \fill[TTCDeepNavy,rounded corners=4pt] (109,133) rectangle (186,191);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.2}{7.4}\selectfont\bfseries]
    at (116,183) {01 • 核心根据地};
  \node[anchor=north west,text width=62mm,text=white,
        font=\fontsize{9.5}{11}\selectfont\bfseries] at (116,173) {北部重工业与电子制造带};
  \node[anchor=north west,text width=62mm,text=white!75!gray,
        font=\fontsize{6.2}{7.6}\selectfont] at (116,153) {工程密度集中于河内、永福、北宁、北江、海阳、海防与南定等各大国家级工业园区。};

  \fill[TTCLightBlue,rounded corners=4pt] (109,73) rectangle (186,127);
  \node[anchor=west,text=TTCRed,font=\fontsize{6.2}{7.4}\selectfont\bfseries]
    at (116,119) {02 • 快速机动调配};
  \node[anchor=north west,text width=62mm,text=TTCBlue,
        font=\fontsize{8.5}{10}\selectfont\bfseries] at (116,109) {跨区域项目团队保障};
  \node[anchor=north west,text width=62mm,text=TTCTextMuted,
        font=\fontsize{6.2}{7.6}\selectfont] at (116,92) {依据项目群设常驻工程总监、QA/QC与HSE工程师，重型机械装备按工序精准调度。};

  \fill[white,rounded corners=4pt] (109,24) rectangle (186,67);
  \draw[TTCBorder,rounded corners=4pt] (109,24) rectangle (186,67);
  \node[anchor=west,text=TTCBlue,font=\fontsize{6.2}{7.4}\selectfont\bfseries]
    at (116,59) {03 • 重点拓展方向};
  \node[anchor=north west,text width=62mm,text=TTCTextDark,
        font=\fontsize{6.3}{7.7}\selectfont] at (116,49) {有选择性地扩大中部及南部高端工业市场，重点服务跨国大型EPC外资厂房及冷链智慧物流基地。};

  \fill[TTCDeepNavy,rounded corners=3pt] (109,0) rectangle (186,16);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.1}{7.2}\selectfont\bfseries]
    at (116,8) {PROJECT FOOTPRINT};
  \node[anchor=east,text=white,font=\fontsize{6.5}{7.7}\selectfont\bfseries]
    at (179,8) {三大项目走廊 • 按项目调配资源};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_33 = r"""% ============================================================
% TRANG 33: LỘ TRÌNH 2026--2030
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{2026--2030 受控发展与能力建设路线图}{第33页}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{精选适配工程 • 稳健建设交付能力}{Controlled growth • Repeat clients • High-tech capability • Delivery discipline}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);
  \node[anchor=west,text=TTCBlue,font=\fontsize{15}{17}\selectfont\bfseries]
    at (0,211) {以健全稳健的治理能力驱动业务规模高质量增长};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{7.2}{8.8}\selectfont]
    at (0,201) {坚持审慎务实的经营方针，以治理、专业能力与高品质交付支持可持续发展。};

  % 3个发展阶段
  \foreach \xa/\xb/\year/\value/\focus/\desc in {
    0/58/2026年/标准化/夯实治理底座/完善CDE协同 • 强化成本基线 • 深耕核心项目走廊,
    64/122/2027--2028年/精选/提升专业能力/发展洁净厂房与高科技工程能力 • 服务长期客户,
    128/186/2029--2030年/可持续/审慎拓展布局/依据资源与履约能力拓展重点区域 • 建设绿色供应链}
  {
    \fill[white,rounded corners=4pt] (\xa,68) rectangle (\xb,190);
    \draw[TTCBorder,rounded corners=4pt,line width=.7pt] (\xa,68) rectangle (\xb,190);
    \fill[TTCDeepNavy,rounded corners=4pt] (\xa,165) rectangle (\xb,190);
    \node[anchor=west,text=TTCCyan,font=\fontsize{7}{8.3}\selectfont\bfseries]
      at ({\xa+6},181) {\year};
    \node[anchor=west,text=white,font=\fontsize{13}{15}\selectfont\bfseries]
      at ({\xa+6},171) {\value};
    \fill[TTCRed] ({\xa+6},153) rectangle ({\xa+22},155);
    \node[anchor=west,text=TTCBlue,font=\fontsize{7.6}{9}\selectfont\bfseries]
      at ({\xa+6},143) {\focus};
    \node[anchor=north west,text width=46mm,text=TTCTextMuted,
          font=\fontsize{6.3}{7.7}\selectfont] at ({\xa+6},133) {\desc};
    \node[anchor=south west,text width=46mm,text=TTCTextDark,
          font=\fontsize{6.1}{7.5}\selectfont] at ({\xa+6},78)
      {\textbf{阶段评审重点：} 治理成熟度、专业团队、合同风险与交付能力。};
  }

  % 亮点
  \foreach \y/\label in {116/CDE 协同平台,104/严控成本基线,92/深耕北部根据地}{
    \fill[TTCRed] (6,\y) circle (1.2mm);
    \node[anchor=west,text=TTCTextDark,font=\fontsize{6.2}{7.4}\selectfont] at (11,\y) {\label};
  }
  \foreach \y/\label in {116/洁净室与高科技,104/老客户高复购率,92/多项目协同管控}{
    \fill[TTCRed] (70,\y) circle (1.2mm);
    \node[anchor=west,text=TTCTextDark,font=\fontsize{6.2}{7.4}\selectfont] at (75,\y) {\label};
  }
  \foreach \y/\label in {116/精选优质 EPC,104/审慎跨区布局,92/绿色低碳供应链}{
    \fill[TTCRed] (134,\y) circle (1.2mm);
    \node[anchor=west,text=TTCTextDark,font=\fontsize{6.2}{7.4}\selectfont] at (139,\y) {\label};
  }

  % 4道筛选机制
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.3}\selectfont\bfseries]
    at (0,57) {项目承接四大内控筛选准入原则};
  \foreach \xa/\xb/\n/\label in {
    0/43.5/01/业务范围适配,
    47.5/91/02/核心团队就绪,
    95/138.5/03/合同法律风险锁定,
    142.5/186/04/履约能力核验}
  {
    \fill[TTCLightBlue,rounded corners=3pt] (\xa,25) rectangle (\xb,49);
    \node[anchor=west,text=TTCRed,font=\fontsize{6}{7}\selectfont\bfseries]
      at ({\xa+5},40) {\n};
    \node[anchor=west,text=TTCBlue,font=\fontsize{6.2}{7.4}\selectfont\bfseries]
      at ({\xa+5},32) {\label};
  }
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{5.4}{6.5}\selectfont\itshape]
    at (0,14) {注：本页为方向性能力建设路线，具体计划以公司年度审批文件为准。};
  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,10);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6}{7.2}\selectfont\bfseries] at (7,5) {CONTROLLED GROWTH};
  \node[anchor=east,text=white,font=\fontsize{6.8}{8}\selectfont\bfseries]
    at (179,5) {专业能力 • 合同纪律 • 可持续交付};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_34 = r"""% ============================================================
% TRANG 34: BẢO HÀNH VÀ HẬU MÃI
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{按合同约定的保修与售后支持}{第34页}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{单一窗口售后维保支持}{Centralized intake • Contract-based response • Field verification • Closed-loop records}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);
  \node[anchor=west,text=TTCBlue,font=\fontsize{15}{17}\selectfont\bfseries]
    at (0,211) {工程交付并非终点 — 而是长期伙伴合作的新起点};
  \node[anchor=west,text=TTCTextMuted,font=\fontsize{7.2}{8.8}\selectfont]
    at (0,201) {竣工后所有维保需求均由专职售后工程团队统一受理、精准处置与闭环归档。};

  % 合同约定承诺
  \fill[TTCDeepNavy,rounded corners=4pt] (0,141) rectangle (54,190);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.4}{7.6}\selectfont\bfseries]
    at (7,181) {保修服务依据};
  \node[anchor=west,text=white,font=\fontsize{23}{25}\selectfont\bfseries]
    at (7,162) {合同约定};
  \node[anchor=west,text=white!72!gray,font=\fontsize{5.9}{7.1}\selectfont]
    at (7,149) {范围与期限以签署文件为准};

  \fill[TTCLightBlue,rounded corners=4pt] (60,141) rectangle (186,190);
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.3}\selectfont\bfseries]
    at (67,181) {单一维保责任窗口 — 闭环追踪处理记录};
  \node[anchor=north west,text width=104mm,text=TTCTextDark,
        font=\fontsize{6.7}{8.2}\selectfont] at (67,171)
    {由统一联络窗口登记维保需求。团队依据合同约定、问题等级及现场条件安排技术评估与处置。};
  \node[anchor=west,text=TTCRed,font=\fontsize{6.4}{7.6}\selectfont\bfseries]
    at (67,149) {责任清晰 • 过程留痕 • 业主确认后闭环归档};

  % 流程
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.3}\selectfont\bfseries]
    at (0,130) {标准化售后维保闭环服务流程};
  \foreach \xa/\xb/\n/\title/\desc in {
    0/42/01/工单受理/登记现场情况 • 影响程度与照片,
    48/90/02/定级分派/界定保修范围与紧急响应等级,
    96/138/03/现场处置/工程技术人员现场排查与维修施工,
    144/186/04/签字闭环/业主验收合格 • 归入工程运维档案}
  {
    \fill[white,rounded corners=3pt] (\xa,78) rectangle (\xb,121);
    \draw[TTCBorder,rounded corners=3pt] (\xa,78) rectangle (\xb,121);
    \fill[TTCRed,rounded corners=1pt] ({\xa+5},109) rectangle ({\xa+16},118);
    \node[text=white,font=\fontsize{6}{7}\selectfont\bfseries] at ({\xa+10.5},113.5) {\n};
    \node[anchor=west,text=TTCBlue,font=\fontsize{7}{8.2}\selectfont\bfseries]
      at ({\xa+5},101) {\title};
    \node[anchor=north west,text width=31mm,text=TTCTextMuted,
          font=\fontsize{5.9}{7.2}\selectfont] at ({\xa+5},94) {\desc};
  }
  \foreach \xa/\xb in {42/48,90/96,138/144}{
    \draw[-{Latex[length=2mm]},TTCBlue!65!white,line width=.8pt]
      ({\xa+1},99) -- ({\xb-1},99);
  }

  % 分项
  \node[anchor=west,text=TTCBlue,font=\fontsize{8}{9.3}\selectfont\bfseries]
    at (0,67) {保修范围严格依照合同及竣工验收纪要约定};
  \foreach \xa/\xb/\title/\desc in {
    0/58/结构工程/刚架 • 节点高强螺栓 • 基础与防腐涂层,
    64/122/围护系统/屋面防水 • 泛水板 • 天沟雨水系统 • 夹芯板,
    128/186/机电与消防/电气系统 • 暖通空调 • 消防管网与泵房}
  {
    \fill[TTCLightBlue,rounded corners=3pt] (\xa,25) rectangle (\xb,58);
    \node[anchor=west,text=TTCBlue,font=\fontsize{7.2}{8.5}\selectfont\bfseries]
      at ({\xa+6},48) {\title};
    \node[anchor=north west,text width=46mm,text=TTCTextMuted,
          font=\fontsize{6}{7.3}\selectfont] at ({\xa+6},40) {\desc};
  }
  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,16);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.1}{7.3}\selectfont\bfseries] at (7,8) {CENTRAL SERVICE DESK};
  \node[anchor=east,text=white,font=\fontsize{6.8}{8}\selectfont\bfseries]
    at (179,8) {快速接单 → 精准处置 → 业主确认 → 留痕归档};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_35 = r"""% ============================================================
% TRANG 35: HỆ SINH THÁI ĐỐI TÁC — LOGO WALL
% ============================================================
\noindent\mbox{}\par\vspace{-\baselineskip}
\casepagebars{企业、供应链与金融机构参考}{第35页}

\begin{minipage}[t][246mm]{\textwidth}
\secbrand{企业、供应链与金融机构参考}{Selected ecosystem references in the TTC network}

\noindent
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (186,220);

  \node[anchor=west,text=TTCBlue,font=\fontsize{15}{17}\selectfont\bfseries]
    at (0,211) {汇聚产业链优质资源 • 赋能工程卓越履约};
  \node[anchor=west,text width=178mm,text=TTCTextMuted,
        font=\fontsize{7.2}{8.8}\selectfont]
    at (0,199) {以下标识用于展示曾合作或业务往来的生态参考；当前关系及适用范围以最新记录为准。};

  % 企业合作伙伴
  \fill[TTCLightBlue,rounded corners=3pt] (0,177) rectangle (186,191);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.2}{7.4}\selectfont\bfseries]
    at (7,184) {CORPORATE ECOSYSTEM};
  \node[anchor=east,text=TTCBlue,font=\fontsize{7.2}{8.6}\selectfont\bfseries]
    at (179,184) {战略企业生态圈};

  \newcommand{\corporatelogoclosing}[3]{%
    \fill[white,rounded corners=3pt] (#1,#2) rectangle ({#1+43.5},{#2+31});
    \draw[TTCBorder,rounded corners=3pt,line width=.6pt]
      (#1,#2) rectangle ({#1+43.5},{#2+31});
    \fill[TTCRed] ({#1+4},{#2+25.5}) rectangle ({#1+12},{#2+27});
    \node[inner sep=0pt] at ({#1+21.75},{#2+15})
      {\includegraphics[width=29mm,height=23mm,keepaspectratio]{#3}};
  }

  \corporatelogoclosing{0}{139}{../../public/logo/Food-logo.png}
  \corporatelogoclosing{47.5}{139}{../../public/logo/aidc_logo.png}
  \corporatelogoclosing{95}{139}{../../public/logo/alo-logo.png}
  \corporatelogoclosing{142.5}{139}{../../public/logo/company-minhphu.png}
  \corporatelogoclosing{0}{103}{../../public/logo/dieuphuong-logo.png}
  \corporatelogoclosing{47.5}{103}{../../public/logo/par5.png}
  \corporatelogoclosing{95}{103}{../../public/logo/y2y.png}
  \corporatelogoclosing{142.5}{103}{../../public/logo/company-sinchi.png}

  % 银行
  \fill[TTCLightBlue,rounded corners=3pt] (0,82) rectangle (186,96);
  \node[anchor=west,text=TTCCyan,font=\fontsize{6.2}{7.4}\selectfont\bfseries]
    at (7,89) {FINANCIAL PARTNERS};
  \node[anchor=east,text=TTCBlue,font=\fontsize{7.2}{8.6}\selectfont\bfseries]
    at (179,89) {金融机构业务往来参考};

  \newcommand{\banklogoclosing}[2]{%
    \fill[white,rounded corners=3pt] (#1,39) rectangle ({#1+28.5},75);
    \draw[TTCBorder,rounded corners=3pt,line width=.55pt]
      (#1,39) rectangle ({#1+28.5},75);
    \node[inner sep=0pt] at ({#1+14.25},57)
      {\includegraphics[width=23mm,height=17mm,keepaspectratio]{#2}};
  }
  \banklogoclosing{0}{../../public/logo/bank-acb.pdf}
  \banklogoclosing{31.5}{../../public/logo/bank-tpbank.pdf}
  \banklogoclosing{63}{../../public/logo/bank-vietcombank.pdf}
  \banklogoclosing{94.5}{../../public/logo/bank-bidv.pdf}
  \banklogoclosing{126}{../../public/logo/bank-vietinbank.png}
  \banklogoclosing{157.5}{../../public/logo/bank-mb.png}

  \fill[TTCDeepNavy,rounded corners=3pt] (0,0) rectangle (186,24);
  \fill[TTCRed,rounded corners=1pt] (7,7) rectangle (9,17);
  \node[anchor=west,text=white,font=\fontsize{8.4}{10}\selectfont\bfseries]
    at (15,15) {深度协同 • 创造更大商业价值};
  \node[anchor=west,text=white!70!gray,font=\fontsize{6.1}{7.4}\selectfont]
    at (15,7) {具体合作关系、授信与供应能力须以项目阶段的有效文件核验。};
  \node[anchor=east,text=TTCCyan,font=\fontsize{6.4}{7.6}\selectfont\bfseries]
    at (179,12) {PARTNERSHIP BUILT ON TRUST};
\end{tikzpicture}
\end{minipage}
\newpage
"""

PAGE_36 = r"""% ============================================================
% TRANG 36: BÌA SAU — NHẬN DIỆN THƯƠNG HIỆU
% ============================================================
\thispagestyle{empty}
\begin{tikzpicture}[remember picture,overlay]
  \fill[TTCDeepNavy] (current page.south west) rectangle (current page.north east);
  \fill[TTCRed] (current page.north west) rectangle ([yshift=-3mm]current page.north east);
  \fill[TTCRed] (current page.south west) rectangle ([yshift=3mm]current page.south east);

  \begin{scope}[opacity=.075]
    \draw[white,line width=.8pt]
      ([xshift=16mm,yshift=122mm]current page.south west)
      -- ([xshift=16mm,yshift=146mm]current page.south west)
      -- ([xshift=52mm,yshift=168mm]current page.south west)
      -- ([xshift=88mm,yshift=146mm]current page.south west)
      -- ([xshift=124mm,yshift=178mm]current page.south west)
      -- ([xshift=158mm,yshift=146mm]current page.south west)
      -- ([xshift=194mm,yshift=166mm]current page.south west)
      -- ([xshift=194mm,yshift=122mm]current page.south west);
    \foreach \x in {28,40,64,76,100,112,136,148,172,184}{
      \draw[white,line width=.4pt]
        ([xshift=\x mm,yshift=122mm]current page.south west)
        -- ([xshift=\x mm,yshift=147mm]current page.south west);
    }
  \end{scope}
  \node[text=white,opacity=.025,font=\fontsize{92}{96}\selectfont\bfseries]
    at ([yshift=8mm]current page.center) {TTC};

  % 顶部 Logo
  \node[anchor=north west,fill=white,rounded corners=4pt,
        inner xsep=7mm,inner ysep=4mm]
    at ([xshift=17mm,yshift=-20mm]current page.north west)
    {\includegraphics[width=57mm]{../../public/logo-ttc-removebg-DNXrVdJp.png}};
  \node[anchor=north east,text=white!75!gray,font=\fontsize{6.5}{7.8}\selectfont\bfseries]
    at ([xshift=-17mm,yshift=-24mm]current page.north east) {COMPANY PROFILE • 2026};

  \node[anchor=north west,text=TTCCyan,font=\fontsize{7.5}{9}\selectfont\bfseries]
    at ([xshift=18mm,yshift=-78mm]current page.north west) {INDUSTRIAL DESIGN • BUILD • DELIVERY};
  \node[anchor=north west,text width=174mm,text=white,
        font=\fontsize{28}{31}\selectfont\bfseries]
    at ([xshift=18mm,yshift=-94mm]current page.north west)
    {携手共建 • 赋能卓越};
  \fill[TTCRed] ([xshift=18mm,yshift=-164mm]current page.north west)
    rectangle ([xshift=60mm,yshift=-167mm]current page.north west);
  \node[anchor=north west,text width=170mm,text=white!78!gray,
        font=\fontsize{8.2}{10.6}\selectfont]
    at ([xshift=18mm,yshift=-178mm]current page.north west)
    {新成功建筑科技股份公司（TTC JSC）愿从投资策划、工程设计、施工总包到合同约定的售后支持，全程服务您在越南的工业项目。};

  % 底部联系卡片
  \fill[white,rounded corners=5pt]
    ([xshift=17mm,yshift=25mm]current page.south west)
    rectangle ([xshift=-17mm,yshift=104mm]current page.south east);
  \node[anchor=north west,text=TTCBlue,font=\fontsize{9.2}{11}\selectfont\bfseries]
    at ([xshift=26mm,yshift=94mm]current page.south west)
    {新成功建筑科技股份公司};
  \node[anchor=north west,text=TTCTextMuted,font=\fontsize{5.8}{7}\selectfont\bfseries]
    at ([xshift=26mm,yshift=83mm]current page.south west)
    {TAN THANH CONG TECHNOLOGY CONSTRUCTION JOINT STOCK COMPANY};
  \draw[TTCBorder,line width=.6pt]
    ([xshift=26mm,yshift=75mm]current page.south west)
    -- ([xshift=-26mm,yshift=75mm]current page.south east);

  \node[anchor=north west,text width=148mm,text=TTCTextDark,
        font=\fontsize{7}{9.2}\selectfont]
    at ([xshift=26mm,yshift=69mm]current page.south west)
    {\textcolor{TTCRed}{\faMapMarker*}\quad
     \textbf{注册地址：} Số 39, ngõ 292 Kim Giang, Đại Kim, Hà Nội\\[2.3mm]
     \textcolor{TTCRed}{\faBuilding}\quad
     \textbf{商务办公：} Số 19N7B, KĐT Trung Hòa Nhân Chính, Hà Nội\\[2.3mm]
     \textcolor{TTCRed}{\faPhone*}\quad +84 976 447 766
     \hspace{12mm}\textcolor{TTCRed}{\faEnvelope}\quad info@tanthanhcongjsc.com
     \hspace{12mm}\textcolor{TTCRed}{\faGlobe}\quad tanthanhcongjsc.com};

  \node[anchor=south west,text=white!65!gray,font=\fontsize{5.6}{6.8}\selectfont]
    at ([xshift=17mm,yshift=8mm]current page.south west)
    {\textcopyright\ 2026 新成功建筑科技股份公司 (TTC JSC)};
  \node[anchor=south east,text=TTCCyan,font=\fontsize{6.2}{7.4}\selectfont\bfseries]
    at ([xshift=-17mm,yshift=8mm]current page.south east)
    {TANTHANHCONGJSC.COM};
\end{tikzpicture}
"""

print("Section Closing (Pages 28-36) Chinese version loaded successfully.")
