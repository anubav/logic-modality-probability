# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinxcontrib.katex as katex

# -- Project information -----------------------------------------------------

project = 'Logic, Modality & Probability'
copyright = '2020, Anubav Vasudevan'
author = 'Anubav Vasudevan'
release = '0.0.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.katex',
    'sphinxcontrib.proof'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of a reST role to use as the default role.
default_role = 'any'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# -- Options for LaTeX output -------------------------------------------------

latex_macros = r"""
\def \al {\alpha}
\def \Al {\Alpha}
\def \be {\beta}
\def \Ba {\Beta}
\def \ga {\gamma}
\def \Ga {\Gamma}
\def \de {\delta}
\def \De {\Delta}
\def \eps {\varepsilon}
\def \ph {\varphi}
\def \Ph {\Phi}
\def \ps {\psi}
\def \Ps {\Psi}
\def \si {\sigma}
\def \Si {\Sigma}
\def \w {\omega}
\def \W {\Omega}
\def \union {\cup}
\def \Union {\bigcup}
\def \inter {\cap}
\def \Inter {\bigcap}
\def \N {\mathbb{N}}
\def \R {\mathbb{R}}
\def \sS {\mathscr{S}}
\def \sL {\mathscr{L}}
\def \sB {\mathscr{B}}
\def \sF {\mathscr{F}}
\def \sT {\mathscr{T}}
\def \sP {\mathscr{P}}
\def \sX {\mathscr{X}}
\def \sY {\mathscr{Y}}
\def \sZ {\mathscr{Z}}
\def \vx {\vec{x}}
\def \vy {\vec{y}}
\def \vz {\vec{z}}
\def \vu {\vec{u}}
\def \vw {\vec{w}}
\def \p {\mathbf{P}}
\def \q {\mathbf{Q}}
\def \v {\mathbf{v}}
\def \f {\mathbf{f}}
\def \g {\mathbf{g}}
\def \h {\mathbf{h}}
\def \r {\mathbf{R}}
\def \s {\mathbf{S}}
\def \t {\mathbf{T}}
\def \c {\mathbf{c}}
\def \iff {\leftrightarrow}
\def \into {\rightarrow}
\def \ind {\Perp}
\def \sat {\models}
\def \proves {\vdash}
\def \peq {\dashv\vdash}
\def \nec {\Box}
\def \pos {\Diamond}
\def \true {\mathbf{T}}
\def \false {\mathbf{F}}
\def \conj {\wedge}
\def \Conj {\bigwedge}
\def \disj {\vee}
\def \Disj {\bigvee}
\def \imp {\rightarrow}
\def \M {\mathscr{M}}
"""

# Translate LaTeX macros to KaTeX and add to options for HTML builder
katex_macros = katex.latex_defs_to_katex_macros(latex_macros)
katex_options = 'macros: {' + katex_macros + '}'

# LaTeX custom theorem environments
latex_theorems = r'''
\usepackage{mathrsfs}
\usepackage{amsthm}
\usepackage{thmtools}

\declaretheoremstyle[
spaceabove=6pt, 
spacebelow=6pt,
headfont=\normalfont\bfseries,
notefont=\mdseries, 
notebraces={(}{)},
bodyfont=\normalfont,
postheadspace=1em,
]{def}

\declaretheorem[style=def, numberwithin=chapter]{definition}
\declaretheorem[style=def, numberwithin=chapter]{exercise}
'''
proof_theorem_types = {
       "algorithm": "Algorithm",
       "conjecture": "Conjecture",
       "corollary": "Corollary",
       "definition": "Definition",
       "example": "Example",
       "exercise": "Exercise", 
       "lemma": "Lemma",
       "observation": "Observation",
       "proof": "Proof",
       "property": "Property",
       "theorem": "Theorem",
    }
proof_latex_notheorem = ['proof', 'definition', 'exercise']

# This value determines the topmost sectioning unit.
latex_toplevel_sectioning = 'part'
# This value determines how to group the document tree into LaTeX source files.
latex_documents = [
    ('index', 'main.tex', r'Logic, Modality \& Probability\\ \vspace{0.3in} \huge{An Introduction to Formal Methods of Philosophical Analysis}',
     'Anubav Vasudevan', 'manual', False)
]
# A dictionary that contains LaTeX snippets overriding those Sphinx usually
# puts into the generated .tex files.
latex_elements = {
    'preamble': latex_theorems + latex_macros + r'''
\usepackage{synttree}
\makeatletter
\fancypagestyle{normal}{
    \fancyhf{}
    \fancyfoot[LE,RO]{{\py@HeaderFamily\thepage}}
    \fancyfoot[LO]{{\py@HeaderFamily\nouppercase{\rightmark}}}
    \fancyfoot[RE]{{\py@HeaderFamily\nouppercase{\leftmark}}}
    \fancyhead[LE,RO]{{\py@HeaderFamily Logic, Modality \& Probability}} 
    \renewcommand{\headrulewidth}{0.4pt}
    \renewcommand{\footrulewidth}{0.4pt}}
\makeatother
\def\sphinxtermref#1{#1}
''',
    'releasename': 'Version',
    'sphinxsetup': 'shadowsize=0pt, shadowsep=8pt, InnerLinkColor={rgb}{0,0,0}'
}
# LaTeX Options for theorem numbering using sphinxcontrib.proof
proof_latex_parent = "chapter"
