# Laguerre index recurrences and the failure of direct induction

## Purpose

This note tests whether A1 can be proved by induction in its Laguerre index.
All comparisons are first made at a common cutoff, so that moving-endpoint
effects are not hidden.  The exact first and second recurrences both retain
a sign-changing arithmetic kernel.

## 1. Common-cutoff certificate

Write
\[
 K_n(u)=e^{-u}L_{n-1}^{(2)}(u),\qquad
 B_n={3\over4}A_n-n,
\]
so the inherited exact identity is
\[
 C_n(T)=B_n-\int_0^T E(u)K_n(u)\,du.                                \tag{1}
\]
For a fixed \(T\), the Laguerre identity
\[
 L_n^{(\alpha)}-L_{n-1}^{(\alpha)}=L_n^{(\alpha-1)}                 \tag{2}
\]
gives
\[
 \boxed{
 C_{n+1}(T)-C_n(T)
 =B_{n+1}-B_n-
 \int_0^T E(u)e^{-u}L_n^{(1)}(u)\,du.}                              \tag{3}
\]
The new kernel has exactly \(n\) positive simple zeros.  It therefore
cannot be paired termwise with \(\Lambda\ge0\) or with a one-sided bound
for \(E\).  Already at the first symbolic instance,
\[
 e^{-u}L_1^{(1)}(u)=e^{-u}(2-u),                                    \tag{4}
\]
the sign changes at \(u=2\).

## 2. The exact second-order recurrence

The three-term Laguerre recurrence with parameter \(2\) gives
\[
 (n+1)K_{n+2}-(2n+3)K_{n+1}+(n+2)K_n=-uK_{n+1}.                      \tag{5}
\]
Combining (1) accordingly yields
\[
\begin{aligned}
 &(n+1)C_{n+2}(T)-(2n+3)C_{n+1}(T)+(n+2)C_n(T)\\
 &\quad=(n+1)B_{n+2}-(2n+3)B_{n+1}+(n+2)B_n
       +\int_0^T uE(u)K_{n+1}(u)\,du .                              \tag{6}
\end{aligned}
\]
This does not create a positive forcing term.  The kernel
\(uK_{n+1}=ue^{-u}L_n^{(2)}(u)\) has \(n\) positive simple zeros.  At
the first nonconstant instance it is
\[
 ue^{-u}L_1^{(2)}(u)=ue^{-u}(3-u),                                  \tag{7}
\]
which changes sign at \(u=3\).

Thus the canonical second-order combination is no better than the first
difference: it replaces one oscillatory Laguerre polynomial by another.
It also has an unavoidable negative coefficient \(-(2n+3)\) on the middle
certificate, so positivity of two preceding certificates would not by
itself control the left-hand side.

## 3. Moving cutoffs do not restore a sign

The exact correction from a common cutoff to the prescribed cutoffs is
\[
 C_{n+1}(T_{n+1})-C_{n+1}(T_n)
 =-\int_{T_n}^{T_{n+1}}E(u)K_{n+1}(u)\,du.                           \tag{8}
\]
For the canonical policy this interval is beyond the oscillatory Laguerre
region, so \(K_{n+1}\) has a fixed sign there.  But \(E=\psi(e^u)-e^u\)
has no unconditional one-sided sign.  A0 supplies an absolute tail budget,
not a signed forcing term.  Hence (8) cannot turn either (3) or (6) into
an induction inequality.

## 4. Scope of the no-go

Equations (3) and (6) rule out the natural first-difference and
three-term-recurrence inductions from positivity of \(\Lambda\),
monotonicity of \(\psi\), or an A0 tail estimate.  They do not rule out a
new arithmetic theorem controlling the signed integrals themselves; such a
theorem would again be an A1/RH-strength cancellation statement.  No
monotonicity of the Li coefficients has been assumed.
