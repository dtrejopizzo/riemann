# Candidate II decided: the Schur coupling of the two metrics of ℕ

Objects: B, 𝔸_M = [B(log m − log k)]_{m,k≤M}, Arch/Div/Near as in STATEMENT_001 §2 (profile a = T_0/2, b = 1, 2T_0 < log 2).
δ(m,k) = log(lcm/gcd) = Σ_p |v_p(m) − v_p(k)| log p, ρ(m,k) = |log m − log k|, 𝕂_t = [e^{−tδ}] = [(gcd²/(mk))^t].
Write β := B(0) = 𝔸_{mm} > 0 (B(0) = a_{T_0}(F_0) ≥ λ_A(T_0) > 0 on the certified range; CITED, Paper 47).

## 1. Corpus check

- Phase 116 (gcd kernel as Gram of dilation states): there the gcd kernel is *identified* with the form. Here it is only a
  Schur multiplier. Difference is genuine, but §2 shows the multiplier version collapses to the form itself.
- L2_028 (multiplicativity diagonalises A_M: NO-GO, real lag log r), L2_029 (near-free tests), L2_030 (Near as separate signed
  operator: NO-GO), L2_031 (residue-balanced subspaces ⟺ D): the Div/Near split tested in §3 is the L2_030 object composed
  with a positive multiplier; §3 shows it inherits the L2_030 failure (a zero-diagonal signed remainder).
- Euler/Möbius algebra family (W7 Λ∗1 = log linear; prop:opcalc): the designer's risk note (row sums Σ_{n|m}Λ(n) = log m)
  is W7 verbatim; not pursued.
- INV_C pair counts: not used.
Verdict: the Schur-multiplier framing is a new *formulation*; §2 proves it carries no content beyond (★) itself, and every
concrete instance tested is NO-GO. Recorded below for the index.

## 2. The existence statement is a restatement (PROVED)

Proposition 1. For every t > 0 and every M: there exist 𝕏_M ⪰ 0, ℝ_M ⪰ 0 with 𝔸_M = 𝕏_M ∘ 𝕂_t + ℝ_M  ⟺  𝔸_M ⪰ 0.
Proof. (⇐) 𝕏 = 0, ℝ = 𝔸. (⇒) 𝕂_t ⪰ 0 (Schoenberg: δ is an ℓ¹ metric on exponent vectors, CND), so 𝕏 ∘ 𝕂_t ⪰ 0 by
Schur's product theorem, and the sum of PSD matrices is PSD. ∎
So Candidate II has content only through a *prescribed* 𝕏. The rest of the memo tests the prescriptions.

Lemma 2 (entrywise cage, PROVED). In any such decomposition, for m ≠ k:
|𝔸_{mk} − ℝ_{mk}| ≤ β e^{−tδ(m,k)}.
Proof. ℝ_{mm} ≥ 0 and 𝕂_{mm} = 1 give 𝕏_{mm} ≤ β; 𝕏 ⪰ 0 gives |𝕏_{mk}| ≤ √(𝕏_{mm}𝕏_{kk}) ≤ β. Multiply by 𝕂_{mk}. ∎
Consequence: on every pair with large δ (in particular every near-coincident pair m ≈ kn, m ≠ kn, and every coprime pair
(k, k+1), δ = log k(k+1)) the remainder ℝ must reproduce 𝔸 up to β(k(k+1))^{−t}. The multiplier part never sees the
near-coincidences; ℝ ⪰ 0 must carry them, which is (★) on those pairs again. The Schur coupling is structurally unable to
move the sign problem off the pairs with ρ small, δ large — exactly the pairs STATEMENT_001 §4(vi) says decide the sign.

## 3. The natural prescriptions: NO-GO (PROVED)

Theorem 3 (division prescription). Let ℝ be diagonal, ℝ = diag(r_m), r_m ≥ 0, 𝕏 = (𝔸 − ℝ) ∘ 𝕂_t^{∘(−1)} (includes r = 0,
𝕏 = 𝔸 ∘ [e^{tδ}]). For every t > 0 there is M with 𝕏_M not PSD.
Proof. B is continuous (c_0 continuous, comb term a finite sum near 0, archimedean part an integral of a bounded kernel
against c_0) and B(0) = β > 0, so there is k_0 with B(log(1 + 1/k)) ≥ β/2 for k ≥ k_0. Principal minor on {k, k+1}:
(β − r_k)(β − r_{k+1}) − B(log(1+1/k))² (k(k+1))^{2t} ≤ β² − (β²/4) k^{4t} < 0 once k^{4t} > 4. ∎
Explicit witness: k ≥ max(k_0, 4^{1/(4t)}). NUMERICAL (validation): λ_min(𝔸_M ∘ [e^{tδ}]) at T_0 = 0.15, M = 12/30/60 is
−0.23/−0.65/−1.01 (t = 0.05), −0.74/−1.57/−2.63 (t = 0.1), −183/−1246/−8226 (t = 1), while λ_min(𝔸_M) = +9.6e−3, +1.3e−3,
+1.6e−4 (normalisation of the phase-190 scripts, β = 1.5905). At t = 0.1, M = 60 the 2×2 minor {59, 60} alone is −5.97.

Theorem 4 (Div/Near prescription). Let 𝕏 = (Arch_M − Div_M) ∘ 𝕂_t^{∘(−1)} on diagonal ∪ divisor pairs plus the archimedean
part of near entries ∘ 𝕂_t^{∘(−1)}, and ℝ the rest. Then ℝ = −Near_M^{comb} is a real symmetric matrix with zero diagonal;
a PSD matrix with zero diagonal is 0 (|ℝ_{mk}|² ≤ ℝ_{mm}ℝ_{kk}); Near^{comb}_M ≠ 0 as soon as M ≥ 4 (pair (4,1), n = 3,
|log 4 − log 3| = 0.288 < 2T_0 = 0.3 at T_0 = 0.15). Hence ℝ_M is not PSD for M ≥ 4. NO-GO. ∎ (Moreover 𝕏 here fails by
Theorem 3's minor on the coprime pairs, whose entries are archimedean.)

Any repair moves diagonal mass into ℝ; by Lemma 2 that cannot help: ℝ must equal 𝔸 off the small-δ set up to
O(β e^{−tδ}), so ℝ ⪰ 0 is (★) restricted to near-coincident pairs plus a bounded perturbation (for t > 1 its Schur-test
norm is ≤ β ζ(t)², PROVED via Σ_k (gcd(m,k)²/mk)^t ≤ σ_{−t}(m)ζ(t) ≤ ζ(t)²) — not small relative to β, and of no sign.

## 4. The dual idea: suppress near-coincidences with 𝕂_t (PROVED: restatement with free endpoint)

Since 𝕂_{t+s} = 𝕂_t ∘ 𝕂_s, the set {t ≥ 0 : 𝔸_M ∘ 𝕂_t ⪰ 0} is a half-line [t*_M, ∞) (Schur). As t → ∞, 𝔸_M ∘ 𝕂_t → βI
(δ ≥ log 2 off the diagonal), so t*_M < ∞ for *every* real symmetric matrix with positive constant diagonal, whatever the
comb. As t → 0, 𝕂_t → J entrywise, so (finite M, closedness of the PSD cone) 𝔸_M ⪰ 0 ⟺ t*_M = 0.
Proposition 5. (★) ⟺ t*_M = 0 for all M. Positivity of the suppressed matrix for all t > 0 transfers to t = 0 trivially
(continuity), but proving it for all t > 0 *is* t*_M = 0, i.e. 𝔸_M ⪰ 0: no information is gained from large t. NO-GO as a
transfer mechanism: large-t positivity holds for every comb (falsifiers included), and the only informative endpoint is
t = 0, where 𝕂_0 = J carries no arithmetic. NUMERICAL: t*_M = 0 for M = 12, 30, 60 (grid step 0.01), consistent with (★).

## 5. Falsifier test

(a) cΛ, (b) a_P, (c) Beurling, (d) finite modification: Proposition 1 and Proposition 5 are restatements valid for any
symmetric matrix with constant positive diagonal; they hold verbatim for all four falsifiers, so they carry no sign step
(correctly: they claim none). Theorems 3, 4 and Lemma 2 are negative statements and use only continuity of B and β > 0,
which hold for all four systems; the NO-GO is therefore uniform over the falsifiers, i.e. Candidate II's prescriptions fail
for the true comb as well as for the false ones. No positive step survived to be tested.

## Result

NO-GO with class: Schur factorisations 𝔸_M = 𝕏 ∘ 𝕂_t + ℝ through the factorisation-metric kernel 𝕂_t = [e^{−tδ}],
and the dual suppression 𝔸_M ∘ 𝕂_t, t > 0.

## What was proved

- Prop. 1: existence of the decomposition ⟺ 𝔸_M ⪰ 0 (restatement; content only in a prescribed 𝕏).
- Lemma 2: |𝔸 − ℝ|_{mk} ≤ β e^{−tδ(m,k)}: the multiplier part is blind to large-δ pairs, so ℝ must carry the near-coincidences.
- Thm 3: 𝕏 = (𝔸 − diag r) ∘ 𝕂_t^{∘(−1)} is never PSD for all M (explicit 2×2 minor on {k, k+1}).
- Thm 4: the Div/Near prescription leaves a zero-diagonal nonzero ℝ, never PSD (M ≥ 4).
- Prop. 5: 𝔸_M ∘ 𝕂_t ⪰ 0 on a half-line [t*_M, ∞); (★) ⟺ t*_M = 0 ∀M; t*_M < ∞ for every comb.

## What failed and why

e^{−tδ} decays on exactly the pairs where the sign is decided (ρ small, δ large); a Schur multiplier can only damp them,
so either the damped part loses them (Lemma 2, Thm 3) or the remainder keeps them with no sign (Thm 4). The divisor
identity Σ_{n|m}Λ(n) = log m is not reachable through 𝕂_t because δ = ρ on divisor pairs makes 𝕂_t a pure archimedean
weight there (e^{−tρ}), indistinguishable from a size weight.

## Next concrete step

Close Candidate II in the index (family "Euler/Möbius algebra, operator partitions", entry "Schur coupling of ρ and δ via
[e^{−tδ}]: restatement + NO-GO, ROUND_003_B"). Any future multiplier route must use a kernel that is *not* PSD-preserving
by Schur alone and that is large (not small) on near-coincident pairs; that is outside this class.
