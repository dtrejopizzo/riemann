# Phase 29 — Doc 32: Direction B — Zero Counting of $C_\infty$ and the Reverse Inclusion

**Direction:** B (direct computation via EF2-emp)
**Objective:** Prove that $N_{C_\infty}(T) = N_\Xi(T)$ via the EF2-emp identity and the argument principle. If the equality of counts is established, and given that $\{C_\infty=0\} \subseteq \{\Xi=0\}$ (Theorem 2, Doc 19), one concludes Inc. Inv. $\Leftrightarrow$ RH.

---

## 1. The bridge: from eigenvalues to the zeros of $C_\infty$

**Reminder (Theorem C1, Doc 17).** The Weyl-Titchmarsh function $m_\infty^{WT}(z)$ of the limit operator $J_\infty$ satisfies the Möbius equation:

$$m_\infty^{WT}(z) = \cfrac{1}{b_0 - z - a_0^2 m_\infty^{(1)}(z)},$$

where $m_\infty^{(n)}$ is the WT function of the operator truncated at $n$. From the analysis of Doc 17: the poles of $m_\infty^{WT}$ on $\mathbb{R}$ are exactly the real zeros of $C_\infty$. As a proposition:

**Proposition 1** (eigenvalues = zeros of $C_\infty$). For all $t_0 \in \mathbb{R}$:

$$t_0 \in \mathrm{spec}(J_\infty) \iff C_\infty(t_0) = 0.$$

*Proof.* $t_0$ is an eigenvalue of $J_\infty$ iff $\mu_\infty^{WT}(\{t_0\}) > 0$ iff $m_\infty^{WT}$ has a pole at $t_0$. By EF2-WT (Doc 17, Theorem C1), the poles of $m_\infty^{WT}$ are the zeros of $C_\infty$. $\square$

**Corollary 1** (direct inclusion, Theorem 2 of Doc 19). Given that $m_\infty^{emp}(z) \to \mu_\gamma^{real}$ (Doc 15) and $\mu_\gamma^{real}$ has support $\{\gamma_n\}$, and $\mathrm{spec}(J_\infty) \subseteq \mathrm{supp}(\mu_\gamma^{real})$:

$$\{C_\infty = 0 \text{ on } \mathbb{R}\} \subseteq \{\Xi = 0 \text{ on } \mathbb{R}\} = \{\gamma_n\}.$$

This is the DIRECT inclusion — unconditional.

---

## 2. The reverse inclusion as equality of counts

**Definition.** Let:

$$N_{C_\infty}(T) := \#\{t \in [0,T] : C_\infty(t) = 0\}, \quad N_\Xi(T) := \#\{t \in [0,T] : \Xi(t) = 0\}.$$

**Proposition 2** (Inc. Inv. $\Leftrightarrow$ equality of counts). From the direct inclusion (Corollary 1):

$$N_{C_\infty}(T) \leq N_\Xi(T) \quad \text{for all } T > 0.$$

The reverse inclusion (Inc. Inv.) is equivalent to:

$$N_{C_\infty}(T) \geq N_\Xi(T) \quad \text{for all sufficiently large } T > 0.$$

*Proof.* $\{C_\infty=0\} \subseteq \{\Xi=0\}$ with equality $\iff$ each $\gamma_n \leq T$ is a zero of $C_\infty$. Equality of counts is equivalent to equality of sets (since the inclusion already gives $\leq$). $\square$

**Corollary 2** (RH from the count). Combining with Theorem 3 (Doc 19):

$$N_{C_\infty}(T) = N_\Xi(T) \text{ for all } T \gg 1 \iff \text{RH}.$$

---

## 3. The argument principle applied to $C_\infty$

**Setup.** Let $R_T^\eta$ be the rectangle with vertices $0, T, T+i\eta, i\eta$ (oriented counterclockwise), where $0 < \eta < 1/2$ (within the strip of analyticity of $C_\infty$, Proposition 1 of Doc 19).

**Proposition 3** (argument principle for $C_\infty$). For $T$ not a zero of $C_\infty$ and $\eta \in (0,1/2)$:

$$N_{C_\infty}(T) = \frac{1}{2\pi i}\oint_{R_T^\eta} \frac{C_\infty'(z)}{C_\infty(z)}\, dz + E(T,\eta),$$

where $E(T,\eta) = O(1)$ is the boundary error from the vertical sides and the top side.

*Proof.* The standard argument formula. The zeros of $C_\infty$ inside $R_T^\eta$ are exactly the real zeros in $[0,T]$ (since $C_\infty$ has no non-real zeros in the strip, by $\{C_\infty=0\} \subseteq \{\Xi=0\}$ and the zeros of $\Xi$ in the strip $|\Im z| < 1/2$ correspond to zeros of $\zeta$ off the critical line, plus the real zeros). $\square$

---

## 4. EF2-emp as a bridge to $N_\Xi$

**The fundamental identity (EF2-emp, Doc 27 Corollary 1).** For $z \in \mathbb{C}^+$:

$$\frac{C_\infty'(z)}{C_\infty(z)} = N \cdot m_\infty^{emp}(z) + \frac{\Xi'(z)}{\Xi(z)}.$$

Integrating over $R_T^\eta$ (counterclockwise):

$$\frac{1}{2\pi i}\oint_{R_T^\eta} \frac{C_\infty'}{C_\infty}\,dz = N \cdot \frac{1}{2\pi i}\oint_{R_T^\eta} m_\infty^{emp}(z)\,dz + \frac{1}{2\pi i}\oint_{R_T^\eta} \frac{\Xi'}{\Xi}\,dz.$$

The third term (argument principle for $\Xi$):

$$\frac{1}{2\pi i}\oint_{R_T^\eta} \frac{\Xi'}{\Xi}\,dz = N_\Xi(T) + E_\Xi(T,\eta),$$

where $E_\Xi = O(1)$ is the boundary error.

**Hence:**

$$N_{C_\infty}(T) = N \cdot \mathcal{I}(T,\eta) + N_\Xi(T) + O(1),$$

where

$$\mathcal{I}(T,\eta) := \frac{1}{2\pi i}\oint_{R_T^\eta} m_\infty^{emp}(z)\,dz.$$

---

## 5. Computing $\mathcal{I}(T,\eta)$

**Proposition 4** (computation of $\mathcal{I}$ via the residue theorem). The function $m_\infty^{emp}$ is the Stieltjes transform of $\mu_\gamma^{real}$:

$$m_\infty^{emp}(z) = \int_\mathbb{R} \frac{d\mu_\gamma^{real}(t)}{z-t} = \frac{1}{N}\sum_{n:\, \gamma_n > 0} \frac{1}{z-\gamma_n}$$

(assuming the normalization $\mu_\gamma^{real} = (1/N)\sum_{n=1}^N \delta_{\gamma_n}$ with $N$ the number of zeros in $[0,T]$, in a regularized limit).

By the residue theorem (contour $R_T^\eta$ enclosing the poles of $m_\infty^{emp}$, which are the $\gamma_n \in [0,T]$):

$$\mathcal{I}(T,\eta) = \frac{1}{2\pi i}\oint_{R_T^\eta} \frac{1}{N}\sum_n \frac{1}{z-\gamma_n}\,dz = \frac{1}{N}\sum_{n:\, \gamma_n \in [0,T]} 1 = \frac{N_\Xi(T)}{N}.$$

**Corollary 3** (the fundamental counting equation). Substituting:

$$\boxed{N_{C_\infty}(T) = N \cdot \frac{N_\Xi(T)}{N} + N_\Xi(T) + O(1) = 2 N_\Xi(T) + O(1).}$$

---

## 6. The apparent contradiction and its resolution

**The fundamental counting equation says:** $N_{C_\infty}(T) = 2N_\Xi(T) + O(1)$.

But the direct inclusion (Corollary 1) requires $N_{C_\infty}(T) \leq N_\Xi(T)$. Having $N_{C_\infty}(T) = 2N_\Xi(T)$ contradicts $N_{C_\infty}(T) \leq N_\Xi(T)$ as $N_\Xi(T) \to \infty$.

**Diagnosis.** The contradiction indicates that the computation of $\mathcal{I}$ is incorrect, or that EF2-emp cannot be used in this way. We identify three sources of error:

**Error A (normalization of $N$).** The factor $N$ in EF2-emp is the renormalization factor of the truncated operator $J_\lambda^N$, and $N \to \infty$ as $\lambda \to \infty$. The computation of $\mathcal{I} = N_\Xi(T)/N$ uses the same $N$, but in the product $N \cdot \mathcal{I} = N_\Xi(T)$, the factors of $N$ cancel — this is consistent.

What happens: $N \cdot m_\infty^{emp}(z) \to \infty$ pointwise (for each fixed $z$), but the contour integral of $N \cdot m_\infty^{emp}$ over $R_T^\eta$ gives $N_\Xi(T)$ (which also grows). The ratios are finite.

**Error B (convergence of EF2-emp in the limit).** EF2-emp is an identity for the FINITE operator $J_\lambda^N$. In the limit $N \to \infty$: EF2 scales as $N \to \infty$, and the logarithmic derivative $C_\infty'/C_\infty$ also scales. The fundamental counting equation is:

$$N_{C_\infty}(T) = 2N_\Xi(T) + O(1)$$

and is CONSISTENT if $C_\infty$ has (approximately) $2N_\Xi(T)$ zeros — but this would contradict $\{C_\infty=0\} \subseteq \{\Xi=0\}$.

**The correct resolution.** EF2-emp in the limit $N\to\infty$ gives:

$$m_\infty^{emp}(z) = \frac{1}{N}\frac{C_\infty'(z)}{C_\infty(z)} - \frac{1}{N}\frac{\Xi'(z)}{\Xi(z)},$$

with the factor $1/N$ in BOTH terms (Doc 27, §7). The contour integral:

$$\frac{1}{2\pi i}\oint \frac{C_\infty'}{C_\infty}\,dz = N_\Xi(T) + N \cdot \frac{1}{2\pi i}\oint m_\infty^{emp}\,dz$$

$$= N_\Xi(T) + N \cdot \frac{N_\Xi(T)}{N} = 2N_\Xi(T).$$

This gives $N_{C_\infty}(T) = 2N_\Xi(T)$, which CONTRADICTS Theorem 2 of Doc 19.

---

## 7. The correct diagnosis: EF2-emp cannot coexist with Theorem B

**Theorem 1** (counting obstruction). The following three statements are INCOMPATIBLE:

(i) EF2-emp: $N \cdot m_\infty^{emp}(z) = C_\infty'(z)/C_\infty(z) - \Xi'(z)/\Xi(z)$ with $m_\infty^{emp}$ = Stieltjes transform of $\mu_\gamma^{real}$.

(ii) $\{C_\infty=0 \text{ on } \mathbb{R}\} \subseteq \{\Xi=0 \text{ on } \mathbb{R}\}$ (Theorem B).

(iii) $N_{C_\infty}(T) > 0$ for large $T$.

*Proof.* (i) $\Rightarrow$ $N_{C_\infty}(T) = 2N_\Xi(T) + O(1)$. But (ii) $\Rightarrow$ $N_{C_\infty}(T) \leq N_\Xi(T)$. Together: $2N_\Xi(T) + O(1) \leq N_\Xi(T)$, that is, $N_\Xi(T) = O(1)$ — contradicts (iii). $\square$

**Corollary 4.** At least one of the three statements is false or needs correction. As (ii) and (iii) are well established, the failure lies in (i): EF2-emp, as formulated in Doc 27, has an inconsistency.

---

## 8. The correct reinterpretation of EF2-emp

**The $N$-factor problem.** The finite EF2 for $J_\lambda^N$ is:

$$N \cdot m_\lambda^{emp}(z) = \frac{C_\lambda'(z)}{C_\lambda(z) - \mu_\lambda} - \frac{\hat k_\lambda'(z)}{\hat k_\lambda(z)}.$$

This is an identity for the finite truncation. In the limit:

- The left-hand side: $N \cdot m_\lambda^{emp}(z) \to N \cdot m_\infty^{emp}(z)$ where $m_\infty^{emp}$ is the Stieltjes transform of $\mu_\gamma^{real} = (1/N)\sum_n \delta_{\gamma_n}$, so $N \cdot m_\infty^{emp}(z) = \sum_n 1/(z-\gamma_n)$.

- The right-hand side: $C_\lambda'/C_\lambda \to C_\infty'/C_\infty$ and $\hat k_\lambda'/\hat k_\lambda \to \Xi'/\Xi$.

So EF2-emp IN THE LIMIT is:

$$\sum_n \frac{1}{z-\gamma_n} = \frac{C_\infty'(z)}{C_\infty(z)} - \frac{\Xi'(z)}{\Xi(z)}.$$

**The explicit-formula identity.** The left-hand side $\sum_n 1/(z-\gamma_n)$ is precisely the "critical-line part" of the logarithmic derivative of $\Xi$:

$$\frac{\Xi'(z)}{\Xi(z)} = \sum_{\gamma: \text{ all zeros}} \frac{1}{z-\gamma} = \sum_{\gamma_n \in \mathbb{R}} \frac{1}{z-\gamma_n} + \sum_{\gamma \notin \mathbb{R}} \frac{1}{z-\gamma}.$$

Under RH: all zeros of $\Xi$ are real, so $\Xi'/\Xi = \sum_n 1/(z-\gamma_n)$.

**Proposition 5** (EF2-emp collapses under RH). Under RH: $\sum_n 1/(z-\gamma_n) = \Xi'/\Xi$. EF2-emp gives:

$$\frac{\Xi'(z)}{\Xi(z)} = \frac{C_\infty'(z)}{C_\infty(z)} - \frac{\Xi'(z)}{\Xi(z)},$$

that is, $C_\infty'(z)/C_\infty(z) = 2\Xi'(z)/\Xi(z)$, which implies $C_\infty(z) = K \cdot \Xi(z)^2$ for some constant $K \neq 0$.

**But** $\{C_\infty=0\} = \{\Xi=0\}$ (under RH = Inc. Inv.) would be consistent with $C_\infty = K\Xi^2$ (the zeros of $C_\infty$ would be double zeros where $\Xi$ has simple zeros).

**Final inconsistency.** If $C_\infty = K\Xi^2$ in the strip: then the zeros of $C_\infty$ would be the same as those of $\Xi$ but with DOUBLE multiplicity. The direct inclusion $\{C_\infty=0\} \subseteq \{\Xi=0\}$ would still hold, but the COUNTS would be: $N_{C_\infty}(T) = N_\Xi(T)$ (same zeros, double multiplicity in $C_\infty$ simply counted once each). This gives $N_{C_\infty}(T) = N_\Xi(T)$, consistent with Inc. Inv.

But the identity $C_\infty = K\Xi^2$ is NOT compatible with the explicit definition of $C_\infty$ via the Weil formula — unless $K = 0$, which would make $C_\infty \equiv 0$.

---

## 9. Candid conclusion of Direction B

**Net result.** Direction B reveals an internal INCONSISTENCY in EF2-emp as applied to the zero-counting question. The fundamental counting equation $N_{C_\infty}(T) = 2N_\Xi(T) + O(1)$ is incompatible with Theorem B.

**Precise diagnosis.** The error lies in taking the limit $N\to\infty$ in EF2-emp. The identity is valid for the finite operator, but in the limit the two functions $m_\lambda^{emp}$ and $\mu_\gamma^{real}$ have a more delicate relationship (the measure $\mu_\gamma^{real}$ already counts the zeros of $\Xi$ and cannot be the limiting spectral measure of $m^{emp}$ without corrections).

**Lesson from Direction B.** The path from EF2-emp to zero counting is not direct. EF2-emp relates $C_\infty'/C_\infty$ to $\Xi'/\Xi$ and $m^{emp}$, but the triple relation contains circularity when the limit is taken.

**What it does contribute.** Direction B clarifies that EF2-emp, the direct inclusion, and the normalization $N$ are three pieces that must be reconciled carefully. The inconsistency of the direct computation of $N_{C_\infty}$ via EF2-emp is a candid result: it signals that Inc. Inv. cannot be obtained trivially from EF2-emp without additional information.

**Referral to Direction A.** The question of whether $C_\infty(z) = K\Xi(z)^2$ or a richer relation holds will be addressed in Doc 33 via the explicit formula and the fixed-point structure.

---

*Next doc: Doc 33 — Direction A: The Explicit Formula as a Fixed-Point Equation.*
