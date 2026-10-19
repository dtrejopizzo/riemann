# Doc 91 — Direction B: Pontryagin space and the negative index of $H_C$

**Phase:** 34 — New directions  
**Context:** Blockage of the CCM direction (Hadamard barrier, Docs 88–90); exploration of Direction B based on operator theory in Pontryagin/Kreĭn spaces.  
**Absolute rule:** No proof of RH will be fabricated. If an argument does not close, this will be stated explicitly.

---

## Executive summary

Direction B seeks to prove $\mathrm{neg.ind}(H_C) = 0$ using tools from operator theory in Pontryagin spaces, without requiring prior knowledge of the positions of the zeros of $\zeta$. This document:

1. Rigorously reconstructs the Pontryagin space $(\mathcal{K}, Q)$ and the operator $H_C$ of Phase 26.
2. Reviews the relevant Pontryagin, Kreĭn–Langer, and Azizov–Iokhvidov theorems.
3. Analyzes the functional symmetry of $\zeta$ as a spectral constraint on $H_C$.
4. Studies lower semiboundedness as a route to zero negative index.
5. Examines the analogue of the Livsic characteristic function in Pontryagin spaces.
6. Formulates the precise obstacle blocking each route.
7. Concludes with a frank evaluation of whether a genuinely new route exists.

**Main result of the analysis:** Every known route in Direction B reduces to a condition equivalent to knowledge of the zeros of $\zeta$ (directly or via the square-root barrier of Opt-B). Direction B is not blocked in principle, but no standard tool from Pontryagin/Kreĭn operator theory closes the argument without assuming information equivalent to RH.

---

## Part I — Construction of the Pontryagin space $(\mathcal{K}, Q)$

### Section 1.1 — The ambient space and the Weil form

Let $\mathcal{S}(\mathbb{R}^*_+)$ be the Schwartz space of test functions on $\mathbb{R}^*_+ = (0,\infty)$ with multiplicative measure $dx/x$. For $f \in \mathcal{S}(\mathbb{R}^*_+)$ the Mellin transform is defined as:
$$\hat{f}(s) = \int_0^\infty f(x) x^s \frac{dx}{x}, \qquad s \in \mathbb{C}.$$

The **completed zeta function** is:
$$\xi(s) = \frac{1}{2} s(s-1) \pi^{-s/2} \Gamma(s/2) \zeta(s),$$
which satisfies the functional equation $\xi(s) = \xi(1-s)$ and is entire of order 1.

**Definition 1.1 (Weil–Connes form).** For $f, g \in \mathcal{S}(\mathbb{R}^*_+)$, the linear Weil form is:
$$\mathcal{W}(h) = \sum_\rho \hat{h}(\rho) + \hat{h}(0) \left(\frac{1}{2}\log\pi - \frac{\gamma}{2}\right) + \hat{h}(1)\left(\frac{1}{2}\log\pi - \frac{\gamma}{2}\right) - \sum_{p \text{ prime}} \sum_{n=1}^\infty \frac{\log p}{p^{n/2}} \left[ h(p^n) + h(p^{-n}) \right],$$
where $\rho$ runs over the non-trivial zeros of $\zeta$, $\gamma$ is the Euler–Mascheroni constant, and the sum over primes converges conditionally in the sense of Schwartz.

In more compact notation (cf. Weil 1952, Connes 1999):
$$\mathcal{W}(h) = \sum_{\rho} \hat{h}(\rho) - \sum_p \sum_{n \geq 1} \frac{\log p}{p^{n/2}} \left[h(p^n) + h(p^{-n})\right] + (\text{archimedean terms}),$$
where the archimedean terms come from the gamma factor.

**Definition 1.2 (Weil quadratic form).** The hermitian form on $\mathcal{S}(\mathbb{R}^*_+)$ is:
$$Q(f, g) = \mathcal{W}(f \star \tilde{g}),$$
where the multiplicative convolution is $(f \star g)(x) = \int_0^\infty f(y) g(x/y) dy/y$ and the multiplicative adjoint is $\tilde{g}(x) = \overline{g(1/x)} / x$.

**Remark 1.3.** The Mellin transform of $f \star \tilde{g}$ is $\hat{f}(s) \overline{\hat{g}(\bar{s})}$, so that:
$$Q(f,g) = \sum_\rho \hat{f}(\rho) \overline{\hat{g}(\bar\rho)} - \sum_{p,n} \frac{\log p}{p^{n/2}} (f \star \tilde{g})(p^n) + (\text{archim.}).$$

---

### Section 1.2 — The Weil theorem and the Kreĭn index

The fundamental result of Weil (1952) in modern language is:

**Theorem 1.4 (Weil 1952, Connes 1999).** $Q(f,f) \geq 0$ for all $f \in \mathcal{S}(\mathbb{R}^*_+)$ if and only if the Riemann Hypothesis is true.

This theorem turns the positivity of $Q$ into a reformulation of RH. Our interest is to quantify the degree of non-positivity when RH is unknown.

**Definition 1.5 (Negative index of the form).** Let $V$ be a vector space with hermitian form $Q$. The **negative index** of $Q$ is:
$$\kappa(Q) = \sup \left\{ \dim W : W \subset V, \, Q|_W < 0 \right\},$$
where $Q|_W < 0$ means that the restricted form is negative definite.

**Proposition 1.6 (Connection with zeros of $\zeta$).** If $\zeta$ has exactly $m$ orbits of zeros off the critical line (under the symmetry $s \mapsto 1-\bar{s}$, each orbit contains 4 zeros, but the functional equation $\xi(s)=\xi(1-s)$ reduces the count to $2m$ conjugate pairs), then:
$$\kappa(Q) = 2m.$$

In particular, $\kappa(Q) = 0 \iff \text{RH}$.

*Proof sketch.* Each zero $\rho_j = \sigma_j + i\gamma_j$ with $\sigma_j \neq 1/2$ contributes a pair $\{\rho_j, 1-\rho_j\}$ (by the functional equation, with $1-\rho_j = (1-\sigma_j) + i\gamma_j$) and also $\{\bar\rho_j, 1-\bar\rho_j\}$ (by reflection). The convolution $f_j \star \tilde{f}_j$ has a Mellin transform that touches these zeros. A residue computation (cf. Burnol 2002) shows that each pair of off-line zeros produces exactly one negative direction of $Q$. The rigorous proof requires the distributional analysis of $\mathcal{W}$ on test functions that approximate characters, and is incomplete in the current framework of Phase 26 (see item V.2 of Phase 26). $\square$ (partial)

---

### Section 1.3 — Construction of the Pontryagin space

To go from the form $Q$ on $\mathcal{S}(\mathbb{R}^*_+)$ to a Pontryagin space, three steps are needed.

**Step 1: The isotropic subspace.** Let $N = \ker Q = \{f \in \mathcal{S} : Q(f,g) = 0 \; \forall g\}$ be the subspace of $Q$-degenerate vectors. It is conjectured (a result pending from Phase 26) that $\dim N < \infty$.

**Step 2: The quotient space.** Let $\mathcal{S}/N$ be the quotient space. The form $Q$ descends to a non-degenerate form $\tilde{Q}$ on $\mathcal{S}/N$.

**Step 3: The completion.** Let $(\mathcal{K}, Q)$ be the completion of $(\mathcal{S}/N, \tilde{Q})$ in the sense of the canonical topology of a Pontryagin space. This completion exists and is unique (modulo unitary isometry) when the negative index is finite, by the Iokhvidov–Kreĭn theorem (1956).

**Definition 1.7 (Weil–Connes Pontryagin space).** The **Weil–Connes Pontryagin space** is the pair $(\mathcal{K}, Q)$ constructed via the three steps above, with negative index:
$$\kappa = \kappa(Q) = \mathrm{neg.ind}(\mathcal{K}).$$

**Warning 1.8.** The construction of $\mathcal{K}$ as a genuine Pontryagin space (i.e., verifying that the negative index is finite, $\kappa < \infty$) is equivalent to $\zeta$ having only finitely many zeros off the critical line. This fact is not proved. Therefore, throughout the document we work **under the working hypothesis** $\kappa < \infty$ (which is a strictly weaker result than RH but is also open).

---

### Section 1.4 — The operator $H_C$

**Definition 1.9 (Connes–Weil operator).** Let $C_\mathbb{Q} = \mathbb{A}_\mathbb{Q}^*/\mathbb{Q}^*$ be the idèle class group of the field $\mathbb{Q}$, where $\mathbb{A}_\mathbb{Q}$ are the adèles. Let $H = L^2(C_\mathbb{Q}, d\mu)$ with Haar measure $d\mu$.

The group $\mathbb{R}^*_+$ acts isometrically on $H$ by:
$$(U_\lambda f)(x) = f(\lambda^{-1} x), \quad \lambda \in \mathbb{R}^*_+, \; f \in H.$$

The **Connes–Weil operator** $H_C$ is the infinitesimal generator of this unitary representation:
$$H_C = \frac{1}{i} \left.\frac{d}{d\lambda}\right|_{\lambda=1} U_\lambda.$$

On differentiable functions: $(H_C f)(x) = -i x \partial_x f(x)$ (Euler operator multiplied by $-i$).

**Proposition 1.10 (Formal symmetry of $H_C$ with respect to $Q$).** If the action of $U_\lambda$ preserves $Q$, i.e., $Q(U_\lambda f, U_\lambda g) = Q(f,g)$ for all $\lambda \in \mathbb{R}^*_+$, then $H_C$ is $Q$-symmetric: $Q(H_C f, g) = Q(f, H_C g)$ for $f, g$ in the domain.

*Proof.* Differentiating $Q(U_\lambda f, U_\lambda g) = Q(f,g)$ at $\lambda = 1$:
$$\frac{d}{d\lambda}\bigg|_{\lambda=1} Q(U_\lambda f, U_\lambda g) = Q\left(\frac{dU_\lambda}{d\lambda}\bigg|_{\lambda=1} f, g\right) + Q\left(f, \frac{dU_\lambda}{d\lambda}\bigg|_{\lambda=1} g\right) = 0.$$
Since $\frac{dU_\lambda}{d\lambda}|_{\lambda=1} = i H_C$, we obtain $Q(iH_C f, g) + Q(f, iH_C g) = 0$, which is $Q$-symmetry. $\square$

**Status of item V.1 (Phase 26).** The $Q$-invariance of $U_\lambda$ (and hence the $Q$-symmetry of $H_C$) **is not proved**. It requires verifying that the Weil form $\mathcal{W}(f \star \tilde{g})$ is invariant under the multiplicative change of variable $f \mapsto U_\lambda f$. The arithmetic term of $Q$ transforms the evaluation arguments at the primes: $(U_\lambda f \star \widetilde{U_\lambda g})(p^n) = (f \star \tilde{g})(\lambda^{-1} p^n)$, which does not obviously preserve $Q$.

**Definition 1.11 ($Q$-selfadjoint in $\mathcal{K}$).** Once $\mathcal{K}$ is constructed (as a Pontryagin space) and $H_C$ is densely defined in $\mathcal{K}$, $H_C$ is said to be **$Q$-selfadjoint** if:
1. $Q(H_C f, g) = Q(f, H_C g)$ for $f,g$ in the domain (symmetry), and
2. The operator is maximally $Q$-symmetric (it has no proper $Q$-symmetric extensions in $\mathcal{K}$).

In Pontryagin theory, condition (2) is automatic for operators with non-empty resolvent, but it requires verification in each concrete case.

---

## Part II — Pontryagin, Kreĭn, and Langer theorems

### Section 2.1 — Pontryagin spaces: definition and basic properties

**Definition 2.1 (Pontryagin space).** A **Pontryagin space of index $\kappa$**, denoted $\Pi_\kappa$, is a complex vector space $\mathcal{K}$ with a non-degenerate hermitian form $Q$ such that:
1. $\mathcal{K} = \mathcal{K}_+ \oplus \mathcal{K}_-$ (fundamental decomposition), with $\mathcal{K}_+, \mathcal{K}_-$ $Q$-orthogonal,
2. $(\mathcal{K}_+, Q)$ is a Hilbert space,
3. $(\mathcal{K}_-, -Q)$ is a Hilbert space,
4. $\dim \mathcal{K}_- = \kappa < \infty$.

**Theorem 2.2 (Uniqueness of the fundamental decomposition, Pontryagin 1944).** In a Pontryagin space $\Pi_\kappa$, every fundamental decomposition $\mathcal{K} = \mathcal{K}_+ \oplus \mathcal{K}_-$ has $\dim \mathcal{K}_- = \kappa$. The decomposition is not unique, but its negative dimension is.

**Theorem 2.3 (Completeness, Iokhvidov–Kreĭn 1956).** Every Pontryagin space $\Pi_\kappa$ is complete with respect to any Hilbert norm associated to a fundamental decomposition. The different norms are equivalent.

**Proposition 2.4 (Isotropic vectors in $\Pi_\kappa$).** A vector $v \in \mathcal{K}$ is **$Q$-isotropic** if $Q(v,v) = 0$. In $\Pi_\kappa$, the subspace of isotropic vectors has dimension no greater than $\kappa$. In particular, there is no isotropic subspace of dimension $> \kappa$.

---

### Section 2.2 — The Pontryagin spectral theorem

**Theorem 2.5 (Pontryagin 1944).** Let $T$ be a $Q$-selfadjoint operator in $\Pi_\kappa$. Then $T$ has at least $\kappa$ eigenvalues (counted with multiplicity) with non-zero imaginary part, or else has an invariant subspace of dimension $\kappa$ on which the form $Q$ is negative.

*Note.* Pontryagin's original statement is in finite dimension. The generalization to infinite dimension (Pontryagin spaces) was carried out by Kreĭn–Langer (1963, 1978) and Azizov–Iokhvidov (1978, 1989).

**Remark 2.6.** Theorem 2.5 gives a **lower bound** on the non-real eigenvalues. In contrast, the theorem giving the upper bound (at most $\kappa$ pairs) is also due to Kreĭn–Langer and is stated below.

---

### Section 2.3 — The Kreĭn–Langer theorem

**Theorem 2.7 (Kreĭn–Langer, 1963; cf. Azizov–Iokhvidov 1989, §2.3).** Let $T$ be a $Q$-selfadjoint operator in a Pontryagin space $\Pi_\kappa$. Then:

**(i) Non-real spectrum.** The non-real spectrum $\sigma(T) \setminus \mathbb{R}$ consists of at most $\kappa$ pairs of complex conjugate eigenvalues $\{\mu_j, \bar\mu_j\}_{j=1}^{r}$ with $r \leq \kappa$, each with finite algebraic multiplicity.

**(ii) Real essential spectrum.** $\sigma_{\mathrm{ess}}(T) \subseteq \mathbb{R}$.

**(iii) Spectral $Q$-orthogonality.** The root subspaces of distinct complex eigenvalues are $Q$-orthogonal to each other and to the subspace corresponding to the real spectrum.

**(iv) $\kappa$-dimensional invariant subspace.** There exists a subspace $L \subset \mathcal{K}$ with $\dim L = \kappa$, $T$-invariant, on which $Q|_L \leq 0$ (the form is non-positive).

**Corollary 2.8.** In the context of Direction B: if $H_C$ is $Q$-selfadjoint in $\Pi_\kappa$ with $\kappa = 2m$, then it has at most $2m$ complex eigenvalues (in conjugate pairs). This gives the bound $r \leq m$ on the orbits of off-line zeros.

**Remark 2.9 (Asymmetry of the Kreĭn–Langer theorem).** The theorem gives a free upper bound. The equality $r = m$ (which links each off-line zero to a complex eigenvalue of $H_C$) is not obtained from the abstract theory and requires specific structure of the operator. See item V.2 of Phase 26.

---

### Section 2.4 — Langer's decomposition theorem and definitizable operators

**Definition 2.10 (Definitizable operator).** A $Q$-selfadjoint operator $T$ in $\Pi_\kappa$ is **definitizable** if there exists a non-zero real polynomial $p(t)$ such that $Q(p(T)f, f) \geq 0$ for all $f \in \mathcal{K}$.

**Theorem 2.11 (Langer, 1982).** Every $Q$-selfadjoint operator with non-empty resolvent set in $\Pi_\kappa$ is definitizable.

**Corollary 2.12.** If $\rho(H_C) \neq \emptyset$, then $H_C$ is definitizable. The definitizing polynomial $p$ is related to the non-real eigenvalues: its degree is at most $2r$ where $r$ is the number of pairs of non-real eigenvalues.

**Remark 2.13 (Relevance to Direction B).** If $H_C$ were definitizable with definitizing polynomial $p(t) = t^2 - c$ for some $c > 0$, that would mean $Q((H_C^2 - c)f, f) \geq 0$, which is a strong spectral condition. The question is whether the arithmetic structure of $H_C$ forces a specific definitizing polynomial.

---

### Section 2.5 — Conditions for zero negative index

The central result we seek is: when is $\kappa = 0$?

**Proposition 2.14.** For a $Q$-selfadjoint operator $T$ in $\Pi_\kappa$, the following conditions are equivalent:

*(a)* $\kappa = 0$ (the space is a Hilbert space).

*(b)* $Q(f, f) \geq 0$ for all $f \in \mathcal{K}$ (the form is positive semidefinite).

*(c)* $T$ has no eigenvalues with non-zero imaginary part.

*(d)* The $\kappa$-dimensional invariant subspace of Theorem 2.7(iv) can be taken with $Q|_L = 0$ (isotropic) and $L = \{0\}$.

*Proof.* (a)$\iff$(b) is the definition of a Hilbert space among spaces with a hermitian form. (b)$\iff$(c): If $Q \geq 0$ and $Tv = \mu v$ with $\text{Im}(\mu) \neq 0$, then by $Q$-selfadjointness: $Q(Tv, v) = \mu Q(v,v) = Q(v,Tv) = \bar\mu Q(v,v)$, so $(\mu - \bar\mu) Q(v,v) = 0$, and since $\mu \neq \bar\mu$ we get $Q(v,v)=0$. But if $Q \geq 0$ and $Q(v,v) = 0$, then $v = 0$ (there are no isotropic vectors in a Hilbert space), contradiction. (c)$\Rightarrow$(b): by the spectral theorem, if there are no complex eigenvalues and the space has index $\kappa > 0$, the negative subspace of Theorem 2.7(iv) exists, which contains vectors with $Q < 0$. Contradiction with (c) if, in addition, we use that $T$ has the property that in that subspace it acts with real eigenvalues by (b)... [The complete argument requires Langer's spectral theory for definitizable operators. We do not close it here.] $\square$ (partial)

**Corollary 2.15 (Key to Direction B).** To prove $\kappa = 0$ it suffices to demonstrate **one** of the following:
- (S1) $Q(f,f) \geq 0$ for all $f \in \mathcal{K}$ (Weil positivity — directly equivalent to RH).
- (S2) $H_C \geq c I$ with respect to $Q$ for some $c > 0$ (uniform lower semiboundedness with respect to $Q$).
- (S3) The spectrum of $H_C$ is contained in $\mathbb{R}$ (absence of complex eigenvalues).
- (S4) The system of eigenvectors and cyclic vectors of $H_C$ is $Q$-complete (Riesz basis in $\Pi_\kappa$).

Each of these conditions is analyzed in Parts III–V.

---

## Part III — The functional equation as a spectral constraint

### Section 3.1 — The symmetry $s \mapsto 1-s$ on $H_C$

The functional equation $\xi(s) = \xi(1-s)$ induces a symmetry on the spectrum of $H_C$. We make this relation precise.

**Definition 3.1.** Let $J: \mathcal{K} \to \mathcal{K}$ be the **functional conjugation** operator defined by:
$$(Jf)(x) = \overline{f(1/x)} / x, \quad x \in \mathbb{R}^*_+.$$

In terms of the Mellin transform: $\widehat{Jf}(s) = \overline{\hat{f}(1-\bar{s})}$.

**Proposition 3.2 (Properties of $J$).** The operator $J$ satisfies:
1. $J^2 = I$ (involution).
2. $Q(Jf, Jg) = Q(f, g)$ (isometry with respect to $Q$, by the symmetry $\xi(s) = \xi(1-s)$).
3. $JH_C = (I - H_C)J$ (commutation relation between $J$ and $H_C$).

*Proof of (3).* On test functions, if $(H_C f)(x) = -ix\partial_x f(x)$, then:
$$(JH_C f)(x) = \overline{(H_C f)(1/x)} / x = \overline{(-i \cdot (1/x) \partial_x|_{x \to 1/x} f(1/x))} / x.$$
With the change $y = 1/x$: $\partial_x f(1/x)|_{x} = -y^2 f'(y)$, so $(H_C f)(1/x) = -i(1/x)(-x^2 f'(1/x)) = ix f'(1/x)$.
Therefore $(JH_C f)(x) = \overline{ix f'(1/x)} / x = -i f'(1/x) = (H_C Jf)(x) \cdot (-1) + (Jf)(x)$... 

[The precise computation depends on the convention for domains and the weight of the measure. What matters is the abstract statement.] $\square$ (formal)

**Theorem 3.3 (Spectral symmetry under the functional equation).** If $\lambda$ is an eigenvalue of $H_C$ (in $\mathcal{K}$ or in a suitable distributional extension), then $1 - \bar\lambda$ is also an eigenvalue of $H_C$. In particular:
- If $\lambda \in \mathbb{R}$, then $1 - \lambda \in \mathbb{R}$ is also an eigenvalue.
- If $\lambda \in \mathbb{C} \setminus \mathbb{R}$, then $\{1-\bar\lambda, \bar\lambda, 1-\lambda\}$ are additional eigenvalues.

*Proof.* If $H_C f = \lambda f$, then $H_C (Jf) = J(I - H_C) f = J f - J H_C f = J f - \lambda J f = (1-\lambda) Jf$. Therefore $Jf$ is an eigenvector for the eigenvalue $1-\lambda$. Taking conjugates with the antilinearity of $J$, we obtain the eigenvalue $1 - \bar\lambda$. $\square$ (formal, assuming relation (3) of Proposition 3.2)

**Corollary 3.4 (Implication for the negative index).** Spectral symmetry implies that the complex eigenvalues of $H_C$ come in orbits $\{\lambda, \bar\lambda, 1-\lambda, 1-\bar\lambda\}$ of size 4 (when all are distinct), unless $\lambda = 1/2$ or $\lambda \in \mathbb{R}$.

In the context of the zeros of $\zeta$: if $\rho = 1/2 + b + i\gamma$ is an off-line zero ($b \neq 0$), the four elements of the orbit are $\{1/2+b+i\gamma, 1/2+b-i\gamma, 1/2-b+i\gamma, 1/2-b-i\gamma\}$. In terms of eigenvalues of $H_C$ (with shift $s \to s - 1/2$): $\{b+i\gamma, b-i\gamma, -b+i\gamma, -b-i\gamma\}$.

By the functional equation, the negative index $\kappa = 2m$ is always **even**, and its complex eigenvalues come in quartets.

**Remark 3.5 (What this does not give).** The functional symmetry imposes constraints on the shape of the complex eigenvalues, but **does not imply that none exist**. To prove $\kappa = 0$ (absence of complex eigenvalues), we need something more than symmetry.

---

### Section 3.2 — The fixed-point subspace and its relation to the critical line

**Proposition 3.6.** The fixed-point subspace of $J$ is:
$$\mathcal{K}_J = \{f \in \mathcal{K} : Jf = f\} = \{f : f(x) = \overline{f(1/x)}/x\}.$$

In Mellin terms: $f \in \mathcal{K}_J$ iff $\hat{f}(s) = \overline{\hat{f}(1-\bar{s})}$, i.e., $\hat{f}$ is "real on the critical line $\mathrm{Re}(s) = 1/2$".

**Proposition 3.7.** The restriction of $H_C$ to $\mathcal{K}_J$ has spectrum symmetric with respect to $1/2$ (in the sense that $\lambda$ is an eigenvalue iff $1-\lambda$ is). On the critical line, eigenvalues of the type $\lambda = 1/2 + i\gamma$ satisfy $1 - \bar\lambda = 1/2 + i\gamma = \lambda$, so they are fixed points of the spectral symmetry.

**Remark 3.8.** The zeros of $\zeta$ on the critical line, in the parametrization $\rho = 1/2 + i\gamma_n$, correspond (formally) to eigenvalues $\lambda_n = i\gamma_n$ of $H_C$ (with the shift $s \to s - 1/2$), which are **purely imaginary**. This is consistent with the constraint $\mathrm{Re}(\lambda) = 0$ (or $\mathrm{Re}(\lambda) = 1/2$ without the shift). The functional symmetry does not distinguish between on-line and off-line zeros except in the type of orbit.

---

## Part IV — Lower semiboundedness and the square-root obstacle

### Section 4.1 — The condition of lower semiboundedness with respect to $Q$

**Definition 4.1 (Lower semiboundedness).** The operator $H_C$ is **$Q$-lower semibounded** if there exists $c \in \mathbb{R}$ such that:
$$Q(H_C f, f) \geq c \cdot Q(f, f) \quad \text{for all } f \in \text{Dom}(H_C) \cap \mathcal{K}_+,$$
where $\mathcal{K}_+$ is the positive component in the fundamental decomposition.

**Note 4.2.** In a Pontryagin space, lower semiboundedness "with respect to $Q$" is more subtle than in a Hilbert space, because $Q$ is not positive. The relevant condition for forcing $\kappa = 0$ is semiboundedness **with respect to the Hilbert norm** of the fundamental decomposition, not with respect to $Q$ directly.

**Proposition 4.3 (Semiboundedness and absence of non-real eigenvalues).** If there exists $c > 0$ such that:
$$Q(H_C f, f) \geq c \quad \text{for all } f \in \mathcal{K} \text{ with } Q(f,f) = 1,$$
then $H_C$ has no eigenvalues with $\mathrm{Re}(\lambda) < c$, and in particular has no non-real eigenvalues with $\mathrm{Re}(\lambda) < c$.

*Proof.* If $H_C v = \lambda v$, then $Q(H_C v, v) = \lambda Q(v,v)$. If $Q(v,v) = 1$ (normalizing), then $\lambda = Q(H_C v, v) \geq c$. But if $\lambda$ is complex, $\lambda = Q(H_C v, v)$ would be real (by $Q$-selfadjointness), a contradiction with $\lambda \notin \mathbb{R}$.

More precisely: for $v$ an eigenvector with complex eigenvalue $\lambda$, $Q(v,v)$ can be 0 (isotropic vectors). The condition on complex eigenvalues requires separate analysis. $\square$ (partial)

---

### Section 4.2 — Connection with the Weil form: the prime-archimedean decomposition

The form $Q$ on $\mathcal{S}(\mathbb{R}^*_+)$ decomposes as:
$$Q(f,f) = Q_\infty(f,f) - Q_{\mathrm{prim}}(f,f),$$
where the archimedean term $Q_\infty$ comes from the gamma factor and is positive semidefinite (for functions in the appropriate half-plane), and the prime term is:
$$Q_{\mathrm{prim}}(f,f) = 2 \sum_{p, n \geq 1} \frac{\log p}{p^{n/2}} \mathrm{Re}(f \star \tilde{f})(p^n).$$

**Proposition 4.4 (Archimedean form as a differential operator).** The archimedean term $Q_\infty(f,f)$ corresponds to the action of the operator:
$$\hat{Q}_\infty(s) = \Omega(s) = \mathrm{Re}\,\psi\left(\frac{s}{2}\right) - \log\pi + \ldots$$
where $\psi = \Gamma'/\Gamma$. In particular, $\Omega(s) \sim \frac{1}{2}\log|s|$ as $|s| \to \infty$ on the critical line.

**The central obstacle (the square-root barrier).** For the lower semiboundedness $Q \geq 0$ (equivalent to RH), we need:
$$Q_\infty(f,f) \geq Q_{\mathrm{prim}}(f,f) \quad \forall f.$$

The prime term, at scale $N = e^{1/\varepsilon}$, has amplitude:
$$Q_{\mathrm{prim}} \sim 2 \sum_{n \leq N} \frac{\Lambda(n)}{\sqrt{n}} |(f \star \tilde{f})(\log n)| \sim 2\sqrt{N} \cdot \|f\|^2,$$
using the Chebyshev estimate $\sum_{n \leq N} \Lambda(n)/\sqrt{n} \sim 2\sqrt{N}$. In contrast, the archimedean term grows like $\log N$.

**Proposition 4.5 ($\sqrt{N}$ vs. $\log N$ barrier).** The amplitude of the prime term grows as $\sqrt{N}$ while that of the archimedean term grows as $\log N$. Therefore, without cancellation among the oscillatory terms of $Q_{\mathrm{prim}}$, the lower semiboundedness $Q \geq 0$ fails.

*Remark 4.6 (The root of the difficulty).* The cancellation in $Q_{\mathrm{prim}}$ comes from the oscillatory signs of $(f \star \tilde{f})(p^n)$ when $f$ has Mellin transform concentrated on the critical line. This cancellation is exactly what encodes the distribution of the zeros of $\zeta$. Hence:

> Lower semiboundedness $Q \geq 0$ is **equivalent** to RH, and its proof requires controlling the cancellation in the prime terms, which is the content of RH.

---

### Section 4.3 — The prime-tail strategy (from Opt-B)

In the program document OPTION-B-pontryagin-index-attack.md, a weaker strategy is proposed:

**Strategy 4.7 (Relative form bound — RFB$_X$).** For a cutoff $X > 0$, separate $Q_{\mathrm{prim}} = Q_{\mathrm{prim}, \leq X} + Q_{\mathrm{prim}, > X}$. The first term is of finite rank (finitely many primes $\leq X$). If for some $X$:
$$|Q_{\mathrm{prim}, > X}(f,f)| \leq a \cdot Q_\infty(f,f) + C \|f\|^2, \quad a < 1,$$
then $Q$ is a finite-rank perturbation of a lower-semibounded form, which implies $\kappa < \infty$ (finitely many off-line zeros). This is weaker than RH but also open.

**Proposition 4.8 (Status of RFB$_X$).** The optimal constant $a_{\mathrm{tail}}(X) = \sup_f Q_{\mathrm{prim},>X}(f,f) / Q_\infty(f,f)$ satisfies:
- $a_{\mathrm{tail}}(X) \leq 1$ (by the N3 results of the program, which establish that the full prime term does not exceed the archimedean one in relative $\ell^\infty$).
- If $a_{\mathrm{tail}}(X) < 1$ for some finite $X$: $\kappa < \infty$ unconditionally.
- If $a_{\mathrm{tail}}(X) \equiv 1$ for all $X$: the strategy does not give $\kappa < \infty$.

The question of whether $a_{\mathrm{tail}}(X) < 1$ or $\equiv 1$ is **open** and quantitative, not easily reducible to known properties of $\zeta$.

**Conclusion of Section 4.** Direct lower semiboundedness is equivalent to RH. The prime-tail strategy (RFB$_X$) could give $\kappa < \infty$ unconditionally, but the constant $a_{\mathrm{tail}}$ is at the critical limit $= 1$ according to the program's results. **This is the most promising direction within Direction B for obtaining an unconditional result weaker than RH.**

---

## Part V — The Livsic characteristic function and its analogue in Pontryagin spaces

### Section 5.1 — The Livsic characteristic function for operators in Hilbert spaces

In the theory of non-selfadjoint operators in Hilbert spaces (Livsic 1946, Brodskii–Livsic 1958), the **characteristic function** of an operator $T$ with finite defect is an analytic matrix function $\Theta_T(z)$ that encodes the non-selfadjoint part of $T$ and determines its spectral structure up to unitary equivalence.

For an operator $T$ with "rank-one non-selfadjoint part" (nuclear defect):
$$\Theta_T(z) = I - 2i K^*(T - zI)^{-1} K,$$
where $K$ is the defect operator. The function $\Theta_T$ satisfies:
- $\Theta_T(z)^* \Theta_T(z) = I$ for $z$ in the real spectrum of $T$ (isometry on the real spectrum).
- The non-real eigenvalues of $T$ are the poles of $\Theta_T$.

**Connection with $\zeta$.** In the Connes–Burnol context, the function $\zeta$ itself (or more precisely the function $\xi$) acts as the characteristic function of a certain Dirac operator associated with adelic scattering (Burnol 2002). The zeros of $\xi$ correspond to the poles of the resolvent, and the non-selfadjointness of the Connes operator is encoded in the "dispersive part" of the characteristic function.

---

### Section 5.2 — Analogue of the characteristic function in Pontryagin spaces

In Pontryagin spaces, the theory of the characteristic function was developed by Livsic–Yantsevich (1979) and later by Alpay–Dijksma–Rovnyak–de Snoo (1997) in the context of Pontryagin operators with defect.

**Definition 5.1 (Characteristic function in $\Pi_\kappa$).** Let $T$ be a $Q$-symmetric operator in $\Pi_\kappa$ with defect space of dimension $d$. The **characteristic function** of $T$ is an analytic matrix function $\Theta_T^{(\kappa)}(z)$ of size $d \times d$ with rational coefficients in $z$, satisfying:
$$\Theta_T^{(\kappa)}(z)^{[*]} \Theta_T^{(\kappa)}(z) = I$$
for $z$ in the real spectrum of $T$, where ${}^{[*]}$ denotes the adjoint with respect to the form $Q$ on the defect space.

The characteristic function in $\Pi_\kappa$ is a **$J$-unitary** function (unitary with respect to an indefinite form), not an ordinary unitary one.

**Proposition 5.2 (Structure of the characteristic function in $\Pi_\kappa$).** The differences between the characteristic function in $\Pi_\kappa$ and in Hilbert space are:
1. $\Theta_T^{(\kappa)}$ is a $J$-unitary function: instead of $\Theta^*\Theta = I$, it satisfies $\Theta^{[*]} \Theta = I$ where ${}^{[*]}$ involves the indefinite form.
2. $\Theta_T^{(\kappa)}$ can have poles on the real axis, corresponding to "real singular" eigenvalues of the operator.
3. The negative index $\kappa$ is reflected in the number of "indefinite singularities" of $\Theta_T^{(\kappa)}$.

**Theorem 5.3 (Livsic–Yantsevich, 1979; cf. Alpay et al. 1997).** For a $Q$-selfadjoint operator $T$ in $\Pi_\kappa$ with discrete spectrum:

**(i)** The non-real eigenvalues of $T$ are exactly the poles of $\Theta_T^{(\kappa)}$ in $\mathbb{C} \setminus \mathbb{R}$.

**(ii)** The negative index $\kappa$ equals the number of indefinite singularities of $\Theta_T^{(\kappa)}$ on $\mathbb{R}$ (counted appropriately).

**(iii)** If $\Theta_T^{(\kappa)}$ is analytic on $\mathbb{R}$ (with no real singularities), then $T$ is selfadjoint in the Hilbert space (i.e., $\kappa = 0$).

---

### Section 5.3 — Connection with $\zeta$: the function $\xi$ as a characteristic function

**Conjecture 5.4 (Burnol–Connes identification).** The function:
$$\Theta_{H_C}^{(\kappa)}(z) = \frac{\xi(1/2 + z)}{\xi(1/2 - z)}$$
is (a version of) the characteristic function of the operator $H_C$ in the Pontryagin space $(\mathcal{K}, Q)$.

*Heuristic justification.* The function $\xi(1/2 + z)/\xi(1/2 - z)$ is:
- Meromorphic on $\mathbb{C}$, with poles at $z = \rho - 1/2$ where $\rho$ is an off-line zero of $\zeta$ (because $\xi(\rho) = 0$ and $1/2 + z = \rho \Rightarrow z = \rho - 1/2$).
- Satisfies $|\Theta_{H_C}^{(\kappa)}(iy)| = 1$ for $y \in \mathbb{R}$ on the imaginary line (by the functional equation $|\xi(1/2 + iy)| = |\xi(1/2 - iy)|$ for real $y$), i.e., it is a Blaschke-type function in the right half-plane.
- Its poles in $\mathbb{C} \setminus i\mathbb{R}$ correspond exactly to the zeros of $\zeta$ off the critical line.

Under RH, the only zeros of $\xi$ have $\text{Re}(\rho) = 1/2$, i.e., $\text{Re}(z) = 0$: the function $\Theta_{H_C}^{(\kappa)}(z)$ has no poles for $\text{Re}(z) \neq 0$. By Theorem 5.3(iii), this would imply $\kappa = 0$.

**Proposition 5.5 (What the characteristic function gives and does not give).** 
- **What it gives:** A direct connection between the zeros of $\xi$ and the complex eigenvalues of $H_C$. If the identification of Conjecture 5.4 is correct, then the program reduces to studying the poles of $\xi(1/2+z)/\xi(1/2-z)$.
- **What it does not give:** An argument for proving that these poles lie on $i\mathbb{R}$ without knowing in advance the positions of the zeros of $\zeta$. The characteristic function is a *reflection* of the spectral structure, not an independent tool for determining it.

**Remark 5.6 (Circularity).** Proving that $\Theta_{H_C}^{(\kappa)}(z)$ is analytic for $\text{Re}(z) \neq 0$ is equivalent to proving that the zeros of $\xi$ have $\text{Re}(\rho) = 1/2$, which is exactly RH. The Livsic characteristic function does not provide an independent lever for closing the argument.

---

## Part VI — Formulation of the precise obstacle

### Section 6.1 — The map of sufficient conditions

We summarize the conditions that would imply $\kappa = 0$, ordered by strength:

| Condition | Implies | Status |
|-----------|---------|--------|
| C1: $Q(f,f) \geq 0$ for all $f$ | $\kappa = 0$ directly | Equivalent to RH |
| C2: $H_C \geq c I$ in $\mathcal{K}$ (Hilbert norm) | $\kappa = 0$ (by spectrum in $[c, \infty)$) | Equivalent to RH |
| C3: Spectrum of $H_C \subset i\mathbb{R}$ | $\kappa = 0$ by Kreĭn–Langer | Reformulation of RH |
| C4: $\Theta_{H_C}$ analytic for $\text{Re}(z) \neq 0$ | $\kappa = 0$ by Theorem 5.3(iii) | Equivalent to RH |
| C5: $a_{\mathrm{tail}}(X) < 1$ for some $X$ | $\kappa < \infty$ (weaker result) | **Open, quantitative** |
| C6: $H_C$ definitizable with $p(t) = t$ | $\kappa = 0$ directly | Implies C1 |
| C7: Complete eigenvector system with real eigenvalues | $\kappa = 0$ (by spectral argument) | Requires Riesz basis in $\Pi_\kappa$ |

**Remark 6.1.** Conditions C1–C4 and C6 are all directly equivalent to RH or imply it in a way that proving the condition requires as much work as proving RH itself. Condition C5 is the only one that could give an unconditional result.

---

### Section 6.2 — Why lower semiboundedness is hard

**Proposition 6.2.** Lower semiboundedness $Q(f,f) \geq c \|f\|_{\mathcal{K}}^2$ (with $\|\cdot\|_{\mathcal{K}}$ the Hilbert norm of the fundamental decomposition) is equivalent to RH plus the bound on the error in the prime number theorem.

*Argument.* Lower semiboundedness $Q \geq c\|\cdot\|^2$ requires controlling the difference $Q_\infty - Q_{\mathrm{prim}} \geq c\|\cdot\|^2$. The prime term is:
$$Q_{\mathrm{prim}}(f,f) = 2\mathrm{Re} \int_0^\infty \hat{f}(1/2 + it) \overline{\hat{f}(1/2 + it)} \left( \sum_\gamma \delta(t - \gamma) \right) dt,$$
where $\gamma$ runs over the imaginary parts of the on-line zeros (under RH). Controlling this expression requires the distribution of the $\gamma_n$, which is equivalent to RH. $\square$ (schematic)

---

### Section 6.3 — The Hadamard obstacle in Direction B

**Definition 6.3 (Hadamard obstacle, version B).** Analogously to the CCM barrier (Doc 88), the **Hadamard obstacle in Direction B** is:

> No property of $Q$ or $H_C$ that is verifiable from global properties of $\zeta$ (such as its growth properties, its functional equation, or its Euler product) implies $\mathrm{neg.ind}(H_C) = 0$ without going through knowledge of the positions of the zeros of $\zeta$ off the critical line.

**Proposition 6.4 (Obstacle in Direction B).** Let $P$ be any property of $H_C$ verifiable from:
- The functional equation $\xi(s) = \xi(1-s)$,
- The Euler product $\zeta(s) = \prod_p (1 - p^{-s})^{-1}$ for $\text{Re}(s) > 1$,
- Global growth estimates of $|\zeta(s)|$ in regions away from the critical line,

and no information about the individual positions of the zeros of $\zeta$. Then $P$ does not imply $\mathrm{neg.ind}(H_C) = 0$.

*Argument (not rigorous but convincing).* The Hadamard obstacle establishes that Weil positivity (condition C1) is "strictly stronger" than all verifiable global properties of $\zeta$. Direction B reformulates C1 in spectral terms for $H_C$, but the underlying difficulty persists: the spectrum of $H_C$ in $\Pi_\kappa$ is determined precisely by the positions of the zeros, and any condition forcing the spectrum to lie in $i\mathbb{R}$ is essentially assuming RH. The complete argument is analogous to that of the Hadamard barrier in the CCM direction (Doc 88). $\square$ (schematic)

**Remark 6.5 (The exception: C5).** Condition C5 ($a_{\mathrm{tail}}(X) < 1$) partially escapes the Hadamard obstacle because it implies only $\kappa < \infty$ (finitely many off-line zeros), not $\kappa = 0$ (RH). The Hadamard barrier in its strong version forbids concluding $\kappa = 0$, but does not exclude $\kappa < \infty$. However, the constant $a_{\mathrm{tail}}$ is at the critical value $= 1$ according to the program's results.

---

## Part VII — Analysis of potential new routes

### Section 7.1 — Route via the adelic Galois group action

**Idea.** The idèle class group $C_\mathbb{Q} = \mathbb{A}_\mathbb{Q}^*/\mathbb{Q}^*$ has the structure of a locally compact group. The representation of $C_\mathbb{Q}$ on $\mathcal{K}$ could impose constraints on the eigenvalues of $H_C$ beyond functional symmetry.

**Proposition 7.1 (Group action and the spectrum).** If a family of operators $\{V_a : a \in C_\mathbb{Q}\}$ acts unitarily on $(\mathcal{K}, Q)$ and commutes with $H_C$, then the spectrum of $H_C$ is invariant under the action of $C_\mathbb{Q}$ (in some sense).

However, the action of $C_\mathbb{Q}$ is precisely what defines $H_C$ (as its infinitesimal generator), so the $C_\mathbb{Q}$-invariance of the spectrum is automatic and gives no new information about the position of the eigenvalues.

**Conclusion.** The symmetry of the group $C_\mathbb{Q}$ is not a new lever: it is already built into the definition of $H_C$.

---

### Section 7.2 — Route via $\mathrm{GL}(1)$ representation theory

**Idea.** In the theory of automorphic forms, Hecke operators act on spaces of modular forms and have spectral properties related to the $L$-function of the form. Can this framework be transferred to the case of $\zeta$?

**For $\mathrm{GL}(1)$ over $\mathbb{Q}$**, the relevant $L$-function is $\zeta$ itself. The Hecke operators $T_p$ act on the idèle class space and have eigenvalues $p + 1/p$ (for the trivial representation) or $p^{it} + p^{-it}$ (for characters). The eigenvalues of $H_C$ on the critical line are $i\gamma_n$ (purely imaginary), consistent with the eigenvalues of the Hecke operators.

**Problem.** For off-line zeros, the eigenvalues would have non-zero real part, which is inconsistent with the interpretation as eigenvalues of unitary Hecke operators. But this inconsistency **is** RH: off-line zeros are inconsistent with the unitarity of the Hecke operators, and proving that none exist is equivalent to proving that $\zeta$ has no zeros off the critical line.

**Conclusion.** The Hecke-operator route is a reformulation of RH, not a new lever.

---

### Section 7.3 — Route via Volterra operators and integration by parts

**Idea.** In the theory of Volterra operators in Hilbert spaces, a Volterra operator has empty point spectrum (spectrum only at 0). If $H_C$ could be decomposed as a compact perturbation of a Volterra operator, its spectrum could be controlled.

**Definition 7.2.** A Volterra integral over $\mathbb{R}^*_+$ has the form:
$$(Vf)(x) = \int_0^x f(y) K(x,y) \frac{dy}{y},$$
with an appropriate kernel $K$. In the case of the function $\xi$, the kernel is related to the pair correlation function of zeros (Montgomery 1973).

**Proposition 7.3 (Obstruction).** The decomposition $H_C = H_{\mathrm{Volterra}} + H_{\mathrm{rest}}$ requires identifying a triangular part of $H_C$. But $H_C = -ix\partial_x$ is a first-order differential operator, and its triangularity (in some basis) is equivalent to the existence of eigenfunctions of the Euler operator — which are exactly the characters $x^s$. The values of $s$ for which these are "admissible" in $\mathcal{K}$ are the off-line zeros of $\zeta$. Circularity again.

---

### Section 7.4 — The question of completeness of the eigenvector system

**Definition 7.3 (Complete system).** The system of eigenvectors and cyclic vectors of $H_C$ is **$Q$-complete** in $\mathcal{K}$ if the closed subspace generated by all the eigenvectors and cyclic vectors is all of $\mathcal{K}$.

**Theorem 7.4 (Completeness implies selfadjointness in $\Pi_\kappa$, under hypothesis).** If the eigenvector system of a $Q$-selfadjoint operator $T$ in $\Pi_\kappa$ forms a Riesz basis of $\mathcal{K}$ (as a Hilbert space), and all eigenvalues are real, then $T$ is selfadjoint in the Hilbert space $\mathcal{K}$ and $\kappa = 0$.

*Remark 7.5.* The above result is circular in the following sense: the hypothesis that all eigenvalues are real is equivalent to asserting that there are no complex eigenvalues, which is what we want to prove.

**Non-circular proposal.** A non-circular version would be: prove the completeness of the eigenvector system **without** assuming that the eigenvalues are real, and then deduce from completeness that there can be no complex eigenvalues.

**Proposition 7.6 (Obstruction to the non-circular proposal).** In general, a $Q$-selfadjoint operator in $\Pi_\kappa$ with $\kappa > 0$ can have a complete eigenvector system with complex eigenvalues. Completeness does not force the eigenvalues to be real. Therefore, completeness of the eigenvector system does not imply $\kappa = 0$ without additional hypotheses on the eigenvalues.

---

### Section 7.5 — The finite-rank perturbation route

**Idea.** If $H_C = H_0 + K$ where $H_0$ is selfadjoint (in the Hilbert sense) with $\kappa_0 = 0$, and $K$ is of finite rank, then by Weyl's theorem the essential spectrum does not change, and the number of complex eigenvalues of $H_C$ is at most equal to the rank of $K$.

**Proposition 7.7.** If there exists a decomposition $H_C = H_0 + K$ with $H_0$ positive selfadjoint in a Hilbert space (with the positive metric associated to the fundamental decomposition of $\Pi_\kappa$) and $K$ of finite rank equal to $\kappa$, then $\mathrm{neg.ind}(H_C) \leq \kappa$.

*Remark 7.8 (Problem).* The condition that the rank of $K$ equals $\kappa$ is exactly the statement we want to prove (that the negative index is finite and controlled). We do not know a priori what the rank of $K$ is, and determining it requires knowing $\kappa$, which requires knowing the off-line zeros.

---

### Section 7.6 — Evaluation: does a genuinely new route exist?

**Theorem 7.9 (Evaluation of Direction B).** No route has been found in Direction B that:
1. Uses exclusively properties of $H_C$ derivable from global properties of $\zeta$ (functional equation, Euler product, growth in the plane), AND
2. Implies $\mathrm{neg.ind}(H_C) = 0$.

The routes found are:
- **C1–C4:** Equivalent to RH.
- **C5 (RFB$_X$):** Could give $\kappa < \infty$ (weaker than RH) but is at the critical threshold.
- **Routes via adelic group, Hecke, Volterra, completeness:** All are reformulations of RH or are circular.

**The only unblocked route is C5.** If the constant $a_{\mathrm{tail}}(X)$ turns out to be strictly less than 1 for some finite $X$, that would give a new unconditional result: $\kappa < \infty$ (finitely many off-line zeros). This does not imply RH but is the largest result achievable within Direction B without new information.

---

## Part VIII — Technical structure of the negative-index problem

### Section 8.1 — The defect operator and the von Neumann extension

To understand $H_C$ in $\Pi_\kappa$ from the perspective of extension theory, we apply von Neumann theory adapted to Pontryagin spaces.

**Definition 8.1.** Let $T_0 = H_C|_{\mathcal{S}_0}$ be the restriction of $H_C$ to the subspace of "well-supported" test functions. The operator $T_0$ is $Q$-symmetric (assuming V.1 is verified) and its closure $\overline{T_0}$ is a closed $Q$-symmetric operator in $\Pi_\kappa$.

**Definition 8.2 (Defect subspaces).** For $z \in \mathbb{C} \setminus \mathbb{R}$, the **defect subspaces** of $T_0$ with respect to $Q$ are:
$$N_z = \ker(T_0^{[*]} - zI) \quad (\text{in } \Pi_\kappa),$$
where $T_0^{[*]}$ is the $Q$-adjoint of $T_0$.

**Proposition 8.3.** The defect indices $n_\pm = \dim N_{\pm i}$ are finite if and only if the Pontryagin space $\Pi_\kappa$ has the property that the "essential spectrum of $T_0$" does not accumulate at the defect points. In the case of $H_C$, the defect indices are related to the regularity of the zeros of $\zeta$ on the critical line.

**The standard selfadjoint extension.** In the Hilbert space $L^2(C_\mathbb{Q})$, the operator $H_C$ has selfadjoint extensions (in the ordinary sense) parametrized by unitary operators between the defect spaces. Each extension corresponds to different adelic "boundary conditions". The question is which extension, if any, is the "correct" one for the Weil formula.

---

### Section 8.2 — The regularization problem and the Weil formula

The Weil form $Q(f,f) = \mathcal{W}(f \star \tilde{f})$ requires regularization because the sum over zeros $\sum_\rho \hat{f}(\rho)$ converges conditionally. This regularization introduces additional terms that are crucial for the properties of $H_C$.

**Proposition 8.4 (Regularization as a perturbation).** The regularization of $\mathcal{W}$ can be written as:
$$Q_{\mathrm{reg}}(f,f) = Q_{\mathrm{formal}}(f,f) + R(f,f),$$
where $R$ is a regularization term that depends on the chosen regularization method. Different regularizations give different operators $H_C$ (in the sense of domains and associated quadratic forms).

**Remark 8.5.** The choice of the "correct" regularization is part of the problem of constructing the space $\mathcal{K}$ (a pending item of Phase 26). A natural regularization is that provided by the explicit Weil formula in adelic form (Tate 1950), which gives a form $Q$ with suitable convergence.

---

### Section 8.3 — The continuous spectrum problem

**Proposition 8.6 (The continuous spectrum of $H_C$).** In $L^2(C_\mathbb{Q})$, the operator $H_C = -ix\partial_x$ has continuous spectrum covering $\mathbb{R}$ (in the parametrization where on-line zeros appear as imaginary eigenvalues). This continuous spectrum corresponds to the "prime wave functions" in the Weil formula.

**Consequence for the negative index.** The distinction between $\kappa = 0$ and $\kappa > 0$ in the presence of continuous spectrum is more subtle than in the discrete case. The negative index in a Pontryagin space with continuous spectrum is measured via the "negatively definite part" of the spectrum, which in terms of the Connes operator corresponds to the off-line zeros.

**Proposition 8.7 (Spectral decomposition in $\Pi_\kappa$).** Under the hypotheses of Phase 26 (V.1–V.4 verified), the operator $H_C$ in $\Pi_\kappa$ has the spectral decomposition:
$$H_C = H_{\mathrm{ess}} \oplus H_{\mathrm{disc}},$$
where:
- $H_{\mathrm{ess}}$ corresponds to the continuous spectrum (on-line zeros), selfadjoint in $L^2$.
- $H_{\mathrm{disc}}$ corresponds to the discrete spectrum of $\Pi_\kappa$, which has $\kappa$ complex eigenvalues corresponding to the off-line zeros.

The negative index $\kappa$ is the contribution of $H_{\mathrm{disc}}$ to the Kreĭn index.

*Status:* This decomposition is conjectural and depends on items V.1–V.4 of Phase 26.

---

## Part IX — Synthesis and work agenda

### Section 9.1 — Table of obstacles in Direction B

| Route | Condition | Main obstacle | Status |
|------|-----------|---------------------|--------|
| Semiboundedness $Q \geq 0$ | C1 | Equivalent to RH | Blocked |
| Semiboundedness $H_C \geq cI$ | C2 | Equivalent to RH | Blocked |
| Spectrum of $H_C \subset i\mathbb{R}$ | C3 | Reformulation of RH | Blocked |
| Analytic characteristic function | C4 | Equivalent to RH | Blocked |
| Prime tail $a_{\mathrm{tail}} < 1$ | C5 | $a_{\mathrm{tail}} = 1$ marginal | **Open** |
| Definitizability of $H_C$ | C6 | Implies C1 | Blocked |
| Completeness real eigenvectors | C7 | Circular | Blocked |
| Hecke / representations | New symmetries | Reformulation of RH | Blocked |
| Finite-rank perturbation | $H_C = H_0 + K$ | Requires knowing $\kappa$ | Circular |
| Volterra / triangular | Decomposition | Requires eigenvectors | Circular |

---

### Section 9.2 — Items V.1–V.4 of Phase 26 revisited

Before proceeding with any route of Direction B, the items of Phase 26 must be resolved. We assess their status in light of the analysis of this document:

**V.1 ($Q$-symmetry of $H_C$).** *Status:* Pending. Requires verifying the invariance of $Q$ under $U_\lambda$. The explicit computation involves the transformation of the prime terms of $Q$ under dilations. It seems verifiable via the Weil formula in adelic form (Tate 1950), where the invariance of the adelic product translates into the invariance of $Q$.

*Proposed action:* Verify the invariance of $\mathcal{W}$ under multiplicative changes of variable using the adelic version of the Weil formula.

**V.2 (zeros ↔ complex eigenvalues).** *Status:* Pending, this is the central obstacle. The characters $f_j = x^{b_j + i\gamma_j}$ are not in $L^2(C_\mathbb{Q})$. The question is whether they are in $\mathcal{K}$ as tempered distributions.

*Proposed action:* Define $\mathcal{K}$ as a space of tempered distributions with respect to the Weil metric, and verify whether the characters are defect vectors of $H_C$ in this space.

**V.3 ($\mathrm{neg.ind}(H_C) = \kappa$).** *Status:* A consequence of V.2 plus the Kreĭn–Langer theorem. If V.2 is verified, V.3 follows from the abstract theory.

**V.4 (dimension of the eigenspace).** *Status:* An algebraic consequence of V.2 and V.3.

---

### Section 9.3 — The Phase 34 agenda for Direction B

**Priority 1 (Possible unconditional result): C5.**

Prove or disprove that $a_{\mathrm{tail}}(X) < 1$ for some finite $X$. This is the only result within Direction B that could be unconditional (not equivalent to RH). The difficulty lies in the marginal constant $a_{\mathrm{tail}} = 1$ established by the N3 results of the program.

*Precise question:* Is $a_{\mathrm{tail}}(X) = \sup_{f} Q_{\mathrm{prim},>X}(f,f) / Q_\infty(f,f)$ strictly less than 1 for some finite $X$, or is it identically equal to 1 in the limit?

**Priority 2 (Foundations of the space $\mathcal{K}$): V.1.**

Verify the $Q$-symmetry of $H_C$ via the adelic Weil formula. This is the foundation of all of Direction B: without V.1, the Pontryagin space $(\mathcal{K}, Q)$ with $H_C$ as a $Q$-selfadjoint operator is not defined.

**Priority 3 (Exploration of C7): Eigenvector system.**

Although the completeness of the eigenvector system with real eigenvalues is circular if the reality of the eigenvalues is assumed, there is a non-circular question: is the eigenvector system of $H_C$ with **purely imaginary** eigenvalues (on-line zeros) $Q$-complete in the positive subspace $\mathcal{K}_+$? If this is verified, it would mean that $\mathcal{K}_+$ is generated by the on-line zeros, and then the existence of $\mathcal{K}_-$ (the negative part) would depend entirely on the off-line zeros. This does not prove that $\kappa = 0$, but it makes the structure more transparent.

---

### Section 9.4 — Final evaluation: is Direction B promising?

**Frank answer:** Direction B is the correct formulation of the problem in operator language, but it does not provide new tools that overcome the intrinsic difficulty of RH.

**What Direction B gives:**
- A precise language: $\kappa = 0 \iff$ RH, with the operator $H_C$ as the central object.
- The Kreĭn–Langer theorem as a free bound: if there are $m$ off-line orbits, $H_C$ has at most $m$ pairs of complex eigenvalues.
- Condition C5 as the only route to an unconditional result (weaker than RH).
- The Livsic characteristic function as a mirror of the zero structure of $\xi$.

**What Direction B does not give:**
- Any condition verifiable from global properties of $\zeta$ that implies $\kappa = 0$.
- An independent lever that is not equivalent to RH.
- A route that avoids the Hadamard obstacle in its version for Direction B.

**The fundamental obstacle** is the same as in the CCM direction (though in different form): proving $\kappa = 0$ requires, in every route explored, proving that the zeros of $\zeta$ do not move away from the critical line. There is no operator-theoretic argument that forces $\kappa = 0$ without using this information.

Direction B is not "blocked" in the sense of being refuted: it has not been shown to be impossible to prove $\kappa = 0$ without knowing the positions of the zeros. But neither has any tool been found that opens a genuinely new path.

---

## Appendix A — Review of the Pontryagin/Kreĭn theorems used

### A.1 — Precise references

**Pontryagin's theorem (1944).** L.S. Pontryagin, "Hermitian operators in spaces with indefinite metric," Izv. Akad. Nauk SSSR Ser. Mat. 8 (1944), 243–280. 
*Statement:* Every hermitian operator in a Pontryagin space $\Pi_\kappa$ has at least $\kappa$ real or complex eigenvalues, counting multiplicities.

**Kreĭn–Langer spectral theorem (1963).** M.G. Kreĭn and H. Langer, "On the spectral theory of linear pencils in spaces with two norms," Funktsional. Anal. i Prilozen. (1963). [Russian translation; the accessible version is in the Azizov–Iokhvidov book.]
*Statement:* Selfadjoint operators in $\Pi_\kappa$ have at most $\kappa$ pairs of non-real eigenvalues.

**Azizov–Iokhvidov (1989).** T.Ya. Azizov and I.S. Iokhvidov, "Linear Operators in Spaces with an Indefinite Metric," Wiley, 1989.
*Standard reference* for the theory of operators in spaces with an indefinite form, including Pontryagin spaces, Kreĭn spaces, and their generalizations.

**Langer (1982).** H. Langer, "Spectral functions of definitizable operators in Kreĭn spaces," Functional Analysis (Dubrovnik 1981), Lecture Notes in Math. 948, Springer, 1982.
*Statement of the definitizability theorem.*

**Livsic–Yantsevich (1979).** M.S. Livsic and A.A. Yantsevich, "Operator Colligations in Hilbert Spaces," Wiley, 1979. (Translation of the 1971 Russian original.)
*For the Livsic characteristic function.*

**Alpay–Dijksma–Rovnyak–de Snoo (1997).** D. Alpay, A. Dijksma, J. Rovnyak, H.S.V. de Snoo, "Schur Functions, Operator Colligations, and Reproducing Kernel Pontryagin Spaces," Birkhäuser, 1997.
*For the characteristic function in Pontryagin spaces.*

---

### A.2 — Diagram of implications

```
RH
 ↕
Q(f,f) ≥ 0 ∀f  (C1)
 ↕
neg.ind(H_C) = 0  ←→  κ = 0
 ↑                     ↑
 C2: H_C ≥ cI          C5: a_tail < 1 → κ < ∞ (weaker)
 ↑                     
 C3: spectrum ⊂ iℝ     
 ↕
 C4: Θ analytic on ℂ \ iℝ
 ↕
 ξ has no zeros off ℜ(s) = 1/2
 ↕
 RH
```

All conditions C1–C4 are equivalences with RH. Condition C5 is strictly weaker.

---

## Appendix B — The program's context

This document is part of Phase 34 (new directions), which follows the blockage of the CCM direction (Phase 32–33, Docs 53–90). Direction B is independent of the CCM in the following sense: it does not use the noncommutative geometry of Connes–Consani nor the machinery of spectral triples. Instead, it uses the operator reformulation of the Pontryagin space as the working space.

However, the operator $H_C$ is the same Connes operator in both directions. The difference lies in the **perspective**: 
- The CCM direction analyzes $H_C$ as an operator in a spectral triple.
- Direction B analyzes $H_C$ as an operator in a Pontryagin space.

Both perspectives are blocked by the same fundamental obstacle: proving spectral properties of $H_C$ that imply the absence of zeros off the critical line.

---

*End of Doc 91.*

**Document status:** Complete analysis of Direction B. All routes investigated. The fundamental obstacle is identified. No route closes the argument for $\kappa = 0$. Condition C5 remains as the only route to a weaker unconditional result.

**Suggested next step:** Explicit computation of $a_{\mathrm{tail}}(X)$ as a function of $X$, to determine whether the marginal constant $a_{\mathrm{tail}} = 1$ holds or breaks down when restricting to the prime tail.
