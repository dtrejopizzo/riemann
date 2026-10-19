# Doc 56 — Poincaré Duality on $\mathcal{MM}$: Construction, Non-Degeneracy and Why It Does Not Close

**Program:** CCM Zeta Spectral Triples — Phase 30  
**Prerequisites:** Docs 52–55  
**Frankness:** This document builds the Poincaré pairing on $\mathcal{MM}$, proves its non-degeneracy, and identifies precisely why the Deligne/Weil argument does not transfer to the arithmetic case over $\mathbb{Q}$. The result is negative but clarifying.

---

## 1. The Poincaré pairing on $\mathcal{MM}$: construction

**Recall (Doc 52).** The category $\mathcal{MM}$ has objects $(\mathcal{R}_\eta, \mu, F)$ with $F = \mathcal{P}[\mu]$, cohomology:

$$H^0(\mathcal{R}_\eta, \mu, F) = \{F|_\mathbb{R}\} \quad\text{(positive harmonic functions on the boundary)}$$
$$H^1(\mathcal{R}_\eta, \mu, F) = \mathcal{M}(\mathcal{R}_\eta)/\mathcal{N} \quad\text{(measures modulo null measures)}$$

where $\mathcal{N} = \{\nu : \mathcal{P}[\nu] = 0\} = \{0\}$ (by injectivity of $\mathcal{P}$, Proposition 2.1, Doc 53).

**Definition 1.1 (Poincaré pairing).** For the object $(\mathcal{R}_\eta, \mu, F)$, let:

$$\langle\cdot,\cdot\rangle_\Pi: H^0 \times H^1 \to \mathbb{R}$$
$$\langle f, [\nu]\rangle_\Pi := \int_{\mathcal{R}_\eta} f(x)\,d\nu(x,y)$$

where $f \in H^0$ is the boundary function and $[\nu] \in H^1$ is a class of measures.

**Remark 1.2 (Symmetry of the pairing).** By the symmetry of the Poisson transform:

$$\int_{\mathcal{R}_\eta} \mathcal{P}[\mu](x)\,d\nu(x,y) = \int_{\mathcal{R}_\eta}\!\int_\mathbb{R} P_y(t-x)\,d\mu(t)\,d\nu(x,y) = \int_\mathbb{R} \mathcal{P}[\nu](t)\,d\mu(t)$$

Hence $\langle \mathcal{P}[\mu], [\nu]\rangle_\Pi = \langle \mathcal{P}[\nu], [\mu]\rangle_\Pi$ — the pairing is symmetric in $\mu, \nu$.

---

## 2. Non-degeneracy of the pairing

**Theorem 2.1 (Non-degeneracy of the Poincaré pairing).** The pairing $\langle\cdot,\cdot\rangle_\Pi$ is non-degenerate: for $[\nu] \in H^1$,

$$\langle f, [\nu]\rangle_\Pi = 0 \;\forall f \in H^0 \implies [\nu] = 0$$

*Proof.* $H^0$ contains all functions $f = \mathcal{P}[\mu]$ with $\mu$ a positive measure on $\mathcal{R}_\eta$. By Remark 1.2:

$$\langle \mathcal{P}[\mu], [\nu]\rangle_\Pi = \int_\mathbb{R} \mathcal{P}[\nu](t)\,d\mu(t) = 0 \quad\forall \mu$$

Taking $\mu = \delta_{(t_0, y_0)}$ (point mass at $(t_0, y_0) \in \mathcal{R}_\eta$): $\mathcal{P}[\mu](x) = P_{y_0}(t_0-x)$, hence:

$$\int P_{y_0}(t-x)\,d\nu(x,y) = \mathcal{P}[\nu](t_0) = 0 \quad \forall (t_0, y_0) \in \mathcal{R}_\eta$$

Since $\mathcal{P}[\nu]$ is a continuous function on $\mathbb{R}$ vanishing on a dense set (if $\mathcal{R}_\eta$ is dense under projection to the real axis), $\mathcal{P}[\nu] \equiv 0$ on $\mathbb{R}$, hence $\nu = 0$ by injectivity of $\mathcal{P}$ (Doc 53, Proposition 2.1). $\square$

**Corollary 2.2.** The pairing $\langle\cdot,\cdot\rangle_\Pi$ is also non-degenerate in the first variable (by the symmetry of Remark 1.2 and the same argument).

**Proposition 2.3 (The pairing for the zeta object).** For the zeta object $(\mathcal{R}_\eta, \mu_{\mathrm{off}}, C_\infty)$:

$$\langle C_\infty, [\mu_{\mathrm{off}}]\rangle_\Pi = \int_{\mathcal{R}_\eta} C_\infty(x)\,d\mu_{\mathrm{off}}(x,y) = \sum_{\rho_0\in\mathcal{Z}_{\mathrm{off}}} (\sigma_0-1/2)\cdot C_\infty(\gamma_0)$$

Under ¬RH: $C_\infty(\gamma_0) > 0$ (Doc 43) and $\sigma_0-1/2 > 0$, hence $\langle C_\infty, [\mu_{\mathrm{off}}]\rangle_\Pi > 0$ — the Cohomological Positivity Conjecture (CPC) holds under ¬RH.

Under RH: $\mu_{\mathrm{off}} = 0$, hence $\langle C_\infty, [\mu_{\mathrm{off}}]\rangle_\Pi = 0$ trivially.

---

## 3. The structure of the Deligne argument and where the transfer fails

In the Weil proof for curves $C/\mathbb{F}_q$, the structure is:

**(W1)** The Frobenius $\mathrm{Fr}_q: C \to C$ is an automorphism of the curve.  
**(W2)** The Frobenius acts on $H^1(C)$ with eigenvalues $\alpha_1, \ldots, \alpha_{2g}$.  
**(W3)** The functional equation of $Z(C,s)$ gives the relation $\alpha_i \leftrightarrow q/\alpha_i$.  
**(W4)** The Weil pairing: $\langle \mathrm{Fr}_q^* \alpha, \beta\rangle_{\mathrm{Weil}} = q \langle \alpha, \mathrm{Fr}_q^{-1*} \beta\rangle_{\mathrm{Weil}}$.  
**(W5)** Cohomological positivity (Hodge): $\langle \alpha, \overline{\alpha}\rangle_{\mathrm{Weil}} > 0$ for $\alpha \neq 0$.  
**(W6)** Combining (W3)–(W5): if $\alpha_i$ is an eigenvalue, $|\alpha_i|^2 = q$ — hence $|\alpha_i| = \sqrt{q}$ (RH).

**Translation to the $\mathcal{MM}$ framework:**

| Weil ingredient | Translation to $\mathcal{MM}$ | Status |
|---|---|---|
| **(W1)** $\mathrm{Fr}_q$ as a geometric automorphism | $\Phi_\zeta$ as an endofunctor of $\mathcal{MM}$ | ✓ (Doc 52) |
| **(W2)** Eigenvalues of $\mathrm{Fr}_q$ on $H^1$ | "Eigenvalues" of $\Phi_\zeta$ on $H^1(\mathcal{MM})$ | ✗ — see §4 |
| **(W3)** Relation $\alpha_i \leftrightarrow q/\alpha_i$ (func. eq.) | Dual relation on $H^1$ via the functional equation of $\zeta$ | ✗ — see §5 |
| **(W4)** Weil pairing: $\langle\mathrm{Fr}^*\alpha,\beta\rangle = q\langle\alpha,\mathrm{Fr}^{-1*}\beta\rangle$ | Pairing $\langle\cdot,\cdot\rangle_\Pi$: does it satisfy a similar relation? | ✗ — see §6 |
| **(W5)** Hodge positivity | CPC: $\langle C_\infty, [\mu_{\mathrm{off}}]\rangle_\Pi > 0$ under ¬RH | ✓ (Proposition 2.3) |
| **(W6)** Conclusion $|\alpha_i| = \sqrt{q}$ → RH | Conclusion $H^1 = 0$ → RH | ✗ — circular without (W2)–(W4) |

---

## 4. The failure of (W2): the absence of nontrivial eigenvalues

**Proposition 4.1 (The "Frobenius" $\Phi_\zeta$ has a trivial eigenvalue on $H^1$).** The endofunctor $\Phi_\zeta$ acts on $H^1(\mathcal{MM}) = \mathcal{M}(\mathcal{R}_\eta)/\mathcal{N}$ by:

$$\Phi_\zeta[\nu] = [\nu_{\mathrm{off}}[\mathcal{P}[\nu]]]$$

where $\nu_{\mathrm{off}}[\mathcal{P}[\nu]]$ is the off-critical measure induced by $\mathcal{P}[\nu]$.

The fixed points of $\Phi_\zeta$ are $[\nu] = 0$ (trivial) and $[\nu] = [\mu_{\mathrm{off}}]$ (the measure of off-critical zeros). The "eigenvalue" of $\Phi_\zeta$ at $[\mu_{\mathrm{off}}]$ is $\lambda = 1$ (fixed point).

**Problem:** In the Weil case, the eigenvalues $\alpha_i \neq 1$ in general — their nontrivial structure is what the Weil pairing can compare. In $\mathcal{MM}$, the only relevant "eigenvalue" is $\lambda = 1$, and the Weil pairing would give $|\lambda|^2 = 1$ trivially — with no information.

**Root of the problem:** The Frobenius over $\mathbb{F}_q$ has a nontrivial "dimension" because the curve $C$ has genus $g \geq 1$ with an $H^1$ space of dimension $2g$. In $\mathcal{MM}$, the "space $H^1$" has effective dimension 0 or $\infty$ — 0 if RH, infinite if ¬RH — and there is no nontrivial finite-dimensional intermediate structure that the Weil argument can exploit.

---

## 5. The failure of (W3): the functional equation does not give the correct dual relation

In the Weil case:
- $Z(C, q^{-s})$ satisfies the functional equation $Z(C, 1-s) = q^{(1-2g)(1/2-s)} Z(C, s)$.
- If $q^{-\alpha}$ is a zero of $Z$ (i.e. $\alpha$ is an eigenvalue of the Frobenius), then $q^{\alpha-1}$ is one too.
- In terms of eigenvalues: $\alpha_i \leftrightarrow q/\alpha_i$ — the eigenvalue duality.

In the case of $\zeta$:
- $\zeta(s)$ satisfies $\xi(s) = \xi(1-s)$, which gives: if $\rho = 1/2+i\gamma$ is a zero, so is $1-\rho = 1/2-i\gamma$ (the conjugate). Under RH, all zeros are self-dual under this symmetry.
- The relation $\rho \leftrightarrow 1-\rho$ in terms of eigenvalues of the "Frobenius" would give: if $\alpha$ is an eigenvalue, so is $1/\alpha$.
- This forces $|\alpha|^2 = 1$ — exactly RH... but ONLY if the notion of "eigenvalue" were well defined.

**Proposition 5.1 (The functional equation gives the correct relation but in a vacuum).** The functional equation of $\zeta$ formally gives the relation $\alpha \leftrightarrow 1/\alpha$ for the "eigenvalues" of $\Phi_\zeta$. Combined with the Poincaré pairing, this would force $|\alpha| = 1$. But $\alpha = 1$ trivially satisfies $|\alpha| = 1$, and there are no other nontrivial eigenvalues in $H^1(\mathcal{MM})$. The argument is vacuous.

---

## 6. The failure of (W4): the relation between the pairing and the Frobenius

**Proposition 6.1 (The pairing $\langle\cdot,\cdot\rangle_\Pi$ does not satisfy the Weil relation).** In the geometric case, the Weil relation is:

$$\langle \mathrm{Fr}_q^* \alpha, \beta\rangle_{\mathrm{Weil}} = q\cdot\langle \alpha, (\mathrm{Fr}_q^*)^{-1}\beta\rangle_{\mathrm{Weil}}$$

which introduces the factor $q$ (the "norm of the Frobenius"). This is what forces $\alpha_i \cdot \bar\alpha_i = q$.

In $\mathcal{MM}$: for the pairing $\langle f, [\nu]\rangle_\Pi = \int f\,d\nu$, the analogous relation would be:

$$\langle \Phi_\zeta^* f, [\nu]\rangle_\Pi = \lambda_{\Phi}\cdot\langle f, (\Phi_\zeta^*)^{-1}[\nu]\rangle_\Pi$$

for some scalar $\lambda_\Phi$ (the "norm of the arithmetic Frobenius").

The natural candidate for $\lambda_\Phi$: by analogy with $q$ over $\mathbb{F}_q$, the role of $q$ in the number case would be played by some invariant of $\zeta$ — perhaps $e^{1}$ (related to $\log q = 1$ in the $q\to 1$ limit), or simply $\lambda_\Phi = 1$.

If $\lambda_\Phi = 1$: the Weil relation says $\langle \Phi_\zeta^* f, [\nu]\rangle_\Pi = \langle f, (\Phi_\zeta^*)^{-1}[\nu]\rangle_\Pi$, which is simply the symmetry of the pairing. It gives $|\alpha|^2 = \lambda_\Phi = 1$ — trivially true for $\alpha = 1$.

**Corollary 6.2.** Without a scalar $\lambda_\Phi \neq 1$ (analogous to $q \neq 1$ over $\mathbb{F}_q$), the Weil relation is trivial and gives no information about the location of the zeros.

---

## 7. The central diagnosis: the structural difference between $\mathbb{F}_q$ and $\mathbb{Q}$

**Proposition 7.1 (The fundamental difference).** In the Weil case over $\mathbb{F}_q$:
- The Frobenius $\mathrm{Fr}_q$ has "degree" $q$ — it is a degree-$q$ endomorphism of the curve, with $q > 1$.
- This degree $q$ appears in the Weil relation and forces $|\alpha_i|^2 = q$.
- RH says $|\alpha_i| = \sqrt{q}$ — the eigenvalues lie on the circle of radius $\sqrt{q}$.

In the arithmetic case over $\mathbb{Q}$:
- The "Frobenius" $\Phi_\zeta$ is the endofunctor of the category $\mathcal{MM}$ — but its "degree" is 1.
- There is no analogue of the parameter $q$ appearing in the Weil relation.
- RH says the zeros lie on $\mathrm{Re}(s) = 1/2$ — the analogue is "radius 1" ($|e^{i\gamma}| = 1$), but this is automatic for any number on the unit circle.

**In summary:** The Weil proof uses the fact that the Frobenius has degree $q \neq 1$ to create a tension between the functional equation and positivity, which resolves exactly to $|\alpha_i| = \sqrt{q}$. Over $\mathbb{Q}$, there is no parameter $q > 1$ — the analogue is $q = 1$ and everything collapses.

---

## 8. Result of Doc 56: what is proved and what is not

**Theorem 8.1 (Poincaré duality on $\mathcal{MM}$: construction and non-degeneracy).** The pairing $\langle\cdot,\cdot\rangle_\Pi: H^0 \times H^1 \to \mathbb{R}$ defined in Definition 1.1 exists, is bilinear, symmetric, and non-degenerate (Theorem 2.1). The category $\mathcal{MM}$ admits a formal Poincaré duality.

**But the Deligne/Weil argument does not transfer.** The three key ingredients fail:
- **(W2)** There are no nontrivial eigenvalues of the Frobenius on $H^1(\mathcal{MM})$ — the only eigenvalue is $\lambda = 1$.
- **(W3)** The functional equation of $\zeta$ gives $\alpha \leftrightarrow 1/\alpha$, which forces $|\alpha| = 1$ — but $\alpha = 1$ already satisfies this trivially.
- **(W4)** The Weil relation with factor $\lambda_\Phi = 1$ is trivial, with no tension to resolve.

**Corollary 8.2 (Final diagnosis of the Langlands-Weil strategy).** Poincaré duality on $\mathcal{MM}$ exists but is trivial for the purpose of proving RH. The Weil argument requires a parameter $q \neq 1$ that does not exist in the arithmetic case over $\mathbb{Q}$.

---

*Phase 30 concludes with the negative result of Doc 56. Next: a global review of the entire program to identify which genuinely new paths remain open.*
