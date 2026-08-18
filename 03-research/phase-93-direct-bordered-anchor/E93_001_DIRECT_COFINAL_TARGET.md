# E93.001 - Direct cofinal bordered target

## 1. Finite projective object

Let

```text
N_(L,N)(z)
 =det[[M_(L,N),b_(L,N)],
      [h_(L,N,z),1]]                                  (1.1)
```

be the full bordered determinant of E92.006.  Put `u=s-1/2` and define the
bilateral normalized numerator

```text
B_(L,N)(s;s_*)
 =[N_(L,N)(iu)N_(L,N)(-iu)]
  /[N_(L,N)(iu_*)N_(L,N)(-iu_*)].                    (1.2)
```

Let `A_(L,N)(s)` be the explicit mesh and hyperbolic factor of E81.002.
The exact core ratio is

```text
C_(L,N)(s)/C_(L,N)(s_*)
 =[A_(L,N)(s)/A_(L,N)(s_*)]B_(L,N)(s;s_*).           (1.3)
```

All determinants of the inner matrix cancel from (1.2).

## 2. Directed family

Let `alpha` range over any directed set for which

```text
L_alpha->infinity,
N_alpha->infinity,                                   (2.1)
```

with the mesh-resolution condition required by the finite characteristic.
No iterated order is imposed.

Define the direct relative ratio

```text
R_alpha(s;s_*)
 ={C_(L_alpha,N_alpha)(s)/C_(L_alpha,N_alpha)(s_*)}
  /{E_(L_alpha)(s)/E_(L_alpha)(s_*)}.                 (2.2)
```

The single target is

```text
DIRECT-BORDERED-ANCHOR:
R_alpha(s;s_*)->1                                    (2.3)
```

locally uniformly on `Re s>1`.

## 3. Logarithmic form

Because every finite ratio is zero-free on the safe domain, (2.3) is locally
equivalent to

```text
partial_s log C_(L_alpha,N_alpha)(s)-H_(L_alpha)(s)
 ->0,                                                 (3.1)
```

together with normalization at `s_*`.  The derivative of the bordered
determinant may be computed by cofactors as in E92.004, without a singular
cluster inverse.

## 4. Status

```text
defined exactly:
  direct cofinal bordered ratio and its logarithmic form;

open:
  DIRECT-BORDERED-ANCHOR.
```

