# Round 5, memo E: the Krylov family grown from the arena band

Object. On P_T (two Tate conditions), with Arch_T := P·Arch·P and Π_T := P·Π·P (STATEMENT_001, ROUND_005_B §1), put

  A_T = Σ_{n∈N_T} v_n                                 (the bound ‖Π_T‖ ≤ A_T, Paper 47 prop:coer-prime),
  Band(t) = span of the eigenvectors of Arch_T with eigenvalue ≤ t,
  K′_j(t) = span{Π_T^i e : e ∈ Band(t), 0 ≤ i < j},

and test two thresholds: t = A_T (the arena band as specified) and t = λ_max(Π_T) (the sharp arena band: the
largest value the comb form actually attains on P_T). E_k = span of the k lowest eigenvectors of Arch_T (both
parities), U_δ = spectral subspace of a_T for eigenvalues < δ (the near-null cluster), m_δ(T) = dim U_δ.

## Corpus check

- ROUTES-TRIED-INDEX: P211-5B (README, phase-211 block) is the Krylov family from Neg_T; G8D-R164_502c (L5) is the
  Krylov space of the symbol σ_T. The present generator differs from both: the starting block is the arena band
  (all archimedean modes the comb can lower to zero), not Neg_T (which has dimension ≈ 4T − 2 and was shown in 5B to
  be orthogonal to part of U_δ), and not the symbol. The recorded failure of 5B (principal cosines 0 with U_δ) is a
  failure of the starting block; this memo changes exactly the starting block. The symbol obstruction of R164_502c
  concerns positivity of σ_T, not used here.
- Paper 47 thm:arena / cor:arena (CITED): even modes with archimedean eigenvalue ≤ A_T compete; their number is
  ≥ exp(4e^T(1+o(1))). Theorem (b) of §3 below is the Weyl-type upper count that matches this band.
- Grid R162_2300: "Krylov" only phase-164 symbol item; "arena" only thm:arena tools (P47). No cluster-count entry.

Numerical set-up (NUMERICAL throughout §1–2, §4): same as ROUND_005_B (N = 80 sines, 78-dimensional Galerkin P_T,
saved Arch matrices; Π exact by Gauss–Legendre; block Krylov with re-orthogonalisation, tolerance 10⁻¹⁰). Capture of
U_δ by V means: the smallest principal cosine between U_δ and V is ≥ 0.99 (set to 0 if dim V < dim U_δ).
Precision: λ_A is resolved for T ≤ 0.9 (1.1·10⁻⁷, 3.8·10⁻¹², 3.1·10⁻¹², 4.5·10⁻¹⁵ at log 2, ½log5 ∓ 10⁻³, 0.9) and
NOT at T = 1.0, 1.2 (round-off, |λ| ≤ 10⁻¹⁴): rows at 1.0, 1.2 are flagged UNRESOLVED for λ_A and for the order of
the cluster eigenvalues below 10⁻¹³; the cluster COUNT at δ = 10⁻³ is resolved there. Extended precision was not
used: the Arch matrix itself comes from a double-precision quadrature, so re-diagonalising it in mpmath would not
resolve anything. Truncation check (N = 40 vs 80): m_{10⁻³} = 2, 4, 4, 6, 9 identical at log 2 … 1.0; at T = 1.2
it is 14 (N = 40) vs 16 (N = 80), so the T = 1.2 count is not converged in N.

## 1. The arena band and its Krylov spaces (NUMERICAL)

Table 1.1. Sizes. N*(T) is the arena count of Paper 47 cor:arena (≥ exp(4e^T(1+o(1))), doubly exponential); the
Galerkin space has only 78 dimensions, so dim Band(A_T) is capped at 78.

| T | A_T | e^{A_T} | dim Band(A_T) (of 78) | λ_max(Π_T) | dim Band(λ_max Π_T) | d_T = #neg Arch | m_{10⁻³} | m_{10⁻⁶} |
|---|---|---|---|---|---|---|---|---|
| log 2 | 2.249 | 9.5 | 24 | 0.901 | 5 | 1 | 2 | 1 |
| ½log5 − 10⁻³ | 2.942 | 19.0 | 59 | 1.218 | 9 | 1 | 4 | 3 |
| ½log5 + 10⁻³ | 4.381 | 80.0 | 78 (saturated) | 1.219 | 9 | 1 | 4 | 3 |
| 0.8 | 2.942 | 19.0 | 58 | 1.218 | 9 | 1 | 4 | 3 |
| 0.9 | 4.381 | 80.0 | 78 (saturated) | 1.516 | 14 | 2 | 6 | 5 |
| 1.0 (unresolved λ_A) | 5.852 | 348 | 78 (saturated) | 1.730 | 21 | 2 | 9 | 7 |
| 1.2 (unresolved λ_A) | 8.521 | 5019 | 78 (saturated) | 2.057 | 36 | 3 | 16 | 14 |

Reading. The band at the threshold A_T is the whole Galerkin space from ½log5 on: as a starting block it is not a
reduction at all (j = 1 already equals P_T^{(N)}, and every K′_j(A_T) = P_T^{(N)}). The meaningful band is the
sharp one, t = λ_max(Π_T), whose dimension n_P(T) = 5, 9, 9, 14, 21, 36 is moderate. Note A_T/λ_max(Π_T) ≈ 2.5–4:
the trivial bound ‖Π_T‖ ≤ A_T loses a factor that, through the logarithmic growth of the Arch eigenvalues, becomes
a factor e^{A_T − λ_max} in the band count.

Table 1.2. Capture by the sharp band and its Krylov spaces, against E_k at EQUAL dimension. μ = Rayleigh bottom of
a_T on V, cos = smallest principal cosine with U_{10⁻³}, c = λ_min of a_T on V^⊥ (complement coercivity), S =
λ_min of the exact Schur complement (equals λ_A whenever c > 0; checked).

| T | V | dim | μ(V) | cos | c(V) | μ(E_dim) | cos(E_dim) | c(E_dim) |
|---|---|---|---|---|---|---|---|---|
| log 2 | K′_1 = Band | 5 | 3.7·10⁻⁴ | 0.981 | 0.42 | (same space) | | |
| log 2 | K′_2 | 10 | 2.5·10⁻⁵ | 0.998 | 0.91 | 6.2·10⁻⁵ | 1.000 | 0.75 |
| log 2 | K′_3 | 15 | 2.1·10⁻⁶ | 0.999 | 0.99 | 3.0·10⁻⁵ | 1.000 | 1.19 |
| ½log5+10⁻³ | K′_1 | 9 | 5.2·10⁻⁶ | 0.988 | 0.59 | (same) | | |
| ½log5+10⁻³ | K′_2 | 18 | 4.3·10⁻⁹ | 1.000 | 0.87 | 1.0·10⁻⁷ | 1.000 | 0.86 |
| ½log5+10⁻³ | K′_3 | 27 | 3.7·10⁻⁹ | 1.000 | 1.25 | 2.7·10⁻⁸ | 1.000 | 1.19 |
| 0.9 | K′_1 | 14 | 2.3·10⁻⁸ | 0.998 | 0.60 | (same) | | |
| 0.9 | K′_2 | 28 | 6.9·10⁻¹¹ | 1.000 | 0.92 | 4.7·10⁻¹² | 1.000 | 0.93 |
| 0.9 | K′_3 | 42 | 1.6·10⁻¹² | 1.000 | 1.39 | 3.9·10⁻¹² | 1.000 | 1.25 |
| 1.0 (unres.) | K′_1 | 21 | 3.0·10⁻¹² | 0.991 | 0.62 | (same) | | |
| 1.0 (unres.) | K′_2 | 42 | round-off | 1.000 | 0.94 | 1.5·10⁻¹³ | 1.000 | 1.12 |
| 1.2 (unres.) | K′_1 | 36 | round-off | 0.924 | 0.40 | (same) | | |
| 1.2 (unres.) | K′_2 | 70 | round-off | 1.000 | 0.013 | round-off | 1.000 | 1.90 |

(½log5 − 10⁻³ agrees with ½log5 + 10⁻³ to two digits; full output r5e.out.) For contrast, the Neg_T-Krylov family of
ROUND_005_B has cos = 0 (some cluster direction orthogonal) at every j ≤ 3 and every T, and first captures U_{10⁻³}
only at dimension 66–78 (≥ 85 % of the Galerkin space) for T ≥ 0.9; it never captures at log 2, ½log5 within 39 steps.

Table 1.3. Smallest dimension at which a family captures U_{10⁻³} (cos ≥ 0.99).

| T | m_{10⁻³} | E_k | K′_2(E_m) (smallest m, dim 2m) | Neg_T-Krylov | sharp band n_P |
|---|---|---|---|---|---|
| log 2 | 2 | 6 | m = 4, dim 8 | none ≤ 78 | 5 (cos 0.981) |
| ½log5 ± 10⁻³ | 4 | 10 | m = 8, dim 16 | none ≤ 78 | 9 (cos 0.988) |
| 0.8 | 4 | 10 | m = 6, dim 12 | none ≤ 78 | 9 |
| 0.9 | 6 | 14 | m = 9, dim 18 | 66 | 14 (cos 0.998) |
| 1.0 (unres.) | 9 | 21 | m = 14, dim 28 | 72 | 21 (cos 0.991) |
| 1.2 (unres., N not converged) | 16 | 42 | m = 23, dim 46 | 78 | 36 (cos 0.924) |

Reading.
(i) The arena band (sharp threshold) captures the cluster at j = 1, by itself: K′_1 = E_{n_P}, with cosine ≥ 0.98
at T ≤ 1.0, and its complement is coercive with an O(1) floor (c = 0.40–0.62). This is what ROUND_005_B lacked:
replacing Neg_T by the sharp arena band moves c(V) from λ_2 (≤ 10⁻⁷) to ≈ 0.6.
(ii) The Krylov step j = 2 doubles the dimension and improves μ by one to three decades; at equal dimension it beats
E_{2n_P} in μ at log 2 and ½log5 (by 2.5× and 25×) and loses at 0.9 (15×). The minimal-dimension capture by K′_2
(m lowest modes + their Π-images) needs dimension 2m ≥ E_k's capture dimension at every T (8 vs 6, 16 vs 10, 18 vs
14, 28 vs 21, 46 vs 42). The comb step adds NO dimension saving over the archimedean ordering; "j = 2 captures at
dimension close to the cluster size" is FALSE (dimension 8, 16, 18, 28, 46 vs m = 2, 4, 6, 9, 16).
(iii) Every family that captures does so at dimension ≈ n_P(T) ≈ 2.3·m(T): the capture dimension is set by the
archimedean count below λ_max(Π_T), not by the comb's algebra. Theorem (b) below explains the upper side.

## 2. Growth of the cluster and of the capture dimension (NUMERICAL)

Table 2.1. The cluster and its sign. All listed eigenvalues of a_T below 10⁻³ (N = 80).

| T | m_{10⁻³} | eigenvalues < 10⁻³ | sign |
|---|---|---|---|
| log 2 | 2 | 1.1·10⁻⁷, 1.3·10⁻⁵ | all > 0 (resolved) |
| ½log5 − 10⁻³ | 4 | 3.8·10⁻¹², 7.9·10⁻¹⁰, 3.9·10⁻⁷, 4.1·10⁻⁵ | all > 0 (resolved) |
| ½log5 + 10⁻³ | 4 | 3.1·10⁻¹², 6.5·10⁻¹⁰, 3.2·10⁻⁷, 3.5·10⁻⁵ | all > 0 (resolved) |
| 0.8 | 4 | 6.0·10⁻¹², 1.1·10⁻⁹, 6.1·10⁻⁷, 5.3·10⁻⁵ | all > 0 (resolved; λ_A = 6.0·10⁻¹²) |
| 0.9 | 6 | 4.5·10⁻¹⁵, 2.3·10⁻¹⁴, 1.3·10⁻¹¹, 2.2·10⁻⁹, 4.1·10⁻⁷, 3.2·10⁻⁵ | all > 0; the lowest two are at the edge of resolution |
| 1.0 | 9 | four values in [−1.2, 1.5]·10⁻¹⁵ … 1.5·10⁻¹⁴, then 1.7·10⁻¹², 2.2·10⁻¹⁰, 4.3·10⁻⁸, 3.9·10⁻⁶, 2.4·10⁻⁴ | lowest four UNRESOLVED (round-off); upper five > 0 |
| 1.2 | 16 | eleven values in [−9.6·10⁻¹⁵, 9.8·10⁻¹⁴], then 1.5·10⁻¹¹, 1.0·10⁻⁹, 9.3·10⁻⁸, 5.0·10⁻⁶, 2.4·10⁻⁴ | lowest eleven UNRESOLVED; upper five > 0 |

Structure (NUMERICAL): the resolved part of the cluster is a geometric ladder, consecutive ratios ≈ 10²–10³, the
top rung always ≈ 2–4·10⁻⁵ … 2.4·10⁻⁴; each step in T adds rungs at the bottom. The sign of every RESOLVED cluster
eigenvalue is positive; no negative eigenvalue is resolved anywhere.

Table 2.2. Fits over T ∈ {log 2, ½log5, 0.9, 1.0, 1.2} (T = 1.2 not converged in N; the 0.8 row is listed but its
count equals ½log5's, see Table 1.1).

| quantity | values | 4T | e^{A_T} | least-squares log-linear fit |
|---|---|---|---|---|
| m_{10⁻³}(T) | 2, 4, 6, 9, 16 | 2.8, 3.2, 3.6, 4.0, 4.8 | 9.5, 80, 80, 348, 5019 | m ≈ 0.145·e^{4.0T} (residuals ≤ 0.17 in log); ratio m/e^{4T} = 0.125, 0.160, 0.164, 0.165, 0.132 |
| capture dim, E_k | 6, 10, 14, 21, 42 | | | ≈ 2.3·m |
| sharp band n_P(T) | 5, 9, 14, 21, 36 | | | n_P ≈ 0.39·e^{3.9T}; n_P/(T e^{λ_max(Π_T)}) = 2.9, 3.3, 3.4, 3.7, 3.8 |

Reading (NUMERICAL; answers task (2)). The cluster size grows exponentially in T at rate ≈ 4 (m ≈ 0.15 e^{4T}, i.e.
like the square of the contact range e^{2T}); it does not grow like 4T (linear: ratio m/4T goes 0.7 → 3.3), and it
does not grow like e^{A_T} (A_T is a step function of the prime powers; e^{A_T} jumps by 4× across ½log5 where m is
unchanged, and is 300× m at T = 1.2). The capture dimension of every tested family tracks m (factor ≈ 2.3), and the
sharp band count n_P tracks T e^{λ_max(Π_T)} — the Weyl count of the archimedean spectrum below the actual top of the
comb form, not below A_T. On the five points, rate-4 exponential and "T·e^{λ_max(Π_T)}" are indistinguishable; both
are single exponentials in T, so on this range the data do NOT show the doubly exponential arena count of
cor:arena, because λ_max(Π_T) ≪ A_T (0.90 vs 2.25 at log 2, 2.06 vs 8.52 at 1.2). Whether λ_max(Π_T) grows like A_T
asymptotically (which would restore the doubly exponential count) is OPEN.

## 3. What can be proved about the cluster size

Let α_1 ≤ α_2 ≤ … be the eigenvalues of Arch_T on P_T (discrete: compact resolvent, CITED Paper 47 prop:nodes),
λ_1 ≤ λ_2 ≤ … those of a_T on P_T, m_δ(T) = #{k : λ_k < δ}, N_Arch(s) = #{k : α_k < s}, and
π_+ = λ_max(Π_T) = sup_{F∈P_T, ‖F‖=1} ⟨F, ΠF⟩, π_− = −inf_{F∈P_T, ‖F‖=1} ⟨F, ΠF⟩.

Lemma 3.0 (PROVED). π_± ≤ A_T.
Proof. ⟨F, ΠF⟩ = Σ_{n∈N_T} v_n c_F(u_n) with c_F(u) = ∫_{−T}^{T−u} F(x)F(x+u)dx (ROUND_005_B (1.1)), and
|c_F(u)| ≤ ‖F‖² by Cauchy–Schwarz; v_n > 0. ∎

Theorem 3.1 (two-sided Weyl count; PROVED). For every δ ∈ ℝ and T > 0,

  N_Arch(δ − π_−) ≤ m_δ(T) ≤ N_Arch(δ + π_+) ≤ N_Arch(δ + A_T).

The same inequalities hold for every Galerkin compression (with α_k, λ_k, π_± of the compression).
Proof. a_T(F) = Arch_T(F) − ⟨F, ΠF⟩ on the form domain, with −π_−‖F‖² ≤ ⟨F, ΠF⟩ ≤ π_+‖F‖². Courant–Fischer for
semibounded forms with discrete spectrum: λ_k = sup_{codim W ≤ k−1} inf_{F∈W, ‖F‖=1} a_T(F). Since
Arch_T(F) − π_+ ≤ a_T(F) ≤ Arch_T(F) + π_− pointwise, λ_k ∈ [α_k − π_+, α_k + π_−]. Hence λ_k < δ ⇒ α_k < δ + π_+
(upper bound), and α_k < δ − π_− ⇒ λ_k < δ (lower bound). The last inequality is Lemma 3.0 and monotonicity of
N_Arch. Compression: the same argument in the finite space. ∎

This is task (3)(b): the cluster is at most the archimedean count below δ + λ_max(Π_T), a fortiori below δ + A_T
(the arena band). Numerically (δ = 10⁻³): upper bound N_Arch(δ + π_+) = 5, 9, 14, 21, 36 against m = 2, 4, 6, 9, 16
— sharp to a factor ≈ 2.3 uniformly; the A_T version gives 24, 59 (and ≥ 78 = the whole Galerkin space from
½log5 on), useless in practice.

Task (3)(a), the lower bound, is PROVED in the form N_Arch(δ − π_−) ≤ m_δ, but it is VACUOUS at every tested T:
π_− = 0.90, 1.03, 1.36, 1.65, 1.83 exceeds |α_1| = 0.15, 0.31, 0.42, 0.53, 0.73, so N_Arch(δ − π_−) = 0.

Proposition 3.2 (no archimedean lower count; PROVED). Any lower bound of the form m_δ ≥ N_Arch(δ − θ) obtained from
a pointwise comparison a_T ≤ Arch_T + θ requires θ ≥ π_−; and if π_− > δ − α_1 it is zero. Complementary check
(NUMERICAL): the test-space bound "λ_k ≤ max of a_T on E_k" from archimedean planes gives
m_{10⁻³} ≥ 0 only (NUMERICAL: a_T(e) ≥ 1.7·10⁻² > 10⁻³ for every single archimedean eigenvector e among the lowest 40, at every T; so already k = 1 fails).
Proof of the first sentence. If a_T ≤ Arch_T + θ as forms then, at the minimiser of ⟨F,ΠF⟩ over P_T,
−⟨F,ΠF⟩ = π_− ≤ θ. If π_− > δ − α_1 then δ − θ < α_1, so N_Arch(δ − θ) = 0. ∎

Reading. The cluster is not counted from below by archimedean modes: its members are cancellation states, in which
Arch_T and Π_T are both of size ≈ α_k ≈ 0.1–2 and nearly equal. Its size is controlled from above (Theorem 3.1) and
measured numerically (≈ 0.15 e^{4T}), with no proved lower bound beyond m_δ ≥ 1 for δ > λ_A.

## 4. Falsifiers at T = 0.9 (NUMERICAL)

Smallest dimension at which a_T|_V becomes negative (necessary-condition detection). The sharp band uses each
falsifier's own λ_max(Π_T).

| comb | λ_A | E_k | K′_2(E_m) (dim 2m) | Neg_T-Krylov | sharp band, j = 1: dim, μ | sharp band, j = 2: dim, μ |
|---|---|---|---|---|---|---|
| Λ | +4.5·10⁻¹⁵ | none | none | none | 14, +2.3·10⁻⁸ | 28, +6.9·10⁻¹¹ |
| 1.1Λ | −1.12·10⁻¹ | 4 | 6 | 26 | 17, −1.00·10⁻¹ | 34, −1.12·10⁻¹ |
| Λ + 0.1·1₂ | −9.17·10⁻² | 3 | 6 | 28 | 16, −8.99·10⁻² | 32, −9.16·10⁻² |
| 0.9Λ | −3.86·10⁻² | 1 | 2 | 2 | 12, −3.50·10⁻² | 24, −3.85·10⁻² |
| a_3 (2 deleted) | −5.26·10⁻¹ | 1 | 2 | 2 | 9, −5.24·10⁻¹ | 18, −5.26·10⁻¹ |

Reading. Every falsifier is detected by E_k at dimension ≤ 4 and by K′_2(E_m) at dimension ≤ 6; the sharp band
detects all four at j = 1 with ≥ 89 % of the true negative value. The Neg_T-Krylov family of ROUND_005_B misses the
comb-strengthening falsifiers until dimension 26–28. No sign step is made in this memo, so the falsifier test of
rule 4 is applied to the capture device only: as a necessary condition, a_T|_V ⪰ 0 on the sharp band is as good a
detector as E_k. But it is not a sign carrier: K′_1 = E_{n_P} depends on Λ only through the single number
λ_max(Π_T), so a margin on it is killed by ROUND_004_A Proposition B (it survives every perturbation that leaves
n_P unchanged and changes λ_A by less than the margin).

(The T = 0.8 row: λ_A = 6.0·10⁻¹², cluster 6.0·10⁻¹², 1.1·10⁻⁹, 6.1·10⁻⁷, 5.3·10⁻⁵, sharp band 9 with cos 0.986,
c = 0.62; K′_2 of the band: μ = 3.2·10⁻⁹ vs μ(E_18) = 1.3·10⁻⁷. Same picture as ½log5.)

## Result

PIVOT with reason (NUMERICAL structure test; two PROVED pieces). The Krylov family grown from the arena band does
not do what the next step of ROUND_005_B hoped: with the band at threshold A_T the starting block is already the
whole Galerkin space (nothing to test), and with the sharp threshold λ_max(Π_T) the band captures the cluster by
itself at j = 1 — but it is then an archimedean plane E_{n_P}, Λ-dependent only through one scalar, and the comb step
j = 2 gives no dimension saving over the archimedean ordering at equal dimension.

What the data say about the specification:
- R1. Holds and is quantified: the cluster to be captured has m_{10⁻³}(T) = 2, 4, 4, 4, 6, 9, 16 at T = log 2,
  ½log5 ∓ 10⁻³, 0.8, 0.9, 1.0, 1.2, fit m ≈ 0.15 e^{4T}; every capturing family needs dimension ≈ 2.3·m.
- R2. Not met by the capturing family: K′_1 = E_{n_P} is Λ-free up to n_P; the Λ-non-linear K′_2 is no better than
  E_{2m} (better μ by 2.5–25× at log 2, 0.8, ½log5; worse by 15× at 0.9).
- R3. Partly met in the sense of R3(i) structure: on the sharp band the complement IS coercive (c = 0.40–0.62 at all
  T ≤ 1.2; the Schur complement reproduces λ_A to three digits at T ≤ 0.9); the margin problem is moved intact into
  the n_P × n_P Schur complement, which requires C⁻¹ on the complement. The capture precision at j = 1 (μ − λ_A from
  3.7·10⁻⁴ at log 2 to 3·10⁻¹² at 1.0) is far from the R3 target λ_A ≤ 4·10⁹ T e^{−15.449T} only in the sense that μ
  is the bottom on V, not λ_A; the Schur route is exact once c > 0.
- R4. The comb-first escape is not supported: the capture dimension is set by the archimedean count below
  λ_max(Π_T) (Theorem 3.1 upper side, sharp to ≈ 2.3), and comb iteration does not reduce it. The new information is
  that on T ≤ 1.2 this count is single-exponential (≈ e^{4T}), not e^{A_T}: the relevant threshold is λ_max(Π_T),
  not A_T, and λ_max(Π_T)/A_T = 0.40, 0.41, 0.28, 0.35, 0.30, 0.24 decreases.

## What was proved

- Lemma 3.0: λ_max(Π_T), −λ_min(Π_T) ≤ A_T on P_T.
- Theorem 3.1 (two-sided Weyl count): N_Arch(δ − π_−) ≤ m_δ(T) ≤ N_Arch(δ + λ_max(Π_T)) ≤ N_Arch(δ + A_T), on P_T
  and on every Galerkin compression. This is (3)(b): the cluster is at most the arena count; the sharp form is the
  count below λ_max(Π_T).
- Proposition 3.2: lower counts from a pointwise archimedean comparison are zero as soon as π_− > δ − α_1 (true at
  every tested T); (3)(a) holds only in this vacuous form.

## What failed and why

- "j = 2 captures at dimension close to the cluster size": FALSE. Minimal capture by K′_2(E_m) needs dimension
  8, 12, 16, 18, 28, 46 for m = 2, 4, 4, 6, 9, 16; E_k needs 6, 10, 10, 14, 21, 42.
- The arena band at A_T saturates the 78-dimensional Galerkin space from T = ½log5 on (24 and 58–59 of 78 below):
  the trivial bound ‖Π_T‖ ≤ A_T overshoots λ_max(Π_T) by a factor 2.5–4, inflating the band exponentially.
- Lower count for the cluster: no archimedean test space has a_T < 10⁻³ (single modes give a_T ≥ 1.7·10⁻²); the
  cluster consists of cancellation states and is invisible to archimedean min–max from below.
- Precision: T = 1.0, 1.2 λ_A and the bottom 4 resp. 11 cluster eigenvalues are at round-off; T = 1.2 cluster count
  not converged in N (14 at N = 40, 16 at N = 80). Extended precision would require recomputing Arch by a
  high-precision quadrature, not re-diagonalising the double-precision matrix.

## Next concrete step

The quantity that sets every capture dimension is λ_max(Π_T) = sup ⟨F, ΠF⟩ over P_T, not A_T. Determine its growth:
prove an upper bound λ_max(Π_T) ≤ A_T − (explicit loss) (the window correlations c_F(u_n) cannot all equal ‖F‖²
for distinct u_n; a Gram-matrix bound on the vectors S_{u_n}F gives λ_max(Π_T) ≤ λ_max of the Toeplitz-type
matrix (v_m v_n)^{1/2}⟨S_{u_m}F, S_{u_n}F⟩), and decide numerically whether λ_max(Π_T)/A_T → 0. If λ_max(Π_T) =
o(A_T), Theorem 3.1 gives a single-exponential cap on the cluster, which removes the doubly exponential arena count
from the capture problem; the sign then lives in an n_P × n_P Schur complement with n_P ≈ T e^{λ_max(Π_T)+O(1)}.
