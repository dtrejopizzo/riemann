# CA_M_000 — Front M (the prime-sited problem): seeds and pre-screens

Phase 193. Pen and paper; **no numerics run**.
**No sign contact. No certified negative value for ζ.**
Read: CA_K_002 (Thm 3.2 site independence, Cor 3.3), CA_K_SYNTHESIS (K-D2 anti-diamagnetism), CA_I_001, CA_H_002 (§1 notation, §3.1
pairing), CA_E_001, CA_J_002, CAMPAIGN_LEDGER; P47 subsec:oneprofile (def of 𝖡, thm:oneprofile, prop:AM), eq:m (C₀ = ψ(¼) − log π).
Corpus check (grep): "prime-sited" only CA_K_*; "Chen" / "Hardy–Littlewood" never used on the window form (R168_102 is
quantitative Kronecker, R162_501 is Chen–Weth PDE); "ζ′/ζ(½)" → phase-159 G2_B1_R1 Lemma 2 and phase-188 L2_BUILD_010 (centre criticality
C₀ = −2ζ′/ζ(½), PROVED there). W-sieve = R167_102 / grid 3A, 6B; NG-A4 = parity problem (MAP_1).

## Setting (checked against P47 prop:AM, def of 𝖡)
𝖡(d) = α(d) − ½Ξ(|d|), α(d) = (1/2π)∫m ĉ₀ cos(τd)dτ, Ξ(D) = Σ_{n≥2}v_n c₀(log n − D), v_n = 2Λ(n)n^{−½}, supp c₀ ⊂ (−2T₀,2T₀), 2T₀ < log 2,
ĉ₀ = F̂₀² with F̂₀(±i/2) = 0 (Tate conditions). Prime-sited test: s supported on primes ≤ M (site 2 allowed or not, stated).
Q(s) := Σ_{p,p′}s_ps_{p′}𝖡(log p − log p′) = Arch(s) − Near(s) (Div ≡ 0, CA_K_002 Cor 3.3(i)).

PRINCIPIO RECTOR test for this front: does the integer relation p − n·p′ = h (the + side) together with the product n·p′ (the · side)
enter the form as an *exact* object, or only through the real number log p − log p′ − log n?

## Seeds
| # | seed | + / · used | pre-screen | decision |
|---|---|---|---|---|
| M1 | exact prime-sited form; shift (Chen-type) decomposition Near = Σ_h C_s(h), primes vs N = p′q^a | + (h), · (N = p′q^a) | identity; (B″) | DEVELOP (CA_M_001 §1) |
| M2 | parity / residue split: odd shifts ⟺ comb prime q = 2; h ≡ p mod ℓ ⟺ q = ℓ | + mod ℓ, · | linear in Λ (H-anat, CA_H_002 Thm 3.2); per-prime local positivity false (CA_F_001 Prop 3) | DEVELOP to record death (§2) |
| M3 | integrality of p − np′: is it seen by the target? real-perturbed sites | + only | decisive test of the PR on this front | DEVELOP (§3, main result) |
| M4 | Chen switching / sieve weights (Selberg, b_θ) as prime-sited test vectors or as bounds on Near | + (sieve) | W-sieve (b_θ ≥ 0, ≤ Λ refutes any upper-bound chain, R167_102); NG-A4 parity: a sieve cannot weight Λ from below | DISCARD (pre-screen) |
| M5 | Hardy–Littlewood singular-series averages (Gallagher; Montgomery–Soundararajan lower-order term −½log H) to evaluate Near | + (h), · (singular series) | conjectural input (OPEN classical); resolution mismatch: Near sees h at scale T₀p (§1.3), bounded h has density → 0; (B′) estimate | DISCARD (ARGUED by §1.3, PROVED in the decisive class by §3) |
| M6 | anti-diamagnetic reversal on prime sites: exact mechanism | · (comb) vs archimedean | must not use the zero side ((R)(4)); FE-class genericity (O10/O12) to be checked | DEVELOP (§4) |
| M7 | multiplicative Goldbach: p ≈ p′q counts (P₂-numbers near primes) via Vinogradov major/minor arcs | + (θ ∈ ℝ/ℤ), · | only the arc θ ≈ 0 has non-negligible weight (§1.4, ARGUED); major arc = PNT in long intervals, comb-generic | DISCARD after §1.4 |
| M8 | Beurling / a_P on prime sites: is "p − np′" a genuine +/· object separating ζ from O11? | + undefined for Beurling | §3: target independent of integrality ⇒ the separation cannot run through h | DEVELOP inside §3 (Cor 3.3) |

Screens common to all: (B″) every statement below holds for any comb (Beurling: Beurling primes as sites); O7 (quartets) keeps sites and
comb; O10/O12 keep the FE. Any seed whose content is "a property of the site set" is tested against §3.
