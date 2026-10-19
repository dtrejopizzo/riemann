# Document 191 — Chink R1 to decision: Farmer's floor, a universal lower bound on the mollified moment, and the exact boundary θ=1/2

**Program:** Riemann Hypothesis — Phase 58 (full audit)
**Mandate:** decide chink R1 opened by audit D188 §5: barrier #2's absolute ceiling ([PROP 180.3]) was CONDITIONAL-ON-FARMER because the floor $c(\theta)\ge1+1/\theta$ is not a theorem over the general class of mollifiers. Three parts: exact inventory of $c(\theta)$'s status; attempted proof in both directions (seal/break); verdict.
**Prerequisites:** [PROP 180.3] (Littlewood–Jensen–mollifier conduit: $E(T)\le\frac{c-1}{2\pi a}\frac T{\log T}+O(\log T)$ — the conduit is proved, D188 §1.3); D188 downgrade (the ceiling was conditional); [Thm 170.5] ($E(T)\ll T/\log T$).
**Contract:** [THEOREM]/[PROP]/[LEMMA] only with complete proof; [GAP]/[literature GAP] declared; no numerics; backward-only; total candor.

**Coordinates.** $E(T)=\sum_{0<\gamma\le T,\beta>1/2}(\beta-\tfrac12)^2$; **A** $\iff E=O(1)$. Mollifier: $\varphi(s)=\sum_{n\le X}b_nn^{-s}$, $X=T^\theta$, $b_1=1$. Mollified moment on the line: $c(\theta):=\liminf_T\inf_\varphi\frac1T\int_0^T|\zeta\varphi(\tfrac12+it)|^2dt$ (infimum over the class to be specified). Breaking barrier #2 requires $(c(\theta)-1)/\theta\ll1/\log T$ for some $\theta\le1$; sealing it requires a floor $c(\theta)-1\gg_\theta1$ (or $\ge\theta/\log T\cdot w(T)$, $w\to\infty$) **for all** $\theta\le1$, as a **lower bound over the entire class**.

---

## 0. Executive summary and verdict

1. **[THEOREM 191.A] (partial, unconditional seal).** For the ENTIRE class of mollifiers with divisor-bounded coefficients, support $[1,T^\theta]$, $b_1=1$: $c(\theta)\ge1+\log\frac{1-\theta}\theta-o(1)$ for $\theta<\tfrac12$, uniform up to $\theta\le\tfrac12-C\frac{\log\log T}{\log T}$. **This is the first universal lower bound on the mollified moment I can locate** (modulo [GAP 191.L1] of novelty). Mechanism: convolution rigidity — $(1*b)(p)=1$ exactly for every prime $p>X$, whatever $b$ is.
2. **Consequence: barrier #2 is a THEOREM for $\theta<\tfrac12$.** The whole conduit with short mollifiers has ceiling $\asymp T/\log T$, no longer conditional on Farmer. Chink R1 narrows from "entire $\theta\le1$" to **$\theta\in(\tfrac12-o(1),\,1]$** — exactly Farmer 1993's *long mollifier* territory.
3. **[PROP 191.C] (non-initial support: catastrophic).** Mollifiers with support $\{1\}\cup(T^\alpha,T^\theta]$ have $c-1\ge\log(\alpha\log T)-O(1)\to\infty$. The mandate's intuition is proved in its logarithmic half: $\varphi$ MUST approximate $\mu$ over its entire initial range; every non-mollified prime costs $1/p$ of moment, with no class escape.
4. **The boundary $\theta=\tfrac12$ is one of RANGE, not arithmetic.** The rigidity $(1*b)(p)=1$ persists for all $p>X$ to infinity; what dies at $\theta\ge\tfrac12$ is the moment's *observable window* (the bilinear range $XY\le T^{1-\varepsilon}$ of Montgomery–Vaughan). [PROP 191.D]: under a bilinear-range hypothesis (TW$_y$) — diagonal domination up to $Y=T^y$, $y>\tfrac12$ — the floor extends and seals $\theta<y$ with $c-1\ge\log(y/\theta)$.
5. **Recalibration of the conditional:** barrier #2 on $\theta\in[\tfrac12,1]$ is NO LONGER conditioned on Farmer's OPTIMALITY conjecture ($c(\theta)=1+1/\theta$ exact) but only on a mean-value RANGE extension (much weaker: it suffices that the diagonal dominate, not that the standard mollifier be optimal). Breaking it would require $c(\theta)-1\ll1/\log T$: not a marginal failure of Farmer but a **constant-size negative off-diagonal conspiracy** erasing the forced diagonal mass — a catastrophic, not marginal, violation.
6. **Levinson/Feng direction (two pieces):** it leaves the conduit (does not vanish at ζ's off zeros) or re-enters the theorem's class; **smooth, adaptive weights in $t$:** the floor is insensitive (the rigidity lives in the coefficients). No examined class trick evades the floor at $\theta<\tfrac12$.
7. **Verdict R1: SEALED-BY-THEOREM at $\theta<\tfrac12$; CALIBRATED-CONDITIONAL (range-hard, no longer Farmer-hard) at $\theta\in[\tfrac12,1]$.** No improvement of $E(T)\ll T/\log T$ is obtained (this document builds a barrier, not a signal). [GAP-191.1]: the floor at $\theta\in[\tfrac12,1]$.

---

## 1. Part 1: exact inventory

### 1.1. What $c(\theta)$ is, and the direction of the inequality

$\frac1T\int_0^T|\zeta\varphi|^2(\tfrac12+it)\,dt$ is, after the available asymptotic evaluations, a quadratic form $\langle M_Tb,b\rangle$ in the coefficients; $c(\theta)$ is its normalized minimum ($b_1=1$). **Critical (D188 flagged it):** conduit 180.3 needs the **lower bound** $c(\theta)\ge1+\delta(\theta)$ over the ENTIRE class — the direction opposite to what the industry optimizes (the industry builds $\varphi$ with SMALL moment for Levinson/critical proportion; it never needed to prove it cannot go lower, except within its own variational class).

### 1.2. What is theorem and what is conjecture

- **Theorem (evaluation):** the asymptotic of the mollified moment for coefficients in concrete classes: Balasubramanian–Conrey–Heath-Brown 1985 evaluate $\frac1T\int|\zeta A|^2$ for Dirichlet polynomials of length $T^\theta$, $\theta<\tfrac12$ (divisor-bounded coefficients); Conrey 1989 extends the evaluable range to $\theta<\tfrac47$ for the forms used in the $\ge2/5$ proportion (Selberg–Levinson-type coefficients $\mu(h)h^{\sigma-1/2}P(\log(y/h)/\log y)$). For the standard mollifier the optimal value within its variational class is $1+\tfrac1\theta+o(1)$.
- **Conjecture (Farmer 1993, "Long mollifiers of the Riemann zeta-function", *Bull. LMS* 25):** that $c(\theta)=1+\tfrac1\theta$ persists for ALL $\theta$ — the "$\theta=\infty$ conjecture", with RH-adjacent consequences (ζ-moments, proportions $\to1$). It is an **optimality** conjecture (the floor is also a ceiling). Later literature on equivalences and consequences (Bettin–Gonek and coauthors on the $\theta=\infty$ conjecture): [literature GAP 191.L2 — I cannot verify the exact statements of those works from memory; not used here].
- **What I do NOT locate as a prior theorem:** the lower bound $c(\theta)\ge1+\delta(\theta)$, $\delta>0$, over the GENERAL class of coefficients (not just the standard variational one). Farmer's variational calculus (and Goldston–Gonek's in sibling quadratic-minimum problems with $\Lambda$/$\mu$) operates over smooth parametrized classes; that the minimum of BCHB's full quadratic form over ARBITRARY coefficients is $1+1/\theta$ is plausible (the problem is quadratic and in principle solvable for $\theta<\tfrac12$ where the form is evaluated), but I do not have the statement in the literature. [literature GAP 191.L1: if Farmer 1993's variational section or a successor already proves the minimum over general coefficients for $\theta<\tfrac12$, Theorem 191.A is redundant in that range — though its elementary proof and its uniformity near $\tfrac12$ would still have independent value. Audit before publication.]
- **$\theta\ge1$:** the mean-value theorem $\int_0^T|\sum_{n\le N}a_nn^{-it}|^2dt=(T+O(N))\sum|a_n|^2$ loses the main term for $N\gg T$; there is no moment technology with $X>T$, nor an impossibility theorem (D188: ceiling *de facto*, not *de jure*). Unchanged.

**Inventory conclusion:** audit D188 was right and understated it: without a universal lower bound, barrier #2 was conditional **even for small $\theta$**. Part 2 fixes exactly that.

---

## 2. Part 2, sealing direction: the universal lower bound

### 2.1. The mechanism: convolution rigidity at primes

**[LEMMA 191.1].** Let $b$ be any sequence with $b_1=1$ and $b_n=0$ for $n>X$. Let $A=1*b$, i.e. $A_k=\sum_{n\mid k}b_n$ (the Dirichlet coefficients of $\zeta\varphi$). Then $A_p=1$ **for every prime $p>X$**.

*Proof.* $A_p=b_1+b_p=1+0=1$. $\square$

This is a combinatorial identity, blind to the class of $b$: the tail of $\zeta\varphi-1$ has coefficient EXACTLY $1$ at every prime beyond the support. The whole question is how much of that forced mass the moment over $[0,T]$ **sees**.

### 2.2. The theorem

**[THEOREM 191.A].** Fix $\kappa\in\mathbb N$, $A_0>0$. Let $\varphi(s)=\sum_{n\le X}b_nn^{-s}$ with $b_1=1$, $|b_n|\le d_\kappa(n)(\log T)^{A_0}$, $X=T^\theta$. There exists $C_0=C_0(\kappa,A_0)$ such that for $0<\theta\le\tfrac12-C_0\frac{\log\log T}{\log T}$ and every $\eta\in[C_0\frac{\log\log T}{\log T},\tfrac12]$ with $\theta+\eta\le\tfrac12$... more precisely, with $Y=T^{1-\theta-\eta}$:
$$\frac1T\int_0^T\big|\zeta\varphi(\tfrac12+it)\big|^2dt\;\ge\;1+\sum_{X<p\le Y}\frac1p\;-\;O\!\big(e^{-\eta\log T/3}(\log T)^{B}\big)\;=\;1+\log\frac{1-\theta-\eta}{\theta}-o_\eta(1).$$
In particular, for every $\theta\le\tfrac12-\delta$ with $\delta\ge C_0\frac{\log\log T}{\log T}$: $\;c(\theta)-1\ge\delta$ (taking $\eta=\delta$, since $\log\frac{1-\theta-\delta}{\theta}\ge\log\frac{1/2}{1/2-\delta}\ge2\delta$, and the error is $\le\delta$ by the choice of $C_0$).

*Proof.* Write $F(t)=\zeta\varphi(\tfrac12+it)$ and $G=F-1$.

**(i) Reduction to polynomials (Hardy–Littlewood).** For $1\le t\le T$, the Hardy–Littlewood approximation (Titchmarsh, Thm 4.11) with $x=T$: $\zeta(\tfrac12+it)=\sum_{m\le T}m^{-1/2-it}+\frac{T^{1/2-it}}{\tfrac12+it-1}+O(T^{-1/2})$. Let $Z(t)=\sum_{m\le T}m^{-1/2-it}$ and $F_0=Z\varphi$, a Dirichlet polynomial of length $TX$ with coefficients $\alpha_N=\sum_{n\mid N,\,n\le X,\,N/n\le T}b_n$, satisfying $|\alpha_N|\le d_{\kappa+1}(N)(\log T)^{A_0}$ and $\alpha_1=1$, $\alpha_p=1$ for $X<p\le T$. The correction term: $|F-F_0|\ll(T^{1/2}/t+T^{-1/2})\,|\varphi(\tfrac12+it)|\ll(T^{1/2}/t)\,X^{1/2}(\log T)^{B_1}$ for $t\ge1$; its contribution to any bilinear form against a polynomial $D$ of length $Y$ bounded by $\sup|D|\ll Y^{1/2}$ is $\ll T^{1/2}X^{1/2}Y^{1/2}(\log T)^{B_2}=T^{1-\eta/2}(\log T)^{B_2}$; the segment $0\le t\le1$ contributes $\ll\sup_{t\le1}|FD|\ll T^{1/2+\theta}$ trivially (convexity and $|\varphi|\le X^{1/2+o(1)}$). Both absorbed into the statement's error.

**(ii) The test.** Let $D(t)=\sum_{X<p\le Y}p^{-1/2-it}$ (sum over primes). By Cauchy–Schwarz,
$$\frac1T\int_0^T|G|^2dt\;\ge\;\frac{\big|\frac1T\int_0^TG\,\overline D\,dt\big|^2}{\frac1T\int_0^T|D|^2dt}.$$

**(iii) Denominator.** Montgomery–Vaughan (mean value): $\frac1T\int_0^T|D|^2dt=\sum_{X<p\le Y}\frac1p\big(1+O(p/T)\big)=\big(1+O(Y/T)\big)\sum_{X<p\le Y}\frac1p$.

**(iv) Numerator.** $\int_0^TG\overline D=\int_0^T(F_0-1)\overline D+\text{(corrections of (i))}$. The bilinear form $\int_0^T(F_0-1)\overline D\,dt$ has frequencies $\log(N/k)$, $N\le TX$, $k\in(X,Y]$ prime. Montgomery–Vaughan's (1974) generalized Hilbert inequality gives
$$\int_0^T(F_0-1)\overline D\,dt\;=\;T\sum_{X<p\le Y}\frac{\alpha_p}{p}\;+\;O\Big(\big(\textstyle\sum_{N\le TX}|\alpha_N|^2\big)^{1/2}\big(\sum_{X<p\le Y}1\big)^{1/2}\Big),$$
(diagonal $N=k=p$; the $-1$ term has no diagonal because $D$ contains no $n=1$). By [LEMMA 191.1], $\alpha_p=1$ over the whole range. The error: $\sum_{N\le TX}|\alpha_N|^2\ll TX(\log T)^{B_3}$, so error $\ll(TXY)^{1/2}(\log T)^{B_3}=T^{1-\eta/2}(\log T)^{B_3}$.

**(v) Assembly.** With $\mathcal P:=\sum_{X<p\le Y}1/p=\log\frac{1-\theta-\eta}\theta+O(1/\log X)$ (Mertens):
$$\frac1T\int_0^T|G|^2dt\;\ge\;\frac{\big(\mathcal P-O(T^{-\eta/2}(\log T)^{B})\big)^2}{\mathcal P\,(1+O(Y/T))}\;=\;\mathcal P-O\big(T^{-\eta/3}\big).$$
**(vi) From $G$'s square to the moment.** $\frac1T\int|F|^2=1+\frac2T\mathrm{Re}\int G+\frac1T\int|G|^2$, and the first moment $\frac1T\int_0^TG\,dt=o(1)$ with power saving: by (i) and Montgomery–Vaughan with $D\equiv1$, the diagonal is $\alpha_1-1=0$ and the error is $\ll T^{-1/2}(TX)^{1/2}(\log T)^{B}=T^{\theta/2-\dots}$… more carefully: $\frac1T\int_0^T(F_0-1)dt=\frac1T\sum_{N\ge2}\alpha_NN^{-1/2}\frac{N^{-iT}-1}{-i\log N}\ll\frac1T\sum_{2\le N\le TX}|\alpha_N|N^{-1/2}\ll T^{-1}(TX)^{1/2}(\log T)^{B}=T^{(\theta-1)/2}(\log T)^B=o(1)$ (power saving for $\theta<1$). The corrections of (i) against $1$: $\ll T^{-1/2}X^{1/2}(\log T)^{B}=o(1)$ likewise. Putting it together: $\frac1T\int|F|^2\ge1+\mathcal P-o(1)$ with all errors $\le e^{-\eta\log T/3}(\log T)^B$ except Mertens's $O(1/\log X)=O(1/(\theta\log T))$, absorbed by choosing $C_0$ large. $\square$

**Candor remarks.** (1) The divisor-bounded class covers every mollifier ever used (Selberg–Levinson, Conrey, Feng with pieces $\mu*\Lambda^{*j}$, Radziwiłł–Soundararajan); truly arbitrary coefficients (e.g. $|b_n|\sim e^{\sqrt n}$) fall outside, but only affect the error constants $B_i$ via $\sum|\alpha_N|^2$ — the proof tolerates $|b_n|\le n^{\varepsilon_0}$ with small fixed $\varepsilon_0$ at the cost of shrinking the range of $\eta$. (2) The rate $\log\frac{1-\theta}\theta$ is **weaker** than Farmer's floor $1/\theta$ as $\theta\to0$ (logarithm vs. reciprocal): our test only sees the tail primes, not all of $1*b$'s mass; the full $1/\theta$ would require the off-diagonal/swap terms that only BCHB-type evaluations capture. For the barrier this is irrelevant: a constant floor $\ge\delta>0$ suffices. (3) As $\theta\to\tfrac12$ the floor degenerates linearly — and that is real, not an artifact: see §3.2.

**[COROLLARY 191.B] (barrier #2 is a theorem for short mollifiers).** For every family $\varphi_T$ in the class of 191.A with $\theta\le\tfrac12-\delta$, $\delta\ge C_0\frac{\log\log T}{\log T}$, [PROP 180.3]'s conduit produces $E(T)\le\frac{c-1}{2\pi a}\frac T{\log T}$ with $c-1\ge\delta$ and $a\asymp\theta\le\tfrac12$: **no choice gives $E(T)=o(\delta\cdot T/\log T)$ via the conduit**; in particular gaining a log ($(c-1)/\theta\ll1/\log T$) is impossible in this range. Moreover, the floor also holds in the shifted versions: the same proof with $\zeta\varphi(\tfrac12+s+it)$ places $p^{-2s}$ on the diagonal ($\alpha_p\,p^{-s}\cdot p^{-s}$), giving $\text{mean}(s)-1\ge\sum_{X<p\le Y}p^{-1-2s}-o(1)$, which reproduces exactly 180.3's exponential form (M) with rate $a\le2(1-\theta)$ FROM BELOW: the conduit's input cannot be smaller than this. *Proof:* substitution into 180.3 + literal repetition of 191.A with the shift (the errors are uniform in $0\le s\le\tfrac12$ because they only improve). $\square$

### 2.3. Non-initial support: worse, not better

**[PROP 191.C].** If additionally $b_n=0$ for $1<n\le T^\alpha$ (support $\{1\}\cup(T^\alpha,T^\theta]$, $\theta<\tfrac12$), then $c-1\ge\sum_{p\le T^\alpha}\frac1p-o(1)=\log(\alpha\log T)-O(1)\to\infty$.

*Proof.* [LEMMA 191.1] now also gives $A_p=1$ for every prime $p\le T^\alpha$ (since $b_p=0$); apply 191.A with the test $D=\sum_{1<p\le T^\alpha}p^{-1/2-it}$ (length $T^\alpha\le Y$, same errors). $\square$

**Reading.** The mechanism conjectured by the mandate ("$\varphi$ must approximate $1/\zeta$; the unapproximated tail has mass") is PROVED in its logarithmic half, with exact localization: **every non-mollified prime costs $1/p$, an identity with no class escape.** Gaps in the support are catastrophic; the only freedom lies in HOW the initial range is mollified, not in WHETHER it is mollified.

---

## 3. Part 2, breaking direction: the four variants and the boundary θ=1/2

### 3.1. The mandate's variants

- **(i) Non-initial support:** killed by [PROP 191.C] — direction opposite to breaking.
- **(ii) Adaptive mollifiers in $t$ (by windows).** Conduit 180.3 admits them: Littlewood's lemma applies by sub-rectangles $t\in[T_j,T_{j+1}]$ ($\sigma$-integration is untouched) and $E=\sum_jE_j$. But the floor also localizes: Hardy–Littlewood and Montgomery–Vaughan work over $[T_j,T_{j+1}]$ as long as the window is $\ge X^{2}$-ish (bilinear range relative to the window), and then $c_j-1\ge\log\frac{1-\theta_j'}{\theta_j'}$ with $\theta_j'=\log X_j/\log|\text{window}|\ge\theta$. Windows shorter than the mollifier's square fall into the same open regime as global $\theta\ge\tfrac12$: **adaptivity creates no new loophole, it reparametrizes the same one.**
- **(iii) Two-piece Levinson/Feng-type ($\psi_1+\psi_2\zeta'$ etc.).** Crucial distinction: conduit 180.3 requires $f$ to VANISH at ζ's off zeros (step (i): $E_\zeta\le E_f$). $f=\zeta\varphi_1+\zeta'\varphi_2$ does NOT vanish at $\rho$ ($f(\rho)=\zeta'(\rho)\varphi_2(\rho)\ne0$ generically): that family detects zeros of combinations — useful for on-line proportion (Levinson 1974, Conrey 1989, Feng 2012), **useless for bounding $E$**: it leaves the conduit. The general admissible form is $f=\zeta G$; if $G$ is any series with divisor-bounded coefficients of effective length $\le T^\theta$ (including combinations with weights $\log n$, pieces $\mu*\Lambda$, etc.), [THEOREM 191.A] applies VERBATIM (the proof never uses multiplicativity or the sign of $b$). If $G$ has length $>T^{1/2}$ (e.g. truncating $\zeta'/\zeta$ to a long range): it re-enters the chink of §3.2, does not evade it.
- **(iv) Smooth weights in $t$ (Radziwiłł–Soundararajan).** The floor is insensitive: the rigidity lives in the coefficients, and a weight $w(t/T)\ge0$ only multiplies the diagonal and the denominator by the same mass $\widehat w(0)$ (Cauchy–Schwarz passes through the same way). Weights NOT multiplicative in $n$ are already within 191.A's class.

**Synthesis: no examined class trick touches the floor at $\theta<\tfrac12$.** The mechanism is information-theoretic as the mandate intuited, with precision: the proved half is **rigidity at primes** (logarithmic); the $1/\theta$ half (total mass of $1/\zeta$'s tail) remains Farmer's conjecture.

### 3.2. Where the boundary really lies: range, not arithmetic

The rigidity $(1*b)(p)=1$ holds for ALL $p>X$ to infinity — the arithmetic obstruction does not end at $\theta=\tfrac12$. What ends is the **observable window**: the proof needs to extract the diagonal of the bilinear form $\int\zeta\varphi\overline D$ with $D$ of length $Y>X$, and the unconditional treatment (HL with $x=T$ + MV) requires $XY\le T^{1-\eta}$, hence $Y>X\Rightarrow\theta<\tfrac12$. Beyond that, the swap terms (the $\chi$ part of the functional equation, saddle at $t\approx2\pi mn/k$) are the size of the diagonal and no one knows how to sum them for general coefficients — the same $\theta<\tfrac47$ range wall of Conrey, seen from the lower-bound side.

**[PROP 191.D] (conditional, range extension).** Fix $y\in(\tfrac12,1)$. Hypothesis (TW$_y$): for polynomials $D$ of length $T^y$ with divisor-bounded coefficients supported on primes, $\int_0^T\zeta\varphi(\tfrac12+it)\overline{D(\tfrac12+it)}\,dt=T\sum_p\alpha_pp^{-1}+O(T^{1-\varepsilon})$ uniformly over 191.A's class. Then $c(\theta)\ge1+\log(y/\theta)-o(1)$ for every $\theta<y$, and barrier #2 is sealed at $\theta<y$. *Proof:* identical to 191.A replacing step (iv) with (TW$_y$). $\square$

**Calibration of the residual conditional ($\theta\in[\tfrac12,1]$).** Breaking the barrier there requires $c(\theta)-1\le\theta/\log T\le1/\log T$. Under Farmer's conjecture, $c(\theta)-1=1/\theta\ge1$: breaking it is not "Farmer fails a little" but **Farmer failing by a factor of $\log T$** — and further, by the structure of 191.A's proof, it would require the swap terms to CANCEL the forced diagonal mass $\sum_{X<p\lesssim T}1/p\asymp\log(1/\theta)+O(1)$ down to $O(1/\log T)$: an exact negative correlation between the $\chi$ part and the prime diagonal, uniform in $T$, for which no candidate mechanism exists. Barrier #2 at $\theta\ge\tfrac12$ remains **range-hard**: implied by (TW$_y$) — a mean-value statement of a genus the industry considers more accessible than any optimality — not equivalent to the full Farmer conjecture. (We do not prove the reverse implication: breaking it does not formally refute (TW$_y$) in full strength, only its diagonal consequence. The exact equivalence remains open.)

---

## 4. Anti-circularity test

| Piece | ζ-free? | Where ζ enters |
|---|---|---|
| [LEMMA 191.1] rigidity | Yes (pure convolution combinatorics) | — |
| [THEOREM 191.A] | No | Only via Hardy–Littlewood (ζ approximation, unconditional) and Mertens; **uses no RH, no A, no LP-112, no zero densities** |
| [PROP 191.C], [COR 191.B] | Inherit from 191.A | same |
| [PROP 191.D] | Conditional on (TW$_y$), a mean-value hypothesis NOT about zeros | — |

No circularity: no piece assumes anything about the position of the zeros; the output is a barrier about techniques, compatible with RH and with ¬RH.

## 5. Part 3: verdict

| Label | Statement | Status |
|---|---|---|
| [LEMMA 191.1] | $(1*b)(p)=1$ for all $p>X$: universal rigidity | Proved (trivial, decisive) |
| [THEOREM 191.A] | $c(\theta)\ge1+\log\frac{1-\theta}\theta-o(1)$, divisor-bounded class, uniform for $\theta\le\tfrac12-C_0\frac{\log\log T}{\log T}$ | **Proved, unconditional** |
| [COR 191.B] | Barrier #2 = THEOREM at $\theta<\tfrac12$ (including the shifted form (M)) | Proved |
| [PROP 191.C] | Non-initial support: $c-1\gg\log\log T$ | Proved |
| [PROP 191.D] | (TW$_y$) ⟹ seal up to $\theta<y$ | Proved conditional |

**R1 stands: SEALED-BY-THEOREM at $\theta<\tfrac12$ (divisor-bounded class, which exhausts the industry), CALIBRATED-CONDITIONAL at $\theta\in[\tfrac12,1]$** — conditional no longer on Farmer's optimality but on the range extension (TW$_y$), and breaking it would require a $\log T$-factor violation of the conjectural floor plus a swap-diagonal cancellation with no known mechanism. In the program's terminology: barrier #2 upgrades from "sociological bet shaped like a theorem" (D188) to **theorem-in-short-range + hard-range-in-long-range**. The correct phrase for the architecture: *the mollifier conduit is closed by theorem except for Farmer's long mollifiers, and opening it there would require catastrophically refuting the $\theta=\infty$ conjecture, not evading it.*

**Improvement of $E(T)\ll T/\log T$?** No — and it could not: this document builds the conduit's input lower bound (a barrier), which is logically opposite to the signal. No improvement claim is made.

**Numbered GAPs:**
- **[GAP-191.1]** (the residual chink): floor $c(\theta)\ge1+\delta(\theta)$ for $\theta\in[\tfrac12,1]$, general class. Implied by (TW$_y$); status = open, genus "bilinear range beyond the square root".
- **[GAP-191.2]**: the rate — our floor is $\log(1/\theta)$, Farmer's is $1/\theta$; closing the gap for $\theta<\tfrac12$ would require evaluating the minimum of BCHB's full quadratic form over arbitrary coefficients (possibly already implicit in the variational literature: see 191.L1). Irrelevant to the barrier, relevant to publication.
- **[literature GAP 191.L1]**: novelty of 191.A (do Farmer 1993 / Goldston–Gonek / successors already contain a universal lower bound?); **[191.L2]**: exact statements of Bettin–Gonek on the $\theta=\infty$ conjecture; **[191.L3]**: the exact range of BCHB 1985's asymptotic for general coefficients ($\theta<\tfrac12$, cited from memory) and Conrey 1989's $\tfrac47$ (restricted class).

**Successor direction.** (1) Audit 191.A (it is elementary: an auditor should be able to reconstruct (i)–(vi) in one session); if it survives, it is a candidate for a publishable note on its own — the first universal lower bound on mollification — pending resolution of 191.L1. (2) Chink R2 (boundary flux, Doc 189) and this seal are independent; with R1 calibrated, the wall's remaining live residue is again unique: $\mu_2=o(1)$ ([GAP-180.1], genus 141.G1). (3) Literature task 188.L2 (Fujii on $\int S_1$) remains pending and precedes any attempt on $\mu_2$.

---

## References

- N. Levinson, "More than one third of zeros of Riemann's zeta-function are on $\sigma=1/2$", *Adv. Math.* 13 (1974).
- R. Balasubramanian, J. B. Conrey, D. R. Heath-Brown, "Asymptotic mean square of the product of the Riemann zeta-function and a Dirichlet polynomial", *J. reine angew. Math.* 357 (1985). [Evaluation, $\theta<\tfrac12$; GAP 191.L3.]
- J. B. Conrey, "More than two fifths of the zeros of the Riemann zeta function are on the critical line", *J. reine angew. Math.* 399 (1989). [$\theta<\tfrac47$, restricted class.]
- D. W. Farmer, "Long mollifiers of the Riemann zeta-function", *Bull. London Math. Soc.* 25 (1993). [$\theta=\infty$ conjecture; floor $1+1/\theta$ as optimality.]
- H. L. Montgomery, R. C. Vaughan, "Hilbert's inequality", *J. London Math. Soc.* (2) 8 (1974). [Mean value and bilinear form; steps (iii)–(iv).]
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford 1986. [Thm 4.11, Hardy–Littlewood approximation.]
- S. Feng, "Zeros of the Riemann zeta function on the critical line", *J. Number Theory* 132 (2012). [Two-piece mollifier; §3.1(iii).]
- M. Radziwiłł, K. Soundararajan, works on moments with smooth weights. [§3.1(iv); calibrational use.]
- D. A. Goldston, S. M. Gonek, works on minima of quadratic forms with $\mu$/$\Lambda$. [GAP 191.L1.]
- S. Bettin, S. M. Gonek, on the $\theta=\infty$ conjecture. [GAP 191.L2: unverified.]
- H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS 2004, chapter on mollifiers/mean values. [Background.]

**Internal documents:** D170 (Thm 170.5), D176 (176.9), D180 (180.3, audited), D188 (audit; chink R1), D189 (R2), D190.
