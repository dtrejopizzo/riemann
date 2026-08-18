# 106.00 — Self-adjoint perturbation determinants cannot be finite critical Euler products

## Result

The finite determinant bridge used in the Phase 64 global canonical-system
proposal is incompatible with self-adjointness.

Let \(A\) and \(A_0\) be self-adjoint operators for which the relative
perturbation determinant is defined on \(\mathbb C\setminus\mathbb R\), for
example when

\[
(A-z)^{-1}-(A_0-z)^{-1}
\]

is trace class. Then its determinant is holomorphic and nonzero on each open
half-plane. In contrast, for every prime \(p\), either choice of sign in

\[
L_p\!\left(\frac12+iz\right)^{\pm1}
=\left(1-p^{-1/2-iz}\right)^{\mp1}
\]

has prime-dependent zeros or poles at

\[
z_{p,k}=\frac{2\pi k}{\log p}+\frac{i}{2},
\qquad k\in\mathbb Z.
\]

Consequently an ordinary perturbation determinant of a positive/self-adjoint
finite canonical system cannot equal a nontrivial finite critical Euler
product times a zero-free normalization.

## 1. The self-adjoint zero-free theorem

### Theorem 1

Suppose \(A\) and \(A_0\) are self-adjoint and that a perturbation determinant
\(D_{A/A_0}\) is defined by

\[
\frac{D_{A/A_0}'(z)}{D_{A/A_0}(z)}
=\operatorname{Tr}\left((A-z)^{-1}-(A_0-z)^{-1}\right)
\tag{1}
\]

on \(\mathbb C\setminus\mathbb R\). Then \(D_{A/A_0}\) is holomorphic and
nonzero on \(\mathbb C_+\) and on \(\mathbb C_-\).

### Proof

For \(z\notin\mathbb R\), self-adjointness gives

\[
z\in\rho(A)\cap\rho(A_0).
\]

In the standard trace-class realization,

\[
D_{A/A_0}(z)
=\det\!\left((A-z)(A_0-z)^{-1}\right)
=\det\!\left(I+(A-A_0)(A_0-z)^{-1}\right).
\tag{2}
\]

The operator in the middle of (2) is invertible because both \(A-z\) and
\(A_0-z\) are invertible. The Fredholm determinant of an invertible operator
of the form \(I+\) trace class is nonzero. Holomorphy follows from the
resolvent identity and the analytic Fredholm theorem. The same conclusion
holds for determinant definitions obtained by integrating (1): its
logarithmic derivative is holomorphic off the real axis, and a zero or pole
there would create a pole in (1), which the resolvent traces do not possess.
\(\square\)

### Corollary 1

Multiplication by \(e^{a+bz}\), or by any holomorphic zero-free
renormalization, does not change the conclusion. Such a normalization cannot
create or cancel an off-real divisor.

## 2. The finite Euler divisor

### Lemma 2

For each prime \(p\), the function

\[
F_p(z)=1-p^{-1/2-iz}
\tag{3}
\]

vanishes precisely at

\[
z_{p,k}=\frac{2\pi k}{\log p}+\frac i2,
\qquad k\in\mathbb Z.
\tag{4}
\]

### Proof

Write \(z=x+iy\). Then

\[
p^{-1/2-iz}
=p^{-1/2+y}e^{-ix\log p}.
\]

It equals \(1\) exactly when \(y=1/2\) and
\(x\log p\in2\pi\mathbb Z\), which is (4). \(\square\)

The reciprocal \(F_p^{-1}\) has poles at the same points. Hence both signs
in a local determinant claim contradict Theorem 1.

## 3. No cancellation by a common archimedean normalization

Let \(P\) be a finite nonempty set of primes and let

\[
E_P(z)=G(z)\prod_{p\in P}F_p(z)^{\epsilon_p},
\qquad \epsilon_p\in\{-1,1\},
\tag{5}
\]

where \(G\) is holomorphic and zero-free in \(\mathbb C_+\). Choose a prime
\(p_0\in P\). Apart from accidental intersections, the lattice (4) depends
on \(\log p_0\) and is not the lattice of another prime. More strongly, if

\[
\frac{k}{\log p}=\frac{\ell}{\log q}
\]

for distinct primes and nonzero integers \(k,\ell\), then
\(p^\ell=q^k\), impossible by unique factorization. Thus every nonzero
lattice point of \(p_0\) survives in (5) unless the inverse factor for that
same prime is inserted and cancels the Euler contribution identically.

Therefore no prime-independent pole/Gamma factor and no zero-free
renormalization can repair the conflict.

## 4. Application to the Phase 64 claim

`CANONICAL-FOUNDATION.md`, Section 3, simultaneously asserts that

1. \(A_P,A_0\) are self-adjoint canonical operators;
2. \(D_P\) is their ordinary relative perturbation determinant; and
3. each prime contributes
   \((1-p^{-1/2-iz})^{\mp1}\).

Theorem 1 and Lemma 2 show that these three assertions cannot all hold.
The statement labelled “finite Tate identity” is therefore not a technical
gap: in the stated operator class it is false.

This does not refute Tate's local zeta integral. It refutes its identification
with the ordinary perturbation determinant of the claimed self-adjoint pair.
The local Tate factor naturally belongs to scattering or generalized
\(J\)-inner data, where off-real poles are allowed.

## 5. Why scattering does not immediately repair the RH route

A self-adjoint scattering system may have a meromorphic scattering
determinant with off-real resonances. Consequently a scattering determinant
can reproduce (3), but the self-adjointness of the underlying Hamiltonian
does not force its resonances onto the real axis. Identifying zeta zeros as
resonances therefore does not prove RH.

Alternatively, a Pontryagin-space realization can encode the off-real
divisor with its Krein--Langer index. In that setting, however, proving that
the negative index vanishes is exactly the unresolved RH statement.

Thus the finite bridge cannot be repaired merely by changing the word
“determinant.” A successful global construction must prove a new relation
which simultaneously:

1. is source-built from the complete Euler--Gamma system;
2. has a positive critical metric;
3. identifies the zeta divisor with genuine spectrum, not unrestricted
   resonances; and
4. retains linear multiplicity.

## 6. Falsification rule for subsequent constructions

Any later global-star proposal must answer the following before invoking a
limit:

> Where do the finite Euler lattices \(z_{p,k}=2\pi k/\log p+i/2\) live?

If they are eigenvalues of a self-adjoint operator, the proposal is false. If
they are scattering resonances, self-adjointness does not locate them. If
they are canceled, the construction must show how the complete arithmetic
divisor reappears at the global level without being inserted as input.

## Status

Proved: the incompatibility theorem above.

Refuted: the finite ordinary self-adjoint perturbation-determinant Euler
identity used as the starting bridge in Phase 64.

Open: a genuinely global positive-star construction not relying on that
finite identity. No RH conclusion is claimed.
