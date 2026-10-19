# Paper 47: readability restructuring

Backup: `main_pre_readability.tex` (the older `main_pre_readability.tex.bak` from September is untouched).
Pages: 192 before, 194 after (the reading guide, the new intro paragraphs and the sources appendix add the pages).
The paper has 24 numbered sections plus 4 appendices.

## Outline (architecture and dependencies)
- I. Duality and certificates (§§2–6): Lévy form of m (thm:S) → primal/dual LP (thm:A, thm:D1, thm:O, thm:E, prop:P)
  → tails and the ½log3 certificate (thm:C) → certificates = explicit formula (thm:Z, thm:Zexh, thm:finZ, Kreĭn problem)
  → lattice ceilings (prop:TK, thm:N, thm:Np, thm:R, thm:latedge).
- II. Structure at one window and the certified range (§§7–13): archimedean threshold/index (thm:index, cor:Tarch)
  → obstructions (thm:Vp, prop:env, prop:finite, cor:margin1, thm:finmod, cor:void) → inertia of remainders
  → semilocal Sonin split → parity Schur complement and polar capacity (thm:parityschur, prop:polarcap)
  → certified ½log5 (thm:log5A, thm:log5W) → finite reduction (thm:coer-B, thm:coer-schur).
- III. Operator and sign structure (§§14–16): Wiener–Hopf pencil (thm:wh-pencil, thm:wh-schur, thm:wh-det)
  → Nyquist identity (thm:nyq, thm:nyq-schur) → NEW §16 even sector (lem:archcount, lem:combsine, prop:WT, cor:H1minus, prop:H).
  §16 depends on thm:parityschur (§11) and prop:wh-polarres (§14).
- IV. Reformulations (§§17–19): first contact, witnesses, polar-free form, combs, one profile (thm:oneprofile).
- V. Limits and the remaining problem (§§20–24): barriers → shape theorem (thm:shape, cor:shape) → new subsection
  "No imported positivity" (thm:noimport, rem:conjunctions) → specification (prop:spec) → exterior form (prob:ext-L) → open problems.

## What changed
1. Introduction: new "Reading guide" (replaces "Organization") grouping the sections into parts I–V with their main
   results; two new paragraphs in "Results" (the even sector; the shape of a proof, specification and leakage inequality);
   a sentence repeated inside "Barriers" (bounded remainders have infinite negative index) removed.
2. Section titles now state what is proved (15 titles changed; labels unchanged).
3. New §16 "The even sector: archimedean cancellation and polar inertia" collects lem:archcount and lem:combsine
   (moved from §2), prop:WT with its proof, the comparison with deposits, cor:H1minus, rem:chiev-sine, prop:H and the closing
   discussion (moved from §11). The proof of prop:WT previously appeared after prop:H, separated from its statement by four
   items; it now follows the statement directly.
4. thm:noimport and rem:conjunctions, which stood before the introduction of §22, now form the last subsection of §21.
5. Computational records to appendices: rem:zcert → App. A (new subsection subsec:enclzcert); rem:finitesign and
   rem:ext-latnum → App. C.
6. Process language: all memo identifiers, phase numbers and "audit" mentions removed from the main text and listed in the new
   App. D "Sources in the research record" (label app:sources). In rem:conjunctions(iv), "tried in the phase-200 to 204
   records" became "examined so far". Eleven editorial placement comments in the source removed.
7. No statement, proof, constant or label changed. The check: the 590 original \label{} are all present (0 missing,
   0 duplicates), 7 labels were added for new (sub)sections and the appendix; the compile gives 0 errors and no undefined references.

## Mathematical errors
None was found that is certain; nothing is marked [Correction needed].
