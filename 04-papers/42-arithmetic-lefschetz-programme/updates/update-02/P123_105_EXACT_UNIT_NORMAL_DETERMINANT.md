# P123.105 — Exact normal determinant renormalization for unit-supported tests

Status: PROVED-IN-REPOSITORY for locally constant
tests on U=Z_q^*. The construction is a determinant germ, with explicit
meromorphic continuation. It is not yet the full normal/external RR line.

## 1. The entire finite-cutoff spectrum

Use D_u and E_MN from P123.042, with L=M+N>=0. For units u, D_u
commutes with E_MN: multiplication by a unit preserves both defining
position and frequency balls. The normal cutoff range identifies with
functions on Z_q/q^L Z_q, after scaling the position variable. The
action is the permutation representation of U on that finite set.

The zero element gives one trivial representation. The nonzero orbits
are the shells of valuation j=0,...,L-1, each isomorphic to U/U_(L-j),
where U_s=1+q^s Z_q. Let c(chi) be the least s>=1 for which chi|U_s=1,
and put c(1)=0. The multiplicity of a nontrivial character chi is

    m_L(chi)=max(L-c(chi)+1,0),
    m_L(1)=L+1.                                            (1)

Indeed chi appears once in each shell quotient U/U_s with s>=c(chi).
This accounts for all cutoff dimensions, including the trivial character
from the zero orbit. The argument includes q=2 without a separate
assumption about nontrivial characters at conductor one.

Let phi be locally constant on U and invariant under U_ell, ell>=1.
Use probability Haar du and define

    A_phi=integral_U phi(u)D_u du,
    a_chi=integral_U phi(u)chi(u)^-1 du.

The labeling of the unit eigenvectors can be chosen so that their
A_phi eigenvalue is a_chi; inversion of characters, if needed, leaves
the conductors unchanged. Only characters of conductor <=ell occur
with a nonzero coefficient. For L>=ell, (1) yields the exact polynomial

    det(1+z E_MN A_phi E_MN)
      =product_chi (1+z a_chi)^(L+1-c(chi)).                 (2)

The determinant on the full Hilbert space is the same finite-rank
Fredholm determinant; the complement contributes eigenvalue one.

## 2. A nonlinear counterdeterminant and exact stabilization

Let A_phi^unit be convolution by phi on the finite unit quotient U/U_ell,
with probability counting measure. Its determinant is

    d_phi(z)=det(1+z A_phi^unit)=product_chi(1+z a_chi).

Refining ell adds only zero eigenvalues, so d_phi is independent of the
chosen sufficiently fine level. Equation (2) proves, as germs at z=0,

    det(1+z E_MN A_phi E_MN) / d_phi(z)^(L+1)
       = Delta_phi(z)
       :=product_chi(1+z a_chi)^(-c(chi)).                  (3)

This is eventual exact equality, not just convergence. Both sides
extend to the same meromorphic function; poles are allowed, and the
ratio at common zeros is understood by that continuation. Near zero
all factors are nonzero, so (3) defines an unambiguous determinant germ.

For example phi=1 gives A_phi the unit-invariant projection. Its cutoff
rank is L+1, so the determinant is (1+z)^(L+1), d_phi=1+z, and
Delta_phi=1. Subtracting only the trace counterterm instead would give

    exp(-z(L+1))(1+z)^(L+1).

Its second Taylor derivative at zero is -(L+1), so it cannot converge
locally uniformly to a holomorphic germ with finite derivatives. Thus
the linear counterterm sufficient for the trace is not sufficient for
the determinant, even for this elementary source test.

## 3. Recovery of the prescribed unit trace

Differentiating (3) at zero gives

    (log Delta_phi)'(0)=-sum_chi c(chi)a_chi,
    Tr(E_MN A_phi E_MN)-(L+1)phi(1)
        =-sum_chi c(chi)a_chi.                              (4)

The second identity follows also directly from (1) and
phi(1)=sum_chi a_chi. The exact unit normal trace calculation of
P123.042, with probability unit Haar, identifies its right side with

    integral_U (phi(u)-phi(1))/|1-u|_q du.                  (5)

Consequently multiplying (4) by log q recovers exactly the unit part
of the earlier local Weil packet, with its original normalization.
This is a trace/determinant derivative comparison; no noninteger power
of the meromorphic determinant is introduced to represent log q.

All higher logarithmic coefficients are determined as well:

    log Delta_phi(z)
      =-sum_(r>=1) (-1)^(r+1) z^r
                         [sum_chi c(chi)a_chi^r]/r          (6)

on a sufficiently small disk. Thus this calculation controls the full
germ, rather than extrapolating it from its first derivative.

## 4. Product, star and exact scope

For unit convolution with probability Haar, let
psi=phi+eta+phi*eta. Then 1+a_chi(psi)
=(1+a_chi(phi))(1+a_chi(eta)). Equations (3) and (6) prove the
corresponding multiplicativity of the relative determinant wherever
the factors are defined, and as meromorphic identities under scalar
parameters. The same spectral formula gives conjugate compatibility
under convolution star. No fixed level is privileged: extra zero
Fourier coefficients contribute determinant one at every refinement.

This proves a full normal determinant renormalization on the compact
unit-supported subalgebra, where the cutoff commutes with the action.
Nonunit dilations do not have that commutation property and their
products mix valuation shells. Their determinant and its coupling to
the tangential induced action require a further calculation. Nor is
(3) yet identified with the geometric determinant line, its arithmetic
metric, multi-stratum gluing or mixed RR required by A.
