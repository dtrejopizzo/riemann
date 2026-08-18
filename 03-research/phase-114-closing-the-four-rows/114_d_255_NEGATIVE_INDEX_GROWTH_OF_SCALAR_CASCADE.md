# D.255 — A scalar relative-Euler cascade has growing negative index

## Verdict

The scalar product of the relative prime factors is not the missing global
Schur transfer function.  For a finite set \(S\) of distinct primes it has
a pole of order \(|S|\) at the disk origin and its generalized-Schur kernel
has exactly \(|S|\) negative squares.  Thus the indefinite index grows with
the active prime set.

A fixed rank-two Tate correction cannot turn this scalar cascade into a
Schur system uniformly in \(S\).  The local negative ports must first be
reorganized by the multichannel degree/contact conservation law of D.247.

## 1. The scalar cascade

For \(p\in S\), put \(r_p=p^{-1/2}\) and

\[
 b_p(z)={z-r_p\over1-r_pz},\qquad
 c_p(z)={b_p(z)\over z}.
\]

The naive scalar cascade is

\[
 C_S(z)=\prod_{p\in S}c_p(z)
 ={B_S(z)\over z^{|S|}},
 \qquad B_S(z)=\prod_{p\in S}b_p(z).               \tag{1.1}
\]

The numerator \(B_S\) is a finite Blaschke product and

\[
 B_S(0)=(-1)^{|S|}\prod_{p\in S}r_p\ne0.           \tag{1.2}
\]

Therefore (1.1) is a reduced quotient and has a pole of exact order
\(|S|\) at \(0\).

## 2. Exact generalized-Schur index

We use the finite Krein--Langer factorization theorem: a scalar
meromorphic function has a de Branges--Rovnyak kernel with \(\kappa\)
negative squares if and only if it admits a reduced representation

\[
 s={s_0\over B},                                   \tag{2.1}
\]

where \(s_0\) is Schur and \(B\) is a finite Blaschke product of degree
\(\kappa\).  In a reduced representation the degree is intrinsic: it is
the total pole multiplicity in the disk.

Equation (1.1) is such a reduced representation with Schur numerator
\(B_S\) and denominator \(z^{|S|}\), a Blaschke product of degree
\(|S|\).  Hence

\[
 \boxed{
\mathrm{ind}_-(K_{C_S})=|S|.
}                                                   \tag{2.2}
\]

This does not contradict D.100.  D.100 studies the displaced annular
ratio \((1-r_+z)/(1-r_-z)\), whose expansive boundary arc yields infinite
index in the half-plane realization.  Here the object is the central
relative delay \(b_r(z)/z\), a different meromorphic disk function with
one explicit pole per factor.

For \(|S|=1\), this recovers the explicit rank-two kernel calculation of
D.253.  No zero of zeta and no global sign is used.

## 3. Finite-rank shorting cannot repair the scalar cascade

Let a Hermitian kernel have \(m\) negative squares.  A Hermitian
perturbation of rank at most \(r\) can reduce its negative index by at most
\(r\); this follows from the min--max principle after restricting to the
kernel of the perturbation.

The two Tate equations change the old/born block by rank at most four on
finite-energy regularizations (D.190).  Consequently a scalar cascade with
\(|S|>4\) retains at least \(|S|-4\) negative directions after that
correction.  In particular no argument of the form

\[
 \text{scalar relative-Euler cascade}
 +\text{two Tate jets}
 =\text{Schur system}
\]

can hold uniformly as the active prime set grows.

This is an index obstruction to that proposed architecture, not a claim
about the final row-D operator: the Gamma and multichannel contact systems
have not been included in the scalar cascade.

## 4. Why the D.247 completion is different

D.247 does not multiply and then short the scalar relative factors.  It
keeps one local contact output per prime and replaces the collection of
free-delay inputs by a coherent global degree channel:

\[
 \|\widetilde{\mathcal E}_-z\|^2
 +\left|\sum_p\sqrt{\log p}\,z_p\right|^2
 =\|\widetilde{\mathcal E}_+z\|^2
 +\sum_p(\log p)|z_p|^2.                            \tag{4.1}
\]

Thus the port dimension grows with \(S\), exactly as the negative index in
(2.2) requires.  Only after this multichannel conservation law is formed
may the single coherent degree channel be subjected to global primitivity.

## 5. Consequence for the selected route

The prime subsystem used in the global feedback must be matrix-valued.  It
must retain:

* all local contact ports;
* the coherent global degree port;
* the even/odd tangent ports;
* the dual central port of D.254.

A scalar Euler-product transfer function loses the required port geometry.
The next Potapov--Ginzburg calculation must therefore be applied to the
matrix-valued D.247 completion, not to \(C_S\).

## 6. Classification

* Pole order of \(C_S\): **PROVED**.
* Negative index \(|S|\): **PROVED**, by finite Krein--Langer
  factorization.
* Uniform scalar-cascade repair by two Tate jets: **IMPOSSIBLE**.
* Necessity of a growing multichannel contact port: **PROVED AS AN INDEX
  REQUIREMENT**.
* Matrix-valued degree/contact Potapov--Ginzburg transform: **OPEN**.
* Row D: **OPEN**.
