# Document 74 — The Weil mechanism: function-field ↔ number-field analogy

**Program:** Riemann Hypothesis — Phase 33 DBN-CCM  
**Prerequisites:** Docs 64, 70, 71, 72, 73

---

## Summary

The CTP criterion of this program establishes: RH $\iff T_\lambda = 0$ for all $\lambda > 0$. In the case of smooth projective curves $C/\mathbb{F}_q$, the Riemann hypothesis is a theorem (Weil 1948). We show that $T_\lambda^C = 0$ holds trivially as a direct consequence of Weil's theorem: since all zeros of $Z_C$ are critical, the difference of measures is zero. The document identifies the three pillars of the Weil mechanism — Frobenius, Poincaré duality, positivity — and formulates the import question: which operator on the number-field world plays the role of Frobenius?

---

## §1. The zeta function of curves and Weil's Riemann hypothesis

### 1.1. Setup

Let $q = p^r$ be a prime power, and let $C$ be a smooth, geometrically irreducible projective curve defined over $\mathbb{F}_q$. For each $n \geq 1$, let $N_n = \#C(\mathbb{F}_{q^n})$ be the number of rational points over the degree-$n$ extension.

**Definition 1.1 (Weil zeta function).** The zeta function of the curve $C/\mathbb{F}_q$ is the formal series:

$$Z_C(u) = \exp\!\left(\sum_{n=1}^{\infty} N_n \frac{u^n}{n}\right) \in \mathbb{Q}[[u]].$$

**Proposition 1.2 (Weil 1948, rationality).** $Z_C(u)$ is a rational function of the form

$$Z_C(u) = \frac{P_C(u)}{(1-u)(1-qu)},$$

where $P_C(u) \in \mathbb{Z}[u]$ is a polynomial of degree $2g$, with $g = g(C)$ the genus of $C$.

*Proof.* See Weil [W48], also Bombieri [B74]. The Lefschetz formula for the Frobenius extension is used. $\square$

**Proposition 1.3 (Functional equation).** $Z_C$ satisfies the functional equation:

$$Z_C(1/(qu)) = q^{1-g} u^{2-2g} Z_C(u).$$

In terms of $P_C$: if $\alpha_1, \ldots, \alpha_{2g}$ are the roots of $P_C$ (counted with multiplicity), then the $\alpha_j$ pair up as $\{\alpha_j, q/\alpha_j\}$.

**Theorem 1.4 (Riemann hypothesis for curves, Weil 1948).** For each root $\alpha_j$ of $P_C(u)$,

$$|\alpha_j| = q^{1/2}.$$

Equivalently, the zeros of $Z_C(u)$ (as a meromorphic function in $u \in \mathbb{C}$) coming from $P_C$ all have modulus exactly $q^{-1/2}$.

*Remark.* The usual statement is phrased in terms of the variable $s$ via the substitution $u = q^{-s}$: the zeros of $s \mapsto Z_C(q^{-s})$ satisfy $\mathrm{Re}(s) = 1/2$, in perfect analogy with the Riemann conjecture for $\zeta(s)$.

### 1.2. The polynomial $L_C(u) = P_C(u)$ via $\ell$-adic cohomology

Fix a prime $\ell \neq p$. The key to Weil's theorem is the cohomological interpretation:

$$P_C(u) = \det\!\bigl(1 - u \cdot \mathrm{Fr}_q \mid H^1_{\text{ét}}(\bar{C}, \mathbb{Q}_\ell)\bigr),$$

where $\mathrm{Fr}_q : \bar{C} \to \bar{C}$ is the geometric Frobenius morphism ($x \mapsto x^q$ in affine coordinates) and $H^1_{\text{ét}}(\bar{C}, \mathbb{Q}_\ell)$ is the first $\ell$-adic étale cohomology of the curve base-changed to $\overline{\mathbb{F}_q}$.

The roots $\alpha_j$ of $P_C$ are precisely the eigenvalues of the operator $\mathrm{Fr}_q^*$ acting on $H^1_{\text{ét}}(\bar{C}, \mathbb{Q}_\ell)$, which is a $\mathbb{Q}_\ell$-vector space of dimension $2g$.

---

## §2. The spectral measure $dm_C$ and the discrepancy trace

### 2.1. Measures in the CCM formalism

We recall the formalism of the previous documents. The archimedean measure is:

$$dm_\infty(s) = (2\pi)^{-2}\,|\Gamma(1/4 + is/2)|^2\,ds,$$

with orthogonal polynomials $\{P_k\}_{k \geq 0}$ (normalized in $L^2(dm_\infty)$) and Jacobi coefficients:

$$a_k^\infty = \tfrac{1}{2}\sqrt{(2k+1)(2k+2)}.$$

The Abel kernel associated with the parameter $\lambda > 0$ is:

$$W_\lambda(s) = \sum_{n=0}^{N(\lambda)} (a_n^\infty)^2\bigl(|P_{n+1}(s)|^2 - |P_n(s)|^2\bigr),$$

where $N(\lambda) = \max\{n : \gamma_n \leq \lambda\}$. This kernel satisfies $W_\lambda(s) \geq 0$ for all $s \in \mathbb{R}$.

### 2.2. Adaptation to the function-field case

The function $s \mapsto Z_C(q^{-1/2-is})$ is the translation of $Z_C$ to the critical line (real variable $s$). Its zeros in $s$ are exactly the $s_j$ such that $q^{-1/2-is_j} = \alpha_j^{-1}$, i.e., $s_j = -\frac{1}{i}(1/2 - \log_q|\alpha_j| + i\arg(\alpha_j)/\log q)$.

**Definition 2.1 (Spectral measure of $C$).** The full spectral measure associated with $C$ is:

$$dm_C(s) = dm_\infty(s) \cdot |Z_C(q^{-1/2-is})|^2.$$

This measure may not have finite total mass in general; for the purposes of the CCM formalism we are interested in its ratio with the analogous "on-critical" measure.

**Definition 2.2 (On-critical version).** Let $Z_{C,\text{on}}$ be the function obtained from $Z_C$ by replacing each zero $u_j = \alpha_j^{-1}$ of modulus $|u_j|$ with $q^{-1/2} e^{i\arg(u_j)}$ (i.e., projecting onto the circle $|u| = q^{-1/2}$). We define:

$$dm_{C,\text{on}}(s) = dm_\infty(s) \cdot |Z_{C,\text{on}}(q^{-1/2-is})|^2.$$

**Definition 2.3 (Discrepancy trace for $C$).** For $\lambda > 0$, the discrepancy trace of the function-field model is:

$$T_\lambda^C = \int_{\mathbb{R}} W_\lambda(s)\,\bigl(dm_C(s) - dm_{C,\text{on}}(s)\bigr).$$

---

## §3. $T_\lambda^C = 0$ as an immediate consequence of Weil's theorem

### 3.1. The central theorem of this section

**Theorem 3.1.** For every smooth projective curve $C/\mathbb{F}_q$ and every $\lambda > 0$,

$$T_\lambda^C = 0.$$

*Proof.* By Theorem 1.4 (Weil's Riemann hypothesis), all zeros of $Z_C(u)$ coming from $P_C$ satisfy $|\alpha_j^{-1}| = q^{-1/2}$. Hence each zero $u_j = \alpha_j^{-1}$ of $Z_C$ already lies on the circle $|u| = q^{-1/2}$. The "on-critical projection" operation does not change any zero. Thus:

$$Z_{C,\text{on}} = Z_C \quad \text{as meromorphic functions},$$

whence $|Z_{C,\text{on}}(q^{-1/2-is})|^2 = |Z_C(q^{-1/2-is})|^2$ for all $s \in \mathbb{R}$. This implies:

$$dm_C(s) = dm_{C,\text{on}}(s) \quad dm_\infty\text{-a.e.},$$

and hence the integrand of $T_\lambda^C$ is identically zero. The integral is zero for all $\lambda > 0$. $\square$

### 3.2. Comparison with the number-field case

The CTP criterion of the program establishes (Doc 64, Thm. 3.1):

$$\text{RH for } \zeta \iff T_\lambda = 0 \;\text{ for all } \lambda > 0.$$

Theorem 3.1 is the exact analogue with $\zeta$ replaced by $Z_C$: the condition $T_\lambda^C = 0$ is equivalent to RH for $C$, and RH for $C$ is a theorem. The fundamental difference is that in the number-field case the direction $\Rightarrow$ (RH $\Rightarrow T_\lambda = 0$) is immediate and the direction $\Leftarrow$ is also proved, but nobody knows how to prove RH. In the case of curves, the work is done by Weil's theorem.

---

## §4. The mechanism: Frobenius, Poincaré duality, positivity

Weil's theorem is not trivial. Its proof (completed by Weil and clarified by Grothendieck–Deligne) rests on three pillars. We identify them precisely because we will look for their analogue in the number-field world.

### 4.1. Pillar I: The Frobenius operator

**Definition 4.1.** The geometric Frobenius morphism $\mathrm{Fr}_q : \bar{C} \to \bar{C}$ acts on $\ell$-adic cohomology:

$$\mathrm{Fr}_q^* : H^i_{\text{ét}}(\bar{C}, \mathbb{Q}_\ell) \to H^i_{\text{ét}}(\bar{C}, \mathbb{Q}_\ell), \quad i = 0, 1, 2.$$

The zeros of $Z_C$ are the reciprocals of the eigenvalues of the operator $\mathrm{Fr}_q^*|_{H^1}$.

**Crucial point:** The eigenvalues of Frobenius are algebraic and their moduli are accessible because $\mathrm{Fr}_q$ is a *concrete, well-defined* operator on a cohomological space of finite dimension $2g$. The problem with Riemann's zeta is that there is no analogous operator defined for $\zeta$.

### 4.2. Pillar II: Poincaré duality

On the curve $C$ of dimension $1$ (projective curve), Poincaré duality provides a perfect pairing:

$$H^1_{\text{ét}}(\bar{C}, \mathbb{Q}_\ell) \times H^1_{\text{ét}}(\bar{C}, \mathbb{Q}_\ell) \to H^2_{\text{ét}}(\bar{C}, \mathbb{Q}_\ell) \cong \mathbb{Q}_\ell(-1).$$

In terms of eigenvalues: if $\alpha$ is an eigenvalue of $\mathrm{Fr}_q^*|_{H^1}$, then $q/\alpha$ is also one. This pairs up the eigenvalues into pairs $(\alpha, q/\alpha)$ under the involution $\alpha \mapsto q/\alpha$.

**Consequence for the moduli:** If $|\alpha| = r$, then $|q/\alpha| = q/r$. For the pair $\{\alpha, q/\alpha\}$ to be consistent with the functional equation (which forces the symmetry $u \mapsto 1/(qu)$), the product of the moduli must be $r \cdot (q/r) = q$. This does not yet force $r = q^{1/2}$; duality imposes the functional symmetry but not positivity.

### 4.3. Pillar III: Positivity (the decisive argument)

Positivity is the heart of the argument. There are two approaches:

**Weil's approach (1948):** Weil used the theory of correspondences on the product variety $C \times C$ over $\mathbb{F}_q$. The intersection form on divisors of $C \times C$ is positive definite in a certain sense (the Castelnuovo–Severi inequality), and this forces $|\alpha_j| = q^{1/2}$.

Concretely, let $\Gamma \subset C \times C$ be the graph of Frobenius. The self-intersection $(\Gamma \cdot \Gamma)$ is $q + 2 - N_1$, and the Hodge inequality implies:

$$N_1 \leq q + 1 + 2g\sqrt{q},$$

which in turn implies that the $\alpha_j$ cannot have $|\alpha_j| > q^{1/2}$ nor $|\alpha_j| < q^{1/2}$ (using the functional equation for both directions).

**Deligne's approach (1974, Weil II):** For higher-dimensional varieties, Deligne proved purity of the Frobenius eigenvalues using the theory of perverse sheaves and the hard Lefschetz theorem. The positivity argument becomes that of positivity of the intersection form on primitive cohomology.

**Proposition 4.2 (Positivity forces criticality).** Let $V = H^1_{\text{ét}}(\bar{C}, \mathbb{Q}_\ell)$ with the bilinear form $\langle \cdot, \cdot \rangle$ induced by Poincaré duality and the Weil pairing. Then $\langle v, \mathrm{Fr}_q^* v\rangle > 0$ for all $v \neq 0$ (in a suitable version over $\mathbb{R}$), and this implies $|\alpha_j| = q^{1/2}$.

*Proof sketch.* Positivity of the form $v \mapsto \langle v, \mathrm{Fr}_q^* v \rangle$ (essentially the positivity of the intersection number $(\Gamma \cdot {}^t\Gamma)$ on $C \times C$, where ${}^t\Gamma$ is the graph of the transposed Frobenius) together with the duality $\alpha \mapsto q/\alpha$ forces all eigenvalues to lie on the rescaled unit circle $|\alpha| = q^{1/2}$. If there existed $|\alpha| < q^{1/2}$, then by duality there would exist $|q/\alpha| > q^{1/2}$, and the associated quadratic form would have indefinite sign, contradicting positivity. $\square$

### 4.4. Synthesis of the mechanism

The Weil mechanism can be summarized in the logical diagram:

$$\underbrace{\text{concrete Frobenius on }H^1}_{\text{Pillar I}} + \underbrace{\text{Poincaré duality}}_{\text{Pillar II}} + \underbrace{\text{positivity of the intersection}}_{\text{Pillar III}} \implies |\alpha_j| = q^{1/2} \implies T_\lambda^C = 0.$$

The import question to the number-field case is: does an analogue of each of these three pillars exist for the Riemann zeta function?

---

## §5. The import question for the number-field case

### 5.1. The Hilbert–Pólya problem

**Conjecture 5.1 (Hilbert–Pólya).** There exists a self-adjoint operator $H$ acting on some Hilbert space $\mathcal{H}$ such that the spectrum of $H$ is the set $\{t_n\}$ of imaginary parts of the zeros of $\zeta(1/2 + it)$.

If the Hilbert–Pólya conjecture were true, self-adjointness of $H$ would force the $t_n$ to be real, i.e., that the zeros of $\zeta$ lie on the critical line. This would be the analogue of Pillar I (Frobenius = concrete operator with eigenvalues = zeros) plus a version of Pillar III (self-adjointness = positivity).

### 5.2. The CCM formalism as a candidate

The CCM program (Connes–Consani–Moscovici 2024) proposes the Jacobi operator $J^{full}$ acting on $\ell^2(\mathbb{N})$ as a natural candidate for the Hilbert–Pólya operator.

**Definition 5.2 (Full Jacobi operator).** Given the orthogonal polynomials $\{Q_k\}$ associated with the measure $dm_{full}(s) = dm_\infty(s) \cdot |\zeta(1/2+is)|^2$, the Jacobi operator $J^{full}$ is the symmetric tridiagonal operator:

$$J^{full} e_k = a_k^{full} e_{k+1} + b_k^{full} e_k + a_{k-1}^{full} e_{k-1},$$

where $a_k^{full}, b_k^{full}$ are the Jacobi coefficients of the measure $dm_{full}$.

The operator $J^\infty$ corresponding to $dm_\infty$ has exact coefficients $a_k^\infty = \frac{1}{2}\sqrt{(2k+1)(2k+2)}$ (from the metaplectic representation).

**Remark 5.3.** The operator $J^{full}$ is completely determined by the spectrum of $\zeta$ (all zeros of $\zeta$ are encoded in $dm_{full}$ via the Hadamard product), and formally its generalized eigenvalues should be related to the spectral support of $dm_{full}$.

### 5.3. The Frobenius analogue

In the world of curves, Frobenius $\mathrm{Fr}_q$ is the "raise to the $q$-th power" morphism, a geometrically defined endomorphism. In the world of numbers, the closest analogue is the arithmetic shift operator. The candidates in the literature are:

1. **Connes's operator (1999):** An operator on the space of adeles acting as multiplication by values of the idele class, whose spectrum is related to the zeros of $\zeta$ via Weil's trace formula. Adelic "time" plays the role of Frobenius.

2. **The Pólya–Hilbert Laplacian (Odlyzko–Schönhage–Berry–Keating):** The shifted operator $H = -d^2/dx^2 + x^2$, whose spectrum approximates the local distribution of the zeros of $\zeta$ but not the exact zeros.

3. **The Jacobi operator $J^{full}$ (CCM program):** The tridiagonal operator mentioned in Definition 5.2, which encodes the whole spectral information of $\zeta$.

**Open question 5.4.** Does there exist an operator $\Phi$ on a well-defined cohomological space such that:
- The eigenvalues of $\Phi$ are exactly the $e^{it_n}$ (or directly the $t_n$)?
- There exists a bilinear form $\langle \cdot, \cdot \rangle$ on that space satisfying an analogue of Poincaré duality?
- Positivity of $\langle v, \Phi v \rangle$ forces the eigenvalues of $\Phi$ to lie on the unit circle (equivalent to RH)?

---

## §6. Does a Frobenius operator exist in the CCM world?

### 6.1. Reformulation in terms of Jacobi coefficients

The CCM formalism translates the Frobenius question into a question about Jacobi coefficients. This is established as follows:

**Proposition 6.1.** The condition $T_\lambda = 0$ for all $\lambda > 0$ is equivalent to:

$$dm_{full} = dm_{full,on} \quad \text{as measures on } \mathbb{R},$$

which in turn (by uniqueness of the Jacobi coefficients) is equivalent to:

$$a_k^{full} = a_k^{full,on} \quad \text{for all } k \geq 0.$$

*Proof.* Two measures have the same orthogonal polynomials (and hence the same Jacobi coefficients) if and only if they are equal as measures (uniqueness theorem for the spectral measure of symmetric Jacobi operators). Equivalence with $T_\lambda = 0$ for all $\lambda$ comes from Theorem 3.1 of Doc 64. $\square$

**Corollary 6.2.** RH is equivalent to equality of the Jacobi coefficients:

$$\text{RH} \iff a_k^{full} = a_k^{full,on} \quad \forall k \geq 0.$$

### 6.2. Positivity in the CCM world

The analogue of Pillar III (positivity of the intersection form) should be a statement about the Jacobi operator. We identify the natural formulation:

**Definition 6.3 (Jacobi quadratic form).** Let $J = J^{full}$ be the Jacobi operator of $dm_{full}$, with coefficients $a_k^{full}, b_k^{full}$. We define the quadratic form:

$$Q_{J}(v) = \langle v, J v \rangle_{\ell^2} = \sum_{k \geq 0} b_k^{full} |v_k|^2 + 2\sum_{k \geq 0} a_k^{full} \mathrm{Re}(v_k \bar{v}_{k+1}).$$

If $J$ were the analogue of Frobenius, the positivity condition would be: $Q_J(v) > 0$ for all $v \neq 0$ in a suitable space.

**Remark 6.4.** In the function-field case, positivity of $\langle v, \mathrm{Fr}_q^* v \rangle$ comes from the geometric interpretation (number of points of the curve, which is a non-negative integer). In the number-field world, the analogous positivity would have to come from an intrinsic property of $dm_{full}$, such as complete monotonicity or the positivity of certain Hankel determinants.

### 6.3. The Poincaré duality analogue

In the case of curves, Poincaré duality manifests as the symmetry $\alpha \mapsto q/\alpha$ of the Frobenius eigenvalues. In the case of $\zeta$, the functional equation $\xi(s) = \xi(1-s)$ (where $\xi(s) = s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$) imposes the symmetry:

$$\rho \text{ is a zero of } \zeta \implies 1-\rho \text{ is a zero of } \zeta.$$

This is the analogue of $\alpha \mapsto q/\alpha$ under the correspondence $\alpha = q^{1-\rho}$.

**Proposition 6.5 (CCM duality).** The functional equation of $\xi$ induces on the Jacobi coefficients of $dm_{full}$ the symmetry:

$$b_k^{full} = 0 \quad \text{for all } k \geq 0$$

(the diagonal coefficients vanish), since the measure $dm_{full}$ is symmetric: $dm_{full}(-s) = dm_{full}(s)$.

*Proof.* The symmetry $|\zeta(1/2+is)|^2 = |\zeta(1/2-is)|^2$ (which follows from the functional equation) implies that $dm_{full}$ is an even measure in $s$. The orthogonal polynomials of an even measure are alternately even and odd, which forces $b_k = 0$ for all $k$. $\square$

**Corollary 6.6.** The Jacobi coefficients of $dm_{full}$ reduce to the off-diagonal coefficients $\{a_k^{full}\}_{k \geq 0}$. The condition RH $\iff a_k^{full} = a_k^{full,on}$ involves only this family.

### 6.4. The concrete question

The three pillars of the Weil mechanism translate to the CCM world as follows:

| Pillar (curves) | Object (curves) | Proposed analogue (numbers, CCM) |
|---|---|---|
| Frobenius | $\mathrm{Fr}_q^* : H^1 \to H^1$ | Jacobi operator $J^{full}$ on $\ell^2(\mathbb{N})$ |
| Poincaré duality | Symmetry $\alpha \mapsto q/\alpha$ | Functional equation $\rho \mapsto 1-\rho$ (Prop. 6.5) |
| Positivity | $\langle v, \mathrm{Fr}_q^* v \rangle > 0$ | $a_k^{full} > 0$ and is there some Turán-type inequality? |

The concrete question that emerges is:

**Open question 6.7 (The positivity-argument analogue).** Does there exist an intrinsic positivity property of the coefficients $a_k^{full}$ (analogous to the positivity of Weil's intersection form) that implies $a_k^{full} = a_k^{full,on}$ for all $k$?

A more precise formulation: in the case of curves, positivity says that the number of points $N_n = \#C(\mathbb{F}_{q^n})$ is a non-negative integer. In the number-field case, the analogues of $N_n$ are the arithmetic coefficients $\sum_{m \leq x} \Lambda(m)$ (integrated von Mangoldt function), which are positive but whose positivity does not directly force RH.

---

## §7. Conclusions and conjectures

### 7.1. What is proved

**Summary of results proved in this document:**

1. (Theorem 3.1) For every curve $C/\mathbb{F}_q$, $T_\lambda^C = 0$ for all $\lambda > 0$, as a direct consequence of Weil's theorem.

2. (Proposition 6.1) In the number-field case, $T_\lambda = 0$ for all $\lambda \iff a_k^{full} = a_k^{full,on}$ for all $k$.

3. (Proposition 6.5) The diagonal coefficients $b_k^{full} = 0$ for all $k$ (consequence of the functional equation). RH reduces to equality of the coefficients $a_k^{full}$.

### 7.2. The fundamental obstacle

The qualitative difference between the case of curves and the case of numbers is the following:

**In the case of curves:** Frobenius $\mathrm{Fr}_q$ is an explicit operator (raising to the $q$-th power) acting on a space of *finite* dimension $2g$. Positivity of the intersection form is a statement about a finite number of eigenvalues, and can be established via algebraic counting on the variety $C \times C$.

**In the case of numbers:** There is no explicit operator on a finite-dimensional space whose eigenvalues are the zeros of $\zeta$. The natural Hilbert space ($L^2$ of some adele space, or the Jacobi space $\ell^2(\mathbb{N})$) is infinite-dimensional, and positivity of the corresponding quadratic form is not evident.

### 7.3. Conjectures for the next phase

**Conjecture 7.1 (Arithmetic Frobenius).** There exists an operator $\Phi_{ar}$ on a Hilbert space $\mathcal{H}_{ar}$ (to be defined) with the following properties:
- $\mathrm{spec}(\Phi_{ar}) = \{e^{it_n} : t_n \in \mathbb{R},\; \zeta(1/2+it_n) = 0\}$.
- There exists a bilinear form $\langle \cdot, \cdot \rangle_{ar}$ on $\mathcal{H}_{ar}$ that is the analogue of Poincaré duality, consistent with the functional equation of $\xi$.
- Positivity of $v \mapsto \langle v, \Phi_{ar} v \rangle_{ar}$ implies $\mathrm{spec}(\Phi_{ar}) \subset S^1$, equivalent to RH.

**Conjecture 7.2 (CCM identification).** The Jacobi operator $J^{full,on}$ (associated with $dm_{full,on}$) is the natural candidate for the arithmetic Frobenius operator of Conjecture 7.1. More precisely:
- The Hilbert space is $\ell^2(\mathbb{N})$.
- The bilinear form is $\langle e_j, e_k \rangle_{ar} = \delta_{j+k, 2K}$ for some $K$ (implementing the symmetry $j \leftrightarrow 2K-j$ analogous to $\rho \leftrightarrow 1-\rho$).
- The positivity condition translates to $a_k^{full,on} > a_k^\infty$ for all $k$ (a growth hypothesis for Jacobi coefficients under the effect of the zeros of $\zeta$).

**Conjecture 7.3 (Jacobi positivity criterion).** The condition $a_k^{full} = a_k^{full,on}$ for all $k$ is equivalent to the following positivity statement: for every $N \geq 1$ and every finite vector $v = (v_0, \ldots, v_N) \in \mathbb{R}^{N+1}$,

$$\sum_{j,k=0}^{N} v_j v_k \int_{\mathbb{R}} Q_j(s) Q_k(s)\, dm_{full}(s) \geq 0,$$

where $\{Q_k\}$ are the polynomials of $dm_{full,on}$. This statement is the positivity of the "comparison operator" between the two measures, and would be the direct analogue of the positivity of Weil's intersection form.

### 7.4. The lesson of the analogy

The function-field/number-field analogy, seen through the CCM lens, suggests that the obstacle to proving RH is not so much the lack of a suitable formula (the criterion $T_\lambda = 0$ already exists), but the lack of a concrete geometric object (Frobenius) whose mere existence and formal properties (duality + positivity) force criticality of the zeros.

The program for Phase 34 is therefore: identify whether the coefficients $a_k^{full}$ satisfy some "positivity"-type inequality that can be established without assuming RH, and that in turn forces $T_\lambda = 0$.

---

## References

- [W48] A. Weil, *Sur les courbes algébriques et les variétés qui s'en déduisent*, Hermann, Paris, 1948.
- [B74] E. Bombieri, *Counting points on curves over finite fields (d'après S. A. Stepanov)*, Séminaire Bourbaki, 1974.
- [D74] P. Deligne, *La conjecture de Weil I*, Publ. Math. IHÉS 43 (1974), 273–307.
- [C99] A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Math. 5 (1999), 29–106.
- [CCM24] A. Connes, C. Consani, H. Moscovici, *Spectral triples and zeta functions*, preprint, 2024.
- [Docs 64, 70–73] Internal documents of the program, Phases 32–33.

---

*End of Document 74.*
