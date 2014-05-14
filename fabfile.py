from fabric.api import local

#LATEXFLAGS = " -shell-escape"
LATEXFLAGS = " "
#LATEXFLAGS = " -interaction=nonstopmode"

# LaTeX sourcecode of slides
SRC = "these"
FIGDIR = "figures"
PDFREADER = "acroread"
#LATEXMODE = "xelatex" + LATEXFLAGS
LATEXMODE = "lualatex" + LATEXFLAGS
#BIBTEX = "biblatex"
BIBTEX = "bibtex"

versions={"these": "these",
          "frontwrap": "frontwrap",
          }

#latexdiff --flatten article-mdpi-old.tex article-mdpi.tex > article-mdpi-diff.tex
#def diff(old,new,diff):
    #doc = shortcut
    #make(doc,bibtex)
    #if display:
        #preview(doc)

def make_method(name,shortcut):
    def _method(bibtex=True,display=False):
        doc = shortcut
        make(doc,bibtex)
        if display:
            preview(doc)
    return _method

for version,docname in versions.iteritems():
    globals()[version] = make_method(version,docname)


def execute(command):
  local(command)
  #local("echo %s"%command)

def move(old,new):
  command = "mv %s %s"%(old,new)
  execute(command)

def preview(chapter):
  print("previewing...")
  command = PDFREADER +" "+ chapter+".pdf"
  execute(command)

def clean():
  command = "rm -f auxiliary/* *.aux *.log *.out *.ps *.toc *.nav *.snm *.dvi *.blg *.bbl *.ccl *.nlo *.mtc* *.brf *.maf *.tdo *.psp *.spl"
  execute(command)

def make(doc,bibtex,quick=False):
    command = LATEXMODE + " --output-directory=auxiliary " + doc
    bibtexcommand = BIBTEX + " auxiliary/" + doc
    output = "auxiliary/" + doc + ".pdf"
    execute(command)
    if quick != True:
        if bibtex == True:
            execute(command)
            execute(bibtexcommand)
            execute(command)
        execute(command)
    move(output,doc+".pdf")
