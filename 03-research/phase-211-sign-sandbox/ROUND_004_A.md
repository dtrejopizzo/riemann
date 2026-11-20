# Round 004 A — Λ-independent archimedean planes: the k × k necessary conditions on the exact Λ(n)

Notation of STATEMENT_001 and ROUND_003_A: Arch(F) = (1/2π)∫ m|F̂|², Π(F) = Σ_{log n<2T} v_n Re c_F(log n),
v_n = 2Λ(n)/√n, a_T = Arch − Π, P_T^ev the even part of P_T. Let α_1 ≤ α_2 ≤ … be the eigenvalues of Arch on P_T^ev
with orthonormal eigenvectors e_1, e_2, …, and E_k = span{e_1, …, e_k}. These are Λ-free. For x = log n put

    R_n(E)_{ij} = ½∫ [e_i(t) e_j(t − x) + e_j(t) e_i(t − x)] dt = (1/2π)∫ cos(τx) Re(ê_i(τ) conj ê_j(τ)) dτ,

so Π|_{E_k} = Σ_n v_n R_n(E_k) and a_T|_{E_k} = diag(α_1, …, α_k) − Σ_n v_n R_n(E_k).
Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## 1. Corpus check

- The index records "nodal/Sturm criterion, fixed finite archimedean truncation" as DEAD with reason "arena N* ≥ 12, no
  fixed truncation decides S_even" (04_PHASES_100-189, G8D-155 thm:arena/P8 and G8D-R160_S4 §2.D#45-46). The present memo
  does not try to decide the sign by a fixed truncation. What differs: the object is the family of NECESSARY conditions
  a_T|_{E_k} ⪰ 0, written as explicit polynomial inequalities in the exact Λ(n), and the question is whether such a
  condition passes the falsifier test of the brief. The answer (§4, Proposition B) is a NO-GO with a class statement that
  the index does not contain: it concerns every fixed finite Λ-independent subspace, not only the archimedean one, and the
  reason is the falsifier test, not the arena count. The arena theorem is used in §5 only to quantify it.
- ROUND_003_A Lemma 4 (rigidity) is the dual statement for Λ-dependent near-kernels; Proposition B below is its
  counterpart for Λ-independent planes.
- Lemma N of Paper 47 (prime atoms as one-sided overlaps) is CITED as the form of Lemma A.

## 2. Validation numerics (NUMERICAL)

Method of ROUND_003_A §2 (Dirichlet sines, N = 40 and 80, Arch by quadrature on |τ| ≤ 6000, Π exact in t-space, even
sector imposed by the constraint ∫F cosh(t/2) = 0). E_k is built from the Galerkin eigenvectors of Arch on the even
section; it is an explicit subspace of P_T^ev, so every number below is the exact (up to quadrature) value of a form on an
explicit subspace. Positive values certify nothing about (★); negative values are explicit witnesses (REVIEW_003 §2) for
the modified combs, valid up to quadrature error. N = 40 and N = 80 agree to two or three digits in every entry; the
table shows N = 80. The window ½log5 is taken at ½log5 + 10⁻³ (stored matrices); the atom n = 5 then has overlap
2T − log 5 = 2·10⁻³ and R_5 ≈ 0.

2.1 The plane E_2 (k = 2).

| T | α_1, α_2 | eig Π|E_2 | eig a_T|E_2 | trace (α_1+α_2) vs tr Π | det a_T|E_2 |
|---|---|---|---|---|---|
| log 2 | −0.150, 0.472 | −0.187, +0.406 | 0.002, 0.101 | 0.322 ≥ 0.219 | 2.3·10⁻⁴ |
| ½log5 | −0.305, 0.321 | −0.361, +0.222 | 0.001, 0.153 | 0.016 ≥ −0.139 | 1.9·10⁻⁴ |
| 0.9 | −0.420, 0.209 | −0.438, +0.177 | 0.001, 0.048 | −0.211 ≥ −0.260 | 3.8·10⁻⁵ |
| 1.0 | −0.531, 0.102 | −0.564, +0.054 | 1·10⁻⁴, 0.080 | −0.429 ≥ −0.509 | 1.2·10⁻⁵ |
| 1.2 | −0.728, −0.083 | −0.747, −0.107 | 6·10⁻⁵, 0.044 | −0.811 ≥ −0.855 | 2.7·10⁻⁶ |

Answers. (i) Π|_{E_2} is indefinite at log 2, ½log5, 0.9, 1.0, and NEGATIVE DEFINITE at 1.2 (there α_2 < 0 as well,
consistent with the arena count: two even archimedean eigenvalues below 0). (ii) a_T|_{E_2} ⪰ 0 at every tested window,
with smallest eigenvalue 10⁻³ … 6·10⁻⁵, far above λ_A(T). (iii) E_2 does NOT capture the pin pair of ROUND_003_A: the
principal cosines between E_2 and the span of the two lowest even eigenvectors of a_T are (0.999, 0.92), (0.999, 0.77),
(0.998, 0.58), (0.994, 0.41), (0.987, 0.57) at the five windows; the Π-Gram eigenvalues on E_2 differ from those of
ROUND_003_A §2.1 by 0.1–0.2 (e.g. −0.187/+0.406 vs −0.095/+0.546 at log 2). The first Arch eigenvector is close to the
a_T ground state; the second is not close to the second a_T eigenvector beyond T ≈ 0.7.

The matrices R_n(E_2) (N = 40; upper triangle r_11, r_12, r_22):

| T | n=2 | n=3 | n=4 | n=5 | n=7 | n=8 | n=9 |
|---|---|---|---|---|---|---|---|
| log 2 | −.439, .201, .386 | .199, −.119, .020 | | | | | |
| ½log5 | −.607, −.021, .568 | .122, .142, −.334 | .136, −.133, .126 | ≈0 | | | |
| 0.9 | −.634, −.151, .396 | −.067, .295, −.260 | .201, −.081, −.056 | .093, −.101, .110 | | | |
| 1.0 | −.591, −.220, .087 | −.280, .292, .080 | .135, .115, −.312 | .188, −.126, .048 | .008, −.009, .011 | | |
| 1.2 | −.409, −.225, −.468 | −.554, .052, .557 | −.190, .309, −.088 | .082, .182, −.343 | .181, −.126, .058 | .128, −.126, .121 | .067, −.075, .084 |

(The sign of e_2 is a convention; r_12 changes sign with it, r_12² does not. At T = 1.2 the atom n = 11 has overlap
2·10⁻³ and R_11 ≈ 0.)

2.2 The spaces E_3, E_4, E_6. a_T|_{E_k} ⪰ 0 at every window and every k (smallest eigenvalue, N = 80):

| T | k = 3 | k = 4 | k = 6 |
|---|---|---|---|
| log 2 | 3.7·10⁻⁴ | 8.3·10⁻⁵ | 3.2·10⁻⁵ |
| ½log5 | 3.0·10⁻⁵ | 1.8·10⁻⁵ | 1.3·10⁻⁶ |
| 0.9 | 4.2·10⁻⁵ | 2.8·10⁻⁶ | 1.9·10⁻⁷ |
| 1.0 | 2.4·10⁻⁵ | 2.0·10⁻⁶ | 1.6·10⁻⁸ |
| 1.2 | 1.1·10⁻⁵ | 7.3·10⁻⁸ | 5.5·10⁻¹¹ |

The smallest eigenvalue falls with k toward λ_A(T) (≈ 10⁻⁷, 3·10⁻¹², ≲ 10⁻¹⁴ … at the five windows); the second principal
cosine with the a_T pin pair rises to 0.998–0.9999 at k = 6. These are the necessary conditions that Paper 47 has
certified on its own archimedean modes at log 2; here they are seen to hold (NUMERICAL) at all five windows.

2.3 Falsifiers on E_k: smallest eigenvalue of diag(α) − Π_w|_{E_k} for the modified comb w (N = 80; "+" = condition
still satisfied, i.e. the falsifier is NOT rejected).

| T | k | cΛ, c = 0.9 / 0.99 / 1.01 / 1.1 | no 2 | no 3 | η = +0.1 / −0.1 / +0.5 | swap 2↔3 | 3 → 3.2 |
|---|---|---|---|---|---|---|---|
| log 2 | 2 | −3·10⁻⁴ / **+.0027** / **+.0018** / −.011 | −.43 | −.03 | −.03 / −.03 / −.27 | −.10 | −.06 |
| log 2 | 3, 4, 6 | c = 0.99: **+.0009, +.0008, +.0007**; others − | − | − | − | − | − |
| ½log5 | 2 | −.015 / +0.0000 / **+.0023** / **+.0072** | −.48 | −.35 | −.005 / −.06 / −.30 | −.16 | −.10 |
| 0.9 | 2 | −.032 / −.0015 / **+.0027** / **+.0037** | −.52 | −.55 | −.02 / −.08 / −.25 | −.18 | −.13 |
| 1.0 | 2 | −.039 / −.0029 / **+.0030** / **+.0183** | −.53 | −.50 | **+.039** / −.09 / −.03 | −.03 | −.12 |
| 1.2 | 2 | −.061 / −.0047 / **+.0043** / **+.0271** | −.53 | −.64 | **+.071** / −.09 / **+.194** | −.03 | −.13 |
| ½log5 … 1.2 | 3, 4, 6 | all negative (−3·10⁻⁴ … −0.08) | − | − | − | − | − |

Reading. The 2 × 2 condition is passed by cΛ with c > 1 at every window ≥ ½log5, by c = 0.99 at log 2, and by
Λ + 0.1·1_2 at T = 1.0, 1.2 (and Λ + 0.5·1_2 at 1.2). From k = 3 on, every tested falsifier is rejected except c = 0.99 at
log 2, where the band of surviving c is |c − 1| ≲ 10⁻² for every k ≤ 6.

## 3. Pure mathematics: the conditions written out

Proposition 1 (the necessary conditions; PROVED). If (★) holds at T, then for every k

    (C_k)   diag(α_1, …, α_k) − Σ_{log n<2T} v_n R_n(E_k) ⪰ 0,

where α_j and R_n(E_k) depend only on T. For k = 2, with p_ij := Σ_n v_n R_n(E_2)_{ij}, (C_2) is equivalent to the three
inequalities

  (L1)  Σ_n v_n R_n,11 ≤ α_1,                      linear; α_1 < 0 for T ≥ 0.60, so the prime atoms must be net
                                                     negative on e_1 by at least |α_1|;
  (L2)  Σ_n v_n R_n,22 ≤ α_2,                      linear;
  (Q)   Σ_{m,n} v_m v_n ½D(R_m, R_n) − α_2 Σ_n v_n R_n,11 − α_1 Σ_n v_n R_n,22 + α_1α_2 ≥ 0,

where D(A, B) = a_11b_22 + a_22b_11 − 2a_12b_12 is the mixed discriminant (D(A, A) = 2 det A). (Q) is
(α_1 − p_11)(α_2 − p_22) ≥ p_12². (Since a PSD 2 × 2 matrix needs both diagonal entries ≥ 0 and determinant ≥ 0, and
these imply the trace condition, (L1), (L2), (Q) are equivalent to "trace ≥ 0 and det ≥ 0".) For general k, (C_k) is the
nonnegativity of all principal minors, polynomial inequalities of degree ≤ k in (v_n).
Proof. (★) says a_T(F) ≥ 0 for F ∈ P_T; restrict to E_k ⊂ P_T^ev ⊂ P_T and use Arch e_j = α_j e_j. The 2 × 2 case is the
determinant/diagonal test, expanded bilinearly in v. ∎

The quadratic step. (Q) is the only nonlinear content of (C_2). Its quadratic part is the form v ↦ Σ v_m v_n ½D(R_m, R_n)
on the window positions; it couples pairs of prime powers (m, n) through the mixed discriminant of their overlap matrices,
not through any arithmetic relation between m and n. (L1) alone is the single-test-function condition a_T(e_1) ≥ 0,
already of the type recorded in the corpus; (Q) is the first condition that needs two atoms at once.

Lemma A (size and regularity of R_n; PROVED). Let E ⊂ P_T^ev be finite-dimensional with orthonormal basis (e_i), x = log n
∈ (0, 2T), and G_E(x) the Gram matrix ⟨e_i, e_j⟩_{L²(x−T, T)}. Then
  (i) ‖R_n(E)‖_op ≤ λ_max(G_E(x)) ≤ 1, and |R_n(E)_{ij}| ≤ ‖e_i‖_{L²(x−T,T)}‖e_j‖_{L²(x−T,T)};
  (ii) for T ≤ x < 2T, with h = 2T − x: since e_i ∈ H¹_0(I_T), ‖e_i‖²_{L²(T−h,T)} ≤ h²‖e_i′‖²/2, hence
       ‖R_n(E)‖ ≤ tr G_E(x) ≤ (2T − x)² Σ_i ‖e_i′‖²/2 (edge decay);
  (iii) x ↦ R(x) is Lipschitz on [0, 2T] with constant ≤ max_{i,j} ‖e_i‖‖e_j′‖, and R(0) = I.
Proof. (i) Write R = ½(B + Bᵀ), B_ij = ∫_{x−T}^{T} e_i(t) e_j(t − x) dt = ⟨U_i, V_j⟩ with U_i = e_i 1_{(x−T,T)} and
V_j = e_j(· − x)1_{(x−T,T)}. By evenness of e_j and t ↦ x − t, the Gram matrix of (V_j) equals G_E(x), as does that of
(U_i). Then |ξᵀBη| = |⟨Σξ_iU_i, Σ η_jV_j⟩| ≤ (ξᵀGξ)^{1/2}(ηᵀGη)^{1/2} ≤ λ_max(G)|ξ||η|. The entrywise bound is
Cauchy–Schwarz. (ii) For x ≥ T the interval (x − T, T) = (T − h, T) lies at the edge. For e ∈ H¹_0 with e(T) = 0,
|e(t)|² ≤ (T − t)‖e′‖², integrate over (T − h, T): ≤ h²‖e′‖²/2; and λ_max(G) ≤ tr G. (iii) Differentiate under the integral; the boundary terms
vanish because e_i(±T) = 0. ∎
CITED form: Paper 47 Lemma N writes each prime atom as such a one-sided overlap; Lemma A is that statement on a k-frame.
What is NOT proved: any sign pattern of R_n(E)_{11} in n. The table of §2.1 shows r_11(2) < 0 at every window but
r_11(n) of both signs for n ≥ 3, varying with T; the sign of p_11 is a cancellation among atoms (NUMERICAL).

## 4. Falsifier test (rule 4) and the class NO-GO

Proposition B (finite Λ-independent subspaces cannot carry the sign; PROVED). Let E ⊂ P_T be any finite-dimensional
subspace chosen without reference to Λ, and let ε_E := λ_min(a_T|_E).
  (i) If ε_E > 0, the condition a^w_T|_E ⪰ 0 holds for every weight vector w with Σ_n |w_n − v_n| < ε_E (positions fixed),
      for every cΛ with |c − 1|·‖Π|_E‖ < ε_E, and for every shift of positions x_n ↦ x_n′ with Σ v_n |x_n − x_n′| L_E < ε_E
      (L_E the Lipschitz constant of Lemma A(iii)). Hence the condition passes falsifiers (a), (d) and small Beurling
      shifts of type (c): it cannot be a sign step.
  (ii) If ε_E = 0 then, under (★), λ_A(T) = 0 and E contains a minimiser of a_T on P_T; i.e. E is not Λ-independent in
      any useful sense (it contains a Λ-dependent vector) — and λ_A(T) = 0 is itself excluded by the strict margin bounds
      only if those are available, which is the question.
  (iii) If ε_E < 0, (★) fails at T.
Proof. (i) a^w|_E = a_T|_E − Σ (w_n − v_n)R_n(E) ⪰ (ε_E − Σ|w_n − v_n|‖R_n(E)‖)I ⪰ 0 by Lemma A(i); the same with
(c − 1)Π|_E; for shifts, Lemma A(iii). (ii)–(iii) are min–max. ∎
Reading. Any fixed finite family of Λ-independent necessary conditions is open in the weights, and a sign step must fail
at cΛ for every c ≠ 1 (STATEMENT §4). So no finite set of conditions (C_k) can be the sign step; at best it is a
necessary condition with a quantified tolerance |c − 1| ≤ ε_E/‖Π|_E‖. The numerics of §2.3 are the instance: E_2 fails
the test for c > 1 at T ≥ ½log5 and for η = +0.1 at T ≥ 1.0; E_3–E_6 reject all tested falsifiers except the band
|c − 1| ≲ ε_E/‖Π|_E‖ ≈ 10⁻² at log 2 (ε_{E_k} ≈ 3·10⁻⁵ … 4·10⁻⁴, ‖Π|_E‖ ≈ 0.6–0.85 — the observed band is wider than
this crude bound because Π|_E is indefinite; the exact band is where λ_min(a_T|_E − (c − 1)Π|_E) ≥ 0).

NO-GO (class: necessary conditions a_T|_E ⪰ 0 on a fixed finite-dimensional Λ-independent subspace E ⊂ P_T, at a fixed
T, used as the sign step). PROVED by Proposition B(i): any such condition satisfied with slack survives an open set of
falsifiers. This does not touch T-dependent families with dim E → ∞, treated in §5.

## 5. Can a T-uniform family of planes work? (assessment)

(a) The plane condition never implies (★) by itself. With E ⊂ P_T and E^⊥ its complement in P_T, a_T ⪰ 0 on P_T iff
C := a_T|_{E^⊥} ≻ 0 and a_T|_E − B C^{-1} Bᵀ ⪰ 0 (Schur complement; B the coupling block) — PROVED (standard, with C
having compact resolvent; CITED Paper 47 prop:nodes for Arch). So a route through E_T needs two further statements: a
positivity of a_T on E_T^⊥ and a bound on the coupling B C^{-1}Bᵀ by ε_{E_T}.

(b) The arena theorem forbids the first for any fixed dim E. Paper 47 thm:arena (CITED): the (k+1)-st even archimedean
eigenvalue is ≤ m((2k + 3)π/2T) = log k + O(1), while ‖Π‖ is of order Σ_n v_n ≍ e^T. On E_k^⊥ the restriction of Arch
still has eigenvalues α_{k+1}, α_{k+2}, … ≤ log(k + j) + O(1) with no prime-independent reason for a_T to be positive
there unless α_{k+1} exceeds the size of Π on E_k^⊥. Thus "Arch dominates Π on E_k^⊥" (the only Λ-free way to prove C ≻ 0)
needs k ≥ N*(T), the arena count, which Paper 47 shows grows doubly exponentially in T (N* ≥ 12 at log 2). ARGUED as the
quantitative reading; PROVED in the weak form "for k fixed and T large, Arch|_{E_k^⊥} has an eigenvalue ≤ log(k+1) + O(1)
< ‖Π|_{E_k^⊥}‖" only if the latter norm is shown to grow, which is OPEN here (we have not proved a lower bound on Π
restricted to E_k^⊥).

(c) The second requirement is at margin precision. Under (★), λ_min(a_T|_{E_T}) ≥ λ_A(T), and the coupling bound must
leave at least λ_A(T) ≤ 4·10⁹Te^{−15.449T} (Paper 47, CITED). The numerics show ε_{E_k} − λ_A ranges from 10⁻³ (k = 2) to
5·10⁻¹¹ (k = 6, T = 1.2): the plane's slack is spent almost entirely by the coupling to E^⊥, and to close the Schur
complement one must estimate BC^{-1}Bᵀ to that precision. Equivalently, E_T must contain the a_T ground state up to an
energy-norm error whose square is ≲ margin. A Λ-independent family can do this only if the ground state is determined to
that precision by Λ-free data, which is exactly what Proposition B rules out at each fixed T (the ground state moves at
first order under w ↦ w + δ, Danskin, CITED in the index INVENT_001, while E_T does not).

(d) Conclusion of the assessment (ARGUED). A T-uniform family E_T with a provable inequality and a proof of (★) from it
must have dim E_T ≥ N*(T) and must carry, in its Schur complement, Λ-dependent information at relative precision
e^{−15.449T}. Such a family is not excluded in principle (dim E_T → ∞ removes Proposition B: an infinite-dimensional
condition can be closed in the weights), but it is then no longer a "plane" condition; the 2 × 2 / k × k inequalities on
Λ-free planes are validation tools, not a sign step.

## Result

NO-GO with class: necessary conditions a_T|_E ⪰ 0 on a fixed finite-dimensional Λ-independent subspace E ⊂ P_T (in
particular the archimedean planes E_k, k = 2, 3, 4, 6) cannot be the sign step for (★): they are open in the weights and
survive falsifiers (a), (d) and small shifts (Proposition B, PROVED; instances NUMERICAL).

## What was proved

- Proposition 1: (C_k) is necessary for (★); for k = 2 it is (L1), (L2) linear in v and (Q) quadratic in v with
  coefficients the mixed discriminants ½D(R_m, R_n) of the overlap matrices, all depending only on T.
- Lemma A: ‖R_n(E)‖ ≤ λ_max(G_E(log n)) ≤ 1, edge decay (2T − log n)², Lipschitz in log n, R(0) = I.
- Proposition B: a strictly satisfied Λ-free finite-dimensional condition tolerates every weight perturbation of ℓ¹ size
  < ε_E; hence the NO-GO.
- NUMERICAL: (C_k) holds at log 2, ½log5, 0.9, 1.0, 1.2 for k = 2, 3, 4, 6 (N = 40/80 agree); Π|_{E_2} is indefinite for
  T ≤ 1.0 and negative definite at 1.2; E_2 does not capture the a_T pin pair beyond T ≈ 0.7 (second principal cosine
  0.41–0.77); E_6 does (≥ 0.997). The 2 × 2 condition passes cΛ for c > 1 (T ≥ ½log5), c = 0.99 (log 2), and Λ + 0.1·1_2
  (T ≥ 1.0); E_3–E_6 reject every tested falsifier except |c − 1| ≲ 10⁻² at log 2.

## What failed and why

- The hope of ROUND_003_A that the Λ-free plane E_2 reproduces the pin (Π-Gram eigenvalues within 10⁻²): false, off by
  0.1–0.2; and Π|_{E_2} is not even indefinite at T = 1.2.
- The 2 × 2 inequality as a sign step: fails the falsifier test numerically (cΛ, c > 1; η = +0.1) and, by Proposition B,
  any finite k × k version fails it in principle.
- No sign pattern of R_n(E)_{11} in n was obtained; (L1) holds by cancellation among atoms.

## Next concrete step

Since only growing families escape Proposition B, test the Schur complement directly: at T = 1.0, 1.2 compute
B C^{-1} Bᵀ for E = E_k and record how ε_{E_k} − λ_min(a_T|_E − BC^{-1}Bᵀ) decays with k; if it decays like the
archimedean gap α_{k+1}^{-1}‖B‖², a k(T) ≈ N*(T) family has an explicit, Λ-dependent but finitely-indexed tail term whose
size could be bounded by Lemma A edge decay — that is the only form in which a plane family could carry the sign.
