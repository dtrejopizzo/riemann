# 107.29 -- Paper 0 recalibration after the genus-2 diagonal audit

## 1. Purpose

`107_28` adds the missing exact genus-2 falsifier for the primitive
diagonal entries.  The present note records the consequence for Paper 0:

\[
 \text{``fixed elliptic control proved''}
 \neq
 \text{``genus-uniform source route proved.''}
 \tag{1.1}
\]

This note does not retract `107_02`.  It recalibrates its scope.

## 2. What remains proved

`107_02` still proves, on the fixed curve

\[
 E/\mathbf F_5:\qquad y^2=x^3+x+1,
 \tag{2.1}
\]

the full chain

\[
 \Gamma_{F^n}
 \longrightarrow
 \Gamma_{F^n}\cdot\Delta
 \longrightarrow
 Z_E(u)
 \longrightarrow
 5^{-kd/2}
 \longrightarrow
 G_n^0
 \longrightarrow
 |a_n|\le 2\cdot 5^{n/2}.
 \tag{2.2}
\]

That result is unchanged.

## 3. What is no longer tacitly bundled into Paper 0

The genus-2 audit of `107_28` shows that one cannot silently treat

\[
 (\Delta^0)^2=-2,
 \qquad
 (\Gamma_n^0)^2=-2q^n
 \tag{3.1}
\]

as if they were already a genus-uniform source output.

For genus \(g\), the correct target shape is

\[
 (\Delta^0)^2=-2g,
 \qquad
 (\Gamma_n^0)^2=-2gq^n.
 \tag{3.2}
\]

Therefore the true open question is now explicit:

> Does the Phase 107 source route derive the genus factor, or does it
> merely fit the elliptic case?

## 4. Status consequence

Paper 0 remains proved in the scope it explicitly solved: the fixed
elliptic positive control.  The genus-2 falsifier gate itself is now
well covered numerically, but genus-uniform portability of the primitive
diagonal package remains a separate auxiliary gate until one specifies
which route derived the genus factor.  In particular, a classical
adjunction derivation on \(C\times C\) and a genuinely Phase 107 source
derivation are not the same claim.
