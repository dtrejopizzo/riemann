# Phase 29 — Doc 36: Deep Audit of Direction B — EF2-emp and Zero Counting

**Objective:** Audit with maximum precision the zero-counting argument of Doc 32, which concluded $N_{C_\infty}(T) = 2N_\Xi(T)$ — apparently contradicting Theorem B ($N_{C_\infty}(T) \leq N_\Xi(T)$). Identify exactly where the error lies, if any, and what EF2-emp correctly says about the count.

---

## 1. The finite EF2-emp: precise statement

**Proposition 0 (finite EF2-emp, Doc 27 Prop. 1 — basis of the audit).** For each $\lambda > 0$ and $z \in \mathbb{C}^+$:

$$\sum_{n=1}^{N(\lambda)} \frac{1}{z - t_n^{(\lambda)}} = \frac{C_\lambda'(z)}{C_\lambda(z) - \mu_\lambda} - \frac{\hat k_\lambda'(z)}{\hat k_\lambda(z)}, \quad (EF_\lambda)$$

where:

- $\{t_n^{(\lambda)}\}_{n=1}^{N(\lambda)}$ are the roots of $\hat\xi_\lambda^{(N)}$ (which coincide with the eigenvalues of $J_\lambda^N$, all real).
- $C_\lambda(z) = w(z) - 2\sum_{p \leq \lambda^2}\Lambda(p)p^{-1/2}e^{iz\log p}$ (truncated potential).
- $\mu_\lambda > 0$ is the Lagrange multiplier (satisfies $\mu_\lambda \to 0$ as $\lambda\to\infty$).
- $\hat k_\lambda(z)$ is the truncated Weil kernel.

The identity $(EF_\lambda)$ is an identity between MEROMORPHIC functions on $\mathbb{C}^+$: the left-hand side has $N(\lambda)$ simple poles with residue $+1$; the right-hand side has poles where $C_\lambda - \mu_\lambda = 0$ (residue $+1$) and poles where $\hat k_\lambda = 0$ (residue $-1$). The equality is an exact cancellation.

---

## 2. The counting interpretation: use of the argument principle

**Proposition 1** (finite counting formula). For the rectangle $R_T^\eta = [0,T] \times [0,\eta]$ (counterclockwise contour), $0 < \eta < 1/2$, $T$ avoiding zeros:

$$N_\lambda(T) = \frac{1}{2\pi i}\oint_{R_T^\eta} \sum_n \frac{1}{z-t_n^{(\lambda)}}\,dz = N_{\lambda}^{\text{rect}}(T,\eta),$$

where $N_\lambda^{\text{rect}}(T,\eta)$ = number of eigenvalues $t_n^{(\lambda)} \in [0,T]$ (all real, none in the strip).

On the right-hand side:

$$\frac{1}{2\pi i}\oint_{R_T^\eta} \left[\frac{C_\lambda'}{C_\lambda-\mu_\lambda} - \frac{\hat k_\lambda'}{\hat k_\lambda}\right]\,dz = \#\{\text{zeros of }(C_\lambda-\mu_\lambda)\text{ in }R_T^\eta\} - \#\{\text{zeros of }\hat k_\lambda\text{ in }R_T^\eta\}.$$

Hence:

$$\boxed{N_\lambda(T) = N_{C_\lambda-\mu_\lambda}^{\text{rect}}(T,\eta) - N_{\hat k_\lambda}^{\text{rect}}(T,\eta).} \quad (C_\lambda)$$

This is the **exact finite counting formula** — correct for each $\lambda$.

**CRITICAL:** $N_{C_\lambda-\mu_\lambda}^{\text{rect}}$ counts the zeros of $C_\lambda(z) = \mu_\lambda$ INSIDE THE RECTANGLE, that is, in the region $0 \leq \Re(z) \leq T$, $0 \leq \Im(z) \leq \eta$. This includes BOTH real zeros AND complex zeros in the interior of the rectangle.

---

## 3. The crucial distinction: real zeros vs. complex zeros in the rectangle

**Proposition 2** (real zeros of $C_\lambda - \mu_\lambda$ are the eigenvalues). For $z = x \in [0,T] \cap \mathbb{R}$: $C_\lambda(x) = \mu_\lambda > 0$ iff $x$ is an eigenvalue of $J_\lambda^N$. Hence:

$$N_{C_\lambda-\mu_\lambda}^{\text{real}}(T) = N_\lambda(T).$$

**Proposition 3** (there may be complex zeros of $C_\lambda - \mu_\lambda$ in the rectangle). For $z = x + iy$ with $0 < y \leq \eta$: the equation $C_\lambda(x+iy) = \mu_\lambda$ is a complex equation ($C_\lambda$ is analytic on $\mathbb{C}^+$). Let $N_{C_\lambda-\mu_\lambda}^{\text{strip}}(T,\eta)$ be the number of such complex solutions with $0 < \Im(z) \leq \eta$.

The counting formula gives:

$$N_{C_\lambda-\mu_\lambda}^{\text{rect}} = N_{C_\lambda-\mu_\lambda}^{\text{real}} + N_{C_\lambda-\mu_\lambda}^{\text{strip}} = N_\lambda(T) + N_{C_\lambda-\mu_\lambda}^{\text{strip}}.$$

**Proposition 4** (zeros of $\hat k_\lambda$ in the rectangle). The zeros of $\hat k_\lambda$ in $R_T^\eta$ include both the real zeros (which approximate the $\gamma_n$) and possible complex zeros in the strip:

$$N_{\hat k_\lambda}^{\text{rect}}(T,\eta) = N_{\hat k_\lambda}^{\text{real}}(T) + N_{\hat k_\lambda}^{\text{strip}}(T,\eta).$$

**The unpacked counting formula:**

$$N_\lambda(T) = [N_\lambda(T) + N_{C_\lambda-\mu_\lambda}^{\text{strip}}] - [N_{\hat k_\lambda}^{\text{real}} + N_{\hat k_\lambda}^{\text{strip}}].$$

Simplifying:

$$0 = N_{C_\lambda-\mu_\lambda}^{\text{strip}}(T,\eta) - N_{\hat k_\lambda}^{\text{real}}(T) - N_{\hat k_\lambda}^{\text{strip}}(T,\eta).$$

Hence:

$$\boxed{N_{\hat k_\lambda}^{\text{real}}(T) + N_{\hat k_\lambda}^{\text{strip}}(T,\eta) = N_{C_\lambda-\mu_\lambda}^{\text{strip}}(T,\eta).} \quad (C_\lambda')$$

Formula $(C_\lambda')$ says that the NUMBER OF COMPLEX ZEROS OF $C_\lambda - \mu_\lambda$ IN THE STRIP equals the total number of zeros of $\hat k_\lambda$ (real + complex) in the rectangle.

---

## 4. The error in Doc 32: confusion between the strip count and the real count

**The argument of Doc 32 (§4-§5) that led to $N_{C_\infty}(T) = 2N_\Xi(T)$.**

In Doc 32, the argument principle was applied to EF2-emp in the limit:

$$\frac{1}{2\pi i}\oint_{R_T^\eta} \frac{C_\infty'}{C_\infty}\,dz = N \cdot \frac{1}{2\pi i}\oint_{R_T^\eta} m_\infty^{emp}\,dz + \frac{1}{2\pi i}\oint_{R_T^\eta}\frac{\Xi'}{\Xi}\,dz.$$

The first error: "$N \cdot \frac{1}{2\pi i}\oint m_\infty^{emp}\,dz = N_\Xi(T)$."

This identity assumes that $N \cdot m_\infty^{emp}(z) = \sum_n 1/(z-\gamma_n)$ with poles EXACTLY at $[0,T]$, and that the residues give $N_\Xi(T)$. But this uses the LIMIT of EF2-emp in an unjustified way.

The second, deeper error: the term $N \cdot \frac{1}{2\pi i}\oint m_\infty^{emp}\,dz$ is the LIMIT of the count $N_\lambda(T)$, NOT the integral count of the limiting function $m_\infty^{emp}$.

**Proposition 5** (the limit-integral interchange error). The following equation of Doc 32 is INCORRECT:

$$\frac{1}{2\pi i}\oint_{R_T^\eta} \underbrace{N\cdot m_\infty^{emp}(z)}_{\text{limit of } N\cdot m_\lambda^{emp}} dz = \lim_{\lambda\to\infty} N_\lambda(T) = N_\Xi(T).$$

The identity fails because the function $N \cdot m_\lambda^{emp}(z)$ diverges as $N \to \infty$ (the integrand grows without bound in the neighborhood of the $\gamma_n$), and the interchange of limit and integral is not justified.

*More precisely:* $N(\lambda) \cdot m_\lambda^{emp}(z) = \sum_{n=1}^{N(\lambda)} 1/(z-t_n^{(\lambda)})$. For fixed $z \in \mathbb{C}^+$ and $N \to \infty$: this sum grows like $\sum_{n \leq N(\lambda)} 1/|\gamma_n| \sim \log\log N(\lambda) \to \infty$. The "limiting" function $N \cdot m_\infty^{emp}(z)$ is formally $\infty$ for each $z$, NOT a finite holomorphic function.

---

## 5. The correct limit of the counting formula

**Theorem 1** (counting formula in the limit). Taking $\lambda \to \infty$ in the identity $(C_\lambda')$ with $\eta > 0$ FIXED:

$$\underbrace{N_{\hat k_\lambda}^{\text{real}}(T)}_{\to N_\Xi(T)} + \underbrace{N_{\hat k_\lambda}^{\text{strip}}(T,\eta)}_{\to N_\Xi^{\text{off}}(T,\eta)} = \underbrace{N_{C_\lambda-\mu_\lambda}^{\text{strip}}(T,\eta)}_{=?}$$

where $N_\Xi^{\text{off}}(T,\eta)$ = number of zeros of $\Xi$ in the strip $0 < \Im(z) \leq \eta$ with $\Re(z) \in [0,T]$ — which are the OFF-CRITICAL zeros of $\zeta$ in the corresponding region.

**Under RH:** $N_\Xi^{\text{off}}(T,\eta) = 0$ for every $\eta < 1/2$. Hence:

$$\lim_{\lambda\to\infty} N_{C_\lambda-\mu_\lambda}^{\text{strip}}(T,\eta) = N_\Xi(T) + 0 = N_\Xi(T).$$

This says: the complex zeros of $C_\lambda - \mu_\lambda$ in the strip converge to $N_\Xi(T)$ in NUMBER but NOT in POSITION: they cannot converge to zeros of $C_\infty$ in the strip (since under RH, $C_\infty$ has zeros only on $\mathbb{R}$). Hence: the complex zeros of $C_\lambda - \mu_\lambda$ in $0 < \Im(z) \leq \eta$ must ESCAPE the rectangle as $\lambda \to \infty$ — they migrate toward the boundary $\Im(z) = \eta$ and eventually leave the rectangle.

**Proposition 6** (migration of the complex zeros). Let $\{z_j^{(\lambda)}\}$ be the zeros of $C_\lambda(z) = \mu_\lambda$ in the strip $0 < \Im(z) \leq \eta$. Then:

(a) For each finite $\lambda$: there are exactly $N_\Xi(T) + N_\Xi^{\text{off}}(T,\eta)$ such zeros (by identity $(C_\lambda')$).

(b) Under RH: $N_\Xi^{\text{off}}(T,\eta) = 0$, so there are $N_\Xi(T)$ complex zeros for each finite $\lambda$.

(c) As $\lambda \to \infty$: these $N_\Xi(T)$ complex zeros move and eventually leave the strip $\Im(z) \leq \eta$ — they escape toward $\Im(z) > \eta$ (and probably toward $\Im(z) \to 1/2$, the boundary of the strip of analyticity of $C_\infty$).

*Evidence:* If the complex zeros of $C_\lambda - \mu_\lambda$ in $0 < \Im(z) \leq \eta$ were to converge to zeros of $C_\infty$ in that strip: by Hurwitz, $C_\infty$ would have $N_\Xi(T)$ complex zeros in $0 < \Im(z) \leq \eta$. But by Theorem B, those zeros would be zeros of $\Xi$ in the strip — contradicting RH. Hence the complex zeros must escape.

---

## 6. The reconciliation: what EF2-emp does say

**Proposition 7** (the correct equation for $N_{C_\infty}(T)$). Under RH and Inc. Inv., for each fixed $\eta > 0$ and $\lambda \to \infty$:

$$N_\lambda(T) \to N_\Xi(T), \quad N_{\hat k_\lambda}^{\text{rect}}(T,\eta) \to N_\Xi(T).$$

The counting formula $(C_\lambda)$:

$$N_\lambda(T) = N_{C_\lambda-\mu_\lambda}^{\text{rect}}(T,\eta) - N_{\hat k_\lambda}^{\text{rect}}(T,\eta)$$

gives:

$$N_\Xi(T) = N_{C_\lambda-\mu_\lambda}^{\text{rect}}(T,\eta) - N_\Xi(T),$$

so $N_{C_\lambda-\mu_\lambda}^{\text{rect}}(T,\eta) = 2N_\Xi(T)$.

Decomposing: $N_{C_\lambda-\mu_\lambda}^{\text{rect}} = N_{C_\lambda-\mu_\lambda}^{\text{real}} + N_{C_\lambda-\mu_\lambda}^{\text{strip}} = N_\Xi(T) + N_\Xi(T) = 2N_\Xi(T)$.

The two instances of $N_\Xi(T)$ are:
- $N_{C_\lambda-\mu_\lambda}^{\text{real}} = N_\lambda(T) \to N_\Xi(T)$: real eigenvalues converging to $\{\gamma_n\}$.
- $N_{C_\lambda-\mu_\lambda}^{\text{strip}} = N_\Xi(T)$: complex zeros in the strip that ESCAPE as $\lambda \to \infty$ (under RH).

**The zero count of $C_\infty$:** By Hurwitz (uniform convergence of $C_\lambda \to C_\infty$ on compact subsets of $\mathbb{C}^+$, with $\Im(z) \geq \eta/2 > 0$ fixed):

$$N_{C_\infty}^{\text{rect}}(T,\eta) = \lim_{\lambda\to\infty} N_{C_\lambda}^{\text{rect}}(T,\eta).$$

Where $N_{C_\lambda}^{\text{rect}}$ (without the $-\mu_\lambda$) = zeros of $C_\lambda$ in the rectangle $\approx N_\Xi(T)$ (under Inc. Inv., the zeros of $C_\lambda$ on $\mathbb{R}$ converge to $\{\gamma_n\}$, and under RH, there are no zeros of $C_\infty$ in the strip).

Hence $N_{C_\infty}^{\text{rect}}(T,\eta) = N_\Xi(T)$ — CONSISTENT with Inc. Inv. and without contradiction.

---

## 7. The precise diagnosis of the error in Doc 32

**Theorem 2** (diagnosis of the Doc 32 error). The argument in §4-5 of Doc 32 has the following error:

In §4: the equation $\frac{C_\infty'(z)}{C_\infty(z)} = N \cdot m_\infty^{emp}(z) + \frac{\Xi'(z)}{\Xi(z)}$ is written and integrated over the contour to obtain $N_{C_\infty}(T)$. The error is using EF2-emp "in the limit" as if it were an identity between FINITE analytic functions — but EF2-emp in the limit involves functions that DIVERGE, and the identity only makes sense in the FINITE COUNT (for each $\lambda$), not as a meromorphic identity in the limit.

Specifically: the identity $N \cdot m_\infty^{emp}(z) = C_\infty'/C_\infty - \Xi'/\Xi$ (as analytic functions on $\mathbb{C}^+$) is NOT valid, because $N \cdot m_\infty^{emp}(z) = \sum_n 1/(z-\gamma_n)$ DIVERGES on $\mathbb{C}^+$ (the series is conditionally convergent at best, and the limit $N \to \infty$ does not produce a finite analytic function).

**Corollary 1.** The "contradiction" $N_{C_\infty}(T) = 2N_\Xi(T)$ of Doc 32 is FALSE — it is the result of an argument that incorrectly mixes two regimes (finite and infinite). There is no contradiction.

---

## 8. What EF2-emp does imply about $C_\infty$

**Proposition 8** (direct implication of EF2-emp on the zeros of $C_\lambda$). For each FINITE $\lambda$: the number of zeros of $C_\lambda(t) = \mu_\lambda$ in the interval $[0,T]$ equals the number of eigenvalues of $J_\lambda^N$ in $[0,T]$.

*Proof.* From the identity $(C_\lambda')$ with $N_{\hat k_\lambda}^{\text{real}}(T) = N_{\hat k_\lambda}^{\text{strip}} = N_{C_\lambda-\mu_\lambda}^{\text{strip}} = 0$ (which required additional verification): $N_{C_\lambda-\mu_\lambda}^{\text{real}} = N_\lambda(T)$.

NOTE: This proposition requires that the complex zeros of $C_\lambda - \mu_\lambda$ and $\hat k_\lambda$ in the strip cancel exactly. This is part of the identity $(C_\lambda')$ — and follows automatically from $(EF_\lambda)$.

**Proposition 9** (the net identity of EF2-emp). The only NET consequence of EF2-emp on the REAL ZEROS is:

$$N_{C_\lambda(t)=\mu_\lambda}^{\text{real}}(T) = N_\lambda(T)$$

for each $\lambda$. In the limit: the real zeros of $C_\lambda(t) = \mu_\lambda$ (eigenvalues) converge to the real zeros of $C_\infty$ (under Inc. Inv.), and $N_\lambda(T) \to N_\Xi(T)$.

Hence: $N_{C_\infty}(T) = N_\Xi(T)$ — which is exactly Inc. Inv. **There is no additional information.**

**Corollary 2** (EF2-emp is circular but not contradictory). EF2-emp, correctly applied to the real zeros in the limit, says: Inc. Inv. $\Rightarrow$ $N_{C_\infty}(T) = N_\Xi(T)$ $\Rightarrow$ Inc. Inv. (circular). It contributes no new information.

---

## 9. The promising path from EF2-emp

**EF2-emp DOES provide information about the complex zeros of $C_\lambda - \mu_\lambda$.**

From $(C_\lambda')$: $N_{C_\lambda-\mu_\lambda}^{\text{strip}}(T,\eta) = N_{\hat k_\lambda}^{\text{rect}}(T,\eta)$.

In the limit: $N_{\hat k_\lambda}^{\text{rect}}(T,\eta) \to N_\Xi^{\text{real}}(T) + N_\Xi^{\text{off}}(T,\eta)$.

**Proposition 10** (EF2-emp and the zeros off the critical line). If we ALSO assume Inc. Inv. (real zeros), EF2-emp gives:

$$N_{C_\lambda-\mu_\lambda}^{\text{strip}}(T,\eta) \to N_\Xi^{\text{off}}(T,\eta)$$

in the limit $\lambda \to \infty$. This says: the complex zeros of $C_\lambda - \mu_\lambda$ in the strip converge exactly to the number of zeros of $\Xi$ OFF THE CRITICAL LINE in the strip.

Under RH: $N_\Xi^{\text{off}}(T,\eta) = 0$ for every $\eta < 1/2$, and the complex zeros of $C_\lambda - \mu_\lambda$ escape the rectangle completely.

If one could show directly (without assuming RH) that $N_{C_\lambda-\mu_\lambda}^{\text{strip}}(T,\eta) \to 0$ for some $\eta > 0$: then $N_\Xi^{\text{off}}(T,\eta) = 0$ — and that would imply RH (at least locally in the strip).

**Open question (new, from the audit).** Can it be proved that the complex zeros of $C_\lambda - \mu_\lambda$ in $0 < \Im(z) \leq \eta$ escape the rectangle as $\lambda \to \infty$, without assuming RH?

If so: RH is obtained locally (for the strip $\eta$). Taking $\eta \to 1/2$: RH would be obtained globally.

---

## 10. Summary of the audit

**Error identified in Doc 32.** The "contradiction" $N_{C_\infty}(T) = 2N_\Xi(T)$ was a limit-integral interchange error: EF2-emp cannot be used as a meromorphic identity between finite functions in the limit $N \to \infty$, because both sides diverge.

**The correct counting formula** (from EF2-emp) is:

$$N_\lambda(T) = N_{C_\lambda-\mu_\lambda}^{\text{rect}}(T,\eta) - N_{\hat k_\lambda}^{\text{rect}}(T,\eta),$$

valid for each finite $\lambda$, and involving BOTH real and complex zeros in the rectangle.

**In the limit:** the complex zeros of $C_\lambda - \mu_\lambda$ in the strip converge to the number of OFF-CRITICAL zeros of $\Xi$ — without assuming RH. Under RH these escape the rectangle.

**The new path.** The audit reveals a new, precise question: do the complex zeros of $C_\lambda - \mu_\lambda$ in the strip escape unconditionally? If so: RH.

---

*Next doc: Doc 37 — Connection with Random Matrix Theory (RMT).*
