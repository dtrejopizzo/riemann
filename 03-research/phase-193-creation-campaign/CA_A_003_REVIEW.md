# CA_A_003 — Review

## Verdict
**§2 CONFIRMED PROVED; Hecke-on-σ_T EXCLUDED (O1–O7, O15 survive; thm:shape(B″)). §3 REF-D ((S)/EI_002 T*₃(η)) and (B′). §4 OPEN, CITED-UNVERIFIED; pre-screened REF-D for the diagonal Parseval reading.**

## 1. PROVED claims
| claim | check | label |
|---|---|---|
| Σa_τ(n)n^{−w} = ζ(w+iτ)ζ(w−iτ); a_τ(p)=2cos(τ log p); unitary Hecke relation | standard (Ramanujan) | CITED/CONFIRMED |
| Thm §2: Hecke relations among cos(τ log n) are 2cos a·2cos b = 2cos(a+b)+2cos(a−b) | ✓; valid for any reals x,y and any finite measure on (0,2T) | CONFIRMED PROVED |
| "a_τ does not appear in σ_T" | σ_T = m − Σv_n cos(τ log n), degree 1 ✓ | CONFIRMED |

## 2. Modifications
Hecke relations as used in §2 hold for every positions set (O15 Poisson), every weights (O1–O6), Beurling (O7: x,y arbitrary reals): **EXCLUDED** by lem:shape-ident / (B″). The test-side reading (§3) keeps b multiplicative and changes Λ ↦ a_P: the inequality "∫σ_T|F̂₀|²|ζ_M|² ≥ 0" is a class statement until evaluated; its evaluation is an estimate with remainder: (B′). Agree.

## 3. (R)
§2: (1),(3),(8),(11) not met. §3: (11) not met; sign step = (S) — **REF-D** (phase-192 EI_002 review). Agree with memo.

## 4. §4 metaplectic (OPEN)
Goldfeld–Hoffstein normalization: at s=½+it, L(2s−½,χ_n) = L(½+2it,χ_n); n=□ gives ζ(½+2it)·(finite Euler factors) ✓ (CITED, verify). Maass–Selberg constant term ζ(4s−1)/ζ(4s) → ζ(1+4it)/ζ(2+4it), abscissa 1 ✓. Horocycle Parseval = diagonal |c_n|² = second moment of ζ: REF-D to (S) as the memo says. The off-diagonal packet form is OPEN and not built; pre-flag: (i) a positive form on L²(Γ₀(4)\ℍ) applied to Eisenstein packets is a norm, comb-generic in the sense that it holds for every lattice/character (O11/O12 risk, as CA_A_001); (ii) (R)(4): the packet norm involves ζ(½+2it)/ζ(4s−1) — the denominator is at abscissa 1, harmless, but any sign beyond ≥0 of a norm goes through the continuous-spectrum density = zeros. It remains to show which positivity is not a norm.
Note also (CA_A_001 review §3): line doubling is not the only escape; the Mellin variable of weight-0 E already reaches ζ(½+iτ).

## 5. Retry: §2 overlaps 159 G1_B2_R3 §5.3 (Hecke-shape carriers, zero side) and R9-15; test side = phase 192. New: the explicit comb-genericity proof of Hecke relations on σ_T. Endorsed move: "Hecke multiplicativity is a mechanism on σ_T" YES→NO (PROVED).
