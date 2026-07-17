# E72.389 - D2BV packet bounds

## 1. Purpose

E72.388 reduces `SFREQ` to the second-variation gate

```text
D2BV-K:
int_0^L e^(ct)(|B_z^M|+|(B_z^M)'|+|(B_z^M)''|)dt
<= C_K e^((c+sigma_K)L)L^B.
```

E72.385 already proves the `B` and `B'` parts at the required scale.  This note proves the `B''`
part using the Dirichlet-Cauchy packet identities.

## 2. Second derivative structure

E72.337 gives

```text
A_z'=-zA_z-iE_zD_M,
(A_z^#)'=zA_z^#+iE_zD_M,
```

and therefore

```text
A_z''=z^2A_z+izE_zD_M-iE_zD_M',
(A_z^#)''=z^2A_z^#+izE_zD_M+iE_zD_M',
```

up to the harmless sign convention in the reflected derivative.  Differentiating the finite packet
twice expresses `(B_z^M)''` as a sum of:

```text
Volterra terms with A_z and X,
Volterra terms with E_z D_M and X,
Volterra terms with E_z D_M' and X,
boundary terms involving A_z,D_M,X.
```

Thus it is enough to bound the three Volterra families.

## 3. Parseval norms

E72.385 gives

```text
||A_z||_2 <= C_K L e^(sigma_K L),
||D_M||_2 = sqrt(L(2M+1)).
```

For

```text
D_M'(r)=sum_{|m|<=M} i d_m e^(id_mr),
```

Parseval gives

```text
||D_M'||_2^2
=L sum_{|m|<=M} d_m^2
=L (2pi/L)^2 2 sum_{m=1}^M m^2
<= C M^3/L.                                           (1)
```

Hence

```text
||D_M'||_2 <= C M^(3/2)L^(-1/2).                      (2)
```

## 4. Volterra estimate

The general estimate from E72.385 is:

```text
int_0^L |P(r)|(K_c|X|)(r)dr
<= C_c sqrt(L)e^(cL)||P||_2.                          (3)
```

Apply (3) to `A_z`, `D_M`, and `D_M'`.

The `A_z` part contributes:

```text
C_K L^(3/2)e^((c+sigma_K)L).
```

The `E_zD_M` part contributes:

```text
|E_z| C sqrt(L)e^(cL)||D_M||_2
<= C_K L sqrt(M)e^((c+sigma_K)L).
```

The `E_zD_M'` part contributes:

```text
|E_z| C sqrt(L)e^(cL)||D_M'||_2
<= C_K M^(3/2)e^((c+sigma_K)L).                       (4)
```

If the active bandwidth is polynomial in `L`, all three are polynomial times
`e^((c+sigma_K)L)`.

Boundary terms are lower order combinations of the same endpoint packets and are bounded by the same
norms via Cauchy-Schwarz.

## 5. Theorem

### Theorem 72.389

For every fixed compact shifted strip `K` and `c>0`, assume the active bandwidth satisfies

```text
M <= C L^p.
```

Then

```text
int_0^L e^(ct)|(B_z^M)''(t)|dt
<= C_K e^((c+sigma_K)L)L^B.
```

Consequently `D2BV-K` and `SV-K` hold.

### Proof

Use the differentiated packet representation and the estimates (1)--(4).  Add the already proved
`B` and `B'` bounds from E72.385. `QED`

## 6. Status

```text
proved: D2BV-K under polynomial active bandwidth;
feeds: SV-K in E72.388;
therefore: SFREQ is closed under polynomial active bandwidth and natural height.
```
