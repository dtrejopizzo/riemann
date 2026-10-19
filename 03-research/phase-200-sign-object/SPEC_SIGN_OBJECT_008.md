# SPEC_SIGN_OBJECT_008 — Round 18: inventory of free variables; grand sieve over characters

Phase 200, "sign object". Synthesizer.
OPEN / NO-GO / NUMERICAL. No closure is proposed.

## Summary (≤300 words)

**Correction incorporated (AUDIT_200_SPEC007_001).** Requirement (F8) of SPEC_007 ("not additive over primes") is
**withdrawn**, because it excludes the form 𝔞^ζ = 𝔪 − Σ_p 𝔠_p itself. It is not used as a filter. The "collective
balance" of Cor. B.3 is not proved: it is a rewriting of cor:Tarch. Sign: erasing primes **lowers** the form on the
witness and restoring them raises it. What remains of the question is whether there exists a **free variable** that
is neither positional data nor a functional of the minimizer. The ones already indexed are: exterior data (strategy
E), the affine parameter θ (branch 1), and g at order ≥ 2 (W-det/W-mom). We inventory the six natural variables of
the problem:
V1 the window T, V2 the exponent σ (or ε), V3 the modulus q of the characters, V4 the level or weight, V5 the Mellin
scale and V6 the quadrature order M. All six fall into 𝒦_Φ (SPEC_006). V1 is in I9 and falls by restriction 11 and
by 𝒦_H. We also prove (Lemma 18.1, PROVED) that every interpolation inequality between windows goes in the useless
direction: to bound the middle window, information from a larger window is needed. Log-convexity of λ_A is already
falsified (R186_033). V2 is in I9: the ε-derivatives died with F4/ES-19, and the global version in ε falls either by
branch 1 (the weights n^{−ε} form a damped comb, of the cΛ family) or leads to the zero side. V3, the main
candidate, **is R162_1102** (Theorem O and O′, Prop. 3.1), together with I7 and Φ.12. The average over characters
only reindexes the same window coefficients by residue classes. The grand sieve is quadratic in the coefficients,
while the Weil form is linear in them. Used against the form, the grand sieve only gives an upper bound of the prime
term (class C_BT), which is moreover blind to the coefficients. We work out the case q = 5 exactly (Prop. 18.2,
PROVED). The main member is ζ(1−5^{−s}), whose difference from ζ is 𝔠_5, undefined (Lemma B.2); its negativity is
OPEN. For q = ∏_{p<P}p (6, 30), the main member is exactly the a_P of Paper 47, with a lower form than ζ's and
certified negative (cor:Tarch). For T < ½log 11, the family sum contains no arithmetic coefficient. On the Mori
frontier only the atom n = 11 appears. The sign of 𝔞^ζ remains a non-convex combination of forms with uncontrolled
sign. This is Cor. O.1 in the harmless direction. V4 falls by Φ.12 and by front A. V5 is gauge (R-Q2). V6 is REF-D
(N3). **No survivor.** The structural consequence is Prop. 18.4 (ARGUED): no variable free intrinsic to the explicit
formula serves as that variable. It must be **exogenous**, i.e., introduced by the object itself. We only close it
for intrinsic variables, not in general. L′♯ OPEN. Row D OPEN.

---

## 0. Corpus and index (mandatory grep)

A grep was performed over `05-meta-and-planning/ROUTES-TRIED-INDEX/` (README, 03_, 04_, 05_, 05b_, 06_), phase 200
(SPEC_006, SPEC_007, DH_TRANSFER_001, AUDIT_200_AMU_001) and R162_1102. Terms searched: "large sieve", "gran criba",
"carácter", "twist", "progresión", "log-convex", "three-window", "Rankin", "ES-19", "R-Q2". These are the entries
that touch this round:

| index entry | content | affected variable |
|---|---|---|
| README l.46; R162_1102 Thm O, O′, Prop 3.1, Cor O.1 | family of characters; Λ-blind average; grand sieve/Parseval in C_BT | V3 |
| 06_ l.146–147, l.154, l.207 (N_021 Thm 2, Prop 3) | progression statistics (BV, BDH, S–W, Brun–Titchmarsh) NO-GO; family of conductor q>1 by twisted vectors = hybrid form | V3 |
| 04_ l.33 W-sieve (R167_102 Thm B/B′, R167_103 Thm S) | positivity + support + upper sieves + grand sieve: NO-GO (b_θ satisfies all of them) | V3 |
| 04_ l.145; 06_ l.98 (R186_050–051) | (E_γ): grand sieve and VK insufficient | V3 |
| README l.397 INV_J_001 J2/J3 | MV/grand sieve/Selberg only give the trivial bound; H_sparse | V3 |
| README l.396 INV_H_001 A6 | progressions as additive identity: window collapse | V3 |
| 04_ l.89 F-Λχ₂ | twisted falsifier Λχ₂ | V3 |
| 04_ l.407, l.449 (G2C-159, G1C-R160) | Haar average over the twist = archimedean form | V2/V3 |
| SPEC_006 Φ.12, Cor Φ.12′; I7, I9 | transfer additivity; averages with the same Γ; families in c, ε, θ, t, τ, T | V2, V3, V4 |
| 04_ l.136 R186-PNTcone; R186_033 Idea 2 | log-convexity of λ_A: FALSE / NO-GO (NUMERICAL); log λ_A concave | V1 |
| README l.458 PROOF_L_SHARP_H_001, AUDIT_14 | 𝒦_H NO-GO; restriction 11: every flow in T is a statement about the out-of-band tail | V1 |
| README l.523 AUDIT_200_AMU_001; l.505–506 (MM, NN) | n^ε = moving the line; "do not retry σ-derivatives"; F4/ES-19 | V2 |
| README l.203, l.446; 05b L97 | front A: Rankin–Selberg blind to the comb; weight gap | V4 |
| SPEC_006 R-Q2 (l.56) | levels/scales = translations within the radical | V5 |
| SPEC_006 N3 | block/quadrature inertia = REF-D | V6 |
| 03_ l.41 NG-B1 | grand sieve among 15 classical mechanisms: NO-GO (upper bounds) | V3 |

**New reason declared in the objective for V3 and its contrast.** The objective proposes that the average over χ mod
q *selects a progression* and that the grand sieve is a **nonlinear positivity-type inequality** with free variable
q. It must be contrasted with R162_1102. Theorem O′ already writes the content of the family as sums by class
P_b(F), for arbitrary q and not only for q > X. Prop. 3.1 already examined exactly the grand sieve with
w_n = a(n)n^{−1/2}φ(log n). So the new reason does not evade the recorded reason for failure. §B verifies it
step by step, because the objective adds two elements that R162_1102 did not treat explicitly: the small-q case with
χ₀ of a_P type and the sign correction of AUDIT_200_SPEC007_001. Both are developed honestly and do not change the
verdict.

---

## A. Table V1–V6

Columns: does it escape 𝒦_Φ?; restriction that kills it C-pol / C-data / C-hom / C-θ / C-emb / C-MvN / Theorem X;
channel through which Λ enters; falsifier.

| V | variable | outside 𝒦_Φ? | restriction that kills it | Λ channel | falsifier | verdict |
|---|---|---|---|---|---|---|
| V1 | window T (one or several T) | no: I9 (families in T) + 𝒦_NL | restriction 11 (flow in T = out-of-band tail = (★★)); 𝒦_H; Lemma 18.1 (direction); Theorem X if evaluated at g* | positions log n ≤ 2T (C-data) | a_P in [0.60, ½log P]; Lemma E (T ≥ 1.59) | **NO-GO** (Lemma 18.1 PROVED + R186_033 NUMERICAL) |
| V2 | exponent σ = ½+ε (weights n^{−ε}) | no: I9 (ε) | F4/ES-19 (derivatives); branch 1 for the global version (damped comb ∈ cΛ family); C-pol (the pole moves and is no longer rank ≤ 2 in P_T) | coefficients Λ(n)n^{−ε}: deformed C-data | cΛ with c<1 (AUDIT_SPEC_001); DH | **NO-GO** (Prop. 18.3) |
| V3 | modulus q (characters mod q) | no: I7 + Φ.12 + Thm O′ | C-data (sums by class of the same coefficients); grand sieve ∈ C_BT and blind to a; C-emb (linear decomposition over classes) | Λ(n)1_{n≡b (q)}: reindexing | χ₀ mod ∏_{p<P}p = a_P within the family; deletion/κ/finmod (Prop 3.1); vacuous DH | **NO-GO** (= R162_1102; §B) |
| V4 | level N / weight k (Hecke, Rankin–Selberg) | no: I7/Φ.12 (products), front A | Φ.12′: 𝔞^{L} = 𝔞^ζ + 𝔞^{L′}, with no sign on 𝔞^{L′}; Rankin–Selberg blind to the comb (front A); weight gap (README l.446) | |a_f(p)|² and Λ_f: another comb | ζ² (branch 2); DH twists | **NO-GO** |
| V5 | Mellin scale u ↦ λu | no: R-Q2/gauge | translation within the radical; dilation = gauge of the dilated frame (H_001) | nothing new | — | **NO-GO** (gauge) |
| V6 | quadrature order M | no: N3, I8 | block inertia = REF-D; dual LP cuts = I8 | samples of c_F | — | **NO-GO** (REF-D) |

### A.1 V1: the window as a free variable

**Lemma 18.1 (direction of interpolation between windows, PROVED, elementary).** Let Ψ(T) be a sound quantity
(Ψ ≤ λ_A) or a lower bound of λ_A(T), and suppose a three-window inequality
  log Ψ(T₂) ≥ (1−θ) log Ψ(T₁) + θ log Ψ(T₃), T₁ < T₂ < T₃, θ = (T₂−T₁)/(T₃−T₁).
If one wants to deduce Ψ(T₂) > 0, one needs Ψ(T₃) > 0. Since λ_A is non-increasing in T (Lemma M), the hypothesis on
T₃ is stronger than the conclusion. No log-concave or log-convex inequality "pointing inward" (bounding the interior
point by the endpoints) transports sign toward larger windows. An "outward" inequality, bounding Ψ(T₃) by Ψ(T₁) and
Ψ(T₂), is an extrapolation. By convexity of log Ψ it would give Ψ(T₃) ≥ Ψ(T₂)^{1+θ′}/Ψ(T₁)^{θ′} > 0 whenever both are
positive. That requires log Ψ to be **convex**, which is precisely what is falsified for λ_A (R186_033: log λ_A is
concave; thm:margin: −log λ_A superexponential).
*Proof.* The first part is monotonicity plus the definition. For the second: if log Ψ is convex on [T₁, ∞), then
log Ψ(T₃) ≥ log Ψ(T₂) + (T₃−T₂)·(log Ψ(T₂)−log Ψ(T₁))/(T₂−T₁), which is finite. ∎

**Consequence.** For V1 to be useful one would need a quantity Ψ with these three properties: (i) Ψ ≤ λ_A; (ii) log Ψ
convex in T; (iii) Ψ(T) > 0 in two certified windows (for example ½log 2 and ½log 15, with Mori). But (i)+(ii)
contradict the superexponential shape of the decay if Ψ must vanish at some T. There is no contradiction if Ψ never
vanishes, but then (ii) is already the sign statement for all windows: it is REF-D (branch 2). If Ψ is defined with
different tests at T₁ and T₂, without evaluating at the minimizer, it is still a functional of the forms 𝔞_{T_i},
and convexity in T of a family of infima is a statement in 𝒦_NL (Φ.11). We falsify it with Lemma E: this satisfies
λ_A(T₁), λ_A(T₂) > 0 for T₁ < T₂ < 1.59, and λ_A(T₃) < 0 at T₃ ≥ 1.59 nearby. The convexity of log Ψ would fail in
Lemma E in the same sense observed in ζ, so the property is not comb-uniform (branch 1).
**Status: NO-GO.** Lemma 18.1 PROVED. The falsification of convexity for λ_A is NUMERICAL (R186_033). The
comb-genericity of the infimum's convexity is ARGUED via Lemma E.

**Index.** The log-convexity "of some quantity ≥ λ_A" from the objective goes in the wrong direction: an *upper*
bound gives no sign. The one for a quantity ≤ λ_A falls into Lemma 18.1. There is no new reason against R186_033
Idea 2.

### A.2 V2: global σ (comb with weights n^{−ε})

Let 𝔞_T^{(ε)} be the window form of ζ(s+ε) read on the ½-line: comb Λ(n)n^{−1/2−ε}, archimedean of Γ_ℝ(s+ε) and
pole at s = 1−ε.

**Prop. 18.3 (V2, PROVED except as indicated).**
(a) For ε > ½ the comb converges absolutely and its operator norm on L²[−T,T] is bounded by
Σ_{n≤e^{2T}} Λ(n)n^{−1/2−ε} ≤ a convergent ψ-sum. But the pole s = 1−ε is now at distance ½−ε from the line.
**It crosses the line at ε = ½**, and its term does **not** vanish in P_T, because P_T is defined by A = B = 0 for
the pole at s = 1. So "trivial for large ε" is false as written: the form with ε > ½ has a rank-2 polar term with
its own sign, and the comparison with ε = 0 loses C-pol. (PROVED: the subspace P_T is not invariant under the shift
of the pole.)
(b) The coefficients n^{−ε}Λ(n), with 0 < ε, are the damped-comb family. They belong to the generalized cΛ class
(multiplicative weights ≤ 1), for which AUDIT_200_SPEC_001 requires every free positivity to be false. A
"continuation in ε" that transports sign from large ε down to ε = 0 must fail at some member. By branch 1 of Φ200,
the object is not uniform. (ARGUED: we have not exhibited the critical ε for ζ; for cΛ with small c the failure is
that of the battery.)
(c) Real analyticity in ε: it does not transport sign. This is standard (PROVED: a real-analytic function can change
sign).
(d) Counting sign changes in ε (Descartes/Pólya): the number of zeros in ε of ε ↦ λ_A^{(ε)}(T) is controlled by the
variation of the family of forms. For ζ, those zeros relate to the geometry of the zeros of ζ(s+ε) with respect to
the line, i.e., to the zero side. This is forbidden as input: branch 4 or a zero-side premise (G6E-159).
**Decision: NO-GO.** The derivatives are dead by F4/ES-19 and AUDIT_AMU (README l.523). The global version falls by
(a) C-pol, by (b) branch 1, and by (d) the zero side.

### A.3 V4, V5, V6

**V4.** For L = ζ·L′ (Hecke towers, base change, Dedekind), Φ.12 gives 𝔞^L = 𝔞^ζ + 𝔞^{L′} in P_T (PROVED in
SPEC_006). A free variable N or k only varies 𝔞^{L′}, and the sign of ζ remains 𝔞^ζ ≥ −𝔞^{L′}, uncontrolled.
Rankin–Selberg L(f×f̄) gives |a_f(p)|² ≥ 0. This is a coefficient positivity at weight n^{−1} (σ > 1) and blind to
ζ's comb (front A, README l.203; weight gap, l.446; L97). The weight k enters only through the archimedean
Γ_ℂ(s+(k−1)/2), which is Λ-blind. **NO-GO, no new reason.**
**V5.** Dilation u ↦ λu: the dilated frame of H_001 shows that W_T is translation-invariant and that the scale only
moves the band edge and the gauge. By R-Q2 it is a translation within the radical. **NO-GO (gauge).**
**V6.** Quadrature order M (number of sampling nodes of c_F): by N3 the block inertia of 𝔞_T is REF-D. The dual LP
cuts are in I8, and thm:D1 bounds them by λ_P(T). M is a discretization variable, not an arithmetic one: λ_A(T) is
the limit M → ∞. **NO-GO (REF-D).**

---

## B. Full development of V3: characters mod q and the grand sieve

### B.1 Exact definitions

Let q ≥ 3 be prime, X = e^{2T} and F ∈ P_T, so that c_F(u) = (F⋆F̃)(u) is supported on |u| ≤ 2T and A = B = 0.
For each χ mod q, let χ* be the associated primitive character, with conductor q_χ ∈ {1, q} and parity 𝔞_χ ∈ {0,1}.
With the normalization of R162_1102 §2 (CITED: Weil 1952; Iwaniec–Kowalski Thm 5.12):

  𝔞_T^{χ}(F) = M_χ‖F‖² + A^∞_{𝔞_χ}(F) − Σ_{n≤X} Λ(n) n^{−1/2} Re χ(n) c_F(log n),  M_χ = log(q_χ/π),

where for χ ≠ χ₀ there is no polar term. For the principal character there are two choices, and the difference
matters:

- **(P)** primitive: χ₀* = 1, i.e., ζ itself: 𝔞^{χ₀*} = 𝔞^ζ;
- **(I)** imprimitive: L(s,χ₀) = ζ(s)(1 − q^{−s}) = a_{{q}}(s). Its form is 𝔞^{a_{{q}}} = 𝔞^ζ + 𝔠_q, with
  𝔠_q(F) = Σ_{k: q^k ≤ X} (log q) q^{−k/2} c_F(k log q) (Lemma B.1 of SPEC_007, PROVED). The pole is that of ζ and is
  null in P_T. The zeros of 1 − q^{−s} lie on Re s = 0 and do not enter the window form on the ½-line
  (R162_1102 §2).

### B.2 The orthogonality identity (exact)

For (n,q) = 1: Σ_{χ mod q} χ(n) = (q−1)·1_{n≡1 (q)}. For q | n, all χ(n) vanish.

**Prop. 18.2 (identity of the mod-q family, PROVED; a special case of Thm O′ of R162_1102).** With choice (I):

  Σ_{χ mod q} 𝔞_T^{χ}(F) = 𝔐_q(F) − (q−1) P_1^{(q)}(F),
  P_1^{(q)}(F) := Σ_{n ≤ X, n ≡ 1 (q)} Λ(n) n^{−1/2} c_F(log n),
  𝔐_q(F) := Σ_χ [M_χ‖F‖² + A^∞_{𝔞_χ}(F)],

and therefore

  𝔞_T^ζ(F) = 𝔐_q(F) − (q−1)P_1^{(q)}(F) − Σ_{χ≠χ₀} 𝔞_T^{χ}(F) − 𝔠_q(F).   (18.1)

*Proof.* Sum the forms. The term Re χ(n) sums to (q−1)1_{n≡1} if (n,q) = 1 and 0 if q | n; choice (I) eliminates
the q^k atoms of χ₀'s comb. Then apply 𝔞^{a_{{q}}} = 𝔞^ζ + 𝔠_q. ∎

Reading against the objective. The "average" (1/φ(q))Σ_χ 𝔞^{χ} is the Λ-blind form 𝔐_q/(q−1), minus ζ's comb
**restricted to the progression 1 mod q**. The identity is exact and does select a progression, as the objective
says. But it is **linear in the coefficients**: selecting the progression is multiplying Λ by the class function
1_{n≡1 (q)}. By Theorem O′, every combination Σc_χ𝔞^χ reads only sums by class P_b of the same coefficients
Λ(n), n ≤ X. Hence it is **C-data**: it introduces no datum of Λ that is not already in (Λ(n))_{n≤X}. Nor is it
nonlinear in the sense of Φ200. The "nonlinearity" of selecting a progression is that of a fixed diagonal projector
in coefficient space, so it is O-lin.

### B.3 The grand sieve: what quadratic form it controls

Grand sieve (CITED: Montgomery–Vaughan; R162_1102 §3(b)), for fixed modulus q:
  Σ_{χ mod q} |Σ_{n≤N} w_n χ(n)|² ≤ (N + q)·Σ|w_n|²,
and in its additive or multimodular form, Σ_{q≤Q}(q/φ(q))Σ*_χ|…|² ≤ (N+Q²)Σ|w_n|².

**The degree mismatch (PROVED; this is Prop. 3.1 of R162_1102).** The form 𝔞_T^{χ}(F) is quadratic in F and
**linear** in the coefficient sequence a = Λ. The grand sieve is quadratic in w. To connect them there are two
possibilities.

(i) w_n = Λ(n)n^{−1/2}φ(log n) with φ built from F. Then Σ_χ|Σ w_nχ(n)|² is a quadratic form in Λ, degree 2 in the
coefficients. It does not appear in any Weil form of L(χ): it is Λ⋆Λ, the channel of products and 4-point forms
(Φ.11, branch 1; N5). The grand sieve bounds it **from above** by (N+q)‖w‖². To use it against 𝔞^ζ one needs
P^Λ(F) ≤ C·(Σ_χ|Σ wχ|²)^{1/2}, i.e., an upper bound of the prime term, which is in C_BT
(R155_053 Prop 1.1). By exact orthogonality (Parseval: Σ_χ|Σ wχ|² = φ(q)Σ_b|Σ_{n≡b} w_n|²), this is moreover
an equality and **holds for any w**: it is blind to the coefficients (deletion, κ, finmod; R162_1102 Prop 3.1).

(ii) w = F-coefficients, i.e., the grand sieve applied to F as a Dirichlet polynomial: |Σ_n f_n χ(n) n^{−it}|². This
is the dual of the hybrid form (N_021 Prop 3: "family of conductor q>1 by twisted vectors = hybrid form, not the
window form of L(s,χ)"). The resulting inequality is a bound on the norm of F, with no Λ. It is Λ-blind (branch 4).

**Conclusion B.3 (PROVED as mismatch; NO-GO as a class).** Neither reading gives an inequality of the type
"form ≥ 0". The grand sieve is a positivity inequality of the form (N+q)‖w‖² − Σ_χ|…|² ≥ 0, but that quadratic
form lives in the coefficient space w, and its positivity is **universal**: it holds for every w and decides
nothing about arithmetic. It is the same situation as "‖ω_+(f)‖²_HS ≥ 0 does not see the comb" (INV_D_001).

### B.4 Where exact Λ enters

There are three points of contact, all three recorded.
1. **Orthogonality**: uses only the group structure of (ℤ/q)^×, not Λ. Holds for every a (Thm O).
2. **a ≡ 1 in the progression**: P_1^{(q)} is Λ restricted. Its content is C-data. Progression statistics
   (BV, BDH, Siegel–Walfisz, Brun–Titchmarsh) as class input is NO-GO (N_021 Thm 2, 06_ l.146), because every
   class closed under finite modification dies by cor:void.
3. **Euler product of each L(χ)**: it enters only via Λχ = Λ·χ, which is completely multiplicative in χ. This adds
   no restriction on Λ beyond being supported on prime powers. Deletion a_P satisfies it, and has well-defined
   characters (a_P·χ), so the twisted family of a falsifier **exists** and satisfies the same identity (18.1) with
   𝔠_q replaced.

### B.5 The q = 5 test

Characters mod 5: χ₀; χ₂ = (·/5), quadratic and even; χ, χ̄ quartic and odd, with χ(2) = i. Conductors: 1 (χ₀*)
and 5 (the other three). In the window, the progression 1 mod 5 contains these prime powers: 11, 16 = 2⁴, 31, 41,
61, 71, 81 = 3⁴, 101, 121 = 11², …

**(a) Small windows.** If X < 11, i.e., T < ½log 11 ≈ 1.199, then P_1^{(5)} ≡ 0 in P_T and (18.1) becomes

  𝔞_T^ζ = 𝔐_5 − 𝔞^{χ₂} − 2Re 𝔞^{χ} − 𝔠_5,   𝔠_5(F) = v_5 Re c_F(log 5)  (X < 25).   (18.2)

The family sum, Σ_χ𝔞^χ = 𝔐_5, is **purely archimedean and of conductor** (Thm O in the regime q > X
effective: every n ≤ X with (n,5)=1 satisfies n ≢ 1). It contains zero Λ data. (PROVED.)

**(b) Mori frontier.** With T ≤ ½log 15, X ≤ 15, the progression contains only n = 11, and

  Σ_χ 𝔞^χ = 𝔐_5 − 4·v_{11} Re c_F(log 11).   (18.3)

A single atom, with undefined sign of c_F(log 11). It is a one-point comb, undefined in P_T by the same
argument as Lemma B.2 (PROVED: the construction of B.2 uses only an isolated atom at log p; it holds for the
atom log 11 at T > ½log 11 + η).

**(c) The a_P-type member within the family (corrected per AUDIT_200_SPEC007_001).** With choice (I),
the χ₀ mod 5 member is ζ(s)(1−5^{−s}). Its comb is Λ without the powers of 5, and its form is 𝔞^ζ + 𝔠_5, with
𝔠_5 = Σ_k v_{5^k} Re c_F(k log 5) undefined in P_T for T > ½log 5 (Lemma B.2, PROVED). It is **not** the a_P of
prop:shape-eulerdel, which erases all primes p < P. The paper gives no witnesses for arbitrary sets of erased
primes (audit §1). So the negativity of ζ(1−5^{−s})'s form in a concrete window remains **OPEN**: it is
not certified in the corpus.

**(c′) The certified case: q = ∏_{p<P} p.** If q = 6 (P = 5) or q = 30 (P = 7), then
L(s,χ₀ mod q) = ζ(s)∏_{p<P}(1−p^{−s}) = ζ_{a_P}(s) **exactly**, with the same archimedean symbol m(τ) (audit §1).
For T ∈ [0.60, ½log P] the comb of a_P is empty in the window. Then 𝔞^{χ₀} = 𝔪 and λ_inf^P(T) < 0 (cor:Tarch):
**the main member of the mod-q family has negative form** in that window, PROVED as a citation of the paper. For
q = 6 and T ≤ ½log 5, 𝔞^ζ ≥ 0 (thm:log5A + lem:monoT, PROVED). The form of the main member is **lower** than
ζ's: erasing lowers and restoring raises. Thm O′ for q = 6 (the only non-principal character is χ₃* mod 3, of
conductor 3, odd) gives
  𝔞^ζ = 𝔞^{χ₀ mod 6} + Σ_{p∈{2,3}} 𝔠_p,
so the difference is exactly the erased comb. With composite q, orthogonality mod q contributes nothing beyond
what is already in the definition of a_P.
**What this honestly says:**
- The family of characters mod q, with choice (I) and q = ∏_{p<P}p, contains a member with **negative**
  (certified) form in windows where 𝔞^ζ is positive. For q = 5 this is OPEN. So the positivity of the family sum,
  even if proved, **does not descend to the members**. The sum is 𝔐_5 (or 𝔐_5 minus one atom). Whether it is
  positive or not is a property of Γ and the conductor, not of Λ.
- With choice (P), the χ₀ member is ζ itself and the identity is Thm O′ with E_q = −𝔠_5. Then (18.2) says
  that 𝔞^ζ ≥ 0 is equivalent to 𝔞^{χ₂} + 2Re𝔞^{χ} ≤ 𝔐_5 − 𝔠_5. An **upper bound** of the non-principal forms
  is needed, i.e., a sign statement for each of them. This is Cor. O.1: the harmless direction. The positivity of
  𝔞^{χ} for χ mod 5 primitive (the analogue of D for L(χ)) **is not certified in the corpus**. Grepping
  "L(χ)", "χ mod 5" and "Dirichlet" in the index and in phase 200 only gives numerical calibrations (R4-09) and the
  DH (which is not Λχ). Status: OPEN, and even if certified it would go in the wrong direction.
- (18.2) is exactly an **additive decomposition over residue classes** of ζ's comb: Λ = Σ_b Λ1_{n≡b}. It is
  the "by classes" linear version of 𝔞^ζ = 𝔪 − Σ_p 𝔠_p. Each piece P_b is undefined (Lemma B.2 applied to the
  first atom of the class), just like each 𝔠_p. As AUDIT_200_SPEC007_001 §5 stresses, the pieces being undefined
  neither prevents nor explains anything. **V3 adds no free variable: it reindexes the same linear decomposition.**
  (PROVED as an identity; the undefinedness of each P_b is PROVED for the classes that have an isolated atom in
  the window.)

**(d) DH.** The DH lives in the span of L(χ), L(χ̄) mod 5, but its comb a_DH = −D′/D is not in the span of the
Λχ′ (R162_1102 §5(i), PROVED). The family lets it pass **vacuously**. Warning from §5(iii): any step of the family
written "linear in L" rather than "linear in log L" absorbs the DH and proves something false. The grand sieve of
B.3(ii), applied to Dirichlet polynomials in L, is in that danger.

### B.6 Target theorem (as it would be formulated) and why it fails

*Proposed objective (V3-GC).* There exist q = q(T) and a grand-sieve inequality giving, for every F ∈ P_T,
  Σ_{χ≠χ₀} 𝔞^χ_T(F) ≤ 𝔐_q(F) − (q−1)P_1^{(q)}(F) − 𝔠_q(F),
and by (18.1) one obtains 𝔞^ζ_T ≥ 0.

*Why it fails (PROVED by identity).* By (18.1), the objective is **identical** to 𝔞^ζ_T ≥ 0: it is REF-D (branch 2;
Cor. O.1). The grand sieve can only contribute upper bounds on Σ_χ|Σ w χ|², which are quadratic in w and blind to
the coefficients (B.3). It cannot bound from above a sum of forms that is **linear** in the coefficients with
undefined sign. For q = q(T) → ∞, the regime is that of Theorem M (double exponential dilution; R162_801 L5), and
moreover q > X makes P_1 ≡ 0 and everything Λ-blind (Thm O).

### B.7 Falsifiers

| falsifier | satisfies (18.1)? | satisfies the grand sieve in w? | consequence |
|---|---|---|---|
| a_P (erases p<P) | yes, with a_Pχ | yes (universal) | V3 does not separate ζ from a_P in [0.60, ½log P] |
| cΛ, c<1 | yes (linear) | yes | scaling; branch 1 |
| κ-models, finmod | yes (Thm O: a-blind) | yes | same |
| Lemma E (T ≥ 1.59) | yes if it has characters; vacuous otherwise | yes | does not decide T |
| DH | does not apply (vacuous) | applies to L, not to log L: dangerous | §5(iii) |

### B.8 First lemma (for audit) and risk

**Lemma 18.V3 (PROVED).** For every prime q and every T ≥ 0.60, identity (18.1) holds **identically** if Λ is
replaced by any a supported on prime powers, with a·χ in place of Λχ. In particular, the family of characters mod q
of a battery falsifier satisfies the same identity with the same 𝔐_q. *Proof.*
Linearity plus orthogonality (Prop. 18.2). ∎
Consequence: every statement derived from V3 that is uniform over the class of combs-with-characters is
comb-generic (branch 1 of Φ200).

**Risk.** None of construction: the route is not constructed. The registration risk is treating Prop. 18.2 as new.
It is not: it is Thm O′ of R162_1102 with explicit E_q = 𝔠_q and q < X. What is new in this round is only
(18.2)–(18.3) as a **concrete instance of the linear decomposition by classes** (q = 5, Mori window: one atom,
n = 11), and the observation that the family with choice (I) contains a falsifier.

---

## C. Ranking and structural consequence

| rank | V | status | useful residue |
|---|---|---|---|
| 1 | V3 (q + grand sieve) | NO-GO (= R162_1102 Thm O/O′/Prop 3.1; N_021; W-sieve) | (18.2)–(18.3); the mod-q family contains an a_P-type member (certified negative for q = 6, 30, …; §B.5(c′)) |
| 2 | V1 (T, three windows) | NO-GO (Lemma 18.1 PROVED; R186_033 NUMERICAL; 𝒦_H) | Lemma 18.1: interpolation between windows goes in the useless direction except for convexity, which is falsified |
| 3 | V2 (global ε) | NO-GO (Prop. 18.3: C-pol fails for ε > ½; branch 1; zero side) | the pole crosses the line at ε = ½: "triviality for large ε" is false in P_T |
| 4 | V4 (N, k) | NO-GO (Φ.12′; front A) | — |
| 5 | V5, V6 | NO-GO (gauge; REF-D) | — |

**Prop. 18.4 (no intrinsic variable is a useful free variable, ARGUED).** The free variables intrinsic to ζ's
window form are: the parameters of the explicit formula (T, σ, the character/conductor, Γ, the scale, the
discretization) and the deformations of the family that preserve the shape of an explicit formula. All are in
I7 ∪ I9 ∪ R-Q2 ∪ N3, and each falls into a branch of Φ200 (table A). So a useful free variable, if it exists, must
be **exogenous**: a degree of freedom that the object itself introduces, that is not a parameter of any explicit
formula and from which the form 𝔞^ζ_T emerges as a section or a limit, not as a member of the family. *Why ARGUED:*
the list of intrinsic parameters is complete by inspection of the Weil–Guinand explicit formula (pole, Γ, conductor,
coefficients, line, test support), but we have no proof that every family preserving the formula must factor
through that list.

**Tentative requirement (V′) for round 19 (OPEN, without constructive content; it does not replace F8 as a filter).**
The sign object must introduce an **exogenous** free variable ν
(ν ∉ {T, σ, q, N, k, scale, M}) such that: (i) for some ν₀, the output at ν₀ is sound for λ_A(T); (ii) the
dependence on ν is **not** linear in the comb (so as not to fall into Lemma 18.V3 / Thm O′); (iii) the family of
falsifiers a_P does not admit the same extension in ν. If it does admit it, the extension must fail in an
**observable** way at ν ≠ ν₀, and Lemma 18.V3 makes this impossible for variables entering linearly in the comb.
Moreover, ν must not be any of the three already indexed (AUDIT_200_SPEC007_001 §5): exterior data, affine θ, g at
order ≥ 2. Before proposing any ν one must grep the index. Entries to review first: Kurokawa's tensor product
(E101_083), the "global object" C10 (LEDGER_L5: never built) and the θ-sheaf (I6). The candidate must say
explicitly why it is none of them.

**Status.** Lemma 18.1 PROVED. Prop. 18.2 PROVED (instance of Thm O′). Prop. 18.3 (a), (c) PROVED; (b), (d) ARGUED.
Lemma 18.V3 PROVED. Prop. 18.4 ARGUED. No survivor. L′♯ OPEN. Row D OPEN.

**For the index (add in this session).** "SPEC_SIGN_OBJECT_008 (round 18, free variables; F8 withdrawn by
AUDIT_200_SPEC007_001): V1–V6 NO-GO.
V3 (q + grand sieve) = retry of R162_1102 Thm O/O′/Prop 3.1 with no new reason surviving. Grand sieve quadratic in
coefficients vs. linear form: C_BT, a-blind. Case q=5: Σ_χ𝔞^χ = 𝔐_5 (Λ-free) for T<½log 11; one atom n=11 on the
Mori frontier; the family with imprimitive χ₀ contains ζ(1−5^{−s}) (negativity OPEN); (18.2) = linear decomposition
by classes (no free variable); with q = ∏_{p<P}p, χ₀ is the a_P of prop:shape-eulerdel. Lemma 18.1
(PROVED): interpolation between windows goes in the useless direction except for log-convexity (falsified,
R186_033). Prop. 18.3: global n^{−ε} fails C-pol for ε>½. Prop. 18.4 (ARGUED): a useful free variable must be
exogenous (V′, OPEN). Do not retry character families, grand sieve, progressions, three windows, or global ε
without breaking Lemma 18.V3 / Lemma 18.1."
