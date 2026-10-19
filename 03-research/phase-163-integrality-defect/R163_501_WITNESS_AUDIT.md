# R163_501 — Audit and repair of the real-rooted first-contact witness

*Audit of R160_X_C1 Theorems B, R, FC (and G, which R163_401 §2.4(iii) uses), line by line against
Paper 47 `main.tex`: `eq:symbol`, `eq:form`, `eq:W`, `\PT`, `lem:monoT`, `lem:contT`, `lem:roughEF`, `lem:contA`,
`lem:firstcontact`, proof of `thm:O` (compactness). Pure mathematics, no numerics. No . No file other than
this one was written. No label of record moves except as recommended in §6.*

## 0. Final status

| statement | status | what changed |
|---|---|---|
| Thm B (Blaschke invariance), [compl] and [prim] | **PROVED** | nothing; one remark on conventions (§1) |
| Lemma S (span) | **PROVED** | — |
| Thm R (a),(b),(c),(e) | **PROVED** | (b) needs "real/imag parts of `E_C` lie in `E_C`"; justified in §2.1 (the §1.4 justification in X_C1 is wrong but its conclusion is true) |
| Thm R (d) | **PROVED AFTER REPAIR** | as stated it covers only the real space `E`; FC(ii) applies it to `E_c = ker W` (complex). Repaired to all of `E_C` (§2.3) |
| Cor R1, R2 | **PROVED** (R2), implication R1 **PROVED** | — |
| FC0(i) (RH ⇒ `ker W_T = 0`) | **PROVED AFTER REPAIR** | "≍R log R zeros" must be "≫R log R *distinct* ordinates": cite positive proportion of simple zeros (Levinson/Conrey), not Riemann–von Mangoldt (§3.1) |
| FC0(ii) (existence of `T_c`, `λ^W_{T_c}=0` attained, `W_{T_c} ≥ 0`, `dim E_c<∞`) | **PROVED** | — |
| FC(i) at `T_c` (full support, type, density) | **PROVED** | "half-line" → "half-plane" unless real-rooted |
| FC(ii) at `T_c` (real-rooted witness in each nonzero parity part) | **PROVED** | second sentence ("one parity ⇒ all of `E_c` real-rooted") PROVED AFTER REPAIR via R(d) repaired |
| FC(iii) at the primitive contact `T_*` | **real-rootedness PROVED; full-support claim UNPROVED as stated (fails if `λ^A` vanishes on an interval `[T_1,T_*]`, which is not excluded; repaired at `T_♭`; corrected per R163_590 D10)** | `T_* = inf{λ^A<0}` (Paper 47 `lem:firstcontact`) only gives `λ^A ≥ 0` below `T_*`. Replacement: work at `T_♭ := sup{T: λ^A_T>0}` (§3.4) |
| Thm G (a)–(e) | **PROVED** with weights `w_x = d_x/|F̂'(x)|²` | R163_401 §2.4(iii) writes `F̂'(x)²`: **wrong for odd `F`** (negative). Must use `|F̂'(x)|²` (§4) |
| R163_401 Prop 4.0 (⇒) | **PROVED** (modulo the cited record inputs listed in §5) | relabel from "PROVED-CITED, unaudited" to PROVED; it uses only FC0(ii) + R(c) at `T_c` |

**Bottom line.** The existence of a nonzero real, parity-definite, real-rooted `F ∈ ker W_{T_c}` with
`W_{T_c} ≥ 0`, `conv supp F = [−T_c,T_c]`, under ¬RH, is **fully proved**. Inputs from outside this audit:
Weil/P45 Thm 11.3 (¬RH ⇒ some `λ^W_T<0`), `lem:monoT`, `lem:contT`, compactness of sublevel sets (`thm:O` proof),
and strict positivity on some initial range (`λ^W ≥ 10^{-18}` on `(0,½log5]`, Paper 47 §`sec:log5`; or
`λ^W>0` on `T≤0.005`, R157_004 Lemma E). Strictness is needed for the full-support claim FC(i), not for existence.

---

## 1. Theorem B — PROVED

Checked against `eq:form`, `eq:W` for complex `F ∈ L²(I_T)`. With `F̂(z)=∫F e^{izt}`, `F̂(−i/2)=A(F)`,
`F̂(i/2)=B(F)`. The Hermitian form of `eq:W` is
`W_T(F,G) = 𝔞_T(F,G) + A(F)\overline{B(G)} + B(F)\overline{A(G)}`, whose diagonal is `𝔞_T(F)+2Re(A\bar B)`. So X_C1
§1.2 with `Π={±i/2}`, `c=1` is exactly `eq:W`.

Line checks.
1. `|z−w̄| ≤ |z−w| + 2|Im w| ≤ 3|z−w|` on `|z−w| ≥ |Im w|`; maximum principle on the disc. Hence
   `|Ĝ(z)| ≤ C' e^{T|Im z|}`, `Ĝ|_R ∈ L²`, Paley–Wiener gives `G ∈ L²(I_T)`, Plancherel gives `‖G‖=‖F‖`, and
   `|Ĝ|=|F̂|` on `R` gives the form-domain integral and the `𝔞_T` value. ✓
2. Polar: `b_w(i/2)\overline{b_w(−i/2)} = \frac{i/2−w̄}{i/2−w}\cdot\frac{i/2−w}{i/2−w̄} = 1`, so
   `B(G)\overline{A(G)} = B(F)\overline{A(F)}`, and likewise the conjugate term. ✓
3. `w = ±i/2`: e.g. `w=i/2`, `B(F)=0`; then `A(G)=Ĝ(−i/2)=b_w(w̄)F̂(w̄)=0`; both polar terms vanish before and after. ✓
4. Primitive case: only free zeros are moved, so `ord_{±i/2}Ĝ ≥ 1` remains. ✓ (Real parity of `F` gives equal
   orders at `±i/2`, used later in R(b).)

No gap. Remark: R163_490 fix 3 is correct that B does not by itself make zeros real; that is R's job.

## 2. Theorem R — PROVED, (d) PROVED AFTER REPAIR

**Admissibility for ζ (checked).** `𝔞_T` is closed and semibounded with form norm equivalent to
`‖F‖²+‖F‖_Q²` (proof of `lem:contT`: `‖F‖_Q² ≤ W_T(F)+C'‖F‖²`; the comb is bounded by `𝖠_T‖F‖²`; `A,B` are bounded
functionals, `|A| ≤ ‖e^{t/2}‖_{L²(I_T)}‖F‖`). The domain is closed (if `F_n` is Cauchy in form norm, `F̂_n → g` in
`L²(log(2+|τ|)dτ)` and `F_n→F` in `L²`, so `g=F̂`). Compact embedding: bounded form norm ⇒ uniform tail control
`∫_{|τ|>R}|F̂|² ≤ C/log R`, and `F ↦ F̂1_{[−R,R]}` is Hilbert–Schmidt (proof of `thm:O`). So `W_T` on `𝒟_T` and
`𝔞_T` on `P_T∩𝒟_T` (closed subspace, finite codimension) have compact resolvent; bottom eigenspaces are
finite-dimensional and attained. Variational characterisation: `F` (nonzero, in the domain) is in the bottom
eigenspace iff `W(F)=λ‖F‖²`. ✓

### 2.1 Reality and parity (repairing X_C1 §1.4)
X_C1 §1.4 justifies `W(F_1+iF_2)=W(F_1)+W(F_2)` by "the ν cross term is odd in τ". That reason is not right as
stated (the cross term `∫σ Re(...)`-type expression is not odd in general). Correct reason: the form is real,
`W(\bar F,\bar G)=\overline{W(F,G)}` (since `σ_T` is even, `\widehat{\bar F}(τ)=\overline{F̂(−τ)}`, and
`A(\bar F)=\overline{A(F)}`, `B(\bar F)=\overline{B(F)}`). Hence `W(F_1,F_2)∈R` for real `F_1,F_2`, and the cross
term `2 Im W(F_1,F_2)` is `0`. In any case R only needs: **`E_C` is closed under conjugation** (a minimiser's
conjugate has the same norm and value) and under `J` (σ even, `A∘J=B`). So `E_C = E⊗C`, `E` = real elements,
`E = E^{ev}⊕E^{odd}`. ✓

### 2.2 (a), (b), (c), (e), Lemma S
- Lemma S: `V_k = (z−z_k)V_{k−1}+(z−\bar z_k)V_{k−1}`; the difference gives `(\bar z_k−z_k)Poly_{≤k−1}`; then
  `z·Poly_{≤k−1}`. ✓
- (a): order count `ord_{z_j}G_{S'} ≥ ord_{z_j}F̂ − #\{i∈S': z_i=z_j\} ≥ 1` (numerator factors only raise the order).
  Each `M_{z_j}` preserves norm and `W` (Thm B), so maps bottom eigenvectors to bottom eigenvectors. `G_S=F̂P_S/Q`.
  Injectivity of `P ↦ F̂P/Q`. ✓ Finiteness of `k` from `dim E_C<∞`. ✓
- (b): `F` real even ⇒ `F̂^#=F̂`, `F̂(−z)=F̂(z)`; non-real zero multiset invariant under `z↦−z, z↦\bar z`, with no
  fixed points ⇒ `k` even, `Q` even with real coefficients. Real `P`: `(F̂P/Q)^#=F̂P/Q` ⇒ `G(t)=\overline{G(−t)}`.
  Even `P` ⇒ `G` real even; odd `P` ⇒ `G=iG_r`, `G_r` real odd, and `G_r=−iG ∈ E_C` real ⇒ `G_r∈E^{odd}`. Real
  dimensions `k/2+1`, `k/2`. Odd `F`: `F̂^#=−F̂`, parities exchange (checked: even `P` ⇒ real odd; odd `P` ⇒
  imaginary even). ✓ Primitive: free multiset is still `±`, conj-symmetric (equal orders at `±i/2`). ✓
- (c): `P=∏_{i≤k/2}(z²−t_i²)`, real, even, degree `k`; `Q` removes **all** non-real (free) zeros; the result lies
  in the same parity part as `F` and is nonzero. ✓
- (e): `k+1 ≤ 1`. ✓

### 2.3 (d) — PROVED AFTER REPAIR
As written, (d) concludes real-rootedness for elements of the **real** space `E`. FC(ii) applies it to
`E_c = ker W_{T_c}`, a complex space, whose complex elements `F_1+iF_2` are not covered (a combination of two
real-rooted functions with a complex coefficient generally has non-real zeros). Repaired statement and proof:

**R(d′).** If `E^{odd}=0` (resp. `E^{ev}=0`), every nonzero `F ∈ E_C` (complex) is real-rooted (resp. primitively).

*Proof.* `F ∈ E_C` is even. Suppose `F̂(w)=0`, `w∉R` (free, in the [prim] case). By Thm B, `G:=M_wF ∈ E_C`. Since
`E_C` is `J`-invariant, the odd part of `G` lies in `E_C^{odd}=E^{odd}⊗C=0`. But
`Ĝ(z)−Ĝ(−z) = F̂(z)[b_w(z)−b_w(−z)] = F̂(z)\cdot\frac{2z(w−\bar w)}{z²−w²}`
(using `F̂(−z)=F̂(z)`; entire because `F̂(±w)=0`), which is `≢0` since `w≠\bar w` and `F̂≢0`. Contradiction. The
odd case is identical. ∎

## 3. FC0 and FC

### 3.1 FC0(i) — PROVED AFTER REPAIR
Steps checked: Weil positivity transferred to the form domain via `F_ε=F*η_ε` and the prime-side convergence of
`lem:roughEF` (archimedean by dominated convergence, comb terms with `c_F(log n)=0` for `log n ≥ 2T`, polar terms);
complex `F` reduced to `Re F, Im F` (the cross terms cancel in the zero sum because ordinates come in pairs `±γ` and
`F̂_j(−γ)=\overline{F̂_j(γ)}`). Fatou gives `F̂(γ)=0` at every ordinate.
**Gap:** this gives vanishing at *distinct* ordinates, without multiplicity. Riemann–von Mangoldt counts with
multiplicity; dividing by the max multiplicity `O(log R)` only gives `≫R` distinct points, which does **not** beat
Jensen's `O(R)`. **Repair:** cite a positive proportion of simple zeros (Levinson 1974 / Conrey 1989, unconditional;
or Montgomery under RH), giving `≫R log R` distinct ordinates in `(0,R)`. Then `F=0`. The same repair applies to
R163_401 Prop 4.0 (⇐) and §4.1 (R163_490 noted it for §4.1 only).

### 3.2 FC0(ii) — PROVED
`T_c:=sup\{λ^W>0\}` (= R163_401's `inf\{λ^W≤0\}` by `lem:monoT`). `T_c ≤ T_0<∞` (P45 Thm 11.3). `λ^W_{T_c}≥0` from
the left and `≤0` from the right by `lem:contT` ⇒ `=0`; attained (compact resolvent); `W_{T_c}≥0`; `E_c` nonzero,
finite-dimensional. Lower bound: X_C1 uses `0.005` (R157_004 Lemma E); R163_401 uses `λ^W ≥ 10^{-18}` on
`(0,½log5]` + continuity ⇒ `T_c>½log5`. Both valid as citations.

### 3.3 FC(i), FC(ii) at `T_c` — PROVED
(i) Translation `F ↦ F(·+c)`: `|F̂|` on `R` unchanged, `A ↦ e^{−c/2}A`, `B ↦ e^{c/2}B`, so `A\bar B` unchanged;
the comb at window `T_c` and at the smaller window `T'` agree by zero extension (`lem:monoT`). A nonzero kernel
element with `b−a<2T_c` would give `W_{T'}=0` at `T'<T_c`, contradicting `λ^W_{T'}>0`. ✓ Type and indicator:
Paley–Wiener + Titchmarsh support theorem; density `T_c/π` by Cartwright–Levinson (`F̂∈L²(R)` ⇒ Cartwright class).
Wording: for a non-real-rooted element the density statement is per right/left half-plane; for the witness, per
half-line. (ii) R(c) per parity; the second sentence by R(d′). ✓

### 3.4 FC(iii) at the primitive contact — PARTLY FALSE; replacement
With Paper 47's `T_*=inf\{λ^A<0\}` (`lem:firstcontact`) one only knows `λ^A_T ≥ 0` for `T<T_*`. If `λ^A` vanishes
on an interval `[T_1,T_*]`, a kernel vector at `T_1`, zero-extended, lies in `ker H_{T_*}` with support
`[−T_1,T_1]`: the full-support claim fails for that element. It is not excluded by anything in the record.
- **True at `T_*`:** each nonzero parity part of `ker H_{T_*}` contains a primitively real-rooted element; one parity
  ⇒ all of `ker H_{T_*}` primitively real-rooted (R(c), R(d′) in the [prim] case; `𝔞_T|P_T` admissible). ✓
- **Replacement for full support:** put `T_♭ := sup\{T: λ^A_T>0\}`. Since `λ^A ≥ λ^W >0` on `(0,½log5]`,
  `T_♭ ≥ ½log5`; `T_♭ ≤ T_*`; `lem:contA` gives `λ^A_{T_♭}=0` attained, `H_{T_♭}≥0`. At `T_♭` every nonzero kernel
  element has convex support `[−T_♭,T_♭]` (translation preserves `P_T`, since moments only rescale), and FC(ii)
  holds in [prim] form. Also `T_c ≤ T_♭`. R163_401 does not use the primitive contact (§2.5 "not used"), so nothing
  there breaks.

## 4. Theorem G — PROVED (with the correct normalisation)
(a) `Ĥ_x=F̂/(z−x) ∈ PW_{T_c}`, form domain; `W(F,·)=0` on `𝒟` since `F` is in the kernel of a nonnegative form
(Cauchy–Schwarz). (b) partial fractions; the splitting is legitimate since `|σ||Ĥ_x||F̂| ≤ |σ|(|Ĥ_x|²+|F̂|²)/2`.
(c) independence of `1, 1/(z−x)`. (d) at simple zeros `c_x=Ĝ(x)/F̂'(x)`, hence
`W(G)=Σ_x w_x|Ĝ(x)|²` with **`w_x=d_x/|F̂'(x)|² ≥ 0`**. For odd real `F`, `F̂` is imaginary on `R`, `F̂'(x)²<0`, so
R163_401 §2.4(iii)'s `W(H_x)/F̂'(x)²` is `≤0` — **error, must be `|F̂'(x)|²`** (confirms R163_490 fix 4, and the
same correction is needed in §2.4(iii) itself, not only §4.4). (e) polar part
`A\bar B/(−i/2−x)+B\bar A/(i/2−x) = −2ABx/(x²+¼)` for real `A,B`; the integral converges at `x` since `F̂(x)=0`. ✓

## 5. What R163_401 may use (exact)
Prop 4.0 (⇒) needs exactly: under ¬RH there is `T_c>½log5` and a nonzero real, parity-definite, real-rooted
`F∈𝒟_{T_c}` with `W_{T_c}≥0` on `𝒟_{T_c}` and `W_{T_c}(F)=0`. This is FC0(ii) + R(c) at `T_c`, both PROVED above.
Additionally available: `conv supp F=[−T_c,T_c]`, zero density `T_c/π` (FC(i)), Gauss nodes with
`w_x=d_x/|F̂'(x)|²` (G). Cited inputs not re-audited here: P45 Thm 11.3, the Paper 47 `½log5` certificate,
Cartwright–Levinson, Paley–Wiener–Titchmarsh, Levinson/Conrey simple-zero proportion. `lem:monoT`, `lem:contT`, the
compactness in `thm:O` were read and checked.

## 6. Recommended record edits (not performed)
1. R163_401 §2.4: "PROVED-CITED (not re-audited)" → "PROVED (audited R163_501)"; in (iii) replace `F̂'(x)²` by
   `|F̂'(x)|²`.
2. R163_401 Prop 4.0 (⇐) and §4.1: cite positive proportion of **simple** zeros for the distinct-ordinate count.
3. R160_X_C1: R(d) → R(d′) (complex kernel); §1.4 reason replaced by reality of the form; FC(iii) full support only at
   `T_♭`; FC0(i) simple-zero citation; "half-line" → "half-plane" for non-real-rooted elements.
4. No change to row D: the witness is a structure statement about a hypothetical object; CL remains ⟺ RH.
