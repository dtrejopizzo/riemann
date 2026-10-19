# Document 105 — The $\partial_t$–$\partial_x$ coupling: first test of Form A on the 2-prime approximant

**Program:** Riemann Hypothesis — Phase 36 (Forms A, B, C)
**Prerequisites:** Docs 63, 64, 69, 70, 71, 72, 99, 103; P39, P41 (§ Form A, Problem 6.2)
**Candor rule:** every unproved step is declared an OPEN GAP; every claim not verified against a source carries [NOT VERIFIED]. No numerics: all values that appear are exact closed forms (rational arithmetic and radicals), with algebraic verification in Appendix A.

---

## 0. Executive summary

Form A of P41 (Problem 6.2) proposes a joint trace $\mathcal{T}(t,x)$ —the finite Euler approximant indexed by $x$, evolved by the De Bruijn–Newman (DBN) flow up to time $t$— and asks whether a differential inequality coupling $\partial_t$ with $\partial_x$ can propagate positivity from the two edges (unconditional theorems) to the corner $(t,x)=(0,\infty)$ (RH). This document runs the first finite, candid test declared in P41: the two-prime approximant $S=\{2,3\}$.

**Main results:**

1. **Interior degeneration theorem (§3).** With the only definition of $\mathcal{T}$ that makes *both* edges already-proved theorems (the CF completion of Doc 99 + DBN flow), one has $\mathcal{T}(t,x)=0$ for **every** finite $x$ and **every** $t\geq 0$, not just on the edges. The reason is structural: the DBN heat flow *preserves* the reality of zeros forward in time (de Bruijn's inheritance), and the property defining the edge $\{x\text{ finite}\}$ is exactly that reality. Consequently $\partial_t\mathcal{T}=\Delta_x\mathcal{T}=\partial_t\Delta_x\mathcal{T}=0$ identically in the quadrant's interior: **every parabolic inequality is vacuous and nothing propagates to the corner**, which remains a pure discontinuity whose continuity is, once again, the 1D wall of P41 §5.1.

2. **Exact computation of the Weil ledger (§5).** In the only place where the variations are nontrivial (the edge $x=\infty$, via Doc 72), the per-prime increment is computed **in closed form**: for the minimal Abel window $N(\lambda_0)=1$,
$$B_{\lambda_0}(r)=\frac{(\cosh r)^{-1/2}}{8}\Bigl(5-78\,\mathrm{sech}^2 r+105\,\mathrm{sech}^4 r\Bigr),$$
from which the increments $\delta_p=-(\log p/\sqrt p)\,B_{\lambda_0}(\log p)$ are **positive for $p=2,3,5,7$ and negative for every $p\geq 11$** (exact, rational sign change), and the sum over primes **diverges marginally** as $-(5\sqrt2/8)\log$ (Mertens-type). Form A's sign test fails in two ways at once: total degeneration in the interior and sign oscillation with no monotone diagonal on the boundary.

3. **Corrections to Docs 70–71 (§4).** The DBN flow satisfies $\partial_t H_t=-\partial_{ss}H_t$ (*backward* heat in the spectral variable), not $+\partial_{ss}H_t$ as written in Doc 70 §5.2; the time-derivative formula is re-derived cleanly ($\partial_t T|_0 = D(\Xi)-D(\Xi^{on})$ with $D$ explicit) and the sign analysis of Doc 71 §4 (the "dominant Term I" heuristic) is thereby invalidated: it omitted the on-critical block and the normalization term. The sign of $\partial_t T_\lambda|_{t=0}$ under $\neg$RH remains OPEN.

**VERDICT (§9): ROUTE CLOSED** for Form A with $\mathcal{T}=$ discrepancy trace, by degeneration (not by chaotic oscillation, which also occurs on the boundary). The sole non-discarded replacement object is named (Form A′, §8), which is no longer Form A and inherits the E4 suspicion from Doc 99.

---

## 1. The joint object: three candidate definitions and the design decision

### 1.1. What Form A requires

P41 (§ Form A) asks for a scalar field $\mathcal{T}(t,x)$ on the quadrant $\{t\geq 0\}\times\{x\in[2,\infty]\}$ such that:

- **(B1)** Temporal edge: $\mathcal{T}(t,\infty)=0$ for $t\geq\Lambda$, unconditional (DBN; Docs 70–71).
- **(B2)** Arithmetic edge: for finite $x$, unconditional control ("real zeros of the approximant", CF rigidity; Doc 99).
- **(C)** Corner: $\mathcal{T}(0,\infty)=0\iff$ RH.

and asks whether there is a $\partial_t$–$\partial_x$ differential coupling that propagates the positivity of (B1)+(B2) toward (C).

### 1.2. The three possible definitions of the evolved approximant

**Definition (a) — heat flow on the pointwise Euler product.** $\zeta_x(s):=\prod_{p\leq x}(1-p^{-s})^{-1}$ and $dm_x=|\zeta_x(\tfrac12+is)|^2\,dm_\infty$ (Doc 99, Lemma 6.4), evolved by heat. **Fatal defect 1:** $\zeta_x(\tfrac12+is)$ is not entire in $s$ (it has poles at $\mathrm{Im} s=\tfrac12$, i.e. $\mathrm{Re}\,\sigma=0$) and *has no zeros at all* in the critical strip: each factor $(1-p^{-1/2-is})^{-1}$ never vanishes for real $s$ nor anywhere ($|p^{-1/2-is}|=p^{-1/2}<1$ on $\mathbb{R}$). The "real-zero edge" is trivially true by vacuity, but the DBN flow does not act naturally on an object without a representation $\int\Phi(u)\cos(zu)\,du$. **Fatal defect 2:** the corner breaks: $\zeta_x(\tfrac12+is)$ does **not** converge pointwise as $x\to\infty$ (the Euler product does not converge on the critical line, not even under RH) — GAP 6.5 of Doc 99. With (a), (C) is not even defined as a limit of the field. **Discarded.**

**Definition (b) — CF completion of the approximant (Doc 99) + DBN flow on the Paley–Wiener class.** This is the one chosen; developed in §2.

**Definition (c) — discrete version via the Weil ledger (Doc 72).** $x=$ prime cutoff, $\Delta_x=$ increment upon adding the next prime, read off the decomposition $T_\lambda = A_\lambda^{off}-\sum_p(\log p/\sqrt p)B_\lambda(\log p)$ (Doc 72, Thm. 4.1). **Defect (which we prove exactly in §5.4):** that decomposition is *strictly formal* — the sum over primes diverges (marginally, Mertens-type), because the test function $W_\lambda w$ is at the **boundary** of the admissible Weil class (the poles of $w(s)=(2\pi)^{-2}|\Gamma(\tfrac14+\tfrac{is}2)|^2$ at $s=\pm i/2$ give Fourier decay exactly $e^{-|r|/2}$, with no $\varepsilon$ margin). Hence the increments $\Delta_x$ of (c) **are not the increments of any convergent quantity**: the "arithmetic edge" of (c) is not a theorem but a rearrangeable divergent series. (c) serves as a *ledger* for reading the $x$ direction on the boundary (we use it in §5), but not as a definition of the field. **Discarded as a definition; retained as an instrument.**

### 1.3. Declared decision

We adopt **Definition (b)**. It is the only one under which (B1), (B2), and (C) are simultaneously true by already-proved theorems (with a verifiable finite non-degeneracy hypothesis, which we declare). The price of that cleanliness is revealed in §3 and is the document's central result.

---

## 2. The chosen definition and verification of the edges

### 2.1. The CF-completed approximant (Doc 99 / CCM-ZST)

We fix the multiplicative parameter $\mu>1$ of the CCM-ZST framework (we call it $\mu$ and not $\lambda$ to avoid colliding with the Abel scale $\lambda_0$ of the kernel $W_{\lambda_0}$, which is a **different** parameter; see Doc 99 §6.2-bis on the risk of identifying the two sides). The arithmetic cutoff is $x=\mu^2$: by automatic support locality (Doc 99 §2.1), the semilocal Weil form $QW_\mu$ on $L^2([\mu^{-1},\mu],d^*u)$ only involves prime powers $p^m\leq\mu^2$.

**Exact realization of $S=\{2,3\}$.** Take $\mu^2=x\in[3,4)$ (e.g. $\mu=\sqrt3$). Then $\{p^m\leq x\}=\{2,3\}$: exactly the primes $2$ and $3$ enter, both with $m=1$ only ($2^2=4>x$). The two-prime approximant of the title is this window.

For each truncation $N$, let $\xi=\xi^{(\mu,N)}$ be the minimal eigenvector of the matrix $QW_\mu^N$ (Loewner structure, Doc 99 §2.3), under the hypothesis:

> **(ES$_x$) finite even-simplicity.** The minimal eigenvalue of $QW_\mu^N$ is simple with even eigenvector. — *Verifiable for each finite $(\mu,N)$ by a non-degeneracy computation; it is not a positivity; it is the exact status of CCM-ZST's Thm. 5.10 per Doc 99 §2.5. We assume it declaredly for the $(\mu,N)$ used.*

We define the **entire function of the approximant**
$$F_x(z) := \widehat{\xi}(z) = \int_{-L/2}^{L/2}\xi(e^v)\,e^{izv}\,dv = 2\int_0^{L/2}\xi(e^v)\cos(zv)\,dv, \qquad L=2\log\mu,$$
(using the parity $\gamma\xi=\xi$). Properties (all from Doc 99 §2.4 and elementary Paley–Wiener theory):

- $F_x$ is entire, **even, real on $\mathbb{R}$**, of exponential type $L/2$, with Fourier transform of **compact support** $[-L/2,L/2]$;
- (CF rigidity, CvS + CCM-ZST Thm. 5.10(iii), unconditional given (ES$_x$)): **all zeros of $F_x$ are real**, and coincide with $\mathrm{spec}(H_x)$ up to the zero-free factor $-i\mu^{-iz}$ of the regularized determinant.

### 2.2. The DBN flow on the approximant

Write $\varphi_x(u):=2\,\xi(e^u)\,\mathbf{1}_{[0,L/2]}(u)$ (cosine kernel of $F_x$) and define the **DBN evolution of the approximant**:
$$F_x^t(z) := \int_0^{L/2} e^{tu^2}\,\varphi_x(u)\cos(zu)\,du, \qquad t\in\mathbb{R}.$$
Since $\varphi_x$ has compact support, $F_x^t$ is defined and entire **for all $t\in\mathbb{R}$** (unlike the $\zeta$ case, where $t\leq 1/2$). It is the same recipe that defines $H_t$ from $\Phi$ (Doc 70 §2.1), applied to the approximant's kernel. Note the PDE satisfied:
$$\partial_t F_x^t(z) = \int u^2 e^{tu^2}\varphi_x\cos(zu)\,du = -\,\partial_{zz}F_x^t(z),$$
i.e., **backward heat** in the spectral variable $z$ (see Remark 4.1 on the sign in Doc 70).

### 2.3. The joint field

For finite $x$ and $t\geq 0$: let $dm^{(t,x)}(s) := |F_x^t(s)|^2\,dm_\infty(s)\cdot C_{t,x}^{-1}$ (normalized), and $dm_{on}^{(t,x)}$ its on-critical version (reflecting onto $\mathbb{R}$ the non-real zeros of $F_x^t$, as in Doc 70 §3.1). For $x=\infty$: $F_\infty^t := H_t$ (the DBN flow of $\Xi$), $dm^{(t,\infty)}=dm_{full}^t$ of Doc 70.

We fix once and for all the **minimal** Abel scale $\lambda_0$ with $N(\lambda_0)=1$, so that (Doc 71 §2.3)
$$W_{\lambda_0}(s) = |P_1(s)|^2 + (a_1^\infty)^2|P_2(s)|^2,$$
with $a_k^\infty=\tfrac12\sqrt{(2k+1)(2k+2)}$, i.e. $(a_0^\infty)^2=\tfrac12$, $(a_1^\infty)^2=3$. By Doc 103 (Theorem 3.1), **a single $\lambda_0$ suffices**: $T_{\lambda_0}(0)=0\iff$ RH; and $W_{\lambda_0}>0$ at every point of $\mathbb{R}$ (Doc 103). We define:

$$\boxed{\;\mathcal{T}(t,x) := \int W_{\lambda_0}(s)\,\bigl(dm^{(t,x)}-dm_{on}^{(t,x)}\bigr)(s)\;}$$

### 2.4. Critical verification: are the edges theorems under this definition?

**Proposition 2.1 (temporal edge).** $\mathcal{T}(t,\infty)=T_{\lambda_0}(t)=0$ for all $t\geq\Lambda$.

*Proof.* This is Obs. 3.1 of Doc 70 with $\lambda=\lambda_0$: for $t>\Lambda$ all zeros of $H_t$ are real, so $H_t=H_t^{on}$ and the measure difference is zero; at $t=\Lambda$ by continuity of the zeros (Rodgers–Tao guarantee $\Lambda\geq0$; reality at $t=\Lambda$ follows from the closedness of $\mathbb{R}$ and Hurwitz). $\square$

**Proposition 2.2 (arithmetic edge, $t=0$).** Under (ES$_x$): $\mathcal{T}(0,x)=0$ for all finite $x$.

*Proof.* By CF rigidity (Doc 99 §3, CCM-ZST Thm. 5.10(iii)), all zeros of $F_x=F_x^0$ are real; hence $F_x^{on}=F_x$, the two measures coincide, and the integral is zero. $\square$

**Corner.** $\mathcal{T}(0,\infty)=T_{\lambda_0}(0)$, and by Doc 64 (CTP) sharpened by Doc 103 (Theorem 3.1, a single $\lambda_0$): $\mathcal{T}(0,\infty)=0\iff$ RH. $\square$

Both edges and the corner are exactly as required by P41. The definition passes the critical check requested in task (i). What follows shows that it passes *too well*.

---

## 3. The degeneration theorem: the quadrant's interior is identically zero

### 3.1. De Bruijn's inheritance

**Lemma 3.1 (preservation of the reality of zeros under the forward DBN flow).** Let $\varphi\in L^1[0,a]$ be real, $a<\infty$, and $F^t(z)=\int_0^a e^{tu^2}\varphi(u)\cos(zu)\,du$, not identically zero. If all zeros of $F^{t_1}$ are real, then all zeros of $F^t$ are real for every $t\geq t_1$.

*Proof.* This is de Bruijn's Theorem 13 [de Bruijn 1950, *The roots of trigonometric integrals*, Duke Math. J. **17**, 197–226]: if the zeros of $\int e^{t_1u^2}\varphi(u)\cos(zu)\,du$ lie in the strip $|\mathrm{Im}\,z|\leq\Delta$, those of the evolution at time $t\geq t_1$ lie in $|\mathrm{Im}\,z|\leq\sqrt{\max(\Delta^2-2(t-t_1),0)}$. With $\Delta=0$ one obtains reality for all $t\geq t_1$. De Bruijn's regularity/decay hypotheses are trivially satisfied for compactly supported kernels on $[0,a]$ (every integral converges absolutely and $F^t$ is entire of order $\leq1$ and finite type in $z$ for each $t$; de Bruijn's statement covers this class — it is the same citation used by Rodgers–Tao 2018, §1, for $\Lambda\leq 1/2$ with $\Delta=1/2$). $\square$

### 3.2. The theorem

**Theorem 3.2 (interior degeneration).** Under (ES$_x$) for each finite $x$ in the family:
$$\mathcal{T}(t,x) = 0 \qquad\text{for all } x<\infty \text{ and all } t\geq 0.$$
In particular, over the interior of the quadrant (and over both edges):
$$\partial_t\mathcal{T} \equiv 0,\qquad \Delta_x\mathcal{T} := \mathcal{T}(t,S\cup\{p\})-\mathcal{T}(t,S) \equiv 0,\qquad \partial_t\Delta_x\mathcal{T} \equiv 0.$$

*Proof.* By CF rigidity (Prop. 2.2), the zeros of $F_x^0$ are all real. By Lemma 3.1 with $t_1=0$, the zeros of $F_x^t$ are all real for every $t\geq 0$. Then $F_x^t=(F_x^t)^{on}$, $dm^{(t,x)}=dm_{on}^{(t,x)}$ and $\mathcal{T}(t,x)=0$. The three vanishing variations are immediate (differences and derivatives of the identically zero function; the derivative $\partial_t$ exists because $t\mapsto F_x^t$ is real-analytic in $t$ with a compactly supported kernel). $\square$

### 3.3. Structural reading: why Form A degenerated

The mechanism is exact and worth isolating:

> **The property defining the arithmetic edge (reality of the approximant's zeros) is invariant under the flow defining the temporal edge.** The forward DBN flow cannot take zeros off the real line (Lemma 3.1). Hence the edge $\{x\text{ finite}, t=0\}$ is not an edge: it is a *source* whose property floods the entire half-plane $t\geq0$ at fixed $x$. The field $\mathcal{T}$ turns out identically zero on $[0,\infty)\times\{x<\infty\}$, and all of RH's content is compressed into the field's behavior on the boundary line $\{x=\infty\}$: there $\mathcal{T}(t,\infty)=T_{\lambda_0}(t)$, which under $\neg$RH is $>0$ for $t\in[0,\Lambda)$ and $0$ for $t\geq\Lambda$.

Immediate consequences for P41's Problem 6.2:

1. **Every parabolic inequality is vacuously true in the interior.** $\partial_t\mathcal{T}\leq c\,\Delta_x\mathcal{T}$, log-convexity on diagonals $t=\alpha/\log p_x$, monotonicity of any $M(t,x)$ built from $\mathcal{T}$ and its derivatives: all hold as $0\leq 0$ and **carry no information** toward the corner.

2. **The corner is a pure discontinuity.** Under $\neg$RH, $\mathcal{T}\equiv 0$ in the interior but $\lim_{x\to\infty}\mathcal{T}(t,x)=0\neq T_{\lambda_0}(t)=\mathcal{T}(t,\infty)$ for every $t<\Lambda$: the field is discontinuous on the **entire segment** $\{x=\infty,\,0\leq t<\Lambda\}$, not just at the corner. No maximum principle, Almgren-type monotonicity formula, or log-convexity sees a discontinuity concentrated on the domain's boundary: those mechanisms propagate information from the edges to the interior **for functions that satisfy a PDE in the interior and are continuous up to the boundary**. Here the needed direction is the opposite one (from the trivial interior toward the nontrivial boundary value), and that is exactly **continuity of the field at the arithmetic boundary**, i.e., the 1D wall of P41 §5.1 (continuity $\equiv$ RH), which Form A was meant to escape.

3. **The degeneration is not an accident of definition (b): it is a dichotomy.** If the definition is modified so that the interior is not trivial, one of the two invariances must be broken: either the arithmetic edge stops being the CF theorem (then (B2) is no longer a theorem — exactly what happens with definitions (a) and (c), §1.2), or the temporal flow stops being forward DBN heat (then (B1) is no longer a theorem, because extinction at $t\geq\Lambda$ is a fact about heat). Formally:

**Proposition 3.3 (Form A dichotomy for discrepancy traces).** Let $\mathcal{T}(t,x)=\int W_{\lambda_0}\,(dm^{(t,x)}-dm^{(t,x)}_{on})$ be any field whose approximant at finite $x$ is a real even entire function $G_x$ with all its zeros real (CF-type condition (B2)) and whose time evolution is $G_x^t=$ multiplication of the cosine kernel by $e^{tu^2}$ (DBN-type condition (B1)). Then $\mathcal{T}\equiv 0$ on $\{x<\infty,\,t\geq0\}$.

*Proof.* Identical to Theorem 3.2: (B2) gives reality at $t=0$, (B1)+Lemma 3.1 propagate it to all $t\geq0$, and reality annihilates the discrepancy. $\square$

The dichotomy is: **(theorem edges) $\Rightarrow$ (trivial interior)**; contrapositively, (nontrivial interior) $\Rightarrow$ (at least one edge is not a theorem). Form A asked for both at once for the discrepancy trace; they are incompatible.

---

## 4. (ii) The time derivative $\partial_t\mathcal{T}$ at $t=0$ for $S=\{2,3\}$

Although Theorem 3.2 already gives the answer ($\partial_t\mathcal{T}(0,x_2)=0$ exactly, with $x_2\in[3,4)$ the two-prime cutoff), we carry out the computation using Doc 71's machinery as the task requests, because the computation (i) reveals **two errors in Docs 70–71** that must be corrected in the corpus, and (ii) shows precisely *what* cancels and why the cancellation at finite $x$ contains no arithmetic.

### 4.1. Sign correction to the flow (Doc 70 §5.2)

**Remark 4.1 (sign of the heat equation).** With the standard definition $H_t(z)=\int e^{tu^2}\Phi(u)\cos(zu)\,du$ (Doc 70 §2.1), one has
$$\partial_t H_t(z) = \int u^2 e^{tu^2}\Phi(u)\cos(zu)\,du = -\,\partial_{zz}H_t(z),$$
because $\partial_{zz}\cos(zu)=-u^2\cos(zu)$. Doc 70 §5.2 writes "$\partial_t H_t=\partial_{ss}H_t$ (heat equation)": the sign is the **opposite** one (the DBN flow is backward heat in the spectral variable; that is why it *sharpens* the function and pushes zeros toward $\mathbb{R}$, whereas $e^{-tu^2}$ — forward heat — smooths it). Consequently, Doc 70's Prop. 8.2 and the boxed formula of Doc 71 §3.3 carry the opposite global sign. Doc 71's *structural* conclusions (quadratic form in $c_k$, cancellation under RH, the limitation of §6) survive because they are sign-invariant; Doc 71's §4 sign analysis does **not** survive (see Obs. 4.3).

### 4.2. The clean derivative

Let $G$ be entire, real on $\mathbb{R}$, even, with $G^t$ its DBN evolution, and let $T(t)=\int W_{\lambda_0}(s)(|G^t|^2-|G^{t,on}|^2)\,dm_\infty\cdot C_t^{-1}$ be the normalized discrepancy trace. On $\mathbb{R}$, $\partial_t|G^t|^2 = 2G^t\,\partial_tG^t = -2\,G^t (G^t)''$, and with the pointwise identity $GG''=\tfrac12(G^2)''-(G')^2$ and integration by parts twice (the boundary terms vanish by the decay $e^{-\pi|s|/2}$ of $w$ against the finite-type polynomial-exponential growth of $G^2$ when $G$ has type $<\pi/2$; for $G=F_x$ the type is $L/2=\log\mu<\pi/2$ if $\mu<e^{\pi/2}\approx 4.81$, which covers $\mu=\sqrt3$; for larger $\mu$ the justification requires type $<\pi/2$ or a mollifier — we declare this as a validity condition):
$$\int W GG''\,dm_\infty = \tfrac12\int (W w)''\,G^2\,ds - \int W (G')^2\,dm_\infty.$$
Hence:

**Proposition 4.2 (time derivative, corrected form).**
$$\partial_t T\Big|_{t=0} = D(G) - D(G^{on}) - \frac{\dot C_0}{C_0}\,T(0), \qquad
D(G) := 2\int W_{\lambda_0}(G')^2\,dm_\infty - \int (W_{\lambda_0}\,w)''\,G^2\,ds.$$

Comparison with Doc 71 §3.3: (1) the global sign is corrected (Obs. 4.1); (2) Doc 71's three terms regroup into $(W w)''= W''w + 2W'w' + Ww''$, which matches Doc 71's Terms II–III **plus** the curvature term $W\cdot((\log w)''+((\log w)')^2)w$ that Doc 71 §3.2 omitted; (3) Doc 71 omitted the subtraction of the on-critical block $D(G^{on})$ and the normalization term $-(\dot C_0/C_0)T(0)$. Doc 71 §5.1's quadratic form $Q^{(\lambda)}(c,c)$ should, strictly, be read as $D(G)$ alone — not as $\partial_tT|_0$.

### 4.3. The derivative at the two-prime approximant

**Theorem 4.3.** Under (ES$_{x_2}$), for the approximant $F_{x_2}$ of $S=\{2,3\}$:
$$\partial_t\mathcal{T}(t,x_2)\Big|_{t=0} = D(F_{x_2}) - D(F_{x_2}^{on}) - \frac{\dot C_0}{C_0}\,\mathcal{T}(0,x_2) = 0,$$
and the cancellation is **term by term**: $F_{x_2}^{on}=F_{x_2}$ (CF rigidity) and $\mathcal{T}(0,x_2)=0$, so the three summands vanish *individually as differences*, not through cancellation of three nonzero integrals.

*Proof.* Immediate from Prop. 4.2 with $G=F_{x_2}$, $G^{on}=G$ (Prop. 2.2) and $\mathcal{T}(0,x_2)=0$. $\square$

**Remark 4.4 (what this cancellation contains and does not contain).** The budget $D(F_{x_2})$ is a finite, computable, genuinely nontrivial quantity: its first term $2\int W_{\lambda_0}(F_{x_2}')^2dm_\infty>0$ strictly, because $W_{\lambda_0}>0$ at every point (Doc 103) and $F_{x_2}'\not\equiv0$. But $\partial_t\mathcal{T}=D(F_{x_2})-D(F_{x_2})=0$ is the subtraction of the **same** quantity from itself: the vanishing of the derivative at finite $x$ is a direct corollary of the reality of the zeros, and **encodes no arithmetic cancellation**. This corrects a possibly optimistic reading of Doc 71 §5.2: the "exact cancellation of the three terms under RH" is, correctly viewed (with the on-critical block restored), the trivial identity $D(\Xi)-D(\Xi)=0$, not a nontrivial algebraic condition on the $c_k$. The nontrivial condition is $T_{\lambda_0}(0)=0$ itself — as Doc 71 §6 already concluded, by another route.

**Remark 4.5 (the sign of $\partial_tT_{\lambda}|_{t=0}$ at $x=\infty$ under $\neg$RH remains OPEN).** Doc 71 §4's analysis ("dominant Term I $\Rightarrow\dot T>0$") used only the block $D(\Xi)$, with the wrong PDE sign and without the block $D(\Xi^{on})$. With the corrected formula, the sign of $\partial_tT|_0=D(\Xi)-D(\Xi^{on})-(\dot C_0/C_0)T(0)$ under $\neg$RH depends on comparing the weighted energy $2\int W(\Xi')^2dm_\infty$ with that of $\Xi^{on}$ (whose additional real zero at $\gamma_0$ *increases* $|(\Xi^{on})'|$ locally near $\gamma_0$ while $|\Xi^{on}|\le|\Xi|$ pointwise on $\mathbb{R}$): the two blocks compete and there is no pointwise inequality between the integrands. We declare: **OPEN GAP** (sign of $\dot T(0)$ under $\neg$RH). The "apparent contradiction" of Doc 71 §4.3 dissolves: there was no evidence for the $+$ sign.

---

## 5. (iii) The discrete increment $\Delta_x\mathcal{T}$ and the Weil ledger in closed form

By Theorem 3.2, $\Delta_x\mathcal{T}(t=0)=\mathcal{T}(0,S\cup\{p\})-\mathcal{T}(0,S)=0-0=0$ exactly. The nontrivial content of the $x$ direction thus lives solely in the **Weil ledger** (Doc 72): the formal decomposition $T_\lambda=A_\lambda^{off}-\sum_p\sum_{m\ge1}(\log p/p^{m/2})B_\lambda(m\log p)+\text{arch.}$, where the term for prime $p$ is the "discrete $\partial_x$ increment" declared in P41. In this section we compute that ledger **in exact closed form** for the window $N(\lambda_0)=1$, and extract three consequences (signs, sign change at $p=11$, marginal divergence).

### 5.1. The Fourier transform of $dm_\infty$ in closed form

**Lemma 5.1.** For $a>0$ and $u\in\mathbb{R}$:
$$\int_{-\infty}^{\infty}|\Gamma(a+it)|^2 e^{iut}\,dt = \frac{2\pi\,\Gamma(2a)}{(2\cosh(u/2))^{2a}}.$$

*Proof.* From the beta integral $B(p,q)=\int_0^\infty y^{p-1}(1+y)^{-p-q}dy$ with $p=a+it$, $q=a-it$ and the substitution $y=e^v$:
$$\Gamma(a+it)\Gamma(a-it) = \Gamma(2a)\,B(a+it,a-it) = \Gamma(2a)\int_{-\infty}^{\infty}\frac{e^{av}e^{itv}}{(1+e^v)^{2a}}\,dv = \Gamma(2a)\int_{-\infty}^{\infty}\frac{e^{itv}}{(2\cosh(v/2))^{2a}}\,dv,$$
using $e^{av}(1+e^v)^{-2a}=(e^{-v/2}+e^{v/2})^{-2a}$. That is, $|\Gamma(a+it)|^2$ is the Fourier transform of $\Gamma(2a)(2\cosh(v/2))^{-2a}\in L^1$; Fourier inversion (both sides even, real, integrable) gives the statement. $\square$

**Corollary 5.2.** With $dm_\infty(s)=(2\pi)^{-2}|\Gamma(\tfrac14+\tfrac{is}2)|^2ds$ and $a=\tfrac14$, $s=2t$:
$$\widehat w(r):=\int e^{irs}\,dm_\infty(s) = \frac{1}{\sqrt{2\pi}}\,(\cosh r)^{-1/2} =: \frac{g(r)}{\sqrt{2\pi}},\qquad g(r)=(\cosh r)^{-1/2}.$$
In particular the total mass is $\int dm_\infty=(2\pi)^{-1/2}$ (the program's normalization is not a probability one; the degree-0 orthonormal polynomial is $P_0=(2\pi)^{1/4}$). The decay $\widehat w(r)\sim \pi^{-1/2}e^{-|r|/2}$ reflects the poles of $w$ at $s=\pm i/2$ (pole of $\Gamma(\tfrac14+\tfrac{is}{2})$ at $s=i/2$): the width of analyticity is **exactly** $1/2$, with no margin.

**Consistency check (Appendix A.1):** the moments $\int s^2\,d\widetilde m=-g''(0)/g(0)=\tfrac12=(a_0^\infty)^2$ and $\int s^4\,d\widetilde m=g''''(0)/g(0)=\tfrac74=(a_0^\infty)^4+(a_0^\infty)^2(a_1^\infty)^2$ exactly reproduce the program's Jacobi coefficients $a_k^\infty=\tfrac12\sqrt{(2k+1)(2k+2)}$: the measure and the recursion are consistent. This validates Lemma 5.1 against the CCM data independently.

### 5.2. $B_{\lambda_0}(r)$ in closed form

With $N(\lambda_0)=1$: $W_{\lambda_0}=|P_1|^2+3|P_2|^2$, and from the recursion ($b_k=0$): $P_1=sP_0/a_0$, $P_2=(s^2-\tfrac12)P_0/(a_0a_1)$, with $a_0^2=\tfrac12$, $a_1^2=3$, $P_0^2=\sqrt{2\pi}$. The blocks $G_n(r):=\int|P_n(s)|^2\cos(rs)\,dm_\infty(s)$ reduce to derivatives of $g$ (even moments against cosine), and a direct computation (Appendix A.2) gives, with $c:=\cosh r$:
$$G_1(r) = -2g''(r) = -\tfrac12\,c^{-1/2}+\tfrac32\,c^{-5/2},\qquad
G_2(r) = \tfrac38\,c^{-1/2}-\tfrac{15}4\,c^{-5/2}+\tfrac{35}8\,c^{-9/2}.$$

**Theorem 5.3 (closed form of the Weil coefficient for the minimal window).**
$$B_{\lambda_0}(r) = G_1(r)+3G_2(r) = \frac{c^{-1/2}}{8}\,Q(\mathrm{sech}^2 r),\qquad Q(y) := 105\,y^2 - 78\,y + 5,\qquad c=\cosh r.$$
Checks: $B_{\lambda_0}(0)=\tfrac{5-78+105}{8}=4=\int W_{\lambda_0}\,dm_\infty$ (= $1+(a_1^\infty)^2$, orthonormality) ✓; $G_1(0)=G_2(0)=1$ ✓.

The roots of $Q$ are $y_\pm=\dfrac{39\pm2\sqrt{249}}{105}$, with $y_-=0.0709\ldots$, $y_+=0.6724\ldots$ Therefore:
$$B_{\lambda_0}(r) < 0 \iff y_-<\mathrm{sech}^2 r<y_+ \,;\qquad B_{\lambda_0}(r)>0 \text{ for } r \text{ large } (\mathrm{sech}^2r<y_-).$$

### 5.3. The per-prime increments: exact signs

For prime $p$ (term $m=1$), the ledger increment is $\delta_p := -\dfrac{\log p}{\sqrt p}\,B_{\lambda_0}(\log p)$. Since $\cosh(\log p)=\tfrac{p+p^{-1}}2$, one has $\mathrm{sech}^2(\log p)=\Bigl(\tfrac{2p}{p^2+1}\Bigr)^2$, rational. Exact evaluation of $Q$:

| $p$ | $\mathrm{sech}^2(\log p)$ | $Q(\mathrm{sech}^2\log p)$ | sign of $B_{\lambda_0}(\log p)$ | sign of $\delta_p$ |
|---|---|---|---|---|
| $2$ | $16/25$ | $-239/125$ | $-$ | $+$ |
| $3$ | $9/25$ | $-1184/125$ | $-$ | $+$ |
| $5$ | $(5/13)^2=25/169$ | $-121120/28561$ | $-$ | $+$ |
| $7$ | $(7/25)^2=49/625$ | $-183520/390625$ | $-$ | $+$ |
| $11$ | $(11/61)^2=121/3721$ | $+35647712/13845841$ | $+$ | $-$ |
| $p\geq11$ | $<y_-$ | $>0$ | $+$ | $-$ |

(For $p\geq11$: $\tfrac{2p}{p^2+1}\leq\tfrac{22}{122}=0.1803\ldots<\sqrt{y_-}=0.2663\ldots$, decreasing in $p$; for $p=7$: $\tfrac{14}{50}=0.28>\sqrt{y_-}$, hence the last $-$ sign of $Q$. Full rational verification in Appendix A.3.) The two increments of the two-prime approximant, in closed form:
$$\delta_2 = \frac{\log 2}{\sqrt2}\cdot\frac{239}{500\sqrt5} \;(>0), \qquad
\delta_3 = \frac{\log 3}{\sqrt3}\cdot\frac{148}{125}\sqrt{\tfrac35} \;(>0).$$
Prime powers follow the same polynomial: $\mathrm{sech}^2(2\log2)=(8/17)^2$ gives $Q<0$ ($\delta_{2^2}>0$), while $\mathrm{sech}^2(3\log2)=(16/65)^2<y_-$ and $\mathrm{sech}^2(2\log3)=(9/41)^2<y_-$ give $Q>0$ ($\delta_{2^3}<0$, $\delta_{3^2}<0$): on the $p^m$ scale, the sign change occurs at the unique solution of $\mathrm{sech}^2(\log u)=y_-$, $u_*\in(7,8)$.

**Theorem 5.4 (oscillation of the discrete increment).** For the window $N(\lambda_0)=1$, the Weil ledger increment is strictly positive for $p^m\in\{2,3,4,5,7\}$ and strictly negative for every $p^m\geq8$ (in particular for every prime $p\geq11$): the exact crossing is at $\mathrm{sech}^2(\log u_*)=y_-=\tfrac{39-2\sqrt{249}}{105}$, with $u_*\in(7,8)$. In particular, $\Delta_x$ (in its only nontrivial reading) **changes sign within the family and is not monotone in $x$ along any diagonal**.

*Proof.* Table above + monotonicity of $\mathrm{sech}^2(\log\cdot)$ + sign of $Q$ outside/inside $(y_-,y_+)$; all values are rational and the computation is exact arithmetic (Appendix A.3). $\square$

### 5.4. The marginal divergence: Doc 72's Theorem 4.1 is strictly formal

**Theorem 5.5 (Mertens divergence of the ledger).** As $r\to\infty$, $B_{\lambda_0}(r)=\tfrac{5\sqrt2}{8}\,e^{-r/2}\,(1+O(e^{-2r}))$. Hence the term for prime $p$ satisfies
$$\frac{\log p}{\sqrt p}\,B_{\lambda_0}(\log p) = \frac{5\sqrt2}{8}\cdot\frac{\log p}{p}\,\bigl(1+O(p^{-2})\bigr),$$
and the sum $\sum_{p\leq X}\frac{\log p}{\sqrt p}B_{\lambda_0}(\log p)$ **diverges** as $\tfrac{5\sqrt2}{8}\log X$ (Mertens: $\sum_{p\le X}\log p/p=\log X+O(1)$). The prime series in Doc 72's Thm. 4.1 converges neither absolutely nor conditionally (terms of eventually constant sign): the decomposition $T_\lambda=A^{off}_\lambda-\sum_p(\log p/\sqrt p)B_\lambda(\log p)$ is **strictly formal** and requires regularization (pairing with the divergent archimedean block before summing).

*Proof.* $c^{-1/2}=(\cosh r)^{-1/2}=\sqrt2\,e^{-r/2}(1+e^{-2r})^{-1/2}$ and $Q(\mathrm{sech}^2r)\to Q(0)=5$; Mertens is classical. Non-conditional convergence: the terms have constant sign for $p\geq11$. $\square$

**Remark 5.6 (the root of the phenomenon and its consistency with Doc 99).** The test function $h_{\lambda_0}=W_{\lambda_0}w$ is analytic exactly for $|\mathrm{Im}\,s|<\tfrac12$ (poles of $w$ at $\pm i/2$): it is at the **boundary** of the Weil class, which requires $|\mathrm{Im}\,s|<\tfrac12+\varepsilon$. The decay $\widehat{h}(r)\asymp e^{-r/2}$ exactly compensates the prime weight $p^{1/2}$ and lays bare the logarithmic divergence. This is the Jacobi-framework version of the prime-tail divergence of Doc 99 (Lemma 5.1: $\sum_{p\le\lambda}\log p/\sqrt p\gtrsim\sqrt\lambda$ for the tent function): different rate because different test function, **same lesson** — MW-2 reappears quantitatively in the $x$ direction, and the $x$ direction of the quadrant is not the sum of absolutely convergent increments of any quantity. We also note that this refines the "formally" comment of Doc 72 §4.1: the obstruction now has an exact constant ($\tfrac{5\sqrt2}{8}$) and an identified mechanism (boundary of the Weil class). That the Mertens sum of Doc 60/72 §7 appears here is not a coincidence: it is the same term.

### 5.5. Why the oscillation is generic in $N$ (not an accident of the minimal window)

**Proposition 5.7.** For every $\lambda_0$ with $N(\lambda_0)\geq1$, the function $r\mapsto B_{\lambda_0}(r)$ is positive definite in the Bochner sense (it is the Fourier transform of the finite nonnegative measure $W_{\lambda_0}w\,ds\geq0$, strictly positive at every point by Doc 103). Consequently $|B_{\lambda_0}(r)|\leq B_{\lambda_0}(0)$ and $B_{\lambda_0}(0)>0$; but Bochner positivity **does not** imply pointwise positivity of $B_{\lambda_0}$, and indeed it fails: $\int_{\mathbb{R}} B_{\lambda_0}(r)\,dr = 2\pi\,W_{\lambda_0}(0)\,w(0)$ is finite while $B_{\lambda_0}(0)=\int W_{\lambda_0}dm_\infty$ grows as $\sim N^2$ (Abel weights), so for large $N$ the positive mass at $r=0$ must be compensated by oscillation: $B_{\lambda_0}$ has sign changes for every sufficiently large $N$, with first crossing $r_*(\lambda_0)$ moving with the scale (heuristically $r_*\sim1/\lambda_0$ by the uncertainty principle; not needed here). For $N=1$ the crossing is computed exactly (Theorems 5.3–5.4).

*Proof (of the claim, not of the heuristic).* Bochner: standard, $W_{\lambda_0}w\in L^1$, $\geq0$. The formula $\int B=2\pi W(0)w(0)$ is Fourier inversion at $r=0$ (both functions integrable: $B$ decays as $e^{-r/2}$ by Cor. 5.2 term by term, $W_{\lambda_0}w$ is Schwartz-exponentially decreasing). The growth $B_{\lambda_0}(0)=\sum_{n=1}^N n\|P_n\|^2+(a_N^\infty)^2=\tfrac{N(N+1)}2+(a_N^\infty)^2\sim N^2$: orthonormality and Doc 71 §2.3. The conclusion "sign changes for large $N$" follows from: if $B\geq0$ everywhere on $\mathbb{R}$, then $\sup B=B(0)\leq\ldots$ does not bound it; the correct argument is: $B\geq0$ and $\int B<\infty$ fixed, with $B(0)\to\infty$ and $B$ uniformly Lipschitz on scales $O(1/N)$... — this line requires quantifying the concentration; we leave it as a **claim proved only for $N=1$ (exact) and plausible for general $N$ [incomplete argument — minor GAP declared]**. What §6 uses is only the $N=1$ case, which is exact. $\square$

The consequence for Form A does not depend on the GAP: already with a single window (the minimal one, which by Doc 103 suffices for the corner) the increment $\Delta_x$ oscillates with an exact crossing.

---

## 6. (iv) The sign test: answer to the central question

P41's question (Problem 6.2) was: is there a fixed sign relation between $\partial_t\mathcal{T}$ and $\Delta_x\mathcal{T}$ supporting (a) a parabolic inequality, (b) log-convexity on diagonals, or (c) a monotone quantity $M(t,x)$ controllable on both edges? The answer has two levels, and on both Form A dies — but by mechanisms different from the one envisioned by the falsifier, which is worth recording precisely.

### 6.1. Interior level: total degeneration (not oscillation)

In the quadrant's interior (every finite $x$, every $t\geq0$):
$$\partial_t\mathcal{T}=0,\qquad \Delta_x\mathcal{T}=0,\qquad \partial_t\Delta_x\mathcal{T}=0 \qquad\text{(Theorem 3.2)}.$$
P41's falsifier contemplated death by *oscillation* ("the mixed variation changes sign with no monotone diagonal"). What happens is stronger and more definitive: the mixed variation does not change sign — it is identically zero — and precisely because of that **every** parabolic inequality, log-convexity, and monotone quantity built from $\mathcal{T}$ holds vacuously while carrying nothing. A maximum principle with no nontrivial function to apply to is not a propagation mechanism; it is a statement about the empty set. Form A does not fail because the coupling is chaotic: it fails because **there is nothing to couple**.

### 6.2. Boundary level: exact oscillation with no monotone diagonal

The only nontrivial variations live on the line $\{x=\infty\}$ (where $\mathcal{T}(t,\infty)=T_{\lambda_0}(t)$) and in the Weil ledger that reads the $x$ direction on that line. There the sign test gives:

- **$x$ direction (Theorem 5.4):** the increments $\delta_p$ change sign (positive for $p^m\in\{2,3,4,5,7\}$; negative for every $p^m\geq8$, in particular every prime $p\geq11$), with exact crossing at $\mathrm{sech}^2(\log u_*)=y_-=(39-2\sqrt{249})/105$, $u_*\in(7,8)$. Moreover the series diverges (Theorem 5.5): there is no accumulated quantity whose increments are the $\delta_p$. The crossing point **depends on the window $\lambda_0$** (the coefficients $105,-78,5$ are those for $N=1$; for larger $N$ the polynomial changes and the crossing moves), so no diagonal $t=\alpha/\log p_x$ can be uniformly monotone across the scale.
- **$t$ direction (Remark 4.5):** the sign of $\partial_tT_{\lambda_0}(0)$ under $\neg$RH is an OPEN GAP; the only prior evidence (Doc 71 §4) is invalidated by the PDE sign and the omitted on-critical block.

Test conclusion: **there is no fixed sign relation** $\partial_t\mathcal{T}\lessgtr c\,\Delta_x\mathcal{T}$ either in the interior (where it is $0=0$, vacuous) or on the boundary (where one side oscillates with a scale-dependent crossing and the other has unknown sign). The first finite, candid test declared in P41 §Form A was carried out and **the falsifier fires**, in degenerate mode (interior) and oscillatory mode (boundary) simultaneously.

### 6.3. Can it be saved with another monotone quantity $M(t,x)$?

For the class "discrepancy traces with theorem edges", no: Proposition 3.3 shows that any functional $M$ of $\mathcal{T}$ and its derivatives is a functional of the zero function in the interior. Any rescue requires changing the object (§8), at which point it is no longer P41's Form A with its two already-proved edges.

---

## 7. (v) The risk of circularity transmutation, run through the Doc 99 pattern

Doc 99's pattern (§4.3): *circularity is not eliminated; it is transmuted into non-uniformity of the passage to the limit, where it reappears under its usual name (MW-1/MW-6)*. We verify that Form A instantiates it exactly, in each of its incarnations:

| Field definition | Edge $x$ a theorem? | Edge $t$ a theorem? | Nontrivial interior? | Where RH ends up |
|---|---|---|---|---|
| (b) CF + DBN (this doc) | Yes (CF, mod ES$_x$) | Yes (DBN) | **No** (Thm. 3.2: $\equiv0$) | Discontinuity of the field on $\{x=\infty,\,t<\Lambda\}$: continuity at the corner $\equiv\lim_x\mathcal{T}(0,x)=T_{\lambda_0}(0)\equiv$ C2/MW-6/MW-1 (Doc 99 §5) |
| (a) pointwise Euler + heat | Vacuous (no zeros) | Not definable | — | The corner does not even exist (GAP 6.5 Doc 99: $\zeta_x\not\to$ on the line) = MW-2 |
| (c) Weil ledger | **No** (divergent series, Thm. 5.5) | Yes | Yes (the $\delta_p$) | In the series' regularization: the cancellation between the divergent prime block and the divergent archimedean block is the explicit formula with $W_\lambda w$, whose total positivity is Weil's criterion = MW-1 |
| hybrid with a rate (any nontrivial interior + quantitative $x$ edge) | rate, not theorem | Yes | Yes | Doc 99's E4: **any uniform finite$\to$full rate is effective RH** — circular |

The key row is the last one. By the dichotomy (Prop. 3.3), a nontrivial interior requires downgrading the arithmetic edge from "theorem = 0" to "quantitative size control"; but Doc 99 (E4) already showed that any uniform bound on the approximant–full spectral distance implies an effective version of C2, hence effective RH. That is:

> **The $\partial_t$–$\partial_x$ coupling, in any nonvacuous version, requires an RH-equivalent positivity/rate at the arithmetic-edge step.** Form A does not find a new mechanism: it re-presents the MW-1/MW-6 wall (via C2) or MW-2 (via the prime-tail divergence, now with exact constant $\tfrac{5\sqrt2}{8}$ in the Jacobi framework). Doc 99's transmutation reproduces without residue.

A fine point of candor in the opposite direction: none of the above uses RH-equivalent positivity *in this document's proved steps*. Theorems 3.2, 4.3, 5.3, 5.4, 5.5 are unconditional (modulo ES$_x$, which is a verifiable finite non-degeneracy, not a positivity). Circularity does not contaminate the results; it contaminates — as always — the single missing step, and this document's contribution is to show that that step cannot be a 2D propagation principle on the discrepancy trace.

---

## 8. What survives: the replacement object (Form A′), declared as a new problem

Theorem 3.2's degeneration indicates precisely what class of object would need to be used for a $(t,x)$ quadrant to have a nontrivial interior with some edge control:

**Candidate A′ (energy budget).** $M(t,x):=D(F_x^t)=2\int W_{\lambda_0}((F_x^t)')^2dm_\infty-\int(W_{\lambda_0}w)''(F_x^t)^2ds$ — the budget whose *difference* with its on-critical version is $\partial_t\mathcal{T}$ (Prop. 4.2). It is strictly nontrivial at finite $x$ ($D\neq0$ in general), computable, and its increment $\Delta_xM$ is read off the semilocal Weil form (adding prime $p$ adds $-W_p$ to the form, with explicit entries of the type in Doc 99 Lemma 5.1). Its $t$-evolution is that of a Dirichlet energy under backward heat, for which classical monotonicity/log-convexity formulas exist (Agmon; Almgren frequency). **Declared caveats:** (i) $M$ has no sign or RH-linked vanishing at the edges — the link to RH goes through $D(F)-D(F^{on})$, which reintroduces the zeros; (ii) any uniform control of $|M(t,x)-M(t,\infty)|$ is a finite$\to$full rate, under E4 suspicion. It is not Form A: it is a new problem, and its circularity audit is pending.

**Candidate A″ (negative package).** $\kappa(t,x):=\#\{\text{negative eigenvalues of }QW^N_{\mu(x)}\text{ deformed at time }t\}$ — the $(t,x)$ version of Doc 99's E5 and the index $\kappa=2m$ of P35/Doc 96. It is integer-valued, which connects it more to Form B (amplification) than to Form A. Outside this document's scope.

**Concrete next step if this direction is pursued:** compute $\Delta_2 M(0,\cdot)$ and $\partial_tM(0,x_2)$ for $S=\{2,3\}$ with the same closed machinery of §5 (the entries of $W_p$ against the Fourier basis are explicit; the $e^{tu^2}$ evolution on compact support is exact), and pass the result through the E4 filter **before** investing further effort. If $\Delta_xM$ and $\partial_tM$ also exhibit no stable sign relation, the entire family of Forms A on quadratic functionals of the approximant is closed.

---

## 9. VERDICT

### ROUTE CLOSED

**(for P41's Form A, Problem 6.2, with $\mathcal{T}=$ the CCM discrepancy trace of the evolved approximant — the paper's literal formulation).**

**Precise reason.** (1) The only definition of $\mathcal{T}(t,x)$ that makes both edges already-proved theorems (CF completion of Doc 99 for the arithmetic edge, DBN flow for the temporal one) annihilates the field **identically throughout the entire interior of the quadrant** (Theorem 3.2), because the forward DBN heat flow preserves the reality of zeros (de Bruijn's inheritance, Lemma 3.1) and the reality of the zeros is exactly the property defining the arithmetic edge. With an identically null interior, $\partial_t\mathcal{T}=\Delta_x\mathcal{T}=\partial_t\Delta_x\mathcal{T}=0$: every parabolic inequality, diagonal log-convexity, or monotone quantity is vacuous, and the corner $(0,\infty)$ remains a pure discontinuity of the field on the boundary $\{x=\infty\}$, whose removal is the 1D continuity wall (P41 §5.1) that Form A was meant to avoid. (2) The dichotomy is structural (Prop. 3.3): nontrivial interior $\Rightarrow$ some edge stops being a theorem, and then control of that edge is a finite$\to$full rate, which by E4 (Doc 99) is effective RH — circularity is transmuted to the limiting step exactly following Doc 99's pattern, without residue. (3) In the only nontrivial ledger (Weil side, §5), the sign test requested by P41 was carried out in exact closed form: the per-prime increments change sign at $p=11$ for the minimal window (positive at $2,3,5,7$; negative thereafter), the crossing point depends on the scale $\lambda_0$, the series diverges as $\tfrac{5\sqrt2}{8}\log X$ (the CCM test function is at the exact boundary of the Weil class), and the sign of $\partial_tT|_0$ under $\neg$RH is an OPEN GAP after correcting Docs 70–71. **There is no fixed sign relation or monotone diagonal: the falsifier declared in P41 fires, simultaneously in degenerate mode (interior) and oscillatory mode (boundary).**

**What remains standing (and is not Form A):** this document's new unconditional results — Theorem 3.2 (degeneration), Theorem 5.3 (closed form $B_{\lambda_0}(r)=\tfrac{c^{-1/2}}8(105\,\mathrm{sech}^4r-78\,\mathrm{sech}^2r+5)$), Theorems 5.4–5.5 (exact signs and Mertens divergence with constant $\tfrac{5\sqrt2}{8}$), the sign and completeness corrections to Docs 70–71 (Obs. 4.1, Prop. 4.2, Obs. 4.4–4.5) — and the new problem A′ (§8), with its mandatory E4 filter before any further investment. For the program's map: Form A is struck out; the pressure shifts entirely to Form B (index amplification, Doc 106) and to the E1/E2 statements of Doc 99.

---

## Appendix A — Algebraic verifications (closed form, no numerics)

### A.1. Derivatives of $g(r)=(\cosh r)^{-1/2}$ and consistency with the $a_k^\infty$

With $c=\cosh r$, $\sigma=\sinh r$, $\sigma^2=c^2-1$:
$$g'=-\tfrac12c^{-3/2}\sigma;\qquad g''=\tfrac34c^{-5/2}\sigma^2-\tfrac12c^{-1/2}=\tfrac14c^{-1/2}-\tfrac34c^{-5/2};$$
$$g'''=\tfrac14g'+\tfrac{15}8c^{-7/2}\sigma;\qquad g''''=\tfrac14g''+\tfrac{15}8\bigl[c^{-5/2}-\tfrac72c^{-9/2}\sigma^2\bigr]=\tfrac1{16}g-\tfrac{78}{16}c^{-5/2}+\tfrac{105}{16}c^{-9/2}.$$
(Intermediate step: with $\sigma^2=c^2-1$, $g''''=\tfrac14g''-\tfrac{75}{16}c^{-5/2}+\tfrac{105}{16}c^{-9/2}$ and $\tfrac14g''=\tfrac1{16}g-\tfrac3{16}c^{-5/2}$.) Values at $r=0$ ($c=1$): $g(0)=1$, $g''(0)=\tfrac14-\tfrac34=-\tfrac12$, $g''''(0)=\tfrac{1-78+105}{16}=\tfrac{28}{16}=\tfrac74$. Normalized moments of $dm_\infty$: $\langle s^2\rangle=-g''(0)=\tfrac12$ and $\langle s^4\rangle=g''''(0)=\tfrac74$. Jacobi side ($b_k=0$): $(J^2)_{00}=(a_0^\infty)^2=\tfrac{1\cdot2}4=\tfrac12$ ✓; $(J^4)_{00}=(a_0^\infty)^4+(a_0^\infty)^2(a_1^\infty)^2=\tfrac14+\tfrac12\cdot3=\tfrac74$ ✓. Exact measure–recursion consistency.

### A.2. The blocks $G_1, G_2$

$\int s^{2j}\cos(rs)\,dm_\infty=(-1)^j\widehat w^{(2j)}(r)$ with $\widehat w=(2\pi)^{-1/2}g$. With $P_0^2=\sqrt{2\pi}$:
$$G_1=\frac{P_0^2}{a_0^2}\int s^2\cos(rs)\,dm_\infty=\sqrt{2\pi}\cdot 2\cdot\bigl(-(2\pi)^{-1/2}g''\bigr)=-2g''=-\tfrac12g+\tfrac32c^{-5/2};$$
$$G_2=\frac{P_0^2}{a_0^2a_1^2}\int(s^2-\tfrac12)^2\cos(rs)\,dm_\infty=\tfrac23\bigl[g''''+g''+\tfrac14g\bigr]=\tfrac1{24}\bigl[9g-90c^{-5/2}+105c^{-9/2}\bigr],$$
using $(s^2-\tfrac12)^2=s^4-s^2+\tfrac14$, $\int s^4\cos\to+g''''$, $-\int s^2\cos\to+g''$. Checks: $G_1(0)=-\tfrac12+\tfrac32=1$ ✓, $G_2(0)=\tfrac{9-90+105}{24}=1$ ✓ (orthonormality). Sum:
$$B_{\lambda_0}=G_1+3G_2=\bigl(-\tfrac12+\tfrac98\bigr)g+\bigl(\tfrac32-\tfrac{45}4\bigr)c^{-5/2}+\tfrac{105}8c^{-9/2}=\tfrac58c^{-1/2}-\tfrac{39}4c^{-5/2}+\tfrac{105}8c^{-9/2},$$
which is $\tfrac{c^{-1/2}}8(5-78y+105y^2)$ with $y=c^{-2}=\mathrm{sech}^2r$. At $r=0$: $\tfrac{5-78+105}8=4=1+(a_1^\infty)^2=\int W_{\lambda_0}dm_\infty$ ✓.

### A.3. Rational evaluations of $Q(y)=105y^2-78y+5$

- $p=2$: $c=\tfrac54$, $y=\tfrac{16}{25}$. $Q=\tfrac{105\cdot256-78\cdot16\cdot25+5\cdot625}{625}=\tfrac{26880-31200+3125}{625}=-\tfrac{1195}{625}=-\tfrac{239}{125}<0$.
- $p=3$: $c=\tfrac53$, $y=\tfrac9{25}$. $Q=\tfrac{8505-17550+3125}{625}=-\tfrac{5920}{625}=-\tfrac{1184}{125}<0$.
- $p=5$: $c=\tfrac{13}5$, $y=\tfrac{25}{169}$. $Q=\tfrac{105\cdot625-78\cdot25\cdot169+5\cdot169^2}{169^2}=\tfrac{65625-329550+142805}{28561}=-\tfrac{121120}{28561}<0$.
- $p=7$: $c=\tfrac{25}7$, $y=\tfrac{49}{625}$. $Q=\tfrac{105\cdot2401-78\cdot49\cdot625+5\cdot625^2}{625^2}=\tfrac{252105-2388750+1953125}{390625}=-\tfrac{183520}{390625}<0$.
- $p=11$: $c=\tfrac{61}{11}$, $y=\tfrac{121}{3721}$. $Q=\tfrac{105\cdot14641-78\cdot121\cdot3721+5\cdot3721^2}{3721^2}=\tfrac{1537305-35118798+69229205}{13845841}=+\tfrac{35647712}{13845841}>0$.
- Monotonicity: $y_p=\bigl(\tfrac{2p}{p^2+1}\bigr)^2$ is strictly decreasing for $p\geq1$; $y_{11}<y_-<y_7$ because $Q(y_{11})>0>Q(y_7)$ and $y_\pm$ are the only roots. For every prime $p\geq11$, $y_p\leq y_{11}<y_-\Rightarrow Q(y_p)>0$.
- Powers: $2^2$: $c=\tfrac{17}8$, $y=\tfrac{64}{289}\in(y_-,y_+)\Rightarrow Q<0$. $2^3$: $c=\tfrac{65}{16}$, $y=\tfrac{256}{4225}=0.0606<y_-\Rightarrow Q>0$. $3^2$: $c=\tfrac{41}9$, $y=\tfrac{81}{1681}=0.0482<y_-\Rightarrow Q>0$.
- $B_{\lambda_0}(\log2)=\tfrac18\cdot\tfrac2{\sqrt5}\cdot\bigl(-\tfrac{239}{125}\bigr)=-\tfrac{239}{500\sqrt5}$; $B_{\lambda_0}(\log3)=\tfrac18\sqrt{\tfrac35}\cdot\bigl(-\tfrac{1184}{125}\bigr)=-\tfrac{148}{125}\sqrt{\tfrac35}$.

### A.4. Note on the domain of validity of integration by parts (Prop. 4.2)

The boundary terms $[W w\,GG']_{\pm\infty}$ and $[(Ww)'G^2]_{\pm\infty}$ vanish if $G^2(s)e^{-\pi|s|/2}\to0$, which holds for $G$ of exponential type $<\pi/2$ with polynomial growth on $\mathbb{R}$ (Paley–Wiener: $|G(s)|$ bounded on $\mathbb{R}$ for an $L^1$ kernel). For $F_{x_2}$ (type $\log\sqrt3<\pi/2$) and its evolution (same type) the condition holds. For $G=\Xi$ (order 1, infinite type in the real direction... $\Xi$'s actual real-line decay is faster than any exponential) the integral converges by $\Xi$'s own decay; we flag this because Doc 71 did not verify the boundary. Minor GAP declared: the uniform-in-$t$ verification of the boundary terms for $H_t$, $t>0$, is not written out (decay of $H_t$ on $\mathbb{R}$: standard by the integral representation, not included here).

---

## Appendix B — Sources and citations (backward-only)

| Source | Use | Status |
|---|---|---|
| Doc 64 (CTP), Doc 103 (Thm. 3.1, strict $W_\lambda>0$ and a single $\lambda_0$) | Definition of $\mathcal{T}$, corner = RH | Program, proved |
| Doc 70 (DBN flow on the trace; Obs. 3.1) | Temporal edge; $H_t$ convention | Program; the sign of §5.2 **corrected here** (Obs. 4.1) |
| Doc 71 (time derivative, quadratic form) | §4; **corrected** (on-critical block, normalization, curvature term, sign) | Program |
| Doc 72 (trace via the Weil formula, $B_\lambda$) | Ledger §5; its Thm. 4.1 is shown here to be **strictly formal** (Thm. 5.5) | Program |
| Doc 99 (CF rigidity, $H_x$, GAPs 6.2/6.5, E1–E6, §4.3 transmutation) | Definition (b); dichotomy §7; E4 filter | Program |
| P41 §Form A (Problem 6.2, falsifier) | Problem and test statement | Program |
| N. G. de Bruijn, *The roots of trigonometric integrals*, Duke Math. J. **17** (1950), 197–226, Thm. 13 | Lemma 3.1 (inheritance of reality under $e^{tu^2}$, strip $\sqrt{\Delta^2-2t}$) | Classical literature, verified through repeated use in the DBN literature (it is the standard citation of Rodgers–Tao) |
| B. Rodgers, T. Tao, *The De Bruijn–Newman constant is non-negative*, arXiv:1801.05914 (Forum Math. Pi 8 (2020)) | $\Lambda\geq0$; context for Lemma 3.1 | Literature, verified in Doc 70 |
| Beta integral / $\int|\Gamma(a+it)|^2e^{iut}dt=2\pi\Gamma(2a)(2\cosh\tfrac u2)^{-2a}$ | Lemma 5.1 | **Proved here** from the beta integral (self-contained; no table needed) |
| CCM-ZST arXiv:2511.22755; CvS CMP 406:312 (2025) | CF rigidity, $H_x$, even-simplicity | Verified in Doc 99 (Appendix A of Doc 99); used only through the statements checked there |

New results of this document: Lemma 3.1 (application), Theorem 3.2, Proposition 3.3 (dichotomy), Remark 4.1 (sign correction to Doc 70), Proposition 4.2 (corrected derivative with on-critical block and normalization), Theorem 4.3, Remarks 4.4–4.5, Lemma 5.1 (self-contained proof), Corollary 5.2, Theorem 5.3 (closed form of $B_{\lambda_0}$), Theorem 5.4 (sign change at $p=11$), Theorem 5.5 (Mertens divergence with constant $\tfrac{5\sqrt2}8$), Remark 5.6, the transmutation table in §7, and the A′/A″ classification of §8.

---

## Appendix C — Position of Doc 105 in the program's map

```
P41 — remaining logical forms after the 1D no-go
  │
  ├─ Form A (2D propagation, Problem 6.2)  ──►  Doc 105: ROUTE CLOSED
  │     │
  │     ├─ death mechanism 1 (interior): de Bruijn's inheritance
  │     │     (B2: real CF zeros) is invariant under (B1: DBN flow)
  │     │     ⟹ 𝒯 ≡ 0 on {x<∞, t≥0}  [Thm 3.2; dichotomy Prop 3.3]
  │     │     ⟹ the corner is the 1D continuity wall (P41 §5.1)
  │     │
  │     ├─ death mechanism 2 (boundary): Weil ledger
  │     │     B_{λ0}(r) = (c^{-1/2}/8)(105 sech⁴r − 78 sech²r + 5)  [Thm 5.3]
  │     │     δ_p > 0 for p^m ∈ {2,3,4,5,7};  δ_p < 0 for p^m ≥ 8  [Thm 5.4]
  │     │     Σ_p diverges ~ (5√2/8) log X  (boundary of the Weil class) [Thm 5.5]
  │     │     sign of ∂_t T|₀ under ¬RH: OPEN GAP  [Obs 4.5]
  │     │
  │     └─ circularity transmutation (Doc 99 §4.3 pattern): verified
  │           without residue — every nonvacuous version falls into C2/MW-1/MW-6,
  │           MW-2 (exact constant 5√2/8), or E4 (rate = effective RH)  [§7]
  │
  ├─ Form A′ (positive budget M(t,x) = D(F_x^t)): NEW problem,
  │     not audited; mandatory E4 filter before investing  [§8]
  │
  └─ Form B (index amplification): unaffected by this doc → Doc 106

Corpus corrections: Doc 70 §5.2 (sign of the DBN flow's PDE),
Doc 71 §§3–5 (on-critical block, normalization, curvature term;
the sign analysis of §4 is invalidated; the "algebraic condition on
the c_k" of §5.2 is the trivial identity D(Ξ)−D(Ξ)=0)  [Obs 4.1, Prop 4.2, Obs 4.4]
```

---

*End of Document 105.*
