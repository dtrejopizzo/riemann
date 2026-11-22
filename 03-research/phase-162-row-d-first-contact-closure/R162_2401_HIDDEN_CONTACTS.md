# R162_2401 — The hidden contacts n ∈ [e^{T_c}, e^{2T_c}) as a separate object — **PARTIAL (four PROVED tools) + NO-GO (PROVED) for sign forcing and for the Theorem M attribution**

* Cell 8B/6C boundary (object: the first-contact witness F and its node system, column B/C; arithmetic:
exact values of Λ on [X^{1/2}, X) with X = e^{2T_c}, row 6). Nearest routes: R162_2202 (Thm NI, residual O2202.2),
R162_2301 (Thm Q, residual "type > 2T_c"), R162_2290 (fixes F8–F12), R160_X_C1 (Thm R, FC, G), G2_B6_R2 (Thm M,
Cor M1, Cor M2), P46 thm:margin. Walls named in advance: W12 (exact identity without sign), W3 (class blindness),
W4 (F2), W2 (Theorem M). No numerics were run; the numbers quoted come from the record (2001/2190,
R160_X_C1 §7, Zhu). No sign for ζ is claimed. No label moves. Gate 1 stays OPEN.*

Conventions. For real F ∈ L²(I_T), c_F(u) := ∫F(s)F(s+u)ds, v_n := 2Λ(n)n^{−1/2} (or the datum's own weights),
W_T(F) = A(F) + P(F) − Σ_{n≥2, log n<2T} v_n c_F(log n). Here A(F) = ∫m|F̂|²dτ/2π is the archimedean term and P(F) is
the polar term (the δ_{±i/2} of μ). The datum is admissible and ι-invariant (the F12 fix). F is even and real unless
stated otherwise; the odd case is written out (the F8 fix). F_+ := F·1_{(0,T]}, and F_−(s) := F_+(−s).

## 0. Corpus check

A grep over 03-research/phase-15x–16x and 04-papers/47 for "hidden", "X^{1/2}", "half-witness", "F_+", "tail
autocorrelation", "e^{T_c}" together with "e^{2T_c}", and "Titchmarsh" found only R162_2202 §2(b), R162_2290
("contacts in [T,2T) enter W only quadratically"), R162_2301 §4 and R162_2201 N0. No file splits W at e^{T}, writes
the hidden part as a functional of the half-witness, or proves that the witness determines the hidden comb. Theorem M
(G2_B6_R2 §3.5–3.7) is proved entirely on the zero side, and Cor M2 already states "density, not arithmetic". §4 of
this file uses that.

## 1. Failing lines first (master grid rule §0.4)

| model | T_c (record) | visible comb n < e^{T_c} | hidden comb [e^{T_c}, e^{2T_c}) | what it kills |
|---|---|---|---|---|
| Λχ₂ (χ mod 4) | ∈ [0.005, 0.38] (R160_X_C1 §7) | empty | **empty** (χ(2)=0, log 3 > 0.76) | "H ≠ 0 at a contact"; "the hidden contacts make the contact" |
| deletion Λ1_{n≥5} | ≤ 0.4608 (grid §4) | empty | **empty** (log 5 > 0.93) | same |
| two-atom Type I, s₃ = 0 | 0.5931 (2001/2190) | empty (log 2 > T_c) | **{2}**, the whole comb | "a contact needs visible primes"; every sign law on H that also holds for positive combs |
| two-atom Type I, s₃ > 0 | 0.593–0.607 | empty | {2, 3} (log 3 = 1.099 < 2T_c) | same |
| Beurling DMV | own | own 𝒩_B | own 𝒩_B | §2–§3 hold verbatim with 𝒩_B; integrality is never read |
| κ, DH, Epstein | own | own | own | §2–§3 hold verbatim |
| ζ (¬RH) | > 0.8 (Zhu) | contains 2 | contains 3, 4, … | hypothetical |

So both extremes are realised by data that have a genuine first contact with w_x ≥ 0. In the first extreme the
hidden part is zero (Λχ₂, deletion). In the other the visible comb is empty and the contact comes only from hidden
contacts (Type I). ζ lies strictly between them. Any statement that forces the sign or the size of H from the node
structure must be false for one of these data, and §3 shows it cannot be proved.

## 2. The split and its node form (task item 1) — PROVED

**Proposition 1 (split).** For F ∈ 𝒟_{T} with T = T_c,

  W(F) = V(F) − H(F),  V(F) := A(F) + P(F) − Σ_{n<e^{T}} v_n c_F(log n),  H(F) := Σ_{e^{T}≤n<e^{2T}} v_n c_F(log n).

V is the form with symbol μ^< (the comb truncated at e^{T}). It agrees with μ on every h of exponential type ≤ T,
that is on ȟ supported in [−T, T]. At a witness, **H(F) = V(F)** (and H(F) = V(F) − λ‖F‖² at a bottom eigenvector
with λ > 0).

**Node form.** (a) By Thm NI, Ĥ_x has type T, so L(x) = ∫Ĥ_x^#dμ = ∫Ĥ_x^#dμ^<. The Gauss weights
w_x = L(x)/F̂′(x) are functionals of (F, μ^<) only. (b) Under (Q) (OS-3 density; R162_2301 §3), Theorem Q and the
split give, for every h ∈ 𝒢 (type ≤ 2T),

  **H(h) = ∫h dμ^< − Σ_x w_x h(x)**,  H(h) := Σ_{hidden} v_n · ½(ȟ(log n) + ȟ(−log n)).

So the node quadrature is exact for μ^< on type ≤ T, and on type (T, 2T] its defect against μ^< is exactly the hidden
comb. At h = |F̂|² both node sums vanish, which returns H(F) = V(F).
*Proof.* (a) supp H_x ⊂ I_T. (b) Σ w_x h(x) = ∫h dμ on 𝒢 (Thm Q, under (Q)); subtract. ∎

## 3. Structure of H (task item 2)

**Theorem HV (hidden = sum channel of the half-witness). PROVED.** Let F be real, even and supported in I_T.
- (i) For T ≤ u ≤ 2T, c_F(u) = (F_+ * F_+)(u). Hence H(F) = Σ_{hidden} v_n (F_+*F_+)(log n): a *square*
  (F̂_+² on the Fourier side, not |F̂_+|²) of the right half, evaluated on the hidden comb.
- (ii) W(F) = 2W(F_+) + 2W(F_+, F_−). The self term W(F_+) contains no hidden contact, because c_{F_+} is supported
  in [−T, T]. **All hidden contacts lie in the cross term.**
- (iii) At an even witness, W(F_+) > 0 and W(F_+, F_−) = −W(F_+) < 0. Moreover
  H(F) = 2[W(F_+) + W^<(F_+, F_−)], where W^< is the cross term with the hidden comb removed.
- (iv) Under (Q), F̂_+(x) = i·S(x) at every node, with S(x) = ∫_0^T F(s) sin(xs)ds, and
  Σ_x w_x S(x)² = W(F_+) > 0. This node identity sees no hidden contact.
- (v) Odd F: c_F(u) = −(F_+*F_+)(u) on [T, 2T], and W(F) = 2W(F_+) − 2W(F_+, F_−).

*Proof.* (i) For u ≥ T, F(s)F(s+u) ≠ 0 forces s ∈ [−T, 0] and s+u ∈ [0, T]. Substitute s = −r and use evenness:
c_F(u) = ∫F_+(r)F_+(u−r)dr. (ii) F = F_+ + F_−, W(F_−) = W(F_+) by ι-invariance, and supp c_{F_+} ⊂ [−T, T]; the
cross terms carry u ∈ (0, 2T). (iii) W_{T_c} ≥ 0 on 𝒟_{T_c} ∋ F_+. If W(F_+) = 0 then F_+ ∈ E_c, but its convex
support is [0, T] ≠ I_T, which contradicts FC(i). Hence W(F_+) > 0, and 0 = W(F) gives the cross term. The formula
for H is Prop. 1 applied to the cross term. (iv) For real x, F̂_−(x) = conj F̂_+(x), so 0 = F̂(x) = 2Re F̂_+(x).
|F̂_+|² has type ≤ T, so it lies in 𝒢; apply (Q)/Thm Q. (v) Same computation with F(−r) = −F(r). ∎

**Proposition P2 (the tails carry no sign). PROVED.** Fix any real F_+ ∈ L²(0, T]. Its even and odd extensions
satisfy H(F^ev) = −H(F^odd). Whatever the datum, the tail data (F_+ on the overlapping tails [u−T, T]) therefore
fixes |H| but not its sign. The sign is fixed only by the parity of the witness. That parity is OS-2 (R160_X_C1 §8),
which is open and RH-neutral.

**Lemma U (the witness determines the hidden primes). PROVED, no (Q) needed.** Let two admissible data share A, P
and μ^<. Suppose they have first contact at the same T and a common element F of their kernels (or a common bottom
eigenvector with the same λ). Then their hidden combs coincide.
*Proof.* Put D := difference of the hidden combs, with atoms d_n at ±log n, T ≤ log n < 2T. Then (W−W′)(F, G) = 0
for all G ∈ 𝒟_T. The δ at u = 0 (from λ) is visible, so it cancels. On s ∈ (0, T) this gives Σ_n d_n F(s − log n) = 0.
Order the hidden n with d_n ≠ 0 as n₁ < n₂ < …. For s ∈ (log n₁ − T, log n₂ − T) ∩ (0, T) only n₁ survives, so
d_{n₁}F = 0 on a left neighbourhood of −T. F does not vanish a.e. there, because its convex support is I_T (FC(i)).
Hence d_{n₁} = 0. Induct on the remaining n. ∎

**Answer to item 2: NO-GO (PROVED).** The node structure is real-rootedness of F̂, density T_c/π and w_x ≥ 0. By FC,
Thm G and Thm Q it is class-level, so every datum of §1 has it. §1 exhibits witnesses with H ≡ 0 (Λχ₂, deletion) and
witnesses with H = V = A + P, the full contact (Type I, s₃ = 0). Prop P2 shows that the tails alone fix no sign.
The only exact relation available is H(F) = V(F), which is W(F) = 0 restated (W12). Lemma U says that H carries no
information beyond (F, μ^<), and it holds for every datum (W3).

## 4. Theorem M and the hidden contacts (task item 3) — NO-GO (PROVED)

The conjecture was that the doubly exponential decay λ^A_T ≤ exp(−e^{(2−ε)T}) comes from the contacts n > X^{1/2}
of the window X = e^{2T}. It is false, for three reasons.
- **Cor M2 (G2_B6_R2 §3.7).** M holds verbatim for Q_M(F) = Σ_{γ∈M}F̂(γ)F̂(−γ) for *any* symmetric multiset M in the
  strip with the counting bounds of Z, including random thinnings and finite universes. These have no prime comb at
  all, visible or hidden.
- **The scale e^{2T} in M is a zero height.** In M the cut is X_M = 2πe^{2θT−1}, the height where the Nyquist
  density θT/π of PW_{θT} meets the zero density (1/2π)log(γ/2π). That density is the Γ-factor main term of
  Riemann–von Mangoldt, which is archimedean. It coincides with the prime cut e^{2T} only because both are Fourier
  dual to type 2T. The hidden range [e^{T}, e^{2T}) is a range in n, and no step of M reads it.
- **Falsifier.** For Λχ₂ under GRH(χ₂) the analogue of Cor M1 holds (same counting, conductor shift). There the
  hidden range is nonempty for large T, but for T ≤ 0.38 no comb is present at all. The decay law does not change
  its form between the two regimes.

What does hold (exact and margin-free, so S12 ✓): for any test, W = V − H. For the M-test F_M, M says that V(F_M) and
H(F_M) cancel to within exp(−e^{(2−ε)T})‖F_M‖². It does not say that either one is small. Whether they are
individually of size ≍ ‖F_M‖² is residual O2401.1 (HEURISTIC: yes, since F_M ∈ P_T spreads over all of I_T). An
exact statement about H alone is therefore margin-free but signless (Lemma U, Thm HV). This is W12, not an escape
from M.

## 5. F1, F2, spec, walls

- **F1.** Prop 1, Thm HV (i), (ii), (iv), (v), P2 and Lemma U hold at every bottom eigenvalue λ, with W(F) = λ‖F‖²
  and a visible δ at u = 0. Only the inequality in HV(iii) uses W_{T_c} ≥ 0, and that is the definition of T_c.
  F1-blind as a forcing mechanism.
- **F2.** Under comb → −comb, H → −H. By P2 the parity flip does the same. Every statement here is either invariant
  or flips. **Fails F2** as a sign source (W4).
- **F3.** All of it holds verbatim for Λχ₂, deletion, κ, DH, Beurling (𝒩_B) and the Type I curve (W3).
- **Spec.** S1 partial (the identities are exact at λ = 0 but also hold at λ > 0), S2 ✓ (w_x is a ratio), S3 ✗ (P2),
  S4 ✗, S5 ✓, S7 ✗, S8 ✗ (Type I passes), S12 ✓.
- **Walls.** W12 (primary), W3, W4. For item 3: W2 is density-driven, as Cor M2 already records.

## 6. Verdict, record, residuals

**PARTIAL + NO-GO.**
- **PROVED (new tools):** Prop 1 (the split and the node-defect formula H(h) = ∫h dμ^< − Σ w_x h(x) on 𝒢, under
  (Q)); Theorem HV (the hidden part is the sum channel F̂_+² of the half-witness and lives only in the cross term
  W(F_+, F_−); at an even witness W(F_+) > 0 and W(F_+, F_−) = −W(F_+)); Prop P2 (parity antisymmetry of H at fixed
  tails); Lemma U (the witness together with μ^< determines the hidden comb; Titchmarsh-type induction on the left
  tail).
- **NO-GO (PROVED):** the node structure forces no sign on H (item 2). The margin of Theorem M does not come from the
  hidden contacts (item 3; Cor M2). O2202.2 is answered: at node level the hidden contacts appear only as the defect
  of the quadrature on type (T_c, 2T_c], and they equal V(F) at the witness (W12).
- **Residuals (not routes):** O2401.1 (sizes of V(F_M) and H(F_M), HEURISTIC). O2401.2 (the parity of ζ's witness is
  the only input that would fix the sign of H via P2; this is OS-2, RH-neutral). O2401.3 (Lemma U for the visible
  comb, i.e. does F with A and P determine the whole comb? The left-tail induction needs log n ≥ T, so the visible
  range is open).
- Cell proposal: 8B/6C stays ◩. Its residual O2202.2 is closed NO-GO.

Files edited: this file, and grid/R162_2300_part7.jsonl (append).
