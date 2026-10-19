# Phase 26-A — Direct attack on V.2: the heart of the bridge

**Thesis:** V.2 is not a verification item. It is the main objective of Phase 26.

If V.2 falls, the bridge does not exist in the proposed form.
If V.2 survives, Phase 26 becomes a serious direction.

---

## 0. The precise question of V.2

Let $\rho_j = (1/2 + b_j) + i\gamma_j$ be a zero of $\zeta$ off the critical line ($b_j > 0$).

**V.2:** There exists a vector $f_j$ in the Kreĭn space $\mathcal{K}$ such that $H_C f_j = \lambda_j f_j$
with $\lambda_j \in \mathbb{C}$, $\text{Im}(\lambda_j) \neq 0$, and $\lambda_j$ determined by $\rho_j$.

The natural candidate for $f_j$ is the character $f_j(x) = x^{\rho_j - 1/2} = x^{b_j + i\gamma_j}$.

---

## 1. The stress test: V.2 without mentioning RH

Before connecting with $\zeta$ and $\rho_j$, we formulate the abstract question:

**Abstract question (V.2-abs):** Let $(\mathcal{K}, Q)$ be a Pontryagin space with
neg.ind$(Q) = \kappa < \infty$ and let $T$ be a $Q$-self-adjoint operator on $\mathcal{K}$. Does
$T$ have exactly $\kappa$ pairs of non-real eigenvalues $\{\mu_j, \bar\mu_j\}$?

**Known answer:** The Kreĭn–Langer spectral theorem (1963, 1978) gives:

> $T$ has **at most** $\kappa$ pairs of non-real eigenvalues.

The exact count is NOT automatic from the abstract theory.

**Direct consequence for Phase 26:**

- The bridge obtains the direction "at most 2m complex eigenvalues" automatically.
- The direction "exactly 2m" requires specific structure of the operator $H_C$ and of the space $\mathcal{K}$.

This distinction is crucial: the abstract inequality is free; the equality is the real work.

---

## 2. The Kreĭn–Langer theorem applied to $H_C$

**Theorem 26-A.1** (Kreĭn–Langer, cf. Azizov–Iokhvidov 1989, §2.3). Let $T$ be a
$Q$-self-adjoint operator on a Pontryagin space $(\mathcal{K}, Q)$ with neg.ind$(\mathcal{K}) = \kappa$.
Then:

**(i)** The non-real spectrum of $T$ consists of at most $\kappa$ pairs of complex eigenvalues
$\{\mu_j, \bar\mu_j\}_{j=1}^{r}$ with $r \leq \kappa/2$.

**(ii)** The essential spectrum $\sigma_{ess}(T) \subseteq \mathbb{R}$.

**(iii)** The eigenvectors associated with $\mu_j$ and $\bar\mu_j$ are $Q$-orthogonal to each other and
to the real spectrum.

**Corollary 26-A.2.** If the Bridge Theorem (Conjecture 26-C.2) holds, then
automatically the bound $r \leq m$ (number of off-line orbits).

*The hard direction is $r \geq m$: that there exist AT LEAST $m$ pairs of non-real eigenvalues.*

---

## 3. The obstacle for "exactly $\kappa$"

To prove $r = m$ (equal instead of at most), we need:

**For each orbit $j = 1, \ldots, m$:**

There exists $f_j \in \mathcal{K}$ such that $H_C f_j = \lambda_j f_j$ with $\text{Im}(\lambda_j) \neq 0$.

This $f_j$ needs to:
1. **Be in $\mathcal{K}$** (in the Pontryagin space defined by $Q$).
2. **Be a genuine eigenvector** (not merely a generalized eigenfunction, not merely a resonance).
3. **Have an eigenvalue determined by $\rho_j$** (the connection with the zero of $\zeta$).

---

## 4. The central obstacle: the characters are NOT in $L^2(C_\mathbb{Q})$

The natural candidate $f_j(x) = x^{b_j + i\gamma_j}$ (a character of $\mathbb{R}^*_+$) formally satisfies:
$$(H_C f_j)(x) = -ix\partial_x(x^{b_j + i\gamma_j}) = -i(b_j + i\gamma_j) x^{b_j + i\gamma_j}
= (\gamma_j - ib_j) f_j(x).$$

With Connes's convention where on-line zeros appear as $\rho - 1/2 = i\gamma$ (purely
imaginary), the eigenvalue $\lambda_j = \gamma_j - ib_j$ has $\text{Im}(\lambda_j) = -b_j \neq 0$.
Consistent.

**But $f_j \notin L^2(C_\mathbb{Q})$.**

*Proof.* On $\mathbb{R}^*_+$ with measure $dx/x$:
$$\|f_j\|_{L^2}^2 = \int_0^\infty |x^{b_j + i\gamma_j}|^2 \frac{dx}{x} = \int_0^\infty x^{2b_j} \frac{dx}{x}
= \int_0^\infty x^{2b_j - 1} dx = \infty.$$

The character has no decay and is not square-integrable. $\square$

**Consequence:** $f_j$ is a generalized function (distribution), not a vector of $L^2(C_\mathbb{Q})$.
In classical operator theory, this corresponds to continuous spectrum (not an eigenvalue).

---

## 5. Two resolution strategies

### Strategy A: Distributional completion

Define $\mathcal{K}$ not as $L^2(C_\mathbb{Q})$ with inner product $Q$, but as a distributional extension
that includes the characters $f_j$ as vectors (in the sense of Gel'fand–Shilov: a rigged
Hilbert triple).

*Precision:* Let $\Phi \subset L^2(C_\mathbb{Q}) \subset \Phi'$ be a rigged triple where:
- $\Phi$ = test functions with rapid decay on $C_\mathbb{Q}$,
- $\Phi'$ = tempered distributions on $C_\mathbb{Q}$.

If $f_j \in \Phi'$, then the pair $(\Phi, Q)$ may have a Pontryagin completion that includes $f_j$.

**Obstacle:** The form $Q$ on $\Phi'$ involves the Weil formula with all its terms (sum
over zeros + sum over primes), and its distributional extension needs careful regularization.

### Strategy B: Weil localization

Do not work with $f_j$ as a global vector, but with its "localized projection":
$$f_j^{(T_0, \sigma)}(x) = f_j(x) \cdot \phi_{T_0, \sigma}(x)$$
where $\phi_{T_0, \sigma}$ is a cutoff function centered near $\gamma_j$ (a Hermite-Gauss
window from the main program).

$f_j^{(T_0, \sigma)} \in L^2(C_\mathbb{Q})$ if $\phi_{T_0, \sigma}$ has sufficient decay.

**Question:** Is $f_j^{(T_0, \sigma)}$ an "approximate eigenvector" of $H_C$ with eigenvalue
close to $\gamma_j - ib_j$?

That is: does $(H_C - (\gamma_j - ib_j))f_j^{(T_0, \sigma)} \to 0$ in some norm as $\sigma \to \infty$?

This question connects Phase 26 with the main program (the localized Weil form of the main arc).

---

## 6. What the form $Q$ says about $f_j$

**Computation of $Q(f_j, f_j)$ (formal).** By definition:
$$Q(f_j, f_j) = \mathcal{W}(f_j * \tilde{f}_j).$$

The Mellin convolution $f_j * \tilde{f}_j$ has Mellin transform:
$$\widehat{f_j * \tilde{f}_j}(s) = \hat{f}_j(s) \cdot \hat{\tilde{f}}_j(s).$$

With $f_j(x) = x^{b_j + i\gamma_j}$:
$$\hat{f}_j(s) = \int_0^\infty x^{b_j+i\gamma_j} x^{s-1} dx.$$
This integral diverges (there is no decay). Formally, if regularized:
$$\hat{f}_j(s) \sim \delta(s - (b_j + i\gamma_j)) \quad (\text{in the distributional sense}).$$

Then:
$$\mathcal{W}(f_j * \tilde{f}_j) \sim \sum_\rho \hat{f}_j(\rho) \hat{\tilde{f}}_j(\rho) \sim \sum_\rho \delta(\rho - (b_j+i\gamma_j)) \cdot \overline{\delta(\rho - (b_j+i\gamma_j))}.$$

The dominant term is $\rho = \rho_j = (1/2+b_j)+i\gamma_j$:

$$Q(f_j, f_j) \sim |\hat{f}_j(\rho_j)|^2 = |\delta(\rho_j - (b_j+i\gamma_j))|^2.$$

The argument: $\rho_j - (b_j + i\gamma_j) = 1/2 \neq 0$ (no cancellation).

**Technical remark:** The zero of $\zeta$ at $\rho_j$ appears in the sum $\sum_\rho$ of $\mathcal{W}$,
but the character $f_j$ is centered at $b_j + i\gamma_j$, which differs from $\rho_j$ by $1/2$.

In Connes's parametrization where the scaling operator acts by $s \to s - 1/2$, the
difference disappears. The correct convention is:

$$f_j(x) = x^{\rho_j - 1/2} = x^{b_j + i\gamma_j} \quad \text{(on the central line } s = 1/2\text{)}.$$

With this convention: $\hat{f}_j(s) \sim \delta(s - \rho_j)$ in the adelic parametrization.

Then $\mathcal{W}(f_j * \tilde{f}_j)$ picks up the term $\rho = \rho_j$ of the sum, which is
$|\hat{f}_j(\rho_j)|^2$. But $\hat{f}_j(\rho_j) = \int_0^\infty x^{b_j+i\gamma_j} x^{\rho_j-1} dx
= \int_0^\infty x^{\rho_j-1/2+\rho_j-1}dx$ — which diverges.

**Conclusion of the formal computation:** $Q(f_j, f_j)$ is formally divergent. The character $f_j$
is a **distributional-isotropic** vector — not in the sense $Q(f_j,f_j)=0$, but in the sense
that the form $Q$ is not well defined on $f_j$ in the $L^2$ space.

---

## 7. Precise diagnosis of the obstruction

The obstacle has three layers:

**Layer 1 (easy):** The Kreĭn–Langer theorem gives "at most $\kappa$" automatically.
There is nothing to prove here given that $H_C$ is $Q$-symmetric.

**Layer 2 (hard):** For "at least $\kappa$", we need the characters $f_j$ to be
genuine eigenvectors of $H_C$ in some extension of $L^2(C_\mathbb{Q})$ that includes $f_j$.

**Layer 3 (fundamental):** The characters $f_j$ are NOT in $L^2(C_\mathbb{Q})$ and the form $Q$ is
not well defined on them. The distributional extension is the central technical problem.

---

## 8. The correct reformulation of V.2

Strategy A (distributional completion) suggests the following reformulation:

**V.2 reformulated:** Let $\mathcal{K}^+ = (\Phi', Q_{reg})$ be the distributional extension of the
Pontryagin space $\mathcal{K}$, where $Q_{reg}$ is the regularization of the Weil form
on distributions. Then:

**(a)** The characters $f_j = x^{\rho_j - 1/2}$ are in $\mathcal{K}^+$.

**(b)** $H_C f_j = \lambda_j f_j$ in $\mathcal{K}^+$ with $\lambda_j = \gamma_j - ib_j$.

**(c)** $Q_{reg}(f_j, f_j)$ is finite (possibly 0, giving an isotropic vector).

This requires:
1. Defining $Q_{reg}$ rigorously on tempered distributions.
2. Verifying that the completion $\mathcal{K}^+$ inherits the Kreĭn index $\kappa$.
3. Computing $H_C f_j$ and $Q_{reg}(f_j, f_j)$ explicitly.

---

## 9. The connection with the main arc of the program

Strategy B (localization) suggests that V.2 is directly connected to the results
of v8/v9 of the main arc:

**The localized Weil form** $Q_{T_0, \sigma, J}$ of the main arc is (formally) the
compression of $Q$ to a Hermite-Gauss basis centered at $T_0 = \gamma_j$, width $\sigma$.

If $\sigma \to \infty$ (complete basis), the compression converges to full $Q$.

The localized eigenvector $f_j^{(T_0, \sigma)}$ should satisfy:
$$Q_{T_0, \sigma, J}(f_j^{(T_0,\sigma)}, \cdot) \approx \lambda_j Q_{T_0,\sigma,J}(\cdot, \cdot).$$

This is precisely the behavior that the main arc measures numerically: the negativity
$\lambda_{\min}(Q_{T_0, \sigma, J}) < 0$ when there is an off-line zero near $T_0$.

**Working hypothesis:** the eigenvector $f_j$ (in the distributional sense) is the limit of
the localized vectors $f_j^{(T_0, \sigma)}$ as $\sigma \to \infty$, and the negativity of
$\lambda_{\min}(Q_{T_0, \sigma, J})$ is the "localized footprint" of the complex eigenvalue
$\lambda_j$ of $H_C$ on $\mathcal{K}^+$.

This hypothesis, if formalized, would directly connect the main arc and the Kreĭn arc.

---

## 10. Status and verdict on V.2

| Component | Status |
|---|---|
| "At most κ non-real eigenvalues" (Kreĭn–Langer) | **Available for free** if $H_C$ is $Q$-symmetric |
| Candidate eigenvector $f_j = x^{b_j+i\gamma_j}$ | Candidate identified; NOT in $L^2(C_\mathbb{Q})$ |
| Eigenvalue $\lambda_j = \gamma_j - ib_j$ | Formally correct; requires a precise convention |
| $Q(f_j, f_j)$ well defined | Divergent in $L^2$; requires regularization or extension |
| "At least κ non-real eigenvalues" | **NOT proved; requires distributional completion** |
| Connection with the main arc | Working hypothesis; not formalized |

**Verdict:** V.2 CANNOT be classified as a "technical verification item". It is the main
objective of Phase 26-A. The obstacles are real (distributional extension of $Q$, non-$L^2$ nature of $f_j$)
and are not minor workarounds.

**The most direct path to V.2:**

1. Define the regularization $Q_{reg}$ on tempered distributions (following Weil/Burnol).
2. Verify that the characters $f_j = x^{b_j+i\gamma_j}$ have $Q_{reg}(f_j, f_j) < \infty$.
3. Compute $H_C f_j$ in the distributional sense.
4. If steps 2–3 succeed: V.2 is proved for the distributional extension.
5. If step 2 fails (divergence): the bridge requires reformulation (Strategy B — localization).

---

## 11. What remains after V.2

If V.2 is proved via Strategy A (distributional completion):

- V.1 ($Q$-symmetry of $H_C$) becomes the next problem. It also requires real work.
- V.3 (Kreĭn index = κ) is a consequence of the Kreĭn–Langer theorem + V.2.
- V.4 (orbit count) is algebraic once V.2 and V.3 are available.

If V.2 fails:

- The bridge in the form of Theorem 26-C.2 is incorrect.
- Diagnosis: the Kreĭn ↔ Connes connection requires the localized form (Strategy B).
- Reformulation: the main arc (v8/v9) IS the Pontryagin arc in local version.

Neither of the two outcomes is a failure. Both are precise.
