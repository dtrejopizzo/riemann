# Document 167 — Dynamics of the index κ: quantization, Maslov walls, and the balance law of instability energy

**Program:** Riemann Hypothesis — Phase 54 (index dynamics)
**Prerequisites:** Phase 26 (κ=2m, Pontryagin space), Phase 28 (DBN = gradient of E_log), Phase 33 / Docs 70–72 (trace T_λ(t), time derivative, Weil formula), Phase 44 / Doc 132 (B.4, δ=1 forbidden), Phase 46 / Doc 143 (Lehmer exponent = 2; LP-134/LP-143), Phase 48 / Doc 144 (Hadamard counterexample, m=∞ analytic), Phases 52–53 (ζ IS the duality; the wall in Kreĭn language).
**Contract:** [NEW-DEFINITION] free; [THEOREM]/[PROP]/[LEMMA] with complete proof or unlabeled; [BRIDGE] honest; [GAP]/[WISH] declared. **This document does NOT attempt to prove κ=0.** The object is κ itself: its quantization, its walls, its dynamics.

---

## 0. Conventions and normalization

### 0.1. The function and the flow

$\Xi(z) = \xi(\tfrac12 + iz)$, entire of order 1, even, real on $\mathbb{R}$. A zero $\rho = \tfrac12 + b + i\gamma$ of $\zeta$ corresponds to the zero $z = \gamma - ib$ of $\Xi$; RH $\iff$ all zeros of $\Xi$ are real. The critical strip gives $|\mathrm{Im} z| < \tfrac12$ for every zero (Hadamard–de la Vallée Poussin's zero-free region gives the strict inequality).

De Bruijn–Newman flow in Polymath 15's normalization: with $\Phi$ the standard super-exponential density and

$$H_t(z) = \int_0^\infty e^{tu^2}\,\Phi(u)\cos(zu)\,du, \qquad H_0 = \tfrac18\,\Xi(\cdot/2)\ \text{(up to a fixed rescaling)},$$

one has the *backward* heat equation

$$\partial_t H_t = -\partial_z^2 H_t.$$

$\Lambda$ = the De Bruijn–Newman constant: $H_t$ has only real zeros $\iff t \ge \Lambda$. Hard facts used as input:

- **de Bruijn 1950** [dB]: $\Lambda \le \tfrac12$; the reality of the zeros is absorbing (if $H_{t_0}$ has real zeros, so does $H_t$ for $t \ge t_0$).
- **Newman 1976** [N]: $\Lambda > -\infty$; conjecture $\Lambda \ge 0$.
- **Ki–Kim–Lee 2009** [KKL]: $\Lambda < \tfrac12$; and for **every $t>0$**, $H_t$ has at most **finitely many** non-real zeros, and all but finitely many zeros are real and simple.
- **Rodgers–Tao 2020** [RT]: $\Lambda \ge 0$. Hence RH $\iff \Lambda = 0$.
- **Polymath 15, 2019** [P15]: $\Lambda \le 0{.}22$; zero dynamics $\partial_t x_k = 2\sum'_{j\ne k} 1/(x_k - x_j)$ (symmetrized sum).

### 0.2. The index

For a zero configuration $Z$ (a multiset in $\mathbb{C}$, closed under $z\mapsto\bar z$ and $z\mapsto -z$):

$$\kappa(Z) := \#\{z \in Z : \mathrm{Im} z > 0\} \quad (\text{with multiplicity}).$$

For $\zeta$: each off-line quadruple $\{\rho, \bar\rho, 1-\rho, 1-\bar\rho\}$ gives 4 non-real zeros of $\Xi$, of which 2 are in the upper half-plane; with $m$ = the number of quadruples, $\kappa = 2m$. This **coincides** with the Kreĭn index of Phase 26 (κ = neg.ind$(Q)$ = 2m): each quadruple contributes exactly one hyperbolic plane to the negative space of the Weil form. We write $\kappa(t) := \kappa(Z_t)$ with $Z_t$ = the zeros of $H_t$. By [KKL], $\kappa(t) < \infty$ for every $t > 0$ **unconditionally**; $\kappa(0) < \infty$ is half of the open finiteness statement ($m<\infty$), which **is not proved here**.

---

## 1. Level 1: κ as a topological invariant — the space 𝒞 and the walls

### 1.1. The configuration space

**[NEW-DEFINITION 1.1] (configuration space $\mathcal{C}$).** $\mathcal{C}$ is the set of locally finite multisets $Z \subset \{|\mathrm{Im} z| \le \tfrac12\}$ such that:

1. *(reality)* $\bar Z = Z$;
2. *(functional equation)* $-Z = Z$;
3. *(RvM density)* $N_Z(T) := \#\{z : |\mathrm{Re} z| \le T\} = \frac{T}{\pi}\log\frac{T}{2\pi e} + O(\log T)$;
4. *(genus)* $\sum_{z \in Z, z\neq 0} |z|^{-2} < \infty$ (automatic from 3).

Topology: induced by **local Hurwitz** convergence — $Z_n \to Z$ if the counting measures converge vaguely and, on every compact set whose boundary avoids $Z$, the counts eventually coincide. An **admissible path** is $u \mapsto Z_u$ continuous in this topology; we call it **proper** if there is a compact $K$ containing $\{z \in Z_u : \mathrm{Im} z \ne 0\}$ for every $u$ (the non-real zeros do not escape to infinity or enter from it).

*Why "proper" is needed:* in the vague topology alone, a non-real pair can slide toward $\mathrm{Re} z \to \infty$ and "disappear", changing κ without a local event. The property is the minimal honest hypothesis; for the DBN flow with $\kappa<\infty$ it holds automatically on compact time intervals (the zeros move with locally bounded velocity, Lemma 2.1).

### 1.2. The two walls

**[NEW-DEFINITION 1.2] (walls).** Within $\mathcal{C}$:

- **Collision wall** $W_{\mathrm{col}} := \{Z : Z$ has a real zero of multiplicity $\ge 2\}$. Codimension 1 (one real condition: the collision of two real zeros, or the landing of a conjugate pair, occurs at a point of the axis).
- **Siegel wall** $W_{\mathrm{Sieg}} := \{Z : Z$ has a non-real zero on the imaginary axis$\}$. There, the orbit of the Klein group degenerates from size 4 to size 2 ($\{i\beta, -i\beta\}$), and κ can be **odd**. For $\zeta$'s class (no real zeros of $\zeta$ in $(0,1)$) the relevant paths avoid $W_{\mathrm{Sieg}}$; this wall is exactly the one that breaks parity in the sense of "Siegel breaks parity" (Doc 140).

**[PROP 1.3] (parity).** On $\mathcal{C} \setminus W_{\mathrm{Sieg}}$, $\kappa \in 2\mathbb{Z}$.

*Proof.* The non-real zeros in the upper half-plane are permuted by $z \mapsto -\bar z$ (composition of the two symmetries), which preserves $\mathrm{Im} z$. Outside $W_{\mathrm{Sieg}}$ this involution has no fixed points in $\{\mathrm{Im} z > 0\}$ (a fixed point satisfies $\mathrm{Re} z = 0$). A finite set —or each stratum of a multiset— with a free involution has even cardinality. $\square$

This re-derives "δ=1 forbidden" (Doc 132) in configurational language: parity is a phenomenon of **Klein-group theory**, not of positivity.

### 1.3. κ is locally constant away from the walls: the degree theorem

**[THEOREM 1.4] (homotopic quantization of κ).** Let $u \mapsto F_u$ be a family of real entire functions on $\mathbb{R}$, even, of order $\le 1$, not identically zero, continuous in the topology of locally uniform convergence on $\mathbb{C}$, with zero configurations $Z_u \in \mathcal{C}$, $\kappa(Z_u) < \infty$ for every $u$, and a **proper** path. Then:

1. $u \mapsto \kappa(Z_u)$ is locally constant on $\{u : Z_u \notin W_{\mathrm{col}} \cup W_{\mathrm{Sieg}}\}$;
2. at a crossing of $W_{\mathrm{col}}$ where a single simple conjugate pair lands on (or departs from) a point $x_0 \ne 0$ of the axis, κ jumps by exactly $\mp 2$ (the pair and its mirror $-x_0$ land simultaneously by the parity of $F$; each landing contributes $\mp 1$ to the upper-half-plane count);
3. κ admits a **degree** representation: for any rectangle $R = [a,b] \times [\eta, \tfrac12 + \eta']$ with $\partial R \cap Z_u = \emptyset$ containing all the zeros in the strict upper half-plane,

$$\kappa(Z_u) = \frac{1}{2\pi i} \oint_{\partial R} \frac{F_u'(z)}{F_u(z)}\,dz = \deg\left(\frac{F_u}{|F_u|} : \partial R \to S^1\right).$$

*Proof.* (3) is the argument principle: the zeros inside $R$ are exactly the non-real ones in the upper half-plane (the real ones are excluded because $\eta > 0$; properness and $\kappa<\infty$ allow such an $R$ to be chosen). (1): by Hurwitz, if $Z_{u_0}$ does not touch $\partial R$, for $u$ near $u_0$ the count in $R$ is constant; one must be able to keep $\eta > 0$ fixed: this fails only if non-real zeros approach the axis, which in the limit produces a real zero of multiplicity $\ge 2$ (the zeros arrive in conjugate pairs, and the real limit point absorbs both) — i.e., only on $W_{\mathrm{col}}$; or if a non-real zero crosses $\mathrm{Re} z = 0$... which does not change the count (the involution preserves it), unless it is *on* the imaginary axis landing at $0$, the case $W_{\mathrm{Sieg}} \cap W_{\mathrm{col}}$. Properness excludes escapes through the vertical sides (one chooses $a,b$ outside the compact set $K$). (2): locally, near the landing, $F_u(z) = c(u)\,(z - z_+(u))(z - z_-(u))\,G_u(z)$ with $G$ non-vanishing, $z_\pm = x_0(u) \pm i\beta(u)$ before the crossing and $z_\pm$ real afterward; the count in a small disk around $x_0$ drops from 1 (upper half-plane) to 0, and the parity of $F$ duplicates the event at $-x_0$. $\square$

**Reading.** κ **is** a topological invariant: the degree of $F/|F|$ on the boundary of the instability band. It is not locally constant on all of $\mathcal{C}$ — and that is correct: if it were, the DBN flow could not bring κ down to 0. It is locally constant **between walls**, and the walls are exactly the collision events on the critical axis. The answer to "of what space is κ a π₀?": κ classifies the connected components of $\{$proper paths$\} \setminus (W_{\mathrm{col}} \cup W_{\mathrm{Sieg}})$, i.e., $\kappa$ is the universal locally constant function of the complement of the walls (together with trivial discrete data).

### 1.4. The wall is a Kreĭn collision: why "Maslov" is the right name

**[BRIDGE 1.5] (signature collision).** Via Phase 26's bridge-theorem (κ = neg.ind of the Weil form $Q$; the off-line zeros = non-real eigenvalues of the $Q$-symmetric operator $H_C$ in the Pontryagin space $(\mathcal{K}, Q)$), the crossing of $W_{\mathrm{col}}$ is exactly the classical mechanism of **Kreĭn collision**: in a space with an indefinite product, a pair of real eigenvalues of a $Q$-self-adjoint operator can only leave the real axis via the collision of two eigenvalues of **opposite Kreĭn signature**; at the collision a Jordan block forms and the pair exits to $\mathbb{C}$ carrying away a hyperbolic plane (a $+$ and a $-$) of the space. This is the strong-stability criterion of Kreĭn (1950) and Gel'fand–Lidskii (1955) for linear periodic Hamiltonian systems; modern exposition: MacKay 1986; abstract framework: Bognár 1974, Azizov–Iokhvidov 1989. The bridge's status is honest: the full operatorial identification depends on Phase 26's V.1–V.4 (open); the **configurational** version (Theorem 1.4) is unconditional.

**This is the structural answer to the director's question (level 1):** the negative directions come in discrete packets because *they are born in pairs through signature collisions* — the same mechanism by which the unstable modes of a stable Hamiltonian system do not appear gradually but in quanta, at Kreĭn resonances. In physics this produces index-counting theorems (Kapitula–Kevrekidis–Sandstede 2004, "Counting eigenvalues via the Krein signature...": the number of unstable modes is bounded by the negative index of the energy; the Vakhitov–Kolokolov 1973 criterion as the scalar case). The dictionary is exact: unstable modes ↔ off-line quadruples; negative index of the energy Hessian ↔ κ = neg.ind(Q); Kreĭn resonance ↔ a Lehmer pair at the wall.

The name "Maslov": the jump of κ at transversal crossings of a signed codimension-1 wall is formally an intersection index of Maslov type (Arnol'd 1967; Robbin–Salamon 1993, spectral index via crossings). $m = \kappa/2$ is the signed intersection number of the path with $W_{\mathrm{col}}$, relative to the final state κ=0.

### 1.5. The Lehmer exponent = 2 is the wall's normal fold

**[PROP 1.6] (fold normal form).** Let $u \mapsto F_u$ be as in Theorem 1.4, with a crossing of $W_{\mathrm{col}}$ at $u = u_0$, $x_0$ a real double zero of $F_{u_0}$, and suppose transversality: $\partial_u [\text{local discriminant}] \ne 0$. Then there are local coordinates in which the two zeros are $x_0 \pm \sqrt{c\,(u - u_0)} + O(u-u_0)$, $c \neq 0$. In particular: on the "real" side of the wall, the **gap** between the two real zeros scales as $|u - u_0|^{1/2}$, i.e. $\text{gap}^2 \asymp \text{distance to the wall}$; on the "complex" side, the **height** $\beta$ of the pair scales the same way: $\beta^2 \asymp \text{distance to the wall}$.

*Proof.* Weierstrass: locally $F_u(z) = e(z,u)\,(z^2 + a_1(u) z + a_0(u))$ with $e \ne 0$ and $a_i$ continuous (of the class of the family); the crossing is the zero of the discriminant $\Delta(u) = a_1^2 - 4a_0$; transversality ⟹ $\Delta(u) \sim c'(u-u_0)$; the zeros are $(-a_1 \pm \sqrt{\Delta})/2$. $\square$

**[BRIDGE 1.7] (unification with Doc 143 and LP-134/LP-143).** The "exact Lehmer exponent = 2" of Doc 143 (Gram–Vandermonde bound: the cost of a near-double-zero enters squared, with an antisymmetric witness) is the *static* manifestation of the fold: the quadratic form sees $\text{gap}^2$ because the wall is quadratic in the transversal coordinate. The two conjectural repulsions are the two lateral distances to the **same** wall, normalized at the local scale $1/\log\gamma$:

- LP-143 ($\liminf \text{gap}\cdot\log\gamma > 0$): the arithmetic point does not approach $W_{\mathrm{col}}$ **from the real side** (the $t = 0^+$ side of the flow);
- LP-134 ($\liminf |\beta - \tfrac12|\cdot\log\gamma > 0$, in coordinate $b = \beta_{\mathrm{off}}$): it does not approach **from the complex side** ($t = 0^-$ side).

Doc 143's "heuristic DBN bridge" (same boundary) thus gains a geometric home: both are transversality of the arithmetic point to the collision wall, measured in the metric rescaled by the RvM density. *Status:* the identification of the two transversal coordinates with the two sides of the same wall is a local theorem (Prop 1.6); the repulsions themselves remain LP (open, and LP-143 conjecturally false under GUE in its uniform form — Doc 143; the correct modulus is relative to the gap).

---

## 2. Levels 1→3: the balance law of instability energy

This is the document's main new content. Docs 70–72 computed $\partial_t T_\lambda$ (a *weighted* trace) and found a quadratic form with arithmetic cancellation under RH. Read as physics: $T_\lambda$ is a Lyapunov energy with spectral weights. We strip the weights and work with the bare geometric energy; the result is cleaner than the weights let one see: **the law is purely dissipative, with a universal rate quantized by κ.**

### 2.1. The zero dynamics

**[LEMMA 2.1] (well-posedness of the dynamics; CSV94, P15, KKL).** Let $t_0 > 0$ and $J \ni t_0$ an interval on which all zeros of $H_t$ are simple. Then the zeros admit real-analytic parametrizations $z_k(t)$ on $J$ with

$$\dot z_k = 2 \sum_{j \ne k}{}^{\!\!'} \frac{1}{z_k - z_j},$$

where $\sum'$ is the symmetrized sum (grouping $z_j$ with $-z_j$, or truncating symmetrically), absolutely convergent after grouping thanks to the RvM density ($\sum_j |z_k - z_j|^{-2} < \infty$, and symmetric grouping reduces the distant terms to $O(|z_j|^{-2})$).

*Proof.* Standard: $0 = \frac{d}{dt} H_t(z_k(t)) = \partial_t H_t + H_t'\,\dot z_k = -H_t'' + H_t' \dot z_k$ at $z_k$, hence $\dot z_k = H_t''/H_t'(z_k)$, and for an entire function of genus 1, real and even with simple zeros, $H''/H'(z_k) = 2\sum'_{j\neq k} (z_k - z_j)^{-1}$ (logarithmic derivative of the Hadamard product; the linear exponential factor vanishes by parity). The real version is exactly the equation of [RT, §2] and [P15]; the extension to isolated complex zeros is identical (local holomorphy + implicit function theorem). By [KKL], for $t > 0$ the hypotheses (finitely many non-real, almost all simple) hold, and collision times are locally finite. $\square$

### 2.2. The instability energy

**[NEW-DEFINITION 2.2] (instability energy).**

$$I(t) := \sum_{\substack{z_k(t)\,:\, \mathrm{Im} z_k > 0}} (\mathrm{Im} z_k(t))^2 \;=\; \sum_{k \text{ upper}} \beta_k(t)^2 .$$

It is half of the total second imaginary moment. For $t > 0$ it is a finite sum [KKL]. $I(t) = 0 \iff \kappa(t) = 0$, and $\Lambda = \inf\{t : I(t) = 0\}$ — the geometric version of Doc 70's Theorem 4.1 ($\Lambda$ as the extinction time of $T_\lambda$).

### 2.3. The balance law

**[THEOREM 2.3] (balance law, pure dissipation with quantized rate).** Let $J$ be a time interval $> 0$ on which $\kappa(t) \equiv \kappa$ is finite and constant and all zeros are simple. Write $z_k = \alpha_k + i\beta_k$ ($\beta_k > 0$) for the upper-half-plane zeros and $x_j$ for the real ones. Then, on $J$:

$$\boxed{\;\frac{dI}{dt} \;=\; -\,2\,\kappa(t)\;-\;D(t), \qquad D(t) \ge 0\;}$$

with explicit dissipation

$$D(t) = 4\sum_{k \text{ upper}} \beta_k^2 \left[ \sum_{x_j \in \mathbb{R}} \frac{1}{|z_k - x_j|^2} + \frac{1}{2|z_k|^2} \right] \;+\; 2\sum_{\substack{k \ne l \text{ upper}}} \left[ \frac{(\beta_k - \beta_l)^2}{|z_k - z_l|^2} + \frac{(\beta_k - \beta_l)^2}{|z_k + \bar z_l|^2} + \frac{(\beta_k + \beta_l)^2}{|z_k - \bar z_l|^2} + \frac{(\beta_k + \beta_l)^2}{|z_k + z_l|^2} \right]$$

(sum over ordered pairs; each term is manifestly $\ge 0$; if $z_k$ lies on the imaginary axis the coinciding mirror terms are counted once).

*Proof.* By Lemma 2.1, $\dot\beta_k = \mathrm{Im} \dot z_k = -2\sum_{w \in Z \setminus \{z_k\}} \dfrac{\beta_k - \mathrm{Im} w}{|z_k - w|^2}$, hence

$$\frac{dI}{dt} = \sum_{k \text{ upper}} 2\beta_k \dot\beta_k = -4 \sum_{k \text{ upper}} \sum_{w \ne z_k} \frac{\beta_k(\beta_k - \mathrm{Im} w)}{|z_k - w|^2}.$$

We classify $w$:

1. **The zero's own conjugate $w = \bar z_k$:** $\beta_k(\beta_k - (-\beta_k))/|2i\beta_k|^2 = 2\beta_k^2/4\beta_k^2 = \tfrac12$. Contribution: $-4 \cdot \tfrac12 = -2$ **per upper-half-plane zero**, total $-2\kappa(t)$. *This is the universal term: it does not depend on where the zero is, only on its existence.*
2. **The mirror $w = -\bar z_k$:** $\mathrm{Im} w = \beta_k$, contribution $0$.
3. **The antipode $w = -z_k$:** $\beta_k(2\beta_k)/|2z_k|^2 = \beta_k^2/(2|z_k|^2)$; contribution $-2\beta_k^2/|z_k|^2 \le 0$.
4. **Real zeros $w = x_j$:** $\beta_k^2/|z_k - x_j|^2$; contribution $-4\beta_k^2 \sum_j |z_k - x_j|^{-2} \le 0$ (convergent by RvM).
5. **Other upper zeros and their orbits** $w \in \{z_l, \bar z_l, -z_l, -\bar z_l\}$, $l \ne k$: the terms with $\mathrm{Im} w = \beta_l$ give $\beta_k(\beta_k - \beta_l)/d^2$ with $d \in \{|z_k - z_l|, |z_k + \bar z_l|\}$, symmetric under $k \leftrightarrow l$; summing the ordered pairs $(k,l)$ and $(l,k)$: $\beta_k(\beta_k - \beta_l) + \beta_l(\beta_l - \beta_k) = (\beta_k - \beta_l)^2$. The terms with $\mathrm{Im} w = -\beta_l$ similarly give $(\beta_k + \beta_l)^2$ with $d \in \{|z_k - \bar z_l|, |z_k + z_l|\}$. All $\le 0$ after symmetrizing.

Summing, $dI/dt = -2\kappa - D$ with $D \ge 0$ as stated. Absolute convergence of each block is guaranteed by $\kappa < \infty$ and RvM. $\square$

**Structural remarks.**

- **The universal rate $-2\kappa$ is the dynamical quantization of the index:** each unstable mode dissipates instability energy at exactly rate 2, via interaction with its own conjugate, *regardless of the configuration*. Energy cannot leak gradually: it is lost in quanta of slope 2 per mode.
- **There is no source term.** This answers the mandate's central question (point 2): under the DBN flow there is no "arithmetic source" feeding instability. The law is purely dissipative. The primes are **not a force** on the zeros: the heat flow knows no arithmetic. All the arithmetic is in the **initial condition** $Z_0$ (and, dually, in the Weil representation of that initial condition: Doc 72). See §4.
- **Monotonicity of Doc 70's Conj. 5.1, resolved in the geometric version:** $I$ is strictly decreasing while $\kappa > 0$. (Monotonicity of the weighted trace $T_\lambda$ remains open; the weights may break it locally, but the bare energy does not.)

### 2.4. Corollaries: virials for Λ

**[COR 2.4] (extinction bound).** If on $(t_0, \Lambda)$ the collision times are locally finite and $\kappa < \infty$ (true for $t_0 > 0$ by [KKL]), then, since $\kappa(t) \ge 2$ for every $t < \Lambda$ (parity, Prop 1.3, and $\kappa > 0$ by the definition of $\Lambda$):

$$\frac{dI}{dt} \le -4 \quad \text{on } (t_0, \Lambda) \qquad\Longrightarrow\qquad \Lambda \;\le\; t_0 + \tfrac14\, I(t_0).$$

($I$ is continuous through the collisions: the zeros move continuously and at a landing the term that goes extinct tends to 0.) In particular, if $\kappa(0) < \infty$ (half of finiteness, **not proved**): $\Lambda \le \tfrac14 I(0^+) \le \tfrac14 \cdot \kappa(0)\cdot \sup_k \beta_k(0)^2 \le \kappa(0)/16$, using $\beta \le 1/2$. *Honestly:* this chain is **conditional on $m < \infty$**; it does not compete with [dB]/[KKL] (unconditional) except when $\kappa(0)$ is small, and it is in the same spirit as the "energy" barrier method of [P15].

**[COR 2.5] (the boundary $\Lambda = 0$ as an energy balance; reformulation of Rodgers–Tao).** By [RT], $\Lambda \ge 0$, hence $\kappa(t) > 0$ for every $t < 0$. On any interval $(t, 0)$ where the dynamics is well defined and $\kappa$ is finite, Theorem 2.3 gives $I(t) \ge I(0^+) + 4|t|$; if $\kappa$ or $I$ are infinite on $(t,0)$ the conclusion holds trivially. That is:

$$I(t) \;\ge\; 4\,|t| \qquad \text{for every } t < 0,$$

and RH is equivalent to this linear bound being *exact at the boundary*: RH $\iff I(0^+) = 0 \iff$ the instability energy of the arithmetic point, looked at backward in time, takes off from zero at the universal minimum quantized slope $4$. The arithmetic point lies **exactly on the boundary of the basin** not as a metaphor: it is the point where the Lyapunov functional touches zero with the minimum quantized slope.

**[PROP 2.6] (the dynamical fold: Lehmer = 2 again).** At an isolated landing at $t_c$ ($\beta_k(t_c) = 0$, the other zeros at distance $\ge d > 0$), the equation for $\beta_k$ is $\dot\beta_k = -1/\beta_k + O(1)$, hence

$$\beta_k(t)^2 = 2\,(t_c - t)\,(1 + o(1)), \qquad t \to t_c^-,$$

and symmetrically the real gap after the landing opens as $\mathrm{gap}(t)^2 \asymp (t - t_c)$. *Proof:* the own-term dominates ($-1/\beta_k \to -\infty$) and the ODE $\beta\dot\beta = -1 + O(\beta)$ integrates directly. $\square$

The exponent $1/2$ ($\beta \sim \sqrt{2(t_c - t)}$) is the **same fold** as Prop 1.6: the static wall (Gram–Vandermonde, Doc 143) and the dynamic landing have the same normal form. Lehmer's "2" is the degree of the discriminant in the coordinate transversal to the wall — a single object seen in two charts (static $u$, dynamic $t$). And CSV 1994 closes the circle from the other side: Lehmer pairs (near-collisions at $t=0$) force lower bounds on $\Lambda$ — i.e., being *close to the wall from the real side at $t=0$* implies *having been on the complex side for $t<0$ just before* — exactly the two-sides-of-the-same-wall reading of Bridge 1.7.

### 2.5. What is conserved?

An honest and complete answer:

1. **The parity of κ** (outside $W_{\mathrm{Sieg}}$): absolutely conserved. Trivial but not vacuous: it is what forbids escaping "one at a time".
2. **κ between walls:** conserved (Theorem 1.4) — κ is the "topological charge" and the walls are the only de-excitation vertices. Together with the sign of the crossing: under DBN the crossings are **only downward** ([dB]: absorbing reality; our Cor 2.4 quantifies it). κ is a monotone stepped integer: the cascading de-excitation of a quantized system.
3. **There is no nontrivial conserved momentum.** The first moment $\sum' z_k$ is conserved (= 0 by symmetry, trivially). The candidate $I$ does **not** conserve: it decreases — and that is the thesis: the correct structure is not a conservation law but a **Lyapunov pair $(\kappa, I)$** with coupled one-sided laws: κ stepped non-increasing, $I$ absolutely continuous with $\dot I = -2\kappa - D$. The identity of Docs 70–72 ($\partial_t T_\lambda|_{t=0}$ as a quadratic form with exact cancellation under RH) is the weighted shadow of this law: under RH, $\kappa = 0$, $I \equiv 0$, and Doc 72's "exact arithmetic cancellation" is the statement that the prime representation of the initial condition has no instability component — i.e., Weil positivity. The balance law does not prove it; it *locates* it as an initial datum.

---

## 3. Level 2 characterized dynamically: finiteness as non-explosion at the boundary

We do not prove $m < \infty$ (mandate). We characterize it.

**[PROP 3.1] (instantaneous regularization, unconditional).** For every $t > 0$: $\kappa(t) < \infty$ and $I(t) < \infty$. *Proof:* [KKL]. $\square$

That is: the flow lands **instantaneously** in the finite-index stratum. The whole difficulty of level (2) is the behavior as $t \to 0^+$:

**[PROP 3.2] (the half of finiteness as a boundary condition).**

1. $\kappa(0) < \infty \implies \kappa(t) \le \kappa(0)$ for $t \ge 0$ and $\limsup_{t\to 0^+}\kappa(t)<\infty$ (the non-real zeros of $H_t$ for small $t$ come, by Hurwitz, from the non-real ones of $H_0$ or from collisions of real ones — under the flow collisions only *destroy* pairs — [dB]).
2. $I(0^+) := \lim_{t \to 0^+} I(t)$ exists in $[0,\infty]$ ($I$ is monotone), and $I(0^+) < \infty \iff \int_0^s [2\kappa(u) + D(u)]\,du < \infty$: the finiteness of the *initial energy* is the **integrability of κ at the boundary**, not its boundedness.
3. $I(0^+) < \infty$ is **strictly weaker** than $\kappa(0) < \infty$: Doc 144's Hadamard counterexample (analytic class, $m = \infty$, heights $\delta_j = e^{-\gamma_j}$) has $\sum_j \delta_j^2 < \infty$, i.e. finite instability energy with infinite index.

*Proof of 3:* immediate from the definition of $I$. $\square$

**Reading (a new quantitative stratification of level 2).** Between "κ(0) = 0" (RH) and "κ(0) < ∞" (half of finiteness) and "no condition" there is a genuine intermediate step: $I(0^+) < \infty$ (finite energy, possibly infinite index). The hierarchy
$$\kappa(0)=0 \;\subsetneq\; \kappa(0)<\infty \;\subsetneq\; I(0^+)<\infty \;\subsetneq\; \mathcal{C}$$
is strict in the analytic class (Doc 144 separates the two middle ones). An open question pointed out, weaker than $m<\infty$ and perhaps attackable via the Fredholm route of B.4:

**[GAP 167.A] Is $I(0^+) < \infty$ provable for ζ?** Equivalently: is $\kappa(t)$ integrable as $t \to 0^+$? Note that this is a "time-average" type statement, on the good side of the master quantifier (Phase 44's key observation: the essential spectrum lives on the average side); and that $I(0^+)<\infty$ is exactly "$\sum_j b_j^2 < \infty$ over the off-line zeros", the $\ell^2$ version of finiteness — the quadratic analogue of the half-finiteness statement, in the same coordinate where the Lehmer exponent is 2. [WISH: that B.4 (essential positivity modulo compacts) imply the $\ell^2$ version before the counting version.]

---

## 4. Why pairs and not a continuum? — what arithmetic adds

Answer in three layers, with the required candor:

**(a) Discreteness is cheap.** Any object in ξ's class (entire of order 1, real on the line, functional equation) has isolated zeros; the "negativity" of the associated Weil form is supported on atoms (each quadruple contributes a finite-dimensional hyperbolic plane to the negative space — Phase 26/44). A "continuous density of negativity" would require continuous non-real spectrum, impossible for a nonzero entire function. **This is not deep:** it is Hadamard. In the analytic class the quantization is free.

**(b) Parity and pairing are symmetry, not arithmetic.** κ ∈ 2ℤ is the Klein group (Prop 1.3); birth/death in pairs is the Kreĭn collision (Bridge 1.5) — valid for any $Q$-dynamics, with not a single prime.

**(c) Finiteness is the only thing arithmetic must pay for — and it is the Fredholm half again. We say this plainly.** Doc 144's counterexample shows $m = \infty$ realizable analytically: no topological-charge argument in the analytic class can give κ < ∞. What arithmetic adds is not an extra quantization mechanism, but (conjecturally) a **compactness obstruction**: B.4 (Doc 132) says essential positivity modulo compacts ⟹ δ < ∞; the arithmetic content needed is that the "symbol" of the Weil form (the part seen by the primes on average) be positive, leaving the negativity in a compact set. This document adds only two things to that picture: (i) the dynamical version — finiteness is a condition at the **boundary of the flow** ($\kappa(t)$ bounded or at least integrable as $t\to 0^+$, Prop 3.2), not a mysterious static condition: the interior $t>0$ is already finite for free [KKL]; (ii) the intermediate step $I(0^+)<\infty$ (GAP 167.A), which is the $\ell^2$ —not counting— form of finiteness, and therefore the first candidate if the route is spectral-essential. Honest verdict on mandate point 3: **"nothing new" regarding the quantization mechanism; finiteness is Fredholm; what is new is the coordinate (boundary of the flow, $\ell^2$ norm) in which the Fredholm half must be measured.**

---

## 5. Anti-circularity test

Applied to each object built:

| Object | RH-free? | ζ-free? | Where ζ re-enters |
|---|---|---|---|
| $\mathcal{C}$, walls, Theorem 1.4 (κ degree) | yes | **yes** (holds for the whole class) | does not re-enter |
| Kreĭn collision (configurational version) | yes | yes | does not re-enter; the operatorial version inherits V.1–V.4 |
| Fold / Lehmer = 2 (Props 1.6, 2.6) | yes | yes | does not re-enter |
| **Balance law** $\dot I = -2\kappa - D$ (Thm 2.3) | **yes** | **yes** (heat + Hadamard; not a single prime in the proof) | does not re-enter |
| Cor 2.5 ($I(t) \ge 4|t|$, $t<0$) | yes | **no**: uses [RT] | ζ enters via Rodgers–Tao (local zero statistics) |
| **Value** $I(t_0)$, $I(0^+)$, $\kappa(0)$ | — | **no**: computing them = knowing the zeros | in the initial condition |

**The predicted pattern is confirmed and precisely localized.** The LAW (the equation of motion of instability) is RH-free and in fact ζ-free: it is a theorem of the Pólya class. The initial VALUE is not — and it *cannot* be: by Phase 52, ζ IS the duality, and the flow's initial condition is exactly the "zeros" side of the duality. The novelty relative to Phase 52 is the clean separation: there every auxiliary structure reintroduced ζ at its core; here there is a structure (the dynamics) that demonstrably does **not** contain ζ, and a datum (the initial condition) that contains **everything**. It is exactly "knowing the equation of motion without the initial condition".

Two nuances that prevent inflating the conclusion:

1. **RH-free computable avatars of the initial datum exist, but with a sign, not squared.** The Li coefficients $\lambda_n = \sum_\rho [1 - (1 - 1/\rho)^n]$ (Li 1997; Bombieri–Lagarias 1999) and the values $(\log\xi)''(\tfrac12) = -\sum_\rho (\rho - \tfrac12)^{-2}$ are computable without knowing the zeros (from the Taylor coefficients of $\log\xi$, i.e. the Stieltjes constants — RH-free), and are *signed moments* of the same configuration whose *positive quadratic moment* is $I(0)$. The exact obstruction: extracting from the signed holomorphic moments the positive-definite quantity $\sum b_j^2$ is the usual positivity problem (RH ⟺ $\lambda_n \ge 0$). The wall did not move; it was located in "signed moment → quadratic moment".
2. **The only dynamical statement with arithmetic content (Cor 2.5) inherits its arithmetic entirely from [RT].** There is no new arithmetic in this document; it is *imported* and kept separate from the rest.

---

## 6. Verdict

### New theorems (level 1 and the balance law)

- **[THEOREM 1.4 + Props 1.3, 1.6]** κ is a genuine topological invariant: the degree of $F/|F|$ on the boundary of the instability band, locally constant on proper paths outside two explicit walls ($W_{\mathrm{col}}$, $W_{\mathrm{Sieg}}$), with jumps of $\pm 2$ at transversal crossings and a fold normal form — which identifies the Lehmer exponent = 2 (Doc 143) as the degree of the wall's discriminant, and LP-134/LP-143 as the two lateral distances to the same wall (Bridge 1.7). The question "of what is κ a π₀?" has an answer: of the complement of the walls in the space of proper paths of $\mathcal{C}$.
- **[THEOREM 2.3]** Balance law: $\dot I = -2\kappa - D$, $D \ge 0$ explicit; pure dissipation with a **universal quantized rate $-2$ per unstable mode** (arising from each zero's interaction with its own conjugate), with no source term. Corollaries: strict monotonicity of $I$ (resolves the geometric version of Conj. 5.1, Doc 70); virial $\Lambda \le t_0 + I(t_0)/4$ (Cor 2.4); dynamical fold $\beta^2 = 2(t_c - t)(1+o(1))$ (Prop 2.6).
- **[PROP 3.2]** A new stratification of level 2: $\kappa(0)<\infty \subsetneq I(0^+)<\infty$ (strict by Doc 144); the half of finiteness is a boundary condition of the flow (the interior is finite unconditionally by [KKL]); GAP 167.A ($I(0^+)<\infty$, the $\ell^2$ finiteness) named as a target strictly weaker than $m<\infty$ and on the "average" side of the master quantifier.

### Reformulations (new language, old wall — declared as such)

- **The boundary $\Lambda = 0$ as an energy balance** (Cor 2.5): RH ⟺ the instability energy, looked at backward from the arithmetic point, takes off with the minimum quantized slope ($I(t) \ge 4|t|$, $t<0$, via [RT]). It is not easier than RH; it is the same boundary with a stability-proof structure.
- **"No arithmetic source":** the primes are not a force in the flow but the dual (Weil, Doc 72) representation of the initial condition; the director's question "why doesn't the source feed instability at $t=0$?" transforms into: "why does the prime representation of the initial datum lack an instability component?" = Weil positivity. Localization, not progress.
- **Quantization (mandate point 3):** mechanically resolved and deflated — discreteness = Hadamard, parity = Klein, pairs = Kreĭn collision; arithmetic is only necessary (and sufficient, if B.4 were realized) for **finiteness**, which is the Fredholm half again. Said plainly, as the contract demands.

### Stability tools pointed at the gap, with precise conditions

1. **Łojasiewicz–Simon** (Łojasiewicz 1963; Simon 1983): the DBN flow is the gradient of $E_{\log}$ (Phase 28). A Łojasiewicz inequality at the RH configuration would give landing rates and basin rigidity. **Exact applicability condition: the Hessian of $E_{\log}$ is Fredholm at the limit configuration** — which is *literally* B.4/the half of finiteness. The program's two halves ("m<∞" and "m<∞⟹m=0") meet in the hypothesis and conclusion of a single stability theorem: this is the cleanest welding point we know.
2. **Hamiltonian index-counting theorems** (Kreĭn 1950; Gel'fand–Lidskii 1955; MacKay 1986; Vakhitov–Kolokolov 1973; Grillakis–Shatah–Strauss 1987; Kapitula–Kevrekidis–Sandstede 2004): the dictionary κ = negative index of the energy ⟹ a bound on unstable modes is exactly the "(1) bound before excluding" direction. Applicability condition: Phase 26's operatorial identification (V.1–V.4); meanwhile, the configurational version (this document) already gives the count.
3. **Virial identities:** realized here (Cor 2.4/2.5): $I$ is the correct virial of the flow, with quantized slope. What a virial cannot do: distinguish $I(0^+) = 0$ from small $I(0^+)$ — that is the initial condition, i.e. the wall.

### Declared [GAPs]

- **GAP 167.A:** is $I(0^+) < \infty$ for ζ? ($\ell^2$ finiteness; weaker than $m<\infty$).
- **GAP 167.B:** monotonicity of the weighted trace $T_\lambda(t)$ (Conj. 5.1 Doc 70) — the bare version is resolved (Thm 2.3); the weighted one requires controlling the commutator of the weights with the dissipation.
- **GAP 167.C:** the operatorial version of the wall (Kreĭn collision for $H_C$ in $(\mathcal{K},Q)$) inherits Phase 26's V.1–V.4.
- **[literature GAP]:** monotonicity of the *count* of non-real zeros under the flow (used only in Prop 3.2.1 via [dB]) is in de Bruijn 1950 for absorbing reality; the quantitative pairwise version we use is derived here from the dynamics (Lemma 2.1), not from the literature; and we do not know of a reference stating the law $\dot I = -2\kappa - D$ — the universal rate $-2$ per mode may be known in the Calogero/heat-flow-on-zeros community, we have not seen it written down.

### References

de Bruijn, N.G. (1950), *The roots of trigonometric integrals*, Duke Math. J. 17, 197–226. — Newman, C.M. (1976), *Fourier transforms with only real zeros*, Proc. Amer. Math. Soc. 61, 245–251. — Csordas, G., Smith, W., Varga, R.S. (1994), *Lehmer pairs of zeros, the de Bruijn–Newman constant Λ, and the Riemann hypothesis*, Constr. Approx. 10, 107–129. — Ki, H., Kim, Y.-O., Lee, J. (2009), *On the de Bruijn–Newman constant*, Adv. Math. 222, 281–306. — Rodgers, B., Tao, T. (2020), *The de Bruijn–Newman constant is non-negative*, Forum Math. Pi 8, e6. — Polymath, D.H.J. (2019), *Effective approximation of heat flow evolution of the Riemann ξ function, and a new upper bound for the de Bruijn–Newman constant*, Res. Math. Sci. 6, 31. — Kreĭn, M.G. (1950), on strong stability of linear periodic Hamiltonian systems (Dokl. Akad. Nauk SSSR 73). — Gel'fand, I.M., Lidskii, V.B. (1955), Uspekhi Mat. Nauk 10 (transl. AMS Transl. 8, 1958). — MacKay, R.S. (1986), *Stability of equilibria of Hamiltonian systems*, in Nonlinear Phenomena and Chaos. — Bognár, J. (1974), *Indefinite Inner Product Spaces*, Springer. — Azizov, T.Ya., Iokhvidov, I.S. (1989), *Linear Operators in Spaces with an Indefinite Metric*, Wiley. — Arnol'd, V.I. (1967), *Characteristic class entering in quantization conditions*, Funct. Anal. Appl. 1, 1–13. — Robbin, J., Salamon, D. (1993), *The Maslov index for paths*, Topology 32, 827–844. — Vakhitov, N.G., Kolokolov, A.A. (1973), Radiophys. Quantum Electron. 16, 783–789. — Grillakis, M., Shatah, J., Strauss, W. (1987), *Stability theory of solitary waves in the presence of symmetry I*, J. Funct. Anal. 74, 160–197. — Kapitula, T., Kevrekidis, P.G., Sandstede, B. (2004), *Counting eigenvalues via the Krein signature in infinite-dimensional Hamiltonian systems*, Physica D 195, 263–282. — Li, X.-J. (1997), *The positivity of a sequence of numbers and the Riemann hypothesis*, J. Number Theory 65, 325–333. — Bombieri, E., Lagarias, J.C. (1999), *Complements to Li's criterion for the Riemann hypothesis*, J. Number Theory 77, 274–287. — Łojasiewicz, S. (1963), *Une propriété topologique des sous-ensembles analytiques réels*, Colloques CNRS 117. — Simon, L. (1983), *Asymptotics for a class of non-linear evolution equations*, Ann. of Math. 118, 525–571.
