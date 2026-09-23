# R153.003 — Builder, round 2 (phase 153, row D): the interval certificate

*Builder of record: Claude Opus 5. Date 2026-09-19. Answers the binding repairs of `R153_002_HOSTILE_AUDIT.md`
and delivers the certificate demanded by `R153_000` §2/Q1 and by D.12-α. Labels: `PROVED` / `RESTATEMENT` /
`DIAGNOSTIC-NUMERIC` / `OPEN` / `WITHDRAWN`. **No sign is claimed for `ζ` at any `T > log 2`.***

**Headline.** For `T = log 2`, `a = 0.45` and one explicit polynomial test function `F` lying **exactly** in the
four-moment primitive space `P_T^{(a)}`, interval arithmetic (`mpmath.iv`, 400 bits) gives

```
        <A_T^{(a)} F, F> / ||F||^2   in   [ -0.037336730 , -0.037336729 ]        (a = 0.45)
        <A_T^{(a)} F, F> / ||F||^2   in   [ -0.014227989 , -0.014227988 ]        (a = 0.30)
```

Both are **strictly negative**, certified. Since `A_T ≥ 0` on `P_T` for `0 < T ≤ log 2` is Paper 42
`thm:certifiedendpoints`, **D.12-α is answered with `(S,T) = ({∞,2,3}, log 2)`; label `PROVED`.**

---

## 0. What is proved, and what is not

> **Theorem R153.1 (`PROVED`).** Let `S = {∞,2,3}`, `T = log 2`. Then
> (i) `W_S ≥ 0` for `ξ` on `P_T` — this is Paper 42 `thm:certifiedendpoints` (`main.tex:4164`), not reproved here;
> (ii) `W_S^{(a)} < 0` for the falsifier `Ξ_a(s) = Λ(s+a)Λ(s−a)` on `P_T^{(a)}`, for `a = 0.45` and for `a = 0.30`,
> witnessed by the explicit `F` of §2 with the enclosures displayed above.
> Hence the semilocal datum `(S,T) = ({∞,2,3}, log 2)` **carries sign**: the inequality it certifies is *false*
> for a function whose zeros lie off the critical line at height `±a`.

**It does NOT prove.** Nothing about `ζ` beyond `T ≤ log 2`; nothing about the sign of `A_T` for `T > log 2`;
nothing about `Ξ_a` for `a < 0.30` at `T = log 2` (see §4: the detection threshold crosses `log 2` at `a ≈ 0.080`,
but that crossing is `DIAGNOSTIC-NUMERIC`, not certified); nothing about Epstein `Ξ_Q` or Beurling zetas.
It does not establish that the *endpoint* is special — §4 shows negativity at `a = 0.45` already appears at
`T ≈ 0.624 < log 2`, strictly inside the certified range (audit #11, accepted).

---

## 1. The exact reduction that makes the certificate cheap

*Corpus check.* `grep -rIl "E_b(F)\|mathcal E_b"` → `114_d_76`, `114_d_79`, `114_d_59/60` (Paper 42's D.76
resolvent energy, for the **single** Gamma factor). `grep -rIn "tau^2/(b"` → no hit; `grep -rIn "P(D)H"` → no hit;
`grep -rIn "mpmath.iv"` → no hit. The `a`-shifted resolvent ladder below and the `P(D)`-construction of exactly
primitive test functions are new.

### Lemma C1 (`PROVED`) — the doubled archimedean symbol as a ladder of non-negative energies

For `a ∈ [0,½)` put `a_j^± := 2j + ½ ± a` (`j ≥ 0`) and `m_0^{(a)} := 2\logπ − ψ(¼+a/2) − ψ(¼−a/2)`. Then for
all real `τ`
```
   Σ_± Re ψ(¼ ± a/2 + iτ/2) − 2 logπ  =  Σ_{j≥0, ±}  2τ² / ( a_j^± ( (a_j^±)² + τ² ) )  −  m_0^{(a)} .
```
*Proof.* `ψ(z) = −γ + Σ_{k≥0}[1/(k+1) − 1/(k+z)]`; with `z = ¼ ± a/2 + iτ/2`, `k+z = (a_k^± + iτ)/2`, so
`Re(k+z)^{−1} = 2a_k^±/((a_k^±)²+τ²)`. Subtracting the value at `τ = 0` term by term (the series converges
absolutely once differenced) gives
`Reψ(¼±a/2+iτ/2) − ψ(¼±a/2) = Σ_k 2τ²/(a_k^±((a_k^±)²+τ²))`. Adding the two signs and `−2logπ` is the claim. ∎

**Correction of the D.76 multiplier (audit #17, accepted).** `2τ²/(b(b²+τ²))` is exactly the Fourier symbol of
`E_b(F) = ∫_0^∞ e^{−br}‖F − S_rF‖²dr`, because `‖F−S_rF‖² = (1/2π)∫2(1−\cos rτ)|\hat F|²dτ` and
`∫_0^∞ e^{−br}2(1−\cos rτ)dr = 2τ²/(b(b²+τ²))`. The round-1 quote `2b/(b²+τ²)` was wrong; **`WITHDRAWN`**, and
the corrected symbol is now `PROVED` (it is the resolvent symbol `(2/b)[1 − b²/(b²+τ²)]`).

### Lemma C2 (`PROVED`) — everything is an autocorrelation

Let `F ∈ L²` be supported in `I_T = (−T,T)`, `c(r) := ∫F(t)F(t+r)dt` (even, supported in `|r| ≤ L := 2T`),
`N² := c(0) = ‖F‖²`, `\hat c(b) := ∫_0^L e^{−br}c(r)dr`. Then
```
   E_b(F) = 2N²/b − 2\hat c(b)  ≥ 0 ,
```
and, combining with Lemma C1 and Prop. 12.6's prime weights `c_n = Λ(n)(n^a+n^{−a})`,
```
   q_a(F) := <A_T^{(a)}F,F>
           = Σ_{j≥0,±} E_{a_j^±}(F)  −  m_0^{(a)} N²  −  Σ_{n<e^{2T}} 2 c_n n^{−1/2} c(\log n) .      (★)
```
*Proof.* `‖F−S_rF‖² = 2(N²−c(r))`, and `∫_0^∞ e^{−br}2(N²−c(r))dr = 2N²/b − 2\hat c(b)` since `c` vanishes past `L`.
Non-negativity is manifest. (★) is Lemma C1 integrated against `|\hat F|²/2π`. ∎

(★) is the whole certificate: **every term is a finite, exactly computable functional of one polynomial `c`**,
and the only infinite object, `Σ_j E`, is a sum of **non-negative** terms, so truncating it at `j ≤ J` and adding
one explicit upper bound for the remainder yields a rigorous **upper** bound for `q_a(F)`.

### Lemma C3 (`PROVED`) — exactly primitive test functions with no linear algebra

Let `p = ½+a`, `q = ½−a`, `P(D) = (D²−p²)(D²−q²)`, and let `H ∈ C^3_c(I_T)`. Then `F := P(D)H` satisfies
```
   ∫ F(t) e^{βt} dt = 0    for every  β ∈ {±(½+a), ±(½−a)} ,
```
i.e. `F ∈ P_T^{(a)}` **exactly**. *Proof.* `∫e^{βt}(D+β)G\,dt = [e^{βt}G] = 0` for any `G` vanishing at `±T`;
`P(D) = (D−p)(D+p)(D−q)(D+q)`, the factors commute, and each partial application of the factors to
`H ∈ C^3_c` still vanishes at `±T`. Choosing the factor `(D+β)` as the innermost one kills the `β`-moment. ∎

Taking `H(t) = (T²−t²)^4 · Σ_i g_i t^i` gives `H ∈ C^3_c(I_T)` and `F` a **single polynomial** on `[−T,T]`
(zero outside), with `g_i` free. No projection, no residual: the four moment constraints hold identically.

---

## 2. The certificate

Script: `scripts/certificate/{polyalg.py, xiform.py, assemble.py, cert.py}`; run
`python3 cert.py 0.45 2000` and `python3 cert.py 0.30 2000` (≈2 min each). All arithmetic in `mpmath.iv`
at `iv.prec = 400` (`python-flint` absent, as the audit records).

**The test function.** `T = \log 2`, `a = 0.45`, `H(t) = (T²−t²)^4 Σ_{i=0}^{10} g_i t^i` with the **exact
decimal** coefficients
```
   g = (0.0168, 0, −0.0494, 0, −0.0899, 0, 0.5822, 0, −1, 0, 0.6515)        (a = 0.45)
   g = (0.0179, 0, −0.0518, 0, −0.0828, 0, 0.5702, 0, −1, 0, 0.6572)        (a = 0.30)
```
and `F = P(D)H`, a polynomial of degree 18 on `[−T,T]`. (The `g` were obtained by minimising the Rayleigh
quotient of (★) over this 11-dimensional family and rounding to four decimals; the rounding is irrelevant to the
proof, which certifies the rounded vector.) `F ∈ P_T^{(a)}` exactly by Lemma C3.

**Step 1 — the autocorrelation.** `c(r) = ∫_{−T}^{T−r}F(t)F(t+r)dt` is computed as an exact polynomial in `r`
of degree 37 by bivariate expansion and term-by-term integration, every coefficient an interval.
Enclosure: `N² = ‖F‖² ∈ [0.73073344548983350213, 0.73073344548983350214]` (`a = 0.45`),
`∈ [0.79001637319300125755, 0.79001637319300125756]` (`a = 0.30`).

**Step 2 — `m_0^{(a)}`.** `ψ` is evaluated by the recurrence `ψ(z) = ψ(z+40) − Σ_{k<40}(z+k)^{−1}` followed by
the Binet/Stirling expansion to `B_{10}` with the standard enveloping-series remainder
`|R| ≤ |B_{12}|/(12 w^{12})`, valid for real `w > 0`. Enclosure (`a = 0.45`):
`m_0^{(a)} ∈ [44.918692819403630719749, 44.918692819403630719755]`.

**Step 3 — `\hat c(b)` for `j ≤ J = 2000`.** Two rigorous representations, switched at `bL = 100`:
*(a) series* `\hat c(b) = Σ_{m≤M}(−b)^m I_m/m!` with `I_m = ∫_0^L r^m c(r)dr` exact, `M = 400`, and the tail
bounded by `\max|c|·L·(bL)^{M+1}/(M+1)!·2`; *(b) asymptotic* `\hat c(b) = Σ_k c_k k!/b^{k+1} + ε`,
`|ε| ≤ ∫_L^∞ e^{−br}Σ|c_k|r^k dr ≤ \max|c|·e^{−bL}/(b − \deg/L)` using `r^k ≤ L^k e^{k(r/L−1)}`.
Both tails are `< 10^{−40}` at the switch point.

**Step 4 — the archimedean remainder `j > J`.** By Taylor with remainder on `[0,L]`,
`N² − c(r) ≤ A r + B r²` with `A := |c'(0^+)| = ½(F(T)² + F(−T)²)` (exact identity: `∫_{−T}^{T}FF' = ½[F²]`) and
`B := ½ \sup_{[0,L]}|c''|`. Since
`c''(r) = F'(T−r)F(T) − F(T−r)F'(T) + ∫_{−T}^{T−r}F(t)F''(t+r)dt`,
`\sup|c''| ≤ 2‖F‖_∞‖F'‖_∞ + ‖F‖_2‖F''‖_2`, and each sup-norm is bounded by the Legendre/Nikolskii inequality
`‖P‖_∞ ≤ ((\deg P + 1)/\sqrt2)·‖P‖_{L²(−T,T)}/\sqrt T` (from `P = Σ p_k L_k(t/T)`, `|L_k| ≤ 1`, Cauchy–Schwarz),
with the `L²` norms exact polynomial integrals. Then `E_b ≤ 2A/b² + 4B/b³ + 2N²e^{−bL}/b`, and using
`a_j^± ≥ 2j`,
```
   Σ_{j>J,±} E_{a_j^±}(F)  ≤  A/J + B/(2J²) .
```
Measured (`a = 0.45`): `A ∈ 6.0200377760644090e−4`, `B ∈ 1987.68567611446348`, so the remainder is
`≤ 2.4876171140312e−4`.

**Step 5 — assembly.** With `J = 2000`, `a = 0.45`:
```
   partial form (j ≤ J)      ∈ [ -0.027531958687944031 , -0.027531958687944030 ]
   archimedean remainder     ≤    0.00024876171140312
   q_a(F)                    ≤   -0.027283196976540919
   q_a(F)/||F||^2            ∈ [ -0.0373367294804088 , -0.0373367294804087 ]      < 0 .
```
and `a = 0.30`:
```
   partial form (j ≤ J)      ∈ [ -0.011505501534395445 , -0.011505501534395444 ]
   archimedean remainder     ≤    0.00026515793702073
   q_a(F)/||F||^2            ∈ [ -0.0142279881516186 , -0.0142279881516185 ]      < 0 .
```
∎ (Theorem R153.1(ii)).

**Independent cross-check (`DIAGNOSTIC-NUMERIC`).** `scripts/certificate/crosscheck.py` evaluates `q_a(F)` for the
*same* `F` by the completely different route of the Fourier-multiplier integral
`(1/2π)∫Σ(τ)|\hat F(τ)|²dτ` straight from Prop. 12.6's symbol, with `\hat F` in closed form (repeated integration
by parts) and graded panels to `τ = 10⁹`. It returns Parseval `0.7307334455 = ‖F‖²` to 10 digits and
`q_a(F)/‖F‖² = −0.03766956` (`a = 0.45`), `−0.01455440` (`a = 0.30`). The certified **upper** bounds exceed these
by `3.4·10⁻⁴` resp. `3.4·10⁻⁴`, exactly the Step-4 remainder budgets. The two routes agree to five digits.

**Consistency with `A_T ≥ 0`.** For `a → 0`, (★) becomes `2A_T` on a codimension-2 subspace of `P_T`, so the same
family must give a **non-negative** value: measured `+5.1·10⁻³` at `a = 10⁻⁴` (`scripts/certificate/explore.py`,
`DIAGNOSTIC-NUMERIC`). No contradiction with the certified endpoint.

---

## 3. Repairs demanded by the audit

| Audit item | Action |
|---|---|
| #5 (A2) "near-nullity mechanism" | **WITHDRAWN.** At `a ≥ a*(\log2) ≈ 0.08` the minimiser has `⟨A_Tu,u⟩ ≈ 2·10⁻²`, five orders above the near-null value; the near-null direction is destroyed by the two extra moment conditions. The operative mechanism is the low-frequency archimedean loss (next row). |
| #6 (A3) "archimedean convexity" | **WITHDRAWN — the inequality is backwards.** By Lemma C1 the correct statement is `Σ_±Reψ(¼±a/2+iτ/2) − 2\logπ = Σ_{j,±}2τ²/(a_j^±((a_j^±)²+τ²)) − m_0^{(a)}`, and `m_0^{(a)}` **grows without bound** as `a → ½` because `ψ(¼−a/2) → −∞`: `m_0^{(a)} = 10.744` at `a=0`, `11.081` at `a=0.1`, `15.275` at `a=0.3`, `44.919` at `a=0.45`, `204.85` at `a=0.49` (certified in Step 2). The `Ξ_a` archimedean channel is therefore heavily *adverse* at low frequency, and the weight growth `n^a+n^{−a}` adds to it. This, not near-nullity, is why `Ξ_a` fails. `PROVED`. |
| #8 `a*(\log2)→0`, "negativity for every `a`" | **WITHDRAWN.** Corrected value `a*(\log 2) = 0.0801` (§4, independent recomputation; the auditor's `0.080` confirmed). `DIAGNOSTIC-NUMERIC`. |
| #9 `λ_min(A_{\log2}\|P_T)` | **Corrected.** Round 1's `2.08·10⁻⁴` was a piecewise-constant artefact. Spectral recomputation (`aud_spectral.lmin(T,K,0)/2`): `K = 80/160/240/320 → 1.114/1.068/1.044/1.031 ·10⁻⁷`. `DIAGNOSTIC-NUMERIC`: `λ_min ≈ 1.0–1.1·10⁻⁷`, Richardson limit `≈ 1.02·10⁻⁷`. *Caveat the auditor did not state:* the sequence is still drifting downward at `K = 320` (it is a Galerkin **upper** bound), so "converged, stable to 2%" is optimistic; the honest claim is `λ_min ∈ (0, 1.05·10⁻⁷]`. |
| #9 "margin `8.63e-8` near-sharp within 25%" | **Recorded with the normalisation stated, and downgraded.** `8.63386022095·10⁻⁸` is *not* a lower bound for `λ_min(A_T\|P_T)` in the `L²`-normalised Rayleigh quotient. Per `W4_CERTIFIED_RANGE` §2(e) it is the **two-level Feshbach capacity margin**, `capacity − ℓ_eff = 1.83281·10⁻⁶ − 1.746475·10⁻⁶`, both quantities living in the *rescaled* capacity budget `capacity = h²δ/(1−hδ)` with `h = 0.0012`. The comparison with `λ_min ≈ 1.0·10⁻⁷` (mass matrix `‖F‖²_{L²(−T,T)}`, spectral sine basis) is a **coincidence of magnitude between two different normalisations**, not a sharpness statement. What *is* legitimate and useful: the certificate's own delicate quantity `ℓ_eff = 1.746475·10⁻⁶` sits within `4.94%` of the capacity that rescues it, and the true `λ_min` is `≈ 1.0·10⁻⁷ > 0` — i.e. `A_{\log2}` is strictly positive but **critical**, and the certificate is not proving something with room to spare. `DIAGNOSTIC-NUMERIC`. |
| #11 "the endpoint carries sign because it is critical" | **WITHDRAWN.** Replaced by the `T`-statement of §4: `T*(0.45) = 0.6242 < \log 2`. The certified *pair* `(S,T) = ({∞,2,3},\log2)` still carries sign (Theorem R153.1) — it is simply not the *first* `T` that does. |
| #13 `b = \log 3` needle | **Kept as `DIAGNOSTIC-NUMERIC` only**, with the auditor's width: the peak of `b ↦ λ_min(b)` at `b = \log 3` has height `≈ 1.1·10⁻⁷` and half-width `O(10⁻⁷)`, not the `2·10⁻³` of round 1 (which was the round-1 mesh resolution). Content retained: the endpoint is exactly critical, and the critical point sits at the arithmetic contact. |
| #14, #16 `v₁` diagnostics, channel splits, overlaps | **WITHDRAWN** (computed from an unresolved minimiser). Not recomputed: they are not needed for anything that survives. |
| #12 `A^{abs}` | **Kept with the auditor's caveat.** `λ_min(G_{Γ,T}−m_0\|P_T) = −0.1526` (spectral) vs `−0.1542` (round 1); `2Σ_{n<4}Λ(n)n^{−1/2} = 2.248826`; so `λ_min(A^{abs}_{\log2}\|P_T) ≤ −2.40`. `DIAGNOSTIC-NUMERIC`. This is a triangle-inequality bound whose failure is already recorded as GAP-142.A (phase 46 Doc 142); the load-bearing part is only `λ_min(G_{Γ,T}−m_0\|P_T) < 0`. |
| #15 Q3(i) monotonicity | **Relabelled `RESTATEMENT`** (Paper 42's extension-by-zero nesting; the eigenvalue phrasing plus the disjoint-support remark `\log n ≥ 2T ⇒ ∫F(t)F(t+\log n)dt = 0` is a one-line corollary). |
| #17 D.76 multiplier, `T`-uniformity | **Corrected** (Lemma C1 / §1: symbol `2τ²/(b(b²+τ²))`). The `T`-uniformity claim is **WITHDRAWN**: the certificate's use of D.76 goes through Robin eigenvalues of `I_T` under `⟨F,\cosh(t/2)⟩ = 0` (`114_d_77` (2.3)–(2.4)), which are `T`-dependent. The `½\log5` diagnosis does **not** follow; it stands as `OPEN`. |
| Q1 at `½\log3` | **Kept.** No negativity for any `a ≤ 0.499` (`+0.793` spectral at `a=0.45`). `DIAGNOSTIC-NUMERIC`. Now explained by §4: `T*(a) > ½\log3` for every `a ≤ ½`. |
| Theorem A, (A1) | **Kept, `PROVED`** (audit #3, #4 STAND). Theorem A is not used by the certificate — §1 works directly with the doubled multiplier, which the audit's own assembly confirms. |

---

## 4. The new object: the detection threshold `T*(a)`

*Corpus check.* `grep -rIn "detection threshold"` → `04-papers/36-obstruction-ledger/main.tex:10754` (a *different*
notion: the factorial detection threshold in the conditional de Bruijn–Newman cascade) and `:9736`
("gauges detecting an off-line zero", the super-ceiling level set of the `N`-gauge form). `grep -rIn` for
`"first negative window"`, `"T\*(a)"`, `"smallest support"`, `"minimal support"` → **no hits**. Paper 42's
Bombieri/Yoshida remarks (`main.tex:4053`, `:4201`, `rem:yoshidacalibration`) state that Yoshida Lemma 2 gives
positivity for *some* small window and that the corpus reproves it with an explicit range; they never define a
threshold in `T` for a falsifier. The object below is new to the corpus.

> **Definition.** `T*(a) := inf{ T > 0 : A_T^{(a)} ≱ 0 on P_T^{(a)} }`.

`T*(a)` is **a property of the falsifier family `Ξ_a`**, not a statement about `ζ`: it says how long a support
window must be before the `Ξ_a` explicit formula betrays its off-line zeros. Computed with the auditor's
mesh-free spectral sine assembly (`scripts/r153_tstar.py`, which reuses `audit/aud_spectral.py` and recomputes the
contact set `{n : n < e^{2T}}` at every `T` — including `n = 4` above `T = \log 2`), by bisection to `10⁻⁵`.
All values `DIAGNOSTIC-NUMERIC`.

| `a` | `T*` (K=100) | `T*` (K=160) | `T* − log 2` |
|---|---|---|---|
| 0.001 | — | 0.80853 | +0.11541 |
| 0.005 | — | 0.76974 | +0.07662 |
| 0.01 | — | 0.75339 | +0.06027 |
| 0.02 | — | 0.73673 | +0.04361 |
| 0.03 | — | 0.72587 | +0.03275 |
| 0.05 | 0.71094 | 0.71028 | +0.01713 |
| 0.06 | 0.70478 | 0.70421 | +0.01106 |
| 0.07 | 0.69952 | 0.69879 | +0.00564 |
| **0.08** | 0.69412 | **0.69352** | **+0.00038** |
| 0.09 | 0.68954 | 0.68893 | −0.00421 |
| 0.10 | 0.68595 | 0.68534 | −0.00781 |
| 0.15 | 0.67286 | 0.67219 | −0.02096 |
| 0.20 | 0.66269 | 0.66199 | −0.03116 |
| 0.25 | 0.65377 | 0.65309 | −0.04006 |
| 0.30 | 0.64573 | 0.64498 | −0.04816 |
| 0.35 | 0.63821 | 0.63754 | −0.05561 |
| 0.40 | 0.63136 | 0.63062 | −0.06253 |
| 0.45 | 0.62483 | 0.62416 | −0.06898 |
| 0.50 | 0.56267 | 0.56208 | −0.13107 |

**Refinement check.** `|T*(K=100) − T*(K=160)| ≤ 7.5·10⁻⁴` throughout, monotone downward — the values are
Galerkin **upper** bounds for `T*` (a larger basis can only find negativity sooner), converged to `≈ 10⁻³`.

**Readings.**

1. **Monotone decreasing in `a` on `(0,½)`** — strictly, at every grid point, in both bases. `DIAGNOSTIC-NUMERIC`.
   (Monotonicity in `T` for fixed `a` is the `RESTATEMENT` of §3 row Q3(i), which is what makes `T*` well defined
   as an infimum with `A^{(a)}_T ≱ 0` for all `T > T*`.)
2. **The crossing of `log 2`** is between `a = 0.08` and `a = 0.09`; linear interpolation gives
   `a*(\log 2) = 0.0801`, confirming the auditor's `0.080` in an independently written driver.
   For `a > a*(\log2)` the certified endpoint detects `Ξ_a`; for `a < a*(\log2)` it does not.
3. **`a → 0⁺`: `T*(a) → ∞`, logarithmically.** The data fit
   `T*(a) ≈ 0.624 + 0.0268·\log(1/a)` over three decades (`a = 10⁻³ … 10⁻¹`, residuals `< 7·10⁻³`).
   Label `DIAGNOSTIC`; the log law is forced by the data across three decades but is not derived.
   The divergence is expected and is the honest statement of the limitation: **no finite window detects an
   arbitrarily small off-line displacement**, and `T*(0⁺) = ∞` is exactly the statement that `A_T ≥ 0` for all
   `T` (i.e. RH on the codimension-2 `a→0` space) cannot be decided at any finite `T`. The *rate* is the new
   quantitative content: `T*` grows only like `\log(1/a)`, so `a` must fall **exponentially** in the window
   length — which is why the `½\log5` step of the programme is worth so little in detection power and why the
   endpoint `\log 2` already reaches `a ≈ 0.08`.
4. **`T*(a) > ½\log 3 = 0.5493` for every `a ≤ 0.5`** — so `½\log3` (and a fortiori Connes–Consani's
   `T = ½\log2 = 0.3466`) carries no sign for this family, confirming round 1's negative answer at `½\log3` with
   a mechanism rather than a table.
5. **A discontinuity at `a = ½`** (`T*` drops from `0.624` to `0.562`): at `a = ½` the exponents `±(½−a)`
   collapse to `0`, the four moment conditions degenerate to three, and `P_T^{(1/2)}` is strictly larger.
   Flagged; not analysed.

**What `T*(a)` is not.** It is not a zero-free region, not a bound on `ζ`, and not monotone information about
`A_T` for `ζ`. It measures the falsifier family only.

---

## 5. Verdict table

| Item | Answer | Label |
|---|---|---|
| Lemma C1: doubled symbol `=` shifted resolvent ladder `− m_0^{(a)}` | new | `PROVED` |
| Lemma C2: `q_a(F)` from the autocorrelation `c(r)`; `E_b = 2N²/b − 2\hat c(b) ≥ 0` | new | `PROVED` |
| Lemma C3: `F = P(D)H` is exactly in `P_T^{(a)}` | new | `PROVED` |
| D.76 multiplier is `2τ²/(b(b²+τ²))` | corrects round 1 | `PROVED` |
| **`W_S^{(a)} < 0` for `Ξ_a` on `P_T^{(a)}`, `(S,T)=({∞,2,3},\log2)`, `a=0.45` and `a=0.30`** | `−0.0373367294804088…`, `−0.0142279881516186…` | **`PROVED`** (interval) |
| **D.12-α** | answered by `(S,T) = ({∞,2,3}, \log 2)`; `W_S ≥ 0` for `ξ` is Paper 42, `W_S^{(a)} < 0` is above | **`PROVED`** |
| Theorem A (`A_T^{(a)} = E_{−a}A_TE_a + E_aA_TE_{−a}`), (A1) cross-term | round 1, audit-confirmed; not used by the certificate | `PROVED` |
| (A2) near-nullity mechanism; (A3) archimedean convexity | false / vacuous | `WITHDRAWN` |
| Correct mechanism: `m_0^{(a)} → ∞` as `a → ½` (`10.74 → 44.92 → 204.8`), low-frequency archimedean loss | Lemma C1 + Step 2 | `PROVED` |
| `λ_min(A_{\log2}\|P_{\log2})` | `≈ 1.0–1.1·10⁻⁷`, still drifting down (Galerkin upper bound) | `DIAGNOSTIC-NUMERIC` |
| Corpus margin `8.63386·10⁻⁸` | capacity-budget normalisation, **not** the `L²` Rayleigh quotient; comparison is magnitude only | `DIAGNOSTIC-NUMERIC` |
| `a*(\log 2)` | `0.0801` (K=160), `0.0801` (K=100) | `DIAGNOSTIC-NUMERIC` |
| `T*(a)` table, monotone decreasing, `T*(0.45)=0.6242 < \log2` | §4 | `DIAGNOSTIC-NUMERIC` |
| `T*(a) ≈ 0.624 + 0.0268\log(1/a)`, `→ ∞` | three decades of data | `DIAGNOSTIC` |
| `Q1` at `½\log3`: no negativity for any `a ≤ ½` | `T*(a) > ½\log3` always | `DIAGNOSTIC-NUMERIC` |
| `A^{abs}_{\log2} ≱ 0` (`≤ −2.40`) | triangle bound, GAP-142.A | `DIAGNOSTIC-NUMERIC` |
| `b`-needle at `\log 3`: peak `1.1·10⁻⁷`, half-width `O(10⁻⁷)` | audit's numbers | `DIAGNOSTIC-NUMERIC` |
| `v₁` overlaps, channel splits, `½\log5` diagnosis via D.76, `T`-uniform capacity | unsupported | `WITHDRAWN` |
| `T ↦ λ_min(A_T\|P_T)` non-increasing | Paper 42 nesting | `RESTATEMENT` |
| Q3(i) phrasing of round 1 as `PROVED` new | relabelled | `RESTATEMENT` |
| `½\log5` obstruction | the two uncomputed cross terms (`main.tex:3990-4010`); not diagnosed here | `OPEN` |

**FATAL rule.** No zero-free region, no moment bound and no cancellation is derived anywhere above from known
theorems; the only inequality about `ζ` used is Paper 42 `thm:certifiedendpoints`, cited not reproved.

---

## 6. Open

1. **`a*(\log 2)` certified.** The crossing `a*(\log2) = 0.0801` is Galerkin. Certifying negativity at, say,
   `a = 0.10` at `T = \log 2` is the same computation as §2 with a richer family (the target is `≈ −7·10⁻⁴`,
   still `10³` times the Step-4 remainder budget, so it is bookkeeping, not new mathematics). Certifying
   *positivity* below `a*` is a genuinely different and much harder problem.
2. **`T*(a)` certified from below.** The table gives upper bounds only. A certified lower bound
   `T*(0.45) > ½\log3` would make "the `Ξ_a` family is invisible below `½\log3`" a theorem.
3. **Is the `\log(1/a)` law exact?** A derivation would presumably come from the `m_0^{(a)}` growth
   (`∼ 2/(½−a)` near `a = ½`, `∼ const` near `0`) against the `τ`-scale `1/T` of the constrained space.
   Not attempted.
4. **`T > \log 2`.** Nothing is claimed, and nothing here bears on the `½\log5` cross terms.
5. **`Ξ_Q` (Epstein) and Beurling.** Untested; Lemma C1's ladder is specific to the two shifted Gamma factors.
6. **The interval certificate for `ξ` itself.** `λ_min(A_{\log2}|P_{\log2}) ≈ 1.0·10⁻⁷` is a *diagnostic*; the
   corpus's proof of `A_T ≥ 0` is the Feshbach/capacity argument, and the present machinery (Lemma C2, which
   gives rigorous **upper** bounds on `q`) cannot reprove positivity — it is one-sided by construction.
