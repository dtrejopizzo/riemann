# R161_043 — The `Xf` Tate correction has opposite parity and pairs to zero

## 0. Verdict

The Tate remainder anticipated in `R161_042` does not produce the positive square `||r||^2` in that ordering.
Multiplication by `X=t` reverses parity. Hence the Tate projection of `Xf` lies on the parity line opposite to the
first-contact forcing and its collar current. Their pairing vanishes exactly.

This is an algebraic simplification of the mixed Green route. The parity-positive identity of `R161_032` remains
correct, but applies only when the endpoint vector has the same parity as the forcing; it must not be inserted into
the source-derivative term.

## 1. Parity reversal by `X`

Let `Jf(t)=f(-t)` and `Xf(t)=tf(t)`. Then

```
JX=-XJ.                                                   (1.1)
```

If

```
Jf=epsilon f,                                            (1.2)
```

then

```
boxed: J(Xf)=-epsilon Xf.                                (1.3)
```

Thus the source derivative has parity `-epsilon`.

## 2. Tate projection preserves parity

The Tate space

```
T_T=span{phi_-,phi_+},
phi_-(t)=exp(-t/2),     phi_+(t)=exp(t/2),               (2.1)
```

is invariant under `J`, which exchanges `phi_-` and `phi_+`. Its orthogonal projection `Tau_T` therefore commutes
with `J`. From (1.3),

```
boxed: J(Tau_TPXf)=-epsilon Tau_TPXf.                    (2.2)
```

In coefficient coordinates, if `C` is exchange, the coefficient vector `w_X` of `Tau_TPXf` satisfies

```
Cw_X=-epsilon w_X.                                      (2.3)
```

## 3. Orthogonality to the first-contact forcing

The first-contact forcing

```
r=alpha phi_-+beta phi_+                                (3.1)
```

has the same parity as `f`; its coefficient vector `v` satisfies

```
Cv=epsilon v.                                           (3.2)
```

Opposite parity subspaces are orthogonal in `L2(-T,T)`. Therefore

```
boxed: <r,Tau_TPXf>=0.                                  (3.3)
```

The collar current is

```
j=G_TCv.                                                 (3.4)
```

Because `G_T` commutes with `C`, `j` also has coefficient parity `epsilon`. Since the coefficient Gram is
`C`-invariant,

```
boxed: <w_X,j>=0.                                        (3.5)
```

## 4. Consequence for the mixed Green expansion

In `R161_042`, the term `C_NXf` forces the decomposition

```
PXf=Pi_TPXf+Tau_TPXf.                                   (4.1)
```

If insertion of `(PC-ren)` converts the Tate component of the resulting pairing into either (3.3) or (3.5), that
component vanishes exactly. It does **not** become

```
epsilon<v,G_TCv>=||r||^2.                               (4.2)
```

Formula (4.2) remains the correct same-parity endpoint identity of `R161_032`, but the `Xf` correction has the
opposite parity and belongs to its orthogonal complement.

This removes the finite-dimensional sign problem from the source-derivative ordering. What remains is to prove
that the primitive part of (4.1) is exactly an admissible radical test and to control the exterior wrong-side
pieces of `R161_042`.

## 5. Status

- parity reversal `JX=-XJ`: **PROVED**;
- opposite parity of the Tate projection of `Xf`: **PROVED**;
- orthogonality to the forcing and collar current: **PROVED**;
- positive same-parity Tate square in this ordering: **REJECTED / WRONG PARITY**;
- conversion of the full finite pairing to the literal orthogonal terms (3.3)/(3.5): **OPEN**;
- remaining primitive/exterior Green identity: **OPEN**;
- row D: **OPEN**.
