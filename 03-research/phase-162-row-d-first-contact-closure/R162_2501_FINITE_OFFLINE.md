# R162_2501 — The dichotomy m<∞ ⟹ m=0 (Conjecture C_B) against the first-contact machinery — **NO-GO (PROVED) for (a) via first contact / nodes / finZ / Theorem M; PARTIAL: two PROVED tools (exponent law, class obstruction); (b) the exact gap stated**

* Cell 8F/4E/7E (master grid ranking #1). Nearest routes: 37/112 Thm 2.3 (LP-112 ⟹ m∈{0,∞}), 37/113
(LP-113, "SIN PRECEDENTE"), 38/115 (audit: survives with corrections; non-equivalence to RH NOT-REFUTED, not proved),
38/116 (Stepanov Thm 5.2 survives), 34/94 §11 (C_B, Lemma 11.4 Blaschke form), P19 Hyp D + def:wall (RSRP),
P30 (L8 + LP-112), P33 (A ⟹ LH; anti-recurrence Prop.: conditionally on A, LP-112 ⟺ RH), P46 thm:finZ, thm:margin,
lem:contA, R162_2202 Thm NI, R162_2301 Thm Q, R162_2401b. Walls named in advance: W2 (Theorem M), W3 (class
blindness), W1/E1. Pure mathematics, no numerics. No label moves. Gate 1 stays OPEN.*

Conventions (as in R162_2401). I_T = [−T,T]; Φ_F(s) := ∫F(t)e^{(s−½)t}dt; for real F in the form domain of
𝔞_T on the primitive space P_T (orthogonal complement of e^{±t/2}), 𝔞_T(F) = Σ_ρ Φ_F(ρ)Φ_F(1−ρ) (P46 lem:roughEF;
polar term vanishes on P_T); λ_A(T) = min spec H_T. Hypothesis H(m): exactly m ≥ 1 off-line quartets
{½±β_j±iγ_j}, 0<β_j<½, counted with multiplicity; β* := max β_j.

## 0. Corpus check

grep "C_B", "LP-112", "finitely many off-line", "Hypothesis D", "κ<∞" over 03-research, 04-papers, OPTIONS.md,
NO-GO-LIST.md. Sources found: 34/94 §§9–12 (C_B formulated; Thm 9.2 "no known argument"; Lemma 11.4 Blaschke
reformulation), 37/109–113, 38/115–116, P19 (Hyp D, lem:noEuler, RSRP), P30, P33 (A ⟹ LH; chain
RH ⟹ (m<∞) ⟹ A ⟹ LH), OPTIONS.md row "C_B: OPEN, no known bridge". **No file compares λ_A(T) with H(m), writes the
growth rate of −λ_A under finiteness, or tests the first-contact tools against a model with exactly finitely many
off-line zeros.** §§2–4 are new; §5 re-reads the old record.

## 1. Failing lines first

| model | #off-line zeros | shares with ζ | verdict for a C_B argument |
|---|---|---|---|
| DH | ∞ (Davenport–Heilbronn; ≫T) | FE, arch side, zero-side identity | C_B holds vacuously (m=∞). Not a counterexample; kills any argument that "finiteness" is used only through FE-level identities (then DH-type finite perturbations, row M_m below, also pass). |
| Λχ₂ | conjecturally 0 | Euler, integrality | not a falsifier (the analogous C_B is expected true); it separates nothing here. |
| deletion Λ1_{n≥N}, amplification, κ/finmod | **same as ζ**: ζ_a = ζ·exp(finite Dirichlet polynomial), a nonvanishing entire factor | Λ≥0, support, zeros | They have finitely many off-line zeros iff ζ does. But λ_A<0 from T≈0.6 (deletion) with no zero moved: **negativity of λ_A is not a zero-side signal outside the atomic Euler datum.** Negativity is O_N(1) (finite-rank change), not exponential. |
| Beurling DMV | ∞ (curve σ=1−c/log t) | Λ≥0, Euler, Λ*1=log | vacuous for C_B. |
| **M_m (constructed, §3)** | κ(ζ)+4m; **exactly m under RH** | everything class-level: FE symmetry, zero-side identity, closed semibounded form, compact resolvent, continuity in T, first contact, witness, nodes, finZ, Theorem M | **the decisive falsifier** (Thm 3). |

Explicit finite model (answer to "construct one"): pick m off-line points ρ_j = ½+β_j+iγ_j and 2m on-line zeros
½±iγ_k^0 of ζ, all with heights > H_PT, and set
ξ_m(s) := ξ(s) · Π_j (s−ρ_j)(s−ρ̄_j)(s−1+ρ_j)(s−1+ρ̄_j) / Π_k (s−½−iγ_k^0)(s−½+iγ_k^0).
ξ_m is entire of order 1, real, ξ_m(s)=ξ_m(1−s), and its off-line set is Z_off(ζ) ∪ {m quartets}. (For an
unconditional example with exactly m, apply the same rational factor to any entire even function with provably
only real zeros, e.g. Pólya's ξ*; it has no explicit formula with primes, so it is only a sanity model.)

## 2. PROVED tool: the exponent law under H(m)

**Proposition 1.** Under H(m) there are constants c, C, T_1 > 0 depending on the configuration such that for T ≥ T_1
  −4 Σ_j sinh(2β_jT)/β_j ≤ λ_A(T) ≤ −c e^{2β*T} + C.
Hence lim_{T→∞} (1/T) log(−λ_A(T)) = 2β*.

*Proof.* Lower bound. For ρ=½+z, z=β+iγ, set A=Φ_F(½+z), B=Φ_F(½−z). The quartet contributes 4Re(AB); on-line zeros
contribute |Φ_F(½+iγ)|² ≥ 0. Cauchy–Schwarz on I_T: |A|,|B| ≤ ‖F‖(∫_{−T}^{T}e^{2βt}dt)^{1/2}, so |AB| ≤
‖F‖² sinh(2βT)/β. This holds on the core C_c^∞(I_T)∩P_T, where the explicit formula is classical; the core is dense
in form norm and 𝔞_T is closed, so the infimum over the core is λ_A(T).
Upper bound. Fix j with β_j=β*. Let F(t)=φ(t−T+1)cos(γ_jt+θ)+φ(−t−T+1)cos(−γ_jt+θ) (even), φ∈C_c^∞(0,1) real.
Then A=B=½e^{β*(T−1)}[e^{iθ}φ̂-value + O(e^{−2β*T}·…)] ; choose θ with arg A = π/2 + o(1), so 4Re(A²) ≤
−c₀e^{2β*T}. Impose finitely many linear conditions on φ: Φ_F(0)=Φ_F(1)=0 (so F∈P_T), and φ̂ vanishing at the
shifted points of the other quartets with β_i=β* (distinct exponentials are linearly independent on [0,1], so
these conditions leave A≠0). Other quartets then contribute O(e^{(β*+β_i)T}) with β_i<β*, on-line zeros contribute
Σ_γ |φ̂(γ−γ_j)|² ≤ C(γ_j), and ‖F‖ is T-independent. □

**Proposition 2 (unconditional floor).** λ_A(T) ≥ −Σ_{log n<2T} v_n − O(1) = −4e^{T}(1+o(1)).
*Proof.* |c_F(u)| ≤ ‖F‖², the archimedean term is bounded below by −O(‖F‖²), Chebyshev. □
(In λ_A language this is Θ ≤ 1: exponent ≤ 1.)

## 3. NO-GO theorems for route (a)

**Theorem 1 (size channel, both directions).** No contradiction with H(m) can come from the size of λ_A.
(i) Theorem M (thm:margin, and the refined λ_A ≤ exp(−e^{(2−ε)T})) is an *upper* bound; H(m) makes λ_A more negative
(Prop 1). Same direction: consistent. The double-exponential decay is a statement about the positive margin in the
RH world and says nothing about how negative λ_A may be.
(ii) The only lower bound is Prop 2 (exponent 1). H(m) gives exponent 2β* < 1. Consistent.
(iii) The bound that would contradict H(m), λ_A(T) ≥ −e^{o(T)}, is by Prop 1 *equivalent under H(m) to m=0*: it is
C_B restated (circular, E1 in exponent form). "Finite exponential sum vs double exponential" was the wrong
comparison: the finite sum governs −λ_A, Theorem M governs λ_A⁺; they never meet.

**Theorem 2 (finZ, nodes).** (a) finZ concerns a finite *total* zero multiset carrying a flat-top certificate.
Under H(m) the zero set is infinite and f_w(τ)=Σ_on ŵ(τ−γ)+Σ_off ŵ(τ−γ∓iβ); the off-line part is a perturbation of
size e^{β U} (U = supp w), not a certificate. finZ has no hypothesis to act on. (b) Thm NI/Thm Q live at the first
contact T_c. Under H(m), T_c<∞, the witness exists and Q holds at T_c (it is W≥0 in type ≤2T_c, true by definition
of T_c); for T>T_c there is no witness. Nothing is overdetermined: the finitely many quartets only fix T_c.

**Theorem 3 (class obstruction by M_m).** Let 𝒫 be any property shared by ζ and the model M_m of §1 (datum = Λ-comb
+ arch + the finite exponential density E_m(u)du, with Δ_T(F)=∫c_F E_m = Σ_j 4Re(A_jB_j) − Σ_k 2|Φ_F(½+iγ_k^0)|²,
a finite-rank, T-continuous form perturbation). If an argument proves 𝒫 ∧ κ<∞ ⟹ κ=0, then applied to M_m it gives
κ(M_m)=∞, i.e. κ(ζ)=∞. So such an argument proves C_B only by *disproving RH*.
Class properties preserved by M_m: closedness, semiboundedness, compact resolvent, continuity of λ_A (lem:contA
proof is perturbation-stable), existence of first contact (λ_A>0 for small T is unaffected at heights >H_PT up to
an O(T·e^{−…}) change; λ_A→−∞ by Prop 1), witness and node quadrature (Q is a statement about PSD of the form in a
type class), finZ (datum-free), Theorem M (its proof uses only zeros ≤ H_PT and the e^{T|β|} bound).
The single property M_m lacks: **the arithmetic side of ζ is arch + pure atoms at log n; M_m has a nonzero
absolutely continuous exponential density.** Every tool of rounds 22–24 is class-level in the above sense (W3).

*Killers:* W2 (Thm 1), W3/F3 (Thm 3), E1 (Thm 1(iii)).

## 4. What a C_B proof must do (spec, sharper than S7/S11)

Prop 3 (restatement, PROVED, from P19 lem:noEuler + 94 Lemma 11.4). Under H(m), ξ_0 := ξ/P_{4m} is RH-type with datum
Λ-comb − E_m. Hence C_B ⟺ *no nonzero off-line-type finite exponential density E can be added to the atomic Λ-comb
while keeping a real zero measure.* For each fixed candidate Z_off this is Weil positivity ∀T for ξ_0 (E1 per
configuration). So a C_B proof must be an incompatibility between **atomicity at log n** (integrality of ℤ + exact
values, the Euler/Landau input of P19 lem:noEuler) and **an a.c. component E_m ≠ 0 of growth e^{β*u}, frequencies γ_j**,
proved *without* passing through positivity of the companion form. Landau's theorem (lem:noEuler(2)) is the only
known incompatibility and it lands on ζ_0, which is allowed to be non-arithmetic: not a contradiction.
In ψ language: ψ(x) = x − 2Re Σ_j x^{ρ_j}/ρ_j + O(√x log²x) (von Koch's argument survives the finite exceptions). The
main term is a finite almost-periodic sum of size x^{½+β*}; monotonicity and prime-power support of ψ do not see it
(its derivative is O(x^{β*−½}) = o(1)). No elementary contradiction.

## 5. (b) Exactly what remains between C_B and RH

1. RH ⟺ C_B ∧ (κ<∞) (Doc 109 §4.5). C_B alone is consistent with κ=∞ (DH-like state) and implies nothing
   unconditional.
2. The other half, finiteness κ<∞ (Diana L8 / A), is far stronger than any theorem: κ<∞ ⟹ Θ<1 (quasi-RH, a zero-free
   half-plane Re s>1−δ) and κ<∞ ⟹ A (I<∞) ⟹ LH (P33 (iv)). So even a proof of C_B leaves a gap of at least
   quasi-RH ∧ Lindelöf strength.
3. In λ_A language: let e := limsup (1/T)log⁺(−λ_A(T)) ∈ [0,1] (≤1 by Prop 2). RH ⟺ e=0 and λ_A≥0 ∀T (the second part
   is E1). Under κ<∞, e = 2β* (Prop 1). Open: does e<1 imply Θ<1 without finiteness (O2501.2)? The Prop 1 upper
   construction is not robust to infinitely many interfering zeros near Re s = Θ.
4. The LP-112 channel dissolves under finiteness: P33 anti-recurrence (conditionally on A, sequential
   self-approximation ⟺ RH), and 38/115 (under H(m) the witness set above the threshold is empty, a theorem).
5. Non-equivalence of C_B with RH remains NOT-REFUTED, not proved (38/115 correction applies to C_B too).

## 6. Residuals

- **O2501.1** (live, 8F/4E): an incompatibility "atomic Λ-comb vs nonzero a.c. finite exponential density" that does
  not pass through Weil positivity of ξ_0. Only honest shape of a C_B proof. No candidate mechanism known; Beurling
  DMV shows Λ≥0 + Euler + Λ*1=log does not suffice (infinitely many off-line zeros there, so it is vacuous for C_B, but
  it rules out tools blind to ℤ).
- **O2501.2**: e<1 ⟹ Θ<1? (would give a λ_A-reading of quasi-RH; does not touch C_B).

## 7. Verdict

(a) **NO-GO (PROVED)** for proving C_B with first contact + NI/Q + finZ + Theorem M: size channel wrong-directional
(Thm 1), finZ/nodes vacuous under H(m) (Thm 2), and the whole toolkit is class-level, so it would prove C_B only by
proving κ(ζ)=∞ (Thm 3). PROVED tools: Prop 1 (exponent law 2β*), Prop 2 (floor exponent 1), Prop 3 (restatement).
(b) Gap stated in §5. Ranking #1 residual narrows to O2501.1. No label moves.
