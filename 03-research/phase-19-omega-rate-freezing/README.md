# Phase 19 — forward flow from primes to ω(n) statistics, rate function and freezing

The phase runs the "forward flow" line (primes → ω(n), the number of prime
factors → moments → multifractal statistics), the one line in the program
not absorbed by the known pair-correlation/CAP wall, to see how far an
unconditional, zero-free theory of ω-statistics can be pushed, and whether
it eventually touches the zeros of ζ.

## Results
- The Keating-Snaith exponent k² for the moments M_k(N) of Dirichlet-type
  sums is derived purely from Erdős-Kac (ω(n) ~ Poisson(log log n)) and the
  Poisson moment generating function, with no use of ζ zeros. **PROVED**
  (unconditional, elementary).
- The large-deviation rate function I(α) for ω(n)/log log n is strictly
  narrower than Gaussian; no bulk freezing transition occurs (the annealed
  rate is linear). **PROVED/derived**.
- B-smooth sums reduce to exact Euler products, quantifying weight
  condensation onto large-ω integers as the moment order increases.
  **PROVED**.
- The quenched (random multiplicative) maximum grows monotonically with
  Σ1/p; only the pre-asymptotic branching-random-walk onset is reached, not
  a true glass/freezing transition. **PARTIAL / pre-asymptotic**.
- The five steps combine into one chain: primes → Poisson ω-statistics →
  moment exponent k² and constant C_k → finite-N large-deviation saturation
  → B-smooth condensation → quenched maximum growth; none of this chain
  requires any zero of ζ.
- Explicit scope statement: the ω-forward-flow theory and the location of
  zeros (row D / RH-type positivity) are, on the evidence gathered, **separate
  theories**; no bridge between them was found. Whether the fluctuations
  (not the mean) of M_k, short-interval ω-statistics, or ω(n)/ω(n+h)
  correlations encode any zero information is left as an **OPEN** question.

## Documents
- `00-PHASE19-CLOSURE.md` — summary table of the five steps, the unification
  diagram, and the candid two-branch assessment.
- `01-camino3-forward-flow.md` — derivation of the k² exponent via
  Selberg-Delange / Erdős-Kac forward flow.
- `02-omega-rate-freezing.md` — the large-deviation rate function I(α) and
  the no-bulk-freezing result.
- `03-bsmooth-freezing.md` — B-smooth sums and weight condensation.
- `04-random-mult-maximum.md` — quenched maximum of random multiplicative
  functions.
- `05-k2-from-erdjoskac.md` — the Poisson-proxy derivation of k² with no
  zeros of ζ.
- `experiments/` — corresponding Python scripts (`camino3_*`).

## Relation to other phases
Independent of the main CAP/de Branges/SURF positivity line (that line is
treated as a frozen wall here); the open bridge question — whether ω
fluctuations or correlations are zero-sensitive — is explicitly handed to
phase 20 as a research program.
