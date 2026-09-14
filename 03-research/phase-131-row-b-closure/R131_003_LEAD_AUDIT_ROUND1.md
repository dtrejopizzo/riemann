# R131.003 — Lead audit of the phase-131 build of Paper 44 (round 1)

Author: session lead (Fable 5.1). Date: 2026-09-12. Independent of the
hostile audit R131.002.

## 1. Re-derived and found correct

| statement | check |
|---|---|
| Lemma 3bis.1 | `φ(a_S(n)) = n`, class `(1/n; 1,…,1)`; ✓ |
| Prop 3bis.2 (`|S_f| ≥ 2`) | `j_q(q^kw)` has `q^{−k}` at `r ≠ q`; equality forces `k=0` then modulus 1; ✓. Neighbourhood basis argument ✓ |
| Cor 3bis.3 | ✓; `w_unit` is a lift quantity |
| Def 3bis.4, Thm 3bis.5 | Haar-coset convolution ✓; `†` ✓; `M = (n^{1/2},n^{−1/2})` ✓; chart pushforward ✓. The builder's correction to average over `K^♮ = {±1}×∏Z_p^×` is right (the sign is needed for the half-sum in 3bis.8) |
| Lemma 3bis.6a, Thm 3bis.7 | shell sum `(log p)p^{−k/2}[h(k log p)+h(−k log p)]`; unit packet zero on radial sections (constant on `Z_p^×`); archimedean kernel `¼[1/|sinh(t/2)|+1/cosh(t/2)] = K(|t|)` consistent with Paper 43 (9.12a) at `ε=0` ✓; colimit via Thm 8A.7c ✓ |
| Def–Thm 3bis.8 | `½[n^{1/2}/(n−1)+n^{1/2}/(n+1)] = n^{3/2}/(n²−1) = K(log n) = n^{−1/2}Σn^{−2j}` ✓ (lead's own computation) |
| Thm 3bis.10 | `Σ_{d|n}Λ(d) = log n`; degrees match ✓ |
| Thm 6.3a, Thm 6.5 | ✓ as degree statements; Rem 6.5a's "dictionary" flag is the right honesty |
| Thm 8.3 | `\widehat{Γ_n^{rad}} = n^{iτ}` on `𝔠_0` ✓; `|Δ_ε| ≤ min(2, |τ|ε)`; `R`-then-`ε` argument gives strong-dual convergence ✓; components ✓ |
| §7 second table | numerics reproduced by `scripts/verify_131_contacts.py` (ALL CHECKS PASS, re-run by the lead) |
| §9, §9bis | the dissolution of the `n−1` obligation is correct and honestly recorded |

## 2. Findings

**F1 (MAJOR, internal inconsistency) — Theorem 8.1(iii), proof.**  The
statement of (iii) was corrected in phase 128 (the family IS separated by the
ruling plane), but the *proof* still reads: "for the second, if `Λ(n)` were a
function of the ruling data it would be a function of `n`, hence determined by
`log n`, but `Λ(4)=Λ(8)` with `log 4 ≠ log 8` shows the level sets differ, so
`Λ` is not pulled back from the ruling plane" — the exact backwards inference
D128.002 B1 refuted. Rewrite the proof of (iii): `M(Γ_n^{rad}) = (n^{1/2},
n^{−1/2})` determines `n`, hence `Λ(n)`; nothing more is to be proved.
Likewise (iv)'s proof still cites Theorem 3.3(iii) and the `q | p^k−1` places
as the answer to Remark 9.5, contradicting the rebuilt statement (iv) and
§9bis W3. Rewrite the proof to cite Theorem 3bis.7.

**F2 (MINOR) — §10 verdict block** has a duplicated line ("confirming that no
clause is a renaming …" twice).

**F3 (NOTE) — `|S_f| = 1`.**  Proposition 3bis.2 assumes `|S_f| ≥ 2`. Add the
remark: for `S_f = {p}` and `n = p^k`, `δ_S(1/n) = j_p(p^k·1)` **does** lie on
the shell, but the element point class still has finite contact `0`, because
the shell term integrates `F∘j_p` against the probability Haar measure of
`Z_p^×` and a point mass at `u = 1` has measure zero; only the unit-spread
(ideal) class receives the shell volume. This makes the dichotomy
element/ideal independent of `|S_f|`.

**F4 (NOTE) — Remark 3bis.4b / Thm 3bis.5(i).**  "Strong monoidal functor to
the convolution monoid of measures" — fine; but say once that on the smeared
level (`Γ_h`, Lemma 3bis.6a) monoidality is inside `D_A^{rad} ⊂ Corr_A^{tr}`,
so clause B.2's "realization into row A's category" is satisfied literally on
the smeared classes and in the completion `N_A^{dist}` on the point classes.

**F5 (decision for the owner) — the B.4 amendment.**  Text proposed by the
builder in §6.2a′ is faithful to the mathematics: the literal clause is false
(P123.060, P123.022), the amended clause is a degree identity in the declared
category, proved (Thm 6.3a). The lead recommends acceptance, on the same
grounds as A.6: it makes the clause say what can be proved on a `C`-linear
carrier, and names the object (the ideal class) the clause was about.

## 3. Renaming test (lead's view, final after R131.002)

`T(Γ_h)` is the geometric side of the explicit formula. Row B's content is:
(a) the family is realized as ideal classes with composition, dagger,
bidegree — objects, not numbers; (b) `Λ` is derived as a shell volume;
(c) the element/ideal distinction and the dissolution of the `n−1` artifact;
(d) the degree matching with the integral cube; (e) membership in `N_A^{dist}`
with canonical components. None of these is a statement the explicit formula
makes. Not a renaming.
