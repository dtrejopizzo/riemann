# E80.003 - Bilateral relative determinant equivalence

## 1. Setup

Fix `L>0`.  Let `T_{L,N}` be a rational function with real coefficients whose
poles and zeros are real.  For

```text
D = {s in C : Re s>1},
u=s-1/2,
```

define

```text
C^raw_{L,N}(s)
 = sinh(Lu/2)^2 T_{L,N}(iu)T_{L,N}(-iu).              (1.1)
```

All poles and zeros of `T_{L,N}` are real.  Since `Im(iu)=Re u>1/2` and
`Im(-iu)=-Re u<-1/2`, neither transfer factor has a pole or zero on `D`.
Also `sinh(Lu/2)` has no zero there.  Therefore `C^raw_{L,N}` is holomorphic
and zero-free on `D`.

Let `Z^ext_{L,N}` be the external-mesh product and define the core object

```text
C_{L,N}(s)=C^raw_{L,N}(s)/Z^ext_{L,N}(-iu).             (1.2)
```

The restricted external product is also holomorphic and zero-free on `D`.
Hence `C_{L,N}` has the same properties there.

Let `E_L` be the product of E80.002 and put

```text
R_{L,N}(s)=C_{L,N}(s)/E_L(s).                         (1.3)
```

Then `R_{L,N}` is holomorphic and zero-free on `D`.

## 2. Exact derivative identity

### Proposition 2.1

For every `s in D`,

```text
R'_{L,N}(s)/R_{L,N}(s)
 = L coth(Lu/2)
   + i T'_{L,N}(iu)/T_{L,N}(iu)
   - i T'_{L,N}(-iu)/T_{L,N}(-iu)
   - B^ext_{L,N}(s)
   - H_L(s).                                           (2.1)
```

Here

```text
B^ext_{L,N}(s)=d/ds log Z^ext_{L,N}(-iu).              (2.2)
```

For real `s>1`, this reduces to

```text
R'_{L,N}(s)/R_{L,N}(s)
 = L coth(Lu/2)
   + 2 Re(i T'_{L,N}(iu)/T_{L,N}(iu))
   - B^ext_{L,N}(s)
   - H_L(s).                                           (2.3)
```

### Proof

Differentiate the logarithm of (1.1) and subtract the logarithmic derivative
of the external product in (1.2).  The hyperbolic factor contributes
`L coth(Lu/2)`.  The two transfer factors contribute the second and third
terms of (2.1).  The mesh product contributes `-B^ext`.  E80.002 gives
`E_L'/E_L=H_L`.  Subtraction proves (2.1).
For real `u`, real coefficients give
`T_{L,N}(-iu)=conj(T_{L,N}(iu))`, and the transfer terms combine into the real
part in (2.3). `QED`

## 3. Projective oscillation

For a bounded domain `V compactly contained in D` and a positive function
`v` on `V`, set

```text
pOsc_V(v)=inf_{a in R} sup_{s in V}|log v(s)-a|.        (3.1)
```

### Theorem 3.1 - flatness implies derivative identification

Let `K compactly contained in V compactly contained in D`, with `V` simply
connected.  There is a constant `C_{K,V}` such that

```text
sup_{s in K}|R'_{L,N}(s)/R_{L,N}(s)|
 <= C_{K,V} pOsc_V(|R_{L,N}|).                         (3.2)
```

Consequently, projective flatness on `V` along any directed family of indices
implies logarithmic-derivative identification on `K` along the same family.

### Proof

Because `R_{L,N}` is zero-free and `V` is simply connected, choose a
holomorphic logarithm `h=log R_{L,N}`.  Subtract a real constant centering
`Re h` and an imaginary constant fixing `Im h` at one point.  The
Borel--Caratheodory inequality on finitely many disks covering `K`, followed by
Cauchy's derivative estimate, gives

```text
sup_K |h'| <= C_{K,V} osc_V(Re h).
```

Since `h'=R'/R` and `osc_V(Re h)=2pOsc_V(|R|)`, absorb the factor `2` into the
constant. `QED`

### Theorem 3.2 - derivative identification implies normalized flatness

Let `V compactly contained in D` be simply connected and let `s_* in V`.
Assume

```text
R'_{L,N}/R_{L,N} -> 0                                (3.3)
```

locally uniformly on `V`.  Then

```text
R_{L,N}(s)/R_{L,N}(s_*) -> 1                          (3.4)
```

locally uniformly on `V`.  In particular, projective oscillation tends to
zero on every compact subset of `V`.

### Proof

Fix a compact `K` in `V`.  Choose a compact connected set `K_1` in `V`
containing `K`, `s_*`, and rectifiable paths from `s_*` to every point of `K`
with lengths bounded by one constant `M_K`.  A holomorphic logarithm gives

```text
log(R_{L,N}(s)/R_{L,N}(s_*))
 = integral_{s_*}^{s} R'_{L,N}(w)/R_{L,N}(w) dw.
```

The modulus of the right side is at most
`M_K sup_{K_1}|R'_{L,N}/R_{L,N}|`, which tends to zero.  Exponentiation proves
(3.4), and taking real parts gives projective flatness. `QED`

## 4. Exact equivalence along a directed family

### Corollary 4.1

Let `(L_alpha,N_alpha)` be any directed family, including an iterated limit or
a cofinal diagonal.  On nested safe domains, the following statements are
locally equivalent:

```text
1. pOsc(|C_{L,N}/E_L|) -> 0;
2. d/ds log C_{L,N} - H_L -> 0;
3. C_{L,N}(s)/C_{L,N}(s_*)
     -> E_L(s)/E_L(s_*).                              (4.1)
```

This is an equivalence of formulations.  It does not prescribe the
quantification of the indices and does not prove any of them for the zeta CCM
sections.

For the inherited two-scale endpoint it is used as follows:

```text
1. first take N->infinity at fixed L to obtain C_L projectively;
2. then apply (4.1) to C_L/E_L as L->infinity.           (4.2)
```

It must not be read as the stronger assertion that `C_L/E_L` is constant for
each fixed finite `L`.

## 5. Cofinal consequence

Suppose there is a cofinal choice `N=N(L)` for which statement 3 of (4.1)
holds as `L->infinity`.  E80.002 then
gives

```text
C_{L,N(L)}(s)/C_{L,N(L)}(s_*)
 -> [xi(s)/xi(s_*)]^2                                (5.1)
```

locally uniformly on `D`.  On the real safe axis this is exactly `SR-SAFE`.
The normal-family theorem of P76.034 then implies `Omega7`.

Thus RDI, together with the cofinal compatibility already isolated in the
chain, is sufficient for `Omega7`.

## 6. Status

```text
proved:
  C_{L,N} and R_{L,N} are holomorphic and zero-free on Re s>1;
  the exact derivative identity (2.1);
  projective flatness => derivative identification;
  derivative identification => normalized local flatness;
  equivalence of the three relative formulations in (4.1) along any directed
  family;

reduced:
  the arithmetic discriminant to fixed-L projective convergence followed by
  any one outer statement in (4.1), or a common cofinal version;

open:
  RDI-CONV and RDI-ANCHOR;
  its cofinal uniformity;

next:
  prove that coherence and GAP-Z cannot, without an arithmetic normalization,
  identify the limit in (4.1).
```
