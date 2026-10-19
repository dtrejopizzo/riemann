# Paper 43 — Row A: the Weil-strength correspondence theory on the graph sector, and the torsion invariant

> **Status,— repaired after adversarial audit; see [REPAIRS.md](REPAIRS.md).**
> Tex numbering ([main.tex](main.tex), [main.pdf](main.pdf)).
> PROVED: §§2–4, Thms 5.3(b), 5.4, 5.12, Cor 5.14, Lemma 5.6 (block lemma), Lemma 5.7 (non-unit twist, now proved
> without excision), Lemma 5.8 (unit twist, corrected at p=2 and stated for the
> reduced HH_0), §§6–15. The archimedean term W_∞ is now defined for all test
> functions (Def 6.5, Convention 6.6) and the odd symbol is derived (Thm 7.2, eq. 57).
> CITED: excision for σ=id (Thm 5.3(a): Wodzicki; Brodzki–Lykova).
> PROVED (second pass): twisted excision (Exc_σ), eq. (25), as Thm 5.3(b)
> (two-filtration argument with twisted coefficients, under a right-linear splitting h of
> multiplication; hypotheses checked for K=E_P⊂T and E_v⊂Q′ in the paragraph after its proof).
> Hence Thm 5.4 (Künneth), Thm 5.12(b) and the global part of Cor 5.14 are now UNCONDITIONAL.
> Numbering unchanged by this pass.
> AUXILIARY, outside the construction: Appendix A (Thm A.1, Mertens; uses Λ(N)).
> Not claimed: compatibility of T with restriction (Prop 11.4, Remark 11.5);
> Thm 13.7(e) is a formal analogy with Weil's decomposition.
> Backups: `main_pre_repair.{tex,pdf}`, `main_pre_*.tex.bak`.

> **Status,  (superseded by ).**  Proved the Hom
> classification (`prop:hom`) and the crossed-product decomposition
> (`prop:crossed`); the claim "only external input left is Wodzicki" was
> inaccurate (the twisted form was used; see above).

> **Status,— label withdrawn.**  An adversarial audit
> ([phase 128](../../03-research/phase-128-adversarial-audit/)) found real
> errors, not only presentation defects.  The `WEIL-STRENGTH-COMPLETE` label is
> withdrawn; see the status banner at the head of [main.md](main.md) and the
> audit record for every finding, its verification and its disposition.
> What survives across the three rows is listed in
> [D128.004](../../03-research/phase-128-adversarial-audit/D128_004_WHAT_SURVIVES.md).

Historical Markdown version: [main.md](main.md) ( its numbering differs from the tex and is superseded).

Consolidates phase 125 (A125.001–015) into one self-contained construction of
row A of the arithmetic Lefschetz programme, closing clauses A.1–A.10 of the
acceptance specification on the declared graph sector ( description;
for the current imports and labels see the  status above).  Central theorems: two-sided excision (§3), the canonical
half-density dagger (§4), decomposition of the full cyclic shadow and the
isomorphic-shadows theorem (§7), the analytic trace invariant and the exact
mixed-sector computation (§§8–9), proper effectivity and Riemann–Roch as a biextension (§10).
Section 1 explains the construction and the insight; Section 13 records the withdrawn routes.  Asserts no sign and does not prove
RH.

[appendix.md](appendix.md): complete proofs of the former imports (finite lattice sums, excision at the origin, Künneth), the second correction (unit twists have infinite-rank twisted shadow), and the single remaining citation (Wodzicki excision).
