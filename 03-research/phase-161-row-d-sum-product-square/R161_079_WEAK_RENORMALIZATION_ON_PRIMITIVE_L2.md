# R161_079 — Weak renormalization on compact primitive L2 sources

## 1. Claim and its scope

The derivative loss in R161_078 can be moved to compact test functions. This constructs a distributional renormalized product on compact L2 primitive sources, including a compactly supported first-contact vector. It does not prove that the product vanishes or that it belongs to the Hilbert carrier of the scattering gate.

Fix T>0 and extend f in L2([-T,T]) by zero. Assume

    integral exp(-u/2) f(u)du=0.                         (1.1)

Both Tate moments may be imposed; only (1.1) is needed for the right-oriented result. Define h=A_loc f in D'(R): the Gamma multiplier acts on the tempered compact source, and the two Euler sums are locally finite. Exact local stabilization from R161_076 remains valid for this definition. The complete h need not be tempered.

For any distribution h and integer N>=1 define

    T_N h(t)=sum_(n<=N) n^(-1/2)h(t+log n)
               -integral_1^N x^(-1/2)h(t+log x)dx.       (1.2)

The integral here is a distributional integral over a compact interval. There is no improper integral or product of distributions.

**Theorem.** Under (1.1), T_N A_loc f converges in D'(R). For tests supported in a fixed [-K,K], the tail is bounded by

    |< (T_B-T_A)A_loc f, phi >|
      <= C_(T,K) ||f||_2 p_J(phi) rho(A),               (1.3)

for integers B>A sufficiently large, where J is finite,

    p_J(phi)=max_(0<=j<=J) ||phi^(j)||_infinity,
    rho(A)=(1+sqrt(log A))exp(-c_0 sqrt(log A))+A^(-1/2).

Constants and the threshold can depend on T,K and the fixed Gamma multiplier, but not on f, phi, B or A. The arithmetic input is exactly the unconditional PNT remainder imported in R161_078. This is a continuity estimate in the source's L2 norm with a distribution-valued output, not an L2 output estimate.

## 2. Move the derivatives to the test

Use bilinear distribution pairing (no complex conjugate) and put check(phi)(t)=phi(-t). Set

    k=f*check(phi).

Then k is smooth and compactly supported in [-T-K,T+K], and

    ||k^(j)||_infinity <= ||f||_1 ||phi^(j)||_infinity,
    integral exp(-u/2)k(u)du
      = [integral exp(-u/2)f(u)du]
        [integral exp(v/2)phi(v)dv]=0.                  (2.1)

One can use the larger open support window (-T-K-1,T+K+1) in R161_078. No regularity of f beyond L1 and compact support is used here.

All operators in (1.2) commute with convolution by a compact test. The locally finite Euler kernel does as well; on any compact output set only finitely many of its shifted terms contribute. The Gamma identity follows from its Fourier multiplier action. Thus

    (A_loc f)*check(phi)=A_loc k,
    <(T_B-T_A)A_loc f,phi>
       =[(T_B-T_A)A_loc k](0).                         (2.2)

For the Euler tail, the proof in R161_078 bounds the right side by a constant times (||k||_infinity+||k'||_infinity+||k''||_infinity) times the first term of rho(A). For the Gamma tail it suffices to bound ||mathcal M k||_infinity and ||(mathcal M k)'||_infinity. Smoothness and polynomial growth of the Gamma multiplier imply that these are bounded by finitely many Schwartz seminorms of k. With fixed compact support these, in turn, are bounded by finitely many sup norms of derivatives of k.

Apply (2.1) and ||f||_1<=sqrt(2T)||f||_2. This proves (1.3). The finite initial T_A A_loc action is also continuous from compact-support L2 sources to distributions. Hence the limit is a distribution and depends continuously on the source on this primitive subspace. This proves the theorem without approximating a radical by purported smooth radicals.

## 3. Renormalized continuum modulo Tate for distributions

A pointwise integration anchor is not meaningful for an arbitrary distribution. Instead choose any distribution v solving

    (partial_t+1/2)v=h.                                (3.1)

Such v exists: take a distributional primitive of exp(t/2)h and multiply it by exp(-t/2). Any two choices differ by c exp(-t/2). Define

    C_N^[v] h=v+integral_1^N x^(-1/2)h(t+log x)dx.

For a smooth h and v(t)=exp(-t/2)integral_a^t exp(y/2)h(y)dy, this is exactly C_(N,a)h from R161_077. For general h it is a justified extension modulo the negative Tate mode. Consequently

    (S_N-C_N^[v])A_loc f = T_N A_loc f-v

converges in distributions for any fixed v, and its class modulo span{exp(-t/2)} is independent of v. Equivalently its pairing is canonical on compact tests phi satisfying integral exp(-t/2)phi(t)dt=0.

This quotient is not the L2 orthogonal projection Pi_K. An arbitrary distribution need not admit that Hilbert projection. Any use of Pi_K here requires additional regularity, not a change of notation.

Reflection gives the left-oriented construction when the other primitive moment vanishes. Thus a source satisfying both Tate conditions has both weak orientations, each modulo its corresponding Tate ambiguity.

## 4. What this changes, and what it cannot change

R161_078's source-regularity obstruction is removed for the distribution topology: compact L2 first-contact vectors are now legitimate inputs to this weak renormalization. This is an extension of the smooth construction, not a new arithmetic annihilation law.

In particular, smoothing f has NOT preserved the compressed equation H_T f=0. Convolution expands support, and compression does not commute with convolution. Only the primitive moments and the global translation-invariant A_loc action were transported in (2.1)-(2.2). Declaring k to be a smooth first-contact vector would invalidate the argument.

Nor does convergence identify the value of the limit. Even a later proof that a zeta product is zero in distributions would not imply that A_loc f is zero or that its exterior energy vanishes: R161_075 distinguishes this from injective L2 multiplication.

To use this limit for D still requires an independently proved equality-state law controlling the exterior remainder (or its Gamma moments), with sufficient topology for the physical compression and quadratic pairing. No such law is supplied by (1.3). Arbitrary joint M,N cutoff limits are also not asserted.

Status: weak renormalization and its source-norm tail estimate proved with the stated PNT input; Hilbert graph transport and equality-state annihilation remain unproved. D is not closed.
