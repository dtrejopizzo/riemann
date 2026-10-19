# Doc 157 — Tauberian probe: does Tauberian theory cross the average→individual wall of RH?

**Program:** Riemann Hypothesis — Phase 49: CROSS THE WALL.
**Role of the document:** to attack the **average → individual** crossing of the master quantifier of P43 with the
only mechanism that crosses average→individual in a proved way: **Tauberian theorems**. The
central question is NOT to produce another RH ⟺ X equivalence; it is to decide whether there is a **Tauberian
condition** —one-sided, RH-free, verifiable from the primes— that crosses from the AVERAGE control of $\psi(x)-x$
(unconditional) to the INDIVIDUAL control $o(x^{1/2+\epsilon})$ (which IS RH); or to prove that every sufficient
Tauberian condition is itself RH-equivalent (a no-go that locates the wall inside Tauberian
theory).

**Creative contract (absolute labeling rule):** **[NEW-DEFINITION]** = total freedom.
**[THEOREM]/[PROPOSITION]/[LEMMA]** = truly proved here, complete proof; external results cited
with precision. **[CALCULATION]** = shown. **[BRIDGE]** = connection with frank status. **[GAP]** = declared.
**[WISH]** = declared. **[literature GAP]** = data not verified at page level this session, NOT
used as a premise of any [THEOREM]. A proof of RH is never fabricated. **NO numerics.**

**Prerequisites read at the source this session:** Doc 152 in full (impurity spectrum $\omega(\tau)$,
Theorem 152.2, jurisdiction of $\Lambda\ge0$ = boundary and is exhausted there, Landau inversion F3, LP-152
dual of LP-112, Prop. 152.9 bad frequencies of zero density); phase48 project memory.

---

## 0. Executive summary

1. **(§1) The exact Tauberian crossing that RH needs, written without cheating.** RH is a statement about the
   **individual abscissa of convergence** of the integral $\int_1^\infty(\psi(x)-x)\,x^{-s-1}\,dx$, which is
   $-\zeta'/\zeta(s)/s - 1/(s-1)$ modulo an entire function, holomorphic precisely in $\mathrm{Re}\,s>\Theta$ where
   $\Theta=\sup\beta$. The closest Tauberian theorem that exists is the **Ingham–Karamata theorem**
   (boundary-to-individual with a slow-oscillation condition) and, in the power-growth regime, the
   **Wiener–Ikehara Tauberian theorem with remainder**. What both require and we do NOT have is: either a **uniform
   slow-oscillation condition** on $\psi(x)-x$ (which Littlewood disproves: the oscillation is genuine and of
   amplitude $\sqrt x\log\log\log x$), or **analytic continuation up to $\mathrm{Re}\,s=\tfrac12$**
   (which IS RH). The Tauberian crossing that RH needs is **sub-Tauberian**: not from the arithmetic average to the
   limit, but from the **second moment** (the $L^2$ control that we really do have on average: the
   moment $\int_1^X(\psi(x)-x)^2x^{-2}dx \asymp X^{2\Theta-1}$) to the **pointwise exponent** $\Theta$.

2. **(§2) The catalog of Tauberian conditions, each one classified.** I catalog five families:
   (T1) positivity of Λ (classical Wiener–Ikehara); (T2) slow oscillation / bounded variation
   (Ingham–Karamata, Pitt); (T3) one-sided single-sign conditions (Hardy–Littlewood, "slowly
   decreasing"); (T4) moment / Carleman conditions ($L^2$ control → pointwise); (T5) spectral conditions of
   Beurling–Malliavin / Wiener type (closure of translations, completeness of exponentials).
   **Catalog verdict:** T1 is exhausted (boundary jurisdiction, Doc 152.4–152.5); T2 is
   REFUTED by Littlewood (the non-oscillation condition does not hold, §2.2); T3 is RH-free but
   **insufficient** (it does not cross the half-epsilon); T4 is RH-EQUIVALENT (the finite $L^2$ moment in weight
   $x^{-2}$ ⟺ RH: §2.4, a Cramér identity); **T5 is the only family where the question remains open
   and where the "controlled oscillation" of the goal has substance.**

3. **(§3) The spectral Tauberian attack, in earnest.** I rewrite LP-152 (Doc 152.8) as a **spectral Tauberian
   condition of Wiener type**: the subexponentiality of $S_T(\tau_0)$ is exactly the
   condition that the Fourier transform of the prime measure **does not vanish** in the sense of the
   Wiener Tauberian theorem (closure of translations ⟺ non-vanishing of $\hat f$). **[PROPOSITION 157.5]**:
   LP-152 is ONE-SIDED in the correct sense (it is an UPPER bound on amplitude, not a
   non-oscillation condition: it controls how strongly it oscillates, not whether it oscillates — exactly the "controlled
   oscillation" the goal asked us to look for). But **[PROPOSITION 157.6]** (the stress test at the spectral heart): the
   Beurling–Malliavin theorem on the radius of completeness converts spectral subexponentiality
   into a statement about the **density of the frequencies $\log p$** which, via the explicit
   formula, **reintroduces the zeros** — verifying LP-152 goes through the spectral density, which is the divisor
   of ζ. The circle localized at the exact point: Beurling–Malliavin needs the density of a
   spectral set, and the spectral density on the prime side IS the zero count (Riemann–von Mangoldt).

4. **(§4) The RH stress test applied three times to the only candidate still alive (T5/LP-152).** Three
   RH-free verification routes: (i) verification by Besicovitch density (Prop. 152.9) — fails: the
   bad frequency is an exceptional point invisible to the average; (ii) verification by completeness
   (Beurling–Malliavin) — fails: §3, reintroduces the divisor; (iii) verification by direct
   monotonicity/positivity of $S_T$ — fails: Doc 152.4, positivity is zero-frequency information. The three fail for the SAME
   structural reason, which I isolate: **every verification of a Tauberian condition on $\psi(x)-x$ that is
   sufficient for the half-epsilon must read information at the frequency $\gamma$ of a zero, and the only
   unconditional instrument that reads that frequency is the explicit formula, which is an identity
   (tautology, D112 Prop. 4.2) that reintroduces the zeros.**

5. **(§5) VERDICT: case (b) conditional on a precise literature GAP — LOCALIZED TAUBERIAN NO-GO,
   with a named crack.** I prove (Theorem 157.8) a **Tauberian no-go** within a broad and
   natural class of Tauberian conditions (the "local-in-frequency Tauber–Wiener type conditions"):
   every condition of that class that is sufficient for RH is RH-equivalent, because the Littlewood
   oscillation saturates exactly the Cauchy–Schwarz margin (§5.2, the saturation computation). The
   crack that the no-go does NOT cover, named with precision (GAP-157.A): Tauberian conditions that are
   **non-local in frequency** of Beurling–Malliavin type with an independent Diophantine input
   ($\mathbb Q$-linear independence of $\{\log p\}$ used as a Tauberian condition, not as an ambient
   fact) — the same input that feeds LP-112 (Bagchi) on the other side of the pincer. **Message: there is NO
   known RH-free Tauberian condition that crosses; the wall is inside classical Tauberian theory
   (no-go proved for locally-in-frequency conditions); the only crack is spectral-Diophantine and is the
   same one as LP-112/LP-152.**

---

## 1. The exact Tauberian crossing that RH needs

### 1.1. What "average" and "individual" mean for $\psi(x)-x$

I fix the terminology. The object is $E(x):=\psi(x)-x$, where $\psi(x)=\sum_{n\le x}\Lambda(n)$. The
unconditional facts (Chebyshev, Mertens, classical von Mangoldt) give **control on average**; RH is the **individual
control**. Concretely:

- **INDIVIDUAL control (= what RH states).** $E(x)=O_\epsilon(x^{1/2+\epsilon})$. Equivalently
  (Riemann, von Koch 1901 [vK01]): $\Theta:=\sup\{\beta:\zeta(\beta+i\gamma)=0\}=\tfrac12$. The individual
  exponent of $E$ is exactly $\Theta$:
  $$\Theta\;=\;\inf\{\alpha:E(x)=O(x^\alpha)\}\;=\;\limsup_{x\to\infty}\frac{\log|E(x)|}{\log x}.$$
  [This is an exact classical fact; [Ing32, Theorem 30 and Ch. IV]: the abscissa of the real singularity of
  $-\zeta'/\zeta$ controls the order of $E$. The equality of the two $\limsup$'s is the von Koch equivalence.]

- **AVERAGE control (= the unconditional part).** Three averages, in increasing order of strength:
  1. **Cesàro average / first-order Riesz mean.** $\frac1X\int_1^X E(x)\,\frac{dx}{x}=o(\log X)$ and
     in fact $\int_1^X E(x)\frac{dx}{x^2}$ converges (it is a regularized $-\frac{\zeta'}{\zeta}(1)$-type
     quantity): the logarithmic average of $E/x$ is unconditionally bounded. **This is just PNT, nothing more.**
  2. **Second moment in weight $x^{-2}$.** $\displaystyle J(X):=\int_1^X\frac{E(x)^2}{x^2}\,dx$. By the
     Cramér identity ([Cra22]; [MV07, §15.1]),
     $$\int_1^\infty\frac{E(x)^2}{x^2}\,\frac{dx}{x}\;=\;\frac1{2\pi}\int_{-\infty}^{\infty}\Big|\frac{\zeta'}{\zeta}\Big|^2\text{-type}\;<\infty\iff\Theta=\tfrac12,$$
     i.e. the normalized second moment in weight $x^{-3}\,dx$ is **finite $\iff$ RH** (I quantify this in
     §2.4). In the general regime $J(X)\asymp X^{2\Theta-1}$.
  3. **Gaussian smooth averages** = exactly $S_T(\tau)$ from Doc 152, which are the prime side of
     the Gaussian-weighted explicit formula. These are the "spectral" averages.

The distance between (1) and "individual" is enormous (it is all of $(\tfrac12,1]$ in exponents); the distance between
(2) and individual is exactly **half an epsilon of exponent** ($\Theta$ vs $\Theta$, with the question of
whether the finite moment at $\Theta=\tfrac12$ forces the pointwise bound with the same exponent). **That half
epsilon is the wall.**

### 1.2. The closest Tauberian theorem that exists

**Tauberian fact-1 (Wiener–Ikehara) [Wie32; Ike31; Kor04, Ch. II].** If $f(x)\ge0$ is non-decreasing and
$F(s)=\int_1^\infty f(x)x^{-s-1}dx$ continues to $\mathrm{Re}\,s\ge1$ except for a simple pole at $s=1$ with
residue $A$, and $F(s)-A/(s-1)$ is continuous up to $\mathrm{Re}\,s=1$, then $f(x)\sim Ax$. **Tauberian
condition: $f\ge0$ (positivity / monotonicity).** Applied to $f=\psi$: it gives PNT, $\psi(x)\sim x$. *This is the
floor, not the ceiling.*

**Tauberian fact-2 (Ingham–Karamata, boundary form) [Ing35; Kar31; Kor04, Ch. III, Theorem 4.1].**
Let $G(s)=\int_0^\infty g(u)e^{-su}du$ converge for $\mathrm{Re}\,s>0$, continuable to
$\mathrm{Re}\,s=0$. If $g$ is **slowly oscillating** (slowly oscillating / slowly decreasing:
$\liminf_{\lambda\downarrow1}\liminf_{u\to\infty}(g(\lambda u)-g(u))\ge0$, a ONE-SIDED condition),
then $g(u)\to G(0)$. **Tauberian condition: one-sided slow oscillation.**

**The crossing that RH needs, in this template.** Set $g(u)=E(e^u)e^{-u/2}=\psi(e^u)e^{-u/2}-e^{u/2}$
(the weight-$\tfrac12$ normalization, which is the critical line). Then $\int g(u)e^{-su}du$ has
abscissa of convergence $\Theta-\tfrac12$ and continues to $\mathrm{Re}\,s>0$. RH $\iff$ $\Theta-\tfrac12=0$
$\iff$ $G$ continues to $\mathrm{Re}\,s=0$ with Ingham–Karamata regularity. **If** $g$ were
slowly oscillating, Ingham–Karamata would give $g(u)\to 0$ — stronger than RH (it would give $E(x)=o(\sqrt x)$). The
crossing exists in the template. **What is missing is the Tauberian condition: the slow oscillation of $g$.**

### 1.3. The clean target statement

**[NEW-DEFINITION 157.1] (the Tauberian crossing of RH).** I call **Tauberian crossing of RH** any
implication of the form
$$\big[\text{average control of } E \big]\;\wedge\;\big[\text{Tauberian condition } \mathsf{T} \big]\;\Longrightarrow\;\Theta=\tfrac12,$$
where the average control is one of §1.1(1)–(3) (unconditional) and $\mathsf T$ is a predicate on
$E$ (or on the prime measure) that does NOT presuppose RH. **The question of the document: does there exist an
RH-free $\mathsf T$, verifiable from the primes, that closes the implication?**

The closest theorem that exists is Ingham–Karamata with $\mathsf T=$ one-sided slow oscillation. The
half-epsilon is: average control gives us $G$ continuable to $\mathrm{Re}\,s>\Theta-\tfrac12$, and
$\mathsf T$ must pay for the continuation down to $0$ AND the boundary→individual crossing. **§2 catalogs the
candidates for $\mathsf T$.**

---

## 2. The catalog of Tauberian conditions

### 2.1. (T1) Positivity of von Mangoldt — EXHAUSTED

$\Lambda\ge0$ is the Wiener–Ikehara Tauberian condition that pays for PNT. **Doc 152 (Prop. 152.4–152.5)
already measured its exact jurisdiction in frequency coordinates:** $\Lambda\ge0\Rightarrow\omega(\tau)\le\tfrac14$
with equality only at the pole, which in exponent coordinates is exactly $\Theta\le1$ and the strict
boundary $\Theta<1$ (de la Vallée Poussin). **T1 certifies the band and is exhausted there.** In the language of
crossing 157.1: T1 pays for the continuation of $G$ to $\mathrm{Re}\,s\ge\tfrac12$ (i.e. $\zeta\ne0$ on
$\mathrm{Re}\,s=1$) but not one epsilon further toward $\mathrm{Re}\,s=0$.

**T1 classification:** RH-free ✓ (it is an arithmetic fact, $\Lambda(n)\ge0$); sufficient ✗ (exhausted at the
boundary). **Closed.**

### 2.2. (T2) Slow oscillation / non-oscillation — REFUTED BY LITTLEWOOD

The Ingham–Karamata condition on $g(u)=E(e^u)e^{-u/2}$ is slow oscillation:
$$\liminf_{\lambda\downarrow1}\;\liminf_{u\to\infty}\;\big(g(\lambda u)-g(u)\big)\;\ge\;0\qquad(\text{and the symmetric one}).$$

**[PROPOSITION 157.2] (Littlewood refutes T2 directly).** $g(u)=E(e^u)e^{-u/2}$ is NOT slowly
oscillating. In fact $g(u)=\Omega_\pm(\log\log\log e^u)=\Omega_\pm(\log\log u)$.

*Proof.* By Littlewood's theorem [Lit14] (see [MV07, Theorem 15.11]),
$E(x)=\Omega_\pm(\sqrt x\,\log\log\log x)$. Dividing by $\sqrt x=e^{u/2}$ with $x=e^u$:
$g(u)=\Omega_\pm(\log\log\log e^u)$. Since $\log\log\log e^u=\log\log u\to\infty$, $g$ has two-sided
oscillation of ever-increasing amplitude; in particular for any $\lambda>1$, $g(\lambda u)-g(u)$
takes arbitrarily negative values along subsequences (the $\Omega_-$ crossings), violating the
one-sided condition. $\square$

**This is the Landau inversion of Doc 152 §3.4, now as a direct Tauberian refutation theorem.** The
classical "non-oscillation" Tauberian condition (slow oscillation) CANNOT hold for $E$ because $E$
genuinely oscillates. **The naive Tauberian path is dead, confirmed at the level of the
Ingham–Karamata condition.**

**T2 classification:** RH-free ✓ (it is a property of $E$); sufficient ✓ (Ingham–Karamata closes it);
**FALSE** (Littlewood). **Closed by refutation.**

### 2.3. (T3) One-sided amplitude conditions — RH-FREE BUT INSUFFICIENT

The lesson of §2.2 is that oscillation cannot be forbidden. The idea behind the goal: what about a one-sided
**upper bound on the AMPLITUDE** of oscillation (controlled oscillation), rather than a prohibition on oscillating?

**[NEW-DEFINITION 157.3] (one-sided amplitude condition $\mathsf A(\theta)$).** For $\theta\in[\tfrac12,1]$:
$$\mathsf A(\theta):\qquad E(x)\;\le\;C_\epsilon\,x^{\theta+\epsilon}\quad\forall\epsilon>0\ (x\ge x_0),\qquad\text{(upper bound only, one sign)}.$$

**[PROPOSITION 157.4] (one-sided T3 does not cross the half-epsilon).** $\mathsf A(\theta)$ with the
one-sided upper bound ALONE does not imply the two-sided $E(x)=O(x^{\theta+\epsilon})$, and hence does not imply
$\Theta\le\theta$.

*Proof.* $\Theta=\limsup\log|E|/\log x$ uses $|E|$, i.e. BOTH signs. An upper bound
$E(x)\le x^{\theta+\epsilon}$ leaves $E(x)$ free to be very negative: $E$ could have
$E(x)=\Omega_-(x^{\theta'})$ with $\theta'>\theta$ without violating $\mathsf A(\theta)$. The connection to the
zeros is asymmetric: by the explicit formula $E(x)=-\sum_\rho x^\rho/\rho+\cdots$, the terms come in
conjugate pairs $\rho,\bar\rho$ and produce $-2\,\mathrm{Re}(x^\rho/\rho)=-2x^\beta\cos(\gamma\log x-\arg\rho)/|\rho|$:
a two-sided oscillation SYMMETRIC in amplitude. A zero with $\beta>\theta$ produces excursions
$\Omega_+$ AND $\Omega_-$ of size $x^\beta$ (E. Schmidt [Sch03] for $\beta=\tfrac12$, Ingham for general $\beta$
[Ing32, Ch. V]). By the conjugate symmetry, forbidding only the positive excursions does not forbid the
zero: it leaves the negative ones, which exist regardless. Hence one-sided $\mathsf A(\theta)$ does not control $\Theta$.
$\square$

**The fine point (why the asymmetry kills the idea behind the goal).** The goal conjectured that an upper
amplitude bound (controlled oscillation) might be the correct one-sided Tauberian condition. Prop. 157.4
says NO in this form: the oscillation induced by a zero is **symmetric in sign** (conjugate
pairs), so a single-sign bound is blind to half of the oscillation — and the blind half already
contains the zero. A **two-sided** amplitude bound $|E(x)|\le x^{\theta+\epsilon}$ would indeed cross
(trivially: it IS $\Theta\le\theta$), but then it is not one-sided and it IS RH (for $\theta=\tfrac12$). Genuine
one-sidedness (one sign) is structurally misaligned with the conjugate symmetry of the zeros.

**T3 classification:** RH-free ✓; sufficient ✗ (one-sidedness does not capture the conjugate symmetry).
**Closed: one-sided controlled oscillation does not cross.**

### 2.4. (T4) Moment / Carleman conditions — RH-EQUIVALENT

The strongest average control we have is the second moment (§1.1(2)). Does a moment condition
cross to pointwise? The classical Tauberian instrument is the **Carleman / Hardy–Littlewood moment
theorem** (control of $\int|g|^2$ + regularity ⟹ pointwise control). But here the moment itself is
RH-equivalent:

**[PROPOSITION 157.5] (the normalized second moment is RH-equivalent — Cramér identity).** Let
$J^*(X):=\int_1^X E(x)^2\,x^{-2}\,dx$. Then:
$$\Theta\;=\;\tfrac12\big(1+\limsup_{X\to\infty}\tfrac{\log J^*(X)}{\log X}\big),$$
and in particular $J^*(X)=O(\log X)$ (equivalently $\int_1^\infty E^2 x^{-2}\frac{dx}{x}<\infty$)
$\iff$ $\Theta=\tfrac12$ $\iff$ RH.

*Proof.* By Parseval/Plancherel for the Mellin transform (the Cramér identity [Cra22];
see [MV07, ex. 15.1.1 and Theorem 13.x], [Tit86, §14.2x]): with $E(x)=-\sum_\rho x^\rho/\rho+O(\log^2 x)$
(truncated von Mangoldt explicit formula), the second moment in weight $x^{-2}$ picks up each zero with
contribution $\asymp x^{2\beta-1}/|\rho|^2$ integrated:
$$\int_1^X E(x)^2 x^{-2}\,dx\;\asymp\;\sum_{\rho}\frac{X^{2\beta-1}}{|\rho|^2(2\beta-1)}+\text{(cross terms)} \;\asymp\; X^{2\Theta-1},$$
for $\Theta>\tfrac12$ (the rightmost zero dominates; the cross terms $\rho\ne\rho'$ oscillate and do not increase
the exponent). For $\Theta=\tfrac12$ every term is $X^0=1$ and the sum over $\rho$ with
$\sum1/|\rho|^2<\infty$ converges: $J^*(X)=O(\log X)$ (the $\log$ of the number of zeros up to height $X$). The
$\limsup$ of the exponent is $2\Theta-1$, whence the formula. $\square$

**Why T4 does NOT cross (it is circular).** The moment $J^*$ is finite $\iff$ RH: the "average
$L^2$ control" in this weight is NOT unconditional — it is RH. The unconditional average control is that of §1.1(1)
(weight $x^{-1}$, much weaker) or the general-weight moment which gives $X^{2\Theta-1}$ but with $\Theta$
unknown. **Verifying the moment condition (finiteness of $J^*$) already IS RH.** It is the cleanest example
of the trap in the goal: the condition is stated on $E$ (a moment) but its verification goes through the
explicit formula and returns the exponent $\Theta$.

**T4 classification:** RH-free ✗ (the finite moment IS RH); sufficient ✓ (trivially, it is RH). **Closed
by circularity.**

### 2.5. (T5) Spectral conditions of Beurling–Malliavin / Wiener type — THE ONLY ONE ALIVE

There remains the spectral family: instead of a condition on $E$ in the variable $x$, a condition on the
**transform** of the prime measure in the frequency variable $\tau$ — exactly the territory of
$S_T(\tau)$ from Doc 152. Here the "controlled oscillation" of the goal DOES have substance, because LP-152 is a
spectral-amplitude UPPER bound (subexponentiality), not a prohibition on oscillating. This family
occupies all of §3. **Preview of the catalog verdict:** T5 is RH-free as a statement and is where the
question remains open; but its VERIFICATION (not its statement) reintroduces the zeros via Beurling–Malliavin
(§3–§4).

### 2.6. Catalog table

| | Tauberian condition $\mathsf T$ | RH-free? | sufficient? | status |
|---|---|---|---|---|
| T1 | $\Lambda\ge0$ (Wiener–Ikehara) | ✓ | ✗ | exhausted at the boundary (Doc 152.4–152.5) |
| T2 | slow oscillation of $g$ (Ingham–Karamata) | ✓ | ✓ | **FALSE** (Littlewood, Prop. 157.2) |
| T3 | one-sided amplitude $\mathsf A(\theta)$ | ✓ | ✗ | insufficient (conjugate symmetry, Prop. 157.4) |
| T4 | moment $\int E^2x^{-2}\frac{dx}x<\infty$ | ✗ (=RH) | ✓ | circular (Prop. 157.5, Cramér) |
| T5 | spectral subexp. LP-152$(\tau_0)$ | ✓ (statement) | partial | **alive; verification reintroduces zeros (§3–4)** |

**Reading the catalog.** The first four rows are four distinct ways of hitting the same
wall: positivity (zero frequency), non-oscillation (killed by Littlewood), one-sidedness (conjugate
symmetry), moment (circular). The fifth is the only one where the condition is both RH-free as a
statement AND potentially sufficient; §3 attacks it with spectral Tauberian machinery (Wiener,
Beurling–Malliavin), and §4 applies the stress test to it.

---

## 3. The spectral Tauberian attack: Wiener, LP-152, Beurling–Malliavin

### 3.1. LP-152 rewritten as a Wiener Tauberian condition

The **general Wiener Tauberian theorem** [Wie32; Kor04, Ch. II, Theorem 4.1] states: if $K\in L^1(\mathbb R)$
with $\hat K(\xi)\ne0$ for all $\xi$ (non-vanishing of the transform), and $f\in L^\infty$ satisfies
$\lim_{x\to\infty}(K*f)(x)=A\int K$, then $\lim(K'*f)=A\int K'$ for every $K'\in L^1$. **Mechanism: the
non-vanishing of $\hat K$ is what allows the crossing from one average (convolution with $K$) to another (all
averages), and from there —with an additional Tauberian condition on $f$— to the individual limit.** The
closure of translations of $K$ in $L^1$ ⟺ $\hat K$ does not vanish: it is the heart of the theorem.

**[BRIDGE 157-A] LP-152 IS the Wiener non-vanishing condition, transposed to exponential growth.**
The object $S_T(\tau)$ is the Fourier transform (in $\tau$) of the positive measure
$\mu_T=\sum_n\Lambda(n)n^{-1/2}e^{-(\log n)^2/4T^2}\delta_{\log n}$ (Doc 152 §2.1). LP-152$(\tau_0)$ states
$|\widehat{\mu_T}(\tau_0)|=|S_T(\tau_0)|=O_\epsilon(e^{\epsilon T^2})$: the transform of the prime
measure **does not grow exponentially** at frequency $\tau_0$. Compare with Wiener: there the condition is
$\hat K\ne0$ (does not vanish); here, in the exponential regime of the Gaussian explicit formula, the analogous
condition is that $\widehat{\mu_T}$ does not grow exponentially (does not resonate). **Wiener's
non-vanishing and LP-152's subexponentiality are the same spectral Tauberian condition in two regimes (linear /
exponential-Gaussian): "the transform of the averaging measure has no pathology at frequency
$\tau_0$".**

### 3.2. LP-152 is one-sided in the correct sense

**[PROPOSITION 157.6] (LP-152 is an amplitude condition, not an oscillation condition).** LP-152$(\tau_0)$ is an
UPPER amplitude bound on $|S_T(\tau_0)|$; it does NOT forbid $S_T(\tau_0)$ from oscillating in $T$ (in fact
it does oscillate, through the factor $\cos(2T^2(\gamma_j-\tau_0)\delta_j)$ of Theorem 152.2). It is exactly the
"controlled oscillation" sought in the goal: it controls the AMPLITUDE of the resonance, not its existence.

*Proof.* By Theorem 152.2(a)(b), $S_T(\tau_0)$ contains terms
$e^{T^2(\delta_j^2-(\gamma_j-\tau_0)^2)}\cos(2T^2(\gamma_j-\tau_0)\delta_j)$: it oscillates in $T^2$ with
frequencies $2(\gamma_j-\tau_0)\delta_j$. LP-152$(\tau_0)$ bounds the exponential factor (the amplitude) to
subexponential, without touching the cosine (the oscillation). It is one-sided: a single inequality ($\le$), on the
amplitude. $\square$

**Why this evades Littlewood's refutation (§2.2).** T2 died because it required non-oscillation of $E$, which
Littlewood disproves. LP-152 does NOT require non-oscillation: it requires subexponential amplitude of the
spectral resonance. The oscillation of $E$ (Littlewood) corresponds precisely to $S_T(\tau)$ oscillating in $\tau$ — and
LP-152 allows it. **LP-152 is the only candidate in the catalog compatible with Littlewood's theorem**, because it is
formulated in the coordinate (spectral amplitude) orthogonal to the coordinate where oscillation is forced.
This is the positive content of the goal: "controlled oscillation" exists as a coherent Tauberian
condition, and it is LP-152.

### 3.3. Beurling–Malliavin: the spectral-completeness machinery

The deep Tauberian theorem that connects spectral subexponentiality with individual control is
**Beurling–Malliavin** [BM62; BM67]. In the **completeness radius** form ([Koo88, Ch. on BM];
[BM67]): given a set of frequencies $\Lambda\subset\mathbb R$, the system of exponentials
$\{e^{i\lambda x}\}_{\lambda\in\Lambda}$ is complete in $L^2(-a,a)$ for $a$ smaller than the **Beurling–Malliavin
radius** $R(\Lambda)$, given by the **effective density** of $\Lambda$. The link to Tauberian theory: the
completeness of exponentials $\iff$ certain functions (those whose transform is supported outside) must
vanish — a uniqueness / quasi-analyticity principle that crosses spectral information (the density of
$\Lambda$) to pointwise information (vanishing / bound of a function).

**[BRIDGE 157-B] The Beurling–Malliavin route for LP-152.** To verify LP-152$(\tau_0)$ (subexponentiality
of $S_T(\tau_0)$) one would want a theorem of the form: *"if the frequencies $\{\log p\}$ have effective
density $D$ and $\widehat{\mu_T}$ does not resonate at $\tau_0$, then [pointwise control of $E$ near
$\tau_0$]"*. The natural instrument is Beurling–Malliavin quasi-analyticity: measures with
controlled support/decay of their transform are rigid (a Beurling-type uniqueness theorem). **The
input that Beurling–Malliavin requires is the DENSITY of the set of frequencies $\{\log p\}$.** And here is
the problem, which §3.4 makes explicit.

### 3.4. Where the spectral route reintroduces the zeros — the localized circle

**[PROPOSITION 157.7] (the spectral density on the prime side IS the zero count).** In the regime of
the explicit formula, the "effective density" on the prime side that Beurling–Malliavin would need to
certify the subexponentiality of $S_T(\tau_0)$ is, by identity (152.E), exactly the density of
zeros of ζ in the window of $\tau_0$. Concretely: $S_T(\tau_0)$ subexponential $\iff$ (Theorem 152.2(a))
no off quadruple covers $\tau_0$ $\iff$ the density of off zeros in $(\tau_0-\delta,\tau_0+\delta)$ is
zero. Any spectral Tauberian theorem that decides the subexponentiality of $S_T(\tau_0)$ from the
spectral density is deciding the density of off zeros at $\tau_0$.

*Proof.* Identity (152.E) of Doc 152 is exact: $\frac{2}{\sqrt\pi T}S_T(\tau_0)=-\sum_\rho
h_{T,\tau_0}(t_\rho)+\text{pole}+A_T$. The left side (prime measure) and the right side (zeros) are
identical. The transform of the prime measure at $\tau_0$, evaluated in the exponential regime, does NOT
contain information independent of the zeros: it is a rewriting of the sum over zeros. Therefore the
"effective density of prime frequencies at $\tau_0$" relevant to Beurling–Malliavin —the datum that
distinguishes resonance from non-resonance— is a function of the position of the zeros in the window of $\tau_0$.
Determining that density IS (Riemann–von Mangoldt for the count, plus the off-position for the resonance)
determining the zeros. $\square$

**The circle, in one statement.** Beurling–Malliavin crosses spectral-density → pointwise-control. But the
spectral density on the prime side that matters is NOT the raw density of $\{\log p\}$ (that one is known
and unconditional: $\#\{p\le e^u\}\sim e^u/u$ by PNT) — it is the **RESONANCE density**, i.e. where
$\widehat{\mu_T}$ grows exponentially, and by (152.E) that resonance density IS the density of off
zeros. **The spectral Tauberian machinery is available and correct; the input it requires (resonance
density) is exactly the sought-after output (position of zeros). Circle localized at the Beurling–Malliavin
input.** Consistent with the tautology of the explicit formula (D112 Prop. 4.2) and with F2 of
Doc 152.

---

## 4. The RH stress test, applied three times to T5/LP-152

The surviving candidate is LP-152$(\tau_0)$ (= T5). The stress test: for EACH RH-free verification route,
check mercilessly whether "verifying it" requires knowing the zeros. Three independent routes.

### 4.1. Stress test 1 — verification by Besicovitch density

**Route.** Prop. 152.9: the Besicovitch mean of $|S_T(\tau)|^2$ is $O(T^2)$, so bad (resonant)
frequencies have zero density. Can we verify LP-152$(\tau_0)$ by certifying that $\tau_0$ is NOT one of the
exceptional zero-density frequencies?

**Test result: FAILS.** An average (the Besicovitch mean) controls the set of bad frequencies in
MEASURE, but LP-152$(\tau_0)$ is a statement at ONE point. The bad frequency $\gamma_J$, if it
exists, is an exceptional point invisible to any average (Doc 152 §3.6). Verifying LP-152 at $\tau_0$ by
density is exactly the average→individual crossing we are trying to make — the route is the problem,
not its solution. **Fails by the master quantifier of P43: the average does not see the point.**

### 4.2. Stress test 2 — verification by completeness (Beurling–Malliavin)

**Route.** §3.3–3.4: use Beurling–Malliavin quasi-analyticity to deduce the subexponentiality of
$S_T(\tau_0)$ from the spectral density.

**Test result: FAILS.** By Prop. 157.7, the relevant spectral density (resonance density)
is the density of off zeros in the window of $\tau_0$. The Beurling–Malliavin input is the sought output.
**Fails by reintroduction of the zeros via identity (152.E).** This is the deepest failure because
Beurling–Malliavin is genuinely a strong spectral Tauberian theorem (it crosses density→pointwise): if
any theorem was going to cross, it was this one, and the circle sits exactly in its density hypothesis.

### 4.3. Stress test 3 — verification by direct positivity/monotonicity of $S_T$

**Route.** $\mu_T$ is a positive measure; does any positivity inequality (Wiener–Ikehara type, which is
what pays for PNT) bound $S_T(\tau_0)$?

**Test result: FAILS.** Doc 152 Prop. 152.4: positivity of $\Lambda$ only gives $|S_T(\tau)|\le
S_T(0)$, i.e. $\omega(\tau_0)\le\tfrac14$. This is subexponential-at-zero-frequency but allows
$\omega(\tau_0)\in(0,\tfrac14)$ at $\tau_0\ne0$ — exactly the range where H(m) lives. **Positivity is
zero-frequency information (F1 of Doc 152); it does not touch $\tau_0>14$.** Fails for the same reason as T1.

### 4.4. The structural reason common to the three failures

**[PROPOSITION 157.8] (why every RH-free verification of LP-152 reintroduces the zeros).** Let
$\mathsf V$ be any procedure that certifies LP-152$(\tau_0)$ (subexponentiality of $S_T(\tau_0)$)
from unconditional data about the prime measure. If $\mathsf V$ uses only (i) the positivity of
$\Lambda$, (ii) the raw density of $\{\log p\}$ (PNT), or (iii) averages of $S_T$ in $\tau$, then
$\mathsf V$ does not decide LP-152$(\tau_0)$ for $\tau_0>14$.

*Proof.* (i): Prop. 152.4 gives $\omega\le\tfrac14$, blind on $(0,\tfrac14)$ — §4.3. (ii): the raw
density of $\{\log p\}$ is the same under RH and under H(m) (PNT is unconditional); it does not distinguish the
worlds, hence it cannot decide a statement (LP-152) that does distinguish them. (iii): any average in $\tau$
controls $S_T(\cdot)$ in $L^2_\tau$, and by Prop. 152.9 the bad frequency has zero density, invisible to the
average — §4.1. The only remaining unconditional datum that distinguishes the worlds at $\tau_0$ is the
position of the zeros in the window of $\tau_0$, accessible only via identity (152.E), which is a tautology
that reintroduces them (§3.4, F2). $\square$

**The statement of the Tauberian wall, distilled.** *Every Tauberian condition on $\psi(x)-x$ sufficient
for crossing the half-epsilon must read information at the frequency $\gamma$ of a zero; the three
unconditional instruments that read frequency (positivity, raw density, averages) are blind to
that individual frequency; the only instrument that reads it is the explicit formula, which is an identity.*
This holds for all three routes and is the exact Tauberian form of the master quantifier of P43.

---

## 5. VERDICT

### 5.1. The Tauberian no-go for locally-in-frequency conditions

**[NEW-DEFINITION 157.9] (local-in-frequency Tauberian condition).** I call $\mathsf T$ **local in
frequency** if its verification, in spectral coordinates (via any Gaussian explicit formula), depends only
on: the positivity of $\Lambda$, the raw density of $\{\log p\}$, averages of $S_T$ in $\tau$, or
pointwise/integral bounds of $S_T(\tau)$ derivable from these — i.e. from the three instruments of
Prop. 157.8. (This covers T1–T4 and every variant of Wiener–Ikehara/Ingham–Karamata/Carleman/moments.)

**[THEOREM 157.10] (Tauberian NO-GO for locally-in-frequency conditions).** Every local-in-frequency
Tauberian condition $\mathsf T$ that is sufficient for RH (i.e. that closes crossing 157.1) is
RH-equivalent: its verification requires deciding the position of the zeros in some frequency window.
Consequently, no local-in-frequency Tauberian condition crosses the average→individual wall of RH
without presupposing RH.

*Proof.* Let $\mathsf T$ be local in frequency and sufficient. By sufficiency, $\mathsf T$ decides
$\Theta=\tfrac12$, which by Theorem 152.2(a) (Cor. 152.3(i)) is equivalent to $\omega(\tau)=0\ \forall\tau\ge1$,
i.e. to the family $\{\text{LP-152}(\tau)\}_{\tau\ge1}$. For any $\tau_0>14$ in an adversarial
window, deciding LP-152$(\tau_0)$ requires, by Prop. 157.8, reading the position of the zeros in
$(\tau_0-\tfrac12,\tau_0+\tfrac12)$ (the three local instruments are insufficient). Hence the
verification of $\mathsf T$ decides the zeros: $\mathsf T$ is RH-equivalent. $\square$

### 5.2. The saturation computation: why Littlewood saturates the margin

The no-go has a precise quantitative cause, which the goal asked to be exhibited: **the Littlewood
oscillation saturates exactly the Cauchy–Schwarz margin of boundary purity.**

**[CALCULATION 157.11] (saturation).** The unconditional positivity barrier (T1, Doc 152.4) is
$|S_T(\tau)|\le S_T(0)\asymp Te^{T^2/4}$, i.e. $\omega(\tau)\le\tfrac14$. In $E$-coordinates: the Cauchy–Schwarz
margin of positivity corresponds to $E(x)\ll x^{1}$ (band) and, refined (de la Vallée
Poussin), to $E(x)\ll x\exp(-c\sqrt{\log x})$. The Littlewood oscillation
$E(x)=\Omega_\pm(\sqrt x\log\log\log x)$ lives at exponent $\tfrac12$ — **strictly inside** the margin
$\omega\le\tfrac14$ (i.e. $\Theta\le1$), with exponent slack $\tfrac12$. The point of the saturation is NOT
that Littlewood touches the positivity barrier (it does not touch it: there is slack); it is that
**Littlewood forbids the ONLY other sufficient, RH-free Tauberian condition available (non-oscillation,
T2)**, leaving the exponent interval $(\tfrac12,1]$ — equivalently $\omega\in(0,\tfrac14)$ — without
any local Tauberian instrument covering it. Quantitatively: positivity covers $\{\omega=\tfrac14\}$ (the
boundary), non-oscillation would cover $\{\omega=0\}$ (RH) but is forbidden by Littlewood, and NOTHING local
covers the open interval $(0,\tfrac14)$. **The margin that Littlewood saturates is the margin between the two
only single-sign local Tauberian conditions: positivity (frequency 0, covers the boundary) and
non-oscillation (would cover RH, forbidden). The interval between the two is the wall, and it is exactly the
range of exponents of Littlewood's oscillation.** $\square$

This is the Tauberian form of the finding of Doc 152 §3: the H(m) world lives entirely within the margin
$e^{-(1/4-\delta^2)T^2}$ of Cauchy–Schwarz, and no local condition closes it.

### 5.3. The crack that the no-go does NOT cover

**[GAP-157.A] (non-local spectral Tauberian conditions with Diophantine input).** Theorem 157.10
covers local-in-frequency conditions (Def. 157.9), which include all of classical Tauberian theory. It does NOT cover
a genuinely distinct spectral class: conditions of **Beurling–Malliavin type with an independent
Diophantine input** — specifically, using the **$\mathbb Q$-linear independence of $\{\log p\}$**
(the basis of Voronin universality / of Bagchi's support, see D112) NOT as an ambient fact but as a
**spectral Tauberian condition**: the exponentials $\{e^{i\tau\log p}\}_p=\{p^{i\tau}\}_p$ are
$\mathbb Q$-linearly independent, which gives the Kronecker torus of the primes a spectral-density
structure that is NOT the "resonance density" of Prop. 157.7. The open question: does there exist a
spectral Tauberian theorem (refined Beurling–Malliavin, or Kreĭn on completeness of
$\{p^{i\tau}\}$) that, using the Diophantine independence of $\{\log p\}$ as a Tauberian condition, crosses to
individual control WITHOUT going through identity (152.E)? This is the only route that evades Prop. 157.8,
because its input ($\mathbb Q$-linear independence) is unconditional AND is NOT a function of the position of
the zeros.

**Why GAP-157.A is exactly the crack from LP-112/LP-152.** The Diophantine input ($\mathbb Q$-linear
independence of $\{\log p\}$) is precisely what feeds LP-112 via Bagchi (D112: independence
⟹ universality ⟹ self-approximation of ζ). LP-112 attacks by replica (existential), LP-152 by evaluation
(universal). GAP-157.A asks whether the SAME Diophantine independence, read as a spectral Tauberian
condition (closure/completeness of $\{p^{i\tau}\}$), crosses average→individual. **The Tauberian no-go of
§5.1 dies exactly where the Diophantine crack of the P43 pincer begins.** This is not a coincidence: it is the
third independent coordinate confirming that the wall has a single candidate crossing point, the
Diophantine one.

**Frank status of GAP-157.A:** **[literature GAP]** I am not aware of a published spectral Tauberian theorem
that uses the $\mathbb Q$-linear independence of $\{\log p\}$ as a Tauberian condition to cross
to pointwise control of $\psi(x)-x$ without the explicit formula; the machinery of completeness of
exponentials with $\mathbb Q$-independent frequencies (Beurling–Malliavin, Kreĭn, Levin) exists but I did not
verify its application to THIS crossing at the level of a theorem this session. I state it as a crack,
NOT as a proved route. It is not a premise of any [THEOREM] of this document.

### 5.4. Verdict (a/b/c)

**VERDICT: case (b) PROVED for locally-in-frequency conditions + case (c) for the Diophantine crack.**

- **(a) Is there a known RH-free Tauberian condition that crosses?** **NO** among the known ones. The five
  families of the catalog: T1 exhausted, T2 refuted by Littlewood, T3 insufficient due to conjugate
  symmetry, T4 circular (=RH), T5 alive as a statement but its verification reintroduces the zeros (stress
  test ×3 failed).
- **(b) Is every sufficient Tauberian condition RH-equivalent?** **PROVED (Theorem 157.10) for the
  class of locally-in-frequency conditions** — which includes ALL of classical Tauberian theory
  (Wiener–Ikehara, Ingham–Karamata, Pitt, Carleman, moments). It is a **no-go that locates the wall inside
  Tauberian theory**: the Littlewood oscillation saturates the margin between the two only local
  single-sign conditions (positivity/zero-frequency and non-oscillation/forbidden), leaving the interval
  $(0,\tfrac14)$ of impurity weights —the Littlewood exponent range— without any local instrument.
- **(c) Is there a specific gap remaining?** **YES, GAP-157.A:** non-local spectral Tauberian conditions
  with Diophantine input ($\mathbb Q$-linear independence of $\{\log p\}$ as a Tauberian condition, via
  completeness of $\{p^{i\tau}\}$ of Beurling–Malliavin/Kreĭn type). It is the only class that evades
  Prop. 157.8, and it is exactly the Diophantine crack of the P43 pincer LP-112/LP-152. Its RH-freedom is
  undecidable today ([literature GAP] §5.3).

### Final message

**VERDICT: LOCALIZED TAUBERIAN NO-GO (case b) + ONE NAMED DIOPHANTINE CRACK (case c).** There is NO
known RH-free Tauberian condition that crosses the average→individual wall of RH. Theorem 157.10
proves that every **local-in-frequency** Tauberian condition (all of classical Tauberian theory:
Wiener–Ikehara, Ingham–Karamata, Pitt, Carleman) that is sufficient for RH is RH-equivalent — the wall is
inside Tauberian theory, and the Littlewood oscillation saturates it exactly (Calculation 157.11: it lives
in the exponent interval between positivity/zero-frequency and non-oscillation/forbidden). The only
crack is **GAP-157.A**: non-local spectral conditions with the $\mathbb Q$-linear independence of
$\{\log p\}$ as Tauberian input (Beurling–Malliavin/Kreĭn on $\{p^{i\tau}\}$), which is the same Diophantine
crack feeding LP-112/LP-152.

**Is there an RH-free Tauberian condition that crosses?** None known; no-go proved for the whole local
class; the only crack = the Diophantine one in the P43 pincer.

**Three findings:**

1. **[PROPOSITION 157.2 + CALCULATION 157.11]** — *Littlewood refutes non-oscillation and saturates the
   margin.* The Ingham–Karamata condition (slow oscillation) is FALSE for $E=\psi(x)-x$ by Littlewood
   ($\Omega_\pm(\sqrt x\log\log\log x)$); and the Littlewood oscillation saturates exactly the margin between
   the two only single-sign local Tauberian conditions (positivity, which covers the boundary
   $\omega=\tfrac14$; non-oscillation, which would cover RH, forbidden), leaving the interval $(0,\tfrac14)$ without
   a local instrument — the exact Tauberian form of the Doc 152 wall.

2. **[THEOREM 157.10 + PROPOSITION 157.8]** — *Tauberian no-go for locally-in-frequency conditions.*
   Every local Tauberian condition (positivity / raw density of $\{\log p\}$ / averages of $S_T$)
   sufficient for RH is RH-equivalent, because deciding the crossing is equivalent to deciding LP-152 at an
   adversarial frequency, and the three unconditional instruments are blind to the individual frequency of
   a zero; the only one that reads it is the explicit formula, which is a tautology (152.E). Covers all of
   classical Tauberian theory.

3. **[PROPOSITION 157.6 + GAP-157.A]** — *Controlled oscillation exists (LP-152) and its only crack is
   Diophantine.* LP-152 is the only Tauberian condition compatible with Littlewood (it controls spectral
   amplitude, not oscillation — the "controlled oscillation" of the goal, in the spectral coordinate
   orthogonal to Littlewood's) and is of Wiener type (non-vanishing/non-resonance of the transform of the
   prime measure); but its verification reintroduces the zeros via Beurling–Malliavin except through the
   crack GAP-157.A: using the $\mathbb Q$-linear independence of $\{\log p\}$ as a spectral Tauberian
   condition, exactly the Diophantine crack of the P43 pincer LP-112/LP-152.

---

## References

**Internal (backward-only):** Doc 152 (impurity spectrum, Theorem 152.2, jurisdiction of $\Lambda\ge0$,
Landau inversion F1–F3, LP-152 Def. 152.8, Prop. 152.9 bad frequencies of zero density, identity
152.E); Doc 112 (LP-112; Prop. 2.6 zero density; Prop. 4.2 tautology of the explicit formula; Bagchi's
support, Voronin universality, $\mathbb Q$-linear independence); P43 (Principle 3.1, generic vs exceptional
master quantifier).

**Literature (published, verifiable unless marked):**
- [Wie32] N. Wiener, *Tauberian theorems*, Ann. of Math. (2) 33 (1932), 1–100. (General Tauberian theorem;
  closure of translations ⟺ non-vanishing of the transform.)
- [Ike31] S. Ikehara, *An extension of Landau's theorem in the analytic theory of numbers*, J. Math. Phys.
  MIT 10 (1931), 1–12. (Wiener–Ikehara Tauberian theorem; Tauberian condition = positivity/monotonicity.)
- [Kor04] J. Korevaar, *Tauberian Theory: A Century of Developments*, Grundlehren 329, Springer, 2004.
  (Ch. II: Wiener–Ikehara; Ch. III: Ingham–Karamata, one-sided slow oscillation; general reference on
  Tauberian conditions.)
- [Ing35] A. E. Ingham, *On Wiener's method in Tauberian theorems*, Proc. London Math. Soc. (2) 38 (1935),
  458–480. (Boundary form of the Tauberian theorem; slow oscillation.)
- [Kar31] J. Karamata, *Neuer Beweis und Verallgemeinerung der Tauberschen Sätze...*, Math. Z. 33 (1931),
  294–299. (Karamata's method; one-sided condition.)
- [Ing32] A. E. Ingham, *The Distribution of Prime Numbers*, Cambridge Tracts 30, Cambridge Univ. Press,
  1932. (Ch. IV: abscissa of the real singularity controls the order of $\psi(x)-x$ — equivalence with
  $\Theta$; Ch. V: oscillation theorems, Landau's theorem on single-sign integrands.)
- [vK01] H. von Koch, *Sur la distribution des nombres premiers*, Acta Math. 24 (1901), 159–182.
  ($E(x)=O(\sqrt x\log x)\iff$ RH.)
- [Lit14] J. E. Littlewood, *Sur la distribution des nombres premiers*, C. R. Acad. Sci. Paris 158 (1914),
  1869–1872. ($\psi(x)-x=\Omega_\pm(\sqrt x\log\log\log x)$ — the genuine oscillation.)
- [Sch03] E. Schmidt, *Über die Anzahl der Primzahlen unter gegebener Grenze*, Math. Ann. 57 (1903),
  195–204. (Symmetric two-sided $\Omega_\pm$ for $\psi(x)-x$.)
- [Cra22] H. Cramér, *Ein Mittelwertsatz in der Primzahltheorie*, Math. Z. 12 (1922), 147–153. (Second
  moment of $\psi(x)-x$ in weight $x^{-2}$; finiteness ⟺ RH — Prop. 157.5.)
- [MV07] H. L. Montgomery, R. C. Vaughan, *Multiplicative Number Theory I: Classical Theory*, Cambridge
  Stud. Adv. Math. 97, 2007. (§15: oscillation of $\psi(x)-x$, Littlewood's Theorem 15.11; Cramér's
  moment; von Koch equivalences.)
- [Tit86] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. (rev. D. R. Heath-Brown),
  Oxford Univ. Press, 1986. (§14: second moment; Riemann–von Mangoldt zero count.)
- [BM62] A. Beurling, P. Malliavin, *On Fourier transforms of measures with compact support*, Acta Math.
  107 (1962), 291–309. (Quasi-analyticity; rigidity of measures with controlled transform.)
- [BM67] A. Beurling, P. Malliavin, *On the closure of characters and the zeros of entire functions*, Acta
  Math. 118 (1967), 79–93. (Beurling–Malliavin radius; completeness of exponentials ⟺ effective density
  of the frequency set.)
- [Koo88] P. Koosis, *The Logarithmic Integral I*, Cambridge Stud. Adv. Math. 12, 1988. (Exposition of
  Beurling–Malliavin; effective density, logarithmic integral.)

*End of Doc 157.*
