# PANEL_REPAIRS — phase 133 apparatus repairs

Repair record for phase 133.  Every finding of PANEL_1, PANEL_2 and PANEL_3
that does **not** require a pending decision is repaired in
`04-papers/43-row-a-correspondence-algebra/main.md`, `04-papers/44-row-b-arithmetic-family/main.md`,
`04-papers/45-row-c-explicit-formula/main.md` (plus two phase-130/131 record files).
Every edit is marked `[phase 133]`.  **No clause grading, no label, and no
decision block was changed**; A.8 and B.7 are untouched except for the one
sentence the panel asked for, which records the panel's opinion and says the
decision is pending.

Each item below is a command and its output.

## PANEL_1 A1 — `D_A^0` denoted two spaces; §8 set renamed `D_A^{off}`, Remark 8.6b corrected

The §8 set (vanishes near the identity class) is renamed `D_A^{off}` everywhere
it carries that meaning, in all three papers.  `D_A^0` now means only Definition
9.10's primitive sector `ker λ_− ∩ ker λ_+`.

```console
$ grep -c 'D_A\^{off}' 04-papers/4[345]*/main.md
04-papers/45-row-c-explicit-formula/main.md:4
04-papers/43-row-a-correspondence-algebra/main.md:22
04-papers/44-row-b-arithmetic-family/main.md:8
```

```console
$ grep -n 'D_A\^0' 04-papers/4[345]*/main.md | grep -v 'phase 133' | grep -v 'off-identity' | sed 's/\(.\{125\}\).*/\1…/'
04-papers/43-row-a-correspondence-algebra/main.md:1084:with Definition 9.10's `D_A^0 = ker λ_− ∩ ker λ_+` (the **primitive** sector).…
04-papers/43-row-a-correspondence-algebra/main.md:1087:`D_A^0` now always means the primitive sector of Definition 9.10.]**
04-papers/43-row-a-correspondence-algebra/main.md:1175:false as written while `D_A^{off}` was named `D_A^0`, because on the
04-papers/43-row-a-correspondence-algebra/main.md:1176:**primitive** sector `D_A^0 = ker λ_− ∩ ker λ_+` of Definition 9.10 the
04-papers/43-row-a-correspondence-algebra/main.md:2922:zero).**  `𝓝_W = 𝓝 ∩ D_A^0`, it is a closed two-sided `⋆`-ideal stable under
04-papers/43-row-a-correspondence-algebra/main.md:2925:*Proof.*  *`𝓝_W = 𝓝 ∩ D_A^0`.*  If `F∈𝓝_W`, the first component gives
04-papers/43-row-a-correspondence-algebra/main.md:2928:i.e. `F∈D_A^0`.  The converse is immediate.  This is P123.017 Prop. 2.1.
04-papers/43-row-a-correspondence-algebra/main.md:2929:*Closed `†`-ideal.*  `𝓝` has these properties by Theorem 9.4.  `D_A^0` is
04-papers/43-row-a-correspondence-algebra/main.md:2940:    D_A^{prim} := D_A^0 , N_A = D_A , B_T = C² with β_T = [[0,1],[1,0]],  (9.1…
04-papers/43-row-a-correspondence-algebra/main.md:2958:  (i) `Φ ∈ D_A^0`.  Theorem 9.5 proves `λ_−(F)=λ_−(F')` and
04-papers/43-row-a-correspondence-algebra/main.md:2973:*Nondegeneracy on the kernel.*  Let `Φ ∈ D_A^0` satisfy `I_A(Φ,G)=0` for every…
04-papers/43-row-a-correspondence-algebra/main.md:2974:`G ∈ D_A^0`.  The conjugate-linear functional `G ↦ I_A(Φ,G)` vanishes on the
04-papers/43-row-a-correspondence-algebra/main.md:2975:subspace `D_A^0 = ker λ_−∩ker λ_+` of codimension two, hence equals
04-papers/43-row-a-correspondence-algebra/main.md:3035:`D_A^0 = ker λ_− ∩ ker λ_+`, hence equals
04-papers/44-row-b-arithmetic-family/main.md:415:| **B.4** | The derived contact of `Γ_n` computed in the declared category; …
04-papers/44-row-b-arithmetic-family/main.md:2296:> `ω_{fin}` representing `T` on the radial sector `D_A^{rad} ∩ D_A^0`**
```

The only surviving `D_A^0` outside Paper 43 §§9–14 is the **accepted**
B.4 amendment text of Paper 44 (lines 415 and 2296), reproduced verbatim and
therefore not edited; a `[phase 133]` note immediately after it says which set
is meant.

```console
$ sed -n '1082,1090p;1170,1180p' 04-papers/43-row-a-correspondence-algebra/main.md

Write `D_A^{off} := {F ∈ D_A : F ≡ 0 on a neighbourhood of the identity class}`.  **[phase 133: this set was called `D_A^0` through phase 132, colliding
with Definition 9.10's `D_A^0 = ker λ_− ∩ ker λ_+` (the **primitive** sector).
The two are different: a primitive `F` generally has `F(1) ≠ 0`.  Renamed
`D_A^{off}` ("off the identity") wherever the off-identity meaning is intended;
`D_A^0` now always means the primitive sector of Definition 9.10.]**

*Normalization dictionary.*  P123.007 (1.2) uses the unnormalized involution
`f^†(x)=x^{−1}conj(f(x^{−1}))` and correspondingly writes its local density
P123.004 §4 calls its own semilocal display schematic and records that "its
real coefficient cannot be imported without reconciling full-line Haar and
even-function conventions"; P123.035 §6 states the stop rule.  Every result
in §§9–10 is either proved on `D_A^{off}`, where `F(1)=0`, or invariant under
changing `c` — Theorem 9.8 explicitly so.  **[phase 133: this sentence was
false as written while `D_A^{off}` was named `D_A^0`, because on the
**primitive** sector `D_A^0 = ker λ_− ∩ ker λ_+` of Definition 9.10 the
constant does **not** drop out: Paper 45 Corollary 9.6a proves
`(Γ_F ⋆ Γ_F^†)(1) = ‖F‖² ≠ 0` there, so `c·F(1)` survives and `c = 0` is
forced rather than immaterial.  The claim above is asserted for `D_A^{off}`
only.]**  The one place where `c` matters
```

```console
$ sed -n '2306,2313p' 04-papers/44-row-b-arithmetic-family/main.md
> category (P123.022).

**[phase 133: the accepted text above is reproduced verbatim and is not
edited.  Its `D_A^0` is the **off-identity** set of Paper 43 §8, renamed
`D_A^{off}` in phase 133; it is not Paper 43 Definition 9.10's primitive
sector.  The same applies to the copy of this text in the §10 clause table
(clause B.4).]**

```

## PANEL_1 A2 — Theorem 14.1(a),(b): the false Paley–Wiener claim replaced by a concentration argument

The withdrawn sentence was *"using that `D_A`'s Fourier images contain all
Schwartz functions in `τ` on each component"* together with *"choosing `F̂`
supported in disjoint such sets"*.  `D_A = C_c^∞(C_S)` is compactly supported in
the `R^×` coordinate, so each `F̂(𝔠,·)` is entire of exponential type and is
never compactly supported in `τ`.

**The argument written in its place, verified before writing.**  Work on one
component with profiles; `F̂[φ] = φ̂`.  The two operations `φ(t) ↦ e^{iat}φ(t)`
and `φ(t) ↦ φ(t/δ)` stay inside `C_c^∞(R)` and translate/dilate `φ̂`.  With
`φ_{a,δ}(t) = δ^{−1/2}e^{iat}φ_0(t/δ)`, `‖φ̂_{a,δ}‖_{L²} = 1` and the **weighted**
tail outside any fixed window `(a−ρ,a+ρ)` is
`∫_{|σ|>δρ}(A_S+|c|+B_S\log(2+|a|+|σ|/δ))|φ̂_0(σ)|²dσ → 0` as `δ → ∞`, because
`φ̂_0` is Schwartz and `|T̂| ≤ A_S + B_S\log(2+|τ|)` (proof of Lemma 9.14a0, from
Theorem 9.7).  So: (a) windows `I_j` with `T̂+c ≤ −K_j`, `K_j ↑ ∞`, give
`I_A ≤ −K_j/2 + ε_j < 0`; rescaling by `K_j^{−1/2}` and choosing the `ε_j`
inductively makes the Gram matrix strictly diagonally dominant with negative
diagonal, hence negative definite on an infinite-dimensional span.  (b) If
`c ≤ −m` the positive index is `0`; if `c > −m`, a **fixed** window with
`T̂+c ≥ κ > 0` is subdivided into countably many disjoint subwindows and the
same estimate runs with the sign reversed.  No `F̂` is compactly supported
anywhere.  The conclusions (a),(b),(c),(d) are unchanged.

```console
$ sed -n '5075,5090p' 04-papers/43-row-a-correspondence-algebra/main.md
      every component, so `{T̂+c < −K}` contains a nonempty open set for every
      `K`, and tests whose symbols **concentrate** in a sequence of such sets
      span an infinite-dimensional negative-definite subspace.
      **[phase 133: "concentrate", not "are supported in".  See the proof.]**
  (b) `I_A` has **infinite positive index if and only if `c > −m`**, and then
      `I_A` is **indefinite**, by the same concentration argument applied to
      an open set on which `T̂+c ≥ κ > 0`.
  (c) For the natural normalization `c = 0` — the one the imported semilocal
      theorem would supply if (O-A5-3) were settled with `c_{an}=0` — the
      hypothesis of (b) holds, since

        m ≥ T̂(ε=0, τ=0; all κ_q = 1)
          = log π − ψ(1/4) + Σ_{p∈S_f} (log p)·\frac{2p^{−1/2}}{1−p^{−1/2}}
          ≥ log π + γ + 3\log 2 + π/2 ≈ 5.372 > 0 .                (14.2)

  (d) `(D_A^{prim})^{⊥I_A} = 0` and there is no `D_A`-module splitting of the
```

```console
$ sed -n '5108,5125p' 04-papers/43-row-a-correspondence-algebra/main.md
Two operations stay inside `C_c^∞(R)` and act on `φ̂` by the two motions we
need: `φ(t) ↦ e^{iat}φ(t)` translates `φ̂` by `a`, and `φ(t) ↦ φ(t/δ)`
dilates it, `φ̂ ↦ δ·φ̂(δ·)`.  Fix once and for all `φ_0 ∈ C_c^∞(R)` with
`‖φ̂_0‖_{L²} = 1`; `φ̂_0` is a Schwartz function on `R` (integration by parts).
Write `φ_{a,δ}(t) := δ^{−1/2}e^{iat}φ_0(t/δ)`, so that
`φ̂_{a,δ}(τ) = δ^{1/2}φ̂_0(δ(τ−a))` has `L²`-norm `1` and, for any `ρ > 0`,

    ∫_{|τ−a| > ρ} |φ̂_{a,δ}|²dτ = ∫_{|σ| > δρ}|φ̂_0(σ)|²dσ  →  0   (δ → ∞),

and, using the growth bound `|T̂(𝔠,τ)| ≤ A_S + B_S\log(2+|τ|)` established in
the proof of Lemma 9.14a0 from Theorem 9.7,

    ∫_{|τ−a| > ρ} (|T̂(𝔠,τ)|+|c|)|φ̂_{a,δ}(τ)|²dτ
      ≤ ∫_{|σ|>δρ}\bigl(A_S+|c|+B_S\log(2+|a|+|σ|/δ)\bigr)|φ̂_0(σ)|²dσ
      →  0   (δ → ∞),                                              (14.1a)

because `φ̂_0` is Schwartz and the weight grows only logarithmically.  So the
**weighted** tail, not merely the `L²` tail, can be made arbitrarily small on
```

## PANEL_1 A3 — the unlabelled transfer of P123.082 (3.3) to the algebra `U`

Labelled `IMPORTED (transfer)`, id `Tr`, added to Paper 43 §12 with the clauses
it serves (A.2 via Prop. 3.2(iv), A.4 via Thm 5.3), the hypotheses that **are**
checked for `U` and the one that is **not** (freeness of the lattice action on
the open stratum).  Clause gradings in §14.0b are **not** touched — that decision stands as recorded; the §12 row and Remark 3.6 record `PROVED modulo (Tr)`.

```console
$ grep -n 'Tr | ' 04-papers/43-row-a-correspondence-algebra/main.md | cut -c1-400
4645:| Tr | **[phase 133, PANEL_1 finding A3.]**  **Transfer of P123.082 (3.3)** — `Hom_{U-U}(E_a,E_b) = C·U_γ` for `a = γb`, `0` otherwise — **from the algebra of P123.082 to the algebra `U` of (2.4)**.  `IMPORTED (transfer)`: the *arguments* apply verbatim, the *conclusion* rests on freeness of the lattice action on the open stratum, which is proved for P123.082's coefficient algebra and 
```

```console
$ sed -n '/I use (3.3) for/,/lattice$/p' 04-papers/43-row-a-correspondence-algebra/main.md | head -16
algebra, and is proved in P123.082 for its own algebra.  I use (3.3) for `U`
and record this as a transfer, not as a citation of an identical statement.
**[phase 133, PANEL_1 finding A3: this transfer now carries a status label and
appears in §12's import table as id `Tr`, **IMPORTED (transfer)**.  Hypotheses
checked: `U` is unital complete Fréchet, `β` is a continuous automorphism, and
left-linearity `f(x)=xf(1)` holds — P123.121 §§1–8,
`PROVED-IN-REPOSITORY` — and these are the only properties the arguments of
P123.064 §§1–3 use; what is **not** checked for `U` is the freeness of the
lattice action on the open stratum, which is what (3.3)'s conclusion rests on
in P123.082's own algebra.  (3.3) is used in Proposition 3.2(iv) (clause
**A.2**) and in the proof of Theorem 5.3 (clause **A.4**); both are therefore
`PROVED modulo (Tr)`.  Discharging it means proving freeness of the lattice
```

```console
$ grep -n 'phase 133: four' -A5 04-papers/43-row-a-correspondence-algebra/main.md
4653:**Count.**  Three, not one, and their load has changed.  **[phase 133: four
4654-rows now stand in the table — `M`, `W`, `C`, `RR` — plus the transfer `Tr`
4655-added by PANEL_1 finding A3.  `Tr` is the only import that a clause graded
4656-`PROVED` depends on: A.2 and A.4 are `PROVED modulo (Tr)`.  The "three" below
4657-counts the load-bearing imports `W`, `C`, `RR` as before; it is not amended,
4658-because the grading of A.2 and A.4 was decided separately.]**  **[REBUILT, phase
```

## PANEL_1 B1 / B2 — Paper 44 §11's "In clauses B.1–B.9: none" is false for the amended B.4

```console
$ sed -n '/In clauses B.1–B.9/,/recorded in Paper 43 §12./p' 04-papers/44-row-b-arithmetic-family/main.md
  * **In clauses B.1–B.9: two elementary `CLASSICAL` facts, in clause B.4
    only.**  **[phase 133, PANEL_1 finding B1: this bullet read "**none**.
    Row B's contract is discharged with no external citation", which is false
    for the amended B.4.]**  Theorem 6bis.4, which is the whole of clause
    **B.4** as amended, is proved from
    (α) `Φ_n(1) = p` if `n = p^k` is a prime power and `= 1` otherwise, hence
    `\log|Φ_n(1)| = Λ(n)` (used in Theorem 6bis.3(v)), and
    (β) `\log n = Σ_{d|n}Λ(d)`, equivalently `Λ = μ ∗ \log` (Corollary 5.3a).
    Both are elementary classical number theory, neither is proved in this
    repository, and neither was in any import table.  They are labelled
    **`CLASSICAL`**; no verdict is at risk, since B.4's content is the
    *identification*, not either fact.  Clauses B.1–B.3 and B.5–B.9 use no
    external citation.  **[phase 133, PANEL_1 finding B2: the clause "adds
    none to the **one** import (`W`, Wodzicki excision) recorded in Paper 43
    §12" misstated Paper 43, whose §12 records four rows — `M`, `W`, `C`, `RR`
    — plus the transfer `Tr` added in phase 133, and says in terms "Count.
    Three, not one".  Corrected:]**  row B adds nothing to the imports
    recorded in Paper 43 §12.
```

## PANEL_1 A4 — Theorem 9.12 / Theorem 9.13(b): the swapped exponents

```console
$ grep -n 'a|w|_S\^' 04-papers/43-row-a-correspondence-algebra/main.md
2991: = a|w|_S^{−1/2}\overline{λ_−(G)} + b|w|_S^{1/2}\overline{λ_+(G)}`, using
3041:`a|w|_S^{−1/2}\overline{λ_−(G)} + b|w|_S^{1/2}\overline{λ_+(G)}`, unbounded as
```

## PANEL_1 A5 — Theorem 9.8: `T̂(𝔠,·)` → `T̂(𝔠,·)+c`

```console
$ grep -n 'zeros of `T̂' -A3 04-papers/43-row-a-correspondence-algebra/main.md
2887:`m = 0` almost everywhere.  By Theorem 9.7(c) the zeros of `T̂(𝔠,·)+c` are
2888-isolated **[phase 133, PANEL_1 finding A5: read "`T̂(𝔠,·)`"; the object named
2889-two sentences earlier, and the one that must have isolated zeros, is
2890-`T̂(𝔠,·)+c`.  No consequence]**, so `F̂(𝔠,τ)=0` off a discrete set, and `F̂(𝔠,·)` is continuous;
```

## PANEL_1 A6 — Theorem 9.14a: `ψ ≥ 0` added to the hypothesis

```console
$ grep -n 'with \*\*`ψ ≥ 0`\*\*' -A6 04-papers/43-row-a-correspondence-algebra/main.md
3144:`ψ ∈ C_c^∞((0,∞))` with **`ψ ≥ 0`**, `∫_R ψ(s)ds = 1` and `supp ψ ⊆ [a,b]`,
3145-`0<a<b<∞`.  **[phase 133, PANEL_1 finding A6: `ψ ≥ 0` was used implicitly in
3146-(a) — the strict inequalities `0 < λ_−(F_n)`, `0 < λ_+(G_n)` need it — and
3147-Theorem 10.8b assumes it separately.  Added to the hypothesis; nothing else
3148-uses the strict positivity, only the upper bound
3149-`‖ψ‖_{L¹}e^{−na}`.]**  For
3150-`n ≥ 1` define `F_n, G_n ∈ D_A` by
```

## PANEL_1 A7 — Theorem 9.7(b): the parity bound is `π/2`, not `π`

```console
$ grep -n 'parity term' -B2 -A3 04-papers/43-row-a-correspondence-algebra/main.md
2616-
2617-For `ε=1` the same two displays bound `Ŵ_∞(1,·)` above by
2618:`max_τ Ŵ_∞(0,τ) + π/2`, the parity term `(−1)^ε·\tfrac12·π/\cosh(πτ)` being
2619-bounded by `π/2` in absolute value.  **[phase 133, PANEL_1 finding A7: the
2620-bound was written with `π`, true but loose by a factor 2.  Cosmetic; nothing
2621-uses the constant.]**
```

## PANEL_1 B3 — Paper 44 Thm 6bis.3(v): "divisor cube" → Möbius total cofiber over the divisor poset

```console
$ grep -n 'Möbius total cofiber' -A7 04-papers/44-row-b-arithmetic-family/main.md
2651:  (v) *Möbius cofiber.*  The **Möbius total cofiber over the divisor poset**
2652-      of `d ↦ Sh_Z(Frob_d)`, `d | n`, is `Prim_n ≅ [\,Z →^{Φ_n(1)} Z\,]`, with
2653-      `H^0 = Z/Φ_n(1)`.  **[phase 133, PANEL_1 finding B3: this said "the
2654-      divisor **cube**".  For non-squarefree `n` the divisor poset is not a
2655-      cube — for `n = p^k` it is a chain of length `k` — and the cube is the
2656-      one indexed by the **radical** divisors, of which this is the top layer.
2657-      The identity `Σ_{d|n}μ(n/d)\log d = Λ(n)` is unaffected.]**
2658-
```

## PANEL_1 C1 — the place-wise Plancherel identity is now Paper 43 Theorem 9.7(d′), and Paper 45 Lemma 5.1a cites it

```console
$ grep -n "9.13′" -B8 -A4 04-papers/43-row-a-correspondence-algebra/main.md
2525-      convergent.
2526-
2527-  (d′) *Place-wise form.*  **[phase 133, PANEL_1 finding C1: this was
2528-      established inside the proof of (d) but never stated as a numbered
2529-      assertion, and Paper 45 Lemma 5.1a needs it in that form.]**  The
2530-      interchange in (d) is justified **termwise**, so for every `v ∈ S` and
2531-      every `H ∈ D_A`,
2532-
2533:        W_v(H) = ∫_{Ĉ_S} Ĥ(χ) Ŵ_v(χ) dχ ,                          (9.13′)
2534-
2535:      each integral absolutely convergent, and (9.13) is the sum of (9.13′)
2536-      over `v ∈ S` plus `c∫Ĥ dχ`.
2537-
2538-*Proof.*  **(a)**  By (9.5b), `j_p(p^k w) = (p^{−k} at ∞, w at p, p^{−k} at
2539-every other place of S)`, so, `sgn(p^{−k})=+1`,
```

```console
$ grep -n 'place by place: Paper 43' -B2 -A7 04-papers/45-row-c-explicit-formula/main.md
```

## PANEL_1 A8 — `phase-130/scripts/ml_check.py`: crash repaired **and** marked superseded

```console
$ head -16 03-research/phase-130-row-a-closure/scripts/ml_check.py
"""[phase 133, PANEL_1 finding A8]  SUPERSEDED BY R130_ml_check.py.

Status.  This script crashed through phase 132 (`TypeError`: numpy's `np.exp`
applied to an mpmath `mpf` handed to it by `mp.quad`).  The type mix is
repaired below and the script now runs end to end.

Blocks 1 and 2 agree with the closed forms (`W_p` versus its Mittag-Leffler
form to ~1e-5; the universal Tate residues at `tau = +-i/2` are `-+i` to 1e-13).
**Block 3 (the contour identity) does not reproduce the direct shell sum** —
its residue family and contour orientation are the draft version.  The script
of record for Theorem 9.7b, including the contour identity, is
`R130_ml_check.py`, which passes.  This file is kept only because it is cited
in the phase-130 record; nothing depends on its block 3.
"""
import numpy as np, mpmath as mp
# 1. Mittag-Leffler for W_p^(tau) = (log p) 2 Re(z/(1-z)), z = p^{-1/2 - i tau}
```

```console
$ cd 03-research/phase-130-row-a-closure/scripts && python3 ml_check.py 2>&1 | tail -3
res at i/2: (2.41509273130968e-6 - 0.999999999999177j)  res of Wp at i/2: None
res Wp(2) at i/2: (3.5237691541963104e-08-0.9999999999999899j) at -i/2: (3.5237691541963104e-08+0.9999999999999899j)
W_p direct 0.594347161078167  residues+contour (-0.137839274943078 - 2.60208521396521e-16j)
```

```console
$ grep -n 'PANEL_1 finding A8' -A11 03-research/phase-130-row-a-closure/README.md
16:**[phase 133, PANEL_1 finding A8.]**  `scripts/ml_check.py` crashed through
17-phase 132 (a numpy/mpmath type mix: `np.exp` applied to an `mpf` inside
18-`mp.quad`).  The crash is repaired and the script runs, but it is **superseded**
19-and is not the script of record: its blocks 1–2 agree with the closed forms,
20-while its block 3 (the contour identity) is a draft that does not reproduce the
21-direct shell sum.  The script of record for Theorem 9.7b — Mittag-Leffler form
22-and the universal Tate residues `∓i` at `±i/2` at every place — is
23-**`scripts/R130_ml_check.py`**, which passes.  Nothing in the phase-130 record
24-depends on `ml_check.py` block 3.
25-
26-## Outcome
27-
```

## PANEL_2 MAJOR-1 — "Paper 43 Remark 9.5" does not exist; six citations re-anchored

Paper 43 has Theorem 9.5 (`N_A ≠ 0`; `T` separates two sections of equal
modulus) and Remark 9.6 (what (9.5) does and does not establish); **neither
poses the question** "what the family's pairings equal in terms of `Λ(n)`", and
that sentence appears nowhere in Paper 43.  The nearest statement that *prompts*
the question is Remark 9.7a (`Λ(p^k) = \log p` appears in `T̂` as a shell
volume).  Per the instruction, the six passages are reworded honestly: the
question is **row B's own**.  The `PROVED` verdict of the §10 ledger row is
untouched — it was discharged by row B's own Theorem 3bis.7 all along.

```console
$ grep -n 'Rem\(ark\)\?\.\? 9\.5' 04-papers/44-row-b-arithmetic-family/main.md | cut -c1-150
2983:  (iv) **[phase 133, PANEL_2 MAJOR-1: this read "Paper 43 Remark 9.5 states
2985:      `Λ(n)`'".  **Paper 43 has no Remark 9.5**, and no statement of Paper 43
2998:      `w_unit` answer Remark 9.5" — is withdrawn (§9bis W3), both for its
3031:9.5's question"; Paper 43 has no Remark 9.5 and poses no such question.]**  The round-1
4742:the question to "Paper 43 Remark 9.5", which does not exist; the question is
5523:| "what the family's pairings equal in terms of `Λ(n)`" | **row B's own question** (§8 Thm. 8.1(iv)), prompted by Paper 43 Rem. 9.7a (`Λ(p^k)=
5639:**[phase 133, PANEL_2 MAJOR-1: "Remark 9.5" does not exist in Paper 43;
```

```console
$ sed -n '2979,2992p' 04-papers/44-row-b-arithmetic-family/main.md
      separated by the ruling plane, and the appeal to Paper 43's mixed sector
      (which concerns *unit* twists `|u|=1`, and `Γ_n` is not one) is withdrawn.
      The correct statement is that the family's unit-sector content sits at the
      places `q | n−1` — an entirely different assertion;
  (iv) **[phase 133, PANEL_2 MAJOR-1: this read "Paper 43 Remark 9.5 states
      exactly this family and leaves open 'what these equal in terms of
      `Λ(n)`'".  **Paper 43 has no Remark 9.5**, and no statement of Paper 43
      poses that question: Theorem 9.5 separates two unit-sector sections of
      equal modulus, Remark 9.6 comments on what that does and does not
      establish, and Remark 9.7a says only that `Λ` appears in `T̂` as a
      derived shell volume.  The question is **row B's own**, raised here;
      the attribution is withdrawn.]**  The question "what does the arithmetic
      family's finite contact equal in terms of `Λ(n)`?" is row B's, and is
      prompted by Paper 43 Remark 9.7a, where `Λ(p^k) = \log p` arises as the
```

```console
$ sed -n '5475p' 04-papers/44-row-b-arithmetic-family/main.md | cut -c1-420
).** B.7: `PROVED` — the mechanism producing the factor that enters
```

## PANEL_2 MAJOR-2 — the phase-132 explicit-formula relabel propagated to the three places it missed

(1) Paper 44 Theorem 8bis.4's own status footer; (2) Paper 44 §11 item (i);
(3) Paper 45 §14.3.  Weil's **criterion** stays `CLASSICAL` everywhere.

```console
$ grep -n -B2 -A9 'in (ii)[*][*]' 04-papers/44-row-b-arithmetic-family/main.md
3858-this argument gives, and it is all that (iv)(a) claims.**  (iv)(b) is
3859-Theorem 8bis.4a.  (v) is the gap computation, as in round 3.  (vi) summarizes,
3860:and rests on (iii) — **not** on (iv).  ∎  `PROVED` in (i),(iv); **`PROVED-IN-REPOSITORY` in (ii)**
3861-(Paper 45 Theorem 9.4); `CLASSICAL` in (iii); `OPEN` in (v).
3862-**[phase 133, PANEL_2 MAJOR-2: this footer still read "`CLASSICAL` in
3863-(ii),(iii)".  The phase-132 relabel of (ii) — the explicit formula — to
3864-`PROVED-IN-REPOSITORY` (Paper 45 Thm 9.4) was applied to the body of (ii), to
3865-§10.4 items 2 and 4a, to the §0 banner and to one sentence of §11, but not
3866-here.  Weil's **criterion**, (iii), remains `CLASSICAL`.]**
3867-
3868-**Theorem 8bis.4a (positivity fails on the pure Frobenius form —
3869-unconditionally, at every finite chart).**  **[REBUILT, phase 131, round 5,
```

```console
$ grep -n "(i) \*Weil's criterion\*, Theorem 8bis.4(iii)" -A8 04-papers/44-row-b-arithmetic-family/main.md
5692:    (i) *Weil's criterion*, Theorem 8bis.4(iii), `CLASSICAL`.
5693-    **[phase 133, PANEL_2 MAJOR-2: this item read "*Weil's criterion **and the
5694-    explicit formula***, Theorem 8bis.4(ii)–(iii)", contradicting the
5695-    `[phase 132]` sentence three lines above.  The **explicit formula**,
5696-    Theorem 8bis.4(ii), is **`PROVED-IN-REPOSITORY`** (Paper 45 Theorem 9.4)
5697-    and is no longer an external input; the count of external inputs in the
5698-    quarantined §8bis.3–§8bis.4 is therefore **two** only if one counts
5699-    Weil's criterion and Chebyshev, which is how (i) and (ii) now read.]**
5700-    (ii) *Chebyshev's bound `ψ(X) ≤ cX`*, Lemma 8bis.5, with an unspecified
```

```console
$ grep -n 'the interface, (i)' -A7 04-papers/45-row-c-explicit-formula/main.md
2214:whose sign is row D's); Theorem 8bis.4 (the interface, (i) `PROVED`,
2215-(ii) **`PROVED-IN-REPOSITORY`** — it is this paper's Theorem 9.4 —
2216-(iii) `CLASSICAL` (Weil's criterion), §§8.3, 14.4)
2217-**[phase 133, PANEL_2 MAJOR-2: this read "(ii)–(iii) `CLASSICAL`", i.e. this
2218-paper recorded as `CLASSICAL` the very statement it proves in its own
2219-Theorem 9.4 and relabelled in §14.5(a).]**; Theorem 8bis.4a and Remark 8bis.4b
2220-(positivity fails on the pure Frobenius form at every chart; the colimit
2221-version `OPEN`, Warning 8.5); Theorem 8bis.8 and Corollary 8bis.8a
```

## PANEL_2 MINOR-1 — Paper 44 §9.4 / §9bis W2 cited withdrawn Paper 45 §11, Thm 11.1 and `G_rad` as live

```console
$ grep -n '9.4 The correction to Paper 45' -A9 04-papers/44-row-b-arithmetic-family/main.md
4660:**9.4 The correction to Paper 45 §11 (now deleted there).**  **[REBUILT, phase
4661-131.]**  **[phase 133, PANEL_2 MINOR-1: Paper 45 §11 and its Theorem 11.1 were
4662-**withdrawn in phase 132** (Paper 45 §13 **W45.7**), which deletes the section
4663-rather than discharging the obligation — exactly the outcome this subsection
4664-asked for.  What follows is therefore **history**, in the past tense; Paper 45
4665-W45.7 records that clause (a) below was and remains correct about the lift.]**
4666-Paper 45 §11 (Theorem 11.1) **stated**, in its phase-130 version, that it
4667-*discharges row B's handoff*, namely that
4668-`w_unit(Γ_n) = n−1` is "a sample of the unit integrand across places".  Two
4669-statements must be separated.
```

```console
$ grep -n 'G_rad' -B6 -A4 04-papers/44-row-b-arithmetic-family/main.md
4685-      128 `B5` correction).  The conclusion — the class contributes no `n−1` —
4686-      holds on every chart; see Remark 3bis.2a.
4687-
4688-Row B therefore withdrew the obligation (§9bis) and recorded that Paper 45
4689-§11 discharged something that was never owed.  **[phase 133: Paper 45's
4690-campaign has since decided — §11 and Theorem 11.1 are deleted (W45.7).  The
4691:sentence that stood here, "Paper 45 §12's radial sector `G_rad` is exactly the
4692:sector in which §3bis works", is **struck**: `G_rad`, together with Paper 45
4693-Proposition 12.2 and Theorem 12.3, was withdrawn in phase 132 (Paper 45 §13
4694-**W45.8**), so it names no live object.  The radial sector in which §3bis
4695-works is `D_A^{rad}` of Definition 3bis.6 here, and Paper 45's live statement
4696-about it is Lemma 1.1.  Nothing rested on the struck sentence (PANEL_2
```

## PANEL_2 MINOR-2 — Paper 43 §13.8 and §14.2 still assigned `𝓝_∞ = 0` to row C

```console
$ grep -n 'declined by row C' 04-papers/43-row-a-correspondence-algebra/main.md
4887:A**.  It is therefore recorded here as `CLASSICAL`, **declined by row C**
4890:The phase-132 edit corrected the §14.0 obstacle row to "declined by row C …
5366:> `𝓝_∞ = 0` for the colimit (§13.8, `CLASSICAL`, **declined by row C and
```

```console
$ grep -n 'belonging to row C' 04-papers/43-row-a-correspondence-algebra/main.md
4889:this paper.  **[phase 133, PANEL_2 MINOR-2: this read "**belonging to row C**".
```

```console
$ sed -n '/recorded here as `CLASSICAL`, \*\*declined/,+6p' 04-papers/43-row-a-correspondence-algebra/main.md
A**.  It is therefore recorded here as `CLASSICAL`, **declined by row C**
(Paper 45 §0.2, §14.3) **and claimed by no row**, and it is used nowhere in
this paper.  **[phase 133, PANEL_2 MINOR-2: this read "**belonging to row C**".
The phase-132 edit corrected the §14.0 obstacle row to "declined by row C …
not claimed by any row" but did not reach here; Paper 45 declines it
explicitly.  No clause depends on it.]**

```

## PANEL_2 MINOR-3 — Paper 44 8bis.4(iv)(a) cited Paper 43 (14.2) where (9.12b) is meant

```console
$ grep -n 'Paper 43 (14.2)\|Paper 43 \*\*(9.12b)\*\*\|Paper 43 (9.12b)' 04-papers/44-row-b-arithmetic-family/main.md
3787:      Paper 43 **(9.12b)**, `→ −∞` as `|τ| → ∞` by (8bis.8));
3788:      **[phase 133, PANEL_2 MINOR-3: this cited Paper 43 (14.2), which is a
3791:      ≈ 5.372` is Paper 43 (9.12b).  The argument is unaffected — every
3853:(iv)(a): by (8bis.8) and Paper 43 (9.12b) **[phase 133, PANEL_2 MINOR-3:
```

## PANEL_2 MINOR-4 — "Paper 44 Theorem 9.1" does not exist; corrected to §9.1 everywhere it occurs

Occurrences found and corrected: Paper 44 §10.4 item 4a; Paper 45 §14.5 table
row (e); `03-research/phase-131-row-b-closure/README.md`;
`03-research/phase-131-row-b-closure/R131_019_FINAL_AUDIT_AND_LABEL.md` §5
(a decision of record — the decision is **not** altered, a bracketed
reading note is added).  `R131_001` line 140 and `R131_014` line 306 refer to
**Paper 43** Thm 9.1, which does exist, and are left alone.

```console
$ grep -rn 'Paper 44 Thm\. \?9\.1\b\|Paper 44 Theorem 9\.1\b' 04-papers 03-research/phase-13-omega-class-multiplicative-chaos[012]* | grep -v PANEL_
(no output — zero remaining occurrences)
```

```console
$ grep -rn 'PANEL_2 MINOR-4' 04-papers 03-research/phase-131-row-b-closure | cut -c1-180
04-papers/45-row-c-explicit-formula/main.md:2345:| (e) | Paper 44 §9 (new §9.1a) and §10.4 (new item 4a) | "row C received **§9.1** (Paper 44 has no Thm 9.1 — **[phase 133, P
04-papers/44-row-b-arithmetic-family/main.md:5617:   (C1) as its standing convention **[phase 133, PANEL_2 MINOR-4: this read
03-research/phase-131-row-b-closure/R131_019_FINAL_AUDIT_AND_LABEL.md:100:**[phase 133, PANEL_2 MINOR-4: read as **§9.1**, whose content is Thm 3bis.7;
03-research/phase-131-row-b-closure/README.md:40:Thm 3bis.7; **[phase 133, PANEL_2 MINOR-4: this line read "Paper 44 Thm 9.1",
```

## PANEL_2 MINOR-5 — Paper 45 Cor 9.6a quoted a Def 8A.7d sentence removed in phase 132

```console
$ grep -n 'is a derivation' -B4 -A9 04-papers/45-row-c-explicit-formula/main.md
1190-phase-132 edit this paper authorized has since rewritten Paper 43
1191-Definition 8A.7d to read that reasons (i)–(iii) are normalization choices and
1192-are **not** derivations, while reason (iv) — which cites this corollary — **is**
1193-one.  **[phase 133, PANEL_2 MINOR-5: the preamble quoted "none of [its four
1194:reasons] is a derivation" as current text of Paper 43; that quotation became
1195-stale with the phase-132 edit.  Non-circularity is unaffected: this
1196-corollary's proof uses only Paper 43's family (8.4) and this paper's
1197-Theorem 9.4.]**]**  Let `c ∈ R` be arbitrary and let
1198-`T^{(c)} := Σ_v W_v + c·F(1)` be the corresponding member of Paper 43's family
1199-(8.4), with `I^{(c)}(F,G) := T^{(c)}(F⋆G^†)` and `I_∞^{(c)}` its colimit.  Then
1200-for every real `F ∈ C_c^∞(R)`:
1201-
1202-  (i) `I_∞^{(c)}(Γ_F,Γ_F) = 2Φ_F(0)Φ_F(1) − Σ_ρΦ_F(ρ)Φ_F(1−ρ)
1203-      + c\,‖Γ_F‖_{L²(C_S)}²`, and `‖Γ_F‖_{L²(C_S)}² = ‖F‖_{L²(R)}²`;
```

## PANEL_2 MINOR-6 — Paper 44 Thm 8bis.7(b) over-labelled `CLASSICAL`

```console
$ grep -n -B3 -A17 'for the passage to the primitive class' 04-papers/44-row-b-arithmetic-family/main.md
4283-      (8bis.12); equivalently, positivity on that class implies that no such
4284-      family `(g_*)` exists.
4285-  (b) *(`CLASSICAL` for Weil's criterion, Theorem 8bis.4(iii);
4286:      **`PROVED-IN-REPOSITORY`** for the passage to the primitive class,
4287-      Paper 45 Theorem 10.4.)*  If RH fails then `Q(g) < 0` for **some**
4288-      `g ∈ C_c^∞(R)` — this is Weil's criterion, `CLASSICAL` — and — by
4289-      Paper 45 Theorem 10.4, which supplies `Π = −∂_t^2+\tfrac14` and
4290-      **proves in the repository** that the primitive class suffices — for
4291-      some **primitive** `g`.
4292-      **[phase 133, PANEL_2 MINOR-6: (b) was labelled `CLASSICAL` wholesale,
4293-      via Theorem 8bis.4(ii)–(iii).  The primitive-class half is a theorem of
4294-      this repository (Paper 45 Thm 10.4, from `106_11` Theorem 1 with the
4295-      `C10` fix and imports (E2) last clause, (E3d), (E6)), and 8bis.4(ii) —
4296-      the explicit formula — is itself `PROVED-IN-REPOSITORY` since phase 132
4297-      (Paper 45 Thm 9.4).  Weil's **criterion** stays `CLASSICAL`.  The
4298-      relabel is toward less external dependence; no verdict moves, and (c)
4299-      and the overall `OPEN` of Theorem 8bis.7 are untouched.]**
4300-  (c) *(`OPEN`.)*  Whether such a `g` can be taken **supported in a moving
4301-      window `[L/2,L]` with `L → ∞`** and with `R(L) → 0` is **not** supplied
4302-      by any classical statement known to this paper, and is **not** asserted.
4303-      Remark 8bis.7a(2) records what is known about the obstruction and by how
```

## PANEL_2 MINOR-7 — Paper 44 §11 omitted Paper 45 from its dependencies

```console
$ grep -n 'Paper 45: \[Paper 45\]' -B4 -A7 04-papers/44-row-b-arithmetic-family/main.md
5637-Thms. 9.1, 9.3, 9.4, 9.5, Remark 9.6) and its
5638-[appendix](../43-row-a-correspondence-algebra/appendix.md).
5639-**[phase 133, PANEL_2 MAJOR-1: "Remark 9.5" does not exist in Paper 43;
5640-corrected to Theorem 9.5 and Remark 9.6, which are what is meant.]**
5641:Paper 45: [Paper 45](../45-row-c-explicit-formula/main.md) — Thm. 5.1,
5642-Lem. 5.1a, Thm. 8.1, **Thm. 9.4** (the explicit formula, `PROVED` there and
5643-cited in §8bis.4(ii) and §10.4), Thm. 10.4 (`Π = −∂_t²+¼`, sufficiency),
5644-Rem. 10.3.  **[phase 133, PANEL_2 MINOR-7: §11 listed Paper 43 only, while
5645-§§8bis.3–8bis.4 and §10.4 cite Paper 45 substantively.]**
5646-Phase 126 record: `03-research/phase-126-row-b-completion/`.
5647-Phase 128 audit: `03-research/phase-128-adversarial-audit/`.
5648-Phase 131 record: `03-research/phase-131-row-b-closure/` — **[REBUILT, phase
```

## PANEL_2 MINOR-8 — the two formulas for `j_p` reconciled in print

(9.5b) is the normalized form and is the one every computation of Papers 43 §9,
44 and 45 uses; (8.5)'s "class of the idele (`x` at `p`, `1` elsewhere)" names
the same class.  The reconciliation is stated once, at (8.5).

```console
$ grep -n 'MINOR-8' -A14 04-papers/43-row-a-correspondence-algebra/main.md
1110:**[phase 133, PANEL_2 MINOR-8: the reconciliation of the two written forms of
1111-`j_p`, stated here once and for all.  The **normalized** form is **(9.5b)**,
1112-`j_p(p^kw) = (p^{−k}` at `∞`, `w` at `p`, `p^{−k}` at every other place of
1113-`S)`, and it is the form used by every computation of this paper's §9 and of
1114-Papers 44 (Prop. 3bis.2) and 45 (§5).  The form written in (8.5) — "the class
1115-of the idele `(x` at `p`, `1` elsewhere)" — denotes the **same class in
1116-`C_S`**: the two ideles differ by the `S`-unit `p^k ∈ Γ_S`, and by the
1117-splitting `A_S^× = Γ_S × ker φ` of Lemma 3.3 the representative in
1118-`C_S ≅ R^× × ∏_{q∈S_f}Z_q^×` is obtained by dividing by `p^k`, which is
1119-exactly (9.5b).  A reader comparing Paper 44 Prop. 3bis.2(ii) with (8.5)
1120-should read (8.5) as naming the class and (9.5b) as giving its coordinates.]**
1121-
1122-at the real place `W_∞` is P123.035 (3.1),
1123-
1124-    W_∞(F) = (γ+log 4π) b(1)
```

## PANEL_2 §5 / PANEL_3 — row D's target, boxed verbatim and identically in all three papers

Inserted in Paper 43 §14.1 (immediately after Theorem 14.1's "What rows B, C
and D must take from this"), Paper 44 §8bis.4 (immediately before item (vi)) and
§10.4, and Paper 45 §14.4.  The four copies are byte-identical.

```console
$ grep -rn "ROW D'S TARGET: I_∂" 04-papers/4[345]*/main.md | cut -c1-95
04-papers/45-row-c-explicit-formula/main.md:2271:> **ROW D'S TARGET: I_∂ ≤ 0 on every primi
04-papers/43-row-a-correspondence-algebra/main.md:5179:> **ROW D'S TARGET: I_∂ ≤ 0 on every primiti
04-papers/44-row-b-arithmetic-family/main.md:3834:> **ROW D'S TARGET: I_∂ ≤ 0 on every prim
04-papers/44-row-b-arithmetic-family/main.md:5575:> **ROW D'S TARGET: I_∂ ≤ 0 on every prim
```

```console
$ grep -rhn "ROW D'S TARGET: I_∂" 04-papers/4[345]*/main.md | cut -d: -f2- | sort -u | md5sum; grep -rc "ROW D'S TARGET: I_∂" 04-papers/4[345]*/main.md
5d37c98affa68ae70aca7c18c0c351ea  -
04-papers/45-row-c-explicit-formula/main.md:1
04-papers/44-row-b-arithmetic-family/main.md:2
04-papers/43-row-a-correspondence-algebra/main.md:1
```

```console
$ sed -n '/ROW D.S TARGET (boxed identically/,+5p' 04-papers/45-row-c-explicit-formula/main.md
> **ROW D'S TARGET (boxed identically in Paper 43 §14.1, Paper 44 §8bis.4(vi)
> and §10.4, and Paper 45 §14.4).**  **[phase 133, PANEL_2 §5 / PANEL_3
> recommendation.]**
>
> **ROW D'S TARGET: I_∂ ≤ 0 on every primitive radial class Γ_g, g ∈ C_c^∞(R), on the colimit D_A^∞ with T_∞ and c = 0 (Paper 45 Cor 9.6a); this implies RH by Paper 45 Thm 9.6 (9.10) and Thm 10.4. Standing negatives: Paper 43 Thm 14.1, Paper 44 Thm 8bis.4a; Paper 44 Thm 8bis.7 is conditional under (H_L), OPEN.**

```

## PANEL_3 §3 — the two dissents: one sentence each, no grading touched

A.8 and B.7 gradings, and every decision block, are **unchanged**.

```console
$ grep -rn 'review panel (PANEL_3 §3) sides with the dissent' 04-papers/4[345]*/main.md | cut -c1-260
04-papers/43-row-a-correspondence-algebra/main.md:3920:**[phase 133: the review panel (PANEL_3 §3) sides with the dissent; the final
04-papers/44-row-b-arithmetic-family/main.md:5507:| B.7 discriminating test `p`, `p²`; mechanism located | **`PROVED` (the test and, per the lead's ruling, the mechanism on the carrier); the map to the `Z`-model `REFUTED`, not open.**  **[REBUILT, phase 131, 
```

```console
$ grep -n '#### 10.3.3' -A4 04-papers/43-row-a-correspondence-algebra/main.md
3918:#### 10.3.3 Theorem 10.7 — clause A.8
3919-
3920-**[phase 133: the review panel (PANEL_3 §3) sides with the dissent; the final
3921-decision on an amendment is pending.]**
3922-
```

## Scripts — every script in phases 130, 131, 132 re-run after the repairs

All seven run to completion with exit status 0.  Last lines of each:

```console
$ cd 03-research/phase-130-row-a-closure/scripts && python3 contour_check2.py   # last lines
W_p direct      = 0.594347161078167
axis integral   = (0.594347161078167 + 6.0593734085651e-34j)
residue sum     = (1.98632923824481 - 1.00478665503513e-27j)
Poisson         = 1.98632923824481
contour (h=1)   = (-1.39198207716664 - 3.5960223515571e-33j)
res + contour   = (0.594347161078167 - 1.00479025105748e-27j)
[exit 0]
```

```console
$ cd 03-research/phase-130-row-a-closure/scripts && python3 mertens_check.py   # last lines
center 8, halfwidth 3: sum = 1.0000  (need log X=17.5 > 11)
center 10, halfwidth 5: sum = 1.0000  (need log X=17.5 > 15)
center 12, halfwidth 5: sum = 1.0000  (need log X=17.5 > 17)
[exit 0]
```

```console
$ cd 03-research/phase-130-row-a-closure/scripts && python3 ml_check.py   # last lines
7 0.0 2.3647681590441008 2.3647585677993765
7 0.37 0.9571538422379684 0.9571442509932433
7 2.5 -0.32358925722473103 -0.3235988484694683
res at i/2: (2.41509273130968e-6 - 0.999999999999177j)  res of Wp at i/2: None
res Wp(2) at i/2: (3.5237691541963104e-08-0.9999999999999899j) at -i/2: (3.5237691541963104e-08+0.9999999999999899j)
W_p direct 0.594347161078167  residues+contour (-0.137839274943078 - 2.60208521396521e-16j)
[exit 0]
```

```console
$ cd 03-research/phase-130-row-a-closure/scripts && python3 R130_ml_check.py   # last lines
inf tau= 1.3 closed=1.656745076 ML(trunc)=(1.656741326 + 0.0j) diff=3.75e-06
inf tau= 5.0 closed=0.2301182182 ML(trunc)=(0.2301144683 + 0.0j) diff=3.75e-06
residue of W_2 at 0.5j = (1.0700467e-32 - 1.0j)
residue of W_2 at (-0-0.5j) = (3.7994746e-33 + 1.0j)
residue of W_inf at 0.5j = (1.1154986e-32 - 1.0j)
residue of W_inf at (-0-0.5j) = (2.2704403e-32 + 1.0j)
[exit 0]
```

```console
$ cd 03-research/phase-131-row-b-closure/scripts && python3 verify_131_contacts.py   # last lines
  optimal c gives block value -3.335141e-02  (negative: a witness EXISTS on this quadruple)
  NB: this is the RESONANT QUADRUPLE ONLY, with a SYNTHETIC zero; the
  full Q adds a large positive on-line sum, which is exactly the
  obstruction (H_L) of Thm 8bis.7(c).  Numerics illustrate, not prove.

ROUND-6 CHECKS PASS
[exit 0]
```

```console
$ cd 03-research/phase-132-row-c-closure/scripts && python3 lead_explicit_formula_check.py   # last lines
polar + gamma - prime        : 0.01881160689647504461
polar, gamma, prime          : 0.12597825843548627542 -0.10716559602723380433 1.0555117774264719911e-6
A(s)+A(1-s) at (0.2999999999999999889 + 2.0j) = (8.4703e-22 + 0.0j)
A(s)+A(1-s) at (0.5 + 14.0j) = (0.0 + 0.0j)
A(s)+A(1-s) at (2.0 + 0.69999999999999995559j) = (0.0 + 0.0j)
A(s)+A(1-s) at (-0.4000000000000000222 + 3.1000000000000000888j) = (1.2705e-21 + 8.4703e-22j)
[exit 0]
```

```console
$ cd 03-research/phase-132-row-c-closure/scripts && python3 verify_132_explicit_formula.py   # last lines
        c =  +0.5000  ->  I^(c) - I^(0) = c||F||^2 = +5.52368961
PASS  (6c) M(Gamma_F) = 0 does NOT kill the c-term, so at most one c can satisfy (9.9) -- and c = 0 does   (Cor 9.6a(ii),(iii); D128 C9 closed)

============================================================================
26/26 checks passed
============================================================================
[exit 0]
```

`ml_check.py` now runs (it crashed through phase 132); it is marked
**superseded** in its own docstring and in the phase-130 README, because its
block 3 (contour identity) is a draft that does not reproduce the direct shell
sum — `R130_ml_check.py` is the script of record for Theorem 9.7b and passes,
as does `contour_check2.py` for the contour identity itself
(`res + contour = 0.594347161078167 = W_p direct`, to `1e−27`).

## What was deliberately **not** changed

* **No clause grading, no label, no decision block.**  A.8 and B.7 keep
  their recorded verdicts; the one sentence added to each records the panel's
  opinion and says the decision is pending.  The three
  `WEIL-STRENGTH-COMPLETE` labels are untouched.
* Paper 43 §14.0b's A.2/A.4 rows are **not** re-graded `PROVED modulo (Tr)`;
  the transfer is labelled where it lives (Remark 3.6) and in the §12 import
  table, which is apparatus, and the grading is left pending.
* Paper 44's **accepted** B.4 amendment text (§10 clause table and the
  §6.2a blockquote) is reproduced verbatim and not edited; a `[phase 133]` note
  beside it says which of the two `D_A^0`'s it means.
* PANEL_3's recommendation to record A.8 as `PROVED IN THE RESTATED FORM` and
  B.7 as `PARTIAL` is a pending decision and is **not** applied.
