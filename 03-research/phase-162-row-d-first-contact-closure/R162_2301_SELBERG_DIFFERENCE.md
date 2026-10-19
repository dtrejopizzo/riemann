# R162_2301 — Cell 6C: Selberg's identity in the difference channel, at the first-contact witness, without resumming

Pure mathematics, no numerics. Cell **6C** (exact values of Λ × quadratic functionals), live residual
of the master grid: "R162_901: difference channel |Σ w_n n^{it}|², without resumming to Σ_ρ". Nearest routes:
R162_901 (Lemma 3.1, Prop 3.2), R162_1003 (Thm S, Thm R: resumming = E1; not used here), R162_2202 (Thm NI: node
range n < e^{T_c}), R162_2201 (O2201.1), R160_X_C1 Thm G (Gauss-node quadrature). Walls named in advance: W12 (exact
identity without sign), W3 (F3 at the use step), W4 (F2). Conventions: μ = σ_{T_c}dτ/2π + δ_{−i/2} + δ_{i/2},
W(G,H) = ∫ĜĤ^#dμ, witness F ∈ E_c real, nodes x = real zeros of F̂, weights w_x = d_x/F̂′(x)² ≥ 0.

**Verdict: NO-GO (PROVED), with one PROVED correction and one PROVED tool.**
- Lemma S (Selberg ⟺ a = Λ, recursive uniqueness), and a correction to R162_901 Lemma 3.1: the "support ω ≤ 2"
  property is class-blind. PROVED.
- Theorem DC (the node-level difference and sum channels are the values W(Dψ,Dψ) and W(Dψ,D̃ψ) of the form, with
  composed thresholds ½log mn exactly visible for m,n < e^{T_c}). PROVED under (Q) below.
- Theorem Q (no sign conflict): every exact node identity built this way is compatible with w_x ≥ 0, for every
  datum, because its positive part is W_{T_c} ≥ 0 (the definition of T_c) via Akhiezer–Fejér–Riesz. PROVED.
No sign for ζ is claimed. Gate 1 stays OPEN. No label moves.

## 0. Failing lines (stated first)

| model | Selberg identity aL + a*a = μ*L² | node identities of Thm DC | sign conflict with w_x ≥ 0 |
|---|---|---|---|
| Λχ₂ | fails (N = 3: −log²3 vs +log²3); satisfies the twisted identity with (μχ₂)*(χ₂L²) | hold verbatim with its own a | none (Thm Q) |
| two-atom Type I s₂δ_{log2}+s₃δ_{log3} | fails by Lemma S (a ≠ Λ: e.g. a(5) = 0 ≠ Λ(5)) | hold | none; the contact at s₂^c is a genuine first contact with w_x ≥ 0 |
| deletion Λ1_{n≥5} | fails at N = 6 (a*a(6) = 0 ≠ 2 log2 log3) — **not** at N = 30 (see §2) | hold | none |
| κ-model | fails at N = p (κ log²p ≠ log²p for κ ≠ 1 on that p) | hold | none |
| DH | coefficients of −L′/L not supported on prime powers; fails | hold | none |
| Beurling DMV | the ℕ-indexed identity fails; the 𝒩_B-indexed one holds (integrality is the only separator) | hold | none |

L2301.a (§3): the node sums are form values, so Selberg re-expresses one W-value in two ways; the datum-specific
content sits on the coefficient side, never on the sign side (W12).
L2301.b (§4): the exactness class of the quadrature is exponential type ≤ 2T_c, and on it nonnegative functions are
|Ĝ|² with type ≤ T_c (Akhiezer), so the node functional is positive there because W_{T_c} ≥ 0. Outside it there is no
identity (Prop T of R162_2202: ascent raises the type).
L2301.c: |D_a|² and Re D_a² are invariant under a → −a (F2), and the whole construction is identical at every λ ≥ 0
bottom (F1 as a forcing mechanism).

## 1. Corpus check

Grep in phase-16x for "Selberg", "Λ*Λ", "difference channel", "quadrature" together with "node": hits are R162_501,
901, 1003, 2201, 2202, R160_X_C1 only. No file evaluates a Dirichlet polynomial in Λ at the Gauss nodes, and none
states the Akhiezer closure of §4. Theorem S/R of 1003 is not used (no functional equation, no Σ_ρ).

## 2. Lemma S (Selberg separates by uniqueness) — PROVED

**Lemma S.** Let a: ℕ → ℂ with a(1) = 0. Then a·L + a*a = μ*L² holds for all N iff a = Λ.
*Proof.* ⇐ is Selberg (coefficients of (ζ′/ζ)′). ⇒: for N ≥ 2, a(N) log N = (μ*L²)(N) − Σ_{mn=N, 1<m,n<N} a(m)a(n)
determines a(N) from a on smaller arguments. ∎

**Correction to R162_901 Lemma 3.1.** For **any** a supported on prime powers, a*a is supported on ω ≤ 2 (a product
of two prime powers has at most two prime factors) and a·L on ω ≤ 1. So "support fails at N = 30" for the deletion
model is false: both sides vanish at 30. The deletion model fails at N = 6. The separation of Lemma 3.1 is correct
only as the equality with μ*L², i.e. Lemma S. Twisted version: for completely multiplicative χ,
(aχ)L + (aχ)*(aχ) = χ(aL + a*a), so Λχ₂ satisfies Selberg with right side (μχ₂)*(χ₂L²) and fails the untwisted one.

## 3. Theorem DC (the channels at the nodes are form values) — PROVED under (Q)

**(Q)** (OS-3 density, with dim E_c = 1): 𝒟_{T_c} = ℂF ⊕ closure span{H_x}, and then W(G,H) = Σ_x w_x Ĝ(x)conj Ĥ(x)
for G, H ∈ 𝒟_{T_c} (Thm G(d) plus W(F,·) = 0 and Ĥ_y(x) = 0 for y ≠ x).

Let D_b(z) = Σ_{n<N} b_n n^{iz}, D̃_b(z) := Σ_{n<N} b̄_n n^{−iz}, so conj D̃_b(x) = D_b(x) on ℝ. Let ψ ∈ 𝒟 have type s
with N e^{s} ≤ e^{T_c}.

**Theorem DC.** Under (Q):
- (i) difference channel: Σ_x w_x |D_b(x)|² |ψ̂(x)|² = W(D_bψ, D_bψ) ≥ 0;
- (ii) sum channel: Σ_x w_x D_b(x)² |ψ̂(x)|² = W(D_bψ, D̃_bψ), and every composed threshold ½log mn with m, n < N ≤
  e^{T_c − s} enters exactly, even when mn > e^{T_c};
- (iii) with b_n = Λ(n)n^{−1/2} and Lemma S, for mn < N the pair sums in (ii) regroup to
  Σ_{k<N} k^{−1/2}[(μ*L²)(k) − Λ(k)log k] k^{ix}, plus the explicit incomplete-divisor tail over k ∈ [N, N²);
- (iv) the algebraic split |D|² = 2(Re D)² − Re D² turns (i) into
  Σ_x w_x |D_Λ(x)|²|ψ̂(x)|² = 2 Σ_x w_x (Re D_Λ(x))²|ψ̂(x)|² − Re W(D_Λψ, D̃_Λψ), an identity between form values.
*Proof.* D_bψ and D̃_bψ have type ≤ log N + s ≤ T_c, so they lie in 𝒟_{T_c}; apply (Q). (iii) is Lemma S
coefficientwise; (iv) is algebra. ∎

This is the requested object: the difference channel restricted to the witness, with Selberg at composed thresholds
in the node-visible range, no functional equation and no Σ_ρ. It matches Thm NI of R162_2202 (only n < e^{T_c}).

## 4. Theorem Q (no sign conflict) — PROVED

Let 𝒢 be the span of products ĜĤ^# with G, H ∈ 𝒟_{T_c} (entire of type ≤ 2T_c).

**Theorem Q.** For every admissible datum with a first contact at T_c and (Q), the node functional
ℓ(h) := Σ_x w_x h(x) equals ∫h dμ on 𝒢, and ℓ(h) ≥ 0 for every h ∈ 𝒢 with h ≥ 0 on ℝ. Hence no exact identity
obtained from Theorem DC (any b, in particular b = Λ with Lemma S) is incompatible with w_x ≥ 0.
*Proof.* Equality on 𝒢 is (Q) and polarisation. If h ∈ 𝒢 is ≥ 0 on ℝ and integrable against the densities in play,
Akhiezer's factorisation (Fejér–Riesz for entire functions of exponential type, Krein class) gives h = |Ĝ|² on ℝ
with Ĝ of type ≤ T_c, hence ℓ(h) = W_{T_c}(G) ≥ 0, since T_c is the first contact (W_{T_c} ≥ 0 is its
definition). ∎

**Reading.** Positivity of the Gauss weights is, on its exactness class, the same statement as W_{T_c} ≥ 0. Any node
identity is therefore a restatement of a W-value, and its sign is already consistent. A contradiction would need h of
type > 2T_c, where ℓ(h) ≠ ∫h dμ and no identity is available (Prop T). Without (Q), Theorem DC holds only on the node
span, which D_bψ is not known to meet, so there is even less. Lemma S is datum-specific, but it enters as a rewriting
of coefficients inside W(D_Λψ, D̃_Λψ). Every other datum has its own exact rewriting (twisted, Beurling-indexed,
or the recursive f^{-1}*(fL²)), and Theorem Q applies to it verbatim. S4 is lost at the use step (W3), not at the
identity.

## 5. F1, F2, M, spec

- **F1.** λ = 0 enters through (Q)/Thm G; Theorem Q's positivity is W_{T_c} ≥ 0, true at every bottom λ ≥ 0. Fails
  as a forcing mechanism.
- **F2.** Both channels are even in a → −a. Fails (W4).
- **M.** Exact, margin-free, single-T object (S5, S12 pass): not a per-window estimate, and no margin extractable.
- Spec: S1 partial, S2 ✓ (w_x ratio), S3 ✗, S4 ✓ at the identity / ✗ at the sign, S5 ✓, S7 ✗ (Euler enters as
  coefficients inside W), S8 ✗ (Type I curve passes), S12 ✓.
- Walls: W12 (primary), W3, W4.

## 6. Record and residual

- PROVED: Lemma S + correction of R162_901 L3.1 (ω ≤ 2 support is class-blind; deletion fails at N = 6, not 30);
  Theorem DC; Theorem Q (Gauss-weight positivity = W_{T_c} ≥ 0 on the exactness class, Akhiezer).
- NO-GO: the difference channel at the witness, with Selberg at ½log mn, m, n < e^{T_c}, cannot force a sign against
  w_x ≥ 0, for ζ or for any datum.
- Residual (sharp, not a route): a contradiction from quadrature needs an identity for ℓ on type > 2T_c, i.e.
  information on the contacts n ∈ [e^{T_c}, e^{2T_c}) beyond the form, which is O2202.2. Cell 6C: residual of 901
  answered NO-GO. Propose 6C → ◩ (the O2202.2 residual only).
- Add to R162_590 §1c: "Selberg difference channel at Gauss nodes — R162_2301 — node channels = W(Dψ,Dψ), W(Dψ,D̃ψ)
  (Thm DC); positivity of w_x on type ≤ 2T_c = W_{T_c} ≥ 0 by Akhiezer (Thm Q); Selberg ⟺ a = Λ but enters only as
  coefficients — W12, W3, F2".

Files edited: this file and grid/R162_2300_part7.jsonl (append).
