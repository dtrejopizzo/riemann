# R183.012 — Type audit and the correct Connes–Consani reduction

> **Correction R183.014:** if the localized sandwich is trace class,
> any strong exhaustion by finite-rank projections recovers
> its trace. The special cutoff-compatibility objection is withdrawn
> under that hypothesis. The distinction between ordinary and regularized
> trace must be checked in the application.

## 1. Verdict

R183.004's factorization

\[
u_S=(I M_S I)E_S
\]

**is not proved as an operator identity on a Hilbert space**. In
Connes–Consani's article, the semilocal unitary is indeed rigorously defined by

\[
\underline{\mathcal F}_\alpha
=w^{-1}I\mathcal F_C^{-1}u_S\mathcal F_Cw,                 \tag{1.1}
\]

whereas the co-Poisson map

\[
E_Sf(x)=|x|^{1/2}\sum_{m\in M_S}f(mx)                     \tag{1.2}
\]

appears later in a discussion the article itself declares formal
("not caring too much about some technical points") and heuristic. The
domain of (1.2) is additive and its output is multiplicative. It is not proved
to be a bounded automorphism of `L^2(X_S)`, nor that its Möbius inverse
is an operator on that space.

Consequently, the triangular blocks (2.3), formulas (3.5)–(3.6),
and contraction (4.4) of R183.004 are **WITHDRAWN**. The formal Dirichlet
formula retains algebraic value on a core where the sums are locally
finite, but it cannot be used to compare physical norms.

R183.011(3.2) and every conclusion depending on it are likewise
**WITHDRAWN**. The tail-separation lemma R183.011(2.4) remains
**PROVED** for the formal translation operator; it is not yet
connected to the semilocal unitary by an operator equality.

## 2. Rigorous identity replacing the factorization

Let

\[
\mathcal H_S=L^2(\widehat{C_{\mathbb Q,S}}),\qquad
P=\mathcal F_C\,1_{\{|x|\ge1\}}\,\mathcal F_C^{-1},
\qquad H=2P-1.                                      \tag{2.1}
\]

Here `u_S` is multiplication by the unimodular function that is the product of Tate's local factors. For `h_1\in\mathcal S(C_{\mathbb Q,S})`, let
`M_\varphi` be multiplication by `\varphi=\mathcal F_C h_1`. If
`h_2=h_1^*`, the semilocal contribution is exactly the localized trace

\[
\mathcal W_S(h_1)
=\operatorname{Tr}\!\left(
 M_\varphi^*\,(u_S^*Pu_S-P)\,M_\varphi\right).       \tag{2.2}
\]

This follows from
`\frac12u_S^{-1}[H,u_S]=u_S^*Pu_S-P`. Hence the restricted semilocal
conjecture is precisely

\[
\boxed{\mathcal W_S(h_1)\le0}                       \tag{2.3}
\]

for short multiplicative support and the two Tate moments. Equation
(2.2) is well typed: the three operators act on `\mathcal H_S`.
It cannot be separated into two Hilbert–Schmidt norms without an
additional cutoff: on a continuous space, `M_\varphi`, `PM_\varphi`, and
`Pu_SM_\varphi` are not Hilbert–Schmidt in general. R183.002(1.2)'s
regularized identity is valid for each finite cutoff `E_R`; identifying its
limit with (2.2) requires `E_R` to be exactly compatible with the
semilocal regularization. That compatibility was not proved in R183.002.

## 3. What exactly the support contributes

For `S=S(q)={\infty}\cup\{p:p<q\}` and
`\operatorname{supp}h_1\subset(q^{-1/2},q^{1/2})`, the explicit formula
sees no prime outside `S`: every nontrivial power of one of those
primes has a logarithm of modulus at least `\log q`. This proves that the
semilocal trace (2.2), including the infinite place and the places `p<q`,
is the global Weil form for that test.

The support does not imply that `M_\varphi\mathcal H_S` is invariant under
`u_S`, nor that `u_S^*` is inner. Connes–Consani's general lemma shows
that the operator inequality on all of `\mathcal H_S` would be equivalent to
`Pu_S=Pu_SP`, and they prove that the local factors do not satisfy that
condition. Only the trace inequality on the allowed ideal of
columns `M_\varphi` can hold.

## 4. Reformulation of the pending trace inequality

Define the cone of localizers

\[
\mathfrak J_{q}^{\rm Tate}
=\{M_{\mathcal F_Ch}:\operatorname{supp}h\subset
(q^{-1/2},q^{1/2}),\ h^0=h^2=0\}.                   \tag{4.1}
\]

The necessary and sufficient property is

\[
\boxed{
\operatorname{Tr}\bigl(X^*(u_S^*Pu_S-P)X\bigr)\le0
\quad (X\in\mathfrak J_q^{\rm Tate}).}              \tag{4.2}
\]

This is the same pending trace inequality. The earlier name "relative
innerness" adds no new property nor sign mechanism. Set (4.1) is a space
of admissible localizers; it has not been proved to be an operator ideal.

Connes–Consani prove every subsequent step except (4.2):

\[
\text{(4.2)}\Longrightarrow\text{(2.3)}
\Longrightarrow W(h_1*h_1^*)\le0
\Longrightarrow D.                                  \tag{4.3}
\]

Thus (4.2) is the correct statement to build along this route. Möbius
inversion may enter a proof on a common core, but it cannot be
presented again as a bounded inverse of `E_S`.

## 5. Exact collision with phase 116

Phase 116's differentiated Poisson identity,

\[
Z\partial f+\mathscr JZ\partial\mathcal Ff
=(C+\mathscr JC\mathscr J)Zf,                       \tag{5.1}
\]

is a current identity on a Meyer core. It does not prove (4.2),
because the map `Z` is a topological isomorphism on the weighted space,
not a bounded inverse on the critical `L^2`. The physical metric proposed
in phase 116(99), via `(ZZ^*)^\dagger`, is exactly the missing datum.
Hence R183 had not surpassed phase 116: it had hidden that datum by
declaring `E_S^{-1}`.

Phase 116(257)'s first-contact equality also does not deliver (4.2).
Both reductions are compatible: (257) describes a possible null vector;
(4.2) would supply the sign excluding it. They are not yet equivalent
theorems without constructing the metric identification.

## 6. Status after the audit

* Semilocal operator formula (1.1): **PROVED/CITED**.
* Localized trace identity (2.2): **PROVED/CITED**.
* Limit of R183.002's HS difference: **PROVED** under trace class
  by R183.014, verified on the smooth modulus sector by R183.015.
* Global exactness for short support: **PROVED/CITED**.
* Co-Poisson and Möbius as algebraic identities on a core: **PROVED**.
* `E_S^{-1}` as a physical operator and R183.004(0.1): **WITHDRAWN**.
* Trace inequality (4.2): **OPEN**; it is the goal, not a new tool.
* Row D: **OPEN**.

The next admissible step is to build a closed metric for the co-Poisson
range and prove (4.2) in that metric, or to prove (4.2) directly
as a kernel inequality. Repeating a formal factorization makes no progress.
