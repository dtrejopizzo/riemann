# INV_K_001 — Divisor gauge vs. the J4 request: ζ is a universal carrier; finite gauges never certify (track K)

Track K.

Notation: Paper 46 (04-papers/46-row-d-sign-radial-intersection-form/main.tex) and INV_H_001 §3 (s_φ, Q_φ, a_φ, N = e^{2T}), INV_J_001 (O_6, a_P, J4).
No numerics used.

## 0. Corpus / index check
- ROUTES-TRIED-INDEX: G3D-159 (mollifiers, DEAD, DH/Epstein), Levinson/Conrey (literature, proportions), L2_030/031
  (Ramanujan components), EI_002 / CA_C_007 (Poisson on ℤ, Euler–Maclaurin), P149 pencil (DEAD); phase 194 H1/H3, J3/J4;
  AUDIT_194_2 (H residue = REF-D; infinite φ = mollifier retry).
- **Scope / new reason.** Nothing here retries a mollifier: §3 is a NO-GO *for the complementary class* (absolutely convergent
  gauges, in particular all finite φ), i.e. it proves that the only gauges that could certify are the indexed DEAD ones. The
  H residue (q ≥ 2 symbol > 0.45) is not targeted (REF-D per audit). The AFE/Riemann–Siegel is examined only for whether it
  yields a certificate inequality (§2): it does not.

## 1. Theorem K1 — ζ(½+iτ) is a universal carrier, not an input (PROVED)
(a) Gauge invariance. For any two admissible gauges φ, φ′ the Toeplitz forms ∫|F̂|²s_φ and ∫|F̂|²s_φ′ coincide on 𝒫_T∩𝒟_T
(both = 𝔞_T(F), H1). So the gauge is invisible to the Toeplitz question; it only affects *sufficient* criteria, of which the
one in H1(ii) is pointwise: λ_A(T) ≥ inf_τ s_φ.
(b) Universality. Let b be any real comb on the window n < N and put c := μ∗b on n < N (Möbius inversion, exact). Then for any
extension ψ of c beyond N with finite support, Σ (1∗ψ)(n)n^{−s} = ζ(s)Q_ψ(s), Q_ψ = Σψ(d)d^{−s}, and the window form of b has
symbol m − 2Re[ζ(½+iτ)Q_ψ(½+iτ)] (proof of H1 verbatim). Hence *every* comb, Λ or not, is written with the same factor ζ(½+iτ).
(c) O_6. For a_P = Λ·1{p ≥ P}: Σ a_P(n)n^{−s} = −ζ_P′/ζ_P with ζ_P = ζ·E_P, E_P = Π_{p<P}(1−p^{−s}). Its divisor gauge is
ζ_P·Q^{(P)} = ζ·(E_P Q^{(P)}), and E_P Q^{(P)} is again a Dirichlet polynomial. So O_6 changes ζ to ζE_P, but E_P is absorbed
into the polynomial: the symbol of a_P is m − 2Re[ζ·Q̃], same ζ, with Q̃ differing from Q_Λ in its window coefficients
(μ∗a_P vs. μ∗Λ = −μ log on d < N).
**Answer to task (1).** s_φ is not sparse-stable, but only through the window coefficients of Q (i.e. through Λ|_{n<N}, the
trivial non-sparse-stability of 𝔞_T itself). The FE content of ζ(½+iτ) is shared by a_P and by every window comb; it does not
distinguish Λ from the O_6 falsifier. The divisor gauge is therefore **not** the object J4 asks for: its FE part is a carrier,
its arithmetic part is the window vector (REF-D as a whole, consistent with AUDIT_194_2).

## 2. Approximate functional equation / Euler–Maclaurin (task 2; PROVED, negative)
For |τ| ≲ 2.1 the Hardy–Littlewood AFE has lengths x, y with 2πxy = |τ| < 1: degenerate. The usable finite expression is
Euler–Maclaurin (CITED, Titchmarsh §2.1/(4.2)): for K ≥ 1, ζ(s) = Σ_{n<K} n^{−s} + K^{1−s}/(s−1) + ½K^{−s} + R_K(s),
|R_K(½+iτ)| ≤ |s(s+1)|K^{−3/2}/12·(1+o(1)). Multiply by Q_φ (finite, support ≤ D). Each term n^{−s}d^{−s} has cosine transform
at log(nd); the K^{1−s}d^{−s} and ½K^{−s}d^{−s} terms sit at u ≥ log K; R_KQ_φ is smooth with Fourier mass concentrated at
u ≥ log K. Taking K ≥ N, on 𝒫_T (Re c_F supported in (−2T,2T)) everything at u ≥ 2T is invisible and the polar factor
1/(s−1) reproduces ρ_{Q(1)}; the Toeplitz form collapses to the truncated explicit formula, i.e. 𝔞_T (window-collapse, H §1).
So Riemann–Siegel/EM gives a restatement, never a certificate inequality: any inequality obtained from it must be a pointwise
(or slack-Toeplitz) bound on s_φ, and §3 shows pointwise bounds fail for every non-mollifier gauge.

## 3. Theorem K2 — finite (indeed absolutely convergent) gauges never certify, at any T (NO-GO, PROVED with CITED core)
**Class 𝓖_ac.** Gauges φ with φ(d) = 1 for d < N, T > ½log 2, and Σ_d |φ(d)|(log d)d^{−1/2} < ∞ (contains every finite φ).
**Theorem.** For every φ ∈ 𝓖_ac: inf_τ s_φ(τ) = −∞. Hence the divisor-gauge certificate λ_A(T) ≥ inf s_φ is void for every φ in
𝓖_ac at every T; no T beyond ½log5 (or any T) is reached by this family.
*Proof.* Put G = ζQ_φ, G_0 = G − Q_φ(1)/(s−1) (entire in σ ≥ ½ after removing the pole; Q_φ is bounded and continuous on
σ ≥ ½ by absolute convergence). Suppose inf s_φ > −∞, i.e. Re G(½+it) ≤ ½m(t) + C ≤ ½log(|t|+2) + C′ (m(t) = log(|t|/2π)+O(1/t²),
CITED Stirling). On σ = ½, Re[Q(1)/(s−1)] = −½Q(1)/(¼+t²) is bounded; on σ = 2, G is bounded. u := Re G_0 − ½log|s+2| − C″ is
subharmonic on the strip ½ ≤ σ ≤ 2, ≤ 0 on both edges, and of finite order (|ζ| ≪ |t|^{1/2}, Q bounded). Phragmén–Lindelöf for
subharmonic functions (CITED) ⇒ u ≤ 0 inside: Re G ≤ ½log|t| + O(1) on the strip, |t| ≥ 2. Borel–Carathéodory on discs
centred at 3/2+it with radii R = 1, r = 1−δ gives |G(σ+it)| ≪_δ log|t| for σ ≥ ½+δ.
Now Q(σ) (σ real) is real-analytic on σ > ½ and not identically 0 (else ζQ ≡ 0, but its coefficient at n = 2 is
a_φ(2) = Λ(2) = log 2 since 2 < N). Fix σ ∈ (½,1) with Q(σ) ≠ 0 and δ < σ−½. Titchmarsh Thm 8.12 (CITED, unconditional):
ζ(σ+it) = Ω(exp((log t)^{1−σ−ε})); its proof selects t by Dirichlet's simultaneous approximation so that ‖t log p/2π‖ is small
for all p ≤ X with X → ∞. For such t, d^{−it} → 1 uniformly for every X-smooth d, so the finite part of Q (support ≤ X) satisfies
Q_X(σ+it) → Q_X(σ), and the tail Σ_{d>X}|φ(d)|(log d)d^{−σ} → 0. Hence |G(σ+it)| ≥ ½|Q(σ)|exp((log t)^{1−σ−ε}) along a sequence
t → ∞, contradicting |G| ≪ log t. ∎
(The adaptation of 8.12 is only the observation that Dirichlet alignment of all p ≤ X aligns every X-smooth d; label PROVED
modulo this one-line check, core CITED.)
**Exact obstruction.** A certifying gauge must satisfy |ζ(s)Q_φ(s)| ≪_δ log|t| on σ ≥ ½+δ for every δ, i.e. Q_φ must cancel the
Ω-growth of ζ on the whole strip — a mollifier in the strict sense, with Σ|φ(d)|log d·d^{−1/2} = ∞. That class is G3D-159
(DEAD); it is not reopened here (no new reason).
**Slack-Toeplitz variants (task 3).** Adding to s_φ any function whose Toeplitz form on 𝒫_T vanishes (exterior measures, incl. the
two Tate/polar directions) is the general dual-certificate problem (thm:Z), REF-D; restricted to divisor-shaped exteriors it is
𝓖_ac (void by K2) or the mollifier class (DEAD).

## 4. Self-check
- thm:shape (B″): K1(b) shows the ζ factor is common to every comb — confirms H1 carries no sign. K2 is a NO-GO, not a sign claim.
- Class declared: 𝓖_ac (pointwise divisor-gauge certificates). Falsifier not needed (impossibility proof).
- No partial positivity obtained; ½log5 range unchanged.

## 5. Verdict
PROVED: K1 (gauge invariance; ζ universal carrier; O_6 absorbed into the polynomial ⇒ divisor gauge ≠ J4 object). PROVED (core
CITED Titchmarsh 8.12 + PL + Borel–Carathéodory): **K2 NO-GO — no absolutely convergent (in particular no finite) divisor gauge
certifies at any T**; upgrades INV_H_001 H1(iii) from ARGUED to PROVED. AFE/EM: restatement only (§2). Only remaining divisor
gauges = mollifiers (G3D-159, DEAD). Residue: none new; J4's request (FE-coupled, non-sparse-stable input) remains OPEN and is not
met by ζ(½+iτ), since ζ is shared by all window combs.
