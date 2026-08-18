# D.26 — Collapse of the ordinary Hilbert Poisson quotient

## Statement

Meyer's closed-range theorem is a theorem in the nuclear Frechet spaces
used by the Poisson construction.  It cannot be transferred to the
ordinary Mellin-Plancherel Hilbert completion while retaining the resonant
quotient.  In that completion the relevant range is dense, and its Hilbert
quotient is zero.

This is the precise reason row C does not already supply the Hilbert
polarization required by row D.

## Abstract density lemma

Let `(X,mu)` be sigma finite.  Let `M_m` be multiplication by a measurable
function `m` on `L^2(X,mu)`, with maximal domain.  Then

```text
closure Ran(M_m) = L^2(X \ Z(m),mu).                (2.1)
```

In particular, if `m != 0` almost everywhere, `M_m` has dense range.

### Proof

The orthogonal complement of the range is the kernel of the adjoint.
The adjoint is multiplication by `conj(m)`, hence

```text
(closure Ran M_m)^perp
 = {g : conj(m)g=0 a.e.}
 = L^2(Z(m),mu).
```

Taking orthogonal complements proves (2.1).

## Application to the zeta multiplier

On the critical Mellin line, the Poisson/Zeta operator is represented,
up to the harmless normalization fixed in row C, by multiplication by a
meromorphic boundary value of zeta.  Its poles and zeros form a discrete
set on the line and therefore a null set for Lebesgue measure.  The density
lemma gives

```text
closure_L2 Ran(Z) = L2.                             (3.1)
```

The two defining conditions

```text
f(0)=0,                 Fourier(f)(0)=0             (3.2)
```

are continuous in the Schwartz/Frechet topology but are not continuous
functionals on unweighted `L2`.  Their joint kernel is therefore dense in
the `L2` completion.  More explicitly, point evaluation and integral can
be corrected by bumps of arbitrarily small `L2` norm; applying two such
independent corrections approximates any smooth compactly supported
function by functions satisfying (3.2).

Consequently

```text
closure_L2 Z(H_cap) = L2,                           (3.3)
```

and the Hilbert quotient

```text
L2 / closure_L2 Z(H_cap)
```

is zero.

## Compatibility with the Frechet result

There is no contradiction with Meyer's theorem.  The Frechet topology
controls all weighted derivatives and point evaluations.  In that
topology `Z(H_cap)` is closed and the quotient carries the transpose
resonance divisor.  Passing to `L2` forgets exactly the distributional
evaluation data that detect the discrete resonances.

Thus:

```text
nuclear closed quotient  !=  ordinary Hilbert closed quotient.
```

## Consequence for D

A faithful Hilbert realization of the resonant quotient must be a space
where the relevant evaluations are continuous.  It must therefore be a
reproducing-kernel or graph-norm completion, rather than the ordinary
absolutely continuous Mellin completion.

The next candidate is a source-defined reproducing-kernel completion of
the image of the Poisson transform.  Its audit has two non-negotiable
tests:

1. its kernel must be positive without assuming the location of the zeta
   zeros;
2. the normalized scale action must be uniformly bounded in the same
   kernel norm.

By D.25, satisfying both tests and retaining all resonant evaluation
classes would prove the global polarization and RH.  A kernel defined by
placing the zeros on the critical line, or by taking the positive part of
the nuclear character, is circular and is excluded.

