# Tribunal — Alain, severe referee Audit of `RH-PROOF-FULL.md` (chain E0→E4, CCM program). Lens: operator
theory, spectral realization, self-adjointness, renormalization `Â=A/ε₀`,
identification of the limit operator (IV.1), distinction H1 / Perron–Frobenius vs PSD. **Golden rule of the program:** a forced result is worse than an admitted gap.
No claim of a proof of RH. What follows attempts to *break* every ✅ and *close* every gap
that is not RH-equivalent. --- ## 0. Verdict by piece (table) | Piece | Verdict | Core |
|---|---|---|
| E0 (def. `QW`, Weil identity) | **SOLID with one caveat** | the *identity* `⟨ξ,QWξ⟩=Σ_ρ g(γ_ρ)conj(g(conj γ_ρ))` needs a qualifier |
| E1 (real-rootedness) | **GAP** | own proof open; depends on CCM Thm 1.1(iii) |
| H1 (PF structure) | **SOLID** (as structure) | correct after correction |
| H1′ (`QW` PSD) | **GAP = RH** | RH-equivalent, not unconditional |
| N0 | **SOLID** | |
| N1 | **SOLID\*** (modulo Boas) | |
| N2 | **SOLID** | |
| N3 | **SOLID\*** (modulo Boas/PL) | |
| Reduction (Thm 2) | **SOLID, modulo E1** | valid as a conditional implication |
| III (renormalization) | **GAP** (conditional) | (H-gap)+(H-lim)+(H-pos); (H-pos)=RH |
| N5b | **SOLID** | |
| N5c | **SOLID\*** (modulo E1 + axis-conv) | |
| IV.1 (limit operator) | **GAP** (not RH-hard) | closed part; see below |
| IV.2 ≡ §V | **GAP = RH** | RH-equivalent core; I do NOT touch it |
| E3 (Hurwitz) | **SOLID, modulo E1** | |
| E4 | **SOLID** | classical | I closed (rigorously or with an exact named residual): **(H-pos) reinterpreted**,
**part of IV.1** (parity/interlacing/compactness — already there; I add the argument
for why `n²` CANNOT be derived from the compact kernel, which *refutes* the optimistic
reading), and **(H-gap) γ>0 remains OPEN** — I explain why it is not a free gift from IV.1. --- ## 1. E0 — construction and the key identity **Verdict: SOLID, with an important caveat about the identity.** The definition of `QW` (Def 0.1) and the band-limited `ξ̂` (Def 0.2, Prop 0.3) are
correct: `sin(Ls/2)` cancels the poles `d_k`, Paley–Wiener gives type `L/2=logλ`,
reality on ℝ. That is impeccable. **Attempt to break the identity ⟨ξ,QWξ⟩ = Σ_ρ g(γ_ρ)conj(g(conj γ_ρ)).**
Here one must be severe. The claim "`QW` IS the Weil form on the zero-side" is
used twice as a pivot (H1′ and the IV.2 core). Let us examine what is true: 1. Weil's explicit formula is an *identity between two sides*: `(arch) − (arith) = (zero-side)`, i.e. `Σ_ρ g(γ_ρ)conj(g(conj γ_ρ))` **equals** `∫ g·ĝ·w_arch − Σ_n (Λ(n)/√n)(…)`. That the matrix `𝒲_{mn}` encodes the left side (arch − arith) is **definition** (Def 0.1) — that part is exact.
2. That this left side **equals** `Σ_ρ g(γ_ρ)conj(g(conj γ_ρ))` is the explicit formula, **classical and true**, for `g∈PW_Ω` of suitable support. **But there is a truncation caveat the document underplays.** The exact
Weil formula runs over **all** `ρ` and **all** primes. The finite matrix
truncates primes to `n'≤λ²`. The document claims "`A_λ = A_∞|_{E_λ}` exact (primes `>λ²`
do not contribute by support)". This is correct **only** because `g=ξ̂` has Fourier
support in `[−logλ, logλ]` and `log n' ≤ logλ² = 2logλ`... — wait: `log n'` for
`n'≤λ²` reaches up to `2logλ`, which is `L`, **the very edge** of the support of the
Fejér window, not its interior. The integrand `q_{mn}(y)` runs over `y∈[0,L]` and `log n'∈[0,2logλ]=[0,L]`.
So the truncation to `n'≤λ²` **is not due to strict support** but to the window
`(1−y/L)` that vanishes at `y=L`. Primes with `log n'` near `L` enter with weight
**nearly zero but not zero**. The claim "exact" is therefore **slightly
oversold**: it is exact in the limit, with an edge error controlled by the
Fejér window. This is benign (it is in fact the candid content of N5b), but
"exact" should read "exact up to the Fejér window tail at `y→L`". **E0 conclusion:** SOLID as a construction and as a Weil identity; correct
"exact" → "exact up to a window tail at the band edge". This caveat does not
damage anything downstream (it is reabsorbed in N5b), but a referee flags it. --- ## 2. E1 / H1 / H1′ **E1 — Verdict: GAP (candid, already flagged 🔧). I confirm the HIGH severity.** The counterexample `ξ=(−1,2,−1)`, `d=(−1,0,1)` → `f(s)=−2/(s³−s)`, zero real roots,
is **correct** and definitively kills the interlacing argument. I verified it:
`−1/(s+1)+2/s−1/(s−1)`, common denominator `s(s²−1)`:
numerator `= −s(s−1)+2(s²−1)−s(s+1) = −s²+s+2s²−2−s²−s = −2`. Exact. The vector is
even with one sign change and produces a secular function with no real roots. Interlacing **dead**. The claim that real-rootedness is nonetheless true rests entirely on
**CCM Thm 1.1(iii)** as a black box. It is legitimate to *cite it*, but then E1 is
not "proved by us". The document acknowledges this. **I cannot close E1** through
my lens without reproducing CCM or building the Hermite–Biehler proof from the
self-adjoint realization — and the latter **is not done and is genuinely
difficult** (the edge carrier `ω*=2πN/(2N+1)` near-Nyquist means the translation
"positivity of the envelope ⟹ HB of `ξ̂`" is not mechanical). E1 **GAP confirmed, not closable here**. Additional critical remark (through my lens): the document states that
real-rootedness "also holds for DH (RH-false)" empirically, and from this concludes
"it is not Perron–Frobenius, it is self-adjoint/HB". **Caution: this is a
double-edged weapon.** If the self-adjoint CCM realization gives real-rootedness
*unconditionally* (even for DH, without `Λ≥0`), then the real-rootedness of `ξ̂_{λ,N}`
**contains no information about RH** — it is a property of the *finite* object, not
of the limit. Fine. That is consistent: the RH content lies entirely in the
*convergence* `ξ̂→Ξ`, not in the finite real-rootedness. But then one must be very
clear: E1 is finite self-adjointness, RH-neutral; all the load is in IV.2. The
document essentially says this. Coherent. **H1 — Verdict: SOLID (as structure).** After the correction, H1 = "Perron–
Frobenius gives a simple ground state + positive-envelope eigenvector (de-modulated)". This is
correct *if* `e^{−tQW}` is positivity-preserving, which is claimed via
Lévy–Khintchine + Schoenberg + Trotter with `Λ(n)≥0`. I did not audit `H1_PROOF.md` line by
line, but the structure is standard and the conclusion (simple ground state, nodeless
eigenvector after de-modulation) is numerically supported and is what PF actually gives.
SOLID **as structure**, with the caveat that it does NOT give PSD (see H1′). **H1′ — Verdict: GAP = RH. This is the most important correction of the audit, and
it is correct.** `QW` PSD (`ε_0≥0`) ⟺ Weil positivity in band `logλ` ⟺ RH-up-to-`T*`.
Perron–Frobenius gives a simple ground state and positive eigenvector, **but it does NOT control the sign
of `ε_0`** (PF says "the smallest eigenvalue is simple and its eigenvector is positive"; it does
not say that the smallest eigenvalue is ≥0). The earlier memo claiming "H1 proves `QW` PSD
unconditionally" **would prove RH**, which is impossible without more. The distinction PF ≠ PSD
is exactly correct and is the central finding of the audit. **H1′ is not an
available link; it is RH in disguise.** Correctly flagged. --- ## 3. Scaffolding N0–N3 + Reduction **N0 — SOLID.** The computation `Φ(u)≤Ce^{9u/2}e^{−πe^{2u}}`, even, and the bound
`|Ξ−Ξ_T|≤2∫_T^∞Φe^{δu}du ≤ Cλ^{5/2+δ}e^{−πλ²}` via the substitution `v=e^{2u}` and the
incomplete Gamma function, is correct. I re-verified it: `a=5/4+δ/2`, `X=e^{2T}=λ²`,
`(λ²)^{5/4+δ/2}=λ^{5/2+δ}`. Robust, unconditional, mentions no zeros. **SOLID.** **N1 — SOLID\* (modulo Boas).** The subharmonicity argument for `log|F|−τ Im z`,
bounded by Boas Thm 6.2.4, two-constants + harmonic measure of the segment, is
standard and correct. The harmonic measure bound `ω(iy₀)=(2/π)arctan(R/y₀)≥1−(2/π)(y₀/R)`
is correct. **SOLID** modulo the classical Boas result (legitimate). **N2 — SOLID.** With normalization `ξ̂(0)=Ξ(0)`, Hurwitz-invariant, `Γ=O(1)`. The
normalization is well justified (the conclusion is real-rootedness of the limit,
invariant under nonzero scaling). Loose end correctly closed. **SOLID.** **N3 — SOLID\* (modulo Boas/PL).** `g=Fe^{iτz}` bounded on ℝ, Phragmén–Lindelöf in H.
Classical and correct. **SOLID\*.** **Reduction (Thm 2) — SOLID as a conditional implication, modulo E1.** The
decomposition `ξ̂−Ξ=(ξ̂−Ξ_T)+(Ξ_T−Ξ)`, control of the second term by N0, of the
first by N1 with `R=T*~λ²` (weight `1−ω~λ^{−2}` negligible), giving
`sup_{|Im z|≤½}|ξ̂−Ξ| ≤ Cλ^{1/2}ε_loc + Cλ³e^{−πλ²}`, is **correct**. I re-verified the
arithmetic of the horizon: `1−ω~(2/π)(½)/(λ²)~λ^{−2}`, and `Γ^{1−ω}=poly(λ)^{λ^{−2}}→1`.
The factor `λ^{1/2}` comes from `e^{τy₀}=e^{(logλ)(½)}=λ^{1/2}`. All correct. **The implication "if `ε_loc=o(λ^{−1/2})` then RH" is valid**, modulo E1
(real-rootedness, needed for Hurwitz to transfer). This is frankly a
*conditional implication*: it does not prove the antecedent. The antecedent `ε_loc=o(λ^{−½})`
is precisely IV.2 = RH-equivalent. **SOLID as a reduction; the antecedent is the
RH core.** **Severity on the use of Hurwitz given the state of E1:** the document asks whether
the use of Hurwitz is valid given the status of E1. Answer: **yes, conditionally.**
Hurwitz (E3) only requires that each `ξ̂_λ` be real-rooted; if we accept E1 (as a CCM
black box), Hurwitz transfers correctly. The validity of Hurwitz is **not** in
doubt; what is in doubt is its *input* E1. There is no circularity: E1 (finite
real-rootedness) is RH-neutral (it also holds for DH), so using E1 + convergence to
conclude RH is not circular — the RH load is in the *convergence*, not in E1. **There is no
circularity in the Reduction.** Correct. --- ## 4. III — the renormalization Â=A/ε₀ (my main lens) **Verdict: GAP. Correct conditional implication; the three hypotheses NOT proved, and
one of them IS RH.** Theorem III says: under (H-gap) `inf ε₁/ε₀=1+γ>0`, (H-lim) L² Cauchy of the
renormalized sequence, (H-pos) `ε₀>0`, then `ξ̂_∞` exists and
`ε_loc ≤ (C/γ)√(logλ)·η(λ) + Cλ³e^{−πλ²}`. The proof (Davis–Kahan on `Â`, gap `γ`,
Nikolskii, N0) is **correct given the hypotheses**. **Attack on the three hypotheses:** **(H-pos) `ε₀>0`.** Here I confirm the most severe finding of the audit, and
reinforce it. Since `QW=`Weil form, `ε₀≥0` ⟺ the Weil form is ≥0 on its lowest
band-limited mode ⟺ **Weil positivity up to `T*`** ⟺ **RH-up-to-`T*`**. The renormalization
`/ε₀` **does not merely assume `ε₀>0`; it assumes `ε₀>0` with the correct sign, which is RH.** The
patch `/|ε₀|` saves nothing: if `ε₀<0` (RH false at that height), the "fundamental" of
the renormalized operator has eigenvalue `−1`, and the "isolated positive bottom"
structure on which Davis–Kahan rests collapses or changes nature. **(H-pos)
is RH-baked-in. Confirmed and, if anything, worse than the document admits:** it is
not just "assumes `ε₀>0`", it is that the *entire architecture* of the renormalization presupposes
the RH-true regime. **(H-gap) `γ>0`.** The document (IV.1) claims that `γ=3` "follows" from the
identification of `Â_∞`=2nd-order Sturm–Liouville with spectrum `n²`. **I challenge this and
find it NOT closed** (see §5): the `n²` spectrum is numerical, not derived; and in fact
the very IV.1 document *refutes* the Gantmacher–Krein route and the constant-coefficient
route. So (H-gap) is **numerical, open**. It is not a gift from IV.1. **(H-lim) L² Cauchy.** This is the existence of the scaling limit `Â_∞`. Numerical
(Conj 2b). Not proved. It is a Toeplitz/Loewner limit analysis — hard, not RH-hard. **III conclusion:** GAP. The *conditional* proof is correct (Davis–Kahan + Nikolskii
are well applied). But (H-pos)=RH means III **cannot be used to prove RH
without circularity**: to conclude `ε_loc→0` (⟹RH) one already assumed `ε₀>0` (⟸RH-up-to-T*).
This is a **semi-circularity**: III converts "RH-up-to-T* + technical limits" into
"RH". It is not empty (it improves the height of validity T*→∞), but it is not unconditional. --- ## 5. IV.1 — identification of the limit operator (my lens) **Verdict: GAP (not RH-hard). I closed what is closable; `n²`/`γ=3` remains phenomenological,
and I argue it is NOT a free gift.** **What is PROVED (and I confirm it correct):**
- (A) `QW` commutes with parity `J:j↦−j` ⟹ it decomposes into even/odd sectors; the eigenvalues interlace `ε₀^E<ε₀^O<ε₁^E<…`, giving the parity alternation `(−1)^k`. **Correct and solid** — it is elementary operator theory (`ℤ/2` symmetry). SOLID.
- (B) In the continuum, `QW_∞` is an integral operator with a **bounded** Loewner kernel ⟹ **compact** (eigenvalues → 0). **Correct.** SOLID. **The severe point I add (breaks the optimistic reading):** (A)+(B) are true, but
**they are MUTUALLY IN TENSION with "spectrum `n²`"** and the document does not exploit this. A
**compact** operator has eigenvalues `ε_k→0`. The law `ε_k/ε_0→(k+1)²=n²` says that
the *renormalized* eigenvalues grow like `n²` — i.e. the original `ε_k` **grow**
relative to `ε₀`. This is consistent with compactness only if `ε₀→0` faster (which
does happen, `ε₀~C/λ²`), but it means that **`n²` is the signature of the boundary-layer
operator after `/ε₀`, NOT of the compact operator `QW_∞` itself.** The document says this
("the 2nd order lives in the boundary layer after `/ε₀`"), and that is the correct
reading — but then **(B) does NOT help derive `n²`**: the compact kernel is smoothing, not
differential; the `n²` must come from the Landau–Widom edge operator, which the
document itself admits **has not been derived** (the known profiles give `2n+1` or
logistic, not `n²`). **Recorded refutations I confirm as decisive:**
- Gantmacher–Krein / total non-negativity: **REFUTED** (E16: 15–22% of 2×2 minors `<0`, negative off-diagonals). This closes the "total oscillation from H1" route. Correct and candid. ⟹ Sturm-ness does **not** come from total matrix positivity.
- Constant coefficient (Dirichlet, Hermite, prolate, box): **REFUTED** by overlaps. Correct. **What remains (exact residual):** `Â_∞` is *qualitatively* 2nd order (the alternating
parity `(−1)^k` IS a robust signature of a 2nd-order symmetric operator — this
(A) does rigorously give), but the law `ε_k/ε₀→n²` and hence `γ=ε₁/ε₀−1→3` are
**ONLY measured numerically, not derived**. The residual is the asymptotics of the
boundary-layer operator of the critical frame (Landau–Widom / variable-coefficient de
Branges-SL). **Hard analysis, NOT RH-hard.** ### Can I close (H-gap) γ>0 through my lens? — Candid partial progress. Attempt: prove `γ>0` (uniform relative gap) **without** going through the exact `n²` law. *Idea.* (H-gap) only asks for `inf_λ ε₁/ε₀ ≥ 1+γ` with `γ>0`, i.e. the second eigenvalue
does not stick to the first in relative terms. By (A), `ε₀=ε₀^E` (even) and `ε₁=ε₀^O` (odd, the
next one by interlacing). So
`γ = ε₀^O/ε₀^E − 1 = (smallest eigenvalue of the odd sector)/(smallest of the even) − 1`.
The question is: **is the smallest odd eigenvalue uniformly separated from above
from the smallest even one, on a relative scale?** *What I CAN argue (partially):* By Perron–Frobenius on the even sector
(H1, the even fundamental mode is nodeless after de-modulation) and Sturm oscillation theory
for the bottom of each parity sector of a 2nd-order symmetric operator,
the odd bottom is strictly larger than the even bottom at each finite `λ`:
`ε₀^O > ε₀^E` (because the odd mode has a forced node at the center, raising the
energy). This gives `γ(λ)>0` **at each λ**. ✔ (strict, finite). *What I CANNOT close (the real residual):* the **uniformity** `inf_λ γ(λ)>0`. That
`γ(λ)` does not decay to 0 as `λ→∞`. This requires asymptotic control of
`ε₀^O/ε₀^E`, which is exactly the `n²`-in-the-limit law. Without deriving the asymptotics
of the edge operator, **I cannot exclude** `γ(λ)→0`. The numerical datum `→4` (γ→3) is
strong but is not a proof. **Exact residual I leave named:**
> **(H-gap-res):** Prove `liminf_λ ε₀^O(λ)/ε₀^E(λ) > 1`, where `ε₀^{E/O}` are the
> bottoms of the even/odd parity sectors of `A_λ/ε₀`. Equivalent to: the even–odd
> relative gap of the boundary-layer operator of the critical frame is asymptotically
> `O(1)`. This is semiclassical Landau–Widom analysis; **not RH-hard** (it does not depend on
> the global sign of `Λ(n)`, only on the geometry of the frame at critical density). I closed the finite part (`γ(λ)>0` ∀λ, via the central node of the odd mode); the uniform
liminf remains open but **localized and not RH-hard**. ### Can I close (H-lim), the existence of Â_∞? Not completely. It is the convergence of the symbol of the Loewner-against-
Weil-measure operator under the rescaling `/ε₀`. Compactness (B) gives control of the *raw
limit operator* `QW_∞`, but (H-lim) is about the **renormalized** operator in the low block,
whose existence is precisely Conj 2b. The most I can say: by (B) and Toeplitz/Loewner
symbol theory, *if* the Liouville coordinate of the edge SL
converges (IV.1-res''), then (H-lim) follows. So (H-lim) and the IV.1
identification are **the same analytic residual**. I leave:
> **(H-lim-res) ≡ (IV.1-res''):** existence of the scaling limit of the boundary-layer
> operator (SL coefficients `(p,q,w)` in Liouville coordinate). Analysis,
> not RH-hard. --- ## 6. N5b, N5c **N5b — SOLID.** The argument that the edge dissolves is correct and in fact
elegant: in **absolute** sup-norm, `|ξ̂(t)−Ξ(t)|≈|Ξ'(t)||ρ̂−γ|` with `|Ξ'|~e^{−πt/4}`
decaying; at `T*~λ²`, suppressed by `e^{−π²λ²/2}`. The distinction between
**root** error (relative, grows at the edge) and **absolute** error (suppressed by the
decay of Ξ) is correct and resolves the "boundary layer" mirage of E8. The
target side `Ξ_T` is already uniform by N0. **SOLID.** The edge is benign; the non-trivial part
concentrates in the interior = the IV.2 core. **N5c — SOLID\* (modulo E1 + axis-conv).** The real-rooted monotonicity `|g(x+iy)|≥|g(x)|`
for `g∈LP` is **correct** (a consequence of Hadamard: for `g` with real zeros,
`|g(x+iy)|²=g(x)²∏(1+y²/(x−a_k)²·…)`, increasing in `|y|`). So if `Ξ_f` has an
off-line zero `z₀=x₀+iη₀`, `sup_{|Im z|≤|η₀|}|ξ̂_f−Ξ_f| ≥ |ξ̂_f(z₀)| ≥ |ξ̂_f(x₀)| → |Ξ_f(x₀)|>0`.
Correct. Gives the RH-false side (no convergence off-axis). **SOLID modulo** (i)
real-rootedness of `ξ̂_f` (= E1, true for DH via self-adjointness) and (ii) axis-convergence
(= scaffolding E2.a instantiated at `f`). No new gap introduced. **SOLID\*.** --- ## 7. IV.2 ≡ §V — the core **Verdict: GAP = RH-EQUIVALENT. I do NOT touch it (tribunal's instruction and candor).** I examine only whether the *reduction to this core* is correct and non-circular. The
variational characterization:
- Under RH (`γ_ρ` real), `A_λ(g,g)=Σ_ρ|g(γ_ρ)|²≥0`, the band-limited minimizer vanishes on `{γ_ρ≤T*}` and by counting (Landau–Beurling at critical density) `g₀→Ξ_T`.
- Without RH (`γ_ρ` complex), the form is **indefinite**, the minimizer concentrates on off-line zeros, `≠Ξ_T`.
- ⟹ "Weil ground state = `Ξ_T`" ⟺ RH. **This is correct as a characterization**, and confirms that IV.2 is genuinely
RH-equivalent, NOT a conflation: `QW` IS the Weil form (same object, audited in
E0 with the edge caveat). What is proved: under RH the minimizer *is* `Ξ_T` (modulo
rigor of the frame deficit, Landau–Beurling — an analysis residual but on the
RH-true side, not unconditional); N5c gives the RH-false side. **What is missing — the
unconditional rate `o(λ^{−½})` — IS RH.** Correctly identified as the core. There is
nothing to close here without proving RH. **A rigor point about the frame deficit:** the step "minimizer vanishes on
`{γ_ρ≤T*}` ⟹ `g₀=Ξ_T`" uses that the number of conditions (`#{γ_ρ≤T*}=N(T*)`) equals the
band-limited dimension (`~(L/2π)·2T*`). The "horizon lemma" asserts this equality. I
re-verified it roughly: `N(T*)~(T*/2π)log(T*)~λ²·2logλ`; DOF `~(logλ/π)·2T*~(2/π)λ²logλ`.
**They are not equal: they differ by a factor of `π`/constant** (`2λ²logλ` vs `(2/π)λ²logλ`).
The document itself calls them "comparable", not equal. This matters: at
critical density the interpolating system is *exact* only if the densities coincide; a
constant excess/deficit factor in DOF changes whether the near-null space has dimension 1
(forcing a unique `g₀=Ξ_T`) or dimension `>1` (a family, `g₀` not unique). **The "exactly
`Ξ_T`" rests on the deficit being precisely such that the kernel dimension is 1**
— this is the Landau–Beurling residual and **is not proved**. It is part of the
RH-hard core (RH-true side). I leave it flagged, I do not close it. --- ## 8. E3, E4 **E3 (Hurwitz) — SOLID, modulo E1.** If `ξ̂_λ→Ξ` uniformly on compacts of `|Im z|≤½` and
each `ξ̂_λ∈LP`, a complex zero of Ξ would be a limit of real zeros — a contradiction by
Hurwitz. Correct, classical. Modulo E1 (input). SOLID. **E4 — SOLID.** `Ξ∈LP ⟺ RH`. Classical (the real-rooted Laguerre–Pólya class of Ξ
is equivalent to all zeros of ζ being on the critical line). SOLID. --- ## 9. Synthesis: closed gaps, open gaps **Closed / with rigorous progress (through my lens):**
1. **(H-gap) finite part:** `γ(λ)>0` at each finite `λ`, proved via the forced central node of the odd mode (parity interlacing (A) + Sturm). Residual: uniform liminf `(H-gap-res)`, not-RH-hard analysis.
2. **IV.1 structure:** I confirm SOLID the parity/interlacing (A) and compactness (B); **I add** the argument that (B) (compactness) *prevents* deriving `n²` from the raw operator — the `n²` belongs to the edge operator, not derived. This **clarifies** (does not close) why `n²`/`γ=3` remain phenomenological despite (A)+(B).
3. **(H-pos) reinterpreted:** I confirm and **aggravate** — it is not just "assumes ε₀>0", the entire architecture of `/ε₀` presupposes the RH-true regime (semi-circularity of III). **Open, not-RH-hard (localized, analysis):**
- (H-gap-res): liminf `ε₀^O/ε₀^E>1` (Landau–Widom, boundary layer).
- (H-lim-res) ≡ IV.1-res'': existence of the scaling limit + SL coefficients `(p,q,w)`.
- E1 proper: Hermite–Biehler from self-adjointness (with near-Nyquist edge carrier). **Open, RH-hard (NOT touched, correctly identified):**
- IV.2 ≡ §V: rate `o(λ^{−½})` ⟺ "Weil ground state = Ξ_T" ⟺ RH.
- (H-pos) `ε₀>0` = Weil-positivity-up-to-T* (RH-up-to-T*).
- H1′: `QW` PSD = RH.
- dim-1 frame deficit (RH-true side of the core). **Overall tribunal verdict.** The chain is candid and, after audit, is a
**correct reduction of RH to an RH-equivalent core** (IV.2), surrounded by genuinely
proved scaffolding (N0–N3, N5b, N5c, Reduction, E3, E4). The two claims that a
severe referee might have taken for "unconditional" and which are NOT —H1′ (PSD) and
III/(H-pos)— are **correctly downgraded** to RH-equivalent in the audited version. **RH is not proved; it is localized without self-deception.** The document withstands
scrutiny precisely because it already absorbed the objections I would have raised. The
only point where I still find it optimistic is the claim that `γ=3` "follows"
from IV.1: it does not follow, it is numerical; the finite part `γ(λ)>0` I did close, the liminf I did not. — A. (referee)
