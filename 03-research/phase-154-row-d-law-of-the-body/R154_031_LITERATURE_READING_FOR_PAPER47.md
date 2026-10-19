# R154.031 — Literature reading for Paper 47 (primary sources, read in full)

* Task: (P154.9) read the five items flagged as "must obtain / must read before any
priority claim" in R154.013, and replace the secondary-source entries there by quoted primary text.*

**Method and honesty statement.** Zhu (arXiv:2608.24827v2, 34 pp.), Groskin (arXiv:2607.02828v3,
15 pp.), Suzuki (arXiv:2206.03682v3; arXiv:2209.04658v3; arXiv:2301.00421v3, local copy),
Bombieri (Rend. Lincei 11 (2000) 183–233, BDIM scan, born-digital text layer) and Yoshida
(Adv. Stud. Pure Math. 21 (1992) 281–325, Project Euclid scan) were all **downloaded and read
from the primary PDF text layer**, not from search-engine summaries. The Yoshida PDF is an OCR
of a 1992 typescript: its text layer garbles inequality signs, subscripts and Greek letters
(`:S;` for `≤`, `r.p`/`cp` for `φ`, `~` for `≥`). Quotations from Yoshida are therefore given as
*OCR-verbatim*, with my reconstruction marked in brackets; nothing is reconstructed that is not
visible in the OCR. All page numbers for Bombieri and Yoshida are the printed journal pages,
recovered from the running page markers of the scan.

Normalisation used throughout: our test function `F` is supported in `[−T,T]`, so the
autocorrelation `Φ = F ⋆ F̃` is supported in `[−2T,2T]`. Zhu's `L` is our `T`; his "support 1.6"
is autocorrelation support `2L = 1.6`. Yoshida's window is `a`, autocorrelation support `2a`.
Our Theorem C is at `T = ½log3`, autocorrelation support `log 3 = 1.0986…`.

---

## 1. X. Zhu, arXiv:2608.24827v2

**Bibliographic.** Xuefeng Zhu, *Weil positivity in compact windows: a finite reduction, certified
two-sided bounds, and a Landau–Widom decay law*, arXiv:2608.24827 [math.NT, math.SP], v1 25 Aug
2026, v2 2 Sep 2026, 34 pp. Ancillary certificate/reproducibility package.

**Object.** §1.1, eq. (2)–(3), read verbatim:

> "Q(f) = 2F(i/2)² + (1/2π) ∫_R |F(t)|² Ψ_L(t) dt,  (2)
>  with the Weil symbol
>  Ψ_L(t) = Re ψ(1/4 + it/2) − log π − Σ_{log n < 2L} (2Λ(n)/√n) cos(t log n),  (3)"

and `λ*(L) := inf { Q(f)/‖f‖₂² : f even, real, supp f ⊂ [−L,L] }`.
**This is, symbol for symbol, our `σ_T`.** The only difference is the pole term: Zhu keeps
`2F(i/2)²` as a rank-one addition; we kill the two Tate moments and pass to `P_T`.

**Main theorems, verbatim.**

- **Theorem 1.1 (One-stroke reduction), §1.2.** "Let L > 0 and set T₁ := 2πe^{A_L}. Fix any T♯ for
  which β* := log(T♯/2π) − 1/T♯ − A_L > 0. … Then for every real even f with supp f ⊆ [−L,L],
  Q(f) ≥ R(f) := 2F(i/2)² + (1/π)∫₀^{T♯}(Ψ_L(t) − β*)|F(t)|² dt + β*‖f‖₂²."  (eq. (4)),
  with `A_L = Σ_{log n<2L} 2Λ(n)/√n` the total mass of the prime comb. Continues: "in the Legendre
  basis of L²[−L,L] the quadratic form R is represented by β*I + 2pp^T + C … if the leading N×N
  block has λ_min ≥ λ₀ > 0, then Q(f) ≥ (min(λ₀, β* − ε_D) − ε_B)‖f‖₂²", with `ε_D` (tail-block
  deviation) and `ε_B` (leading–tail coupling norm) "below 10^{-100}" in the certified run.
- **Theorem 1.2 (Certified positivity, support 1.6), §1.2.** "For every real even f ∈ L²(R) with
  supp f ⊆ [−0.8, 0.8], Q(f) ≥ 8.9 × 10^{-18}‖f‖₂². In particular the Weil form is positive on all
  autocorrelations g = f ⋆ f̃ with supp g ⊆ [−1.6,1.6]."
  Certificate parameters: "T♯ = 200, β* = 0.5134…, N = 200 even Legendre modes, working precision
  50 digits"; ingredients "an envelope lemma proved by classical means, a Bernstein-ellipse
  quadrature bound, a forbidden-region tail bound and a verified Cholesky residual" (Lemmas 5.1,
  5.2, §5).
- **Theorem 1.3, §1.3.** "Assume RH. There is an L₀ such that for all L ≥ L₀, λ*(L) ≤ exp(−L e^L)."
- **Theorem 1.4 (Barrier for pointwise-envelope certificates), §1.4 / §14.** "Any application of
  Theorem 1.1 requires T♯ > T₁(L) = 2πe^{A_L}, and A_L = (4+o(1))e^L as L → ∞ by the prime number
  theorem; hence the matrix size N ≍ LT₁ and the number of quadrature nodes grow doubly
  exponentially in L. Moreover sup_t of the prime comb equals A_L exactly (Lemma 3.2), so within
  the class of certificates that bound the comb pointwise the threshold T₁ cannot be lowered."
- **Theorem 6.2 / Corollary 6.3, §6.** Odd sector certified `Q ≥ 8.2 × 10^{-15}` at support 1.6,
  hence positivity for arbitrary complex `f`; "the ground state is simple and even, with certified
  margins", described as "the first of the two missing spectral hypotheses in the operator program
  of Connes–Consani–Moscovici [9] and Connes–van Suijlekom [8]".
- **Synthesis, §1.4.** "8.9 × 10^{-18} ≤ λ*(0.8) ≤ 2.27 × 10^{-17}", "a factor 2.6"; claimed as
  "the first RH-equivalent quantity whose window profile has been enclosed from both sides by
  certified computation".
- **Conjecture 12.1 (the decay law), §12.** "As L → ∞, −ln λ*(L) = 2π² · N(T*)/ln N(T*) · (1+o(1)),
  T* = 2πe^{2L}, N(T*) = e^{2L}(2L−1) + O(L)." Fitted to certified upper bounds at
  `L = 1.4, 1.6, 1.8, 2.0` with residuals below 0.7%.
- **Retraction, §1.2 and Remark 3.3.** "An earlier draft of this work claimed a certified theorem
  at that support [L = 1.19, support 2.38], on the basis of a per-prime 'sharpening' of the
  envelope constant which in fact bounds the prime comb in the wrong direction; Remark 3.3 explains
  the error, and Lemma 3.2 shows that no such sharpening can exist. We retract the claim." The
  950×950 exploratory computation (`λ_min ∈ (10^{-48},10^{-46})`) is kept as evidence only.
- **Prior art as Zhu states it, §1.1.** "the record has stood for three decades: Yoshida [3] proved
  positivity for 2L ≤ log 2, and Connes–Consani [6] re-proved this range … (Claims beyond log 2
  exist in unrefereed preprints; we do not rely on or compare against them beyond noting their
  existence.)"

**Negative findings (searched the full text).** "dual", "linear programming", "subordinator",
"Lévy" do **not occur**. "Bernstein" occurs only as *Bernstein ellipse* (quadrature, Lemma 5.1,
"sum of semiaxes ρ = 6.55"). There is **no** result at autocorrelation support `log 3` and no
per-prime or prime-coupled statement — indeed Lemma 3.2 + Remark 3.3 prove that the per-prime
refinement Zhu attempted is impossible *within pointwise-envelope certificates*.

**Relation to our theorems.** Same symbol, same window functional, opposite method and opposite
epistemic content.
*Overlap.* Zhu's Theorem 1.2 certifies `λ_min > 0` on a window strictly larger than ours
(`2L = 1.6 > log 3 = 1.0986 > log 2`); numerically it therefore **implies** the sign statement of
our Theorem C, at a much larger window, for the full even sector (his `Q` includes the pole term;
on `P_T ⊂ ker` of the Tate moments the same bound holds a fortiori for the corresponding subspace
since `P_T` is a subspace of his class with `F(i/2)` constrained — we should say only that the two
statements are *numerically compatible and his window is larger*, and not claim any implication in
the other direction).
*Weaker than ours.* His route is a pointwise envelope plus a certified finite Galerkin block; it
carries no mechanism — the quantity `8.9e-18` is a machine output, and Theorem 1.4 proves the route
is doubly-exponentially capped. Our Theorem C's `8.86e-5` is produced by an **explicit dual
feasible point** (atomic measure on `|u| ≥ 2T`, multipliers `β₀,β₁`, contact comb), i.e. a weak
duality certificate whose objects are readable; and our Theorem D1 states the equivalence
`A_T|P_T ≥ 0 ⟺ outside-window dual feasibility for all ε`, which has **no counterpart in Zhu**.
Our Theorem O (non-attainment by finite objects) and Theorem E (exponential columns exhaust) are
also absent.
*Stronger than ours.* Window size, and a two-sided enclosure with certified upper bounds; our work
has no upper bound on `λ_min`. Also his parity/ground-state result (Theorem 6.2) is a spectral
statement we do not have.
*Defensible novelty after this reading.* (i) the finite-support **dual equivalence** (Theorem D1);
(ii) **non-attainment** (Theorem O) and the exponential-column exhaustion (E); (iii) the
complete-Bernstein/Lévy structure of the archimedean multiplier and its subordinate-BM reading;
(iv) *first proof of Weil positivity with a prime coupled by an explicit outside-window dual
certificate, with no Galerkin compression and no eigenvalue computation.* The unqualified phrase
"first positivity beyond `log 2`" is **not defensible** and must not appear: Zhu is at 1.6.
Our Lemma V′ (`Θ(log R)` mass-vs-value exchange, no uniform rate) is a lower-bound-on-cost
statement of the same genus as Zhu's Theorem 1.4 / Remark 1.5, obtained for a different
(dual-side) resource; the parallel is worth one sentence and no more.

---

## 2. A. Groskin, arXiv:2607.02828v3

**Bibliographic.** Akiva Groskin, *A finite Guinand–Weil dictionary and archimedean tail order for
the truncated Weil quadratic form*, arXiv:2607.02828 [math.NT, math.SP], v1 2 Jul 2026, v3 14 Aug
2026, 15 pp., 2 figures, reproducibility package.

**Abstract, verbatim.** "The Connes–van Suijlekom and Connes–Consani–Moscovici truncations of the
Weil quadratic form, at a prime cutoff c > 1 and frequency band N, produce finite Galerkin matrices
whose spectra are the finite-rank window on Weil positivity. We prove two exact finite theorems
about this truncation. First, every real even Galerkin coefficient vector v determines, in closed
form, a band-limited Guinand–Weil test function g_v with ⟨v, Q_∞ v⟩ = Σ*_{ζ(1/2+iz)=0} g_v(z),
zeros counted with multiplicity, Q_∞ the cutoff-free truncated matrix: every value of the truncated
form is an exact sum over the nontrivial zeros of ζ. The construction factors through an exact
source quotient of dimension 2N+1 and admits a non-collapsing pole-neutral subfamily. Second,
beyond the Galerkin band the omitted archimedean tail is a totally positive Cauchy–Stieltjes
increment. This yields a two-sided certification rule with an explicit budget
B_T ∼ (2N+1)ρ log T/(π²T), where T is the archimedean cutoff and ρ = 2π/log c: finite-cutoff
positivity certifies cutoff-free positivity, a finite-cutoff eigenvalue below −B_T certifies a
cutoff-free negative, and a negative eigenvalue in the band [−B_T, 0) certifies nothing. Resolving
a spectral scale of 10^{-59} at c = 100 by brute cutoff would require T of order 10^{63}; a
cutoff-free interval LDL^T factorization resolves it directly. The dictionary is verified over the
first 512 zeros of ζ and by three independent computational routes; all scripts and artifacts ship
with the paper."

**Statements read.**
- **Lemma 2.1 (Entry identification), §2.** "The limit defining Q_{arch,∞} exists entrywise, and
  Q_∞ is the Connes–Consani–Moscovici Galerkin matrix."
- **Corollary 2.4 (Finite source quotient), §2**: all finite signed source distributions act
  through an exact quotient of dimension `2N+1`.
- **Theorem 2.5 (Finite Guinand–Weil dictionary), §2** (p. 396 of the text layer): "For fixed
  c > 1, N ≥ 0, and every real even finite Galerkin vector v ∈ R^{N+1}, ⟨v, Q_∞ v⟩ = Σ_{z}g_v(z)",
  with `ĝ_v(ξ) = πK_v(1 − |ξ|/Δ)` on `|ξ| ≤ Δ`, `Δ = L/2π`, `L = log c`, and
  `K_v(ω) = 2∫₀^ω T_v(t)T_v(ω−t)dt` a Volterra (auto-)convolution.
- **Corollary 2.7 (Pole-neutral source survival), §2.** `dim(H_s(N) ∩ P_N(c)) = N − s − 1 > 0` —
  "the finite analogue of working orthogonally to the pole".
- **Theorem 3.2 (Archimedean tail order), §3.** "Let T₂ > T₁ > max(ρN, 7). Then
  Δ_{T₁,T₂} := Q_{arch,T₂} − Q_{arch,T₁} = (1/π²)∫_{T₁}^{T₂} h₊(T)(sin²(LT/2)/ρ)(p_T p_T^t +
  q_T q_T^t)dT"; the increment is positive definite and "in the natural frequency order it is
  strictly totally positive".
- **Corollary 3.3 (Two-sided finite certification rule), §3.** "λ_j(Q_T^tot) ≥ 0 certifies
  λ_j(Q_∞) > 0; λ_j(Q_T^tot) < −B_T certifies λ_j(Q_∞) < 0; a negative eigenvalue in [−B_T, 0)
  certifies nothing", with `B_T = ((2N+1)ρ/(π²T))(log(T/2π)+1)(1+o(1))`.
- **Numerics.** first 512 zeros (`γ₅₁₂ ≈ 826.90`); parameter sets `c=13,N=4`; `c=29,N=6`;
  `c=100,N=200,T=800`.
- **Relation-to-prior-work paragraph, §1**, verbatim: "The autocorrelation mechanism g = f∗f̃ goes
  back to Weil [29], finite-dimensional restrictions of the Weil form were studied by Yoshida [30],
  and the divided-difference structure of the truncated matrix is Proposition 4.1 of
  Connes–van Suijlekom [11]." Also: "Suzuki's screw-function framework [27] gives a parallel
  continuous-variable treatment of the same form."

**Negative findings (full text searched).** "dual", "linear programming", "Lévy", "Bernstein",
"subordinator", "measure outside the window", "log 3" do **not occur**. No positivity theorem at
any explicit window is claimed: the paper is a calibration/dictionary paper, explicitly disclaiming
RH, prime-counting or factorisation claims.

**Relation to our theorems.** Complementary, no collision. Groskin certifies *the truncation*, not
the window: his `Q_T^tot` is the CvS/CCM Galerkin matrix and his theorem says what a finite
eigenvalue computation does and does not prove about the cutoff-free matrix. His `c = log`-cutoff
is a prime cutoff, not our support truncation `[−T,T]` (although `Δ = log c/2π` makes his
band-limited `g_v` supported like ours in the Fourier variable, so his dictionary is the *primal*
direction of our LP: coefficient vector `↦` test function `↦` zero sum). Our Theorem D1 is the
*dual* direction and has no counterpart. His Theorem 3.2 (tail is a totally positive
Cauchy–Stieltjes increment) is the closest object in the 2026 literature to our Structure theorem —
Cauchy–Stieltjes is precisely the Nevanlinna/complete-Bernstein family — but it is a statement about
*matrix increments in the cutoff parameter T*, not the identification of `φ(τ²) = Re ψ(¼+iτ/2) −
ψ(¼)` as a complete Bernstein function of `τ²` with Lévy density
`ν(u) = ½/sinh(u/2) + ½/cosh(u/2)`. That identification, and the subordinate-Brownian-motion
reading, remain unclaimed in this paper. Groskin should be cited (a) as the correct reference for
what finite Galerkin numerics can certify, and (b) as independent 2026 evidence that the
finite-window route is being pursued by matrix methods only.

---

## 3. M. Suzuki: screw function and the Weil Hilbert space

**Bibliographic.**
- M. Suzuki, *Aspects of the screw function corresponding to the Riemann zeta function*,
  J. London Math. Soc. (2) **107** (2023) no. 5, 1846–1888, doi:10.1112/jlms.12785;
  arXiv:2206.03682v3 (31 May 2023).
- M. Suzuki, *The screw line of the Riemann zeta-function and its applications*, arXiv:2209.04658v3
  (17 May 2023), 9 pp. MSC 11M26, 42A82, 46E22.
- M. Suzuki, *On the Hilbert space derived from the Weil distribution*, arXiv:2301.00421v3
  (7 Nov 2025), 20 pp. — local copy `00-references/2301.00421v3.pdf`, read in full.

**The screw function (2206.03682, §1, eq. (1.1) and (1.8)), verbatim.**

> "Ψ(t) := 4(e^{t/2} + e^{−t/2} − 2) − Σ_{n ≤ e^t} (Λ(n)/√n)(t − log n)
>  + (t/2)(Γ′/Γ)(1/4) − (t/2)log π + (1/4)(C − e^{−t/2}Φ(e^{−2t},2,1/4))",
> with `C = π² + 8G` (G the Catalan constant), `Φ` the Hurwitz–Lerch zeta function; and
> `g(t) := −Ψ(t)`.

**Theorem 1.1 (unconditional), §1/§2.** (1) "∫₀^∞ Ψ(t)e^{izt}dt = −(1/z²)(ξ′/ξ)(1/2 − iz)" for
`ℑz > 1/2`; (2) "Ψ(t) = Σ_γ (1 − cos γt)/γ² = Σ_γ (1 − e^{iγt})/γ²"; (3)
"Ψ(t) ≪ exp(t/2 − c√t)".

**Krein class / Lévy–Khintchine-type representation.** Suzuki uses Kreĭn's class `G_a`, §1:
> "he introduced the class G_a consisting of all continuous functions g(t) on (−2a,2a) such that
> g(−t) = g(t) (hermitian) and the kernel G_g(t,u) := g(t−u) − g(t) − g(−u) + g(0) (1.4) is
> non-negative definite on (−a,a)."
The representation is stated in **2209.04658, §1**:
> "an even real-valued function g̃(t) on R with g̃(0) = 0 is a screw function if and only if it
> admits a representation g̃(t) = ∫_{−∞}^{∞} ((cos γt − 1)/γ²) dτ̃(γ) with a non-negative measure τ̃
> such that ∫ dτ̃(γ)/(1+γ²) < ∞",
and in **2301.00421, §2.2, eq. (2.3)**:
> "Every g ∈ G_∞ admits a representation
> g(t) = g(0) + ibt + ∫_{−∞}^{∞} (e^{iλt} − 1 − iλt/(1+λ²)) dτ(λ)/λ²
> with b ∈ R and a measure τ on R such that ∫ dτ(λ)/(1+λ²) < ∞ and vice versa."
**This is a Lévy–Khintchine representation of the *zero-side* measure `τ` (a spectral measure
supported on the zero ordinates `γ`), in the variable `t` dual to `τ`.** It is *not* a
Lévy–Khintchine/Bernstein representation of the archimedean multiplier `Re ψ(¼+iτ/2)`.

**Equivalences.**
- **Theorem 1.2**: "The RH is true if and only if g(t) defined by (1.8) is a screw function on R."
- **Theorem 1.3**: "The RH is true if and only if the hermitian form ⟨·,·⟩_{G_g,a} is non-negative
  definite on C₀(a) … for every 0 < a < ∞. Moreover, assuming that the RH is true, ⟨·,·⟩_{G_g,a} is
  positive definite on L²(−a,a)."
- **Theorem 1.4**: nondegeneracy of `⟨·,·⟩_{G_g,a}` on `L²(−a,a)` for every `a`; equivalently the
  trace-class operator `G_g[a]` has no zero eigenvalue.
- **Theorem 1.5**: "For each 0 < a < ∞, G_g[a] is a trace class operator unconditionally."
- **Theorem 1.6 / 1.7**: RH ⟺ `Ψ(t) = O(1)` on `[0,∞)`; RH ⟺ `Ψ(t) ≥ 0` pointwise (with `Ψ>0` for
  `t ≠ 0` under RH). **Theorem 1.8** discretises 1.7 as a Stieltjes moment problem on
  `μ_n = ∫₀^∞ 4^{-1}e^{-t/2}Ψ(t)t^n dt` (Hankel determinants `Δ_n ≥ 0`).

**Finite-support / small-window positivity (2206.03682, §4) — read verbatim.**
- **Theorem 4.1**: "There exists t₀ > log 2 such that Ψ(t) > 0 for 0 < t < t₀." The proof is
  explicit and unconditional: "there is no contribution from the primes for Ψ(t) on [0, log 2)",
  `Ψ′` has exactly two zeros `t₁ = 0.152631…`, `t₂` on `[0, log 2)`, whence positivity on
  `[0, log 2]` and beyond by continuity. **This is pointwise positivity of `Ψ`, not positivity of
  the form.**
- **Theorem 4.2**: "There exists a₀ > 0 such that G_g(t,u) is positive definite on L²(−a,a) if
  0 < a < a₀. In particular, the restriction g|_{[−2a,2a]} belongs to the class G_a for every
  0 < a < a₀." — **no numerical value of `a₀` is given.**
- **Theorem 4.3**: "Let a₀ > 0 and μ > 0 be given numbers. Then there exists N ≥ 0 such that
  ⟨φ,φ⟩_{G_g,a} ≥ μ∫_{−∞}^{∞}|Φ₁(φ,z)|²dz for every φ ∈ K_{N,0}(a) and 0 < a ≤ a₀" — the analogue
  of Yoshida's Lemma 3. §4.3 notes this "can also be proved using (3.8) and [33, Lemma 3]".
- **§4.2, on Yoshida**, verbatim: "Yoshida proved without any assumption that the hermitian form
  ⟨·,·⟩_W is positive definite on K(a) if a > 0 is sufficiently small ([33, Lemma 2]).
  Connes–Consani [4] provides an operator theoretic conceptual reason for this result. Yoshida also
  proved that, for given a₀ > 0 and μ > 0, there exists N ≥ 0 such that ⟨φ,φ⟩_W ≥ μ‖φ‖_{L²} for
  every φ ∈ K_N(a) and 0 < a ≤ a₀ ([33, Lemma 3])."

**2301.00421 (Hilbert space).** Theorem 1.1: under RH the completion `H_W` of `C_c^∞(R)` in the
Weil hermitian form is isomorphic to the de Branges space `H(E_ξ)`, `E_ξ(z) = ξ(1/2−iz) +
ξ′(1/2−iz)`, via Fourier transform composed with a simple map; §3.3 constructs unconditionally
two Hilbert spaces `H₀, K₀` agreeing with `H_W, K(Θ_ξ)` under RH; **Theorem 1.4**: "The RH is true
if and only if the equality ‖P̂_{Dψ}‖²_{L²(R)} = π⟨ψ,ψ⟩_W holds for all ψ ∈ C_c^∞(R)"; Corollary 1.5
restates it as `2‖ψ‖² = ⟨ψ,ψ⟩_W` on `V°(0)`. §6: `H_W` is "one of the Hilbert–Pólya spaces".

**Negative findings (all three papers searched).** The words "Bernstein", "complete Bernstein",
"subordinator", "Lévy", "Khintchine" **do not occur** in 2206.03682, 2209.04658 or 2301.00421.
There is **no** statement that `Re ψ(¼+iτ/2)` (or `−log π` plus it) is a complete Bernstein /
negative-definite function of `τ²`, and no jump-density computation. No window with an explicit
numerical `a` beyond Yoshida's `log 2/2` is proved; Theorem 4.1's `t₀ > log 2` is about the
*function* `Ψ`, not the form, and must not be cited as a positivity window.

**Relation to our theorems.** Same genus, disjoint content.
*Overlap.* Suzuki's `G_g(t,u)` kernel is (under RH) the same positivity object as our `A_T`
restricted to mean-zero test functions on `(−a,a)`; his `C₀(a)` (`∫φ = 0`) is the analogue of our
"kill one Tate moment"; our `P_T` kills two. His Kreĭn representation is a Lévy–Khintchine formula
for the *zero measure*; our Structure result is a Lévy–Khintchine/complete-Bernstein statement for
the *archimedean multiplier*. These are dual sides of the explicit formula and should not be
conflated, but the genus proximity means Suzuki must be cited whenever we say "Lévy–Khintchine".
*Weaker than ours (for our purposes).* No dual/LP formulation, no outside-window measures, no
non-attainment, no explicit window beyond `a₀` unspecified.
*Stronger than ours.* The trace-class statement (Thm 1.5), the de Branges identification
(2301.00421 Thm 1.1) and the moment-problem discretisation are structural results we do not have.
*Defensible novelty after this reading.* The complete-Bernstein-in-`τ²` identity with the explicit
Lévy density `ν(u) = ½/sinh(u/2) + ½/cosh(u/2)` and the subordinate-Brownian-motion reading remain
**unclaimed in the primary literature I read** — the R154.013 caveat is now discharged, and the
claim may be made, phrased as "the archimedean multiplier, rather than the zero measure, carries a
complete Bernstein structure", with Suzuki cited for the zero-side Kreĭn representation.

---

## 4. E. Bombieri, Rend. Lincei 11 (2000) 183–233

**Bibliographic.** Enrico Bombieri, *Remarks on Weil's quadratic functional in the theory of prime
numbers, I*, Atti Accad. Naz. Lincei Cl. Sci. Fis. Mat. Natur. Rend. Lincei (9) Mat. Appl. **11**
(2000), no. 3, 183–233. Read in full from the BDIM digitisation
(`bdim.eu/item?id=RLIN_2000_9_11_3_183_0`), which carries a clean text layer. (EUDML doc/252338
returns HTTP 403 to automated fetches; BDIM is the accessible mirror.)

**Abstract, verbatim (p. 183).** "This Memoir studies Weil's well-known Explicit Formula in the
theory of prime numbers and its associated quadratic functional, which is positive semidefinite if
and only if the Riemann Hypothesis is true. We prove that this quadratic functional attains its
minimum in the unit ball of the L²-space of functions with support in a given interval [−t;t], and
prove again Yoshida's theorem that it is positive definite if t is sufficiently small. The Fourier
transform of the functional gives rise to a quadratic form in infinitely many variables and we then
study its finite truncations and corresponding eigenvalues. In particular, if the Riemann
Hypothesis is false but only with finitely many non-trivial zeros off the critical line we show that
the number of negative eigenvalues is precisely one-half of the number of zeros failing to satisfy
the Riemann Hypothesis, provided the truncation is big enough."

**Statements read (printed pages).**
- **Theorem 1 (p. 191).** "The Riemann Hypothesis holds if and only if Σ_ρ ĝ(ρ)ĝ(1−ρ) > 0 for every
  complex-valued g(x) ∈ C₀^∞((0,∞)), not identically 0." (a strengthening of Weil's criterion:
  strict positivity, complex test functions, multiplicative variable).
- **Theorem 2 (p. 193).** The explicit formula for the linear functional
  `T[f] = ∫₀^∞ f + ∫₀^∞ f* − Σ_n Λ(n){f(n)+f*(n)} − (log 4π + γ)f(1) − ∫₁^∞ (f(x)+f*(x)−2f(1))
  x dx/(x²−1)` (the archimedean term appears in the `x/(x²−1)` kernel form).
- **Lemma 1 (p. 195), variational equation.** "The variational equation for Problem 1 is
  λ𝒟f(a) − L[f](a) = 0 for a ∈ (M^{-1},M)", where `𝒟 = −D − D²` and `L[f]` is the Euler–Lagrange
  operator of the functional. Two Remarks on the same page propose the Neumann/odd variant and the
  viscosity regularisation `T[f∗f*] + ε‖𝒟f‖²`.
- **Lemma 2 (p. 196).** "If f ∈ W₀ then f is Hölder continuous with exponent 1/2" (plus decay
  estimates). **Lemma 3 (p. 197)**: for `f ∈ L²` supported in `[M^{-1},M]`, a Fourier decay bound
  `f̂(ρ) = O(|ρ|^{-2})` used throughout. **Lemma 4 (p. 198)**: pointwise bound on Taylor
  coefficients of `f̂` at `½+it`.
- **Theorem 3 (existence of a minimiser, p. 197–199).** "Let E be a finite union of closed finite
  intervals in (0,∞). Then the infimum of T[f ∗ f*] in the unit sphere of the space L²(E) of
  L²-functions with compact support in E is attained." (Bombieri stresses in the Introduction that
  "the proof of the first result hinges on the special structure of the term for the «prime at
  infinity» in the Explicit Formula.")
- **Theorem 4 (p. 199).** "Let λ be the infimum of T[f ∗ f̄] in the unit sphere of the space
  W₀ = W₀^{1,2}([M^{-1},M]). If λ < 0, then this infimum is attained."
- **Theorem 5 (p. 199).** "Let μ₊(M) and μ₋(M) be the infimum of T[f ∗ f*] in the class of even and
  odd functions in L²([M^{-1},M]) of norm 1. Then μ₊(M) and μ₋(M) are continuous decreasing
  functions of M."
- **Theorem 6 (p. 205 ff.), Theorem 7 (p. 207 ff.).** The resolvent `(7.5)` is entire in the
  spectral parameter; multiplicity analysis of zeros of the characteristic determinant `D(Λ,t)`.
- **Lemma 10 (p. 211).** "The matrix H(Γ;t) admits the eigenvalue 0 if and only if there is γ ∈ Γ
  [with a degeneracy]" — i.e. eigenvalue 0 is excluded for the finite truncations; Bombieri calls
  this result "new" in the Introduction.
- **Theorem 8 (counting negative eigenvalues, p. 213).** "The number of negative eigenvalues of the
  matrix H(Γ;t) equals the number of distinct complex conjugate pairs (γ, γ̄) in Γ." Proof by a
  continuous deformation of `Γ` keeping eigenvalues real and non-zero.
- **Theorem 9 (p. 217).** Same count for `K_E(Γ)` on a finite union `E` of intervals, with the
  parity-split refinement for symmetric `E`: negative eigenvalues of `K_E^+` count pairs with
  `ℑγ > 0`, of `K_E^-` count pairs with `ℑγ ≥ 0`.
- **Theorem 10 (p. 221) and Theorem 11 (p. 223).** If `ζ` has only finitely many off-line zeros and
  at least one, then for every `t > 0` (resp. every finite union `E`) there are coefficients with
  `Σ|w_γ|² = 1` and `λ ≤ 0` realising an explicit negative-eigenvalue lower bound.
- **Corollary to Theorem 11 (p. 225).** "Let E ⊂ (0,∞) be a finite union of bounded closed
  intervals and suppose that T[f ∗ f̄] ≥ 0 for every smooth function f with compact support in E.
  Then either the Riemann Hypothesis is true, or ζ(s) has infinitely many zeros off the critical
  line, or the functions x^{−ρ} are linearly dependent over E, for a suitable sequence of
  coefficients {c_ρ} ∈ ℓ² such that at least half of its ℓ²-mass is supported on the set of zeros ρ
  with ℜ(ρ) = 1/2." An Example on the same page exhibits genuine linear dependence for two Dirichlet
  L-functions of the same modulus and parity, with `f` supported in `(1/p₀, p₀)`.
- **§12 "Sets of positivity" (p. 225–229), Theorem 12.** "If F(x) has compact support in an
  interval I of length |I| < log 2 we have T[F(x) ∗ F(−x)] = Σ_γ F̂(γ)F̂(γ̄) ≥ (log(1/|I|) −
  log log(1/|I|) − O(1))‖F‖²." Proof, verbatim: "Since G(x) = F(x) ∗ F(−x) remains unchanged if we
  replace F(x) by a translation F(x+c), we may assume that F(x) is supported in the interval
  [−a/2, a/2] with a < log 2. Then G(x) is supported in [−a,a] ⊂ (−log 2, log 2). Thus in the
  Explicit Formula as above for T[G], the contribution of the sum involving Λ(n) vanishes."
  Bombieri notes at the head of §12: "Another proof can be found in Yoshida's paper [5]."

**Negative findings.** No duality, no linear programming, no measures outside the window: the whole
memoir is primal/variational plus a finite-matrix eigenvalue theory. The only "outside" objects are
the deformations of the zero multiset `Γ` in Theorems 8–9.

**Relation to our theorems.** Bombieri studies exactly our `λ_min(A_T)` (his `μ±(M)`, `λ`), and
Theorems 3–5 are the primal existence/continuity facts underlying any dual treatment; our Theorem O
("the dual sup is never attained by finite objects") is the **precise dual counterpart** of his
Theorem 3 ("the primal inf is attained"), and the pairing of the two is the sharpest way to state
our contribution: *primal attained, dual not attained.* This pairing is, on this reading, new.
Theorem 12 is the classical `|I| < log 2` window with a **quantitative** lower bound
`log(1/|I|) − log log(1/|I|) − O(1)`, which **degrades to nothing as `|I| ↑ log 2`** and is vacuous
at `|I| = log 3`: it is strictly weaker than our Theorem C in window and gives no constant there.
Theorems 8–11 (eigenvalue counting, the linear-dependence trichotomy) concern a different question
(what positivity on a fixed `E` can imply about the zeros) and are the right citation for why a
single-window positivity theorem, ours included, cannot imply RH. Our Lemma V′ has no analogue
here.

---

## 5. H. Yoshida, Adv. Stud. Pure Math. 21 (1992) 281–325

**Bibliographic.** Hiroyuki Yoshida, *On Hermitian forms attached to zeta functions*, in *Zeta
Functions in Geometry* (N. Kurokawa, T. Sunada, eds.), Adv. Stud. Pure Math. **21**, Kinokuniya,
Tokyo, 1992, pp. 281–325; doi:10.2969/aspm/02110281. **Primary text obtained and read** from the
open Project Euclid chapter PDF. Caveat: OCR of a typescript; inequality signs and Greek letters
are unreliable in the text layer, so quotations below are OCR-verbatim with bracketed
reconstruction.

**Setting (§0, pp. 281–282).** For `F ∈ C_c^∞(R)`, `Φ(s) = ∫F(x)e^{(s−1/2)x}dx`, `F̂(t) =
Φ(½+it)`, the explicit formula is displayed with archimedean term
`(1/2π)∫_{−∞}^{∞} F̂(t) Re ψ(¼ + it/2) dt` and `T(F) = Σ_ρ Φ(ρ)`. Hermitian form
`(φ₁,φ₂) := T(φ₁ ∗ φ̄₂)`; `C(a) = {φ ∈ C_c^∞(R) : supp φ ⊆ [−a,a]}`;
`K(a) = {φ : φ = f on |x| ≤ a, 0 on |x| > a, f ∈ C^∞(R) of period 2a}`; and
`K_N(a) = {φ ∈ K(a) : ∫_{−a}^{a} φ(x)exp(πinx/a)dx = 0 for all |n| ≤ N}`.
"R.H. is equivalent to the positive definiteness of ( , )|C(a) for every a > 0 (cf. Proposition 2)."

**Lemma 2 (p. 289), OCR-verbatim.** "There exists a₀ > 0 such that (cp, cp) > 0 for every
r.p E K(a), r.p -=I= 0 if a :S; ao" — i.e. *there exists `a₀ > 0` such that `(φ,φ) > 0` for every
`φ ∈ K(a)`, `φ ≠ 0`, if `a ≤ a₀`.* The proof concludes: "If a₀ is sufficiently small, we can find
μ > 0 such that (φ,φ) > μ‖φ‖²_{L²} for every φ ∈ K(a), a ≤ a₀." **No numerical value of `a₀`
is given.**

**Lemma 3 (p. 290–291), OCR-verbatim.** "Suppose that a₀ > 0 and µ > 0 are given. Then there exists
a non-negative integer N such that [(φ,φ) ≥ µ‖φ‖²_{L²}] for every cp E KN(a), 0 <a::; ao." — i.e.
*given `a₀ > 0` and `µ > 0` there is `N ≥ 0` with `(φ,φ) ≥ µ‖φ‖²_{L²}` for all `φ ∈ K_N(a)` and
`0 < a ≤ a₀`.* (Confirmed independently by Suzuki's paraphrase, 2206.03682 §4.2, quoted in item 3
above.)

**Theorem 1 (§6, p. 310), OCR-verbatim.** "Let a = log 2/2. We have [(φ,φ) ≥ 0] for every
<p E K(a), where equality holds if and only if cp = 0." The Introduction (p. 283) states the
intended reading explicitly: "In §6, we shall give a detailed sample computation, though it does not
follow the algorithm faithfully, when a = log 2/2: We find ( , )|K(a) is positive definite for
a ≤ log 2/2 (Theorem 1). The idea is to calculate the hermitian matrix on W(a) with sufficient
approximation for a suitably chosen N." §6 carries out a `10 × 10` matrix positivity check on the
odd part and a `200`-mode estimate on the even part, with `ε = 1/40` in (6.15).

**Theorem 2 (§7/§8).** RH ⟺ the extended hermitian form is non-degenerate on the completed space
`K̂(a)` for every `a > 0`; **Propositions 2 and 7** give non-degeneracy on `C(a)` and `K(a)`
unconditionally; **Proposition 6 (§8)**: if RH fails, `( , )|C(a)` is not positive definite for `a`
large enough. **Proposition 1 (§1)** separates even/odd positive definiteness: `T_k` oddly positive
definite ⟺ RH for `ζ_k`; evenly positive definite ⟺ RH for `ζ_k` excluding real zeros.

**Relation to our theorems.** Yoshida's `a = (log 2)/2` is autocorrelation support `log 2`; our
Theorem C is at autocorrelation support `log 3`, with the prime 3 genuinely coupled (his window is
exactly the largest one in which *no* prime term appears in the explicit formula — cf. Bombieri's
proof of Theorem 12, quoted above: "the contribution of the sum involving Λ(n) vanishes").
**So our window is the first one past the prime-free regime that is handled by an analytic dual
certificate, and Yoshida's method (a finite matrix computed to sufficient approximation) is
precisely the method we do not use.** His Lemmas 2 and 3 are qualitative (no explicit `a₀`,
no explicit `N`), so there is no constant of his to compare with our `8.86 × 10^{-5}`.

---

## Summary table

| Item | Window certified | Method | Dual/LP? | Lévy/Bernstein? | Collides with |
|---|---|---|---|---|---|
| Yoshida 1992 Thm 1 | `2a = log 2` (prime-free) | finite matrix, hand computation | no | no | nothing of ours |
| Bombieri 2000 Thm 12 | `\|I\| < log 2` (prime-free), with rate `log(1/\|I\|)` | explicit formula, primes vanish | no | no | nothing of ours |
| Bombieri 2000 Thms 3–5 | — (existence of minimiser, continuity) | variational | no | no | **dual counterpart of our Thm O** |
| Suzuki 2022–23 | `a < a₀`, `a₀` unspecified | Kreĭn screw functions, trace class | no | Kreĭn rep. of the **zero** measure | genus of our Structure thm |
| Groskin 2026 | none (calibration only) | Galerkin + tail budget `B_T` | no | Cauchy–Stieltjes **matrix increment** | nothing of ours |
| Zhu 2026 Thm 1.2 | `2L = 1.6` (primes 2,3,4 coupled) | pointwise envelope + certified 200×200 Cholesky | no | no | **supersedes our window numerically** |
| **ours** | `2T = log 3`, `λ ≥ 8.86e-5` | explicit outside-window dual certificate | **yes (Thm D1, O, E)** | **yes (complete Bernstein in `τ²`)** | — |

**Priority verdict.** Defensible, after this reading: (1) the finite-support **dual** equivalence
(Theorem D1) and its non-attainment (Theorem O) and exhaustion (Theorem E) — no counterpart in any
of the five sources; (2) the complete-Bernstein/Lévy identification of the archimedean multiplier
with the explicit density `½/sinh(u/2) + ½/cosh(u/2)` — absent from Suzuki, who has the dual-side
Kreĭn representation instead; (3) Theorem C as *the first Weil-positivity window past the prime-free
regime proved by an explicit dual certificate rather than by matrix compression*. **Not defensible:**
any claim of the form "first positivity beyond `log 2`" or "largest known window" — Zhu's certified
`1.6` is larger, and must be cited at the point where our window is announced.

---

## Proposed «Related work» paragraph (LaTeX-ready, 287 words)

```latex
\paragraph{Related work.}
Positivity of the Weil functional on a fixed window goes back to Yoshida~\cite{Yoshida1992}, who
proved strict positivity of the Hermitian form on $K(a)$ at $a=\tfrac12\log 2$ by an approximate
finite-matrix computation, together with the qualitative small-window and high-frequency lemmas
(\cite[Lemmas~2--3, pp.~289--291]{Yoshida1992}). Bombieri~\cite{Bombieri2000} gave the variational
theory: the infimum of the functional on the unit sphere of $L^2(E)$ is attained
(\cite[Thm.~3, p.~197]{Bombieri2000}), the window minima $\mu_\pm(M)$ are continuous and decreasing
(\cite[Thm.~5]{Bombieri2000}), the finite truncations never have eigenvalue $0$, and the number of
negative eigenvalues equals the number of off-line conjugate pairs
(\cite[Thm.~8, p.~213]{Bombieri2000}); his \cite[Thm.~12, p.~225]{Bombieri2000} makes the
$|I|<\log 2$ window quantitative, the range in which the prime sum is empty. Suzuki's screw-function
programme \cite{Suzuki2023jlms,Suzuki2023screwline,Suzuki2025hilbert} recasts the same form through
Kre\u{\i}n's class $\mathcal G_a$, with a L\'evy--Khintchine representation of the \emph{zero}
measure, trace-class kernels, and a de Branges model of the Weil Hilbert space; the archimedean
multiplier itself is not analysed there. Two 2026 preprints treat the truncated form by matrix
methods: Groskin~\cite{Groskin2026} proves an exact finite Guinand--Weil dictionary and shows the
omitted archimedean tail is a totally positive Cauchy--Stieltjes increment, yielding a two-sided
certification budget $B_T$; Zhu~\cite{Zhu2026} reduces the window problem to one finite matrix by a
pointwise envelope and certifies $Q(f)\ge 8.9\cdot 10^{-18}\|f\|_2^2$ for $\operatorname{supp}f
\subseteq[-0.8,0.8]$, with a matching upper bound and a conjectural Landau--Widom decay law, while
proving that pointwise-envelope certificates face a doubly exponential barrier. Our window is
smaller than Zhu's; what is new here is the \emph{dual} formulation --- an exact equivalence with
outside-window certificates, the non-attainment of the dual supremum by finite objects, and a
positivity constant produced by an explicit certificate rather than by a spectral computation.
```

## BibTeX

```bibtex
@incollection{Yoshida1992,
  author    = {Yoshida, Hiroyuki},
  title     = {On {H}ermitian forms attached to zeta functions},
  booktitle = {Zeta Functions in Geometry},
  series    = {Adv. Stud. Pure Math.},
  volume    = {21},
  pages     = {281--325},
  publisher = {Kinokuniya},
  address   = {Tokyo},
  year      = {1992},
  doi       = {10.2969/aspm/02110281}
}

@article{Bombieri2000,
  author  = {Bombieri, Enrico},
  title   = {Remarks on {W}eil's quadratic functional in the theory of prime numbers, {I}},
  journal = {Atti Accad. Naz. Lincei Cl. Sci. Fis. Mat. Natur. Rend. Lincei (9) Mat. Appl.},
  volume  = {11},
  number  = {3},
  pages   = {183--233},
  year    = {2000},
  note    = {\url{http://www.bdim.eu/item?id=RLIN_2000_9_11_3_183_0}}
}

@article{Suzuki2023jlms,
  author  = {Suzuki, Masatoshi},
  title   = {Aspects of the screw function corresponding to the {R}iemann zeta function},
  journal = {J. Lond. Math. Soc. (2)},
  volume  = {107},
  number  = {5},
  pages   = {1846--1888},
  year    = {2023},
  doi     = {10.1112/jlms.12785},
  eprint  = {2206.03682},
  archivePrefix = {arXiv},
  primaryClass  = {math.NT}
}

@misc{Suzuki2023screwline,
  author = {Suzuki, Masatoshi},
  title  = {The screw line of the {R}iemann zeta-function and its applications},
  year   = {2023},
  eprint = {2209.04658},
  archivePrefix = {arXiv},
  primaryClass  = {math.NT}
}

@misc{Suzuki2025hilbert,
  author = {Suzuki, Masatoshi},
  title  = {On the {H}ilbert space derived from the {W}eil distribution},
  year   = {2025},
  note = {version 3, 7},
  eprint = {2301.00421},
  archivePrefix = {arXiv},
  primaryClass  = {math.NT}
}

@misc{Groskin2026,
  author = {Groskin, Akiva},
  title  = {A finite {G}uinand--{W}eil dictionary and archimedean tail order for the truncated {W}eil quadratic form},
  year   = {2026},
  note = {version 3, 14},
  eprint = {2607.02828},
  archivePrefix = {arXiv},
  primaryClass  = {math.NT}
}

@misc{Zhu2026,
  author = {Zhu, Xuefeng},
  title  = {{W}eil positivity in compact windows: a finite reduction, certified two-sided bounds, and a {L}andau--{W}idom decay law},
  year   = {2026},
  note = {version 2, 2},
  eprint = {2608.24827},
  archivePrefix = {arXiv},
  primaryClass  = {math.NT}
}
```
