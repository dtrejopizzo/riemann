# Paper 36 — The Riemann Hypothesis: An Obstruction Ledger and an Arithmetic Pick Reformulation

## What the paper studies

Part I is a ledger of obstructions met by several spectral, arithmetic, adelic and positivity-based approaches to RH, grouped into structural walls (arithmetic propagation, wrong-sign positivity, absence of a Hasse–Minkowski principle for infinite-dimensional forms, per-place indefiniteness, absence of a gapped polarization, sign versus magnitude, uniform-norm bounds). Each item is either cited to a proved result, proved in the paper, or labelled heuristic or observation; most classifications are heuristic. Two statements that might be expected are recorded as not used, with their correct forms (§3.9); other statements are given in weaker or conditional form where they occur.

Part II builds the arithmetic Pick positivity (ARP-P) chain: fifteen steps proving ARP-P ⟺ RH. Since the target function is a sum over the zeros, this is a Nevanlinna-class reformulation of RH. Eleven are unconditional statements (definitions, classical facts, or implications), two (Steps 9 and 11) are proved consequences of Step 5, Step 15 assembles them, and Step 5 (ARP-P itself) is open. Its internal reduction ends at the terminal inequality Ω₇ (δ_N ≥ 0 for all N), which is the classical Li criterion λ_n ≥ 0 for all n and is equivalent to RH. The chain does not reduce the difficulty of RH. The paper does not prove RH.

## What is proved (statement numbers refer to the compiled PDF)

- Theorems 9.241 (ARP-P ⟹ RH, by Nevanlinna–Pick interpolation and a normal-family argument) and 9.245 (RH ⟹ ARP-P); Corollary 9.246 (equivalence); Corollary 9.247 (the open input is ARP-P, which is equivalent to RH).
- Theorem 9.8 (explicit channel formula); Theorems 9.14, 9.16, 9.17 (scalar one-node positivity and separated-node and two-node criteria); Theorem 9.28 (window positivity ⟺ ARP-P); Corollary 9.29 (finite negative witness) and Theorem 9.33 (phase-adjusted single-cluster reduction).
- Theorem 9.39 (determinant serialization; an equivalent reformulation of RH).
- Theorem 9.43 (scalar Pick positivity for fixed finite cluster patterns at large height); Theorem 9.64 (for each fixed N, scalar Pick positivity at sufficiently large height in an interior band, ineffective threshold). Neither bears on RH.
- Theorem 9.53 (RH ⟺ one-point jet positivity for all N) and Theorem 9.100 (J_N ≥ 0 for all N ⟺ RH); both are Li/Pick-type reformulations.
- Proposition 9.86 (finite-range interpolation bound).
- Lemma 9.132 (prime-number-theorem tail A0) and Corollary 9.136 (A1 ⟹ Ω₇). A1 is open and at least as strong as RH.
- Proposition 9.137 (numerical, computer-assisted): an interval-arithmetic check of D_n = 2λ_n − A_n > 0 for 9 ≤ n ≤ 20, and for 21 ≤ n ≤ 149 conditionally on a coefficient-tail bound for the eta series that is tested numerically but not proved (scripts below); for 1 ≤ n ≤ 8 only uncertified numerical values are used. Under RH, A1 holds for all sufficiently large n, with no effective threshold.
- The de Bruijn–Newman terminal cascade formula lim t_N^* = Λ_Ξ is stated as a conjecture; only t_N^* ≤ Λ_Ξ is proved (Λ_Ξ denotes the constant of the flow normalized by Ξ_0 = Ξ, one quarter of the standard de Bruijn–Newman constant). The window hypothesis of the detection proposition fails for large N at fixed gauge.

## Conditional, heuristic, numerical

- Theorem 9.23 is conditional on a decoherence hypothesis (PDH) which Remark 9.22 shows to be false under RH, so it is vacuous under RH.
- Theorem 9.233 (measure bridge) and the realization layer are conditional on an operator family that the paper does not construct.
- Remarks 3.1 and 3.2 (classification of classical mechanisms; sign principle) are heuristic. Conjecture 9.96 (two-sided factorial bounds), Conjecture 9.200 (Li envelope), Conjecture 9.207 (Gronwall rigidity) and Conjecture 9.214 (terminal cascade formula) are unproved.
- Several reformulations of Li's criterion are recorded (logarithmic-density, Fermi, Abel, block, entropic and deep-tail forms such as (HD4)). Each is equivalent to RH, none is easier than λ_n ≥ 0 for all n, and none is proved.
- Floating-point values quoted in the text (κ_sin(1) ≈ 0.686, the Davenport–Heilbronn rate, Li values up to n = 170, cascade ratios) are observations without an included script; nothing depends on them.

## Known versus new

Li's criterion, Weil's criterion, the Kreĭn–Langer theory, de Bruijn–Newman results and the Bombieri–Lagarias expansion are classical and are cited. What is new is the Pick-kernel chain, its internal reductions and the ledger organisation. None of it is progress toward RH.

## Files

- `main.tex` — LaTeX source.
- `obstruction-ledger.pdf` — compiled paper (170 pages).
- `scripts/` — interval-arithmetic scripts for Proposition 9.137: `fixed_margin_9_20.py`, `fixed_margin_eta_21_149.py`, `eta_fixed_generator.py`, `stieltjes_em_interval_pilot.py`, `omega7_point4_interval_verify.py`.

## Relation to other papers

It cites no other paper of the series; statements of Part I that come from earlier work of the series are either proved here or labelled heuristic or observation.
