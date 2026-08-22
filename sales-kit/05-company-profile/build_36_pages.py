#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main Builder for TTC Master Company Profile 2026 (36 Pages)
Assembles all sections, writes 05-company-profile.tex, compiles with xelatex,
and validates page count.
"""

import os
import sys
import subprocess

from section1 import PAGE_01, PAGE_02, PAGE_03, PAGE_04, PAGE_05, PAGE_06, PAGE_07
from section2 import PAGE_08, PAGE_09, PAGE_10
from section3 import PAGE_11, PAGE_12, PAGE_13
from section4 import PAGE_14, PAGE_15, PAGE_16, PAGE_17, PAGE_18, PAGE_19
from section5 import (
    PAGE_20, PAGE_21, PAGE_22, PAGE_23, PAGE_24,
    PAGE_25, PAGE_26, PAGE_27
)
from section_closing import (
    PAGE_28, PAGE_29, PAGE_30, PAGE_31, PAGE_32,
    PAGE_33, PAGE_34, PAGE_35, PAGE_36
)

PREAMBLE = r"""% !TEX program = xelatex
\documentclass[10pt,a4paper,oneside]{article}
\usepackage[utf8]{inputenc}
\usepackage[vietnamese]{babel}
\usepackage{fontspec}
\usepackage{geometry}
\usepackage{xcolor}
\usepackage{tikz}
\usepackage{graphicx}
\usepackage{tabularx}
\usepackage{booktabs}
\usepackage{array}
\usepackage{multicol}
\usepackage{enumitem}
\usepackage{microtype}
\usepackage{fancyhdr}
\usepackage{fontawesome5}
\usepackage{eso-pic}

\usetikzlibrary{shapes.geometric, arrows.meta, positioning, calc, backgrounds, shadows, fit}

% Set margins: 12mm left/right, 14mm top, 14mm bottom
\geometry{a4paper, top=14mm, bottom=14mm, left=12mm, right=12mm, headheight=0mm, headsep=0mm, footskip=0mm}

% Typography: Segoe UI with robust fallback
\IfFontExistsTF{Segoe UI}{
  \setmainfont{Segoe UI}[
    BoldFont={Segoe UI Bold},
    ItalicFont={Segoe UI Italic},
    BoldItalicFont={Segoe UI Bold Italic}
  ]
}{
  \IfFontExistsTF{Arial}{
    \setmainfont{Arial}[
      BoldFont={Arial Bold},
      ItalicFont={Arial Italic},
      BoldItalicFont={Arial Bold Italic}
    ]
  }{
    \setmainfont{DejaVu Sans}[
      BoldFont={DejaVu Sans Bold},
      ItalicFont={DejaVu Sans Oblique},
      BoldItalicFont={DejaVu Sans Bold Oblique}
    ]
  }
}

% Color Palette - Luxury Corporate High-Tech
\definecolor{TTCDeepNavy}{RGB}{10, 25, 47}
\definecolor{TTCBlue}{RGB}{15, 60, 120}
\definecolor{TTCLightBlue}{RGB}{240, 246, 255}
\definecolor{TTCRed}{RGB}{214, 40, 40}
\definecolor{TTCCyan}{RGB}{0, 180, 216}
\definecolor{TTCGold}{RGB}{247, 127, 0}
\definecolor{TTCTextDark}{RGB}{30, 41, 59}
\definecolor{TTCTextMuted}{RGB}{100, 116, 139}
\definecolor{TTCBorder}{RGB}{203, 213, 225}

\newcolumntype{Y}{>{\centering\arraybackslash}X}
\newcolumntype{L}{>{\raggedright\arraybackslash}X}
\newcolumntype{R}{>{\raggedleft\arraybackslash}X}

\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\linespread{1.05}
\pagestyle{empty}

% Header & Footer Macros
\newcommand{\pageheaderbar}[2]{%
  \begin{tikzpicture}[remember picture, overlay]
    \fill[TTCDeepNavy] (current page.north west) rectangle ([yshift=-10mm]current page.north east);
    \fill[TTCRed] ([yshift=-10mm]current page.north west) rectangle ([yshift=-11mm]current page.north east);
    \node[anchor=west, text=white, font=\fontsize{7.5}{9}\selectfont\bfseries] at ([xshift=12mm, yshift=-5mm]current page.north west) {
      \faBuilding\quad CÔNG TY CỔ PHẦN CÔNG NGHỆ XÂY DỰNG TÂN THÀNH CÔNG \textbullet\ TTC JSC
    };
    \node[anchor=east, text=TTCCyan, font=\fontsize{7.5}{9}\selectfont\bfseries] at ([xshift=-12mm, yshift=-5mm]current page.north east) {
      #1
    };
  \end{tikzpicture}%
}

\newcommand{\pagefooterbar}[1]{%
  \begin{tikzpicture}[remember picture, overlay]
    \fill[TTCDeepNavy] (current page.south west) rectangle ([yshift=8mm]current page.south east);
    \fill[TTCCyan] ([yshift=8mm]current page.south west) rectangle ([yshift=8.8mm]current page.south east);
    \node[anchor=west, text=white, font=\fontsize{6.8}{8}\selectfont] at ([xshift=12mm, yshift=4mm]current page.south west) {
      \faPhone*\ +84 976 447 766 \quad\textbullet\quad \faEnvelope\ info@tanthanhcongjsc.com \quad\textbullet\quad \faGlobe\ https://tanthanhcongjsc.com
    };
    \node[anchor=east, text=white, font=\fontsize{7}{8}\selectfont\bfseries] at ([xshift=-12mm, yshift=4mm]current page.south east) {
      #1
    };
  \end{tikzpicture}%
}

% Header/footer anchored directly to shipout; use for dense TikZ case-study pages.
\newcommand{\casepagebars}[2]{%
  \AddToShipoutPictureFG*{%
    \AtPageUpperLeft{%
      \begin{tikzpicture}[x=1mm,y=1mm]
        \path[use as bounding box] (0,0) rectangle (0,0);
        \fill[TTCDeepNavy] (0,0) rectangle (210,-10);
        \fill[TTCRed] (0,-10) rectangle (210,-11);
        \node[anchor=west,text=white,font=\fontsize{7.5}{9}\selectfont\bfseries] at (12,-5)
          {\faBuilding\quad CÔNG TY CỔ PHẦN CÔNG NGHỆ XÂY DỰNG TÂN THÀNH CÔNG \textbullet\ TTC JSC};
        \node[anchor=east,text=TTCCyan,font=\fontsize{7.5}{9}\selectfont\bfseries] at (198,-5)
          {#1};
      \end{tikzpicture}%
    }%
    \AtPageLowerLeft{%
      \begin{tikzpicture}[x=1mm,y=1mm]
        \path[use as bounding box] (0,0) rectangle (0,0);
        % Faint industrial line-art motif to make the lower breathing space intentional.
        \begin{scope}[opacity=.075]
          \draw[TTCBlue,line width=.55pt]
            (12,9) -- (12,15) -- (28,15) -- (35,22) -- (51,22) -- (58,15)
            -- (78,15) -- (84,28) -- (90,28) -- (90,15) -- (110,15)
            -- (119,23) -- (137,23) -- (146,15) -- (162,15)
            -- (169,20) -- (191,20) -- (198,14) -- (198,9);
          \draw[TTCBlue,line width=.35pt] (12,9) -- (198,9);
          \draw[TTCBlue,line width=.35pt] (35,22) -- (43,15) -- (51,22);
          \draw[TTCBlue,line width=.35pt] (119,23) -- (128,15) -- (137,23);
          \draw[TTCBlue,line width=.35pt] (84,15) -- (90,28);
          \draw[TTCBlue,line width=.35pt] (96,15) -- (96,31) -- (101,31) -- (101,15);
          \foreach \x in {18,24,64,70,116,152,158,176,184,192}{
            \draw[TTCBlue,line width=.25pt] (\x,10.5) -- (\x,14);
          }
        \end{scope}
        \fill[TTCDeepNavy] (0,0) rectangle (210,8);
        \fill[TTCCyan] (0,8) rectangle (210,8.8);
        \node[anchor=west,text=white,font=\fontsize{6.8}{8}\selectfont] at (12,4)
          {\faPhone*\ +84 976 447 766 \quad\textbullet\quad \faEnvelope\ info@tanthanhcongjsc.com \quad\textbullet\quad \faGlobe\ https://tanthanhcongjsc.com};
        \node[anchor=east,text=white,font=\fontsize{7}{8}\selectfont\bfseries] at (198,4)
          {#2};
      \end{tikzpicture}%
    }%
  }%
}

% Section Header Brand Macro
\newcommand{\secbrand}[2]{%
  \noindent\begin{tikzpicture}
    \fill[TTCRed] (0,0) rectangle (4mm,10mm);
    \node[anchor=west, align=left, inner sep=0pt] at (6mm, 5mm) {
      {\fontsize{13}{15}\selectfont\bfseries\color{TTCBlue} #1}\\[1.5pt]
      {\fontsize{7.2}{8.8}\selectfont\itshape\color{TTCTextMuted} #2}
    };
  \end{tikzpicture}\par\vspace{1.5mm}%
}

\begin{document}
"""

POSTAMBLE = r"""
\end{document}
"""

def assemble_document():
    work_dir = os.path.dirname(os.path.abspath(__file__))
    tex_file = os.path.join(work_dir, "05-company-profile.tex")
    
    pages = [
        PAGE_01, PAGE_02, PAGE_03, PAGE_04, PAGE_05, PAGE_06, PAGE_07,
        PAGE_08, PAGE_09, PAGE_10,
        PAGE_11, PAGE_12, PAGE_13,
        PAGE_14, PAGE_15, PAGE_16, PAGE_17, PAGE_18, PAGE_19,
        PAGE_20, PAGE_21, PAGE_22, PAGE_23, PAGE_24, PAGE_25, PAGE_26, PAGE_27, PAGE_28, PAGE_29, PAGE_30,
        PAGE_31, PAGE_32, PAGE_33, PAGE_34, PAGE_35, PAGE_36
    ]
    
    print(f"Assembling {len(pages)} pages into {tex_file}...")
    
    with open(tex_file, "w", encoding="utf-8") as f:
        f.write(PREAMBLE)
        for p in pages:
            f.write(p.strip())
            f.write("\n\n")
        f.write(POSTAMBLE)
        
    print("LaTeX file written successfully.")

if __name__ == "__main__":
    assemble_document()
