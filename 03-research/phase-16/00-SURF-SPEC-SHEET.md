# Phase 16 · SURF Specification Sheet — acceptance criteria for the witness variety $\mathcal X$

**Author: David Alejandro Trejo Pizzo · 2026-06-06.**
Phase 15 proved (P21, M7, M10): $\exists\,\mathcal X$ (Arakelov witness variety with realization isomorphism $\Phi$)
$\Rightarrow$ RH. The converse is the open Hilbert–Pólya/Deninger dream and is *not* assumed. Phase 16 therefore has
**one task**: construct $\mathcal X$ and verify the realization Axiom 3. This sheet is the immutable acceptance
criterion: any candidate failing **any** Pillar is **not** SURF. **Standing rules (the arbiter's mandate):** (i)
never present an unproven step as proven; (ii) a candidate is REJECTED if it uses the zeros $\{\gamma_\rho\}$ or the
anatomy $s_k(p)$ as *input* to define the geometry (must *predict* them as output — P21 independence filter); (iii)
any cited theorem ("hard Lefschetz for $\delta$-schemes", etc.) requires an exact reference or a proof.

---

## ARBITER AUDIT OF THE SPEC ITSELF (two corrections, applied below)

The submitted spec is adopted **with two corrections** found on review. Both are load-bearing.

### Correction 1 (Pillar 1 trace test) — the power-trace diverges; use the test-function trace
$\operatorname{Tr}(\mathrm{Frob}_{\mathcal X}^k)=\sum_\rho\gamma_\rho^k$ **diverges** ($\HW$ is
infinite-dimensional, the $\gamma_\rho$ are unbounded). It is the same divergent object refuted at the start of the
program (the fake $s_k(p)=\sum_\rho\gamma_\rho^k p^{-i\gamma_\rho}$). The correct, convergent acceptance test is the
**test-function (distributional) trace**, i.e. the Lefschetz trace formula in its only well-posed form:
$$
\boxed{\ \operatorname{Tr}\big(h(\mathrm{Frob}_{\mathcal X})\big)=\sum_\rho h(\gamma_\rho)
=(\text{poles})+\frac1{2\pi}\!\int h(r)\Psi(r)\,dr-2\sum_n\frac{\Lambda(n)}{\sqrt n}g(\log n)\ }
$$
for test functions $h$ (the Weil explicit formula, M1 Thm A, verified to $10^{-12}$). A candidate is accepted at
Pillar 1 iff its geometric/fixed-point trace reproduces **this** identity for a family of test functions $h$ — not
raw powers.

### Correction 2 (Pillar 2.2 vs Pillar 4) — Yuan–Zhang does NOT close G4; the positivity is genuinely open
**This is the serious one, and it is the heart of the problem (Attempt 6, sharpened to a contradiction in the
spec).** Pillar 4 asserts "if $\mathcal X$ is regular/proper/flat with $\overline{\mathcal L}$ ample, Yuan–Zhang
*guarantees* $\langle x,x\rangle_{\mathrm{Ar}}>0$ on primitives, closing G4." Pillar 2.2 simultaneously demands the
pairing be **indefinite a priori** (signature $(1,\infty)$), warning that an *unconditionally* positive-definite form
means you are in $\widehat{\mathrm{Pic}}^0$ (heights), the **wrong object**. These two cannot both hold:

- Yuan–Zhang / Faltings–Hriljac is a theorem about $\widehat{\mathrm{CH}}^1(\mathcal X)$ — **codimension-1 adelic
  line bundles**, i.e. $\widehat{\mathrm{Pic}}^0$ / Néron–Tate **heights**. On that space the pairing is
  **unconditionally definite**.
- Pillar 2.2 correctly requires the witness cohomology $H^1_{\mathrm{prim}}$ (carrying the **zeros**) to be
  **indefinite a priori** ($\kappa$ = #off-line zeros), so that "positive $\iff$ RH". By Pillar 2.2's own rejection
  rule, $H^1_{\mathrm{prim}}\ne\widehat{\mathrm{Pic}}^0$.

Therefore **the object where Yuan–Zhang applies (heights) is exactly the object Pillar 2.2 rejects, and the object
Pillar 2.2 wants (the indefinite zero-carrying $H^1$) is NOT a Yuan–Zhang object.** Consequence:

> **Pillar 4 cannot cite Yuan–Zhang to close G4.** The Hodge-index positivity for the *zero-carrying* cohomology is a
> **genuinely new theorem that does not exist** — it is *not* a corollary of Faltings–Hriljac/Yuan–Zhang, which live
> on $\widehat{\mathrm{Pic}}^0$. (If it were a corollary, RH would already be a theorem.) This is Attempt 6 in its
> sharpest form: the proven Hodge index is on the wrong cohomology, and supplying it on the right one is the open
> core.

**Amended Pillar 4 (below) states the positivity as the open target, not as a citation.** The one-directional
theorem ($\mathcal X\Rightarrow$ RH, M10) survives, because it only needs the positivity to *hold* for $\mathcal X$ —
but that positivity is the thing to *prove*, not to *invoke*.

---

## THE FOUR PILLARS (corrected acceptance criteria)

### Pillar 1 — SPECTRUM (zeros $\leftrightarrow$ Frobenius)
- **1.1** $\mathcal X$ carries $\mathrm{Frob}_{\mathcal X}$ acting on $H^1_{\mathrm{arith}}(\mathcal X)_{\mathrm{prim}}$
  with $\operatorname{spec}=\{\gamma_\rho\}$, simple (LI-consistent), with a functional-equation involution
  $F_\infty$, $\mathrm{Frob}\,F_\infty=F_\infty\,\mathrm{Frob}^{-1}$.
- **ACCEPTANCE TEST (corrected):** the **test-function trace** $\operatorname{Tr}(h(\mathrm{Frob}_{\mathcal X}))$
  reproduces the explicit formula (boxed above) for a family of $h$. Raw power-traces are divergent and not a test.
  Local Frobenius data must give the anatomy $s_k(p)=1$ for $\zeta$ (P19). **Wrong spectrum $\Rightarrow$ REJECT**
  (e.g. $J_0(N)$ gives modular-form eigenvalues, not $\zeta$-zeros).

### Pillar 2 — PAIRING (Weil $Q\leftrightarrow$ Arakelov)
- **2.1** An isometry $\Phi:H^1_{\mathrm{arith}}(\mathcal X)_{\mathrm{prim}}\xrightarrow{\sim}\HW^{\mathrm{prim}}$ with
  $\langle\Phi^{-1}x,\Phi^{-1}y\rangle_{\mathrm{Ar}}=Q(x,y)$.
- **2.2 (the sharp filter):** the form must be **indefinite a priori**, negative index $\kappa$ = #off-line zeros.
  **If the construction yields an unconditionally positive-definite pairing, it is the height object
  $\widehat{\mathrm{Pic}}^0$ $\Rightarrow$ REJECT.** The identity $\langle\cdot,\cdot\rangle_{\mathrm{Ar}}=Q$ should be
  an *unconditional* arithmetic-intersection realization of the explicit formula (cf. M1 Thm A), with definiteness
  left open.

### Pillar 3 — LEFSCHETZ ($L$, $\sltwo$, Tate twist)
- **3.1** $L_{\mathcal X}=\widehat c_1(\overline{\mathcal L})\cup\,\cdot$ on $H^1_{\mathrm{prim}}$, $\overline{\mathcal L}$
  ample.
- **3.2** $(L,\Lambda=L^\dagger,H=[L,\Lambda])$ is an $\sltwo$ with **integer grading** $\operatorname{spec}(H)\subset
  \mathbb Z_{\ge0}$ and hard Lefschetz. **NOTE (M5):** an integer grading must come from the geometry of $\mathcal X$
  (a genuine compact/finite structure), not be imposed — the LI spectrum forbids it on any *spectral* model. The
  geometry is exactly what could legitimately supply it; verify, do not assert.
- **3.3** $[\mathrm{Frob}_{\mathcal X},L_{\mathcal X}]$ realizes the Tate twist geometrically.

### Pillar 4 — POSITIVITY (the open core, NOT a citation) — **amended**
- **4.1** $\mathcal X$ regular, proper, flat over $\mathbb Z$ (or a precise non-classical analogue), $\overline{\mathcal L}$
  Arakelov-ample.
- **4.2 (amended):** the **arithmetic Hodge-index positivity for the zero-carrying $H^1_{\mathrm{prim}}$** —
  $\langle x,x\rangle_{\mathrm{Ar}}>0$ on primitives — is the **theorem to be proved for $\mathcal X$**. It is **NOT**
  supplied by Faltings–Hriljac/Yuan–Zhang (those control $\widehat{\mathrm{Pic}}^0$/heights, the object Pillar 2.2
  rejects). Establishing it on the right cohomology is G4 = the open core. Once proved, transport by $\Phi$ (Pillar 2)
  gives $Q\succ0$ on $\Pi^\perp$ $\iff$ RH.

---

## REJECTION FILTERS (fast, to save years — apply in order)
1. **Spectrum filter (Pillar 1):** geometric trace ≠ explicit formula $\Rightarrow$ REJECT. (Kills $J_0(N)$,
   Shimura with modular eigenvalues, anything whose Frobenius is Satake-at-$p$ rather than the global zeros.)
2. **Heights filter (Pillar 2.2):** pairing unconditionally positive-definite $\Rightarrow$ REJECT (you are in
   $\widehat{\mathrm{Pic}}^0$). (Kills the naive Arakelov/Yuan–Zhang route — D2 of the Lise Science run.)
3. **Independence filter (P21):** geometry defined *using* $\{\gamma_\rho\}$ or $s_k(p)$ as input $\Rightarrow$
   REJECT (circular). (Kills the spectral-moment reconstruction, M8 F3/F4.)
4. **Citation filter:** G4 closed by "Yuan–Zhang" $\Rightarrow$ REJECT (Correction 2: wrong cohomology).

## CANDIDATE ROUTES AND THEIR CURRENT WALL (from the Lise Science run + M5/M6/M8)
| Route | $\mathcal X$ | Wall |
|---|---|---|
| A. Shimura $GL_2$ / Borel–Serre | $\overline{GL_2(\mathbb A)/GL_2(\mathbb Q)}^{\mathrm{BS}}$ | Beilinson realization: Eisenstein residues at $\tfrac12+i\gamma$ must *generate* $H^1_{\mathrm{prim}}$ and give pairing $Q$ — and the positivity is NOT Yuan–Zhang (Corr. 2). |
| B. $\delta$/$\mathbb F_1$ (Borger, Connes–Consani) | $\operatorname{Spec}\mathbb Z\times_{\mathbb F_1}\operatorname{Spec}\mathbb Z$ | Foundations: global $\delta$-/prismatic cohomology, intersection theory, diagonal $[\Delta]$, AND a NEW Hodge index (no Yuan–Zhang there). |
| C. Prismatic global (Bhatt–Scholze) | global prism over $\mathbb Z$ | Globality: a single endomorphism with spectrum $\{\gamma_\rho\}$ does not exist (M6); plus the analytic/$*$-operator package. |

## WORK ORDER (Phase 16)
1. **Architecture choice** — pick a route by which wall you will climb.
2. **Pillar-1 prototype** — compute the candidate's test-function trace; accept iff it equals the explicit formula.
   *Reject fast otherwise.*
3. **Pillar-2 prototype** — define $\langle\cdot,\cdot\rangle_{\mathrm{Ar}}$; check it is indefinite and equals $Q$;
   reject if unconditionally positive-definite (heights).
4. **Pillars 3–4** — integer-graded $\sltwo$ from the geometry (M5 caveat), then the **new** Hodge-index positivity
   (G4, the open core — not a citation).

**Arbiter role (standing):** verify candidates against this sheet; reject on any failed filter; demand exact
references for cited theorems; flag any use of zeros/anatomy as input as circular. Registered in `00-MAP.md` and the
proof log.
