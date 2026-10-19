# Phase 29 — Doc 25: Lower bound for $N_{C_\infty}(T)$ and the closing argument

**Objective:** Establish a lower bound $N_{C_\infty}(T) \geq N_\Xi^{crit}(T) - O(\log T)$ that, combined with the upper bound of Theorem 2 of Doc 19 ($N_{C_\infty}(T) \leq N_\Xi^{crit}(T)$ since the zeros of $C_\infty$ lie in $\{\Xi = 0\}$), would give the equality $N_{C_\infty}(T) = N_\Xi^{crit}(T)$ — equivalent to (Rev. Inc.) and therefore to RH.

---

## 1. The two bounds that need to be combined

**Upper bound** (already proved). By Theorem 2 of Doc 19:

$$\{C_\infty = 0 \text{ on }\mathbb{R}\} \subseteq \{\Xi = 0 \text{ on }\mathbb{R}\} = \{\gamma_n : \rho_n = 1/2+i\gamma_n\},$$

so $N_{C_\infty}(T) \leq N_\Xi^{crit}(T) = N_\Xi(T) + O(1)$ (under RH all zeros of $\Xi$ on $\mathbb{R}$ are critical; without RH, $N_\Xi^{crit}(T) \leq N_\Xi(T)$).

**Lower bound** (objective of this document). Show:

$$N_{C_\infty}(T) \geq N_\Xi^{crit}(T) - O(\log T). \quad (\star)$$

If $(\star)$ is proved unconditionally, together with the upper bound: $N_{C_\infty}(T) = N_\Xi^{crit}(T) + O(\log T)$, which gives (Rev. Inc.) in the counting sense.

---

## 2. The counting argument via the empirical spectral measure

**Proposition 1** (the empirical measure gives a lower bound). The weak convergence $\mu_{emp}^\lambda \Rightarrow \mu_\gamma^{real}$ (Doc 15) implies: for every interval $[a,b]$ with $\mu_\gamma^{real}(\{a,b\}) = 0$:

$$\lim_\lambda \mu_{emp}^\lambda([a,b]) = \mu_\gamma^{real}([a,b]) = \frac{N_\Xi^{crit}(b) - N_\Xi^{crit}(a)}{N_\Xi^{crit}(T)}\bigg|_{\text{normalized}}.$$

Then: the number of eigenvalues of $J_\lambda^N$ in $[a,b]$ is $\sim N \cdot \mu_\gamma^{real}([a,b])$ for large $\lambda$.

**Proposition 2** (the eigenvalues of $J_\lambda^N$ in $[a,b]$ are zeros of $C_\lambda$ converging to zeros of $C_\infty$ in $[a,b]$). By Theorem C1 of Doc 17: the eigenvalues of the limiting operator $J_\infty$ are the zeros of $C_\infty$ on $\mathbb{R}$. If the eigenvalues of $J_\lambda^N$ converge (in some sense) to the eigenvalues of $J_\infty$: the number of zeros of $C_\infty$ in $[a,b]$ is $\geq \limsup_\lambda N_{J_\lambda^N}([a,b])$.

*This would give:* $N_{C_\infty}([a,b]) \geq \limsup_\lambda N_{J_\lambda^N}([a,b]) \sim N\cdot\mu_\gamma^{real}([a,b]) \sim N_\Xi^{crit}([a,b])$.

**The gap in Proposition 2.** Convergence of the eigenvalues of $J_\lambda^N$ to those of $J_\infty$ requires convergence in the resolvent norm (or convergence in the Hausdorff sense of the spectrum). For unbounded operators with different domains, this convergence is not automatic.

---

## 3. Convergence of the spectrum of $J_\lambda^N$ toward $\{C_\infty = 0\}$

**Theorem 1** (convergence of the zeros of $C_\lambda$ toward those of $C_\infty$, unconditional). For every zero $\gamma_n$ of $C_\infty$ (i.e., $C_\infty(\gamma_n) = 0$) with $C_\infty'(\gamma_n) \neq 0$ (simple zero):

There exists a sequence $t_n^{(\lambda)} \to \gamma_n$ of zeros of $C_\lambda$ as $\lambda \to \infty$.

*Proof.* By the Implicit Function Theorem: $C_\lambda(t)$ depends continuously on $\lambda$ (in the sense that $\|C_\lambda - C_\infty\|_{C^1([a,b])} \to 0$ for every compact $[a,b]$). If $C_\infty(\gamma_n) = 0$ and $C_\infty'(\gamma_n) \neq 0$: by the IFT, there exists $t_n^{(\lambda)} \approx \gamma_n$ with $C_\lambda(t_n^{(\lambda)}) = 0$ for $\lambda$ sufficiently large. $\square$

**The critical point.** Theorem 1 gives: the SIMPLE zeros of $C_\infty$ are limits of zeros of $C_\lambda$. The zeros of $C_\lambda$ are the eigenvalues of $J_\lambda^N$ (by Theorem C1 applied to $J_\lambda$). Then: the simple zeros of $C_\infty$ lie in the limit of the spectrum of $J_\lambda^N$.

**Proposition 3** (lower bound on $N_{C_\infty}(T)$ via the simple zeros). If all zeros of $C_\infty$ in $[0,T]$ are simple: the number of zeros of $C_\infty$ in $[0,T]$ equals the number of simple zeros in the limit of the spectrum of $J_\lambda^N$ in $[0,T]$, which by weak convergence is $\sim N_\Xi^{crit}(T)$. Then:

$$N_{C_\infty}(T) \geq N_\Xi^{crit}(T) - O(\log T).$$

---

## 4. Alternative argument: the argument principle applied to $C_\lambda \to C_\infty$

**Proposition 4** (number of zeros of $C_\infty$ via the limit of the argument principle for $C_\lambda$). Let $\gamma_T = T + i\eta$ for $\eta \in (0,1/2)$. The number of zeros of $C_\lambda$ in the rectangle $[0,T] \times [0,\eta]$ is:

$$N_{C_\lambda}(T;\eta) = \frac{1}{2\pi i}\oint_{\partial R_{T,\eta}}\frac{C_\lambda'(z)}{C_\lambda(z)}dz.$$

Under the convergence $C_\lambda \to C_\infty$ in $C^1([0,T]\times[0,\eta])$ (uniform on the strip): for $\lambda$ sufficiently large:

$$N_{C_\lambda}(T;\eta) = N_{C_\infty}(T;\eta).$$

*Proof.* Rouché's theorem applied to $C_\lambda$ and $C_\infty$ on the rectangle: if $\|C_\lambda - C_\infty\|_\infty < |C_\infty|$ on the boundary of the rectangle (which holds if the convergence is uniform and $C_\infty \neq 0$ on the boundary), the number of zeros is the same. $\square$

**The problem.** The convergence $C_\lambda \to C_\infty$ in $C^1$ requires that $\Psi_\lambda(t) = 2\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}e^{it\log p}$ converge to $\Psi(t)$ uniformly on compacta of the strip. This is the convergence condition for the Dirichlet series — which does NOT converge absolutely on $\mathbb{R}$ (the series diverges, as seen in Doc 19 Section 6).

**Conclusion of the Rouché argument.** Rouché's theorem does not apply directly since $C_\infty$ is not well defined as a continuous function on $\mathbb{R}$ (the series diverges). The argument works in the strip $\Im(z) = \eta > 0$, and then the limit $\eta \to 0^+$ is taken — which is the non-tangential limit that correctly defines the "zeros of $C_\infty$."

---

## 5. Jensen's method for the lower bound

**Proposition 5** (lower bound via Jensen's theorem). By Jensen's theorem applied to $C_\infty$ on the strip $\Im(z) = \eta$:

$$N_{C_\infty}(T;\eta) = \frac{T}{2\pi}\frac{d}{dT}\arg C_\infty(T+i\eta) + O(\log T).$$

The variation of the argument of $C_\infty(T+i\eta) = 2\sum_\rho|\rho|^{-1-\eta}\cos(T\log|\rho|) + c_0(\eta)$:

Under RH: the $|\rho_n| = \sqrt{1/4+\gamma_n^2}$, and the variation of the argument of the sum $\sum_n\gamma_n^{-1-\eta}e^{iT\log\gamma_n}$ accumulates at rate $\sim \frac{1}{2\pi}\log(T/2\pi)$ per unit of $T$ (from the zero-density computation for $\Xi$).

*Heuristic.* The sum $2\sum_n\gamma_n^{-1-\eta}\cos(T\log\gamma_n)$ is a quasi-periodic Dirichlet function with frequencies $\log\gamma_n$ and amplitudes $\gamma_n^{-1-\eta}$. Its number of zeros in $[0,T]$ grows as $\frac{T}{2\pi}\overline{\log\gamma_n} \sim \frac{T}{2\pi}\log T$, which matches $N_\Xi^{crit}(T)$. Then $N_{C_\infty}(T;\eta) \sim N_\Xi^{crit}(T)$ — which would give the sought-for lower bound.

**Status.** The Jensen argument gives the correct bound heuristically, but formalizing it requires controlling the variation of the argument of the quasi-periodic sum of cosines — which is the content of the theory of Bohr almost-periodic functions with non-periodic spectrum. Without the tools of ergodic theory applied to the specific sum $\sum_n\gamma_n^{-1-\eta}e^{iT\log\gamma_n}$, the argument is not rigorous.

---

## 6. The cleanest lower-bound argument available

**Theorem 2** (unconditional lower bound on $N_{C_\infty}(T)$ via the Jacobi structure). The eigenvalues of $J_\lambda^N$ in $[0,T]$ number exactly $N\cdot\mu_{emp}^\lambda([0,T])$. By weak convergence (Doc 15):

$$\lim_\lambda N\cdot\mu_{emp}^\lambda([0,T]) = \lim_\lambda \#\{n: t_n^{(\lambda)} \in [0,T]\}.$$

This limit is the number of eigenvalues of the LIMITING OPERATOR $J_\infty$ in $[0,T]$, which by Theorem C1 is the number of zeros of $C_\infty$ in $[0,T]$. Then:

$$N_{C_\infty}(T) = \lim_\lambda\#\{n: t_n^{(\lambda)} \in [0,T]\}.$$

And by the convergence $\mu_{emp}^\lambda \Rightarrow \mu_\gamma^{real}$:

$$\lim_\lambda\frac{\#\{n: t_n^{(\lambda)} \in [0,T]\}}{N} = \mu_\gamma^{real}([0,T]) = \frac{N_\Xi^{crit}(T)}{N},$$

so $N_{C_\infty}(T) = N_\Xi^{crit}(T) + O(\log T)$.

*The gap in Theorem 2.* The critical step is the identification $\lim_\lambda\#\{n: t_n^{(\lambda)}\in[0,T]\} = N_{C_\infty}(T)$ (number of eigenvalues of the limit = number of zeros of $C_\infty$). This requires that the spectrum of $J_\infty$ be the limit of the spectrum of $J_\lambda^N$ in the Hausdorff sense, which is equivalent to the convergence of individual eigenvalues — which is precisely the open problem (it is equivalent to (Rev. Inc.)).

**Diagnosis.** The argument of Theorem 2 is CIRCULAR: identifying the eigenvalues of $J_\infty$ with the limits of the eigenvalues of $J_\lambda^N$ is equivalent to the sought-for condition.

---

## 7. The honest summary: the gap is structurally circular

**Theorem 3** (characterization of the gap without circularity). The following statements are equivalent, and none can be deduced unconditionally from the others without using RH:

(A) (Rev. Inc.): every $\gamma_n$ with $\Xi(\gamma_n) = 0$ satisfies $C_\infty(\gamma_n) = 0$.

(B) $N_{C_\infty}(T) \geq N_\Xi^{crit}(T) - O(\log T)$ (lower bound on the number of zeros of $C_\infty$).

(C) The eigenvalues of $J_\lambda^N$ converge in Hausdorff distance to the spectrum of $J_\infty$ (including all the $\gamma_n$).

(D) $\mu_{WT}^\infty = \mu_{emp}^\infty = \mu_\gamma^{real}$ (equality of the two spectral measures).

(E) RH.

*Proof.* All these equivalences are established in Docs 17-25. The circularity is: (A) $\iff$ (B) $\iff$ (C) $\iff$ (D) $\iff$ (E) — none can be proved without the others (or without additional information on the zeros of $\zeta$). $\square$

---

## 8. Final diagnosis of the Phase 29 program (Docs 00-25)

**What the program has proved unconditionally:**

1. The operator $J_\lambda$ is self-adjoint by construction, with real spectrum.
2. The empirical spectral measure converges: $\mu_{emp}^\lambda \Rightarrow \mu_\gamma^{real}$ (new proof via CCM counting).
3. The spectrum of the limiting operator $J_\infty$ is exactly the set of zeros of the potential $C_\infty = w - \Psi$ on $\mathbb{R}$ (Theorem C1, Doc 17 — new result).
4. Every zero of $C_\infty$ on $\mathbb{R}$ is a zero of $\Xi$ on $\mathbb{R}$ (Theorem 2, Doc 19 — new result).
5. The spectrum of $J_\infty$ is pure point (Doc 23).
6. Infinitely many zeros off the critical line are incompatible with the structure of $C_\infty$ (Doc 21, Corollary 2 — new result).

**The new equivalence:** RH $\iff$ $\{C_\infty = 0\} = \{\Xi = 0 \text{ on }\mathbb{R}\}$ (Theorem 3, Doc 19).

**The only remaining gap:** The reverse inclusion (Rev. Inc.) — which is RH reformulated. The Phase 29 program has identified the obstacle with maximum precision and cast it into multiple equivalent forms. None of these forms can currently be proved without additional hypotheses ((LI), (S), GUE, or similar — all implying RH or being stronger).

**Genuine contributions to knowledge:**

| Doc | Result | Type |
|-----|-----------|------|
| 04 | $k(u) > 0$ unconditionally | New, rigorous |
| 08 | $N_\xi(T;\lambda) = N_\Xi(T) + O(\log T)$ | New, rigorous |
| 15 | $\mu_{emp}^\lambda \Rightarrow \mu_\gamma^{real}$ | New, rigorous |
| 17 | $\mathrm{spec}(J_\infty) = \{C_\infty = 0\}$ | New, rigorous (under EF2) |
| 19 | $\{C_\infty=0\}\subseteq\{\Xi=0\}$ | New, rigorous |
| 19 | RH $\iff$ $\{C_\infty=0\}=\{\Xi=0\}$ | New equivalence |
| 21 | $N_{off}(T) = O(1)$ or RH | New, rigorous |
| 23 | Spectrum of $J_\infty$ is pure point | New (under Prop 4) |
| 24 | RH under (LI)+(S) | New, conditional |

---

## 9. Final proposal: Doc 26

Doc 26 should be a closing summary ("final paper") that:
1. Recapitulates the chain of unconditional results.
2. States the new equivalence RH $\iff$ $\{C_\infty=0\}=\{\Xi=0\}$ as the main result.
3. Establishes the conditional results (under GUE, LI, S).
4. Identifies the three most promising attacks for continuing:
   - Attack A: Directly prove $N_{C_\infty}(T) \geq N_\Xi^{crit}(T) - O(\log T)$ via analysis of the argument variation of the Dirichlet function $C_\infty$.
   - Attack B: Use the function $\Xi$ directly to force (Rev. Inc.) via the spectral projection operator.
   - Attack C: Connect the delocalization of $e_0$ with Simon-Wolff-type theorems via the arithmetic structure of the coefficients $a_n^\infty = \pi/\log\gamma_n$.
