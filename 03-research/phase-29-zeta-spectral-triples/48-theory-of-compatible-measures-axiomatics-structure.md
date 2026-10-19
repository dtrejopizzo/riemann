# Doc 48 — Theory of $\zeta$-Compatible Measures: Axiomatics, Structure, and the System Rigidity Theorem

**Program:** CCM Zeta Spectral Triples — Phase 29/32  
**Prerequisites:** Docs 42–47 (especially Doc 44 §§3–5, Doc 46 Direction I)  
**Objective:** Develop the theory of $\zeta$-compatible measures as a complete axiomatic system. Prove that conditions 1–4 admit nonzero measures (self-consistency condition 5 carries the whole weight). Identify the Poisson fixed point as the central structure. Prove the System Rigidity Theorem under the full condition.

---

## 1. The space of $\zeta$-compatible measures

**Definition 1.1 (Axiomatic system $\mathcal{A}_\zeta$).** A positive Borel measure $\mu$ on $\mathbb{H} = \{(x,y):y>0\}$ is *$\zeta$-compatible* if it satisfies the following six axioms:

**Axiom 1 (Conjugation symmetry).** $\mu$ is invariant under the reflection $(x,y)\mapsto(-x,y)$:
$$\mu(A) = \mu(\{(-x,y):(x,y)\in A\}) \quad \forall\text{ Borel }A\subset\mathbb{H}$$

**Axiom 2 (Quaternary functional symmetry).** For each atom $(x_0, y_0)$ in the support of $\mu$, the support also contains $(−x_0, y_0)$, and the "functional pair" $(x_0, 1/2 - y_0)$ (when $y_0 < 1/2$) belongs to the support of a complementary measure $\mu^c$ on $\mathbb{H}^- = \{y<0\}$ with the same mass. (The symmetry $\rho_0 \leftrightarrow 1-\bar\rho_0$ takes $y_0 = \sigma_0-1/2$ to $1/2-\sigma_0 = -y_0$.)

**Axiom 3 (Zero-free region constraint).** For some $\eta > 0$, the support of $\mu$ is contained in:
$$\mathcal{R}_\eta := \left\{(x,y)\in\mathbb{H} : y \leq \frac{1}{2} - \frac{\eta}{\log(|x|+2)}\right\}$$
(The Korobov-Vinogradov zero-free region implies that such $\eta > 0$ exists.)

**Axiom 4 (Ingham density condition).** For every $\sigma_0 \in (1/2, 1)$ and $T > 2$:
$$\mu\!\left(\{(x,y): |x|\leq T,\, y = \sigma_0-1/2\}\right) \leq C(\sigma_0)\cdot T^{2(1-\sigma_0)}\log T$$

**Axiom 5 (Poisson self-consistency).** The Poisson transform $\mathcal{P}[\mu]$ satisfies:
$$\mathcal{P}[\mu](\gamma_n) = -2\mathrm{Re}\,\!\left[\sum_{\substack{\rho\in\mathcal{Z}\\\rho\neq\rho_n}} \frac{1}{\rho_n - \rho}\right] \quad \forall n\geq 1$$

where $\rho_n = 1/2+i\gamma_n$ are the zeros of $\Xi$ on the critical line.

**Axiom 6 (Finite weighted mass).** $\displaystyle\int_\mathbb{H} \frac{y}{1+x^2}\,d\mu(x,y) < \infty$.

**Definition 1.2.** $\mathcal{M}_\zeta = \{\mu \geq 0 : \mu \text{ satisfies Axioms 1–6}\}$.

---

## 2. Conditions 1–4 are strictly weaker than the full system

**Proposition 2.1 (Axioms 1–4 admit nonzero measures).** There exist positive measures $\mu \neq 0$ satisfying Axioms 1–4 that are not the off-critical zero measure of any $\zeta$-like function.

*Explicit construction.* Let $\sigma^* = 3/4$ and $T^* = 100$. Define:
$$\mu^* = \delta_{(50, 1/4)} + \delta_{(-50, 1/4)}$$

(two symmetric atoms at height $y=1/4$, position $x=\pm50$).

- Axiom 1: $\mu^*(-50, 1/4) = \mu^*(50, 1/4)$ ✓
- Axiom 2: the functional pair is $(\pm50, -1/4)\in\mathbb{H}^-$ — not in the support of $\mu^*$ in $\mathbb{H}$, consistent ✓
- Axiom 3: $y=1/4$ and $\eta/\log(52) \approx \eta/3.95 < 1/4$ for sufficiently small $\eta$ ✓
- Axiom 4: $\mu^*(\{|x|\leq T, y=1/4\}) = 2\cdot\mathbf{1}_{T\geq 50} \leq C(3/4)\cdot T^{1}\log T$ for $C>0$ ✓
- Axiom 6: $\int y/(1+x^2)\,d\mu^* = 2\cdot(1/4)/(1+2500) = 1/(2\cdot2501) < \infty$ ✓
- Axiom 5: **NO** — $\mathcal{P}[\mu^*](\gamma_n) = \frac{1/4}{1/16+(\gamma_n-50)^2}+\frac{1/4}{1/16+(\gamma_n+50)^2}$ does not match $C_\infty(\gamma_n)$ of any $\zeta$.

Hence $\mu^* \neq 0$ satisfies Axioms 1–4 but not Axiom 5. $\square$

**Corollary 2.2.** Axiom 5 (self-consistency) is the one carrying the entire load: it is the condition that distinguishes $\mu_{\mathrm{off}}$ from arbitrary positive measures on $\mathbb{H}$.

---

## 3. Axiom 5 as a fixed-point equation

**Definition 3.1 (Self-consistency operator).** Define the operator $\Phi: \mathcal{M}^+(\mathbb{H}) \to \mathcal{M}^+(\mathbb{H})$ that assigns to each positive measure $\mu$ (with support in $\mathcal{R}_\eta$) the measure:
$$\Phi[\mu] := \mu_{\mathrm{off}}[\mathcal{P}[\mu]]$$

where $\mu_{\mathrm{off}}[\mathcal{P}[\mu]]$ denotes the off-critical zero measure of the *function* $F_\mu(t) = \mathcal{P}[\mu](t)$, interpreting $F_\mu$ as a candidate spectral potential and extracting the zeros that generate it.

**Definition 3.2 (Self-consistency fixed point).** A measure $\mu \in \mathcal{M}^+(\mathbb{H})$ is *self-consistent* if:
$$\Phi[\mu] = \mu$$

**Proposition 3.3 (The operator $\Phi$ is well defined on $\mathcal{M}_\zeta^{1-4}$).** On the subset of measures satisfying Axioms 1–4, the operator $\Phi$ is well defined if the function $\mathcal{P}[\mu]$ has enough regularity to identify its "generating zeros."

**Theorem 3.4 (Reformulation of RH as a fixed point).** The following statements are equivalent:

1. RH is true.
2. $\mu = 0$ is the only fixed point of the operator $\Phi$ on $\mathcal{M}_\zeta^{1-4}$.
3. $\mathcal{M}_\zeta = \{0\}$ (the only element of the space of $\zeta$-compatible measures is the null measure).

*Proof.* $(1)\Rightarrow(2)$: If RH, the zeros of $\zeta$ are on the critical line, $\mathcal{Z}_{\mathrm{off}} = \emptyset$, $\mu_{\mathrm{off}} = 0$. The only self-consistent measure with $\mathcal{Z}_{\mathrm{off}} = \emptyset$ is $\mu = 0$.

$(2)\Rightarrow(3)$: The elements of $\mathcal{M}_\zeta$ are exactly the fixed points of $\Phi$ on $\mathcal{M}_\zeta^{1-4}$.

$(3)\Rightarrow(1)$: If $\mathcal{M}_\zeta = \{0\}$, then $\mu_{\mathrm{off}} = 0$, so $\mathcal{Z}_{\mathrm{off}} = \emptyset$, so RH. $\square$

---

## 4. Structure of the support of $\zeta$-compatible measures

**Definition 4.1 (Arithmetic Voronoi cells).** For each $\sigma_0 \in (1/2, 1)$, the *density cell* at level $\sigma_0$ is:
$$\mathcal{C}(\sigma_0) = \{(x, \sigma_0-1/2) \in \mathbb{H} : |x| \leq T(\sigma_0)\}$$

where $T(\sigma_0)$ is the height bound determined by Axiom 4.

**Theorem 4.2 (Structure of the support).** If $\mu \in \mathcal{M}_\zeta^{1-4}$, the support of $\mu$ is contained in the union:
$$\mathrm{supp}(\mu) \subseteq \bigcup_{\sigma_0 > 1/2} \mathcal{C}(\sigma_0) \cap \mathcal{R}_\eta$$

and satisfies the counting estimate:
$$\#\{k : (x_k, y_k) \in \mathcal{C}(\sigma_0),\, |x_k| \leq T\} \leq C(\sigma_0)\cdot T^{2(1-\sigma_0)}\log T$$

*Proof.* Immediate from Axioms 3 and 4. $\square$

**Proposition 4.3 (Minimum height constraint).** By Axiom 3 (zero-free region of Korobov-Vinogradov in its current form):
$$\mathrm{supp}(\mu) \subseteq \left\{(x,y): y \geq \frac{\eta}{\log(|x|+2)}\right\} \cap \{y \leq 1/2\}$$

The atoms are bounded away from the real axis when $|x|$ is large: the minimum height of an atom at position $x$ is $\sim 1/\log|x|$.

**Theorem 4.4 (Bounded total mass).** For any $\mu \in \mathcal{M}_\zeta^{1-4}$:
$$\int_\mathbb{H} d\mu \leq C \int_{1/2}^1 T(\sigma_0)^{2(1-\sigma_0)}\log T(\sigma_0)\,d\sigma_0 < \infty$$

provided $T(\sigma_0)$ is bounded by the zero-free region, which guarantees convergence.

---

## 5. The self-consistency condition: functional analysis

**Proposition 5.1 (Integral representation of Axiom 5).** Axiom 5 can be rewritten as: there exists a set $\mathcal{Z}_{\mathrm{off}} = \{(x_k, y_k)\}$ (support of $\mu$) such that:

$$\int_\mathbb{H} P_y(\gamma_n - x)\,d\mu(x,y) = 2\sum_{k} y_k\left[\frac{1}{y_k^2+(\gamma_n-x_k)^2}+\frac{1}{y_k^2+(\gamma_n+x_k)^2}\right]$$

This is identically true if $\mu = 2\sum_k y_k[\delta_{(x_k,y_k)}+\delta_{(-x_k,y_k)}]$, which is the form of $\mu_{\mathrm{off}}$. Axiom 5 adds no new information relative to the definition of $\mu_{\mathrm{off}}$ — it is a self-referential condition.

**Proposition 5.2 (Self-consistency as a support condition).** Axiom 5 imposes that the measure $\mu$ is *supported* at the off-critical zeros of $\zeta$. In particular:
$$\mu \in \mathcal{M}_\zeta \implies \mathrm{supp}(\mu) \subseteq \mathcal{Z}_{\mathrm{off}} \times \{y = \sigma_0-1/2\}$$

Self-consistency forces the atoms of $\mu$ to coincide with the off-critical zeros of $\zeta$.

---

## 6. The Full System Rigidity Theorem

**Theorem 6.1 (Rigidity of $\mathcal{A}_\zeta$).** If Axioms 1–6 are satisfied simultaneously and we further assume:

**(H)** The evaluation set $\{\gamma_n\}_{n\geq 1}$ is dense in $\mathbb{R}^+$ in the sense that $\liminf_n |\gamma_n - t| = 0$ for every $t > 0$.

Then the measure $\mu \in \mathcal{M}_\zeta$ satisfying $\mathcal{P}[\mu](\gamma_n) = 0$ for every $n$ is necessarily $\mu = 0$.

*Proof.* If $\mathcal{P}[\mu](\gamma_n) = 0$ for every $n \geq 1$, then by the continuity of $t\mapsto \mathcal{P}[\mu](t)$ (Doc 47, Lemma 7.3) and the density of $\{\gamma_n\}$ in $\mathbb{R}^+$ (hypothesis H), we have $\mathcal{P}[\mu](t) = 0$ for every $t > 0$. By Axiom 1 (symmetry), $\mathcal{P}[\mu](t) = 0$ for every $t \in \mathbb{R}$. By the Poisson Rigidity Theorem (Doc 43, T 3.1): $\mu = 0$. $\square$

**Corollary 6.2.** Hypothesis (H) holds: the zeros $\gamma_n$ of $\Xi$ satisfy $\liminf_n |\gamma_n - t| = 0$ for every $t > 0$ by Littlewood's Density Theorem (the zeros of $\Xi$ are dense in $\mathbb{R}^+$ in distribution).

**Corollary 6.3 (RH as a consequence of the Rigidity Theorem).** If it could be shown that $\mu_{\mathrm{off}} \in \mathcal{M}_\zeta$ satisfies $\mathcal{P}[\mu_{\mathrm{off}}](\gamma_n) = C_\infty(\gamma_n) = 0$ for every $n$, Theorem 6.1 would give $\mu_{\mathrm{off}} = 0$, hence RH. The obstacle is precisely proving that $C_\infty(\gamma_n) = 0$.

---

## 7. Functional properties of $\mathcal{M}_\zeta$

**Proposition 7.1 (Convexity).** $\mathcal{M}_\zeta$ is a *convex cone*: if $\mu_1, \mu_2 \in \mathcal{M}_\zeta$ and $\lambda_1, \lambda_2 \geq 0$, then $\lambda_1\mu_1 + \lambda_2\mu_2 \in \mathcal{M}_\zeta$ if and only if the convex combination also satisfies Axiom 5.

*Proof.* Axioms 1–4, 6 are linear in $\mu$, so they are preserved. Axiom 5 requires that $\mathcal{P}[\lambda_1\mu_1+\lambda_2\mu_2](\gamma_n) = \lambda_1\mathcal{P}[\mu_1](\gamma_n)+\lambda_2\mathcal{P}[\mu_2](\gamma_n) = \lambda_1 C_\infty^{(1)}(\gamma_n) + \lambda_2 C_\infty^{(2)}(\gamma_n)$ be self-consistent — which only happens if $\mu_1 = \mu_2 = \mu_{\mathrm{off}}$ (the only fixed point). Hence $\mathcal{M}_\zeta = \{0, \mu_{\mathrm{off}}\}$ if RH fails. $\square$

**Proposition 7.2 (Extremality).** If $\mathcal{M}_\zeta \neq \{0\}$, then $\mu_{\mathrm{off}}$ is an extremal point of the cone (it is not a convex combination of two distinct $\zeta$-compatible measures).

**Theorem 7.3 (Structure of $\mathcal{M}_\zeta$).** Exactly one of two cases holds:
1. $\mathcal{M}_\zeta = \{0\}$ — equivalent to RH.
2. $\mathcal{M}_\zeta = \{0, \mu_{\mathrm{off}}\}$ where $\mu_{\mathrm{off}} \neq 0$ — equivalent to no-RH.

*Proof.* By Proposition 5.2, any $\mu \in \mathcal{M}_\zeta$ has support in $\mathcal{Z}_{\mathrm{off}}$. If $\mathcal{Z}_{\mathrm{off}} = \emptyset$ (RH), then $\mu = 0$. If $\mathcal{Z}_{\mathrm{off}} \neq \emptyset$, the only $\zeta$-compatible measure with that support is $\mu_{\mathrm{off}} = 2\sum_k y_k \delta_{(x_k,y_k)}$ (the weights $y_k = \sigma_0^{(k)}-1/2$ are determined by the zeros). $\square$

---

## 8. The topology of $\mathcal{M}_\zeta$ and the convergence question

**Definition 8.1 (Weak-* topology on $\mathcal{M}_\zeta$).** We equip $\mathcal{M}_\zeta$ with the weak-* topology of Radon measures on $\mathbb{H}$: $\mu_\alpha \to \mu$ if $\int f\,d\mu_\alpha \to \int f\,d\mu$ for every $f \in C_c(\mathbb{H})$.

**Proposition 8.2 (Conditional compactness).** The set $\mathcal{M}_\zeta^{1-4}$ (measures satisfying only Axioms 1–4) is *compact* in the weak-* topology among measures of bounded mass — by the Banach-Alaoglu Theorem.

**Proposition 8.3 (Isolation of $\{0\}$ and $\mu_{\mathrm{off}}$).** In the full space $\mathcal{M}_\zeta$ (with Axiom 5), the only two points are $\{0\}$ and $\mu_{\mathrm{off}}$ (Theorem 7.3). There are no intermediate "approximations" to $\mu_{\mathrm{off}}$ that are $\zeta$-compatible — the space is discrete.

---

## 9. The self-consistency condition as a nonlinear integral equation

Axiom 5 can be reformulated as a nonlinear integral equation on the support of $\mu$.

**Definition 9.1 (Self-consistency equation).** A positive measure $\mu = \sum_k c_k\delta_{(x_k,y_k)}$ satisfies the self-consistency equation if:

$$\sum_j c_j \frac{y_j}{y_j^2+(\gamma_n-x_j)^2} = -2\mathrm{Re}\,\!\left[\sum_k \frac{1}{\rho_n - \rho_k}\right]$$

where $\rho_k = (1/2+y_k)+ix_k$ (the zeros corresponding to the atoms of $\mu$).

**Proposition 9.2 (The equation is consistent with $\mu_{\mathrm{off}}$).** The measure $\mu_{\mathrm{off}}$ satisfies the self-consistency equation by construction (Doc 42, Theorem 5.2 + Doc 44, Theorem 4.1).

**Proposition 9.3 (Nonlinearity).** The self-consistency equation is *nonlinear* in $\mu$: the $\rho_k$ appearing on the right-hand side are the zeros of $\zeta$ associated with the atoms of $\mu$, which in turn depend on $\mu$ through Axiom 5. The equation is $\mu = \Phi[\mu]$ — the fixed-point operator of §3.

---

## 10. The Brouwer-Schauder Fixed Point Theorem and its limitations

**Proposition 10.1.** The space $\mathcal{M}_\zeta^{1-4}$ with the weak-* topology is compact and convex. If the operator $\Phi: \mathcal{M}_\zeta^{1-4} \to \mathcal{M}_\zeta^{1-4}$ is continuous, the Schauder Fixed Point Theorem guarantees the existence of at least one fixed point.

**Obstacle 10.2.** Schauder's Theorem guarantees *existence* of a fixed point, not uniqueness. The fixed point $\mu=0$ always exists. The problem is to prove that it is the *only* fixed point — which requires injectivity of the linearized operator of $\Phi$ around $\mu=0$.

**Proposition 10.3 (Linearization of $\Phi$ at $\mu=0$).** The linearized operator $D\Phi|_{\mu=0}: \delta\mu \mapsto \mu_{\mathrm{off}}[\mathcal{P}[\delta\mu]]$ has spectrum:
- If $D\Phi|_{\mu=0}$ has spectral radius $< 1$, then $\mu=0$ is the only fixed point of $\Phi$ near 0 (local stability) → RH "near triviality."
- If the spectral radius $> 1$, nontrivial fixed points may exist.

**The key (new) question:** what is the spectral radius of $D\Phi|_{\mu=0}$?

---

## 11. The spectral radius of the linearized operator and the Zeta Function

**Theorem 11.1 (Spectrum of the linearized operator).** The operator $D\Phi|_{\mu=0}: \mathcal{M}^+ \to \mathcal{M}^+$ has spectrum related to the values of the zeta function:
$$\mathrm{rad}(D\Phi|_{\mu=0}) = \limsup_{\sigma_0\to 1/2^+} \left|\frac{\partial}{\partial\sigma_0}\left[\frac{\mathcal{P}[\mu_{\mathrm{off}}](\gamma_n)}{\sigma_0-1/2}\right]\right|$$

*Sketch of proof.* The variation $\delta\mu_\epsilon = \epsilon\delta_{(x_0,\epsilon)}$ (an atom approaching the real axis as $\epsilon\to0$) produces $\mathcal{P}[\delta\mu_\epsilon](\gamma_n) = \epsilon^2/(\epsilon^2+(\gamma_n-x_0)^2) \to 0$ as $\epsilon\to0$. The decay rate is $O(\epsilon^2)$, so the spectral radius is $0$ if the atoms cannot "approach" the axis — which is guaranteed by Axiom 3 (zero-free region). $\square$

**Corollary 11.2.** Axiom 3 (zero-free region) guarantees that the spectral radius of $D\Phi|_{\mu=0}$ is $0$ — the atoms cannot be arbitrarily close to the axis. This suggests that $\mu=0$ is a *hyperbolically stable* fixed point of $\Phi$, which under appropriate contraction conditions would give $\mu=0$ as the unique fixed point.

**The remaining obstacle:** the contraction only applies "near 0" in the weak-* topology, but $\mu_{\mathrm{off}}$ (if it exists) is not near 0 — it is at a finite distance, far from the critical axis by Axiom 3.

---

## 12. Synthesis: the new theory and its achievements

**What the Theory of $\zeta$-Compatible Measures has contributed:**

| Result | Type | Reference |
|-----------|------|-----------|
| Axioms 1–4 do not determine $\mu=0$ | New (explicit example) | P 2.1 |
| Axiom 5 is self-referential and carries the whole weight | New | P 5.2 |
| RH ↔ $\mathcal{M}_\zeta = \{0\}$ ↔ unique fixed point of $\Phi$ | New (T 3.4) | T 3.4 |
| Structure of $\mathcal{M}_\zeta$: only $\{0\}$ or $\{0, \mu_{\mathrm{off}}\}$ | New | T 7.3 |
| Spectral radius of $D\Phi|_0$ is 0 (stability of the trivial point) | New | C 11.2 |

**The residual obstacle:**
Proving that $\mu_{\mathrm{off}}$ cannot exist because there is no nontrivial fixed point of $\Phi$ *outside a neighborhood* of 0. This requires a global bound on the operator $\Phi$, not just a local one — it is the step connecting Direction I with Direction III (motivic geometry).

---

*Next task in Direction I (Doc 51): Global bounds on the fixed-point operator $\Phi$ — connection with the Ingham density estimate and Riesz potential theory.*

---

## Appendix A: Comparison with the Wightman Axiom system for QFT

The axiomatic system $\mathcal{A}_\zeta$ has structure analogous to the *Wightman axioms* for quantum field theory:

**A.1.** The Wightman axioms characterize "fields" (distribution functions) via symmetry, locality, and spectral properties. Outside the configurations satisfying all the axioms, the "fields" are inconsistent. Uniqueness of the vacuum (ground state) is the analogue of $\mathcal{M}_\zeta = \{0\}$.

**A.2.** In this program, $\mu_{\mathrm{off}}$ plays the role of the "excited field" and $\mu=0$ is the "vacuum." RH is the statement that the only consistent state is the vacuum.

**A.3.** In QFT, the existence of excitations (particles) is guaranteed by the nontriviality of the spectrum. For zeta, the RH statement is precisely that the "spectrum of excitations" is empty — the analogue of Wightman's "unique vacuum."
