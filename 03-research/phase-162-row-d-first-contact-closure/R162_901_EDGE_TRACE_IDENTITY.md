# R162_901 — Round 9: exact nonlinear edge-trace identity (O802.1)

Notation from R162_802 (A_T = B_T − K_T per parity, B_T = arch + polar,
K_T = prime comb Σ w_n S_{log n} compressed to I_T, w_n = Λ(n)n^{-1/2}, u_T = A_T^{-1}φ, f(T) = ⟨u_T,φ⟩,
S_C the collar Schur complement), R162_406 (Z-frame edge germ), R162_301 (noncommutative Euler lift).

**Verdict: NO-GO for the flow; PARTIAL for the identity.** An exact nonlinear identity that separates Λ
from all four falsifier classes exists (§3, Selberg's quadratic identity, placed in the coupling-order-2
coefficient of f). It cannot constrain f_par(0;T) at coupling 1, and so it cannot forbid first contact
(§4, §5). No sign is claimed. Gate 1 remains OPEN.

## 0. Failing lines (stated first)

| line | where | what fails | killer |
|---|---|---|---|
| L901.a | §2, Thm 2.1 | the only nonlinearity at the edge is the **square** of a residual that is linear in w once ũ_T is fixed | F2 |
| L901.b | §3, Prop 3.2 | products w_m w_n come with a kernel β_T(log m, log n) that depends on the sum **and** the difference of the logs. The sum channel sees Λ*Λ. The difference channel sees \|Σ w_n n^{it}\|², which is not a Dirichlet convolution | split dependence |
| L901.c | §4 | the Selberg identity is exact only coefficient by coefficient in the coupling ε (a → εa). For T > T_P the function ε ↦ f(T;ε) has a pole at some ε_c(T) < 1 (the Perron crossing), so no resummation to ε = 1 exists | radius < 1 |
| L901.d | §4.3 | the all-orders version exp_*(Λ/L) = δ_1 (Euler product) needs commuting transfer operators. The collar transfers do not commute (compressions, Brown–Halmos) | R162_301, F3 |
| L901.e | §5 | even granting §3 at every order, the bound needed to stop overshoot is an upper bound on ∫ flux. Any such bound from a quadratic identity is an estimate, so it dies by Theorem M | M |

## 1. Corpus check

- The square of (PC) is sign-blind: R161_099 (F2).
- Z-frame edge germ n_0^{-1/2}(log n_0 − Σ_{d|n_0,d<n_0} a(d)): R162_406. This is linear in a. It is reused
  below, not repeated.
- Noncommutative Euler lift and Brown–Halmos leakage: R162_301.
- Möbius conjugation Z S² Z⁻¹ = M(Λ) + S²: R162_502 and R162_701.
- Floor ledger, "exact nonlinear use" residual: R162_801 §6.
- Selberg's identity Λ·L + Λ*Λ = μ*L² has not been used anywhere in phases 152–162 (grep: no hits for
  "Selberg identity" / "Λ*Λ" in phase-16x). Its use in the Selberg–Riccati files of phase 104 is
  zero-side (Riccati for ζ'/ζ), not the T-flow.

## 2. The edge nonlinearity is a square — PROVED

**Theorem 2.1.** Fix T < T′ with A_T and A_{T′} invertible. In Theorem 2.1 of R162_802 the collar
residual splits as

  ρ = ρ_B[ũ_T] − φ|_C − Σ_{log n < T+T′} w_n (S_{log n}ũ_T)|_C,

where ρ_B is the arch+polar residual. For fixed ũ_T, ρ is affine in the weight vector w = (w_n), and

  f(T′) − f(T) = ⟨S_C^{-1}ρ, ρ⟩.

*Proof.* This is R162_802 Thm 2.1 and Cor 2.2, with the prime part written out. Only contacts with
log n < T + T′ reach C from I_T. ∎

**Corollary 2.2.** Under (REG), the infinitesimal flux is 𝔣(T) = c_T·R(T)², where

  R(T) = ρ_B[u_T](T) − φ(T) − Σ_{n<e^{2T}} w_n u_T(T − log n)

is the edge residual.
- The newest contact (n with ½log n = T) contributes w_n·u_T(−T⁺) = ε·w_n·u_T(T⁻). This is the edge trace
  of R162_802 §4.
- The older contacts contribute interior values.
- Substituting Λ = μ*L in R(T) gives the Z-frame expression of R162_406, which is linear.

**Failing line L901.a.** Once u_T is frozen, Λ*1 = log enters R linearly. The flux therefore contains
it only as a square, and the square of a linear identity is invariant under the orientation flip
(F2). The only other source of nonlinearity in w is the dependence of u_T on w. That is §3.

## 3. Products of weights: where Λ*Λ appears — PROVED (identity), PARTIAL (use)

Put a → εa and expand f(T;ε) = ⟨(B_T − εK_T)^{-1}φ, φ⟩ at ε = 0. This is legitimate on the set where
B_T > 0. B_T is the arch+polar form. It is positive only below the archimedean threshold T ≈ 0.58, and
beyond that it has finitely many negative directions, so the expansion is taken at a regular point
(R162_802 §3). Then

  f = f_0 + ε Σ_n w_n α_T(log n) + ε² Σ_{m,n} w_m w_n β_T(log m, log n) + O(ε³),

with α_T(x) = ⟨B^{-1}S_xB^{-1}φ,φ⟩ and β_T(x,y) = ⟨B^{-1}S_xB^{-1}S_yB^{-1}φ,φ⟩, where S_x is the
symmetrised shift compressed to I_T.

**Lemma 3.1 (Selberg, coefficient form).** For every N ≥ 1,

  Σ_{mn=N} Λ(m)Λ(n) + Λ(N) log N = (μ*L²)(N).

For a general a ≥ 0 supported on prime powers, write a = Λ_F with F = exp(Σ a(n)n^{-s}/log n). Then
a·L + a*a = f^{-1}*(f·L²), where f are the coefficients of F.
- For f = 1 (a = Λ) the right-hand side is μ*L², which is supported on ω(N) ≤ 2. The failure for
  the three falsifier classes is checked below. A general "iff" is not claimed.
- Deletion model Λ1_{n≥5}: f = coefficients of ζ·exp(−Σ_{n<5}Λ(n)n^{-s}/log n). The support fails, for
  example at N = 30.
- κ-model: at N = p the identity gives κ log²p ≠ log²p.
- DH: f_DH ≠ 1, so the support fails.

So this is an exact identity that is **nonlinear** in a and separates Λ from F3 (all classes) and F4
(it is quadratic). This answers the first half of O802.1.

*Proof.* Take the coefficients of (F'/F)' = F''/F − (F'/F)². For F = ζ the right-hand side is μ*L².
The claim ω ≤ 2 holds because μ*L² vanishes when ω(N) ≥ 3. The falsifier failures are direct
coefficient checks: at N = p for the κ-model, and at squarefree N with three primes for the deletion
model and for DH. ∎

**Proposition 3.2 (split dependence).** On the full line (T = ∞, B Toeplitz, no compression) one has
S_x B^{-1} S_y = B^{-1} S_x S_y and S_xS_y = (S_{x+y} + S_{x−y})/2 (symmetrised shifts), so β(x,y) = γ(x+y) + γ(x−y). The second-order term
is then

  Σ_N N^{-1/2}(Λ*Λ)(N)·γ(log N)  +  ∫ γ̂(t)·|Σ_n w_n n^{it}|² dt.

- The **sum channel** evaluates Λ*Λ at the multiplicatively composed threshold ½log(mn). By Lemma 3.1
  it equals Σ N^{-1/2}[(μ*L²)(N) − Λ(N)log N]γ(log N). The Λ log N piece is the dilation derivative
  of the first-order term, since ∂_x acting on α brings down log n. This is the requested exact
  relation between the thresholds ½log m, ½log n and ½log mn.
- The **difference channel** is the mean square of ζ'/ζ on a vertical line against γ̂. It is not
  constrained by Lemma 3.1.
- At finite T the compression breaks even the two-channel form: β_T(x,y) depends on x and y
  separately, through the positions of the contacts inside I_T (Brown–Halmos).

**Failing line L901.b.** The pair (m,n) with mn = N is weighted by β_T(log m, log n). This kernel is not
a function of N alone, so Λ*Λ never appears as a coefficient of the flow at finite T. It appears only
after a split-independence that the compressed operator does not have. The edge-trace version is the
same statement. At T = ½log N the pair contributes ε·u(T − log m)·u(T − log n)-type products, and these
vary over divisor pairs of N.

## 4. Why the identity does not reach the flow at coupling 1 — NO-GO

**4.1 Radius (L901.c).** For T > T_P the Perron eigenvalue μ_1(B − εK) crosses 0 at some ε_c(T) < 1,
because μ_1 ~ −4e^T at ε = 1 (R162_802 §5.2). Hence f(T;·) has a pole at ε_c and its Taylor series at 0
does not converge at ε = 1. An identity for each Taylor coefficient therefore says nothing about
f(T;1), and there is no resummation, because the pole is genuine (R162_802 §3.1: f → ±∞ across
crossings). A Padé or Stieltjes continuation would need positivity of the ε-moment problem, and that
is the Weil sign (E1).

**4.2 Order k.** The degree-k coefficient carries Λ^{*k} with a k-point kernel. The only exact relations
among the Λ^{*k} are the consequences of ζ = exp(Σ Λ n^{-s}/log n), i.e. exp_*(Λ/L) = δ_1. The Neumann
series in ε is geometric, not exponential, so it produces 1/(1−K) and not exp. Matching the two needs a
logarithmic reparametrisation of K, and that is a function of an operator. It is exact only if the
contact operators commute.

**4.3 Commutation (L901.d).** The compressed shifts S_{log m}, S_{log n} on L²(I_T) do not commute. Their
commutator is a finite-rank edge operator whose size is independent of the symbol (Brown–Halmos). This
is exactly the anomaly of R162_301, which was shown to be symbol-independent and so not Λ-specific
(F3). So "multiplicativity of the jump pattern" holds iff the transfer operators commute, and they do
not.

**Criterion 4.4 (what multiplicativity would require).** Let e(T) = u_T(T⁻)² be the edge-trace profile on
the thresholds T_n. The jump series D(s) = Σ w_n e(T_n) n^{-s} satisfies a Selberg-type relation
(−D′ + D²/c = Dirichlet series supported on ω ≤ 2) iff e(T_n) = c·n^{α} on prime powers, i.e. iff e is
exponential in T on the threshold set. The table of R162_703 §3 (even and odd edge traces at ½log5
differing by orders of magnitude, with non-monotone variation) excludes this in at least one sector.
This is a structural statement and no new numerics were run.

## 5. Consequence for overshoot — NO-GO

Stopping first contact means showing f_ev(T) < −½ and f_odd(T) < ½ for all T (R162_802 §3.3–3.4). The
flow is monotone increasing, so this is an **upper** bound on ∫ 𝔣. The only Λ-specific exact input
found (Lemma 3.1) controls the sum channel of one Taylor coefficient. Turning it into a bound on f(T;1)
needs the following:
- (i) control of the difference channel, i.e. a mean-square bound for ζ'/ζ against γ̂ (an estimate,
  which dies by Theorem M, L901.e);
- (ii) resummation across ε_c (E1);
- (iii) commutation (F3).

The deletion model violates Lemma 3.1, yet it is not excluded by any line above that stays exact. Its
overshoot at 0.4608 (cor:convfail) happens where ε_c(T) < 1 already, so the separating identity lives
in a regime the flow never visits at coupling 1.

## 6. Record

- New: Lemma 3.1 as the Λ-separating nonlinear identity. It separates on all four falsifier classes.
  Prop 3.2 places it exactly in the sum channel of the coupling-2 coefficient, at the composed
  threshold ½log(mn).
- Dead: every route from it to f_par(0;T) at coupling 1 (L901.a–e).
- Add to R162_590 §1c: "Selberg quadratic identity in the T-flow — R162_901 — edge flux is a square
  (F2); Λ*Λ only in the sum channel of the ε²-coefficient, split-dependent at finite T; ε-radius < 1 past
  T_P; exp_* needs commuting transfers (R162_301) — F2, F3, M, E1".
- Residual (not claimed): a non-perturbative object in which the difference channel |ζ'/ζ|² cancels
  exactly against the sum channel. That would be a positivity statement for ζ'/ζ on a line, i.e. Weil
  again (E1), unless it is exact and not positive.
