# Round 5, memo B: the comb-Krylov family from the archimedean negative cone

Object (OBJECT_SPEC_001, first candidate direction). On the window I_T = [−T, T], with P the orthogonal projection of
L²(I_T) onto P_T (the two Tate conditions ∫F e^{±x/2} = 0) and a_T = Arch − Π the form of STATEMENT_001, put

  Neg_T = span of the eigenvectors of P·Arch·P on P_T with negative eigenvalue,
  K_j   = span{(PΠP)^i e : e ∈ Neg_T, 0 ≤ i < j}      (j ≥ 1; K_1 = Neg_T),

and compare with the archimedean planes E_k = span of the k lowest eigenvectors of P·Arch·P (ROUND_004_A, here taken in
both parities at once, so E_k here has k/2 vectors of each parity approximately). The question: does the comb-generated
family K_j reach the ground state of a_T on P_T with dimension O(T), while E_k needs the arena count?

## Corpus check

- ROUTES-TRIED-INDEX: the only Krylov entry is G8D-R164_502c (tool L5), the Krylov space of the Wiener–Hopf SYMBOL
  operator σ_T (DEAD for symbol non-positivity). The generator here is different: the comb operator Π itself, acting on
  the archimedean negative cone, with P_T imposed. The recorded failure (σ_T(0) < 0, symbol never positive) concerns a
  positivity of the symbol, which this memo does not use; the family is tested only as a capture device for the
  minimiser, so the recorded obstruction does not apply to it.
- ROUND_004_A (planes E_k): Proposition B kills every fixed Λ-free finite subspace. K_j is Λ-dependent (its vectors are
  polynomials in v, §1), so Proposition B does not apply to it directly; this memo measures whether that Λ-dependence
  buys capture.
- Grid R162_2300: no Krylov-of-Π entry (grep "Krylov": only the phase-164 symbol item).

Numerical set-up (all NUMERICAL claims below). Galerkin space: the first N = 80 Dirichlet sines e_k, both parities;
P_T imposed exactly by restriction to the 78-dimensional null space of the two constraint rows (Gauss–Legendre, 800
nodes); Arch from the saved matrices (spectral quadrature to τ = 6000), the comb matrix Π exactly by lem:combsine-type
quadrature (Gauss–Legendre 600 nodes per atom); Π^i means powers of the Galerkin compression QᵀΠQ. Krylov blocks were
built by block Gram–Schmidt with re-orthogonalisation (rank tolerance 10⁻¹⁰); no rank loss occurred up to j = 16.
Scripts: r5.py, r5b.py (scratch). T-values: log 2, ½log5 − 10⁻³ and ½log5 + 10⁻³ (the saved matrices), 0.9, 1.0, 1.2, 1.4.

Precision caveat (essential for reading every table). At N = 80 in double precision, the computed λ_A is
1.1·10⁻⁷ (log 2), 3.1·10⁻¹² (½log5 + 10⁻³), 4.5·10⁻¹⁵ (0.9), and |λ_A| ≤ 2.3·10⁻¹⁴ at T ≥ 1.0, where it is at the
round-off floor (negative computed values there are noise, not a sign). The low spectrum of a_T is a cluster:
#{eigenvalues < 10⁻³} = 2, 4, 4, 6, 9, 16, 26 at the seven T-values. Statements about "capturing the ground state" at
T ≥ 1.0 therefore mean capturing this cluster; the individual ground vector is not resolved.

## 1. Bookkeeping (PROVED)

Notation. u_n = log n, N_T = {n ≥ 2 : Λ(n) > 0, u_n < 2T}, v_n = 2Λ(n)/√n. For 0 < u < 2T let S_u be the bounded
operator on L²(I_T), (S_uG)(x) = G(x + u)·1[x + u ∈ I_T]. Then S_u^*G(x) = G(x − u)·1[x − u ∈ I_T], and the comb form
of a_T is ⟨F, ΠF⟩ with

  Π = Σ_{n∈N_T} v_n · ½(S_{u_n} + S_{u_n}^*),                                                         (1.1)

since ⟨F, S_uF⟩ = ∫_{−T}^{T−u} F(x)F(x+u)dx = c_F(u) for real F (lem:combsine, CITED Paper 46).

Proposition 1.1 (degree-2 entries; PROVED). For e, e′ ∈ L²(I_T),

  ⟨e, Π² e′⟩ = ¼ Σ_{m,n∈N_T} v_m v_n Σ_{σ,σ′∈{±1}} ∫_{J(σu_m, σ′u_n)} e(x + σu_m) e′(x + σ′u_n) dx,          (1.2)

  J(a, b) = [−T + max(0, a, b), T + min(0, a, b)]  (empty when its length 2T − (max(0,a,b) − min(0,a,b)) ≤ 0).

The window length is 2T − max(u_m, u_n) when σ = σ′ and 2T − u_m − u_n when σ = −σ′; the second family is non-empty
exactly for the pairs with mn < e^{2T}. After the substitution y = x + σu_m each term is ∫ e(y) e′(y + δ) dy over an
interval, with shift δ = σ′u_n − σu_m ∈ {±log(n/m), ±log(mn)}: the degree-2 entries are window correlations of e, e′
at the ratios n/m and the products mn of comb points. For the compressed operator PΠP (needed because K_j lives in P_T),

  ⟨e, ΠPΠ e′⟩ = ⟨Πe, Πe′⟩ − Σ_{i=1,2} ⟨Πe, q_i⟩⟨q_i, Πe′⟩,                                              (1.3)

with q_1, q_2 an orthonormal basis of span{e^{x/2}, e^{−x/2}} ⊂ L²(I_T), and ⟨q_i, Πe⟩ = Σ_n v_n ½(⟨q_i, S_{u_n}e⟩ +
⟨q_i, S_{u_n}^*e⟩), a linear form in v whose coefficients are ∫ e^{±x/2} e(x ± u_n) over windows of length 2T − u_n.
So (1.3) is again a quadratic polynomial in v, the correction being a sum of products of two single-shift
exponential moments.

Proof. Π is self-adjoint by (1.1), so ⟨e, Π²e′⟩ = ⟨Πe, Πe′⟩. Expand Πe = ½ Σ_m v_m Σ_σ S_{σu_m}e, writing S_{−u} := S_u^*;
(S_{σu}e)(x) = e(x + σu)·1[x + σu ∈ I_T] for x ∈ I_T. Hence ⟨S_{σu_m}e, S_{σ′u_n}e′⟩ = ∫ e(x + σu_m)e′(x + σ′u_n) over
{x : x, x + σu_m, x + σ′u_n ∈ I_T} = J(σu_m, σ′u_n). Multiplying out gives (1.2) with the factor ¼. For (1.3), P = I −
Σ_i |q_i⟩⟨q_i| and ⟨e, ΠPΠe′⟩ = ⟨Πe, PΠe′⟩. ∎

In the sine basis each term of (1.2) is elementary: for an interval [α, β] and shift δ,
∫_α^β e_k(y)e_l(y + δ)dy = (1/2T)∫_α^β [cos(ω_k(y+T) − ω_l(y+δ+T)) − cos(ω_k(y+T) + ω_l(y+δ+T))]dy, closed form as in
lem:combsine; no new constants enter.

Proposition 1.2 (polynomial structure of K_j; PROVED). Let (P Arch P)|_{P_T} have negative spectral subspace Neg_T, of
finite dimension d_T (compact resolvent of Arch on the window: CITED Paper 46 prop:nodes; Neg_T does not depend on v).
Then K_j is spanned by the d_T·j vectors (PΠP)^i e_r (e_r a basis of Neg_T, i < j), and the coefficient
⟨e_k, (PΠP)^i e_r⟩ is a homogeneous polynomial of degree i in (v_n)_{n∈N_T}:

  ⟨e_k, (PΠP)^i e_r⟩ = 2^{−i} Σ_{n_1,…,n_i∈N_T} v_{n_1}⋯v_{n_i} Σ_{σ_1,…,σ_i} ⟨e_k, P S_{σ_1u_{n_1}} P ⋯ P S_{σ_iu_{n_i}} P e_r⟩,

with v-independent coefficients. Consequently every vector of K_j is, in the sine basis, a combination of vectors whose
coefficients are polynomials in v of degree < j, and the Gram matrix ⟨(PΠP)^i e_r, a_T (PΠP)^{i′} e_{r′}⟩ has entries
polynomial in v of degree ≤ i + i′ + 1. Proof: (1.1) is linear in v, P and e_r are v-independent; expand the i-fold
product. ∎

Remark (scope). The orthonormalised basis of K_j and the Schur complements below are rational/algebraic, not
polynomial, in v; Proposition 1.2 is about the spanning set only. The Galerkin computation uses the compression of Π to
span{e_1..e_80} ∩ P_T, whose powers differ from (PΠP)^i by the tail Σ_{l>80} in each intermediate sum.

Reading against R2. The family meets the letter of R2: the entries that decide the bottom of a_T|_{K_j} (j ≥ 2) are
non-linear in v, and (1.2) shows that the first non-linear level is exactly the semiring interplay (ratios n/m with the
same-sign windows, products mn < e^{2T} with the opposite-sign windows). Whether this content reaches the sign is the
numerical question of §2–4.

## 2. The negative cone and the Krylov spaces (NUMERICAL)

Table 2.1. d_T = dim Neg_T on P_T (N = 80) against lem:archcount (CITED Paper 46: n_−(Arch) ≥ ⌈2Tt_0/π⌉ − 1 on the full
window; imposing the two Tate conditions can remove at most 2).

| T | lem:archcount (full) | its P_T consequence (≥) | d_T observed | negative Arch eigenvalues on P_T |
|---|---|---|---|---|
| log 2 | 2 | 0 | 1 | −0.150 |
| ½log5 + 10⁻³ | 3 | 1 | 1 | −0.305 (next +1.1·10⁻⁴) |
| 0.9 | 3 | 1 | 2 | −0.420, −0.112 |
| 1.0 | 4 | 2 | 2 | −0.531, −0.218 |
| 1.2 | 4 | 2 | 3 | −0.728, −0.404, −0.083 |
| 1.4 | 5 | 3 | 4 | −0.902, −0.562, −0.241, −0.052 |

d_T grows like ≈ 4T − 2, as lem:archcount predicts. K_j has full dimension j·d_T for every tested j ≤ 16 (no Krylov
breakdown); the smallest singular value of the raw (un-orthogonalised) generator matrix decays geometrically in j
(e.g. 1.6·10⁻¹, 1.0·10⁻¹, 4.7·10⁻², 1.1·10⁻² for j = 2..5 at log 2; 9·10⁻³ … 4·10⁻⁴ at T = 1.2), so numerical rank is
full but the raw polynomial generators become ill-conditioned quickly.

## 3. Capture and Rayleigh bottom (NUMERICAL)

Table 3.1. Rayleigh bottom μ(V) = min a_T|_V, the distance ‖v_0 − Proj_V v_0‖ of the computed bottom eigenvector v_0 of
a_T on P_T to V, and the captured fraction f(V) = ‖Proj_V U_low‖²_F / dim U_low of the eigenspace U_low of eigenvalues
< 10⁻³. (Krylov: dimension j·d_T.)

T = log 2 (λ_A = 1.1·10⁻⁷, dim U_low = 2)

| V | dim | μ(V) | dist(v_0, V) | f(V) |
|---|---|---|---|---|
| K_1 = E_1 | 1 | 3.4·10⁻² | 0.62 | 0.31 |
| K_2 | 2 | 1.2·10⁻² | 0.60 | 0.32 |
| K_4 | 4 | 4.8·10⁻³ | 0.48 | 0.39 |
| K_8 | 8 | 3.5·10⁻³ | 0.19 | 0.48 |
| K_16 | 16 | 1.8·10⁻³ | 0.07 | 0.50 |
| E_4 | 4 | 2.3·10⁻³ | 0.051 | 0.98 |
| E_8 | 8 | 8.3·10⁻⁵ | 0.0071 | 1.00 |
| E_16 | 16 | 3.0·10⁻⁵ | 0.0056 | 1.00 |

T = ½log5 + 10⁻³ (λ_A = 3.1·10⁻¹², dim U_low = 4)

| V | dim | μ(V) | dist | f |
|---|---|---|---|---|
| K_1 | 1 | 4.7·10⁻² | 0.76 | 0.21 |
| K_4 | 4 | 3.3·10⁻³ | 0.70 | 0.25 |
| K_8 | 8 | 2.3·10⁻³ | 0.57 | 0.35 |
| K_16 | 16 | 1.3·10⁻³ | 0.39 | 0.44 |
| E_8 | 8 | 1.8·10⁻⁵ | 0.0083 | 0.99 |
| E_12 | 12 | 1.3·10⁻⁶ | 0.0044 | 1.00 |
| E_24 | 24 | 3.0·10⁻⁸ | 0.0022 | 1.00 |

(½log5 − 10⁻³ agrees to two digits.)

T = 0.9 (λ_A = 4.5·10⁻¹⁵, dim U_low = 6)

| V | dim | μ(V) | dist | f |
|---|---|---|---|---|
| K_1 | 2 | 1.7·10⁻² | 0.83 | 0.30 |
| K_4 | 8 | 2.9·10⁻³ | 0.82 | 0.34 |
| K_8 | 16 | 2.3·10⁻³ | 0.75 | 0.64 |
| K_16 | 32 | 1.6·10⁻³ | 0.47 | 0.89 |
| E_8 | 8 | 2.8·10⁻⁶ | 0.026 | 0.84 |
| E_16 | 16 | 1.6·10⁻⁹ | 0.0023 | 1.00 |
| E_24 | 24 | 2.6·10⁻¹¹ | 0.0016 | 1.00 |

T = 1.0 (|λ_A| ≤ 2·10⁻¹⁵, round-off; dim U_low = 9)

| V | dim | μ(V) | dist | f |
|---|---|---|---|---|
| K_1 | 2 | 1.7·10⁻² | 0.77 | 0.21 |
| K_4 | 8 | 1.6·10⁻³ | 0.75 | 0.25 |
| K_8 | 16 | 1.3·10⁻³ | 0.73 | 0.36 |
| K_16 | 32 | 4.4·10⁻⁴ | 0.70 | 0.58 |
| E_8 | 8 | 1.5·10⁻⁶ | 0.062 | 0.62 |
| E_16 | 16 | 3.2·10⁻¹¹ | 0.0028 | 0.96 |
| E_24 | 24 | 1.6·10⁻¹² | 0.0021 | 1.00 |

T = 1.2 (dim U_low = 16) and T = 1.4 (dim U_low = 26)

| V | dim (1.2) | μ (1.2) | f (1.2) | dim (1.4) | μ (1.4) | f (1.4) |
|---|---|---|---|---|---|---|
| K_1 | 3 | 6.1·10⁻⁵ | 0.18 | 4 | 2.8·10⁻⁵ | 0.15 |
| K_2 | 6 | 1.9·10⁻⁶ | 0.18 | 8 | 1.1·10⁻⁶ | 0.15 |
| K_4 | 12 | 6.5·10⁻⁷ | 0.21 | 16 | 2.1·10⁻⁷ | 0.18 |
| K_8 | 24 | 2.1·10⁻⁷ | 0.36 | 32 | 8.3·10⁻⁸ | 0.32 |
| K_16 | 48 | 8.3·10⁻⁹ | 0.67 | 64 | ≈ 0 (round-off) | 0.75 |
| E_8 | 8 | 7.3·10⁻⁸ | 0.47 | 8 | 1.2·10⁻⁸ | 0.30 |
| E_16 | 16 | 5.7·10⁻¹³ | 0.71 | 16 | 9.8·10⁻¹⁴ | 0.51 |
| E_24 | 24 | 2.4·10⁻¹⁴ | 0.84 | 24 | 3.8·10⁻¹⁵ | 0.67 |

Reading.
(i) The Krylov step K_1 → K_2 gains one to two orders in μ (the comb pushes the negative cone toward the near-null
cluster), then stalls: from j = 2 to j = 16 the bottom improves by less than one order at T ≤ 1.0 and the distance to
v_0 stays ≥ 0.4 at T ≥ ½log5. At equal dimension E_k is better by 2–9 orders in μ at every T. K_j does NOT reach the
ground state with dimension O(T); it does not reach it within dimension 64 ≈ 80% of the Galerkin space at T = 1.4
except by exhausting the space.
(ii) The principal cosines between K_j and U_low (computed, r5.py) are 0 to four digits for 2 ≤ j ≤ 5 at T ≥ ½log5:
some near-null direction is orthogonal to K_j. The comb-Krylov family is spread over the near-null cluster only
through f(K_j) ≈ 0.2–0.5, i.e. it sees part of every low direction and the whole of none.
(iii) E_k captures the cluster once k exceeds dim U_low by a margin (k ≈ 8 at log 2, 12 at ½log5, 16 at 0.9–1.0, > 32 at
1.2–1.4). The required k tracks dim U_low = 2, 4, 6, 9, 16, 26, which grows faster than d_T ≈ 4T; this is the
arena phenomenon (many archimedean modes compete) seen at the Galerkin level, NUMERICAL.

## 4. Schur complement onto V^⊥ (NUMERICAL; the identity is PROVED)

For V ⊂ P_T finite-dimensional, write a_T on V ⊕ V^⊥ (complement inside the Galerkin P_T) as [[A_V, B],[Bᵀ, C]]. If
C ≻ 0, then a_T ⪰ 0 iff S_V := A_V − B C⁻¹ Bᵀ ⪰ 0, and λ_min(S_V) has the sign of λ_A (standard; PROVED). The
coupling cost is κ(V) := μ(V) − λ_min(S_V). Quantities: c(V) = λ_min(C) (coercivity of the complement), ‖B‖, κ(V).

Table 4.1 (Λ, selected rows; full output r5.out).

| T | V | dim | c(V) | ‖B‖ | λ_min(S_V) | κ(V) ≈ μ(V) − λ_A |
|---|---|---|---|---|---|---|
| log 2 | K_1..K_5 | 1..5 | 1.29·10⁻⁵ (= λ_2) for all j | 0.17 → 1.13 | 1.4–1.8·10⁻⁷ | 3.4·10⁻² → 4.8·10⁻³ |
| log 2 | E_8 / E_24 | 8 / 24 | 0.74 / 1.56 | 0.35 / 0.58 | 1.11·10⁻⁷ | 8.3·10⁻⁵ / 2.4·10⁻⁵ |
| ½log5+10⁻³ | K_1..K_5 | 1..5 | 6.5·10⁻¹⁰ (= λ_2) for all j | 0.25 → 0.99 | 5–7·10⁻¹² | 4.7·10⁻² → 3.1·10⁻³ |
| ½log5+10⁻³ | E_8 / E_24 | 8 / 24 | 0.59 / 1.19 | 0.55 / 0.47 | 3.09·10⁻¹² | 1.8·10⁻⁵ / 3.0·10⁻⁸ |
| 0.9 | K_1 / K_3 / K_5 | 2 / 6 / 10 | 6·10⁻¹² / 2.8·10⁻⁸ / 9.1·10⁻⁴ | 0.27 / 1.06 / 1.20 | ≈ 1.4·10⁻¹⁴ | 1.7·10⁻² / 3.0·10⁻³ / 2.4·10⁻³ |
| 0.9 | E_12 / E_24 | 12 / 24 | 0.49 / 0.74 | 0.83 / 0.85 | ≈ 4.5·10⁻¹⁵ | 1.9·10⁻⁷ / 2.6·10⁻¹¹ |
| 1.0 | K_1 / K_5 | 2 / 10 | 5·10⁻¹⁵ / 9.8·10⁻⁸ | 0.23 / 1.09 | round-off | 1.7·10⁻² / 1.4·10⁻³ |
| 1.2 | K_1 / K_5 | 3 / 15 | ≈ 10⁻¹⁴ | 0.31 / 1.50 | round-off | 6.1·10⁻⁵ / 6.2·10⁻⁷ |
| 1.4 | K_1 / K_5 | 4 / 20 | ≈ 10⁻¹⁴ | 0.33 / 1.14 | round-off | 2.8·10⁻⁵ / 1.9·10⁻⁷ |

ROUND_004_A next step: the coupling cost for E_k at T = 1.0 and 1.2 as a function of k.

| k | 2 | 4 | 6 | 8 | 12 | 16 | 24 |
|---|---|---|---|---|---|---|---|
| κ(E_k), T = 1.0 | 1.7·10⁻² | 1.5·10⁻⁴ | 1.8·10⁻⁵ | 1.5·10⁻⁶ | 1.6·10⁻⁸ | 3.2·10⁻¹¹ | 1.6·10⁻¹² |
| c(E_k), T = 1.0 | 5·10⁻¹⁵ | 7·10⁻¹³ | 1.1·10⁻⁸ | 7.2·10⁻⁵ | 1.5·10⁻² | 0.26 | 0.62 |
| κ(E_k), T = 1.2 | 1.8·10⁻² | 6.1·10⁻⁵ | 6.7·10⁻⁶ | 7.3·10⁻⁸ | 5.5·10⁻¹¹ | 5.7·10⁻¹³ | 2.4·10⁻¹⁴ |
| c(E_k), T = 1.2 | 7·10⁻¹⁶ | 5·10⁻¹⁵ | 1·10⁻¹⁴ | 1.5·10⁻¹⁴ | 6·10⁻¹¹ | 8.5·10⁻⁶ | 6.4·10⁻³ |

Reading.
(i) κ(E_k) decays roughly geometrically in k, about one decade per unit of k (T = 1.0: 1.5·10⁻⁴ → 3·10⁻¹¹ for k = 4 → 16),
NOT like α_{k+1}^{-1}‖B‖² (that quantity is ≈ 0.3–1, since ‖B‖ does not decay: 0.37 → 0.91). The decay of κ is the
approximation of the low cluster by archimedean modes, not a smallness of the coupling block.
(ii) The complement is coercive with a usable floor only once V contains the whole near-null cluster: c(E_k) jumps
from round-off to 0.26 at k = 16 for T = 1.0 and is still 6·10⁻³ at k = 24 for T = 1.2 (≈ 10⁻⁸ at T = 1.4). For every
Krylov space tested, c(K_j) is at the level of λ_2 (≤ 10⁻⁷ for T ≥ ½log5, up to j = 5): the Schur route on K_j has no
complement coercivity at all. R3(i) — PROVED coercivity of a_T on E_T^⊥ — is therefore unavailable for K_j, and
available for E_k only at k ≥ dim U_low + O(1).
(iii) The Schur identity is exact, so λ_min(S_V) reproduces λ_A whenever c(V) > 0 (checked to 2–3 digits at log 2,
½log5, 0.9); nothing is gained: S_V carries the full margin problem, and its computation requires C⁻¹ on the near-null
cluster.

## 5. Falsifier behaviour at T = 1.0 (NUMERICAL)

Here the Krylov space is built from the falsifier's own comb (Π replaced by cΠ, by Π_{a_3}, by Π + 0.1·v-change at 2),
Neg_T being Λ-independent.

Table 5.1. μ(K_j) and μ(E_k) against λ_A for the falsifier.

| comb | λ_A | K_1 | K_2 | K_4 | K_8 | K_12 | K_16 | E_4 | E_8 | E_16 |
|---|---|---|---|---|---|---|---|---|---|---|
| Λ | ≈ 0 | +1.7·10⁻² | +3.5·10⁻³ | +1.6·10⁻³ | +1.3·10⁻³ | +1.2·10⁻³ | +4.4·10⁻⁴ | +1.5·10⁻⁴ | +1.5·10⁻⁶ | +3·10⁻¹¹ |
| 0.9Λ | −5.0·10⁻² | −2.6·10⁻² | −4.8·10⁻² | −4.8·10⁻² | −4.9·10⁻² | −4.9·10⁻² | −4.9·10⁻² | −3.9·10⁻² | −4.6·10⁻² | −4.9·10⁻² |
| 1.1Λ | −1.5·10⁻¹ | +4.1·10⁻² | +2.5·10⁻² | +2.1·10⁻² | +2.1·10⁻² | −2.6·10⁻² | −6.7·10⁻² | −6.2·10⁻³ | −4.7·10⁻² | −1.1·10⁻¹ |
| a_3 (no 2) | −5.3·10⁻¹ | −4.8·10⁻¹ | −5.2·10⁻¹ | −5.2·10⁻¹ | −5.2·10⁻¹ | −5.3·10⁻¹ | −5.3·10⁻¹ | −5.2·10⁻¹ | −5.3·10⁻¹ | −5.3·10⁻¹ |
| Λ + 0.1·1₂ | −9.7·10⁻² | +1.1·10⁻¹ | +8.6·10⁻² | +8.4·10⁻² | +8.2·10⁻² | +5.8·10⁻² | +3.6·10⁻³ | −5.3·10⁻² | −8.7·10⁻² | −9.4·10⁻² |

Reading.
(i) Falsifiers that weaken the comb (0.9Λ, a_3) are detected at j = 1: their negative direction lies in the archimedean
negative cone itself (f(K_1) = 0.99 for 0.9Λ). This is comb-generic and carries no Λ-specific information.
(ii) Falsifiers that strengthen the comb (1.1Λ, Λ + 0.1·1₂) are NOT detected by K_j for j ≤ 8 (1.1Λ: first negative at
j = 12, dim 24; Λ + 0.1·1₂: still positive at j = 16, dim 32), while E_4 already detects both. Their negative
directions are orthogonal to K_1 to three digits (dist(v_0, K_1) = 1.000 and 0.999): the over-strong comb creates
negativity at high archimedean frequency, outside the comb's orbit of the negative cone.
(iii) So the K_j-bottom does not turn negative "exactly when λ_A does": as a necessary condition a_T|_{K_j} ⪰ 0 it is
weaker than the plane condition on E_k of equal dimension and it fails falsifier (a) for c > 1 and (d) at j ≤ 8. As a
capture device it fails at Λ itself (§3). Neither failure is a precision artefact: the margins in Table 5.1 are 10⁻²–10⁻¹.

## Result

NO-GO with class (NUMERICAL, not a theorem): the comb-Krylov family K_j = span{(PΠP)^i Neg_T : i < j} grown from the
archimedean negative cone does not capture the minimiser of a_T on P_T with dimension O(T) — nor with dimension up to 64
of the 78-dimensional Galerkin P_T at T = 1.4 — and its complement is never coercive (c(K_j) ≈ λ_2) at the tested j;
as a necessary condition it misses the comb-strengthening falsifiers (1.1Λ; Λ + 0.1·1₂) that E_4 already detects.
PROVED pieces: the bookkeeping of §1.

## What was proved

- Proposition 1.1: exact formula (1.2)–(1.3) for ⟨e, Π²e′⟩ and ⟨e, ΠPΠe′⟩ as double sums over m, n ∈ N_T of v_m v_n times
  window correlations at the shifts ±log(n/m) (windows of length 2T − max(u_m, u_n)) and ±log(mn) (windows of length
  2T − u_m − u_n, present only when mn < e^{2T}), with the Tate correction a product of two single-shift exponential
  moments.
- Proposition 1.2: K_j is spanned by vectors whose sine coefficients are homogeneous polynomials in v of degree i < j,
  with explicit v-independent coefficients; the Gram matrix of a_T on these generators is polynomial of degree ≤ 2j − 1.
- The Schur identity of §4 (standard).

## What failed and why

Against the specification:
- R1 (dim → ∞): satisfied formally (dim K_j = j·d_T, d_T ≈ 4T − 2, Table 2.1), but the data show that dimension
  O(T)·j with j ≤ 16 does not reach the ground state: μ(K_j) stalls at 10⁻³ (T ≤ 1.0) and 10⁻⁷–10⁻⁸ (T = 1.2, 1.4),
  2–9 decades above μ(E_k) at equal dimension.
- R2 (non-linear in v, Λ-specific): satisfied in form (Prop. 1.2; the first non-linear level is exactly the n/m and
  mn < e^{2T} interplay of Prop. 1.1), but the non-linear content does not steer K_j toward the near-null cluster: the
  principal cosines with U_low vanish for 2 ≤ j ≤ 5 and the captured fraction stays ≤ 0.5 at T ≥ ½log5 for j ≤ 8.
- R3 (exact reduction or margin with coercive complement): fails for K_j — c(K_j) is the second eigenvalue of a_T
  (≤ 10⁻⁷ beyond ½log5), so no coercivity on K_j^⊥ exists to be proved; κ(K_j) ≈ 10⁻³ ≫ λ_A. For the comparison family,
  κ(E_k) decays about one decade per unit k and c(E_k) becomes O(1) only when k exceeds the size of the near-null
  cluster dim U_low = 2, 4, 6, 9, 16, 26 (T = log 2 … 1.4), the Galerkin shadow of the arena count.
- R4 (comb-first escapes the arena count): NOT supported. The near-null cluster that must be captured is spanned by
  archimedean modes at the arena frequencies; Π applied to the low archimedean cone reaches them only partially and
  slowly, so the comb-first family pays at least the same dimension as the archimedean one, and in the data more.
  Strong-comb falsifiers produce negative directions orthogonal to K_1, confirming that the comb's orbit of Neg_T is
  not where the competition happens.
- Precision limit: at T ≥ 1.0 the computed λ_A is at round-off and U_low is a cluster; no statement about the individual
  ground vector is made there.

## Next concrete step

Replace the generator: instead of Π acting on Neg_T (low archimedean modes), build the family from the near-null
cluster's own mechanism — the comb responses Π e_k at the arena frequencies (third candidate of OBJECT_SPEC_001), i.e.
K′_j = span{(PΠP)^i e_k : k ∈ arena band, i < j}, and test whether j = 2 already captures U_low with dim ≈ dim U_low;
if so, the degree-2 entries (1.2) at ratios n/m and products mn are the explicit matrix on which the margin must be
decided. Before that, re-run the T ≥ 1.0 rows in extended precision (mpmath, N = 120) so that U_low and λ_A are resolved
rather than at round-off.
