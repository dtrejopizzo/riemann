# 107.240 -- Principal invariance of the corner pairing: what holds, and where it stops

## 0. Purpose

107_239 constructs the numerical corner pairing

\[
 I_\partial(D_f,D_g)=\mathfrak T(f\star\widetilde g)=N(f\star\widetilde g)
 \tag{0.1}
\]

and leaves open its descent to a pairing on classes.  That descent needs two
statements: the DC local equations define a nonprincipal class, and the
pairing is invariant under principal divisors.

This note settles the invariance question.  The answer is a split: one half
is automatic, one half is not merely unproved but **not yet well posed**, and
the residual content is a zero-determined matching statement.

Nothing here uses a zero of \(\xi\) as an input to a definition.  Zeros enter
only in Section 4, as the description of an obstruction.

## 1. Lemma A -- unit invariance is automatic

Let \(X_S=\mathbb Z_S^\times\backslash\mathbb A_S\) and let \(\theta\) act by
\((\theta(u)\xi)(a)=\xi(u^{-1}a)\).

> **Lemma A.**  \(\theta(\gamma)=\mathrm{id}_{\mathcal H_S}\) for every
> \(\gamma\in\mathbb Z_S^\times\).  Hence \(\theta\) factors through the
> semilocal idele class group and \(\mathfrak T_S\) is well defined on idele
> classes.

**Proof.**  An element \(\xi\in L^2(\mathbb Z_S^\times\backslash\mathbb A_S)\)
satisfies \(\xi(\gamma a)=\xi(a)\) for all \(\gamma\in\mathbb Z_S^\times\).
Therefore
\((\theta(\gamma)\xi)(a)=\xi(\gamma^{-1}a)=\xi(a)\). \(\square\)

This is genuine well-posedness and it is free.  **It is not principal-divisor
invariance.**  Conflating the two would be an error: Lemma A says the
*representation* is insensitive to units; it says nothing about modifying a
divisor by the divisor of a function.

## 2. Lemma B -- local (affine) principal invariance holds

By 107_237 (2.3), the DC potential determines its test function through

\[
 u_f''(r)=\frac{f(r)}r,
 \tag{2.1}
\]

and 107_237 Theorem 2.1 states that \(U_f\) is unique modulo affine
functions.  In homogeneous coordinates an affine correction is
\(U\mapsto U+\alpha y+\beta x\).

> **Lemma B.**  \(I_\partial\) is invariant under
> \(U_f\mapsto U_f+\alpha y+\beta x\).

**Proof.**  Affine functions have vanishing angular second derivative, so
(2.1) returns the same \(f\).  Since \(I_\partial\) is a function of \(f\)
alone, its value is unchanged. \(\square\)

This is the local half of the missing lemma.  It is immediate from the
already published uniqueness statement and adds no new content.

## 3. Theorem C -- the local principal subspace is trivial

> **Theorem C.**  The map \(f\mapsto D_f\) is injective.  Consequently the
> subspace of *locally* principal DC divisors is \(\{0\}\).

**Proof.**  If \(D_f=D_g\) as distributions then their angular densities
agree, so by (2.1) \(f=g\) pointwise. \(\square\)

The consequence is the operative one and it is negative in an unexpected
direction:

> **There are no nontrivial local principal directions to be invariant
> under.**

Principal invariance therefore cannot be established, tested, or even stated
on the universal positive chart.  It is entirely a statement about global
rational functions on the quotient topos.  107_237 §2 records that those are
not constructed:

> "Here \(U_f\) is a local equation on the universal positive chart, not yet
> a global rational function on the quotient topos."

So the requested lemma is not hard; at present it is **not well posed**.

## 4. Theorem D -- what the descent actually requires

Suppose the global principal subspace \(\mathcal P\) is eventually
constructed.  Descent of \(I_\partial\) to classes is equivalent to

\[
 \mathcal P\subseteq\mathrm{rad}\,I_\partial
 :=\{f:\ N(f\star\widetilde g)=0\ \ \forall g\}.
 \tag{4.1}
\]

> **Theorem D.**  Under Weil's explicit formula,
> \[
>  \mathrm{rad}\,I_\partial
>  =\{f:\ \widehat f(0)=\widehat f(1)=0
>  \text{ and }\widehat f(\rho)=0\text{ for every zero }\rho\text{ of }\xi\}.
> \]

**Proof.**  The explicit formula gives
\(N(h)=\widehat h(0)+\widehat h(1)-\sum_\rho\widehat h(\rho)\).  With
\(h=f\star\widetilde g\) one has
\(\widehat h(s)=\widehat f(s)\overline{\widehat g(\bar s)}\), so

\[
 N(f\star\widetilde g)
 =\widehat f(0)\overline{\widehat g(0)}
 +\widehat f(1)\overline{\widehat g(1)}
 -\sum_\rho\widehat f(\rho)\overline{\widehat g(\rho)} .
\]

This vanishes for every \(g\) exactly when all the displayed coefficients of
\(\widehat f\) vanish. \(\square\)

### 4.1 Consequence

The radical of the corner pairing is **zero-determined**.  Hence proving
(4.1) for a geometrically defined \(\mathcal P\) is a source-versus-target
matching statement whose target side is the zero set of \(\xi\).  This is the
same shape as the obstruction that closed row (c), and it is in direct
tension with the source rule of 107_00 §2.

Principal invariance is therefore **not a formality that concentrated effort
can discharge**.  Its content is exactly as large as the matching problem.

## 5. The constructive split

Theorem D has a positive reading which changes what should be pursued.

**Quotienting by the radical is free.**  For any bilinear form, the induced
form on the quotient by its radical is well defined and nondegenerate.  So

\[
 \overline{I_\partial}\ \text{ on }\
 \{\text{DC divisors}\}/\mathrm{rad}\,I_\partial
 \tag{5.1}
\]

exists unconditionally, with no principal-invariance lemma required.  This
quotient is the analogue of numerical equivalence, and (5.1) is the analogue
of the intersection form on the Neron--Severi group.

**But it is not enough for Riemann--Roch.**  \(H^0(D)\) depends on \(D\) up
to *linear* equivalence, not numerical equivalence.  A Riemann--Roch theorem
therefore genuinely needs \(\mathcal P\) and Theorem D applies in full.

This yields an exact fork:

| goal | needs principal invariance? | status |
|---|---|---|
| Hodge index / signature statement on the numerical quotient | **no** | (5.1) available now |
| Riemann--Roch, \(H^0\), \(H^1\) | **yes** | blocked by Theorem D |

## 6. Status

Proved here:

* Lemma A: unit invariance, automatic, and distinct from principal
  invariance;
* Lemma B: local affine principal invariance;
* Theorem C: the local principal subspace is \(\{0\}\), so the question is
  purely global and currently not well posed;
* Theorem D: the radical of \(I_\partial\) is the zero-vanishing subspace;
* §5: the numerical quotient (5.1) exists unconditionally.

Not proved, and not promoted:

* existence of global rational functions on the DC quotient topos;
* \(\mathcal P\subseteq\mathrm{rad}\,I_\partial\);
* any change to `ROW_A_STATUS`, which remains `partial`.

## 7. Verifier

`107_240_principal_invariance_of_the_corner_pairing.py` checks Lemma A on
five finite idele-class models with their unit subgroups (including that
non-units act nontrivially), verifies (2.1) numerically, verifies Lemma B
against three affine perturbations, and verifies the injectivity of
\(f\mapsto D_f\) of Theorem C on four distinct test functions.
