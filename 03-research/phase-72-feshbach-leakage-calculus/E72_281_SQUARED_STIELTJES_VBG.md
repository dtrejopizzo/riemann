# E72.281 -- Squared-Stieltjes form of VBG

**Purpose.** Convert the variance-bracket gate into a positive Stieltjes transform statement.

Let

```text
p_n=xi_n^2,
W_x(t)=sum_n p_n/(t-d_n).
```

This is the Cauchy/Stieltjes transform of the positive finite measure carried by the squared ground
state.

Recall

```text
S_tau(d)=2tau/(tau^2-d^2)=1/(tau-d)+1/(tau+d).
```

Since

```text
W_x(-tau)=sum_n p_n/(-tau-d_n)=-sum_n p_n/(tau+d_n),
```

we have the exact identity

```text
V_x(tau)=<xi_x,S_tau xi_x>
        = W_x(tau)-W_x(-tau).                              (S1)
```

For the vector norm,

```text
||S_tau xi_x||^2
= sum_n p_n [1/(tau-d_n)+1/(tau+d_n)]^2.
```

Using

```text
W_x'(t)=-sum_n p_n/(t-d_n)^2,
```

and

```text
2/((tau-d_n)(tau+d_n))=2/(tau^2-d_n^2)=S_tau(d_n)/tau,
```

gives

```text
||S_tau xi_x||^2
= -W_x'(tau)-W_x'(-tau)+V_x(tau)/tau.                      (S2)
```

Thus VBG is equivalent to controlling `W_x` and `W_x'` at the finite Weyl roots.

## Probe

Run:

```text
python3 E72_281_squared_stieltjes_vbg_probe.py
```

Output:

```text
E72.281 squared-Stieltjes VBG probe
W(t)=sum xi_n^2/(t-d_n): V=W(tau)-W(-tau), ||S_tau xi||^2=-W'(tau)-W'(-tau)+V/tau.
lam L roots maxErrV maxErrNorm2 maxV max||Sxi||
 16 5.545177     7 3.712e-15 4.338e-14 2.057616e-02 1.018889e-01
 20 5.991465     7 1.186e-15 2.617e-15 2.536685e-02 2.200618e-01
 24 6.356108     5 3.145e-16 1.465e-15 1.103267e-02 5.441412e-02
```

## Reading

This does not prove VBG yet, but it changes its type.

Before:

```text
control a singular diagonal operator S_tau near mesh poles.
```

After:

```text
control W_x(tau), W_x(-tau), W_x'(tau), W_x'(-tau)
for the positive squared-ground measure p_n=xi_n^2.
```

This is the correct finite identity for the variance channel.  The remaining VBG theorem can now be
stated as a squared-Stieltjes root estimate:

```text
sup_{0<tau_j<=H}
[-W_x'(tau_j)-W_x'(-tau_j)+(W_x(tau_j)-W_x(-tau_j))/tau_j]
= O_H(L^(2beta))
```

for some `beta<3/2`, preferably `beta=0`.
