# D.30 — Kummer audit and the semilocal uniform gate

## 1. Purpose

This note distinguishes a failed route from an impossibility result.  Row D
is not known to be impossible.  What has been proved is that the constructions
already audited do not supply the required primitive sign independently.

## 2. The exact sign

On the primitive test space

```text
P = {F : integral exp(t/2)F(t) dt = integral exp(-t/2)F(t) dt = 0},
```

rows A--C give the exact identity

```text
B_nuc(F,F) = ||S F||^2 - ||B F||^2.                 (2.1)
```

Thus the force-bearing assertion is the contraction

```text
||S F|| <= ||B F||,       F in P,                   (2.2)
```

together with the equality theorem.  The B--C comparison then identifies
(2.2) with Weil positivity.  Consequently (2.2) may not be used as an axiom,
as a definition of the metric, or as a consequence of a completion whose
positivity is itself verified from the zero divisor.

## 3. Kummer audit

The Kummer 1-motive

```text
M_p = [Z -> G_m],       1 |-> p
```

does solve a source problem: `log p` is an actual regulator period before
nuclear realization.  Poincare biextensions and height splittings construct
pairings for a 1-motive and its dual.  They do not, by their existence alone,
give a negative definite form on the completed primitive restricted product.
Polarizability of the graded pieces of a mixed realization also does not imply
definiteness on extension data.

Therefore the proposed Kummer--Rosati statement of D.29 is not presently a
theorem obtained from the standard 1-motive formalism.  Using it without a new
proof would merely rename the missing sign in (2.2).

This does not discard Kummer motives.  They remain a natural integral source
for the local classes and may enter a later comparison theorem.  What is
discarded is the claim that existing biextension theory automatically closes D.

## 4. New pivot: semilocal exhaustion

Let `Q>1`, let

```text
S_Q = {infinity} union {p prime : p < Q},
```

and restrict to primitive test functions supported in the multiplicative
window `[Q^(-1/2),Q^(1/2)]`.  Construct the finite-place source and boundary
operators `S_Q` and `B_Q` directly from the local Tate--Gamma objects of A--C.
The target theorem is

```text
||S_Q F|| <= ||B_Q F||                              (4.1)
```

with all of the following properties proved independently of the zeros:

1. the same two primitive moment conditions as in (2.2);
2. a contraction constant exactly one, not `1+epsilon_Q`;
3. compatibility under `Q<Q'`;
4. no loss at primes crossing the boundary of the support window;
5. equality only for the principal/null class;
6. convergence of the quadratic forms to (2.1) on every compact support.

If (4.1) is proved for every `Q`, property 6 gives (2.2) without exchanging two
separately divergent norm limits.  This is stronger and better typed than the
failed critical Szego limit: each statement is finite/semilocal, while the
limit is taken only after forming the renormalized quadratic form.

## 5. Candid status of the pivot

The semilocal inequality is not proved in this note.  It is the next research
gate.  Existing operator-theoretic literature presents the sufficiency of the
corresponding semilocal framework as a conjectural route, not as a theorem.
Accordingly it must be established here from the finite local objects before it
can close D.

The live task is now concrete: derive a finite Gram/kernel formula for
`||B_QF||^2-||S_QF||^2`, find an intrinsic sum-of-squares or Hodge realization,
and prove uniform compatibility in `Q`.
