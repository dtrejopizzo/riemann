# R131.009 — Lead audit of round 3 (Frobenius family, integral shadow, Weil interface)

Author: session lead (Fable 5.1). Date: 2026-09-12. Independent of R131.008.

## 1. Re-derived and found correct

| statement | check |
|---|---|
| Def 3ter.1–2, Lemma 3ter.3 | class of `ι(n)`: `(1/n; unit at p|n; 1/n at r∤n)`; coset `c_nK_{P(n)}` ✓ |
| Thm 3ter.4 | Haar⋆Haar on compact subgroups = Haar on the product subgroup; `c_mc_n = c_{mn}`; `Frob_1 = δ_1 = Δ` ✓; injectivity via modulus and averaged coordinates ✓ |
| Rem 3ter.4a | no weak-⋆ continuous interpolation: correct (`|P(n)|` jumps) |
| Prop 3ter.5 | `Frob_n⋆Δ^{rad} = Γ_n^{rad}` ✓ |
| Thm 3ter.6(ii) | `Frob_n⋆Frob_n^† = Δ^{(n)}`, idempotent ✓ |
| Thm 3ter.10 | shell at `q`: archimedean coordinate of `j_q(q^mw)` is `q^{−m}`; only `n = q^m` survives; for `n=p^k` the `r`-coordinates `p^{−k}=1/n` sit at the centre of the level-`N` cosets, so the indicators are 1 for every `N`; `a_p ≡ h(1/n)` on the shell; unit packets vanish since the unit slice has archimedean coordinate 1 ∉ supp h ✓. The builder's correction of the blueprint (`h(1/n)`, not `∫ρ_ε`) is right |
| Thm 3ter.10 archimedean, Cor 3ter.10b | `b = h·∏1[r^N | n−1]` ✓; vanishes for large `N` when `S_f ⊋ P(n)` ✓; consistent with §3bis (norm class = Frobenius averaged over `K^♮`, which restores the archimedean slice) |
| Thm 3ter.12 | supports meet no stratum for composite `n` ✓ |
| §6bis | `ι(n)_fL_S = nL_S`; triangle `(id,n)` with cokernel `L_S/nL_S` ✓; `Tor_1(Z/2,Z/2)` counterexample ✓; Möbius cofiber via P123.038 (4.1) ✓; P123.022 Scope quoted verbatim ✓ |
| Thm 8bis.1 | `Frob_m⋆Frob_n^†` supported on `c_{m/n}K_{P(m)∪P(n)}`; a shell meets it iff `m/n = q^{±k}` ✓ |
| Thm 8bis.2 | `Ŵ_∞ = −log|τ| + log 2π + O(1/|τ|)`; finite symbols bounded by `A_S`; scaling `σ = ετ` gives `ε^{−1}‖φ‖²(log ε + O(1))` ✓; the builder's correction of the blueprint's rate is right |
| Thm 8bis.4(iv) | the fixed-window obstruction to the naive density argument is correct as stated |

No errors found in round 3. Three things remain to be done, one of them mathematics.

## 2. Instructions for round 4

**L1 (R4, make it a derivation, not a declaration).**  The normalization
`vol_{d^*x}(Z_p^×) = log p` is currently inherited from P123.042 §1. It is
**forced** by the universality of the Tate residue: with `vol(Z_p^×) = c_p`,
Paper 43 (9.11) becomes `Ŵ_p = c_p·2Re(ζ_p/(1−ζ_p))`, `ζ_p = p^{−1/2−iτ}`, and
near `τ = i/2` one has `1−ζ_p = 1−e^{−w}` with `w = (½+iτ)log p`, so
`Res_{τ=i/2}Ŵ_p = c_p·(−i/log p)`; the archimedean residue is `−i`
(Paper 43 Thm 9.7b(b)). Hence **the Tate residues of all local factors agree
iff `c_p = log p` for every `p`** — equivalently, iff the Tate functionals
`λ_±` are the universal residues of the symbol (Paper 43 Thm 9.7b(c)), which is
the product formula in residue form. Write this as a theorem (with the residue
computation) and conclude: `Λ(p^k) = log p` is the Haar volume of the support
of `Frob_{p^k}` in the unique local normalization compatible with the Tate
boundary. R4 is then fully answered.

**L2 (the P123.038 §5 arrow, closed in the only form that exists).**  Extend
`Sh_Z` additively to the free abelian group on the Frobenius monoid — the
"Dirichlet-polynomial correspondences" `Σ c_n Frob_n` — by `⊕`; it is cyclic
trivially (commutative); and the comparison `n^{1/2}·contact_fin = deg_det
Prim(Sh_Z)` extends linearly to that group, where `T` (Paper 43's nuclear
trace on `Corr_A^tr ⊃` smeared Frobenii) is defined. State: this is the
cyclic extension to mixed (finite-combination) arithmetic correspondences and
the comparison with the analytic nuclear trace, **as far as it can exist**;
what is impossible is an object-level functor into the `C`-linear `G`
(P123.022), which is a refutation, not an open item. Re-grade the ledger row
accordingly; the lead's ruling in R131.005 §2 stands.

**L3 (the converse of the interface — attempt, CLASSICAL, quarantined).**
Weil's own proof of "positivity ⇒ RH" uses tests `g_L(t) = ψ(t/L)e^{iγt}`
with `L → ∞`, whose contribution at a hypothetical zero `ρ_0 = β+iγ`,
`β ≠ ½`, grows exponentially in `L`. Attempt to prove: *if `I_∂ ≤ 0` on every
primitive smeared Frobenius combination (all `ε`, all finite `A`), then RH.*
Route: approximate `g_L` on `[a, L]` by `Σ_n g_L(log n)ρ_{ε_n}(t−log n)·gap_n`
(Riemann sum with gaps `log(1+1/n)`), leaving an error supported in `[−a,a]`
of size `O(1)` independent of `L`; show the cross term is `O(L e^{cL})` while
the main term is `≍ L²e^{2cL}`, `c = |β−½|·(const)`, so positivity on the
Frobenius class forces `β = ½`. If the argument closes, label it `CLASSICAL`
(explicit formula used), quarantine it exactly like Paper 43 Thm 10.8b, and
state that it makes the Frobenius Gram form **sufficient** for RH. If it does
not close, record the exact obstruction (which estimate fails) — no
hand-waving. Either way, nothing in B.1–B.9 depends on it.

**L4 (B.7).**  The lead's ruling R131.005 §2 stands: `PROVED` for test and
mechanism on the carrier, with the map to the `Z`-model refuted (P123.022),
not open. Re-grade the row; keep Rem 6.5a′.

## 3. Interim verdict

With rounds 1–3, reservations R1, R2, R3, R6 are dissolved by proved
theorems; R5 has an honest interface with one classical step and one open
converse (L3); R4 becomes a derivation after L1. Renaming test: the Frobenius
family, the integral shadow, the inverse-semigroup relations
`Frob_n⋆Frob_n^† = Δ^{(n)}`, the two-slice theorem (finite Frobenii off
`Im j_∞`, archimedean Frobenius off every `Im j_q`), and `Δ·Δ = −∞` are not
statements of the explicit formula. **Pass.**
