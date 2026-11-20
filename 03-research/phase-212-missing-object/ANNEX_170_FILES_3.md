# Annex 170 — stretch 3: files R170_841 to R170_862

Reading record of phase 170, files 841–862 (842 does not exist; there are two 858 files). Notation of
the memos: window (−T,T), N ≥ e^{2T}, P = P_T (window), Q = I−P (exterior), Π primitive, R_T = P−Π
(Tate block, rank two), S_N = Σ_{m≤N} m^{-1/2}τ_{log m}, L_M = Σ_{d≤M} Λ(d)d^{-1/2}τ_{log d},
K_N = Σ_{k≤N}(log k)k^{-1/2}τ_{log k}, H_{M,N} = L_M S_N − K_N, C_N polar continuum, Z_N = S_N − C_N,
dilation U_r f(t) = r^{-1/2}f(t/r), Ḃ = d/dr (U_r^{-1}BU_r)|_{r=1}, τ̇_a = −a∂_tτ_a. "VIR–LB" is the
inequality 𝒱_{Λ,T}(F) ≤ 0 on the radical N_T^ε = {F ∈ ker H_T : JF = εF} of a hypothetical first-contact
window, with 𝒱 = (1/2π)∫τm'(τ)|F̂|² − Σ_{n<e^{2T}} 2Λ(n)n^{-1/2} log n c_F'(log n) +
2Re⟨F, t r_F'⟩. The whole chain 841–862 works under that first-contact hypothesis (argument by
contradiction on the minimal window), not on a global identity of type (G).

Cross-check against the terrain not excluded by round 1 of 212:
(T1) continuous squares with arithmetic in the index/dilation weights; (T2) divisor incidence Gram
E diag(Λ) Eᵀ; (T3) Σ_{d|n}Λ(d) = log n converted into a quadratic bound; (T4) common residue:
mixed Poisson–Chebyshev pairings (H_{M,N}, E_N) as Σ_{k>N} h(k)|ℓ_k(F)|², h ≥ 0.

---

## 1. Entries by file

### R170_841 — Derivative of the finite hyperbola, first-order no-go and oriented residue

**Object.** Real weight a with a(1)=0; L_M^a, H^a_{M,N} = L_M^a S_N − K_N = Σ_{k≤MN} q^a_{M,N}(k)k^{-1/2}τ_{log k},
q^a(k) = Σ_{dm=k, d≤M, m≤N} a(d) − 1_{k≤N} log k. Scale Ward identity (Thm. 3.1):
Ḣ^a = −Σ q^a(k) log k k^{-1/2}∂_tτ_{log k}; L̇S + LṠ − K̇ = Ḣ; Π_{≤N}Ḣ^a = −Σ_{k≤N} δ_a(k) log k
k^{-1/2}∂_tτ_{log k}, δ_a = a∗1 − log; for Λ the block k ≤ N vanishes and what remains is
Ḣ^Λ = −Σ_{N<k≤MN} h_{M,N}(k) log k k^{-1/2}∂_tτ_{log k}, h ≥ 0 (3.8). Antisymmetric channel
𝒜_{M,N} = L̇_M S_N − L_M Ṡ_N with complete-fibre coefficient
β_Λ(k) = Σ_{d|k}Λ(d) log(d/(k/d)) = 2Σ_{d|k}Λ(d)log d − (log k)². Decomposition
2L̇S = Ḣ + K̇ + 𝒜 (4.5). Variance Σ_Λ(k) = Σ_{d|k}Λ(d)(2log d − log k)² ≥ 0 with
|β_Λ(k)|² ≤ (log k)Σ_Λ(k) (Cauchy–Schwarz with the probability Λ(d)/log k). Explicit derivative of the
polar continuum Ċ_N (5.5), with boundary face −(log N)√N f(t+log N). Ledger (5.8): interior β ⊕
incomplete hyperbola k>N ⊕ Ċ_N ⊕ [P_T,Z_N] ⊕ Tate.

**Claims.** Declares PROVED: synchronized derivative (3.4)–(3.8); defect for altered weight and
for DH with ordinary comb (3.9); separation of legs and β_Λ; Σ_Λ and the bound; Ċ_N; no-go of the class
𝒞_fib^{(1)} (Thm. 6.1). Declares FALSE: uniform sign of β_Λ (β(p^j) = j(log p)² > 0, β(12) < 0 by
(4.7)); that the variance orients β; sign of the virial independent of the source (§6.1: family
F_ξ = φ cos ξt with c'_{F_ξ} ≍ ξ of both signs, archimedean term O(1)). What the text sustains:
agrees; the no-go 6.1 is a class argument (qualitative, "condition 5" is defined as not introducing a
new physical identity), correct within that definition.

**Where it stopped.** The only first-order quantity that survives (β_Λ) changes sign; the
positive completion is second order (even under inversion of the leg difference) and does not orient
a first moment. Möbius returns to Λlog = μ∗log² − Λ∗Λ (Selberg no-go, paired with c_F', without
sign). The tail h ≥ 0 lives on ∂_tτ (correlation derivative) and gives no sign. Left OPEN: an "antisymmetric
boundary Green law" (7.1) orienting 𝒜 with the ledger (5.8).

**Later correction.** R170_843 continues it (reassembles β into a positive Hankel form).

**T1–T4.** T1: no (only one square per fibre, Σ_Λ). T2: partial — groups by fibres k = dm with weight
Λ(d) (incidence), but not the Gram factorization; diagonalization by fibres is declared
forbidden (it changes the physical Gram). **T3: yes, directly** — converts Σ_{d|k}Λ(d) = log k into the
probability Λ(d)/log k and into the quadratic bound |β|² ≤ (log k)Σ_Λ; fails because the bound is even and does not
orient the first moment β. **T4: yes** — the tail Ḣ^Λ with k>N and h ≥ 0 is exactly the residue of the
hyperbola after using δ_Λ = 0, but it is coupled to ∂_tτ_{log k}, not to |ℓ_k(F)|²; without sign.

### R170_843 — Antisymmetric Green of the hyperbola: Laplace sign, support collision, minimal Hankel lifting

**Object.** 𝒜^raw = L̇S − LṠ and 𝒜^ren = L̇Z − LŻ = 𝒜^raw − (L̇C_N − LĊ_N); master
2L̇Z = Ḣ̃ + K̇^Z + 𝒜^ren. Truncated β_{M,N}(k) (1.8); 𝒜^raw = −Σ_{k≤MN} β_{M,N}(k)k^{-1/2}∂_tτ_{log k}.
Laplace transform K_F(a) = ∫F e^{-at}: K_{∂_tτ_{log k}F}(a) = a k^{-a}K_F(a), hence
K_{𝒜^raw F}(a) = −a B_{M,N}(s)K_F(a), s = a+½, B_{M,N} = ℓ_M σ_N' − ℓ_M' σ_N (Dirichlet Wronskian).
In the limit B_Λ(s) = ζ'' − 2ζ'²/ζ = −ζ²(1/ζ)'' > 0 for s>1. Gamma lattice a_m = 2m+½, s_m = 2m+1;
observer (𝓡_δ F)_m = e^{-a_m(T+δ)}K_F(a_m), G_δ = 𝓡_δ*𝓡_δ (Hankel). Energy
𝓔^β(F) = −Re⟨𝓡F, 𝓡𝒜^raw_{N,N}F⟩ = Σ_m a_m B_{N,N}(s_m)e^{-2a_m(T+δ)}|K_F(a_m)|² > 0.
Typed collar (6.6)–(6.8): 𝓡Π𝒜^rawΠ = −D_{β,N}𝓡Π − 𝓡(R+Q)𝒜^rawΠ.

**Claims.** PROVED: 𝒜^raw finite with all fibres; collinearity of the two routes at r=1
(2.2)–(2.3) (every alternating polarization by route is zero); compressed Green form = support
concomitant ⟨g,[P,B]w⟩ (4.2); B_Λ = −ζ²(1/ζ)''; uniform finite positivity B_{N,N}(s) > 0 for s ≥ 3,
N ≥ N_0 absolute (Thm. 5.1, by continuity and convergent tail); strict Hankel energy; typed
collar. CITED: B_Λ > 0 on all s > 1 (published theorem on strict concavity of 1/ζ on (1,∞)).
FALSE: Herm(P𝒜P) is only a boundary term; parity kills the Hermitian part; use of λ_δ after filtering
by 𝒜 or Z (4.11). Declares "FALSE": separation of weights by the isolated Gamma energy (§5.4: many altered
positive weights also give a positive Wronskian at s_m ≥ 3); "PROVED" separation in the full
half-plane for an altered weight — what the text sustains is only the example δ_2, B_{δ_2}(s) =
2^{-s}ζ(s)(log 2 + ζ'/ζ) < 0 near s=1. OPEN: physical lifting (7.3) Π G_δ 𝒜^ren Π = H_T𝒦 +
𝓑^pol + 𝓑^supp + 𝓑^Tate and (7.4).

**Where it stopped.** Passing from the signed Hankel energy to the renormalized physical operator adds
L̇C_N − LĊ_N, PZ_NQ, QZ_NP, R_T and the Tate virial, without sign; the first contact replaces the
positive overlap ⟨F_δ,E_TF⟩ with a filtered one without sign. No-go of the class 𝒞_Green^{(1)}
(Thm. 8.1): standard Green with 𝒜, compression, reflection, XF, F_δ, without a Hankel operator between legs.

**Later correction.** Header added by R170_844: (6)–(7) are only formal for small δ;
K_{C_NF}(a) = N^{a+½}/(a+½)·K_F(a), the interior observer requires δ > log N; the static factorization
is blocked by Fredholm. Thm. 5.1 and (5.18) are not affected.

**T1–T4.** **T1: yes** — G_δ = 𝓡*𝓡 is a continuous square (Laplace observation on the Gamma
lattice) with arithmetic weights a_m B_{N,N}(s_m); its sign exists but does not separate weights (§5.4) and is not
lifted to the physical form. T2: no. **T3: yes** — uses δ_Λ = 0 to rewrite β and obtain
Σβ_Λ k^{-s} = −ζ²(1/ζ)''; the sign comes from the cited concavity, not from a quadratic bound per
fibre. **T4: partial** — retains the tail Σ_{N<k≤N²} β_{N,N}(k)k^{-s} inside B_{N,N}; the synchronized
tail h ≥ 0 is kept separate.

### R170_844 — Physical lifting of the Wronskian: complete expansion, Fredholm obstruction and minimal covariant derivative

**Object.** Detector 𝒞_β = Π𝓡*D_{β,N}𝓡Π > 0; polar Wronskian 𝒫^pol_N = L̇_N C_N − L_N Ċ_N.
Domain gate (1.6a)–(1.6c): 𝓡_δ C_N bounded only if δ ≥ log N. Identity (2.4)
ΠG_δ𝒜^renΠ = −𝒞_β − ΠG_δ𝒫^polΠ. Polar symbol (3.2b)–(3.2c): K_{Ċ_NF}(a) = c_N(s)(1 − 1/(2s) − a log N)K_F,
c_N = N^s/s; π_N(s) = c_N ℓ_N[a(log N − μ_N(s)) − 1 + 1/(2s)], μ_N = −ℓ_N'/ℓ_N ≤ μ_∞(3) =: M_3 for s≥3.
Synchronized tail Θ_N(s) = Σ_{N<k≤N²} h_{N,N}(k)log k k^{-s} ≥ 0 with K_{Ḣ F}(a) = −aΘ_N K_F (4.4).

**Claims.** PROVED: (2.3), (2.4), polar symbol and Re 𝔭(F,F) > 0 after enlarging N_0 ≥ e^{M_3+1}
(3.2i); synchronized tail with positive symbol; defect for δ_a ≠ 0 / DH with ordinary comb;
necessary condition for the lifting: 𝒱 = Re 𝔭_pol on the radical (5.4); Thm. 6.1 (Fredholm
criterion: 𝒯 = H𝒦 + 𝓑 requires P_N(𝒯 − 𝓑) = 0). Consequence: (5.4) with (3.2i) would give 𝒱 > 0 on the
radical, the opposite sign — the static lifting with orientation (0.5) is REFUTED, not pending.
Static Tate block R_T𝒜Π "FALSE IN TYPE" as Tate virial (the latter depends on Π̇, §5.1).
"FORMALLY BUILT": covariant derivative ∇^PC = d/dr(Π_{rT}𝔓^ren(r)Π_{rT}) (8.1)–(8.2). OPEN: covariant
Ward–PC. What the text sustains: correct; the refutation uses the positivity of π_N, which is proved
with a valid monotone-means argument.

**Where it stopped.** The sum of support/Tate/polar blocks is tautological (3.10): no term
identifiable with the virial remains. δ cannot remain free (7.1)–(7.2): Re 𝔭 → 0 as δ → ∞.

**Later correction.** R170_846 points out that 𝔓^ren was not defined as an operator; (8.1) remains
wrongly typed until a side and a polarization are chosen.

**T1–T4.** T1: yes (same Gamma observation, now with polar symbol; positivity appears with the
sign opposite to the one required). T2: no. T3: inherits δ_Λ = 0. **T4: yes** — Θ_N(s) ≥ 0 is the tail k>N observed
as a positive multiplier in Gamma coordinates (a form Σ_m a_mΘ_N(s_m)e^{…}|K_F(a_m)|² ≥ 0), but
in the Hankel metric, not the physical one, and it does not close with the rest of the ledger.

### R170_845 — Moving Tate connection: exact computation and remaining Ward–PC gate

**Object.** Transported columns φ_∓(r,t) = e^{∓rt/2}; Gram G_T = 2[[sinh T, T],[T, sinh T]];
Π̇F = −ΦG^{-1}Φ̇*F for F primitive (1.5); by parity, b_ε = e^{-t/2} + εe^{t/2}, q_ε = 4(sinh T + εT),
ḃ_ε = t b_ε', Π̇F = −b_ε⟨ḃ_ε,F⟩/q_ε. Identity (0.1): 2Re⟨Π̇F, r_F⟩ = −2Re⟨F, t r_F'⟩ if r_F = ρb_ε.

**Claims.** PROVED: derivative of the primitive projection, rank one by parity, "Π̇ = minus
Tate virial for the complete operator". DEFINED: defect d^Tate = R_T𝔓^renF − r_F. OPEN: its
vanishing and Fourier derivative = archimedean virial.

**Where it stopped.** The port equality R_T𝔓F = r_F (0.2) remains to be proved.

**Later correction.** Header of R170_846: §4 was conditional; 𝔓 not defined; the defect (4.1)
is not defined until a carrier is chosen. (1.4)–(3.2) remain valid.

**T1–T4.** Touches none (geometry of the Tate projection).

### R170_846 — Audit of the Ward–PC carrier and transversal corpus filter

**Object.** Finite PC of Paper 47: Y = S_N A_M 𝓕 = {X,E_N} − L_M*E_N − JH_{M,N} − H_{M,N}𝓕 = Z
(equality, not a distinguished operator). Minimal Hermitian carrier 𝒲^ren = ½(S_N^ren A_M𝓕 + 𝓕A_M(S_N^ren)*);
scalar defect Δ^Tate = ω^ε − ρ_F with ω^ε = ⟨𝒲F, b_ε⟩/‖b_ε‖².

**Claims.** WITHDRAWN: application to undefined 𝔓. DEFINED: 𝒲^ren, Δ^Tate. COMPLETED: corpus
filter (eight requirements: polar Hardy residues of R161_009 are not a projection; linear limits of PC
are a tautology; compressed Tate port ≠ crossed collar; polar velocity and integer births
together; linear variation of PC coefficients is an algebraic zero (R162_305); PC squares, linear
limits and Λ∗1 = log after regularizing excluded; M/N corner anomaly; Wronskian and tail of
841–844). OPEN: WPC–Tate (4.1)/(4.2) and WPC–bulk (4.3).

**Later correction.** Header of R170_847: the carrier (1.1) is not new (anticommutators and
Hermitian powers of R161_062–064) and hermitianizes after recombining the legs; (4.1)–(4.3)
withdrawn as the preferred route.

**T1–T4.** No; it is an audit. Records that "Λ∗1 = log after regularizing" is excluded (relevant for T3).

### R170_847 — Two-parameter PC curvature before hermitianizing

**Object.** Antidiagonal derivation ∂_− = (∂_r − ∂_q)|_{1,1} with L_M(r), Z_N(q):
∂_−[L(r)Z(q)] = 𝒜^ren. Form 𝔚^−(F,G) hermitianized from ∂_−⟨F, Π_{rT}G_δL(r)Z(q)Π_{rT}G⟩ (2.2)–(2.3).
Two-scale PC (Thm. 4.1): with X_r = rX, K_N(r,q) = (r/q)Σ log n n^{-1/2}τ_{log n/q},
A_M(r) = 𝓜_r − L(r) − L(r)*, E_N(r,q) = S(q)𝓕_r − JS(q), H(r,q) = L(r)S(q) − K(r,q):
S(q)A(r)𝓕_r = {X_r,E} − L(r)*E − JH𝓕_r − H𝓕_r ∀ r,q. Jet: ∂_−K = 2K_N + K_N^{(2,∂)},
K^{(2,∂)} = Σ(log n)² n^{-1/2}∂_tτ_{log n}.

**Claims.** PROVED: ∂_−(LZ) = 𝒜^ren; Wronskian bulk inside the form (with the domain
gate); two-scale PC (the proof repeats that of PCfinite; the factor r/q is necessary for
[X_r,S(q)] = −K(r,q)). COMPUTED: jet of K. OPEN: coupling with the complete PC and archimedean virial;
Π̇/Tate cancellation against the polar residue.

**Where it stopped.** The form does not contain the archimedean term; the whole side
S(q)A(r)𝓕_r must be differentiated.

**T1–T4.** T1: yes, inherits G_δ. T4: partial (H(r,q) at two scales, without sign). T2, T3: no.

### R170_848 — PC curvature with the right Fourier removed

**Object.** Multiply the two-scale PC by 𝓕_r (𝓕_r² = I): S(q)A(r) = {X_r,E}𝓕_r − L*E𝓕_r −
JH𝓕_r − H. Curvature 𝒞 = SȦ − ṠA = SṀ − Ṡ𝓜 − 𝒜^raw − (SL̇* − ṠL*). ṁ(τ) = −τm'(τ), hence
⟨F,Ṁ F⟩ = −(1/2π)∫τm'|F̂|² (minus the archimedean term of the virial). L̇_M =
−Σ Λ(n)log n n^{-1/2}∂_tτ_{log n}; d/dr⟨F,Π_{rT}A(r)Π_{rT}F⟩ = −𝒱 under (REG) (known identity).

**Claims.** PROVED: PC without right Fourier; curvature; appearance of −𝒜^raw with the
correct orientation; Ṁ; identification of the interior jet of A with archimedean+prime. OPEN: extract Ȧ from SȦ without
inverting S_N; group the seven residues of §5.

**Where it stopped.** ⟨F,G_δSȦF⟩ cannot be replaced by ⟨F,ȦF⟩ without inverting S_N (5.1).

**Later correction.** R170_849 solves the extraction in the physical metric.

**T1–T4.** Does not touch (PC algebra); T1 only through the inherited observer.

### R170_849 — Finite causal extraction and clash between physical metric and Hankel metric

**Object.** PS_NP = P + R_{N,T}, R^{J_T} = 0 with J_T = ⌊2T/log 2⌋+1 (nilpotency by shifts
≥ log 2); B_{N,T} = (PS_NP)^{-1} = Σ_{j<J_T}(−R)^j. Exact extraction (2.2):
PȦF = BP𝒞F + BPṠPAF + BPṠQAF − BPSQȦF; at first contact PAF = r_F. Metric defect
𝔇^met = Re⟨(B* − G_δ)F, P𝒜^rawF⟩ (3.3). Modified observer G^ext = 𝓡*diag(σ_N(a_m)^{-1})𝓡 which extracts
S_N in Gamma coordinates, σ_N(a) = Σ_{n≤N} n^{a−½}.

**Claims.** PROVED: nilpotency, finite inverse, extraction (2.2), identification of ports,
positive Laplace extraction (4.1)–(4.3). FALSE IN GENERAL: equality between physical and Hankel metric
(𝓡*D𝓡 is compact; the identity is not). OPEN: MET–WARD (the difference B* − G^ext has diagonal ≤ 0 or
cancels on ker H_T); the text says that postulating it amounts to postulating the sign bridge.

**Where it stopped.** The sign of 843 lives in the Hankel metric; the exact extraction asks for the dual
metric of (PSP)^{-1}; there is no identity identifying them.

**Later correction.** R170_850 (B = PMP); R170_851 (the ports PṠP and PṠQ create atoms; only the
sum is legitimate).

**T1–T4.** **T1: yes** — two extractions: physical (loses sign) and Gamma with weights 1/σ_N (keeps sign
but produces a filtered virial). T2: partial (finite inverse of the comb). T3, T4: no.

### R170_850 — Arithmetic law of the Möbius-extracted Wronskian

**Object.** B_{N,T} = PMP with M = Σ μ(n)n^{-1/2}τ_{log n} (causality: no trajectory leaves and
returns). γ_Λ = μ∗β_Λ = −Σ_{d|n}μ(d)(log d)²: γ(p^k) = (log p)², γ(p^aq^b) = −2 log p log q,
γ = 0 if ω(n) ≥ 3 (total finite difference of a quadratic polynomial). Extracted form (4.2):
Σ_p(log p)²Σ_k p^{-k/2}Re⟨F,∂_tτ_{k log p}F⟩ − 2Σ_{p<q}log p log q Σ_{a,b}(p^aq^b)^{-1/2}Re⟨F,∂_tτ_{a log p+b log q}F⟩
+ 𝒯^cut.

**Claims.** PROVED: B = PMP, interior extraction, law γ, support ω ≤ 2, uniformity in T.
RETAINED/OPEN: cut port 𝒯^cut. OPEN: signed completion of the two-prime-base channel (a
rank-two object in the lattice of prime bases is suggested, completing the square; not claimed).
Verified: (3.4) gives −x² for r=1 and 2x₁x₂ for r=2, correct.

**Later correction.** Header of R170_851: γ = Λlog − Λ∗Λ; with W = Λlog + Λ∗Λ it returns to the
Selberg no-go; the synchronized tail is zero in low fibres; (0.2) is not a new positive completion.

**T1–T4.** T2: partial (Möbius inverse of the comb; the channel −2 log p log q suggests a quadratic
form in prime bases, not built). **T3: yes** — uses Λ∗1 = log and μ∗1 = δ; the result
coefficient by coefficient has no sign (negative crossed channel) and neither do the correlations ∂_tτ.
T1, T4: no.

### R170_851 — Selberg collision of the Möbius law and boundary atoms of the extracted port

**Object.** γ_Λ = Λlog − Λ∗Λ (via B_Λ/ζ = −𝓛' − 𝓛², 𝓛 = −ζ'/ζ); W = μ∗log² = Λlog + Λ∗Λ;
γ + W = 2Λlog. Atoms: ∂_t(Pg) = Pg' + g(−T+)δ_{−T} − g(T−)δ_T and opposite ones for Q; only
PṠ(P+Q)AF = PṠAF is legitimate. Corrected extraction (4.1): PȦF = BP𝒞F + BPṠAF − BPSQȦF; combined
port 𝒫^comb = BPṠAF − BPSQȦF.

**Claims.** PROVED: γ = Λlog − Λ∗Λ, γ + W = 2Λlog, collision with Selberg (2.2) without sign,
atoms and their cancellation in the combined port. REJECTED: identifying the synchronized tail with W
(it is zero for k ≤ N). OPEN: Tate projection of the combined port and cancellation with Π̇.

**Later correction.** R170_854 qualifies: interior W is indeed in PC, in the second jet K²; then
R170_856 shows that this W cancels with a −W from the Poisson–X block.

**T1–T4.** **T3: yes** — Selberg as a second identity on Λ; reproduces the deconvolution no-go
(W ≥ 0 paired with c_F' without sign). T4: records that the tail k>N contributes nothing in the interior.

### R170_852 — Exact Tate defect of the combined port

**Object.** h_ε = B*b_ε with PS_N*Ph_ε = b_ε; at first contact PAF = ρ_Fb_ε, QAF = ℓ_F. Coordinate
ω^comb = (1/q_ε){ρ_F⟨PṠ*Ph,b⟩ + ⟨QṠ*Ph,ℓ_F⟩ − ⟨QS*Ph, QȦF⟩}; defect
Δ^Tate = (κ^ε − 1)ρ_F + 𝓔^{ext,1} − 𝓔^{ext,2}, κ^ε = ⟨PṠ*Ph,b⟩/q_ε (comb geometry only).
Connection residue 𝔑^Tate = 2Re⟨Π̇F, Δ^Tate b_ε⟩.

**Claims.** PROVED: causal dual, (0.5), (0.6), compatibility with atoms. DEFINED: 𝔑^Tate.
OPEN: cancellation with polar + support. Falsification tests: N=1 gives κ = 0 (there is no automatic
cancellation); κ does not see Λ (the cancellation must go through the exterior residues); without exterior what remains is
(κ−1)ρ_F.

**T1–T4.** Touches none directly (port algebra).

### R170_853 — Curvature of the causal graph and exterior arithmetic mismatch

**Object.** C_{N,T} = PS*P, 𝒟_{N,T} = QS*P C^{-1}; h = C^{-1}b, q = 𝒟b = QS*Ph (S*Ph = b + 𝒟b,
causal graph). Exterior mismatch z_F = ℓ_F − ρ_F q. Decomposition (2.2):
q^Gram Δ^Tate = ρ_F 𝔎(F) + ⟨q̇^0, z_F⟩ − ⟨q, ż^0_F⟩ with 𝔎 purely causal (no Λ, no Gamma).

**Claims.** PROVED: decomposition, isolation of the causal curvature 𝔎, identification of the
residue as an exterior Wronskian. FORBIDDEN/TAUTOLOGICAL: imposing z_F = 0 (repeats L161.6, exterior
reciprocity). OPEN: law (5.1) Re(⟨q̇^0,z⟩ − ⟨q,ż^0⟩) = 0 from the two-scale PC.

**T1–T4.** T4: partial — z_F measures exactly the part of the exterior QAF not predicted by the comb; it is not
converted into a sum of squares. Otherwise: no.

### R170_854 — Graded Green law for the exterior Wronskian

**Object.** With real product (u,v) = Re⟨u,v⟩ and frozen jets ḃ^0 = PṠ*Ph, q̇^0 = QṠ*Ph,
ȧ^0 = PȦF, ℓ̇^0 = QȦF: Thm. 2.1 (h, P(SȦ − ṠA)F) + ((q̇^0,z) − (q,ż^0)) = (b,ȧ^0) − ρ(ḃ^0,b);
𝔚_bulk + 𝔚_ext = 𝔚_Tate. ℤ/2-graded realization: 𝔻_{L,S} = [[0,L],[S,0]],
[𝔻̇,𝔻] = Γ𝒜^raw (ordinary commutator; the anticommutator gives the synchronized channel). Every
quadratic representation of the current is indefinite (3.4). Second jet: M K^{(2,∂)} = W, hence
−M𝒜^raw + MK^{(2,∂)} = −2L̇ (4.6). General formula μ∗β_a = Da − (μ∗a)∗D1 (4.7) (verified).

**Claims.** PROVED: antidiagonal polarization, law (0.4), graded realization, indefiniteness of
every completion by squares, Möbius-extracted K² = W, γ + W = 2Λlog "inside PC", localization correction
with respect to 851. OPEN: cancellation of 2MK and tails; minimality ⟹ (0.5); exterior law.
What the text sustains: the identity (0.4) is an insertion of I = P+Q, correct; the claim
that γ + W survives in PC is withdrawn by 856.

**Where it stopped.** Minimality controls the diagonal in F, not the cross pairing with the causal
dual h; differentiating PAF = ρb would presuppose the sought tangency.

**Later correction.** R170_855/856: K² does not survive as an independent summand.

**T1–T4.** **T3: yes** — the reconstruction of the weight 2Λ(n)log n through γ + W uses Λ∗1 = log, μ∗1 = δ and
Selberg; refuted as a physical contribution in 856. T1: no (explicitly: squaring the graded
sector gives either ratio-comb with positive metric, or an indefinite form with supertrace). T2, T4: no.

### R170_855 — Möbius assembly of the two jets

**Object.** ∂_−K_N = 2K_N + K^{(2,∂)}; M K^{(2,∂)} = Σ_{k≤N} W(k)k^{-1/2}∂_tτ_{log k}; Thm. 3.1:
−M𝒜^raw + MK^{(2,∂)} = −2L̇ on every complete fibre.

**Claims.** PROVED (coefficients): jet, M K² = W, γ + W = 2Λlog, assembly. In its table:
complete cancellation of 2MK + MK² "PROVED R170_856"; physical survival of the assembly "REFUTED
R170_856". OPEN: sign of the physical diagonal.

**Later correction.** Header of R170_856: in the complete PC the jet of {X_r,E}𝓕_r contains
−K_− − JK_−𝓕 and the two branches of −JH𝓕 − H contain +JK_−𝓕 + K_−; term-by-term cancellation.

**T1–T4.** T3: yes (same as 854), closed by 856.

### R170_856 — Complete PC jet: total Chebyshev cancellation and boundary ledger

**Object.** H_− = 𝒜^raw − K_−, K_− = 2K + K^{(2,∂)}. Poisson–X jet (2.1)–(2.2):
{X_r,E}𝓕_r = S𝓜_r − K − JK𝓕_r; 𝒳_− = SṀ − Ṡ𝓜 − K_− − JK_−𝓕 − JK𝓕̇. Total cancellation
(−K_− − JK_−𝓕) + (K_− + JK_−𝓕) = 0. Reduced identity (3.5):
𝒞 = SṀ − Ṡ𝓜 − L̇*E𝓕 − L*E_−𝓕 − L*E𝓕̇ − J𝒜^raw𝓕 − JK𝓕̇ − JH𝓕̇ − 𝒜^raw. Ledger
P𝒞P = 𝓡_int + 𝓡_cross (5.3)–(5.4); atoms (6.1)–(6.4); extraction PȦF = BP𝒞F + 𝒫^comb (7.2);
simplified Tate coordinate g_ε ω^comb = (b,PȦF) − (h,P𝒞F) (8.6), defect
g_εΔ^Tate = (b,PȦF) − (h,P𝒞F) − ρg_ε (8.7); polar continuum Z Ȧ − ŻA = 𝒞 − 𝒫_{C,A} (9.1)–(9.4).

**Claims.** PROVED: all of the above. REFUTED: persistence of K² as an independent physical
contribution; 855 valid only as a one-branch identity. OPEN: sign of the ledger; exterior law.

**Where it stopped.** The algebraic cancellation is complete and tautological; what is missing is to orient
the dual scalar (11.3). No summand of (11.2) can be erased or signed separately. The positive
tail H appears in JH𝓕̇ but the Fourier jet and the compression have both signs.

**T1–T4.** **T4: yes, directly** — H = Σ_{N<k≤MN} h_{M,N}(k)k^{-1/2}τ_{log k} with h ≥ 0 remains
in the ledger as −JH𝓕̇ and −PJHQ𝓕̇P (reflected route of the tail); its positive coefficient does not sign
the pairing (it does not have the form |ℓ_k(F)|²). T3: closes the γ + W route (the W cancels with −W of 4.4).
T1, T2: no.

### R170_857 — Kato radical/transverse reduction of the Tate defect

**Object.** Under an explicit C¹ frame (§1: isometric transport, Kato family with common form domain,
H_s ≥ 0 for s ≤ 0, representable velocity): 𝖹 = 1_{0}(H), 𝖰 = I − 𝖹, reduced resolvent R,
B = 𝖹V𝖹, C = 𝖰V𝖹, V = Ḣ. Prop. 2.1: B ⪯ 0. Kato: Bf = νf, 𝖰ḟ = −RCf; horizontal lifting
f_s^K = f − sRCf. Exterior observer 𝓛_s = Q_eA_sι_s, connection χ_F, η = 𝓛_0*q. Main identity
(5.3)/(5.5): gΔ^Tate = 𝔚_K(f) + (q,χ_F) − (𝖰η, RCf).

**Claims.** PROVED under the C¹ frame: B ⪯ 0, transverse equation, exact reduction. OPEN
(REG): unconditional existence of the C¹ family. UNDETERMINED: sign of C. IDENTIFIED/OPEN: scalar
condition (6.1) 𝔚_K + (q,χ_F) = (𝖰η, RCf). 2×2 falsifier (7.1): H = diag(0,1), V = [[−1,c],[c,0]]:
H + sV ≥ 0 for small s<0, B = −1, RC = c arbitrary (verified). What the text sustains:
correct as CONDITIONAL on (REG)/C¹; the memo says so explicitly.

**T1–T4.** Touches none (perturbation theory).

### R170_858 (MOBIUS_RESOLVENT_WARD_COORDINATE) — Möbius–resolvent coordinate and Ward wall

**Object.** 𝔯_T(f) = Re(𝖰η, R𝖰Ḣ𝖹f) = Re(Y, Ḣf), Y = R𝖰η; explicit observer
η = ΠPAQ_eS*PM_μ*Pb (2.2) expanded in (2.3) with 𝓜, Λ(d), intermediate Q_e and M_μ*. Transverse
source (3.7): (y,𝖢f) = (𝓑*Y, P𝒞_{PC}F) + (Y, 𝒫^comb) + 𝔱_T(Y,F), 𝔱_T of rank one by parity.
Complete PC expansion (4.5); spectral form Σ_{λ_j>0}(η,φ_j)(φ_j,Ḣf)/λ_j. RES–WARD (7.1).

**Claims.** PROVED: η, source with connection, complete expansion, identification with MET–WARD/W12,
finite causal falsifier (§8: H = diag(0,1), V_c, A_0 3×3, nilpotent cell S_2 = I + 2^{-½}N_0,
M_2 = I − 2^{-½}N_0, M_2S_2 = I; coordinate = c arbitrary). REFUTED: cancellation by linear Ward
(R162_305 gives 0 = 0 for every test). OPEN: RES–WARD. ABSENT: coupling of the Ward edges
(finite defect of a_κ: (κ−1)log2(δ_0 − ν_4), (κ−1)log3(δ_0 − ν_3)) with the resolvent.

**Where it stopped.** The two numerators of the spectral expansion are independent cross-correlations;
minimality only signs 𝖹Ḣ𝖹, eliminated by R𝖹 = 0. A mixed Ward–resolvent identity is requested,
not another convolution of coefficients.

**Later correction.** R170_859 (the sandwich is not gauge invariant).

**T1–T4.** T3: records that Λ∗1 − log = 0 cannot pass through R (non-causal dependence on all of
H). T2: partial (M_μ in η). T1, T4: no.

### R170_858 (RESOLVENT_WARD_SANDWICH) — The minimal residue is a Ward resolvent sandwich

**Object.** Same content as the previous one in shorter form: 𝔖_RW(f) = (Q_Kη, RCf) = (Y, Ḣf),
spectral expansion (2.1), PC extraction (3.4), RES–WARD (5.2): 𝔚_K + (q,χ_f) = (B_μ*Y, P𝒞f) +
(Y,𝒫^comb) + 𝔗_conn. 2×2 falsifier (6.1)–(6.2).

**Claims.** DEFINED/PROVED: same as the other 858. REFUTED: linear Ward evaluates the sandwich;
minimality signs it. Header of R170_859: the sandwich is not canonical; (q,χ_f) − 𝔖_RW is
gauge invariant.

**Remark.** The two 858 files are two parallel drafts of the same step; they differ in
notation (𝖰 / Q_K, 𝔯_T / 𝔖_RW, 𝔱_T / 𝔗_conn) and in that the first adds the analysis of a_κ (§9). Neither
cites the other.

**T1–T4.** Does not touch directly.

### R170_859 — Gauge-invariant exterior connection defect

**Object.** Change of trivialization U_s = I + sK, K* = −K: Ṽ = V + HK − KH, C̃ = C + Q_KHKZ,
RC̃ = RC + Q_KKZ; χ̃ = χ + 𝓛_0Kf; with ZKZ = 0 the combination Θ_ext = (q,χ_f) − 𝔖_RW is invariant.
Gauge K_C = [[0,(RC)*],[−RC,0]] kills C. gΔ^Tate = 𝔚_K + Θ_ext.

**Claims.** PROVED: transformations, invariance of Θ_ext, Δ^Tate = (𝔚_K + Θ_ext)/g.
CONSTRUCTED: gauge killing C. REFUTED: 𝔖_RW as intrinsic residue. OPEN: (0.4) 𝔚_K + Θ_ext = 0.
Verified (1.5), (1.6), (3.2).

**T1–T4.** Does not touch.

### R170_860 — Audit of the alleged two-scale holonomy

**Object.** Scalar rectangle 𝓑(r,s) = (q_r, z_s): ∮d𝓑 = 0 but the antidiagonal derivative is not zero
(example 𝓑 = r). The physical family depends only on r: ∂_qH_r = 0, Berry curvature Ω_{rq} = 0.
S(q)A(r) is not self-adjoint. Prop. 4.1: every congruence G(q)*H(r)G(q) is pure transport. List of
seven criteria for a nontrivial second connection 𝕳(r,q).

**Claims.** PROVED: zero circulation. REFUTED: zero circulation ⟹ zero antidiagonal Wronskian;
congruence by causal comb contributes new curvature. ZERO: r–q Berry. FALSE: S(q)A(r) self-adjoint
contact family. FORMULATED: criteria 1–7. OPEN: 𝔚_K + Θ_ext = 0.

**T1–T4.** T2: partial — records that congruence by the comb (or its Möbius inverse) is a change of
coordinates and does not introduce a unique factorization in intrinsic form. Otherwise: no.

### R170_861 — Every positive dilation with physical Schur is pure congruence

**Object.** 𝕳 = [[A,D*],[D,G]], G > 0, Schur A − D*G^{-1}D = H ⟹ 𝕳 = [[I,D*G^{-1}],[0,I]]·(H ⊕ G)·[[I,0],[G^{-1}D,I]];
ker 𝕳 = {(f, −G^{-1}Df): f ∈ ker H}. If D(r,1) = 0, D*G^{-1}D = O(u²) (no first jet). G semidefinite:
same elimination with G^† (closed range); G indefinite: the Hilbert order is lost. Application to
D ∈ {E, H_{M,N}, S(q)A(r), 𝒞_PC}.

**Claims.** PROVED: triangular factorization, positivity and kernel, q direction pure gauge with
fixed Schur. REFUTED: coupling with D(r,1)=0 gives a jet. OPEN CLASS: linear arithmetic deformation of the
Schur S(r,q) = H(r) + 𝓡(r,q), 𝓡(r,1) = 0, ∂_q𝓡 ≠ 0. REFUTED by 862: diagonal (6.3) as encoding.

**Later correction.** Header of R170_862: (6.3) has incorrect homogeneity (quadratic vs
linear).

**T1–T4.** T1: yes, as a class — any square completion D*G^{-1}D with arithmetic D (including
H_{M,N} or the PC) is congruence; without compensating, the new Schur asks for a new global inequality and
generates ratio-comb. T4: yes, as a class — placing H_{M,N} in the cross block does not create energy. T2, T3: no
("Λ∗1 = log may simplify D but does not alter (0.3)").

### R170_862 — Correct homogeneity: the law needs a bordered null anchor

**Object.** 𝔏_T(f) = 𝔚_K + Θ_ext = g_εΔ^Tate(f) is linear in f (directly from (8.7) of 856, without REG).
Lemma 2.1: C¹ family with 𝕳(s) ≥ 0 on both sides ⟹ P_N𝕳̇(0)P_N = 0 (only ⪯ 0 if positive on one side).
Correct homogeneous encoding 𝔏_T(f) = (a, 𝕳̇f) with a ∈ ker. Model (3.2): 𝕳_c(s) = (sc,1)ᵀ(sc,1)
≥ 0, (e_2, 𝕳̇_c(0)e_1) = c arbitrary if the anchor is not null. Specification of the "bordered null
anchor": coordinate e_T produced by the comb and the ports, exact nullity from Λ∗1 = log and the
finite hyperbola, jet equality (4.3), two-sided positivity.

**Claims.** PROVED: linearity, two-sided lemma, null anchor forces zero. REFUTED: diagonal
encoding; anchor outside the kernel receives cancellation. FALSE: the Tate column b is a null anchor
(g_ε > 0). NOT PROVED: the interior cancellation of the hyperbola (H_{M,N} without coefficients at k ≤ N) gives a
null vector of a positive form. SPECIFIED/OPEN: null anchor law.

**T1–T4.** **T4: yes** — proposes to realize the interior nullity of H_{M,N} (zero coefficients k ≤ N) as
a null coordinate of a positive form with the tail k>N as boundary flux; records that it is nullity of
coefficients, not of a vector, and that its jet K_− cancels in the complete PC. **T3: yes** — the required exact
nullity must come from Λ∗1 = log; not built. T1, T2: no.

---

## 2. Synthesis

### (a) Reusable PROVED pieces

- Scale Ward identity of the finite hyperbola and support k>N after δ_Λ = 0: R170_841 Thm. 3.1,
  (3.4)–(3.8); defect δ_a for altered weights (3.6), (3.9).
- Antisymmetric coefficient β_Λ(k) = 2Σ_{d|k}Λ(d)log d − (log k)², sign examples (4.6)–(4.7); bound
  |β|² ≤ (log k)Σ_Λ (4.9)–(4.10): R170_841 §4.
- Derivative of the polar continuum Ċ_N: R170_841 (5.5); its Laplace symbol
  K_{Ċ_NF} = c_N(s)(1 − 1/(2s) − a log N)K_F: R170_844 (3.2b).
- Laplace transform of the Wronskian: K_{𝒜^raw F}(a) = −aB_{M,N}(s)K_F(a), B_{M,N} = ℓσ' − ℓ'σ:
  R170_843 (5.2)–(5.4); B_Λ = −ζ²(1/ζ)'' (5.6)–(5.7) (positivity CITED); B_{N,N}(s) > 0 for s ≥ 3,
  N ≥ N_0 absolute (Thm. 5.1); Hankel energy 𝓔^β > 0 (5.18); typed collar (6.6)–(6.8).
- Collinearity of the two routes when differentiating at r = 1 (R170_843 §2.1); universal concomitant
  𝔎_P(B;g,w) = ⟨g,[P,B]w⟩ (R170_843 (4.2)).
- Domain gate K_{C_NF}(a) = N^{a+½}K_F(a)/(a+½) and δ > log N: R170_844 §1.1; π_N > 0 (3.2h)–(3.2i);
  Fredholm criterion (Thm. 6.1).
- Derivative of the primitive projection and Π̇F = −b_ε⟨ḃ_ε,F⟩/q_ε, 2Re⟨Π̇F,r_F⟩ = −2Re⟨F,t r_F'⟩:
  R170_845 (1.5), (2.4), (3.1).
- Two-scale PC (r,q) with the factor r/q: R170_847 Thm. 4.1; jet ∂_−K = 2K + K^{(2,∂)} (4.6);
  version without right Fourier and ṁ = −τm': R170_848 (1.1), (3.1)–(3.2).
- Nilpotency and finite inverse of PS_NP: R170_849 (1.2)–(1.3); B_{N,T} = PM_μP: R170_850 (1.5).
- γ_Λ = μ∗β_Λ = −Σμ(d)(log d)² = Λlog − Λ∗Λ, values by ω(n): R170_850 (0.2), R170_851 (0.1);
  general formula μ∗β_a = Da − (μ∗a)∗D1: R170_854 (4.7).
- Boundary atoms of ∂_t(Pg), ∂_t(Qg) and combined port: R170_851 §§3–4, R170_856 §6.
- Tate coordinate of the combined port and defect: R170_852 (0.5)–(0.6); simplified form
  g_εΔ^Tate = (b,PȦF) − (h,P𝒞F) − ρg_ε: R170_856 (8.7).
- Causal graph S*Ph = b + 𝒟b and mismatch z_F: R170_853 (1.1), (2.2).
- Graded Green law 𝔚_bulk + 𝔚_ext = 𝔚_Tate and [𝔻̇,𝔻] = Γ𝒜^raw: R170_854 Thm. 2.1, (3.2).
- Total cancellation of K_− = 2K + K² in the differentiated PC and complete P/Q ledger: R170_856 (0.2),
  (3.5), (5.3)–(5.4), (9.1)–(9.4).
- (CONDITIONAL on REG/C¹) B = 𝖹Ḣ𝖹 ⪯ 0 and Kato reduction: R170_857 Prop. 2.1, (5.3)/(5.5).
- Gauge invariance of Θ_ext and gauge K_C killing C: R170_859 (2.6), (3.1)–(3.3).
- Pure congruence proposition: R170_860 Prop. 4.1; triangular factorization of extensions with
  fixed Schur: R170_861 (0.3), (1.3).
- Two-sided lemma P_N𝕳̇P_N = 0 and linearity of 𝔏_T: R170_862 Lemma 2.1, §1.

### (b) Closures (class and falsifier)

- 𝒞_fib^{(1)} (first-order diagonal operations per fibre, δ_Λ = 0, positivity of coefficients,
  squares within the fibre): R170_841 Thm. 6.1. Falsifier: β_Λ(12) < 0; parity of Σ_Λ; family
  F_ξ with c'_{F_ξ} ≍ ξ of both signs (§6.1).
- 𝒞_Green^{(1)} (standard mixed Green with compressed 𝒜, reflection, XF, F_δ, without Hankel between legs):
  R170_843 Thm. 8.1. Reason: collinearity of routes, (4.2) = concomitant of R161_065, (4.11) without sign.
- Static lifting (7.3) of 843 with orientation (0.5): R170_844 §5, refuted by sign
  (would imply 𝒱 > 0 on the radical since π_N > 0) and by Fredholm (Thm. 6.1; only with H^†).
- Isolated Gamma energy as weight separator: R170_843 §5.4 (many altered positive weights
  also give a positive Wronskian at s_m ≥ 3).
- Equality physical metric = Hankel metric: R170_849 §4 (𝓡*D𝓡 compact).
- Completion by the synchronized tail as Selberg's W: R170_851 §2 (the tail is zero for k ≤ N).
- Physical survival of γ + W = 2Λlog: R170_856 §4 (the −W of the Poisson–X block cancels it).
- Every completion by squares of the graded current: R170_854 (3.4) (indefinite metric) and §6.3
  (with positive metric ratio-comb reappears).
- Minimality signs the transverse block / sandwich: R170_857 §7, R170_858 (both) — 2×2 falsifier
  H = diag(0,1), V_c = [[−1,c],[c,0]]; with Möbius causal cell (858 §8).
- Linear Ward (R162_305) evaluates the resolvent coordinate: R170_858 §6 (gives 0 = 0).
- Sandwich 𝔖_RW as intrinsic residue: R170_859 (gauge K_C kills it).
- Two-scale holonomy with the existing families: R170_860 (zero circulation without content; Berry
  zero; S(q)A(r) not self-adjoint; congruence = gauge).
- Positive extensions with fixed physical Schur (includes completing the square with D ∈ {E, H_{M,N}, S(q)A(r),
  𝒞_PC}): R170_861 (0.3); coupling vanishing on the physical fibre: (3.3).
- Diagonal (quadratic) encoding of the defect: R170_862 §1; anchor with positive energy (b, h):
  model (3.2), (e_2, 𝕳̇_c e_1) = c.

### (c) Explicitly open and exact obstacle

- Antisymmetric boundary Green law for 𝒜_{M,N} with ledger (5.8) (R170_841 §7): missing a
  physical first-contact relation that orients a first moment.
- Physical Hankel lifting (R170_843 (7.3)–(7.4)): refuted in its static form by 844; its
  substitute is the covariant derivative (844 (8.1)), later wrongly typed (846).
- Covariant Ward–PC (R170_844 §8; R170_847 "PC–curvature"): prove that the Hermitian diagonal of the
  antidiagonal derivative of the complete PC is −𝒱 − 𝓔^β − tail energy + polar residue cancelling Π̇.
- Extraction of Ȧ from SȦ without inverting S_N (R170_848): solved algebraically in 849, but with
  a metric clash: MET–WARD (R170_849 §5) — difference B* − G^ext with diagonal ≤ 0 on ker H_T.
- Signed completion of the two-prime-base channel −2 log p log q (R170_850 §5).
- Exterior law (R170_853 (5.1)) ⇔ dual equality (R170_854 (0.5)):
  (h, P(SȦ − ṠA)F) = (b, PȦF) − ρ(PṠ*Ph, b); minimality does not control the pairing with the causal
  dual h.
- Sign of the dual scalar (R170_856 (11.3)): (b,PȦF) − (h,P𝒞F) − ρ‖b‖².
- Kato scalar condition (R170_857 (6.1)); RES–WARD (R170_858 (7.1)/(5.2)), with the requirement of
  coupling the finite edges of the a_κ defect with the resolvent.
- Intrinsic identity 𝔚_K(f) + Θ_ext(f) = 0 (R170_859 (0.4)).
- Family 𝕳(r,q) with criteria 1–7 (R170_860 §5); live class: linear arithmetic deformation of the
  Schur S(r,q) = H(r) + 𝓡(r,q) with ∂_q𝓡 ≠ 0 (R170_861 §6).
- Bordered null anchor law (R170_862 §4): build e_T from the comb and the ports, with exact
  nullity by Λ∗1 = log, jet (4.3) and two-sided positivity. Obstacle: the interior nullity of H_{M,N} is
  of coefficients, not of a vector of a positive form.
- Transversal to the whole stretch: (REG)/C¹ regularity of the family of windows remains OPEN (841 §1,
  857 §1).

### (d) What this stretch already walks of T1–T4, with reason for failure

- **T1 (continuous squares with arithmetic in the index/dilation weight).**
  R170_843: G_δ = 𝓡_δ*𝓡_δ on the Gamma lattice with weights a_mB_{N,N}(s_m) gives 𝓔^β > 0, but (i) the sign
  does not separate Λ from altered positive weights at s_m ≥ 3 (§5.4), (ii) the passage to the renormalized operator
  adds polar/support/Tate blocks without sign. R170_844: the same observer gives the polar residue the
  sign opposite to the one required (3.2i) and the static factorization is Fredholm-circular. R170_849: the
  observer with weights 1/σ_N(a_m) extracts S_N with sign, but it is compact and produces a filtered virial,
  not the physical one. R170_861: completing the square D*G^{-1}D with arithmetic D is pure congruence; without
  compensating it requires a new inequality and generates ratio-comb. R170_854 §6.3: squaring the graded sector
  gives ratio-comb or an indefinite metric. None is a continuous square on P_T reproducing a_T with
  remainder ≥ 0; all are auxiliary observations in Laplace coordinates.
- **T2 (divisor incidence Gram).** The factorization [log gcd] = E diag(Λ) Eᵀ does not appear in
  any file of the stretch. The closest: grouping by fibres k = dm (841), declared forbidden
  as a diagonalization because it changes the physical Gram (841 §6, 843 §2.1); the Möbius inverse of the comb
  as a change of metric (849–850), which 860 Prop. 4.1 reduces to congruence; and the channel −2 log p log q
  of γ_Λ (850 §5), which suggests a square in the lattice of prime bases, not built.
- **T3 (Σ_{d|n}Λ(d) = log n as a quadratic bound).** Walked directly in R170_841 §4.2:
  probability Λ(d)/log k and Cauchy–Schwarz |β_Λ|² ≤ (log k)Σ_Λ; fails because the bound is even in the
  leg difference and β_Λ is odd (changes sign, β(12) < 0). Variants: 843 (Dirichlet sum
  with concavity of 1/ζ: sign in the half-plane, does not separate weights on the lattice), 850–851 (γ = Λlog −
  Λ∗Λ, clash with Selberg without sign), 854–855 (γ + W = 2Λlog inside PC), closed by 856 (the W
  appears with opposite sign in the Poisson–X jet and cancels). 858 records that Λ∗1 − log = 0 does not
  cross the reduced resolvent. 862 requires an exact nullity by Λ∗1 = log as a null vector, not
  built.
- **T4 (common residue as Σ_{k>N} h(k)|ℓ_k(F)|²).** The tail exists with h_{M,N}(k) ≥ 0 (841 (3.8)), but
  throughout the stretch it is coupled to ∂_tτ_{log k} or to τ_{log k}𝓕̇, never to a squared modulus: its
  pairing is a correlation derivative without sign (841 Thm. 6.1, 856 §10.4). In Gamma
  coordinates it does give a positive multiplier Θ_N(s) (844 (4.3)–(4.4)), but in the Hankel metric, not the
  physical one, and the rest of the ledger remains without sign. 861: putting H_{M,N} in a cross block is
  congruence. 862: the interior nullity of H_{M,N} is nullity of coefficients, not a null vector of a
  positive form; its jet K_− cancels in the complete PC. The stretch does not attempt the conversion of the
  mixed pairings (H, E_N) into a sum of squares |ℓ_k(F)|² with h ≥ 0; that exact form does not
  appear.

### (e) Inconsistencies or errors between memos

1. R170_844 (8.1) uses the symbol 𝔓^ren_{N,N} without definition; R170_846 withdraws it and R170_845 §4 becomes
   conditional (the headers record this).
2. R170_843 (7.3) is presented as an open target; R170_844 proves that the requested orientation is
   impossible (opposite sign of π_N), not merely open. The final table of 843 still says OPEN; the
   added header only mentions domain and Fredholm, not the refutation by sign.
3. R170_843 table: "full half-plane separation for an altered weight PROVED" — the text only
   shows it for the weight δ_2 (5.21); it is not a general statement.
4. R170_849 (1.3) says that the finite inverse holds "simultaneously for all N"; the stabilization
   PS_NP = PSP requires N ≥ e^{2T} (R170_850 (1.3)).
5. R170_851 declares that the interior W is not in the tail; R170_854 corrects that it is in K²; R170_856
   in turn corrects that this W cancels in the complete PC. The claim of 854 "γ + W = 2Λlog inside
   PC PROVED" is invalidated as a physical contribution (it only holds per branch).
6. Notation: R170_852 uses q_ε = ‖b_ε‖²; R170_853–856 use q for the exterior vector QS*Ph and rename
   the norm as q^Gram or g_ε.
7. The two R170_858 files are parallel drafts of the same step with different notations
   (𝖰/Q_K, 𝔯_T/𝔖_RW, 𝔱_T/𝔗_conn) and do not cite each other; the header of 859 only corrects the
   "SANDWICH" file.
8. R170_861 (6.3) proposes a quadratic diagonal equality for a linear functional; corrected by 862.
9. R170_849 (2.2) separates PṠPAF and PṠQAF; R170_851 shows that each carries boundary atoms and only
   the sum is typed.
10. No mathematical errors found in the spot checks performed: (3.4) of 850, (4.7) of
    854, (3.2) of 854, (1.5)–(1.6)/(3.2) of 859, 2×2 falsifiers of 857/858/862, (3.2f)–(3.2h) of 844.

### (f) Files read (complete reading with Read)

R170_841_VIRIAL_LB.md (718 lines); R170_843_ANTISYMMETRIC_HYPERBOLA_GREEN.md (1140);
R170_844_WRONSKIAN_PHYSICAL_LIFT.md (947); R170_845_MOVING_TATE_CONNECTION.md (230);
R170_846_PC_CARRIER_AUDIT_AND_CORPUS_FILTER.md (237); R170_847_TWO_PARAMETER_PC_CURVATURE.md (305);
R170_848_FOURIER_REMOVED_PC_CURVATURE.md (221); R170_849_FINITE_EXTRACTION_AND_METRIC_MISMATCH.md (214);
R170_850_MOBIUS_EXTRACTED_WRONSKIAN_LAW.md (233); R170_851_SELBERG_COLLISION_AND_BOUNDARY_ATOMS.md (194);
R170_852_EXACT_COMBINED_TATE_DEFECT.md (203); R170_853_CAUSAL_GRAPH_CURVATURE_AND_ARITHMETIC_MISMATCH.md
(197); R170_854_GRADED_EXTERIOR_WRONSKIAN_GREEN.md (418); R170_855_MOBIUS_TWO_JET_ASSEMBLY.md (181);
R170_856_FULL_PC_JET_AND_BOUNDARY_LEDGER.md (582); R170_857_KATO_RADICAL_TRANSVERSE_REDUCTION.md (364);
R170_858_MOBIUS_RESOLVENT_WARD_COORDINATE.md (489); R170_858_RESOLVENT_WARD_SANDWICH.md (276);
R170_859_GAUGE_INVARIANT_EXTERIOR_CONNECTION.md (264); R170_860_TWO_SCALE_HOLONOMY_AUDIT.md (217);
R170_861_POSITIVE_BLOCK_DILATION_NO_GO.md (234); R170_862_BORDERED_NULL_ANCHOR_LAW.md (225).
Total: 22 files (841, 843–857, two 858, 859–862; 842 does not exist). All read in full.
