# Round 001 D — Moment criteria for the representing measure of B

## Object
B(d) = a(F_0, V_d F_0) (STATEMENT_001.md §2). If (★) holds, B = μ̂ for a finite positive measure μ
(Bochner). The candidate (C5 of the ledger) was to decide positivity of μ from the moments of B at
d = 0, by a determinacy argument (Carleman).

## Corpus check
Moment rigidity appears in Paper 22 for a different measure; moment barriers for the window form in
Paper 47 (W-mom); the Kreĭn extension form thm:KEP1–3. No entry treats the germ of B at d = 0.

## Proposition 1 (PROVED). The germ of B at 0 does not see the comb.
For |d| < log 2 − 2T_0 the comb part of B(d), namely −½Σ_n v_n[c_0(log n − d) + c_0(log n + d)],
vanishes: c_0 is supported in [−2T_0, 2T_0] and |log n ± d| > 2T_0 for every n ≥ 2. Hence on that
interval B(d) = (1/2π)∫ m F̂_0² cos(τd) dτ, the same function for Λ, for cΛ (any c) and for a_P (any P).
In particular every moment of μ that exists (for the standard profile, orders ≤ 2 only, since
F̂_0² ≍ τ^{−4}) is comb-free. ∎

## Proposition 2 (PROVED, given the CITED falsifiers of Paper 47). No criterion that uses only the
germ of B at 0, or only moments of μ, can decide the sign.
The germ is identical for Λ, cΛ and a_P (Proposition 1), while (★) holds for Λ on the certified range
and fails for a_P with P > e^{2T} at T ≥ 0.60 and for cΛ, c ≠ 1, at explicit windows (Paper 47
prop:shape-eulerdel, lem:shape-scale). A criterion depending on the germ alone would give the same
verdict for all three. ∎

## Remark (what is not claimed)
Whether the Hamburger moment problem of μ is determinate is not decided here and is not relevant: by
Proposition 2 it could not carry the sign. For the standard profile only two moments exist; for smoother
profiles thm:oneprofile is not available as stated. Carleman's criterion can in any case not be
verified for compactly supported profiles (Denjoy–Carleman), which says nothing about indeterminacy.

## Result
NO-GO with class: criteria depending only on the germ of B at 0 (moments of the representing measure).
What was proved: Propositions 1–2. What failed: the moments do not see the comb. Next concrete step: none on
this object.
