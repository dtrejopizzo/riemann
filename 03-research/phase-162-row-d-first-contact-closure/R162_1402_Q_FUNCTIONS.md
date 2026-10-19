# R162_1402 — The Q-functions Q_m(z;T) as T varies — **PARTIAL (laws PROVED) + NO-GO (PROVED)**

Note. Pure mathematics, plus one uncertified float computation used as guidance only (§7).
Inputs: README (F1–F4), R162_590, R162_1301 (Thm 3), R162_1201 (Thm 1.2, Thm 3.1, Prop 4.2, Thm 4.1), R162_802 (Thm 2.1,
§3), R162_402 (Thm 1.3), R162_303, R162_001 / Paper 47 lem:contA, lem:monoT.

**Labels.**
- Thm 1 (variational form. The functional x_m is fixed in T, and Q_m(0;T) is nondecreasing and left-continuous at T_*.
  So Gate 1 ⟺ sup_{T<T_*} Q_m(0;T) < ∞ on a harmonic-divergent S) PROVED. **New form** of R162_1301 Thm 3.
- Thm 2 (exact collar law for Q_m with an explicit residual: e^{a_m t} + exterior Gamma field + comb spill) PROVED.
  This is R162_802 Thm 2.1 specialised, **new** in its residual formula.
- Thm 3 (bottom dichotomy and square-root law: Q_m(0;T) ≍ |x_m(ψ_T)|²/λ(T); Gate 1 ⟺ x_m(ψ_T) = O(λ(T)^{1/2})) PROVED.
  The upper half is conditional on a spectral gap λ₂(T_*) > 0, i.e. on N being simple.
- Thm 4 (cross-m identity: pole residue matrix = rank-dim N Gram matrix of Gamma data; Cauchy/Stieltjes kernel form;
  Gate 1 ⟺ bounded Q for exterior evaluations at log n along any infinite set of n) PROVED. Restatement (E1).
- Thm 5 (Markov–Kreĭn NO-GO: no bound on Q_m(0;T) from finitely many spectral moments that avoids λ(T)) PROVED.
- Thm 6 (NO-GO: reflection rescales Q_m by a nonzero constant. Every law in Thms 1–5 transports to DH, deletion and Beurling.)
  PROVED.
Gate 1 OPEN. No label moves.

## 0. Corpus check

I grepped "Q-function", "q_m(0", "Douglas", "monoton", "collar" in phases 160–162 and Paper 47.
- Q-function / Douglas form: this appears only in R162_1301 Thm 3 and R162_1401 (at fixed T_*).
- The T-evolution of a resolvent quantity f_par(0;T) = ⟨A_T^{-1}φ,φ⟩ is R162_802, with φ the Tate vector.
- Kreĭn/de Branges T-flows are in phase 64 and thm:KEP3 (E1).
- Not found: the T-flow of the Gamma-lattice Q-functions, the square-root law, the Markov–Kreĭn obstruction.

## 1. Setup, and why the Gamma functionals are better than φ

Notation:
- I_T = (−T,T), and P_T is the primitive space, cut out by T-independent linear conditions (vanishing Tate moments).
- h_T is the form on P_T. H_T is the operator, with H_T > 0 for T < T_*.
- x_m(G) = ∫G e^{a_m u}du, with a_m = 2m+½.
- e_m^T = Π_T e^{a_m t}1_{I_T}, so that ⟨G,e_m^T⟩ = x_m(G) for G ∈ P_T.
- Q_m(z;T) = ⟨(H_T−z)^{−1}e_m^T,e_m^T⟩, and dμ_{m,T} is its spectral measure.

Two facts make the T-flow clean:
- (i) x_m is **one fixed linear functional** on ∪_T L²(I_T). Unlike e_m^T, it does not move with T.
- (ii) Extension by zero maps P_T into P_{T'} with h_{T'}(G̃) = h_T(G). This is lem:monoT: new contacts satisfy log n ≥ 2T.

## 2. Thm 1 (variational monotonicity and left-continuity) — PROVED

For T < T_*:

  Q_m(0;T) = sup_{0≠G∈P_T} |x_m(G)|²/h_T(G) = 1/c_m(T),   c_m(T) := inf{h_T(G) : G ∈ P_T, x_m(G)=1}.       (2.1)

(a) T ↦ Q_m(0;T) is nondecreasing on (0,T_*), and c_m is nonincreasing.

(b) lim_{T↑T_*} Q_m(0;T) = q_m(0−;T_*) := lim_{ε↓0}⟨(H_{T_*}+ε)^{−1}e_m,e_m⟩ ∈ (0,∞]. This quantity is infinite iff x_m ≢ 0
on N = ker H_{T_*}.

(c) Consequently, for S with Σ_S 1/m = ∞: Gate 1 at T_* ⟺ sup_{T<T_*} Q_m(0;T) < ∞ for all m ∈ S.

*Proof.*
- (2.1) is the Douglas/Cauchy–Schwarz extremal problem for a positive operator with bounded inverse. The supremum is
  attained at G = H_T^{−1}e_m.
- (a) follows from (ii): the supremum is taken over an increasing family of sets, of the same ratio.
- (b), "≤": by (ii) at T' = T_* we have Q_m(0;T) ≤ sup_{P_{T_*}} |x_m|²/(h_{T_*} + ε‖·‖²) = q_m(−ε;T_*) for every ε, and
  this is ≤ q_m(0−;T_*).
- (b), "≥": G ∈ P_{T_*} in the form domain can be approximated in the form norm by elements of ∪_{T<T_*}P_T. First take
  the truncation 1_{I_{T_*−η}}G. It converges in H^s for s < ½, hence in the log-order form norm, which is dominated by
  H^s. Then restore the two Tate moments by adding a fixed pair of C_c^∞(I_{T_0}) functions with small coefficients.
  Both h_{T_*} and x_m are continuous in that norm. Hence the supremum over the union equals q_m(0−;T_*), with the
  sup-ratio taken against h_{T_*}. That is the Douglas constant, which is infinite iff e_m ∉ ran H^{1/2}, i.e. iff
  ⟨e_m,N⟩ ≠ 0 (compact resolvent, R162_1301 Thm 3).
- (c) is (b) combined with Müntz–Szász (R162_1201 Thm 4.1). ∎

So the pole at z = 0 is born **monotonically**. It is the limit of an increasing family of finite positive numbers.
Gate 1 is exactly "this family is bounded". Monotonicity is weight-blind (§6).

## 3. Thm 2 (exact collar/Hadamard law with explicit residual) — PROVED

Let T < T' < T_* and u = H_T^{−1}e_m^T ∈ P_T, the extremal function up to scale. Define r ∈ (form domain of h_{T'})* by
r(G) = h_{T'}(ũ,G) − x_m(G). Then:

 (i) r vanishes on P_T, and r(ũ) = 0.

 (ii) Q_m(0;T') − Q_m(0;T) = ⟨H_{T'}^{−1}r,r⟩ ≥ 0.

 (iii) On test functions G supported in the collar C = I_{T'}∖I_T, whose Tate moments are zero:

   r(G) = −∫_C G(t)[ e^{a_m t} + Σ_{k≥1} x_k(u) e^{−a_k|t|}ε_k(t) + (C_{N_{T'}}u)(t) ] dt,

  where ε_k(t) = 1 for t > T and ε_k(t) = ε_par for t < −T, and C_N u = Σ_{n∈N_{T'}} w_n(u(·−log n)+u(·+log n)).
  On general G, r adds the Tate-direction correction.

*Proof.*
- (i) and (ii) are R162_802 Thm 2.1 verbatim, with φ replaced by the functional x_m. The proof uses only (ii) of §1 and
  the fact that x_m is T-independent.
- (iii): for G supported in C, h_{T'}(ũ,G) = ⟨A ũ,G⟩ with u supported in I_T. On C, A ũ = −(𝒦u) − C u by R162_1201 Thm 1.2,
  using the exterior Gamma field. The k = 0 term vanishes by primitivity of u. ∎

Reading:
- The flux of Q_m is the H_{T'}^{−1}-energy of the collar residual.
- The residual has three parts: the probe e^{a_m t} itself (growing like e^{a_m T'}); the exterior Gamma field of the
  extremal u, whose coefficients x_k(u) = Q_{mk}(0;T) are the Gram row (§5); and the comb spill of u into the collar.
- The infinitesimal version dQ_m/dT = lim ⟨H^{−1}r,r⟩/δ needs the edge regularity (REG) of R162_407. It is not proved;
  the finite-δ law needs none.

## 4. Thm 3 (bottom dichotomy, square-root law) — PROVED (upper half conditional on a gap)

Let λ(T) = min σ(H_T), let ψ_T be a normalised bottom eigenvector, and let λ₂(T) be the next eigenvalue.

 (a) Q_m(0;T) ≥ |x_m(ψ_T)|²/λ(T) for all T < T_*.

 (b) If λ₂(T) ≥ γ > 0 on (T_*−η,T_*) (a simple kernel with a gap, persistent by continuity of the spectrum in T), then
     Q_m(0;T) ≤ |x_m(ψ_T)|²/λ(T) + ‖e_m^T‖²/γ.

 (c) Hence, if N is simple with a gap: Gate 1 ⟺ for m ∈ S, |x_m(ψ_T)|² = O(λ(T)) as T ↑ T_*.
     By lem:contA, λ(T) → 0. So x_m of the ground state must vanish at least at the square-root rate of the bottom.

 (d) If x_m(F) ≠ 0 for F ∈ N, then λ(T)Q_m(0;T) → Σ_j|x_m(F_j)|² > 0.

*Proof.*
- (a) and (b) come from the spectral sum Q_m = Σ_j |⟨e_m,φ_j⟩|²/λ_j, with ⟨e_m,ψ⟩ = x_m(ψ).
- (c) combines (a), (b) and Thm 1(b).
- (d): the ground eigenprojections converge in norm to the projection onto N, by the gap and norm-resolvent continuity
  along the flow. That continuity follows from (ii) and the form monotonicity (lem:contA argument). ∎

Remark (F1). Note what (c) does and does not say.
- It is not "x_m(ψ_T) = 0". That would be false for λ > 0 eigenvectors, and is false here: see §7, where x_m(ψ_T) stays
  of order 1.
- It is a **rate** statement relating two infinitesimals at the bottom. This uses λ = 0 non-perturbatively: it is the
  first corpus form of Gate 1 that is a *rate comparison along the flow*.
- It is still E1.

## 5. Thm 4 (cross-m identities) — PROVED, restatement

(a) Q_{mn}(T) := ⟨H_T^{−1}e_m,e_n⟩ is a positive Gram matrix. It is nondecreasing in T in the Loewner order (Thm 1 applied
    to Σc_m x_m), and it has pole residue lim λ(T)Q_{mn}(T) = Σ_j x_m(F_j) conj x_n(F_j), of rank ≤ dim N.

(b) Generating kernel. Put k_q(u) = e^{u/2}qe^{2u}/(1−qe^{2u}) for |q| < e^{−2T}. Then

      K_T(q,p) := Σ_{m,n≥1} Q_{mn}(T)q^m p̄^n = ⟨H_T^{−1}Πk_q, Πk_p⟩,

    the reproducing kernel of the Cauchy-transform space {g_G} of R162_1201 Prop 4.2, normed by h_T.

(c) Exterior-field form. For t > T, the Euler functional E_t(G) = (𝒦G)(t) = Σ_m x_m(G)e^{−a_m t} has
    Q_{E_t}(0;T) = e^{−t}K_T(e^{−2t},e^{−2t}). Moreover, for any infinite set 𝒩 of integers n > e^{T_*}:
    Gate 1 ⟺ sup_{T<T_*} Q_{E_{log n}}(0;T) < ∞ for all n ∈ 𝒩.
    By R162_1201 Thm 3.1, w_n E_{log n} = Σ_m Λ(n)n^{−2m−1}x_m. These are exactly the Euler-channel functionals.

*Proof.*
- (a): the proof of Thm 1 applies to any fixed functional, and Thm 4(d) gives the residue.
- (b): geometric series.
- (c): for F ∈ N, E_t(F) = e^{−t/2}g_F(e^{−2t}), and g_F is analytic on |q| < e^{−2T_*}. It vanishes at q_n = n^{−2}, which
  accumulate at the interior point 0, so g_F ≡ 0. Then F = 0 by Müntz. The converse is trivial. Each finiteness is the
  Douglas criterion of Thm 1 for E_{log n}. ∎

This is the only place the Λ-weights appear in a Q-function law: the Euler functionals are Λ(n)-weighted lattice
combinations. But (c) holds for every infinite 𝒩 with any weights, so Λ drops out (F3).

## 6. NO-GO results

**Thm 5 (Markov–Kreĭn).** Fix T < T_* and finitely many moments M_j = ∫λ^j dμ_{m,T}, for j = −K..K with j ≠ −1. (All are
explicit when j ≥ 0: M_0 = ‖e_m‖², M_1 = h_T(e_m) from the secular ledger R162_1401 Thm 2.) Then
sup{∫λ^{−1}dν : ν ≥ 0, supp ν ⊂ [λ(T),∞), same moments} is attained by a Markov–Kreĭn extremal measure with an atom at
λ(T). It tends to ∞ as λ(T) → 0 whenever the moments stay bounded, which they do: M_j(T) → M_j(T_*) < ∞.
So no bound on Q_m(0;T) uniform as T ↑ T_* can come from finitely many spectral moments. Every such bound goes through
λ(T), and hence through the square-root law of Thm 3(c) (circular).

*Proof.* This is the Chebyshev–Markov–Stieltjes extremal problem (Kreĭn–Nudel'man, *The Markov Moment Problem*, Ch. III,
CITED). The function 1/λ is strictly convex, and its maximum over the moment body is attained at principal
representations with an atom at the left endpoint. As the endpoint → 0 with bounded moments, ∫λ^{−1} ≥ (atom
mass)/λ(T), and the atom mass stays bounded below for the upper principal representation. ∎

**Thm 6 (transport).**
- (a) Reflection. By R162_402 Thm 1.3(e), G_+^0(−a_m) = −εζ'(−2m)K_F(a_m) and x_m = ερ_m b_m G_+^0(−a_m). So the
  Q-function of the port functional G ↦ G_+^0(−a_m) is |ρ_m b_m|^{−2}Q_m. It is a nonzero constant rescaling in each m,
  and it cannot change finiteness.
  - ζ'(−2m) (equivalently ζ(2m+1), through the functional equation plus the Euler product) enters only through this
    constant.
  - An identity across m would need a relation among the Q_m (nonlinear in the Gram matrix) with Λ-specific
    coefficients. The only coefficients available are the Euler weights of Thm 4(c), and there the conclusion is
    independent of the weights.
- (b) Thms 1–5 use only these inputs: lem:monoT extension compatibility, positivity below T_*, the Gamma exterior field,
  Müntz, and spectral theory.
  - All of them hold verbatim for deletion a = Λ1_{n≥5} and κ-models (same M, comb ≥ 0), and for Beurling (same M).
  - For DH, the lattice becomes 2m+3/2 and κ_DH = e^{−|u|}κ. This is the same structure.
  - DH and the deletion model have first contacts with x_m ≠ 0 (R162_102, R162_702). There Q_m(0;T) ↑ ∞ at the
    rate of Thm 3(d).
  - So no law derived here forces boundedness. **F3 failed** for every law.
- (c) F1: passed as statements, since Thms 1(c), 3(c) and 4(c) are bottom-only. F2: all laws are quadratic in h, and no
  orientation is added. F4: everything is exact at finite T, with no graph limit.

Lines checked first, as instructed:
- DH: transported, (b).
- Deletion: transported, (b). Also note that the deletion odd-sector overshoot at 0.4608 (R162_802 §5) is a first
  contact of the *complete* form, where the monotone flow of Q_m diverges identically.
- Beurling: same M and positive comb, so the flow laws are identical.

## 7. Numerics — UNCERTIFIED float Galerkin, guidance only

Setup:
- Script: `scripts/c3/q1402_float_Q.py`.
- The exact symbol s_T is used, with a quadrature to τ = 3000 plus an asymptotic tail.
- Basis: Legendre, K = 34, split by parity, with the primitive constraint imposed.
- The Galerkin Q is a lower bound for the true Q (a supremum over a subspace) up to quadrature error.
- The Galerkin λ is an upper bound. It is **not converged** at ½log5: float λ_ev = 4.4e−7 against the certified value
  ≈ 2.5e−12 (R162_303).
- "gs" = share of the ground state in Q, that is |x_m(ψ)|²/(λQ).

| T | sector | λ (float) | Q_1 | Q_2 | Q_3 | gs (m=1) |
|---|---|---|---|---|---|---|
| 0.30 | ev | 7.1e−1 | 5.1e−3 | 6.7e−2 | 3.8e−1 | 0.87 |
| 0.50 | ev | 2.5e−2 | 1.5 | 2.4e1 | 1.9e2 | 0.99 |
| 0.65 | ev | 1.5e−2 | 5.6 | 1.3e2 | 1.7e3 | 0.002 |
| 0.70 | ev | 1.3e−3 | 9.6e1 | 2.7e3 | 4.2e4 | 0.93 |
| 0.78 | ev | 3.2e−6 | 6.5e4 | 1.8e6 | 2.9e7 | 0.999 |
| 0.8047 | ev | 4.4e−7 | 5.2e5 | 1.5e7 | 2.4e8 | 0.999 |
| 0.30 | odd | 1.0 | 5.6e−5 | 2.3e−3 | 2.6e−2 | 0.80 |
| 0.60 | odd | 1.6e−2 | 3.1e−1 | 1.7e1 | 3.0e2 | 0.99 |
| 0.70 | odd | 1.1e−2 | 3.9e−1 | 2.5e1 | 5.9e2 | 0.22 |
| 0.78 | odd | 1.4e−4 | 4.9e1 | 4.7e3 | 1.6e5 | 0.97 |
| 0.8047 | odd | 2.5e−5 | 3.7e2 | 3.5e4 | 1.2e6 | 0.99 |

Observations (guidance only):
- Q_m is monotone in T in every row, consistent with Thm 1.
- Past T ≈ 0.7, Q_m ≈ |x_m(ψ_T)|²/λ(T), and |x_m(ψ_T)|²/‖e_m‖² stays of order 0.2–1. So the ground state carries
  O(1) Gamma data while λ collapses doubly exponentially.
- At T = ½log5 the true Q is therefore ~ 10⁵ times larger than the table (true λ ≈ 2.5e−12).
- The dips in gs at 0.65 (even) and 0.70 (odd) are near-crossings where the bottom vector is briefly Gamma-orthogonal.
  This shows that x_m(ψ_T) ≈ 0 does occur for λ > 0 and is unstable (F1).
- **Guidance: nothing in the data suggests a bounded law.** If there is a contact with the present bottom branch, then
  Thm 3(d) is the observed regime, not (c).

## 8. Verdict and residual

**PARTIAL + NO-GO (PROVED).** Proved results:
- Q_m(0;T) is a monotone, left-continuous family that is finite for T < T_*. Its supremum is the Douglas constant at T_*
  (Thm 1).
- It obeys an exact collar law with an explicit residual (Thm 2).
- It is governed at the bottom by the square-root law |x_m(ψ_T)|² = O(λ(T)) ⟺ Gate 1 (Thm 3).
- Its cross-m structure is a Loewner-monotone Gram/reproducing kernel whose Euler-evaluation form is weight-blind
  (Thm 4).

What fails:
- Moment methods cannot bound Q_m without λ(T) (Thm 5).
- Reflection only rescales, and every law transports to DH, deletion and Beurling (Thm 6).

**Residual (sharp).** Prove the rate comparison |x_m(ψ_T)|² ≤ C_m λ(T) as T ↑ T_* for m in a harmonic-divergent S. The
proof must use an input that fails for DH and deletion: the Λ*1 = log / ×p cocycle acting on the collar residual of
Thm 2(iii), whose comb spill C_N u is the only Λ-dependent term. Candidate: compare the comb spill at the thresholds
½log n and ½log(nm) (O802.1), now with the Gamma probe e^{a_m t} in place of the Tate vector.

Add to R162_590 §1c: "T-flow of the Gamma Q-functions (monotone Douglas family, collar law, square-root law,
reproducing kernel, Markov–Kreĭn) — R162_1402 — weight-blind; rate form of Gate 1 | E1, F3".

Files edited: this file; new script `scripts/c3/q1402_float_Q.py`.
