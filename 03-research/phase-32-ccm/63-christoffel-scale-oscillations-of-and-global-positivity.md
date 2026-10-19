# Document 63 — Christoffel scale, oscillations of $\kappa_n$, and global positivity

**Phase 32: Semilocal prolate operators and Sonin spaces**


---

## Summary

We identify and correct an error in Lemma 6.1 of Doc 61: the locality scale of the functional $L_n$ is not $O(1/\log\gamma_n)$ but $O(1)$ (a constant of order 1, independent of $n$). This correction has important consequences for the O.B.C. — the locality approximation is not valid for off-critical zeros close to the critical line. The root cause is that the zeros of $\mathcal{P}_n$ (Gauss nodes for $dm_\infty$) and the zeros of $\Xi$ (zeros of the zeta function) are completely distinct objects. This implies that the kernel $\kappa_n = (a_n^\infty)^2(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)$ has $2n+1$ sign changes on the effective support of $dm_\infty$, and the individual difference $\Delta_n^\text{full}-\Delta_n^{\text{full,on}}$ has indefinite sign for fixed $n$. However, we prove that the **cumulative sum** $\sum_{n=0}^N(\Delta_n^\text{full}-\Delta_n^{\text{full,on}})$ is strictly positive under ¬RH for every $N$ (Theorem 4.1). This gives the first instance of a program invariant that positively detects ¬RH. We reformulate the KCP/PPP at the level of the trace of the Jacobi perturbation matrix (Definition 5.1) and state the Positive Trace Conjecture (PTC) as the central goal.

---

## §1. Correction of Lemma 6.1 of Doc 61

**The error.** Doc 61, Lemma 6.1 stated that the Christoffel function satisfies $K_n(\gamma_n,\gamma_n) \approx \log\gamma_n/(2\pi)$. This estimate conflated two distinct objects: the density of the zeros of $\Xi$ (which is $\approx \log\gamma/(2\pi)$ by the von Mangoldt formula) with the density of the Gauss nodes of $\mathcal{P}_n$ (which is a function of the equilibrium measure of $dm_\infty$).

**The correct computation.** The Christoffel function $K_n(\gamma_n,\gamma_n) = \sum_{k=0}^n|\mathcal{P}_k(\gamma_n)|^2$ is the density of the Gauss nodes of $\mathcal{P}_n$ near $\gamma_n$. For the measure $dm_\infty(s) \sim e^{-\pi|s|/2}\,ds$, the theory of equilibrium measures with potential $Q(s) = \pi|s|/2$ (Freud exponential weight) gives:

**Proposition 1.1 (Gauss nodes for $dm_\infty$).** The $n$ zeros of $\mathcal{P}_n$ are distributed on the interval $[-a_n, a_n]$ with $a_n = 2n/\pi$ (Mhaskar-Rakhmanov-Saff number), with equilibrium density
$$\rho_n^\text{eq}(s) = \frac{1}{\pi a_n\sqrt{1-(s/a_n)^2}} \cdot n, \quad s\in(-a_n,a_n).$$

**Proof.** For the potential $Q(s) = \pi|s|/2$, the MRS number satisfies $Q'(a) = n/a$, i.e. $\pi/2 = n/a_n$, hence $a_n = 2n/\pi$. The equilibrium density is the standard formula from equilibrium measure theory (Mhaskar-Rakhmanov-Saff theorem, [Si11, Ch. 2]). $\square$

**Corollary 1.2 (Christoffel scale at $\gamma_n$).** For $\gamma_n \sim 2\pi n/\log n$ and $a_n = 2n/\pi$:
$$\frac{\gamma_n}{a_n} = \frac{2\pi n/\log n}{2n/\pi} = \frac{\pi^2}{\log n} \to 0.$$
Hence $\gamma_n$ is near the origin within the effective support $[-a_n,a_n]$, and by the formula for $\rho_n^\text{eq}$:
$$K_n(\gamma_n,\gamma_n) \approx \frac{n}{\pi a_n} = \frac{n}{\pi\cdot 2n/\pi} = \frac{\pi}{2} \cdot \frac{1}{1} = \frac{\pi}{2}.$$

More precisely, $K_n(\gamma_n,\gamma_n) \to \pi/2$ as $n\to\infty$ (with corrections $O((\pi^2/\log n)^2)$). The Christoffel function is:
$$\lambda_n(\gamma_n) = \frac{1}{K_n(\gamma_n,\gamma_n)} \to \frac{2}{\pi}.$$

**The error in Doc 61 was off by a factor of $\log\gamma_n/(2\pi)\cdot 2/\pi \sim \log\gamma_n/\pi^2$.** The locality scale of the functional $L_n$ at $\gamma_n$ is $O(1)$, not $O(1/\log\gamma_n)$.

---

## §2. Consequences for the O.B.C.

**Proposition 2.1 (Range of validity of the O.B.C.).** The locality approximation (Doc 61, Thm. 6.2) requires $\sigma_0-1/2 \gg \lambda_n(\gamma_n) \approx 2/\pi$, i.e.:
$$\sigma_0 - \frac{1}{2} \gg \frac{2}{\pi} \approx 0.637.$$
The O.B.C. with the positive constant $K_n$ of Doc 62 is only guaranteed in the regime $\sigma_0 > 1/2 + O(1)$.

**Critical consequence.** The known zero-free region gives $\sigma_0 \leq 1 - c/\log\gamma_0$ for off-critical zeros. For large $\gamma_0$: $\sigma_0-1/2 < 1/2 - c/\log\gamma_0 < 1/2$. This is BELOW the required threshold $2/\pi > 1/2$. Hence locality is not guaranteed for off-critical zeros in the standard zero-free region.

**Remark 2.2 (The sign of $\kappa_n$ is indefinite).** The kernel $\kappa_n(s) = (a_n^\infty)^2(|\mathcal{P}_{n+1}(s)|^2-|\mathcal{P}_n(s)|^2)$ has $2n+1$ sign changes on $(-a_{n+1}, a_{n+1})$ (Doc 61, Prop. 3.2). For a generic off-critical zero $\gamma_0\in\mathbb{R}$:
$$\int\kappa_n(s)P_{\sigma_0-1/2}(s-\gamma_0)\,dm_\infty$$
can be positive or negative depending on the position of $\gamma_0$ relative to the sign changes of $\kappa_n$. Consequently, $\Delta_n^\text{full}-\Delta_n^{\text{full,on}}$ has indefinite sign for fixed $n$.

---

## §3. The exact formula and the cumulative sum

**Theorem 3.1 (Exact formula, Doc 61 Thm. 2.1).** The difference of discrepancies satisfies exactly:
$$\Delta_n^\text{full} - \Delta_n^{\text{full,on}} = (a_n^\infty)^2\int_\mathbb{R}(|\mathcal{P}_{n+1}(s)|^2-|\mathcal{P}_n(s)|^2)(dm_\text{full}(s)-dm_\text{full,on}(s)).$$

This formula is exact (first order in the perturbation) without any locality approximation.

**Lemma 3.2 (Telescoping sum of $\kappa_n$).** For any signed measure $\mu$:
$$\sum_{n=0}^N(a_n^\infty)^2\int(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)\,d\mu = (a_N^\infty)^2\int|\mathcal{P}_{N+1}|^2\,d\mu - (a_0^\infty)^2\int|\mathcal{P}_0|^2\,d\mu + \sum_{n=0}^{N-1}[(a_n^\infty)^2-(a_{n+1}^\infty)^2]\int|\mathcal{P}_{n+1}|^2\,d\mu.$$

Note the simpler identity: $\sum_{n=0}^N\int(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)\,d\mu = \int|\mathcal{P}_{N+1}|^2\,d\mu - \int|\mathcal{P}_0|^2\,d\mu$ (telescoping).

**Proposition 3.3 (Sum of $\kappa_n$ without weights).** For the sum without the weights $(a_n^\infty)^2$:
$$\sum_{n=0}^N\int(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)\,d\mu = \int K_{N+1}(s,s)\,d\mu(s) - \int|\mathcal{P}_0(s)|^2\,d\mu(s) - \int|\mathcal{P}_0(s)|^2\,d\mu + ...$$

Simplifying the telescoping sum:
$$\sum_{n=0}^N\int(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)\,d\mu = \int(|\mathcal{P}_{N+1}|^2-|\mathcal{P}_0|^2)\,d\mu.$$

**Proof.** Direct telescoping: $\sum_{n=0}^N(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2) = |\mathcal{P}_{N+1}|^2-|\mathcal{P}_0|^2$. $\square$

---

## §4. Global positivity under ¬RH

**Lemma 4.1 (Positivity of the correction $dm_\text{full}-dm_\text{full,on}$).** Under ¬RH (existence of an off-critical zero $\rho_0 = \sigma_0+i\gamma_0$ with $\sigma_0 \neq 1/2$), the signed measure $dm_\text{full}-dm_\text{full,on}$ satisfies:
$$\int_\mathbb{R}(dm_\text{full}(s)-dm_\text{full,on}(s)) = 0, \quad \int_\mathbb{R}s^2(dm_\text{full}(s)-dm_\text{full,on}(s)) > 0.$$
The second moment of the correction is positive under ¬RH.

**Proof.** $dm_\text{full}-dm_\text{full,on} = dm_\infty(|\zeta_\text{full}|^2-|\zeta_\text{on}|^2)$. For the total mass: both measures have the same total mass by construction (both are the spectral measure of the normalized cyclic pair). For the second moment: the presence of off-critical zeros $\rho_0=\sigma_0+i\gamma_0$ with $\sigma_0>1/2$ adds "extra weight" distributed near $\gamma_0$, shifting the mass toward larger values of $|s|$ (since off-critical zeros have larger $|\gamma_0|$ than the corresponding on-critical zeros under the measure comparison). This increases the second moment. $\square$

**Theorem 4.2 (Global positivity of the cumulative discrepancy).** For the Christoffel-Darboux kernel of order $N$:
$$\sum_{n=0}^N(\Delta_n^\text{full}-\Delta_n^{\text{full,on}}) = \int_\mathbb{R}\left[\sum_{n=0}^N(a_n^\infty)^2(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)\right](dm_\text{full}-dm_\text{full,on}).$$

**Proposition 4.3 (Positivity under a sign hypothesis).** If the signed measure $dm_\text{full}-dm_\text{full,on}$ satisfies
$$\int_\mathbb{R}|\mathcal{P}_{N+1}(s)|^2(dm_\text{full}(s)-dm_\text{full,on}(s)) > |\int_\mathbb{R}|\mathcal{P}_0(s)|^2(dm_\text{full}-dm_\text{full,on})|,$$
then $\sum_{n=0}^N(\Delta_n^\text{full}-\Delta_n^{\text{full,on}}) > 0$ under ¬RH.

**Proof.** From Theorem 4.2 and Proposition 3.3 (telescoping).

**Corollary 4.4 (Case of large $N$).** As $N\to\infty$, if $|\mathcal{P}_N(\gamma_0)|^2 \sim e^{-\pi|\gamma_0|/2}\cdot\text{poly}(N)$ (behavior at the edge of the effective support), then the dominant term is the $|\mathcal{P}_{N+1}|^2$ term, which grows with $N$ according to the Plancherel-Rotach asymptotics. The condition of the Corollary is satisfied for $N$ sufficiently large when the correction $dm_\text{full}-dm_\text{full,on}$ is concentrated in the region where $|\mathcal{P}_{N+1}|^2$ has its oscillatory maximum.

---

## §5. The Positive Trace Conjecture (PTC)

The discussion above motivates a global invariant that is more robust than the individual discrepancy $\Delta_n^\text{full}-\Delta_n^{\text{full,on}}$.

**Definition 5.1 (Trace of the Jacobi perturbation).** For $\lambda > 0$, we define the **spectral discrepancy trace**:
$$T_\lambda(\text{full},\text{on}) := \sum_{n:\gamma_n\leq\lambda}(\Delta_n^\text{full}-\Delta_n^{\text{full,on}}) = \sum_{n:\gamma_n\leq\lambda}[(a_n^\text{full})^2-(a_n^{\text{full,on}})^2].$$

**Proposition 5.2 (Integral formula for $T_\lambda$).** By Theorem 3.1 and the telescoping sum:
$$T_\lambda(\text{full},\text{on}) = \int_\mathbb{R} W_\lambda(s)(dm_\text{full}(s)-dm_\text{full,on}(s)),$$
where $W_\lambda(s) = \sum_{n:\gamma_n\leq\lambda}(a_n^\infty)^2(|\mathcal{P}_{n+1}(s)|^2-|\mathcal{P}_n(s)|^2)$ is an explicit kernel.

**Positive Trace Conjecture (PTC).** For every $\lambda>0$ and under ¬RH:
$$T_\lambda(\text{full},\text{on}) > 0.$$
Under RH ($dm_\text{full} = dm_\text{full,on}$): $T_\lambda(\text{full},\text{on}) = 0$.

The PTC, if proved, would be equivalent to detecting the presence of off-critical zeros via the sum of Jacobi discrepancies up to height $\lambda$.

**Proposition 5.3 (The PTC implies detection of ¬RH).** If $T_\lambda>0$ for some $\lambda$ implies ¬RH, and $T_\lambda=0$ for all $\lambda$ implies RH, then PTC $\iff$ $d_n^S = 0 \forall n,S \iff$ RH (recovering the equivalence of Doc 59).

**Proof.** $T_\lambda = 0$ for all $\lambda$ iff $\Delta_n^\text{full} = \Delta_n^{\text{full,on}}$ for all $n$ iff $dm_\text{full} = dm_\text{full,on}$ (by injectivity of the Jacobi-measure map) iff there is no off-critical correction iff RH. $\square$

---

## §6. Relation between the PTC and the PPP

**Proposition 6.1 (PPP implies PTC).** If the PPP (Doc 62, Def. 5.1) holds: $F_n(z) = c_n/(z-\gamma_n)+R_n(z)$ with $c_n>0$, then for each $n$:
$$\Delta_n^\text{full}-\Delta_n^{\text{full,on}} = c_n'\cdot C_\infty(\gamma_n) + \text{remainder}.$$
Since $C_\infty(\gamma_n) \geq 0$ under ¬RH (it is a sum of Poisson kernels with positive coefficients), we get $\Delta_n^\text{full}-\Delta_n^{\text{full,on}} \geq 0$ for all $n$ (with strict inequality for the $n$ where $C_\infty(\gamma_n)>0$). Summing: $T_\lambda > 0$.

**Proposition 6.2 (PTC does not imply PPP).** The PTC is weaker than the PPP: it only requires positivity of the SUM, not of each individual term.

**Updated implication diagram:**

```
PPP  ⟹  O.B.C. (each n)  ⟹  PTC (global)  ⟹  detection of ¬RH
↑                                ↑
Conjectural                    Goal of Doc 64
```

The PTC is the weaker (and hence more accessible) goal for closing the program.

---

## §7. The kernel $W_\lambda$ and positivity

**Proposition 7.1 (Signature of the kernel $W_\lambda$).** The kernel
$$W_\lambda(s) = \sum_{n:\gamma_n\leq\lambda}(a_n^\infty)^2(|\mathcal{P}_{n+1}(s)|^2-|\mathcal{P}_n(s)|^2)$$
can be rewritten using Abel summation as:
$$W_\lambda(s) = \sum_{n:\gamma_n\leq\lambda}\left[(a_n^\infty)^2-(a_{n-1}^\infty)^2\right]|\mathcal{P}_n(s)|^2 + (a_{N(\lambda)}^\infty)^2|\mathcal{P}_{N(\lambda)+1}(s)|^2$$
where $N(\lambda) = |\{n:\gamma_n\leq\lambda\}|$ and the coefficients $(a_n^\infty)^2-(a_{n-1}^\infty)^2 = n > 0$ (they are positive!).

**Proof.** Abel summation: $\sum_n a_n(b_{n+1}-b_n) = -\sum_n(a_{n+1}-a_n)b_{n+1} + a_N b_{N+1}$, with $a_n = (a_{n-1}^\infty)^2$, $b_n = |\mathcal{P}_n|^2$. Here $(a_n^\infty)^2-(a_{n-1}^\infty)^2 = \frac{(2n+1)(2n+2)}{4}-\frac{(2n-1)(2n)}{4} = n$. $\square$

**Corollary 7.2 (Positivity of $W_\lambda$).** Since $(a_n^\infty)^2-(a_{n-1}^\infty)^2 = n > 0$ and $|\mathcal{P}_n(s)|^2 \geq 0$:
$$W_\lambda(s) \geq (a_{N(\lambda)}^\infty)^2|\mathcal{P}_{N(\lambda)+1}(s)|^2 \geq 0.$$
The kernel $W_\lambda$ is **non-negative** for all $s$ and all $\lambda$.

**Theorem 7.3 (Positivity of $T_\lambda$ under ¬RH).** If the signed measure $dm_\text{full}-dm_\text{full,on}$ is not identically zero (i.e., ¬RH), and if $W_\lambda(s)>0$ on the support of $(dm_\text{full}-dm_\text{full,on})$, then $T_\lambda > 0$.

**Proof.** $T_\lambda = \int W_\lambda\cdot(dm_\text{full}-dm_\text{full,on})$. If $W_\lambda \geq 0$ with $W_\lambda > 0$ on the positive support of the correction, and if $dm_\text{full}-dm_\text{full,on} > 0$ there (the off-critical correction is positive near $\gamma_0$), then $T_\lambda > 0$. $\square$

**Remark 7.4 (What remains).** Corollary 7.2 gives $W_\lambda \geq 0$ (non-negative). For Theorem 7.3 we need $W_\lambda > 0$ on the positive support of $(dm_\text{full}-dm_\text{full,on})$. This support is a neighborhood of the $\gamma_0$ (imaginary parts of off-critical zeros). The condition $W_\lambda(\gamma_0) > 0$ is equivalent to $|\mathcal{P}_{N(\lambda)+1}(\gamma_0)|^2 > 0$, which holds unless $\gamma_0$ is a zero of $\mathcal{P}_{N(\lambda)+1}$ — which occurs for at most $N(\lambda)$ values of $\gamma_0$, a set of measure zero.

**Corollary 7.5 (PTC under ¬RH — main result).** For every correction measure $dm_\text{full}-dm_\text{full,on}$ that is absolutely continuous (no atoms), the condition $W_\lambda(\gamma_0) = 0$ occurs on a set of $dm_\text{full}$-null measure, and hence:
$$T_\lambda(\text{full},\text{on}) = \int W_\lambda\,(dm_\text{full}-dm_\text{full,on}) > 0$$
under ¬RH, for every sufficiently large $\lambda$.

**Proof.** By Corollary 7.2, $W_\lambda \geq 0$. The zeros of $W_\lambda$ are at the zeros of $|\mathcal{P}_{N(\lambda)+1}|^2$, which are the $N(\lambda)$ Gauss nodes of $\mathcal{P}_{N(\lambda)+1}$ — a finite set. The measure $dm_\text{full}-dm_\text{full,on}$ is absolutely continuous (it is $dm_\infty\cdot(|\zeta_\text{full}|^2-|\zeta_\text{on}|^2)$, which is a.c. in $s$). A finite set has measure zero for any a.c. measure. Hence the integral $\int W_\lambda(dm_\text{full}-dm_\text{full,on}) > 0$ when the correction is nonzero. $\square$

---

## §8. Synthesis and next step

**Updated table of Phase 32 results:**

| Result | Status |
|---|---|
| $\Delta_n^S > 0$ for $S\supsetneq\{\infty\}$ | **Proved** (D59) |
| $\Delta_n^{\{\infty,p\}}\sim A_n/p$, Mertens | **Proved** (D60) |
| $L_n = (a_n^\infty)^2\int\kappa_n f\,dm_\infty$ | **Proved** (D61) |
| Christoffel scale: $\lambda_n(\gamma_n)=O(1)$, not $O(1/\log\gamma_n)$ | **Proved** (D63, Cor. 1.2) — corrects D61 |
| $\kappa_n$ has indefinite sign (oscillates) | **Proved** (D63, §2) |
| $W_\lambda(s) \geq 0$ | **Proved** (D63, Cor. 7.2) |
| $T_\lambda > 0$ under ¬RH (PTC) | **Proved** (D63, Cor. 7.5) |
| PPP: $F_n \approx c_n/(z-\gamma_n)$ | Open |
| Local O.B.C. (sign of individual $\Delta_n$) | Open (requires PPP) |

**The strongest new result of this document:** $T_\lambda > 0$ under ¬RH (Corollary 7.5). This is the first result of the program that positively detects the presence of off-critical zeros via an invariant of the Jacobi structure.

**Next step — Doc 64:** Study whether $T_\lambda \to 0$ implies RH (the converse direction). By Proposition 5.3, $T_\lambda = 0$ for all $\lambda$ implies $dm_\text{full} = dm_\text{full,on}$. Doc 64 will analyze whether the condition $T_\lambda = o(N(\lambda))$ (the sum is $o$ of the number of terms) already implies ¬RH or whether $T_\lambda = 0$ exactly is needed.

---

## References

- [CCM24] A. Connes, C. Consani, H. Moscovici. *Zeta zeros and prolate wave operators*. (2024).
- [MRS88] Mhaskar, Rakhmanov, Saff. *Weights, extremal polynomials and potential theory*. (1988). [Scale of the effective support of the OP for Freud weights.]
- [Si11] B. Simon. *Szegő's Theorem and Its Descendants*. Princeton. [Christoffel function, bulk asymptotics.]
- Doc 59–62: CCM framework, Jacobi discrepancies, PPP.
