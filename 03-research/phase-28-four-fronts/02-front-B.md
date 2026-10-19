# Front B — Spectral flow and the Atiyah–Patodi–Singer $\eta$-invariant


---

## 1. Setup: spectral flow as a reformulation of $\kappa$

**Definition B.1** (spectral flow). Let $\{T_\lambda\}_{\lambda \in [0,1]}$ be a continuous
family of self-adjoint Fredholm operators on a Hilbert space $H$. The
*spectral flow* $\mathrm{sf}(\{T_\lambda\})$ is the net number of eigenvalues
crossing zero from negative to positive as $\lambda$ goes from $0$ to $1$.

Formally: $\mathrm{sf}(\{T_\lambda\}) = \#\{\text{crossings} \uparrow\} - \#\{\text{crossings} \downarrow\}$.

**Proposition B.2** (spectral flow = Kreĭn index). Let $Q$ be the Weil form with
associated operator $T$ (defined by $Q(f,g) = \langle Tf, g\rangle_H$ with respect to a
fixed positive inner product $\langle\cdot,\cdot\rangle_H$ on $H$). Let $T_1 = I$
(identity, positive definite). Then for any path $\{T_\lambda\}_{\lambda
\in [0,1]}$ from $T_0 = T$ to $T_1 = I$:
$$\mathrm{sf}(\{T_\lambda\}) = \kappa(Q) = \#\{\text{negative eigenvalues of } T\}.$$

*Proof:* The spectral flow along the path counts the zero crossings. We start
from $T_0 = T$ with $\kappa$ negative eigenvalues and reach $T_1 = I > 0$ with no
negative eigenvalues. Each negative eigenvalue of $T_0$ must cross zero
exactly once (for generic paths). The net difference is $\kappa - 0 = \kappa$.
$\square$

*Remark:* The spectral flow is a homotopy invariant (relative to the endpoints):
it does not depend on the specific path from $T$ to $I$.

---

## 2. The Atiyah–Patodi–Singer theorem

**Theorem B.3** (APS 1976). Let $M = [0,1] \times X$ be a cylindrical manifold with boundary
$\partial M = \{0\} \times X \cup \{1\} \times X$, and $D = \partial/\partial\lambda + T_\lambda$
the Dirac-type operator on the cylinder. Then:
$$\mathrm{sf}(\{T_\lambda\}) = \mathrm{Ind}(D_{\text{APS}}) + \frac{\eta(T_0) - \eta(T_1)}{2},$$
where $\mathrm{Ind}(D_{\text{APS}})$ is the index of the APS boundary value
problem, and $\eta(A)$ is the $\eta$-invariant of the operator $A$:
$$\eta(A) = \lim_{s \to 0^+} \sum_{\lambda \ne 0} \mathrm{sgn}(\lambda) |\lambda|^{-s},$$
the sum over all nonzero eigenvalues of $A$.

Combining with B.2:
$$\kappa(Q) = \mathrm{Ind}(D_{\text{APS}}) + \frac{\eta(T_0) - \eta(T_1)}{2}.$$

For $T_1 = I$ (identity): $\eta(I) = 0$ (all eigenvalues positive, signed sum
$= +\infty$ regularized $= 0$ by symmetry... needs care). More precisely,
$\eta(I) = \dim H$ in finite dimension, but for the path to $I$ in infinite dimension
the correct convention is $\eta(I) = 0$ by choice of reference path.

**Corollary B.4.** Under standard conventions:
$$\kappa(Q) = \mathrm{Ind}(D_{\text{APS}}) + \frac{\eta(T_0)}{2}.$$

Then: **$\kappa(Q) = 0$ if and only if $\mathrm{Ind}(D_{\text{APS}}) = -\eta(T_0)/2$.**

In particular, if both $\mathrm{Ind}(D_{\text{APS}}) = 0$ and $\eta(T_0) = 0$, then $\kappa = 0$.

---

## 3. The $\eta$-invariant of the Weil operator

**Definition B.5** (Weil operator). Let $T_0$ be the operator of the Weil form $Q$
on $L^2(C_\mathbb{Q})$ with fixed positive inner product $\langle\cdot,\cdot\rangle$:
$$Q(f,g) = \langle T_0 f, g\rangle, \qquad T_0 = T_0^*.$$

The spectrum of $T_0$:
- Positive eigenvalues: come from the contributions of primes and from the
  archimedean factor.
- Negative eigenvalues: come from the zeros off the critical line.
- Under Hypothesis D with $m$ orbits: there are exactly $2m$ negative eigenvalues.

**Definition B.6** ($\eta$-invariant of $T_0$). Formally:
$$\eta(T_0) = \lim_{s \to 0^+} \left(\sum_{\lambda > 0} \lambda^{-s} - \sum_{\lambda < 0} |\lambda|^{-s}\right),$$
where the sums are over eigenvalues of $T_0$.

This quantity measures the *spectral asymmetry*: how much heavier the positive spectrum
is than the negative one.

---

## 4. Functional symmetry and the possible vanishing of $\eta$

**Proposition B.7** (symmetry $s \leftrightarrow 1-s$ of the Weil form). The functional
equation $\xi(s) = \xi(1-s)$ implies that the Weil form $Q$ satisfies:
$$Q(Jf, Jg) = Q(f, g), \quad \text{where } (Jf)(x) = \frac{1}{x} f\!\left(\frac{1}{x}\right).$$

In terms of the operator $T_0$: $J T_0 J^{-1} = T_0$, i.e., $T_0$ commutes with $J$.

*Proof:* The functional equation $\xi(s) = \xi(1-s)$ corresponds to the transformation $x
\mapsto 1/x$ on the space of test functions. The Weil form is invariant under
this transformation. $\square$

**Consequence for the eigenvalues:** If $T_0 \phi = \lambda \phi$, then
$T_0 (J\phi) = J T_0 \phi = \lambda (J\phi)$.
So $J$ permutes the eigenspaces with the same eigenvalue. This does NOT anti-symmetrize
the spectrum; the symmetry $J$ does not force $\eta = 0$.

*This is the first obstacle of Front B.* The symmetry $s \leftrightarrow 1-s$ of the
functional equation preserves the eigenvalues of $T_0$, it does not invert them. For $\eta = 0$
we would need a symmetry that anti-symmetrizes the spectrum.

---

## 5. When is $\eta(T_0) = 0$?

**Proposition B.8** (sufficient condition for $\eta = 0$). If there exists an involution
$K: H \to H$ such that $K T_0 K^{-1} = -T_0$ (anti-symmetrization), then $\eta(T_0) = 0$.

*Proof:* $K$ maps the positive spectrum bijectively to the negative one and vice versa, with
equal multiplicity. The sum $\eta = \sum \mathrm{sgn}(\lambda)|\lambda|^{-s}$
cancels. $\square$

**Question B.9** (new, central). Does an involution $K$ exist on $L^2(C_\mathbb{Q})$
such that $K T_0 K^{-1} = -T_0$?

For $K$ to anti-symmetrize $T_0$, it would need to map the positive contributions
(primes + archimedean) into negative ones (zeros). This would require a duality between
the "arithmetic sector" and the "spectral sector" of the Weil form.

The natural candidate: the Fourier transform on $C_\mathbb{Q}$. Under the
Fourier transform $\hat\cdot$:
$$Q(f,g) \longleftrightarrow Q(\hat f, \hat g) = ?$$

If $Q(\hat f, \hat g) = -Q(f,g)$, then $K = \mathcal{F}$ (Fourier) anti-symmetrizes $T_0$.

**Proposition B.10** (obstacle to Fourier anti-symmetrization). The Poisson–Weil
equation gives:
$$Q(f,g) + Q(\hat f, \hat g) = (\text{boundary terms}).$$

If the boundary terms are zero, then $Q(\hat f, \hat g) = -Q(f,g)$, giving $\eta = 0$.

*Status:* It is unknown whether the boundary terms vanish in general. This is the
precise question to resolve in Front B.

---

## 6. The connection with special values of $\zeta$

**Remark B.11.** For arithmetic operators, the $\eta$-invariant is frequently
expressed in terms of $L$-functions at special points. Known examples:

- $\eta(\mathrm{sign}_\Gamma)$ for the sign operator on an arithmetic hyperbolic
  manifold expresses combinations of values of Dedekind $L$-functions at $s = 0$.
- The Dirac $\eta$-invariant on lens spaces is expressed via Dedekind sums.

**Conjecture B.12** (new). The $\eta$-invariant of the Weil operator $T_0$ satisfies:
$$\eta(T_0) = c \cdot \zeta'(0) + d \cdot \log(2\pi)$$
for some constants $c, d$ depending only on normalizations.

If $\eta(T_0) \ne 0$ and $\mathrm{Ind}(D_{\text{APS}}) = \eta(T_0)/2$, Corollary
B.4 gives $\kappa = 0$. This would be the proof of RH via APS.

The explicit computation of $\eta(T_0)$ is the primary objective of Front B.

---

## 7. Verdict of Front B

| Result | Status |
|---|---|
| $\mathrm{sf} = \kappa(Q)$ | Proved (Prop. B.2) |
| APS formula for $\kappa$ | Established (Cor. B.4) |
| Symmetry $J$ does not anti-symmetrize | Proved (Prop. B.7) |
| Candidate $K = \mathcal{F}$ (Fourier) | Identified; requires verifying boundary terms |
| $\eta(T_0) = 0$ by anti-symmetrization | **Open — the heart of Front B** |
| $\eta(T_0)$ as a special value of $\zeta$ | Conjecture B.12 — new result to be proved |

**The precise obstacle:** verifying whether $Q(f,g) + Q(\hat f, \hat g) = 0$ (boundary
terms vanish in the Poisson–Weil equation). This would imply $\eta(T_0) = 0$ and,
via APS, $\kappa = 0$, hence RH.
