# CA_D_001 — Hardy-amplitude transfer: the window form weighted by Z_T² is positive on P_T, unconditionally (phase 193)

Pen and paper; no numerics.
**No negative value of 𝔞_T for ζ is produced or claimed.**
Conventions are those of CA_D_000. For F ∈ L²(ℝ), F̂(τ) = ∫F(x)e^{iτx}dx. For a tempered g, G = ǧ means G(τ) = ∫g(u)e^{−iτu}du, so
∫|G|²dτ = 2π∫|g|²du. P_T^∞ := {F ∈ C_c^∞(−T,T) real : F̂(±i/2) = 0}. This set is dense in P_T for the form norm; the density
extension is standard and is labelled ARGUED where it is used.

## 0. Corpus check
- EI_003 Thm 1 = P47 prop:shape-phase (PROVED): Z_T = e^{iΘ}Z_X(½+iτ) is real, and σ_T = 2Θ′.
- CA_B_001: J(σ) with the frozen weight ω = F̂₀²|Z_{<X}(½+iτ)|². There the sign of J′(½) is ARGUED to be zero geometry. The weight here
  is |F̂|² alone, the test is primitive, and the sign is PROVED by a support argument. Different object.
- R164_102 (W-Landau): positivity of the coefficients z_X is not used below; only their support is used.
- EI_002 / P47 prop:shape-family: ζ_w's polar term. The pole of Z_X is handled here by the Tate condition, not by smoothing.
- Grep for Mandel, analytic signal, first spectral moment, time delay in 03-research: no hit (R186_114 mentions Kahane–Mandelbrojt, which
  is unrelated). Not a retry.

## 1. Two lemmas

**Lemma 1 (spectral structure of the beyond-window factor; PROVED, with CITED inputs).** Let κ_X := 1/Z_{<X}(1) =
exp(−Σ_{n<X}Λ(n)/(n log n)) > 0, which is the residue of Z_X at s = 1. As tempered distributions in τ,
  Z_X(½+iτ) = 1 + κ_X·X^{½−iτ}/(iτ−½) + Y_X(τ),
where 1 = δ̌_0. The middle term is the transform of μ_− := −κ_X e^{u/2}1_{u<2T}du, a finite measure. Y_X = μ̌_+ for a tempered
distribution μ_+ supported in [2T,∞). Explicitly, μ_+ = Σ_{k≥X} z_X(k)k^{−½}δ_{log k} − κ_X e^{u/2}1_{u≥2T}du.

*Proof.* Put H(s) := X^{s}(Z_X(s) − 1) − κ_X X/(s−1).
(i) H is holomorphic on Re s > 0. Z_X = ζ·W with W := 1/Z_{<X} entire. The only pole of Z_X − 1 is the simple pole at 1, with residue
κ_X. At s = 1, X^{s}κ_X/(s−1) − κ_X X/(s−1) = κ_X(X^{s}−X)/(s−1) is regular.
(ii) H has polynomial growth on Re s ≥ ½. First, W(s) = Σ_m w_m m^{−s} with Σ|w_m|m^{−½} ≤ exp(Σ_{n<X}Λ(n)n^{−½}/log n) < ∞, so
|W| is bounded on Re s ≥ ½. Second, |ζ(s)| ≪ (1+|t|)^{½} on Re s ≥ ½, |s−1| ≥ 1 (convexity bound, CITED [Titchmarsh §5.1]).
(iii) H is bounded as Re s → +∞. For Re s > 1, X^{s}(Z_X(s) − 1) = Σ_{k≥X}z_X(k)(X/k)^{s}. This uses the formal identity
Z_X = exp(Σ_{n≥X}Λ(n)n^{−s}/log n): the coefficients of Z_X vanish on 1 < k < X. This is the Euler gap.
By the Paley–Wiener–Schwartz theorem for half-planes (CITED: a function holomorphic on Re s > ½ with polynomial growth on the closed
half-plane has boundary values that are the Fourier–Laplace transform of a tempered distribution supported in [0,∞)),
H(½+iτ) = η̌(τ) with supp η ⊂ [0,∞). Hence X^{−½−iτ}H(½+iτ) = μ̌_+ with μ_+ := η(· − 2T), supported in [2T,∞).
Next, κ_X X/(s−1)·X^{−s} at s = ½+iτ equals κ_X X^{½−iτ}/(iτ−½) = −κ_X∫_{−∞}^{2T}e^{(½−iτ)u}du = μ̌_−.
The explicit form of μ_+ comes from writing ζ(½+iτ) as the transform of Σ_n n^{−½}δ_{log n} − e^{u/2}du on ℝ, whose partial integral on
[0,∞) is bounded, and convolving with the finite measure Σ_m w_m m^{−½}δ_{log m}. The continuous part becomes −(Σ_m w_m/m)e^{u/2} =
−κ_X e^{u/2} on all of ℝ. The explicit form is not used below. ∎

**Lemma 2 (first moment = phase velocity; PROVED).** Let G ∈ H¹(ℝ) with G = ǧ, and suppose G = e^{−iφ}r with r real-valued and
φ ∈ C¹. Then ∫φ′(τ)|G(τ)|²dτ = 2π∫u|g(u)|²du.
*Proof.* From conj(G)·iG′ = r(φ′r + ir′), Re(conj G·iG′) = φ′r² = φ′|G|². Also iG′ = (ug)ˇ, so ∫conj(G)·iG′ = 2π∫u|g|², which is real. ∎
(Lemma 2 is valid for every φ. It is the coordinate D1 of CA_D_000 and carries no sign by itself.)

## 2. The theorem

**Theorem 1 (Hardy-amplitude transfer; PROVED).** Let T > 0 and X = e^{2T}. Let F ∈ P_T^∞ have even part E and odd part O. Define
g_E by ǧ_E(τ) = Ê(τ)Z_X(½+iτ), and R_E := g_E − E; define g_O and R_O in the same way. Then R_E and R_O are
supported in [T,∞), and
  𝔞_T^{Z}(F) := (1/π)∫Θ_X′(τ)|F̂(τ)|²Z_T(τ)²dτ = 2∫_T^∞u(|R_E(u)|² + |R_O(u)|²)du ≥ 2T·ρ_F,
  ρ_F := ‖R_E‖² + ‖R_O‖² = (1/2π)∫|F̂(τ)|²(Z_T(τ)² − 1)dτ ≥ 0.
Here Z_T(τ)² = |ζ(½+iτ)|²·exp(−2Σ_{n<X}Λ(n)n^{−½}cos(τ log n)/log n).

*Proof.* (a) Support. Lemma 1 gives g_E = E + E*μ_− + E*μ_+ (convolution on ℝ_u). E is supported in [−T,T] and μ_+ in [2T,∞), so E*μ_+ is
supported in [T,∞). For u ≤ T and v in the support of E(u−·), that is v ∈ [u−T,u+T] ⊂ (−∞,2T], the factor 1_{v<2T} equals 1. So
(E*μ_−)(u) = −κ_X e^{u/2}∫E(w)e^{−w/2}dw = −κ_X e^{u/2}Ê(i/2) = 0, by the Tate condition (Ê(i/2) = (F̂(i/2)+F̂(−i/2))/2 = 0). Hence
E*μ_− is supported in [T,3T], and R_E = g_E − E is supported in [T,∞). The same holds for O.
(b) Phase. Ê is real-valued and Ô is purely imaginary. Z_X(½+iτ) = e^{−iΘ}Z_T with Z_T real. So ǧ_E = e^{−iΘ}(ÊZ_T), and ǧ_O =
e^{−iΘ}(−i)(iÔZ_T), each of the form e^{−iΘ}·(real) up to a constant phase. Regularity: Ê, Ô are Schwartz, and Z_X, Z_X′ grow
polynomially on the line, so ǧ_E, ǧ_O ∈ H¹.
(c) Lemma 2 with φ = Θ gives ∫Θ′|ÊZ_X|² = 2π∫u|g_E|² = 2π(∫uE² + 2∫uE·R_E + ∫u|R_E|²). The first term vanishes because E² is even. The
second vanishes because the supports [−T,T] and [T,∞) meet in a null set. So ∫Θ′|ÊZ_X|² = 2π∫_T^∞u|R_E|² ≥ 2πT‖R_E‖². The same holds
for O.
(d) |F̂|²Z_T² = |ÊZ_X|² + |ÔZ_X|². The cross term 2Re(Ê·conj Ô)Z_T² vanishes since Ê is real and Ô imaginary. Summing and dividing by π
gives the formula. Plancherel and E ⊥ R_E give ‖g_E‖² = ‖E‖² + ‖R_E‖², that is (1/2π)∫|ÊZ_X|² − (1/2π)∫|Ê|² = ‖R_E‖². Summing over E, O
gives the expression for ρ_F. ∎

**Corollary 1.1 (two unconditional ζ-statements on P_T; PROVED).** For every F ∈ P_T^∞, with C_X(τ) := Σ_{n<X}Λ(n)n^{−½}cos(τ log n)/log n:
 (i) ∫|F̂(τ)|²|ζ(½+iτ)|²e^{−2C_X(τ)}dτ ≥ ∫|F̂(τ)|²dτ, a mean-value inequality for the beyond-window factor on primitive autocorrelations;
 (ii) ∫[(Θ_X′(τ) − T)Z_T(τ)² + T]·|F̂(τ)|²dτ ≥ 0.
In particular, for T < ½log 2 (no comb, Θ = θ): ∫m(τ)|F̂(τ)|²|ζ(½+iτ)|²dτ ≥ 2T∫|F̂|²(|ζ(½+iτ)|² − 1)dτ ≥ 0.

**Theorem 1′ (integer powers; PROVED).** Let k ≥ 1, and let F be real in C_c^∞(−T,T) with F̂^{(l)}(±i/2) = 0 for 0 ≤ l ≤ k−1. Then
  ∫Θ_X′|F̂|²Z_T^{2k}dτ = (2π/k)∫_T^∞u(|R^{(k)}_E|² + |R^{(k)}_O|²)du ≥ 0,
with R^{(k)} := (·)*(μ_X^{*k} − δ_0).
*Proof.* Z_X^k = (μ_X^{*k})ˇ, where the convolutions are of distributions supported in a common half-line, and the Laplace transform of
a convolution is the product of the transforms. The phase of Z_X^k is −kΘ (mod π). In μ_X^{*k}, any term with j ≥ 1 factors μ_− has the
form μ_−^{*j}*(δ_0 or μ_+)^{*(k−j)}. Here μ_−^{*j} has density (−κ_X)^j e^{u/2}(2jT−u)^{j−1}/(j−1)! on u < 2jT. For u ≤ 2jT − T,
(F*μ_−^{*j})(u) = (−κ_X)^j e^{u/2}∫F(w)e^{−w/2}(2jT−u+w)^{j−1}dw/(j−1)!, which vanishes under the j-th order Tate condition. So
F*μ_−^{*j} is supported in [2jT−T,∞) ⊂ [T,∞). Terms with only μ_+ factors lie in [2T,∞), and their convolution with F lies in
[T,∞). Then apply Lemma 2 with φ = kΘ and the argument of (c). ∎

## 3. The general form, and what the theorem is not

**Theorem 1″ (FE class; PROVED, same proof).** Let L(s) = Σa_n n^{−s} have real coefficients and satisfy the following:
- L converges absolutely for Re s > σ₀ and is nonzero for Re s ≥ σ₁;
- L is meromorphic on Re s > ½−ε, with at most a simple pole at s = 1;
- L has polynomial growth on Re s ≥ ½ away from the pole;
- L satisfies an FE γ_L(s)L(s) = γ_L(1−s)L(1−s) with γ_L real on ℝ and zero-free and pole-free on Re s ≥ ½.
Define the comb by −L′/L = Σ Λ_L(n)n^{−s}, the window factor Z_{<X,L} := exp Σ_{n<X}Λ_L(n)n^{−s}/log n, and the window phase
Θ_{X,L} := arg γ_L(½+iτ) + Im log Z_{<X,L}(½+iτ). Then Theorem 1 holds for L, with Θ_{X,L}′, which is half the window symbol of L.
*Proof.* Lemma 1 used only the gap of exp Σ_{n≥X}, which holds for every comb, the growth of L, and the simple pole. Lemma 2 needs
Z_{X,L} = e^{−iΘ_{X,L}}·(real), which is the FE on the line. ∎
**Consequences for the campaign (PROVED from Theorem 1″ and thm:shape).**
(a) Theorem 1″ applies to Davenport–Heilbronn-type and Epstein-type series (O10), to ζ_K (O12) and to any FE-quartet model with a
Dirichlet expansion (O7, ARGUED: it depends on the model of lem:shape-quartet having a Dirichlet series with the stated growth). These
include objects with negative primitive bottoms at some windows (P47 falsifier list). So **the weighted positivity holds where D fails**.
By thm:shape(C), Theorem 1 is not, and cannot be made, the sign step of row D. It is a tool; its YES column is (R)(2), (3) and (4).
(b) The positivity of z_X(n) is never used. Only the gap {1 < n < X} ∩ supp z_X = ∅ is used. Lead (a) of the brief ("nonnegative
coefficients beyond the window") therefore contributes nothing beyond the gap, and the gap holds for every comb.
(c) Without the FE (a_P, Λ+cδ_{n₀}, deletions O1–O3, O5–O6), Lemma 2 applies with the phase −arg Z_{X,a}. Its velocity is
Re R_{X,a}(½+iτ) ≠ Θ_{X,a}′. The statement then concerns a symbol different from the window symbol. So the FE is load-bearing in
Theorem 1, which is (P6) satisfied as an inequality, but only jointly with a property (gap + simple pole) shared by the whole FE class.

## 4. Relation to row D (exact)
For F ∈ P_T^∞ even or odd, let 𝒵F := g_F = F + R_F. Since 𝔞_T is defined by the symbol on the whole form domain,
  𝔞_T(𝒵F) = 𝔞_T^{Z}(F) = 2∫_T^∞u|R_F|² ≥ 0,
and expanding,
  𝔞_T(F) = 2∫_T^∞u|R_F|²du − 2Re 𝔞_T(F,R_F) − 𝔞_T(R_F).      (4.1)
(4.1) is exact. As a criterion it is REF-D: its content is 𝔞_T(F) itself. Its reading is as follows. Row D is the **amplitude-one
endpoint** of a family of statements that are PROVED for every amplitude |Z_X|^k, k ≥ 1. Multiplying the test by Z_X pushes every
spectral component other than the window part itself to u ≥ T. There the first moment, which is the mean phase velocity, is at least
T > 0. With amplitude one, the phase e^{−iΘ} = Z_X/Z_T is a unimodular function whose spectrum is not one-sided: dividing by the real
Z_T destroys the half-line support. At non-integer powers, restoring it needs log Z_X holomorphic on Re s > ½, which is excluded zero
information (D8 in CA_D_000).
**Where the weight is small (PROVED, elementary).** On the central Nyquist cell I_T := {|τ| ≤ π/(8T)} (T ≥ 1), every n < X has
|τ log n| < π/4, so C_X(τ) ≥ B_X/√2 with B_X := Σ_{n<X}Λ(n)n^{−½}/log n. Also |ζ(½+iτ)| ≤ |s|/|s−1| + 2|s| ≤ 2.55 there, from
ζ(s) = s/(s−1) − s∫_1^∞{x}x^{−s−1}dx. Hence Z_T² ≤ 6.6·e^{−√2B_X} on I_T. This is doubly-exponentially small in T, since
B_X ≍ e^{T}/T by Chebyshev (CITED). The centre is where σ_T(0) = C₀ − A < 0 and where (R)(7) demands exactness. **Theorem 1's
positivity is therefore produced by suppressing the amplitude exactly where the comb is coherent.** CA_D_002 turns this into a NO-GO.

## 5. Review (own)
1. *Is Lemma 1's half-plane PWS correctly applied?* H is holomorphic on Re s > 0 ⊃ closed half-plane Re s ≥ ½, with polynomial growth
   there, so the boundary values on Re s = ½ are a tempered distribution whose transform is supported in [0,∞). Orientation: for
   s = ½+iτ, Re s > ½ ⟺ Im τ < 0, and e^{−iτu} is bounded there for u ≥ 0. ✓ Growth near s = 1: H is regular there, by (i). ✓
2. *Tate sign.* ∫E(w)e^{−w/2}dw = Ê(τ) at iτ = −½, that is τ = i/2. P_T has F̂(±i/2) = 0. ✓ Only one Tate point is needed for k = 1. The
   other one is automatic for even or odd parts.
3. *Phase of the odd part.* ǧ_O = Ô·Z_X = (iÔ_r)e^{−iΘ}Z_T with Ô_r real. A constant phase does not change φ′. ✓
4. *Cross term in (c).* ∫uE·R_E: E vanishes on (T,∞), and R_E vanishes on (−∞,T). ✓ For a test with support touching ±T, the
   intersection {T} is null. ✓
5. *Convergence of ∫u|R|².* It is finite iff ǧ ∈ H^{½}. Here ǧ ∈ H¹, since F̂ is Schwartz and |Z_X|, |Z_X′| ≪ τ^{½+ε}. ✓
6. *Is Theorem 1 trivial?* It is a support plus Plancherel argument (an analytic-signal argument). The non-trivial inputs are (i) the
   Euler gap of Z_X, (ii) the FE identification arg Z_X = −Θ (P47 prop:shape-phase), and (iii) the cancellation of the pole by the
   Tate condition at exactly the abscissa ½. Each of the three is necessary: without (i) the window part is not isolated, without (ii)
   the phase is not the window symbol, and without (iii) μ_− lands in [−T,T]. It is not in the corpus. It contradicts nothing:
   Corollary 1.1(i) is a lower bound for a mean value, and 𝔞^{Z} is not 𝔞.
7. *Does it smuggle in zero information?* No. Zeros of Z_X anywhere are irrelevant. Only poles in Re s ≥ ½ would break Lemma 1. ✓
8. *Overclaim check.* Theorem 1 is not a statement about λ_A. Theorem 1″(a) shows it holds for falsifiers. No column of (R) is moved for
   the sign step.

## 6. Compliance and bookkeeping
| clause | status |
|---|---|
| (R)(1) exact Λ | uses only the gap of the comb's exponential and Γ_ℝ; holds for every FE comb (Theorem 1″) — ✗ as sign step |
| (R)(2) Euler × FE jointly | ✓ (gap × phase identity × pole) |
| (R)(3) non-linear | ✓ (weight |Z_X|² = exp of the comb; Plancherel positivity of a support, not C–S on a linear identity) |
| (R)(4) no zero information | ✓ |
| (R)(5)–(9) | not applicable: no claim about λ_A |
| (R)(10)–(11) | ✗: FE-class generic (Theorem 1″), survives O10, O12 |
| (P1)–(P6) | (P1), (P4), (P6) ✓; (P3) ✗ (reads only the comb + FE); (P5) ✗ within the FE class |
Index entry proposed: "Hardy-amplitude transfer (weighted window form 𝔞^{Z}_T ≥ 2Tρ_F on P_T): PROVED tool, FE-class generic, no sign for D".
No YES→NO move proposed for (R). New fact for the campaign: **the D-defect lives where |ζ/Z_{<X}| < 1**, in particular on the central cell.
