# E72.383 - Natural-height wall gate

## 1. Purpose

E72.382 shows that the local prime-window mass is polynomial only if the wall height satisfies

```text
T >= e^L / L^A.
```

This note records the natural choice

```text
T_L=e^L L^A
```

and the compatible right wall

```text
1/2<c<1-sigma_K,
```

where `sigma_K:=sup_{z in K} Re z`.  This choice can control both the local wall mass and the
horizontal contour terms.

## 2. Local mass

With

```text
delta_L=T_L^(-1/2)=e^(-L/2)L^(-A/2),
```

E72.382 gives

```text
int_0^L W_{L,delta_L}(r)dr
=O(L^(-A/2)).                                         (1)
```

Thus the positive local mass obstruction disappears at natural height.

## 3. Horizontal contour estimate

Let

```text
F_z(w)=int_{-L}^{L}e^(wt)f_z(t)dt,
f_z(t)=B_z^M(|t|)1_{|t|<=L}.
```

On the top horizontal side `w=u+iT_L`, `|u|<=c`, integration by parts gives

```text
|F_z(u+iT_L)|
<= [e^(uL)|f_z(L)|+e^(-uL)|f_z(-L)|]/T_L
   + T_L^(-1) int_{-L}^{L} e^(ut)|df_z(t)|.           (2)
```

Since `B_z^M(L)=0`, the endpoint term vanishes.  If the packet has the strip-gauge BV bound

```text
BV-K:
int_{-L}^{L} e^(ct)|df_z(t)| <= C_K e^((c+sigma_K)L)L^B,  z in K,       (3)
```

then

```text
|F_z(u+iT_L)| <= C_K e^((c+sigma_K-1)L)L^(B-A).        (4)
```

Choosing

```text
c+sigma_K<1
```

makes the horizontal contribution polynomial, indeed exponentially decaying up to powers of `L`.

The logarithmic derivative contributes only `O(log T_L)=O(L)` on zero-avoiding horizontal lines, so
the full horizontal trace remains polynomial.

## 4. The natural-height gate

For each compact shifted strip `K` with `sigma_K<1/2`, choose

```text
1/2<c<1-sigma_K,
T_L=e^L L^A.
```

The natural-height wall gate is:

```text
NHW:
BV-K for the actual packet,
signed FarWall control from E72.379,
finite-mesh tail control at height T_L.
```

Then `FWB` follows.

## 5. Theorem

### Theorem 72.383

Assume `sigma_K<1/2`.  If `NHW` holds for some `A` large enough, then `FWB(K,c)` holds.  Consequently,
by E72.376:

```text
PW-Cauchy(K)
```

and hence the transformed Mellin spectral divisibility endpoint of E72.329 follow.

### Proof

The local positive mass is polynomial by (1).  The horizontal contour is polynomial by (2)--(4) and
the standard zero-avoiding bound `Z'/Z=O(log T_L)`.  The prime wall has no infinite prime tail after
Paley inversion (E72.377), and its finite-height error is the weighted quadrature defect of E72.379.
The remaining two assumptions in `NHW` are exactly the signed far-wall and finite-mesh tail terms.
Therefore all terms in `FWB` are polynomial.  E72.376 gives `PW-Cauchy`. `QED`

## 6. Why the restriction `sigma_K<1/2` is natural

The shifted strip variable is `w=s-1/2`.  Nontrivial zeros off the line have `0<Re w<1/2`.  Therefore
any fixed compact off-line cluster lies in a strip with `sigma_K<1/2`, and a wall satisfying

```text
1/2<c<1-sigma_K
```

exists.

## 7. Status

```text
proved: natural height T=e^L L^A neutralizes local mass;
proved: horizontal contour is polynomial under BV-K if c+sigma_K<1;
reduced: FWB to NHW, consisting of BV-K, signed FarWall, and finite-mesh tail at natural height;
open: prove NHW for the actual Feshbach packet.
```
