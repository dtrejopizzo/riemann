# R161_035 — The correct algebraic gate is the coherent two-orientation parallelogram

## 0. Verdict

The direct-sum lift audited in `R161_033` is unnecessary. The derivation of `(PC)` already supplies two global
coherent orientation vectors, with every `k/l` and `kl` interference retained. Applying the two-point variance
identity to those vectors gives an exact nonnegative Poisson-orientation square entirely inside the original
physical Hilbert space.

`Lambda*1=log` first synthesizes every divisor path into `K_N`; additive Poisson/Fourier then compares the two
global orientations `K_NFcal` and `JK_N`. No source label is declared orthogonal. The remaining theorem is a scalar
saturation equality for this coherent parallelogram after polar renormalization and boundary compression.

## 1. The two coherent orientations

Recall

```
K_N=sum_(k<=N)(log k)k^(-1/2)tau_(log k),
E_N=S_NFcal-JS_N.                                       (1.1)
```

On every completed hyperbola `k<=N<=M`, `K_N` is exactly the divisor synthesis of `L_MS_N-H_M,N` by
`Lambda*1=log`. Define

```
U_N=K_NFcal,
V_N=JK_N.                                                (1.2)
```

These are the two terms which occur unrecombined in the proof of `(PC)`.

## 2. Exact source formula for their mean

Equation `R161_001(3.1)` is

```
S_N M Fcal=J K_N+K_NFcal+{X,E_N}.                       (2.1)
```

Therefore

```
boxed: U_N+V_N=S_NM Fcal-{X,E_N}.                       (2.2)
```

For the polar-renormalized operators put `K_N^ren=-[X,S_N^ren]`. The same core algebra gives

```
U_N^ren+V_N^ren
 =S_N^ren M Fcal-{X,E_N^ren},                            (2.3)
```

with `U_N^ren=K_N^renFcal`, `V_N^ren=JK_N^ren`.

## 3. Coherent orientation variance

For any two Hilbert-space vectors `u,v`,

```
1/2(||u||^2+||v||^2)-1/4||u+v||^2
 =1/4||u-v||^2.                                          (3.1)
```

### Theorem 3.1 (coherent sum--product gate)

On the common core,

```
D_N^coh(f)
 :=1/2(||K_N^renFcal f||^2+||JK_N^ren f||^2)
   -1/4||[S_N^ren M Fcal-{X,E_N^ren}]f||^2

 =1/4||(K_N^renFcal-JK_N^ren)f||^2
 >=0.                                                       (3.2)
```

Equality holds if and only if

```
K_N^renFcal f=JK_N^ren f.                                  (3.3)
```

No cross-`k` term has been removed: all such terms occur inside the coherent norms in (3.2).

## 4. Exact role of `Lambda*1=log`

For `M>=N`,

```
K_N=L_MS_N-H_M,N,                                         (4.1)
```

and `H_M,N` has no coefficient on `k<=N`. Thus the order is

```
divisor synthesis by Lambda*1=log
 -> retain the two Fourier orientations
 -> take the two-state coherent variance.                       (4.2)
```

Taking a divisor variance before synthesis gives the old prime-root diagonal; taking a norm after adding the two
orientations loses their difference. Formula (3.2) does neither.

## 5. Compression and leakage

Let `P=P_T` and `f=Pf`. The clean exterior component of (3.2) is

```
D_(N,T)^ext(f)
 =1/4||(I-P)(U_N^ren-V_N^ren)f||^2>=0.                (5.1)
```

All interior and exterior terms must be obtained by applying the same orthogonal decomposition to the three norms
in (3.2); no boundary term may be discarded. The polar-layer derivative in `R161_028` belongs to (5.1), while the
projection of the coherent mean (2.3) produces the Tate collar current.

The exact terminal target is the saturation

```
1/2(||U_N^renf||^2+||V_N^renf||^2)
 =1/4||(U_N^ren+V_N^ren)f||^2+o(1)                    (5.2)
```

in the crossed-Tate first-contact graph limit. By (3.2), (5.2) is equivalent to

```
(U_N^ren-V_N^ren)f ->0.                                (5.3)
```

Its boundary component is the finite precursor of zero scattering leakage.

## 6. Relation to the parity Tate identity

When the compressed mean in (2.3) is paired with the first-contact forcing, its endpoint coefficient is the collar
vector `j=G_TCv`. If the Green expansion produces `epsilon<v,j>`, `R161_032` converts it exactly to `||r||^2`.
Thus the Tate term belongs to the boundary contribution to the mean energy in (5.2), not to an artificial
direct-sum norm. Its sign/order still must be derived from the expansion.

## 7. Noncircularity boundary

Equation (3.2) is proved algebra. Equation (5.2) is not. First-contact radicality supplies a vanishing linear
pairing after primitive projection, whereas (5.2) is equality between second moments. A proof must show that the
finite polarized `(PC-ren)` Green identity is exactly the difference of the two sides of (5.2), including the
polar and crossed-Tate pieces.

Defining that Green identity to be `D_N^coh`, or using the desired scattering law to pass to (5.3), would be
circular.

## 8. Status

- global coherent orientation vectors from `(PC)`: **PROVED**;
- exact source formula for their sum: **PROVED**;
- coherent two-state square (3.2): **PROVED**;
- retention of the full product--ratio Gram: **PROVED**;
- polar/crossed-Tate first-contact saturation (5.2): **OPEN / TERMINAL**;
- identification of (5.3) with physical scattering in the graph limit: **OPEN**;
- row D: **OPEN**.
