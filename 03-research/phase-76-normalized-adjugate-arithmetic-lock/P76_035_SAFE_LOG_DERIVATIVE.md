# P76.035 - Safe logarithmic derivative endpoint

For `sigma>1/2`, put

```text
M_{L,N}(sigma)=Psi_{L,N}(-i sigma).
```

The critical normalization disappears after differentiation.  Since
`E_+(z)=sin(zL/2)T_+(z)` and `M=|E_+(i sigma)|^2/|E_+(0)|^2`,

```text
d/dsigma log M_{L,N}(sigma)
 =L coth(sigma L/2)
  +2 Re[i T_+'(i sigma)/T_+(i sigma)].          (SL-1)
```

The target is

```text
2 d/ds log Xi(s),  s=1/2+sigma,                 (SL-2)
```

where in `s>1`

```text
d/ds log Xi(s)
 =1/s+1/(s-1)-(1/2)log pi
  +(1/2)digamma(s/2)+zeta'(s)/zeta(s),          (SL-3)

zeta'(s)/zeta(s)=-sum_{n>=2} Lambda(n)n^(-s).
```

Thus `(SL-1) -> (SL-2)` locally uniformly on `sigma>1/2` is a purely
Euler-safe arithmetic identity.  Integrating it between `sigma_0` and
`sigma` proves `SR-SAFE` of P76.034, hence Omega7.

The remaining theorem is named:

```text
SR-LOG:
L coth(sigma L/2)+2 Re[i T_+'(i sigma)/T_+(i sigma)]
 ->2 Xi'(1/2+sigma)/Xi(1/2+sigma).              (SL-4)
```

Unlike the original adjugate endpoint, `(SL-4)` has no determinant scale,
ground-vector phase, critical-line value, or zero list.  Both `T` and `T'`
are finite rational Schur expressions.
