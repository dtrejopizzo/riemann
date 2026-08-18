# 108.04 -- Is 107_240 Theorem C resolved? A split verdict, in its own style

## 0. The question, precisely

107_240 Theorem C: the map \(f\mapsto D_f\) (on \(C_c((0,\infty))\)) is
injective, so the subspace of *locally* principal DC divisors is
\(\{0\}\). Its consequence, quoted verbatim: "there are no nontrivial local
principal directions to be invariant under. Principal invariance
therefore cannot be established, tested, or even stated on the universal
positive chart. It is entirely a statement about global rational functions
on the quotient topos" -- which 107_237 SS2 records as not constructed.

108_00 SS5.108.04 asks: with 108.03's graded sheaf in hand, is the
**global** principal subspace nonzero, and does that resolve the
not-well-posedness? Per instruction, this note establishes well-posedness
only; it does not test principal invariance.

Following 107_240's own method (its SS0: "one half is automatic, one half
is not merely unproved but not yet well posed"), the candid answer here is
again a split -- not the unconditional "yes" that 108_00's phrasing might
suggest, and the extra structure below is not something 108_00 anticipated.

## 1. What is resolved: existence of a nonzero global principal subspace

### Theorem 1.1

\(\operatorname{Prin}(\mathcal G)=\mathbb R\cdot\operatorname{div}(U_0)\)
(108.03 Definition 6.1, Theorem 6.2) is a well-defined, explicit,
one-dimensional, **nonzero** subspace of currents on the universal positive
chart, constructed without reference to any zero of \(\xi\), Li
coefficient, or Weil-form sign.

This is not a re-assertion of 108.03; it is the fact 108.03 established,
restated here as input.

### Corollary 1.2 (the mechanism behind Theorem C's negative clause no longer applies verbatim)

107_240 Theorem C's proof is: \(f\mapsto D_f\) injective on \(C_c\)
\(\Rightarrow\) the only \(f\) with \(D_f=0\) is \(f=0\)
\(\Rightarrow\) no nonzero \(f\in C_c\) is "principal" in any sense that
could act nontrivially, so there is nothing to test invariance against.

This proof is about \(C_c\) alone; 108.03's \(U_0\) is not an element of
that category (108.02 Theorem 4.1: character covariance excludes compact
support). So Corollary 1.2 does not contradict Theorem C -- it exhibits a
strictly larger category (the graded family \(\mathcal G\)) in which the
analogous injectivity (108.03 Proposition 5.2) does *not* force the
principal subspace to vanish, because \(\mathcal G\) contains an object,
\(U_0\), that is genuinely weight-\(0\) (Frobenius-invariant) and nonzero.
Theorem C's \(\{0\}\) conclusion is therefore a fact about the category
\(C_c\), not an intrinsic obstruction; 108.03 changes the category.

**In this precise sense**, the question 107_240 SS3 declared "not even
[able to be] stated on the universal positive chart" now has a concrete,
nonzero, named term to state it about: SS1 of this note settles the
existence half.

## 2. What is not resolved: whether the invariance statement is formulable against \(I_\partial\)

Testing "principal invariance" means asking whether

\[
 I_\partial(D+P,E)=I_\partial(D,E)
 \qquad\text{for }P\in\operatorname{Prin}(\mathcal G),
 \tag{2.1}
\]

is true. Formulating (2.1) at all requires \(I_\partial\) to accept
\(P=c\cdot\operatorname{div}(U_0)\) as an input.

### Proposition 2.1 (the domain gap)

\(I_\partial(D_f,D_g):=\mathfrak T(f\star\widetilde g)\) (107_239 Definition
4.1) is defined through the finite-part trace \(\mathfrak T_S(h)\) of
107_239 (1.4), stated there **only for compactly supported test \(h\)**
(107_239 SS1: "For a compactly supported test \(h\)..."; SS3 stabilizes the
place set \(S\) precisely because \(\operatorname{supp}h\) is assumed
bounded). \(U_0\)'s generating test function is \(f_0(r)\equiv1\)
(108.02 SS4, \(s=0\)), which is not compactly supported.

**Consequence.** \(I_\partial(D,\,c\cdot\operatorname{div}(U_0))\) is not
covered by the published definition. (2.1) is not yet a well-formed
statement, let alone a provable or disprovable one.

This is a genuine finding of this note, not a restatement of 107_240: it is
a *second* well-posedness gap, one level up from Theorem C's. Theorem C's
gap was "no nonzero object exists to test against"; the gap identified here
is "an object now exists, but the pairing that would need to consume it is
not defined on it." Closing it would require extending \(\mathfrak T_S\)
(most plausibly via a further finite-part/renormalization construction in
the spirit of the \(-2h(1)\log\Lambda\) subtraction already used in 107_239
(1.4), which exists precisely to tame a divergence) to non-compactly
supported \(h\) of power-law type. No such extension is attempted here; per
108_00 SS5, principal invariance is explicitly not to be tested in this
note, and this proposition shows why attempting it immediately would be
premature: the statement is not yet formed.

## 3. Verdict

\[
 \boxed{\texttt{GLOBAL\_PRINCIPAL\_SUBSPACE\_NONZERO: YES (Theorem 1.1)}}
\]
\[
 \boxed{\texttt{THEOREM\_C\_EXISTENCE\_GAP: RESOLVED\_IN\_GRADED\_CATEGORY}}
\]
\[
 \boxed{\texttt{PRINCIPAL\_INVARIANCE\_STATEMENT\_WELL\_FORMED: NO
 (Proposition 2.1)}}
\]
\[
 \boxed{\texttt{PRINCIPAL\_INVARIANCE\_TESTED: NOT\_ATTEMPTED, PER SCOPE}}
\]

108_00 SS5's conditional ("if yes [nonzero], the question... becomes well
posed, and principal invariance becomes testable for the first time") is
correct about *existence* and premature about *testability*: a nonzero
witness now exists, but "testable" additionally requires the pairing's
domain to include it, which it currently does not. This refinement is the
substantive content of this note, beyond simply reporting 108.03's result.

## 4. What this changes, and what it does not

Changes:

* the specific proof mechanism of 107_240 Theorem C ("no nontrivial local
  principal directions") no longer forces vacuity once the graded category
  \(\mathcal G\) is admitted;
* there is now a named, explicit, zero-free-constructed candidate
  \(\operatorname{Prin}(\mathcal G)\) for future work to test against, once
  \(I_\partial\) is extended.

Does not change:

* `ROW_A_STATUS`, which remains `partial`;
* 107_240's own content, which is about the category \(C_c\) and is not
  contradicted;
* the numerical quotient of 107_240 SS5 / 107_241, which is untouched by
  this note (108.10 audits it directly).

## 5. Scope

Proved here:

* Corollary 1.2: the graded category strictly enlarges the category in
  which Theorem C's vacuity argument was stated, and contains a nonzero
  principal witness;
* Proposition 2.1: \(I_\partial\) as published does not accept that
  witness as an input, so principal invariance is not yet a well-formed
  statement, only a well-defined *object*.

Not established, and not attempted:

* any extension of \(\mathfrak T_S\)/\(I_\partial\) to non-compactly
  supported test data;
* whether \(P\subseteq\operatorname{rad}I_\partial\) once such an extension
  exists;
* any change to the status of row (a).

## 6. Verifier

`108_04_well_posedness_verdict.py`:

1. re-derives (does not merely quote) that \(f_0\equiv1\) is not
   compactly supported and that 107_239's stabilization argument (SS3,
   finiteness of contributing primes for \(\operatorname{supp}h\subset
   [e^{-T},e^T]\)) fails to apply to it, by checking that no finite \(T\)
   contains the support of a nonzero constant function;
* checks the analogous statement for every \(f_s\), \(s\in\mathbb R\)
  (108.03's whole graded family), confirming the domain gap is generic
  to \(\mathcal G\), not an accident of \(s=0\);
2. confirms Theorem 1.1's numeric witness (imports the same explicit
   density check as 108.03) independently, to keep this document
   self-checking;
3. prints the four boxed verdict lines and `VERDICT: SPLIT` (this is the
   correct outcome, not a failure: existence is resolved, formulability of
   the invariance statement is not).
