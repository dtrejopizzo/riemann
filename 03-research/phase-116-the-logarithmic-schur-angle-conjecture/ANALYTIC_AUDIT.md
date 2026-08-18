# Analytic audit of the proposed mean-zero closure

## Verdict

The decomposition

\[
E_N=\mathbb C u_N\oplus E_N^0,
\qquad
u_N=\delta_N^{-1/2}\mathbf 1_{(0,\delta_N)},
\qquad
E_N^0=\left\{h:\int h=0\right\},
\]

is exact and useful. The proposed argument after that decomposition does
not prove positivity. Several of its analytic assertions either concern the
wrong operator or are precisely the estimate that still has to be proved.

## Exact block reduction — PROVED

Put

\[
\mathfrak A_N[e]=\|\mathbf L_Ne\|^2,
\qquad
\mathfrak Q_N[e]=\mathcal E_{\Gamma T,N}(e),
\qquad
\mathfrak D_N=\mathfrak Q_N-\mathfrak A_N.
\]

Relative to the decomposition above,

\[
\mathfrak D_N=
\begin{pmatrix}d_N&b_N^*\\ b_N&C_N\end{pmatrix}.
\]

The unit Gamma--Tate inequality is equivalent to

\[
C_N\ge0,
\qquad
b_N\in\operatorname{Ran}C_N^{1/2},
\qquad
d_N-b_N^*C_N^\dagger b_N\ge0.
\]

This is an algebraic/form-theoretic equivalence. It does not supply any of
the three inequalities.

## Failure 1: the Gamma cross term is not zero

Gamma is applied to the arithmetic output, not directly to the input
profile. The relevant cross term is

\[
\sum_k\mathcal G_\Gamma
   (L_{N,k}h,L_{N,k}u_N),
\]

not \(\mathcal G_\Gamma(h,u_N)\). In Fourier variables it contains

\[
\sum_k\int_{\mathbb R}g_\Gamma(\tau)
 |P_{N,k}(\tau)|^2
 \widehat h(\tau)\overline{\widehat u_N(\tau)}
 \frac{d\tau}{2\pi},
\]

which is not identically zero. Moreover, \(u_N\) is an indicator after zero
extension to the line and has boundary jumps; it is not a global constant
annihilated by the Gamma multiplier.

## Failure 2: zero mean is not hard spectral support

The condition \(\widehat h(0)=0\) gives a zero at one frequency. It does not
imply

\[
\operatorname{supp}\widehat h\subset\{|\tau|\gtrsim N\}.
\]

An arbitrary element of \(L^2(0,\delta_N)\) need not even possess an
\(L^2\) derivative, so a derivative-form Wirtinger inequality cannot be
inserted without changing the domain. A quantitative uncertainty estimate
may still yield an averaged logarithmic coercivity statement, but that is a
new theorem and must survive multiplication by every arithmetic polynomial
\(P_{N,k}\).

## Failure 3: the claimed Gamma gap is the missing theorem

The bound

\[
C_N[h]\ge \kappa\log N\,\|\mathbf L_Nh\|^2
\qquad(h\in E_N^0)
\]

has not been proved. It cannot be inferred solely from
\(g_\Gamma(\tau)\sim\log|\tau|\), because \(P_{N,k}\widehat h\) may
redistribute its energy between the Gamma-deficit window and its exterior.
This is a sharpened version of the global observability problem, not a
consequence already available in the manuscript.

## Failure 4: the Schur penalty is a supremum

When the range condition holds,

\[
b_N^*C_N^\dagger b_N
=\sup_{0\ne h\in E_N^0}\frac{|b_N(h)|^2}{C_N[h]}.
\]

Evaluation at one selected \(h\) gives a lower bound for this supremum, not
an upper bound. To majorize the penalty one must prove

\[
|b_N(h)|^2\le K_N C_N[h]
\quad\text{for every }h\in E_N^0.
\]

Cauchy--Schwarz applied only to the leakage part does not control the full
functional \(b_N\), which also contains Gamma and Tate cross terms.

## Failure 5: the constant margin is not Tate minus leakage

The exact scalar is

\[
d_N=
\sum_k\bigl(
 \mathcal G_\Gamma[L_{N,k}u_N]
 +\mathcal T_{I_N}[L_{N,k}u_N]
 -\|L_{N,k}u_N\|^2\bigr).
\]

Neither positivity nor proportionality to
\(\|\mathbf L_Nu_N\|^2\) follows from its definition. Both require proof.

## What survives from the proposed idea

For \(h\in E_N^0\), cancellation of the constant Taylor coefficient gives
the rigorous estimate

\[
|M_\pm(h)|
\le
\left\|e^{\pm t/2}-1\right\|_{L^2(0,\delta_N)}\|h\|_2
=O(\delta_N^{3/2})\|h\|_2.
\]

Translation gives the exact identities

\[
M_+(L_{N,k}h)=P_{N,k}(i/2)M_+(h),
\qquad
M_-(L_{N,k}h)=P_{N,k}(-i/2)M_-(h).
\]

Thus the zero-mean condition genuinely suppresses the Tate cross channel.
It does not annihilate the Gamma or leakage cross channels.

## Correct irreducible target

Assuming \(d_N>0\) and positivity of \(C_N\), define the exact squared
Schur angle

\[
\rho_N=
\frac{b_N^*C_N^\dagger b_N}{d_N}
=\sup_{0\ne h\in E_N^0}
 \frac{|b_N(h)|^2}{d_NC_N[h]}.
\]

The scalar Schur condition is exactly \(\rho_N\le1\). Therefore the candid
analytic programme is:

1. prove \(C_N\ge0\) with the required range control;
2. prove \(d_N>0\);
3. prove the uniform angle bound \(\rho_N\le1\).

The finite-dimensional experiments estimate \(\rho_N\) near
\(0.01\)--\(0.02\) on the tested discretizations. They are strong evidence
for the angle formulation, but they are not interval-certified and do not
control arbitrary profiles or all \(N\).

A reproducible six-bin scan using fixed anchor thresholds and eight seeded
random thresholds in \(3\le N\le260\) is stored in
`current-chat/work/mean_zero_schur_scan.csv`. Across its eighteen sampled
thresholds, the smallest full quotient stays above \(4.08\), the smallest
zero-mean quotient increases from about \(7.11\) to \(11.51\), and the
finite-dimensional Schur fraction stays below \(0.0144\). This strengthens
the numerical pattern but does not change the OPEN status.

## Status

- Reciprocal band theorem: **PROVED**.
- Uniform connected-cluster payment: **PROVED**.
- Intra-band low-frequency coherence: **PROVED**.
- Mean/oscillation Schur equivalence: **PROVED**.
- Proposed Cauchy--Schwarz/Gamma-gap closure: **REJECTED BY AUDIT**.
- Uniform Schur-angle bound and row (d): **OPEN**.

## Addendum (2026-08-17): the second open target

Two external audits of `main.tex` concluded that row (d) had a *second*,
unnamed gap — the passage from the source estimate to the physical threshold
Schur condition, justified in the manuscript only by the subjunctive clause
"shorting a passive source network would give". That reading of the
manuscript was correct; the inference that it is a research gap was not.

The machinery is proved in the corpus and was simply never transferred:

- `previous-phase-114/114_e_01_BALANCED_CHANNEL_FACTORIZATION.md` — the
  balanced factorization `A_T = X_T^*X_T - Y_T^*Y_T` with explicit columns
  (Thm 3.1), the identification `H_{5/4} = G_{Γ,T}` (Cor 3.2), the exact step
  R1 (Thm 5.0, including corona = annulus ⊕ 2 Tate modes), and the
  regularized one-step theorem D1 (Thm 5.1) which *derives* the range
  condition instead of assuming it. 17 + 15 checks pass.
- `previous-phase-114/114_d_170_OUTPUT_DEFECT_CHANNEL_REDUCTION.md` — the
  reference Cholesky transform, the push-through and Julia identities, and
  the reduction of the threshold condition to the unit output capacity
  `y_N^* D_out^† y_N ≤ I`. Verifier passes.
- That same file, §0, had already recorded the correction: those objects
  "no fueron transferidos al paper … es una tarea editorial, no una laguna
  de investigación".

All of it is now in `main.tex` (see `thm:balancedfactorization`,
`thm:exactstep`, `thm:newdOutputDefect`, `thm:newdRegularizedStep`,
`prop:returnisschur`, `cor:scalarnogo`).

**What is genuinely open is one estimate in two normalizations, plus the
comparison between them:**

1. **Source model** — the uniform Schur angle bound, `ρ_N ≤ 1−ε`
   (`conj:newdLogSchurAngle`). Restated at the strength actually consumed;
   the empirical `ρ_N ≤ 1/(20 log N)` is now recorded as an observation, not
   as the hypothesis.
2. **Exact/physical** — `‖Θ‖ ≤ 1` with `Θ = D_0^{†/2} Q_c 𝔇_E^{†/2}`,
   equivalently `y_N ∈ Ran D_out^{1/2}` with `‖D_out^{†/2} y_N‖ ≤ 1`
   (D.170 (3.8); D2 of `114_e_01` §6).
3. **The comparison** — `𝔇_E ≥ c_N · Ξ_N^* 𝔇_N Ξ_N`, now stated in the paper
   as `prob:newdTransferComparison`. This is the only item neither the paper
   nor the corpus addresses, and it is finite-dimensional at each `N`, hence
   decidable numerically before any analytic investment. **It is the next
   thing to compute.**

Also newly transferred, and worth flagging because it constrains every future
attempt: `114_e_01` §4 proves the scalar route closed **unconditionally** —
`α_N/(m_0+2σ_N) → 1/4`, the deficit `3√N` is of leading order, and
`α_N ∼ √N` is sharp. No sharpening of the coercivity constant can close it.
