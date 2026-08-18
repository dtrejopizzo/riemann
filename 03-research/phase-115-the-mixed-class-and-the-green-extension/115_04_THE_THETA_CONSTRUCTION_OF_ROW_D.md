# 115.04 — Constructing row (d): the theta section functor on row (a)'s lattices

The section functor row (d) needs is built here from row (a)'s own data, by
running Wei He's **recipe** (not his theorem) on the lattices row (a) already
produces.  The two-term Riemann–Roch comes out exactly, with the right
constant.  What remains open is stated precisely at the end.

## 0. Why a recipe and not a theorem

Wei He, arXiv:2512.01811, constructs numerical \(h^0,h^1,h^2\) for **classical
Arakelov arithmetic surfaces** \(f:\mathcal X\to\operatorname{Spec}\mathcal O\)
with Hermitian line bundles.  \(\mathscr Y_{\mathbb S}\) is not one of those,
and `main.tex`'s Hodge-route audit says exactly why.  Importing his *theorem*
fails on the same category gap as Faltings–Hriljac–Moriwaki and Yuan–Zhang.

But his construction needs only two inputs:

```text
a lattice  +  a metric   --theta series-->  h^0
Poisson summation        --------------->  Riemann-Roch
lattice duality          --------------->  h^2
```

Row (a) supplies both inputs.  So we do not apply his theorem; we run his
construction on our data.  That is the difference, and it is why this is not
another failed import.

## 1. The data row (a) already has

For effective rational-radius divisors \(D,E\) of degrees \(a,b>0\) and integer
scale \(t\ge1\), row (a) gives:

* \(V_{t,\mathbb Z}(D,E)\) — a **free integral lattice** on the ordered
  digit-pair coordinate basis (`eq:perfectCotangentObject`), of rank
  \[
   N_t:=\dim_{\mathbb R}V_t(D,E)=r(m_t)\,r(n_t)
       =\frac{t^2ab}{(\log2)^2}+O(t)
   \qquad\text{(`cor:cotangentRRdimension`)};
  \]
* a norm on its determinant line (`eq:finiteRRmetric`)
  \[
   \|1_t\|=\exp\bigl(-(\log2)^2N_t\bigr).
  \]

## 2. The metric, and a universal constant

A theta series needs a Euclidean metric on the lattice, not merely a norm on
its determinant.  Row (a) has a **distinguished basis** — the ordered
digit-pair coordinates — so the natural choice is the one making that basis
orthogonal with a common scale \(\sigma_t\).  Then
\(\operatorname{covol}=\sigma_t^{N_t}\), and matching `eq:finiteRRmetric`
forces \(\sigma_t^{N_t}=e^{-(\log2)^2N_t}\), i.e.

\[
 \boxed{\ \sigma=e^{-(\log2)^2}=0.618503\ldots\ }
\]

**independent of \(t\), of \(D\) and of \(E\)**.  The metric is the
distinguished digit basis scaled by one universal constant.  This is a
consequence of the coefficient-one normalization of
`prop:continuousRRdet`; a different normalization would make \(\sigma\) depend
on the divisor and the construction below would not close.

## 3. The definition

\[
 h^0_t(D,E):=\log\!\!\sum_{x\in V_{t,\mathbb Z}(D,E)}\!\!e^{-\pi\|x\|_t^2},
 \qquad
 h^2_t(D,E):=h^0_t(-D,-E).
\]

With the metric of §2 the lattice is \(\sigma\mathbb Z^{N_t}\), so the sum
factors and

\[
 h^0_t(D,E)=N_t\log\theta(\sigma),
 \qquad
 \theta(\sigma):=\sum_{k\in\mathbb Z}e^{-\pi\sigma^2k^2},
\]

a Jacobi theta constant.  \(h^0_t\) is therefore explicit, finite, and
positive.

## 4. Riemann–Roch, exactly

**Theorem (two-term RR).**  For every \(t\),

\[
 \boxed{\;
 h^0_t(D,E)-h^2_t(D,E)=(\log2)^2N_t=\tfrac{t^2}{2}\,B_{\rm int}(D,D)+O(t).
 \;}
\]

*Proof.*  The dual of \(L=\sigma\mathbb Z^{N}\) is
\(L^{*}=\sigma^{-1}\mathbb Z^{N}\), and `prop:divisorlines` identifies it with
the lattice of \((-D,-E)\) through \(\mathcal L(D,E)^{-1}\simeq\mathcal
L(-D,-E)\).  Poisson summation in one variable gives
\(\theta(\sigma)=\sigma^{-1}\theta(1/\sigma)\), hence

\[
 h^0_t-h^2_t=N\bigl[\log\theta(\sigma)-\log\theta(1/\sigma)\bigr]
 =N\log\tfrac1\sigma=(\log2)^2N_t .
\]

For the last equality, `cor:cotangentRRdimension` gives
\((\log2)^2N_t=t^2ab+O(t)\), while `eq:cotangentRRform` gives
\(B_{\rm int}(D,D)=2d_1(D)d_2(D)=2ab\), so
\(\tfrac{t^2}{2}B_{\rm int}(D,D)=t^2ab\). \(\square\)

Three things worth noting.

* The identity is **exact at each finite \(t\)**, not only asymptotic; the
  \(O(t)\) enters only in passing from \(N_t\) to \(t^2ab\).
* The constant matches with **no spurious factor**.  That is precisely what
  the coefficient-one determinant of row (a) was built to deliver — the design
  closes here.
* The mechanism is Poisson summation, which is also the mechanism of row (c)
  (`eq:Hcap`, \(Zf=\mathscr JZ\mathcal Ff\)).  The two rows run on the same
  engine, which is why the transport is available at all.

## 5. The four axioms, one at a time

**Axiom 2 — nonzero strictly effective classes have positive degree.**
`prop:externaleffectivity`: the level-one global sections of \(c\{\infty\}\)
are \(\{n\in\mathbb Z:|n|\le e^{c}\}\), nonzero exactly when \(c\ge0\), applied
independently in the two retained factors.  So effective \(\Rightarrow\) both
degrees \(\ge0\), and nonzero effective \(\Rightarrow\) \(a+b>0\).
**HOLDS.**

**Axiom 3 — \(h^2(D)=h^0(-D)\).**  True by the definition in §3, and
consistent with the Poisson duality used in §4 rather than imposed on top of
it.  **HOLDS.**

**Axiom 4 — the quadratic asymptotic.**  §4 proves the **two-term** form
\(h^0-h^2=\frac{t^2}{2}q+O(t)\).  `thm:mixedsectionforcing` asks for the
**three-term** form \(h^0-h^1+h^2\).  Closing the gap requires identifying
\(h^1\), which is exactly the step Wei He performs by the Leray spectral
sequence plus relative Serre duality, obtaining
\(h^1_{\mathcal X}(\mathcal L)=h^0_{\mathcal X}(\omega_{\mathcal X}\otimes
\mathcal L^\vee)\).  **This is the transport target.**  Do not fudge it: a
curve-type \(\chi\) is not a surface-type \(\chi\).

**Axiom 1 — WITHDRAWN CLAIM.  It does not fail; see `115_05`.**  The text
below argued that a theta invariant is always positive.  That ignores
\(r(0)=0\): off the effective cone row (a)'s code gives the **zero** lattice,
and its theta is \(\log1=0\).  `115_05` proves
\(\widehat h^0=c\,d_1{}_+d_2{}_+\), which settles axioms 1 and 2.  The
paragraphs below are kept only as the record of the error.

A theta invariant is *always* strictly positive — the \(x=0\) term alone
contributes \(1\).  So "\(h^0>0\)" carries no information.  This is a known
feature of theta invariants (van der Geer–Schoof, Bost): effectivity appears
as a **threshold**, not as strict positivity.

What the forcing theorem's proof actually uses is weaker.  It needs only

\[
 h^0(nD)+h^0(-nD)\ \text{large}
 \;\Longrightarrow\;
 nD\ \text{or}\ -nD\ \text{is nonzero strictly effective}.
\]

So axiom 1 should be replaced by:

> **Axiom 1\('\) (threshold form).**  There is \(\kappa>0\) such that
> \(h^0_\theta(D)>\kappa\) implies \(D\) has a nonzero section of norm
> \(\le1\), hence is strictly effective; and \(h^0_\theta(D)\to0\) as the
> lattice's shortest nonzero vector grows.

The second half is elementary: if \(L\) has no nonzero vector of norm
\(\le\rho\) then \(h^0_\theta(L)\le\log(1+Ce^{-\pi\rho^2})\), exponentially
small.  The first half is a lattice-geometry statement of
Minkowski/transference type and is where the work sits.

**Why the replacement is legitimate.**  §4 gives \(h^0_t\) growing like
\(t^2\), which beats any fixed \(\kappa\) for large \(t\).  So the forcing
argument goes through with axiom 1\('\) in place of axiom 1, provided axiom
1\('\) is proved.

## 6. What is now open, precisely

Three items, in order of difficulty.

1. **Axiom 1\('\)** — the threshold-to-effectivity implication on row (a)'s
   lattices.  Lattice geometry; no arithmetic input needed.
2. **\(h^1\) and the three-term \(\chi\)** — transport Wei He's Leray step.
   Requires a Leray-type filtration in \(\operatorname{Perf}_{IDN}\); row (a)
   has the category and the duals, so this is a construction, not an import.
3. **The mixed classes.**  Everything above is on the **ruled** cone, where
   \(V_{t,\mathbb Z}(D,E)\) exists.  The classes row (d) needs are the
   \(D_f\), \(f\in\mathcal T^0\), and row (a) does not yet give
   \(\mathbf H^{\rm int}\) for those.

Item 3 is the real gap, and the construction above changes its character:
it is no longer "find a section functor" but

> **extend one lattice-with-metric family from the ruled cone to the mixed
> classes.**

A theta series needs a lattice and a metric — nothing else.  It does not need
a section space, a cohomology theory, or an effective cone defined in advance.
That is a far smaller demand than the one `113_11` proved impossible inside
\(\mathcal D\), and it is what should be attempted next.

## 7. Classification

* The metric and the universal constant \(\sigma=e^{-(\log2)^2}\): **DERIVED**
  from `eq:finiteRRmetric` and the distinguished basis.
* \(h^0_t=N_t\log\theta(\sigma)\): **PROVED** (the lattice is a scaled
  \(\mathbb Z^{N}\)).
* Two-term RR \(h^0_t-h^2_t=\frac{t^2}{2}B_{\rm int}(D,D)+O(t)\): **PROVED**,
  exact at finite \(t\), constant matching with no spurious factor.
* Axioms 2 and 3: **HOLD**.
* Axiom 4 three-term: **OPEN** — needs \(h^1\) via Leray.
* Axioms 1 and 2: **PROVED** in `115_05` (this note's claim that axiom 1
  fails is withdrawn there).
* Extension to the mixed classes: **OPEN**, and reduced to extending a
  lattice-with-metric family.
* Row D: **OPEN**.
