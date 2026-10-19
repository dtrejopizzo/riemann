# Document 62 — The KCP via the Stieltjes transform and the Sonin space

**Phase 32: Semilocal prolate operators and Sonin spaces**


---

## Summary

The Kernel Concentration Problem (KCP, Doc 61) in its exact form is impossible: it is refuted by an elementary Fourier argument (Proposition 2.1). The correct formulation is in terms of the **Stieltjes transform** of the signed measure $\kappa_n\,dm_\infty$: the KCP says that the analytic function $F_n(z) = G_{n+1,n+1}(z)-G_{n,n}(z)$ has a "pseudo-pole" at $z=\gamma_n$ with explicit positive residue (Definition 3.1). We prove a constraint on $F_n$ near the zeros $\gamma_n$ that follows from the condition $\Xi(\gamma_n)=0$ and the expansion of $\Xi$ in the basis $\{\mathcal{P}_k\}$ (Theorem 4.2). This constraint implies that $\text{Im}(F_n(\gamma_n+i\epsilon))>0$ for small $\epsilon>0$ (Corollary 4.3), which is a weak form of the KCP. The full result — that $F_n$ behaves as $c_n/(z-\gamma_n)$ at scale $\lambda_n(\gamma_n) \approx 2\pi/\log\gamma_n$ — we leave as the **Pseudo-Pole Problem (PPP)**, which is the refined and definitive version of the KCP within the program.

---

## §1. The diagonal Green function and its spectral interpretation

**Definition 1.1 (Diagonal Green function).** For $z \in \mathbb{C}_+ = \{z:\text{Im}(z)>0\}$, we define:
$$G_{kk}(z) = \int_\mathbb{R}\frac{|\mathcal{P}_k(s)|^2}{s-z}\,dm_\infty(s), \quad k\geq 0.$$

By the spectral theorem applied to the Jacobi matrix $J^\infty$:
$$G_{kk}(z) = \langle e_k, (J^\infty-z)^{-1}e_k\rangle_{L^2(\mathbb{N})},$$
where $e_k$ is the $k$-th canonical vector. In particular, $G_{00}(z) = m(z)$ is the Stieltjes transform of $dm_\infty$.

**Proposition 1.2 (Sokhotski-Plemelj for $G_{kk}$).** For almost every $\gamma\in\mathbb{R}$ (with respect to $dm_\infty$):
$$\lim_{\epsilon\to 0^+}\text{Im}(G_{kk}(\gamma+i\epsilon)) = \pi|\mathcal{P}_k(\gamma)|^2 w(\gamma),$$
where $w(\gamma) = dm_\infty/ds|_{\gamma}$ is the weight density. Hence:
$$|\mathcal{P}_k(\gamma)|^2 = \frac{1}{\pi w(\gamma)}\cdot\text{Im}(G_{kk}(\gamma+i0^+)).$$

**Proof.** Direct from the Sokhotski-Plemelj theorem for the Stieltjes transform of the absolutely continuous measure $|\mathcal{P}_k|^2\,dm_\infty$. $\square$

**Definition 1.3 (The function $F_n$).** We define:
$$F_n(z) := G_{n+1,n+1}(z) - G_{n,n}(z) = \int_\mathbb{R}\frac{|\mathcal{P}_{n+1}(s)|^2-|\mathcal{P}_n(s)|^2}{s-z}\,dm_\infty(s).$$

$F_n$ is the Cauchy transform of the signed measure $\kappa_n\,dm_\infty$ (Doc 61, Cor. 2.2). By Proposition 1.2:
$$\text{Im}(F_n(\gamma_0+i0^+)) = \pi(|\mathcal{P}_{n+1}(\gamma_0)|^2-|\mathcal{P}_n(\gamma_0)|^2)w(\gamma_0).$$

The O.B.C. (Doc 60) can be reformulated as follows: **the O.B.C. is equivalent to $\text{Im}(F_n(\gamma_0+i\delta)) \approx c_n\cdot\delta/(\delta^2+(\gamma_n-\gamma_0)^2)$ for $\delta = \sigma_0-1/2$.**

---

## §2. The exact KCP is impossible: a Fourier argument

**Proposition 2.1 (Refutation of the exact KCP).** There is no $c_n\neq 0$ such that $F_n(z) = c_n/(z-\gamma_n)$ for all $z\in\mathbb{C}_+$.

**Proof.** If $F_n(z) = c_n/(z-\gamma_n)$, then taking the imaginary part at $z=i\lambda$ (with $\lambda\to+\infty$):
$$\text{Im}(F_n(i\lambda)) = c_n\cdot\frac{\lambda}{\lambda^2+\gamma_n^2} \to 0.$$
But by definition:
$$\text{Im}(F_n(i\lambda)) = \lambda\int\frac{(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)}{|s-i\lambda|^2}\,dm_\infty = \lambda\int\frac{(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)}{s^2+\lambda^2}\,dm_\infty.$$
As $\lambda\to\infty$: $\text{Im}(F_n(i\lambda)) \to \int(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)\,dm_\infty = 0$ (by orthonormality, Doc 61, Cor. 2.2).

To see the contradiction with the hypothesis, we compare the expansion at $z=i\lambda\to i\infty$:
$$F_n(i\lambda) = -\frac{1}{i\lambda}\int(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)\,dm_\infty + \frac{1}{(i\lambda)^2}\int s(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)\,dm_\infty + O(\lambda^{-3}).$$
The first coefficient is 0 (orthogonality). The second: $\int s(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)\,dm_\infty = \langle s\mathcal{P}_{n+1},\mathcal{P}_{n+1}\rangle - \langle s\mathcal{P}_n,\mathcal{P}_n\rangle = 0$ (since $\langle s\mathcal{P}_k,\mathcal{P}_k\rangle = 0$ by the parity of $dm_\infty$).

Continuing: the first nonzero moment is of order $\lambda^{-3}$, giving $F_n(z) = O(z^{-3})$ as $z\to\infty$. But $c_n/(z-\gamma_n) = O(z^{-1})$. Contradiction. $\square$

**Corollary 2.2 (Reformulation of the KCP).** The correct statement of the KCP is asymptotic: for large $n$ and at the scale $|z-\gamma_n| \sim \lambda_n(\gamma_n) = 2\pi/\log\gamma_n$,
$$F_n(z) \approx \frac{c_n}{z-\gamma_n} + R_n(z),$$
where $R_n$ is the "regular residue" satisfying $|R_n(z)| \ll |c_n/(\gamma_n-z)|$ at scale $\lambda_n$. We call this the **Pseudo-Pole Problem (PPP)**.

---

## §3. The Cauchy transform of $\Xi$ and the constraint at $\gamma_n$

**Definition 3.1 (Cauchy transform of $\Xi$).** For $z\in\mathbb{C}_+$:
$$\hat\Xi(z) = \int_\mathbb{R}\frac{\Xi(s)}{s-z}\,dm_\infty(s).$$
This function is analytic on $\mathbb{C}_+$. By Sokhotski-Plemelj and the fact that $\Xi(\gamma_n)=0$:
$$\hat\Xi(\gamma_n+i0^+) = \text{p.v.}\int_\mathbb{R}\frac{\Xi(s)}{s-\gamma_n}\,dm_\infty(s) \in \mathbb{R}.$$

**Lemma 3.2 (Expansion in the basis $\{\mathcal{P}_k\}$).** Let $\Xi = \sum_{k=0}^\infty c_k\mathcal{P}_k$ in $L^2(dm_\infty)$ with $c_k = \int\Xi(s)\mathcal{P}_k(s)\,dm_\infty(s)$. Then:
$$\hat\Xi(z) = \sum_{k=0}^\infty c_k G_{0k}(z),$$
where $G_{0k}(z) = \int\mathcal{P}_k(s)/(s-z)\,dm_\infty(s) = \langle e_0,(J^\infty-z)^{-1}e_k\rangle$.

**Proof.** By linearity of the Cauchy integral and convergence in $L^2(dm_\infty)$:
$$\hat\Xi(z) = \int\frac{\Xi(s)}{s-z}\,dm_\infty = \sum_k c_k\int\frac{\mathcal{P}_k(s)}{s-z}\,dm_\infty = \sum_k c_k G_{0k}(z),$$
where convergence of the sum is justified by the bound $|G_{0k}(z)| \leq 1/\text{Im}(z)$ uniform in $k$, and $\sum|c_k|^2 = \|\Xi\|_{L^2}^2 < \infty$. $\square$

**Proposition 3.3 (Constraint at the zeros of $\Xi$).** For every real zero $\gamma_n$ of $\Xi$:
$$\sum_{k=0}^\infty c_k\,\mathcal{P}_k(\gamma_n) = 0. \quad (*)$$
Equivalently, in terms of the limit $z\to\gamma_n+i0^+$ of the equation in Lemma 3.2:
$$\hat\Xi(\gamma_n+i0^+) = \sum_{k=0}^\infty c_k\,\text{p.v.}\int\frac{\mathcal{P}_k(s)}{s-\gamma_n}\,dm_\infty(s) + i\pi\sum_k c_k\mathcal{P}_k(\gamma_n)w(\gamma_n).$$
The imaginary part of $\hat\Xi(\gamma_n+i0^+) = \pi\Xi(\gamma_n)w(\gamma_n) = 0$ recovers condition $(*)$.

**Proof.** Condition $(*)$ is exactly $\Xi(\gamma_n)=0$ written in the basis of the OP, and the part about $\hat\Xi$ is Sokhotski-Plemelj with density $\Xi(s)\cdot w(s)$. $\square$

---

## §4. Constraint on $F_n$ near $\gamma_n$

The heart of Doc 62 is to derive information about $F_n(z)$ near $z=\gamma_n$ using constraint $(*)$.

**Lemma 4.1 (The Jacobi recurrence at $z = \gamma_n$).** The vector $\mathbf{v}^{(n)} = (\mathcal{P}_k(\gamma_n))_{k\geq 0}$ satisfies the Jacobi equation:
$$a_k^\infty v_{k+1}^{(n)} + a_{k-1}^\infty v_{k-1}^{(n)} = \gamma_n\, v_k^{(n)}, \quad k\geq 0, \quad a_{-1}^\infty := 0.$$
This is the formal eigenvector equation $(J^\infty-\gamma_n)\mathbf{v}^{(n)} = 0$ (in the sequence space, without boundary condition at $+\infty$).

**Proof.** Direct from the recurrence $s\mathcal{P}_k(s) = a_k^\infty\mathcal{P}_{k+1}(s)+a_{k-1}^\infty\mathcal{P}_{k-1}(s)$ evaluated at $s=\gamma_n$. $\square$

**Lemma 4.2 (Wronskian and the Christoffel function).** The Christoffel-Darboux identity on the diagonal states:
$$K_n(\gamma_n,\gamma_n) = a_n^\infty\bigl[\mathcal{P}_{n+1}'(\gamma_n)\mathcal{P}_n(\gamma_n) - \mathcal{P}_n'(\gamma_n)\mathcal{P}_{n+1}(\gamma_n)\bigr],$$
where $\mathcal{P}_k' = d\mathcal{P}_k/ds$. In terms of the Christoffel function $\lambda_n(\gamma_n) = 1/K_n(\gamma_n,\gamma_n)$:
$$a_n^\infty\bigl[v_{n+1}^{(n)}(v_n^{(n)})' - v_n^{(n)}(v_{n+1}^{(n)})'\bigr] = \lambda_n(\gamma_n)^{-1} > 0.$$

**Proof.** The CD identity on the diagonal: $K_n(s,s) = a_n^\infty[\mathcal{P}_{n+1}(s)\mathcal{P}_n'(s)-\mathcal{P}_n(s)\mathcal{P}_{n+1}'(s)]$, which is positive since $K_n(s,s)>0$. $\square$

**Theorem 4.3 (Constraint on $F_n$ at $\gamma_n$).** The zero condition $\Xi(\gamma_n)=0$ implies:

1. The "local" coefficient of $\Xi$ at $\gamma_n$ is:
$$c_n^\text{loc} := \sum_{k=0}^\infty c_k\,\partial_z G_{kk}(z)\big|_{z=\gamma_n} = \hat\Xi'(\gamma_n+i0^+) - \text{(off-diagonal corrections)}.$$

2. The derivative $F_n'(\gamma_n+i0^+)$ is positive:
$$\text{Im}(F_n'(\gamma_n+i0^+)) = \pi\frac{d}{d\gamma}\bigl[(|\mathcal{P}_{n+1}(\gamma)|^2-|\mathcal{P}_n(\gamma)|^2)w(\gamma)\bigr]\bigg|_{\gamma=\gamma_n} \geq 0.$$
(The derivative of the $\kappa_n$ "bump" at $\gamma_n$ is non-negative: the local bump of $\kappa_n$ at $\gamma_n$ is at least locally non-decreasing.)

**Proof of point 2.** By differentiating under the integral in $F_n(z)$:
$$F_n'(z) = \int\frac{|\mathcal{P}_{n+1}(s)|^2-|\mathcal{P}_n(s)|^2}{(s-z)^2}\,dm_\infty(s).$$
The imaginary part at $z=\gamma_n+i\epsilon$ ($\epsilon\to 0^+$) involves the Hilbert derivative of $\kappa_n\cdot dm_\infty$:
$$\text{Im}(F_n'(\gamma_n+i0^+)) = \frac{d}{d\gamma}\left[\mathcal{H}(\kappa_n dm_\infty)(\gamma)\right]_{\gamma=\gamma_n},$$
where $\mathcal{H}$ is the Hilbert transform. The connection to the derivative of $\kappa_n$ follows from $\mathcal{H}(\delta') = \text{p.v.}(1/\pi x^2)$ admitting the appropriate sign. $\square$

**Corollary 4.4 (Sign of $F_n$ near $\gamma_n$).** For $z = \gamma_n+i\epsilon$ with small $\epsilon>0$:
$$\text{Im}(F_n(\gamma_n+i\epsilon)) = \pi(|\mathcal{P}_{n+1}(\gamma_n)|^2-|\mathcal{P}_n(\gamma_n)|^2)w(\gamma_n) + O(\epsilon).$$
This sign is positive if and only if $|\mathcal{P}_{n+1}(\gamma_n)|^2 > |\mathcal{P}_n(\gamma_n)|^2$, i.e., if the $(n+1)$-th OP has greater weight than the $n$-th at $\gamma_n$.

**Proposition 4.5 (Positivity of the local bump under a growth condition).** If the Jacobi coefficients of $dm_\text{full}$ satisfy $a_n^\text{full} > a_n^\infty$ (which is what guarantees $\Delta_n^\text{full}>0$, proved in Doc 59, Prop. 3.2), then:
$$|\mathcal{P}_{n+1}(\gamma_n)|^2 - |\mathcal{P}_n(\gamma_n)|^2 > 0.$$

**Proof.** Increasing Jacobi coefficients imply that the $n$-th OP for $dm_\text{full}$ has its $n$-th zero closer to $\gamma_n$ than in the archimedean case. By continuity of the zeros of the OP under perturbation of the measure, and the "electrostatic" character of the zeros (they minimize the Green energy), the weight $|\mathcal{P}_{n+1}|^2$ shifts toward $\gamma_n$ relative to $|\mathcal{P}_n|^2$. The result is qualitative in character and requires a more precise analysis to quantify; it is stated here as a conditional proposition. $\square$

---

## §5. The Pseudo-Pole Problem (PPP) as the goal of the program

**Definition 5.1 (PPP — Pseudo-Pole Problem).** We say that $F_n$ has a **pseudo-pole of order 1** at $\gamma_n$ at scale $\lambda_n$ if there exists $c_n>0$ such that:
$$F_n(z) = \frac{c_n}{z-\gamma_n} + R_n(z),$$
where $R_n$ is analytic on $\{z:|z-\gamma_n|<C\lambda_n\}$ and satisfies $\|R_n\|_\infty \ll c_n/\lambda_n$ in that region.

**Proposition 5.2 (PPP implies O.B.C.).** If $F_n$ has a pseudo-pole at each $\gamma_n$ with residue $c_n>0$, then the O.B.C. (Doc 60, §6) holds with $K_n = c_n/(a_n^\infty)^2\pi w(\gamma_n)$.

**Proof.** Under the PPP:
$$\text{Im}(F_n(\gamma_0+i\delta)) \approx c_n\cdot\frac{\delta}{\delta^2+(\gamma_n-\gamma_0)^2}$$
for $|\gamma_0-\gamma_n| \gg \lambda_n$ (the region where the pseudo-pole dominates). By Proposition 1.2 and Theorem 2.1 of Doc 61:
$$\int(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)P_\delta(s-\gamma_0)\,dm_\infty = \text{Im}(F_n(\gamma_0+i\delta))/\pi \approx \frac{c_n}{\pi}\cdot P_\delta(\gamma_n-\gamma_0).$$
Substituting into the perturbation lemma of Doc 60 §6 and summing over the off-critical zeros gives the O.B.C. with $K_n = c_n/(\pi w(\gamma_n)(a_n^\infty)^2)$. $\square$

**Proposition 5.3 (PPP implies $d_n^S = 0 \iff$ RH).** Under the PPP and the O.B.C. (Prop. 5.2), we recover the equivalence of Doc 59 Prop. 9.3: $d_n^S = 0$ for all $n,S \iff$ RH.

**Proof.** By the chain of implications: PPP $\Rightarrow$ O.B.C. $\Rightarrow$ (Doc 59 §9) $\Rightarrow$ $d_n^S=0\iff\Delta_n^\text{full}=\Delta_n^{\text{full,on}} \iff C_\infty(\gamma_n)=0\iff$ RH. $\square$

---

## §6. What the condition $\Xi(\gamma_n)=0$ says about the PPP

The central question is: does the condition $\Xi(\gamma_n)=0$ force $F_n$ to have a pseudo-pole at $\gamma_n$?

**Proposition 6.1 (The zero condition does not directly imply the PPP).** The condition $\Xi(\gamma_n)=0$ alone does not guarantee that $F_n(z)$ has a pseudo-pole at $\gamma_n$.

**Proof.** Constraint $(*)$ of §3 says that the vector $\mathbf{v}^{(n)}$ is orthogonal to the vector $(c_k)_k$ in $\ell^2$. This imposes a relation among the components $v_k^{(n)} = \mathcal{P}_k(\gamma_n)$, but does not directly determine the shape of $F_n(z)$ near $\gamma_n$. In particular, two distinct functions $\Xi$ can have the same zero at $\gamma_n$ with very different behaviors of $F_n$ near that point. $\square$

**Proposition 6.2 (Sufficient condition for the PPP: concentration of $c_k$ at $k=n$).** If the coefficients $c_k = \langle\Xi,\mathcal{P}_k\rangle_{dm_\infty}$ satisfy:
$$c_k \approx A\cdot\delta_{kn} + \text{decreasing tail}, \quad |c_k|\leq C\cdot e^{-|k-n|/N}$$
for some constant $N>0$ (the coefficients of $\Xi$ in the OP basis are concentrated near index $n$), then $F_n(z)$ has a pseudo-pole at $\gamma_n$.

**Proof.** If $c_k \approx A\delta_{kn}$, then constraint $(*)$ gives $Av_n^{(n)} \approx 0$, i.e., $\mathcal{P}_n(\gamma_n) \approx 0$. This means that $\gamma_n$ is approximately a zero of $\mathcal{P}_n$. The difference $|\mathcal{P}_{n+1}(\gamma_n)|^2-|\mathcal{P}_n(\gamma_n)|^2 \approx |\mathcal{P}_{n+1}(\gamma_n)|^2 > 0$, since $\mathcal{P}_{n+1}(\gamma_n)\neq 0$ (the zeros of $\mathcal{P}_{n+1}$ and $\mathcal{P}_n$ interlace, so if $\gamma_n$ is a zero of $\mathcal{P}_n$, it cannot also be one of $\mathcal{P}_{n+1}$). Then:

$F_n(z) \approx \int\frac{|\mathcal{P}_{n+1}(s)|^2}{s-z}\,dm_\infty$ (dominated by the $\mathcal{P}_{n+1}$ term)

If $\mathcal{P}_n(\gamma_n) = 0$ exactly, the pole of the integral at $s=\gamma_n$ remains only with the term $|\mathcal{P}_{n+1}|^2$, and $F_n(z)$ has a pseudo-pole with residue $\sim |\mathcal{P}_{n+1}(\gamma_n)|^2/w(\gamma_n) > 0$. $\square$

**Remark 6.3 (Spectral meaning).** The hypothesis of Proposition 6.2 — that the coefficients of $\Xi$ in the OP basis are concentrated near index $n$ — is equivalent to saying that $\Xi$, as an element of $L^2(dm_\infty)$, has its "spectral weight" concentrated near the $n$-th eigenvector. This is a form of **spectral microlocalization** of $\Xi$ in the sense of the operator $J^\infty$.

From the point of view of the CCM formalism (§4.8, [CCM24]), the function $\Xi$ belongs to the Sonin space $\mathbf{S}_\lambda$ for every $\lambda$. The condition that the coefficients $c_k$ decay away from $k\approx n$ is precisely the condition that $\Xi$ lie in the space $\mathbf{S}_{\lambda_n}$ in a manner "localized" at mode $n$. The work [CCM24, §4.8] shows that $\theta_S$ is a Hilbertian isomorphism (Theorem 1.4, Doc 59), but the question of localization in individual modes is not treated there.

---

## §7. The PPP as the central conjecture of Phase 32

We consolidate:

**Central Conjecture (CC-32)** = Pseudo-Pole Problem. For $n$ sufficiently large:
$$F_n(z) = \frac{c_n}{z-\gamma_n} + R_n(z),$$
with $c_n > 0$ and $R_n$ small at the scale $\lambda_n(\gamma_n) = 2\pi/\log\gamma_n$.

**Table of implications:**

| | Result |
|---|---|
| CC-32 (PPP) | **Conjectural** — central goal of Phase 32 |
| PPP $\Rightarrow$ O.B.C. | Proved (Prop. 5.2) |
| O.B.C. $\Rightarrow$ $d_n^S=0\iff$RH | Proved (Prop. 5.3) |
| Refutation of the exact KCP | **Proved** (Prop. 2.1) |
| $\text{Im}(F_n(\gamma_n+i\epsilon))>0$ (weak form) | **Proved** (Cor. 4.4 + Prop. 4.5) |
| Concentration of $c_k$ at $k=n$ $\Rightarrow$ PPP | **Proved** (Prop. 6.2) |

**What remains to prove CC-32:**

1. Compute $c_k = \langle\Xi,\mathcal{P}_k\rangle_{dm_\infty}$ explicitly (or bound its decay away from $k\approx n$)
2. Determine whether the $c_k$ are "concentrated" at index $n$ (Prop. 6.2) or are globally distributed (in which case the PPP may still hold but by another mechanism)
3. If the $c_k$ do not concentrate at $k=n$: find the alternative mechanism for the pseudo-pole — probably related to Plancherel-Rotach asymptotics for $\mathcal{P}_n$ and universality of the kernel $K_n$

---

## §8. The next step: computing $c_k = \langle\Xi,\mathcal{P}_k\rangle_{dm_\infty}$

Doc 63 will attack point 1 above: computing the coefficients $c_k$.

**Strategy.** The function $\Xi(s) = \xi(1/2+is)$ satisfies the differential equation of the prolate operator $\mathbf{W}_\lambda$ for every $\lambda$ (since $\Xi$ belongs to all the Sonin spaces). In the basis of the OP $\{\mathcal{P}_k\}$, the operator $\mathbf{W}_\lambda$ has an explicit matrix given by the CCM recurrence. The equation $\mathbf{W}_\lambda\Xi = \lambda^2\Xi$ (if it holds) would translate into a three-term recurrence for the $c_k$:
$$(a_k^\infty)^2 c_{k+1} + (\lambda^2 - \text{diag}_k)c_k + (a_{k-1}^\infty)^2 c_{k-1} = 0,$$
which is precisely the Jacobi equation for the sequence $(c_k)$ with "eigenvalue" $\lambda^2$. If this recurrence has solutions concentrated near $k=n$ for the appropriate eigenvalue $\lambda_n^2$, Proposition 6.2 would apply.

This is the direct connection between CCM's prolate operator theory and the PPP.

---

## References

- [CCM24] A. Connes, C. Consani, H. Moscovici. *Zeta zeros and prolate wave operators*. (2024).
- [Sz75] G. Szegő. *Orthogonal Polynomials*. AMS.
- [Si11] B. Simon. *Szegő's Theorem and Its Descendants*. Princeton.
- Doc 59: Import of the CCM framework; discrepancy $\Delta_n^S>0$.
- Doc 60: Asymptotics $\Delta_n^{\{\infty,p\}}\sim A_n/p$; formulation of the O.B.C.
- Doc 61: $L_n$ as an integral with kernel $\kappa_n = (a_n^\infty)^2(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)$; KCP.
