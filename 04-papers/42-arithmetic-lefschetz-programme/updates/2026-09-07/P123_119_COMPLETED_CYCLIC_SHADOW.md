# P123.119 — Completed cyclic comparison and finite tangential periodic homology

Date: 2026-09-07. Status: PROVED-IN-REPOSITORY for the normalized
completed boundary complex of P123.101, P123.118 and the explicitly
formal cyclic totalizations below. No entire/analytic cyclic topology,
full arithmetic trace comparison, or Hilbert heat determinant is inferred.

## 1. A strict morphism of mixed complexes

On the normalized completed Hochschild complex C_n of S=S(Y), use
Connes' operator

    B(a_0[a_1|...|a_n])
      =sum_(i=0)^n (-1)^(n i)
         1[a_i|...|a_n|a_0|...|a_(i-1)].                  (1)

Bars containing a scalar identity are zero. The usual boundary b and
(1) satisfy b^2=B^2=bB+Bb=0: B^2 terms contain an identity bar; in
bB+Bb the products of adjacent factors cancel with the corresponding
cyclic rotations, including the first/last-factor products. These are
finite identities on tensors and extend continuously. Each B_n is
continuous because it is a finite sum of a tensor permutation, insertion
of 1, and scalar quotient maps.

Set Omega^0=S, Omega^1=S dt and Omega^j=0 otherwise. Give Omega the
zero Hochschild differential and mixed differential d(f)=Df dt,
d(f dt)=0. The maps in P123.118 give a strict mixed-complex morphism

    pi:(C,b,B) -> (Omega,0,d).                            (2)

Indeed pi b=0, pi_1 B_0 f=Df dt, and in every positive input degree
both pi B and d pi are zero. P123.118 supplies a continuous section
of pi as graded spaces and a b-chain homotopy bH+Hb=1-s pi.
Thus (2) is already a b-chain homotopy equivalence. The section s is
not asserted to be a morphism of mixed complexes.

## 2. Formal completion: an explicit kernel filling

Let u have homological degree -2. Define the negative cyclic complex
by the coefficientwise product totalization C[[u]] with differential
b+uB. Its degree n consists of coefficients x_j in C_(n+2j), j>=0,
with negative chain degrees taken as zero. Define C((u)) by allowing
finitely many negative powers of u, still with the coefficientwise
product topology in each total degree. In a fixed degree n, the condition
C_k=0 for k<0 supplies a lower bound on j automatically. These are
formal totalizations; no estimate in an analytic value of u is claimed.

Let K=ker pi degreewise. It is closed and preserved by both b and B,
by (2). The homotopy H of P123.118 preserves K: H_0=0, and in higher
degrees its output has degree at least two, where pi vanishes. On K,

    bH+Hb=1.

For a (b+uB)-cycle x=sum_(j>=j0) u^j x_j in K[[u]] or K((u)),
construct a filling y of total degree one higher by

    y_(j0-1)=0,
    y_j=H(x_j-B y_(j-1)).                                (3)

The residual in parentheses is b-closed. Indeed the cycle equation is
b x_j=-B x_(j-1), and the preceding step gives
b y_(j-1)=x_(j-1)-B y_(j-2). Using bB=-Bb and B^2=0 proves the
assertion. Therefore b y_j=x_j-B y_(j-1), and (b+uB)y=x.
Each coefficient depends on finitely many earlier coefficients through
continuous maps. Thus (3) is continuous in the product topology and
preserves the lower bound on u powers. No uniform operator bound in
chain degree is needed for this formal construction.

Consequently (2) induces quasi-isomorphisms

    (C[[u]],b+uB) -> (Omega[[u]],u d),
    (C((u)),b+uB) -> (Omega((u)),u d).                     (4)

There is also a direct topological justification. The graded section
s lifts any target cycle z to s z; its differential is a cycle in K.
Subtract its continuous filling (3) to obtain a source cycle. If a
source cycle maps to a target boundary, lift a target primitive with s;
the difference is a kernel cycle and again has a continuous filling.
In the periodic case the target boundaries are closed and split by the
Green operator below. These constructions give continuous mutually
inverse identifications on periodic homology and closed source boundary
images, not just abstract vector-space isomorphisms.

## 3. Tangential de Rham cohomology with controlled division

P123.103 constructs the frequency-zero projection P_0 and Fourier
multiplier G=(i tau)^-1 off zero, with

    DG=GD=1-P_0,
    rho_m(Gf) <= (log q)/(2pi) rho_(m+1)(f).               (5)

Hence the two-term complex S --D--> S dt retracts continuously to

    K_0[0] direct_sum K_0 dt[1],  K_0=ker D.               (6)

The retraction is P_0 in both degrees and the homotopy from degree one
to degree zero is G. In the periodic complex it is u^-1 G on forms.
It follows from (4)–(6), with homological indexing, that

    HP_(2j)(S) = K_0,
    HP_(2j+1)(S) = K_0 dt,       j in Z,                  (7)

for the formal topological periodic complex just defined. The powers
of u identify the periodic copies. This result supplies an explicit
cyclic-compatible reduction of the same completed boundary shadow.

## 4. The frequency-zero sector is finite for these p,q

Assume, as in the two-prime boundary, that p and q are distinct positive
rational primes. Put U=Z_p^* and H=closure of the subgroup generated
by q in U. A frequency-zero character is exactly a unit character
kappa with kappa(q)=1, equivalently a character of U/H.

Here H is open. For odd p choose m=p-1; for p=2 choose m=2. Then
q^m belongs to 1+p Z_p for odd p, and to 1+8 Z_2 for p=2. Put
b=v_p(q^m-1), which is finite since the positive integer q^m is not 1.
The p-adic logarithm and exponential are inverse continuous isometries
on 1+p^b Z_p and p^b Z_p, respectively (on the logarithm's stated
small-ball domains). Also v_p(log(q^m))=b. Density of Z in Z_p gives

    closure{q^(m n): n in Z}
       =exp(log(q^m) Z_p)=1+p^b Z_p.

Thus 1+p^b Z_p is contained in H. Conversely modulo this subgroup the
closure of the powers of q is its finite cyclic subgroup. Consequently

    r=[U:H]=|U/(1+p^b Z_p)| / ord_(U/(1+p^b Z_p))(q).      (8)

Every zero-frequency character factors through that same finite quotient.
The Fourier description proves

    K_0=C(U/H),       dim_C K_0=r<infinity.                (9)

For example (p,q)=(3,2) gives b=1 and r=1; (p,q)=(2,3) gives b=3
and r=2. These examples illustrate (8), not a selected RH test family.
No density of powers in the whole unit group is assumed.

## 5. Original trace and actual finite determinant target

For the quotient Haar measure of mass a=log q in P123.101, restriction
to (9) is exactly

    tau_Y(f)=(a/r) sum_(v in U/H) f(v).                   (10)

Indeed the quotient Haar measure on the finite group U/H is uniform.
Furthermore tau_Y(Df)=0 by its zero Fourier coefficient, so the same
integration functional on S dt passes to the degree-one de Rham quotient.
This retains the original tangential normalization through (4)–(7).

A single even/odd period of (7) is finite-dimensional in both parities.
Its graded determinant line is

    det_C K_0 tensor (det_C(K_0 dt))^-1.                  (11)

The fixed physical form dt identifies the two factors and trivializes
(11). This is the determinant of the periodic boundary cohomology
pair, not the full source determinant or a regularized Hilbert trace.
In particular (9) does not contradict the divergent heat trace in
P123.103: the topology and inverse (5) are on the stronger Fourier
space, while infinitely many nonzero real frequencies remain bounded
in the Hilbert spectrum.

## 6. Scope of the cyclic comparison

The projection pi uses only multiplication and the physical derivative;
it respects finite-level inclusions and external translations. The Green
operator and the zero-frequency projection have those compatibilities
by their Fourier definitions. Thus the induced homology identifications
retain these boundary maps; no naturality of the auxiliary chosen bar
homotopy for unrelated charts is assumed.

This closes the formal cyclic/periodic comparison for this completed
boundary algebra, with a finite periodic cohomology target and the original
trace normalization. It does not establish entire cyclic convergence,
full smooth orbit Morita transport, geometric descent over all strata,
or identification of (11) with the intrinsic arithmetic ruling/mixed
determinant and its metric. Those remain required for A and mixed RR.
