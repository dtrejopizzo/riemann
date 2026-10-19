# Paper 10 — The localized-Weil anatomy as a complete local invariant of L-functions: Euler products, Satake recovery, and functoriality

To each $L$-function in the Selberg class the paper attaches a per-prime-power anatomy $\mathcal R_L$:
the profile of its localized Weil form weighted by the ground state, whose prime sum is the bottom
eigenvalue. Three results follow. First, $L$ has an Euler product if and only if its anatomy
factorizes. Second, for $\mathrm{GL}(n)$ automorphic $L$-functions the anatomy recovers the Satake
parameters at every prime. Third, the anatomy is functorial under Rankin–Selberg products and
lifts. Nothing here depends on the Riemann hypothesis. A numerical appendix checks the
autocorrelation zero structure on which the converse rests.

## Main results

- `thm:fwd`: Euler product ⟹ factorizing anatomy — PROVED.
- `lem:auto`: the ground-state autocorrelation is a polynomial times a Gaussian, with at most
  $2\deg P$ moving real zeros — PROVED; numerical check in the appendix — NUMERICAL.
- `thm:convdet`, `thm:conv2`, `thm:char`: converse in the localized-detector regime (one window)
  and in general across two windows of generic width ratio; characterization — PROVED.
- `thm:carleson`, `prop:finite`, `thm:concave`: Carleson reformulation of local positivity,
  finite unconditional Carleson bound, concavity and extremal reduction — PROVED.
- `thm:satake`, `thm:gen`: recovery of Satake power sums, local factors, degree (Hankel rank) and
  Ramanujan exponent — PROVED.
- `thm:rs`, `thm:lift`: multiplicativity under Rankin–Selberg; lifts are polynomial in the base
  anatomy — PROVED, using CITED functoriality inputs where needed.
- `thm:gl1`: $\mathrm{GL}(1)$ automorphy from factorizing anatomy — PROVED; the $\mathrm{GL}(2)$ case
  is reduced to the Selberg degree-two conjecture — CONDITIONAL / OPEN.

## Files

- `main.tex`, `main.pdf` — source and compiled paper.
- `code.py` — code for the numerical appendix.

## Relation to other papers

Extends the anatomy profile of Paper 09.
