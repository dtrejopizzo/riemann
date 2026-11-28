# Deep audit of Spanning and sieve systems

This record continues the review of P51/P52. The lines are those of the local `main.tex` files. Statuses: **proved** means that the indicated obligation was reconstructed; **literal failure** identifies a false inference as written; **pending** identifies the next dependency that remains to be closed. The papers are not modified.

## Pass 1 Siegel step to squares of orbital sums

Object: P52 `pff:S`, lines 4223–4238; proof 4279–4556. Those lines were read in full, together with the proofs of measures, supports and fibres in 4640–5096 and 5220–5520. The real sieve estimate (R) and the finite mass limit (F) are not inferred from this audit: here the assembly step (S) is separated from those other results.

### Literal finding with a repair already available in the manuscript

**P52:4364–4365, `pff:offT`: literal failure.** The frequency is cut to `b∈u bar(u) O_skew` and it is then said that as `u→0` the cut integrals converge to the integral over the whole space. Under the local topology used, those domains contract to zero. The dual region `(u bar(u))^{-1} O_self` expands; it is not an approximation of the identity either. There is no convention of inverse size declared in this paragraph that would change the meaning of `u→0`.

Exact model: let `E_v/Q_5` be unramified quadratic, `k≥3`, standard form `Q(x)=Σbar(x_i)x_i`, `α=1`, and `Ψ=1_{e_1+5O_E^k}`. We normalise both additive lattices to volume one and the character as in `pfg:duality`. For `u=5^j`, every `b∈5^{2j}O_skew` gives trivial phase on that support, so that the cut integral is `5^{-2j}·5^{-2k}→0`. The density of `Q=1` on that support is `5^{1−2k}>0`: the map `Q−1` carries the support to `5Z_5`; its real coordinate in the first variable has unit derivative after extracting the factor 5, and the fibres are counted by Hensel or by local change of variable. The normalised average over the fibre is therefore `vol(support)/vol(5Z_5)`.

**Repair without loss:** take `u=varpi_1^{-j}` with `varpi_1` of `pfg:psi(c)`. The domains `u bar(u)O_skew=varpi_1^{-2j}O_skew` exhaust the group and the duals contract. More directly, the manuscript already contains the correct argument in `pfg:orth` and `pfg:fibres(a)` (P52:4970–5080): it uses `B_l=varpi_1^{-l}O_skew`, which grows, and an integrable bound independent of `α`. `pfg:rem-fibres` applies that result explicitly to `pff:offT`. For this reason this erratum does not leave the local identity without proof nor change the constant of (S).

### Obligations closed by reconstruction

| Obligation | Status and justification |
|---|---|
| Skew/self-adjoint duality, even in residue characteristic 2, `pfg:psi`, `pfg:duality` (4899–4967) | **Proved.** There exist an element of trace one and a skew unit in the unramified extension; the integral decomposition into two coordinates proves that the lattices of volume one are dual. There is no division by 2 in the local proof. |
| Gauss bound `pfg:gauss` (4993–5022) | **Proved.** Differencing the phase leaves a linear character; unimodularity identifies its annihilator with `I_b^κ`. The volume of the stratum of frequencies of index `I` is ≤`|g|^{-1}[O:I]^{1/2}`. Summing one obtains `∫|G|≤ζ_O(μ)|g|^{κ−1}` when `κ≥2μ+1`. |
| Construction of `ν_β`, `pfg:fibres` (5024–5096) | **Proved.** Finite combination of indicators of classes, absolute Fourier, orthogonality on `B_l`, domination independent of `β`, positive limit and support on the fibre. Continuity and disintegration follow by dominated convergence; uniqueness is recovered with averages over decreasing slabs. |
| Coarea `pfg:coarea` (5228–5248) | **Proved.** Change of basis of determinant `bar(π_N)^{-1}` and the change `t→−N^{-1}t` leave exactly `|π_N|_T^{-1}`. Only finitely many functions `φ_t` appear; the preceding domination allows the limit to be passed under the integral. |
| Orbital compact support `pfg:Op` (5295–5320) | **Proved, with explicit gauge axioms.** `pfg:cramer` bounds the columns of the unipotent; `pfg:unipinv` and `pfg:sizehead` bound `y` by `60n²`. Applying the same to the conjugate head also bounds the second position; the support of `l` is compact. Invariance under the open `K_M` gives local constancy uniform in `l`. |
| Extension of the fibre `pfg:fibrepairing` (5322–5362) | **Proved from the preceding support.** The integral over `H_T` has compact support; the orbital map is open (Baire). A finite cover by balls gives a common modulus of constancy and a compactly supported and invariant extension. It is not required that `H_T` be compact. |
| Finiteness of the set of heads | **Proved.** P51:3557–3564 defines `B` by a bound on all the conjugates of algebraic integers and `T_entries={δ/δ′}`. It is finite. Thus the use of `pff:headsum`, formulated for finite sets, does not conceal an exchange of infinite sums. |
| Separation `pff:sep` (4464–4475) | **Proved, assuming the cited free level.** Equality of `σz` makes `σ_1^{-1}σ_2∈H(E⁺)`; the local congruence and the exterior integrality place it between the same two class representatives, with an element of `J_X`; the triviality of the stabiliser gives equality. |
| Count of cosets `pff:headsum` (4443–4462) | **Proved as algebra of Gram matrices.** For each reduction `s_i` exactly `#C` distinct coordinates in `C×C` are selected. Each summand is non-negative; discarding the others only decreases the right-hand side. No triangle inequality with a loss `#heads` is used. |
| Sum over a fibre `pff:fibresum` (4477–4492) | **Proved.** The points `l_θ=k_θl_0` occupy disjoint cosets of `H_T∩K_M`. The integrated function is non-negative and constant on each coset by (W2). Each coset has the same volume by unimodularity. |
| Weights and mass `pff:weights`, `pff:rhoD` (4494–4521) | **Proved.** The product formula for each entry cancels `κ_ρ(p,1)` with the archimedean absolute values. There remains `ρ_p κ_ρ(p,1)=r_*√G_t`. Moreover `r(Z)=μ_H(H∩K_M)vol(K_M)^2 #C·(#Hbar #Ubar²)` exactly. |
| Final assembly (4523–4556) | **Proved as an implication from the inputs identified.** Group by `t`, then by `(c,v)` and by `(c′,σ)`; apply cosets, separation and Siegel; divide by `G_t r(Z)/D`. This leaves exactly `(1+b^{-6})a_* ΣR_pq J^T_n(p,q)`. |

### The Siegel formula and its constant

The original of Weil was downloaded to `sources/weil-1965.pdf`, with extraction `sources/weil-1965.txt`. Source: [Weil, Sur la formule de Siegel dans la théorie des groupes classiques](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5988-11511_2006_Article_BF02391774.pdf).

Theorem 5, printed pages 76–77, uses measure of mass one and the condition `m>2n+4ε−2`; in the unitary case `ε=1/2`, `n=1`, it requires `k>2`. Proposition 8 permits the anisotropic case. The local hypothesis of transitivity can be satisfied at a split finite place: the group is general linear and acts transitively on pairs with prescribed product and maximal rank. This does not require RH. Thus the range and the normalisation of mass one cited in `pfg:weil` coincide with the primary source.

In P52:5462–5520 the extraction of the coefficient `α>0` was reconstructed. The identity coset does not contribute; Bruhat parametrises the others by `E⁺`. The Weil representation uses the standard rational character and the adelic measure of covolume one. The archimedean Fourier transform of the Gaussian gives `π^k α^{k−1}/(k−1)!`. The decomposition of the compact quotient into classes of free level gives weight `1/#C` per class. The remaining factor is `|disc E|^{1/4}` by the normalisation of the finite self-adjoint variable. **There is no missing Tamagawa factor 2**, because the quotient of the group is integrated from the outset with mass one.

The bound outside `T` can be justified cleanly as a product of local densities, all with `O_E` of measure one, multiplied by `v^k`. Weyl differencing and the count of characters of each ideal give `≤ζ_E(μ)v^k`, with `μ=3ρ+4` and `k≥2(μ+1)`. For the data, `2f·2^{2−μ}` is much smaller than `b^{-6}`: one uses `ρ≥√x/2−1`, `f≤x^{12}`, `log b≤x^{1/100}`. This last relation is inherited from P46; it must not be replaced by the bound `b≥1000` alone.

### Obligations still open from this pass

1. **Global-local identification of Kloosterman (`pff:locKl`, 4414–4441):** the local expansion in cosets is reconstructed and keeps `vol(K_M)`. To close the global equality one must check that, outside `T`, the unipotent solutions are integral when the head has unit entries and `σ` is integral. The text compresses this into “all data are integral”. The concrete route is to use the elimination by unit pivots of the big cell, P51 `pbm:cell` (3450), and to verify that its inverse is defined over the ring of integers, without introducing denominators other than those pivots.
2. **Free level and stabilisers:** verify the argument of P46 `au:free`/Lemma 14.5 cited by the separation and by the weights `1/#C`. It must be proved for all the representatives of the genus, not only for the standard lattice.
3. **Characters and bases:** check `ψ_f` under conjugation by the representatives `h_c∈H`, and the use of the lattice of P51 `pb:KR`. The relevant requirement is that `H` normalise `U` and preserve the Bessel character; it will be reviewed in their definitions.

Next action: close 1–3 before issuing a definitive verdict on (S), and then reconstruct `pbc:C1` and `pbc:C2`. The failure of direction of the limit is not the pending obligation: it has a proved repair with domination, indeed a correct argument already present in the same paper.

## Closure of pass (S), 28-11-2026

The three preceding obligations are closed:

1. **Integral cell:** P51:3450–3502 constructs `u_1,u_2` by the perfect pairing of `A` and `γA`, followed by LDU elimination. When all the pivots are units, the normalised bases and the elimination are integral. The lattice is the orthogonal sum of the unimodular hyperbolic block and the middle block. The formula `ux=x−Σ bar(h(e′_a,x))e_a` does not divide by 2. Outside T the representatives `h_c` are absorbed by conjugation and the pivots are units, so that the unipotent variables of the global sum are integral. The characters are trivial there. This closes the compressed step of `pff:locKl`, without an additional factor.
2. **Free level in the whole genus:** P46:3598–3610 considers explicitly `Γ∩gJg^{-1}` for any `g`. For `H=U(X_0)` the real group is compact, so that the arithmetic group of a fixed lattice is finite. At a chosen split place, an element is conjugate into `1+p_0M_k(Z_p)`. Its eigenvalues of finite order different from 1 would have degree ≥`p_0−1>k`; impossible. Finiteness and characteristic zero eliminate the unipotent case. This justifies simultaneously the separation and the equality of masses of the classes.
3. **Character and lattice:** P51:529–549 defines `σ(u)` by the entries in the frame; `H` fixes the frame and its duals, so that `σ(huh^{-1})=σ(u)` and the same for `ψ_f`. P51:554–580 proves `K_R=K_U⋊K_H` through the quotient `A^⊥/A`, describes the middle lattice and obtains `K_H∩J=J_X`. There is no change of character caused by `h_c`.

**Local verdict on (S): (b) literal because of P52:4364–4365, but with a complete repair, without loss of constants, already contained in `pfg:fibres`.** Replacing the decreasing limit by the increasing exhaustion proved there, the chain Siegel → fibres → squares of orbital sums is reconstructed correctly, with the measures and parameters identified above. This is a closure of this obligation, not a certification of the rest of P51/P52.

## Pass C2: mean count of lattices

P51:8615–8823 was read and reconstructed, together with `pbc:disc`, `pbc:pack` and the preceding free level. **Verdict on the argument of C2: (a), under its explicit size conditions.**

- `pbc:average`: refining to a common subgroup converts all the fibres into sets of cardinality `vol(J_X)/vol(J′)`; conjugation preserves volume. The free level avoids weights of stabilisers.
- `pbc:index`: the cosets correspond to non-zero rows at each place of `π_N`; `∏(q_w^k−1)≥N^{kf}/2`. Rows are not confused with lines: there is no division by `N−1`.
- `pbc:forms`: decomposing the saturation as a direct summand leaves `N^{fl}` forms on the complement and at most the index `i` on the saturation. Valid also for non-free projective lattices.
- `pbc:zeta`: local Hermite gives exactly `∏_{j=0}^{r−1}ζ_E(s−j)`. The estimate `≤2^r` uses `s≥r+2ρ+4` and `2f≤2^{2ρ}`.
- `pbc:siegel`: Minkowski in real dimension `2lf`, covolume `2^{-lf}|D_E|^{l/2}disc`, and choosing successive vectors independent over E at indices `2f(i−1)+1`, give `∏||X_i||^{2f}≤(lf rd)^{lf}disc`. The discriminant of the complement coincides by unimodularity.
- `pbc:height`: each subspace is determined by a chosen independent tuple; summing over all the tuples only increases. The minimal separation ≥1 and packing give `Σ||X||^{-2f(k+1)}≤5^{2f(k+1)}`. The case `l=0` is treated separately.
- Assembly: with `D=b^{n³f}`, `μ=2ρ+4`, `disc=d_V i`, the inequality `i(d_Vi)^{-k}≤D^{μ+2}d_V^{-(k+1)}i^{-(r+μ)}` uses `i,d_V≥1`, `r≤k`. The sum is bounded by `2^kD^{2ρ+6}[N^f(25n³f rd)^{f(k+1)}]^l`. Each factor is absorbed into `β_*=b^{kf/4}`, keeping `1/2`. There are no uncontrolled infinite sums.

**Range of application:** `l≤n³` is essential in the last absorption; the passage from pairs to corank already audited in `ppi:pillars` gives `18i≤n³` and `l≤i+1≤n³`. C2 is not applied in the interval `n³<l≤k`. The conditions Z4/Z5 depend on the data of P46, not on assuming only `b≥1000`.

## Pass C1: count for a fixed lattice

P51:8234–8613 was read in full, together with the dependencies of separation and cell P51:2569–2581, 6483–6595. **Verdict on the counting mechanism: (a), with the ambient data of nearness and cell declared.** The reduction of terms to those data remains an obligation distinct from the complete second moment theorem.

The convention in P51:8241–8251 is explicitly conjugate-linear in the first variable. Hence `h(υ,·)` is indeed linear and the projective lifting of Step 2 does not have the supposed failure of conjugation that reading it under Cv1 would produce.

- Step 0: equality of frames modulo moves leads to `R_0`, then the fixed label gives equal reduction; `K_R=K_U⋊K_H` and free level give the same class and the same chosen double coset.
- Step 1: integral packing of `Z` and the bound of its minors leave `≤b^{270n³f}` values; the moduli `Mδ` and `Mδ barδ` have norm `≤b^{2n³f}`.
- Step 2: `L′` is projective (Dedekind), so the map to the quotient lifts. The cokernel of the hermitian dual has order `disc(L′)^2`; colouring the ρ coordinates costs `≤b^{2n³ρf}`. The moves equalise the products with `L′`.
- Step 3: the difference of the middle parts belongs to `L_c∩(EL′)^⊥`, of rank l. Colouring modulo `Mδ` costs `≤b^{2n⁴lf}`. The adjugate of Y permits integral moves. The shared columns are zero; the exceptional column has squared norm `≤4/N<1` at all the places. Integrality and positivity force it to zero.
- Step 4: the shared vectors are fixed by the moves. Their coefficients are bounded using the quantitative independence of the boxed frame; the written exponent `180n²−73n−23` is smaller than `182n²`. Packing gives `≤b^{366n⁴f}`.
- Step 5: after colouring the part A modulo `Mδ barδ`, an integral and skew S is constructed by the explicit formula of P51:8590–8603. Multiplying by P one obtains `SP=δ barδ Θ`; there is no division by 2. The corresponding move identifies the frames and Step 0 concludes uniqueness. The sum of exponents is smaller than `2000n⁶(l+1)f`.

`pbc:moves` was verified by expanding unitarity: `W+W*=MG`, so that the linear and quadratic parts cancel; `ν³=0` gives an integral inverse and level congruence. `pbc:shared` is verified by Y and the form of `f`; `ppi:cell` uses positivity of X_0 and the climbing argument by means of rational characters. The Eichler identity requires the integral element of trace one already declared for the ambient field. The existence of such an element is not being asserted for an arbitrary CM field ramified at 2.

**Next global obligation:** these closures remove S, C1 and C2 from the pending front. To certify the total second moment it remains to reconstruct the use of the pairs of terms in `ppi:G`/`G′` and their intersection indices, and to verify the spectral contribution/multiplicities (which is not a consequence of C1/C2).

## Pass G′ and coverage of pairs

P51:7604–8206 read in full, including `pbg:climbp`, and collated with `pbe:link` (2838–2904) and `pbe:rank/pairs/two/XL1` (2941–3045).

**G′: mechanism proved for the declared data.** The chain of indices is real, not a substitution of an index by a determinant:

1. In the unimodular quotient by `I=A∩γA`, Jacobi with two borders gives exactly `d(L¹_γ)·ι=μ(γ)`; here it is applied with `c=N`, real positive. The sublattices `L_1⊂L_2⊂L_3⊂L_4` make `i_γ`, `i′_γ` and `t(γ)` divide the three successive indices. Their product divides ι, so that no index is cancelled improperly.
2. The homomorphism to the lattice of rows modulo M has rank j′ and kernel contained in `L⁺_γ`; its cost is `M^{2j′f}`.
3. The orthogonal decomposition into common part, part seen by the two functionals z and complement gives a product of discriminants. The image of the common part is only included in `C_γ`; the inequality of discriminants is used in the correct direction.
4. In `pbg:climbp` the role of the two conjugate places was verified: the lifted coordinates are supported at one place and their conjugates at the other. This produces distinct transvection matrices without introducing the false residual positivity. The equality of characters for every r forces a congruence by duality with the different. `pbg:meet` makes the determinant divisible by each distinct conjugate prime, with total factor `mn(s)`.
5. The linking form between the two complements is non-degenerate and takes values in `M O_E`: both terms are in the same block. Gram's Cauchy–Schwarz, applied after dividing a lattice by M, and `||1−u||≤2`, give `1≤(2/M)^{2if}d(L_y)d(L′_y)`.
6. For the common index, `v∈C_γ` produces `w=−M^{-1}(γ′γ^{-1}−1)y∈Λ∩(A+γ′A)`. This proves the inclusion of images that allows `pbg:indexmap` to be applied; the index divides `t(γ′)`, with neither irreducibility nor saturation assumed. Multiplying the two cuts and the bound of the complements gives G′ exactly.

**Remark on a statement:** `pbg:jacobi` P51:7693 allows an arbitrary `c∈O_E` to be written although it calls `h+c^{-1}Σbar(h(p_i,x))h(p_i,y)` hermitian. That form is hermitian only for c fixed by conjugation (or zero perturbation). The identity of determinants is algebraic and remains valid; all the applications here use `c=N>0`. It is advisable to correct the hypothesis of that lemma. It is not a break in G′ nor does it require altering its bounds.

**Coverage of all the pairs:** under the size bound (S) of `pbs:S`, the complete combinatorial part is now proved. G gives `18i≤n³`; the dimension of the common space gives `l≤i+1`, or `l≤i` in the degenerate case. Therefore C2 covers every pair. If i=0, both links are equal and both are degenerate or both non-degenerate. This divides exhaustively into: equal non-degenerate links, equal degenerate links, and different links (i≥1). The second go into the error with `D=β_*^{-16}D_id`; the third use the saving `(M/2)^{if}` and the bound `D_main≤(M/b⁶)^{kf}D_id`. No intermediate range remains uncounted.

The bound of `pbe:pairs` is obtained by summing over l and costs `n³+1≤β_*`. The pairs in each fibre `(label,L_{γγ′})` are at most the square of C1; this overcounts pairs of distinct classes, which only increases the bound. Each real pair determines its block and its stable pieces, so that the sums of `pbe:XL1` omit no multiplicities and need no further factor for the number of classes.

**Precise pending item:** the preceding coverage is conditional only on the analytic bound `pbs:S` and on the sizes `pb:sizes`. The audit continues with `pbs:S`/`pbo:O1`, the local systems that feed the iterated Poisson and the spectral equality that fixes the main constant.

## Analytic size: progress and a new local failure

The sections on weighted Schur P51:9182–9707 were reconstructed: projection of a negative semidefinite space to a negative definite one, determinant of volume, triangular bases by Cholesky, Ostrowski–Taussky and Hua's integral. The choice of the last column of a lower triangular matrix is used correctly to leave the last vector fixed. The Jacobian of Hua is `|det S|^{2k}`, and the loss `π^k/k!≤1` requires k≥7, which is satisfied. Colouring the module of rows costs `i_γ^k`; the shifts are integrated over a fundamental domain of volume ≥1. This last point is justified because the ambient field does contain Q(i), P46:3354. No such assertion is needed for a general CM field.

The packing of frames controls the multiplicity within each colour; the two Schur inequalities, one for γ and another for γ^{-1}, make `i_γi′_γ` appear with the correct exponent. The argument covers the degenerate cells and the part of the open cell where `Nm(g)≤N^f μ`. The other part uses O1. There is no gap of range between the two.

In O1 the explicit section, the GF normalisation, the adding of vectors, the mean measure, unfolding, Sobolev of dimension `2n²`, the application of Schur and the tensorisation (P51:10050–10590) were reconstructed. The GF factor is `V(r)/2^r`, obtained by the matrix Gaussian integral; adding the isotropic duals costs `2^{-ρ}`, without another factor for off-diagonal entries. The final product gives exactly `c_G`, not an unknown factor.

**Literal failure P51:10499–10500 (`pbo:tube`):** the dilation `β→tβ`, `σ→t²σ` multiplies the measure by `t^{2ρk+2ρ²}`, not by `t^{2ρk+ρ²}`. The text calls Q the real dimension and uses it as homogeneous dimension. Minimal model: ρ=1, β∈C^k and σ∈iR; the Jacobian is `t^{2k+2}`.

**Repair checked without changing the bound:** define `Q=2ρk+2ρ²` throughout the tube argument. `Q≤r²/2` is kept because `r=k+2ρ+1`, and the chosen radius `R_tube=Q²(T²+1)²` still gives `||vy||≤T^9≤T^10`. The quotient of volumes becomes correctly `(1+1/Q)^Q≤e<3`. Thus exactly the factor 3 and the exponent `10^5 n^4` of O1 survive. The papers were not corrected.

The part of O1 based on Bessel pairs is reconstructed after this repair. **Pending dependencies:** check externally the lowest K-type input and the Flensted–Jensen formula P49:Theorem 3.17, and audit DS4 (the quantitative positivity of the Bessel period). DS1(i,ii) was reconstructed by Schur and DS3 P51:6124–6205 by Casimir, local Lipschitz and packing of balls; DS2 P51:6054–6123 is correct conditional on that explicit formula. The exact formal degree depends on `pbr:degree`, which is coordinated with the main review.

## DS4 and explicit formula of P49

DS4, P51:6712–7577, was read in full. Its argument was reconstructed **conditional on the FJ formula and on the identity of the K-type**:

- The scale `κ_τ=Mτ(varpi)/(2πi)` absorbs exactly the additive character; inverting its sign is carried out by a diagonal isometry of order 2 that preserves Haar.
- The interpolation residues at the integer nodes μ_i produce a frame with the prescribed Gram; Witt gives the stationary position. The length is bounded by Gram–Schmidt using also the vectors of index up to 2ρ, so that control of the dual vectors is not lost.
- The expansion of a minor has remainder uniform in dimension by the Frobenius norm. On scaling only the parts that cross the projection, the remainder is an even holomorphic function; Schwarz improves `O(δ³)` to `400δζ²`. The step `pbp:minorconj` compares the conjugate projections and keeps the error `10³δ(x²+κ²)`.
- FJ and the independence of the block diagonal factor eliminate the unipotent factors. The weight of compact minors satisfies `|m_Λ(k)|²≤exp(−Q_Λ(k)/2)`, and `d_Λ≤e^{2T}` absorbs the complement of the Gaussian region. The Gaussian form gives a cone with error `12e^{-100T}`.
- The stationary position also allows one to localise modulo `U(k−1)`: the rows and columns outside X are controlled by the non-compact part. The equality of traces passes to logarithms by induction on powers. This justifies the phase, not only its first-order derivative.
- The combination of uniform error and decay gives `|θ|−2Re θ≤6EG`. Packing of the small ball in the large one, the local lower limit `|c|≥1/2` and the monomial coefficient `h_kk^a` give `vol(B_y)≤b^{60(r+k)²}|∫θ|` with the written exponent.

**P49 `pco:FJ`, 1848–2271:** read: products of minors, flag densities, independence of the block factor, K behaviour, Casimir, decay and identification. The reductions up to `pco:rigid` are reconstructed. In particular the invariance of the density uses the real modulus `|b^{2ρ_c}|²`; the holomorphic polarisation separates the two variables and proves constancy, so that the polar decomposition is not being gratuitously replaced by a holomorphic one. The Casimir acts with `|μ|²−2<μ,ρ>=|λ|²−|ρ|²`. The integrability uses exponent h>n(n−1), satisfied by h≥n²+1. The rigidity is left to the P49 front (D1–D3), explicitly coordinated.

**Local failure of order, P49:2250–2251:** `∫bar(F(xh))F(gh)dh` is identified with `<R(x)F,R(g)F>`, although the declared operator is `R(x)F(h)=F(hx)`. The change of order is not justified in a non-commutative group. **Exact direct repair:** the preceding line already gives `F(g)=∫e(h)F(gh)dh`. Substituting `x=gh` and using `e(h)=d·bar(c(h))=d·c(h^{-1})` gives immediately `F(g)=d∫F(x)c(x^{-1}g)dx`. The problematic double integral is omitted; its conclusion and Steps 2–4 remain with the same constant. The calculation does not need centrality of F.

Therefore no new obstruction to FJ was found after this repair: the remaining substantial obligation is exactly the spectral rigidity D1–D3, which is verified on the P49 front. The main review confirmed separately the formal degree `pbr:degree` of P51 conditional on those same inputs.

## Closure of spectral inputs and progress on local masses

The P49 front checked the external inputs against primary sources: Atiyah–Schmid (1977), Theorem 8.5, p. 42, establishes multiplicity one of the minimal K-type `λ+ρ_n−ρ_c` and the form of the remaining types; Vogan–Zuckerman (1984), Theorem 1.4, p. 54, provides the unitary uniqueness by Casimir and the cohomological K-type, and §§5.3–5.6, pp. 74–75, justify the transcription of D3(c). Source consulted by that front: https://www.math.utah.edu/~ptrapa/math-library/schmid/atiyah-schmid.pdf . With that coordinated check, the pending spectral dependency of FJ and DS is closed, after the local repair indicated above. The main review also reconstructed `pbr:basic–degree`, P51:5199–5833, including the exact constant of formal degree. This external check is not attributed to a duplicate reading in this review.

**Global reduction reconstructed:** P51:1483–1535, amplitudes → E1–E3. The use of `pb:basic` after E1 is not circular: it only requires E1 for `β(s)≤2 dim X`. For E2 all the scalar cosets and their complement are separated; their contributions are respectively ≤T/4 and ≤T/2. For E3 the opening excludes all the scalar cosets, even R; thus the induced term really disappears. One uses `D_id≤b^{-11kf}D_main≤b^{-6k#A}D_main`. All the square-root errors keep the final factor `1+4b^{-4}`.

**Real mass reconstructed:** P52:1072–1183 with H0–H5 in 909–924. The L² comparison between the vector and its cut, integrated over the ball, costs `b^{6300nr³}` and is absorbed by `f_W≥4000n`, the explicit hypothesis H5. The contribution without cut is exactly `c λ³ (#I)²/deg`, which reduces to `(vol U(k)/vol U(r))λ/deg≤1/deg`. The tail uses the saving of remote position; the main constant is not replaced by an implicit constant. The shared lemmas on floors/gauges that produce those savings remain as obligations of the local system.

**Finite mass reconstructed conditional on those shared lemmas:** reading of P52:3370–3840 and 4010–4222. The unfolding identity of `pff:unfold` respects the order `uyx(uy)^{-1}` and produces exactly the factor λ. Hence `m(Z)=λ²∫|k₀|²`; on K(M) the inner integral is `vol Z`, by normality, giving the main part `vol(Z)² vol(K(M))`. In the estimate of the norm of the vector, although several coordinates may be non-zero, all of them represent the same coset `U K(M) g`: no factor of the number of coordinates is lost in the support mass `vol(K(M))/λ`.

The explicit construction of the hyperbolic basis in `pff:L1` uses norm −1 and trace 1 in the unramified extension, also in residue characteristic 2; its determinant is the unit −c. The lower bound for the volume of the upper floor is obtained through the unit coefficient b in `a u+b u′+y′`, integral transport to z and the surjective trace map, whose pushforward of normalised Haar is normalised Haar. Thus no lost factor 2 appears.

`pff:oneplace` keeps the exact index `p₀^r−1` of a **non-zero vector**, not a line. For `t=k−10¹⁰n⁴` and `k≥3·10¹⁰n⁴`, one verifies `6k≤9t`; the index absorbs `B^{t+1}`, B=b⁹. The mass estimate and the lower bound for K give precisely the saving `b^{-6k}`. On multiplying conjugate places, the change of Haar normalisation costs λ³ in m and λ in volume, which cancel on both sides: total saving `b^{-6k#A}` with main constant 1. The strong hypotheses are satisfied in the ambient data; the result is not validated here for general parameters outside them.

**Remaining front delimited:** complete reading and reconstruction of the shared lemmas on floors (P52:376–878 and 1183–3336), and of the finite decay (3841–4009), to discharge the dependencies of mass and local system. It is not enough that the final constants fit: that front remains pending. E4 of P51 has in addition the combinatorial input `pbm:Phi`; its final application 3396–3414 is arithmetically correct, but that input still requires specific reconstruction.

## Floors and descent: detailed partial closure

P52:376–878 and 1183–1756 reconstructed: measure of the quadric, charts, Weyl invariance, inverse weight, separation of frames, cut at the first deep vector, summation of shells and exact descent. The density of the quadric keeps `κ_C=2`, `κ_T=1`; the majorant `mod(t)^{-1/2}` is locally integrable, also in the product of finite fields. The Heisenberg section costs exactly `mod(c^{-1})^{1/2}` after cancelling the Jacobian `mod(c)^{d_a}`. The step of block disintegration eliminates only a null set common to a countable family of bounds, sufficient for the later integrals.

Weyl invariance is not assumed for the singular measure of floors: it is proved by completing with Haar of the upper group and comparing integrals of invariant functions. The separation crosses the weights before Cauchy–Schwarz and uses `w_p^{-1}=w_{bar p}`, preserving the same product of moduli. The cut at the first deep vector is justified by descending induction; for j=0 both pivots coincide and give the double exponent, used in the finite mass. The summation of shells keeps a geometric factor 2, absorbed explicitly.

The descent 1693–1756 compares laws by right translation of a floor over its quotient; it does not require that the measure of the floor itself be Haar. The change `τ→w_c^{-1}nσ` leads exactly to `Π(x;w w_c;nσg)` and to the weight `mod(c)^{d_a}`. The hypothesis of integrability of the lower floor controls by Tonelli the expanded integral before Fubini; there is no formal exchange of conditional integrals.

**Additional local erratum:** P52:1810, convention (iii), says that `U_(<l)` fixes the e_b for b<l. In general it only preserves their flag and acts unitriangularly: with l=2, `N_0` can send e₁ to e₁+a e₀. The following sentence describes that behaviour correctly, and the effective use in the proofs read is triviality on `Y^(l)` and congruence modulo the lower span, which do hold. Replacing “fixes” by “acts unitriangularly on” repairs this line without changing bound or identity.

Pending after this pass: proofs of one-frame/gains by frequency and two heads (from 1757), verification of the real and finite gauges that feed G4/G5, and finite decay. The preceding results are reconstructed conditionally on those explicitly identified inputs.

## Closure of the real system and of the three shared theorems

P52:1757–3336 read and reconstructed in full. The dependencies one-frame, frequency and two heads, and the real gauges, of the preceding passes are now discharged.

The Plancherel inequality is proved by Gaussian regularisation and Fatou, with constant `P=π²` for the character `exp(c−bar c)`. On the quadric **two disjoint blocks** are used: one eliminates the dependence of its fibre on y by means of Cauchy–Schwarz, and the other eliminates the fibre of v; the remaining phase permits Plancherel on X′. Fourier is not incorrectly applied to a singular measure. Parseval on Heisenberg keeps `mod(ξu)` and `c_a(u)`. The climbing uses `ξ=M^{-1},u=M`, so that the modulus of the level is cancelled exactly in that phase.

In one-frame the change of Weyl-ratio produces `J=∏mod(p_a/q_a)^{d_a+1}`. On combining with the density and the weights one obtains **exactly** `κ_j²DJ=mod((q₀⋯q_{j−1})^{-1})≤Λ`; no arbitrary product of heights of p remains. The gain by two heads uses `M^{-1}(p_i/q_i−1)=−ξp_i` and then `u=p_i^{-1}`, so that no factor p_i is lost in the frequency. All the integrations of positive functions are carried out with Tonelli before the applications of Cauchy–Schwarz.

Real G5 is verified by choosing a subspace of dimension s+1 on which **both** isometries preserve the Euclidean norm: at most 3n equations are imposed and `rank X′=s+3n+1` is used. The function `φ=36/q` has integrable s-th power, because the radial law has density proportional to `t^s`; this avoids the divergence that there would be in dimension s. The factorial factor absorbs the exponential cost and gives the declared exponent `99n(i+1)`.

The Haar normalisation reduces to the Gram fibres already reconstructed in P51: each hyperbolic pair costs 1/4, z costs 1/2, and the compact block costs `vol U(k)/2^k`. With r=k+2ρ+1 all the factors 2 cancel. Only the Haar inequality that is proved is needed; the main constant of mass remains ≤1/deg. The upper floor is identified with the Gram of orbitals by means of `σ=h₁σ_c h₂`, a unitary operator independent of the head, and the equality `N(p^c)N(q^c)=c λ² h(c)κ_ρ(p,q)` keeps the exact normalisation.

H1–H5 are collated in 3252–3307: H2 is deduced with equality from the reproduction B7 and Schur, H3 from the product of formal degree, H4 from DS3, H5 from S7(b) of P46. After the local repairs already recorded in FJ and O1, the real system R is reconstructed for the ambient data, subject to the construction of the Bessel vectors of P51 and to the admissible data of P46 (this sentence is not turned into an independent certification of those constructions).

**Next obligation:** finish finite decay/gauge (P52:3841–4009 and its dependencies in §6), then the input E4/Phi and the Bessel/global construction if they are not covered by another front.

## Closure of F: finite gauge, decay and upper floor

P52:3841–4009 and 5097–5227 reconstructed; with the dependencies of §6 already reconstructed in the first passes, this discharges the finite local front F.

Finite G5 uses Smith over each DVR to impose 3ρ equations without denominators on the basis of the kernel. The vectors obtained are fixed by the conjugate unipotent; the factor k∈K(M) produces the congruence of nearness. The content function satisfies its integral by a sum over ideals, with `d−s=m′+4>0`; exactly `|β|^{-a-(d−s)}` is kept. G4 uses fibres of a unimodular form of rank 2m′+2 and the zeta bound, without additional restriction at 2.

The upper floor 3841–3937 was reconstructed with explicit order of multiplication: on putting `l=(h′τ)(hσ)^{-1}`, the phase is `ω(l^{-1})`, and the orbital is `O_p(l)`. Therefore the final character is `ψ_T(ξt)`, without extra conjugation. Tonelli applied first to the absolute value and the compact support of orbitals justify Fubini even when H_T is not compact. The coarea maintains `|π_N|_T^{-1}`. Positivity and continuity are deduced from Gram and from the continuous fibres, not from a formal identification of distributions.

For the decay, `α=M bar(βγ)βγ` controls simultaneously inverses of the partial products and of the entries. In the frequency case, one chooses component by component η generating `(ξ,α^{200n²})`; the equality of characters on the support allows η to be used. In the two heads case one takes η=ξ. The saving decomposes into the power `n(ξ)^{t/2}` and the denominator `den(ξ)^{-6}`, paying `Λ^{1200n²}`. Here `n(ξ)=|ξ|_T^{-1}` is the inverse modulus, **not** the norm of a numerator ideal; with that definition, its multiplicativity used at 3996 is correct. `4E≤10¹⁰n⁴≤K` discharges the whole cost onto the weights of F.

**Status of P52:** its systems R/F and step S have been reconstructed for the ambient data, with the correction of direction of the cutoff 4364–4365 and the unitriangular erratum 1810 already recorded. This is a closure of the local mechanisms and their constants, not an assertion that the original text is literally correct without those corrections. The dependency that is now transferred to P51 is the Bessel/global construction and E4/Phi; the numerical/admissible data are controlled on the P46 front.

## E4 and Bessel/Poincaré construction

P51:771–821, 3139–3414 reconstructed: positivity of the intersection function as a Gram matrix; exact recursion on removing a hyperbolic pair (open cell `NwLN` with bijective parametrisation); recursion on fixing the first vector (two factors `q^{r−1}`, one by orthogonality of characters and another by N); bound of intersection of subspaces by means of Gaussian binomials; and inequality of singular minors by Fourier tensorised with the vectors of positive type. The residual exponent `j²−m/2≤−2` and the recurrence `(1−4/q)Φ_j≤Φ_{j−1}+128(ρ+1)/q²` are verified. The lower bound 1 is justified directly by `pbm:pos(c)` and the value 1 of the induced function at the identity. E4≤2 is closed in the ambient range.

P51:2229–2695 reconstructed: the length is continuous by the two inequalities with g and g^{-1}; Gram–Schmidt is invariant under unitriangular modifications. The covering of R has real dimension 2r² and exponent 4r², absorbed by 9r². The average that constructs W converges absolutely, is reproduced by e, and its L² norm is exactly the period divided by deg. The positivity of the period is deduced from that identity; DS4 contributes its lower limit. The cutoff keeps continuity/type H and its L² error is controlled with the written exponent.

In the global count `pbe:count`, the reduction of representatives uses integral/Eichler transvections with trace 1, also at level N; the order of reduction of the Gram–Schmidt coefficients is triangular. Two classes with the same frame differ by U: the H part disappears by free level, previously checked. For nearby frames, integrality in all the conjugates forces equality of the Grams, positivity of X₀ eliminates its component, and the largest non-zero index of the isotropic component is eliminated by the scaled length. Packing in dimension 2nrf gives the count uniform in y, not an assertion of term-by-term uniformity. Thus the Poincaré series is bounded, reproduced and continuous by L¹ continuity of translations of the kernel.

The final unfolding B4 keeps `c_W=vol(R_f∩J)/vol(J) ·∏deg_τ/c₀τ`. The conjugation is handled by the duality between W and its contragredient; on substituting s by s^{-1} there appears precisely the local average constructed. No additional obstruction to B1–B7 was found under DS and the declared data. The finite dimension of A_z is cited from P49 and is not replaced by the mere convergence of the series.

## Closure of the two global normalisations

P51:1573–2010 reconstructed in full: the row functionals and the central imaginary parts are ordered triangularly; translation by a low element is additive in the following coordinate. The Eichler transvections reach all the permitted integral rows. The existence of an element of trace 1 avoids introducing 1/2 even at 2. The fundamental box is obtained successively without supposing that all the coordinates are homomorphisms simultaneously. The triangular translation matrix has Jacobian 1. Inverting the box converts right cosets into left ones because U is unimodular.

The covolumes are verified: the duality of rows cancels the factor of the level N with the scaling of z; the centre uses `O_E^−=i O_{E⁺}` (i is a unit of the ambient field), so that its covolume is `|D_E|^{1/4}`. The sums of dimensions are `Σm_a=ρ(ρ+k)` and `Σ(2m_a+1)=ρ(2k+2ρ+1)`; the remaining scalings are `N^{−kf}Λ^{−1}`. This proves the exact value ν_* for each class c under the data of the paper.

The ratio of masses 1336–1357 was checked against the primary source [Gan–Hanke–Yu, equations (4.2),(4.3), Propositions 4.4–4.5](https://web.math.princeton.edu/~jonhanke/Web-02/Mass-Formula-of-Shimura/shimura-mass.pdf). The group is totally definite; the standard unimodular lattice is maximal and its stabiliser hyperspecial at the unramified places. The norm of units of an unramified extension is surjective, so that the unit determinant does not introduce exceptional places. The source gives `Mass_l=2^{−lf}·2·∏_{j≤l}|L(1−j,χ^j)|`; the factor 2 cancels between ranks. The functional equation with trivial relative conductor gives the factor `2^f` per quotient, which cancels `2^{−f}`. Thus exactly the declared quotient is obtained, without an undetermined constant depending on the rank.

## Final assembly of the second moment

P51:837–998 and 1027–1110 reconstructed. The operator β is positive; applying the singular estimate to the vector that maximises its quadratic form controls the terms outside the open cell. A pair is open if there exists a Weyl element for which all the required principal minors are non-zero; if none exists, the singular control is applied to the fixed Weyl element. The alternatives E2/E3 cover respectively all the fixed blocks and at least one non-fixed. The accumulated margin is the written `1+9b^{−4}`. No absent range of pairs was detected.

The comparison with the original lattice uses a unitary conjugation of P and of its adjoint, not literal equality of the two lattices; it keeps exactly the Hilbert–Schmidt norm. The estimate of bad labels and the passage to the cuspidal part are reconstructed as algebraic arguments conditional on Green's description of the cuspidal characters of the finite linear group; that external classification was not reproved in this audit. Multiplicities and formal degree are referred to the ledger MULTIPLICITIES and to the independent review of the inputs of P49.

**Updated verdict by questions:** (1) the written proof requires the local repairs recorded (FJ of 49 and homogeneous exponent O1 of 51); the assembly was reconstructed with exact constant and uniformity under the ambient and representation inputs indicated. (2) **(b) literal**, first failure of the limit at P52:4364–4365, repairable by inverting the cutoff without altering constants; the fibres, Siegel and Poisson were reconstructed. (3) **(b) literal** in the homogeneous exponent of P51:10499–10500; the repair keeps the final bound and the exhaustive count was reconstructed. (4) review of the independent front MULTIPLICITIES, including its local erratum on global uniformity of a series. These failures of steps are not counterexamples to the final statement of second moment nor to RH.
