# R161_037 — Saturation alone forces `F=0`; no differentiated strong graph limit is needed

## 0. Verdict

The two open statements listed in `R161_036` are not independent. If first contact saturates the finite coherent
parallelogram, the norm of the orientation difference tends to zero. Pointwise differentiated Euler--Maclaurin
convergence then identifies its only possible Fourier limit. A subsequence argument forces the limiting completed
jet times `Fhat` to vanish almost everywhere. Since that jet is a nonzero analytic multiplier with a null zero set,
`F=0`.

Thus differentiated **strong graph convergence is unnecessary for closure**. The sole remaining theorem is the
finite polar/crossed-Tate saturation of `R161_035`.

## 1. Finite multipliers

Let

```
B_N=U_N^ren-V_N^ren
   =K_N^renFcal-JK_N^ren.                               (1.1)
```

By `R161_036`, its Fourier-reflection multiplier is

```
b_N(tau)=-Z_N'(s)u(s)+Z_N'(1-s),
s=1/2+i tau.                                           (1.2)
```

For every fixed `tau`, differentiated Euler--Maclaurin gives

```
Z_N'(s)->zeta'(s),
Z_N'(1-s)->zeta'(1-s).                                 (1.3)
```

Hence

```
b_N(tau)->b_infty(tau)
 :=-zeta'(s)u(s)+zeta'(1-s)
 =-2zeta'(s)u(s)-zeta(s)u'(s),                         (1.4)
```

where the last equality is the differentiated functional equation.

Only fixed-frequency convergence is asserted in (1.3); no uniform multiplier estimate is needed below.

## 2. Norm saturation implies almost-everywhere annihilation

Assume the first-contact saturation target of `R161_035`:

```
D_N^coh(F)=1/4||B_NF||_2^2 ->0.                        (2.1)
```

Plancherel gives

```
||b_N(tau)Fhat(-tau)||_(L2_tau)->0.                     (2.2)
```

Every sequence converging to zero in `L2` has a subsequence converging to zero almost everywhere. Choose such a
subsequence `N_j`. For almost every `tau`, (1.3) and (2.2) then give simultaneously

```
b_(N_j)(tau)Fhat(-tau)->b_infty(tau)Fhat(-tau),
b_(N_j)(tau)Fhat(-tau)->0.
```

Therefore

```
boxed: b_infty(tau)Fhat(-tau)=0 for almost every tau.    (2.3)
```

This argument deliberately avoids dominated convergence.

## 3. The completed jet is nonzero almost everywhere

The function

```
b_infty(s)=-2zeta'(s)u(s)-zeta(s)u'(s)                 (3.1)
```

is meromorphic in a strip containing every compact critical-line segment away from the standard Gamma poles. It
is not identically zero. Indeed, if it vanished identically on a connected open set where `zeta u` is regular,
then

```
(zeta(s)^2u(s))'
 =zeta(s)[2zeta'(s)u(s)+zeta(s)u'(s)]
 =0.                                                    (3.2)
```

Thus `zeta^2u` would be constant there and hence meromorphically constant, contradicting either the pole of zeta
at `s=1` or any nontrivial zero.

The zeros of a nonzero meromorphic function on the critical line are discrete unless the line is contained in its
analytic zero set, which would imply the excluded identity by analytic continuation. Hence

```
measure{tau:b_infty(1/2+i tau)=0}=0.                    (3.3)
```

Equations (2.3)--(3.3) imply `Fhat=0` almost everywhere. By Plancherel,

```
boxed: F=0.                                             (3.4)
```

## 4. Closure consequence

The implication is now unconditional after saturation:

```
first-contact coherent saturation
 -> ||B_NF||_2->0
 -> b_infty Fhat=0 a.e.
 -> F=0
 -> no first contact
 -> row D by the existing nesting/cofinal theorem.       (4.1)
```

This route is stronger than evaluation at the critical zeros and avoids simplicity or zero-density input. It uses
only the already proved pointwise differentiated Euler--Maclaurin asymptotic and Plancherel.

## 5. Exact remaining theorem

It remains to derive, from finite `(PC-ren)` on a parity first-contact state,

```
1/2(||U_N^renF||^2+||V_N^renF||^2)
 -1/4||(U_N^ren+V_N^ren)F||^2 ->0,                    (5.1)
```

with the polar boundary and crossed Tate term retained. By the exact parallelogram this is neither an inequality
nor a limit-identification problem: it is precisely the assertion `||B_NF||_2->0`.

The proof of (5.1) must come from the finite Green pairing. Radicality alone remains insufficient.

## 6. Status

- pointwise differentiated Euler--Maclaurin convergence: **PROVED**;
- subsequence/Fatou-free limit argument: **PROVED**;
- nonvanishing almost everywhere of the completed jet: **PROVED**;
- `D_N^coh(F)->0 => F=0`: **PROVED**;
- differentiated strong graph convergence: **REMOVED AS A REQUIREMENT**;
- first-contact coherent saturation (5.1): **OPEN / SOLE TERMINAL GATE**;
- row D: **OPEN**.
