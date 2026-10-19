# LEMMA_AINF_001 — Lemma A∞ with explicit constants (phase 204s)

Result with no Λ and no comb: negative inertia of the archimedean form alone on L²(−T,T).
Pure mathematics; numerics only as a check (NUMERICAL).

## 0. Summary

**Theorem A∞ (PROVED).** Let 𝔪_T(F) = C₀‖F‖² + Lev(c_F) be the archimedean form of P47 eq:Aform with v ≡ 0
(no comb, no polar term) on L²(I_T), I_T = (−T,T). For every t₁ ∈ (0, t₀] (t₀ = zero of m) and every
integer N ≥ 1 with πN/(2T) < t₁,

  n₋(𝔪_T) ≥ N,  and moreover λ_N(𝔪_T) ≤ −B(t₁) · (t₁² − (πN/2T)²) < 0,  B(t₁) := φ′(t₁²) > 0.

With t₁ = t₀: **n₋(𝔪_T) ≥ N(T) := #{k ∈ ℕ_{≥1} : k < 2Tt₀/π} = ⌈2Tt₀/π⌉ − 1**, and by sectors
**n₋(𝔪_T|ev) ≥ ⌈N(T)/2⌉, n₋(𝔪_T|odd) ≥ ⌊N(T)/2⌋**. Asymptotically N(T) = (2t₀/π)T + O(1) ≈ 4.0042·T.
The error term is exactly ≤ 1 (no log c, no o(1)): the proof does not use Landau–Pollak–Slepian.

Single numerical input: t₀ = 6.289835988… (NUMERICAL, 30-digit mpmath; certifiable with interval arithmetic).
For the entirely PROVED version, any t₁ with m(t₁) ≤ 0 certified suffices; t₁ = 3 is elementary (§3).

**Corollary C (PROVED).** If 𝔄 = 𝔪_T + R with R a bounded symmetric form (comb, pole, finite rank…), then
n₋(𝔄) ≥ #{j : μ_j(R_N) < δ_N}, R_N = compression of R to the Dirichlet space E_N, δ_N = B(t₀² − (πN/2T)²). In
particular H1⁺ (n₋(𝔄_ev) ≤ 1) requires n₊(R^ev_N) ≥ ⌈N(T)/2⌉ − 1 on an explicit space of dimension ⌈N(T)/2⌉.

NUMERICAL check (Legendre Galerkin, N_basis = 48): n₋(𝔪_T) = N(T) **exactly** at T ∈ {½log3, 1, ½log15, 2, 3},
and by sectors = (⌈N/2⌉, ⌊N/2⌋). The bound appears to be optimal; the upper bound remains OPEN.

## 1. Corpus check (index, grid, crossword)

grep in `05-meta-and-planning/ROUTES-TRIED-INDEX/` (occurrence totals): "Lemma A∞" 1, "n₋ → ∞" 1, "archimedean alone" 1,
"6.29" 6, "6.2898" 3, "Szegő" 4, "eigenvalue count" 0, "Dirichlet" 25 (all in other senses: Dirichlet series,
Dirichlet problem of other lemmas), "concav" 4 (Guerra/ASS interpolation, unrelated).
The only entry is H1_TRACT_001 (phase 204r): qualitative Lemma A∞ (n₋ → ∞, tests φ_L·cos, φ_L·sin, PROVED) and the
quantitative version "≈ 4T" ARGUED via Landau–Pollak–Slepian. **New and explicit reason (not a retry):** this memo
does not reopen any route toward D; it quantifies a lemma already PROVED with a different technique (tangent of the
concave Bernstein function + Dirichlet eigenfunctions) that replaces the ARGUED prolate argument with a proof with an
exact constant. No closed route is being retried.

## 2. Conventions (verified against P47)

- P47 l.106: I_T = (−T,T), F ∈ L²(I_T) extended by zero; c_F(u) = ∫F(x+u)\overline{F(x)}dx, support in [−2T,2T].
- P47 lem:K, eq:m: K(u) = 2e^{3u/2}/(e^{2u}−1),
  m(τ) = Re ψ(¼ + iτ/2) − log π = C₀ + ∫_0^∞ (1 − cos τu) K(u) du, C₀ = ψ(¼) − log π = −5.3721834…
- P47 thm:A, eq:Aform (proof): (1/2π)∫ m(τ)|F̂(τ)|² dτ = C₀‖F‖² + Lev(c_F), Lev(Φ) = ∫_0^∞ (Φ(0) − Re Φ(u))K(u)du,
  with Plancherel ‖F̂‖² = 2π‖F‖² (convention F̂(τ) = ∫F(x)e^{−iτx}dx). Define
  **𝔪_T(F) := C₀‖F‖² + Lev(c_F) = (1/2π)∫ m|F̂|²**, i.e. 𝔞_T with v ≡ 0. It is finite exactly when
  ∫ log(2+|τ|)|F̂|² < ∞ (thm:A); its domain contains H¹₀(I_T).
- P47 thm:S(i): m(τ) = C₀ + φ(τ²), φ(x) = Σ_{k≥0} x / (a_k(x + 4a_k²)), a_k = k + ¼, φ completely Bernstein.
- Sectors: ev/odd = F(−x) = ±F(x); 𝔪_T commutes with reflection (m even), so n₋ adds up by sectors.
- Constants from AUDIT_204_H1MINUS_001 (C₀, K, tail thm:S(iii)) match the ones used here.

## 3. Inputs

**(I1) Concavity (PROVED).** φ is concave on [0,∞): each summand x ↦ a_k^{−1} x/(x + 4a_k²) has second
derivative −8a_k/(x+4a_k²)³ < 0, the series converges locally uniformly with derivatives (summands O(k^{−3}),
derivatives O(k^{−3})). Moreover φ′(x) = Σ_k 4a_k/(x + 4a_k²)² > 0 (m strictly increasing for τ ≥ 0, PROVED).
Consequence (tangent of a concave function): for all x₁ ≥ 0 and all x ≥ 0,

  φ(x) ≤ φ(x₁) + φ′(x₁)(x − x₁),  i.e.  m(τ) ≤ m(t₁) + B(t₁)(τ² − t₁²),  B(t₁) := φ′(t₁²).

This is the key observation: the logarithmic tail of m is dominated by a parabola, whose quadratic form is
‖F′‖² — controllable exactly on H¹₀ with no spectral-leakage estimate at all.

**(I2) The zero t₀.** m(0) = C₀ < 0, m strictly increasing on [0,∞) and m(τ) → +∞ (≈ log(τ/2π)), so there is a
unique t₀ > 0 with m(t₀) = 0, m < 0 for |τ| < t₀. Value: t₀ = 6.28983598883690… (NUMERICAL, mpmath dps = 30,
findroot on Re ψ; `LEMMA_AINF_001_data/out.txt`). Constants: B(t₀) = φ′(t₀²) = 0.012665242526…;
m(6.28) = −0.0015683…, m(3) = −0.744244…
Status: the number t₀ is NUMERICAL (certifiable by intervals: ψ(¼) = −γ − π/2 − 3log 2 exact, φ as a series
with remainder ≤ x/(4(M+¼)²) after M terms). **Elementary PROVED version with t₁ = 3:** φ(9) ≤ Σ_{k<M} … + 9/(4(M+¼)²)
and with a modest M the bound gives m(3) < −0.7 < 0 by hand; everything that follows holds with t₁ = 3 instead of t₀
(it loses the factor 3/t₀ in the slope: N ≈ 1.91·T). Label recommendation: the theorem is PROVED for every t₁ with
m(t₁) ≤ 0; the constant 2t₀/π ≈ 4.0042 is PROVED-modulo-numerical-certification of t₀ (margin 10⁻²⁷).

**(I3) Dirichlet basis (elementary).** e_k(x) = T^{−1/2} sin(πk(x+T)/(2T)), k ≥ 1, is an orthonormal basis of L²(I_T)
contained in H¹₀(I_T), with ⟨e_k′, e_l′⟩ = (πk/2T)² δ_{kl}. Parity: e_k(−x) = sin(πk − πk(x+T)/2T)/√T =
(−1)^{k+1} e_k(x): **k odd ⇒ even, k even ⇒ odd.** For F ∈ H¹₀(I_T), the extension by zero lies in H¹(ℝ) and
(1/2π)∫ τ²|F̂|² = ‖F′‖².

**(I4) Min–max for forms.** If q is a closed form bounded below (𝔪_T ≥ C₀‖·‖²) and q(F) < 0 for
every F ≠ 0 in a subspace V ⊂ dom(q) of dimension N, then q has at least N negative eigenvalues (n₋ := sup of
dimensions of subspaces where q < 0, which coincides with the number of negative eigenvalues with multiplicity).
Moreover λ_N(q) ≤ max_{F∈V,‖F‖=1} q(F). Standard (Reed–Simon IV, XIII.1; CITED).

## 4. Theorem A∞ and proof

**Theorem A∞.** Let t₁ ∈ (0, t₀] (or any t₁ > 0 with m(t₁) ≤ 0), B = φ′(t₁²) > 0, and E_N = span{e_1,…,e_N}.
For every F ∈ E_N,

  𝔪_T(F) ≤ B Σ_{k=1}^N ((πk/2T)² − t₁²) |⟨F,e_k⟩|² + m(t₁)‖F‖².   (★)

Consequently, if πN/(2T) < t₁:
(a) 𝔪_T ≺ 0 on E_N, with 𝔪_T(F) ≤ −δ_N ‖F‖², δ_N := B(t₁² − (πN/2T)²) − m(t₁) > 0;
(b) n₋(𝔪_T) ≥ N and λ_N(𝔪_T) ≤ −δ_N;
(c) by sectors, with E_N^ev = span{e_k : k ≤ N odd}, E_N^odd = span{e_k : k ≤ N even}:
    n₋(𝔪_T|ev) ≥ ⌈N/2⌉, n₋(𝔪_T|odd) ≥ ⌊N/2⌋, with the same margin δ_N.
Taking t₁ = t₀ and N maximal: **N(T) = ⌈2Tt₀/π⌉ − 1 ≥ 2Tt₀/π − 1**, so that

  n₋(𝔪_T) ≥ (2t₀/π)·T − 1,  n₋(𝔪_T|ev) ≥ (t₀/π)·T − ½,  n₋(𝔪_T|odd) ≥ (t₀/π)·T − 1,

with 2t₀/π = 4.004178… and t₀/π = 2.002089….

*Proof.* Let F ∈ E_N ⊂ H¹₀(I_T). By (I1), m(τ) ≤ m(t₁) + B(τ² − t₁²) for every τ ∈ ℝ (m even). Multiplying by
|F̂(τ)|² ≥ 0 and integrating (both sides integrable: the right one because F ∈ H¹, the left one by thm:A):

  𝔪_T(F) = (1/2π)∫ m|F̂|² ≤ (m(t₁) − Bt₁²)‖F‖² + B‖F′‖²      [Plancherel and (I3)].

With F = Σ c_k e_k: ‖F‖² = Σ|c_k|², ‖F′‖² = Σ(πk/2T)²|c_k|² (I3), which gives (★). If πN/2T < t₁, each coefficient
of (★) is ≤ B((πN/2T)² − t₁²) + m(t₁) = −δ_N < 0 (m(t₁) ≤ 0, B > 0). That is (a); (b) is (I4). For (c): 𝔪_T commutes
with reflection, E_N^ev ⊂ L²_ev and E_N^odd ⊂ L²_odd by (I3), and (a) holds on each; count the odd/even k's
≤ N. Finally, N(T) = #{k ≥ 1 : πk/2T < t₀} = ⌈2Tt₀/π⌉ − 1. ∎

**Remarks.**
1. There is no o(1) nor log c: the error is ≤ 1 (≤ 1 in each sector). The prolate heuristic (2Tt₀/π) is recovered
   with an exact constant, because the log tail of m is absorbed into ‖F′‖² and the Dirichlet eigenfunctions
   diagonalize ‖F′‖² exactly. Landau–Widom (J. Math. Anal. Appl. 77 (1980) 469–481) is not needed.
2. Uniformity across scale: δ_N is explicit; with t₁ = t₀ and N = N(T), t₀ − πN/2T ∈ (0, π/2T], so δ_N can
   be as small as B·t₀·(t₀ − πN/2T) (≤ 0.25/T, and ~0 near a jump). The negative margin per direction is O(1/T)
   near the band edge and ≈ |C₀| for small k: with N = ⌊Tt₀/π⌋ (half the band) δ ≥ (3/4)Bt₀² ≈ 0.376, uniform in T.
3. Monotone version: N(T) is non-decreasing and jumps at T_j = πj/(2t₀) = 0.24974·j; consistent with BARRIER_W_001
   (n₋ non-decreasing in T for the full form).
4. **Upper bound (OPEN / NUMERICAL):** Galerkin gives n₋ = N(T) exactly at the five T of §6; an upper bound
   n₋(𝔪_T) ≤ N(T) + O(1) would require a lower bound of m by a parabola on |τ| ≤ t₀ plus tail control (Landau–Widom
   style); it is not attempted here.

## 5. Corollary on the comb (PROVED as a necessity)

Write the full form as 𝔄 = 𝔪_T + R, with R a bounded symmetric form on L²(I_T): for 𝔞_T,
R = Π_T, Π_T(F) = −Σ_{n ∈ N_T} v_n Re c_F(log n) (finite sum, n ≤ e^{2T}, each F ↦ c_F(log n) is a bounded form of
norm ≤ 1 — truncated translation, of infinite rank on L²(I_T)); for W_T or 𝔄_ev of H1_TRACT, R = Π_T plus the polar
terms of rank ≤ 2. Let R_N be the N×N matrix ⟨R e_k, e_l⟩ (compression to E_N) and μ_1 ≤ … ≤ μ_N its eigenvalues.

**Corollary C.** With t₁, B, δ_N as in Theorem A∞,
(i) n₋(𝔄) ≥ #{j : μ_j(R_N) < δ_N} ≥ N − n₊(R_N) ≥ N − n₊(R);
(ii) likewise by sectors with E_N^ev, E_N^odd (R commutes with reflection in every case of P47: v real, even/odd
polar terms).
*Proof.* Let V ⊂ E_N be the spectral subspace of R_N for eigenvalues < δ_N. For F ∈ V \ {0}:
𝔄(F) = 𝔪_T(F) + R(F) ≤ −δ_N‖F‖² + R_N(F) < 0 by Theorem A∞(a). Apply (I4). The second inequality: the
eigenvalues ≥ δ_N > 0 number ≤ n₊(R_N); and n₊(R_N) ≤ n₊(R) by min–max. ∎

**Honest reading.**
- **H1⁺ (n₋(𝔄_ev(T)) ≤ 1 ∀T) requires, for each T,** that the compression of the non-archimedean part to
  E^ev_{N(T)} have at least ⌈N(T)/2⌉ − 1 eigenvalues ≥ δ_{N(T)}. For T = 1: ≥ 1; T = 2: ≥ 3; T = 3: ≥ 5;
  in general ≥ (t₀/π)T − 3/2 ≈ 2.0T − 1.5. This is a finite-dimensional, falsifiable-at-each-T statement.
- **B (𝔄_odd ≻ 0) requires** n₊ ≥ ⌊N(T)/2⌋ on E^odd_{N(T)} — the whole block.
- There is no counting contradiction: the rank of each truncated translation is infinite and #contacts ≈ e^{2T} ≫ 4T;
  the corollary states how many positive directions of size ≥ δ_N the comb must produce **within an explicit space
  of dimension N(T)**, not globally. The Weyl bound in the reverse direction (n₋ ≤ n₋(𝔪) + n₋(R)) remains useless
  (WT_HALVES §3.3); this is the useful direction.
- **Epstein at T = 2 (CALIB_R4, n₋ = 2):** if that n₋ = 2 is the one for the even sector of its form 𝔄_ev, Corollary C
  gives that its non-archimedean part has n₊(R^ev_4) ≥ N^ev(2) − 2 = 4 − 2 = 2 on E^ev_4 = span{e_1,e_3,e_5,e_7};
  if it is the total n₋, n₊(R_8) ≥ 8 − 2 = 6. CONDITIONAL on the reading of CALIB_R4 (not re-verified here).
- None of this says anything about the sign of D: it is a quantitative necessity about the comb (independent of D).

## 6. NUMERICAL check (`LEMMA_AINF_001_data/check.py`, `out.txt`)

Galerkin in orthonormal Legendre of degree < 48 on (−T,T); matrix via the Lévy form
𝔪 = (C₀ + κ_T)I + ∫_0^{2T}(I − Re C(u))K(u)du, κ_T = ∫_{2T}^∞ K (thm:S(iii)), C(u)_{jl} = ∫ P_j(x+u)P_l(x)dx by
Gauss (exact), u by Gauss with u = 2Ts². Galerkin gives lower bounds of n₋ (restriction to a subspace).

| T | 2Tt₀/π | N(T) | (N^ev, N^odd) | Galerkin n₋ (tot, ev, odd) |
|---|---|---|---|---|
| ½log3 = 0.5493 | 2.200 | 2 | (1,1) | (2,1,1) |
| 1 | 4.004 | 4 | (2,2) | (4,2,2) |
| ½log15 = 1.3540 | 5.422 | 5 | (3,2) | (5,3,2) |
| 2 | 8.008 | 8 | (4,4) | (8,4,4) |
| 3 | 12.013 | 12 | (6,6) | (12,6,6) |

Exact match in all five cases (NUMERICAL). Note: T = 1 and T = 2 are at 0.004/0.008 from a jump, and even so
Galerkin sees the direction N(T): consistent with the bound being optimal.

## 7. Entry for the index (ROUTES-TRIED-INDEX)

- **LEMMA_AINF_001 (phase 204s): quantitative Lemma A∞ PROVED.** n₋(𝔪_T) ≥ N(T) = ⌈2Tt₀/π⌉ − 1 (ev ⌈N/2⌉, odd ⌊N/2⌋),
  t₀ = 6.28984 (NUMERICAL-certifiable; PROVED with any t₁, m(t₁) ≤ 0), margin δ_N = B(t₁² − (πN/2T)²) − m(t₁).
  Technique: tangent of concave φ (thm:S) ⇒ m ≤ m(t₁) + B(τ² − t₁²), Dirichlet eigenfunctions; no prolates.
  Corollary C: n₋(𝔪_T + R) ≥ #{μ_j(R_N) < δ_N}; H1⁺ requires n₊ ≥ ⌈N/2⌉ − 1 on E^ev_N. Galerkin: n₋ = N(T) exact at 5 T.
  Upper bound OPEN. Not a route toward D: a tool.

## 8. Text for P47 (English, ≤ 6 lines; after thm:A or in sec:spec)

\begin{lemma}[archimedean negative count]\label{lem:archcount} Let $t_0$ be the zero of $m$ and $B=\varphi'(t_0^2)>0$. For $N\ge1$ with $\pi N<2Tt_0$, the form $\mathfrak m_T(F)=\frac1{2\pi}\int m|\widehat F|^2$ satisfies $\mathfrak m_T(F)\le-B\big(t_0^2-(\pi N/2T)^2\big)\|F\|^2$ on $\mathrm{span}\{\sin\frac{\pi k(x+T)}{2T}\}_{k\le N}$; hence $n_-(\mathfrak m_T)\ge\lceil 2Tt_0/\pi\rceil-1$, with $\lceil N/2\rceil$ even and $\lfloor N/2\rfloor$ odd directions.
\end{lemma}
\begin{proof} $\varphi$ is concave (Theorem~\ref{thm:S}), so $m(\tau)\le B(\tau^2-t_0^2)$; integrate against $|\widehat F|^2$ for $F\in H^1_0(I_T)$ and use $\frac1{2\pi}\int\tau^2|\widehat F|^2=\|F'\|^2$, diagonal on the Dirichlet sine basis. \end{proof}
