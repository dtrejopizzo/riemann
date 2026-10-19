# Document 81 — Positivity of $L(z)$ on the unit circle and the reformulation via the disk

**Program:** Riemann Hypothesis — Phase 33 DBN-CCM (Path 2)
**Prerequisites:** Docs 75, 78, 79

---

## Summary

This document rigorously develops Path 2 of the program: the function $L(z) = \log\xi(z/(z-1))$ and the positivity condition on the unit circle $|z| = 1$. §1 establishes the exact geometry of the Möbius transformation $\tau(z) = z/(z-1)$ and unambiguously identifies which regions of the $s$-plane correspond to the interior, boundary, and exterior of the unit disk. §2 studies the function $F(z) = \xi(z/(z-1))$ and shows that RH is equivalent to the absence of zeros of $F$ in the interior of the disk (Proposition 2.1). §3 analyzes the positivity condition $\mathrm{Re}[L(e^{i\theta})] \geq 0$ and shows that it is necessarily false at the zeros of $\xi$ on the critical line; the boundary-positivity approach cannot work directly. §4 formulates the correct Nevanlinna-Herglotz condition in the interior of the disk, and establishes its equivalence with RH via the Carathéodory function (Proposition 4.2). §5 develops the connection with orthogonal polynomials on the unit circle (OPUC) and the Schur coefficients, pointing out precisely which part of the OPUC formalism is automatic and which part requires new input. §6 examines whether any property of $\xi$ independent of the position of its zeros can force non-vanishing in the disk. The frank conclusion is that the reformulation via the disk is exact and elegant, but the proof of the non-vanishing condition is equivalent to RH and is not obtained for free.

---

## §1. Geometry of the transformation $\tau(z) = z/(z-1)$

### 1.1. Basic description

Let $\tau : \hat{\mathbb{C}} \to \hat{\mathbb{C}}$ be the Möbius transformation defined by
$$\tau(z) = \frac{z}{z-1}.$$
Its values at special points: $\tau(0) = 0$, $\tau(1/2) = -1$, $\tau(\infty) = 1$, $\tau(2) = 2$, and $\tau(1) = \infty$ (simple pole). The inverse is $\tau^{-1}(s) = s/(s-1)$, i.e., $\tau$ is an involution: $\tau \circ \tau = \mathrm{id}$.

### 1.2. Image of the unit disk

**Proposition 1.1.** *The transformation $\tau$ establishes an analytic bijection between:*
- *$\{|z| < 1\} \longleftrightarrow \{\mathrm{Re}(s) < 1/2\}$,*
- *$\{|z| = 1,\, z \neq 1\} \longleftrightarrow \{\mathrm{Re}(s) = 1/2\}$,*
- *$\{|z| > 1\} \longleftrightarrow \{\mathrm{Re}(s) > 1/2\}$.*

*Proof.* Let $s = \tau(z)$. Then $z = \tau(s) = s/(s-1)$, and hence $|z| < 1 \iff |s/(s-1)| < 1 \iff |s| < |s-1|$. Writing $s = \sigma + it$, the condition $|s| < |s-1|$ is $\sigma^2 + t^2 < (\sigma-1)^2 + t^2$, i.e., $\sigma^2 < \sigma^2 - 2\sigma + 1$, i.e., $2\sigma < 1$, i.e., $\sigma < 1/2$. The other two statements follow analogously. $\square$

**Corollary 1.2.** *If $\rho = \sigma + i\gamma$ is a nontrivial zero of $\xi$, then $z_\rho = \tau(\rho) = \rho/(\rho-1)$ satisfies:*
- *$|z_\rho| < 1$ if and only if $\sigma < 1/2$,*
- *$|z_\rho| = 1$ if and only if $\sigma = 1/2$ (i.e., $\rho$ lies on the critical line),*
- *$|z_\rho| > 1$ if and only if $\sigma > 1/2$.*

### 1.3. Parametrization of the critical line

For $s = 1/2 + it$ with $t \in \mathbb{R}$, the corresponding point on the unit circle is
$$z(t) = \tau(1/2+it) = \frac{1/2+it}{it-1/2} = -\frac{1/2+it}{1/2-it} = -e^{2i\arctan(2t)}.$$
As $t$ ranges over $\mathbb{R}$, $\arctan(2t)$ ranges over $(-\pi/2, \pi/2)$, so $2\arctan(2t)$ ranges over $(-\pi, \pi)$. Hence $z(t)$ traces the arc $\{e^{i\theta} : \theta \in (0, 2\pi)\} = \{|z|=1\} \setminus \{1\}$ (i.e., the unit circle minus the point $z = 1$, which would correspond to $t \to \pm\infty$, i.e., $s \to 1/2 \pm i\infty$).

### 1.4. Symmetry of $\tau$ under the functional equation

The functional equation $\xi(s) = \xi(1-s)$ in disk coordinates: if $s = \tau(z)$, then $1 - s = 1 - z/(z-1) = -1/(z-1)$, so $\xi(\tau(z)) = \xi(-1/(z-1))$. The function $F(z) = \xi(z/(z-1))$ thus satisfies
$$F(z) = \xi\!\left(\frac{-1}{z-1}\right).$$
In particular, if $z_0$ is a zero of $F$, so is $z_1 = 1 - 1/\tau(z_0) = \ldots$; the symmetry of the zeros of $\xi$ is reflected in a symmetry of the zeros of $F$ with respect to the unit circle.

---

## §2. The function $F(z) = \xi(z/(z-1))$ and the equivalence with RH

### 2.1. Analyticity of $F$

The function $\xi$ is entire of order 1, and the transformation $\tau(z) = z/(z-1)$ is analytic on $\mathbb{C} \setminus \{1\}$. In the closed unit disk $\{|z| \leq 1\}$, the point $z = 1$ lies on the boundary (accessible only as a limit from the interior), and $\tau(z) \to \infty$ as $z \to 1$. Since $\xi(s) \to \infty$ as $s \to \infty$ (indeed $|\xi(s)| \to \infty$ because of the $\Gamma$ factor), the function $F(z)$ has no finite limit as $z \to 1$ from the interior of the disk.

Consequently, $F$ is analytic in the open disk $\{|z| < 1\}$ (since $\xi$ is entire and $\tau$ is analytic on $|z| < 1$, where $\tau(z)$ takes values in $\mathrm{Re}(s) < 1/2$, a region free of singularities of $\xi$). The function $F$ does not extend continuously to the boundary point $z = 1$, but it does extend to every other point of $|z| = 1$.

### 2.2. The zeros of $F$ in relation to RH

The zeros of $F$ in the open disk $\{|z| < 1\}$ correspond exactly to the zeros of $\xi$ in $\{\mathrm{Re}(s) < 1/2\}$. By the functional equation $\xi(s) = \xi(1-s)$, if $\rho$ is a zero of $\xi$ with $\mathrm{Re}(\rho) > 1/2$, then $1-\rho$ is a zero with $\mathrm{Re}(1-\rho) < 1/2$. Hence the zeros of $\xi$ in $\{\mathrm{Re}(s) < 1/2\}$ are in bijection with the zeros in $\{\mathrm{Re}(s) > 1/2\}$: no zero in $\{\mathrm{Re}(s) < 1/2\}$ coincides with any zero in $\{\mathrm{Re}(s) > 1/2\}$.

**Proposition 2.1.** *The following conditions are equivalent:*

*(i) Riemann Hypothesis: every nontrivial zero of $\zeta$ (equivalently, of $\xi$) has real part $1/2$.*

*(ii) The function $F(z) = \xi(z/(z-1))$ has no zeros in the open disk $\{|z| < 1\}$.*

*(iii) The function $F$ has no zeros in the region $\{|z| > 1\}$ (i.e., in $\{\mathrm{Re}(s) > 1/2\}$).*

*Note: (ii) and (iii) are equivalent by the functional equation.*

*Proof.* By Corollary 1.2, the zeros of $F$ in $|z| < 1$ correspond exactly to the zeros of $\xi$ in $\mathrm{Re}(s) < 1/2$. By the functional equation, $\xi$ has no zeros in $\mathrm{Re}(s) < 1/2$ if and only if it has none in $\mathrm{Re}(s) > 1/2$, which is equivalent to all its zeros lying on $\mathrm{Re}(s) = 1/2$, i.e., (i). $\square$

---

## §3. The boundary positivity condition and its failure

### 3.1. The condition $\mathrm{Re}[L(e^{i\theta})] \geq 0$

We define $L(z) = \log F(z)$ with an appropriate branch of the logarithm. On the unit circle, $z = e^{i\theta}$ corresponds (via $\tau$) to the point $s = \tau(e^{i\theta})$, which has $\mathrm{Re}(s) = 1/2$ (Proposition 1.1). Hence,
$$\mathrm{Re}[L(e^{i\theta})] = \log|F(e^{i\theta})| = \log|\xi(\tau(e^{i\theta}))| = \log|\xi(1/2 + it_\theta)|$$
where $t_\theta$ is the value of $t$ such that $\tau(e^{i\theta}) = 1/2 + it_\theta$.

The condition $\mathrm{Re}[L(e^{i\theta})] \geq 0$ for every $\theta$ would be equivalent to $|\xi(1/2 + it)| \geq 1$ for every $t \in \mathbb{R}$.

### 3.2. Failure of the condition at the zeros of $\xi$

The function $\xi(1/2+it)$ has infinitely many real zeros $t = \gamma_n > 0$ (the imaginary parts of the Riemann zeros on the critical line, whose existence and density are known). At each zero $\gamma_n$, $\xi(1/2+i\gamma_n) = 0$, and hence $|\xi(1/2+i\gamma_n)| = 0$, which gives
$$\mathrm{Re}[L(e^{i\theta_n})] = \log 0 = -\infty,$$
where $\theta_n = 2\pi + 2\arctan(2\gamma_n)$ (or the angle corresponding to $z_n = \tau(\rho_n)$).

**Proposition 3.1.** *The condition $\mathrm{Re}[L(e^{i\theta})] \geq 0$ for every $\theta$ is necessarily false. In particular, it is false at each $\theta_n$ corresponding to a zero of $\xi$ on the critical line (unconditionally, without assuming or denying RH).*

**Conclusion.** The approach of proving RH via the positivity of the real part of $L$ on the unit circle cannot work: this positivity is false independently of RH. The presence of zeros of $\xi$ exactly on $|z| = 1$ (which is precisely what RH predicts) guarantees that $L$ cannot be continuous on the boundary, much less non-negative.

---

## §4. The correct condition: non-vanishing in the interior of the disk

### 4.1. Reformulation via the function $L$ in the interior

The correct Nevanlinna condition is not on the boundary but on the interior of the disk:

**Proposition 4.1.** *If $F$ has no zeros in $\{|z| < 1\}$, then $L(z) = \log F(z)$ is well defined as an analytic function in $\{|z| < 1\}$, and $F(z) = e^{L(z)}$ in the disk.*

Note that it is not claimed that $\mathrm{Re}[L(z)] \geq 0$ in the interior; it is only claimed that $L$ is analytic (i.e., that $F$ has no zeros). Positivity of $\mathrm{Re}[L]$ in the interior would be the much stronger condition $|F(z)| \geq 1$ for $|z| < 1$, which is not a consequence of RH.

### 4.2. The associated Carathéodory function

Let $dm_{\xi}$ be the (positive, Borel) measure on the unit circle defined by
$$dm_{\xi}(e^{i\theta}) = |\xi(1/2 + it_\theta)|^2 \cdot \left|\frac{dt}{d\theta}\right| d\theta,$$
where $t_\theta$ is the parametrization of the critical line introduced in §1.3. The Carathéodory function of this measure is
$$C_\xi(z) = \int_{|w|=1} \frac{w+z}{w-z}\, dm_{\xi}(w), \qquad |z| < 1.$$
By Herglotz's theorem, $\mathrm{Re}[C_\xi(z)] \geq 0$ for every $|z| < 1$ unconditionally, since $dm_{\xi}$ is a positive measure.

However, the Carathéodory function $C_\xi$ does not coincide with $L(z) = \log F(z)$; they are different objects.

**Proposition 4.2.** *RH is equivalent to $F(z)$ having no zeros in $\{|z| < 1\}$. This non-vanishing condition is a "Nevanlinna class" type condition on $F$ in the disk, but it is not equivalent to any simple positivity condition on $\mathrm{Re}[L(z)]$ in the interior of the disk.*

*Proof.* The equivalence with RH is Proposition 2.1. For the second part: the condition $\mathrm{Re}[L(z)] \geq 0$ in $|z|<1$ would be equivalent to $|F(z)| \geq 1$ in the disk, which is much stronger than non-vanishing. It suffices to note that $|F(0)| = |\xi(0)| = 1/2 < 1$, which refutes $|F(z)| \geq 1$ at $z = 0$ unconditionally. $\square$

---

## §5. Connection with orthogonal polynomials on the unit circle (OPUC)

### 5.1. The Schur-Simon formalism

Orthogonal polynomials on the unit circle (OPUC) associated with a positive measure $d\mu$ on $\{|z|=1\}$ satisfy the Szegő recursion with reflection coefficients (Schur coefficients) $\alpha_k \in \mathbb{C}$. The OPUC admissibility condition is always $|\alpha_k| \leq 1$; the strict condition $|\alpha_k| < 1$ is equivalent to the measure being absolutely continuous with strictly positive density a.e.

**Remark 5.1.** For the measure $d\mu = dm_\xi$ defined in §4.2, the Schur coefficients $\alpha_k$ automatically satisfy $|\alpha_k| \leq 1$. Their being strictly less than 1 is equivalent to $|\xi(1/2+it)| > 0$ for almost every $t$, which is true unconditionally (the zeros of $\xi$ form a discrete set, of measure zero).

**Hence, the condition $|\alpha_k| < 1$ is automatic and does not imply RH.**

### 5.2. The correct distinction: poles versus zeros

The relevant equivalence in OPUC is not about the Schur coefficients of the measure $dm_\xi$, but about the Schur function (or Carathéodory function) of the measure and the location of its poles in the disk. But the poles of the Carathéodory function of $dm_\xi$ correspond to point mass on the circle (possible zeros of $\xi$ on the critical line with infinite multiplicity), not to the zeros of $F$ in the interior of the disk. The OPUC formalism does not directly capture the non-vanishing condition of $F$.

### 5.3. What is missing

To connect OPUC with RH in a non-circular way, one would need to identify a natural measure $d\mu$ for which:

(a) The Schur coefficients $\alpha_k$ are related concretely and computably to the function $F(z)$ or to the zeros of $\xi$.

(b) The condition $|\alpha_k| < 1$ (or some other condition on the $\alpha_k$) is equivalent, nontrivially, to the non-vanishing of $F$ in the disk.

To date, such an identification has not been established in this program.

---

## §6. Properties of $\xi$ independent of the position of its zeros

### 6.1. The question

Does there exist any property of $\xi$ that is verifiable without knowing the position of its zeros and that implies the non-vanishing of $F$ in $\{|z|<1\}$?

### 6.2. Known properties of $\xi$

The function $\xi$ satisfies the following known unconditional properties:
- It is entire of order 1.
- It satisfies $\xi(s) = \xi(1-s)$ (functional equation).
- It has the Hadamard product $\xi(s) = \xi(0) \prod_\rho (1 - s/\rho) e^{s/\rho}$, where the product runs over all nontrivial zeros $\rho$ and converges absolutely.
- $\xi(s) > 0$ for real $s$, $0 < s < 1$ (in the real "critical strip").
- The argument $S(T) = (1/\pi)\arg\xi(1/2+iT)$ satisfies $S(T) = O(\log T)$.
- The zeros are symmetric with respect to $s = 1/2$ and with respect to $\mathbb{R}$ (since $\xi$ is real on the real line).

### 6.3. Why they are not enough to force non-vanishing in the disk

All these properties are compatible with the existence of zeros of $\xi$ off the critical line (assuming RH is false). In particular:
- The Hadamard product has the same formal appearance with or without off-critical zeros; non-vanishing in $\mathrm{Re}(s) < 1/2$ (equivalently, of $F$ in $|z|<1$) does not follow from the form of the product.
- The functional equation makes the zeros symmetric with respect to the line $\mathrm{Re}(s) = 1/2$ but does not force them to lie on it.
- The growth (order 1, genus 1) is compatible with zeros distributed arbitrarily in the strip $0 < \mathrm{Re}(s) < 1$.

**Proposition 6.1.** *None of the properties listed in §6.2 individually implies (nor, as far as is known, in combination) that $F(z)$ has no zeros in $\{|z| < 1\}$.*

### 6.4. A possible route: differential or functional equations for $F$

If $F(z)$ satisfied a first-order ordinary differential equation with no singular points in $\{|z| \leq 1\}$ forcing the solutions to be non-vanishing, or a contraction functional equation on the disk, non-vanishing could be deduced without direct reference to the zeros of $\xi$. However:

- The function $\xi(s)$ does not satisfy any linear differential equation with polynomial coefficients (unlike hypergeometric functions or Bessel functions). This follows from $\xi$ not being a function of algebraic $D$-module type.

- The functional equation $\xi(s) = \xi(1-s)$ translates, in terms of $F$, into $F(z) = F(\tau'(z))$ for some involution $\tau'$ of the disk, but this symmetry does not restrict the location of zeros beyond what was established in §2.

The search for such a differential or functional equation for $F$ constitutes an open direction for Phase 35.

---

## §7. The central obstruction: circularity of the reformulation

### 7.1. The exact reformulation

Proposition 2.1 establishes exactly:
$$\text{RH} \iff F(z) = \xi(z/(z-1)) \text{ has no zeros in } \{|z| < 1\}.$$
This equivalence is exact, with no loss of information and no additional hypotheses. It is a completely faithful reformulation of RH.

### 7.2. The vicious circle

To prove non-vanishing of $F$ in the disk $\{|z|<1\}$ one needs to control the position of the zeros of $\xi$ in $\{\mathrm{Re}(s) < 1/2\}$, which is precisely RH. To date, no argument exists that proves non-vanishing of $F$ in $\{|z|<1\}$ without essentially proving RH.

More precisely: any argument showing that $F$ has no zeros in $\{|z|<1\}$ would by construction be a proof of RH, but an argument that showed this via "simpler" or "more accessible" properties of $F$ would constitute real progress. The obstacle is not logical circularity (every proof of RH is circular in that sense), but the absence of properties of $F$ that are (a) verifiable without knowing the zeros, and (b) sufficient for non-vanishing.

### 7.3. Comparison with Paths 1 and 3

Path 1 (OPUC-Jacobi) reformulates RH as the condition $a_k^{full} = a_k^\infty$ for every $k$; similarly, this is exact but no proof is known. Path 3 (DBN-CCM) reformulates RH as $T_\lambda = 0$ for every $\lambda$; also exact, but the required cancellation seems to need information about the zeros. Path 2 joins this list: exact reformulations, with no progress toward a proof.

---

## §8. Synthesis and open questions for Phase 35

### 8.1. Clean picture of Path 2

Path 2 produces the following structure:

- $F(z) = \xi(z/(z-1))$ is analytic in $\{|z| < 1\}$.
- $F(0) = \xi(0) = 1/2$ (in particular, $|F(0)| = 1/2 < 1$).
- The zeros of $F$ on $|z|=1$ correspond exactly to the zeros of $\xi$ on the critical line (under RH, all the zeros are here).
- RH $\iff$ $F$ has no zeros in $\{|z| < 1\}$ (Proposition 2.1).
- The boundary positivity condition $\mathrm{Re}[L(e^{i\theta})] \geq 0$ is incorrect (Proposition 3.1).
- The Herglotz condition $\mathrm{Re}[C_\xi(z)] \geq 0$ in the interior is automatic (§4.2) and does not imply RH.
- The Schur coefficients of $dm_\xi$ automatically lie in the closed unit disk (§5.1) and do not imply RH.

### 8.2. Open questions

**Q1.** Does $F(z)$ satisfy any differential or functional equation whose solutions are automatically zero-free in the disk, as a consequence of the structure of $\xi$?

**Q2.** Does there exist a measure $d\mu$ on the unit circle, constructed from $\xi$ without explicit reference to its zeros, such that the Carathéodory function of $d\mu$ is directly related to $F$ and captures the non-vanishing condition?

**Q3.** Does the Hadamard product of $\xi$, when transferred to the disk via $\tau$, give a finite or infinite Blaschke product whose convergence imposes restrictions on the location of its factors?

**Q4.** The Li condition, $\lambda_n \geq 0$ for every $n$, is equivalent to RH and is related to the derivatives of $L(z)$ at $z=0$ (see Docs 75, 78). Can the non-negativity of the $\lambda_n$ be deduced from properties of $F$ in the disk without going through the position of the zeros?

These four questions define the working space of Path 2 in Phase 35.

---

## Appendix: Verification of Proposition 1.1

For greater clarity, we give the direct verification that $|z| < 1 \implies \mathrm{Re}(\tau(z)) < 1/2$.

Let $z = x+iy \in \mathbb{C}$ with $|z| < 1$, i.e., $x^2 + y^2 < 1$. We compute:
$$\tau(z) = \frac{z}{z-1} = \frac{(x+iy)}{(x-1)+iy} = \frac{(x+iy)\overline{((x-1)+iy)}}{|(x-1)+iy|^2} = \frac{(x+iy)((x-1)-iy)}{(x-1)^2+y^2}.$$
The real part of the numerator is $x(x-1) + y^2 = x^2 - x + y^2$. Hence,
$$\mathrm{Re}(\tau(z)) = \frac{x^2 + y^2 - x}{(x-1)^2 + y^2}.$$
The condition $\mathrm{Re}(\tau(z)) < 1/2$ is equivalent to $2(x^2 + y^2 - x) < (x-1)^2 + y^2$, i.e., $2x^2 + 2y^2 - 2x < x^2 - 2x + 1 + y^2$, i.e., $x^2 + y^2 < 1$. This is exactly the condition $|z| < 1$. $\square$

---

*Doc 81 completed. Next: Phase 35, exploration of Questions Q1–Q4.*
