# R153.004 — Confirmation round: is the interval certificate a proof?

* Mandate: decide whether the round-2 interval
certificate is a **proof** that `⟨A_T^{(a)}F,F⟩ < 0` for the explicit `F` at `T = log 2`, `a = 0.45` (and `0.30`),
on `P_T^{(a)}`. Everything below was rederived or rerun by the auditor. Sources of truth read: Paper 42
`main.tex:4072–4230`; Paper 47 `main.md:3141–3180` (Proposition 12.6, (S1)–(S2)); phase 114
`114_d_76_GAMMA_TAIL_SINGLE_ROBIN_DOMINATION.md`, `114_d_77_SEMILOCAL_GUARD_BAND_TRACE_AUDIT.md`;
phase 118 `W4_CERTIFIED_RANGE.md` §§2(e), 197–208.*

---

## 0. Certificate verdict

> **PROOF ACCEPTED**, conditionally on Paper 42 `thm:certifiedendpoints` for the `ξ` half, and subject to two
> **write-up** defects (§2.3, §2.5) that are repairable in place and do not touch the numbers.

`⟨A_{\log2}^{(a)}F,F⟩ < 0` for the displayed `F` is established. Every step of the chain
Definition 1.1 → Lemma C1 → Lemma C2 → Lemma C3 → Steps 1–5 was rederived independently and holds; the
interval code is genuinely `mpmath.iv` end to end; the printed enclosures reproduce verbatim; and the value is
confirmed to 6–7 digits by two further, wholly independent evaluations of the same `F`.

---

## 1. Verdict table

| # | Claim | Verdict | Reason |
|---|---|---|---|
| 1 | **Lemma C1**: `Σ_±Reψ(¼±a/2+iτ/2) − 2logπ = Σ_{j≥0,±}2τ²/(a_j^±((a_j^±)²+τ²)) − m_0^{(a)}`, `a_j^±=2j+½±a` | **STANDS** (`PROVED`) | Rederived from `ψ(z)=−γ+Σ_k[1/(k+1)−1/(k+z)]`: `k+z=(a_k^±+iτ)/2`, so `Re(k+z)^{−1}=2a_k^±/((a_k^±)²+τ²)`; differencing against `τ=0` gives `2τ²/(a_k(a_k²+τ²))` termwise. Verified numerically at `τ=0,1,7.3`, `a=0.30,0.45` to 10 digits (`Σ_{j<4·10⁵}`) |
| 2 | Constant `m_0^{(a)} = 2logπ − ψ(¼+a/2) − ψ(¼−a/2)`; reduces to `2m_0` at `a=0` | **STANDS** | `ψ(¼) = −γ−π/2−3log2`, so `m_0^{(0)} = 2(logπ+γ+π/2+3log2) = 2m_0`, the **correct factor 2** for the doubled block. Cross-checked against `main.tex:4122`: `g_Γ−m_0 = Reψ(¼+iτ/2)−logπ`. Independent scipy values `44.918692819404` (`a=.45`), `15.274599256695` (`a=.30`) match the certified enclosures to all printed digits |
| 3 | **Sign direction**: truncation of `Σ_j E ≥ 0` is a *lower* bound, so the remainder must be **added** | **STANDS** | `cert.py:54` computes `qup = q + tail`, i.e. an **upper** bound for `q_a(F)`, and negativity is asserted from `qup.b < 0` (`cert.py:64`). Direction correct — this was the single most likely place to hide a fatal sign error, and it is right |
| 4 | Remainder bound `Σ_{j>J,±}E_{a_j^±} ≤ A/J + B/(2J²)`, `A=½(F(T)²+F(−T)²)`, `B=½\sup|c''|` | **STANDS with a formal gap** (§2.3) | `c'(0⁺) = −½(F(T)²+F(−T)²)` exactly (verified: `A = 0.024535765² = 6.02004·10⁻⁴`, matching the certified `A`). `N²−c(r) ≤ Ar+Br²` by Taylor; `E_b ≤ 2A/b²+4B/b³+2N²e^{−bL}/b`; `a_j^±≥2j` and `Σ_{j>J}j^{−2}<1/J`, `Σ_{j>J}j^{−3}<1/(2J²)` give `A/J+B/(2J²)`. **The `2N²Σ_{j>J}e^{−a_jL}/a_j` term is omitted** from both the lemma and the code. Its size is `< 10^{−2400}`; harmless, but the inequality as written is not literally proved |
| 5 | Nikolskii/Legendre `‖P‖_∞ ≤ (d+1)‖P‖_{L²(−T,T)}/√(2T)`; `\sup|c''| ≤ 2‖F‖_∞‖F'‖_∞+‖F‖₂‖F''‖₂` | **STANDS** | Both rederived (Legendre expansion + Cauchy–Schwarz; `c''(r)=F'(T−r)F(T)−F(T−r)F'(T)+∫FF''`). `cert.py:47–52` implements exactly these |
| 6 | **Lemma C3**: `F=P(D)H`, `P(D)=(D²−p²)(D²−q²)`, `H=(T²−t²)⁴Σg_it^i` lies in `P_T^{(a)}` exactly | **STANDS as a statement; proof text REFUTED** (§2.5) | The lemma is true by the **adjoint** argument: `∫e^{βt}P(D)H = P(−β)∫e^{βt}H` after four integrations by parts, and `P(−β)=(β²−p²)(β²−q²)=0` for `β∈{±p,±q}`. The boundary terms need `H,H',H'',H'''` to vanish at `±T`, exactly the order-4 zero of `(T²−t²)⁴` against the order-4 operator — matched with nothing to spare, correctly. **The written proof ("choosing the factor `(D+β)` as the innermost one kills the `β`-moment") does not work**: `P(D)H = Q(D)[(D+β)H]` does not make `∫e^{βt}P(D)H` a boundary term. Replace it with the adjoint line. Verified numerically on the *actual* code-built `F` (deg 18): all four moments `≤ 6·10⁻⁵⁹` at `dps=60` |
| 7 | `P_T^{(a)}` = the four exponentials `±(½+a)`, `±(½−a)`; polar block absent on it | **STANDS** | Prop. 12.6 (S1): primitivity is `Φ_F(p)=0` for `p∈P={−a,a,1−a,1+a}`, kernel spanned by `e^{(p−½)t}`; `p−½ ∈ {±(½+a),±(½−a)}` exactly. `\hat f(s)=∫Fe^{(s−½)t}` (`main.tex:4082`) confirms the pullback. The rank-4 polar form vanishes identically on `P_T^{(a)}`, as `M_±` does on `P_T` for `ξ` |
| 8 | Prime block: exactly `n=2,3`; weights `Λ(n)n^{−1/2}(n^a+n^{−a})`; **minus** sign | **STANDS** | `e^{2T}=4` ⇒ contacts `{2,3}` (`assemble.py:61–65` loops only `n∈{2,3}`). `main.tex:4122` has `−Σ(Λ(n)/√n)(S_{\log n}+S_{−\log n})`, whose form is `−2(Λ(n)/√n)c(\log n)`; `assemble.py:88` subtracts `2c_nn^{−1/2}c(\log n)` with `c_n=Λ(n)(n^a+n^{−a})`, which at `a=0` is exactly twice the `ξ` term — consistent with the doubled archimedean block and `m_0^{(a)}=2m_0`. Normalisation is internally coherent: `q^{(0)} = 2q_ξ` |
| 9 | Autocorrelation `c(r)` evaluated exactly as a degree-37 interval polynomial; `E_b = 2N²/b − 2\hat c(b) ≥ 0` | **STANDS** | `‖F−S_rF‖²=2(N²−c(r))`, `c` supported in `|r|≤L`; the two `\hat c` representations (series `bL≤100`, asymptotic `bL>100`) carry rigorous, correctly-signed tails (series: `maxc·L·(bL)^{M+1}/(M+1)!·geom`, geom `≤1.33` bounded by the coded factor `2`; asymptotic: `maxc·L·e^{−bL}/(b−\deg/L)`, valid since `b>72>\deg/L≈27`). The per-entry error is added as a symmetric interval and is conservative under the `g_ig_k` recombination |
| 10 | `mpmath.iv` used end to end; no float leaks | **STANDS** | `grep "float(\|np\.\|math\."` over `polyalg.py, xiform.py, assemble.py, cert.py` yields exactly **three** float uses, all *branch decisions*, never arithmetic: `assemble.py:17–18` (series-vs-asymptotic split — both branches rigorous either way), `assemble.py:62` (contact-set test, `n<4`), `xiform.py:106` (same split in the unused `Chat` class). Coefficients are **exact decimal strings** parsed by `iv.mpf` (`cert.py:18–19`), `T=iv.log(iv.mpf(2))`, `a=iv.mpf('0.45')`. `numpy`/`scipy` appear only in `crosscheck.py` and `explore*.py`, which are labelled diagnostics and are not in the certificate path |
| 11 | Printed report values are what the code prints | **STANDS** | Rerun verbatim: `q_J ∈ [−0.0275319586879440309, −0.0275319586879440308]`, tail `≤ 2.4876171140312·10⁻⁴`, `Rayleigh ≤ −0.0373367294804087`, `NEGATIVE CERTIFIED: True`; `a=0.30` gives `−0.0142279881516186`. Identical to R153_003 §2 to every printed digit, including `‖F‖²`, `m_0^{(a)}`, `A`, `B` |
| 12 | Stability in `J` | **STANDS** | `J=500 → −0.032344`, `J=2000 → −0.037337`, `J=4000 → −0.037586`: monotone toward the true value `−0.037670`, tail shrinking as `1/J`. Sign certified at every `J` tested |
| 13 | Stability in precision | **STANDS, with a floor** | `iv.prec = 300, 400, 600` all agree to every printed digit and certify the sign. At `iv.prec = 200` the enclosure **blows up to `±8437`** and the script correctly prints `NEGATIVE CERTIFIED: False`. So the certificate has a precision floor (the degree-37 alternating series at `M=400` cancels ~200 digits) — it **fails safe**, never silently. This floor is not documented in R153_003 and should be |
| 14 | Independent evaluation of `q_a(F)` for the same `F` | **CONFIRMS** | Three routes now agree: (i) certified ladder, `J→∞` limit `≈ −0.03767`; (ii) construction's `crosscheck.py` Fourier-multiplier quadrature: `−0.03766956` / `−0.01455440`; (iii) **this auditor's own** from-scratch route (own polynomial construction of `F`, own Gauss autocorrelation `c(r)`, own ladder to `J=2·10⁴`, own `ψ` from scipy): `−0.03766967` / `−0.01455470`. Agreement to 6–7 digits; both certified upper bounds sit **above** the true value by exactly the Step-4 tail budget, as they must |
| 15 | **Theorem R153.1(ii)** `W_S^{(a)} < 0` at `(S,T)=({∞,2,3},\log2)`, `a=0.45, 0.30` | **STANDS** (`PROVED`) | Consequence of 1–14 |
| 16 | **D.12-α answered**, label `PROVED` | **STANDS, one label repair** (§2.4) | Half (i) is Paper 42 `thm:certifiedendpoints`, a computer-assisted theorem **cited not reproved**; the label should read `PROVED (conditional on Paper 42 thm:certifiedendpoints)`. Also to state plainly: `P_T^{(a)} ⊄ P_T`, so `F` is *not* a single function violating one inequality and satisfying the other — the comparison is between each model's own primitive space, which is what (S1) and D.12-α ask for, but the report never says it |
| 17 | Mechanism restated as `m_0^{(a)} → ∞` (`10.74 → 44.92 → 204.8`), low-frequency archimedean loss; (A3) withdrawn | **STANDS** (`PROVED`) | Immediate from Lemma C1 and `ψ(¼−a/2) → −∞`; `m_0^{(a)}` values independently reproduced |
| 18 | D.76 multiplier `2τ²/(b(b²+τ²))`; `T`-uniformity withdrawn | **STANDS** | `∫_0^∞e^{−br}2(1−\cos rτ)dr = 2/b − 2b/(b²+τ²) = 2τ²/(b(b²+τ²))`. Consistent with `114_d_76` (1) and its `E_b ≥ (B/b)³E_B`. `T`-dependence of `114_d_77` (2.3)–(2.4) correctly conceded |
| 19 | `T*(a)` table, labels `DIAGNOSTIC-NUMERIC`, Galerkin **upper** bounds | **STANDS** | A Galerkin `λ_min` is an upper bound, so detected negativity is genuine at the discrete level only and `T*` computed is an upper bound for the true `T*` — stated correctly. Bisection is licensed by monotonicity in `T` (zero extension preserves the four moment conditions), which is the `RESTATEMENT` of Q3(i) applied to `A^{(a)}`; the discrete basis is not literally nested in `T`, a caveat the report omits but which the `DIAGNOSTIC` label absorbs |
| 20 | Log-fit `T*(a) ≈ 0.624 + 0.0268\log(1/a)`, label `DIAGNOSTIC` | **STANDS as labelled** | Checked: `a=10⁻³ → 0.809` vs `0.80853`; `a=0.1 → 0.6857` vs `0.68534`; `a=0.05 → 0.7043` vs `0.71028` (residual `6·10⁻³`, within the stated `7·10⁻³`). The fit is claimed only on `[10⁻³,10⁻¹]` and fails outside it (`a=0.45`: `0.645` vs `0.624`). The inference `T*(0⁺)=∞` is extrapolation and is labelled as such |
| 21 | `T*(a) > ½\log3` for all `a ≤ 0.5`; `½\log3` and CC's `½\log2` carry no sign | **STANDS** (`DIAGNOSTIC-NUMERIC`) | Table minimum `0.56208 > 0.54931` |
| 22 | `a=½` discontinuity flagged, not analysed | **STANDS** | At `a=½` the moment matrix has two coincident rows; `null_space` returns a rank-3 constraint, i.e. the strictly larger `P_T^{(1/2)}`. Correctly flagged |
| 23 | **Construction vs predecessor on "margin near-sharp within 25%"** | **Construction is RIGHT; predecessor's #9 by-product REFUTED** | `W4_CERTIFIED_RANGE.md:197–208` states it explicitly: `capacity = 1.8328136·10⁻⁶`, `ell_eff = 1.746475·10⁻⁶`, `margin = capacity − ell_eff = 8.6339·10⁻⁸`, inside the rescaled budget `capacity = h²δ/(1−hδ)`, `h = g − η`, `g = 0.0015`. It is a **two-level Feshbach capacity margin**, not a lower bound on the `L²` Rayleigh quotient. The coincidence with `λ_min ≈ 1.0·10⁻⁷` is a magnitude coincidence across two normalisations. The legitimate reading, `capacity/ell_eff − 1 = 0.04944`, is the corpus's own line 205 |
| 24 | `λ_min(A_{\log2}|P_{\log2}) ∈ (0, 1.05·10⁻⁷]`, still drifting at `K=320` | **STANDS** | Honest: a Galerkin value is an upper bound; the predecessor's "converged, stable to 2%" was the over-claim, and the construction's correction is right |
| 25 | Round-2 repairs vs R153_002's required list (items 1–8) | **7 of 8 complete** | 1 ✓ (with the *correct* replacement, now `PROVED` via C1), 2 ✓ (numbers redone; but round 1's tables remain in the corpus uncorrected — mark `R153_001` superseded), 3 **partial**: `a*→0` retracted and `a*=0.0801` recorded, but the jump value `λ(0⁺) = +1.24·10⁻³` the auditor asked to be recorded is **nowhere** in round 2, 4 ✓, 5 ✓, 6 ✓, 7 ✓, 8 ✓ |
| 26 | FATAL rule; no `ζ` sign beyond `\log 2` | **CLEAN** | No zero-free region, no moment bound, no cancellation derived from known theorems. The only `ζ` inequality used is `thm:certifiedendpoints`, cited. §0 of R153_003 lists the non-claims explicitly and §4 repeats that `T*` "measures the falsifier family only". `T*(a)` for `T > \log2` is stated as a property of `Ξ_a`, not of `ζ` — correct, since `A_T^{(a)} ≱ 0` says nothing about `A_T` |

---

## 2. The five things that must change (none is fatal)

**2.1 `Σ_{j>J}` exponential term.** Step 4's displayed inequality omits `2N²Σ_{j>J,±}e^{−a_j^±L}/a_j^±`. Add it, or
add a blanket `+10^{−100}` to `tail` in `cert.py:53`. Size: `< 10^{−2400}`.

**2.2 Lemma C3's proof.** Delete the "innermost factor `(D+β)`" sentence. Replace with: *four integrations by
parts, licensed by `H,H',H'',H''' ∈ C_0` at `±T`, give `∫e^{βt}P(D)H = P(−β)∫e^{βt}H`, and `P(−β)=0` for
`β ∈ {±p,±q}`.* The lemma and the order count (`(T²−t²)⁴` against `\deg P(D)=4`) are correct as they stand.

**2.3 Precision floor.** Record that the certificate requires `iv.prec ≥ ~300`; at `prec = 200` the enclosure
blows up and the script correctly reports failure. Non-reproducibility at the default precision of a naive rerun
is the kind of thing a referee finds first.

**2.4 Label of D.12-α.** `PROVED (ii) unconditionally; (i) inherited from Paper 42 thm:certifiedendpoints
(computer-assisted, Feshbach margin 8.63·10⁻⁸)`. And add one sentence: `P_T^{(a)}` is *not* a subspace of `P_T`;
each model is tested on its own primitive space, per (S1).

**2.5 Two bookkeeping omissions.** (a) Record `λ(a→0⁺) = +1.24·10⁻³` (R153_002 repair 3). (b) Add a banner to
`R153_001_ROUND1.md` marking §1.3, §2, §3 superseded — its `2.08·10⁻⁴` and `a*→0` are still on disk.

---

## 3. What the phase now holds

`PROVED`: Lemmas C1–C3 (C3 with the proof rewritten), the corrected D.76 symbol, Theorem A and (A1), the
mechanism (`m_0^{(a)}` divergence), and **`W_{{∞,2,3}}^{(a)}(F,F) < 0` at `T = \log2` for `a = 0.45, 0.30`** by
interval arithmetic. Hence **D.12-α is answered** — conditionally on Paper 42's `ξ` half. That is the first
statement in the corpus which a function with off-line zeros violates at a **finite, certified** `T`, and which
Connes–Consani's archimedean window (`T = ½\log2`, where `T*(a) > 0.56` for every `a`) does not reach.

`DIAGNOSTIC-NUMERIC` and nothing more: `a*(\log2)=0.0801`, the whole `T*(a)` table, `λ_min(A_{\log2}|P_{\log2})`,
the `\log3` needle, `A^{abs}`. `DIAGNOSTIC`: the `\log(1/a)` law. `OPEN`: certified `a*`, certified lower bounds
for `T*`, `½\log5`, `Ξ_Q`, Beurling.

**Scripts rerun or written by this audit.** `certificate/cert.py` (at `J=500,2000,4000` and `prec=200,300,400,600`),
`certificate/crosscheck.py`, plus three auditor scripts: the Lemma C1 symbol check, the four-moment check on the
code-built `F` at `dps=60`, and a from-scratch double-precision ladder evaluation
(`scratchpad/ind5.py`: own `F`, own Gauss autocorrelation, `J=2·10⁴`) returning `−0.03766967` / `−0.01455470`.
