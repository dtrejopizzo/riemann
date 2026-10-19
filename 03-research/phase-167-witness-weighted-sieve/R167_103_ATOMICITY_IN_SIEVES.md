# R167_103 — Where atomicity and integrality enter the sieve bounds: test of (WS) tools against M_m, f_t and Beurling systems

*Task A3 of R167_000 §5. Pure mathematics, no numerics. Inputs: R167_000 (problem (WS)),
R163_801 Thm 5 (M_m), R163_901 Thm F (f_t), R166_802 Thm 1–4, R166_501 Thm A, R164_201 (class 𝒦_θ, Thm L), R163_101 §1 item 5
(Hilberdink via Révész), 00-references/beurling-dmv (DMV/Zhang, secondary sources only). No label of record moves.
(WS), (★_cell), Gate 1, row D: **OPEN**.*

## 0. Status table

| # | Statement | Label |
|---|---|---|
| 1 | Per-bound structural input (table §2): (a) Selberg and (c) B–T use Λ ≥ 0 + Euler product + the remainder bound \|r_d\| ≤ 1 for counting multiples in intervals (θ = 0 regularity of ℕ); (b) in Dirichlet-polynomial form and (e) use only frequency separation; (d) uses Λ = μ*log in the semigroup algebra, and its type I/II estimates use Poisson summation on ℤ | PROVED (reading of the standard proofs; PROVED-CITED for the theorems themselves) |
| 2 | M_m test: every Λ-sum bound of type (a)–(e) is true **verbatim** for M_m's atomic part (it is ζ's). Atomicity enters not in the sieve but in the identification "Tail = Σ_n Λ(n)…", i.e. in the hypothesis "P is purely atomic beyond the polar/arch part". The continuous part β_m contributes ≍ X^{δ}·\|ŵ(γ−γ_j)\| to the full prime-side sum, which violates η < δ at γ = γ_j | PROVED |
| 3 | f_t test: (a), (c), (d) **do not apply** to f_t (b_t has both signs, no Euler product, no counting function); (b), (e) apply with a separation loss: at the contact level the frequency set near X is ℕ ∪ {m/√M}, log-separation ≥ 1/(2M X²) (M non-square), and globally ≥ X^{−A(M)} | PROVED |
| 4 | Theorem S (class transfer): Selberg upper bound, B–T for y ≥ x^{θ+ε}, Vaughan identity, Dirichlet-polynomial large sieve and MV mean value hold for every discrete Beurling system in 𝒦_θ^+(A, C_N), with constants depending only on (A, θ, C_N) | PROVED (sieve: §4.1; the rest PROVED-CITED, the extension to Beurling is routine and written out) |
| 5 | Corollary: a (WS)-type inequality proved only from tools (a)–(e) holds on 𝒦_θ^+(A, θ, C_N) with the same proof. For θ ≥ ½ + o(1) the class contains RH-false systems (DMV 2006, Zhang 2007), so such a proof with **uniform-in-X** exponent η < ½ is impossible for θ ≥ ½ inputs | PROVED given DMV/Zhang (CITED secondary) + R166_802 Thm 3 transferred (Landau's theorem holds for Beurling ζ: PROVED-CITED) |
| 6 | The brief's expectation "sieve classes contain f_t and M_m" is **false as stated**: sieve classes exclude f_t (signs, no Euler product) and see only M_m's atomic part. The correct falsifier for sieve classes is the DMV/Zhang family, not f_t or M_m | PROVED (corrects R167_000 §3 bullets 4–5) |
| 7 | "Sign-blind for row D" for 𝒦_θ^+: DMV/Zhang systems have no Γ_ℝ functional equation, so they are **not** systems in the sense of R166_501 Def 1, and they have no window form W_T in the record's sense. The transfer to row D is ARGUED only (needs a Beurling Weil form; Thm A of R166_501 does not apply verbatim) | ARGUED |
| 8 | No known system lies in 𝒦_θ^+ ∩ Def 1 (Euler product, Λ ≥ 0, Γ_ℝ FE, pole at 1) with RH false. Such a system would be a degree-1 "Beurling–Selberg" function; for ℕ-support Kaczorowski–Perelli give only ζ and twists. For non-integer frequencies the classification is unknown to me | OPEN (flagged) |
| 9 | Theorems true for ζ, provable without zeros, false for some discrete Beurling system with Euler product and PNT: yes, e.g. ψ(x+1) − ψ(x) ≤ log(x+1), Brun–Titchmarsh with the constant 2 for all y ≥ 2, Chebyshev bounds with explicit constants, Mertens' constant | PROVED (§5, explicit construction) |
| 10 | All examples in 9 are consequences of one property: N_ℕ(x) = ⌊x⌋, i.e. 𝒦_0^+(1, 1) regularity. Whether 𝒦_0^+ (or 𝒦_θ^+ with θ < ½) contains an RH-false system is Paper 48 Problem 6 at θ → 0 | OPEN (Problem 6; R164_201 row 7, 9) |
| 11 | Additive structure (residue classes, Bombieri–Vinogradov, B–T in APs, van der Corput on n^{it}): "integer multiset of the system = ℕ" forces the prime multiset = rational primes, so ζ_𝒫 = ζ exactly | PROVED (unique factorisation; trivial) |
| 12 | "Any additive structure compatible with Γ_ℝ degree 1 = ℕ" (so additive structure = integrality = identification) | ARGUED (ring-of-integers structures give Dedekind ζ of degree [K:ℚ]; general "residue-class structures" not classified) |
| 13 | Range remark: in (WS) the scale X lies in a **compact** range [e^{1.61}, e^{2T_max}] and γ > 3·10¹², so S is a finite sum over few n; asymptotic class arguments (row 5) only forbid uniform-in-X proofs. A finite-range (WS) with explicit C is a numerical statement on finitely many terms and is not refuted by any class argument | PROVED (logic) |
| (WS), (★_cell), row D | | **OPEN** |

**Verdict.** Atomicity of the prime side is not where any sieve acts: for M_m the sieve bounds are literally true (same atoms) and M_m is
excluded only by the separate hypothesis "P has no continuous part". f_t is excluded from the sieve tools already by Λ ≥ 0 and the
Euler product, so f_t is not the relevant falsifier for sieves. The relevant one is the Beurling family DMV/Zhang. Every sieve and
large-sieve proof transfers to 𝒦_θ^+, and the only quantity in which ℕ is special is θ = 0, C_N = 1. Whether that regularity carries
any zero information is exactly Paper 48 Problem 6 at small θ. It is OPEN, and the only integrality theorem known (Hilberdink 2005)
constrains exponents of error terms and not zeros. Additive structure gives nothing beyond this: it is integrality, hence
identification.

## 1. Setting and classes

- S(X,Δ;γ,w) = Σ_{X≤n≤Xe^{2Δ}} Λ(n) n^{−1/2+iγ} w(log n) (R167_000 §2).
- For a system with prime-side measure P (atomic part Σ_λ b(λ) λ^{−1/2} δ_{log λ}, plus maybe a density), put
  S_P := ∫_{[log X, log X+2Δ]} e^{iγu} w(u) dP(u). For ζ, S_P = S.
- **𝒦_θ^+(A, C_N)** (discrete Beurling, positive): a multiset 𝒫 of reals 1 < p_1 ≤ p_2 ≤ …, the multiplicative semigroup 𝒩 it
  generates (with multiplicity), Λ_𝒫(p^k) = log p and 0 otherwise, N(x) := #{ν ∈ 𝒩 : ν ≤ x} = Ax + E(x), |E(x)| ≤ C_N x^θ for x ≥ 1.
  ℕ ∈ 𝒦_0^+(1, 1). This is R164_201's 𝒦_θ without the Witt-lattice construction.

## 2. Per-bound analysis

| Tool | Exact input from ℤ | (i) Λ + β_m (M_m) | (ii) f_t | (iii) general Beurling (positive) |
|---|---|---|---|---|
| (a) Selberg upper sieve | Λ ≥ 0 only through "primes are a subset of the sifted set"; counting #{n ∈ I : d \| n} = \|I\|/d + r_d with \|r_d\| ≤ 1 (θ = 0); λ_d supported on d ≤ D, quadratic form minimisation (no arithmetic) | atomic part = ζ's: bound true verbatim. β_m: nothing to sieve; it is not part of the sifted sum | not applicable: b_t takes both signs, so no upper bound on b_t follows from an upper bound on a sifted count; 𝒩 is not free (no Euler product) | holds with r_d replaced by E: \|r_d\| ≤ 2C_N (x/d)^θ (§4.1) |
| (b) large sieve, Dirichlet-polynomial form | separation of the frequencies log n (log-gap ≥ 1/(2x) at height x). The additive-character and Farey forms use ℤ's additive group (e(nα)) | holds for the atoms; for the density, Plancherel replaces it (no loss) | holds with separation from §3: loss factor ≍ M X at the contact level | holds with the separation of log 𝒩, which is a free parameter of the system (no lower bound from the axioms; multiplicities allowed) |
| (c) Brun–Titchmarsh | (a) + interval structure: y ≥ 2 suffices because θ = 0 | true verbatim for the atoms | not applicable (signs) | holds only for y ≥ x^{θ+ε} (§4.1); for y ≤ x^θ it fails (§5) |
| (d) Vaughan / Heath-Brown | Λ = μ * log as formal identity in the Dirichlet algebra of 𝒩, \|μ\| ≤ 1, d_k bounds. Type I/II estimates of Σ n^{−1/2+iγ}: Euler–Maclaurin / Poisson on ℤ (van der Corput); type II: (b)/(e) | atomic part = ζ's, true; β_m not of convolution form | identity exists formally (−f_t′/f_t = (−f_t′)·(1/f_t)), but coefficients of 1/f_t are not bounded by 1 and the "integers" sum Σ a_t(λ)λ^{−s} has no smooth main term: type I estimates are absent | identity holds; type I sums carry the error E, so the saving is capped by x^θ |
| (e) MV mean value Σ\|a_λ\|²(T + 3π/δ_λ) | only real frequencies with δ_λ = min gap; arbitrary complex a_λ | holds | holds (§3) | holds |

Explanation of the rows (PROVED by reading the proofs).
- (a) Selberg's bound for Σ_{n∈I}(Σ_{d|n} λ_d)² is a quadratic form in λ whose coefficients are #{n ∈ I : [d_1,d_2] | n} = |I|/[d_1,d_2] + r.
  The only arithmetic fact is the size of r. Primes enter as "1_{p} ≤ (Σ_{d|n}λ_d)², λ_1 = 1", which needs the weight on primes to be
  ≤ 1 — a positivity (Λ ≥ 0) fact.
- (b), (e) Montgomery–Vaughan's generalized Hilbert inequality (PROVED-CITED, MV 1974) holds for any real λ_r with gaps δ_r and any
  coefficients. No multiplicative or additive structure enters. The Farey large sieve needs e(nα) on ℤ, but (WS) is multiplicative,
  so only the Dirichlet-polynomial form is relevant.
- (d) Vaughan's identity is an identity among formal Dirichlet series of a free semigroup. The arithmetic is in the type I/II
  estimates. Type I: Σ_{m∈I} m^{−1/2+iγ} needs a main term ∫ plus an error, i.e. Euler–Maclaurin on ℤ (θ = 0) or exponent pairs
  (Poisson on ℤ). Type II: (b)/(e).

**Effect on (WS) (R166_802 Thm 4 refined).** With n^{−1/2} normalisation every tool above gives |S| ≤ C X^{1/2}·(log)·‖w‖. The
exponent ½ is the trivial size. (a), (c) give it with the B–T constant 2. (b), (e) give it as ‖a‖₂·√(length). None gives η < ½.

## 3. Separation of f_t's frequencies

**Prop 3.1. PROVED.** Let M ≥ 2 be a non-square, so √M is irrational, and let the new generators be λ_m = m/√M, m > R (R163_901 Thm F).
(a) Below λ_1², the frequencies are ℕ, the single atoms λ_m, and products nλ_m ≥ 2λ_1 (R163_901 item 4). For n, m ≥ 1,
|m/√M − n| = |m² − n²M| / (√M(m + n√M)) ≥ 1/(√M(m + n√M)). Here m² − n²M is a non-zero integer. With λ_m ≈ n ≈ x this is
≥ 1/(2M x)·(1 + o(1)). Two atoms differ by ≥ 1/√M. So the log-gap at height x is ≥ 1/(2M x²)(1 + o(1)), against 1/(x + 1) for ℕ.
(b) In general λ_mλ_{m′} = mm′/M ∈ M^{−1}ℤ, and every frequency lies in ⋃_k M^{−k}ℤ ∪ M^{−k}ℤ/√M with k ≤ log x/log 2 (all
generators ≥ 2). Same-type frequencies are spaced ≥ M^{−k} ≥ x^{−log M/log 2}. A mixed pair a/M^k vs b/(M^k√M) is spaced
≥ 1/(M^{2k}·2x√M) by the computation in (a). So the log-gap is ≥ x^{−A(M)}, A(M) = 1 + 2log M/log 2 + o(1).
The set is discrete (finitely many elements ≤ x), countable, and its gaps are polynomially small. It is not dense. ∎

So (b), (e) hold for f_t with the loss 3π/δ_λ ≤ x^{A(M)}. At the contact level (X < 2λ_1) the loss is ≍ M X², and only on the
O(1) atoms λ_m near integers. These tools therefore do not separate f_t from ζ: they are blind to coefficients, and f_t's only
distinguishing feature at contact level is the coefficient t·c(m_1)log λ_1 of one atom.

## 4. Theorem S (class transfer)

**Theorem S.** Let 𝒫 ∈ 𝒦_θ^+(A, C_N), 0 ≤ θ < 1. Then:
(S1) (Selberg) for an interval I = (x, x+y] and D ≥ 1, Σ_{ν∈𝒩∩I, ν has no prime of 𝒫 below D} 1 ≤ Ay/L_𝒫(D) + 2C_N Σ_{d_1,d_2≤D} |λ_{d_1}λ_{d_2}| (x+y)^θ,
with L_𝒫(D) = Σ_{d∈𝒩 squarefree, d≤D} ∏_{p|d}(1/(Ap(1 − 1/p)))-type sum (the density function g(p) = 1/p).
(S2) (B–T) for y ≥ x^{θ+ε}: π_𝒫(x+y) − π_𝒫(x) ≤ (2 + o(1)) A y/log(y x^{−θ}).
(S3) (Vaughan) −ζ_𝒫′/ζ_𝒫 = formal identity with μ_𝒫, |μ_𝒫| ≤ 1 on 𝒩; type I sums Σ_{ν∈𝒩∩I} ν^{−1/2+iγ} = A∫_I u^{−1/2+iγ}du + O(C_N(1+|γ|)x^{θ−1/2}·y/x + C_N x^{θ−1/2}).
(S4) (MV / large sieve) Σ_r|Σ_ν a_ν ν^{it_r}|² ≤ Σ(T + 3π/δ_ν)|a_ν|², δ_ν the log-gap in 𝒩 (no axiom bounds it below).
*Proof.* (S1) is Selberg's argument verbatim. #{ν ∈ 𝒩∩I : d | ν} = N((x+y)/d) − N(x/d) = Ay/d + r_d, because "d | ν in 𝒩" means ν = dν′
with ν′ ∈ 𝒩 (free semigroup, counted with multiplicity), and |r_d| ≤ 2C_N((x+y)/d)^θ. The quadratic form minimisation is the same.
(S2): with Σ|λ_d| ≤ D and D² x^θ ≤ y x^{−ε}, take D = (y x^{−θ−ε})^{1/2}. Then L_𝒫(D) ≥ (1/A)(log D)(1 + o(1)) by the Beurling Mertens
theorem, which follows from N(x) = Ax + O(x^θ) with θ < 1 (Beurling/Diamond–Zhang, PROVED-CITED). (S3): partial summation against
dN = A du + dE. (S4): MV 1974 applies to any real frequencies. ∎

**Corollary S′. PROVED** (given the citations in row 5). Let 𝒯 be a proof of an inequality ℐ(Λ) that uses only (S1)–(S4), Λ ≥ 0,
Λ(p^k) = log p, the Euler product and PNT with dlVP error. Then ℐ(Λ_𝒫) holds for every 𝒫 ∈ 𝒦_θ^+(A, C_N) with constants
C(A, θ, C_N), where θ ≥ (the θ actually used). For θ ≥ ½ + o(1) the DMV/Zhang systems (N error x^{½+o(1)}, R164_x records;
secondary source BDV 2004.11501 §1) lie in the class and have zeros at σ = 1 − c/log|t|. By Landau's theorem for Beurling ζ
(non-negative coefficients; PROVED-CITED) and R166_802 Thm 3 (whose proof uses only the Dirichlet series and the twist), the
twisted sums of such a system have exponent Θ − ½ > η for every η < ½. So **no 𝒯 with θ ≥ ½ proves a uniform-in-X (WS) with η < ½.** ∎

**Remark S″ (why this is not a row-D theorem). ARGUED.** R166_501 Thm A concerns systems with Γ_ℝ archimedean part and (1.1).
DMV/Zhang have no functional equation, so "W_T", "contact" and "witness" are undefined for them without a Beurling Weil form, which
the record has not set up. The transfer "class-level ⟹ sign-blind for row D" therefore goes through the twisted-sum exponent
(R166_802 Thm 3), not through Thm A. That suffices for the uniform version of (WS), which is the only version an asymptotic class
member can refute (row 13).

## 5. Theorems true for ζ, zero-free, false for a Beurling system with Euler product and PNT

**Prop 5.1. PROVED.** Let 𝒫′ be the rational primes with K extra copies of one prime p_0 (or K new primes in (x_0, x_0+1)). Then
𝒫′ is a discrete Beurling system with Euler product ζ·(1 − p_0^{−s})^{−K}, Λ ≥ 0, Λ(q^k) = log q, and PNT with the same error as ζ
(finitely many primes added). For K > 1 + log(x_0 + 1)/log x_0 it violates ψ(x+1) − ψ(x) ≤ log(x+1). For K ≥ 3 it violates
π(x_0+2) − π(x_0) ≤ 2·2/log 2 + … and B–T with constant 2 at y = 2. By choosing K large one also shifts Mertens' constant
Σ_{p≤x}1/p − log log x → M + K/p_0. ∎

These four are true for ζ and proved without zeros. **Each is a consequence of the single fact N_ℕ(x) = ⌊x⌋** (θ = 0, C_N = 1, and
integer spacing ≥ 1). For 𝒫′, the factor (1 − p_0^{−s})^{−K} is analytic in σ > 0, so N_{𝒫′}(x) = A′x + O_{ε,K}(x^ε).
θ is still 0+, but the constant C_N is huge. This shows the separating parameter is C_N (and the
spacing), not θ alone. The question that matters for the sign:

**Problem P6₀ (= Paper 48 Problem 6 at θ → 0). OPEN.** Does 𝒦_0^+(A, C_N), or 𝒦_θ^+ with θ < ½, contain a system whose ζ_𝒫 has a zero
with real part > ½? The record's state: Theorem L (R164_201) shows the Witt-lattice constructions cannot reach θ < 1/3 with the
needed rounding; Hilberdink 2005 (via Révész 2207.00665, CITED secondary) says the two largest of the exponents of the errors in
N, ψ, M must both be ≥ ½ and equal. With θ < ½ this forces Θ_ψ ≥ ½ and Θ_ψ = Θ_M. That is consistent with RH and with ¬RH alike.
**No zero-free consequence of small θ is known.** If P6₀ has answer "no RH-false member", then integer regularity is a genuine
non-class H, and the statement "θ small ⟹ RH" would be a Beurling RH theorem. If the answer is "yes", every sieve tool is
sign-blind.

## 6. Additive structure

**Prop 6.1. PROVED.** If the integer multiset 𝒩 of a discrete Beurling system equals ℕ with multiplicity one, then 𝒫 = the rational
primes and ζ_𝒫 = ζ. *Proof.* The irreducibles of the free commutative monoid (ℕ, ·) are the primes. A free monoid determines its basis,
with multiplicities. ∎

So every theorem that uses residue classes mod q of the integers (Dirichlet characters, Bombieri–Vinogradov, B–T in APs, the Farey
large sieve, van der Corput/Poisson for Σ n^{it}) assumes 𝒩 = ℕ, and by Prop 6.1 it is a theorem about ζ alone. As a hypothesis H it
is identification. It is not a class property, it cannot be falsified within a class, and a proof of (WS) that uses it is a proof
about ζ. That is allowed, but it has to produce a sign, and R166_802 Thm 1–3 says the needed strength is δ, beyond every current
zero-free tool. Bombieri–Vinogradov has level ½ in the modulus. Its proof is the multiplicative large sieve plus Vaughan, and its
exponent in x is the GRH-on-average exponent ½. In our normalisation that is again η = ½.
**Claim 6.2. ARGUED.** Any additive structure that makes 𝒩 an ℤ-module or a residue-class system compatible with a degree-1 Γ_ℝ
functional equation forces 𝒩 = ℕ. Number-field structures give Dedekind ζ_K with Γ-factor of degree [K:ℚ]. A general classification
of "residue-class structures" on Beurling semigroups is not available. Hence "additive structure = integrality = identification"
is PROVED for 𝒩 = ℕ and ARGUED beyond it.

## 7. Answer to the A3 questions

1. **Where atomicity enters.** Not in any sieve. It enters in the step "the tail of (1.1) equals Σ_n Λ(n)n^{−1/2}Ψ̌(log n)", i.e. in
   the hypothesis that P has no continuous part. For M_m the extra term is ∫ w(u)e^{iγu}β_m(u)du. At γ = γ_j it is
   2∫w(u)e^{δ_j u}(1 + O(e^{−2δ_j u}) + oscillating)du ≍ X^{δ_j}‖w‖₁. So the full-prime-side (WS) fails for M_m exactly as the test
   requires. The atomic-part (WS) is identical for ζ and M_m. (PROVED.)
2. **Where integrality enters.** In (a), (c), (d) through C_N = 1, θ = 0 (remainder |r_d| ≤ 1, Euler–Maclaurin on ℤ). In (b), (e)
   through the gap 1/x of log ℕ. f_t is excluded from (a), (c), (d) by the sign of b_t and by the missing Euler product, before
   integrality is used. (PROVED.)
3. **Theorem S + Cor S′.** Sieve and large-sieve inequalities are class theorems on 𝒦_θ^+. For θ ≥ ½ the class contains RH-false
   members, so uniform (WS) with η < ½ cannot come from them. (PROVED, with DMV/Zhang CITED secondary.) The row-D form of
   "sign-blind" is ARGUED (Rem S″).
4. **Non-class property.** The candidates are the exact regularity of ℕ (C_N = 1, θ = 0, spacing 1) and the additive structure.
   The second is identification (Prop 6.1). Whether the first is sign-relevant is Problem P6₀, which is OPEN. That is the precise
   residual for any sieve route to (WS).
5. **Correction to R167_000 §3.** The two "mandatory tests" are not failure points of sieve proofs. M_m passes every atomic bound,
   and f_t is outside the sieve's hypotheses. The meaningful falsifier for an (a)–(e) proof of (WS) is 𝒦_θ^+ with θ ≥ ½ (DMV/Zhang).
   For finite-range (WS) (row 13) no class falsifier is known.

## 8. Ledger

- New: Theorem S written for 𝒦_θ^+ (routine). Prop 3.1 (f_t's frequency gaps: ≥ 1/(2MX²) at contact level, polynomial globally).
  Prop 5.1 (zero-free ζ-theorems false for Euler-product PNT Beurling systems). Prop 6.1. The reduction of every sieve route to (WS)
  to Problem P6₀ plus the uniform/finite-range distinction.
- Corrections: R167_000 §3 bullets 4–5 (atomicity/integrality are not the steps where sieves act; see §7.5). The brief's
  "Diamond–Halberstam–Galway treats Beurling": not verified. Theorem S does not need it (Selberg's sieve is written out in §4).
  Flagged: do not cite DHG for Beurling.
- Citations, all flagged: Montgomery–Vaughan 1974 (Hilbert inequality), Montgomery–Vaughan 1973 (B–T), DMV 2006 / Zhang 2007
  (secondary only), Hilberdink 2005 (via Révész, secondary), Kaczorowski–Perelli degree-1 classification (memory), Landau's
  theorem for non-negative Dirichlet integrals.
- Labels of record: none move. (WS), (★_cell), Gate 1, row D: **OPEN**.
