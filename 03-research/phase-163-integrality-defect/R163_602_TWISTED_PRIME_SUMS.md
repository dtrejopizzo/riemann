# R163_602 — Local Weil positivity from the prime side: twisted prime sums, Selberg, Levinson–Conrey

* No numerics were run. No file other than this one was edited. No label of record moves.*
*Inputs: R163_401 (§4.8 $(\star_{\rm cell})$, Rem 4.8a, Cor 4.10a) and R163_402 (Thm 4, Landau ceiling).
Corpus check: NG-B1 and CIR-2 (MAP_1_WALLS, `NO-GO-LIST.md:62-65, 246`) already list Levinson–Conrey as "aggregate, not individual".
The record's Kreĭn-indeterminacy reformulation (phase 155, round 5) is the global form of §1.3 below. This memo adds three things:
the local version, the Bombieri–Hejhal falsifier, and the mean-value/Landau duality (§4.3).*

Labels: **PROVED**, **PROVED-CITED**, **ARGUED**, **NO-GO** (a route shown not to deliver the target; the reason is proved or cited).

## Outcome first

| item | statement | label |
|---|---|---|
| 1.2 | localisation formula for $W_T(g\cos\gamma u)$ | PROVED |
| 2.1 | $P_{\rm loc}$ in the double-log range $4.16\,e^{T}\le\log(\gamma/2\pi)-O(1)$ | PROVED |
| 2.2 | at the Landau window, $P_{\rm loc}$ needs square-root cancellation in $\sum_{n<\gamma}\Lambda(n)n^{-1/2-i\gamma}$ | PROVED (reduction) |
| 2.3 | $P_{\rm loc}$ at $T=\pi\rho$ for all $\gamma$ excludes zeros with $\delta\ge 2.5/\log\gamma$ | PROVED in the lattice model; ARGUED for ζ |
| (a) | Selberg/Hadamard formula for $\zeta'/\zeta$ as a sign mechanism | **NO-GO** (tautological; DH-blind) |
| (b) | Selberg $\Lambda^2$ / sieve positivity | **NO-GO** (wrong direction plus parity factor) |
| (b′) | Λ ≥ 0 (Mertens 3-4-1) | **NO-GO** (gives the wrong inequality for $W$) |
| (c) | Levinson–Conrey mollifier ⇒ $P_{\rm loc}$ | **NO-GO** (non-local by MV duality; Bombieri–Hejhal falsifier; Cor 4.10a) |
| row D | | **OPEN** |

---

## §1 The localised form

### 1.1 Definitions

Fix $\gamma\gg1$ and $T>0$. For real $g\in L^2(-T,T)$ put $G(u)=g(u)\cos(\gamma u)$. Then
$\widehat G(\tau)=\tfrac12(\widehat g(\tau-\gamma)+\widehat g(\tau+\gamma))$. Use the notation of R163_401 §1.1:
$\sigma_T$, $m$, $v_n=2\Lambda(n)n^{-1/2}$, $V_T:=\sum_{\log n<2T}v_n$.

**Definition ($P_{\rm loc}(\gamma,T)$).** $P_{\rm loc}(\gamma,T)$ is the statement $\mathfrak a_T(G)\ge0$ for every $G=g\cos\gamma u$ with $g\in L^2(-T,T)$
real and $G\in\mathcal P_T\cap\mathcal D_T$. (In the complete form, the polar term $2\mathrm{Re}A\bar B$ is $O(|\widehat g(\gamma\pm i/2)|^2)$. It is absorbed into the primitive
condition.)

### 1.2 Localisation formula. PROVED.

Expand $\mathfrak a_T(G)=\frac1{2\pi}\int\sigma_T|\widehat G|^2$. Using $\int|\widehat G|^2\cos(\tau\log n)\,d\tau=2\pi\,c_G(\log n)$ gives
$$
\mathfrak a_T(G)=\frac1{2\pi}\int m|\widehat G|^2\;-\;\sum_{\log n<2T}v_n\,c_G(\log n),
$$
$$
c_G(u)=\tfrac12\cos(\gamma u)\,c_g(u)+\tfrac12 X_\gamma(u),\qquad X_\gamma(u)=\int g(t)g(t-u)\cos(\gamma(2t-u))\,dt .
$$
So the prime part is
$$
\mathcal S_\gamma(g):=\sum_{n<e^{2T}}v_nc_G(\log n)=\mathrm{Re}\sum_{n<e^{2T}}\Lambda(n)\,n^{-1/2-i\gamma}\,c_g(\log n)\;+\;\mathcal X_\gamma(g),
$$
with $\mathcal X_\gamma=\frac12\sum v_nX_\gamma(\log n)\to0$ as $\gamma\to\infty$ for fixed $g$ (Riemann–Lebesgue).
Note that $c_g=g*\tilde g$ is positive definite, with $c_g(0)=\|g\|^2$ and $|c_g|\le\|g\|^2$. Also
$m(\tau)=\log(|\tau|/2\pi)+O(\tau^{-2})$ (Stirling), so the archimedean part is
$\frac12\log(\gamma/2\pi)\|g\|^2\,(1+o(1))$ for $g$ with $\widehat g$ concentrated at $|\tau|\ll\gamma$. This is the twisted prime sum of the task. ∎

### 1.3 Spectral form. PROVED (rewriting).

Write $\mathcal S_\gamma(g)=\frac1{2\pi}\int|\widehat g(t)|^2\,D_T(\gamma+t)\,dt+\mathcal X_\gamma$, where $D_T(\tau)=\sum_{n<e^{2T}}\Lambda(n)n^{-1/2}\cos(\tau\log n)$.
Then $P_{\rm loc}(\gamma,T)$ says that the Toeplitz form on $PW_T$ with symbol $\tfrac12 m(\gamma+t)-D_T(\gamma+t)$ is nonnegative, up to $\mathcal X$ and the primitivity constraint.
The symbol has spectrum in $(-2T,2T)$ and so does $|\widehat g|^2$. This is the Carathéodory–Toeplitz/Kreĭn extension problem of the record, recentred at $\gamma$. **No new object:** the local problem is the record's
global Kreĭn problem restricted to tests with spectral mass near $\gamma$.

---

## §2 What is true unconditionally, and what $P_{\rm loc}$ costs

### 2.1 Trivial range. PROVED.

For every $F\in\mathcal P_T$, $\sigma_T(\tau)\ge m(\tau)-V_T$ pointwise. Hence
$$
\mathfrak a_T(F)\ \ge\ \frac1{2\pi}\int\big(m(\tau)-V_T\big)|\widehat F|^2\,d\tau .
$$
Chebyshev's bound $\psi(x)<1.04x$ (Rosser–Schoenfeld) and partial summation give
$V_T=2\sum_{n<e^{2T}}\Lambda(n)n^{-1/2}\le 2\cdot2.08\,e^{T}=4.16\,e^{T}$.
Therefore $\mathfrak a_T(F)\ge0$ whenever the mass of $|\widehat F|^2$ in $\{m<V_T\}$ is dominated by the mass in $\{m>V_T\}$. For the localised $G$ with
$\widehat g$ concentrated at $|t|\le R\ll\gamma$, this holds once
$$
4.16\,e^{T}\le\log(\gamma/2\pi)-O(R/\gamma),\qquad\text{i.e.}\qquad T\le\log\log\gamma-1.43+o(1).
$$
This range uses only $\Lambda\ge0$ and Chebyshev. It is DH-blind in the sense that any Dirichlet series with $|a(n)|\le\Lambda(n)$ gives the same bound. ∎

### 2.2 The gap to the Landau window is square-root cancellation. PROVED (reduction).

R163_402 locates detection at $T\approx\pi\rho=\frac12\log(\gamma/2\pi)$, i.e. at prime length $N=e^{2T}\approx\gamma/2\pi$. There the archimedean budget is
$\asymp\log\gamma\cdot\|g\|^2$, while the trivial size of the prime sum is $\asymp N^{1/2}\|g\|^2=\gamma^{1/2}\|g\|^2$.
So $P_{\rm loc}(\gamma,\pi\rho)$ for all $g$ needs, through §1.3, the following on the $1/T$-neighbourhood of $\gamma$ (in the $|\widehat g|^2$-averaged sense):
$$
\Big|\sum_{n<\gamma/2\pi}\Lambda(n)n^{-1/2-it}c_g(\log n)\Big|\ \lesssim\ \log\gamma\,\|g\|^2 ,
$$
a saving of $\gamma^{1/2}/\log\gamma$ over the trivial bound. Unconditional exponential-sum technology is far from this.
Vinogradov–Korobov saves $\exp(-c(\log N)^3/(\log\gamma)^2)=\gamma^{-c'}$ at $N=\gamma$, with $c'$ tiny, and less for $N=\gamma^{a}$, $a<1$.
In the whole range $\log\log\gamma\ll T\le\frac12\log\gamma$, no unconditional method reaches the needed bound. ∎

### 2.3 Strength of $P_{\rm loc}$. PROVED in the lattice model, ARGUED for ζ.

By R163_402 Thm 4, in the model (M1)–(M2) a quartet with $\delta\ge(3/2)^{1/2}/(\pi\rho)\approx2.45/\log(\gamma/2\pi)$ is detected, meaning the localised form is negative, at some $T<\pi\rho$.
Contrapositively, $P_{\rm loc}(\gamma,\pi\rho)$ for all $\gamma$ excludes all zeros with $\beta-\frac12\ge2.5/\log\gamma$. That is a zero-free region of width $\asymp1/\log\gamma$ to the right of the line.
Nothing of this strength is known: the best unconditional region is Korobov–Vinogradov, $\beta\le1-c(\log\gamma)^{-2/3}(\log\log\gamma)^{-1/3}$.
So $P_{\rm loc}$ at the Landau window is a quasi-RH statement. Any prime-side proof of it must contain a proof of a $\frac12+O(1/\log\gamma)$ zero-free region. This is the quantitative form of "circular at the witness" (R163_401 Rem 4.8a), now localised.

---

## §3 Falsifier lines first

**F1 (DH).** The Davenport–Heilbronn function $L_{\rm DH}$ satisfies the same functional equation as a degree-1 $L$-function. Its Dirichlet coefficients satisfy $|a(n)|\ll1$, but $-L'_{\rm DH}/L_{\rm DH}$ has coefficients not supported on prime powers and with no sign.
It has $\gg T$ zeros with $\beta>\frac12$ in $[T,2T]$ (Davenport–Heilbronn; Voronin). PROVED-CITED.

**F2 (Bombieri–Hejhal).** For linear combinations $\sum c_jL_j$ of primitive $L$-functions with a common functional equation (DH is one), 100% of zeros lie on the line, conditionally on GRH for the $L_j$ and a weak pair-independence hypothesis (Bombieri–Hejhal, Duke 1995). PROVED-CITED.
Combined with F1: *the statement "100% of zeros on the line", even when derived from Euler products (of the constituents $L_j$), coexists with infinitely many off-line zeros.*
Any route whose output is an on-line proportion, even 100%, is therefore falsified as a route to RH. It is also falsified as a route to $P_{\rm loc}$: in DH, $P_{\rm loc}$ fails at the off-line ordinates by R163_402 Cor 2, with the zero side computed for DH.

**F3 (Levinson for DH).** Levinson's method has not been carried out for DH unconditionally. The best unconditional on-line count is Karatsuba's $\gg T(\log T)^{1/2-\epsilon}$, which is not a positive proportion. The obstruction is the main-term evaluation of $\int|L\psi|^2$ with a mollifier $\psi\approx1/L$: it uses the multiplicativity of $\mu$-type coefficients, and DH has no Euler product.
So the task's suspicion is correct: Levinson *as executed* uses the Euler product, and DH lacks it. F2 shows that this difference does not survive to the level of conclusions about off-line zeros. PROVED-CITED, with the remark ARGUED.

---

## §4 The three routes

### (a) Euler product / Selberg's formula for $\zeta'/\zeta$. NO-GO.

Selberg's formula (Titchmarsh §14.21; Selberg 1946) gives, for $x\ge2$ and $s$ not a zero,
$$
-\frac{\zeta'}{\zeta}(s)=\sum_{n<x^2}\frac{\Lambda_x(n)}{n^s}+\frac{x^{2(1-s)}-x^{1-s}}{(1-s)^2\log x}+\frac1{\log x}\sum_\rho\frac{x^{\rho-s}-x^{2(\rho-s)}}{(s-\rho)^2}+(\text{trivial zeros}).
$$
It is derived by integrating $-\zeta'/\zeta(s+w)\,(x^{2w}-x^w)/(w^2\log x)$ and shifting past every pole. That is, it *is* the explicit formula with the test kernel $(x^{2w}-x^w)/(w^2\log x)$.
Inserting it into $\mathcal S_\gamma$ returns, term for term, the zero-side identity (1.1) of R163_401 for the test $G$.
- **Circularity (PROVED).** The map prime side → zero side is an identity (Paper 46 Thm Z). The sign of the "local formula" is $\sum_\rho\mathrm{Re}\,\widehat G(t_\rho)^2$, which is decided by the off-line zeros in the light cone (R163_402 Cor 2). So the local formula restates $P_{\rm loc}$ and does not prove it.
- **The zero sum does not localise.** An off-line zero $\beta=\frac12+\delta$ near $\gamma$ enters with weight $x^{\delta}/(\delta^2\log x)$, which grows as $x\to\infty$; the zero sum is not uniformly bounded.
- **DH-blind (PROVED).** The derivation uses only the meromorphy of $L'/L$ and the functional equation, so it holds verbatim for $L_{\rm DH}$ with $\Lambda_x$ replaced by the coefficients of $-L'_{\rm DH}/L_{\rm DH}$.

The Euler product enters only through $\Lambda$, and §2.1 is all that $\Lambda$'s sign gives. NO-GO.

### (b) Selberg $\Lambda^2$ / sieve positivity. NO-GO.

- **Direction (PROVED).** $P_{\rm loc}$ needs an *upper* bound on the twisted prime sum $\mathrm{Re}\sum\Lambda(n)n^{-1/2-i\gamma}c_g(\log n)$, because it enters $\mathfrak a_T$ with a minus sign.
  - Sieve majorants $\Lambda\le\Lambda^+$ (Selberg $\Lambda^2$, Brun–Titchmarsh) bound $\sum\Lambda(n)w(n)$ only for $w\ge0$.
  - The twist $n^{-i\gamma}c_g(\log n)$ is signed and oscillating, and $\Lambda\le\Lambda^+$ gives no information on $\sum(\Lambda^+-\Lambda)n^{-i\gamma}c$.
  - Applied to $|c_g|$, sieves return $\le(2+o(1))\times$ the PNT size $\asymp e^{T}$. This is the trivial range of §2.1 up to the parity factor 2: the parity barrier makes 2 the best constant of any pure sieve.
- **Squares (PROVED).** Selberg's positive-proportion method (and the λ-weights behind it) proves lower bounds for $\int|\zeta\phi|^2$-type expressions. These are trivially $\ge0$ because they are squares, and the work is in the *size* of the main term.
  The Weil form is not a square of a Dirichlet polynomial. Writing $\mathfrak a_T(G)=\int|\mathcal D|^2d\mu$ with $\mu\ge0$ is exactly the Kreĭn/Toeplitz positivity of §1.3, which is the target. NO-GO.

**(b′) Λ ≥ 0 via Mertens' 3-4-1. NO-GO (PROVED).** For $c_g\ge0$, $\sum\Lambda(n)n^{-1/2}c_g(\log n)(3+4\cos(\gamma\log n)+\cos(2\gamma\log n))\ge0$. In Weil-form language,
$3\mathcal S_0+4\mathcal S_\gamma+\mathcal S_{2\gamma}\ge0$, i.e. a *lower* bound on prime sums. That is an *upper* bound on the corresponding combination of $\mathfrak a_T$, the direction used to *detect* zeros (de la Vallée Poussin near $\sigma=1$), not to exclude them. Positivity of $\Lambda$ is structurally on the wrong side of the Weil form.

### (c) Levinson–Conrey mollifier. NO-GO.

**What the method gives (PROVED-CITED).** Let $V=Q(-\frac1L\frac d{ds})\zeta$ and let $\psi=\sum_{n<X}\mu(n)P(\log(X/n)/\log X)n^{-s-R/L}$ with $X=\gamma_0^\theta$. Littlewood's lemma and convexity give
$$
\kappa\ \ge\ 1-\frac1R\log\Big(\frac1H\int_{\gamma_0}^{\gamma_0+H}|V\psi(a+it)|^2dt\Big),\qquad a=\tfrac12-R/L,
$$
and the mean value is $c(\theta,P,Q,R)+o(1)$, provided $H\ge\gamma_0^{\theta+\epsilon}$ (Conrey 1989: $\theta=\frac47$, $\kappa>0.4$). Getting $\kappa\to1$ would require $c\to1$ along a sequence, which is known to need $\theta\to\infty$ (Farmer's "θ=∞" heuristic).

**Why 2/5 is not RH, precisely (PROVED).**
1. $\kappa<1$.
2. $\kappa=1$ still allows $o(N(\gamma_0))$ off-line zeros. F2 shows that this gap is real for DH-type functions.
3. The inequality is an $L^2$ average over $t\in[\gamma_0,\gamma_0+H]$. One off-line quartet changes $\log\int|V\psi|^2$ by $O(1/H)$, so it is invisible.

**Mean-value / Landau duality (PROVED from Montgomery–Vaughan).** Diagonal dominance of a mollified local form requires
$\int_{\gamma_0}^{\gamma_0+H}|\sum_{n<N}a_nn^{-it}|^2=\sum(H+O(n))|a_n|^2$ with $H\gg N$.
The Weil test at window $T$ involves prime length $N=e^{2T}$, and at the Landau window $N\approx\gamma/2\pi$. So diagonal dominance needs averaging over $H\gg\gamma$: the entire range below $\gamma$.
At fixed $\gamma$, i.e. a single cell, the off-diagonal $\sum_{m\ne n}a_m\bar a_nc_g(\log m/n)$ is of full size, because $|\log m/n|<2T$ for most pairs. **Locality in $\gamma$ and mollifier control are mutually exclusive at and above the Landau window.**
Below it ($N\ll H$ with $H\asymp1$), $N=O(1)$ and the mollifier is trivial: we are back in §2.1.

**Does the first-contact structure supply the missing piece? NO (PROVED, from the record).**
- The witness $F$ at $T_c$ is a single fixed test of window $T_c>0.8047$ with node density $T_c/\pi$. Any mollifier argument outputs an on-line *count* (a proportion) of zeros near height $\gamma$.
- R163_401 Cor 4.10a (in the lattice model, via R163_402 Lemma 4.10) shows that $(\star_{\rm cell})$ cannot follow from on-line counting together with $\delta<\frac12$: in the model, regime (α) is empty.
- The real-rootedness of $\widehat F$ only fixes the phase law $\theta'_\delta=\pi P_\delta*\nu$. It does not interact with $|V\psi|^2$, which concerns $\zeta$ at $\sigma=\frac12-R/L$, not $\widehat F$.
- The light cone needs a node within $\approx\delta$ of each off-line ordinate. The nodes have bounded density $T_c/\pi$, while zero density grows like $\log\gamma$, so the cells at height $\gamma$ contain $\asymp\log\gamma$ zeros each. Levinson does not resolve below the scale $H\ge\gamma^{\theta}$.

So the witness adds an exact linear relation $W(F)=0$, but Levinson adds only an averaged count, and the record has already shown that counts are insufficient. NO-GO.

---

## §5 Where the remaining gap sits

All three routes reduce to the same quantitative wall:
$$
\boxed{\ \text{an upper bound }\ \mathrm{Re}\sum_{n<\gamma}\Lambda(n)n^{-1/2-it}c_g(\log n)\le\tfrac12\log(\gamma/2\pi)\|g\|^2\ \text{ on }1/T\text{-windows at height }\gamma\ }
$$
This is square-root cancellation at length $\gamma$, localised in $t$. It is stronger than a $\frac12+O(1/\log\gamma)$ zero-free region (§2.3).
- The Euler product contributes $\Lambda\ge0$, which is on the wrong side ((b′)).
- Sieves contribute majorants with parity factor 2 ((b)).
- Mollifiers contribute averages over $H\gg N$, which are non-local ((c)).
- Selberg/Hadamard formulas contribute the explicit formula back ((a)).

A prime-side proof of $P_{\rm loc}$ would need an unconditional square-root-cancellation mechanism for $\Lambda(n)n^{-it}$ in short $t$-windows. No such mechanism is known, and F2 forbids it from being proportion-based. Row D: OPEN; no label moves.

**Open items (named, not attempted).** (O602.1) A rigorous version of §2.3 for actual ζ zeros, without (M2). (O602.2) Whether the DH zero side violates $P_{\rm loc}$ at *every* off-line ordinate: R163_402 Cor 2 gives it once a node can be placed, and this needs a DH Landau-window check.
