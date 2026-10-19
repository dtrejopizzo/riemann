# CA_H_000 — Seeds, front H (the semiring (ℕ,+,·): interplay of addition and multiplication as the source of the sign)

Phase 193. Pen and paper, no numerics.
**No certified negative value for ζ. No sign contact.**
Read before seeding: CA_G_SYNTHESIS + CA_G_000 (G0, G1), CAMPAIGN_LEDGER, CA_A/B/D/F_SYNTHESIS, CA_C_000 (screen key), CA_C_007
(FE-class genericity), CA_E_001 (separability; Kronecker line), CA_F_003 (gap G-F), P47 §20 (def:shape-ops, lem:transfer,
prop:shape-inputs, lem:shape-quartet, lem:shape-ident, cor:shape, prob:region (R)(1)–(11)), P47 prop:nearfree, rem:boxes,
thm:ceiling, rem:resolution, thm:band, thm:oneprofile, prop:AM, ROUTES-TRIED-INDEX README + 06_ (R9 table of dead sub-routes),
phase 190 EXP_005, phase 191 SPEC_B §1.3/§4 (Lines 1–4), phase 192 README + EI_002, phase 159 G1_B9_R2 (Lemma 3, Remark 3.1).

**Corpus grep (done first).** Buium: 3 hits, all G1_B9_R2/P4/P5 (Remark 3.1 "per-prime, not additive", HEURISTIC). p-derivation,
Fermat quotient, Wieferich, Raynaud, Erdős–Szemerédi, Solymosi, Elekes, "multiplication table", Kátai: 0 hits. Mason: 2 (not
Mason–Stothers). Stothers: 0. sum-product: 3 (R162_590 O-D4.1 "sum-product in one quadratic step" = (S); R152_001 lists Bourgain;
R166_403 survey). Stepanov / Bombieri–Stepanov: P38-2, G1_B9 (Lemma 3 PROVED: no characteristic-0 derivation kills p-th powers;
Thm 3′: transported Stepanov speaks only as u → ∞). Witt/Borger: P44-1 (Hodge–Witt, DEAD), G4H-159 G1_B5 (Borger/Witt/Bost–Connes,
DEAD), R160 C4 (W(ℝ) correction = Weil archimedean term, REF-D), R175_FINAL (Borger third coordinate, NO-GO W10). Frobenius lift: phase
107/114/159 (CM lifts, G1_B5_R3). Integrality defect: phase 163/164 (Theorem L, R164_201, PROVED, no sign). Near-coincidences
m ≈ kn: phases 188–192 (L2_020/023/028–031, N_021/022, EXP_001–005, SPEC_B, EI_002 Thms 1–5) — **the near-coincidence +/· locus is the
most-mined part of the corpus**; every seed below states which of those records it is not.

## Screen key
As CA_C_000 / CA_G_000. Idx = retry of an indexed route. (R)k = clause k of prob:region. O-labels are Paper 47's (O2 = Λ+cδ_{n₀},
O6 = a_P, O7 = quartets, O8 = f_t, O10 = Epstein/DH, O11 = Beurling, O12 = ζ_K, O15 = Poisson). B′ = estimate with remainder;
B″ = identity valid for every comb. G0 = squares are Gram factorizations; G1 = monoid-functorial positivity survives O11/O12.
FE-gen = survives the FE-class generic falsifier (Epstein x²+5y², CA_C_007). [crit] = must resolve the sign at relative precision
M^{−3} on the family s_w (EXP_005 C1, NUMÉRICO). REF-D = restatement of the target.

## Common fact H0 (PROVED, from the definitions of P47): the +/· genuineness test
Call a property 𝖯 of the form object **monoid-only** if it is defined from (ℕ^×, N) alone (free monoid plus norm), **additive-only**
if it is defined from the additive group ℤ ⊂ ℝ and the archimedean place alone (Poisson summation, Γ_ℝ, theta functions), and
**+/·-genuine** otherwise.
(a) Monoid-only ⇒ the property transfers to every Beurling system with free generators (O11) and to every ζ_K (O12): G1.
(b) Additive-only ⇒ the property is shared by every real-analytic Dirichlet series with the same Γ-factor and FE coming from a
    lattice theta function, in particular by the Epstein zeta function of x²+5y² (O10), whose FE is Poisson summation on ℤ²
    and which has no Euler product. So it is FE-gen (CA_C_007).
(c) Comb-only ⇒ the property survives O7 (lem:shape-quartet: the quartet models keep (Λ(n))_n exactly), whatever its +/· content.
**Label (FIX 1):** (a), (c) PROVED; (b) ARGUED — x²+5y² has Γ(s) and conductor 20, not Γ_ℝ at conductor 1, so the transfer of an additive-only property must be checked property by property (as CA_C_007 did).
Hence **a sign step drawn from the semiring must be +/·-genuine (fails for O10 and for O11), and must read the form, not the comb (P3),
because of (c).** By prop:shape-inputs the +/·-genuine content available is exactly (E) Euler product over ℕ [·], (I) integrality of the
frequencies [the norm image is the additive monoid ℕ], and (F) FE at conductor 1 [Poisson on ℤ, +], used jointly.
*Proof.* (a) is G1 (CA_G_000). (b): the Epstein ζ_Q, Q = x²+5y², satisfies Λ_Q(s) = Λ_Q(1−s) from Poisson summation on ℤ² (Hecke,
CITED as in P47 lem:shape-epstein), has nonnegative coefficients on ℕ and a pole at 1; a property built only from ℤ-Poisson and Γ_ℝ is
built identically for it. (c) is lem:shape-quartet. ∎
**Where the semiring sits in the target (PROVED, P47 prop:AM + CA_E_001 Lemma 0).** In the PD-on-G formulation (G = ℚ_{>0}^×), the
monoid part is the group G and the exact relations m = kn (Div); the additive part is the archimedean topology of G, i.e. the rationals
q = a/b ≠ 1 with |log q| < 2T₀, which are exactly the **additive near-identities a = b + h, |h| < (e^{2T₀}−1)b** (Near). This is made
an exact identity in CA_H_002 Theorem 3.1 (Near = Kronecker defect of the line measure against Haar measure).

## Seeds (each row states the +/· use, why it is not monoid-only, why it is not additive-only)
| # | seed | +/· use | not monoid-only? | not additive-only? | Idx |
|---|---|---|---|---|---|
| H1 | Buium p-derivations δ_p(x) = (x−x^p)/p, arithmetic jet/Wronskian; Mason–Stothers analogue | δ_p is the unique map with δ(a+b) = δa+δb+C_p(a,b) (carry) and δ(ab) = a^pδb+b^pδa+pδaδb: the defining mixture of + and · | yes (C_p uses +) | yes (Frobenius lift uses ·) | new (G1_B9 Remark 3.1 HEURISTIC only) |
| H2 | Stepanov/Bombieri auxiliary polynomial with a derivation replacing d/dt over ℤ | d/dt kills p-th powers (char p) | — | — | retry G1_B9 Lemma 3 / Thm 3′ |
| H3 | carries and Witt vectors as the explicit +/· cocycle | carry C_p(a,b) = (a^p+b^p−(a+b)^p)/p | yes | yes | partly P44-1, G4H-159, R160 C4; differs: carry cocycle itself, not W(R)-corrections |
| H4 | sum-product as exact structure: near-coincidence graph, multiplicative/additive energies, multiplication-table (Ford), Erdős–Szemerédi/Solymosi | |A·A| vs |A+A| on supports of test vectors | yes | yes (as set statements) | new; neighbours R162_590 O-D4.1, L2_020 |
| H5 | the semiring invariant ℤ has and every falsifier lacks: successor-continuity of the divisor sum (Erdős's characterization of log) | f(n+1)−f(n) → 0 (+) for additive f (·) | yes | yes | new |
| H6 | Kronecker line ι(ℝ) ⊂ Ĝ on multiplicative test vectors (front E input): Near as line-minus-Haar defect | line = archimedean (+), Haar = monoid (·) | yes | yes | retry on boxes: CA_C_002 Prop 2(d); new: full-solenoid form + anatomy (CA_H_002 §3) |
| H7 | integrality gap / Liouville / product formula: |a−b| ≥ 1, |log(a/b)| ≥ 1/max(a,b) | integer determinant of two lattice vectors | yes | yes | retry: P47 thm:ceiling + rem:resolution (density ceiling), phase 163/164 (integrality defect, Thm L), CA_C_001 (product formula) |
| H8 | polarized object over ℤ built from global Frobenius lifts (Λ-structure, Borger): the ℤ-analogue of Γ_Frob ⊂ C×C (coordinator's bridge to G-F) | Frobenius lifts at all p = δ-structures | yes | yes | partly MW-5/OT-5′, R175 (Borger coordinate), G4H-159; new: Raynaud obstruction + P¹ computation |
| H9 | divisibility pattern of integers N ≍ M by small n (CRT, residues), SPEC_B Line 3 | n | N with N ≈ M | yes | yes | retry SPEC_B §4 Line 3, L2_030 §3 (c_{p^b}(j)), N_021 |
| H10 | arithmetic derivative n′ (Barbeau), logarithmic derivative ld(n) = Σv_p(n)/p | Leibniz on ·; no rule for + | **no** (defined from the monoid with weights 1/p) | — | new |

## Full pre-screen table
| # | (R) | (P1)–(P6) | O2 Λ+cδ₂ | O6 a_P | O7 quartets | O8 f_t | O10 Epstein/DH | O11 | O12 ζ_K | FE-gen (x²+5y²) | B′ | B″ | G0 | G1 | REF-D | [crit] | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| H1 | (8) per prime; (5) bounded at p ≥ 3 | P1 ✓, P3 ✗ (comb-level split), P6 ✗ | δ_p-calculus on tests holds for every 𝖡 (B″) | δ-log comb Λ·1[not p-th power] is itself an O3/O6-type modification | survives (comb split) | breaks (I): no Frobenius lift on non-integral frequencies | δ-structure on D_ℤ exists for every ℤ-coefficient series, incl. ζ_Q | Beurling: φ_p undefined unless norms closed under p-th powers — (I)-sensitive ✓ | ζ_K ∈ D_ℤ too: survives | survives (D_ℤ functorial) | — | ✓ for the test calculus | — | — | split = CA_B_007 | ✗ (bounded at p≥3) | EXCLUDED at screen; developed only to record the death (CA_H_001) |
| H2 | (4) zero-side if the auxiliary function vanishes at ordinates | P4 ✗ | — | — | — | — | — | — | — | — | — | — | — | — | — | — | DISCARD (retry G1_B9; char-0 Lemma 3) |
| H3 | (8) per prime | P3 ✗ | form is carry-blind: weights Λ(n) depend on n, not on digit relations (CA_H_001 §1.4) | — | survives | — | — | — | — | — | — | ✓ | — | — | — | — | DISCARD (folded into H1 §1.4) |
| H4 | (3) C–S/energy bounds; (5) set statistics | P1 ✗ (energy bound of 𝔞 on a set), P3 ✗ | survives (set statements ignore weights) | survives | survives | **survives** (Solymosi/Elekes hold for real sets) | n/a | **survives** (real sets) | survives | survives | ✓ (constants O(1) or log) | ✓ | — | — | — | ✗ (log-loss ≫ M^{−3}) | DISCARD |
| H5 | (10) names the property separating ζ from ζ_K ✓ | P3 ✗ (comb-only), P6 ✗ | separated ✓ | separated ✓ | **survives** | separated | separated | separated | separated ✓ | separated | — | — | — | — | — | — | **DEVELOP (CA_H_002 §2)**: exact separating invariant; dies at O7 by (c) |
| H6 | (8) ✓ all frequencies; (7) exact at integer resolution ✓ | P1 ✓, P2 ✗ (linear in Λ), P3 ✓ (form), P5 ✗ (identity for every comb) | identity holds | holds | holds | holds | its own G | holds for independent Beurling logs | holds | holds | — | ✓ | — | Haar part is monoid-only | sign content = (S) | [crit] reading only | **DEVELOP (CA_H_002 §3)**: exact identity; sign content REF-D |
| H7 | (7) ✓ | P1 ✓ | — | — | — | — | — | Beurling lattice combs satisfy a gap too | — | — | ✓ (gap is a one-sided bound) | — | — | — | gives only the density ceiling (necessary direction, thm:ceiling) | ✗ | DISCARD (retry) |
| H8 | (10) | — | — | — | — | — | — | — | — | — | — | — | Hodge index = Gram | — | G-F | — | **DEVELOP (CA_H_001 §5)**: NO-GO for the declared class (Raynaud + P¹ content-free) |
| H9 | (5) local on residues; (8) | P2 ✗ (W7 linear) | — | — | survives | — | — | — | — | — | — | — | — | — | REF-D for η ≤ η₀ (SPEC_B §1.4) | ✓ sensitive | DISCARD (retry SPEC_B) |
| H10 | (10) ✗ | — | — | — | — | — | — | **survives** (monoid + weights 1/N(p)) | survives | — | — | — | — | ✗ G1 | — | — | DISCARD (G1) |

**Survivors / least-dead developed:** H1 + H8 (CA_H_001, one memo: δ-structures on ℤ and on schemes over ℤ), H5 + H6 (CA_H_002, one
memo: the separating semiring invariant and the Kronecker-defect identity for Near). Both memos end in proved statements of where the
seed dies.

## Self-review of the screen
1. *H4 discarded too fast?* Sum-product theorems are inequalities about finite sets of reals with constants that are powers of log|A|.
   They survive O11 and O15 (they never use that the set is in ℕ), they ignore the weights (survive O2/O6), and their losses are ≫ M^{−3}.
   An *exact* sum-product structure in the form is H6's identity (Near = line − Haar), which is developed. Nothing is lost.
2. *H7 is the most +/·-genuine object of all (the integer determinant).* Agreed; but its only output in the record is one-sided
   (thm:ceiling: density ≤ 1; rem:resolution says explicitly it does not give the mechanism). A positivity proof needs the other side.
   Phase 163/164 built the integrality-defect inequality (Thm L, PROVED, no sign). Retry.
3. *H9 is the near-coincidence locus itself.* Yes; SPEC_B Lines 1–4 already reduce the family statement to it, and its content for
   η ≤ η₀ is REF-D. Not reopened; H6 gives it a new coordinate (line − Haar), which is the honest addition.
4. *H10*: the arithmetic derivative uses + only in its (unproved) conjectures, never in its definition: G1 applies.
