# 107.150 -- The projective tensor mass inherited from CC is entrywise l1

## 1. Result

The mass functional for the square is fixed by the norm used in
Connes--Consani's 2022 dimension construction.  If both factors carry
the \(\ell^1\) norm, their projective tensor norm is not the trace norm.
For every real \(r\times s\) matrix \(A=(a_{ij})\),

\[
 \|A\|_{\ell^1_r\widehat\otimes_\pi\ell^1_s}
 =
 \sum_{i,j}|a_{ij}|.
 \tag{1.1}
\]

Thus the tensorial continuation of the published CC mass is the
entrywise \(\ell^1\) norm.  The trace norm considered in 107_147 is
the projective tensor norm of Euclidean factors and remains a valid
no-go for that different choice.

## 2. Exact proof

By definition,

\[
 \|A\|_\pi
 =
 \inf\left\{
 \sum_\nu\|x_\nu\|_1\|y_\nu\|_1:
 A=\sum_\nu x_\nu\otimes y_\nu
 \right\}.
\]

The coordinate decomposition

\[
 A=\sum_{i,j}a_{ij}e_i\otimes e_j
\]

gives \(\|A\|_\pi\le\sum_{i,j}|a_{ij}|\).

For the reverse inequality, set
\(b_{ij}=\operatorname{sign}(a_{ij})\).  The bilinear form

\[
 B(x,y)=\sum_{i,j}b_{ij}x_i y_j
\]

has norm at most one on \(\ell^1_r\times\ell^1_s\), since

\[
 |B(x,y)|
 \le\sum_{i,j}|x_i||y_j|
 =\|x\|_1\|y\|_1.
\]

For every decomposition of \(A\),

\[
 \sum_{i,j}|a_{ij}|
 =B(A)
 \le\sum_\nu\|x_\nu\|_1\|y_\nu\|_1.
\]

Taking the infimum proves (1.1).  The coordinate decomposition is
integral when \(A\) is integral, so no scalar-extension gap occurs for
the lattice used by the absolute dimension.

## 3. Dimension consequence

After vectorizing \(M_{r,s}(\mathbb Z)\), the norm ball in (1.1) is
exactly the module \(M_{rs}(n)\) of 107_146.  Hence, for \(rs\ge2\),

\[
 \left\lceil\log_2(n+1)\right\rceil
 \le
 \dim_{\mathbb S[\pm1]} M_{r,s}(n)
 \le
 rs\left\lceil\log_2(n+1)\right\rceil.
 \tag{3.1}
\]

With \(n=\lfloor e^{\deg D}\rfloor\), the dimension is
\(\Theta(\deg D)\).  Therefore the CC-inherited projective tensor mass
passes the necessary Riemann--Roch growth gate.

For a \(2\times2\) matrix lattice, the explicit generating family is

\[
 \{2^k E_{ij}:0\le k<\lceil\log_2(n+1)\rceil,\ 1\le i,j\le2\}.
\]

It represents every integral matrix of entrywise mass at most \(n\)
without cancellation and within the same mass budget.

## 4. Scope

This fixes the mass functional conditional on transporting the published
CC \(\ell^1\) norm functorially to a tensor product.  It does not define
\(H^0\) on the arithmetic-site square, construct \(H^1\), or prove a
surface Riemann--Roch theorem.  It removes the mass-functional ambiguity
from the next construction and reopens the CC tensor branch that had
been incorrectly identified with the trace norm.

