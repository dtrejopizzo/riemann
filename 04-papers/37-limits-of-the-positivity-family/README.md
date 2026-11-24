# Paper 37: The Limits of the Positivity Family in the Li–Keiper Route to the Riemann Hypothesis

## What the paper studies

The direct route from the Li–Keiper criterion to the Riemann Hypothesis (RH), taken from Paper 36, ends in a compact–tail inequality (★). This inequality bounds the prime-counting error weighted by a Laguerre kernel. The paper studies sixteen attempts to prove (★) by moving the nonnegativity of an auxiliary object (a measure, a square, a Gram form, a totally positive kernel or a completely monotone function) onto the compact certificate. It shows why each attempt fails.

## What is proved

- Reductions (Section 2): the compact–tail decomposition (Theorem 2.3) and the θ-family identity (Theorem 2.4). Admissible cutoffs are upward closed (Lemma 2.9), which gives the cofinal exponent-four criterion 4λ_n − A_n > 0 (Theorem 2.10). Also proved: the fixed-ratio sufficient form (Theorem 2.12, Corollary 2.13) and the fixed-floor algebraic identity with its shortfall A_n/1001 at T = 1000 (Theorem 3.3, Corollary 3.4). The floor constants 2002/501 and A_n/1001 describe only a sufficient transfer. By Li's criterion together with Bombieri–Lagarias, 4λ_n − A_n ≥ 0 for all large n would already imply RH.
- Structural thesis (Proposition 3.6): the completed cocycle H_u^r K_u^{r−1} is not the Laplace transform of a positive measure, with an explicit closed-form witness. Its Euler and Gamma factors are positive. Its polar factor has density equal, up to the positive normalizing factor e^{−ε x₀}, to −r + (r−1)/√2 < 0 at ½ log 2 (Theorem 12.1, Proposition 12.2). The absolute value of this defect is at least (1 − 1/√2) r, so it never vanishes and grows with r.
- No-go results (Sections 5–11). The order-kernel energy identity and its Hessian collapse (Theorems 5.1, 5.3, 5.4). The PF₂ witness −1/2916 (Theorem 6.1, Witnesses 6.1–6.2). Polar channel densities (Theorems 7.2, 7.3), complete monotonicity and Stein–Mecke (Theorems 7.5–7.8). Abel and Fejér summation, including the fact that the holomorphy needed for Fejér is equivalent to RH (Theorems 8.1–8.4). Tower identities and squares (Theorems 9.1, 9.2, Witness 9.1). Tail-sign statements (Theorems 10.1, 10.2). The arithmetic witness H(2969) < −21 < 0 < 110 < H(3167). Each no-go holds only relative to the inputs declared at the head of its section. For most of them an exact witness is given. A few are structural observations.
- Successor criteria (Section 14): syndetic negativity of the Li coefficients if RH fails (Theorem 14.5), the density and block criteria (Theorem 14.6), and the exact prime–pole form of a bounded Fermi average (Theorem 14.7). The Fermi average itself is not estimated.

## Conditional, heuristic and numerical parts

- The tail estimate (Theorem 2.5, Corollary 2.6) uses an imported effective prime number theorem.
- The finite range 1 ≤ n ≤ 149: λ_n > 0 is certified for 1 ≤ n ≤ 150 by the ball-arithmetic computation scripts/li_ball_certificate.py (Arb balls via python-flint, Taylor coefficients of log ξ(1/(1-z))). Independent partial checks: scripts/li_interval_enclosures.py for 1 ≤ n ≤ 7, and Proposition 9.137 of Paper 36, which gives 2λ_n − A_n > 0 unconditionally for 9 ≤ n ≤ 20 (for 21 ≤ n ≤ 149 only under an unproved coefficient-tail bound).
- The summary of the catalogue (Proposition 13.1, Corollary 13.3) is a classification obtained by inspecting the catalogue. It covers only the catalogued fixed-cutoff transfers and says nothing about arithmetic certificates.
- The operator-norm gap discussion (Remark 14.1) is conditional: if the operator realizes the Weil form, an operator-norm gap is incompatible with RH.
- The absolute load estimate and the detection-scale statements for the Fermi average are heuristic.
- Remark 9.4 is a double-precision diagnostic used only as directional evidence. Remark 16.2 is a failed diagnostic: its two radii disagree, so it says nothing about the sign.
- Neither (★) nor RH nor its negation is proved.

## Known versus new

Li's criterion (Theorem 2.1), the Bombieri–Lagarias theorem and the classical prime number theorem inputs are cited. The following are, to the author's knowledge, new in this combination: the global energy identity for the order kernel, the Hessian cancellation, the tower identities, the hypergeometric polar density, the signed Lévy triple at ½ log 2, and the Fejér coefficient identity.

## Files

- `main.tex`: LaTeX source.
- `limits-of-the-positivity-family.pdf`: compiled paper, 61 pages.
- `scripts/`: supporting computations, cited in the text by relative path. Ball-arithmetic certificate of λ_n > 0 for 1 ≤ n ≤ 150 (requires python-flint): `li_ball_certificate.py`. Exact rational checks: `m1_cumulative_sign_certificate.py`, `m1_global_hessian_check.py`, `global_compound_poisson_tp_check.py`, `incomplete_abel_stop_gate_check.py`, `jordan_cocycle_sign_gate.py`, `li_interval_enclosures.py`, `local_tower_square_check.py`, `near_quartic_margin_check.py`, `fejer_caratheodory_gate_check.py`, `quartic_square_stop_gate_check.py`, `three_channel_cocycle_check.py`. Minimal cutoffs of Remark 2.11: `minimal_cutoffs.py`. Double-precision diagnostics: `global_cocycle_probe.py`, `cubic_cocycle_probe.py`, and the helper `zeta_tools.py`.

## Relation to other papers

The paper builds on the Li–Keiper endpoint of Paper 36 (*The Riemann Hypothesis: An Obstruction Ledger and an Arithmetic Pick Reformulation*). It uses that paper's compact–tail assembly (Proposition 9.131), its far-tail lemma and corollary (Lemma 9.132, Corollary 9.133), the sign range of the archimedean coefficients (Lemma 9.121) and the pole–prime Abel regularization (Proposition 9.126); the finite range is certified in the present paper's own script, with Proposition 9.137 of Paper 36 as an independent check for 9 ≤ n ≤ 20.
