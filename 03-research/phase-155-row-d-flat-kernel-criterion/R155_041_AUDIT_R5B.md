# R155_041 — Audit of R155_040 (round 5b, Kreĭn extension)

Target: `R155_040_ROUND5B_KREIN.md`. Sources checked line by line: Paper 46
`04-papers/46-row-d-sign-radial-intersection-form/main.tex` §1 (l. 118–150, 180–215, 265–290), §2 (l. 294 `eq:g`),
§3 (l. 430–470 `def:PD`, `prop:weak`, `prop:P` l. 604 ff.), §5 (l. 880–900 `thm:C`), §5.x (l. 985–1005
`subsec:compare`), §7 (l. 1120 `def:W`, l. 1135 `thm:Z`, l. 1176 `thm:Zexh`, l. 1206 `cor:RH`,
l. 1224 `cor:zeros`, l. 1350 `thm:finZ`, l. 1453 `prop:finuniv`, l. 1538 `rem:RHcert`, l. 1554
Remark (Kreĭn)), §8 (l. 1699–1715, 1775–1790), §9 (l. 2650–2680); `R155_014` Rem. 2.5; `R155_031` §4 P5.

## §1 Verdicts

| item | verdict |
|---|---|
| §2 Defs (2.1)/(2.2), Def. 2.1 KEP(T) | **CORRECT.** (2.1) is `eq:fw` (l. 1137) read on `h=w\cos(\tau\cdot)`, with `h(0)=w(0)=1`; the `2π` is right: for even `h`, `\hat h(\tau)=\int h\cos\tau u\,du` and `(1/2π)\int\hat h\cos(\tau u)d\tau=h(u)`, so `ν_w=f_w d\tau/2π` has `\hat ν_w=w\!\cdot\!g` exactly, no stray factor. `μ_ζ` tempered (`N(t)\ll t\log t`) and `\hatμ_ζ=g` distributionally by `thm:Z`(ii). |
| Lemma 2.2 (signature (1,1)) | **PROVED.** Gram `=ab^T+ba^T`, `a_i=e^{t_i/2}`, `b_i=e^{-t_i/2}`; eigenvalues `a\!\cdot\!b\pm|a||b|`, and `a\!\cdot\!b=n<|a||b|` strictly for `n\ge2` distinct points (Cauchy–Schwarz, `a\nparallel b`). |
| Thm 1 (certificate ⟹ a.c. solution; strict ⟹ continuum) | **PROVED.** The audit's worry is unfounded: `R155_040`'s `r_χ` (l. 109) **does** carry the prime atoms `-\sum_n v_nχ(\log n)\cos(\tau\log n)`, finite because `χ\in C_c^\infty` and `\sum_{n\notin N_T}v_n|χ(\log n)|<\infty`; `|ε|<c/R` gives `f_{w_ε}>0`. Distinctness is also right: `χ\!\cdot\!g` has a.c. part `χ(u)D(u)\ge0`, `\not\equiv0` (`D>0` on `|u|\ge2T\ge\log2>0.3`, `thm:Zexh` l. 1195), which the negative **atoms** cannot cancel (a.c. vs singular). |
| Thm 2 (solvable ⟹ `λ^W_T\ge0`) | **PROVED on `C_c^\infty(-T,T)`; one unstated hypothesis.** With `F\in C_c^\infty`, `\hat h=|\hat F|^2` is rapidly decaying, so the pairing against a positive **tempered** `ν` is legitimate — the audit's `L^2` regularity worry is avoided by `R155_040`'s own choice of class. **Gap M1 (`R155_040` l. 118, 121):** the step `W_T\ge0` on `C_c^\infty(-T,T)` `\Rightarrow λ^W_T\ge0` (inf over the unit sphere of `L^2(I_T)`) needs `C_c^\infty(I_T)` to be a form core for `W_T`; `\mathfrak a_T`'s form domain is stated at l. 123 of `main.tex` but the core property is not. One line, but must be written. |
| Thm 3 (dichotomy; RH ⟺ indeterminate ∀T) | **PROVED, modulo M1.** The audit's suspected gap at `λ^W_T=0` is handled: `R155_040` does not use `cor:RH`'s **statement** (which gives only `f_w\ge0`) but its **proof** (l. 1214–1221 of `main.tex`: the Jensen/exponential-type argument yields `λ^W_T>0` strictly under RH), and says so at l. 134. `𝒲_{T'}\subset𝒲_T` for `T'>T` is `main.tex` l. 1779. Chain (1)⟹(4)⟹(3)⟹(2)⟹(1) closes. |
| Thm 4 (finite `Z`: `μ_Z` unique finite positive symmetric solution) | **PROVED, and a genuine strengthening of `thm:finZ`.** Steps 2–4 of `thm:finZ` use only continuity, PD and agreement at `0,a,\dots,ra`; Step 5 (the only use of `w\to0`) is not needed. The lattice-density step is valid: for each `m\ge1` the identity `φ(ma)=g_Z(ma)` holds for all `a\in(0,2T/d]` off a discrete set, both sides continuous in `a` ⟹ all `a`; `\bigcup_m m\cdot(0,2T/d]=(0,\infty)`. The three-line derivation of `thm:finZ` from it (l. 159–163) also checks out. |
| Thm 5 (perturbed datum `g_β` at `½log3`) | **PROVED** as a statement about `g_β`; its `OPEN` rider is **WRONG** (E1 below). |

## §2 Errors of record

**E1 (major, `R155_040` l. 31, 171–174, 207).** *"`λ^W_{½\log3}>0` unconditionally is OPEN"* and *"no
unconditional indeterminacy at any window is established here"* are **false**. `main.tex` l. 994–997:
Zhu's Thm 1.2 certifies `Q(f)\ge8.9\cdot10^{-18}\|f\|^2` for `\supp f\subseteq[-0.8,0.8]`, **for the
complete form `Q=W_T`** (the paper states this explicitly). `W_T` is the restriction of `W_{0.8}` to
`L^2(I_T)\subset L^2(I_{0.8})`, so `λ^W_T` is nonincreasing in `T` (trivially, and `main.tex` l. 1781);
since `½\log3=0.5493<0.8`,
```
λ^W_{½log3} ≥ λ^W_{0.8} ≥ 8.9·10⁻¹⁸ > 0.
```
Hence, by `R155_040`'s **own** Thm 3(a), **KEP(T) is unconditionally indeterminate for every
`T\le0.8`**, in particular at `½\log3`. Status of `λ^W_{½\log3}>0`: **KNOWN via Zhu 2026**
(`CITED-NOT-VERIFIED`: a certified matrix computation in a 2026 preprint), **not** via `thm:C`, and
**not** via `prop:P` (whose hypothesis `β=(2,0)` Theorem C fails). Note Yoshida/Bombieri reach only
autocorrelation support `\log2`, i.e. `T=½\log2=0.347<0.5493`, and `Paper42`'s `T\le\log2` is the
primitive `λ^A` — so the conclusion rests on Zhu alone. `R155_040` §0.3, §3 Thm 5 and §5 rows 7–8
must be rewritten accordingly.

**E2 (minor, `R155_040` l. 90–91, 193–194).** *"Lemma 2.2 is the structural reason `β_0=2`"* and
*"(`rem:RHcert`, previously heuristic)"*: a **reading, not a proof**, and the attribution is wrong.
Uniqueness of `β_0=2` is already `PROVED` in `prop:P` (`main.tex` l. 604 ff.: `\Rel(A\bar B)` takes
both signs, witnesses `(1,\pm1,0,0)`); what is heuristic in `rem:RHcert` is only the *convergence of
optimiser duals* to `(2,0)` (paper open item (2), l. 2653). Lemma 2.2 explains the **rank/one negative
square**, not the coefficient `2`, which comes from the polar term `2\Rel(A\bar B)`.

**E3 (minor, l. 136).** For `0<T<½\log2` the transported certificate needs a perturbing `χ` supported
in `\{|u|\ge\log2\}` (where `D>0`), not merely outside `(-2T,2T)`. Trivial to fix; say it.

**Correct in substance (the half of §0.3 that stands):** "Theorem C ⟹ KEP(½log3) indeterminate" is
indeed **false as stated** — `thm:C`'s `β=(2.00256\ldots,-0.00965\ldots)\ne(2,0)` (`main.tex` l. 892),
`g_0,g_1` are supported **inside** the window (`main.tex` l. 294 `eq:g`, `\mathbf 1_{|u|<2T}`), and the
defect `|β_0-2|\hat g_0(0)=5.9\cdot10^{-3}\gg c=8.86\cdot10^{-5}` is not absorbable. The conclusion
"therefore nothing unconditional" is what fails (E1).

## §3 Paper 46: does it over-claim? (item 7(b))

Grep of `\lamW`, "complete Weil form", "Weil form" over `main.tex`: **no over-claim found.** The
abstract quotes `λ_min\ge8.8577\cdot10^{-5}` for `A_T` "with the two Tate moments killed" (primitive);
`thm:C` l. 898 states `λ^A\ge λ^P\ge\ldots`; l. 185–188 flags `β_0=2.0026`; l. 1107 says the sign at
`½\log3` "rests on `Paper42`, `Zhu2026`". **One sentence to sharpen, not to correct:** l. 284–286,
"Positivity at `T\le\log2` is known … and at support 1.6 by Zhu; Theorem C is an independent proof …
not a new range" — add "of the **primitive** form", since Zhu's is the complete one.

## §4 Labels (as they should read)

- Lemma 2.2, Thms 1, 4, 5: `PROVED`. Thm 2, Thm 3: `PROVED` after M1 (form-core line).
- `λ^W_{½\log3}>0`: **KNOWN** (Zhu 2026, `CITED-NOT-VERIFIED`), *not* `OPEN`.
- KEP(T) indeterminate for `T\le0.8`: **PROVED unconditionally** (Zhu + Thm 3(a)).
- "KEP(T) indeterminate for **every** `T>0`": **RH-EQUIVALENT** (Thm 3(b)) — this reclassification of
 `R155_014` Rem. 2.5 is correct and is the file's real contribution.
- §4(iii) extremal extensions: `HEURISTIC`. Row-D label: **unchanged**, no sign.

## §5 Readiness of the Paper 46 proposals

(1) §7.x with Def. 2.1 + Lemma 2.2 + Thms 1–3: **ready after M1 and E1**; it is a reformulation, and
must be presented as such. (2) Thm 4 **should** replace `thm:finZ`'s proof (prove Thm 4, derive
`thm:finZ` in three lines): **ready, recommended** — the decay hypothesis is then visibly inessential.
(3) Amending open item (5): **ready** ("a third proof of `thm:D1`" → an RH-equivalence), but the
"remaining honest question" must not be stated as `λ^W_T>0` at `½\log3` (E1); state it at
`T>0.8`. (4) Amending `R155_014` Rem. 2.5: **ready** with the E1 correction folded in.

**Net.** Three correct theorems, one correct correction, one wrong "OPEN" that inverts the file's
headline conclusion at `½\log3`. P5 is answered and should be closed as a route.
