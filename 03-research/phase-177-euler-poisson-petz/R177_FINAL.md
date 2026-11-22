# R177 — Euler–Poisson recovery law: finite test and obstruction

## Verdict

**NO-GO (PROVED) for the canonical construction via conditional mutual
information/Petz.** The exact normalization `Lambda*1=log` produces a channel
conditioned on the product `n=dk`. Every information loss of that channel
decomposes along the divisor fibers of `n`. On a fiber of cardinality one, the loss,
its Hessian, and the recovery defect are identically zero. The fibers of the
primes `2` and `3` have cardinality one, while Paper 46's physical form
has nonzero atoms at `log 2` and `log 3`. Hence no Petz Hessian of this class
can equal `Q_(N,L)`, even before dealing with Gamma or the poles.

## 1. The canonical arithmetic channel

For a finite cutoff let

\[
 \Omega_N=\{(d,k):dk\leq N,\ \Lambda(d)>0\},\qquad m(d,k)=dk.
\]

The ordinary identity

\[
 \sum_{d\mid n}\Lambda(d)=\log n
\]

defines, and only defines, with no additional data, the conditional law

\[
 a_{d\mid n}={\Lambda(d)\over\log n}\quad(d\mid n).
\tag{1.1}
\]

Let `A` be an arbitrary auxiliary register (which may in particular contain
the full Poisson orientation). The canonical class of states built from
(1.1) is

\[
 \rho_{DNA}=\sum_n q_n |n\rangle\langle n|_N\otimes
 \sum_{d\mid n}a_{d\mid n}|d\rangle\langle d|_D\otimes\rho_{A\mid d,n},
\tag{1.2}
\]

where `rho_(A|d,n)` may depend on `F` through any controlled channel,
including Fourier/Poisson. The coarse-graining forgets `D` and keeps `N,A`.

This is the direct realization of the experiment: first the integer
`n` is known, then one of its von Mangoldt divisors is chosen via (1.1), and the
Poisson register keeps the associated orientation. Adding coherences between
different `n` does not come from (1.1) and ceases to be the conditional channel
built by `Lambda*1=log`.

## 2. Exact decomposition

### Theorem 2.1 (fiber decomposition; PROVED)

For every state (1.2),

\[
 I(D:A\mid N)_\rho=\sum_nq_n I(D:A)_{\rho^{(n)}}.
\tag{2.1}
\]

If the fiber

\[
 D_n=\{d:d\mid n,\ \Lambda(d)>0\}
\]

has a single element, then its summand in (2.1) is zero for every choice
of `rho_(A|d,n)`. All its derivatives, including any Hessian with respect to
`F`, are also zero.

### Proof

The register `N` is classical and its blocks are orthogonal. The entropy
identities for a direct sum give

\[
 S(\bigoplus_nq_n\sigma_n)=H(q)+\sum_nq_nS(\sigma_n).
\]

Substituting this expression into

\[
 I(D:A\mid N)=S(DN)+S(AN)-S(N)-S(DAN),
\]

the four `H(q)` terms cancel, leaving (2.1). If `D_n` contains a single
value, `D` is deterministic conditional on `N=n`; hence `I(D:A)=0`,
regardless of the register `A`. The last statement follows by differentiating the
zero identity. QED.

## 3. The {2,3,4} chamber

The fibers are

\[
 D_2=\{2\},\qquad D_3=\{3\},\qquad D_4=\{2,4\},
\]

and on the last one

\[
 a_{2\mid4}=a_{4\mid4}=\tfrac12.
\]

By Theorem 2.1, the Petz Hessian sees only the dispersion between the two
paths `2|4` and `4|4`. In tangent coordinates `X_2,X_4` of the register `A`, its
quadratic part is a positive BKM metric applied to `X_2-X_4`; in the
commutative/Hilbert case it reduces, up to normalization, to

\[
 {1\over4}\|X_2-X_4\|^2.
\tag{3.1}
\]

The fibers `2` and `3` contribute exactly zero.

The physical form, by contrast, contains

\[
 -{2\Lambda(2)\over\sqrt2}\Re c_F(\log2)
 -{2\Lambda(3)\over\sqrt3}\Re c_F(\log3)
 -{2\Lambda(4)\over2}\Re c_F(\log4),
\tag{3.2}
\]

with all three coefficients nonzero. In particular, functions `F` can be
chosen for which `c_F(log 2)` or `c_F(log 3)` is nonzero. No form whose Hessian
vanishes identically on the fibers `2` and `3` can coincide with (3.2).

### Corollary 3.1 (mismatch before Gamma; PROVED)

There are no choices of the controlled states `rho_(A|d,n)`, of the
Poisson channel, nor of the BKM metric making

\[
 \operatorname{Hess} I(D:A\mid N)=Q_{N,L}
\]

within class (1.2). The contradiction already occurs at the prime
coefficients; adding Gamma and the poles in an independent tensor cannot create
the missing terms of `log 2` and `log 3`.

## 4. Why the repairs abandon the input

There are two formal repairs:

1. allowing coherences between different `n` blocks;
2. adding to the state a Gamma–prime coupling directly containing the
   terms (3.2).

The first is no longer produced by the conditional probability (1.1): it
requires phases and amplitudes between different integers that `Lambda*1=log` does
not specify. The second must choose exactly the mixed operator missing in
R161–R170. Its positivity or recoverability again becomes the open law, now
encoded in the reference state. Neither is a continuation of the canonical
Petz construction.

## 5. Phase result

The Petz equality is rigid, but it acts after decomposing by the
product `n`. That decomposition precisely kills the prime atoms, whose
divisor fibers are trivial. The route does not reach the physical operator and
hence does not reach the stage of using first-contact minimality.

The pattern is sharpened thus: the missing law cannot condition on the
recombined integer `n=dk`. It must simultaneously preserve interference
**between different integers** and **between divisor paths of the same
integer**, before any trace, entropy, norm, or recombination in `K_N`.
