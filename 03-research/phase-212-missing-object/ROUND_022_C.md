# Round 22, memo C — «First contact» standpoint: inventory of the null vector and cross-check of two ideas

Notation of round 7: `a_T(F) = Arch(F) − Σ_n v_n c_F(log n)` on `P_T = {∫F e^{±t/2} = 0}`, `λ_A(T)` the primitive
bottom, `W_*` the global form, `Π_T(M∗φ)` the near-radical family of `ROUND_021_A` §1.

## Four-point filter (cross-check first)

1. **Antecedents, read in primary sources.**
   - P46 §`sec:firstcontact`: `lem:firstcontact` (l.6591), weak equation `eq:localweak` (l.≈6620),
     `prob:annihilate` (l.6887), `prop:annihilate-equiv` (l.6914: the problem IS the goal).
   - `phase-197-*/BARRIER_W_001.md` Theorems W1, W2, W3; in particular **W3(b)**: «to bring a zero crossing to
     codimension ≥ 2 one needs an extra condition `L(h)=0` on every kernel vector, independent of the
     Euler–Lagrange equation; candidates reviewed […]; no independent condition exists in 𝒮».
   - `phase-124-direct-first-contact/`: P124_004 §§4–6 (window variation: no shape derivative; births
     without rate or sign), P124_008 (null regularity only `H^s`, `s<½`), P124_011 §6 (collar = cross block
     `ρ_{+,T}`; obstruction `Π_{ker L_T}ρ_{+,T}`; range condition `ρ ∈ Ran L_T^{1/2}` not supplied),
     P124_012 (reduction to `𝒞_T(F) ≤ 0`, without sign).
   - `phase-162-*/R162_502_MULTIPLICATIVE_EQUIVARIANCE.md` A5 (envelope lemma), `R162_590` §3(H).
   - Phase 114: `114_d_53_THRESHOLD_FLOW_*` (Feynman–Hellmann at thresholds: free orientation),
     `114_d_134_CENTERED_SCREW_BIRMAN_SCHWINGER_AUDIT.md` (0.4): `‖𝒲_T𝓡_T^{−1/2}‖ ≤ 1 ⟺` goal.
   - Master index: «Annihilation of Gamma moments at first contact» (OPEN = Gate 1 = REF-D), «P124 direct first
     contact» (NO-GO), «Finite radical detection» R161_046–051 (DEAD), «Thm P lock» R162_1603 (DEAD),
     «Kadison equality» R180 (DEAD), D-E/P122.028 (OPEN, constant nonzero flux).
2. **What the assignment proposes as new.** (i) the conditions `a_{T_*}(F_*, Π_{T_*}(M∗φ)) = 0`, read through the
   radical identity as tail functionals; (ii) a terminal-layer positivity.
3. **Result of the cross-check.** (i) is **contained in the Euler–Lagrange equation** (§2, PROVED, elementary) and the
   independence question is exactly W3(b) of BARRIER_W_001, already closed. (ii) repeats P124_004 §5–6 /
   P124_011 and is blind to the class (§3). **Repetition in both cases.**
4. **Global connection.** None: `prop:annihilate-equiv` makes any exclusion of first contact a
   reformulation of the goal unless one side has an independent proof (F5); neither of the two provides one.

## §1 Table: what is known about the null vector `F_*`

| Property | Status | Source |
|---|---|---|
| Existence of `T_*>½log5` and `F_*≠0` in `ker H_{T_*}`, `H_{T_*} ≥ 0` | PROVED (conditional on the goal failing) | P46 `lem:firstcontact`, `lem:contA`, `lem:monoT` |
| Definite parity `JF_* = ±F_*` | PROVED | same |
| Convex envelope of the support of length exactly `2T_*` | PROVED (blind to the weight: `c_F` and the constraints are translation covariant; if it fitted in a shorter interval, translated it would give `λ_A(T)≤0` with `T<T_*`) | R162_502 A5 |
| Euler–Lagrange equation: `a_{T_*}(F_*,G) = ⟨r,G⟩` ∀G in the domain, `r = α e^{t/2}+β e^{−t/2}` unique (the two Lagrange multipliers) | PROVED | P46 `eq:localweak` |
| Whole-line form: `(L+R_T)u = f_T`, `L = log⟨D⟩`, `u = E_TF_*` | PROVED | P124_008 (1.1)–(1.2) |
| Regularity: `E_TF_* ∈ H^s`, `0≤s<½`; no gain to `H^{1/2}` from the equation alone (mapping countermodel) | PROVED / NO-GO | P121, P124_008 |
| Boundary at `±T_*`: a nonzero jump in `H^{1/2}` is forbidden by Lions–Magenes; assuming `H^{1/2}` kills the Tate coefficient (circular) | PROVED (conditional, circular) | P122.019/029, P124_008 §4 |
| Multiplicity: `dim ker H_{T_*} < ∞`; 1 «generically» | PROVED (finiteness) / ARGUED (simplicity: vNW, no proof for the concrete family) | `lem:compact`; W3(a),(c) |
| Past `T_*`: `n_−` does not decrease, all crossings downward; jump `1 ≤ n_−(T_*+0) ≤ dim ker H_{T_*}` | PROVED (≥1, monotonicity) / ARGUED (upper bound by semicontinuity; `lem:contA` gives only continuity of the bottom) | W1 |
| One-sided tangential touch | PROVED | W1, W3(c) |
| Hadamard-type formula `dλ_A/dT` in boundary values | **NOT proved**: the Euler part has no shape derivative in the domain of `F_*` (packet model (4.2)); births `= o(1)` without rate; with `H^1` assumed, (4.3) would give the derivative, but it is not available | P124_004 §§4–5 |
| First variation at a threshold `p^k` | no uniform sign: `λ'(s) = ⟨f,W_af⟩`, `W_a = c_a(S_a+S_{−a})` indefinite | D.53 §2 (note D.134 is something else: screw factorization + BS, (0.4) ⟺ goal) |
| Relation with the near-null block | `a(F_*,Π(M∗φ)) = 0` ∀φ, by EL | §2 below |
| Collar | `c=0` on a branch ⟺ `Π_{ker L_T}ρ_{+,T} = 0`; ⟸ `ρ_{+,T} ∈ Ran L_T^{1/2}`, not proved | P124_011 §6 |
| Seam scalar | `L_TF=0 ⇒ 𝒞_T(F) ≤ 0` would suffice; not proved | P124_012 |

**Contradiction routes attempted and how they ended.** Window variation / virial (P124_004, P124_007):
NO-GO by regularity and free sign. Schur/Douglas collar (P124_011): exact reduction, range condition open =
REF. Causal seam (P124_012): scalar reduction without sign. Finite radical detection (R161_046–051): 3-dim unitary
countermodel, REF-D. Thm P lock (R162_1603): = Gate 1. Kadison (R180): «first contact forces equality» not
proved. OS-2 parity (R166_202): empty or REF-D. Threshold flow (D.53): no orientation. Index invariants
(W1–W3): `n_−` is the only one and it is the goal. Annihilation of Gamma moments (`prob:annihilate`): equivalent to the
goal (`prop:annihilate-equiv`), OPEN as a route. Tangency at `c_*` (phase 211 ROUND_003_A): structural,
without sign.

## §2 Idea (i): the tail conditions

**Lemma 2.1 (PROVED, elementary).** For every admissible `φ`, `Π_{T_*}(φ) ∈ P_{T_*}` and is in the form domain,
hence by `eq:localweak`, `a_{T_*}(F_*, Π_{T_*}φ) = ⟨r, Π_{T_*}φ⟩ = 0` (since `r ⟂ P_{T_*}`). With the radical
identity of ROUND_021_A (1.1), polarized, this reads `W_*(F_*, R̃_φ) = 0`, `R̃_φ = R_φ + A(R_φ)u_+ + B(R_φ)u_−`.

*Consequence.* The `≍ e^{2T_*}` conditions «tail functional_φ(F_*) = 0» are **special cases** of the
Euler–Lagrange equation with `G = Π_{T_*}φ`; they overdetermine nothing. The requested count: the set of solutions
of EL with `F ∈ P_{T_*}` is `ker H_{T_*}` (finite dimension; the equation is Fredholm with compact resolvent,
not a delay equation with solution space fixed by initial conditions); the problem without the
constraint `F∈P` adds at most the 2 parameters `(α,β)`. The tail conditions are `≤` «all `G`»,
so the number of **new** independent conditions is 0. The question «is there a linear condition on the
kernel independent of EL?» is literally W3(b), closed in 𝒮 (BARRIER_W_001 §4).

Reading in annihilator form: `F_*` belongs to the `a`-orthogonal complement of the near-null block, which has
finite codimension `≍ e^{2T}` and is huge; being there is not contradictory. Turning `W_*(F_*, R̃_φ) = 0` into
`F_* = 0` would require Cauchy–Schwarz with `W_* ≥ 0` (the goal: circular, F5) or a uniqueness theorem of the type
«the `W_*`-annihilator of `{R̃_φ}` in `P_T` is zero», which is false by the above.

**Controls.** With `2Λ`, deletion of a prime power or a Beurling weight, `M∗φ` stops being in the radical and the
step «radical identity» falls (the functional stops being a tail functional); but Lemma 2.1 still holds for their null
vectors, which exist. That is: the part that survives is blind (it holds in the controls), and the part that depends on the
weight provides no new condition.

## §3 Idea (ii): terminal-layer positivity

What is true (ARGUED, from the shape of `W`): since `G′ = K ~ 1/u` at `0`, `π − G(T−t) ~ log(1/(T−t))`, and `Arch`
contains a positive logarithmic weight in the layers. With the prime term bounded in `L²` and `Arch` bounded
below, one obtains a Gårding-type inequality

    a_T(F) + C_T‖F‖² ≥ c·log(1/δ)·‖F·1_{T−δ<|t|<T}‖².

At the null vector it gives `‖F_*‖²_{layer δ} ≤ C_T/log(1/δ)`: decay of the layer mass, compatible with
`H^s`, `s<½` (mass `O(δ^{2s})`). To contradict first contact one would need a quantitative **lower bound**
on the layer mass of `F_*`, and minimality gives only A5 (the envelope touches the endpoints: positive
mass in every layer, not large). The quantitative version —comparing `a(F_*) = 0` with `a(χF_*) ≥ λ_A(T_*−δ)‖·‖²`—
is exactly the window variation of P124_004 (collar cross terms without rate or sign) and the cross
block of P124_011.

**Inequality that would contradict first contact** (precise statement): there exist `c(T)>0` and `δ>0` with
`a_T(F) ≥ c(T)‖F 1_{layer δ}‖² − (something vanishing on ker H_T)` for `F ∈ P_T`, together with
`F ∈ ker H_T, F≠0 ⇒ ‖F 1_{layer δ}‖ ≥ κ‖F‖`. The first half is blind (it uses only `W`, it holds in the three controls);
the second is quantitative minimality, which **fails in the controls**: there are first contacts there with
null vectors of envelope `2T_*` (A5 is blind to the weight), so the pair of inequalities would prove something false in
the controls if it does not use the weight, and there is no step that uses it. Lemma T (F1): fails.

The term `(2T+O(1))‖(1−χ)(M∗φ)‖²` of ROUND_021_A is a defect of the near-null block, not a lower bound on
general vectors: it does not transfer to `F_*`, which is `a`-orthogonal to the block (Lemma 2.1).

## §4 Verdict

**REPETITION.** (i) PROVED trivially: the tail conditions are instances of EL; the sought independence is
W3(b) (BARRIER_W_001), closed. (ii) repeats P124_004 §§5–6 / P124_011 §6; the positive part is archimedean and
blind, the missing part is quantitative minimality, false in the controls. No new intermediate result:
the layer-mass decay is a direct consequence of P124_008 and is not recorded as new.
I find no defensible different idea within this standpoint: every contradiction from `F_*` goes through
`prop:annihilate-equiv`, and the proved properties of `F_*` (table §1) are, except for the identities of P46
§`sec:firstcontact`, valid on all of 𝒮. **Next operation: none in this standpoint.**
