# AUDIT_005 — Premise of the diagonal/same-prime round

2026-10-18. Initial and final review of CONSTRUCTOR_005. No parallel candidates were built. Full target D active; no auxiliary completes it.

**Final verdict: PROVED the canonical SPD completion of −R_α on c_00 of distinct divisors d≥2 for 0<α<1/2; PROVED its inheritance under finite deletions on surviving indices. Link with Q_T OPEN.**

## 1. Corpus check and admissible reason

Reread: README index (families Gram, SOS, phase193 frontK, INV_C/D/V, R183_006–008 and entries209), 06_OPEN_RESIDUES (R1, R7–R9), P1_BBSTAR and the 209 memos. Targeted reading of R183_006_GCD_FIBER_LAURENT_BRIDGE, including its initial correction; grid/crossword and index queries for diagonal, regularisation, renormalisation, Laplacian and dominance.

Proximities that must not be confused with the new computation:

- **R183_006–008:** a positive Gram pole does NOT give positivity of its finite part. The documented correction uncovers a residue of infinite rank. Here the object is different, but the invalid inference would be the same.
- **Phase193 frontK / CA_K_001:** signed Laplacian and Cheeger already examined. Do not present the choice of diagonal as a new mechanism.
- **P1_BBSTAR / thm:sos:** Gram, root and closure by sum of squares are indexed. Classifying as a certificate does not prove impossibility; nor does constructing a generic norm identify the node.
- **INV_C / forms on ratios:** obtaining a pair form does not automatically construct an identity with the window form.

**New reason admitted by this round:** compute the exact finite part of the SAME object B_y of CONSTRUCTOR_002–004, on the diagonal and same prime, keeping the subtraction scheme already fixed; compare it with the coprime cross terms whose signed ordinary Mellin has just been proved. The diagonal is not reassigned to make a favourable matrix. Neither Sonin nor the Laplacian of the Weil matrix is retried. This is a new question internal to the specific candidate, not a reason to reopen closed families.

## 2. What the coprime sign actually tells

**PROVED, elementary algebra.** Knowing the cross entries −w<0 does not determine the diagonals. In dimension two,

    [[a,−w],[−w,b]]≥0  iff  a≥0, b≥0, ab≥w².

The same w appears in positive, indefinite or negative matrices depending on a,b. Hence A_α(d,e)>0 for coprimes neither identifies a diagonal value nor its sign, nor gives gamma domination. The positive-inverse structure of ANTICORRELATION003 was for the NORMALISED covariance or its positive Mellin, not for an unknown renormalised denormalised matrix.

Assigning to each diagonal the sum of incident weights would produce a generic PSD Laplacian. There is still no proof that this diagonal coincides with the archimedean/polar part of the node. If used as a control, label it as an algebraic identity, not as an achieved link.

## 3. Finite part: fixed orientation and scheme

The object already fixed for 0<α<1/2 is

    R_α(d,e)=∫_0^∞ y^(α−1)[B_y(d,e)−y^(−1/2)G₀(d,e)]dy,
    G₀=(gcd(d,e)−1)/(de).

For coprimes, R_α=−A_α<0. For diagonal or same prime G₀>0 and the subtraction is indispensable. PSD cannot be transferred from ∫B at α>1/2 to R at α<1/2: a kernel has been subtracted and the explicit term G₀/(α−1/2) has negative sign. The canonical scheme of CONSTRUCTOR002 must be kept.

Changing a cutoff function in the subtraction changes a finite part by an explicit multiple of G₀. If it is modified, that change must be computed and kept; not chosen to favour the sign. The required uniqueness comes from fixing the original Mellin continuation, not from a verbal choice of "natural renormalisation".

The general algebraic asymptotics, already verified in AUDIT004, is

    B_y=y^(−1/2)G₀−[(d−1)(e−1)/(de)]/(1−√y)+exponential error.

The regularised constant term is negative for ALL d,e≥2; this only describes small y, it does not prove the sign of its integral at all scales.

## 4. Powers of the same prime and global sum

Before summing all powers of p, justify expansion, sum of the counterterm and integrable error. The formal sum of the local G₀ is

    Σ_{j,k≥1}(p^min(j,k)−1)/p^(j+k)=p/(p−1)².

It is verified via the geometric divisibility probabilities 1/p^j and the identity v_p=Σ_j1_{p^j|N}; or by two geometric series. It is a positive coefficient. This does not justify without domination interchanging the sum of finite parts.

When summing primes with weights log²p, the global coefficient Σ_p(log p)²p/(p−1)² diverges. Do not carry the regularisation of each prime to a finite global sum without additional treatment. This is a concrete interchange/limit problem, not a NO-GO for the candidate.

## 5. Eulerian mixture and link

The total covariance identity at σ>1 has explicit diagonal p^(−σ)/(1−p^(−σ))² and two PSD forms. Its scalar expression can be continued by formulas; the PROBABILITY identity does not survive at σ=1/2. Do not deduce PSD of the continued forms from that scalar diagonal staying positive.

For any link with Q_T, one must define a map of all tests of the declared domain, keep quadratic degree in F, list archimedean/polar terms and prove the identity or domination without assigning signs by analogy. The difference between divisor indices and Mellin heights is still pending. A result on R_α will be an auxiliary positive or negative according to its proof, not a closure of D.

## 6. Initial verdict

Admissible round with the new reason of §1. There is no legitimate inference from the off-diagonal sign already obtained to the sign of the diagonal or to the node. The concrete opportunity is to COMPUTE the canonical diagonal/same-prime part and its interaction with the cross terms, before proposing favourable structures. Final review pending CONSTRUCTOR_005.

## 7. Verification of the comparison of shells of one prime

Premise stated in CONSTRUCTOR_005, independently verified; review of the final memo pending.

Let p be fixed and s_j(y)=τ(p^(2j)y)−τ(p^(2j+2)y), j≥0. It is the unnormalised Gaussian mass of v_p(|N|)=j. The reference is g_j(y)=c(1−1/p)p^(−j), c=y^(−1/2). Poisson with z=p^(2j)y gives

    s_j=c_z(1−1/p)+c_z[τ(1/z)−p^(−1)τ(1/(p²z))].

Punctured concavity implies q_u(p)=τ(p²u)/τ(u)<1/p for u>0 (quotient strictly decreasing from its limit 1/p). With u=1/(p²z), the bracket is negative. Thus 0<s_j<g_j for all j,y.

For a bounded observable f(j) and positive finite masses w_j,

    V_w(f)=min_{z∈ℂ}Σ_j w_j|f(j)−z|².

Therefore, with m_g its reference mean,

    V_s(f)≤Σ_j s_j|f(j)−m_g|²
          <Σ_j g_j|f(j)−m_g|²=V_g(f)

if f is not constant. The direction of the comparison of minima is correct; it is not inferred by inverting a lower bound. Strictness follows from g_j−s_j>0 for ALL j and some value f(j) different from m_g.

For f(j)=Σ_{k≤j}a_k with a nonzero finite vector a on k≥1, f is bounded and non-constant because f(0)=0. The two sides are exactly B_y[a] and cG₀[a] on the block of powers of p. This proves D_y=cG₀−B_y strictly positive on each finite block of a single prime. Its integral against y^(α−1), 0<α<1/2, converges by the expansions already fixed and is positive definite: −R_α is SPD on each finite block of the same prime. **PROVED.** It does not determine the global sign across several primes.

## 8. Independent control: the global pointwise comparison is false

**PROVED for a precise class: D_y=cG₀−B_y over all divisibility indicators is not PSD for each fixed scale y>0.** This does NOT rule out positivity of the integrated kernel −R_α: integration may compensate scales and passing to the limit of the following family under Mellin has not been justified.

Let L_P be the product of all primes ≤P and f_P(n)=1_{gcd(|n|,L_P)=1}. By inclusion-exclusion,

    f_P(n)=Σ_{d|L_P}μ(d)1_{d|n}.

The term d=1 is constant, so the same variance observable is realised with finite coefficients a_d=μ(d), d|L_P,d>1. The form G₀ on that vector is the variance of f_P under the uniform measure on residues modulo L_P:

    G₀[a]=δ_P(1−δ_P), δ_P=φ(L_P)/L_P=Π_{p≤P}(1−1/p)→0.

The convergence δ_P→0 follows, for example, from harmonic divergence: δ_P^(−1) is the partial Euler product and dominates Σ_{n≤P}1/n.

For each n≠0, f_P(n)→1_{|n|=1}. Domination by 1 gives convergence of means and variances under the fixed punctured Gaussian. Consequently,

    B_y[a]→τ(y)Var_y(1_{|N|=1})>0,
    cG₀[a]→0.

It follows that D_y[a]<0 for P sufficiently large. This result coexists with: individual entries D_y(d,e)>0; SPD blocks of ONE prime; and possible positivity of the global Mellin, still undecided. It prevents using the single-prime shell principle as a joint mass comparison without checking what fails in the shells of several primes.

Record the falsifier only with that pointwise scope. Do not turn it into a NO-GO for O1 nor for the canonical integrated diagonal.

## 9. Integrated global completion: independent verification

Proof stated in CONSTRUCTOR_005 and verified; final memo pending. **The pointwise counterexample of §8 does NOT prevent this integrated completion.**

For finite support of coefficients a_d, d≥2, let A(n)=Σ_da_d1_{d|n}. The divisibilities of the support generate a FINITE partition into cylinders of truncated valuations. Let P_t be the probability on that partition making the valuations of each involved prime independent, with tails P_t(v_p≥j)=p^(−tj), t>0. It is a probability for ANY t>0 because it only involves finitely many primes; it is not a normalisable global zeta law when t≤1.

Write μ₁=E_{P₁}A=Σ_da_d/d and define the finite signed measure on that partition

    ν_y=cP₁−τ(y)P_y, c=y^(−1/2).

Each cylinder is represented by finite inclusion-exclusion among events d|N. For each basic event,

    ∫_0^∞y^(α−1)[c/d−τ(d²y)]dy=κ_α d^(−2α),
    κ_α=−Z_α=−2π^(−α)Γ(α)ζ(2α)>0,
    0<α<1/2.

The integral converges and the change of scale proves the exact factor d^(−2α). Positivity of κ also follows directly from c−τ(y)>0 and the same integral for d=1. Inclusion-exclusion gives

    ∫ y^(α−1)ν_y(cell)dy=κ_α P_{2α}(cell).

No infinite probabilities are integrated nor are all primes summed. Positivity arises after integrating ν_y, which may have negative parts at each scale.

The exact algebraic identity is

    D_y[A]=cVar_{P₁}(A)−τ(y)Var_y(A)
           =ν_y(|A−μ₁|²)+τ(y)|E_yA−μ₁|².

Integrating,

    −R_α[A]=κ_α E_{P_{2α}}|A−μ₁|²
          +∫_0^∞ y^(α−1)τ(y)|E_yA−μ₁|²dy ≥0.

All steps are legitimate: the first function is constant on finitely many cells; the rest converges by E_yA−μ₁=O(√y) at zero and decay of τ at infinity. If a is not zero and the d≥2 are distinct, A is not constant (N=1 and successive evaluation at the ordered indices). P_{2α} assigns positive mass to all cells, so the first term is strictly positive. **−R_α is positive definite on every nonzero finite vector of indicators d≥2, not only on blocks of one prime.**

This proves a canonical completion of the diagonal in the already fixed OBJECT R, without assigning it by hand. It does not prove identity with Q_T, does not prove boundedness/realisation in PW_T nor close D. It is a global auxiliary positive on its declared finite domain.

## 10. Specificity: the completion is inherited under finite deletion

**Verified as an essential filter, not as a barrier to all links.** For a finite set S of removed primes, define

    τ_S(y)=Σ_{d|∏S}μ(d)τ(d²y),
    δ_S=Π_{p∈S}(1−1/p),
    κ_{α,S}=κ_α Π_{p∈S}(1−p^(−2α))>0.

τ_S is the Gaussian mass on n≠0 without factors from S. The reference measure is cδ_SP₁^S, where P_t^S fixes v_p=0 for p∈S and keeps the geometrics of parameter p^(−t) for the other finitely many primes of the partition. The same inclusion-exclusion, with the subtraction cδ_S, integrates the signed measure into κ_{α,S}P_{2α}^S. The same variance identity gives PSD of the analogous regularised kernel for the deleted measure.

If indicators divisible by a removed prime are included, they vanish and the form has a radical; SPD only holds on an independent family of surviving indicators. Do not call the whole deleted family SPD.

Therefore the canonical positivity of −R by itself is NOT specific to the complete Euler product. An eventual link with Q_T may still use a specific identity that fails after deletion; it must be proved. Inheritance of the kernel does not refute every possible link, but forces locating where that information enters.

## 11. Final verdict on the complete CONSTRUCTOR_005

Final memo §§0–10 read. **All claims labelled PROVED are approved within their scope.** The previous experiments are not needed for the proofs and are not used as evidence of sign once (5) is available.

Specific checks:

- ν is applied to an algebra generated by finitely many indicators. Every product X_dX_e is X_lcm and H=|A−μ₁|² has a FINITE expansion including X₁. There is no problem of global σ-additivity nor of a divergent zeta law below s<1.
- The change of variable in (3), the factor 2 in Z, the sign −Z and the complex variance identity are correct. Strictness on distinct divisors d≥2 has a valid triangular proof; d=1 would be a constant and is correctly excluded.
- In (6), H_s(d,e)=E_s[(X_d−1/d)(X_e−1/e)] expands with exactly the four indicated terms. The splitting H_s=G_s+v_sv_s* is correct. Π is a real Gram matrix with entrywise convergent integral. There is no attempt to identify v_s with the pole of the node.
- The block control §6 uses the comparison of minima in the correct direction; the global proof §5 neither uses nor needs the false global pointwise domination of §8 of this audit.
- §7 recovers the positive cross terms: G_s=0 on coprimes; v_s(d)>0 and q_d−1/d<0 by concavity, so both contributions are entrywise strictly positive. This observation does not add a link to Q_T.
- §10 correctly limits the identities of τ_P(k²y) to k coprime to P. Its mass reference is δ_Pc and the Mellin factor is Z_αΠ_{p|P}(1−p^(−s)), NOT δ_PZ_α. The difference between these two factors is kept. The absence of a constant term in τ_P gives exponential cancellation at zero. The Haar centre for the surviving indices is still Σa_d/d. The SPD claim is restricted to those indices, and the vanishing indicators are not counted as strict directions.

The PSD completion is an exact identity with R defined before the argument, so it is neither a favourable choice of diagonal nor an abstract root of the node. At the same time, the deletion test proves that this sign is inherited: it does not yet provide full specificity. Both claims must be communicated together.

**Final status:** canonical auxiliary resolved, full target D unresolved and active. What follows is to build and verify the map and the link to Q_T, including domain, tails, archimedean, polar and all modes. None of those obligations is satisfied by the auxiliary result.
