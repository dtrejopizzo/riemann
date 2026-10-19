# Doc 165 — Destructor of the quantum import (Stone + wave equation → RH via structural unitarity?)

**Phase 53.**

## Claim under attack

> There exists a unitary evolution $U(t)=e^{itH}$ on a natural space, with $\mathrm{spec}(H)=\{\gamma_\rho\}$ (the ordinates of the zeros of $\zeta$), where unitarity — via **Stone's theorem** ($U(t)$ strongly continuous unitary $\Rightarrow$ $H$ self-adjoint $\Rightarrow$ $\mathrm{spec}(H)\subset\mathbb{R}$ $\Rightarrow$ RH) — comes from a **structural RH-free symmetry** (the functional equation $s\leftrightarrow 1-s$, an involution), **not** from the Weil metric $\langle f,g\rangle_W=\sum_\rho \hat f(\gamma_\rho)\overline{\hat g(\gamma_\rho)}$ that already enumerates the zeros.

The concrete hope: that "unitary" be a **free** property (inherited from the functional symmetry), so that the reality of the spectrum falls out without paying the positivity price that is RH.

Verdict summary, stated in advance: **all three routes kill the claim**, and all three do so by reducing to **ALREADY KNOWN** obstructions of the program (indefinite-Krein = the Phase 51 metric; deficiency = boundary conditions; absorption = trace positivity). The quantum import **does NOT touch $\zeta$ at a new node**: it re-expresses in Stone/von Neumann language the same "$\zeta$ IS the duality" node from Phase 52. Details below.

---

## Route 1 — Unitarity = the Weil metric in disguise (Stone does NOT give a real spectrum in a Kreĭn space)

### The killing argument (closed form)

**Structural premise.** "$U(t)$ unitary" is not an absolute statement: it is unitary **with respect to an inner product**. The operative question is: which sesquilinear form $\langle\cdot,\cdot\rangle$ leaves invariant the candidate evolution that has $\{\gamma_\rho\}$ as spectrum?

The available, RH-free structural symmetry is the functional equation, embodied as the involution $J:\;s\mapsto 1-s$ (equivalently, in the spectral variable, $\xi(s)=\xi(1-s)$ with $s=\tfrac12+i\gamma$). This involution is **RH-free**: it holds unconditionally. But what it produces on the test space **is not a positive-definite inner product**. It produces exactly the **Weil form** $Q$, the quadratic form of the explicit formula:
$$
Q(\hat h,\hat h)=\sum_\rho \hat h(\gamma_\rho)\,\overline{\hat h(\gamma_\rho)}\quad\text{(schematically, with the archimedean term + primes)}.
$$
The program has ALREADY shown (Phase 26, Phase 38 D63, Phase 51 D161) that this $Q$ has **negative index $\kappa=2m$**, where $m$ = the number of zeros off the critical line (counted with the Klein symmetry $V$, orbits $\rho,1-\rho,\bar\rho,1-\bar\rho$). That is:
- $Q$ positive definite $\iff \kappa=0 \iff m=0 \iff$ RH.
- Under non-RH, $Q$ is **indefinite**, with $\kappa=2m>0$ negative directions: a **Pontryagin form** $\Pi_\kappa$ (Kreĭn space of finite index).

**The blow.** In this scenario, "$U(t)$ unitary with respect to $Q$" means **$J$-unitary** (unitary in the Kreĭn sense), and the generator $H_C$ (Connes) is **$Q$-self-adjoint** (= $J$-self-adjoint), NOT self-adjoint in the Hilbert sense. And here is the operator-theory fact that destroys the hope:

> **Stone's theorem does NOT guarantee a real spectrum for $J$-self-adjoint generators in Kreĭn spaces with $\kappa>0$.** $J$-self-adjoint operators (= self-adjoint with respect to an indefinite form) generically admit **complex spectrum**, organized in pairs conjugate with respect to the $J$ product (i.e. $\lambda$ eigenvalue $\Rightarrow \bar\lambda$ eigenvalue, spectral symmetry, NOT reality).

More finely (Bognár, *Indefinite Inner Product Spaces*, Springer 1974, Ch. VI; Azizov–Iokhvidov, *Linear Operators in Spaces with an Indefinite Metric*, Wiley 1989, §II.6 and Ch. V): a $J$-self-adjoint operator in $\Pi_\kappa$ has at most $\kappa$ **non-real** eigenvalues (counting multiplicities in the sense of the maximal negative subspace), and precisely these are the ones that can fall off $\mathbb{R}$. **The number of potentially complex eigenvalues is bounded by $\kappa=2m$** — which is precisely the bridging conjecture of Phase 26 (Theorem 26-C.2): the $2m$ complex eigenvalues $\{\pm b_j+i\gamma_j\}$ correspond to the off-line zeros.

**This is mathematically fatal for the hope, and it is fatal for the cleanest possible reason:** the version of Stone that gives a real spectrum requires a **genuine Hilbert space**, i.e. a **positive-definite** form. The only form for which the evolution is "unitary" is $Q$ (Weil form), and $Q$ is positive definite **if and only if RH**. Therefore:

$$
\boxed{\;\text{"unitary}\Rightarrow\text{real spectrum"} \;\equiv\; \text{"}Q\text{ positive definite"} \;\equiv\; \kappa=0 \;\equiv\; \text{RH}.\;}
$$

The quantum import buys nothing: **assuming the Hilbert hypothesis (positive-definite form) is already assuming RH.** Stone's theorem is a disguised biconditional, not a lever.

### Why the Kreĭn version of Stone does not save the situation

There is a theory of one-parameter groups in Kreĭn spaces (a Stone-type theorem for $J$-unitary $C_0$-groups; see Azizov–Iokhvidov §V.3, and the Langer–Najman theory of definite functions of operators in Pontryagin spaces). BUT its conclusion is exactly the opposite of the one desired: the generator is $J$-self-adjoint and, **when $\kappa>0$, its non-real part is generic and is supported precisely on the negative subspace of dimension $\kappa$.** The $J$-unitary group $e^{itH}$ with $H$ having complex eigenvalues **is not bounded in Hilbert norm** (it grows like $e^{|\mathrm{Im}\,\lambda|\,t}$), which is consistent: no Hilbert norm is preserved because the preserved form is indefinite. Stone-on-Hilbert does not apply because its hypothesis (norm unitarity) **fails**, and Stone-on-Kreĭn does apply but **does not conclude reality**.

### Verdict Route 1: **KILLS.**
And it kills at the **KNOWN node of the metric/orientation** (Phase 51 D161, Phase 52 D163 Route 1). The "RH-free structural symmetry" (functional equation) genuinely delivers a structure — but a **Kreĭn/Pontryagin** structure, not a Hilbert one. Turning it into Hilbert (= choosing a positive-definite product with respect to which $U$ is unitary) is exactly the Weil metric that carries $\zeta$, and its definiteness is RH. **This is the κ=2m of Phase 26 reformulated as a Stone obstruction.**

---

## Route 2 — The generator is not essentially self-adjoint (the Berry–Keating wall: deficiency indices = boundary conditions = ζ)

### The killing argument (closed form, with index quantification)

The natural candidate generator in this circle of ideas is the Berry–Keating dilator/Hamiltonian $H_{BK}=\tfrac12(xp+px)=-i\left(x\partial_x+\tfrac12\right)$ on the half-line $x>0$ (or Connes's scale operator $H_C$, the adelic version of the same dilation generator). The classical-semiclassical spectrum $\sim\frac{1}{2\pi}E\log E$ reproduces the Riemann–von Mangoldt count $N(T)\sim\frac{T}{2\pi}\log\frac{T}{2\pi}$. Berry–Keating (*SIAM Review* 41 (1999) 236–266; and Berry–Keating, "$H=xp$ and the Riemann zeros", in *Supersymmetry and Trace Formulae*, 1999) explicitly point this out and name the obstacle: **the operator is not defined without boundary conditions, and exact quantization of the $\gamma$ requires a condition that encodes $\zeta$.**

**Quantification of the deficiency indices.** Conjugating by the Mellin transform, $H_{BK}=-i(x\partial_x+\tfrac12)$ is unitarily equivalent to the momentum operator $-i\partial_u$ on $u=\log x\in\mathbb{R}$ (over the whole line) — which is essentially self-adjoint, indices $(0,0)$, spectrum $=\mathbb{R}$ entirely (continuous). **That case gives a continuous spectrum, NOT $\{\gamma\}$.** To get a discrete spectrum one must **restrict the domain** (half-line $x>0$, or introduce a cutoff/regularization of type $|x|\geq\ell$, or the Berry–Keating–Connes "box"). As soon as one restricts to a half-line $u\in(0,\infty)$ or to an interval, the momentum operator $-i\partial_u$ acquires **nonzero deficiency indices**:

- Half-line $u\in(0,\infty)$, $-i\partial_u$: indices $(n_+,n_-)=(1,0)$ — **there is no self-adjoint extension** (unequal indices). The operator is maximal symmetric but not self-adjoint; it generates a semigroup of isometries, not a unitary group. This is the classical von Neumann/Reed–Simon example (Reed–Simon, *Methods of Modern Mathematical Physics II*, 1975, example in §X.1, "momentum on the half-line"). **Stone does not apply: there is no unitary $U(t)$ at all.**
- Interval $u\in(a,b)$, $-i\partial_u$: indices $(1,1)$ — there is a $U(1)$ **family of self-adjoint extensions** parametrized by $\theta\in[0,2\pi)$ (quasi-periodic boundary condition $\psi(b)=e^{i\theta}\psi(a)$). Each $\theta$ gives a distinct self-adjoint operator with **equally spaced** spectrum $\{(2\pi n+\theta)/(b-a)\}$ — never $\{\gamma\}$.

**The blow.** The structural symmetry (dilation + functional equation) fixes the generator **only up to the choice of self-adjoint extension**, i.e. up to the boundary condition. And:

1. If the natural domain gives **unequal** indices ($(1,0)$, half-line case), **no self-adjoint extension exists**: the sought unitary evolution **does not exist**, Stone is inapplicable from the outset.
2. If a domain with **equal** indices is forced ($(1,1)$ or $(n,n)$), a family of extensions exists, but the boundary condition that produces the spectrum $\{\gamma\}$ **is not the functional equation alone** — it is a gluing/scattering condition whose spectral datum is the **phase of $\zeta(\tfrac12+i\gamma)$** (the factor $\chi(s)$ of the functional equation evaluated, which is where $\zeta$ enters). Berry–Keating–Connes quantization makes this explicit: the boundary condition is of type $\frac{\zeta(\tfrac12-iE)}{\zeta(\tfrac12+iE)}$, i.e. **fixing the extension that gives $\{\gamma\}$"$\equiv$"knowing $\zeta$ on the critical line = knowing the zeros.**

$$
\boxed{\;\text{"choosing the self-adjoint extension giving }\{\gamma\}\text{"}\;\equiv\;\text{"boundary condition}=\text{phase of }\zeta\text{"}\;\equiv\;\text{knowing the zeros.}\;}
$$

Self-adjointness is not structural: it is a **von Neumann choice** among a continuum of operators, and the only member of the family with spectrum $\{\gamma\}$ is the one with $\zeta$ encoded at its boundary. The functional symmetry restricts but **does not determine** the boundary condition.

### Honest nuance — [GAP]

There is a subtlety worth declaring: the functional equation **does** impose a boundary condition (the involution $s\leftrightarrow 1-s$ translates into a pairing of the two endpoints / the two asymptotics via the factor $\chi$). In that sense, the structural symmetry **does not leave** the condition entirely free. BUT the factor $\chi(s)=2^s\pi^{s-1}\sin(\pi s/2)\Gamma(1-s)$ is the **archimedean/gamma** part of the functional equation; the information missing to reach $\{\gamma\}$ is the **finite** part (the Euler product / the primes). [literature GAP, honest]: I do not know a published proof that the complete functional equation (including the Euler side) uniquely determines the extension, **nor** one showing that an RH-dependent degree of freedom remains. What is solid: the half-line case gives indices $(1,0)$ (total non-self-adjointness), and the interval case gives a family where the correct member encodes $\zeta$. The hope of "free self-adjointness" dies by either of these two.

### Verdict Route 2: **KILLS** (with a minor [GAP] on the uniqueness of the archimedean condition).
A **KNOWN** node: boundary conditions. It is the classical Berry–Keating wall, not a new obstruction. The program had already found it as "the choice of self-adjoint extension of $H_C$ = RH" (implicit in Phase 26, $H_C$ $Q$-symmetric but its genuine self-adjointness $\equiv$ RH).

---

## Route 3 — Connes's spectrum is ABSORPTION, not EMISSION (trace positivity = RH)

### The killing argument (closed form)

Connes (*Selecta Math.* 5 (1999) 29–106, "Trace formula in noncommutative geometry and the zeros of the Riemann zeta function") does **not** construct a self-adjoint operator whose eigenvalues are the $\gamma_\rho$. What he constructs is:

- An action of the idele class group $C_\mathbb{Q}$ on $L^2(X)$ (adelic quotient), with scale generator $H_C=D$.
- The zeros appear as the spectrum of $H_C$ **restricted to the quotient** $L^2_\delta(X)$ after removing the pole contribution — and crucially, they appear as **gaps** (absorption) in a **continuous** spectrum of $H_C$ on the unrestricted space. Connes himself emphasizes: it is an **absorption** spectrum, "missing spectral lines", not genuine emission eigenvalues.

**The decisive technical difference.**
- *Emission*: $H$ self-adjoint on a Hilbert space, $\{\gamma\}$ = genuine point spectrum, Stone applies, RH follows immediately. This is what the hope needs.
- *Absorption*: $\{\gamma\}$ = the set of frequencies **absent** from the continuum, or equivalently poles/zeros of a scattering coefficient. **There is no self-adjoint operator whose point spectrum is $\{\gamma\}$**; there is an operator (self-adjoint, yes, with continuous spectrum $=\mathbb{R}$) whose **scattering matrix** $S(E)$ has a phase related to $\zeta$. The reality of the $\gamma$ does NOT follow from the self-adjointness of that operator (which is trivial, its spectrum is the whole line).

**The blow.** To go from absorption to emission — i.e. to turn the gaps into genuine eigenvalues of a self-adjoint operator — exactly one **positivity** is needed: that the "kernel" of the quotient $L^2_\delta$ be a genuine Hilbert space (positive-definite norm). And that positivity is, word for word, the **positivity of the Weil trace-formula distribution** (Weil positivity), which is **equivalent to RH** (Weil 1952; Bombieri, *Problems of the Millennium: RH*, Clay, 2000, §explicit formula; Connes 1999, where the global trace formula with the correct term $\equiv$ positivity $\equiv$ RH is the "missing ingredient" Connes himself declares).

$$
\boxed{\;\text{"absorption}\to\text{emission"}\;\equiv\;\text{positivity of the Weil term}\;\equiv\;\text{positivity of the trace formula}\;\equiv\;\text{RH.}\;}
$$

**Why Connes did not close RH (the adversarial reading):** because his trace formula is **unconditional as an identity** (it always holds, zeros as absorption), but the step to a self-adjoint emission operator requires proving that a certain term (the archimedean/local trace term) has the **correct sign** — Weil positivity — which is RH. Connes reduced RH to that positivity; he did not prove it. The quantum import of "Stone + wave" adds nothing to this step: Stone needs an operator **self-adjoint on a Hilbert space with point spectrum**, and producing that operator (emission) **is** the missing positivity.

### Verdict Route 3: **KILLS.**
A **KNOWN** node: positivity of the Weil trace. It is exactly the documented reason why Connes (1999) did not conclude RH. The quantum import does not route around this; it rediscovers it.

---

## Overall verdict

**ALL THREE routes kill the claim.** None fails; none leaves an escape. And — most importantly for the program — all three kill it **by reduction to the same obstruction, seen from three faces of the die**:

| Route | Killing mechanism | ζ node | New? |
|---|---|---|---|
| 1. Kreĭn | $Q$ indefinite ($\kappa=2m$); Stone does not give a real spectrum in Pontryagin; the only invariant positive-definite form $\iff$ RH | **METRIC / ORIENTATION** (the Weil form) | KNOWN (Phase 51 D161, Phase 52 D163-Route1, Phase 26 κ=2m) |
| 2. Deficiency | Generator not essentially self-adjoint; self-adjoint extension = boundary condition = phase of $\zeta$ | **BOUNDARY CONDITION / EXTENSION** | KNOWN (the Berry–Keating wall; self-adjointness of $H_C \equiv$ RH) |
| 3. Absorption | Connes gives absorption not emission; passing to emission = trace positivity | **POSITIVITY OF THE WEIL TRACE** | KNOWN (Connes 1999's declared gap) |

### Does $\zeta$ touch a NEW node? — **NO.**

The quantum import (Stone + wave equation) does **NOT open a new node**. It is a **translation into the language of mathematical quantum mechanics** of the three already-known nodes:
- "indefinite-Kreĭn" = the Phase 51 **metric** (the polarization metric carries $\zeta$ via the partition of the dual weight; here, the only form with respect to which $U$ is unitary is $Q$, indefinite except under RH).
- "deficiency indices" = the **boundary conditions** (the von Neumann choice among self-adjoint extensions $\equiv$ encoding $\zeta$ at the boundary).
- "absorption vs emission" = the **trace positivity** (Connes's gap).

These three nodes are, in Phase 52's synthesis, **manifestations of the single irreducible node: "$\zeta$ IS the duality"** (the explicit formula in the fundamental class of the zeros↔primes carrier IS the zero count). The quantum import confirms the Phase 52 wall from the Stone/von Neumann angle: every quantum accessory added (unitarity, self-adjointness, evolution) reveals $\zeta$ one level deeper:
- add **unitarity** → $\zeta$ reappears in *which form* is preserved (Route 1 = metric);
- add **domain/dynamics** → $\zeta$ reappears in *which boundary condition* (Route 2 = boundary);
- add **genuine discrete spectrum** → $\zeta$ reappears in *the positivity that discretizes it* (Route 3 = trace).

It is the same "remove an accessory, $\zeta$ goes down a floor" pattern of Phase 51→52, now with quantum accessories. **The quantum import does not escape: it re-derives the wall in Hilbert–Pólya vocabulary.**

### What would have to be true for the import to escape? (an honest list)

For the hope to survive, the following would ALL be needed SIMULTANEOUSLY:
1. **(against Route 1)** A **genuine** Hilbert space (positive-definite form), RH-free, with respect to which the evolution is unitary, distinct from $(L^2(C_\mathbb{Q}),Q)$. Equivalent to a spectral triple whose $D$ is **NOT** the prime flow (spectrum $\neq\{\log k\}$, partition $\neq\zeta$) with Chern/signature $=\kappa=2m$. This is the [central GAP] inherited from Phase 49 D156 §4.5 / Phase 51 D161 — **not built, [literature GAP]**.
2. **(against Route 2)** That the **complete** functional equation (archimedean side + Euler side) **uniquely** determine a self-adjoint extension with no RH-dependent freedom. [GAP] unresolved; the evidence (Berry–Keating) suggests otherwise.
3. **(against Route 3)** An **emission** construction (genuine eigenvalues) without going through Weil positivity. Equivalent to trace positivity via an independent route = the **Diophantine thread** (GAP-157.A / GAP 162.D), outside the current toolbox.

The three conditions are **one, in disguise**: the Connes/Deninger object with a spectrum outside $\{\log k\}$ and a partition outside $\zeta$. As long as it does not exist, the quantum import is circular.

---

## Final message

**Which route kills it:** all **three** kill it, and they are three faces of the same die. The cleanest and most fatal is **Route 1 (Kreĭn)**: unitarity with respect to the only structurally available form (the Weil form $Q$) is *J*-unitarity in a Pontryagin space $\Pi_{\kappa}$ with $\kappa=2m$; Stone's theorem **does not give a real spectrum** there, and requiring it to (positive-definite form) **is** RH. Stone is a disguised biconditional, not a lever.

**$\zeta$ node:** **KNOWN, not new.** The quantum import re-expresses the three already-mapped nodes — metric/orientation (Route1=Phase 51 D161), boundary condition (Route2=Berry–Keating), trace positivity (Route3=Connes's gap) — all collapsing to the irreducible node of Phase 52: **"$\zeta$ IS the duality"**. The Stone/von Neumann/Hilbert–Pólya vocabulary does not touch a new hiding place of $\zeta$; it finds it in the same three places, in quantum language.

**Three labeled findings:**

- **[FINDING 165.A — Stone-is-biconditional].** In the Weil/Connes scenario, "$U(t)=e^{itH}$ unitary $\Rightarrow$ $\mathrm{spec}(H)\subset\mathbb{R}$ (Stone)" is logically **equivalent** to "$Q$ positive definite" $\equiv \kappa=0 \equiv$ RH. Stone's hypothesis (genuine Hilbert space) already contains the conclusion. Unitarity is not free-structural: it is the Weil metric under another name. Exact connection: the $\kappa=2m$ of Phase 26 = the number of non-real eigenvalues of the $J$-self-adjoint generator in $\Pi_\kappa$ (Bognár/Azizov–Iokhvidov), i.e. **bridge 26-C.2 IS the Stone-on-Kreĭn theorem applied.**

- **[FINDING 165.B — deficiency-bifurcates].** The dilation generator $-i(x\partial_x+\tfrac12)$ has deficiency indices $(1,0)$ on the half-line (self-adjointness **impossible**, Stone inapplicable from the root) and indices $(n,n)$ on truncated domains (a family of extensions, where the only one with spectrum $\{\gamma\}$ encodes the phase of $\zeta$ in its boundary condition). On both branches genuine self-adjointness **is not structural**: either it does not exist, or it requires knowing $\zeta$. The functional symmetry restricts the boundary (archimedean factor $\chi$) but **does not determine it** (the Euler side is missing) — [GAP] of uniqueness declared.

- **[FINDING 165.C — absorption-is-Connes's-gap].** The quantum import collapses to the exact point where Connes (1999) stopped: the $\gamma$ are **absorption** spectrum (gaps in a continuum), not **emission** (genuine eigenvalues). The absorption→emission step = positivity of the Weil trace formula = RH. Stone requires emission (self-adjoint operator with point spectrum); producing emission **is** the missing positivity. The import adds nothing to Connes's gap: it re-derives it. The only escape = construct emission without Weil positivity = the Diophantine thread outside the toolbox.

**Adversarial conclusion:** the hope of "RH via structural unitarity through Stone" is **dead**. RH-free structural unitarity exists — but it is *J*-unitarity in Kreĭn (Route 1), or it does not fix the dynamics (Route 2), or it only gives absorption (Route 3). Turning any of the three into "Hilbert + self-adjoint + emission" is, in each case, exactly RH. The quantum import is a **mirror of the wall**, not a door.
