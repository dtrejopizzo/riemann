# 107.40 -- Paper B exact external Davenport--Heilbronn witness

## 1. Purpose

This note adds the exact external witness that was still missing from the
Part II coverage matrix of `107_37`.

The target is the structural claim already used in `107_03` and
`107_09`:

\[
 \text{Davenport--Heilbronn fails before positivity because it has no
 primitive Euler tower.}
 \tag{1.1}
\]

The present note does not use zeros.  It certifies that failure directly
from the arithmetic coefficients.

## 2. Workspace coefficient model

The local validation notebook in the repository models the
Davenport--Heilbronn coefficients as

\[
 a_n=A\chi(n)+B\overline{\chi(n)},
 \tag{2.1}
\]

with \(\chi\) the order-4 character modulo \(5\).

After normalization by the nonzero scalar \(a_1\), the coefficient
pattern reduces exactly to

\[
 \psi(n)=
 \begin{cases}
 1,&n\equiv1,2\pmod 5,\\
 -1,&n\equiv3,4\pmod 5,\\
 0,&5\mid n.
 \end{cases}
 \tag{2.2}
\]

So the arithmetic shape of the control is exact and finite.

## 3. Exact verifier

The verifier is
`107_40_davenport_heilbronn_external_witness.py`.

It checks:

1. the normalized coefficient pattern (2.2);
2. exact non-multiplicativity witnesses such as

\[
 \psi(2)^2=1\neq -1=\psi(4),
 \tag{3.1}
\]

and

\[
 \psi(3)^2=1\neq -1=\psi(9);
 \tag{3.2}
\]

3. a finite scan of coprime pairs \(m,n\le 20\) showing repeated
   failures of multiplicativity
   \(\psi(mn)=\psi(m)\psi(n)\).

## 4. Why this is the right witness

If a Dirichlet series with \(a_1\neq0\) admitted an Euler product by
primitive prime towers, then after normalization by \(a_1\) its
coefficients would be multiplicative.

The normalized Davenport--Heilbronn coefficient system is not
multiplicative.  Therefore:

\[
 \text{no Euler product}
 \Longrightarrow
 \text{no canonical primitive prime-power tower}
 \Longrightarrow
 \text{no Phase 107 connected-return package unchanged from }\zeta.
 \tag{4.1}
\]

This is exactly the external witness row that was previously only
formalized.

## 5. Audit outcome

Running the verifier on Friday, July 31, 2026 produced:

```text
psi(2)^2 = 1 != psi(4) = -1
psi(3)^2 = 1 != psi(9) = -1
Found 56 coprime multiplicativity failures in the window n <= 20.
Therefore this coefficient system admits no Euler-product multiplicativity.
```

So the workspace now contains an exact external arithmetic witness that
the Davenport--Heilbronn control fails already at the Euler/coefficient
stage.

## 6. Scope

This note proves something specific and sufficient.

It proves:

1. the external control is genuinely non-Eulerian in exact arithmetic;
2. the failure occurs before any zero-side comparison;
3. the Phase 107 requirement that the package reject Davenport--
   Heilbronn at the orbit/Euler stage now has an independent witness.

It does **not** prove:

1. any statement about the geometric realization of the mixed/tower
   correspondences;
2. the joint prime--Gamma--polar fixed-point package of `107_09`;
3. RH or any positivity statement.
