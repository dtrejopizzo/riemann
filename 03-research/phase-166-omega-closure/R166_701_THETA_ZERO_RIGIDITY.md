# R166_701 — θ = 0: discrete Beurling systems with N = ρx + O(1)

Memo, no numerics. Labels: PROVED / PROVED-CITED / ARGUED / OPEN.
Inputs: R166_190 (requirements (G), (N)), R166_601 point 3 (N is blind to zeros), R164_201 Thm L, R164_503,
R164_401 Thm R, R163_101, 00-references/beurling-dmv (Révész 2207.00665 §refs [21],[22],[24]).

## 0. Status table

| # | Statement | Label |
|---|-----------|-------|
| T0 | Local structure: bounded multiplicities, relatively dense, ζ_𝒫 − ρs/(s−1) holomorphic and O(\|s\|) on Re s ≥ σ₀ > 0 | PROVED |
| T1 | Every θ = 0 system has Θ_𝒫 := sup Re(zeros) ≥ ½ (ψ_𝒫 − x = Ω(x^{½−ε})) | PROVED-CITED (Hilberdink 2005 Ω-results [22] + Révész Thm 8) |
| T2 | Removing finitely many primes preserves θ = 0 | PROVED |
| T3 | Adding one prime q preserves θ = 0 ⟺ R_𝒫 is a bounded coboundary for x ↦ x/q | PROVED |
| T4 | ℕ ∪ {q} (any real q > 1, incl. a second copy of a prime) is never θ = 0 | PROVED |
| T5 | Free-monoid reformulation: θ = 0 systems = free commutative monoids in (1,∞) with bounded-discrepancy counting | PROVED (tautological) |
| T6 | "All θ = 0 systems satisfy Θ = ½" ⇒ RH; converse not available | PROVED (⇒), OPEN (⇐) |
| C1 | "Every θ = 0 system is ζ·E, E finite Euler modification" | OPEN; evidence for: T2–T4; no counterexample |
| C2 | ∃ θ = 0 discrete system with a zero Re s > ½ | OPEN (neither constructed nor excluded) |
| C3 | Perturbing a single prime of ℕ (p → p(1+ε)) breaks θ = 0 | ARGUED |
| L | Hilberdink 2012 (Acta Arith. 152) "g-prime systems with periodic integer counting function": PDF not in corpus; may already contain a rigidity theorem for N − cx periodic | MUST-CHECK before any claim of novelty |

Honest headline: **no theorem at θ = 0 decides C2.** What is proved: the zeros cannot all lie left of ½ (T1),
the class is closed under prime removal and almost never under prime addition (T2–T4), with an exact
coboundary criterion. θ = 0 for discrete systems is *at least as strong as* RH only in the sense of T6.

## 1. Setting

𝒫 = (q_j) reals > 1 with integer multiplicities; 𝒩 the free commutative monoid (with multiplicity);
N(x) = #{n ∈ 𝒩 : n ≤ x}, R(x) := N(x) − ρx for x ≥ 1, N(x) = 0 for x < 1. Hypothesis (θ0): sup_{x≥1}|R(x)| = C < ∞.
ζ_𝒫(s) = ∫_{1⁻}^∞ x^{−s} dN = s∫_1^∞ N x^{−s−1}dx = ρs/(s−1) + s∫_1^∞ R(x)x^{−s−1}dx (Re s > 1, then by continuation).

## 2. T0 (PROVED)

(a) N(x+1) − N(x) = ρ + R(x+1) − R(x) ≤ ρ + 2C: each unit interval holds ≤ ρ+2C integers counted with
multiplicity. In particular every prime and every integer has multiplicity ≤ ρ + 2C.
(b) For L > 2C/ρ, N(x+L) − N(x) ≥ ρL − 2C > 0: every interval of length L meets 𝒩. Hence q₁ ≤ 1 + L.
(c) The integral ∫_1^∞ R x^{−s−1}dx converges absolutely for Re s > 0 and is ≤ C/σ. So ζ_𝒫 is meromorphic
in Re s > 0 with a single simple pole at 1, and |ζ_𝒫(σ+it)| ≤ ρ|s|/|s−1| + ρ + C|s|/σ. Convexity-type only,
as noted in the brief (ℕ itself saturates the trivial bound; nothing Lindelöf-like follows).
(d) Log-Abelian: if R has logarithmic mean m (lim (1/log X)∫_1^X R dx/x), then, since ρs/(s−1) → 0,
lim_{s→0⁺} ζ_𝒫(s) = lim s∫R x^{−s−1}dx = m. For ℕ, R = −{x}, m = −½ = ζ(0). (PROVED; standard Abelian lemma.)

## 3. T1 — zeros reach ½ (PROVED-CITED)

Hilberdink, *Ω-results for Beurling's zeta function and lower bounds for the generalised Dirichlet divisor
problem* [22 in Révész]: for any system with N = ρx + O(x^α), ψ = x + O(x^β), one has max(α,β) ≥ ½. Révész
(2207.00665, line ≈1935) records exactly this consequence. With α = 0: β ≥ ½. Translation to zeros: if
ζ_𝒫 had no zeros in Re s > ½ − δ, T0(c) + Borel–Carathéodory/Hadamard three-circles on −ζ′_𝒫/ζ_𝒫 give
|ζ′_𝒫/ζ_𝒫| ≪ |t|^ε on Re s ≥ ½ − δ/2 and Perron gives ψ_𝒫 = x + O(x^{½−δ/2+ε}), contradicting β ≥ ½.
So **Θ_𝒫 ≥ ½ for every θ = 0 system.** (The derivation zero-free ⇒ ψ-error is ARGUED-standard; the input
is PROVED-CITED.) This is the precise sense in which θ = 0 is "the rigidity end": the integers being perfect
forces the primes to be imperfect, at least at square-root scale.

## 4. T2–T4: the coboundary criterion (PROVED)

**T2 (removal).** Remove one generator q (one unit of multiplicity). The new counting is N''(x) = N(x) − N(x/q)
(ζ'' = ζ_𝒫·(1−q^{−s})), ρ'' = ρ(1−1/q), R''(x) = R(x) − R(x/q) (with R(y) := −ρy for y < 1, |·| ≤ ρ).
Bounded. Induct for finite removals. Example: integers coprime to a finite set T; ζ·∏_{p∈T}(1−p^{−s}).

**T3 (addition).** Add one generator q. N'(x) = Σ_{k≥0} N(x/q^k), ρ' = ρ/(1−1/q),
R'(x) = Σ_{0≤k≤K(x)} R(x/q^k) − ρ Σ_{q^k>x} x/q^k, K(x) = ⌊log x/log q⌋. The second sum is ≤ ρq/(q−1).
Hence θ' = 0 ⟺ F(x) := Σ_{k=0}^{K(x)} R(x/q^k) is bounded. Since F(x) = R(x) + F(x/q) exactly (x ≥ q),
**R is a bounded coboundary**: R(x) = F(x) − F(x/q) with F bounded. Consequence: the q-orbit averages
(1/n)Σ_{k<n} R(x/q^k) → 0 uniformly; in particular the log-mean m of T0(d), if it exists, is 0, i.e. ζ_𝒫(0⁺)=0.
Mellin form: ζ_{𝒫'} = ζ_𝒫/(1−q^{−s}); boundedness requires the zeros 2πik/log q of 1−q^{−s} on Re s = 0 to be
"absorbed" by R — the k = 0 instance is m = 0.

**T4.** For ℕ, R(x) = −{x} (x ≥ 1). For any real q > 1, F(x) = −Σ_{k≤K}{x/q^k}. Average over x ∈ [X, 2X]:
for q^k ≤ X/M, (1/X)∫_X^{2X}{x/q^k}dx = ½ + O(q^k/X). So the average of −F is ≥ ½(K(X) − log_q M) − O(1/M)·const
→ ∞. F unbounded ⇒ ℕ ∪ {q} not θ = 0. This covers q a new real, q an existing prime (multiplicity 2), q = 1-adjacent, all.
Consistency: ℕ = (ℕ minus 2) ∪ {2}: there R = R_odd, F bounded because N_odd(x) = ⌈x/2⌉-type and the sum telescopes to ⌊x⌋ — checks T3.

Corollary (PROVED): the θ = 0 class contains {ζ·∏_{p∈T}(1−p^{−s}) : T finite} and, among finite Euler
modifications ζ·∏_{T}(1−p^{−s})·∏_{Q}(1−q^{−s})^{−1}, membership is decided by the coboundary test; with
Q ⊄ T the generic answer is no (T4-type averaging). Removals with T infinite: OPEN (sum over 2^{#T∩[1,x]}
terms μ(d)R(x/d) need not stay bounded; no proof either way).

## 5. C3 — perturbing one prime (ARGUED)

Replace 2 by r = 2(1+ε). Then N_r(x) = Σ_{a≥0} N_odd(x/r^a), and by T3 with base system "odd integers"
(R_odd(y) = ½ − {(y+1)/2}, period 2, mean 0) θ = 0 ⟺ G(x) = Σ_{a≤log_r x} R_odd(x/r^a) bounded.
For r = 2 this telescopes (exactness of ⌊x⌋). For r ≠ 2 one expects √(log x)-size fluctuations: the
second moment over x ∈ [r^K, r^{K+1}] is K·(var R_odd) + off-diagonal, off-diagonal terms bounded by
integration by parts by ≈ (r^{−d})·(r−1)/8 per lag d. This closes the lower bound only for r > 4
(diagonal (r−1)/12 beats off-diagonal ≤ ¼); for r near 2 the off-diagonal constant is not controlled. ARGUED.
Interpretation: θ = 0 is destroyed by any non-arithmetic move of a single prime — rigidity evidence for C1.

## 6. Why C2 is not decided — the exact gap

(i) N is blind to zeros (R166_601 pt 3): Perron on ζ_𝒫 x^s/s picks up only s = 1 and Re s ≤ 0 data.
A zero ρ* of ζ_𝒫 with Re ρ* > ½ is the statement ρ/(ρ*−1) + M_R(ρ*) = 0 (after dividing by ρ*), M_R the Mellin transform of
a bounded function — one complex equation, no inequality. Nothing in (θ0) forbids it analytically:
the analytic class (bounded R, no integrality) contains such functions trivially (perturb R by a smooth bounded
bump to move a zero; ARGUED, monotonicity of N not used). So any proof of "θ = 0 ⇒ Θ = ½" must use **integrality / free-monoid structure** (T5).
(ii) T5: given a locally finite multiset 𝒩 ∋ 1 in [1,∞), generators are forced greedily (smallest
non-generated element is a prime); 𝒩 is Beurling ⟺ it is free on them. A θ = 0 construction is a greedy
process: at scale x, composites in [x, x+1) are fixed by primes < x/q₁; one may only *add* primes. Failure mode:
composite overshoot R > C cannot be repaired. This is the same obstruction as R164_503 (prime-side rounding
capped at x^{½}) and Thm L (lattice rounding cannot reach θ < ⅓): neither method approaches θ = 0, and
T3–T4 show even the mildest modifications of ℕ fail. No construction known reaches any θ < ⅓ off ℕ-modifications.
(iii) Hence C2 sits strictly beyond both available tools. A disproof of C2 (rigidity) would in particular
reprove RH? No — only if it went through "θ = 0 ⇒ Θ = ½", which for ℕ is RH (T6). A rigidity theorem of the
form C1 ("ζ_𝒫 = ζ·E, E zero-free in the strip") would NOT prove RH; it would make C2 ⟺ ¬RH.

**T6 (PROVED, trivial).** ℕ is θ = 0. So "every θ = 0 discrete system has Θ = ½" ⇒ RH. If C1 holds with E
zero-free in 0 < Re s < 1 (as in T2), then C2 ⟺ ¬RH and the θ = 0 frontier question is *equivalent* to RH.
Without C1 it is *stronger* than RH. Either way θ = 0 cannot yield RH by a method that is blind to which
system it is applied to, unless it proves RH.

## 7. Falsifier check

- ζ_θ extended class: excluded by discreteness (T0(a) uses integrality of jumps only for multiplicity bound; the
  coboundary T3 holds for continuous systems too — so T3/T4 are NOT discreteness-specific; only T5 is).
- Theorem C systems (θ > ⅓), ζ((k+1)s−k) (θ ≥ ½): not θ = 0; no conflict.
- Dedekind ζ_K, [K:ℚ] = 2: lattice-point error is Ω(x^{¼}) (Hardy–Landau type), so θ_K ≥ ¼ > 0: not θ = 0; consistent with C1.
- ℕ: R = −{x}, m = −½ = ζ(0) ≠ 0 ⇒ by T3 no prime can be added: T4. ✓

## 8. Ledger / cell 5G

- New PROVED: T0, T2, T3 (coboundary criterion), T4. New PROVED-CITED: T1 (via Hilberdink [22]).
- ARGUED: C3 (r > 4 rigorous by the second-moment bound; r ∈ (1,4] open).
- OPEN: C1, C2, infinite removal. O166.701.1: obtain Hilberdink 2012 (Acta Arith. 152, 217–241) and check whether it
  already classifies systems with N − cx periodic / bounded. O166.701.2: does T3 extend to an Ω-statement on
  ψ_𝒫 (coboundary along every prime orbit simultaneously)?
- **Cell 5G (θ = 0 rigidity): NO-GO as a route to row D.** Against (G),(N) of R166_190: the hypothesis H = (θ0)
  uses only N, which is blind to zeros (fails (N): it does not see Λ beyond any window); every statement
  derivable is either T1-type (Θ ≥ ½, wrong direction) or identification of ℕ-modifications (T6). No sign-carrying content.
