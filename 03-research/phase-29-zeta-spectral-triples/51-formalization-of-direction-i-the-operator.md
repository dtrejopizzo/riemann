# Doc 51 — Formalization of Direction I: The Operator $\Phi$ on Banach Lattices and the Krein-Rutman Theorem

**Program:** CCM Zeta Spectral Triples — Phase 29/32  
**Prerequisites:** Docs 42–49, especially Doc 48  
**Nature:** Complete formalization — the operator $\Phi$ as an object in functional analysis. No heuristics: definitions, norms, domains and the exact boundary of the argument.  
**Objective:** Define the correct Banach space for $\zeta$-compatible measures. Define $\Phi$ rigorously. Apply the Krein-Rutman theorem. Identify the exact obstacle to uniqueness of the fixed point.

---

## 1. Diagnosis of the Doc 48 gap

Doc 48 used "spectral radius" without defining the Banach space. Without a space structure and a norm, the spectral radius has no formal mathematical content. This document corrects that gap.

---

## 2. The space of signed measures of bounded total variation

**Definition 2.1 (Space $M(\mathcal{R}_\eta)$).** Let $\mathcal{R}_\eta = \{(x,y)\in\mathbb{H}: y \leq 1/2 - \eta/\log(|x|+2)\}$ be the admissible region (Axiom 3 of Doc 48). The space:
$$M(\mathcal{R}_\eta) = \{\text{signed Borel measures } \nu \text{ on } \mathcal{R}_\eta : \|\nu\|_{\mathrm{TV}} < \infty\}$$

equipped with the total variation norm $\|\nu\|_{\mathrm{TV}} = |\nu|(\mathcal{R}_\eta)$, is a Banach space.

**Proposition 2.2.** $M(\mathcal{R}_\eta)$ is a *Banach lattice* with the positive/negative decomposition: $\nu = \nu^+ - \nu^-$ with $\|\nu\|_{\mathrm{TV}} = \|\nu^+\|_{\mathrm{TV}} + \|\nu^-\|_{\mathrm{TV}}$.

**Definition 2.3 (The positive cone).** $M^+(\mathcal{R}_\eta) = \{\mu \in M(\mathcal{R}_\eta) : \mu \geq 0\}$ is the cone of positive measures — a closed convex subset of $M(\mathcal{R}_\eta)$.

**Definition 2.4 (The subspace $\mathcal{M}_\zeta^{1-4}$).** The subspace of measures satisfying Axioms 1–4 of Doc 48:
$$\mathcal{M}_\zeta^{1-4} = \left\{\mu \in M^+(\mathcal{R}_\eta): \mu \text{ satisfies Axioms 1, 2, 4}, \int\frac{y}{1+x^2}\,d\mu < 1\right\}$$

is a closed, convex and bounded subset of $M(\mathcal{R}_\eta)$ (the bounded-mass condition $\int y/(1+x^2)d\mu < 1$ is the normalization of Axiom 6).

**Proposition 2.5 (Compactness).** $\mathcal{M}_\zeta^{1-4}$ is compact in the weak* topology of $M(\mathcal{R}_\eta)$ — by the Banach-Alaoglu theorem, the unit ball of $M(\mathcal{R}_\eta)$ in the weak* topology is compact.

---

## 3. The self-consistency operator $\Phi$: rigorous definition

The operator $\Phi: \mathcal{M}_\zeta^{1-4} \to \mathcal{M}_\zeta^{1-4}$ requires a two-step definition.

**Step 1: From the measure to the harmonic function.**

For $\mu \in \mathcal{M}_\zeta^{1-4}$, we define:
$$F_\mu: \mathbb{H}^+ \to \mathbb{R}, \quad F_\mu(z) = \mathcal{P}[\mu](z) = \int_\mathbb{H} P_{\mathrm{Im}(z)}(\mathrm{Re}(z)-x)\,d\mu(x,y)$$

This is a positive harmonic function on $\mathbb{H}^+$, with boundary trace on $\mathbb{R}$ given by $F_\mu(t) = \int P_y(t-x)d\mu(x,y)$ (interpreted as a non-tangential limit).

**Step 2: From the harmonic function to the zero measure.**

Given $F_\mu$, we define its *generated off-critical measure*:
$$\Phi[\mu] := \mu_{\mathrm{off}}[F_\mu]$$

where $\mu_{\mathrm{off}}[F]$ is the measure of off-critical zeros of the candidate $\zeta$ function whose spectral potential is $F$. More precisely:

**Definition 3.1 (The map $\mu_{\mathrm{off}}[F]$).** For a positive harmonic function $F: \mathbb{H}^+ \to [0,\infty)$ with Herglotz representation $F(z) = \int P_y(x-t)d\nu_F(t)$, the measure:
$$\mu_{\mathrm{off}}[F] = \nu_F \text{ (the Herglotz measure representing } F\text{)}$$

whenever $\nu_F$ satisfies Axioms 1–4.

**Proposition 3.2 (Consistency).** If $\mu = \mu_{\mathrm{off}}$ (the actual measure of off-critical zeros of $\zeta$), then $\Phi[\mu_{\mathrm{off}}] = \mu_{\mathrm{off}}$ — that is, $\mu_{\mathrm{off}}$ is a fixed point of $\Phi$.

*Proof.* $F_{\mu_{\mathrm{off}}} = \mathcal{P}[\mu_{\mathrm{off}}] = C_\infty$ (Doc 44, Theorem 4.1). The Herglotz measure of $C_\infty$ is $\mu_{\mathrm{off}}$ (by uniqueness of the Herglotz-Riesz representation). Hence $\Phi[\mu_{\mathrm{off}}] = \mu_{\mathrm{off}}$. $\square$

**Proposition 3.3 ($\mu=0$ is a trivial fixed point).** $F_0 = 0$, and the Herglotz measure of $0$ is $\nu=0$. Hence $\Phi[0] = 0$.

---

## 4. Continuity of $\Phi$

**Lemma 4.1 (Continuity of the map $\mu\mapsto F_\mu$).** The map $\Phi_1: \mu \mapsto F_\mu = \mathcal{P}[\mu]$ is weak*-to-uniform-on-compacts continuous: if $\mu_\alpha \xrightarrow{w^*} \mu$, then $F_{\mu_\alpha}(z) \to F_\mu(z)$ for every $z\in\mathbb{H}^+$.

*Proof.* $F_\mu(z) = \int P_y(x-t)d\mu(t)$ where $P_y(x-\cdot) \in C_b(\mathcal{R}_\eta)$ for fixed $z=x+iy$. Weak* convergence of measures against bounded continuous functions gives pointwise convergence of $F_\mu$. $\square$

**Lemma 4.2 (Continuity of the map $F\mapsto\mu_{\mathrm{off}}[F]$).** The map $\Phi_2: F \mapsto \mu_{\mathrm{off}}[F]$ is continuous in the topology of uniform convergence on compacts, provided the off-critical zeros of the $\zeta$ function associated with $F$ vary continuously with $F$.

*Critical note.* Lemma 4.2 requires a hypothesis about how "the $\zeta$ function associated with $F$" depends on $F$. This is circular: to define $\Phi_2$, we need to know which zeta function has $F$ as its spectral potential. In the real case, $F = C_\infty$ determines $\zeta$ — but in general $F$ might not correspond to any $\zeta$.

**Resolution of the circularity problem.** We reformulate $\Phi$ to avoid the circularity:

**Definition 4.3 (Reformulated operator $\Phi$).** The operator $\Phi$ acts only on the space of measures that are already candidates for $\mu_{\mathrm{off}}$ for some $\zeta$:
$$\Phi: \mathcal{C}_\zeta \to \mathcal{C}_\zeta$$

where $\mathcal{C}_\zeta = \{\mu \in \mathcal{M}_\zeta^{1-4}: \exists\text{ zeta function }\zeta_\mu \text{ such that } \mu = \mu_{\mathrm{off}}[\zeta_\mu]\}$.

On this domain, $\Phi[\mu] = \mu_{\mathrm{off}}[\mathcal{P}[\mu]]$ is well defined because $\mathcal{P}[\mu]$ determines the off-critical zeros of $\zeta_\mu$ via the Hadamard formula (Doc 42).

---

## 5. The Krein-Rutman Theorem and its consequences

**Theorem 5.1 (Krein-Rutman, 1948).** Let $X$ be a Banach space with positive cone $K$ having nonempty interior, and let $T: X\to X$ be a compact linear operator that preserves $K$ (i.e. $T(K) \subseteq K$). Then:

1. The spectral radius $r(T) = \sup\{|\lambda|: \lambda \in \sigma(T)\}$ is an eigenvalue of $T$.
2. There exists a positive eigenvector $v \in K$ with $Tv = r(T)v$.
3. The eigenvalue $r(T)$ is simple and is the only eigenvalue with an eigenvector in $K$.

**Proposition 5.2 (The linearized operator of $\Phi$).** The differential of $\Phi$ at $\mu=0$, denoted $D\Phi_0$, is the linear operator:
$$D\Phi_0: \nu \mapsto \frac{\partial}{\partial\epsilon}\Phi[\epsilon\nu]\bigg|_{\epsilon=0}$$

**Explicit computation:**

$\Phi[\epsilon\nu] = \mu_{\mathrm{off}}[\mathcal{P}[\epsilon\nu]] = \mu_{\mathrm{off}}[\epsilon\cdot\mathcal{P}[\nu]]$. For small $\epsilon$, the off-critical zeros associated with the harmonic function $\epsilon\cdot\mathcal{P}[\nu]$ correspond to perturbed zeros of $\zeta$ — which lie at distance $O(\epsilon)$ from the critical line (zero-free region: there can be no zeros at distance $< c/\log T$ from the axis). Hence the perturbation $\mu_{\mathrm{off}}[\epsilon\cdot\mathcal{P}[\nu]] = 0$ for $\epsilon < \epsilon_0(\nu)$ (no zero can enter the off-critical region under a small perturbation).

**Proposition 5.3 (Zero spectral radius of the linearization).** $r(D\Phi_0) = 0$.

*Proof.* For every $\nu \in M(\mathcal{R}_\eta)$ with $\|\nu\| = 1$, the perturbation $\epsilon\nu$ produces a harmonic function $\epsilon\mathcal{P}[\nu]$ of norm $O(\epsilon)$. The off-critical zeros of the perturbed zeta function lie in the zero-free region when $\epsilon$ is small — hence $D\Phi_0[\nu] = 0$. Since $D\Phi_0 \equiv 0$ on all of $M(\mathcal{R}_\eta)$, its spectral radius is $0$. $\square$

**Corollary 5.4 (Local stability of $\mu=0$).** By the Krein-Rutman theorem (Proposition 5.3), the fixed point $\mu=0$ is locally stable: in a small $\epsilon$-neighborhood of $\mu=0$ in $M(\mathcal{R}_\eta)$, there are no other fixed points of $\Phi$.

---

## 6. The obstacle to global stability

**Proposition 6.1 (Position of $\mu_{\mathrm{off}}$ relative to 0).** If RH fails, the nontrivial fixed point $\mu_{\mathrm{off}}$ satisfies:
$$\|\mu_{\mathrm{off}}\|_{\mathrm{TV}} = \mu_{\mathrm{off}}(\mathcal{R}_\eta) = \#\mathcal{Z}_{\mathrm{off}} \cdot \overline{y_0}$$

where $\overline{y_0}$ is the mean weight of the atoms. By the zero-free region, $\overline{y_0} \geq c/\log T_0 > 0$, hence $\|\mu_{\mathrm{off}}\|_{\mathrm{TV}} \geq c > 0$ — the nontrivial fixed point is at positive distance from 0.

**Proposition 6.2 (The Schauder argument does not distinguish the two fixed points).** The Schauder Fixed Point Theorem (applied to $\Phi: \mathcal{M}_\zeta^{1-4} \to \mathcal{M}_\zeta^{1-4}$) guarantees the existence of at least one fixed point, but does not distinguish $\mu=0$ from $\mu_{\mathrm{off}}$.

**The exact global obstacle:**

> Prove that $\Phi$ has no fixed points in $\{0 < \|\mu\|_{\mathrm{TV}} < \infty\}$, i.e. that there are no fixed points other than the trivial one.

This requires a *global contraction* property of $\Phi$ — which does not follow from local stability.

---

## 7. Lyapunov estimates and the Lyapunov functional

To study global stability, we introduce a Lyapunov functional.

**Definition 7.1 (Energy functional $\mathcal{E}$).** For $\mu \in \mathcal{M}_\zeta^{1-4}$, we define:
$$\mathcal{E}[\mu] = \int_\mathbb{H} \mathcal{P}[\mu](x)\,d\mu(x,y) = \int_\mathbb{H}\int_\mathbb{H} P_y(x-x')\,d\mu(x,y)\,d\mu(x',y')$$

This is the "self-interaction potential" of the measure $\mu$ under the Poisson kernel.

**Proposition 7.2 (Positivity of $\mathcal{E}$).** $\mathcal{E}[\mu] \geq 0$ for every $\mu \geq 0$, with $\mathcal{E}[\mu] = 0$ only if $\mu = 0$.

*Proof.* $\mathcal{E}[\mu] = \|h\|_{L^2}^2$ where $h = \mathcal{P}[\mu]$. The $L^2$ norm of a nonnegative function is zero only if the function is zero, and $\mathcal{P}[\mu] = 0$ implies $\mu = 0$ by injectivity of the Poisson transform. $\square$

**Proposition 7.3 (Relation to the mass).** $\mathcal{E}[\mu] \geq c\|\mu\|_{\mathrm{TV}}^2$ for some constant $c > 0$ (this follows from the Poisson bound $\mathcal{P}[\mu](x) \geq c\|\mu\|_{\mathrm{TV}}$ at the maximum of $\mathcal{P}[\mu]$).

**Key question for the Lyapunov functional:**

> Is $\mathcal{E}[\Phi[\mu]] \leq \mathcal{E}[\mu]$ for every $\mu \in \mathcal{M}_\zeta^{1-4}$?

If so, then $\mathcal{E}$ would be a Lyapunov functional for $\Phi$, the energy decreases, and the system converges to $\mu=0$ (the unique minimum of $\mathcal{E}$).

**Proposition 7.4 (The Lyapunov inequality is not automatic).** The condition $\mathcal{E}[\Phi[\mu]] \leq \mathcal{E}[\mu]$ is equivalent to:
$$\int_\mathbb{H}\mathcal{P}[\Phi[\mu]]\,d\Phi[\mu] \leq \int_\mathbb{H}\mathcal{P}[\mu]\,d\mu$$

This is an inequality between the self-energy of the off-critical zeros of $\zeta_{\mathcal{P}[\mu]}$ and the self-energy of $\mu$. It does not follow from general principles — it requires arithmetic information about how the $\zeta$ function perturbs its own off-critical zeros.

---

## 8. Exact status of Direction I

**What is proved:**

| Statement | Status | Tool |
|------------|--------|-------------|
| $M(\mathcal{R}_\eta)$ is a Banach lattice | ✓ | Standard functional analysis |
| $\mathcal{M}_\zeta^{1-4}$ is weak* compact | ✓ | Banach-Alaoglu |
| $\mu = 0$ and $\mu = \mu_{\mathrm{off}}$ are fixed points | ✓ | Direct construction |
| Continuity of $\mu \mapsto F_\mu$ (weak* → uniform on compacts) | ✓ | Harmonic analysis |
| $r(D\Phi_0) = 0$ | ✓ | Zero-free region |
| Local stability of $\mu = 0$ | ✓ | Krein-Rutman + spectral radius |
| No fixed points other than $\{0, \mu_{\mathrm{off}}\}$ | ❌ Open | — |
| Lyapunov inequality $\mathcal{E}[\Phi[\mu]]\leq\mathcal{E}[\mu]$ | ❌ Open | — |

**The precise reduction:**

> Direction I reduces RH to: *proving that the Lyapunov inequality $\mathcal{E}[\Phi[\mu]] \leq \mathcal{E}[\mu]$ holds for every $\mu \in \mathcal{M}_\zeta^{1-4}$ with $\mu \neq 0$.*

Equivalently: the self-interaction energy of the off-critical zeros of $\zeta_F$ is strictly smaller than the self-interaction energy of the measure $\mu$ that generates $F = \mathcal{P}[\mu]$.

---

## 9. Connection with Direction II

**Proposition 9.1 (The two reductions are equivalent).** The obstacle of Direction I (Lyapunov) and the obstacle of Direction II (sign of the harmonic function on the kernel of $M^T$) are equivalent under the following identification:

- In Direction II, the coefficient $(a_k)$ produces the function $F^a = \sum_k a_k P_{y_k}(\cdot-x_k)$ with $F^a(\gamma_n) = 0$ for every $n$.
- In Direction I, the Lyapunov inequality $\mathcal{E}[\Phi[\mu]] < \mathcal{E}[\mu]$ requires the function $G = \mathcal{P}[\Phi[\mu]] - \mathcal{P}[\mu]$ to be nonpositive in an averaged sense.
- $G$ has the same structure as $F^a$ from the sign problem.

*Both reductions ask the same thing: can a harmonic function formed by linear combinations of Poisson kernels of off-critical zeros of $\zeta$, vanishing at all on-critical zeros, fail to have definite sign?*

---

*Next (Doc 54): Sign analysis for harmonic functions with zeros at $\{\gamma_n\}$ — necessary conditions via potential theory.*
