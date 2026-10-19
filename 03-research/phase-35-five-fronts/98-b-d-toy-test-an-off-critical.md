# Doc 98 — B+D toy test: an off-critical quadruple

**Program:** Riemann Hypothesis — Phase 35, Five Fronts
**Prerequisites:** Docs 82, 83, 86, 89, 91, 93, 95, 96, 97; Papers P35, P39
**Absolute rule:** no proof is fabricated. Every step is either a complete proof within the toy model, or a GAP declared with precision.

---

## Executive summary

This document subjects the B+D connection conjecture — "the irreducible part $d\nu^*$ of the variational problem (Direction D) corresponds to the localization of the negative index in $\mathcal{K}_{\mathrm{off}}$ (Direction B)" — to the simplest possible test: $\neg$RH with **exactly one quadruple** of off-critical zeros $\{1/2\pm\delta\pm i\gamma_0\}$, $\delta\in(0,1/2)$, $\gamma_0>0$, and all other zeros on the critical line.

**Test results:**

1. (§2) The factor $R_{\gamma_0,\delta}$ and the measure $d\nu$ are computed in **closed form**: $R-1$ is an exact degree-4 polynomial in $\delta^2$, with no infinite remainder. To leading order, $d\nu = 2\delta^2 K_0(s)\,f_0^{on}(s)\,dm_\infty + O(\delta^4)$ with $K_0(s) = (s-\gamma_0)^{-2}+(s+\gamma_0)^{-2}$.

2. (§3) The test detects **two internal errors in Docs 93/95**: (a) the "transversal variation" $\epsilon=i\delta$ of Doc 93 §2.3 is actually tangential, and with the correct transversal direction the second transversal variation at $f_0^{on}$ is **negative** ($\psi''(0) = -8\mathcal{Q}_\lambda^{(0)} < 0$), not positive; (b) the Euler–Lagrange kernel $2s/(s^2-\gamma_j^2)$ of Docs 95/97 is odd and makes the equations **vacuous** by parity; the correct kernel (compatible with the functional equation) is $-4\gamma_j/(s^2-\gamma_j^2)$, even.

3. (§4–5) **Absorption theorem** (central result): the order-$\delta^2$ component of $d\nu$, localized at the frequencies $\pm\gamma_0$ of the quadruple, is **asymptotically absorbable** within $\overline{\mathcal{M}}$ by delocalized reorganization of the distant on-line zeros (plus addition of pairs at infinity). Consequently $\tilde\delta_\lambda(\delta) = o(\delta^2)$ and the mass of $d\nu^*$ is $o(\delta^2)$: it is **not** $O(\delta^2)$ with positive coefficient; whether it is exactly $O(\delta^4)$ remains a gap.

4. (§6) Side B: the quadruple generates $\mathcal{K}_{\mathrm{off}}$ of dimension 4 (eigenvalues $\pm\delta\pm i\gamma_0$ of $H_C$), with Gram form equal to two hyperbolic planes: $\kappa = 2$, **independent of $\delta$** and discontinuous at $\delta=0$. Consistent with P35 ($\kappa = 2m$, $m=1$).

5. (§7) Maslov index of the crossing $\delta:0\to\delta_0$: spectral flow $= -2$, $|\mu| = 2 = \kappa$ (with declared technical regularity gaps).

6. (§8) **Central question (vi): the strong correspondence $d\nu^* \leftrightarrow \mathcal{K}_{\mathrm{off}}$ does NOT hold.** The magnitudes do not agree at any order in $\delta$ (constant integer $\kappa=2$ vs. evanescent mass $o(\delta^2)$); the localization does not agree ($\mathcal{K}_{\mathrm{off}}$ rigidly anchored to the quadruple, $d\nu^*$ delocalized by the absorption mechanism); there is no natural map. The only thing that coincides is simultaneous vanishing, which is tautological via RH. **The B+D connection, in its strong form, is dead.** What survives is a different, weaker correspondence: $\mathcal{K}_{\mathrm{off}} \leftrightarrow d\nu$ (the fixed-reference residual at $f_0^{on}$, not the optimized one), both of scale $\delta^2$ and both localized at the quadruple.

**VERDICT: ROUTE CLOSED** for the strong correspondence $d\nu^*\leftrightarrow\mathcal{K}_{\mathrm{off}}$ (§10).

---

## §1. The toy model: exact definitions

### 1.1. Hypotheses of the model

**Hypothesis (T1) — Zero configuration.** The non-trivial zeros of $\xi$ are:
- the simple pairs $\{1/2 \pm i\gamma_j\}_{j\geq 1}$, with $0 < \gamma_1 < \gamma_2 < \cdots$, $\gamma_j \to \infty$;
- exactly one off-critical quadruple
$$Z_\delta = \{\,1/2+\delta+i\gamma_0,\; 1/2+\delta-i\gamma_0,\; 1/2-\delta+i\gamma_0,\; 1/2-\delta-i\gamma_0\,\},$$
with $\delta \in (0,1/2)$, $\gamma_0 > 0$, $\gamma_0 \notin \{\gamma_j\}_{j\geq 1}$.

**Hypothesis (T2) — Perturbative regime.** All expansions are carried out in powers of $\delta^2$ with $\gamma_0$ fixed. As will be seen (Proposition 2.2), in this model the relevant expansions are exact polynomials in $\delta^2$: there is no remainder problem.

**Hypothesis (T3) — Inherited CCM structure (cited, not proved here).**
- (W-pos) $W_\lambda \geq 0$ (CCM Abel kernel, Doc 82).
- (W-pol) $W_\lambda$ has at most polynomial growth in $|s|$ (Doc 82 §2, cited via Doc 95, Lemma 2.2).
- (W-par) $W_\lambda(s) = W_\lambda(-s)$. This parity is implicit in the symmetric framework of Doc 83 §2.2 (both measures $dm_{\mathrm{full}}$, $dm_{\mathrm{full,on}}$ are even and the odd moments vanish). It is declared as a structural hypothesis.

**Hypothesis (T4) — Spectral separation (only for §7).** The cluster $\{\pm i\gamma_0\}$ is at positive distance from the rest of the spectrum of $H_C$, uniformly in $\delta \in [0,\delta_0]$.

### 1.2. $\zeta_{\mathrm{on}}$ in the toy model

By the definition of Doc 83 §1.1, $\xi_{\mathrm{on}}$ is obtained by projecting each zero onto the critical line while preserving the imaginary part. The quadruple $Z_\delta$ projects onto $\{1/2+i\gamma_0,\,1/2-i\gamma_0\}$, **each with multiplicity 2** (Doc 83, §1.2, quadruple computation). Hence, in the toy model:

- $\xi_{\mathrm{on}}$ has simple zeros at $1/2\pm i\gamma_j$ ($j\geq 1$) and **double** zeros at $1/2\pm i\gamma_0$.
- On the line, $f_0^{on}(s) = |\zeta_{\mathrm{on}}(1/2+is)|^2$ vanishes to order 2 at $s=\pm\gamma_j$ and to **order 4** at $s = \pm\gamma_0$. We write
$$f_0^{on}(s) = (s^2-\gamma_0^2)^4\, G(s), \qquad G \text{ continuous}, \; G(\pm\gamma_0) > 0. \tag{1.1}$$

**Remark 1.1 (rigidity of multiplicity).** The real symmetry of $\eta\in\mathcal{E}$ (real coefficients after rotation) together with the functional equation forces off-critical zeros to appear in quadruples. Consequence: a simple on-line pair $\{1/2\pm i\gamma_j\}$ **cannot** be deformed off the line within the class of functions with the symmetries of $\xi$; only on-line points of multiplicity $\geq 2$ admit transversal splitting. In the toy model, $f_0^{on}$ admits exactly **one** genuine transversal direction: the splitting of the double zero at $\pm\gamma_0$. This will be used in §3.3.

---

## §2. Object (i): the factor $R$ and the measure $d\nu$ in closed form

### 2.1. Closed form of $R$

**Proposition 2.1 (Quadruple factor; Doc 83, Proposition 1.1 specialized).** For every $s \in \mathbb{R}$ with $s \neq \pm\gamma_0$:
$$R_{\gamma_0,\delta}(s) := \frac{f_0(s)}{f_0^{on}(s)} = \left(1+\frac{\delta^2}{(s-\gamma_0)^2}\right)^{2}\left(1+\frac{\delta^2}{(s+\gamma_0)^2}\right)^{2} \;\geq\; 1. \tag{2.1}$$

*Proof.* This is the exact computation of Doc 83, §1.2 (factor $C_j(u)$ of the quadruple), with a single quadruple: the product of Proposition 1.1 of Doc 83 has only one term. The inequality $\geq 1$ is immediate. $\square$

Consequently, with $d\nu := dm_{\mathrm{full}} - dm_{\mathrm{full,on}} = (f_0 - f_0^{on})\,dm_\infty$ (Doc 83, Corollary 1.3; Doc 89):
$$d\nu(s) = \bigl(R_{\gamma_0,\delta}(s) - 1\bigr)\, f_0^{on}(s)\, dm_\infty(s) \;\geq\; 0 \quad \text{(unconditional)}. \tag{2.2}$$

### 2.2. Exact expansion in $\delta^2$ (no remainder)

**Proposition 2.2 (Exact polynomial expansion).** Let $a = \delta^2/(s-\gamma_0)^2$, $b = \delta^2/(s+\gamma_0)^2$. Then
$$R_{\gamma_0,\delta}(s) - 1 = 2(a+b) + (a^2 + b^2 + 4ab) + 2ab(a+b) + a^2b^2, \tag{2.3}$$
that is, $R-1$ is an **exact degree-4 polynomial in $\delta^2$** with explicit rational coefficients in $s$:
$$R - 1 = 2\delta^2 K_0(s) + \delta^4 Q_2(s) + 2\delta^6 Q_3(s) + \delta^8 Q_4(s),$$
where
$$K_0(s) = \frac{1}{(s-\gamma_0)^2}+\frac{1}{(s+\gamma_0)^2} = \frac{2(s^2+\gamma_0^2)}{(s^2-\gamma_0^2)^2} \;>\;0,$$
$$Q_2 = \frac{1}{(s-\gamma_0)^4}+\frac{1}{(s+\gamma_0)^4}+\frac{4}{(s^2-\gamma_0^2)^2},\quad Q_3 = \frac{K_0(s)}{(s^2-\gamma_0^2)^2},\quad Q_4 = \frac{1}{(s^2-\gamma_0^2)^4}.$$

*Proof.* $(1+a)^2(1+b)^2 = (1+2a+a^2)(1+2b+b^2)$; direct expansion and grouping by total degree in $(a,b)$, which coincides with the degree in $\delta^2$. $\square$

**Proposition 2.3 (Integrability and closed form of $d\nu$).** Each term of (2.3) multiplied by $f_0^{on}$ is continuous at $s=\pm\gamma_0$ and belongs to $H_\lambda = L^2(W_\lambda\,dm_\infty)$. In particular:
$$d\nu = \Bigl[\,2\delta^2\, K_0(s)\,f_0^{on}(s) \;+\; \delta^4 E_\delta(s)\,f_0^{on}(s)\Bigr]\, dm_\infty(s), \qquad E_\delta := Q_2 + 2\delta^2 Q_3 + \delta^4 Q_4, \tag{2.4}$$
with $\|E_\delta f_0^{on}\|_{H_\lambda} \leq C(\gamma_0,\lambda)$ uniformly for $\delta\in(0,1/2)$. The "remainder" $\delta^4 E_\delta f_0^{on}$ is exact, not asymptotic.

*Proof.* By (1.1), $f_0^{on} = (s^2-\gamma_0^2)^4 G$ with $G$ continuous and positive at $\pm\gamma_0$. The most singular term of (2.3) is $Q_4 = (s^2-\gamma_0^2)^{-4}$, and $Q_4 f_0^{on} = G$ is continuous. Likewise $K_0 f_0^{on} = 2(s^2+\gamma_0^2)(s^2-\gamma_0^2)^2 G$ vanishes to order 2 at $\pm\gamma_0$. Membership in $H_\lambda$ follows from (W-pol), from the polynomial growth of $f_0(s) \geq f_0^{on}(s)$ on the line (convexity bound $|\zeta(1/2+it)| \ll (1+|t|)^{1/4}$, Titchmarsh [T86], Ch. V) and from the decay $dm_\infty \asymp |s|^{-1/2}e^{-\pi|s|/2}ds$ (Doc 95, Lemma 2.2). $\square$

**This answers object (i):** explicit $R$ (2.1), explicit $d\nu \geq 0$ (2.2), expansion to order $\delta^2$ with **exactly controlled** remainder (2.4). The leading density of $d\nu$ is
$$\nu_2(s) := 2\,K_0(s)\,f_0^{on}(s) = 4(s^2+\gamma_0^2)(s^2-\gamma_0^2)^2 G(s), \tag{2.5}$$
a **smooth, even function, positive away from $\pm\gamma_0$**, with "resonance" (concentration of the kernel $K_0$) at the frequencies $\pm\gamma_0$ of the quadruple.

### 2.3. Mass of $d\nu$ to leading order

**Corollary 2.4 (Exact leading-order mass).** The $H_\lambda$ norm of the density of $d\nu$ satisfies
$$\bigl\|\,(R_{\gamma_0,\delta}-1)\,f_0^{on}\,\bigr\|_{H_\lambda} = 2\delta^2\,\bigl\|K_0\,f_0^{on}\bigr\|_{H_\lambda} + O(\delta^4), \qquad \bigl\|K_0f_0^{on}\bigr\|_{H_\lambda}^2 = \int_\mathbb{R} W_\lambda\,\bigl(2(s^2+\gamma_0^2)(s^2-\gamma_0^2)^2G(s)\bigr)^2 dm_\infty \in (0,\infty),$$
with the constant depending only on $(\gamma_0,\lambda)$ and on the on-line zeros. Likewise, $T_\lambda = \int W_\lambda\,d\nu = 2\delta^2\int W_\lambda K_0 f_0^{on}\,dm_\infty + O(\delta^4)$, consistent with the lower bound $T_\lambda \geq 2\delta^2 K_\lambda(\gamma_0)$ of Doc 86, §6 (the kernel $K_\lambda(\gamma_0)$ of Doc 86 is the integral with the term $(s-\gamma_0)^{-2}$ of $K_0$). Both fixed-reference objects are $\asymp \delta^2$ with explicit positive constants. $\square$

---

## §3. Local geometry of $\mathcal{M}$ at $f_0^{on}$: two corrections

Before setting up Euler–Lagrange, the toy model forces the correction of two points in Docs 93/95/97. Both corrections are proved completely.

### 3.1. Correction A: parity of the Euler–Lagrange kernel

**Lemma 3.1 (The EL equations of Docs 95/97, as written, are vacuous).** Under (W-par), for any even $g \in \mathcal{M}$ and any $\gamma > 0$:
$$\int_\mathbb{R} W_\lambda(s)\,\bigl(f_0(s)-g(s)\bigr)\,g(s)\,\frac{2s}{s^2-\gamma^2}\,dm_\infty(s) = 0 \quad \text{identically}.$$

*Proof.* $f_0$, $f_0^{on}$ and every $g=|\eta|^2\in\mathcal{M}$ are even in $s$ (functional equation + Schwarz reflection: $|\zeta(1/2-is)| = |\zeta(1/2+is)|$ for real $s$; likewise for $\eta\in\mathcal{E}$ with symmetric zeros $\pm\gamma_j$). $W_\lambda$ and $dm_\infty$ are even ((W-par); $|\Gamma(1/4+is/2)|^2$ is even). The kernel $2s/(s^2-\gamma^2)$ is **odd**. The integral of (even)·(odd) with respect to an even measure is zero (principal value at $\pm\gamma$, where moreover the integrand is regular because $g$ vanishes to order $\geq 2$ if $\gamma$ is a zero of $\eta$). $\square$

**Consequence 3.2 (correction to Doc 95, Lemma 4.6, and to Doc 97, eq. (EL)).** The claim "$f_0^{on}$ does not satisfy the Euler–Lagrange equations under $\neg$RH" cannot be sustained with the odd kernel $2s/(s^2-\gamma_j^2)$: with that kernel **every** even element satisfies them trivially. The origin of the error is the underlying variation: the kernel $1/(s-\gamma_j)+1/(s+\gamma_j)$ corresponds to translating **both** zeros $\pm\gamma_j$ in the same direction ($\gamma_j\mapsto\gamma_j+\epsilon$, $-\gamma_j\mapsto-\gamma_j+\epsilon$), which breaks the symmetry $s\mapsto 1-s$ and leaves $\mathcal{E}$. The admissible variation (preserving the functional equation) moves the pair symmetrically: $\pm\gamma_j \mapsto \pm(\gamma_j+\epsilon)$.

**Lemma 3.3 (Correct tangent vectors).** Let $g_\Gamma \in \mathcal{M}$ with zeros $\{\pm\gamma_j\}$ of multiplicities $m_j$. The admissible curve $\epsilon \mapsto g_{\Gamma(\epsilon)}$ that moves $\pm\gamma_j \mapsto \pm(\gamma_j+\epsilon)$ has tangent vector at $\epsilon = 0$:
$$t_j(s) = \frac{\partial}{\partial\epsilon} g_{\Gamma(\epsilon)}(s)\Big|_{\epsilon=0} = -\,\frac{4\,m_j\,\gamma_j}{s^2-\gamma_j^2}\; g_\Gamma(s), \tag{3.1}$$
which is **even** in $s$ and belongs to $H_\lambda$ (the apparent pole at $\pm\gamma_j$ cancels against the order-$2m_j$ zero of $g_\Gamma$).

*Proof.* On the line, the pair contributes the factor $\bigl((s^2-\gamma_j^2)^2\bigr)^{m_j}$ to $g_\Gamma$ (modulo positive constants and Hadamard's exponential compensators, whose joint contribution from the pair is independent of $s$ modulo a multiplicative constant that is reabsorbed into the constant direction, available by Lemma 4.1 below). Then
$$\frac{\partial}{\partial\epsilon}\log\bigl((s^2-(\gamma_j+\epsilon)^2)^{2m_j}\bigr)\Big|_{\epsilon=0} = 2m_j\cdot\frac{-2\gamma_j}{s^2-\gamma_j^2} = -\frac{4m_j\gamma_j}{s^2-\gamma_j^2}. \qquad\square$$

**Corrected Euler–Lagrange equations.** For $g^* = |\eta^*|^2$ with zeros $\{\pm\gamma_j^*\}$, multiplicities $m_j^*$:
$$\boxed{\;\mathrm{EL}_j:\quad \int_\mathbb{R} W_\lambda(s)\,\bigl(f_0(s)-g^*(s)\bigr)\, g^*(s)\,\frac{\gamma_j^*}{s^2-(\gamma_j^*)^2}\,dm_\infty(s) = 0 \quad \forall j.\;} \tag{3.2}$$
The kernel is even and the equations are non-trivial. The orthogonality structure of Doc 97 (Theorem 2.7, Corollary 2.8) is preserved with the replacement $K_j^* \rightsquigarrow \tilde K_j^*(s) = \gamma_j^*/(s^2-(\gamma_j^*)^2)$.

### 3.2. Correction B: the sign of the second transversal variation of Doc 93

**Lemma 3.4 (Parametrization error in Doc 93 §2.3).** In Doc 93, the "transversal variation" was defined as $\epsilon = i\delta$ (Definition 2.1), but the computation of §2.3 substitutes $\alpha_j + i\delta = 1/2 + i(\gamma_j+\delta)$: that displacement is **tangential** (along the critical line). The genuinely transversal variation is real $\epsilon = \delta$, with zeros displaced to $1/2\pm\delta+i\gamma_j$, and it produces the factor with a **plus** sign:
$$|R^{\mathrm{transv}}_{\delta}(1/2+is)|^2 = \left(1+\frac{\delta^2}{(s-\gamma_j)^2}\right)^{2}\left(1+\frac{\delta^2}{(s+\gamma_j)^2}\right)^{2},$$
coinciding with (2.1), not $(1 - 2\delta^2 K_j + O(\delta^4))$ as in Lemma 2.3 of Doc 93.

*Proof.* With the zero at $1/2+\delta+i\gamma_j$: $\bigl|(1/2+is) - (1/2+\delta+i\gamma_j)\bigr|^2 = \delta^2 + (s-\gamma_j)^2$. Dividing by $(s-\gamma_j)^2$ gives $1+\delta^2/(s-\gamma_j)^2 \geq 1$. This is exactly the computation of Doc 83 §1.2 (which is correct). $\square$

**Proposition 3.5 (Second transversal variation: corrected sign).** In the toy model, the only transversal direction at $f_0^{on}$ (Remark 1.1) is the splitting of the double zero at $\pm\gamma_0$. Let $\psi(\delta') := \|f_0 - f_0^{on}\,R_{\gamma_0,\delta'}\|^2_{H_\lambda}$ for $\delta'\in[0,\delta]$ be the distance along that transversal curve. Then:

(a) $\psi(\delta) = 0$ exactly (the curve reaches $f_0$).

(b) $\psi'(0) = 0$ and
$$\psi''(0) = -8\,\mathcal{Q}_\lambda^{(0)} \;<\; 0, \qquad \mathcal{Q}_\lambda^{(0)} := \int_\mathbb{R} W_\lambda\,(f_0-f_0^{on})\,f_0^{on}\,K_0\,dm_\infty \;>\;0.$$

That is: $f_0^{on}$ is a **strict local maximum**, not a minimum, along the transversal curve; the curve is a descent direction toward $f_0$.

*Proof.* (a) By Proposition 2.1, $f_0 = f_0^{on}R_{\gamma_0,\delta}$. (b) By Proposition 2.2 applied with parameter $\delta'$: $f_0^{on}R_{\gamma_0,\delta'} = f_0^{on} + 2\delta'^2 K_0 f_0^{on} + O(\delta'^4)$ in $H_\lambda$. Then
$$f_0 - f_0^{on}R_{\gamma_0,\delta'} = D_0 - 2\delta'^2 K_0 f_0^{on} + O(\delta'^4), \qquad D_0 := f_0 - f_0^{on} \geq 0,$$
and
$$\psi(\delta') = \psi(0) - 4\delta'^2 \int W_\lambda\, D_0\, f_0^{on} K_0\,dm_\infty + O(\delta'^4) = \psi(0) - 4\delta'^2\,\mathcal{Q}_\lambda^{(0)} + O(\delta'^4).$$
Positivity $\mathcal{Q}_\lambda^{(0)}>0$ is the argument of Doc 93, Proposition 4.3(a) (integrand $\geq 0$, positive on a set of positive measure), which is correct; what was incorrect was the sign of the order-$\delta'^2$ term. $\square$

**Remark 3.6 (Scope of the correction).** Proposition 3.5 **refutes** Corollary 4.4 and Proposition 6.6 of Doc 93 ("convexity of $\mathcal{M}$ toward $f_0$"): under $\neg$RH (in the toy model), the genuine normal direction is one of descent, which is geometrically obvious in hindsight — de-projecting the zeros toward their true positions brings $f_0^{on}$ closer to $f_0$, until reaching it at $\delta'=\delta$. There is no contradiction with $\tilde\delta_\lambda^2>0$: the transversal curve leaves $\mathcal{M}$ (for $\delta'>0$ the quadruple is off the line), so the descent is not realizable within $\mathcal{M}$. The bound $T_\lambda \geq 2\delta^2 K_\lambda(\gamma_0)$ of Doc 86 and the P39 criterion remain intact: they do not depend on the sign of $\psi''$.

---

## §4. Object (ii): Euler–Lagrange for $g^*$ and its first-order solution

### 4.1. Linearization of the variational problem

We seek $g \in \mathcal{M}$ (or $\overline{\mathcal{M}}$) close to $f_0^{on}$, $g = f_0^{on} + h$. Since $\|f_0 - f_0^{on}\|_{H_\lambda} = 2\delta^2\|K_0f_0^{on}\|_{H_\lambda} + O(\delta^4)$ (Corollary 2.4) and $g = f_0^{on}$ is admissible, every relevant competitor satisfies $\|h\|_{H_\lambda} \leq C\delta^2$; for curves in $\mathcal{M}$ parametrized by zero displacements of size $O(\delta^2)$, the second-order corrections of the curve are $O(\delta^4)$ (exact rational factors, Lemma 4.1 below). The linearized problem is then:
$$\text{minimize } \bigl\|\,2\delta^2\, K_0\, f_0^{on} - h\,\bigr\|_{H_\lambda} \quad\text{over } h \in \mathcal{T}, \tag{4.1}$$
where $\mathcal{T}$ is the **closed tangent cone** of $\mathcal{M}$ at $f_0^{on}$ within $H_\lambda$ (closure of the set of limits $\lim \tau_n^{-1}(g_n - f_0^{on})$ with $g_n\in\mathcal{M}$, $\tau_n\downarrow0$). Its solution is the metric projection of $2\delta^2 K_0f_0^{on}$ onto $\mathcal{T}$, and
$$d\nu^* = \bigl(\mathrm{Id} - P_{\mathcal{T}}\bigr)\bigl(2\delta^2 K_0 f_0^{on}\bigr)\,dm_\infty + O(\delta^4). \tag{4.2}$$

Everything reduces, to leading order, to one question: **what does $\mathcal{T}$ contain, and is $K_0f_0^{on}$ in it?** Note that the corrected EL equations (3.2), evaluated in the linearized problem, are exactly the normal equations of (4.1) with respect to the directions $t_j$ of Lemma 3.3: $\langle 2\delta^2K_0f_0^{on} - h^*,\, t_j\rangle_{H_\lambda} = 0$. But Lemma 4.1 will show that $\mathcal{T}$ is strictly larger than $\overline{\mathrm{span}}\{t_j\}$ taken term by term: it contains all the collective combinations of distant zero movements, and that decides the problem.

### 4.2. The tangent cone contains the even polynomial directions

**Lemma 4.1 (Polynomial directions).** For every even polynomial $p(s) = \sum_{k=0}^K p_k s^{2k}$ with real coefficients (of either sign) and every $\epsilon_0 > 0$, there exists a family $\{g_\tau\}_{\tau\in[0,\tau_0]}\subset\mathcal{M}$, obtained by moving a finite number of distant zeros $\gamma_{j_1} < \cdots < \gamma_{j_N}$ ($N = K+1$) of $\zeta_{\mathrm{on}}$ by amounts $\tau a_i$, such that
$$g_\tau = f_0^{on}\,\bigl(1 + \tau\,p(s) + \tau\, e_\tau(s)\bigr), \qquad \|f_0^{on} e_\tau\|_{H_\lambda} \leq \epsilon_0 + C(p,\Gamma)\,\tau,$$
with $C(p,\Gamma)$ independent of $\tau$. Consequently, the closed tangent cone $\mathcal{T}$ contains the subspace
$$\mathcal{T}_{\mathrm{pol}} := \overline{\mathrm{span}}^{H_\lambda}\bigl\{\, f_0^{on}(s)\, s^{2k} \;:\; k \geq 0 \,\bigr\}.$$

*Proof.* Moving the pair $\pm\gamma_{j}$ by $\epsilon_i = \tau a_i$ multiplies $f_0^{on}$ by the exact factor $\bigl((s^2-(\gamma_{j}+\epsilon_i)^2)/(s^2-\gamma_{j}^2)\bigr)^2$ (plus a positive constant from Hadamard's compensators, which is $1+O(\tau)$ and is absorbed). For $|s| \leq \gamma_{j}/2$:
$$\log\frac{(s^2-(\gamma_j+\epsilon_i)^2)^2}{(s^2-\gamma_j^2)^2} = 2\log\Bigl(1 - \frac{2\gamma_j\epsilon_i+\epsilon_i^2}{\gamma_j^2 - s^2}\cdot(-1)\Bigr) = \frac{4\epsilon_i}{\gamma_j}\sum_{k\geq 0}\Bigl(\frac{s^2}{\gamma_j^2}\Bigr)^k + O(\epsilon_i^2),$$
using $1/(s^2-\gamma_j^2) = -\gamma_j^{-2}\sum_k (s^2/\gamma_j^2)^k$. Summing over $i=1,\dots,N$, the coefficient of $s^{2k}$ is $\sum_i 4 a_i\,\gamma_{j_i}^{-(2k+1)}\,\tau$. The matrix $\bigl(4\gamma_{j_i}^{-(2k+1)}\bigr)_{k=0..K,\,i=1..N}$ is a generalized Vandermonde matrix in the distinct nodes $x_i = \gamma_{j_i}^{-2}$ with nonzero column scalings $4/\gamma_{j_i}$: invertible. The $a_i$ are chosen by solving $\sum_i 4a_i\gamma_{j_i}^{-(2k+1)} = p_k$. The error $e_\tau$ has two sources: (1) the terms $k > K$ of the series, of size $\leq C\sum_i |a_i|\,\gamma_{j_i}^{-(2K+3)}\,|s|^{2K+2}$ for $|s|\leq\gamma_{j_1}/2$ — since $\|s^{2m}f_0^{on}\|_{H_\lambda}^{1/(2m)} \leq C\,m$ (moments of $e^{-\pi|s|/2}$: $\int s^{4m}e^{-\pi s/2}ds = (4m)!\,(2/\pi)^{4m+1}$), it suffices to take $\gamma_{j_1} \geq C'(K)$ large to make this contribution $\leq \epsilon_0/2$; (2) the region $|s| > \gamma_{j_1}/2$, where the exact factor is bounded by $C(p)$ and the weight $W_\lambda f_0^{on}\,dm_\infty \lesssim e^{-\pi\gamma_{j_1}/4}$ crushes it below $\epsilon_0/2$ by choosing $\gamma_{j_1}$ large. The terms $O(\epsilon_i^2) = O(\tau^2)$ give the part $C(p,\Gamma)\tau$. The constant direction ($k=0$) additionally covers the normalization constants of the compensators. Both signs of $p_k$ are realizable because $\epsilon_i = \tau a_i$ admits either sign (distant zeros can move inward or outward). $\square$

**Remark 4.2 (addition of pairs at infinity).** Alternatively, adding a pair of zeros at $\pm\mu$ with $\mu\to\infty$ produces the direction $-2s^2f_0^{on}/\mu^2 + O(\mu^{-4})$ (exact factor $(1-s^2/\mu^2)^2$ after renormalizing): this is the "zeros escaping to infinity" mechanism of Doc 95 §2.6, now used constructively. It gives only the negative sign of the $s^2$ coefficient; Lemma 4.1 (movement of existing zeros) gives both signs, and that is what we use.

### 4.3. Polynomial density: the Carleman–Riesz step

**Lemma 4.3 (Density of polynomials).** Let $\mu_\star$ be the finite measure $d\mu_\star = W_\lambda(s)\,\bigl(f_0^{on}(s)\bigr)^2\,dm_\infty(s)$ on $\mathbb{R}$. Then the polynomials are dense in $L^2(\mu_\star)$.

*Proof.* By (W-pol), by $f_0^{on} \leq f_0 \ll (1+|s|)^{1/2+\epsilon}$ (convexity bound [T86]), and by $dm_\infty \asymp |s|^{-1/2}e^{-\pi|s|/2}ds$ (Stirling; Doc 95, Lemma 2.2), there exists $A<\infty$ with $d\mu_\star \leq C(1+|s|)^{A}e^{-\pi|s|/2}ds$. Its moments satisfy $m_{2k}(\mu_\star) \leq C\,(2k+A)!\,(2/\pi)^{2k}$, hence $m_{2k}^{-1/(2k)} \gtrsim 1/(Ck)$ and $\sum_k m_{2k}^{-1/(2k)} = \infty$: Carleman's condition, the measure is determinate (Hamburger). By M. Riesz's theorem, every determinate measure has polynomials dense in $L^2$ (Akhiezer [A65], Cor. 2.3.3). $\square$

**Lemma 4.4 ($K_0 \in L^2(\mu_\star)$).** $K_0$ is continuous away from $\pm\gamma_0$, $K_0(s) = O(s^{-2})$ at infinity, and near $\pm\gamma_0$ one has $K_0^2\,(f_0^{on})^2 \asymp (s\mp\gamma_0)^{-4}\cdot (s\mp\gamma_0)^{16} \to 0$ by (1.1). Hence $K_0 \in L^2(\mu_\star)$. $\square$

### 4.4. First-order Euler–Lagrange solution: it exists in the limit, not in $\mathcal{M}$

**Theorem 4.5 (Absorption of the leading component).** In the toy model, under (T1)–(T3):
$$\inf_{p \text{ even polynomial}} \bigl\|\,2K_0 f_0^{on} - p\cdot f_0^{on}\,\bigr\|_{H_\lambda} = \inf_p \|2K_0 - p\|_{L^2(\mu_\star)} = 0.$$
That is: the curvature direction $K_0f_0^{on}$ (leading density of $d\nu$, eq. (2.5)) belongs to $\mathcal{T}_{\mathrm{pol}} \subseteq \mathcal{T}$: it is **totally absorbable** by the closed tangent cone of $\mathcal{M}$ at $f_0^{on}$.

*Proof.* Immediate from Lemmas 4.3 and 4.4. $\square$

**Answer to object (ii).** The corrected EL equations (3.2), linearized around $f_0^{on}$, are the normal equations of the projection (4.1). By Theorem 4.5, the projection of the leading density is **itself**: the linearized system "is solved" with
$$g^*_{\mathrm{lin}} = f_0^{on}\,(1 + 2\delta^2 K_0) + o(\delta^2) = f_0 + o(\delta^2),$$
**but it is not attained by any element of $\mathcal{M}$**: the solution is realized only as a limit of sequences $\{g_n\}\subset\mathcal{M}$ whose polynomial approximations require moving ever more distant zeros ($\gamma_{j_1}(n)\to\infty$). This is the constructive materialization of the ND1/ND3 failure anticipated in Doc 95 §2: in the toy model, **ND1 actually fails** (there is no minimizer in $\mathcal{M}$ realizing the leading order; if the infimum is attained in $\overline{\mathcal{M}}$, the shadow minimizer is an object of the closure with "escaped zeros"). GAP G2 (§9): it is not determined here whether the infimum is attained in $\overline{\mathcal{M}}$.

---

## §5. Object (iii): the decomposition $d\nu = d\nu^* + (g^*-f_0^{on})\,dm_\infty$ to order $\delta^2$

**Theorem 5.1 (The variational distance is $o(\delta^2)$).** In the toy model, under (T1)–(T3):
$$\tilde\delta_\lambda(\delta) := \inf_{g\in\mathcal{M}}\|f_0 - g\|_{H_\lambda} = o(\delta^2) \qquad (\delta\to 0,\ \gamma_0,\lambda \text{ fixed}).$$
More precisely: for every $\epsilon>0$ there exists $C_\epsilon = C(\epsilon,\gamma_0,\lambda) <\infty$ with
$$\tilde\delta_\lambda(\delta) \;\leq\; \epsilon\,\delta^2 \;+\; C_\epsilon\,\delta^4 \qquad \forall \delta\in(0,1/2).$$

*Proof.* Given $\epsilon>0$: by Theorem 4.5 choose an even polynomial $p_\epsilon$ with $\|2K_0 - p_\epsilon\|_{L^2(\mu_\star)} \leq \epsilon/2$. By Lemma 4.1 with $\tau = \delta^2$ and $\epsilon_0 = \epsilon/4$, there exists $g_\delta \in \mathcal{M}$ (distant zeros moved by amounts $O(\delta^2)$) with
$$g_\delta = f_0^{on}\bigl(1 + \delta^2 p_\epsilon + \delta^2 e\bigr), \qquad \|f_0^{on}e\|_{H_\lambda} \leq \tfrac{\epsilon}{4} + C(p_\epsilon)\,\delta^2.$$
By Proposition 2.3, $f_0 = f_0^{on}(1 + 2\delta^2K_0 + \delta^4 E_\delta)$ with $\|f_0^{on}E_\delta\|_{H_\lambda}\leq C(\gamma_0,\lambda)$. Then
$$\|f_0 - g_\delta\|_{H_\lambda} \leq \delta^2\,\|(2K_0-p_\epsilon)f_0^{on}\|_{H_\lambda} + \delta^2\|f_0^{on}e\|_{H_\lambda} + \delta^4\|f_0^{on}E_\delta\|_{H_\lambda} \leq \epsilon\,\delta^2\cdot\tfrac34 + C_\epsilon\delta^4. \qquad\square$$

**Corollary 5.2 (Structure of the decomposition of Doc 97, Prop. 9.1, in the toy model).** Under (H-ND1) (existence of $g^*$ in $\overline{\mathcal{M}}$; conditional):
$$\underbrace{d\nu}_{\text{mass } \asymp\, \delta^2} \;=\; \underbrace{d\nu^*}_{\text{mass } =\, o(\delta^2)} \;+\; \underbrace{(g^* - f_0^{on})\,dm_\infty}_{\text{mass } \asymp\, \delta^2},$$
where "mass" denotes the $H_\lambda$ norm of the density. That is:

(a) The **absorbable** part of $d\nu$ is **the entire leading order**: $(g^*-f_0^{on})\,dm_\infty = 2\delta^2K_0f_0^{on}\,dm_\infty + o(\delta^2)$.

(b) The **irreducible** part $d\nu^*$ is $o(\delta^2)$: strictly subdominant. Answer to the question "(iii) is $d\nu^* = O(\delta^2)$ or $O(\delta^4)$?": **it is not $O(\delta^2)$ with positive coefficient; it is proved to be $o(\delta^2)$; the exact $O(\delta^4)$ bound is a GAP (G3)**, because the constant $C_\epsilon$ of Theorem 5.1 may blow up as $\epsilon\to0$ (it depends on the degree of the approximating polynomial) and the optimal trade-off $\epsilon(\delta)$ is not quantified.

(c) Lower bound: $\tilde\delta_\lambda(\delta) > 0$ for every $\delta\in(0,1/2)$ by the criterion of Doc 82 ($\tilde\delta^2_\lambda = 0 \iff$ RH, and in the toy model $\neg$RH). The test produces no quantitative lower bound in $\delta$; that is exactly the non-trivial content of ND4 (Doc 95 §7.4), which remains open.

**Proposition 5.3 (Separation of functionals: $T_\lambda$ vs. $\tilde\delta_\lambda^2$).** In the toy model:
$$T_\lambda = \int W_\lambda\,d\nu \;\geq\; 2\delta^2\,K_\lambda(\gamma_0) \;\asymp\; \delta^2 \qquad (\text{Doc 86, §6}),$$
while $\tilde\delta_\lambda^2 = o(\delta^4)$ by Theorem 5.1. Hence **$T_\lambda$ and $\tilde\delta_\lambda^2$ are not comparable**: the trace functional (linear in $d\nu$, fixed reference $f_0^{on}$) detects the quadruple at order $\delta^2$; the distance functional (which re-optimizes the reference over $\mathcal{M}$) detects it at a strictly higher order. Any quantitative identification $T_\lambda \approx \tilde\delta_\lambda^2$ is refuted in the toy model. $\square$

**Remark 5.4 (mechanism).** The structural reason for the absorption is the identity
$$K_0(s) = -\tfrac{1}{2}\,\partial_{\gamma_0}\Bigl(\frac{-4\gamma_0}{s^2-\gamma_0^2}\Bigr) = -\tfrac{1}{2}\,\partial_{\gamma_0}\,\hat t_0(s),$$
where $\hat t_0$ is the tangent kernel (3.1) at $\gamma_0$: the leading density of $d\nu$ is the **derivative of the tangent field with respect to the position of the zero** — a second-jet object (curvature, second fundamental form of Doc 93 §6), which is not in the span of the tangents at the fixed zeros $\{\gamma_j\}$, but is in its closure **once collective reorganization of distant zeros is allowed** (Lemma 4.1 + Lemma 4.3). The absorption is necessarily **delocalized**: no finite movement of zeros near $\gamma_0$ realizes it; the minimizing sequences spread the correction over tails of zeros escaping to infinity.

---

## §6. Object (iv): the contribution of the quadruple to the negative index $\kappa$

We work within the framework of Doc 91/96: $(\mathcal{K},Q)$ the Weil–Connes Pontryagin space, $H_C$ the $Q$-self-adjoint operator whose eigenvalues are $\rho - 1/2$ for $\rho$ a zero of $\xi$ (Doc 96, Prop. 4.10).

**Proposition 6.1 (The subspace $\mathcal{K}_{\mathrm{off}}$ of the quadruple).** In the toy model:

(a) The eigenvalues of $H_C$ off $i\mathbb{R}$ are exactly the four numbers
$$z_1 = \delta + i\gamma_0,\quad \bar z_1 = \delta - i\gamma_0,\quad z_2 = -\delta + i\gamma_0,\quad \bar z_2 = -\delta - i\gamma_0,$$
with eigenvectors $v_{z_1}, v_{\bar z_1}, v_{z_2}, v_{\bar z_2}$ (simple, by (T1)). The subspace of Theorem 8.1 of Doc 96 is
$$\mathcal{K}_{\mathrm{off}} = \mathrm{span}\{v_{z_1}, v_{\bar z_1}, v_{z_2}, v_{\bar z_2}\}, \qquad \dim \mathcal{K}_{\mathrm{off}} = 4.$$

(b) For $H_C$ $Q$-self-adjoint with eigenvalues $\lambda,\mu$: $Q(v_\lambda, v_\mu) = 0$ unless $\mu = \bar\lambda$. In particular each eigenvector is $Q$-neutral: $Q(v_{z_i},v_{z_i}) = 0$.

(c) In the ordered basis $(v_{z_1}, v_{\bar z_1}, v_{z_2}, v_{\bar z_2})$, the Gram matrix of $Q|_{\mathcal{K}_{\mathrm{off}}}$ is block-diagonal with two hyperbolic blocks:
$$G(\delta) = \begin{pmatrix} 0 & q_1 & & \\ \bar q_1 & 0 & & \\ & & 0 & q_2 \\ & & \bar q_2 & 0 \end{pmatrix}, \qquad q_i = q_i(\delta) \neq 0,$$
with eigenvalues $\pm|q_1|, \pm|q_2|$: signature $(2,2)$.

(d) Hence
$$\boxed{\;\kappa = \mathrm{neg.ind}\bigl(Q|_{\mathcal{K}_{\mathrm{off}}}\bigr) = 2 \quad \text{for every } \delta\in(0,1/2),\;}$$
**independent of $\delta$**, and discontinuous at $\delta = 0$ (where $\kappa = 0$). Consistent with the bridge theorem P35 ($\kappa = 2m$ with $m = 1$ quadruple) and with Doc 96, Prop. 2.14 ($\dim\mathcal{K}_{\mathrm{zeros}} = 2\kappa = 4$).

*Proof.* (a) Doc 96, Prop. 4.10 and Theorem 8.1: the non-$i\mathbb{R}$ eigenvalues are $\rho-1/2$, $\rho\in Z_\delta$. (b) $Q(H_Cv_\lambda, v_\mu) = Q(v_\lambda, H_Cv_\mu)$ gives $\lambda\,Q(v_\lambda,v_\mu) = \bar\mu\,Q(v_\lambda,v_\mu)$ (with $Q$ Hermitian, antilinear in the second entry), hence $Q(v_\lambda,v_\mu)=0$ if $\lambda\neq\bar\mu$. With $\lambda=\mu$ non-real: $Q(v_\lambda,v_\lambda)=0$. (c) By (b), the only possible nonzero pairings are $\{z_1,\bar z_1\}$ and $\{z_2,\bar z_2\}$ ($\overline{z_1} = \bar z_1 \neq z_2, \bar z_2$). If some $q_i$ were $0$, $Q$ would be degenerate on $\mathcal{K}_{\mathrm{off}}$, contradicting the non-degeneracy of the $Q$-orthogonal decomposition of Doc 96, Theorem 8.1 (a vector $Q$-orthogonal to $\mathcal{K}_{\mathrm{off}}$ and to $\mathcal{K}_{\mathrm{crit}}$ would be $Q$-orthogonal to all of $\mathcal{K}$). Each $2\times2$ block of the form $\bigl(\begin{smallmatrix}0&q\\ \bar q&0\end{smallmatrix}\bigr)$ has eigenvalues $\pm|q|$: signature $(1,1)$ — the canonical hyperbolic block of the theory of indefinite scalar products ([GLR83], Ch. I). (d) Sum of the two blocks: $\mathrm{sig} = (2,2)$, $\kappa = 2$; $\dim\mathcal{K}_{\mathrm{off}} = 4 = 2\kappa$. $\square$

**Remark 6.2 (pairing convention).** Some presentations of the Weil form pair $\rho \leftrightarrow 1-\bar\rho$, that is $z \leftrightarrow -\bar z$ (which in the quadruple pairs $z_1 \leftrightarrow z_2$). Under either convention the Gram matrix consists of **two hyperbolic planes** over a dimension-4 space and $\kappa = 2$: conclusion (d) is robust. The choice of convention does affect which fine decomposition into planes is canonical; see §8 (failure of the fine map). GAP G5: the correct convention for the $Q$ of Doc 91 is not fixed here.

**Remark 6.3 (what the generators are).** In the Mellin model, $v_{z}$ is (formally) the class in $\mathcal{K}$ of the residual functional $f \mapsto \hat f(1/2+z)$ at the corresponding zero: the generators of $\mathcal{K}_{\mathrm{off}}$ are **rigidly indexed by the four zeros of the quadruple** — frequency $\pm\gamma_0$ and displacement $\pm\delta$. They do not depend on any optimization: they are pointwise spectral data.

---

## §7. Object (v): the Maslov index of the crossing $\delta: 0 \to \delta_0$

**Definition 7.1 (family of forms of the crossing).** Under (T4), let $V(\delta) \subset \mathcal{K}$ be the spectral subspace (Riesz projection) of $H_C(\delta)$ associated with the cluster of eigenvalues near $\{\pm i\gamma_0\}$, for $\delta \in [0,\delta_0]$, identified with a fixed space $V \cong \mathbb{C}^4$ via the family of projections (Kato). Let $G(\delta) = Q|_{V(\delta)}$ be the resulting family of $4\times4$ Hermitian forms. We define the **Maslov index of the crossing** as the spectral flow
$$\mu_{\mathrm{crossing}} := \mathrm{sf}\bigl(\{G(\delta)\}_{\delta\in[0,\delta_0]}\bigr)$$
(net number of eigenvalues of $G(\delta)$ crossing $0$, counted with sign; Robbins–Salamon convention [RS93]).

**Proposition 7.2 (computation of the crossing).** Under (T1)–(T4) and regularity of the family (GAP G4 below):

(a) For $\delta > 0$: $\mathrm{sig}\,G(\delta) = (2,2)$ (Proposition 6.1(c)).

(b) For $\delta = 0$: the four zeros collapse into the two critical double zeros $1/2\pm i\gamma_0$. The contribution of a critical zero of multiplicity 2 to the Weil form is $2\,|\hat f(\rho_0)|^2$: rank 1 and positive pointwise. On the 4-dimensional jet space (values and derivatives $\hat f(\rho_0), \hat f'(\rho_0)$ at $\pm\gamma_0$), $G(0)$ has signature $(2,0)$ with 2-dimensional kernel.

(c) Consequently, two eigenvalues of $G(\delta)$ (namely $-|q_1(\delta)|, -|q_2(\delta)|$) emerge from the kernel at $\delta = 0$ toward the negative half-axis:
$$\mu_{\mathrm{crossing}} = -2, \qquad |\mu_{\mathrm{crossing}}| = 2 = \kappa.$$
The crossing occurs exactly at $\delta = 0$ and at no other point of $[0,\delta_0]$ (the $q_i(\delta)\neq 0$ for $\delta>0$).

*Proof (modulo G4).* (a) and non-vanishing for $\delta>0$ are Proposition 6.1. (b): the limiting form only evaluates $\hat f(\rho_0)$ (the zero term of the explicit formula for an on-line zero of multiplicity $m$ is $m\,\hat f(\rho_0)\overline{\hat f(\rho_0)}$); the derivative directions $\hat f'(\rho_0)$ lie in the kernel. (c): counting eigenvalues: signature $(2,2)$ for $\delta>0$, $(2,0)+\mathrm{nul}\,2$ at $\delta=0$; the two negative eigenvalues tend to $0^-$ as $\delta\to0^+$ (continuity of eigenvalues of the Hermitian family), hence the net spectral flow on $[0,\delta_0]$ is $-2$. $\square$

**Detail of the collapse (jet basis).** To make the crossing mechanism explicit: the evaluation functionals at the zeros collapsing at $+\gamma_0$ are $e_\pm(\delta): f \mapsto \hat f(1/2\pm\delta+i\gamma_0)$. The regularized jet basis is
$$x(\delta) = \tfrac{1}{2}\bigl(e_+(\delta)+e_-(\delta)\bigr) \xrightarrow{\delta\to0} \bigl[f\mapsto \hat f(\rho_0)\bigr], \qquad y(\delta) = \tfrac{1}{2\delta}\bigl(e_+(\delta)-e_-(\delta)\bigr) \xrightarrow{\delta\to0} \bigl[f\mapsto \hat f'(\rho_0)\bigr],$$
with $\rho_0 = 1/2+i\gamma_0$. The change of basis $(e_+,e_-)\mapsto(x,\delta y)$ is singular of order $\delta$; in the basis $(x,y)$ the family $G(\delta)$ is continuous and its $2\times2$ minor associated with the $y$ directions vanishes linearly at $\delta = 0$. That the two vanishing eigenvalues do so from the negative side for $\delta>0$ is forced by (a): there is no room for a choice of signs. Uniform control of this rescaling within the full Pontryagin space (not only in the 4-dimensional model) is the content of GAP G4.

**GAP G4 (declared).** The construction of the family $\{G(\delta)\}$ requires: (i) that the Riesz projection of the cluster be continuous in $\delta$ **including** the Jordan degeneracy at $\delta=0$ (the eigenvector basis collapses; one must pass to the jet basis with a rescaling $\sim\delta$ whose control is not carried out here); (ii) the V.1 verification of program P35 ($Q$-self-adjointness of $H_C$ on a precise domain). Without (i)–(ii), Proposition 7.2 is a computation in the finite-dimensional model of the restricted Weil form, not a theorem about $H_C$.

**Remark 7.3 (reading for $\mathbf{C}_D^B$).** Conjecture $\mathbf{C}_D^B$ of Doc 96 (§8.2) proposes $\mu_{\mathbb{A}} = \mu_\infty + \sum_p \mu_p = 0$. The toy model shows the minimal content that any such theory must reproduce: a single quadruple contributes $|\mu| = 2$ concentrated at the crossing $\delta=0$; under RH there is no crossing and $\mu = 0$. The Maslov index of the crossing is, in the toy model, **exactly $\kappa$ with a sign**: the Maslov–Krein identification (Conjecture 3.10 of Doc 96) is verified in dimension 4 trivially, because both sides count the same two hyperbolic planes. The toy model provides no evidence about the genuinely difficult part (local adelic decomposition $\mu = \mu_\infty + \sum_p\mu_p$).

---

## §8. Object (vi): B+D confrontation — the central question

We now have the two objects in the same model:

| | **Direction D: $d\nu^*$** | **Direction B: $(\mathcal{K}_{\mathrm{off}}, Q)$** |
|---|---|---|
| Nature | measure (density in $H_\lambda$) | Pontryagin subspace + form |
| Magnitude | mass $= o(\delta^2)$ (Cor. 5.2) | $\kappa = 2$, integer, $\forall\delta>0$ (Prop. 6.1) |
| Dependence on $\delta$ | continuous, $\to 0$ | constant, discontinuous at $0$ |
| Localization | **delocalized**: the component localized at $\pm\gamma_0$ ($2\delta^2K_0f_0^{on}$) is absorbed by reorganization of distant zeros (Thm. 4.5/5.1) | **rigidly localized** at the quadruple: 4 eigenvectors indexed by $\pm\delta\pm i\gamma_0$ (Remark 6.3) |
| Fine structure | no known canonical decomposition | 2 hyperbolic planes (convention-dependent, Remark 6.2) |
| Vanishing | $d\nu^* = 0 \iff \delta = 0$ | $\mathcal{K}_{\mathrm{off}} = 0 \iff \delta = 0$ |

**Theorem 8.1 (Failure of the strong correspondence $d\nu^* \leftrightarrow \mathcal{K}_{\mathrm{off}}$).** In the toy model, under (T1)–(T3) (and (H-ND1) wherever $d\nu^*$ is invoked as a realized object):

(a) **The magnitudes do not agree at leading order in $\delta^2$, nor at any order.** $\kappa = 2$ is an integer invariant independent of $\delta$, while $\mathrm{mass}_{H_\lambda}(d\nu^*) \leq \tilde\delta_\lambda = o(\delta^2)$. There is no function $c(\gamma_0,\lambda) > 0$ such that $\mathrm{mass}(d\nu^*) = c\cdot\kappa\cdot\delta^2 + o(\delta^2)$: the coefficient of $\delta^2$ on side D is **zero**, while that of side B (normalized in any non-trivial way in $\delta$) is not.

(b) **The localization does not agree.** The trace of the quadruple in $d\nu$ at order $\delta^2$ — the kernel $K_0$ concentrated at the frequencies $\pm\gamma_0$ — is exactly the part that the optimization of Direction D **eliminates** (Corollary 5.2(a)): it is absorbed by a delocalized deformation (tails of distant zeros). What remains ($d\nu^*$) has, at leading order, no effective support identifiable with the frequencies of the quadruple. By contrast, $\mathcal{K}_{\mathrm{off}}$ is supported exactly at the quadruple and is not deformable: the negative index cannot be "absorbed" by moving on-line zeros, because it depends only on the non-$i\mathbb{R}$ eigenvalues of $H_C$.

(c) **There is no natural map.** A map $\Phi$ sending the 2 hyperbolic planes of $\mathcal{K}_{\mathrm{off}}$ to components of $d\nu^*$ with comparable masses cannot exist: the domain has fixed dimension-4 structure and the codomain is evanescent of higher order. Even at the level of $d\nu$ (not optimized), the natural decomposition of the leading density is by frequencies $\{+\gamma_0, -\gamma_0\}$ (the two double poles of $K_0$), while the hyperbolic planes of $Q$ pair eigenvectors **across** the frequencies ($z_1$ with $\bar z_1$, i.e. $+\gamma_0$ with $-\gamma_0$, in the convention of Prop. 6.1(b)): the fine decompositions do not correspond canonically (and the one on side B depends on the convention, Remark 6.2).

(d) **The only thing that coincides is simultaneous vanishing:** $d\nu^* = 0 \iff \delta = 0 \iff \mathcal{K}_{\mathrm{off}} = 0$. But this is tautological: each side is separately equivalent to RH-in-the-toy-model (side D: Doc 82/Theorem 7.5 of Doc 97 under H-ND1+ND2; side B: Doc 96, Cor. 8.2), so the "coincidence" goes through RH and does not constitute a bridge with content of its own.

*Proof.* (a) Corollary 5.2(b) + Proposition 6.1(d). (b) Theorem 4.5, Corollary 5.2(a), Remark 5.4, Remark 6.3. (c) consequence of (a) (magnitudes) and of the pairing analysis in (b)/Remark 6.2. (d) the two cited equivalences. $\square$

**Conclusion without detours.** **The B+D connection, in its conjectured form ("the irreducible part $d\nu^*$ is the variational avatar of the localization of the negative index in $\mathcal{K}_{\mathrm{off}}$, with magnitudes coinciding at leading order"), is dead.** The toy model refutes it in the most favorable case possible: a single quadruple, exact expansions, no interference between off-critical zeros.

**Theorem 8.2 (What does survive: correspondence $\mathcal{K}_{\mathrm{off}} \leftrightarrow d\nu$, not $d\nu^*$).** In the toy model, the object of Direction D that does correspond structurally to $\mathcal{K}_{\mathrm{off}}$ is the **fixed-reference** residual $d\nu = (f_0-f_0^{on})\,dm_\infty$ (Doc 89), not the optimized one:

(a) Magnitudes: $\mathrm{mass}_{H_\lambda}(d\nu) = 2\delta^2\|K_0f_0^{on}\|_{H_\lambda} + O(\delta^4) \asymp \delta^2$, and $T_\lambda = \int W_\lambda\,d\nu \geq 2\delta^2K_\lambda(\gamma_0)$ (Doc 86): scale $\delta^2$, the square of the displacement — the same power governing the opening of the hyperbolic planes ($z_i - i(\pm\gamma_0) = \pm\delta$) and the Jordan splitting of the Maslov crossing (§7), which are second-order phenomena in the non-self-adjointness (cf. P35, $\kappa = 2m$).

(b) Localization: the leading density $2\delta^2K_0f_0^{on}$ has its two resonances at $\pm\gamma_0$, indexed by the same quadruple generating $\mathcal{K}_{\mathrm{off}}$; the count "2 kernel resonances $\leftrightarrow$ 2 hyperbolic planes $\leftrightarrow$ $\kappa = 2$" is exact in the toy model (with the caveat about fine pairing of (c) above).

(c) Vanishing: $d\nu = 0 \iff \delta = 0 \iff \kappa = 0$, and here the equivalence on side D is **unconditional** (Doc 83, Cor. 1.2), without H-ND1/ND2.

*Proof.* (a) Proposition 2.3 and Doc 86. (b) Proposition 2.2 and Proposition 6.1. (c) Doc 83 and Doc 96. $\square$

**Structural moral.** The passage from $d\nu$ to $d\nu^*$ — that is, the optimization over $\mathcal{M}$ defining Direction D in its Doc 97 version — **destroys** the localized information that the Pontryagin space sees. The B+D bridge must be built (if it exists) between $(\mathcal{K}_{\mathrm{off}}, Q)$ and the fixed-reference objects ($d\nu$, $T_\lambda$, the kernels $K_\lambda(\gamma_j)$ of Doc 86), not with the shadow minimizer. This downgrades the interest of the Doc 97 program for the B+D front, and simultaneously revalues the Doc 83–86–89 line (P39).

---

## §9. Declared open gaps

- **G1 (structural hypotheses).** (W-pol) and (W-par) are cited from the CCM framework (Docs 82, 83, 95) with no new proof here. If $W_\lambda$ were not even, Lemma 3.1 changes (the odd equations cease to be vacuous), but the corrections of §3.1–3.2 regarding the admissible variation remain.
- **G2 (attainment of the infimum).** It is not determined whether $\tilde\delta_\lambda$ is attained in $\overline{\mathcal{M}}$ in the toy model; Theorem 5.1 is an upper bound via explicit minimizing sequences, sufficient for all of §8. (H-ND1) remains conditional.
- **G3 (exact rate).** $\mathrm{mass}(d\nu^*) = o(\delta^2)$ is proved; the natural conjecture is $O(\delta^4)$ (the next exact term $\delta^4E_\delta f_0^{on}$ of (2.4) contains the component $Q_4f_0^{on} = G$, possibly also absorbable — not analyzed). Quantifying $C_\epsilon$ of Theorem 5.1 (polynomial degree vs. $\epsilon$, weighted approximation theory) would decide the rate.
- **G4 (regularity of the Maslov family).** Continuity of $\{G(\delta)\}$ across the Jordan degeneracy at $\delta=0$, and the V.1 verification of P35, remain open; Proposition 7.2 is a computation in the finite-dimensional model of the Weil form.
- **G5 ($Q$-pairing convention).** $\lambda\leftrightarrow\bar\lambda$ vs. $\lambda\leftrightarrow-\bar\lambda$ (Remark 6.2); $\kappa=2$ is robust, the fine plane structure is not.
- **G6 (non-vanishing of the corrected EL at $f_0^{on}$).** With the even kernel (3.2), $\mathrm{EL}_j(f_0^{on}) = 2\delta^2\int W_\lambda (f_0^{on})^2 K_0(s)\,\frac{\gamma_j}{s^2-\gamma_j^2}\,dm_\infty + O(\delta^4)$; the kernel $\gamma_j/(s^2-\gamma_j^2)$ changes sign at $|s|=\gamma_j$ and the generic non-vanishing of these integrals (which would restore Lemma 4.6 of Doc 95 in its corrected form) is not proved here.

---

## §10. VERDICT

**ROUTE CLOSED** — for the strong B+D correspondence as formulated (irreducible object $d\nu^*$ of Direction D $\leftrightarrow$ localization of the negative index in $\mathcal{K}_{\mathrm{off}}$ of Direction B, with a natural map and magnitudes coinciding at leading order in $\delta^2$).

**Precise reason.** In the single-quadruple toy model: (1) the magnitudes live at incompatible scales — $\kappa = 2$ is an integer independent of $\delta$ (Prop. 6.1), while the mass of $d\nu^*$ is $o(\delta^2)$ (Theorem 5.1, Cor. 5.2), so the coefficient of $\delta^2$ on side D is null and cannot equal anything non-trivial on side B; (2) the localization is opposite — $\mathcal{K}_{\mathrm{off}}$ is rigidly anchored to the quadruple, while the component of $d\nu$ localized at $\pm\gamma_0$ is exactly what the variational optimization absorbs via delocalized reorganization of distant on-line zeros (Theorem 4.5); (3) the only remaining coincidence (simultaneous vanishing) is tautological via RH.

**What the test rescues** (does not alter the verdict, orients the program):
1. The living correspondence is $\mathcal{K}_{\mathrm{off}} \leftrightarrow d\nu$ (fixed reference, Doc 89/P39): same scale $\delta^2$, same indexing by the quadruple, unconditional vanishing equivalence (Theorem 8.2). The B+D front must be reformulated over $d\nu$ and $T_\lambda$, not over $g^*$/$d\nu^*$.
2. Absorption theorem (Theorem 5.1): $\tilde\delta_\lambda = o(\delta^2)$, with constructive failure of ND1 in the toy model and quantitative separation $T_\lambda \asymp \delta^2$ vs. $\tilde\delta_\lambda^2 = o(\delta^4)$ (Prop. 5.3) — the program's two functionals are not interchangeable.
3. Two internal corrections proved: the EL kernel of Docs 95/97 is odd and vacuous by parity (Lemma 3.1; correct kernel in (3.2)); the second transversal variation of Doc 93 has the wrong sign due to a parametrization error ($\psi''(0) = -8\mathcal{Q}_\lambda^{(0)} < 0$: $f_0^{on}$ is a local maximum in the genuine normal direction, Prop. 3.5). Downstream results that depended on "convexity of $\mathcal{M}$ toward $f_0$" (Doc 93 §6, Doc 95 §1.3) must be revised.
4. The Maslov index of the crossing equals $|\mu| = 2 = \kappa$ in the toy model (Prop. 7.2, modulo G4): a minimal benchmark datum for any future adelic theory $\mathbf{C}_D^B$.

---

## Appendix A: Notation of the document

| Symbol | Meaning | Reference |
|---|---|---|
| $Z_\delta$ | off-critical quadruple $\{1/2\pm\delta\pm i\gamma_0\}$ | (T1) |
| $f_0,\ f_0^{on}$ | $|\zeta(1/2+is)|^2$, $|\zeta_{\mathrm{on}}(1/2+is)|^2$ | Docs 82, 83 |
| $G(s)$ | regular part: $f_0^{on} = (s^2-\gamma_0^2)^4G$, $G(\pm\gamma_0)>0$ | (1.1) |
| $R_{\gamma_0,\delta}$ | quadruple factor $f_0/f_0^{on}$ | (2.1) |
| $K_0(s)$ | $\frac{1}{(s-\gamma_0)^2}+\frac{1}{(s+\gamma_0)^2} = \frac{2(s^2+\gamma_0^2)}{(s^2-\gamma_0^2)^2}$ | Prop. 2.2; Doc 93, Lemma 2.3 |
| $d\nu$ | $(f_0-f_0^{on})\,dm_\infty \geq 0$ (fixed reference) | Doc 83, Cor. 1.3; Doc 89 |
| $d\nu^*$ | $(f_0-g^*)\,dm_\infty$ (optimized reference) | Doc 97, Def. 2.1 |
| $\nu_2$ | leading density $2K_0f_0^{on}$ of $d\nu/\delta^2$ | (2.5) |
| $t_j$ | admissible tangent vector $-4m_j\gamma_j\,g_\Gamma/(s^2-\gamma_j^2)$ | Lemma 3.3 |
| $\mathcal{T},\ \mathcal{T}_{\mathrm{pol}}$ | closed tangent cone; subspace of polynomial directions $f_0^{on}s^{2k}$ | §4.1, Lemma 4.1 |
| $\mu_\star$ | $W_\lambda\,(f_0^{on})^2\,dm_\infty$ (approximation measure) | Lemma 4.3 |
| $\tilde\delta_\lambda$ | variational distance $\inf_{g\in\mathcal{M}}\|f_0-g\|_{H_\lambda}$ | Doc 82 |
| $\mathcal{K}_{\mathrm{off}}$ | Pontryagin subspace of the quadruple, $\dim 4$ | Doc 96, Thm. 8.1; Prop. 6.1 |
| $q_i(\delta)$ | hyperbolic pairings $Q(v_{z_i}, v_{\bar z_i})$ | Prop. 6.1(c) |
| $\kappa$ | negative index $\mathrm{neg.ind}(Q|_{\mathcal{K}_{\mathrm{off}}}) = 2$ | Prop. 6.1(d); P35 |
| $G(\delta)$ | Gram family of the crossing over $V\cong\mathbb{C}^4$ | Def. 7.1 |
| $\mu_{\mathrm{crossing}}$ | spectral flow of $G(\delta)$ on $[0,\delta_0]$, $=-2$ | Prop. 7.2 |
| $\mathcal{Q}_\lambda^{(0)}$ | second-variation coefficient in the direction of the quadruple | Prop. 3.5; Doc 93, Def. 4.1 |

## Appendix B: Table of logical dependencies of the main results

| Result | Unconditional in the toy model | Hypotheses used |
|---|---|---|
| Prop. 2.1–2.3, Cor. 2.4 ($R$, $d\nu$, masses) | yes | (T1), (W-pos), (W-pol) |
| Lemma 3.1 (odd EL vacuous) | yes | (W-par) |
| Lemma 3.3, eq. (3.2) (corrected EL) | yes | (T1) |
| Prop. 3.5 ($\psi''(0)<0$, correction to Doc 93) | yes | (T1)–(T3) |
| Theorem 4.5 / Theorem 5.1 (absorption, $\tilde\delta_\lambda = o(\delta^2)$) | yes | (T1)–(T3) + [A65] |
| Cor. 5.2 (structure of $d\nu^*$) | partial | + (H-ND1) to speak of realized $d\nu^*$ |
| Prop. 6.1 ($\kappa=2$) | yes, given the Doc 91/96 framework | V.1 of P35 implicit in "$H_C$ is $Q$-self-adjoint" |
| Prop. 7.2 (Maslov $=-2$) | finite-dim. model | (T4) + GAP G4 |
| Theorem 8.1 (non-correspondence) | yes | union of the above |
| Theorem 8.2 (correspondence with $d\nu$) | yes | (T1)–(T3) + Doc 96 framework |

---

## References

- [A65] N. I. Akhiezer, *The Classical Moment Problem and Some Related Questions in Analysis*, Oliver & Boyd, 1965. (M. Riesz's theorem: density of polynomials for determinate measures; Carleman's criterion.)
- [GLR83] I. Gohberg, P. Lancaster, L. Rodman, *Matrices and Indefinite Scalar Products*, Birkhäuser, 1983. (Canonical forms of Hermitian pairs $(G, H)$; hyperbolic blocks.)
- [AI89] T. Ya. Azizov, I. S. Iokhvidov, *Linear Operators in Spaces with an Indefinite Metric*, Wiley, 1989. (Pontryagin theory; spectral $Q$-orthogonality.)
- [RS93] J. Robbins, D. Salamon, *The Maslov index for paths*, Topology 32 (1993), 827–844. (Spectral flow and Maslov index conventions.)
- [T86] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. (rev. D. R. Heath-Brown), Oxford, 1986. (Convexity bound on the critical line.)
- Internal program documents: Docs 82, 83, 86, 89, 91, 93, 95, 96, 97 (Phases 33–34); Papers P35 (bridge theorem $\kappa = 2m$), P39 (criterion $T_\lambda = 0\;\forall\lambda \iff$ RH).

---

*End of Doc 98.*
