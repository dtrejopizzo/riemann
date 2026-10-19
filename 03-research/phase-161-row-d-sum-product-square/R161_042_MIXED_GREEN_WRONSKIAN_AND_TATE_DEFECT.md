# R161_042 — The mixed sum--difference pairing is the exterior Green moment plus a Tate defect

## 0. Verdict

The correctly oriented mixed object from `R161_041` has an exact Green identity. Pairing the Poisson difference
with `X` applied to the complementary sum cancels all cross-orientation terms and leaves the difference of the two
oriented first moments. After right/left exterior compression this is a same-sign positive distance-to-boundary
energy.

The only term preventing immediate use of the critical-jet identity is the second half of the anticommutator,
`C_NXf`. Since multiplication by `X=t` does not preserve the two Tate moment conditions, its primitive correction
is finite-dimensional. `R161_043` shows that this Tate correction has parity opposite to the forcing and hence its
literal forcing/collar pairing vanishes; it is not the positive same-parity square anticipated below.

## 1. Abstract Green cancellation

Let `X=X*` and let `a,d` belong to its form domain. Put

```
e=a-d,          c=a+d.                                  (1.1)
```

Then

### Lemma 1.1 (sum--difference Green identity)

```
boxed: Re<e,Xc>=<a,Xa>-<d,Xd>.                         (1.2)
```

*Proof.* Expand

```
<a-d,X(a+d)>
 =<a,Xa>-<d,Xd>+<a,Xd>-<d,Xa>.
```

The last two terms are conjugates because `X=X*`; their difference has zero real part. QED.

## 2. Application to the two Poisson orientations

Put

```
a_N=Z_NFcal f,
d_N=JZ_Nf,
e_N=E_Nf=a_N-d_N,
c_N=C_Nf=a_N+d_N.                                      (2.1)
```

Lemma 1.1 gives the exact finite identity

```
boxed:
Re<E_Nf,X C_Nf>
 =<Z_NFcal f,XZ_NFcal f>
  -<JZ_Nf,XJZ_Nf>.                                     (2.2)
```

Since `JXJ=-X`, the second term can also be written

```
-<JZ_Nf,XJZ_Nf>=<Z_Nf,XZ_Nf>.                         (2.3)
```

Thus the mixed pairing is the sum of the two oriented first moments before support localization.

## 3. Exterior right/left positivity

Let

```
P_+=1_[T,infinity),       P_-=1_(-infinity,-T].          (3.1)
```

For the physical exterior pieces

```
a_+=P_+a_N,
d_-=P_-d_N,                                               (3.2)
```

one has

```
<a_+,(X-T)a_+> >=0,
<d_-,(-X-T)d_-> >=0.                                    (3.3)
```

Equivalently,

```
boxed:
<a_+,Xa_+>-<d_-,Xd_->
 -T(||a_+||^2+||d_-||^2)

=||(X-T)^(1/2)a_+||^2
 +||(-X-T)^(1/2)d_-||^2 >=0.                            (3.4)
```

After parity/reflection identifies the two exterior ports, (3.4) is the two-sided version of the Sonin--Gamma
excess energy in `R161_014`.

The remaining interior and wrong-side exterior pieces must be retained when (2.2) is compressed; they are not
declared zero here.

## 4. The anticommutator and the source derivative

The critical jet identity of `R161_041` is

```
B_N:=K_NFcal-JK_N=Z_NM Fcal-{X,C_N}.                    (4.1)
```

Pairing with `E_Nf` gives

```
Re<E_Nf,B_Nf>
 =Re<E_Nf,Z_NM Fcal f>
  -Re<E_Nf,XC_Nf>
  -Re<E_Nf,C_NXf>.                                      (4.2)
```

The middle term is evaluated by (2.2). The final term is the source-derivative remainder.

## 5. Why the last term is Tate-typed at first contact

Let `Pi_T` be the primitive projection in the physical window and write

```
PXf=Pi_TPXf+Tau_TPXf,        Tau_T=I-Pi_T.              (5.1)
```

The first term is an admissible primitive test. On a first-contact radical, its Weil pairing with `f` vanishes.
`R161_044` notes that this is exactly the phase-121 horizontal-modulation tautology and cannot kill the mixed term
until the exterior commutator needed to identify it with that Weil pairing has been retained.
The second term belongs to the two-dimensional Tate span. Its coefficients are obtained by pairing `tf` with
`exp(+/-t/2)`, i.e. by derivatives of the two Tate moments. Hence the obstruction created by moving `X` through
the compressed source is exactly finite-dimensional and is the natural location of the crossed Tate matrix.

This section identifies the type of the remainder. The successor parity audit proves that any literal Tate
pairing with the forcing/collar current is zero. The remaining calculation is to show that `(PC-ren)` actually
reduces the term to that literal pairing and to identify the primitive/exterior pieces.

## 6. Precise next calculation

Insert `(PC-ren)` into the first and last terms of (4.2), split every vector into

```
right exterior + primitive interior + Tate interior + left exterior,  (6.1)
```

and retain the polar continuum. The acceptance identity is

```
0=
 ||(X-T)^(1/2)a_+||^2
 +||(-X-T)^(1/2)d_-||^2
 +D_N^boundary(f),                                      (6.2)
```

with `D_N^boundary>=0` the remaining Poisson compression defect. Formula (3.4) proves the signs of the first two
terms. By `R161_043`, the `Xf`-generated Tate term should vanish by opposite parity if the finite pairing has the
claimed literal typing.

Equation (6.2) is not yet proved. The new content of this note is that its infinite-dimensional Green part follows
from the elementary cancellation (1.2); only the source-derivative/Tate coefficient and the residual boundary
pieces remain to be computed.

## 7. Status

- abstract sum--difference Green identity: **PROVED**;
- exact oriented first-moment formula (2.2): **PROVED**;
- same-sign right/left exterior excess (3.4): **PROVED**;
- localization of the `Xf` obstruction to primitive plus Tate components: **PROVED AS A DECOMPOSITION**;
- primitive component as a new equality law: **REJECTED / HORIZONTAL-MODULATION TAUTOLOGY**;
- exact reduction of the Tate component to the opposite-parity zero pairing: **OPEN**;
- sign of all residual boundary pieces: **OPEN**;
- row D: **OPEN**.
