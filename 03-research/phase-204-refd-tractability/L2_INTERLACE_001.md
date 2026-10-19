# L2_INTERLACE_001 — (L2) by interlacing / first crossing: T13.1 and T13.2 are NO-GO within already registered classes; the premise "k jumps at contacts" is false

Phase 204. Paper 47 notation (eq:Aform, 𝒫_T, λ_A, 𝒞F, v_n = Λ(n)/√n·(…)).
Writes only this file; the index lines are in §8 for the integrator to copy.

## 0. Corpus and index check (rule) and new reason, written out

**Index hits.**
- `06_OPEN_RESIDUES` l.≈181: **(L2)** = S_{T,k(T)} ⪰ 0 ∀T > ½log5, OPEN; dead routes already listed: norms, determinants,
  moments, local symbol (W-*), Lemma H (ARGUED), front T₁/(B_T), β₀ = 2, PNT cone, 4×4 Schur, **Schur tower n₋
  independent of k (L2_002, PROVED partial)**, **scalar transfer Φ(c_k, λ_min) (L2_003, NO-GO by 2×2 falsifier)**,
  Γ-moment annihilation (REF-D).
- `04_PHASES` l.67 **lem:flowdet** (log-det flow / Hellmann–Feynman: NO-GO, "coefficient dominated by h*(T)²/λ_A"); l.139
  Fold/Grönwall NO-GO; l.401 lem:monoT (REF-D); l.975 R170_888 Hellmann–Feynman.
- **BARRIER_W_001** (phase 197, `03-research/phase-197-barrier-theorem/BARRIER_W_001_NONCROSSING_INDEX_SIGNATURE_CODIMENSION_NO_GO.md`):
  class **𝒦_W** = index / spectral flow / Kreĭn signature / vNW codimension / **non-crossing by determinant vanishing**
  over the structural class 𝒮 (S1 extension by zero, S2 concavity, S3 continuity + invisibility of input U0 + modulus
  U2, S4 parity, S5 compact resolvent). Theorem W1: the index is monotone along T. Conclusion: the only Λ-specific
  crossing datum is the pairing Σ v_n c_{h*}(log n), a functional of the minimizer.
- **PROOF_L_SHARP_H_001** (`03-research/phase-199-frontier-pattern/proof-L-sharp/`): class **𝒦_H** = differential
  inequalities in T or c whose coefficients are evaluated at the minimizer; NO-GO as a class.
- **INV_U_001** (`03-research/phase-195-modern-tools/INV_U_001_CONTACT_CROSSING_EDGE_LAW_LOG_ONSET_C1_NO_GO.md`):
  boundary law at the contact: U0 (no jump in λ), U5b (no jump in λ′), non-analytic germ −v_n a_+a_−·2η/log(κ/2η); class
  𝒦_cross NO-GO (ARGUED).
- Phase 156 (memory; P47 thm:parityschur, prop:polarcap): In(W_T) = In(𝔞_T|𝒫_T) + In(𝔊_T), 𝔊_T = S^{Sch}_T + D_pol, 2×2.
- R186_025 / R186_104 / R186_105: definition of S_{T,k} and audit judgment "(L2) = W ≥ 0 rewritten in a basis of
  piecewise Tate exponentials; NO-GO as a proof route" (R186_104 row 6, MAJOR).
- grep "interlacing", "interlacing", "Cauchy", "rank-one edge", "rank-one": only TRACT_001 §6.1 (the proposal itself)
  and unrelated uses (Lemma H.2 band-edge rank-one rate in H_001; "rank-one Schur at log 2" phase 156a). There is no
  prior entry of Cauchy interlacing at a contact jump.

**New reason, written out (against BARRIER_W_001 and 𝒦_H).** BARRIER_W_001 works on the infinite-dimensional form
𝔞_T|𝒫_T; 𝒦_H on differential inequalities at the minimizer. TRACT_001 §6.1 proposes two pieces that, *if the
structural premise were true*, would not be in those classes: (i) a finite k×k matrix whose size changes exactly at
the contacts, with an algebraic jump (rank-one edge) to which Cauchy interlacing applies, a linear-algebra theorem
that is neither flow nor index; (ii) the possibility that the rank structure of dS/dT between contacts (not the value
of a functional of the minimizer) prevents the crossing. The stated difference: the object is finite and the theorem
used is combinatorial-algebraic (Cauchy), not flow-based. This memo first checks whether that structural premise is
true (§1). It is not, and that decides the rest.

## 1. Exact definition of S_{T,k} and of (L2) (from R186_024/025/104/105)

**Data.** I_T = (−T,T), split into k equal blocks B_1,…,B_k of half-length τ = T/k. Two subspaces of 𝒫_T = {F ∈
L²(I_T): A(F) = B(F) = 0} (global Tate ∫F e^{±x/2} = 0):
- 𝒱_k = ⊕_B {F_B ∈ L²(B): ∫_B F_B e^{±x/2} = 0} (Tate **per block**; ⊂ 𝒫_T; high-pass subspace, finite codimension);
- E_k = 𝒱_k^⊥ ∩ 𝒫_T = (span{e^{x/2}1_B, e^{−x/2}1_B : B}) ∩ 𝒫_T, **dim E_k = 2k − 2** (R186_104 row 1, PROVED).

With G the Gram matrix/operator of the form 𝔞_T in the decomposition 𝒫_T = 𝒱_k ⊕ E_k,
  **S_{T,k} := G_EE − G_E𝒱 G_𝒱𝒱^{−1} G_𝒱E**, real symmetric (2k−2)×(2k−2) matrix,
well defined when G_𝒱𝒱 = 𝔞_T|𝒱_k ≻ 0, which is exactly **(L1)**: c(T,k) := min 𝔞_T|𝒱_k ≥ log(k/T) − C_B(T/k) −
‖P|𝒱_k‖ > 0 (R186_025 Theorem B + Corollary, PROVED; R186_105 confirms it). It requires k ≳ 25 at ½log5 (with the
1.674 CITED bound of R186_104) and, with the correct constants, **k exponential in T** (R186_104 row 6:
k ≍ T·e^{π+𝒜_T/2} for the norm route; with Theorem B, k ≍ T·e^{C_B+𝒜_T}).

**Equivalence (PROVED, Haynsworth/Sylvester: additive inertia of the Schur complement).** If (L1) holds,
In(𝔞_T|𝒫_T) = In(G_𝒱𝒱) + In(S_{T,k}) = (∞,0,0) + In(S_{T,k}); so λ_A(T) > 0 ⟺ S_{T,k} ≻ 0 and λ_A(T) ≥ 0 ⟺ S_{T,k} ⪰ 0,
**for any admissible k** (n₋ independent of k: L2_002). **(L2)** is: for every T > ½log5 there exists k = k(T) with
(L1) and S_{T,k(T)} ⪰ 0. It is nothing finer than that: it is "S ⪰ 0 for every T" with whatever k is needed.

**Answer to question 1 (correction of TRACT_001's premise).**
- (a) **k is not the number of contacts.** k is a discretization parameter (number of blocks), chosen so that (L1)
  holds; it bears no relation to {n : log n ≤ 2T}. TRACT_001 §2 R13(d) ("k(T) jumps at new primes") and §6.1 T13.2
  ("S_{T_j,k+1} is obtained from S_{T_j,k} by an edge") confuse k with #𝒩_T. PROVED (by definition, R186_025 Notation).
- (b) **Dependence on T.** With k fixed, the blocks scale with T (τ = T/k); under the dilation U_T: L²(−1,1) → L²(I_T)
  the entries of S_{T,k} in a fixed basis of E are continuous in T (lem:contA applied to G, plus continuity of the
  inverse of G_𝒱𝒱 by (L1) uniform on compacts). PROVED. **They are NOT real-analytic in T** at the contacts: INV_U_001
  U2 gives a germ −v_n a_+a_− 2η/log(κ/2η) in λ_A, non-analytic at η = T − T_n (PROVED there). Between contacts they
  are real-analytic (analytic form in the dilation parameter, Kato type-(B) family with G_𝒱𝒱 ≻ 0). ARGUED (standard;
  the proof is not written out).
- (c) **The size and structure of S do not change at the contacts.** When n enters (2T_n = log n), the form changes
  (−v_n 𝒞F(log n) appears), not the basis. By U0/lem:monoT the new term is identically 0 at T = T_n:
  S_{T_n^+,k} = S_{T_n^−,k}. PROVED.
- (d) **When k changes (k → k+1) the partitions are not nested**: E_k ⊄ E_{k+1} in general (the blocks of length 2T/k
  and 2T/(k+1) do not refine each other), so there is no edge or Cauchy interlacing between S_{T,k} and S_{T,k+1}.
  There IS nesting k → 2k (E_k ⊂ E_{2k}), which is L2_002: S_{T,k} is the Schur complement of S_{T,2k} and n₋ is
  independent of k. Already on record.

**Consequence.** The object on which T13.2 would apply Cauchy (an edge at the contact) does not exist. What does exist
at the contact is a change in the *T-derivative* of the entries (§4).

## 2. Is R6 ≡ (L2)? No: they are the other two floors of the same Schur tower (PROVED)

prop:polarcap: 𝔊_T = S^{Sch}_T + D_pol, with S^{Sch}_T the compression of 𝔞_T to the 𝔞_T-complement of 𝒫_T in 𝒟_T (2×2,
modes h_ev, h_odd), and thm:parityschur: In(W_T) = In(𝔞_T|𝒫_T) + In(𝔊_T). Combining with §1:

  **Lemma T3 (three-floor inertia tower; PROVED given (L1) and the non-degeneracy of thm:parityschur(a)).**
  In(W_T|𝒟_T) = In(𝔞_T|𝒱_k) + In(S_{T,k}) + In(𝔊_T),  with dimensions ∞ / 2k−2 / 2.
  Proof: two applications of Haynsworth additivity, on 𝒟_T = 𝒫_T ⊕ (polar complement) and 𝒫_T = 𝒱_k ⊕ E_k. ∎

Thus, (L2) is the **primitive** floor (λ_A, sign of 𝔞_T on 𝒫_T) and R6 is the **polar** floor (passage from λ_A to
λ_W). They are not the same object in two coordinate systems; TRACT_001 §4's warning ("does S_{T,k} contain 𝔊_T as a
block?") is answered **no**: 𝔊_T lives outside 𝒫_T, S_{T,k} inside it. The only relation is that the rank condition of
thm:parityschur(b) for 𝔊_T uses λ_A > 0, i.e. R6 relies on (L2), not the reverse. The two phase-204 builders do not
duplicate the object; they do share the barrier class (§3), because both propose non-crossing by continuation in T.

## 3. T13.1 (non-vanishing of det S_{T,k} between contacts): it is 𝒦_W ∩ 𝒦_H — NO-GO within registered classes

Fix (T_j, T_{j+1}) with no contacts and k with (L1) throughout the interval. Then S(T) := S_{T,k} is real-analytic
(§1(b)) and det S(T) = 0 ⟺ an eigenvalue crosses 0.

**3.1 The variation law.** In dilation coordinates F = U_T φ, φ ∈ L²(−1,1):
  𝔞_T(U_Tφ) = (1/2π)∫ m(s/T)|φ̂(s)|² ds − Σ_{n∈𝒩_T} v_n 𝒞φ(log n / T)
(m the archimedean symbol of lem:K). Differentiating (between contacts, 𝒩_T fixed):
  d/dT 𝔞_T(U_Tφ) = −(1/2πT²)∫ s m′(s/T)|φ̂(s)|² ds + (1/T²)Σ_{n∈𝒩_T} v_n log n · (𝒞φ)′(log n / T).        (3.1)
The first term is negative-definite (m increasing in |s|, m′(s)s ≥ 0: lem:mbounds) and **of infinite rank**; the
second is a sum of bilinear forms ⟨φ, (S′_ℓ + S′_ℓ*)φ⟩ with ℓ = log n/T, each indefinite and of infinite rank
(derivative of a translation). dS/dT is the Schur compression of (3.1) plus the variation terms of G_𝒱𝒱^{−1}; **it has
no low-rank structure**. PROVED (formula (3.1) is differentiation under the integral, justified by lem:mbounds and a
finite sum).

**3.2 Hellmann–Feynman.** At a simple eigenvalue λ_min(T) with eigenvector g*(T) ∈ ℝ^{2k−2},
  dλ_min/dT = ⟨g*, S′(T) g*⟩ = d/dT 𝔞_T evaluated at h*_T := (Schur extension of g*) = minimizer of 𝔞_T|𝒫_T,   (3.2)
because the Schur complement restricted to the minimal eigenvector reproduces exactly the form at the minimizer
(variational Schur property; with λ_min of S ≠ λ_A in general, but at the crossing λ_min(S) = 0 ⟺ λ_A = 0 and the null
vector of S extends to the null vector of 𝔞_T|𝒫_T). PROVED at the crossing (the case that matters).
**Hence any argument using the sign or size of dλ_min/dT at a crossing is a functional of h*.** It is exactly
lem:flowdet ("coefficient dominated by h*(T)²/λ_A"), BARRIER_W_001 §5 (the only Λ-specific crossing datum is
Σ v_n c_{h*}(log n)) and 𝒦_H. The finiteness of the matrix changes nothing: (3.2) is computed in the finite basis but
its value is that of the infinite form at h*.

**3.3 The quantitative (Lipschitz) argument.** By lem:monoT λ_A is non-increasing; the continuation "λ_A(T₀) > 0 and
|dλ_A/dT| ≤ L ⇒ λ_A > 0 on [T₀, T₀ + λ_A(T₀)/L)" requires:
- an explicit L: between contacts, from (3.1), |d𝔞_T/dT| ≤ (C/T)(𝔞_T + M_0‖·‖²) (dilation + lem:mbounds) — O(1) relative;
- **there is no Lipschitz property at the contacts**: INV_U_001 U2 gives modulus η/log(1/η) in λ_A (PROVED), so no
  Lipschitz argument crosses a contact without losing a logarithmic constant.
With the certified margin at ½log15 (Mori, CITED; ≈ 1.5·10⁻⁷⁰ in λ_A per AUDIT_ZENODO_FRONTIER l.48,
NUMERICAL from the cited author) and L = O(1), the advance is ΔT ≲ 10⁻⁷⁰: **useless**, as the objective anticipates.
For it to help one would need |dλ_A/dT| ≲ 10⁻⁷⁰ in the direction of h*, which by (3.2) is a statement about h* — 𝒦_H.
Moreover the same L holds for every comb with v_n ≥ 0 of bounded support in 𝒩_T (the bound uses only Σ|v_n| and
lem:mbounds), and a_P, Epstein (2Λ_Q ≥ 0) do cross: CERT_FALSIFIERS #11 (Epstein, T = 1.59, value −0.05994, PROVED
intervals) and a_P (crossing at 0.60). By lem:transfer, no "Lipschitz + margin ⇒ non-crossing" deduction with
comb-uniform constants can work without a margin that distinguishes ζ, and that margin is what one wants to prove.

**3.4 Is there an algebraic feature forcing codimension ≥ 2?** BARRIER_W_001 Thm W3: a simple-eigenvalue crossing in a
one-parameter family of real symmetric matrices is codimension 1; vNW only forbids multiple kernels. The finite
version adds no linear condition L(g) = 0 on the kernel (the Tate moments are already quotiented out in 𝒫_T). PROVED
in finite dimension (W3(a)), applies literally to S_{T,k}.

**Verdict T13.1: NO-GO** within 𝒦_W ∪ 𝒦_H (det-zero non-crossing, Hellmann–Feynman at the crossing, Lipschitz in T).
The finiteness of S_{T,k} is a choice of basis and does not evade the recorded reason for failure: the crossing
coefficient is Σ v_n × (functional of h*).

## 4. T13.2 (jump at the contact): there is no edge; there is a boundary law for the derivative, already recorded as INV_U_001

**4.1 What changes when n enters.** By §1(c), at T_n neither the dimension nor the value of S changes. The new term is
  q_n(F) := −v_n 𝒞F(log n) = −v_n ∫_{−T}^{T−log n} F(x)F(x+log n) dx,  overlap support of length δ = 2T − log n.
As a form on L²(I_T), 𝒞F(ℓ) = ½⟨F,(S_ℓ + S_ℓ*)F⟩ is an **exchange** between [−T,−T+δ] and [T−δ,T]: eigenvalues ±½
with infinite multiplicity (R186_104 row 3a: orbits of length ≤ 2 ⇒ norm-1 exchange). **It is neither rank one nor
of definite sign.** PROVED.

**4.2 Exact jump law in finite coordinates (Lemma J; PROVED for basis E).** For F continuous on [−T,T] (in particular
F ∈ E_k: piecewise Tate exponentials, with well-defined boundary values e(−T), e(T)),
  d/dT q_n(F)|_{T=T_n^+} = −2 v_n F(−T_n)F(T_n),   d/dT q_n(F)|_{T=T_n^−} = 0.
Proof: dδ/dT = 2 and ∫_{−T}^{−T+δ}F(x)F(x+log n)dx = δ·F(−T)F(T) + o(δ) by continuity. ∎
Thus the block G_EE receives at T_n a **derivative jump** −2v_n·(e(−T_n) e(T_n)ᵀ + e(T_n) e(−T_n)ᵀ)/2: rank ≤ 2,
signature (1,1). Separated by parity (S4; basis E chosen even/odd):
  even sector: F(−T) = F(T) ⇒ jump −2v_n F(T)² — **rank one, ≤ 0**;
  odd sector: F(−T) = −F(T) ⇒ jump +2v_n F(T)² — **rank one, ≥ 0**.
This is the only "rank-one edge" that exists: an edge in the derivative, per sector, not in the matrix.

**4.3 Why Lemma J does not transmit to S_{T,k} nor to λ_A.** The block 𝒱_k is only L²; there, pointwise evaluation is
unbounded and q_n|_{𝒱_k} enters with modulus o(1) but not O(δ). The Schur compression mixes both blocks and the
derivative jump of G_EE is compensated/deformed by G_E𝒱 G_𝒱𝒱^{−1} G_𝒱E. The intrinsic result (basis-independent) is
INV_U_001: **there is no jump in λ_A′** (U5b) and the germ is −v_n a_+a_− · 2η/log(κ/2η), with a_± boundary amplitudes
of h*. The jump −2v_n F(±T)² of Lemma J is the "appearance" of that logarithmic germ in a basis that does not resolve
h*'s boundary layer: **discretization artifact** that disappears as k → ∞ (in the sense of R186_104 row 6). ARGUED
(consistent with U2/U5b; the convergence is not proved).

**4.4 Interlacing (Weyl/Cauchy) applied anyway.** If one takes the derivative jump of G_EE as a rank-one perturbation
per sector, Weyl gives, for the even sector, λ_min(T_n + η) ≥ λ_min(T_n) − 2v_n η ‖e(T_n)‖²_{E} − o(η): a lower bound
**in the bad direction** (negative) and in terms of norms, with ‖e(T)‖ ~ (k/T)^{1/2} growing with k. This is criterion
(b)/R-K1 (norm bound) and is dead by L2_003 (scalar transfer, 2×2 falsifier) and by W-lin. There is no exact identity
giving a signed scalar complement: the scalar complement of the derivative edge is −2v_n·(a_+)² / (something ≥ 0),
which cannot be ≥ 0.

**4.5 Worked case 5 → 7 (T = ½log7).** At T = ½log7 = 0.97296, n = 7 enters (previous contacts 2,3,4,5; v_4 includes
Λ(4) = log 2).
- Matrix: S_{½log7,k} with k ≥ k(½log7) (by (L1), k ≳ 30; dim ≥ 58). When 7 enters: S_{½log7^+,k} = S_{½log7^−,k}
  (U0). Jump only in S′, of size 2v_7·F(±T)² ≈ 2(log 7/√7)·F(T)² ≈ 1.47·F(T)² per sector (v_7 = Λ(7)/√7 = 0.7355;
  trivial NUMERICAL).
- There is no small matrix to write: the reduction to a 2×2 or 4×4 at the contact is the "uniform 4×4 Schur"
  reduction, NO-GO (R186_104, confirmed in `06_` l.181). The "near-cancellation of four shifted copies at 1.6·10⁻⁶"
  from CA_R4_001 that TRACT_001 §6.1 wanted to recover as a scalar complement is a property of the minimizer
  (boundary amplitudes a_± and their pairing with the translations log 2, log 3, log 4, log 5), i.e. again
  Σ v_n c_{h*}(log n). It is not an algebraic datum of S.
- Conclusion of the case: at ½log7 there is no edge; there is a boundary germ with coefficient −v_7 a_+a_−, whose sign
  depends on the parity of h* (a_+a_− = ±a_+²). Without information about h* there is no statement.

**Verdict T13.2: the premise (rank-one edge at the contact) is false (PROVED, §1(c), §4.1); the only true version
(Lemma J, rank-one derivative jump per sector in basis E) is a discretized form of INV_U_001, already NO-GO
(𝒦_cross).**

## 5. Λ's distinguishing feature: where could it enter, and why doesn't it?

lem:transfer forces any non-crossing argument to fail for F_DH (T ≥ 9/5, CERT_FALSIFIERS #12, PROVED arb, witness in
the **odd** sector) and for Epstein x²+5y² (T ≥ 1.59, #11).
- **Sign of the contact perturbations.** For ζ, v_n ≥ 0 for all n; by Lemma J the derivative jump is ≤ 0 in the even
  sector and ≥ 0 in the odd one, at every contact. For F_DH the coefficients are complex (χ(2) = i) with real part of
  both signs, so the jumps have both signs in both sectors. **But** Epstein has comb 2Λ_Q(n)/√n ≥ 0 and a_P has comb
  ≥ 0, and both cross: the sign uniformity of the jumps is **not** the distinguishing feature (lem:transfer with
  q_1 = Epstein or a_P). PROVED (by the cited certificates).
- **Lemma M (monotonicity).** λ_A is non-increasing in T (lem:monoT), but not because of the sign of the
  perturbations: the contact term is an indefinite exchange (§4.1); the monotonicity comes from the extension by zero
  𝒫_T ↪ 𝒫_{T′} (S1), common to every real comb. Correction to the objective's formulation ("same-sign perturbations
  ⇒ λ_min decreasing"): the conclusion is true, the reason is not. PROVED.
- So the argument can only have the form "λ_A decreases but never reaches 0," whose content is exactly the
  objective: positivity of 𝔞_T|𝒫_T for every T. In S_{T,k} coordinates, identical. The finite matrix is a basis, with
  size exponential in T, and it inherits thm:margin whole (λ_A ≤ λ_S ≤ λ_A(1+‖K‖)², R186_100/104).
- **Where Λ makes a difference, within this framework:** only in the pairing Σ_{n∈𝒩_T} v_n c_{h*}(log n) (plus the
  boundary germ a_+a_− at each contact), which is a functional of the minimizer (BARRIER_W_001 §5, Theorem X). No
  algebraic property of S_{T,k} (size, rank of S′, interlacing, sign of the jump) sees it. The DH falsifier in the odd
  sector with variable-sign jump, and Epstein/a_P with uniform-sign jump, cover the two possible cases of a "sign
  feature."

## 6. What does remain (new sub-lemmas and their label)

1. **Premise correction (PROVED).** k in S_{T,k} is the number of blocks, not of contacts; at the contacts S is
   continuous and does not change size; k → k+1 does not nest (only k → 2k, L2_002). TRACT_001 R13(d) and §6.1 need
   correcting.
2. **Lemma T3, three-floor inertia tower (PROVED given (L1) and thm:parityschur(a)).** In(W_T) = In(𝔞_T|𝒱_k) +
   In(S_{T,k}) + In(𝔊_T). R6 and (L2) are distinct floors; R6 depends on (L2).
3. **Formula (3.1) of the dilation derivative between contacts (PROVED)**: dS/dT is of infinite rank before
   compression; no low-rank structure.
4. **Lemma J, derivative jump in basis E (PROVED)**: −2v_n F(−T_n)F(T_n), rank one per sector, ≤ 0 even / ≥ 0 odd;
   intrinsically it is INV_U_001 U5b (no jump in λ_A′) — the jump is a basis artifact (ARGUED).
5. **Correction to Lemma M (PROVED)**: the monotonicity of λ_A does not come from the sign of the contact term (which
   is an indefinite exchange, eigenvalues ±½), but from the extension by zero.

None of this gives a sign. No new positivity claim.

## 7. Verdict

**(L2) by interlacing / first crossing is not a route of its own.** The structural premise that made it different
(matrix size changing at the contacts, rank-one edge) is false; with the real structure, T13.1 falls into 𝒦_W ∪ 𝒦_H
(Hellmann–Feynman at the crossing = functional of h*, Lipschitz useless at scale 10⁻⁷⁰ and void at the contacts by
U2, codimension 1 by W3) and T13.2 falls into INV_U_001 / 𝒦_cross (boundary germ with coefficient a_+a_−, functional
of h*). In finite-matrix coordinates (L2) is the objective with the same content (REF-D in the literal sense:
S_{T,k} ⪰ 0 ⟺ λ_A(T) ≥ 0 for any admissible k), and finiteness contributes no tractability because k(T) is
exponential in T and the margin is inherited whole.
Labels: T13.1 **NO-GO** (class 𝒦_W ∪ 𝒦_H, not new); T13.2 **NO-GO** (false premise; residue = INV_U_001); (L2) as an
objective remains **OPEN** (the objective is not closed, the method is). R6 ≠ (L2) (Lemma T3).
What would survive from this family requires a datum that is **not** a functional of the minimizer and that Epstein
(comb ≥ 0) does not have; nothing in the structure of S_{T,k} provides it.

## 8. Entry for the index (`06_OPEN_RESIDUES`, row (L2); and `04_PHASES` phase 204)

| L2_INTERLACE_001 (phase 204) | (L2) by first crossing between contacts (T13.1) + Cauchy interlacing at the contact (T13.2) | NO-GO | False premise: k = number of blocks, not of contacts; S continuous and of fixed size at T_n (U0); k→k+1 does not nest. T13.1 = Hellmann–Feynman at the crossing = functional of h* (𝒦_W/𝒦_H/lem:flowdet); Lipschitz does not cross contacts (U2) and is useless at margin 10⁻⁷⁰. T13.2: the only "edge" = derivative jump −2v_nF(−T)F(T) in basis E (Lemma J, PROVED), an artifact of INV_U_001 U5b. Uniform jump sign is not the feature (Epstein, a_P ≥ 0 cross). New PROVED results: Lemma T3 In(W)=In(𝔞|𝒱_k)+In(S_{T,k})+In(𝔊_T) ⇒ R6 ≠ (L2); correction of lem:monoT's reason (contact = indefinite exchange). |
