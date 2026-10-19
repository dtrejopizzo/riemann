# R183.015 — Trace class and sign on the modulus sector

## Statement — PROVED

In H=L²(R,ds), let P be the Hardy projection with kernel
δ(s-t)/2 + (2πi)^(-1) pv(1/(s-t)). Let u be smooth, |u|=1, whose
derivatives of every order grow at most polynomially. For φ in
Schwartz space, M=M_φ, the operator

    D=M* (M_u* P M_u-P) M

has a Schwartz kernel, is trace class, and satisfies

    Tr D = (i/(2π)) ∫ |φ(s)|² conjugate(u(s)) u'(s) ds.

If u=e^{iθ}, this is -(2π)^(-1)∫|φ|² θ'. The orientation matches
the negative-Fourier and positive-half-axis conventions used in
Connes–Consani.

## Proof of the kernel and of trace class

The delta contribution cancels exactly. The remaining kernel is

    K(s,t) = conjugate(φ(s)) φ(t) conjugate(u(s))
             × [u(t)-u(s)]/[2πi(s-t)].

The singularity is removable because

    [u(t)-u(s)]/(t-s) = ∫_0^1 u'(s+r(t-s)) dr.

All derivatives of this quotient have polynomial growth in
(s,t). Multiplying it by the two Schwartz factors produces K in S(R²).
Its diagonal is i|φ(s)|² conjugate(u(s))u'(s)/(2π).

To justify trace class without a merely formal diagonal evaluation, take
A=1-d²/ds²+s². Its eigenvalues are 2n+2, so A^(-1)
is Hilbert–Schmidt. The operator with kernel A_s K(s,t) is Hilbert–Schmidt
because that kernel belongs to L²(R²). Hence D=A^(-1)(AD) is a product
of two Hilbert–Schmidt operators and is trace class. The expansion of K
in Hermite functions has rapidly decreasing coefficients; this
allows integrating the diagonal term by term and gives the formula for Tr D.

## Application to the semilocal product — PROVED

We work in the trivial sector of the compact group, identified via
the modulus with the real variable s. For finite S and z=1/2+is,

    u_S(s) = π^(-is) Γ(1/4+is/2)/Γ(1/4-is/2)
             × ∏_{p in finite S} (1-p^(-1/2+is))/(1-p^(-1/2-is)).

Each prime factor and all its derivatives are bounded: its denominator
has modulus at least 1-p^(-1/2)>0. The Gamma factor is unimodular;
its logarithmic derivative is i[Re ψ(1/4+is/2)-log π]. Stirling's
estimates with derivatives on that line give logarithmic growth of
the first phase derivative and at most polynomial growth of all
derivatives of u_infinity. The finite product satisfies the hypotheses.

For h in C_c^∞(R), φ(s)=∫h(t)e^(-ist)dt is Schwartz. This proves
trace class for D and R183.014's limit for these tests in this sector.
No extension to all characters nor to all h in L² is claimed here.

## Exact phase computation — PROVED

The absolutely convergent expansion of the logarithm of each prime factor
gives

    θ'_S(s) = m(s) - 2 Σ_{p in finite S} Σ_{k≥1}
                          (log p) p^(-k/2) cos(ks log p).

Hence

    -Tr D = (1/(2π)) ∫ m(s)|φ(s)|² ds
             - 2 Σ_{p in finite S} Σ_{k≥1}
                   (log p) p^(-k/2) Re c_h(k log p).

Here c_h(a)=∫h(t)conjugate(h(t-a))dt. If supp h⊂(-T,T),
the contributions with k log p≥2T vanish. If S contains all
primes p<exp(2T), this is exactly the archimedean part minus the
prime part of the energy. For tests with ∫h(t)e^{±t/2}dt=0,
the polar term also vanishes: -Tr D is the sought primitive energy.

The orientation is thus verified twice: via the kernel diagonal and
via the positive coefficients of Λ in the original energy.

## What remains unproved

The sign Tr D≤0 does not follow from trace class. R183.013's relative
determinant has derivative Tr D and does not by itself add an
inequality. The pending task is an Euler–Poisson comparison proving
that sign on the primitive tests for every T. This file removes the
domain blockage on the smooth kernel of the modulus sector; it does not
close D.

## Transfer test upon adding a prime — PROVED

Let p be outside S, a=log p, and E_S(h)=-Tr D_{S,h}. The exact formula
gives

    E_{S∪{p}}(h)-E_S(h)
      = -2(log p) Σ_{k≥1}p^(-k/2) Re c_h(ka).

That increment has both signs even on smooth primitive tests.
To verify this without approximations, take ε<a/4 and a real nonzero
function b in C_c^∞((-ε,ε)); set g=b''-b/4. Integration by parts gives
∫g(t)e^{±t/2}dt=0. g is not zero, since a compactly supported solution of
g=0 would force b''=b/4 and, by uniqueness, b=0.

Define h_+(t)=g(t)+g(t-a) and h_-(t)=g(t)-g(t-a). Both are primitive,
because translating g multiplies each vanishing moment by e^{±a/2}.
Separation of supports gives exactly

    c_{h_+}(a)=||g||²,    c_{h_-}(a)=-||g||²,
    c_{h_±}(ka)=0 for k≥2.

Hence the increments are, respectively,

    -2(log p)p^(-1/2)||g||² and +2(log p)p^(-1/2)||g||².

After translating the whole test by -a/2, both fit in
(-a/2-ε,a/2+ε); the moments remain zero and the autocorrelation
does not change. The conclusion only refutes monotonicity of E_S(h) for a
fixed h upon adding p. It does not refute a transport h↦J_p h with a
variable metric, nor does it prove that the total energy is negative.
For that alternative, J_p must be built and the archimedean term must also
be compared; the Sonin isomorphism cited in phase 116 does not by itself
provide that comparison.

## Domain of the transport by one prime — PROVED

The positive realization of a prime's Poisson kernel already appears in
phase 116 v94, (361)–(366). It is not claimed here as a new mechanism.
Its resolvent in the causal orientation is

    R_p h(t)=Σ_{k≥0}e^(-ka/2)h(t-ka),  a=log p.

It is bounded on L² by the geometric series of unitary translations. However,
it does not in general preserve the space of compact primitive tests.
If supp h⊂[-T,T], for t>T one obtains exactly

    e^(t/2)R_p h(t)=Π_a q(t),
    q(t)=e^(t/2)h(t),    Π_a q(t)=Σ_{k in Z}q(t-ka).

The bilateral sum is locally finite and a-periodic. Negative indices
do not contribute when t>T, which proves the equality with the causal
series. The positive Tate moment only says

    ∫_0^a Π_a q(t)dt = ∫_R q(t)dt = 0.

It does not say that Π_a q is identically zero. If it is not,
∫_T^∞ e^(t/2)|R_p h(t)|dt=∞ and the tail of R_p h does not vanish.
For an exact example, take h=b''-b/4 nonzero with support of length
less than a: it is primitive, but the copies of q do not overlap and
Π_a q≠0.

The full condition Π_a q=0 is equivalent to all the equalities

    Fourier(h)(2πj/a+i/2)=0,    j in Z,

via the Fourier coefficients of the periodic function. The positive
Tate moment imposes only j=0. This locates the loss of domain exactly:
the inverse of a single Euler factor introduces an entire lattice of
cancellation conditions, not just Tate's polar residue.

This does not refute the transport between Sonin spaces within their
proper domains. It does prevent identifying that transport, without proof,
with a map preserving the compact primitive tests of the trace
inequality.
