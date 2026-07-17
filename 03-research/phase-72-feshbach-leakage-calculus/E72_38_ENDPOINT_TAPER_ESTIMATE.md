# E72.38 -- Endpoint taper estimate for normalized scalar WRL

**Date:** 2026-07-08.
**Role:** explain and partially prove the positive signal from E72.37. The finite CCM cell kernels
vanish linearly at the endpoint `u=x`, and the normalized Mellin character `(u/x)^z` localizes near
that endpoint when `Re z>0`.

## 0. Finite cell shape

In the Phase 71 CCM matrix, the test kernel is

```text
q_{mn}(y),       0 <= y <= L,
L=log x.
```

For `m=n`:

```text
q_{nn}(y)=2(1-y/L)cos(2*pi*n*y/L).
```

For `m != n`:

```text
q_{mn}(y)= [sin(2*pi*m*y/L)-sin(2*pi*n*y/L)]/[pi(n-m)].
```

The prime-power cell matrix has entries

```text
T_{x,u}(m,n)=u^(-1/2)q_{mn}(log u).
```

## 1. Endpoint taper lemma

### Lemma 72.38

For all integers `m,n` and `0<=y<=L`,

```text
|q_{mn}(y)| <= 2(1-y/L)        near the endpoint y=L,
```

more precisely, for all `m,n`,

```text
|q_{mn}(y)| <= 2(L-y)/L.                         (TAPER)
```

### Proof

For `m=n`, this is immediate:

```text
|q_{nn}(y)| <= 2(1-y/L)=2(L-y)/L.
```

For `m != n`, use periodicity at the endpoint:

```text
sin(2*pi*m*y/L)=sin(2*pi*m(y-L)/L).
```

Thus

```text
|sin(2*pi*m*y/L)-sin(2*pi*n*y/L)|
 = |sin(2*pi*m(y-L)/L)-sin(2*pi*n(y-L)/L)|
 <= 2*pi|m-n|(L-y)/L.
```

Dividing by `pi|n-m|` gives

```text
|q_{mn}(y)| <= 2(L-y)/L.
```

`QED`

## 2. Scalar cell bound

Let

```text
l_x(s;u)=<v_{x,s},T_{x,u}k_x>.
```

From `(TAPER)`,

```text
|l_x(s;u)|
 <= B_x(s) u^(-1/2) (1-log u/L),                (CELL)
```

where `B_x(s)` is the compressed channel bound

```text
B_x(s) := 2 ||v_{x,s}||_1 ||k_x||_1
```

in the finite coordinate basis, or any sharper operator-norm replacement.

The proof of `(CELL)` is entrywise from the taper lemma.

## 3. Normalized Mellin endpoint estimate

For `sigma=Re z>1/2`, the continuous endpoint integral satisfies

```text
int_1^x (u/x)^sigma u^(-1/2)(1-log u/L) du/u
 = int_0^L exp(sigma(y-L)) exp(-y/2)(1-y/L)dy
 = x^(-1/2) int_0^L exp(-(sigma-1/2)r) r/L dr
 <= 1/((sigma-1/2)^2 L x^(1/2)),                 (E1)
```

where `r=L-y`.

If the finite prime-power sum is controlled by the corresponding integral with a loss `A_x`, then

```text
|sum_{n<=x} (n/x)^z l_x(s;n)|
 <= A_x B_x(s)/((sigma-1/2)^2 L x^(1/2)).        (E2)
```

Thus normalized scalar WRL follows from:

```text
A_x B_x(s) = o((sigma-1/2)^2 L x^(1/2)).         (CHAN)
```

## 4. Interpretation

The endpoint taper supplies a real mechanism:

```text
cell action vanishes linearly at u=x,
normalized Mellin characters concentrate at u=x,
therefore the normalized transform is small.
```

This is not a PNT estimate and not a zero-location argument. It is a structural property of the CCM
Fejer window.

## 5. What remains

The missing analytic estimate is now the compressed channel bound `(CHAN)`. In particular, one needs
control of:

```text
v_{x,s}=C_x^(-1)Q_x(sI-D_x)^(-1)1_x
```

in a coordinate norm compatible with the endpoint taper.

This is weaker and more concrete than full reduced leakage: it asks only for a weighted coordinate
bound on the Weyl-Feshbach test vector.

## 6. Status

```text
proved: endpoint taper |q_mn(y)| <= 2(L-y)/L;
proved: taper implies normalized Mellin smallness under compressed channel bound;
open:   prove the compressed channel bound for v_{x,s}.
```

The next step is to estimate `B_x(s)` from the compressed complement `C_x`.
