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

unicode_substitutions = r"""
.. |Aacute| unicode:: U+000C1 .. LATIN CAPITAL LETTER A WITH ACUTE
.. |aacute| unicode:: U+000E1 .. LATIN SMALL LETTER A WITH ACUTE
.. |Acirc|  unicode:: U+000C2 .. LATIN CAPITAL LETTER A WITH CIRCUMFLEX
.. |acirc|  unicode:: U+000E2 .. LATIN SMALL LETTER A WITH CIRCUMFLEX
.. |AElig|  unicode:: U+000C6 .. LATIN CAPITAL LETTER AE
.. |aelig|  unicode:: U+000E6 .. LATIN SMALL LETTER AE
.. |Agrave| unicode:: U+000C0 .. LATIN CAPITAL LETTER A WITH GRAVE
.. |agrave| unicode:: U+000E0 .. LATIN SMALL LETTER A WITH GRAVE
.. |Aring|  unicode:: U+000C5 .. LATIN CAPITAL LETTER A WITH RING ABOVE
.. |aring|  unicode:: U+000E5 .. LATIN SMALL LETTER A WITH RING ABOVE
.. |Atilde| unicode:: U+000C3 .. LATIN CAPITAL LETTER A WITH TILDE
.. |atilde| unicode:: U+000E3 .. LATIN SMALL LETTER A WITH TILDE
.. |Auml|   unicode:: U+000C4 .. LATIN CAPITAL LETTER A WITH DIAERESIS
.. |auml|   unicode:: U+000E4 .. LATIN SMALL LETTER A WITH DIAERESIS
.. |Ccedil| unicode:: U+000C7 .. LATIN CAPITAL LETTER C WITH CEDILLA
.. |ccedil| unicode:: U+000E7 .. LATIN SMALL LETTER C WITH CEDILLA
.. |Eacute| unicode:: U+000C9 .. LATIN CAPITAL LETTER E WITH ACUTE
.. |eacute| unicode:: U+000E9 .. LATIN SMALL LETTER E WITH ACUTE
.. |Ecirc|  unicode:: U+000CA .. LATIN CAPITAL LETTER E WITH CIRCUMFLEX
.. |ecirc|  unicode:: U+000EA .. LATIN SMALL LETTER E WITH CIRCUMFLEX
.. |Egrave| unicode:: U+000C8 .. LATIN CAPITAL LETTER E WITH GRAVE
.. |egrave| unicode:: U+000E8 .. LATIN SMALL LETTER E WITH GRAVE
.. |ETH|    unicode:: U+000D0 .. LATIN CAPITAL LETTER ETH
.. |eth|    unicode:: U+000F0 .. LATIN SMALL LETTER ETH
.. |Euml|   unicode:: U+000CB .. LATIN CAPITAL LETTER E WITH DIAERESIS
.. |euml|   unicode:: U+000EB .. LATIN SMALL LETTER E WITH DIAERESIS
.. |Iacute| unicode:: U+000CD .. LATIN CAPITAL LETTER I WITH ACUTE
.. |iacute| unicode:: U+000ED .. LATIN SMALL LETTER I WITH ACUTE
.. |Icirc|  unicode:: U+000CE .. LATIN CAPITAL LETTER I WITH CIRCUMFLEX
.. |icirc|  unicode:: U+000EE .. LATIN SMALL LETTER I WITH CIRCUMFLEX
.. |Igrave| unicode:: U+000CC .. LATIN CAPITAL LETTER I WITH GRAVE
.. |igrave| unicode:: U+000EC .. LATIN SMALL LETTER I WITH GRAVE
.. |Iuml|   unicode:: U+000CF .. LATIN CAPITAL LETTER I WITH DIAERESIS
.. |iuml|   unicode:: U+000EF .. LATIN SMALL LETTER I WITH DIAERESIS
.. |Ntilde| unicode:: U+000D1 .. LATIN CAPITAL LETTER N WITH TILDE
.. |ntilde| unicode:: U+000F1 .. LATIN SMALL LETTER N WITH TILDE
.. |Oacute| unicode:: U+000D3 .. LATIN CAPITAL LETTER O WITH ACUTE
.. |oacute| unicode:: U+000F3 .. LATIN SMALL LETTER O WITH ACUTE
.. |Ocirc|  unicode:: U+000D4 .. LATIN CAPITAL LETTER O WITH CIRCUMFLEX
.. |ocirc|  unicode:: U+000F4 .. LATIN SMALL LETTER O WITH CIRCUMFLEX
.. |Ograve| unicode:: U+000D2 .. LATIN CAPITAL LETTER O WITH GRAVE
.. |ograve| unicode:: U+000F2 .. LATIN SMALL LETTER O WITH GRAVE
.. |Oslash| unicode:: U+000D8 .. LATIN CAPITAL LETTER O WITH STROKE
.. |oslash| unicode:: U+000F8 .. LATIN SMALL LETTER O WITH STROKE
.. |Otilde| unicode:: U+000D5 .. LATIN CAPITAL LETTER O WITH TILDE
.. |otilde| unicode:: U+000F5 .. LATIN SMALL LETTER O WITH TILDE
.. |Ouml|   unicode:: U+000D6 .. LATIN CAPITAL LETTER O WITH DIAERESIS
.. |ouml|   unicode:: U+000F6 .. LATIN SMALL LETTER O WITH DIAERESIS
.. |szlig|  unicode:: U+000DF .. LATIN SMALL LETTER SHARP S
.. |THORN|  unicode:: U+000DE .. LATIN CAPITAL LETTER THORN
.. |thorn|  unicode:: U+000FE .. LATIN SMALL LETTER THORN
.. |Uacute| unicode:: U+000DA .. LATIN CAPITAL LETTER U WITH ACUTE
.. |uacute| unicode:: U+000FA .. LATIN SMALL LETTER U WITH ACUTE
.. |Ucirc|  unicode:: U+000DB .. LATIN CAPITAL LETTER U WITH CIRCUMFLEX
.. |ucirc|  unicode:: U+000FB .. LATIN SMALL LETTER U WITH CIRCUMFLEX
.. |Ugrave| unicode:: U+000D9 .. LATIN CAPITAL LETTER U WITH GRAVE
.. |ugrave| unicode:: U+000F9 .. LATIN SMALL LETTER U WITH GRAVE
.. |Uuml|   unicode:: U+000DC .. LATIN CAPITAL LETTER U WITH DIAERESIS
.. |uuml|   unicode:: U+000FC .. LATIN SMALL LETTER U WITH DIAERESIS
.. |Yacute| unicode:: U+000DD .. LATIN CAPITAL LETTER Y WITH ACUTE
.. |yacute| unicode:: U+000FD .. LATIN SMALL LETTER Y WITH ACUTE
.. |yuml|   unicode:: U+000FF .. LATIN SMALL LETTER Y WITH DIAERESIS
"""

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
\def \Be {\Beta}
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

latex_substitutions = r"""
.. |al| replace:: :math:`\al`
.. |Al| replace:: :math:`\Al`
.. |be| replace:: :math:`\be`
.. |Be| replace:: :math:`\Be`
.. |ga| replace:: :math:`\ga`
.. |Ga| replace:: :math:`\Ga`
.. |de| replace:: :math:`\de`
.. |De| replace:: :math:`\De`
.. |eps| replace:: :math:`\eps`
.. |ph| replace:: :math:`\ph`
.. |Ph| replace:: :math:`\Ph`
.. |ps| replace:: :math:`\ps`
.. |Ps| replace:: :math:`\Ps`
.. |si| replace:: :math:`\si`
.. |Si| replace:: :math:`\Si`
.. |w| replace:: :math:`\w`
.. |W| replace:: :math:`\W`
.. |N| replace:: :math:`\N`
.. |R| replace:: :math:`\R`
.. |L| replace:: :math:`\sL`
.. |T| replace:: :math:`\true`
.. |F| replace:: :math:`\false`
.. |x| replace:: :math:`x`
.. |y| replace:: :math:`y`
.. |z| replace:: :math:`z`
.. |u| replace:: :math:`u`
.. |v| replace:: :math:`v`
.. |i| replace:: :math:`i`
.. |j| replace:: :math:`j`
.. |k| replace:: :math:`k`
.. |n| replace:: :math:`n`
.. |m| replace:: :math:`m`
"""

rst_prolog = unicode_substitutions + latex_substitutions

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

\declaretheorem[style=def, qed=$\square$, numberwithin=chapter]{definition}
\declaretheorem[style=def, qed=$\square$, numberwithin=chapter]{exercise}
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
\renewcommand{\qedsymbol}{$\blacksquare$}
''',
    'releasename': 'Version',
    'sphinxsetup': 'shadowsize=0pt, shadowsep=8pt, InnerLinkColor={rgb}{0,0,0}'
}
# LaTeX Options for theorem numbering using sphinxcontrib.proof
proof_latex_parent = "chapter"


