# LINK_009 — Test of a direct continuous-flow realization of the module

2026-10-19. Principal constructor. PROVED, independent review approved in AUDIT_009.
This tests a proposed connection to the continuous Mellin carrier, rather
than constructing another positive auxiliary norm. D remains OPEN.

## 0. Corpus check and precise new reason

Consulted index, grid, crossword, Paper44 no-interpolation statements and
CONSTRUCTOR_007–008. Paper44 discusses interpolation of its Frobenius family. Its unrestricted
no-interpolation wording is NOT used here: arbitrary continuous interpolation
without a semigroup law is possible (see SCOPE_P44_009.md). This note does
not retry that family or depend on its support argument. The new object is V_n in the positive Hilbert completion of −R.
The Gaussian component could in principle have changed the continuity
question. We test whether THIS normalized representation is the restriction
or even a compression of a strongly continuous logarithmic unitary flow.

The proof uses an explicit vector and its arithmetic isometric component.
It does not invoke support discreteness of measures or zero information.
It does not exclude all representations of Q_T, all continuous embeddings,
or arbitrary non-semigroup interpolation. Power-rescaled semigroup samples
are treated explicitly below; their unitary compressions are not all excluded.

## 1. A concrete arithmetic vector

Use 0<alpha<1/2, s=2alpha, kappa=−Z_alpha>0 and H_alpha of007.
Take

    A=X_2−1/2,   E_1 A=0,   E_s|A|²=1/4.

For integers n,m odd and coprime, multiplication or division by either
integer does not change the2-adic valuation. Thus on the joint divisibility
event,

    (D_n A)(N)(D_m A)(N)=1_(nm|N)|A(N)|².

Independence of the2-adic coordinate from the primes of nm under P_s gives

    E_s[V_n A overline(V_m A)]=(nm)^(-s/2)/4,
    E_s|V_n A|²=E_s|V_m A|²=1/4.

Consequently

    ||V_n A−V_m A||²_(H_alpha)
      >= (kappa/2)[1−(nm)^(-s/2)].                 (1)

This uses the positive arithmetic summand of the norm only. There is no
negative Gaussian term that could cancel this bound.

Choose n_k=2k+1 and m_k=2k+3. They are coprime odd integers, while
log(m_k/n_k)->0. The lower bound in(1) tends to kappa/2>0.
The Gaussian difference actually tends to0 by

    ||G_n T A−G_m T A|| <= sqrt(Pi(A))(n^(-1/2)+m^(-1/2)),

so the full squared difference tends to kappa/2. Only the lower bound is
needed in the next result.

## 2. No strongly continuous semigroup interpolation of V_n

**Theorem1.** There is no strongly continuous semigroup of bounded operators W(t),
t>=0, on H_alpha satisfying W(log n)=V_n for every integer n>=1.

Proof: the semigroup law and the known bound ||W(log n)||=||V_n||<=1 give

    ||V_m A−V_n A||
      =||W(log n)[W(log(m/n))A−A]||
      <=||W(log(m/n))A−A|| ->0

along the sequence above. This contradicts(1). No uniform bound away from
the sampled times is needed. Strong continuity is only used at0.

**Corollary1.1.** For any real beta there is no strongly continuous semigroup
with W(log n)=n^beta V_n for every integer n. Indeed e^(-beta t)W(t) would
be a strongly continuous semigroup interpolating V_n, which is impossible.
In particular, the unnormalized operators D_n=n^(-s/2)V_n also cannot be
interpolated by such a semigroup. This does NOT exclude an arbitrary
continuous path through those values without the semigroup law.

## 3. Not even a compression of a strongly continuous unitary flow

**Theorem2.** There are no Hilbert space K, fixed bounded maps J:H_alpha->K
and P:K->H_alpha, and a strongly continuous unitary group U(t) on K such
that

    P U(log n)J=V_n   for every n>=1.

In particular, a usual isometric unitary dilation with compression is
impossible for these exact normalized operators.

Proof: using unitarity and the group law,

    ||V_m A−V_n A||
      <=||P|| ||[U(log(m/n))−I]J A|| ->0,

again contradicting(1). The result concerns fixed bounded J,P. Changing
maps with n, unbounded maps or restricting the set of n changes the claim.

## 4. What the test does and does not decide

The natural attempt to obtain the real Mellin semigroup by interpolating
V_n, or any power rescaling including D_n, fails for this module. A new carrier
map cannot assume such a flow or a unitary compression and then use its
spectral theorem as if it had already been constructed.

This is **not** a NO-GO for O1 or D. In particular:

- D_n are also excluded as samples of a C0 semigroup by Corollary1.1.
  Their values as compressions of a unitary group are a DIFFERENT question: 
  such compressions need not satisfy the semigroup law for all real times.
  Theorem2 does not resolve that question for D_n, since their amplitudes
  decay. No unnormalized compression impossibility is claimed.
- A different realization using the full Poisson identity and a different
  domain might supply a useful form; it requires its own construction.
- The known Gaussian inversion from008 still has its adjoint defect.
- No trace or equality with Q_T follows from either the positive kernel or
  the present negative interpolation result.

The next candidate must specify whether it uses D_n, V_n, a compression,
or another observable, and calculate the resulting gamma, prime comb and
polar terms. Merely declaring a continuous generator for V_n is no longer
an admissible step.
