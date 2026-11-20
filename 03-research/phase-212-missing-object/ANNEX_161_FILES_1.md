# Annex: file-by-file reading of phase 161, part 1 (README and R161_000 to R161_027)

Folder read: `03-research/phase-161-row-d-sum-product-square/`. It exists; it contains README.md, R161_000 to
R161_081 and `scripts/` with: 161_01_hyperbola_defect.py, 161_02_poisson_defect_probe.py,
161_03_gamma_hankel_identity.py, 161_04_pc_matrix_countermodel.py (not analysed).

Cross-check against what `REVIEW_003.md` leaves unexcluded:
U1 term of degree ≥ 2 in the weight that enters additively and vanishes at Λ through Σ_{d|n}Λ(d) = log n;
U2 compression to the window (leakage ‖(I−P)·PF‖², words QV_aQ), position operator, finite rank, joint accounting
with the Tate block; U3 indefinite forms with non-radical neutral vector; U4 remainder of near-coincidences
with truncated Möbius c_N(k); U5 isometric source dilation (exit A of R161_033).

General reading caveat. From R161_004 §4 on, the phase works on a «first-contact state» (vector
of the radical of the semidefinite primitive form at the first T where it ceases to be definite) and seeks to prove that this
vector is zero. To that end the memos R161_004, 005, 007–012, 014, 019–021 use an external equivalence (reduction to
values on a set of zeros and a Cartwright-type counting argument imported from phase 121). It is recorded
neutrally as «uses an external equivalence»; it is not developed. Pieces that do not depend on it are marked.

Notation of the phase: τ_aF(t) = F(t+a), JF(t) = F(−t), X = Q = multiplication by t, 𝓕 = additive Fourier in the
logarithmic coordinate, M = m(D) with m(τ) = Re ψ(1/4+iτ/2) − log π, X + 𝓕X𝓕 = M (imported, R160_C8_R1);
S_N = Σ_{n≤N} n^{−1/2}τ_{log n}, K_N = Σ (log n)n^{−1/2}τ_{log n}, L_M = Σ_{d≤M} Λ(d)d^{−1/2}τ_{log d},
A_M = M − L_M − L_M*.

---

## 1. Entries by file

### README.md
Index of the phase with 35 «verdict» items and a «backward audit update» summarizing R161_046 to
R161_081 (outside this part). Declared status: OPEN. Items relevant to this part: 1–19. Items 20–35 and the
audit summarize later memos: the «two-level variance» over product fibres (item 20), the Poisson square
in direct sum (21), the crossed Tate block positive by parity (22, later annulled at the order of
source derivative, item 33), the lack of a coherent Gram step versus direct sum (23: «an explicit
Parseval/Naimark dilation or an exact Green identity is required») — direct antecedent of U5 —, the
coherent compressed leakage ‖(I−P_T)Σ_k(log k)d_kP_TF‖² (24) — direct antecedent of U2 —, the 2×2 countermodel that
satisfies all algebraic identities with A = 0 and D^coh(f) = ‖f‖² (28), and R161_081: on a parity eigenvector
Hf = λf, the exact remainder is Q = −2Σ_m(d_{m,N}+λ)|(R_Lf)_m|², hence it admits no representation by
nonnegative squares on the whole primitive space. Labels: none of its own is given. Cross-check: U2 yes (items 10, 24, 30–32,
as summary); U5 yes (item 23, as summary); U1, U3, U4 no.

### R161_000_BLUEPRINT.md
Object: plan. Fixes the normalization above, defines E_N = S_N𝓕 − JS_N (finite Poisson defect) and the multiplier
A_{M0}. Requires four properties of a candidate: conjunction (Poisson and Λ∗1 = log in a single operator
identity), quadraticity, orientation (retain A_T, not A_T² nor |A_T|), separation (explicit interior defect
for Λχ_2, Ξ_a, deletion, amplification, Dedekind, Beurling). Cited premises: primitive positivity PROVED up to
log 2, complete CITED up to 0.8; margin without uniform lower bound. No proved statements. Not corrected.
Cross-check: U1 no; U2 no (only announces); U3 no; U4 no; U5 no.

### R161_001_MUNTZ_CHEBYSHEV_ANOMALY.md
Object: the hyperbola operator H_{M0,N} = L_{M0}S_N − K_N and the joint identity
(PC) S_N A_{M0} 𝓕 = {X, E_N} − L_{M0}* E_N − J H_{M0,N} − H_{M0,N} 𝓕.
Statements: Theorem 2.1 (support of the hyperbola; PROVED, upheld): if M0 ≥ N, H_{M0,N} =
Σ_{k>N} h(k) k^{−1/2}τ_{log k} with h(k) = Σ_{dm=k, d≤M0, m≤N} Λ(d) ≥ 0, without coefficients at k ≤ N. Theorem 3.1 ((PC);
PROVED on S(ℝ), upheld: uses [X,S_N] = −K_N, X𝓕 + 𝓕X = M𝓕, JL = L*J and commutation of sums of translations).
Theorem 4.1 (interior defect; PROVED, upheld): with general weight a, the coefficient at k ≤ N is
δ_a(k) = Σ_{d|k}a(d) − log k; list of values for the falsifiers (deletion −log 2 at k = 2, amplification c at
n_0, Λχ_2 −2 log 2, Ξ_a log 2(2^a+2^{−a}−1), etc., taken from R160_D4_R2). §5: passing to the limit M0, N → ∞ is
forbidden without a domination theorem (S_∞ unbounded at critical density). §6: claims no sign; «positive coefficients
do not make a sum of translations positive». Stopped: no sign; the square is analysed in R161_002. Not withdrawn.
Cross-check: U1 no (Λ∗1 = log enters linearly, as atom δ_a(k); it is exactly the phenomenon of R3-i); U2 no (no
compression); U3 no; U4 no, but it is the antecedent with weights Λ instead of μ: h(k) for N < k ≤ M0·N is the
truncated remainder of the convolution Λ∗1, with coefficients ≥ 0; U5 no.

### R161_002_SQUARE_VERDICT_AND_NEXT_LEMMA.md
Object: the canonical square Q_{M,N}(F) = ‖R_{M,N}F‖² = ‖S_N A_M 𝓕F‖² and the oriented pairing
B_{M,N}(F) = Re⟨R_{M,N}F, S_N𝓕F⟩ = ⟨A_M G, S_N*S_N G⟩, G = 𝓕F. Defines the leakages C_T = (1−P_T)𝓕P_T,
C_T^{(N)} = (1−P_T)S_N𝓕Π_T and the compressed defect E_{N,T} = P_T(S_N𝓕 − JS_N)Π_T.
Statements: Theorem 1.1 (loss of orientation; PROVED, trivial and upheld): Q invariant under A ↦ −A; Cor. 1.2:
every nonnegative sum of such squares is blind to the sign. §2 (ARGUED, correct): positivity of B on all of L² ⇔
A_M ≥ 0 up to a null set; false for finite M on the line (negative semilocal background, cited). §3: without
compression one returns to the window shift (CITED R160_D4_R2 Thm 5.1). Problem SP-161 and Lemma L161.1 (OPEN):
canonical weights w_N ≥ 0 with Σ w_N B_{M,N} = a_T + boundary ≥ 0 (boundary = leakage squares with C_T, C_T^{(N)}).
Theorem 8.1 (no positive telescoping; PROVED, upheld): for w_N ≥ 0 not all zero, the coefficient of
Σ w_N H_{M,N} at a large prime p is log p·Σ_{N<p} w_N > 0. Cor. 8.2: the discrete jump h_p(p) − h_{p−1}(p) = −log p;
the sign appears as a terminal boundary derivative. Stopped: L161.1 dies in the positive-weight branch (Thm 8.1);
the leakage-square branch was never built. Corrected/withdrawn by R161_004 (scalar and fibrewise readings of L161.2).
Cross-check: U1 no (only degree one; «sign-flip» test Λ(2) ↦ −Λ(2) in §6); U2 yes: SP-161 is literally
«a_T = Σ oriented pairings + compression leakage squares ≥ 0» — it remained OPEN without a written object, and the
positive branch died by Thm 8.1, not by an argument about the leakage; U3 no; U4 no (Thm 8.1 is the analogue with Λ:
no positive weighting of hyperbola remainders cancels); U5 no.

### R161_003_POLAR_RENORMALIZATION.md
Object: C_N(s) = N^{1−s}/(1−s), Z_N = D_N − C_N, S_N^ren = Z_N(1/2+iD) = S_N − ∫_0^N x^{−1/2}τ_{log x}dx,
E_N^ren = S_N^ren𝓕 − JS_N^ren, and the identity (PC-ren) with H^ren = H_{M,N} − L_M C_N(D) + [X, C_N(D)].
Statements: Prop. 1.1 (obstruction of raw truncation; PROVED, upheld): |e_N(τ)| ≥ c_τ N^{1/2} infinitely
often. Theorem 2.1 (renormalized convergence; PROVED on Schwartz data, upheld via Euler–Maclaurin and the
functional equation). Theorem 2.2 (lattice minus continuum; PROVED): (C_N(D)F)(t) = e^{−t/2}∫_{−∞}^{t+log N}e^{y/2}F;
if ∫e^{y/2}F = 0, support of C_N(D)F in [−T−log N, T−log N] (translated boundary layer). (PC-ren) PROVED (same
algebra). §4: the polar term is of size N^{1/2} and can be neither discarded nor cancelled after norms. Lemma L161.2
(OPEN, later WITHDRAWN by R161_004 in its scalar and fibrewise forms). Stopped: no sign.
Cross-check: U1 no; U2 partially: the polar layer is a window-boundary object but no quadratic leakage
is formed; U3 no; U4 no; U5 no.

### R161_004_CORPUS_COLLISION_AND_STOP_GATES.md
Object: cross-check of L161.2 against the corpus. Prop. 1.1 (stabilization; PROVED, upheld): for N ≥ e^{2T},
P_T S_N P_T = Z_{T,−} and P_T JS_NJ P_T = Z_{T,+}, causal observations of phase 121, invertible with non-identity
part nilpotent. §2 (Cor. 2.1, PROVED by cited identities of Paper 41 C4–C5): the scalar version of L161.2
(primitive D(u) = Σ_{log n≤u}Λ(n)/√n − 2(e^{u/2}−1)) falls into the excluded class: local completion with a square of the
wrong sign and negative scalar density below log 2. §3 (Cor. 3.1, CITED from phases 104/106 and 121): the lifting over
divisor fibres P(D=d|N) = Λ(d)/log N has zero spectral gap; the unitriangular Möbius elimination
(D = {1,2,3,4,6,12}) kills the identity diagonal on taking the logarithmic derivative. §4: uses an external equivalence
(oriented rank certificate (4.1) of phase 121). §5: on 0.8 < T < ½ log 5 only 2, 3, 4 make contact (nilpotency
order 3). Decision: L161.2 WITHDRAWN; replacement L161.3 (OPEN). Cross-check: U1 no (the divisor fibre uses Λ∗1
as a positive disintegration, linear; it dies by zero gap, not by degree); U2 yes, partially: the double compression
P S_N P is identified with old objects (phase 121) — «the new must come out of the extra port», not from S_N;
finite rank: the chamber 2,3,4; U3 no; U4 no (the Möbius elimination is unitriangular over divisors, not c_N(k));
U5 no.

### R161_005_FIRST_CONTACT_POISSON_PORT.md
Object: for F in the radical (P A P F = r ∈ span{e^{∓t/2}}), the exterior port ℓ_T(F) = (1−P)AF, AF = r + ℓ_T(F), and
Theorem 1.1 (PROVED, trivial and upheld): P R_{M,N}𝓕F = P S_N r + B_{N,T}(F), B_{N,T}(F) = P S_N(1−P)AF; renormalized
version (3.1). §2: P S_N(1−P) does not stabilize; ‖B‖² loses orientation. §4: finite interior algebra in the
chamber 0.8 < T < ½ log 5: Z_{T,−}^{−1} = I − K + K² (PROVED). §5 «PC-port theorem» (OPEN; uses an external
equivalence). Cross-check: U1 no; U2 yes: it is exactly a compression block P S_N (1−P) A P (word Q V Q′ with
complementary projections); it was left without sign and as an unknown; U3 no; U4 no; U5 no.

### R161_006_EXTERIOR_PORT_KERNEL.md
Object: exact kernel of the renormalized port. Theorem 2.1 (PROVED, upheld): for g = (1−P)g,
(P S_N^ren(1−P)g)(t) = Δ^R_{N,T}g(t) − e^{−t/2}a_−(g), with Δ^R the «integers minus continuum» discrepancy on the
right tail with moving endpoint e^{T−t}, and a_−(g) = ∫_{−∞}^{−T}e^{y/2}g. Reflected (3.2) with a_+(g). The
cross-contamination of tails is exactly the Tate plane. Nonlocal remainders: Δ^R ℓ_T(F), Δ^L ℓ_T(F) (OPEN).
Cross-check: U2 yes (exact computation of a compression leakage block and its Tate part; no sign); rest no.

### R161_007_CHEBYSHEV_CRITICAL_JET.md
Object: G_{+,T}F = ζ(s)H_{+,T}F = −ζ′(s)K_F(z) − ζ(s)Q_{+,T}(z); on Re s > 1 it is (Σ1·n^{−s})(ΣΛ(d)d^{−s}) = Σ log k·k^{−s}.
Theorem 2.1 (PROVED; uses an external equivalence: value on a set of zeros). §5: compatibility (5.1) OPEN.
§4: «sign blindness is fatal for direct positivity but not for rigidity in the equality state». Cross-check:
U1 no (product of series = Λ∗1 = log, linear in Λ); U2–U5 no.

### R161_008_PRODUCT_HARDY_SEPARATION.md
Object: corrected port G_+^0 = G_+ − c_+(F)ζ(1/2+z)Θ_T(z), with θ_T ∈ C_c^∞((T,T+1)). Theorem 3.1 (PROVED):
e^{Tz}G_+^0 ∈ H²(ℂ_+); reflected in H²(ℂ_−). Uses the H^s regularity, s < 1/2, of the radical vectors (CITED
phase 121) and the convexity bound (CITED). Reader's reservation: the Paley–Wiener step from causal support and L²
boundary requires growth control in the strip 0 < Re z ≤ 1/2 that the memo does not write (ARGUED at that point). §4–§5:
closure by disjoint support if «PC limit = g_+ + g_−» (OPEN; uses an external equivalence). Corrected by R161_011
(the cosine scattering is missing). Cross-check: U1–U5 no.

### R161_009_POLAR_COEFFICIENT_MATCH.md
Object: polar residues of the port = exterior Tate moments; by primitivity c_+′(F) =
Σ_{2≤n<e^{2T}} Λ(n)/n ∫_{T−log n}^T e^{−u/2}F (finite collar); plus continuous Gamma collars; crossed Tate system
[[2T, 2sinh T],[2sinh T, 2T]](α,β)ᵀ = (J_+, J_−)ᵀ, determinant 4(T² − sinh²T) ≠ 0. Theorem 3.1 (PROVED, relative
to the collar theorem of phase 121). (5.2) OPEN. Cross-check: U2 yes, in the «Tate block» part: it is the accounting
of the crossed Tate block that U2 mentions; the crossed matrix is indefinite (see R161_023 §4); U3 touches: indefinite
matrix, but it is used only to solve for (α,β), not as a form; U1, U4, U5 no.

### R161_010_FIRST_CONTACT_CLOSURE.md
Object: «closure» by Hardy division. Theorem 3.1 (originally PROVED) RETRACTED by the erratum note itself
(R161_011): it omits the cosine/reflection scattering. Conclusions 4.1, 5.1, 5.2 downgraded to CONDITIONAL. Uses
an external equivalence. Cross-check: U1–U5 no.

### R161_011_TYPED_SCATTERING_AUDIT.md
Object: typed equation g_+ + C_log R g_− = 0 (instead of g_+ + g_− = 0); for parity
(I + εC_log)g_+ = 0 with support in [T,∞): Sonin space, nontrivial. Terminal lemma (4.2) OPEN: intersection
of the range of the arithmetic port with Son_T^ε trivial. Retracts R161_010 Thm 3.1. Mentions that the scalar shadow of
two contours of phase 116 has Kreĭn inertia (CITED). Cross-check: U3 touches (cites the Kreĭn inertia of a
scalar shadow, does not build a neutral vector); U2 no; U1, U4, U5 no.

### R161_012_PRODUCT_RANGE_AND_FIRST_COLLAR.md
Object: physical range Ran_phys(Z_+) (defined as graph range); Prop. 1.1 (PROVED CONDITIONALLY; uses an
external equivalence). Exact germ (3.2) on the first collar T < t < T+δ, 0.8 < T < ½ log 5:
g_+^0(t) = (log2/√2)F(t−log 2) + (log3/√3)F(t−log 3) + (log2/2)F(t−log 4) (PROVED, upheld by local finiteness).
§4–§5: the derived equation is not independent (see R161_013). Cross-check: U2 yes in «finite rank»: finite chamber
2,3,4; rest no.

### R161_013_FIRST_COLLAR_TRANSMISSION.md
Object: Y_3(F) as in (3.2); exact transmission: Y_3(F) = D_ΓF − r_ε on the interior collar and = g_+^0 on the
exterior (PROVED). §3: [Q,Z_+]F = Z_+B_+F reduces to a tautology on the collar (REJECTED as a second row; PROVED).
§4: with D_Γ = Q + C_log Q C_log, nonlocal equation Y_3(F) − tF + r_ε = C_logQC_logF on the interior collar (PROVED
as an equation); its rigidity consequence OPEN. Cross-check: U2 yes: uses the position operator Q and the word
C_log Q C_log restricted to a collar of the window; no sign; U1, U3, U4, U5 no.

### R161_014_SONIN_GAMMA_COERCIVITY.md
Object: Theorem 2.1 (PROVED, elementary and upheld): if g ∈ Dom Q, supp g ⊂ [T,∞) and C_log g = σg, then
⟨D_Γg,g⟩ = 2⟨Qg,g⟩ = 2T‖g‖² + 2∫(t−T)|g|² ≥ 2T‖g‖², equality only at g = 0. Excess energy
E_T^PC(F) = 2‖(Q−T)^{1/2}g‖². Cor. 3.1 (PROVED CONDITIONALLY; uses an external equivalence): closure if
E_T^PC ≤ 0 on the radical. §1 domain: G′ ∈ L² (ARGUED with the same convexity). Target (5.2) OPEN. Cross-check: U2 yes:
position operator Q composed with the reflection C_log; the coercivity is exactly the phenomenon «multiplier +
reflection in a parity sector» of R3-a (ε⟨X²F,F⟩ analogue with X instead of X²); U1, U3, U4, U5 no.

### R161_015_CANONICAL_HARDY_GAUGE_AND_NORM_SLOPE.md
Object: canonical gauge Θ_T(s) = e^{−T(s−1)}/s (normalized reproducing kernel), G_+^can, moving contour
G_{T,δ}(τ) = e^{Tδ}G_+^can(1/2+δ+iτ), g_δ(t) = e^{−δ(t−T)}g(t), N_T(δ) = ‖g_δ‖². Theorem 3.1 (PROVED, upheld):
N_T′(0+) = −2∫(t−T)|g|² = −E_T^PC(F) ≤ 0. The sought inequality is N_T′(0+) ≥ 0 («port minimum theorem»,
OPEN). §5: the gauge obstacle of phase 116 (adding δh to one port and −δh to the other) is reduced to the
Sonin part. Cross-check: U2 yes (position: moment ∫(t−T)|g|²); U1, U3, U4, U5 no.

### R161_016_MARKOV_PULLBACK_AND_ARROW_AUDIT.md
Object: comparison between the Euler–Gamma Markov defect (contractions M_δ with Julia defect
D_δ = (I − M_δ*M_δ)^{1/2}) and the Hardy norm. Prop. 1.1 (arrow obstruction; PROVED, upheld): a contraction
that identifies input with the critical port and output with the shifted one only gives N_T(0) − N_T(δ) = ‖D_δE_0g‖² ≥ 0,
the direction already known. Theorem 2.1 (PROVED CONDITIONALLY): closure if there exists (2.2)
N_T(δ) − N_T(0) = ‖D E^phys F‖² + R, liminf R/δ ≥ 0. §3 (PROVED in the class of bounded strong limits): E_N^ren → 0
cannot be the zero-order scattering; Grams of ports ± differ by S_a + S_{−a} ≠ 0. §4 (PROVED by the divergence theorem
of phase 116, CITED): the labelled family of Julia innovations {d_{n,δ}J_{log n,−}F}_n has
divergent exterior energy; it cannot be completed orthogonally and summed afterwards; the norm/synthesis order does not
commute. §5 (PROVED): the finite data 2,3,4 control only the first collar, not the global slope. Open: (2.2)
global and the local route Y_3(F) = 0. Cross-check: U5 yes, as antecedent: the «labelled direct sum before synthesizing»
(which is what an isometric source dilation would provide) clashes with the divergence of exterior energy of
phase 116; and the contraction with Julia defect (implicit Sz.-Nagy dilation) gives the wrong arrow; U2 yes
(compression/finite collar); U1, U3, U4 no.

### R161_017_EXACT_SCATTERING_DEFECT.md
Object: Theorem 2.1 (PROVED, upheld; direct computation with ζ′(s) + χ(s)ζ′(1−s) = (χ′/χ)ζ):
G_+ + χG_− = ζ(s)W_ε, W_ε = d_ΓK_F − Q_+ − Q_−, d_Γ = −χ′/χ. (3.3): (W_ε)^∨ = D_ΓF − B_+F − B_−F = r_ε on the window
(PROVED). Cor. 5.1 (PROVED CONDITIONALLY): exact physical scattering ⇒ r_ε = 0. The claim that an open homogeneous
problem would remain is corrected by R161_019. Cross-check: U1–U5 no (U2 only in that the polar correction has
exterior support and does not alter the restriction to the window).

### R161_018_PC_GRAPH_COMPARISON_NO_GO.md
Object: split w_ε = A_∞u + h_+ + h_−; comparison (2.3)–(2.4) ⇒ ZA_∞u = 0 = [Z,D_Γ]. Theorem 2.1 and Cor. 5.1
(labelled PROVED: «no linear closure by PC»). Domain audit note at the start (from R161_075): the
identification ZA_∞ = [Z,D_Γ] = 0 and the universal exclusion of linear limits are NOT established; L²,
distributional and meromorphic multiplication have different implications. Current status: the PROVED label does not hold;
read ARGUED/unproved. What does remain: the need to retain a finite quadratic defect is a design
conclusion, not a theorem. Cross-check: U1–U5 no.

### R161_019_GAMMA_POLE_LATTICE_RIGIDITY.md
Object: poles of d_Γ = −log π + ½ψ((1−s)/2) + ½ψ(s/2) at s = 3, 5, 7, …; Lemma 2.1 (PROVED): vanishing of W_ε^0 ⇒
K_F(2m+1/2) = 0, m ≥ 1. Theorem 3.1 (PROVED, upheld; independent of any external equivalence): if
∫_{−T}^T F(t)e^{−(2m+1/2)t}dt = 0 for all m ≥ 1, F = 0 (change x = e^{−2t}, density of {x^m, m ≥ 1} in L²(a,b),
a > 0). Theorem 4.1 (PROVED CONDITIONAL on the physical scattering). Corrects R161_017 §5. Cross-check: U1–U5 no.

### R161_020_COMPRESSED_SCATTERING_AND_LEAKAGE_SQUARE.md
Object: Lemma 1.1 (PROVED, elementary): if U is unitary, Pg = g and PUg = λg with |λ| = 1, then Ug = λg. Leakage
square L_T^sc(g) = ‖(I−P_+)C_log g‖² = ‖g‖² − ‖P_+C_log g‖² ≥ 0 (PROVED); with error e, L = −2σRe⟨g,e⟩ − ‖e‖².
Hardy form (4.1)–(4.3) (PROVED). L161.4 (OPEN): normalization V_{M,N,T}F with
lim‖H_T^− E_N^ren V F‖² = L_T^sc(F) and vanishing on the radical; not built. Cross-check: U2 yes, fully: compression
leakage ‖(I−P)·Pg‖² of a unitary (P onto the half-line [T,∞), not onto the window); the identification with the finite
PC defect was left without an object; U5 touches (the rigidity of unitary compression is the «no dilation» version); U1, U3,
U4 no.

### R161_021_EXTREMAL_CROSS_CORRELATION.md
Object: Lemma 1.1 (PROVED, elementary): with C a self-adjoint involution, Pg = g, e = PCg − σg: Re⟨g,e⟩ = ⟨g,Cg⟩ − σ‖g‖²,
‖g − σCg‖² = −2σRe⟨g,e⟩. X_T(F) = ‖g‖² + ε⟨g,Cg⟩ = ½‖(I+εC)g‖² ≥ 0. Mellin form X_T = Re⟨G_+^0, ζW_ε^0⟩
(PROVED). §4: radicality a_T(F,H) = 0 ∀H primitive; seek a conjugate test H_F with a_T(F,H_F) = X_T(F). L161.5 OPEN.
Cross-check: U3 touches: works with a vector of the radical of a semidefinite form (radical neutral vector), not with
a non-radical one of an indefinite form; U2 yes (compression P and leakage); U1, U4, U5 no.

### R161_022_CANONICAL_CONJUGATE_TEST_AND_BOUNDARY_RECIPROCITY.md
Object: canonical test H_F = Π_T P_T Z*g (primitive; a_T(F,H_F) = 0). Theorem 3.1 (PROVED on the common graph):
X_T(F) = Re[⟨r, Τ P y⟩ + ⟨ℓ,(I−P)y⟩ + ⟨d,y⟩], y = Z*g, d = w − AF with Pd = 0. Exterior reciprocity (4.2) OPEN.
Finite version (5.1) with y_{M,N} = (S_N^ren)*g_{M,N}: DEFINED, convergence OPEN. Corrected by R161_023 (tautological
collapse). Cross-check: U2 yes, fully: decomposition Π + Tate + exterior of a word Π P Z* with compression; the
crossed Tate block appears as B_T^Tate = Re⟨r, Τ P Z*g⟩; U1, U3, U4, U5 no.

### R161_023_CONJUGATE_TEST_COLLAPSE_AND_TRUE_RECIPROCITY_GATE.md
Object: (1.3) ⟨r, Τ P y_N⟩ = ⟨Sr, g_N⟩ (PROVED); the Tate term plus the exterior Weil leakage recombine into
⟨S AF, g_N⟩ = ⟨R^ren 𝓕F, g_N⟩, the mixed pairing of (PC-ren) (PROVED); adding d reconstructs X_T (PROVED).
§4: the positive Tate Gram matrix is G_T = 2[[sinh T, T],[T, sinh T]]; that of the collar system is the crossed one
G_TC = 2[[T, sinh T],[sinh T, T]], indefinite; using it as a Gram gives a false sign (REJECTED). L161.6 (OPEN): independent
antisymmetric boundary law distinguishing ⟨g_N, S w_N⟩ from ⟨S*g_N, w_N⟩ by its moving boundary. Cross-check: U2 yes: it is the
proof that the word «conjugate test by compression Π P S*» is tautological with radicality; U3 yes, in the
negative: the available indefinite form (crossed Tate matrix) is rejected as a Gram; no neutral vector is studied;
U1, U4, U5 no.

### R161_024_POLE_REMOVABILITY_IS_ENOUGH.md
Object: Theorem 1.1 (PROVED, upheld): if W_ε^0 is holomorphic at s_m = 2m+1, m ≥ 1, then F = 0. Equivalences
§2 (PROVED). §3: the support-commutator shortcut (I−P_+)M_χP_+ (Hankel block) is CIRCULAR (CITED phase 114:
its vanishing is inner-ness of the multiplier). §5: testing directly against high exponentials is REJECTED
(moment audit of phase 121). L161.7 OPEN, superseded by L161.8. Final correction: there is no second residue
that cancels the Gamma one. Cross-check: U2 yes: the compression Hankel block (I−P_+)M_χP_+ is discarded as
circular; U1, U3, U4, U5 no.

### R161_025_EXACT_GAMMA_RESIDUE_ENERGY.md
Object: Res_{s=2m+1} d_Γ = 1; Res[ζW_ε^0] = ζ(2m+1)K_F(2m+1/2) (PROVED, upheld; also checked via
G_−^0(s_m) = −ζ′(−2m)K_F(a_m)). §2: the linear step to the safe half-plane is insufficient (locally uniform convergence on
circles already contains the theorem). Energy D_T^pole(F) = Σ 2^{−m}a_m e^{−2a_mT}|K_F(a_m)|² ≥ 0, faithful (Theorem 3.1,
PROVED). L161.8 OPEN. Cross-check: U1–U5 no.

### R161_026_GAMMA_POLE_ENERGY_IS_A_HANKEL_BOUNDARY_DERIVATIVE.md
Object: k_Γ^+(v) = c_Γ(v) − e^{−v/2} = Σ_{m≥1}e^{−a_mv}; B_{T,δ}^Γ(F) = Σ e^{−2a_m(T+δ)}|K_F(a_m)|²,
D_{T,δ}^Γ = Σ a_m e^{−2a_m(T+δ)}|K_F(a_m)|² = −½∂_δB ≥ 0. Theorem 3.1 (PROVED): Hankel kernels
k_Γ^+(2T+2δ+t+u) and −(k_Γ^+)′(·). D_T^pole = 2^{1/4}D_{T,δ_0}^Γ with δ_0 = (log 2)/4 (PROVED). Bounded observation
R^Γ_{T,δ} to ℓ² with D = ‖R F‖² (PROVED). L161.9 OPEN: reverse sign ∂_δB ≥ 0 on the radical. Cross-check: U2 touches
(infinite-rank observation, not window compression); U5 no (R^Γ is not isometric); U1, U3, U4 no.

### R161_027_METHOD_OF_IMAGES_AND_PRIME_FORCE_AUDIT.md
Object: reflected image (M_{T,δ}F)(x) = F(−x−2L), L = T+δ; Theorem 2.1 (PROVED): B^Γ = ⟨F, C_{k_Γ^+}M_{T,δ}F⟩,
D^Γ = −½∂_δ⟨F, C M F⟩. Prime contact I_{a,T,δ}(F) = ⟨F, τ_aM F⟩; its derivative in δ has no sign (PROVED by
example: phase change of F). Prime force B^prime = Σ Λ(n)/√n [I + Ī] indefinite («fixed sign: FALSE»). §5: a
conservation law ∂_δ(B^Γ − B^prime) = 0 does not suffice; L161.10 (OPEN): 0 = 2D^Γ + D^Poisson + o(1) with D^Poisson ≥ 0 from the
additive boundary defect. Cross-check: U3 touches: records that «2D^Γ − D^Poisson = 0» is an indefinite Green
conservation that does not close; U2 touches (the image is outside the window; reflection with translation is a word
JτQ); U1 no (Λ ≥ 0 linear); U4 no; U5 no.

---

## 2. Synthesis

### (a) Reusable PROVED pieces (independent of any external equivalence)

1. Finite identity (PC) and its version (PC-ren): R161_001 Thm 3.1; R161_003 §3.
2. Support of the hyperbola and interior defect for general weight δ_a(k) = Σ_{d|k}a(d) − log k: R161_001 Thms 2.1, 4.1.
3. Sign blindness of ‖S_N A_M 𝓕F‖² and of its positive sums: R161_002 Thm 1.1, Cor. 1.2.
4. No positive telescoping of the hyperbola remainders; terminal jump −log p at primes: R161_002 Thm 8.1, Cor. 8.2.
5. Obstruction of raw truncation and renormalized convergence; lattice-minus-continuum representation and support
   of the polar layer on data with vanishing Tate moment: R161_003 Prop. 1.1, Thms 2.1, 2.2.
6. Stabilization P_T S_N P_T = Z_{T,−}, nilpotency; finite algebra of the chamber 0.8 < T < ½ log 5:
   R161_004 Prop. 1.1; R161_005 §4.
7. Exact kernel of the exterior port P S_N^ren (1−P) = Δ^R − e^{−t/2}a_−: R161_006 Thm 2.1, (3.2).
8. Identity of the functional-equation defect G_+ + χG_− = ζW_ε: R161_017 Thm 2.1.
9. Completeness of exponential moments {e^{−(2m+1/2)t}}_{m≥1} in L²(−T,T): R161_019 Thm 3.1.
10. Residues Res d_Γ = 1 at 2m+1; faithful pole energy; Gamma Hankel identity and method of images:
    R161_025 §1, Thm 3.1; R161_026 Thm 3.1, §5; R161_027 Thm 2.1.
11. Elementary Hilbertian lemmas: rigidity of unitary compression and leakage square (R161_020 Lemma 1.1, (3.2),
    (3.4)); extremal correlation for involutions (R161_021 Lemma 1.1); coercivity of Q on sectors of C_log with
    support in [T,∞) (R161_014 Thm 2.1); norm slope −2∫(t−T)|g|² (R161_015 Thm 3.1); arrow of a
    contraction with Julia defect (R161_016 Prop. 1.1).
12. Tate projection: ⟨r, ΤPy⟩ = ⟨r,y⟩; positive Tate Gram G_T versus the indefinite crossed G_TC:
    R161_023 (1.1)–(1.3), §4.

### (b) Closures with class and falsifier

- Squares of (PC) and nonnegative sums of them: blind to the sign (A ↦ −A). R161_002 Thm 1.1.
- Weightings w_N ≥ 0 of the hyperbola remainders: they never cancel (coefficient log p·Σ_{N<p}w_N > 0 at large
  primes). R161_002 Thm 8.1.
- Oriented pairing without compression: reduces to the window shift (CITED R160_D4_R2 Thm 5.1).
  R161_002 §3.
- Scalar version of L161.2 (Stieltjes primitive D(u)): class of Paper 41 C4–C5, square of the wrong sign and
  negative density below log 2. R161_004 Cor. 2.1.
- Lifting over divisor fibres Λ(d)/log N, conditional variance, unitriangular Möbius: zero spectral gap
  (prime parents), identity diagonal annihilated on differentiating. R161_004 Cor. 3.1 (CITED 104/106/121).
- Second row via [Q,Z_+] = Z_+B_+: tautological on the collar. R161_013 §3.
- Direct Markov contraction: automatic arrow, falsifier = any contraction (it uses no arithmetic).
  R161_016 Prop. 1.1.
- E_N^ren as zero-order scattering: impossible in bounded strong limits. R161_016 §3.
- Orthogonal sum of labelled innovations before synthesizing: divergent energy (CITED phase 116). R161_016 §4.
- Conjugate test Π_T P_T Z*g: tautological with radicality. R161_023 §§2–3.
- Crossed Tate matrix as Gram: false sign. R161_023 §4.
- Support commutator (I−P_+)M_χP_+: circular (CITED phase 114). R161_024 §3.
- Linear step to the safe half-plane: insufficient. R161_025 §2.
- Raw prime force by images: indefinite (falsifier: phase change of F). R161_027 §§3–4.
- Linear split of the PC graph (R161_018): the NO-GO label does not hold after the domain audit of R161_075.

### (c) Explicitly open, with exact obstacle

- SP-161 / L161.1 (R161_002 §§4–5): a_T = Σ w_N Re⟨R_{M,N}F, S_N𝓕F⟩ + leakage squares of C_T = (1−P_T)𝓕P_T and
  C_T^{(N)} = (1−P_T)S_N𝓕Π_T. Only the positive-weight branch died; the version with signed weights or discrete
  derivatives and with the compressed leakages was never written.
- L161.3 / PC-port (R161_005–006): sign or object for the remainders Δ^R ℓ_T(F), Δ^L ℓ_T(F) (one-sided
  integers-minus-continuum discrepancies of the exterior Weil leakage).
- L161.4 (R161_020): identify the leakage ‖(I−P_+)C_log g‖² with a projected limit of ‖H_T^−E_N^ren V F‖²;
  the non-circular normalization V is missing.
- L161.5–L161.6 (R161_021–023): antisymmetric boundary law independent of radicality distinguishing
  ⟨g_N, S w_N⟩ from ⟨S*g_N, w_N⟩ by the moving boundary.
- Port minimum theorem / inverse pullback (R161_015–016): N_T(δ) − N_T(0) = square + R with liminf R/δ ≥ 0;
  a zero-order scattering that inverts input and output is missing.
- Local route 2,3,4 (R161_013, R161_016 §5): force Y_3(F) = 0 on a collar with the nonlocal equation
  Y_3 − tF + r_ε = C_logQC_logF.
- L161.8–L161.10 (R161_025–027): realize D^pole or −∂_δB^Γ from (PC-ren) with the reverse sign; complete the combined
  prime force into a Poisson square of the same sign (0 = 2D^Γ + D^Poisson).
All these targets, except SP-161, are formulated on a vector of the radical and depend on an external equivalence
to conclude; none is an identity (G) on all of P_T.

### (d) What already covers U1–U5 and the recorded reason for failure

- U1: nothing in this part. Λ∗1 = log enters only linearly (R161_001 Thm 4.1: atom δ_a(k); R161_007: product of
  Dirichlet series). R161_002 §6 asks for the test «Λ(2) ↦ −Λ(2)», linear. There is no quadratic term in the weight.
- U2: it is the central ground of the part, always on the radical and without sign for all P_T.
  · SP-161 (R161_002 §§3–4): proposed form «a_T = oriented pairings + compression leakages», OPEN without object;
    only the positive-weight branch was closed (Thm 8.1), not the leakage branch.
  · Double compression P S_N P = old causal observation (R161_004 Prop. 1.1): the new must come out of the block
    P S_N (1−P), whose exact kernel is R161_006; no sign.
  · Unitary leakage ‖(I−P_+)C_log g‖² (R161_020) and correlation X_T = ½‖(I+εC)g‖² (R161_021): correct squares, but
    there is no identity connecting them to the finite PC defect; L161.4/5 OPEN.
  · Word Π_T P_T S* as test (R161_022–023): collapses into the mixed pairing of (PC-ren) — tautology.
  · Position operator: D_Γ = Q + C_logQC_log gives coercivity 2T‖g‖² on Sonin sectors (R161_014) and the slope
    −2∫(t−T)|g|² (R161_015); the sign produced is always the automatic one (R161_016 Prop. 1.1).
  · Hankel block (I−P_+)M_χP_+: circular (R161_024 §3).
  · Finite rank: chamber 2,3,4; controls only the first collar (R161_016 §5); the derived row is tautological
    (R161_013 §3).
  · Accounting with the crossed Tate block: R161_009 fixes (α,β) via the crossed matrix; R161_022 isolates
    B_T^Tate; R161_023 proves that ⟨r,ΤPy⟩ = ⟨Sr,g⟩ and that the crossed matrix is not a Gram. The positive version by
    parity (README item 22, memo R161_032) lies outside this part; README item 33 says that at the order of source
    derivative that block vanishes by opposite parity.
- U3: no non-radical neutral vector is built. Contacts: indefinite crossed Tate matrix rejected as Gram
  (R161_023 §4); Kreĭn inertia of the scalar shadow of phase 116 cited (R161_011 §1); «2D^Γ − D^Poisson = 0»
  discarded as an indefinite conservation (R161_027 §5). The whole programme uses radical vectors of a
  semidefinite form (R161_021 §4).
- U4: there is no truncated Möbius. The analogue with Λ is the hyperbola remainder h(k) = Σ_{dm=k,d≤M,m≤N}Λ(d) at k > N
  (R161_001 Thm 2.1): coefficients ≥ 0 that do not make the sum of translations positive (R161_001 §6, R161_027 §4), and
  no positive weighting in N cancels them (R161_002 Thm 8.1). The remainder with Möbius weights c_N(k) does not appear.
- U5: exit A of R161_033 lies outside the part. Antecedents in this part: R161_016 §4 — completing the labelled
  family of Julia innovations into an orthogonal sum and summing afterwards is blocked by the divergence of
  exterior energy (phase 116); R161_016 §1 — the contraction with Julia defect gives the automatic arrow. README
  item 23 (summary of a later memo) explicitly asks for «a Parseval/Naimark dilation» to pass from the coherent
  sum to the direct sum.

### (e) Inconsistencies between memos

1. R161_010 Thm 3.1 was given as PROVED; retracted by R161_011 (the cosine scattering is missing). The README records it.
2. R161_017 §5 claims that after the scattering the homogeneous problem would remain; R161_019 corrects it (pole lattice).
3. R161_018 is titled NO-GO and its Cor. 5.1 says PROVED; the initial note (from R161_075) declares the identification
   ZA_∞ = [Z,D_Γ] = 0 not established. README item 8 and R161_019, 020, 025 still rely on R161_018 as
   proved.
4. R161_024 describes «cancellation by the continuous/Tate residue»; its own final correction says there is no residue
   that cancels. R161_025 confirms it.
5. R161_008 Thm 3.1 labels membership in H² as PROVED; the Paley–Wiener step in the strip 0 < Re z ≤ 1/2 does not
   write growth control (ARGUED at that point). R161_014 §1 (domain of G′) likewise.
6. README item 21 claims that the divisor seam vanishes; item 23 qualifies it (the coherent Gram step is missing);
   both are summaries of memos outside the part.
7. The status of R161_003 says «L161.3 OPEN», an object defined only in R161_004: retroactive annotation, not a
   contradiction.

### (f) Files read (complete reading with Read)

README.md (298 lines), R161_000 (85), R161_001 (185), R161_002 (183), R161_003 (216), R161_004 (193),
R161_005 (153), R161_006 (123), R161_007 (137), R161_008 (178), R161_009 (156), R161_010 (200), R161_011 (148),
R161_012 (149), R161_013 (127), R161_014 (159), R161_015 (175), R161_016 (231), R161_017 (227), R161_018 (203),
R161_019 (196), R161_020 (187), R161_021 (171), R161_022 (199), R161_023 (149), R161_024 (173), R161_025 (169),
R161_026 (192), R161_027 (167). Twenty-nine files, all read in full. `scripts/` only listed.
