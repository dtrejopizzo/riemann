# E71.7 -- NO-GO / Phase 53 wall audit for CAND-1

**Date:** 2026-07-07.
**Role:** check the Phase 71 route against `NO-GO-LIST.md`, Phase 53 Stone import, and the Phase 60
CCM tribunal before pushing further.

## Sources audited

- `riemann-program/NO-GO-LIST.md`
- Phase 53:
  - `164-import-stone-onda.md`
  - `165-destructor-import-cuantico.md`
- Phase 60:
  - `tribunal-Connes.md`

## Main lesson from Phase 53

Phase 53 killed the generic quantum import:

```text
unitary flow + Stone => real spectrum => RH
```

because the Hilbert metric needed for Stone is not free. Either:

1. it is the Weil metric, whose positivity is RH;
2. the dilation generator has boundary/deficiency freedom, and the right extension encodes zeta;
3. Connes gives absorption, not emission; converting absorption to emission is Weil positivity.

This is the "inverted Stone" wall.

## Why CAND-1 is not the same move

Phase 71 must not claim:

```text
structural unitarity of the zeta flow proves RH.
```

That is dead by Phase 53.

The CAND-1 claim is different:

```text
for each finite cutoff, CCM constructs a self-adjoint finite operator H_{lambda,N};
if the associated finite real-rooted characteristic functions converge normally to Xi,
then Hurwitz transfers real-rootedness to Xi.
```

The finite self-adjointness is not used as a global Hilbert metric for the zeta flow. It is used only
to produce real-rooted approximants. The hard step is not Stone; it is convergence.

So the Phase 71 route avoids Phase 53 only under this discipline:

```text
do not prove unitarity;
prove normal-family convergence of real-rooted approximants.
```

## Wall map

### MW-1: Weil positivity

Avoided so far. E71.1-E71.6 do not try to prove `A-T_Lambda >= 0` or positivity of a Weil form.

Risk: any step that says "the limiting CCM form is positive" re-enters MW-1. Forbidden.

### MW-2: arithmetic propagation

Still the major risk. Proving

```text
Phi_{lambda,N} -> Xi
```

from a finite Euler product may require exactly the propagation of arithmetic information from
`Re(s)>1` to the critical strip. E71.3 already records that PNT alone is too weak.

Safe form: prove convergence from the exact CCM construction as an operator/normal-family theorem, not
from crude prime-counting.

### MW-4: Hilbert-Polya wrong sign

Avoided only if we do not ask for a global self-adjoint operator whose spectrum is already the zeta
zeros. The finite operators are real-rooted approximants; the limit is obtained by Hurwitz.

Risk: claiming existence of a limiting self-adjoint `H_zeta` with spectrum `{gamma_rho}` before proving
normal convergence. That would be Hilbert-Polya by assumption.

### MW-5: Connes-Consani arithmetic-site wall

Partially nearby. If the needed determinant normalization requires the unfinished arithmetic site or a
positive intersection theory, CAND-1 falls back into MW-5.

Safe form: the normalization must be built from the finite CCM matrices/rational functions themselves,
not from an external cohomology/polarization over `Spec Z`.

### MW-6: uniform spectral-gap wall

Riesz projection convergence needs uniform contour control. If the required lower bound is simply
"the limiting zeros stay separated and on the line", it is circular.

Safe form: use normal-family convergence on compact sets. Hurwitz then handles zeros without assuming
their location.

## Phase 60 tribunal warnings

The tribunal already identified the same viable skeleton:

```text
finite real-rootedness + convergence + Hurwitz => RH.
```

It also marked:

```text
E1 real-rootedness: depends on CCM finite self-adjointness / Thm 1.1(iii);
convergence: the entire burden;
renormalizations using epsilon_0>0: RH-circular.
```

Therefore Phase 71 must keep:

1. finite real-rootedness as a cited/implemented CCM input, not a generic rational-function lemma;
2. convergence as the only open theorem;
3. no normalization by positive ground energy `epsilon_0`;
4. no claim that raw zero locking proves function convergence.

## Audit verdict

Phase 71 remains a live CAND-1 route if and only if it proves the following theorem:

```text
There are finite real-rooted CCM characteristic functions D_{lambda,N},
canonically normalized from the finite CCM data,
such that D_{lambda,N} -> Xi locally uniformly.
```

Then Hurwitz closes `Omega_7`.

Everything else is either:

- a detector;
- a numerical symptom;
- or one of the old walls.

## Immediate next target

E71.6 showed that the raw entire numerator

```text
(2/sqrt(L)) sin(sL/2) sum xi_k/(s-d_k)
```

does not converge to `Xi` after scalar fitting.

The next object to test is the canonical product/determinant of the finite real spectrum:

```text
D_N(t) = product_{r in sp_+(H_{lambda,N})} (1 - t^2/r^2),
```

normalized by `D_N(0)=1`, compared to `Xi(t)/Xi(0)`.

This is still diagnostic, because a finite product over a truncated spectrum may need an exponential
genus factor. But it is closer to the Hurwitz theorem than the raw sine-comb numerator.
