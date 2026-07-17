# E73.239 - Moment annihilator audit for curvature weights

Date: 2026-07-14.

## 1. Purpose

E73.236--E73.238 extract the endpoint and balanced-ramp quotient structure:

```text
sum c_omega=0,
sum l_omega=0,
B'(0)=sum iomega c_omega+sum l_omega,
F_L[r_*]=0.
```

This note audits whether those moment relations alone explain the smallness of
the center.  The answer is no.  They organize the finite identity, but they do
not close it.

## 2. Finite coefficient space

For a fixed row/window write the coefficient vector as

```text
x=(c_omega)_omega \oplus (l_omega)_omega.
```

The weight vector is

```text
g=(W_omega)_omega \oplus (V_omega)_omega,
```

or equivalently the curvature quotient vector from E73.238.

The known moment rows are:

```text
m_c(x)=sum c_omega,
m_l(x)=sum l_omega,
m_d(x)=sum iomega c_omega+sum l_omega.
```

Only `m_c=m_l=0` are annihilating constraints for the original packet.  The
derivative row is the source removed by the balanced neutral ramp; it is useful
for the second-Abel form, but it is not zero before balancing.

## 3. Audit

Project the weight vector `g` onto the span of the moment rows and write:

```text
g=g_mom+g_res.
```

If endpoint moments explained the cancellation, then:

```text
<x,g_res>
```

would be much smaller than `<x,g>`.  The numerical audit shows this does not
happen.  The residual pairing is essentially the center.

Therefore:

```text
END-MOM + balanced ramp
```

are not the missing proof.  They are normal forms.  The missing input must use
additional algebraic structure of the actual vector `eta=(I-P)xi`, most likely
the finite eigen-equation / Feshbach relation, not endpoint conditions alone.

## 4. Consequence

The next proof target should be an eigenline-induced coefficient identity:

```text
EIG-COEFF:
the coefficient vector x(eta_w) satisfies additional finite relations
whose annihilator contains the curvature quotient weights up to O_M(L^-M).
```

This is sharper than ETA-DIV because it asks for the missing source of
orthogonality.

## 5. Status

```text
proved by audit: endpoint moments alone do not explain U4;
open: derive eigen-equation coefficient relations for eta_w.
```

