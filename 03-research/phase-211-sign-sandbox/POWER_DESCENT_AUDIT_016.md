# POWER_DESCENT_AUDIT_016 — What is missing to descend from the high-pass tails

Status: PROVED and reviewed: density obstructions, logical non-implication and specific constructions of016; see §§6–8. Papers untouched.

## 1. Corpus and difference in scope

Consulted the project rules, ROUTES-TRIED-INDEX entries POWER014–015, grid/crossword and searches for highpass, dense, vanishing moments, all moments vanish and continuous moment functional. The bridges BRIDGE002/CONFLUENT_BRIDGE014 and their review prove strong density of the COMPLETE confluent envelope. The obstructions of growing thresholds of THREE002 dealt with another temporal concentration. The following exact application of growing Laplace zeros to the current tails was not found registered. Continuity of moments and analytic uniqueness of Laplace are standard tools; no novelty is attributed to those general principles.

## 2. A high-pass zero prevents density in the norm of015

Let eta>0 be fixed and use L²_eta={f causal: e^(eta y)f∈L²(0,infinity)}. For each integer r>=0, the moment

    ell_r(f)=integral_0^infinito y^r f(y)dy

is a continuous functional, with exact bound

    |ell_r(f)|<=sqrt((2r)!/(2eta)^(2r+1)) ||e^(eta y)f||_2.

Every function of Q^k V_N, Q=s/(s+u), with k>=1, has a Laplace transform with numerator divisible by s^k and denominator non-zero at0. Hence ell_r(f)=0 for0<=r<k. In particular the union of ALL those spaces with k>=1 remains in the closed hyperplane ell_0=0 and is not dense in L²_eta nor in the stronger norms of015 that include that weight.

The obstruction persists on the relevant primitive carrier: choose g≥0 smooth compactly supported inside the half-line, with positive integral, and F=(1/4-D²)g. Its two Tate moments vanish by integration by parts, but ell_0(F)=(1/4)integral g>0. For any h of that union,

    ||e^(eta y)(F-h)||_2>=sqrt(2eta)|ell_0(F)|>0.

It does not suffice to allege that the Tate restrictions already select the pertinent tests: the additional ordinary moment is not a consequence of them. Translating functions does not eliminate a zero of order k in Laplace at0 either, since the transform gets multiplied by a non-zero exponential.

## 3. Zeros of growing order: every strong limit is zero

Suppose k_j→infinity and f_j∈Q^(k_j)V_(N_j), with N_j arbitrary. If f_j converges to f in L²_eta for a SAME eta>0, the continuity of each ell_r and its eventual vanishing imply ell_r(f)=0 for ALL r.

The Laplace transform H_f(z)=integral e^(-zy)f(y)dy is analytic in Re z>-eta, by Cauchy--Schwarz on compacts. The point0 lies in that domain and H_f^(r)(0)=(-1)^r ell_r(f)=0 for all r. By the identity theorem H_f is zero on the connected half-plane. Uniqueness of Fourier on a vertical line implies f=0.

Thus a sequence of normalized vectors with k_j→infinity cannot have a non-zero strong limit in any common norm of015. This result does not depend on how N_j grows nor on a rate between N_j and k_j. In particular it does not authorize a bridge by density of the union of individual tails in THAT topology.

If an assignment k(N) is>=1 for all large N and has only finitely many blocks with k0, its union also stays far from generic tests: the closure is contained in the hyperplane ell0=0 plus the finite union of those exceptional blocks. If k0 appears in arbitrarily large degrees N, density can be recovered by the confluent bridge, but precisely the initial blocks without sign that015 does not decide have been reintroduced.

The statement does not exclude approximations in a different topology where those moments are not continuous, nor an additional moment correction. Such an argument would have to verify again the continuity of the COMPLETE form, including all contacts and the polar; L² density alone does not prove it.

## 4. Logical falsifier of a descent based only on structure and eventual positivity

Consider the modified form W_C[f]=W[f]-C||f||². The finite and infinite mixture identities of015 are preserved, because the norm² satisfies the SAME identities with the same weights. The linear partitions of forms deduced from those identities are also preserved. The EVENTUAL theorem is preserved for each fixed N: its Rayleigh quotient grows like .5logk plus a bounded block, and subtracting C only changes the constant, leaving every sufficiently large k positive with another threshold.

However one can take C4 and obtain an explicit negative initial vector. For f(y)=e^(-31.5y), its complete quotient is

    W[f]/||f||²=psi16-logpi+2zeta'(32)/zeta(32)+126/992.

Since psi16=H15-gamma<H15<7/2, logpi>0, zeta'(32)/zeta(32)<0 and126/992<1/2, this quotient is strictly less than4. Hence W_4[f]<0.

This refutes only the logical inference 'positive mixture + partitions + eventual positivity in each dimension ⇒ sign of all initial members'. It is a DIFFERENT form, with archimedean symbol m-4, not a counterexample to the real W nor an argument against using its specific coefficients and certificates. The initial certificates of W do not transfer to W_4 and it is not claimed that they do.

## 5. Obligation that remains legitimate

To descend one needs an inequality that controls the defect of the initial blocks by additional information, or a joint uniformity that reaches the pertinent mass of a partition and allows passing the form to the limit. The complete confluent bridge remains valid. The previous results only prevent replacing it without proof by the union of tails having prescribed zeros; they do not classify or close the new inequalities being constructed.

## 6. Review of POWER_DESCENT_016 and its verifier

APPROVED in full. The complementary identity includes the polar because the products of evaluations of Q and L at±1/2 sum to1. The filters commute and the binomial iteration is exact for each contact and the complete sum. The formula (-1)^r Delta^r a_k=W[L^rQ^k f] is obtained by induction without normalizing the vectors. Applying015 to the space V_(N+r) is legitimate for fixed N,r and provides uniformity in the numerator, not a common threshold in r.

The telescopic series of energies converges absolutely: the partial sums converge by Q^k f->0 in strong norm, and the tail of its terms is positive by EVENTUAL applied to Lf. A positive tail of a convergent sum is absolutely summable; the prefix is finite. Positivity of all terms was not assumed to prove it.

The conditional binomial law and the Lipschitz bound1/(2sqrt(m)) are correct. For a fixed edge r<=R, the conditional probability of having few failures tends to0 for each finite frequency, and domination by1 justifies EDGE. Its uniform version on the sphere of V_N uses a finite positive compression of bounded multipliers, whose trace tends to0; operatornorm<=trace is the correct step.

The ENERGY contribution of the fixed edge was also verified: L^r f has initial order N+r and the same numerator degreeD, so its degree deficit is r0+r. The asymptotics015 give norm²O(m^(.5-r0-r)) and RayleighO(logm). Multiplying by binom(m,r)=O(m^r) leaves O(m^(.5-r0)logm), which tends to0 because r0>=1. The sum over r=0,...,R is finite. The vanishing of energy was not inferred only from the vanishing of mass; its own estimate was provided here.

The current verifier tools/power_descent_016_verify.py was executed with PASS. Its elementary bound2L32<H15-1+1/16+2/31<3 is correct: psi16<H15,logpi>1 and zeta'/zeta32<0. Hence the modified falsifier W4 has the stronger margin<-1 on the initial vector. This strengthens the weaker bound of§4 of this audit without changing its scope.

## 7. Review of POWER_JOINT_SCALE_016

APPROVED. The transformation Z=tau²/(u²+tau²) produces Beta(k+.5,N-.5), and the norm factor is u^(1-2N)B/(2pi), with the contribution of both half-lines correctly incorporated. Concentration for k/N->c and convergence of correlations to cos(u sqrt(c)t) are consequences of beta mean/variance. For the average of m, the uniform bound on E tau² and the logarithmic growth provide the required integrable uniformity. The counterexample to uniform vanishing of contact2 in a linear cone uses a fixed resonant c and k=ceil(cN); it makes no claim of complete sign.

The identity of the endpoint P=s^(N-1) with the initial orbit of dimension1 is exact. The complete Gram entries have sign(-1)^(r+i) when i+j=2r, and the declared beta parameters are correct. The Jacobi coordinate with final exponent±.5 is interpreted by taking the maximal degree ALLOWED by the sector for N (null coefficients can be filled in), not necessarily the effective degree of a particular P. Thus the statement covers the whole sector without changing its weight.

The temporal mean(N-.5)/u follows from the phase derivative with correct sign. For k>=1, the phase jump of(i tau)^k contributes nothing because the transform vanishes at0. The second Parseval derivative uses exactly k²/tau²+(N²-k²)/(u²+tau²); the beta moments produce E y² and Var y of the memo. The algebraic extension k0 coincides with the known temporal gamma law. Jensen proves the exponential growth in N of the NON-centred weight for all k, and cosh/Jensen prove that centring does not uniformize both weights simultaneously: the product of their expectations is at least1+2eta²Var, as claimed (in fact the same hypotheses allow a larger bound).

These results refute precise uniformization tools, not the sign of W in linear or quadratic cones. The quadratic cone keeps the OPEN status of the memo and is not turned by this audit into a theorem of uniform spectral dispersion.

## 8. Final status of this round

The moment lemmas of§§2–4 were independently reviewed and approved. The two specific constructions of016 are reviewed and approved in§§6–7. Global arithmetic descent, sign of the initial blocks and joint sign uniformity remain open. No paper was edited.


## 9. Complement: shifted filter, dense span and insufficient positive diagonals

**PROVED; mathematical and literal review of cases approved.** It is a complement of the falsifier W4 of§4/§6, not a new sign principle. Dedup: targeted searches in indices01–06, grid/crossword and corpus; antecedents015 (weighted orbits),014 (confluent density),016 (partition and moments) and010 (weighted multipliers). The following literal formula was not found; no absolute novelty of the exterior filter is claimed.

Fix u=63/2, delta=1, eta=3/4, f0(s)=1/(s+u) and Qdelta(s)=(s+delta)/(s+u). Use H_eta={h:e^(eta t)h belongs to H¹(0,infinity)}, the norm of014. The filter and its inverse are bounded causal operators on that space:

 Qdelta=1-(u-delta)/(s+u),
 Qdelta^(-1)=1+(u-delta)/(s+delta).

Their weighted exponential kernels are integrable because u,delta>eta; the derivatives are also controlled by the exponential convolution equation. Thus each fixed power is a bounded isomorphism. In particular Qdelta(0)=delta/u does not annihilate the ordinary moment; the zero -delta lies outside the half-plane Re s>-eta where the moments of§2 are read continuously.

For r>=0 put fr=Qdelta^r f0. For each m, span{fr:0<=r<=m}=V_(m+1)(u): expanding Qdelta=1-(u-delta)/(s+u) gives a triangular matrix with non-zero diagonal over the powers (s+u)^(-j-1). By014 the union of those spaces is dense in H_eta. For EVERY fixed R, span{fr:r>=R}=Qdelta^R span{fr:r>=0} is also dense. This genuinely avoids the zero-moment obstruction, even for a tail of the family.

Now let W4=W-4||.||², the same complete falsifier of016. It is continuous on H_eta by014/002. Put Q0=s/(s+u), gk=Q0^k f0 and d=delta²/u², p=1-d. The EXACT scalar identity is

 |Qdelta(i tau)|²=d+p|Q0(i tau)|²,
 Qdelta(-1/2)Qdelta(1/2)=d+p Q0(-1/2)Q0(1/2).

Therefore, including the polar, all contacts and the norm,

 W4[fr]=sum_(k=0)^r binom(r,k)d^(r-k)p^k W4[gk].

The sum of functions has not been expanded quadratically suppressing crossings; a multiplier identity of the complete forms is used.015 in dimension1 gives W4[gk]~C k^(-1/2)log k, C>0, and the same for W. There exists K with all those diagonals positive for k>=K. The terms k<K of the binomial sum have absolute loss O(r^K d^(r-K)), exponentially small. In the bulk k>=pr/2 the binomial probability tends to1; there W4[gk]>=c log(r)/sqrt(r) for large r, uniformly in pr/2<=k<=r. Hence W4[fr]>0 for ALL sufficiently large r. Also W[fr]>0 eventually. These are scalar statements at fixed initial dimension1; not uniformity over all numerators nor positivity of the crossed pairs.

However,016§6 proves W4[f0]/||f0||²<-1. The span of any tail r>=R is dense and W4 is continuous; hence there exists a FINITE combination v=sum_(r=R)^L c_r fr with W4[v]<0. Choosing R after the previous threshold guarantees that each generator used individually has W4[fr]>0. All terms are causal rationals in H_eta; no weak topology losing the polar or the arithmetic is used.

The inference «dense span in the form norm + eventual individual sign of its generators implies sign on that span» is refuted, even after repairing the zero moment by an invertible filter. It is not claimed that the real W is negative, nor PSD pairs, nor impossibility of a control of crossings specific to the real datum. There is no new certificate, new time window, tower of degrees or modification of papers.
