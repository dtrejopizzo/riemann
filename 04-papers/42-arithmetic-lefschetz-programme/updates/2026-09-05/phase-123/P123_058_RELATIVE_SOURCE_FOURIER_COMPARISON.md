# P123.058 — Exact comparison of relative source integration and local Fourier trace

Date: 2026-09-05. Status: PROVED for the local functional comparison and
its operator relative-trace value. This is not a convolution-preserving
source realization of the displacement operation.

## 1. Fourier distribution in the relative source coordinates

Use R_p and ev_p of P123.054, with multiplicative unit volume one.
The distribution T_p=-F(log|x|_p) of P123.034 satisfies, for every
additive Bruhat test phi,

    <T_p,phi>=(log p)R_p(phi)
                     +log p/(p-1) phi(0).       (1.1)

Indeed decompose phi=phi(0)chi_p+r. The remainder is compactly supported
away from zero. P123.034 gives density log p/((1-p^-1)|y|_p) there,
which integrates r to (log p)R_p(phi), since multiplicative unit Haar
is dy/((1-p^-1)|y|_p). Its value on chi_p is log p/(p-1), giving the
remaining term. This proof uses the fixed Fourier normalization, not
an adjustable subtraction convention.

Both terms are continuous for nu_p. Therefore T_p, initially on Bruhat
tests, has a unique continuous extension to E_p with the formula (1.1).
This means extension of this functional, not invariance of E_p under
the additive Fourier transform.

## 2. The displacement operation on external tests

For a compact multiplicative Bruhat test a on Q_p^*, put

    L_p(a)(y)=|1-y|_p^(-1/2) a(1-y),             (2.1)

extended by zero at and near y=1, since a vanishes near zero.
This is an additive Bruhat test: the multiplicative support is compact
and bounded away from zero, so translation yields compact support and
local constancy everywhere. In particular L_p(a)(0)=a(1).

For an external test f on H_S set a=f compose j_p. P123.034 and (1.1)
give the exact local equality

    W_p(f)=(log p)R_p(L_p(a))
                     +log p/(p-1) f(1).         (2.2)

Thus the relative integration already present in the faithful source
domain produces the Fourier packet after a specified displacement and
half-density operation, with its forced evaluation term.

As a normalization check within the proof, take a=1_(Z_p^*). Then
L_p(a)=1_(Z_p^*)(1-y)=chi_p(y)-1_(1+p Z_p)(y). Hence
R_p(L_p(a))=-1/(p-1), and the two terms of (2.2) cancel. The constant-unit
packet is zero, as required; omitting the evaluation term would fail it.

## 3. Agreement with the constructed operator trace

Let B_p,MN(f) be the induced compressed operator of P123.043, L=M+N.
For L beyond the unit level of f, that note and (2.2) give

    Tr B_p,MN(f)-(L+1)(log p)f(1)
      =(log p)R_p(L_p(f compose j_p))
                          +log p/(p-1)f(1).     (3.1)

All operations on the right now belong to the declared local source
domain E_p. The left is the actual trace of a trace-class compression,
with the prescribed relative subtraction. Equation (3.1) proves a local
scalar source/analytic comparison, including constants and unit tests.

For S contained in T and an old p, the normalized local embeddings obey
pi_TS j_(T,p)=j_(S,p). Therefore a and L_p(a) are unchanged by scalar
test pullback, and (2.2)–(3.1) are exactly compatible on those charts.

## 4. The remaining source operation is identified precisely

The map a -> L_p(a) is linear, but is not being asserted to carry
multiplicative convolution to pointwise multiplication in E_p. Nor does
restriction f -> f compose j_p preserve external convolution. Thus
(3.1), although an equality with an actual operator trace, does not
construct a monoidal functor from correspondences into this coefficient
operation.

To close the common-shadow requirement, (2.1) must arise from the source
graph/diagonal operation with its half-density and regularization, and
that operation must respect composition, the layer attaching maps and
the integral contact comparison. Those are the remaining categorical
claims; the equality of the local scalar functionals is no longer
missing. The archimedean and global comparisons, mixed RR and D sign
also remain in scope.
