# 106.69 — The overdetermined eigenproblem and the vertical-difference gate

## Purpose and verdict

The remaining bound-state problem can be written as the simultaneous system

\[
 F*K=0,
 \qquad
 \mathcal L_FF=\lambda F,
 \qquad 0<\lambda<\frac12,                         \tag{1}
\]

where

\[
 \mathcal L_F:=W L W^{-1}\big|_{\mathcal N_K},
 \qquad
 \mathcal N_K=\{F:F*K=0\},
 \qquad
 T_F=\mathcal L_F-\frac12 .                        \tag{2}
\]

Thus (1) is the positive-generator notation for the negative-eigenvalue
problem for the operator called \(T_F\) in 106.64.

The additional exact identity

\[
 \boxed{
 \Phi(z+i/2)+\Phi(z-i/2)=2\Xi(z),
 \qquad
 \Phi=\widehat{K/h},\quad h(x)=\cosh(x/2)}          \tag{3}
\]

suggests a nonharmonic-Fourier exclusion: the mean-periodic frequencies lie
in the horizontal gap

\[
 |\operatorname {Re}z|\geq\gamma _1,
 \qquad |\operatorname {Im}z|<\frac12,              \tag{4}
\]

whereas the archimedean negative band lies strictly below \(\gamma _1\).
This note checks that argument at its load-bearing point.

The result is an exact obstruction.

1.  Equation (3) is injective in the physical weighted-Fourier class, but
    its injectivity merely recovers \(K/h\) from \(K\).  It supplies no
    positivity or coercivity.
2.  The eigen-equation is a Toeplitz--Hankel generalized eigenproblem whose
    entries contain the **horizontal** samples \(\Phi(s-z)\) and
    \(\Phi(s+z)\).  Equation (3) controls **vertical** half-shifts.  The two
    sample geometries do not close under one another.
3.  The horizontal zero-free gap applies to the mean-periodic coordinate
    \(F\), but the physical test is \((K/h)F\).  Multiplication by \(K/h\)
    spreads every point frequency across the whole real spectral axis.
4.  If the physical Fourier class is omitted, (3) has an explicit
    infinite-dimensional homogeneous kernel which changes the finite
    Toeplitz--Hankel matrices while leaving \(\Xi\), its zero divisor and the
    gap (4) unchanged.  If the physical class is imposed, that freedom
    disappears, but one has returned exactly to the original signed
    prime--Gamma operator.

Consequently no uncertainty theorem based only on (3)--(4) excludes (1).
The surviving theorem is a horizontal Toeplitz--Hankel coercivity estimate
for the *literal* transform \(\Phi=\widehat{K/h}\).  By Theorem 1 below,
that estimate is equivalent to excluding the off-line channel, not a
weaker support theorem.

## 1. Exact logical strength of the overdetermined system

The Dirichlet form of \(L\) is nonnegative.  Its Gamma channel has positive
density at every displacement \(u>0\).  Therefore

\[
 \mathscr E_K(q)=0
 \quad\Longrightarrow\quad
 q(x)=q(x-u)\quad\text{for a.e. }(x,u),              \tag{5}
\]

so the zero eigenspace consists only of constants.  Constants have already
been removed from \(\mathcal N_K\).  Document 106.47 proves that the
essential spectrum of \(\mathcal L_F\) begins at \(1/2\); hence every
spectral point in \((0,1/2)\) is an isolated finite-multiplicity eigenvalue.

### Theorem 1 — Bound-state exclusion is equivalent to RH

The following statements are equivalent.

1.  RH holds.
2.  System (1) has no nonzero solution for any \(0<\lambda<1/2\).
3.  \(\mathcal L_F\geq\frac12 I\) on \(\mathcal N_K\).
4.  \(T_F\geq0\) on \(\mathcal N_K\).

#### Proof

Under RH the negative evaluation channel in 106.64(25) is absent, so
\(T_F\geq0\).  Thus 1 implies 4, and 4 is exactly 3 by (2).  Statement 3
implies 2.

Conversely, suppose 2 holds.  Nonnegativity and (5) exclude zero spectrum
on \(\mathcal N_K\).  The essential-spectrum theorem quoted above says that
any spectrum below \(1/2\) would be an eigenvalue in \((0,1/2)\), contrary
to 2.  Hence 3 holds.  Finally, 106.64(35) proves

\[
 T_F\geq0\quad\Longleftrightarrow\quad\mathrm {RH}, \tag{6}
\]

so 4 implies 1. \(\square\)

This theorem identifies the exact standard required of any proposed
uncertainty argument: it must use more than the kinematic frequency gap,
because the desired exclusion has the full strength of the signed
evaluation inequality.

## 2. The vertical finite-difference identity

Put

\[
 w(x)=\frac{K(x)}{h(x)},
 \qquad \Phi(z)=\widehat w(z),
 \qquad \widehat K(z)=\Xi(z).                       \tag{7}
\]

Since \(hw=K\), multiplication by
\(h(x)=\frac12(e^{x/2}+e^{-x/2})\) gives

\[
 \widehat{hw}(z)
 =\frac12\{\Phi(z+i/2)+\Phi(z-i/2)\}.              \tag{8}
\]

Equations (7)--(8) prove (3).  In particular, for every zero
\(z\in\mathcal Z(\Xi)\),

\[
 \boxed{\Phi(z+i/2)=-\Phi(z-i/2).}                  \tag{9}
\]

The identity is stronger than a formal recurrence because the physical
transform belongs to a weighted Fourier class.

### Lemma 2 — Physical uniqueness of the half-shift equation

Let

\[
 \mathscr F_{1/2}
 =\left\{\widehat v:
   v\in L^1(\mathbb R),\quad
   e^{|x|/2}v(x)\in L^1(\mathbb R)\right\}.         \tag{10}
\]

If \(H\in\mathscr F_{1/2}\) and

\[
 H(z+i/2)+H(z-i/2)=0                                \tag{11}
\]

on the real axis, then \(H\equiv0\).  Consequently (3) has at most one
solution in \(\mathscr F_{1/2}\).

#### Proof

Write \(H=\widehat v\).  The exponential moment in (10) justifies the two
shifts and gives

\[
 H(t+i/2)+H(t-i/2)=2\widehat{hv}(t),
 \qquad t\in\mathbb R.                              \tag{12}
\]

Thus (11) and Fourier injectivity imply \(hv=0\) almost everywhere.  Since
\(h>0\) on \(\mathbb R\), one has \(v=0\), hence \(H=0\). \(\square\)

The theta kernel decays double exponentially, so \(w=K/h\) lies in every
class (10).  Lemma 2 therefore says that the vertical equation does not
leave a hidden physical branch to select: its unique physical solution is
the already known \(K/h\).  Injectivity is not a lower bound for the
quadratic form.

## 3. Why the zero-free gap is in the wrong coordinate

For a zero \(z\) of \(\Xi\), let

\[
 F_z(x)=\cos(zx),
 \qquad q_z(x)=\frac{F_z(x)}{h(x)},
 \qquad f_z(x)=w(x)F_z(x).                          \tag{13}
\]

Then

\[
 F_z*K=0,                                           \tag{14}
\]

and the double-exponential weight \(K/h\) makes \(F_z\) an admissible
element of \(L^2(\omega_K)\) for every zero in the strip (4), including a
hypothetical nonreal \(z\).  But

\[
 \boxed{
 \widehat f_z(s)=B(s,z)
 =\frac12\{\Phi(s-z)+\Phi(s+z)\}.}                 \tag{15}
\]

The function \(B(\cdot,z)\) is entire and nonzero.  It therefore cannot
vanish on the open interval \((-\gamma _1,\gamma _1)\); otherwise the
identity theorem and Fourier injectivity would imply \(f_z=0\), hence
\(F_z=0\).

Thus (4) is a support statement for the formal mean-periodic spectrum of
\(F\), while the archimedean and Weil forms act on the spread transform
\(B\) of \(f=wF\).  No uncertainty principle can replace one coordinate by
the other without estimating this spreading map.

This is exactly the mismatch already detected in 106.62.  It also explains
why Phase 15, M4.1 does not close the problem.  The archimedean multiplier

\[
 \Psi(t)=\operatorname {Re}\psi\!\left(\frac14+\frac{it}{2}\right)-\log\pi
                                                               \tag{16}
\]

is positive for \(|t|>r_0\), with
\(r_0=6.2898\ldots<\gamma _1\), but it multiplies
\(|\widehat f(t)|^2\), not the point divisor of \(\widehat F\).  Formula
(15) places nonzero mass in the negative band even when \(z\) lies far
outside it.

## 4. The actual generalized eigenproblem

Let \(z_1,\ldots,z_d\) be zeros of \(\Xi\), with derivative jets when a
zero is multiple, and put

\[
 F=\sum_{j=1}^d a_jF_{z_j}.                         \tag{17}
\]

Use the norm matrix \(N\) and the shifted energy matrix \(H\) of 106.62:

\[
\begin{aligned}
 N(z,w)
 &=\frac1{2c_K}
   \{\Phi(w-\overline z)+\Phi(w+\overline z)\},\tag{18}\\
 H(z,w)
 &=\langle F_z,T_FF_w\rangle_{\omega_K}.         \tag{19}
\end{aligned}
\]

On the complete operator, 106.64 gives

\[
 H(z,w)=\sum_{s\in\mathcal Z}
 \overline{B(\overline s,z)}B(s,w)                 \tag{20}
\]

with the symmetric Weil convention and its signed off-line conjugation.
System (1) becomes

\[
 \boxed{
 \sum_{j=1}^dH(z_i,z_j)a_j
 =-\left(\frac12-\lambda\right)
   \sum_{j=1}^dN(z_i,z_j)a_j,
 \qquad 1\leq i\leq d.}                           \tag{21}
\]

The spectral-synthesis closure gives the same equation on the full
mean-periodic space.

Now compare the sample geometries.  Equation (9) controls

\[
 \Phi(z\pm i/2)                                     \tag{22}
\]

at a single zero \(z\).  Equations (18)--(20) require

\[
 \Phi(w\pm\overline z),
 \qquad
 \Phi(s\pm z),                                     \tag{23}
\]

for pairs of zeros.  Applying (3) at \(s\pm z\) gives

\[
 \Phi(s\pm z+i/2)+\Phi(s\pm z-i/2)
 =2\Xi(s\pm z),                                    \tag{24}
\]

but \(s\pm z\) is generally not a zero and the two shifted values in (24)
are not entries in (18)--(20).  Hence (3) supplies no row recurrence, no
diagonalization and no sign for (21).

The missing statement is precisely

\[
 \boxed{a^*Ha\geq0\quad\text{for every finite zero block and every }a,}
                                                               \tag{25}
\]

together with form-norm spectral synthesis.  Formula (25) is the horizontal
Toeplitz--Hankel coercivity theorem, not a consequence of the vertical
difference equation.

## 5. Exact homogeneous falsifier outside the physical class

The failure of an algebraic half-shift argument can be seen without any
asymptotics.  Define

\[
 (\mathcal DH)(z)=H(z+i/2)+H(z-i/2).                \tag{26}
\]

Every entire function satisfying \(H(z+i)=-H(z)\) belongs to
\(\ker\mathcal D\).  In particular,

\[
 H_0(z)=\cosh(\pi z)                                \tag{27}
\]

is even, real on the real axis and satisfies \(\mathcal DH_0=0\).  Thus,
for every real \(c\),

\[
 \Phi_c(z)=\Phi(z)+cH_0(z)                          \tag{28}
\]

has exactly the same right side \(2\Xi\) in (3), and therefore the same
zero divisor and horizontal gap.  Nevertheless,

\[
\begin{aligned}
 B_c(s,z)
 &=B(s,z)+c\cosh(\pi s)\cosh(\pi z),              \tag{29}\\
 N_c(z,w)
 &=N(z,w)+\frac{c}{c_K}
   \overline{\cosh(\pi z)}\cosh(\pi w).           \tag{30}
\end{aligned}
\]

Thus every finite matrix defined by the sample formula (18) acquires an
arbitrary rank-one perturbation while (3)--(4) remain unchanged.  Outside
the physical class this matrix need not remain a norm Gram; that is exactly
why (3)--(4) alone cannot certify the physical Gram property.

Even rapid decay on the real axis does not eliminate the algebraic
freedom.  For \(a>0\),

\[
 H_a(z)=2\cosh(\pi z)
 \exp\{-a(e^{2\pi z}+e^{-2\pi z})\}                \tag{31}
\]

is entire, even, real on \(\mathbb R\), satisfies \(H_a(z+i)=-H_a(z)\),
and decays super-exponentially as \(z\to\pm\infty\) on the real axis.

There is no contradiction with Lemma 2.  The functions (27) and (31) do
not belong to the physical weighted-Fourier class (10).  This gives an
exact dichotomy:

* with only entire-function symmetry, the half-shift equation is
  underdetermined and does not determine the Gram matrices;
* with the physical Fourier class, it is uniquely solvable, but its unique
  solution is simply the original \(K/h\), and the sign problem (25)
  remains untouched.

## 6. Audit of the nonharmonic-Fourier route

Three possible versions of the route are now separated.

### 6.1 Real-frequency support

A theorem for exponentials \(e^{i\gamma x}\) with real \(\gamma\) may use
the gap \(|\gamma|\geq\gamma _1\).  Applying it to every Riemann frequency,
however, assumes that every zero parameter is real.  That assumption is
RH in the \(z\)-coordinate.  Complex frequencies in the strip (4) remain
perfectly admissible in \(L^2(\omega_K)\), because the theta weight decays
double exponentially.

### 6.2 High-frequency archimedean coercivity

Phase 15, M4.1 proves positivity of the multiplier (16) outside a compact
band.  Formula (15) proves that the physical test is not supported outside
that band.  This is not a loss in a numerical estimate; it is an exact
coordinate mismatch.

### 6.3 Completeness or uncertainty in the weighted space

The horizontal gap alone never forces a finite exponential polynomial to
vanish in \(L^2(\omega_K)\).  A lower-frame or uniqueness theorem strong
enough to exclude (21) would have to estimate the literal horizontal
samples (23), including their off-line conjugation.  That estimate is
exactly (25).  Phase 33 already found that replacing the complex divisor by
a real Beurling--Malliavin sequence either assumes RH or reintroduces the
unknown divisor.  The present calculation identifies the same obstruction
at the operator-matrix level.

Two further earlier gates agree with this conclusion.

* 106.42 proves that the Gamma kernel is not TP2, so a
  variation-diminishing or nodal-ordering theorem cannot order the first
  complementary eigenvalue.
* 106.60 proves that projection idempotence and the reducing equation
  collapse exactly to \(\sum\lambda_j(\lambda_j-1/2)\); they supply no
  additional positive term with which to control (21).

## 7. Surviving target

The vertical finite-difference identity is exact and useful for computing
\(\Phi\), but it does not couple the horizontal samples required by the
overdetermined eigenproblem.  The next admissible statement is therefore
not a generic uncertainty theorem.  It is the literal ordinary-prime--Gamma
estimate

\[
 \boxed{
 \sum_{i,j}\overline{a_i}a_j
 \langle F_{z_i},T_FF_{z_j}\rangle_{\omega_K}\geq0
 }                                                   \tag{32}
\]

for every finite zero block, all multiplicity jets and all coefficient
vectors, followed by form-norm spectral synthesis.  Equivalently, in the
Krein notation of 106.64,

\[
 \|\mathcal B_-F\|^2
 \leq\|\mathcal B_0F\|^2+\|\mathcal B_+F\|^2,
 \qquad F\in\mathcal N_K.                           \tag{33}
\]

Any proof of (32) or (33) must use the signed horizontal placement of the
literal von Mangoldt, Gamma and polar channels jointly.  Equations (3)--(4)
do not provide that comparison, and the explicit homogeneous family
(27)--(31) prevents obtaining it from vertical analytic continuation
alone.

## 8. Status

The overdetermined formulation (1) is exact, but its two equations do not
produce independent spectral localizations.  Mean periodicity localizes
\(F\) on the zero divisor; the eigen-equation acts on the spread physical
test \((K/h)F\).  The finite-difference identity uniquely identifies the
spreading kernel in its physical class, yet does not control the horizontal
Toeplitz--Hankel matrices.

Accordingly, the proposed nonharmonic-Fourier shortcut is closed by an
exact sample-geometry obstruction.  The unresolved step remains (32), or
equivalently (33), for the literal coupled arithmetic kernel.
