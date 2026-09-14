# P123.101 — A nuclear completion of the smooth finite-unit boundary algebras

Date: 2026-09-06. Status: PROVED-IN-REPOSITORY for the two-prime
compact boundary Y=B_q. This constructs a declared topology and its
tensor algebra; it does not assert convergence of diagonal resolutions
or determinant corrections merely from density of finite levels.

## 1. Characters with both real and unit complexity controlled

Put a=log q, U=Z_p^*, and Y=(R times U)/((t,u)~(t+a,q u)).
Its continuous characters have the form

    chi_(tau,kappa)(t,u)=exp(i tau t) kappa(u),
    exp(i tau a) kappa(q)=1,                                (1)

where kappa is a finite-order continuous character of U. For a fixed
kappa, the allowed tau form one translate of (2pi/a)Z. These characters
separate points, as also follows through the finite-unit quotients in
P123.099. Denote their countable group by L.

Let N_0=U and N_n=1+p^n Z_p for n>=1. Define c(kappa)=p^n for the
least n with kappa|N_n=1, and

    W(chi)=(1+|tau|) c(kappa).

Then W>=1, W(chi^-1)=W(chi), and W(chi psi)<=W(chi)W(psi).
Indeed conductors of products are at most the larger conductor, while
1+|tau+sigma|<=(1+|tau|)(1+|sigma|).

There is the summability estimate

    sum_(chi in L) W(chi)^(-3)<infinity.                     (2)

The sum of (1+|tau|)^(-3) over a translated frequency lattice is
uniformly bounded in the translate. The number of unit characters of
conductor at most p^n is |U/N_n|<=p^n, so the remaining conductor sum
is bounded by 1+sum_(n>=1) p^n p^(-3n).

## 2. The complete algebra and its relation to the finite levels

Define S(Y) to be the Fourier series

    f=sum_(chi in L) f_hat(chi) chi,
    rho_m(f)=sum_chi |f_hat(chi)| W(chi)^m<infinity for all m>=0.

The series converges uniformly, and character orthogonality makes its
coefficients unique, using probability Haar to extract them. Thus this
is an injectively embedded algebra of actual continuous functions on Y.
The weighted ell1 projective limit is Frechet complete. Submultiplicativity
of W and convolution of the absolute Fourier series prove

    rho_m(fg)<=rho_m(f)rho_m(g),  rho_m(conjugate f)=rho_m(f).

It is unital. The real derivative D=partial_t is continuous, with
rho_m(Df)<=rho_(m+1)(f); all real derivatives therefore exist uniformly.

Every B_N=C^infinity(Y_N) from P123.099 embeds continuously in S(Y):
only finitely many kappa occur at that level, and smooth circle Fourier
coefficients decrease faster than every power of their lattice index.
Conversely on that fixed set of kappa, the rho_m topology is exactly
the usual smooth topology. In one direction, derivative sup norms are
bounded by Fourier ell1 sums. In the other, integration by parts with
two extra derivatives bounds the weighted ell1 sums on each of the
finitely many circles. Thus the inclusion retains each finite-level
topology, rather than merely its underlying functions.

The union of the finite levels is dense in S(Y): finite Fourier sums
belong to that union and converge in every rho_m. This defines the
completion by the displayed seminorms. It is not claimed to be the
strict inductive-limit topology on the union or the entire algebra of
functions merely smooth along the real flow.

## 3. Nuclearity and the completed tensor algebra

The completion for rho_m is weighted ell1(L,W^m). The inclusion from
level m+3 into level m is a nuclear operator: in the normalized coordinate
bases it is the sum of rank-one coordinate operators with coefficients
W(chi)^(-3), whose absolute sum is finite by (2). For every seminorm
there is therefore a stronger one with nuclear bonding map; this proves
nuclearity of this Frechet space by the seminorm criterion.

Moreover S(Y) tensorhat_pi S(Y) is explicitly the double Fourier algebra
with seminorms

    sum_(chi,psi) |b_hat(chi,psi)| W(chi)^m W(psi)^m.         (3)

To prove this, use the isometric projective tensor identity for weighted
ell1 spaces at each pair of seminorms. Conversely a coefficient family
satisfying (3) gives the absolutely convergent tensor series
sum b_hat(chi,psi) chi tensor psi in every projective seminorm.
These inverse maps agree on finite sums and extend by completeness;
equal indices m are cofinal among all pairs of indices. Uniform Fourier
convergence and orthogonality identify (3) injectively with functions
on Y times Y. Thus the completed square coefficient algebra is explicit.

## 4. Unit averaging, external translations and the original trace

Averaging over N_n is the Fourier projection retaining exactly the
characters whose kappa is trivial on N_n. It contracts every rho_m,
commutes with D, and converges strongly to identity by weighted summable
tails. The projections compose by the subgroup tower and preserve Haar
integrals. They are linear projections, not multiplicative maps in general.

External quotient translations multiply each Fourier coefficient by a
unit-modulus phase. They act isometrically in every rho_m and strongly
continuously, first on finite Fourier sums and then by density. Thus
the completed algebra retains the actual boundary action.

For the original quotient measure of total mass a,

    tau_Y(f)=integral_Y f dy=a f_hat(1),
    |tau_Y(f)|<=a rho_0(f).                                 (4)

This extends exactly the finite-level Haar functional. It introduces
neither a new logarithmic normalization nor a selected arithmetic weight.

## 5. Remaining diagonal and determinant comparison

There is now a concrete nuclear Frechet smooth boundary algebra
containing all finite-unit smooth levels with their original topologies,
an explicit completed square, compatible averaging and translations,
and the original continuous trace. These properties supply a domain
on which the next diagonal comparison can be posed precisely.

They do not alone extend the finite free diagonal resolutions of
P123.099 or the deck decompositions of P123.100: their estimates must
be controlled in the conductor weights above. Nor do they prove a
completed smooth orbit-decay Morita theorem or convergence of normal
determinant metrics. Those and the full-source/strata comparisons remain
necessary for the mixed RR and row A.
