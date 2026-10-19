# R162_402 — G2: the trivial-zero reflection of the Gamma lattice

Status: **PROVED STEP (exact reflected dictionary) + NO-GO (Hardy pole/zero mechanism).** Gate 1 OPEN.

Sources used: Paper 47 §sec:firstcontact (eq:residue, eq:Gammaenergy, eq:smallgain); R161_017 (2.3), (4.1)–(4.3);
R161_008 Thm 3.1, (3.2); R162_102 Prop 1.1, 2.1; R162_305 §4.

## 0. Conventions

s = ½+z, ζ(s)=χ(s)ζ(1−s), χ(s)=π^{s−½}Γ((1−s)/2)/Γ(s/2), d_Γ=−χ'/χ. s_m=2m+1, a_m=2m+½, so
1−s_m=−2m and the reflected z-point is −a_m. F(−t)=εF(t), K_F(−z)=εK_F(z). Ports (R161_017 (1.3)–(1.5), (4.1)):

    G_+ = −ζ'(s)K_F(z) − ζ(s)Q_+(z),   G_-(z)=εG_+(−z) = −ζ'(1−s)K_F(z) − ζ(1−s)Q_-(z),
    G_+^0 = G_+ − ζ(s)Θ_+,             G_-^0 = G_- − ζ(1−s)Θ_-,

Q_±, Θ_± Laplace transforms of compactly supported (Q) or exterior Schwartz-type (Θ, supported in [T,T+1]
resp. [−T−1,−T]) distributions, hence **entire**. Laurent data of χ at s_m, u=s−s_m:

    χ(s) = ρ_m/u + c_m + O(u),   ρ_m = Res_{s_m}χ = −2(−1)^m π^{2m+½}/(m! Γ(m+½)) ≠ 0.       (0.1)

(From Γ(−m+w)=(−1)^m/(m!w)+O(1), w=−u/2.)

## 1. The reflected dictionary (PROVED; functional equation + ζ(−2m)=0 only)

**Lemma 1.1.** ζ(s_m) = −ρ_m ζ'(−2m); ζ'(s_m) = ½ρ_m ζ''(−2m) − c_m ζ'(−2m).

*Proof.* ζ(1−s) = −ζ'(−2m)u + ½ζ''(−2m)u² + O(u³) since ζ(−2m)=0. Multiply by (0.1): the constant term is
−ρ_mζ'(−2m). For the derivative use ζ'(s)=χ'(s)ζ(1−s)−χ(s)ζ'(1−s) with χ'=−ρ_m/u²+O(1),
ζ'(1−s)=ζ'(−2m)−ζ''(−2m)u+O(u²):
χ'ζ(1−s)=ρ_mζ'/u − ½ρ_mζ''+O(u), χζ'(1−s)=ρ_mζ'/u − ρ_mζ'' + c_mζ' + O(u); subtract. ∎

(Lemma 1.1(i) is the classical ζ'(−2m)=(−1)^m(2m)!ζ(2m+1)/(2(2π)^{2m}); checked to 30 digits, m=1,2,5.)

**Lemma 1.2.** FP_{s_m} d_Γ = −c_m/ρ_m = −log π + ½ψ(m+1) + ½ψ(m+½).

*Proof.* χ'/χ = (−ρ/u²+O(1))/(ρ/u+c+O(u)) = −1/u + c/ρ + O(u). Second form: d_Γ=−logπ+½ψ((1−s)/2)+½ψ(s/2)
and ψ(−m+w)=−1/w+ψ(m+1)+O(w). ∎

**Theorem 1.3 (reflected dictionary).** For every F ∈ L²(I_T) of parity ε (no first-contact hypothesis):

    (a) value channel:   x_m = ζ(s_m)b_mK_F(a_m) = −ρ_m ζ'(−2m) b_mK_F(a_m) = ε ρ_m b_m G_+^0(−a_m) = ρ_m b_m G_-^0(a_m);
    (b) residue germ:    Res_{s_m}[ζW^0_ε] = ζ(s_m)K_F(a_m) = ρ_m G_-^0(a_m)   (= eq:residue);
    (c) jet channel:     j_m = −ζ'(s_m)b_mK_F(a_m) = [c_m ζ'(−2m) − ½ρ_mζ''(−2m)] b_mK_F(a_m);
    (d) Euler diagonal:  d_m = −ζ'/ζ(s_m) = ½ ζ''(−2m)/ζ'(−2m) + FP_{s_m}d_Γ;
    (e) logarithmic port: H_+ := G_+/ζ = −(ζ'/ζ)K_F − Q_+ has Res_{z=−a_m} H_+ = −εK_F(a_m), and
                          G_+^0(−a_m) = G_+(−a_m) = −εζ'(−2m)K_F(a_m)  (polar correction invisible).
    (f) Gamma energy:    ‖R_LF‖² = Σ_{m≤L} a_m e^{−2a_m(T+δ)} |G_+^0(−a_m)/ζ'(−2m)|².

*Proof.* G_+^0(−a_m) = −ζ'(−2m)K_F(−a_m) − ζ(−2m)[Q_+(−a_m)+Θ_+(−a_m)] = −εζ'(−2m)K_F(a_m), as Q_+, Θ_+ are
entire and ζ(−2m)=0. With Lemma 1.1(i) this is (a), (e) second part; G_-^0(a_m)=εG_+^0(−a_m) since the Θ_-
correction likewise carries ζ(1−s)|_{s_m}=0. (b): take residues in R161_017 (4.2): G_+^0 is holomorphic at s_m,
so Res[χG_-^0] = ρ_mG_-^0(a_m) = Res[ζW^0]; this recovers eq:residue independently. (c),(d): Lemma 1.1(ii),
1.2. (e) first part: ζ'/ζ has residue 1 at the simple zero −2m, Q_+ entire. (f): (e) inserted in
eq:Gammaenergy. ∎

Hence the two channels of eq:smallgain reflect as announced: at s=−2m the value channel of ζ is 0, the
product port G_+^0 retains only the derivative channel ζ'(−2m)=(nonzero)·ζ(2m+1), and

    **R_LF = 0  ⟺  G_+^0(−a_m) = 0 (m ≤ L)  ⟺  H_+ is regular at the trivial zeros −2m (m ≤ L).**      (1.1)

This is the requested identity (nonzero factor)·K_F(a_m) = (reflected port value): −εζ'(−2m)K_F(a_m) = G_+^0(−a_m).
The polar layer (Θ_+) and the prehistory Q_+ drop out of it identically (they are multiplied by ζ(−2m)=0); the
Tate vector enters only through (b). So nothing on the right side is *forced* to vanish: (1.1) is a
reformulation of Gate 1, not a closing identity.

Link to R162_305 §4: the multiplier "renormalised Σ n^{2j} = ζ(−2j)=0" there is exactly the factor ζ(−2m)
killing Q_+ and Θ_+ in (a); the surviving term is the jet ζ'(−2m), i.e. the ζ(2m+1) value channel on the other
side. The trivial-zero cancellation removes the *history*, not the residue.

## 2. The Hardy pole/zero test (NO-GO, PROVED)

Question: does ζ'(−2m)≠0 give G_-^0 near z=a_m (equivalently G_+^0 near −a_m) a pole/zero structure
incompatible with e^{Tz}G_+^0 ∈ H²(C_+), e^{−Tz}G_-^0 ∈ H²(C_−) unless K_F(a_m)=0?

**Proposition 2.1.** No.
(i) G_+^0 is entire (its only singularity z=½ is removed by Θ_+, R161_008 (2.3)); G_-^0 likewise. ζ'(−2m)≠0
produces neither a pole nor a forced zero: G_+^0(−a_m) is a finite value, zero iff K_F(a_m)=0 (tautologically).
(ii) The reflected lattice lies outside each port's Hardy half-plane: −a_m ∈ C_− for G_+^0, a_m ∈ C_+ for G_-^0.
(iii) Hardy membership imposes no condition on the values of the entire continuation there: for any
v ∈ C^L take g ∈ C_c^∞((T,T+1)) with ∫g(t)e^{a_m t}dt = v_m (the exponentials e^{a_m t} are linearly
independent on (T,T+1)); then e^{Tz}ĝ(z) ∈ H²(C_+), ĝ entire, ĝ(−a_m)=v_m. So H² ∩ entire realizes every finite
value vector at −a_m.
(iv) Falsifiers kill any variant: Theorem 1.3 holds for every F (F1: includes λ>0 eigenvectors with R_LF≠0);
it is linear in F (F2, F4); it uses neither Λ*1=log nor the Euler product (F3); for Davenport–Heilbronn,
L(s)=χ_L(s)L(1−s) with the same Γ-factor type, trivial zeros at −2m−κ, and R162_102 Prop 2.1 supplies a
first-contact mode with R_LF≠0, while its product port L·H_+ is still right-causal (L is an absolutely
convergent Dirichlet series on Re s>1, so the proof of R161_008 Thm 3.1 goes through). Thus reflection +
Hardy membership is satisfied by a nonzero-residue DH mode. ∎

## 3. Where the Euler product enters

- Lemma 1.1, 1.2, Theorem 1.3(a)–(f), (1.1), Prop 2.1: **functional equation only**, plus ζ(−2m)=0 simple
  (from the Gamma poles) and ζ(s_m)≠0. The last is Dirichlet-series positivity (ζ(σ)>1), not the Euler product;
  for DH the analogue L(s_m)≠0 holds for m large by absolute convergence (a(1)=1) but is not automatic for small m.
- The only Euler input anywhere in the reflected picture is the **sign/size of d_m** in (d):
  d_m = Σ Λ(n)n^{−s_m} ∈ (0,q_0]. Reflected, this is a nontrivial arithmetic statement about the
  second Taylor coefficient at the trivial zeros:
  0 < ½ζ''(−2m)/ζ'(−2m) − log π + ½ψ(m+1) + ½ψ(m+½) ≤ q_0.
  But by eq:equivgate this positivity gives no leverage (j=Dx is equivalent-in-notation to the target).

## 4. Falsifier table

| test | result |
|---|---|
| F1 | fails as a closing tool: dictionary valid for every F |
| F2 | linear; invariant under the sign reversal |
| F3 | Euler/Λ*1=log absent except through d_m positivity (no leverage); DH shares everything |
| F4 | no limit taken; identities exact at finite data |
| DH | explicit nonzero-residue DH first-contact mode satisfies all of §1–2 |

## 5. Verdict and next sub-lemma

Status: **PROVED STEP** (exact reflected dictionary (1.1); polar layer and prehistory provably invisible at the
reflected lattice) and **NO-GO** for the Hardy pole/zero mechanism. Gate 1 OPEN; Row D OPEN.

Next sub-lemma (G2.1, Euler-stripped trivial-zero regularity). By (1.1) Gate 1 is: the logarithmic port
H_+ = −(ζ'/ζ)K_F − Q_+ has no pole at s=−2m. Its finite-N Euler-stripped version
H_{+,N} = A_N K_F − Q_{+,N} (A_N = Σ_{n≤N}Λ(n)n^{−s}, entire) has no such poles; the pole appears only in the
limit, through the continuum renormalisation of R162_305 §4. G2.1: find an oriented finite-N identity at
first contact (using minimality of T_* and Λ*1=log in the interior divisor defect B_a of R162_204) that
controls the *growth in N* of H_{+,N}(−a_m) − [continuum] (the regularised Σ_{n≤N}Λ(n)n^{2m} moment of F);
boundedness in N of that quantity is expected (NOT proved; first task of G2.1) to be equivalent to K_F(a_m)=0. Must fail at DH (no interior divisor defect).

Files edited: this file only.
