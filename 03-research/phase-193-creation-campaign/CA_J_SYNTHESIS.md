# CA_J_SYNTHESIS — Front J (correlation inequalities, rigorous statistical mechanics), phase 193

 Pen and paper; no numerics. **No sign contact. No negative value for ζ. No clause of (R) moved.**
Memos: CA_J_000 (12 seeds, screens, Lemmas J0/J0′), CA_J_001 (lattice RP / chessboard), CA_J_002 (GKS frustration, FKG on the divisor lattice).
Corpus check: 0 prior hits for FKG / Griffiths / chessboard / Brascamp / Prékopa (grep).

## Verdicts
| seed | verdict | killing clause |
|---|---|---|
| J1 GKS I/II | NO-GO (PROVED) | 002 Thm 1.3: 𝔸_M frustrated in both readings (additive triangles; +/· cycle m→…→2m→m) |
| J2 FKG/Harris on (ℕ,\|) | NO-GO as sign step | 002 Prop 2.1/Cor 2.2: Euler tests = FKG-equality class; Prop 2.3: no positive FKG measure (signed / B″ / REF-D) |
| J3 Ginibre, GHS, Lebowitz, Newman | DISCARD | need J1's ferromagnetic sign |
| J4 Brascamp–Lieb variance | DISCARD | input Hess V ⪰ 0 is the target (REF-D) |
| J4′ geometric BL / Lieb Gaussians / BCCT | DISCARD | dimension data FE-/Beurling-generic; "Gaussians suffice" = CA_E_001 Thm 1 |
| J5 Prékopa–Leindler / log-concavity | DISCARD (retry) | Pólya-frequency route (phase 135, G7) |
| J6 chessboard / lattice RP per prime | NO-GO (PROVED) | 001 Thm 1 (fails on short windows, explicit at p=2), Thm 2 (RP_p ⟺ ν on (π/log p)ℤ), Cor 3 (two primes ⇒ 𝖡 constant, false) |
| J7 Gaussian domination / infrared bounds | DISCARD | needs RP ⇒ J6 |
| J8 strong Rayleigh / negative dependence | DISCARD | Lee–Yang family (L32) |
| J9 FK random cluster | DISCARD | needs ferromagnetic weights ⇒ J1 |
| J10 Dobrushin / cluster expansion | DISCARD | perturbative, (R)(3), cannot see [crit] M^{−3} |
| J11 Holley, J12 log-supermodular kernel | folded into J2 | linear in Λ and local (Prop 2.4, ARGUED); φ has negative values |

## PROVED facts (usable elsewhere)
J-0. For |d| ≥ 2T₀: α(d) = −½∫K(u)[c₀(d−u)+c₀(d+u)]du, |α(d)| ≤ 2T₀K(|d|−2T₀). For 2T₀ ≤ 0.1: 𝖡(log 2) < −0.27, 𝖡(log 4) < −0.23
     (kernel values at nonzero shift, not form values).
J-RP. Under the premise, site-RP of φ in prime p ⟺ supp ν ⊂ (π/log p)ℤ ⟺ 𝖡 is 2log p-periodic (bond: (2π/log p)ℤ). RP in two
     primes ⇒ 𝖡 constant (false, CITED explicit formula + Hardy). One prime: fails for p ≤ 7 at every T₀ (CITED γ₁ digits).
J-σ. Any multiplicative symmetry σ of G (prime transposition) compatible with φ forces μ_φ onto a discrete set (Prop 5): monoid
     symmetries do not preserve the archimedean line.
J-F. 𝔸_M has no ferromagnetic ±1 gauge: frustrated cycle = additive path + multiplicative closing edge.
J-L. Positive log-modular functions on divisor boxes = Euler-product tests; the decisive class of CA_E_001 Thm 1 is the FKG-equality class.

## Proposed YES→NO moves
- "ferromagnetic correlation inequalities (GKS, GHS, Lebowitz, FK) force the sign on the integer lattice" → NO (frustration, PROVED).
- "chessboard / reflection positivity in prime coordinates" → NO (RP_p ⟺ lattice support of ν; false, PROVED).
- "FKG on the distributive divisor lattice" → NO (blind on the decisive class; no positive measure).
- "Brascamp–Lieb / Prékopa–Leindler / log-concavity" → NO (REF-D or Pólya retry).

## +/· reading (PRINCIPIO RECTOR)
In this area + and · meet in two exact places, and both are obstructions: (1) monoid reflections and symmetries of G do not preserve
ι(ℝ), where the Bochner measure lives (J-RP, J-σ); (2) the sign pattern of 𝔸_M is frustrated, with positive additive near-diagonal
edges and negative multiplicative Euler-atom edges (J-F). Correlation-inequality machinery needs exactly the compatibility these
facts deny. No object here supplies a non-linear input that is neither the minimizer (REF-D) nor comb-only (O7). Area exhausted; front J stops.
