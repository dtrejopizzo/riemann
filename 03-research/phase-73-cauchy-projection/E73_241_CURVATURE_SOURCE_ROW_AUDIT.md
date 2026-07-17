# E73.241 - Curvature source row audit

Date: 2026-07-14.

## 1. Purpose

E73.240 leaves `CURV-COB` as the non-circular target.  Before building a
primitive module, this note identifies the curvature quotient source as an
actual row on the finite mesh.

The key question is:

```text
Is the curvature source a new object, or is it just qH modulo the Cauchy
plane constraints Q eta=0?
```

The answer is the latter.

## 2. Coefficient source row

For a fixed Cauchy row `q_a`, E73.222--E73.238 write

```text
C_{a,w}=sum c_omega W_omega+sum l_omega V_omega.
```

The coefficients are linear in `eta`:

```text
c_omega=u_omega eta,
l_omega=v_omega eta.
```

Therefore the scalar has a row source:

```text
Src_{a,w}
=sum W_omega u_omega + sum V_omega v_omega,

C_{a,w}=Src_{a,w} eta.                            (1)
```

Using the exact finite explicit formula cell, this source row is exactly

```text
Src_{a,w}=q_a H_L                                  (2)
```

up to the finite WR-series assembly error.

On the transverse subspace `ker Q_w`, this is equivalent to the residual row

```text
rho_a=q_aH_L(I-P_w),
```

because the Cauchy principal part `q_aH_LP_w` annihilates every `eta` with
`Q_w eta=0`.

## 3. Coborder warning

There is an apparent primitive:

```text
Y=q_a^*.
```

Since

```text
E=H_L-mu_L I,
q_aH_L = q_aE + mu_L q_a,
```

and `q_a eta=0`, we get

```text
q_aH_L eta = q_aE eta.                             (3)
```

But this is not a valid coborder proof.  A coborder useful for pairing with
the eigenline must be of the form:

```text
Src = Y^*E
```

so that

```text
Src xi = Y^*E xi = 0.
```

Equation (3) instead places `E` on `eta`, not on `xi`.  It is the same
transverse branch:

```text
E eta = -E P xi,
```

and therefore reintroduces the Cauchy-plane variable `h=Qxi` if used to prove
smallness.

## 4. Consequence for CURV-COB

The curvature source row is not a new source.  It is:

```text
Src_{a,w}=q_aH_L modulo Row(Q_w).
```

Thus `CURV-COB` cannot be closed by the trivial primitive `q_a^*`.  The valid
structured coborder must generate the residual row `rho_a=q_aH_L(I-P_w)` as a
left coborder modulo fixed endpoint residual slots:

```text
rho_a = Y_{a,w}^*E + endpoint residual,
```

with `Y_{a,w}` chosen from a fixed symbolic primitive module.  This is exactly
the non-tautology condition inherited from E73.162, now applied to the
transverse residual row.

## 5. Status

```text
proved: curvature coefficient source row = q_aH_L modulo finite assembly;
proved: modulo ker Q, source = transverse residual row rho_a;
rejected: trivial primitive q_a^* as a proof, because it puts E on eta and
          recovers the circular eigen-branch;
new target: structured left-coborder for rho_a, not for q_aH_L.
```

