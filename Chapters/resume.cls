\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{thesisart}[2008/07/16 Articles made from thesis chapters]

\LoadClassWithOptions{article}

%\RequirePackage{thesis}

\let\chaptertitle=\title
\newcommand{\introformatting}{%
}

\let\mySection\section
\renewcommand\section{\newpage\mySection}
\newcommand{\outroformatting}{
}
\author{Rapha\"el Fournier}
\date{}
\pagestyle{empty}
