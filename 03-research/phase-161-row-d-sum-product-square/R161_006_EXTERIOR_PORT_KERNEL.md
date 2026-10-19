# R161_006 — Exact kernel of the renormalised exterior Poisson port

## 0. Verdict

The remaining port in `R161_005` admits an elementary exact decomposition. In the `S_N` orientation, its discrete
part samples only the **right** exterior tail, whereas the polar continuum contains:

1. the Euler--Maclaurin continuum under that right tail; and
2. one rank-one scalar from the entire left exterior tail, in the Tate direction `e^(-t/2)`.

Reflection exchanges left and right. Thus the opposite exterior tail is not a second bulk discrepancy: it enters
through an explicit Tate scalar and must be cancelled before any norm is taken. What survives is a one-sided
integer-minus-continuum boundary sampling operator. No sign is claimed.

## 1. Setup

Let `I_T=(-T,T)`, `P=P_T`, and let `g=(1-P)g` satisfy the integrability needed below. Put

```
a_-(g)=integral_(-infinity)^(-T) e^(y/2)g(y)dy.                    (1.1)
```

For `t in I_T`, define the right-tail discrepancy

```
Delta_(N,T)^R g(t)
 := sum_(e^(T-t)<n<=N) n^(-1/2)g(t+log n)
    -e^(-t/2) integral_T^(t+log N) e^(y/2)g(y)dy,                 (1.2)
```

where the integral is declared zero when `t+log N<=T`.

## 2. Exact port formula

Recall

```
S_N^ren=S_N-C_N(D),
(C_N(D)g)(t)=e^(-t/2)integral_(-infinity)^(t+log N)e^(y/2)g(y)dy.
```

**Theorem 2.1 (one-sided exterior decomposition; PROVED).** For almost every `t in I_T`,

```
(P S_N^ren(1-P)g)(t)
 = Delta_(N,T)^R g(t)-e^(-t/2)a_-(g).                            (2.1)
```

*Proof.* Since `n>=1` and `t>-T`, the point `t+log n` never lies in the left exterior. Since `g` vanishes on
`I_T`, the discrete term is nonzero only when `t+log n>T`, equivalently `n>e^(T-t)`. This gives the sum in (1.2).

For the continuum integral, split `(-infinity,t+log N]` into the left exterior, the window and the right exterior.
The window contribution is zero. The left contribution is (1.1), and the right contribution is the integral in
(1.2). Subtracting `C_N(D)` proves (2.1). ∎

For the first-contact exterior Weil port `g=ell_T(F)=(1-P)A_MF`, formula (2.1) becomes

```
B_(N,T)^ren(F)(t)
 = Delta_(N,T)^R ell_T(F)(t)
   -e^(-t/2)a_-(ell_T(F)).                                      (2.2)
```

This is an exact formula for the unknown term in `R161_005`, equation (3.1).

## 3. Reflected orientation

Put `S_(N,-)^ren=J S_N^ren J` and

```
a_+(g)=integral_T^infinity e^(-y/2)g(y)dy.                       (3.1)
```

Reflection of Theorem 2.1 gives a left-tail discrepancy `Delta_(N,T)^L` satisfying

```
P S_(N,-)^ren(1-P)g
 = Delta_(N,T)^L g-e^(t/2)a_+(g).                               (3.2)
```

The precise left formula is obtained from (1.2) by `t->-t`, `y->-y`, and `g->Jg`. Therefore the two orientations
carry the two exterior tails separately, while their cross-tail contamination is exactly the two-dimensional Tate
span.

## 4. Consequence for primitive first contact

The primitive conditions are imposed on `F`, not automatically on `ell_T(F)`. Hence neither scalar in (2.2) or
(3.2) may be set to zero separately. At first contact they must be combined with the explicit term
`P S_N^ren r` and the crossed Tate system of phase 121.

This explains two earlier failures.

- Dropping the polar counterterm loses the cross-tail Tate scalar and recreates the order-`sqrt(N)` oscillation.
- Squaring either oriented port before combining the Tate scalars destroys their signed cancellation and returns to
  the Volterra/Stieltjes wrong-sign completion.

After the exact two-Tate cancellation, the genuinely nonlocal remainder is only

```
Delta_(N,T)^R ell_T(F),   Delta_(N,T)^L ell_T(F).                 (4.1)
```

These are one-sided sampling discrepancies of the exterior Weil image, not positive measures and not finite
divisor histories.

## 5. The next calculation

The operator in (1.2) is a translated Euler--Maclaurin remainder with a moving lower endpoint `e^(T-t)`. Its global
Mellin multiplier would be `Z_N(s)`, but the moving endpoint is precisely the compression defect and must not be
replaced by that multiplier.

The next admissible step is to compute the one-sided Mellin boundary value of the pair (4.1) and its commutator with
`Q`. The target coefficient at a simple critical zero is `zeta'(rho)K_F(rho-1/2)`. A calculation yielding only
`zeta(rho)K_F(rho-1/2)=0` is sign-free and supplies no information; a calculation that divides by `zeta` before
proving range membership is circular.

## 6. Status

- exact right-port decomposition (2.1): **PROVED**;
- exact reflected decomposition (3.2): **PROVED**;
- identification of all cross-tail terms with the Tate span: **PROVED**;
- cancellation with the first-contact Tate forcing: **not yet computed**;
- extraction and annihilation of the critical normal coefficient: **OPEN**.
