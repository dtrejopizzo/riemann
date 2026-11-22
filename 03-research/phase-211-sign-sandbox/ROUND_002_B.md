# ROUND_002_B — The O(1) term Q₁ of the exterior form on the bulk prolate sector, as a matrix in the comb

Object: the exterior form 𝔔 of Paper 46 §sec:ext (def:ext, thm:ext-half, prop:ext-univ, lem:ext-cell, thm:ext-multi,
lem:ext-envelope, thm:ext-layer), restricted to the prolate sector span{ψ_4, ψ_8, …, ψ_{4K}} of K3_GAMMA_001, with the comb
replaced by an arbitrary weight w ≥ 0. Starting point: ROUND_001_B, Proposition 2.4 and "Next concrete step".
Notation as in ROUND_001_B: λ = e^T, N = λ², c = 2πN; universal frame ϱ on (1,∞), u(x) = e^{x/2}ϱ(e^x),
u_n(y) = u(y + log n)1_{y>0}, Ψ̌_ϱ = Σ_{n≥1} n^{−1/2}u_n; H(t) = Σ_{k≤t}1/k. For a comb weight w on n ≥ 2 put
W := w∗1 (so W(1) = 0, W = log for w = Λ) and H₁^w(t) := Σ_{k≤t} W(k)/k (so H₁^Λ = H₁ of Paper 46).
𝔔^w[ϱ] := 𝒲^w[Ψ̌_ϱ] is the complete form on the line with comb 2w(q)q^{−1/2} at ±log q, archimedean part and pole unchanged
(the convention of Paper 46 for 𝔔^{c′} and of K3_GAMMA_001 §2.3). The target is (★) as a statement about one quadratic form;
no equivalence of it with any other statement is used.

---------------------------------------------------------------------------------------------------------------------
## 0. Summary

1. The comb part of 𝔔^w is exactly linear in W = w∗1 and splits, for every datum, into a coherent part
   𝒟_w[ϱ] = 2∫_1^∞ H₁^w(t)|ϱ(t)|² dt (a nonnegative multiplication operator, monotone in w) and an incoherent part
   𝒪_w = Σ_{n≥2} W(n)ℬ_n with ℬ_n indefinite (Lemma 1.1, Proposition 1.2, PROVED). No product of weights, no w∗w and no
   other non-linearity in w can occur in any expansion of 𝔔^w: the only non-monotone content anywhere is 𝒪_w.
2. On the prolate sector the coherent comb matrix is a Gram matrix of a positive weight, hence positive semidefinite, for
   every N and K, with no asymptotics (Theorem 2.1, PROVED). Its limit is the Toeplitz matrix
   Σ_n (W(n)/n)·𝐆(n), 𝐆(n)_{jk} = (4/π)∫_{arcsec n}^{π/2} cos(4(j−k)θ)dθ, each 𝐆(n) ⪰ 0 (Theorem 2.2, ARGUED: relative
   prolate phase).
3. Q₁ written out: 𝒩^w = log N·𝐓₀ + Q₁(w) + o(1), with 𝐓₀ = Toeplitz[H∘sec] ⪰ I, and
   Q₁(w) = 𝐀₁ + 𝐄 − Σ_n (W(n)/n)𝐆(n), 𝐀₁ = Toeplitz[H(secθ)log(2/sin 2θ)] explicit, 𝐄 comb-free (edge, pole, incoherent
   archimedean). The incoherent comb part is O(N^{−1/2}log N) on the sector (ARGUED, from thm:ext-layer(iv)).
   Correction to K3_GAMMA_001: the leading form is log N·𝐓₀, not log 2N·‖b‖²; 𝐓₀ ⪰ I, so K3's leading term is a valid lower
   bound but not the leading term (PROVED in the coherent form).
4. Decision: Q₁ is monotone (nonincreasing) in w: w ≤ w′ coefficientwise ⟹ Q₁(w) − Q₁(w′) = Σ_n ((W′−W)(n)/n)𝐆(n) ⪰ 0.
   PROVED for the coherent part; CONDITIONAL, for Q₁ itself, on the ARGUED smallness of the incoherent part. Moreover the
   w-dependence of Q₁ is a bounded linear functional of the weights (absolutely convergent against W(n)/n²). The exterior
   route on the bulk prolate sector is **NO-GO** by the class of Lemma 1.6 of ROUND_001_B, enlarged: comb-monotone and
   bounded-linear; it fails the falsifier test for cΛ (c < 1), a_P, downward finite modifications, and is insensitive to
   Beurling systems at orders log N and 1.
5. Task (3) does not arise: there is no Λ-specific non-monotone part at order 1. The first non-monotone piece on the sector is
   the (1,n) resonance vector at order N^{−1/2}log N, linear in W(n) with oscillating signs, dominated by log N·𝐓₀ ⪰ log N·I;
   no inequality on it can decide a sign. No N ≤ 15 test is run on a non-existent object; the validations run are listed in §4.

Result: NO-GO with class (see the last section).

---------------------------------------------------------------------------------------------------------------------
## Corpus check

Searched: ROUTES-TRIED-INDEX/README.md (phase 199 proof-L-sharp lines 448–535, PROOF_L_SHARP_E_001, PROOF_L_SHARP_Y_001,
K3_GAMMA_001, META_200_BARRIER_001, phase 211 entries), the master grid (keywords Q₁, monotone, Toeplitz, harmonic cut),
K3_GAMMA_001, ROUND_001_B, Paper 46 §sec:ext.

- PROOF_L_SHARP_E_001 (Thm E.1/E.2) wrote 𝒲_ext as a pair sum over (m,n) with weights log m + log n and the harmonic cut; it
  closed "positivity class by class" (classes indefinite). This memo uses the same pair expansion for a general comb, but asks
  a different question (dependence on w, not positivity of a class) and isolates the coherent diagonal, which is not a ratio
  class statement: the diagonal class (1,1) of E.5 includes the archimedean part and is indefinite; the comb part of it alone
  is a positive multiplication operator. No conflict: E.5 is about the sum, Proposition 1.2 about the comb summand.
- PROOF_L_SHARP_Y_001 (Theorem B′, resonant pairs (1,n)) and thm:ext-multi: the (1,n) pairs are the only c^{−1/2} effects.
  Used here as input (ARGUED status kept), not retried.
- K3_GAMMA_001 declared Q₁ OPEN and named it "the real question"; META_200_BARRIER_001 lists "uniform bound of Q₁" as virgin.
  This memo computes the comb dependence of Q₁; it does not retry the Γ-limit (the expansion is written at fixed K and the
  renormalisation is the one of K3, used only as a coordinate system).
- ROUND_001_B Lemma 1.6 (single-cell comb monotonicity): the present Proposition 1.2 is its extension from single-cell data
  to all data (coherent part) and the identification of the only non-monotone remainder.
New reason, stated as required: the object (the comb dependence of the O(1) term on the bulk prolate sector) has not been
computed before; the method class is unchanged (exact pair expansion + oscillatory analysis), and the conclusion is a closure,
not a retry.

---------------------------------------------------------------------------------------------------------------------
## 1. The comb part of 𝔔^w for an arbitrary weight

### Lemma 1.1 (exact comb identity). PROVED.
Let w ≥ 0 on n ≥ 2 with Σ_n w(n)n^{−σ} < ∞ for σ > 1, and ϱ real on (1,∞) with ϱ ∈ C¹, ϱ = O(X^{−2}). Then the comb part of
𝔔^w[ϱ], namely 𝒫_w[ϱ] := Σ_{q≥2} 2w(q)q^{−1/2} ⟨Ψ̌_ϱ, Ψ̌_ϱ(· + log q)⟩, equals
  𝒫_w[ϱ] = Σ_{m,n≥1} (mn)^{−1/2} (W(m) + W(n)) ⟨u_m, u_n⟩,   W = w∗1,
all sums absolutely convergent, and 𝔔^w[ϱ] = 𝔄[ϱ] − 𝒫_w[ϱ] with 𝔄 (archimedean part plus pole term 2A B) independent of w.

*Proof.* Ψ̌_ϱ is supported in [0,∞), so in ⟨Ψ̌, Ψ̌(·+log q)⟩ only y > 0 matters, and there
Ψ̌(y + log q) = Σ_l l^{−1/2}u(y + log lq) = Σ_l l^{−1/2}u_{lq}(y) (the cut y + log q > 0 is implied by y > 0). Hence
⟨Ψ̌, Ψ̌(·+log q)⟩ = Σ_{m,l}(ml)^{−1/2}⟨u_m, u_{lq}⟩. Multiply by 2w(q)q^{−1/2} and put n = lq:
𝒫_w = 2Σ_{m,n}(mn)^{−1/2}⟨u_m,u_n⟩ Σ_{q|n, q≥2} w(q) = 2Σ_{m,n}(mn)^{−1/2}W(n)⟨u_m,u_n⟩; symmetrise in (m,n) (real data).
Convergence: u(x) = O(e^{−3x/2}), so |⟨u_m,u_n⟩| ≤ ‖u_m‖‖u_n‖ ≪ (mn)^{−1}·const, and W(n) ≪_ε n^{ε} under the hypothesis on w
for the weights considered (Λ, cΛ, a_P, finite modifications; for a general w the bound Σ W(n)n^{−3/2−δ} < ∞ suffices, which
follows from the Dirichlet-series hypothesis). The comb in 𝒲 is −Σ_q v_q c_Ψ(log q) and c_Ψ(log q) = ⟨Ψ(·+log q),Ψ⟩. ∎
For w = Λ this is the pair expansion of thm:ext-multi (weights log m + log n) and Thm E.1 of PROOF_L_SHARP_E_001.

### Proposition 1.2 (coherent/incoherent split). PROVED.
𝒫_w = 𝒟_w + 𝒪_w with
  𝒟_w[ϱ] = 2∫_1^∞ H₁^w(t)|ϱ(t)|² dt,   𝒪_w = Σ_{n≥2} W(n)ℬ_n,   ℬ_n[ϱ] = 2Σ_{m≥1, m≠n}(mn)^{−1/2}⟨u_m,u_n⟩.
(a) 𝒟_w ≥ 0, and for weights w ≤ w′ (coefficientwise) 𝒟_{w′} − 𝒟_w = 𝒟_{w′−w} ≥ 0 as forms.
(b) Each ℬ_n (n ≥ 2) is indefinite on C_c^1(1,∞).
(c) Consequently 𝔔^w is affine in W, the w-dependence of 𝔔^w is −𝒟_w − 𝒪_w, and every failure of monotonicity of 𝔔^w in w
on any set of data is a failure of 𝒪_w to be semidefinite on that set.

*Proof.* Diagonal m = n: Σ_m m^{−1}·2W(m)‖u_m‖² and ‖u_m‖² = ∫_{x>log m}|u|² = ∫_{t>m}|ϱ|²; so the diagonal is
2∫|ϱ(t)|² Σ_{m<t}W(m)/m dt = 𝒟_w (the value at integer t is irrelevant). (a) W = w∗1 ≥ 0 and is linear in w, so H₁^w ≥ 0 and
H₁^{w′} − H₁^w = H₁^{w′−w} ≥ 0. (b) Fix n ≥ 2, s₀ ∈ (1,2), ε small, α ∈ C_c^1(s₀,s₀+ε), β ∈ C_c^1(ns₀, n(s₀+ε)), ϱ = α + β.
Then u_m ≠ 0 on a set meeting the support of the pair only for: m = 1 (from α and β), m ≤ n (from β). The supports of
u_m and u_{m′}, in the variable s = e^y > 1, are supp ϱ/m and supp ϱ/m′; for m ≠ m′ these meet only if m′/m = n with
m = 1 (since supp α/m ⊂ (0,1) for m ≥ 2 and ε small). So ℬ_n[ϱ] = 2n^{−1/2}⟨u_1,u_n⟩ = 2∫_1^∞ α(s)β(ns)ds·(n^{−1/2}·n^{1/2})
up to the positive Jacobian, which changes sign under β ↦ −β. (c) Lemma 1.1 and (a). ∎

Reading. The coherent part is exactly the harmonic-cut count of ROUND_001_B Lemma 1.6, now valid for all data, not only single
cells: every dilate is paired with itself through Σ_{q|n}w(q) = W(n), and this is positive and monotone. The near-coincidences
m ≈ n, m ≠ n (clause (vi) of STATEMENT_001 §4) live only in 𝒪_w, with weight W(m)+W(n) — linear in w.

---------------------------------------------------------------------------------------------------------------------
## 2. The prolate sector

### 2.0 Data (as in K3_GAMMA_001 §1)
For k ≡ 0 mod 4, ψ_k is the prolate function of bandwidth c = 2πN on [−1,1], normalised in L²(ℝ), ϱ_k = ψ_k|_{(1,∞)},
d_k = 1 − χ_k, one-sided exterior mass ∫_1^∞ ϱ_k² = ½d_k. The sector is span{ϱ_4, …, ϱ_{4K}} (the coefficient of ψ_0 is enslaved
by f(0) = 0 and contributes √(d_0/d_4) → 0 to all exterior quantities; K3 §1.4). Coordinates b_j = a_{4j}(d_{4j}/d_4)^{1/2},
j = 1..K, and the renormalised form 𝒩^w(b) := 𝔔^w[Σ a_{4j}ϱ_{4j}]/(½d_4). Basis signs are fixed so that ψ_k(1) > 0 (a diagonal
±1 congruence; it changes neither semidefiniteness nor monotonicity). Matrices below are indexed by j, k ∈ {1..K} and "j − k"
means the difference of the indices j, k (the prolate orders differ by 4(j − k)).

### Theorem 2.1 (the coherent comb matrix is PSD and monotone, exactly). PROVED.
For every N, K and every w, the matrix
  𝐃^w_{jk} := 𝒟_w(ϱ_{4j}, ϱ_{4k})/(½√(d_{4j}d_{4k})) = 4∫_1^∞ H₁^w(t) ϱ_{4j}(t)ϱ_{4k}(t) dt / √(d_{4j}d_{4k})
satisfies 𝒟_w[Σa_{4j}ϱ_{4j}]/(½d_4) = bᵀ𝐃^w b, 𝐃^w ⪰ 0, and 𝐃^{w′} − 𝐃^w = 𝐃^{w′−w} ⪰ 0 for w ≤ w′.
*Proof.* Gram matrix of the functions ϱ_{4j}/√d_{4j} in L²((1,∞), 4H₁^w dt), with H₁^w ≥ 0; linearity in w. ∎
No asymptotics, no envelope, no WKB enters: the monotone part of the comb on the sector is monotone at every finite N.

### Theorem 2.2 (explicit limit of 𝐃^w). ARGUED (one input not proved; see the proof).
For fixed K and w with Σ_n W(n)n^{−2} < ∞, as N → ∞,
  𝐃^w_{jk} → 𝐃^w_{∞,jk} = (4/π)∫_0^{π/2} H₁^w(sec θ) cos(4(j−k)θ) dθ = Σ_{n≥2} (W(n)/n)·𝐆(n)_{jk},
  𝐆(n)_{jk} = (4/π)∫_{arcsec n}^{π/2} cos(4(j−k)θ) dθ = (4/π)arcsin(1/n) if j = k,  −sin(4(j−k)·arcsec n)/(π(j−k)) if j ≠ k.
Each 𝐆(n) is PSD (Gram matrix of e^{4ijθ} on (arcsec n, π/2)), and ‖𝐆(n)‖ ≤ (4/π)·K·arcsin(1/n) = O(K/n), so the series converges
absolutely against W(n)/n².
*Proof.* (i) Envelope (lem:ext-envelope, PROVED under (H_ν), which holds for fixed k once c ≥ c₀(k)): on t > 1 outside the Bessel
zone t − 1 ≲ c^{−2}, ψ_k(t) = (G_k e^{x_k(t)})^{1/2}P^{−1/4}cos φ_k(t), |x_k| ≤ σ(t) = O(c^{−1}(1 + (t²−1)^{−1/2})),
G_k = cC_k², C_k² = (2/π)d_k(1 + O(c^{−1}log c)), and P^{−1/2} = (t²−1)^{−1/2}(c²t² − ϑ_k)^{−1/2} = (1 + O(k/c))/(c·t√(t²−1)).
(ii) Relative phase (ARGUED). φ_k′ = Ω_k = ((c²t² − ϑ_k)/(t²−1))^{1/2} up to the adiabatic correction of lem:ext-envelope(a);
∂Ω/∂ϑ = −(1/(2c))(t√(t²−1))^{−1}(1 + O(ϑ/c²t²)), and all ψ_k start with the same phase at t = 1⁺ (thm:ext-layer(ii): the
regular solution J₀(√(2(c²−ϑ_k)(t−1))), whose phase does not depend on k to O(k/c)). With ϑ_j − ϑ_k = 2c(j′−k′)(1 + O(k/c))
for prolate orders j′, k′, φ_{j′} − φ_{k′} = −(j′−k′)·arcsec t + O(k²/c) uniformly on t > 1. This is consistent with the
large-t phases −k′π/2 of the radial functions and with the phase Ψ_n of thm:ext-layer(iv); the uniform O(k²/c) bound including
the adiabatic correction and the matching through the Bessel zone is not written out. (iii) Product: ψ_{j′}ψ_{k′} =
½C_{j′}C_{k′}(t²(t²−1))^{−1/2}[cos(φ_{j′}−φ_{k′}) + cos(φ_{j′}+φ_{k′})](1 + O(c^{−1}·…)); the sum-phase term oscillates at
frequency ≍ c t/√(t²−1) and, against H₁^w (piecewise constant, jumps W(J)/J at integers, H₁^w(t) ≪ Σ_{k≤t}W(k)/k) and the
weight (t√(t²−1))^{−1}, contributes O(c^{−1}Σ_J W(J)J^{−2}) by one integration by parts per cell (the oscillation-averaging step
of lem:ext-envelope(d)). (iv) With dt/(t√(t²−1)) = dθ, θ = arcsec t, and j′ − k′ = 4(j − k):
4∫H₁^w ψψ dt/√(dd) → 4·½·(2/π)∫_0^{π/2}H₁^w(secθ)cos(4(j−k)θ)dθ. (v) Writing H₁^w(sec θ) = Σ_n (W(n)/n)1_{sec θ ≥ n} gives the
𝐆(n) form. The Bessel zone t − 1 ≲ c^{−2} contributes nothing to 𝐃^w since H₁^w = 0 on (1,2). ∎
The only unproved input is (ii); everything else is lem:ext-envelope plus calculus.

### Proposition 2.3 (the incoherent comb part on the sector). ARGUED.
On the sector, 𝒪_w(ϱ_{4j}, ϱ_{4k})/(½√(d d)) = R^w_{jk}(N) with
  R^w_{jk}(N) = Σ_{n≥2} W(n)·(4/π)N^{−1/2} 𝓌_n cos(Ψ_n^{(j,k)} − π/4)·(1 + o(1)) + O_K(N^{−1}Σ_n W(n)n^{−3/2}),
𝓌_n = n/((n²+1)√(n²−1)), Ψ_n^{(j,k)} = −c(n²−1)/n + (phases of thm:ext-layer(iv) for the orders 4j, 4k).
*Reason.* ℬ_n restricted to the sector contains the pairs (m,n), m ≠ n. For 2 ≤ m < n the relative phase has no stationary
point (lem:ext-phase(ii)), one integration by parts gives O(c^{−1}) per pair, weighted by (mn)^{−1/2}·(envelope mass at
t ≥ 2) ≪ (mn)^{−1}; for (1,n) there is exactly one stationary point (lem:ext-phase(iii)) and the leading term is thm:ext-layer(iv)
with the comb share W(n) of the pair weight (W(1) = 0). The stationary-phase remainder is not controlled (thm:ext-layer(iv) is
open), and thm:ext-multi, which does control it, requires amplitudes vanishing at integers and a fixed cut X; prolate tails
satisfy neither. Hence ARGUED. Note the comb share of a (1,n) resonance is W(n) alone, so for w = cΛ the weight
log N + (1−c)log n + log(1+n^{−2}) of the paragraph after thm:ext-layer is recovered.

### 2.4 Q₁ written out
Collect the archimedean coherent part by the same steps (the archimedean diagonal on dilate m is m^{−1}⟨m(D)u_m,u_m⟩, and
lem:ext-osc replaces m(D) by log(τ(t)/2π), τ = ct²/√(t²−1); summing over m gives H(t)log(τ/2π); thm:ext-multi "Diagonal").
With the weight 𝔴^w_N(t) = H(t)log(Nt²/√(t²−1)) − 2H₁^w(t) and t²/√(t²−1) = 2/sin 2θ:

  𝒩^w(b) = log N·bᵀ𝐓₀b + bᵀQ₁(w)b + o(1)‖b‖²,
  𝐓₀,jk = (2/π)∫_0^{π/2} H(secθ)cos(4(j−k)θ)dθ,
  Q₁(w) = 𝐀₁ + 𝐄 − 𝐃^w_∞,
  𝐀₁,jk = (2/π)∫_0^{π/2} H(secθ) log(2/sin 2θ) cos(4(j−k)θ)dθ,
  𝐃^w_∞ = Σ_{n≥2}(W(n)/n)𝐆(n)   (Theorem 2.2),
  𝐄 = comb-free remainder: the Lévy edge terms of the dilate cuts at y = 0 (Proposition 2.2 of ROUND_001_B), the pole term
      2A B, the incoherent archimedean pairs, and the correction coming from the admissibility constraints f(λ) = 0, C² (prolate
      combinations are not admissible; K3's "boundary channel (E)").
Status: the coherent pieces 𝐓₀, 𝐀₁, 𝐃^w_∞ are ARGUED with the single gap of Theorem 2.2(ii) (for the archimedean part also the
operator form of lem:ext-osc on truncated dilates with jumps, which thm:ext-multi has only for amplitudes vanishing at integers).
𝐄 is not computed here; it does not depend on w (Lemma 1.1), which is all the decision below needs. The incoherent comb part is
o(1) by Proposition 2.3 (ARGUED).

Facts on 𝐓₀ (PROVED in this coherent form): since H ≥ 1 and (2/π)∫_0^{π/2}cos(4dθ)dθ = δ_{d0},
𝐓₀ − I = Toeplitz[(2/π)(H∘sec − 1)] ⪰ 0, i.e. 𝐓₀ ⪰ I. The diagonal is 1 + (2/π)Σ_{J≥2}(H_J − 1)(arcsec(J+1) − arcsec J) =
1.4182 (NUMERICAL), not 1: the cells t ≥ 2 contribute at order log N, with off-diagonal entries 0.2877, 0.1111, … .
**Correction to K3_GAMMA_001 §2.3–2.4:** "𝒩_μ = L(μ)Q₀ + Q₁ with Q₀ = ‖b‖²" holds for the layer only; the full leading form is
log N·𝐓₀, not diagonal, with 𝐓₀ ⪰ I. K3's Γ-limit statement survives as the lower bound 𝐓₀ ⪰ I; its comb-genericity is
unaffected (𝐓₀ contains no comb). The Mori-test comparison of K3 §4.3 used the layer only and is not changed by this.

---------------------------------------------------------------------------------------------------------------------
## 3. Decision on monotonicity, and the falsifier test

### Theorem 3.1 (Q₁ is nonincreasing in the comb). PROVED for the coherent part; CONDITIONAL for Q₁.
(a) PROVED. For w ≤ w′, at every N: 𝔔^{w}[ϱ] − 𝔔^{w′}[ϱ] = 𝒟_{w′−w}[ϱ] + 𝒪_{w′−w}[ϱ], with 𝒟_{w′−w} ⪰ 0 on all data
(Proposition 1.2) and, on the sector, 𝐃^{w′−w} ⪰ 0 (Theorem 2.1).
(b) CONDITIONAL on Proposition 2.3 (and on Theorem 2.2 for the explicit form): Q₁(w) − Q₁(w′) = Σ_n ((W′−W)(n)/n)𝐆(n) ⪰ 0.
So Q₁ is monotone, and the answer to question (2) is: yes, nonincreasing in w; the only part of the comb that is not monotone
is 𝒪_w, which on the sector is of order N^{−1/2}log N.
(c) PROVED (given the form of (b)). The comb enters Q₁ through K numbers e_d(w) = Σ_n (W(n)/n)·κ_d(n), d = 0..K−1,
κ_0(n) = (4/π)arcsin(1/n), κ_d(n) = −sin(4d·arcsec n)/(πd); |κ_d(n)| ≤ (4/π)·... ≪ 1/n uniformly in d ≤ K (|sin(4d(π/2 − α))| =
|sin 4dα| ≤ 4d·α, α = arcsin(1/n) ≤ π/(2n)), so each e_d is a bounded linear functional of the weights, absolutely
convergent against W(n)/n².

### 3.2 Falsifier test of any sign statement on the sector at orders log N and 1
(a) cΛ, 0 < c < 1: W = c log ≤ log, so Q₁(cΛ) ⪰ Q₁(Λ); every positivity statement for Λ on the sector holds verbatim for cΛ.
    For c > 1 the order of the sector form is still log N·𝐓₀ ⪰ log N·I against a comb term c·𝐃^Λ_∞ of order 1; the sector form is
    positive for N ≥ N₀(c,K) as well. So on the sector nothing separates c > 1 from c = 1 either, at fixed K.
(b) a_P (primes p < P deleted): W_{a_P} ≤ log, so Q₁(a_P) ⪰ Q₁(Λ). SURVIVES.
(c) Beurling systems with zeta continued to the line: Q₁ depends on the system only through e_d(w) = Σ W(n)κ_d(n)/n, bounded
    linear functionals; the sector form is log N·𝐓₀ + O(1) for every such system. SURVIVES (no Λ-specific input at these orders).
(d) Finite modifications: downward ones give Q₁ ⪰ Q₁(Λ) (SURVIVES); upward ones change Q₁ by a bounded PSD matrix, dominated by
    log N·𝐓₀ (SURVIVES for N large).
Every falsifier passes, so no sign argument located on the bulk prolate sector at orders log N and 1 is a sign step for (★).
**NO-GO, class: the comb dependence of the exterior form on the bulk prolate sector is −Σ_n (W(n)/n)𝐆(n) with 𝐆(n) ⪰ 0
(comb-monotone, bounded linear in the weights), plus an incoherent remainder of order N^{−1/2}log N.** This is the class of
ROUND_001_B Lemma 1.6 (comb monotonicity), extended from single cells to the whole coherent part, together with the class
"bounded functionals of the weights" of STATEMENT_001 §4(iv).

### 3.3 What this says about Proposition 2.4 of ROUND_001_B
Proposition 2.4 (CONDITIONAL on (ext-L)) placed the decision at the minimiser on a fixed sector span{ψ_0,…,ψ_K}. On that sector
the form is log N·𝐓₀ + Q₁ + o(1) with 𝐓₀ ⪰ I and Q₁ comb-monotone. Hence, for fixed K and N large, the sector form is positive
for every comb in the falsifier list, and the positivity of Λ's form near its minimiser carries no Λ-specific information at
orders log N and 1. All Λ-specificity of the exterior route therefore sits in the localisation step itself — (ext-L), the
statement that near-minimisers lie in the sector — which fails for cΛ (c > 1) and is the open problem prob:ext-L. The route
"localise, then sign on the sector" is circular: the sign step is comb-generic, and the localisation step is the whole problem.
(Recorded numerics are consistent: K3 §4.3 finds W/d₄ = 4.08 at N = 15 against a layer prediction 8.70, i.e. a large negative
O(1) share; by Lemma 1.1 the comb part of that share is −𝐃^Λ − 𝒪_Λ, and the remainder belongs to the comb-free 𝐄.)

### 3.4 The window reading (Proposition 1.3 of ROUND_001_B), for completeness
If instead of 𝔔^w one varies the comb in the window form at the same g = Ef, then
W^w_T(g) = W_T(g) + 𝒫_{Λ−w}[g] (comb pairing of the window function). On the sector W_T(g) = O(d₄) while 𝒫_{Λ−w}[g] = Σ_n
2(Λ−w)(n)n^{−1/2}c_g(log n) is of order ‖g‖² unless it vanishes, so the renormalised expansion does not exist for w ≠ Λ and there is
no Q₁(w). The w-dependence there is linear with coefficient the translation pairing c_g(log n), indefinite in sign; it is the
content of thm:geo-tv (comb-robust premises give at most δ ≤ λ^W) and of ROUND_001_B Proposition 1.4. ARGUED (the non-vanishing
of 𝒫_Λ[g] on the sector is not checked); nothing new.

---------------------------------------------------------------------------------------------------------------------
## 4. Validation (NUMERICAL; proves nothing)

Scripts: tools/ROUND_002_B_toeplitz.py (exact cell sums, cut J ≤ 2·10⁵), tools/ROUND_002_B_coherence.py (prolate radial functions).

(i) e_d(w) = (𝐃^w_∞)_{d}, d = 0..4, and eigenvalues of the 4×4 Toeplitz matrix 𝐃^w_∞ (sector ψ_4, ψ_8, ψ_12, ψ_16):

| comb w | e_0 | e_1 | e_2 | e_3 | e_4 | eigenvalues |
|---|---|---|---|---|---|---|
| Λ | 1.2092 | 0.9889 | 0.6505 | 0.5118 | 0.4282 | 0.0448, 0.3029, 0.8729, 3.6163 |
| ½Λ | 0.6046 | 0.4945 | 0.3252 | 0.2559 | 0.2141 | 0.0224, 0.1515, 0.4364, 1.8081 |
| a_3 (p = 2 deleted) | 0.7135 | 0.6511 | 0.5119 | 0.3890 | 0.3278 | 0.0023, 0.0632, 0.3846, 2.4038 |
| a_7 (p ≤ 5 deleted) | 0.2816 | 0.2774 | 0.2654 | 0.2473 | 0.2255 | 0.0000, 0.0009, 0.0385, 1.0869 |
| (3/2)Λ | 1.8138 | 1.4834 | 0.9757 | 0.7677 | 0.6423 | 0.0672, 0.4544, 1.3093, 5.4244 |
| 𝐓₀ (comb-free) | 1.4182 | 0.2877 | 0.1111 | 0.0814 | 0.0702 | 1.0292, 1.1908, 1.4382, 2.0148 |
| 𝐀₁ (comb-free) | 2.3964 | 1.3464 | 0.8323 | 0.6223 | 0.5059 | 0.7833, 1.1721, 2.0407, 5.5893 |

All 𝐃^w_∞ are PSD and ordered as Theorem 3.1 predicts. The coherent part 𝐀₁ − c𝐃^Λ_∞ of Q₁ (without 𝐄) is positive definite
for c = 1 (eigenvalues 0.738, 0.868, 1.168, 1.974) and c = 1.5 (min 0.161), indefinite from c ≈ 2 (min −1.644 at c = 2): the
coherent O(1) term sees large upward perturbations only, and even then it is dominated by log N·𝐓₀ for N large.
(ii) Check of Theorem 2.2 against scipy radial prolate functions (normalised to unit amplitude 1/(ct) at infinity), c = 60,
cut X = 40: diagonal (0,0), (4,4), (8,8): 0.665, 0.695, 0.694 against the predicted 0.665; off-diagonal (4,8): 0.511 against
0.492; (0,4): 0.609 against 0.492; (4,12): 0.006 against 0.227. At c = 80 the deviations are 2–20 %. The agreement is good
for low orders and degrades as k²/c grows, as the O(k²/c) phase error of Theorem 2.2(ii) predicts; the scipy routines fail
(NaN or segmentation fault) for c ≥ 100 or t ≳ 50, so no convergence study was possible. Theorem 2.1 (PSD, monotone) does not
depend on this check.
(iii) Task (3): not run. There is no Λ-specific non-monotone part at order 1 (Theorem 3.1); the first non-monotone piece is
O(N^{−1/2}log N) and is dominated by log N·𝐓₀ ⪰ log N·I, so no finite inequality on it could decide the sign of the sector form.

---------------------------------------------------------------------------------------------------------------------
## Result

**NO-GO with class.** Q₁ on the bulk prolate sector is nonincreasing in the comb: its comb part is −Σ_n (W(n)/n)𝐆(n),
W = w∗1, with explicit PSD Toeplitz matrices 𝐆(n); it is comb-monotone and a bounded linear functional of the weights, so
every sign statement on the sector at orders log N and 1 survives cΛ (c < 1), a_P, Beurling systems and finite modifications.
Class: comb-monotone / bounded-linear dependence (ROUND_001_B Lemma 1.6 class, extended from single cells to the full coherent
part of the exterior form). The Λ-specificity of the exterior route is entirely in the localisation (ext-L); the sector step
carries none.

## What was proved
- Lemma 1.1: exact comb identity 𝒫_w = Σ(mn)^{−1/2}(W(m)+W(n))⟨u_m,u_n⟩ for any comb w. PROVED.
- Proposition 1.2: 𝒫_w = 𝒟_w + 𝒪_w, 𝒟_w = 2∫H₁^w|ϱ|² ⪰ 0 monotone in w on all data; ℬ_n indefinite; 𝔔^w affine in w = w∗1,
  so no products of weights, no w∗w, no non-linearity in w exist in any expansion. PROVED.
- Theorem 2.1: the coherent comb matrix on the prolate sector is PSD and monotone at every N, K. PROVED.
- Theorem 2.2: explicit limit Σ_n (W(n)/n)𝐆(n), 𝐆(n) PSD Toeplitz. ARGUED (relative prolate phase, one gap).
- Proposition 2.3: incoherent comb part O(N^{−1/2}log N) on the sector. ARGUED.
- §2.4: Q₁(w) = 𝐀₁ + 𝐄 − 𝐃^w_∞ with 𝐀₁ explicit, 𝐄 comb-free; leading form log N·𝐓₀ with 𝐓₀ ⪰ I (correction to K3:
  not ‖b‖²). ARGUED for the expansion, PROVED for 𝐓₀ ⪰ I in the coherent form.
- Theorem 3.1: monotonicity of Q₁ in w. PROVED for the coherent part; CONDITIONAL (on Proposition 2.3) for Q₁.
- §4: NUMERICAL tables (validation only).

## What failed and why
- The hope that Q₁ carries a Λ-specific, non-monotone O(1) term: the comb part of the exterior form is linear in W = w∗1, and
  its diagonal (coherent) part is a nonnegative multiplication operator 2H₁^w. On data oscillating at the prolate frequency
  c = 2πN, all off-diagonal (incoherent) pairs, including every near-coincidence m ≈ n, are suppressed by the phase to
  O(N^{−1/2}log N) (resonances (1,n)) or O(N^{−1}). So the only comb content of Q₁ is monotone.
- The sector cannot detect c > 1 either at fixed K: the comb term is O(1) against log N·𝐓₀ ⪰ log N·I.
- K3's leading term Q₀ = ‖b‖² is the layer part only; the cells contribute at order log N (comb-free), 𝐓₀ ⪰ I.

## Next concrete step
The only non-monotone comb content of the exterior form is 𝒪_w = Σ_n W(n)ℬ_n, which is of order 1 only on data whose dilates
overlap without a large relative phase: low Mellin frequency (frequency ≲ log of the cell index), i.e. outside the prolate
sector — the regime of the deep quasimode (prop:ext-deep) and of the plunge j ≈ μ (K3 §3.2). The next object is therefore the
restriction of 𝒪_Λ to the gauge-quotient of PW_N at bounded Mellin frequency: write ℬ_n there as a finite matrix on a basis
of low-frequency admissible tails (Legendre block of META_200 question P2), and decide whether Σ_n log n·ℬ_n has a sign
pattern that fails for W = c log and for W_{a_P}. If 𝒪_w is again a bounded linear functional with indefinite but
comb-generic coefficients there, the exterior form is closed as a sign carrier on every regime (prolate sector by this memo,
single cells by ROUND_001_B, low frequency by that step).
