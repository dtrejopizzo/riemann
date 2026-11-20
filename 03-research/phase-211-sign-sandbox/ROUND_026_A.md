# Round 26 A — Computer-assisted lower certificate for λ_A beyond ½log5

Target: a certified lower bound λ_A(T) ≥ μ > 0 at windows T > ½log5, by the lower certificate of Paper 47
prop:lowercert (frequency-truncated symbol, Legendre block, Haynsworth inertia, interval Cholesky), first at T = 1.0,
then as far as the method reaches. Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.
Notation of STATEMENT_001 and Paper 47 §sec:log5, app. subsec:encllog5: s_T(τ) = m(τ) − Σ_{n∈𝒩_T} v_n cos(τ log n),
𝒜 = Σ_{n∈𝒩_T} v_n, e_l the normalised Legendre basis of L²(I_T), j_l spherical Bessel functions, S_c the
time–frequency concentration operator with c = Tτ_N, Λ_k(c) = tr(P_k^⊥S_cP_k^⊥).

## 0. Corpus check
Read: Paper 47 §sec:log5 (thm:log5A, thm:log5W, rem:log5scope, prop:onewindow, cor:beyond5) and app. subsec:encllog5
(prop:lowercert and its computation); ROUTES-TRIED-INDEX rows on certificates (P155 certificates at log 2, ½log3,
½log5; Mori ½log15 CITED; Liu 17/16 CITED as preprint); STATE_002 §1 R1, R15 (E_T and the Neumann/Schur form),
ROUND_017_C, ROUND_018_A (arb compression with Hilbert–Schmidt tail).
What differs. Nothing indexed is retried as a sign mechanism: this round is a certificate at a single window, in the
class already used by Paper 47 at ½log5. The differences are computational and are what make T = 1.0 reachable:
(i) the floor s_∞ is not taken as m(τ_N) − 𝒜 but certified as a lower bound of s_T on [τ_N, τ_B] by an interval scan,
with m(τ_B) − 𝒜 ≥ s_∞ beyond (m increasing); (ii) quadrature panels of length 8 away from τ = 0, with the Bernstein
ellipse sized by the distance to the poles of ψ(¼ ± iτ/2), which lie on the imaginary axis (≈ 12 nodes per unit
length instead of 92); (iii) the spherical Bessel values come from the three-term recurrence in ball arithmetic at
adaptive precision from exact nodes, with the Lipschitz bound |j_l′| ≤ 1 for the node radius; (iv) the trace
Λ_{k_1} of the complement is computed from the same quadrature (diagonal of S_c) instead of the crude Taylor bound,
which lets the Cholesky block stop at k_1 ≈ c instead of ≈ ec/2; (v) positive definiteness is certified by
recursive block Schur complements with interval linear solves. The certificate block E_T of ROUND_005_C and the
Legendre compression of ROUND_017_C are not used: the frequency-truncated lower form already has a band-limited
remainder, whose Legendre columns decay super-exponentially past degree ≈ c, which is what the Schur tail needs.

## 1. The certificate (statement and proof skeleton)

### 1.1 Lower form (PROVED, Paper 47 prop:lowercert with a certified floor)
Fix T, τ_N > 0 and s_∞ > 0. Suppose (F1) s_T(τ) ≥ s_∞ for |τ| ≥ τ_N. Put g = (s_∞ − s_T)1_{|τ|<τ_N},
𝒢 = Q_T g(D) Q_T. Then a_T(F) ≥ s_∞‖F‖² − ⟨𝒢F,F⟩, and 0 ≤ 𝒢_± ≤ ω_± S_c with c = Tτ_N,
ω_+ = s_∞ − C_0 + 𝒜, ω_− = m(τ_N) + 𝒜 − s_∞. The rest of prop:lowercert is unchanged, with one change in (a):
on Y = span{e_l : l ≥ k_1} (parity fixed), ‖P_Y𝒢_+P_Y‖ ≤ ω_+ tr(P_Y S_c P_Y), and the trace is
    tr(P_Y S_c P_Y) = Σ_{k_1 ≤ l < K_2, l ≡ par} (2T/π)(2l+1)∫_0^{τ_N} j_l(τT)² dτ + (tail over l ≥ K_2) ≤ (that sum) + Λ*_{K_2}(c),
each diagonal entry being a quadrature with its own ellipse remainder. Proof: ⟨S_c e_l, e_l⟩ = (1/2π)∫_{|τ|<τ_N}|ê_l|² and
|ê_l(τ)|² = 2T(2l+1) j_l(τT)²; the tail is cor:P1 of Paper 47. ∎
(F1) is certified as follows: m is increasing on [0,∞) (lem:mbounds(i)) and the comb is ≥ −𝒜, so s_T ≥ m(τ_B) − 𝒜 on
|τ| ≥ τ_B; on [τ_N, τ_B] the interval extension of s_T on 512 boxes per unit length is checked to exceed s_∞.

### 1.2 Quadrature (PROVED bound)
G_{il} = (2T/π)√((2i+1)(2l+1))(−1)^{(l−i)/2}∫_0^{τ_N} g j_i(τT) j_l(τT)dτ (i ≡ l mod 2). Panels: [0,20] in 40 panels of
length ½ with 46 Gauss nodes and ρ = 3.2 (as in Paper 47); [20, τ_N] in panels of length 8 with 92 nodes and ρ = 2
(ellipse semi-axes a = 5, b = 3). On a panel centred at c_0 ≥ 24 the ellipse stays at real part ≥ c_0 − 5 ≥ 19, so with
w = ¼ ± iτ/2 one has |Im w| ≥ 9.5 and ψ(w) = ψ(w + 10) − Σ_{k<10}(w + k)^{−1} with |w + k| ≥ max(Re(w + k), |Im w|) and
Binet's bound for Re(w + 10) ≥ 8.75; |cos(τ log n)| ≤ cosh(b log n), |j_l(z)| ≤ e^{|Im z|}. Remainder (ATAP Thm 19.3):
(64/15)·L·M ρ^{−2N}/(ρ² − 1) per panel, summed over panels: 4.73·10⁻⁴⁵ per raw entry at T = 1 (3.2·10⁻⁴⁶ for the trace
integrals), added as a ball before scaling.

### 1.3 Bessel values (PROVED enclosures)
Nodes τ_q are balls of radius ≤ 2^{−320}. j_l(x) is evaluated at the exact midpoint x̃ of x = τ_qT by the forward
recurrence j_{l+1} = ((2l+1)/x̃)j_l − j_{l−1} from j_0, j_1 in ball arithmetic at precision 1.6x̃ + 600 bits (raised by 1.5×
until every radius is < 2^{−330}), and the radius of x is added using |j_l′| ≤ 1. Beyond the first l > x̃ with
x̃^l/(2l+1)!! < 2^{−330} the value is replaced by the ball [0 ± 2^{−320}], valid because |j_l(x)| ≤ x^l/(2l+1)!! and the
right side decreases for l > x/2 (the bound at the cut is checked in balls).

### 1.4 Positive definiteness (PROVED criterion)
After the Householder congruence and the 2×2 Haynsworth step of Paper 47 (unchanged), the Schur complement S (ball
matrix, dimension dim E − 1) is certified positive definite as follows: an approximate Cholesky factor of its
midpoint is computed recursively (block 2×2, approximate solves), X ≈ L^{−1} is kept as an exact lower-triangular matrix
with non-zero diagonal, and M = XSXᵀ is formed in ball arithmetic. If every Gershgorin disc of M lies in (0,∞), then M,
hence S, is positive definite (X invertible). This replaces the interval Cholesky of Paper 47, whose ball radii grow
exponentially at dimension ~10³ (observed: radius 10⁻⁴¹ → 0.47 after 27 elimination steps in a 39×39 leaf).

### 1.5 Validation at ½log5 (NUMERICAL reproduction of a PROVED result)
With τ_N = 244, s_∞ = 7/10, k_1 = 280, K_2 = 330, the pipeline reproduces thm:log5A exactly: even sector certified at
μ = 2.5·10⁻¹², fails at 3·10⁻¹²; odd sector certified at 3.0·10⁻¹⁰ (12 s build, 2 s certificate).

## 2. The window T = 1 (PROVED, computer-assisted)

Contact set 𝒩_1 = {2,3,4,5,7} (log 8 > 2), 𝒜 = 5.852. Data: s_∞ = ¼, τ_N = 2500 (scan of s_T on [2500, 2809]: min of
the lower enclosures 0.621 > ¼; m(2809) − 𝒜 > ¼), c = 2500, ω_+ = 11.4747, quadrature 30360 nodes, K_2 = 3470
(Λ*_{K_2}(c) = 8.9·10⁻⁶⁹), k_1 = 2550 (dim E = 1275 per parity), tr(P_YS_cP_Y) ≤ 3.49·10⁻⁹ (even), 2.28·10⁻⁹ (odd),
q_Y ≥ 0.2499999, tail box β = 2.2·10⁻³³, entry radii of S ≤ 1.5·10⁻⁴¹, det B = −2.175 (even), −0.175 (odd), 320-bit balls.

| sector | certified μ | failed μ | Gershgorin lower bound of XSXᵀ at the certified μ |
|---|---|---|---|
| even | 1.0·10⁻²³ | 1.5·10⁻²³ (midpoint Cholesky breaks: the lower form itself is below) | ≥ 0.9999 |
| odd | 1.5·10⁻²³ (not pushed further) | — | ≥ 0.9999 |

**Theorem 26A.1 (PROVED, computer-assisted).** λ_A(1) ≥ 1.0·10⁻²³, hence λ_A(T) ≥ 1.0·10⁻²³ for every 0 < T ≤ 1
(lem:monoT). The Galerkin value 1.74·10⁻²³ (NUMERICAL, an upper bound) is within a factor 1.74 of the certified bound.

Timings (20-core machine, one core per process): Gram build 5 processes × 2000–2400 s (bottleneck: Python-level filling of
the 1735 × 1200 node blocks and recurrences at 4000–4600 bits for the large nodes; matrix products in Arb are ≈ 20 %);
merge 3 min; one certificate (one parity, one μ) 140 s alone, ≈ 1200 s with eight running concurrently.
Reproduction: tools/cert_window/build_G.py 1 2500 1 4 3470 320 G_T1.pkl (PART/NPART env for parallel parts),
combine.py, cert.py G_T1.pkl <par> 2550 <mu>.

Relation to the cited range. T = 1 lies inside the cited ranges (Liu, T ≤ 17/16, preprint; Mori, T ≤ ½log15, unrefereed),
so Theorem 26A.1 is not beyond the cited frontier; it is an independent certificate with the constant 10⁻²³ against
Liu's 2^{−151} ≈ 3.5·10⁻⁴⁶ at T = 1, and it extends the in-paper certified range of Paper 47 from ½log5 to 1.

## 3. Reach of the method: why ½log15 + 0.01 is out of range here

### 3.1 Two forced sizes (PROVED)
Let a certificate of the class of §1 (constant floor s_∞ > 0 beyond τ_N, Legendre or any other block E, complement
bound q_Y = s_∞ − μ − ω_+·tr(P_{E^⊥}S_cP_{E^⊥}) > 0) succeed at T. Then
(i) τ_N ≥ τ_0(T; s_∞) := sup{τ : s_T(τ) < s_∞} (else the lower symbol is not below s_T);
(ii) dim E ≥ #{j : λ_j(S_c) > s_∞/ω_+} − 0 ≥ #{j : λ_j(S_c) > ½}, c = Tτ_N (both parities together), because by Ky Fan
tr(P_{E^⊥}S_cP_{E^⊥}) ≥ Σ_{j > dim E} λ_j(S_c), and s_∞/ω_+ < ½ (ω_+ ≥ 𝒜 − C_0 > 5 > 2s_∞ for T ≥ ½log5 and s_∞ ≤ 1).
By the Landau–Widom count (CITED) #{λ_j(S_c) > ½} = 2c/π + O(log c). So dim E ≳ (2/π)Tτ_0(T; s_∞).
The quadrature has to resolve [0, τ_N], so the Gram build costs ≳ (dim E)²·τ_N operations and the memory is ≈ (dim E)²
balls.

### 3.2 The threshold τ_0 (NUMERICAL, double-precision scan of s_T at step 0.01; not a certified quantity)

| T | 𝒩_T | 𝒜 | τ_0(T; 0+) | τ_0(T; 0.3) | (2/π)Tτ_0(T; 0.3) |
|---|---|---|---|---|---|
| 1.0 | 2,3,4,5,7 | 5.852 | 1550 | 2448 | 1560 (used: dim E = 2550 in Legendre degrees) |
| 1.2 | + 8, 9, 11 | 8.521 | 19852 | 19852 | 1.5·10⁴ |
| ½log15 + 0.01 = 1.364 | + 13 | 9.944 | 77404 | 132508 | 1.15·10⁵ |
| 1.4 | + 16 | 10.29 | 132508 | 183135 | 1.6·10⁵ |
| 1.5 | + 17, 19 | 13.02 | ≥ 3.8·10⁵ (scan range) | ≥ 3.9·10⁵ | ≥ 3.7·10⁵ |

The growth is that of 2πe^{𝒜(T)} damped by the rarity of simultaneous alignment of the phases τ log p (Kronecker), i.e.
doubly exponential in T, as rem:log5scope and prop:env of Paper 47 predict.

### 3.3 Consequence (NO-GO for this machine, not in principle; NUMERICAL sizes)
At T_* = ½log15 + 0.01 the certificate needs dim E ≥ 1.1·10⁵ (≥ 5.5·10⁴ per parity, Legendre ≈ 1.6× more), i.e. a dense
ball matrix of ≥ 3·10⁹ entries per parity (≥ 250 GB at 320–400 bits) and ≳ 10¹⁵–10¹⁶ ball multiply-adds for the Gram
build. Precision is not the bottleneck: the margin ≈ 10⁻⁶¹ needs entry radii ≈ 10⁻⁸⁰ (about 150 Gauss nodes per panel and
≈ 450-bit balls, a factor ≈ 2 in cost); dimension is. On the available machine (20 cores, 31 GB) the largest reachable
window of this class is below the entry of the contact 8 at ½log8 = 1.0397 plus a margin (dim E ∝ τ_0, which jumps with
each new contact: 𝒜 increases by v_8 = 0.49 at ½log8). Windows 1.2, ½log15 + 0.01, 1.4, 1.5 are out of reach.
What would change the class: a complement bound that does not need a positive floor of the symbol at every frequency
beyond τ_N, i.e. that uses the averaging of s_T over frequency windows of width ≈ π/T seen by functions supported on I_T
(packet bounds, Q12 of STATE_002, proved there only for T ≤ log 2 for all profiles). This is not attempted here.

## 4. The window T = 1.035 (PROVED, computer-assisted): the last window before the contact 8

Same contact set {2,3,4,5,7} (½log8 = 1.03972), same s_∞ = ¼ and τ_N = 2500 (s_T does not depend on T inside a fixed
contact set, so the scan of §2 applies verbatim), T = 207/200 exactly, c = 2587.5, K_2 = 3590, k_1 = 2640 (dim E = 1320
per parity), quadrature remainder 4.85·10⁻⁴⁵ per raw entry, tr(P_YS_cP_Y) ≤ 1.54·10⁻⁹ (even), 1.01·10⁻⁹ (odd),
det B = −2.265 (even), −0.195 (odd).

| sector | certified μ | failed μ |
|---|---|---|
| even | 2·10⁻²⁶ | 4·10⁻²⁶ (midpoint Cholesky of S breaks) |
| odd | 6·10⁻²⁶ (not pushed further) | — |

**Theorem 26A.2 (PROVED, computer-assisted).** λ_A(207/200) ≥ 2·10⁻²⁶; hence λ_A(T) ≥ 2·10⁻²⁶ for 0 < T ≤ 1.035.
(Galerkin interpolation between 1.74·10⁻²³ at T = 1 and 2.24·10⁻²⁷ at T = 1.05 gives ≈ 3·10⁻²⁶, NUMERICAL.)

Timings: build 8 processes × 1640–2300 s; certificate ≈ 1100 s per (parity, μ) with six running concurrently.

