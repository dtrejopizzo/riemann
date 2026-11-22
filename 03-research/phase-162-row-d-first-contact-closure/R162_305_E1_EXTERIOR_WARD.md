# R162_305 — E1: exterior Ward feasibility (Sub-lemma C2.1)

Mechanism E1.

Status: **NO-GO (PROVED). Gate 1 is not closed.** Every term of the finite PC identity and of the
collar balance has been differentiated along the exterior direction. Two facts result:

- The collar balance (eq:Qbalance/eq:Qfull) is invariant **term by term**, up to the pair
  (δc, δQ) = (+κ, −2κ) with κ := ⟨R_LF, δD R_LF⟩.
- The u-derivative of eq:PCfinite is an **algebraic identity**. It holds for every source F and
  every test g, and it cancels in two blocks:
  - the Ward slot cancels against the LHS term S_N L^η 𝓕;
  - the backward term (L^η)^*E_N cancels against S_N (L^η)^* 𝓕 once the J-part is removed by
    compression.

So the Ward slot never produces a quadratic form that could be compared with the collar shift. It
contributes exactly 0 net, for every F in P_T, whatever the sign of H_T on F. Route (ii) of R162_302
is closed completely. The suspected tautology is confirmed, and its mechanism is identified in §4.

Notation: Paper 46 §sec:firstcontact. We write T = T_*. The direction η is real and finitely
supported, with supp η ⊂ [e^{2T}, M]. Put a_u = Λ + uη and
L^η := Σ_d η(d) d^{-1/2} τ_{log d}, so that L_M^{(u)} = L_M + uL^η. Throughout, M ≥ N ≥ max supp η.

## 1. What does not move (PROVED)

**Lemma 1.1.** For every u:

- (a) P L^η P = P (L^η)^* P = 0. Hence H_T^{(u)} = H_T, the form 𝔞_T is unchanged, and so are the
  radical, the parity ε and the first-contact window T_*.
- (b) The Tate vector r of eq:localweak does not depend on u.
- (c) B_N^{(u)} = B_N and the backward moments R_L B_N^* F are unchanged.
- (d) The compressed Gamma form 𝔪_T, the continuum polar layer C_N (Rem. rem:Sren), K_N, S_N, 𝓕,
  X and E_N do not depend on the coefficients.

*Proof.*
- (a) For d ≥ e^{2T}, τ_{log d} maps functions supported in [−T, T] to functions supported in
  [−T − log d, T − log d] ⊂ (−∞, −T]. Hence P τ_{±log d} P = 0. The primitive form only involves
  the compressed comb, which is unchanged. The first-contact property is decided by the H_{T'} with
  T' ≤ T. These depend only on n < e^{2T'} ≤ e^{2T}, which lies outside supp η.
- (b) r is defined by 𝔞_T(F, G) = ⟨r, G⟩, and neither side changes.
- (c) The same support argument applies.
- (d) These operators are built from the integers alone. ∎

## 2. The collar balance: exact derivative (PROVED)

Put δD := diag(δd_m) with δd_m := Σ_n η(n) n^{-(a_m+½)}. This quantity is finite and has no sign,
because η has no sign.

**Lemma 2.1.** d/du D_{N,L} = δD_L. Also d/du 𝓔_{N,L} = δD_L R_L, **exactly**, on all of L²(I_T).

*Proof.* For n ≥ e^{2T}, the lower limit max(−T, T − log n) equals −T, so the n-summand of
(𝓔_N F)_m equals b_m η(n) n^{-(a_m+½)} K_F(a_m). ∎

**Proposition 2.2.** Differentiate every term of eq:Qfull and eq:Qbalance at u = 0:

| term | d/du |
|---|---|
| 2Re⟨R_LF, R_LB_N^*F⟩ | 0 (Lemma 1.1c) |
| −2Re⟨R_LF, 𝓔_{N,L}F⟩ | −2⟨R_LF, δD R_LF⟩ |
| −Re 𝔪_T(F, S_LF) | 0 |
| Re⟨r, S_LF⟩ (crossed Tate endpoints) | 0 (Lemma 1.1b) |
| 2c_{N,L}(F) | +2⟨R_LF, δD R_LF⟩ |

The sum is 0 **for every F in the domain of H_T**, not only on the radical. The same holds for
eq:Qrecombine and eq:Qspectral: there λ and d_{m,N} + λ shift consistently, and d_{m,N} ↦ d_{m,N} + uδd_m.

*Proof.* Combine Lemma 1.1 and Lemma 2.1. The identity eq:Qbalance comes from eq:localweak together
with eq:collar. It contains no hyperbola remainder, so the Ward defect cannot appear in it. ∎

So along the exterior direction, the collar balance moves by the pair (+κ, −2κ) and nothing else.

## 3. The PC identity: exact derivative, both orientations (PROVED)

For a_u, eq:PCfinite reads S_N A_M^{(u)} 𝓕 = {X, E_N} − (L_M^{(u)})^* E_N − JH^{(u)} − H^{(u)} 𝓕, with
H^{(u)} = L_M^{(u)} S_N − K_N. Its u-derivative is (R162_205 (2.2))

    −S_N(L^η + L^η*)𝓕 = −(L^η)^* E_N − J D^η − D^η 𝓕,    D^η := L^η S_N.        (3.1)

The coefficients of D^η are

    D^η = Σ_k w(k) k^{-1/2} τ_{log k},   w(k) = Σ_{dm=k, d≤M, m≤N} η(d).

Its interior truncation at k ≤ N is exactly the Ward slot u(η*1)(k) of R162_204/205, because every
divisor d ≤ k ≤ N ≤ M is admitted. Every k with w(k) ≠ 0 satisfies k ≥ min supp η ≥ e^{2T}.

**Theorem 3.1 ((3.1) is an algebraic zero).** Identity (3.1) holds on the Schwartz core for every
source, independently of first contact, of the value of the Weil form, and of the coefficients
Λ. Concretely, after expanding E_N = S_N 𝓕 − J S_N, the six terms cancel in the following pairs:

- (W) Ward slot, 𝓕-orientation: −D^η𝓕 = −S_N L^η 𝓕, which cancels the LHS term −S_N L^η 𝓕;
- (J) Ward slot, J-orientation: −J L^η S_N = −(L^η)^* J S_N, which cancels the term +(L^η)^* J S_N
  coming from −(L^η)^*E_N;
- (B) backward: −(L^η)^* S_N 𝓕, which cancels the LHS term −S_N (L^η)^* 𝓕.

*Proof.* The finite translation sums commute, and J L^η = (L^η)^* J. ∎

**Corollary 3.2 (pairing with F ⊗ ΠS_LF).** Let F ∈ L²(I_T) and g = ΠS_LF. Pair (3.1) with g. The
J-orientation terms vanish separately:

- ⟨J D^η F, g⟩ = 0, because D^ηF is supported in (−∞, −T] (k ≥ e^{2T});
- ⟨(L^η)^* J S_N F, g⟩ = 0, because J S_N F is supported in [−T, ∞), and τ_{−log d} moves it into
  [log d − T, ∞) ⊂ [T, ∞).

So compression removes (J) as the suspected tautology, 0 = 0. The 𝓕-orientation terms (W) and (B)
survive compression, because 𝓕F is not compactly supported. They cancel exactly against the LHS in
pairs, as in Theorem 3.1. The net contribution of the Ward slot to the paired identity is

    ⟨D^η𝓕F, g⟩ − ⟨S_N L^η 𝓕F, g⟩ = 0,

identically in F and g.

The crossed Tate endpoint term is Re⟨r, S_LF⟩. It does not move (Lemma 1.1b). The continuum polar
layer C_N does not depend on the coefficients, so its derivative is 0. It enters only if one renormalizes S_N ↦ S_N^{ren}, and then it
does so identically on both sides of (3.1).

**Theorem 3.3 (answer to C2.1).** Retain all terms (both orientations, polar layer, Tate endpoints,
full collars). Then the total u-derivative at u = 0 of the combined system {eq:PCfinite paired with
F ⊗ ΠS_LF, eq:Qbalance} is the zero functional on P_T × P_T. The Ward slot contributes 0, not a
quadratic form in (K_F(a_m)). Its difference from the collar shift, −(−2κ) = 2κ, is **not** of the
form c‖R_LF‖² with c ≠ 0 as a consequence of any identity. The collar shift is already cancelled
inside eq:Qbalance by δc = +κ (Prop. 2.2). The Ward slot is cancelled inside (3.1) by its own LHS
partner (Thm 3.1). There is no cross-cancellation between the two identities that could leave a
residual. Therefore neither alternative of C2.1 yields F = 0. The "identically equal" alternative
holds in the stronger form that each block is separately identically zero.

The family is also exactly affine in u. Both identities are linear in the coefficients, so all
higher u-derivatives vanish too. No non-perturbative information is available along exterior
directions beyond the u = 0 identities themselves.

## 4. Why the Ward slot is silent: the trivial zeros (PROVED to the stated extent; remark)

One can ask what the surviving 𝓕-orientation pairing ⟨S_N(L^η)^*𝓕F, g⟩ sees in Gamma-residue
coordinates. Write F(t) = e^{t/2}f(e^t) with f even. The left tail of 𝓕F (t → −∞) is the Taylor
series of f̂ at 0:

    𝓕F(t) = Σ_{j≥1} γ_j ε K_F(a_j) e^{a_j t},    γ_j = 2(−1)^j (2π)^{2j}/(2j)!.

This series is entire and exact for all t. The j = 0 term is the Tate moment, which vanishes on P_T.
So the left tail is exactly a generating function of the Gamma residues K_F(a_j) (the moments of f
are ∫F(t)e^{a_j t}dt = εK_F(a_j)).

Consider the part of ⟨S_N(L^η)^*𝓕F, g⟩ with n ≤ d e^{-2T}. It samples only the left tail and equals

    Σ_{j≥1} γ_j K_F(a_j) K_g(a_j) · [Σ_d η(d) d^{-(a_j+½)}] · [Σ_{n ≤ d e^{-2T}} n^{a_j − ½}]
      = Σ_j γ_j K_F(a_j) K_g(a_j) · δd_j · (Hurwitz-type partial sum of ζ(−2j)).

The factor δd_j is exactly the collar weight of §2. The companion factor Σ n^{2j} is a partial sum
whose renormalized value (subtract the continuum C_N) is ζ(−2j) = 0. So the Ward direction does meet
the δD channel in Gamma-residue coordinates, but its multiplier is a trivial zero of ζ, up to
continuum and boundary terms. Theorem 3.1 shows that these terms are cancelled exactly by the LHS.
This is the precise sense in which "compression kills k ≥ e^{2T}". The J-orientation is killed by
support. The 𝓕-orientation is killed by ζ(−2j) = 0 together with the continuum layer, which is an
archimedean fact valid for every coefficient system. The form is also not diagonal: K_g(a_j), with
g = ΠS_LF, mixes all j through the Gram matrix of the e^{−a_m t} on I_T, and it involves j > L.

## 5. Falsifiers

- **F1 (minimality).** Theorem 3.3 holds for every F ∈ P_T, including eigenvectors with λ > 0 and
  R_LF ≠ 0 (eq:Qspectral). An identity with this property cannot imply R_LF = 0. So any closure
  along exterior directions would fail F1 automatically. This is the structural reason for the
  NO-GO.
- **F2 (sign reversal).** Identity (3.1) is linear and odd in η, and it is zero. It carries no
  orientation.
- **F3 (finite modifications).** Theorem 3.1 uses neither Λ*1 = log nor the Euler product. The same
  zero derivative holds at a = Λ + η_0 for every finite η_0. The exterior Ward slot is also, by
  definition, supported at k ≥ e^{2T}, where the interior identity Λ*1 = log is never used.
- **F4 (not a limit or a square).** There is nothing to square; the derivative is 0.
- **Davenport–Heilbronn.** DH has no Euler realization of (1.4) of R162_204. However, (3.1) is
  coefficient-free algebra, so an exterior perturbation of any Dirichlet coefficient system (DH
  included) gives the same zero. No DH-distinguishing content is present. This is consistent: a DH
  first-contact vector would otherwise be killed.

## 6. Consequences

- Sub-lemma C2.1: **NO-GO, PROVED** (Thm 3.3).
- Route (ii) of R162_302 is closed completely. After R162_304 (the α-route is equivalent to
  K^ε = {0}) and this note (exterior η is tautological), no coefficient-direction variation of the
  finite PC-ren/collar system carries information at first contact. Interior directions are
  vacuous (R162_302 Lemma 3.1). Exterior directions are algebraic zeros.
- One genuinely new structural fact comes out of §4. The only point where the exterior Ward
  direction touches the Gamma-residue channel δD, the multiplier is the trivial-zero value
  ζ(−2j) = 0. Any future identity that wants the Ward slot to act on (K_F(a_m)) must break this
  archimedean cancellation, for instance by a non-continuum renormalization of S_N. It must then
  answer to Problem prob:annihilate (ii)–(iii) directly.
- **GATE 1: OPEN.** Row D: OPEN.

Files edited: this file only.
