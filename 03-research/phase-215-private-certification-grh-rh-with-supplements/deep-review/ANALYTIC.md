# Deep audit of the analytic deduction of paper 46

Status: first batch reconstructed. The argument of lines 2492–3274 and 5107–5408 was audited, together with the heights principle 3386–3511 and the elementary reductions 4190–4308 and 4626–4788. This record separates the implications that have been checked from the automorphic theorems that still have to supply their premises.

## Large sieve and zero detection

The variant cited as `an:thm-HB` was collated with the facsimile of **Corollary 2, p.238**, of [Heath-Brown, A mean value estimate for real character sums](https://matwbn.icm.edu.pl/ksiazki/aa/aa72/aa7234.pdf). It allows arbitrary complex coefficients and sums over primitive real characters of conductor ≤Q, with cost `(QN)^ε(Q+N)` and the sum of `|a_n1 a_n2|` over square products. It was not confused with Corollary 1, which is restricted to squarefree indices. Status: published input collated; the classical theorem was not reproved from its foundations.

Reconstruction of `an:prop-density`:

1. For `χ=ξχ_d`, with d prime and d∤N, the component at d is primitive and non-trivial. The primitive conductor contains d; the factors omitted on passing to modulus Nd come from N. Hence inclusion–exclusion over e|N gives a constant depending only on N in Pólya–Vinogradov. The product is not principal, so L is entire.
2. The exact identity for the truncation remainder is obtained from `s∫_Z∞S(u)u^{-s-1}du−S(Z)Z^{-s}`. Replacing S(u) by S(u)−S(Z) is correct even when Z is real and not an integer.
3. In the product with the mollifier, `b_1=1` and `b_n=0` for `1<n≤Y`, since `Y≤Z`. The length is ≤YZ=X. The bound `|b_n|≤τ(n)` is uniform in d, ξ and s.
4. The detection uses the mean of the holomorphic function g, followed by Cauchy–Schwarz, on a disc of radius θ/2. The disc lies in the fixed rectangle because every zero is to the left of 1. A count of zeros is not exchanged with a count of characters: at least one zero is detected per bad prime, which is precisely the object being counted.
5. In the error term, the saving is `e1=θ(2−θ)/4≥3θ/8` for `0<θ<1/2`. The factor X from summing over primes has been included.
6. In the large sieve, writing `n_i=k u_i²` with k squarefree and dropping the squarefree restriction to obtain an upper bound leads to `Σ k^{−α}(Σ u^{−α})²`, `α=1+θ−2ε>1`. For k≤Y the term is `Y^{1−α}/k`; for k>Y the tail is `O(Y^{1−α})`. The factor log Y is present and the extension to infinite sums converges.
7. The exponent before absorbing the logarithm is `1−θ²/4+(2+θ/2)ε`; given `θ<1/2`, the logarithm is absorbed in the margin up to `3ε`. With `ε=θ²/32` the exponent is `1−5θ²/32 < 1−θ²/8`. The constants may depend on θ; θ is fixed before X.
8. Integrating over the rectangle and summing over the finite number φ(N) of ξ preserves the saving. The comparison with `X/(φ(N)log X)` allows d to be chosen in any fixed coprime class.

**Local verdict:** `an:prop-density` and `an:cor-choice` are checked from the declared classical inputs. They need no global non-vanishing hypothesis for the twists, nor GRH. The chosen prime may depend on the box and on the zero to be excluded.

## Transform and Landau's lemma

`an:lem-R` (2547–2589): integrating `1/n−1/x` produces `D_q(s)/(s(s−1))`. The principal double pole cancels on subtracting `log x/φ(q)`. The remaining numerator vanishes at s=1 by the definition of c_q. The residue at ρ is

`(n_q(ρ)−n_q^K(ρ))/(φ(q)ρ(1−ρ))`.

The sign is correct: the logarithmic derivative of the twists appears with positive sign in D and is divided by `ρ(ρ−1)`. Poles may cancel; the text does not assert that every zero necessarily produces one.

`an:prop-pnt` (2594–2630): for fixed moduli, an exceptional real zero contributes `t^β1`, with β1<1 fixed, which can indeed be absorbed into `t exp(−c√log t)` for t sufficiently large. The tail of the integral converges. Holomorphy of the transform at 1 forces the constant limit of R to be zero. No uniformity in d beyond what the PNT provides is used here.

`an:lem-landau` (2636–2682): f≥0 only after v0; the remaining initial integral is entire. If the abscissa of convergence σc exceeds β, a holomorphic continuation at σc would allow expansion in a disc centred at σc+1. Tonelli on the non-negative coefficients would extend the convergence to σc−δ, a contradiction. Meromorphy and the hypothesis of simple real poles turn the singularity into a simple pole with positive residue for Ψ, negative for F. The argument does not exclude complex poles by a local sign reasoning: it excludes them by guaranteeing holomorphy in the half-plane of convergence.

`an:thm-criterion` (2842–2874): one first chooses a d whose set of twists has no zeros in the box containing ρ and the real segment [β,1). This makes all possible real residues to the right of β non-negative. The alternative of a negative real pole in Landau's lemma is excluded, and then the residue at ρ cannot cancel against that of a twist. The order of quantifiers is correct: the premise is required for every d in the class; the proof uses one that depends on ρ. **Verdict: checked as an implication.**

## Existence of data and their ranges

`an:lem-behrend` was reconstructed: there is no carry because each integral convex combination has digits smaller than the base `Λ0H`; both encodings lie in [0,o). The congruence becomes an equality and the strict convexity of a sphere forces equality of the three vectors. The degenerate case of base 1 has only one vector and causes no exception.

In `an:prop-sparse`, the 2-adic part of g has order exactly `2^s`, by the valuation of `(1+2^v w')^{2^j}−1` with v≥4. For ℓ=2 one uses the order of 4 modulo `3^c`; for ℓ odd, squaring removes signs and Behrend forces e1=e2=e3. The lifting-the-exponent formula produces the contradiction `2^s≤(ℓ+1)i<(L+1)l0≤2^s`. It is not being assumed that ℓ is coprime to all of q1: only to q', as the definition requires.

`an:lem-windows` uses moduli `Q≤W^A≤(log y1)^A`; Siegel–Walfisz is applied at both endpoints. The interval in p is multiplicative, not a short additive interval that would require another theorem. The cost of prime powers is smaller than the main term because `√y2≥e^W`.

The construction `an:thm-data` satisfies D1–D8 for every sufficiently large integer x, with fixed parameters:

- The minimal powers of 2 and 3 give m and r in the declared intervals.
- Rounding b to a multiple of q1x1 changes log b by less than 1; rounding x1 down preserves the inequality of the six logarithms.
- The density of the set of places loses `x^{ε/2}` and a fixed power of log x; the latter is absorbed by the other `x^{ε/2}`. The integer n depends on ε, which is already fixed.
- The h_K+1 intervals of primes are disjoint. Equality of two ideal classes gives `p_i bar p_j` principal and an integral generator; the complex norm is the positive product p_i p_j, with no need to choose all the primes principal.
- For N one needs a generator of norm N in E, not in K. The representation as a sum of two squares suffices because i∈E.

The inequalities S1–S7 were reviewed. Their margins come from `log x≥10^14 C_P`, `log b≤x^{1/100}`, `x^{10^6}≤x1` and `x1^{10^6}≤b`. In particular, the relation that 51 needs in order to absorb `f2^{3−k}` is indeed available. The analytic existence takes as input that C0(q0,d) is finite and independent of the data; this property, specific to the kernel of 49, was checked later in THETA, CJ08 (`pz:C0` and its absorption). It cannot be omitted from the list of inputs.

## Product with a prime-dependent twist

`au:product` and `au:twistprime` (3403–3511) were reconstructed completely as abstract results. The field isomorphisms are abstract, not continuous; `overline(Q_ℓ)` and C are algebraically closed of characteristic zero and of transcendence degree the continuum. This allows embeddings of number fields to be extended and a transcendental element to be moved so as to contradict a uniform valuation bound.

In the proof of `au:twistprime`, the two changes of basis u and u' correspond to iota and to bar-iota; **they serve the same twist θ_iota** because the index is defined simultaneously for all the permitted twists. This is a necessary point and it is indeed included in the definition. Taking determinants gives the cost `2δ`, not δ. Complex conjugation does not commute with an arbitrary automorphism σ: the text correctly uses `σ'=cσc`. The bound for the conjugate Gram matrix comes from Cauchy–Schwarz on the exterior power and from Fischer/Hadamard, keeping the volume factor squared.

**Verdict:** abstract principle checked. The construction of the concrete twisted lattice and the height bounds for the quotient of determinants that 53–56 must give remain separate.

## Final assembly

The Short Forms and Spanning reductions of 46 are correct **if I1–I7 are supplied with exactly the declared scope**:

- The rounding `g_ℓ=floor(gain_ℓ−err_ℓ)` makes the product integral after multiplying by cB, with the correct direction of the valuation.
- The seesaw constant cancels before estimating. The archimedean bound for cB is multiplied by 2 because a squared norm is being bounded.
- The index of a union is controlled by block matrices; the definition allows families of arbitrary size and the cost is not unduly multiplied by that size.
- `au:onetranslate` is an application of Cauchy–Schwarz to the conjugate mean of BB*. `au:few` is an iteration that reduces the codimension; the initial inequality forces `ρ=2dim V/(5dim W)≤1`, so that the rounding of the number of steps is controlled.
- Restricting to the ramified part costs at most the number of translates times the codimension of the source; the error b^-8 stays within the final budget b^-2.

For the covolume theorem, the assembly 5014–5052 is also correct as an implication from `inj`, `aux`, `factor`, `regular`, `onelift`, `hecke` and `mult`: the cost of the auxiliaries of rank ≤4d/b² is absorbed and the sign `−H_main` is preserved. None of those new inputs is taken as verified by this deduction.

Finally `an:lem-rem` identifies the sum over primes exactly. In `an:lem-hmain` the positive bound for the main term allows nH to be replaced by dH; without that positivity the argument would be invalid. The bound is proved in the text, using `Λ_K≤2Λ`, `floor(n/ν)≥n/(2ν)` and `log(M/Ω)≥20log b`.

The cancellation delivers `m rem≤fa(log b)^5`. To pass to R, the factor `#Φ_a/#Φ_b` is kept and costs log b. The PNT is applied only at x1, enormously larger than x, with q0,d fixed. The transition from integer x to real y costs O(1/x), smaller than the scale sought. Choosing `q0=18480q` and removing the added Euler factors, whose zeros have real part 0, gives the half-plane. The functional equation of the primitive character gives the other side of the strip.

**Conclusion of this batch:** the implication from the three automorphic theorems, valid for the constructed data, to GRH for Dirichlet and RH is checked, under the classical inputs indicated and the finiteness of C0. The pending work is now localised in obtaining those premises and their junctions rigorously; not in a supposed inference of RH from checks of finite windows.


## Cancellation of gains and the level window: rereading for the junctions

`def:au-hmain` and `au:gains`, 46:3804–3883, were collated directly. In the inert case, Λ_K(p^e) is 2logp for e odd and 0 for e even; in the ramified case d, the normalisation v(π_d)=1/2 produces logd. This agrees with the sets I_p and the p-adic normalisation used by 49. A non-split prime is prime to q₁, so that the partner u(−p^e) is defined in all the non-zero summands. For p≥x₁, y/p^e≤a/x₁≤κ annihilates each positive part. There is no tail of primes discarded without estimate.

On multiplying the gains by 2logp and summing, the identity of `au:cancel` removes exactly the two finite packets: that of the places of κ and that of Pa. The factors m,k and #Pa are kept; the sign of the remainder is not used for this equality. Stirling with upper remainder 1+(log a)/2 and logΩ=−1−c₁+log(2π/rd) cancels c₁ in the difference s∞(a)−s_main. The lower bound for logN in `au:level` leaves aG+(15/2)a logb+m(1+(log a)/2), dominated by (23+15/2+1)a logb<32a logb with the sizes already checked. This is the precise reason why the same window of N serves in the application of Short Forms; the upper bound for N is used separately in the dimension ratio of Spanning.

This check discharges the content and the normalisations of the import `au:gains` in 49. It does not by itself discharge the theta constructions that have to realise those gains; their audit is THETA/JUNCTIONS-THETA.
