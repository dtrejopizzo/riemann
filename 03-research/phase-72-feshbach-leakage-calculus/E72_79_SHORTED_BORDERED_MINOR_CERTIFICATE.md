# E72.79 -- Shorted bordered minor certificate

**Date:** 2026-07-09.
**Role:** remove the last opaque inverse in the even Feshbach certificate by replacing every shorted
pairing with a finite bordered determinant.

## 0. Context

E72.75 reached the exact even shorted form:

```text
F_x(s;tau_j)/alpha_j = <Q r_s^even, C_even^(-1) Q W_j>,
```

where:

```text
S_j       = 2 tau_j(tau_j^2 I-D^2)^(-1),
r_j       = (tau_j I-D)^(-1)1,
h_x       = k_x-xi_x,
W_j       = i S_j k_x - (E_j-1)L^(-1)S_j1 <r_j,h_x>,
E_j       = exp(i tau_j L).
```

E72.76 split:

```text
W_j^core = i S_j xi_x,
W_j^disp = S_j( i h_x - (E_j-1)L^(-1)<r_j,h_x>1 ),
W_j      = W_j^core+W_j^disp.
```

The open target was hidden in the inverse `C_even^(-1)`. This note makes it a finite determinant
identity.

## 1. Reduced even basis

Let `E_x` be the even subspace and let:

```text
Q_x = I-k_x k_x^*.
```

Choose an orthonormal basis matrix `B_x` for:

```text
E_x cap k_x^perp.
```

Define:

```text
C_E      := B_x^* C_x B_x,
a_s      := B_x^* r_s^even,
b_j      := B_x^* W_j,
b_j^core := B_x^* W_j^core,
b_j^disp := B_x^* W_j^disp.
```

Since the columns of `B_x` lie in the even `Q_x`-space, inserting `Q_x` before `r_s^even` or `W_j`
does not change the coordinates.

## 2. Bordered minor identity

For every vector `b` in the reduced even coordinate space:

```text
<Q r_s^even, C_even^(-1)Qw>
 = <a_s,C_E^(-1)b>
 = - det [ C_E   b   ] / det(C_E).                              (BM)
         [ a_s^* 0   ]
```

The pairing convention is linear in the second variable:

```text
<a,C_E^(-1)b> = a^* C_E^(-1)b.
```

### Proof

The Schur complement of `C_E` in the bordered matrix gives:

```text
det [ C_E   b   ]
    [ a_s^* 0   ]
 = det(C_E) det(-a_s^*C_E^(-1)b)
 = -det(C_E)<a_s,C_E^(-1)b>.
```

Dividing by `det(C_E)` proves `(BM)`. `QED`

## 3. The finite certificates

Define the numerator minors:

```text
N_j^core(s) := det [ C_E       b_j^core ]
                    [ a_s^*    0        ],

N_j^disp(s) := det [ C_E       b_j^disp ]
                    [ a_s^*    0        ],

N_j(s)      := det [ C_E       b_j      ]
                    [ a_s^*    0        ].
```

Then:

```text
CORE-C  <=>  max_j sup_s |N_j^core(s)|/|det(C_E)| -> 0,
DISP-C  <=>  max_j sup_s |N_j^disp(s)|/|det(C_E)| -> 0,
EV-CERT <=>  max_j sup_s |N_j(s)|/|det(C_E)| -> 0.              (BMC)
```

This is the current exact finite algebraic form of scalar WRL resonance annihilation. The inverse has
not disappeared by an estimate; it has been replaced by a single explicit bordered minor.

## 4. Why this is useful

The old statement:

```text
<Q r_s^even,C_even^(-1)QW_j> -> 0
```

could hide all arithmetic in the inverse. The new statement says the remaining cancellation is exactly
the vanishing, after normalization by `det(C_E)`, of one finite determinant whose last column is one of:

```text
b_j^core,
b_j^disp,
b_j.
```

Thus the next proof target is no longer an analytic norm estimate. It is a determinant divisibility
or cofactor-cancellation statement inside the reduced even bordered pencil.

## 5. Numerical verification

The companion script:

```text
E72_79_bordered_minor_probe.py
```

compares the direct solve:

```text
<a_s,C_E^(-1)b>
```

against the bordered minor:

```text
-det[[C_E,b],[a_s^*,0]]/det(C_E).
```

Representative output:

```text
lambda=6, tau=2.903:
  core   |solve|=2.131e-02  rel.diff=1.628e-16
  disp   |solve|=2.671e-02  rel.diff=2.905e-16
  total  |solve|=2.545e-02  rel.diff=3.048e-16

lambda=10, tau=6.227:
  core   |solve|=2.771e-02  rel.diff=2.800e-16
  disp   |solve|=2.431e-02  rel.diff=7.136e-16
  total  |solve|=3.566e-03  rel.diff=8.158e-16

lambda=12, tau=7.356:
  core   |solve|=1.125e-02  rel.diff=2.566e-15
  disp   |solve|=2.210e-02  rel.diff=1.651e-15
  total  |solve|=1.854e-02  rel.diff=2.448e-15
```

## 6. Status

```text
proved: exact bordered minor formula for CORE-C, DISP-C, and EV-CERT;
proved: the formula matches the finite harness to roundoff;
open:   prove the normalized minors in (BMC) vanish at finite roots.
```
