# 113.08 — The two polar coordinates are the two rulings, and what the index engine actually needs

> **What this file does.** Three things.
>
> **(1) Cross-validation.** Our $\mathfrak T$ is checked against a *published*
> functional in a completely different grouping. Connes' essay
> (arXiv:1509.05576, eq. (18)) defines
> $$N(h)=\sum_n\Lambda(n)h(n)+\int_1^\infty\frac{u^2h(u)-h(1)}{u^2-1}\,d^\times u+c\,h(1),
> \qquad c=\tfrac12(\log\pi+\gamma),$$
> and his criterion (eq. (17)) is $\mathrm{RH}\iff\mathfrak s(f,f)\le0$ for all
> real $f$ with $\int f\,d^\times u=\int f\,du=0$, where $\mathfrak s(f,g)=N(f\star\widetilde g)$.
> We find, to 18 digits, $\ \mathfrak T(f\star\widetilde f)=2N(f\star\widetilde f)$,
> and that Connes' two side conditions are *literally*
> $\widehat f(0)=0$ and $\widehat f(1)=0$. So 113_07 Proposition 4.1 **is**
> Connes' published criterion, and 113_06 Theorem 2.2 extends it from
> compactly supported $f$ to the $*$-algebra $\mathcal D$.
>
> **(2) The rulings.** The two polar coordinates $\widehat f(0),\widehat f(1)$
> of $I_\partial$ carry a hyperbolic plane, and that plane is exactly the pair
> of rulings $F_v,F_h$ with $F_v^2=F_h^2=0$, $F_v\!\cdot\!F_h=1$,
> $H=F_v+F_h$, $H^2=2$ — so requirement **d2 is re-derived intrinsically**,
> inside our own pairing, rather than imported.
>
> **(3) The candid verdict on the index engine.** Connes' Lemma 2.1 is the
> Hodge-index substitute the programme has been aiming at. We verify it, and
> then show that **in our coordinates its hypothesis (2) is precisely the
> contrapositive of Weil positivity**. Lemma 2.1 therefore supplies no
> arithmetic whatever: it is an *interface*, converting "effectivity $\Rightarrow$
> nonzero pairing with a ruling" into the index inequality. This is worth
> stating loudly, because it forecloses the reading in which Lemma 2.1 is
> itself progress. What it buys is a precise specification of the only two
> statements the geometry (rows d3–d5) has to deliver. Those are
> pre-registered here as **(E)** and **(R)**.

$$\boxed{\texttt{CROSS\_VALIDATION\_VS\_CONNES\_N: PASS (}\mathfrak T=2N\texttt{, 18 digits)}}$$
$$\boxed{\texttt{d2 (POLARIZATION }H=F_v+F_h,\ H^2=2\texttt{): RE-DERIVED INTRINSICALLY}}$$
$$\boxed{\texttt{CONNES\_LEMMA\_2.1: VERIFIED, AND SHOWN TO BE ARITHMETICALLY EMPTY}}$$
$$\boxed{\texttt{ROW\_D\_REQUIREMENT: REDUCED TO (E) + (R), PRE-REGISTERED}}$$

---

## 1. Cross-validation against the published functional

> ### Theorem 1.1 (Connes' side conditions are our polar coordinates)
> For $f\in\mathcal D$,
> $$\int_0^\infty f(u)\,d^\times u=\widehat f(0),
> \qquad \int_0^\infty f(u)\,du=\widehat f(1).$$

**Proof.** Immediate from $\widehat f(s)=\int_0^\infty f(u)u^s\,d^\times u$ at
$s=0$ and $s=1$, since $u\,d^\times u=du$. $\square$

Trivial, but it settles the dictionary: the class over which Connes quantifies
in eq. (17) is exactly $\mathcal D^\circ=\{f:\widehat f(0)=\widehat f(1)=0\}$
of 113_07 Proposition 4.1. This is a real check on our coordinate model, not a
restatement — the two polar slots of 107_241's model were introduced there as
the residues at $s=0,1$ of $\xi'/\xi$, and it is not automatic that they
coincide with the two elementary integrals Connes constrains.

> ### Theorem 1.2 (the two archimedean groupings agree; verified, constant included)
> Let $f\in\mathcal D$ be real, $h=f\star\widetilde f$. Then $h(1/u)=u\,h(u)$,
> hence $h(1/n)/n=h(n)$ and $P(h)=2\sum_n\Lambda(n)h(n)$; and
> $$\mathfrak T(h)=P(h)+W_\infty(h)=2\,N(h).$$

**Proof of the symmetry.** By 113_07 Lemma 1.2, the balanced profile of $h$ is
$H=F*\overline{F(-\cdot)}$; for real $F$ this is $H(x)=\int F(t)F(t-x)\,dt$,
which is even. Hence $\tilde h(x)=e^{-x/2}H(x)$ satisfies
$\tilde h(-x)=e^{x/2}H(x)=e^{x}\tilde h(x)$, i.e. $h(1/u)=u\,h(u)$. $\square$

The factor $2$ is exactly this one-sided/two-sided count, and it is consistent
with Connes writing $\tfrac12 D(f)\!\cdot\!D(f)=\mathfrak s(f,f)$; so
$$\mathfrak s(f,f)=N(h)=\tfrac12\mathfrak T(h)=\tfrac12 Q(f).$$

**The equality $\mathfrak T(h)=2N(h)$ itself is verified, not re-derived here.**
Proving it amounts to the classical identification of the two standard forms of
the archimedean Weil term — the $\Gamma$-kernel Fourier integral $-A(h)$ of
113_06 Definition 2.1 against Connes' regularised
$\int_1^\infty(u^2h(u)-h(1))/(u^2-1)\,d^\times u+c\,h(1)$ — which goes back to
Weil (1952) and which we quote rather than re-prove. On the probe
$F(x)=e^{-ax^2}\cos(bx)$, $b=14$, $a=b/2\pi$, at 40-digit working precision:

| quantity | value |
|---|---|
| $\sum_n\Lambda(n)h(n)$ | $-0.18414626360628602337$ |
| $\int_1^\infty\frac{u^2h(u)-h(1)}{u^2-1}d^\times u$ | $-0.52835989820926327685$ |
| $c\,h(1)$, $c=0.860972775375$ | $+0.36144754402439858216$ |
| **$N(h)$ (Connes)** | $-0.35105861779115071806$ |
| $P(h)$ (ours) | $-0.36829252721257204674$ |
| $A(h)$ (ours) | $+0.33382470836972939117$ |
| **$\mathfrak T(h)=P-A$ (ours)** | $-0.70211723558230143791$ |
| $\mathfrak T/N$ | $2.0000000000000000051$ |
| $\mathfrak T-2N$ | $-1.78\times10^{-18}$ |

The match is not special to a probe in $\mathcal D^\circ$. On two further probes
of the same family, with $\widehat f(0),\widehat f(1)$ both nonzero:

| $(a,b)$ | $N(h)$ | $\mathfrak T(h)$ | $\mathfrak T/N$ | $|\mathfrak T-2N|$ |
|---|---|---|---|---|
| $(b/2\pi,\,14)$ | $-0.35105861779115071806$ | $-0.70211723558230143791$ | $2.0000000000000000051$ | $1.8\times10^{-18}$ |
| $(1.0,\,3.0)$ | $+0.021172123116328140875$ | $+0.042344246232656279058$ | $1.9999999999999998729$ | $2.7\times10^{-18}$ |
| $(0.6,\,0)$ | $+6.4487662867933214405$ | $+12.897532573586642874$ | $1.9999999999999999989$ | $6.9\times10^{-18}$ |

Note that $N$ changes sign across the family: the middle and last probes have
$N>0$, which is *not* a violation of Connes' criterion, because neither lies in
$\mathcal D^\circ$ — for them the positive polar term
$2\mathrm{Re}[\widehat f(0)\overline{\widehat f(1)}]$ dominates. Only the
first probe satisfies the two side conditions, and it is the one with
$\mathfrak T<0$. That is exactly the behaviour the criterion predicts, and it
is a check on the coordinate identification of Theorem 1.1.

Two things follow beyond the identity itself. First, $\mathfrak T(h)=-0.702117236$
agrees with the *spectral* side $Q(f)=-0.702117236$ computed in the 113_07
verifier from $\widehat f(0),\widehat f(1)$ and the zeros — three independent
routes to one number. Second, since Connes' grouping carries the explicit
constant $c=\tfrac12(\log\pi+\gamma)$ and ours carries none, the exact match
**independently confirms that our $A(h)$ has no missing additive constant** —
the point argued on other grounds in 113_06 §3, now checked against the
literature.

---

## 2. The two rulings

Work in the coordinate model of 107_241: $V=\mathbb C^{\{0,1\}}\oplus\mathbb C^{Z}$,
$x\mapsto(\widehat x(0),\widehat x(1),(\widehat x(\rho))_\rho)$, with

$$\mathfrak s(x,y)=\widehat x(0)\overline{\widehat y(1)}+\widehat x(1)\overline{\widehat y(0)}
-\sum_\rho m_\rho\widehat x(\rho)\overline{\widehat y(\rho')},\qquad\rho'=1-\bar\rho.
\tag{2.1}$$

> ### Definition 2.1
> $F_v:=(1,0,\mathbf 0)$ and $F_h:=(0,1,\mathbf 0)$ in $V$.

> ### Proposition 2.2 (d2, intrinsically)
> $$\mathfrak s(F_v,F_v)=\mathfrak s(F_h,F_h)=0,\qquad \mathfrak s(F_v,F_h)=\mathfrak s(F_h,F_v)=1,$$
> so $\{F_v,F_h\}$ spans a hyperbolic plane; and with $H:=F_v+F_h$,
> $$H^2:=\mathfrak s(H,H)=2 .$$
> Moreover for every $x\in V$,
> $$\mathfrak s(x,F_v)=\widehat x(1),\qquad \mathfrak s(x,F_h)=\widehat x(0). \tag{2.2}$$

**Proof.** Direct evaluation of (2.1); the zero coordinates of $F_v,F_h$ vanish,
so the $\rho$-sum never contributes. $\square$

This is requirement **d2** of the backward map — recorded in the programme as
"met, $H=F_v+F_h$, $H^2=2$" — now obtained *inside* the pairing rather than
posited alongside it. The names are earned: on a product of curves the two
rulings are the fibre classes, they are isotropic, they meet once, and their
sum is the natural polarization. Here the isotropy of $F_v,F_h$ is the
statement that the polar part of $\xi'/\xi$ contributes only the cross term
$\widehat h(0)+\widehat h(1)$ and no square — which is 113_06 Theorem 2.2
Step 3.

> ### Remark 2.3 (realisation in $\mathcal D$ — **closed in 113_09**)
> $F_v$ and $F_h$ are elements of the coordinate space $V$. Whether they lie in
> the *image* of $\mathcal D$ — i.e. whether some $f\in\mathcal D$ has
> $\widehat f(0)=1$, $\widehat f(1)=0$ and $\widehat f(\rho)=0$ for every zero
> $\rho$ — was left open when this file was written. Nothing below needed it:
> §3 works in $V$, and 113_07 Proposition 4.1 was proved directly on
> $\mathcal D^\circ$, which *is* exhibited nonempty.
>
> **It is now settled affirmatively.** 113_09 Theorem 3.1 realises them by
> $$\widehat f_v(s)=-2(s-1)\,\xi(s),\qquad \widehat f_h(s)=2s\,\xi(s),$$
> which lie in $\mathcal D_\theta$ for *every* $\theta>0$ because $\xi$ decays
> like $e^{-\pi|t|/4}$ in vertical strips, and which have the required
> coordinates because $\xi(0)=\xi(1)=\tfrac12$ and $\xi$ vanishes on $\mathcal Z$.
> The polarization is $\widehat{(f_v+f_h)}(s)=2\xi(s)$. Consequently the
> projection in the proof of Lemma 3.1 below stays inside $\mathcal D$
> (113_09 Corollary 3.2), and Theorem 3.3 holds with $E=\mathcal D$ and no gap.
> 113_09 Theorem 4.1 also verifies the four numbers of Proposition 2.2
> *arithmetically*, from a prime sum and the digamma kernel with no zero of
> $\xi$ entering.

---

## 3. Connes' index engine, and exactly how much it gives

> ### Lemma 3.1 (Connes, essay Lemma 2.1, eq. (13) — quoted)
> Let $\mathfrak s$ be a symmetric bilinear form on a vector space $E$ and
> $\xi_0,\xi_1\in E$ with
> 1. $\mathfrak s(\xi_j,\xi_j)=0$ and $\mathfrak s(\xi_0,\xi_1)=1$;
> 2. for any $x\in E$ with $\mathfrak s(x,x)>0$ one has $\mathfrak s(x,\xi_0)\ne0$
>    or $\mathfrak s(x,\xi_1)\ne0$.
>
> Then $\ \mathfrak s(x,x)\le2\,\mathfrak s(x,\xi_0)\,\mathfrak s(x,\xi_1)$ for all $x\in E$.

**Proof** (reconstructed; the essay states the lemma without proof). Put
$a=\mathfrak s(x,\xi_1)$, $b=\mathfrak s(x,\xi_0)$ and
$y:=x-a\xi_0-b\xi_1$. Using (1),
$$\mathfrak s(y,\xi_0)=b-a\cdot0-b\cdot1=0,\qquad
\mathfrak s(y,\xi_1)=a-a\cdot1-b\cdot0=0,$$
$$\mathfrak s(y,y)=\mathfrak s(x,x)-2ab-2ba+2ab\cdot\mathfrak s(\xi_0,\xi_1)=\mathfrak s(x,x)-2ab.$$
By the contrapositive of (2), $\mathfrak s(y,y)\le0$. $\square$

> ### Proposition 3.2 (hypothesis (1) holds by construction)
> With $E=V$, $\xi_0=F_v$, $\xi_1=F_h$, hypothesis (1) of Lemma 3.1 is exactly
> Proposition 2.2, hence holds unconditionally.

> ### Theorem 3.3 (hypothesis (2) *is* Weil positivity — the engine is arithmetically empty)
> With $E=V$, $\xi_0=F_v$, $\xi_1=F_h$:
> 1. the projection of Lemma 3.1's proof is
>    $y=x-\widehat x(0)F_v-\widehat x(1)F_h$, which has
>    $\widehat y(0)=\widehat y(1)=0$ and $\widehat y(\rho)=\widehat x(\rho)$ for
>    every $\rho$ — i.e. $y$ is $x$ with the polar coordinates deleted and the
>    zero coordinates untouched;
> 2. consequently
>    $$\mathfrak s(y,y)=\mathfrak s(x,x)-2\mathrm{Re}\,\bigl[\widehat x(0)\overline{\widehat x(1)}\bigr]
>    =-\sum_\rho m_\rho\widehat x(\rho)\overline{\widehat x(\rho')};$$
> 3. hypothesis (2) of Lemma 3.1 is **logically equivalent** to
>    $$\mathfrak s(z,z)\le0\quad\text{for all }z\text{ with }\widehat z(0)=\widehat z(1)=0,$$
>    which by 113_07 Proposition 4.1 is equivalent to RH;
> 4. and the conclusion of Lemma 3.1 is likewise equivalent to the same
>    statement.
>
> Therefore Lemma 3.1 contributes **no** arithmetic information: on the
> hyperbolic-plane-plus-zeros model its hypothesis, its conclusion, and Weil
> positivity are three names for one statement.

**Proof.** (1) By (2.2), $a=\mathfrak s(x,\xi_1)=\widehat x(0)$ and
$b=\mathfrak s(x,\xi_0)=\widehat x(1)$, so $y=x-\widehat x(0)F_v-\widehat x(1)F_h$;
$F_v,F_h$ have zero $\rho$-coordinates, and subtracting them cancels the polar
slots. (2) Evaluate (2.1) on $y$. (3) ($\Rightarrow$) If $\widehat z(0)=\widehat z(1)=0$
then $\mathfrak s(z,F_v)=\mathfrak s(z,F_h)=0$, so (2) forces
$\mathfrak s(z,z)\le0$. ($\Leftarrow$) If $\mathfrak s(x,x)>0$ and
$\mathfrak s(x,F_v)=\mathfrak s(x,F_h)=0$, then $x$ itself is such a $z$,
contradiction. (4) The conclusion at $x$ with $\widehat x(0)=\widehat x(1)=0$
reads $\mathfrak s(x,x)\le0$; conversely (2)+(1) give the conclusion by
Lemma 3.1. $\square$

> ### Why this matters
> The programme has repeatedly treated "obtain the Hodge index / Castelnuovo–Severi
> inequality" as the goal of rows d3–d5. Theorem 3.3 says the index inequality
> is *free* once hypothesis (2) is in hand, and that hypothesis (2) is the whole
> problem. So d3–d5 are not needed to produce an inequality; they are needed to
> produce **effectivity**, which is the only known route to (2) that is not
> circular. On a genuine algebraic surface, (2) holds because: $D^2>0$ plus
> Riemann–Roch forces $D$ or $-D$ to be linearly equivalent to a nonzero
> effective divisor, and a nonzero effective divisor has strictly positive
> intersection with at least one ruling. Both steps are geometry, not analysis,
> and neither is available here.

---

## 4. Pre-registration: the two statements the geometry must deliver

For $f\in\mathcal D$ write $D_f$ for the associated divisor-like object and
$Q(f)=\mathfrak s(D_f,D_f)$ as in 113_07 (3.3). Rows d3–d5 are hereby reduced
to the following two statements, which 113_11 and 113_13 will target and which
are recorded now so that they cannot be quietly weakened later.

> **(E) Effectivity dichotomy (what $h^0$ is for).**
> There is a functor $h^0$ on the divisor objects of $\mathcal D$, taking values
> in $\mathbb Z_{\ge0}\cup\{\infty\}$ or in $\mathbb R_{\ge0}$, such that
> $$Q(f)>0\ \Longrightarrow\ h^0(D_f)>0\ \text{ or }\ h^0(-D_f)>0 .$$

> **(R) Ruling positivity (what effectivity is for).**
> For every nonzero $D$ with $h^0(D)>0$,
> $$\mathfrak s(D,F_v)\ne0\quad\text{or}\quad\mathfrak s(D,F_h)\ne0,$$
> equivalently $\widehat{\,\cdot\,}(1)\ne0$ or $\widehat{\,\cdot\,}(0)\ne0$ in
> the coordinates of §2.

**(E) + (R) $\Rightarrow$ hypothesis (2) of Lemma 3.1 $\Rightarrow$ RH** (by
Theorem 3.3(3) and 113_07 Proposition 4.1) — provided (E) and (R) are
established *without* using Weil positivity, a zero of $\xi$, a Li
coefficient, or a positive part of a Weil-type form. That proviso is the whole
content of the source rule, and by Theorem 3.3 it is now the only thing
standing between the programme and row (d).

### Pre-registered refutation conditions

The following outcomes, if found, refute the (E)+(R) route and must be recorded
as such rather than worked around:

- **R1.** Any $h^0$ satisfying (E) whose construction quantifies over the zeros
  of $\xi$, or over the sign of $Q$, is circular and does not count.
- **R2.** If $h^0$ is deformation-blind in the sense of paper 40's
  deformation-blindness Proposition — i.e. $h^0$ is constant on
  $\sim$-classes while the index depends on divisor position, and a witness
  $x\sim y$ with $\kappa(x)\ne\kappa(y)$ exists — then (E) is unreachable by
  that $h^0$, unless the escape clause is met (a spectral gap **and** a
  continuous Fredholm path are supplied).
- **R3.** If the candidate $h^0$ fails the Davenport–Heilbronn test — it must
  *fail* for a DH-type function with no Euler product, must preserve the CCM
  divisor, and must obtain its positivity from arithmetic source structure
  rather than assume it — the construction is not detecting arithmetic.
- **R4.** If (R) fails for some nonzero effective $D$, the rulings are not
  ample enough and $F_v,F_h$ must be replaced; note that Proposition 2.2 pins
  them completely, so there is no freedom here — a failure of (R) would refute
  the hyperbolic-plane model itself.

### One route already closed

The tropical/max-plus route to $h^0$ — $\mathrm{cdim}^{(2)}$ of 107_232/233,
relocated in 107_236 — **cannot** carry (E), and this is now settled by a
theorem already in the corpus rather than by conjecture:

- $\mathrm{cdim}^{(2)}H^0_{\rm ext}(D\boxtimes E)=\max(\deg D,0)\max(\deg E,0)$
  (107_236 eq. (4.2)) is defined only for **external** divisors $D\boxtimes E$,
  is bidegree $(1,1)$, and contains no $D^2$;
- 107_237 Theorem 2.1 proves that for $f$ continuous and nonzero on an
  interval, $D_f=\int f(\lambda)\Psi_\lambda\,d^\times\lambda$ **is not the
  divisor of any finite-PL rational section of $\mathcal O_{\mathscr S^2}$** —
  the very sheaf 107_236 builds. The mixed divisors provably do not live there.
- 107_236 §5 lists the same gap in its own words: "extend from external
  divisors to the intrinsically mixed correspondence divisors"; and
  107_232 §6, 107_233 §5, 107_234 §5, 107_237 §5, 107_238 §5 each record
  "$H^1$, Serre duality, RR" as absent. Every verifier in 107_234–238 prints
  `ROW_A_STATUS: PARTIAL`.

So 113_11 must build $h^0$ somewhere other than the max-plus square. That is a
constraint, not a defeat, and it is better to have it in writing.

---

## 5. Scope

**Proved here.** Theorem 1.1. The symmetry $h(1/u)=u\,h(u)$ and
$P(h)=2\sum\Lambda(n)h(n)$ for real $f$ (Theorem 1.2, first part).
Proposition 2.2 (the rulings, $H^2=2$, and formula (2.2)). Lemma 3.1 with a
proof supplied (the essay states it without one). Proposition 3.2.
Theorem 3.3 (all four parts) — the reduction of the index engine to Weil
positivity.

**Read from source, not re-derived.** Connes, arXiv:1509.05576: Lemma 2.1
(= our Lemma 3.1), eq. (13); eq. (17) `negcrit` (the criterion); eq. (18)
`negcrit1` (the functional $N$, with $c=\tfrac12(\log\pi+\gamma)$); the
grey-box target $\tfrac12D.D=\mathfrak s(f,f)$ of §4.3.2. 107_236 eq. (4.2)
and §5; 107_237 Theorem 2.1. 107_241's coordinate model. The classical
identity of the two archimedean Weil groupings (Weil 1952), used in
Theorem 1.2 — **quoted, verified, not re-derived**.

**Verified numerically** (60/60 checks, exit 0). Theorem 1.1 by direct
quadrature on $(0,\infty)$, *not* by the log-substitution that would make it
tautological. Theorem 1.2, including the closed form $H=F*F$ checked against
quadrature. $\mathfrak T(h)=2N(h)$ to 18 digits at 40-digit working precision on
three probes, with the full term-by-term tables of §1; and the constant
$c=\tfrac12(\log\pi+\gamma)$ shown load-bearing (deleting it destroys the match
by $1.09$), which is what pins our $A(h)$ exactly. Proposition 2.2 and (2.2) in
the coordinate model, *and* re-run in a model with off-line zeros and
multiplicities $2,3$ — the four numbers $(0,0,1,2)$ are unchanged, so the
rulings carry no zero data. Hermitian symmetry of $\mathfrak s$.
Theorem 3.3(1)–(2) on a 50-element random ensemble.

Two further checks worth naming:

- **Negative control (F).** Moving one zero off the line to $\rho=0.7$ (so
  $\rho'=0.3$) and taking $w$ with $\widehat w(\rho)=1$, $\widehat w(\rho')=-1$
  gives $\mathfrak s(w,w)=+2$ with $\mathfrak s(w,F_v)=\mathfrak s(w,F_h)=0$:
  hypothesis (2) fails **and** the conclusion of Lemma 3.1 fails. The identical
  witness pattern in the all-on-line model gives $\mathfrak s=-2$. So Lemma 3.1
  is not vacuous, hypothesis (2) is load-bearing, and its failure is caused by
  the off-line zero and nothing else — Theorem 3.3(3) exhibited rather than
  merely argued.
- **Independent confirmation of 113_06 Theorem 2.2 (G).** For all three probes
  the spectral side $Q$ (polar coordinates and zeros, float64) equals the
  arithmetic side $\mathfrak T$ (prime sum and $\Gamma$-kernel integral,
  mpmath at 40 digits) — two disjoint computations, agreeing to $9.0\times10^{-15}$,
  $1.1\times10^{-14}$ and $4.9\times10^{-8}$ (the last limited by prime-sum
  truncation at $n\le4000$ for the slowly-decaying Gaussian). This is
  independent of the Connes comparison and of everything in §§2–4.

**Not established, and explicitly not claimed.** (E). (R). Hypothesis (2) of
Lemma 3.1. Weil positivity. The realisation of $F_v,F_h$ inside $\mathcal D$
(Remark 2.3). The re-derivation of $\mathfrak T=2N$ from first principles.
Anything about rows (a), (b), (c). **Anything about RH.**

## 6. Verifier

`113_08_the_two_rulings_and_the_index_engine.py` — exits 0 with
`VERDICT: ALL CHECKS PASS`. Zeros of $\xi$ appear only inside numerical checks
of classical identities quoted from 113_06 and from the Connes essay. No
definition in this file uses a zero of $\xi$, a Li coefficient, or a positive
part of a Weil-type form; in particular the probe parameter $b=14$ is a round
number chosen for numerical bite, not a zero ordinate.
