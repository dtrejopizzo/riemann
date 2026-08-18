# Phase 119 — what a finite compression certifies unconditionally

Opened 2026-08-17, after `phase-118-the-exact-threshold-inequality` closed.

## The pivot

Phase 118 verified, against real zeros of zeta, that for `F` primitive and
supported in `I_T`

    <A_T F,F> = sum_rho h(gamma_rho),      h(tau) = Fhat(tau)Fhat(-tau).

So `A_T >= 0` for all `T` is Weil positivity, which is *equivalent* to RH
(Weil 1952; Yoshida 1992; Bombieri 2000) — not a route to it. Chasing that
inequality is chasing RH itself with no extra arithmetic input, and phases
113–118 have now eliminated every internal reformulation that looked like it
might supply one.

**This phase stops asking whether the form is positive and asks a different
question:**

> The form restricted to a finite family of test functions is a computable
> matrix. Its *inertia* is constrained by where the zeros are (Sylvester's law).
> Its *moments* are computable unconditionally from the prime side. What does
> that combination certify?

The point is that this question has unconditional answers, whereas the previous
one has exactly one answer and it is RH.

## Why this program is unusually well placed to ask it

Four things already built and verified:

- the identity above, checked to 10 digits against actual zeros;
- an **exact filtration**: `E^*A_{tau_{j+1}}E = A_{tau_j}`, so the compressions
  at consecutive thresholds are nested with no error between them;
- a **balanced factorization** `A_T = X^*X - Y^*Y` with both halves explicit
  and PSD — a second, independent signature decomposition of the same matrix;
- a working **interval-certification pipeline** (Arb), with a reproduced
  certificate.

## The candid gate

Any argument built only from the functional equation, the explicit formula, and
mean values of Dirichlet polynomials applies verbatim to the Davenport–Heilbronn
function, whose RH-analogue is **false**. So no such argument can prove RH, and
this phase will not claim otherwise.

Rows (a)–(c) of paper 42 derive `Lambda(n)` as degrees of determinants of Witt
contact complexes — a constraint on the coefficients that is *not* on that list.
Whether that constraint separates zeta from Davenport–Heilbronn is the one
question in this phase whose answer could matter for RH, and it is scheduled
early rather than late. See `PLAN.md` §5c.

## Scope

Paper 42 is left as it stands. Nothing is written to it from this phase until
there is a result worth writing.

See [`PLAN.md`](PLAN.md).
