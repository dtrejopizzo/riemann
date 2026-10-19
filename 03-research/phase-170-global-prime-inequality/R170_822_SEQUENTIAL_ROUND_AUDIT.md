# R170_822 — Audit of steps 1 → 2 → 3

Three independent attempts sequentially built
R170_819, R170_820, and R170_821. This audit validated the formulas and
required the following corrections. A sign proof was not completed.

## Step 1: algebraic connection, not a sign comparison

The polarizations (4)–(5), the identity with remainder (8), and the
scale transport (9e) of R170_819 are validated. With δ=G_ρF−F and
z=S_N U S_LF,

    Φ+E_ρ=Re e_G(z)+h⁻¹ Re a_M(δ,δ−hz).

The first part is a general polarization identity. The specific
information lies in the expansion of e_G: the original residue over
D_ρ*z, the defect m(D/ρ)−m(D), the translation differences, the Tate
shift, and the primitivity correctors. Their sum has not been bounded
with the required sign.

A wrong interpretation was corrected: scaling log d to log d/ρ does NOT
destroy the multiplication of divisors. The scaled translations still
compose via dm. What must be compared is the complete transport of the
operators, not a supposed loss of factorization.

## Step 2: exact joint comparison

The conjugation O^(ρ)=D_ρ*OD_ρ takes X to ρX, the translations to
τ_{a/ρ}, and U to U_ρ. The conjugated PC and the subtraction (7) of
R170_820 were validated by expanding products. The hyperbola
coefficients are the same, and the interior cancellation Λ*1=log is
preserved.

It was required that the tests and the Tate vector be explicitly fixed
when comparing the scalars. Conjugating all the data keeps the same
scalar; keeping the data fixed leaves the remainders as written. The
two cases cannot be combined to eliminate a remainder without paying
its contribution.

The local equation was also corrected: e_F(v)=a(F,v)−<r,v> annihilates
every admissible test supported on the window, not only the primitive
ones. The vanishing of a(F,v) without the Tate port does require
primitivity. This does not annihilate the nonlocal tests appearing in
the comparison.

Step 2 did not obtain a new one-sided inequality. It should not be
described as a completed sign piece.

## Step 3: what uniformity is actually proved

For distinct shifts, the Fourier multiplier of their difference has
essential supremum 2. Hence

    ||τ_{a/ρ}−τ_a||=2

on L² and on Q_log when a≠0 and ρ≠1. By contrast,

    ||m(D/ρ)−m(D)||≤C_m|logρ|≤(8/7)C_m h,
    C_m=sup_x |x m'(x)|<∞.

Both proofs are valid. The first does not allow claiming that EVERY sum
of translations has that norm: there may be cancellations. Nor does a
proof of strong continuity of D_ρ by itself prove absence of norm
continuity for any conjugated expression, in particular U_ρ.
Corrections were requested to avoid such extrapolations.

On each fixed finite radical, strong convergence and local boundedness
give uniformity on its sphere. This does not automatically control the
family of radicals as T, N, M, and L vary. Moreover, a small two-sided
bound does not impose a sign at a contact with zero margin.

## Final decision

The three attempts carried out the three tasks in order. Explicit
identities and rigorous uniformity restrictions were obtained, but not
the inequality needed to complete step 2. For that reason step 3 can
only deliver partial estimates of the remainders: there is no new
proved sign inequality to transport to every scale.

Neither the certified range is extended nor is D proved. The R170_818
map becomes more precise: the remainders are identified; their sign
correlations remain uncontrolled. Completing each attempt's tasks
should not be confused with completing the map's mathematical pieces.
