# 114.a.03 — The candidate ledger: a verdict on every product structure over Spec Z

> **I7 supersession (114.a.05/09/10).** The rational-Witt candidate described
> below as "built-modulo-gap" is now closed negatively as a route to the
> unified row (a).  Its cyclotomic kernel is an explicit infinite free
> lattice, but the quotient loses the resultant data; moreover its generators
> are principal after compactification and fixed by coprime Frobenius maps.
> See `114_a_05_I7_KERNEL_AND_HARAN_REAUDIT.md`,
> `114_a_09_I7_FROBENIUS_AND_PRINCIPAL_NO_GO.md`, and the authoritative
> completion audit `114_a_10_ROW_A_COMPLETION_AUDIT.md`.
>
> **Haran correction (114.a.05).** Section 11 of the cited Haran source, which
> follows the square construction in section 10, defines completed bundles,
> their section sheaves, and rank-one isomorphism classes for arbitrary
> pro-objects in the category.  Thus G-7 is not missing a formal divisor/section
> language from zero. `a_66` restores the abstract external Picard sector by
> unit-torsor pullback and proves each ruling injective; `a_63` requires
> H7-PB-REG only for its completed-lattice/gauge realization. The full
> continuous kernel still reduces to the anti-diagonal. A proper gauge, Kunneth
> theorem, a typed Cartier/module comparison, intersection and geometric
> Frobenius cycle remain absent.

```
+--------------------------------------------------------------------------+
| ROW (a), ITEM a4 — STAGE 3: ONE VERDICT PER CANDIDATE                    |
|                                                                          |
| GENERAL NEGATIVE RESULT (Thm 2.1, the continuous-dimension obstruction)  |
|   ANY dimension function with h^0(mD) = m h^0(D) has delta = 1 and can   |
|   NEVER carry a quadratic Riemann-Roch term.  Continuity IS linearity.   |
|   This kills, by ONE mechanism and unconditionally: the scaling site     |
|   (CC's own cdim, which they identify with a type-II normalised trace),  |
|   the adele class space, and every von Neumann / noncommutative-measure  |
|   dimension, including Bost-Connes.  Not a survey remark: a theorem.     |
|                                                                          |
| SECOND NEGATIVE RESULT (Thm 2.3, the rank-one obstruction)               |
|   Every object in the Connes-Consani programme through 2026 - Spec Zbar, |
|   the arithmetic site, the scaling site, the Jacobian paper, the         |
|   absolute F_1-curve - has RANK-ONE section modules, by their own        |
|   descriptions.  114_a_01 Thm 4.3 then forces delta <= 1.  CC's route    |
|   is a CURVE route, by construction, and cannot supply a4.               |
|                                                                          |
| THIRD NEGATIVE RESULT (Prop 4.2, the overshoot)                          |
|   On CC's REDUCED SQUARE the sections are Newton polygons.  There are at |
|   least 2^{n+1} of them in a box of side n^2, so any counting dimension  |
|   is EXPONENTIAL in deg, not quadratic.  The square fails on the other   |
|   side: too many sections, not too few.                                  |
|                                                                          |
| POSITIVE (two, and only two)                                             |
|   (i)  Arakelov arithmetic surfaces.  BUILT (114_a_02).  a4-weak closed. |
|   (ii) RATIONAL WITT VECTORS W_rat / W_J.  BUILT-MODULO-GAP, and it is   |
|        the best candidate in the ledger: Deninger arXiv:2508.05329       |
|        Thm 2.8 gives an ADDITIVE filtration W_J^{<=n} . W_J^{<=m} c      |
|        W_J^{<=n+m} with Frobenius F_N at every N, and Thm 5.1 identifies |
|        W_rat(O(X)) with a ring of FINITE ALGEBRAIC CYCLES - row (b)      |
|        living inside a row-(a) candidate.  Missing: a norm and a         |
|        pairing.  Gap G-4.                                                |
|                                                                          |
| a4-STRONG  The only genuine square Spec Z x_{F_1} Spec Z actually        |
|            CONSTRUCTED in the literature read here is HARAN's            |
|            (arXiv:1709.05831 sec.10).  It has no degree and no gauge, so |
|            the test cannot fire.  Gap G-7.  That is the frontier.        |
|                                                                          |
| 107_242 Thm 4.1  ANSWERED: it forbids THE CYCLES ONLY, and only through  |
|            the Morishita bridge Psi.  The Deninger space itself is       |
|            untouched, and 107_242 sec.5 says so.                         |
|                                                                          |
| VERIFIER  114_a_03_the_candidate_ledger.py — 22 checks, exit 0,          |
|           VERDICT: ALL CHECKS PASS (output in sec.8)                     |
|                                                                          |
| GAPS OPENED  G-4, G-5, G-6, G-7, G-8.  DISCHARGED: none.                 |
| CIRCULARITY  CLEAN throughout; see sec.9.                                |
+--------------------------------------------------------------------------+
```

**Depends on:**

- `phase-114-closing-the-four-rows/114_a_01_THE_GROWTH_DICHOTOMY_AND_THE_RANK_FALLACY.md`
  — Thm 3.3, Thm 4.2, Thm 4.3, Defs 5.1/5.2, Prop 5.4.
- `phase-114-closing-the-four-rows/114_a_02_AN_ARITHMETIC_SURFACE_OVER_SPEC_Z_WITH_QUADRATIC_H0.md`
  — Thm 3.4, Cor 6.4.
- `03-research/phase-107-arithmetic-lefschetz-reconstruction/107_242_THE_MORISHITA_BRIDGE.md`
  — §0, Thm 4.1, §5. Read in full.
- `00-references/papers-nuevos/A/arXiv-1507.05818v2/scalingsite-CRAS.tex` — abstract, intro, Thm `RRperiodic`. Read.
- `00-references/papers-nuevos/A/arXiv-1502.05580v1/arithmeticsite_Adv_final1.tex` — intro §, §`sectsquare`. Read.
- `00-references/papers-nuevos/A/arXiv-2205.01391v2/RR-J-final.tex` — §2–3. Read.
- `00-references/papers-nuevos/A/arXiv-2602.15941v1/Jacobian.tex` — abstract. Read.
- `00-references/papers-nuevos/A/arXiv-2606.06604v1/FF.tex` — abstract. Read.
- `00-references/papers-nuevos/A/arXiv-1709.05831v1/HARAN_Dec2016_updated_4.tex` — §10. Read.
- `00-references/papers-nuevos/B/arXiv-2508.05329v1/*.tex` — Deninger, *Rational Witt vectors and associated sheaves*: Introduction, Thm 2.8, Thm 5.1. Read.
- `00-references/papers-nuevos/D/arXiv-2512.01811v2/…` — Thm `main1`. Read (see `114_a_02` §8).

---

## 1. The protocol

Every candidate is put through exactly the two tests of `114_a_01` §5, plus the
bookkeeping condition:

- **O1-TEST** (Def 5.1): do the section modules $H^0(mD)$ contain integral
  lattices of unbounded rank, with a non-scale-invariant effectivity condition?
- **GROWTH-TEST** (Def 5.2): is $\delta(D)=\lim\log h^0(mD)/\log m$ equal to $2$?
- **Bookkeeping** (Prop 5.4): are both $\deg_{\mathrm{fin}}(mD)$ and
  $\deg_\infty(mD)$ of size $\Theta(m)$?

Four verdicts are possible, and each candidate gets exactly one:

| verdict | meaning |
|---|---|
| **PASSES** | $\delta=2$ is proved for an explicit family |
| **CLOSED NEGATIVE** | $\delta\le1$ is *proved*, with the mechanism named |
| **OVERSHOOTS** | the natural $h^0$ is proved super-polynomial in $\deg$ |
| **UNTESTABLE (Gap G-n)** | no $h^0$ and no gauge exists in the source; the precise missing datum is written as a Gap |

"UNTESTABLE" is a real verdict, not an evasion: in each case §7 states exactly
which object has to be defined before the test can fire.

---

## 2. Two general obstructions, proved once

### 2.1 The continuous-dimension obstruction

**Theorem 2.1.** Let $h^0$ be a dimension function on a divisor set closed under
$D\mapsto mD$, $m\in\mathbb Z_{\ge1}$, and suppose
$$
 h^0(mD)=m\,h^0(D)\qquad\text{for all }m\ge1\text{ and all }D. \tag{L}
$$
Then $\delta(D)=1$ for every $D$ with $h^0(D)>0$, and no Riemann–Roch formula of
the form $h^0(mD)=\tfrac12(mD)^2+O(m)$ with $(D)^2\ne0$ can hold.

*Proof.* $\dfrac{\log h^0(mD)}{\log m}=\dfrac{\log m+\log h^0(D)}{\log m}\to1$.
If in addition $h^0(mD)=\tfrac12m^2D^2+O(m)$ with $D^2>0$, then
$h^0(mD)/m\to\infty$, contradicting (L), which forces $h^0(mD)/m=h^0(D)$
constant. $\square$

**Remark 2.2 (why this is the whole noncommutative-geometry family).**
Condition (L) is precisely the defining property of a *continuous*, or type-II,
dimension: a normalised von Neumann trace is additive and homogeneous of degree
one on projections. Connes–Consani say so themselves. Quoting
arXiv:1507.05818v2 §1 verbatim:

> The appearance of arbitrary positive real numbers as continuous dimensions in
> this formula is due to the density in $\mathbb R$ of the subgroup
> $H_p\subset\mathbb Q$ … and the fact that continuous dimensions are obtained as
> limits of normalized dimensions $p^{-n}\mathrm{tdim}(H^0(D)^{p^n})$. We
> view this outcome as the analogue in characteristic $1$ of what happens for
> matroid $C^*$-algebras and the type II normalized traces …

So the mechanism has a name: **a continuous dimension is linear, and linearity
is exactly what a surface must not have.** Whatever else is true of the adele
class space, the scaling site or the Bost–Connes system, any dimension theory on
them that is a trace is excluded from row (a) by Theorem 2.1. This is *not*
obstruction O1 (which is $\delta=0$); it is one degree worse than a curve is
allowed to be, and one degree short of what is needed.

### 2.2 The rank-one obstruction

**Theorem 2.3.** (= `114_a_01` Thm 4.3, restated for use here.) If the section
modules $H^0(mD)$ have integral rank bounded by $r_0$ along the ray, and the
archimedean size is $e^{O(\deg mD)}$, then $h^0(mD)=O(m)$ and $\delta\le1$.

Every object whose points are *rank-one* modules falls under this. That is the
whole Connes–Consani list; see §3.

---

## 3. The Connes–Consani programme

### 3.1 $\overline{\mathrm{Spec}\,\mathbb Z}$ and the Riemann–Roch of arXiv:2205.01391

Their $\dim_{\mathbb S_\pm}\|H\mathbb Z\|_n=\lceil\log_3(2n+1)\rceil$ with
$n=\lfloor e^{\deg D}\rfloor$; `107_146` Cor C then gives
$\dim=\Theta(\deg D)$ in every fixed rank.

- **O1-TEST:** weak pass — $\dim H^0$ is integer-valued while $\deg$ is real, which
  is what `113_10` route (i) noticed. But the integral rank is $1$.
- **GROWTH-TEST:** **FAIL.** $\delta=1$ (measured $0.99605$; §8 check C1).
- **Bookkeeping:** fails — $\deg_{\mathrm{fin}}\equiv0$: nothing charges the rank
  direction.
- **VERDICT: CLOSED NEGATIVE.** *Mechanism: rank one.* It is a curve, as its own
  title says.

### 3.2 The arithmetic site (arXiv:1405.4527, arXiv:1502.05580)

The topos $\widehat{\mathbb N^\times}$ with structure sheaf $\mathbb Z_{\max}$;
its points over $\mathbb R_{\max}$ are the adele class space modulo
$\hat{\mathbb Z}^*$.

- There is **no divisor group, no $h^0$ and no degree** anywhere in
  arXiv:1502.05580. I read §`sectsquare` in full and grepped the whole section
  for `dim`, `H^0`, `Riemann`, `divisor`, `degree`: none occur.
- **VERDICT: UNTESTABLE — Gap G-5.** *What is missing:* a divisor group and a
  section functor on $\widehat{\mathbb N^\times}$. *Prediction from Theorem 2.1:*
  if the dimension is taken to be the type-II trace on the adele class space, it
  will satisfy (L) and $\delta$ will be $1$.

### 3.3 The scaling site and the periodic orbits $C_p$ (arXiv:1507.05818)

Their Theorem `RRperiodic`, quoted verbatim:

> **Theorem.** $(i)$ Let $D\in\mathrm{div}(C_p)$ be a divisor with
> $\deg(D)\ge0$. Then the limit in $(\ast)$ converges and one has
> $\mathrm{cdim}(H^0(D))=\deg(D)$.
> $(ii)$ The following Riemann–Roch formula holds
> $\mathrm{cdim}(H^0(D))-\mathrm{cdim}(H^0(-D))=\deg(D)$, for all
> $D\in\mathrm{div}(C_p)$.

- **GROWTH-TEST:** **FAIL, exactly and not merely asymptotically.**
  $\mathrm{cdim}\,H^0(mD)=\deg(mD)=m\deg D$, which is hypothesis (L) of
  Theorem 2.1 on the nose. Hence $\delta=1$ identically (§8, check B1: measured
  $1.000000000000$).
- **Independent confirmation of the criterion.** CC also record the exact
  sequence
  $0\to\mathbb Z/(p-1)\mathbb Z\to\mathrm{div}(C_p)/\mathcal P
  \xrightarrow{\deg}\mathbb R\to0$. The discrete part is **finite**, so the
  lattice rank is bounded and Theorem 2.3 predicts $\delta\le1$ *before* looking
  at their theorem. Their theorem then gives $\delta=1$. The criterion of
  `114_a_01` and CC's Riemann–Roch agree.
- **VERDICT: CLOSED NEGATIVE.** *Mechanism: continuous (type-II) dimension;
  equivalently, finite discrete part of the divisor class group.*

### 3.4 The square of the arithmetic site (arXiv:1502.05580 §`sectsquare`)

This is a genuine two-directional object: the topos
$\widehat{\mathbb N^\times\times\mathbb N^\times}$ with structure sheaf
$\mathbb Z_{\min}\otimes_{\mathbb B}\mathbb Z_{\min}$; after reduction the
elements of the semiring are **Newton polygons**, with operations "convex hull of
the union" and "Minkowski sum", and it carries the Frobenius correspondences
$\Psi(\lambda)$, $\lambda\in\mathbb R_+^\times$, with
$\Psi(\lambda)\circ\Psi(\lambda')=\Psi(\lambda\lambda')$ (their Thm
`thmcomp0`). This is the closest thing in CC to a4-strong, and it is why the
task singles it out.

**Proposition 3.5 (the overshoot).** Let $\mathcal P(N)$ denote the set of
convex lattice polygons contained in $[0,N]^2$. Then
$$
 \#\mathcal P(N)\ \ge\ 2^{\lfloor\sqrt N\rfloor+1}.
$$

*Proof.* Put $n=\lfloor\sqrt N\rfloor$ and $P_j=(j,j^2)$, $j=0,\dots,n$; all lie
in $[0,n]\times[0,n^2]\subseteq[0,N]^2$. Since $x\mapsto x^2$ is strictly convex,
for $i<j<k$ the cross product
$(P_j-P_i)\times(P_k-P_i)=(j-i)(k^2-i^2)-(j^2-i^2)(k-i)=(j-i)(k-i)(k-j)>0$, so
the $n+1$ points are in strictly convex position and every subset $S$ has
$\mathrm{vert}(\mathrm{conv}\,S)=S$. Distinct subsets therefore give
distinct polygons, and there are $2^{n+1}$ of them. $\square$

(Machine-checked for $n\le80$: §8 checks F1–F3.)

**Corollary 3.6.** If, on the reduced square, the sections of a divisor of degree
$d$ are taken to be the Newton polygons inside a box of side $e^{d}$ — the only
normalisation consistent with the archimedean normalisation
$n=\lfloor e^{\deg D}\rfloor$ used by CC on $\overline{\mathrm{Spec}\,\mathbb Z}$ —
then
$$
 \log\#H^0(D)\ \ge\ e^{d/2}\log 2,
 \qquad\text{and}\qquad
 \dim_{\mathbb S_\pm}H^0(D)\ \ge\ e^{d/2}\log_3 2
$$
by the entropy bound `114_a_01` Thm 2.1. Both are **exponential** in $\deg D$,
not quadratic.

- **VERDICT: OVERSHOOTS** under the only natural normalisation, and
  **UNTESTABLE — Gap G-6** otherwise, since no $h^0$ is defined in the source.
  *Mechanism: the semiring of the square is a semiring of convex bodies, and
  convex bodies in a box of side $N$ are $e^{\Theta(\sqrt N)}$ in number, not
  $N^{O(1)}$.* The square fails on the far side of the target: too many
  sections. Any repair must cut the sections down — e.g. by bounding the number
  of vertices — and that reintroduces a rank parameter, which is exactly what
  Theorem 2.3 says is needed.

### 3.7 The 2026 papers

*On the Jacobian of $\overline{\mathrm{Spec}\,\mathbb Z}$* (arXiv:2602.15941),
abstract, verbatim: *"We identify the elements of this space with torsion-free
**rank-1** abelian groups $L$ endowed with rigidifying data. In the Riemann
sector, this data corresponds to a norm, extending the classical notion of
metrized line bundles in Arakelov geometry."*

*On the Absolute Geometry of $\mathrm{Spec}\,\mathbb Z$ and the
Fargues–Fontaine curve* (arXiv:2606.06604), abstract, verbatim: *"We construct
the absolute $\mathbb F_1$-arithmetic **curve** $\mathrm{Spec}(\mathbb Z)_{\mathbb F_1}$
by pulling back the $\mathbb F_1$-structure sheaf of the arithmetic site to
$\mathrm{Spec}(\mathbb Z)$."*

- **VERDICT (both): CLOSED NEGATIVE.** *Mechanism: rank one, by the authors' own
  descriptions* — "torsion-free rank-1 abelian groups", "the absolute
  $\mathbb F_1$-arithmetic curve". Theorem 2.3 applies verbatim. These are
  refinements of the curve, and they are excellent ones; they are not the
  surface.

### 3.8 Segal $\Gamma$-rings, $\mathbb S$-modules, the sphere spectrum

The $\mathbb S_\pm$-module formalism of arXiv:2205.01391 §2 supplies the
*dimension function*, not the *space*. `114_a_01` Thm 2.4 shows it is
**neutral**: on a rank-$r$, radius-$n$ gauged module it returns
$\Theta(r\log n)$, which is quadratic exactly when the space is.

- **VERDICT: NEUTRAL, and reusable.** It is the right measuring instrument; it
  measures whatever it is pointed at. `114_a_02` Thm 3.6 points it at an
  arithmetic surface and it returns $\tfrac12 D^2/\log q$, $q\in[2,3]$.

---

## 4. Arakelov geometry

`114_a_02` builds $\overline{\mathbb P^1_{\mathbb Z}}$ explicitly and proves
$h^0_\theta(D)=\tfrac12\langle D,D-K\rangle+\eta$ with $\eta$ super-exponentially
small. arXiv:2512.01811v2 Theorem `main1` gives the same shape for *arbitrary*
arithmetic surfaces (quoted verbatim in `114_a_02` §8).

- **O1-TEST: PASS** (section lattices of rank $mk+1\to\infty$).
- **GROWTH-TEST: PASS**, $\delta=2$ (§8, check D1).
- **Bookkeeping: PASS** ($\deg_{\mathrm{fin}}=mk$, $\deg_\infty=ma$).
- **VERDICT: PASSES. a4-weak BUILT.**
- **But:** it is not the square (`114_a_02` §7.1), and realising the row-(c)
  pairing $s$ inside an Arakelov intersection form is RH-hard — `114_a_04`.
  Faltings–Hriljac, Moriwaki, Yuan–Zhang and the arithmetic Hodge index
  (arXiv:1810.06342) all live on this candidate and all inherit that difficulty;
  they are treated there, not here.

---

## 5. Λ-geometry, Witt vectors, and the best candidate in the ledger

### 5.1 What was actually read

Deninger, *Rational Witt vectors and associated sheaves*, arXiv:2508.05329v1.
Introduction and two theorems, read:

> The rational functions within the big Witt vector ring $W(A)=1+TA[[T]]$ form a
> subring $W_{\mathrm{rat}}(A)$ for any commutative unital ring $A$. It carries
> Frobenius and Verschiebung endomorphisms and may be viewed as an uncompleted
> version of $W(A)$.

> **Theorem 2.8.** The $\mathrm{ind}$-scheme $W_J$ is a subring in
> $\mathrm{Indsch}$ of $W$. It is equipped with Frobenius ring
> endomorphisms $F_N$ and additive Verschiebung endomorphisms $V_N$ which are
> compatible with those of $W$. More precisely, for the closed affine subschemes
> $W_J^{\le n}$ of $W_J$ we have factorizations
> $W_J^{\le n}\times W_J^{\le m}\xrightarrow{+,\;\cdot}W_J^{\le n+m}$ …

> **Theorem 5.1.** On the category of normal, Noetherian, affine schemes $X$
> there is a unique functorial factorization of the map (25) over a functorial
> ring isomorphism $W_{\mathrm{rat}}(\mathcal O(X))\xrightarrow{\ \sim\ }\underline{\mathrm{Corr}}(X,\mathbb A)$.

### 5.2 The test

**Proposition 5.3.** The set $1+T\mathbb Z[T]_{\le n-1}=\{1+c_1T+\dots+c_nT^n:
c\in\mathbb Z^n\}$ is contained in $W_{\mathrm{rat}}(\mathbb Z)$ and is a torsor
under the rank-$n$ lattice $\mathbb Z^n$. Gauging it by the coefficient norm
$|c|_1\le e^{a}$ and setting $D=(n,a)=(mk,ma)$ gives
$$
 \log\#H^0(mD)\ =\ ka\,m^2+O(m\log m),
$$
i.e. $\delta=2$, with leading constant $1$.

*Proof.* A polynomial with unit constant term is a unit of $\mathbb Z[[T]]$ and
is a rational function, hence lies in $W_{\mathrm{rat}}(\mathbb Z)$; the map
$c\mapsto 1+\sum c_jT^j$ is a bijection onto the stated set. The count is
`114_a_02` Theorem 3.1 with $r=n$. $\square$

(§8, checks E1–E4: $\delta$ measured $2.02143$, leading ratio $0.98490$ at
$m=256$.)

**Remark 5.4 (why this is the best candidate).** Three structures coincide on
this object and on no other in the ledger.

1. **A growing rank with an additive degree, from the source.** Theorem 2.8's
   filtration satisfies $W_J^{\le n}\cdot W_J^{\le m}\subseteq W_J^{\le n+m}$, so
   $n$ *is* a degree — additive under the product, exactly what Prop 5.4 of
   `114_a_01` demands of $\deg_{\mathrm{fin}}$.
2. **Frobenius at every prime, from the source.** $F_N$ for all $N$, compatible
   with $W$: this is precisely the $\Lambda$-structure that Borger's programme
   proposes as descent data to $\mathbb F_1$, and it is here as a theorem about
   an ind-scheme, not as a philosophy.
3. **Cycles, from the source.** Theorem 5.1 identifies
   $W_{\mathrm{rat}}(\mathcal O(X))$ with $\underline{\mathrm{Corr}}(X,\mathbb A)$,
   a ring of **finite algebraic cycles**. That is row (b) sitting inside a row-(a)
   candidate — the one place in this ledger where the two rows meet inside a
   single object.

- **O1-TEST: PASS.** **GROWTH-TEST: PASS.** **Bookkeeping: PASS in the finite
  direction (Thm 2.8), NOT ESTABLISHED in the archimedean direction.**
- **VERDICT: PASSES, MODULO GAP G-4.**

**Gap G-4 (the Witt gap).** There is no archimedean gauge and no intersection
pairing on $W_{\mathrm{rat}}(\mathbb Z)$ in the source. What is needed: a norm
$\|\cdot\|$ on $W_J^{\le n}(\mathbb Z)$ compatible with $F_N$ and $V_N$, and a
symmetric bilinear form on pairs $(n,a)$ with $\langle f_{\mathrm{fin}},f_\infty\rangle=1$.
The natural candidate for the norm is the logarithmic Mahler measure
$\log M(f)=\int_0^1\log|f(e^{2\pi i\theta})|\,d\theta$, which is *additive* under
multiplication of Witt vectors — hence a homomorphism $W_{\mathrm{rat}}(\mathbb Z)\to\mathbb R$,
which is the right shape for $\deg_\infty$. Comparing it with the coefficient
norm requires Jensen's formula and is **not carried out here**.

### 5.5 Borger's $\Lambda$-algebraic geometry

The task records that "the ledger does not record it as having been tested. Test
it." Two candid statements:

1. **Attribution.** The identification of $\mathrm{Spec}\,\mathbb Z\times_{\mathbb F_1}\mathrm{Spec}\,\mathbb Z$
   with a Witt-vector object is attributed to Borger's programme. **I have not
   read a Borger paper in this session and cite no theorem of his.** No paper of
   his is in `00-references/papers-nuevos`.
2. **The test, run on the object rather than on the attribution.** The object
   $W(\mathbb Z)=1+T\mathbb Z[[T]]$, with its truncations $W_n(\mathbb Z)\cong\mathbb Z^n$
   (as sets, by ghost/coefficient coordinates) and its Frobenius lifts $F_p$ at
   every prime, is tested in §5.2 through its rational sub-object. **It passes
   the GROWTH-TEST.** Whatever the correct attribution, the Witt object is the
   one that works.

- **VERDICT: PASSES, MODULO GAP G-4, with the attribution flagged as unverified.**

---

## 6. Deninger, Haran, and the rest

### 6.1 Deninger's foliated dynamical system, and what 107_242 Thm 4.1 forbids

The task asks to determine *exactly* what `107_242` Thm 4.1 forbids — "the cycles
only, or the space too". Read in full; the answer is unambiguous.

`107_242` §5, verbatim:

> * **Solved as an object.** Deninger's $W_{\rm rat}(X)$ exists and gives
>   periodic orbits in bijection with closed points, of length $\log|\kappa(x)|$.
>   Nothing remains to be constructed.
> * **Assembled as indexing.** Corollary 2.1 …
> * **Not assembled as a correspondence.** Theorem 4.1: the bridge collapses the
>   transverse direction, so no cycle-level transport is available through it.
>
> What would be needed to assemble (b) fully: a map between the two settings that
> is transverse-preserving at closed fibers, or a construction of the Frobenius
> graphs directly inside the row-(a) divisor group. The second is the candid
> route, and it is a row-(a) task.

- **ANSWER: the cycles only, and only through the specific Morishita bridge
  $\Psi_F:\mathfrak X_F\to\mathscr X_F$.** Theorem 4.1 is a statement about $\Psi$
  ("$\Psi$ sets the $p$-component to zero at every point over $p$"), not about
  the Deninger space, which `107_242` explicitly certifies as existing and
  complete.
- **VERDICT for the Deninger space as a row-(a) candidate: UNTESTABLE — Gap G-8**,
  because no divisor group with a degree is attached to it in the sources read.
  *But note*: Deninger's own $W_{\rm rat}$ is precisely the object of §5, which
  **passes**. The row-(a) content of the Deninger route and the Witt route are
  the same content.

### 6.2 Haran's non-additive geometry, and the only actual square

Haran, arXiv:1709.05831v1 §10 ("Arithmetical surface, and new commutative
rings"), read: he constructs $\mathrm{Spec}\,\mathcal O_K\times_{\mathrm{Spec}\,\mathbb F\{\mu_K\}}\mathrm{Spec}\,\mathcal O_K$
and in particular
$$
 \mathrm{Spec}\,\mathbb Z\times_{\mathrm{Spec}\,\mathbb F\{\pm1\}}\mathrm{Spec}\,\mathbb Z
 =\{X_N\times_{\mathrm{spec}\,\mathbb F\{\pm1\}}X_M\}
$$
as a pro-object containing the affine dense sub-scheme
$\mathrm{spec}(\mathbb Z\otimes_{\mathbb F\{\pm1\}}\mathbb Z)$, with
$\mathbb Z^{\otimes n}$ generated by $\delta_1,\dots,\delta_n$ and the scalar
$(-1)$, and with every element of $(\mathbb Z^{\otimes n})_{Y,X}$ represented as
a quadruple $(F_y,G_x,\sigma,\varepsilon)$ — finite rooted trees with labelled
non-leaf vertices, a bijection of leaves, and signs.

This is, of everything read in this phase, **the only construction that is
literally the square $\mathrm{Spec}\,\mathbb Z\times_{\mathbb F_1}\mathrm{Spec}\,\mathbb Z$**
with both factors equal to $\mathrm{Spec}\,\mathbb Z$.

- **O1-TEST: structurally PASS.** $\mathbb Z^{\otimes n}$ has $n$ generating
  vectors $\delta_1,\dots,\delta_n$; the rank grows with $n$.
- **GROWTH-TEST: cannot fire.** There is no divisor group, no degree and no
  gauge in §10. Both failure modes are live: the tree data are Catalan-many, so
  an unnormalised count would *overshoot* as in Prop 3.5, while a naive rank
  count would give $\delta=1$.
- **VERDICT: UNTESTABLE — Gap G-7, and this is the frontier of a4-strong.**

**Gap G-7 (the Haran gap).** Define, on
$\mathrm{spec}(\mathbb Z\otimes_{\mathbb F\{\pm1\}}\mathbb Z)$, (i) a divisor
group with a $\mathbb Z\oplus\mathbb R$ (or $\mathbb Z^2\oplus\mathbb R^2$)
bigrading, (ii) a section functor $H^0$, (iii) a degree charging both
$\mathbb Z$-directions. Then run the two tests. Until (i)–(iii) exist, a4-strong
is not *false*, it is *unformulated*.

### 6.3 Durov, Toën–Vaquié, hyperrings

**NOT TESTED HERE.** No paper by Durov or Toën–Vaquié is in
`00-references/papers-nuevos`, and I read none in this session. I record no
verdict rather than a guessed one. What the criterion buys is that the test is
now one line: *exhibit the pair $(\text{rank}_m,\log\text{radius}_m)$ and check
both are $\Theta(m)$.* Any future file testing them owes exactly that pair.

### 6.4 The Bost–Connes system and its square

**NOT READ HERE**; but Theorem 2.1 applies to it *conditionally on the shape of
its dimension function*, and that shape is not in doubt: the BC system is a
$C^*$-dynamical system whose natural dimensions are KMS-state values and von
Neumann traces, and Remark 2.2 shows any such dimension satisfies (L). So:

- **VERDICT: CLOSED NEGATIVE conditional on (L)**, i.e. on the dimension being a
  trace. If someone exhibits a BC dimension that is *not* a trace — a genuine
  count of a lattice of growing rank — the verdict is void and the object must
  be re-tested. That is recorded as **R32** below.

### 6.5 Tropical surfaces (`mas-papers`)

Tropical surfaces do have genuine quadratic self-intersection and a Hodge index
(the `mas-papers` folder holds *Hodge theory for tropical varieties*,
*combinatorial tropical surfaces*, *Lefschetz $(1,1)$ in tropical geometry*).
**Titles only were read; no theorem is cited.** They are not over
$\mathrm{Spec}\,\mathbb Z$: the base is $\mathbb R$ or a value group.
The one place tropical geometry enters $\mathrm{Spec}\,\mathbb Z$ in the
material read is CC's scaling site, which §3.3 closes negative, and CC's reduced
square, which §3.4 shows overshoots. **VERDICT: OUT OF SCOPE, no verdict
claimed.**

---

## 7. The ledger

| # | candidate | source read | O1 | GROWTH | verdict | mechanism |
|---|---|---|---|---|---|---|
| 1 | CC $\overline{\mathrm{Spec}\,\mathbb Z}$, RR | 2205.01391 §2–3 | weak pass | **FAIL** $\delta{=}1$ | CLOSED NEGATIVE | rank one |
| 2 | CC arithmetic site | 1502.05580 §sectsquare | — | no $h^0$ | UNTESTABLE **G-5** | no dimension theory |
| 3 | CC scaling site $C_p$ | 1507.05818 Thm RRperiodic | pass | **FAIL** $\delta{=}1$ exact | CLOSED NEGATIVE | continuous (type-II) dimension |
| 4 | CC **square** of the arithmetic site | 1502.05580 §sectsquare | — | **OVERSHOOTS** $\ge e^{\sqrt N}$ | CLOSED NEGATIVE / **G-6** | Newton polygons are too many |
| 5 | CC Jacobian of $\overline{\mathrm{Spec}\,\mathbb Z}$ | 2602.15941 abstract | — | **FAIL** | CLOSED NEGATIVE | "torsion-free rank-1 groups" |
| 6 | CC absolute $\mathbb F_1$-curve + FF | 2606.06604 abstract | — | **FAIL** | CLOSED NEGATIVE | it is a curve, by name |
| 7 | Segal $\Gamma$-rings / $\mathbb S_\pm$-modules | 2205.01391 §2 | — | neutral | INSTRUMENT, not a space | measures whatever it is pointed at |
| 8 | **Arakelov arithmetic surfaces** | 2512.01811 Thm main1; `114_a_02` | **PASS** | **PASS** $\delta{=}2$ | **BUILT** (a4-weak) | rank $mk{+}1$, radius $e^{ma}$ |
| 9 | **Rational Witt $W_{\rm rat}$ / $W_J$** | 2508.05329 Thms 2.8, 5.1 | **PASS** | **PASS** $\delta{=}2$ | **BUILT-MODULO-GAP G-4** | additive filtration + $F_N$ + cycles |
| 10 | Borger $\Lambda$-geometry / big Witt | attribution **unverified** | **PASS** | **PASS** | as #9; attribution flagged | Frobenius lift at every prime |
| 11 | Deninger foliated system | `107_242` in full | — | no $h^0$ | UNTESTABLE **G-8**; row (b) intact | Thm 4.1 blocks *cycles through $\Psi$* only |
| 12 | **Haran** $\mathbb Z\otimes_{\mathbb F\{\pm1\}}\mathbb Z$ | 1709.05831 §§10–11 | formal Picard/sections; external sector in `a_12` | cannot fire | PARTIAL **G-7** — *the a4-strong frontier* | anti-diagonal kernel, gauge/Kunneth and intersection open |
| 13 | Durov, Toën–Vaquié, hyperrings | **not read** | — | — | NO VERDICT CLAIMED | — |
| 14 | Bost–Connes and its square | not read | — | (L) applies | CLOSED NEGATIVE *conditional on (L)* | trace $\Rightarrow$ linear (Thm 2.1) |
| 15 | Tropical surfaces | titles only | — | — | OUT OF SCOPE | not over $\mathrm{Spec}\,\mathbb Z$ |

**Summary in one line.** Of fifteen candidates, two pass ( #8, #9/#10 ), six are
closed negative with a named mechanism, four are untestable with the missing
datum written as a numbered gap, and three carry no verdict because the sources
were not read.

---

## 8. Verifier

`114_a_03_the_candidate_ledger.py`, run in full; every PASS line verbatim.

```
$ python3 114_a_03_the_candidate_ledger.py
A  114_a_01 Theorem 4.3 instantiated: bounded rank => delta <= 1
PASS  A1 for every fixed rank r0 in {1,2,5,50}, delta = 1 (not 2)   | r0=1: delta=1.00000; r0=2: delta=1.00000; r0=5: delta=1.00000; r0=50: delta=1.00000
PASS  A2 and delta = 2 requires rank ~ m: rank m+1 gives delta 2   | delta = 1.99641

B  CC scaling site, Thm RRperiodic of arXiv:1507.05818v2:  cdim H^0(D) = deg D
PASS  B1 cdim H^0(mD) = m deg D is homogeneous of degree EXACTLY 1   | delta = 1.000000000000  (exact, not asymptotic)
PASS  B2 their RR  cdim H^0(D) - cdim H^0(-D) = deg D  has NO quadratic term   | the formula is linear in D by inspection; a surface RR would carry D^2/2
PASS  B3 div(C_p)/P sits in 0 -> Z/(p-1)Z -> . -> R -> 0, so the DISCRETE part is FINITE   | finite discrete part => bounded lattice rank => Thm 4.3 forces delta <= 1

C  CC Spec Zbar, Jacobian (2602.15941), absolute curve (2606.06604): rank 1
PASS  C1 CC's own dim_1(floor(e^a)) = ceil(log_3(2e^a+1)) has delta = 1   | delta = 0.99605
PASS  C2 rank-1 objects (torsion-free rank-1 groups L with a norm) have delta <= 1   | Thm 4.3 with r0 = 1
PASS  C3 CC's own bracket deg/log2 <= dim_r <= r deg/log2 + r (107_146 sec.5) is linear   | matches Corollary C exactly

D  Arakelov / P^1_Z  (114_a_02):  delta = 2
PASS  D1 h0_theta(mD) = (m+1)m has delta = 2   | delta = 1.99641
PASS  D2 and it equals (1/2)(mD)^2 + (1/2)deg(mD)*(-deg K)/2 exactly   | (1/2)(mD)^2 = m^2 with D=(1,1); linear term m = a m

E  Rational Witt vectors:  W_J^{<=n}(Z) carries a rank-n lattice
PASS  E1 the Witt section lattice has rank n = deg_fin, growing linearly   | 1 + c_1 T + ... + c_n T^n  <->  (c_1,...,c_n) in Z^n
PASS  E2 with the coefficient gauge, log #sections has delta = 2   | delta = 2.02143
PASS  E3 the leading constant is 1 against (1/2)D^2 = ka m^2   | ratio at m=256 is 0.98490
PASS  E4 the Witt and P^1_Z section lattices are the SAME up to a torsor   | H^0(P^1_Z,O(k)) = Z[T]_{<=k} = Z^{k+1};  1 + T Z[T]_{<=n-1} = Z^n

F  CC reduced square: Newton polygons OVERSHOOT any polynomial dimension
PASS  F1 the n+1 points (j, j^2), j=0..n, are in strictly convex position   | hence every subset has a distinct convex hull
PASS  F2 so there are at least 2^{n+1} Newton polygons in the box [0,n] x [0,n^2]   | with N = n^2 the side, log #(polygons) >= sqrt(N) log 2
PASS  F3 with a box of side e^deg this lower bound is EXPONENTIAL in deg, not quadratic   | deg=10: >= 1.029e+02 vs deg^2 = 100; deg=20: >= 1.527e+04 vs deg^2 = 400; deg=40: >= 3.363e+08 vs deg^2 = 1600

G  the verdict table, checked for internal consistency
  CC Spec Zbar (arXiv:2205.01391)              rank 1          delta = 1
  CC arithmetic site (1405.4527/1502.05580)    rank 1          delta = 1
  CC scaling site C_p (1507.05818)             rank 0 (finite) delta = 1
  CC Jacobian of Spec Zbar (2602.15941)        rank 1          delta = 1
  CC absolute curve (2606.06604)               rank 1          delta = 1
  Arakelov surface / P^1_Z (114_a_02)          rank m k + 1    delta = 2
  Rational Witt W_J^{<=mk}(Z)                  rank m k        delta = 2
PASS  G1 every rank-bounded candidate is assigned delta = 1 and every rank-growing one delta = 2   | consistent with 114_a_01 Thm 3.3 and Thm 4.3
PASS  G2 exactly two candidates in the table pass the GROWTH-TEST   | Arakelov surfaces and rational Witt vectors
PASS  G3 no candidate with a rank-1 section module passes

VERDICT: ALL CHECKS PASS
$ echo $?
0
```

No check in this verifier was weakened; it ran green on the first execution.

---

## 9. Circularity audit for this file

- **Theorem 2.1** quantifies over dimension functions satisfying (L). CLEAN: no
  zero of $\xi$, no sign of a quadratic form. NOT VACUOUS: (L) is satisfied by
  CC's own $\mathrm{cdim}$, by their Theorem `RRperiodic`.
- **Theorem 2.3** is `114_a_01` Thm 4.3, already audited CLEAN there.
- **Proposition 3.5** is a finite convexity computation over $\mathbb Z^2$.
  CLEAN, NOT VACUOUS.
- **Proposition 5.3** is a lattice count. CLEAN.
- Every verdict in §7 is either (i) a proof from Theorem 2.1 or 2.3, (ii) a
  quotation of a theorem in a source read, or (iii) an explicit "no verdict
  claimed". No verdict is derived from RH, from the truth of RH, or from any
  statement about the zeros.
- **Vacuity check on the negative verdicts.** None of them is vacuously true: in
  each case the hypothesis is verified against the source (rank one for #1,#5,#6;
  (L) for #3; the semiring of Newton polygons for #4).

---

## 10. Gaps

- **Gap G-4 (Witt).** *Statement:* there exists a norm $\|\cdot\|$ on
  $W_J^{\le n}(\mathbb Z)$, compatible with $F_N$ and $V_N$, and a symmetric
  bilinear form on the resulting gauged divisor group $\mathbb Z\oplus\mathbb R$
  with $\langle f_{\mathrm{fin}},f_\infty\rangle=1$, such that
  $h^0(D)=\log\#\{x:\|x\|\le e^{a}\}$ satisfies
  $h^0(mD)=\tfrac12(mD)^2+O(m\log m)$.
  **Status: OPEN.** **Closes if:** the logarithmic Mahler measure is shown to be
  comparable to the coefficient norm on $W_J^{\le n}$ uniformly in $n$ up to
  $e^{O(n)}$, which suffices by `114_a_02` Thm 5.1's squeeze argument.
  **Hard? No, and not RH-related** — it is Jensen's formula plus Mahler's
  inequalities. This gap is *technical*.
- **Gap G-5 (CC arithmetic site).** *Statement:* a divisor group, degree and
  section functor on $\widehat{\mathbb N^\times}$. **Status: OPEN.** **Closes if:**
  someone defines them. **Hard?** Unknown; but Theorem 2.1 predicts the answer
  will be $\delta=1$ if the dimension is a trace.
- **Gap G-6 (CC reduced square).** *Statement:* a section functor on the reduced
  square whose sections in degree $d$ number $e^{O(d^2)}$ rather than
  $e^{\Omega(e^{d/2})}$. **Status: OPEN.** **Closes if:** the Newton polygons are
  cut down by a vertex bound $v\le\Theta(d)$, restoring a rank parameter.
  **Hard? No** — but doing so re-imports exactly the rank parameter that
  Theorem 2.3 says is the real content, so it would make the square into an
  instance of the mechanism of `114_a_02`, not an alternative to it.
- **Gap G-7 (Haran / a4-strong).** *Statement:* a divisor group with a bigraded
  degree and a section functor on
  $\mathrm{spec}(\mathbb Z\otimes_{\mathbb F\{\pm1\}}\mathbb Z)$, with both
  $\mathbb Z$-directions charged to $\deg$. **Status: OPEN.** **Closes if:** such
  a structure is written down; then the two tests fire in one line.
  **Hard? Unknown, and this is the candid frontier of a4-strong.** Not obviously
  RH-equivalent: it is a definitional task about a construction that already
  exists.
- **Gap G-8 (Deninger space).** *Statement:* a divisor group with a degree on
  Deninger's foliated dynamical system. **Status: REDUCED-TO(G-4)**: the row-(a)
  content of the Deninger route is $W_{\rm rat}$, which is candidate #9.

---

## 11. Refutation conditions, pre-registered (continuing from R30)

- **R31.** If a candidate is recorded here as CLOSED NEGATIVE and someone later
  exhibits on it a section family with rank$_m=\Theta(m)$ and
  $\log$radius$_m=\Theta(m)$, the verdict is void and must be re-run. The
  verdicts are conditional on the section modules being as the sources describe
  them, and nothing more.
- **R32.** The Bost–Connes verdict (#14) is conditional on hypothesis (L). A
  Bost–Connes dimension that is a genuine count of an unbounded-rank lattice
  voids it.
- **R33.** If any future file assigns a verdict to Durov, Toën–Vaquié, hyperrings
  or tropical surfaces without exhibiting the pair
  $(\text{rank}_m,\log\text{radius}_m)$, it fires this condition. §6.3 and §6.5
  deliberately claim nothing; a claim without that pair is worse than silence.
- **R34.** If a future file reports Haran's square as *refuted*, it fires this
  condition unless it first supplies the missing degree and gauge of Gap G-7.
  a4-strong is currently *unformulated*, not false.

---

## 12. Scope

**Proved here.**

- Theorem 2.1 (continuous-dimension obstruction) and Remark 2.2 identifying (L)
  with the type-II trace property.
- Proposition 3.5 (at least $2^{\lfloor\sqrt N\rfloor+1}$ convex lattice
  polygons in $[0,N]^2$) and Corollary 3.6 (the reduced square overshoots).
- Proposition 5.3 (rational Witt vectors carry rank-$n$ lattices with
  $\delta=2$).
- The verdicts of §7 for candidates #1, #3, #4, #5, #6, #8, #9/#10, #14
  (conditional), each with its mechanism.

**Read from source.**

- arXiv:1507.05818v2 Theorem `RRperiodic` and the "type II normalized traces"
  sentence, both quoted verbatim.
- arXiv:1502.05580v1 §`sectsquare` (structure sheaf = Newton polygons; Frobenius
  correspondences $\Psi(\lambda)$; Thm `thmcomp0`); confirmed by grep that no
  divisor/degree/$h^0$/Riemann–Roch occurs in that section.
- arXiv:2602.15941v1 and arXiv:2606.06604v1 abstracts, quoted verbatim.
- arXiv:2508.05329v1 Introduction, Theorem 2.8, Theorem 5.1, quoted verbatim.
- arXiv:1709.05831v1 §10 (the construction of
  $\mathbb Z\otimes_{\mathbb F\{\pm1\}}\mathbb Z$).
- `107_242` §0, Thm 4.1, §5, quoted verbatim.
- arXiv:2205.01391v2 §2–3; `107_146` §5.

**Verified numerically.**

- $\delta=1$ for every fixed rank $r_0\in\{1,2,5,50\}$ and $\delta=2$ for
  rank $\sim m$.
- $\delta=1$ exactly for CC's $\mathrm{cdim}$; $\delta=0.99605$ for CC's
  own rank-one absolute dimension.
- $\delta=2$ for $\overline{\mathbb P^1_{\mathbb Z}}$ ($1.99641$) and for the
  Witt lattice ($2.02143$, leading ratio $0.98490$).
- Strict convex position of $\{(j,j^2)\}_{j\le80}$ and the resulting
  $2^{n+1}$ bound.

**Not established.**

- Any verdict for Durov, Toën–Vaquié, hyperrings, or tropical surfaces (§6.3,
  §6.5). No source was read; no verdict is claimed.
- The Borger attribution (§5.5(1)). The object is tested; the attribution is not
  verified.
- Gaps G-4 through G-8.
- That any passing candidate has anything to do with $\xi$. That is Gap G-3 of
  `114_a_02`, and `114_a_04` shows it is RH-hard.
