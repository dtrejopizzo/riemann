# CA_R4_001 — L*_j(θ) at the first uncertified contact: T_j = ½log5 → T_{j+1} = ½log7 (phase 193, round R4)

Pen and paper; the only
numbers below are closed-form arithmetic (v_n, ε) and the cited certified value of thm:log5A.
ARGUED / OPEN / NO-GO. **No negative value of 𝔞_T for ζ is produced or claimed.**

## 0. Which step this is (PROVED, bookkeeping)
Contacts 2,3,4,5,7,… ; n_j = 5, n_{j+1} = 7. T_j = ½log5 = 0.8047 (λ_A ≥ 2.5·10⁻¹², thm:log5A, ball arithmetic, CITED from P46);
T_{j+1} = ½log7 = 0.9730. By SPEC_A §1.1 the atom whose row is new on R_j = (½log5, ½log7] is **5** (entered invisibly at T_j,
R186_048 L3.1), not 7; 7 enters invisibly at the endpoint T_{j+1}. (CA_R3_001 §6 names "n_j = 7" as first test case: that is the
step ½log7 → ½log8; the step asked here is the one before it.) Liu Thm B (CITED, 17/16) covers this step if accepted; the step
below is attempted *without* it. cor:margin1 needs T ≥ 1 and does **not** apply at ½log7; the only PROVED upper bound on the
slack is λ_A(½log7) ≤ λ_A(½log5) (lem:monoT).

## 1. Every object of the step, explicitly (PROVED)
- ε_j = ½log(7/5) = 0.16824; collars L = [−½log7, −½log5), R = (½log5, ½log7]; key fact √(5·7) = 5.916 < 7.
- Comb on the window: n ∈ {2,3,4,5}, v_n = 2Λ(n)n^{−½}: v₂ = log2·√2, v₃ = 2log3/√3, v₄ = ½log2·2 = log2, v₅ = 2log5/√5.
- Frozen block 𝔄_j = 𝔞_{½log5}|_{P_{½log5}∩𝒟}, ≥ 2.5·10⁻¹² (thm:log5A); parity-split (thm:parityschur), so the whole step splits into
  even/odd edge functions G(−t) = ±G(t) (PROVED: reflection preserves P_T, 𝔞_T, the collars and the Tate pair up to swap).
- Edge space ℰ_j = {α e^{t/2}𝟙_I + β e^{−t/2}𝟙_I + G : G ∈ L²(L∪R)∩𝒟, A = B = 0}, (α,β) fixed by the Tate moments of G.
- Lags seen by the coupling: for t ∈ R, s ∈ I_{½log5}, t − s ∈ (0, log√35) ⊂ (0, log7): n ≤ 5 only. For every t ∈ R all four atoms
  land inside I (t − log n ∈ I ⟺ log n ≥ t − ½log5 ∈ (0, ε], true for n ≥ 2). Edge energy: within-collar lags < ε < log2 (no atom);
  cross-collar lags ∈ (log5, log7): only the atom 5, at the boundary lag (visibility bound |c_G(log5)| ≤ ‖G‖²_{edge,ε}).
- (Ch) on [1,7): μ(4) = 0, so for 1 ≤ y < 7
  ψ(y) = log⌊y⌋! − log⌊y/2⌋! − log⌊y/3⌋! − log⌊y/5⌋! + log⌊y/6⌋!   (check y ∈ [6,7): log720 − log6 − log2 = log60 = ψ(6) ✓).
- Contact block on [5, √35): Λ(5)δ₅ − du.

## 2. Two exact facts that change the reading of CA_R3_001 (PROVED)
**Proposition R4.1 (the density half of the contact block is invisible in the coupling).** In Φ_e = Π_{P}[α𝔄e⁺ + β𝔄e⁻ − 𝒬_G − 𝒦₁G],
the −du part of d(ψ − u) and the polar part of K contribute exactly 0 (Prop Θ: they are multiples of e^{∓s/2}, annihilated by Π_P).
Hence 𝒬_G may be replaced by the pure comb Σ_{n=2}^{5}Λ(n)n^{−½}[G(s+log n) + G(s−log n)]. In particular the "ratio Λ(5) against the gap
length" of CA_R3_001 §1(b) has **no effect on Φ_e**; the gap (n_{j+1}) enters the step only through the support of G (the collar width)
and the edge energy 𝔞_{½log7}(e), never through the coupling.
**Proposition R4.2 (H1 realized exactly at this contact).** On [1,7), (Ch) together with the positions {1,…,6} is equivalent to the vector
(Λ(2),…,Λ(6)) = (log2, log3, log2, log5, 0): finite Möbius inversion is a bijection on functions of {1,…,6}, and the jump set of each
log⌊y/k⌋! is a subset of {2,…,6}. So clause (iii) of 𝒞_θ supplies, at this step, exactly the four numbers already in H_j.2 and nothing
else; the sawtooth B̃₁ enters only through the Euler–Maclaurin rewriting of log m! for m ≤ 6, which is the same finite data.
*Consequence.* At this contact the "ℤ-mechanism" has no content beyond the data; any proof of L*_j(θ) here is a proof from
(log2, log3, log2, log5) + exact K. H1 is not a risk here, it is a theorem.

## 3. The quantity whose sign is needed (PROVED reduction; sign OPEN)
Euler–Lagrange for the frozen minimizer h* = h*_{½log5}: σ(D)h* = μh* + a e^{t/2} + b e^{−t/2} on I (μ = λ_A(½log5), a,b Tate multipliers).
Rank-one part of the Schur term: ⟨Φ_e,𝔄_j^{−1}Φ_e⟩ ≥ |ℓ_e(h*)|²/μ with
  ℓ_e(h*) = (α,β)·(Tate multiplier terms of h*) − ⟨G, g*⟩,  g*(t) = Σ_{n=2}^{5}Λ(n)n^{−½}h*(t ∓ log n) + (½K₁ ⋆ h*)(t),  t ∈ L ∪ R.
Necessary condition: |ℓ_e(h*)|² ≤ μ·𝔞_{½log7}(e) for all e, i.e. the exterior field g* of h* on the collars must be, in edge-energy dual norm,
≤ √μ ≈ 1.6·10⁻⁶ (at the certified μ; smaller if μ is larger) while each of its four atom terms is O(1)·|h*| (v_n ≈ 0.7–1.4). The full
condition replaces |h*⟩⟨h*|/μ by the whole resolvent. **This is the defeating term:** the near-cancellation of the four shifted copies
of h* (plus the K₁ tail) at relative precision ≲ 10⁻⁶ on a collar of width 0.168.

## 4. Can it be done by hand in 𝒞_θ? (verdict)
Attempts and why they stop:
1. *Subspace where the step is free.* Edge functions with ℓ_e ≡ 0 would reduce L* to 𝔞_{½log7}(e) ≥ ν‖e‖². The kernel of e ↦ ℓ_e is not
   identifiable by identities (it is the annihilator of the range of 𝒯_j*, a transcendental subspace); and even there the edge energy has
   C₀ = Re ψ(¼) − logπ < 0, with m(τ) ≈ 0 near τ ≈ 1/ε, so positivity of the edge energy on width-0.168 collars is itself not an identity. NO.
2. *Lemma C.* 5 prime: cross-lags log(5/n′), n′ ≤ 4, are non-resonant (PROVED); this sorts entries but gives no inequality. NO.
3. *(Ch)/sawtooth.* Empty by Prop R4.2. NO.
4. *Rank-one budget.* Requires ℓ_e(h*) to precision √(μν) with ν ≤ λ_A(½log7)/‖e_min‖²; h* has no closed form (minimizer of a form with
   digamma symbol on a finite interval), so ℓ_e(h*) is computable only by enclosure.
**Classification of the defeating term:** prime-side and archimedean only — **not zero-side**; **not B′** (no estimate is involved: it is
an exact, finite, explicitly defined number); it is an *evaluation/precision* term: the resolvent 𝔄_j^{−1} (equivalently h* and the
spectrum near μ) applied to the four-atom exterior field. Within 𝒞_θ it is **genuinely OPEN**, and (ARGUED) it cannot be closed by
identities alone, because the class has no identity that evaluates 𝔄_j^{−1}; the only known way to decide it is certified enclosure
(the thm:log5A machinery extended to ½log7 = record item "polarcap5"), which is numerics-as-mechanism and outside the spec.

## 5. Result
- PROVED: explicit form of every object of the step; Prop R4.1 (coupling sees only the atoms 2,3,4,5; the −du/polar half of the contact
  block is exactly invisible in Φ_e); Prop R4.2 (H1 holds as a theorem at this contact); parity splitting of the step.
- OPEN (not proved, not refuted): L*_j(θ) at ½log5 → ½log7, on any subspace, with any ν.
- ARGUED NO-GO (method level, this contact): 𝒞_θ cannot prove L* here, since (iii) is empty and (i)+(ii) contain no evaluation of 𝔄_j^{−1}.
  Not a falsifier for ζ; not a proved impossibility theorem (no class-closure proof written).
No first structural proof beyond ½log5 is obtained.

## 6. Self-review
1. *Is Prop R4.1 too strong?* Π_P kills only span{e^{±s/2}𝟙_I}; Prop Θ shows the −du and polar contributions lie exactly in that span. ✓
   It does not say the gap is irrelevant: it enters 𝔞_{½log7}(e) and the collar width. ✓
2. *R4.2 generalises?* Yes for every contact: on [1,n_{j+1}) Möbius inversion is bijective, so (Ch) ≡ data always (CA_R3_001 H1 upgraded
   ARGUED → PROVED as an information statement). The proof-class distinction (operations on the factors) remains, but at small contacts
   there are no non-trivial operations to perform. ✓
3. *H2:* no Mellin step taken. ✓  *Zero information:* none. ✓  *Numerics:* only arithmetic of closed forms and the cited thm:log5A value. ✓
4. *Weak point of this memo:* the "cannot be closed by identities" claim is ARGUED; a clever identity expressing g* through σ(D)h* outside
   I (continuation of the EL equation) is not excluded — that is the one line worth trying (exterior continuation of EL, SPEC_A §3).
