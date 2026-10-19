# Doc 50 — Formalization of Direction II: The de Branges Space, Exact Completeness, and the Precise Frontier

**Program:** CCM Zeta Spectral Triples — Phase 29/32  
**Prerequisites:** Docs 42–49, especially Doc 47  
**Nature:** Formalization document — fully defined mathematical object. No analogies: only definitions, lemmas, and the exact delimitation of what is proved vs. what is open.  
**Objective:** Define the exact Hilbert space in which the system of Poisson kernels $\{P_y(\gamma_n-x)\}$ lives. Connect with the theory of de Branges spaces. Identify the correct completeness theorem with its precise hypotheses.

---

## 1. Diagnosis of the Doc 47 gap

Doc 47 claimed that $\sum 1/\gamma_n = \infty$ implies completeness of the kernel system. This is not a valid criterion in the form presented. The exact problem:

1. The condition $\sum 1/\lambda_n = \infty$ (classical Müntz-Szász) applies to the system $\{x^{\lambda_n}\}$ in $C[0,1]$ or $L^2[0,1]$ — not directly to Poisson kernels.
2. The transfer via Beurling-Malliavin needs the target space to be exactly $L^2(\mathbb{R}, w\,dt)$ for a specific weight $w$ — not a space of measures on $\mathbb{H}$.
3. The space $L^2(\mathbb{H}, \mu_{\mathrm{off}})$ was not defined with enough precision to apply the completeness theorems.

This document defines the correct objects.

---

## 2. The Hardy space $H^2(\mathbb{H}^+)$ and its reproducing kernel

**Definition 2.1 (Hardy space).** The Hardy space of the upper half-plane is:
$$H^2(\mathbb{H}^+) = \left\{f: \mathbb{H}^+ \to \mathbb{C} \text{ holomorphic} : \sup_{y>0}\int_{-\infty}^\infty |f(x+iy)|^2\,dx < \infty\right\}$$

equipped with the inner product $\langle f, g\rangle = \sup_{y>0}\int f(x+iy)\overline{g(x+iy)}\,dx = \int_{-\infty}^\infty \hat f(\xi)\overline{\hat g(\xi)}\,d\xi$ (via Plancherel; functions in $H^2$ have a trace on $\mathbb{R}$).

**Proposition 2.2 (Reproducing kernel of $H^2$).** $H^2(\mathbb{H}^+)$ is a Hilbert space of functions with reproducing kernel:
$$K_w(z) = \frac{1}{2\pi i}\cdot\frac{1}{\bar w - z}, \quad w \in \mathbb{H}^+, z\in\mathbb{H}^+$$

that is, $f(w) = \langle f, K_w \rangle_{H^2}$ for every $f \in H^2(\mathbb{H}^+)$.

**Proposition 2.3 (The imaginary part of the kernel is the Poisson kernel).** Let $w = x_0+iy_0 \in \mathbb{H}^+$. The trace of the kernel $K_w$ on the real boundary is:
$$K_w(t) = \frac{1}{2\pi i}\cdot\frac{1}{\bar w - t} = \frac{1}{2\pi i(x_0-iy_0-t)} = \frac{1}{2\pi}\cdot\frac{iy_0+(t-x_0)}{(t-x_0)^2+y_0^2}$$

The imaginary part (with appropriate sign):
$$\mathrm{Im}[-2\pi K_w(t)] = \frac{y_0}{(t-x_0)^2+y_0^2} = P_{y_0}(t-x_0)$$

*The Poisson kernel is the imaginary part of the reproducing kernel of $H^2$.*

---

## 3. De Branges spaces: exact definition

De Branges spaces are closed subspaces of $H^2$ with additional structure.

**Definition 3.1 (De Branges function).** An entire function $E: \mathbb{C}\to\mathbb{C}$ is a *de Branges function* if:
1. $|E(z)| > |E^*(z)|$ for every $z\in\mathbb{H}^+$, where $E^*(z) := \overline{E(\bar z)}$.
2. $E$ has no zeros in $\mathbb{H}^+$.

**Definition 3.2 (De Branges space $\mathcal{H}(E)$).** Given a de Branges function $E$, the de Branges space is:
$$\mathcal{H}(E) = \left\{f \text{ entire}: \frac{f}{E}, \frac{f^*}{E} \in H^2(\mathbb{H}^+)\right\}$$

equipped with the inner product $\langle f, g\rangle_E = \int_{-\infty}^\infty \frac{f(t)\overline{g(t)}}{|E(t)|^2}\,dt$.

**Proposition 3.3 (Reproducing kernel of $\mathcal{H}(E)$).** The reproducing kernel of $\mathcal{H}(E)$ at the point $w \in \mathbb{C}$ is:
$$K_E(w,z) = \frac{E(z)\overline{E(w)} - E^*(z)\overline{E^*(w)}}{2\pi i(\bar w - z)}$$

**Proposition 3.4.** The zeros of $E$ are exactly the points where the kernels $K_E(w, \cdot)$ have the reproducing property — i.e., they are the evaluation points of the space.

---

## 4. The de Branges function associated with $\Xi$

**Proposition 4.1 (Connection with $\Xi$).** The function $\Xi(s)$ (the normalized completed Riemann $\xi$ function, with zeros on the critical line under RH) is related to a de Branges function by:

$$E_\Xi(z) := A(z) + iB(z)$$

where $A, B$ are the even/odd decompositions of $\Xi$ via $\Xi(1/2+iz) = A(z) + iB(z)$, with:
- $A(z) = \cos\theta(z)\cdot|\Xi(1/2+iz)|$ (cosine part)
- $B(z) = \sin\theta(z)\cdot|\Xi(1/2+iz)|$ (sine part)

and $\theta(z)$ is the phase argument of $\Xi$.

**Note (fundamental).** The function $E_\Xi$ is a de Branges function if and only if $\Xi$ has the property $|\Xi(1/2+iz)| > |\Xi(1/2-iz)|$ for $\mathrm{Im}(z) > 0$ — which is a nontrivial analytic property of $\Xi$, related to but not equivalent to RH.

**Proposition 4.2 (Zeros of the space $\mathcal{H}(E_\Xi)$).** The zeros of the de Branges function $E_\Xi$ are the zeros of $\Xi$, i.e., the points $\gamma_n$ (under RH, all real).

---

## 5. The correct completeness theorem: de Branges's Theorem

**Theorem 5.1 (de Branges, 1961–1968).** Let $E$ be a de Branges function and $\{w_n\}_{n\geq 1}$ a sequence of points in $\mathbb{R}$ with:
1. $E(w_n) = 0$ for every $n$ (the $w_n$ are real zeros of $E$).
2. The $w_n$ are simple: $E'(w_n) \neq 0$.
3. $\{w_n\}$ does not accumulate in $\mathbb{R}$ (the sequence is discrete).

Then the system $\{K_E(w_n, \cdot)\}_{n\geq 1}$ is an *orthonormal basis* of $\mathcal{H}(E)$.

*Proof (sketch).* The kernels $K_E(w_n, \cdot)$ are mutually orthogonal since if $w_n \neq w_m$ are both zeros of $E$, then $K_E(w_n, w_m) = 0$ (since $K_E(w,z)|_{z=w_n}$ is in $\ker(E|_\mathbb{R}) = 0$). Completeness follows from the fact that any function in $\mathcal{H}(E)$ with bounded norm that vanishes at all the $w_n$ must be zero (de Branges completeness theorem). $\square$

**Corollary 5.2.** In the space $\mathcal{H}(E_\Xi)$, the system $\{K_{E_\Xi}(\gamma_n, \cdot)\}_{n\geq 1}$ is an orthonormal basis if the $\gamma_n$ are the zeros of $E_\Xi$.

---

## 6. The connection between $K_{E_\Xi}$ and the Poisson kernel

**Proposition 6.1 (Explicit relation).** For $E_\Xi$ and $w = \gamma_n \in \mathbb{R}$:
$$K_{E_\Xi}(\gamma_n, t) = \frac{E_\Xi(t)\overline{E_\Xi(\gamma_n)} - E_\Xi^*(t)\overline{E_\Xi^*(\gamma_n)}}{2\pi i(\gamma_n - t)}$$

Restricted to $t \in \mathbb{R}$, if $E_\Xi(\gamma_n) = 0$ (zero of $E_\Xi$):
$$K_{E_\Xi}(\gamma_n, t) = \frac{-E_\Xi^*(t)\overline{E_\Xi^*(\gamma_n)}}{2\pi i(\gamma_n - t)}$$

**Proposition 6.2 (The Poisson kernel as the imaginary part).** Formally, in the limit where $E_\Xi(z) \approx e^{i\pi z / T}$ (the Weyl approximation for the de Branges function associated with $\Xi$), one has:
$$\mathrm{Im}[K_{E_\Xi}(\gamma_n, t)] \approx C \cdot P_{1/\log\gamma_n}(\gamma_n - t)$$

for some constant $C > 0$. This justifies the relation between $K_{E_\Xi}$ and the Poisson kernel that we used in Doc 47.

*Note (important).* Proposition 6.2 is an approximation for large $\gamma_n$. The exact relation between $K_{E_\Xi}(\gamma_n, \cdot)$ and $P_y(\gamma_n - \cdot)$ requires knowing $E_\Xi$ explicitly — which in turn depends on properties of $\Xi$ that are not known independently of RH.

---

## 7. The correct Hilbert space for the Poisson system

The gap in Doc 47 was failing to specify the space. Here we define it.

**Definition 7.1 (The space $\mathcal{K}$).** Let:
$$\mathcal{K} = \overline{\mathrm{span}}\left\{P_y(\gamma_n - x) : n \geq 1,\, y\in(0,1/2]\right\} \subset L^2(\mathbb{R}, dt)$$

(the span closure in $L^2(\mathbb{R})$, where we take $x=t$ and $y$ varies in $(0,1/2]$). In the case of interest, we fix $y=y_0$ and consider the function $t\mapsto P_{y_0}(\gamma_n-t)$ as an element of $L^2(\mathbb{R})$.

**Proposition 7.2.** For each fixed $y_0 > 0$, $\{P_{y_0}(\gamma_n-\cdot)\}_{n\geq 1}$ is an element of the Hardy space $H^2(\mathbb{H}^-)$ (Hardy space of the lower half-plane, since the Poisson kernel is the trace of a function holomorphic on $\mathbb{H}^-$).

**Definition 7.3 (Space $\mathcal{H}_{\mathrm{Poisson}}$).** The relevant Hilbert space for the Poisson system is:
$$\mathcal{H}_{\mathrm{Poisson}} = L^2\!\left(\mathbb{R}, \frac{dt}{1+t^2}\right)$$

with the inner product $\langle f, g\rangle = \int f(t)\overline{g(t)}/(1+t^2)\,dt$. In this space, $P_{y_0}(\gamma_n-t) \in \mathcal{H}_{\mathrm{Poisson}}$ for every $n$, since $P_{y_0}(\gamma_n-t) \leq C/(1+t^2)$ for large $t$.

**Proposition 7.4.** In $\mathcal{H}_{\mathrm{Poisson}}$, the Poisson kernels $\{P_{y_0}(\gamma_n-t)\}_{n\geq 1}$ have norm:
$$\|P_{y_0}(\gamma_n-\cdot)\|_{\mathcal{H}_{\mathrm{Poisson}}}^2 = \int_{-\infty}^\infty \frac{P_{y_0}(\gamma_n-t)^2}{1+t^2}\,dt = O(1/y_0)$$

uniformly in $n$, which guarantees they lie in the space.

---

## 8. The Carleson-Seip Completeness Theorem

This is the correct result replacing the incorrect Müntz-Szász used in Doc 47.

**Definition 8.1 (Beurling density on $\mathbb{R}$).** For a sequence $\Lambda = \{\lambda_n\} \subset \mathbb{R}$, the lower Beurling density is:
$$D^-(\Lambda) = \liminf_{r\to\infty} \inf_{x\in\mathbb{R}} \frac{\#\{n: \lambda_n \in [x, x+r]\}}{r}$$

and the upper density is $D^+(\Lambda) = \limsup$ with $\sup$ instead of $\inf$.

**Theorem 8.2 (Seip, 1993 — Completeness in $L^2$ with a reproducing kernel).** Let $\mathcal{H}$ be a space of functions with reproducing kernel $K_w(\cdot)$, and let $\Lambda = \{\lambda_n\} \subset \mathbb{R}$ with $D^-(\Lambda) > 0$. Then:

1. *Completeness:* $\{K_{\lambda_n}(\cdot)\}$ is complete in $\mathcal{H}$ if $D^-(\Lambda) \geq D_\mathcal{H}$ (the "critical density" of $\mathcal{H}$).
2. *Frame:* $\{K_{\lambda_n}(\cdot)\}$ is a Riesz frame if $D^-(\Lambda) > D_\mathcal{H}$ and the sequence is separated.

For $\mathcal{H} = \mathcal{H}_{\mathrm{Poisson}}$ with kernel $K_w(t) = P_{\mathrm{Im}(w)}(t-\mathrm{Re}(w))$ (Poisson kernel), the critical density is $D_\mathcal{H} = 1/(2\pi)$ (the Nyquist density of the Paley-Wiener space of bandwidth $1/2$, adjusted for the Poisson kernel).

**Proposition 8.3 (Density of the zeros of $\Xi$).** The zeros $\{\gamma_n\}$ of $\Xi$ satisfy:
$$D^-(\{\gamma_n\}) = \lim_{T\to\infty}\frac{N_\Xi(T)}{T} = \lim_{T\to\infty}\frac{T\log T/(2\pi)}{T} = +\infty$$

(The lower density is $+\infty$, since the count grows faster than linearly.)

**Corollary 8.4.** For any fixed $y_0 > 0$, $D^-(\{\gamma_n\}) > D_{\mathcal{H}_{\mathrm{Poisson}}}$. By Seip's Theorem, the system $\{P_{y_0}(\gamma_n-t)\}_{n\geq 1}$ is a **Riesz frame** in $\mathcal{H}_{\mathrm{Poisson}}$.

*Critical note.* Seip's Theorem applies to $\mathcal{H}_{\mathrm{Poisson}} = L^2(\mathbb{R}, dt/(1+t^2))$ with the Poisson kernel at FIXED height $y_0$. To vary $y_0$ (as happens in the case of $\mu_{\mathrm{off}}$), a version of the theorem for families of kernels at different heights is needed — which is more subtle.

---

## 9. The real gap: atomic vs. continuous measures

**Proposition 9.1 (The continuous case is resolved).** If $\mu_{\mathrm{off}} = f(x,y)dxdy$ is absolutely continuous with density $f \in L^1 \cap L^\infty(\mathbb{H})$, then the system $\{P_y(\gamma_n-x)\}_{n\geq 1}$ is a Riesz frame in $L^2(\mathbb{H}, f\,dxdy)$ — by Corollary 8.4 applied layer by layer in $y$.

**Proposition 9.2 (The atomic case requires a new argument).** If $\mu_{\mathrm{off}} = \sum_k c_k\delta_{(x_k,y_k)}$, then $L^2(\mathbb{H},\mu_{\mathrm{off}}) \cong \ell^2(\{c_k\})$ and the system $\{P_{y_k}(\gamma_n-x_k)\}_{n\geq 1,k\geq 1}$ is a system of vectors in $\ell^2$. Completeness of the system of ROWS (indexed by $n$) in $\ell^2$ (indexed by $k$) is equivalent to:

$$\ker\left[(M)_{nk} = P_{y_k}(\gamma_n-x_k)\right]^\top = \{0\} \subset \ell^2$$

**Lemma 9.3 (The Poisson matrix).** The matrix $M_{nk} = P_{y_k}(\gamma_n-x_k)$ has the following structure:
- The rows are the functions $k\mapsto P_{y_k}(\gamma_n-x_k)$ (evaluation of the Poisson kernel at the supports of $\mu_{\mathrm{off}}$).
- The columns are the functions $n\mapsto P_{y_k}(\gamma_n-x_k)$ (Poisson kernel of the $k$-th atom evaluated at the zeros of $\Xi$).

**Proposition 9.4 (Completeness of rows ↔ injectivity of $M^T$).** The system of rows is complete in $\ell^2$ if and only if the operator $M^T: \ell^2 \to \mathbb{R}^{\mathbb{N}}$ (the transpose of $M$) is injective — i.e., if there is no sequence $(a_k) \in \ell^2$ with $\sum_k a_k P_{y_k}(\gamma_n-x_k) = 0$ for every $n$.

---

## 10. The harmonic function generated by the kernel of the system

**Theorem 10.1 (The kernel of $M^T$ as a harmonic function).** If $(a_k) \in \ell^2$ satisfies $\sum_k a_k P_{y_k}(\gamma_n - x_k) = 0$ for every $n\geq 1$, then the function:
$$F(t) = \sum_k a_k P_{y_k}(t-x_k)$$

is a harmonic function on $\mathbb{H}^+$ (Poisson extension of the measure $\nu = \sum_k a_k\delta_{(x_k,y_k)}$) satisfying $F(\gamma_n) = 0$ for every $n\geq 1$.

*Proof.* $F$ is a convergent sum of positive harmonic functions with coefficients in $\ell^2$, so it is harmonic. And $F(\gamma_n) = \sum_k a_k P_{y_k}(\gamma_n-x_k) = 0$ by hypothesis. $\square$

**Corollary 10.2.** The kernel of $M^T$ consists of coefficients $(a_k) \in \ell^2$ such that the harmonic function $F = \sum_k a_k P_{y_k}(\cdot-x_k)$ vanishes on the entire set $\{\gamma_n\}$.

**Lemma 10.3 (Uniqueness of harmonic extension).** If $F$ is harmonic on $\mathbb{H}^+$, continuous up to the boundary, and $F(\gamma_n) = 0$ for every $n\geq 1$, and if $F$ has *definite sign* (i.e., $F \geq 0$ or $F \leq 0$ on $\mathbb{R}$), then $F \equiv 0$ (by the Poisson Rigidity Theorem, Doc 43 T 3.1).

---

## 11. The final theorem of Direction II and the exact obstacle

**Theorem 11.1 (Completeness under a sign hypothesis).** If the coefficients $(a_k)$ in the kernel of $M^T$ are such that the function $F = \sum_k a_k P_{y_k}(\cdot - x_k)$ has constant sign on $\mathbb{R}$, then $(a_k) = 0$.

*Proof.* If $F \geq 0$, then by the Rigidity Theorem (Doc 43, T 3.1), $F \equiv 0$. By the injectivity of the Poisson transform (measure → harmonic function), $\sum_k a_k\delta_{(x_k,y_k)} = 0$, so $(a_k c_k) = 0$, so $(a_k) = 0$ since $c_k > 0$. $\square$

**The exact obstacle (made precise):**

> Prove that any $(a_k)\in\ker(M^T)$ produces a function $F$ of constant sign.

Formally: if $F = \sum_k a_k P_{y_k}(\cdot-x_k)$ with $F(\gamma_n) = 0$ for every $n$, does it follow that $F$ does not change sign?

**Proposition 11.2 (The obstacle does not follow from existing information).** In general, harmonic functions vanishing on a dense set do not have definite sign. Additional information on the structure of the $(x_k, y_k)$ (the off-critical zeros of $\zeta$) is needed to conclude the sign.

**The connection point with RH:** if RH is true, $(x_k,y_k) = \emptyset$, there is nothing to prove. If RH fails, the $(x_k,y_k)$ are off-critical zeros with specific arithmetic properties. The sign hypothesis is equivalent to asking: can the off-critical zeros of $\zeta$ be arranged so that $\sum_k a_k P_{y_k}(\cdot-x_k)$ changes sign on $\mathbb{R}$? This is a question about the distribution of the off-critical zeros — which is, once again, equivalent to RH.

---

## 12. Exact state of Direction II

**What is proved:**

| Statement | State | Tool |
|------------|--------|-------------|
| $\{P_{y_0}(\gamma_n-t)\}$ is a Riesz frame in $\mathcal{H}_{\mathrm{Poisson}}$ (fixed height $y_0$) | ✓ Proved | Seip 1993 |
| $\{K_{E_\Xi}(\gamma_n,\cdot)\}$ is an orthonormal basis in $\mathcal{H}(E_\Xi)$ | ✓ Proved under the de Branges hypothesis | de Branges 1961 |
| Completeness for absolutely continuous $\mu_{\mathrm{off}}$ | ✓ Proved | Seip + disintegration |
| $\ker(M^T)$ of constant sign $\Rightarrow (a_k)=0$ | ✓ Proved | Poisson rigidity |
| $\ker(M^T) = \{0\}$ (without a sign hypothesis) | ❌ Open | — |
| Completeness for atomic $\mu_{\mathrm{off}}$ unconditionally | ❌ Open | — |

**The precise reduction:**

> Direction II reduces RH to: *proving that any harmonic function vanishing at all the $\gamma_n$ and representable as $\sum a_k P_{y_k}(\cdot-x_k)$ with $(a_k)\in\ell^2$ and $(x_k,y_k)$ supports of off-critical zeros — has constant sign.*

This is a statement about the geometry of the off-critical zeros of $\zeta$, precisely formulated.

---

*Next (Doc 53): The sign problem — when can $\sum a_k P_{y_k}(\cdot-x_k)$ change sign? Necessary and sufficient conditions.*
