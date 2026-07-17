# E73.246 - Quotient coordinate audit

## 1. Purpose

E73.245 defined the canonical quotient defect

```text
delta_a = rho_a - Proj_{M_DD} rho_a,
M_DD = {Y^*E : Y in P_DD},
E = H_L - mu_L I,
rho_a = q_a H_L(I-P_w).
```

The scalar obstruction is now:

```text
delta_a xi_L.
```

This note asks whether the quotient defects themselves live in a small stable
coordinate system after the DD-local image is removed.

## 2. Finite coordinate form

For a finite set of critical nodes and rows, stack the quotient defects as rows:

```text
D_Q =
[
  delta_{gamma_1,0}
  delta_{gamma_1,1}
  delta_{gamma_2,0}
  delta_{gamma_2,1}
].
```

Let `e_1,...,e_r` be an orthonormal row basis for `Row(D_Q)`.  Then

```text
delta_a = sum_r theta_{a,r} e_r
```

and hence

```text
delta_a xi_L = theta_a · z_Q,
z_Q = (e_1 xi_L,...,e_r xi_L).
```

Thus the load-bearing divisibility statement becomes:

```text
QUOT-COORD-DIV:
theta_a(L,w) · z_Q(L,w) = O_M(L^-M)
```

for the quotient coordinates produced by the DD-local module.

## 3. What this does and does not prove

This is not a proof of smallness.  The SVD basis used in the audit is only a
diagnostic coordinate chart for the already-defined quotient.

The useful mathematical reduction is:

```text
CURV-QUOT-DIV is equivalent, on this finite block, to a finite coordinate
cancellation inside Row(D_Q).
```

The next proof target is no longer an ambient row-space statement.  It is a
symbolic formula for:

```text
1. rank Row(D_Q);
2. the coordinates theta_a;
3. the quotient test coordinates z_Q=e_r xi_L.
```

## 4. Non-circularity constraints

The coordinate chart is admissible only because:

```text
1. M_DD is fixed before seeing xi_L;
2. delta_a is defined by projecting rho_a modulo M_DD, not by fitting xi_L;
3. z_Q is the remaining test coordinate, not an input used to construct delta_a.
```

The forbidden alternatives remain:

```text
full rowspace projection of E;
using h=Q_w xi_L from the transverse eigen-branch;
adding primitive vectors until the scalar pairing disappears.
```

## 5. Current endpoint

The current exact finite theorem to prove is:

```text
For the canonical DD-local quotient module, the quotient coordinate packet
z_Q(L,w) is super-polynomially orthogonal to the coordinate vectors theta_a:

theta_a(L,w) · z_Q(L,w) = O_M(L^-M).
```

This is the sharpened form of the scalar WRL resonance-annihilation obstruction
inside Phase 73.
