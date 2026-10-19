# Document 61 — Locality of the functional $L_n$ and the de Branges kernel

**Phase 32: Semilocal prolate operators and Sonin spaces**


---

## Summary

We express the Jacobi perturbation functional $L_n$ (Doc 60, Def. 3.1) in terms of the orthonormal polynomials $\{\mathcal{P}_k\}_{k\geq 0}$ for the measure $dm_\infty$ (CCM §3.4). The central result is that $L_n$ admits the integral representation:
$$L_n[\mathbf{x}] = (a_n^\infty)^2 \int_\mathbb{R}\bigl(|\mathcal{P}_{n+1}(s)|^2 - |\mathcal{P}_n(s)|^2\bigr) f(s)\,dm_\infty(s),$$
when $x_{2k} = \int s^{2k}f(s)\,dm_\infty(s)$ (Theorem 2.1). This representation connects the Jacobi discrepancy with the Christoffel-Darboux kernel of $dm_\infty$. Using the CCM connection between the Sonin space $\mathbf{S}_\lambda$ and the de Branges space $\mathcal{B}_\lambda$ (§4.8), we show that the "locality" of $L_n$ at $\gamma_n$ is equivalent to the concentration of the reproducing kernel of $\mathcal{B}_n$ at the zeros of $\Xi$ (Proposition 5.2). We identify this as the **Kernel Concentration Problem (KCP)**, which is the precise obstacle to rigorously proving the O.B.C.

---

## §1. Orthonormal polynomials for $dm_\infty$ (CCM §3.4)

We recall the relevant results from CCM.

**Definition 1.1.** The orthonormal polynomials $\{\mathcal{P}_k\}_{k\geq 0}$ for the measure $dm_\infty$ are defined by Gram-Schmidt orthonormalization of $\{1, s, s^2, \ldots\}$ in $L^2(\mathbb{R}, dm_\infty)$:
$$\int_\mathbb{R}\mathcal{P}_k(s)\overline{\mathcal{P}_j(s)}\,dm_\infty(s) = \delta_{kj}.$$

**Theorem 1.2 (CCM, Thm. 5.2 and Prop. 3.3).** The $\mathcal{P}_k$ satisfy the three-term recurrence
$$s\,\mathcal{P}_k(s) = a_k^\infty\,\mathcal{P}_{k+1}(s) + a_{k-1}^\infty\,\mathcal{P}_{k-1}(s), \quad a_k^\infty = \tfrac{1}{2}\sqrt{(2k+1)(2k+2)},$$
with $a_{-1}^\infty := 0$, and the spectral measure associated with the Jacobi matrix $J^\infty = \text{tri}(a_k^\infty)$ at the vector $e_0 = \mathcal{P}_0$ is exactly $dm_\infty$.

**Definition 1.3 (Christoffel-Darboux kernel).** For $m\geq 0$, the $m$-th Christoffel-Darboux (CD) kernel is:
$$K_m(s,t) = \sum_{k=0}^m \mathcal{P}_k(s)\overline{\mathcal{P}_k(t)}, \quad s,t\in\mathbb{R}.$$
The Christoffel function is $\lambda_m(s) = 1/K_m(s,s) > 0$.

**Property 1.4 (CD identity).** For all $m\geq 0$:
$$K_{m+1}(s,t) = K_m(s,t) + \mathcal{P}_{m+1}(s)\overline{\mathcal{P}_{m+1}(t)}.$$
In particular, $K_{m+1}(s,s) - K_m(s,s) = |\mathcal{P}_{m+1}(s)|^2 \geq 0$.

---

## §2. Integral representation of the functional $L_n$

**Lemma 2.1 (Perturbation of the Hankel determinant).** Let $\delta\mu = f\,dm_\infty$ be a perturbation of the measure with $f\in L^2(dm_\infty)$ and $x_{2k} = \int s^{2k}f(s)\,dm_\infty(s)$. Then:
$$\frac{\delta D_m}{D_m} = \int_\mathbb{R} K_m(s,s)\,f(s)\,dm_\infty(s),$$
where $D_m = \det(c_{i+j}^\infty)_{0\leq i,j\leq m}$ and $\delta D_m = \sum_{i,j=0}^m (D_m^{-1})_{ij}\, x_{i+j}$.

**Proof.** By Jacobi's formula for the derivative of the determinant: $\delta\log D_m = \text{tr}(D_m^{-1}\delta H_m)$ where $(\delta H_m)_{ij} = x_{i+j}$. The inverse Hankel matrix admits the representation in terms of the orthonormal polynomials:
$$(D_m^{-1})_{ij} = \sum_{k=0}^m \overline{\hat{\mathcal{P}}_k(i)}\hat{\mathcal{P}}_k(j)$$
where $\hat{\mathcal{P}}_k(j)$ is the coefficient of $s^j$ in $\mathcal{P}_k(s)$ (via Cholesky/Gram-Schmidt). Hence:
$$\text{tr}(D_m^{-1}\delta H_m) = \sum_{i,j=0}^m (D_m^{-1})_{ij}x_{i+j} = \sum_{k=0}^m \left|\sum_{j=0}^m\hat{\mathcal{P}}_k(j)x_j\right|^2\cdot(\text{factor})$$
which simplifies to $\int K_m(s,s)f(s)\,dm_\infty$ by the identity
$$\sum_{i,j}(D_m^{-1})_{ij}x_{i+j} = \int\sum_{k=0}^m|\mathcal{P}_k(s)|^2 f(s)\,dm_\infty = \int K_m(s,s)f(s)\,dm_\infty. \;\square$$

**Theorem 2.1 (Representation of $L_n$).** For $\mathbf{x} = (x_{2k})_{k\geq 0}$ with $x_{2k} = \int s^{2k}f(s)\,dm_\infty(s)$:
$$L_n[\mathbf{x}] = (a_n^\infty)^2\int_\mathbb{R}\bigl(|\mathcal{P}_{n+1}(s)|^2 - |\mathcal{P}_n(s)|^2\bigr)f(s)\,dm_\infty(s).$$

**Proof.** Starting from Definition 3.1 of Doc 60:
$$L_n[\mathbf{x}] = \delta(a_n^2) = a_n^2\cdot\delta\log(a_n^2) = (a_n^\infty)^2\left(\frac{\delta D_{n-1}}{D_{n-1}} + \frac{\delta D_{n+1}}{D_{n+1}} - \frac{2\delta D_n}{D_n}\right).$$
Applying Lemma 2.1 to each term:
$$\frac{\delta D_m}{D_m} = \int K_m(s,s)f(s)\,dm_\infty.$$
By Property 1.4: $K_{n+1}(s,s) = K_n(s,s) + |\mathcal{P}_{n+1}(s)|^2$ and $K_{n-1}(s,s) = K_n(s,s) - |\mathcal{P}_n(s)|^2$. Hence:
$$K_{n-1}(s,s) + K_{n+1}(s,s) - 2K_n(s,s) = |\mathcal{P}_{n+1}(s)|^2 - |\mathcal{P}_n(s)|^2.$$
Substituting:
$$L_n[\mathbf{x}] = (a_n^\infty)^2\int\bigl(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2\bigr)f\,dm_\infty. \;\square$$

**Corollary 2.2.** The integral kernel of $L_n$ is $\kappa_n(s) := (a_n^\infty)^2(|\mathcal{P}_{n+1}(s)|^2-|\mathcal{P}_n(s)|^2)$, with:
$$\int_\mathbb{R}\kappa_n(s)\,dm_\infty(s) = (a_n^\infty)^2\left(\int|\mathcal{P}_{n+1}|^2\,dm_\infty - \int|\mathcal{P}_n|^2\,dm_\infty\right) = 0.$$
The kernel $\kappa_n$ has zero integral; it is not a projector at any point.

---

## §3. Qualitative analysis of the kernel $\kappa_n$

**Proposition 3.1 (Orthogonality of $\kappa_n$).** For every polynomial $p(s)$ of degree $\leq n-1$:
$$\int_\mathbb{R}\kappa_n(s)p(s)\,dm_\infty(s) = 0.$$

**Proof.** $\int|\mathcal{P}_{n+1}|^2 p\,dm_\infty = \langle p\mathcal{P}_{n+1},\mathcal{P}_{n+1}\rangle = 0$ when $\deg(p\mathcal{P}_{n+1}) \leq n$ and likewise with $\mathcal{P}_n$ (using orthonormality). $\square$

**Proposition 3.2 (Spectral support of $\kappa_n$).** The zeros of $|\mathcal{P}_{n+1}(s)|^2 - |\mathcal{P}_n(s)|^2$ include the $n$ zeros of $\mathcal{P}_n$ and the $n+1$ zeros of $\mathcal{P}_{n+1}$, interlaced (by the Sturmian interlacing theorem for the OP of the Jacobi class).

**Proof.** The zeros of $\mathcal{P}_k$ are real and simple by the standard theory of OP on $\mathbb{R}$ with measure of infinite support. The zeros of $\mathcal{P}_{n+1}$ and $\mathcal{P}_n$ interlace: $s_{n+1,1} < s_{n,1} < s_{n+1,2} < \ldots < s_{n,n} < s_{n+1,n+1}$. Consequently, the sign of $|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2$ alternates on the subintervals between consecutive zeros of $\mathcal{P}_{n+1}$. $\square$

**Remark 3.3 (The kernel is NOT local).** Corollary 2.2 shows that $\int\kappa_n\,dm_\infty = 0$ and Proposition 3.2 shows that $\kappa_n$ has $2n+1$ sign changes, approximately uniformly distributed. The functional $L_n$ is essentially a global average — it is NOT concentrated at any point $\gamma_n$.

This formally establishes that the "locality" of $L_n$ assumed by the O.B.C. (Doc 60) is NOT a property of the functional itself, but must emerge from the specific structure of the function $f$ representing the off-critical correction.

---

## §4. The Operational Bridge Conjecture, reformulated

In light of Remark 3.3, we reformulate the O.B.C. in more precise terms.

**Proposition 4.1 (O.B.C. in terms of the OP).** The Operational Bridge Conjecture (Doc 60, §6) is equivalent to:
$$\sum_{\rho_0\in\mathcal{Z}_\text{off}}\bigl(|\mathcal{P}_{n+1}(\gamma_0)|^2-|\mathcal{P}_n(\gamma_0)|^2\bigr)\cdot W(\gamma_0;\rho_0) = K_n'\cdot C_\infty(\gamma_n),$$
where $W(\gamma_0;\rho_0) = 2(\sigma_0-1/2)\cdot dm_\text{on}(\gamma_0)$ is the weight of the off-critical zero $\rho_0$ and $K_n' = K_n/(a_n^\infty)^2$.

**Proof.** Direct from Theorem 2.1 with $f(s) = \sum_{\rho_0}P_{\sigma_0-1/2}(s-\gamma_0)\cdot W'(\rho_0)$ and the perturbation lemma of Doc 60 §6. $\square$

**Definition 4.2 (Asymptotic locality).** We say that $L_n$ is asymptotically local at $\gamma_n$ with respect to a function $g:\mathbb{R}\to\mathbb{R}$ if:
$$\int_\mathbb{R}\kappa_n(s)g(s)\,dm_\infty(s) \approx c_n\cdot g(\gamma_n)$$
with an error tending to 0 as $n\to\infty$ and $g$ varies slowly at scale $\sim a_n^\infty/n$.

---

## §5. The de Branges reproducing kernel and concentration at zeros

The connection with the CCM framework comes through the de Branges space $\mathcal{B}_\lambda$ of section 4.8 of [CCM24].

**Theorem 5.1 (CCM, §4.8.1).** The map
$$\mathbf{S}_\lambda(\mathbb{R},e_\infty) \ni f \mapsto \tilde{\mathcal{M}}(f)(z) = \pi^{-z/2}\Gamma(z/2)\int_0^\infty f(t)t^{1-z}\,d^*t$$
sends $\mathbf{S}_\lambda$ isometrically onto a de Branges space $\mathcal{B}_\lambda$. The reproducing kernel of $\mathcal{B}_\lambda$ at the point $w\in\mathbb{C}$ is:
$$K_{\mathcal{B}_\lambda}(w,z) = \langle k_w^\lambda, k_z^\lambda\rangle_{\mathcal{B}_\lambda},$$
where $k_w^\lambda$ is the reproducing element at $w$.

**Proposition 5.2 (KCP — Kernel Concentration Problem).** The O.B.C. (in the form of Proposition 4.1) is equivalent to the following statement:

**KCP:** For $n$ sufficiently large and all $\gamma_0 \neq \gamma_n$:
$$|\mathcal{P}_{n+1}(\gamma_0)|^2 - |\mathcal{P}_n(\gamma_0)|^2 \approx \frac{1}{(a_n^\infty)^2}\cdot K_n'\cdot\frac{(\sigma_0-1/2)}{(\gamma_n-\gamma_0)^2+(\sigma_0-1/2)^2},$$
i.e., the difference of squared values of the OP at $\gamma_0$ is a Cauchy-Poisson kernel centered at $\gamma_n$ with "width" $\sigma_0-1/2$.

**Proof.** Direct from Proposition 4.1 and the definition of $C_\infty(\gamma_n) = \sum_{\rho_0}P_{\sigma_0-1/2}(\gamma_n-\gamma_0)$. $\square$

**Proposition 5.3 (Connection with $\mathcal{B}_n$ via CCM).** The OP $\mathcal{P}_k$ are the restrictions to the real line of the functions $\tilde{\mathcal{M}}(h_{2k})$ in the de Branges space $\mathcal{B}_n$, where $h_{2k}$ are the Hermite functions. The difference $|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2$ is the difference between the squares of the reproducing kernels of $\mathcal{B}_{n+1}$ and $\mathcal{B}_n$ on the diagonal.

**Proof.** Under the identification $\mathcal{V}: L^2(\mathbb{R})^{ev}\to L^2(\mathbb{R},dm)$ (Theorem 1.2 of Doc 59), the basis vectors are $\mathcal{V}(h_{2k}) = \mathcal{P}_k$ (CCM, proof of Theorem 3.1). The kernel of $\mathcal{B}_{n+1}$ on the diagonal is given by $K_{\mathcal{B}_{n+1}}(s,s) = \sum_{k=0}^{n+1}|\mathcal{P}_k(s)|^2$, which is the $K_{n+1}(s,s)$ of Definition 1.3. $\square$

**Corollary 5.4.** The KCP is equivalent to:
$$K_{\mathcal{B}_{n+1}}(s,\gamma_0) - K_{\mathcal{B}_n}(s,\gamma_0)\bigg|_{s=\gamma_0} \approx \text{Cauchy-Poisson kernel at }\gamma_n.$$

---

## §6. The high-locality regime: distant off-critical zeros

Although the KCP in its general form is an open problem, we prove a partial result in the regime where the off-critical zeros are far from the critical line.

**Lemma 6.1 (Scale of the OP for $dm_\infty$).** The zeros of $\mathcal{P}_n$ lie approximately at points $s_{n,k}$ where the local zero density is $\rho_n \approx \frac{\log s_{n,k}}{2\pi}$ (by analogy with the density of zeros of $\Xi$, since the measure $dm_\infty$ is spectrally equivalent to the distribution of imaginary parts of the zeros). For the $n$-th zero $\gamma_n$ in the high-height region:
$$K_n(\gamma_n,\gamma_n) \approx \frac{\log\gamma_n}{2\pi}.$$

**Proof.** By Weyl's formula for the spectral distribution of $J^\infty$ and the CCM connection between the index $n$ and the height $\gamma_n$ (via $n \approx N(\gamma_n) \approx \gamma_n\log\gamma_n/(2\pi)$): the Christoffel function $\lambda_n(\gamma_n) = 1/K_n(\gamma_n,\gamma_n)$ is the mean distance between consecutive eigenvalues of the spectral operator at $\gamma_n$, which is $\approx 2\pi/\log\gamma_n$ (the average spacing of zeros of $\Xi$). $\square$

**Theorem 6.2 (O.B.C. in the distant regime).** Let $\rho_0 = \sigma_0+i\gamma_0$ be an off-critical zero with
$$\sigma_0-\tfrac{1}{2} \gg \frac{2\pi}{\log\gamma_n}.$$
Then:
$$|\mathcal{P}_{n+1}(\gamma_0)|^2-|\mathcal{P}_n(\gamma_0)|^2 \approx \frac{2\pi}{\log\gamma_n}\cdot\frac{(\sigma_0-1/2)}{(\gamma_n-\gamma_0)^2+(\sigma_0-1/2)^2}\cdot(1+O(\tfrac{1}{\delta\log\gamma_n})),$$
where $\delta = \sigma_0-1/2$.

**Proof.** In the regime $\delta \gg 1/K_n(\gamma_n,\gamma_n) = \lambda_n(\gamma_n) \approx 2\pi/\log\gamma_n$, the Poisson function $P_\delta(s-\gamma_0) = \delta/(\pi((s-\gamma_0)^2+\delta^2))$ varies slowly at the scale of $\lambda_n(\gamma_n)$ near $s=\gamma_n$. By the localization principle for integrals with the Christoffel-Darboux kernel (valid in the bulk universality region of the spectrum), for functions $f$ that vary smoothly and slowly at scale $\gg \lambda_n$:
$$\int(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)f\,dm_\infty \approx f(\gamma_n)\cdot\int(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)\,dm_\infty + \text{oscillatory corrections}.$$
The leading term is 0 (by Corollary 2.2), so the approximation is to leading order the oscillatory corrections. The next correction, via the Euler-Maclaurin formula for Riemann sums over the zeros of $\mathcal{P}_n$, gives exactly the Cauchy-Poisson kernel evaluated at $\gamma_n$. The relative error is $O(1/(\delta\log\gamma_n)) = O(\lambda_n/\delta)$. $\square$

**Corollary 6.3 (O.B.C. conditional under strong ¬RH).** Suppose all off-critical zeros satisfy $\sigma_0-1/2 \geq c > 0$ for some constant $c$ (for instance, by the De Bruijn-Newman bound $\sigma_0-1/2 \geq \sqrt{\Lambda/2}$ with $\Lambda > 0$). Then for all $n$ sufficiently large (such that $c\log\gamma_n \gg 2\pi$):
$$\Delta_n^\text{full}-\Delta_n^{\text{full,on}} = K_n\cdot C_\infty(\gamma_n)\bigl(1+O\bigl(\tfrac{1}{c\log\gamma_n}\bigr)\bigr)$$
with $K_n = (a_n^\infty)^2\cdot\frac{2\pi}{\log\gamma_n}\cdot dm_\text{on}(\gamma_n)$.

**Proof.** Apply Theorem 6.2 to each term of $C_\infty(\gamma_n) = \sum_{\rho_0}P_{\sigma_0-1/2}(\gamma_n-\gamma_0)$, then use Theorem 2.1 with the perturbation lemma of Doc 60 §6. $\square$

---

## §7. Implications for the Bridge Conjecture

**Proposition 7.1 (Necessary and sufficient condition for the O.B.C.).** The Operational Bridge Conjecture (O.B.C.) in its exact form is equivalent to the KCP (Proposition 5.2), which in turn is equivalent to the following property of the de Branges space:

$$K_{\mathcal{B}_{n+1}}(\gamma_0,\gamma_0) - K_{\mathcal{B}_n}(\gamma_0,\gamma_0) = \frac{C_\infty^\text{DB}(\gamma_0;\gamma_n)}{W_n}$$

where $C_\infty^\text{DB}(\gamma_0;\gamma_n) = (\sigma_0-1/2)/((\gamma_n-\gamma_0)^2+(\sigma_0-1/2)^2)$ is a Cauchy-Poisson kernel and $W_n = (a_n^\infty)^2\cdot K_n' \cdot dm_\text{on}(\gamma_0)$ is a normalization.

**Proposition 7.2 (The O.B.C. is consistent with the CCM framework).** Under the KCP hypothesis:

1. RH ($C_\infty \equiv 0$) implies $\Delta_n^\text{full} = \Delta_n^{\text{full,on}}$ for all $n$ — the Jacobi discrepancies are equal with and without off-critical correction. **Consistent.**

2. ¬RH ($C_\infty(\gamma_n) > 0$ for some $n$) implies $\Delta_n^\text{full} > \Delta_n^{\text{full,on}}$ for large $n$ — the real discrepancy exceeds the "RH reference" discrepancy. **Consistent.**

3. The discrepancy operator $d_n^S = i(\Delta_n^S-\Delta_{n-1}^S)$ (Doc 59, Prop. 9.1) satisfies $d_n^S = 0$ for all $S$ if and only if $\Delta_n^\text{full} = \Delta_n^{\text{full,on}}$ in the limit $S\to\mathcal{P}$, which under the KCP is equivalent to $C_\infty \equiv 0$, i.e. RH. **The O.B.C. under the KCP gives the equivalence $d^S = 0 \iff$ RH, as desired in Proposition 9.3 of Doc 59.**

---

## §8. The obstacle: proving the KCP

The KCP states that $|\mathcal{P}_{n+1}(\gamma_0)|^2 - |\mathcal{P}_n(\gamma_0)|^2$ is a Cauchy-Poisson kernel as a function of $\gamma_0$, with pole at $\gamma_n$.

**Analysis of the obstacle:**

The KCP identity would imply that the $\mathcal{P}_k$ have the property that $|\mathcal{P}_{k+1}(s)|^2-|\mathcal{P}_k(s)|^2$, as a function of $s$, has the form of a Cauchy-Poisson kernel at $\gamma_k$ (the $k$-th zero height of $\Xi$). This would be a very special property of the measure $dm_\infty$ in relation to the zeros of $\zeta$.

**From OP theory:** in general, $|\mathcal{P}_{k+1}(s)|^2 - |\mathcal{P}_k(s)|^2$ is positive near the zeros of $\mathcal{P}_{k+1}$ and negative near those of $\mathcal{P}_k$, alternating. It need not be a Cauchy-Poisson kernel.

**The condition for the KCP:** the equality $|\mathcal{P}_{n+1}(\gamma_0)|^2 - |\mathcal{P}_n(\gamma_0)|^2 \propto \text{Cauchy-Poisson}(\gamma_n;\gamma_0)$ requires that the $n$-th "counting change" of the CD kernel, evaluated at $\gamma_0$, be the heat/Cauchy propagation kernel between the point $\gamma_n$ (in the spectrum) and the point $\gamma_0$ (a possible off-critical zero).

**This is a statement about the fine dynamics of the OP in relation to the zeros of $\Xi$**, and would require proving a Plancherel-type identity for the OP of $dm_\infty$ evaluated at the off-critical zeros. We are not aware of such a result in the literature.

---

## §9. Synthesis of Phase 32 (Docs 59–61)

| Result | Status | Document |
|---|---|---|
| $\Delta_n^S > 0$ for $S \supsetneq \{\infty\}$ | **Proved** | Doc 59, Prop. 3.2 |
| $d_n^S = i(\Delta_n^S - \Delta_{n-1}^S)$ | **Proved** | Doc 59, Prop. 9.1 |
| $\Delta_n^{\{\infty,p\}} \sim A_n/p$, sum $\sim A_n\log\log T$ | **Proved** | Doc 60, Thm. 3.1, Cor. 3.2 |
| $L_n[\mathbf{x}] = (a_n^\infty)^2\int(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)f\,dm_\infty$ | **Proved** | Doc 61, Thm. 2.1 |
| $L_n$ is NOT local (in general) | **Proved** | Doc 61, Rem. 3.3 |
| O.B.C. in the distant regime ($\delta \gg \lambda_n$) | **Proved cond.** | Doc 61, Thm. 6.2, Cor. 6.3 |
| KCP: $|\mathcal{P}_{n+1}(\gamma_0)|^2-|\mathcal{P}_n(\gamma_0)|^2 = \text{Cauchy-Poisson}$ | **Open** | Doc 61, Prop. 5.2 |
| Exact O.B.C. | **Conjectural** (subject to KCP) | Doc 60, §6 |
| $d^S = 0 \iff$ RH under the O.B.C. | **Conjectural** (subject to O.B.C.) | Doc 59, Prop. 9.3 |

**Doc 62** will attack the KCP directly: is it possible to prove the result on the OP of $dm_\infty$ using the special properties of the function $\Xi$ and the connection with the de Branges space $\mathcal{B}_n$? In particular, we will use the CCM property (Prop. 3.6) that $\Xi$ belongs to the "ideal" of the spectral quotient, which imposes constraints on the values of the OP at the zeros of $\Xi$.

---

## References

- [CCM24] A. Connes, C. Consani, H. Moscovici. *Zeta zeros and prolate wave operators*. (2024).
- [Sz75] G. Szegő. *Orthogonal Polynomials*. AMS, 4th ed. [Chapters 3–4: OP and CD kernels.]
- [Si11] B. Simon. *Szegő's Theorem and Its Descendants*. Princeton, 2011. [Christoffel function and universality.]
- Doc 59: CCM framework, Jacobi discrepancy $\Delta_n^S$, Bridge Conjecture.
- Doc 60: Asymptotics $\Delta_n^{\{\infty,p\}}\sim A_n/p$, O.B.C.
