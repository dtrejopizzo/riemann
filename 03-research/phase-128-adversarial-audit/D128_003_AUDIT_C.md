# D128.003 — row C audit: findings and dispositions

Target: Paper 45.

## Accepted (verified) — the crux fails

**C1. Theorem 5.4 ("no corner terms") is broken.**  Step (d) argued: a
functional attached to the source cannot depend on the arbitrary choice of
`p_0 ∈ J`, so it must agree with `τ_J^{p_0}` for every `p_0`, hence annihilates
every label `≠ 1`.  **The premise is inconsistent.**  The reduction
`[Z_J/Γ] ≅ [Y_{J,p_0}/Z^{|J|−1}]` collapses the `p_0`-arrows into identity
arrows of the mapping torus, so for `f ∈ C(Y)`:

    τ_J^{p_0}(δ_{p_0}·f) = ∫f dμ_J ≠ 0,     τ_J^{p_1}(δ_{p_0}·f) = 0  (p_1 ≠ p_0).

The `τ_J^{p_0}` therefore **disagree with each other**, no functional agrees
with all of them, and the argument derives its conclusion from a contradiction.
Underneath: for `|J| ≥ 2` the invariant Radon measure on `B_J` is infinite, so
`A(Z_J)` has no canonical trace **state**; each `τ_J^{p_0}` is a different
finite normalization cut along a fundamental domain of mass `log p_0`.
P123.048 §2 says exactly this — "These normalized traces depend on a measure
convention" — and §5 says "Nonzero algebras and the traces (2.1) do not imply a
particular Weil contribution, **and do not justify declaring higher layers
zero**."  P123.047 §5: "neither a zero contribution nor a copy of `τ` may be
inserted without a comparison from the source shadow."  I verified all three
quotations.  **`ACCEPTED`.  Theorem 5.4 is withdrawn.**

**C2. There is no localization of the character along the filtration.**  It is
never proved that `χ_A` decomposes along (1.4); the splittings of P123.048 (4.1)
are explicitly not asserted equivariant or multiplicative.  P123.048 §5 names
this as the missing result.  `ACCEPTED`.  With C1 and C2, §§5.3–5.5, 6.2 and
the reclassifications in §13.2 that rest on Thm. 5.4 are withdrawn.

**C3. Additivity over places is inherited from a definition.**  P123.046 (4.1)
is stated for `B_P(f) := Σ_p C_p λ_G(f) C_p`, *defined as a sum*, with the note
adding "`B_P` is not asserted to be a compression by their sum, nor a
representation".  So `Σ_p W_p` is a well-defined and canonical functional — but
that it is *the* relative character of the carrier is exactly what is not
proved.  `ACCEPTED`.

**C4. Theorem 9.2's contour step is invalid.**  "Moving the contour to the
critical line ... since the combination is regular there" is false: `ζ'/ζ` has
a pole at every nontrivial zero, and sweeping from `Re s = c` to `Re s = ½`
collects precisely the residues being computed.  `ACCEPTED`.  Disposition: the
explicit formula is **not** reproved here; it is labelled `CLASSICAL` (Weil
1952), stated in the corpus at P124.013 and P123.036 (1.1).  Clause C.8 is
restated to mean what it should have meant: no black-boxed **spectral
realization** (Meyer), which remains true.

**C5. "One operator produces both" is an overclaim.**  `det_ζ(N_Γ+s−½)`
delivers `Γ(s/2)` up to `2^{1/2−s/2}`, not `π^{−s/2}`; `106_195` needs an extra
scalar `√π(2π)^{−s/2}`.  The `log π` in (7.4) comes from P123.035's finite
part, not from the spectrum of `N_Γ`.  Also `N_Γ` is *defined* by its spectrum,
so Thm. 7.2 is a consistency check, not a discovery.  `ACCEPTED`.  Thms. 7.2
and 7.3 are correct as computations (the audit re-verified 7.3 independently)
and are kept as such; the interpretive claims are struck.

**C6. The half-density is archimedean only in the normalized gauge.**
`h_S(n)` has all finite coordinates `1`, where (1.3) is undefined; the ramified
factors come from the other representative `a_S(n)`.  So §0.2(2) is the product
formula in a chosen gauge, not a place-intrinsic fact.  `ACCEPTED`.

**C7. Theorem 6.1 is a normalization-compatibility lemma.**  `vol(Z_p^×)=log p`
is a stipulation (P123.032 §1) chosen to absorb the orbit factor, and the
mapping-torus mass is forced by `dt` modulo `(log p)Z`.  No map or pairing
relating the torsion module to the covolume is exhibited.  `ACCEPTED`;
Remark 6.3's "same Arakelov degree" is struck.

**C8. Proposition 3.2's "compact section" citation is wrong.**  P123.032–033
stabilize the set of contributing **places**, not classes; `K_h` has nonzero
coefficient on a set of classes of positive measure.  The convolution identity
also needs probability Haar on `∏Z_ℓ^×`, unstated.  `ACCEPTED`.

**C9. The `f(1)` counterterm.**  `W_p` *is* independent of `L_p` for `L_p ≥ ℓ`
(P123.042 (3.2)), so each local term is canonical — that part of the audit
overstates.  But P123.033 §1 does record that "A different extension could add
`c_p f(1)`; no cutoff theorem has yet identified its normalization", and
Theorem 5.4 conceded the deep strata contribute a multiple of `f(1)` that is
never computed.  `ACCEPTED in part`: `I_A` is well defined modulo `R·‖·‖²`, and
for a **sign** statement that is not harmless.  Recorded as an explicit open
item for row D.

**C10. Minor, all verified:** `I_A` is Definition 9.1, not 9.2; Thm. 9.2 needs
`F` real for `|F̂|²`; `Σ_ρ` must be taken in symmetric order; "External inputs:
none" contradicts the use of Lerch and `ζ_H(0,a)`; Thm. 10.4's "rescaling
`a_N,b_N`" is wrong because those must stay real — the correct argument is
`106_11` (20)–(21), that `(a,b) ↦ a + b s_0²` is an `R²→C` isomorphism;
`Π`'s injectivity is by analyticity, not continuity.

## Confirmed correct, and kept

- **Theorem 8.1** (the polar packet *is* the hyperbolic Tate form): verified
  against P123.036 §1 and P123.008 (2.2).  Clean.
- **Theorem 10.4** (primitivization; sufficiency for Weil's criterion): checked
  line by line against `106_11` and confirmed, modulo C10's fix to one step.
  The audit's own words: "the strongest and most defensible result in the
  paper", and it "genuinely closes a real gap".
- **Theorem 7.3** (`det_ζ(N_Γ+s−½) = √(2π)2^{1/2−s/2}/Γ(s/2)`): re-derived
  independently from `ζ_H(0,a)=½−a` and Lerch.  Correct.
- **All sign conventions** (`q = −B_nuc`, (1.6)–(1.7), (9.5)–(9.7)) and the
  local computations `p^{−|k|/2}` and `I_L = L+1`: verified correct.

## Disposition

The label `WEIL-STRENGTH-COMPLETE` for row C is **withdrawn**.  See
[D128.004](D128_004_WHAT_SURVIVES.md).
