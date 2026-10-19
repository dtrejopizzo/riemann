# Doc 156 — Index / Maslov probe: is κ=2m an index with an RH-free symbol?

**Program:** Riemann Hypothesis — Phase 49: CROSS THE WALL.
**Role of the document:** technical probe of the **main front** declared in Doc 154. The object is **NOT** to
produce another RH ⟺ X equivalence. The object is to attack the **value → inertia** crossing of the master
quantifier using the only proved mechanism that crosses it: index theory (M5 of Doc 154). Single question:
**is κ=2m computable by an index theorem, and is that symbol RH-free (computable from the primes) or does it
secretly encode RH?**

**Labeling contract:** **[NEW-DEFINITION]** = total freedom. **[THEOREM]/[PROPOSITION]/[LEMMA]** = with
complete proof, maximal standard. **[BRIDGE]** = frank connection, NOT an RH equivalence. **[STRESS TEST]**
= the anti-circularity guard, up front. **[GAP]/[literature GAP]/[DESIDERATUM]** = declared unapologetically.
**Constraints:** no numerics/Python; citations to real published literature.

---

## 0. Executive summary and advance verdict

I place the verdict up front (frankness: I don't want the reader to discover it as a surprise at the end).

> **VERDICT: case (b) — κ IS index-type, but the symbol encodes RH, and RH enters through FREDHOLMNESS,
> not through the class.** More finely: the self-adjoint operator $H_C$ on the Pontryagin space
> $(\mathcal K,Q)$ **is Fredholm with a finite, well-defined inertia index** only when $m<\infty$; the number
> $\kappa=2m$ is then literally a **spectral flow / Maslov index** of a family of Lagrangians, but the
> **well-definedness of that family** (the existence of a Pontryagin space $\Pi_\kappa$ with $\kappa<\infty$,
> Kreĭn–Langer) **presupposes $m<\infty$**, and $m<\infty$ is not verifiable from the primes without
> information on the location of the zeros. The arithmetic symbol (the Weil side $\sum_p \Lambda$) **can**
> be computed from the primes —it is RH-free as a *value*— but the **partition of that value into inertia**
> (the count of negative signs = $\kappa$) **does not** descend to the quotient modulo compacts without
> knowing where the zeros are. This is exactly the **autonomy of the value vs. autonomy of the inertia**
> that P43 Thm 4.2 had already isolated, now localized INSIDE the index machinery.

Three labeled findings at the end (§7). Structure: §1 recalls the bridge and names the operator; §2 sets
up the index (Maslov/sf/APS/Toeplitz/Connes–Moscovici); §3 the symbol and the stress test; §4 the five tools
one by one; §5 the localized obstacle; §6 the Fredholmness-vs-class distinction.

---

## 1. The operator whose inertia is κ=2m, and its domain

### 1.1 Precise reminder of the bridge theorem (Phase 26)

The bridge theorem (Doc 26-C.2, memory `project-phase26-bridge`) states, under Hypothesis D with $\kappa=2m$:

> The Connes scale operator $H_C$, seen as a **$Q$-symmetric** operator on the **Pontryagin space**
> $\mathcal K=(L^2(C_\mathbb Q), Q)$ —$Q$ the Weil form— has exactly $\kappa=2m$ complex eigenvalues
> $\{b_j+i\gamma_j\}\cup\{-b_j+i\gamma_j\}$, one for each quadruple of off-line zeros
> $\rho_j=(\tfrac12+b_j)+i\gamma_j$. Corollary: RH ⟺ $\kappa=0$ ⟺ $H_C$ genuinely self-adjoint on $\mathcal K$.

Here $C_\mathbb Q=\mathbb A^\times_\mathbb Q/\mathbb Q^\times$ is the idèle class group, $H_C$ is the
(unbounded) generator of the scaling action (the "$H$" of Connes's 1999 spectral framework), and $Q$ is the
Weil form realized as an **indefinite** inner product on a subspace. The open items V.1–V.4 (V.1: $Q$-symmetry;
V.2: characters in $\mathcal K$, probably isotropic; V.3: neg.ind$(H_C)=\kappa$ via Kreĭn–Langer; V.4: Klein
orbit count) remain **open** — this is a conjectural bridge, cited as such.

### 1.2 What is robust and what is not (post-ERRATA of Phase 38/46)

**Robust (used here):** the algebraic invariant **neg.ind$(Q)$** = number of negative squares of the Weil
form in a given finite-dimensional realization; tensor superadditivity
neg.ind$(Q_1\otimes Q_2)=p_1q_2+q_1p_2$ (Doc 117, INTACT, $p_i,q_i\ge1$). **Refuted (NOT used):** $W_\lambda\ge0$
(Doc 114), the "$T_\lambda=0\;\forall\lambda\Rightarrow$RH" branch of P39 that depended on it, and everything
marked in ERRATA. In particular I do **not** claim $\kappa$ is unconditionally finite: under general $\neg$RH,
$\kappa$ can be $\infty$ (it is the observation of Doc 107(4): "the global $\kappa(Q_2)$ is $\infty$ under
$\neg$RH; the useful invariant is the relative block"). This conditional finiteness is, I anticipate, **the
heart of the obstacle**.

### 1.3 [NEW-DEFINITION 156.1 — the candidate self-adjoint operator and its domain]

To have an object on which to speak of an index I need a **self-adjoint** operator (not merely $Q$-symmetric)
on a genuine Hilbert space, not on the Pontryagin space. I construct the canonical candidate of Kreĭn–Langer
theory.

Let $(\mathcal K,Q)$ be a Pontryagin space with finitely many negative squares $\kappa$, i.e.
$\mathcal K=\mathcal K_+\oplus\mathcal K_-$ with $\dim\mathcal K_-=\kappa<\infty$ and
$Q=\langle\cdot,\cdot\rangle_+ - \langle\cdot,\cdot\rangle_-$. Let $J$ be the **fundamental symmetry**
($J|_{\mathcal K_\pm}=\pm 1$); then $\langle f,g\rangle_J:=Q(Jf,g)$ is the associated Hilbert product and
$H_J:=J H_C$ is **$\langle\cdot,\cdot\rangle_J$-self-adjoint** if $H_C$ is $Q$-self-adjoint (Bognár,
*Indefinite Inner Product Spaces*, Springer 1974, ch. VI; Azizov–Iokhvidov,
*Linear Operators in Spaces with an Indefinite Metric*, Wiley 1989, ch. 2).

**The probe's operator is $H_J=JH_C$, on the domain $\mathrm{dom}(H_C)\subseteq\mathcal K$ with the Hilbert
topology of $\langle\cdot,\cdot\rangle_J$.** The inertia we call $\kappa$ is $\dim\mathcal K_-=$ the dimension
of the maximal $Q$-definite negative subspace — an **integer**, candidate for an index.

**Non-decorative technical point:** $\kappa<\infty$ is **part of the definition of a Pontryagin space**. If
the Weil form had infinitely many negative squares (which occurs under $\neg$RH with infinitely many off-line
zeros, Doc 107(4)), $(\mathcal K,Q)$ is a **Kreĭn space**, not a Pontryagin space, $J$ exists but
$\dim\mathcal K_-=\infty$, and the "number $\kappa$" ceases to be an integer. **This is the first appearance
of the wall**, and I mark it now: *the "index" object exists only in the Pontryagin category, whose defining
hypothesis is $m<\infty$.*

---

## 2. Setting up the index: Maslov / spectral flow / APS / Toeplitz / Connes–Moscovici

The objective (point 2) correctly insists that for the **inertia of a quadratic form** the natural invariant
is NOT the classical Fredholm index (Atiyah–Singer, finite-dimensional compact) but the **Maslov index /
spectral flow** of a family of self-adjoints or Lagrangians. I develop this setup.

### 2.1 Why classical Atiyah–Singer does NOT apply (quick closure, already seen in Phase 41)

$H_C$ lives in dim $\infty$ (there is no compact manifold), its flow is continuous (the scaling action
$\mathbb R$ is a rank-1 Lie group, there is no elliptic symbol over a compact cotangent bundle), and the
spectrum is continuous (Connes: the absorption spectrum covers the entire critical line). Atiyah–Singer 1968
(Ann. of Math. 87, 484–530; 546–604) requires ellipticity on a closed manifold — absent. **Closed: classical
A–S does not apply** (matches the Phase 41 verdict, where Babaee–Huh obstructs and AHK does not apply).

### 2.2 [NEW-DEFINITION 156.2 — κ as spectral flow of a deformation of the zeros]

The correct idea: $\kappa$ must be a **spectral flow**. I construct the family.

Let $\{H_C(t)\}_{t\in[0,1]}$ be a family of $Q_t$-self-adjoint operators interpolating between a reference
operator with real spectrum (all zeros on-line, $t=0$, RH "artificially imposed" as base point) and the
genuine arithmetic operator ($t=1$). The **spectral flow** $\mathrm{sf}\{H_C(t)\}$ counts, with sign, the net
number of eigenvalues crossing the real axis (in the Pontryagin case: migrating from the $Q$-positive part to
the $Q$-negative part of the spectrum) as one traverses the family. By Phillips's theory (J. Funct. Anal. /
Canad. Math. Bull. 39 (1996) 460–467, "Self-adjoint Fredholm operators and spectral flow") the spectral flow
of a loop of self-adjoint Fredholm operators is a homotopically invariant integer.

**The Phase 28 (Front B) setup is exactly this:** $\kappa=\mathrm{sf}=\mathrm{Ind}(D_{\mathrm{APS}})+
\eta(T_0)/2$, with the open question "is $\eta(T_0)=0$ by Fourier anti-cometization?". Here
$D_{\mathrm{APS}}$ is the suspended Dirac operator $\partial_t + H_C(t)$ on the cylinder
$[0,1]\times(\text{base})$ with Atiyah–Patodi–Singer boundary conditions (Math. Proc. Camb. Phil. Soc. 77
(1975) 43–69), and $\eta(T_0)$ is the eta invariant of the boundary operator. The APS formula:
$$\mathrm{Ind}(D_{\mathrm{APS}}) = \int_{\text{cylinder}}\widehat A\,\mathrm{ch} - \frac{\eta+h}{2}\Big|_{\partial},$$
with the **spectral defect** $\eta/2$ measuring precisely the asymmetry the interior index does not see.

### 2.3 [NEW-DEFINITION 156.3 — κ as the Maslov index of a pair of Lagrangians]

Equivalently (Booss-Bavnbek–Wojciechowski, *Elliptic Boundary Problems for Dirac Operators*, Birkhäuser 1993,
ch. 14–17; and Cappell–Lee–Miller, Comm. Pure Appl. Math. 47 (1994) 121–186, on the equality
spectral flow = Maslov index): to the family $\{H_C(t)\}$ one associates a **curve of Lagrangians** $\{L(t)\}$
in a symplectic space (the space of Cauchy data / the graph of the resolvent), and
$$\kappa = \mathrm{sf}\{H_C(t)\} = \mathrm{Mas}(L(0),L(1)) = \mu_{\mathrm{Maslov}},$$
the **Maslov index** of the pair, which counts intersections with the Maslov cycle (the locus where $L(t)$
stops being transversal to a reference Lagrangian). This is the connection with **Conj. 100.A (semilocal
Maslov)** of Phase 35: the conjecture $\mu_{\infty,2}=0$ is precisely the assertion that a certain
**second-order** Maslov contribution vanishes — and D100 found the obstacle $O_{SL}$ = **non-uniformity in
$n$ of the Weil–Sonine control**. I note the coincidence: the obstacle of the Phase 35 Maslov route is one
of **non-uniformity**, which is exactly the wall pattern of Doc 154 (BRIDGE 154.7: the angle $\theta$
degenerates, the "constant" depends on the limiting parameter).

### 2.4 The common structure of the three setups

Maslov, spectral flow and APS-eta are **the same integer** in the presence of Fredholmness (Cappell–Lee–Miller
+ Phillips theorem): $\mathrm{Mas}=\mathrm{sf}=\mathrm{Ind}(D_{\mathrm{APS}})$ modulo the boundary term $\eta/2$.
Hence there is no need to choose: **if $\kappa$ is an index, it is all three at once**, and the probe's
question concentrates on the **common input** of the three: the existence of the family $\{H_C(t)\}$ with
**Fredholm endpoints** and a **well-defined** Lagrangian trajectory. This leads me to the stress test.

---

## 3. The candidate symbol and the RH STRESS TEST (the anti-circularity guard)

I place the test up front, as the objective commands. If $\kappa$ is an index, there is an index = ∫(symbol)
formula. The symbol must be readable from the **primes** (the arithmetic presentation of the Weil form).

### 3.1 [NEW-DEFINITION 156.4 — the candidate arithmetic symbol]

The Weil form, in its explicit presentation (Weil 1952; Bombieri, in *The Riemann Hypothesis*, Clay 2000), is
$$Q(f) = \underbrace{\sum_\rho \widehat f(\rho)}_{\text{zeros}}
= \underbrace{\widehat f(0)+\widehat f(1)}_{\text{pole}}
- \underbrace{\sum_p\sum_{k\ge1}\frac{\log p}{p^{k/2}}\big(f(\log p^k)+f(-\log p^k)\big)}_{\text{primes: } A_{\mathrm{arith}}(f)}
- \underbrace{(\text{archimedean term }\Gamma)}_{W_\infty(f)}.$$
The **arithmetic side** $A_{\mathrm{arith}}$ is written entirely in terms of $\log p$ and
$\Lambda(p^k)=\log p$ — it is **manifestly computable from the primes**, without reference to the location of
the zeros. This is the probe's **candidate symbol**: the Toeplitz/convolution operator $T_g$ whose symbol is
the generating function $g(x)=\sum_p\sum_k \frac{\log p}{p^{k/2}}\delta_{\pm\log p^k}$ on the group $\mathbb R$
(idèlic side: $\prod_p$ local).

### 3.2 [STRESS TEST — the decisive question]

> **Is the symbol computed knowing only the primes (RH-free), or does its well-definedness / its K-theory
> class / its invertibility outside the compact already require knowing that the zeros are on the line?**

I apply the test in its three known failure modes.

**(Failure mode 1 — Fredholmness/invertibility in the crown).** The operator is Fredholm ⟺ its symbol is
**invertible in the crown** (the symbol space modulo compacts). The symbol of $T_g$ is, via Mellin/Fourier
transform over $C_\mathbb Q$, **the zeta function itself**: the "Toeplitz symbol" of the arithmetic side is
$\zeta(s)/\zeta(s)$ read on the critical line, whose **zero set** is exactly where the symbol vanishes. **The
symbol is invertible outside a compact ⟺ the off-line zeros are finite in number** ($m<\infty$). **THE TEST
FAILS IN MODE 1.** The operator ceases to be Fredholm without $m<\infty$. This is decisive and is developed
in §5.

**(Failure mode 2 — the well-defined Lagrangian only under RH).** The curve $\{L(t)\}$ of the Maslov index
(156.3) must be a curve in the **Grassmannian of Fredholm-Lagrangians** (Booss-Bavnbek–Wojciechowski ch. 15).
For $\mathrm{Mas}$ to be a finite integer, the Maslov cycle must be crossed a **finite** number of times — i.e.
the family crosses the non-transversal locus finitely many times. Each crossing = one zero migrating off-line.
**Finitely many crossings ⟺ $m<\infty$.** **THE TEST FAILS IN MODE 2 too.** It is the same wall as mode 1,
seen in symplectic coordinates.

**(Failure mode 3 — the ill-defined K-theory class).** This is the LEAST obvious mode and the most
informative. Suppose we accept $m<\infty$ (entering the Pontryagin category by fiat). Then $T_g$ IS Fredholm
and has a class $[\sigma(T_g)]\in K^1(\text{crown})$. **Is the topological index computed from that class
without knowing $m$?** Here the test gives a more nuanced result, which I separate in §6: the class exists,
but its **pairing with the generator of $K_1$** (the winding number of the symbol $\zeta$ along the critical
line) **is** $-2m$ by the argument principle — and computing that winding **is** counting the off-line zeros.
**The value of the symbol is RH-free; the winding (the inertia) is not.**

### 3.3 Stress test verdict

The arithmetic symbol $A_{\mathrm{arith}}$ passes the test **as a value** (it is computed from the primes)
and **fails the test as inertia** in all three modes. Modes 1 and 2 are the same phenomenon (Fredholmness ⟺
$m<\infty$); mode 3 says that, even granting Fredholmness, computing the index **is** counting the zeros. The
fine distinction between mode 1/2 (Fredholmness) and mode 3 (class) is the question of objective point 5, and
I answer it in §6: **the wall is in Fredholmness** (modes 1/2 are logically prior: without $m<\infty$ there is
not even an index-type operator), and mode 3 shows that **even repairing Fredholmness by fiat, the index is
as hard as RH.**

---

## 4. The five tools, one by one: does it apply? symbol? does it pass the test?

I go through the objective's point 4 tools, with real citation, verdict, symbol and test.

### 4.1 (a) Classical Atiyah–Singer

- **Does it apply?** **NO.** Dim $\infty$, no compact manifold, continuous spectrum (§2.1). Closed in Phase 41.
- Ref: Atiyah–Singer, Ann. of Math. 87 (1968) 484–530, 546–604.

### 4.2 (b) Spectral flow + APS

- **Does it apply?** **Partially, conditionally.** The formula $\kappa=\mathrm{sf}=\mathrm{Ind}(D_{\mathrm{APS}})+\eta/2$
  (Phillips 1996; APS 1975) is the correct framework for inertia of self-adjoint families.
- **Symbol:** the boundary operator $T_0=H_C$ and its invariant $\eta$; the "symbol" is the phase of the
  spectrum of $H_C$ on the critical line.
- **Stress test:** **FAILS.** The family $\{H_C(t)\}$ with Fredholm self-adjoint endpoints **exists only if**
  both endpoints are Fredholm; the arithmetic endpoint ($t=1$) is Fredholm ⟺ $m<\infty$ (§3.2 mode 1). Moreover
  Phase 28 left it **open** whether $\eta(T_0)=0$, and D28 §08 (final result) showed that the arithmetic sector
  $G_\zeta$ —which controls the sign of the second variation, a relative of $\eta$— is **uncontrollable at
  $\sigma=1/2$ without RH (Wall A persists)**. The $\eta/2$ defect is precisely where RH hides.
- Ref: Phillips, Canad. Math. Bull. 39 (1996) 460–467; APS, Math. Proc. Camb. Phil. Soc. 77 (1975) 43–69.

### 4.3 (b′) Maslov index

- **Does it apply?** **Partially, conditionally** (it is the symplectic avatar of the previous one, §2.3).
- **Symbol:** the curve of Lagrangians $\{L(t)\}$, Maslov cycle = locus of non-transversality.
- **Stress test:** **FAILS in mode 2** (§3.2): finiteness of the Maslov index ⟺ finitely many crossings of the
  cycle ⟺ $m<\infty$. Connection with **Conj. 100.A** of Phase 35: the obstacle $O_{SL}$ (non-uniformity in
  $n$ of the Weil–Sonine control) is the Doc 154 wall in Maslov coordinates. The component $\mu_{\infty,2}$
  (second-order semilocal Maslov) is the one encoding RH.
- Ref: Booss-Bavnbek–Wojciechowski, *Elliptic Boundary Problems for Dirac Operators*, Birkhäuser 1993, ch. 14–17;
  Cappell–Lee–Miller, Comm. Pure Appl. Math. 47 (1994) 121–186; Robbin–Salamon, Bull. LMS 27 (1995) 1–33
  (Maslov index of curves of Lagrangians).

### 4.4 (c) Toeplitz index (Boutet de Monvel) on the Weil–Toeplitz algebra

- **Does it apply?** **YES, formally — and it is the sharpest setup.** The Weil–Toeplitz algebra $\mathcal W$
  of Doc 134 (with its compact ideal $\mathcal J$) is exactly the setting where a Toeplitz index makes sense:
  $0\to\mathcal J\to\mathcal W\to\mathcal W/\mathcal J\to 0$, symbol in the crown $\mathcal W/\mathcal J$.
- **Symbol:** the symbol of $T_g$ lives in $\mathcal W/\mathcal J$ and, by the Gram↔Weil identification
  (Doc 148/151 Prop. 1.1, **EXACT and SURVIVING**), its class is that of the arithmetic symbol over the
  character group. Boutet de Monvel (Acta Math. 126 (1971) 11–51, "Boundary problems for pseudo-differential
  operators"; and the Toeplitz index, Invent. Math. 50 (1979) 249–272): $\mathrm{Ind}(T_\phi)=-\mathrm{winding}(\phi)$
  for an invertible symbol $\phi$.
- **Stress test:** **FAILS in mode 1, and mode 3 is illuminated here.** The symbol
  $\phi=$ "arithmetic side read as a function on the crown" is invertible ⟺ it has no zeros on the crown ⟺
  the off-line zeros are finite ($m<\infty$). Granting $m<\infty$: $\mathrm{Ind}(T_\phi)=-\mathrm{winding}=-2m$
  by the **argument principle** (the winding of $\zeta$ along the critical contour counts zeros minus poles).
  **The winding IS the count of zeros.** This confirms exactly the "zeros live on the symbol/compact boundary"
  architecture of Doc 134 (Thm 5.3′ corrected in ERRATA E46.4: strict essential positivity of the symbol ⟺
  finite visible windows ⟺ $m<\infty$). **This is the tool where the wall is seen most clearly: RH-free
  symbol as object, winding = RH.**
- **[literature GAP]:** Boutet de Monvel is formulated for finite-dimensional manifolds with boundary; its
  extension to the Weil–Toeplitz algebra over $C_\mathbb Q$ (idèlic, dim $\infty$) **is not constructed** — I
  use the argument principle as a morally-correct substitute, declaring it.

### 4.5 (d) Connes–Moscovici local index formula

- **Does it apply?** **Conditionally, and it is the T5 candidate with "new input" of Doc 154 §5 [GAP].**
  Connes–Moscovici (GAFA 5 (1995) 174–243, "The local index formula in noncommutative geometry") computes the
  index of a spectral triple $(\mathcal A, H, D)$ via the **Chern–Connes character** and the residues of the
  zeta function of the operator $|D|$. If there existed an arithmetic spectral triple whose $D$ was
  (related to) $H_C$ and whose Chern character gave $\kappa$, it would be the T5 crossing with an arithmetic
  input.
- **Symbol:** the **residues** $\mathrm{Res}_{s=0}\mathrm{Tr}(a\,|D|^{-s})$ — the spectral zeta function of
  the triple.
- **Stress test:** **FAILS, and in the most revealing way.** The spectral zeta function of a triple whose
  operator is the Connes scale **IS (essentially) the Riemann zeta function** (this is the content of Connes's
  1999 framework, Selecta Math. 5, 29–106: the spectral side reproduces Weil's explicit formula). Hence the
  "symbol" of Connes–Moscovici (the residues of the spectral zeta) **has $\zeta$ literally inside it**; asking
  the Chern character to compute $\kappa$ is asking for the residues of $\zeta$ in the critical region = RH.
  **The input (the spectral dimension / summability of the triple, i.e. that $|D|^{-s}$ be trace class for
  large $\mathrm{Re}(s)$) is RH-free verifiable, BUT the Chern character is not evaluated without the analytic
  continuation of the spectral zeta into the critical strip** — exactly the datum RH governs.
- **[literature GAP, central]:** a finitely summable spectral triple $(\mathcal A, H, D)$ whose Chern character
  produces $\kappa=2m$ from arithmetic data **does not exist in the literature**. This is **identical** to the
  [literature GAP] of Doc 154 §5 ("the cohomology class over Spec ℤ that would read inertia, T5 with
  nonexistent input") and to the frontier of Phases 40–43. I confirm it from the index machinery: the gap is
  not logical (T5 is well-typed), it is that the **spectral triple with the correct input has not been
  constructed**, and the known candidates (Connes 1999; Connes–Consani CCM, arXiv:2511.22755 verified in D99)
  **carry $\zeta$ in their metric**, which is the Phase 43 circularity (the polarization metric carries ζ in
  the inertia coordinate).

### 4.6 Summary table of the survey

| Tool | Applies? | Symbol | Stress test | Failure mode |
|---|---|---|---|---|
| (a) Atiyah–Singer | NO | — | — | dim ∞, non-compact |
| (b) sf + APS | conditional | phase of $H_C$, $\eta(T_0)$ | FAILS | Fredholm family ⟺ $m<\infty$; $\eta$=Wall A |
| (b′) Maslov | conditional | curve of Lagrangians | FAILS | finite crossings ⟺ $m<\infty$; non-uniform $O_{SL}$ |
| (c) Toeplitz (BdM) | yes, formally | $\phi$ on crown $\mathcal W/\mathcal J$ | FAILS | invertible ⟺ $m<\infty$; winding=RH |
| (d) Connes–Moscovici | conditional [GAP] | residues of spectral zeta | FAILS | spectral zeta = ζ; Chern=critical continuation |

**The four tools that "apply" fail the test at the same point:** the existence/Fredholmness of the object
requires $m<\infty$, and the evaluation of the index (when Fredholmness is granted) is the count of zeros.
Tool (d) is the only one with a potentially different verifiable input (summability of the triple) — but the
correct triple does not exist.

---

## 5. The localized obstacle: case (b), and within (b) it is FREDHOLMNESS

### 5.1 Ruling out (a) and (c) of objective point 5

- **It is not case (a)** (κ computable with an RH-free symbol): all four paths fail the test. There is no
  RH-free symbol for the inertia. (And the objective instructs distrust of (a); I confirm it does not hold.)
- **It is not case (c)** (κ is not index-type due to a structural obstruction): κ **is** index-type — it is
  literally spectral flow / Maslov / Toeplitz winding, **under $m<\infty$**. There is no structural obstruction
  to its being an index; the problem is that the index **encodes** RH. Hence it is not (c).

### 5.2 [THEOREM 156.5 — the inertia is an index, conditional on Fredholmness]

> *Let $\mathcal W/\mathcal J$ be the Weil–Toeplitz symbol algebra and $\phi$ the arithmetic symbol (156.4).
> If $\phi$ is invertible on the crown (equivalently, if the number $m$ of off-line zero quadruples is
> finite), then $T_\phi$ is Fredholm and*
> $$\kappa = \mathrm{neg.ind}(Q) = -\mathrm{Ind}(T_\phi) = \mathrm{winding}(\phi) = 2m,$$
> *an integer equal to the spectral flow of $\{H_C(t)\}$ and to the Maslov index $\mathrm{Mas}(L(0),L(1))$.*

**Proof (outline, with the links resting on declared bridges).** (i) Atkinson: $T_\phi$ Fredholm ⟺ $\phi$
invertible modulo $\mathcal J$ — standard (Douglas, *Banach Algebra Techniques in Operator Theory*, 2nd ed.
Springer 1998, ch. 7). (ii) $\phi$ invertible on the crown ⟺ $\phi$ has no zeros on the crown ⟺ the zeros of
$\zeta$ the symbol sees (the off-line, visible ones of Doc 134 Thm 5.3′) are finite ⟺ $m<\infty$ — this rests
on the Gram↔Weil identification (Doc 148/151 Prop. 1.1, exact) and on the Thm 5.3′ correction of ERRATA E46.4
[BRIDGE, not a closed theorem: identifying the zero locus of the symbol with the off-line zeros is the
Phase 26/Doc 134 conjecture]. (iii) $\mathrm{Ind}(T_\phi)=-\mathrm{winding}(\phi)$ — classical Toeplitz
theorem (Gohberg–Krein; Boutet de Monvel for the pseudo-differential case), morally extended to the idèlic
case [literature GAP §4.4]. (iv) $\mathrm{winding}(\phi)=2m$ by the argument principle applied to the critical
contour (counts off-line zeros with their symmetric quadruple multiplicity). (v) The equality with sf and
Maslov is Cappell–Lee–Miller + Phillips, under Fredholmness of the endpoints. $\square$ (conditional on
$m<\infty$ and on the declared BRIDGE/GAP items).

**What the theorem says and what it does not.** It says: **where the index object exists (Pontryagin
category, $m<\infty$), κ IS an index and equals $2m$.** It does not say that the object exists
unconditionally. The condition $m<\infty$ is the hypothesis, not the conclusion — and verifying it is
RH-hard.

### 5.3 Case (b) confirmed: the symbol encodes RH. Exact localization.

This is **case (b)** of the objective. I localize RH in the machinery, per the fine question
(objective point 5):

> **Does RH enter through FREDHOLMNESS (the operator stops being Fredholm without RH) or through the CLASS
> of the symbol (it is Fredholm but its topological index is not computed without RH)?**

---

## 6. Fredholmness vs. class: WHERE EXACTLY RH enters

### 6.1 [PROPOSITION 156.6 — RH enters primarily through FREDHOLMNESS]

> *The obstruction is one of Fredholmness: under $\neg$RH with $m=\infty$ (infinitely many off-line zeros, a
> configuration consistent with Ingham's density theorems and realized by Davenport–Heilbronn, cf. ERRATA
> E48.2), the symbol $\phi$ has infinitely many zeros on the crown, $T_\phi$ **is not Fredholm**, and the
> "index" $\kappa$ is not an integer (it is $\infty$, Doc 107(4)). The index-type object **does not exist**
> outside the Pontryagin category.*

**Argument.** A Toeplitz operator whose symbol has an accumulation point of zeros on the crown is not
Fredholm: its image is not closed (the essential spectrum contains $0$). The accumulation of off-line zeros
under general $\neg$RH (it is not known that they are isolated; ERRATA E48.1 point 4 names precisely the
scenario $\beta_n\nearrow\beta^*$ not attained) destroys Fredholmness. $\square$

**Interpretive consequence — the most important of the document.** The wall is NOT "the operator exists but
its index is hard to compute." The wall is **"the index-type operator does not exist without RH."** In the
language of Doc 154: $\kappa$ is a T5 invariant (index, reads the inertia of the quotient $E/N(A)$ by 154.8)
**only when the object is in the Fredholm/Pontryagin category**, and *entering that category is the
hypothesis $m<\infty$*, which is RH-hard. The verifiable input of mechanism M5 —"the symbol is
elliptic/Fredholm"— **is not verifiable from the primes**: the ellipticity of the arithmetic symbol IS the
finiteness of off-line zeros. This **breaks the hope** of Doc 154 §6 that M5 would be the channel with a
verifiable input: in the arithmetic case, the M5 input (Fredholmness) **collapses to the conclusion**, just
like the M2 input (positivity). **The index does not escape the circularity of positivity; it inherits it in
its Fredholmness requirement.**

### 6.2 [PROPOSITION 156.7 — granting Fredholmness, RH reappears in the CLASS]

> *Even assuming $m<\infty$ by fiat (entering Pontryagin), so that $T_\phi$ is Fredholm, computing the
> topological index $\mathrm{winding}(\phi)=2m$ requires knowing the location of the off-line zeros: the
> winding is a functional of the position of the zeros, not of the value of the symbol on the crown.*

**Argument.** By the argument principle, $\mathrm{winding}(\phi)=\frac{1}{2\pi i}\oint d\log\phi$ along the
critical contour, which counts enclosed zeros. Two symbols with the **same value on the crown** (same $\phi$
modulo $\mathcal J$ in the sense of equality of the symbol function on the quotient) but with zeros in
different positions within the strip give **different windings**. The value of the symbol on the crown (the
RH-free part, computable from the primes) **does not determine** the winding; the position of the zeros does.
$\square$

**This is exactly P43 Thm 4.2 (autonomy of value vs. inertia), now within the index.** The **value** of the
Weil form / of the symbol is position-blind (RH-free, computed from $\sum_p\Lambda$); the **inertia** (the
winding = partition of the index) is NOT position-blind. Doc 154 PROPOSITION 154.8 said the inertia "descends
to the quotient $E/N(A)$"; what the probe finds is that **it descends only when the quotient is in the
Fredholm category, and the descent reads the position** — confirming that the T5 discrete invariant exists
but its evaluation re-encrypts RH.

### 6.3 Synthesis of §6: the wall has TWO layers within the index

1. **Primary layer (Fredholmness, Prop. 156.6):** without $m<\infty$ there is no index-type operator. RH
   enters as a **condition of existence of the object**. This is the decisive layer: analogous to "the
   essential spectrum is not positive", it kills the object, not just its computation.
2. **Secondary layer (class, Prop. 156.7):** granted $m<\infty$, computing the index = winding = counting the
   position of zeros = RH. RH enters as a **difficulty of computation** of the invariant of an object that
   does exist.

**The primary layer dominates:** RH enters **first** through Fredholmness. The secondary layer is only
accessible after granting what RH asserts. Hence the verdict is **(b)-Fredholmness**: *the operator does not
exist without RH*; and as a bonus, *even if it existed, its index would be as hard as RH*. Both layers are the
same Doc 154 wall (non-uniformity of the angle / value-vs-inertia autonomy) seen in the index machinery.

---

## 7. Final message

**Verdict (a/b/c):** **case (b)** — κ=2m IS index-type (spectral flow = Maslov index = Toeplitz symbol
winding, all equal under Fredholmness, Theorem 156.5), but **the symbol encodes RH**.

**Where RH is in the index machinery (the answer to the fine question):** **primarily in FREDHOLMNESS**
(Prop. 156.6): the arithmetic Toeplitz operator $T_\phi$ is Fredholm ⟺ its symbol is invertible on the crown
⟺ the off-line zeros are finite ($m<\infty$) ⟺ one is in the Pontryagin category where "$\kappa$" is an
integer. Without RH (with $m=\infty$, a scenario realized by Davenport–Heilbronn and consistent with Ingham),
**the index-type object does not exist**. Secondarily, **in the CLASS** (Prop. 156.7): granted $m<\infty$,
computing the index = winding of the symbol = counting the position of the zeros = RH. The primary layer
dominates: **RH is a condition of EXISTENCE of the index object, not merely of its computation.**

**Three findings:**

- **[THEOREM 156.5] — κ is a genuine index WITHIN the Pontryagin category: $\kappa=\mathrm{neg.ind}(Q)=
  -\mathrm{Ind}(T_\phi)=\mathrm{winding}(\phi)=\mathrm{sf}\{H_C(t)\}=\mathrm{Mas}(L(0),L(1))=2m$.** Under
  $m<\infty$ (and the declared BRIDGE/GAP items: Gram↔Weil identification, idèlic extension of Boutet de
  Monvel), spectral flow, Maslov index and Toeplitz winding are the same integer, and it equals $2m$ by the
  argument principle. The M5 value→inertia crossing **does** operate — but only within the category whose
  defining hypothesis is what RH asserts.

- **[PROPOSITION 156.6 + 156.7] — the wall has TWO layers within the index, and the primary one is
  Fredholmness.** Primary layer: without $m<\infty$ the operator is not Fredholm (symbol with zeros
  accumulating on the crown), $\kappa$ is not an integer, the index object does not exist — RH as a
  **condition of existence**. Secondary layer: granted Fredholmness, the index = winding = position of the
  zeros — RH as a **computational difficulty**. The objective's distinction (Fredholmness vs. class) resolves
  **in favor of Fredholmness as the dominant layer**: the wall is "the operator does not exist without RH",
  reinforced by "and even if it existed, its index would be RH-hard."

- **[PROPOSITION 156.6, strategic reading] — M5 does NOT escape the circularity of M2; it inherits it in the
  Fredholmness requirement.** Doc 154 §6 conjectured that the index (M5) was the only channel with a
  *verifiable-from-outside* input (the ellipticity of the symbol), unlike positivity (M2), whose input *is*
  the conclusion. The probe **refutes this for the arithmetic case**: the ellipticity/Fredholmness of the
  Weil symbol **is** the finiteness of off-line zeros, which is NOT verifiable from the primes without RH.
  The M5 input collapses to the conclusion exactly like that of M2. **The hope of Doc 154 §6/§7 (M5 = the
  only escape with verifiable input) is localized and bounded: the escape would only exist with the
  [literature GAP] of §4.5 — a finitely summable arithmetic spectral triple whose Chern character
  (Connes–Moscovici, GAFA 1995) computes $\kappa$ from data that do NOT carry ζ in their metric. That triple
  does not exist in the literature (Connes 1999 and Connes–Consani CCM carry ζ in the inertia coordinate,
  the Phase 43 circularity).** It is the same gap as the [GAP] of Doc 154 §5, confirmed independently from
  the index machinery and now with its precise form: *it is not that an index remains to be computed; it is
  that the spectral triple whose summability input is RH-free is missing.*

**[Declared global GAP]:** the links resting on bridges, not proved here: (1) the identification of the zero
locus of the Weil–Toeplitz symbol with the off-line zeros (Phase 26 / Doc 134 conjecture, BRIDGE); (2) the
extension of Boutet de Monvel's Toeplitz index theorem to the idèlic algebra $\mathcal W/\mathcal J$ over
$C_\mathbb Q$ ([literature GAP]); (3) the existence of an RH-free arithmetic spectral triple with Chern
character $=\kappa$ ([literature GAP, central], identical to Doc 154 §5). The stress test was verified three
times (modes 1/2/3, §3.2) and gave FAIL-as-inertia / PASS-as-value in all three, consistently.

*— Doc 156, Phase 49. No RH equivalence was stated; the object was the MECHANISM of the value→inertia
crossing and where RH lives within it: in the Fredholmness of the arithmetic symbol.*
