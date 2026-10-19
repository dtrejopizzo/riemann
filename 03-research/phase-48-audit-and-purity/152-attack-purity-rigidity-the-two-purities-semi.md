# Doc 152 — Attack purity ⟹ rigidity: the two purities, semi-global purity, and the attempt «m<∞ + Λ≥0 + functional equation ⟹ m=0»

**Program:** Riemann Hypothesis — Phase 48: AUDIT AND PURITY.
**Role of the document:** attack the rigidity half **m<∞ ⟹ m=0** of the architecture
$\mathrm{RH}=(m<\infty)\wedge(m<\infty\Rightarrow m=0)$ (D-109), in light of the Phase 47 finding
(Doc 146): repulsion is cheap (given by the quasi-Euler of Davenport–Heilbronn) and what is missing is the
**purity/positivity** that collapses $m$ to 0. The goal: (1) clarify the two purities of the program
(local/global) and the weight discrepancy; (2) propose the intermediate **semi-global** purity — what D–H
violates and ζ has; (3) attempt the theorem «$m<\infty$ + $\Lambda\ge0$ + functional equation $\Rightarrow m=0$»
via the explicit formula/oscillations, with each step labeled; (4) locate the exact failure point and the
minimal hypothesis that would save it, compared with RH and with LP-112; (5) verdict.

**Creative contract (absolute labeling rule):** **[NEW-DEFINITION]** = total freedom.
**[THEOREM]/[PROPOSITION]/[LEMMA]** = GENUINELY proved here, complete proof; external results cited
precisely. **[CALCULATION]** = shown. **[BRIDGE]** = connection with honest status. **[GAP]** = declared.
**[DESIDERATUM]** = declared. **[literature GAP]** = datum not verified at page level this session, NOT
used as a premise of any [THEOREM]. No proof of RH or of rigidity is ever fabricated.

**Prerequisites read at the source this session:** Doc 146 in full (cheap repulsion / expensive purity; D–H
fat, zeros with $\beta>1$); Doc 144 in full (LP-141, category D131-H⁺, Conjecture 144.D); Doc 131 §6
in full (Theorem 6.7 local purity, two-bump Mertens test, Prop. 6.5 diagonal mass, Prop. 6.8 D–H by
blocks, Desideratum 6.9 = Conjecture H⁺); Doc 112 in full (LP-112, Theorem 2.3/5.1, Prop. 2.6 zero
density, Prop. 4.2 explicit-formula tautology, Obs. 4.3 external evaluators); Doc 135 §7.2 (breakpoints
B1–B4; B3 = weight mismatch); Doc 137 (audit of the boundary $|\alpha|=1$). Phase 38 ERRATA respected:
$W_\lambda\ge0$ is refuted and is NOT used.

---

## 0. Executive summary

1. **(§1) The two purities, clarified, and the weight discrepancy resolved in a single statement.** The
   local purity of Doc 131 (Theorem 6.7) is purity **of weight 1**: $|\alpha|=\sqrt p$, local divisor at the
   **center** $\mathrm{Re}=\tfrac12$, barrier $|c_m|\le 2p^{m/2}$. The local factor of ζ has $\alpha=1$:
   it is **pure of weight 0** (local divisor at the **boundary** $\mathrm{Re}\in\{0,1\}$, $\sigma$-free orbit)
   and, read in the weight-1 normalization, is **maximally impure** ($c_m=1+p^m>2p^{m/2}$ for every
   $m\ge1$; the boundary $|\alpha|=1$ audited in Doc 137 kills H). The global functional equation recenters the
   **archimedean weights** (gamma factor, pole: swap B1 of Doc 135) but NOT the zeros: **RH is the recentering
   of the zeros from weight 0 to weight 1, the one piece the functional equation does not do** (= B3 of Doc 135,
   now stated as a purity statement).

2. **(§2) Semi-global purity exists and has a theorem.** [NEW-DEFINITION 152.1]: the **Gaussian prime
   correlation** $S_T(\tau):=\sum_n\Lambda(n)n^{-1/2}e^{-(\log n)^2/4T^2}\cos(\tau\log n)$, the
   **impurity weight** $\omega(\tau):=\limsup_T T^{-2}\log(2+|S_T(\tau)|)$ and the **impurity spectrum**.
   **[THEOREM 152.2]** (unconditional, complete proof): for $\tau\ge1$,
   $\omega(\tau)=\max\bigl(0,\max_{j:\,|\gamma_j-\tau|<\delta_j}(\delta_j^2-(\gamma_j-\tau)^2)\bigr)$,
   where $(\delta_j,\gamma_j)$ range over the off quadruples of ζ; and at the exact height of a
   dominant quadruple the bias has **forced negative sign**:
   $S_T(\gamma_J)=-2\sqrt\pi\,m_J\,T\,e^{\delta_J^2T^2}(1+o(1))$. At frequency 0, $\omega(0)=\tfrac14$:
   **the pole is the weight-$\tfrac14$ impurity at frequency 0 — the diagonal mass**. Corollary:
   $\mathrm{RH}\iff\omega(\tau)=0$ for every $\tau\ge1$ ⟺ *the infinite interaction of the primes creates
   exactly one resonance: the pole*.

3. **(§2.4–2.5) The exact jurisdiction of $\Lambda\ge0$: the boundary, not an epsilon more.**
   **[PROPOSITION 152.4]**: $\Lambda\ge0\Rightarrow|S_T(\tau)|\le S_T(0)\asymp Te^{T^2/4}\Rightarrow
   \omega(\tau)\le\tfrac14$ for every $\tau$ — *nothing surpasses the diagonal* (the exact semi-global avatar of
   the local barrier $|c_m|\le2p^{m/2}$ and of the Mertens test of Doc 131). **[PROPOSITION 152.5]** (complete
   proof within the framework): with the Mertens inequality $3+4\cos\theta+\cos2\theta\ge0$, the equality
   $\omega=\tfrac14$ is realized only by the pole: there are no zeros with $\beta\ge1$. That is: **the
   positivity of von Mangoldt certifies exactly boundary purity (weight 0) and is exhausted there** —
   it reproduces de la Vallée Poussin and does not take a single step toward the center. Moreover
   **[PROPOSITION 152.7]**: every isolated prime and every finite set of primes is semi-globally pure
   ($\omega\equiv0$); impurity — including the pole — is an **irreducibly collective** phenomenon, consistent
   with B1–B4 of Doc 135 (the wall lives in the limit, not in any finite step).

4. **(§2.6) What D–H violates, visibly and maximally.** D–H has zeros with $\beta>1$ (Doc 146): its
   spectral impurity spectrum has weights $>\tfrac14$ — **it surpasses its own diagonal**, something no
   von Mangoldt datum $\ge0$ with abscissa 1 can feed (**[PROPOSITION 152.6]**). Semi-global purity of
   weight $\le\tfrac14$ is exactly the boundary that separates ζ (theorem, via $\Lambda\ge0$) from D–H
   (violated): the requested items (a)–(b) are satisfied. Item (c) — that $m<\infty$ should imply
   $m=0$ — is where the wall lies: §3.

5. **(§3) The attempt «$m<\infty+\Lambda\ge0+$FE $\Rightarrow m=0$» is carried out to the end and fails at a
   single, named point.** Step A [theorem]: under H(m), the dominant quadruple forces a negative exponential bias
   $S_T(\gamma_J)\sim-2\sqrt\pi m_JTe^{\delta_J^2T^2}$ — dominance over on-line zeros is achieved FULLY
   ($e^{\delta^2T^2}$ against $O(\log\gamma_J)$) and the sign is forced. Step B [proposition]: the only
   law with a sign that $\Lambda\ge0$ gives is $|S_T(\tau)|\le S_T(0)$. Step C [the clash]: the
   contradiction requires $\delta_J\ge\tfrac12$ — positivity refutes exactly the boundary, already excluded. The
   slack is $e^{-(1/4-\delta_J^2)T^2}$: **the whole world H(m) lives entirely within the Cauchy–Schwarz margin of
   boundary purity.** Failure located: **positivity is zero-frequency information; the off zero is an event at
   frequency $\gamma_J$; there is no bridge between frequencies without RH** (consistent with Calculation
   141.M4: Landau's lever vanishes on the line). The oscillation route (Ingham/Pintz) fails with an exact
   inversion: positivity does not prevent the oscillation of $\psi(x)-x$ — it is the **classical engine
   that proves it** (Landau's oscillation theorem, which REQUIRES an integrand of fixed sign); the
   missing complement (upper bound $|\psi(x)-x|=O(x^{1/2+\delta_J-\epsilon})$) is the negation of the
   hypothesis: structural circularity.

6. **(§3.6, §4) The minimal saving hypothesis, named and measured.** [NEW-DEFINITION 152.8] LP-152$(\tau_0)$:
   *$S_T(\tau_0)$ is subexponential in $T^2$*. By 152.2: LP-152$(\tau_0)$ ⟺ «no off quadruple with
   $|\gamma_j-\tau_0|<\delta_j$»; LP-152 at EVERY frequency ⟺ RH; under H(m) rigidity needs LP-152 only
   in the $m$ unknown windows. **[PROPOSITION 152.9]**: the Besicovitch mean in $\tau$ of
   $|S_T(\tau)|^2$ is $O(T^2)$ — the exponential frequencies, if they exist, have density ZERO in $\tau$:
   certifying LP-152 at the bad frequency is certifying an exceptional point invisible to every average —
   the master quantifier of P43, in the coordinate **dual** to that of LP-112 (Doc 112 Prop. 2.6).
   LP-112 (existential: produce ONE good $\tau$ from a density-zero set) and LP-152 (universal:
   exclude ONE bad frequency from a density-zero set) are the two arms —replica and evaluation—
   of the same pincer, incomparable with each other, both strictly weaker than RH as instances.

7. **VERDICT (§5): NEW REDUCTION + MAP-OF-THE-FAILURE.** There is no theorem
   «$m<\infty+\Lambda\ge0+$FE$\Rightarrow m=0$» and this document shows WHY this route cannot
   give it (three failure points F1–F3, §3). What does remain: the rigidity half now has a new,
   quantized, equivalent form — *under $m<\infty$, the impurity spectrum of ζ is a finite menu of
   parabolas with weights $\delta_j^2\in(0,\tfrac14)$ and forced negative sign; rigidity ⟺ the menu is
   empty* — and a dual target to LP-112 (LP-152) with its exceptionality certificate (152.9). The hierarchy of
   purities is now measured: boundary ($\omega\le\tfrac14$, theorem, cheap) ⊊ center ($\omega=0$, RH); $m<\infty$
   does not move $\omega$ by an epsilon (finiteness protects internal arguments, not external evaluators —
   Obs. 4.3 of D112, confirmed in the new coordinate).

---

## 1. The two purities and the weight discrepancy

### 1.1. Local purity (exact recall, Doc 131)

The Euler object of a prime $F_{p,\alpha}$ ($1<|\alpha|<p$; Doc 131 Prop. 6.6′) has divisor
$Z(\alpha)\sqcup Z(p/\bar\alpha)$ (two vertical progressions at $\mathrm{Re}=\log_p|\alpha|$ and
$1-\log_p|\alpha|$) and data $c_m=\alpha^m+(p/\bar\alpha)^m$. **Theorem 6.7** (local purity):

$$F_{p,\alpha}\ \text{satisfies H}\iff|\alpha|=\sqrt p\iff|c_m|\le2p^{m/2}\ \forall m\ge1.$$

Local Weil positivity is **decidable** and equivalent to the divisor falling at the center
$\mathrm{Re}=\tfrac12$. The mechanism of the negative direction is the two-bump Mertens test
(diagonal mass at $1$ against the coefficient at $p^M$ with an adversarial phase), with exact barrier
$|c_M|\le2p^{M/2}$ — Cauchy–Schwarz tight exactly in the pure case.

**Weight reading.** Call **purity of weight $w$** the case $|\alpha|=p^{w/2}$: the local divisor lives at
$\mathrm{Re}=\tfrac w2$ and (by $\sigma$-stability, via the pair $p/\bar\alpha$) at $\mathrm{Re}=1-\tfrac w2$.
For $w=1$ the two lines coincide at the **center** $\tfrac12$: the divisor is pointwise $\sigma$-fixed
(self-dual). For $w=0$ they are the **boundary** $\{0,1\}$: a $\sigma$-free orbit. Theorem 6.7 is the case
$w=1$; the objects of the two-prime theorem (Doc 135, Theorem A) are pure of weight 1.

### 1.2. The factor of ζ is pure of weight 0 and impure of weight 1 — the discrepancy

The local datum of ζ is $a(p^m)=\Lambda(p^m)=\log p$; the local factor is $(1-p^{-s})^{-1}$, i.e.
$\alpha=1$. Exact facts (Doc 135 §7.2 B3; Doc 137 boundary audit):

- $|\alpha|=1=p^{0/2}$: the factor of ζ is **pure of weight 0**. Its local divisor (the lattice
  $Z(1)\sqcup Z(p)$) lives at $\mathrm{Re}\in\{0,1\}$ — the boundary of the strip, a free orbit of
  $\sigma:s\mapsto1-\bar s$.
- Read in the weight-1 normalization of Doc 131, $c_m=1+p^m$ and $1+p^m>2p^{m/2}$ for every $m\ge1$
  (strict AM–GM): **maximal violation of the weight-1 Ramanujan barrier**. The boundary $|\alpha|=1$ was
  audited in Doc 137: the two-bump test kills H there too ($\delta'=\pm\tfrac12$ after the swap). **Each
  factor of ζ, in isolation, violates weight-1 Weil positivity.**
- The pure objects of the program (two primes, $n$ primes: Doc 135) have a *constructive* arithmetic
  term; ζ lives in the *destructive* regime ($a=\Lambda\ge0$ subtracting against the polar block). The
  constructive/destructive mismatch is the shadow of the weight mismatch (B3).

**The discrepancy, in one statement.** The functional equation of ζ performs the recentering $0\to\tfrac12$ on
the **archimedean weights** (the pole $[0]+[1]$, the gamma factor, the swap
$\theta(y)\leftrightarrow\Omega(t)$ of B1) — that is why the GLOBAL divisor is $\sigma$-stable with respect to
the center. But $\sigma$-stable is not $\sigma$-fixed: the functional equation pairs $\rho$ with $1-\bar\rho$,
it does not force $\rho=1-\bar\rho$. **RH is the recentering of the ZEROS: that the global divisor, built from
local data pure of weight 0 (boundary), be pure of weight 1 (center). That is the piece the functional
equation does not do and that no local purity can do (the factors are individually impure of
weight 1).** "Global purity" $m=0$ is not the aggregation of local purities: it is a property of the
**interaction** — exactly the intuition that the semi-global purity of §2 formalizes.

### 1.3. What boundary purity certifies globally

Weight-0 purity of the factors has a classical, unconditional global manifestation: ζ does not vanish
on $\mathrm{Re}\,s\ge1$ (Euler for $\sigma>1$; de la Vallée Poussin/Mertens for $\sigma=1$ [dVP96],
[Mer98]), and by the functional equation also not on $\mathrm{Re}\,s\le0$ (except trivial zeros). That is: **the
global zeros are repelled from the boundary — the position of the local divisor pure of weight 0.** Section
§2.4–2.5 will show that this is EXACTLY what the positivity $\Lambda\ge0$ certifies within the
semi-global framework ($\omega\le\tfrac14$, with equality only at the pole), and that it is exhausted there. The
purity table of the program is:

| purity | statement | divisor position | status |
|---|---|---|---|
| local weight 0 | $\vert\alpha_p\vert=1$ for each $p$ | local boundary $\{0,1\}$ | **trivially true for ζ** |
| boundary (global) | no zeros in $\mathrm{Re}\ge1$ ∪ $\mathrm{Re}\le0$ | boundary repulsion | **theorem** (dVP; §2.5 within the framework) |
| semi-global | $\omega(\tau)=0$ $\forall\tau\ge1$ (§2) | no resonances except the pole | **⟺ RH** (Cor. 152.3) |
| global weight 1 | $m=0$: divisor $\sigma$-fixed (center) | center $\tfrac12$ | RH |

---

## 2. Semi-global purity: the definition and the impurity spectrum theorem

### 2.1. The definition

**[NEW-DEFINITION 152.1] (Gaussian correlation, impurity weight, impurity spectrum).** For
$\tau\in\mathbb R$ and $T\ge1$:
$$S_T(\tau)\;:=\;\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,e^{-(\log n)^2/4T^2}\,\cos(\tau\log n)$$
(absolutely convergent: the Gaussian kills the tail). The **impurity weight** at frequency $\tau$:
$$\omega(\tau)\;:=\;\limsup_{T\to\infty}\;\frac{\log\bigl(2+|S_T(\tau)|\bigr)}{T^2}\;\in\;[0,\infty],$$
and the **impurity spectrum** $\Sigma_{\mathrm{imp}}:=\{\tau\ge0:\omega(\tau)>0\}$. I say ζ is
**semi-globally pure at $\tau$** (PSG$(\tau)$) if $\omega(\tau)=0$, i.e. if the primes hide no
exponential correlation (in $T^2$) with the phase $\cos(\tau\log n)$ at Gaussian scale $T$.

**Why this is the notion of "purity of the interaction".** $S_T(\tau)$ involves ALL primes at
once: it is the Fourier transform (in $\tau$) of the positive measure
$\sum_n\Lambda(n)n^{-1/2}e^{-(\log n)^2/4T^2}\delta_{\log n}$ — the full von Mangoldt datum, weighted
on the critical line. Prop. 152.7 will show that no isolated prime nor finite set of primes can
produce $\omega>0$: semi-global impurity, if it exists, is a phenomenon of the infinite interaction.
The definition is the exact global avatar of the local datum of Doc 131: there
the impurity of $F_{p,\alpha}$ is detected in the coefficients $c_m$ at support $m\gtrsim1/\delta'$ (barrier
$|c_m|\le2p^{m/2}$, dictionary M3 of D134 §5.8); here it is detected in $S_T(\tau)$ at support $T\gtrsim1/\delta$
(Cor. 152.3(iii)).

### 2.2. The impurity spectrum theorem

**Explicit-formula convention.** I use the Weil–Guinand explicit formula in the normalization of
[IK04, Thm. 5.12] for ζ: for $h$ even, holomorphic on $|\mathrm{Im}\,t|\le\tfrac12+\epsilon$, with
decay $h(t)\ll(1+|t|)^{-2-\epsilon}$ in the strip,
$$\sum_{\rho}h(t_\rho)\;=\;h\bigl(\tfrac i2\bigr)+h\bigl(-\tfrac i2\bigr)
+\frac1{2\pi}\int_{\mathbb R}h(t)\,\Omega_\infty(t)\,dt
-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,g(\log n),$$
where $\rho=\beta+i\gamma$ ranges over the nontrivial zeros, $t_\rho:=(\rho-\tfrac12)/i$ (so that
$\rho=\tfrac12+\delta+i\gamma\mapsto t_\rho=\gamma-i\delta$), $g(u)=\tfrac1{2\pi}\int h(t)e^{-iut}dt$, and
$\Omega_\infty(t)=\mathrm{Re}\,\frac{\Gamma'}{\Gamma}(\tfrac14+\tfrac{it}2)-\log\pi=O(\log(2+|t|))$.
[Absolute constants are carried symbolically; what is load-bearing in the theorem —exponential
rates and signs— is robust against the convention.]

**Gaussian test.** $h_{T,\tau}(t):=e^{-T^2(t-\tau)^2}+e^{-T^2(t+\tau)^2}$ (even, entire; on
$|\mathrm{Im}\,t|\le1$, $|h|\le e^{T^2}\bigl(e^{-T^2(\mathrm{Re}\,t-\tau)^2}+e^{-T^2(\mathrm{Re}\,t+\tau)^2}\bigr)$:
admissible with margin). Its transform: $g(u)=\frac1{\sqrt\pi\,T}e^{-u^2/4T^2}\cos(\tau u)$. The formula
becomes, exactly:
$$\boxed{\;\frac{2}{\sqrt\pi\,T}\,S_T(\tau)\;=\;-\sum_\rho h_{T,\tau}(t_\rho)\;+\;4\,e^{T^2(\frac14-\tau^2)}\cos(\tau T^2)\;+\;A_T(\tau),\;}\tag{152.E}$$
with $A_T(\tau)=\frac1{2\pi}\int h_{T,\tau}\,\Omega_\infty=O\bigl(T^{-1}\log(2+\tau)\bigr)$
(since $\int h=2\sqrt\pi/T$ and $\log(2+|s\pm\tau|)\le\log(2+\tau)+\log(2+|s|)$ under the Gaussian), and where the
pole term was computed in closed form:
$h(\pm\tfrac i2)$ sums to $4e^{T^2(\frac14-\tau^2)}\cos(\tau T^2)$ (direct computation of
$(\tfrac i2\mp\tau)^2=-\tfrac14\mp i\tau+\tau^2$).

**[THEOREM 152.2] (impurity spectrum of ζ; unconditional).** Let
$\{(\delta_j,\gamma_j)\}_{j\in J}$ be the (finite or infinite) list of off quadruples of ζ
($\delta_j\in(0,\tfrac12)$, $\gamma_j>14$), with multiplicities $m_j$. Then:

**(a) (exact weight formula).** For every $\tau\ge1$:
$$\omega(\tau)\;=\;\max\Bigl(0,\;\max_{j:\,|\gamma_j-\tau|<\delta_j}\bigl(\delta_j^2-(\gamma_j-\tau)^2\bigr)\Bigr),$$
where the inner maximum ranges over a FINITE set (the quadruples with $|\gamma_j-\tau|<\delta_j\le\tfrac12$).
In particular $\Sigma_{\mathrm{imp}}\cap[1,\infty)=\bigcup_j(\gamma_j-\delta_j,\gamma_j+\delta_j)$, a
union of "parabolic caps" centered at the off heights with peak weights $\delta_j^2$.

**(b) (forced sign at the exact height).** If $m\ge1$ and $J^*$ is the set of quadruples with
$\delta_j=\delta_{\max}:=\max_j\delta_j$ (maximum attained: trivially under $m<\infty$; in general, the
quadruples with $|\gamma_j-\tau|<\delta_j$ for fixed $\tau$ are finitely many and the local maximum suffices),
and $\gamma_J$ is the height of one of them with total multiplicity $m_J$ in $(\delta_{\max},\gamma_J)$,
then
$$S_T(\gamma_J)\;=\;-\,2\sqrt\pi\;m_J\;T\;e^{\delta_{\max}^2T^2}\,\bigl(1+o(1)\bigr)\qquad(T\to\infty).$$
The bias is **permanently negative** (with no free phase): the whole quadruple anti-correlates the primes
with $\cos(\gamma_J\log n)$.

**(c) (purity under RH; the pole).** If $m=0$, then $S_T(\tau)=O\bigl(T\log(2+\tau)\bigr)$ for every
$\tau\ge1$: $\omega\equiv0$ on $[1,\infty)$. Unconditionally, $\omega(0)=\tfrac14$ with
$S_T(0)=2\sqrt\pi\,T\,e^{T^2/4}(1+o(1))$: **the pole is the weight-$\tfrac14$ impurity at frequency 0.**

*Proof.* Everything follows from (152.E) by evaluating each block.

*(i) Pole block.* $\bigl|4e^{T^2(\frac14-\tau^2)}\cos(\tau T^2)\bigr|\le4e^{-T^2(\tau^2-\frac14)}=o(1)$
for $\tau\ge1$. For $\tau=0$: $h_{T,0}(t)=2e^{-T^2t^2}$ and the pole term is $4e^{T^2/4}$, dominant
(below).

*(ii) On-line zeros.* For $\rho=\tfrac12+i\gamma$: $h_{T,\tau}(\gamma)\in(0,2]$. By Riemann–von Mangoldt,
the number of zeros with $|\gamma-\tau|\in[k,k+1)$ is $O(\log(2+\tau+k))$; hence
$$0\;\le\;\sum_{\gamma\ \mathrm{on}}h_{T,\tau}(\gamma)\;\le\;C\sum_{k\ge0}e^{-T^2k^2}\log(2+\tau+k)\;\le\;C'\log(2+\tau)\qquad(T\ge1).$$

*(iii) Off quadruples.* The quadruple $(\delta_j,\gamma_j)$ contributes the four points
$t=\pm\gamma_j\mp i\delta_j$. Since $h$ is even with real coefficients,
$$X_j:=\sum_{\mathrm{quadruple}}h_{T,\tau}(t)\;=\;4\,\mathrm{Re}\,e^{-T^2(\gamma_j-\tau-i\delta_j)^2}\;+\;4\,\mathrm{Re}\,e^{-T^2(\gamma_j+\tau-i\delta_j)^2}.$$
Computing the exponent: $-T^2[(\gamma_j-\tau)^2-\delta_j^2-2i(\gamma_j-\tau)\delta_j]$, hence
$$\mathrm{Re}\,e^{-T^2(\gamma_j-\tau-i\delta_j)^2}\;=\;e^{T^2(\delta_j^2-(\gamma_j-\tau)^2)}\,\cos\bigl(2T^2(\gamma_j-\tau)\delta_j\bigr),$$
and the mirror term has rate $\delta_j^2-(\gamma_j+\tau)^2<0$ for $\tau,\gamma_j>0$ (negligible).
**Upper bound:** grouping by $|\gamma_j-\tau|\in[k,k+1)$ and using $\delta_j\le\tfrac12$,
$$\Bigl|\sum_jX_j\Bigr|\;\le\;8\!\!\sum_{j:|\gamma_j-\tau|<1}\!\!e^{T^2(\delta_j^2-(\gamma_j-\tau)^2)}\;+\;C\log(2+\tau)\sum_{k\ge1}e^{-T^2(k^2-\frac14)}\;\le\;C''\log(2+\tau)\,e^{T^2\,r(\tau)},$$
with $r(\tau):=\max\bigl(0,\max_{|\gamma_j-\tau|<\delta_j}(\delta_j^2-(\gamma_j-\tau)^2)\bigr)$ (the $j$ with
$|\gamma_j-\tau|<1$ number $O(\log(2+\tau))$, finitely many). Inserting (i)–(iii) into (152.E):
$|S_T(\tau)|\le CT\log(2+\tau)\,e^{T^2r(\tau)}$, whence $\omega(\tau)\le r(\tau)$. This proves "≤" in (a)
and proves (c) ($m=0\Rightarrow r\equiv0$ for $\tau\ge1$; and $S_T(0)$: in (152.E) with $\tau=0$ the pole gives
$4e^{T^2/4}$, the zeros contribute $O(1)$ —every zero has $|\gamma|>14$, so $h_{T,0}(t_\rho)$ is
$O(e^{-T^2(14^2-1/4)})$—, thus $S_T(0)=\frac{\sqrt\pi T}2\cdot4e^{T^2/4}(1+o(1))$; this matches the
direct saddle-point computation $\sum\Lambda(n)n^{-1/2}e^{-u^2/4T^2}\approx\int_0^\infty e^{u/2-u^2/4T^2}du=2\sqrt\pi Te^{T^2/4}(1+o(1))$,
consistency check ✓).

**Lower bound of (a) and (b) — the no-cancellation lemma.** Let $\tau\ge1$ with $r(\tau)>0$ and let
$a_{\max}=r(\tau)$ be the maximal rate, attained by a finite set $I$ of quadruples (window
$|\gamma_j-\tau|<\delta_j$, finite). The terms of rate $a_{\max}$ in $-\sum_\rho h$ are
$$f(T^2),\qquad f(x):=-\sum_{i\in I}4m_i\cos(b_ix),\qquad b_i:=2(\gamma_i-\tau)\delta_i,$$
**all with coefficients of the same sign** (negative) and zero phase. The function $f$ is a nonzero real
trigonometric polynomial: its Besicovitch mean square is
$M(f^2)=8\sum_{b}\bigl(\sum_{i:b_i=b}m_i\bigr)^2>0$ (equal frequencies sum coherently — same
sign—; distinct frequencies are orthogonal on average; the case $b_i=0$, i.e. $\gamma_i=\tau$, gives a
constant negative term, even better). Hence there exists $c>0$ and a set of $x$ of positive density with
$|f(x)|\ge c$; along a sequence $T_n\to\infty$ with $T_n^2$ in that set,
$$|S_{T_n}(\tau)|\;\ge\;\frac{\sqrt\pi T_n}2\Bigl[c\,e^{a_{\max}T_n^2}-C\log(2+\tau)\,e^{(a_{\max}-\eta)T_n^2}-C\log(2+\tau)\Bigr]\;\ge\;c'\,T_n\,e^{a_{\max}T_n^2},$$
where $\eta>0$ is the gap between $a_{\max}$ and the next rate (finitely many rates in the window; the rates of
the pole and of the mirrors are $\le\tfrac14-\tau^2<0$ for $\tau\ge1$). Hence $\omega(\tau)\ge a_{\max}$:
equality in (a). For (b): at $\tau=\gamma_J$ with $\delta_J=\delta_{\max}$, the set of maximal rate is
exactly that of the quadruples at $(\delta_{\max},\gamma_J)$ (any other $j$ has
$\delta_j^2-(\gamma_j-\gamma_J)^2<\delta_{\max}^2$, strictly: either $\delta_j<\delta_{\max}$, or
$\gamma_j\ne\gamma_J$ with fixed separation), its frequency is $b=0$ and its contribution is the CONSTANT
$-4m_J e^{\delta_{\max}^2T^2}$: no oscillation, no subsequence —
$S_T(\gamma_J)=-\frac{\sqrt\pi T}2\cdot4m_Je^{\delta_{\max}^2T^2}(1+o(1))$, a full limit, permanent negative
sign. $\square$

**Remark 152.2bis (what the $o(1)$ of (b) exactly is).** The absorbed terms: other quadruples
(strictly smaller rate, fixed gap of the world H(m) — the frozen constants of D112 §1.2 (F1)), on-line
zeros ($O(\log\gamma_J)$, no exponential), pole ($e^{-T^2(\gamma_J^2-1/4)}$, negligible for
$\gamma_J>14$), archimedean ($O(T^{-1}\log\gamma_J)$). **Dominance of the off term over the on-line
density is achieved completely** — the fear that zeros on the line would drown out the signal was unfounded;
what is NOT achieved is turning dominance into a contradiction (§3).

### 2.3. Corollaries: equivalence, quantization, dictionary

**[COROLLARY 152.3].**

**(i) (semi-global purity ⟺ RH).** $\mathrm{RH}\iff\omega(\tau)=0$ for every $\tau\ge1$
$\iff\Sigma_{\mathrm{imp}}=\{0\}$ (with $\omega(0)=\tfrac14$, the pole). In words: *RH says that the
infinite interaction of the primes produces exactly one exponential resonance: the diagonal (the pole).
Every additional resonance is an off quadruple and vice versa, with exact dictionary
(position, weight) = (height, $\delta^2$).*

**(ii) (quantized dichotomy).** For each fixed $\tau\ge1$: either $S_T(\tau)=O(T\log(2+\tau))$
(polynomial), or $|S_T(\tau)|=e^{(\omega(\tau)+o(1))T^2}$ along a sequence, with
$\omega(\tau)$ taken from the menu $\{\delta_j^2-(\gamma_j-\tau)^2\}$ — **there are no intermediate growth
rates** (e.g. $e^{cT}$ is impossible). Under H(m), the menu is finite and the peaks are
$\delta_1^2,\dots,\delta_m^2\in(0,\tfrac14)$: impurity is **quantized** by the distances of the
zeros to the line.

**(iii) (the impurity↔resolution dictionary, now a global theorem).** The cap of the quadruple
$(\delta,\gamma)$ is invisible in $S_T$ while $\delta^2T^2\lesssim\log(T\log\gamma)$ and dominates when
$\delta^2T^2\gg\log(T\log\gamma)$: the detection threshold is $T\asymp\delta^{-1}$ modulo polylogarithmic
factors. This is dictionary M3 of D134 §5.8 ("off zero at distance $\delta$ ⟷ detectable impurity
at support $\asymp1/\delta$"), previously calibrated in the local world $F_{p,\alpha}$, now **proved for ζ at
the global level** (via 152.2).

*Proof.* (i): "⟸" if there is a quadruple $(\delta^*,\gamma^*)$, by 152.2(a) $\omega(\gamma^*)\ge\delta^{*2}>0$.
"⟹" is 152.2(c). (ii): a direct reading of the proof of 152.2 (the only rates available in (152.E) are
those of the menu; if all are $\le0$, each block is at most $O(T\log)$). (iii): comparison of
$T e^{\delta^2T^2}$ against $T\log\gamma$. $\square$

### 2.4. The positivity barrier: the only law with a sign

**[PROPOSITION 152.4] (nothing surpasses the diagonal).** Unconditionally, from $\Lambda(n)\ge0$:
$$|S_T(\tau)|\;\le\;S_T(0)\;=\;2\sqrt\pi\,T\,e^{T^2/4}\,(1+o(1))\qquad\forall\tau\in\mathbb R,$$
and hence $\omega(\tau)\le\tfrac14$ for every $\tau$. Equivalently (via 152.2(a)): all zeros
lie in the closed band $0\le\beta\le1$.

*Proof.* $|\cos(\tau\log n)|\le1$ and all terms of $S_T(0)$ are $\ge0$: the inequality is
term by term. The size of $S_T(0)$: Chebyshev bound $\psi(x)\asymp x$ (unconditional) plus a Gaussian
saddle point, or directly 152.2(c). The spectral reading: if there were a zero with $\delta>\tfrac12$
(i.e. $\beta>1$), 152.2(b) would give $|S_T(\gamma_J)|\sim2\sqrt\pi m_JTe^{\delta^2T^2}>S_T(0)$ for
large $T$: contradiction. $\square$

**Structural reading (the exact avatar of the local world).** The barrier $|S_T(\tau)|\le S_T(0)$ is the
semi-global version of the local barrier $|c_m|\le2p^{m/2}$ of Theorem 6.7 of D131 — "coefficient bounded
by diagonal", arithmetic Cauchy–Schwarz — and of the diagonal-mass mechanism of Prop. 6.5 of D131. The
global diagonal mass is the pole ($\omega(0)=\tfrac14$); positivity says no frequency can resonate
stronger than the diagonal. **And that is exactly the boundary purity of §1.3:**
$\omega\le\tfrac14$ ⟺ closed band.

### 2.5. Mertens at the boundary: positivity is exhausted exactly there

**[PROPOSITION 152.5] (strict boundary within the framework).** $\omega(\tau)=\tfrac14$ is impossible for
$\tau\ge1$: there are no zeros with $\beta=1$ (nor, by 152.4, with $\beta>1$). Von Mangoldt positivity,
executed to the maximum (Mertens inequality), certifies the **open band** and nothing more.

*Proof.* Suppose a zero with $\delta_J=\tfrac12$ (i.e. $\beta=1$) at height $\gamma_J\ge14$, with
multiplicity $m_J\ge1$; by 152.4, $\delta_{\max}=\tfrac12$. From $\Lambda(n)\ge0$ and
$3+4\cos\theta+\cos2\theta=2(1+\cos\theta)^2\ge0$ with $\theta=\gamma_J\log n$, term by term:
$$3\,S_T(0)\;+\;4\,S_T(\gamma_J)\;+\;S_T(2\gamma_J)\;\ge\;0.$$
By 152.2(b)(c): $S_T(0)=2\sqrt\pi Te^{T^2/4}(1+o(1))$ and $S_T(\gamma_J)=-2\sqrt\pi m_JTe^{T^2/4}(1+o(1))$.
Hence
$$S_T(2\gamma_J)\;\ge\;(8m_J-6)\sqrt\pi\,T\,e^{T^2/4}\,(1+o(1))\;\ge\;2\sqrt\pi\,T\,e^{T^2/4}\,(1+o(1)),$$
a POSITIVE bias of rate $\tfrac14$ at frequency $2\gamma_J\ne0$. But by (152.E) at
$\tau=2\gamma_J$: the pole contributes $O(e^{-T^2(4\gamma_J^2-1/4)})$ (nothing); the on-line zeros contribute to $S_T$
at most $O(T\log\gamma_J)$; and the off caps at $2\gamma_J$ have rate
$\delta_j^2-(\gamma_j-2\gamma_J)^2\le\tfrac14$, with equality ONLY if $\delta_j=\tfrac12$ and
$\gamma_j=2\gamma_J$ exactly — in which case its contribution to $S_T(2\gamma_J)$ is, by 152.2(b),
**negative** ($-2\sqrt\pi m'Te^{T^2/4}$), not positive. That is: a positive bias of rate $\tfrac14$ at a
nonzero frequency has no producer in (152.E) — the only positive term of rate $\tfrac14$ in the
formula is the pole, which lives at frequency 0. Contradiction. $\square$

**Remarks.** (i) This reproduces, within the framework, the classical theorem $\zeta(1+i\gamma)\ne0$ [dVP96],
[Mer98] — it is not new as a fact; it is new as a **measurement of jurisdiction**: the 3-4-1 mechanism (the
two-bump test of D131 §6.5, in its global version: frequencies $0,\gamma_J,2\gamma_J$ against the diagonal
mass) is ALL that $\Lambda\ge0$ knows how to do, and it reaches exactly to the boundary. (ii) The
classical refinement $\beta\le1-c/\log\gamma$ (de la Vallée Poussin) comes from the same mechanism competing
against the archimedean term at finite $T$ calibrated with $\log\gamma$; the **calendar** $1/\log\gamma$
of boundary repulsion is the same scale as the natural calendar of LP-134/LP-141 (Docs 141/144) —
but measured from the boundary $\mathrm{Re}=1$, not from the center. I do not re-derive it (classical, cited); I
record it because it exhibits the symmetry: **boundary repulsion at log calendar = theorem (positivity);
center repulsion at log calendar = LP-134/141, non-analytic and open.** (iii) After 152.4+152.5,
positivity is EXHAUSTED: $\omega(\tau)<\tfrac14$ strict, with no information about $\omega\in(0,\tfrac14)$
— the zone where H(m) lives.

### 2.6. Impurity is irreducibly collective

**[PROPOSITION 152.7] (each prime is semi-globally pure; finite truncations too).** For
any finite set $P$ of primes, the partial sum
$S^{(P)}_T(\tau):=\sum_{p\in P}\sum_{k\ge1}(\log p)\,p^{-k/2}e^{-(k\log p)^2/4T^2}\cos(\tau k\log p)$
satisfies $|S^{(P)}_T(\tau)|\le\sum_{p\in P}\frac{\log p}{\sqrt p-1}=O_P(1)$, uniform in $T$ and $\tau$:
$\omega^{(P)}\equiv0$, **including frequency 0**.

*Proof.* Trivial bound: Gaussian and cosine $\le1$, geometric series in $k$. $\square$

**Reading.** Neither the pole ($\omega(0)=\tfrac14$) nor any hypothetical impurity at $\tau>0$ is visible in
any finite stretch of primes: both are phenomena of the LIMIT — the Chebyshev mass emerging from the
infinite tail. Consistent, and now quantitatively aligned, with B1–B4 of Doc 135 (positivity passes to the
limit; spectrality does not; all the difficulty lies in the limit, not in any finite step) and with the
two-prime theorem (Doc 135, Theorem A: cross terms = 0 — in the pure finite world there is no interaction that
could resonate). **Semi-global purity is, literally, purity of the infinite interaction: the object that
decides it is neither a local nor a finite semilocal datum.**

### 2.7. Davenport–Heilbronn violates semi-global purity, visibly and maximally

**[PROPOSITION 152.6] (the violation by D–H surpasses the ceiling of positivity).**

(a) If $F$ is any function such that $-F'/F$ admits a Dirichlet expansion
$\sum_n\Lambda_F(n)n^{-s}$ with $\Lambda_F(n)\ge0$ and $\sum_n\Lambda_F(n)n^{-\sigma}<\infty$ for every
$\sigma>1$ (normalization $F\to1$ as $\sigma\to+\infty$), then $F$ does not vanish on $\sigma>1$.

(b) The Davenport–Heilbronn function $f$ has infinitely many zeros with $\beta>1$ ([DH36]; Doc 146, Fact
146.4, verified). By (a), **$f$ admits no positive von Mangoldt datum with abscissa 1**. In the
language of the framework: the spectral analogue of its impurity weight at the heights of those zeros is
$\delta^2>\tfrac14$ — D–H **surpasses the ceiling $\tfrac14$ that no object with a positive datum can
surpass** (152.4).

*Proof.* (a) For $\sigma\ge\sigma_0$ large, $\log F(s)=\sum_n\frac{\Lambda_F(n)}{\log n}n^{-s}$
(term-by-term integration, legitimate by absolute convergence); the series on the right converges
absolutely for every $\sigma>1$, defining $G$ holomorphic on $\sigma>1$ with $e^G=F$ for
$\sigma\ge\sigma_0$; by analytic continuation $e^G=F$ on $\sigma>1$ and $F=e^G\ne0$ there. (b) [DH36] +
(a), contrapositive. The spectral reading of the weight: the cap of a zero with $\delta>\tfrac12$ has
peak $\delta^2>\tfrac14$ (block (iii) of the proof of 152.2 is a computation on the zero side and
applies to any given divisor; for D–H I do not claim the identity (152.E) — which would require ITS
explicit formula — only the reading of the divisor). $\square$

**The balance of (a)–(b)–(c).** (a) D–H violates semi-global purity **visibly**: its zeros
with $\beta>1$ are violations of weight $>\tfrac14$, impossible for any positive datum — the crudest
form of "interaction purity" ($\Lambda\ge0$) already separates, and the separation is the one Doc 146
asked for (positivity of the prime term is the one thing D–H lacks). (b) ζ satisfies **by theorem**
semi-global purity of weight $\le\tfrac14$ with strict boundary (152.4+152.5), because $\Lambda\ge0$.
(c) But the purity rigidity needs is $\omega\equiv0$ ($\tau\ge1$), which by Corollary 152.3(i)
**is RH**: the interval $(0,\tfrac14)$ of impurity weights is exactly the space of worlds H(m). The
question is reduced to its exact form: can $m<\infty$ close the interval
$(0,\tfrac14)$? Section §3 carries out the attempt and locates the failure.

---

## 3. The attempt «m<∞ + Λ≥0 + functional equation ⟹ m=0», step by step

Working hypothesis H(m) (Doc 112 §1.1): ζ has exactly $m$ off quadruples, $0<m<\infty$,
$\{\tfrac12\pm\delta_j\pm i\gamma_j\}_{j\le m}$, frozen parameters (F1 of D112): $\delta_{\max}>0$,
fixed heights. Goal: contradiction. Each step carries a label.

### 3.1. Step A [THEOREM — instance of 152.2(b)]: the forced exponential bias

Under H(m), with $J$ the dominant quadruple ($\delta_J=\delta_{\max}$, height $\gamma_J$, multiplicity
$m_J$):
$$S_T(\gamma_J)\;=\;-\,2\sqrt\pi\,m_J\,T\,e^{\delta_{\max}^2T^2}\,(1+o(1))\;\longrightarrow\;-\infty.$$
Three features, all proved: (i) **total dominance**: the off term exceeds the on-line zeros
($O(\log\gamma_J)$, no exponential), the pole, and the archimedean term — the initial hope ("the off
term dominates the on-line density in long tests") is REALIZED completely; (ii) **forced sign**: the
functional equation + reality on the axis turn the quadruple into a zero-phase signal — the four
zeros push in the SAME direction, pure anti-correlation of the primes with $\cos(\gamma_J\log n)$, with no
free phase that could rotate the bias; (iii) **frozen constants**: the visibility threshold
$T\gtrsim1/\delta_{\max}$ is a fixed number of the world H(m) — no internal uniformity issue.

### 3.2. Step B [PROPOSITION — 152.4/152.5]: the only available law with a sign

What signed bound does the prime side have? Positivity $\Lambda\ge0$ produces exactly
$$|S_T(\tau)|\;\le\;S_T(0)\;=\;2\sqrt\pi\,T\,e^{T^2/4}(1+o(1)),\qquad\text{plus the Mertens improvement at the edge,}$$
and nothing more. In particular, **the prime side does NOT "have a sign" against the test that detects
$\gamma_J$**: the test $\cos(\gamma_J\log n)$ oscillates, and $\Lambda\ge0$ only gives a sign against
non-negative tests ($g\ge0\Rightarrow\sum_n\Lambda(n)n^{-1/2}g(\log n)\ge0$), whose spectral content
concentrates at $t\approx0$ and does not see the height $\gamma_J>14$. This is the point that was
sought: **von Mangoldt positivity is zero-frequency information.** It is also the frequency-domain
version of Calculation 141.M4 (Doc 141): Landau's positivity lever, which at $s=1$ gives
Deuring–Heilbronn, is identically zero on the critical line.

### 3.3. Step C [the clash]: where the contradiction dies — GAP-152.A

Combining A and B: the contradiction $|S_T(\gamma_J)|>S_T(0)$ requires
$$e^{\delta_{\max}^2T^2}\;>\;e^{T^2/4}\qquad\Longleftrightarrow\qquad\delta_{\max}\;\ge\;\tfrac12\;\Longleftrightarrow\;\beta\ge1.$$
Positivity refutes exactly the zeros at/beyond the boundary — which are ALREADY excluded (152.5 = dVP).
For $\delta_{\max}<\tfrac12$, the required bias is a factor $e^{-(1/4-\delta_{\max}^2)T^2}$ SMALLER
than the total available mass: **the world H(m) lives entirely within the Cauchy–Schwarz margin of
boundary purity.** There is no contradiction; identity (152.E) is satisfied identically with the
bias included — the tautology of the explicit formula (Doc 112, Prop. 4.2) reappears intact in
frequency coordinates: the formula does not overdetermine; the only non-tautological content is the sign, and
the available sign (Step B) is exhausted at the boundary.

**[GAP-152.A] (the missing link, named).** An unconditional bound
$$|S_T(\tau_0)|\;=\;O_{\epsilon,\tau_0}\!\bigl(e^{\epsilon T^2}\bigr)\quad\forall\epsilon>0,\qquad\text{for some }\tau_0\in(\gamma_J-\delta_J,\;\gamma_J+\delta_J),$$
i.e. subexponentiality of the prime correlation at ONE frequency. By 152.2(a) this is equivalent to
«no off quadruple whose window covers $\tau_0$» — the desired conclusion, by frequency. Step C cannot
close without GAP-152.A, and GAP-152.A at the bad frequency IS (a local instance of) what is to be
proved. **Circularity located precisely: the attempt turns «there is no quadruple
$(\delta_J,\gamma_J)$» into «there is no exponential correlation at $\gamma_J$», which is the same statement under
exact dictionary 152.2.** The value of the dictionary is not nil (§4); the direct path does not close.

### 3.4. The oscillation route (Ingham/Pintz) and its exact inversion

Idea (2): an off zero forces oscillation of $\psi(x)-x$ of growing amplitude; does
$m<\infty$ make the oscillation "non-cancelable", contradicting something? Honest inventory:

- **[Classical datum, verified qualitatively].** If ζ has a zero $\rho_0=\beta_0+i\gamma_0$,
  then $\psi(x)-x=\Omega_\pm(x^{\beta_0-\epsilon})$; finer forms give two-sided oscillation of
  size comparable to $x^{\beta_0}/|\rho_0|$ (E. Schmidt [Sch03] for $\Omega_\pm(x^{1/2})$; Ingham
  [Ing36] and [Ing32, Ch. V] for the version with a hypothetical zero; Pintz [Pin80] for effective,
  localized versions). **[literature GAP]:** exact constants and forms of [Ing36]/[Pin80] not verified at
  page level this session; I use ONLY the qualitative content "the oscillation genuinely occurs", which
  is not a premise of any [THEOREM] of this document.
- **The mechanism of those theorems is Landau's oscillation theorem** (an integrand of eventually
  ONE sign forces the abscissa of convergence to be a real singularity; [Ing32, Ch. V]): it applies to
  $\psi(x)-x$ **using $\Lambda\ge0$**.

**The inversion.** The naive hope was: "$\Lambda\ge0$ gives a sign to the prime side, and the oscillating
term $x^{1/2+\delta_J}\cos(\gamma_J\log x+\phi)$ of the off zero contradicts that sign". It is exactly
the reverse: **positivity is the engine that PROVES the oscillation of the off zero is realized** (Landau
needs an integrand of one sign). Positivity and oscillation of $\psi(x)-x$ do not clash: they cooperate. $\psi$
is non-decreasing (positivity), but the oscillating terms are $o(x)$ and monotonicity does not see them;
$\psi(x)-x$ is a difference and oscillates freely.

**Where a contradiction would fail and what would save it.** A contradiction via oscillations needs a
PAIR: (forced oscillation $\ge X$) ∧ (upper bound $<X$). The lower half exists (Landau/Ingham, via
positivity). The missing upper half would be $|\psi(x)-x|=O(x^{1/2+\delta_{\max}-\epsilon})$ — which is
**the negation of H(m)** (that bound eliminates the dominant quadruple): the route is structurally circular,
not missing an estimate. $m<\infty$ does not supply the upper half: under H(m), $\psi(x)-x$ genuinely
has the terms $x^{1/2+\delta_j}$ and no better bound is true IN that world. **The
minimal hypothesis that would save the oscillation route is the negation of the hypothesis: zero value as
route.** (This confirms, by a third independent coordinate, Obs. 4.3 of D112: finiteness protects
arguments internal to the world, not external evaluators.)

### 3.5. What m<∞ genuinely buys, and what it does not

**Buys (proved):**
1. **Finite, quantized menu** (Cor. 152.3(ii)): the impurity spectrum is a FINITE union of
   caps with peaks $\delta_1^2,\dots,\delta_m^2$ and forced negative sign at the exact heights. The
   rigidity becomes: *a finite menu of forbidden resonances must be empty.*
2. **Frozen constants**: the detection threshold $T\asymp1/\delta_{\max}$ is a number of the world, not
   a degenerating limit: the statement to be certified (GAP-152.A at $\gamma_J$) is ONE individual
   instance, with no pending internal uniformity — the exact analogue of what H(m) bought for Rouché in D112
   §2.6.
3. **Dominance and sign** (Step A): under H(m) the defect signal is not subtle — it is exponential, of
   fixed sign, at a fixed frequency. No average hides it WITHIN the world.

**Does not buy (proved):**
1. The bound of Step B does not improve with $m$: the barrier $|S_T|\le S_T(0)$ is blind to the
   cardinality of off zeros. The interval $(0,\tfrac14)$ of allowed weights does not narrow by an epsilon with
   $m<\infty$.
2. The tautology (D112 Prop. 4.2) is not broken: (152.E) is ONE identity satisfied identically by the
   true configuration; the bias of Step A is the formula being self-consistent, not a tension.
3. The case $m=1$ is not easier (an exact parallel of D112 §5.3): the difficulty is certifying
   ONE frequency, independent of $m$.

### 3.6. Dual exceptionality: the bad frequencies are invisible to every average

**[PROPOSITION 152.9] (Besicovitch mean over the frequency).** For each fixed $T\ge1$, $S_T(\cdot)$ is
a Bohr almost-periodic function of $\tau$ (uniform limit of trigonometric polynomials: the series
converges absolutely and uniformly), and its mean square is
$$M_\tau\bigl(|S_T|^2\bigr)\;:=\;\lim_{\Omega\to\infty}\frac1{2\Omega}\int_{-\Omega}^{\Omega}|S_T(\tau)|^2\,d\tau
\;=\;\frac12\sum_{n\ge2}\frac{\Lambda(n)^2}{n}\,e^{-(\log n)^2/2T^2}\;\le\;C\,T^2.$$
Consequently, for every threshold $V>0$, the (Besicovitch) upper density of the set
$\{\tau:|S_T(\tau)|\ge V\}$ is $\le CT^2/V^2$; with $V=e^{\epsilon T^2}$, the **exponential
frequencies have density $\le CT^2e^{-2\epsilon T^2}\to0$**: they are exceptional for every average in $\tau$.

*Proof.* Bohr almost-periodicity: absolute and uniform convergence in $\tau$ of the series of
$S_T$. Parseval for almost-periodic functions [Bes32, Ch. I–II]: the frequencies $\log n$ are pairwise distinct
and each term $\Lambda(n)n^{-1/2}e^{-(\log n)^2/4T^2}\cos(\tau\log n)$ contributes half the
square of its amplitude. The sum: with $u=\log n$ and $\sum_{n\le x}\Lambda(n)^2/n\asymp(\log x)^2$
(Chebyshev + partial summation),
$\sum_n\Lambda(n)^2n^{-1}e^{-u^2/2T^2}\asymp\int_0^\infty ue^{-u^2/2T^2}du\asymp T^2$. Chebyshev's
inequality (measure estimate) for the density. $\square$

**Reading — the pincer with Doc 112.** Under H(m), the bad frequency $\gamma_J$ exists and is ONE;
Prop. 152.9 says the set of frequencies capable of carrying an exponential signal has density zero:
**certifying GAP-152.A at $\gamma_J$ is deciding an exceptional point of the statistics that govern
it** — Principle 3.1 of P43 (the master quantifier), in the coordinate DUAL to that of Prop. 2.6 of
D112. There: the good replica $\tau$'s (for Rouché) form a density-zero set and one must
PRODUCE one. Here: the bad (resonant) $\tau$ frequencies form a density-zero set and one must
EXCLUDE one. Replica and evaluation, existential and universal: the same wall, its two faces.

---

## 4. The minimal hypothesis and the comparative map

### 4.1. LP-152: the pointwise form of semi-global purity

**[NEW-DEFINITION 152.8] (LP-152).** For $\tau_0\ge1$:
$$\mathrm{LP\text{-}152}(\tau_0):\qquad |S_T(\tau_0)|\;=\;O_\epsilon\bigl(e^{\epsilon T^2}\bigr)\ \ \forall\epsilon>0
\qquad(\text{subexponentiality in }T^2).$$
By Theorem 152.2(a): $\mathrm{LP\text{-}152}(\tau_0)\iff$ no off quadruple of ζ has
$|\gamma_j-\tau_0|<\delta_j$. Immediate consequences, all proved:

1. LP-152 at EVERY frequency $\tau\ge1$ $\iff$ RH (Cor. 152.3(i)). The full family is
   RH-equivalent — declared with no embellishment.
2. A single instance LP-152$(\tau_0)$ is **strictly weaker than RH**: it only forbids
   quadruples in the window of $\tau_0$ (it is "RH per frequency").
3. Under H(m), the contradiction needs LP-152 at ONE frequency (any point in the window of the
   dominant quadruple, e.g. $\tau_0=\gamma_J$) — but the frequency is UNKNOWN (a datum of the hypothetical
   world): full rigidity $m<\infty\Rightarrow m=0$ is equivalent to the family
   $\{\mathrm{LP\text{-}152}(\tau)\}$ over the finitely many adversarial frequencies.

**Honesty about the status.** I do not claim that LP-152$(\tau_0)$ is provable for any $\tau_0$ beyond
what the classical zero-free regions give (for windows within the verified zone
$\gamma\le3\cdot10^{12}$ [PT21], LP-152 holds trivially: there are no off zeros there; the unverified
zone is exactly where the problem lives). The content of the definition is **the dictionary and the
duality**, not a promise of provability.

### 4.2. LP-152 against LP-112: the two faces of the pincer

| | **LP-112** (Doc 112) | **LP-152** (this doc) |
|---|---|---|
| logical type | existential: exhibit ONE $\tau$ with $\sup_D\vert\zeta(s+i\tau)-\zeta(s)\vert<\epsilon$ | universal: bound $S_T(\tau_0)$ at ONE frequency |
| mechanism against H(m) | replica (Rouché): produces zero $m{+}1$ | evaluation (explicit formula): forbids the bias of quadruple $J$ |
| what H(m) freezes | radius, margin, height threshold (F1–F4 of D112) | frequency and threshold $T\asymp1/\delta_{\max}$ |
| relevant set under H(m) | good witnesses: density ZERO (D112 Prop. 2.6) | bad frequencies: density ZERO (Prop. 152.9) |
| relation to RH | RH ⟹ LP-112 (Bagchi); LP-112 ⇏ RH known; LP-112 ⟹ $m\in\{0,\infty\}$ | RH ⟹ LP-152$(\tau)\,\forall\tau$; single instance weaker than RH; family ⟺ RH |
| arithmetic input | $\mathbb Q$-linear independence of $\{\log p\}$, Bagchi's support | fine equidistribution of $\Lambda$ against $\cos(\tau\log n)$ |
| form of the wall | produce a point of an exceptional set | exclude a point of an exceptional set |

**Honest comparison of strength.** I know of no implication in either direction between LP-112 and the
relevant family of LP-152 instances: LP-112 attacks H(m) via the self-approximation geometry of ζ (Kronecker
torus, D112 §3); LP-152 via the statistics of primes at one frequency. Under H(m) BOTH are
statements about individual events that the entire averaging machinery classifies as exceptional:
the wall of P43 does not distinguish existential from universal — it distinguishes generic from exceptional (the
lesson of D112 §6.3, now with its dual twin). The gain of having TWO forms: they are routes with
independent inputs — a non-generic selection mechanism in EITHER of the two coordinates would close
rigidity.

### 4.3. Position with respect to 144.D, H⁺ and the limit B1–B4

- **Against Conjecture 144.D (the finiteness half).** 144.D asks that the continuation of genuine Euler
  force a subsequence of FAT off zeros ($\delta_j\log\gamma_j\ge c$): it belongs to the $m<\infty$ half. The
  semi-global purity is orthogonal and complementary: it does not count zeros; it says how ANY of them
  resonates in the primes. Dictionary 152.3(iii) (detection at $T\asymp1/\delta$) is the proved global
  version of the mechanism 144.D postulates locally (impurity sustained at support $\asymp\log\gamma$). If
  144.D holds, the off zeros of an $m=\infty$ world are fat ⟹ their resonances are detectable at
  $T\asymp\log\gamma_j$: a calendar coherence between the two halves, recorded.
- **Against Conjecture H⁺ (Doc 131, Desideratum 6.9).** The desired theorem —«hermitian + Euler +
  $a\ge0$ + polar + $m<\infty$ ⟹ H»— is H⁺ degraded by $m<\infty$. The result of §3 is that the
  degradation does NOT buy a mechanism: the piece of H⁺ that $\Lambda\ge0$ already gives (boundary,
  $\omega\le\tfrac14$, 152.4–152.5) does not use $m<\infty$, and the remaining piece ($\omega=0$) is not cheapened
  by $m<\infty$ (§3.5). H⁺ remains RH-hard; its first genuine case is still GAP-135.B (the destructive
  semilocal two-prime object).
- **Against B1–B4 (Doc 135 §7.2).** Prop. 152.7 quantifies B1/B4 within the new framework: no finite
  stretch of primes produces impurity OR the diagonal; the pole (the global diagonal, $\omega(0)=\tfrac14$)
  and the hypothetical resonances ($\omega(\gamma_J)=\delta_J^2$) emerge together in the limit. RH is the
  statement that the limit creates THE diagonal and NOTHING more — *unique resonance*. Semi-global
  purity is the first formulation of the program in which the pole and the off zeros are objects of the
  SAME type (impurity caps) distinguished only by position (frequency 0 vs $\ne0$), weight ($\tfrac14$ vs
  $\delta^2$) and sign (positive vs negative).

---

## 5. VERDICT

### VERDICT: **NEW REDUCTION + MAP-OF-THE-FAILURE. There is no rigidity theorem; there is a new equivalent form, theorems internal to the framework, and the failure of the positivity route located at a single point.**

**What is proved (unconditional, complete proof in this document):**

1. **[THEOREM 152.2 + COROLLARY 152.3] (impurity spectrum).** $\omega(\tau)=\max(0,\max_j(\delta_j^2-(\gamma_j-\tau)^2))$
   for $\tau\ge1$; the pole is the weight-$\tfrac14$ impurity at frequency 0; at the height of a
   dominant quadruple the bias is permanently negative, $S_T(\gamma_J)\sim-2\sqrt\pi m_JTe^{\delta_{\max}^2T^2}$.
   RH ⟺ $\omega\equiv0$ on $[1,\infty)$ ⟺ *unique resonance (the pole)*. Intermediate growth rates
   impossible; impurity quantized by the $\delta_j^2$; detection dictionary $T\asymp1/\delta$ (M3 of
   D134) proved at the global level.

2. **[PROPOSITIONS 152.4 + 152.5 + 152.6 + 152.7] (exact jurisdiction of positivity and the ζ/D–H
   boundary).** $\Lambda\ge0\Rightarrow\omega\le\tfrac14$ with equality only at the pole (global Mertens,
   strict boundary = dVP reproduced in the framework) — exactly the global manifestation of the local
   weight-0 purity of the factors of ζ, and nothing more. Impurity is irreducibly collective (every finite
   stretch of primes is pure, consistent with B1–B4). D–H surpasses the ceiling $\tfrac14$ (zeros with
   $\beta>1$ ⟹ no positive von Mangoldt datum is possible): the repulsion/purity separation of Doc 146,
   formalized as $\omega\le\tfrac14$ (theorem, ζ) vs $\omega>\tfrac14$ (D–H).

3. **[§3: Steps A–C + GAP-152.A + PROPOSITION 152.9] (map of the failure).** The attempt
   «$m<\infty+\Lambda\ge0+$FE ⟹ $m=0$» fails at three exact points: **(F1)** positivity is
   zero-frequency information — its only law is $|S_T(\tau)|\le S_T(0)$ and the contradiction would require
   $\delta_{\max}\ge\tfrac12$ (the boundary, already excluded): the world H(m) lives in the Cauchy–Schwarz
   margin $e^{-(1/4-\delta_{\max}^2)T^2}$; **(F2)** the tautology of the explicit formula (D112 Prop. 4.2)
   is confirmed in frequency coordinates: the bias of Step A is self-consistency, not tension; **(F3)**
   the oscillation route is circular with a Landau inversion: positivity is the ENGINE of the oscillation
   of $\psi(x)-x$, not its brake, and the missing upper bound is the negation of H(m).

**The minimal hypothesis, measured.** LP-152$(\gamma_J)$ (subexponentiality of ONE frequency
correlation): strictly weaker than RH as an instance; as a family over the adversarial frequencies,
equivalent to rigidity; exact dual of LP-112 (replica/evaluation,
existential/universal); with its own exceptionality certificate (152.9: bad frequencies of density
zero) — the master quantifier of P43 through its second face.

**How the rigidity half now stands.** Better focused and with two independent arms: LP-112 (replica) and
LP-152 at the adversarial frequencies (evaluation), both non-RH-equivalent as instances, both
blocked by the same wall of non-generic selection, with distinct inputs. The requested synthesis is now
established: there are THREE purities, not two — **boundary** (weight 0, theorem: what $\Lambda\ge0$
buys), **semi-global** ($\omega\equiv0$: what rigidity needs, ⟺ RH), **global** ($m=0$, identical to the
preceding one via dictionary 152.2) — and the exact content of the rigidity half is crossing from
$\omega\le\tfrac14$ to $\omega=0$ over a finite menu of unknown frequencies. $m<\infty$ freezes the
menu; it does not empty it. **Von Mangoldt positivity is not the purity that collapses $m$: it is the
purity that confines impurity to the interval $(0,\tfrac14)$.** What genuine Euler structure must supply
further — if the program is right — is a non-generic selection mechanism in one of the two dual
coordinates; none of the catalogued methods (averages, recurrence, amplification, positivity, moments)
produces it.

### Final message

**VERDICT: NEW REDUCTION + MAP-OF-THE-FAILURE.** There does not exist (and this document shows why it
cannot exist via this route) the theorem «$m<\infty+\Lambda\ge0+$functional equation ⟹ $m=0$»: von
Mangoldt positivity certifies exactly boundary purity ($\omega\le\tfrac14$, de la Vallée Poussin) and is
blind to every nonzero frequency; the world H(m) lives in the Cauchy–Schwarz margin of that barrier. In
exchange, the rigidity half gains a new equivalent form (impurity spectrum, quantized, with
forced sign) and a dual target to LP-112.

**Three main results:**

1. **[THEOREM 152.2 + COROLLARY 152.3]** — *Impurity spectrum of ζ:* exact formula
   $\omega(\tau)=\max(0,\max_j(\delta_j^2-(\gamma_j-\tau)^2))$ for $\tau\ge1$; forced negative bias
   $S_T(\gamma_J)\sim-2\sqrt\pi m_JTe^{\delta_{\max}^2T^2}$; the pole = weight-$\tfrac14$ impurity at
   frequency 0; RH ⟺ unique resonance; quantized polynomial/exponential dichotomy; the
   impurity↔resolution dictionary ($T\asymp1/\delta$, M3 of D134) proved at the global level for ζ.

2. **[PROPOSITIONS 152.4 + 152.5 + 152.6 + 152.7]** — *Exact jurisdiction of positivity and the
   ζ/D–H boundary:* $\Lambda\ge0\Rightarrow\omega\le\tfrac14$ with equality only at the pole (global
   Mertens test, strict boundary); impurity is irreducibly collective; D–H surpasses the ceiling $\tfrac14$
   and admits no positive von Mangoldt datum — the repulsion/purity separation of Doc 146, formalized; and
   the weight discrepancy (B3 of D135) clarified: RH = recentering the ZEROS from weight 0 to weight 1, the
   one thing the functional equation does not do.

3. **[GAP-152.A + NEW-DEFINITION 152.8 + PROPOSITION 152.9]** — *Map of the failure and dual of LP-112:* the
   positivity+finiteness path dies at F1–F3 (zero frequency / tautology / circularity of oscillations,
   with the Landau inversion identified: positivity proves the oscillation, it does not prevent it); the
   minimal hypothesis is LP-152 (subexponentiality of the prime correlation at one frequency), weaker
   than RH per instance, existential/universal dual of LP-112, with bad frequencies of density
   zero — the second face of the master quantifier.

---

## References

**Internal (backward-only):** Doc 146 (cheap repulsion/expensive purity; D–H fat; Facts 146.4–146.6);
Doc 144 (LP-141, category D131-H⁺, Conjecture 144.D, GAP-144.C); Doc 141 (LP-134; Calculation 141.M4, lever
null on the line; Conjecture 141.E); Doc 137 (audit of the boundary $|\alpha|=1$); Doc 135 (Theorem A of two
primes; §7.2 B1–B4, B3 weight mismatch); Doc 134 (§5.8 M3 purity↔resolution dictionary; calendars);
Doc 131 (§6: Theorem 6.7 local purity, Prop. 6.5 diagonal mass, Prop. 6.8 D–H by blocks, Desideratum 6.9
Conjecture H⁺); Doc 112 (LP-112; Theorem 2.3/5.1; Prop. 2.6 zero density; Prop. 4.2 tautology of the
explicit formula; Obs. 4.3 external evaluators; §5.3 case m=1; §6.3 generic vs exceptional); Doc 109
(architecture D-109); P43 (Principle 3.1, master quantifier); P35 ($\kappa=2m$). Phase 38 ERRATA
respected ($W_\lambda\ge0$ refuted, not used).

**Literature (published, verifiable except as noted):**
- [Wei52] A. Weil, *Sur les «formules explicites» de la théorie des nombres premiers*, Comm. Sém. Math.
  Univ. Lund (1952), 252–265. (Explicit formula; positivity criterion ⟺ RH.)
- [Gui48] A. P. Guinand, *A summation formula in the theory of prime numbers*, Proc. London Math. Soc. (2)
  50 (1948), 107–119. (Summation form of the explicit formula.)
- [IK04] H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloq. Publ. 53, 2004. (Thm. 5.12:
  explicit formula with admissible test class — the convention used in (152.E).)
- [dVP96] Ch.-J. de la Vallée Poussin, *Recherches analytiques sur la théorie des nombres premiers*,
  Ann. Soc. Sci. Bruxelles 20 (1896), 183–256. (Non-vanishing on $\mathrm{Re}\,s=1$; classical zero-free
  region.)
- [Mer98] F. Mertens, *Über eine Eigenschaft der Riemannschen ζ-Funktion*, Sitzungsber. Akad. Wiss. Wien
  107 (1898), 1429–1434. (The inequality $3+4\cos\theta+\cos2\theta\ge0$.)
- [Sch03] E. Schmidt, *Über die Anzahl der Primzahlen unter gegebener Grenze*, Math. Ann. 57 (1903),
  195–204. ($\Omega_\pm$ for $\psi(x)-x$.)
- [Ing32] A. E. Ingham, *The Distribution of Prime Numbers*, Cambridge Tracts 30, Cambridge Univ. Press,
  1932. (Ch. V: oscillation theorems; Landau's theorem on integrands of one sign.)
- [Ing36] A. E. Ingham, *A note on the distribution of primes*, Acta Arith. 1 (1936), 201–211.
  (Oscillation forced by a hypothetical zero. **[literature GAP]:** exact constants not verified
  at page level this session; qualitative use only, not load-bearing.)
- [Pin80] J. Pintz, *On the remainder term of the prime number formula* I–II, Acta Arith. 36–37 (1980).
  (Effective oscillations localized by a zero. **[literature GAP]:** exact statements not
  verified at page level this session; qualitative use only, not load-bearing.)
- [Bes32] A. S. Besicovitch, *Almost Periodic Functions*, Cambridge Univ. Press, 1932. (Parseval for
  almost-periodic functions — Prop. 152.9.)
- [DH36] H. Davenport, H. Heilbronn, *On the zeros of certain Dirichlet series*, J. London Math. Soc. 11
  (1936), 181–185 and 307–312. (Zeros with $\beta>1$ — Prop. 152.6.)
- [Tit86] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. (rev. D. R. Heath-Brown),
  Oxford Univ. Press, 1986. (Riemann–von Mangoldt: $O(\log)$ zeros per unit window; §10.25 D–H.)
- [PT21] D. Platt, T. Trudgian, *The Riemann hypothesis is true up to* $3\cdot10^{12}$, Bull. London
  Math. Soc. 53 (2021), 792–797. (Verified zone — §4.1.)

*End of Doc 152.*
