# R155.049 — The correct lattice-sampling theorem for flat-top certificates

*[amended per R155_050]*

*Phase 155. Executes `TEX_HOSTILE_REVIEW_R2` Finding 1 (FATAL on `thm:AL`,
`main.tex:2930–2959`). Inherits Paper 47 `def:PD` (§3), `def:W`/`eq:nuw`, `thm:Z`, `thm:Dtail` (§7),
`lem:F1`, `lem:mbounds`, `lem:gbounds`, `prop:weak`, `prop:TK`, and `R155_033 §2`, `R155_037 §1`.
`main.tex` is NOT touched; §4 below is the exact replacement text. Scripts: `scripts/r49/` (one
10-second `DIAGNOSTIC` check of a proved constant).*

**No sign for `ζ` is claimed. Endpoint of record unchanged (`λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵`).**

---

## §0 Verdict in one paragraph

`thm:AL`/`cor:ALdef` as printed are **RETRACTED**: the density of the a.c. part of `ν_w` is
`½(1−w)K + 2w cosh(u/2)`, not `(1−w)K`, and that density has a **jump of size `2 cosh T` at the
window edge `u = 2T⁺`** (`w(2T) = 1`), so its even extension is not `C^{r−1}` and the `O(M^{−r})`
Poisson argument does not apply. A correct theorem **does** hold, but at a different rate:
sampling a flat-top certificate on the lattice `2T·ℤ/M` costs **exactly `Θ(1/M)`**, with the sharp
constant `(4/π)·2T·cosh T` for the endpoint-corrected (trapezoidal) sampling. The `M^{−1}` is not an
artefact of the estimate and no smoothness of `w` removes it: it is the alias of the **polar block**
`2 cosh(u/2)·1_{|u|<2T}`, whose transform is `2ĝ₀` and which has a jump at `±2T` independent of `w`.
The archimedean-only Theorem AL of `R155_033 §2.3` is **unaffected and stands** (there `G = (1−w)K`
does vanish at `2T`). Consequence: the reading "the lattice is never the deficit" is **WITHDRAWN**.
*[amended per R155_050]* The edge rate `Θ(M^{−1})` is a statement about the full
programme; the measured `0.28·M^{−1.17}` of `R155_033 §2.5` is the **archimedean** `Ceil_∞` deficit,
a different setting (`β = 0`, no polar block, no jump), and the two must not be compared or claimed
coherent.

---

## §1 What exactly is wrong with `thm:AL` as printed

Three defects, all confirmed:

1. **Hypothesis.** "`w ≡ 1` on `[U,∞)`" contradicts `def:W` (`|w| ≤ Ce^{−(½+δ)|u|}`) and makes `ν_w`
 infinite. In the archimedean programme `(D_∞)` of `R155_033 §2.1` the same clause is **correct**
 (there `ν_w = (1−w)K·1_{u≥2T}du`, and `w → 1` at `U⁻` is exactly what makes `G` compactly
 supported and `G_e ∈ C^{r−1}`), so `R155_037`'s clause is right *in its own programme*; what is
 wrong is transplanting it into `W_T`. In `W_T` the correct clause is `w ≡ 0` near `∞` with
 `C^{r−1}` contact with `0` at `U`.
2. **Density.** By `eq:nuw` the a.c. density is `½(1−w)K + 2w cosh(u/2)`; the printed `G = (1−w)K`
 drops both the `½` and the whole `cosh` block.
3. **Consequence.** The dropped block is exactly the one `thm:Dtail` must regroup with `2ĝ₀`,
 because it is the one carrying the edge jump; and the prime atoms
 `−Σ_{n∉𝒩_T}(v_n/2)w(log n)δ_{±log n}` of `eq:nuw` are neither sampled nor bounded.

---

## §2 The correct theorem

Throughout: `T > 0`, `M ∈ ℕ`, `d = 2T/M`, `P = 2π/d = πM/T`; note `2T = Md` **is a lattice point**.

**Definition (admissible sampling weight).** `w ∈ 𝒲_T^{(r)}` iff `w ∈ 𝒲_T` (`def:W`), `w` is even,
`w ≡ 1` on `[−2T,2T]`, `w ∈ C^{r−1}(ℝ)` with `w^{(r−1)}` locally absolutely continuous and
`w^{(r)} ∈ BV`, `supp w ⊆ [−U,U]` with
`C^{r−1}` contact with `0` at `±U`, `r ≥ 2`, **and `w(log n) = 0` for every `n` with `log n > 2T`**
(*comb-vanishing*; the set `{log n} ∩ (2T,U]` is finite, so this is a finite set of interpolation
conditions and `𝒲_T^{(r)} ≠ ∅`). Put, as in `thm:Dtail`,
`W(u) = w(|u|) cosh(u/2)` (globally `C^{r−1}`, since `W = cosh(u/2)` on the window),
`R(u) = ½(1−w(u))K(u)·1_{|u|≥2T}` (even; `R` and its first `r−1` derivatives vanish at `±2T`, so
`R ∈ C^{r−1}(ℝ)`, `R^{(r)} ∈ L¹`), and `G = R + 2W·1_{|u|≥2T}`, the even a.c. density of `ν_w`.
Set `V_r = ‖R^{(r)}‖_{L¹} + 2‖W^{(r)}‖_{L¹}`, `V_0 = ‖G‖_{L¹}`.

**Theorem AL′ (lattice sampling of a flat-top certificate). `PROVED`.**
Let `w ∈ 𝒲_T^{(r)}`, `c_w = inf_ℝ f_w` with `f_w = σ_T + ν̂_w + 2ĝ₀` (`def:W`). Define
```
ν_lat = Σ_{|j| ≥ M} d·κ_j·G(jd)·δ_{jd}, κ_M = κ_{−M} = ½, κ_j = 1 otherwise,
```
a **signed** even measure supported in `{|u| ≥ 2T}` with **countably many** atoms (`G(jd) ≠ 0` for
every large `j`, since `w = 0` and `G = ½K > 0` there) but **finite total variation**
`‖ν_lat‖_TV = d Σ|G(jd)| < ∞` (`G ∈ L¹ ∩ BV` on `[2T,∞)`; that is all Step 4 below uses). No sign or
bound `0 ≤ w ≤ 1` is assumed — `(D)` allows signed `ν` (`def:PD`) and `G` is genuinely signed. Then
`(ν_lat, β = (2,0))` is feasible for `(D)` and
its value `c_lat(M) = inf_ℝ [σ_T + ν̂_lat + 2ĝ₀]` satisfies
```
c_lat(M) ≥ min{ c_w − E_edge(M) − ε_r(M), m(P/2) − 𝖠_T − ‖ν_lat‖_TV − 2ĝ₀(0) },
E_edge(M) = 8cosh T/P + 2π² sinh T/P² + 16.9 cosh T/P³ = (4/π) cosh T·d + (sinh T/2) d² + O(d³),
ε_r(M) = 2(1 − 2^{−r}) ζ(r) V_r (P/2)^{−r} = O_r(V_r M^{−r}).
```
In particular, for `M ≥ M₀(w)` the first branch is the minimum and
```
c_w − c_lat(M) ≤ (4/π)(2T cosh T)·M^{−1} + O(M^{−2}) + O_r(V_r M^{−r}).
```
**Sharpness.** `sup_τ |f_lat(τ) − f_w(τ)| ≥ E_edge(M)(1 + o(1))` with the *same* constant
`(4/π) cosh T·d`: the bound is attained asymptotically, so the rate `M^{−1}` and its constant are
exact for this construction and are **not improvable by increasing `r`**.

### Proof

*Feasibility.* The atoms sit at `|u| = |j|d ≥ Md = 2T`; `(D)` (`def:PD`) imposes no moment equality
on `ν`, and the boundary atom at `±2T` is harmless because `č_F(±2T) = 0` (`prop:weak`). `β` is free
in `(D)`, so `β = (2,0)` is admissible.

*Step 1: the three blocks.* By comb-vanishing, `ν_w` has no atoms, so `ν_w = G(u)du` and, by
`thm:Dtail` `eq:Dsplit`,
```
ν̂_w(τ) + 2ĝ₀(τ) = 2Ŵ(τ) + Ψ_w(τ), Ψ_w = R̂. (AL′.1)
```
For the lattice measure, split `G = R + 2W·1_{|u|≥2T}` and use `2T = Md`:
```
ν̂_lat(τ) = [ d Σ_{|j|≥M} κ_j R(jd)e^{ijdτ} ] + [ d Σ_{j∈ℤ} 2W(jd)e^{ijdτ} − T_d(τ) ],
T_d(τ) := d[ Σ_{|j|<M} 2W(jd)e^{ijdτ} + ½(2W(2T)e^{2iTτ} + 2W(−2T)e^{−2iTτ}) ],
```
i.e. `T_d` is exactly the trapezoidal sum, on the window nodes, of
`h(u) := 2 cosh(u/2)·1_{[−2T,2T]}(u)`, whose transform is `ĥ = 2ĝ₀` (`lem:gbounds`). The
`κ_M = ½` weight is what makes the two half-weights at `±2T` complete `T_d`.

*Step 2: the smooth aliases.* `R ∈ C^{r−1}(ℝ)`, `R^{(r)} ∈ L¹`, and likewise `2W`; Poisson summation
applies absolutely to both, and `|R̂(ξ)| ≤ ‖R^{(r)}‖₁|ξ|^{−r}`, `|2Ŵ(ξ)| ≤ 2‖W^{(r)}‖₁|ξ|^{−r}`. Hence
for `|τ| ≤ P/2`, and with the half-weight at `j = ±M` shifting only an `O(d)` amount already counted
in `T_d`,
```
| d Σ_{|j|≥M} κ_j R(jd)e^{ijdτ} + d Σ_{j∈ℤ} 2W(jd)e^{ijdτ} − (R̂(τ) + 2Ŵ(τ)) | ≤ ε_r(M),
```
using `Σ_{k≠0}|τ+kP|^{−r} ≤ 2(P/2)^{−r}(1−2^{−r})ζ(r)` (the deleted low `R`-nodes contribute nothing:
`R ≡ 0` on `(−2T,2T)`).

*Step 3: the edge term.* Combining Step 1, Step 2 and (AL′.1),
```
f_lat(τ) − f_w(τ) = ν̂_lat(τ) − ν̂_w(τ) = [ 2ĝ₀(τ) − T_d(τ) ] + (alias, ≤ ε_r(M)). (AL′.2)
```
So the entire non-smooth cost of sampling is the **quadrature error of the polar block on the
window**. Poisson summation for the BV, compactly supported `h` (symmetric values at the jumps —
this is precisely the trapezoidal weighting), in the symmetric principal-value sense, gives
`T_d(τ) = Σ_{k∈ℤ} ĥ(τ+kP)`, hence
```
2ĝ₀(τ) − T_d(τ) = −Σ_{k≠0} ĥ(τ + kP), ĥ(ξ) = 2ĝ₀(ξ) = 4·[ ½ sinh T cos 2Tξ + ξ cosh T sin 2Tξ ] / (ξ² + ¼).
```
**Phase coherence.** Since `2T·P = 2πM`, `cos 2T(τ+kP) = cos 2Tτ` and `sin 2T(τ+kP) = sin 2Tτ` for
every `k`: all aliases of the edge carry the *same* phase. Therefore
```
2ĝ₀ − T_d = −4[ ½ sinh T cos(2Tτ)·Σ_{k≠0}(ξ_k²+¼)^{−1} + cosh T sin(2Tτ)·Σ_{k≠0} ξ_k(ξ_k²+¼)^{−1} ],
ξ_k = τ + kP.
```
The first sum is absolutely convergent and `≤ 2Σ_{k≥1}((k−½)P)^{−2} = π²/P²`. The second is
conditionally convergent; writing `ξ/(ξ²+¼) = 1/ξ − ¼/(ξ(ξ²+¼))` and using
`Σ_{k≠0}(τ+kP)^{−1} = P^{−1}[π cot(πz) − 1/z]` with `z = τ/P` (the Mittag-Leffler expansion of `cot`;
the subtracted `1/z` is exactly the removed `k = 0` term, so `π cot πz − 1/z` is **regular** at
`z = 0` — no pole, and no cancellation between the two window edges is needed), whose modulus is
`≤ 2/P` on `|z| ≤ ½` (the function `π cot πz − 1/z` is odd, decreasing, equal to
`−2` at `z = ½`), and `¼Σ_{k≠0}|ξ_k|^{−3} ≤ 4.21/P³`, we get
```
|2ĝ₀(τ) − T_d(τ)| ≤ (8 cosh T)/P + (2π² sinh T)/P² + (16.9 cosh T)/P³
 = (4/π) cosh T·d + (sinh T/2)·d² + (2.14/π³) cosh T·d³ =: E_edge(M), [P = 2π/d]
```
uniformly in `τ ∈ ℝ` (the identity is `P`-periodic in the alias index but the bound is uniform).
This is the first display of the theorem (the printed constants above are the rounded-up ones).

*Step 4: the tail branch.* For `|τ| ≤ P/2`, (AL′.2) gives `f_lat ≥ c_w − E_edge − ε_r`. For
`|τ| > P/2`, `σ_T(τ) ≥ m(τ) − 𝖠_T ≥ m(P/2) − 𝖠_T` (`lem:mbounds`(i),(iii)), while
`|ν̂_lat| ≤ ‖ν_lat‖_TV` and `|2ĝ₀| ≤ 2ĝ₀(0)`. Since `m(P/2) = log(πM/4πT)+O(1) → ∞` and
`‖ν_lat‖_TV = V_0 + O(d)` is bounded, the second branch exceeds the first for
`M ≥ M₀(w) := (2T/π)·m^{−1}(c_w + V_0 + 2ĝ₀(0) + 𝖠_T + 1)`. ∎

*Sharpness.* Take `τ` with `sin 2Tτ = ±1` inside `|τ| ≤ P/2`; the `cosh T` term of Step 3 is then
`(8 cosh T/P)(1+O(1/P))` in modulus, so `sup_τ|2ĝ₀ − T_d| = (4/π)cosh T·d·(1+O(d))`. No hypothesis on
`w` enters this quantity at all — `h` does not involve `w`. **`DIAGNOSTIC` confirmation**
(`scripts/r49/r49_01_edge.py`, double precision, `τ`-grid of 2·10⁴ points on `[0,P/2]`):
`sup_τ|2ĝ₀ − T_d|/d = 1.4050, 1.4535, 1.4660` at `M = 16, 64, 256`, `T = ½log3`, against
`(4/π)cosh T = 1.4702`; and `1.5211, 1.5735, 1.5870` at `T = log 2` against `1.5915`. Constant
confirmed to 3 digits and approached from below. ∎

**Corollary AL′.1 (the uncorrected sampling). `PROVED`.** With `κ_M = 1` (plain sampling, no
endpoint correction) the same proof gives
`f_lat − f_w = 2ĝ₀ − T_d + 2d cosh T cos(2Tτ) + alias`, hence
`E_edge^{plain}(M) ≤ (2 + 4/π) cosh T·d + O(d²)` is a valid **upper** bound, but the added
`2d cosh T cos 2Tτ` term is in quadrature with the `sin 2Tτ` edge term of `E_edge`, so the sharp
plain constant is `cosh T·√(4 + 16/π²)·d = 2.3708 cosh T·d` (measured `2.3464 cosh T·d` at `M = 256`,
rising toward `2.3708 cosh T·d`; the triangle bound `(2+4/π)cosh T·d` is never approached), still
`Θ(d)`; at `τ = 0` the discrepancy equals `2d cosh T` exactly, up to `O(d²)`. So the boundary atom of
weight `d cosh T` at `±2T` (admissible in `(D)`) improves the constant by the factor
`√(4+16/π²)/(4/π) = 1.862`, and **nothing improves the order**.

---

## §3 What this says, and what is withdrawn

1. **`cor:ALdef` is RETRACTED.** "The lattice costs `O(M^{−r})`, hence the deficit of Problem A is
 not the lattice" is **false for the full programme**. The lattice costs `Θ(M^{−1})`, with the
 explicit constant `(8T/π)cosh T`, and the loss is *charged entirely to the window edge of the
 polar block*, which is exactly the object `thm:Dtail` isolates and `thm:O` identifies as the
 obstruction. *[amended per R155_050]* The two statements are simply about different
 programmes ((D) full vs. `(D_∞)` archimedean); "agree instead of competing" is withdrawn as
 imprecise.
2. **The classes differ at the edge — but only by `Θ(1/M)`.** By (AL′.2), the flat-top certificate
 and its lattice sample differ by `2ĝ₀ − T_d`. *[amended per R155_050]* **This is not a
 trigonometric polynomial**: `T_d` is a `P`-periodic trig sum of degree `M` (not `< M`) sampling
 the polar block, and `2ĝ₀` is not periodic, so `2ĝ₀ − T_d` is not a trigonometric polynomial
 either. The correct statement is `f_lat − f_w = 2ĝ₀ − T_d + O_r(M^{−r})`. This is
 the precise sense in which `𝒲_T`-certificates are not lattice certificates, and the claim that it
 explains `R155_012`'s finding — that `prop:TK` (whose ceiling uses orthogonality to every mode
 `|j| < M`) does not apply to flat-top certificates — is a **READING**, not proved by AL′.
3. **Comparison with the numbers — CONFLATION, struck.** *[amended per R155_050]* `prop:TK`
 gives `c_lat(M) ≤ Ceil(M,T)`, so AL′ yields `c_w ≤ Ceil(M,T) + E_edge(M) + ε_r(M)` with
 `E_edge = Θ(1/M)` for the *full* programme. The measured deficit `≈ 0.28·M^{−1.17}` of
 `R155_033 §2.5` is the `Ceil_∞` deficit of the **archimedean** programme `(D_∞)`, where `β = 0`,
 the polar block is absent, `G` vanishes to order `r` at `2T`, there is no jump, and sampling is
 `O(M^{−r})` (item 4 below). The edge rate `Θ(M^{−1})` cannot explain the `M^{−1.17}` archimedean
 deficit — the two live in different programmes and must not be compared. What survives: (i) in
 `(D_∞)` the deficit is not the edge, and its source remains the `V_r ↑ ∞` trade-off of
 `R155_033 §2.3`; (ii) in the full programme no `Ceil` has been computed at all, so `E_edge` is
 compared to nothing. "The corrected rate makes `D ≍ M^{−1}` the natural conjecture" is downgraded
 to a **READING**, unsupported by the `Ceil_∞` table. It remains **OPEN** whether the lattice class
 itself (optimising the atom weights rather than sampling) loses `Θ(1/M)`: AL′ bounds one
 construction, not the class.
4. **The archimedean AL survives.** In `(D_∞)` (`R155_033 §2.1–2.3`) the certificate is `m + ν̂_w`
 with `β = 0` and `ν_w = (1−w)K·1_{u≥2T}du`; `G(2T) = (1−w(2T))K(2T) = 0`, there is **no jump**,
 and the `O(M^{−r})` Poisson argument is correct as written. The dichotomy is therefore sharp and
 informative: *in the toy archimedean dictionary sampling is free; in the true explicit-formula
 dictionary of `thm:Z` it costs `Θ(1/M)`, and the difference is precisely the polar block.*
5. **Unaffected by all of the above** (re-checked line by line): `R155_033`'s Theorem R∞, the `τ = 0`
 cap and the "`w` must go negative outside the window" factors `2.307 / 2.576`, the trivial-
 certificate deficit `5.45 / 5.22`, §2.4 (the spectral-gap-not-smoothness reading), §2.5's
 `Ceil_∞` diagnostics and the `T`-independence of the gap, §2.6, and §3 (Prop NC). Only §2.3 and
 the sentence of §0.1(β) that rests on it change. Paper 47's `thm:Z`, `thm:Dtail`, `thm:O`,
 `thm:E`, `lem:F1`, `prop:TK` are untouched and were used, not modified.

---

## §4 Exact replacement text for Paper 47 `subsec:lat` (not applied; `main.tex` not touched)

Replace `main.tex:2925–2968` (the paragraph, `thm:AL`, its proof and `cor:ALdef`) by:

```latex
\subsection{Sampling a flat-top certificate, and where the deficit is}\label{subsec:lat}
Problem~\ref{prob:A} asks for the loss incurred by restricting the dual to a lattice class. For the
flat-top certificates of \S\ref{sec:cert} that loss can be computed exactly, and it is not a
smoothness effect: it is an edge effect, of order $1/M$, carried entirely by the polar block.

\begin{theorem}[lattice sampling of a flat-top certificate]\label{thm:AL}
Let $r\ge2$ and let $w\in\Wcl\cap C^{r-1}(\R)$ with $w^{(r)}$ of bounded variation, $\supp w\subseteq
[-U,U]$ with $C^{r-1}$ contact with $0$ at $\pm U$, and $w(\log n)=0$ for every $\log n>2T$. Put
$W(u)=w(|u|)\cosh\frac u2$, $R=\frac12(1-w)K\mathbf 1_{|u|\ge2T}$ (even), $G=R+2W\mathbf 1_{|u|\ge2T}$
the density of $\nu_w$, $V_0=\|G\|_{L^1}$, $V_r=\|R^{(r)}\|_{L^1}+2\|W^{(r)}\|_{L^1}$, and
$c_w=\inf_\R f_w$. For $M\in\N$ let $d=2T/M$, $P=2\pi/d$ and
\[
\nu_{\mathrm{lat}}=\sum_{|j|\ge M}d\,\kappa_j\,G(jd)\,\delta_{jd},\qquad
\kappa_{\pm M}=\tfrac12,\quad\kappa_j=1\ (|j|>M).
\]
Then $(\nu_{\mathrm{lat}},\beta=(2,0))$ is dual feasible and
\[
c_{\mathrm{lat}}(M)\ \ge\ \min\Big\{c_w-E_{\mathrm{edge}}(M)-\varepsilon_r(M),\
m\big(\tfrac{\pi M}{2T}\big)-\Aconst-\|\nu_{\mathrm{lat}}\|_{\TV}-2\gh0(0)\Big\},
\]
\[
E_{\mathrm{edge}}(M)=\frac{8\cosh T}{P}+\frac{2\pi^2\sinh T}{P^2}+\frac{16.9\cosh T}{P^3}
=\frac4\pi\,\cosh T\cdot d+O(d^2),\qquad
\varepsilon_r(M)=2(1-2^{-r})\zeta(r)V_r\Big(\frac{\pi M}{2T}\Big)^{-r}.
\]
Moreover $\sup_\tau|f_{\mathrm{lat}}-f_w|\ge\frac4\pi\cosh T\cdot d\,(1+O(d))$: the rate $M^{-1}$ and
its constant are attained, and no smoothness of $w$ improves them.
\end{theorem}
\begin{proof}
Feasibility: the atoms lie at $|u|=|j|d\ge Md=2T$, $(D)$ imposes no moment equality on $\nu$
(Proposition~\ref{prop:weak}), the boundary atom at $\pm2T$ is harmless because $\cF(\pm2T)=0$, and
$\beta$ is free. Since $w(\log n)=0$ off the window, $\nu_w=G(u)\,du$ has no atoms and
Theorem~\ref{thm:Dtail} gives $\nuh_w+2\gh0=2\widehat W+\Psi_w$ with $\Psi_w=\widehat R$. Because
$2T=Md$ is a lattice point, the samples of $G$ on $|j|\ge M$ are those of $R$ plus those of $2W$, so
\[
\nuh_{\mathrm{lat}}(\tau)=\Big[d\!\!\sum_{|j|\ge M}\!\!\kappa_jR(jd)e^{ijd\tau}\Big]
+\Big[d\sum_{j\in\Z}2W(jd)e^{ijd\tau}-T_d(\tau)\Big],
\]
where $T_d$ is the trapezoidal sum on the window nodes of $h=2\cosh\frac u2\mathbf 1_{[-2T,2T]}$, whose
transform is $\widehat h=2\gh0$. Both $R$ and $2W$ are $C^{r-1}$ with $r$-th derivative in $L^1$, so
Poisson summation applies absolutely to each and the two bracketed Poisson defects are bounded on
$|\tau|\le P/2$ by $V_r\sum_{k\ne0}|\tau+kP|^{-r}\le\varepsilon_r(M)$. Hence
$f_{\mathrm{lat}}-f_w=\big[2\gh0-T_d\big]+O(\varepsilon_r)$: the whole non-smooth cost is the
quadrature error of the polar block. Poisson summation for the compactly supported BV function $h$
with its symmetric values at the jumps gives $T_d=\sum_k\widehat h(\tau+kP)$, and since $2TP=2\pi M$
all aliases carry the same phase:
\[
2\gh0-T_d=-4\Big[\tfrac12\sinh T\cos2T\tau\sum_{k\ne0}\frac1{\xi_k^2+\frac14}
+\cosh T\sin2T\tau\sum_{k\ne0}\frac{\xi_k}{\xi_k^2+\frac14}\Big],\qquad\xi_k=\tau+kP.
\]
The first sum is at most $\pi^2/P^2$; for the second, $\xi/(\xi^2+\frac14)=\xi^{-1}-\frac14\xi^{-1}
(\xi^2+\frac14)^{-1}$, $\sum_{k\ne0}\xi_k^{-1}=P^{-1}[\pi\cot\pi z-z^{-1}]$ with $z=\tau/P$ (the
subtracted $z^{-1}$ is exactly the removed $k=0$ term, so $\pi\cot\pi z-z^{-1}$ is regular at $z=0$;
no pole and no cancellation between the two window edges is needed), of
modulus $\le2/P$ for $|z|\le\frac12$, and the correction is at most $4.21/P^3$. This is
$E_{\mathrm{edge}}$, uniformly in $\tau$, and it is attained where $\sin2T\tau=\pm1$. For
$|\tau|>P/2$ use $\sT\ge m(P/2)-\Aconst$ (Lemma~\ref{lem:mbounds}), $|\nuh_{\mathrm{lat}}|\le
\|\nu_{\mathrm{lat}}\|_{\TV}$ and $|2\gh0|\le2\gh0(0)$.
\end{proof}

\begin{corollary}\label{cor:ALdef}
At fixed $w$ the lattice sampling costs $\frac8\pi T\cosh T\cdot M^{-1}+O(M^{-2})$, and the
$M^{-1}$ is not removable: it is the alias of the jump of $2\cosh\frac u2\mathbf 1_{|u|<2T}$ at the
window edge, an object independent of $w$. Two consequences. \emph{(i)} The deficit of
Problem~\ref{prob:A} is of order at least the edge cost along this route; the smooth blocks $R$ and
$W$ contribute only $O_r(M^{-r})$, so \emph{the whole lattice cost of a flat-top certificate sits at
$u=\pm2T$} --- the same place as the non-attainment of Theorem~\ref{thm:O}. \emph{(ii)} The
difference $f_{\mathrm{lat}}-f_w$ is, up to $O(M^{-r})$, the discrepancy $2\gh0-T_d$ between the
polar multiplier and its window Riemann sum; here $T_d$ is a $P$-periodic trigonometric sum of
degree $M$ (not a trigonometric polynomial of degree $<M$: $2\gh0$ is not periodic and $2\gh0-T_d$
is not one either). \emph{[amended per R155\_050]} The claim that this is why
Proposition~\ref{prop:TK} --- whose ceiling rests on orthogonality to every mode $|j|<M$ --- bounds
lattice certificates but not flat-top ones is a \textsc{reading}, not proved here. Whether the lattice \emph{class} --- with weights
optimised rather than sampled --- also loses $\Theta(M^{-1})$ is exactly the open half of
Problem~\ref{prob:A}.
\end{corollary}
```

Two further edits required by the same finding: (i) *[amended per R155_050]* the sentence
after `cor:ALdef` beginning "\textsc{diagnostic}. The test-kernel ceilings" keeps its `≈0.28M^{−1.2}`
reading, but its closing clause must **not** be followed by any claim of coherence with the edge rate
of `thm:AL`: `≈0.28M^{−1.17}` is the `Ceil_∞` deficit of the archimedean programme `(D_∞)` (no polar
block, no jump), a different setting from the full-programme edge rate `Θ(M^{−1})`, and comparing the
two is a conflation, not a corroboration; "this suggests `D ≍ M^{−1}`" is at most a **READING**;
(ii) no other statement in the paper cites `thm:AL` (grep: `thm:AL`
appears only at its own label, in `cor:ALdef`, and in the table of results at `main.tex:3156`, whose
row must be reworded to "lattice sampling of a flat-top certificate; the cost is the edge, of order
`M^{-1}`"), so the retraction propagates
nowhere.

---

## §5 Labels of record

| item | label |
|---|---|
*[amended per R155_050]*

| item | label |
|---|---|
| `thm:AL`/`cor:ALdef` **as printed in `main.tex`** | **RETRACTED** (density and hypothesis both wrong) |
| Theorem AL′ (§2) + Corollary AL′.1 | `PROVED` |
| sharpness of `(4/π)cosh T·d` | `PROVED` (asymptotic constant), `DIAGNOSTIC` confirmation to 3 digits |
| "lattice sampling of a flat-top certificate costs `Θ(1/M)`, edge-charged" | `PROVED` |
| "the lattice is never the deficit" (`cor:ALdef`, `R155_033 §0.1(β)`) | **WITHDRAWN** |
| "the lattice *class* loses `Θ(1/M)`" | `OPEN` (AL′ bounds one construction) |
| Theorem AL of `R155_033 §2.3` **in `(D_∞)`** | `PROVED`, unaffected |
| Theorem R∞, Prop NC, `Ceil_∞` diagnostics (`R155_033`) | unaffected |
| "`ν_lat` has finitely many atoms" | **ERROR** → countably many atoms, finite TV |
| Corollary AL′.1 plain-sampling constant `(2+4/π)cosh T·d`, factor `2.57` | **ERROR** → `2.3708 cosh T·d`, factor `1.862` |
| "coherent with the measured `0.28M^{−1.17}`" / "`D ≍ M^{−1}` natural" | **CONFLATION** — struck / downgraded to `READING` (different programme: `Ceil_∞` is archimedean) |
| "`f_lat − f_w` is a trig polynomial of degree `< M`"; `prop:TK` reading | **ERROR** → `2ĝ₀ − T_d`, `T_d` of degree `M`, not periodic-degree `<M`; `prop:TK` applicability claim = `READING` |

Row-D label and the endpoint of record are unchanged. No numerical claim about `ζ` is made.
