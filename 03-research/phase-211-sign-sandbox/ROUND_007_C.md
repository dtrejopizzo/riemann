# ROUND_007_C — Certified falsifiers: λ_A(T; w) < 0 for a_3, the Beurling shift 3 → 3.2, and 1.1Λ

Target (★): λ_A(T) ≥ 0 for every T, for the explicit form a_T of DOSSIER_001 §1.1. This memo does not touch (★) for Λ.
It turns three falsifier values that the phase has used as NUMERICAL into PROVED statements, by exhibiting explicit
witnesses F ∈ P_T and enclosing a_T^w(F) in ball arithmetic.

Notation (DOSSIER_001 §1.1). For a finite comb w = Σ_x w_x δ_x (x ∈ (0, 2T)),
    a_T^w(F) = C_0‖F‖² + Lev(c_F) − Σ_x w_x c_F(x),   Lev(Φ) = ∫_0^∞ (Φ(0) − Re Φ(u)) K(u) du,
    K(u) = 1/(2 sinh(u/2)) + 1/(2 cosh(u/2)),   C_0 = ψ(1/4) − log π,
    λ_A(T; w) = inf{a_T^w(F) : F ∈ P_T ∩ D_T, ‖F‖ = 1},  P_T = {A(F) = ∫F e^{t/2} = 0, B(F) = ∫F e^{−t/2} = 0}.
Combs (v_n = 2Λ(n)/√n):
- a_3 (the prime 2 deleted): atoms log 3 (v_3), log 5 (v_5) [+ further prime powers ≥ 7, irrelevant for 2T < log 7].
- Beurling shift 3 → 3.2: atoms log 2 (v_2), log 3.2 (weight v_3 = 2log3/√3), log 4 (v_4), log 5 (v_5).
- 1.1Λ: atoms log n with weights 1.1·v_n, n = 2, 3, 4, 5, 7 (all prime powers with log n < 2).

## Corpus check

Index searched for "certif* falsif*", "falsifier", "Beurling 3.2", "1.1Λ", "a_3". The values −0.507 (a_3), −0.240 / −0.206
(3 → 3.2) and λ_A(T; 1.1Λ) < 0 appear in ROUND_002_E §3, ROUND_005_C §4.6, ROUND_003_A Lemma 4 / ROUND_005_A §7 only as
Galerkin values (NUMERICAL); REVIEW_004 §6 item 2 records that certifying a_3 would make the NO-GO of ROUND_005_C §5.3(iv)
fully PROVED. Nothing here is a retry of a route: it is a certificate for existing falsifiers. The literature caution
L84 (truncated-spectrum negative eigenvalues certify nothing below a budget B_T) does not apply: each witness below is a
single explicit function in P_T whose form value is enclosed rigorously, not an eigenvalue of a truncated matrix, and the
values are ≤ −0.18 in absolute form value.

## 1. Two elementary lemmas

Lemma 1 (upper bound by a witness; PROVED). If F ∈ P_T ∩ D_T, F ≠ 0 and a_T^w(F) < 0, then λ_A(T; w) ≤ a_T^w(F)/‖F‖² < 0.
Proof. Definition of the infimum (the form is homogeneous of degree 2). ∎

Lemma 2 (monotone extension; PROVED). Let w be a comb on (0, ∞) and w|_T its restriction to (0, 2T). If F ∈ P_T then its
zero extension F̃ lies in P_{T'} for every T' ≥ T and a_{T'}^{w|_{T'}}(F̃) = a_T^{w|_T}(F).
Proof. A, B, ‖·‖ and c_F are unchanged by zero extension; c_F vanishes on |u| ≥ 2T, so atoms in [2T, 2T') contribute 0
and the Lévy integral is the same. ∎
Hence each certificate below holds for every T' ≥ T (for a_3 and 1.1Λ with the full infinite combs a_3, 1.1Λ restricted
to the window; for the Beurling system with any continuation of its atom set beyond 5).

Lemma 3 (Lévy form on Dirichlet sines; PROVED). Put L = 2T, ω_k = kπ/L, s = t + T, and F = Σ_{k≤N} a_k sin(ω_k s) on
(−T, T). Then:
(i) F ∈ H¹_0(I_T) ⊂ D_T, ‖F‖² = T Σ a_k²; F is even if only odd k occur and odd if only even k occur; for even F,
    A(F) = B(F); for odd F, B(F) = −A(F). Hence P_T is cut out by the single condition A(F) = 0 in either parity.
(ii) A(F) = Σ a_k e^{−T/2} Im[(e^{(1/2+iω_k)L} − 1)/(1/2 + iω_k)], B(F) the same with 1/2 → −1/2.
(iii) for 0 ≤ u ≤ L, c_F(u) = ∫_u^L F(s)F(s−u) ds = ½ Σ_{j,k} a_j a_k [I(ω_j − ω_k, ω_k u) − I(ω_j + ω_k, −ω_k u)],
    I(α, β) = (sin(αL + β) − sin(αu + β))/α (α ≠ 0), I(0, β) = (L − u) cos β; c_F is entire in u.
(iv) ∫_L^∞ K = −log tanh(T/2) + π − 2 arctan(e^T) (antiderivatives log tanh(u/4) and 2 arctan(e^{u/2})), so
    Lev(c_F) = c_F(0)∫_L^∞K + ∫_0^L (c_F(0) − c_F(u))K(u) du.
(v) for 0 < δ ≤ L: 0 ≤ ∫_0^δ (c_F(0) − c_F(u))K(u) du ≤ ‖F′‖²(δ²/4 + δ³/12), ‖F′‖² = T Σ a_k² ω_k².
Proof. (i)–(iv) are direct integration (parity: sin(ω_k(t+T)) = sin(kπ/2 + ω_k t)). (v): |c_F(u)| ≤ c_F(0) gives the
lower bound. Since F ∈ H¹_0, c_F″ = −c_{F′}, so |c_F″| ≤ ‖F′‖², and c_F′(0) = −∫F F′ = 0; Taylor gives
c_F(0) − c_F(u) ≤ ‖F′‖²u²/2. Also K(u) ≤ 1/u + 1/2 (sinh x ≥ x, cosh ≥ 1). Integrate. ∎

Enclosure method. All quantities are evaluated in arb ball arithmetic (python-flint 0.9, 256-bit precision): C_0 via
acb digamma; the tail (iv) in closed form; the comb part Σ w_x c_F(x) exactly by (iii); the integral over [δ, L] by
acb.integral (rigorous Gauss–Legendre with analytic error bounds on complex ellipses; the integrand is meromorphic, poles of
K at 2πiℤ and iπ(2ℤ+1), the pole at 0 outside [δ, L]); [0, δ] by (v), δ = 10⁻⁶. The two-coefficient solve for A(F) = 0 is
done in balls; the exact witness is the function with the exact solved coefficient, which lies in the printed ball, and
every enclosure contains its true value. Script: tools/falsifier_cert.py, tools/falsifier_cert_run.py
(`python3 falsifier_cert_run.py a3 8 1e-6`, `beur 8 1e-6`, `1.1L 12 1e-6`).

## 2. The certificates

### Theorem 1 (a_3; PROVED). At T = ½log5 + 10⁻⁴, λ_A(T; a_3) ≤ −0.50528 < 0; by Lemma 2 also for every T′ ≥ T.
Witness (even, N = 8): F = Σ a_k sin(kπ(t+T)/2T) with
    a_1 = −384199/10⁶,  a_5 = 172109/10⁶,  a_7 = −4131/125000,  a_2 = a_4 = a_6 = a_8 = 0,
    a_3 = x the unique real with A(F) = 0;  x ∈ 1.0000005632467671625 ± 4.3·10⁻²⁰.
Enclosures:
    ‖F‖² = c_F(0) ∈ 0.948337231229387 ± 5·10⁻¹⁵,   ‖F′‖² ∈ 30.47902244 ± 4·10⁻⁹,
    C_0 ∈ −5.37218341922566558 ± 4·10⁻²⁰,   ∫_{2T}^∞K ∈ 1.80330599255814873 ± 3·10⁻²⁰,
    ∫_δ^{2T}(c_F(0) − c_F(u))K ∈ 3.14169227831778053 ± 7·10⁻²¹,   ∫_0^δ ∈ [0, 7.7·10⁻¹²],
    Arch(F) ∈ −0.24280705908 ± 6·10⁻¹²,   Σ w_x c_F(x) = v_3 c_F(log3) + v_5 c_F(log5) ∈ 0.236375494575948 ± 2·10⁻¹⁵,
    a_T^{a_3}(F) ∈ −0.47918255366 ± 7·10⁻¹²,   a_T^{a_3}(F)/‖F‖² ∈ −0.5052870834 ± 2·10⁻¹¹.
(Note: the archimedean part alone is already negative on this F; the deleted contacts 2, 4 are what Λ uses to
compensate.)

### Theorem 2 (Beurling shift 3 → 3.2; PROVED). At T = ½log5 + 10⁻⁴, λ_A(T; w_{3.2}) ≤ −0.23448 < 0, and for T′ ≥ T.
Witness (even, N = 8):
    a_1 = −4887/15625,  a_3 = 3507/12500,  a_7 = 1039/125000,  a_2 = a_4 = a_6 = a_8 = 0,
    a_5 = x with A(F) = 0;  x ∈ 1.0000016578009623462 ± 4.1·10⁻²⁰.
Enclosures: ‖F‖² ∈ 0.946958145049132 ± 5·10⁻¹⁵; ∫_δ^{2T} ∈ 3.56661806397264891 ± 4·10⁻²⁰; ∫_0^δ ∈ [0, 2.0·10⁻¹¹];
    Arch(F) ∈ 0.1870405161 ± 3·10⁻¹¹; comb part ∈ 0.409085479019024 ± 5·10⁻¹⁵;
    a_T(F) ∈ −0.2220449629 ± 2·10⁻¹¹;  ratio ∈ −0.2344823412 ± 5·10⁻¹¹.

### Theorem 3 (1.1Λ; PROVED). At T = 1, λ_A(1; 1.1Λ) ≤ −0.078244 < 0, and for every T′ ≥ 1.
Witness (odd, N = 12):
    a_2 = 9143/50000,  a_4 = 172617/10⁶,  a_6 = 159663/10⁶,  a_8 = −454879/500000,  a_12 = 82331/125000,
    all odd-index a_k = 0,  a_10 = x with A(F) = 0;  x ∈ −0.99999732355597536013 ± 9·10⁻²².
Enclosures: ‖F‖² ∈ 2.35019813544511 ± 5·10⁻¹⁵; ‖F′‖² ∈ 535.3460318 ± 5·10⁻⁸; ∫_{2}^∞K ∈ 1.47696367646054272 ± 2·10⁻²⁰;
    ∫_δ^{2} ∈ 11.0811872257443559 ± 2·10⁻¹⁹; ∫_0^δ ∈ [0, 1.4·10⁻¹⁰]; Arch(F) ∈ 1.9266490492 ± 9·10⁻¹¹;
    comb part ∈ 2.11053797193042 ± 2·10⁻¹⁵;  a_1(F) ∈ −0.1838889227 ± 9·10⁻¹¹;  ratio ∈ −0.0782440084 ± 6·10⁻¹¹.
(An even 8-sine witness also works: N = 8 gives ratio −0.0452631179 ± 6·10⁻¹¹; the 12-sine one is the stated one.)

Consistency checks (NUMERICAL, not used in the proofs). The certified ratios coincide to 10 digits with the double-precision
Galerkin minimum of the same 8- resp. 12-dimensional spaces, and lie above the larger-space values of ROUND_005_C §4.6
(−0.5074 for a_3, −0.2398 for 3 → 3.2 at T₁ = ½log5 + 10⁻³), as they must. The same code with the true comb Λ returns
positive Galerkin minima (1.1·10⁻⁸ at ½log5 + 10⁻⁴, 6.8·10⁻¹¹ at T = 1, N = 12), confirming the sign conventions.

## 3. Consequences for the phase register

1. ROUND_005_C §5.3(iv) (identity-based sign mechanisms on E_T: Λ∗1 = log, Selberg identities, Euler-factor bounds,
   the Lévy kernel identity of Prop. 3). Its logic is PROVED (those identities hold verbatim for a_3 and for the
   Beurling shift); its falsifiers are now PROVED: λ_A(T; a_3) < 0 and λ_A(T; w_{3.2}) < 0 for every T ≥ ½log5 + 10⁻⁴,
   in particular at T₁ = ½log5 + 10⁻³ (Lemma 2). REVIEW_004 §6 item 2 becomes **NO-GO (PROVED)**. Precisely: any argument
   that derives (SL_T) or λ_A(T) ≥ 0 at some T ≥ ½log5 + 10⁻⁴ using only identities valid for a_3 or for the 3 → 3.2 system
   is refuted. (The failure on E_T itself follows a fortiori only if the witness lies in E_T; the class statement of
   005_C is about the conclusion λ_A ≥ 0, which the certificates refute directly.)
2. ROUND_002_E. The λ_A column for (b) "no 2" and (f) "3 → 3.2" at T₁ and T = 0.9 becomes PROVED as an upper bound:
   λ_A ≤ −0.5052 and ≤ −0.2344 respectively (Lemma 2). The Θ_T column is NOT certified here: Θ_T(w) =
   max_μ λ_min(Arch − μΠ_w) < 0 needs witnesses covering every μ ∈ ℝ. A sufficient certificate (PROVED criterion): two
   functions F_± ∈ P_T with Arch(F_+) − μΠ(F_+) < 0 for μ > μ_+ and Arch(F_−) − μΠ(F_−) < 0 for μ < μ_− with μ_+ < μ_−
   (each F gives a half-line, since the expression is affine in μ). This is OPEN (not attempted); so ROUND_002_E's
   statement "Θ_T ≥ 0 fails for deletion of 2 and the Beurling shift" stays NUMERICAL, while the weaker falsifier
   statement "(★)_T fails for these combs" is PROVED.
3. ROUND_005_A §7 / REVIEW_004 §6 item 3 (Π-Krylov family). The fact used there, λ_A(T; 1.1Λ) < 0 "at T ≤ 1.0", is
   PROVED at T = 1.0 (and every T ≥ 1); for T < 1 it stays NUMERICAL (ROUND_003_A). So the statement "the bounded-j Krylov
   family does not reject c = 1.1 at T = 1.0 although (★) fails there for 1.1Λ" has its falsifier half PROVED; the
   non-rejection half (positivity of the pencil on K_j) remains NUMERICAL. Item 3 stays NO-GO (NUMERICAL) for the
   non-rejection, with a PROVED falsifier value.
4. The rule-4 falsifiers (a) cΛ with c = 1.1, (b) a_P with P = 3, (c) a Beurling shift, now each have a re-verifiable
   witness at an explicit window. Any proposed sign step at T ≥ 1 (for (a)) or T ≥ ½log5 + 10⁻⁴ (for (b), (c)) that
   does not distinguish Λ from these combs is refuted by a single function with ≤ 5 rational coefficients.

## Result

PROVED piece. Three falsifier certificates: λ_A(½log5 + 10⁻⁴; a_3) ≤ −0.50528, λ_A(½log5 + 10⁻⁴; 3 → 3.2) ≤ −0.23448,
λ_A(1; 1.1Λ) ≤ −0.078244, each by an explicit sine-sum witness in P_T with interval enclosure, and each extended to all
larger T by zero extension.

## What was proved

- Lemmas 1–3 (witness bound, monotone extension under zero extension for any comb, closed-form Lévy evaluation on
  Dirichlet sines with the rigorous [0, δ] bound and the closed tail ∫_{2T}^∞K = −log tanh(T/2) + π − 2arctan e^T).
- Theorems 1–3 with the witnesses and enclosures above.
- Register: REVIEW_004 §6 item 2 → NO-GO (PROVED); ROUND_002_E λ_A values for (b), (f) → PROVED upper bounds; ROUND_005_A
  falsifier c = 1.1 → PROVED at T = 1.

## What failed and why

- Nothing in the certificates failed. Not done: Θ_T < 0 for the modified combs (ROUND_002_E) — requires a covering in μ;
  the criterion is stated in §3.2 but no witnesses were computed. λ_A(T; 1.1Λ) < 0 for T < 1 not certified.
- Technical: acb.integral with explicit tolerance arguments returned non-finite balls in this setup; default parameters
  were used, and the ball x² in arb must be computed as x·x when x contains 0 (pow returns nan).

## Next concrete step

Certify Θ_T(w) < 0 for a_3 and 3 → 3.2 at T₁ with the two-witness μ-covering of §3.2 (eigenvectors of Arch − μΠ_w at
μ slightly above and below the Galerkin maximiser c*), which would make ROUND_002_E's Θ falsifiers PROVED; and certify
1.1Λ at T = 0.9 (the smallest window where ROUND_005_A uses it).
