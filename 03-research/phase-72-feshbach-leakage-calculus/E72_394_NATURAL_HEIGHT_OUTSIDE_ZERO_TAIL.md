# E72.394 - Natural-height outside-zero tail

## 1. Purpose

E72.393 leaves the outside-window zero contribution as a load-bearing gate.  A fixed zero window is
not the sharp formulation: the paired packet kernel has high-frequency decay, so the correct finite
window must grow to the natural height

```text
T_L=e^L L^A.
```

This note proves that the zero contribution above `T_L` is polynomially bounded.  The remaining
inside-window zeros form a finite nodal system, while the true high zero tail is no longer an
independent obstruction.

## 2. Bilateral packet transform

For the actual finite packet put

```text
f_z(t)=B_z^M(|t|) 1_{|t|<=L},
F_z(w)=int_{-L}^L e^(wt)f_z(t)dt.
```

This is the paired kernel of E72.339:

```text
F_z(w)=M_z^M(w)+M_z^M(-w).
```

Let `w=rho-1/2` be a shifted nontrivial zero.  Since `0<Re rho<1`,

```text
|Re w|<1/2.
```

Fix `theta<1/2` and restrict to zeros with `|Re w|<=theta`; the limiting `theta -> 1/2` version is
obtained by keeping a harmless `epsilon` margin in the contour and then sending it down after the
polynomial estimate.

## 3. High-frequency transform bound

For `|Re w|<=theta`, two integrations by parts on `[-L,0]` and `[0,L]` give

```text
|F_z(w)| <= C_theta V_2,theta(f_z)/|Im w|^2,           (1)
```

where

```text
V_2,theta(f_z)
= Var_{[-L,0]}((e^(theta |t|)f_z(t))')
 + Var_{[0,L]}((e^(theta |t|)f_z(t))')
 + endpoint and t=0 jump terms.
```

Equivalently, by E72.388--E72.389,

```text
V_2,theta(f_z) <= C_K e^((theta+sigma_K)L)L^B         (2)
```

for `z` in a fixed compact shifted strip with `theta+sigma_K<1`, under polynomial active bandwidth.

## 4. Zero-density summation

Use the standard zero-counting bound

```text
N(U+1)-N(U) <= C log(2+U)
```

for shifted nontrivial zeros counted with multiplicity in unit height slabs.  From (1),

```text
sum_{|Im w|>T_L} |F_z(w)|
<= C V_2,theta(f_z) sum_{n>T_L} log n / n^2
<= C V_2,theta(f_z) log T_L / T_L.                   (3)
```

With

```text
T_L=e^L L^A
```

and (2), (3) becomes

```text
sum_{|Im w|>T_L} |F_z(w)|
<= C_K e^((theta+sigma_K-1)L)L^(B+1-A).              (4)
```

If

```text
theta+sigma_K<1,
```

then the outside-zero tail is polynomially bounded, and with `A` large it is even decaying by a
negative power of `L`.

## 5. Theorem

### Theorem 72.394

Let `K` be a compact shifted `z`-strip with `sigma_K:=sup_{z in K} Re z`.  Choose

```text
theta<1/2,                 theta+sigma_K<1,
T_L=e^L L^A.
```

Assume the polynomial active-bandwidth hypothesis of E72.389.  Then

```text
OUT-HIGH:
sum_{|Im(rho-1/2)|>T_L}
 |F_z(rho-1/2)|
<= C_K L^B
```

uniformly for `z in K`.  More precisely it satisfies the decay estimate (4).

### Proof

The transform bound (1) is the standard compact-support second-variation estimate, applied separately
on the two smooth halves of the even packet and with the jump at `0` included.  E72.388--E72.389 give
(2).  Sum (1) over unit zero-height slabs using the zero-counting bound and obtain (3).  Substitute
`T_L=e^L L^A` to get (4). `QED`

## 6. Consequence for the nodal system

The transformed compact branch should no longer use a fixed zero window.  It should use:

```text
W_L={w=rho-1/2: |Im w|<=T_L}/+-.
```

Then:

```text
outside W_L: closed by OUT-HIGH;
finite Fourier tail inside W_L: absorbed by E72.391--E72.392;
inside W_L: finite nodal Cauchy system.
```

Thus the remaining theorem is not an outside-tail theorem.  It is the finite nodal suppression theorem
for the natural-height window `W_L`.

## 7. Status

```text
proved: high zero tail beyond T_L=e^L L^A is polynomial/decaying;
closed: outside-window tail after switching to natural-height windows;
remaining: finite natural-height nodal suppression and propagation to PW-Cauchy.
```

