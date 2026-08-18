# E92.004 - Inverse-free cluster tangent

## 1. Polynomial derivative

On every interval on which the regular Feshbach data are differentiable,
differentiate E92.001(1.2):

```text
dot N_t(z)
 =dot G_(t,z)^reg det F_t
  +G_(t,z)^reg partial_t det F_t
  -(dot h_(t,z)^eff)adj(F_t)b_t^eff
  -h_(t,z)^eff partial_t[adj(F_t)]b_t^eff
  -h_(t,z)^eff adj(F_t)dot b_t^eff.                  (1.1)
```

Every term is polynomial in `F_t` and its derivative.  No factor `F_t^{-1}`
appears.

For a fixed cluster dimension, the standard identities

```text
partial_t det F_t
 =sum_(a,b) Cof_(a,b)(F_t) dot F_(a,b),               (1.2)
```

and the entrywise derivative of the cofactor polynomials define (1.1) even at
singular `F_t`.

## 2. Projective tangent current

Where the four numerator values are nonzero,

```text
CURR_t(s;s_*)
 =partial_t log
  {[N_t(iu)N_t(-iu)]/[N_t(iu_*)N_t(-iu_*)]}          (2.1)

 =dot N_t(iu)/N_t(iu)+dot N_t(-iu)/N_t(-iu)
  -dot N_t(iu_*)/N_t(iu_*)
  -dot N_t(-iu_*)/N_t(-iu_*).                        (2.2)
```

The current can have poles when the chosen numerator chart vanishes.  The
endpoint quotient of E92.002 remains the primary object and is continued by
changing the safe base chart or by using the bordered determinant directly.

## 3. Relation with the Kato coordinate

If one spectral residue dominates, expansion of `adj(F_t)` along that line
reduces (2.2) to the transported Kato current of E89.003 and then to the full
line coordinate of E90.  Thus the Kato formulas are local coordinates of the
cluster numerator, not additional hypotheses for defining it.

## 4. Status

```text
proved:
  exact inverse-free cluster tangent;
  exact projective current in a nonvanishing chart;
  reduction to the Kato coordinate under one-line dominance;

open:
  cofinal control and Euler identification of the cluster current.
```

