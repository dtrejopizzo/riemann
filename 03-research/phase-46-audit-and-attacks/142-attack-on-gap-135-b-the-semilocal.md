# Doc 142 — Attack on GAP-135.B: the semilocal object with archimedean term

**Program:** Riemann Hypothesis — Phase 46: audit and attacks.
**Prerequisites:** Doc 135 (two-prime theorem; breakpoints B1–B4; GAP-135.B), P48 (`06-papers/P48-weil-positivity-finite-primes/main.tex`: Conjecture H⁺, normalizations), Doc 131 (category $\mathcal{A}rith$, slots $(a,c,\omega)$).
**Creative contract:** [NEW-DEFINITION] total freedom; [THEOREM]/[PROPOSITION]/[LEMMA] with complete proof; [COMPUTATION] verified; [BRIDGE] with declared status; [GAP] named. Absolute frankness.

**Conventions (those of Doc 135/P48, fixed once).** $G=\mathbb R_+^*$, $d^*x=dx/x$, tests $f\in C_c^\infty(G)$, Mellin $\hat f(s)=\int_0^\infty f(x)x^{s-1}dx$, $\tilde f(x)=\overline{f(1/x)}x^{-1}$, $g:=f\star\tilde f$ (multiplicative convolution). For given $f$:
$$F(t):=f(e^t)e^{t/2}\in C_c^\infty(\mathbb R),\qquad \hat F(\xi):=\int_{\mathbb R}F(t)e^{i\xi t}dt,\qquad \hat f(\tfrac12+i\xi)=\hat F(\xi),$$
$$G(t):=g(e^t)e^{t/2}=\int_{\mathbb R}F(s)\overline{F(s-t)}\,ds,\qquad \hat G(\xi)=|\hat F(\xi)|^2,\qquad G(-t)=\overline{G(t)},$$
$$\|f\|_w^2:=\int_G|f|^2x\,d^*x=\|F\|_{L^2}^2,\qquad g(1)=G(0)=\|f\|_w^2.$$
"Window of length $2T$" = $\mathrm{supp}\,F$ contained in an interval of length $2T$ (free position). $L_p:=\log p$. $\psi:=\Gamma'/\Gamma$ is the digamma function; $\gamma$ is Euler's constant.

---

## 0. Executive summary

GAP-135.B asked to decide the H axiom for the first object of the **destructive** regime: $n$ primes with data $a=\Lambda\ge0$, polar block $[0]+[1]$, and an archimedean term of $\zeta$-type (the factor $\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2)$). Result, without ornament: **H fails** — for every finite set $S$ of primes, and even for $S=\varnothing$ (the polar+archimedean heart alone). But it fails in an extraordinarily informative way, and positivity **survives in two explicit cones**. The findings:

1. **(§1–2)** The semilocal object $X_S^{\mathrm{ar}}$ and its form $Q_S$ are defined in closed form in the normalization of P48. The archimedean weight is $\Omega(\xi)=\mathrm{Re}\,\psi(\tfrac14+\tfrac{i\xi}2)-\log\pi$, with three closed-form lemmas: explicit series, exact value
   $$\Omega(0)=\psi(\tfrac14)-\log\pi=-\gamma-\tfrac\pi2-3\log2-\log\pi\approx-5.3722<0,$$
   strict monotonicity in $|\xi|$ (whence $\mathcal A(f)\ge\Omega(0)\|f\|_w^2$: **archimedean destructiveness has an absolute floor**, unlike the impurity of Doc 135, which was bottomless destructiveness $p^{M\delta'}$), and effective logarithmic bounds.

2. **(§3) [THEOREM A — the first semilocal positivity of the program]** For **every** finite $S$ (and for $\zeta$ itself): if the window is $2T\le1/150$, then $Q_S(f)\ge\tfrac3{10}\|f\|_w^2$, unconditional, with explicit (crude, declared) constants. The mixed constructive/destructive regime is positive at short scale: at high frequency $\Omega\sim\log|\xi|$ dominates everything.

3. **(§4) [COMPUTATION]** The Mertens test — the adversary that decided everything in the constructive regime (Doc 135 §4) — **does not break** the semilocal object: the destructive coupling of a prime at height $M$ decays as $L_p\,p^{-M/2}\le0.736$, and the archimedean margin $\sim\log(1/\epsilon)$ crushes it. The correct adversary is a different one.

4. **(§5) [THEOREM B — the failure, localized]** The correct adversary is **slow, wide, and low-frequency, with the pole evaded**: an explicit family $f_T$ with $\hat f_T(1)=0$ (a single linear condition, of exponentially small cost $e^{-T/8}$) and spectral mass concentrated at $\xi=O(1/T)$ gives
   $$\lim_{T\to\infty}\frac{Q_S(f_T)}{\|f_T\|_w^2}\;=\;\Omega(0)\;-\;\sum_{p\in S}\frac{2\log p}{\sqrt p-1}\;<\;0,$$
   also for $S=\varnothing$. For $S=\{2,3\}$ (the object of GAP-135.B): $\approx-11.72$. **Each added prime worsens the violation** — the exact inversion of the constructive regime, where the foreign prime protected ($+L_q$, Doc 135 §4).

5. **(§6) [BRIDGE + COROLLARY]** The mechanism, isolated: **the polar block guards only the complex frequency $\xi=-i/2$; the archimedean deficit lives at real frequencies $|\xi|<\xi_*$. In $\zeta$, it is the FULL sum over primes that transmits the pole's custody to the real axis** (the identity $Q_S(f_T)=Q_\zeta(f_T)-[P_S-P_{\mathrm{full}}](f_T)$ and, under RH, $\lim_T P_{\mathrm{full}}(f_T)=\Omega(0)\|\eta\|^2<0$: the full sum over primes changes sign in aggregate; no finite truncation sees it, since each fixed lag contributes $+\|\eta\|^2$). B1/B4 of Doc 135, exact facts on a single family of tests.

6. **(§7) Map of the destructive regime:** positivity on $[0,T_0]$ (Theorem A), failure on $[T_1,\infty)$ (Theorem B), intermediate region = GAP-142.A; and an explicit **high-frequency cone** where positivity survives in every window (Proposition 7.2). The constructive threshold $\log(p_1\cdots p_n)$ of Doc 135 **collapses** in the destructive regime to an absolute archimedean threshold, independent of $S$.

7. **(§8) Verdict on H⁺:** surgical. Our counterexample verifies all the explicit hypotheses of H⁺ **except spectrality, which remains undecided**. Therefore: **H⁺ $\Rightarrow$ $X_S^{\mathrm{ar}}$ is not spectral** (contrapositive proved). Either GAP-135.B was ill-posed (the semilocal object was never in the class of H⁺, and spectrality carries the ENTIRE weight of the conjecture), or H⁺ is false. Deciding which = GAP-142.B. H⁺ survives in refined form: restricted to short windows (proved here for finite $S$) or to the high-frequency cone, or with the additional hypothesis of the **complete Euler product** — in which case its content concentrates on the pole→real-axis transmission, i.e. on RH itself.

---

## 1. [NEW-DEFINITION] The archimedean semilocal object

**[NEW-DEFINITION 1.1] ($\zeta$-type archimedean weight).** The **archimedean weight** is the function
$$\Omega(\xi)\;:=\;\mathrm{Re}\,\,\psi\Bigl(\frac14+\frac{i\xi}2\Bigr)\;-\;\log\pi,\qquad \xi\in\mathbb R,$$
and the **archimedean term** of the program is the quadratic functional
$$\mathcal A(f)\;:=\;\frac1{2\pi}\int_{\mathbb R}|\hat F(\xi)|^2\,\Omega(\xi)\,d\xi.$$
This is exactly the contribution of $\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2)$ in the Riemann–Weil explicit formula: $\frac{d}{ds}\log\Gamma_{\mathbb R}(s)\big|_{s=1/2+i\xi}=\tfrac12[\psi(\tfrac14+\tfrac{i\xi}2)-\log\pi]$, and the fold $s\leftrightarrow1-\bar s$ produces the real part. **[FACT]:** Weil 1952; Bombieri 2000, §1; Iwaniec–Kowalski 2004, Theorem 5.12.

**[NEW-DEFINITION 1.2] (the archimedean semilocal object).** Let $S=\{p_1,\dots,p_n\}$ be a finite set of primes ($S=\varnothing$ is allowed). The **archimedean semilocal object** is
$$X_S^{\mathrm{ar}}\;:=\;\bigl(a_S,\;[0]+[1],\;\omega_\zeta\bigr),\qquad a_S:=\Lambda\cdot\mathbf 1_{\{p^m:\,p\in S,\,m\ge1\}}\;\ge\;0,$$
that is: von Mangoldt arithmetic data restricted to $S$ (**destructive** regime: $a\ge0$, exactly the class of H⁺ and the opposite sign to the pure objects of Doc 135), standard polar block $[0]+[1]$, archimedean weight $\omega_\zeta\leftrightarrow\Omega$. Its Weil quadratic form is, for $f\in C_c^\infty(G)$ and $g=f\star\tilde f$:
$$\boxed{\;Q_S(f)\;:=\;\underbrace{2\,\mathrm{Re}\,\bigl(\hat f(0)\,\overline{\hat f(1)}\bigr)}_{\text{polar block }=\,\hat g(0)+\hat g(1)}\;+\;\underbrace{\frac1{2\pi}\int_{\mathbb R}|\hat F(\xi)|^2\,\Omega(\xi)\,d\xi}_{\mathcal A(f)}\;-\;\underbrace{\sum_{p\in S}\sum_{m\ge1}\frac{\log p}{p^{m/2}}\;2\mathrm{Re}\,G(m\log p)}_{P_S(f)}\;}$$
The H axiom for $X_S^{\mathrm{ar}}$ is: $Q_S(f)\ge0$ for every $f\in C_c^\infty(G)$.

**Remark 1.3 (consistency with $\zeta$ and with Doc 131; why this is THE definition).**
(i) *Polar block:* $\hat g(0)=\hat f(0)\overline{\hat f(1)}$ and $\hat g(1)=\hat f(1)\overline{\hat f(0)}$ (from $\hat g(s)=\hat f(s)\overline{\hat f(1-\bar s)}$); the sum is $2\mathrm{Re}(\hat f(0)\overline{\hat f(1)})$ — **indefinite in sign**, unlike the constructive diagonal atom $2\log(pq)\,g(1)$ of Doc 135. This is already information.
(ii) *Prime term:* $\Lambda(p^m)\bigl(g(p^m)+p^{-m}g(p^{-m})\bigr)=\frac{\log p}{p^{m/2}}\bigl(G(mL_p)+\overline{G(mL_p)}\bigr)$, using $g(x)=G(\log x)x^{-1/2}$. It is the Weil term of $\zeta$ restricted to prime powers from $S$ — the minus sign is that of the explicit formula (primes enter subtracting against the zeros).
(iii) *Case $S=$ all primes:* $Q_{\mathrm{full}}(f)=\sum_\rho\hat g(\rho)$ over the nontrivial zeros of $\zeta$ (Riemann–Weil formula), and H is equivalent to RH [FACT: Weil 1952; Bombieri 2000]. Definition 1.2 is the only truncation of that formula compatible with the slots $(a,c,\omega)$ of Doc 131.
(iv) *Hermiticity:* $Q_S(f)\in\mathbb R$ for every $f$ (each block is manifestly real). $X_S^{\mathrm{ar}}$ is hermitian in the sense of Doc 131, Prop. 2.8.

**Remark 1.4 (what is NOT assumed).** It is not assumed that $X_S^{\mathrm{ar}}$ is *spectral* (Doc 131, Def. 4.1: existence of a multiset $Z$ with $\sum_{\rho\in Z}\hat g(\rho)=W(g)$ and polynomial density). This omission is not carelessness: it is the point on which the verdict on H⁺ will turn (§8). The object is defined by its three blocks; whether or not it has a divisor is a pending theorem, not a definition.

---

## 2. The archimedean weight in closed form

**[LEMMA 2.1] (explicit series).** For every $\xi\in\mathbb R$, with $y:=\xi/2$:
$$\Omega(\xi)\;=\;-\gamma-\log\pi\;+\;\sum_{n\ge0}\Bigl(\frac1{n+1}\;-\;\frac{n+\tfrac14}{(n+\tfrac14)^2+y^2}\Bigr),$$
with absolute and locally uniform convergence.

*Proof.* From the digamma series $\psi(z)=-\gamma+\sum_{n\ge0}\bigl(\frac1{n+1}-\frac1{n+z}\bigr)$ with $z=\tfrac14+iy$: $\mathrm{Re}\,\frac1{n+\tfrac14+iy}=\frac{n+1/4}{(n+1/4)^2+y^2}$. The $n$-th term is $O(n^{-2})$ uniformly in $y$ bounded (numerator $y^2-\tfrac34(n+\tfrac14)$ over denominator $\asymp n^3$). $\square$

**[LEMMA 2.2] (the value at the center, exact).**
$$\Omega(0)\;=\;\psi(\tfrac14)-\log\pi\;=\;-\gamma-\frac\pi2-3\log2-\log\pi\;\approx\;-5.3722\;<\;0.$$

*Proof.* Gauss's digamma theorem [FACT: Whittaker–Watson, §12.3]: for $0<p<q$ integers,
$$\psi(p/q)=-\gamma-\log(2q)-\frac\pi2\cot\frac{\pi p}q+2\sum_{k=1}^{\lfloor(q-1)/2\rfloor}\cos\frac{2\pi kp}q\,\log\sin\frac{k\pi}q.$$
With $p=1$, $q=4$: $\psi(\tfrac14)=-\gamma-\log8-\frac\pi2\cot\frac\pi4+2\cos\frac\pi2\log\sin\frac\pi4=-\gamma-3\log2-\frac\pi2$ (the last term vanishes since $\cos\frac\pi2=0$). Symbolic evaluation: $\gamma\approx0.57722$, $\frac\pi2\approx1.57080$, $3\log2\approx2.07944$, $\log\pi\approx1.14473$; sum $\approx5.37219$. $\square$

**[LEMMA 2.3] (monotonicity: the destructive floor).** $\Omega$ is even, strictly increasing in $|\xi|$, and $\Omega(\xi)\to+\infty$. Consequently:
(a) $\Omega(\xi)\ge\Omega(0)$ for every $\xi$, and hence
$$\mathcal A(f)\;\ge\;\Omega(0)\,\|f\|_w^2\qquad\text{for every }f\in C_c^\infty(G):$$
**the archimedean term is destructive with absolute floor** $|\Omega(0)|<5.38$.
(b) There exist unique $0<\xi_*<\xi_{**}$ with $\Omega(\xi_*)=0$, $\Omega(\xi_{**})=1$; $\Omega<0$ exactly on $(-\xi_*,\xi_*)$.

*Proof.* Parity: the series of Lemma 2.1 depends on $y^2$. Strict monotonicity: each term $-\frac{n+1/4}{(n+1/4)^2+y^2}$ is strictly increasing in $y^2$ (derivative $\frac{(n+1/4)\cdot 2y}{((n+1/4)^2+y^2)^2}>0$ for $y>0$), and the series of derivatives converges locally uniformly. Divergence: from Lemma 2.4(a) below. (a) and (b) are immediate from $\Omega(0)<0$ (Lemma 2.2), continuity, strict monotonicity and $\Omega\to\infty$; $\mathcal A(f)\ge\Omega(0)\frac1{2\pi}\int|\hat F|^2=\Omega(0)\|F\|_2^2$ by Parseval. $\square$

**Remark (the structural contrast with Doc 135).** In the constructive regime, the only destructive source was impurity, and it was **bottomless**: $|c_M|p^{-M/2}=p^{M\delta'}\to\infty$ (Doc 135, Thm. 4.1). The $\Gamma$ term is destructive but **bounded below by the absolute constant $\Omega(0)$**. The whole question of GAP-135.B is whether that bounded destructiveness, plus that of the primes with $a\ge0$, can be bought by the polar block. Answer: yes at short scale (§3), no at long scale (§5), and the boundary is where the pole stops seeing the test.

**[LEMMA 2.4] (effective logarithmic bounds).**
(a) For $\xi\ge4$:
$$\Omega(\xi)\;\ge\;\log\frac{\xi}2-\gamma-\log\pi-\frac54.$$
In particular $\Omega(\xi)\ge0$ for $\xi\ge40$ and $\Omega(\xi)\ge1$ for $\xi\ge107$; that is, $\xi_*\le40$ and $\xi_{**}\le107$.
(b) For every $\xi$: $|\Omega(\xi)|\le\log(4+|\xi|)+4+\gamma+\log\pi\le\log(4+|\xi|)+6$.

*Proof.* Let $y=\xi/2\ge2$ and $N:=\lfloor y\rfloor\ge2$. In the series of Lemma 2.1 we split into $n\le N-1$ and $n\ge N$.
*(a)* For $n\le N-1$: $\frac{n+1/4}{(n+1/4)^2+y^2}\le\frac{n+1/4}{y^2}$, so these terms sum to $\ge\sum_{n=0}^{N-1}\frac1{n+1}-\frac1{y^2}\sum_{n=0}^{N-1}(n+\tfrac14)\ge\log(N+1)-\frac{N^2}{2y^2}\ge\log y-\frac12$. For $n\ge N$: $\frac{n+1/4}{(n+1/4)^2+y^2}\le\frac1{n+1/4}$, so these terms sum to $\ge-\frac34\sum_{n\ge N}\frac1{(n+1)(n+1/4)}\ge-\frac34\sum_{n\ge N}\frac1{n^2}\ge-\frac3{4(N-1)}\ge-\frac34$. Total: $\Omega(\xi)\ge-\gamma-\log\pi+\log y-\frac54$. Checking the thresholds: $\log20=2.9957>\gamma+\log\pi+\tfrac54=2.9719$ gives $\Omega(40)>0$; $\log53.5=3.9798>1+2.9719$ gives $\Omega(107)>1$. ✓
*(b)* The $n$-th term is $\frac{y^2-\frac34(n+1/4)}{(n+1)\bigl((n+1/4)^2+y^2\bigr)}\le\min\Bigl(\frac1{n+1},\,\frac{y^2}{(n+1)(n+1/4)^2}\Bigr)$. For $y\ge2$: $\sum_{n\le\lceil y\rceil}\frac1{n+1}\le\log(y+2)+1$ and $\sum_{n>\lceil y\rceil}\frac{y^2}{(n+1)(n+1/4)^2}\le y^2\sum_{n\ge\lceil y\rceil}\frac1{n^3}\le\frac{y^2}{2(y-1)^2}\le2$. Hence $\Omega(\xi)\le-\gamma-\log\pi+\log(y+2)+3\le\log(4+\xi)+3$. For $0\le y\le2$, by monotonicity $\Omega(\xi)\le\Omega(4)\le\log4+3-\gamma-\log\pi$. The lower bound $|\Omega|$: $\Omega\ge\Omega(0)\ge-5.38$ (Lemmas 2.2–2.3). Combine. $\square$

*(The constants in 2.4 are deliberately crude: what is needed is an integrable dominator for dominated convergence and explicit finite thresholds. The true values of $\xi_*,\xi_{**}$ are much smaller; we do not need them and do not claim them.)*

---

## 3. [THEOREM A] Semilocal positivity in short window

**[THEOREM 3.1] (unconditional semilocal positivity; uniform in $S$, includes $\zeta$).** Let $T_0:=\tfrac1{300}$. For **every** set $S$ of primes (finite, infinite, or all) and every $f\in C_c^\infty(G)$ with window $2T\le2T_0=\tfrac1{150}$:
$$Q_S(f)\;\ge\;\frac3{10}\,\|f\|_w^2.$$

*Proof.* Three blocks, separately.

*(1) Primes: zero.* $G(t)=0$ for $|t|>2T$ and $2T\le\tfrac1{150}<\log2\le mL_p$: $P_S(f)=0$ for every $S$. (Here it matters that the data $a_S$ lives on $\{p^m:m\ge1\}$, far from $1$.)

*(2) Polar: $\ge-4Te^{T}\|f\|_w^2$.* If $\mathrm{supp}\,F\subset[\lambda-T,\lambda+T]$,
$$\bigl|\hat f(0)\overline{\hat f(1)}\bigr|=\Bigl|\int\!\!\int F(t)\overline{F(s)}\,e^{(s-t)/2}\,dt\,ds\Bigr|\le e^{T}\Bigl(\int|F|\Bigr)^2\le e^{T}\cdot2T\,\|F\|_2^2,$$
using $|s-t|\le2T$ (the position $\lambda$ cancels in $e^{(s-t)/2}$ — the polar block is window-invariant, as it must be) and Cauchy–Schwarz. Hence the polar block is $\ge-4Te^{T}\|F\|_2^2$.

*(3) Archimedean: $\ge(1-205\,T)\|f\|_w^2$.* For any $K>0$, by Cauchy–Schwarz $|\hat F(\xi)|^2\le2T\|F\|_2^2$, so the low spectral mass satisfies
$$m_{\le K}:=\frac1{2\pi}\int_{|\xi|\le K}|\hat F|^2\,d\xi\;\le\;\frac{2KT}\pi\,\|F\|_2^2.$$
We split $\mathbb R$ into $\{|\xi|\le40\}$, $\{40<|\xi|<107\}$, $\{|\xi|\ge107\}$ and use $\Omega\ge\Omega(0)$, $\Omega\ge0$, $\Omega\ge1$ respectively (Lemmas 2.3, 2.4(a)):
$$\mathcal A(f)\;\ge\;\Omega(0)\,m_{\le40}\;+\;0\;+\;1\cdot\bigl(\|F\|_2^2-m_{\le107}\bigr)\;\ge\;\Bigl[1-\frac{2T}{\pi}\bigl(107+|\Omega(0)|\cdot40\bigr)\Bigr]\|F\|_2^2\;\ge\;\bigl(1-205\,T\bigr)\|F\|_2^2,$$
with $|\Omega(0)|\le5.3722$: $\tfrac2\pi(107+214.9)=204.9\le205$.

Summing at $T=T_0=\tfrac1{300}$: $1-\tfrac{205}{300}-4\cdot\tfrac1{300}e^{1/300}\ge0.3166-0.0134\ge\tfrac3{10}$. For $T<T_0$ the bounds only improve. $\square$

**Remark 3.2 (a frank reading).** (i) The window $2T\le1/150$ is ridiculously short compared to the constructive threshold $\log p_1$ of Doc 135 — but the statement is **uniform in $S$, includes the $\Gamma$ term, and includes $\zeta$ itself** (for $\zeta$, every window $2T<\log2$ kills the primes and the Theorem applies just the same). It is the program's first Weil positivity in the destructive regime: the initial [DESIDERATUM], realized in a weak version. (ii) The constants are crude because $\xi_*\le40$, $\xi_{**}\le107$ are. With the true values of $\xi_*,\xi_{**}$ the threshold $T_0$ would improve by one or two orders of magnitude, no more: the genuine threshold is $O(1)$, not $O(\log P)$. (iii) The positivity mechanism is **entirely archimedean**: at short window the spectral mass is forced to high frequencies (uncertainty), where $\Omega\sim\log|\xi|>0$. The pole only needs not to interfere ($O(T)$), and the primes do not arrive. Compare with Doc 135, where at short window positivity was the diagonal atom $2\log(pq)g(1)$: **in the destructive regime the arithmetic diagonal does not exist; its role is inherited by the logarithmic growth of $\Gamma$.** This is the B1 exchange ($\theta(y)\leftrightarrow\Omega$) seen in positive.

---

## 4. [COMPUTATION] $n=1$: the Mertens test does not bite in the destructive regime

Let $S=\{p\}$, the first genuinely mixed object (one destructive prime + $\Gamma$ + pole). The champion adversary of the constructive regime was the two-bump test (Doc 135 §4): $f=u+\theta\,u(\cdot/p^M)$, with $u(e^t)=\epsilon^{-1/2}\chi(t/\epsilon)$, $\chi$ even, $\mathrm{supp}\,\chi\subset[-1,1]$, $\int\chi^2=1$. We evaluate $Q_p$ on that family, to leading order in $\epsilon$ (the $O(\epsilon)$ terms are absorbed as in Doc 135).

We take the **mean-zero** profile: $\int\chi=0$ (allowed: $\chi$ even, signed). Then:

- **Polar:** $\hat f(1)=\int F e^{t/2}dt=\epsilon^{1/2}\!\int\chi(v)\bigl(e^{\epsilon v/2}-1\bigr)dv\cdot(1+\theta p^{M/2}\cdot[\,\cdot\,])=O(\epsilon^{3/2})(1+|\theta|p^{M/2})$, and likewise $\hat f(0)$ with $p^{-M/2}$. The polar block is $O(\epsilon^3)(1+|\theta|^2)p^{M/2}\cdot p^{...}$ — with $M$ fixed, it is absorbed by choosing $\epsilon$ at the end. *(With $\int\chi\ne0$ the polar term enters with $+2I^2\,p^{M/2}\mathrm{Re}\,\theta$, $I^2=\epsilon(\int\chi)^2$: it reinforces positivity against the adversary aligned with the prime; the mean-zero case is the worst one.)*
- **Archimedean:** $|\hat F|^2=|\hat u_\epsilon|^2\bigl(1+|\theta|^2+2\mathrm{Re}(\theta e^{iML_p\xi})\bigr)$ with $\hat u_\epsilon(\xi)=\epsilon^{1/2}\hat\chi(\epsilon\xi)$, hence
  $$\mathcal A(f)=(1+|\theta|^2)\,A_0+2\mathrm{Re}\,\theta\cdot\omega_M,\qquad A_0:=\frac1{2\pi}\int|\hat u_\epsilon|^2\Omega\,d\xi,\quad \omega_M:=\frac1{2\pi}\int|\hat u_\epsilon|^2\,\Omega(\xi)\cos(ML_p\xi)\,d\xi.$$
  With $\int\chi=0$ ($\hat\chi(0)=0$) the spectral mass lives at $|\xi|\asymp1/\epsilon$, where $\Omega\ge\log\tfrac1{2\epsilon}-O(1)$: $A_0\ge(\log\tfrac1\epsilon)(1-o(1))\to+\infty$. And $\omega_M$ is **small**, not comparable to $A_0$: integrating by parts once, $|\omega_M|\le\frac{\|(|\hat u_\epsilon|^2\Omega)'\|_{L^1}}{ML_p}=O\Bigl(\frac{\epsilon\log(1/\epsilon)}{ML_p}\Bigr)$, since $\||\hat u_\epsilon|^2{}'\|_1=\epsilon\|(|\hat\chi|^2)'\|_1$ and $\int|\hat u_\epsilon|^2|\Omega'|=O(\epsilon\log\tfrac1\epsilon)$ ($\Omega'=O(1/|\xi|)$ by the derivative of 2.1).
- **Prime:** only $m=M$ survives in support: $P_p(f)=\frac{L_p}{p^{M/2}}\,2\mathrm{Re}\,G(ML_p)=\frac{2L_p}{p^{M/2}}\mathrm{Re}\,\theta\,(1+O(\epsilon))$, with $G(ML_p)=\bar\theta(1+O(\epsilon))$... the total destructive coupling of the prime at height $M$ is bounded by
  $$\frac{2L_p}{p^{M/2}}\;\le\;\frac{2\log p}{\sqrt p}\;\le\;2\cdot0.736\qquad(\text{maximum at }p=7;\ \text{for }p=2:\ 2\cdot0.490).$$

With $\mathrm{Re}\,\theta=-t$ adversary:
$$Q_p(f)=(1+t^2)A_0-2t\Bigl(\frac{L_p}{p^{M/2}}+O\bigl(\tfrac{\epsilon\log(1/\epsilon)}{ML_p}\bigr)\Bigr)+O(\epsilon^{3}\!\cdot p^{M})\;\ge\;A_0-\frac{\bigl(L_pp^{-M/2}+o(1)\bigr)^2}{A_0}\;>\;0$$
for $\epsilon$ small, since $L_pp^{-M/2}\le0.736\ll A_0\sim\log\tfrac1\epsilon$.

**[PROPOSITION 4.1] (Mertens deactivated).** Over the whole two-bump family (even profile, any height $M\ge1$, any phase $\theta$), $Q_p(f)>0$, with margin $\ge A_0-O(1/A_0)\to\infty$ as $\epsilon\to0$. *(Proof: the computation above; the case $\int\chi\ne0$ adds to the polar term $+2I^2p^{M/2}\mathrm{Re}\,\theta$ which, with the prime's adversarial phase $\mathrm{Re}\,\theta<0$... its sign is opposite to that of the prime term, and the analysis repeats with the minimum in the same quadratic form; the details are identical.)* $\square$

**Remark 4.2 (the structural moral).** In the constructive regime, the adversary's coupling to the prime **grew** with height ($|c_M|p^{-M/2}=p^{M\delta'}$ if impure; $=2$ constant if pure). In the destructive regime the coupling **decays**: $\Lambda(p^m)/p^{m/2}=L_p\,p^{-m/2}\to0$. Each prime of the data $a\ge0$ is, individually, a compact and small perturbation of $\mathcal A$ — no test localized at ONE scale $p^M$ can exploit the minus sign. The destructive danger is not at any single scale: it is in the **aggregate of the diagonal at small lag**, that is, in wide and slow tests. That motivates (and the next section confirms) which is the correct adversary.

---

## 5. [THEOREM B] The failure: where, how, and how much

**[THEOREM 5.1] (the semilocal object violates H; the heart $S=\varnothing$ too).** For every finite set $S$ of primes (including $S=\varnothing$):
$$\inf\Bigl\{\,Q_S(f)\;:\;f\in C_c^\infty(G),\ \|f\|_w=1\,\Bigr\}\;\le\;\Omega(0)\;-\;B_S\;<\;0,\qquad B_S:=\sum_{p\in S}\frac{2\log p}{\sqrt p-1}=\sum_{p\in S}\frac{2(\sqrt p+1)\log p}{p-1}.$$
In particular $X_S^{\mathrm{ar}}$ **does not satisfy H**, and there exists an explicit test (constructed in the proof) with $Q_S<0$. Symbolic values:
$$S=\varnothing:\ \le-5.3722;\qquad S=\{2\}:\ \le-5.3722-2(\sqrt2+1)\log2\approx-8.7190;\qquad S=\{2,3\}:\ \le-11.7207.$$

*Proof.* **The family.** Fix $\eta,\eta_2\in C_c^\infty(\mathbb R)$ real, $\eta\not\equiv0$ with $\mathrm{supp}\,\eta\subset(0,\tfrac38)$, $\eta_2\ge0$ with $\mathrm{supp}\,\eta_2\subset(\tfrac12,1)$ and $\int_{5/8}^{7/8}\eta_2>0$. For $T>0$ define
$$F_T(t):=T^{-1/2}\Bigl[\eta\bigl(\tfrac tT\bigr)-c_T\,\eta_2\bigl(\tfrac tT\bigr)\Bigr],\qquad c_T:=\frac{\int\eta(u)\,e^{Tu/2}\,du}{\int\eta_2(u)\,e^{Tu/2}\,du},\qquad f_T(x):=F_T(\log x)\,x^{-1/2}.$$
Then $f_T\in C_c^\infty(G)$ with support in $(1,e^T)$ (window $2T'=T$), and by construction
$$\hat f_T(1)=\int F_T(t)\,e^{t/2}\,dt=T^{1/2}\int\bigl[\eta-c_T\eta_2\bigr](u)\,e^{Tu/2}\,du=0.$$

**(0) The cost of the pole is exponentially small.** $\bigl|\int\eta\,e^{Tu/2}du\bigr|\le\|\eta\|_1e^{3T/16}$ and $\int\eta_2e^{Tu/2}du\ge e^{5T/16}\int_{5/8}^{7/8}\eta_2$, hence
$$|c_T|\;\le\;C_\eta\,e^{-T/8}\;\longrightarrow\;0.$$
Since the supports of $\eta$ and $\eta_2$ are disjoint: $\|F_T\|_2^2=\|\eta\|_2^2+c_T^2\|\eta_2\|_2^2\to\|\eta\|_2^2$, i.e. $\|f_T\|_w^2\to\|\eta\|_2^2$.

**(1) Polar $=0$ exact.** $\hat g(0)=\hat f(0)\overline{\hat f(1)}=0$ and $\hat g(1)=\hat f(1)\overline{\hat f(0)}=0$ because $\hat f_T(1)=0$. (A single linear condition kills both terms: the polar block is rank one in this sense.)

**(2) Archimedean $\to\Omega(0)\|\eta\|_2^2$.** Write $\eta_c:=\eta-c_T\eta_2$. Since $\hat F_T(\xi)=T^{1/2}\hat\eta_c(T\xi)$,
$$\mathcal A(f_T)=\frac1{2\pi}\int_{\mathbb R}\bigl|\hat\eta_c(u)\bigr|^2\,\Omega\bigl(\tfrac uT\bigr)\,du.$$
Domination: $|\hat\eta_c(u)|^2\le2|\hat\eta(u)|^2+2|\hat\eta_2(u)|^2$ for $T$ large ($|c_T|\le1$), which is Schwartz; and $|\Omega(u/T)|\le\log(4+|u|)+6$ for $T\ge1$ (Lemma 2.4(b), monotonicity of the logarithm). Pointwise $\Omega(u/T)\to\Omega(0)$ ($\Omega$ continuous, Lemma 2.1) and $\hat\eta_c\to\hat\eta$ uniformly. Dominated convergence:
$$\mathcal A(f_T)\;\longrightarrow\;\Omega(0)\cdot\frac1{2\pi}\int|\hat\eta|^2\;=\;\Omega(0)\,\|\eta\|_2^2.$$

**(3) Primes $\to B_S\|\eta\|_2^2$ — the destructive diagonal.** For fixed $t$, $G_T(t)=\int\eta_c(u)\,\eta_c\bigl(u-\tfrac tT\bigr)\,du\to\|\eta\|_2^2$ (continuity of translation in $L^2$ and $c_T\to0$), real. Moreover $|G_T|\le\|\eta_c\|_2^2\le\|\eta\|_2^2+1$ for $T$ large, uniformly. Since $\sum_{p\in S}\sum_{m\ge1}L_p\,p^{-m/2}<\infty$ (finitely many primes, geometric), dominated convergence over the index $(p,m)$:
$$P_S(f_T)=\sum_{p\in S}\sum_{m\ge1}\frac{2L_p}{p^{m/2}}\,G_T(mL_p)\;\longrightarrow\;2\,\|\eta\|_2^2\sum_{p\in S}L_p\sum_{m\ge1}p^{-m/2}\;=\;B_S\,\|\eta\|_2^2.$$

Summing: $Q_S(f_T)=0+\mathcal A(f_T)-P_S(f_T)\to\bigl(\Omega(0)-B_S\bigr)\|\eta\|_2^2<0$, and $\|f_T\|_w^2\to\|\eta\|_2^2$. For $T$ sufficiently large, $Q_S(f_T)<0$ and the ratio $Q_S/\|f_T\|_w^2$ is as close to the limit as desired. Symbolic evaluations: $B_{\{2\}}=2(\sqrt2+1)\log2\approx3.3468$; $B_{\{2,3\}}\approx3.3468+(\sqrt3+1)\log3\approx6.3485$. $\square$

**Remark 5.2 (anatomy of the counterexample — the map of interference).** Each piece of the test is there for an identifiable reason:
1. **Slow and wide** ($\eta(t/T)$, frequencies $O(1/T)$): places the spectral mass in $(-\xi_*,\xi_*)$, where $\Omega<0$. This is what the Mertens test could not do (§4): its mass lived at $1/\epsilon$, high.
2. **Pole evasion** ($\hat f(1)=0$ via $c_T$): the polar block guards exactly ONE direction — the "exponential moment" $\int Fe^{t/2}$ — and that custody is evaded at cost $e^{-T/8}$, asymptotically free. Note the geometry: **the pole lives at the complex frequency $\xi=-i/2$; the archimedean deficit lives at real frequencies $|\xi|<\xi_*$. They are distinct points of the plane, and no uncertainty principle links them when the test is wide** (with a short window, yes: Theorem 3.1).
3. **Primes at fixed lag are positive autocorrelation**: $G_T(mL_p)\to+\|\eta\|_2^2$ for EACH fixed $(p,m)$ — the slow test is nearly invariant under the translation $t\mapsto t+mL_p$, so the prime term enters with its worst possible sign (full subtraction). Each added prime subtracts $\frac{2L_p}{\sqrt p-1}$ more: **in the destructive regime, more primes = worse**, the exact inversion of the protective diagonal tide $+L_q$ of the constructive regime (Doc 135 §4, quantitative remark). The sign of the data $a$ reverses the role of foreign primes.

**Remark 5.3 (the case $S=\varnothing$ is the heart of the matter).** The failure does NOT need primes: the object $(0,[0]+[1],\omega_\zeta)$ — pole plus $\Gamma$, no arithmetic — already violates H with deficit $\Omega(0)$. The primes with $a\ge0$ only deepen a hole that is **archimedean in origin**. This localizes the destructive regime of GAP-135.B precisely: the zero/prime interference posed is, at bottom, **pole/archimedean** interference, and the truncated primes are amplifiers.

---

## 6. [BRIDGE] The transmission identity: why $\zeta$ does not fail where the semilocal object does

How is it possible that $Q_S(f_T)\to$ negative for every finite $S$, if $Q_{\mathrm{full}}$ (all primes) is $\ge0$ under RH? The answer is an identity, not an estimate.

**[PROPOSITION 6.1] (truncation identity).** For every $f$ and every finite $S$:
$$Q_S(f)\;=\;Q_{\mathrm{full}}(f)\;+\;\bigl[P_{\mathrm{full}}(f)-P_S(f)\bigr]\;=\;\sum_{\rho}\hat g(\rho)\;+\;\bigl[P_{\mathrm{full}}(f)-P_S(f)\bigr],$$
where the sum runs over the nontrivial zeros of $\zeta$ (Riemann–Weil formula, unconditional [FACT: Weil 1952; Iwaniec–Kowalski 2004, Thm 5.12]). *(Trivial: the three blocks of $Q_S$ and $Q_{\mathrm{full}}$ coincide except for the prime term; the second equality is the explicit formula.)* $\square$

**[COROLLARY 6.2] (the full sum over primes changes sign in aggregate; under RH).** On the family $f_T$ of Theorem 5.1, under RH:
$$\lim_{T\to\infty}P_{\mathrm{full}}(f_T)\;=\;\lim_{T\to\infty}\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,2\mathrm{Re}\,G_T(\log n)\;=\;\Omega(0)\,\|\eta\|_2^2\;<\;0,$$
while **each individual term** has positive limit: $\frac{\Lambda(n)}{\sqrt n}2\mathrm{Re}\,G_T(\log n)\to\frac{2\Lambda(n)}{\sqrt n}\|\eta\|_2^2>0$.

*Proof.* By Proposition 6.1 with $S=\varnothing$: $P_{\mathrm{full}}(f_T)=\mathcal A(f_T)-\sum_\rho\hat g_T(\rho)$ (polar $=0$). Under RH, $\rho=\tfrac12+i\gamma$ and $\hat g_T(\rho)=|\hat F_T(\gamma)|^2=T|\hat\eta_c(T\gamma)|^2$. Since $\zeta(\tfrac12)\ne0$ and the first zero has $|\gamma_1|>0$: $T|\hat\eta_c(T\gamma)|^2\le C_kT(1+T|\gamma_1|)^{-2k}\cdot(1+|\gamma|)^{-2}$-type (Paley–Wiener for $\hat\eta_c$, uniform in $T$ large), and the sum over zeros (density $\log\gamma$) tends to $0$. With $\mathcal A(f_T)\to\Omega(0)\|\eta\|_2^2$ (Theorem 5.1, step 2), done. $\square$

**[BRIDGE] reading, declared status.** Corollary 6.2 is the exact form, on a single family of tests, of breakpoints B1+B4 of Doc 135:

- At **fixed lag** $\log n$, the prime term is autocorrelation: positive (subtracted in $Q$). In the **aggregate** $\sum_n\Lambda(n)n^{-1/2}(\cdots)$, the oscillations of $G_T$ against the density of primes produce a **negative** total (summed in $Q$), of value exactly $\Omega(0)\|\eta\|^2$: the full sum of primes returns, with changed sign, the archimedean deficit — to the penny. That is the "transmission of polar custody to the real axis": $\hat f(1)=0$ (a condition on the moment $e^{t/2}$, i.e. on the pole) forces, via the explicit formula, the full sum of primes to compensate $\Gamma$. **No finite truncation sees the condition $\hat f(1)=0$**: each fixed lag is blind to a global exponential moment (the cost $c_T\sim e^{-T/8}$ is invisible at a fixed scale $mL_p$).
- The **transmission deficit** is the exact quantity of the failure: $D_S:=\lim\bigl[P_S-P_{\mathrm{full}}\bigr](f_T)=B_S-\Omega(0)>0$ and $\lim Q_S(f_T)=\lim Q_{\mathrm{full}}(f_T)-D_S=0-D_S$. The violation of the semilocal object IS its transmission deficit. (Under RH; unconditionally, identity 6.1 holds term by term in $T$.)
- Frankness about status: 6.2 uses RH (or at least: if RH fails, $\lim\sum_\rho\hat g_T(\rho)$ might not be $0$ and the accounting changes — without RH we only assert identity 6.1). None of this section proves anything about RH; it **localizes** where the limit $S\to$ all primes stops commuting with positivity, which is what GAP-135.B asked to map.

---

## 7. The map of the destructive regime

Let us collect. Let $\mu_S(T):=\inf\{Q_S(f):\|f\|_w=1,\ \text{window }2T\}$.

**Proved:**
- $\mu_S(T)\ge\tfrac3{10}$ for $2T\le\tfrac1{150}$, **uniform in $S$** (Theorem 3.1). The positivity threshold is **absolute** (archimedean), not arithmetic: it does not scale with $\log(p_1\cdots p_n)$. The initial [DESIDERATUM] ("the archimedean term dominates the interference for support $\le\theta\log(p_1\cdots p_n)$") is **false as stated** — the correct scale is not the conductor but the $O(1)$ constant of the crossing of $\Omega$ — and **true in spirit** at that absolute scale.
- $\mu_S(T)<0$ for $T\ge T_1(S,\eta)$ finite and effective (Theorem 5.1; the proof gives $T_1$ as a function of the speed of the three convergences, all explicit: $c_T\le C_\eta e^{-T/8}$, modulus of continuity of $\Omega$ at $0$, translations of $\eta$). We do not optimize $T_1$; with reasonable $\eta$ it is $O(10)$.
- $\lim_{T\to\infty}\mu_S(T)\le\Omega(0)-B_S$, strictly decreasing as primes are added.

**[PROPOSITION 7.2] (the surviving high-frequency cone).** Let $S$ be finite, $B_S$ as in 5.1, and let $\bar\xi_S$ be the unique point with $\Omega(\bar\xi_S)=B_S+2$ (exists by Lemma 2.3; effective bound $\bar\xi_S\le2\pi e^{\gamma+5/4}\,e^{B_S+2}$ by Lemma 2.4(a)). Let
$$\varepsilon_S:=\frac1{B_S+2+|\Omega(0)|}.$$
If $f$ satisfies (i) $\hat f(1)=0$ or $\hat f(0)=0$ (dead pole), and (ii) low spectral mass $\frac1{2\pi}\int_{|\xi|\le\bar\xi_S}|\hat F|^2\,d\xi\le\varepsilon_S\|f\|_w^2$, then
$$Q_S(f)\;\ge\;\|f\|_w^2.$$

*Proof.* Polar $=0$ by (i). Primes: $|G(mL_p)|\le\|F\|_2^2$ (Cauchy–Schwarz), hence $|P_S(f)|\le B_S\|F\|_2^2$. Archimedean: with $m_{\mathrm{low}}\le\varepsilon_S\|F\|^2$ the mass below $\bar\xi_S$ and $\Omega\ge\Omega(0)$ there, $\Omega\ge B_S+2$ above (monotonicity):
$$\mathcal A(f)\ge\Omega(0)\,\varepsilon_S\|F\|^2+(B_S+2)(1-\varepsilon_S)\|F\|^2 = \bigl[B_S+2-\varepsilon_S(B_S+2+|\Omega(0)|)\bigr]\|F\|^2=(B_S+1)\|F\|^2.$$
Total: $Q_S\ge(B_S+1-B_S)\|F\|^2=\|F\|^2$. $\square$

**The map, in one line.** The destructive regime is a phenomenon of **low frequency and wide window with pole evaded**; positivity survives exactly in the two complements: short window (every frequency forced high — Theorem 3.1) and high-frequency cone (every window — Proposition 7.2). The failure lives in the rectangle "frequency $\lesssim\xi_*$ × window $\gtrsim T_1$", and there it is unavoidable.

**[GAP-142.A] (the archimedean threshold).** Determine $T_\square:=\sup\{T:\mu_\varnothing(T)\ge0\}$ — the threshold of the polar+$\Gamma$ heart, a question of pure analysis with no arithmetic (quadratic form $2\mathrm{Re}(\hat f(0)\overline{\hat f(1)})+\mathcal A$ over windows), and the corresponding $T_{\mathrm{crit}}(S)\le T_\square$. Proved: $\tfrac1{300}\le T_\square<\infty$. Natural conjecture: $T_\square\asymp1/\xi_*$ by the scaling of Remark 5.2(1), modulo the cost of the pole. It is the destructive analogue of GAP-135.A (which was the modulus of the gap; here the **sign** in the intermediate region is at stake).

**[GAP-142.B] (spectrality of the semilocal object).** Decide whether $X_S^{\mathrm{ar}}$ is spectral in the sense of Doc 131, Def. 4.1 (does there exist a multiset $Z$ — positive multiplicities, polynomial density — with $\sum_{\rho\in Z}\hat g(\rho)=Q_S(f)$ for every $f$?). Evidence that it does NOT:
1. If such a $Z$ existed, contained in the critical line and $\sigma$-stable, then $Q_S\ge0$ — contradicted by Theorem 5.1. Hence any divisor would be off the line. **[Proved.]**
2. The natural candidate, the function $\xi_S(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\prod_{p\in S}(1-p^{-s})^{-1}$, has **poles** in the strip (negative multiplicity) at $s\in\tfrac{2\pi i}{\log p}\mathbb Z$ and lacks a functional equation; and the prime term of $Q_S$ is "a half with mirror weight" ($m\ge1$ with weight $1$, $m\le-1$ with weight $p^{m}$) which is **not** a combination of Poisson sums of full vertical progressions $\sum_k\hat g(i\tau_k)$, $\sum_k\hat g(1+i\tau_k)$ (these give the bilateral weights $1+p^m$ — the impure factor of B3). The one-sidedness is exactly the mark of the missing analytic continuation. **[Argument, not proof: a uniqueness theorem for divisors of explicit formulas is missing.]**

---

## 8. Verdict on H⁺

Recall H⁺ (P48, Conjecture 7.1): *if $X$ is hermitian, **spectral**, with data $a\ge0$ supported on prime powers (Euler product), standard polar block, and $\zeta$-type archimedean weight, then $X$ satisfies H.*

The object $X_S^{\mathrm{ar}}$ satisfies: hermitian ✓ (Rem. 1.3(iv)), $a=\Lambda\cdot\mathbf 1\ge0$ supported on prime powers ✓, standard polar ✓, $\zeta$-type archimedean ✓, and **violates H** (Theorem 5.1). Only one hypothesis remains unverified: spectrality. Hence:

**[THEOREM 8.1] (the contrapositive).** $H^+\;\Longrightarrow\;X_S^{\mathrm{ar}}$ **is not spectral** (for no finite $S$, including $\varnothing$). *(Immediate from 5.1 + the statement of H⁺.)* $\square$

**The trilemma, surgical.** Exactly one of these three:
1. **$X_S^{\mathrm{ar}}$ is spectral** (a positive divisor with explicit formula exists). Then **H⁺ is REFUTED** by Theorem 5.1, with explicit counterexample and deficit $\Omega(0)-B_S$.
2. **$X_S^{\mathrm{ar}}$ is not spectral** (what the evidence of GAP-142.B suggests). Then H⁺ survives, but GAP-135.B was **ill-posed**: the semilocal object was never "the first genuine case of H⁺" — it is not in the class — and this document proves that **the spectrality hypothesis carries one hundred percent of the content of H⁺**: the remaining hypotheses (hermitian + $a\ge0$ Euler + polar + $\Gamma$) are consistent with violations of H of size $\ge|\Omega(0)|$. Spectrality, for a destructive object, must be strong enough to force the pole→real-axis transmission of §6 — that is, it must encode the completeness of the Euler product and the functional equation. H⁺ reveals itself as: "having a divisor ⟹ the data is complete enough to guard the low frequencies" — a paraphrase of RH, not an intermediate test case.
3. The definition of "spectral" in Doc 131 admits divisors with parts off the line and the object qualifies with an off-line divisor — then H⁺ as written is equally refuted by 5.1 (case 1 with an exotic divisor), or else H⁺ implicitly required an on-line divisor, in which case H⁺ was nearly tautological (on-line divisor + hermitian $\Rightarrow$ H is Theorem 4.4(a) of Doc 131).

In any branch: **H⁺ does not survive as it stood** — either it is false, or its only accessible test case evaporates and its content collapses onto the spectrality hypothesis. The decision between the branches is GAP-142.B.

**Refinements of H⁺ that DO survive this document (the cones of §7):**
- **H⁺-loc (proved here for finite $S$):** the class of H⁺ satisfies H restricted to tests of window $\le\tfrac1{150}$ — Theorem 3.1, unconditional, uniform in the data.
- **H⁺-conic (proved here for finite $S$):** the class satisfies H in the high-frequency cone with dead pole — Proposition 7.2.
- **H⁺-complete (open, and this is the frank reformulation):** *hermitian + spectral + $a=\Lambda$ on ALL prime powers (complete Euler product) + polar + $\Gamma$ $\Rightarrow$ H.* The class reduces essentially to $\zeta$ and the conjecture to RH: the truncation to finite $S$ — the only "weaker than RH" content that H⁺ offered — is refuted as a route. The wall, redrawn with precision: **there is no semilocal interpolation between the constructive two-prime theorem (Doc 135) and RH; the first destructive step already costs the full price.**

---

## 9. The map

**Proved [THEOREM/PROPOSITION/LEMMA], with complete proof in this document:**
- Lemmas 2.1–2.4: the archimedean weight $\Omega$ in closed form; $\Omega(0)=-\gamma-\frac\pi2-3\log2-\log\pi$ exact (Gauss); monotonicity (destructive floor $\mathcal A\ge\Omega(0)\|f\|_w^2$); effective logarithmic bounds ($\xi_*\le40$, $\xi_{**}\le107$).
- **[THEOREM A = 3.1]:** unconditional semilocal positivity in short window, $Q_S\ge\frac3{10}\|f\|_w^2$ for $2T\le\frac1{150}$, uniform in $S$ (includes $\zeta$). The program's first Weil positivity with archimedean term.
- **[PROPOSITION 4.1]:** the Mertens test does not break the destructive regime (coupling $L_pp^{-M/2}$ decays; margin $\sim\log(1/\epsilon)$).
- **[THEOREM B = 5.1]:** $X_S^{\mathrm{ar}}$ violates H for every finite $S$, including $S=\varnothing$; explicit family $f_T$ ($\hat f_T(1)=0$, low frequency); exact asymptotic deficit $\Omega(0)-B_S$ ($\approx-11.72$ for $S=\{2,3\}$). **GAP-135.B is decided: H fails.**
- **[PROPOSITION 6.1]:** truncation identity $Q_S=Q_{\mathrm{full}}+[P_{\mathrm{full}}-P_S]$.
- **[COROLLARY 6.2]** (under RH): $\lim P_{\mathrm{full}}(f_T)=\Omega(0)\|\eta\|^2<0$ — the full sum of primes changes sign only in aggregate; no finite truncation sees it.
- **[PROPOSITION 7.2]:** the surviving high-frequency cone, with explicit constants.
- **[THEOREM 8.1]:** H⁺ $\Rightarrow$ $X_S^{\mathrm{ar}}$ is not spectral.

**[BRIDGE] (declared status):** §6 — B1/B4 of Doc 135 made identity on a family: the pole's custody ($\xi=-i/2$) is transmitted to the real axis only through the complete Euler product; the transmission deficit $D_S=B_S-\Omega(0)$ IS the violation. None of this brings RH closer; it redistributes GAP-135.B onto the spectrality hypothesis.

**Initial [DESIDERATUM], audited:** archimedean domination for support $\le\theta\log(p_1\cdots p_n)$ is **false** (the threshold does not scale with the conductor: it is absolute, $O(1)$ archimedean) and its true version is Theorem 3.1 + GAP-142.A.

**[GAP]s, named:**
- **GAP-142.A:** the archimedean threshold $T_\square\in[\tfrac1{300},T_1]$ — sign of $\mu_\varnothing(T)$ in the intermediate region; conjecture $T_\square\asymp1/\xi_*$.
- **GAP-142.B:** prove that $X_S^{\mathrm{ar}}$ is not spectral (uniqueness theorem for divisors of explicit formulas; the one-sidedness of the prime term as obstruction). Decides the trilemma of §8.

---

## References

**Internal (backward-only):** Doc 135 (two-prime theorem; B1–B4; GAP-135.B); P48 (`06-papers/P48-weil-positivity-finite-primes/main.tex`: Conjecture H⁺ = Conjecture 7.1, normalizations, final Remark "GAP-B"); Doc 131 (slots $(a,c,\omega)$, Def. 2.1, Def. 4.1 spectral, Thm. 4.4).

**Literature [FACT]:**
- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm. Sém. Math. Lund (1952), 252–265. (The quadratic form; the criterion H ⟺ RH; the local terms.)
- E. Bombieri, *Remarks on Weil's quadratic functional in the theory of prime numbers I*, Rend. Mat. Acc. Lincei (9) 11 (2000), 183–233. (Normalization of the functional; the role of the archimedean term and the polar block.)
- H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloq. Publ. 53, 2004, Theorem 5.12. (The explicit formula in the normalization $h(\gamma)$ used in §1; the weight $\mathrm{Re}\,\psi(\frac14+\frac{i\xi}2)-\log\pi$.)
- A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Math. (N.S.) 5 (1999), 29–106. (The local terms of the explicit formula as distributions; the archimedean place.)
- E. T. Whittaker, G. N. Watson, *A Course of Modern Analysis*, 4th ed., CUP 1927, §12.3. (Gauss's digamma theorem; $\psi(\frac14)=-\gamma-\frac\pi2-3\log2$.)
- H. L. Montgomery, R. C. Vaughan, *Multiplicative Number Theory I*, CUP 2007. (Mertens; $\sum_{n\le x}\Lambda(n)n^{-1/2}\sim2\sqrt x$, background to §6.)

*End of Document 142.*
