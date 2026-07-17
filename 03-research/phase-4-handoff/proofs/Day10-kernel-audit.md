# Day 10 — Audit of the load-bearing kernel computation, and the robust gem it leaves

Per the referee: before A.2 or Carleson, **audit** the Day-9 kernel computation, now load-bearing. Three
flagged dangers (A: which $E$; B: the diagonal formula; C: a sign/normalization flip to $e^{+\pi t/2}$).
**Outcome:** B cleared (formula re-derived); **A/C NOT cleared** — the trivialization is
*normalization-dependent* and downgraded. But the audit isolates a **space-independent theorem** (the
faithfulness ⟂ $a=0$ dichotomy) that survives the uncertainty and is the real content.

**Tags:** ✅ rigorous · ◆ conditional/standard · ⬜ open · ❌ downgraded.

---

## 1. Danger B — the diagonal-kernel formula: CLEARED ✅
For a de Branges space $\mathcal H(E)$, $E=A-iB$ ($A,B$ real entire), norm $\int|F/E|^2$, write the phase
$E(t)=|E(t)|e^{-i\varphi(t)}$ so $A=|E|\cos\varphi$, $B=|E|\sin\varphi$. The diagonal kernel (limit of the
off-diagonal $\frac{B(z)A(\bar w)-A(z)B(\bar w)}{\pi(z-\bar w)}$) is $K(t,t)=\tfrac1\pi(B'A-A'B)$. Compute:
$$
B'A-A'B=\big(|E|'\sin\varphi+|E|\varphi'\cos\varphi\big)|E|\cos\varphi-\big(|E|'\cos\varphi-|E|\varphi'\sin\varphi\big)|E|\sin\varphi=|E|^2\varphi' .
$$
$$
\boxed{\ K(t,t)=\frac{1}{\pi}\,|E(t)|^2\,\varphi'(t),\qquad \varphi'\ge0\ \text{(Hermite–Biehler)}.\ }
$$
No sign or normalization slip; $K(t,t)\ge0$ as required. **Formula is correct.**

---

## 2. Dangers A & C — which $E_\gamma$? NOT CLEARED; trivialization is normalization-dependent ◆→ downgrade
The Gamma factor admits **two** Hermite–Biehler normalizations, giving **opposite** conclusions:

| Normalization | $|E(t)|$ on $\mathbb R$ | $K(\gamma,\gamma)=\tfrac{\varphi'}\pi|E|^2$ | $\sum_\gamma K(\gamma,\gamma)$ | verdict |
|---|---|---|---|---|
| $E\sim\gamma$ (built from $\Gamma$) | $\sim e^{-\pi|t|/4}$ (**decays**) | $\sim\log\gamma\,e^{-\pi\gamma/2}\to0$ | $<\infty$ | **trivializes** (Day-9 claim) |
| $E\sim1/\gamma$ (built from $1/\Gamma$, entire) | $\sim e^{+\pi|t|/4}$ (**grows**) | $\sim\log\gamma\,e^{+\pi\gamma/2}\to\infty$ | $=\infty$ | does **not** trivialize |

Both are entire, zero-free in the UHP (legitimate HB). **The conclusion flips with the convention** —
exactly Danger C. I did **not** pin which is "the" archimedean de Branges space; that needs a reference
(de Branges, *HSEF*; Lagarias, *Hilbert spaces of entire functions and the RH*).

> **Honest downgrade.** Day-9's "$H(E_\gamma)$ trivializes (✅)" → **"◆ conditional on the decaying-modulus
> normalization."** What survives unconditionally: **neither Gamma normalization is Goldilocks** — the
> decaying one trivializes ($\mathfrak t_+$ trace-class), and the growing one fails *uniform* eval-control
> ($K(t-ib,t-ib)\sim e^{+\pi t/2}\to\infty$ in $t$, so $\mathfrak t_-$'s terms have exploding norms). The
> faithful space is **intermediate**, of the mild-weight Hardy-band type. The reframing the referee asked
> for: *"$K(\gamma,\gamma)$ rules out the Gamma–de-Branges family (both extremes fail); the leading
> candidate is a mild-weight Hardy-band space"* — **not** a victory for a specific $H^2(S_d)$.

---

## 3. The robust gem: faithfulness and $a=0$ are mutually exclusive ✅ (space-independent)
This needs **no** de Branges $E$, no convention — only RKHS positivity. It is the durable output.

**Setup.** Let $H$ be any RKHS of analytic functions on the strip with reproducing kernel $K$, in which
off-axis evaluations at depth $|b|<\tfrac12$ are bounded (so the Weil form is defined). Two facts:
- **(F1) Kernel grows off-axis:** $K(t-ib,t-ib)=\|K_{t-ib}\|^2\ge\|K_t\|^2=K(t,t)$. *(Continuation into
  the strip is "harder," so the evaluation functional is larger.* Rigorous: $K(w,w)$ is plurisubharmonic /
  the diagonal of a positive kernel; for translation-invariant $H$, $K(t-ib,t-ib)=\kappa(b)$ with
  $\kappa(b)\ge\kappa(0)$, $\kappa$ even and increasing in $|b|$.)*
- **(F2) Faithful $\iff$ kernel not vanishing:** $\mathfrak t_+=\sum_\gamma|\langle g,K_\gamma\rangle|^2$ is
  **non**-trace-class (faithful) iff $\sum_\gamma K(\gamma,\gamma)=\infty$, which (for kernels not
  oscillating to $0$) forces $\inf_t K(t,t)=:c>0$.

**Theorem (Day 10).** If $H$ is **faithful** ($c=\inf_t K(t,t)>0$) and RH fails with **infinitely many**
off-line zeros, then
$$
S_{\mathrm{off}}=\sum_{\text{off-line}}K(t_\rho-ib_\rho,\,t_\rho-ib_\rho)\ \overset{(F1)}{\ge}\ \sum_{\text{off-line}}K(t_\rho,t_\rho)\ \ge\ c\cdot\#\{\text{off-line}\}\ =\ \infty .
$$
Hence the clean sufficient condition "$\mathfrak t_-$ bounded" ($a=0$) **cannot hold in any faithful
space.** Conversely, $a=0$ (i.e. $S_{\mathrm{off}}<\infty$) requires $K(t,t)\to0$, i.e. a **trivializing**
space where $\mathfrak t_+$ is already trace-class.
$$
\boxed{\ \text{faithful}\ \Longrightarrow\ S_{\mathrm{off}}=\infty\ \Longrightarrow\ a=0\ \text{impossible}\ \Longrightarrow\ \text{relative Carleson }(a>0)\ \text{is forced.}\ }
$$

**Consequence (the conceptual phase-change).** The arithmetic difficulty of B-2 — the **relative Carleson
embedding** of the off-line zeros — is **intrinsic**: it cannot be dodged by any choice of (faithful)
Hilbert space. This proves the referee's Day-8 suspicion ("$S_{\mathrm{off}}<\infty$ hides almost all the
difficulty") in its strongest form: *faithfulness and the easy bound are incompatible*. The
space-pinning question (§2, flat vs log) affects the **form** of the Carleson condition but **not** its
necessity. *(Caveat: for marginally-trivializing kernels $K(t,t)\sim1/\log t\to0$ slowly, $\mathfrak t_+$
can stay non-trace-class while $S_{\mathrm{off}}$ becomes height-dependent; the theorem is clean for
$K(t,t)\not\to0$, e.g. flat strip Hardy, and marginal otherwise — flagged, not hidden.)*

---

## 4. Parallel advances (what is space-robust and can move now)
Per the referee's "advance other todo items so you don't stall," here is what does **not** depend on the
contested space-pinning and is therefore locked:

- **B-1 (realization exists) — space-robust ✅.** von Neumann (conjugation $f\mapsto\tilde f$ ⟹ equal
  deficiency indices) is a statement about the symmetric operator, independent of the ambient inner
  product. Unaffected.
- **EF-id (explicit-formula identity) — space-robust ✅.** $\mathfrak t(g,g)=\sum_\rho h(\gamma_\rho)$ is an
  identity of *values* on the core $\mathcal D$; the norm enters only at closure. Unaffected (and the
  indefinite RHS structure, §Q2 audit, is intrinsic).
- **The Day-10 dichotomy (§3) — space-robust ✅.** As shown, needs only RKHS positivity + faithfulness +
  infinitely many off-line zeros.
- **Over-sampling observation — space-robust ◆.** Zeta zeros have density $\tfrac1{2\pi}\log T\uparrow$,
  super-linear in any translation-invariant (constant-density) reference; so as a sampling sequence they
  are **over-complete at height**, suggesting a *lower* frame bound $\mathfrak t_+(g)\gtrsim\|g\|^2$ may
  hold (the redundancy only grows). This is **independent of the exact weight** and is the natural first
  step of form-core A.2.
- **External resolver — Bombieri / de Branges / Lagarias (literature task).** The §2 normalization is a
  *known* object; the right move is to **read which space these works use** rather than re-derive it. This
  is the single literature check that would settle §2 and pin the weight. (Flagged for the team; not
  re-derivable from scratch without the references.)

---

## 5. Status

| Claim | Day 9 | Day 10 (audited) |
|---|---|---|
| $K(t,t)=\tfrac{\varphi'}\pi|E|^2$ | used | ✅ **re-derived, correct** |
| $H(E_\gamma)$ trivializes | ✅ | ◆ **conditional on $E\sim\gamma$ (decaying) normalization** |
| Gamma–de-Branges is wrong home | implied | ✅ **both normalizations fail** (one trivial, one eval-uncontrolled) |
| faithful $\Rightarrow S_{\mathrm{off}}=\infty$ | sketched in $H^2(S)$ | ✅ **space-independent theorem** (§3) |
| $a=0$ vs faithful | — | ✅ **mutually exclusive** |
| exact weight (flat vs log) | "$H^2(S_d)$" | ⬜ open; **resolve via Bombieri/Lagarias** |

**Net (Day 10).** The referee's "audit the load-bearing kernel first" was right and productive: Danger C
is **real** — the trivialization conclusion is normalization-dependent, so "use strip Hardy" is downgraded
to "the Gamma–de-Branges family is ruled out; the faithful space is an intermediate mild-weight Hardy-band
type, to be pinned from the literature." But the audit **upgraded** the robust core into a
space-independent theorem: **in any faithful space, $S_{\mathrm{off}}=\infty$, so the relative Carleson
($a>0$) problem is unavoidable** — the arithmetic difficulty is intrinsic, not a modeling artifact.
**Next:** (1) literature check (Bombieri/Lagarias) to pin §2; (2) the over-sampling/lower-frame-bound first
step of form-core A.2 (space-robust); (3) only then the relative-Carleson characterization.
