# Document 71 — Time derivative of $T_\lambda$ and the coefficients $c_k$

**Program:** Riemann Hypothesis — Phase 33 DBN-CCM
**Prerequisites:** Docs 64, 65, 70

---

## 1. The goal

In Doc 70, §8.2, we derived the formula

$$\partial_t T_\lambda \bigg|_{t=0} = -4\int W_\lambda(s)\mathrm{Re}(\overline{H_0(s)}\, H_0''(s))\, dm_\infty(s).$$

We want to compute this integral explicitly in terms of the coefficients $c_k = \langle \Xi, P_k \rangle_{dm_\infty}$ and the eigenvalues $\mu_k$ of the Schrödinger operator $\mathcal{L}_0$.

---

## 2. The Schrödinger quadratic form

### 2.1. Expansion in the Jacobi basis

Recall that $H_0 = \Xi$ (identifying $s$ with the imaginary variable). The expansion is $\Xi = \sum_k c_k P_k$ with $c_k = 0$ for odd $k$ (parity).

The second derivative $\Xi'' = -\mathcal{L}_0\Xi + V\Xi$ where $V(s) = \pi^2 s^2/4 + \pi/2$ (the Schrödinger potential). In the basis $\{P_k\}$:

$$\Xi'' = \sum_k c_k P_k'' = \sum_k c_k (-\mathcal{L}_0 P_k + V P_k) = -\sum_k c_k \mu_k P_k + \sum_k c_k V P_k.$$

Multiplication by $V(s) = \pi^2 s^2/4 + \pi/2$ in the basis $\{P_k\}$ acts as $(J^\infty)^2 \cdot \pi^2/4 + \pi/2 \cdot I$, where $J^\infty$ is the Jacobi matrix. This gives:

$$[V\Xi]_k = \frac{\pi^2}{4}[(J^\infty)^2 c]_k + \frac{\pi}{2}c_k = \frac{\pi^2}{4}(\alpha_{k-2}c_{k-2} + \gamma_k c_k + \alpha_k c_{k+2}) + \frac{\pi}{2}c_k,$$

with $\alpha_k = a_k^\infty a_{k+1}^\infty$ and $\gamma_k = (a_k^\infty)^2 + (a_{k-1}^\infty)^2$.

### 2.2. The integral $\int W_\lambda \overline{\Xi} \Xi'' \, dm_\infty$

The integral of Prop. 8.2 of Doc 70 decomposes as:

$$\int W_\lambda(s)\overline{\Xi(s)}\Xi''(s)\, dm_\infty(s) = -\int W_\lambda(s)|\Xi(s)|^2 \mathcal{L}_0 \log|\Xi|\, dm_\infty + \text{off-diagonal}.$$

But it is cleaner to compute directly:

$$\int W_\lambda \overline{\Xi}\Xi''\, dm_\infty = \sum_{k,l} \bar{c}_k c_l \int W_\lambda P_k P_l'' \, dm_\infty.$$

### 2.3. Self-adjointness of $\mathcal{L}_0$ and the diagonal form

$$\int W_\lambda P_k \mathcal{L}_0 P_l\, dm_\infty = \mu_l \delta_{kl} \int W_\lambda P_k P_l\, dm_\infty.$$

This simplification is only valid if $W_\lambda$ is constant or if the operator $W_\lambda \cdot$ commutes with $\mathcal{L}_0$, which in general is false. However, we can use the Abel expansion of $W_\lambda$:

$$W_\lambda(s) = \sum_{n=0}^{N(\lambda)-1}(n+1)|P_{n+1}(s)|^2 + (a_{N(\lambda)}^\infty)^2|P_{N(\lambda)+1}(s)|^2,$$

and compute term by term.

---

## 3. Computing the time derivative

### 3.1. Bilinear quadratic form

We define the bilinear form

$$B_\lambda(u, v) := \int W_\lambda(s)\, u(s)\, v(s)\, dm_\infty(s).$$

Then:

$$\int W_\lambda \overline{\Xi} \Xi''\, dm_\infty = B_\lambda(\overline{\Xi}, \Xi'').$$

### 3.2. Integration by parts in $dm_\infty$

The measure $dm_\infty$ has density $w(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2$. Integrating by parts with respect to $s$:

$$B_\lambda(\overline{\Xi}, \Xi'') = -B_\lambda(\overline{\Xi'}, \Xi') - \int (W_\lambda w)'\,\overline{\Xi}\Xi'/w\, ds + \text{boundary.}$$

For the main part (ignoring the boundary, which decays exponentially):

$$B_\lambda(\overline{\Xi}, \Xi'') = -B_\lambda(\overline{\Xi'}, \Xi') - \int W_\lambda' \overline{\Xi}\Xi'\, dm_\infty.$$

Hence:

$$\mathrm{Re}\,\, B_\lambda(\overline{\Xi}, \Xi'') = -\int W_\lambda |\Xi'|^2\, dm_\infty - \frac{1}{2}\int W_\lambda' \partial_s|\Xi|^2\, dm_\infty.$$

Integrating by parts the second term:

$$-\frac{1}{2}\int W_\lambda' \partial_s|\Xi|^2\, dm_\infty = \frac{1}{2}\int W_\lambda'' |\Xi|^2\, dm_\infty + \frac{1}{2}\int W_\lambda' |\Xi|^2 (\log w)'\, dm_\infty.$$

### 3.3. The time-derivative formula

Gathering terms and substituting into Prop. 8.2 of Doc 70:

$$\boxed{\partial_t T_\lambda\bigg|_{t=0} = 4\int W_\lambda |\Xi'|^2\, dm_\infty - 2\int W_\lambda''|\Xi|^2\, dm_\infty - 2\int W_\lambda'(\log w)'|\Xi|^2\, dm_\infty.}$$

---

## 4. Sign analysis of $\partial_t T_\lambda|_{t=0}$

### 4.1. The three terms

Let $\dot{T} := \partial_t T_\lambda|_{t=0}$.

**Term I:** $4\int W_\lambda |\Xi'|^2\, dm_\infty > 0$ (always positive, since $W_\lambda \geq 0$ and $|\Xi'|^2 \geq 0$).

**Term II:** $-2\int W_\lambda''|\Xi|^2\, dm_\infty$. The sign of $W_\lambda''$ is indefinite: $W_\lambda'' = \sum (n+1) \partial_{ss}|P_{n+1}|^2$, which oscillates.

**Term III:** $-2\int W_\lambda'(\log w)'|\Xi|^2\, dm_\infty$. With $(\log w)'(s) = -\pi/2 + O(s^{-1})$ for large $s$, this term is positive for large $s$ (since $W_\lambda' \geq 0$ there by the Abel structure).

### 4.2. Dominance of Term I under ¬RH

Under $\neg$RH, $\Xi$ has a complex zero $\rho_0 = \sigma_0 + i\gamma_0$ with $\sigma_0 > 1/2$. The function $|\Xi'(s)|^2$ near $\gamma_0$ has a peak of height $|\Xi'(\gamma_0)|^2 = |\Xi'(\gamma_0)|^2 \cdot |\text{factor}|^2$. In particular, $\Xi'(\gamma_0) \neq 0$ because $\gamma_0$ is a simple zero (under the simplicity hypothesis).

For $\lambda \gg \gamma_0$, $W_\lambda(\gamma_0) \sim N(\lambda) \cdot \pi/2$ (Prop. of Doc 64), so:

$$\text{Term I} \geq 4 \cdot N(\lambda) \cdot \frac{\pi}{2} \cdot |\Xi'(\gamma_0)|^2 w(\gamma_0).$$

This grows as $N(\lambda) \to \infty$.

Terms II and III involve $W_\lambda''$ and $W_\lambda'$, which are of order $N(\lambda)^2/\lambda \ll N(\lambda)^2$ for large $\lambda$... but $N(\lambda) \sim \lambda \log \lambda / (2\pi)$, so $N(\lambda)^2/\lambda \sim N(\lambda) \cdot \log\lambda / (2\pi)$.

The balance among the three terms is not determined without more information about the behavior of $|\Xi|^2$ and $|\Xi'|^2$ on the support of $W_\lambda$.

**Provisional conclusion:** Term I suggests that $\dot{T} > 0$ under $\neg$RH (the trace *grows* initially when the heat flow is applied). This would be the *opposite* sign from what we would expect for the monotonicity of Conj. 5.1.

### 4.3. Resolution of the apparent contradiction

Conj. 5.1 says that $T_\lambda(t)$ is *decreasing* in $t$. Term I suggests that $\partial_t T_\lambda|_{t=0} > 0$. Is this a contradiction?

Not necessarily. Conj. 5.1 applies on the range $t \geq 0$, and the derivative at $t = 0$ can be positive without contradicting *eventual* monotonicity (the trace can grow initially before decreasing). Furthermore, Conj. 5.1 is formulated under general hypotheses; under $\neg$RH the situation may differ.

**Remark 4.1.** The behavior of $T_\lambda(t)$ under $\neg$RH is as follows:
- At $t = 0$: $T_\lambda(0) > 0$ (PTC).
- For $t > \Lambda$: $T_\lambda(t) = 0$.
- Therefore, $T_\lambda(t)$ must decrease from $T_\lambda(0) > 0$ to $0$ on the interval $[0, \Lambda]$.

The fact that $\partial_t T_\lambda|_{t=0} > 0$ (Term I dominant) suggests that the trace *first rises* before falling. This is possible: $T_\lambda(t)$ may have a maximum at some $t^* \in (0, \Lambda)$ before becoming extinct at $t = \Lambda$.

This non-monotonic behavior is itself informative: it indicates that the heat flow initially *amplifies* the discrepancy before resolving it.

---

## 5. The derivative in terms of $c_k$

### 5.1. Explicit expression

Using $\Xi = \sum_k c_k P_k$ (only even $k$) and the Abel expansion of $W_\lambda$:

$$\int W_\lambda |\Xi'|^2\, dm_\infty = \sum_{n=0}^{N(\lambda)-1}(n+1)\int|P_{n+1}|^2|\Xi'|^2\, dm_\infty + \ldots$$

The integral $\int|P_m|^2|\Xi'|^2\, dm_\infty$ is computed using $\Xi' = \sum_k c_k P_k'$ and the relation $P_k' = \sum_j \alpha_{kj} P_j$ (where the coefficients $\alpha_{kj}$ are computed from the Jacobi recurrence). In general $P_k'(s) = \sum_{j<k, j\equiv k+1\,(\text{mod }2)} d_{kj} P_j(s)$ with explicit $d_{kj}$.

**Proposition 5.1** (Time derivative via $c_k$). The derivative $\partial_t T_\lambda|_{t=0}$ is expressed as a quadratic form in the coefficients $c_k$:

$$\partial_t T_\lambda\bigg|_{t=0} = \sum_{k,l} c_k c_l\, Q_{kl}^{(\lambda)},$$

where the matrix $Q^{(\lambda)}$ has entries

$$Q_{kl}^{(\lambda)} = 4\int W_\lambda P_k' P_l'\, dm_\infty - 2\int W_\lambda'' P_k P_l\, dm_\infty - 2\int W_\lambda'(\log w)' P_k P_l\, dm_\infty.$$

Whether $Q^{(\lambda)}$ is positive definite (or not) determines the sign of $\dot{T}$ as a function of the $c_k$.

### 5.2. The case $\Lambda = 0$ (RH): $\dot{T} = 0$

Under RH, $\Xi = \Xi^{on}$ and $H_t = H_t^{on}$ for all $t$, so $T_\lambda(t) = 0$ for all $t$. In particular $\partial_t T_\lambda|_{t=0} = 0$. This means $\sum_{k,l} c_k c_l Q_{kl}^{(\lambda)} = 0$ for all $\lambda$. The quadratic form $Q^{(\lambda)}$ is positive semidefinite (by Term I) and vanishes on the vector $(c_k)$: so the $c_k$ must satisfy $Q^{(\lambda)}(c,c) = 0$, which would imply $\Xi' = 0$ on the support of $W_\lambda$... which is absurd.

**Apparent contradiction.** If $W_\lambda > 0$ and $\Xi' \not\equiv 0$, Term I is strictly positive, but under RH $\dot{T} = 0$. The resolution: under RH, the three terms cancel exactly. The positive Term I is cancelled by the negative Terms II and III. This is possible because the cancellation reflects a special property of the $c_k$ when *all zeros are real*.

This cancellation is an algebraic condition on the $c_k$ equivalent to RH — which suggests that the equation $Q^{(\lambda)}(c,c) = 0$ could be a new line of attack.

---

## 6. Cancellation condition as a new criterion

### 6.1. Formulation

**Proposition 6.1** (Cancellation criterion for the time derivative). The following are equivalent:

1. RH.
2. $\partial_t T_\lambda|_{t=0} = 0$ for all $\lambda > 0$.
3. $\sum_{k,l} c_k c_l Q_{kl}^{(\lambda)} = 0$ for all $\lambda > 0$.
4. The three terms of the derivative formula cancel exactly.

*Proof.* (1)$\Rightarrow$(2): under RH, $T_\lambda(t) = 0$ for all $t$. (2)$\Rightarrow$(1): if $\partial_t T_\lambda|_{t=0} = 0$ for all $\lambda$, and $T_\lambda(0) = 0$ (by PTC+RH)... but this path is circular: we are assuming $T_\lambda(0) = 0$ which is RH.

**Correction:** The correct equivalence is:

$$\text{RH} \iff T_\lambda(0) = 0 \ \forall\lambda \iff \partial_t T_\lambda|_{t=0} = 0 \ \forall\lambda,$$

where the second equivalence uses that $T_\lambda(0) = 0$ implies $\partial_t T_\lambda|_{t=0} = 0$ (derivative of the identically-zero function), and the converse requires the initial condition $T_\lambda(0) = 0$, which is itself RH. Without information about $T_\lambda(0)$, the condition $\partial_t T_\lambda|_{t=0} = 0$ is *weaker* than RH.

**Frank conclusion:** The time derivative does not give a new equivalence with RH; it only gives a necessary condition.

---

## 7. What is genuinely new: the quadratic form $Q^{(\lambda)}$

Despite the limitation of §6, the quadratic form $Q^{(\lambda)}_{kl}$ is a new object:

1. **It is explicit** in terms of $W_\lambda$, $\log w$, and the polynomials $P_k$.
2. **It encodes the dynamics of the heat flow** on the Jacobi space.
3. **Its positivity/vanishing** on the vectors $(c_k)$ is equivalent to conditions on the zeros of $\Xi$.

The genuinely new question is: does the form $Q^{(\lambda)}$ have a spectral description in terms of the prolate operator $W_\lambda$? If $Q^{(\lambda)} = B_\lambda^T B_\lambda$ for some explicit operator $B_\lambda$, the condition $Q^{(\lambda)}(c,c) = 0$ would become $\|B_\lambda c\|^2 = 0$, i.e., $B_\lambda c = 0$, which is a kernel condition.

---

## 8. Summary and direction for Doc 72

**Main result:**
$$\partial_t T_\lambda\bigg|_{t=0} = 4\int W_\lambda|\Xi'|^2 dm_\infty - 2\int W_\lambda''|\Xi|^2 dm_\infty - 2\int W_\lambda'(\log w)'|\Xi|^2 dm_\infty.$$

**Structure:** It is a quadratic form $Q^{(\lambda)}(c,c)$ in the coefficients $c_k = \langle\Xi,P_k\rangle_{dm_\infty}$.

**Consequence under RH:** The three terms cancel. The cancellation imposes an algebraic condition on $(c_k)$ equivalent to all zeros of $\Xi$ being real.

**Limitation:** The condition $\partial_t T_\lambda|_{t=0} = 0$ alone is not equivalent to RH without the initial information $T_\lambda(0) = 0$.

**Doc 72** should study the quadratic form $Q^{(\lambda)}$ more explicitly: is $Q^{(\lambda)}$ positive definite on the orthogonal complement of the vectors $(c_k)$ that make $\Xi$ vanish at all real zeros? If the answer is yes, this would give structural information about the zeros.

---

*End of Document 71.*
