# 114.a.139 — I7 scope: decorated dynamics is closed; integration is open

~~~
+------------------------------------------------------------------------+
| CONTRACT    Row a requires Div/Prin, principal invariance, product       |
|             growth and a pairing; it does not say ordinary Chow only.    |
| HAVE        Picard-decorated diagonal spans Gamma_n compose faithfully.  |
| HAVE        Their monoidal contact shadow has mass Lambda(n).             |
| MISSING     A functor into the same divisor/intersection theory used by   |
|             G-7, with contact equal to geometric diagonal intersection.   |
| OPTIONAL    An undecorated Chow representative is one possible upgrade,  |
|             not a separately stated row-a axiom.                          |
+------------------------------------------------------------------------+
~~~

## 1. Compare with the authoritative contract

The row-a contract audited in a10 consists of:

1. a divisor group and principal subgroup;
2. principal invariance;
3. curve-like fixed-rank dimension;
4. a product with quadratic growth;
5. a working graded pairing.

It does not require that every correspondence be represented by an ordinary
integral Chow cycle. Algebraic cycles are the classical model, but a
bivariant, K-theoretic or derived kernel theory can satisfy the same five
requirements if all operations and comparisons are constructed.

## 2. What I7 already has

The construction a70 gives a genuine category of spans decorated by
\(GL_1(\mathcal O)\)-torsors:

\[
 \Gamma_n=(X\xleftarrow{\rm id}X\xrightarrow{\rm id}X;T_n),
\qquad
 \Gamma_m\circ\Gamma_n\simeq\Gamma_{mn}.                              \tag{2.1}
\]

The family is faithful because \(T_n\) is faithful. Its symmetric monoidal
contact functor satisfies

\[
 \operatorname{Cont}(\Gamma_n)=\mathcal P_n,\qquad
 \log\#\Gamma\mathcal P_n=\Lambda(n).                                \tag{2.2}
\]

Thus the abstract dynamic and arithmetic-contact portions of I7 are closed:

> **I7-DYN-TOR:** closed positively.

The no-go a133 only says that the decoration cannot be replaced by a
multiplicity \(k(n)\Delta\) in an ordinary diagonal-supported Chow group.
It does not invalidate (2.1)--(2.2).

## 3. The actual missing compatibility

Neither a70 nor the row-a contract permits assigning (2.2) as an
intersection by declaration. One still needs a comparison

\[
 \mathfrak I:\operatorname{Corr}_{Pic}(X,X)
 \longrightarrow \mathcal C_{G7}(Y)                                  \tag{3.1}
\]

into the same divisor, bivariant or derived category on \(Y^{locreg}\) in
which:

1. \(\mathfrak I(\Gamma_m\circ\Gamma_n)\) is convolution-compatible;
2. the underlying torsor agrees with the prime classes in
   \(D_1^{cmp}/Pic_{cmp}\);
3. the canonical reduced retract of derived diagonal pullback is the
   already constructed \(\mathcal P_n\), including mixed-prime zero, and
   the pairing either factors through that projector or accounts for the
   complementary excess;
4. the reduced local degree is therefore \(\Lambda(n)\), as a theorem
   rather than an assigned shadow;
5. the global RR/Green pairing and principal equivalence act on the same
   objects.

Call this conjunction **H7-DYN-INTEGRATE**.

### Proposition 3.1

H7-DYN-INTEGRATE is sufficient for the I7 contribution required by a1, a2
and a5. An undecorated Chow lift is not additionally necessary unless the
chosen final category is required, as an extra convention, to be ordinary
Chow.

The proof is the list above: (2.1) supplies composition, items 2 and 5 place
the kernels in the unified divisor theory, and items 3--4 identify the
geometric intersection with \(\Lambda\).

## 4. Relation with the remaining routes

There are now two candid ways to prove H7-DYN-INTEGRATE:

- construct a bivariant intersection theory directly for
  Picard-decorated spans;
- prove H7-TOR-LIN from a134 and realise
  \(\Gamma_n\) as derived/module kernels.

A moving-support or thickened undecorated cycle from a133 is a third,
stronger option. The diagonal-multiplicity route is impossible.

## 5. Correct status

I7 is no longer one undifferentiated open box:

| I7 component | status |
|---|---|
| faithful multiplicative dynamics | closed in decorated spans |
| exact monoidal Lambda contact | closed |
| ordinary diagonal Chow multiples | impossible |
| integration with G-7 divisor/intersection | open: H7-DYN-INTEGRATE |

This correction does not close row A: H7-DYN-INTEGRATE and the independent
G-7 boundary/RR/Green gates remain. It only removes the unsupported claim
that an undecorated Chow representative is mandatory.

The verifier 114_a_139_i7_integration_scope_verify.py checks the monoid and
contact algebra, the a1--a5 contract markers and the scope distinction.
