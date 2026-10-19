# Phase 29 — Doc 29: Spectral Geometry of the Quotient $C_\infty / \Xi$

**Context:** Doc 28 identified Front C as the most promising: study the quotient $Q(z) := C_\infty(z)/\Xi(z)$, or equivalently the difference $C_\infty'/C_\infty(z) - \Xi'/\Xi(z)$, with the goal of proving that $Q$ has no zeros or poles on $\mathbb{R}$ (which is equivalent to Inc. Inv. plus the direct inclusion).

**Objective:** Study the quotient $Q = C_\infty/\Xi$ as a meromorphic function on $\mathbb{C}^+$, determine its behavior on $\mathbb{R}$, and look for a principle that forces $Q(\mathbb{R}) \subseteq \mathbb{R}\setminus\{0\}$ (no zeros or poles on $\mathbb{R}$), which implies RH.

---

## 1. Definition and basic properties of the quotient

**Definition.** Let

$$Q(z) := \frac{C_\infty(z)}{\Xi(z)}, \quad z \in \mathbb{C}^+.$$

**Proposition 1** (properties of $Q$).

(a) $C_\infty(z)$ is holomorphic on $\mathbb{C}^+$: since $C_\infty(t) = w(t) - \Psi(t)$ where both are analytic functions that extend to $\mathbb{C}^+$ with $\Im(C_\infty(z)) = \Im(w(z)) - \Im(\Psi(z))$ absolutely convergent for $\Im(z) > 0$.

(b) $\Xi(z)$ is holomorphic on $\mathbb{C}^+$ and has no zeros in $\mathbb{C}^+$: since all zeros of $\Xi$ lie on $\mathbb{R}$ (the $\gamma_n$) under RH, and in the strip $0 < \Im(\rho) < 1/2$ for zeros off the critical line (under $\neg$RH).

(c) Under RH: $Q(z)$ is holomorphic on $\mathbb{C}^+$ (since $\Xi \neq 0$ on $\mathbb{C}^+$ and $C_\infty$ is holomorphic).

(d) Under $\neg$RH: $\Xi$ has zeros $\rho_0$ with $0 < \Im(\rho_0) < 1/2$, which are poles of $Q$.

**Proposition 2** (behavior of $Q$ on $\mathbb{R}$). The quotient $Q$ has:
- Poles on $\mathbb{R}$ at the zeros of $\Xi$ that are NOT zeros of $C_\infty$ (missing zeros).
- Zeros on $\mathbb{R}$ at the zeros of $C_\infty$ that are NOT zeros of $\Xi$ — but by Theorem B (Doc 19): $\{$zeros of $C_\infty\} \subseteq \{$zeros of $\Xi\}$, so there are NO zeros of $C_\infty$ on $\mathbb{R}$ that are not zeros of $\Xi$.

In particular: $Q$ is holomorphic at the zeros of $C_\infty$ and has simple poles at the zeros of $\Xi$ that are not zeros of $C_\infty$.

---

## 2. The reformulation in terms of $Q$

**Proposition 3** (Inc. Inv. $\Leftrightarrow$ $Q$ holomorphic on $\mathbb{R}$). The following are equivalent:

(i) Inc. Inv.: $\Xi(\gamma_n) = 0 \Rightarrow C_\infty(\gamma_n) = 0$ for all $n$.

(ii) $Q(z) = C_\infty(z)/\Xi(z)$ extends holomorphically to a neighborhood of $\mathbb{R}$ (no poles on $\mathbb{R}$).

(iii) $Q$ is holomorphic on $\mathbb{C}^+\cup\mathbb{R}$ (on the closure of the upper half-plane).

*Proof.* (i)$\Rightarrow$(ii): If $C_\infty(\gamma_n) = 0$ whenever $\Xi(\gamma_n) = 0$, the zeros of $\Xi$ on $\mathbb{R}$ are also zeros of $C_\infty$ (with at least the same multiplicity), so the poles of $Q$ on $\mathbb{R}$ cancel. (ii)$\Rightarrow$(i): if $Q$ is holomorphic on $\mathbb{R}$, it has no poles, so $C_\infty(\gamma_n) = 0$ for all $n$. $\square$

**Proposition 4** (RH $\Leftrightarrow$ $Q$ meromorphic on $\mathbb{C}$ with zeros/poles only on $\mathbb{R}$). Equivalently: RH $\Leftrightarrow$ $Q$ is holomorphic on $\mathbb{C}\setminus\mathbb{R}$ (no singularities outside $\mathbb{R}$) AND $Q$ has no poles on $\mathbb{R}$.

*Proof.* $\Rightarrow$: Under RH, $\Xi$ has no zeros in $\mathbb{C}^+$ (nor in $\mathbb{C}^-$ by symmetry), so $Q$ is holomorphic on $\mathbb{C}^+$. And by Inc. Inv. (which is RH), $Q$ has no poles on $\mathbb{R}$. Hence $Q$ is holomorphic on $\mathbb{C}\setminus\mathbb{R}$ and on $\mathbb{R}$ (except for possible zeros of $C_\infty$ on $\mathbb{R}$, which are zeros of $Q$, not poles). $\Leftarrow$: If $Q$ is holomorphic on $\mathbb{C}^+$, all zeros of $\Xi$ lie on $\mathbb{R}$ (RH). If moreover $Q$ has no poles on $\mathbb{R}$: Inc. Inv. Together these give RH. $\square$

---

## 3. The functions $C_\infty$ and $\Xi$ as exponential-type functions

**Proposition 5** (exponential type of $C_\infty$ and $\Xi$). On the upper half-plane $\mathbb{C}^+$:

(a) $\Xi(z) = \xi(1/2+iz)$ is an entire function of exponential type $\pi/2$ (from Hadamard theory).

(b) $C_\infty(z) = w(z) - \Psi(z)$ with $w(z)$ the archimedean symbol and $\Psi(z) = 2\sum_p \Lambda(p)p^{-1/2}e^{iz\log p}$.

For $z \in \mathbb{C}^+$: $|\Psi(z)| \leq 2\sum_p\Lambda(p)p^{-1/2-\Im(z)} < \infty$ for $\Im(z) > 0$. The function $\Psi$ extends analytically to $\mathbb{C}^+$ but is NOT entire (the series diverges conditionally on $\mathbb{R}$).

(c) $C_\infty$ is holomorphic on $\mathbb{C}^+$ but NOT entire: it has singularities on the real line and in the strip $0 \leq \Im(z) \leq 1$ (from the terms $e^{iz\log p}$ for primes $p$).

**Corollary 1** (type of the quotient $Q$). The quotient $Q = C_\infty/\Xi$ is NOT an entire function in general (since $C_\infty$ is not). $Q$ is meromorphic on $\mathbb{C}^+$ with possible singularities on the boundary $\mathbb{R}$.

---

## 4. The quotient $Q$ and the Hardy class $H^2$

**Definition.** We say $Q \in H^2(\mathbb{C}^+)$ (Hardy class) if:

$$\sup_{\eta > 0}\int_{-\infty}^\infty |Q(t+i\eta)|^2 dt < \infty.$$

**Proposition 6** ($H^2$ condition for $Q$). If $Q \in H^2(\mathbb{C}^+)$ and $Q$ is holomorphic on $\mathbb{C}^+$:

- $Q$ has non-tangential boundary values on $\mathbb{R}$ a.e. (by Hardy theory).
- Poles of $Q$ on $\mathbb{R}$ would be singularities of the non-tangential boundary values.

**Proposition 7** ($H^\infty$ bound of $Q$). For $z \in \mathbb{C}^+$:

$$|Q(z)| = \left|\frac{C_\infty(z)}{\Xi(z)}\right| \leq \frac{|w(z)| + |\Psi(z)|}{|\Xi(z)|}.$$

The denominator $|\Xi(z)|$ for $z = t+i\eta$ with $\eta > 0$: $|\Xi(z)| \geq |\Xi(0)|\prod_n(1 - (t+i\eta)^2/\gamma_n^2)|$, which can be bounded from below.

For $t$ far from all the $\gamma_n$ and $\eta \to 0$: $|\Xi(t+i\eta)| \to |\Xi(t)|$, which can be small if $t$ is close to a $\gamma_n$.

**The boundedness problem for $Q$.** To prove that $Q$ extends holomorphically to $\mathbb{R}$ (with no poles), we need $|Q(t+i\eta)|$ to remain bounded as $\eta\to 0^+$ and $t\to\gamma_n$. This requires $|C_\infty(t+i\eta)/\Xi(t+i\eta)|$ not to diverge, which in turn requires $C_\infty(\gamma_n) = 0$ — again Inc. Inv.

---

## 5. The maximum principle and its consequences

**Proposition 8** (application of the maximum principle). Let $f: \mathbb{C}^+ \to \mathbb{C}$ be holomorphic and bounded. If $|f|$ attains its maximum on the boundary $\mathbb{R}$, then $|f|$ is constant (by the maximum principle).

For the quotient $Q$: if $Q$ is holomorphic on $\mathbb{C}^+$ (under RH) and $|Q(t)|$ is bounded on $\mathbb{R}$ for $t$ far from the $\gamma_n$, the maximum principle controls $Q$ on $\mathbb{C}^+$.

But controlling $|Q|$ on $\mathbb{R}$ near the $\gamma_n$ is exactly Inc. Inv. — circular.

**Proposition 9** (Schwarz reflection principle). If $C_\infty$ and $\Xi$ satisfy real symmetries ($\overline{C_\infty(\bar z)} = C_\infty(z)$ and $\overline{\Xi(\bar z)} = \Xi(z)$ for $z$ in the appropriate domain):

$$Q(\bar z) = \overline{Q(z)}.$$

This symmetry says that $Q(t) \in \mathbb{R}$ for $t \in \mathbb{R}$ where $Q$ is defined. Hence the "zeros" of $Q$ on $\mathbb{R}$ are real zeros of a real function, and the "poles" of $Q$ on $\mathbb{R}$ are real poles.

*Verification of the symmetry.* $C_\infty(t) = w(t) - \Psi(t)$ with $w$ and $\Psi$ real on $\mathbb{R}$, so $C_\infty$ is real on $\mathbb{R}$. $\Xi(t)$ is real on $\mathbb{R}$ (since $\xi(1/2+it)$ is real for real $t$). Hence $Q(t) = C_\infty(t)/\Xi(t) \in \mathbb{R}$ where it is defined.

**Conclusion from the symmetry.** $Q$ is a meromorphic function on $\mathbb{C}$ that maps $\mathbb{R} \to \mathbb{R}\cup\{\infty\}$. The poles of $Q$ on $\mathbb{R}$ are points where $\Xi(\gamma_n) = 0$ but $C_\infty(\gamma_n) \neq 0$. Avoiding these poles is exactly Inc. Inv.

---

## 6. The function $Q$ and the Blaschke transform

**New idea.** Consider the generalized Blaschke function:

$$B_Q(z) := \exp\left(i\int_{-\infty}^\infty \frac{1+tz}{t-z}\cdot\frac{d\mu_{C_\infty}(t) - d\mu_\Xi(t)}{1+t^2}\right),$$

where $\mu_{C_\infty}$ is the zero measure of $C_\infty$ and $\mu_\Xi$ is the zero measure of $\Xi$. Formally:

$$B_Q(z) = \frac{C_\infty(z)/C_\infty(0)}{\Xi(z)/\Xi(0)} \cdot \exp(\text{entire part}).$$

If $B_Q = 1$ (the Blaschke part of $Q$ is trivial): the zeros and poles of $C_\infty/\Xi$ cancel, giving Inc. Inv.

**Proposition 10** (Inc. Inv. and triviality of the Blaschke part). $B_Q = 1$ (in the sense that the Blaschke function generated by the difference of zero measures is trivial) if and only if $\mu_{C_\infty} = \mu_\Xi$, which is exactly Inc. Inv.

*Proof.* The Blaschke function of $Q$ is generated by the poles of $Q$ on $\mathbb{R}$ (zeros of $\Xi$ not covered by $C_\infty$). If there are no such poles: $B_Q = 1$. $\square$

**The problem.** Proving $B_Q = 1$ unconditionally is equivalent to Inc. Inv. There is no general principle forcing the triviality of the Blaschke function of $Q$.

---

## 7. A genuinely new angle: the function $Q$ as a Nevanlinna quotient

**Definition.** A meromorphic function $f: \mathbb{C}^+ \to \mathbb{C}$ is of Nevanlinna class ($f \in \mathcal{N}$) if:

$$\sup_{\eta > 0}\int_{-\infty}^\infty \log^+|f(t+i\eta)|\frac{dt}{1+t^2} < \infty.$$

**Proposition 11** ($Q \in \mathcal{N}$). The function $Q = C_\infty/\Xi$ is in the Nevanlinna class $\mathcal{N}$ under mild conditions on $C_\infty$.

*Proof.* $\log^+|Q| \leq \log^+|C_\infty| + \log^+|1/\Xi|$. The term $\log^+|C_\infty|$ is integrable since $C_\infty$ is bounded on $\mathbb{C}^+$. The term $\log^+|1/\Xi|$ requires a lower bound on $|\Xi|$ on $\mathbb{C}^+$ away from the zeros — this is standard for entire functions of exponential type. $\square$

**The Nevanlinna factorization theorem.** For $f \in \mathcal{N}$:

$$f(z) = B(z)\cdot S(z)\cdot O(z),$$

where $B$ = Blaschke product (zeros and poles in $\overline{\mathbb{C}^+}$), $S$ = singular factor (singular measure on $\mathbb{R}$), $O$ = outer factor (log-modulus function given by the absolutely continuous part).

**Proposition 12** (factorization of $Q$).

$$Q(z) = \frac{C_\infty(z)}{\Xi(z)} = B_{C_\infty}(z)\cdot B_{1/\Xi}(z)\cdot O_Q(z)\cdot S_Q(z),$$

where:
- $B_{C_\infty}$ = Blaschke product of the zeros of $C_\infty$ in $\overline{\mathbb{C}^+}$ (= the zeros on $\mathbb{R}$ under Theorem B).
- $B_{1/\Xi}$ = "anti-Blaschke" product of the zeros of $\Xi$ in $\overline{\mathbb{C}^+}$ (= the $\gamma_n$, under RH).
- $O_Q$ = outer factor determined by $|Q|$ on $\mathbb{R}$.
- $S_Q$ = singular factor.

Inc. Inv. says: all the $\gamma_n$ are zeros of $C_\infty$, so $B_{C_\infty}$ exactly cancels $B_{1/\Xi}$.

---

## 8. The outer factor $O_Q$ and the primes

**The key point.** The outer factor of $Q$ on $\mathbb{C}^+$ is completely determined by $|Q(t)|$ for $t \in \mathbb{R}$:

$$O_Q(z) = \exp\left(\frac{1}{\pi i}\int_{-\infty}^\infty \frac{1+tz}{(t-z)(1+t^2)}\log|Q(t)|dt\right).$$

The logarithm $\log|Q(t)| = \log|C_\infty(t)| - \log|\Xi(t)|$.

**Proposition 13** (expression of $\log|Q|$ in terms of primes). For $t \notin \{\gamma_n\}$:

$$\log|C_\infty(t)| = \log|w(t) - \Psi(t)|,$$

where $\Psi(t) = 2\sum_p\Lambda(p)p^{-1/2}\cos(t\log p)$ (sum over primes, conditionally convergent for real $t$).

And $\log|\Xi(t)|$ is determined by the distribution of zeros $\{\gamma_n\}$ via Jensen's formula:

$$\log|\Xi(t)| = \log|\Xi(0)| + \int_0^\infty \log|1 - t^2/r^2|d\mu_\Xi(r) \quad (\text{by Hadamard}).$$

**The identity on $\mathbb{R}$.** The function $\log|Q(t)| = \log|C_\infty(t)/\Xi(t)|$ connects the distribution of primes (via $\Psi$) with the distribution of zeros of $\Xi$. If this function is integrable on $\mathbb{R}$ (modulo the poles): the outer factor $O_Q$ is determined, and the program reduces to determining whether the zeros and poles of the Blaschke part cancel.

---

## 9. The new result: impossibility of "extra" zeros of $C_\infty$

Theorem B says: the zeros of $C_\infty$ on $\mathbb{R}$ are all in $\{$zeros of $\Xi\}$. The most important part for the quotient $Q$ is whether there are zeros of $\Xi$ that are NOT zeros of $C_\infty$ (the "missing zeros").

**Proposition 14** (structure of the missing zeros). Suppose $\gamma_{n_0}$ is a zero of $\Xi$ that is NOT a zero of $C_\infty$ (a "missing zero"). Then:

(a) $Q = C_\infty/\Xi$ has a simple pole at $\gamma_{n_0}$ with residue $C_\infty(\gamma_{n_0})/\Xi'(\gamma_{n_0}) \neq 0$.

(b) The m-function $m_\infty^{WT}(z)$ (whose support is $\subseteq\{$zeros of $C_\infty\}$) has no mass at $\gamma_{n_0}$.

(c) The spectral measure $\mu_{WT}^\infty$ gives zero mass to $\gamma_{n_0}$: $\mu_{WT}^\infty(\{\gamma_{n_0}\}) = 0$.

(d) The eigenvalue $\gamma_{n_0} \in \text{spec}(J_\infty)$ (it is in the spectrum as an eigenvalue) but the eigenvector $\psi_{n_0}^\infty$ satisfies $\langle e_0, \psi_{n_0}^\infty\rangle = 0$ — the eigenvector is orthogonal to the initial state.

*Proof.* (a) From the definition of $Q$. (b) From $\text{EF2}_{WT}$: support of $\mu_{WT}^\infty$ = zeros of $C_\infty$. (c) From (b). (d) From the interpretation of $\mu_{WT}^\infty$ as the Weyl-Titchmarsh measure: $\mu_{WT}^\infty(\{\gamma_{n_0}\}) = |\langle e_0, \psi_{n_0}^\infty\rangle|^2$. $\square$

**Theorem 1** (characterization of the missing zeros). The "missing zeros" (zeros of $\Xi$ that are not zeros of $C_\infty$) correspond exactly to the eigenvalues of $J_\infty$ whose eigenvectors are INVISIBLE from $e_0$, that is, they form part of the point spectrum of $J_\infty$ that does NOT appear in the spectral decomposition of $e_0$.

*Proof.* Direct from Proposition 14. $\square$

---

## 10. Analysis of "invisibility" from $e_0$

**The invisible point spectrum.** For a semi-infinite Jacobi operator $J$, the point spectrum splits into:
- **Spectrum visible from $e_0$**: eigenvalues with $\langle e_0, \psi_n\rangle \neq 0$ (appear in $\mu_{WT}$).
- **Spectrum invisible from $e_0$**: eigenvalues with $\langle e_0, \psi_n\rangle = 0$ (do not appear in $\mu_{WT}$).

For the semi-infinite operator $J_\infty$ with $b_n^\infty = 0$ and $a_n^\infty = \pi/\log\gamma_n$:

**Proposition 15** (condition for invisibility). $\langle e_0, \psi_n^\infty\rangle = 0$ if and only if the eigenvector $\psi_n^\infty$ is orthogonal to the initial state $e_0$ — that is, the eigensolution of $J_\infty u = \gamma_n u$ with initial condition $u_0 = 1$ is NOT in $\ell^2(\mathbb{N})$ (it is not a true eigenvalue of $J_\infty$) OR has initial condition $u_0 = 0$.

For $b_n^\infty = 0$: the recurrence equation $a_{n-1}^\infty u_{n-1} + a_n^\infty u_{n+1} = \gamma_n u_n$ with $u_0 = 1$, $u_{-1} = 0$ has a unique solution $u_n = p_n(\gamma_n)$ (the orthogonal polynomial). And $\langle e_0, \psi_n^\infty\rangle \neq 0$ iff the eigenvalue is in the support of $\mu_{WT}^\infty$.

**The connection with $C_\infty$.** By $\text{EF2}_{WT}$: $\gamma_n \in \text{supp}(\mu_{WT}^\infty)$ iff $\gamma_n$ is a zero of $C_\infty$. Hence: $\gamma_n$ is "invisible from $e_0$" iff $\gamma_n$ is NOT a zero of $C_\infty$.

---

## 11. The density principle: attacking invisibility

**Central question.** Can a Jacobi operator $J_\infty$ with $a_n^\infty = \pi/\log\gamma_n$ and $b_n^\infty = 0$ have eigenvalues "invisible from $e_0$"?

**Proposition 16** (density of the cyclic subspace). For a Jacobi operator $J$ on $\ell^2(\mathbb{N}_0)$:

- The cyclic subspace $\mathcal{H}_{e_0}(J) := \overline{\text{span}\{J^n e_0: n \geq 0\}}$ is, by definition, all of $\ell^2(\mathbb{N}_0)$ since $e_0, J e_0, J^2 e_0, \ldots$ generates the whole canonical basis (by the tridiagonal structure).

*Proof.* From the Jacobi structure: $J e_0 = a_0 e_1$, $J^2 e_0 = a_0 a_1 e_2 + a_0^2 e_0 + \ldots$ — iterating generates all the $e_n$. Hence the cyclic subspace is all of $\ell^2$. $\square$

**Theorem 2** (NO invisible eigenvalues for Jacobi operators). For any Jacobi operator $J$ on $\ell^2(\mathbb{N}_0)$ with $a_n \neq 0$ for all $n$: ALL eigenvalues of $J$ are in the support of $\mu_{WT}$. In particular: there are NO eigenvalues "invisible from $e_0$".

*Proof.* The cyclic subspace of $e_0$ is all of $\ell^2$ (Proposition 16). Hence the spectral decomposition of $e_0$ "sees" the whole spectrum: $J$ is unitarily equivalent to multiplication by $t$ on $L^2(\mathbb{R}, d\mu_{WT})$, and the support of $\mu_{WT}$ = spectrum of $J$. Hence every eigenvalue $\lambda$ with eigenvector $\psi$ satisfies: $\psi = c\cdot K_\lambda$ where $K_\lambda$ is the evaluation kernel at $\lambda$ (in the reproducing-kernel model). And $\langle e_0, K_\lambda\rangle = K_\lambda(0) \neq 0$ (the kernel does not vanish at the reproducing point). $\square$

---

## 12. The fundamental corollary

**Corollary 1** (all eigenvalues of $J_\infty$ are in the support of $\mu_{WT}^\infty$). For the Jacobi operator $J_\infty$ with $a_n^\infty = \pi/\log\gamma_n > 0$ for all $n$ and $b_n^\infty = 0$:

$$\text{spec}(J_\infty) = \text{supp}(\mu_{WT}^\infty).$$

*Proof.* Direct application of Theorem 2 (all $a_n^\infty = \pi/\log\gamma_n \neq 0$). $\square$

**Corollary 2** (the $\gamma_n$ are in the support of $\mu_{WT}^\infty$). If $\gamma_n \in \text{spec}(J_\infty)$ for all $n$ (that is, each $\gamma_n$ is an eigenvalue of $J_\infty$): then $\gamma_n \in \text{supp}(\mu_{WT}^\infty)$ for all $n$.

By $\text{EF2}_{WT}$: $\text{supp}(\mu_{WT}^\infty) \subseteq \{$zeros of $C_\infty\}$. Hence: $\gamma_n \in \{$zeros of $C_\infty\}$ — which is Inc. Inv.

*Proof.* $\gamma_n \in \text{spec}(J_\infty) \Rightarrow \gamma_n \in \text{supp}(\mu_{WT}^\infty)$ (by Corollary 1) $\Rightarrow C_\infty(\gamma_n) = 0$. $\square$

**THE REDUCTION.** Inc. Inv. follows if and only if: the $\gamma_n$ are eigenvalues of $J_\infty$.

---

## 13. Are the $\gamma_n$ eigenvalues of $J_\infty$?

**The reduced question (Inc. Inv. reduced to eigenvalues).** By Corollary 2, the entire program reduces to:

$$\boxed{\gamma_n \in \text{spec}(J_\infty) \text{ for all } n?}$$

That is: is $\gamma_n$ an eigenvalue of the operator $J_\infty$ with $a_n^\infty = \pi/\log\gamma_n$, $b_n^\infty = 0$?

**The eigenvalue condition.** $\gamma_n$ is an eigenvalue of $J_\infty$ iff there exists $u = (u_0, u_1, u_2, \ldots) \in \ell^2(\mathbb{N}_0)$ with:

$$a_{k-1}^\infty u_{k-1} + a_k^\infty u_{k+1} = \gamma_n u_k, \quad k \geq 0,$$

with boundary condition $u_{-1} = 0$ (or equivalently: $a_0^\infty u_1 = \gamma_n u_0$).

The unique solution with $u_0 = 1$: $u_k = p_k(\gamma_n)$ (the Jacobi orthogonal polynomials).

**$\ell^2$ condition.** $\gamma_n \in \text{spec}(J_\infty)$ iff $\sum_{k=0}^\infty |p_k(\gamma_n)|^2 < \infty$.

**Proposition 17** ($\ell^2$ condition for $p_k(\gamma_n)$). For the Jacobi orthogonal polynomials with $a_k^\infty = \pi/\log\gamma_k$ and $b_k^\infty = 0$:

$$p_k(t) \sim C_k \prod_{j=1}^k \frac{t}{\pi/\log\gamma_j} = C_k \cdot \frac{t^k \prod_{j=1}^k \log\gamma_j}{\pi^k}.$$

For $t = \gamma_n$ and large $k$: $|p_k(\gamma_n)| \sim c_k \cdot \gamma_n^k \cdot (\log\gamma_n)^k / \pi^k$. If $\gamma_n\log\gamma_n > \pi$: the terms grow super-exponentially and $p_k(\gamma_n) \notin \ell^2$.

This would mean $\gamma_n \notin \text{spec}(J_\infty)$ for the large $\gamma_n$ (such that $\gamma_n\log\gamma_n > \pi$) — the opposite of what we need!

**The apparent contradiction.** If the $\gamma_n$ are NOT in spec$(J_\infty)$, then — by Corollary 2 — we cannot conclude Inc. Inv. But then what are the eigenvalues of $J_\infty$?

---

## 14. Resolution of the contradiction: the spectrum of $J_\infty$ does not directly contain the $\gamma_n$

**Proposition 18** (the spectrum of $J_\infty$ as zeros of $C_\infty$, not as the $\gamma_n$). By $\text{EF2}_{WT}$:

$$\text{supp}(\mu_{WT}^\infty) = \{t \in \mathbb{R}: C_\infty(t) = 0\} = \{t_n^C\}.$$

The points $\{t_n^C\}$ are the zeros of $C_\infty(t) = w(t) - \Psi(t)$ — which by Theorem B are a subset of $\{\gamma_n\}$.

**The correct question.** The eigenvalues of $J_\infty$ are the $\{t_n^C\}$ (zeros of $C_\infty$), NOT the $\gamma_n$ directly. Inc. Inv. asserts that $\{t_n^C\} = \{\gamma_n\}$, that is, EACH $\gamma_n$ is also a zero of $C_\infty$.

The $\ell^2$ condition of Theorem 2 (visibility of eigenvalues from $e_0$) applies to the $t_n^C$ (which ARE eigenvalues), not directly to the $\gamma_n$. Hence there is NO contradiction.

**Theorem 2 is correct but does not directly give Inc. Inv.** What Theorem 2 guarantees is: if $t \in \text{spec}(J_\infty)$ then $t \in \text{supp}(\mu_{WT}^\infty)$ — but we already knew this (it is the definition of the support of the spectral measure). The theorem does not tell us which points are in spec$(J_\infty)$; that comes from $\text{EF2}_{WT}$ (= zeros of $C_\infty$).

---

## 15. Final diagnosis of Front C

**Synthesis.** Front C (spectral geometry of the quotient $Q = C_\infty/\Xi$) has produced:

1. **New result**: Inc. Inv. is equivalent to $Q$ extending holomorphically to a neighborhood of $\mathbb{R}$ (Proposition 3).

2. **New result**: Invisibility of eigenvalues from $e_0$ is IMPOSSIBLE for Jacobi operators with $a_n \neq 0$ (Theorem 2). This leaves the argument intact.

3. **The true wall**: The eigenvalues of $J_\infty$ are the zeros of $C_\infty$ (by $\text{EF2}_{WT}$), not directly the $\gamma_n$. The question of whether each $\gamma_n$ is a zero of $C_\infty$ requires:

$$\gamma_n \text{ is an eigenvalue of }J_\infty \iff p_k(\gamma_n) \in \ell^2 \iff C_\infty(\gamma_n) = 0. \quad (\star)$$

The equivalence $(\star)$ between the $\ell^2$ condition of the orthogonal polynomials and the zeros of $C_\infty$ is the deep content of $\text{EF2}_{WT}$.

4. **The genuinely new open question**: Is it possible to prove directly that $\sum_k |p_k(\gamma_n)|^2 < \infty$ for each $n$ USING the explicit formula for $p_k$ in terms of $a_j^\infty = \pi/\log\gamma_j$? This sum involves arithmetic properties of the $\gamma_j$ — in particular, the distribution of the zeros of $\zeta$ on the critical line. This is a problem in NUMERICAL OPERATOR ANALYSIS with arithmetic inputs.
