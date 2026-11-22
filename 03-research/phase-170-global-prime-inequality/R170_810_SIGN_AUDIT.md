# R170_810 — Audit of the sign attempt with preserved reserve

This note covers both the construction and the audit. The two independent attempts of this round failed due to
usage limits; they delivered neither a construction nor an independent
verification.

## Mathematical verdict

Inequality (4) of R170_809 is valid under the definitions given there.
It does not prove W≥0 for every T. The attempt does not complete the
global goal. Paper 46 is not modified to claim a nonexistent closure.

The following points were checked:

- The reserve on functions with zero average on each cell is
  log M+γ_E−1/2, combining l₀ and r before minimizing.
- The negative polar term costs at most 2sinh(L/2)−L in the coercivity
  bound, since ||s_L||²=sinh(L/2)−L/2.
- The form domains are preserved under P and Q; B has a bounded
  inverse once its gap g_M>0 is proved.
- PV=I and bV=P D⁻¹ annihilate the mixed term of b, not that of W.
- The remaining coupling is exactly −QK_LV; changing that sign does
  not alter the quadratic debit, but does change the minimizing
  response.
- Completing the square preserves the summed sources before squaring
  them and leaves an explicit positive remainder.

## Exact proof of the loss at contact

Consider the real two-dimensional model

    b=diag(1,3),   K=[[1/2,1],[1,1]],
    W=b−K=[[1/2,−1],[−1,2]].

Take P on the first coordinate. Then Vx=(x,0), C=1/2,
A=1 and B=2. W is positive semidefinite and W(1,1/2)=0. A correct but
non-exact bound B≥gI with g=1 gives

    C−A²/B=0,            C−A²/g=−1/2.

This shows that a valid positive gap of the complement is not enough to
certify the sign at the contact. This example does not belong to the
Paper 46 prime data and does not refute them; it refutes the purely
operator-theoretic inference that the reserve and its coercivity alone
force the sign.

Even strict positivity of the complement and zero coupling can allow a
negative remaining block: b=diag(1,3), K=diag(2,0) gives W=diag(−1,3).
An additional arithmetic property is needed to exclude this in the real
operator. That property has not been proved here.

## Reproducible checks

`python3 verify_retained_reserve.py` compares two computations of the
Schur complement: the original one, by direct elimination of W, and the
one obtained using the harmonic extension of b. Three complex matrices
defined with fixed seeds gave differences smaller than 1.7e−14. The
identity of the square with its remainder gave errors smaller than
5.7e−14. The contact example is also verified with exact fractions,
obtaining 0 and −1/2.

These are algebraic diagnostics; they do not certify the continuous
complement nor extend the certified interval of Paper 46.

## Contrast with the corpus map

R170_809 avoids the error of discarding R_S detected in R170_808.
However:

1. Choosing M for each L is a per-scale construction, not the missing
   uniform law. No novelty is attributed to the existence of finite
   reductions.
2. Preserving Λ in A and C is not equivalent to using an identity of
   the integers to prove a sign. The arithmetic requirement was not
   resolved.
3. Replacing B⁻¹ by g_M⁻¹I introduces precisely the loss (6). It was
   not proved compatible with the critical margin; the example shows
   why it cannot be assumed.
4. The corrected v2 version of R169_000 still stands: γ_q cannot be
   treated as a frequency determined by the window, nor the primes of
   the short tail as free data independent of it.

**Final result of this round:** an inequality with retained reserve was
constructed and checked. The global sign inequality was not
constructed, nor was a new arithmetic law implying it. The closure of
Paper 46 remains open.
