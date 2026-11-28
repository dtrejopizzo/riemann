> **V1: historical record, revised in V2.** Do not apply its character objections or its propagation statuses to the corrected manuscripts without consulting the [V2 status](../review-v2/STATUS.md). The specialised cancellation of characters corrects the global impact attributed in V1; the remaining results are being consolidated.

# Auxcore of P53, bounded descent and height of P54

Audit of the local text `main.tex`; line references are to the audited copy. The papers were not edited. Verdicts: (a) correct in the stated scope; (b) argument incorrect as written; (c) step not verified. A correct conditional deduction does not turn its pending premises into certified theorems.

## Result and scope

- **P54 `ppe:bdd`, 4383–4411: (a)**, with R2/R3 and the mean lemma of P53 and the vanishing `ppe:zero` as audited inputs. The growth of the theta distribution is cancelled by short isotropic vectors. Continuity of theta evaluation for the Hilbert norm alone is not used.
- **P54 `psu:arch`, 9217–9253: (a) as a deduction from CL, `psu:normL`, `psu:I` and the explicit bounds**. The height multiplier and the cancellation of the exact constants were checked. This argument does not cite `pc:auxcore` directly; it must not be confused with the production of integral lifts by the second grid. The certification of the inputs is referred to COVOLUME/THETA and the other ledgers.
- **P53 `pc:auxcore`, 1616–1631: not proved unconditionally by this chain.** The deduction 9436–9497 is correct conditionally on its propositions. The square-exchange propositions used in the turns depend on `pcx:X`, whose proof contains the character failure of `pcu:product` documented in ERROR-53-CHARACTERS. It is **(b) for the proof as presented**, not a counterexample to the statement of auxcore. The existence of a global repair that preserves the periods, their non-vanishing and their constants remains **(c)**.
- Two additional **local (b)** errors, in `pgq:slice` and `pgk:lat(c)`, admit the following complete repairs; both preserve the constants. They are not new global obstructions.

## 1. Two local errors with proved repair

### 1.1 Matrix order in `pgq:slice`

P53:13740–13742 identifies `rr₀⁻¹` with the product `(g(r₀⊕1))⁻¹g(r⊕1)`. This product is `(r₀⁻¹r)⊕1`. The equality as written is not a valid rule for matrices; the factors of an indefinite unitary group cannot be permuted.

Repair: keep the minimiser r₀ and write

`||r₀⁻¹r|| ≤ ||(g(r₀⊕1))⁻¹|| · ||g(r⊕1)|| = t₀ ||g(r⊕1)|| ≤ ||g(r⊕1)||²`.

The function attains its minimum by the coercivity bound that opens the proof; in this unitary group the norm of an element and that of its inverse coincide. Hence

`∫ ||g(r⊕1)||⁻ˢ dr ≤ ∫ ||r₀⁻¹r||⁻ˢ/² dr = ∫ ||r||⁻ˢ/² dr ≤ 2·16^(n²)Vτ`.

The equality of integrals uses **left** Haar measure. It changes neither the fixed Haar measure (the group is unimodular) nor the minimal exponent s≥16n². `pgq:balls` requires s/2≥8n², which is satisfied exactly. The fix preserves the domination needed by the deep period.

### 1.2 Finite determinant in `pgk:lat(c)`

P53:14549–14551 asserts that, because it preserves the unimodular form, `det x_f` is a unit at every finite place. This is false at a split place v of F=E⁺: for U(1)(F_v), the element `(π,π⁻¹)` satisfies the unitary condition but neither of those two components has valuation zero.

Repair: from `det x · overline(det x)=1` one deduces that the **total finite modulus** is one. At non-split places the valuation is zero; at the two places above a split one, the opposite valuations have equal residual norms, and their moduli cancel. Thus `x_f Ô_E^n` has the same adelic volume as `Ô_E^n`. The subsequent covolume argument is valid. The archimedean Jacobian is `Πτ |det Pτ|⁻² |det xτ|⁻²`; the second factor is one and the first is the absolute norm of the unit `det H`, also one. What remains is exactly `(2⁻ᶠ |D_E|^(1/2))^n`. No later rounding or height bound is altered.

## 2. Reconstruction of `ppe:bdd`

P54:4364–4411 was collated with P53 R2/R3 (2292–2415) and `pcx:mean` (2519–2577).

1. The theta mean over the isotropic subspace Z is theta₀. `ppe:zero` annihilates the integral of that term against Y, so that theta may be replaced by theta−theta₀. The form Y and the finite datum are fixed.
2. R2 gives the growth `ht(g)^A` in a moment norm; A can be chosen sufficiently large, in particular for the thresholds of the mean lemma. A polynomial Fock vector belongs to all those moment spaces. The bound does not claim that theta is a bounded functional on the Hilbert space.
3. For ht(g)>2, R3 provides a non-zero rational isotropic vector d of length ≤2/ht(g). Witt allows its line to be carried to Ee by a rational γ. The lattice identity `Λ_(γg)=γΛ_g` is isometric, so **ht(γg)=ht(g)**; no uncontrolled height of γ appears.
4. Since V is definite, the quotient of U(V) is compact. Having chosen a compact set of representatives h, there exists an integer N that makes all the `Nh⁻¹d_i` simultaneously integral at the finite places. The vectors `z_i=N d_i〈·,γd〉` belong to the required lattice and span Z over E; their lengths are ≤C/ht(g), uniformly in h.
5. In `pcx:mean` one takes l=A and δ=C/ht(g). Its factor δ^A cancels ht(g)^A exactly. The other constants depend on the fixed datum, not on g. The region ht(g)≤2 is covered directly by R2. Finally the bound is integrated over the compact quotient against Y.

This proves global boundedness, which is what the later application requires. A constant uniform over all the ranks/weights of the paper is not needed. If one works with an equivalent height instead of the convention ht(h)=1, compactness absorbs its maximum and the same conclusion holds.

## 3. Reconstruction of the height `psu:arch`

Lines 9180–9253 and the declared inputs were collated. For p=(ν,z), one takes the flat pair q=(υ⁻ᶻ,z) of the **same rank z** and

`H=I_q(1)/||φ_(p,1)||²`, `h_l=0`.

The product H||φ_p||²=I_q(1) is integral at all places by `psu:I(b)`. Thus the finite part of the height is zero; there is no hidden infinite sum of losses.

For a conjugate σ, the case of σ fixing K suffices: K is imaginary quadratic and composing with complex conjugation preserves the absolute value. CL applied to p and q introduces the same factor `a_σ(z)`, because z coincides; `psu:normL` introduces the same B(z). Both cancel in the quotient. The degrees lτ are permuted, so that what remains is exactly

`Στ (log(lτ!)+lτ log(M/Ω)) = Στ s∞(lτ)`.

The flat degree is zero and its d is one; the term `−log d_(p^σ)` is non-positive. The two Euler logarithms contribute at most 2f. Since M/Ω≥1 and lτ≥κ(τ), one obtains

`log|σH| ≤ log N_z +8fz log M +2f −Στ s∞(κ(τ)) ≤ budget−Στ s∞(κ(τ))`.

The last two inequalities are exactly (N5), (N6). The CM period is not replaced by an estimate, nor is an archimedean factor lost by taking absolute values. The scope is the conditional deduction indicated above, not a new proof of CL/Rallis.

## 4. Auxcore: pieces actually reconstructed

### 4.1 Final deduction, indices and delta

Lines 9057–9707, 9900–10106 and 11540–11795 were reconstructed; in addition the diagonal closure 10640–10715 and the last path 11998–12065 were read. The combinatorial transformation uses m² turns. The non-diagonal turns have bound factor one; the diagonal ones pay V. The final bound is `L=V^(m²) E^(2m)`.

The principal level J° is NOT identified with the parabolic level Jθ. The index of the former is `#GL_(r+mt)(R_m)` and the quotient of indices of the latter contains the orders of blocks and the unipotent radical; it is not a simple power of the norm. The proof 9390–9497 maintains this distinction and cancels the correct index in the period identity.

The delta forms are constructed at free level, which removes ambiguity of stabilisers; the archimedean Schur average produces the factor `1/dim λ′`. The identity obtained is

`〈v,(cθ/c1)ιθ(rφ)(x_f)〉du = β′ Λ(Ψθ;δ_(x_f,v),φ)`.

Choosing sβ′=h ε N₀, ε∈{0,1}, is valid even if β′=0: there is no division by zero. Integrality is verified by means of gauges, rational transfer to integral points over l, and integral duality with denominator h. For θ=1 one obtains

`||σ ι1(srφ)(x_f)||² ≤ Cdu h² exp(2(x^99+x^200)b²) B ≤ exp(2x^201 b²) B`.

The surjectivity of r uses the first transposition; it does not follow from the final estimate alone. That transposition has an exchange dependence indicated in 4.4.

### 4.2 Denominators, conjugates and short forms

Lines 13048–13575 and 14027–14389 were reconstructed. In the last path all the nodes are definite. The joint invariance of the path datum removes stabiliser denominators when the class sums are expanded. The jet factor d and the ramification factor `M_branch` give `N₀=M_branch d^(2m)≤exp(x^99 b²)`; the primes of Qθ are explicitly excluded. In the archimedean bound, the normalisation of averages divides by their cardinality, so that a group-size factor is not counted again. The bounds B1/B2/B3 cover jets, ramification and classes respectively, including the ranks up to 2n_m of this second grid.

For the short forms (9900–10106), the determinant exponents of each component may be negative. The construction of short bases is applied to the already twisted lattice x^(eτ); one and the same bound is not blindly raised to a negative exponent. The gauge computation transforms the determinant into that of an integral matrix. The evaluations at roots of unity are Zariski dense and span the representation; this justifies "spanned", without asserting that they constitute an integral basis. The norm of all the conjugates is controlled by the prescribed bounds on rank and number of boxes.

### 4.3 Non-vanishing of the deep period

Lines 13583–14026, 14395–14742, 14776–15052 and the coefficient estimates 15078–15420 were reconstructed. The scheme consists of cusp control C, reproduction Q and restriction S.

Q uses separation of neighbourhoods and a bound for the **total sum**, not the incorrect assertion of uniform convergence of tails for global g found in P51. C uses rounding in the dual lattice of the trace, short isotropic vectors and the unipotent radicals as written. The covolume correction of 1.2 suffices here. S uses a stationary point of the phase, located by the interlaced weights, and a Gaussian bound around it; the volume factor `Vτ` is preserved. The slice correction of 1.1 preserves the tail bound.

With D=b^(x^36), the separation and variation bounds give the contradiction scheme `S_sup≤S_sup/2`; it does not require the supremum to be attained. The use of sizes for Π/D≤1/20 and the descent of the exponent thresholds to those of the ball integrals were verified. The inputs on minimal types/discrete series are referred to the THETA/MULTIPLICITIES audits already carried out; they were not taken again as proved on the mere name of a theorem.

### 4.4 Where the global dependence persists

Lines 12604–13012 were reconstructed: the transpositions I/P use a second grid of even ranks and verify the signs of characters, the convergent range and the sum of errors for injectivity. However, their T1 uses `pcx:X` explicitly. The same holds for the square law that enters the turns of 4.1.

The character failure in P53:3359–3360 is not resolved by the characters having modulus one: the corresponding variable is integrated. The repair may change the period and its non-vanishing. For this reason it is not legitimate to conclude that auxcore is certified unconditionally merely because its bounds and its final deduction are in order.

## 5. Continuation: line inversion, diagonal turn and G1–G4

The reading and reconstruction of 10330–10639, 10728–11466 and 12065–12603 was completed. The pending reading recorded at the start of this batch is replaced by the following results; the global exchange obstruction is not modified.

**Line inversion:** the general case `pgx:line` uses data supported on `A=a_w O_w^n`, not on the unscaled integral matrices. The Fourier image of the vacuum lies in `B′=bar(α)_w O_w^n`; the fixed diagonal element has component `u_w=bar(α)_w/(α_w π^k)`, so that `u_w A′=π^(-k) B′`. The Fourier coefficient of the indicator of a coset is `γ q^(-kn)`; after the unitary dilation, its modulus is determined by norms: the input indicator has squared norm q^(-kn), whereas the sum of the q^(kn) output indicators, with coefficients of modulus one and disjoint supports, has squared norm one. Hence the local modulus is exactly q^(-kn/2), also when α is not a unit. On assembly one obtains `|c_line|²=C₀(Nm m)^(-n)` with C₀ independent of the twist. The character factor that appears on moving u is `β_(L′)(u)^(-1)`; here u is a fixed point, and absorbing its value of modulus one is indeed legitimate. Unlike the failure of `pcu:product`, it is not a character of a variable that is still being integrated.

**Seesaw and turn:** the double functional in `pgu:seesaw` is continuous in a moment norm, thanks to R2 and the rapid decay of both forms; Fubini has domination. The set of vectors whose image belongs to the line CΞ is closed for that topology (also when Ξ=0). The density of polynomials is applied in moments, not only in the Hilbert space. The turned data are the finite transform in the column of the line followed by the matching: the invariance is obtained by the change v→g_S v, and the determinant factors cancel using that opposite edges have the same character. The left-inverse condition is inherited from the block x₂; adding the row v′ does not destroy it. The sum has at most `(#R)^n≤(#R)^(2n_m)=V` terms. The decomposition into blocks `(S,y,v)` and `(S,x,v′)` is bijective, so that no multiplicative fibre is missing. The closure gives `c_jj=c⁰_jj/c′_line`, preserving the required modulus up to powers of the norm.

**G1/G2/G4:** the rank and sign formulas are verified by counting the negative stem coordinates. In particular N¹_(j,j+1)=N⁰_(j+1,j)=r+(2j+1)t and their negative signs coincide. Only spaces/groups/lattices are identified; the distinct types are not identified. G2 uses the floor/ceiling roundings of ranks of different parity and produces exactly β^c=1, α^r=υ. G4 uses u=bar(u₀)/u₀ and coincides with the element of the preceding general local computation.

**G3 and squares:** the extension of the matching from excess t to t±1 was verified: the half-integer classes, the chain of the new block, the change of sign of the stem and the distance of at least Δ/2−1/2. The distinct signs are separated by at least Δ−t; the ranks are ≤2n_m. The applications to harmonics, projections and types rest on the inputs of P49 already audited; they do not require keeping t odd in the local excess. In E2 the products of edge characters equal `ν⁻¹υ^M₀`: in the first grid floor+ceiling=M₀, in the second both ranks are even and their halves sum to M₀. The four orientations of E1 are verified with the explicit conjugation of types for the ascending edges. Passing from a form y₂ to an arbitrary functional l is valid because the images of point data fall in a space of fixed level and finite dimension, with positive definite Petersson product.

**Verdict of this continuation: (a) for the local deductions with the declared inputs.** No other failure was found in these blocks. The square law still depends on `ptr:square`/`pcx:X`; the correct computation of E2 does not repair the incorrect identity used inside its proof. The next global obligation continues to be to reconstruct that exchange with its characters and to verify the resulting periods again, not a pending reading of these three blocks.
