# Phase 3 — first-pass numerical results (honest report: one confirmation, one genuine blocker)

**Route B / Phase 3.** Author: David Alejandro Trejo Pizzo · 2026-06-03.
Code: `phase3_carleson.py` (numpy + mpmath). **Self-contained Gram, NOT P7's validated engine.**

> **Outcome.** **(1) Band test — CONFIRMS T3.4:** the anatomy concentration rises to the **Hermite
> turning-point edge** ($\log p\approx4$–4.5, envelope $\sqrt{2J}/\sigma\approx4.9$), so it is a **basis
> artifact**, not arithmetic — exactly as T3.4 cautioned. The genuine band test *requires the Slepian
> flat-box basis*, which the self-contained build does not have. **(2) Carleson constant — BLOCKED:** the
> self-contained engine **fails the $\zeta$ validation gate** ($C(\zeta)\approx1.98>1$, i.e.
> $\lambda_{\min}(A_\infty-P)<0$ for RH-true $\zeta$, which is wrong). The absolute baseline is not calibrated
> (engine-spec §3: needs $X=10^5$ **with the validated archimedean+polar normalization**). So **the Carleson
> constant of $\nu_\zeta$ vs $\nu_{L_{\mathrm{DH}}}$ cannot be measured reliably here** — Phase 3 needs the
> validated engine. The structural/analytic program (P9, P10, T1–T4) is unaffected.

---

## 1. The Carleson constant: the gate fails (honest)

$C(L)=\lambda_{\max}(A_\infty^{-1/2}P(L)A_\infty^{-1/2})$; $C\le1\iff$ local positivity (Thm T4-I). Result
(stable across $X\in\{10^3,2\!\cdot\!10^4,10^5\}$ — the prime tail is already negligible, so the issue is
*normalization*, not truncation):

| $L$ | $C(L)$ | $\lambda_{\min}(A_\infty-P)$ | gate |
|---|---|---|---|
| $\zeta$ | $1.98$ | $-1.95$ | **FAIL** (RH-true must give $C\le1$) |
| $L(\chi_4\bmod5)$ | $0.11$ | $+3.19$ | pass |

**Diagnosis.** $C(\zeta)\approx1.98\approx2\times$ the positivity threshold, while the mean archimedean weight
$\bar\Omega\approx1.986$: the prime block $P$ is $\approx2\times$ too large relative to $A_\infty$ in my
normalization — almost certainly the standard **factor-2 convention** in the explicit formula (the prime term
$2\sum_n\Lambda_L(n)/\sqrt n\,\widehat g(\log n)$ vs $\sum$, or a missing $2\,\mathrm{Re}$ in the archimedean
block). With the correct factor, $\zeta$ would sit at $C\approx1$ (the floor, consistent with engine-spec §4's
"RH-true controls at the floor"). **But I will not fudge the constant**: fixing it rigorously, and validating
against P7's reference behavior, is exactly the Phase-3 engineering task. The huge apparent discriminant
$|C(\zeta)-C(\chi_4)|\approx1.87$ is **confounded by the un-calibrated baseline** (different $\Gamma$-factors
$a=\tfrac14$ vs $\tfrac34$ give different baselines); it is **not** a clean measurement.

> **Honest conclusion (Carleson).** The Carleson-constant measurement — the sharp Phase-3 target — is
> **blocked** on reproducing P7's validated engine (engine-spec §3: $X=10^5$, full archimedean+polar, the
> validated normalization), and additionally on handling $L_{\mathrm{DH}}$'s **lack of an Euler product** (its
> arithmetic side is not a clean $\sum\Lambda_L(n)n^{-s}$). This is real engineering, best done with P7's
> actual code; it is not reliably reproducible self-contained in this session.

## 2. The band test: T3.4 confirmed (basis artifact)

The anatomy density $|\widehat{u_0}(\log p)|^2$ (Hermite basis, $J=12$, $\sigma=1$, $T_0=46.13$):
```
 log p   p    density
  1.6    5    1.1e-02  #
  2.8   17    3.3e-02  ###
  2.9   19    3.9e-02  ###
  3.6   37    1.8e-01  #################
  3.8   43    3.4e-01  ################################
  4.0   53    4.9e-01  ###############################################
  4.1   59    5.1e-01  ##################################################   <- peak
  4.2   67    4.9e-01  ###############################################
  4.5   89    3.0e-01  #############################
```
The density **rises monotonically to the Hermite turning-point edge** ($\sqrt{2J}/\sigma\approx4.9$) and peaks
at $p\approx59$ ($\log p\approx4.1$). This is the **basis envelope**, not arithmetic structure — confirming
T3.4 cleanly (and showing the earlier "band at 3.3–3.7" was simply the rising edge for smaller $J$).

> **Honest conclusion (band).** The observed concentration is a **Hermite-basis artifact**. Deciding whether
> any *arithmetic* concentration exists requires re-running in the **Slepian (flat-box) basis** — the genuine
> band test of Phase 2 §A, which needs the prolate construction (and ideally the validated engine).

## 3. Net for Phase 3

- **Confirmed:** the band is basis-enveloped (T3.4) — a clean, honest negative that *validates* the earlier
  demotion. The Slepian basis is genuinely required to look for arithmetic structure.
- **Blocked:** the Carleson-constant measurement (the sharp target) needs the validated engine + the
  $L_{\mathrm{DH}}$ no-Euler-product handling. My self-contained build fails the $\zeta$ gate by an apparent
  factor-2 normalization; calibrating and validating it is the Phase-3 engineering task.
- **Unaffected:** the analytic results — P9 (stability, RH-independent), P10 (anatomy, Carleson reformulation,
  Conjecture B2), T1–T4 — stand on their own; none depended on this measurement.

**Recommendation.** Phase 3, done faithfully, requires **P7's validated engine** (Colab/v8 per the index) or a
careful engine-spec §3 reimplementation validated against the reference behavior ($\zeta$ at the floor,
$L_{\mathrm{DH}}\ \lambda_{\min}\approx-9\times10^4$). Until then, the Carleson/discriminant numbers are **not**
trustworthy and should not be reported as measurements. The honest state: **the analytic program is banked
(P9/P10); the numerical confirmation of the Carleson discriminant is the open Phase-3 engineering task.**

---

### Status
- Band test (basis artifact, T3.4 confirmed) — ✅ done; honest negative.
- Carleson constant measurement — ⛔ blocked (validated engine + $L_{\mathrm{DH}}$ Euler-product handling).
- Slepian band test (the real one) — ⬜ needs prolate basis.
- Conjecture B2 numerical test — ⬜ needs the engine.
- **Decision point for the user:** obtain P7's validated engine code, or invest the engine-spec §3
  reimplementation, before trusting any Phase-3 measurement.
