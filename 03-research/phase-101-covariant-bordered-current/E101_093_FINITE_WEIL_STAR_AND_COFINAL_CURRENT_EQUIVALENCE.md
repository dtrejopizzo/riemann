# E101.093 - Finite Weil star and Xi current criterion

## 1. Decision

The finite Weil--CCM construction supplies the positive star operation sought
in E101.091 without using a zero of `Xi`, a root idempotent or a normalizing
companion metric.  Under the finite even-simple hypothesis, it also supplies
an exact connected determinant Hessian computable from the polar,
archimedean and prime entries of the truncated Weil matrix.

This closes the finite versions of `NA-1`, `NA-2` and `NA-3`.

For a real-type rank-one parity atom `Q`, however, the contracted Hessian is
identically zero:

```text
B_(lambda,N,Q)(w)
 =1/4 Tr[R(w)^2{tr(Q^2)-(tr Q)^2}(Dphys_(lambda,N))]
 =0.                                                    (1.1)
```

Thus `NA-4` has two different meanings which must not be conflated:

```text
NA-4_F   finite source contraction vanishes                 CLOSED;

NA-4_Xi  the parity Gram principal-part current of the Xi
         divisor vanishes for every separating atom         OPEN. (1.2)
```

The first statement is exact but nondiscriminating: every finite spectral
point is real before a limit is taken.  The second statement is the complete
discriminator.  More precisely, for the separating family of parity atoms
constructed in E101.085,

```text
annihilation of every separating Xi divisor current
 <=> every zero of Xi is real
 <=> RH
 <=> Omega7.                                             (1.3)
```

Equation (1.3) is an equivalence of mathematical content, not a proof of
either side.  It locates the force-bearing theorem exactly.  The finite star
is build-neutral infrastructure.  The Xi current criterion belongs to
`DIRECTIONAL-IDENT` and the `DISCRIMINANT`.  A genuine cofinal identification
of uncontracted divisors would imply that criterion, but is stronger than it
and cannot be proved by a build-neutral convergence theorem because the
planted off-line control has the same finite self-adjoint infrastructure.

There is consequently no live reason to construct another finite positive
star.  The only operator-valued successor is a source-canonical Gamma--Euler
identity for uncontracted determinants or divisors which:

```text
1. identifies the finite determinant/current with the Xi target;
2. retains the local double-pole coefficient and linear multiplicity;
3. is proved on the arithmetic source side;
4. fails at a specified source identity for the planted off-line build. (1.4)
```

## 2. Exact finite Weil matrix

Fix `lambda>1` and put

```text
L=2 log lambda.                                         (2.1)
```

On `[0,L]`, extended by zero to the real line, let

```text
U_n(x)=L^(-1/2) exp(2 pi i n x/L),
E_N=span{U_n: |n|<=N}.                                  (2.2)
```

For compactly supported functions define

```text
f^*(x)=conj(f(-x)),
(f*g)(y)=integral_R f(x)g(y-x) dx,

q(f,g)(y)=(f^**g)(y)+(f^**g)(-y).                      (2.3)
```

The functions required below are explicit and real on `[0,L]`:

```text
q(U_n,U_m)(x)
 = [sin(2 pi m x/L)-sin(2 pi n x/L)]/[pi(n-m)],
                                                       n!=m,

q(U_n,U_n)(x)
 =2(1-x/L)cos(2 pi n x/L).                              (2.4)
```

Write

```text
omega_(nm)(x)=q(U_n,U_m)(x).                            (2.5)
```

The exact truncated Weil matrix is

```text
W_(lambda,N)=(W_(nm))_(|n|,|m|<=N),

W_(nm)=P_(nm)-A_(nm)-E_(nm),                            (2.6)
```

where the polar term is

```text
P_(nm)
 =32 L sinh(L/4)^2 (L^2-16 pi^2 mn)
  /[(L^2+16 pi^2m^2)(L^2+16 pi^2n^2)],                (2.7)
```

the archimedean term is

```text
A_(nm)
 =omega_(nm)(0)/2
   [gamma+log(4 pi (exp(L)-1)/(exp(L)+1))]

  +integral_0^L
   [exp(x/2)omega_(nm)(x)-omega_(nm)(0)]
   /[exp(x)-exp(-x)] dx,                               (2.8)
```

and the complete finite Euler term is

```text
E_(nm)
 =sum_(1<k<=exp(L))
   Lambda(k)k^(-1/2)omega_(nm)(log k).                 (2.9)
```

Equations (2.6)--(2.9) contain no spectral zero data.  They are the finite
Guinand--Weil formula in the Fourier basis.  In particular, all subsequent
matrix operations in this document start from:

```text
L, N, gamma, pi and the finite list
{Lambda(k): 1<k<=exp(L)}.                              (2.10)
```

The source formulas are the equations labelled `bombtest`, `bombtest02`,
`bombtestR`, `bombtestp`, `hh`, `bomp`, `weinfty`, `formN` and `form` in

```text
00-references/papers-ref-phase-60/
arXiv-2511.22755v1/arXiv-2511.22755v1.tex.             (2.11)
```

## 3. Even-simple finite quotient

Let `epsilon_(lambda,N)` be the smallest eigenvalue of `W_(lambda,N)` and
put

```text
T=W_(lambda,N)-epsilon_(lambda,N) I.                   (3.1)
```

The finite even-simple hypothesis is:

```text
ES-1 epsilon_(lambda,N) is simple;

ES-2 its eigenvector is even under U_n -> U_(-n).      (3.2)
```

Then

```text
T=T^*>=0,
ker T=C xi_eta.                                        (3.3)
```

Let

```text
eta=sum_(|n|<=N)U_n,
D_0 U_n=nU_n.                                          (3.4)
```

The matrix structure in (2.4) implies that there is a real odd vector
`beta` for which

```text
D_0T-TD_0
 =|beta><eta|-|eta><beta|.                            (3.5)
```

Normalize the even vector `xi_eta` by

```text
<eta,xi_eta>=1.                                        (3.6)
```

This normalization is possible under (3.2).  The Dirichlet source vector and
the normalization used in the full determinant are

```text
delta_N=L^(-1/2)eta,
xi_delta=L^(1/2)xi_eta,
<delta_N,xi_delta>=1.                                (3.6a)
```

The two normalizations give the same rank-one perturbation.  At the
dimensionless level define

```text
D'=D_0-|D_0xi_eta><eta|.                              (3.7)
```

It obeys

```text
D'xi_eta=0,
TD'=(D')^*T.                                          (3.8)
```

The radical quotient

```text
H_(lambda,N)=E_N/Cxi_eta                              (3.9)
```

has the positive inner product

```text
<[x],[y]>_T=<Tx,y>.                                   (3.10)
```

Because `D'` preserves the radical, it induces a dimensionless operator
`Dbar_(lambda,N)` on (3.9).  Put

```text
c_L=2 pi/L,
Dphys_(lambda,N)=c_L Dbar_(lambda,N),
Dphys'=c_LD'.                                        (3.10a)
```

### Theorem 3.1 - Source-built finite self-adjoint operator

Under (3.2), both `Dbar_(lambda,N)` and `Dphys_(lambda,N)` are self-adjoint
in (3.10).

### Proof

For `x,y in E_N`, equations (3.5)--(3.7) give

```text
TD'=TD_0+|beta><eta|
   =D_0T+|eta><beta|.                                (3.11)
```

The right side is `(D')^*T`; hence

```text
<TD'x,y>=<Tx,D'y>.                                   (3.12)
```

Equation (3.8) makes (3.12) independent of the chosen quotient lifts.
Therefore the induced operator is symmetric.  It acts on a finite
dimensional positive Hilbert space, so it is self-adjoint. `QED`

The physical operator `Dphys_(lambda,N)` has the same coordinate as the
CCM atoms and the centered `Xi` divisor.  The factor `c_L` must therefore be
retained in every Hessian and current below.

## 4. The finite positive star

Let `A_(lambda,N)` be the unital algebra generated by
`Dphys_(lambda,N)`.  Its positive involution is the Hilbert adjoint in
(3.10):

```text
X -> X^(dagger_T).                                    (4.1)
```

For a polynomial or a function holomorphic near the finite spectrum, put

```text
f^#(z)=conj(f(conj z)).                               (4.2)
```

### Theorem 4.1 - Exact star functional calculus

For every such `f`,

```text
f(Dphys_(lambda,N))^(dagger_T)
 =f^#(Dphys_(lambda,N)).                             (4.3)
```

In particular, at every spectral fibre `theta`,

```text
f^#(theta)=conj(f(theta)).                            (4.4)
```

### Proof

Theorem 3.1 gives `Dphys^(dagger_T)=Dphys`.  The identity follows first for
polynomials by reversing products and conjugating coefficients, and then
for the holomorphic functional calculus by its Cauchy integral.  Since the
spectrum of a finite self-adjoint operator is real, (4.4) follows. `QED`

This construction answers the finite source questions as follows:

```text
NA-1_F  algebra=A_(lambda,N), star=dagger_T;

NA-2_F  same-fibre complex conjugation follows from (4.3),
        without selecting spectral roots.                         (4.5)
```

The order of construction is essential:

```text
finite Gamma--Euler matrix W
 -> lowest source eigenpair (epsilon,xi_eta)
 -> positive quotient (H,<.,.>_T)
 -> self-adjoint Dphys
 -> star functional calculus.                                    (4.6)
```

Diagonalizing `Dphys` can verify (4.3), but it is not used to define the star.
This distinguishes (4.6) from the root-built normalizing metrics rejected
in E101.091.

## 5. Exact connected Hessian

Let

```text
R(w)=(w-Dphys_(lambda,N))^(-1).                      (5.1)
```

For holomorphic probes `f,g`, define

```text
H_(lambda,N)(w;f,g)
 =-partial_u partial_v log det[
    w-Dphys-u f(Dphys)
      -v g(Dphys)^(dagger_T)]|_(u=v=0).              (5.2)
```

### Theorem 5.1 - Finite source Hessian

One has the exact identities

```text
H_(lambda,N)(w;f,g)
 =Tr_H[R(w)f(Dphys)R(w)g^#(Dphys)]

 =Tr_H[R(w)^2 f(Dphys)g^#(Dphys)]

 =sum_(theta in spec Dphys)
   m_theta f(theta)conj(g(theta))/(w-theta)^2.        (5.3)
```

### Proof

Jacobi differentiation gives the first line.  All four factors are
functions of `Dphys`, so they commute, which gives the second.  The spectral
theorem and (4.4) give the third, including algebraic multiplicity. `QED`

No root extraction is needed to compute the first two lines of (5.3).
There is also an exact lift to the original Fourier space.

### Proposition 5.2 - Quotient trace lift

For every function `h` holomorphic near the spectra of `Dphys'` and
`Dphys`,

```text
Tr_H h(Dphys)=Tr_(E_N)h(Dphys')-h(0).               (5.4)
```

Consequently, with

```text
h_(w,f,g)(t)=f(t)g^#(t)/(w-t)^2,                    (5.5)
```

and provided

```text
w not in spec(Dphys')=spec(Dphys) union {0},         (5.5a)
```

the Hessian is the finite source expression

```text
H_(lambda,N)(w;f,g)
 =Tr_(E_N) h_(w,f,g)(Dphys')-h_(w,f,g)(0).          (5.6)
```

### Proof

The line `Cxi_eta` is invariant under `Dphys'` and carries eigenvalue zero.
In a basis formed by `xi_eta` followed by lifts of a quotient basis,
`Dphys'` is block upper triangular with diagonal blocks `0` and `Dphys`.
The same is true after
holomorphic functional calculus.  Taking traces gives (5.4), and (5.6)
follows from Theorem 5.1. `QED`

Equations (2.6)--(3.10a) and (5.6) answer `NA-3_F`: the connected trace is an
exact finite algorithm on the Gamma--Euler matrix,

```text
W -> (epsilon,xi_eta,T,Dphys') -> H.                 (5.7)
```

The lowest-eigenpair selection couples the polar, archimedean and Euler
channels nonlinearly.  Thus (5.7) is not an additive term-by-term
decomposition of the Hessian.  It does retain the complete matrix containing
the polar term, the full archimedean integral, every prime power below the
cutoff, the cutoff itself and the quotient correction `-h(0)`.

## 6. Rank-one parity contraction

Let `Q(z)=(q_(ab)(z))_(1<=a,b<=d)` be a symmetric matrix-valued function
such that

```text
Q(z)=K(z)v(z)v(z)^T,
Q^#=Q.                                               (6.1)
```

The parity atoms `Q_e,Q_o` of E101.085 have precisely these properties.
Define the bilinear matrix contraction

```text
b(A,B)={tr(AB)-tr(A)tr(B)}/4.                       (6.2)
```

The connected parity Hessian is

```text
B_(lambda,N,Q)(w)
 =1/4[
   sum_(a,b)H_(lambda,N)(w;q_(ab),q_(ba))
  -sum_(a,b)H_(lambda,N)(w;q_(aa),q_(bb))].         (6.3)
```

### Theorem 6.1 - Finite null contraction

For every finite even-simple Weil--CCM quotient,

```text
B_(lambda,N,Q)(w)=0                                 (6.4)
```

identically outside the finite spectrum, and hence meromorphically
everywhere.

### Proof

Because `Q^#=Q`, Theorem 5.1 and finite summation give

```text
B_(lambda,N,Q)(w)
 =1/4 Tr_H R(w)^2[
    tr(Q(Dphys)^2)-(tr Q(Dphys))^2].                (6.5)
```

Here `tr` contracts the matrix indices of `Q`, while `Tr_H` is the operator
trace.  The rank-one identity in (6.1) is the polynomial identity

```text
tr(Q(z)^2)=(tr Q(z))^2.                             (6.6)
```

Functional calculus applies (6.6) to `Dphys`, so the bracket in (6.5) is
zero.
`QED`

The spectral form of the same calculation is

```text
B_(lambda,N,Q)(w)
 =sum_(theta in spec Dphys)
   m_theta g_Q(theta)/(w-theta)^2=0,

g_Q(z)=b(Q(z),Q(z)^*).                              (6.7)
```

Indeed every `theta` is real, `Q(theta)` is a real rank-one matrix, and
therefore

```text
g_Q(theta)=0.                                       (6.8)
```

This proves `NA-4_F`, but also proves that it cannot be the missing
discriminator.  Finite self-adjointness has already placed every finite
fibre on the real line.  Equation (6.4) holds equally for a finite
construction whose intended limiting divisor has a planted off-line point.

## 7. The separating Xi divisor current

Use the centered entire function

```text
Xi(z)=xi(1/2+iz),                                   (7.1)
```

so that RH is equivalent to every zero of `Xi` being real.  Let
`Z_Xi` be its divisor, with multiplicities `m_rho`.

For a rank-one real-type atom `Q`, define the local parity Gram coefficient

```text
g_Q(rho)=b(Q(rho),Q(rho)^*)>=0.                     (7.2)
```

At a real point it vanishes.  Fix one support length `L_0>0`.  The finite
parity-jet construction of E101.085, with all finite symmetric collars, all
finite jet depths and both parities, supplies a countable source-defined
family

```text
Q_PAR(L_0)
 ={Q_(sigma,L_0,N,R): sigma in {e,o}, N,R in N}      (7.2a)
```

with the separation property

```text
rho in Z_Xi and rho not real
 => there exists Q in Q_PAR(L_0) with g_Q(rho)>0.    (7.3)
```

Here is the nondegeneracy check omitted from the bare statement of
E101.085.  Write `rho=x+iy`.  Since `rho` is nonreal, `y!=0`.  If `x=0`,
then `s=1/2+i rho` is real and belongs to `(0,1)`.  But for `0<s<1`, the
alternating eta series is positive and

```text
eta(s)=(1-2^(1-s))zeta(s),                           (7.3a)
```

so `zeta(s)<0`; it has no zero there.  Hence `x!=0`.  Also
`sin(rho L_0/2)!=0`, since the zeros of sine are real.  Thus every nonreal
`Xi` zero is a nondegenerate quartet point for E101.085.  That theorem gives
a finite collar and finite jet depth at which its parity Gram is positive.
The whole family was fixed before reading the divisor; the detecting member
is not inserted into the construction after locating a zero.

Global summability is not needed for the force argument.  Let `M(C)` and
`O(C)` denote meromorphic and entire functions.  Define the divisor current
as a global Mittag--Leffler class modulo entire functions,

```text
[C_(Xi,Q)] in M(C)/O(C),

PP_rho[C_(Xi,Q)]
 =m_rho g_Q(rho)/(w-rho)^2.                         (7.4)
```

A Mittag--Leffler representative may add a holomorphic term, which is why
the quotient in (7.4) is essential.  It cannot alter a principal part.
Hence a nonzero coefficient in (7.4) cannot be cancelled by remote zeros or
by the chosen representative.

The same coefficient data define the positive locally finite Radon measure

```text
nu_(Xi,Q)=sum_(rho in Z_Xi)
           m_rho g_Q(rho) delta_rho.                (7.4a)
```

Local finiteness follows because an entire nonzero function has only
finitely many zeros on each compact set.

### Theorem 7.1 - Parity-current criterion

The following are equivalent:

```text
(a) every zero of Xi is real;

(b) [C_(Xi,Q)]=0 in M(C)/O(C) for every Q in Q_PAR(L_0);

(c) for every rho in Z_Xi and every Q in Q_PAR(L_0),
    m_rho g_Q(rho)=0;

(d) nu_(Xi,Q)=0 for every Q in Q_PAR(L_0).           (7.5)
```

### Proof

If `(a)` holds, every `rho` is real, so `Q(rho)` is real rank one and
`g_Q(rho)=0`.  This proves `(c)`, which immediately gives `(b)` and `(d)`.

Conversely, suppose `(a)` fails and choose a nonreal zero `rho_0`.  By
(7.3), some source probe `Q` satisfies `g_Q(rho_0)>0`.  Its current has the
nonzero principal part

```text
m_(rho_0)g_Q(rho_0)/(w-rho_0)^2.                    (7.6)
```

Thus `(b)`, `(c)` and `(d)` all fail. `QED`

Multiplicity is assigned linearly in the target definition (7.4), as
required by the Xi divisor.  It is not yet obtained as a limit of finite
currents.  No product of two zero sums and no quadratic divisor weight has
been introduced.

## 8. Exact current criterion and location of the bridge

For every finite even-simple quotient and every `Q in Q_PAR(L_0)`, Theorem
6.1
gives

```text
C_(lambda,N,Q)=0.                                   (8.1)
```

Define `XI-PARITY-CURRENT-NULL` by

```text
[C_(Xi,Q)]=0 in M(C)/O(C)
for every Q in Q_PAR(L_0).                          (8.2)
```

### Theorem 8.1 - Xi current equivalence

Assuming the established links `Omega1`--`Omega6`,

```text
XI-PARITY-CURRENT-NULL
 <=> all Xi zeros are real
 <=> RH
 <=> Omega7.                                        (8.4)
```

### Proof

The first equivalence is Theorem 7.1.  The second is the centered form of
RH.  The third is the Li criterion, with the intermediate links already
proved in paper 36. `QED`

Theorem 8.1 is the promised H0 audit.  It is a divisor criterion, not a
convergence theorem.  Since the finite current (8.1) is identically zero, a
formal sequence

```text
0,0,... -> [C_(Xi,Q)]                                (8.3)
```

in a Hausdorff principal-part topology says only that the target class is
zero.  It transports no finite pole position or multiplicity.  Calling
(8.3) `cofinal identification` would hide the complete force of Theorem 8.1
inside a limit symbol.

A genuine divisor bridge must instead begin with the uncontracted finite
logarithmic derivative or divisor current, prove its convergence to the Xi
divisor with linear multiplicity, and only then commute the parity
contraction with that limit.  Such a bridge implies (8.2), but RH alone does
not prove that an even-simple cofinal family or that stronger convergence
exists.

Any proposed proof of the genuine bridge must contain either:

```text
an arithmetic identity which rejects an off-line plant,
or an error which silently replaces the limiting divisor.           (8.5)
```

This also answers the four questions of E101.091 with their correct scope:

```text
NA-1_F   CLOSED conditionally on finite even-simplicity;
NA-2_F   CLOSED by the source-built Hilbert adjoint;
NA-3_F   CLOSED by the quotient trace formula (5.6);
NA-4_F   CLOSED as the null rank-one identity;

NA-4_Xi  OPEN as the criterion (8.2), equivalent to Omega7;

TRUE-DIVISOR-IDENT
         OPEN as a stronger sufficient bridge, not asserted equivalent. (8.6)
```

## 9. Full regularized determinant

The finite quotient is the nontrivial finite block of the perturbed bilateral
scaling operator

```text
Dpert_(lambda,N)
 =Dlog^(lambda)-|Dlog^(lambda)xi_delta><delta_N|.     (9.0)
```

It must not be confused with the unperturbed periodic operator, whose
regularized determinant is `1-exp(-izL)`.  Restoring the exterior lattice,
the CCM determinant formula is

```text
det_reg(Dpert_(lambda,N)-z)
 =-i lambda^(-iz) xi_hat_delta_(lambda,N)(z),       (9.1)

xi_hat_delta_(lambda,N)(z)
 =2L^(-1/2)sin(zL/2)
   sum_(|j|<=N)(xi_delta)_j/(z-2 pi j/L)

 =2sin(zL/2)
   sum_(|j|<=N)(xi_eta)_j/(z-2 pi j/L).             (9.2)
```

The apparent poles in (9.2) are removable.  Every zero of (9.1) is real
because it is a regularized characteristic determinant of a self-adjoint
operator.  The exterior lattice contributes only real fibres and does not
change the rank-one null contraction.

### Theorem 9.1 - Determinant convergence is sufficient

Suppose there exists a cofinal family `(lambda_j,N_j)` satisfying the
even-simple hypothesis, and there are source-canonical real or complex
constants `a_j,b_j` such that

```text
exp(a_j+i b_j z)
 det_reg(Dpert_(lambda_j,N_j)-z)
   ---> Xi(z)                                           (9.3)
```

locally uniformly on the open strip `|Im z|<1/2`.  Assume the limit is not
identically zero.  Then RH holds.

### Proof

The exponential factor is zero-free, so every approximating function in
(9.3) has only real zeros.  If `Xi` had a nonreal zero `rho`, choose a closed
disk around `rho` contained in the strip and disjoint from the real axis.
Every approximant is zero-free on that disk.  Hurwitz's theorem says that a
locally uniform nonzero limit is also zero-free there, a contradiction.
`QED`

Theorem 9.1 is one sufficient implementation of `NA-4_Xi`; it is not
asserted to be necessary.  In particular,

```text
RH does not by itself prove the determinant convergence (9.3).       (9.4)
```

The exact equivalence is the local-current statement of Theorem 8.1, not
the stronger entire-function convergence in (9.3).

Strong resolvent convergence, agreement of finitely many low eigenvalues,
or pointwise convergence on a real set does not imply (9.3).  It does not
control escaping zeros, determinant normalization or local uniformity off
the real axis.

## 10. Source-canonical normalization gate

The constants and the cofinal path in (9.3) are admissible only if they are
fixed before reading the zero divisor.  A valid construction must satisfy:

```text
SC-1  W_(lambda,N) is exactly (2.6)--(2.9);

SC-2  epsilon and the line C xi_eta are selected as the finite lowest
      eigenpair;

SC-3  xi_eta and xi_delta use exactly the normalizations (3.6)--(3.6a);

SC-4  the cofinal relation between lambda and N is specified from
      source error estimates, not from zero matching;

SC-5  a_j and b_j come from the regularization, fixed base values or
      asymptotics on a zero-free Euler half-plane;

SC-6  no zero of Xi, root projector, fitted spectral node or value of
      Xi at an unknown zero enters the construction;

SC-7  every limiting interchange retains polar, Gamma, prime, cutoff,
      exterior-lattice and quotient terms.                          (10.1)
```

Matching two or more values of the approximant directly to `Xi` can be a
numerical normalization, but it is not a proof of (9.3) unless those target
values are themselves recovered by an independent Gamma--Euler identity on
a zero-free half-plane.

## 11. Planted-system falsifier

Let `Xi_plant` be a controlled real-type entire target with a nonreal zero
`rho_plant` in the strip

```text
S={z: |Im z|<1/2}.                                   (11.0)
```

Feed its finite data through the same recipe (2.6)--(4.6).  Whenever the
finite even-simple hypothesis holds, its finite operators are again
self-adjoint and the contracted spectral measures

```text
nu_(lambda,N,Q)
 =sum_(theta in spec Dphys)
   m_theta g_Q(theta)delta_theta                    (11.0a)
```

vanish.  Give locally finite Radon measures on `C` the vague topology, which
is Hausdorff, and holomorphic functions on `S` the compact-open topology.

### Proposition 11.1 - Topological planted obstruction

For a planted target with a detected nonreal zero, neither of the following
convergences can hold:

```text
0=nu_(lambda_j,N_j,Q) ---> nu_(plant,Q) vaguely

or

normalized det_reg(Dpert_(lambda_j,N_j)-z) ---> Xi_plant(z)
in the compact-open topology.                                      (11.1)
```

### Proof

For the measure statement, choose `Q` detecting `rho_plant`.  Then
`nu_(plant,Q)` has the positive atom
`m_(rho_plant)g_Q(rho_plant)delta_(rho_plant)` and is nonzero.  A constant
zero sequence cannot converge to a nonzero element of a Hausdorff space.
For determinant convergence, the approximants have only real zeros, while
Hurwitz on a disk around `rho_plant` contained in `S` forbids the stated
compact-open limit. `QED`

Therefore:

```text
finite self-adjointness and the positive star are build-neutral;

an identification valid for both targets in either topology is impossible;

the identity at which the plant fails is exactly the DISCRIMINANT.  (11.2)
```

This is the precise mathematical content behind the build-neutrality stop
rule.  `GAP-Z` may provide compactness or uniformity for both builds, but a
final arithmetic identification in either topology must use information
absent from the plant.

## 12. Relation to the earlier nonnormal wall

E101.092 proves that a fixed positive metric on a nonnormal companion gives
the overlap current

```text
sum_(i,j)O_(ij)b(Q(p_i),Q(p_j)^*)/(w-p_i)^2,        (12.1)
```

which can be nonzero even for an all-real parity-symmetric divisor.  The
finite Weil quotient avoids that false positive because it is self-adjoint
in its source-built quotient metric.  Its overlap matrix is the identity.

This does not contradict the no-go in E101.092.  The metric here is not an
arbitrary normalizing metric fitted to a companion divisor.  It is the
shifted finite Weil form (3.1), and self-adjointness follows from the exact
rank-two commutator (3.5).

The price is visible in (6.4): the construction makes the finite divisor
real before it has identified that divisor with `Xi`.  It therefore moves
the complete problem into `TRUE-DIVISOR-IDENT` instead of solving it.

## 13. Literature and nonduplication audit

The following mechanisms are prior mathematics and are not claimed as new:

```text
positive Hilbert adjoints and self-adjoint functional calculus;
normalizing metrics for diagonalizable matrices;
connected logarithmic determinant Hessians;
Hurwitz transfer of real-rootedness under local uniform convergence;
finite Guinand--Weil matrices and finite self-adjoint approximants.   (13.1)
```

The closest primary sources inspected are:

```text
Connes--Consani, arXiv:2006.13771:
  convolution involution and positive Sonin-space trace; the residual
  difference from the Weil form remains;

Suzuki, arXiv:2301.00421:
  positive spaces built from source data; the identity equating the norm
  with the Weil form for all tests is RH-equivalent;

Connes--Consani--Moscovici, arXiv:2511.22755:
  the finite Weil matrix, rank-one perturbation, source quotient,
  self-adjoint approximants and regularized determinant used here;

Connes--van Suijlekom, arXiv:2511.23257:
  the abstract lower-bounded self-adjoint/even-ground-state mechanism;

Suzuki, arXiv:2606.09096:
  finite self-adjoint operators with real-zero characteristic functions;
  convergence to the zeta target remains the force-bearing conjecture;

A. Groskin, arXiv:2607.02828,
`A finite Guinand-Weil dictionary and archimedean tail order for the
truncated Weil quadratic form`:
  exact one-level finite dictionary and archimedean tail order, not the
  same-fibre conjugate parity-current identification.                (13.2)
```

The finite star, the determinant-to-real-zeros route and the Hurwitz limit
strategy are therefore not novelty claims.  Groskin also supplies an exact
finite one-level dictionary to zero sums.  The contribution here is the
internal parity-CCM crosswalk and its stop rule:

```text
finite Weil star
 -> identically zero rank-one parity Hessian
 -> separating Xi principal-part current
 -> Xi current criterion equivalent to Omega7.                       (13.3)
```

No inspected source proves `XI-PARITY-CURRENT-NULL` or the stronger
`TRUE-DIVISOR-IDENT`; the former is already equivalent to RH.  Absence from
the inspected literature is not evidence that either statement is true.

## 14. Revised work order

The operator front is now divided into completed infrastructure and one
force-bearing statement.

```text
proved at finite even-simple level:
  exact Weil--CCM source matrix;
  positive quotient metric;
  self-adjoint finite operator;
  positive star and same-fibre conjugation;
  connected Hessian and quotient trace lift;
  zero parity contraction;

frozen:
  another finite star construction;
  a root-built normalizing companion metric;
  treating finite real-rootedness as evidence for Omega7;
  build-neutral convergence advertised as target identification;
  low-zero numerical agreement without off-axis determinant control;

finite infrastructure still requiring proof along the chosen cofinal path:
  even-simplicity and source normalization at every required scale;
  quantitative compactness and regularization estimates;

single force-bearing front:
  COGAMMA-IDENT: prove TRUE-DIVISOR-IDENT, or the sufficient determinant
  form (9.3), from a source-canonical Gamma--Euler identity which rejects
  the plant.                                                   (14.1)
```

The next calculation should not estimate the already-zero current.  It
should compare the complete finite logarithmic derivative of (9.1) with the
Euler-side logarithmic derivative of `Xi` on a fixed zero-free half-plane,
retain the exact discrepancy, and determine which source term can or cannot
propagate that identity into the critical strip.  If the discrepancy is
build-neutral, it belongs to infrastructure.  The first term whose
cancellation fails for the planted build is the only candidate for new
RH-strength mathematics.

## 15. Status

```text
proved:
  exact finite Gamma--Euler matrix formulas;
  conditional finite source-built positive star;
  exact connected Hessian and quotient trace formula;
  exact rank-one parity null contraction;
  parity-current criterion for reality of the Xi divisor;
  equivalence of XI-PARITY-CURRENT-NULL with RH/Omega7;
  determinant convergence sufficiency by Hurwitz;
  topological planted-system obstruction;

conditional finite hypothesis:
  even-simplicity of the lowest truncated Weil eigenpair along the
  selected cofinal family;

closed as infrastructure:
  NA-1_F, NA-2_F, NA-3_F, NA-4_F;

open and force-bearing:
  NA-4_Xi=XI-PARITY-CURRENT-NULL;
  TRUE-DIVISOR-IDENT or a source-canonical determinant identity;
  DIRECTIONAL-IDENT, the DISCRIMINANT and Omega7.                    (15.1)
```
