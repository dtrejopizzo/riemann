# Phase 167 — The witness-weighted sieve bound (WS)

Goal (R167_000): construct the one inequality the map leaves after R166_802: a bound on the sum of Λ
twisted at the frequency γ_q of the quartet and weighted by the witness weight, treated as a multiplicative-theory problem.

## File index
- `R167_000_PROBLEM.md` — setup of (WS): fixed data (scale, weight, frequency, exponent) and tasks A1–A3.
- `R167_101_QUANTITATIVE_TARGET.md` — A1: exact quantitative requirement. Corrected weight w = (e^{−iγ_q·}g)*ǩ; Thm A (exact identity), Lemma Q, Thm C, Prop W PROVED; Thm B given (Dom_θ); box **(WS\*)**; residues O167.101.1 (Dom_θ), O167.101.2 (small-y regime).
- `R167_102_SIEVE_CONSTRUCTION.md` — A2: direct sieve attack. Mean values give η = ½; **Thm B/B′ (blindness of sieves, b_θ)**; Thm C circular; Thm D ARGUED (Vaughan/Heath-Brown ⇒ zero density); Thm E (at a fixed scale = explicit formula). DEAD.
- `R167_103_ATOMICITY_IN_SIEVES.md` — A3: atomicity and integrality in sieves. **Theorem S** (sieves valid in discrete Beurling systems); Cor S′: DMV/Zhang is the falsifier for sieve proofs.
- `R167_190_AUDIT.md` — audit (round 1, Lemma K, verdict corrected after review); authoritative labels.
- `R167_291_AUDIT_PHASE167.md` — review: Lemma K downgraded to a remark; Thm B repaired as B′; verdict R5.

## Result
(WS\*): Re Σ_{n≤Y} Λ(n) n^{−½+iγ_q} w(log n) < (1−θ) c_Θ |G(t_q)|² |k(−iδ_q)| − E_K/4, over all of [1, Y], given (Dom_θ).
It is a single-scale polylogarithmic bound, of RH quality. (a) Unreachable by the sieve class (Thm B′, b_θ; Theorem S with
DMV/Zhang); (b) uniform in the scale ⟺ a zero-free statement (Thm C / Landau); (c) at a single scale = evaluation of the explicit
formula (Thm E). It is not "uniformly false" (Lemma K downgraded, R167_291).

## Status
**Closed in round 1; (WS\*) characterized: unreachable with no zeros, circular with them; (★_cell) OPEN.** Row D OPEN.
Editor (R164_301 §15): grid part 18 (1022 routes, ■11 ◩19 ◧34), R163_401 v12 (§4.11(i)), Paper 48 (paragraph "Phases 166–167"; 31 pages).
</content>
