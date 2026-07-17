# CORRECTIONS — Connes/Consani audit, round R3 (the log-derivative closure)

**Phase 65 / Signature-Continuity Package.** Pure mathematics. This record captures the third correction
round on P51 (the RH proof paper and its verification notebook) and the resolution adopted. The verdict of
the round: **the Vitali bridge is correct and is the right closing mechanism, but the decisive step was
*asserted, not proved*.** The fix replaces an arbitrary-pairing realization with the **log-derivative of
the renormalized spectral determinant**, where the resolvent identity is exact.

Governing principle unchanged: *a false victory is worse than failure.* The single load-bearing input is
named explicitly (**H1**), and the proof is conditional on the standing inputs G1–G5 exactly as the input
box of P51 frames it.

## The six audit points and their resolution

1. **Arbitrary-pairing realization is illegitimate (old Theorem 5.3 / "Check 4").** A resolvent is not
   additive; its Neumann expansion produces cross words `V_{v1}…V_{vr}` (convolutions of all orders) which
   `−ζ'/ζ = Σ Λ(n) n^{−s}` (a log-derivative of an Euler product) does not contain. The cancellation was
   asserted.
   **Fix.** Take the log-derivative of the determinant `D_P^∘ = det₂(I+T_P^∘)`:
   `−∂_z log D_P^∘ = −Σ_{r≥0}(−1)^r Tr(T_P^r ∂_z T_P) + Tr ∂_z T_P`. There the cross words reorganize
   **under the trace** into the single Dirichlet datum `i[Φ_{∞,P} + Σ_{n≤P} Λ(n) n^{−s}]`. This is the new
   **Theorem (word-level trace-log identity)**. The Herglotz property of `M_P := −∂_z log D_P^∘ − E_P'/E_P`
   is then a *theorem* (**Theorem, M_P Herglotz**): `D_P^∘` has only real zeros because `A_P` is
   self-adjoint (G2). That reality of the zeros is the input **H1 ⇐ G2**.

2. **Change-of-variable factor `i`.** With `s = ½ + iz`, `Ξ(z) = ξ(s)` gives `Ξ'(z) = i ξ'(s)`, so
   `M_Ξ(z) = −Ξ'/Ξ = i·M_ξ(s)`, `M_ξ = −ξ'/ξ`. The old Lemma 6.1 conflated `d/dz` and `d/ds`. Fixed
   throughout (Eq. (2.2) of P51); the `i` is what makes `M_Ξ` Herglotz in `z`.

3. **One-variable Weyl function vs two-variable Pick kernel.** `M_Ξ = −Ξ'/Ξ` (and its channel matrix
   `G_Ξ^{G5}`) is a one-variable function; the Pick kernel `K_Ξ(z,w) = (M_Ξ(z) − \overline{M_Ξ(w)})/(z−w̄)`
   is built from it *afterwards*. Vitali acts on the one-variable `M_P`; `sq₋` is read off `K_Ξ` at the end.

4. **Source-frame bound (old Lemma 5.4) was false as proved.** "Schwartz in `log p`" gives only powers of
   `log p`, which do not beat `p^{−1/2}`. **Fix.** Source core `S_a^∘ = { |φ̂(t)| ≤ C_N e^{−a t}(1+t)^{−N} }`
   with `a > 1/4`. Then `|φ̂(k log p)|² ≤ C p^{−2ak}`, so `Σ (log p) p^{−k(1/2+2a)} < ∞` iff `1/2+2a>1` iff
   `a > 1/4`. Uniform in `P`.

5. **Residue detection (old Lemma 7.3) invoked an unconstructed functional.** **Fix.** Constructive Mellin
   bump: `ℓ_a(φ) = ∫_0^∞ φ(t) e^{−iat} dt`; if it killed every `φ ∈ C_c^∞` then `e^{−iat} ≡ 0`,
   contradiction. So some bump detects the residue, `Res_{z=a} G_Ξ = −m_ρ|ℓ_a(φ)|² ≠ 0`.

6. **Notebook `G_R` bug.** `[[R,√R],[√R,1]]` has `det = 0`, trace `> 0`, so `ν₋ = 0` for all `R`; the
   notebook had printed `ν₋ = 1` from an untoleranced `~ −1e−15` eigenvalue. Fixed with a tolerance.

## What this changes in the chain

`D_P^∘` has real zeros (G2 = H1) ⟹ `M_P = −∂_z log D_P^∘ − E_P'/E_P` matrix-Herglotz, bounded
`≤ C_F/|Im z|` ⟹ normal family (Montel). On `U_- = {Re s>1}` (zero-free): `D_P^∘ E_P → Ξ` (G3) ⟹
`M_P → M_Ξ` (log-derivative of a non-vanishing locally-uniform limit), identified with
`i[Φ_∞ + Σ Λ(n) n^{−s}]` by the trace-log identity. Vitali ⟹ `M_Ξ` has no off-real pole ⟹ `K_Ξ` formed
from it has `sq₋ = 0` ⟹ (G5) **RH**. The DH falsifier breaks at **H1**: its sign-indefinite Gram form makes
`A_P^{DH}` a Pontryagin self-adjoint relation with off-real spectrum, so `D_P^{DH,∘}` has off-real zeros and
`M_P^{DH}` is not Herglotz.

## Flagged-items ledger (single residual)

- **[INPUT, H1 ⇐ G2]** `D_P^∘` has only real zeros, i.e. `A_P` self-adjoint on a Hilbert space, i.e. the
  von Mangoldt Gram form is positive (`Λ ≥ 0`). Everything else (trace-log identity, factor `i`, frame
  bound `a>1/4`, residue detection, Vitali) is proved with no use of zero locations and lives in `Re s>1`.
  The proof is conditional on G1–G5; H1 is the precise hinge, and it is exactly the property the DH
  falsifier lacks.

## Artifacts updated

- `04-papers/P51-riemann-hypothesis-proof/main.tex` (+ `main.pdf`, 11 pp, compiles clean): §2 factor-`i`
  and Weyl/kernel split; §5 trace-log theorem + `M_P` Herglotz (replacing the arbitrary-pairing Theorem);
  §6 corrected Lemma 6.1 + LD endpoint convergence; §7 Vitali on `M_P`; Lemma 5.4 → `S_a^∘`, `a>1/4`;
  Lemma 7.3 → Mellin bump; §9 + abstract re-pointed to H1.
- `04-papers/P51-riemann-hypothesis-proof/P51_RH_full_verification*.ipynb`: Part H (six R3 checks) + `G_R`
  tolerance fix. All blocks pass, 0 embedded errors (mpmath dps=40).
