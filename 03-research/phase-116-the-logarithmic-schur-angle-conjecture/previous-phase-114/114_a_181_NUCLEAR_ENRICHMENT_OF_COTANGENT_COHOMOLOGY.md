# Nuclear enrichment of cotangent code cohomology

## 1. Characteristic-zero coefficient algebra

Let `C_R` be the real rapidly decreasing Dirichlet algebra

`C_R={a=(a_n):sum_n |a_n|n^k<infinity for every k}`

with Dirichlet convolution.  It is a commutative unital nuclear Frechet
algebra, its point masses satisfy

`delta_m star delta_n=delta_(mn)`,

and

`ell(a)=sum_n a_n Lambda(n)`

is continuous.

Keeping this factor in characteristic zero is essential.  Reducing the
arithmetic label modulo `2` would kill even labels and could not retain
`Lambda(2^k)`.

## 2. Enriched cotangent cohomology

Let `V_m` be the real vector space with basis the negabinary digit
cotangents `u_0,...,u_(r(m)-1)`.  For a pair put

`V_(m,n)=V_m tensor_R V_n`.

Define

`H_nuc(m,n)=C_R completed-tensor_R V_(m,n)`.

It is a finite free `C_R`-module of rank `r(m)r(n)`.  The cotangent Kunneth
isomorphism lifts to

`H_nuc(m,n)
 ~= (C_R tensor V_m) completed-tensor_(C_R)
     (C_R tensor V_n)`.

Because the digit spaces are finite-dimensional, the completed tensor
products introduce no exactness ambiguity.

## 3. Frobenius correspondence action

For every positive integer `k`, define the continuous `C_R`-linear map

`rho_k(a tensor v)=(delta_k star a) tensor v`.

Continuity follows from

`q_j(delta_k star a)<=k^j q_j(a)`.

Associativity of Dirichlet convolution gives

`rho_m rho_n=rho_(mn)`

exactly.  No parity exception occurs.  The diagonal coefficient trace is

`ell(delta_n)=Lambda(n)`.

Thus the same enriched cotangent object carries both the quadratic digit
direction and every exact arithmetic correspondence label.

## 4. Internal sheaf on the spherical carrier

Regard the nuclear Frechet algebra `C_R` as a solid/condensed commutative
ring and let `H_solid(C_R)` be its Eilenberg--Mac Lane `E_infinity` algebra
in solid spectra.  This retains the Frechet topology and its completed
projective tensor product.  On the absolute spherical square `Y_S`, define

`K_nuc,S=O_(Y_S) derived-smash_S H_solid(C_R)`.

Equivalently, this is extension of spherical scalars by the constant
nuclear coefficient algebra.  Its homotopy sheaf in degree zero contains
the global sections `delta_n`, and completed convolution is its coefficient
multiplication.  At finite cotangent depth define

`H_nuc_sheaf(m,n)=K_nuc,S completed-tensor_R V_(m,n)`.

This is locally free of rank `r(m)r(n)` over `K_nuc,S`.  Multiplication by the
global section `delta_k` defines `rho_k` sheafwise.  Hence composition and
the Kunneth maps commute with restriction and descent.

The fixed structural module

`N_nuc=K_nuc,S e_1 direct-sum K_nuc,S e_2 direct-sum K_nuc,S e_Gamma`

is locally free of rank three.  The first two generators record the
rulings and the third records the correspondence action on cotangent
cohomology.  Arithmetic labels are coefficients, not additional module
generators.  This is the finite-type statement compatible with the
unbounded prime-contact rank.

## 5. Determinant over the nuclear algebra

Since `H_nuc(m,n)` is finite free, its algebraic determinant is the rank-one
`C_R`-module

`det_(C_R) H_nuc(m,n)=wedge_(C_R)^(r(m)r(n)) H_nuc(m,n)`.

The augmentation

`epsilon:C_R->R`, `epsilon(a)=a_1`,

is a continuous algebra morphism because `(a star b)_1=a_1b_1`.
Base change along `epsilon` identifies the determinant with the real digit
determinant of the cotangent construction.  Give this real fiber the
absolute trace norm

`exp(-(log 2)^2 r(m)r(n))`.

The normalized limit is therefore unchanged and equals

`exp(-deg(D)deg(E))`.

The arithmetic contact does not pass through the augmentation; it is
retained by the independent continuous functional `ell`.  Consequently
even prime powers may act trivially on the augmentation fiber without
losing their contact mass in the nuclear coefficient line.

## 6. Compatibility with contact and Green

On the mixed structural generator put

`K_Gamma(a,b)=ell(a star b)`.

Then

`K_Gamma(delta_m,delta_n)=Lambda(mn)`.

On the two ruling generators use the external degree polarization.  Their
direct sum is the continuous form

`B_nuc=B_ext direct-sum K_Gamma`.

The cotangent determinant supplies `B_ext`; the reduced torsion contact
complex supplies the diagonal `Lambda` line.  Their quotient is the Green
line, and the determinant isometry

`delta lambda_RR^cot ~=lambda_C tensor lambda_G^cot`

is equivariant for the `C_R`-coefficient action.

## 7. Consequence

The previous compatibility gate is closed: Frobenius labels do not act by
their reduction on the binary digit coordinates.  They act by convolution
on a separate characteristic-zero nuclear coefficient factor.  This keeps
all `Gamma_n`, exact composition and exact contact while leaving the
cotangent Kunneth dimension and determinant unchanged.

The construction does not reinstate a finite-rank abelian
Neron--Severi group.  Its precise finiteness statement is local freeness of
rank three over the nuclear arithmetic algebra, which is the strongest
form not contradicted by the prime-rank theorem.
