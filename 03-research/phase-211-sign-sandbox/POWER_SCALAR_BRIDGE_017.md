# POWER_SCALAR_BRIDGE_017 — Two scalar indices suffice for all blocks

Status: PROVED, independent formal review; final audit in POWER_INTERIOR_AUDIT_017. It does not yet prove the sign of the scalar family. Papers untouched.

## 1. Corpus and explicit difference

Consulted ROUTES-TRIED-INDEX, master grid, CROSSWORD-TO-D and POWER* searching for Bernstein, degree elevation, positive coefficients, partition and bridge. The recorded uses of Bernstein for completely monotone measures, bounds of entire functions and frequency limits are not this argument. POWER_DESCENT016 locates the pending binomial interior; CONFLUENT_BRIDGE014 proves sufficiency of all blocks, and JOINT_SCALE016 gives beta coordinates for its sectors. There is no renewed attempt to infer positivity of a linear envelope from a union of positive families.

The difference is a FINITE identity of rational densities with positive coefficients obtained by degree elevation, after an arbitrarily small perturbation. The identity also preserves the polar by rational evaluation off the spectral half-axis. The elementary polynomial lemma is standard; the contribution here is its exact application to the full form and the control of all crossings through that identity.

Local antecedents verified in the audit: `03-research/phase-114-closing-the-four-rows/114_d_180_BERNSTEIN_DIRECTED_ENDPOINT_GATE.md` §1 already uses positive degree elevation for stable integration in Bernstein coordinates; `03-research/phase-72-feshbach-leakage-calculus/E72_259_RATIONAL_BERNSTEIN_LM8_CERTIFICATE.md` certifies polynomial inequalities via Bernstein coefficients and exact subdivision. They are antecedents of the instrument, not of the present bridge: neither of those two documents turns a rational density into the cone of monomial atoms nor explicitly preserves the polar by evaluation at x=-1/4.

## 2. Sufficient and necessary statement on the confluent blocks

Fix u>1; one may take u=63/2. For N>=1,k>=0, let h_(N,k) be the real causal function with transform

    H_(N,k)(s)=s^k/(s+u)^(N+k).

The following are equivalent:

(A) W[h_(N,k)]>=0 for all N>=1,k>=0.
(B) W[f]>=0 for every F(s)=P(s)/(s+u)^M, M>=1, P real, degree P<M.

B implies A immediately. The proof that A implies B occupies §§3–5. By CONFLUENT_BRIDGE014, A suffices for the sign of all tests of the declared carrier and, through the already proved bridge, the target of Paper47. A is not presupposed: it remains OPEN.

Condition A uses only a monomial numerator and TWO indices. It has not been reduced to the single chain k0, nor to fixed N, nor to the eventually positive endpoints of015.

## 3. Every rational density is a nonnegative polynomial over a common weight

For F=P/(s+u)^M, set x=tau² and

    S(x)=P(i sqrt(x))P(-i sqrt(x)),
    q=x/(u²+x), F1(s)=1/(s+u).

S is a real polynomial of degree<=M−1, nonnegative for x>=0. The rational identity is

    |F(i tau)|²=|F1(i tau)|² R(q),
    R(q)=u^(2−2M)(1−q)^(M−1) S(u²q/(1−q)).           (R)

R is a real polynomial of degree<=M−1. It is nonnegative on [0,1): all factors of (R) are nonnegative there. By polynomial continuity it is also so at1. Its value at1 is zero if degreeP<M−1, and the square of the leading coefficient if degreeP=M−1. Neither strict positivity nor absence of interior roots is required.

## 4. Elementary degree-elevation lemma with explicit threshold

Let R(q)=sum_(l=0)^d r_l q^l and R>=0 on [0,1]. For epsilon>0, choose an integer D>=d. The EXACT expansion of R+epsilon in the Bernstein basis of degree D is

    R(q)+epsilon=sum_(j=0)^D b_(D,j) binom(D,j)q^j(1−q)^(D−j),
    b_(D,j)=epsilon+sum_(l=0)^d r_l (j)_l/(D)_l.      (BER)

Understand (j)_0/(D)_0=1 and (j)_l=0 for j<l. The formula is proved by counting marked subsets of size l in a binomial variable, or by expanding the identity of its factorial moment.

Uniformly in j,

    |(j)_l/(D)_l − (j/D)^l| <=l(l−1)/(2D).

Elementary proof: draw l uniform indices with replacement from a set of D, with j marked indices. The probability that all are marked is (j/D)^l. Conditioned on no index being repeated, it is (j)_l/(D)_l. The difference between both probabilities is at most the probability of some repetition, bounded by l(l−1)/(2D). For l0 and l1 the equality is exact.

Consequently, defining

    C_R=(1/2)sum_l |r_l|l(l−1),

one has b_(D,j)>=epsilon+R(j/D)−C_R/D. If D>=max(d,1) and D>C_R/epsilon, ALL coefficients are strictly positive. The procedure is effective for each R and epsilon. The approximating Bernstein polynomial is not confused with the EXACT representation by degree elevation.

## 5. Identity of the FULL form, including the polar

Define Q=s/(s+u), L=u/(s+u), and g_(D,j) by

    G_(D,j)=Q^j L^(D−j) F1
            =u^(D−j)s^j/(s+u)^(D+1).

It is a positive real multiple of the atom h_(D+1−j,j). On the spectral axis,

    |G_(D,j)|²=|F1|² q^j(1−q)^(D−j).

Multiplying (BER) by |F1|² and using (R) gives

    |F|²+epsilon|F1|²
      =sum_j b_(D,j)binom(D,j)|G_(D,j)|².            (DEN)

The archimedean part and that of each contact are linear in these densities, so they satisfy DEN. All arithmetic series converge absolutely for each of the rational functions of this finite identity; no degree limit is interchanged with an uncontrolled series.

For the polar, read DEN as a rational identity in x. At x=−1/4, the denominators do not vanish because u>1, and

    F(i sqrt(x))F(-i sqrt(x))=F(-1/2)F(1/2).

The identity is algebraic and does not depend on choosing a branch: each product is rational in x. Multiplying its evaluation by2 produces EXACTLY the identity of the polars. Although q=−1/(4u²−1) is negative there, the coefficients b_(D,j) remain the same positive numbers; no separate sign is attributed to the value of the polar.

One concludes the full identity

    W[f]+epsilon W[f1]
      =sum_j b_(D,j)binom(D,j) W[g_(D,j)].            (FORM)

FORM is an equality of quadratic values; the left-hand side is NOT W[f+sqrt(epsilon)f1]. No cross term was omitted: all the crossings of the numerator P are already in S and R.

Under A, each summand on the right is nonnegative. Hence W[f]>=−epsilon W[f1]. Letting epsilon->0 proves W[f]>=0. No uniform margin, function-approximation topology, nor strong convergence of g_(D,j) is needed.

## 6. Finite extraction of a negative atom, if a negative direction existed

The proof is also constructive by contraposition. If W[f]=−delta<0, choose epsilon>0 so that epsilon |W[f1]|<delta/2, and D>=max(d,1), D>C_R/epsilon. Then the left-hand side of FORM is negative. Since all coefficients are positive, at least one of the D+1 atoms h_(D+1−j,j) has negative W.

This does not construct a real counterexample: no initial negative direction of W is known. It specifies that any failure in a full matrix would have a monomial scalar witness at some finite order explicitly boundable from that failure. The representation allows treating the crossings without assuming that a union of positive subspaces is positive.

## 7. Exact relation with016 and pending obligation

There is no contradiction with the moment obstruction of016: here f is not approximated by a high-pass sequence. Its density is represented, with an arbitrarily small energy perturbation, through a positive cone of densities; the rational identity preserves the polar.

EVENTUAL015 does not suffice either. The triangle of FORM contains atoms with both indices variable, including the initial ones. The mass and energy that016 locates in the interior are not covered by tails of fixed dimension. The sufficient target is now explicit: prove the sign of the whole scalar table W[h_(N,k)] with the full arithmetic datum. Identities and tails alone still do not decide that table, as the falsifier W4 of016 shows.
