# R184_016 — Selector check: is A1 weaker than RH?

**Status:** memo + audit. Pure mathematics, no numerics, no web. RH is not asserted, nor the closure of D.
Answers priority 1 of
`CROSSWORD-TO-D.md` §4.1 / §5 (U2(a), R169_000 §8).

**Verdict.** **A1 is E1.** (a) As written (F in the image of the first-contact selector) it is a statement
"about the witness": vacuous under RH and, given (Dom_θ), equivalent to "there is no witness with its quartet in the regime" (Thm 1, PROVED).
(b) Any strengthening without a witness, with a family of tests 𝔉 defined without zeros, is exactly equivalent to a zero-free
region Z(𝔉) (Thm 2, PROVED given (Dom_θ)). To exclude an unknown witness, Z(𝔉) must contain the whole regime,
and the sine-translation family already does so (Prop 3, PROVED): A1 is RH in the regime. No genuine intermediate node remains.
(Dom_θ) and (P_gap) are on the zero side, vacuous under RH, and cannot be the arithmetic input (§4).

Sources read: CROSSWORD-TO-D §1.3, §2.4–2.6, §4; R169_000 (v1 + v2); R169_091 §0–§6; R168_102 Thm 4–5; R167_101 Lemma Q,
Lemma O, Thm B, Thm C, Prop E; R168_103 (P_gap); R166_802 (N′) via R167_101 §Thm B.

---

## 1. The objects (literal quote)

**A1** (CROSSWORD §4.1):
> A1 = 𝓘_X for every X: Re𝒮 < B at every (γ,δ) ∈ Γ_S(F), F in the image of [S]

**𝓘_X** (CROSSWORD §2.4(i), witnessless version of R169 v2):
> 𝓘_X: for every F in the image of the selector [S] at scale X and every (γ,δ) ∈ Γ_S(F), the same bound holds.

with the bound from (WS*): with w = (e^{−iγ·}g) ∗ ǩ, with transform G(s+γ)²k(s) ≥ 0, Y = Xe^{Δ},
Re Σ_{n≤Y} Λ(n) n^{−½+iγ} w(log n) < (1−θ) c_Θ |G(t)|² |k(−iδ)| − ¼E_K, t = γ − iδ.

**Selector [S]** (R169_000 §5): "the map window ↦ (T_c, F, X, γ_q, w) of the first contact (R163_401 §2, R165_202 flow).
It is deterministic and depends only on Λ in the window and on the archimedean term." Corrected by R169_091 Prop 3.1: γ_q is **not** a
function of the window; [S] delivers F, G, nodes x_k and the set

**Γ_S(F)** (R169_091 §3): Γ_S(F) := {(γ,δ) : 0 < δ < ½, cos 2Φ_F(γ,δ) < 0, (γ,δ) in the regime of Thm B (Dom_θ, Prop E, B > 0)},
Φ_F(γ,δ) = arg G(γ+iδ).

**𝒮 = 𝒮_X(γ)** = Σ_{n≤Y} Λ(n) n^{−½+iγ} w(log n), Y = Xe^Δ, X = e^{2T}. By R169_091 Prop 5.2 (PROVED), if Y < X² the tail
Λ|[X,Y] is the sieve-of-Eratosthenes image of the window: at fixed X, 𝒮 is a function of the window.

**B** = (1−θ)c_Θ|G(t)|²|k(−iδ)| − E_K/4, E_K := 2C_S(γ)(2T+Δ)‖G‖²_∞‖k‖₁ + |𝔭_K| + |ε_K| + |ε′_K| (R167_101 Thm B).
Only an upper bound on B is available (R169_091 §1 step 4); B > 0 requires 2T+Δ ≲ 11.4 c_Θ e^{δΔ}.

**Uniformity in X:** "for every X", i.e. for every first-contact scale.

Notation: Reg := {(γ,δ): regime of Thm B, B > 0}. Reg⁺ := {(γ,δ) ∈ Reg : E_K < 2(1−θ)c_Θ|G(t)|²|k(−iδ)|}, the
subregime where B > E_K/4 (necessary for the direction RH ⟹ bound, Lemma 0).

## 2. Two base lemmas

**Lemma 0 (the bound of A1 under RH). PROVED** (with R167_101 Lemma O, PROVED-CITED + PROVED).
For every real-rooted G of type T, every k of §1 of R167_101, and every (γ,δ) ∈ Reg⁺: if ξ has no zeros off the line in
the localization zone of K, then Re 𝒮(γ) < B(γ,δ).
*Proof.* Identity (2.1) of R167_101 (Thm A, explicit formula for Ψ = G(·+γ)²k) gives
4Re𝒮 = ((L/π)I − O_K) + |Q_K| − R_K + 𝔭_K + ε_K. Without zeros off the line in the zone, Q_K = R_K = 0. Lemma O bounds the first
bracket by the counting part of E_K; the remaining terms are inside E_K. Thus 4Re𝒮 ≤ E_K < 4B on Reg⁺. ∎
*Note.* On Reg \ Reg⁺ the bound of A1 **can fail even under RH** (nothing prevents 4Re𝒮 ∈ [4B, E_K]); there A1 would be stronger
than RH, not weaker. From here on A1 is read on Reg⁺.

**Lemma 1 (Thm B does not use the contact). PROVED** (reading of the proof of R167_101).
Let G be any real, entire, real-rooted function of type T (not necessarily a witness) and ρ = ½+δ+iγ a zero of ξ with
(γ,δ) ∈ Γ_S(F) ∩ Reg and (Dom_θ) for that test. Then Re𝒮(γ) ≥ B(γ,δ).
*Proof.* Lemma Q is an evaluation of the quartet's contribution in the explicit formula; it uses only cos 2Θ_q < 0 (the cone),
which is the condition cos 2Φ_F < 0 of Γ_S, plus the phase rotation (ii) that chooses k as a function of Θ_q. Lemma O is unconditional.
(Dom_θ) controls R_K. The proof of Thm B combines only these three pieces. The first contact only entered in R163_401 (3.1)
to **guarantee the existence** of a quartet in the cone, not in the inequality. ∎

## 3. Theorems

**Theorem 1 (A1 literal is a statement about the witness). PROVED** (given (Dom_θ) at the witness).
Let A1 be as in §1, with F in the image of the first-contact selector. Then
 (i) RH ⟹ A1, vacuously;
 (ii) A1 ⟺ ¬[there exists a first contact whose lowest quartet t_q satisfies (γ_q,δ_q) ∈ Reg].
*Proof.* (i) Under RH, W_T ≥ 0 for every T with λ^W_T > 0 (Weil; CITED), there is no first contact and the image of [S] is empty.
(ii) ⟸: if there is no contact, (i). If there is a contact with t_q ∉ Reg, then (γ_q,δ_q) ∉ Γ_S(F) … but A1 requires the bound
over all of Γ_S(F), not just at t_q: here the direction ⟸ also needs the bound to hold on Γ_S(F) \ {t_q}, which by Lemma 0 holds on
Reg⁺ away from the zone of other quartets. Read on Reg⁺ and with (Dom_θ), the direction ⟸ is PROVED; without those readings, A1 is
**stronger** than the negation of the witness (which does not help). ⟹: if there is a contact with t_q ∈ Reg, step 2 of R169 §1 (PROVED,
R165_201) gives cos 2Φ_F(t_q) < 0, so (γ_q,δ_q) ∈ Γ_S(F); Lemma 1 gives Re𝒮(γ_q) ≥ B, against A1. ∎
*Consequence.* Literal A1 belongs to the "witness" row of the E1 cluster (CROSSWORD §1.3, Quantifier Warning): its
hypothesis ("F in the image of [S]") is nonempty if and only if ¬RH (Weil). Every proof of literal A1 is a proof that the
object F, which exists only under ¬RH, does not exist with t_q ∈ Reg. **It is E1 localized to the regime.** The "selector image" is not
a set of frequencies of ζ under RH: it is ∅.

**Theorem 2 (dichotomy for every witnessless strengthening). PROVED** (given (Dom_θ) uniform in 𝔉).
Let 𝔉 = ⋃_T 𝔉_T be any family of real real-rooted G of type T, defined without zeros (e.g. lowest eigenvectors of W_T
for every T, or all type-T tests), and let A1^𝔉: for every T, every G ∈ 𝔉_T and every (γ,δ) ∈ Γ_S(F) ∩ Reg⁺, Re𝒮 < B.
Put Z(𝔉) := ⋃_{G∈𝔉} Γ_S(F) ∩ Reg⁺ ⊂ {(γ,δ)}. Then
  RH ⟹ A1^𝔉 ⟹ ξ has no zeros ½+δ+iγ with (γ,δ) ∈ Z(𝔉).
Moreover, if ξ has no zeros off the line in a localization neighborhood of Z(𝔉), A1^𝔉 holds. That is, modulo (Dom_θ),
**A1^𝔉 ⟺ "Z(𝔉) is a zero-free region"**.
*Proof.* First arrow: Lemma 0. Second: if there were a zero at (γ,δ) ∈ Γ_S(F) ∩ Reg⁺, Lemma 1 gives Re𝒮 ≥ B. Converse: Lemma 0
localized. ∎
*Consequence (the dichotomy sought).* (a) If Z(𝔉) does not contain the witness's position (γ_q,δ_q), A1^𝔉 does not exclude it: useless.
(b) If it does contain it, A1^𝔉 at that point **is** the force-(N′) bound equivalent to the absence of that zero (R166_802 Thm 2,
transfer). Since (γ_q,δ_q) is external to the window (R169_091 Prop 3.1, PROVED: the window does not determine γ_q), the only
way to capture the witness without knowing it is Z(𝔉) ⊇ the entire Reg⁺.

**Proposition 3 (the translation family sweeps the regime). PROVED.**
Let 𝔉_T^{sin} = {G_a(z) = sin(T(z−a)) : a ∈ ℝ}. Each G_a is real, entire, real-rooted, of type T (Paley–Wiener), and
Γ_S(F_a)_δ ⊇ {|tan T(γ−a)| < tanh Tδ} (R169_091 Prop 3.2(c), exact for sine type). Taking a = γ: γ ∈ Γ_S(F_γ)_δ for every δ > 0.
Hence Z(𝔉^{sin}) = Reg⁺ (restricted to sine-type parameters). ∎
*Corollary.* A1^{𝔉^{sin}} ⟺ (modulo (Dom_θ)) no zero of ξ in Reg⁺: E1 in the regime. With (P_gap) for small y and Reg⁺ for
large y, it is D itself. This closes U2(a) of CROSSWORD §4.2 **in sense (a)**: the relevant image is dense.

**Proposition 4 (the minimal family: lowest eigenvectors). OPEN, ARGUED dense.**
For 𝔉_T = {lowest eigenvector of W_T} (exists for every T, no zeros), the union over T in the bounded range of Reg
(2T+Δ ≲ 11.4c_Θe^{δΔ}) of the nodes x_k(T) moves continuously with T, with speed ≈ x_k/T at height x_k; for x_k ≫ 1
it sweeps intervals of length ≫ 1 (ARGUED; requires simplicity of the eigenvalue). Even if it were not dense, Thm 2 applies: A1^𝔉
would be a comb-shaped zero-free region, which does not contain an arbitrary witness, case (a): **useless**.

**Theorem 5 (no escape via uniformity in X nor via the size of B). PROVED.**
(i) Uniformity in X adds no content: at fixed X, A1^𝔉 is a finite computation (Eratosthenes, R169_091 Prop 5.2) and its truth
is equivalent (Thm 2) to the absence of zeros in Z(𝔉) ∩ {scale X}; "∀X" is the union of these regions. An "on-average-in-X" version
(Theorem M / W2: average ⇏ uniform per window) does not exclude a witness living at one scale, case (a).
(ii) B is polylogarithmic (R169_000 §2), hence stronger than the bound X^{Θ−½+ε} that (N′) declares necessary; weakening B to
X^η with η < δ still excludes it (Thm C), and with η ≥ δ it does not (Thm C, amplification ceiling): NO-GO below the
strength of (N′). At no point in the useful range is the bound weaker than "there is no zero there".

## 4. (Dom_θ) and (P_gap)

**(Dom_θ)** (O167.101.1, R167_101 l.142, literal): "(Dom_θ) S^+_K ≤ θ|Q_K| for some θ < 1"; "other quartets near γ_q outside
their cones carry ≤ θ|Q_K|". **Zero side.** Under RH it is vacuous (S^+_K = 0 = Q_K; the version of Lemma 1 is read without a quartet).
M_m satisfies it or violates it at will by placing neighboring quartets. It does not use Λ: it cannot be the arithmetic input. Its conjunction
with PROVED tools: with Thm B it gives the exclusion criterion; with Thm 2 it gives "A1^𝔉 ⟺ free region". Nothing more. **OPEN, technical.**

**(P_gap)** (R168_103 l.48, literal): "For every off-line zero ρ* with δΛ < y₀ and γ* > H, the interval |x − γ*| ≤ c₁/Λ
contains an on-line zero γ with |γ − γ*| ≥ c₂ δ (with c₁, c₂ absolute; c₂ ≈ 4 suffices in the deep regime)."
**Zero side**, quantified over zeros off the line: vacuous under RH, violable by M_m (R168_103 §3). With R168_103
(PROVED) it gives (★_loc) ⟹ local (★_cell) in y < y₀, i.e. it excludes the small-y regime. **OPEN.** Its form is the same
"Quantifier Warning": a statement about an object that exists only under ¬RH.

**Conjunction.** A1 ∧ (Dom_θ) ∧ (P_gap) ⟹ D (CROSSWORD §4.1). By Thm 1–2, A1 is "no zeros in Reg⁺"; (P_gap) is "no zeros in
y < y₀ with an adverse neighborhood". The conjunction is RH split into two regions plus a domination hypothesis. **E1.**

## 5. Crossword update

- Route A of CROSSWORD §4.1: **A1 moves from "OPEN — THE square" to E1** (literal Thm 1; strengthened Thm 2 + Prop 3). Route A
  reduces to the E1 cluster: no intermediate node.
- U2 of §4.2: resolved in sense (a) for 𝔉^{sin} (Prop 3); for the eigenvector family, Prop 4 OPEN but irrelevant
  (case (a) of Thm 2).
- **What replaces A1:** nothing within the witness architecture. The only blank square without a meta-theorem
  covering it remains **O166.802.1** (nonlinear inequalities on Λ, multiscale, not of power-family type), which is now the
  only candidate of the minimal crossword. Every inequality linear in Λ evaluated on tests of the form G(·+γ)²k falls into Thm 2.

## For the audit

1. **Lemma 1** is a reading of the proof of R167_101 Thm B: verify that (3.1) of R163_401 is used only for the existence of the
   quartet in the cone. If Lemma O depended on the witness's normalization (|w| ≤ w(0)), check that it also holds for G_a.
2. **Thm 1(ii) ⟸** needs A1 to be read on Reg⁺ and Lemma 0 to be localized; on Reg \ Reg⁺ A1 can be false under RH. Should the record
   redefine A1 with Reg⁺? Proposal: yes.
3. **Prop 3** uses exact sine type; G_a is not a witness of anything. That is what is wanted (witnessless strengthening); but
   (Dom_θ) for G_a with arbitrary zeros is as OPEN as it is at the witness.
4. **Thm 2** depends on (Dom_θ) uniform in 𝔉: without it, the arrow A1^𝔉 ⟹ free region fails where there are clusters of quartets;
   then A1^𝔉 is even less useful, not more.
5. **Thm 5(ii)** cites Thm C as the ceiling: confirm that η < δ is the exact condition (R167_101 l.173–191).
6. Not asserted: RH, closure of D, nor that O166.802.1 has a candidate.

## Note (R184_094)

* Thm 1(ii)/Thm 2: what is proved is a sandwich zero-free(N(Z)) ⟹ A1^𝔉 ⟹ absence of zeros in Z(𝔉); «zero-free region» → «absence of zeros in Z(𝔉)». ⟸ CONDITIONAL.
* Prop 3: only for 𝔉^{sin}; G_a is not in the image of the selector; withdraw «A1 is RH in the regime» and «closes U2(a)».
* Thm 5(ii): R166_802 Thm 3 is asymptotic (global Θ); withdraw «B polylog ⟺ (N′)»; the condition of Thm C is η < α ≤ δ.
* «Only blank square» holds only on route A; still open are B1=O2601.1, B2=L8, C_B, C_T, (M)/(E′_loc), C1(O(1)).
