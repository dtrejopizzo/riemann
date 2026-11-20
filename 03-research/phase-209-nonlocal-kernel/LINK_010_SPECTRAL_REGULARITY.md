# LINK_010 — Necessary regularity for a compression of D_n

2026-10-19. **PROVED, independent review favourable in AUDIT_010.md.**
The Q_T link is not constructed nor is a general compression discarded.

## Class and prior consultation

Consulted the routes index (including archive 06), corpus 209, master grid and
crossword: the exclusion of V_n compressions is not reused as if it covered
D_n. The new question keeps the amplitudes n^(−s/2) and adds an explicit
hypothesis of spectral regularity on finite arithmetic vectors. The proof
of 009 only gave distances that now tend to zero; here their rate is computed.
No positive extension theorem is used, nor is it assumed that compressions
inherit a semigroup law.

## 1. Increments of exact order along a sequence

Use H_alpha of 007, s=2alpha in (0,1) and kappa>0. Let A be nonzero in the finite
algebra of divisibility observables, centred by E_1 A=0. Let S be the finite
set of primes appearing in its indices and L a positive even integer divisible
by all of them (for example 2 times their product). Take

    n_k=1+kL,  m_k=n_k+L,  h_k=log(m_k/n_k).

Then n_k,m_k are coprime to each other and to S. Dividing by them does not change
the valuations of S: D_n A=X_n A and D_m A=X_m A. If a=E_s|A|²>0,

    E_s|D_n A−D_m A|²
      =a[n^(−s)+m^(−s)−2(nm)^(−s)].

The positivity of the two components of the norm of 007 implies

    liminf_k ||D_m A−D_n A||² / h_k^s >= 2 kappa a/L^s >0.       (1)

Indeed n h_k→L, m/n→1, while n^s(nm)^(−s)→0. There is no need to
compute the Gaussian component: it cannot subtract from the bound.
The strict positivity of a follows from the linear independence of the
finite indicators under the law P_s, already proved in 005.

## 2. Necessary regularity theorem

Suppose fixed bounded maps J:H_alpha→K and P:K→H_alpha, a strongly
continuous unitary group U(t)=exp(itB), and

    P U(log n)J=D_n,   n>=1.                                    (2)

Neither P=J* nor J isometric is required. For every A as above, the positive
spectral measure mu_A(E)=||1_E(B)JA||² necessarily satisfies

    integral |lambda|^s dmu_A(lambda)=infinity.                  (3)

Proof. If that moment were finite, the spectral theorem would give

    ||[U(h)−I]JA||²/h^s
      = integral |exp(ih lambda)−1|²/h^s dmu_A(lambda) →0.

Dominated convergence applies: for 0<s<2,
|exp(ix)−1|²<=4|x|^s and the pointwise quotient tends to zero.
But unitarity and (2) imply

    ||D_m A−D_n A|| <= ||P|| ||[U(log(m/n))−I]JA||,

contradicting (1). This proves (3).

Equivalently: JA does not belong to Dom(|B|^(s/2)) for ANY nonzero centred finite
arithmetic observable. At alpha=1/4, the absolute spectral moment 1/2
is excluded, or the domain Dom(|B|^(1/4)). It is essential not to confuse
the order of the moment with the power of the domain.

## 3. Scope for the sought link

The class of links (2) that additionally map even one of those
observables to a vector with finite spectral moment s is discarded; in particular,
an identification mapping all of them to spectrally smooth vectors.
The mere C0 group does NOT require that moment: there is no contradiction for a
compression with sufficiently irregular images. The general compression
of D_n remains OPEN.

Nor has it been proved that a map from the smooth tests of Q_T must invert
this correspondence or send an observable A of this type to a smooth vector.
Such a claim requires a concrete map and its domain. This result is not used
to exclude all representations of Q_T nor to pay for gamma,
comb or pole. D remains OPEN; full goal active.
