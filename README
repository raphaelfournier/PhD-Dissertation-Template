# Ph.D Dissertation Thesis template

This repo contains a template for a Ph.D dissertation manuscript in Latex.
The main file is called these.tex, which can be compiled with lualatex as is
(up-to-date version on an Archlinux desktop, as of May 2014). However, it can be
greatly automated with fabric files (fabfile.py, in the main folder and in
Chapters and Appendices). these.tex make several calls to other tex files, for
header files (packages, newcommands, etc., see folder preamble) and for
chapters and appendices.

Some wrappers enable the compilation of each chapter independantly, with its
dedicated settings (for instance baselinestretch{2} if your advisor wants more
space to write/rewrite) and its own bibliography. See
Chapters/chapter1_wrapper.tex.

## Usage of FabricFiles

Install Fabric through 

    pip install fabric

Then

    fab these

in the main folder, or

    fab chapter1

in the Chapters folder. A full compilation then be performed. Some options may
be given, for instance for bibtex or for display:

    fab these:bibtex=False,display=True

All compilation files go to dedicated auxiliary folders, and which can be
cleaned with

    fab clean

## Bonus 

I used package comment to make so frame text at the end of each section, it can
also be useful to mark "working text". See \begin{brouillon} in chapter1.tex.

I also used \includegraphicsmaybe, which includes a text with missing filename in
case a graphic is missing. It's a hack, there's proably a better solution.

## Warning

Many things may be improved, everything is provided as is. For questions, drop
me a mail at raphael @ fournier-sniehotta.fr
