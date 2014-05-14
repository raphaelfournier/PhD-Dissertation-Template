from fabric.api import local

LATEXFLAGS = " -shell-escape"
#LATEXFLAGS = " -interaction=nonstopmode"

# LaTeX sourcecode of slides
SRC = "these"
FIGDIR = "figures"
PDFREADER = "zathura"
#LATEXMODE = "pdflatex"+LATEXFLAGS
LATEXMODE = "lualatex"+LATEXFLAGS
BIBTEX = "bibtex"
bib = True
disp = False

# format : "<callingname>": "<documentname>",
# documentname without ".tex"
versions={"appendice1": "appendice1",
          "appendice2": "appendice2",
          }

def make_method(shortcut,name):
    def _method(bibtex=True,display=False):
        doc = name
        make(doc,bibtex)
        if display:
            preview(doc)
    return _method

for version,docname in versions.iteritems():
    globals()[version] = make_method(version,docname)

def execute(command):
  local(command)
  #local("echo %s"%command)

def move(output,chapter):
  command = "mv %s %s.pdf"%(output,chapter)
  execute(command)

def preview(chapter):
  print("previewing...")
  command = PDFREADER +" "+ chapter+".pdf"
  execute(command)

def clean():
  command = "rm -f auxiliary/* *.aux *.log *.out *.ps *.toc *.nav *.snm *.dvi *.blg *.bbl *.ccl *.nlo *.mtc* *.brf *.maf *.tdo *.psp *.spl"
  execute(command)

#def makequick(chapter):
  #command = LATEXMODE + " --output-directory=auxiliary " + chapter + "_wrapper.tex"
  #bibtexcommand = BIBTEX + " auxiliary/" + chapter + "_wrapper"
  #output = "auxiliary/" + chapter + "_wrapper" + ".pdf"
  #execute(command)
  #move(output,chapter)

def make(doc,bibtex,quick=False):
    command = LATEXMODE + " --output-directory=auxiliary " + doc + "_wrapper.tex"
    bibtexcommand = BIBTEX + " auxiliary/" + doc + "_wrapper"
    output = "auxiliary/" + doc  + "_wrapper"
    execute(command)
    if quick != True:
        if bibtex == True:
            execute(command)
            execute(bibtexcommand)
            execute(command)
        execute(command)
    move(output+".pdf",doc)
