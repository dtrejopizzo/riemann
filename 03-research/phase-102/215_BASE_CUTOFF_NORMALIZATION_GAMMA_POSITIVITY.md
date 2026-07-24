# Base-cutoff normalization for Gamma_B positivity

## Purpose

`213_GAMMA_B_COMPACT_BASE_IDENTITY.md` proves
\[
  \Gamma_{\mathcal B}={I_7(T_7)-I_8(T_8)\over16}.
\]

This note removes a separate \(\Gamma_{\mathcal B}\)-sign obstruction by
using the freedom in the auxiliary base cutoff \(T_7\).  Since A0 starts at
\(n=8\), \(T_7\) is not a PNT tail cutoff.  It is only a base cutoff used
to write the moving-diagonal recurrence.

With \(T_7\) chosen sufficiently small, the required base condition
\[
  C_8^\ast=C_8(T_8)\ge0
\]
already implies
\[
  \Gamma_{\mathcal B}>0.
\]

Thus the terminal VK load can be absorbed asymptotically once the ordinary
base A1 condition \(C_8^\ast\ge0\) is proved.  The separate tasks that
remain are the base certificate \(C_8^\ast\ge0\), finite thresholds, and the
mixed \(L^1\) loads of `211`.

## Small \(T_7\) control

Recall
\[
  I_7(T_7)=
  \int_0^{T_7}E(e^u)e^{-u}L_6^{(2)}(u)\,du.
\tag{1}
\]

For \(0\le u<\log2\), one has \(\psi(e^u)=0\), hence
\[
  E(e^u)e^{-u}=(\psi(e^u)-e^u)e^{-u}=-1.
\tag{2}
\]

Therefore \(I_7(T_7)\to0\) as \(T_7\downarrow0\).  More explicitly, on
\(0\le u\le1\),
\[
  |L_6^{(2)}(u)|
  \le
  \sum_{j=0}^{6}{\binom{8}{6-j}\over j!}
  <130.
\tag{3}
\]

Thus, for
\[
  0<T_7\le \min(\log2,1/130),
\tag{4}
\]
one has
\[
\boxed{
  |I_7(T_7)|<1,
  \qquad\hbox{so in particular } I_7(T_7)>-1.
}
\tag{5}
\]

This is a harmless base normalization.  If one allows the degenerate
cutoff \(T_7=0\), then \(I_7(T_7)=0\) exactly and the same conclusion is
even simpler.  The positive-cutoff form (4) avoids relying on a degenerate
interval convention.

## Consequence of the base A1 condition at \(n=8\)

By definition,
\[
  C_8^\ast
  =
  -8-I_8(T_8)+{3\over4}\lambda_8^{\rm arch}.
\tag{6}
\]

If
\[
  C_8^\ast\ge0,
\tag{7}
\]
then
\[
  I_8(T_8)
  \le
  -8+{3\over4}\lambda_8^{\rm arch}.
\tag{8}
\]

The exact finite archimedean formula gives
\[
  0<\lambda_8^{\rm arch}<1.
\tag{9}
\]

Hence (8) implies
\[
\boxed{
  I_8(T_8)<-{29\over4}.
}
\tag{10}
\]

Combining (5) and (10),
\[
  I_7(T_7)>-1>-{29\over4}>I_8(T_8).
\]

Therefore
\[
\boxed{
  C_8^\ast\ge0
  \quad\Longrightarrow\quad
  I_7(T_7)>I_8(T_8)
  \quad\Longrightarrow\quad
  \Gamma_{\mathcal B}>0,
}
\tag{11}
\]
provided \(T_7\) is normalized by (4).

## What this closes

This closes the separate sign question for the large-\(n\) terminal budget
coefficient:

- `210` reduced terminal absorption to the sign of \(\Gamma_{\mathcal B}\);
- `212` evaluated the infinite archimedean series;
- `213` converted \(\Gamma_{\mathcal B}\) into \(I_7(T_7)>I_8(T_8)\);
- this note shows that, under a small auxiliary \(T_7\) normalization,
  \(C_8^\ast\ge0\) implies that comparison.

Thus no additional infinite or asymptotic budget sign theorem is needed for
the terminal VK load beyond the already required base condition
\[
  C_8^\ast\ge0.
\]

## What remains open

This does not prove A1.  It leaves:

1. the base compact certificate
   \[
     C_8^\ast=C_8(T_8)\ge0;
   \]
2. explicit threshold and finite-range checks for terminal absorption;
3. the mixed off-diagonal \(L^1\) theorem of `211`, or a signed replacement;
4. any alternate closure route from `196`.

In particular, \(C_8^\ast\ge0\) is itself the \(n=8\) instance of the A1
compact core.  This note only shows that once that base instance is proved,
the terminal large-\(n\) budget coefficient is automatically positive.

## Status

Closed as a base-cutoff normalization for \(\Gamma_{\mathcal B}\).

A1 remains open.  The terminal budget sign gate is absorbed into the
ordinary base condition \(C_8^\ast\ge0\), but the base certificate and mixed
loads remain.
