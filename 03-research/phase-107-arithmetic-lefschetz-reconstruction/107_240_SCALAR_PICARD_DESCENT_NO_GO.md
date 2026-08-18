# 107.240 -- Scalar Picard descent no-go for continuous correspondences

## 1. Pullback law

Let \(D_f\) be the correspondence current with local potential

\[
 U_f(x,y)=\int f(\lambda)\max(y-\lambda x,0)\,d^*\lambda.
 \tag{1.1}
\]

For the two-variable Frobenius chart map

\[
 T_{m,n}(x,y)=(mx,ny),
 \tag{1.2}
\]

107_237 proved

\[
 T_{m,n}^*U_f
 =n\,U_{\rho_{m,n}f},
 \qquad
 (\rho_{m,n}f)(r)=f\left(\frac n m r\right).
 \tag{1.3}
\]

On angular curvature this reads

\[
 \left(T_{m,n}^*U_f\right)''(r)
 =n\,\frac{f(nr/m)}r.
 \tag{1.4}
\]

A finite-PL transition function can change (1.4) only by an atomic measure.
It cannot change its continuous density.

## 2. Literal descent is impossible

### Theorem 2.1

No nonzero continuous compactly supported test \(f\) defines a scalar DC
Cartier/Picard class on the quotient Scaling square whose local equations are
the potentials \(U_f\) and whose transition functions are finite-PL rational
functions.

### Proof

Scalar descent under \(T_{m,n}\) requires the continuous curvature densities
of \(U_f\) and \(T_{m,n}^*U_f\) to agree:

\[
 f(r)=n f\left(\frac n m r\right)
 \qquad(m,n\in\mathbb N^\times).
 \tag{2.1}
\]

Take \(m=n=2\). Then \(f(r)=2f(r)\), so \(f=0\). A finite-PL transition
cannot repair the contradiction because its curvature is atomic, while the
difference in (2.1) is continuous. \(\square\)

## 3. Degree-normalized descent also fails

One may try to divide the pullback by its degree \(n\). The resulting
condition is

\[
 f(r)=f(qr)
 \qquad(q\in\mathbb Q_+^\times).
 \tag{3.1}
\]

### Theorem 3.1

Every continuous compactly supported function satisfying (3.1) is zero.

### Proof

If \(f(r_0)\ne0\), then \(f(qr_0)=f(r_0)\ne0\) for every
\(q\in\mathbb Q_+^\times\). The orbit \(\mathbb Q_+^\times r_0\) is dense in
\((0,\infty)\) and unbounded in both multiplicative directions. Continuity
would make \(f\) constant and nonzero on \((0,\infty)\), contradicting
compact support. \(\square\)

The conclusion survives every scalar normalization depending only on
\((m,n)\): the diagonal maps force an incompatible eigenvalue unless the
normalization removes it, and the remaining rational rescalings force
(3.1).

## 4. Correct categorical status of \(D_f\)

The objects constructed in 107_237 are therefore not scalar divisor classes
on \(\mathscr S^2\). They are elements of the completed **correspondence
module**, on which \(\mathbb N^{\times2}\) acts by the nontrivial
representation

\[
 f\longmapsto n\,\rho_{m,n}f.
 \tag{4.1}
\]

The numerical corner pairing of 107_239 remains valid on this representation:
composition is convolution and the adelic trace is equivariant. What fails is
the map to a rank-one Picard object required by an ordinary RR/Hodge theorem.

Thus the corrected statuses are

\[
 \boxed{\texttt{DC\_CORRESPONDENCE\_CURRENT: CONSTRUCTED}},
\]

\[
 \boxed{\texttt{SCALAR\_DC\_PICARD\_DESCENT: CLOSED\_NO\_GO}}.
\]

This is precisely the continuum-to-discrete obstruction in geometric form:
the full test-function representation cannot be compressed into one scalar
line bundle compatible with all Frobenius chart maps.

## 5. Surviving alternatives

Only two architectures remain:

1. a vector/infinite-rank equivariant sheaf carrying the representation
   (4.1), followed by a new RR/Hodge theorem for that category;
2. a relative or derived correspondence category in which \(D_f\) is an
   operator/kernel rather than a divisor class, with positivity proved
   directly from its trace pairing.

Neither is in the domain of classical Faltings--Hriljac or Yuan--Zhang.
Consequently row (d) cannot be imported after this no-go without a new
categorical Hodge theorem.

The original finite-PL external \(H^0\) construction of 107_236 is unaffected:
its divisors have finite polyhedral support and transform inside the
published sheaf. The no-go applies to nonzero continuous superpositions
\(D_f\).

## 6. Status

Row (a) remains **partial**, but its scalar-Picard branch is closed. The active
question is now binary: construct an equivariant higher-rank realization with
an applicable positivity theorem, or prove a no-go for every finitely
generated equivariant target.

## 7. Machine certificate

Run:

    /home/trabajo/miniforge3/bin/python \
      107_240_scalar_picard_descent_no_go.py

The certificate tests both descent laws on five nonzero compactly supported
continuous functions, checks diagonal Frobenius failure, rational-orbit
escape from support, and the atomic-versus-continuous transition obstruction.
