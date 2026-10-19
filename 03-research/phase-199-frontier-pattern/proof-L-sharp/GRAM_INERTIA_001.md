# GRAM_INERTIA_001 — inertia of the Möbius-lattice Gram G_{mm′} = 𝒲_ext(Zσ^{(m)}, Zσ^{(m′)}) at μ = 15 (NUMÉRICO)

Phase 199, analyst.
Requested by AA_001 §4 ("concrete next test"). No new certification; float64 except step 1 (arb).
Corpus/index check: AA_001 §4, EXTERIOR_DATUM_001, AUDIT_12; index phase-199 block grepped ("Gram", "inercia", "G_{mm′}"):
only AA_001 (b) "G circular" — this memo does not use G as a proof input, it measures where the sign sits.

## Pipeline (same as EXTERIOR_DATUM_001)
Step 1 `GRAM_INERTIA_001_hnodes.py` (python-flint, 320 bits): h(v) = v^{-1/2}p(log v) on the 14 Möbius cells × 900 GL nodes
of [1/λ,λ] (= supp H), p = g*_50 (ROUGH pvecs), same Legendre normalisation. Check: p(T)/√λ = −5.92355186666357e-35 = κ₀ ✓.
Step 2 `GRAM_INERTIA_001_gram.py`: ρ_m(ω) = (2/m)∫H(v)cos(2πλωv/m)dv on the EXTERIOR ω-grid [1,48], Δω = 0.002;
φ̂₀ := ρ_p − Σμ(m)ρ_m (ρ_p = stored EXTERIOR column, min-leak gauge with Tate rows); 𝒲_ext by the EXTERIOR X-form summed over
all 47 dilates (bilinear identity, verified: W(p) direct = 1.326812 = EXTERIOR 'total' ✓; Galerkin 1.2325 differs by the
known ω ≤ 48 truncation). Output `GRAM_INERTIA_001_data/{gram_inertia.json,G_all15.npy,K_classes.npy}`.

## Results
1. **Scale (the main finding).** sup_{[1,48]}|ρ_m|: m=1 3.3e32, m=2 3.0e33, m=3 8.3e33, m=5…14 1.0–1.8e34; φ̂₀ 2.6e33; ρ_p 7.2
   (all ×1e-35). On ω ≥ 4: line 1 7e25, lines ≥ 5 ≈ 1e32–3e33. The lines read the O(1) bulk of Ĥ (σ_λ(1) = −3.3e-3,
   σ_λ(3) = 6e-8, σ_λ(10) = 1e-18), not its tail. Σμ(m)ρ_m + φ̂₀ = ρ_p is a 33-digit cancellation.
2. **Inertia.** G (10 squarefree lines): (10,0,0), eigenvalues 3.7e59 … 1.9e67 W* (cond 5e7, resolved). G (lines + φ₀, 11×11):
   (10,0,1): ten eigenvalues 4.5e59 … 1.9e67 and one at 2.8e52 = float noise floor (1.9e67·ε); its eigenvector is
   v/|v| = (μ(m)) ⊕ 1 /√11 to 4 digits (all |entries| 0.3015 with signs μ(m)). 
3. **Check vᵀGv.** In float: 3.0e53 (noise); assembling Σμρ_m + φ̂₀ first returns 0 (ρ_p lost below ulp). Reproducing
   W(p) ≈ 1.33 (pipeline) / 1.23 (Galerkin) from G would require ≈ 70 significant digits in G — **check fails structurally**, not
   numerically: the lattice Gram is the wrong coordinate system for the value.
4. **Classes (denominator a; pair (line m, dilate n) → a = m/gcd(m,n), coefficients included; 0 = φ₀).** Class Gram K:
   inertia (5,5,1); K_aa < 0 for a = 1 (−4e61), 10 (−5.1e67), 14 (−3.2e67); most negative eigvecs dominated by a = 10 (0.84) and
   a = 14 (0.88), third by a = 2 (0.86). Integer class a = 1 is negligible (|K_11| ≈ 1e-6 of the max). 1ᵀK1 = −1.4e53 (noise; true 1.33).
   Class components are Ψ̌-space pieces, not realisable r-data, so K's indefiniteness is a splitting artefact (Sylvester does
   not relate K and G); it only says the non-integer even-denominator classes 10, 14, 2 carry the large negative pieces that
   must cancel.
5. **Falsifier vectors (vector transport on the FIXED Gram, φ₀ coefficient 1, a_D dilate weights and φ₀ NOT re-solved; so
   these are not falsifier data):** vᵀGv/W*: μ_c c = 0.85 → +2.4e65; c = 1.15 → +3.7e65; μ without p = 2 lines → +3.0e67;
   without p = 3 lines → +4.6e66; lines only (no φ₀) → +1.1e64. **No sign change is visible:** any vector off the null direction
   of G sees the PD bulk and is hugely positive. The falsifiers' negativity (certified elsewhere: CERT_FALSIFIERS_001) is
   invisible at the Gram level; it lives where the ζ datum's own value lives — in the cancellation direction.

## What the inertia says about where the sign is decided
The lattice Gram is positive (numerically PD) on the line span and degenerate exactly along v = μ ⊕ 1. Therefore: (i) the sign
of W(p) is not decided by the inertia of G, nor by the class coefficients C_q (integer class negligible; non-integer classes
10⁶⁷-size and mutually cancelling); (ii) it is decided by the second-order structure inside the null direction — the
Schur complement of G along v, i.e. by how admissibility (band limitation of f, Tate constraints on φ₀) forces the
33-digit cancellation; (iii) falsifier vectors transported on a fixed G are uninformative (they leave the null direction).
Labels: all NUMÉRICO (float64, ω ≤ 48 truncation; Gram entries of bulk lines are cutoff-dependent since ρ_m is not small at
ω = 48). Obstruction (NUMÉRICO, not a proved NO-GO) for the method class "inertia / coefficient bounds of the lattice Gram on
{Zσ^{(m)}} ∪ {Zφ̂₀}": it cannot see the sign. Row D OPEN.
