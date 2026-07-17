# E72.39 -- Compressed channel bound for endpoint Weyl-Feshbach tightness

**Date:** 2026-07-08.
**Role:** convert the endpoint taper of E72.38 into a concrete sufficient theorem for normalized scalar
WRL annihilation.

## 0. Cell measure notation

Let the scalar finite-cell transform be

```text
N_x(s;z)=sum_{n<=x} (n/x)^z <v_{x,s},T_{x,n}k_x>.
```

Write

```text
y_n=log n,
L=log x,
tau_n=(L-y_n)/L.
```

The taper lemma gives the cell bound

```text
|<v_{x,s},T_{x,n}k_x>|
 <= B_x(s) n^(-1/2) tau_n.                       (CB)
```

Here `B_x(s)` is any valid compressed channel constant.

## 1. Weighted endpoint mass

For `sigma=Re z`, define the endpoint mass

```text
W_x(sigma)
 := sum_{n<=x, cells} (n/x)^sigma n^(-1/2) tau_n.
```

Then

```text
|N_x(s;z)| <= B_x(s) W_x(sigma).                 (W)
```

This is exact from `(CB)`.

## 2. Sufficient theorem

### Theorem 72.39

Fix a compact spectral set `K` with

```text
sigma_0 := inf_{z in K} Re z > 1/2.
```

Assume:

```text
sup_{z in K} W_x(Re z) <= omega_x(K),
```

and the compressed channel bound

```text
sup_{s in S_eta} B_x(s) omega_x(K) -> 0          (CCB)
```

on the two Cauchy heights `S_eta`. Then:

```text
sup_{s,z} |N_x(s;z)| -> 0.
```

Consequently the normalized scalar WRL resonance vanishes on `K`, provided the model-main Abel
subtraction error from E72.31 is also `o(1)`.

### Proof

By `(W)`,

```text
sup_{s,z}|N_x(s;z)|
 <= sup_s B_x(s) sup_z W_x(Re z)
 <= sup_s B_x(s) omega_x(K).
```

Assumption `(CCB)` gives the result. The final implication is exactly the normalized Abel form of
E72.31. `QED`

## 3. PNT-scale evaluation of `W_x`

For a continuous cell measure comparable to `du/u`, E72.38 gives:

```text
W_x(sigma) <= C / ((sigma-1/2)^2 L x^(1/2)).
```

For a prime-weighted measure comparable to `dpsi(u)`, the mass is larger:

```text
sum Lambda(n)(n/x)^sigma n^(-1/2)tau_n
 ~ x^(1/2)/(L(sigma+1/2)^2).
```

Therefore the scalar WRL proof must use the **post-main-subtraction / Chebyshev-discrepancy**
measure, not the raw prime measure. This matches E72.31: the PNT main term is absorbed by the model,
and only the Abel discrepancy remains.

## 4. Channel bound from complement gap

A crude bound is:

```text
v_{x,s}=C_x^(-1)Q_x(sI-D_x)^(-1)1_x,
||v_{x,s}|| <= ||C_x^(-1)|| ||(sI-D_x)^(-1)1_x||
            <= ||C_x^(-1)|| sqrt(d_x)/|Im s|.
```

If `||k_x||_1 <= sqrt(d_x)||k_x||` and `||v_x||_1 <= sqrt(d_x)||v_x||`, then

```text
B_x(s) <= C d_x ||C_x^(-1)|| sqrt(d_x)/|Im s|.   (crude)
```

This is probably too crude, but it gives a concrete sufficient condition:

```text
d_x^(3/2)||C_x^(-1)|| omega_x(K) -> 0.           (GAP-CCB)
```

Sharper weighted `l^2` bounds should replace the coordinate `l^1` estimate.

## 5. Current endpoint

The scalar WRL proof is now reduced to two estimates:

```text
(A) post-main-subtraction endpoint mass omega_x(K) is small;
(B) compressed Cauchy channel B_x(s) grows slowly enough.
```

Both are zero-free. Both are finite CCM/prolate estimates.

## 6. Status

```text
proved: endpoint taper + channel bound => normalized scalar WRL annihilation;
open:   prove post-main endpoint mass and sharp compressed channel bounds.
```

This is the first fully analytic sufficient route from the normalized Mellin signal to the scalar WRL
target.
