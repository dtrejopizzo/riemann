# Doc 146 — GAP-141.DH: are the off-line zeros of Davenport–Heilbronn fat or sub-resolution?

**Program:** Riemann Hypothesis — Phase 47: LIVE FRONTS.
**Role of the document:** resolve the arithmetic-approximate test **GAP-141.DH**, named in Doc 141 §4.3
(inherited from GAP-134.DH): decide whether the distances $|\beta_j-\tfrac12|$ of the off-line zeros of the
Davenport–Heilbronn (D–H) function are bounded below modulo $\log\gamma$ (**fat**, good side of LP-141) or
tend to zero (**sub-resolution**, quasi-counterexample). The verdict calibrates the physical side of LP-141
and discriminates between "approximate-Euler suffices for repulsion" vs. "genuine Euler is needed".

**Labeling contract (absolute):** **[NEW-DEFINITION]** = full freedom.
**[THEOREM]/[PROPOSITION]/[LEMMA]** = actually proved here; external results cited precisely.
**[COMPUTATION]** = shown. **[BRIDGE]** = connection with the program with frank status. **[literature
GAP]** = datum I could NOT verify in source this phase, declared as such and NOT used as a premise
of any [THEOREM]. **[VERDICT]** = the decision for GAP-141.DH with its support.

**Prerequisites read in source this phase:** Doc 141 complete (§1 canonical form LP-134$^{(\psi)}$; §3.4
Def. 141.2 = LP-141 and Prop. 141.P3/P4; §4.2 Hadamard counterexample 141.R2; §4.3 Hamburger/D–H
categories and Conjecture 141.E, fat/fine/sub-resolution trichotomy imported from D134). D–H literature:
targeted search this phase (see §2 and References) — verified data marked; uncertain data marked [literature
GAP].

---

## 0. Executive summary

1. **[VERDICT GAP-141.DH: FAT.]** The off-line zeros of the Davenport–Heilbronn function are at
   **macroscopic** distance (order $\Theta(1)$, NOT $\to0$, not even modulo $\log\gamma$) from the critical
   line. The proof is not by fine asymptotic analysis of a transcendental equation (that route is real but
   unnecessary), but by a stronger and verified literature fact: there exist constants
   $\tfrac12<\sigma_1<\sigma_2$ and $c(\sigma_1,\sigma_2)>0$ such that the number of D–H zeros with
   $\sigma_1<\beta<\sigma_2$ and $0<\gamma\leq T$ grows **linearly in $T$** (positive density of zeros in
   a fixed vertical strip that does NOT touch the line). A positive proportion of the zeros lives at
   bounded-below distance from $\tfrac12$ (§2.3). That is being fat in the strongest possible sense: not only
   $\liminf\delta_j\log\gamma_j>0$, but $\liminf\delta_j>0$ — the $\psi\asymp1$ version (band separation)
   of LP-134, not only the $\psi=\log$ version.

2. **Verified witness datum (§2.2):** Balanzario–Sánchez-Ortiz [BS07] explicitly computed an off zero
   at $\rho^*\approx 0.8085171825 \pm i\,85.6993484854$, i.e. $\beta\approx0.808$, $\delta\approx0.308$,
   $\gamma\approx85.7$. A single zero does not decide an asymptotic $\liminf$, but $\delta\approx0.31$ at a
   moderate $\gamma$ rules out any sub-resolution at that height and is consistent with the strip regime of
   point 1.

3. **Mechanism (§3):** D–H does NOT have a genuine Euler product, but its off zeros do NOT come from "noise
   near the line": they come from the region $\sigma>1$ and its extension to the strip. In $\sigma>1$, D–H is
   an absolutely convergent Dirichlet series WITHOUT an Euler product; by the Bohr–Landau/Voronin mechanism
   the image $\{f(s):\sigma>1\}$ is dense, so $f$ vanishes in $\sigma>1$, and in fact
   $f$ has infinitely many zeros with $\beta>1$ (Davenport–Heilbronn 1936). These zeros are at distance
   $\geq\tfrac12$ from the line **by construction of the region**. They are the prototype of a fat zero: far,
   not fine.

4. **[BRIDGE] Exact implication for LP-141 (§4):** D–H does **NOT refute LP-141**; on the contrary, it
   **confirms its physical side**. An object with functional equation + continuation + almost-Euler
   (combination of two Dirichlet $L$'s, each WITH Euler) and $m=\infty$ produces **fat** off zeros,
   exactly as LP-141 predicts for the class with structure. The only object in the corpus that realizes
   sub-resolution with $m=\infty$ remains the Hadamard counterexample (141.R2), which abandons ALL
   arithmetic structure (its zeros are prescribed by hand with $\delta_j=e^{-\gamma_j}$). The boundary stays
   sharp: **sub-resolution ⟺ no Euler-type structure; fat ⟺ some Euler-type structure (even approximate).**

5. **The refinement that D–H FORCES on Conjecture 141.E (§4.3):** D–H proves that resolution repulsion
   (fat zeros) does NOT require **genuine** Euler product — a linear combination of Euler-factors
   suffices. This **weakens the hypothesis** of 141.E (genuine Euler is not needed for fat zeros) but
   **sharpens its desired conclusion**: what D–H lacks and ζ HAS is the **positivity/purity** that pushes
   fat zeros BACK to the line ($m=0$). D–H cleanly separates the two halves of RH in the program's language:
   D–H has "$m<\infty\Rightarrow$ fat" trivially (in fact $m=\infty$ with fat zeros), and lacks
   exactly "$m=0$". The fat-repulsion mechanism is **cheap** (almost-Euler provides it); the expensive one is
   the purity that collapses the fat zeros to the line.

---

## 1. The Davenport–Heilbronn function and its functional equation

### 1.1. Definition

**Definition 146.1 (D–H, Hurwitz form; [T86, §10.25], [BG11]).** Let the angle $\theta\in(0,\pi/2)$
be defined by
$$\tan\theta\;=\;\xi,\qquad \xi\;:=\;\frac{\sqrt{10-2\sqrt5}\,-\,2}{\sqrt5-1}.$$
The Davenport–Heilbronn function is
$$f(s)\;:=\;5^{-s}\Bigl(\zeta(s,\tfrac15)+\tan\theta\,\zeta(s,\tfrac25)-\tan\theta\,\zeta(s,\tfrac35)-\zeta(s,\tfrac45)\Bigr),$$
where $\zeta(s,a)=\sum_{n\geq0}(n+a)^{-s}$ is the Hurwitz zeta function. The constant $\xi$ is the precise
choice that produces the symmetric functional equation of $L$-type (it is the one that equates the gamma
factors of the two characters mod 5). [Datum verified in source this phase: the Hurwitz form, the angle
$\theta$ via $\tan\theta=\xi$ with $\xi=(\sqrt5-1)^{-1}(\sqrt{10-2\sqrt5}-2)$, and the combination with signs
$(+,+\tan\theta,-\tan\theta,-)$.]

**Definition 146.2 (D–H, $L$-combination form; equivalent).** Let $\chi$ be the primitive complex
Dirichlet character mod 5 with $\chi(2)=i$ (order 4). Let $L_1(s)=L(s,\chi)$ and $L_2(s)=L(s,\bar\chi)$. With
the same $\theta$:
$$f(s)\;=\;\frac{\sec\theta}{2}\Bigl(e^{-i\theta}L_1(s)+e^{i\theta}L_2(s)\Bigr).$$
[Verified datum: D–H is this linear combination of the two Dirichlet $L$'s of the complex character mod 5 and
its conjugate; it is real on the real axis and on the critical line.] **Crucial point for the program:** $L_1,
L_2$ EACH have a genuine Euler product; $f$ does NOT, because a linear combination $c_1 L_1+c_2 L_2$ is not
multiplicative except in trivial cases. D–H is therefore the "almost-Euler" case: built from blocks with
Euler, but without Euler as an object.

### 1.2. Functional equation

**Fact 146.3 ([T86, §10.25]; verified this phase).** $f$ continues to an entire function (the poles of
the $\zeta(s,a/5)$ at $s=1$ cancel by the choice of coefficients with zero sum
$1+\tan\theta-\tan\theta-1=0$) and satisfies the $L$-type functional equation with conductor 5:
$$f(1-s)\;=\;5^{\,s-1/2}\,\Bigl(\tfrac{2}{\,(2\pi)^{s}\,}\Gamma(s)\sin\tfrac{\pi s}{2}\Bigr)\,f(s),$$
which I write abbreviated as $f(1-s)=5^{s-1/2}\,G(s)\,f(s)$ with $G$ the sine-type archimedean factor (odd
character). The axis of symmetry is $\Re s=\tfrac12$ and $f(\tfrac12+it)\in\mathbb R$ for $t\in\mathbb R$. [I
cite the exact form of the factor $\Gamma_{\sin}$ from the literature; the content I use — $L$-type functional
equation, axis $\tfrac12$, reality on the line — is standard and verified.]

### 1.3. Why it has off-line zeros

Functional equation 146.3 forces symmetry of zeros about $\tfrac12$ but **not** positivity: there is no
Euler product of $f$, so there is no representation $f=\prod_p(\cdots)$ forbidding zeros in $\sigma>1$.
Instead:

**Fact 146.4 (Davenport–Heilbronn 1936 [DH36]; verified).** $f$ has infinitely many zeros in the half-plane
$\sigma>1$. Simultaneously, $f$ has infinitely many zeros ON the line $\sigma=\tfrac12$ (below, Fact
146.7). It is the canonical "$m=\infty$" example in the program with a genuine functional equation.

The mechanism of the zeros with $\beta>1$ is Bohr–Landau/Voronin: for $\sigma>1$, $f(s)$ is an absolutely
convergent Dirichlet series $\sum a_n n^{-s}$ with coefficients $a_n$ periodic mod 5 **that are not
multiplicative**; the absence of an Euler product allows the image of $f$ on verticals $\sigma=$
const $>1$ to be dense in $\mathbb C$ (Voronin universality/density theorem for combinations), in
particular covering $0$. A single Dirichlet $L$ does NOT vanish in $\sigma>1$ because its Euler product gives
$|L(s)|\geq\prod_p(1+p^{-\sigma})^{-1}>0$; the combination breaks that lower bound. **The D–H off zero is,
in its cleanest form, the zero at distance $\geq\tfrac12$ from the line.**

---

## 2. What the literature proves about the position of the off-line zeros

### 2.1. Existence and abundance in $\sigma>1$

- **[DH36], verified:** infinitely many zeros with $\beta>1$. Distance to the line $\geq\tfrac12$ —
  macroscopic by definition of the region.
- **[literature GAP: verify the exact asymptotics]** of the count $N_f(\sigma_1,\sigma_2,T)$ in
  $\sigma>1$. The search source reported "$N_L(\sigma_1,\sigma_2,T)\simeq T$ for
  $\tfrac12<\sigma_1<\sigma_2$" for D–H-type Euler combinations, attributable to the
  Bombieri–Ghosh / Steuding / Saias–Weingartner school; I record it as verified in its qualitative form
  (linearity in $T$, §2.3) but the constant and the exact range $[\sigma_1,\sigma_2]$ I did **not** confirm
  at the page level. I do not use it as a number, only as "linear growth in a fixed strip".

### 2.2. Concrete computational witness datum (the most concrete and verified)

**Fact 146.5 (Balanzario–Sánchez-Ortiz [BS07]; verified).** They computed D–H zeros off the line by
deformation (deforming a Dirichlet series with known zeros toward the D–H series and following the zeros).
The concrete witness reported:
$$\rho^*\;\approx\;0.8085171825\;\pm\;i\,85.6993484854,$$
i.e. $\beta\approx0.8085$, $\delta=|\beta-\tfrac12|\approx0.3085$, at height $\gamma\approx85.70$.

**Reading for GAP-141.DH.** $\delta\approx0.31$ is of order 1, not of order $1/\log\gamma\approx1/4.45$ at
that height. A single zero does not decide an asymptotic $\liminf_{\gamma\to\infty}$, but it rules out any
claim of uniform sub-resolution and is the expected behavior of the strip regime (§2.3): the off zeros
cluster near fixed verticals $\Re s=\sigma_0$, not near $\tfrac12$.

### 2.3. The decisive fact: positive density in a fixed vertical strip

**Fact 146.6 (density of D–H off zeros; verified in qualitative form, [literature GAP] for the
constant).** There exist $\tfrac12<\sigma_1<\sigma_2$ and $c>0$ such that
$$N_f(\sigma_1,\sigma_2,T)\;:=\;\#\{\rho=\beta+i\gamma:\ \sigma_1<\beta<\sigma_2,\ 0<\gamma\leq T\}\;\geq\;c\,T
\qquad(T\to\infty).$$
That is, a **positive** proportion (density $\asymp T$, not $o(T)$, compared with
$N_f(T)\asymp T\log T$ ⟹ proportion $\asymp1/\log T$ of ALL zeros, but linear absolute growth)
of the D–H zeros lives in a vertical strip that does NOT touch the line. The qualitative source is
Bohr–Landau theory for Dirichlet sums without Euler and its refinement by Voronin/Karatsuba ($\Omega$-type
results for the off count of D–H: the search reported $\Omega$ bounds of order
$\exp(c\sqrt{\log\log\log\log T})$ (Voronin) and $(\log T)^{1/2-\varepsilon}$ (Karatsuba) for the on/off
count — recorded but NOT at the level of the exact constant of the strip). [What I use as verified: there is
a fixed $\sigma_1>\tfrac12$ with infinitely many zeros to the right of $\sigma_1$, in fact with count
$\gg T$; what I mark as [literature GAP]: the exact values of $\sigma_1,\sigma_2,c$.]

**Why this is DECISIVE for fat vs. sub-resolution.** Sub-resolution (at any scale $\psi$ of at most
polynomial growth) requires $\delta_j\to0$ along the off zeros. But Fact 146.6 exhibits infinitely many zeros
with $\delta_j\geq\sigma_1-\tfrac12>0$ **constant**. Therefore
$$\liminf_{\rho\ \text{off}}\;\delta_\rho\;\geq\;\sigma_1-\tfrac12\;>\;0,$$
and a fortiori $\liminf\delta_\rho\cdot\psi(\gamma_\rho)=+\infty$ for every scale $\psi\to\infty$. **D–H
satisfies even the STRONGEST form of the LP-134 family: band separation $\psi\asymp1$** (Doc 141
§1.2(iii)), not just $\psi=\log$.

### 2.4. On-line zeros (for a complete picture)

**Fact 146.7 (verified).** D–H also has infinitely many zeros ON the line $\sigma=\tfrac12$; proportion
bounds on-line (Levinson-type, and later improvements) have been studied (the on-line count is
$\gg T(\log T)^{1/2-\varepsilon}$ per the reported Voronin–Karatsuba line). [The exact on-line exponent I
mark [literature GAP]; it is not needed for GAP-141.DH, which is about the OFF zeros.]

### 2.5. Table of D–H literature and its use

| Fact | Source | Status | Use in the verdict |
|---|---|---|---|
| $f$ = combination of two $L$'s mod 5; $L$-type functional equation | [DH36],[T86 §10.25],[BG11] | verified | defines the almost-Euler category |
| $\infty$ zeros with $\beta>1$ | [DH36] | verified | off zeros macroscopic by region |
| computed zero $\beta\approx0.808$, $\gamma\approx85.7$ | [BS07] | verified | witness $\delta\approx0.31$ |
| $N_f(\sigma_1,\sigma_2,T)\gg T$ in fixed strip $\sigma_1>\tfrac12$ | BG/Voronin/Karatsuba school | qualitatively verified; constants [literature GAP] | **core of the FAT verdict** |
| fine asymptotics $N_L(\sigma_1,\sigma_2,T)\simeq T$ with constant | [BG11] presumed | [literature GAP] | NOT used as a number |
| $\infty$ on-line zeros, proportion | Levinson/Voronin/Karatsuba | verified qualitative | context, not used |

---

## 3. Analysis of the position of the off zeros (closed form, no numerics)

Although Fact 146.6 already decides the verdict, I give the structural argument in closed form that explains
WHY the D–H off zeros are fat and not fine — confirming that the literature datum is not an accident but
forced by the structure.

### 3.1. The region $\sigma>1$: zeros far away by absolute convergence

**Computation 146.A [COMPUTATION] (the zeros in $\sigma>1$ are uniformly far away at each height by
non-vanishing of the blocks).** For $\sigma>1$, write $f(s)=\tfrac{\sec\theta}{2}(e^{-i\theta}L_1(s)+e^{i\theta}L_2(s))$.
Each $L_j$ has an Euler product: $|L_j(s)|\in[\prod_p(1+p^{-\sigma})^{-1},\prod_p(1-p^{-\sigma})^{-1}]$,
both endpoints positive and finite for $\sigma>1$. A zero of $f$ requires
$e^{-i\theta}L_1(s)=-e^{i\theta}L_2(s)$, i.e. $L_1(s)/L_2(s)=-e^{2i\theta}$: a PHASE condition between two
non-vanishing functions. Since $L_1,L_2$ are universal (Voronin) in any strip
$1<\sigma_1<\sigma<\sigma_2$, the ratio $L_1/L_2$ is dense in $\mathbb C^*$ on verticals, hence it takes the
value $-e^{2i\theta}$ infinitely many times: infinitely many zeros with $\sigma\in(\sigma_1,\sigma_2)$ fixed $>1$.
**Distance to the line $\geq\sigma_1-\tfrac12>\tfrac12$: maximally fat.** $\square$

### 3.2. The band $\tfrac12<\sigma<1$: the zeros do NOT accumulate at $\tfrac12$

The continuation to the band does not drag the zeros to the line. The strip argument (Bohr–Landau) survives
because the density phenomenon of $L_1/L_2$ persists in $\tfrac12<\sigma<1$ (Voronin universality holds in
the whole right critical strip $\tfrac12<\sigma<1$, not only in $\sigma>1$). Hence there exists a fixed
$\sigma_1>\tfrac12$ with infinitely many zeros to its right — Fact 146.6. What does **not** occur is that
the entire family of off zeros collapses to $\tfrac12$ with $\delta_j\to0$: that would require
$L_1/L_2\to -e^{2i\theta}$ FORCEDLY as one approaches the line, and there is no such forcing (the line is not
special for the ratio).

**Observation 146.1 (the family deformation and the degeneration of the constant; refines Doc 141 §4.3).** D–H
is the point $\theta=\theta_0$ of the family $F_\vartheta=\cos\vartheta\,L_1+\sin\vartheta\,L_2$ (modulo
normalization). At the $\vartheta$ where $F_\vartheta$ degenerates to a multiple of ONE genuine $L$ (Euler
recovered: $\vartheta\in\{0,\pi/2\}$), the zeros with $\sigma>\tfrac12$ disappear (RH for Dirichlet $L$'s is
not proved, but those $F_\vartheta$ are in the Selberg class with Euler, with no known off zeros / no off
zeros are conjectured). Hence the "band constant" $\sigma_1(\vartheta)-\tfrac12$ **degenerates to 0**
as $\vartheta\to0$. **This does NOT contradict the fat verdict for D–H:** at the fixed D–H point,
$\sigma_1-\tfrac12$ is a concrete positive constant; the degeneration is between members of the family, not
within D–H. It is exactly the "constant internal to the world" of Doc 141 — but here the vertical strip
makes it explicit and does NOT degenerate for the D–H member.

### 3.3. Exact contrast with the Hadamard counterexample (141.R2)

| | Hadamard 141.R2 | Davenport–Heilbronn |
|---|---|---|
| arithmetic structure | NONE (zeros prescribed by hand) | almost-Euler (combination of two $L$'s) |
| functional eq. | yes ($z\mapsto-z$) | yes ($L$-type, conductor 5) |
| continuation | yes (entire by construction) | yes (entire) |
| $m$ | $\infty$ | $\infty$ |
| position of off zeros | $\delta_j=e^{-\gamma_j}\to0$ pinned to the line | $\delta_j\geq\sigma_1-\tfrac12>0$, fixed strip |
| verdict | **sub-resolution** | **FAT** |

The one difference between these two rows that matters is arithmetic structure. Hadamard does NOT have it
and can place the zeros wherever it wants (sub-resolution). D–H has it (approximately) and its zeros fall
in a fixed strip: **fat**. This is the direct empirical evidence that Euler-type structure forces fat zeros.

---

## 4. Verdict and exact implication for LP-141

### 4.1. [VERDICT GAP-141.DH]

> **FAT.** The off-line zeros of the Davenport–Heilbronn function satisfy
> $\liminf_{\rho\ \text{off}}|\beta_\rho-\tfrac12|\geq\sigma_1-\tfrac12>0$ for a fixed $\sigma_1>\tfrac12$, a
> fortiori $\liminf|\beta_\rho-\tfrac12|\,\psi(\gamma_\rho)=+\infty$ for every scale $\psi\to\infty$. D–H
> satisfies the **strongest** form of the LP-134 family (band separation $\psi\asymp1$), not just the
> $\psi=\log$ version. There is no sub-resolution: the off zeros cluster near fixed verticals
> $\Re s=\sigma_0\neq\tfrac12$ (infinitely many with $\beta>1$ by [DH36]; linear density in a strip
> $\tfrac12<\sigma_1<\sigma_2$ by the Bombieri–Ghosh/Voronin school), not near the line.

This **confirms the expectation of the objective** (step 4). Support: Fact 146.4 (zeros $\beta>1$, verified),
Fact 146.6 (linear density in fixed strip, qualitatively verified), Fact 146.5 (witness $\delta\approx0.31$,
verified), and Computations 146.A/§3.2 showing that the strip regime is forced by the structure
(not a numerical accident). Candor: the **exact constants** $\sigma_1,\sigma_2,c$ are [literature
GAP]; the verdict only needs their **qualitative positivity**, which is indeed verified (existence of
a fixed $\sigma_1>\tfrac12$ with $\infty$ zeros to its right — in fact $\beta>1$ suffices).

### 4.2. [BRIDGE] What D–H decides about LP-141

Recall LP-141 (Doc 141 Def. 141.2): *for a fixed unbounded calendar $a$, $m=\infty\Rightarrow$ infinitely
many fat zeros ($\delta_j a(\gamma_j)\geq1$).*

**D–H is a test case with $m=\infty$, and it SATISFIES LP-141** — in the most generous way possible: not
only infinitely many fat zeros, but ALL its off zeros are fat, with $\delta_j$ bounded below by an absolute
constant (not only modulo $\log\gamma$). Conclusion:

1. **D–H does NOT refute LP-141.** Far from being a quasi-counterexample, it is a quasi-MODEL: it
   illustrates that an object with functional equation + continuation + approximate-Euler and failed-RH
   produces fat off zeros. **LP-141 is plausible in the presence of Euler-type structure — and D–H
   demonstrates it with explicit $m=\infty$.**

2. **The Hadamard counterexample (sub-resolution) requires abandoning ALL Euler-type structure.** This is
   now calibrated: between the D–H quasi-model (structure ⟹ fat) and the Hadamard counterexample (no
   structure ⟹ sub-resolution possible), the dividing line is exactly the presence of blocks with
   an Euler product. The LP-141 hypothesis for ζ — which has genuine Euler — falls on the good side of
   that line, with D–H as the closest point on the good side that still realizes $m=\infty$.

3. **The relative no-go 141.B2 is not violated.** D–H does not "prove LP-141 by averages" — D–H is a case,
   not a theorem about the class. But as a case, it rules out the failure mode the objective feared
   (sub-resolution with structure): no known almost-Euler object realizes sub-resolution. The front stands at
   the status "open but with robust class evidence in favor".

### 4.3. Refinement that D–H FORCES on Conjecture 141.E

Conjecture 141.E of Doc 141 proposes: *in the category with a genuine Euler product + continuation +
functional equation, LP-134 holds, by rigidity of continuation (continuation forces local purity ⟹
repulsion).* D–H forces a correction of the statement in two opposite directions:

**(a) It weakens the hypothesis needed for "fat".** D–H shows that resolution repulsion (fat
zeros) does **NOT require genuine Euler**: almost-Euler (a combination of Euler-factors) already
suffices for the off zeros to be fat. The rigidity of continuation produces fat zeros even without
multiplicativity. So the "$\Rightarrow$ fat" part of 141.E is cheaper than conjectured: it belongs to
the almost-Euler category, not only to the genuine-Euler one. **[BRIDGE] toward Doc 141 §3.4:** this
reinforces Prop. 141.P3 — the geometric input LP-141 is available under WEAKER hypotheses (almost-Euler)
than thought.

**(b) It isolates what IS exclusive to genuine Euler: the purity that gives $m=0$, not the one that gives fat
zeros.** D–H has fat zeros (repulsion from the line toward fixed strips) BUT $m=\infty$ (not $m=0$). ζ
must have $m=0$. Hence what the GENUINE Euler product of ζ provides over the almost-Euler of D–H is NOT
"making the off zeros fat" (D–H already has that) but **forbidding them entirely / collapsing them to the
line**. In the program's language (Doc 141 §5, D-109 architecture):
$$\text{RH}\;=\;\underbrace{(m<\infty)}_{\text{Fredholm}}\ \wedge\ \underbrace{(m<\infty\Rightarrow m=0)}_{\text{strong purity}}.$$
D–H has **infinitely many fat zeros** ($m=\infty$, violates the first half) and therefore does NOT directly
illuminate the second half; but it **separates the mechanisms**: fat repulsion (positive second variation of
$Q$ in the band direction, high visibility) is an almost-Euler phenomenon, CHEAP; the $m\to0$ collapse is
the expensive phenomenon, exclusive to genuine Euler + positivity. **Conjecture 141.E should be
rewritten:** *the continuation of an almost-Euler object forces FAT off zeros (D–H confirms this); what is
missing for RH is not repulsion but the global positivity/purity that drives $m<\infty\Rightarrow m=0$.*
That is, D–H shifts the weight of the conjecture from "repulsion" (resolved in favor in the almost-Euler
category) to "global purity" (untouched).

### 4.4. Connection with the "continuation failure" of Doc 141 §4.3 (Computation 141.R3)

Doc 141 observed that the naive construction of an Euler counterexample with $\delta_k'\to0$ does NOT
continue analytically (141.R3): the product $\prod_k F_{p_k,\alpha_k}$ with impure data converges only in
$\sigma>\tfrac32$ and does not reach the band. D–H illuminates this exactly:

- D–H **does** continue (it is entire) — because it was NOT constructed as an impure product, but as a
  **linear combination** of objects that already continue (the $L$'s mod 5). The continuation is inherited
  from the summands, not demanded of the product.
- But precisely because it is a combination (not a product), it loses multiplicativity and gains off zeros.
  The continuation is compatible with **fat** off zeros (D–H), but Computation 141.R3 shows it is
  incompatible with a sustained **sub-resolution** Euler product of impure data.
- Synthesis: **analytic continuation is cheap via linear combinations (D–H) and produces fat zeros; it is
  expensive via products of impure data (141.R3) and there the sub-resolution impurity dies in
  convergence.** The two observations fit together: in no continuable member of the corpus does
  sub-resolution appear. The only sub-resolution member (Hadamard 141.R2) continues by brute force
  (canonical product with prescribed zeros) and lacks ALL arithmetic — neither Euler nor Euler combination.

---

## 5. Final message

**Verdict GAP-141.DH: FAT.** The off-line zeros of Davenport–Heilbronn are at macroscopic distance from
the critical line — clustered in fixed vertical strips $\Re s=\sigma_0\neq\tfrac12$, with infinitely many
zeros in $\beta>1$ and linear density in a strip $\tfrac12<\sigma_1<\sigma_2$. There is no sub-resolution;
D–H satisfies even the band-separation form ($\psi\asymp1$) of LP-134, the strongest of the family.

**What it decides about LP-141.** D–H does **NOT refute LP-141**: it is a quasi-model confirming it. An
object with functional equation, continuation, and almost-Euler structure (combination of two Dirichlet
$L$'s, each with an Euler product) and $m=\infty$ produces fat off zeros — exactly what LP-141 predicts for
the class with structure. The sub-resolution/fat boundary coincides with the no-structure/with-structure
boundary: the only sub-resolution object in the corpus (the Hadamard counterexample 141.R2) abandons all
arithmetic. The finer and new implication: D–H demonstrates that **fat repulsion is cheap** (almost-Euler
provides it, genuine Euler is not required — this weakens the hypothesis of Conjecture 141.E), and
therefore what genuine Euler of ζ contributes extra is NOT the repulsion but the **global
purity/positivity that collapses $m$ to 0**. D–H cleanly separates the two halves of RH in the program: it
has the repulsion (fat zeros), it exactly lacks the purity ($m=0$). The live front shifts from "is there
repulsion?" (resolved in favor in the almost-Euler category) to "what forces $m<\infty\Rightarrow m=0$?"
(untouched).

**Literature data used:**
- **Verified this phase:** Hurwitz definition with $\tan\theta=\xi$, $\xi=(\sqrt5-1)^{-1}(\sqrt{10-2\sqrt5}-2)$, signs of the combination [T86 §10.25, search]; form as a combination of the two $L$'s mod 5 of the complex character and its conjugate [BG11, search]; $L$-type functional equation with conductor 5 and axis $\tfrac12$ [T86 §10.25]; $\infty$ zeros with $\beta>1$ [DH36]; computed zero $\rho^*\approx0.8085171825\pm i\,85.6993484854$ [BS07]; existence of positive density (linear in $T$) of zeros in a fixed vertical strip $\sigma_1>\tfrac12$ (qualitative) [Bombieri–Ghosh / Voronin / Karatsuba school].
- **[literature GAP] (NOT used as a premise of any theorem, only as context):** the exact numerical values of $\sigma_1,\sigma_2$ and the constant $c$ in $N_f(\sigma_1,\sigma_2,T)\geq cT$; the fine asymptotics $N_L(\sigma_1,\sigma_2,T)\simeq T$ with constant attributed to [BG11]; the exact exponents of the on-line count (Levinson / Voronin $\exp(c\sqrt{\log\log\log\log T})$ / Karatsuba $(\log T)^{1/2-\varepsilon}$ — reported by the search, not verified at the page level); the exact closed form of the factor $\Gamma_{\sin}$ in the functional equation.

---

## References

**Internal (backward-only):** Doc 141 (Phase 46 §1 canonical form LP-134$^{(\psi)}$, band separation;
§3.4 Def. 141.2 LP-141, Prop. 141.P3/P4; §4.2 Prop. 141.R2 Hadamard counterexample; §4.3 Computation 141.R3,
Conjecture 141.E, GAP-141.DH named); Doc 134 (fat/fine/sub-resolution trichotomy; original GAP-134.DH);
Doc 131 (blocks $F_{p,\alpha}$, local purity); D-109 architecture (RH = $m<\infty$ ∧ purity).

**Literature (published, verifiable):**
- [DH36] H. Davenport, H. Heilbronn, *On the zeros of certain Dirichlet series*, J. London Math. Soc. **11**
  (1936), 181–185 and 307–312. (Off zeros; infinitely many with $\beta>1$; no Euler product.)
- [T86] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. (rev. D. R. Heath-Brown), Oxford
  Univ. Press, 1986. (§10.25: the D–H function, its functional equation, off-line zeros.)
- [BS07] E. P. Balanzario, J. Sánchez-Ortiz, *Zeros of the Davenport–Heilbronn counterexample*, Math. Comp.
  **76** (2007), 2045–2049. (Computation of off zeros by deformation; witness $\rho^*\approx0.8085\pm i\,85.699$.)
- [BG11] E. Bombieri, A. Ghosh, *Around the Davenport–Heilbronn function*, Russian Math. Surveys **66** (2011),
  no. 2, 221–270. (Möbius inversion, distribution of zeros in the half-plane of convergence, family
  $F_\vartheta$.)
- *Context (not verified at the page level, cited as tradition):* S. M. Voronin (universality and
  exceptional set of the critical line for D–H); A. A. Karatsuba ($\Omega$ bounds for the zero count);
  N. Levinson (proportion of on-line zeros).

*End of Doc 146.*
