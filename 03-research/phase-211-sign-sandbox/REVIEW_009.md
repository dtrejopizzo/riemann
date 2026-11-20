# Review 009: rounds 010_A, 011_A, 011_C, 012_A, 012_B, 013_A against Paper 47 §sec:ext and prolate theory

Scope. ROUND_010_A, ROUND_011_A, ROUND_011_C, ROUND_012_A, ROUND_012_B, ROUND_013_A, checked against Paper 47
(04-papers/47-row-d-dual-certificates/main.tex: eq:symbol and eq:W at L.110–124, lem:mbounds L.505–515, def:W/thm:Z
L.1225–1260, §sec:ext L.9856–10045: def:ext, lem:ext-mob, thm:ext-half, prop:ext-gauge, lem:ext-ellbound, prob:ext-L,
prop:ext-consol, lem:ext-hf) and against the classical prolate theory (Slepian–Pollak; double orthogonality; the
whole-line finite Fourier eigen-equation). Verdict per PROVED claim: CONFIRMED / REFUTED / DOWNGRADE. Line numbers are
memo line numbers. Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## 1. ROUND_010_A

**Identity (3.1) (L.136–141).** CONFIRMED. It is eq:form + eq:W of Paper 47 for real g: the comb term
(1/2π)∫Σv_n cos(τ log n)|ĝ|² equals Σv_n c_g(log n), the contact set n < N is NT of eq:symbol, and 2Re(AB̄) = 2AB for real
g. Notational defect: the memo writes P_T for the trigonometric polynomial while Paper 47 writes \PT for the primitive
subspace; both appear in the same sentences (e.g. L.174–179). Rename the polynomial in any integration.

**§1 consistent quotient, D_g = D − DJH⁻¹JᵀD (L.24–35).** CONFIRMED as bookkeeping. leak(f) = Σd_k⟨f, ψ_k⟩² for f supported
in [−λ, λ] requires ψ_k normalised in L²(−λ, λ) (stated so in ROUND_012_B L.4; L.5 here says only "normalised in L²";
fix). H = I − Jᵀdiag(χ)J is the exact leakage Gram of the gauge only when the gauge basis is orthonormal and the in-band
sum is complete; with the truncation k ≤ K it overestimates leak(φ) by Σ_{k>K}χ_k⟨φ, ψ_k⟩², which is negligible for
k ≫ 4N. The restriction to the five conditions is the exact restriction of prob:ext-L to f ∈ span{ψ_k} ⊕ 𝒢_T because
f(0) and ℱf(0) are gauge-invariant (def:ext). C² is not imposed (acknowledged L.271–274); nothing in §1 is used in a proof.

**Remark 1.1 (L.37–43).** CONFIRMED (bookkeeping; Table 1.0 NUMERICAL).

**Lemma 3.1, L² Markov (L.147–150).** CONFIRMED. ‖P_j′‖² = j(j+1) on [−1, 1], so ‖P̄_j′‖² = (2j+1)j(j+1)/2 ≤ (j+1)³;
Σ_{j≤K}(j+1)³ = ((K+1)(K+2)/2)², whence ‖p′‖ ≤ ((K+2)²/2)‖p‖ on length 2 and (K+2)²/L after rescaling.

**Proposition 3.2 (L.152–163).** CONFIRMED. g′ formula and the substitution u = ne^x are correct (only n ≤ λe^T = N
contribute); ‖E⁻¹‖ ≤ 2√N is lem:ext-mob; the jump/Sobolev split gives ‖(1 − P_<)g‖² ≲ (NK² + N²K⁴)/Ω_*‖g‖², which is
covered by the stated C(1 + N²K⁴)/Ω_*. The hypothesis of lem:ext-hf is ‖P_<g‖² ≤ ‖g‖²/(2(K_T + λ + 1)), stronger than the
"≥ ½" used at L.155, so the conclusion holds a fortiori. The prolate transfer (Remark L.164–167) is ARGUED, as labelled.

**Proposition 3.3, NO-GO for 𝒦_S (L.169–182).** CONFIRMED as a statement; DOWNGRADE of its reading. Proof checked:
c_{g₀}(log 2) = (1 − O(T⁻²))‖g₀‖² when τ₀log 2 ∈ 2πℤ; archimedean term ≤ log(2 + 3Ω₀) + C_∞. One error-term misstatement:
A(g₀), B(g₀) are not O((τ₀T)^{−M})‖g₀‖ (the weight e^{±x/2} has Paley–Wiener growth e^{T/2}); the correct bound is
O_M(T(τ₀T)^{−M}e^{T/2}), and after projection to \PT the cost is ‖g − g₀‖ = O_M(T(τ₀T)^{−M})‖g₀‖, so the conclusion stands
(rank two vanishes on \PT). The reading at L.180–182 and L.297 ("this is exactly why lem:ext-hf needs Ω_* ≍ e^{λ+O(1)}") is
wrong: in lem:ext-hf (main.tex L.10038–10041) K_T = C_∞ + 𝒜_T with 𝒜_T = Σ_{n<N}v_n ≈ 4λ the comb mass, so
Ω_* = e^{K_T+λ+1} − 2 ≍ e^{5λ+O(1)}. The NO-GO and lem:ext-hf are consistent (negativity is possible up to e^{4λ−C},
positivity is certified above e^{5λ+O(1)}); the sentence must say e^{𝒜_T+λ+O(1)}. Prop 3.2's threshold
K ≥ c′N^{−1/2}e^{(K_T+λ+1)/4} is stated with K_T and is unaffected. The transfer to the high block (L.183–185) is ARGUED.

**Proposition 4.1 (L.217–226).** CONFIRMED (classical): double orthogonality on [−λ, λ] at c = 2πλ² with
ℱf(ξ) = ∫f e^{−2πixξ} (def:ext convention) gives zero cross-overlaps and diagonal leakage; (4.1) is (3.1) polarised with
A_jB_k + A_kB_j. The "no spectral separation" mechanism (L.224–226) is ARGUED.

**Numerics (§2, §5).** NUMERICAL, not reviewed digit by digit. Hostile note: the "assembled bound" W_T ≥ θ_Kλ_A‖Ef‖²
(L.124–126, L.285) is a Galerkin value on a span, with M computed by a sine-Galerkin image that is neither an upper nor a
lower bound for W_T in general; it must not be called a bound. §3.4(i)–(iii) is ARGUED / OPEN as labelled; the
Landau–Widom constant in (ii) is quoted without the normalisation of c being checked against the source; it is not used.

## 2. ROUND_011_A

**Lemma 1.1 (L.38–48).** CONFIRMED for (a), (b); DOWNGRADE (correction) for (c). (a): c_{g₀}(u) splits as stated, with
∫β(x/T)β((x+u)/T)dx = Tρ(u/T)∫β² and ‖g₀‖² = ½T∫β² + O; the oscillatory term is O_M((τ₀T)^{−M})T. (b): the first-order
term of m around τ₀ cancels by evenness of β̂, so the error is in fact O(1/(τ₀T)²); the stated O(1/(τ₀T)) is weaker and
correct. (c): as in §1 above, |A(g₀)| + |B(g₀)| ≤ C_M(τ₀T)^{−M}‖g₀‖ is false as written (missing factor ≍ e^{T/2}); the
second clause ‖g − g₀‖ ≤ C_M(τ₀T)^{−M}‖g₀‖ holds up to a factor T. In the high range τ₀ ≥ 2πN the corrected bound is
still super-polynomially small, so nothing downstream changes.

**Proposition 1.2 (L.50–60).** DOWNGRADE: necessity CONFIRMED, equivalence not proved. The proof gives (HR)(a) ⟹ (1.2).
Two repairs: (i) the \PT-projection of g₀ adds multiples of the duals of e^{±x/2}, which do not vanish at ±T, so the
packet is not in the core required by prob:ext-L; project instead with two fixed C_c^∞(I_T) functions dual to (A, B);
the cost is the same order. (ii) The phrases "equivalent at leading order" (L.56) and "⟺" (L.189) claim sufficiency, which
would require control of cross terms between packets; nothing in the memo proves it (ROUND_012_A §4.2 itself shows that
cross terms reassemble long profiles). Read "⟹" throughout.

**Lemma 2.1 (L.64–67).** CONFIRMED (gχ₀(·/T) = g, Cauchy–Schwarz with |Tχ̂₀(T·)|; constant C₀²/4π²).

**Kovrijkine citation (L.69–74).** CONFIRMED: O. Kovrijkine, Proc. Amer. Math. Soc. 129 (2001) 3037–3047, Theorem 1,
constant (γ/C)^{C(ab+1)}; with b = 2T (support of the Fourier transform of ĝ) and a = A/T, ab = 2A. The 2π factor of the
Fourier convention changes only C.

**Proposition 2.2 (L.76–90).** CONFIRMED (split E_ϑ / complement / low band; Plancherel). The reading that thickness
reduces to a pointwise statement is ARGUED, correctly.

**Theorem 3.1 (L.94–109).** CONFIRMED as stated, CONDITIONAL on Theorem B of ROUND_006_C (CONFIRMED in REVIEW_005 §3) and
on its extension to the weights ρ(k log p/T) (the extension only lowers block masses; accepted). Bernstein step, superlevel
interval of length s/(TΣ₀), choice k = ⌊log Ω/(2T)⌋ with N^k ≤ Ω, and the asymptotic (3.2) all recomputed
(4kS₂/(es²) = 64T/(eϑ²L)). DOWNGRADE of its value: the theorem is superseded by the trivial bound. Since 0 ≤ ρ ≤ 1 and
v_n ≥ 0, P^ρ_T ≤ Σ₀ everywhere (Paper 47 lem:mbounds(iii)), hence P^ρ_T < ϑm on every τ with m(τ) > Σ₀/ϑ, i.e. above
log Ω_triv = Σ₀/ϑ + log 2π + o(1) ≈ 4λ/ϑ, while log Ω_B ≈ (64/(eϑ²))TN. Theorem B therefore certifies nothing that the
triangle inequality does not certify at a doubly-exponentially lower height.

**Corollary 3.2 (L.111–118).** CONFIRMED (θ formula and its asymptotics recomputed), with the same downgrade: the identical
argument with Ω_triv in place of Ω_B gives coercivity of size m(Ω_triv) ≍ λ with θ = O(η) and is the mechanism already
used in lem:ext-hf. Consequently the "Result" statement (L.181–182, L.202) that (HR)(a) is "OPEN on 2T ≲ log τ < log Ω_B"
is REFUTED as a description of the open range: the open range is 2T ≲ log τ < Σ₀ + O(1) (as ROUND_011_C Lemma 1.1 later
records); and ROUND_011_C L.27 ("Theorem 3.1 is still what gives the coercivity of size ≍ m … which Lemma 1.1 does not") is
likewise wrong. The NO-GO for the moment class (L.137–150, §4(a)–(b)) stays as a class statement but loses its relevance:
the class limit lies above a height that the trivial bound already clears.

**Proposition 4.1 (L.122–131).** CONFIRMED with one correction. MV lower bound, the (𝒫^ρ)² cross integral ≤ 2Σ₀²/log 4,
the fourth moment (CONDITIONAL on ROUND_006_C Lemma B.0 / Theorem B), Hölder (ΩV^{3/2}/(244S₂)), mean ≤ 3Σ₀ and the final
constant ρ(1)³/(488·2√2) ≈ ρ(1)³/1381 all recomputed. Correction: the autocorrelation of a nonnegative even β need not be
monotone on [0, 1], so V ≥ ρ(1)²Σ_{n≤λ}… must read (min_{[0,1]}ρ)². The size (sup ≥ c₁T with c₁ ≈ 7·10⁻⁴) is far below
m ≈ 4T at Ω = N²; the "genuine O(1) competition" reading (L.132–135) is ARGUED, not a consequence of this bound.

**Falsifier §5.** CONFIRMED (size statements; cΛ fails (1.2) for c > c* by Proposition 4.1).

## 3. ROUND_011_C

**Lemma 1.1 (L.18–24).** CONFIRMED. (i) d/dτ Reψ(¼ + iτ/2) = Σ(k + ¼)(τ/2)/|k + ¼ + iτ/2|⁴ is correct; this is
lem:mbounds(i) of Paper 47 and should be CITED from there. (ii) is lem:mbounds(iii) with weights 0 ≤ ρ ≤ 1. (iii)
m(τ) = log(τ/2π) + O(τ⁻¹) by lem:mbounds(ii) (the memo's O(τ⁻²) is also true asymptotically, Stirling); log 2π < 2 gives
log τ*_κ ≤ Σ₀ + κ + 2. The table of §1 and Tables 2.1, 3.1 are NUMERICAL (spot-check: m(Ω_lo) at T = 0.8 equals
log(1.1N) = 1.695 to the printed digits). Reading (L.25–28): the second sentence is wrong, see Corollary 3.2 above.
The grid-error argument for the scan (L.52–54) is sound for frequencies < 2T. §4(i) "(HR)(a) in pointwise form is the
right formulation" overstates: (1.2) is necessary only (Proposition 1.2 downgrade).

## 4. ROUND_012_A

**Lemma 1.1 (L.20–22).** CONFIRMED (for u ≥ 1 the sets [−1, 1 − u] and [u − 1, 1] overlap in measure 0).

**Lemma 1.2 (L.24–28).** CONFIRMED. The closed form of ρ and the formula for 6ρ′ were checked by quadrature (agreement to
30 digits at u = 0.3, 1.0, 1.7) and by differentiation; the sign argument on [1, 2] via t ≤ tan t is correct.

**Theorem 2.1 (L.35–41).** CONFIRMED. m(Ω_lo) at 30 digits: m(2π·1.1) = 0.09443, m(2π·2.2) = 0.78824, m(2π·3.3) = 1.19383;
½v_2 = 0.49013, ½(v_2 + v_3) = 1.12441; slack 0.0694 (the memo's 0.0688 is a rounding slip; κ = 0.069 holds). The
range split by contact thresholds and the use of |ρ| ≤ ½ at log n/T ≥ 1 (equality at T = log 2, n = 2, allowed by
Lemma 1.1(ii)) are correct. Note: the statement needs Σ^{|ρ|}, since ρ_β may be negative for real β; the proof uses it.

**Theorem 2.2 (L.44–50), certified computation.** CONFIRMED; re-run. tools/cos2_trivial_cert.py was executed on the grids of
the proof: [0.01, 0.3] step 0.01 → min slack 0.1145; [0.3, 2.5] step 0.01 → 0.3316; [2.5, 2.6] step 0.002 → 0.1367;
[2.6, 2.64] step 0.001 → 0.0486; [2.64, 2.67] step 0.001 → first failing cell [2.660, 2.661] (slack −9.5·10⁻⁵). On (0, 0.01]
the comb is empty and the slack is m(2π·1.1) = 0.0944. All printed slacks reproduce. Hostile remarks, none fatal: (i) Σ is
enclosed in interval arithmetic, m is a 50-digit floating evaluation, not an enclosure (error ≪ slack); (ii) grid points
are floats accumulated by addition, but each cell is [T_j, T_{j+1}] with the same floats on both sides, so coverage is
contiguous; (iii) the docstring calls the result "Theorem 2.1"; it is Theorem 2.2; (iv) the script divides by T and
cannot be started at T₀ = 0. The failure location "2.662, slack −0.004" (L.50) is a point value; the cell test fails first
at 2.660–2.661 (conservative), consistent.

**Proposition 3.1 (L.59–64).** CONFIRMED as an identity: with f(x) = β(x/T), ⟨f, A_τf⟩ = ‖f‖²P^{ρ_β}_T(τ), and the supremum
over L²[−1, 1] is λ_max of the real symmetric A_τ. DOWNGRADE of the reading "what (HR)(a) actually needs" (L.53–57, L.127):
Proposition 1.2 of 011_A is proved for each fixed smooth β with constants C_M(β); a supremum over all L² profiles is
reached only through T-dependent, possibly rough profiles, for which the packet error is not controlled. What follows
from (HR)(a) is λ_max(A_τ) ≤ m(τ) − κ + o(1) after approximating the top eigenvector by smooth profiles at scale ≫ 1/N (true,
since A_τ is bounded), and only for τ ≥ 2Ω_lo(1 + o(1)), not τ ≥ Ω_lo. Record it as "necessary up to o(1)".

**NO-GO 4.1 (L.72–76).** CONFIRMED, with the bound read for Σ^{|ρ|} (the class "P ≤ Σ^ρ_T" is the trivial bound) or for
β ≥ 0; for signed ρ the displayed lower bound on Σ^ρ_T is not valid as written. **NO-GO 4.2 (L.78–84).** DOWNGRADE to
ARGUED: it is a valid remark that any proof must imply the long-profile bounds and that absolute-value cross-term bounds
return Σ^{ρ′}; it is not a theorem about a class of methods. **NO-GO 4.3 (L.86–90).** CONFIRMED as an instance of the closed
mean-square family (loss recorded). §4.4 and §5: NUMERICAL / ARGUED as labelled.

## 5. ROUND_012_B

**Input (S) (L.25–30).** CONFIRMED. With ℱ as in def:ext and the interval [−λ, λ], the time–band parameter is c = 2πλ², and
the finite Fourier eigen-equation holds for every real argument, giving ℱ(ψ_k1_{[−λ,λ]}) = ε_k√χ_kφ_k on ℝ, ε_k = i^k for even
k (the sign convention (−i)^k vs i^k coincides for even k). ‖φ_k‖² = 1/χ_k and ⟨u_j, u_k⟩ = δ_{jk}d_k follow.

**Input (T) (L.31–33).** CONFIRMED for admissible f, g: it is the bilinear form of the radical relation used in the proof of
thm:ext-half (main.tex L.9918–9925) and ROUND_001_B; Ef = Φ_f − Ψ_f and the Poisson form of Φ_f are in def:ext.

**Theorem 1.1 (L.35–43).** DOWNGRADE: the polarised half-line identity W_T(Ef, Eg) = 𝒲(Ψ_f, Ψ_g) with off-band data
ℱf|_{|ξ|>λ} = Σa_kε_ku_k is CONFIRMED; the entrywise factorisation M = ZᵀS𝒢SZ with a "class-blind Gram matrix"
𝒢_{jk} = 𝒲(𝒯u_j, 𝒯u_k) is not established and, entrywise, is not defined. Reason: the tail map 𝒯 and the Poisson
representation Ψ_f = 𝒯(ℱf) need f(0) = ℱf(0) = 0 and ℱf = O(ξ⁻²) (def:ext, and the memo's own domain condition at
L.36). A raw prolate has ψ_k(λ) ≠ 0 (ROUND_010_A Table 1.0: |ψ_k(λ)| = 3–5 above 4N), so u_k(ξ) ~ ε_kψ_k(λ)sin(2πλξ)/(πξ)·(sign),
the series Σ_n u_k(ne^{−x}) converges only conditionally, 𝒯u_k ~ e^{x/2}·(sawtooth) as x → −∞, and B(𝒯u_k) and the comb sum
of 𝒲 diverge absolutely. 𝒢 is therefore a bilinear form only on the subspace of coefficient vectors b with
Σb_kε_kψ_k(λ) = 0 (and the conditions at 0), and that subspace is defined through ε_k: the domain of 𝒢 is not class-blind.
The use of the Slepian eigen-equation is correct; the half-line identity is used correctly only on admissible pairs.

**Corollary 1.2 (L.45–57).** DOWNGRADE to a tautology plus a CONFIRMED NO-GO. On per-class admissible blocks the objects are
defined, and M_{+−} = −Z₊ᵀ𝒢_{+−}Z₋ holds with 𝒢_{+−} defined by that very equation; "exact sign" carries no information
until 𝒢 is given an independent definition across classes. The NO-GO "no smallness of the high cross-class coupling from
the selection rule" is CONFIRMED by the cited Fourier defect 2Σ(1 − εε_k√χ_k)a_k² → 2‖a‖² as χ_k → 0 (ROUND_009_B Thm 1.2,
CONFIRMED in REVIEW_008).

**Corollary 1.3 (L.59–66).** CONFIRMED as an identity on spans where each class block is admissible on its own (then
a₊ ± a₋ are both admissible and M(a₊ + a₋) = 𝒢[a₊ − a₋] is meaningful). The interpretation "near-cancellation of
neighbouring exterior tails" presupposes a banded, index-continuous 𝒢 and is ARGUED; the range-split control (§2.4) is
NUMERICAL support, not proof.

**Proposition 1.4 (L.68–80).** DOWNGRADE to ARGUED. The comb estimate is not derived: for Ψ, Ψ′ supported in (−∞, −T] with
|Ψ(y)| ≤ C_Ψe^{3(y+T)/2} one gets |c_{Ψ,Ψ′}(log n)| ≤ C_Ψn^{−3/2}3^{−1/2}‖Ψ′‖ and a sum Σv_nn^{−3/2} = 2(−ζ′/ζ)(2), not
the stated (−ζ′/ζ)(3/2) mechanism (the stated constant is an upper bound but its derivation is missing); the rank-two
term of 𝒲 is absent from the displayed bound; the low factor is CONDITIONAL on ROUND_009_A. "PROVED shape" is not
supported by a proof.

**Numerics §2–§3.** NUMERICAL; NO-GO for the three-block LM/H₊/H₋ Schur assembly with block-diagonal ℓ_g normalisation
(θ₃ < 0 on resolved points, Dcross ≤ 0.16) is accepted as a NUMERICAL NO-GO for that assembly, not as a proof. The
falsifier paragraph (L.148–159) is CONFIRMED in its logical part (Theorem 1.1 uses the radical relation, specific to Λ).

## 6. ROUND_013_A

**Lemma 1.1 (L.23–29).** DOWNGRADE to CITED (standard Poisson/B-process). (i) is correct (no stationary point for j = 0;
smooth amplitude). (ii) the range j > τm/(2πN) ≥ m(1 + δ) is correct; the leading-order stationary-phase formula with
factor χ(s) and the error (1 + O(1/τ)) is the classical B-process; the error term is quoted, not derived, and is not
uniform near the ends of the support x_j ∈ (e^{−2T}/m, N/m) where w varies at scale T in log x. NUMERICAL check accepted.

**Proposition 2.1 / identity (2.2) (L.38–48).** CONFIRMED, with an identification the memo misses. Mellin inversion,
−ζ′/ζ(z) = ζ′/ζ(1 − z) − χ′/χ(z) (from ζ(z) = χ(z)ζ(1 − z)), absolute convergence at Re u = c′ < −½, w(1/n) = w(n) and
n^{s−1} = conj n^{−s} on the line are all correct, so P^ρ_T = 𝒜_w + R_w exactly. But R_w is, by the residue theorem, the
sum of the residues of (ζ′/ζ)(1 − s − u)w̃(u) in the strip between the two lines, i.e. the contribution of the nontrivial
zeros of ζ plus the polar term. (2.2) is therefore the Weil explicit formula for the even test function ρ(|x|/T)cos(τx),
already in Paper 47 as thm:Z (eq:fw, eq:Z, L.1240–1260) for compactly supported weights. Labels: identity CITED (Weil;
Paper 47 thm:Z), not new. The memo's statements that "the sandbox does not evaluate" R_w and that R_w is a
"strip-crossing defect" are correct but hide what R_w is; the reformulation of (U) at L.60–61 is a restatement of (U) as
a statement about the zero side of the explicit formula on cells of width 1/T. It is a restatement, as the memo says, and
must be recorded as such.

**Lemma 2.2 (L.50–54).** CONFIRMED with an omission. −(χ′/χ)(½ + ir) = Reψ(¼ + ir/2) − log π = m(r) is correct, the kernel
(1/2π)w̃(iv) has mass ρ(0) = 1, and evenness kills the first-order term, so 𝒜_w = m(τ) + O(T⁻²τ⁻²). Moving 𝒜_w from Re u = c
to Re u = 0 crosses the pole of χ′/χ(s + u) at s + u = 1; its residue w̃(1 − s) is of the same negligible size
O(e^{T}(Tτ)^{−k}) as the polar term, but it should be written.

**Proposition 3.1, NO-GO class 𝒱 (L.65–83).** DOWNGRADE to ARGUED (class closure). (a) is a correct structural description;
(b) "every Type I/Type II split is a split of the same Mellin integrand" and (c) "bounded only with constant/power losses"
are not theorems. The identification above sharpens the reason: any method in 𝒱 that produced the O(1) constant would
evaluate the zero side of the explicit formula on a cell, which no Type I/II estimate does. The NO-GO is accepted as an
ARGUED class closure.

**Falsifier §4.** CONFIRMED (identity linear; (b), (d) break it; (c) depends on a functional equation of the system).

## 7. Verdict table

| Memo | Claim | Verdict |
|---|---|---|
| 010_A | (3.1), §1 quotient, Remark 1.1, Lemma 3.1, Prop 3.2, Prop 4.1 | CONFIRMED (fix: P_T vs \PT notation; normalisation of ψ_k on [−λ, λ]) |
| 010_A | Prop 3.3 (NO-GO 𝒦_S) | CONFIRMED; reading "Ω_* ≍ e^{λ+O(1)}" REFUTED (Ω_* ≍ e^{𝒜_T+λ+O(1)} ≈ e^{5λ}); A, B error term corrected |
| 010_A | "assembled bound" θ_K | NUMERICAL Galerkin value, not a bound |
| 011_A | Lemma 1.1(a)(b), Lemma 2.1, Prop 2.2, Kovrijkine citation | CONFIRMED |
| 011_A | Lemma 1.1(c) | DOWNGRADE (missing factor e^{T/2} in |A| + |B|; projection clause holds) |
| 011_A | Prop 1.2 | DOWNGRADE: necessity only; core membership of the packet needs compactly supported duals |
| 011_A | Thm 3.1, Cor 3.2 | CONFIRMED (CONDITIONAL on ROUND_006_C Thm B); superseded by the trivial bound P ≤ Σ₀ |
| 011_A | "OPEN on 2T ≲ log τ < log Ω_B" | REFUTED as a range description: open range is 2T ≲ log τ < Σ₀ + O(1) |
| 011_A | Prop 4.1 | CONFIRMED with ρ(1) → min_{[0,1]}ρ |
| 011_C | Lemma 1.1 | CONFIRMED (= lem:mbounds(i),(iii) of Paper 47; cite); reading L.27 REFUTED |
| 012_A | Lemmas 1.1, 1.2; Thm 2.1 | CONFIRMED (slack 0.0694) |
| 012_A | Thm 2.2 | CONFIRMED, re-run reproduces all slacks; first failing cell [2.660, 2.661] |
| 012_A | Prop 3.1 | CONFIRMED as identity; "needed" reading DOWNGRADE to "necessary up to o(1), τ ≥ 2Ω_lo" |
| 012_A | NO-GO 4.1 / 4.2 / 4.3 | CONFIRMED (Σ^{|ρ|}) / ARGUED / CONFIRMED (closed family) |
| 012_B | (S), (T) | CONFIRMED |
| 012_B | Thm 1.1 M = S𝒢S | DOWNGRADE: polarised half-line identity CONFIRMED; entrywise class-blind 𝒢 undefined (ψ_k(λ) ≠ 0, Poisson conditions fail for raw ψ_k) |
| 012_B | Cor 1.2 | tautological on per-class admissible blocks; NO-GO (no smallness from the selection rule) CONFIRMED |
| 012_B | Cor 1.3 | CONFIRMED as identity; interpretation ARGUED |
| 012_B | Prop 1.4 | DOWNGRADE to ARGUED |
| 013_A | Lemma 1.1 | DOWNGRADE to CITED (standard B-process; error term quoted) |
| 013_A | Prop 2.1 / (2.2) | CONFIRMED; it is the explicit formula (Paper 47 thm:Z): label CITED, R_w = zero side + polar term |
| 013_A | Lemma 2.2 | CONFIRMED (add the residue of χ′/χ at s + u = 1, negligible) |
| 013_A | Prop 3.1 (NO-GO 𝒱) | DOWNGRADE to ARGUED class closure |

Nothing in these six memos is a sign step, and none is offered as one.

## 8. NO-GO register (this review)

1. 𝒦_S, comb-mass-only estimates on high frequencies (010_A Prop 3.3): PROVED NO-GO; negativity possible up to
   e^{S−C}, consistent with lem:ext-hf's threshold e^{𝒜_T+λ+O(1)}.
2. lem:ext-hf on polynomial-index data (010_A Prop 3.2): PROVED void unless K ≥ c′N^{−1/2}e^{(K_T+λ+1)/4}.
3. Measure-of-large-values + Logvinenko–Sereda/Kovrijkine (011_A §2): collapses to a pointwise bound; PROVED as a
   comparison of conditions, class closure ARGUED.
4. Moment class with integer-spacing error (011_A §4): ARGUED; irrelevant in practice, because the trivial bound
   P ≤ Σ₀ already clears every height where the class could act.
5. Trivial bound with a fixed profile (012_A §4.1): PROVED (finite T_β for every β).
6. Short packets with absolute-value cross terms (012_A §4.2): ARGUED.
7. Mean value + Sobolev/Gallagher (012_A §4.3): instance of the closed mean-square family.
8. Three-block LM/H₊/H₋ Schur with block-diagonal ℓ_g normalisation (012_B §2): NUMERICAL NO-GO.
9. Smallness of the H₊–H₋ coupling from the ℱ-class selection rule (012_B Cor 1.2): PROVED NO-GO (Fourier defect → 2‖a‖²).
10. Class 𝒱, Vaughan/Heath-Brown + Poisson/B-process on the packet polynomial above the plunge (013_A §3): ARGUED class
    closure; the full B-process dual returns the explicit formula, whose zero side is the only place the O(1) margin lives.

## 9. Consequences for the record

- The open part of (HR)(a) in packet form is the finite range Ω_lo ≤ τ ≤ 2π·exp(Σ₀ + κ + O(1)) (011_C Lemma 1.1); the
  thresholds Ω_B of 011_A are not part of the open statement.
- (U) of 012_A is a necessary condition for coercive (HR)(a), up to o(1), not a reduction; together with 011_A
  Prop 1.2 nothing yet gives sufficiency.
- The S𝒢S picture of 012_B is a heuristic organising principle on per-class admissible spans, not an exact
  class-blind factorisation; the "next step" of 012_B (banded sweep in b = Sa) must first define 𝒢 on a common domain.
- 013_A's identity is the explicit formula already in Paper 47; the one-profile margin is a statement about its zero
  side on cells of width 1/T. Recording that is a restatement of (U), not a reduction.
- Row D OPEN.
