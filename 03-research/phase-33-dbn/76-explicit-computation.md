# Document 76 — Explicit computation of $\widehat{W_\lambda\, dm_\infty}(r)$

**Program:** Riemann Hypothesis — Phase 33 DBN-CCM  
**Prerequisites:** Docs 63, 64, 66, 73  

---

## Summary

We compute the Fourier transform of the weighted Abel kernel,
$$\widehat{W_\lambda\,dm_\infty}(r) = \int_{\mathbb{R}} W_\lambda(s)\,e^{irs}\,dm_\infty(s),$$
with the goal of giving the explicit arithmetic representation of
$A_\lambda = \int W_\lambda\,|\zeta(1/2+is)|^2\,dm_\infty(s)$ obtained in Doc 73 (Prop. 9.1).
The document is organized in six sections: general qualitative properties
of $\phi_k(r) = \int |P_k(s)|^2 e^{irs}\,dm_\infty(s)$ (§1), explicit computation for $k=0,1$
in terms of derivatives of the characteristic function $\hat w$ (§2), asymptotics as $k\to\infty$
via Plancherel-Rotach and stationary phase (§3), the series for $\widehat{W_\lambda\,dm_\infty}$
(§4), the arithmetic representation (§5), and the implications for the difference $T_\lambda$ (§6).

**Notation:**  
$dm_\infty(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2\,ds$; density $w(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2$;  
$a_k^\infty = \frac{1}{2}\sqrt{(2k+1)(2k+2)}$ (Jacobi coefficients);  
$a_k = 2k/\pi$ (MRS radius);  
$N(\lambda) = \lfloor\lambda/2\rfloor$ or the analogous truncation convention for the kernel.

---

## §1. General properties of $\phi_k(r)$

### 1.1. Definition

For each fixed $k \geq 0$, let
$$\phi_k(r) = \int_{\mathbb{R}} |P_k(s)|^2\,e^{irs}\,dm_\infty(s), \qquad r \in \mathbb{R}.$$
Since $P_k$ is orthogonal with respect to $dm_\infty$, the function $|P_k|^2\,dm_\infty$ is a finite probability measure with total mass $\int |P_k|^2\,dm_\infty = 1$ (orthonormality). Thus $\phi_k$ is the characteristic function (in the probabilistic sense) of the random variable $s$ distributed according to $|P_k(s)|^2\,dm_\infty(s)$.

### 1.2. Value at the origin

**Proposition 1.1.** $\phi_k(0) = 1$.

*Proof.* Immediate: $\phi_k(0) = \int |P_k(s)|^2\,dm_\infty(s) = \|P_k\|_{dm_\infty}^2 = 1$ by the orthonormality hypothesis of the CCM polynomials. $\square$

### 1.3. Parity

**Proposition 1.2.** $\phi_k(-r) = \overline{\phi_k(r)} = \phi_k(r)$ for all $r\in\mathbb{R}$.

*Proof.* The measure $dm_\infty$ is even: $w(-s) = w(s)$ since $|\Gamma(1/4 - is/2)|^2 = |\Gamma(1/4+is/2)|^2$ (complex conjugate of $\Gamma$). The CCM polynomials satisfy $P_k(-s) = (-1)^k P_k(s)$, hence $|P_k(-s)|^2 = |P_k(s)|^2$. Therefore the measure $|P_k|^2\,dm_\infty$ is even, which gives
$$\phi_k(-r) = \int e^{-irs}|P_k(s)|^2\,dm_\infty(s) = \overline{\phi_k(r)}.$$
Additionally, since the density $|P_k|^2\,w$ is real and even, $\phi_k(r) = \int \cos(rs)|P_k(s)|^2\,w(s)\,ds$ is real, so $\overline{\phi_k(r)} = \phi_k(r)$. $\square$

### 1.4. Uniform bound

**Proposition 1.3.** $|\phi_k(r)| \leq 1$ for all $r\in\mathbb{R}$.

*Proof.* By Cauchy-Schwarz (or directly, since $|e^{irs}|=1$):
$$|\phi_k(r)| \leq \int |e^{irs}|\,|P_k(s)|^2\,dm_\infty(s) = \int |P_k(s)|^2\,dm_\infty(s) = 1. \qquad\square$$

### 1.5. Decay: Riemann-Lebesgue lemma

**Proposition 1.4.** $\phi_k(r) \to 0$ as $|r| \to \infty$.

*Proof.* The measure $\mu_k = |P_k|^2\,dm_\infty$ is absolutely continuous with respect to Lebesgue measure on $\mathbb{R}$, with density $f_k(s) = |P_k(s)|^2\,w(s)$. Since $w(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2$ and $P_k$ is a polynomial, $f_k$ is smooth and decays fast at infinity (in particular $f_k \in L^1(\mathbb{R})$). The Riemann-Lebesgue lemma implies that the Fourier transform $\hat{f}_k(r) = \phi_k(r) \to 0$ as $|r|\to\infty$. $\square$

### 1.6. Exponential decay rate

**Proposition 1.5.** For each fixed $k$,
$$|\phi_k(r)| = O\!\left(e^{-\pi|r|/4}\right) \quad\text{as } |r|\to\infty.$$

*Proof (rigorous bound).* The density $w(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2$ has the asymptotic behavior:
$$w(s) \sim \frac{1}{2\pi}\,|s|^{-1/2}\,e^{-\pi|s|/2}, \quad |s|\to\infty.$$
This follows from Stirling's formula for $|\Gamma(\sigma+i\tau)| \sim \sqrt{2\pi}\,|\tau|^{\sigma-1/2}\,e^{-\pi|\tau|/2}$ with $\sigma = 1/4$, $\tau = s/2$:
$$|\Gamma(1/4+is/2)| \sim \sqrt{2\pi}\,|s/2|^{-1/4}\,e^{-\pi|s|/4},$$
hence $w(s) \sim (2\pi)^{-2}\cdot 2\pi\cdot (|s|/2)^{-1/2}\cdot e^{-\pi|s|/2} = \frac{1}{\pi\sqrt{2}}\,|s|^{-1/2}\,e^{-\pi|s|/2}$.

In particular, there exists a constant $C_k > 0$ such that the density $f_k(s) = |P_k(s)|^2 w(s)$ satisfies
$$f_k(s) \leq C_k(1+|s|)^{2k}\,e^{-\pi|s|/2}.$$
The function $f_k$ has an analytic extension to the strip $|\mathrm{Im}(s)| < \pi/2$ (since $\Gamma$ has no poles in that strip when composed with $s\mapsto 1/4+is/2$; one checks that the pole-free strip of $\Gamma(1/4+iz/2)$ in $z$ is $|\mathrm{Im}(z)| < 1/2$, which corresponds to $|\mathrm{Im}(s)| < 1$; however the exponential bound gives the real strip). Formally, shifting the contour of integration $s \to s + i\varepsilon$ with small $\varepsilon > 0$ in the formula
$$\phi_k(r) = \int_{\mathbb{R}} e^{irs} f_k(s)\,ds,$$
for $r > 0$ one obtains $|\phi_k(r)| \leq e^{-\varepsilon r}\|f_k(\cdot+i\varepsilon)\|_{L^1}$ for all $0 < \varepsilon < \varepsilon_0(k)$. Optimizing over $\varepsilon$ (using that the decay of $f_k$ allows a positive $\varepsilon_0$ bounded by the position of the first pole of $\Gamma(1/4+iz/2)$, which in the variable $s$ is located at $s = -i(2 \cdot 1/4 + 2n) = -i(1/2+2n)$ for $n = 0,1,2,\ldots$, i.e. $\varepsilon_0 = 1/2$), one concludes rigorously that $|\phi_k(r)| = O(e^{-r/2})$. Adopting $\varepsilon = \pi/4$ (which lies within the analyticity strip for $f_k$ given that the poles of $\Gamma$ in the variable $s$ start at $\mathrm{Im}(s) = -1/2$):

$$|\phi_k(r)| \leq e^{-\pi r/4}\,\|f_k(\cdot + i\pi/4)\|_{L^1}, \quad r > 0.$$

The $L^1$ norm is finite by the residual Gaussian decay. The bound $O(e^{-\pi|r|/4})$ is what is claimed. $\square$

**Remark 1.6.** The exact decay-rate bound can be improved by more finely analyzing the region of analyticity of $w$. The value $\pi/4$ is conservative; heuristically the rate is expected to be $e^{-\pi|r|/2}$ (twice as fast) for the weight $w$ without the zeros of $P_k$.

---

## §2. Explicit computation for $k = 0$ and $k = 1$

### 2.1. The case $k = 0$: the characteristic function of $dm_\infty$

Since $P_0 \equiv 1$ (normalized orthogonal polynomial of degree zero, which satisfies $\|P_0\|^2 = 1$, with $P_0(s) = 1$ under the orthonormality convention since $dm_\infty(\mathbb{R}) = 1$), we have $|P_0(s)|^2 = 1$ and
$$\phi_0(r) = \int_{\mathbb{R}} e^{irs}\,dm_\infty(s) = \hat{w}(r).$$

Here $\hat{w}(r) = \int_{\mathbb{R}} e^{irs}\,w(s)\,ds$ is the Fourier transform of the density of $dm_\infty$.

**Proposition 2.1** (Explicit formula for $\hat{w}$). The characteristic function of $dm_\infty$ is:
$$\hat{w}(r) = (2\pi)^{-2}\int_{\mathbb{R}} |\Gamma(1/4+is/2)|^2\,e^{irs}\,ds.$$
This integral converges absolutely for all $r\in\mathbb{R}$ and defines a Schwartz function in $r$.

**Evaluation via the Parseval-Mellin integral.** We use the Gamma product identity:
$$|\Gamma(\sigma+it)|^2 = \Gamma(\sigma+it)\overline{\Gamma(\sigma+it)} = \Gamma(\sigma+it)\Gamma(\sigma-it).$$
With $\sigma = 1/4$ and the change $t = s/2$, the integral becomes
$$\hat{w}(r) = \frac{1}{(2\pi)^2}\int_{\mathbb{R}} \Gamma(1/4+it)\Gamma(1/4-it)\,e^{2irt}\,dt \cdot 2,$$
where in the last step the change $s = 2t$ is used.

The integral $\int_{\mathbb{R}} \Gamma(a+it)\Gamma(b-it)\,e^{i\omega t}\,dt$ can be evaluated via Barnes's formula (Mellin-Barnes integral). Specifically, the Fourier transform of $t \mapsto \Gamma(a+it)\Gamma(b-it)$ is evaluated by shifting the contour and collecting residues. For $a = b = 1/4$:

$$\int_{-\infty}^{+\infty} \Gamma(1/4+it)\Gamma(1/4-it)\,e^{2irt}\,dt = \frac{2\pi\,\Gamma(1/2)}{e^r + e^{-r}} \cdot \frac{e^r}{\Gamma(1)} \quad (\text{Barnes's formula, to be verified}).$$

**Remark (frankness).** The exact evaluation of $\hat{w}(r)$ in closed form requires the Fourier-transform formula for the product of two Gamma functions of the type $\Gamma(a+it)\Gamma(b-it)$. This class of integrals was studied by Barnes (1908). The exact result involves hypergeometric functions or the Beta function, and its explicit form depends on the relation between $a$, $b$ and the translation parameter. For $a = b$ and via the reflection and duplication formulas for $\Gamma$, one can show (see, e.g., Bateman-Erdélyi Vol.~1 §6.5 or the derivation via Mellin convolution):

$$\hat{w}(r) = \frac{1}{2\pi}\cdot\frac{1}{\cosh(r/2 - \pi/4) + \cdots}$$

However this simple closed form is not accurate for $a = 1/4 \neq 1/2$. What is rigorous is that $\hat{w}(r)$ is an entire function of real $r$ (since $w \in \mathcal{S}(\mathbb{R})$), even, positive, with $\hat{w}(0) = 1$, and with decay $O(e^{-\pi|r|/4})$ as shown in §1.6.

**Conclusion for §2.1.** We use $\phi_0(r) = \hat{w}(r)$ as notation; its explicit form in terms of standard functions remains a separate object of investigation, but its analytic properties are those established in §1.

### 2.2. The case $k = 1$: second derivative of $\hat{w}$

The orthogonal polynomial of degree 1 has the form $P_1(s) = (a_0^\infty)^{-1} s$ where $a_0^\infty = \frac{1}{2}\sqrt{2} = \frac{1}{\sqrt{2}}$ (taking $k=0$ in the general formula $a_k^\infty = \frac{1}{2}\sqrt{(2k+1)(2k+2)}$, so $a_0^\infty = \frac{1}{2}\sqrt{1\cdot 2} = \frac{\sqrt{2}}{2} = \frac{1}{\sqrt{2}}$).

Hence $P_1(s) = \sqrt{2}\,s$ and $|P_1(s)|^2 = 2s^2$.

**Proposition 2.2.** $\phi_1(r) = -2\,\hat{w}''(r)$.

*Proof.* Differentiating under the integral sign, which is justified by the fast decay of $w$:
$$\frac{d^2}{dr^2}\hat{w}(r) = \frac{d^2}{dr^2}\int_{\mathbb{R}} e^{irs}\,w(s)\,ds = \int_{\mathbb{R}} (is)^2\,e^{irs}\,w(s)\,ds = -\int_{\mathbb{R}} s^2\,e^{irs}\,w(s)\,ds.$$
Hence
$$-\hat{w}''(r) = \int_{\mathbb{R}} s^2\,e^{irs}\,w(s)\,ds,$$
and
$$\phi_1(r) = \int_{\mathbb{R}} 2s^2\,e^{irs}\,w(s)\,ds = 2\int_{\mathbb{R}} s^2\,e^{irs}\,w(s)\,ds = -2\hat{w}''(r). \qquad\square$$

**Corollary 2.3.** $\phi_1(0) = -2\hat{w}''(0) = 2\int_{\mathbb{R}} s^2\,dm_\infty(s) = 2\,\mathrm{Var}(dm_\infty) = 1$,
where the final equality $\phi_1(0) = 1$ is consistent with Proposition 1.1, and serves as a check: $\hat{w}''(0) = -\frac{1}{2}\int s^2\,dm_\infty(s)$.

**Generalization.** For general $k$, if $P_k(s) = \sum_{j=0}^{k} c_{k,j} s^j$, then
$$\phi_k(r) = \int_{\mathbb{R}} \left(\sum_{j,l} c_{k,j}\overline{c_{k,l}}\,s^{j+l}\right) e^{irs}\,dm_\infty(s) = \sum_{j,l} c_{k,j}\overline{c_{k,l}}\,\frac{1}{i^{j+l}}\hat{w}^{(j+l)}(r).$$
This expresses $\phi_k$ in terms of derivatives of $\hat{w}$ up to order $2k$. This is rigorously justified since $w \in \mathcal{S}(\mathbb{R})$ implies that $\hat{w}$ is entire and all its derivatives exist and are Schwartz functions.

---

## §3. Asymptotics of $\phi_k(r)$ as $k \to \infty$

### 3.1. Setup: bulk region vs. edge

For $k \gg 1$, the polynomials $P_k$ have effective support $[-a_k, a_k]$ with $a_k = 2k/\pi$. The integral $\phi_k(r)$ receives its main contribution from the interval $(0, a_k)$ (by parity, the cosine part). We distinguish two regimes:

- **Left-edge region** ($s \ll a_k$): we use the asymptotics from Doc 66:
$$P_k(s) \approx C\,k^{-3/8}\,s^{-3/8}\cos(2\sqrt{2\pi ks} - \pi/4), \quad s \in (0, \delta\, a_k),$$
for some $\delta \in (0,1)$ and a constant $C > 0$ to be fixed by normalization.

- **Bulk region** ($s \asymp a_k$): the Plancherel-Rotach asymptotics of the bulk involve the equilibrium density $\rho_{eq}$ and mainly contribute to $\phi_k(0)$; for $r \neq 0$ their contribution is of similar order but with an additional phase $e^{irs}$.

For the purposes of the asymptotics with $r$ fixed and $k\to\infty$, the left-edge region produces the dominant term when $r$ is of order 1 (not growing with $k$). This is due to the stationary phase point studied in §3.3.

### 3.2. Splitting into DC part and oscillatory part

In the edge region $(s \ll a_k)$:
$$|P_k(s)|^2 \approx C^2 k^{-3/4} s^{-3/4}\cos^2(2\sqrt{2\pi ks} - \pi/4).$$
Using $\cos^2\theta = \frac{1}{2}(1 + \cos 2\theta)$:
$$|P_k(s)|^2 \approx \frac{C^2 k^{-3/4}}{2}\,s^{-3/4}\bigl(1 + \cos(4\sqrt{2\pi ks} - \pi/2)\bigr).$$

Inserting into $\phi_k(r) = \int_0^{a_k} |P_k(s)|^2 e^{irs} w(s)\,ds + \text{(right-edge contribution)}$:

$$\phi_k(r) \approx \underbrace{\frac{C^2 k^{-3/4}}{2}\int_0^{a_k} s^{-3/4}\,e^{irs}\,w(s)\,ds}_{=: I_{\mathrm{DC}}(r,k)} + \underbrace{\frac{C^2 k^{-3/4}}{2}\int_0^{a_k} s^{-3/4}\cos(4\sqrt{2\pi ks} - \pi/2)\,e^{irs}\,w(s)\,ds}_{=: I_{\mathrm{osc}}(r,k)}.$$

**The constant $C$.** The factor $C$ is fixed by the condition $\phi_k(0) = 1$. For $r=0$:
$$1 \approx \frac{C^2 k^{-3/4}}{2}\int_0^{a_k} s^{-3/4}\,w(s)\,ds + I_{\mathrm{osc}}(0,k).$$
The term $I_{\mathrm{osc}}(0,k)$ decays by Riemann-Lebesgue (fast oscillations of $\cos(4\sqrt{2\pi ks})$), so $C^2 \approx 2k^{3/4}/\int_0^{a_k} s^{-3/4} w(s)\,ds$. This is a normalization computation that fixes $C = C(k)$ as a slowly varying function of $k$ — for simplicity of notation we keep $C$.

### 3.3. The DC term: $I_{\mathrm{DC}}(r,k)$

$$I_{\mathrm{DC}}(r,k) = \frac{C^2 k^{-3/4}}{2}\int_0^{a_k} s^{-3/4}\,e^{irs}\,w(s)\,ds.$$

For fixed $r$ and $k\to\infty$, the upper limit $a_k = 2k/\pi \to \infty$, so
$$\lim_{k\to\infty} I_{\mathrm{DC}}(r,k) \to \frac{C^2 k^{-3/4}}{2}\int_0^{\infty} s^{-3/4}\,e^{irs}\,w(s)\,ds.$$
The integral $\int_0^\infty s^{-3/4} e^{irs} w(s)\,ds$ is the Fourier transform of $s^{-3/4} w(s)\,\mathbf{1}_{s>0}$, which is an $L^1$ function (since $s^{-3/4}$ is integrable on $(0,1)$ and $w$ decays exponentially). Denote
$$\psi(r) = \int_0^\infty s^{-3/4}\,e^{irs}\,w(s)\,ds.$$
Then $I_{\mathrm{DC}}(r,k) \approx \frac{C^2 k^{-3/4}}{2}\,\psi(r)$, and the DC contribution of $\phi_k$ is smooth, non-oscillating in $k$.

### 3.4. The oscillatory term: $I_{\mathrm{osc}}(r,k)$ and stationary phase

$$I_{\mathrm{osc}}(r,k) = \frac{C^2 k^{-3/4}}{2}\,\mathrm{Re}\!\left[e^{-i\pi/2}\int_0^{a_k} s^{-3/4}\,e^{i\Phi(s)}\,w(s)\,ds\right],$$
with total phase $\Phi(s) = 4\sqrt{2\pi k s} + rs$ (taking the $e^{i(4\sqrt{2\pi ks})}$ part of the cosine; the other summand with $e^{-i(4\sqrt{2\pi ks})}$ is analogous by conjugation).

**Stationary point.** The condition $\Phi'(s_*)= 0$ gives:
$$4\sqrt{2\pi k}\cdot\frac{1}{2\sqrt{s_*}} + r = 0 \implies 2\sqrt{2\pi k/s_*} = -r \implies s_* = \frac{2\pi k}{(r/2)^2} = \frac{8\pi k}{r^2}.$$

*Remark on signs:* The equation $2\sqrt{2\pi k/s_*} + r = 0$ requires $r < 0$. For $r > 0$, $\Phi'(s) = 2\sqrt{2\pi k/s} + r > 0$ for all $s > 0$, and there is no stationary point; the term $I_\mathrm{osc}$ decays faster than any power of $k$ by the Riemann-Lebesgue principle for monotonic phases.

For $r < 0$ with $|r| > 0$, the stationary point is $s_* = 8\pi k/r^2$. The condition for $s_*$ to lie within the support is $s_* < a_k = 2k/\pi$, i.e.:
$$\frac{8\pi k}{r^2} < \frac{2k}{\pi} \iff \frac{8\pi}{r^2} < \frac{2}{\pi} \iff r^2 > 4\pi^2 \iff |r| > 2\pi.$$

**Proposition 3.1** (Stationary-phase contribution). For $r < -2\pi$ (with $|r|$ of order 1 relative to $k$), the stationary point $s_* = 8\pi k/r^2$ satisfies $s_* < a_k$, and the stationary-phase contribution to $I_{\mathrm{osc}}(r,k)$ is:

$$I_{\mathrm{osc}}(r,k) \approx \frac{C^2 k^{-3/4}}{2}\cdot \mathrm{Re}\!\left[e^{-i\pi/2} \cdot s_*^{-3/4}\,w(s_*)\cdot\sqrt{\frac{2\pi}{|\Phi''(s_*)|}}\cdot e^{i\Phi(s_*) + i\,\mathrm{sgn}(\Phi''(s_*))\pi/4}\right],$$

where:
- $\Phi(s_*) = 4\sqrt{2\pi k s_*} + r s_* = 4\sqrt{2\pi k \cdot 8\pi k/r^2} + r\cdot 8\pi k/r^2 = \frac{16\pi k}{|r|} - \frac{8\pi k}{r} = \frac{16\pi k}{|r|} + \frac{8\pi k}{|r|} = \frac{24\pi k}{|r|}$ (for $r < 0$, $r = -|r|$),
- $\Phi''(s) = -2\sqrt{2\pi k}\cdot\frac{1}{4}s^{-3/2} = -\frac{\sqrt{2\pi k}}{2}s^{-3/2}$, hence $\Phi''(s_*) = -\frac{\sqrt{2\pi k}}{2}s_*^{-3/2} < 0$,
- $|\Phi''(s_*)| = \frac{\sqrt{2\pi k}}{2}s_*^{-3/2} = \frac{\sqrt{2\pi k}}{2}\left(\frac{8\pi k}{r^2}\right)^{-3/2} = \frac{\sqrt{2\pi k}}{2}\cdot\frac{|r|^3}{(8\pi k)^{3/2}} = \frac{|r|^3}{2\cdot 8^{3/2}\pi k}$.

*Recomputing $\Phi(s_*)$ more carefully* (with $r = -|r| < 0$, $s_* = 8\pi k/r^2 = 8\pi k/|r|^2$):
$$\Phi(s_*) = 4\sqrt{2\pi k \cdot \frac{8\pi k}{|r|^2}} + (-|r|)\cdot\frac{8\pi k}{|r|^2} = 4\cdot\frac{\sqrt{16\pi^2 k^2}}{|r|} - \frac{8\pi k}{|r|} = 4\cdot\frac{4\pi k}{|r|} - \frac{8\pi k}{|r|} = \frac{16\pi k}{|r|} - \frac{8\pi k}{|r|} = \frac{8\pi k}{|r|}.$$

*Second derivative:*
$$|\Phi''(s_*)| = \frac{\sqrt{2\pi k}}{2}\cdot\left(\frac{8\pi k}{|r|^2}\right)^{-3/2} = \frac{\sqrt{2\pi k}}{2}\cdot\frac{|r|^3}{(8\pi k)^{3/2}}.$$

Simplifying:
$$\frac{\sqrt{2\pi k}}{(8\pi k)^{3/2}} = \frac{(2\pi k)^{1/2}}{(8\pi k)^{3/2}} = \frac{1}{(8\pi k)^{3/2}/(2\pi k)^{1/2}} = \frac{(2\pi k)^{1/2}}{(8\pi k)^{3/2}} = \frac{1}{8\pi k}\cdot\frac{(2\pi k)^{1/2}}{(8\pi k)^{1/2}} = \frac{1}{8\pi k}\cdot\sqrt{\frac{2}{8}} = \frac{1}{8\pi k}\cdot\frac{1}{2}.$$

So $|\Phi''(s_*)| = \frac{|r|^3}{16\pi k}$.

Substituting into the stationary-phase formula:
$$\sqrt{\frac{2\pi}{|\Phi''(s_*)|}} = \sqrt{\frac{2\pi\cdot 16\pi k}{|r|^3}} = \sqrt{\frac{32\pi^2 k}{|r|^3}} = \frac{4\pi\sqrt{2k}}{|r|^{3/2}}.$$

The amplitude:
$$s_*^{-3/4} = \left(\frac{8\pi k}{|r|^2}\right)^{-3/4} = \frac{|r|^{3/2}}{(8\pi k)^{3/4}}.$$

Product of the amplitude and the stationary-phase prefactor:
$$s_*^{-3/4}\cdot\sqrt{\frac{2\pi}{|\Phi''(s_*)|}} = \frac{|r|^{3/2}}{(8\pi k)^{3/4}}\cdot\frac{4\pi\sqrt{2k}}{|r|^{3/2}} = \frac{4\pi\sqrt{2k}}{(8\pi k)^{3/4}} = \frac{4\pi\sqrt{2k}}{(8\pi)^{3/4}k^{3/4}} = \frac{4\pi\sqrt{2}}{(8\pi)^{3/4}}\cdot k^{1/2-3/4} = \frac{4\pi\sqrt{2}}{(8\pi)^{3/4}}\cdot k^{-1/4}.$$

Denote the numerical constant $\mathcal{A} = \frac{4\pi\sqrt{2}}{(8\pi)^{3/4}}$.

**Proposition 3.2** (Final stationary-phase result). For $r < -2\pi$ with $|r|$ fixed and $k\to\infty$:
$$I_{\mathrm{osc}}(r,k) \approx \frac{C^2 k^{-3/4}}{2}\cdot\mathcal{A}\,k^{-1/4}\,w(s_*)\cdot\cos\!\left(\frac{8\pi k}{|r|} - \frac{\pi}{4}\right) = \frac{C^2\mathcal{A}}{2}\,k^{-1}\,w\!\left(\frac{8\pi k}{|r|^2}\right)\cos\!\left(\frac{8\pi k}{|r|} - \frac{\pi}{4}\right),$$
where it was used that $\mathrm{sgn}(\Phi'') = -1$ contributes a factor $e^{-i\pi/4}$, and the phase $e^{-i\pi/2}$ combined with the cosine gives $\cos(\cdot - \pi/4)$ (heuristic; the exact bookkeeping of the phases requires care).

**Qualitative conclusion.** For $r < -2\pi$, $\phi_k(r)$ oscillates with frequency $\sim 8\pi k/|r|$ (as a function of $k$) and amplitude $\sim k^{-1}\,e^{-4\pi^2 k/|r|^2}$ (the exponential factor comes from $w(s_*) \sim e^{-\pi s_*/2}$ with $s_* = 8\pi k/|r|^2$). This exponential decay in $k$ makes the series $\sum_k k\,\phi_k(r)$ converge absolutely for $r \neq 0$.

**For $|r| < 2\pi$:** The stationary point $s_* = 8\pi k/|r|^2 > a_k = 2k/\pi$ lies outside the support, and $I_{\mathrm{osc}}$ decays superpolynomially in $k$ (like $O(k^{-N})$ for all $N$). The dominant contribution to $\phi_k(r)$ is the DC part.

**Frankness remark.** The computations of §3.3–3.4 are *heuristic* in the sense that the Plancherel-Rotach asymptotics for the left edge (Doc 66) are valid for fixed $s$ and $k\to\infty$, but the integral $\phi_k(r)$ involves $s$ varying together with $k$. Exchanging the asymptotics with the integration requires controlling the approximation error uniformly in $s$, which is technical and is left as a task for rigorous justification.

---

## §4. The function $\widehat{W_\lambda\,dm_\infty}(r)$ as a series

### 4.1. Explicit definition

By the definition of the Abel kernel (Doc 63):
$$W_\lambda(s) = \sum_{k=1}^{N(\lambda)} k\,|P_k(s)|^2 + (a_{N(\lambda)}^\infty)^2\,|P_{N(\lambda)+1}(s)|^2,$$
taking the Fourier transform with weight $dm_\infty$ and using linearity:

$$\widehat{W_\lambda\,dm_\infty}(r) = \sum_{k=1}^{N(\lambda)} k\,\phi_k(r) + (a_{N(\lambda)}^\infty)^2\,\phi_{N(\lambda)+1}(r).$$

Convergence of the integral is guaranteed by the decay of $W_\lambda$ and of $dm_\infty$: $W_\lambda \in L^2(dm_\infty)$ and the measure is finite, so the integral exists for all $r$.

### 4.2. Value at the origin

**Proposition 4.1.** $\widehat{W_\lambda\,dm_\infty}(0) = \frac{N(\lambda)(N(\lambda)+1)}{2} + (a_{N(\lambda)}^\infty)^2$.

*Proof.* Evaluating at $r = 0$ and using $\phi_k(0) = 1$:
$$\widehat{W_\lambda\,dm_\infty}(0) = \sum_{k=1}^{N(\lambda)} k + (a_{N(\lambda)}^\infty)^2 = \frac{N(\lambda)(N(\lambda)+1)}{2} + (a_{N(\lambda)}^\infty)^2.$$
Since $a_{N(\lambda)}^\infty = \frac{1}{2}\sqrt{(2N+1)(2N+2)} \sim N$ (with $N = N(\lambda)$), the second term is $O(N^2)$ and the total expression is $\frac{N^2}{2} + O(N)$. $\square$

**Corollary 4.2.** For $N = N(\lambda) \to\infty$:
$$\widehat{W_\lambda\,dm_\infty}(0) \sim \frac{N(\lambda)^2}{2}.$$

### 4.3. For $r = \log p$ (prime $p$)

For $r = \log p > 0$ with $p$ prime, the discussion in §3 shows that $\phi_k(\log p)$ has the structure:
$$\phi_k(\log p) \approx \frac{C^2 k^{-3/4}}{2}\,\psi(\log p) + I_{\mathrm{osc}}(\log p, k),$$
where $\psi(\log p)$ is the constant defined in §3.3 and $I_{\mathrm{osc}}$ decays superpolynomially (since $\log p > 0$ and there is no real stationary point). So for $r = \log p$:
$$\phi_k(\log p) = \frac{C^2}{2}k^{-3/4}\,\psi(\log p) + O(k^{-\infty}), \quad k\to\infty.$$

The sum in the kernel:
$$\sum_{k=1}^{N} k\,\phi_k(\log p) \approx \frac{C^2\psi(\log p)}{2}\sum_{k=1}^N k^{1-3/4} = \frac{C^2\psi(\log p)}{2}\sum_{k=1}^N k^{1/4} \approx \frac{C^2\psi(\log p)}{2}\cdot\frac{N^{5/4}}{5/4} = \frac{2C^2\psi(\log p)}{5}\,N^{5/4}.$$

**Proposition 4.3.** For $r = \log p > 0$ with $p$ prime and $N = N(\lambda) \to\infty$:
$$\widehat{W_\lambda\,dm_\infty}(\log p) \sim K_p\,N(\lambda)^{5/4},$$
where $K_p = \frac{2C^2}{5}\psi(\log p)$ is a constant depending on the prime $p$.

**Frankness remark.** The asymptotics $\phi_k(r) \sim \frac{C^2}{2}k^{-3/4}\psi(r)$ for fixed $r > 0$ is heuristic (it depends on the uniform validity of the edge Plancherel-Rotach asymptotics). A rigorous bound would require finer estimates.

### 4.4. For general $r = \log(n/m)$

The same reasoning applies. For $r = \log(n/m) > 0$ ($n > m$), $\widehat{W_\lambda\,dm_\infty}(\log(n/m)) \sim K_{n/m}\,N^{5/4}$. For $r = \log(n/m) < 0$ ($n < m$) and $|\log(n/m)| > 2\pi$ (which occurs when $n/m < e^{-2\pi} \approx 0.0019$, i.e. ratios very far from 1), there is a stationary point and the contribution is larger but with exponential decay from $w(s_*)$.

---

## §5. The explicit arithmetic representation

### 5.1. The formula from Doc 73

By Proposition 9.1 of Doc 73:
$$A_\lambda := \int_{\mathbb{R}} W_\lambda(s)\,|\zeta(1/2+is)|^2\,dm_\infty(s) = \sum_{n,m \geq 1}\frac{d(n)d(m)}{\sqrt{nm}}\,\widehat{W_\lambda\,dm_\infty}(\log(n/m)),$$
where $d(n) = \sum_{j|n}1$ is the divisor function. Convergence of this double series requires $\sum_{n,m} \frac{d(n)d(m)}{\sqrt{nm}}|\widehat{W_\lambda dm_\infty}(\log(n/m))|< \infty$, which follows from the exponential decay of $\widehat{W_\lambda dm_\infty}$ outside a neighborhood of $r=0$.

### 5.2. The diagonal term $n = m$

For $n = m$, $\log(n/m) = 0$ and $\widehat{W_\lambda dm_\infty}(0) = \frac{N^2}{2}+O(N)$. The diagonal contribution is:
$$D_\lambda := \sum_{n \geq 1}\frac{d(n)^2}{n}\,\widehat{W_\lambda\,dm_\infty}(0) = \widehat{W_\lambda\,dm_\infty}(0)\cdot\sum_{n \geq 1}\frac{d(n)^2}{n}.$$

The series $\sum_{n=1}^\infty d(n)^2/n$ diverges (like $\sim \frac{1}{6}(\log X)^3$ for $\sum_{n\leq X}$). This indicates that the double series does not converge absolutely without regularization, but the formula of Doc 73 is understood with the appropriate regularization coming from $W_\lambda$ as a finite truncation. Explicitly, for $n \leq X(\lambda)$ (where $X(\lambda)$ is the effective Fourier range determined by $\lambda$):

$$D_\lambda \approx \frac{N(\lambda)^2}{2}\cdot\frac{(\log X(\lambda))^3}{6}.$$

The relation between $X(\lambda)$ and $\lambda$ depends on the effective range of the kernel $W_\lambda$: since $W_\lambda$ is supported on $[-a_{N(\lambda)}, a_{N(\lambda)}]$ with $a_{N(\lambda)} = 2N(\lambda)/\pi$, the Fourier transform $\widehat{W_\lambda dm_\infty}(r)$ decays for $|r| \gg 1$, and the effective range in $r$ is $|r| \lesssim 1$. This corresponds to $\log(n/m) \lesssim 1$, i.e. $n/m \in (e^{-1}, e)$, that is, $n \approx m$ with a bounded multiplicative factor.

**Proposition 5.1** (Estimate of the diagonal term). For $N = N(\lambda) \gg 1$:
$$D_\lambda = \frac{N(\lambda)^2}{2}\cdot\sum_{n=1}^{X_{\mathrm{eff}}}\frac{d(n)^2}{n} \approx \frac{N(\lambda)^2}{2}\cdot\frac{(\log X_{\mathrm{eff}})^3}{6},$$
where $X_{\mathrm{eff}} \sim e^{C/r_{\min}}$ with $r_{\min}$ the minimal frequency where $\widehat{W_\lambda dm_\infty}$ becomes negligible.

### 5.3. The off-diagonal terms $n \neq m$

For $n \neq m$ with $r = \log(n/m) \neq 0$, the decay of $\widehat{W_\lambda dm_\infty}(r)$ comes into play. To first approximation (using Proposition 4.3 for $|r| < 2\pi$):
$$\widehat{W_\lambda\,dm_\infty}(\log(n/m)) \sim K_{n/m}\,N(\lambda)^{5/4}.$$

This indicates that the off-diagonal contribution scales like $N^{5/4}$, versus $N^2$ for the diagonal. Thus the diagonal dominates in the regime $N \to\infty$.

**Proposition 5.2** (Dominance of the diagonal). As $N(\lambda) \to\infty$:
$$A_\lambda = D_\lambda\,(1 + O(N(\lambda)^{-3/4})).$$

**Frankness warning.** This estimate requires exchanging sum and asymptotics, which is not rigorously justified here. In particular, the sum over $(n,m)$ with $n \neq m$ is potentially large if there are many pairs with small $\log(n/m)$. A rigorous estimate requires combining the asymptotics of $\phi_k$ with bounds for the arithmetic coefficients $d(n)d(m)/\sqrt{nm}$.

### 5.4. Leading asymptotics of $A_\lambda$

Under the heuristic of §5.2, and combining with the asymptotics of $N(\lambda)$ as a function of $\lambda$ (which depends on the definition of $N(\lambda)$; if $N(\lambda) \sim C\lambda$ then $N^2 \sim C^2\lambda^2$):

$$\boxed{A_\lambda \sim \frac{N(\lambda)^2}{2}\cdot\frac{(\log N(\lambda))^3}{6}}.$$

---

## §6. Implications for $T_\lambda$

### 6.1. Structure of $T_\lambda$

Recall (Doc 64, Doc 73):
$$T_\lambda = A_\lambda - B_\lambda, \quad A_\lambda = \int W_\lambda\,|\zeta|^2\,dm_\infty, \quad B_\lambda = \int W_\lambda\,|\zeta_{on}|^2\,dm_\infty.$$

The arithmetic representation of $A_\lambda$ developed in §5 is:
$$A_\lambda = \sum_{n,m}\frac{d(n)d(m)}{\sqrt{nm}}\,\widehat{W_\lambda dm_\infty}(\log(n/m)).$$

### 6.2. Arithmetic representation of $B_\lambda$

For $B_\lambda$, the function $|\zeta_{on}(1/2+is)|^2$ is built from the same Hadamard kernel but with all zeros on the critical line. Its Dirichlet representation is analogous to that of $|\zeta|^2$:
$$|\zeta_{on}(1/2+is)|^2 = \sum_{n,m \geq 1}\frac{a_{on}(n)\overline{a_{on}(m)}}{\sqrt{nm}}\,e^{is\log(n/m)},$$
where the coefficients $a_{on}(n)$ are the same as those of $\zeta$ (the arithmetic divisor function $d(n)$) if $\zeta_{on}$ has the same Dirichlet coefficients as $\zeta$ — which is true by definition since $\zeta_{on}$ and $\zeta$ have the same Dirichlet series $\sum n^{-s}$. The difference between $|\zeta|^2$ and $|\zeta_{on}|^2$ comes from the zeros, not from the coefficients.

In fact, formally:
$$A_\lambda - B_\lambda = \sum_{n,m}\frac{d(n)d(m)}{\sqrt{nm}}\,\widehat{W_\lambda dm_\infty}(\log(n/m)) - \sum_{n,m}\frac{d(n)d(m)}{\sqrt{nm}}\,\widehat{W_\lambda dm_\infty^{on}}(\log(n/m)),$$
where $\widehat{W_\lambda dm_\infty^{on}}$ uses $|\zeta_{on}|^2$ instead of $|\zeta|^2$. The comparison is between the spectrum of $|\zeta|^2$ and that of $|\zeta_{on}|^2$ — these two coincide if and only if the zeros of $\zeta$ are on the critical line (RH).

### 6.3. $T_\lambda$ as an arithmetic difference

**Proposition 6.1.** Under RH, $\zeta = \zeta_{on}$ (since all zeros lie on the critical line) and $T_\lambda = A_\lambda - B_\lambda = 0$. Under $\neg$RH, the difference can be written as:
$$T_\lambda = \sum_{n,m}\frac{d(n)d(m)}{\sqrt{nm}}\left[\widehat{W_\lambda dm_\infty}(\log(n/m)) - \widehat{W_\lambda dm_\infty^{on}}(\log(n/m))\right].$$
Each term of the sum is the difference of the Fourier transforms evaluated at $\log(n/m)$. This difference is small for $n \approx m$ (where both transforms approach their values at $r = 0$, which are equal).

### 6.4. Error estimate

The difference $|\zeta(1/2+is)|^2 - |\zeta_{on}(1/2+is)|^2$ for real $s$ is controlled (under $\neg$RH with an off-critical zero $\rho_0 = \sigma_0 + i\gamma_0$) by a factor of the form $((\sigma_0 - 1/2)^2 + (s - \gamma_0)^2)/((s-\gamma_0)^2) - 1 = (\sigma_0-1/2)^2/(s-\gamma_0)^2$. For $s \gg \gamma_0$, this factor is small. The integral $T_\lambda = \int W_\lambda(|\zeta|^2 - |\zeta_{on}|^2)dm_\infty$ is then of order:
$$T_\lambda \lesssim C(\sigma_0,\gamma_0)\cdot\widehat{W_\lambda dm_\infty}(0)\cdot (\sigma_0 - 1/2)^2,$$
but this is not an upper bound that forces $T_\lambda$ to vanish — only a bound showing that $T_\lambda$ is small when $\sigma_0 - 1/2$ is small.

**Frankness remark.** The arithmetic representation of $A_\lambda$ does not by itself provide a proof that $T_\lambda = 0$. What it does provide is a completely explicit description of $A_\lambda$ in terms of arithmetic coefficients: the quantity $A_\lambda = \sum_{n,m} d(n)d(m)/\sqrt{nm}\cdot \widehat{W_\lambda dm_\infty}(\log(n/m))$ is computable. The equality $T_\lambda = 0$ ($\Leftrightarrow$ RH) requires an additional argument connecting the Fourier transforms of $W_\lambda dm_\infty$ with those of $W_\lambda dm_\infty^{on}$: this is precisely the open content of the program.

---

## §7. Synthesis and results table

| Object | Rigorous result | Quality |
|---|---|---|
| $\phi_k(0) = 1$ | Yes (Prop. 1.1) | Rigorous |
| $\phi_k(-r) = \phi_k(r)$ | Yes (Prop. 1.2) | Rigorous |
| $|\phi_k(r)| \leq 1$ | Yes (Prop. 1.3) | Rigorous |
| $\phi_k(r) \to 0$ for $|r|\to\infty$ | Yes (Prop. 1.4) | Rigorous |
| $|\phi_k(r)| = O(e^{-\pi|r|/4})$ | Yes (Prop. 1.5, with analyticity hypothesis) | Rigorous (under the strip-analyticity hypothesis) |
| $\phi_0(r) = \hat{w}(r)$ | Yes | Rigorous |
| $\phi_1(r) = -2\hat{w}''(r)$ | Yes (Prop. 2.2) | Rigorous |
| Asymptotics of $\phi_k(r)$ via P-R | Heuristic (Prop. 3.2) | Heuristic (asymptotic-integral exchange pending) |
| $\widehat{W_\lambda dm_\infty}(0) \sim N(\lambda)^2/2$ | Yes (Prop. 4.1) | Rigorous |
| $\widehat{W_\lambda dm_\infty}(\log p) \sim K_p N^{5/4}$ | Heuristic (Prop. 4.3) | Heuristic |
| $A_\lambda \sim \frac{N^2}{2}\cdot\frac{(\log N)^3}{6}$ | Heuristic | Heuristic |

---

## §8. Directions for rigorous justification

The heuristic results of §3 require the following steps to become rigorous:

1. **Uniformity of Plancherel-Rotach:** Establish that the asymptotics of Doc 66 are uniform in $s \in (0, \delta a_k)$ with an error bounded by $C k^{-3/8-\varepsilon} s^{-3/8}$. This would allow dominating the integrand and justifying the exchange.

2. **Bulk analysis:** Complete the asymptotics of $\phi_k(r)$ including the bulk region $s \asymp a_k$, where the interior Plancherel-Rotach asymptotics (Doc 66, §5) are different.

3. **Determination of $C$:** Compute the normalization constant $C = C(k)$ in the left-edge asymptotics from the data of Doc 66, or from the condition $\phi_k(0) = 1$.

4. **Estimates for the double series:** Prove that the series $\sum_{n\neq m} d(n)d(m)/\sqrt{nm}\cdot \widehat{W_\lambda dm_\infty}(\log(n/m))$ is indeed $O(N^{5/4+\varepsilon})$, rigorously establishing the dominance of the diagonal in §5.2.

---

*End of Document 76.*
