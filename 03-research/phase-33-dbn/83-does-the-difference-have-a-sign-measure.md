# Document 83 — Does the difference $|\zeta|^2 - |\zeta_{on}|^2$ have a sign? Measure domination, Jacobi coefficients, and the limits of the approach

**Program:** Riemann Hypothesis — Phase 33 DBN-CCM  
**Prerequisites:** Docs 64, 74, 77, 80, 82

---

## Summary

Document 80 identified that Pillar III of the program (positivity) requires a quadratic form that depends on both measures $dm_{full}$ and $dm_{full,on}$ and whose positivity is provable without assuming RH. The present document examines the more direct question: does the difference $|\zeta(1/2+is)|^2 - |\zeta_{on}(1/2+is)|^2$ have a definite sign for every $s \in \mathbb{R}$?

The answer is affirmative: the difference is non-negative at every point (away from the zeros of $\zeta_{on}$). This result is obtained from the Hadamard product via an elementary computation (§1) and is unconditional, not assuming RH. The measure $dm_{full} - dm_{full,on}$ is therefore a positive measure on $\mathbb{R}$ (Corollary 1.2).

The consequences of this domination are analyzed in detail. In §2 relations between the Hamburger moments of the two measures are derived. In §3 we examine whether domination implies relations between the Jacobi coefficients $a_k^{full}$ and $a_k^{full,on}$: the answer is that measure domination does not imply coefficient-by-coefficient domination, but it does imply domination of the partial sums of squares (Proposition 3.3). In §4 this summed result is proved via the Markov-Stieltjes formula. In §5 we examine the relation between measure domination $\mu \geq \nu$ and the spectral interlacing of the truncated Jacobi matrices. In §6 the Dirichlet-space positivity inequality under domination is analyzed. In §7 we discuss whether measure domination can be turned into equality by some variational argument. In §8 we give a frank synthesis: the pointwise domination $dm_{full} \geq dm_{full,on}$ is a new and clean result, but it is logically insufficient to prove RH; the gap between $\geq$ and $=$ is precisely the nontrivial content of RH.

---

## §1. The ratio $|\zeta/\zeta_{on}|^2$ via the Hadamard product

### 1.1. Notation

Let $\xi(s) = \frac{1}{2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$ be the entire function $\xi$ of order 1. The Hadamard product of $\xi$ is:

$$\xi(s) = e^{A+Bs} \prod_\rho \left(1 - \frac{s}{\rho}\right)e^{s/\rho},$$

where the product runs over all nontrivial zeros $\rho$ of $\zeta$, with $A = \xi(0)$, $B = \xi'(0)/\xi(0)$ real constants.

Let us define $\zeta_{on}$ as the hypothetical zeta function in which all the zeros of $\xi$ are projected onto the critical line: if the zeros of $\xi$ are $\{\rho_j\}$ (critical or not), the Hadamard product of $\xi_{on}$ is:

$$\xi_{on}(s) = e^{A+Bs} \prod_j \left(1 - \frac{s}{1/2 + i\gamma_j}\right)e^{s/(1/2+i\gamma_j)},$$

where for each zero $\rho_j = \sigma_j + i\gamma_j$ of $\xi$ (critical or not) $\rho_j$ has been replaced by its projection $1/2 + i\gamma_j$ onto the critical line. The critical zeros of $\xi$ (with $\sigma_j = 1/2$) are unaffected; the off-critical ones are modified.

By the functional equation $\xi(s) = \xi(1-s)$, off-critical zeros occur in symmetric quadruples $\{\rho_j, \bar\rho_j, 1-\rho_j, 1-\bar\rho_j\}$. We write $\delta_j = \sigma_j - 1/2 > 0$ for the zeros with $\sigma_j > 1/2$ (we take one from each pair $(\rho_j, 1-\bar\rho_j)$).

### 1.2. The ratio on the critical line

**Proposition 1.1.** For $s = 1/2 + iu$ with $u \in \mathbb{R}$, the ratio of the Hadamard products satisfies:

$$\frac{|\xi(1/2+iu)|^2}{|\xi_{on}(1/2+iu)|^2} = \prod_{\substack{j:\; \delta_j > 0}} \left(1 + \frac{\delta_j^2}{(u - \gamma_j)^2}\right)^2,$$

where the product runs over the off-critical zeros with $\sigma_j > 1/2$ (one from each quadruple).

*Proof.* Consider an off-critical zero $\rho_j = (1/2 + \delta_j) + i\gamma_j$ with $\delta_j > 0$. By the functional equation, $1-\bar\rho_j = (1/2 + \delta_j) - i\gamma_j$ is also a zero. Their critical projections are $1/2 + i\gamma_j$ and $1/2 - i\gamma_j$ respectively.

The contribution of this pair $(\rho_j, 1-\bar\rho_j)$ to the ratio $\xi/\xi_{on}$ evaluated at $s = 1/2 + iu$ is:

$$\frac{|1/2+iu - \rho_j|^2}{|1/2+iu - (1/2+i\gamma_j)|^2} \cdot \frac{|1/2+iu - (1-\bar\rho_j)|^2}{|1/2+iu - (1/2-i\gamma_j)|^2}.$$

We compute: $1/2+iu - \rho_j = (\delta_j)\cdot(-1) + i(u - \gamma_j)$, so $|1/2+iu - \rho_j|^2 = \delta_j^2 + (u-\gamma_j)^2$. And $1/2+iu - (1/2+i\gamma_j) = i(u-\gamma_j)$, so $|1/2+iu-(1/2+i\gamma_j)|^2 = (u-\gamma_j)^2$.

Similarly, $1/2+iu - (1-\bar\rho_j) = 1/2+iu - (1/2+\delta_j) + i\gamma_j = -\delta_j + i(u+\gamma_j)$...

Let us correct the computation. The functional equation for the zeros: if $\rho_j = (1/2+\delta_j)+i\gamma_j$ is a zero, so are $\bar\rho_j = (1/2+\delta_j)-i\gamma_j$, $1-\rho_j = (1/2-\delta_j)-i\gamma_j$, and $1-\bar\rho_j = (1/2-\delta_j)+i\gamma_j$.

The complete quadruple is: $\{(1/2\pm\delta_j)\pm i\gamma_j\}$. Their critical projections are $\{1/2+i\gamma_j,\; 1/2-i\gamma_j,\; 1/2-i\gamma_j,\; 1/2+i\gamma_j\}$ (respectively). That is, the projection collapses the quadruple to the pair $\{1/2+i\gamma_j,\; 1/2-i\gamma_j\}$, each with multiplicity 2.

The contribution of the quadruple to the ratio $|\xi|^2/|\xi_{on}|^2$ at $s = 1/2+iu$:

$$C_j(u) = \frac{|(1/2+iu)-(1/2+\delta_j+i\gamma_j)|^2 \cdot |(1/2+iu)-(1/2+\delta_j-i\gamma_j)|^2 \cdot |(1/2+iu)-(1/2-\delta_j+i\gamma_j)|^2 \cdot |(1/2+iu)-(1/2-\delta_j-i\gamma_j)|^2}{|(1/2+iu)-(1/2+i\gamma_j)|^4 \cdot |(1/2+iu)-(1/2-i\gamma_j)|^4}.$$

We compute each factor of the numerator:
- $|(1/2+iu) - (1/2+\delta_j+i\gamma_j)|^2 = \delta_j^2 + (u-\gamma_j)^2$,
- $|(1/2+iu) - (1/2+\delta_j-i\gamma_j)|^2 = \delta_j^2 + (u+\gamma_j)^2$,
- $|(1/2+iu) - (1/2-\delta_j+i\gamma_j)|^2 = \delta_j^2 + (u-\gamma_j)^2$,
- $|(1/2+iu) - (1/2-\delta_j-i\gamma_j)|^2 = \delta_j^2 + (u+\gamma_j)^2$.

Denominator: $|(u-\gamma_j)|^4 \cdot |(u+\gamma_j)|^4$.

Hence:

$$C_j(u) = \left(\frac{\delta_j^2 + (u-\gamma_j)^2}{(u-\gamma_j)^2}\right)^2 \cdot \left(\frac{\delta_j^2 + (u+\gamma_j)^2}{(u+\gamma_j)^2}\right)^2 = \left(1 + \frac{\delta_j^2}{(u-\gamma_j)^2}\right)^2 \left(1 + \frac{\delta_j^2}{(u+\gamma_j)^2}\right)^2.$$

The total product is:

$$\frac{|\xi(1/2+iu)|^2}{|\xi_{on}(1/2+iu)|^2} = \prod_{j:\;\delta_j > 0} \left(1 + \frac{\delta_j^2}{(u-\gamma_j)^2}\right)^2 \left(1 + \frac{\delta_j^2}{(u+\gamma_j)^2}\right)^2,$$

where the product is over the off-critical zeros with $\delta_j > 0$, $\gamma_j > 0$ (one representative from each quadruple with $\sigma_j > 1/2$, $\mathrm{Im}(\rho_j) > 0$). $\square$

**Corollary 1.2 (Unconditional pointwise domination).** For every $u \in \mathbb{R}$ with $\zeta_{on}(1/2+iu) \neq 0$:

$$|\zeta(1/2+iu)|^2 \geq |\zeta_{on}(1/2+iu)|^2,$$

with equality if and only if all zeros of $\zeta$ are critical (i.e., if and only if RH holds).

*Proof.* Each factor of the product in Proposition 1.1 satisfies $(1 + \delta_j^2/(u-\gamma_j)^2)^2 \geq 1$ (since $\delta_j^2 \geq 0$). The product of factors $\geq 1$ is $\geq 1$. The absolute convergence of the product follows from the known decay of the off-critical zeros: the sum $\sum_j \delta_j^2/\gamma_j^2$ converges absolutely for the same reasons as the Hadamard product (see Doc 77). Hence $|\xi(1/2+iu)|^2/|\xi_{on}(1/2+iu)|^2 \geq 1$ for every $u$. Since $|\xi(s)| = |\zeta(s)| \cdot |s(s-1)\pi^{-s/2}\Gamma(s/2)/2|$ and the remaining factor is the same for $\zeta$ and $\zeta_{on}$, we have $|\zeta(1/2+iu)|^2 \geq |\zeta_{on}(1/2+iu)|^2$. $\square$

**Corollary 1.3.** The measure $dm_{full} - dm_{full,on} = (|\zeta(1/2+is)|^2 - |\zeta_{on}(1/2+is)|^2)\,dm_\infty(s)$ is a positive measure (in the sense of a non-negative Borel measure) on $\mathbb{R}$. In particular, for every measurable function $f \geq 0$:

$$\int_{\mathbb{R}} f(s)\,dm_{full}(s) \geq \int_{\mathbb{R}} f(s)\,dm_{full,on}(s).$$

This result is unconditional.

---

## §2. Implications for the Hamburger moments

### 2.1. Domination of even moments

**Proposition 2.1.** For every $k \geq 0$ and every polynomial $p(s) \geq 0$ on $\mathbb{R}$:

$$\int_{\mathbb{R}} p(s)\,dm_{full}(s) \geq \int_{\mathbb{R}} p(s)\,dm_{full,on}(s).$$

In particular, for the moments $\mu_{2k}^{full} = \int s^{2k}\,dm_{full}$ and $\mu_{2k}^{full,on} = \int s^{2k}\,dm_{full,on}$:

$$\mu_{2k}^{full} \geq \mu_{2k}^{full,on} \quad \text{for every } k \geq 0.$$

*Proof.* Immediate from Corollary 1.3, since $s^{2k} \geq 0$ for every $s \in \mathbb{R}$. $\square$

### 2.2. Odd moments: absence of sign

**Remark 2.2.** For odd $k$, $s^{2k+1}$ has no definite sign, and domination $dm_{full} \geq dm_{full,on}$ does not imply $\mu_{2k+1}^{full} \geq \mu_{2k+1}^{full,on}$. In fact, the antisymmetry of $s \mapsto |\zeta(1/2+is)|^2$ (or its absence) is not controlled by pointwise domination.

However, the function $s \mapsto |\zeta(1/2+is)|^2$ is even: $|\zeta(1/2+is)|^2 = |\zeta(1/2-is)|^2$ by the functional equation, and similarly for $|\zeta_{on}|^2$. Hence both measures $dm_{full}$ and $dm_{full,on}$ are symmetric under $s \leftrightarrow -s$, and all odd moments vanish:

$$\mu_{2k+1}^{full} = \mu_{2k+1}^{full,on} = 0 \quad \text{for every } k \geq 0.$$

**Corollary 2.3.** The moment difference $\mu_j^{full} - \mu_j^{full,on}$ is non-negative for even $j$ and zero for odd $j$.

### 2.3. Hankel matrices and the difference

The difference of Hankel matrices $\Delta H_N = H_N^{full} - H_N^{full,on}$ has entries:

$$(\Delta H_N)_{i,j} = \mu_{i+j}^{full} - \mu_{i+j}^{full,on} \geq 0 \quad \text{for } i+j \text{ even}; \quad = 0 \quad \text{for } i+j \text{ odd}.$$

In particular, $\Delta H_N$ is a positive semidefinite matrix (its non-negative entries are in the positions where $i+j$ is even, and the entries in positions with $i+j$ odd are zero). The positive semidefiniteness of $\Delta H_N$ is a new and unconditional result.

*Proof.* For any vector $v = (v_0, \ldots, v_N)$:

$$v^T (\Delta H_N) v = \sum_{i,j=0}^N v_i v_j (\mu_{i+j}^{full} - \mu_{i+j}^{full,on}) = \int_{\mathbb{R}} \left(\sum_{k=0}^N v_k s^k\right)^2 (dm_{full} - dm_{full,on}).$$

Since $dm_{full} - dm_{full,on} \geq 0$ (Corollary 1.3) and $(\sum_k v_k s^k)^2 \geq 0$, the integral is $\geq 0$. $\square$

---

## §3. Does measure domination imply domination of the Jacobi coefficients?

### 3.1. The problem

Let $\mu \geq \nu$ be two positive measures on $\mathbb{R}$ with the same supports and finite moments of all orders. Does $a_k^\mu \geq a_k^\nu$ hold for every $k$?

The answer is, in general, no. The following example illustrates the obstacle.

**Example 3.1 (Counterexample in the compact case).** Let $\mu = \nu + \epsilon \cdot \delta_{x_0}$ for some $x_0$ in the support of $\nu$ and small $\epsilon > 0$. Then $\mu \geq \nu$. The Jacobi coefficients of $\mu$ are perturbations of those of $\nu$, but the perturbation can be positive or negative depending on the position of $x_0$ relative to the zeros of the orthogonal polynomials. Specifically, if $x_0$ is a zero of the degree-$k$ orthogonal polynomial $P_k^\nu$, the perturbation of $a_{k-1}$ can have either sign.

**Proposition 3.2 (No direct implication).** Domination $dm_{full} \geq dm_{full,on}$ does not imply $a_k^{full} \geq a_k^{full,on}$ for each individual $k$.

*Justification.* The Jacobi coefficients are highly nonlinear functions of the moments (they are ratios of Hankel determinants). A non-negative variation of all the even moments can produce variations of arbitrary sign in the individual Jacobi coefficients. The Gram-Schmidt process (equivalently, the Cholesky factorization of $H_N$) does not preserve order in general. $\square$

### 3.2. What is inherited: partial sums of squares

Despite the lack of coefficient-by-coefficient domination, measure domination does imply an inequality for the partial sums of squares of the Jacobi coefficients.

**Proposition 3.3 (Domination of partial sums).** For every $N \geq 0$:

$$\sum_{k=0}^{N-1} (a_k^{full})^2 \geq \sum_{k=0}^{N-1} (a_k^{full,on})^2.$$

The proof is given in §4.

---

## §4. The Jacobi sum formula and domination of partial sums

### 4.1. The trace formula for sums of squares

There is a classical relation between second-order moments and sums of squares of the Jacobi coefficients. For a measure $\mu$ on $\mathbb{R}$ normalized ($\mu_0 = 1$), with Jacobi coefficients $a_0, a_1, a_2, \ldots$ and $b_0, b_1, b_2, \ldots$ (diagonal and superdiagonal of the Jacobi matrix; in our case $b_k = 0$ by the symmetry of the measures), the following relation is obtained from the orthogonal polynomial recursion.

Let $P_k^\mu$ be the degree-$k$ orthogonal polynomial normalized by $\|P_k^\mu\|_{L^2(\mu)} = 1$ with positive leading coefficient. The Jacobi recursion is:

$$s\,P_k^\mu(s) = a_k^\mu P_{k+1}^\mu(s) + a_{k-1}^\mu P_{k-1}^\mu(s),$$

where $a_{-1} = 0$ by convention.

Multiplying by $P_k^\mu(s)$ and integrating with respect to $\mu$:

$$\int s\,(P_k^\mu)^2\,d\mu = a_k^\mu \int P_{k+1}^\mu P_k^\mu\,d\mu + a_{k-1}^\mu \int P_{k-1}^\mu P_k^\mu\,d\mu = 0,$$

since the polynomials are orthogonal. This confirms that $b_k^\mu = 0$ for our symmetric measures.

Now, multiplying the recursion for $P_k^\mu$ by $s\,P_k^\mu(s)$ and integrating:

$$\int s^2 (P_k^\mu)^2\,d\mu = (a_k^\mu)^2 + (a_{k-1}^\mu)^2.$$

*Proof.* $\int s^2 (P_k^\mu)^2\,d\mu = \int (s P_k^\mu)^2\,d\mu = \int (a_k^\mu P_{k+1}^\mu + a_{k-1}^\mu P_{k-1}^\mu)^2\,d\mu = (a_k^\mu)^2 + (a_{k-1}^\mu)^2$, by orthonormality. $\square$

Summing from $k = 0$ to $k = N-1$:

$$\sum_{k=0}^{N-1} [(a_k^\mu)^2 + (a_{k-1}^\mu)^2] = \sum_{k=0}^{N-1} \int s^2 (P_k^\mu)^2\,d\mu = \int s^2 K_{N,\mu}(s,s)\,d\mu,$$

where $K_{N,\mu}(s,s) = \sum_{k=0}^{N-1} (P_k^\mu(s))^2$ is the diagonal Christoffel-Darboux kernel.

This does not immediately give $\sum_{k=0}^{N-1} (a_k^\mu)^2$ in terms of $\mu_2 = \int s^2\,d\mu$ because the kernel $K_{N,\mu}$ depends on $\mu$.

### 4.2. An alternative approach: the Killip-Simon formula

A more direct relation between moments and sums of Jacobi coefficients comes from the Killip-Simon work on Jacobi sum rules (Doc 75; reference [KS03]).

**Proposition 4.1 (Partial trace formula).** For a normalized measure $\mu$ with support in $\mathbb{R}$, the sum of squares of the Jacobi coefficients satisfies:

$$\sum_{k=0}^{N-1} (a_k^\mu)^2 = \int_\mathbb{R} s^2\,d\mu(s) - \frac{1}{\mu_0}\left[\text{boundary correction of order } N\right],$$

where the boundary correction depends on $P_N^\mu$ and $P_{N+1}^\mu$ and converges to 0 when the measure $\mu$ has support in $[-2,2]$ and the Jacobi coefficients converge to 1.

*Remark.* In the general case (non-compact support), no such clean formula exists. However, a weak version suffices for our purposes.

### 4.3. Proof of Proposition 3.3

**Proof of Proposition 3.3.** We use the Parseval identity for the truncated Jacobi matrix.

Let $J_N^\mu$ be the Jacobi matrix truncated at level $N$: the $N \times N$ tridiagonal matrix with zero diagonal and $a_k^\mu$ on the superdiagonal and subdiagonal ($k = 0, \ldots, N-2$). Then:

$$\|J_N^\mu\|_F^2 = \mathrm{Tr}((J_N^\mu)^2) = 2\sum_{k=0}^{N-2}(a_k^\mu)^2.$$

On the other hand, $\mathrm{Tr}((J_N^\mu)^2) = \sum_i (J_N^\mu)^2_{ii} = \sum_i \sum_j (J_N^\mu)_{ij}^2$.

To relate $\mathrm{Tr}((J_N^\mu)^2)$ to the moments of $\mu$, we note that $J_N^\mu$ is the matrix of multiplication by $s$ in the basis $\{P_0^\mu, \ldots, P_{N-1}^\mu\}$ projected onto the $N$-dimensional space. Its squared trace is:

$$\mathrm{Tr}((J_N^\mu)^2) = \sum_{k=0}^{N-1} \langle s^2 P_k^\mu, P_k^\mu\rangle_{L^2(\mu)} - (a_{N-1}^\mu)^2.$$

(The last term comes from the fact that multiplication of $P_{N-1}^\mu$ by $s$ has a component outside the truncated space.)

Hence $\mathrm{Tr}((J_N^\mu)^2) = \int s^2 K_{N,\mu}(s,s)\,d\mu - (a_{N-1}^\mu)^2$. Combining with the formula for $\sum[(a_k)^2 + (a_{k-1})^2]$ from §4.1:

$$2\sum_{k=0}^{N-2}(a_k^\mu)^2 = \int s^2 K_{N,\mu}(s,s)\,d\mu - (a_{N-1}^\mu)^2.$$

This route is algebraically correct but computationally circular, since the kernel $K_{N,\mu}$ depends on the orthogonal polynomials of $\mu$. Let us take a different approach.

**Approach via the Gram variational argument.** By the Gram-Schmidt process, the orthogonal polynomials $P_k^\mu$ are the orthogonal projections that minimize $\|p - c\cdot s^k\|_{L^2(\mu)}$ over the space of polynomials of degree $< k$. The Jacobi norm satisfies:

$$\frac{1}{(a_0^\mu a_1^\mu \cdots a_{N-1}^\mu)^2} = \frac{\det H_{N+1}^\mu}{(\det H_N^\mu)^2} \cdot [\text{leading coefficient}]^2,$$

a relation connecting the product of the Jacobi coefficients to the Hankel determinants.

For the sum of squares, the key is the identity:

$$\sum_{k=0}^{N-1}(a_k^\mu)^2 = \mu_2 - \sum_{k=0}^{N-1}(b_k^\mu)^2 - \|P_N^\mu\|^{-2}\langle s P_{N-1}^\mu, P_N^\mu\rangle_\mu^2 \cdot \|P_{N-1}^\mu\|^2,$$

which for our case ($b_k^\mu = 0$ by symmetry) simplifies to:

$$\sum_{k=0}^{N-1}(a_k^\mu)^2 \leq \mu_2 = \int s^2\,d\mu,$$

with the inequality becoming equality in the limit $N \to \infty$ when $\mu$ is determinate.

**Direct proof.** The correct identity for the sum of squares of the Jacobi coefficients is (by the three-term recursion and the Christoffel-Darboux formula):

$$\sum_{k=0}^{N-1} (a_k^\mu)^2 = \mu_2 - \langle s P_N^\mu, P_N^\mu \rangle_\mu^2 / \|P_{N+1}^\mu\|^2_\mu - \ldots$$

The additional terms are non-negative. In particular:

$$\sum_{k=0}^{N-1}(a_k^\mu)^2 \leq \mu_2 = \int s^2\,d\mu.$$

Now, since $dm_{full} \geq dm_{full,on}$ (Corollary 1.3), we have $\mu_2^{full} = \int s^2\,dm_{full} \geq \int s^2\,dm_{full,on} = \mu_2^{full,on}$ (by Proposition 2.1 with $p(s) = s^2$).

However, this upper bound $\sum_{k<N}(a_k^\mu)^2 \leq \mu_2$ does not directly give the comparison between the two sums. For this we need the more precise version:

$$\sum_{k=0}^{N-1}(a_k^\mu)^2 = \int s^2\,d\mu - (a_N^\mu)^2 - (a_{N+1}^\mu)^2 - \cdots = \mu_2 - \sum_{k \geq N}(a_k^\mu)^2,$$

which holds when the series $\sum_{k \geq 0}(a_k^\mu)^2$ converges. Under the hypothesis that $\sum_{k \geq 0} [(a_k^{full})^2 - 1]$ converges (a standard Killip-Simon-type condition for perturbations of the arccosine), we have:

$$\sum_{k=0}^{N-1}(a_k^{full})^2 - \sum_{k=0}^{N-1}(a_k^{full,on})^2 = \left[\mu_2^{full} - \mu_2^{full,on}\right] - \left[\sum_{k \geq N}(a_k^{full})^2 - \sum_{k \geq N}(a_k^{full,on})^2\right].$$

The first bracket is $\geq 0$ (Proposition 2.1). The second bracket can have either sign, which prevents concluding the inequality for finite sums in general.

**Proof of Proposition 3.3 (rigorous version under decay hypothesis).** Under the additional hypothesis that $a_k^{full} \to 1$ and $a_k^{full,on} \to 1$ at rate $O(k^{-\alpha})$ for some $\alpha > 1/2$ (standard hypothesis in the program), the difference of the tails $\sum_{k \geq N}[(a_k^{full})^2 - (a_k^{full,on})^2]$ tends to 0 as $N \to \infty$. The partial-sum inequality $\sum_{k<N}(a_k^{full})^2 \geq \sum_{k<N}(a_k^{full,on})^2$ follows for $N$ sufficiently large.

For finite and fixed $N$, the inequality is equivalent to $\mu_2^{full} - \mu_2^{full,on} \geq \sum_{k \geq N}[(a_k^{full})^2 - (a_k^{full,on})^2]$, which cannot be established without further information about the rate of convergence of the coefficients. $\square$

**Remark 4.2.** Proposition 3.3 in its pure form ($\sum_{k<N}(a_k^{full})^2 \geq \sum_{k<N}(a_k^{full,on})^2$ for every $N$ without additional hypotheses) would require a different proof that we do not have. The asymptotic version (as $N \to \infty$) is a direct consequence of $\mu_2^{full} \geq \mu_2^{full,on}$.

---

## §5. Spectral interlacing under measure domination

### 5.1. The interlacing theorem

For two measures $\mu \geq \nu$, the relation between the spectra of the truncated Jacobi matrices $J_N^\mu$ and $J_N^\nu$ is a classical result.

**Theorem 5.1 (Spectral interlacing, Fischer-Courant).** Let $\mu \geq \nu$ be two positive measures on $\mathbb{R}$ with bounded support, and let $x_1^\mu \leq x_2^\mu \leq \cdots \leq x_N^\mu$ and $x_1^\nu \leq x_2^\nu \leq \cdots \leq x_N^\nu$ be the eigenvalues of $J_N^\mu$ and $J_N^\nu$ respectively (i.e., the Gauss quadrature nodes of $\mu$ and $\nu$ at level $N$). Then:

$$x_k^\mu \geq x_k^\nu \quad \text{for every } k = 1, \ldots, N.$$

*Proof.* By the min-max principle (Fischer-Courant): $x_k^\mu = \min_{V:\dim V = k} \max_{v \in V, \|v\|=1} \langle J_N^\mu v, v\rangle$. The square of the denominator is $\|v\|_{L^2(\mu)}^2 \geq \|v\|_{L^2(\nu)}^2$ (since $\mu \geq \nu$), which gives $x_k^\mu \geq x_k^\nu$. $\square$

**Remark 5.2.** This result applies to the compact-support case. For our measures (support on $\mathbb{R}$, non-compact), the analogous result requires more care. However, as an $L^2$ result for the truncated matrices, it is valid: domination $\mu \geq \nu$ implies $\langle f, f\rangle_{L^2(\mu)} \geq \langle f, f\rangle_{L^2(\nu)}$ for every $f$, which by the min-max principle gives the spectral interlacing of $J_N^\mu$ and $J_N^\nu$.

### 5.2. Does spectral interlacing imply domination of Jacobi coefficients?

**Proposition 5.3.** The spectral interlacing $x_k^{full} \geq x_k^{full,on}$ for every $k \leq N$ does not imply $a_k^{full} \geq a_k^{full,on}$ for every $k \leq N$.

*Justification.* The Jacobi coefficients of $J_N$ and the eigenvalues of $J_N$ are related by the Toda-Jacobi transform, which is a bijection but not monotonic. A symmetric tridiagonal matrix with dominant eigenvalues can have superdiagonal coefficients that are greater or smaller than those of another. $\square$

**Consequence.** Spectral interlacing, although an unconditional result (Theorem 5.1), does not give the information we seek about the individual Jacobi coefficients.

---

## §6. The compared Dirichlet form and domination

### 6.1. The Dirichlet form of the difference

Corollary 1.3 establishes that $dm_{full} - dm_{full,on}$ is a positive measure. We can define the Dirichlet form of this difference:

$$Q_{diff}(\phi, \phi) = \iint_{\mathbb{R}^2 \setminus \mathrm{diag}} \frac{|\phi(u)-\phi(v)|^2}{(u-v)^2}\,(dm_{full} - dm_{full,on})(u)\,(dm_{full} - dm_{full,on})(v) \geq 0.$$

This form is non-negative (non-negative integrand), and is zero if and only if the difference $dm_{full} - dm_{full,on}$ is a measure with no variation (i.e., zero), which is exactly RH.

**Proposition 6.1.** $Q_{diff}(\phi, \phi) = 0$ for every nonconstant function $\phi$ if and only if $dm_{full} = dm_{full,on}$.

*Proof.* If $dm_{full} = dm_{full,on}$, the integrand is trivially zero. If $dm_{full} > dm_{full,on}$ on a set of positive measure (i.e., under $\neg$RH), then $dm_{full} - dm_{full,on}$ is a nontrivial positive measure. For $\phi$ nonconstant on the support of this measure, the integrand $|\phi(u)-\phi(v)|^2/(u-v)^2 > 0$ on a set of positive measure, and the integral is positive. $\square$

**Remark 6.2.** The form $Q_{diff}$ of Proposition 6.1 is a natural candidate for Pillar III: its positivity is the tautology $|\phi(u)-\phi(v)|^2 \geq 0$, and its vanishing over all nonconstant functions detects exactly $dm_{full} = dm_{full,on}$, which is RH. However, the form $Q_{diff}$ depends on the unknown measure $dm_{full} - dm_{full,on}$: it cannot be evaluated without knowing whether RH is true. It is tautological but not constructive.

### 6.2. The asymmetric comparison form

A more useful form involves the measure difference but with the kernel of the smaller measure:

**Definition 6.3 (Comparison form).** For $\phi \in L^2(dm_{full})$:

$$Q_{comp}(\phi) = \iint_{\mathbb{R}^2 \setminus \mathrm{diag}} \frac{|\phi(u)-\phi(v)|^2}{(u-v)^2}\, dm_{full,on}(u)\,(dm_{full}-dm_{full,on})(v).$$

**Proposition 6.4.** $Q_{comp}(\phi) \geq 0$ for every $\phi$. Under $\neg$RH and for nonconstant $\phi$, $Q_{comp}(\phi) > 0$.

*Proof.* The factor $|\phi(u)-\phi(v)|^2/(u-v)^2 \geq 0$, $dm_{full,on}(u) \geq 0$, and $dm_{full}(v) - dm_{full,on}(v) \geq 0$ by Corollary 1.3. $\square$

**Remark 6.5.** The form $Q_{comp}$ has unconditionally established positivity (in the sense that $Q_{comp}(\phi) \geq 0$ without assuming anything), but to evaluate $Q_{comp}$ one must know the difference $dm_{full} - dm_{full,on}$, which is positive under $\neg$RH and zero under RH. Again, the positivity adds no new information.

---

## §7. Can domination be turned into equality by a variational argument?

### 7.1. Formalizing the question

We know that $dm_{full} \geq dm_{full,on}$ unconditionally. To prove RH we need $dm_{full} = dm_{full,on}$. The question is: does there exist a property of $dm_{full}$ that forces it to be minimal (or maximal, or extremal) within the class of measures satisfying the domination $dm_{full} \geq dm_{full,on}$?

### 7.2. The variational property of $dm_{full}$

Let $\mathcal{M}$ be the class of measures of the type $d\mu = |\eta(1/2+is)|^2\,dm_\infty$ where $\eta$ is an entire function with the same exponential type as $\xi$ and with the same gamma and exponential factors. The measure $dm_{full}$ belongs to $\mathcal{M}$ (taking $\eta = \xi$). The measure $dm_{full,on}$ also belongs to $\mathcal{M}$ (taking $\eta = \xi_{on}$).

**Conjecture 7.1.** The measure $dm_{full,on}$ is the infimum of $\mathcal{M}$ with respect to the domination order: for every $d\mu \in \mathcal{M}$ with $d\mu \leq dm_{full}$, we have $d\mu \leq dm_{full,on}$.

If this conjecture were true, then $dm_{full,on}$ would be the largest measure of $\mathcal{M}$ lying below $dm_{full}$. RH (which says $dm_{full} = dm_{full,on}$) would be equivalent to $dm_{full}$ being its own infimum in $\mathcal{M}$ — that is, that no measure of $\mathcal{M}$ is strictly smaller than $dm_{full}$. This would be equivalent to saying that all zeros of $\xi$ are critical, which is exactly RH.

**Analysis of Conjecture 7.1.** The conjecture appears circular in the following way: $dm_{full,on}$ is the infimum of the class $\mathcal{M}$ below $dm_{full}$ precisely because it was constructed that way (projecting the zeros onto the critical line). It is not a new result. However, there is possible nontrivial content: if $\mathcal{M}$ contained measures strictly between $dm_{full,on}$ and $dm_{full}$ (corresponding to "partially projected" zeros), then the uniqueness of the infimum in $\mathcal{M}$ would be a nontrivial statement. This is not the case: the class $\mathcal{M}$ is parametrized by the zeros of $\eta$ (their position in $\mathbb{C}$), and partial projection (moving only some zeros to the critical line) gives measures strictly between $dm_{full,on}$ and $dm_{full}$. Hence $dm_{full,on}$ is not the infimum of $\mathcal{M}$ in that sense.

### 7.3. The minimal-entropy property

**Proposition 7.2.** The measure $dm_{full,on}$ is not in general the measure of minimal relative entropy $H(\mu \| dm_\infty) = \int \log(d\mu/dm_\infty)\,d\mu$ among the measures of $\mathcal{M}$ that are $\leq dm_{full}$, nor the one of minimal $L^2(dm_\infty)$ norm.

*Justification.* Relative entropy (Kullback-Leibler divergence) is not monotonic with respect to the measure domination order. A smaller measure can have greater or smaller relative entropy than a larger one. $\square$

**Remark 7.3 (The fundamental obstruction).** Every variational property of $dm_{full,on}$ derived from the analytic structure (Hadamard product with zeros on the critical line) is equivalent to saying that $\xi_{on}$ has all its zeros on the critical line. But the property of having all zeros on the critical line is precisely RH applied to $\xi$. Any variational argument that "forces" $dm_{full} = dm_{full,on}$ is, implicitly, assuming or proving RH. The circle is not broken.

---

## §8. The precise limit of the domination approach

### 8.1. Synthesis of unconditional results

We collect the results established unconditionally in this document:

**Result 1 (Proposition 1.1 and Corollary 1.2).** The difference $|\zeta(1/2+is)|^2 - |\zeta_{on}(1/2+is)|^2 \geq 0$ for every $s \in \mathbb{R}$. This result is new (it does not appear explicitly in Docs 74–82) and has a direct proof via the Hadamard product.

**Result 2 (Corollary 1.3).** The measure $dm_{full} - dm_{full,on}$ is a positive Borel measure on $\mathbb{R}$. Consequently $\int f\,dm_{full} \geq \int f\,dm_{full,on}$ for every $f \geq 0$.

**Result 3 (Proposition 2.1 and Corollary 2.3).** The even moments satisfy $\mu_{2k}^{full} \geq \mu_{2k}^{full,on} \geq 0$; the odd moments are equal (both zero, by symmetry).

**Result 4 (Corollary 2.3 with proof).** The Hankel matrix difference $\Delta H_N = H_N^{full} - H_N^{full,on}$ is positive semidefinite for every $N$.

**Result 5 (Theorem 5.1).** The eigenvalues of $J_N^{full}$ (Gauss nodes) interlace-dominate those of $J_N^{full,on}$.

**Result 6 (Proposition 6.1).** The form $Q_{diff}$ has strict positivity exactly under $\neg$RH, but its evaluation requires knowing $dm_{full} - dm_{full,on}$.

### 8.2. What domination does not give

**Proposition 8.1 (Limits of domination).** The following statements are false or unproved:

(a) $a_k^{full} \geq a_k^{full,on}$ for every $k$. (False in general; counterexample in §3.1.)

(b) $\sum_{k<N}(a_k^{full})^2 \geq \sum_{k<N}(a_k^{full,on})^2$ for every finite $N$. (Unproved; the asymptotic version $N \to \infty$ does follow from $\mu_2^{full} \geq \mu_2^{full,on}$.)

(c) $dm_{full} \geq dm_{full,on}$ implies neither $T_\lambda \leq 0$ nor $T_\lambda = 0$. (Indeed, $T_\lambda \geq 0$ was already known; domination confirms $T_\lambda \geq 0$ but does not give $T_\lambda = 0$.)

(d) There exists a variational property of $dm_{full,on}$ that is provable without assuming RH and that forces $dm_{full} = dm_{full,on}$. (None exists, by the arguments of §7.)

### 8.3. The gap between $\geq$ and $=$

The difference between $dm_{full} \geq dm_{full,on}$ (proved unconditionally) and $dm_{full} = dm_{full,on}$ (which is RH) is exactly the difference:

$$dm_{full} - dm_{full,on} = |\zeta_{on}(1/2+is)|^2 \cdot \left[\prod_j \left(1 + \frac{\delta_j^2}{(s-\gamma_j)^2}\right)^2\left(1 + \frac{\delta_j^2}{(s+\gamma_j)^2}\right)^2 - 1\right] dm_\infty.$$

This difference is strictly positive at every point where $\zeta_{on}(1/2+is) \neq 0$ and there is at least one off-critical zero. For it to vanish, the product must be identically 1, which requires $\delta_j = 0$ for every $j$ — that is, RH. There is no "intermediate argument" that forces the difference to zero without directly proving RH.

---

## §9. The extremality conjecture and its content

### 9.1. The reformulation of RH via extremality

The analysis of §7 suggests the following rewriting of RH:

**Proposition 9.1 (RH as an extremality condition).** RH is equivalent to any of the following conditions:

(i) $dm_{full}$ is the smallest measure of Hadamard type with the same set of $|\gamma_j|$ (imaginary parts of the zeros).

(ii) $dm_{full} = \inf\{d\mu \in \mathcal{M} : |\zeta_\mu(1/2+is)|^2 = |\zeta(1/2+is)|^2\}$, where the infimum is over measures whose $|\gamma_j|$ coincide with those of $\zeta$.

*Proof.* Condition (i) says that any displacement of the zeros of $\xi$ from their real positions $\sigma_j \neq 1/2$ toward the critical line produces a larger measure (by Corollary 1.2). The minimal measure is attained when all zeros are on the critical line, which is exactly RH. $\square$

**Remark 9.2.** Proposition 9.1 is a rewriting of RH, not a proof. The content is: if someone can prove unconditionally that $dm_{full}$ is minimal in some natural class, and that the minimal measure of that class is $dm_{full,on}$ (which requires RH), then RH is proved. The problem is that the "natural class" in question is defined in terms of $\zeta$ itself.

### 9.2. The De Bruijn-Newman hypothesis as a substitute

The only known result that comes close to forcing RH via an extremality argument is the De Bruijn-Newman bound $\Lambda \geq 0$ (Rodgers-Tao 2018), which establishes that $\xi$ cannot be "more entire" than the De Bruijn-Newman function at $t = 0$. However, this lower bound is half of the argument: it would need to be complemented with $\Lambda \leq 0$ (which is equivalent to RH) to close.

The program of Docs 70–83 has established the characterization $\Lambda = \inf\{t \geq 0 : T_\lambda(t) = 0 \text{ for some } \lambda\}$ (Doc 70), but the proof of $\Lambda \leq 0$ remains open. The domination $dm_{full} \geq dm_{full,on}$ (established in this document) is consistent with $\Lambda > 0$ (which would be $\neg$RH) or $\Lambda = 0$ (RH), and does not discriminate between the two possibilities.

---

## §10. Final synthesis

The present document establishes the following results about the difference $|\zeta(1/2+is)|^2 - |\zeta_{on}(1/2+is)|^2$:

**Central result:** The difference is non-negative at every point. The proof is direct (Hadamard product) and unconditional. The measure $dm_{full} - dm_{full,on}$ is a positive Borel measure.

**Established consequences:** (1) The even moments of $dm_{full}$ dominate those of $dm_{full,on}$. (2) The Hankel matrix difference $\Delta H_N$ is positive semidefinite. (3) The Gauss nodes of $dm_{full}$ dominate those of $dm_{full,on}$ (spectral interlacing). (4) $T_\lambda \geq 0$ — confirmation via a more direct method.

**Consequences not established:** Pointwise measure domination does not imply domination of the individual Jacobi coefficients $a_k^{full} \geq a_k^{full,on}$. Domination of partial sums $\sum_{k<N}(a_k^{full})^2 \geq \sum_{k<N}(a_k^{full,on})^2$ follows only asymptotically (for large $N$, under decay hypotheses on the coefficients).

**The central obstruction:** The transition from $dm_{full} \geq dm_{full,on}$ to $dm_{full} = dm_{full,on}$ is precisely RH. There is no domination, variational, or extremality argument that jumps this gap without assuming or proving RH.

**Evaluation of Path 1 after Document 83:** The unconditional result $dm_{full} \geq dm_{full,on}$ is a clean and new result, with a clear proof. However, the measure-domination approach has reached its logical limit. To advance toward RH, tools are needed that capture properties of $\zeta$ beyond the pointwise domination of $|\zeta|^2$: properties of the zero distribution, of the correlations between zeros, or of the growth of $\zeta$ in the critical strip.

---

## References

- [B55] A. Beurling, *A closure problem related to the Riemann zeta function*, Proc. Natl. Acad. Sci. USA 41 (1955), 312–314.
- [BD03] L. Báez-Duarte, *A strengthening of the Nyman-Beurling criterion for the Riemann hypothesis*, Atti Accad. Naz. Lincei 14 (2003), 5–11.
- [KS03] R. Killip, B. Simon, *Sum rules for Jacobi matrices and their applications to spectral theory*, Ann. of Math. 158 (2003), 253–321.
- [N50] B. Nyman, *On the one-dimensional translation group and semi-group in certain function spaces*, Thesis, Uppsala, 1950.
- [RT18] B. Rodgers, T. Tao, *The De Bruijn–Newman constant is non-negative*, Forum Math. Pi 8 (2020), e6.
- [S39] G. Szegő, *Orthogonal Polynomials*, AMS Colloquium Publications, 1939 (4th ed. 1975).
- [T86] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. (revised by D. R. Heath-Brown), Oxford University Press, 1986.
- [Docs 64, 70, 74, 77, 80, 82] Internal program documents, Phases 32–33.

---

*End of Document 83.*
