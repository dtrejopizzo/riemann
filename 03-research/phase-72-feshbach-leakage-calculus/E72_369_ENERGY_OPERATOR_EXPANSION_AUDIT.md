# E72.369 - Energy operator expansion audit

## 1. Purpose

E72.368 introduced the positive master certificate

```text
E_CFIR=||(Lambda_L I-KWin)k+t||^2.
```

This note expands it as a finite quadratic form and records what can and cannot be gained from
positivity.

## 2. Quadratic expansion

Set

```text
A_L:=Lambda_L I-KWin.
```

Then

```text
E_CFIR
= ||A_L k+t||^2
= <k,A_L^*A_L k> + 2 Re <A_L k,t> + ||t||^2.        (1)
```

The matrix

```text
Q_L:=A_L^*A_L
```

is positive semidefinite by construction.

## 3. Why positivity alone is useless

The bound

```text
E_CFIR <= ||A_L k||^2 + 2||A_Lk||||t|| + ||t||^2
```

is the incoherent bound in energy form.  It discards the cancellation in

```text
A_Lk+t.
```

Moreover `Q_L>=0` is tautological: it says only that a squared norm is nonnegative.  It gives no upper
bound.  Therefore the proof cannot be:

```text
show Q_L positive.
```

It must show:

```text
A_L k = -t + O_T(L^B)
```

as a coupled identity.

## 4. Spectral interpretation

If `A_L` is invertible on a maximal off-line cluster, then

```text
k=-A_L^{-1}t + A_L^{-1}O_T(L^B).
```

E72.324--E72.325 provide exactly the leading invertibility of `A_L` through the Cauchy block.
Thus `ENERGY-CFIR` is not the source of suppression; it is the residual whose smallness allows the
already-proved Cauchy inverse to suppress `k`.

The analytic proof still has to establish smallness of the residual.

## 5. No-go for coercive upper bounds

Any argument of the form

```text
E_CFIR <= spectral_norm_bound(Q_L)||k||^2 + ...
```

is circular or too weak.  Since the desired conclusion is that `k` is exponentially small on off-line
clusters, an upper bound proportional to `||k||^2` does not force anything unless its coefficient is
itself exponentially small.  But the leading Cauchy block shows `A_L` is exponentially large, not
small.

Therefore the residual estimate must be a cancellation identity, not a coercivity estimate.

## 6. Correct next target

The next non-circular target is:

```text
COUPLED-RES:
A_L k+t
```

must be represented as a finite coupled Feshbach/explicit-formula expression whose leading
exponential terms cancel before norming.

Equivalently, one must prove:

```text
(Lambda_L I-KWin)J_TG_x + J_TTail_T^M = O_T(L^B)
```

directly, not by bounding `KWin`, `k`, and `tail` separately.

## 7. Status

```text
proved: ENERGY-CFIR expands as a positive quadratic form;
proved: positivity/coercivity alone cannot provide the upper bound;
reduced: analytic proof must target coupled residual cancellation before taking norms.
```
