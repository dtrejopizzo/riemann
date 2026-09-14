# P123.062 — Local operator conjugacy along the integral deformation

Date: 2026-09-05. Status: PROVED for the compact p-adic neighborhood,
arithmetic dilation semigroup and finite-rank traces specified below.
This is not a global deformation-invariance theorem for the Weil shadow.

## 1. A measure-preserving logarithmic coordinate

Fix a prime p and a parameter t in p Z_p if p is odd, or 4 Z_2 if p=2.
For z in Z_p define

    H_t(z)=log(1+tz)/t
          =z+sum_(j>=2) (-1)^(j+1)t^(j-1)z^j/j,

with H_0(z)=z. The remainder is a strict contraction on Z_p: the
coefficients have absolute value at most p^-1 for odd p and at most
2^-1 for p=2 under the stated stronger parameter condition, and tend
to zero. Also |z^j-w^j|_p<=|z-w|_p on Z_p. Therefore

    |H_t(z)-H_t(w)|_p=|z-w|_p.

For each y, solving z=y-(H_t(z)-z) by contraction proves surjectivity.
Thus H_t is a bijective isometry of Z_p fixing zero. It permutes balls
of every radius p^-N and preserves their Haar measures, so preserves
additive Haar on all Borel sets. In particular it carries p^k Z_p to
itself for every k>=0.

The usual power-series logarithm identity gives, for every integer n>=1,

    H_t(F_n(t,z))=n H_t(z),                      (1.1)

where F_n is the integral polynomial of P123.061. The arguments remain
in the logarithm domain: F_n(t,z) lies in Z_p. The logarithm identity
can also be checked by differentiating the convergent series in z and
matching the value at zero. Hence it holds for all z in Z_p and also
at t=0. This is an exact local conjugacy, not a truncated expansion.

## 2. Half-density operators and composition

On L²(Z_p) let V_n be the isometry

    (V_n f)(z)=|n|_p^-1/2 f(z/n) for z in n Z_p,
               0 otherwise.

These obey V_m V_n=V_(mn). Put U_t f=f compose H_t^-1, a unitary by
section 1. The corresponding operator for F_n is

    V_t,n=U_t^-1 V_n U_t.

By (1.1) this is the half-density pushforward along F_n: its image is
n Z_p, and its inverse branch there is H_t^-1 composed with division
by n composed with H_t. The constant half-density factor is correct
since F_n is conjugate through a measure-preserving map to dilation.
Equivalently its derivative n(1+tz)^(n-1) has absolute value |n|_p.

Consequently V_t,m V_t,n=V_t,mn and the Hilbert adjoints are transported
by the same U_t. These are semigroup isometries on the compact ball;
for p dividing n they are not surjective unitaries. Their adjoints must
not be called inverse dilation maps on this compact domain.

## 3. The Fourier-position cutoffs are preserved exactly

Let E_N on L²(Z_p) be the orthogonal projection onto functions constant
on cosets of p^N Z_p. This is the restriction of E_(0,N)=P_0 Q_N in
P123.042 and has rank p^N. Since H_t bijectively permutes these cosets
and preserves measure, U_t E_N=E_N U_t. Therefore

    E_N V_t,n E_N=U_t^-1 E_N V_n E_N U_t,
    Tr(E_N V_t,n E_N)=Tr(E_N V_n E_N).           (3.1)

The normal kernel calculation of P123.042, or the normalized coset
indicator basis, evaluates the common trace as

    |n|_p^1/2 min(p^N,|1-n|_p^-1),              (3.2)

with p^N at n=1. In particular for n=p^k, k>=1, it is p^-k/2 for every
N>=0 and every allowed t. For a p-adic unit integer n, (3.2) retains
the stated fixed-point cutoff rather than discarding its singularity.

This proves finite-rank trace compatibility along the deformation on
the specified local domain. No limit exchange or numerical estimate
is involved. Any finite linear combination of these arithmetic operators
has the same conjugacy and trace identities.

## 4. Relation to the integral contact

The same F_n family carries the constant primitive relative-fiber
contact [Z[t] --Phi_n(1)--> Z[t]] of P123.061. Its p-adic base change
and specialization at the allowed t preserve that complex. Thus both
the integral contact and this local normal operator trace have explicit
compatible specialization along a common family.

This does not identify them with one another: the contact is a relative
fiber operation with vertical torsion, whereas (3.2) is a graph-action
trace. Their simultaneous compatibility supplies a concrete local
specialization result but not the mixed RR comparison relating their
values. Analytic points in Z_p alone do not detect the vertical Z/p
contact in the special fiber.

The parameter neighborhood here excludes t=1. Extending the comparison
to the full power-map geometry, all external tests, semilocal induction
and all boundary layers requires further work. In particular this note
does not assert a global unitary equivalence between a power map and
dilation on Q_p, nor invariance of the full Weil trace under arbitrary t.
