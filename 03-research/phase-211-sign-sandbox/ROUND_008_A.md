# Round 008 A — The exact band Schur complement, its Neumann expansion in the comb, and the degree at which the truncation carries the sign

Target (★): λ_A(T) ≥ 0 for every T (STATEMENT_001). Predecessors: ROUND_005_E (sharp band, Lemma 3.0, Theorem 3.1),
ROUND_006_A (π_±(P_T) = π_±(L²(I_T)), λ_max(Π_T) ≤ ½(A_T + V(T)), ratio to A_T in [¼, ½]), ROUND_006_B (§5(iii):
the sign must be carried by an inequality on the captured block). Labels: PROVED / CITED / CONDITIONAL / ARGUED /
OPEN / NO-GO / NUMERICAL. No equivalence of (★) with any other statement is used.

## 0. Notation

H = P_T (or one parity sector of it; both forms preserve parity). Arch = the archimedean form on H, realised as a
self-adjoint operator bounded below with compact resolvent (CITED, Paper 47 prop:nodes), eigenpairs (α_l, u_l),
α_1 ≤ α_2 ≤ …. Π = Π_T = Σ_{n∈N_T} v_n S_{x_n} compressed to H, bounded self-adjoint, π_+ = λ_max(Π), π_− =
−λ_min(Π), both ≤ A_T (ROUND_005_E Lemma 3.0) and ≤ ½(A_T + V(T)) (ROUND_006_A Theorem 2). a_T = Arch − Π,
λ_A(T) = inf of a_T on the unit sphere of the form domain 𝒟.

For a threshold t ∈ ℝ: B_t = span{u_l : α_l ≤ t} (the band, finite-dimensional, dimension n_b = N_Arch(t)),
C_t = B_t^⊥ ∩ 𝒟 (the complement), t_c = min{α_l : α_l > t} (the first archimedean eigenvalue above the threshold).
The sharp band of ROUND_005_E is t = π_+. Block notation relative to H = B ⊕ C: D_b = diag(α_l)_{l∈B},
Arch_c = Arch|_C, Π_bb, Π_bc = Π_cb^*, Π_cc. Since B is a spectral subspace of Arch, Arch(b, c) = 0 for b ∈ B,
c ∈ C ∩ 𝒟: **in this splitting Arch is block-diagonal and the two blocks are coupled only by the comb.**

## 1. Corpus check

- ROUTES-TRIED-INDEX, grep "Neumann", "resolvent", "coer-B", "coer-L1", "thm:coer-schur", "Schur": the hits are the
  von Neumann dimension (Ξ1, NO-GO, unrelated), the resolvent cone order (prop:cone, NO-GO, unrelated: a Möbius
  resolvent, not the archimedean one), POLAR_CAP_001 (bordered Schur complement that inverts a_T|P_T itself —
  consumes λ_A > 0; the present resolvent is that of Arch_c − Π_cc, which is coercive unconditionally), the (L2)
  residue "S_{T,k(T)} ⪰ 0, finite Schur matrix" (OPEN; attacked by norms, determinants, moments, local symbol,
  4×4 Schur: W-det, W-mom, R186_024), AUDIT_204_CLOSURES (thm:coer-schur: blocks, S continuous in T, no
  interlacing at contacts), literature L69/L70/L104 (block-Schur finite/infinite splits with certified tails at
  fixed windows), and P211-6B (word families, NO-GO, whose §5(iii) is the origin of this memo).
- Paper 47 §sec:coer (lines 4876–5339), read. Its reduction thm:coer-schur splits P_T = 𝒱_k ⊕ E_k with E_k the
  piecewise Tate exponentials on k blocks; coercivity of a_T on 𝒱_k comes from a high-pass bound on Arch
  (thm:coer-B) minus the norm ‖Π_T‖ (cor:coer-L1), so k_0(T) is governed by log(k/T) > C_B + ‖Π_T‖, i.e. dim E_k
  doubly exponential in T (rem:coer-size); Arch is NOT block-diagonal in that split, and the coupling operator
  𝖪 is defined abstractly by the Riesz theorem, with no expansion.
- What differs here, and why it avoids the recorded failures. (i) Object: the split is spectral for Arch, so the
  off-diagonal block is −Π_cb alone and the resolvent is (Arch_c − Π_cc)^{−1}, a bounded perturbation of a diagonal
  operator; this is what makes a convergent expansion in the comb weights possible (none exists for 𝖪 of
  thm:coer-schur, where Arch couples the blocks). (ii) Threshold π_+ instead of A_T + C_B: the band dimension is
  N_Arch(π_+) (single exponential in the size of π_+, ROUND_005_E Theorem 3.1), not 2k_0(T) − 2. (iii) Method
  class: the recorded attacks on S_{T,k} (norms, determinants, moments, symbols) treat the matrix as a whole; the
  question here is the *degree in v* at which the sign is decided, i.e. whether a fixed-degree polynomial
  inequality in the weights carries it. That question is not in the index. The (L2) residue is the same kind of
  statement (a finite matrix ⪰ 0 ⟺ (★) at T); nothing below claims more than an equivalent finite form plus its
  graded structure, and the NO-GO (if any) is for the class "bounded-degree truncations".

## 2. The exact band reduction (PROVED)

Theorem 2.1. Let t be a threshold with t_c > π_+ (in particular every t ≥ π_+; t_c > t by definition). Put
C := Arch_c − Π_cc (closed form on C ∩ 𝒟). Then:
(i) C ≥ (t_c − π_+)‖·‖² on C ∩ 𝒟; hence C^{−1} exists, is bounded on C with ‖C^{−1}‖ ≤ (t_c − π_+)^{−1}, and maps
C into C ∩ 𝒟.
(ii) For every b ∈ B, inf_{c ∈ C∩𝒟} a_T(b + c) = ⟨S_T b, b⟩, attained exactly at c = C^{−1}Π_cb b, where
    S_T := D_b − Π_bb − Π_bc C^{−1} Π_cb    (an n_b × n_b real symmetric matrix);
and for all b, c: a_T(b + c) = ⟨S_T b, b⟩ + C[c − C^{−1}Π_cb b].
(iii) (★) at T ⟺ S_T ⪰ 0; λ_A(T) > 0 ⟺ S_T ≻ 0. Quantitatively, with κ := ‖C^{−1}Π_cb‖ ≤ π/(t_c − π_+)
(π := max(π_+, π_−) = ‖Π‖):
    min{λ_min(S_T), t_c − π_+}/(1 + κ)² ≤ λ_A(T) ≤ λ_min(S_T)/(1 + κ²)^{[λ_min(S_T) < 0]} ,  and λ_A(T) ≤ λ_min(S_T)
    whenever λ_min(S_T) ≥ 0.
Proof. (i) For c ∈ C ∩ 𝒟: Arch(c) ≥ t_c‖c‖² (spectral theorem; C is spanned by the u_l with α_l ≥ t_c) and
⟨Πc, c⟩ ≤ π_+‖c‖². So C is a closed, coercive form on the Hilbert space C; by the representation theorem
(Kato VI.2.1, CITED) it is the form of a self-adjoint operator ≥ t_c − π_+ > 0, whose inverse is bounded with the
stated norm and has range in its domain ⊂ C ∩ 𝒟. (ii) Since Arch(b, c) = 0, a_T(b + c) = ⟨(D_b − Π_bb)b, b⟩ −
2Re⟨Π_cb b, c⟩ + C[c]. With y = Π_cb b and c_* = C^{−1}y: C[c] − 2Re⟨y, c⟩ = C[c − c_*] − ⟨C^{−1}y, y⟩ (expand,
using C(c_*, c) = ⟨y, c⟩ for c ∈ C ∩ 𝒟). Both claims follow, the infimum being attained only at c = c_* by (i).
(iii) If S_T ⪰ 0 then a_T(b + c) ≥ C[c − c_*] ≥ 0. If ⟨S_T b, b⟩ < 0 for some b then F = b + c_* has a_T(F) < 0. For
the bounds: F = b + c, ‖F‖² = ‖b‖² + ‖c‖², and ‖b‖² + ‖c‖² ≤ (1 + κ)²(‖b‖² + ‖c − c_*‖²) (triangle inequality, as in
Paper 47 thm:coer-schur); a_T(F) ≥ λ_min(S_T)‖b‖² + (t_c − π_+)‖c − c_*‖² gives the lower bound when λ_min(S_T) ≥ 0
(the case λ_min(S_T) < 0 is the upper bound). Upper: test F = b + c_* with b the bottom eigenvector:
a_T(F) = λ_min(S_T)‖b‖², ‖F‖² = ‖b‖² + ‖c_*‖² ∈ [‖b‖², (1 + κ²)‖b‖²]. ∎

Remarks. (a) The proof uses t only through t_c > π_+; the band is finite-dimensional for every t (compact
resolvent), and t = π_+ is the smallest band of this form. (b) Unlike thm:coer-schur, no high-pass estimate is
needed: coercivity of the complement is the definition of the band plus π_+ < t_c. (c) The same theorem holds
verbatim for every Galerkin compression, with the compressed α_l and π_± (the Galerkin π_+ is below the true one,
ROUND_006_A Theorem 1, which is harmless inside the compression). (d) In the falsifier tests the band of the
falsifier w is taken at w's own π_+^w.

## 3. The Neumann expansion in the comb (PROVED)

Put X := Arch_c^{−1/2} Π_cc Arch_c^{−1/2} and Y := Arch_c^{−1/2} Π_cb (Arch_c ≥ t_c > 0, so Arch_c^{−1/2} is bounded
with norm t_c^{−1/2}; X is bounded self-adjoint on C, Y: B → C bounded). Let r_+ = max(sup spec X, 0),
r_− = max(−inf spec X, 0), r = ‖X‖ = max(r_+, r_−). Then r_± ≤ π_±/t_c.

Theorem 3.1. Assume t_c > π_+ (Theorem 2.1). Then:
(i) r_+ < 1, C = Arch_c^{1/2}(1 − X)Arch_c^{1/2}, C^{−1} = Arch_c^{−1/2}(1 − X)^{−1}Arch_c^{−1/2}, and
    S_T = D_b − Π_bb − Y*(1 − X)^{−1}Y.
(ii) (Convergence.) The series Arch_c^{−1}Σ_{k≥0}(Π_cc Arch_c^{−1})^k converges in operator norm to C^{−1} iff
r < 1; a sufficient condition is max(π_+, π_−) < t_c, i.e. the threshold t is at least ‖Π‖ (so that t_c > ‖Π‖).
Under it,
    S_T = D_b − Π_bb − Σ_{k≥0} Π_bc Arch_c^{−1}(Π_cc Arch_c^{−1})^k Π_cb = D_b − Π_bb − Σ_{k≥0} Y* X^k Y.
(iii) (Grading.) For a fixed threshold t, the k-th term T_k := Π_bc Arch_c^{−1}(Π_cc Arch_c^{−1})^k Π_cb is a homogeneous
polynomial of degree k + 2 in the weights (v_n)_{n∈N_T}: in the Arch eigenbasis,
    (T_k)_{ij} = Σ_{n_0,…,n_{k+1} ∈ N_T} v_{n_0}⋯v_{n_{k+1}} Σ_{l_1,…,l_{k+1} ∈ C} σ^{n_0}_{i l_1} α_{l_1}^{−1} σ^{n_1}_{l_1 l_2} α_{l_2}^{−1} ⋯ α_{l_{k+1}}^{−1} σ^{n_{k+1}}_{l_{k+1} j},
with σ^n_{lm} := ⟨u_l, S_{x_n} u_m⟩ (archimedean overlaps of the truncated shift); the inner sum converges absolutely
in the sense of bounded operators (it is the matrix entry of a product of bounded operators). Hence the truncation
    S_T^{(K)} := D_b − Π_bb − Σ_{k=0}^{K} T_k
is a polynomial matrix in v of degree K + 2, whose coefficients are built from the band eigenvalues α_i (i ∈ B), the
complement eigenvalues α_l (l ∈ C) and the overlaps σ^n — archimedean data only.
(iv) (Two-sided tail.) S_T − S_T^{(K)} = −Y* X^{K+1}(1 − X)^{−1} Y, and with
    ε_K := max{ r_+^{K+1}/(1 − r_+), r_−^{K+1}/(1 + r_−) }:
    S_T^{(K)} − ε_K Y*Y ⪯ S_T ⪯ S_T^{(K)} + ε_K Y*Y,   Y*Y = Π_bc Arch_c^{−1} Π_cb ⪯ (π²/t_c)·1_B.
Moreover, for every odd K, S_T ⪯ S_T^{(K)} (one-sided, no tail term); and for every K,
S_T ⪰ S_T^{(K)} − (r_+^{K+1}/(1 − r_+)) Y*Y.
Proof. (i) For u ∈ C, ⟨(1 − X)u, u⟩ = C[Arch_c^{−1/2}u] ≥ (t_c − π_+)‖Arch_c^{−1/2}u‖² ≥ 0 with equality only at u = 0, and
sup spec X ≤ π_+/t_c < 1 directly from ⟨Πw, w⟩ ≤ π_+‖w‖² ≤ (π_+/t_c)Arch_c[w] (w = Arch_c^{−1/2}u). The factorisation
is an identity of forms on C ∩ 𝒟 = Ran Arch_c^{−1/2}; invert. (ii) Arch_c^{−1}(Π_cc Arch_c^{−1})^k =
Arch_c^{−1/2}X^kArch_c^{−1/2}; the series Σ X^k converges in norm iff the spectral radius r < 1 (X self-adjoint),
to (1 − X)^{−1}; r_± ≤ π_±/t_c. (iii) Multilinearity of Π = Σ v_n S_{x_n} in each of the k + 2 factors; insert the
spectral resolution of Arch_c^{−1} = Σ_{l∈C} α_l^{−1} u_l ⊗ u_l between them. (iv) Σ_{k>K} X^k = X^{K+1}(1 − X)^{−1} = f_K(X)
with f_K(x) = x^{K+1}/(1 − x). On [0, r_+], 0 ≤ f_K ≤ r_+^{K+1}/(1 − r_+); on [−r_−, 0], |f_K(x)| = |x|^{K+1}/(1 + |x|) ≤
r_−^{K+1}/(1 + r_−) (s ↦ s^{K+1}/(1 + s) increasing). Hence −ε_K ≤ f_K(X) ≤ ε_K, and conjugation by Y gives the
two-sided bound. For K odd, f_K ≥ 0 on spec X ⊂ (−1, 1), so Y*f_K(X)Y ⪰ 0 and S_T ⪯ S_T^{(K)}. For any K, f_K ≤
r_+^{K+1}/(1 − r_+) on spec X. Y*Y ⪯ ‖Π_cb‖²/t_c. ∎

Corollary 3.2 (what a truncation can certify; PROVED). (a) If λ_min(S_T^{(K)}) < 0 for some odd K, then λ_A(T) < 0.
(b) If λ_min(S_T^{(K)} − ε_K Y*Y) > 0 (resp. − (r_+^{K+1}/(1 − r_+))Y*Y), then λ_A(T) > 0. (c) A degree-(K + 2) inequality
resolves the sign at T only if ε_K‖Y*Y‖ ≲ λ_min(S_T), i.e. K + 1 ≳ log(‖Y*Y‖/((1 − r)λ_min(S_T)))/log(1/r).
(c) is the quantitative content of OBJECT_SPEC R3(i) for this object: the degree needed is the precision
log(1/λ_min(S_T)) divided by the per-degree gain log(1/r).

Remark 3.3 (scale behaviour, contrast with ROUND_006_B Prop. 4.1). With the band fixed, S^{(K)}(cv) = D_b − cΠ_bb −
Σ_k c^{k+2}T_k(v) is NOT homogeneous: the cΛ falsifier moves every degree differently. The truncation is therefore
not blind to c in the way the word families are; whether it rejects c = 1.01 at bounded degree is the numerical
question of §4.

