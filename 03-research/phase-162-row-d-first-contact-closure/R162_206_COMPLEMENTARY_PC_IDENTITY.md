# R162_206 — The complementary Poisson--Chebyshev identity is linearly dependent


Status: **PROVED IDENTITY AND LINEAR NO-GO / GATE 1 OPEN.** Replacing the Poisson difference by the
complementary Poisson sum produces an exact finite identity in which the covariant derivative has
the critical-jet orientation. However, this identity and `(PC)` have the same left side and their
difference is an algebraic zero valid for every source. No linear combination supplies a new
equality-state law.

## 1. Difference and sum histories

On the finite Schwartz core use the notation of R161_001 and put

    E_N=S_N Fcal-JS_N,
    C_N=S_N Fcal+JS_N,
    K_N=-[X,S_N]=L_M S_N-H_(M,N).                       (1.1)

The standard finite anomaly is

    S_N A_M Fcal
      ={X,E_N}-L_M^*E_N-JH_(M,N)-H_(M,N)Fcal.           (PC-)

The identity of R161_041 gives the correctly oriented finite jet

    K_NFcal-JK_N=S_NM Fcal-{X,C_N}.                     (1.2)

## 2. Complementary anomaly

**Theorem 2.1 (complementary PC identity; PROVED).** On the same core,

    S_N A_M Fcal
      ={X,C_N}-L_M^*C_N+JH_(M,N)-H_(M,N)Fcal.           (PC+)

*Proof.* Expand the left side of (1.2) using `K_N=L_MS_N-H_(M,N)`:

    K_NFcal-JK_N
      =L_MS_NFcal-L_M^*JS_N-H_(M,N)Fcal+JH_(M,N).

Since `JS_N=C_N-S_NFcal` and the finite translation sums commute,

    K_NFcal-JK_N
      =(L_M+L_M^*)S_NFcal-L_M^*C_N
       -H_(M,N)Fcal+JH_(M,N).

Compare with (1.2), move `(L_M+L_M^*)S_NFcal` to the left, and use
`A_M=M-(L_M+L_M^*)`. ∎

The sign of `JH_(M,N)` is reversed relative to `(PC-)`, while the `HFcal` sign is unchanged. Thus
`(PC+)` is the natural candidate if one wants the covariant derivative of `C_N`, rather than that of
the small Poisson defect `E_N`.

## 3. Exact dependence

Subtract `(PC-)` from `(PC+)`. Because

    C_N-E_N=2JS_N,                                      (3.1)

one obtains

    0={X,2JS_N}-L_M^*(2JS_N)+2JH_(M,N),                 (3.2)

or

    {X,JS_N}-L_M^*JS_N+JH_(M,N)=0.                      (3.3)

Equation (3.3) is an algebraic identity: using `XJ=-JX`,
`JL_M=L_M^*J`, `H_(M,N)=L_MS_N-K_N`, and `[X,S_N]=-K_N`, its left side
vanishes term by term. It contains no first-contact hypothesis.

Adding the two identities is equally redundant. Since

    C_N+E_N=2S_NFcal,                                   (3.4)

their half-sum reduces to the defining expansion of `S_NA_MFcal`.

**Corollary 3.1 (linear-span obstruction; PROVED).** The affine span of `(PC-)` and `(PC+)` contains
only `(PC-)` plus the universal zero (3.3). In particular, no scalar linear combination can turn
Poisson control of `E_N` into independent control of the critical orientation carried by `C_N`.

## 4. Consequence after physical compression

Applying `P_T`, primitive projection, Tate correction, or the right/left exterior split preserves
(3.2), provided every resulting block is retained. Dropping a block can make `(PC+)` look independent,
but the omitted block is exactly the support commutator/exterior correlation isolated in
R161_057--R161_060.

Thus physical compression does not convert the algebraic dependence into a second equation. It only
relocates the universal cancellation among:

- the two one-sided integer-minus-continuum discrepancies;
- the polar boundary layer;
- the crossed Tate endpoints;
- the wrong-side exterior history.

This explains the orientation obstruction of R161_041 in a stronger form: the correctly oriented
jet identity exists at finite level, but it is not independent of `(PC-ren)`.

## 5. Remaining possibility

After R162_205 and Corollary 3.1, neither literal Green substitution nor a second *linear* PC equation
can close Gate 1. Any further use of the finite anomaly must introduce information not present in its
linear span. The remaining algebraic possibility is a genuinely nonlinear two-parameter identity
whose mixed term:

1. is evaluated before setting `a=Lambda`;
2. retains the odd Ward defect `b_a` in one direction;
3. uses an independent physical deformation in the other direction;
4. reduces at `a=Lambda` to the coherent critical-jet energy rather than to the symmetric completed
   commutator.

No such mixed identity is asserted here.

## 6. Exact status

- complementary identity `(PC+)`: **PROVED**;
- exact dependence `(PC+)-(PC-)=(3.3)`: **PROVED**;
- independent coherent-difference conservation law in the linear PC span: **IMPOSSIBLE**;
- nonlinear two-parameter identity: **OPEN**;
- Gate 1 and row D: **OPEN**.
