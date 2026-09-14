# P123.054 — New-place relative integration and its exact dilation defect

Date: 2026-09-05. Status: PROVED for the new-place divergence and the
relative integration identities on Bruhat tests. A completed semilocal
trace-domain functor is not yet asserted.

## 1. Why ordinary boundary integrability is not chart-stable

The repaired coefficient chart adds chi_ell=1_(Z_ell) at a new prime ell.
Take S_f={p,q}, a nonnegative nonzero g in C_c^infinity(R), and the ideal
test

    i(t,x_p,x_q)=g(t)1_(Z_p^*)(x_p)1_(Z_q)(x_q)

at the identity label. It belongs to the two-prime I_int of P123.051.
Its q-zero boundary integral is integral g(t)dt with unit-probability
multiplicative Haar. The chart image is i times chi_ell. On the q-zero
stratum with p and ell nonzero, its putative unregularized boundary
integral contains

    integral_(Q_ell^*) chi_ell(x)d^*x
       =sum_(j>=0) vol(ell^j Z_ell^*)=infinity.  (1.1)

Thus imposing ordinary multiplicative L¹ on every new single-zero
stratum would exclude the chart image of this existing test. This does
not refute the original rapid coefficient chart, which uses supremum
norms. It specifies the obstruction to this particular integrability
extension of that chart.

## 2. A relative integral compatible with the lattice extension

For a Bruhat function f on Q_ell define

    R_ell(f)=integral_(Q_ell^*)
                     (f(x)-chi_ell(x)f(0))d^*x, (2.1)
    ev_ell(f)=f(0),

where the unit group has multiplicative volume one. The numerator
vanishes near zero and outside a compact set, so the integral converges
absolutely. In particular

    R_ell(chi_ell)=0,  ev_ell(chi_ell)=1.         (2.2)

For the truncated domain Omega_N={x:v_ell(x)<=N}, N>=0, local constancy
at zero gives, for sufficiently large N depending on f,

    integral_(Omega_N) f(x)d^*x-(N+1)f(0)
                           =R_ell(f).           (2.3)

The negative-valuation part is finite by compact support, and chi_ell
has exactly N+1 unit-mass shells in Omega_N. Thus (2.3) is eventual exact
equality. This is a spatial boundary integral; it is not the Fourier
normal dilation trace of P123.042, despite the related shell counting.

## 3. The dilation anomaly is completely explicit

Let alpha_a f(x)=f(a^-1 x), k=v_ell(a). Multiplicative Haar is invariant,
and alpha_a chi_ell=1_(ell^k Z_ell). Therefore

    integral (alpha_a chi_ell-chi_ell)d^*x=-k.

Writing f=(f-chi_ell f(0))+chi_ell f(0) in (2.1) proves

    R_ell(alpha_a f)=R_ell(f)-v_ell(a)f(0),
    ev_ell(alpha_a f)=ev_ell(f).                 (3.1)

The normalized pair (R_ell,ev_ell) hence transforms by an upper triangular
matrix with off-diagonal entry -v_ell(a). The formula composes exactly
because valuations add. It is invariant under units, which include all
old Gamma_S labels at the new place.

This is the explicit compensation term that a semilocal trace domain
must retain. Declaring R_ell dilation-invariant would discard it.

## 4. Chart compatibility and several new coordinates

For an old compact test b and j(b)=b tensor chi_ell,

    (id tensor ev_ell)j(b)=b,
    (id tensor R_ell)j(b)=0.                     (4.1)

For multiple new coordinates, evaluation and R in distinct variables
commute on the Bruhat tensor test space. Indeed each function is a finite
sum of tensor products at finite level, and each regularized factor has
compact multiplicative support away from zero. Fubini then applies to
the subtracted integrands. Consequently the maps (4.1) compose on chart
triples, retaining the old component by evaluation and creating zero
relative component in every added pure lattice factor.

Equation (3.1) also acts tensorwise: each dilation defect is evaluation
in that coordinate, and simultaneous defects produce the corresponding
evaluation terms in several coordinates. This gives explicit lower-layer
terms rather than an assumed cancellation of higher-zero strata.

## 5. A local norm controlling both components

On local Bruhat tests set

    nu_ell(f)=max(||f||_infinity,
                 |f(0)|+integral |f-chi_ell f(0)|d^*x).

Both R_ell and evaluation are bounded by nu_ell, and nu_ell(chi_ell)=1.
Writing f=f(0)chi_ell+r_f gives

    fg-f(0)g(0)chi_ell
       =f(0)chi_ell r_g+g(0)chi_ell r_f+r_f r_g.

Supremum/L¹ estimates prove nu_ell(fg)<=4 nu_ell(f)nu_ell(g).
Complex conjugation is isometric. The completion is thus a Banach star
algebra after an equivalent rescaling of the norm. It embeds in C_0(Q_ell):
uniform convergence and convergence of the subtracted L¹ functions force
their limits to agree, and evaluation at zero is uniform-continuous.
The shell identity yields

    nu_ell(alpha_a f)<=(1+|v_ell(a)|)nu_ell(f).    (5.1)

This supplies a completed local building block with controlled gauge
growth and the correct chart lattice vector. It does not by itself
construct the full twisted semilocal tensor algebra or its trace shadow.

## 6. Next required assembly

Ordinary boundary L¹ cannot simply be imposed after adding primes.
The relative pair above instead has exact lattice-chart compatibility,
explicit dilation covariance and a complete local norm. The remaining
construction must assemble these pairs with the real moments, rapid
Gamma action and layer attaching maps, then compare the resulting source
operation with the Fourier-normalized external character. Neither that
comparison nor full A/B/C closure is inferred from this local repair.
