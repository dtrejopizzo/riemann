# R161_003 — Polar renormalization of the Müntz defect

## 0. Verdict

The raw finite Müntz sums `S_N` are not a convergent approximation to the Poisson-intertwining operator on the
critical half-density. Their defect energy is generically oscillatory and of order `N`. Therefore monotonicity of
`||E_NF||^2` cannot orient row D.

There is, however, a canonical correction: subtract the explicit polar term in Euler–Maclaurin. The resulting
renormalized Müntz multipliers converge to `zeta(1/2+i tau)` and their Poisson defects converge to zero on Schwartz
data. This identifies the correct object for the next phase-161 round.

No sign is claimed.

## 1. Raw defect on the Mellin line

Put `s=1/2+i tau`,

`D_N(s)=sum_(n<=N)n^(-s)`

and let

`u_infty(tau)=pi^(-i tau) Gamma(1/4+i tau/2)/Gamma(1/4-i tau/2)`.

In Mellin coordinates the finite Poisson defect `E_N=S_NFcal-JS_N` is the reflection multiplier

`e_N(tau)=D_N(s)u_infty(tau)-D_N(1-s)`.

The full functional equation is `zeta(s)u_infty(tau)=zeta(1-s)`, but the Dirichlet series does not converge at
`Re s=1/2`.

Euler–Maclaurin gives, uniformly on fixed vertical compact sets,

`D_N(s)=zeta(s)+N^(1-s)/(1-s)+O_s(N^(-1/2))`.

Hence

```
e_N(tau)
 = N^(1/2)[u_infty(tau)N^(-i tau)/(1/2-i tau)
            -N^(i tau)/(1/2+i tau)] + O_tau(N^(-1/2)).             (1.1)
```

**Proposition 1.1 (raw truncation obstruction; PROVED).** For every fixed `tau!=0`, there is a sequence `N_j->infty`
and a constant `c_tau>0` such that `|e_Nj(tau)|>=c_tau N_j^(1/2)`. In particular `e_N(tau)` has no finite pointwise
limit, and no monotonicity of `|e_N(tau)|^2` follows from Poisson.

*Proof.* Substitute Euler–Maclaurin and use the functional equation to cancel the two zeta terms. Since
`|1/2-i tau|=|1/2+i tau|`, the leading bracket is a fixed nonzero multiple of
`sin(tau log N+alpha_tau)`. The sequence `tau log N` is unbounded and its successive increments tend to zero; hence
modulo `pi` it enters an interval on which `|sin|>=1/2` infinitely often. Along that subsequence the leading term is
`>=c_tau N^(1/2)`, while the error is `O_tau(N^(-1/2))`. ∎

The accompanying script gives diagnostic values; the proposition, not the numerics, is the result.

## 2. Canonical polar subtraction

Define

```
C_N(s) = N^(1-s)/(1-s),
Z_N(s) = D_N(s)-C_N(s).
```

Let `S_N^ren=Z_N(1/2+iD)` and define

`E_N^ren=S_N^ren Fcal-JS_N^ren`.

Its reflection multiplier is

`e_N^ren(tau)=Z_N(s)u_infty(tau)-Z_N(1-s)`.

**Theorem 2.1 (renormalized Poisson convergence; PROVED on Schwartz data).** For each fixed `tau`,

`e_N^ren(tau)=O_tau(N^(-1/2))`.

Moreover, after multiplication by any fixed Schwartz function of `tau`, `e_N^ren` tends to zero in `L^2` provided
the standard Euler–Maclaurin remainder is used with sufficiently many terms.

*Proof.* `Z_N(s)=zeta(s)+O_s(N^(-1/2))` and the same holds at `1-s`. Insert the functional equation. Repeating
Euler–Maclaurin to order `r` gives an error bounded by `N^(-r-1/2)` times a polynomial in `|tau|`; a Schwartz factor
absorbs that polynomial and dominated convergence applies. ∎

This is the operator version of the polar subtraction already implicit in `R160_D4_R2`, Theorem 4.1. Its role here is
different: it repairs the Poisson defect *before* forming the quadratic object.

### 2.1 The polar term is the continuum

**Theorem 2.2 (lattice-minus-continuum representation; PROVED).** With `tau_aF(t)=F(t+a)`,

```
C_N(D) = integral_(0)^N x^(-1/2) tau_(log x) dx,                  (2.1)
S_N^ren = sum_(1<=n<=N)n^(-1/2)tau_(log n)
          - integral_(0)^N x^(-1/2)tau_(log x) dx.               (2.2)
```

The integrals are strong integrals on compactly supported smooth vectors. Moreover

```
(C_N(D)F)(t)
 = exp(-t/2) integral_(-infinity)^(t+log N) exp(y/2)F(y)dy.       (2.3)
```

If `supp F subset (-T,T)` and `A(F)=integral exp(y/2)F(y)dy=0`, then

`supp C_N(D)F subset [-T-log N,T-log N]`.

Finally, in the continuous parameter `x>0`,

`d/dx C_x(D)=x^(-1/2)tau_(log x)`.                               (2.4)

*Proof.* The Mellin multiplier of `x^(-1/2)tau_(log x)` is `x^(-s)`. Integrating from `0` to `N` gives
`N^(1-s)/(1-s)=C_N(s)`, proving (2.1)–(2.2). The inverse Mellin kernel of `1/(1-s)` is
`exp(-u/2)1_(u>=0)`. Translation by `log N` and direct convolution give

`sqrt(N) integral_0^infinity exp(-u/2)F(t+log N-u)du`,

which becomes (2.3) after `y=t+log N-u`; the factors `sqrt(N)` cancel. Below the left endpoint the cumulative
integral is zero; above the right endpoint it is the full moment `A(F)=0`, proving the support statement. Equation
(2.4) follows either from (2.1) or by differentiation of the upper limit. ∎

**Reading.** `S_N^ren` is exactly the Euler–Maclaurin discrepancy between the positive integers and the positive
continuum, transported through multiplicative dilations. Poisson is now being applied to a discrepancy rather than
to a divergent critical Dirichlet series. The primitive Tate moment does not annihilate `C_N(D)` pointwise; it turns
its one-sided tail into a compact boundary layer.

## 3. The renormalized anomaly

The algebraic proof of `R161_001`, Theorem 3.1, works for any operator `S` preserving the core if one defines

`K=-[X,S]`, `E=SFcal-JS`, and `H=L_MS-K`.

Consequently the renormalized operators satisfy the exact identity

```
S_N^ren A_M Fcal
 = {X,E_N^ren}-L_M^*E_N^ren-JH_M,N^ren-H_M,N^ren Fcal,            (PC-ren)
```

with `H_M,N^ren=L_MS_N^ren+ [X,S_N^ren]`.

Unlike the finite `H_M,N`, this renormalized hyperbola term contains an explicit polar operator. Write

`S_N^ren=S_N-C_N(D)`. Then

```
H_M,N^ren
 = H_M,N - L_MC_N(D) + [X,C_N(D)].                               (3.1)
```

The last two terms are explicit. With the Fourier convention of phase 161,

```
[X,C_N(D)] has multiplier
(-log N + 1/(1-s)) C_N(s),       s=1/2+i tau.                     (3.2)
```

Thus `(PC-ren)` separates three pieces:

1. the finite positive-coefficient hyperbola tail `H_M,N`;
2. the polar counterterm, known explicitly;
3. the genuinely small Poisson defect `E_N^ren`.

## 4. Why the polar term is not disposable

The polar correction is of size `N^(1/2)` before cancellation. Dropping it recreates Proposition 1.1. Cancelling it
after taking norms is also invalid: the cross term between `S_N` and `C_N(D)` is of the same order as each square.

On complete Weil data the pole is the Tate `H^0/H^2` block. On primitive data the two scalar moments vanish in the
final quadratic form, but it does not follow that the operator `C_N(D)` vanishes on `P_T`. A proof of that stronger
statement would be false. The cancellation must be performed at form level after all cross terms are retained.

Theorem 2.2 adds the useful refinement: on `P_T`, the polar term is a translated **boundary layer** of the same finite
width `2T`. Thus it may be retained exactly in a compressed calculation; no asymptotic estimate of it is required.

## 5. Revised next lemma

**Later corpus-audit note.** `R161_004` shows that the scalar-positive reading of the target below collides with
Paper 41 C4--C5 and that its positive divisor-fibre reading collides with the phase-104/106 and phase-121 no-go
results. It is retained here as the historical target after the polar repair; the active successor is `L161.3`, the
oriented first-contact exterior port in `R161_005`--`R161_006`.

The raw L161.1 of `R161_002` is too optimistic if it uses `E_N`. Replace it by:

**Lemma target L161.2 (polar-oriented boundary law; OPEN).** For `F in P_T`, find a canonical signed discrete
derivative/weighting in `N` such that inserting `(PC-ren)` yields

```
a_T(F) = positive Poisson-boundary energy + explicit polar cancellation + R_T(F),
```

where `R_T(F)>=0` follows from the positive hyperbola coefficients and no spectral gap is used.

Required tests:

- the signed derivative must recover the terminal jump `-log p` at every prime;
- the polar cross term must cancel exactly using `A(F)=B(F)=0`, not by an estimate;
- the formula must retain the interior defects `delta_a(k)` of every falsifier;
- taking absolute values anywhere before the terminal jump is forbidden, because it returns to `A_T^2`.

By Theorem 2.2 the target can equivalently be called a **quadratic Euler–Maclaurin discrepancy inequality**: its
positive side must come from Poisson applied to `(integer lattice) - (positive continuum)`, while its oriented side
must retain the terminal jumps of the divisor hyperbola.

## 6. Status

- finite joint identity: **PROVED**;
- raw-square sign-blindness: **PROVED**;
- positive-weight tail no-go: **PROVED**;
- raw Poisson truncation obstruction: **PROVED**;
- polar-renormalized defect convergence: **PROVED on Schwartz data**;
- polar-oriented boundary law L161.2: **RETIRED in scalar-positive and positive-fibre forms by `R161_004`**;
- oriented first-contact exterior port L161.3: **OPEN**.

This is genuine progress in localisation: the possible sign is now confined to the oriented interaction between the
terminal divisor-hyperbola jump and the polar-renormalized Poisson boundary.
