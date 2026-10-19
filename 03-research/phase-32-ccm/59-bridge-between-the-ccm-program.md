# Document 59 — Bridge between the CCM program and the deficit $C_\infty$

**Phase 32: Semilocal prolate operators and Sonin spaces**


---

## Abstract

We import the Connes–Consani–Moscovici (2024) framework [CCM24] as a foundation and integrate it with the results of the program developed in Docs 42–58. The goal of this phase is twofold: (i) identify the exact place where the deficit $C_\infty(\gamma_n)$ (Doc 42) appears within the formalism of semilocal cyclic pairs, and (ii) build the bridge between the semilocal Jacobi discrepancy $\Delta_n^S$ and our arithmetic formula (Doc 54). The main result of this document is that the discrepancy $\Delta_n^S$ is explicitly computable for $S = \{\infty, p\}$ and that its asymptotic behavior as $S$ grows is governed by the same Euler factors that appear in the arithmetic deficit. We formulate the **Bridge Conjecture** (B.C.) as the central objective of Phase 32.

---

## §1. Foundations imported from CCM

We accept without proof the following results from [CCM24].

**Notation.** For a finite set of places $S \ni \infty$, let $\mathbb{A}_S = \prod_{v \in S} \mathbb{Q}_v$, $\Gamma = GL_1(\mathbb{Q}_S)$, and the semilocal idèle class space $X_S = \mathbb{A}_S/\Gamma$.

**Theorem 1.1 (CCM, Thm. 3.1).** Let $\mathbb{S} = -i(H + 1/2)$ be the scaling operator on $L^2(\mathbb{R})^{ev}$ and $\xi_\infty = 2^{1/4}e^{-\pi x^2}$. The cyclic pair $(\mathbb{S}, \xi_\infty)$ is even and the unitary transformation
$$\mathcal{V} := \mathcal{M} \circ \mathcal{U} : L^2(\mathbb{R})^{ev} \to L^2(\mathbb{R}, dm)$$
gives the canonical form of the cyclic pair, where
$$dm(s) = (2\pi)^{-2}\left|\Gamma\!\left(\tfrac{1}{4} + \tfrac{is}{2}\right)\right|^2 ds.$$
Under $\mathcal{V}$, the operator $\mathbb{S}$ becomes multiplication by $s$ and the prolate operator takes the form
$$(\mathcal{M} \circ \mathcal{U}) \circ \mathbf{W}_\lambda \circ (\mathcal{M} \circ \mathcal{U})^* = -s^2 + 2\pi\lambda^2(4N+1) - \tfrac{1}{4}.$$

**Theorem 1.2 (CCM, Prop. 3.6).** The zeros of $\zeta$ are the spectrum of the operator $M_s$ (multiplication by $s$) on the quotient space $\mathcal{H}_{\leq 1}/\overline{\text{span}\{R_\ell^\pm(s)\,\Xi(s)\}}$, where $R_\ell^\pm$ are explicit polynomials and $\mathcal{H}_{\leq 1}$ is the Hadamard topological ring of entire functions of order $\leq 1$.

**Theorem 1.3 (CCM, Thm. 5.2).** The coefficients $a_n^\infty$ of the Jacobi matrix of the cyclic pair $(\mathbb{S}, \xi_\infty)$ are
$$a_n^\infty = \frac{1}{2}\sqrt{(2n+1)(2n+2)},$$
and are uniquely determined by the condition that $\sigma: \mathfrak{sl}(2,\mathbb{R}) \to \text{End}(\mathcal{H})$ be a representation of the Lie algebra. The discrepancy coefficients satisfy $d_n^\infty = 0$ for all $n \geq 0$.

**Theorem 1.4 (CCM, Thm. 4.6).** For every finite $S \ni \infty$ and $\lambda > 0$, the map
$$\theta_S : \mathbf{S}_\lambda(\mathbb{R}, e_\infty) \to \mathbf{S}_\lambda(X_S, \alpha)$$
is a Hilbert isomorphism, where $\mathbf{S}_\lambda(\mathbb{K}, \alpha) = \{f \in L^2(\mathbb{K}) : f(x) = 0 \text{ and } \mathbb{F}_\alpha f(x) = 0 \ \forall\, |x| < \lambda\}$ is the Sonin space.

---

## §2. Semilocal cyclic pair and spectral measure

For $S = \{\infty, p_1, \ldots, p_k\}$ finite with $\infty \in S$, CCM [Prop. 4.2] builds the semilocal cyclic pair $(\mathbb{S}, \xi_S)$ on $L^2(X_S)^{K_S}$. The canonical form of this pair is given by the spectral measure

$$dm_S(s) = \left|\prod_{v \in S} L_v\!\left(\tfrac{1}{2} - is\right)\right|^2 ds,$$

where the local Euler factors are
$$L_\infty(z) = \pi^{-z/2}\Gamma(z/2), \quad L_p(z) = (1-p^{-z})^{-1}.$$

**Proposition 2.1.** The measure $dm_S$ decomposes as
$$dm_S(s) = dm_\infty(s) \cdot \prod_{p \in S \setminus \{\infty\}} |L_p(\tfrac{1}{2}-is)|^2,$$
where each additional factor satisfies $|L_p(\tfrac{1}{2}-is)|^2 = (1 - 2p^{-1/2}\cos(s\log p) + p^{-1})^{-1}$.

**Proof.** The factorization is immediate from the definition of $dm_S$ and the multiplicativity of the Euler factors. For the computation of the squared modulus:
$$|L_p(\tfrac{1}{2}-is)|^2 = |(1-p^{-1/2+is})^{-1}|^2 = |1-p^{-1/2}e^{is\log p}|^{-2}.$$
Expanding: $|1-p^{-1/2}e^{is\log p}|^2 = 1 - p^{-1/2}(e^{is\log p}+e^{-is\log p}) + p^{-1} = 1-2p^{-1/2}\cos(s\log p)+p^{-1}$. $\square$

**Corollary 2.2.** The semilocal correction relative to the archimedean case is
$$\frac{dm_S(s)}{dm_\infty(s)} = \prod_{p \in S\setminus\{\infty\}} \frac{1}{1 - 2p^{-1/2}\cos(s\log p) + p^{-1}}.$$
In particular, $dm_S(s)/dm_\infty(s) > 1$ for every $s \in \mathbb{R}$ and every $S \supsetneq \{\infty\}$.

---

## §3. Semilocal Jacobi discrepancy

The coefficients $a_n^S$ of the Jacobi matrix of the semilocal cyclic pair are determined by the even moments of $dm_S$:
$$c_{2k}^S = \int_{\mathbb{R}} s^{2k}\, dm_S(s).$$

**Definition 3.1 (Semilocal Jacobi discrepancy).** For finite $S \ni \infty$, the discrepancy of the $n$-th Jacobi coefficient is
$$\Delta_n^S := (a_n^S)^2 - (a_n^\infty)^2 = (a_n^S)^2 - \frac{(2n+1)(2n+2)}{4}.$$

By Theorem 1.3, $\Delta_n^{\{\infty\}} = 0$ for every $n$. The discrepancy $\Delta_n^S$ measures the deviation of the semilocal cyclic pair from the purely archimedean case.

**Proposition 3.2 (Positivity of the discrepancy).** For every $S \supsetneq \{\infty\}$ and every $n \geq 0$, one has $\Delta_n^S > 0$.

**Proof.** The coefficients $a_n^S$ are determined by Hankel determinants: $a_n^S = (D_{n-1}^S/D_n^S)^{1/2} \cdot \text{const}$, where $D_n^S = \det(c_{i+j}^S)_{0 \leq i,j \leq n}$. By Corollary 2.2, $c_{2k}^S > c_{2k}^\infty$ for every $k \geq 0$ (since $dm_S/dm_\infty > 1$). Stochastic dominance $dm_S \succ dm_\infty$ implies $a_n^S > a_n^\infty$ for every $n$ by monotonicity of the Jacobi coefficients under domination of measures [Sz75, Ch. 2]. Hence $\Delta_n^S = (a_n^S)^2 - (a_n^\infty)^2 > 0$. $\square$

---

## §4. Explicit computation for $S = \{\infty, p\}$

We fix $S = \{\infty, p\}$ and compute the correction to the moments.

**Lemma 4.1.** For $S = \{\infty, p\}$:
$$c_{2k}^S = c_{2k}^\infty + \delta c_{2k}^p,$$
where the correction is
$$\delta c_{2k}^p = \sum_{\substack{m,n \geq 0 \\ (m,n) \neq (0,0)}} p^{-(m+n)/2} \int_{\mathbb{R}} s^{2k} e^{i(m-n)s\log p}\, dm_\infty(s).$$

**Proof.** We expand $|L_p(1/2-is)|^2 = \sum_{m,n \geq 0} p^{-(m+n)/2}e^{i(m-n)s\log p}$ (convergent Neumann series since $p^{-1/2} < 1$). Multiplying by $s^{2k}$ and integrating against $dm_\infty$, the term $(m,n)=(0,0)$ contributes $c_{2k}^\infty$. $\square$

**Proposition 4.2 (Characteristic function of $dm_\infty$).** The characteristic function of the measure $dm_\infty$ is
$$\phi_\infty(t) = \int_{\mathbb{R}} e^{its}\, dm_\infty(s) = \text{sech}^{1/2}(t) = \left(\frac{2}{e^t + e^{-t}}\right)^{1/2},$$
and the corrections satisfy
$$\int_{\mathbb{R}} s^{2k} e^{i\alpha s}\, dm_\infty(s) = (-1)^k \frac{d^{2k}}{dt^{2k}}\left[\text{sech}^{1/2}(t)\right]_{t=\alpha}.$$

**Proof.** The first equality is Theorem 5.2(iii)+(iv) of CCM. The second is the standard relation between the characteristic function and the moments: $\int s^{2k}e^{i\alpha s}d\mu = (-1)^k\hat{\mu}^{(2k)}(\alpha)$ where $\hat\mu(\alpha) = \int e^{i\alpha s}d\mu(s) = \phi_\infty(\alpha)$. $\square$

**Corollary 4.3 (Asymptotic expansion for $p \to \infty$).** 
$$\delta c_{2k}^p = 2p^{-1/2}(-1)^k\left[\text{sech}^{1/2}\right]^{(2k)}(\log p) + O(p^{-1}).$$
In particular, the dominant term is controlled by the derivatives of $\text{sech}^{1/2}$ evaluated at $\log p$.

**Proof.** The dominant term in the expansion of Lemma 4.1 corresponds to $(m,n) = (1,0)$ and $(m,n) = (0,1)$, which contribute $p^{-1/2}\int s^{2k}(e^{is\log p}+e^{-is\log p})dm_\infty = 2p^{-1/2}\text{Re}\int s^{2k}e^{is\log p}dm_\infty$. Using Proposition 4.2, this is $2p^{-1/2}(-1)^k[\text{sech}^{1/2}]^{(2k)}(\log p)$. The following terms are $O(p^{-1})$ by convergence of the series. $\square$

---

## §5. The Jacobi discrepancy and the Euler factors

Proposition 4.2 and Corollary 4.3 express $\delta c_{2k}^p$ in terms of $\text{sech}^{1/2}$. We now connect this with the Euler factors $L_p(1/2 + is)$.

**Lemma 5.1 (Integral representation of the correction).** For $S = \{\infty, p\}$:
$$\delta c_{2k}^p = \int_{\mathbb{R}} s^{2k}\left(|L_p(\tfrac{1}{2}-is)|^2 - 1\right)dm_\infty(s),$$
and the function $s \mapsto |L_p(1/2-is)|^2 - 1$ can be written as
$$|L_p(\tfrac{1}{2}-is)|^2 - 1 = \frac{2p^{-1/2}\cos(s\log p) - p^{-1}}{1 - 2p^{-1/2}\cos(s\log p) + p^{-1}}.$$

**Proof.** Immediate from Proposition 2.1. $\square$

**Proposition 5.2 (Peak structure of the discrepancy).** The function $s \mapsto |L_p(1/2-is)|^2 - 1$ has Lorentzian peaks at $s_k = 2\pi k / \log p$ for $k \in \mathbb{Z}$, with height $\approx p^{1/2}/(p^{1/2}-1)^2 - 1$ and width $\sim 2(p^{1/2}-1)/(p^{1/2}\log p)$.

**Proof.** At $s = s_k$: $\cos(s_k \log p) = 1$, so $|L_p(1/2-is_k)|^2 = (1-p^{-1/2})^{-2}$, giving the peak value. The width follows from the expansion of $\cos(s\log p) \approx 1 - (s-s_k)^2(\log p)^2/2$ near $s_k$. $\square$

**Remark 5.3.** The peaks of $|L_p(1/2-is)|^2$ are spaced every $2\pi/\log p$ and grow like $p/(p-1)^2$ as $p \to \infty$. The density of zeros of $\Xi$ in the same region is $\sim \log(\gamma/(2\pi))/(2\pi)$. When the spacing $2\pi/\log p$ matches the average zero spacing $2\pi/\log\gamma$, i.e. $p \approx \gamma$, the factor $L_p$ "resonates" with the zero $\gamma$. This resonance is the structural connection with the deficit $C_\infty(\gamma_n)$ (see the Bridge Conjecture, §7).

---

## §6. Connection with the deficit $C_\infty$ of the earlier program

We recall the key results of Docs 42–58:

- **Doc 42:** $C_\infty(\gamma_n) = \sum_{\rho_0 \in \mathcal{Z}_{\text{off}}} \frac{2(\sigma_0-1/2)}{(\gamma_n-\gamma_0)^2+(\sigma_0-1/2)^2} \geq 0$.
- **Doc 43:** $C_\infty(\gamma_{n_0}) = 0$ for some $n_0$ $\Leftrightarrow$ RH.
- **Doc 54:** $C_\infty(\gamma_n) = w(\gamma_n) - 2\text{Re}[A_n]$ where $A_n$ collects the arithmetic contribution of the zeros off the critical line.
- **Doc 58:** $c_* = \inf_n C_\infty(\gamma_n) = 0$ unconditionally.

**Proposition 6.1 (Connection via the Hardy–Titchmarsh dual transform).** Let $\upsilon_S : L^2(X_S)^{K_S} \to L^2(\mathbb{R}, ds/|E_S(s)|^2)$ be the Hardy–Titchmarsh dual transform of CCM [§4.4], where $E_S(s) = \prod_{p \in S\setminus\{\infty\}} L_p(1/2+is)$. Then for every $f \in L^2(\mathbb{R})^{ev}$:
$$\langle \upsilon_S \theta_S(f) \mid \upsilon_\infty f \rangle_{\mathbb{R}} = \langle f \mid f \rangle_{L^2(\mathbb{R})}.$$

**Proof.** This is exactly Proposition 4.7(iii) of CCM applied with the notation of section 4.4. $\square$

**Proposition 6.2 (Spectral evaluation at the zeros).** For each zero $\rho_n = 1/2+i\gamma_n$ of $\zeta$, let $F_n \in \mathcal{H}_{\leq 1}$ be the spectral evaluation function given by Prop. 3.6 of CCM. Then, under $\mathcal{V}_S$:
$$\mathcal{V}_S(F_n)(s) = R_n^S(s) \cdot \Xi(s),$$
where $R_n^S \in \mathbb{C}[s]$ is a polynomial depending on $S$ and on $\rho_n$.

**Proof.** This is Proposition 3.6 of CCM with the semilocal extension of Proposition 4.2 of CCM. The polynomial $R_n^S$ is obtained by projecting onto the eigenvector of the quotient corresponding to $\gamma_n$. $\square$

**Lemma 6.3 (Spectral weight of the $n$-th zero).** The spectral weight of $\gamma_n$ in the measure $dm_S$ is
$$\omega_n^S := \lim_{\epsilon \to 0} \frac{1}{2\epsilon} \int_{|\gamma_n - s| < \epsilon} dm_S(s) = |L_\infty(\tfrac{1}{2}-i\gamma_n)|^2 \prod_{p \in S\setminus\{\infty\}} |L_p(\tfrac{1}{2}-i\gamma_n)|^2.$$

**Proof.** The measure $dm_S$ is absolutely continuous with respect to Lebesgue measure, so $\omega_n^S = dm_S(\gamma_n)/ds$. By Proposition 2.1, the density is exactly the indicated product. $\square$

---

## §7. The Bridge Conjecture

The structure of §3–6 points to a deep connection between $\Delta_n^S$ and $C_\infty(\gamma_n)$. We formulate the central conjecture of Phase 32.

**Bridge Conjecture (B.C.).** For each $n \geq 1$ and each prime $p$, there exists a constant $K_n > 0$ depending only on $\gamma_n$ such that
$$C_\infty(\gamma_n) = K_n \cdot \lim_{S \to \mathcal{P}} \frac{1}{\log|S|} \sum_{p \in S \setminus \{\infty\}} \Delta_n^{\{\infty,p\}} \cdot (\log p)^{-1},$$
where the limit is taken over sets $S$ that grow like the primes less than $T$ as $T \to \infty$, and $\mathcal{P}$ denotes the set of all primes.

**Heuristic justification.** The deficit $C_\infty(\gamma_n) = \sum_{\rho_0} \Delta(\gamma_n;\rho_0)$ is a sum over zeros off the critical line. Each zero $\rho_0 = \sigma_0 + i\gamma_0$ contributes through the Cauchy-Poisson kernel. On the other hand, the discrepancy $\Delta_n^{\{\infty,p\}}$ measures how much the factor $L_p$ "shifts" the Jacobi coefficient of the $n$-th basis vector. By Remark 5.3, when $p \approx e^{2\pi/|\gamma_n-\gamma_0|}$ (resonance between the prime $p$ and the gap between a critical and a non-critical zero), the discrepancy $\Delta_n^{\{\infty,p\}}$ captures exactly the same information as $\Delta(\gamma_n;\rho_0)$.

**Weak version of the B.C. (checkable).** A weaker version, which does admit attack with current methods, is:

$$C_\infty(\gamma_n) = 0 \iff \Delta_n^S = 0 \text{ for every } S \supsetneq \{\infty\}.$$

Note that by Proposition 3.2, $\Delta_n^S > 0$ for every $S \supsetneq \{\infty\}$. The weak version of the B.C. would assert that the implication $\Leftarrow$ is vacuously true and that $\Rightarrow$ implies RH. This translates to:

$$C_\infty(\gamma_n) = 0 \iff \text{RH} \iff a_n^S = a_n^\infty \text{ for every } S.$$

The first equivalence is the Rigidity Theorem (Doc 43). The second is the claim that the semilocal cyclic pair collapses to the archimedean one exactly under RH.

---

## §8. A proved result: monotonicity under enlargement of $S$

**Proposition 8.1 (Monotonicity of the discrepancy).** Let $S \subset S'$ with $\infty \in S$. Then $\Delta_n^{S'} \geq \Delta_n^S$ for every $n \geq 0$.

**Proof.** $dm_{S'} = dm_S \cdot \prod_{p \in S' \setminus S} |L_p(1/2-is)|^2$. By Proposition 2.1, each additional factor is $\geq 1$, so $dm_{S'} \geq dm_S$ pointwise. By stochastic dominance, $c_{2k}^{S'} \geq c_{2k}^S$ for every $k$, and by the same monotonicity as in Prop. 3.2, $(a_n^{S'})^2 \geq (a_n^S)^2$, i.e. $\Delta_n^{S'} \geq \Delta_n^S$. $\square$

**Corollary 8.2.** The net $\{\Delta_n^S\}_{S \ni \infty, \text{finite}}$ ordered by inclusion is non-decreasing. In particular, the limit
$$\Delta_n^* := \sup_S \Delta_n^S = \lim_{S \to \mathcal{P}} \Delta_n^S$$
exists in $[0, +\infty]$.

**Proposition 8.3 (Relation with the moments of the function $\Xi$).** Let $d\mu_\Xi(s) = |\Xi(1/2+is)|^2 ds$. Then formally
$$\lim_{S \to \mathcal{P}} dm_S(s) = |L_\infty(\tfrac{1}{2}-is)|^2 \cdot |\zeta(\tfrac{1}{2}+is)|^2\,ds = d\mu_\Xi(s) \cdot |\pi^{-1/4}\Gamma(1/4)|^{-2}.$$

**Proof.** By the Euler product: $\prod_p L_p(1/2+is) = \zeta(1/2+is)$ when the product converges (conditionally on the critical line). The limit of $dm_S$ as $S$ includes all primes is $|L_\infty|^2 \cdot |\zeta(1/2+is)|^2\,ds$, which is proportional to $d\mu_\Xi$ up to normalization factors. $\square$

**Remark 8.4.** The limiting measure $d\mu_\Xi$ has zeros exactly at $s = \pm\gamma_n$ (the imaginary values of the zeros of $\zeta$ on the critical line, i.e. the zeros of $\Xi$ as a function of real $s$). Under RH, these are all the zeros. The structure of the Jacobi coefficients $a_n^*$ for the measure $d\mu_\Xi$ encodes all the information about the zeros of $\zeta$ on the critical line, and the B.C. asserts that $\Delta_n^* - \Delta_n^\infty$ captures the information about the zeros off the critical line.

---

## §9. Relation with the prolate operator and the CCM discrepancy coefficients

In section 5 of CCM, the discrepancy coefficients of the prolate operator are (eq. 5.10):
$$\frac{1}{i}d_n = -2n + a_n^2 - a_{n-1}^2.$$

For the archimedean case: $d_n^\infty = 0$ (imported Theorem 1.3). For the semilocal case:

**Proposition 9.1.** For $S = \{\infty, p\}$ with $p$ prime, the discrepancy coefficients of the prolate operator satisfy
$$d_n^S = i\left(\Delta_n^S - \Delta_{n-1}^S\right) + d_n^\infty = i\left(\Delta_n^S - \Delta_{n-1}^S\right).$$

**Proof.** Applying the definition to $a_n^S$:
$$\frac{1}{i}d_n^S = -2n + (a_n^S)^2 - (a_{n-1}^S)^2 = \underbrace{-2n + (a_n^\infty)^2 - (a_{n-1}^\infty)^2}_{=0} + \Delta_n^S - \Delta_{n-1}^S.$$
$\square$

**Corollary 9.2.** The discrepancy coefficients $d_n^S$ of the semilocal prolate operator are deterministic: they are completely controlled by the increments $\Delta_n^S - \Delta_{n-1}^S$ of the Jacobi discrepancy.

**Proposition 9.3 (Condition $d^S = 0$ and RH).** If the Bridge Conjecture is true, then
$$d_n^S = 0 \text{ for every } n \geq 0 \text{ and every } S \iff C_\infty(\gamma_n) = 0 \text{ for some } n \iff \text{RH}.$$

**Proof.** ($\Rightarrow$): $d_n^S = 0$ for every $n$ implies $\Delta_n^S = \Delta_{n-1}^S$ for every $n$. By Proposition 3.2, $\Delta_n^S \geq 0$. By Corollary 8.2, $\Delta_n^S$ is constant in $n$. Using the B.C., this implies $C_\infty(\gamma_n) = 0$ for some $n$. By the Rigidity Theorem (Doc 43), RH. ($\Leftarrow$): RH implies $C_\infty \equiv 0$ (Doc 42), and by the B.C., $\Delta_n^S = \Delta_n^\infty = 0$ for every $S$ and every $n$, whence $d_n^S = 0$. $\square$

---

## §10. Frank barriers

**Barrier B1 (The B.C. is not proved).** The Bridge Conjecture is the central missing ingredient. Without it, the results of this phase are foundational but do not constitute an attack on RH.

**Barrier B2 (The limiting measure $d\mu_\Xi$ requires convergence).** The product $\prod_p L_p(1/2+is)$ converges conditionally on the critical line, and controlling the limit $dm_S \to d\mu_\Xi$ requires a Vinogradov–Korobov-type estimate or similar. Off the critical line or without RH, convergence of the Euler product is an open problem.

**Barrier B3 (The semilocal prolate operator is not constructed).** CCM explicitly mentions that the semilocal prolate operator is the subject of a "forthcoming paper." Proposition 9.3 is conditional on the B.C., and the spectral meaning of $d_n^S \neq 0$ requires that operator.

**Barrier B4 (Weil positivity).** As in all previous phases, the fundamental wall remains: proving that the Weil quadratic form $Q_n(\varphi, \varphi) \geq 0$ is equivalent to RH, and the CCM framework plus our program give two distinct characterizations of the same wall, without overcoming it.

---

## §11. Synthesis and direction of Phase 32

The results of this document establish:

1. The semilocal measure $dm_S$ for $S = \{\infty, p\}$ is explicitly computable (Proposition 2.1, Lemma 4.1, Proposition 4.2).

2. The Jacobi discrepancy $\Delta_n^S > 0$ for every $S \supsetneq \{\infty\}$ (Proposition 3.2).

3. The discrepancy coefficients of the prolate operator $d_n^S$ are completely determined by the increments $\Delta_n^S - \Delta_{n-1}^S$ (Proposition 9.1).

4. The Bridge Conjecture (B.C.) asserts that $C_\infty(\gamma_n)$ is the renormalized limit of $\sum_p \Delta_n^{\{\infty,p\}}/\log p$ (§7).

5. Under the B.C.: $d_n^S = 0$ for every $n, S$ $\Leftrightarrow$ RH (Proposition 9.3).

**The goal of Doc 60** is to attack the weak version of the B.C.: proving that $\Delta_n^{\{\infty,p\}} \to 0$ as $p \to \infty$ at a rate controlled by $C_\infty(\gamma_n)$, and that $\sum_{p \leq T} \Delta_n^{\{\infty,p\}}/\log p \sim C_\infty(\gamma_n) \log T$.

---

## References

- [CCM24] A. Connes, C. Consani, H. Moscovici. *Zeta zeros and prolate wave operators*. Ann. Funct. Anal. (2024). https://doi.org/10.1007/s43034-024-00388-z
- [Sz75] G. Szegő. *Orthogonal Polynomials*. AMS, 4th ed., 1975. [CCM24 Ref. 18]
- Doc 42: Deficit formula and positivity of $C_\infty$.
- Doc 43: Rigidity Theorem — a zero of the deficit implies RH.
- Doc 54: Arithmetic formula $C_\infty(\gamma_n) = w(\gamma_n) - 2\text{Re}[A_n]$.
- Doc 57: Connection with the De Bruijn–Newman constant.
- Doc 58: $c_* = \inf_n C_\infty(\gamma_n) = 0$ unconditionally.
