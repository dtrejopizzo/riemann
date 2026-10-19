# C127.004 — closing the exhaustion gap to Weil's criterion

Status: `PROVED`. Full statement: Paper 45 §10, Thm. 10.4.

## The gap

"`q_T ≥ 0` on primitive tests for every `T` ⟹ RH" is asserted throughout the
corpus as classical (phase 118 closure, paper 42 `eq:Dcircularity`, THE_BACKWARD_MAP)
but is **proved nowhere in it**:

- `113_07` Prop. 4.1's (⇐) leg is flagged by its own scope ledger as resting on
  an unproved Paley–Wiener interpolation in `D° = {\hat f(0)=\hat f(1)=0}`;
- `106_11` Thm. 1 does prove, unconditionally and in **both parities**, that a
  failure of RH produces fixed nonzero compactly supported negative Weil tests —
  but for **unconstrained** `C_c^∞`, and it is never upgraded to the two-moment
  primitive class.

So the chain `A+B+C → D → RH` was, at this joint, an assertion.

## The closure

The primitivization operator is `Π = −∂_t² + 1/4`.  It multiplies the entire
function by `s(1−s)`:

    Φ_{ΠG}(s) = (1/4 − (s−1/2)²)·Φ_G(s) = s(1−s)·Φ_G(s),

so `Φ_{ΠG}(0) = Φ_{ΠG}(1) = 0` — both Tate moments die.  On the Fourier side it
is multiplication by `τ² + 1/4`, a **positive even real** polynomial: compact
support, reality and parity are preserved, the exponential type is unchanged
(Paley–Wiener), and `ρ(1−ρ) ≠ 0` at every nontrivial zero, so prescribing values
of `Φ_{ΠG}` at target zeros is equivalent to prescribing them for `Φ_G`.

Running `106_11`'s construction on the primitivized targets therefore produces
nonzero compactly supported **primitive** tests of both parities with `q < 0`
whenever RH fails.  The tail estimate acquires `|ρ(1−ρ)|² = O((1+|Im ρ|)^4)`,
absorbed by enlarging `N` since `Φ^N` decays faster than any polynomial.

Why the gap survived: it sat on the seam.  The identity `q(F) = Σ_ρ Φ_F(ρ)Φ_F(1−ρ)`
on the primitive class is row C (Paper 45 (9.7)); the negative-test construction
is `106_11`.  Neither alone suffices.
