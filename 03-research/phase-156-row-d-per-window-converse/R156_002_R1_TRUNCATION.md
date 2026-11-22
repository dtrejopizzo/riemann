# R156_002 — Report, 156d-R1: the truncation lemma for the Gaussian witness

Task: `R156_000` round 1, row 2; residual **R1** of `R155_057` (l.59–67, 261–266),
left by `R155_054` §1.1 (l.50–56). Pure mathematics; the only numerics are trivial arithmetic on constants P47 has already
certified. Every statement labelled. Paper 47 = `04-papers/47-intersection-frame-defect/archive/main.md` (P47). Nothing in P47 or any
README is edited.

**Verdict.** Residual R1 is **closed**. Theorem 19.25 holds with `h⁰` defined only on `𝒟_c := C_c^∞(R) ⊕ RK`, and also
on the smaller space `𝒟_p := P_c^∞ ⊕ RK`, which is the linear span of `𝒢_min`. The proof of 19.25 uses **no** property of
the Gaussian that truncation destroys. The one exact identity it needs is `\deg F = 0`, and an even cutoff keeps it,
because `F_0` is odd. No finite-dimensional correction is needed on `𝒟_c`. On `𝒟_p` a one-dimensional correction of size
`< 2×10^{−17}` restores primitivity. No new certified constant enters. The only new input is the classical bound
`Σ_ρ|γ_ρ|^{−2} < 1`. One side finding (§7) matters for how R1 is worded. On the bare set `𝒢_min`, which only has classes
of degree `0` and `1`, the hypothesis of Theorem 12.3 is **equivalent to RH** (take `h⁰ ≡ 0`), so the frame defect cannot
act there. The correct small domain is a linear one, and it must contain classes of degree `≥ 326`.
**[amended per R156_003, A2: "must contain classes of degree `≥ 326`" is not proved. What is proved is: (i) no
unconditional non-existence theorem is possible on the bare set `𝒢_min` unless RH is false (Prop 7.1); (ii) the kill of
Theorem 6.1 uses the pair `\{E_w, K−E_w\}`, whose degrees are `d > d_0^{(R)}` and `1−d`. No lower bound on the degree of an
arbitrary witness is proved; it is governed by the unknown `s_*` of P47 §19.9 and by witnesses of other shapes.]**

## 0. Corpus check

* `grep -n -i "truncat"` over phases 142–155 and P47: nothing truncates `F_0`. The hits are about truncating zero sums or
  scan windows (`R143_002:193,314`, `R143_000:38`). The only statements of the residual are `R155_054:50-56` and
  `R155_057:59-67`, and both are sketches labelled `OPEN`. P47 has a compactly supported witness only for `Ξ_a`
  (Theorem 19.15).
* Paper 46 `lem:roughEF` (`04-papers/46-row-d-dual-certificates/main.tex:690`) goes the **other** way: it mollifies a
  rough test **into** `C_c^∞` so that Paper 45 Thm 9.4 applies. It is not needed here. Every functional below is already
  defined, with its explicit formula, on all of `D^W`: Theorem 11.3 for the explicit formula, Theorem 11.5 for the
  comparison identity (11.6), and Theorem 11.14 for `w_F` and `C_F`. `F_0` and its truncation both lie in `D^W`. **No
  approximation of the explicit formula is needed, and no topology on `D^W` either** (P47 §19.9 correctly notes that §11
  has none). All that is needed is the explicit seminorm bound of Lemma 3.1, which follows from Theorem 11.14 and (11.2).

## 1. The small domains and the restricted clauses

**Definition 1.1.** `P_c^∞ := \{F ∈ C_c^∞(R) \text{ real} : Φ_F(0) = Φ_F(1) = 0\}`, `𝒟_c := C_c^∞(R) ⊕ RK`,
`𝒟_p := P_c^∞ ⊕ RK`. The sums are direct because `K > 0` everywhere (Theorem 11.7(i)), so `K ∉ C_c^∞`.
`𝒢_min := \{nF,\ K−nF : F ∈ P_c^∞,\ n ∈ Z\}` (the set named in `R155_054:50`, `R155_057:52`).

For a subset `𝒟 ⊆ D^W` and `h⁰ : 𝒟 → R_{≥0}`, the clauses restricted to `𝒟` are:
(a)_𝒟 `h⁰ ≥ 0` on `𝒟`;
(b′)_𝒟 if `E ∈ 𝒟` and `h⁰(E) > 0`, there is `E' ∈ D^W` with `E' ≥ 0`, `E' ≢ 0`, `E − E' ∈ 𝓝_∞`;
(c)_𝒟 `h⁰(E) + h⁰(K−E) ≥ R(E)` whenever `E, K−E ∈ 𝒟`, with `R` from Definition 19.1.
In (b′)_𝒟 the representative may lie anywhere in `D^W`. Requiring `E' ∈ 𝒟` only makes the hypothesis stronger, so every
non-existence result below also covers that reading.

**Lemma 1.2 (`PROVED`).** (i) `𝒟_c` and `𝒟_p` are `σ_K`-stable, and `𝒟_p = \mathrm{span}_R 𝒢_min`. (ii) Theorem 12.3
runs verbatim for `h⁰` defined on `𝒟_p` (a fortiori on `𝒟_c`, or on `𝒢_min`) satisfying (a),(b′),(c) restricted to that
domain. (iii) `𝓝_∞ ∩ 𝒟_c = 0`.
**[amended per R156_003, A6: (ii) should read "Theorem 12.3 runs verbatim for `h⁰` defined on any `𝒟 ⊇ 𝒢_min`,
with the clauses restricted to `𝒟`; in particular on `𝒢_min`, on `𝒟_p` and on `𝒟_c`". The smallest domain is the
strongest case, and the others follow from it by restriction. The draft had the "a fortiori" backwards.]**

*Proof.* (i) `K − (G + cK) = −G + (1−c)K`. Since `nF, K − nF ∈ 𝒢_min`, the span contains `P_c^∞` and `K`, and it lies
inside `𝒟_p`. (ii) Theorem 12.3's proof (P47:2744–2797) evaluates `h⁰` only at `nF` and `K − nF`, with `(c)` used at
`E = nF`. The ample class `H' = F + 2mK` of Step 1 enters only through `I_∞(·,H')`, never through `h⁰`. (iii) Let
`N = G + cK ∈ 𝓝_∞` with `G ∈ C_c^∞`. By (11.14), `Φ_N(ρ) = Φ_G(ρ) + cξ(ρ) = Φ_G(ρ) = 0` at every zero. The proof of
Theorem 11.12 (zero counting, (X13), (X18)) gives `G = 0`. Then `Φ_N(0) = c/2 = 0`. ∎

(iii) explains why R1 is not a formality. On `𝒟_c` no two classes are identified modulo the radical, so `F_0` cannot be
swapped for an `𝓝_∞`-equivalent compactly supported class for free. Whether any such class exists is not decided here
(`OPEN`, not needed). The truncated class `F_R` is a **different** class. It works only because the inequality it has to
satisfy is strict and open. Contrast the curve model in Remark 8.3.

## 2. What the proof of Theorem 19.25 actually uses of `F_0`

I read the proofs of Theorems 19.21, 19.23 and 19.25 and Corollary 19.24 (P47 §19.6–19.7) line by line. The class `F_0`
enters **only** through four properties:

* (U1) `F ∈ D^W`, real. This makes `E = tF + dK ∈ D^W` and makes (11.6), Theorem 11.13 and Theorem 11.14 available.
* (U2) `\deg F = 0` **exactly**. This gives (19.3): `\deg E = d`, `I_∞(F,K) = 0`, `I_∞(E,E) = d²/2 − t²W_F`.
* (U3) `W_F := −I_∞(F,F) > 0`.
* (U4) `s_F := C_F/\sqrt{W_F/2} < 1` **strictly**, where `C_F` is the exact constant of Theorem 11.14(ii).

The proof does **not** use: the Gaussian integrals (they serve only to *evaluate* `C_{F_0}` and `W_{F_0}` in
Lemma 19.20); positivity of any Fourier transform; primitivity (`F_0` is not primitive, since `η ≠ 0`); oddness, except
as the reason (U2) holds; any exact moment beyond `\deg F = 0`; or simplicity of `ρ_1`, except through the numerical
values behind (U4). So the only exact identity that truncation could break is (U2). §4 shows it is kept.

**Proposition 2.1 (the abstract witness; `PROVED`, unconditional; it is Theorems 19.21 and 19.23 with `F_0` replaced by
`F`).** Let `F` satisfy (U1)–(U4). Fix `χ ∈ R` and `d > 1` with `d²(1 − s_F²) > d − 4χ`. Pick `t > 0` with

    s_F²d²/2 \;<\; t²W_F \;<\; d²/2 − d/2 + 2χ                                   (2.1)

(the interval is nonempty exactly when the displayed inequality holds), and put `E := tF + dK`. Then `\deg E = d > 1`,
`R(E) > 0`, and **no** `E' ∈ D^W` has `E' ≥ 0`, `E' ≢ 0`, `E − E' ∈ 𝓝_∞`. The same holds for every positive multiple
`N·E` (the stable form of Corollary 19.24).

*Proof.* (19.3) uses only (U1),(U2), `\deg K = 1` and `I_∞(K,K) = ½` (Theorem 19.21's proof). So
`R(E) = ½(d²/2 − t²W_F) − d/4 + χ > 0` by the upper bound in (2.1). Suppose such an `E'` exists. By Theorem 11.11 and
Theorem 11.13(ii),(iv), `\deg E' = d` and `I_∞(E',F) = I_∞(E,F) = −tW_F`. Theorem 11.14(ii) then gives
`tW_F ≤ C_F d`, i.e. `t²W_F ≤ C_F²d²/W_F = s_F²d²/2`, which contradicts the lower bound in (2.1). For `N·E` the factor
`N` cancels, as in Corollary 19.24. ∎

With `F = F_0`, Lemma 19.20(v),(vi) and Proposition 19.18 give `s_{F_0} ≤ s_1(1 + 10^{−89})`. That is P47's case.
**[amended per R156_003, A4: Proposition 2.1 stated with the exact ratio `s_F` is the correct form. P47 Theorem 19.23
states its window with `s_1` in place of `s_{F_0}` (P47:6297), and its proof reaches only
`t²W_{F_0} ≤ s_1²d²/2·(1+10^{−89})`. So the admissible `t` with `t²W_{F_0} ∈ (s_1²d²/2,\ s_1²d²/2·(1+10^{−89})]` are not
covered, and the threshold `d_0 = (1−s_1²)^{−1}` is a sliver too low. This is harmless for Theorem 19.25, which needs one `t`
(the certified instance sits far from that edge). It is an editor item for P47, and P47 is not edited here.]**

*Side remark (not load-bearing).* Lemma 19.20(v) states `W(F_0) = −I_∞(F_0,F_0) + 2η²`. Its own proof line,
`I_∞ = 2Φ(0)Φ(1) − W = −2η² − W`, gives `W(F_0) = −I_∞(F_0,F_0) − 2η²`. The sign of the `2η²` term is a typo of size
`< 10^{−780}` and changes nothing. It is flagged for the editor, not corrected here (no P47 edits).

## 3. The two estimates

For measurable `g` let `N(g) := ∫_R |g(u)|\,2\cosh(u/2)\,du`. Let `S_2 := Σ_ρ |ρ − ½|^{−2}`, summed over the zeros of `ξ`
with multiplicity.

**Lemma 3.1 (seminorm bounds; `PROVED`, unconditional given `S_2 < ∞`, i.e. (E3d)).** For real `F, E ∈ D^W`:
 (i) `F ↦ w_F` of (11.16) is linear, so `C_{F+G} ≤ C_F + C_G` for the exact constants of Theorem 11.14(ii);
 (ii) `C_F ≤ N(F) + S_2\,N(F'')`;
 (iii) `|I_∞(E,F)| ≤ C_F\,N(E)` for **every** `E ∈ D^W`, effective or not;
 (iv) `|Φ_F(0)| + |Φ_F(1)| ≤ N(F)`.

*Proof.* (i) (11.16) is linear in `(Φ_F(0), Φ_F(1), (Φ_F(1−ρ))_ρ)`, the zero sum converging absolutely (Theorem 11.14).
So `w_{F+G} = w_F + w_G`, and a supremum of `|w|/2\cosh` is subadditive. (iv) `e^{±u/2} ≤ 2\cosh(u/2)`. (ii) Apply
(11.17). The polar part is at most `N(F)` by (iv). For the zero part, (11.2) at `s = 1−ρ`, `σ = 1 − β ∈ (0,1)` (E2)
gives `|Φ_F(1−ρ)| ≤ |ρ−½|^{−2}∫|F''(t)|e^{(½−β)t}dt ≤ |ρ−½|^{−2}N(F'')`, because `|(½−β)t| ≤ |t|/2`. Sum over `ρ`.
(iii) Theorem 11.14(i) gives `I_∞(E,F) = ∫E\,w_F`, absolutely convergent. So
`|I_∞(E,F)| ≤ ∫|E||w_F| ≤ C_F∫|E|2\cosh(u/2) = C_F N(E)`. ∎

This is the "`C²`-weighted continuity" that `R155_057:59-61` invoked, written out. It needs no topology: (ii) and (iii)
are inequalities between numbers.

**Lemma 3.2 (`S_2 < 1`; `PROVED` given a classical import).** `S_2 ≤ 0.0465`.

*Proof.* The import (**CLASSICAL**) is Davenport, *Multiplicative Number Theory*, 3rd ed., Ch. 12, eqs. (10)–(11):
`Σ_ρ \mathrm{Re}(1/ρ) = 1 + ½γ_E − ½\log 4π = 0.0230957…`. This is unconditional, and the terms `β/|ρ|²` are positive.
The zero multiset is invariant under `ρ ↦ 1 − \barρ` (E2 plus reality). For `β ∈ (0,1)`,

    \mathrm{Re}\tfrac1ρ + \mathrm{Re}\tfrac1{1−\barρ} = \tfrac{β}{β²+γ²} + \tfrac{1−β}{(1−β)²+γ²} ≥ \tfrac{1}{1+γ²} .

Averaging over the involution gives `Σ_ρ(1+γ²)^{−1} ≤ 2·0.0230957 < 0.04620`. Every zero has `|γ| ≥ γ_1 > 14` (X19). So
`|ρ−½|^{−2} ≤ γ^{−2} ≤ (1 + 14^{−2})(1+γ²)^{−1}`, and `S_2 ≤ 1.0052·0.04620 < 0.0465`. ∎

*Second route, needing no new import.* Use the count P47 itself uses in Lemma 19.20(iv): `≤ \log T` ordinates in
`[T,T+1]`, `T ≥ 21`, and only `ρ_1, \barρ_1` below `21` (X19). This gives
`S_2 ≤ 2/γ_1² + 2∫_{20}^∞ t^{−2}\log t\,dt = 0.0101 + (1+\log 20)/10 < 0.41`.
**[amended per R156_003, A10: this route inherits P47's count `≤ \log T` per unit interval for `T ≥ 21`
(Lemma 19.20(iv), `certify_leakage.py:8–10`). Trudgian-type bounds for `S(T)` do not give that count for
`21 ≤ T ≲ 2×10^4`; there it needs the verified zero list. So "no new import" is accurate only relative to P47's own
unaudited input. The route is not used; Lemma 3.2 rests on the Davenport route.]** **Only `S_2 ≤ 1` is used below.** Even
without any explicit constant, (E3d) alone gives `S_2 < ∞` and everything goes through with a larger `R_0`.

## 4. The truncation lemma

**[amended per R156_003, A1: the cutoff was called `χ` in its draft, which collides with the
Riemann–Roch constant `χ` of Definition 19.1; it is renamed `ϑ` throughout §§4, 5, 8.4 and the auditor notes. Every
`χ` that remains in this memo is the Riemann–Roch constant.]**
Fix a cutoff `ϑ ∈ C_c^∞(R)`, **even**, `0 ≤ ϑ ≤ 1`, `ϑ = 1` on `[−1,1]`, `\mathrm{supp}\,ϑ ⊆ [−2,2]`. Put
`A := 1 + \|ϑ'\|_∞ + \|ϑ''\|_∞`, `ϑ_R(u) := ϑ(u/R)`, and

    F_R := F_0\,ϑ_R ∈ C_c^∞(R),\qquad D_R := F_0 − F_R = F_0(1 − ϑ_R) .

**Lemma 4.1 (truncation; `PROVED`, unconditional given (X19) and Lemma 3.2).** Let
`R ≥ R_0(ϑ) := 6\sqrt{40 + 2\log A}` (`≥ 37.95`). Then:
 (i) `F_R ∈ C_c^∞(R)` is real and **odd**, `\mathrm{supp}\,F_R ⊆ [−2R, 2R]`, and `\deg F_R = 0` **exactly**;
 (ii) `N(D_R) ≤ 4e^{−R²/36}`, `N(D_R'') ≤ 76\,A R\,e^{−R²/36}`, `C_{D_R} ≤ 80\,A R\,e^{−R²/36} ≤ 10^{−6}`;
 (iii) `C_{F_R} ≤ G s_1 + 10^{−6} + 10^{−90}`;
 (iv) `|W_{F_R} − W_{F_0}| ≤ C_{D_R}(2N(F_0) + N(D_R)) ≤ 9.3×10^{−5}`, with `N(F_0) ≤ 4Ge^{9/8} < 46.33`; hence
      `W_{F_R} > 2G² − 10^{−4} > 0`;
 (v) `s_{F_R} = C_{F_R}/\sqrt{W_{F_R}/2} ≤ s_1 + 3.6×10^{−6} < \bar s := 0.998464 < 1`, and
      `1 − s_{F_R}² ≥ 1 − \bar s² > 3.0696×10^{−3}`;
 (vi) `|Φ_{F_R}(0)| = |Φ_{F_R}(1)| ≤ 10^{−390} + N(D_R) < 2×10^{−17}`.
So `F_R` satisfies (U1)–(U4), and in the threshold of Theorem 19.23 `s_1` is replaced by `\bar s`:
`d_0^{(R)} := (1 − s_{F_R}²)^{−1} < 325.78`.

*Proof.* (i) `ϑ_R` is even and `F_0` is odd, so `F_R` is odd. Then `u ↦ F_R(u)2\cosh(u/2)` is odd and integrable, so
`\deg F_R = 0` with no error term. The support claim is clear.

(ii) *Pointwise bounds.* Write `g = e^{−u²/18}`. Then `|F_0| ≤ g`, `|F_0'| ≤ g(|u|/9 + γ_1)`, and
`|F_0''| ≤ g[(|u|/9 + γ_1)² + 1/9]`, from `F_0'' = g[(u²/81 − 1/9 − γ_1²)\sin γ_1u − (2γ_1u/9)\cos γ_1u]`. We have
`D_R'' = F_0''(1−ϑ_R) − 2F_0'ϑ_R' − F_0ϑ_R''`. Every term vanishes for `|u| < R`. For `R ≥ 1`, `|ϑ_R'| ≤ \|ϑ'\|_∞` and
`|ϑ_R''| ≤ \|ϑ''\|_∞`. For `|u| ≥ 18` we have `|u|/9 + γ_1 ≤ |u|` (since `γ_1 < 14.14 < 16`), so

    |D_R''(u)| ≤ g(u)\big(u² + 2\|ϑ'\|_∞|u| + \|ϑ''\|_∞ + 1\big)\mathbf 1_{|u|≥R} ≤ A\,u²\,g(u)\,\mathbf 1_{|u|≥R}\quad(R ≥ 18).

*Tail integrals.* For `u ≥ 18`, `u/2 ≤ u²/36`, so `g(u)2\cosh(u/2) ≤ 2e^{−u²/36}`. With
`I_k := ∫_R^∞ u^k e^{−u²/36}du`: `I_0 ≤ (18/R)e^{−R²/36}` and `I_2 = 18Re^{−R²/36} + 18I_0 ≤ 19R\,e^{−R²/36}` for
`R ≥ 18`. Hence `N(D_R) ≤ 4I_0 ≤ 4e^{−R²/36}` and `N(D_R'') ≤ 4A\,I_2 ≤ 76ARe^{−R²/36}`. By Lemma 3.1(ii) and
`S_2 ≤ 1`, `C_{D_R} ≤ (4 + 76AR)e^{−R²/36} ≤ 80ARe^{−R²/36}`. Write `R = 6\sqrt L`. Then
`80AR e^{−R²/36} = 480A\sqrt L e^{−L} ≤ 480A e^{−L/2}` (because `\sqrt L e^{−L/2} ≤ e^{−1/2}`). This is `≤ 10^{−6}` once
`L ≥ 2\log(4.8×10^8 A)`, and `2\log(4.8×10^8) = 39.98`. So `R ≥ R_0` suffices. It also gives `R ≥ 18`.

(iii) Lemma 3.1(i) with `F_R = F_0 − D_R`, and Lemma 19.20(vi): `C_{F_0} < Gs_1 + 10^{−90}`.

(iv) `W_{F_R} − W_{F_0} = 2I_∞(F_0,D_R) − I_∞(D_R,D_R)`. By Lemma 3.1(iii), with the pairing taken against `D_R` in the
second slot, this is at most `C_{D_R}(2N(F_0) + N(D_R))`. Next,
`N(F_0) ≤ ∫e^{−u²/18}2\cosh(u/2)du = 2σ\sqrt{2π}e^{σ²/8} = 4Ge^{9/8} = 46.325…`, so the bound is
`≤ 10^{−6}·92.66 < 9.3×10^{−5}`. Finally `W_{F_0} = 2G²(1 ± 10^{−90})` with `2G² = 9π = 28.2743…` (Lemma 19.20(v)).

(v) By (iv), `W_{F_R}/2 ≥ G² − 4.65×10^{−5} = G²(1 − 3.29×10^{−6})` (using `G² = 9π/2 = 14.137…`), so
`\sqrt{W_{F_R}/2} ≥ G(1 − 3.29×10^{−6})`. With (iii),
`s_{F_R} ≤ (s_1 + 2.7×10^{−7})(1 + 3.3×10^{−6}) ≤ s_1 + 3.6×10^{−6} = 0.9984638… < \bar s`. Then
`1 − \bar s² = 2(1.536×10^{−3}) − (1.536×10^{−3})² = 3.06964×10^{−3}`.

(vi) `Φ_{F_R}(0) = η − Φ_{D_R}(0)`. Use Lemma 19.20(ii) and Lemma 3.1(iv). Oddness gives `Φ(1) = −Φ(0)`. ∎

**Certified instance, carried over (trivial arithmetic).** Take `χ = 0` and `d = 400`. The window (2.1) for `t²W_{F_R}` is
`(\bar s²·80000,\ 79800) ⊇ (79754.43,\ 79800)`, which is nonempty. Take `t²W_{F_R} = 79780`, i.e.
`t := (79780/W_{F_R})^{1/2}`. Then `\deg E = 400`, `I_∞(E,E) = 220`, `R(E) = 10`, all exactly as in P47:6412–6422. The
value of `t` differs from `53.11911…` only in the fifth significant digit, because `W_{F_R}` is known only to `10^{−4}`.
It is defined implicitly, and nothing needs it numerically.
**[amended per R156_003, A7: the relative error in `W_{F_R}` is `≤ 3.3×10^{−6}`, so `|Δt| ≤ 1.7×10^{−6}·t < 10^{−4}`. The
change is at the sixth significant digit or later, not the fifth. P47's certified instance is at P47:6308–6320, not
6412–6422.]**

## 5. The primitive version (the span of `𝒢_min`)

Fix `B ∈ C_c^∞(R)` real and odd with `Φ_B(0) = 1`. For example, take `B := −uψ(u)/c_ψ` with `ψ ≥ 0` an even bump,
`ψ ≢ 0`. Then `c_ψ := ∫uψ(u)\sinh(u/2)du > 0` and `Φ_B(0) = ∫B e^{−u/2} = 1`. Put `β_B := N(B) + N(B'') < ∞`, so that
`C_B ≤ β_B` by Lemma 3.1(ii) with `S_2 ≤ 1`.

**Lemma 5.1 (a primitive compactly supported witness class; `PROVED`, same hypotheses as Lemma 4.1).** Let `R ≥ R_0(ϑ)`
and in addition `(10^{−390} + 4e^{−R²/36})\,β_B ≤ 10^{−6}`. Put `η_R := Φ_{F_R}(0)` and `F_R^♭ := F_R − η_R B`. Then
`F_R^♭ ∈ P_c^∞` is real and odd, and it satisfies (U1)–(U4) with

    C_{F_R^♭} ≤ Gs_1 + 2×10^{−6} + 10^{−90},\qquad s_{F_R^♭} ≤ s_1 + 8×10^{−6} ≤ 0.998469,\qquad
    1 − s_{F_R^♭}² > 3.0596×10^{−3},\quad d_0^{♭} < 326.9 .

*Proof.* `Φ_{F_R^♭}(0) = η_R − η_R = 0`, and oddness gives `Φ(1) = −Φ(0) = 0`. So the class is primitive, and in
particular `\deg = 0`. Write `F_R^♭ = F_0 − D'` with `D' := D_R + η_R B`. By Lemma 3.1(i), (iv) and 4.1(vi),
`C_{D'} ≤ C_{D_R} + |η_R|β_B ≤ 2×10^{−6}` and `N(D') ≤ N(D_R) + |η_R|N(B) ≤ 2×10^{−6}`. Repeat 4.1(iii)–(v) with `D'`:
`|W − W_{F_0}| ≤ 2×10^{−6}(92.66 + 10^{−5}) < 1.86×10^{−4}`, so `\sqrt{W/2} ≥ G(1 − 6.6×10^{−6})`. Then
`s ≤ (s_1 + 5.4×10^{−7})(1 + 6.7×10^{−6}) ≤ s_1 + 8×10^{−6}`. Finally
`1 − 0.998469² = 3.0597×10^{−3}`. ∎

At `χ = 0`, `d = 400` the window becomes `(0.998469²·80000, 79800) = (79755.2, 79800)`, which still contains `79780`.

## 6. The frame defect theorem on the small domain

**Theorem 6.1 (Theorem 19.25 on `C_c^∞ ⊕ RK`; `PROVED`, unconditional given (X19)).** Let `𝒟 ∈ \{𝒟_c, 𝒟_p\}`. There is
**no** `h⁰ : 𝒟 → R_{≥0}` satisfying (a)_𝒟, (b′)_𝒟, (c)_𝒟, for any `χ ∈ R`. The same holds with (b′) replaced by its
stable form (b′)_{st} of Theorem 19.12.

More precisely (**localised form**, `PROVED`). Fix `χ`, and let `F := F_R` (for `𝒟_c`) or `F := F_R^♭` (for `𝒟_p`).
Take `d > 1` with `d²(1 − s_F²) > d − 4χ` and `t` as in (2.1). Put `E_w := tF + dK`. On **any** set `𝒟 ⊆ D^W` containing
the two classes `E_w` and `K − E_w`, no `h⁰ ≥ 0` satisfies (b′) at `E_w` and at `K − E_w` together with (c) at `E_w`.

*Proof.* `E_w ∈ 𝒟_p ⊆ 𝒟_c`, and `K − E_w = −tF + (1−d)K` lies there too (Lemma 1.2(i)). Suppose `h⁰` satisfies the
clauses.
*Step 1 at `K − E_w`.* We have `\deg(K−E_w) = 1 − d < 0` (Theorem 11.13(iv), `\deg K = 1`). If `h⁰(K−E_w) > 0`, then
(b′) gives `E' ≥ 0`, `E' ≢ 0` with `\deg E' = 1 − d < 0` (Theorem 11.13(ii),(iv)). That contradicts Theorem 11.13(i).
So `h⁰(K − E_w) = 0`.
*Step 2.* By (c) at `E_w`, `h⁰(E_w) ≥ R(E_w) − h⁰(K − E_w) = R(E_w)`. Serre symmetry is not needed, as `R155_054` noted.
Proposition 2.1 gives `R(E_w) > 0`.
*Step 3.* Then `h⁰(E_w) > 0`, so (b′) at `E_w` supplies `E'`, which Proposition 2.1 forbids. For (b′)_{st} the multiple
`N` cancels (Proposition 2.1, last sentence). The required `F` exists by Lemma 4.1 or Lemma 5.1. ∎
**[amended per R156_003, A9: the **existence** of a suitable `R` needs only `S_2 < ∞`, which is (E3d) with
`|ρ−½| ≥ |γ_ρ|`, because `C_{D_R} ≤ N(D_R) + S_2N(D_R'') → 0`. So Theorem 6.1 is `PROVED` given (X19), (E2), (E3d),
exactly P47's inputs for Theorem 19.25. The Davenport import of Lemma 3.2 enters only the **explicit** `R_0` and the
explicit constants of Lemmas 4.1 and 5.1.]**

**Consequence of record.** *Residual R1 of `R155_057` is closed: Theorem 19.25 holds with `h⁰` defined only on
`C_c^∞ ⊕ RK`, and also on `P_c^∞ ⊕ RK = \mathrm{span}\,𝒢_min`, verbatim. The witness class `E_w = tF_R + dK` is
compactly supported up to the multiple of `K`, and at `χ = 0` it lives at degree `d ≥ 326`.* The definition-free
small-domain kill of D-HS (`R155_054` Corollary 1, (Ev-1)) no longer rests on the reading-dependent Lemma 3 of
`R155_054`, and it needs no new certified constant. `R155_054`'s remark that "it re-enters the computer-assisted layer
through `s_1`, `L`" (l.56) is true only in the weak sense that Lemma 19.20(v),(vi) are **cited**. Nothing is
re-certified. `PROVED`.

**Corollary 6.2 (the same over number fields and for Theorem 19.28; `PROVED` modulo the per-field (X19)-analogue, as
P47 Theorem 19.28).** §§2–6 use only (U1)–(U4), Lemma 3.1 (whose proof transports with `\deg_K`, the weight
`2\cosh(u/2)` in the normalisation of Theorem 19.28, and `S_2^{(K)} < ∞`, which follows from the zero count for `ξ_K`),
and the Gaussian tails. So the truncation works for `ξ_K` whenever Theorem 19.28 does. The explicit `R_0` depends on
`S_2^{(K)}` and on the per-field margin `1 − s_1^{(K)}`. That dependence is logarithmic in `S_2^{(K)}`; it is **not**
computed here.
**[amended per R156_003, A3: "`S_2^{(K)} < ∞`, which follows from the zero count for `ξ_K`" is false when `ξ_K(½) = 0`.
That happens for some number fields (Armitage, *Invent. Math.* 15 (1972), 199–205), and then the term at `ρ = ½` is
`|ρ−½|^{−2} = ∞`. Repair: at a zero with `ρ = ½` use `|Φ_F(1−ρ)| = |Φ_F(½)| ≤ N(F)` in place of (11.2). This gives
Lemma 3.1(ii) in the form `C_F ≤ (1 + m_{1/2})N(F) + S_2^{′}N(F'')`, where `m_{1/2}` is the multiplicity of `½` and
`S_2^{′} := Σ_{ρ≠½}|ρ−½|^{−2} < ∞`. The rest of §§2–6 is unchanged. For `ξ` itself, `ξ(½) ≠ 0` and every zero has
`|γ| > 14` (X19), so nothing changes. Note also that `\deg_K F = Φ_F(0) + Φ_F(1)` (P47:5343), so its weight is again the
even function `2\cosh(u/2)` and an even cutoff keeps `\deg_K F_R = 0` exactly.]**

## 7. Side finding: the bare set `𝒢_min` is too small, and this is why the domain must be linear

**Proposition 7.1 (`PROVED`; a sharpening of P47 §19.9's first paragraph).** For `h⁰` defined only on the set `𝒢_min`,
with clauses (a),(b′),(c) restricted to it, the hypothesis of Theorem 12.3 is **satisfiable if and only if RH holds**.
The frame defect theorem therefore does not act on `𝒢_min`. It needs a domain containing classes of degree
`> d_0 ≈ 325` (Theorem 6.1: `E_w` and `K − E_w`).
**[amended per R156_003, A2: the last two sentences are to be read as follows. "No unconditional non-existence
theorem for `h⁰` on `𝒢_min` can be proved unless RH is false. The kill of Theorem 6.1 uses the pair `\{E_w, K−E_w\}`,
of degrees `d > d_0^{(R)}` and `1−d`." It is **not** proved that every domain admitting a kill contains classes of degree
`> 325`. Here "satisfiable" means that some pair `(h⁰, χ)` exists, as in (12.1), where `χ` is existential.]**

*Proof.* ⇐: assume RH. Then `I_∞(F,F) = −Σ_ρ|Φ_F(ρ)|² ≤ 0` for `F ∈ P_c^∞` (11.6). Take `h⁰ ≡ 0` and `χ = 0`.
(a) holds, and (b′) holds vacuously. For (c) at `E = nF` or `E = K − nF`,
`R(E) = R(nF) = ½n²I_∞(F,F) ≤ 0` (Serre symmetry, `\deg F = 0`). At `n = 0`, `R(0) = R(K) = 0`. ⇒: Lemma 1.2(ii),
i.e. Theorem 12.3 on `𝒢_min`. ∎

So "the minimal domain `𝒢_min`" of `R155_054:50` / `R155_057:52` must be read as its **linear span** `𝒟_p`, or as any
domain containing the high-degree pair `\{E_w, K − E_w\}`. On `𝒢_min` itself, Theorem 12.3 is RH restated, and no `h⁰`
can be "killed" there without deciding RH. This does not favour D-HS: D-HS needs the growth `h⁰(mK) ≳ m²/4` (its test T2),
so its domain contains `mK` for large `m` and is in any case larger than `𝒢_min`. **This is the degree gap of Horn A**
(P47 §19.9: the load-bearing degrees are `0` and `1`, while the witnesses live at `d ≥ d_*`), seen from the domain side.
`DIAGNOSTIC`.

## 8. Remarks on the other residuals

**Remark 8.1 (R2 = Horn B, P47 §19.9, Theorem 19.30, B4; remark only).** Theorem 19.30's proof uses (U1)–(U4) with `C`
replaced by `C'`. So on `𝒟_c` its conclusion holds with `F_R` in place of `F_0`: a cone `𝓔'` satisfying
(T1_cone),(T2_cone) can support the small-domain transfer only if `C'_{F_R} ≥ \sqrt{W_{F_R}/2} ≥ G(1 − 3.3×10^{−6})`
(`PROVED`, same proof). Truncation neither closes nor reopens R2. The bridge `C'_{F_0} ↔ C'_{F_R}` needs `C'_{D_R}` small,
and for a general cone `𝓔'` the quantity `C'_{D_R}` is not controlled by `C_{D_R}`: (T2_cone) gives finiteness, not size.
The B4 row ("the whole witness family lies in B4", P47 §19.9 table) was computed for `F_0`. For `F_R` the traces
`t_n(F_R)` would have to be recomputed. That is `OPEN`, and it does not matter: B4 **passes** Theorem 19.30, so no
refutation is at stake, and the status "`(b′)_{B4}` ⟺ RH" (`R155_057:263-266`) does not depend on which witness is used.

**Remark 8.2 (Horn A's primitivity caveat; `PROVED` existence, `DIAGNOSTIC` consequence).** P47 §19.9 records that in
Horn A "`F_0` is not primitive, so the gate must be taken by primitive test classes". Lemma 5.1 supplies a primitive,
compactly supported, odd test class `F_R^♭` with `s_{F_R^♭} ≤ s_1 + 8×10^{−6}`. The primitivity caveat is thereby
discharged at no cost in the constant. Horn A's binding obstacle (the sufficiency half of the moment problem) is untouched.
**[amended per R156_003, A8: primitivity alone needs no truncation. `F_0 − ηB` with `B` as in §5 already lies in
`P^W`, and its `s` is `≤ s_1 + O(10^{−389})`. What Lemma 5.1 adds is **compact support together with** primitivity. The
caveat of P47 §19.9 is about which classes the gate may test. Supplying a primitive witness meets that requirement as an
existence statement. It does not touch the gated-candidate argument itself.]**

**Remark 8.3 (the curve, Theorem 21.15: no R1 there; `PROVED` from P47 Theorem 21.8).** In the model,
`D^W_C/𝓝^C_∞` is `(2+2g)`-dimensional, and the evaluation map is onto already from the `δ_m` (Theorem 21.8's proof,
P47:8554–8556: "the same independence makes the evaluation map onto"). So every class, including the witness of
Theorem 21.14, has a **finitely supported** representative modulo `𝓝^C_∞`, and (b′) is read modulo `𝓝^C_∞`. The
small-domain question is empty on the curve. Arithmetically `𝓝_∞ ∩ 𝒟_c = 0` (Lemma 1.2(iii)), so the replacement must be
analytic, as in §4, and not modulo the radical.

**Remark 8.4 (the constant `s_*` is a `C_c^∞` constant; `PROVED`).** For every real `F ∈ D^W` with `\deg F = 0` and
`W_F > 0` there are real `F_k ∈ C_c^∞`, `\deg F_k = 0`, with `s_{F_k} → s_F`. If `F ∈ P^W`, the `F_k` can be taken in
`P_c^∞`. Hence the infimum `s_*` of P47 §19.9 may be taken over `C_c^∞` (resp. `P_c^∞`) without change.
*Proof.* First truncate: `F_R := Fϑ_R`. It is `C²` with compact support, and by (11.1) for `j ≤ 2` together with
`|ϑ_R^{(j)}| ≤ A`, both `N(F − F_R)` and `N((F − F_R)'')` tend to `0`. Next mollify with an even `φ_δ`: on the fixed
compact support `N ≤ 2\cosh(R+1)\|·\|_{L¹}`, and `(F_R ⋆ φ_δ)'' = F_R'' ⋆ φ_δ → F_R''` in `L¹`. Then correct, with `B_1, B_2 ∈ C_c^∞` fixed and having
`(Φ(0),Φ(1))`-images `(1,1)` and `(1,−1)` (for `B_2` take `B` of §5; for `B_1` any even bump, normalised). In the
degree-only case subtract `λB_1` with `λ := ½\deg` of the approximant. In the primitive case subtract `λB_1 + μB_2`,
solving for `Φ(0) = Φ(1) = 0`. The
coefficients are bounded by `N` of the error, by Lemma 3.1(iv). By Lemma 3.1(i)–(iii), `C` and `W` then converge, and
`W_F > 0` makes `s = C/\sqrt{W/2}` continuous at `F`. ∎

## Statement list

| # | statement | label |
|---|---|---|
| 1.2 | `𝒟_c, 𝒟_p` `σ_K`-stable; `𝒟_p = \mathrm{span}\,𝒢_min`; Thm 12.3 runs on them; `𝓝_∞ ∩ 𝒟_c = 0` | PROVED |
| §2 | the proof of Thm 19.25 uses of `F_0` only (U1)–(U4); the only exact identity is `\deg F = 0` | PROVED (by inspection of P47 §19.6–19.7) |
| 2.1 | abstract witness: (U1)–(U4) ⟹ `E = tF + dK` is in `S_χ` and has no nonnegative representative (stable form too) | PROVED |
| 3.1 | `C_F ≤ N(F) + S_2N(F'')`; `|I_∞(E,F)| ≤ C_F N(E)` for all `E`; `C` subadditive | PROVED |
| 3.2 | `S_2 ≤ 0.0465` (Davenport import), or `< 0.41` (P47's own count) | PROVED given import |
| 4.1 | truncation: `F_R ∈ C_c^∞` odd, `\deg F_R = 0` exactly, `C_{D_R} ≤ 10^{−6}` for `R ≥ 6\sqrt{40+2\log A}`, `s_{F_R} < 0.998464`, `d_0 < 325.78` | PROVED given (X19) |
| 5.1 | primitive version `F_R^♭ ∈ P_c^∞`, `s ≤ 0.998469`, `d_0 < 326.9` | PROVED given (X19) |
| 6.1 | Thm 19.25 (and stable form) on `C_c^∞ ⊕ RK` and on `P_c^∞ ⊕ RK`; localised to the pair `\{E_w, K−E_w\}` | PROVED given (X19), (E2), (E3d) [amended per R156_003, A9: explicit constants additionally use Lemma 3.2] |
| 6.2 | same for `ξ_K` wherever Thm 19.28 applies; `R_0` not computed | PROVED modulo per-field (X19) [amended per R156_003, A3: with the `ρ = ½` repair of Lemma 3.1(ii)] |
| 7.1 | on the bare set `𝒢_min`: hypothesis of Thm 12.3 satisfiable ⟺ RH | PROVED [amended per R156_003, A2: new, elementary; the "degree `≥ 326` needed" gloss withdrawn] |
| §7 end | this is Horn A's degree gap seen from the domain side | DIAGNOSTIC |
| 8.1 | Thm 19.30 on `𝒟_c` with `F_R`; R2 unchanged; B4 traces at `F_R` | PROVED / OPEN (not needed) |
| 8.2 | Horn A primitivity caveat discharged | PROVED / DIAGNOSTIC |
| 8.3 | curve: no R1 (finitely supported representatives mod `𝓝^C_∞`) | PROVED (from Thm 21.8) |
| 8.4 | `s_*` unchanged over `C_c^∞` / `P_c^∞` | PROVED |
| — | whether `F_0` is `𝓝_∞`-equivalent to an element of `𝒟_c` | OPEN (not needed) |
| — | sign typo `±2η²` in Lemma 19.20(v) | DIAGNOSTIC (size `< 10^{−780}`) |

## For the auditor

1. **[amended per R156_003, A5: the proofs are at P47:6209–6351 (Lemma 19.20 at 6209, Thm 19.21 at 6252, Thm 19.23 at
   6292, Cor 19.24 at 6320, Thm 19.25 at 6332–6351); 6356–6455 is Remarks 19.26–19.27, Thm 19.28, §19.8.]**
   **(U1)–(U4) are exhaustive.** Check P47:6356–6455 for any use of `F_0` other than `\deg F_0 = 0`, `W_{F_0} > 0` and
   the ratio `C_{F_0}/\sqrt{W_{F_0}/2}`. In particular, check that Theorem 19.23's use of `W_{F_0} = 2G²(1±10^{−90})` is
   only through `s_F`.
2. **Lemma 3.1(iii) for non-effective `E`.** It rests on Theorem 11.14(i) (absolute convergence of `∫E w_F` for
   every `E ∈ D^W`) and on `C_F` being the **exact** supremum. Lemma 19.20(vi) bounds the exact constant, not only
   (11.17). Confirm this.
3. **(11.2) at `s = 1 − ρ`.** P47 states (11.2) "uniformly in closed substrips". I use only the pointwise inequality
   `|Φ_g(s)| ≤ |s−½|^{−2}∫|g''|e^{(σ−½)t}`, which is the two integrations by parts, valid at every `s` in the strip
   where `g ∈ D^W`.
4. **`S_2`.** Lemma 3.2 imports the Davenport identity `Σ\mathrm{Re}(1/ρ) = 1 + γ_E/2 − ½\log4π`, a new classical import
   not in P47's list. The alternative route uses P47's own count `≤ \log T` per unit interval for `T ≥ 21`. I doubt that
   count is provable from Trudgian-type explicit bounds for moderate `T` (for `T ≲ 5000` it needs the zero list).
   That is P47's input for Lemma 19.20(iv), not mine; it is flagged, not used. Only `S_2 ≤ 1` is load-bearing.
5. **The cutoff constant `A`.** `R_0` is explicit **given** `ϑ`. I did not certify `\|ϑ'\|_∞, \|ϑ''\|_∞` for a named
   cutoff. For the standard `f/(f+f)` step with `f = e^{−1/x}`, `|ϑ'| = 2` at the midpoint, and I expect `A ≤ 10³`,
   i.e. `R ≥ 45`. That is not load-bearing.
6. **Proposition 7.1** says the audit's phrase "minimal domain `𝒢_min`" is literally too small: there, Thm 12.3's
   hypothesis is RH itself. Decide whether R1 should be recorded as closed "on `C_c^∞ ⊕ RK` and on `\mathrm{span}\,𝒢_min`"
   (my wording), and whether 7.1 is new or already implicit in P47 §19.9's first paragraph. My view is that it is
   implicit there, and I label it a sharpening.
7. **(b′)_𝒟 reading.** Representatives are taken in `D^W`. If they must lie in `𝒟`, the hypothesis is stronger and
   Theorem 6.1 still applies. Check that no reading makes it **weaker**, e.g. equivalence modulo a smaller radical
   `𝓝_∞ ∩ 𝒟 = 0`. Under that reading `E − E' = 0`, so `E'` would have to equal `E_w`, which is even more constrained;
   the kill holds.
8. **Remark 8.4** (density of `C_c^∞` for `s`). The degree-only correction uses only `B_1` (`\deg B_1 = 2`). Check that
   the `\deg`-only case does not accidentally require primitivity. An even bump `B_1 ≥ 0` has `Φ(0) = Φ(1) > 0`, so
   normalising gives `(1,1)`.
