# 115.05 — Axiom 1 holds: the closed form of the normalized theta invariant

**Axiom 1 does not fail.**  `115_04` §5 claimed it did, on the grounds that a
theta invariant is always strictly positive.  That reasoning ignores the one
feature of row (a) that makes the construction work off the effective cone,
and the claim is withdrawn here.  Axioms 1 and 2 are now **proved**.

## 1. The point that was missed

A theta series over a *nonzero* lattice is indeed always \(>0\): the term
\(x=0\) contributes \(1\).  But row (a)'s code produces the **zero lattice**
in negative degree.

From `eq:rmdefinition`, \(r(m)=\lfloor\log_2(m+1)\rfloor\), so \(r(0)=0\).
And from `eq:scaledCode`, \(m_t=\lfloor e^{ta}\rfloor\), which is \(0\) as soon
as \(a<0\).  Hence \(N_t=r(m_t)r(n_t)=0\), the lattice
\(V_{t,\mathbb Z}(D,E)\) is \(\{0\}\), the defining sum collapses to its single
term, and

\[
 h^0_t=\log 1=0 .
\]

This is exactly the classical behaviour of \(h^0\), and it is inherited rather
than imposed: the bounded-section modules \(H_m\) of row (a) vanish in negative
degree, and the code vanishes with them.  It is also the point at which this
construction differs from a theta invariant on a fixed lattice (van der
Geer–Schoof, Bost), where \(h^0\) is small but positive for very negative
classes.

## 2. The theorem

Write \(x_+:=\max(x,0)\) and
\(\widehat h^0(D,E):=\lim_{t\to\infty}t^{-2}h^0_t(D,E)\).

> **Theorem.**  The limit exists for every pair of rational-radius divisors and
> \[
>  \widehat h^0(D,E)=c\;d_1(D)_+\,d_2(E)_+,
>  \qquad
>  c=1+\frac{\log\vartheta(\sigma^{-1})}{(\log2)^2}=1.0011290\ldots
> \]
> Likewise \(\widehat h^\vee=(c-1)\,d_1{}_+d_2{}_+\), so
> \(\widehat h^0-\widehat h^\vee=\tfrac12B_{\rm int}(D,D)\).

**Proof.**  \(h^0_t=N_t\log\vartheta(\sigma)\) by the factorization of
`115_04` §3.  Three cases:

* \(a<0\): \(m_t=0\), \(r(0)=0\), \(N_t=0\), \(h^0_t=0\) for every \(t\).
  Symmetrically for \(b<0\).
* \(a=0\): \(m_t=1\), \(r(1)=1\), \(N_t=r(n_t)=O(t)\), so \(N_t/t^2\to0\).
* \(a,b>0\): `lem:negabinaryradius` gives \(r(m_t)=ta/\log2+O(1)\) and
  \(r(n_t)=tb/\log2+O(1)\), so \(N_t/t^2\to ab/(\log2)^2\).

Multiply by \(\log\vartheta(\sigma)\) and put
\(c=\log\vartheta(\sigma)/(\log2)^2\).  Poisson,
\(\vartheta(\sigma)=\sigma^{-1}\vartheta(\sigma^{-1})\), gives
\(\log\vartheta(\sigma)=(\log2)^2+\log\vartheta(\sigma^{-1})\), hence the value
of \(c\). \(\square\)

Numerically: \(\log\vartheta(\sigma)=0.480995445972\ldots\),
\((\log2)^2=0.480453013918\ldots\),
\(\log\vartheta(\sigma^{-1})=5.4243\ldots\times10^{-4}\),
\(c-1=1.12900\ldots\times10^{-3}\).

## 3. Axioms 1 and 2

With **"strictly effective" read as "interior of the effective cone"** —
\(d_1>0\) and \(d_2>0\), the interior of the \(\mathbb R^2_{\ge0}\) of
`prop:externaleffectivity` — the closed form gives at once:

* \(\widehat h^0\ge0\) everywhere;
* \(\widehat h^0(0)=0\);
* \(\widehat h^0(D)>0\iff D\) strictly effective;
* strictly effective \(\Rightarrow\deg D=d_1+d_2>0\).

Hence the implication the proof of `thm:mixedsectionforcing` actually uses,

\[
 \widehat h^0(D)>0\ \Longrightarrow\ \deg D>0,
\]

holds **unconditionally**.  Axioms 1 and 2: **PROVED**.

Two caveats, both recorded in the paper.  \(\widehat h^0\) vanishes on the two
boundary rays of the cone as well as outside it, which is why "strictly
effective" must be interior membership and not "effective and nonzero".  And
\(c\) cancels in the Riemann–Roch identity, so it plays no role there; it
records only the exponentially small dual contribution.

## 4. Status of the construction after this

| axiom | status |
|---|---|
| 1 — \(h^0(0)=0\), \(h^0>0\iff\) strictly effective | **PROVED** (§3) |
| 2 — strictly effective \(\Rightarrow\) positive degree | **PROVED** (§3) |
| 3 — \(h^2(D)=h^0(-D)\) | **OPEN**: needs the anti-effective extension |
| 4 — quadratic \(\chi\), three-term | **OPEN**: two-term proved, needs \(h^1\) via Leray |

Plus the standing gap: everything is on the **ruled cone**; the mixed classes
\(D_f\), \(f\in\mathcal T^0\), are not covered.

Axiom 3 has an interesting shape now.  The dual invariant is
\(\widehat h^\vee=(c-1)d_1{}_+d_2{}_+\), i.e. positive exactly on the interior
of the effective cone — whereas \(h^0(-D)\) should be positive exactly on the
interior of the *anti*-effective cone.  So \(\widehat h^\vee\ne h^0(-D)\) as
functions on the ruling sector, and axiom 3 cannot hold on the nose for the
present lattices.  What the Riemann–Roch identity needs is the dual lattice,
which is available; what axiom 3 asks for is a different object.  This should
be resolved before \(h^1\) is attempted, because the Leray step will need to
know which of the two is the dualizing object.

## 5. Classification

* Closed form \(\widehat h^0=c\,d_1{}_+d_2{}_+\): **PROVED**.
* Axioms 1 and 2: **PROVED**, with the interior reading of strict
  effectivity.
* `115_04` §5's claim that axiom 1 fails: **WITHDRAWN**, cause recorded in §1.
* Axiom 3: **OPEN**, and §4 shows it is not merely unproved but false for the
  present pair \((h^0,h^\vee)\) — the dual invariant is supported on the wrong
  cone.
* Axiom 4 three-term: **OPEN**.
* Mixed classes: **OPEN**.
* Row D: **OPEN**.
