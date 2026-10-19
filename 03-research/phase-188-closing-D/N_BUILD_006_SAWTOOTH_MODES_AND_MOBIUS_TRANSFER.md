# N_BUILD_006 — Sawtooth modes of (Ω_EM): the additive half is uniformly bounded; the whole sign sits in Z^{−1}

Pen and paper. Notation of N_BUILD_005: 𝔄_T, Z = Z_{½} = M + B, M = ½δ₀ + e^{u/2}du|_{(0,2T)},
B = Euler–Maclaurin (sawtooth) remainder; f := Re c_F on [0,2T), F ∈ P_T ∩ H¹_0 real, ‖F‖ = 1.

## Corpus check
grep "Euler–Maclaurin|sawtooth|Poisson|Voronoi|S_N − C_N|peine entero|Z_N" whole corpus + MAP_D + grid.
- **phase 170 (audited in R184_002 §1): S_N = Σ n^{−½}τ_{log n} (integer comb), C_N (continuous polar), Z_N = S_N − C_N
  "discrepancia Euler–Maclaurin"; R170_884–888 "puerto EM": exact identities without sign, classified W12; grid W4
  ("el sawtooth es el comb de (PC)"). R184_002 table: the EM chain is generic in the comb; Beurling DMV satisfies
  Λ_B*1 = log_B exactly, so the chain does not distinguish; what remains is Z_N, classed W4 + integrality.**
- R161_005: Poisson–Chebyshev port, exterior term, no sign. R164_201: Bessel lower bound against sawtooth family.
- L2_BUILD_011 row 4: Beurling (Euler product + Λ*1 = log without ℤ-integrality) KILLED.
**Consequence for (Ω_EM):** N_BUILD_005 §4 is the 𝔄_T (algebra, log-derivative) version of the phase-170 EM split;
the object is NOT new as a split. What is new below: (1) the explicit mode analysis with a T-uniform bound for the
additive half; (2) the exact transfer showing where the sign lives, and the cost of any termwise route. No phase-170
memo does either (they stayed at operator identities).

## 1. The additive half (PROVED; NEW as a T-uniform statement in this frame)
For h(x) := x^{−½} f(log x) on [1, N]:
 ⟨B, f⟩ = Σ_{1≤n<N} h(n) − ∫₁^N h − ½h(1) = −∫₁^N ({x} − ½) h′(x) dx  (EM, f(2T) = 0),
and with {x} − ½ = −Σ_{k≥1} sin(2πkx)/(πk) the k-th mode is
 β_k := (1/πk)∫₁^N sin(2πkx)h′(x)dx = (1/(2π²k²))[cos(2πk)h′(1) − cos(2πkN)h′(N) + ∫₁^N cos(2πkx)h″(x)dx].
**Theorem 1.** |⟨B, f⟩| ≤ (1/12)(|h′(1)| + |h′(N)| + ‖h″‖_{L¹(1,N)}) ≤ C(1 + ‖F′‖²), C absolute, uniformly in T.
*Proof.* Σ 1/(2π²k²) = 1/12. h′(x) = x^{−3/2}(f′ − ½f)(log x), h″ = x^{−5/2}(f″ − 2f′ + ¾f)(log x); |f| ≤ 1,
|f′| ≤ ‖F′‖ (as in prop:wit-cheb), |f″| ≤ ‖F′‖² (f″ = −Re c_{F′} for F ∈ H¹_0... in distributional sense; c_{F′}
bounded by ‖F′‖²), and ∫₁^∞ x^{−5/2}dx·x = ∫ e^{−3u/2}du finite. ∎
Stationary phase: the phase 2πk e^u has derivative ≥ 2πk on [0,2T]: no stationary point; this is why every mode
decays like k^{−2} against the band-limited f. **The integer comb has exponent-½ (indeed O(1)) fluctuation against
c_F, unconditionally, uniformly in T.** Both N_BUILD_003 modifications are irrelevant here (B does not see Λ).

## 2. Exact transfer to the Möbius comb (PROVED)
In 𝔄_T: −∂_s log Z = Z^{−1} * L, L := −∂_s Z|_{½} = Σ_{n<N} (log n) n^{−½}δ_{log n} = L_M + L_B (EM split of the
log-weighted integer comb, L_M = u e^{u/2}du, L_B its sawtooth remainder, bounded as in §1 with h ↦ (log x)h).
Pairing: ⟨Z^{−1}*ν, f⟩ = ⟨ν, f^μ⟩, f^μ(u) := Σ_{d<N} μ(d)d^{−½} f(u + log d) (the **Möbius-transported test**).
Hence the comb term of the window form is
 Σ_{n<N} v_n f(log n) = 2⟨L_M, f^μ⟩ + 2⟨L_B, f^μ⟩,
both terms exact. The polar main term 2e^{u/2} (N_BUILD_001) is contained in 2⟨L_M, f^μ⟩ (via Z^{−1}*L_M =
M^{−1}*L_M − M^{−1}*B*Z^{−1}*L_M; M^{−1}*L_M carries the pole).

## 3. Termwise cost (NO-GO for termwise bounds, PROVED)
By Theorem 1 applied to each shifted test, |⟨L_B, f(·+log d)⟩| ≤ C T(1+‖F′‖²) (extra log factor from log n), so the
termwise bound of ⟨L_B, f^μ⟩ is ≤ C T(1+‖F′‖²) Σ_{d<N} d^{−½} ≍ T e^{T}. Any bound of (Ω_EM) obtained mode-by-mode and
divisor-by-divisor loses e^{T}; the cancellation needed is in Σ_d μ(d)d^{−½}g(log d) for smooth g = the sawtooth
response — a smoothed Mertens sum at exponent ½. So **(Ω_EM) ⟺ (Ω_μ)**: a signed/O(1) bound for the Möbius
transport of the additive response, at exponent ½ (the multiplicative half). The additive half is fully controlled
(§1); the sign is entirely in Z^{−1}.

## 4. Stability of the reduced object
(Ω_μ) uses μ on [1,N): the Dirichlet inverse of the all-ones comb on ℤ-positions. Tail deletion of Λ changes Z^{−1}
(it becomes Π_{p∈S}(1 − p^{−½}δ_{log p}) — finite μ-support), ε-rescaling makes Z^{−1−ε}; both change (Ω_μ). Beurling
(L2_011 row 4) changes the positions log n → log n_B, where §1 fails (no sawtooth of period 1 in x): §1 is exactly where
ℤ-integrality enters. So (Ω_μ) + §1 escapes W-tail, ε-rescaling and Beurling by construction (integrality in §1,
multiplicativity and exactness in Z^{−1}). It is NOT shown to escape W4 (orientation): §1 is a two-sided bound, the
sign must come from (Ω_μ).

## Self-review
1. §1: f″ bound — c_F″ = −c_{F′}·(sign) requires F ∈ H¹; for F ∈ P_T ∩ D_T only, use F ∈ H¹_0 dense subset and state
the bound for such F. Accepted with that scope. EM boundary: f(2T) = 0 and h(N) = 0 — correct; ½h(1) term matches
M's ½δ₀ — correct.
2. Theorem 1 "new": the boundedness of the integer-comb discrepancy is classical (EM); the novelty is only its
T-uniform form against c_F in this frame. Downgrade: PROVED, elementary, low novelty.
3. §2: ⟨Z^{−1}*ν, f⟩ = ⟨ν, f^μ⟩ is the adjoint of convolution in 𝔄_T, valid since f vanishes beyond 2T. Correct.
4. §3: equivalence (Ω_EM) ⟺ (Ω_μ) is a renaming (exact identity), ARGUED as "where the difficulty sits". Mertens at
exponent ½ is of the same strength as the original target; no gain claimed.
5. Corpus overlap with phase 170 is large; recorded.
No sign contact; no negative value.

## Next construction
(Ω_μ) with sign: the two halves are coupled by Z*Z^{−1} = δ₀ in 𝔄_T, i.e. (M + B)*Z^{−1} = δ₀. Since §1 bounds B
uniformly, write Z^{−1} = M^{−1} − M^{−1}*B*Z^{−1} and look for a positivity-preserving structure of the resolvent
map ν ↦ M^{−1}*B*ν on the cone of autocorrelations (M^{−1} is an explicit Volterra resolvent; B a sawtooth): if
M^{−1}*B were a contraction in a norm in which c_F-pairings are controlled, (Ω_μ) would follow. Test first whether
‖M^{−1}*B‖ < 1 in a weighted Beurling norm ∫e^{−au}d|ν| (a > ½): a pen-and-paper computation.

## Addendum — the contraction test (done, pen and paper): NO-GO (PROVED)
M = ½δ₀ + e^{u/2}du has Laplace transform (z+½)/(2(z−½)), so **M^{−1} = 2δ₀ − 2e^{−u/2}du** (exact, explicit).
Weighted norm ‖ν‖_a = ∫e^{−au}d|ν| is submultiplicative. ‖M^{−1}‖_a = 2 + 2/(a+½); ‖B‖_a ≤ ‖Z−δ₀‖_a + ‖M−½δ₀‖_a + ½
= (ζ(½+a) − 1) + 1/(a−½) + ½ (a > ½). The product is < 1 only for a bounded below by an absolute a₀ > ½ (as a → ½⁺
both ζ(½+a) and 1/(a−½) blow up). For such a the Neumann series converges, but the pairing costs
|⟨ν, f⟩| ≤ ‖ν‖_a sup_u |f(u)|e^{au} ≤ e^{2aT}‖ν‖_a: a loss e^{2aT} ≥ e^{T}. This is the half-plane of absolute convergence
of 1/ζ, not exponent ½. NO-GO for "contraction of M^{−1}*B in a Beurling weight"; any working norm must be
non-absolute (cancellation-sensitive), e.g. built from the autocorrelation cone itself.
