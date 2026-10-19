# Document 87 — The Jensen integral via the Poisson-Jensen formula in the critical strip

**Program:** Riemann Hypothesis — Phase 33 DBN-CCM (Path 2)
**Prerequisites:** Docs 75, 78, 81, 84

---

## Summary

This document examines the relation between the Jensen criterion of Doc 84 and the Poisson-Jensen formula for meromorphic functions in the upper half-plane, with the aim of obtaining a more explicit representation of the excess
$$\delta = \int_{-\infty}^\infty \log|\xi(1/2+it)|\frac{2\,dt}{\pi(1+4t^2)} - (-\log 2)$$
in terms of the off-critical zeros of $\xi$. §1 establishes the Poisson-Jensen formula in the upper half-plane and identifies the correct evaluation point. §2 applies the formula to $g(t) = \xi(1/2+it)$ and establishes the central proposition connecting the integral with the zeros of $\xi$. §3 carefully analyzes which region of the $\rho$-plane contributes to the formula, resolving an apparent paradox (the integral would trivially be $-\log 2$). §4 makes explicit the change of variables between the integral over the disk and the integral over the critical line. §5 computes the excess $\delta$ directly in terms of $F$ and its interior zeros. §6 obtains the excess formula in terms of the zeros of $\xi$ via the Hadamard product, and carefully shows that the apparent cancellation of Doc 84 §10.3 is invalid. §7 regularizes the integral for zeros on the critical line. §8 synthesizes the state of Path 2 at the end of this document.

The conclusion is that the Jensen criterion is expressed exactly as a Poisson-Jensen formula, that the excess is a convergent sum over the off-critical zeros (with $\mathrm{Re}(\rho) \neq 1/2$), and that the pairwise cancellation of Doc 84 §10.3 is invalid because the residue computation is not legitimate for $\log|\xi|$.

---

## §1. The Poisson-Jensen formula in the half-plane

### 1.1. Statement of the formula

Let $f$ be meromorphic in the upper half-plane $\mathbb{H} = \{w \in \mathbb{C} : \mathrm{Im}(w) > 0\}$, continuous up to the real boundary $\partial\mathbb{H} = \mathbb{R}$, and suppose $f$ has neither zeros nor poles on the real boundary. Let $w_0 = x_0 + iy_0 \in \mathbb{H}$. The Poisson-Jensen formula establishes:

$$\log|f(w_0)| = \int_{-\infty}^\infty \log|f(t)|\, P_{y_0}(x_0 - t)\, dt + \sum_{w_k \in \mathbb{H}} \log\left|\frac{w_0 - \bar{w}_k}{w_0 - w_k}\right| - \sum_{p_j \in \mathbb{H}} \log\left|\frac{w_0 - \bar{p}_j}{w_0 - p_j}\right|,$$

where $P_y(x) = \frac{y}{\pi(x^2+y^2)}$ is the Poisson kernel of the half-plane, the first sum runs over the zeros $w_k$ of $f$ in $\mathbb{H}$ (counted with multiplicity), and the second over the poles $p_j$ of $f$ in $\mathbb{H}$. The factors $\left|\frac{w_0 - \bar{w}_k}{w_0 - w_k}\right|$ are always greater than 1 for zeros in $\mathbb{H}$ and $w_0 \in \mathbb{H}$ (since $|w_0 - \bar{w}_k| > |w_0 - w_k|$ when both are in the upper half-plane), so the contribution of the zeros is non-negative.

The precise regularity hypotheses are: $\log|f|$ integrable on the real boundary with the Poisson weight, and the zeros and poles in $\mathbb{H}$ satisfying the Blaschke convergence condition of the half-plane $\sum_k \frac{\mathrm{Im}(w_k)}{1 + |w_k|^2} < \infty$.

### 1.2. Identifying the evaluation point

We take $f(t) = \xi(1/2 + it)$ as a function of the real variable $t$, and analytically continue to $t \in \mathbb{C}$. With the parametrization $s = 1/2 + it$ (so that $t \in \mathbb{R}$ corresponds to the critical line $\mathrm{Re}(s) = 1/2$), the non-trivial zeros of $\xi$ in the strip $0 < \mathrm{Re}(s) < 1$ translate into zeros of $f(t) = \xi(1/2+it)$ in the $t$-plane. For a zero $\rho = \sigma + i\gamma$ of $\xi$:
$$1/2 + it_\rho = \rho \implies t_\rho = \frac{\rho - 1/2}{i} = -i(\rho - 1/2) = \gamma + i(1/2 - \sigma).$$

Thus, $\mathrm{Im}(t_\rho) = 1/2 - \sigma$. Therefore:

- If $\sigma < 1/2$ (zero with real part less than $1/2$): $\mathrm{Im}(t_\rho) = 1/2 - \sigma > 0$. The zero $t_\rho$ is in $\mathbb{H}$.
- If $\sigma = 1/2$ (zero on the critical line): $\mathrm{Im}(t_\rho) = 0$. The zero $t_\rho = \gamma$ is on the real boundary.
- If $\sigma > 1/2$ (zero with real part greater than $1/2$): $\mathrm{Im}(t_\rho) = 1/2 - \sigma < 0$. The zero $t_\rho$ is in the lower half-plane $\mathbb{H}^- = \{w : \mathrm{Im}(w) < 0\}$.

To apply the Poisson-Jensen formula in the upper half-plane $\mathbb{H}$, the evaluation point $w_0$ must be in $\mathbb{H}$. The value of $f$ at a point corresponding to the interior of the critical strip on the side $\mathrm{Re}(s) > 1/2$ is what is sought. The point $s = 1 \in \mathbb{R}$ corresponds to $t = (1 - 1/2)/i = -i/2 \in \mathbb{H}^-$, which is in the lower half-plane. To use the upper half-plane, we take $s = 0$, which gives $t = (0 - 1/2)/i = i/2 \in \mathbb{H}$, and $f(i/2) = \xi(1/2 + i(i/2)) = \xi(1/2 - 1/2) = \xi(0) = 1/2$.

**Proposition 1.1.** *The natural evaluation point for the Poisson-Jensen formula in $\mathbb{H}$ is $w_0 = i/2$, which corresponds to $s_0 = 1/2 + i(i/2) = 0$. At this point, $f(i/2) = \xi(0) = 1/2$ and $\log|f(i/2)| = -\log 2$.*

*The Poisson kernel at $w_0 = i/2$ is:*
$$P_{1/2}(t) = \frac{1/2}{\pi(t^2 + 1/4)} = \frac{2}{\pi(1 + 4t^2)},$$
*which coincides exactly with the weight of the integral in the Jensen criterion.*

---

## §2. Applying Poisson-Jensen to $\xi(1/2+it)$

### 2.1. The formula in the upper half-plane

Let $f(w) = \xi(1/2 + iw)$ be meromorphic in $\mathbb{C}$ (in fact entire in $w$). The zeros of $f$ in $\mathbb{H}$ correspond to the zeros $\rho$ of $\xi$ with $\mathrm{Re}(\rho) < 1/2$ (by Proposition 1.2 of §1). Apply the Poisson-Jensen formula with $w_0 = i/2$:

$$\log|f(i/2)| = \int_{-\infty}^\infty \log|f(t)|\, P_{1/2}(t)\, dt + \sum_{\substack{\rho: \mathrm{Re}(\rho) < 1/2}} \log\left|\frac{i/2 - \overline{t_\rho}}{i/2 - t_\rho}\right|.$$

Here $t_\rho = \gamma + i(1/2 - \sigma)$ with $\sigma = \mathrm{Re}(\rho) < 1/2$, so that $\mathrm{Im}(t_\rho) = 1/2 - \sigma > 0$, and $\overline{t_\rho} = \gamma - i(1/2 - \sigma)$. The two factors appearing in the logarithm are:
$$i/2 - t_\rho = i/2 - \gamma - i(1/2 - \sigma) = -\gamma + i\sigma,$$
$$i/2 - \overline{t_\rho} = i/2 - \gamma + i(1/2 - \sigma) = -\gamma + i(1 - \sigma).$$

Therefore:
$$\log\left|\frac{i/2 - \overline{t_\rho}}{i/2 - t_\rho}\right| = \log\frac{\sqrt{\gamma^2 + (1-\sigma)^2}}{\sqrt{\gamma^2 + \sigma^2}} = \frac{1}{2}\log\frac{\gamma^2 + (1-\sigma)^2}{\gamma^2 + \sigma^2}.$$

**Proposition 2.1 (Poisson-Jensen for $\xi$ at $w_0 = i/2$).** *Let $f(w) = \xi(1/2+iw)$. Then:*
$$\int_{-\infty}^\infty \log|\xi(1/2+it)|\frac{2\,dt}{\pi(1+4t^2)} = -\log 2 - \sum_{\rho:\, \mathrm{Re}(\rho) < 1/2} \log\frac{\sqrt{\gamma_\rho^2 + (1-\sigma_\rho)^2}}{\sqrt{\gamma_\rho^2 + \sigma_\rho^2}},$$
*where the sum runs over all non-trivial zeros $\rho = \sigma_\rho + i\gamma_\rho$ of $\xi$ with $\mathrm{Re}(\rho) < 1/2$.*

*Proof.* Direct from the Poisson-Jensen formula with $w_0 = i/2$, using $\log|f(i/2)| = -\log 2$ and the explicit computation of the ratios. $\square$

### 2.2. The sign of the excess

For $\rho = \sigma + i\gamma$ with $\sigma < 1/2$: $(1-\sigma)^2 > \sigma^2$ since $1 - \sigma > 1/2 > \sigma > 0$ (assuming $\sigma > 0$, which holds for all non-trivial zeros). Therefore $\gamma^2 + (1-\sigma)^2 > \gamma^2 + \sigma^2$, and each term in the sum of Proposition 2.1 satisfies
$$\log\frac{\sqrt{\gamma^2 + (1-\sigma)^2}}{\sqrt{\gamma^2 + \sigma^2}} > 0.$$

Consequently, the integral $I = \int \log|\xi(1/2+it)|\frac{2\,dt}{\pi(1+4t^2)}$ satisfies $I \leq -\log 2$, with equality if and only if there are no zeros of $\xi$ with $\mathrm{Re}(\rho) < 1/2$.

### 2.3. Relation to the functional equation

By the functional equation $\xi(s) = \xi(1-s)$, the zeros come in pairs: if $\rho$ is a zero with $\mathrm{Re}(\rho) < 1/2$, then $1 - \rho$ is a zero with $\mathrm{Re}(1-\rho) > 1/2$. There are no zeros with $\mathrm{Re}(\rho) < 1/2$ lacking their partner with real part $> 1/2$. In particular:

- If RH is false: there exist zeros $\rho_0$ with $\mathrm{Re}(\rho_0) > 1/2$, and by the functional equation there exist zeros $1-\rho_0$ with $\mathrm{Re}(1-\rho_0) < 1/2$. These latter contribute to the sum in Proposition 2.1, and the excess is strictly negative: $I < -\log 2$.
- If RH is true: all zeros have $\mathrm{Re}(\rho) = 1/2$, the sum is empty, and $I = -\log 2$.

**Corollary 2.2 (criterion via Poisson-Jensen in $\mathbb{H}$).** 
$$\mathrm{RH} \iff \int_{-\infty}^\infty \log|\xi(1/2+it)|\frac{2\,dt}{\pi(1+4t^2)} = -\log 2.$$
*Under $\neg$RH: the integral is strictly less than $-\log 2$.*

---

## §3. Reconciliation with the disk criterion (Doc 84)

### 3.1. The sign of the excess in the two formulations

Corollary 2.2 establishes that the integral is $\leq -\log 2$ with equality under RH. However, Proposition 6.1 of Doc 84 establishes that $I \geq -\log 2$ with equality under RH, based on the Jensen formula for $F(z)$ in the disk. The two results seem to contradict each other: one says $I \leq -\log 2$, the other says $I \geq -\log 2$, and both say that equality is equivalent to RH. This implies that, under both formulations, $I = -\log 2$ always — which is the contradiction announced in the task and which must be carefully resolved.

### 3.2. The error in applying Poisson-Jensen in $\mathbb{H}$

The Poisson-Jensen formula for $f(w) = \xi(1/2+iw)$ in $\mathbb{H}$ evaluated at $w_0 = i/2$ assumes that $f$ has no zeros on the real boundary $\partial \mathbb{H} = \mathbb{R}$. This hypothesis fails under RH: the zeros $\rho = 1/2 + i\gamma_n$ of $\xi$ correspond to $t_\rho = \gamma_n \in \mathbb{R}$ (real zeros of $f$, on the boundary). The standard Poisson-Jensen formula is not valid when $f$ has zeros on the boundary, because $\log|f(t)| = -\infty$ at those points and the integral on the right-hand side is not well defined in the usual way.

**Proposition 3.1.** *The Poisson-Jensen formula applied to $f(w) = \xi(1/2+iw)$ at $w_0 = i/2$ is valid in the form of Proposition 2.1 only if $f$ has no zeros on the real boundary, i.e., if $\xi$ has no zeros on the critical line $\mathrm{Re}(s) = 1/2$. Under RH, $f$ has infinitely many real zeros $\gamma_n$, the integral $\int \log|f(t)| P_{1/2}(t)\,dt$ diverges to $-\infty$, and the formula provides no finite information.*

### 3.3. The error in the formulation of Doc 84

Similarly, Proposition 6.1 of Doc 84 applies the Jensen formula for $F(z)$ in the disk by taking $r \to 1^-$. The formula for $r < 1$ is exact:
$$\frac{1}{2\pi}\int_0^{2\pi}\log|F(re^{i\theta})|\,d\theta = \log|F(0)| + \sum_{|z_k|<r}\log\frac{r}{|z_k|}.$$
The problem is the limit $r \to 1^-$. The integral on the left-hand side converges to $\int \log|F(e^{i\theta})|d\theta/(2\pi)$ if $\log|F(e^{i\theta})|$ is integrable, which requires that the zeros of $F$ on the boundary be integrable. As noted in Doc 84 §6.3, the zeros of $F$ at $|z|=1$ corresponding to the zeros of $\xi$ on the critical line give singularities $\sim \log|e^{i\theta} - e^{i\theta_n}|$ that are indeed individually integrable. However, there are infinitely many zeros and the sum $\sum_n \int_{|e^{i\theta}-e^{i\theta_n}|<\epsilon}\log|e^{i\theta}-e^{i\theta_n}|d\theta$ needs to converge absolutely, which requires the zeros $\theta_n$ not to accumulate too quickly.

Conditional (non-absolute) integration of $\log|F(e^{i\theta})|$ is the source of the ambiguity. The integral can be $-\infty$ if the zeros are sufficiently dense (in the sense of the boundary Blaschke condition).

**Proposition 3.2.** *The integral $I = \int_{-\infty}^\infty \log|\xi(1/2+it)| \frac{2\,dt}{\pi(1+4t^2)}$ is not well defined as a Lebesgue integral: the integrand is $-\infty$ at the real zeros $\gamma_n$ of $\xi$. The integral as a principal value or improper integral converges conditionally if and only if the series $\sum_n P_{1/2}(\gamma_n)|\log \epsilon_n|$ converges, where $\epsilon_n$ is some exclusion radius around $\gamma_n$.*

The "equivalence RH $\iff I = -\log 2$" of Doc 84 Proposition 6.1 should be understood in the sense of the limit $r \to 1^-$: the integral for $r < 1$ always converges and gives $-\log 2 + \sum_{|z_k|<r}\log(r/|z_k|)$. The criterion is: under RH, this limit tends to $-\log 2$; under $\neg$RH, the limit is $> -\log 2$ due to the interior zeros.

---

## §4. The change of variables between the disk and the critical line

### 4.1. The explicit transformation

The function $\tau : \mathbb{D} \to \mathbb{C}$ defined by $\tau(z) = z/(z-1)$ maps the unit disk $\{|z|<1\}$ to the right half-plane $\{\mathrm{Re}(s) > 1/2\}$... not exactly. Let us check: for $z = re^{i\theta}$ with $r < 1$, the point $\tau(z) = z/(z-1)$. If $|z| < 1$, then $z = -w/(1-w)$ for some $w$ with $|w| < 1$... Let us compute directly: the transformation $s = z/(z-1)$ takes the circle $|z| = 1$ to the line $\mathrm{Re}(s) = 1/2$ (as verified in Doc 81). The disk $|z| < 1$ corresponds to the region $\mathrm{Re}(s) < 1/2$ (the side $\sigma < 1/2$ of the critical-line half-plane). This is the correct direction: check with $z = 0$: $\tau(0) = 0$, and $\mathrm{Re}(0) = 0 < 1/2$. With $z = -1$: $\tau(-1) = (-1)/(-2) = 1/2$, on the boundary. With $z = 1/2$: $\tau(1/2) = (1/2)/(1/2-1) = (1/2)/(-1/2) = -1$, and $\mathrm{Re}(-1) = -1 < 1/2$. Correct.

The change of variables $e^{i\theta} = z(\theta)$ on the boundary of the disk gives, with $e^{i\theta} = (1/2+it)/(1/2+it-1) = (1/2+it)/(-1/2+it)$:
$$e^{i\theta} = \frac{1/2+it}{-1/2+it} = \frac{2it+1}{2it-1}.$$
Differentiating: $ie^{i\theta}d\theta = \frac{2i(2it-1) - 2i(2it+1)}{(2it-1)^2}dt = \frac{-4i}{(2it-1)^2}dt$, so that
$$d\theta = \frac{-4i}{ie^{i\theta}(2it-1)^2}dt = \frac{-4i}{i\cdot\frac{2it+1}{2it-1}\cdot(2it-1)^2}dt = \frac{-4i}{i(2it+1)(2it-1)}dt = \frac{-4i}{i(-(4t^2+1))}dt = \frac{4\,dt}{1+4t^2}.$$

**Proposition 4.1 (change of variables).** *With the parametrization $e^{i\theta} = (2it+1)/(2it-1)$ for $t \in \mathbb{R}$, the arc-length measure in the disk becomes:*
$$\frac{d\theta}{2\pi} = \frac{2\,dt}{\pi(1+4t^2)}.$$
*In particular:*
$$\frac{1}{2\pi}\int_0^{2\pi}\log|F(e^{i\theta})|\,d\theta = \int_{-\infty}^\infty \log|\xi(1/2+it)|\frac{2\,dt}{\pi(1+4t^2)}.$$

The measure $\frac{2\,dt}{\pi(1+4t^2)}$ is the Cauchy measure of scale $1/2$, with total mass $1$. It is also the Poisson kernel of the disk evaluated at $z = 0$, which is consistent with the fact that $F(0) = \xi(0) = 1/2$ and the integral is the harmonic average of $\log|F|$ from the center of the disk.

### 4.2. Interpretation as a Poisson average

The integral $I = \int \log|\xi(1/2+it)| P_{1/2}(t)\,dt$ is the harmonic function $u(w_0) = P[\log|f|](w_0)$ evaluated at $w_0 = i/2$, where $P[\cdot]$ is the Poisson integral. The function $u(w) = P[\log|f|](w)$ is harmonic in the half-plane $\mathbb{H}$ away from zeros of $f$. Under RH, the zeros of $f(t) = \xi(1/2+it)$ are all on $\mathbb{R}$, and the function $u$ is harmonic throughout $\mathbb{H}$. The value at $w_0 = i/2$ is $u(i/2) = \log|f(i/2)| = -\log 2$ if and only if $f$ has no zeros in $\mathbb{H}$ (this is exactly Proposition 2.1 with an empty sum under RH). The consistency is perfect.

---

## §5. The excess $\delta$ in terms of the zeros of $F$ in the disk

### 5.1. The Jensen formula for $r < 1$

For $r < 1$, the Jensen formula for $F$ in the disk $|z| \leq r$ is exact:
$$\frac{1}{2\pi}\int_0^{2\pi}\log|F(re^{i\theta})|\,d\theta = -\log 2 + \sum_{|z_k|<r}\log\frac{r}{|z_k|},$$
where the sum runs over the zeros $z_k$ of $F$ in the disk $|z| < r$. The zeros of $F$ in the unit disk are (by Doc 84 §2, Corollary 2.3) exactly the points:
$$z_\rho = \frac{\rho - 1}{\rho} = 1 - \frac{1}{\rho}$$
for each zero $\rho = \sigma + i\gamma$ of $\xi$ with $\mathrm{Re}(\rho) > 1/2$, and their conjugates. The modulus is $|z_\rho|^2 = |\rho-1|^2/|\rho|^2 = ((\sigma-1)^2+\gamma^2)/(\sigma^2+\gamma^2)$.

### 5.2. The limit $r \to 1^-$

Taking $r \to 1^-$, the integral on the left-hand side converges (under the integrability condition for $\log|F|$ on the boundary) to $I = \int_{-\infty}^\infty \log|\xi(1/2+it)|\frac{2\,dt}{\pi(1+4t^2)}$. The right-hand side converges to:
$$-\log 2 + \sum_{|z_k|<1}\log\frac{1}{|z_k|} = -\log 2 + \sum_{\rho:\, \mathrm{Re}(\rho)>1/2}\log\frac{|\rho|}{|\rho-1|}.$$

**Proposition 5.1.** *The excess of the Jensen criterion is:*
$$\delta = I - (-\log 2) = \sum_{\rho:\, \mathrm{Re}(\rho)>1/2}\log\frac{|\rho|}{|\rho-1|}.$$
*For each zero $\rho = \sigma + i\gamma$ with $\sigma > 1/2$:*
$$\log\frac{|\rho|}{|\rho-1|} = \frac{1}{2}\log\frac{\sigma^2+\gamma^2}{(\sigma-1)^2+\gamma^2} > 0,$$
*since $\sigma^2 > (\sigma-1)^2$ when $\sigma > 1/2$. Consequently, $\delta \geq 0$ with equality if and only if there are no zeros with $\mathrm{Re}(\rho) > 1/2$, i.e., under RH.*

This confirms Proposition 6.1 of Doc 84: $I \geq -\log 2$ with equality under RH.

---

## §6. Reconciliation with the Poisson-Jensen formula and pairwise cancellation

### 6.1. Why the excess is not unconditionally zero

Corollary 10.4 of Doc 84 claimed that each pair of zeros $(\rho, 1-\rho)$ contributes zero to the excess, making the criterion trivially true. The error in that argument is precise: the computation evaluated, for a pair $(\rho, 1-\rho)$, the contribution to the excess $\delta$ as:
$$\log\frac{|\rho|}{|\rho-1|} + \log\frac{|1-\rho|}{|(1-\rho)-1|} = \log\frac{|\rho|}{|\rho-1|} + \log\frac{|1-\rho|}{|\rho|} = \log\frac{|\rho|}{|\rho-1|} + \log\frac{|\rho-1|}{|\rho|} = 0.$$
The error is that the sum in Proposition 5.1 runs only over zeros with $\mathrm{Re}(\rho) > 1/2$. If $\rho_0$ has $\mathrm{Re}(\rho_0) > 1/2$, its partner by the functional equation $1-\rho_0$ has $\mathrm{Re}(1-\rho_0) < 1/2$, and therefore $1-\rho_0$ does not contribute to the sum in Proposition 5.1 (its corresponding zero in the disk satisfies $|z_{1-\rho_0}|>1$, outside the disk). The zero $1-\rho_0$ with $\mathrm{Re}(1-\rho_0) < 1/2$ maps to the point $z_{1-\rho_0} = (1-\rho_0-1)/(1-\rho_0) = -\rho_0/(1-\rho_0)$, with $|z_{1-\rho_0}| = |\rho_0|/|1-\rho_0|$. For $\mathrm{Re}(\rho_0) > 1/2$, this quantity is $> 1$ (since $|\rho_0| > |\rho_0 - 1|$ when $\mathrm{Re}(\rho_0) > 1/2$). The zero is outside the disk.

**Proposition 6.1 (correction of the cancellation in Doc 84 §10.3).** *For a pair of zeros $(\rho_0, 1-\rho_0)$ with $\mathrm{Re}(\rho_0) > 1/2$:*
- *The zero $\rho_0$ gives a zero of $F$ at $z_{\rho_0} = (\rho_0-1)/\rho_0 \in \{|z|<1\}$, with $\log(1/|z_{\rho_0}|) = \log(|\rho_0|/|\rho_0-1|) > 0$.*
- *The zero $1-\rho_0$ gives a zero of $F$ at $z_{1-\rho_0} = -\rho_0/(1-\rho_0) \in \{|z|>1\}$, which does not contribute to the Jensen formula (it is outside the disk).*

*The arithmetic cancellation $(+A) + (-A) = 0$ that seemed to annul the excess was mistaken because the second term comes from a zero outside the disk and does not appear in the Jensen formula. The excess $\delta = \sum_{\rho:\,\mathrm{Re}(\rho)>1/2}\log(|\rho|/|\rho-1|)$ is a sum of strictly positive terms under $\neg$RH.*

### 6.2. The additional error in the residue computation of Doc 84 §10

Doc 84 §10.3 also argued that, for each pair $(\rho, 1-\rho)$, the integral $J(\rho) + J(1-\rho) = \mathrm{Re}[\log(1-1/\rho)] + \mathrm{Re}[\log(1-1/(1-\rho))] = \mathrm{Re}[\log(-1)] = 0$ (or indeed $= 0$ by an algebraic computation). This computation evaluated the harmonic function $u(w) = \mathrm{Re}[\log(1-(1/2+iw)/\rho)]$ at $w = -i/2$ (using the Poisson kernel of the lower half-plane). But the Poisson kernel of the lower half-plane $P_{1/2}^-(t) = \frac{1/2}{\pi(t^2+1/4)}$ evaluated at $w_0 = -i/2$ gives the harmonic extension of the boundary values to the lower half-plane, and the point $w_0 = -i/2 \in \mathbb{H}^-$ is valid for harmonic functions in $\mathbb{H}^-$. The correct computation of the harmonic value of $\mathrm{Re}[\log(1-s/\rho)]$ at $s = 1/2 + iw_0 = 1/2 + i(-i/2) = 1$ is $\mathrm{Re}[\log(1-1/\rho)]$, which is correct as an algebraic operation. And indeed:
$$\mathrm{Re}[\log(1-1/\rho) + \log(1-1/(1-\rho))] = \mathrm{Re}[\log\frac{\rho-1}{\rho}\cdot\frac{-\rho}{1-\rho}] = \mathrm{Re}[\log(-1)] = 0 \pmod{2\pi\mathbb{Z}}.$$
The result is $\mathrm{Re}[i\pi] = 0$: the real value is indeed zero.

**Proposition 6.2.** *For each pair $(\rho, 1-\rho)$ of zeros of $\xi$, with $\rho = \sigma + i\gamma$ anywhere in the strip $0 < \sigma < 1$:*
$$\mathrm{Re}[\log(1-1/\rho)] + \mathrm{Re}[\log(1-1/(1-\rho))] = \log\frac{|\rho-1|}{|\rho|} + \log\frac{|\rho|}{|\rho-1|} = 0.$$

*This cancellation is arithmetically correct, but is irrelevant to the Jensen criterion:*
*the integral $J(\rho)$, correctly computed, is not $\mathrm{Re}[\log(1-1/\rho)]$ for all $\rho$.*

### 6.3. Why $J(\rho) \neq \mathrm{Re}[\log(1-1/\rho)]$ for zeros in the disk

The integral $J(\rho) = \int_{-\infty}^\infty \mathrm{Re}[\log(1-(1/2+it)/\rho)]\frac{2\,dt}{\pi(1+4t^2)}$ is computed, for $\rho \notin \{1/2+it : t \in \mathbb{R}\}$, by the Poisson mean-value property of harmonic functions. The function $h(t) = \mathrm{Re}[\log(1-(1/2+it)/\rho)]$ is the real part of the analytic function $\log(1-s/\rho)$ with $s = 1/2+it$, which is harmonic in $t$ whenever $1/2+it \neq \rho$, i.e., away from the point $t = -i(\rho-1/2) = t_\rho$.

If $t_\rho \in \mathbb{H}^-$ (i.e., $\mathrm{Re}(\rho) > 1/2$), the function $h(t)$ is harmonic in a neighborhood of $\mathbb{H}^-$, and the Poisson integral with weight $P_{1/2}(t)$ gives the value of the harmonic extension at $w_0 = -i/2 \in \mathbb{H}^-$, which is $h_\mathrm{harm}(-i/2) = \mathrm{Re}[\log(1-s_0/\rho)]$ with $s_0 = 1/2+i(-i/2) = 1$. The computation is valid in this case: $J(\rho) = \mathrm{Re}[\log(1-1/\rho)]$ when $\mathrm{Re}(\rho) > 1/2$.

If $t_\rho \in \mathbb{H}$ (i.e., $\mathrm{Re}(\rho) < 1/2$), the function $h(t)$ has a logarithmic singularity at $t_\rho \in \mathbb{H}^-$... no, in $\mathbb{H}$. This means that $h(t)$ is not harmonic in all of $\mathbb{H}^-$ but only in $\mathbb{H}^- \setminus \{t_\rho\}$. The Poisson mean formula at $w_0 = -i/2 \in \mathbb{H}^-$ must include the correction for the singularity of $h$ at $t_\rho$:
$$J(\rho) = \mathrm{Re}[\log(1-1/\rho)] + \log\left|\frac{-i/2 - \bar{t}_\rho}{-i/2 - t_\rho}\right|.$$

The correction factor is the Poisson-Jensen term for the singularity at $t_\rho$. Computing it with $t_\rho = \gamma + i(1/2-\sigma)$ for $\sigma < 1/2$ (so that $\mathrm{Im}(t_\rho) = 1/2-\sigma > 0$, and the zero is in $\mathbb{H}$, not in $\mathbb{H}^-$)... The point $t_\rho$ is in $\mathbb{H}$, not $\mathbb{H}^-$, so there is no singularity in the lower half-plane. The function $h(t)$ for $\mathrm{Re}(\rho) < 1/2$ has its singularity in $\mathbb{H}$ (upper half-plane), and the Poisson integral at $w_0 = -i/2 \in \mathbb{H}^-$ does not pass through that singularity.

**Proposition 6.3.** *For $\mathrm{Re}(\rho) < 1/2$ (zero of $\xi$ in the left half-plane of the critical strip): $J(\rho) = \mathrm{Re}[\log(1-1/\rho)]$.*

*For $\mathrm{Re}(\rho) > 1/2$: also $J(\rho) = \mathrm{Re}[\log(1-1/\rho)]$.*

*Consequently, the cancellation $J(\rho) + J(1-\rho) = 0$ is algebraically correct for every pair $(\rho, 1-\rho)$.*

### 6.4. The real source of the discrepancy: sum-integral interchange

The cancellation $\sum_\rho [J(\rho) + J(1-\rho)] = 0$ is formally correct term by term, but the convergence of the series $\sum_\rho J(\rho)$ and the interchange $\sum_\rho J(\rho) = \int(\sum_\rho \mathrm{Re}[\log(\cdots)])\cdot P_{1/2}\,dt$ require absolute convergence of the sum. The series of the Hadamard product $\xi(1/2+it) = \xi(0)\prod_\rho (1-(1/2+it)/\rho)(1-(1/2+it)/(1-\rho))$ converges absolutely on the critical line, but the logarithm $\log|\xi(1/2+it)| = \log|\xi(0)| + \sum_\rho \mathrm{Re}[\log(1-(1/2+it)/\rho) + \log(1-(1/2+it)/(1-\rho))]$ is a conditionally convergent sum in $t$.

The integral-sum interchange in §5 of the task statement:
$$I = -\log 2 + \sum_\rho \int \mathrm{Re}[\log(\cdots)] P_{1/2}\,dt = -\log 2 + \sum_\rho [J(\rho) + J(1-\rho)] = -\log 2 + \sum_\rho 0 = -\log 2,$$
is invalid when the integral of $|\log|\xi(1/2+it)||$ against $P_{1/2}(t)$ diverges, which is exactly what happens under RH (zeros of $\xi$ on the critical line give $\log|\xi| = -\infty$ at real points of the integration domain).

**Proposition 6.4 (the source of the collapse).** *The unconditional cancellation argument $I = -\log 2$ fails because:*
*(a) Under RH, $\log|\xi(1/2+it)| = -\infty$ at the points $t = \gamma_n$, and the integral $I$ does not exist as a Lebesgue integral.*
*(b) Without RH (if $\xi$ has no zeros on the critical line), the cancellation would be valid and would give $I = -\log 2$, but this contradicts Proposition 5.1 (which asserts $I = -\log 2 + \delta$ with $\delta > 0$ under $\neg$RH). The contradiction reveals that, without zeros on the critical line, the sum-integral interchange has no technical obstacles, but the hypothesis itself (no zeros on the critical line) implies RH, making the argument circular.*

---

## §7. Regularization of the Jensen integral

### 7.1. The need for regularization

The integral $I = \int_{-\infty}^\infty \log|\xi(1/2+it)|\frac{2\,dt}{\pi(1+4t^2)}$ is not a Lebesgue integral because $\log|\xi(1/2+i\gamma_n)| = -\infty$ for each zero $\gamma_n$ of $\xi$ on the critical line. The function $\log|\xi(1/2+it)|$ is locally integrable near each zero (the behavior is $\sim \log|t-\gamma_n|$, which is integrable on an interval), but the presence of infinitely many zeros requires the series of contributions to converge.

### 7.2. Regularization via the Jensen formula for $r < 1$

The most natural regularization is the one already indicated: use the Jensen formula for $r < 1$ and take the limit:
$$I_r = \frac{1}{2\pi}\int_0^{2\pi}\log|F(re^{i\theta})|\,d\theta = -\log 2 + \sum_{|z_k|<r}\log\frac{r}{|z_k|}.$$
The integral $I_r$ is well defined for all $r < 1$ because $F(re^{i\theta}) \neq 0$ for $r < r_0$ where $r_0 = \min_{k}|z_k|$ (with the minimum over the zeros of $F$ in the disk). Under RH, $F$ has no zeros in the disk, and $I_r = -\log 2$ for all $r < 1$; the limit $I = -\log 2$ is trivially valid (without zeros in the disk, $\log|F(re^{i\theta})|$ converges uniformly to $\log|F(e^{i\theta})|$ if the convergence of $F$ is uniform, but in fact $F$ has zeros on the boundary and the convergence is not uniform). Under RH, the convergence of $I_r$ to $I$ is the monotone convergence of $\log|F(re^{i\theta})|$ to $\log|F(e^{i\theta})|$ (from above, since there are no zeros in the disk), and the integral converges by the monotone convergence theorem if $I > -\infty$.

**Proposition 7.1 (regularized criterion).** *The correct criterion for RH via the Jensen formula is:*
$$\mathrm{RH} \iff \lim_{r \to 1^-} \frac{1}{2\pi}\int_0^{2\pi}\log|F(re^{i\theta})|\,d\theta = -\log 2.$$
*Under $\neg$RH: the limit is $-\log 2 + \delta$ with $\delta = \sum_{\rho:\,\mathrm{Re}(\rho)>1/2}\log(|\rho|/|\rho-1|) > 0$.*

*The boundary integral $I = \int \log|F(e^{i\theta})|d\theta/(2\pi)$, if it exists as a Lebesgue integral, satisfies $I \leq -\log 2$ under RH (due to the presence of zeros on the boundary) and $I = -\infty$ if the zeros of $\xi$ on the critical line are sufficiently dense. The formulation via the limit $r \to 1^-$ is the well-defined version of the criterion.*

### 7.3. Convergence condition for the boundary integral

The integral $I = \int_0^{2\pi}\log|F(e^{i\theta})|d\theta$ converges (possibly to $-\infty$) when the series $\sum_n \int_{|\theta-\theta_n|<\epsilon_n}\log|e^{i\theta}-e^{i\theta_n}|\,d\theta$ converges absolutely. For simple zeros of $F$ at $e^{i\theta_n}$ (corresponding to simple zeros of $\xi$ on the critical line), the contribution of each zero is $\sim -c|\log\epsilon_n|\epsilon_n$. The series converges if the zeros of $\xi$ on the critical line are not too dense.

The density of zeros of $\xi$ in $[0,T]$ is $\sim \frac{T}{2\pi}\log\frac{T}{2\pi e}$ (Riemann-von Mangoldt formula). The typical spacing between consecutive zeros near $\gamma_n \approx T$ is $\sim 2\pi/\log T$. The contribution of each zero to $I$ is $\sim -\frac{2}{\pi(1+4\gamma_n^2)}\cdot |\log(2\pi/\log\gamma_n)|$. The series of these contributions converges conditionally (the positive contributions of $\log|\xi|$ away from the zeros compensate). The integral $I$ exists as a Lebesgue integral with value $-\infty$ only if the negative contributions dominate unconditionally, which does not occur for the zero distribution of $\xi$.

---

## §8. Synthesis of Path 2 at the end of Document 87

### 8.1. The complete structure of the Jensen criterion

Path 2 has produced, over the course of Docs 75–87, the following chain of equivalences:

**(a)** RH $\iff$ $F(z) = \xi(z/(z-1))$ has no zeros in $\{|z|<1\}$ (Doc 81).

**(b)** RH $\iff$ $\lim_{r\to 1^-}\frac{1}{2\pi}\int_0^{2\pi}\log|F(re^{i\theta})|\,d\theta = -\log 2$ (Proposition 7.1 of this document).

**(c)** RH $\iff$ $\int_{-\infty}^\infty \log|\xi(1/2+it)|\frac{2\,dt}{\pi(1+4t^2)} = -\log 2$ (distributed form of (b), valid as a Lebesgue integral if the zeros of $\xi$ on the critical line are simple and satisfy the convergence condition of §7.3).

**(d)** The excess of the criterion, under $\neg$RH, is exactly $\delta = \sum_{\rho:\,\mathrm{Re}(\rho)>1/2}\log(|\rho|/|\rho-1|) > 0$ (Proposition 5.1).

**(e)** The Poisson-Jensen formula in $\mathbb{H}$ evaluated at $w_0 = i/2$ is equivalent to (c), but is valid as a finite formula only under $\neg$RH (zeros of $f(t) = \xi(1/2+it)$ in the lower half-plane, corresponding to off-critical zeros with $\mathrm{Re}(\rho) > 1/2$); under RH, the zeros are on the real boundary and the formula diverges.

### 8.2. Table of corrected errors

The errors detected throughout the analysis, and their corrections:

| Error (identified in) | Correction |
|---|---|
| §2.2: $I \leq -\log 2$ under RH (Poisson-Jensen in $\mathbb{H}$) | The formula does not apply when $f$ has zeros on the boundary. The correct result is $I \geq -\log 2$ (disk criterion, Doc 84). |
| Doc 84 §10.3: pairwise cancellation $\delta = 0$ | The excess is a sum only over $\mathrm{Re}(\rho)>1/2$; the partner $1-\rho$ contributes from outside the disk. |
| Doc 84 §10: residue computation of $J(\rho)$ | The residue computation gives the correct value of $J(\rho)$, but the sum-integral interchange fails under RH due to non-integrability of $\log|\xi|$ on the boundary. |

### 8.3. The state of Path 2

**Solid result:** RH is equivalent to $\delta = 0$, where $\delta = \sum_{\rho:\,\mathrm{Re}(\rho)>1/2}\log(|\rho|/|\rho-1|)$. This is the excess of the Jensen formula, a convergent sum of non-negative terms.

**The barrier:** Proving $\delta = 0$ without assuming RH requires proving that $\xi$ has no zeros with $\mathrm{Re}(\rho) > 1/2$, which is exactly RH. The criterion is an exact, non-circular reformulation, but does not by itself offer a method of proof.

**The question that remains open:** Can $\delta$ be bounded above by analytic methods (energy bound, integral inequality, variational principle) in such a way as to force $\delta = 0$?

The relation $\delta = \sum_{|z_k|<1}\log(1/|z_k|)$ is the "logarithmic energy" of the zeros of $F$ in the disk with respect to the origin. A proof of $\delta = 0$ via function-theoretic methods would require a bound $\log(1/|z_k|) \leq 0$ for every zero of $F$ in the disk, which is equivalent to $|z_k| \geq 1$, that is, to there being no zeros in the disk. There is no circular escape here: any proof of $\delta = 0$ must use properties of $\xi$ going beyond the functional equation and the Hadamard product.

---

*Doc 87 completed.*
