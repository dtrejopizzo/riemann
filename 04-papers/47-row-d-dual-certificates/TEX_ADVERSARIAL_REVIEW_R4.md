# Adversarial referee report R4: `main.tex` (Paper 47), 73 pp., whole-paper review after rounds 6–8

Scope: (a) full-rigour reading of everything added since `main_pre_R4.tex.bak`: 1220 diff lines, mainly
§1 (abstract/intro), `lem:monoT`, `lem:roughEF`, `prop:arch`/`lem:strict`/`cor:Tarch`, `lem:parity`/`thm:index`/`cor:H1`,
§10.3–10.7, App. A.4, App. C. Each was checked against the paper's own `def:W`, `eq:nuw`, `def:PD` (signed `ν`),
`P_T`, `\Ainf`, `Γ_T`, `\laminf`, `\laminfP`, `\lamP`, `\lamA`, `λ^W`, `𝒲_T`, and against memos R155_052/053/055/058/059/061.
(b) Rulings on the six items the editors flagged.
(c) Global checks, including a re-run of every certificate file cited, the script of the margin crossings, and
`main.log`.

**VERDICT: MINOR REVISION (accept after the repairs below).** Nothing is FATAL. No headline theorem changes, no
label changes. The endpoint of record is unchanged (`λ_min(A_{½log3}|P_{½log3}) ≥ 8.8577·10⁻⁵`, primitive form).
The paper claims no sign for `ζ` beyond `log 2`, and "first beyond" does not occur. Two findings are
substantive. **R4-1:** the margin crossings `1.226`, `1.852` printed in `rem:margin` and in the label table are
wrong, because the script that produced them has a bug that makes the bound 21 times too small; the audit
R155_059 passed them. **R4-2:** the proof of `cor:RH` (a)⇒(c), which the reduction chain and `thm:Al`(c)
depend on, has two gaps: rough-test positivity, and zeros counted with multiplicity. Two sentences and one
citation repair both. All other findings are one-clause repairs.

---

## 1. Rulings on the editors' six items

**Item 1 (endpoint at `T₀(0)`): the editors are right, and the text must say strict.** At `T = T₀(A)`,
`φ((3π/2T)²) = φ(x_A) = −C₀ − A`, so the bound of `thm:SC` equals `0`. That gives "`≤ 0`", not "negative".
Strictness is not available from `thm:SC`'s ingredients: the Song–Vondraček inequality `λ_n ≤ φ(μ_n)` and the
codim-2 min–max are non-strict, and for `A = 0` the comb step gives nothing. For `A = 0` the non-strict
statement at `T₀(0)` is in fact true, but only through `cor:Tarch`, which is machine-verified and gives
`λ^{∞,P} < 0` for `T ≥ 0.60`. `prop:arch`(ii) currently derives the endpoint from `thm:SC`, and that derivation
is invalid. Every downstream use (`prop:finite`(iii), `thm:finmod`(i), `cor:void`, L2548) already reads
`T > T₀(0)`, so the repair costs nothing. See R4-3.

**Item 2 (`cor:RH`, rough minimiser): not written adequately.** Text is supplied in R4-2. Two points.
(a) Only the *inequality* `Σ_γ|F̂⋆(γ)|² ≤ W_T(F⋆)` is needed. It follows from Fatou applied to the mollification
of `lem:roughEF`, whose archimedean, polar and prime steps use only hypothesis (a). The same Fatou step then
*verifies* (b) under RH, so the equality holds as well.
(b) There is a second gap, present since R1 and missed by R1–R3. The count `N(t) ≫ t log t` counts zeros
with multiplicity, but `W_T(F⋆) = 0` forces `F̂⋆` to vanish only at the *distinct* ordinates. Jensen gives `O(t)`
zeros for exponential type, which beats `≫ t` (all that `N(t)` divided by an `O(log t)` multiplicity bound
gives), but not `≫ t log t` counted with multiplicity. Repair: under RH the multiplicity at height `t` is
`O(log t / log log t)` (Titchmarsh, Thm 14.13), so there are `≫ t log log t` distinct ordinates. A real
minimiser must also be stated: `W_T(u+iv) = W_T(u) + W_T(v)`.

**Item 3 (`prop:P` on the whole form domain): the editor's sentence (L681–685) is accurate but not sufficient.**
The *statement* of `prop:P` (L663–664) still asserts `W_T(F) = Σ_ρ Φ_F(ρ)Φ_F(1−ρ)` for every `F` in the form
domain. That is unproved for rough `F`, where the zero sum need not converge. It is also wrong as written for
complex `F`: the Hermitian zero form is `Σ Φ_F(ρ)\overline{Φ_F(1−\barρ)}`, and the proof itself says "for the real
forms considered here". The statement must be restricted, with the zero-sum clause routed through
`lem:roughEF`. See R4-4.

**Item 4 (DISPUTE on `lem:strict`): the editor is right; the memo remark R155_061 L232 is wrong and must not be
added.** I worked the Euler–Lagrange argument in three cases. Let `F⋆` be a real minimiser at `T'`, extended by
zero, and let `G₀ ∈ C_c^∞(T',T)`.
- *(α) `\laminfP` / `λ_par` (the paper's case).* Tests must lie in `P^par_T`. This forces `∫G₀e^{±y/2} = 0` and
  leaves two multipliers: `Φ = αe^{y/2} + βe^{−y/2}` on `(T',T)`. Decay forces `α = 0`. The power series in
  `w = e^{−2y}` gives `2c₀ = β` and `c_k = 0` for `k ≥ 1`.
- *(β) The bottom of `Γ_T` on `L²(I_T)` (no constraint, no pole term).* Every `G₀` is admissible, so
  `∫ΦG₀ = 0` for all of them. Then `Φ ≡ 0` on `(T',T)`, `α = β = 0`, and all `c_k = 0`. This is the editor's case.
- *(γ) `\laminf` itself (`\Ainf` with the pole term `2A(F)B(F)`, unconstrained).* The pole term polarises to
  `A(F⋆)B(G₀) + B(F⋆)A(G₀)` and plays the role of the multipliers: `Φ = 2B(F⋆)e^{y/2} + 2A(F⋆)e^{−y/2}`. Decay
  forces `B(F⋆) = 0`. The series gives `c₀ = A(F⋆)`, a tautology and literally the memo's "`c₀ = β/2`", together
  with `c_k = 0` for `k ≥ 1`.

The memo's error is the belief that the argument then "stops". It does not: `c_k = 0` for all `k ≥ 1` already
forces `F⋆ = 0`. With `u = e^{2x}`, `∫(u f(u))u^j du = c_{j+1} = 0` for every `j ≥ 0`. Since `u f ∈ L¹` on a
compact subinterval of `(0,∞)`, Weierstrass gives `u f = 0`, hence `f = 0`. So:
(1) strict monotonicity holds in all three cases, including `\laminf` and the bottom of `Γ_T`;
(2) even in case (α) the clause "`c₀ = A(F⋆) = 0` because `F⋆ ∈ P_{T'}`" is **not needed**, so the audit's
"correct and essential" is also wrong. The proof as printed is correct, because it uses a true but superfluous
fact. Omitting the memo remark was right. An optional one-line simplification and remark is in R4-12.

**Item 5 (`prop:negtrace`(v) repair): correct.** The void symbol `σ − c·1_off` (void because `σ₊ ≠ 0` on the
band) is correctly replaced by `σ·1_band − c·1_off`. The entire-function argument is sound: `S` is compact,
`0 ≤ S ≤ 1`, and `λ₀ = ‖S‖` is attained at `F₀`. If `λ₀ = 1`, then `F̂₀ = 0` on the open set `|τ| > τ_last`, so
`F̂₀ ≡ 0`, a contradiction. The two form bounds `(s₊ − c(1−λ₀))‖F‖²` and `(c(1−λ₀) − ‖Neg_T‖)‖F‖²` check line by
line, and both symbols agree with `σ` on `|τ| ≤ τ_last`. The only defect is notational: `R_T` is used without
definition in "the notation of §9.2" (R4-13).

**Item 6 (`thm:finmod`(i)): correct, including at `T = ½log N`.** With `a = Λ𝟏_{n≥N}` and the strict convention
`N_T = {n : log n < 2T}`, `n ∈ N_T` means `n < e^{2T} ≤ N` for `T ≤ ½log N`. Equality `T = ½log N` is included,
because `n = N` is not yet a contact. So the comb is empty and `RD_T(a) ⟺ \laminfP(T) ≥ 0`, as in
`prop:finite` and `def:PD`. Then:
- **Holds on `(0, 0.58]`:** `thm:index`(i) gives `\laminfP > 0`, and `N ≥ 5` gives `½log N ≥ 0.8047 > 0.58`.
- **Fails on `[0.60, ½log N]`:** `cor:Tarch` gives `\laminfP < 0` for all `T ≥ 0.60`, and the interval is
  non-empty because `N ≥ 5 > e^{1.2}`.
- **On `(0.58, 0.60)`:** the dichotomy at `T*_{∞,P}` is `lem:strict`.

Nothing is claimed for `T > ½log N`, where `n = N` enters. One optional sharpening: `cor:void`'s deletion clause
could now read `T ≥ 0.60` (machine-verified) instead of `T > T₀(0)`. It is not required, since the hand-proved
version is weaker but true.

## 2. What was checked and found CLEAN (no edit)

- **`lem:monoT`.** Checked, including the `\lamP` clause: `Φ(log n) = 0` for new contacts, by continuity at `2T`.
- **`lem:roughEF`.** Dominations checked: `|Φ_η| ≤ e^{ε/2}` in the strip and `|η̂_ε| ≤ 1`. Prime terms with
  `e^{2T} ≤ n < e^{2T+2ε}` vanish in the limit.
- **`lem:testfam`, `thm:margin`, `cor:margin1`.** All re-derived:
  - `ϖ(iτ) = (τ²+¼)(τ²−γ₁²)`;
  - `ϖ(β+iγ) ≤ (1+10⁻²²)γ⁴` above `3·10¹²`;
  - `ε₈(1) = 0.00602`, `ε₉(8e/21) = 0.01565`, `0.5797`;
  - `2kx − 2k = −42T/e + 2θ²e/21T`;
  - final constant `3.9625·10⁹ ≤ 3.97·10⁹`;
  - `H_PT` ratio `2·10⁻⁷⁶` at `T = 1`.
- **`cor:margin2`.** Checked; the rough-test positivity sentence is present.
- **`lem:Ncount`** (`6.112` at `21`) and **`lem:zerosum`** (the boundary term is `≤ 0`).
- **`prop:finite`, `lem:cpos`, `thm:finmod`(ii),(iii), `prop:finsupp`.**
  - `|N_T| = ⌈e^{2T}⌉ − 2`.
  - `F_T = (−∂²+¼)G_T` gives `F̂_T = (τ²+¼)Tĝ(Tτ)`, and the Rayleigh quotient tends to `σ(0) = C₀ − A_S`.
- **`cor:void`.** Checked, including closure of `𝒞_zeros` under deletion for every member.
- **`prop:uniform`.** Checked.
- **`prop:band`.** `τ^lo = 60.5432` and `120.0865` re-derived.
- **`prop:align`.** Re-derived:
  - `τ_a = 23.3409`, `τ_b = 17.7446`, `τ_b′ = 34.4909`;
  - `y₀ = 0.43702`, `arccos y₀ = 1.1185`;
  - bracket constants `log 6/4 = 0.44794` and `0.36886`;
  - `(0.6390, 1.5650)`;
  - arc counts `⌊4.104⌋+2 = 6` and `⌊10.673⌋+2 = 12`;
  - the witnesses: comb `2.21553` against `m_up = 2.00493` at `45.64206`, and `2.9368` against `2.86013` at
    `108.72265`.
- **`rem:bandtable`.** The `(k,l)` pairs and ratios `1.185, 1.0535, 0.9364, 0.98654` are right; `8/5, 19/12`
  are convergents, and `5/3, 11/7` are intermediate fractions.
- **`def:Al`, `lem:Alband`, `lem:Onat`, `thm:Al`.**
  - `def:Al` is exactly `f_w ≥ 0` by `eq:fw`.
  - `lem:Onat`'s inverse transform on `0 < |u| < 2T` uses `ν_w = 0` there, per `eq:nuw`.
  - `thm:Al`(b) is `thm:Zexh`(i) plus `lem:Onat`.
- **`rem:Cheb`.** The identity `eq:Cheb` is right: `∫c_F e^{u/2} = A(F)B(F)`, and evenness.
- **`lem:strict`.** Correct, per item 4.
- **`lem:parity`, `thm:index`, `cor:Tarch`.** Every threshold deduction checked. The real/complex remark is
  present.
- **App. A.4.**
  - `lem:border`: the substitution `η = ξ + q(w,v₀)`, determinant `−1`.
  - `lem:multiband`: chord offset `M_aΔ²/8`. The `m''` summand `a(a²−3s)/(2(a²+s)³)` was re-derived; the
    majorant `a(a²−2s)/(2(a²+s)³)` is decreasing-then-increasing, with turning point `s = 5a²/4`.
  - `prop:haynsworth`: signs of `𝖱_{iξ}` and `𝖱_{ξξ}` re-derived, and they match `r8a_01_upper.py` L136–157.
  - The `P^⊥_{k₂}` box `ρ𝓜_ii` was verified via `‖M^{1/2}P^⊥M^{1/2}‖`.
  - `prop:negplane`, `lem:polround` (`2T³+2T⁴` dominates `(2T³+T⁴)/3`), `lem:zeroext`, `lem:rzero`.
  - `rem:signfix`: `2·6.4·9.2·10⁻³⁶/1.04 = 1.2·10⁻³⁴`.
- **Certificate files.** All eight `03-research/phase-155-row-d-flat-kernel-criterion/scripts/r8a/r8a_01_*_rerun.json` and `r8a_03_recheck.json` exist, and every
  margin in the two App. A.4 tables matches them to the printed digits:
  - upper: `0.015998, 0.047516, 0.041093, 0.185541, 0.144840, 0.420225, 0.298000, 0.161624`;
  - lower: `0.006627, 0.005124, 0.147170, 0.290056, 0.012368`;
  - `r8a_02_0p90_par1` is correctly out of range.
  - `c_* = Tτ_N = 16.0000` in every run; entry widths are `≤ 1.64·10⁻¹³`.
- **`main.log`.** 73 pp., 0 `^!` errors, 0 undefined or multiply-defined references or citations.
- **Labels.** No `\ref` to an undefined label. Every new label (`lem:monoT` … `rem:odd080`) has a row in one of
  the two label tables.
- **No sign for `ζ` beyond `log 2`.** New material that sits beyond `log 2` is the archimedean-only
  `thm:index`, the upper bound `thm:margin`, and the method constraints.
- **"first beyond"** does not occur.
- **Numbers consistent.** Every occurrence was grepped:
  - `0.58/0.60` (13 places) and `0.5958` (4);
  - `log2 ≤ T*_odd ≤ 0.81`;
  - `4·10⁹Te^{−15.449T}` (6);
  - `8.8577·10⁻⁵` (5), `8.86·10⁻⁵` (2);
  - `2.24883` (3) and `A = 2.248826`;
  - `T₀(0) = 0.74921` (re-computed: `0.749207`).
  The exception is `1.226/1.852` (R4-1).

---

## 3. Findings

**R4-1 — MAJOR (numerical, not load-bearing). L3180–3181, L3895, L4459: the crossings of `rem:margin` are wrong;
the script has a factor-`H` bug.** `03-research/phase-155-row-d-flat-kernel-criterion/scripts/r8d/r8d_margin_bound.py` L59–61 rewrites
`(k/T)^{2k}Σ_p(H) = (k/(TH))^{2k}·H⁸·(p/2π)[…]`. The correct identity is
`(k/T)^{2k}H^{1−p} = (k/(TH))^{2k}H^{9}`, because `1−p = 9−2k`. So every scripted `𝓑(T,k)` is 21 times too
small (by `3·10¹²` for the negligible `H_PT` term).

I recomputed with a direct `mpmath` evaluation of `eq:Bmargin` and `Lemma zerosum`. At `T = 1` the true
`min_k 𝓑` is `589.7`: the script gives `28.08`, and `cor:margin1`'s own closed form gives `781`. The true
crossings are:
- `𝓑 = 1` at **`T = 1.430`**, not `1.226`;
- `𝓑 = 8.8577·10⁻⁵` at **`T = 2.054`**, not `1.852`.

The theorem, `eq:Bmargin` and `cor:margin1` are unaffected: the hand derivation correctly carries `21⁹`. The
App. C ratio "five to eight orders" was computed against the buggy `𝓑`; against the true one it is 6.3 to 9.6
orders. The memo R155_055 §3.2 table and its "worst ratio `0.036`" are wrong for the same reason (true ratio at
`T = 1` is `0.755`), and R155_059 L138 "✓" missed it. This is a process note.
**Exact edits.**
- L3179–3182: "…The explicit right side of \eqref{eq:Bmargin}, minimised over $k$, exceeds $1$ for $T<1.430$ and
  falls below the value $8.8577\cdot10^{-5}$ of Theorem~\ref{thm:C} only at $T=2.054$ (numerical evaluation of
  the explicit expression, \path{03-research/phase-155-row-d-flat-kernel-criterion/scripts/r8d/r8d_margin_bound.py}); the theorem is an asymptotic statement…"
- L3895: "…the crossings $1.430$, $2.054$ of Rem.~\ref{rem:margin} are numerical evaluations of the explicit bound".
- L4459: "…Rayleigh quotient smaller than the proved bound $\mathcal B(T,k)$ by six to ten orders of magnitude over
  $\frac12\log3\le T\le1.5$…".
- Script, L59 and L61: `H^8` → `H^9` and `8*math.log(H)` → `9*math.log(H)`, then re-run, and check that the new
  crossings print `1.430`, `2.054`.

**R4-2 — MAJOR (gap in a PROVED equivalence; two-sentence repair). L1242–1249, the proof of `cor:RH`, (a)⇒(c).**
This proof is inherited by `thm:Al`(c) (L3523) and the reduction chain (L2931). It has two gaps: rough-test
positivity (item 2), and distinct zeros versus zeros with multiplicity (item 2(b)).
**Replace** the sentence from "(a)$\Rightarrow$(c): under RH, for real $F$," to the end of the proof by:
> (a)$\Rightarrow$(c): assume RH. For real $F$ in the form domain let $F_\varepsilon=F*\eta_\varepsilon$ be the
> mollification in the proof of Lemma~\ref{lem:roughEF}. By \cite[Thm.~9.4]{Paper45} and RH,
> $W_{T+\varepsilon}(F_\varepsilon)=\sum_\gamma|\Fh(\gamma)|^2|\widehat{\eta_\varepsilon}(\gamma)|^2$, and the
> archimedean, polar and prime steps of that proof, which use only hypothesis (a), give
> $W_{T+\varepsilon}(F_\varepsilon)\to W_T(F)$; since $\widehat{\eta_\varepsilon}\to1$ pointwise, Fatou's lemma gives
> $\sum_\gamma|\Fh(\gamma)|^2\le W_T(F)$ (so hypothesis (b) holds and, by Lemma~\ref{lem:roughEF}, with equality).
> The form $W_T$ is real, $W_T(u+iv)=W_T(u)+W_T(v)$ for real $u,v$, so its infimum on the unit sphere, which is
> attained (\cite[Thm.~3]{Bombieri2000}, or the compactness in the proof of Theorem~\ref{thm:O}), is attained at a
> real $F_\star$. If $W_T(F_\star)=0$ then $\Fh_\star(\gamma)=0$ at every ordinate $\gamma$. Under RH a zero at
> height $t$ has multiplicity $O(\log t/\log\log t)$ \cite[Thm.~14.13]{Titchmarsh}, so there are
> $\gg t\log\log t$ distinct ordinates in $(0,t]$, while the nonzero entire function $\Fh_\star$ of exponential
> type $T$ has $O(t)$ zeros in $|z|\le t$ by Jensen's formula. Hence $\lamW=W_T(F_\star)>0$, and
> Theorem~\ref{thm:Zexh}(i) gives $w$ with $\inf f_w>0$.

**Add to the bibliography:** `\bibitem{Titchmarsh} E.~C.~Titchmarsh, \emph{The Theory of the Riemann
Zeta-Function}, 2nd ed., revised by D.~R.~Heath-Brown, Oxford Univ.~Press, 1986.`

**R4-3 — MINOR (mathematical: endpoint). L2078 (`thm:SC`), L2360 (`prop:arch`(ii)).**
- L2078: "then the form is negative on $\PT$ for every $T>T_0(A)$, and nonpositive at $T=T_0(A)$, where…"
- L2360: "Hence both are nonpositive at $T=T_0(0)=0.74921$ and negative for $T>T_0(0)$ (at $T_0(0)$ itself, as for
  every $T\ge0.60$, $\laminf\le\laminfP<0$ by Corollary~\ref{cor:Tarch}), and $\laminfP(T)\downarrow C_0$ as…"
- (iv)'s bound `T*_{∞,P} ≤ 0.74921` is unaffected: a supremum is not moved by one endpoint.

**R4-4 — MINOR (mathematical: statement too strong). L660–667 and L681–685 (`prop:P`).**
- Replace the display and the sentence before it with: "For every $F\in L^2(\IT)$ in the form domain,
  $\frac1{2\pi}\int\gh0|\Fh|^2=\Rel\big(A(F)\overline{B(F)}\big)$ and hence
  \[\frac1{2\pi}\int\big(\sT+2\gh0\big)|\Fh|^2\,d\tau=W_T(F);\] if moreover $F$ is real and
  $\sum_\rho|\Phi_F(\rho)\Phi_F(1-\rho)|<\infty$ (in particular if $F\in C_c^\infty(\IT)$ is real), then
  $W_T(F)=\sum_\rho\Phi_F(\rho)\Phi_F(1-\rho)$ (Lemma~\ref{lem:roughEF} below)."
- In the proof, "The identification of $W_T$ with the zero sum is the explicit formula…" stays as is (it is the
  smooth case).
- L681–685: "\cite[Thm.~9.4]{Paper45} is stated for real $F\in C_c^\infty$. The first equality of
  Proposition~\ref{prop:P} holds on the whole form domain and is the only one the certificates use; wherever the
  zero sum is used for a rough test (Corollary~\ref{cor:RH}, Theorem~\ref{thm:margin}, Remark~\ref{rem:Cheb}),
  it enters through the following lemma."
- L141 (intro): "…for tests that are not smooth, under absolute convergence of the zero sum,
  Lemma~\ref{lem:roughEF})".

**R4-5 — MINOR (mathematical slip). L2786–2797 (`cor:H1`) and L3881.**
- The problem: "in particular for $T_2=\log2$" does not follow from "every $T_2<T^*_{\mathrm{odd}}$", because
  only `log 2 ≤ T*_odd` is known and no continuity of `λ_odd` is asserted. It is nevertheless true, by
  `thm:index`(i): `n_odd = 0` on `(0, log 2]`.
- A second point: `(H1)(T₂)` is defined only for `T₂ > T*_{∞,P}`.
- Replace the statement with: "$(\mathrm{H1})(T_2)$ holds for every $T_2\in(T^*_{\infty,\mathrm P},T^*_{\mathrm{odd}})$
  and for every $T_2\in(T^*_{\infty,\mathrm P},\log2]$, and fails for every $T_2>T^*_{\mathrm{odd}}$; the case
  $T_2=T^*_{\mathrm{odd}}>\log2$ is not decided. Hence the supremum of the admissible $T_2$ is
  $T^*_{\mathrm{odd}}\in[\log2,0.81]$."
- Add to the proof: "For $T_2\le\log2$ use instead Theorem~\ref{thm:index}(i): $n_{\mathrm{odd}}=0$ on $(0,\log2]$,
  and $n_{\mathrm{ev}}=1$ on $(T^*_{\mathrm{ev}},0.90]$ by Lemma~\ref{lem:strict} and (i)."
- L3881: "for every $T_2\in(T^*_{\infty,\mathrm P},\max(\log2,T^*_{\mathrm{odd}}))$ and at $T_2=\log2$".

**R4-6 — MINOR (exposition that is false as a reading). L3583–3588 (`rem:Cheb`).**
- The problem: "a prime-side proof that the margin tends to $0$ would have to bound $\int e^{-u/2}\cF\,dr_\Lambda$
  by $o(\|F\|^2)$" is not what `eq:Cheb` says. For `𝔞_T(F) = o(‖F‖²)` the last term must *equal*
  `C₀‖F‖² + Lev(c_F) + 2∫c_F e^{−u/2}` to within `o(‖F‖²)`; it need not be small.
- Replace from "Reading, not a theorem:" with: "Reading, not a theorem: a zero-free-region bound controls the last
  term only up to an error that grows with $T$, whereas any $F\in\PT$ with $\mathfrak a_T(F)=o(\|F\|^2)$
  (Corollary~\ref{cor:margin2}) needs $2\int e^{-u/2}\cF\,dr_\Lambda$ to equal
  $C_0\|F\|^2+\Lev(\cF)+2\int_0^{2T}\cF e^{-u/2}du$ up to $o(\|F\|^2)$; by Lemma~\ref{lem:roughEF} that precision
  is a statement about $\sum_\rho\Phi_F(\rho)\Phi_F(1-\rho)$."

**R4-7 — MINOR (overclaim in the introduction). L263.**
- The problem: "so no classical prime-side hypothesis decides any window" is stronger than `cor:void`. `cor:void`
  covers windows `T > ½log2` for `𝒞_PNT` and `𝒞_zeros`, and `T > T₀(0)` for `𝒞_BT`. For `T ≤ ½log2` the comb is
  empty and `RD_T` holds for every `a`.
- Replace with: "so no classical prime-side hypothesis decides any window $T>\frac12\log2$ (any window
  $T>0.74921$ for upper-bound sieve hypotheses)".

**R4-8 — MINOR (global rule: machine-verified claims without a named certificate file). L3921–3925, L3637, L3695.**
- The problem: `thm:N`, `thm:Np`, `thm:w11`, `thm:nest` (and `thm:Bbeta`'s constants) say only "archived with
  the accompanying scripts".
- Insert after L3925: "The enclosures of Theorem~\ref{thm:N} are
  \path{03-research/phase-155-row-d-flat-kernel-criterion/scripts/r2_a_enclosure_M<M>.json},
  $M\in\{3,5,6,7,8\}$, written by \texttt{r2\_a\_enclosure.py}; the $\beta$-box of Theorem~\ref{thm:Bbeta} is
  \path{r2_c_beta_bound.json} there; the certificates of Theorems~\ref{thm:w11} and \ref{thm:nest} are
  \path{03-research/phase-155-row-d-flat-kernel-criterion/scripts/r4a/r4a_02_<T>*.json} ($T\in\{\log2,0.62,0.65\}$) with the archived vectors of
  \path{03-research/phase-155-row-d-flat-kernel-criterion/scripts/r4a/r4a_01.json}, written by \texttt{r4a\_02\_nested\_enclosure.py}; those of
  Theorem~\ref{thm:Np} are [editor: insert path]."
- The editor must confirm each mapping, especially `thm:Np` and `thm:w11`: the `r2_b_*.json` files I found are
  `T = 0.58` ceiling measurements, not obviously `thm:Np`.
- Also name the `rem:margin` script, as in R4-1.

**R4-9 — MINOR (forward dependence). L2473–2474 (`lem:strict`) and L2618–2621 (after `lem:parity`).** `lem:strict`'s attainment step,
and the real/complex paragraph after `lem:parity` both rest on "the real splitting in the proof of
Proposition~\ref{prop:finite}(ii)", which is 700 lines later. There is no circularity, but the argument is one
line. Replace, at L2473–2474: "Since the symbol is real and even, $\Gamma_T(u+iv)=\Gamma_T(u)+\Gamma_T(v)$ for real
$u,v$, and $u+iv\in\PT^{\mathrm{par}}$ if and only if $u,v\in\PT^{\mathrm{par}}$ ($A,B$ are real on real
functions), so the minimiser may be taken real." At L2618–2621, point to `lem:strict` instead.
`cor:Tarch` is likewise proved by the later `thm:index`. That is acceptable because it is explicitly pointed,
but consider moving `cor:Tarch` after `thm:index`.

**R4-10 — MINOR (wording in a proved remark). L3178 (`rem:margin`).** "it uses the positions of the zeros only up
to the gap edge $21$ and the counting bound beyond" omits (X19′). The fact that zeros lie on the line up to
`3·10¹²` is used in step (4); without it every zero above `21` carries `e^T`. Replace with: "it uses the positions
of the zeros up to the gap edge $21$, their lying on the line up to $3\cdot10^{12}$, and the counting bound beyond".
In the same remark, write "it gives, whenever $\lamA>0$, $-\log\lamA\ge\dots$".

**R4-11 — COSMETIC (App. A.4 numbers vs files). L4162, L3936.**
- "$\Lambda_{22}(16)\le7.2150\cdot10^{-6}$": the files give `7.21502–7.21502` (`LamK_hi = 7.2150159…·10⁻⁶` to
  `7.2150186…·10⁻⁶`). Write `7.2151\cdot10^{-6}`.
- "$\rho\le4.0\cdot10^{-20}$": the files give `4.0105·10⁻²⁰`. Write `4.02\cdot10^{-20}`.
- The runtime of `r8a_02_lower.py`, "$10$--$28$\,s per window": the log2 run is `55.4 s` in `03-research/phase-155-row-d-flat-kernel-criterion/scripts/r8a/README.md`.
  Write "$10$--$56$\,s".
- `c_*`: "c_*≈16" can read "c_*=16" (to six decimals of `τ_N`).

**R4-12 — COSMETIC (optional, from item 4). L2494–2496 (`lem:strict`).** Replace "and $c_0=A(F^*)=0$ because
$F^*\in\mathcal P_{T'}$. With $u=e^{2x}$, … all moments of $f$ vanish, so $f=0$ by Weierstrass" with: "(the value
$c_0=\beta/2$ is not needed). With $u=e^{2x}$, $c_k=\int f(u)u^k\,du$ for
$f(u)=\frac12F^*(\frac12\log u)u^{-3/4}\in L^1[e^{-2T'},e^{2T'}]$, so all moments of $uf(u)$ vanish and $uf=0$ by
Weierstrass". Optionally add after the proof: "The same argument, with the pole term of $\Ainf$ in place of the
two multipliers, shows that $\laminf$ and the bottom of $\Gamma_T$ on $L^2(\IT)$ are strictly decreasing as well."

**R4-13 — COSMETIC (notation). L2819, L3432.** `R_T` (restriction) is used at L2819 and in `prop:negtrace` with no
definition before L3748, and `R` is the reflection of §9.1. At L2819 write "$M_\pm=R_Tm_\pm(D)R_T\ge0$ on
$L^2(\IT)$, $R_T$ the restriction to $\IT$ of the extension by zero,". Likewise `𝖱`: the matrix of App. A.4 is
already distinguished by font, so leave it.

**R4-14 — COSMETIC (hardcoded subsection number). L3462, L3821, L3905.** "\S\ref{sec:path}.2" appears three times
(R3's "no hardcoded numbers" check predates round 8). Add `\label{subsec:where}` to L2969 and write
`\S\ref{subsec:where}`.

**R4-15 — COSMETIC.**
- L706 (`lem:roughEF`): "(Lemma~\ref{lem:mbounds}(i),(ii); $m\le0$ for $|\tau|\le\tau_0$)", since the bound
  $|m|\le|C_0|+\log(1+|\tau|)$ is not stated there as such.
- Label table row for `prop:finite` (L3898): add "; the clause $T\ge0.60$ of (iii) \textsc{machine-verified}
  (Cor.~\ref{cor:Tarch})".
- Macros `\dd`, `\AT`: unused (inherited); delete.
- Abstract L96–98 and intro L256: "computed exactly for $T\le0.90$ up to two thresholds" is fair but compressed.
  Suggested: "computed exactly for $T\le0.90$ outside the two threshold brackets $[0.58,0.60]$ and $[\log2,0.81]$".

## 4. Summary table

| # | line(s) | severity | type | edit |
|---|---|---|---|---|
| R4-1 | 3180–3181, 3895, 4459; `r8d_margin_bound.py` L59–61 | **MAJOR** | numerical | crossings `1.226/1.852` → `1.430/2.054`; "five to eight" → "six to ten"; fix `H⁸ → H⁹` and re-run |
| R4-2 | 1242–1249; bibliography | **MAJOR** | mathematical | `cor:RH` (a)⇒(c): Fatou for rough `F⋆`, real minimiser, distinct zeros via Titchmarsh 14.13 |
| R4-3 | 2078, 2360 | MINOR | mathematical | endpoint `T₀`: negative for `T > T₀`, `≤ 0` at `T₀` |
| R4-4 | 660–667, 681–685, 141 | MINOR | mathematical | `prop:P`: zero-sum clause only for real `F` with absolute convergence |
| R4-5 | 2786–2797, 3881 | MINOR | mathematical | `cor:H1`: `T₂ = log 2` via `thm:index`(i); domain `T₂ > T*_{∞,P}` |
| R4-6 | 3583–3588 | MINOR | exposition (false reading) | `rem:Cheb`: "`o(‖F‖²)` bound" → "match to `o(‖F‖²)`" |
| R4-7 | 263 | MINOR | overclaim | "any window" → "any window `T > ½log2`" (`0.74921` for sieve) |
| R4-8 | 3921–3925 | MINOR | reproducibility | name certificate files of `thm:N/Np/w11/nest/Bbeta` and the margin script |
| R4-9 | 2473, 2618 | MINOR | exposition | inline the real splitting; no forward reference to `prop:finite` |
| R4-10 | 3176–3178 | MINOR | exposition | `rem:margin` also uses (X19′); "whenever `\lamA > 0`" |
| R4-11 | 4162, 3936 | COSMETIC | numerical | `7.2151·10⁻⁶`, `4.02·10⁻²⁰`, `10–56 s`, `c_* = 16` |
| R4-12 | 2494–2496 | COSMETIC | mathematical (optional) | `c₀` not needed; strictness also for `\laminf` |
| R4-13 | 2819 | COSMETIC | notation | define `R_T` |
| R4-14 | 3462, 3821, 3905 | COSMETIC | cross-reference | `\S\ref{sec:path}.2` → `\S\ref{subsec:where}` |
| R4-15 | 706, 3898, preamble, 96–98 | COSMETIC | exposition | `lem:mbounds` pointer; label row; unused macros; abstract wording |

**Mathematical findings:** R4-1 (numbers), R4-2, R4-3, R4-4, R4-5, and R4-12 (optional). Everything else is
exposition, reproducibility or notation.
**Rulings on the flagged items:**
1. Endpoint: fix to strict (R4-3).
2. `cor:RH`: not adequate; text supplied (R4-2).
3. `prop:P` sentence: insufficient, restrict the statement (R4-4).
4. `lem:strict` dispute: **editor right, memo wrong**, and even `c₀ = 0` is unnecessary.
5. `prop:negtrace`(v): correct.
6. `thm:finmod`(i): correct, including at `½log N`.

Row-D label unchanged; endpoint of record unchanged; no sign for `ζ` claimed beyond `log 2`.
