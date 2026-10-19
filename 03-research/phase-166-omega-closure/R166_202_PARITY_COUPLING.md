# R166_202 — Parity coupling at the first contact (OS-2, cells 6C / 7A)

*pure math, no numerics. Nothing else edited. No label of record moves.*
*Corpus checked before building: R163_401 §1–§3 (Lemma 3.1 conventions), R163_501 (witness per parity), R162_2401
(Prop P2, identity (v)), R162_2902 (Lemma 1: mixed-parity terms vanish; parity splitting = R155_026 §3 / D.56),
R162_2300 grid ("OS-2", parts 7/16), R165_201/202, R166_190.*

**Status.** Mechanism "parity coupling" **DEAD (E1 + vacuous)**. Proved: sector orthogonality (record, re-derived),
the cross identity is vacuous *term by term* (new form), a parity sum rule with one inequality
λ_e(T)+λ_o(T) ≤ 2λ^W_{T/2}. OPEN: T_e = T_o (not decided; no ordering provable from the record). The brief's premise
"the lattice extremal is odd" refers to the *local* parity about γ_q, not the global sector; in the model the two
global sectors are degenerate (T_e = T_o). Row D stays OPEN; (★_cell) stays OPEN.

Notation as R163_401 §1. For real F put F = F_e + F_o (even/odd parts). Sector bottoms
λ_e(T) = inf W_T on even L²(I_T)∩𝒟_T, λ_o(T) likewise; T_e, T_o their first contacts (inf{λ ≤ 0}); G as in §3
(G = F̂ for even F, G = −iF̂ for odd F; both real on ℝ, Lemma 3.1).

## 1. Sector orthogonality. PROVED (re-derivation of R155_026 §3 / R162_2902 Lemma 1)

**Prop 1.** For real F_e even, F_o odd in 𝒟_T: W_T(F_e,F_o) = 0. Hence W_T = W_T^e ⊕ W_T^o,
λ^W_T = min(λ_e,λ_o), T_c = min(T_e,T_o), and E_c = (E_c∩even) ⊕ (E_c∩odd).

*Proof.* Archimedean/prime part: 𝔞_T(F,H) = (2π)⁻¹∫σ_T F̂ conj Ĥ; σ_T is even, F̂_e is even real, F̂_o = i·(odd real);
the integrand is odd, integral 0. Pole part (hermitian polarisation of 2Re A B̄): A(F)conj B(H) + B(F)conj A(H). For
even F: A(F)=B(F)=:a; for odd H: A(H) = −B(H) =: b (t ↦ −t swaps e^{±t/2}). So the sum is a(−b̄)+a b̄ = 0. ∎
Also W^e = 𝔞 + 2A², W^o = 𝔞 − 2A² (A real): the pole term is positive on the even sector, negative on the odd.

## 2. The cross identity is vacuous term by term. PROVED

**Thm 2.** Let Z be any multiset of points in the strip |Im t|<½ symmetric under t ↦ −t and t ↦ t̄ (any L with a
functional equation of ζ-type: ζ, M_m, f_t, f_χ, P_{a,c}). For every odd entire φ, the zero sum Σ_{t∈Z} φ(t) vanishes
*summand-pairwise*: the terms at t and −t cancel. In particular, for parity witnesses,
(1.1) applied to the pair gives W(F_e,F_o) = Σ_ρ G_e(t_ρ)·(±i)G_o(t_ρ) and G_eG_o is odd, so every on-line pair
{γ,−γ} and every quartet {t,t̄,−t,−t̄} contributes exactly 0.

*Proof.* G_eG_o is odd (even × odd); Z = −Z with multiplicity. ∎

**Consequence.** There is no "third phase relation": the would-be quartet term Re[G_e(t_q)conj G_o(t̄_q)] appears with
its partner at −t_q with the opposite sign and cancels identically, for every function with the functional equation.
The cross identity carries no information about ζ, about the quartet phases, or about ω(E). (The brief's suggested
Σ_on G_eG_o·sign + Σ_q(cross) = 0 is 0 = 0 summand by summand.)

The product G_eG_o (real-rooted, odd, type 2T) is a test of type 2T: R166_103(α) (window data / f_t) applies; its
zero sum is again vacuous by Thm 2. The quotient tests G_eG_o/(z−x) need a common node; R163_501 gives none, and any
such test is a single-sector test of type ≤ 2T (E1, R162 "Thm Q" lesson).

## 3. Parity sum rule and one inequality. PROVED

For F_+ ∈ L²(0,T) let F^ev, F^odd be its even and odd extensions (‖F^ev‖² = ‖F^odd‖² = 2‖F_+‖²), and
Φ(s) := F_+(s+T/2) ∈ L²(−T/2,T/2).

**Lemma 3 (translation invariance).** W is invariant under translation of the test: 𝔞 depends on c_F only; under
F ↦ F(·−h), A ↦ e^{h/2}A, B ↦ e^{−h/2}B, so A·B̄ is unchanged. Hence W_T(F_+) = W_{T/2}(Φ). PROVED.

**Thm 3 (sum rule).** W_T(F^ev) + W_T(F^odd) = 4 W_{T/2}(Φ). (Identity (v) of R162_2401 summed over parities.)
*Proof.* F^ev = F_+ + F_−, F^odd = F_+ − F_− (F_−(s)=F_+(−s)); W(F_±) equal by reflection invariance of W
(c_{F_−}=c_{F_+}, A↔B). Expand; the cross terms cancel; Lemma 3. ∎

**Cor 3.1 (one inequality).** For every T: λ_e(T) + λ_o(T) ≤ 2 λ^W_{T/2}.
*Proof.* 4W_{T/2}(Φ) ≥ (λ_e+λ_o)·2‖Φ‖² for all Φ; take inf. ∎
**Cor 3.2.** For T < 2T_c (in particular at T_c), no F_+ has both extensions in the kernel; if F^odd ∈ E_c then
W(F^ev) = 4W_{T_c/2}(Φ) ≥ 4λ_{T_c/2}‖Φ‖² > 0, and symmetrically. (Matches R162_2401 line 139 for even witnesses.)

**Wall.** Thm 3 is (1.1) applied to F_+ (zero side: W(F^ev)+W(F^odd) = 4Σ_ρ F̂_+(t_ρ)conj F̂_+(t̄_ρ)); it holds for M_m,
f_t, f_χ with their own forms. **E1.** Cor 3.1 relates sector bottoms to the half window; it does not order T_e, T_o.

## 4. T_e versus T_o

- **Not decided (OPEN).** The record gives no ordering. The only parity-asymmetric ingredient is the rank-one pole
  term ±2A² (Prop 1), which makes W^e ≥ 𝔞 ≥ W^o on the same sector-free function space — but 𝔞 is restricted to
  different subspaces, so no inequality between λ_e and λ_o follows. On primitive tests (A=0) both sectors are 𝔞, so
  any splitting T_e ≠ T_o is carried by the full non-primitive form and the cross-height terms.
- **Lattice model (Lemma 4.10 of R163_401). PROVED (in the model):** the model localises F̂ = G(z−γ) ± G(−z−γ) and drops
  cross terms; the ± is the *global* parity and it enters only cross terms. So both global sectors have the same
  model form and **T_e = T_o = T*** in the model; the extremal "odd, node at the cone vertex" is local parity of G about
  γ (a property shared by the even and odd global witnesses G(z−γ) ± G(−z−γ), whose node sets near ±γ agree).
  Hence the question "is the even sector positive at the odd contact" has answer **no, both contact** in the model;
  the model is exactly degenerate and does not separate parities.
- **ζ:** the splitting T_e − T_o is controlled by cross-height terms (size governed by |G(2γ_q)|, i.e. by the decay of
  the localised witness at distance 2γ_q) plus the pole term ±2A² with A = F̂(−i/2) ≈ G(−γ−i/2) ± G(γ−i/2), likewise
  cross-height; both are window data (f_t carries the same). HEURISTIC: generically T_e ≠ T_o by an exponentially small
  amount; no proof either way. Neither outcome feeds a sign: if T_e ≠ T_o the witness lives in one sector and the
  argument is the single-sector (1.1) of R163_401 (already E1/(★_cell)); if T_e = T_o, Thm 2 shows the coupling is void
  and Thm 3 is E1.
- **M_m / f_t:** both have the FE symmetry, so Prop 1, Thm 2 and Thm 3 hold for them verbatim; each has a contact
  in min(T_e,T_o) with witness in the contacting sector (R163_501 applies unchanged). Any argument from the parity
  triple is satisfied by their configurations. An argument *requiring both* sectors to contact is not killed by M_m
  directly, but it needs the hypothesis T_e = T_o, which is unproved for ζ, and under that hypothesis the extra input is
  Thm 2 (empty). So the escape is void, not merely unproved.

## 5. Verdict on the brief's questions

1. T_e = T_o: **OPEN**; one inequality PROVED (Cor 3.1); model degenerate (T_e = T_o, PROVED in the model).
2. Phase conventions: with G real on ℝ in both parities (Lemma 3.1), quartet negativity is cos2Θ < 0, i.e.
   arg G(t_q) ∈ (π/4,3π/4) mod π, **the same condition in both sectors** (the i of the odd case is absorbed in G, and
   F̂F̂^# = G² in both). Even G: G(0) ≠ 0 generically (m = 0 or even); odd G: m odd. Near γ_q ≫ 1 the factor z^m
   shifts Θ by m·arctan(δ/γ_q) = O(δ/γ_q): parity does not move the phase at height (PROVED from Lemma 3.3).
3. Cross identity: **PROVED vacuous term by term** (Thm 2). The parity triple = even balance ⊕ odd balance; it is
   not overdetermined.
4. Constraint beyond (1.1) on single tests: **none** (Thm 2 + Thm 3 = (1.1) for F_+). OS-2 closed negative.

## Ledger
| item | label |
|---|---|
| Prop 1 sector orthogonality, λ^W = min(λ_e,λ_o), T_c = min | PROVED (record R155_026 §3, re-derived) |
| W^e = 𝔞+2A², W^o = 𝔞−2A² | PROVED |
| Thm 2 cross identity vacuous summand-pairwise, any FE-symmetric zero set | PROVED |
| Lemma 3 translation invariance of W | PROVED |
| Thm 3 sum rule W(F^ev)+W(F^odd)=4W_{T/2}(Φ) | PROVED (record identity (v), R162_2401, summed) |
| Cor 3.1 λ_e+λ_o ≤ 2λ_{T/2}; Cor 3.2 | PROVED |
| T_e vs T_o ordering / equality for ζ | OPEN |
| model: T_e = T_o (global parity only in dropped cross terms) | PROVED (in the model) |
| generic T_e ≠ T_o, exponentially small split | HEURISTIC |
| parity moves quartet phase by O(δ/γ_q) only | PROVED |
| parity coupling as a route to (★_cell) | DEAD: E1 (Thm 3) + vacuous (Thm 2) |

## Grid cells
- **6C (OS-2, parity of the witness):** CLOSED negative. Parity fixes the sign of the tail datum H (R162_2401 P2) but
  the sector choice is not forced by anything sign-carrying; the coupling between sectors is empty (Thm 2) or E1 (Thm 3).
- **7A (ω(E) at the contact):** parity does not determine ω(E): the phase condition is parity-independent (§5.2).
- Residue: O202.1 (decide T_e vs T_o for ζ; RH-neutral, not sign-carrying, low priority).
