# 108.10 -- What is constructible on the numerical quotient without principal invariance, and where it stops

## 1. Purpose

107_240 SS5 constructs, unconditionally, the numerical quotient
\(V:=\{\text{DC divisors}\}/\operatorname{rad}I_\partial\) with a
nondegenerate induced form \(\overline I_\partial\); 107_241 goes on to
compute the full signature of \(\overline I_\partial\) on \(V\) and shows
the Hodge-index statement there is exactly equivalent to RH. Both are
already complete, proved documents; nothing here re-derives them. 108_00
SS6.108.10 asks for an audit: what, precisely, is constructible on \(V\)
without principal invariance, and what fails for lack of it. This note is
that audit, plus one new finding: the domain on which \(V\) is built and the
domain of 108.03's graded family \(\mathcal G\) are currently **disjoint**,
so Part I's constructive step does not yet feed Part II.

## 2. Inventory: what IS constructible on \(V\) (cited, not re-derived)

| object | needs principal invariance? | source | status |
|---|---|---|---|
| \(V=\{\text{divisors}\}/\operatorname{rad}I_\partial\) | no | 107_240 SS5 (5.1) | constructed unconditionally |
| \(\overline I_\partial\), nondegenerate on \(V\) | no | 107_240 SS5 | constructed unconditionally |
| evaluation coordinates \(f\mapsto(\hat f(0),\hat f(1),(\hat f(\rho))_\rho)\) | no | 107_241 Lemma 2.2 | injective on \(V\) |
| full blockwise signature of \(\overline I_\partial\) | no | 107_241 Theorem 3.1 | \(n_+=1+\#P\), \(n_-=1+\#L+\#P\) |
| Hodge index \(\iff\) RH | no | 107_241 Corollary 3.3 | proved equivalence |
| primitive Faltings-Hriljac-shaped form | no | 107_241 Corollary 3.4 | proved |

All of the above is genuinely free of principal invariance: quotienting a
bilinear form by its own radical is always well defined and nondegenerate,
independent of whether the radical happens to contain any *geometrically
distinguished* subspace such as the principal divisors. This is exactly
107_240 SS5's point, and 107_241 shows the resulting numerical intersection
theory is already as rich as a Hodge-index theorem.

## 3. What fails, precisely, for lack of linear equivalence

### 3.1 The classical dependency

\(H^0(D)=\{\text{effective divisors linearly equivalent to }D\}\) (as a set,
or its span) is a functor of the **linear** equivalence class of \(D\), not
of its numerical class. Two divisors \(D,D'\) with \([D]=[D']\) in \(V\)
(same numerical class) can have unequal \(H^0\): numerical equivalence only
guarantees equal intersection numbers against every test class, which is
strictly weaker than \(D-D'\) being principal.

### Proposition 3.1 (no functor of \(H^0\)-type factors through \(V\) alone)

Any construction of \(H^0\), Riemann-Roch, or an effectivity/positivity
statement about *sections* (not just intersection numbers) genuinely
requires knowing \(\mathcal P\subseteq\operatorname{rad}I_\partial\)
(107_240 Theorem D), i.e. requires the principal subspace to be identified
and shown to lie in the radical. \(V\) alone, by construction, only ever
sees divisors modulo \(\operatorname{rad}I_\partial\); it has no memory of
which classes in that radical came from an actual global rational
(Frobenius-invariant) section versus an accidental numerical coincidence.

This is not a new theorem -- it is 107_240 SS5's own stated fork, restated
here as the audit's negative half:

| goal | needs principal invariance? | status |
|---|---|---|
| Hodge index / signature (SS2 above) | no | available now |
| \(H^0\), \(H^1\), Riemann-Roch | **yes** | blocked by 107_240 Theorem D |

## 4. New finding: \(\mathcal G\) (108.03) and \(V\) (107_240 SS5) live on disjoint domains

This is the substantive new content of this audit. It was not asked for by
name in 108_00, but it is the direct obstruction to using 108.03's
explicit \(\operatorname{Prin}(\mathcal G)\) (108.03 Theorem 6.2, 108.04
Theorem 1.1) to make progress on Proposition 3.1's blockage.

### Proposition 4.1

The numerical quotient \(V\) of 107_240 SS5 is built from the pairing
\(I_\partial(D_f,D_g)=\mathfrak T(f\star\widetilde g)\) (107_239 Definition
4.1), itself defined only for \(f,g\) compactly supported (107_239 SS1,
explicitly; 107_241 SS1 fixes the test class as
\(\mathcal A=C_c^\infty(\mathbb R_+^\times)\)). The graded family
\(\mathcal G=\{U_s\}\) of 108.03 is built from \(f_s(r)=r^s\), which by
108.02 Theorem 4.1 is **never** compactly supported for any \(s\) (it is
nowhere zero). Hence no nonzero element of \(\mathcal G\) is the image of
any \(f\in\mathcal A\) under \(f\mapsto D_f\): \(\mathcal G\) and the
category underlying \(V\) intersect only in \(0\).

**Proof.** Immediate from the definitions cited: \(\mathcal A\subset C_c\),
and 108.02 Theorem 4.1 shows character-covariant \(f\) (in particular every
generator of a weight space of \(\mathcal G\)) has full support. \(\square\)

### Corollary 4.2 (108.04's domain gap, restated as a fact about \(V\))

108.04 Proposition 2.1 found that \(I_\partial\) does not accept
\(\operatorname{Prin}(\mathcal G)\) as an input. Proposition 4.1 sharpens
this: it is not merely that the *specific* generator \(U_0\) falls outside
\(I_\partial\)'s stated domain, it is that the **entire ambient category**
\(\mathcal G\) is disjoint from the category \(\{D_f:f\in C_c\}\) that \(V\)
is built from. So even granting a future extension of \(\mathfrak T\) to
some non-compactly-supported inputs, that extension would have to be built
*from scratch* to reach \(\mathcal G\); it is not a matter of checking
whether an already-defined pairing happens to converge on a borderline case.

### 4.3 Consequence for this audit

The clean, if narrow, conclusion is:

\[
 \boxed{\text{Part I (108.02-108.04) and Part II (107_240 SS5/107_241) are,
 right now, constructions on disjoint test-function categories.}}
\]

Nothing proved in either part is threatened by this -- 107_241's signature
theorem stands on \(C_c\)-currents exactly as published, and 108.03's
graded sheaf stands on its own non-compact category exactly as constructed
-- but the *hoped-for* synthesis (use 108.03's explicit nonzero principal
witness to make progress on 107_240 Theorem D, and hence unblock \(H^0\)/RR
per SS3 above) does not yet have a bridge. Building one -- extending
\(\mathfrak T_S\)/\(I_\partial\) to a category containing both \(C_c\) and
the graded monomials, e.g. via the same finite-part/renormalization idea
already used once in 107_239 (1.4) to tame a different divergence -- is the
next gate for row (a)'s numerical route. It is not attempted here.

## 5. Status

Constructible without principal invariance (cited, confirmed unconditional):
numerical quotient \(V\), nondegenerate \(\overline I_\partial\), its full
signature, and the Hodge-index/RH equivalence.

Not constructible without principal invariance: \(H^0\), \(H^1\),
Riemann-Roch, effectivity (107_240 Theorem D, Proposition 3.1 above).

New in this note: the two halves of Phase 108's own current work (the
graded sheaf of Part I and the numerical quotient of Part II) do not yet
compose, because they are built on disjoint test-function categories
(Proposition 4.1). This is an candid, structural, and previously
unstated gap; closing it is a concrete, well-posed next task, distinct from
(and prior to) actually testing principal invariance.

`ROW_A_STATUS` is unaffected and remains `partial`.

## 6. Verifier

`108_10_numerical_route_audit.py`:

1. re-affirms (cites, cross-checks does not re-derive) the shape of
   107_241 Theorem 3.1's signature formula and 107_240 SS5's fork table as
   structured data, checking internal consistency (\(n_++n_-=\) the number
   of evaluation coordinates present in a synthetic finite truncation, as
   in 107_241's own verifier pattern);
2. directly tests Proposition 4.1 on the actual objects: confirms every
   sampled \(f_s(r)=r^s\), \(s\) in a bank of values, fails a compact-support
   test (nonzero at arbitrarily large and arbitrarily small sampled radii),
   while a bank of genuine \(C_c\) bump functions (reusing 108.01's
   candidates) passes it;
3. prints the fork table and `VERDICT: DISJOINT_DOMAINS_CONFIRMED`.
