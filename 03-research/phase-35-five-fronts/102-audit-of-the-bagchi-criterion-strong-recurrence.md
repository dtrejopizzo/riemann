# Doc 102 — Audit of the Bagchi criterion: strong recurrence and Voronin universality

**Phase 35 — Five fronts ·**
**Status: complete audit — mechanism run through discriminator D0 (I1, I2a, I2b, I3, I4)**

---

## 0. Executive summary

This document closes an explicit gap in the program: "universality" has been audited
only in the GUE / random matrix sense (gap-universality, FAIL I1/I3 in
`meta-docs/DISCRIMINATOR-hardening-phase-A.md`). **Voronin universality** — the
self-approximation of $\zeta$ in the strip $1/2<\mathrm{Re}(s)<1$ — and the **Bagchi
criterion** (RH $\iff$ strong recurrence of $\zeta$) never went through the discriminator.
They are objects distinct from GUE statistics: they live in topological dynamics and
ergodic theory, not in spectral statistics.

Audit results:

1. The hard direction of the Bagchi criterion (recurrence $\Rightarrow$ RH) contains an
   **amplification mechanism** (Rouché + unconditional zero density) that is **not a
   positivity**: it is the only mechanism in the corpus that turns ONE off-critical zero
   into a contradiction with an unconditional theorem. The mechanism itself is non-circular.
2. The circularity does not disappear: it **relocates into the premise**. Strong
   recurrence is RH-equivalent (Bagchi's theorem), and its only known route of proof
   (universality) requires the target function to be non-vanishing — exactly the missing
   information.
3. **Main finding (question iv):** the "individual orbit vs. generic orbit" obstruction
   of Bagchi's ergodic framework is **NOT** a failure of unique ergodicity (the Kronecker
   flow on the Bohr torus is minimal and uniquely ergodic, and the arithmetic point
   $\omega_0$ **is recurrent on the torus, unconditionally**). The obstruction is the
   **divergence of the Euler observable over the arithmetic orbit**: membership of the
   orbit of $\omega_0$ in the convergence set of the observable is itself RH-equivalent
   (Proposition 7.2). This identifies the ergodic obstruction with **MW-2** (arithmetic
   propagation wall) word for word, and its verification with **MW-7** (Hadamard barrier).
4. Discriminator: **I1 checked · I2a partial · I2b failed · I3 checked · I4 checked → FAIL I2b**, the same
   profile as Connes (genuine independent structure, no decisive theorem).

**VERDICT: ROUTE CLOSED** as a proof route — with one transferable asset registered
(§9): the Rouché-density amplifier, the only non-CAP, individual-resolving mechanism in
the corpus.

---

## 1. Position in the program: the gap this doc closes

The adversarial table of `DISCRIMINATOR-hardening-phase-A.md` audits ~30 programs. The
entries "RMT (Katz–Sarnak, CFKRS)" and "Montgomery pair correlation" cover universality
in the *statistical-spectral* sense (FAIL I1/I3: statistics, not arithmetic, aggregated).
The Phase 24/25 audit (`phase-25-lower-bounds-bj-audit/01-audit-classical.md`) touched two
neighboring mechanisms:

- **Mechanism 9 (Bohr almost-periodicity):** verdict "Dead end — gives no information
  about $b_j$". Almost-periodicity shows that an off-critical zero "approximately
  reappears" for arbitrarily large $T$, but with no lower bound on $b_j$.
- **Mechanism 4 (Deuring–Heilbronn):** verdict "Dead end — wrong spectral region"
  (repulsion near $\mathrm{Re}(s)=1$, fed by the Euler product near 1).

Neither entry is the Bagchi criterion. The Bagchi criterion is stronger than the
qualitative almost-periodicity of Mechanism 9 in two decisive points: (a) the recurrence
has **positive lower density** (not just "arbitrarily large $T$"), and (b) the recursive
direction uses that density to **collide with an unconditional theorem**
($N(\sigma,T)=o(T)$), something almost-periodicity alone does not achieve. Whether this
passes I2a was never formulated as a question. This doc formulates it and answers it.

---

## 2. Verified statements (literature)

All statements in this section were verified against Matsumoto's survey
(*A survey on the theory of universality for zeta and L-functions*, arXiv:1407.4216,
2014; full text consulted), which in turn carefully expounds the content of Bagchi's
unpublished thesis. Matsumoto's notation: $D(a,b)=\{s:a<\sigma<b\}$;
$H^c(K)$ = functions continuous on $K$, holomorphic in the interior; $H_0^c(K)\subset
H^c(K)$ = those that additionally **do not vanish on $K$**.

### 2.1 Voronin 1975 — original form (disk)

**Theorem (Voronin 1975).** *Let $K(r)$ be the closed disk centered at $3/4$ with radius
$r$, $0<r<1/4$. For every $f\in H_0^c(K(r))$ and every $\varepsilon>0$ there exists
$\tau>0$ such that*
$$\max_{s\in K(r)}\,|\zeta(s+i\tau)-f(s)|<\varepsilon.$$

*Reference:* S. M. Voronin, "Theorem on the 'universality' of the Riemann
zeta-function", Izv. Akad. Nauk SSSR Ser. Mat. **39** (1975), 475–486; English transl.
Math. USSR-Izv. **9** (1975), 443–453. The original proof already contains (implicitly)
the fact that the set of such $\tau$ has positive lower density.

### 2.2 Modern form (strip; Bagchi, Reich, Gonek)

**Theorem 2.1 (universality, modern form; Matsumoto Thm. 1).** *Let $K$ be a compact
subset of $D(1/2,1)$ with connected complement, $f\in H_0^c(K)$, $\varepsilon>0$. Then*
$$\liminf_{T\to\infty}\ \frac{1}{T}\,\mathrm{meas}\Big\{\tau\in[0,T]\ :\ \sup_{s\in K}|\zeta(s+i\tau)-f(s)|<\varepsilon\Big\}\;>\;0.$$

Three known proofs: Voronin (Pecherskiĭ rearrangement in Hilbert spaces),
Good/Gonek, and Bagchi's probabilistic proof (1981 thesis) — §3.

### 2.3 Bagchi 1981/1987 — strong recurrence

**Definition.** $\zeta$ is **strongly recurrent** on $D(1/2,1)$ if for every compact
$K\subset D(1/2,1)$ with connected complement and every $\varepsilon>0$:
$$(\mathrm{SR})\qquad \liminf_{T\to\infty}\ \frac{1}{T}\,\mathrm{meas}\Big\{\tau\in[0,T]\ :\ \sup_{s\in K}|\zeta(s+i\tau)-\zeta(s)|<\varepsilon\Big\}\;>\;0.$$

**Theorem 2.2 (Bagchi; Matsumoto Thm. 20).** *RH is true $\iff$ (SR) holds on
$D(1/2,1)$.*

*References:* B. Bagchi, *The statistical behaviour and universality properties of the
Riemann zeta-function and other allied Dirichlet series*, thesis, Indian Statistical
Institute, Calcutta, 1981 (unpublished; content expounded in Laurinčikas's 1996 book
and in Matsumoto §1, §9); B. Bagchi, "Recurrence in topological dynamics and the
Riemann hypothesis", Acta Math. Hungar. **50** (1987), 227–240 (the dynamical-topological
formulation; the statement RH $\iff$ (SR) verified via secondary sources;
the full text of the 1987 paper was not accessible — the specific internal details
of that paper cited here are marked as such). Extensions: Bagchi himself to Dirichlet
$L$-functions; R. Steuding to Beurling zetas.

### 2.4 The unconditional input on the density side

**Theorem 2.3 (zero density, unconditional).** *For fixed $\sigma>1/2$,
$N(\sigma,T)=\#\{\rho:\zeta(\rho)=0,\ \mathrm{Re}\,\rho\ge\sigma,\ 0\le\mathrm{Im}\,\rho\le T\}=o(T)$.*

This does NOT require RH. Carlson (1920): $N(\sigma,T)\ll T^{4\sigma(1-\sigma)+\varepsilon}$,
and $4\sigma(1-\sigma)<1$ for $\sigma>1/2$; Ingham (1940) improves the exponent. The
qualitative precursor is Bohr–Landau (1914). Matsumoto cites exactly this form
($N(T;\sigma_1,\sigma_2;\zeta)=o(T)$) as the ingredient that kills strong universality
of $\zeta$ (his Corollary 2).

---

## 3. The machinery of the universality proof (Bagchi's proof)

To locate exactly where everything breaks, we need the five modules of the proof in
view. We follow Bagchi's architecture (expounded in Laurinčikas 1996, Steuding LNM
1877 ch. 5, Matsumoto §1).

**Module 1 — the Bohr torus.** $\Omega=\prod_p \mathbb{T}_p$, a product of unit circles
indexed by the **primes**, compact, with Haar measure $m_H$. A point
$\omega=(\omega(p))_p$ is a choice of phase per prime (a "generalized character").

**Module 2 — the Kronecker flow.** $T_\tau(\omega)=(p^{-i\tau}\omega(p))_p$. The
non-trivial characters of $\Omega$ are finite products $\prod_p\omega(p)^{n_p}$, on
which the flow acts by $e^{-i\tau\sum_p n_p\log p}$. Since $\{\log p\}_p$ is
**linearly independent over $\mathbb{Q}$** (= unique factorization in $\mathbb{Z}$),
$\sum n_p\log p\neq0$ for every non-trivial character: the flow is **ergodic** with
respect to $m_H$. This is the real arithmetic input of the whole theory.

**Module 3 — the random element.** For $\omega\in\Omega$ and $s\in D(1/2,1)$:
$$\zeta(s,\omega)=\prod_p\big(1-\omega(p)\,p^{-s}\big)^{-1}.$$
For $m_H$-almost every $\omega$, the product converges in $H(D(1/2,1))$ (compact-open
topology). The reason: the variables $\omega(p)$ are independent with $\mathbb{E}[\omega(p)]=0$,
and the random series $\sum_p\omega(p)p^{-s}$ converges a.s. for $\sigma>1/2$ (Kolmogorov's
three-series theorem / $L^2$ martingale, $\sum_p p^{-2\sigma}<\infty$). **Randomization
restores the Euler product in the strip** — this will be central in §7.

**Module 4 — functional limit theorem (unconditional).** The empirical distributions of
the shifts, $P_T(A)=\frac1T\mathrm{meas}\{\tau\in[0,T]:\zeta(\cdot+i\tau)|_D\in A\}$,
converge weakly in $H(D)$ to the law $P_\zeta$ of $\zeta(\cdot,\omega)$. The proof uses:
approximation of $\zeta$ by regularized absolutely convergent products/series, the
ergodicity of Module 2 via the **Birkhoff–Khinchin theorem** (Matsumoto §10 points to
this as the exact ergodic point of Bagchi's proof), and mean-square estimates
of $\zeta$ for $\sigma>1/2$ — all unconditional.

**Module 5 — support theorem + Mergelyan + positive density.** The support of
$P_\zeta$ in $H(D)$ is
$$S=\{f\in H(D)\ :\ f(s)\neq0\ \forall s\in D\}\cup\{0\}.$$
Density ("every nonzero $f$ is reachable") comes from the linear independence of
$\{\log p\}$ via Kronecker–Weyl: the phases $\omega(p)$ can be oriented to approximate
any given $\log f$ (an $L^2$ density lemma / the Pecherskiĭ rearrangement in Voronin's
proof). Closure ("nothing with zeros is in the support") is **Hurwitz's theorem**: a
limit in $H(D)$ of zero-free holomorphic functions is either zero-free or identically
zero — and each partial product $\prod_{p\le X}(1-\omega(p)p^{-s})^{-1}$ does not
vanish. Mergelyan reduces compacts $K$ with connected complement to polynomials.
Finally, $f\in\mathrm{supp}\,P_\zeta$ + weak convergence $\Rightarrow$ every
neighborhood of $f$ has positive limiting mass $\Rightarrow$ positive lower density of
$\tau$. ∎

**Where the non-vanishing of the target function enters — with surgical precision:** in
Module 5 and only there. The proof approximates $\log f$ by the $\log$ of random
truncated Euler products; if $f$ has a zero in $K$, $\log f$ does not exist on $K$, and
by Hurwitz $f\notin S=\mathrm{supp}\,P_\zeta$: the limiting mass of every sufficiently
small neighborhood of $f$ is **zero**. The machinery does not degrade gradually: it
gives exactly zero density for targets with zeros. (This is consistent with, not
contradictory to, the Rouché direction of §4.2.)

---

## 4. The two directions of Bagchi's theorem (question i)

### 4.1 RH $\Rightarrow$ strong recurrence

Under RH, $\zeta$ is holomorphic and **non-vanishing** on $D(1/2,1)$ (the pole $s=1$ is
outside; the critical zeros are on the boundary $\sigma=1/2$, outside the open set).
Then, for every compact $K\subset D(1/2,1)$ with connected complement, $\zeta|_K\in
H_0^c(K)$: $\zeta$ itself is an admissible target of Theorem 2.1. Applying it with
$f=\zeta$ gives (SR). ∎

Note the logical asymmetry: this direction consumes universality (unconditional) plus
**a single conditional bit** — "$\zeta\in H_0^c(K)$", that is, non-vanishing, that is,
RH itself. RH is not used in any estimate: it is used only as the admissibility
certificate of the target.

### 4.2 Strong recurrence $\Rightarrow$ RH (the hard direction)

Suppose (SR) and, by contradiction, a zero $\rho_0=\beta_0+i\gamma_0$ with
$\beta_0>1/2$. Choose $\delta>0$ small enough that the closed disk
$\bar B(\rho_0,\delta)\subset D(1/2,1)$ and $\zeta$ has no other zeros in it, and take
$$\varepsilon\ :=\ \tfrac12\min_{|s-\rho_0|=\delta}|\zeta(s)|\ >\ 0.$$
By (SR) applied to $K=\bar B(\rho_0,\delta)$, the set
$A_\varepsilon=\{\tau:\sup_{s\in K}|\zeta(s+i\tau)-\zeta(s)|<\varepsilon\}$ has positive
lower density $c>0$. For each $\tau\in A_\varepsilon$, on the circle $|s-\rho_0|=\delta$:
$$|\zeta(s+i\tau)-\zeta(s)|\ <\ \varepsilon\ <\ \min_{|s-\rho_0|=\delta}|\zeta(s)|\ \le\ |\zeta(s)|,$$
and by **Rouché's theorem**, $\zeta(\cdot+i\tau)$ has in $B(\rho_0,\delta)$ as many
zeros as $\zeta$: at least one. That is, $\zeta$ has a zero in
$B(\rho_0+i\tau,\delta)$, with $\mathrm{Re}>\beta_0-\delta>1/2$.

How many zeros this produces: $A_\varepsilon\cap[0,T]$ has measure $\ge cT$ for large
$T$; a given zero can be counted by the $\tau$'s of an interval of length $\le2\delta$;
hence
$$N\big(\beta_0-\delta,\ T+\delta\big)\ \ge\ \frac{cT}{2\delta}\ \gg\ T.$$
This contradicts $N(\sigma,T)=o(T)$ for $\sigma=\beta_0-\delta>1/2$ (Theorem 2.3,
**unconditional**). Hence there is no off-critical zero. ∎

(The same skeleton proves Matsumoto's Theorem 11: "strong universality
$\Rightarrow N\ge CT$ zeros", and his Corollary 2: $\zeta$ **cannot** be strongly
universal — it cannot approximate targets with zeros — precisely because of
$N(\sigma,T)=o(T)$.)

### 4.3 Localization remark (new, minor)

To refute **one** hypothetical zero $\rho_0$, full (SR) is not needed: ONE instance
suffices — the compact $K=\bar B(\rho_0,\delta)$ and the concrete
$\varepsilon(\rho_0,\delta)$ of §4.2. The minimal premise of the amplifier is pointwise,
not uniform. This does not help prove it (it still depends on the hypothetical zero,
which we do not know), but it matters for the discriminator: the mechanism is
**individual-resolving** (I3 checked), an absolute rarity in the corpus.

---

## 5. The amplification mechanism under the microscope (question ii)

### 5.1 What it is and why it is not a positivity

Step §4.2 has a structure unique in the entire audited corpus:

> **Amplification:** a recurrence property (positive density of self-returns)
> **replicates** a single off-critical zero into a family of $\gg T$ off-critical zeros,
> and the family collides with an **unconditional** density bound.

Compare with the program's inventory of mechanisms:

- **It is not CAP.** There is no quadratic form, no center-definiteness, no
  "$\lambda_{\min}\ge0$ equivalent to RH". The contradiction is one of **counting**: $\gg
  T$ against $o(T)$. The input producing the contradiction (Carlson/Ingham) is a real,
  unconditional theorem, on the correct side.
- **It is not the MW-4 pattern** (wrong sign): no positivity upper bound is needed at
  all; the zero density is exactly the kind of bound the unconditional tools DO know how
  to give (FAIL I3 in its direct use — "density, not absence" — but here density is used
  as the *ceiling* against which the amplification is smashed, not as a detector of
  absence).
- **Inversion of Deuring–Heilbronn.** D–H (audited, Mechanism 4 of Phase 25) is
  *repulsion*: an exceptional zero near $\mathrm{Re}(s)=1$ **expels** the others; the
  engine is the Euler product near 1 and does not reach the strip (Paley–Wiener wall,
  Phases 22–23). Bagchi is *replication*: an off-critical zero, given the recurrence
  input, **multiplies** copies of itself within the strip. D–H consumes a hypothetical
  zero and produces a conditional restriction on other zeros; Bagchi consumes a
  hypothetical zero PLUS recurrence and produces an **absolute contradiction**. These are
  the only two "dynamical over individual zeros" mechanisms in the corpus, and they have
  opposite directions. D–H failed on spectral region; Bagchi's amplifier operates exactly
  in the correct region, $D(1/2,1)$.

**Direct answer to question (ii):** yes, it is the only mechanism in the corpus that
turns zero-density theorems into a contradiction, and the *isolated* mechanism does not
fail I2a: it uses two genuine, unconditional inputs (Kronecker–Weyl equidistribution in
the machinery that would produce the premise; Carlson/Ingham in the ceiling). But a
mechanism is not a criterion.

### 5.2 Where the circularity ended up: relocated, not eliminated

Theorem 2.2 says the premise (SR) is **equivalent** to RH. So the full scheme is:

$$\underbrace{(\mathrm{SR})}_{\text{RH-equivalent}}\ \xRightarrow{\ \text{amplifier (non-circular)}\ }\ \mathrm{RH}.$$

The situation is structurally identical to that of Connes in the Phase A table: a
genuine independent machinery (there the adele class space; here the Bohr–Kronecker
dynamics with its unique-factorization input) that does all the work **except the last
step**, and the last step — proving (SR), there proving Weil positivity — re-encodes RH.
The difference from a pure FAIL I2a (Li, Báez-Duarte, etc.) is that here the non-circular
work is massive and produces collateral unconditional theorems (§6.3). The correct
classification is therefore **FAIL I2b**, not FAIL I2a: independent input exists
(I2a partial/checked), the decisive theorem supplying the premise is missing.

---

## 6. Can strong recurrence be proved without RH? (question iii)

### 6.1 The exact breaking point

By §3, the only obstruction is admissibility of the target: $\zeta\in H_0^c(K)$. The
universality proof breaks down in Module 5 if the target has a zero, and it breaks
down in binary fashion (exactly zero density, by Hurwitz + support). There is no
"degraded" version of the proof giving positive density for targets with small zeros:
Matsumoto's Corollary 2 (via the very amplifier of §4.2 against $N(\sigma,T)=o(T)$)
**forbids** such a version from existing. The machinery is thus *exactly
self-consistent*: it proves (SR) if and only if the non-vanishing of $\zeta$ is
certified beforehand, and the non-vanishing of $\zeta$ is RH. There is no slack.

### 6.2 MW-7 test (Hadamard barrier): is (SR) verifiable without knowing zero positions?

**No.** In both directions:

- (SR) $\Rightarrow$ no off-critical zeros (§4.2): verifying (SR) implies localizing
  zeros (negatively). Conversely, by §4.1, certifying (SR) via the only known route
  requires first certifying non-vanishing in the strip. The property "(SR)" is a
  property of $\zeta$ whose verification **is** a control of zero positions: Rouché
  works in both directions — the closeness $|\zeta(s+i\tau)-\zeta(s)|<\varepsilon$ on a
  disk transports the zero structure of the disk. In MW-7's language: strong recurrence
  is NOT a property of $\zeta$ "verifiable without knowing zero positions"; it is a
  dynamical encoding of zero positions. MW-7 applies.

### 6.3 Is the set of recurrent $\tau$ controlled by accessible arithmetic structure? The family $d$ and the diagonal point

Here lies the most informative material in the literature, because it measures *how
far* the unconditional arithmetic input reaches. Consider the two-speed
self-approximation (Matsumoto §9, formula (9.3)):
$$(\mathrm{SR}_d)\qquad \liminf_{T\to\infty}\frac1T\,\mathrm{meas}\Big\{\tau\in[0,T]:\sup_{s\in K}|\zeta(s+i\tau)-\zeta(s+i d\tau)|<\varepsilon\Big\}>0.$$
Note that $(\mathrm{SR}_0)=(\mathrm{SR})$ = RH (Theorem 2.2). Verified state
(Matsumoto Thm. 21 and surroundings):

- **$d$ algebraic irrational:** $(\mathrm{SR}_d)$ holds unconditionally (Nakamura
  2010, Arch. Math. 95) — via joint universality, using that
  $\{\log p^{d_j}\}$ is linearly independent over $\mathbb{Q}$ by **Baker's theorem**
  (linear forms in logarithms).
- **$d$ transcendental irrational:** $(\mathrm{SR}_d)$ holds (Pańkowski, via the **six
  exponentials theorem**).
- **$d=a/b$ nonzero rational, $(a,b)=1$, $|a-b|\neq1$:** $(\mathrm{SR}_d)$ holds
  (Garunkštis; Nakamura; correction Nakamura–Pańkowski, Arch. Math. 99 (2012)).
- **$\log\zeta$ instead of $\zeta$:** variant (9.4) holds **for every $d\neq0$**; and if
  it held at $d=0$ it would imply RH.

That is: the unconditionally accessible arithmetic structure (independence of
$\{\log p\}$, Baker, six exponentials — genuine transcendental number theory, real I2a
input!) controls the set of recurrent $\tau$ for **every** relative speed $d\neq0$
(except the technical rational case $|a-b|=1$), and stops **exactly** at the diagonal
point $d=0$, which is RH. The structural reason: for $d\neq0$ the two copies
$\zeta(s+i\tau)$, $\zeta(s+id\tau)$ traverse the torus at different speeds and there is
*relative* equidistribution to exploit — the relative phases $p^{-i(1-d)\tau}$
equidistribute, and linear independence over $\mathbb{Q}$ of the joint system
$\{\log p,\,d\log p\}$ is certified by Baker or the six exponentials. At $d=0$ the
relative displacement is identically zero: no relative equidistribution remains
available, and the problem collapses to the **absolute** position of the arithmetic
point on the torus (§7). The limit $d\to0$ transfers nothing: the positive density of
$(\mathrm{SR}_d)$ for $d\neq0$ compares two points *generic relative to each other*,
while $(\mathrm{SR}_0)$ requires the arithmetic point to be generic *relative to
itself* — the exact non-uniformity is that of Module 5: the limiting target $\zeta$
falls outside the support $S$ as soon as it has a zero.

**Conclusion of (iii):** strong recurrence is not provable without RH by the existing
machinery, and the boundary of what is provable is mapped with unusual precision: the
entire family $(\mathrm{SR}_d)_{d\neq0}$ is unconditional; the only missing point is the
diagonal, and it is equivalent to RH. The real arithmetic input reaches literally up to
the boundary of the problem.

---

## 7. The ergodic levers and the identification of the obstruction (question iv — main content)

### 7.1 What the dynamics gives for free (unconditional)

We fix the system $(\Omega,m_H,(T_\tau))$ of §3. Classical facts, all unconditional:

**(E1) Ergodicity** of the Kronecker flow (Module 2; unique factorization).

**(E2) Minimality and unique ergodicity.** The orbit of the neutral element,
$\{(p^{-i\tau})_p:\tau\in\mathbb{R}\}$, is dense in $\Omega$: on each finite subtorus
$\prod_{p\le X}\mathbb{T}_p$ this is Kronecker–Weyl (independence of $\{\log p\}_{p\le X}$),
and $\Omega$ is the inverse limit. A compact-group translation with a dense
one-parameter subgroup is **minimal** and **uniquely ergodic** (classical theorem on
rotations of compact groups; Walters, *An Introduction to Ergodic Theory*, ch. 6).
In particular:

**(E3) EVERY point of $\Omega$ is uniformly recurrent.** In a minimal system on a
compact space, every point is almost periodic in Birkhoff's sense: for every
neighborhood $U$ of $\omega$, the set $\{\tau:T_\tau\omega\in U\}$ is relatively dense
(syndetic), in particular of positive lower density. **This includes the arithmetic
point** $\omega_0=(1,1,1,\dots)$ (all phases trivial — the point corresponding to
$\zeta$ itself).

It should be stressed: the recurrence of the arithmetic orbit **on the torus** is not
the problem. It is an unconditional, quantitative fact (it is Kronecker–Weyl
almost-periodicity, Mechanism 9 of Phase 25 in its correct form). If Bagchi's
obstruction were "individual orbit vs. generic" in the sense of the pointwise ergodic
theorem — a.e. convergence with no control at specific points due to lack of unique
ergodicity — then (E2) would resolve it: there is unique ergodicity, and for
**continuous observables** convergence of averages and return properties hold at ALL
points, not just a.e. The obstruction must lie elsewhere. It lies in the observable.

### 7.2 The Euler observable and its arithmetic singularity

The connection between the abstract dynamics and $\zeta$ is the **Euler observable**
$$\Phi:\Omega\ \dashrightarrow\ H(D(1/2,1)),\qquad \Phi(\omega)=\zeta(\cdot,\omega)=\prod_p(1-\omega(p)\,p^{-\cdot})^{-1},$$
defined only where the product converges. Properties:

- $\Phi$ is defined on a set $\Omega_{\mathrm{conv}}$ with $m_H(\Omega_{\mathrm{conv}})=1$
  (Module 3), invariant under the flow.
- $\Phi$ **admits no continuous version** on $\Omega$: it is an a.e./$L^2$ limit of
  continuous functions (the partial products), not a uniform limit; on the strip the
  series $\sum_p\omega(p)p^{-s}$ does not converge absolutely and its convergence
  depends on specific phase cancellations of $\omega$.
- On the arithmetic orbit, $\Phi(T_\tau\omega_0)$ is formally the Euler product of
  $\zeta(s+i\tau)$ — the object that, according to MW-2, **does not converge** (is not
  available) in the strip.

The exact identification is as follows.

**Proposition 7.2 (membership of the arithmetic orbit in the domain of the observable
is RH-equivalent).** *The following are equivalent:*
*(a) RH;*
*(b) the series $\sum_p p^{-s}$ converges for every $s$ with $\sigma>1/2$;*
*(c) the arithmetic orbit $\{T_\tau\omega_0\}_{\tau\in\mathbb{R}}$ is contained in
$\Omega_{\mathrm{conv}}$, and there $\Phi(T_\tau\omega_0)=\zeta(\cdot+i\tau)$.*

*Proof sketch.* (a)$\Rightarrow$(b): under RH, $\pi(x)=\mathrm{Li}(x)+O(x^{1/2}\log x)$,
and Abel partial summation gives convergence of $\sum_p p^{-s}$ for $\sigma>1/2$; since
$\log\zeta(s)=\sum_p p^{-s}+E(s)$ with $E(s)=\sum_p\sum_{k\ge2}p^{-ks}/k$ absolutely
convergent for $\sigma>1/2$, the product converges to $\zeta(s)$ (classical; cf.
Titchmarsh, *The Theory of the Riemann Zeta-Function*, ch. XIV). (b)$\Rightarrow$(a): if
$\sum_p p^{-s}$ converges at every point of $\sigma>1/2$, it defines a holomorphic
function there (Dirichlet series theory: convergence at $s_0$ gives locally uniform
convergence for $\sigma>\sigma_0$ within Stolz angles; convergence at every point gives
holomorphy on the whole strip) agreeing with $\log\zeta-E$ for $\sigma>1$; then
$\log\zeta$ continues holomorphically to $\sigma>1/2$, hence $\zeta$ has no zeros there:
RH. (b)$\iff$(c): convergence of the product at $\omega=T_\tau\omega_0$ is convergence
of $\sum_p p^{-(s+i\tau)}$, which ranges over the same points of the strip. ∎

**Corollary 7.3 (ergodic form of MW-2).** The divergence set
$\Omega\setminus\Omega_{\mathrm{conv}}$ is an $m_H$-null, flow-invariant set, and the
question "is the arithmetic orbit outside it?" is exactly RH. Under $\neg$RH the entire
arithmetic orbit lives in the null exceptional set; under RH it lives in the good set.
**Arithmetic cannot be certified generic.**

### 7.3 The diagnosis: MW-2 in disguise, or a new ergodic obstruction?

We can now answer question (iv) with precision. There are three candidates for "the
obstruction", and the first two are ruled out:

1. **Lack of recurrence of the arithmetic point on the torus?** No: (E3) — $\omega_0$ is
   uniformly recurrent, unconditionally.
2. **A failure of the type "pointwise ergodic theorem without unique ergodicity"
   (individual orbit not controlled by the measure)?** No: (E2) — the system IS uniquely
   ergodic and minimal. For continuous observables, unique ergodicity gives control at
   *every* point. The "a.e. vs. specific point" dichotomy is not, by itself, the barrier.
3. **The observable $\Phi$ is not continuous, and its domain of definition excludes
   (under $\neg$RH) precisely the arithmetic orbit.** This is the real obstruction, by
   Proposition 7.2. The chain that fails is:
   $$\underbrace{T_\tau\omega_0\ \text{returns near}\ \omega_0}_{\text{unconditional (E3)}}\ \not\Rightarrow\ \underbrace{\Phi(T_\tau\omega_0)\ \text{returns near}\ \Phi(\omega_0)}_{\text{= (SR) = RH}},$$
   because translating closeness in $\Omega$ into closeness in $H(D)$ requires $\Phi$ to
   be continuous at $\omega_0$ along the orbit — and continuity of the Euler observable
   at the arithmetic point of the strip is, again, propagation of the Euler product to
   $\sigma\in(1/2,1)$: **MW-2**.

**Verdict (iv): the obstruction is MW-2, exactly and without residue.** The statement of
MW-2 in the program's summary ("the Euler product is valid only for $\mathrm{Re}(s)>1$;
arithmetic information does not propagate to the critical strip; zeros are global
objects") translates term for term:

| MW-2 (analytic language) | Ergodic language (this doc) |
|---|---|
| the Euler product does not converge in the strip | $\omega_0\notin\Omega_{\mathrm{conv}}$ (under $\neg$RH); $\Phi$ undefined/discontinuous on the arithmetic orbit |
| randomization/averages do see the arithmetic | $m_H(\Omega_{\mathrm{conv}})=1$; unconditional functional limit theorem (Module 4) |
| zeros are global objects, no prime possesses a zero | the zeros of $\zeta(\cdot,\omega)$ do not exist a.e. (support $S$); they appear only at the global exceptional point $\omega_0$, at no coordinate $p$ |
| information from $\sigma>1$ does not propagate to the strip | the identification $\Phi(T_\tau\omega_0)=\zeta(\cdot+i\tau)$ holds for $\sigma>1$ and its extension to the strip is RH (Prop. 7.2) |

And the connection to MW-7 closes the triangle: *verifying* the recurrence of the
individual orbit amounts (Rouché, §6.2) to controlling zero positions — the Hadamard
barrier. The ergodic category offers no formulation where Hadamard fails to apply; it
offers the sharpest formulation the program has of WHY it applies: **the ergodic theorem
(even with unique ergodicity and minimality) controls orbits through continuous
observables; the only observable connecting the torus with $\zeta$ has its singularity
exactly at the arithmetic point, and removing it from there is RH.**

### 7.4 Synthetic reformulation (for the program map)

> Under $\neg$RH, $\zeta$ is a point that **does not belong to the support of its own
> shift statistics**: Bagchi's limit theorem (unconditional) says the orbit
> $\{\zeta(\cdot+i\tau)\}$ equidistributes toward a law $P_\zeta$ whose support consists
> of zero-free functions; if $\zeta$ has an off-critical zero, $\zeta$ is outside that
> support, and its orbit visits it with zero density (although it does visit: $\tau=0$,
> and the returns of qualitative almost-periodicity of Mechanism 9). RH says exactly
> that $\zeta$ is a **generic point of its own dynamics**. The Hadamard barrier, in
> ergodic terms: *there is no way to certify the genericity of the arithmetic point
> without knowing its zeros, because "being generic" IS "having no zeros".*

---

## 8. The discriminator (question v)

We apply D0 with the split I2 → I2a ∧ I2b of Phase A. Object audited: **the Bagchi
criterion as a route to RH** (= proving (SR) via the dynamical-ergodic route and
concluding via the amplifier).

**I1 — prime-distinguishing: checked.** The entire apparatus is indexed by primes: the
torus $\Omega=\prod_p\mathbb{T}_p$, the flow with frequencies $\{\log p\}$, ergodicity IS
the linear independence of $\{\log p\}$ over $\mathbb{Q}$ (unique factorization). The
identity of the primes (not just their counts) is load-bearing: Baker and the six
exponentials (§6.3) distinguish fine multiplicative relations between primes.

**I2a — independent input: partial (exists, and does real work, but does not reach the
point).** Input not reconstructible from $\zeta$/the explicit formula exists: (1) linear
independence of $\{\log p\}$ + Kronecker–Weyl; (2) the Bohr compact-group structure with
Haar measure and its unique ergodicity; (3) transcendence theory (Baker, six
exponentials). This input produces non-trivial unconditional theorems: universality
itself (Thm. 2.1), the entire family $(\mathrm{SR}_d)_{d\neq0}$ (§6.3), the $\log\zeta$
variant for $d\neq0$. But at the required point ($d=0$ / target $=\zeta$), the property
still to be proved re-encodes the positions of the zeros (§6.2, §7.3): the independent
input is exhausted exactly at the boundary. This is not the flat FAIL of Li/Báez-Duarte
(where there is no independent input at all); it is the partial case of "real structure
that does not reach", like Berry–Keating in the Phase A table.

**I2b — decisive theorem supplying the restriction: failed.** The necessary decisive
theorem has an exact name: *"the arithmetic orbit $\{T_\tau\omega_0\}$ is
$\Phi$-recurrent"*, equivalently *"$\omega_0$ is a generic point of the Euler
observable"*, equivalently (Prop. 7.2) convergence of $\sum_p p^{-s}$ in the strip. No
such theorem exists; by Proposition 7.2 it is RH-equivalent, so no theorem from the
dynamical machinery (which controls continuous observables / a.e. classes) can supply it
without new input. Same profile as Connes: the geometry/dynamics does everything but the
last step, and the last step is the re-encoding.

**I3 — individual-resolving: checked.** Notable rarity (§4.3): the amplifier resolves
individual zeros — ONE hypothetical zero produces the contradiction; the signal is
$O(1)$ (the minimum of $|\zeta|$ on a fixed circle) and not an aggregate/moment/density
used as a detector. Of the ~30 programs in the Phase A table, only the full PASSes and
the "elite" FAIL-I2 cases (Weil, Hilbert–Pólya, Connes, de Branges, Lee–Yang) have I3
checked; no other mechanism in the corpus turns I3 into a contradiction against an
unconditional theorem.

**I4 — arithmetic-aware: checked.** Nothing in the apparatus survives an
arithmetic-blind deformation: replacing $\{\log p\}$ with rationally dependent
frequencies kills ergodicity (Module 2) and the entire universality. Unique
factorization is the engine, not decoration.

### Row for the Phase A table

| Program | I1 | I2a | I2b | I3 | I4 | D0 verdict | Known outcome | Match? |
|---|---|---|---|---|---|---|---|---|
| **Bagchi strong recurrence / Voronin universality** | checked | partial | failed | checked | checked | **FAIL I2b** | RH-equivalent criterion; (SR$_d$) proved $\forall d\neq0$, open only at $d=0$ | yes (Connes profile: real structure, missing the decisive theorem) |

**Discriminator verdict:** FAIL I2b. This is not a pure FAIL I2a (there is genuine
independent input producing unconditional theorems up to the exact boundary of the
problem), and it is not CAP (there is no positivity anywhere in the mechanism). It is the
program's second clean example — after Connes — of the pattern "independent structure
without a decisive theorem", and the first of **dynamical-ergodic** nature.

---

## 9. Transferable asset (honest record)

Although the route is closed, the audit leaves a precise asset the program did not have
inventoried:

**(A1) The Rouché-density amplifier.** Scheme: [recurrence with positive density on a
disk around a hypothetical zero] + [unconditional $N(\sigma,T)=o(T)$]
$\Rightarrow$ contradiction. It is non-CAP, individual-resolving (I3 checked), and its
minimal premise is *pointwise* (§4.3): it would suffice to produce, for each
hypothetical zero $\rho_0$, positive density of self-returns on ONE disk with ONE
concrete $\varepsilon$. Any future program mechanism producing recurrence — from any
source, not necessarily universality — would plug in here and close RH. The amplifier is
registered as the only known non-circular "final consumer" of recurrence properties.

**(A2) The exact measure of the boundary.** The family $(\mathrm{SR}_d)$: every $d\neq0$
unconditional (Baker / six exponentials / rational with $|a-b|\neq1$), $d=0$
$\iff$ RH. No other front of the program has the boundary of the unconditional mapped
with a single missing, parametrized point.

**(A3) The ergodic form of MW-2/MW-7 (Prop. 7.2, Cor. 7.3, table §7.3).** Reusable as a
quick test: any future proposal of dynamical flavor (flows on adelic tori,
almost-periods, Bohr compactifications) must first answer "is the observable connecting
the dynamics with $\zeta$ continuous at the arithmetic point?" — if not, MW-2 applies
and ergodic control (even with unique ergodicity) does not transfer.

**Gaps declared in this document:**
- The full text of Bagchi 1987 (Acta Math. Hungar. 50) was not accessible; the statement
  RH $\iff$ (SR) and the bibliographic references were verified via Matsumoto
  (arXiv:1407.4216, full text consulted) and secondary sources. The specific internal
  dynamical-topological framework of the 1987 paper (the exact notion of Birkhoff
  recurrence Bagchi uses there) is reconstructed here from the survey and should be
  considered [NOT VERIFIED in the original].
- The internal theorem numbering of Steuding's book (*Value-distribution of
  L-functions*, Springer LNM 1877) and of Laurinčikas (1996) was not verified against the
  texts; the cited contents (support theorem, limit theorem) are standard and are
  confirmed by Matsumoto and by the self-approximation literature.
- Proposition 7.2 is a reorganization of classical facts (Titchmarsh ch. XIV +
  Dirichlet series theory); direction (b)$\Rightarrow$(a) requires convergence
  at *every* point of the strip, as stated — convergence at a single point only gives
  holomorphy to its right. No novelty is claimed, only the identification with the
  ergodic language.

---

## 10. VERDICT

**ROUTE CLOSED.**

**Precise reason:** the Bagchi criterion has the structure [RH-equivalent premise] →
[non-circular amplifier] → [RH]. The amplifier (Rouché + Carlson/Ingham) is genuine,
non-CAP and individual-resolving — it passes I1, I3, I4 — but the premise (strong
recurrence) is only reachable via the universality machinery, which requires certifying
the non-vanishing of $\zeta$ in the strip: RH itself. The discriminator gives **FAIL
I2b**: real independent input exists (independence of $\{\log p\}$, Bohr–Kronecker
dynamics, transcendence theory — unconditionally produces the entire family
$(\mathrm{SR}_d)_{d\neq0}$), but the missing decisive theorem ("the arithmetic orbit is
$\Phi$-recurrent" / "$\omega_0$ is a generic point of the Euler observable") is
RH-equivalent (Proposition 7.2).

**Answer to question (vi):** the ergodic category does NOT offer a formulation where the
Hadamard barrier ceases to apply. The "individual orbit vs. generic" obstruction **IS**
MW-2 in ergodic language — and the identification is more precise than expected: it is
not the recurrence of the arithmetic point on the torus that fails (unconditional, by
minimality), nor does unique ergodicity fail (the Kronecker flow has it); what fails is
the **continuity of the Euler observable at the arithmetic point**, and that continuity
is literally "the Euler product propagates to the strip" (MW-2), whose verification is
"knowing the positions of the zeros" (MW-7). The three walls are the same stone seen from
analysis, measure, and dynamics. What the ergodic category does contribute is the
sharpest formulation the program has of that stone (Cor. 7.3: *under $\neg$RH the entire
arithmetic orbit lives in the measure-zero exceptional set of its own dynamics*), plus a
new non-circular asset: the Rouché-density amplifier (§9, A1), the only known final
consumer of recurrence that produces RH without positivity.

---

## References

**External literature (verified):**
- S. M. Voronin, *Theorem on the "universality" of the Riemann zeta-function*, Izv. Akad.
  Nauk SSSR Ser. Mat. **39** (1975), 475–486; Math. USSR-Izv. **9** (1975), 443–453.
- B. Bagchi, *The statistical behaviour and universality properties of the Riemann
  zeta-function and other allied Dirichlet series*, doctoral thesis, Indian Statistical
  Institute, Calcutta, 1981.
- B. Bagchi, *Recurrence in topological dynamics and the Riemann hypothesis*, Acta Math.
  Hungar. **50** (1987), 227–240.
- K. Matsumoto, *A survey on the theory of universality for zeta and L-functions*,
  arXiv:1407.4216 (2014) — main source of the statements (Thms. 1, 11, 20, 21;
  Cor. 2; §§1, 9, 10, 18; full text consulted).
- J. Steuding, *Value-distribution of L-functions*, Springer Lecture Notes in
  Mathematics 1877, 2007.
- A. Laurinčikas, *Limit Theorems for the Riemann Zeta-Function*, Kluwer, 1996.
- F. Carlson (1920); A. E. Ingham (1940) — zero density estimates,
  $N(\sigma,T)=o(T)$ for $\sigma>1/2$; precursor: H. Bohr and E. Landau (1914).
- T. Nakamura, Arch. Math. **95** (2010), 549–555; T. Nakamura and Ł. Pańkowski, Arch.
  Math. **99** (2012), 43–47 (erratum); R. Garunkštis, *Self-approximation of Dirichlet
  L-functions*, J. Number Theory (2010) — the family $(\mathrm{SR}_d)$.
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed., ch. XIV.
- P. Walters, *An Introduction to Ergodic Theory*, Springer GTM 79 — unique ergodicity of
  rotations of compact groups.

**Internal program docs (backward-only):**
- `meta-docs/DISCRIMINATOR-hardening-phase-A.md` — criteria I1, I2a, I2b, I3, I4; table.
- `meta-docs/DISCRIMINATOR-independent-input-filter.md` — D0, H0, calibration.
- `phase-25-lower-bounds-bj-audit/01-audit-classical.md` — Mechanism 4 (Deuring–Heilbronn), Mechanism 9
  (Bohr almost-periodicity).
- `COMPLETE-PROGRAM-SUMMARY.md` — MW-1…MW-7; Hadamard barrier (Doc 89); P39, P40.
- Doc 89 ($d\nu$ synthesis); P39 (RH $\iff T_\lambda=0$); P40 (three paths).

---

*Doc 102 · Phase 35*
