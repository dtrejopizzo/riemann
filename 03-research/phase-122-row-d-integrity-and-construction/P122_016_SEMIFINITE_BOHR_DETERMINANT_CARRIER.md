# P122 -- the global Euler carrier is semifinite, not an ordinary determinant line

## Status

* `IMPORTED FRAMEWORK + PROVED APPLICATION`: crossed products, canonical
  semifinite trace and restricted determinant/index framework are standard;
  their finite-active-prime Bohr realization and exact Fourier criterion
  are checked here;
* `PROVED-IN-REPOSITORY`: the ordinary Hardy restrictedness obstruction in
  this physical representation;
* `CANDIDATE BUILDING BLOCK`: its metrized determinant/central-extension
  enhancement and coupling to Gamma--Tate.

This changes the type of the live D architecture.  A local prime tower has
an ordinary determinant line, but the physical continuous-time realization
has infinite transverse multiplicity.  The correct finite-place global
container is a semifinite determinant **density** over the Bohr phase flow.

## 1. Why the ordinary restricted group fails

Let `P_+` be the Hardy projection on `L^2(R_tau)`.  After Fourier transform
to the time variable it is multiplication by `1_[0,infinity)`.  For `a>0`,
multiplication by `exp(i a tau)` becomes the translation `U_a`.

### Theorem 1.1 -- one physical prime already has infinite multiplicity

The commutator `[P_+,U_a]` is not compact and hence is not Hilbert--Schmidt.

#### Proof

On the time side, `[P_+,U_a]` is, up to orientation, the partial isometry
carrying `L^2((-a,0))` onto `L^2((0,a))`.  Both spaces are
infinite-dimensional and every singular value on that subspace is one.
Therefore the commutator is not compact.  QED.

The same obstruction applies to any nonconstant periodic Euler scattering
factor.  More explicitly, use the Floquet decomposition

\[
 L^2(\mathbb R_t)
 \simeq L^2([0,a))\mathbin{\bar\otimes}\ell^2(\mathbb Z),
 \qquad t=x+ka.                                    \tag{1.1}
\]

Then

\[
 P_+=I_{L^2([0,a))}\otimes P_{\mathbb N_0},\qquad
 U_a=I_{L^2([0,a))}\otimes S_{\mathbb Z}.         \tag{1.2}
\]

Every nonzero discrete Hankel defect is tensored with the identity on
`L^2([0,a))`, so it has infinite ordinary multiplicity.

### Corollary 1.2

The finite-window scattering multiplier `K_T` of phase 120 does not lie in
the standard `GL_res` associated with the real-line Hardy polarization as
soon as one nonconstant prime factor is present.  Its global lift cannot be
an ordinary Pressley--Segal determinant line or an ordinary fermionic Fock
implementer on `L^2(R)`.

This does not contradict P122.013: that line lives on the discrete local
history `ell^2(N_0)`, before tensoring by the continuous cell coordinate.

## 2. The missing trace is trace per cell

Although the operator in (1.2) is not ordinarily Hilbert--Schmidt, it is
square-integrable for the natural semifinite trace

\[
 \tau_a(A)=\int_0^a\operatorname {Tr}_{\ell^2}(A(x))\,dx
                                                               \tag{2.1}
\]

on

\[
 \mathcal N_a=L^\infty([0,a))\mathbin{\bar\otimes}
                       B(\ell^2(\mathbb Z)).        \tag{2.2}
\]

Indeed, the boundary projection of one shift is
`I tensor |e_0><e_0|`, and

\[
 \boxed{\tau_a([P_+,U_a]^*[P_+,U_a])=a.}          \tag{2.3}
\]

For a prime, `a=log p`.  Thus the continuous multiplicity which destroys
the ordinary determinant is exactly the geometric length producing the
arithmetic coefficient.  Discarding it to recover an ordinary line would
discard `log p`; treating it with the semifinite trace retains it.

The rank-one curvature operator `C_r` of P122.013 similarly becomes the
measurable field `I tensor C_r`; for a history field `h(x)` its quadratic
density is

\[
 \int_0^a {1\over1-r^2}|\ell_r(h(x))|^2\,dx.       \tag{2.4}
\]

This is finite on the natural `L^2` module and remains orientation
sensitive.

## 3. Simultaneous primes: the canonical Bohr flow

Let `S` be a finite set of active primes and put

\[
 X_S=\mathbb T^S,\qquad
 \alpha_t((z_p)_{p\in S})=(e^{it\log p}z_p)_{p\in S}. \tag{3.1}
\]

Unique factorization implies rational independence:

\[
 \sum_{p\in S}n_p\log p=0, n_p\in\mathbb Z
 \quad\Longrightarrow\quad n_p=0\quad\forall p.  \tag{3.2}
\]

Hence the flow is ergodic, indeed uniquely ergodic, for Haar measure.  Its
smooth algebra carries the source derivation

\[
 \delta_S(z^n)=i\omega_nz^n,\qquad
 \omega_n=\sum_{p\in S}n_p\log p.                 \tag{3.3}
\]

Each prime grading and every cross-place phase are retained in one object.
No orthogonal direct sum over places has been taken.

Let

\[
 \mathcal M_S=L^\infty(X_S)\rtimes_{\alpha}\mathbb R             \tag{3.4}
\]

be the measured crossed product with its canonical semifinite trace,
normalized so that a spectral interval of the flow generator has trace
equal to its length.  In the regular covariant representation let `D` be
the flow generator and `P=1_[0,infinity)(D)`.

### Theorem 3.1 -- exact semifinite restrictedness criterion

For a trigonometric polynomial

\[
 f(z)=\sum_{n\in\mathbb Z^S}f_nz^n,               \tag{3.5}
\]

one has

\[
 \boxed{
 \tau_S\bigl([P,\pi(f)]^*[P,\pi(f)]\bigr)
 =\sum_{n\in\mathbb Z^S}|\omega_n|\,|f_n|^2.}     \tag{3.6}
\]

Consequently `[P,pi(f)]` is semifinite Hilbert--Schmidt precisely when the
right side is finite; (3.6) then extends by completion.

#### Proof

For one character `z^n`, covariance gives

\[
 D\pi(z^n)=\pi(z^n)(D+\omega_n).                  \tag{3.7}
\]

Thus its commutator with `P` is a partial isometry supported on the
spectral interval between `0` and `omega_n`, whose semifinite trace is
`|omega_n|`.  For two distinct characters, the cross term has nontrivial
Haar character `z^(m-n)` and its canonical conditional expectation is
zero.  Expanding the polynomial therefore gives (3.6).  Monotone
completion proves the last assertion.  QED.

For `S={p}` and the monomial `z_p`, (3.6) is exactly (2.3): its value is
`log p`.

## 4. The finite Euler scattering is semifinitely restricted

On `X_S`, define

\[
 c_p(z_p)={1-p^{-1/2}z_p^{-1}\over
                 1-p^{-1/2}z_p},\qquad
 c_S(z)=\prod_{p\in S}c_p(z_p)^{-1}.              \tag{4.1}
\]

Every factor is holomorphic on a fixed annulus around the unit circle, so
the Fourier coefficients of `c_S` decay exponentially.  Therefore

\[
 \sum_n|\omega_n||\widehat c_S(n)|^2<\infty,       \tag{4.2}
\]

and Theorem 3.1 proves that `pi(c_S)` belongs to the semifinite restricted
unitary group of `(M_S,P,tau_S)`.

Along the physical orbit `z_p=exp(i tau log p)`, its logarithmic flow
derivative is the exact finite Euler part of phase 120:

\[
 {1\over i}\delta_S\log c_S
 =\sum_{p\in S}(\log p)(1-P_p).                   \tag{4.3}
\]

Thus the Bohr carrier retains simultaneously:

* the exact prime-power coefficients;
* irrational cross-place phase;
* the source orientation;
* the canonical trace density producing `log p`;
* restriction maps `X_{S'} -> X_S` and Haar conditional expectations when
  `S subset S'`.

This is a global finite-Euler object defined before the Weil-form sign.

## 5. Why this is more than the direct-sum construction

The direct sum of local prime lines makes different places orthogonal by
definition.  In contrast, `C^infinity(X_S)` multiplies their characters
before tracing.  A multi-index `n` represents the actual rational
monomial `product p^(n_p)`, and its flow frequency is the physical logarithm
`log(product p^(n_p))`.  The central extension therefore sees mixed prime
products before Haar expectation.

Formula (3.6) diagonalizes only at the final canonical trace, by unique
factorization.  This is the pre-scalar cross-place information demanded by
P122.005 and absent from row C alone.

## 6. The archimedean obstruction is now isolated

The Gamma scattering

\[
 b_\infty(\tau)=\pi^{-i\tau}
 {\Gamma(1/4+i\tau/2)\over\Gamma(1/4-i\tau/2)}     \tag{6.1}
\]

is not almost periodic and does not belong to `C(X_S)`.  Its logarithmic
derivative grows like `log|tau|`, and the two Tate conditions remove only
the specified polar modes, not this failure of Bohr compactness.

Therefore the finite Euler construction cannot simply absorb (6.1).  A
global D needs an archimedean correspondence bimodule

\[
 \mathcal E_{\infty,S}:
   \text{Bohr semifinite Euler module}
   \longleftrightarrow
   \text{quarter-Gamma Calderon module},            \tag{6.2}
\]

together with a renormalized determinant anomaly.  The common causal
half-line and slit-disk filling of phase 120 provide a candidate underlying
module, but no determinant trivialization or anomaly theorem has been
proved.

## 7. Consequence for D

The finite-place carrier can now be stated without analogy:

\[
 D^{\rm Eul}_{T,\mathrm{sf}}
 =\bigl(\mathcal M_{S_T},\tau_{S_T},P,delta_{S_T},
         \pi(c_{S_T}),\text{Real port duality}\bigr).          \tag{7.1}
\]

It is source-defined, oriented, restriction-compatible, and has a genuine
semifinite determinant class.  It fails for Davenport--Heilbronn because
there is no Euler torus/scattering element; a shifted degree-two Euler
system changes the local Hankel rank rather than masquerading as (7.1).

What remains open is not the finite-place determinant carrier.  It is:

1. construct the bimodule (6.2), including both Tate conditions;
2. prove its local index/anomaly formula with the exact Gamma finite part;
3. prove that its first-contact equality section has zero oriented anomaly;
4. identify the resulting curvature with `B_nuc` only afterward.

The ordinary determinant-line target in P122.015 must therefore be read as
a semifinite determinant density plus an archimedean correspondence, not as
a `GL_res(L^2(R))` central extension.

The finite-section sign and normalization checks are reproducible with
`scripts/verify_p122_euler_determinant.py`.

## 8. Internal prior-art audit and nonduplication

This phase does not claim that semifiniteness itself is new to the
repository.  `106_152_POISSON_HOLONOMY_HEAT_LIFT_AND_COMPLETION_GATE.md`
already constructs, for each prime separately, a direct integral of
twisted-circle heat kernels over the Poisson holonomy measure.  Its
canonical semifinite trace recovers every damped winding and proves that
the winding-zero direct sum diverges.  D.194--D.195 also construct a
semifinite reduced-contact GNS algebra and its Poisson completely positive
dilation.

The first two constructions establish

```text
one prime -> positive heat/Poisson fiber -> semifinite local trace,
```

but their global operation is a prime-wise direct sum or contact GNS trace.

There is a further and more important predecessor:
`106_154_CAUCHY_DILATION_GLOBAL_POLARIZED_DESCENT.md` embeds all prime
modules into one stationary circular-Cauchy path space, proves joint
observability of the dense group `log Q_+^*`, and places all von Mangoldt
moments in one finite von Neumann algebra.  It already retains nonorthogonal
cross-prime information.  Therefore P122.016 must not claim to be the first
global finite-place carrier.

The narrower new content of Sections 1--4 is instead:

```text
all active primes in one torus
  -> irrational logarithmic flow
  -> one crossed-product semifinite trace
  -> exact H^(1/2) restrictedness formula (3.6)
  -> a determinant-class realization of the finite-Euler scattering.
```

Thus P122.016 gives a deterministic Bohr/crossed-product model and equips
the finite scattering with the missing determinant topology.  It is an
alternative realization of finite-place data already globally descended
in phase 106, not an upgrade of that descent theorem.  It does not solve
the old completion gate and may not reuse the open conversion (16) of phase
106 as if it had been proved.  The Cauchy-process, heat-semigroup and Bohr
determinant models all point to the same missing archimedean correspondence,
expressed in three coordinate systems.
