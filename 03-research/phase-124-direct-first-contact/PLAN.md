# Phase 124 — first attack on the arithmetic exclusion of first contact

Objective: investigate the direct route with fewer
dependencies. It does not require finishing A, creating another geometric
theory, or editing the papers.

## 1. Operational target

Start from a hypothetical first contact T_* > log 2 and a nonzero primitive
state F of definite parity. We have q_(T_*) >= 0 and the radical
variational equation on the primitive domain. We must show that
this situation is incompatible with the arithmetic data.

On the R/S route, the pending obligations are:

1. **Cancel the Tate source.** The existing incoming current satisfies
   L_(T,-)^gr(F) = -Z_(T,+) r_eta, where
   r_eta(t) = c(exp(t/2) + eta exp(-t/2)), eta = +/-1.
   Critical transmission forces c=0 by P122.019/P122.029. We must
   prove transmission, or directly c=0, from the state's arithmetic
   equation.
2. **Exclude the homogeneous state.** After c=0, prove the relation
   between channels needed to apply first-cell rigidity.
   The candidate is (E_(p,T)-E_(q,T)) h_F = 0 for two distinct active
   primes, with the domains and conditions of P122.020.

The known energy

```
E_eff(F) = ||(E_(q,T)-E_(p,T)) h_F||^2 / log(q/p)
```

does not need to be recomputed. A harmonic extension has constant flux,
which can be nonzero. The new proof must control the flux.

## 2. First candidate: joint variation of the Gamma–Euler source

Use the literal system of phase 120, keeping together the prime-delay
states, the Gamma oscillator states, and the coherent degree
profile. Do not independently vary states that are already determined
by F.

The first computation will look for a boundary identity obtained by varying
the source F and propagating that variation to all states through their
equations. The variations will be corrected to maintain the two
primitive conditions. The sign of q at first contact allows using
its radical equation; it does not allow assuming the sign of separate
boundary terms.

Concrete order:

1. Write the operators that transport the variation of F to each
   state and the degree term. Work initially on a regular kernel with
   interior support and declare its relation to the minimizer's closed
   domain.
2. Carry out the variation of the full SIGNED action. Keep the boundary
   terms from the truncated translations, from Gamma, and from the Tate
   corrections; eliminate none of them by analogy with a local operator.
3. Prove the passage to the first-contact state. If F is regularized,
   estimate the equation's residual and the convergence in the topology
   needed for the boundary term. Do not assume H^(1/2) in this step.
4. Determine whether the identity contains an additional relation that
   forces c=0 or zero flux. Point out the exact arithmetic property that
   produces it. If it only recovers the radical equation or an equivalent
   factorization, it does not count as closing an obligation.

This is a research candidate, not an already proved identity.
It is not enough that the action be stationary: a stationary point of a
signed action does not thereby have all its terms positive or null.

## 3. Results of the first attempt and decision

| Result | Next action |
|---|---|
| c=0 is obtained with a valid proof on the minimizer's domain | Keep that proof and focus the next task on the homogeneous state; do not keep seeking unnecessary stronger regularity. |
| A law is obtained forcing the gluing under c=0 | Keep it and attack exclusively the Tate cancellation. |
| F is excluded directly without R/S | Use that proof; R/S are not added as extra obligations. |
| Only the radical equation or the known detector is reproduced | Briefly record where the information disappears; do not multiply new versions of the same candidate. |
| There is a concrete domain obstruction or a counterexample | Delimit the refuted class and design a modification that changes that hypothesis. Do not declare the whole route impossible. |

A result valid only for two primes is a test of the candidate, not an
exclusion for all windows. The subsequent proof must include all
active channels, both parity sectors, and the relevant birth
thresholds.

## 4. Alternative within the same phase

If the variation does not produce a new law, attack the signed inequality
directly on the complete system. The identity

```
q_T(F) = ||X_T F||^2 - ||Y_T F||^2
```

allows formulating a domination bound. The advance would have to be an
arithmetic estimate that proves it, with sufficient constant and full
domain. Constructing an operator whose contractivity is equivalent to
the bound does not prove it.

That a goal has RH-strength is not a veto. The distinction is between
proving the inequality from the data and assuming it in another notation.
Consult the existing no-gos only to check their exact hypotheses.

## 5. Route closure

The closure chain will be:

```
certified base + first contact reached
  + new arithmetic law proved
  -> exclusion of a first sign loss
  -> q_T >= 0 for all finite windows
  -> sufficient domain of the Weil criterion
  -> RH.
```

The last step requires using the normalizations, density, and continuity of
the corresponding criterion; it does not require constructing a geometric
intersection of A. A uniform positive margin in T is not needed if the
sign is proved in each window and the resulting test class is already
sufficient.

## 6. Work discipline

- Do not repeat the log 2 certificate, the phase 121 detectors, the
  two-prime energy, or the identification of the critical boundary space.
- Do not deduce transmission from subcritical regularity or from a
  computation that imposes the transmission condition itself.
- Do not discard an analytic proof because it works on minimizers;
  do require an independent proof of every consequence used.
- Do not confuse a global signed identity with a sign theorem.
- Keep at most one main candidate and one alternative.
- Keep only the proofs, obstructions, and computations that change
  an obligation. Do not modify papers or turn every step into an
  extensive memo.

Pending first deliverable: the joint variation and its boundary
identity, with justified domain and a verdict on its capacity to
cancel the Tate source or the flux. Neither of those cancellations is
proved by opening this phase.

## 7. Selected continuation

After P124.013--014 the Gate R obligation is stated without a minimizer:

```
Sigma(T) = B_T - X_T^* L_T^{-1} X_T >= 0   for every window T < T_q,
```

with `X_T` the column of the necklace `rho_{\pm,T}` (P124.005) and `B_T` the
Tate block of the full Weil form (P124.013 (2.3)).  It is a `2x2`
inequality on explicit objects, in the range where `L_T > 0`.

The falsifier `Xi_a` violates it before its first contact, and `zeta` did not violate
it in the explored range.  The separation between the two is the unimodularity of the
local roots (`p^{-1/2}` versus `p^{-1/2\pm a}`).  Hence the only admissible
main candidate remains a local unitarity law, now with the obligation to
produce Gate R (via `Sigma`) and Gate S **simultaneously**; the split
"R soft, S arithmetic" is closed.
