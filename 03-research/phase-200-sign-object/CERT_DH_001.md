# CERT_DH_001: interval certificate for a negative witness of the window form of F_DH (phase 200, round 17C)

**Verifier.** Goal: upgrade the Davenport–Heilbronn falsifier from UNVERIFIED (P47 rem:FDH, "Ziad") to an
interval-arithmetic certificate. F_DH appears only as a
falsifier of window-form positivity (CITED: it has zeros off the line, Davenport–Heilbronn 1936).
Labels: everything computed is NUMERICAL except the §4 certificates, which are PROVED (arb balls, rigorous rounding).

## Summary

With the conventions of DH_TRANSFER_001 §1.3 (C₀^{DH} = log(5/π)+ψ(¾), kernel K_{3/4}, comb 2b_n/√n with
−F′/F = Σ b_n n^{−s}, P_T = e^{±t/2} conditions), **the certificate is PROVED at T = 9/5**:

- odd sector, orthogonal to sinh(t/2) (Ziad's sector): 𝔞_{9/5}^{DH}(F)/‖F‖² ∈ −7.051974709479(1)·10⁻⁹, radius < 10⁻¹⁸;
- full sector (two conditions): −2.379887118231·10⁻⁷, radius < 10⁻¹⁶;
- large margin at T = 2 (odd sector): −0.751936825418, radius < 10⁻¹⁰.

The witnesses are polynomials in t/T of degree ≤ 259 (≤ 199 at T = 2), with dyadic Legendre coefficients of denominator
2⁶⁰. Direction P₁ (and P₀ in the full sector) is solved in balls so that F lies **exactly** in P_T. By
lem:monoT, the form is not ≥ 0 on P_T for any T ≥ 9/5. This **reproduces Ziad**: same sector, same window, and same
order of magnitude (−7.05·10⁻⁹ versus −6.169·10⁻⁹, which is a Rayleigh quotient from a different test and hence larger).
Control: with the same template for L(s,χ₋₄) there is no negative eigenvalue above the noise floor (≈10⁻¹³).

## 0. Corpus and index check

- Index (`05-meta-and-planning/ROUTES-TRIED-INDEX/`): DH appears only as a CITED/UNVERIFIED falsifier. No
  entry contains a DH certificate. This is not a route toward D but the verification of an already-
  registered falsifier, so the no-retry rule does not apply.
- P47 rem:FDH (l. 8334): Ziad, odd test orthogonal to sinh(x/2), support on (−9/5, 9/5), ratio −6.169·10⁻⁹ with ball
  arithmetic, "plausible, unverified."
- DH_TRANSFER_001 §1.3–1.4 (data and parametric form; (F-DH-ex) ARGUED with T_DH unquantified).
- LEMMA_E_EPSTEIN_001 and its `cert_epstein.py`, and phase-198 `cert_falsifiers.py`: the pipeline whose template is reused.
  The new certificate uses arb (python-flint) instead of mpmath.iv, because degree 260 requires 7000 bits (§3).

## 1. Exact F_DH (NUMERICAL except where noted)

χ mod 5 with χ(2) = i: χ(1), χ(2), χ(3), χ(4) = 1, i, −i, −1, so χ(−1) = −1 and χ is odd.
κ = (√(10−2√5) − 2)/(√5 − 1) = 0.284079043840412296…

**Real coefficients (PROVED, algebra).** a_n = ½(1−iκ)χ(n) + ½(1+iκ)χ̄(n) = Re((1−iκ)χ(n)) = Re χ(n) + κ Im χ(n).
This gives (a₁, …, a₅) = (1, κ, −κ, −1, 0), periodic mod 5.

**−F′/F.** Since F·(−F′/F) = −F′, Σ_{d|n} a_d b_{n/d} = a_n log n, and hence
b_n = a_n log n − Σ_{d|n, 1<d<n} a_d b_{n/d}. The b_n are real, of both signs, and not multiplicative, and b_n = 0 if
5 | n. First values: b₂ = 0.19691, b₃ = −0.31209, b₄ = −1.44223, b₆ = 1.93636, b₉ = −2.28588, b₁₁ = 2.39790, …,
b₃₆ = −2.40515. The full table is in `check_fdh_out.txt`. Check: Σ_{n≤60} b_n n⁻³ = −0.001442, and
−F′/F(3) = −0.001419; the difference is consistent with the tail.

**Functional equation (NUMERICAL, 30 digits).** Λ_DH(s) = (5/π)^{s/2} Γ((s+1)/2) F_DH(s), with F_DH = 5^{−s} Σ_r a_r ζ(s, r/5).
One gets |Λ(s) − Λ(1−s)|/|Λ(s)| ≤ 2.5·10⁻³⁰ at s = 0.3+2i, 0.8+17.5i and 2−5i. Hence ε = +1.

**Zero off the line (NUMERICAL; existence CITED, Spira 1994).** Newton's method from the cited value converges to
ρ = 0.808517182456637385… + 85.699348485377592…i, with |F(ρ)| = 2·10⁻³⁰. The dual zero 1−ρ̄ gives |F| = 3·10⁻²⁹. The
optimal test at T = 2 has |F̂| maximal at ξ ≈ 84.5, next to γ₀ = 85.70: the negativity rests on that pair.

## 2. The window form and P_T

With F ∈ L²[−T, T], c(u) = ∫F(t)F(t−u)dt:

  𝔞_T^{DH}(F) = C₀ c(0) + ∫₀^{2T} (c(0) − c(u)) K(u) du + c(0) ∫_{2T}^∞ K − Σ_{2≤n<e^{2T}} (2b_n/√n) c(log n),

where

- C₀ = log(5/π) + ψ(¾) = log 5 − log π − γ + π/2 − 3 log 2 = −0.621152853202… (the conductor log 5 is already inside);
- K(u) = K_{3/4}(u) = 2Σ_k e^{−(2k+3/2)u} = 2e^{−3u/2}/(1 − e^{−2u}). This is the Lévy representation of Re ψ(¾ + iξ/2),
  which comes from Γ_ℝ(s+1) at ½ + iξ.

There is no polar term (r = 0). This is exactly the CERT_FALSIFIERS / cert_epstein template with (C₀, K, v) substituted,
as DH_TRANSFER §1.3 fixes.

**P_T.** The corpus convention is adopted (DH_TRANSFER §1.3): supp F ⊂ [−T, T] and ∫F e^{±t/2} = 0. With no pole, these
conditions have no polar content: they are a codimension-≤2 restriction that can only raise the infimum. Both
versions are reported (NUMERICAL, Galerkin float64):

| T | odd, P_T | odd, no conditions | full, P_T | full, no conditions |
|---|---|---|---|---|
| 1.8 | −7.052·10⁻⁹ | −8.04·10⁻⁹ | −2.380·10⁻⁷ | −2.52·10⁻⁷ |
| 2.0 | −0.7519 | −0.7644 | −0.7624 | −0.7538 (N=200) |

The moment conditions change nothing qualitatively. The certificate is produced in the strict version, with P_T.

## 3. Search for the witness (NUMERICAL)

**Why the first attempt was not enough.** Lemma E's monomial Galerkin (`cert_dh.py`, degree < 24–40) gives **positive**
and tiny eigenvalues at T = 1.8 (9.6·10⁻⁹ at degree 24; 3.8·10⁻¹³ at degree 40). The reason is resolution: the test
must concentrate F̂ near ξ ≈ 85.7, and a degree-N polynomial basis on [−T, T] resolves frequencies up to ≈ πN/(2T).
At T = 1.8 that requires N ≳ 100, and in practice 200–260.

**Legendre Galerkin** (`explore_leg.py`, float64). Uses basis P_j(t/T) with j < N and c_{jk}(u) by exact Gauss
quadrature, because the integrand is polynomial. The Lévy term is integrated with Gauss on [0, 2T] over
(c(0) − c(u))K(u), and the finite comb is evaluated at log n. The noise floor is ≈ 10⁻¹³. Lowest eigenvalue:

| T | odd sector (N = 260) | full sector |
|---|---|---|
| 1.5 | +4.1·10⁻⁹ | — |
| 1.6 | +2.6·10⁻¹³ (noise) | — |
| 1.7, 1.75 | noise (|·| < 10⁻¹³) | noise (N = 200, no conditions) |
| **1.8** | **−7.05·10⁻⁹** (N = 200: −6.24·10⁻⁹) | −2.38·10⁻⁷ |
| 1.85 | −4.34·10⁻² | — |
| 1.9 | −0.248 | — |
| 2.0 | −0.752 (N = 200) | −0.762 |
| 2.2 / 2.6 | −1.26 / −2.14 | — |

The crossing is very abrupt: log₁₀|λ| goes from −8 to −1.4 between T = 1.8 and 1.85. Below 1.75 double precision does
not resolve the sign. A positive Galerkin eigenvalue does not prove positivity, because Galerkin only gives upper
bounds on the infimum. That is why **there is no lower bound on T_DH**. What there is, is the certified upper bound
T_DH ≤ 9/5 (§4), with numerical evidence that the real threshold lies in [≈1.6, 1.8].

**Control (NUMERICAL).** With the same template, the same K_{3/4}, and the comb of L(s,χ₋₄) (q = 4, δ = 1, with Euler
product), N = 200 and T ∈ {1.8, 2.0, 2.5}, all eigenvalues stay in [−7·10⁻¹⁴, 0) (`control_chi4_out.txt`). DH's
negativity is not an artifact of the template or the quadrature.

## 4. Interval certificates (PROVED)

`cert_arb.py`, in arb balls (python-flint), evaluates 𝔞_T^{DH}(F)/‖F‖² for **one** explicit F:

1. **Exact test.** G₀ = Σ_{j≥2} (m_j/2⁶⁰) P_j(x) ∈ ℚ[x], with the rounded integer m_j from the Galerkin vector and the
   P_j from flint in exact form. Set G = G₀ + λ₁x (+ λ₀), and solve for λ₁ (λ₀) in balls from ∫G(x)sinh(Tx/2)dx = 0
   (∫G cosh = 0). The even and odd parts decouple. The moments are computed with the exact finite formula
   ∫₋₁¹ G e^{cx} = Σ_k (−1)^k [G^{(k)} e^{cx}]₋₁¹ / c^{k+1}. The true λ lies in the ball, so F = G(t/T) ∈ P_T
   exactly.
2. **Exact autocorrelation.** P(s) = ∫G(x)G(x−s)dx = Σ_k (−s)^k/k! [H_k(1) − H_k(s−1)], with H_k′ = G·G^{(k)}. Computed
   piecewise in ℚ[s] (G₀G₀, G₀x, xx, …), combined with λ in balls. Also c(u) = T·P(u/T).
3. **Lévy.** M_r = ∫₀^{2T} u^r K = r! 2^{−r} ζ(r+1, ¾) − 2Σ_k Γ(r+1, 2Ta_k)/a_k^{r+1}, with a_k = 2k + 3/2 (Hurwitz and
   upper Γ from arb). The sum over k is cut off with the explicit bound Γ(r+1, x) ≤ 2x^r e^{−x} for x ≥ 2(r+1), giving a
   remainder ≤ 2(2T)^r e^{−x_k}/(a_k(1−e^{−4T})) < 2^{−prec}. The tail ∫_{2T}^∞ K = 2Σ e^{−2Ta_k}/a_k is cut off after 200
   terms with a geometric remainder.
4. **Comb.** It is a **finite sum**: since supp c ⊂ [−2T, 2T], the n with log n ≥ 2T contribute c(log n) = 0. Hence
   no tail bound on the comb is needed, and the sign of b_n is irrelevant. For T = 9/5 the contacts are
   n ≤ 36 (e^{3.6} = 36.6), and log n < 2T is decided in balls. The b_n are obtained in balls via the recursion, with
   κ = (√(10−2√5)−2)/(√5−1) in arb.
5. **Precision.** The cancellation between r! 2^{−r} ζ and the upper Γ for r ≈ 520 requires 7000 bits at T = 9/5 (with 3000
   bits the ball blows up to ±10⁴⁸, which the script detects and reports as "NOT CERTIFIED"); at T = 2, 2500 suffice.

**Results** (`cert_*.txt`):

| T | sector | degree | contacts | Galerkin float64 | certificate 𝔞/‖F‖² | ‖F‖² |
|---|---|---|---|---|---|---|
| **9/5** | odd ⊥ sinh | ≤ 259 | 35 (n ≤ 36) | −7.052035·10⁻⁹ | **[−7.05197470947908·10⁻⁹ ± 4·10⁻²⁵]** | 0.4602380650 |
| 9/5 | full (P_T) | ≤ 259 | 35 | −2.379888·10⁻⁷ | [−2.37988711823112·10⁻⁷ ± 3·10⁻²²] | 0.5409810068 |
| 2 | odd ⊥ sinh | ≤ 199 | 53 (n ≤ 54) | −0.7519368 | [−0.751936825418122 ± 2·10⁻¹¹] | 0.2756383086 |

Decomposition at T = 9/5, odd sector, over ‖F‖²: C₀ = −0.621152853, Lévy + tail = 3.009035029, and comb = 2.387882183.
The total is −7.05·10⁻⁹: a 9-digit cancellation, which is Ziad's "near-degeneracy."

**Vectors.** The floating-point input vectors are `vec_T1.8_odd_N260.json`, `vec_T1.8_full_N260.json`, and
`vec_T2_odd_N200.json`. The integer numerators m_j of the witness (denominator 2⁶⁰, Legendre coefficients j ≥ 2) are
in `*_witness_den2^60.json`. The certificate is deterministic: `python3 cert_arb.py vec_T1.8_odd_N260.json 9 5 60 7000`
(about 10 minutes).

**Match with Ziad.** The sector (odd, orthogonal to sinh(t/2)), the window (9/5), and the order of magnitude all match.
Our value is lower (−7.05 versus −6.17·10⁻⁹), as expected from a richer Galerkin subspace. With
N = 200 we get −6.24·10⁻⁹, very close to theirs. Ziad speaks of support on the open interval (−9/5, 9/5). Our certificate
is on the closed window T = 9/5, and by lem:monoT it holds for every T ≥ 9/5. For T < 9/5 the question remains open (§3).

**What depends on what.** The certificate is PROVED for the form defined in §2. That this form is the "window form of
F_DH" in the sense of P47 rests on the DH_TRANSFER §1.3 verification against lem:K / eq:m / eq:Aform, which is not
redone here. The χ₋₄ control is NUMERICAL evidence that the template is correct.

## 5. Entries for the editor

**CERT_FALSIFIERS, row 12 (proposed):**
> | 12 | Davenport–Heilbronn F_DH (χ mod 5, χ(2)=i, κ=0.2840790…; Γ_ℝ(s+1), q=5, no pole, no Euler) | T=9/5, odd
> sector ⊥ sinh(t/2), degree ≤259 in P_j(t/T), dyadic coefficients 2⁻⁶⁰ | 𝔞/‖F‖² ∈ [−7.05197470947908e−9 ± 4e−25]; full
> −2.3798871e−7; T=2: −0.7519368 | **PROVED** (arb, 7000 bits; CERT_DH_001) |

**ROUTES-TRIED index entry (3–4 lines):**
> CERT_DH_001 (phase 200, r17C): DH falsifier **certified**. 𝔞_T^{DH} is not ≥ 0 on P_T for T ≥ 9/5 (PROVED,
> intervals; reproduces Ziad, −7.05e−9 in the odd sector; −0.75 at T=2). Any method using only FE + Γ factor +
> Dirichlet series with bounded real coefficients (DH_TRANSFER's theory 𝔗₁) does not prove window positivity at any
> T ≥ 9/5. Lower bound on T_DH: open (numerically the threshold lies in [1.6, 1.8]).

**Note for P47 rem:FDH (English, to replace "we have not reproduced it; we label it plausible, unverified"):**
> We have reproduced and certified it: in the odd sector orthogonal to $\sinh(t/2)$ at $T=\frac95$, an explicit
> polynomial test of degree $\le259$ in $t/T$ with dyadic Legendre coefficients gives
> $\mathfrak a^{\mathrm{DH}}_{9/5}(F)/\|F\|^2\in-7.05197470947908\cdot10^{-9}\pm4\cdot10^{-25}$ (arb ball arithmetic), and
> $-0.7519368\ldots$ at $T=2$; by Lemma~\ref{lem:monoT} the form fails to be nonnegative on $\PT$ for all $T\ge\frac95$. \emph{Proved.}

## 6. What remains

- A **lower** bound on T_DH, i.e. certified positivity for T < 9/5. This is a different type of certificate (lower
  bound on the infimum, dual) and was not attempted. Numerically the sign is not resolved below T ≈ 1.75 in
  float64. An arb Galerkin with N ≈ 260 would resolve it and would take hours.
- Independently redo the identification of the §2 form with eq:Aform for (δ, q) = (1, 5). It is currently
  verified in DH_TRANSFER and backed numerically by the χ₋₄ control.

## Files

`CERT_DH_001_data/`:

- `check_fdh.py` / `_out.txt`: κ, a_n, FE, zero off the line, b_n.
- `cert_dh.py`: monomial template in the style of Lemma E. Only resolves low degrees; documented as the failed attempt.
- `explore_leg.py`: Legendre Galerkin, with scans in `sc260_*.txt` and `scan_full40.txt`.
- `control_chi4.py` / `_out.txt`.
- `cert_arb.py`: the certificate.
- `cert_T9_5_odd_N260.txt`, `cert_T9_5_full_N260.txt`, `cert_T2_odd_N200.txt`.
- `vec_*.json` and `*_witness_den2^60.json`.
