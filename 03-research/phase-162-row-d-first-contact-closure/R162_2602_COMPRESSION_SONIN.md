# R162_2602 — Cell 8D: the Connes–Consani Sonin count and PATH-TO-D (ii) (compression) — **NO-GO (PROVED)**, with one PROVED dictionary

Note. Pure mathematics, no numerics, no parallel passes. Cell **8D** (no arithmetic × spectrum).
The nearest routes are the two live residues of 8D in R162_2300 §2: 115_15 (CC count #{λ_j(K_I)>1}) and
PATH-TO-D §3 (ii).
Inputs: R162_2300 §0, §3, §7 (S1–S12); 115_15; PATH-TO-D (ii); R162_1201 §1–2; R162_1301 §1 (L1–L4); R162_504 Thms 1–2;
R162_902; R162_2501a/b; R157_002 §4–5 (Pontryagin κ, Paper 11, C_B); Paper 47 eq:form, thm:parityschur, prop:polarcap,
lem:contA, thm:finmod.

**Labels.**
- Thm 1 (the carrier exists and is canonical: A_T = P_I S P_I with S the full-line Weil operator; S = S_0 − 2·sym(ℓ_+⊗ℓ_−)) PROVED. **Dictionary** (explicit formula + support). Not new in content; new as the stated (ii) answer.
- Thm 2 (compression obstruction: no S ≥ 0 on any Hilbert space containing L²(I_T) isometrically, for T with μ_1(A_T) < 0; n₋(S) ≥ n₋(A_T)) PROVED. Trivial, recorded as the line.
- Thm 3 (codim-2 version: "A_T|P_T is the compression of some S_+ ≥ 0 with A_T − P S_+ P of rank ≤ 2 and vanishing on P_T" ⟺ λ_A(T) ≥ 0 (with the kernel/Schur clause)) PROVED. **Restatement, E1.**
- Thm 4 (semilocal CC carrier = the same S, truncated; no independent positivity; blind to deletion) PROVED. **NO-GO.**
- Def 5 + Thm 6 (the Sonin count N(T) := n₋(A_T|P_T): nondecreasing, right-continuous jump structure, first jump at T_*, N(T) ↑ 2κ_off; CC's count = N(T) + δ(T), δ ∈ {0,1,2}) PROVED (the limit uses the corpus Pontryagin identity, Papers 08/18, and R162_2501a's two-bump construction).
- Cor 7 ("count stays at CC's value ∀T" ⟺ RH, E1; "sup_T N(T) < ∞" ⟺ finitely many off-line zeros — genuinely weaker than RH, but it is exactly the 8F residue m<∞ / Pontryagin κ<∞, already EXCL in R157_002 §4) PROVED.
- Prop 8 (falsifier transport: deletion → N unbounded; two-atom curve → N(T) ≳ cT; κ/finmod → N ↑ 2·(#off-line), so no a≥0-blind argument bounds N) PROVED (Prop 8(b) uses the Landau–Widom/Szegő count for truncated convolutions, standard).
Gate 1 OPEN. No label moves. Cell 8D: both residues closed → 8D becomes ◩ (dead with residue = 8F m<∞).

## 0. Corpus check (done before building)

grep "compression", "Sonin", "Pontryagin", "n₋", "κ_off", "semilocal", "R_Λ", "prolate" in phases 115, 150–162, R160_S1–S5:
- CC's Thm 6.11 mechanism and the unexamined count: 115_15 §3–4 (read). Beyond |I| ≤ log 2 their N_I formula is undefined (115_15 §2).
- Pontryagin index κ = n₋ of the complete Weil form = off-line zeros; "κ<∞ ⟹ κ=0" = Conjecture C_B, route EXCL (R157_002 §4; Paper 11: near-null space of the pencil is infinite-dimensional, F3). Bridge κ(Q) = ind₋(H_C) (Paper 25): EQUIV (R157_002 §5).
- Two-bump test at ±T with frequency γ_j (one negative direction per off-line quartet in a window): R162_2501a upper bound.
- The rank-2 Tate correction W_T − a_T = 2AB: thm:parityschur(o) (R162_504 §1).
New here: the per-window count N(T) with monotonicity and first jump = first contact (Thm 6); the identification of the CC count with N(T)+δ(T); the answer to (ii) as a statement with its obstruction (Thms 1–4). None is a closing identity.

## 1. Falsifier lines first

Any construction in 8D must, before a proof is written, do the following.
- **(L-F1)** Use λ = 0 as the *bottom* of A_T|P_T. A spectral count read off an identity valid at every eigenvalue proves nothing (R162_1301 L1).
- **(L-F2)** Be orientation-sensitive. n₋ is (under A → −A it becomes n₊), so a count passes F2 *as a statement*. A proof through the square of (PC) does not.
- **(L-del/κ)** A positivity S_+ ≥ 0 or a count bound built from "CM archimedean kernel + comb with a ≥ 0 + Perron" also holds for the deletion and κ/finmod models (R162_504 Thm 1, "F3 line"). Those models have first contacts, so the construction must fail for them.
- **(L-2atom)** The two-atom comb (s₂, s₃) coincides with ζ for T < ½log 4 at s = (1,1) and has a Type I first contact near s₂ ≈ 0.9998 (R162_2001, uncertified). A weight-blind spectral criterion is killed there (W3/S8).
- **(L-M)** No finite zero set and no numerical margin (S12, finZ). A count "= 1 at |I| = log 2" (CC, numerical with rigorous enclosure) is a margin statement at one window and cannot be propagated in T without a mechanism.

## 2. PATH-TO-D (ii): the carrier operator

Notation: I = I_T = [−T,T]. ℓ_±(F) = ∫F e^{±t/2} (so A = ℓ_+, B = ℓ_−, and ℓ_ev, ℓ_odd are their half-sum and half-difference). P_T = ker ℓ_+ ∩ ker ℓ_−.
a_T is Paper 47 eq:form, and λ_A(T) = inf a_T on the unit sphere of P_T.

**Theorem 1 (the carrier).** Let 𝒟 be the space of F ∈ L²(ℝ) with compact support in the form domain. Define on 𝒟 the full-line Weil form
 s(F) := m-part − Σ_{n≥2} (Λ(n)/√n)·2c_F(log n),  c_F(x) = ∫F(t)F(t−x)dt,
i.e. the convolution form with distributional symbol σ = m(τ) − Σ_n 2Λ(n)n^{−1/2}cos(τ log n). Then:
(a) s(F) = a_T(F) for every F supported in I_T, so A_T = P_I S P_I exactly as forms, where S is the closed form s. The comb truncation N_T is automatic: c_F(log n) = 0 for log n > 2T.
(b) (explicit formula) s(F) = S_0(F) − 2ℓ_+(F)ℓ_−(F), with S_0(F) := Σ_ρ F̂(γ_ρ)F̂(−γ_ρ) (symmetric summation, ρ = ½+iγ_ρ).
(c) S_0 ≥ 0 on 𝒟 ⟺ RH (Weil). ℓ_± are not L²(ℝ)-bounded, so the rank-2 term exists only on compactly supported (or e^{|t|/2}-weighted) carriers.

*Proof.* (a) Paper 47 eq:form is the restriction of this form (the comb terms with log n > 2T vanish by support). (b) is Weil's explicit formula applied to g = F * F̃, ĝ(z) = F̂(z)F̂(−z), with ĝ(±i/2) = ℓ_+ℓ_−. This is the identity W_T = a_T + 2AB of thm:parityschur(o). (c) is Weil's criterion. ∎

So the self-adjoint carrier asked for in (ii) exists, is explicit, and is unique up to the choice of how the full line is regularised. The question is only whether some *positive* S is available.

**Theorem 2 (compression obstruction).** Let H ⊃ L²(I_T) isometrically, P the orthogonal projection, and S a self-adjoint semibounded form on H with A_T = P S P on the form domain. Then n₋(S) ≥ n₋(A_T). In particular S ≥ 0 is impossible whenever μ_1(A_T) < 0. That holds for all large T (Perron ground state against the pole: R162_504 Thm 1 with prop:polarcap, R162_902 §2 terminal value).
*Proof.* ⟨F,A_TF⟩ = ⟨F,SF⟩ for F ∈ L²(I_T). A negative subspace of A_T of dimension k is a negative subspace of S (min–max). ∎

So "positivity of A_T on the window is automatic" is false as stated. What must be asked is a codim-2 statement:

**Theorem 3 (codim-2 compression = λ_A ≥ 0).** For fixed T the following are equivalent:
(i) λ_A(T) ≥ 0;
(ii) there is a closed form S_+ ≥ 0 on L²(I_T) with A_T − S_+ = R, R of rank ≤ 2, R|_{P_T} = 0 (i.e. R = Σ_{i,j} r_{ij} ℓ_i ⊗ ℓ_j, ℓ_i ∈ {ℓ_+, ℓ_−});
(iii) (Schur form) 𝔊_T := S^Sch + diag(2,−2) satisfies the polar-capacity condition of prop:polarcap.
Moreover (ii) can be realised on the full line by S_+ = S_0 exactly when RH holds.
*Proof.* (ii)⇒(i): on P_T, a_T = S_+ ≥ 0. (i)⇒(ii): if λ_A(T) > 0, compactness of the resolvent and the fact that ℓ_± are bounded on L²(I_T) give c with A_T + c(ℓ_+² + ℓ_−²) ≥ 0 (standard Schur-complement / Weinstein–Aronszajn argument). Take S_+ := A_T + c(ℓ_+²+ℓ_−²) and R := −c(ℓ_+²+ℓ_−²). If λ_A(T) = 0 with kernel N, the same holds iff the Tate functionals do not reach the kernel from the negative side. That is precisely the Schur clause (iii) (prop:polarcap; R162_504 Prop 4.1). The last sentence is Thm 1(b),(c). ∎

Thm 3 is E1: the "right statement" of (ii) is λ_A(T) ≥ 0 itself. Content could only come from an S_+ whose positivity is proved *independently*. The two explicit candidates are:
- S_0 (zero side): positivity = RH (W6).
- The CC semilocal / Sonin operator. This is Thm 4.

**Theorem 4 (semilocal CC carrier: no independent positivity; deletion-blind).** Let Σ be a finite set of places containing ∞ and every p ≤ e^{2T}. In the Connes semilocal trace formula Tr(R_Λ U(f)) = 2f(1)log Λ − Σ_{v∈Σ} W_v(f) + o(1) (Λ→∞), the only positive operator is the cutoff projection R_Λ. For F supported in I_T one gets
 a_T(F) = lim_Λ [2 log Λ‖F‖² − Tr(R_Λ U(F)U(F)*)]   (window comb = Σ-comb, since the p ∉ Σ never reach the window).
(a) This expresses A_T as a limit of differences c_Λ·Id − (positive compression), so it gives no lower bound.
(b) The formula holds verbatim for Σ' = Σ∖{p}. The resulting form is the deletion model ζ(s)(1−p^{−s}), whose zeros on Re s = 0 are off the critical line, so λ_A < 0 there for large T. The carrier construction cannot distinguish Σ from Σ'. The only difference is "Σ is complete up to e^{2T}", and that difference is the statement itself (F3/deletion line fired).
(c) At the archimedean place alone (T ≤ ½log 2), CC's decomposition W_∞ = Tr(ϑSϑ*) + E is exactly a Thm 3(ii) splitting with S_+ = the Sonin trace form (≥ 0) and E carrying the negative part. CC prove n₋ = 1, controlled by the one functional ĝ(0) (115_15 §3). Beyond log 2 the comb enters E, and n₋(E_T) ≥ N(T) (Thm 6). So the CC splitting is of the kind Thm 3 requires, but its content beyond log 2 is again λ_A ≥ 0.
*Proof.* (a) is the form of the trace formula. (b) is the observation that the local factors enter additively and independently, with nothing coupling membership in Σ to T. (c) combines 115_15 §1, §3 with n₋ subadditivity (W_∞ = positive + E ⇒ n₋(W_∞|_V) ≤ n₋(E|_V)). ∎

**NO-GO for (ii).** The explicit carrier exists (Thm 1), but no S ≥ 0 exists (Thm 2). The codim-2 version is λ_A ≥ 0 (Thm 3). Both explicit S_+ reduce to RH (S_0) or are deletion-blind (semilocal).

## 3. The Sonin count, run

**Definition 5.** N(T) := n₋(A_T|P_T), the number of negative eigenvalues of the compression of A_T to P_T. The total count is n₋(A_T) = #{μ_j(A_T) < 0}. In CC's normalisation K := Id − A/c, this is #{λ_j(K) > 1}. By codim-2 interlacing (two Cauchy steps, one per parity, R162_504 Thm 2),
 n₋(A_T) = N(T) + δ(T),  δ(T) ∈ {0,1,2}.
Here δ is the polar deficiency. By Perron and the pole, δ ≥ 1 once μ_1 < 0, with the even sector giving 1 (R162_504 Thm 2(b)).
CC's count at |I| = log 2 (T = ½log 2, before any prime): n₋ = 1, N = 0, δ = 1. This is consistent: λ_A(½log 2) > 0 is proved ((H1) at log 2).

**Theorem 6 (structure of the count).**
(a) N is nondecreasing in T: extension by zero maps P_T into P_{T'} isometrically for T < T' and preserves the form (Thm 1(a)).
(b) N(T) = 0 for T < T_*, and T_* = inf{T : N(T) ≥ 1} ∪ {T : λ_A(T) = 0} = the first contact. λ_A is nonincreasing by (a) and continuous by lem:contA. The first jump of N occurs at the first T > T_* where λ_A < 0; if λ_A touches 0 and returns, no jump occurs.
(c) N(T) ≤ 2κ_off for every T, where κ_off is the number of off-line pairs {ρ, 1−ρ̄} (possibly ∞). Off-line quartets contribute to S_0 the forms 2Re(F̂(γ)F̂(−γ)), each of signature (2,2), and the on-line zeros contribute Σ|F̂(γ)|² ≥ 0. On P_T, a_T = S_0.
(d) lim_T N(T) = 2κ_off. The lower bound is the finite-interpolation two-bump construction of R162_2501a, which gives 2 negative directions per off-line quartet in large windows, in general position for finitely many quartets. It agrees with the corpus Pontryagin identity κ = n₋ (Papers 08/18, R157_002 §4).
*Proof.* (a),(b) as stated. (c) The negative index of a form is at most the negative index of any summand decomposition, and it is inherited by restriction. (d) Given k off-line quartets, the construction of R162_2501a (two bumps at ±T' modulated at γ_j, with P_T' corrections by finite interpolation) yields a 2k-dimensional subspace on which a_T' ≤ −c e^{2β_min T'} + C < 0 for T' large. ∎

**Corollary 7 (what the count gives).**
(i) "The CC count stays at its |I| = log 2 value" (N ≡ 0, i.e. n₋(A_T) = δ(T) ∀T) ⟺ RH. **E1**, and it fails S5 (∀T of a per-window law).
(ii) sup_T N(T) < ∞ ⟺ κ_off < ∞ (finitely many off-line zeros). This is **genuinely weaker than RH**, so it passes S11. It is exactly the 8F residue m < ∞ and the Pontryagin route κ < ∞ (R157_002 §4, EXCL: Paper 11 shows the prime–archimedean pencil has an infinite-dimensional near-null space, so no finite-rank argument bounds it). The step κ < ∞ ⟹ κ = 0 is Conjecture C_B.
(iii) Unconditionally provable: N(T) < ∞ for each T (compact resolvent) and the trivial Hilbert–Schmidt bound, which is O(e^{T})-type through ‖C_I‖ ≤ Σ_{n≤e^{2T}}2Λ(n)/√n ≍ e^{T}. Neither rules out any off-line zero. 115_15 §4's warning is confirmed: tr K_I = 0 does not bound the count.
So the count is a Pontryagin index read window by window. It is a new *coordinate* on κ, not a new mechanism.

**Proposition 8 (falsifier transport for any bound on N).**
(a) Deletion: ζ(s)(1−p^{−s}) has infinitely many zeros on Re s = 0, so N_del(T) → ∞. Every step used by an a ≥ 0-blind argument (CM archimedean part, Perron, Beurling–Deny) holds for it. So such an argument cannot prove sup N < ∞, still less N ≡ 0.
(b) Two-atom comb: for T > ½log 4 the form is the convolution form with the fixed symbol σ₂ₐ = m(τ) − 2Σ_{p=2,3}s_p w_p cos(τ log p) (restricted to P_T). Where {σ₂ₐ < 0} has positive measure, Landau–Widom/Szegő for truncated convolutions gives N(T) ~ (T/π)|{σ₂ₐ<0}|, i.e. linear growth. For ζ the symbol is a positive measure plus the rank-2 pole iff RH. The count therefore distinguishes ζ from the two-atom model only through the atomic zero measure (W6: zero side).
(c) κ/finmod models (R162_2501b M_m): N ↑ 2m exactly, with the same formal structure (FE, closed semibounded form, lem:contA, first contact). A counting argument must read the purely atomic arithmetic side. That is the one property M_m lacks.
*Proof.* (a) Thm 6(d) applied to the deletion form (its Weil identity holds with the deleted comb). (b) is the standard eigenvalue-distribution theorem for Wiener–Hopf truncations with symbol bounded below and locally integrable (the log growth of m is harmless on bounded τ-sets). (c) is R162_2501b plus Thm 6(c),(d). ∎

## 4. Verdict against the specification (R162_2300 §7)

- S1 (λ = 0 non-perturbatively): the count uses the bottom (Thm 6(b)), but only as a definition.
- S2/S3: a count is nonlinear and orientation-sensitive (passes F2).
- S4/S8: fails. Prop 8(b),(c): the count separates ζ from the table only through the zero side.
- S5: N ≡ 0 is ∀T of a per-window law (E1). sup N < ∞ is an asymptotic object, but it is an old one (κ).
- S9/S7: the semilocal carrier does not use Euler beyond "local factors add" (Thm 4(b)).
- S10: fine (analytic, no h⁰).
- S11: sup N < ∞ is weaker than RH. **This is the one pass**, and it lands on the 8F residue.
- S12: CC's count at log 2 is a margin statement at one window (L-M).

**Status: NO-GO (PROVED) for cell 8D as a closing route.** PROVED dictionary: CC Sonin count = n₋(A_T) = N(T)+δ(T); N is monotone, first jump = first contact, limit 2κ_off.
(ii) has an explicit carrier with no positive version (Thm 2), and the codim-2 version is E1 (Thm 3). The only weaker statement produced, sup N < ∞, is the Pontryagin/m<∞ residue of 8F (ranking #1), which is not provable here.

## 5. Open items

- **O2602.1** (routes into 8F #1): prove sup_T N(T) < ∞ from Euler input that fails for deletion (Prop 8(a)) and for M_m (Prop 8(c)). This is the same as the 8F dichotomy lemma; there is no separate 8D residue.
- **O2602.2** (cheap, certifiable): decide whether δ(T) = 2 ever occurs, i.e. whether an odd negative eigenvalue appears before the odd primitive sector fails (R162_504 Thm 2(a) gives μ_1^odd ≥ μ_2). This is a tool, not a closure.
