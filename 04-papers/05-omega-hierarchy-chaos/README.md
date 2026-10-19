# Paper 05 — The ω-Class Hierarchy of the Riemann Zeta Function: Per-Prime Weights, Multiplicative Chaos, and the Branching Structure of the Maximum

The paper connects three families of objects attached to ζ without assuming the Riemann
hypothesis: the moment exponents $(\log T)^{k^2}$, the multiplicative-chaos exponents of
$|\zeta(\tfrac12+it)|^{2\beta}$, and the two-term asymptotics of the maximum of $\log|\zeta|$ on
short intervals. The connecting device is the per-prime weight carried by $\omega(n)$. The
arithmetic core (§§3–6) is rigorous. The identification with the maximum (§7) is the established
multiplicative-chaos and branching picture, presented as such and not as a new proof.

## Main results

- `lem:lsd`: Landau–Selberg–Delange asymptotics for $\sum_{n\le N} z^{\omega(n)}/n$ — CITED.
- `prop:dk`, `thm:weight`: on squarefree $n$, $d_k(n)=k^{\omega(n)}$, so the moment exponent $k^2$
  is the per-prime weight $z=k^2$ — PROVED.
- `prop:dict`: dictionary $z=\beta^2$; freezing $\beta_c=1$ corresponds to neutral weight $z_c=1$ — PROVED
  as a dictionary; its link to chaos theory is CITED.
- `thm:ld`: the supercritical regime $\beta>1$ corresponds to large deviations of $\omega(n)$,
  $\omega(n)\sim z\log\log N$ — PROVED.
- `prop:levels`: grouping primes by $\lfloor\log\log p\rfloor$ gives $\log\log T$ levels of equal
  variance $\tfrac12$ (Mertens) — PROVED.
- Branching random walk reproducing both terms of the maximum (height $\log\log T$, correction
  $-\tfrac34\log\log\log T$) — CITED/heuristic (§7); numerical confirmation — NUMERICAL.

## Files

- `main.tex`, `main.pdf` — source and compiled paper.

## Relation to other papers

Extends the ω-class decomposition of Papers 02–03 from Dirichlet polynomials to ζ.
