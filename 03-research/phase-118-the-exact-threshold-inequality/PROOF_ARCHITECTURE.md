# Proof architecture for the exact threshold inequality

Coordinator's working document. Status of each item is marked
**[derived]**, **[measured]**, **[verified]**, or **[open]**.
Nothing here is in the paper.

---

## 1. The inequality

At every prime-power threshold `q_j -> q_{j+1}`,

    (T)   S_E - Z_E^*Z_E - b_E^* A_0^dag b_E >= 0
    (T')  ||Theta_N|| <= 1,   Theta_N = D_out^{dag/2} y_N

and, because the step is exact, `(T)` at every `j` plus the base window is
equivalent to `A_T >= 0` for all `T`, i.e. row (d).

## 2. What `A_T` actually is  **[VERIFIED against real zeta zeros]**

> **Status upgraded 2026-08-17.** `scripts/W5_highprec.log` checks
> `<A_T F,F> = sum_rho h(gamma_rho)` at `T = 0.6, 1.2, 2.0, 3.0` for several
> primitive test vectors, summing 200+ cached zeta zeros. Relative agreement
> **5.4e-11 to 1.6e-9**. The identity below is confirmed.
>
> The log also exhibits the mechanism: at `T=3.0`, `gamma_term = -0.037905513926`
> against `2*prime_sum = -0.037905515879` — they cancel to nine digits, and the
> residue `~2e-9` *is* the zero sum. The whole difficulty of RH lives in that
> cancellation, which is also why the assembly is delicate to condition.

### UNRESOLVED — resolve this before trusting any fine numerical conclusion

`scripts/W5_crossvalidate_assembly.log` compares two routes to the same
`<A_T F,F>` for piecewise-constant `F` on the mesh and they **disagree**: 2%-8%
relative, with a nearly constant absolute offset `~-2.2e-3` across every `T` and
every test vector, the matrix route always the larger. A systematic bias, not noise.

Coordinator's check: `psi_kernel` agrees with a 30-digit `mpmath` evaluation of
`sum_j exp(-a_j D)/a_j^2` to machine precision at `D = 0, 0.01, 0.05, 0.1, 0.3,
0.5, 1, 2, 4` (only at `D <= 1e-4`, below any realized mesh spacing, does the
Euler-Maclaurin tail lose digits). And the four-point formula
`Psi(c_i-c_j) - Psi(c_i-d_j) - Psi(d_i-c_j) + Psi(d_i-d_j)` is *algebraically*
exact for piecewise-constant `F` — derived from
`|Fhat(tau)|^2 = sum_ij F_i F_j [cos tau(d_i-d_j) - cos tau(d_i-c_j) -
cos tau(c_i-d_j) + cos tau(c_i-c_j)]/tau^2` and
`(1/pi) int_0^inf g_Gamma(tau) cos(tau D)/tau^2 dtau = Psi(D)`. So
`rowd_assembly` involves **no approximation at all** and is exact by construction.

**Inference (coordinator's, not yet checked):** the bug is in the new
cross-validation script, most likely truncation of the Gamma integral at finite
`tau` — the tail weighs like `log tau / tau^2`, and truncating it would produce a
*smaller* value, which is the observed direction of the offset.

**Until this is settled, treat every fine numerical conclusion as suspended** —
in particular `lam_min_norm ~ 1e-4`, since a `2e-3` bias would be twenty times
the measured quantity. This is the first thing to resolve on resume.

---

### The identity

Write `Fhat(tau) = int F(t)e^{i tau t}dt` and `h(tau) = Fhat(tau)Fhat(-tau)`.
For `F` real, supported in `I_T`, and primitive (`M_±F = 0`):

    <A_T F,F> = sum_rho h(gamma_rho),     rho = 1/2 + i gamma_rho,

the sum over the nontrivial zeros of zeta. Three collapses make this exact:

1. **The pole terms die.** Weil's formula carries `h(i/2)+h(-i/2)`, and
   `h(±i/2) = M_+F · M_-F`, which is `0` precisely because `F` is primitive.
   This is what the two Tate moments are *for*.

2. **The archimedean constant is forced.** `psi(1/4) = -(gamma + pi/2 + 3 log 2)`
   — checked to 30 digits — hence

        Re psi(1/4 + i tau/2) - log pi  ==  g_Gamma(tau) - m_0

   identically in `tau`, with `m_0 = log pi + gamma + pi/2 + 3 log 2`. The
   paper's `m_0` is not a normalization choice; it **is** the archimedean
   constant of the explicit formula. Verified at
   `tau = 0, 0.5, 3, 17.5, 120` to `< 1e-30`.

3. **The truncation is exact, not an approximation.** The prime sum in Weil's
   formula is weighted by the autocorrelation `g(u) = int F(t+u)F(t)dt`, which
   is supported in `(-2T,2T)`. So `g(log n) = 0` for `n >= e^{2T}` and the
   paper's cutoff `n < e^{2T}` loses nothing.

**Corollary of the shape.** For large `tau`, `Re psi(1/4+i tau/2) ~ log(tau/2)`,
so

    g_Gamma(tau) - m_0  =  2 pi * (density of zeros at height tau) + o(1),

the density being `(1/2pi)log(tau/2pi)`. Checked numerically: the ratio
`g_Gamma/(2 pi * density)` runs `3.59, 2.23, 1.80, 1.60` at
`tau = 50, 500, 5000, 50000` — converging to 1, with the discrepancy at finite
`tau` equal to exactly `m_0`. So `A_T` is literally
*(smooth zero-counting density) minus (prime oscillation)*, integrated against
`|Fhat|^2`.

### Consequence, stated without softening

The row-(d) inequality **is** localized Weil positivity on the primitive space.
It is therefore *equivalent* to RH, not a sufficient condition for it, and no
reformulation internal to the operator theory — factorization, Schur
complement, defect operators, scattering — can close it. Those reformulations
are exact and they are worth having, because they turn one global statement
into an induction with an exact step. They do not add arithmetic input, and
arithmetic input is what a proof needs.

This is a deliverable, not a setback: it settles what kind of work remains and
rules out an entire family of approaches, in the same way the unconditional
scalar no-go did.

## 3. Criticality  **[measured]**

`lam_min_norm = 1 - ||Theta_N||^2` decreases toward `0` under mesh refinement at
every threshold, roughly like `refine^{-1.4}`:

    step (2,3):   refine 4,8,12,16,24,32 -> .02792 .01214 .00633 .00403 .00215 .00144
    step (31,32):                        -> .09154 .07198 .05082 .04741 .03328 .02544

Galerkin restriction bounds a minimum from **above**, so the true value is at
most these. The data are consistent with `lam_min_norm -> 0+`, i.e.
`||Theta_N|| = 1`.

Section 2 explains why this must be so. `<A_T F,F> = sum_rho |Fhat(gamma_rho)|^2`
under RH, and the infimum over `||F||=1` is `0` because `Fhat` — entire of
exponential type `T` — can be made small at every zero ordinate the mesh can
resolve. Finer meshes reach higher frequencies, where more room to hide between
zeros is available, so the Galerkin minimum keeps falling. The operator is
positive with **no spectral gap**, exactly as the corpus's O3 records.

**What this forbids.** Any proof that loses a constant factor anywhere fails.
Only an exact conservative identity can work — which is precisely what
`thm:newdRegularizedStep` already prescribes (`C_eps = Z_eps^*Z_eps + E_eps`,
then `eps -> 0`).

**What this permits.** Numerics can still *refute*: a `lam_min_norm` that goes
negative at some refinement would kill row (d). They can never *confirm*.

## 4. Workstreams

| | question | status |
|---|---|---|
| W1 | is `lam_min_norm -> 0+` or does it cross zero? what is the minimizer? | running |
| W2 | does the target split into a coercive annulus block ⊕ an explicit 2x2 Tate block? | running |
| W3 | is there an explicit contraction `Phi` with `Y_T = Phi X_T`? | running |
| W4 | how far past `T = log 2` does interval certification reach? | running |
| W5 | verify §2 numerically against real zeta zeros; how far does *verified* RH carry the inequality? | running |

## 5. The one route that adds arithmetic input

Section 2 says the inequality needs input from outside the operator theory. The
cheapest such input available is the **verified height**: RH is known for all
`|gamma| <= H = 3.0000175e12` (Platt–Trudgian). Splitting

    <A_T F,F> = sum_{|gamma|<=H} |Fhat(gamma)|^2 + sum_{|gamma|>H} h(gamma_rho),

the first sum is `>= 0` unconditionally. The second is where the work is: an
off-line zero `sigma + i t` contributes at `gamma_rho = t - i(sigma-1/2)`, costing
a factor `e^{2T(sigma-1/2)}`. Two effects oppose each other — zeros far from the
line are rare (zero-density estimates), zeros near it are harmless — and the
high-frequency Gamma channel is, by §2's corollary, asymptotically *exactly* the
zero density, so it may absorb the tail. Whether that absorption is exact or only
asymptotic decides whether the mechanism closes. W5 is measuring it.

This is the only direction identified so far that is both (a) not blocked by §2
and (b) not blocked by phase 117's `c_N < 1`. It is also very likely classical —
Bombieri's work on Weil's quadratic functional is the place to check, and W5 has
been told to check it rather than assume novelty.
