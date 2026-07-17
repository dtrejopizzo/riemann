# E72.338 -- PACK-SMOOTH is too strong; replace by paired oscillatory smoothness

**Purpose.** Audit the sufficient condition `PACK-SMOOTH` introduced in E72.335--E72.337. It is a
valid sufficient condition, but it is too strong for the transformed route: absolute variation of the
finite packet destroys the same exponential cancellation that the route was designed to preserve.

## 1. Complete-mesh warning

For the complete mesh, E72.318 gives

```text
A_z^infty(r):=(1-e^(zL))sum_{m in Z} e^(id_mr)/(iz-d_m)
= iL e^(z(L-r)).
```

If `Re z=sigma>0`, then

```text
int_0^L |A_z^infty(r)|dr
= L int_0^L e^(sigma(L-r))dr
~ L e^(sigma L)/sigma.
```

Therefore any gate requiring

```text
int |A_z| <= L^B
```

or an absolute `L^1` bound for `(B_z^M)''` cannot hold in right shifted strips. It would demand the
impossible pointwise tail cancellation already rejected in E72.331.

## 2. What remains true

E72.335 remains useful only as a formal integration-by-parts identity:

```text
Pair_z^M(w)=M_z^M(w)+M_z^M(-w)
= (1/w)int_0^L [e^(-wy)-e^(wy)](B_z^M)'(y)dy.
```

But the next estimate must keep this oscillatory/exponential pairing. It must not take

```text
int |(B_z^M)''(y)|dy
```

as the primary object.

## 3. Replacement gate

Replace `PACK-SMOOTH` by:

```text
POSC:
for zero-avoiding outside contours Gamma_T,
|int_{Gamma_T} [ (1/w)int_0^L (e^(-wy)-e^(wy))(B_z^M)'(y)dy ]
   Z'(w)/Z(w) dw|
<= C_K L^B.
```

Equivalently, after interchanging the finite `y` integral and the contour,

```text
POSC:
|int_0^L (B_z^M)'(y)
   [ int_{Gamma_T} (e^(-wy)-e^(wy))/w * Z'(w)/Z(w)dw ]
 dy|
<= C_KL^B.                                             (1)
```

The bracket is an explicit odd zero-counting kernel. This is the correct object: it contains the
pairing `w ~ -w` before any absolute value is taken.

## 4. Endpoint derivative identities still matter

E72.336 is still load-bearing. Its endpoint identities show that boundary terms produced by
integration by parts reduce to the rank-one scalar

```text
-(2/L)(sum_m a_m(z))(sum_n xi_n),
```

rather than a full incoherent matrix sum.

But the bulk estimate must be `(POSC)`, not total variation.

## 5. Updated route

The transformed tail gate is now:

```text
POSC => UREM-POLY.
```

`PACK-SMOOTH` should be kept only as an overly strong sufficient condition and not as the main target.

## 6. Status

```text
proved: absolute PACK-SMOOTH is too strong in right shifted strips;
replaced: UREM-POLY target by paired oscillatory smoothness POSC;
kept: endpoint rank-one identities from E72.336 as boundary control.
```
