# R183.018 — Construction of the semilocal Sonin remainder and its inertia

## 0. Verdict

* Exact identity E_S = Son + R_{S,T} in R183.015's normalization,
  for every T and every admissible S: `PROVED` from CC (83), (152).
* For S={∞} and T≤½log 2: R ≥ −b|v><v| + c(I−|v><v|) with c>0 in CC's
  ξ metric. It is `CITED` (CC §6, rigorous numerical bounds) at T=½log 2. For
  T<½log 2 it is `PROVED` by Cauchy interlacing.
* Structure of the prime term in the window: a measurable direct sum of
  finite Toeplitz matrices. It has eigenvalues of both signs with
  infinite multiplicity: `PROVED`. It is neither finite rank nor compact.
* **NO-GO (PROVED).** If T>½log 2 and S contains all primes p<e^{2T},
  then R_{S,T} is negative definite on arbitrarily large-dimensional
  subspaces of primitive tests: n₋(R_{S,T})=∞. No inner product admits a
  bound with at most one negative direction. R183.017's obligation 2 is
  false, as stated, throughout the range once primes are present.
* This does not refute E_S≥0 nor CC's conjecture. It only refutes the
  claim that the *entire* Sonin trace is the positive part with a
  finite-rank defect. An open lemma remains (§6) about a different
  partition.

Neither RH nor the closure of D is claimed. The Sonin + remainder
mechanism is Connes–Consani's. What is new here is the computation of the
semilocal remainder and its inertia.

## 1. Source (local copy, 2006.13771v1)

Source: 00-references/2006.13771v1.pdf. The same text is in
phase-137/cc_2006.13771_text.txt. In v1 the numbering is Lemma 6.9 and
Theorem 6.11; R183.017 calls them "Lemma 9" and "Theorem 11", following
the html numbering.

* **Def. 4.4 (72).** S(α,β) := {ξ∈L²(R)^ev : ξ(q)=0 for |q|≤α,
  (F_{e_R}ξ)(p)=0 for |p|≤β}. **S** is the orthogonal projection onto S(1,1).
  By (81), S = R is the eigenvalue-1 part of P P̂ P.
* **Thm 4.7 (83)–(84).** For every f∈C_c^∞(R_+^*), with no support
  restriction: Tr(ϑ(f)S) = W_∞(f) + ∫f(ρ^{-1})ε(ρ)d^*ρ.
  Here ε(ρ^{-1})=ε(ρ) and, for ρ≥1, ε(ρ)=Σ_n λ(n)(1−λ(n)²)^{-1/2}⟨ξ_n|ϑ(ρ^{-1})ζ_n⟩,
  with ξ_n, ζ_n prolate vectors. Write E(f):=∫f(ρ^{-1})ε(ρ)d^*ρ (91).
* **(152)–(154).** W_∞(f)=∫ h_+(τ) f̃(1/2+iτ) dτ/2π, h_+(τ)=−log π+Re ψ(1/4+iτ/2)=2θ'(τ).
  This matches R183.015's m(s) and holds for every f; no polar term appears.
* **Lemma 5.4, (102).** ε'(1^+)=Σ λ(n)²(1−λ(n)²)^{-1}ξ_n(1)² ≈ 22.9965 > 0.
  Also E_+(Q_+f) = −2ε'(1^+)f(0) + ∫_0^∞(f(x)+f(−x))(Qε)(e^x)dx.
* **Prop. 5.5 (103)–(104).** Let I⊂[−log2,log2] with |I|≤log 2. Then
  N_I = −2ε'(1^+)(Id−K_I), where K_I has kernel
  (Qε)(e^{|x−y|})/(2ε'(1^+)) and is Hilbert–Schmidt.
* **§6, (134)–(137), Lemma 6.10, Thm 6.11 (141).** For I=[−½log2,½log2]:
  λ_max(K_I)≈1.05158 and λ₂(K_I)≤0.7722+0.00122. The vector ζ satisfies
  ⟨ζ|ξ₀⟩≈0.94865, with ξ₀ a normalized constant. One obtains
  ⟨ξ|N_Iξ⟩≤γ|⟨ξ₀|ξ⟩|², γ≈2.94355. For g supported in [2^{-1/2},2^{1/2}]
  and ĝ(−i/2)=0:
  W_∞(g*g^*) ≥ Tr(ϑ(g)Sϑ(g)^*) − c|ĝ(0)|²,  c=4γ/log 2,  13<c<17.
* **Why it stops at log 2.** Reduction (102)→(104) uses that
  f=η*ξ^* vanishes outside [−log2,log2]. Moreover, K_I's spectrum is only
  controlled numerically in that window (Remark 3.9(ii), §6; already
  recorded in 115_15 §2). Starting from the log 2 window, primes enter:
  the first is p=2, with 2T=log 2. CC work with S={∞}. The support of the
  functions g has length log 2; that of f=g*g^*, length 2·log 2.

**Dictionary.** t=log ρ and h(t)=g(e^t). With CC's conjugation Δ^{1/2}
(App. A), f=g*g^* turns into the autocorrelation c_h. g's support
on [2^{-1/2},2^{1/2}] corresponds to T=½log 2. Also ĝ(0)=∫h, and
ĝ(∓i/2) are the moments ∫h e^{±t/2}.

## 2. Corpus consulted

* R162_2602 Thm 4(c), Def 5, Thm 6: CC's partition is a "Thm 3(ii)"
  partition, and starting from log 2 the count n₋ inherits N(T). Thm 6(d) and
  Cor 7: N(T)→2κ_off, and sup N<∞ is the 8F/Pontryagin residue. **The
  present file refines Thm 4(c).** The Sonin remainder has n₋=∞ as soon as
  a single prime enters, unconditionally. Hence it is not even comparable
  to N(T).
* 115_15 §2–4: the bound |I|≤log 2 is used in the proof, and the count
  #{λ_j(K_I)>1} was not examined.
* R161_014: Sonin–Gamma coercivity for ports supported to the right
  of T. It is a different object (product port, not a window) and is not
  duplicated here.
* Grid R162_2300, row 2A: "115_13–16, phase derivative of the semilocal
  Sonin trace: favorable sign, no exact identity." **§3 supplies
  the exact identity.** Row 8D: closed by R162_2602.
* Paper 46 thm:P (Ky Fan ceiling) bounds the n₋ of the **total** Weil form
  on mode arenas. It does not contradict §5: there n₋ is finite because the
  unbounded Sonin part is included. Here it is subtracted.

## 3. Exact identity — PROVED (from CITED)

Let T>0, I_T=(−T,T), and S finite with ∞∈S and every prime p<e^{2T} in S.
For h∈C_c^∞(I_T), φ=ĥ and c_h(x)=∫h(t)conj h(t−x)dt, R183.015 gives

    E_S(h) = (1/2π)∫m|φ|² − Σ_{p∈S} 2log p Σ_{k≥1} p^{-k/2} Re c_h(k log p).

Define

    Son(h) := Tr(ϑ(g)Sϑ(g)^*) ≥ 0,
    R_{S,T}(h) := −∫_{−2T}^{2T} c_h(x) ε(e^{|x|}) dx
                  − Σ_{p<e^{2T}} 2log p Σ_{k: k log p<2T} p^{-k/2} Re c_h(k log p).

**Proposition 3.1.** E_S(h) = Son(h) + R_{S,T}(h) for every h∈C_c^∞(I_T).
No moment condition is required.

*Proof.* By (152) and the dictionary, the first term of E_S is W_∞(f),
with f=g*g^*. By (83), W_∞(f)=Tr(ϑ(f)S)−E(f). Moreover
Tr(ϑ(f)S)=Tr(ϑ(g)Sϑ(g)^*)=Son(h), by cyclicity: ϑ(g) is bounded and
Sϑ(g)^* is Hilbert–Schmidt, which is used in CC (4). In additive
coordinates, by (101), E(f)=∫c_h(x)ε(e^{|x|})dx. The integral is real because
ε is real and even and c_h(−x)=conj c_h(x). Its support is in [−2T,2T]. The
primes only contribute with k log p<2T, by support (R183.001 Thm 1). ∎

**Domain.** The natural Hilbert space is L²(I_T,dt) in the variable h.
There, R_{S,T} is a **bounded**, self-adjoint operator:
R_{S,T} = −C_ε − Σ_p B_p. C_ε is the integral operator with kernel
ε(e^{|x−y|}), continuous on I_T×I_T (ε continuous: CITED, (84) and App. F). Hence
C_ε is Hilbert–Schmidt and **compact**. B_p is the compression of
2log p Σ_k p^{-k/2}(τ_{ka}+τ_{−ka})/2, with a=log p. The evaluation
h↦ĥ(0)=∫h is bounded on L²(I_T), with norm (2T)^{1/2}; the same holds for
the two Tate moments. Son is not bounded on L² (logarithmic growth
of θ'), but it is a closable positive form. The identity holds on the
core C_c^∞.

## 4. Structure of the prime term — PROVED

Let a=log p<2T. For r∈[0,a) set n(r)=#{j≥0 : −T+r+ja<T}. Define
U: L²(I_T) → ∫^⊕_{[0,a)} C^{n(r)} dr by (Uh)(r)_j = h(−T+r+ja).

**Proposition 4.1.** U is unitary. Moreover U B_p U^{-1} = ∫^⊕ T_{n(r)}(σ_p) dr,
where T_n(σ) is the n×n Toeplitz matrix of the symbol

    σ_p(θ) = 2log p Σ_{k≥1} p^{-k/2} cos kθ
           = 2log p · (x cosθ − x²)/(1−2x cosθ+x²),   x=p^{-1/2}.

Consequently:

(i) n(r) takes at most two values, n₀=⌈2T/a⌉ and n₀−1, each on a
set of r of positive measure when a does not divide 2T. If a divides 2T,
n(r)=2T/a almost everywhere.

(ii) The spectrum of B_p is the union of the spectra of T_n(σ_p), with n in
those values. Each eigenvalue has infinite multiplicity, so
B_p is not compact.

(iii) If a<2T, some such n is ≥2. T_n(σ_p) has zero diagonal and
entry (0,1) equal to log p·p^{-1/2}≠0. Having zero trace and not being
zero, it has one eigenvalue >0 and another <0. Hence B_p has
positive and negative spectral subspaces of infinite dimension.

*Proof.* Writing t=−T+r+ja gives a measurable partition of I_T, and U is
unitary by Fubini. Translating by ka moves the index j to j±k within the
same fiber r and truncates at the edges; that is the Toeplitz matrix. The
geometric sum of σ_p converges because x<1. ∎

With several primes, the logarithms are incommensurable and the
fibration is no longer common. The NO-GO only needs one prime, but (iii)
shows that the prime term is a truncated Wiener–Hopf operator, not a
finite-rank perturbation. This answers Obligation 2(b).

## 5. Case S={∞} and NO-GO for T>½log 2

### 5.1 S={∞}, T≤½log 2 — CITED / PROVED

In CC's ξ variable (h=(½−∂)ξ, ξ∈C_c^∞(I_T), equivalent to
∫h e^{−t/2}=0), (142) and (103) give R_{∞,T}(h) = 2ε'(1^+)⟨ξ,(Id−K_{I_T})ξ⟩.
For T=½log 2, (135)–(137) and (134) give

    R ≥ −b|ζ><ζ| + c(I−|ζ><ζ|),
    b=2ε'(λ_max−1+ε₁),  c=2ε'(1−λ₂−ε₁)>0.

This is `CITED`, with α=⟨ζ|ξ₀⟩≈0.94865 and δ>0 in R183.017's sense.

For T<½log 2: K_I's kernel depends only on x−y, so
K_{I_T}=P_{I_T}K_{I_{½log2}}P_{I_T}. By Cauchy interlacing,
λ₂(K_{I_T})≤λ₂(K_{I_{½log2}})<1, and the same bound holds with v=P_{I_T}ζ.
This is `PROVED` (given the CITED input). The negative direction may
disappear; the single-negative-direction bound persists.

### 5.2 NO-GO theorem — PROVED

**Theorem 5.1.** Let T>½log 2, S⊇{∞}∪{p<e^{2T}}, and N≥1. There exists a
subspace V_N⊂C_c^∞(I_T) of dimension N, made of primitive tests
(∫h e^{±t/2}=0), on which R_{S,T}(h)<0 for every h≠0. Hence
n₋(R_{S,T}|primitives)=∞, also within ker(h↦∫h). Consequently, for
**no** inner product on the tests, no v, no b≥0, and no
c>0 does R_{S,T} ≥ −b|v><v| + c(I−|v><v|) hold. The same conclusion holds
with at most k negative directions, for any finite k.

*Proof.* Fix p=2 and a=log 2<2T. Let Λ be the finite set of offsets
k log q<2T, with q∈S. Let F=(Λ∪(Λ+a)∪(Λ−a)∪−(…))∖{0}, which is
finite. Choose w>0 smaller than ¼min{|y| : y∈Λ∖{0}} and take
t_1,…,t_N∈(−T+w, T−a−w) whose pairwise differences are more than 4w away
from F∪{0}. This is possible for small w, because 2T−a>0.

Fix c₀∈C_c^∞((−1,1)) real and nonzero, set c_w(t)=c₀(t/w) and
β=c_w''−c_w/4. By integration by parts β is primitive (R183.015),
β≠0, and its translates remain primitive. Define
h_j(t)=β(t−t_j)+β(t−t_j−a).

By the choice of w and the t_j, for x=Σ_j c_j h_j the only nonzero
correlation at an offset in Λ is that of each h_j's internal pair,
at exactly offset a=log 2. The cross-correlations between pairs and
each bump's self-correlation at offsets in Λ∖{0} vanish by support. Thus

    Σ_p 2log p Σ_k p^{-k/2} Re c_x(k log p) = 2log2·2^{-1/2}‖β‖₂² Σ|c_j|².

For the archimedean part, with M=sup_{|y|≤2T}|ε(e^{|y|})|,

    |∫c_x ε| ≤ M‖x‖₁² ≤ M·N·Σ|c_j|²·4‖β‖₁².

By scaling, ‖β‖₁ ≤ w^{-1}‖c₀''‖₁ + w‖c₀‖₁ and ‖β‖₂² ≥ ½w^{-3}‖c₀''‖₂² for
small w, so ‖β‖₁²/‖β‖₂² = O(w). Hence

    R_{S,T}(x) ≤ −‖β‖₂²Σ|c_j|²·(√2 log 2 − O(MNw)) < 0

for x≠0 and small w. The conclusion about forms follows from a
dimension argument. If R ≥ −b|v><v| + c(I−|v><v|), then R≥0 on
ker⟨v,·⟩∩V_2, which is nonzero, contradicting R<0 on V_2. With k
directions, use V_{k+1}. Imposing ∫h=0 reduces the dimension by one. ∎

**Remarks.** (a) The proof only uses |ε| bounded on [1,e^{2T}] and one
prime in the window. It is blind to which prime, and to deletion; it says
nothing about the sign of E_S. (b) E_S(x)=Son(x)+R(x) can be positive on
V_N: the Son part grows like w^{-3}log(1/w), faster than the prime part.
(c) In CC's ξ metric the phenomenon worsens. h=(½−∂)ξ makes
c_h(a)=c_ξ(a)/4+c_{ξ'}(a), and the prime term is not even bounded
relative to ‖ξ‖. (d) For T≤½log 2 there are no primes and R=−C_ε is
compact, consistent with §5.1.

## 6. What remains: the partition must give up part of Sonin

The NO-GO says that, for T>½log 2, the positive part cannot be the
entire Son. The weakest admissible form, not excluded by §5, is to
give up a (frequency-dependent) fraction of the Sonin trace.

**Open lemma (L-Son).** For T>½log 2 and S as above, there exist 0≤η<1
(or an operator 0≤H≤Id commuting with ϑ), b≥0, c>0, and a fixed vector
e_T∈L²(I_T) representing h↦∫h, such that, for every primitive
h∈C_c^∞(I_T),

    η·Son(h) − ∫c_h(x)ε(e^{|x|})dx
       − Σ_{p<e^{2T}} 2log p Σ_k p^{-k/2} Re c_h(k log p)
    ≥ −b|⟨v,h⟩|² + c‖h − ⟨v,h⟩v‖²_X,

where X is the norm of the closed form Son+‖·‖². It must also hold that
δ=(b+c)|⟨v,e_T⟩|²−b>0 (R183.017's threshold).

**Caveats, all PROVED in the corpus.**
(i) With η=1 the inequality is just E_S≥0 plus the threshold. There is no
gain unless the lemma is proved with η<1 from source data.
(ii) By R162_2602 Thm 4(b), any proof using only that the local factors
sum is blind to deletion. It must use that S contains **all**
p<e^{2T}.
(iii) The prime term requires high-frequency absorption. By
Prop. 4.1(iii), its positive part has infinite dimension and concentrates
at frequencies s≈2πj/log p. Hence η·Son must dominate
Σ_p σ_p(s log p) at large |s|, which is easy because θ'~log|s|. The
difficulty lies at low frequencies, which is exactly where
m(s)<0 (R183.016) and where ĝ(0)'s direction lives.

## 7. Status

```text
identity E_S = Son + R_{S,T} (every T, admissible S)          PROVED (from CC (83),(152) CITED)
R_{S,T} bounded on L²(I_T); archimedean part compact            PROVED (ε continuous: CITED)
evaluation ∫h and Tate moments bounded on L²(I_T)               PROVED
prime term = fiberwise Wiener–Hopf/Toeplitz, B_p not compact,
  eigenvalues of both signs with infinite multiplicity if p<e^{2T}  PROVED
S={∞}, T=½log2: one negative direction, δ>0                     CITED (CC Lemma 6.10, Thm 6.11)
S={∞}, T<½log2: at most one negative direction                   PROVED (interlacing) / CITED
T>½log2, S with primes: n₋(R_{S,T})=∞ on primitives               NO-GO (PROVED), Thm 5.1
R183.017's obligation 2 (whole Son)                               NO-GO for T>½log2
Lemma (L-Son) with η<1                                             OPEN
E_S ≥ 0 / CC conjecture / row D                                    OPEN
```

## 8. Review points

1. **CC→R183.015 dictionary.** It must be checked that (152) with h_+=2θ' and
   the conjugation Δ^{1/2} produce exactly (1/2π)∫m|ĥ|², with no residual
   polar term. It must also be checked that (83) holds in the
   additive version with f=c_h, including the sign of E(f)=∫c_hε(e^{|x|}).
   A global sign error in ε does not affect Thm 5.1, which only uses |ε|≤M.
2. **Continuity and boundedness of ε on [1,e^{2T}] for every T.** This is
   cited from (84) and App. F, whose explicit controls are given near [1,2].
   Outside that range only convergence of the series is used: it is the
   weakest step. However, ε∈L^∞_loc suffices. Even ε∈L¹_loc would not
   directly suffice: then ‖c_x‖_∞ ≤ ‖x‖₂² would have to be used, giving
   |∫c_xε| ≤ ‖ε‖_{L¹}·N·Σ|c_j|²‖β‖₂², with no small factor.
3. **§5.1 for T<½log2** inherits CC's numerical bounds (134)–(137). The
   compression K_{I_T}=P K P assumes kernel (104) depends on differences
   with the same normalization 2ε'(1^+), as read off (104). Also, the
   ξ metric requires ∫h e^{−t/2}=0, not the two moments.

## Note (R183_026)

In lemma (L-Son) of §6, requiring c>0 "in the norm X = Son + L²" is
incorrect for every T: the archimedean remainder is Hilbert–Schmidt on
L²(I_T). The correct metric is CC's ξ metric (of H^{-1} type in h),
which is the one R183_019 uses. N_T in R183_024 must be corrected the same way.
