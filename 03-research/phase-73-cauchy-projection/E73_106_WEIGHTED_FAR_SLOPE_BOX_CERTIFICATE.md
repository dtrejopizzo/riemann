# E73.106 - Weighted FAR-SLOPE box certificate

## 1. Purpose

E73.105 shows that the weighted main budget:

```text
L^5 sum_{gamma_k in D_3(A,L)} FAR_k Q_k
```

has large finite slack.  This note states the interval certificate needed to prove it on a natural
cluster box.

## 2. Cluster box

Fix a natural-height box:

```text
B = [alpha_0,alpha_1] x [tau_0,tau_1] x {m}
```

with:

```text
a=alpha+i tau.
```

The finite CCM data at scale `L` are fixed:

```text
d_n, xi_n, P_x, D_x, Div(P_x), gamma_k.
```

Only the geometric Hermite weight varies over `B`.

## 3. Interval enclosures

For every critical row `gamma_k` in the finite natural-height window, compute interval enclosures:

```text
W_k(B,L)       >= sup_{a in B} e^(alpha L)G_theta,m(a,i gamma_k)|1-e^(i gamma_k L)|,
R_k(L)         =  dist(-gamma_k,Div(P_x)),
Q_k(L)         =  |P_x(-gamma_k)|/(|D_x(-gamma_k)|R_k(L)).
```

`R_k` and `Q_k` do not vary over `B`; they are finite rational/algebraic scale data.

Define:

```text
FAR_k^+(B,L):=W_k(B,L)R_k(L),
B_k^+(B,L):=L^5 W_k(B,L)R_k(L)Q_k(L).
```

Since `R_k Q_k=|P_x(-gamma_k)|/|D_x(-gamma_k)|`, this is:

```text
B_k^+(B,L)=L^5 W_k(B,L)|P_x(-gamma_k)|/|D_x(-gamma_k)|.
```

## 4. Certifying the FAR3 set

Let `S` be a proposed three-row set.  It is certified as the FAR3 set on `B` if:

```text
inf_{k in S} FAR_k(B,L) > sup_{j notin S} FAR_j(B,L).
```

In interval form, using lower and upper enclosures:

```text
min_{k in S} FAR_k^-(B,L) > max_{j notin S} FAR_j^+(B,L).
```

If this strict separation fails, subdivide the box or certify all possible competing three-row sets.

## 5. Weighted FAR-SLOPE box certificate

For every certified possible selected set `S`, prove:

```text
sum_{k in S} B_k^+(B,L) <= C_main.
```

With `C_main=1`, this gives:

```text
sum_{k in D_3(A,L)} W_k(A,L)|P_x(-gamma_k)|/|D_x(-gamma_k)|
<= L^-5
```

for every `A in B`.

## 6. Theorem

**Theorem 106.1.**  If the weighted FAR-SLOPE box certificate holds on a cluster box `B`, then
`FAR3-MAIN-RAT(A,L)` holds for every `A in B`.

*Proof.*  For each `A in B`, the selected FAR3 set is one of the certified sets `S`.  By the upper
enclosures:

```text
L^5 sum_{k in S} W_k(A,L)|P_x(-gamma_k)|/|D_x(-gamma_k)|
<=
sum_{k in S} B_k^+(B,L)
<= C_main.
```

Divide by `L^5`.  This is `FAR3-MAIN-RAT`. `□`

## 7. Why this is the right proof object

This certificate preserves the weighted structure:

```text
sum FAR_k Q_k.
```

It does not replace it by:

```text
sum FAR_k * max Q_k,
```

which E73.104 shows is too crude in low windows.

## 8. Status

```text
finite certificate: stated;
tested constant: C_main=1 has slack in E73.105;
remaining: implement interval enclosures W_k(B,L) and FAR selection separation.
```
