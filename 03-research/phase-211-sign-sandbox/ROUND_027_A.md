# Round 027 A: is the weight vector of the comb the global maximiser of μ_T?

## Hypothesis
μ_T(v) = bottom of a_T^{(v)} = Arch − Σ_n v_n Π_n on P_T, for v ∈ ℝ^{N_T}. Paper 47 (lem:degen) shows
that μ_T is concave and that μ_T(v_T(Λ)) = λ_A(T). The hypothesis is (A) v_T(Λ) = argmax μ_T, plus (B)
some explicit v̂ has μ_T(v̂) ≥ 0. Together they would give λ_A = max μ_T ≥ μ_T(v̂) ≥ 0.

## Corpus check
lem:degen and rem:resweights (Paper 47, ~3260–3320) bound μ_T from above by a tangent plane at v_T(Λ)
and leave open whether the degenerate case (all c_{F*}(log n) = 0) occurs. ROUND_002_D/E studied only
the ray cΛ, where c* = 1 holds as a kink. The new step here is to maximise over the full weight space.
This route is not in the index.

## Method (NUMERICAL)
tools/galerkin_mp.py, N = 60 (T = 0.8, 1.0) and N = 90 (T = 1.2), 40 digits (working precision 60).
Π_n is built separately for each contact n with the exact c^sym. Each parity sector is restricted to
P_T. The gradient test uses g_n = F^T Π_n F for the bottom eigenvectors F; −g is the supergradient.
M_T = max_v μ_T(v) is found with a log-barrier path-following Newton method for the LMI
"maximise t such that Arch − Σ v_n Π_n − tI ⪰ 0 on each sector of P_T", in multiprecision with τ up
to 10^28. Scripts are in the scratchpad and are not kept.

## 1. Gradient test at v_T(Λ)
In every case the bottom eigenvalue is simple. The gap to the next eigenvalue is a factor of about
200–2000, and it is resolved far above the precision floor. The gradient g is clearly nonzero:

| T | λ_A | next eigenvalue (sector) | g = (c_{F*}(log n))_n, normalised |
|---|---|---|---|
| 0.8 | 6.23e-12 | 1.12e-9 (odd) | (0.0371, 0.0214, 2.5e-5) for n = 2, 3, 4 |
| 1.0 | 2.49e-23 | 1.27e-20 (odd) | (−0.0121, 0.0355, 3.0e-4, 3.2e-7, 5.5e-18) for n = 2, 3, 4, 5, 7 |
| 1.2 | 2.61e-41 | 4.40e-38 (odd) | (−0.0430, 0.0449, 7.5e-4, 3.1e-6, …) for n = 2, …, 11 |

Since the bottom is simple, ∂μ_T(v_T(Λ)) = {−g}, which does not contain 0. So v_T(Λ) is NOT a
maximiser at any of the three windows, at Galerkin level. This is also the non-degenerate case of
lem:degen: the minimiser has c_{F*}(log 3) ≠ 0. The near-null cluster does not rescue the hypothesis.
Its members are separated by factors of 10²–10³, so the convex-hull condition reduces to the single
bottom vector.

## 2. The global maximum (T = 0.8)
The barrier path converges to 13 digits:
M_{0.8} = 0.0473548670538, against λ_A(0.8) = 6.23e-12.
The maximiser is v* = (0.0843, −0.858, −1.820) · v_T(Λ) coordinatewise (n = 2, 3, 4). The relative
distances from v_T(Λ) are 0.92, 1.86 and 2.82. The maximiser is far from the comb and has negative
weights. T = 1.0 (τ up to 10^9; converged to 8 digits): M_{1.0} = 0.02967824, against λ_A(1.0) = 2.49e-23. The maximiser is
v* = (0.530, 0.0105, −0.403, −0.735, −1.982) · v_T(Λ) for n = 2, 3, 4, 5, 7. At v* the bottom is
six-fold (0.029678 twice, 0.029683 twice, 0.029771, 0.03173, one in each sector). This is the
degeneracy that an LMI optimum needs, and it is formed by moving the weights by O(1), not at the comb.
T = 1.2 was not maximised: the gradient test of §1 already settles it there.

## 3. Reading
- (A) fails decisively (NO-GO, NUMERICAL, with the PROVED mechanism of lem:degen). The tangent bound
  of lem:degen is strict in the useful direction: λ_A = μ_T(v_T(Λ)) < M_T by a margin of order 10^-2.
- So the split (A) + (B) cannot work. (B) is true but useless: M_T > 0 says nothing about μ_T at the
  comb. The comb sits where μ_T is almost zero, on the slope of a concave function whose top is
  O(10^-2) high.
- Falsifier test: μ_T does not depend on the comb. The maximiser v* is one fixed point, and neither
  v_T(Λ) nor cv_T(Λ) nor a_P nor any other comb in the list is v*. The route therefore does not
  separate the true comb from the falsifiers. It is not a sign mechanism.
- Θ^full was not computed. Under (A) false it gives only the weak dual bound M_T ≤ Θ^full, which says
  nothing about λ_A.

## Result
NO-GO (class: global concave maximisation of the bottom over weight vectors on the positions log N_T;
v_T(Λ) is not the argmax, because the bottom is simple and has a nonzero autocorrelation gradient).

## What was proved
Nothing new. The mechanism is lem:degen together with simplicity of the bottom eigenvalue, which holds
at Galerkin level, NUMERICAL.

## What failed and why
0 ∉ ∂μ_T(v_T(Λ)): g ≠ 0 at T = 0.8, 1.0, 1.2. At T = 0.8, M_T − λ_A ≈ 0.047.

## Next concrete step
None along this route. A constrained variant (v ≥ 0, or v restricted to a falsifier-separating set)
would need its own reason to separate the comb. Without one, it is not worth retrying.
