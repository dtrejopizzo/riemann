# R161_041 — Orientation audit: the Poisson defect differentiates to the mean, the Poisson sum to the jet

## 0. Verdict

`R161_040` correctly identifies the two exterior histories through the Poisson defect. Its proposed next
differentiation must be corrected: the covariant derivative of the **difference** `E_N=Z_NFcal-JZ_N` produces the
orientation mean `K_NFcal+JK_N`. The desired critical jet `K_NFcal-JK_N` is instead the covariant derivative of the
complementary **sum** `C_N=Z_NFcal+JZ_N`.

Thus a successful quadratic construction must use `E_N` and `C_N` simultaneously. Squaring or differentiating the
small Poisson defect alone has the wrong orientation.

## 1. Sum and difference ports

Put

```
Z=Z_N=S_N^ren,
K=-[X,Z],
E=ZFcal-JZ,
C=ZFcal+JZ.                                             (1.1)
```

Let

```
U=KFcal,
V=JK.                                                   (1.2)
```

The Tate--Beckner relation is

```
XFcal+Fcal X=M Fcal.                                    (1.3)
```

## 2. Derivative of the difference

The phase-161 calculation already gives

```
{X,E}=ZM Fcal-U-V.                                      (2.1)
```

Equivalently,

```
boxed: U+V=ZM Fcal-{X,E}.                               (2.2)
```

This is the mean identity of `R161_035`.

## 3. Derivative of the sum

For the first term,

```
{X,ZFcal}=ZM Fcal-KFcal.                                (3.1)
```

For the reflected term, use `XJ=-JX`:

```
{X,JZ}=XJZ+JZX
       =-JXZ+JZX
       =-J[X,Z]
       =JK.                                             (3.2)
```

Adding (3.1)--(3.2) proves:

### Theorem 3.1 (sum derivative is the critical jet)

```
boxed: U-V=ZM Fcal-{X,C}.                               (3.3)
```

Therefore the coherent square can be written exactly as

```
D_N^coh(f)
 =1/4||[Z_NM Fcal-{X,C_N}]f||^2.                       (3.4)
```

No limit or functional equation is used.

## 4. Mellin check

Let

```
e_N(s)=Z_N(s)u(s)-Z_N(1-s),
c_N(s)=Z_N(s)u(s)+Z_N(1-s).                            (4.1)
```

Differentiation gives

```
-e_N'(s)+Z_N(s)u'(s)
 =-Z_N'(s)u(s)-Z_N'(1-s)=U_N+V_N,                     (4.2)

-c_N'(s)+Z_N(s)u'(s)
 =-Z_N'(s)u(s)+Z_N'(1-s)=U_N-V_N.                     (4.3)
```

This confirms the physical-space signs.

## 5. Consequence for the exterior-history route

The exact identity of `R161_040`,

```
(I-P)ZFcal f-epsilon(I-P)Z*f=(I-P)Ef,                 (5.1)
```

is valuable because it controls the difference history. But differentiating its norm controls the mean jet
`U+V`, not the critical jet `U-V`. Therefore the proposed equation `R161_040(6.1)` is not justified as written and
is withdrawn.

The missing quadratic must couple the controlled difference `E` to the covariant derivative of the sum `C` before
taking a real part. Schematically the only correctly oriented bilinear object is

```
Re < exterior E f,
       exterior [ZM Fcal-{X,C}]f >,                   (5.2)
```

with polar and Tate corrections included. Whether (5.2) completes to `||U-V||^2` is the next calculation; it is
not asserted here.

## 6. Why this is the simultaneous construction

The two identities have complementary roles:

```
Poisson/Fourier:       E=ZFcal-JZ is the small/intertwining defect;
Chebyshev critical jet: U-V=ZM Fcal-{X,C};
divisor synthesis:     K=L_MS-H_M,N.                         (6.1)
```

Using only `E` returns to a vanishing linear commutator. Using only `C` has no Poisson control. A new term can arise
only from their mixed compressed pairing, where moving support prevents formal adjoint cancellation.

## 7. Status

- exact exterior-history identity for `E`: **PROVED in `R161_040`**;
- derivative of `E` gives `U+V`: **PROVED**;
- derivative of `C` gives `U-V`: **PROVED**;
- former differentiated-defect target `R161_040(6.1)`: **WITHDRAWN / WRONG ORIENTATION**;
- mixed compressed `E`--`C` Green completion: **OPEN / NEXT GATE**;
- row D: **OPEN**.
