# E73.108 - Hermite weight interval target

## 1. Purpose

E73.106 reduces the remaining main theorem to box certificates.  The only non-rational object that
varies over a cluster box is the Hermite geometric weight:

```text
G_theta,m(a,i gamma).
```

This note isolates the interval arithmetic target needed to make E73.107 rigorous.

## 2. Explicit formula

For:

```text
a=alpha+i tau,
k=i gamma,
beta=k-a,
w0=1/(2a),
wstar=-1/beta,
d=|wstar-w0|,
r=theta d,
```

the bound used throughout Phase 73 is:

```text
G_theta,m(a,k)
=
1/(|beta|(1-theta)d)
*
sum_{p=0}^{m-1}
  1/p!
  sum_{q=p}^{m-1}
    binom(q,p)|w0|^(q-p) r^(-q).
```

All quantities are elementary functions of `(alpha,tau,gamma)`.

## 3. Needed enclosure

For a cluster box:

```text
B=[alpha0,alpha1]x[tau0,tau1],
```

and a fixed critical row `gamma`, prove an upper bound:

```text
G_theta,m(B,i gamma)
>= sup_{a in B} G_theta,m(a,i gamma).
```

Then:

```text
W_k(B,L)
= e^(alpha1 L)G_theta,m(B,i gamma_k)|1-e^(i gamma_k L)|
```

is a certified upper enclosure for `W_k(A,L)` on the box.

## 4. Interval strategy

A rigorous implementation can proceed in either of two ways.

### A. Direct interval arithmetic

Use rectangular interval arithmetic for:

```text
a, beta, 1/a, 1/beta, |.|, sums, products.
```

This is fully automatic but may be loose because of dependency in:

```text
d=|-1/(k-a)-1/(2a)|.
```

### B. Subdivision plus Lipschitz

On each subbox, evaluate `G` on a small grid and add:

```text
Lip_B(G) diam(B).
```

The Lipschitz constant is explicit because all denominators stay away from zero on natural boxes:

```text
|a|>=a_min,
|k-a|>=dist(k,B)>0,
d>=d_min>0.
```

For the tested boxes, `k` is far from the off-line cluster height, so this is expected to be sharp.

## 5. Certificate input for E73.106

Once `G_theta,m(B,i gamma)` is certified, the box budget is:

```text
B_k^+(B,L)
=
L^5 e^(alpha1 L)G_theta,m(B,i gamma_k)
|1-e^(i gamma_k L)|
|P_x(-gamma_k)|/|D_x(-gamma_k)|.
```

The interval FAR3 selection uses:

```text
FAR_k^+(B,L)
= e^(alpha1 L)G_theta,m(B,i gamma_k)
  |1-e^(i gamma_k L)|dist(-gamma_k,Div(P_x)).
```

and corresponding lower bounds with `alpha0` and a lower Hermite enclosure.

## 6. Remaining technical lemma

The next concrete lemma is:

```text
HERM-BOX:
For every natural cluster box B and critical row gamma in K_L,
the explicit formula above admits computable upper/lower interval enclosures with finite
subdivision, and the enclosure width can be made smaller than the FAR score separation margin.
```

Together with E73.106 this gives a rigorous finite box certificate for `FAR3-MAIN-RAT`.
