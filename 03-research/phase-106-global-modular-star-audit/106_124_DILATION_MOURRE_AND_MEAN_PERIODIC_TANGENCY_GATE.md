# 106.124 — Dilation--Mourre and mean-periodic tangency gate

## 1. Purpose and verdict

The physical surplus is the exclusion of an isolated eigenvalue

\[
 Aq=\alpha q,\qquad
 0<\alpha<\frac12,\qquad
 A=L\big|_{\mathscr C},\qquad
 \mathscr C=(\mathbf 1\oplus\mathcal R)^\perp .
 \tag{1}
\]

This note tests the positive-commutator route directly on the literal
ordinary-prime--Gamma generator, after the complete Riemann radical has
been anti-shorted.  Both natural first-order conjugates can be computed
exactly.

* The translation commutator is parity odd.  Its quadratic form is
  identically zero on the physical even space, before one uses the
  eigenvalue equation.
* The dilation commutator is parity even, but every prime-power
  displacement \(a=\log n\) contributes the isolated order-one
  distribution

  \[
  a\{\delta'_a-\delta'_{-a}\}.
  \tag{2}
  \]

  The Gamma channel is continuous in the displacement and the polar
  threshold is scalar.  Neither can remove (2).  The resulting full
  dilation commutator is unbounded in both signs on the even smooth core.
* Geometric dilation is not tangent to the exact mean-periodic constraint
  \((hq)*K=0\).  On the zero divisor its transverse derivative is
  \(t\Xi'(t)\widehat F(t)\), which is nonzero at every simple nonzero zero.
  Translation is tangent to the constraint, but it exchanges even and odd
  parity and hence has zero physical compression.
* Projecting dilation back to \(\mathscr C\) produces a nonlocal conjugate
  operator.  Below the proved essential threshold \(1/2\), a strict Mourre
  estimate for that projected operator is equivalent to the absence of
  the isolated eigenstates it is intended to prove.

Thus the virial identity does not contradict (1).  It gives an exact
signed balance whose missing sign is the compression of the prime
derivative distributions (2) against the hypothetical bound-state
correlations.  This is a source-level localization of the obstruction,
not a counterexample to the physical surplus.

## 2. Semantic audit

The following earlier commutator routes were checked before carrying out
the present calculation.

| document | earlier result | relation to this note |
|---|---|---|
| Phase 54--58 | de Bruijn--Newman virial hierarchy, with the intermediate moment interpolation subsequently retracted | a different heat flow; it is not the spatial ordinary-prime generator |
| Phase 77, E77.2 | the rank-two CCM displacement commutator has a growing blind subspace and cannot yield a raw Kato--Putnam/Mourre closure | finite CCM mesh, not the complete prime--Gamma form |
| Phases 83, 97 and 100 | Gamma--Euler boundary, sensitivity and characteristic commutator identities | boundary and determinant bookkeeping, not a virial identity on \(\mathscr C\) |
| E101.090, Proposition 21.2 | a finite nonzero Hermitian commutator has trace zero and is indefinite | finite trace obstruction |
| 106.24 | sharp prolate truncation creates a nonintegrable Mellin-dilation boundary carrier | additive/prolate endpoint, before the global radical anti-short |
| 106.41 | identifies the full generator and names a joint virial calculation as a possible successor | supplies the operator used below |
| 106.52 and 106.56 | compression of the Euler commutator leaves an exact position-leakage norm; an \(L\)-commutator cannot change the diagonal block of a reducing cluster | finite-cluster versions of the same diagonal obstruction |
| 106.105 | an abstract harmless commutator has zero expectation on a bound state | binding abstract virial gate |
| 106.119 | a moving reducing radical has zero Feynman--Hellmann connection term; a nonreducing motion adds an unsigned commutator | deformation analogue |

What is new below is the exact translation and dilation commutator of the
literal generator itself, the prime \(\delta'\)-term, and its compatibility
with the mean-periodic constraint.  No previous phase contains this joint
calculation.

## 3. Ground-state coordinate for the complete generator

Use the notation of 106.41:

\[
 h(x)=\cosh(x/2),\qquad
 a_n={\Lambda(n)\over\sqrt n},\qquad
 g(u)={e^{-u/2}\over1-e^{-2u}},\qquad c_K=\frac12 .
\tag{3}
\]

Put

\[
 w(x)={h(x)K(x)\over c_K},\qquad
 \kappa(x)=\sqrt{{K(x)\over h(x)}},\qquad
 \ell(x)=\log\kappa(x).
\tag{4}
\]

The unitary ground-state map is

\[
 \mathcal U:L^2(\mu_K)\longrightarrow L^2(\mathbb R,dx),
 \qquad
 \mathcal Uq=w^{1/2}q.
\tag{5}
\]

For a common finite cutoff, let \(\nu\) be the even displacement measure

\[
 d\nu(u)
 =\chi_{\varepsilon,R}(|u|)g(|u|)\,du
  +\sum_{\substack{n\ge2\\ \log n<R}}
     a_n\{\delta_{\log n}+\delta_{-\log n}\}(du),
\tag{6}
\]

where the Gamma cutoff is smooth and compactly supported in
\((0,\infty)\).  Direct substitution in 106.41(7) gives

\[
 \boxed{
 \widetilde L:=\mathcal UL\mathcal U^{-1}
 =M_V-T,}
\tag{7}
\]

where

\[
\begin{aligned}
 (T\psi)(x)
 &=c_K\kappa(x)\int_{\mathbb R}
       \kappa(x+u)\psi(x+u)\,d\nu(u),\\
 V(x)
 &={c_K\over h(x)}
   \int_{\mathbb R}K(x+u)\,d\nu(u).
\end{aligned}
\tag{8}
\]

At finite cutoff these are bounded on the smooth compact core.  The
cutoff-free operator is recovered in the closed difference form.  All
commutator identities below are first proved with (6), and then passed to
the common form core.  This order is needed because the separate Gamma
diagonal and off-diagonal terms diverge at \(u=0\), whereas their
difference and their commutator are finite.

## 4. Translation is invisible on the even sector

Let

\[
 P=-i\partial_x .
\tag{9}
\]

### Theorem 1 — Exact translation commutator

On the finite-cutoff smooth core,

\[
 \boxed{
 i[\widetilde L,P]
 =-M_{V'}+\mathcal K_P,}
\tag{10}
\]

where the symmetric distribution kernel of \(\mathcal K_P\) is

\[
 \boxed{
 \mathcal K_P(x,y)
 =c_K\kappa(x)\kappa(y)
   \{\ell'(x)+\ell'(y)\}\,d\nu(y-x).}
\tag{11}
\]

If \(\psi\) is even, then

\[
 \boxed{\langle\psi,i[\widetilde L,P]\psi\rangle=0.}
\tag{12}
\]

#### Proof

For a smooth symmetric kernel \(k(x,y)\), integration by parts gives

\[
 i[K_k,P](x,y)
 =-(\partial_x+\partial_y)k(x,y).
\tag{13}
\]

The off-diagonal kernel of \(\widetilde L\) is

\[
 k(x,y)=-c_K\kappa(x)\kappa(y)\,d\nu(y-x).
\]

The derivative \(\partial_x+\partial_y\) annihilates every function or
distribution of \(y-x\), so (11) follows.  The multiplication part gives
\(i[M_V,P]=-M_{V'}\), proving (10).

The functions \(V,\kappa,\ell\) are even and \(\ell'\) is odd.  Hence
parity conjugation changes the sign of both terms in (10).  The operator
maps the even space to the odd space, which proves (12). \(\square\)

Equation (12) is stronger than the usual eigenstate virial identity:
translation supplies no diagonal information on any physical even row,
including every heat and hybrid row.

## 5. The exact dilation commutator

Let

\[
 D=-i\left(x\partial_x+\frac12\right)
\tag{14}
\]

be the self-adjoint dilation generator in \(L^2(dx)\).  For a distribution
\(\nu\) in the displacement variable define

\[
 \Theta\nu:=\nu+u\partial_u\nu .
\tag{15}
\]

### Theorem 2 — Literal prime--Gamma dilation identity

On the finite-cutoff smooth core,

\[
 \boxed{
 i[\widetilde L,D]
 =-M_{xV'}+\mathcal K_D,}
\tag{16}
\]

where

\[
\boxed{
\begin{aligned}
\mathcal K_D(x,y)
=c_K\kappa(x)\kappa(y)\Big[
 &\{x\ell'(x)+y\ell'(y)\}\,d\nu(u)\\
 &+d(\Theta\nu)(u)\Big],
\qquad u=y-x .
\end{aligned}}
\tag{17}
\]

The two parts of the completed displacement source transform as

\[
\boxed{
\begin{aligned}
\Theta\{g(|u|)\,du\}
 &=\{g(|u|)+|u|g'(|u|)\}\,du,\\
\Theta\{\delta_a+\delta_{-a}\}
 &=a\{\delta'_a-\delta'_{-a}\}.
\end{aligned}}
\tag{18}
\]

The scalar polar threshold contributes nothing:

\[
 i[-\tfrac12I,D]=0.
\tag{19}
\]

#### Proof

For a smooth kernel, a second integration by parts gives

\[
 i[K_k,D](x,y)
 =-\{k+x\partial_xk+y\partial_yk\}.
\tag{20}
\]

Insert the kernel
\(-c_K\kappa(x)\kappa(y)d\nu(y-x)\).  Since

\[
 x\partial_x\nu(y-x)+y\partial_y\nu(y-x)
 =u\partial_u\nu(u),
\]

formula (20) is exactly (17).  The multiplication part gives
\(-xV'\).

For an atom at \(a>0\), the distribution identities

\[
 \delta_a+u\delta'_a=a\delta'_a,\qquad
 \delta_{-a}+u\delta'_{-a}=-a\delta'_{-a}
\]

prove the second line of (18).  The first line is ordinary
differentiation away from zero; its apparent \(u^{-1}\) singularity
cancels because \(g(u)+ug'(u)=O(1)\) as \(u\downarrow0\).
Equation (19) is immediate. \(\square\)

The derivative distributions in (18) are not an artefact of a separated
prime estimate.  They are the exact infinitesimal response of the real
locations \(\log p^k\) under spatial dilation.  Gamma is absolutely
continuous in \(u\), while the pole is scalar, so neither has an
order-one singularity supported at a prime displacement.

## 6. The isolated prime derivative has no sign

For \(\psi\) in the smooth core put

\[
 C_\psi(u)
 =\int_{\mathbb R}\overline{\psi(x)}\kappa(x)
   \kappa(x+u)\psi(x+u)\,dx
\tag{21}
\]

and

\[
\begin{aligned}
 M_\psi(u)
 =\int_{\mathbb R}\overline{\psi(x)}\kappa(x)\kappa(x+u)
 &\{x\ell'(x)+(x+u)\ell'(x+u)\}\\
 &\times\psi(x+u)\,dx .
\end{aligned}
\tag{22}
\]

For the prime-power displacement \(a=\log n\), write

\[
 V_n(x)
 ={c_Ka_n\over h(x)}
   \{K(x+a)+K(x-a)\}.
\tag{23}
\]

Pairing (17) with \(\psi\) gives the exact atom contribution

\[
\boxed{
\begin{aligned}
\mathcal V_n[\psi]
={}&-\int_{\mathbb R}xV_n'(x)|\psi(x)|^2\,dx\\
 &+2c_Ka_n\operatorname {Re}M_\psi(a)
 -2c_Ka_na\operatorname {Re}C_\psi'(a).
\end{aligned}}
\tag{24}
\]

The last term is the only term in (24) containing a derivative of the
translated state.  It has no fixed sign.

### Theorem 3 — Two-sided unboundedness on the full even core

There is a real even \(\varphi\in C_c^\infty(\mathbb R)\) and two
sequences \(\xi_j^\pm\to\infty\) such that, for

\[
 \psi_\xi(x)=\varphi(x)\cos(\xi x),
\tag{25}
\]

the cutoff-free complete commutator satisfies

\[
\boxed{
\begin{aligned}
\langle\psi_{\xi_j^+},i[\widetilde L,D]\psi_{\xi_j^+}\rangle
 &\ge c_\varphi\xi_j^+,\\
\langle\psi_{\xi_j^-},i[\widetilde L,D]\psi_{\xi_j^-}\rangle
 &\le-c_\varphi\xi_j^-,
\end{aligned}}
\tag{26}
\]

for a constant \(c_\varphi>0\).  The norms of the vectors in (25) stay
bounded above and below.  Thus the literal dilation commutator is
unbounded in both signs even after primes, Gamma and the pole have been
assembled.

#### Proof

Choose \(\varphi\ge0\), even, and positive on an interval of length larger
than \(\log2\).  Define

\[
 A_\varphi(u)
 =\int_{\mathbb R}\kappa(x)\kappa(x+u)
        \varphi(x)\varphi(x+u)\,dx.
\tag{27}
\]

Then \(A_\varphi(\log2)>0\), and \(A_\varphi(u)=0\) once \(|u|\) exceeds
the diameter of \(\operatorname {supp}\varphi\).  Product-to-sum and
integration by parts give, uniformly on compact \(u\)-sets,

\[
\begin{aligned}
 C_{\psi_\xi}(u)
 &=\frac12A_\varphi(u)\cos(\xi u)+O_N(\xi^{-N}),\\
 C_{\psi_\xi}'(u)
 &=-\frac{\xi}{2}A_\varphi(u)\sin(\xi u)+O(1).
\end{aligned}
\tag{28}
\]

The first two lines of (24) are \(O(1)\).  Only finitely many prime
displacements meet the support of \(A_\varphi\), while the remaining
prime diagonal tail is \(O(1)\) by the double-exponential theta decay.
The Gamma small-jump cancellation gives

\[
 \mathcal V_\Gamma[\psi_\xi]=O(\log(2+\xi))=o(\xi).
\tag{29}
\]

For completeness, (29) follows by splitting at \(u=\xi^{-1}\), using
\(|\psi_\xi(x+u)-\psi_\xi(x)|
\ll\min(1,\xi u)\), and integrating by parts for
\(u>\xi^{-1}\).  This is the same logarithmic Gamma scale computed
exactly in 106.116.

Equations (24), (28) and (29) yield

\[
\langle\psi_\xi,i[\widetilde L,D]\psi_\xi\rangle
=c_K\xi\,P_\varphi(\xi)+o(\xi),
\tag{30}
\]

where

\[
 P_\varphi(\xi)
 =\sum_{\substack{n\ge2\\
       \log n<\operatorname {diam}(\operatorname {supp}\varphi)}}
   a_n(\log n)A_\varphi(\log n)\sin(\xi\log n).
\tag{31}
\]

This is a nonzero finite trigonometric polynomial because its \(n=2\)
coefficient is positive.  It has Bohr mean zero.  Hence it takes both
positive and negative values; recurrence of its finite torus flow gives
unbounded sequences on which it is bounded respectively above
\(c>0\) and below \(-c\).  Substitution in (30) proves (26).
Finally,

\[
 \|\psi_\xi\|_2^2
 =\frac12\|\varphi\|_2^2+o(1),
\]

so normalization does not change the conclusion. \(\square\)

Theorem 3 does not by itself refute a *spectrally localized* Mourre
estimate on \(\mathscr C\), because 106.43 proves that \(\mathscr C\)
contains no nonzero compactly supported vector.  It does prove that no
global positivity follows from the literal source measure.  Any surviving
sign must use both the mean-periodic constraint and the spectral
localization of the hypothetical bound state.

## 7. The mean-periodic tangency obstruction

Write

\[
 F=hq,\qquad F*K=0.
\tag{32}
\]

### Theorem 4 — Translation is tangent; dilation is transverse

For every sufficiently regular solution of (32),

\[
 \boxed{F'*K=0,}
\tag{33}
\]

whereas for every constant \(c\),

\[
 \boxed{
 (xF'+cF)*K=-F*(xK').}
\tag{34}
\]

With the Fourier convention \(\widehat K(t)=\Xi(t)\), equation (34)
becomes

\[
 \boxed{
 \widehat{(xF'+cF)*K}(t)
 =t\Xi'(t)\widehat F(t).}
\tag{35}
\]

At a simple nonzero zero \(z\) of \(\Xi\), the elementary mode supported
at \(z\) therefore has nonzero transverse leakage

\[
 z\Xi'(z)\delta_z.
\tag{36}
\]

#### Proof

Equation (33) is obtained by differentiating \(F*K=0\).  Integration by
parts gives

\[
\begin{aligned}
 (xF')*K(t)
 &=-F*K(t)+\int xF(x)K'(t-x)\,dx\\
 &=-F*(xK')(t),
\end{aligned}
\]

because both \(F*K\) and \(F*K'\) vanish.  The term \(cF\) convolves to
zero, proving (34).

The Fourier identities

\[
 \widehat{xK'}(t)=-\Xi(t)-t\Xi'(t),
 \qquad
 \Xi(t)\widehat F(t)=0
\]

give (35).  Multiplication by \(t\Xi'(t)\) on a simple point fibre gives
(36). \(\square\)

This produces an exact first-order dichotomy.

* Translation preserves the zero divisor, but it sends an even mode to an
  odd mode.  The physical even compression is zero, in agreement with
  Theorem 1.
* Dilation preserves parity, but moves each discrete zero frequency and
  therefore leaves the mean-periodic solution space.

Consequently the local geometric dilation cannot be used directly on
\(\mathscr C\).  It must first be projected back by the global
anti-short.  That projection is nonlocal and is precisely where the
prime--Gamma sign which is absent from (18) must enter.

## 8. Projected Mourre estimates are equivalent to exclusion

Let \(Q\) be the projection onto \(\mathscr C\), and let

\[
 D_{\mathscr C}=Q\mathcal U^{-1}D\mathcal UQ
\tag{37}
\]

on a regularized common domain.  Since \(\mathscr C\) reduces \(L\), the
standard virial identity gives, for every isolated eigenvector in (1),

\[
 \boxed{
 \langle q,i[A,D_{\mathscr C}]q\rangle=0.}
\tag{38}
\]

Document 106.47 proves that the essential spectrum of \(A\) begins at
\(1/2\).  Hence every spectral point in a compact interval
\(I\Subset(0,1/2)\) is an isolated eigenvalue of finite multiplicity.

### Theorem 5 — Exact Mourre gate below the essential threshold

Assume the usual bounded-commutator regularization needed for (38).  For
\(c_I>0\), the strict estimate

\[
 \boxed{
 E_I(A)i[A,D_{\mathscr C}]E_I(A)
 \ge c_IE_I(A)}
\tag{39}
\]

holds if and only if

\[
 E_I(A)=0.
\tag{40}
\]

#### Proof

If \(E_I(A)\ne0\), it contains an eigenvector \(q\).  Taking its matrix
element in (39) and using (38) gives

\[
 0\ge c_I\|q\|^2,
\]

a contradiction.  If \(E_I(A)=0\), equation (39) is vacuous. \(\square\)

Thus proving (39) for intervals exhausting \((0,1/2)\) is exactly the
physical-surplus theorem, not an intermediate consequence of the source
commutator.

The same conclusion holds on heat and hybrid rows.  If \(\alpha<1/2\) is
the bottom cluster and \(\Gamma_t\) is any faithful heat-core state, then
spectral concentration and (38) give

\[
 \boxed{
 {\operatorname {Tr}\{i[A,D_{\mathscr C}]\Gamma_t\}
  \over\operatorname {Tr}\Gamma_t}
 \longrightarrow0.}
\tag{41}
\]

Multiplying the heat state by a fixed spectral polynomial does not change
(41), provided that polynomial does not vanish on the bottom cluster.
The commutator therefore supplies no asymptotic surplus on the heat/hybrid
rows that must exclude the state.

## 9. Exact remaining sign in the virial coordinate

For a hypothetical state (1), put
\(\psi_q=\mathcal Uq\).  Theorems 1--2 reduce the source-level virial
statement to

\[
 \boxed{
 0=\mathcal V_\Gamma[\psi_q]
   +\sum_{n\ge2}\mathcal V_n[\psi_q],}
\tag{42}
\]

with \(\mathcal V_n\) given by (24), after the nonlocal projection back to
\(\mathscr C\).  The pole has disappeared only because it is the scalar
threshold and commutes exactly.

To obtain a contradiction from (42), one would have to prove a strict
sign for the compressed sum of

\[
 -2c_K{\Lambda(n)\over\sqrt n}(\log n)
 \operatorname {Re}C_{\psi_q}'(\log n)
\tag{43}
\]

together with all amplitude, Gamma and projection-leakage terms.  Theorem
3 shows that (43) has no source-independent sign; Theorem 4 shows that the
mean-periodic constraint cannot be inserted by an unprojected dilation.
After projection, a strict sign is the Mourre estimate (39), and Theorem 5
shows that it is equivalent to the desired exclusion.

Proved here:

* the exact translation commutator and its parity annihilation;
* the exact completed dilation commutator;
* the isolated derivative distribution at every real prime power;
* two-sided unboundedness of the complete raw dilation commutator;
* the translation/dilation tangency dichotomy for \(F*K=0\);
* equivalence of a strict projected Mourre estimate below \(1/2\) with
  absence of the subthreshold spectrum;
* vanishing of the normalized virial contribution on heat/hybrid rows
  concentrating on a bound cluster.

Not proved here:

\[
 A\ge\frac12I.
\]

The commutator route is therefore closed as an independent mechanism.
Its exact survivor is the projected signed correlation (42)--(43), which
is another source coordinate for the physical surplus and not a harmless
virial remainder.
