# Direct transfer of certificates by mixing changes of scale

**Selection.** The convex average of twists without change of scale was already discarded in G2_B8_R2 §3.2 and R162_1102_CHARACTER_FAMILY. The reason is the extremality of the phase one in each coordinate of modulus ≤1. It is not reopened. We consider only the additional change that would allow a positive complete form of window T₀ to be applied literally to all tests of a larger window T.

Let F be a test on (−T,T). Compress its logarithmic variable via G(t)=a⁻¹ᐟ²F(t/a), with 0<a≤T₀/T<1. Unitary translation and modulation of G are allowed. By polarization it suffices to compare the kernels at the differences |r|<2T. A source contact of displacement log n moves to displacement (log n)/a because c_G(s)=c_F(s/a) before modulating. Consequently all contacts of all terms lie outside the open interval (0,(T/T₀)log 2). If 2T>log 2, the target contact at log 2 is interior to the window and belongs to that interval.

Also for a mixture of finite mass no atom coming from the continuous background can appear there. In a compact neighbourhood of log 2 inside the indicated interval, the off-diagonal archimedean part has density uniformly bounded after the change of scale: aK(ar)=O(1/r) by the singularity K(s)=O(1/s) at zero of P47. The polar part has density proportional to a cosh(ar/2), uniformly bounded. The modulations introduce factors of modulus one and the diagonal terms keep support at zero. Hence the mixed kernel is absolutely continuous in that neighbourhood, while W has there an atom of nonzero weight. They are distinguished on complete forms over smooth tests: polarizing and using pairs of bumps in the interior of the window, at distance log 2, allows probing the kernels locally (fix one bump approximating a delta and vary the other).

**Decision.** Discarded: an exact identity of W on a larger window via a finite mixture, in total variation, of these compressions, even with modulations. The proof holds for measures over continuous scales. It does not decide an inequality with a signed remainder, nor decompositions that cut pieces of the profile and recombine their crossings. The obstruction uses the location of the first contact and not the sign of W. Independent cross-check and review.

## Direct domination also fails, even in the target primitive sector

Fix a₀=T₀/T<1. There are real primitive tests Fδ, normalized in L², such that, uniformly in 0<a≤a₀ and in every modulation ω of the source,

    W(Mω D_a Fδ) − W(Fδ) ≥ log(1/a₀) − o(1),       δ↓0.

Here D_a is the unitary compression above. Translations adjusting the support to the source window are allowed. The estimate excludes W(F)≥∫W(Mω D_a F)dμ for every primitive F and every choice of an average of mass one, even with test-dependent parameters.

**Test.** Choose d>0 with 2d<min(log 2,2T). Centre three copies of the same smooth nonnegative bump of width δ and L² norm one at −d,0,d. Combine them with coefficients 1,−2cosh(d/2),1 and normalize the sum in L². Both moments with weights exp(±t/2) vanish exactly. For small δ the supports are separated and the total diameter is less than log 2. Both the test and all its compressions are free of arithmetic contacts. Its L¹ norm is O(√δ).

**Estimate.** Denote by H the archimedean form with multiplier m of P47 and by fδ=|Fδ|. The Lévy representation with positive kernel gives H(Mω D_a Fδ)≥H(D_a fδ) by the pointwise inequality of moduli on the increments. On the original test H(Fδ)−H(fδ)=O(δ): only crossings of bumps of opposite sign contribute. There the kernel is uniformly bounded by the distance between supports and each product of L¹ norms is O(δ). The polar term in the source is O(δ) in modulus uniformly: its difference kernel is bounded on this diameter and the L¹ norm after compression is √a times the initial one. In the target the polar term is zero.

By monotonicity of m in |t|, H(D_a fδ)≥H(D_a₀ fδ). The difference of multipliers m(t/a₀)−m(t) is bounded and tends to log(1/a₀) at both ends by the asymptote of m. The spectral mass of fδ totals one and escapes every bounded interval since |widehat(fδ)|≤||fδ||₁=O(√δ). Plancherel proves H(D_a₀ fδ)−H(fδ)→log(1/a₀). Combining the bounds gives the announced inequality.

The test detects the archimedean cost before meeting any prime. A strategy with explicit subtraction of that cost, subnormalized coefficients or an operator combining distinct pieces would have another pending inequality. Antecedents of the estimate: P47 thm:A, lem:mbounds and prop:nearfree.

## Residual cost of the first prime after correcting each scale

Assume 2T>log 2 and a₀=T₀/T<1. Even after subtracting the cost log(1/a) *specific to each scale* there remains, for a family of unit primitive tests, the uniform bound

    inf_{0<a≤a₀, ω real} [ W(Mω D_a Fδ) − log(1/a) − W(Fδ) ]
        ≥ (log 2)/√2 − o(1).

For the proof, let Gδ be the unit primitive triple above, with d fixed so small that two copies separated by log 2 have total diameter less than min(2T, log 3, (log 2)/a₀) for small δ. Centre their sum Fδ in the window and divide by √2. The disjoint copies keep the vanishing moments and c_Fδ(log 2)=1/2 exactly: on translating by log 2 only the two identical copies overlap. The target therefore has W(Fδ)=H(Fδ)−v₂/2. After compression no contact remains. The polar bound O(δ), the diamagnetic inequality and the comparison H(Fδ)−H(|Fδ|)=O(δ) remain valid by separation of the six pulses.

To allow a arbitrarily close to zero an additional uniform estimate is needed. Put f=|Fδ| and h_a(t)=m(t/a)−log(1/a)−m(t). On 0<|t|≤R one has h_a(t)≥log|t|−C_R, since m(z)−log z has finite infimum on z>0. The negative part on that interval costs at most O_R(δ) when integrated against |widehat f|² dt/(2π). For |t|>R, write m(t)=log|t|+c+η(t), where η(t)→0. Then |h_a(t)|≤2 sup_{|z|≥R}|η(z)|. First let δ↓0 at fixed R and then R↑∞. Thus H(D_a f)−log(1/a)≥H(f)−o(1) uniformly, which gives the bound. For averages one integrates the energy already corrected scale by scale.

The additional necessary cost is at least v₂/2, even for a₀ arbitrarily close to one; the test depends on a₀. The bound is for the comparison error and does not give the minimal energy of W. PROVED after independent audit.

Direct antecedent identified in the cross-check: the double packet isolating log 2 and its value 1/2 are already P47 lem:cpos and cor:Qp. What is additional here is the uniform bound after subtracting log(1/a), applied to the transfer of certificates.
