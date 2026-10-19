# R161_013 — First-collar transmission and the failure of the bare differentiated equation

## 0. Verdict

In the first chamber, the differentiated co-Poisson identity does **not** give a second independent equation for
the `2,3,4` collar germ.  It reproduces that germ exactly.  The first-contact equation does give a nontrivial
transmission law: the same finite delay combination equals the interior Gamma--Tate trace immediately before the
endpoint and the product port immediately after it.

Therefore the next load-bearing calculation must retain the nonlocal Gamma half `C Q C` before scalar
supertrace.  Reapplying `[Q,Z]=ZB_+` cannot close the system.

## 1. The finite delay field

For

```
0.8<T<(log 5)/2
```

put

```
Y_3(F)(t)
 =(log 2)/sqrt(2) F(t-log 2)
 +(log 3)/sqrt(3) F(t-log 3)
 +(log 2)/2       F(t-log 4).                         (1.1)
```

Choose `0<delta<min(log 2,log 5-2T)` and extend `F` by zero.  Local finiteness gives

```
B_+F(t)=Y_3(F)(t),       T-delta<t<T+delta,             (1.2)
B_-F(t)=0,               T-delta<t<T.                   (1.3)
```

For (1.2), no `n>=5` is active because `t-log n<-T`.  For (1.3), every `t+log n>T` for `n>=2` after reducing
`delta` if necessary to `delta<log 2`; the zero extension kills all terms.

## 2. Exact transmission law

Let `F` be a parity first-contact state, so on `I_T`

```
(D_Gamma-B_+-B_-)F=r_epsilon.                         (2.1)
```

Equations (1.2)--(1.3) imply on the inner collar

```
Y_3(F)(t)=D_Gamma F(t)-r_epsilon(t),
                         T-delta<t<T.                  (2.2)
```

By `R161_012`, after placing the polar profile beyond `T+delta`, the exterior product port satisfies

```
g_(+,T)^0(t)=Y_3(F)(t),  T<t<T+delta.                  (2.3)
```

Thus (2.2)--(2.3) are the exact endpoint transmission:

```
interior trace: D_Gamma F-r_epsilon
       -- same three-delay field Y_3 -->
exterior trace: g_(+,T)^0.                             (2.4)
```

No boundary value of `F` itself has been assumed.  The statements hold almost everywhere in the two collars and
are compatible with the available `H^s`, `s<1/2`, regularity.

## 3. Audit of the proposed second equation

The global causal identity is

```
[Q,Z_+]F=Z_+B_+F.                                      (3.1)
```

For `T<t<T+delta`, zero extension gives

```
(QZ_+F-Z_+QF)(t)
 =sum_(n>=2) (log n)/sqrt(n) F(t-log n)
 =Y_3(F)(t).                                           (3.2)
```

On the right side of (3.1), the outer `Z_+` has only its identity term in the same collar, and hence also equals
`Y_3(F)(t)`.  Therefore (3.1) reduces to the tautology `(3.2)=(1.1)` and supplies no independent row.

This is a local, exact stop-gate: differentiating the scalar co-Poisson observation once more does not overdetermine
the three translates.

## 4. The surviving Gamma equation

Use the proved decomposition

```
D_Gamma=Q+C_log Q C_log.                              (4.1)
```

Then (2.2) becomes

```
Y_3(F)(t)-tF(t)+r_epsilon(t)
   =(C_log Q C_log F)(t),       T-delta<t<T.           (4.2)
```

Unlike (3.1), equation (4.2) is not a finite-delay identity.  It couples the endpoint collar to the full source
through the additive Fourier/cosine kernel.  It is exactly the cross-place term which disappears if the two
orientations are scalarised too early.

The next target is now unambiguous:

> Combine the exterior Sonin eigenrelation for `g_(+,T)^0` with the interior transmission (4.2), keeping the two
> Tate scalars, and prove either physical zeta-range membership or vanishing of one nonempty product-port collar.

Any calculation using only (3.1), parity and the Tate moments has already lost the new equation.

## 5. Status

- finite inner/outer transmission (2.2)--(2.4): **PROVED**;
- bare differentiated co-Poisson equation as a second collar row: **REJECTED by exact identity**;
- unsupertraced Gamma transmission (4.2): **PROVED as an equation**;
- rigidity consequence of (4.2) plus the Sonin relation: **OPEN**;
- row D: **OPEN**.

