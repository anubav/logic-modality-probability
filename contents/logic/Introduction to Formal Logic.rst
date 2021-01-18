*******************************
An Introduction to Formal Logic
*******************************

.. _what-is-formal-logic:

What is Formal Logic? 
=====================

Logic, in the most general sense of the term, refers to the study of
the norms that govern the activity of reasoning. In this sense, logic
comprehends not only the sort of deductive reasoning expressed in
mathematical proofs but also such inductive reasoning as may be
involved in a statistical inference or the confirmation of a
scientific theory. If we further countenance informal methods of
reasoning, the scope of logic is wider still, including even those
vague heuristics and patterns of inference summarized by the phrase
'common sense'. Given such a wide scope of application, how is the
qualifier 'formal' when prefixed to the term 'logic' meant to restrict
the domain of the inquiry?

The phrase 'formal logic' is, in fact, ambiguous, owing to the
inherent polysemy of the term 'formal', which has at least three
distinct connotations each of which will be relevant to the present
study. In the first sense of the term, 'formal' means, quite
literally: pertaining to the form of a thing as opposed to its
matter. In logic, the things that we are concerned to study are
arguments or inferences. So, in this first sense of the term, formal
logic is the study of inferences insofar as they are to be judged by
consideration of their form alone; that is, without paying any mind to
the specific subject matter with which they deal. The distinction
between argumentative form and matter is not easy to make precise and,
as we shall see, an argument's form is perhaps best viewed as being
relative to a specific system of logic, as opposed to something which
is absolute. Nevertheless, we can gain an initial grasp on the idea of
argumentative form, as it figures in the study of logic, by means a
simple example.

Consider the following argument:

.. epigraph::

   Socrates is a man. Therefore, the
   teacher of Plato was fated to die. 

This argument may be regarded as valid in the sense that the truth of
the conclusion follows from the truth of the premise offered in its
support: the eventual death of the teacher of Plato, namely Socrates,
is indeed assured by the fact of his being a man. Note, however, that
the validity of this inference is predicated on a few additional facts
which are not explicitly included as premises in the argument. For
one, it is presumed that human beings are mortal in the sense that
every man is fated to die. It is also presumed that the proper name
'Socrates' and the definite description 'the teacher of Plato' refer
to one and the same individual. While these facts may be a matter of
common knowledge, they still express material assumptions insofar as
each falls within the purview of some specialized domain of knowledge
(viz., that of human beings, in the first case, and that of Socrates,
in the second). Thus, insofar as the above argument is viewed as one
whose validity turns on the truth of such matters as pertain to human
beings or to Socrates, the question of the argument's validity cannot
be referred to the expertise of the formal logician to decide. We can,
however, render the above argument a more suitable object of logical
scrutiny by making explicit all of the material assumptions on which
the inference's validity depends:

.. epigraph::

   Socrates is a man. Every man is fated to die. Socrates is
   (identical to) the teacher of Plato. Therefore, the teacher of
   Plato was fated to die.

While more cumbersome in its phrasing, this is the sort of argument
whose validity can be affirmed by consideration of its logical form
alone. Indeed, in this course we will develop the tools needed to
underwrite just such a determination of validity. We will return to
the issue of logical form again when we introduce, in more precise
terms, the notion of semantic validity (see :ref:`semantic-validity`
below).

The second sense of 'formal' which is germane to the study of logic is
one in which 'formal' is taken to be roughly synonymous with
'official', meaning that which has been sanctioned as being in
accordance with a set of prescribed and codified rules. In this sense,
formal logic is the study of such reasoning as proceeds by means of a
sequence of inferential steps, each of which conforms to a
well-defined rule of inference. In logic, such rule-governed sequences
of inferential steps are referred to as 'proofs', so that formal
logic, in this second sense of the phrase, refers to the study of the
specific sort of reasoning which consists in providing a proof of a
conclusion from already established premises. Of course, the most
obvious intellectual context in which such formal reasoning takes
place is that of mathematics, where a proof may be supplied, for
example, to establish that a certain geometrical theorem follows from
the axioms characterizing more basic geometrical notions, such as
points, lines and the like. For this reason, mathematics has always
been an object of central concern to logicians, and some of the most
important discoveries in formal logic have emerged out of the attempt
to place mathematical reasoning on secure logical foundations. In a
later chapter, we will consider in detail proof systems that were
devised for the express purpose of validating such simple arithmetical
inferences as: 'from :math:`3x + 4y = -2` and :math:`y = 1`, it
follows that :math:`x = -2`'. There, we will see that even the attempt
to supply a precise account of the logic of such simple arithmetical
inferences gives rise to a host of deep and interesting philosophical
issues. We will return to the issue of formal proof again when we
introduce, in more precise terms, the notion of a deductive system
(see Section ??? below).

The third and final sense of the term 'formal' that will be relevant
to the present study is one in which this term is synonymous with
'mathematical', where the latter phrase is taken to function as an
adverbial modifier, indicating something about the methodology by
which the study of logic is to be pursued rather than limiting its
scope. In this case, the qualifier 'mathematical' implies,
specifically, that the methods to be used in conducting the study of
logic are themselves mathematical in nature. Thus, 'formal logic', in
this third sense of the phrase, refers not to the study of the sort of
reasoning that is done in mathematics, but rather to the study of
reasoning *done mathematically*, where the systems of reasoning that
we are concerned to investigate will themselves be represented as
mathematically well-defined structures and the claims that we will
make about these systems will be established using standard
mathematical techniques.

At this point, one may take note of an interesting interplay that
could arise between the latter two senses of the phrase formal
logic. If formal logic is, at least in part, concerned to study the
sort of reasoning that is done in mathematics and if, at the same
time, formal logic is itself just a branch of mathematics, then one
may meaningfully ask what follows when the claims established in the
study of formal logic are applied to itself. The answer, as it turns
out, is quite a lot! The essentially self-reflective nature of formal
logic is what endows the subject not only with its peculiar charm but
also with the greater part of its intrinsic philosophical value. It
allows for the precise formulation of such provocative theses as
'arithmetical truth cannot be defined arithmetically' and 'if a
computer can simulate all of our mathematical reasoning, then, in
principle, we cannot grasp how it works'. A more careful analysis of
these tantalizing claims must be deferred until later on in the
course. For now let us begin by considering in more detail how the
study of logic can be made mathematical.

.. _making-logic-mathematical:

Making Logic Mathematical 
=========================

Logic seeks to investigate the norms that govern the activity of
reasoning, or, the activity by which we are led to draw inferences. As
such, logic is concerned with questions of the following form:

* Is a given method of reasoning such as to result only in valid
  inferences, or, by employing this method, will one sometimes be led
  to draw fallacious inferences?
  
* Are there some valid inferences which, in principle, cannot be the
  result of employing a given method of reasoning, or are all such
  inferences to be judged fallacious?

In order to render such questions mathematically precise, the
following tasks must be performed:

#. 'Inferences' must be represented as mathematical objects. 
#. The standard for normative assessment by which a given inference is
   judged to be 'valid' or 'fallacious' must be expressed in terms of
   the possession by that inference of a mathematically well-defined
   property.
#. The notion of a 'method of reasoning' must be described in such a
   way that it becomes a mathematical fact whether or not a given
   inference can result from employing a given method of reasoning.

Once these three tasks have been performed, the two questions listed
above become no less mathematically well-defined than the question: is
4,753,234,127 a prime number? In this chapter, we will take up each of
these three tasks in turn.

.. _arguments:

Arguments
---------

In informal terms, an inference may be characterized as any rational
transition from one set of thoughts to another. [#rational]_ It is
natural to regard the thoughts comprising an inference as
linguistically abstract entities, distinct from the specific
propositions that may be used to express these thoughts in a given
language. Thus, for example, one may wish to allow for the possibility
that one and the same inference can be carried out in either Dutch or
Swahili, and that even in a single language, say German, the same
thought can be expressed in a variety of different ways by a variety
of syntactically distinct sentences. Nevertheless, for the purpose of
modeling inferences in mathematically precise terms, we will disregard
the intuitive difference between an abstract inference and its
concrete linguistic expression and construe inferences as purely
*syntactic* constructs. In other words, we will represent an inference
by a particular collection of grammatically well-formed sentences
expressed in a given syntax. Such syntactic representations of
inferences are referred to as 'arguments'.

An argument is as a collection of sentences in a given language, one
of which is distinguished as that for the sake of which the others are
set forth. The distinguished sentence is referred to as the argument's
*conclusion* and the sentences offered in its support as the
argument's *premises*. The specific syntax in which we will formulate
arguments will not be that of a natural language, such as English, but
will instead be that of an artificial or 'formal' language devised for
the express purpose of representing certain argument forms. We will
adopt this formal approach so as to minimize the syntactic complexity
of the arguments that we consider. The rules determining when a
sequence of symbols in the English alphabet (or a sequence of words in
the English lexicon) constitute a grammatically well-formed sentence
are exceedingly complex, and much of this complexity is unnecessary
for capturing the differences in meaning that are relevant for
assessing the particular sort of arguments with which we will be
concerned. [#passive-active]_

In each of the formal languages that we will consider, the syntax of
the language will be introduced in two distinct stages:

#. First, we will specify an *alphabet* for the language, i.e., a set
   of symbols. Any nonempty finite string of symbols from this
   alphabet will be referred to as an *expression* of the language.

#. Second, we will specify *grammatical rules* determining when a
   given expression constitutes a *sentence* of the language.

Sentences, thus defined, are purely syntactic constructs. They are
strings of symbols devoid of any meaning. Of course, our choice of the
syntax for a language will in all cases be guided by semantic
considerations. In other words, we will always have in mind a certain
conception of how various syntactic items are to be interpreted and we
will choose our syntax so as to ensure that the sentences in the
language consist only of expressions which, when given such an
interpretation, express meaningful propositions.

We are now ready to define the notion of an 'argument' in a formal
language.

.. _def-argument:

.. proof:definition::

   An *argument* in a formal language :math:`\sL` consists of (i) a
   possibly empty set of sentences of :math:`\sL`, the members of
   which are referred to as the *premises* of the argument; and (ii) a
   sentence of :math:`\sL`, referred to as the *conclusion* of the
   argument. We denote the argument with premises :math:`\Ga` and
   conclusion :math:`\ph` as follows:
   
   .. math::
      \begin{array}{c}
      \underline{\hspace{0.1in}\Gamma\hspace{0.1in}}\\
      \ph
      \end{array}

For the sake of readability, when referring to the set of premises of
an :term:`argument`, we will often omit the outer braces from the
set. Thus, for example, if :math:`\Ga` is the set of sentences
:math:`\{\psi_1,\ldots,\psi_n\}`, then the above argument may be
denoted as follows:

.. math::
   \begin{array}{c}
   \underline{\hspace{0.1in}\psi_1,\ldots,\psi_n\hspace{0.1in}}\\ \ph
   \end{array}

.. _the-formal-language-Lx:

.. topic:: Example 1 - The Formal Language :math:`\sL_\times`

	   In this example, we will devise a formal language
	   :math:`\sL_\times` suitable for expressing a very simple
	   class of arithmetical arguments, namely, those which only
	   consist of equations involving a single variable :math:`x`
	   and in which both sides of the equality are expressed as
	   the product of numbers belonging to the set
	   :math:`\{1,0\}`.

	   The alphabet for our language is given by the set of
	   symbols:

	   .. math::
	      \{x, 1, 0, \times, =\}

	   We refer to the symbols :math:`x, 1,` and :math:`0` as
	   *numerals*.

	   .. _def-numerical-expression:

	   .. proof:definition::

	      A *numerical expression* is any expression of
	      :math:`\sL_\times` which can be judged to be a numerical
	      expression on the basis of the following two facts:

	      #. Every expression consisting of a single numeral is a
		 numerical expression.

	      #. If :math:`\al` and :math:`\be` are numerical
		 expressions, then the expression :math:`\al\times\be`
		 is a numerical expression.

	   It follows from this inductive definition that the
	   numerical expressions are all and only those expressions of
	   :math:`\sL_\times` that are of the form:

	   .. math::
	      n_1 \times n_2 \times \cdots \times n_k,

	   where :math:`n_1,\ldots,n_k` are numerals.

	   The sole grammatical rule for the language
	   :math:`\sL_\times` is as follows:

	   .. epigraph::

	      An expression of :math:`\sL_\times` is a sentence of
	      :math:`\sL_\times` iff it is of the form
	      :math:`\al=\be`, where :math:`\al` and :math:`\be` are
	      numerical expressions.

	   In accordance with this rule, the following expressions are
	   all sentences of the language:

	   i. :math:`x = 0`
	   ii. :math:`1 = x`
	   iii. :math:`1 \times 0 = 0 \times 1`
	   iv. :math:`x \times x = 1`
	   v. :math:`x \times 0 \times 1 \times x = 1`
	   vi. :math:`x \times 1 \times 1 \times 1 = 1 \times x \times 0`

	   An example of an argument in the formal language
	   :math:`\sL_\times` is:

	   .. math::
	      \underline{x\times 0 = 0\times 1,\hspace{0.1in}
	      1\times x\times 1 = 1}\\ 1=x\hspace {0.7in}

	   .. _ex-expressions-Lx:

	   .. proof:exercise::

	      We refer to the number of symbols in an expression as
	      the *length* of that expression.

	      a. Show that the length of every sentence of
		 :math:`\sL_\times` is odd.
	      b. If :math:`k` is an odd number greater than 2, how
		 many distinct expressions of :math:`\sL_\times` are
		 there of length :math:`k`? How many distinct
		 sentences of :math:`\sL_\times` are there of length
		 :math:`k`?  Show that the probability with which a
		 randomly chosen expression of length :math:`k` is a
		 sentence goes to :math:`0` as :math:`k` increases.

	   .. _ex-trees-Lx:

	   .. proof:exercise::

	      A *binary tree* is a finite tree structure in which
	      every node in the tree has either exactly two direct
	      descendants (referred to as its 'left' and 'right'
	      descendant, respectively), or is a terminal node (i.e.,
	      a node with no direct descendants). Let :math:`\al` be
	      an expression of :math:`\sL_\times`. A \textit{formation
	      tree} for :math:`\al` is a binary tree the nodes of
	      which are all expressions, and for which:

	      1. The root node of the tree (i.e., the unique node with
		 no parents) is :math:`\al`.
	      2. If :math:`\be` and :math:`\ga` are the left and right
		 descendants of the node :math:`\de`, then :math:`\de`
		 is the expression :math:`\be\times\ga`.
	      3. Every terminal node is an expression consisting of a
		 single numeral.

	      For example, the following is a formation tree for the
	      expression :math:`1\times x\times 0`:

	      .. math::
	         \textrm{\synttree[$1\times x \times 0$ [$1$][$x \times 0$[$x$][$0$]]]}
	      
	      a. An expression :math:`\al` is a :term:`numerical
                 expression` iff there is a formation tree for
                 :math:`\al`, but a single :term:`numerical
                 expression` can have multiple distinct formation
                 trees. Identify three distinct formation trees for
                 the :term:`numerical expression` :math:`0\times
                 1\times x\times 0`.

	      b. Show that there are exactly

		 .. math::
		    \frac{(2k-2)!}{k!(k-1)!}=\frac{(2k-2)\cdot(2k-3)\cdots(k+1)}{(k-1)\cdot(k-2)\cdots 1}

		 distinct formation trees for any numerical expression
		 involving :math:`k` numerals.

	      c. Suppose we extend the language :math:`\sL_\times` by
                 adding to its alphabet the left and right
                 parentheses, '(' and ')'. Rewrite the definitions of
                 a :term:`numerical expression` and a formation tree
                 so as to ensure that every :term:`numerical
                 expression` has exactly one formation tree.

		 
.. _semantic-validity:

Semantic Validity
-----------------


Chapter Exercises
=================

1. We refer to the number of symbols in an expression as the *length*
   of that expression.

   a. Show that the length of every sentence of :math:`\sL_\times` is
      odd.
   b. If :math:`k` is an odd number greater than 2, how many distinct
      expressions of :math:`\sL_\times` are there of length :math:`k`?
      How many distinct sentences of :math:`\sL_\times` are there of
      length :math:`k`?  Show that the probability with which a
      randomly chosen expression of length :math:`k` is a sentence
      goes to :math:`0` as :math:`k` increases.

2. A *binary tree* is a finite tree structure in which every node in
   the tree has either exactly two direct descendants (referred to as
   its 'left' and 'right' descendant, respectively), or is a terminal
   node (i.e., a node with no direct descendants). Let :math:`\al` be
   an expression of :math:`\sL_\times`. A \textit{formation tree} for
   :math:`\al` is a binary tree the nodes of which are all
   expressions, and for which:

   1. The root node of the tree (i.e., the unique node with no
      parents) is :math:`\al`.
   2. If :math:`\be` and :math:`\ga` are the left and right
      descendants of the node :math:`\de`, then :math:`\de` is the
      expression :math:`\be\times\ga`.
   3. Every terminal node is an expression consisting of a single
      numeral.

   For example, the following is a formation tree for the expression
   :math:`1\times x\times 0`:

   .. math::
      \textrm{\synttree[$1\times x \times 0$ [$1$][$x \times 0$[$x$][$0$]]]}
	      
   a. An expression :math:`\al` is a :term:`numerical expression` iff
      there is a formation tree for :math:`\al`, but a single
      :term:`numerical expression` can have multiple distinct
      formation trees. Identify three distinct formation trees for the
      :term:`numerical expression` :math:`0\times 1\times x\times 0`.

   b. Show that there are exactly

      .. math::
	 \frac{(2k-2)!}{k!(k-1)!}=\frac{(2k-2)\cdot(2k-3)\cdots(k+1)}{(k-1)\cdot(k-2)\cdots 1}

      distinct formation trees for any numerical expression involving
      :math:`k` numerals.

   c. Suppose we extend the language :math:`\sL_\times` by adding to
      its alphabet the left and right parentheses, '(' and
      ')'. Rewrite the definitions of a :term:`numerical expression`
      and a formation tree so as to ensure that every :term:`numerical
      expression` has exactly one formation tree.


Glossary of Defined Terms
=========================

.. glossary::

   argument
       An *argument* in a formal language :math:`\sL` consists
       of (i) a possibly empty set of sentences of :math:`\sL`, the
       members of which are referred to as the *premises* of the
       argument; and (ii) a sentence of :math:`\sL`, referred to as
       the *conclusion* of the argument. We denote the argument with
       premises :math:`\Ga` and conclusion :math:`\ph` as follows:

       .. math::
	  \begin{array}{c}
	  \underline{\hspace{0.1in}\Gamma\hspace{0.1in}}\\
	  \ph
	  \end{array}

   numerical expression
       A *numerical expression* is any expression of
       :math:`\sL_\times` which can be judged to be a numerical expression
       on the basis of the following two facts:

       #. Every expression consisting of a single numeral is a
	  numerical expression.

       #. If :math:`\al` and :math:`\be` are numerical
	  expressions, then the expression :math:`\al\times\be`
	  is a numerical expression.
   
.. rubric:: Footnotes

.. [#rational]

   The requirement that the transition be rational is meant to
   indicate that the having of the antecedent thoughts from which the
   inference proceeds is what constitutes the 'ground' or 'reason' for
   the having of the consequent thought to which the inference
   leads. This requirement is thus meant to distinguish an inference
   from the mere having of a sequence of thoughts in consecution.

.. [#passive-active]

   For example, while there may be some subtle difference in meaning
   between the sentence 'John gave the letter to Mary,' and the
   sentence 'Mary was given the letter by John,' this difference in
   meaning, while relevant perhaps for producing a desired poetic
   effect, is altogether irrelevant for judging whether or not it
   follows from this claim that 'Mary was given something by
   someone'. Consequently, we can study such inferential relations
   even in a language whose grammar is not rich enough to capture the
   difference between active and passive voice constructions.
   
