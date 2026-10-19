# Phase 29 — Doc 37: Connection with Random Matrix Theory and Montgomery's Conjecture

**Objective:** Examine whether Random Matrix Theory (RMT), specifically Montgomery's pair-correlation conjecture and the GUE structure of the zeros of $\zeta$, can provide evidence or a proof path for Inc. Inv. and ultimately RH.

---

## 1. Context: the obstacle from Doc 35 (Direction D)

In Doc 35 (Direction D, Szegő/Delocalization) it was shown that:

- Jacobi operators with $b_n \to \infty$ and $a_n \to 0$ (the $J_\infty$ regime) generically exhibit eigenvector LOCALIZATION.
- The first-order perturbation gives $|c_n|^2 \approx a_0^2/\gamma_n^2 \to 0$ — exactly the opposite behavior to delocalization.
- The Inc. Inv. condition ($|c_n|^2 = 1/N$, equipartition in the limit) requires a SPECIAL ARITHMETIC property of the zeros of $\zeta$, not a generic property of Jacobi operators.

**The question:** Is that special arithmetic property precisely the GUE statistics that RMT predicts for the zeros of $\zeta$?

---

## 2. Montgomery's conjecture (1973)

**Definition 1** (pair correlation function). For $T > 0$ and $f \in S(\mathbb{R})$ (Schwartz), the normalized pair correlation function of the zeros of $\zeta$ in $[0,T]$ is:

$$F(\alpha, T) = \frac{2\pi}{T \log T} \sum_{\substack{0 < \gamma, \gamma' \leq T \\ \gamma \neq \gamma'}} f\!\left(\frac{(\gamma-\gamma')\log T}{2\pi}\right),$$

where the sum runs over pairs of zeros $\rho = 1/2 + i\gamma$, $\rho' = 1/2+i\gamma'$ (implicitly assuming RH in this formulation).

**Montgomery's conjecture (1973).** For $f$ with support in $(-1,1)$ (strong conjecture) or for $\hat f$ with support in $(-1,1)$ (original version):

$$\lim_{T\to\infty} F(\alpha, T) = \int_{-\infty}^\infty f(x)\left[1 - \left(\frac{\sin\pi x}{\pi x}\right)^2\right]dx.$$

The function $1 - (\sin\pi x/\pi x)^2$ is precisely the pair correlation function of the eigenvalues of GUE (Gaussian Unitary Ensemble) random matrices.

**Note on honesty.** Montgomery's conjecture is:
- PROVED for $\hat f$ with support in $(-1,1)$ (Montgomery 1973, conditional on RH).
- NOT PROVED in general — it is an open conjecture.
- Supported by extensive numerical evidence (Odlyzko 1987–2001).

---

## 3. The connection with Jacobi operators and delocalization

**Proposition 1** (correlations and eigenvectors). Let $J_\lambda^N$ be the Jacobi operator from the CCM construction, with eigenvalues $\{t_n^{(\lambda)}\}_{n=1}^N$ and eigenvectors $\{\mathbf{v}_n^{(\lambda)}\}_{n=1}^N$. The coefficient $c_n^{(\lambda)} = \langle \mathbf{v}_n^{(\lambda)}, \mathbf{e}_1\rangle$ satisfies (from Doc 22):

$$|c_n^{(\lambda)}|^2 = \frac{1}{N} \iff m_\lambda^{WT}(z) = m_\lambda^{emp}(z) \text{ for all } z.$$

The condition $|c_n^{(\lambda)}|^2 = 1/N$ (equipartition, = maximal delocalization in the sense of the point $\mathbf{e}_1$) is equivalent to the spectral measure centered at $\mathbf{e}_1$ being the empirical eigenvalue measure.

**Proposition 2** (the role of correlations). If the eigenvalues $t_n^{(\lambda)}$ have the same pair correlation structure as the zeros of $\zeta$ on the $1/\log T$ scale: then, by GUE universality, the eigenvectors of $J_\lambda^N$ should satisfy GOE/GUE delocalization.

*Motivation:* For $N \times N$ GUE matrices: the eigenvalues have pair correlation statistics with sinusoidal kernel $1-(\sin\pi x/\pi x)^2$, AND the eigenvectors are uniformly distributed on the unit sphere of $\mathbb{C}^N$ (by unitary invariance). This implies $\mathbb{E}[|c_n|^2] = 1/N$ for every $n$ — exactly equipartition.

---

## 4. The random Jacobi model: the technical barrier

The connection between RMT and delocalization for $J_\infty$ requires overcoming a fundamental barrier.

**The GUE model is NOT a Jacobi operator in the sense of $J_\infty$.**

GUE has:
- Diagonal entries: $b_n \sim \mathcal{N}(0,1)$ (bounded on average, fixed variance).
- Off-diagonal entries: $a_n \sim \mathcal{N}(0,1)/\sqrt{2}$ (bounded).

The operator $J_\infty$ has:
- Diagonal entries: $b_n = \gamma_n \to \infty$ (UNBOUNDED).
- Off-diagonal entries: $a_n \to 0$ (go to 0).

**Proposition 3** (regime incompatibility). The eigenvector delocalization of GUE matrices (proved via unitary invariance) applies to the BOUNDED regime. The operator $J_\infty$ lives in the UNBOUNDED regime. GUE-type delocalization theorems do not apply directly.

**Corollary 1** (what the RMT analogy CANNOT do). There is no theorem in the literature asserting: "if the spectrum of $J_\infty$ has GUE correlations, then the eigenvectors are delocalized." This implication is an unestablished conjecture for the $b_n \to \infty$ regime.

---

## 5. The path toward RMT: the comparison operator

**Definition 2** (rescaled Jacobi operator). For each scale $T > 0$, let $J_\infty^{(T)}$ be the Jacobi operator with the zeros of $\zeta$ in $[0,T]$ rescaled to $[-2,2]$ (GUE scale). On the local scale (of $1/\log T$): the eigenvalues $t_n^{(\lambda)}$ have spacings $\sim 2\pi/\log T$ between consecutive zeros.

**Proposition 4** (the local scale and universality). On the local scale:

$$\frac{(t_{n+1}^{(\lambda)} - t_n^{(\lambda)})\log T}{2\pi} \to \text{distribution according to zero statistics of }\zeta.$$

If the zero statistics of $\zeta$ are GUE (Montgomery's conjecture), on the local scale the zeros are "almost GUE." For Jacobi operators on the local scale with GUE spectrum: local delocalization would be expected.

**BUT:** LOCAL delocalization (on the $1/\log T$ scale) does not directly imply GLOBAL equipartition $|c_n^{(\lambda)}|^2 = 1/N$ (which requires delocalization on the GLOBAL scale of $[0,T]$).

---

## 6. Montgomery's result and the function $\hat k_\lambda$

**Proposition 5** (Montgomery's conjecture as a constraint on $\hat k_\lambda$). The function $\hat k_\lambda$ of the CCM program is the discrete Weil kernel — an approximation of the continuous kernel $k_\lambda$. Its zeros in $\mathbb{C}^+$ reflect the structure of the zeros of $\Xi$ in the relevant region.

The pair correlation function of the zeros of $\hat k_\lambda$ on the local scale is related to the pair correlation function of the zeros of $\Xi$ (= zeros of $\zeta$ on the critical line, under RH).

If Montgomery's conjecture is true: the zeros of $\hat k_\lambda$ (which approximate the zeros of $\Xi$) have GUE structure on the local scale. This means that in the neighborhood of any zero $\gamma_n$, the zeros of $\hat k_\lambda$ repel each other according to the GUE rule: the probability that two zeros are at distance $s$ decreases like $s^2$ as $s \to 0$ (quadratic repulsion, GUE level = $\beta = 2$).

---

## 7. The heuristic argument: RMT + CCM → Inc. Inv.

**Heuristic argument (NOT a proof).** Assuming Montgomery's conjecture (GUE structure of the zeros of $\zeta$), the following argument suggests that Inc. Inv. might be derivable:

**Step 1.** GUE repulsion implies that on the local scale, the zeros of $\hat k_\lambda$ and the eigenvalues of $J_\lambda^N$ are statistically INDISTINGUISHABLE (if $J_\lambda^N$ inherited the same statistics). In particular, the "mean distance" between the two sets is $o(1/\log T)$ — the eigenvalues converge to the zeros of $\hat k_\lambda$ faster than the spacing scale.

**Step 2.** If the eigenvalues $t_n^{(\lambda)}$ and the zeros of $\hat k_\lambda$ converge (in the limit $\lambda \to \infty$) to the same set — the zeros of $\Xi$ — this is exactly Inc. Inv.

**Problem with Step 2.** Step 2 requires justifying that the convergence $t_n^{(\lambda)} \to \gamma_n$ is more than "statistical" — that there is a POINTWISE convergence of each eigenvalue to its corresponding zero. GUE statistics only give convergence of the empirical measure (weak), not pointwise convergence.

**Proposition 6** (the gap between statistical and pointwise convergence). Convergence of the empirical measure:

$$\frac{1}{N}\sum_n \delta_{t_n^{(\lambda)}} \xrightarrow{w} \frac{1}{N}\sum_n \delta_{\gamma_n}$$

is a STATISTICAL statement that does not imply $t_n^{(\lambda)} \to \gamma_n$ for each individual $n$ (this fails for indeterminate measures, as shown by Doc 26 for $\mu_\gamma^{real}$).

---

## 8. Montgomery's conjecture and the complex zeros of $C_\lambda - \mu_\lambda$

The audit in Doc 36 identified the key question:

> Can it be proved that the complex zeros of $C_\lambda - \mu_\lambda$ in the strip $0 < \Im(z) \leq \eta$ escape as $\lambda \to \infty$?

**Proposition 7** (RMT's contribution to the strip question). Suppose Montgomery's conjecture. The zeros of $\hat k_\lambda$ in the strip $0 < \Im(z) \leq \eta$ converge (by the RMT analogy and the Fredholm determinant theory of GUE matrices) to the zeros of $\Xi$ in that strip.

Under RH: there are no zeros of $\Xi$ in the strip → $N_{\hat k_\lambda}^{\text{strip}}(T,\eta) \to 0$.

By $(C_\lambda')$: $N_{C_\lambda-\mu_\lambda}^{\text{strip}}(T,\eta) \to N_\Xi^{\text{real}}(T)$ (the complex zeros of $C_\lambda - \mu_\lambda$ in the strip remain in number $N_\Xi(T)$ for each finite $\lambda$, but must escape to the edge of the strip $\Im(z) = \eta$ in the limit).

**The precise question transforms.** RMT (under Montgomery's conjecture) gives information about the zeros of $\hat k_\lambda$ in the strip, but the question about the complex zeros of $C_\lambda - \mu_\lambda$ in the strip is INDEPENDENT: it is a question about the POTENTIAL $C_\lambda$, not about $\hat k_\lambda$.

---

## 9. The fundamental obstruction and the new question

**Proposition 8** (fundamental obstruction of the RMT route). The contribution of Random Matrix Theory to proving Inc. Inv. (and RH) faces the following obstruction:

(a) **RMT describes global statistics.** Montgomery's conjecture gives the correlation structure at the mean spacing scale ($1/\log T$). Inc. Inv. requires POINTWISE convergence of each eigenvalue to its corresponding zero.

(b) **The regime is wrong.** Delocalization theorems for GUE apply to bounded matrices. $J_\infty$ has unbounded spectrum and $a_n \to 0$ — a regime for which no analogous delocalization theorems exist.

(c) **The gap is an INPUT, not an OUTPUT.** If RH is assumed (all zeros on the critical line), Montgomery's conjecture provides the GUE statistics of the zeros. But to use this to PROVE RH, one would need to prove GUE without assuming RH — and Montgomery's conjecture IS CONDITIONAL on RH.

**Corollary 2** (the vicious circle). The complete logical chain is:

$$\text{RH} \Rightarrow \text{Montgomery's conj. (GUE)} \Rightarrow \text{Delocalization of }J_\infty \Rightarrow \text{Inc. Inv.} \Rightarrow \text{RH}.$$

The first implication is conditional (Montgomery 1973), the intermediate implications are conjectures, and the last is Theorem D from Doc 19. The whole circle is circular: it does not give a new proof of RH without the input hypothesis.

---

## 10. What RMT genuinely contributes to the program

Despite the obstructions, RMT contributes the following, which can be USEFUL:

**Contribution A (strong heuristic evidence).** The numerical consistency of the spectrum of $J_\lambda^N$ with GUE (at local scales) provides heuristic evidence that Inc. Inv. is true. This is not a proof but it orients the program.

**Contribution B (the question of the zeros of $C_\lambda - \mu_\lambda$ in the strip).** The question that Doc 36 identifies as the new path — do the complex zeros of $C_\lambda - \mu_\lambda$ in the strip escape unconditionally? — is an ANALYTIC question about the potential $C_\lambda$, not a spectral question. RMT does not answer it but identifies what is needed: a proof that the function $C_\lambda(z) = \mu_\lambda$ has no complex solutions in the strip for large $\lambda$.

**Contribution C (Montgomery's theorem as conditional).** If Inc. Inv. is proved by other means: Theorem D (Inc. Inv. $\Rightarrow$ RH, Doc 19) completes the proof. And Montgomery's conjecture would then give a precise description of the spectral statistics of $J_\infty$ — an elegant consequence of the CCM program.

**Contribution D (new sub-program).** Directly study the distribution of the complex zeros of $C_\lambda - \mu_\lambda$ in the strip $0 < \Im(z) \leq \eta$ as a function of $\lambda$. If it can be shown that these zeros move toward $\Im(z) = \eta$ as $\lambda$ grows (with controllable speed): that would prove that there are no zeros of $C_\infty$ in the strip — which is weaker than RH but a real advance.

---

## 11. Conclusion: the state of Direction D (updated)

**Synthesis of Docs 35 and 37.** Direction D (Szegő/Delocalization/RMT) reveals:

1. Eigenvector delocalization of $J_\infty$ is NOT a generic property (Doc 35): it requires special arithmetic properties of the zeros of $\zeta$.

2. The arithmetic properties in question are exactly those predicted by Montgomery's conjecture (GUE) — but that conjecture is conditional on RH (Doc 37).

3. The RMT connection creates a vicious circle (Doc 37, Corollary 2) that does not allow for a new proof.

4. However, the route is not completely closed: the question of the complex zeros of $C_\lambda - \mu_\lambda$ in the strip (Doc 36, §9; Doc 37, §8) is an ANALYTIC question independent of RMT — and potentially attackable.

**State of Direction D:** Deep wall identified. The only genuine opening is the analytic strip question (via the audit in Doc 36, Prop. 10).

---

## 12. Executive summary for the Program

**After Docs 32-37 (Phase 30/Phase 29):**

| Direction | State | Main blockage |
|-----------|--------|-------------------|
| A (Pointwise Weil) | Closed | The Weil formula is distributional, not pointwise |
| B (EF2-emp Counting) | Resolved (audit) | Doc 32's argument was invalid; the strip question is new |
| C (Phragmén-Lindelöf) | Circular | PL presupposes holomorphy of Q |
| D (Szegő/RMT) | Deep wall | Montgomery's conjecture is conditional on RH |

**The only unclosed opening:** The question of the complex zeros of $C_\lambda - \mu_\lambda$ in the strip, identified in Doc 36. It is proposed as Phase 31.

---

*Next: Phase 31 — Analysis of the complex zeros of $C_\lambda - \mu_\lambda$ in the strip $0 < \Im(z) \leq \eta$.*
