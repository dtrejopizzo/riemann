# CA_A_SYNTHESIS — Front A of phase 193 (creation campaign): closing synthesis

Pen and paper. One literature lookup (citation verified); no numerics.
**No sign contact anywhere. No certified negative value for ζ.**

## Seeds and verdicts
| memo | seed | verdict | label |
|---|---|---|---|
| CA_A_001 | Petersson / Maass–Selberg / Rankin–Selberg norm positivity on PSL₂(ℤ)\ℍ | NO-GO for the norm class (Hilbert-norm positivity of Eisenstein data; abscissa 1; survives O10 via CM points and O12) | PROVED for the class; general extension withdrawn |
| CA_A_002 | Lewis–Zagier period functions / Mayer transfer operator | NO-GO: positivity only at real s; Λ only via det (zeros) | ARGUED (Prop 1 PROVED) |
| CA_A_003 | Hecke multiplicativity as the Euler mechanism | at tempered parameters, the Hecke relations are cosine identities and comb-generic (B″); on the test side they give (S) | PROVED |
| CA_A_004 | weight-½ metaplectic Eisenstein series on Γ₀(4) | NO-GO: Parseval positivity, rank one per index, mixes all χ_D | Prop 1, Cor 2 PROVED; Cor 3 ARGUED |
| CA_A_005 | regularized Rankin–Selberg with the minimizer-built test g=F̂₀D_h | NO-GO: test-generic and comb-blind (B″); no kernel equals the window multiplier; continuation to ½ gives (S) | Props 1–3 PROVED; Prop 4 ARGUED |
| CA_A_006 | moving Maass–Selberg positivity from abscissa 1 to ½ (Y-integration; Hecke average) | NO-GO: Y-integration never moves the arithmetic abscissa (MW-2); Hecke average = (S) | PROVED |
| CA_A_007 | homotopy / no-crossing; boundary triples; cross-place reflection positivity | homotopy covered (N_012, W5, flowdet, W-cont); boundary triple = 𝔊_T coordinates; RP false for every atomic comb | PROVED (reduction, Thm 2) |
| CA_A_008 | integer invariant (spectral flow / Maslov / signed index) | collapses: constancy along the path is equivalent to the target (REF-D); forcing mechanisms are dead (P49-2, P37-2, P35-3, NG-69, inertia-nogo, R186_028) | PROVED (Lemma 1) + cited NO-GOs |

## Exact facts proved on this front (usable elsewhere)
1. **No invariant positive form at Re s=¼** (CA_A_001 Lemma 2): Im s(1−s)=t/2≠0. *Line doubling as a general barrier is
   WITHDRAWN* (Mellin in y and Rankin–Selberg in w reach ζ(½+iτ) on the unitary axis). It holds only for the invariant-form /
   norm class.
2. **Hecke at tempered parameters is comb-generic** (CA_A_003 §2): the Hecke relations are cosine product identities, valid for any
   positions, so (B″) applies.
3. **Metaplectic coefficients** (CA_A_004 §0, CITED and verified): Duke–Imamoḡlu–Tóth, Ann. Math. 173 (2011), Lemma 4,
   eqs. (2.23)–(2.25): b₀(Dm²,s) ∝ L_D(2s−½)/ζ(4s−1); unitary axis Re s=½.
4. **Rank-one obstruction** (CA_A_004 Prop 1): the off-diagonal horocycle-Parseval kernel is g_n(t)·conj g_n(t′) for each n.
   Matching a multiplication operator needs D-orthogonality, which is an estimate (B′).
5. **Continuous kernel ≠ window multiplier** (CA_A_005 Prop 2), by a Hilbert–Schmidt argument.
6. **Maass–Selberg is the window form of ζ(2s) on the squares** (CA_A_006 Remark 3): 4Λ(n)/n = 4Λ(√N)/√N at N=n², and
   cos(2τ log n)=cos(τ log N). Its positivity is PNT-strength.
7. **Y-integration of the Maass–Selberg cone fixes the arithmetic abscissa** (CA_A_006 Theorem 2): μ enters only through
   scalars and the positive-definite multiplier μ̂.
8. **Hecke average Σn^{−½}T_n has Eisenstein eigenvalue |ζ(½+iτ)|²**, so it gives the second moment (S) (CA_A_006 §3).
9. **Reflection positivity is the Hankel half** (CA_A_007 Lemma 1): 𝔞_T(f+Θf)=2𝔞_T(f)+2H_K(f). OS reflection positivity
   fails for every comb with an atom (Theorem 2, bump at ½log n0).
10. **Boundary triple Weyl function at λ=0 is 𝔊_T** (CA_A_007 Prop 1; thm:parityschur).
11. **Spectral flow constancy along a path from a positive endpoint is equivalent to no crossing** (CA_A_008 Lemma 1).

## YES→NO moves proposed (subject to endorsement in CAMPAIGN_LEDGER.md)
- Hecke/Petersson positivity carries the window comb at ½ → NO (norm class).
- Lewis–Zagier route: OPEN (never attempted) → NO-GO (ARGUED).
- Hecke multiplicativity as a mechanism on σ_T → NO.
- Metaplectic Parseval carries the σ_T-correlation without Shimura → NO.
- Rankin–Selberg with a minimizer-built test couples to the window form → NO.
- Maass–Selberg positivity can be moved to abscissa ½ by positive Eisenstein-side operations → NO.
- Reflection positivity (per place or cross-place) carries the window sign → NO. NG-E1 cross-place: never built → NO-GO.
- Boundary triples for W_λ: never attempted → covered as coordinates of thm:parityschur.
- Integer invariant along a path from a positive endpoint → REF-D.

## Diagnosis of the front
Every PSL₂(ℤ)/automorphic positivity found is either blind to the comb and to h* (norms, Parseval, reflection
positivity, Rankin–Selberg weights) or an exact restatement (𝔊_T, spectral flow, (S)). The ζ-specific arithmetic it does
carry sits at abscissa 1 (ζ(2s) on the squares), and moving it is MW-2. The missing object must be open in the weights
(CA_B_006) and couple to h* at the sign step (the O7/O8 lesson). None of the automorphic structures examined does both.
Open residues left: the half-integral-weight Kuznetsov/Salié variant (CA_A_004 §5–6, low priority); (M) propagation
(L2_027) in general; Cayley signed index (632), unbuilt.
Front A stops here.
