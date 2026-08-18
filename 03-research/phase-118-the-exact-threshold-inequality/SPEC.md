# Phase 118 — proving the exact threshold inequality

**Shared ground truth. Read this before doing anything.**

## 0. The single inequality

Let `2 = q_1 < q_2 < ...` be the prime powers, `tau_j = (1/2) log q_j`,
`I_T = (-T,T)`. On `L^2(I_T)` define the localized primitive operator

    A_T = G_{Gamma,T} - m_0 I - sum_{2<=n<e^{2T}} w_n (S_{log n} + S_{-log n})
    w_n = Lambda(n)/sqrt(n),  m_0 = log pi + gamma + pi/2 + 3 log 2

restricted to the **primitive space** `P_T = ker M_- ∩ ker M_+`, where
`M_± F = ∫ F(t) e^{±t/2} dt` (the two Tate moments).

`A_T >= 0` for all `T` is Weil positivity, i.e. row (d), i.e. RH.

Because the step `P_{tau_j} -> P_{tau_{j+1}}` is **exact**
(`E* A_{tau_{j+1}} E = A_{tau_j}`, no error accumulates — the newborn contact
`q_j` has shift length exactly `2 tau_j` = the width of the old window, so it
is null on the core), row (d) is **equivalent** to: the base window is
positive, and at every threshold the enlarged block is nonnegative.

Split `P_{tau_{j+1}} = C ⊕ A` (old core = zero-extended `P_{tau_j}`; corona
`A = C^perp`). With the balanced factorization `A_T = X_T^*X_T - Y_T^*Y_T`,
`X = (X_0,X_E)`, `Y = (Y_0,Y_E)`, and

    R_0 = X_0^*X_0,  L_0 = Y_0^*Y_0,  r = X_0^*X_E,  l = Y_0^*Y_E,  A_0 = R_0-L_0
    H   = R_0^dag r,  S_E = X_E^*X_E - r^*R_0^dag r
    Z_E = Y_E - Y_0 H,  b_E = L_0 H - l

**THE INEQUALITY TO PROVE, at every threshold j:**

    (T)   S_E - Z_E^* Z_E - b_E^* A_0^dag b_E  >=  0        [eq:newdSchurTarget]

equivalently, in the normalization where the constant is one:

    K_N = Y_0 R_0^{dag/2},   y_N = (Y_E - Y_0 H) S_E^{dag/2}
    D_in = I - K_N^*K_N,     D_out = I - K_N K_N^* = I - Y_0 R_0^dag Y_0^*
    (T')  y_N^* D_out^dag y_N <= I    i.e.   ||Theta_N|| <= 1,
          Theta_N = D_out^{dag/2} y_N ,
    equivalently  y_N = D_out^{1/2} v_N  with  v_N  a contraction (Douglas).

The normalized minimum measured in code is

    lam_min_norm = lambda_min( S_E^{dag/2} (T) S_E^{dag/2} ) = 1 - ||Theta_N||^2 .

## 1. What is already established (do NOT re-derive)

- Balanced factorization `A_T = R_T - L_T = X_T^*X_T - Y_T^*Y_T`, explicit,
  unique given the codomain convention `L^2(R)`.
- `R_T = G_{Gamma,T} + sum w_n (I - Re S_n)`, `L_T = m_0 I + sum w_n (I + Re S_n)`.
- The step is exact; corona = (primitives supported in the annulus)
  ⊕ span{e^{-t/2}, e^{t/2}}|_{I_{tau_j}} — annulus **plus exactly two** Tate
  directions restricted to the old core.
- Output-defect reduction (T) <=> (T').
- Regularized one-step criterion: `C_eps = D_E - Q_c^*(D_0+eps)^{-1}Q_c` is
  monotone in eps; positivity of the enlarged block <=> `C_eps >= 0` for all
  eps>0; and then the range condition `Ran Q_c ⊆ Ran D_0^{1/2}` is **forced**,
  not assumed.
- Unconditional scalar no-go: the scalar/trace route cannot close
  (`alpha_N/(m_0+2 sigma_N) -> 1/4`; deficit `3 sqrt N` of leading order).
- Phase 117: the *source model* route is dead — the transfer constant `c_N` in
  `D_E >= c_N Xi^* D_N Xi` is `< 1` at every threshold and decays like
  `(log N)^{-0.6}`. **Do not work on the Gamma-Tate source estimate.**
- Phase 117 also refuted the bound `rho_N <= 1/(20 log N)`.

## 2. The new fact that governs this phase

`lam_min_norm` **decreases to 0** under mesh refinement, roughly like
`refine^{-1.4}`, at every threshold tested:

    step (2,3):  refine 4,8,12,16,24,32  ->  .02792 .01214 .00633 .00403 .00215 .00144
    step (31,32):                        ->  .09154 .07198 .05082 .04741 .03328 .02544

Galerkin restriction gives an **upper** bound on a minimum, so the true value
is `<=` these. The sequence is consistent with `lam_min_norm -> 0+`, i.e.

> **the inequality is CRITICAL: ||Theta_N|| = 1, not <= 1 - delta.**

Consequences that constrain every proof attempt:

1. No estimate that loses any constant factor can work. The proof must be an
   **identity**: a conservative decomposition
   `C_eps = Z_eps^* Z_eps + E_eps` with `E_eps >= 0`, passed to the limit.
2. Numerics can never *confirm* the inequality by margin — the margin is zero.
   Numerics are useful only to (a) detect a **violation** (a negative
   `lam_min_norm` at some refinement would kill row (d)), and (b) reveal the
   **structure of the near-null direction**, which is what the identity has to
   reproduce.
3. Therefore the decisive numerical question is not "is it positive" but
   **"what is the minimizing direction, and does it stay on the positive side"**.

## 3. Code

`scripts/rowd_assembly.py` — mesh, Gram, `shift_form`, closed-form Gamma
kernel `Psi(D) = sum_j exp(-a_j|D|)/a_j^2`, `a_j = 2j+1/2`, Tate moments,
`assemble(T, refine, extra_points) -> {c,d,Gram,G,R,L,A,Tate,T,N}`.
All matrices are **form** (Gram-weighted) matrices in a piecewise-constant
basis; the `L^2` inner product matrix is `Gram = diag(d-c)`.

`scripts/rowd_threshold.py` — `threshold_blocks(q_old,q_new,refine)` returns
`Zc` (old core), `Za` (corona, Gram-orthonormal), and all blocks
`R0,L0,r,l,RE,LE,A0,Anew,B`; `schur_target(bk)` returns `S`, `S_E`, `b_E`,
`pen`, `lam_min_norm`, plus range residuals.

Validated in phase 117 against: direct quadrature for `Psi`; exact
mesh-independence to 9 digits (refine 4->64); `A = R - L` to `0.000e+00` with
both halves PSD; `thm:exactstep`(4) old-core spectra to `0.000e+00` at 9
consecutive prime-power steps; `thm:exactstep`(5) `extra = 2` exactly.

Environment: `numpy` 1.26.4, `scipy` 1.11.4 are importable directly.
`python-flint` (0.9.0) needs `PYTHONPATH=/tmp/rowd-flint`. **`/tmp` is
volatile — copy it into the phase directory before relying on it.**

## 4. Rules

- Never report a claim you did not compute. Distinguish measured / derived /
  conjectured in every line you write.
- Every reported number must be reproducible by a script left in
  `scripts/` with the command line in a comment at the top.
- Pseudo-inverse cutoffs are load-bearing: **always** report results as a
  function of the spectral cutoff `rtol`, never at a single silent value.
  Near-null directions of `A_0` are the whole story.
- Monotonicity directions matter. State for each quantity whether Galerkin
  gives an upper or a lower bound, and why.
- Nothing here proves RH. Do not promote status.
