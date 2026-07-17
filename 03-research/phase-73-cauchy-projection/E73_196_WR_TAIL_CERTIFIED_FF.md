# E73.196 - WR tail certification for the finite-frequency endpoint

Date: 2026-07-14.

## 1. Purpose

E73.195 shows that the finite-frequency certificate reaches the residual
scale when the WR series is taken deep enough.  This note asks whether the
existing rigorous tail bounds from E73.184--E73.185 are sharp enough for that
certificate.

## 2. Tail object

For

```text
B(y)=sum c_omega e^(i omega y)+y sum l_omega e^(i omega y),
F(y)=e^(y/2)B(y)-B(0),
```

the omitted WR tail after `R` odd-exponential terms and Taylor acceleration
to order `K` is bounded by

```text
|Tail_{R,K}| <= M_{K+1}^{grp}
               sum_{r>=R}(2r+1)^(-(K+2)).
```

Here

```text
M_s^{grp}
<= e^(L/2) sum_omega
 ( |c_omega lambda_omega^s+s l_omega lambda_omega^(s-1)|
   + L |l_omega lambda_omega^s| ),
lambda_omega=1/2+i omega.
```

## 3. Result

The grouped bound is rigorous, but remains conservative at the final residual
scale.  It correctly dominates the observed tail, yet can be several powers of
`L` above the signed tail needed to certify `FF-SECOND-ABEL`.

This does not invalidate the finite-frequency certificate.  It means the final
interval implementation should not rely only on a coefficient-absolute local
WR tail.  It needs one of:

```text
1. much larger R, with the elementary tail bound;
2. a signed/special-function evaluation of the infinite WR tail;
3. interval arithmetic applied directly to the closed polygamma/Lerch form.
```

## 4. Status

```text
proved: grouped WR tail bound applies to the finite-frequency endpoint;
observed: bound is safe but conservative;
open: replace the absolute tail by a signed special-function tail or use
      large-R interval summation.
```
