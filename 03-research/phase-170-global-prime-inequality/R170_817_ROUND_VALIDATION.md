# R170_817 — Validation of the construction round

Constructions carried out in two independent attempts:
`green_sign_construction` (R170_815) and `divisor_sign_construction`
(R170_816). This audit reviewed and requested corrections; no proofs
are attributed to the attempts that they did not deliver.

## Validation result

**The requested proof was not completed.** Neither attempt proved the
two bounds of R170_814. The identities and elementary estimates listed
below are accepted, not the global sign nor a refutation of the
conjecture for the real operator.

| Result | Verdict |
|---|---|
| Interior quotient equal to −E_ρ and E_ρ≥0 | Correct; a consequence of the radical equation and the primitive construction. |
| Identification of that quotient with Φ | Not proved. The interior and nonlocal tests are different. |
| Vanishing of <JH_{M,N}F,S_LF> by support | Correct; already in R170_812, not counted as new progress. |
| Two-sided bound of the tail H_{M,N}UF | Correct, but elementary and without the required sign. |
| Mass of the absolute bound ≥(log2)/(2√2)√N | Correct, using only d=2 and N/2<m≤N. |
| Oriented decomposition of the d=2 channel, R170_816 (14) | Correct by the composition rules for translations and reflection. |
| Contradiction with an arithmetic first contact | Not obtained. |

## Corrections required during the audit

1. R170_815 introduced P_Tz without justifying that the indicator
   preserved Q_log for that test. That step was removed: e(z) is used
   directly, whose definition is already valid, and the weak equation
   only on admissible interior tests. It is not claimed that the
   multiplier property is false, only that it was neither proved nor
   necessary.
2. The three-dimensional model of R170_815 does not contain a
   continuous family of windows nor the specific contraction G_ρ. Its
   scope was restricted to refuting an inference from the semidefinite
   compression, its radical, and an interior competitor. It does not
   refute a specific law of the zeta first contact.
3. The norm bound of R170_816 is no longer called a new arithmetic
   estimate. An explicit lower bound of its mass was added to make the
   loss precise, instead of merely stating it could be large.
4. The negative-correlation examples do not satisfy the contact
   hypotheses. The conclusions that intended to transfer them to that
   radical without justification were corrected.

## Check of the second arithmetic attempt

For the divisor 2, −L_M*E_N produces a reflected family and a Fourier
family, while −H_{M,N}UF adds a second Fourier family. Their shifts are,
respectively,

    −log(2m) on JF,
     log(m/2) on UF,
     log(2m) on UF, with m>N/2 in this last one.

The first family vanishes when log(2m)≥2T. The other two carry the
same exterior sign in the expression and do not cancel term by term;
formally equating their shifts changes indices, weights, and ranges.
That does not rule out a deeper cancellation with other parts of PC. It
does prevent attributing the sought sign to this separation alone.

The growing mass of the absolute bound is not a lower bound of the real
flux. The correlations may cancel. Hence it does not prove an
impossibility of every strategy that preserves those correlations
either.

## State of the work

The repaired constructions of R170_813–814 remain well defined. The
exterior–interior comparison and the domination by the Gamma reserve
remain conjectural obligations. This round does not provide a uniform
arithmetic law nor extend the certified range of Paper 47. Validation
does not turn two failed attempts into a proof.
