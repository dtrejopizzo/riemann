# Phase 213 — New constructions for global positivity

Working memos in this folder are written in Spanish.

## Aim

Prove positivity of the full form of Paper 46 on its whole admissible carrier. This phase continues that
goal; it does not restart earlier attempts, nor does it turn the partial results of phases 211 and 212
into a global proof. The sign is treated as a problem about the explicit form, without reasoning from
equivalences with other targets (sandbox). Elementary mathematics is preferred; small computations are
used only for concrete checks, and a sample never proves all orders.

Definitions: `../phase-211-sign-sandbox/STATEMENT_001.md` and Paper 46. The specification and
restrictions of `../phase-212-missing-object/OBJECT_SPEC.md` and `../phase-212-missing-object/RULES_AVOID.md`
remain references, with the scopes and corrections recorded in the current master index. No paper is
modified without the global proof.

## Status

- **Global positivity of the full form: OPEN.**
- Each `ROUND_*` memo states its own claim, proof or precise defect, scope and label (PROVED,
  CONDITIONAL, OPEN, NO-GO with class, NUMERICAL, CITED or ARGUED). PROVED requires a complete proof and
  independent review. None of the rounds closes global positivity.
- Results 212-95-A/B (in `../phase-212-missing-object/ROUND_095_A.md`, `ROUND_095_B.md`) refute PSD of
  J_sc and every repair J_sc + cA with fixed c; they do not refute the full form nor supply the missing
  compensation. That repair is not retried here.
- The record of every attempt (antecedent, difference, result, what worked, what failed, reopening
  condition, file) is in `05-meta-and-planning/ROUTES-MASTER-INDEX.md`, Part V.

## Before any construction

Consult `../../05-meta-and-planning/ROUTES-MASTER-INDEX.md` (especially Parts VII, VI and V), Paper 48 and
the relevant primary sources. Failed paths are not repeated or renamed; a variant is considered only if it
introduces a distinct mathematical operation and explains why it does not reproduce the earlier
obstruction. Changing dimension, threshold, basis, parameters or representation is not enough.

Each candidate specifies, before derivations:

1. The closest antecedent, with file and section.
2. The concrete operation and mathematical claim that are different.
3. Which difficulty of the antecedent that difference avoids, and why.
4. The precise identity or inequality connecting the attempt with the full form and all its orders; for an
   auxiliary falsifier, which useful class of proposals it would decide.

An independent review checks this comparison before building. Absolute novelty is not promised.

## Contents

- `ROUND_nnn_A.md` (plus `ROUND_001_B.md` and `ROUND_012_B.md`) — rounds 001–416: comparison, statement, proof or
  precise defect, scope and next step (full list below).
- `SELECTION_nnn.md` — selection-gate records (candidates examined before construction).
- `AUDIT_370_PHASE.md` — Verification of the phase transfer in 370
- `SADDLE_FIXED_POWER_CALIBRATION.md` — Which abscissa a fixed cut at powers of log x requires
  round 390).
- `verify_*.py`, `verify_dyadic_gcd_subtotal.cpp`, `check_4944_blocks.py`, `probe_dilation_lp.py` — small
  verification scripts, each cited by the round with the same number or topic.

## Suggested reading order

1. This README and the Part V entries of the master index for phase 213.
2. `ROUND_001_A.md`, `ROUND_001_B.md`, then the `SELECTION_*` records.
3. Rounds in numerical order; the index below gives each title.

## Running the scripts

Python 3 with `numpy`, `scipy`, `mpmath` and `python-flint` (Arb); run from this folder, e.g.
`python3 verify_189.py`. The C++ check compiles with `g++ -O2 verify_dyadic_gcd_subtotal.cpp -o v && ./v`.
Outputs validate specific points of the corresponding memo; they are not proofs of the global sign.

## Full index of rounds and selection records

- `ROUND_001_A.md` — Scope of the even-sector inertia equivalence
- `ROUND_001_B.md` — Scope of the PRIME–ARCH inequality recovered from phase138
- `ROUND_006_A.md` — A negative upper tail in the physical cell matrix
- `ROUND_007_A.md` — Loss of the Poisson majorant under cell dilation
- `ROUND_010_A.md` — Combinations of nearby translations of a step profile
- `ROUND_011_A.md` — Two distant jump tubes prevent a uniform floor for free remainders
- `ROUND_012_A.md` — Control of the arithmetic crossing linked by the translation modulus
- `ROUND_012_B.md` — Energy limit for a fixed smooth mixture of translations of BUILD084
- `ROUND_013_A.md` — Uniform separation of head and tail for mixtures of bounded total variation
- `ROUND_014_A.md` — Two translations with arbitrary coefficients and a radius common to all k
- `ROUND_015_A.md` — All signed coefficients at the scale of the far cell
- `ROUND_016_A.md` — Signed translations over a growing number of cell widths
- `ROUND_017_A.md` — Absorption of the crossing by the two localized energies
- `ROUND_018_A.md` — Recovery of the full energy by two remote correctors
- `ROUND_020_A.md` — Head on two cells and arbitrary tail in a growing band
- `ROUND_021_A.md` — A single channel of possible negativity in a band of length proportional to K
- `ROUND_022_A.md` — Variance of the arithmetic crossing that the global sign would tolerate
- `ROUND_023_A.md` — Cost of taking absolute values between two bands
- `ROUND_024_A.md` — Norm of the crossing after cancelling within triples
- `ROUND_025_A.md` — Coercivity on a fraction of dimensions tending to one
- `ROUND_026_A.md` — Spectral count at the full cell cut
- `ROUND_028_A.md` — Transfer of a negative test to the other parity by translations
- `ROUND_029_A.md` — The plateau line as a global criterion
- `ROUND_030_A.md` — A fixed plateau profile would detect arbitrarily large widths
- `ROUND_031_A.md` — Polynomial threshold for a counterexample on cells
- `ROUND_032_A.md` — Uniform error when replacing only the prime tail by continuous density
- `ROUND_033_A.md` — Limit of the normalized defect in the full cell matrices
- `ROUND_034_A.md` — Boundary condition of a negative extremizer
- `ROUND_036_A.md` — Mellin zeros of a possible negative extremizer
- `ROUND_037_A.md` — A single compact test for all centres of the first filter
- `ROUND_038_A.md` — Trace norm of the tail and exact trace of the full arithmetic form
- `ROUND_039_A.md` — A one-sided arithmetic criterion at fourth powers
- `ROUND_041_A.md` — Optimal loss of a positive divisorial minorant at variable scale
- `ROUND_042_A.md` — An explicit minorant with a single sieve corrector
- `ROUND_043_A.md` — How much inclusion-exclusion the value of the original sieve requires
- `ROUND_044_A.md` — A local inequality on the primes equivalent to the criterion of 039
- `ROUND_045_A.md` — The cost of reproducing the band with a divisor sum
- `ROUND_046_A.md` — The deficit is localised in the first j−1 terms of the quadrature
- `ROUND_047_A.md` — A fixed weight with only O((log x)²) pending outer samples
- `ROUND_048_A.md` — The pending criterion as a finite alternating sum
- `ROUND_049_A.md` — Criterion with two factors of size close to the square root
- `ROUND_050_A.md` — Products with small squarefree part
- `ROUND_051_A.md` — Signed cancellation in rows whose prime repeats in the second factor
- `ROUND_052_A.md` — Cutting by the squarefree part, and a positive subsum after pairing
- `ROUND_053_A.md` — Where the positive term of 052 is compensated in the rows 3L<p<4L
- `ROUND_054_A.md` — Second difference of scales and elimination of all small rows
- `ROUND_055_A.md` — What the residue classes detect in the criterion of 054
- `ROUND_056_A.md` — An off-diagonal quadratic Möbius criterion
- `ROUND_057_A.md` — Cancellation of the diagonal by rational quotients in the form of 056
- `ROUND_058_A.md` — The cutoff by size of the quotients gives excesses of both signs
- `ROUND_059_A.md` — A centre that annihilates the main term in all quotients
- `ROUND_060_A.md` — Averaging fourth-power scales eliminates the squarefree condition in each slope
- `ROUND_061_A.md` — How far slopes can be removed by summing their absolute values
- `ROUND_062_A.md` — Signed compensation in the semiprime band of 061
- `ROUND_063_A.md` — A single average for the bands of every fixed logarithmic width
- `ROUND_064_A.md` — Semiprime band with superlogarithmic width
- `ROUND_065_A.md` — Sum over rows with the cutoff pq ≥ L
- `ROUND_066_A.md` — Two cutoffs of opposite sign for the semiprime total
- `ROUND_067_A.md` — The complete semiprime sector exceeds the root scale after any finite number of differences
- `ROUND_068_A.md` — One copy of each reduced product admits a lower bound at the root scale
- `ROUND_069_A.md` — Rows of reduced numerator up to powers below the square root
- `ROUND_070_A.md` — Which complete rows can be paid for according to their cofactor of large primes
- `ROUND_071_A.md` — At the critical boundary the rows of each sign exceed the root margin
- `ROUND_072_A.md` — Signed compensation between two complementary sectors of complete rows
- `ROUND_073_A.md` — The cost of all composite prime powers in a recurrence for the full criterion
- `ROUND_074_A.md` — A single sum over primes suffices, and its logarithmic scale is necessary in both directions
- `ROUND_075_A.md` — What is lost by cutting the prime sum of 074 before centering it
- `ROUND_076_A.md` — A single fixed block can contain the whole criterion; there is also detection in the interior
- `ROUND_077_A.md` — Regularity of minimizers and a power modulus for the full floor
- `ROUND_078_A.md` — Jensen at the reciprocal frequency: exact floor for the cell complement
- `ROUND_079_A.md` — Uniform bound on the cross block and explicit enclosure of the full minimum
- `ROUND_080_A.md` — Schur correction depending on the jumps of each vector
- `ROUND_081_A.md` — Unavoidable cost of separating the comb from the archimedean symbol on the complement
- `ROUND_082_A.md` — Energy needed for the exponential cost of the comb to survive
- `ROUND_083_A.md` — Positivity of the truncated exponential and width of the zero strip
- `ROUND_084_A.md` — Thirteen fast rates with the physical cutoff of any window
- `ROUND_085_A.md` — All dimensions and windows with a bounded sum of reciprocal rates
- `ROUND_086_A.md` — The sum of reciprocals is exactly the half-length of the limit window
- `ROUND_087_A.md` — A single list of poles: two-sided comparison with the effective window
- `ROUND_088_A.md` — Two orientations: exact threshold for switching on the reflected exponential
- `ROUND_090_A.md` — Simultaneous detection on a family of steps
- `ROUND_091_A.md` — The cosh with rate 1/2 detects an attained extreme on every grid
- `ROUND_093_A.md` — A prefix inequality without a continuous parameter
- `ROUND_094_A.md` — Only descending crossings can host a maximum violating the prime ceiling
- `ROUND_095_A.md` — Size of the excesses at the original crossings if there is an attained extreme
- `ROUND_097_A.md` — Maximal gain from allowing pairwise coprime composites
- `ROUND_100_A.md` — A conservative cut for scale-dependent splittings
- `ROUND_101_A.md` — Majorization only at prime samples with x-dependent splittings
- `ROUND_102_A.md` — How much of the cost of squares admits a divisibility certificate
- `ROUND_103_A.md` — The cubes decide the contact at the covering threshold for squares
- `ROUND_104_A.md` — The upper prime band above any fixed power less than one suffices
- `ROUND_105_A.md` — A ceiling without tolerance on a band of ratio four
- `ROUND_106_A.md` — No positive weight on a sufficiently narrow band admits the ceiling of its integral
- `ROUND_107_A.md` — A weight of ratio exp(0.88) with ceiling equal to its integral
- `ROUND_108_A.md` — Joint constraint of the harmonics of the first zero on the prime ceiling
- `ROUND_109_A.md` — A local inequality that only needs to be proved at prime centers
- `ROUND_110_A.md` — Only centers with local mass balance need a reciprocal bound
- `ROUND_111_A.md` — Prime ceiling certified on a continuous interval and comparison with the filter
- `ROUND_112_A.md` — Unconditional bound at all scales between 10¹⁰ and 10¹² for 109
- `ROUND_113_A.md` — The prime ceiling of 109 holds on the whole real interval from 2 to 10¹²
- `ROUND_114_A.md` — Absolutely controlled tail from the height of the fourth root
- `ROUND_115_A.md` — Detection in each power interval without a maximum of real parts
- `ROUND_116_A.md` — Long intervals of excess and sampling on a sequence of bands
- `ROUND_117_A.md` — Ceiling for the full minimum with possibly unbounded local mass
- `ROUND_118_A.md` — Exact law of the floor with a derivative penalty that may tend to zero
- `ROUND_119_A.md` — The exact rate on explicit matrices without penalty
- `ROUND_120_A.md` — How much data of the even matrix suffices in each window
- `ROUND_121_A.md` — Which arithmetic block keeps the rate of the full matrix
- `ROUND_122_A.md` — Detection with fixed maximal frequency for each lower exponent
- `ROUND_123_A.md` — Interpolation of the prime comb at the fourth-power nodes
- `ROUND_124_A.md` — What mass alone loses between two fourth powers
- `ROUND_125_A.md` — The masses of the true primes between fourth powers keep the rate
- `ROUND_126_A.md` — Unweighted Chebyshev oscillations at sparse nodes
- `ROUND_127_A.md` — Eventual sign of the signed mean of primorials at fourth powers
- `ROUND_129_A.md` — The centered factorial remainder descends below the root
- `ROUND_130_A.md` — Two-sided suppression of scales in the factorial remainder
- `ROUND_131_A.md` — A prime band around the cube root
- `ROUND_132_A.md` — A failure requires simultaneous excursions of θ and of Mertens
- `ROUND_133_A.md` — Exact exponent of the local Mertens oscillation in each power band
- `ROUND_134_A.md` — Bands chosen by a harmonic crossing of Möbius
- `ROUND_135_A.md` — The maximal oscillation has root scale in a typical shifted window
- `ROUND_136_A.md` — The anchoring with multiplicative signs and the sector of two real primes
- `ROUND_137_A.md` — A fixed multiplicative falsifier with arbitrarily small inversion defect
- `ROUND_138_A.md` — Transfer at the critical scale of the inversion defect
- `ROUND_139_A.md` — The Liouville boundary is linear in the root with uniform error
- `ROUND_140_A.md` — A positive Möbius weight computable with three Liouville sums
- `ROUND_141_A.md` — Two positive weights and a Möbius contribution of determined sign
- `ROUND_142_A.md` — Frequency of the crossings of the critical level
- `ROUND_143_A.md` — Frequency of the sign changes of the critical moment
- `ROUND_144_A.md` — A single sign criterion for a short Liouville average
- `ROUND_145_A.md` — A full Liouville average with unconditional sign and a variance frontier
- `ROUND_146_A.md` — A positive Liouville average with uniformly bounded variance
- `ROUND_147_A.md` — A complete detector with the same limiting density as the already signed average
- `ROUND_148_A.md` — A certified degree interval inside a criterion that detects all zeros
- `ROUND_149_A.md` — Which polynomial slopes can be certified after cancelling the verified ordinates
- `ROUND_150_A.md` — A fixed positive average that keeps the poles of the Liouville sum
- `ROUND_151_A.md` — Which part of the odd correction escapes the verified height
- `ROUND_152_A.md` — Drift of the squares in the odd correction
- `ROUND_153_A.md` — A density ceiling for integers whose squarefree part is prime
- `ROUND_154_A.md` — The logarithmic deficit of 153 is the exact mass of the perfect squares
- `ROUND_155_A.md` — How much is lost by averaging the complete count over divisors
- `ROUND_156_A.md` — Which exact statement a finite number of divisor moments can prove
- `ROUND_157_A.md` — Sign of the quadrature error for the inner divisor sum
- `ROUND_158_A.md` — Subtracting the elementary weight keeps the critical error per unit of tilt
- `ROUND_159_A.md` — A flat weight that beats the Gaussian prefix barrier and keeps detection
- `ROUND_160_A.md` — Removing the small prime powers with both their inner sums complete
- `ROUND_161_A.md` — Two contributions of determined sign in the band of 160
- `ROUND_162_A.md` — Which correlation of simple primes the band needs
- `ROUND_163_A.md` — The near block is positive even at logarithmic distance
- `ROUND_164_A.md` — How far the negativity of the distant block reaches
- `ROUND_165_A.md` — Measuring the threshold of the distant block at an individual scale
- `ROUND_166_A.md` — A criterion on a family of blocks of zero density in the logarithmic variable
- `ROUND_167_A.md` — Critical precision of the weights on the actual primes
- `ROUND_168_A.md` — How much exactness of the divisor identity the energy criterion requires
- `ROUND_169_A.md` — A sparse defect invisible on the real axis and in any finite list of moments at one
- `ROUND_170_A.md` — Minimal negative mass of a truncated certificate of paper 46
- `ROUND_171_A.md` — Radius of the certificate and displacement of a finite list
- `ROUND_172_A.md` — A signed extension for all zeros with summable weighted cost
- `ROUND_173_A.md` — Transferring the verified tail to a bound in L² norm
- `ROUND_174_A.md` — A finite verification threshold that suffices for strict positivity in each fixed window
- `ROUND_175_A.md` — Strict positivity of the full form up to T=6/5
- `ROUND_176_A.md` — Sufficient height law for growing windows
- `ROUND_177_A.md` — The height cost uses the norm of the compressed comb
- `ROUND_178_A.md` — Strict positivity of the full form up to T=21/10
- `ROUND_179_A.md` — Strict positivity up to T=5/2 via a direct Fourier leakage bound
- `ROUND_180_A.md` — A quartet above the height can cost (1+o(1))exp T
- `ROUND_181_A.md` — Sign of the true form at almost all modulations at the height of 180
- `ROUND_182_A.md` — Margin at two neighbouring modulations over the whole band of 181
- `ROUND_183_A.md` — Mass law required to saturate the comb in the critical band
- `ROUND_184_A.md` — Almost total alignment on a multiplicative interval of primes
- `ROUND_185_A.md` — How large a sample detecting misalignment over the whole band must be
- `ROUND_186_A.md` — Separation of the frequencies required by 184
- `ROUND_187_A.md` — Sufficient negativity test at a single frequency in the critical band
- `ROUND_188_A.md` — The linear error of test 187 is realized with both signs
- `ROUND_189_A.md` — Strict positivity of the full form up to T=129/50
- `ROUND_190_A.md` — Strict positivity up to 131/50 with a Chebyshev filter
- `ROUND_191_A.md` — Positivity of the full form up to T=67/25
- `ROUND_192_A.md` — Strict positivity up to T=68/25
- `ROUND_193_A.md` — Full form up to T=553/200 with a flat mask at the high end
- `ROUND_194_A.md` — From the strict window to power blocks of growing order and unequal rates
- `ROUND_195_A.md` — Corollary of 086–087 for the block without physical truncation
- `ROUND_196_A.md` — A pole that stays fixed leaves a tail in the limit problem
- `ROUND_197_A.md` — Exact cancellation at the critical tail rate and a common window for every rate
- `ROUND_198_A.md` — Short arbitrary window followed by three tails of arbitrary rates
- `ROUND_199_A.md` — Four tails on a common window, even under partial collisions
- `ROUND_200_A.md` — A block of arbitrary dimension with four free rates
- `ROUND_201_A.md` — Positivity for up to 32 arbitrary real poles over the whole admissible range
- `ROUND_202_A.md` — Quadratic sampling of the numerator: up to 4096 real poles without additional restrictions
- `ROUND_203_A.md` — Up to 72 000 poles and sufficient height quadratic in the order
- `ROUND_204_A.md` — Linear sufficient height and 500 million real poles
- `ROUND_205_A.md` — A complete cone in the scalar table and 10¹⁵ entire rows
- `ROUND_206_A.md` — To close the bridge, the eventual sign on each fixed dyadic ray would suffice
- `ROUND_207_A.md` — A single POWER diagonal with variable rate: exact detection interval
- `ROUND_208_A.md` — A centred, finite prime sum that preserves the growth of the diagonal
- `ROUND_209_A.md` — Profile of each verified zero in an uncentred finite sum over primes
- `ROUND_210_A.md` — A parameter-free quadratic prime average measures the maximal relative displacement
- `ROUND_211_A.md` — Distribution of the diagonal mass in criterion 210
- `ROUND_212_A.md` — Stability threshold of the prime cut at linear scale
- `ROUND_213_A.md` — Centring changes the stability of the critical cut
- `ROUND_214_A.md` — In which frequencies of the rate parameter a possible violation of the sign lives
- `ROUND_215_A.md` — A frequency band of width one detects the extreme angle without knowing it
- `ROUND_216_A.md` — Exact cost of separating the primes after the Mellin oscillation
- `ROUND_217_A.md` — A single sample per order, without exceptional orders
- `ROUND_218_A.md` — Forced cancellation between two already signed prime sums
- `ROUND_219_A.md` — What centring and separately controlling the endpoints of 218 demands
- `ROUND_220_A.md` — Unconditional balance and conditional frequency of sign excursions
- `ROUND_221_A.md` — Counting data up to x^(1/2+o(1)) allow samples to be programmed in a perturbation on the same primes
- `ROUND_222_A.md` — A stability scale for the prime sample
- `ROUND_223_A.md` — The stability constant of 222 is exact for perturbations on the primes
- `ROUND_224_A.md` — A change of order eliminates the instability of 221 for a family that still detects the whole sign
- `ROUND_225_A.md` — A model on logarithmic cells with integer data and subexponential error
- `ROUND_226_A.md` — Preserving exact moments of each cell does not suffice if their number grows without rate
- `ROUND_227_A.md` — What a subset of authentic primes with unaltered weights can contribute
- `ROUND_228_A.md` — An average of squares in the arithmetic variable measures the absolute horizontal displacement
- `ROUND_229_A.md` — Kernel-free diagnosis: the ordinary error on each power band
- `ROUND_230_A.md` — The quadratic mean on any interval of fixed ratio detects the complete displacement
- `ROUND_231_A.md` — Local detection with plain primes after fitting a line
- `ROUND_232_A.md` — Separating the cost of the gaps and an identity with weights only on primes
- `ROUND_233_A.md` — The average over modular directions satisfies the ceiling; parity obstructs transferring it to the original direction
- `ROUND_234_A.md` — Why small odd inverses do not work either and what a class-wise correction preserves
- `ROUND_235_A.md` — Only the first η log q modes of the original order detect the complete exponent
- `ROUND_236_A.md` — A single cosine as the interval varies, and a subsequence of false negatives
- `ROUND_237_A.md` — Windows of size X^(2/3) where the first component already passes the ceiling, unconditionally
- `ROUND_238_A.md` — Cancellation of increments lengthens the windows of small cost
- `ROUND_239_A.md` — One and the same smoothed count with growing fit at two near-linear scales
- `ROUND_240_A.md` — Transition law for the polynomial fit of a compact prime count
- `ROUND_241_A.md` — Discrete test with binomial weights and no continuous term
- `ROUND_242_A.md` — Scattered good samples in the block of two counts suffice
- `ROUND_243_A.md` — An exact node at the detecting scale and good blocks at extremes of the prime count
- `ROUND_244_A.md` — How many small nodes an extreme line with zeros would admit
- `ROUND_245_A.md` — Two increments of a positive average with data from earlier primes
- `ROUND_246_A.md` — The two readings have a sign and a main term on an interval of slopes
- `ROUND_247_A.md` — A barycentre of primes with linear weights and minimum at prime endpoints
- `ROUND_248_A.md` — The barycentre stays on the positive side up to 10^20
- `ROUND_249_A.md` — How much future the barycentre admits using only the primes already known
- `ROUND_250_A.md` — Blocks of length p^a that preserve the barycentre when primes are lost
- `ROUND_251_A.md` — Scattered deletions and the cost of inverting the barycentre
- `ROUND_252_A.md` — A regular zero-free product across the line that changes the barycentre
- `ROUND_253_A.md` — Simultaneous positivity of all logarithmic moments up to s=9·10^24
- `ROUND_254_A.md` — Exact frontier of all orders and size of the first negative order
- `ROUND_255_A.md` — A row of finite differences, with sign certified up to order 2^G
- `ROUND_256_A.md` — A budget of 1/3 for a finite sum of positive prime contributions
- `ROUND_257_A.md` — Positive budget using only primes between x and 2x
- `ROUND_258_A.md` — Optimal loss of the positive binomial carries in an octave
- `ROUND_259_A.md` — Binomial subtractions for the octave: construction and necessary cost
- `ROUND_260_A.md` — Which part of a binomial reaches the prime atoms of the octave
- `ROUND_261_A.md` — Exact integer binomials and the cost of their signed representation
- `ROUND_262_A.md` — Fit on prime powers: a scalar replaces the composite equations
- `ROUND_263_A.md` — Correcting one unit of mass at a cost tending to zero
- `ROUND_264_A.md` — Explicit correction with a gain of at least order log log N
- `ROUND_265_A.md` — The correction from proper powers of a binomial, even for decreasing splits
- `ROUND_266_A.md` — Differences of rows with a common endpoint
- `ROUND_267_A.md` — A single binomial top reproduces the octave and damps the small atoms
- `ROUND_268_A.md` — Necessary separation of the binomial endpoints in a fit of square-root cost
- `ROUND_269_A.md` — An explicit set of endpoints suffices for the whole calibrated representation
- `ROUND_270_A.md` — Optimal cost of universally compressing to a fixed number of endpoints
- `ROUND_271_A.md` — Chain repair: only primes above √N require interpolation
- `ROUND_272_A.md` — Unconditional calibrated fit on all moduli above the square-root cutoff
- `ROUND_273_A.md` — Calibrated interpolation on both sides of a band of moduli
- `ROUND_274_A.md` — A band of squared-logarithm ratio for the calibrated binomial fit
- `ROUND_275_A.md` — One weight for the one-sided sign in the octave and the signed residue of the band
- `ROUND_276_A.md` — At the primes of the band themselves the absolute error exceeds the square-root budget
- `ROUND_277_A.md` — The two signs of the band balance with a quantified relative error
- `ROUND_278_A.md` — The part with small divisors already satisfies the square-root bound
- `ROUND_279_A.md` — The exact exponent of the absolute mass in the band
- `ROUND_280_A.md` — A maximum over prefixed samples measures the exponent of the zeros
- `ROUND_281_A.md` — The diagonal of the samples, including both calibrations, already costs a square root
- `ROUND_282_A.md` — Pairs sharing a large divisor already meet the square-root bound
- `ROUND_283_A.md` — Along an unconditional subsequence the two infinite tails disappear
- `ROUND_284_A.md` — There is an auxiliary crossing in every interval of sufficiently large fixed ratio
- `ROUND_285_A.md` — A Möbius band of ratio tending to one suffices to detect an exterior zero
- `ROUND_286_A.md` — Proved favorable bands for μ and a multiplicative falsifier of the length jump
- `ROUND_287_A.md` — For ordinary Möbius increments it suffices to control one direction
- `ROUND_288_A.md` — One-sided majorant for the Möbius parity and its first failure
- `ROUND_289_A.md` — Widening the filter with local repair: logarithmic gain and semiprime barrier
- `ROUND_290_A.md` — Separation of nearby divisors by congruences and minimum rank cost
- `ROUND_291_A.md` — The principal character at fixed frequency oscillates too much; it can be removed from the full average
- `ROUND_292_A.md` — What hypothesis bounding a nonprincipal character would require, and how to eliminate the auxiliary condition
- `ROUND_293_A.md` — Which cofactors can be removed from the self-convolution at square-root cost
- `ROUND_294_A.md` — Sign of the block with a prime above the square root and cancellation with the complement
- `ROUND_295_A.md` — A cutoff near the square root balances the block without a large prime at square-root precision
- `ROUND_296_A.md` — Two monotone cutoffs and the number of primes separating them
- `ROUND_297_A.md` — How many frequency-independent cutoffs allow the block to be balanced
- `ROUND_298_A.md` — Sampling the balance at frequencies where the smooth block is exactly zero
- `ROUND_299_A.md` — An explicit frequency and the first order that detects each zero
- `ROUND_300_A.md` — Positive inversion by dilations for the odd discrepancy of the first row
- `ROUND_301_A.md` — Positive families larger than the square root after summing all their square parts
- `ROUND_302_A.md` — Sign of the full block with a large prime as the frequency approaches zero
- `ROUND_303_A.md` — A macroscopic cutoff leaves the large-prime block bounded by a constant
- `ROUND_304_A.md` — The first row admits balanced cutoffs with arbitrarily large cofactors
- `ROUND_305_A.md` — Barrier for the balanced cutoff above the square root
- `ROUND_306_A.md` — The sign at fixed logarithmic cutoffs detects any exterior zero
- `ROUND_307_A.md` — The endpoint k=4 fails unconditionally, with oscillation larger than the main term
- `ROUND_308_A.md` — Effective crossings beyond the fourth power by a doubly logarithmic factor
- `ROUND_309_A.md` — A positive average of the full balance keeps the square-root ceiling after sieving the divisors
- `ROUND_310_A.md` — A positive sieve isolates the main scale up to any subpolynomial threshold
- `ROUND_311_A.md` — Simultaneous trimming of the large and small arguments in the sieved average
- `ROUND_312_A.md` — Negative sign of the sieved average on decreasing relative intervals
- `ROUND_313_A.md` — Negative sign with a growing gap and positive weights outside the gap
- `ROUND_314_A.md` — Simultaneous sign on the full space of divisor coefficients
- `ROUND_315_A.md` — Unavoidable cost of the two orientations of the balance for the whole divisor matrix
- `ROUND_316_A.md` — Three dilations cancel the range of arguments up to a fixed power
- `ROUND_317_A.md` — Cut at the root by two successive order-one convolutions
- `ROUND_318_A.md` — Cut at X^(2/3) with mean-square error sufficient for the global sign
- `ROUND_319_A.md` — Reduction to indices below an arbitrary power with local observation
- `ROUND_320_A.md` — Polylogarithmic band with recombinable positive local averages
- `ROUND_321_A.md` — The short operator is small in frequency mean, but admits no uniform contraction
- `ROUND_322_A.md` — Uniform contraction of the observed multiplier in an explicit strip
- `ROUND_323_A.md` — Contraction in rectangles of verified height via explicit Taylor weights
- `ROUND_324_A.md` — Localization up to the critical line without assuming simple zeros
- `ROUND_325_A.md` — An energy of nearby pairs measures exactly the extreme abscissa of the zeros
- `ROUND_326_A.md` — When the proximity of the pairs pays the budget by itself
- `ROUND_327_A.md` — Relative cancellation proved in the band of pairs that still demands exponential cancellation
- `ROUND_328_A.md` — The diagonal dominates even when widening the critical window
- `ROUND_329_A.md` — Saving of every power in the central Möbius energy
- `ROUND_330_A.md` — A multiplicative countermodel preserves the signs and all polynomial savings
- `ROUND_331_A.md` — Truncation by common divisor in the energy of nearby pairs
- `ROUND_332_A.md` — The class of primitive quotients already carries the whole absolute rate
- `ROUND_333_A.md` — Simultaneous cancellation in the classes of exact greatest common divisor
- `ROUND_334_A.md` — Separating by greatest common divisor preserves the rate that detects the zeros
- `ROUND_335_A.md` — Threshold of the weights on the common divisor
- `ROUND_336_A.md` — The exact off-diagonal cost, even with weight equal to the gcd
- `ROUND_337_A.md` — Detection of the abscissa by a local mean without the Taylor weights
- `ROUND_338_A.md` — Two copies of the same Möbius block in the local mean
- `ROUND_339_A.md` — A shared logarithmic phase survives the square of the block
- `ROUND_340_A.md` — A single isolated subblock with the true signs already demands RH
- `ROUND_341_A.md` — Pointwise bound for all reduced quotients of small height in 338
- `ROUND_342_A.md` — A second dilation cancels the density of each quotient separately
- `ROUND_343_A.md` — The residue of large quotients in an isolated rectangle still detects RH
- `ROUND_344_A.md` — Which terms compensate the isolated rectangle
- `ROUND_345_A.md` — What balance the first rows surviving the inversion have
- `ROUND_346_A.md` — Compensation between bands in two families of odd products
- `ROUND_347_A.md` — Pairing between distinct odd products in the full observable
- `ROUND_348_A.md` — Disjoint pairing of mass comparable to the whole window
- `ROUND_349_A.md` — A single pairing leaves a sparse residue and preserves coverage at each center
- `ROUND_350_A.md` — Almost total coverage at all centers using two moments
- `ROUND_351_A.md` — Residues of prescribed prime support and a cross criterion without diagonal
- `ROUND_352_A.md` — Counter-test for decorrelation based only on the carriers
- `ROUND_353_A.md` — The higher prime powers consume at most half of the critical norm
- `ROUND_354_A.md` — Two sectors of simple primes compensate in their signed mean
- `ROUND_355_A.md` — Compensation of the sectors of 354 at each center
- `ROUND_356_A.md` — Smooth-divisor threshold for removing terms at root cost
- `ROUND_357_A.md` — It suffices to estimate cofactors without small primes, with a single prescribed cut
- `ROUND_358_A.md` — Reconstruction without depth losses for growing sieves
- `ROUND_359_A.md` — Criterion with the whole product free of small primes
- `ROUND_360_A.md` — A single linear average at fixed width for the sieved products
- `ROUND_361_A.md` — How the cut amplifies the forced oscillation of the triangular window
- `ROUND_362_A.md` — Frequency tail below the root with the moving cut
- `ROUND_363_A.md` — Gaussian window and truncation at the root of log x
- `ROUND_364_A.md` — Which zero region a diffusive Gaussian with moving sieve detects
- `ROUND_365_A.md` — A single moving cut and a single inequality for the diffusive Gaussian
- `ROUND_366_A.md` — The positive bias of the sieved product and a sign criterion without barrier
- `ROUND_367_A.md` — Positivity criterion with a fixed Gaussian for the full sieved product
- `ROUND_368_A.md` — A single comparison of parities, with cut and width fixed by x
- `ROUND_369_A.md` — Unconditional odd dominance in a growing range of layers
- `ROUND_370_A.md` — Unconditional saddle up to cuts exp(C(log log x)²)
- `ROUND_371_A.md` — The scale reaching the Vinogradov–Korobov region
- `ROUND_372_A.md` — Exponents of the two excursions at the exact moving cut
- `ROUND_373_A.md` — Width of the parity exceptions on the logarithmic scale
- `ROUND_374_A.md` — Cost of the high-multiplicity layers at the exact cut
- `ROUND_375_A.md` — The growing prefix of layers has negative sign at the exact cut
- `ROUND_376_A.md` — Logarithmic marking of the layer: growth up to (1−ε)log log x
- `ROUND_377_A.md` — The intermediate block has positive excess and compensates the prefix
- `ROUND_378_A.md` — One large layer at every scale and the limit of multiplicity moments
- `ROUND_379_A.md` — Sign of the whole sector with a single prime above a second scale
- `ROUND_380_A.md` — Balance of the sector with exactly two large primes
- `ROUND_381_A.md` — Balance of all sectors of fixed order and obstruction to truncation
- `ROUND_382_A.md` — Uniform comparison of sectors on both sides of the maximum of the main profile
- `ROUND_383_A.md` — The real zero of the parity weight near one
- `ROUND_384_A.md` — Sign inversion of the sector with a single macroscopic prime
- `ROUND_385_A.md` — Quantified transition and cut that neutralizes the one-prime sector
- `ROUND_386_A.md` — Neutralizing the union of all large primes: reduction to a finite product
- `ROUND_387_A.md` — The jump at the neutral cut is positive and smaller than the square root
- `ROUND_388_A.md` — Unavoidable cost of taking absolute values on a vertical of the neutralized product
- `ROUND_389_A.md` — A horizontal band that no simple contour of absolute values can go around
- `ROUND_390_A.md` — Two crossings in the order of the primes and the distance between them
- `ROUND_391_A.md` — Second crossing of the union and a finite cut below the square root
- `ROUND_392_A.md` — Arbitrarily distant crossings and representation with primes x^o(1)
- `ROUND_393_A.md` — What prime size would suffice and what size is unavoidable
- `ROUND_394_A.md` — At the endpoint four mass is still missing
- `ROUND_395_A.md` — Exact threshold of absolute mass to second order
- `ROUND_396_A.md` — Effective cancellation among the multiplicity classes near 4z
- `ROUND_397_A.md` — The two dominant frequencies of the majorant at the positive saddle
- `ROUND_398_A.md` — Two conjugate saddles and conditional sufficiency of the mass threshold
- `ROUND_399_A.md` — Inversion of the terminal prime size at individual scales
- `ROUND_400_A.md` — An explicit unconditional ceiling for the terminal prime
- `ROUND_401_A.md` — The phase of the deterministic cut when moving the scale: both signs in each block
- `ROUND_402_A.md` — Search window in number of primes around a computable amplitude
- `ROUND_403_A.md` — Unconditional separation of the negative term and of the poles at growing height
- `ROUND_404_A.md` — One part of the sum of residues already satisfies an exponential saving
- `ROUND_405_A.md` — How much the Euler product loses at the verified and higher heights
- `ROUND_406_A.md` — A positive average suppresses all residues in an explicit window
- `ROUND_407_A.md` — Removing a critical pair from the average while keeping positive weights
- `ROUND_408_A.md` — Iteration of the narrowing with sufficiently high critical zeros
- `ROUND_409_A.md` — The first critical zero can be removed before narrowing again
- `ROUND_410_A.md` — What exactly the variance measures after removing the critical pairs
- `ROUND_411_A.md` — Counterexample: removing all critical pairs in order with positive kernels
- `ROUND_412_A.md` — Integrated comparison on the real axis that recovers the unweighted sum of displacements
- `ROUND_413_A.md` — D(R) already tends to zero without RH and the strong limit has a rectangular formula
- `ROUND_414_A.md` — Eliminating the unknown normalization without losing the sign of each zero
- `ROUND_415_A.md` — What the derivatives of the integrated deficit detect
- `ROUND_416_A.md` — The second dyadic difference already changes sign if there is an exterior zero
- `SELECTION_002.md` — Selection: powers and falling factorials
- `SELECTION_003.md` — Selection: theta grouping by sums of two squares
- `SELECTION_004.md` — Prime dilations of the jump profile
- `SELECTION_005.md` — Two jump profiles with scales 2 and 3
- `SELECTION_008.md` — Reflection of the cells at zero
- `SELECTION_009.md` — Eliminating the composite jump of maximal index
- `SELECTION_019.md` — Remote crossing after cancelling the polar term
- `SELECTION_027.md` — Selection of averages of growing width
- `SELECTION_035.md` — Direct transfer of certificates by mixing changes of scale
- `SELECTION_040.md` — Divisorial minorization of the weight of 039
- `SELECTION_089.md` — Uniform sampling of the odd parity of 088
- `SELECTION_092.md` — Limit of the prime reading of cosh
- `SELECTION_096.md` — Equal mass, equal gap and opposite signs without primality
- `SELECTION_098.md` — Local cost of majorizing the prime weight via positive counts of multiples
- `SELECTION_099.md` — A fixed binomial splitting does not reproduce the logarithmic weight with positive dilations
- `SELECTION_128.md` — Required resolution of a factorial majorant of the prime mean

## Other files in this folder

- `ROW*` series (6 further files, `ROW_D_COMPILED_REFERENCES.json.gz` … `ROW_D_PROOF_DEPENDENCIES.md`).
- `verify*` series (30 further scripts, `verify_039_interval.py` … `verify_spline_nodes_5.py`).
- `CHEBYSHEV_TRIVIAL_CHARACTER_MELLIN.md` — Fractional weight of the trivial character.
