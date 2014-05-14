\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{thesisart}[2008/07/16 Articles made from thesis chapters]

\LoadClassWithOptions{article}

%\RequirePackage{thesis}

\let\chaptertitle=\title
\newcommand{\introformatting}{%
  \maketitle\bigskip
  \tableofcontents\bigskip
%  \listoftodos\bigskip
\newpage
}

\newcommand{\outroformatting}{
  \appendix
\bibliographystyle{plain}
\bibliography{../Bibliography/bibliography,../Bibliography/these}
}

\author{Rapha\"el Fournier-S'niehotta}
\date{Chapitre de th\`ese (version du \today)}
