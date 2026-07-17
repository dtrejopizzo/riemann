# E73.252 - Structured coordinate coborder audit

## 1. Purpose

E73.251 sharpened the remaining divisibility target to:

```text
COORD-ROW-DIV:
m_j = Y_j^*E + O_M(L^-M),
```

where `m_j` are the coordinate rows of

```text
M_J = D_Q[:,J_*]^{-1}D_Q.
```

The first possible closure is that these coordinate rows already lie, up to a
small error, in the DD-local generated image used to define the quotient:

```text
M_DD = {Y^*E : Y in P_DD}.
```

This note audits that possibility.

## 2. Test

For the two critical nodes used in the quotient packet, form the combined
structured image:

```text
M_DD^comb = span{Y^*E : Y in P_DD(gamma_1)+P_DD(gamma_2)}.
```

For each coordinate row `m_j`, project:

```text
m_j = Proj_{M_DD^comb}m_j + r_j.
```

If the old DD-local image explained the coordinate divisibility, then:

```text
r_j xi_L
```

would be much smaller than

```text
m_j xi_L=z_j.
```

## 3. Result

The projection does not reduce the scalar pairing:

```text
resPairMaxB ~= zMaxB
```

through all trusted windows and all tested DD rational powers.

Thus the DD-local image already removed in E73.245 does not explain
`COORD-ROW-DIV`.

## 4. Meaning

This is a useful no-go, not a failure of the route.  It says the remaining
coordinate rows live in the quotient layer:

```text
Row(D_Q) / M_DD^comb
```

and require a new compatibility identity.

The proof cannot be:

```text
1. enlarge the old DD-local module;
2. project onto full Row(E);
3. fit by adjugate or pseudoinverse.
```

The next object must be a second-layer coborder for the coordinate matrix:

```text
M_J = D_J^{-1}D_Q.
```

## 5. New endpoint

The target is now:

```text
COORD-COB2:
m_j = Y_j^*E + O_M(L^-M),
```

where `Y_j` is not drawn from the first DD-local primitive module, but is
constructed from the quotient coordinate denominator `D_J^{-1}` and the finite
DD-local projection data.

Equivalently, the missing identity is a quotient-coordinate coborder, not a
source-row coborder.

## 6. Status

```text
rejected: first-layer DD-local image as explanation of z_J;
kept:     COORD-ROW-DIV as the correct endpoint;
new:      COORD-COB2, a second-layer quotient-coordinate coborder.
```
