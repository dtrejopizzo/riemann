# Phase 29 — Doc 34: Direction C — The Phragmén-Lindelöf Principle for the Quotient $Q$

**Direction:** C (analysis of the function $Q = C_\infty/\Xi$ in the strip $|\Im z| \leq 1/2$)
**Objective:** Use the Phragmén-Lindelöf principle to control the quotient $Q(z) = C_\infty(z)/\Xi(z)$ in the strip of analyticity $\mathcal{S} = \{z \in \mathbb{C}: |\Im z| < 1/2\}$. The hypothesis that $Q$ be holomorphic on $\mathbb{R}$ is equivalent to Inc. Inv.; the hypothesis that $Q$ be holomorphic on all of $\mathcal{S}$ is equivalent to RH.

---

## 1. Definition and basic properties of the quotient

**Definition (Doc 29, §3).** The spectral quotient is:

$$Q(z) := \frac{C_\infty(z)}{\Xi(z)},$$

where $C_\infty(z) = w(z) - \Psi(z)$ (CCM limit potential, Doc 19) and $\Xi(z) = \xi(1/2 + iz)$ (Riemann's $\xi$ function in the variable $t = z$).

**Proposition 1** (meromorphy of $Q$ on $\mathcal{S}$).

(a) $C_\infty(z)$ is analytic on $\mathcal{S}$ (Proposition 1, Doc 19).

(b) $\Xi(z) = \xi(1/2+iz)$ is entire (no poles in $\mathbb{C}$).

(c) Hence $Q(z) = C_\infty(z)/\Xi(z)$ is meromorphic on $\mathcal{S}$, with poles exactly at the zeros of $\Xi$ in $\mathcal{S}$.

**Proposition 2** (zeros of $\Xi$ in $\mathcal{S}$ and RH). A point $z_0 \in \mathcal{S}$ satisfies $\Xi(z_0) = 0$ iff $1/2 + iz_0$ is a non-trivial zero of $\zeta$. Under RH: all zeros of $\zeta$ have $\Re(s) = 1/2$, so $\Im(z_0) = 0$, that is, $z_0 \in \mathbb{R} \cap \mathcal{S}$. In the absence of RH: there may be zeros of $\Xi$ in the interior of $\mathcal{S}$.

**Proposition 3** (pole of $Q$ iff failure of Inc. Inv./RH).

- $Q$ has a pole at $z_0 \in \mathbb{R}$ iff $\Xi(z_0) = 0$ and $C_\infty(z_0) \neq 0$ iff $z_0 = \gamma_n$ for some $n$ with $C_\infty(\gamma_n) \neq 0$ iff Inc. Inv. fails at $z_0$.

- $Q$ has a pole at $z_0 \in \mathcal{S} \setminus \mathbb{R}$ iff $\Xi(z_0) = 0$ (a zero of $\zeta$ off the critical line) iff RH fails.

**Corollary 1** (equivalences with $Q$ holomorphic). The following are equivalent:

(i) $Q$ is holomorphic on $\mathbb{R}$ (no poles on the real axis): Inc. Inv.

(ii) $Q$ is holomorphic on all of $\mathcal{S}$: RH.

(iii) $Q$ is holomorphic on $\mathcal{S}$: $\{C_\infty = 0\} = \{\Xi = 0\}$ on $\mathcal{S}$.

---

## 2. The Phragmén-Lindelöf principle for strips

**Classical PL theorem (Phragmén-Lindelöf for strips).** Let $f$ be holomorphic and continuous on the closed strip $\mathcal{S}_{a,b} = \{z: a \leq \Im z \leq b\}$. Suppose:

(H1) On $\Im z = a$: $|f(x+ia)| \leq M_a$ for all $x \in \mathbb{R}$.

(H2) On $\Im z = b$: $|f(x+ib)| \leq M_b$ for all $x \in \mathbb{R}$.

(H3) Growth bound: $|f(x+iy)| \leq C e^{e^{\alpha|x|}}$ for some constant $\alpha < \pi/(b-a)$ and $C > 0$.

Then: $|f(x+iy)| \leq M_a^{(b-y)/(b-a)} M_b^{(y-a)/(b-a)}$ for all $z = x+iy \in \mathcal{S}_{a,b}$.

**Application to $Q$.** We want to apply PL to $Q(z)$ on $\mathcal{S}_{-1/2,1/2}$ (the full strip of analyticity). To do so we need to verify hypotheses (H1)-(H3).

---

## 3. The lower boundary of the strip: $\Im z = -1/2$

**Evaluation of $C_\infty$ at $\Im z = -1/2$.** For $z = t - i/2$ with $t \in \mathbb{R}$:

$$C_\infty(t-i/2) = w(t-i/2) - 2\sum_p\Lambda(p)p^{-1/2}e^{i(t-i/2)\log p} = w(t-i/2) - 2\sum_p\Lambda(p)p^{-1/2+1/2}e^{it\log p}.$$

But $\sum_p\Lambda(p)p^0 e^{it\log p} = \sum_p\Lambda(p)e^{it\log p}$, which diverges absolutely. The boundary $\Im z = -1/2$ lies OUTSIDE the region of absolute convergence of $\Psi(z) = 2\sum_p\Lambda(p)p^{-1/2}e^{iz\log p}$ (which converges absolutely only for $\Im z > 1/2$).

**The pole of $C_\infty$ at $\Im z = -1/2$.** The archimedean symbol $w(z) = \frac{1}{2i}\psi(\frac{1}{4}+\frac{iz}{2}) + \text{c.c.} - \log\pi$ has poles at $z = i(2k+1)/2$ for $k \in \mathbb{Z}_{\geq 0}$ — the first pole at $z = i/2$ (i.e., $\Im z = 1/2$) and the symmetric one at $z = -i/2$ (i.e., $\Im z = -1/2$).

**Conclusion.** $C_\infty$ has poles at $\Im z = \pm 1/2$. The strip of analyticity of $C_\infty$ is strictly $|\Im z| < 1/2$ — the boundaries $\Im z = \pm 1/2$ are SINGULAR.

This PREVENTS direct application of PL on the closed strip $\overline{\mathcal{S}}$: $Q$ does not extend continuously to $\Im z = \pm 1/2$.

---

## 4. PL on sub-strips $|\Im z| \leq 1/2 - \varepsilon$

**Setup.** For $\varepsilon \in (0, 1/2)$, let $\mathcal{S}_\varepsilon = \{z: |\Im z| \leq 1/2-\varepsilon\}$ be the compact sub-strip.

**Proposition 4** (behavior of $Q$ at $\Im z = \pm(1/2-\varepsilon)$). For $z = t \pm i(1/2-\varepsilon)$ with $t \in \mathbb{R}$ and $|t| \to \infty$:

(a) $|C_\infty(t\pm i(1/2-\varepsilon))| \leq 2\sum_\rho |\rho|^{-1-(1/2-\varepsilon)}\cdot 1 = 2\sum_\rho |\rho|^{-3/2+\varepsilon}$, which is absolutely convergent for $\varepsilon < 1/2$ (the zeros of $\zeta$ satisfy $|\rho| \geq 1$ and $\sum|\rho|^{-3/2+\varepsilon}$ converges). In particular, $|C_\infty|$ is BOUNDED at $\Im z = \pm(1/2-\varepsilon)$ for $\varepsilon > 0$.

(b) $|\Xi(t\pm i(1/2-\varepsilon))| = |\xi(1/2 + i(t\pm i(1/2-\varepsilon)))| = |\xi(\varepsilon \pm it)|$ or $|\xi(1-\varepsilon\pm it)|$.

For $t\to\infty$: $|\xi(\varepsilon + it)| \sim C|t|^{1/2-\varepsilon}|\zeta(\varepsilon+it)| \cdot \text{Gamma factor}$.

Since $|\zeta(\varepsilon+it)| = O(|t|^\sigma)$ for some $\sigma > 0$: $|\Xi(t\pm i(1/2-\varepsilon))| \to \infty$ as $t\to\infty$ (polynomially).

**Proposition 5** (bound for $Q$ at the sub-strip boundaries). For $z = t + i\eta$ with $|\eta| = 1/2-\varepsilon$ and $|t| \to \infty$:

$$|Q(t+i\eta)| = \frac{|C_\infty(t+i\eta)|}{|\Xi(t+i\eta)|} \leq \frac{C_\varepsilon}{|t|^{1/2-\varepsilon-\delta}} \to 0 \quad \text{as } |t| \to \infty,$$

for some $\delta > 0$ (using the bound $|C_\infty| \leq C$ bounded and $|\Xi| \to \infty$ polynomially).

*Proof.* $|C_\infty(t+i\eta)| \leq 2\sum_\rho|\rho|^{-3/2+\varepsilon}$ = a finite constant $C_\varepsilon > 0$. And $|\Xi(t+i\eta)| \geq c|t|^{1/2-\varepsilon-\delta}$ for large $|t|$ (from the standard estimates of $\xi$ on the line $\Re s = \varepsilon$, using the functional equation $\xi(s)=\xi(1-s)$). $\square$

---

## 5. Applying PL on the sub-strip

**Setup.** For fixed $\varepsilon > 0$, $Q$ is meromorphic on $\mathcal{S}_\varepsilon$ (with possible poles where $\Xi = 0$). If $Q$ turns out to be holomorphic on $\mathcal{S}_\varepsilon$: the hypotheses of PL are:

(H1) At $|\Im z| = 1/2-\varepsilon$: $|Q| \to 0$ as $|z| \to \infty$ (Proposition 5). $\Rightarrow$ $|Q|$ is BOUNDED on the boundaries by some constant $M_\varepsilon < \infty$.

(H2) Growth bound: $Q$ is meromorphic on $\mathcal{S}_\varepsilon$; if holomorphic, it satisfies $|Q(x+iy)| \leq \exp(\exp(\alpha|x|))$ for some $\alpha > 0$ (from the meromorphy of $C_\infty/\Xi$).

**PL theorem applied to $Q$ on $\mathcal{S}_\varepsilon$.** If $Q$ is holomorphic on $\mathcal{S}_\varepsilon$ (no poles):

$$|Q(z)| \leq M_\varepsilon^{1-|\Im z|/(1/2-\varepsilon)} \cdot M_\varepsilon^{|\Im z|/(1/2-\varepsilon)} = M_\varepsilon \quad \forall\, z \in \mathcal{S}_\varepsilon.$$

(In this case the bound is uniform: $Q$ is bounded on all of $\mathcal{S}_\varepsilon$.)

**Corollary 2** (RH implies $Q$ bounded on every sub-strip). Under RH: $Q$ is holomorphic on $\mathcal{S}_\varepsilon$ for all $\varepsilon > 0$ (no zeros of $\Xi$ off $\mathbb{R}$). By PL: $Q$ is uniformly bounded on each $\mathcal{S}_\varepsilon$.

**Corollary 3** (failure of RH implies $Q$ unbounded). If RH fails: there exists a zero $z_0$ of $\Xi$ with $0 < |\Im z_0| < 1/2$. Then $Q$ has a pole at $z_0$ and $|Q(z)| \to \infty$ as $z \to z_0$.

---

## 6. PL as a detection tool, not a proof tool

**The logical problem with PL here.** The PL theorem can be used in two modes:

**CONSEQUENCE mode:** Assume $Q$ holomorphic $\Rightarrow$ PL gives a bound. (Useful if we already know $Q$ is holomorphic, to deduce properties.)

**PROOF-of-holomorphy mode:** Assume boundedness at the boundaries $\Rightarrow$ PL gives holomorphy in the interior. (WRONG: PL does not prove holomorphy; it only bounds functions that are already holomorphic.)

To prove Inc. Inv. (= $Q$ holomorphic on $\mathbb{R}$): we need the Proof mode. But PL requires $Q$ to ALREADY BE HOLOMORPHIC on the domain.

**Conclusion.** PL, as it stands, cannot PROVE that $Q$ is holomorphic on $\mathbb{R}$. It can only:

(a) Give bounds for $Q$ IF it is assumed to be holomorphic (Corollaries 2-3).

(b) Give a negative CHARACTERIZATION: if $Q$ is not holomorphic on $\mathbb{R}$, the PL bounds on the sub-strip boundaries are not satisfied in a certain way.

---

## 7. The reverse argument: boundedness implies holomorphy

**The tool: Riemann's theorem on removable singularities.** If $Q$ is meromorphic on $\mathcal{S}_\varepsilon$ and bounded in a neighborhood of each point $z_0 \in \mathbb{R}$ with $\Xi(z_0) = 0$: then $z_0$ is a REMOVABLE singularity of $Q$, and $Q$ extends holomorphically to $z_0$.

Hence: to prove Inc. Inv. (holomorphy of $Q$ on $\mathbb{R}$), it suffices to show that $Q$ is LOCALLY BOUNDED at each $\gamma_n$.

**Proposition 6** (local boundedness of $Q$ at $\gamma_n$). $Q$ is bounded in a neighborhood of $\gamma_n$ iff $C_\infty(\gamma_n) = 0$ (when $\Xi(\gamma_n) = 0$ and the singularity is removable) iff Inc. Inv. holds at $\gamma_n$.

*Proof.* If $\Xi(\gamma_n) = 0$ with multiplicity 1 and $C_\infty(\gamma_n) \neq 0$: $Q(z) \sim C_\infty(\gamma_n)/[\Xi'(\gamma_n)(z-\gamma_n)] \to \infty$ as $z \to \gamma_n$ — unbounded. If $C_\infty(\gamma_n) = 0$: $Q$ is bounded near $\gamma_n$ (the pole cancels). $\square$

**The attempt at reverse-PL.** Suppose we can prove, from the structure of $C_\infty$ and $\Xi$:

(*) $|Q(z)|$ is uniformly bounded on $\mathcal{S}_\varepsilon$ for some $\varepsilon > 0$, INDEPENDENTLY of Inc. Inv.

Then: by Riemann's theorem, $Q$ cannot have poles on $\mathbb{R}$ — so Inc. Inv. would follow.

Can (*) be proved independently?

---

## 8. Attempting a uniform bound for $Q$ without assuming Inc. Inv.

**Proposition 7** (the bound fails because of the poles on $\mathbb{R}$). If Inc. Inv. fails at some $\gamma_{n_0}$: then $|Q(z)| \to \infty$ as $z \to \gamma_{n_0}$, so (*) does not hold. Condition (*) is EQUIVALENT to Inc. Inv. — circular.

**The fundamental obstacle.** The uniform bound (*) cannot be proved independently of Inc. Inv., because the poles of $Q$ on $\mathbb{R}$ are exactly the points where Inc. Inv. fails. Proving (*) requires knowing that there are no poles on $\mathbb{R}$, which is Inc. Inv.

---

## 9. PL in the diagonal direction: bounds on $|Q|$ from growth

**Even so, PL can be used to give conditional bounds.** Suppose:

(A) $Q$ has exactly $K$ poles on $\mathbb{R}$ (that is, Inc. Inv. fails at $K$ points).

(B) Near each pole $z_0 = \gamma_{n_k}$: $|Q(z)| \leq M|z-z_0|^{-1}$ (simple pole).

**Proposition 8** (the regularized quotient $\tilde Q$). Define $\tilde Q(z) = Q(z)\cdot\prod_{k=1}^K (z-\gamma_{n_k})$. If (A) and (B) hold: $\tilde Q$ is holomorphic on $\mathbb{R}$ and meromorphic on $\mathcal{S}_\varepsilon$.

PL applied to $\tilde Q$: if $|\tilde Q|$ is bounded at the sub-strip boundaries, then $|\tilde Q| \leq M_\varepsilon$ on all of $\mathcal{S}_\varepsilon$.

**The bound of the regularizing product.** $\prod_{k=1}^K |z-\gamma_{n_k}|$: at the boundaries $|\Im z| = 1/2-\varepsilon$, this product is $O(1)$ (since the $\gamma_{n_k}$ are finitely many). Hence if $|Q|$ is bounded at the boundaries (is it?), so is $|\tilde Q|$.

**The problem with the "bounded at the boundaries" hypothesis.** At the boundaries $|\Im z| = 1/2-\varepsilon$: $|Q| = |C_\infty|/|\Xi|$. If $\Xi$ has NO zeros at $|\Im z| = 1/2-\varepsilon$ (which depends on the distribution of the zeros of $\zeta$ in the strip, a result not established unconditionally): $Q$ is continuous and $|Q| \to 0$ by Proposition 5.

If $\Xi$ DOES have zeros at $|\Im z| = 1/2-\varepsilon$ (an even stronger violation of RH, zeros at distance $1/2-\varepsilon$ from the critical line): $Q$ also has poles at the boundaries, and the PL hypothesis fails.

---

## 10. A partial result: conditional PL

**Theorem 2** (conditional PL, main result of Direction C). Assuming:

(C1) $\Xi$ has no zeros in the strip $1/2-2\varepsilon \leq |\Im z| \leq 1/2-\varepsilon$ (that is, the possible zeros of $\zeta$ off the critical line are at distance $> \varepsilon$ from the boundary of $\mathcal{S}_\varepsilon$).

(C2) $C_\infty$ is bounded on the strip $|\Im z| \leq 1/2-\varepsilon$ (from Proposition 4(a), this holds with constant $C_\varepsilon$).

Then: $Q = C_\infty/\Xi$ satisfies $|Q| \leq C_\varepsilon/c_\varepsilon$ at the boundaries $|\Im z| = 1/2-\varepsilon$ (where $c_\varepsilon = \min_{|\Im z|=1/2-\varepsilon}|\Xi|$).

And if moreover $Q$ is holomorphic on $\mathcal{S}_\varepsilon$ (no poles, i.e., no zeros of $\Xi$ in the interior): $|Q| \leq C_\varepsilon/c_\varepsilon$ on all of $\mathcal{S}_\varepsilon$ (from PL).

*Proof.* Direct from the PL theorem applied to $Q$ under hypotheses (C1)-(C2). $\square$

**Candor.** Condition (C1) is a hypothesis about the distribution of the zeros of $\zeta$ in the strip, and requires knowledge that is not available unconditionally. The hypothesis "no zeros of $\Xi$ in $\mathcal{S}_\varepsilon$" is exactly RH. Circular again.

---

## 11. Conclusion of Direction C

**What works.** The analysis of $Q = C_\infty/\Xi$ in the strip is an elegant formulation:

- Inc. Inv. ↔ $Q$ holomorphic on $\mathbb{R}$.
- RH ↔ $Q$ holomorphic on $\mathcal{S}$.
- The quotient $Q$ decays to $0$ at the boundaries $|\Im z| = 1/2-\varepsilon$ (Proposition 5) — an unconditional result.

**The structural obstacle.** PL is a tool for BOUNDING holomorphic functions, not for PROVING holomorphy. To prove that $Q$ has no poles on $\mathbb{R}$ (= Inc. Inv.), a DIFFERENT argument is needed — not PL.

**What PL DOES give (candid result).**

Under RH (as a hypothesis): $Q$ is holomorphic on $\mathcal{S}$ and satisfies $|Q| \leq C_\varepsilon$ uniformly on $\mathcal{S}_\varepsilon$, with $C_\varepsilon \to 0$ as $\varepsilon \to 0$. This gives the bound $|Q(t)| = O(1)$ on $\mathbb{R}$ (conditional on RH). Consistent but not probative.

**New geometric observation.** The fact that $|Q(z)| \to 0$ at the boundaries $|\Im z| = 1/2-\varepsilon$ (for every $\varepsilon > 0$) suggests that $Q$ "wants" to be zero at the boundaries of the strip — consistent with Inc. Inv. (the poles on $\mathbb{R}$ being the only obstacle). If one could show that this decay at the boundaries is UNIFORM in $\varepsilon$ (that is, $|Q|$ decays to 0 uniformly as one approaches $\Im z = \pm 1/2$ from the interior): by a limiting argument, $Q$ would vanish at the boundaries of the strip — but the boundaries are not in $\mathcal{S}$.

**Proposal for Phase 31.** The geometry of the decay of $Q$ in the strip deserves study. Specifically: is the decay of $|Q|$ at the boundaries $|\Im z| \to 1/2$ uniform enough to imply, via a subharmonic argument, that $Q$ cannot have poles on $\mathbb{R}$?

---

*Next doc: Doc 35 — Direction D: Eigenvector Delocalization and the Szegő Theorem.*
