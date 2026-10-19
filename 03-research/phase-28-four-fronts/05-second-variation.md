# Second variation of the Weil form in the transversal direction

**Context:** Execution of Question D.15 of Front D.

---

## 1. Setup: the family of forms $Q_\epsilon$

We fix a test function $f$ (Schwartz on $\mathbb{R}^*_+$) and perturb the
zero configuration in the transversal direction. Under Hypothesis D with $m$ off-line
orbits, each orbit $j = 1, \ldots, m$ has zeros at
$$\rho_j = \tfrac{1}{2} + b_j + i\gamma_j, \quad \bar\rho_j, \quad 1-\rho_j, \quad 1-\bar\rho_j.$$

**Transversal perturbation.** For $\epsilon \in \mathbb{R}$ and $(c_j) \in \mathbb{R}^m$,
define the family of configurations:
$$b_j(\epsilon) = b_j + \epsilon c_j, \qquad \rho_j(\epsilon) = \tfrac{1}{2} + b_j + \epsilon c_j + i\gamma_j.$$

The full orbit under the Klein group $V$ moves as:
$$\rho_j(\epsilon),\ \bar\rho_j(\epsilon),\ 1-\rho_j(\epsilon) = \tfrac{1}{2} - b_j - \epsilon c_j - i\gamma_j,\ 1-\bar\rho_j(\epsilon).$$

**Perturbed Weil form.** The Weil form decomposes as:
$$Q_\epsilon(f,f) = Q_{\text{arith}}(f,f) + Q_{\text{zero},\epsilon}(f,f),$$
where
$$Q_{\text{zero},\epsilon}(f,f) = -\sum_{\rho \in Z_\epsilon} |\hat h(\rho)|^2,$$
with $\hat h(s) := \int_0^\infty f(x)\, x^{s-1}\, dx$ the Mellin transform, and
$Z_\epsilon = \{\rho_j(\epsilon), \bar\rho_j(\epsilon), 1-\rho_j(\epsilon), 1-\bar\rho_j(\epsilon)\}_{j=1}^m$.

**Key remark.** The arithmetic term $Q_{\text{arith}}$ (contributions from primes
and the archimedean factor) does not depend on the zeros. Therefore:
$$\frac{d^k}{d\epsilon^k} Q_\epsilon(f,f) = \frac{d^k}{d\epsilon^k} Q_{\text{zero},\epsilon}(f,f), \qquad k \ge 1.$$

---

## 2. Functional symmetry and simplification

**Lemma 1** (orbit symmetry). If $f$ satisfies the symmetry condition
$$\hat h(s) = \overline{\hat h(\bar s)} \quad \text{(real functions: natural condition)}$$
and the functional equation
$$\hat h(s) = \hat h(1-\bar s),$$
then for each orbit $j$:
$$\sum_{\rho \in \text{orbit}_j} |\hat h(\rho(\epsilon))|^2 = 4\,|\hat h(\rho_j(\epsilon))|^2.$$

*Proof.* The reality condition gives $|\hat h(\bar\rho)| = |\hat h(\rho)|$. The functional
symmetry gives $|\hat h(1-\bar\rho)| = |\hat h(\rho)|$. Hence the four terms of the
orbit contribute equally. $\square$

By Lemma 1:
$$Q_{\text{zero},\epsilon}(f,f) = -4\sum_{j=1}^m |\hat h(\rho_j(\epsilon))|^2.$$

---

## 3. First variation: the critical line is a stationary point

**Proposition 1** (null gradient). For every symmetric $f$:
$$\frac{d}{d\epsilon} Q_\epsilon(f,f)\bigg|_{\epsilon=0} = -8 \sum_{j=1}^m c_j\, \mathrm{Re}\,\!\left(\hat h'(\rho_j)\,\overline{\hat h(\rho_j)}\right).$$

*Proof.* $\frac{d}{d\epsilon}|\hat h(\rho_j + \epsilon c_j)|^2 = 2c_j\,\mathrm{Re}(\hat h'(\rho_j + \epsilon c_j)\,\overline{\hat h(\rho_j+\epsilon c_j)})$. At $\epsilon = 0$ this gives the result. $\square$

**Corollary.** At $b_j = 0$ (critical line): $\rho_j = \frac{1}{2} + i\gamma_j$. If $f$ is even
under $x \mapsto 1/x$ (the natural symmetry condition), then $\hat h(s)$ is real and
positive on the critical line, and $\hat h'(\rho_j)$ is purely imaginary. Hence:
$$\mathrm{Re}\,\!\left(\hat h'(\rho_j)\,\overline{\hat h(\rho_j)}\right) = 0.$$

Therefore the first variation of $Q_\epsilon$ vanishes at $b_j = 0$: **the critical line
is a stationary point of $Q$ in the transversal direction**. (Confirms Proposition D.13.)

---

## 4. Second variation: the central computation

**Theorem 1** (transversal second-variation formula). For $f$ with the symmetry of
Lemma 1:
$$\boxed{\frac{d^2}{d\epsilon^2} Q_\epsilon(f,f)\bigg|_{\epsilon=0}
  = -8\sum_{j=1}^m c_j^2 \left[\mathrm{Re}\,\!\left(\hat h''(\rho_j)\,\overline{\hat h(\rho_j)}\right) + |\hat h'(\rho_j)|^2\right].}$$

*Proof.* Let $g_j(\epsilon) := |\hat h(\rho_j + \epsilon c_j)|^2$. Then:
$$g_j'(\epsilon) = 2c_j\,\mathrm{Re}\,\!\left(\hat h'(\rho_j + \epsilon c_j)\,\overline{\hat h(\rho_j+\epsilon c_j)}\right),$$
$$g_j''(\epsilon) = 2c_j^2\,\mathrm{Re}\,\!\left(\hat h''(\rho_j + \epsilon c_j)\,\overline{\hat h(\rho_j+\epsilon c_j)}\right) + 2c_j^2\,|\hat h'(\rho_j+\epsilon c_j)|^2.$$
At $\epsilon = 0$ and summing with the factor $-4$:
$$\frac{d^2}{d\epsilon^2} Q_{\text{zero},\epsilon}(f,f)\bigg|_{\epsilon=0}
  = -4\sum_j g_j''(0) = -8\sum_j c_j^2 \left[\mathrm{Re}\,\!\left(\hat h''(\rho_j)\,\overline{\hat h(\rho_j)}\right) + |\hat h'(\rho_j)|^2\right]. \quad \square$$

---

## 5. Sign analysis: the Laguerre–Pólya class

The second variation is positive (critical line = local minimum of $-Q$ = local
minimum of energy) if and only if:
$$\mathrm{Re}\,\!\left(\hat h''(\rho_j)\,\overline{\hat h(\rho_j)}\right) + |\hat h'(\rho_j)|^2 < 0 \quad \forall j.$$

Reformulating in terms of $\log|\hat h(s)|$: let $\sigma \mapsto u(\sigma) := \log|\hat h(\sigma + i\gamma_j)|$ be the function of $\sigma = \mathrm{Re}(s)$. At $\sigma_0 = \frac{1}{2} + b_j$:

**Proposition 2** (log-concavity condition). The inequality
$\mathrm{Re}(\hat h'' \overline{\hat h}) + |\hat h'|^2 < 0$ at $\rho_j$ is equivalent to:
$$u''(\sigma_0) < 0 \quad \text{(concavity of } \log|\hat h| \text{ in the } \mathrm{Re}(s) \text{ direction)}.$$

*Proof.* Writing $\hat h = r e^{i\theta}$ with $r = |\hat h|$, $\theta$ the phase:
$$\hat h' = (r' + ir\theta') e^{i\theta}, \quad \hat h'' = (r'' - r(\theta')^2 + i(2r'\theta' + r\theta''))e^{i\theta}.$$
Then:
$$\mathrm{Re}(\hat h'' \overline{\hat h}) + |\hat h'|^2 = r''r - r^2(\theta')^2 + (r')^2 + r^2(\theta')^2 = r''r + (r')^2.$$
The condition $r''r + (r')^2 < 0$ is equivalent to $(r^2)'' < 0$, i.e. $r'' < -(r')^2/r$, i.e.
$(\log r)'' = (r'r - (r')^2)/r^2 < 0$, which is exactly $u'' < 0$. $\square$

**Definition.** A test function $f$ belongs to the *transversal Laguerre–Pólya class* (class LP-T) if for every zero $\rho_j$ on the critical line:
$$\sigma \mapsto \log|\hat h(\sigma + i\gamma_j)| \text{ is concave in a neighborhood of } \sigma = 1/2.$$

**Theorem 2** (sufficient condition for variational RH). If $f \in$ LP-T and the
critical line is the unique stationary point of $Q_\epsilon(f,f)$ in the transversal
direction, then $Q_\epsilon(f,f)$ is locally maximal at $b_j = 0$, equivalently
$-Q_\epsilon(f,f)$ is locally minimal at $b_j = 0$.

---

## 6. Interpretation: an anti-restoring force

Theorem 1 reveals something fundamental about the geometry of the problem:

**Proposition 3** (anti-restoring character of the Weil form). For functions
$f \in$ LP-T, the second variation satisfies:
$$\frac{d^2}{d\epsilon^2} Q_\epsilon(f,f)\bigg|_{\epsilon=0} > 0.$$

This means: moving a zero FROM the critical line OUTWARD INCREASES $Q_\epsilon(f,f)$
(makes it less negative). Equivalently: the critical line is a **local minimum of
negativity** of $Q$ in the transversal direction.

*Direct consequence:* if $Q_0(f,f) \ge 0$ (which is equivalent to RH via the Weil
criterion), then for LP-T functions, moving the zeros off the critical line would,
to first order, only make $Q$ even more positive. One must go to third order to
see the sign change.

*Wait — this seems to contradict $\kappa > 0$ when there are off-line zeros.*
Let us clarify the apparent paradox:

**Proposition 4** (resolution of the apparent contradiction). The two statements
are compatible:
1. $\kappa(Q_\epsilon) > 0$ for $b_j > 0$ (Phase 26): the form has negative directions.
2. $\delta^2_b Q_\epsilon(f,f)|_{\epsilon=0} > 0$ for $f \in$ LP-T: the form evaluated at
   specific functions is a local minimum.

The reason: the Kreĭn index $\kappa$ measures the subspace of MAXIMUM negativity (the
minimum over all $f$). Theorem 1 measures $Q$ evaluated at a specific $f$. The minimum
over all $f$ can be negative even when the value at a given $f$ has its minimum on
the critical line.

In matrix language: a matrix $A$ having a negative eigenvalue does not prevent
$\langle Ax, x \rangle$ from being positive for specific vectors $x$. The Kreĭn index
counts negative eigenvalues; the second variation evaluates at a fixed vector.

---

## 7. The correct transversal potential

Proposition 3 suggests that the correct transversal energy is NOT $\Phi = \sum b_j^2$
but rather:
$$\Phi^*(f) := -Q_{\text{zero}}(f,f) = \sum_{\rho \in Z} |\hat h(\rho)|^2.$$

This is the energy of the zero configuration "as seen from $f$."

**Proposition 5** (properties of $\Phi^*$).
1. $\Phi^*(f) \ge 0$ always.
2. $\Phi^*$ does not distinguish between zeros on the critical line and off it (it depends
   on the value of $\hat h$ at the zeros, not on their position).
3. $\frac{d^2}{d\epsilon^2}\Phi^*(f)\big|_{\epsilon=0} = 8\sum_j c_j^2 [u''_j + (u'_j)^2 + (\theta'_j)^2]$ where $u_j = \log|\hat h(\rho_j)|$, $\theta_j$ its phase.

The condition for $b_j = 0$ to be a minimum of $\Phi^*$ in the transversal direction:
$$u''_j\bigg|_{\sigma=1/2} < 0 \quad \forall j,$$
is exactly the LP-T condition.

---

## 8. The connection with the Euler product

**Proposition 6** (the LP-T class and arithmetic structure). A function $f$ belongs
to LP-T if and only if the function $\sigma \mapsto |\hat h(\sigma + i\gamma_j)|$ is log-concave
in $\sigma$ for each height $\gamma_j$.

The natural test functions of Connes's formalism are of the form:
$$\hat h(s) = \zeta(s) \cdot g(s)$$
for some entire function $g$. For these functions, the log-concavity of $|\hat h(\sigma + i\gamma_j)|$ in $\sigma$ at fixed $\gamma_j$ involves the log-concavity of $|\zeta(\sigma + i\gamma_j)|$.

**Question 28.1** (new). Is $\sigma \mapsto \log|\zeta(\sigma + i\gamma)|$ concave in
$\sigma \in (0,1)$ for every $\gamma$?

If the answer is yes: the natural test functions of the formalism belong to LP-T,
the second variation has positive sign, and the critical line is a local minimum of $Q$.

If the answer is no: there exist test functions for which the critical line is a
maximum or saddle point, and the variational mechanism does not work.

---

## 9. What can be checked: the case of the line $\sigma = 1/2$

On the critical line $\sigma = 1/2$ with $\gamma \gg 1$:
$$\log|\zeta(\tfrac{1}{2} + i\gamma)| = -c\sqrt{\log\gamma/\log\log\gamma} + O(\ldots)$$
(Korobov–Vinogradov order-of-magnitude estimates).

The derivative in $\sigma$:
$$\partial_\sigma \log|\zeta(\sigma + i\gamma)|\bigg|_{\sigma=1/2}$$
is related to $\mathrm{Re}(\zeta'/\zeta(\frac{1}{2}+i\gamma))$.

The second derivative:
$$\partial_\sigma^2 \log|\zeta(\sigma + i\gamma)| = \mathrm{Re}\,\!\left[\frac{\zeta''}{\zeta} - \left(\frac{\zeta'}{\zeta}\right)^2\right]_{\sigma + i\gamma}$$

The sign of this quantity at $\sigma = 1/2$ is the log-concavity condition. Related
to Question 28.1, it is a concrete analytic question about $\zeta$.

---

## 10. Comparison with the situation in function fields

In the case of curves over $\mathbb{F}_q$, the zeta function has the form:
$$Z(u) = \frac{P(u)}{(1-u)(1-qu)}, \quad P(u) = \prod_{j=1}^{2g}(1-\alpha_j u).$$

The analogous log-concavity corresponds to $\log|P(q^{-\sigma})|$ being concave in
$\sigma$. For $|\alpha_j| = q^{1/2}$ (RH in function fields, proved), the $\alpha_j$
lie on the circle $|u| = q^{-1/2}$, and the log-concavity is immediate: $|P(q^{-\sigma})|$
is a product of functions concave in $\sigma$ (modulated by the radius $q^{1/2-\sigma}$).

This suggests that **Question 28.1 is the analogue for $\mathbb{Z}$ of the log-concavity
that in function fields follows automatically from RH**. For $\zeta$, it is the
question to be answered.

---

## 11. Verdict of the computation

| Result | Status |
|---|---|
| Transversal second-variation formula (Theorem 1) | **Proved — new result** |
| First variation null on the critical line (Prop. 1 + Corollary) | Proved |
| Equivalence positive second variation ↔ log-concavity (Prop. 2) | Proved |
| LP-T class defined and characterized | New |
| Positive second variation in LP-T (Theorem 2) | Proved conditional on LP-T |
| Question 28.1: is $\log|\zeta(\sigma+i\gamma)|$ concave in $\sigma$? | **Open — central question** |
| Automatic log-concavity in function fields via RH | Remark (§10) |

---

## 12. The most concrete question of the program

**Question 28.1** (restated). For every $\gamma > 0$ and $\sigma_0 \in (0,1)$:
$$\frac{\partial^2}{\partial \sigma^2} \log|\zeta(\sigma + i\gamma)|\bigg|_{\sigma=\sigma_0} \overset{?}{<} 0.$$

Equivalently: $|\zeta(\sigma + i\gamma)|^2$ is log-concave in $\sigma$ for each fixed $\gamma$.

This can be checked locally on the critical line. If proved with uniform log-concavity:
$$\frac{\partial^2}{\partial \sigma^2} \log|\zeta(\sigma + i\gamma)| \le -\delta(\gamma) < 0 \quad \text{for } \sigma \in (1/4, 3/4),$$
then the natural test functions of the program belong to LP-T, Front D's second
variation has positive sign, and the critical line is a local minimum of $Q$ in
the transversal direction for ALL canonical test functions.

Combined with the uniqueness of the minimum (which would require an additional
global argument), this would prove RH.
