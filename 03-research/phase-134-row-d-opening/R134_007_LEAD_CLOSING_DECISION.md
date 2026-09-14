# R134.007 — Lead closing decision for the row-D opening campaign

Author: session lead (Fable 5.1), audit of record. Date: 2026-09-12.

## 1. Grep verification of round 3 (lead)

| item | result |
|---|---|
| E1 | Prop 3.6a(iii) survives only inside the §9.2b withdrawal table; Remark 3.6b present; §9.1 consistent ✓ |
| E2 | Definition 6.8 carries (R5); `† ` excluded by (R5); §9.1 item 3a "no K-twist constructed" ✓ |
| E3 | README free of the `B_T`-as-block residue ✓ |
| no-sign | every `I_∂ ≤ 0` occurrence is the target, a hypothesis, an OPEN item, RH-conditional or a disclaimer ✓ (R134.005 §6, re-grepped) |
| label | §10 "None." ✓ |
| scripts | both reproduce all printed numbers (builder and auditor re-runs; lead spot check `d134_gram.py --check`) ✓ |

## 2. Decision

    ROW D: NO LABEL. The opening campaign is closed; Paper 46 stands as
           row D's opening state, fit per R134.005 after the bounded erratum.

Recorded:

1. **What Paper 46 proves.** Lemma 3.1 (`Π` is a bijection onto the primitive
   class; the two Tate conditions are exactly compact support of `e^{−|t|/2}∗F`);
   Thm 3.6 (`Λ(g) = 𝔏(g⋆g^†)`, `𝔏 = −Π²(W_fin+ω_∞)`, with `Π²ϖ = 0`); Thm 3.7
   (`RESTATEMENT`: RH ⟺ row D's target ⟺ `𝔏` positive-definite ⟺ Fourier
   transform of a positive measure ⟺ a unitary representation of the carrier's
   modulus group with `Λ(g) = ‖π(g)Ω‖²`; classical links named); the swap law
   Thm 4.3 and Cor 4.4 (the P124.013 target splits into two scalar even/odd
   inequalities — a reduction of shape, not progress); Thm 5.8 (the archimedean
   diagonal dominates at small `ε`, unconditionally, for `ζ` and for `Ξ_a`:
   finite inertia at small `ε` is uninformative; D.3 retired as a programme
   item); the negatives of §6 with counterexamples and the requirement list
   (R1)–(R5) for a nonnegative invariant, with (R5) exposing that rows A–C
   construct no duality carrying the primitive sector off itself (no
   `K`-twist); the falsifier suite §7 (`Ξ_a` has no Frobenius family in row B's
   sense — Thm 3ter.6 fails; Davenport–Heilbronn has neither Frobenius nor Tate
   block).
2. **What it does not prove.** Any sign; any statement about the zeros outside
   the comparison theorem and the labelled equivalence; the temperedness of
   `𝔏` (Rem 3.6b: equivalent to a PNT-type growth bound, RH ⟹ it, not decided).
3. **Refutations of record.** Six blueprint claims of the lead (the gravest:
   `|ρ(1−ρ)|²` — RH written as a definition; `B_T` conflated with the Tate
   block); five builder statements across three rounds, the last (3.6a(iii))
   introduced by a repair and **also accepted by the lead** before the hostile
   auditor showed it false under RH and equivalent to a proof of ¬RH in the
   paper (R134.003 addendum).
4. **Findings against the corpus**, recorded in phases 124 and 118 with
   `[phase 134]` notes: the Galerkin eigenvalues of the double-precision scans
   are variational upper bounds (a positive one certifies nothing; the
   interval-arithmetic endpoint certificate is untouched); P124.014's brackets
   are resolution-unstable (`T_q(Ξ_{0.35}) ≤ 1.68`); P124.013's `liminf`
   criterion is invariant but its numerical value is not.
5. **The problem, stated once.** The missing object of row D is a
   nonnegative invariant of type *norm*: a Hilbert space in which the averaged
   Frobenius flow of the carrier is unitary and the target functional is
   `‖π(g)Ω‖²`, constructed **without** using RH — equivalently a Riemann–Roch
   identity with a duality that moves the primitive sector off itself ((R5))
   and a vanishing theorem. Rows A–C supply the equality; nothing in the
   repository supplies the norm, and Paper 46 proves which shapes it cannot
   have.

## 3. Next

Row D proper requires new mathematics of the kind §2 item 5 names. The lead
recommends that any further D campaign start from (R5): construct or refute
the existence of a duality on the correspondence algebra that does not
preserve the primitive sector and is compatible with `T`, since without it no
Riemann–Roch shape exists to carry a sign.
