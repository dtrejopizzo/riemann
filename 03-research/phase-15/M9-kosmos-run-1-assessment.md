# Phase 15 · M9 — Assessment of the first Lise Science discovery run (the SURF / K_geom discovery report)

**Author: David Alejandro Trejo Pizzo · 2026-06-06.**
The guarded Lise Science prompt (attack G1–G4 / construct $\mathcal K_{\mathrm{geom}}$, with anti-fabrication gates)
returned a four-discovery report. **Headline: the run did NOT fabricate a proof — the gates held.** It returned three
honest negatives (one per route) that converge with our M5/M6/M8, plus one genuinely new RH-independent constraint.
This is the best realistic outcome short of a proof, and it sharpens the map. Below, the per-discovery audit.

---

## Discovery 1 (Route C, NCG/scaling) — confirms + sharpens M5/M8
**Verdict: correct, consistent, with new specifics.** Re-derives our Lefschetz dichotomy from the NCG side:
noncompact scaling ⇒ regularization cutoffs ⇒ no compact integer-graded structure; bounded $L$ with $[T,L]=cL$
obstructed by LI; positivity $\equiv$ RH; no intersection theory on the "square" for $[\Delta]$.
**New, valuable specifics:** (a) on each periodic orbit $C_p$, Riemann–Roch gives $\chi(D)=\deg(D)\in\mathbb R$
(arbitrary real) ⇒ no integer Euler characteristic ⇒ no integer grading — a concrete mechanism for our M5 continuum
horn; (b) **unbounded** $L$ would need infinitely many *repeated gaps* $c$, which the GUE pair statistics of the first
$10^6$ zeros (no spikes, no excess 3-term APs) empirically exclude — strengthens M4.2a beyond the conjectural LI.

## Discovery 2 (Route A, Arakelov / $\lambda$-rings) — genuine partial progress, but the "passed gates" are on the wrong object
**Verdict: the most valuable discovery, and the one needing the sharpest caveat.** Genuine, non-circular moves:
- $L=$ cup with an arithmetic $\widehat c_1$ (ample hermitian bundle), $Q=$ arithmetic intersection $+$ degree,
  positivity from the **proven** arithmetic Hodge index (Faltings–Hriljac / Yuan–Zhang). This is a *geometric* $L$,
  **not** a spectral reconstruction — so it does **not** commit our F2/F4 circularity. Good.
- **Independence via metric variation** (new idea): $\widehat c_1$ depends on the metric through a Green's-function
  term; varying $m$ deforms $L\to L_m$ while $T$ (fixed by $\{\gamma_\rho\}$) does not ⇒ evidence $L\notin W^*(T)$.
- $\lambda$-ring Adams operations $\psi^n$ give an intrinsic integer grading; $L$ shifts Adams weight by $+1$.

**The caveat (= our Attempt 6, which the run under-emphasizes).** These gates are passed for the **Arakelov / height
structure** ($\widehat{\mathrm{Pic}}^0$, Néron–Tate), **not** for the zero-carrying cohomology $\Pi^\perp$. The
arithmetic Hodge index gives positivity of the **height** pairing, not of the Weil form $Q$ on the zeros; and the
metric-variation argument lives on an Arakelov variety where the zero-Frobenius $T$ does not act — so "$L\notin
W^*(T)$" is not yet posed on the right object. This run's own open items are exactly the bridge: the $\mathfrak{sl}_2$
$H$ aligns with **cohomological degree, not Adams weight**; the lowering $\Lambda$ exists geometrically only for
abelian varieties (Fourier–Mukai); **the absolute surface is unbuilt**. So Discovery 2 is real progress that lands
**precisely on Attempt 6 (heights↔zeros) + SURF**, not on a crossing. Honest status: a clean *blueprint* whose two
"passed" gates become real only once the surface realizes $\Pi^\perp$ as the relevant cohomology.

## Discovery 3 (Route B, prismatic) — confirms M6 verbatim
**Verdict: correct, equals our M6.** Prismatic/TC packages local Frobenius $\{\varphi_p\}$ into a monoid action but
yields **no single global endomorphism with spectrum $=\{\gamma_\rho\}$**; global Sen generator fails (prismatic
Frobenius $\to$ local $L$-factors; Sen $\to$ Hodge–Tate weights — division of labor, not interchangeable = our M6
"local Satake, not global zeros"). Missing: hermitian pairing, $*$-operator, regularized $\zeta(s)$ determinant.
Leaves G1, G3, G4 unaddressed. New detail: Nygaard filtration is the best weight-filtration candidate but
unidentified with a Deninger weight theory.

## Discovery 4 (long-range statistics) — genuinely NEW, RH-independent design constraint
**Verdict: correct and useful.** The Dyson–Mehta rigidity $\Delta_3(L)$ of the first $10^6$ zeros **saturates** at a
plateau $\approx0.1908$ (departing from GUE's logarithmic growth). Berry's semiclassical prime-orbit formula
$\Sigma^2_\infty=\pi^{-2}[\ln\ln(E/2\pi)+1.4009]$ gives $\Delta_3^\infty\approx\Sigma^2_\infty/2$; at $E\approx6\times
10^5$ this is $0.1946$ (**self-consistency checked here: $\ln\ln(E/2\pi)=2.4395$, $\Sigma^2=0.3891$, $\Delta_3=0.1946$**),
$\approx2\%$ above empirical, driven by the prime-power series $\sum_{p,r}1/(r^2p^r)$. This is a quantitative,
falsifiable **design constraint**: any candidate $\mathcal K_{\mathrm{geom}}$ must reproduce the plateau and its
$\ln\ln E$ scaling without circularly encoding the zeros. RH-independent (a fingerprint, like P14/P9), not itself on
the proof path, but a real validation target for any future surface.

---

## Bottom line
- **No proof, no crossing** — and, crucially, **no fabrication**: the gates converted a "prove RH" request into honest
  research output. The prompt design worked.
- **Convergent confirmation:** the run independently re-derived our three-route obstruction (A = Arakelov controls
  heights not zeros + unbuilt surface = Attempt 6/SURF; B = prismatic is local not global = M6; C = noncompact, no
  integer grading = M5/M8).
- **The live direction is Route A (Arakelov).** It is the only route with a *geometric, non-circular* $L$ and a
  *proven* positivity theorem; the precise remaining gap is the standing wall — **build the absolute surface so the
  Arakelov Hodge index lands on the zero cohomology $\Pi^\perp$, not on heights** (Attempt 6). Everything else
  (independence, integer grading, positivity) has a candidate; the surface does not.
- **One new asset:** the $\Delta_3$ plateau ($0.1908$, $\ln\ln E$ scaling, prime-power series) as an RH-independent
  design constraint on any $\mathcal K_{\mathrm{geom}}$.
- **Next probe, if continued:** a Route-A-only deep prompt — *construct the absolute surface $S$ (or a higher-dim
  arithmetic variety) whose Arakelov $H^1$ carries the $\zeta$-zeros as Frobenius eigenvalues (not heights)*, i.e.
  attack the heights↔zeros realization directly, with the $\Delta_3$ constraint as an acceptance test.
