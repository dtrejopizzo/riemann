# P3 through the quarter-twisted Calderon problem

Status: the quarter twist, its Hardy spectrum, the Gamma reservoir and its
constant connection coefficient are proved in Sections 1--2. The local
boundary channels are fixed; the single global gluing lemma in Section 6 is
the proof target. No positivity of `B_nuc` is used to define these objects.

## 1. Geometric input and the origin of the quarter

For every prime `p`, Connes--Consani canonically give

    E_p = C_p x X_phase,
    length(C_p)=log p,
    length(X_phase)=2 pi,

with complex structure determined by the invariant forms `d lambda/lambda`
and `d theta`. All primes share the same phase circle.

The determinant line is centrally self-dual, hence carries the half-density
character `s=1/2`. This statement determines the phase holonomy without an
appeal to the explicit formula. In polar coordinates `z=lambda exp(i theta)`,

    |z|^s = (z conjugate(z))^(s/2).

Holomorphic polarization retains the factor `z^(s/2)`. Under
`theta -> theta+2 pi` it has monodromy `exp(2 pi i s/2)`. Consequently the
polarized line has

    alpha = s/2 = 1/4,

and the holomorphic Hardy spectrum is

    a_n = n+1/4,  n>=0.

This proves the geometric source of the quarter at the central point from the
central metric and the complex polarization of the common phase circle. The
Hardy restriction is canonical: it is the nonnegative Fourier polarization
selected by the complex structure of `C^x`. There is no normalization
parameter.

## 2. The common-phase positive energy

Let `L_(1/4)` be that phase line. After Fourier decomposition along
`X_phase`, the positive radial/phase energy has masses `a_n`. Its boundary
gradient on a logarithmic profile `F` is

    Fourier((W_Gamma F)_n)(tau)
      = (tau/2)/sqrt(a_n (a_n^2+(tau/2)^2)) Fourier(F)(tau).

Therefore

    ||W_Gamma F||^2
      = integral g_Gamma(tau) |Fourier(F)(tau)|^2 d tau/(2 pi),

    g_Gamma(tau)
      = sum_(n>=0) (tau/2)^2/[a_n(a_n^2+(tau/2)^2)]
      = Re psi(1/4+i tau/2)-psi(1/4).

The last equality follows directly from

    psi(alpha+i x)-psi(alpha)
      = sum_(n>=0) [1/(n+alpha)-1/(n+alpha+i x)]

by taking real parts at `alpha=1/4`, `x=tau/2`. Thus the forced Gamma Green
operator is the Dirichlet energy of the common quarter-twisted Hardy phase.
It is not imported from `B_nuc` and it is not fitted.

The constant term comes from the same object. For the positive twisted Hardy
operator `D_alpha` one has the Hurwitz-zeta determinant

    det_zeta(D_alpha)=exp(-zeta'(0,alpha))=sqrt(2 pi)/Gamma(alpha).

After applying the canonical archimedean metric factor `pi^alpha`, its
connection coefficient in the holonomy direction is

    d/dalpha log(pi^alpha/Gamma(alpha))
      = log pi-psi(alpha).

At `alpha=1/4` this is exactly

    m_0=log pi-psi(1/4).

Hence both `g_Gamma` and `m_0` are respectively the positive variation and
the connection coefficient of one quarter-twisted determinant line.

There is a real-space form which ties this determinant to the same dilation
carrier used by the places. For `a_n=n+1/4`, define the Markov contraction

    (R_n F)(t)=a_n integral exp(-2a_n|t-s|)F(s)ds.

Its Fourier multiplier is

    4a_n^2/(4a_n^2+tau^2).

Consequently, as a monotone sum of positive forms,

    G_Gamma=sum_(n>=0) a_n^(-1)(I-R_n).

Indeed its `n`-th multiplier is
`tau^2/[a_n(4a_n^2+tau^2)]`, the summand already proved above. The kernel
`exp(-2a_n|t-s|)` is the Gram of normalized translated exponential states
on a half-line. Thus the quarter-phase Green and the half-density Frobenius
dilation admit a common exponential translation carrier. This constructs the
required Green source, not yet the global four-port attachment: the latter
must still reproduce the D.247 degree/contact wiring without an additional
boundary term.

## 3. Prime returns and the unique boundary metric

For `q=p^j`, set

    ell_q = j log p,
    w_q = log p/sqrt(q),
    c_p = 2 pi/log p,
    beta_q = sqrt(w_q/c_p)
           = log p/sqrt(2 pi) p^(-j/4).

The first equality for `beta_q` is forced by the Hodge norm of the integral
harmonic form on `E_p`; the second is its value. Frobenius gives the oriented
return edge `(V_(ell_q)F,F)`. The phase polarization gives its unitary
Hadamard boundary coordinates

    B_q^- F = sqrt(w_q/2)(V_(ell_q)-I)F,
    B_q^+ F = sqrt(w_q/2)(V_(ell_q)+I)F.

This derives both prime channels from the absolute Tate cylinder. Positivity
of `w_q` is exactly where Davenport--Heilbronn fails. Frobenius coherence
keeps `q=4` on the same `p=2` cylinder rather than introducing a second
place.

There is also an exact local complex, not merely a pair of operators. For
`H=L^2(R)` and `V=V_(ell_q)`, put

    0 -> H --E_q--> H direct-sum H --J_q--> H -> 0,
    E_q F=(VF,F),
    J_q(a,b)=a-Vb.

It is acyclic: `E_q` is injective, `J_q` is surjective, and
`ker J_q=graph(V)=im E_q`. The normalized Hadamard dagger rotates `E_qF` to

    ((VF-F)/sqrt(2),(VF+F)/sqrt(2)),

and the Hodge metric `w_q` turns these two entries into exactly
`B_q^-F,B_q^+F`. Thus every Frobenius return is an acyclic metrized cone. It
contributes determinant/contact energy but no new cohomology. Coherent
composition of the `V_(j log p)` is precisely the Witt/Frobenius composition
law, so `q=4` is an iterate in the same cone system.

More strongly, the central metric packages the whole tower into one strict
contraction

    C_p=p^(-1/2)V_(log p).

Its canonical Poisson observation map

    O_p=sqrt(1-p^(-1))(I-C_p)^(-1)

has the exact Gram

    O_p^*O_p-I
      =sum_(j>=1) p^(-j/2)(V_(j log p)+V_(-j log p)).

Thus multiplication by `log p` recovers every physical coefficient
`Lambda(p^j)/sqrt(p^j)` from a single place object. This is the invariant P3
replacement for an iterate-indexed list of channels. The minimal unitary
dilation of `C_p` is canonical, so the local return tower already has a
unitary colligation before any comparison with `B_nuc`.

In fact all places have one simultaneous dilation. On

    K=L^2(R_t) tensor L^2(R_+),

let `S_a` be the unilateral right shift, let `k(x)=exp(-x/2)`, and embed
`JF=F tensor k`. Then

    J^*(V_a tensor S_a)J=exp(-a/2)V_a.

The cross-place orbit Gram is already non-diagonal:

    <U_a JF,U_b JG>
      =exp(-|a-b|/2)<V_aF,V_bG>.

At `a=log n` the right side is exactly `C_n=n^(-1/2)V_(log n)`. Hence the
whole Witt semigroup `C_m C_n=C_(mn)` is the compression of one isometric
translation semigroup, whose bilateral dilation is unitary. This common
half-density state is the first explicit global cross-place carrier: it is
constructed before `B_nuc`, and distinct primes act in the same dilation
space rather than in orthogonal place blocks.

## 4. Incoming and outgoing traces

For a finite Frobenius-closed set `S`, define from geometry

    X_S F = (W_Gamma F, (B_q^- F)_(q in S)),
    Y_S F = (sqrt(m_0) F, (B_q^+ F)_(q in S)),

where

    m_0 = log pi - psi(1/4).

Here `m_0` is the holonomy-connection coefficient of the zeta-regularized
quarter-twisted Hardy determinant computed in Section 2. It is not an
independent constant.

The already proved analytic identities give

    X_S^*X_S = R_S,
    Y_S^*Y_S = L_S,

and only afterwards row (c) identifies

    R_S-L_S = -B_nuc,S.

Equivalently, grouping by place and writing

    theta_T=sum_(p<exp(2T)) log p,

one has the exact positive factorization

    R_T^pl=G_Gamma,T+theta_T I,
    L_T^pl=m_0 I+sum_(p<exp(2T)) log p O_(p,T)^*O_(p,T),
    A_T=R_T^pl-L_T^pl.

This is the preferred P3 factorization: Frobenius coherence and the
place-indexed unitary dilation are visible, and `q=4` is automatically the
second coefficient of `C_2`.

## 5. Scattering orientation and the minus sign

Before imposing the source condition, there is an exact scattering check
which fixes the orientation of every boundary component. Put

    b_infty(tau)
      = pi^(-i tau) Gamma(1/4+i tau/2)/Gamma(1/4-i tau/2).

It is unimodular for real `tau`, and

    (1/i) d/dtau log b_infty(tau)
      = Re psi(1/4+i tau/2)-log pi
      = g_Gamma(tau)-m_0.

For a prime put `r=p^(-1/2)`, `z=exp(i tau log p)` and take the disk
Blaschke factor

    b_p(z)=(z-r)/(1-rz).

Its boundary phase derivative is the positive Poisson kernel

    (1/i) d/dtau log b_p(exp(i tau log p))
      = log p [1+2 sum_(j>=1) p^(-j/2) cos(j tau log p)].

The constant term is the equal norm carried by the two oriented sheets and
cancels in the Hadamard input/output difference. The remaining Fourier
coefficients are exactly the prime-power contacts. Thus `A=-B_nuc` is the
relative Wigner--Smith boundary form: the archimedean component has the outer
orientation and each Frobenius cylinder has the inner-boundary orientation.
This fixes the otherwise dangerous minus sign geometrically.

The global theorem is therefore not the claim that an arbitrary phase
derivative is positive. It is the source-free Green identity for a common
outer boundary with its Frobenius inner boundaries. Forgetting the common
filling loses precisely the desired sign.

## 6. Why the two Tate equations are the right source condition

On a compactly supported logarithmic profile, the two polar conditions have
an exact source-complex interpretation. Put

    L_0=-d^2/dt^2+1/4.

Its Green kernel is `exp(-|t|/2)`. Therefore

    G_F(t)=integral exp(-|t-s|/2)F(s)ds

satisfies `L_0 G_F=F`, and outside the support of `F` its two tails are

    G_F(t)=exp(-t/2) M_+(F)  on the right,
    G_F(t)=exp( t/2) M_-(F)  on the left.

Consequently

    ker M_- intersect ker M_+ = L_0(C_c^infinity)

with a unique compactly supported potential. The two obstruction pairings
are

    M_-(F)=integral F(t)e^(-t/2)dt,
    M_+(F)=integral F(t)e^( t/2)dt.

Hence the Fredholm compatibility condition is exactly

    P_T = ker M_- intersect ker M_+.

This proves, already at the polar complex, that the two Tate modes are the
full compact-support obstruction. The remaining gluing theorem must show that
attaching the Frobenius cylinders introduces no additional cokernel.

At the algebraic test-function level, one obtains only an acyclicity
statement, not the asserted adjoint-cokernel statement. Index the Witt
semigroup by the filtered divisibility
category `(N^x, divides)` and use the isometries
`V_(log n) tensor S_(log n)` as transition maps. Every return complex in
Section 3 is acyclic, and filtered colimits of vector spaces are exact.
Therefore the homotopy colimit of the return cones is acyclic relative to the
common phase carrier. Its attachment to the polar complex adds no algebraic
cohomology. This does **not** determine the adjoint cokernel after choosing a
metric and closing the differential: closed range can fail and a boundary
defect can appear. Thus it does not yet prove that the two polar modes exhaust
the analytic cokernel.

For a finite support window the truncation is not a closed filtered category;
its missing successors are literal outgoing boundary ports. More precisely,
for `a=log p` the Poisson state has the stabilized trace

    T_pF(r)=sqrt(1-exp(-a))
      sum_(ell in Z) exp((r+ell a)/2)F(r+ell a),
      r in R/aZ.

Its mean is `sqrt(1-exp(-a)) M_+(F)`. Hence primitivity removes only the
constant mode and leaves the canonical defect space
`L^2_0(R/(log p)Z)`. Zero extension retains these ports, but does not wire
them. The analytic construction must pair the direct sum of these periodic
traces with the Gamma boundary, prove closability, and show that Green's
formula has no residual Maslov term.

## 7. The one theorem to prove

**Quarter-twisted passive gluing conjecture.** Let `S` be finite and closed under
the Frobenius predecessors which act in the chosen support window. Glue the
corresponding Tate cylinders along their common phase circle, with the
determinant metric and real involution above. Then every
`F in ker M_- intersect ker M_+` has a unique minimal-energy extension `u_F`
and Green's identity is

    ||X_S F||^2 - ||Y_S F||^2 = ||d_(1/4) u_F||^2 + ||delta_S u_F||^2.   (C)

Both terms on the right are ordinary positive Hodge norms. Equivalently, the
outgoing trace is the compression of the unitary Calderon scattering map:

    Y_S P = Theta_S X_S P,
    ||Theta_S||<=1.

The conjecture cannot be invoked as a theorem. It would follow from an
explicit global Dirac domain with the stated trace maps. The proof attack has
three required strokes:

1. take the derived pushout of the acyclic return cones over the common
   quarter-twisted phase and close its positive Dirac form;
2. use local acyclicity plus the compact polar-potential lemma to identify
   its adjoint kernel with exactly the two polar modes;
3. apply the standard Green formula, checking the Frobenius boundary terms
   in the Hadamard coordinates of Section 3.

The first stroke is presently incomplete: the local return cones and their
individual dilations do not specify how the D.247 defect complements are
identified with the Gamma boundary space. A unitary extension exists but is
not canonical, and choosing it by matching the desired boundary form would
be circular. See `P3_EXPLICIT_DIRAC_ATTACK.md` for the exact criterion.

No spectral sign test and no Galerkin limit belongs in this proof.

## 8. Consequences if (C) is established

Comparison with row (c) gives, with no loss,

    -B_nuc,S(F,F)=||d_(1/4)u_F||^2+||delta_Su_F||^2>=0.

At `S={2,3,4}` this closes the first open endpoint directly. Under compatible
inclusions of the finite pushouts, monotone convergence of the positive
energies defines the global closed form; the raw boundary masses need not
converge separately. This is the correct renormalization: pass to the bulk
energy identity before taking the cofinal limit.

For a number field, the same proof uses one cylinder per place and would give
GRH for its Dedekind zeta. For a function-field curve, the phase Dirac is
replaced by finite-dimensional polarized `H^1`, recovering Weil. The shifted
pair fails because two self-dual contact lines cannot descend to the single
indecomposable quarter-holonomy line.

## 9. Immediate kill conditions

The construction is rejected if any of the following occurs:

- the central character fails to polarize to the quarter-holonomy line;
- the adjoint kernel contains more than the two Tate modes;
- Frobenius gluing produces an extra boundary term in Green's identity;
- the zeta-regularized polar mass is not exactly `m_0`;
- the finite energies fail to be compatible under Frobenius-closed inclusion.

These are algebraic/analytic identities, not numerical positivity tests.
