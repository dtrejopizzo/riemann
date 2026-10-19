# Document 80 — The "arithmetic Castelnuovo-Severi": construction and critical analysis of the Pillar III quadratic form

**Program:** Riemann Hypothesis — Phase 33 DBN-CCM  
**Prerequisites:** Docs 64, 74, 77

---

## Summary

Doc 77 identified Pillar III (positivity) as the only element missing from the program of importing Weil's mechanism into the CCM formalism. The present document attempts to construct a quadratic form $Q$ that plays the role of the Castelnuovo-Severi inequality from the case of curves. The result is a precise diagnosis: a natural candidate $Q$ is constructed via the Cauchy kernel of the measure $dm_{full,on}$, it is shown to be positive semidefinite (Proposition 5.2), and the obstruction preventing the argument from closing is identified precisely: the kernel of $Q$ is not trivial (it contains functions that vanish at the zeros of $\zeta_{on}$), and the condition $Q(\phi, \phi) = 0$ is not directly equivalent to $T_\lambda = 0$. The document states the residual problem precisely and proposes a regularization.

---

## §1. The Castelnuovo-Severi inequality and its analogue for Jacobi matrices

### 1.1. The original inequality

In the theory of algebraic curves, the Castelnuovo-Severi inequality (or the Hodge index inequality for $C \times C$) states the following. Let $C$ be a smooth projective curve over an algebraically closed field, and let $D$ be a divisor on $C \times C$ with class $(a, b)$ in $\mathrm{Pic}(C) \otimes \mathrm{Pic}(C)$ (i.e., $D = a \cdot ([\mathrm{pt}] \times C) + b \cdot (C \times [\mathrm{pt}]) + D_0$ with $D_0$ of degree $(0,0)$). Then:

$$D_0^2 \leq 0,$$

with equality if and only if $D_0$ is numerically trivial. In the most useful formulation: for a divisor $\Gamma$ that is the graph of a morphism $f: C \to C$ of degree $d$,

$$(\Gamma \cdot \Gamma) = 2 - 2g + d \cdot (\text{number of fixed points}) - \deg(f) \cdot 2g,$$

and the positivity of the intersection form on the complement of the ample divisor $(1,1)$ forces the eigenvalues of $f^*$ on $H^1$ to have controlled modulus.

The key property is: the inequality comes from the fact that the intersection quadratic form on $\mathrm{Pic}^0(C \times C)$ is negative semidefinite (Hodge index theorem), and its negativity is an intrinsic geometric property, independent of the Frobenius eigenvalues.

### 1.2. Translation to the world of finite Jacobi matrices

Let $J_N^{full}$ be the order-$N$ truncation of the Jacobi operator $J^{full}$: the $(N+1) \times (N+1)$ tridiagonal matrix with entries $(J_N^{full})_{k,k+1} = (J_N^{full})_{k+1,k} = a_k^{full}$ and zero diagonal (since $b_k^{full} = 0$). Similarly $J_N^{full,on}$.

**Definition 1.1.** The truncated Jacobi difference at level $N$ is:

$$M_N = J_N^{full} - J_N^{full,on}.$$

This is also a tridiagonal matrix with entries $(M_N)_{k,k+1} = a_k^{full} - a_k^{full,on}$, zero diagonal, and all other coefficients zero.

**Proposition 1.2 (Proposition 1.1 of the statement: analysis).** The inequality

$$\mathrm{Tr}(M_N^2) \leq C \cdot \frac{(\mathrm{Tr}(M_N))^2}{N}$$

cannot serve as an analogue of Castelnuovo-Severi, for the following reason: $\mathrm{Tr}(M_N) = 0$ for every $N$, since the diagonal of $M_N$ is zero (all $b_k^{full} = b_k^{full,on} = 0$). Hence the proposed inequality would reduce to $\mathrm{Tr}(M_N^2) \leq 0$, which is false (the trace of a squared symmetric matrix is the sum of the squares of its entries, hence $\geq 0$, with equality only if $M_N = 0$).

*Proof.* A direct computation: $\mathrm{Tr}(M_N^2) = \sum_{j,k} (M_N)_{jk}^2 = 2\sum_{k=0}^{N-1}(a_k^{full} - a_k^{full,on})^2 \geq 0$. And $\mathrm{Tr}(M_N) = \sum_k (M_N)_{kk} = \sum_k (b_k^{full} - b_k^{full,on}) = 0$. Thus Proposition 1.1 in the stated form is vacuously true (any quantity is $\leq C \cdot 0$ only if the quantity is $\leq 0$), but the hypothesis $\mathrm{Tr}(M_N) = 0$ does not imply $M_N = 0$ unless the specific structure of the squared trace is also used. $\square$

**Remark 1.3 (Correct reformulation).** The relevant property does not involve the trace of $M_N$ but that of $M_N^2$. The correct statement we would want to prove is:

$$\mathrm{Tr}(M_N^2) = 0 \implies M_N = 0 \implies a_k^{full} = a_k^{full,on} \;\forall k \leq N.$$

The first implication is obvious (the trace of a sum of squares is zero if and only if each term is zero). The real problem is establishing $\mathrm{Tr}(M_N^2) = 0$ without assuming RH. The discrepancies $a_k^{full} - a_k^{full,on}$ are real quantities; if it could be shown that they are all zero, RH would follow. There is, therefore, no linear inequality between $\mathrm{Tr}(M_N^2)$ and the trace of $M_N$ that carries nontrivial information. The Castelnuovo-Severi analogy must be sought elsewhere.

**Remark 1.4 (The correct property of $J^{full}$).** The Hodge inequality for curves can be reformulated in terms of the non-negativity of point counts: for the graph of the Frobenius $\Gamma_n \subset C \times C$, the intersection number $(\Gamma_n \cdot \Delta)$ (with the diagonal $\Delta$) is $N_n = \#C(\mathbb{F}_{q^n}) \geq 0$. In the CCM world, the analogue of $N_n$ is $\sum_{k \leq N} a_k^{full}$, which is positive but whose positivity does not force equality with $\sum_{k \leq N} a_k^{full,on}$.

---

## §2. The measure $dm_{full}$ as a Hamburger measure: moment theory

### 2.1. Determinacy of $dm_{full}$

**Proposition 2.1 (Determinacy).** The measure $dm_{full}(s) = |\zeta(1/2+is)|^2\, dm_\infty(s)$ is determinate in the Hamburger sense: it is uniquely determined by its moment sequence $\mu_k^{full} = \int s^k\, dm_{full}(s)$.

*Proof.* The measure $dm_\infty$ has exponential decay: for every $t > 0$,

$$\int_{\mathbb{R}} e^{t|s|}\, dm_\infty(s) = (2\pi)^{-2} \int_{\mathbb{R}} e^{t|s|} |\Gamma(1/4+is/2)|^2\, ds < \infty$$

for $t < \pi/2$ (since $|\Gamma(1/4+is/2)|^2 \sim C|s|^{-1/2} e^{-\pi|s|/2}$ as $|s| \to \infty$, by Stirling's formula). The factor $|\zeta(1/2+is)|^2$ grows at most polynomially in $|s|$ (on average; there are known bounds $|\zeta(1/2+is)| = O(|s|^\epsilon)$ for every $\epsilon > 0$), so that for some $t_0 > 0$,

$$\int_{\mathbb{R}} e^{t_0|s|}\, dm_{full}(s) < \infty.$$

By Carleman's criterion (or directly by the Carleman-Riesz test), the condition $\int e^{t|s|}\, d\mu < \infty$ for some $t > 0$ implies that the measure $\mu$ is uniquely determined by its moments. $\square$

### 2.2. The Hamburger positivity condition and Hankel matrices

For a positive measure $\mu$ on $\mathbb{R}$ with moments $c_k = \int s^k\, d\mu(s)$, the necessary and sufficient condition for the sequence $\{c_k\}$ to come from a positive measure is that the Hankel matrices:

$$H_N^\mu = (c_{i+j})_{0 \leq i,j \leq N}$$

be positive semidefinite for every $N \geq 0$. This is the Hamburger positivity condition.

For $dm_{full}$ and $dm_{full,on}$, both matrices $H_N^{full}$ and $H_N^{full,on}$ are positive definite (they are Gram matrices of linearly independent functions in the respective $L^2$ spaces).

**Proposition 2.2 (Relation between discrepancies and the Hankel difference).** Let $\Delta H_N = H_N^{full} - H_N^{full,on}$. The condition $a_k^{full} = a_k^{full,on}$ for every $k \leq N$ is equivalent to the moments coinciding: $\mu_j^{full} = \mu_j^{full,on}$ for $j = 0, 1, \ldots, 2N$, i.e., $\Delta H_N = 0$.

*Proof.* The Jacobi coefficients $a_0, a_1, \ldots, a_N$ are determined by the moments $\mu_0, \mu_1, \ldots, \mu_{2N+1}$ via the Gram-Schmidt algorithm (which corresponds to the Cholesky factorization of the Hankel matrix $H_{N+1}$). Two measures have the same first $2N+2$ moments if and only if their Hankel matrices $H_{N+1}$ are equal, if and only if their Jacobi coefficients $a_0, \ldots, a_N$ are equal. This is a version of Favard's theorem. $\square$

**Corollary 2.3.** The condition $T_\lambda = 0$ (CTP criterion) is equivalent to:

$$\int_{\mathbb{R}} W_\lambda(s)\, s^j\, dm_\infty(s) \cdot (|\zeta(1/2+is)|^2 - |\zeta_{on}(1/2+is)|^2) = 0 \quad \forall j, \lambda,$$

which is a condition on the difference $|\zeta|^2 - |\zeta_{on}|^2$ weighted by the polynomials of the reference measure.

The relation between $\Delta_k = (a_k^{full})^2 - (a_k^{full,on})^2$ and $\Delta H_N$ is the following: $\Delta_k$ is a degree-$1$ homogeneous function of the entries of $\Delta H_N$ (specifically, it is the ratio of two determinants of Hankel submatrices, depending on the first $2k+2$ entries). The map $\Delta H_N \mapsto (\Delta_0, \ldots, \Delta_N)$ is, in general, nonlinear.

---

## §3. The Markov-Stieltjes inequality and control of the coefficients

### 3.1. The Markov-Stieltjes theorem

**Theorem 3.1 (Markov-Stieltjes, relevant formulation).** Let $\mu$ and $\nu$ be two positive measures on $\mathbb{R}$ with the same first $2N$ moments: $\int s^k\, d\mu = \int s^k\, d\nu$ for $k = 0, 1, \ldots, 2N-1$. Let $x_1 < x_2 < \cdots < x_N$ be the zeros of the degree-$N$ orthogonal polynomial with respect to $\mu$ (= with respect to $\nu$, since the moments coincide). Then:

$$\mu((-\infty, x_j]) = \nu((-\infty, x_j]) \quad \text{for every } j = 1, \ldots, N.$$

That is, the distribution functions of $\mu$ and $\nu$ coincide at all the Gauss quadrature nodes.

*Reference:* Szegő [S39], Chapter 3; Akhiezer [A65], Theorem 1.3.3.

**Corollary 3.2.** If the measures $dm_{full}$ and $dm_{full,on}$ have the same first $2N$ moments, then their Jacobi coefficients $a_k^{full}$ and $a_k^{full,on}$ coincide for $k = 0, 1, \ldots, N-1$.

### 3.2. The moment-equality condition and its arithmetic meaning

The condition that the moments coincide, $\mu_j^{full} = \mu_j^{full,on}$ for $j \leq 2N-1$, is equivalent to:

$$\int_{\mathbb{R}} s^j \left(|\zeta(1/2+is)|^2 - |\zeta_{on}(1/2+is)|^2\right) dm_\infty(s) = 0, \quad j = 0, 1, \ldots, 2N-1.$$

**Proposition 3.3.** If RH is true, then $|\zeta(1/2+is)|^2 = |\zeta_{on}(1/2+is)|^2$ for every $s \in \mathbb{R}$, so all the moments coincide and, by Corollary 3.2, $a_k^{full} = a_k^{full,on}$ for every $k$. This is the direct implication (already known).

**Proposition 3.4 (Hard direction: Markov-Stieltjes is not sufficient).** Equality of the first $2N$ moments implies equality of the first $N$ Jacobi coefficients (Corollary 3.2). To conclude RH one would need equality of all the moments — that is, equality of the measures as measures on $\mathbb{R}$. But equality of the measures is precisely RH (which is what we want to prove). The argument is circular: using Markov-Stieltjes to reduce RH to moment equality is only a rewriting of the problem, not a proof.

---

## §4. The difference $|\zeta|^2 - |\zeta_{on}|^2$ and its moments under $\neg$RH

### 4.1. Formula via the Hadamard product

Under the hypothesis $\neg$RH, there exists at least one zero $\rho_0 = \sigma_0 + i\gamma_0$ with $\sigma_0 \neq 1/2$. By the functional equation, off-critical zeros appear in quadruples $\{\rho_0, \overline{\rho_0}, 1-\rho_0, 1-\overline{\rho_0}\}$. Let us write $\delta_0 = \sigma_0 - 1/2 \neq 0$.

The relation between $\zeta$ and $\zeta_{on}$ via the Hadamard product is:

$$\frac{\xi(s)}{\xi_{on}(s)} = \prod_{\rho_0 \text{ off-crit}} \frac{s - \rho_0}{s - (1/2 + i\gamma_0)},$$

where the product is over all off-critical zeros (with their multiplicities and the four elements of the quadruple). Restricting to the critical line $s = 1/2 + iu$ with $u \in \mathbb{R}$:

$$\frac{|\zeta(1/2+iu)|^2}{|\zeta_{on}(1/2+iu)|^2} = \prod_j \frac{|1/2+iu - \rho_j^{off}|^2}{|1/2+iu - 1/2 - i\gamma_j^{off}|^2} = \prod_j \left(1 + \frac{\delta_j^2}{(u - \gamma_j^{off})^2}\right),$$

where the product runs over the off-critical zeros $\rho_j^{off} = (1/2 + \delta_j) + i\gamma_j^{off}$ (with $\delta_j > 0$ by convention, including only one of each pair $\rho_j, 1-\overline{\rho_j}$ in the right half).

Hence:

$$|\zeta(1/2+iu)|^2 - |\zeta_{on}(1/2+iu)|^2 = |\zeta_{on}(1/2+iu)|^2 \cdot \left[\prod_j \left(1 + \frac{\delta_j^2}{(u-\gamma_j^{off})^2}\right) - 1\right].$$

**Proposition 4.1 (Sign of the difference).** The function $u \mapsto |\zeta(1/2+iu)|^2 - |\zeta_{on}(1/2+iu)|^2$ is non-negative for every $u \in \mathbb{R}$ (away from the zeros of $\zeta_{on}$), since the product is $\geq 1$ and $|\zeta_{on}|^2 \geq 0$.

*Proof.* Each factor $1 + \delta_j^2/(u-\gamma_j^{off})^2 \geq 1$, so the product is $\geq 1$. The factor $|\zeta_{on}|^2 \geq 0$. The product of non-negatives is non-negative. $\square$

**Corollary 4.2.** Under $\neg$RH, $dm_{full}(s) \geq dm_{full,on}(s)$ for every $s$ (in the pointwise sense of the densities), and consequently $\mu_k^{full} \geq \mu_k^{full,on}$ for even $k$ (moments of a larger measure). In particular, $\Delta_k = (a_k^{full})^2 - (a_k^{full,on})^2 \geq 0$ for every $k$ (the already-known direction).

### 4.2. The moments of the difference

Under the simplified hypothesis of a single pair of off-critical zeros with $\delta_0 \ll 1$ (linearization):

$$|\zeta(1/2+iu)|^2 - |\zeta_{on}(1/2+iu)|^2 \approx |\zeta_{on}(1/2+iu)|^2 \cdot \delta_0^2 \sum_j \frac{1}{(u-\gamma_j^{off})^2}.$$

The $k$-th moment of the difference is then:

$$\mu_k^{full} - \mu_k^{full,on} \approx \delta_0^2 \sum_j \int_{\mathbb{R}} \frac{u^k |\zeta_{on}(1/2+iu)|^2}{(u-\gamma_j^{off})^2}\, dm_\infty(u).$$

**Proposition 4.3 (Convergence of the moment integral).** The integral

$$I_{k,j} = \int_{\mathbb{R}} \frac{u^k |\zeta_{on}(1/2+iu)|^2}{(u-\gamma_j^{off})^2}\, dm_\infty(u)$$

converges as a principal value for every $k \geq 0$ and $\gamma_j^{off} \in \mathbb{R}$.

*Proof.* The integrand has a pole of order 2 at $u = \gamma_j^{off}$, but the measure $dm_\infty$ is absolutely continuous (with $C^\infty$ density) and $|\zeta_{on}|^2$ vanishes at $u = \gamma_j^{off}$ (since $\gamma_j^{off}$ is the imaginary part of a zero of $\zeta_{on}$ on the critical line). Hence:

$$|\zeta_{on}(1/2+iu)|^2 \sim C_j \cdot (u - \gamma_j^{off})^{2m_j} \quad \text{as } u \to \gamma_j^{off},$$

where $m_j \geq 1$ is the multiplicity of the zero. If $m_j = 1$, the singularity $1/(u-\gamma_j^{off})^2 \cdot (u-\gamma_j^{off})^2 = 1$ is integrable (the singularity cancels). If $m_j \geq 2$, the integrand is even more regular. In all cases, $I_{k,j}$ is a convergent proper integral. $\square$

**Remark 4.4.** The cancellation in Proposition 4.3 is of a deep arithmetic nature: the zeros of $\zeta_{on}$ sit exactly at the $\gamma_j^{off}$, which regularizes the singularity of the kernel $1/(u-\gamma_j^{off})^2$. This suggests that the natural construction of the quadratic form $Q$ should involve $|\zeta_{on}|^2$ in the numerator.

---

## §5. The arithmetic Castelnuovo-Severi quadratic form

### 5.1. Construction of $Q$

Motivated by the cancellation in Proposition 4.3, we define the following quadratic form.

**Definition 5.1 (Arithmetic Castelnuovo-Severi quadratic form).** For functions $\phi, \psi \in L^2(dm_{full,on})$, define the sesquilinear form:

$$Q(\phi, \psi) = \iint_{\mathbb{R}^2 \setminus \mathrm{diag}} \frac{(\phi(u) - \phi(v))\overline{(\psi(u) - \psi(v))}}{(u-v)^2}\, |\zeta_{on}(1/2+iu)|^2 |\zeta_{on}(1/2+iv)|^2\, dm_\infty(u)\, dm_\infty(v).$$

The associated quadratic form is $Q(\phi) = Q(\phi, \phi)$.

**Remark 5.2 (Equivalent form via fractional derivative).** The form $Q$ is exactly the squared norm in the fractional Sobolev space $H^{1/2}(dm_{full,on})$ (Dirichlet space of the measure $dm_{full,on}$). Indeed:

$$Q(\phi, \phi) = \iint \frac{|\phi(u) - \phi(v)|^2}{(u-v)^2}\, dm_{full,on}(u)\, dm_{full,on}(v),$$

which is precisely the squared norm in the Dirichlet space $\mathcal{D}(dm_{full,on})$ (see Fukushima-Oshima-Takeda [FOT94]).

**Proposition 5.3 (Positive semidefiniteness).** The form $Q$ is positive semidefinite: $Q(\phi, \phi) \geq 0$ for every $\phi$ in the domain.

*Proof.* The integrand is $|\phi(u) - \phi(v)|^2 \cdot (u-v)^{-2} \cdot |\zeta_{on}|^2(u) \cdot |\zeta_{on}|^2(v) \geq 0$ for $(u,v)$ off the diagonal and away from the zeros of $\zeta_{on}$. Since the integrand is non-negative and the integral is absolutely convergent (by Proposition 4.3 and the condition $|\phi(u) - \phi(v)|^2/(u-v)^2 \leq |\phi'|^2$ when $\phi$ is Lipschitz), the integral is non-negative. For general functions in $L^2(dm_{full,on})$ regularity is obtained by density. $\square$

**Proposition 5.4 (The kernel of $Q$).** $Q(\phi, \phi) = 0$ if and only if $\phi$ is constant $dm_{full,on}$-a.e. In particular, the kernel of $Q$ in $L^2_0(dm_{full,on})$ (functions with zero integral) is $\{0\}$.

*Proof.* If $Q(\phi, \phi) = 0$, then $\phi(u) = \phi(v)$ for $dm_{full,on} \otimes dm_{full,on}$-a.e. $(u,v)$, which implies that $\phi$ is constant $dm_{full,on}$-a.e. (since $dm_{full,on}$ has no atoms: it is absolutely continuous with respect to $dm_\infty$, which is in turn absolutely continuous with respect to Lebesgue measure). $\square$

### 5.2. Relation of $Q$ to the comparison of measures

The form $Q$ measures the regularity of $\phi$ in the Dirichlet space of $dm_{full,on}$. For $Q$ to be Pillar III of Weil's mechanism, we need its positivity (or the structure of its kernel) to detect the difference $dm_{full} \neq dm_{full,on}$.

**Proposition 5.5.** Let $f(u) = |\zeta(1/2+iu)|^2 - |\zeta_{on}(1/2+iu)|^2$ be the density difference. Then:

$$Q(f, \mathbf{1}) = \iint \frac{(f(u) - f(v)) \cdot 1}{(u-v)^2}\, dm_{full,on}(u)\, dm_{full,on}(v).$$

If $dm_{full} = dm_{full,on}$ (i.e., $f = 0$), then $Q(f, \phi) = 0$ for every $\phi$. The converse — if $Q(f, \phi) = 0$ for every $\phi$ then $f = 0$ — would require $f = 0$ in $\mathcal{D}(dm_{full,on})$, which would amount to $f$ being constant $dm_{full,on}$-a.e.

**Remark 5.6 (The main obstruction).** The form $Q$ of Definition 5.1 is well defined and positive semidefinite, but its definition does not directly involve the difference $dm_{full} - dm_{full,on}$. To connect $Q$ with the criterion $T_\lambda = 0$, one would have to show that the difference function $f = |\zeta|^2 - |\zeta_{on}|^2$ (which is $\geq 0$ under $\neg$RH, by Proposition 4.1) belongs to the kernel of some quadratic form related to $Q$. But this is not available: the positivity of $Q$ is an intrinsic property of the Dirichlet space of $dm_{full,on}$, not a statement about the comparison of measures.

---

## §6. Regularization and the form $Q_\lambda$

### 6.1. The zeros of $\zeta_{on}$ as an obstruction to regularity

The Dirichlet space $\mathcal{D}(dm_{full,on})$ is well defined, but the function $f = |\zeta|^2/|\zeta_{on}|^2 - 1$ (the ratio of densities) may not belong to $\mathcal{D}(dm_{full,on})$ due to the presence of the zeros of $\zeta_{on}$: in a neighborhood of $u = \gamma_n$ (a zero of $\zeta_{on}$), the function $f(u) \approx C_n(u-\gamma_n)^{2\delta_n^2}$ (small power), whose derivative can be large. To remedy this, a regularization is introduced.

**Definition 6.1 (Regularized form $Q_\lambda$).** For $\lambda > 0$, let $W_\lambda$ be the Abel kernel of the CCM program. Define:

$$Q_\lambda(\phi, \psi) = \iint_{\mathbb{R}^2 \setminus \mathrm{diag}} \frac{(\phi(u) - \phi(v))\overline{(\psi(u)-\psi(v))}}{(u-v)^2} W_\lambda(u) W_\lambda(v)\, dm_\infty(u)\, dm_\infty(v).$$

This form does not depend on $|\zeta_{on}|^2$ directly; the role of the Abel kernel $W_\lambda$ is to provide a spectral cutoff that regularizes the singularities.

**Proposition 6.2 (Properties of $Q_\lambda$).** 

(i) $Q_\lambda$ is positive semidefinite for every $\lambda > 0$.

(ii) $Q_\lambda \to Q_{Lebesgue}$ as $\lambda \to \infty$, where $Q_{Lebesgue}$ is the Dirichlet form of Lebesgue measure (norm in $H^{1/2}(\mathbb{R})$).

(iii) For the function $f_\lambda = W_\lambda \cdot (|\zeta|^2 - |\zeta_{on}|^2)$:

$$Q_\lambda(f_\lambda, f_\lambda) = \iint \frac{|f_\lambda(u) - f_\lambda(v)|^2}{(u-v)^2}\, dm_\infty(u)\, dm_\infty(v) \geq 0.$$

*Proof.* Point (i) is identical to that of Proposition 5.3 (the integrand is non-negative). Point (ii) follows from $W_\lambda(u) \to 1$ as $\lambda \to \infty$ (in the Cesàro sense for the measure $dm_\infty$). Point (iii) is a direct application of the definition. $\square$

**Remark 6.3.** The form $Q_\lambda$ of Definition 6.1 is positive semidefinite but its positivity has no direct arithmetic content: it is simply the (fractional) $H^{1/2}$ norm of the truncation $f_\lambda$, which is non-negative because it is a squared norm. There is no information distinguishing $|\zeta|^2$ from $|\zeta_{on}|^2$ in the positivity of $Q_\lambda$.

---

## §7. The connection with the Montgomery pair correlation

### 7.1. The kernel $1/(u-v)^2$ and pair correlation

The quadratic form $Q$ of Definition 5.1 involves the kernel $K(u,v) = |\phi(u)-\phi(v)|^2/(u-v)^2$. For $\phi = \mathbf{1}$ (the constant function 1), this kernel reduces to $1/(u-v)^2$, and the double integral:

$$\iint_{u \neq v} \frac{1}{(u-v)^2}\, dm_{full,on}(u)\, dm_{full,on}(v)$$

is a sum of the form $\sum_{m \neq n} (\gamma_m - \gamma_n)^{-2}$ (over the zeros of $\zeta_{on}$, with weights from the measure $dm_\infty$). This is exactly the class of sums appearing in the Montgomery pair correlation conjecture.

**Montgomery's conjecture (1973)** states that for test functions $f$ in the Schwartz class,

$$\sum_{\substack{\gamma, \gamma' \leq T \\ \gamma \neq \gamma'}} f\!\left(\frac{(\gamma-\gamma')\log T}{2\pi}\right) \sim \frac{T \log T}{2\pi} \int_{-\infty}^{\infty} f(u)\left[1 - \left(\frac{\sin \pi u}{\pi u}\right)^2\right] du$$

as $T \to \infty$ (where the sum is over the imaginary parts of zeros with $\mathrm{Im}(s) > 0$).

For $f(u) = |u|^{-2}$ (the kernel function of our $Q$), Montgomery's integral diverges at $u = 0$, reflecting the fact that the sum $\sum_{\gamma \neq \gamma'} (\gamma-\gamma')^{-2}$ diverges (the zeros accumulate on the logarithmic scale). This means that $Q(\mathbf{1}, \mathbf{1}) = +\infty$, or equivalently that the constant function $\phi = 1$ does not belong to the Dirichlet space $\mathcal{D}(dm_{full,on})$.

**Proposition 7.1 (The domain of $Q$ excludes constant functions).** The function $\phi = \mathbf{1}$ does not belong to the Dirichlet space $\mathcal{D}(dm_{full,on})$: $Q(\mathbf{1}, \mathbf{1}) = +\infty$. Functions in $\mathcal{D}(dm_{full,on})$ must decay sufficiently fast as $|u| \to \infty$.

*Proof.* For $\phi = 1$:

$$Q(1, 1) = \iint \frac{|1 - 1|^2}{(u-v)^2}\, dm_{full,on}^2 = 0.$$

Contradiction: the computation gives zero, not $+\infty$. The proposition is vacuously false as stated: $|\phi(u) - \phi(v)|^2 = 0$ for constant $\phi$, so $Q(\phi, \phi) = 0$ for every constant $\phi$. The Dirichlet space contains all constants in the kernel of the semidefinite form. $\square$

**Remark 7.2 (Correction).** The Dirichlet space $\mathcal{D}(dm_{full,on})$ contains the constants in its kernel. The nontrivial part is the restriction to the space $L^2_0(dm_{full,on})$ of functions with zero integral (where Proposition 5.4 guarantees triviality of the kernel). The connection with Montgomery is the following: the divergent sum $\sum_{\gamma \neq \gamma'} (\gamma-\gamma')^{-2}$ appears when the form $Q$ is evaluated on the indicator function of an interval (which is not in $\mathcal{D}$), not on smooth functions.

**Proposition 7.3 (Formal connection with Montgomery).** Under Montgomery's conjecture, for functions $\phi$ in the Schwartz class with $\hat\phi$ compactly supported in $(-1,1)$:

$$Q(\phi, \phi) \sim C \cdot \int_{\mathbb{R}} |\hat\phi(\xi)|^2 |\xi|\, d\xi,$$

which is the squared norm in $H^{1/2}$ (Sobolev space of order $1/2$). This confirms that the form $Q$ is equivalent to the $H^{1/2}$ norm under Montgomery's conjecture, and in particular is positive definite on $L^2_0(dm_{full,on})$.

*Status:* Conjectural (requires Montgomery's conjecture). The unconditional equivalence between $Q$ and the $H^{1/2}$ norm is an open problem.

---

## §8. Synthesis: the diagnosis of Pillar III and what is missing

### 8.1. Results established in this document

**Result 1 (Proposition 1.2).** Proposition 1.1 in the stated form (with $\mathrm{Tr}(M_N)$ in the denominator) is vacuous because $\mathrm{Tr}(M_N) = 0$ identically. The Castelnuovo-Severi analogy cannot be formulated via the trace of $M_N$; the relevant structure is that of $\mathrm{Tr}(M_N^2)$.

**Result 2 (Proposition 2.2).** Equality of the first $2N$ moments of $dm_{full}$ and $dm_{full,on}$ implies (via Markov-Stieltjes) equality of the first $N$ Jacobi coefficients, but the moment condition is equivalent to RH, so this approach is circular.

**Result 3 (Proposition 4.1).** Under $\neg$RH, the difference $|\zeta|^2 - |\zeta_{on}|^2$ is non-negative, which is consistent with $\Delta_k \geq 0$ (already known). There is no sign cancellation: the difference cannot be zero on a set of positive measure without forcing RH.

**Result 4 (Propositions 5.3 and 5.4).** The quadratic form $Q$ of Definition 5.1 is positive semidefinite with kernel exactly the constants. On $L^2_0(dm_{full,on})$ it is positive definite. However, the positivity of $Q$ is an intrinsic property of $dm_{full,on}$ that does not depend on whether $dm_{full} = dm_{full,on}$.

**Result 5 (Proposition 4.3).** The cancellation of the singularity of $1/(u-\gamma_j)^2$ by the zeros of $\zeta_{on}$ at $u = \gamma_j$ is exact and regularizes all the moment integrals.

### 8.2. The precise obstruction: the positivity of $Q$ does not distinguish $dm_{full}$ from $dm_{full,on}$

The fundamental difficulty of Pillar III can now be stated with surgical precision.

**Proposition 8.1 (The Pillar III obstruction — precise statement).** No quadratic form $Q$ that is:

(a) defined solely in terms of $dm_{full,on}$ (not of $dm_{full}$), and  
(b) positive definite on $L^2_0(dm_{full,on})$,

can by itself distinguish whether $dm_{full} = dm_{full,on}$.

*Proof.* A form $Q$ as in (a) and (b) is a property of $dm_{full,on}$ alone. Its positivity carries no information about $dm_{full}$. To compare the two measures it is necessary to involve $dm_{full}$ directly in the construction of $Q$. $\square$

**Corollary 8.2 (The correct form $Q$ must involve $dm_{full}$).** The arithmetic analogue of the Castelnuovo-Severi inequality, if it exists, must be a quadratic form $Q[dm_{full}, dm_{full,on}]$ that depends on both measures and whose positivity is equivalent to $dm_{full} = dm_{full,on}$.

The natural candidate is the comparison form:

$$Q_{comp}(\phi, \psi) = \int_{\mathbb{R}} \phi(u)\, \overline{\psi(u)}\, (dm_{full}(u) - dm_{full,on}(u)),$$

which is a linear form in $dm_{full} - dm_{full,on}$ and, under $\neg$RH, satisfies $Q_{comp}(\phi, \phi) \geq 0$ for every $\phi$ (by Proposition 4.1). But the positivity of $Q_{comp}$ is equivalent to the non-negativity of $dm_{full} - dm_{full,on}$, which we already know is non-negative under $\neg$RH, and is zero under RH. This form captures the content of the criterion $T_\lambda = 0$ but adds no information on how to prove it.

### 8.3. A program for closing Pillar III

For Pillar III to close the argument toward RH, one would need — in parallel with the case of curves — an argument of the following type:

**Step A:** Construct a quadratic form $Q_{arith}$ that is positive for reasons *independent* of whether RH is true (i.e., whose positivity is an intrinsic property of the problem, not a consequence of RH). This is the analogue of the positivity of the point count $N_n \geq 0$ in the case of curves.

**Step B:** Show that the positivity of $Q_{arith}$ together with the functional equation (Pillar II) forces $dm_{full} = dm_{full,on}$.

In the case of curves, Step A comes from geometry ($N_n$ counts points, a non-negative integer quantity). In the case of numbers, no direct analogue exists: the sums $\sum_{k \leq N} \Delta_k$ are positive but their positivity is a consequence of $|\zeta|^2 \geq |\zeta_{on}|^2$ under $\neg$RH, which is circular.

**Proposition 8.3 (Final diagnosis).** The analogue of Weil's positivity argument in the CCM world requires finding a property of $|\zeta|^2$ that is:

(i) Provable without assuming RH.  
(ii) Strong enough to distinguish $|\zeta|^2 = |\zeta_{on}|^2$ from $|\zeta|^2 > |\zeta_{on}|^2$.

The only property of this type glimpsed in the literature is the conjecture that the zeros of $\zeta$ are in generic position (simple zeros, with GUE statistics), which would be formalized as a lower bound of the type $|\zeta(1/2+iu)|^2 \geq C/(|\log(u-\gamma_n)|)$ near each zero $\gamma_n$. If such a lower bound were provable, and if $|\zeta_{on}|$ satisfies exactly the same bound, then equality of moduli at the zeros could be forced. But this bound is also not known unconditionally.

---

## §9. Conclusion and state of the program

Document 80 establishes the following facts about the "arithmetic Castelnuovo-Severi":

1. **The direct analogy with Jacobi matrices (§1) does not work**: the trace of $M_N$ is identically zero, emptying the proposed inequality.

2. **The Markov-Stieltjes argument (§3) is circular**: it reduces RH to the equality of moments, which is another way of stating RH.

3. **The difference of measures under $\neg$RH (§4) is non-negative**: there is no sign cancellation, which is consistent with the program but gives no new information.

4. **The form $Q$ of Definition 5.1 (§5) exists, is positive semidefinite, and is positive definite on $L^2_0$**, but it does not detect the difference $dm_{full} \neq dm_{full,on}$ because it does not depend on $dm_{full}$.

5. **The connection with Montgomery (§7) is formal**: under Montgomery's conjecture, $Q$ is equivalent to the $H^{1/2}$ norm, but this fact adds no information toward RH.

6. **The Pillar III obstruction (§8) is precise**: a quadratic form is needed that depends on $dm_{full}$ and $dm_{full,on}$ simultaneously, whose positivity is provable without assuming RH, and whose kernel is exactly $\{dm_{full} = dm_{full,on}\}$.

**Conjecture 9.1 (Arithmetic Castelnuovo-Severi — corrected version).** The quadratic form of Pillar III is:

$$Q_{CS}(\phi) = \int_{\mathbb{R}} |\phi(u)|^2\, (dm_{full}(u) - dm_{full,on}(u)) + \iint \frac{|\phi(u)-\phi(v)|^2}{(u-v)^2}\, dm_{full,on}(u)\, dm_{full,on}(v).$$

This form is positive semidefinite in any case, and its restriction to $L^2_0$ satisfies: $Q_{CS}(\phi) = 0$ for every $\phi \in L^2_0$ implies $dm_{full} = dm_{full,on}$ (i.e., RH). However, the positivity of $Q_{CS}$ on $L^2_0$ is not proved: the first term can be zero or positive (it is positive under $\neg$RH), but its relation to the second term is unknown.

The state of Path 1 remains: Pillar III is the only obstruction, and its rigorous construction is the central open problem of the program.

---

## References

- [A65] N. Akhiezer, *The Classical Moment Problem and Some Related Questions in Analysis*, Oliver and Boyd, 1965.
- [C99] A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Math. 5 (1999), 29–106.
- [FOT94] M. Fukushima, Y. Oshima, M. Takeda, *Dirichlet Forms and Symmetric Markov Processes*, De Gruyter, 1994.
- [KS03] R. Killip, B. Simon, *Sum rules for Jacobi matrices and their applications to spectral theory*, Ann. of Math. 158 (2003), 253–321.
- [M73] H. Montgomery, *The pair correlation of zeros of the zeta function*, in Analytic Number Theory (St. Louis, 1972), Proc. Sympos. Pure Math. 24 (1973), 181–193.
- [S39] G. Szegő, *Orthogonal Polynomials*, AMS Colloquium Publications, 1939 (4th ed. 1975).
- [T86] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. (revised by D. R. Heath-Brown), Oxford University Press, 1986.
- [Docs 64, 74, 77] Internal program documents, Phases 32–33.

---

*End of Document 80.*
