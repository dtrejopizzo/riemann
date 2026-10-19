# R162_401 — G1: the log-weighted (dilation) channel at first contact

Round 4, mechanism G1.

Status: **NO-GO (PROVED), with one PROVED STEP.** Gate 1 is not closed.

- PROVED STEP (§2–§3). The log-weighted channel does survive in Gamma coordinates. At finite N it
  carries σ'_{2j}(N) = Σ_{n≤N}(log n)n^{2j}. Its continuum-renormalized value is −ζ'(−2j), and
  γ_j·(−ζ'(−2j)) = −ζ(2j+1) = −ζ(s_j) **exactly**. So the X-direction sees the residue data
  ζ(s_m)K_F(a_m) of eq:residue, with coefficient 1.
- NO-GO (§4). In the PC identity this channel occurs in exactly two slots. One is the LHS, through
  M𝓕 = X𝓕 + 𝓕X. The other is the RHS, through the K_N𝓕 inside H_{M,N}𝓕. The two copies are the same
  series with the same scalar σ'_{2j}(N) for every N, so they cancel identically. The cancellation is
  [X,S_N] = −K_N applied to the Gamma series of 𝓕F: the log channel is the X-derivative of the value
  channel, and X is the generator of the Gamma factor (M = X + 𝓕X𝓕). The Chebyshev-jet channel
  ζ'(s_m)K_F(a_m) (the product d_m·ζ(s_m)) appears only in X-commutators of PC and cancels there too
  (§5). Combined with eq:Qbalance, nothing is left that could force R_LF = 0 (§6).

Notation: Paper 47 §sec:firstcontact. Write μ_F(a) := ∫ e^{at}F(t)dt, so μ_F(a) = εK_F(a) when
JF = εF. Also e_a(t) := e^{at}, a_j = 2j+½, s_j = 2j+1, σ_k(N) := Σ_{n≤N} n^k, and
σ'_k(N) := Σ_{n≤N}(log n) n^k. Real pairing ⟨h,g⟩ = ∫hg.

## 1. The Gamma series and its pairing at finite N (PROVED)

**Lemma 1.1.** Let F ∈ L²(I_T). Then 𝓕F(t) = Σ_{j≥0} γ_j μ_F(a_j) e^{a_j t} for all real t, with
γ_j = 2(−1)^j(2π)^{2j}/(2j)!. For |μ_F(a_j)| ≤ √(2T)e^{a_jT}‖F‖ the series converges absolutely
and locally uniformly. The j = 0 term is the Tate moment μ_F(½), which is 0 on P_T.

*Proof.* F(t) = e^{t/2}f(e^t) with f even and supported in e^{−T} ≤ |y| ≤ e^T. So f̂ is entire and
equals Σ_k (−2πix)^k/k! ∫y^k f. Only even k survive, and 2∫_0^∞ y^{2j} f dy = 2μ_F(a_j). Absolute
convergence: Σ(2πe^{t}e^{T})^{2j}/(2j)! < ∞. ∎

**Lemma 1.2 (exact finite-N pairings).** Let F, g ∈ L²(I_T) and N ≥ 1. Then

    ⟨S_N𝓕F, g⟩  = Σ_j γ_j μ_F(a_j) μ_g(a_j) σ_{2j}(N),
    ⟨K_N𝓕F, g⟩  = Σ_j γ_j μ_F(a_j) μ_g(a_j) σ'_{2j}(N),
    ⟨S_N X𝓕F, g⟩ = Σ_j γ_j μ_F(a_j) [σ_{2j}(N) μ_{Xg}(a_j) + σ'_{2j}(N) μ_g(a_j)],
    ⟨S_N L_M^*𝓕F, g⟩ = Σ_j γ_j μ_F(a_j) μ_g(a_j) σ_{2j}(N) d_{j,M},   d_{j,M} = Σ_{d≤M}Λ(d)d^{−s_j},
    ⟨S_N L_M𝓕F, g⟩  = Σ_j γ_j μ_F(a_j) μ_g(a_j) σ_{2j}(N) ψ_{2j}(M),  ψ_{2j}(M) = Σ_{d≤M}Λ(d)d^{2j}.

All the series converge absolutely.

*Proof.* n^{−1/2}τ_{log n}e_a = n^{a−1/2}e_a. For a = a_j this is n^{2j}e_a. Also
τ_{log n}(t e_a) = (t + log n)n^a e_a, and ⟨e_a, g⟩ = μ_g(a), ⟨t e_a, g⟩ = μ_{Xg}(a). Finite sums
in n and d commute with the absolutely convergent j-series (majorant
Σ(2πNMe^{2T})^{2j}/(2j)!). ∎

The d_{j,M} of Lemma 1.2 is **the collar weight** of eq:collar: d_{j,M} = d_{j,N} for M = N, and it
tends to −ζ'/ζ(s_j).

## 2. Continuum renormalization of both channels (PROVED)

Let C_N be the polar layer of rem:Sren and put K_N^C := −[X, C_N].

**Lemma 2.1.** C_N e_{a_j} = N^{s_j}/s_j · e_{a_j}. Also
K_N^C e_{a_j} = (N^{s_j}log N/s_j − N^{s_j}/s_j²) e_{a_j} = (∫_0^N x^{2j}log x dx) e_{a_j}. Hence
[X, S_N^ren] = −K_N^ren exactly, with K_N^ren := K_N − K_N^C.

*Proof.* With b = a+½: e^{−t/2}∫_{−∞}^{t+log N} e^{bu}du = N^b e^{at}/b, and
e^{−t/2}∫_{−∞}^{t+log N}(t−u)e^{bu}du = e^{at}N^b(−log N/b + 1/b²). ∎

**Proposition 2.2 (the renormalized constants).** By Euler–Maclaurin, for each fixed j,

    σ_{2j}(N) − N^{s_j}/s_j = ζ(−2j) + P_j(N) + o(1) = P_j(N) + o(1),
    σ'_{2j}(N) − ∫_0^N x^{2j}log x dx = −ζ'(−2j) + P'_j(N) + o(1),

where P_j and P'_j are explicit boundary terms (N^{2j}/2, N^{2j}log N/2, and Bernoulli terms in
N^{2j−2i+1}, N^{2j−2i+1}log N). They have no constant term. The constants are

    ζ(−2j) = 0,   −ζ'(−2j) = (−1)^{j+1}(2j)! ζ(2j+1) / (2(2π)^{2j})   (j ≥ 1),

and therefore

    γ_j · (−ζ'(−2j)) = −ζ(2j+1) = −ζ(s_j).                                          (2.1)

For j = 0 the constants are ζ(0) = −½ and −ζ'(0) = ½log 2π.

*Proof.* The first two are standard, with constant = the analytic continuation of Σn^{−s},
−∂_sΣn^{−s} at s = −2j. The formula for ζ'(−2j) follows by differentiating ζ(s) = χ(s)ζ(1−s)
at the trivial zero. Then (2.1) is arithmetic:
2(−1)^j(2π)^{2j}/(2j)! · (−1)^{j+1}(2j)!ζ(2j+1)/(2(2π)^{2j}) = −ζ(2j+1). Check at j = 1:
ζ'(−2) = −ζ(3)/(4π²). ∎

So the the insight is correct on the channel level. The **formal** renormalized log pairing is

    ⟨K^ren𝓕F, g⟩_fp = −Σ_{m≥1} ζ(s_m) μ_F(a_m) μ_g(a_m) =: −𝔅(F, g),                  (2.2)

with coefficient exactly ζ(s_m). This is the residue data of eq:residue: x_m = ζ(s_m)b_mK_F(a_m) up
to the damping b_m. The value channel gives 0 for every j ≥ 1, as in E1 §4. On primitive pairs the
j = 0 (Tate) terms vanish because μ_F(½) = μ_g(½) = 0.

**Remark 2.3 (divergence).** 𝔅 is not a convergent form on L²(I_T) × L²(I_T): |μ_F(a_m)| can be of
size e^{a_mT}, while ζ(s_m) → 1. It converges for tests whose moments decay faster than e^{−2a_mT},
for example after the Gamma damping b_m² of eq:Gammaenergy. This matches rem:Sren: exponential
tails keep their residues under renormalization. For this reason §4 argues at **finite N**, where
every series converges (Lemma 1.2), and uses (2.2) only as the name of the constant.

## 3. Where the log channel enters eq:PCfinite (PROVED)

Pair eq:PCfinite with F ⊗ g, where F, g ∈ L²(I_T) are arbitrary (in particular g = ΠS_LF). Use
M𝓕 = X𝓕 + 𝓕X, which follows from X + 𝓕X𝓕 = M and 𝓕² = 1. Every term splits into:

- **Gamma-channel terms**, where 𝓕 acts before a comb: S_N X𝓕, S_N𝓕X, XS_N𝓕, S_N𝓕X,
  L_M^*S_N𝓕, L_MS_N𝓕, K_N𝓕. By Lemma 1.2 these are j-series whose multipliers lie in
  {σ_{2j}, σ'_{2j}, σ_{2j}d_{j,M}, σ_{2j}ψ_{2j}(M)}.
- **J-orientation terms**: XJS_N, JS_NX, L_M^*JS_N, JL_MS_N, JK_N. These have compact support, and
  for N ≥ e^{2T} they do not depend on N.

**Table (log-channel content, i.e. terms carrying σ'_{2j}).**

| slot | term | log-channel part |
|---|---|---|
| LHS | S_N M𝓕 ⊃ S_N X𝓕 | +Σγ_jμ_F(a_j)μ_g(a_j)σ'_{2j}(N) |
| LHS | S_N𝓕X, −S_N(L_M+L_M^*)𝓕 | none (multipliers σ, σd, σψ) |
| RHS | {X,E_N} ⊃ XS_N𝓕 + S_N𝓕X | none (σ only: X acts after the comb or before 𝓕) |
| RHS | −L_M^*E_N | none |
| RHS | −H𝓕 = −L_MS_N𝓕 + K_N𝓕 | +Σγ_jμ_F(a_j)μ_g(a_j)σ'_{2j}(N) |
| RHS | −JH, J-parts of {X,E_N} and L_M^*E_N | none (compact) |

## 4. The exact cancellation (PROVED): NO-GO for the log channel

**Theorem 4.1.** For all M, N ≥ 1 and all F, g ∈ L²(I_T):

- (a) The log-channel parts of the two sides of eq:PCfinite are equal term by term: in both,
  Σ_jγ_jμ_F(a_j)μ_g(a_j)σ'_{2j}(N). They cancel identically.
- (b) The remaining Gamma-channel parts cancel identically. The value multipliers σ_{2j} pair up
  inside {X, S_N𝓕} against S_N𝓕X and XS_N𝓕 ⊂ S_NX𝓕. The d_{j,M} and ψ_{2j}(M) multipliers cancel
  between −S_N(L_M+L_M^*)𝓕 and −L_M^*S_N𝓕 − L_MS_N𝓕.
- (c) The J-orientation parts cancel identically, by J[X,S_N] = −JK_N and JL_M = L_M^*J.

So the paired identity is 0 = 0 separately in each of the three channels (value, log, compact),
for every F and g. The same holds after replacing (S_N, K_N) by (S_N^ren, K_N^ren), by Lemma 2.1,
and after any linear finite-part functional in N. In particular the renormalized form −𝔅(F,g) of
(2.2) appears on both sides and cancels. The polar layer contributes equally to both sides, because
[X, C_N] = −K_N^C is exact.

*Proof.* (a) Lemma 1.2 and the table. (b) The σ-terms: S_NX𝓕 − XS_N𝓕 = K_N𝓕 exactly. What is left
of S_N X𝓕 after removing its σ' part is ⟨σ μ_{Xg}⟩, which equals ⟨XS_N𝓕F,g⟩. S_N𝓕X occurs once on
each side. The L-terms are identical as operators, because translations commute. (c) As in the
proof of thm:PCfinite. ∎

**The exact new cancellation.** In the Gamma coordinates the PC identity is the scalar identity

    S_N X e_a − X S_N e_a = σ'(a; N) e_a,   σ(a; N) = Σ_{n≤N} n^{a−½},

that is, **[X, S_N] = −K_N evaluated on the Gamma series of 𝓕F**. The log weight is ∂_aσ(a), and
the X in the LHS comes from the Gamma factor itself (M𝓕 = X𝓕 + 𝓕X). So the ζ(2j+1) that the
Gamma factor contributes on the LHS is the same ζ(2j+1) that K_N contributes on the RHS. The
trivial-zero cancellation of E1 kills the value channel by ζ(−2j) = 0. This second cancellation
kills its derivative by identity, not by a zero value. It is **not** archimedean-accidental; it is
the defining commutator of the identity.

## 5. The Chebyshev-jet channel and the mixed variations (PROVED)

The jet j_m = −ζ'(s_m)b_mK_F(a_m) = d_m x_m would need a Gamma-channel multiplier d_{j,M}·σ'_{2j}(N).
Its renormalized value is γ_j·d_j·(−ζ'(−2j)) = −d_jζ(s_j) = ζ'(s_j). By Lemma 1.2 this multiplier
occurs only for the operator L_M^*K_N𝓕 (or K_NL_M^*𝓕). That operator is absent from eq:PCfinite.

**Proposition 5.1.** Let 𝒜 be the algebra generated by X, J, 𝓕, finite translation sums with
arbitrary coefficients, and the continuum layers C_N. Every identity obtained from eq:PCfinite
inside 𝒜 is an algebraic identity valid for all sources and tests. This covers commutators with X
([X, PC], which is the only source of L_M^*K_N𝓕), the mixed variations ∂_u{X, E_N} and ∂_u K_N
along a_u = Λ + uη, and any finite-part functional in N. Its jet-channel parts cancel in pairs.
In particular:

- ∂_uK_N = 0 and ∂_u{X, E_N} = 0 (K_N, E_N, X do not depend on the coefficients; Lemma 1.1d of
  R162_305).
- In [X, PC] the term K_NL_M^*𝓕 arises on the LHS as −[X,S_N]L_M^*𝓕. On the RHS it arises as
  L_M^*[X, S_N𝓕] ⊂ [X, L_M^*E_N]. The two are equal, since the translations commute.
- The log-weighted Λ-operator [X, L_M^*] = Σ Λ(d)(log d)d^{−1/2}τ_{−log d} has Gamma multiplier
  σ_{2j}(N)·Σ Λ(d)log d·d^{−s_j}. After renormalization this is ζ(−2j)·(…) = 0: the value
  channel again.

*Proof.* Each is a finite rearrangement of commuting translation sums together with
[X, τ_a] = −aτ_a and M𝓕 = X𝓕 + 𝓕X. Apply Lemma 1.2 term by term. ∎

**Corollary 5.2 (where Λ can enter the Gamma channel).** In eq:PCfinite and in all of its
𝒜-consequences, the coefficients Λ enter the Gamma channel only multiplied by σ_{2j}(N). Their
renormalized value is ζ(−2j) = 0. The surviving channel ζ(s_j) (log) comes from the integer comb
alone and is Λ-free. The Λ-bearing channel ζ'(s_j) (jet) survives renormalization but cancels in
pairs (Prop. 5.1).

## 6. Combination with the first-contact equality (PROVED): no forcing

The first-contact inputs are H_TF = 0 and eq:Qbalance (0 = 2c_{N,L} + Q_{N,L}). By Theorem 4.1 and
Prop. 5.1, the log and jet channels add to this system only the identity 0 = 0 on P_T × P_T. So the
combined system is eq:Qbalance alone. By eq:Qrecombine that is a rearrangement of
𝔞_T(F, ΠS_LF) = 0, and by eq:equivgate forcing R_LF = 0 from it is equivalent to the conclusion.

Compressed Gamma form check. 𝔪_T(F, g) = ⟨XF, g⟩ + ⟨X𝓕F, 𝓕g⟩ is the only Gamma object in
eq:Qfull. In Gamma coordinates it is ∫ t·(Σγ_jμ_F e_{a_j})(Σγ_kμ_g e_{a_k}) dt (convergent, since
𝓕F is Schwartz at +∞). It contains **no** ζ(s_j). So the log channel cannot be matched to any term
of eq:Qbalance either.

**Theorem 6.1 (answer).** Take the log-weighted analogue of the E1 computation, retaining both
orientations, the polar layer C_N and K_N^C, the Tate endpoint (j = 0: ζ(0) = −½ and
−ζ'(0) = ½log 2π, both multiplied by μ_F(½) = 0 or μ_g(½) = 0 on primitive pairs), and the crossed
Tate term Re⟨r, S_LF⟩ (unchanged, since it lies in eq:Qbalance only). Then:

- The log channel survives renormalization, with coefficients ∝ ζ'(−2j), exactly −ζ(s_j) after the
  factor γ_j, giving the bilinear form −𝔅(F, g) = −Σζ(s_m)μ_F(a_m)μ_g(a_m).
- 𝔅 appears twice in the paired eq:PCfinite and cancels identically (Thm 4.1a).
- Together with H_TF = 0 and eq:Qbalance it does **not** force R_LF = 0.

## 7. Falsifiers

- **F1.** Theorem 4.1 holds for every F, including eigenvectors with λ > 0 and R_LF ≠ 0. λ = 0 is
  never used, so the channel cannot close Gate 1. This is the NO-GO in falsifier form.
- **F3 (finite modifications).** Replace Λ by Λ + η_0 with η_0 finite. The Gamma-channel log
  content is unchanged, since it comes from K_N, which is integer-comb only. The interior defect of
  thm:finmod (at k ≤ N) sits in H, whose Gamma part renormalizes to ψ·ζ(−2j) = 0 plus the K_N term
  that cancels. So the channel cannot distinguish Λ.
- **F3 (Davenport–Heilbronn).** DH has the same Gamma factor, so the same trivial zeros at −2j and
  the same derivative −L'_DH(−2j) ∝ L_DH(2j+1), via its functional equation. Its analogue of (2.1)
  gives the residues L_DH(s_j)K_F(a_j). Theorem 4.1 is coefficient-free, so the same cancellation
  holds verbatim. No Euler product is used. The channel is DH-blind, which is consistent: a
  closure through it would also kill DH first-contact vectors, which is false.
- **F4.** Renormalization is a linear finite-part functional. By F4 it could not prove vanishing,
  and here it yields exactly 0 = 0.

## 8. Consequences and exact next sub-lemma

- The E1 obstruction (value channel = ζ(−2j) = 0) has a companion. The derivative channel
  (ζ'(−2j) ∝ ζ(s_j)) is nonzero, but it is cancelled by [X, S_N] = −K_N itself, because the Gamma
  factor is the X-generator (M = X + 𝓕X𝓕). Every operator in 𝒜 built from the integer comb has
  renormalized Gamma multiplier in span{ζ^{(k)}(−2j)}. These multipliers are either 0 (k = 0) or
  appear in commutator pairs.
- To break both cancellations, a comb **without trivial zeros** and not in 𝒜 is needed. The
  natural candidate is the partial Euler product comb
  S^{(P)} = Π_{p≤P}(1 − p^{−1/2}τ_{log p})^{−1} (smooth-number comb). On e_{a_j} its value multiplier
  is ζ_P(−2j) = Π_{p≤P}(1 − p^{2j})^{−1} ≠ 0, and its log derivative is multiplicative:
  −(ζ_P'/ζ_P)(−2j) = Σ_{p≤P} log p·p^{2j}/(p^{2j} − 1). This multiplier is Euler-specific, so it
  fails for DH, as F3 requires. However S^{(P)} has no additive Poisson partner (𝓕S^{(P)} ≠ JS^{(P)}
  formally).

**Next sub-lemma G1.2 (Euler-comb Poisson defect).** Derive the exact analogue of eq:PCfinite with
S_N replaced by the truncated smooth-number comb S^{(P)}_N. That is: compute E^{(P)}_N = S^{(P)}_N𝓕 − JS^{(P)}_N
and its Gamma-channel multiplier ζ_P(−2j) − ζ(−2j)·(…) = ζ_P(−2j). Then decide whether its pairing
with F ⊗ ΠS_LF at first contact produces a term Σ_m ζ_P(−2j)·(…)·K_F(a_m)K_g(a_m) that is **not**
cancelled by a commutator partner, and that is comparable with c_{N,L} in eq:Qbalance. Before
building: corpus-check against R162_301 (C1 Euler lift NO-GO), R162_202 (multiprime Sonin leakage)
and R160 survey, since the Brown–Halmos half-line leakage of C1 may be the same object.

GATE 1: OPEN. Row D: OPEN.

Files edited: this file only.
