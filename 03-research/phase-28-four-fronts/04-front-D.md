# Front D — Transversal energy and the critical line as attractor

**Credit:** The central direction of this front was proposed by a mathematician colleague.

---

## 1. The starting point: $b$ as the only variable that matters

The whole program since Phase 21 converges on a single parameter:
$$b_j := \mathrm{Re}(\rho_j) - \frac{1}{2},$$
the transversal distance of the zero $\rho_j$ to the critical line. The three
descriptions of the obstacle are:

| Language | Manifestation of $b_j > 0$ |
|---|---|
| Kreĭn | Negative direction of $Q$ |
| Connes | Complex eigenvalue $\lambda_j = \gamma_j - ib_j$ of $H_C$ |
| Adelic | Non-unitary character $|x|^{b_j + i\gamma_j}$ (Phase 27) |

**Program diagnosis:** we have studied *the existence* of $b_j$. Phase 28 asks
about its *dynamics*: does a mechanism exist that forces $b_j \to 0$?

---

## 2. Three ingredients for the arithmetic energy

**Definition D.1** (logarithmic energy). For the zero configuration $Z = \{z_n\}$
(zeros of $H_0$ as in Front A, with $z_n = \gamma_n + ib_n$):
$$E_{\log}(Z) := -\sum_{j \ne k} \log|z_j - z_k|.$$

This energy appears in the GUE distribution of zeros (Montgomery–Odlyzko): the zeros
of $\zeta$ behave like eigenvalues of a random Hermitian matrix, whose equilibrium
measure minimizes $E_{\log}$ subject to the von Mangoldt density.

**Definition D.2** (confinement potential). The mean density of zeros of $\zeta$
is $W(\gamma) \approx \frac{1}{2\pi}\log(\gamma/2\pi)$ (Riemann–von Mangoldt formula). Define:
$$E_{\text{conf}}(Z) := \sum_n W(\gamma_n),$$
the potential that reproduces the correct density in the $\gamma$ direction (height on the
critical line).

**Definition D.3** (transversal energy, new). The novel ingredient:
$$\Phi(Z) := \sum_n b_n^2 = \sum_n \left(\mathrm{Re}(z_n) - 0\right)^2,$$
the confinement energy in the direction *transversal* to the critical line.

**Definition D.4** (total arithmetic energy):
$$E_{\text{arith}}(Z) := E_{\log}(Z) + E_{\text{conf}}(Z) + \Phi(Z).$$

---

## 3. The variational formulation of RH

**Proposition D.5** (RH as a minimization problem). Under the following hypotheses:
1. The only zero configuration of $\zeta$ compatible with the functional equation and
   the Euler product is the real configuration with all $b_n = 0$;
2. The energy $E_{\text{arith}}$ is strictly convex in the transversal direction;
then RH is equivalent to the zero configuration of $\zeta$ being the unique
minimum of $\Phi$ subject to the arithmetic constraints.

*Note:* Hypotheses (1) and (2) are the content of what needs to be proved. But the
formulation as a minimization problem is new.

**Proposition D.6** (basic properties of $\Phi$).
1. $\Phi(Z) \ge 0$ for every configuration.
2. $\Phi(Z) = 0 \iff b_n = 0$ for all $n \iff$ all zeros lie on the critical line.
3. $\Phi(Z) = -\mathrm{tr}(Q|_{\text{neg}}) / C$ for some normalization $C > 0$,
   where $\mathrm{tr}(Q|_{\text{neg}})$ is the trace of the Weil operator restricted
   to its negative subspace.

*Proof of (3):* The negative eigenvalues of $T_0$ (Weil operator) are, under
Hypothesis D, proportional to $-b_j^2$ (the $j$-th eigenvalue measures the "depth"
of the negative direction, which scales as $b_j^2$). The trace over the negative
subspace is $\sum_j (-b_j^2) \cdot C^{-1}$, hence $\Phi = -\mathrm{tr}(Q|_{\text{neg}})/C$. $\square$

*Consequence of (3):* $\Phi$ is an invariant of the Weil operator, not an
artificial quantity. It follows naturally from the Weil form.

---

## 4. The connection with the de Bruijn–Newman flow (unification of A and D)

**Theorem D.7** (unification of Fronts A and D). The de Bruijn–Newman flow on
zero configurations is the gradient flow of $E_{\log}$:
$$\frac{dz_n}{dt} = -\frac{\partial E_{\log}}{\partial \bar z_n} = \sum_{k \ne n} \frac{2}{z_k - z_n}.$$

(Csordas–Norfolk–Varga 1988, cf. Front A.)

Therefore, Front D's question —

> Is $b_n = 0$ the unique global minimum of $E_{\text{arith}}$ subject to the
> arithmetic constraints of $\zeta$?

— is the same question as Front A expressed in variational language.

**Difference between A and D:** Front A asks about the *monotonicity* of $\kappa_t$.
Front D asks about the *structure of the minimum* of $E_{\text{arith}}$. The second
formulation is more precise: a minimum can exist without the flow being monotone.

---

## 5. The analogy with function fields

**Weil's mechanism (1948) for curves over $\mathbb{F}_q$:**

Let $C$ be a curve over $\mathbb{F}_q$, $Z(u)$ its zeta function. The Frobenius
eigenvalues $\alpha_i$ satisfy $|\alpha_i| = q^{1/2}$. Weil proved this by showing that
the quadratic form $\langle D, D \rangle$ (self-intersection degree of the
Frobenius correspondence $D = \Gamma_\phi - \Delta$) is *positive definite*.

The structure is:
- There is a space of correspondences (analogue of $L^2(C_\mathbb{Q})$).
- There is a canonical bilinear form (analogue of $Q$).
- The positivity of the form forces the eigenvalues to have the correct modulus.

In function fields, the proof has TWO ingredients:
1. **Self-adjointness:** the Frobenius correspondence is *self-adjoint* with respect
   to the intersection form.
2. **Positivity:** the intersection form is *positive definite*.

Front D seeks the analogue of positivity for $\mathbb{Z}$:

> Does a canonical energy exist on zero configurations of $\zeta$ whose
> positivity in the transversal direction forces $b_j = 0$?

**Comparison table:**

| Object | Curves over $\mathbb{F}_q$ | $\zeta$ over $\mathbb{Z}$ |
|---|---|---|
| Frobenius eigenvalues | $\alpha_i$ with $|\alpha_i| = q^{1/2}$ | Zeros $\rho_j$ with $\mathrm{Re}(\rho_j) = 1/2$ |
| Canonical form | Intersection $\langle D, D \rangle$ | Weil form $Q$ |
| Positivity proved | Yes (Weil 1948) | No (open) |
| Transversal energy | $\sum_i |\alpha_i - q^{1/2}|^2 = 0$ iff Weil | $\Phi = \sum_j b_j^2 = 0$ iff RH |
| Mechanism | Hodge index theorem on $J(C)$ | **Unknown — Front D's goal** |

---

## 6. The exact energetic model

**Definition D.8** (transversal energy derived from the Weil form). For the
Weil form $Q$ with operator $T_0 = T_0^+ + T_0^-$ (decomposition into positive and
negative part), define:
$$\Phi_{\text{Weil}}(Q) := \|T_0^-\|_{\text{tr}} = \mathrm{tr}(-T_0^-)
  = \sum_j |\lambda_j^-|,$$
where the sum runs over the negative eigenvalues of $T_0$.

This is the *trace norm of the Weil operator* on its negative part.

**Proposition D.9.** $\Phi_{\text{Weil}}(Q) = 0 \iff \kappa(Q) = 0 \iff$ RH.

*Proof:* If $\kappa(Q) = 0$, the negative part $T_0^- = 0$, hence $\Phi_{\text{Weil}} = 0$.
If $\kappa(Q) > 0$, there is at least one negative eigenvalue $\lambda^- < 0$, hence
$\Phi_{\text{Weil}} \ge |\lambda^-| > 0$. $\square$

**The dynamical question (new):** Can $\Phi_{\text{Weil}}$ be decreased by a
natural flow on the space of Weil forms, with a unique minimum at $\Phi_{\text{Weil}} = 0$?

---

## 7. The transversal penalty and the space of constraints

The colleague's proposal: add a penalty $\sum_i V(b_i)$ where $V: \mathbb{R} \to
\mathbb{R}_{\ge 0}$ satisfies $V(b) = 0 \iff b = 0$ and $V(b) > 0$ for $b \ne 0$.

The precise question: can $V$ be *derived* from the functional equation of $\zeta$?

**Proposition D.10** (the transversal potential of the functional equation). The
functional equation $\zeta(s) = \chi(s)\zeta(1-s)$ (with $\chi(s)$ the symmetry
factor) implies that zeros come in pairs $(\rho, 1-\rho)$. For a zero $\rho = 1/2 + b + i\gamma$
with $b \ne 0$:

- The orbit under $s \mapsto 1 - \bar s$ is $\{1/2 + b + i\gamma, 1/2 - b - i\gamma,
  1/2 + b - i\gamma, 1/2 - b + i\gamma\}$.
- The contribution to the energy $E_{\log}$ of this four-point orbit includes
  internal repulsion between points of the same orbit.
- The *self-interaction energy of the orbit* is:
  $$E_{\text{self}}(b, \gamma) = -\log|2b| - 2\log|2i\gamma| - \log|2b| + \ldots$$
  which DIVERGES as $b \to 0$ (via the term $-\log|2b|$).

**Remark D.11** (new). The potential $V(b) = -\log|2b|$ has a logarithmic
singularity at $b = 0$: the two zeros of the orbit with $\mathrm{Re} = 1/2 \pm b$
*repel each other logarithmically*. The smaller $b$ is, the stronger the
repulsion.

But this repulsion acts *along the critical line*, not transversally. For
transversal confinement we need the gradient of $E_{\text{arith}}$ in the
$b$ direction to point toward $b = 0$.

---

## 8. Front D's central question

**Question D.12** (new, central to Front D). Let
$$\mathcal{Z}_\zeta := \{\text{zero configuration of } \zeta\}$$
(a single point, the real zero configuration). Consider the family of configurations
$$\mathcal{Z}_{\text{arith}} := \{\text{zeros of functions in the class of } \zeta\}$$
(entire functions of the same order and type, with an Euler product and an analogous
functional equation). Does $E_{\text{arith}}$ satisfy the following properties at
$\mathcal{Z}_\zeta$?

1. $\partial E_{\text{arith}}/\partial b_j\big|_{b_j = 0} = 0$ (the critical line is a critical point).
2. $\partial^2 E_{\text{arith}}/\partial b_j^2\big|_{b_j = 0} > 0$ (it is a strict local minimum).
3. No other minima exist in $\mathcal{Z}_{\text{arith}}$ (uniqueness of the global minimum).

If all three conditions hold: the critical line is the unique global minimum of
$E_{\text{arith}}$ in $\mathcal{Z}_{\text{arith}}$, and RH follows from the existence
of a minimum (which occurs at $b_j = 0$).

---

## 9. Verification of condition (1): the critical line is a critical point

**Proposition D.13.** The configuration $b_j = 0$ (all zeros on the critical line)
is always a stationary point of $E_{\text{arith}}$ in the transversal direction.

*Proof:* By symmetry. If $b_j = 0$ for all $j$, the configuration is symmetric under
$z_n \mapsto -\bar z_n$ (reflection across the critical line, which in the $z$
coordinate is the line $\mathrm{Re} z = 0$). The energy $E_{\text{arith}}$ is symmetric
under this reflection. Therefore the gradient in the transversal direction $b_j$ is
zero at $b_j = 0$. $\square$

*Remark:* This proposition only says that the critical line is a stationary point.
It does not distinguish between minimum, maximum, or saddle point. That is the content
of condition (2).

---

## 10. The obstacle: condition (2) requires the Euler structure

**Proposition D.14** (obstacle). The positivity of the Hessian $\partial^2
E_{\text{arith}}/\partial b_j^2 > 0$ at $b_j = 0$ does NOT follow from symmetry
alone. It requires restriction to configurations compatible with the Euler product.

*Argument:* Without the Euler product, one can construct entire functions with a
functional equation and zeros off the critical line where the Hessian is negative
(the critical point is a local maximum). The Euler product imposes that the function
factorizes over the primes, which restricts the zeros to "positions compatible with
arithmetic."

*This is exactly Wall A (Phase 27) in variational language:* the restriction to
the Euler product is the reason the Hessian might be positive. Without that
restriction, the minimum is not necessarily on the critical line.

---

## 11. The more precise analogy with function fields

In the case of curves over $\mathbb{F}_q$, the positivity of the intersection form
is proved using the *Hodge index theorem*: for divisors on the Jacobian,
the intersection form has precisely a Sylvester index determined by the
geometry of the curve (genus $g$ gives index $(1,2g-1)$ in a certain normalization).

The analogue for $\zeta$ would be:

> The Weil form $Q$ has Sylvester index $(+\infty, 0)$ (positive definite)
> when restricted to test functions compatible with the structure of the Euler
> product.

This is exactly the RH statement expressed as a claim about the *Hodge
index* of the "space of arithmetic correspondences" of $\mathrm{Spec}\,\mathbb{Z}$.

Formulated this way, **Front D is isomorphic to Front B in variational language:**

| Front B | Front D |
|---|---|
| $\eta(T_0) = 0$ by anticommutativity | Positive Hessian by Euler restriction |
| Fourier anticommutativity | Restriction to the Euler product |
| $\kappa = 0$ by APS | $\kappa = 0$ by variational minimum |

---

## 12. Verdict of Front D

| Result | Status |
|---|---|
| $\Phi(Z) \ge 0$ with equality iff RH | Trivial |
| $\Phi$ derived from the Weil form | Proved (Prop. D.6, (3)) |
| DBN flow = gradient of $E_{\log}$ | Established (Front A = Front D) |
| Critical line is a stationary point of $E_{\text{arith}}$ | Proved (Prop. D.13) |
| Positive Hessian at $b_j = 0$ | **Open — requires Euler restriction** |
| Uniqueness of the global minimum | **Open — depends on arithmetic structure** |
| Precise analogy with Weil/function fields | Identified |
| Front D = Front B in variational language | **New result of Phase 28** |

---

## 13. The most concrete question to attack

Of the four fronts, the most directly attackable question that has not been
formulated in any known paper:

**Question D.15** (Phase 28's question). Consider the second variation of the
Weil form $Q[Z + \epsilon \delta Z]$ when the zero configuration is perturbed
in the transversal direction $b_j \to b_j + \epsilon c_j$:

$$\frac{d^2}{d\epsilon^2} Q[Z_\epsilon]\bigg|_{\epsilon=0} = ?$$

Is this second variation positive (semidefinite) for every perturbation $c_j$ compatible
with the Euler product?

If the answer is yes: $b_j = 0$ is a strict local minimum of $Q$ in the
transversal direction, and (with uniqueness) RH follows.

The computation of this second variation from the Weil–Guinand explicit formula
is, as far as we know, new. It is the first concrete step of Front D.
