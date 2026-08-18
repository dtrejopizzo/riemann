# D.80 — Cutoff-free Fourier audit at `T=log(2)`

This is an independent finite-band audit, not a proof on the complete
support space.  Since `2T=log(4)`, the cutoff-free matrix of Groskin
(arXiv:2607.02828, ancillary `arb_ldlt_certify.py`) applies with `c=4`.
Only its closed digamma/trigamma and rigorously tailed geometric formulas
for the archimedean entries are used here; no sum over zeta zeros is used
to infer a sign.

The primary ancillary was executed directly with python-flint:

```bash
curl -L --silent --show-error \
  https://arxiv.org/src/2607.02828v1/anc/arb_ldlt_certify.py |
  PYTHONPATH=/tmp/d61-flint python3 - --c 4 --N 40 --prec 500
```

It certified `n_pos=81, n_neg=0`.  The deeper independent run

```bash
curl -L --silent --show-error \
  https://arxiv.org/src/2607.02828v1/anc/arb_ldlt_certify.py |
  PYTHONPATH=/tmp/d61-flint python3 - --c 4 --N 200 --prec 2000
```

built the 401-dimensional cutoff-free matrix in 53 seconds and certified
all 401 interval `LDL^T` pivots positive in 128 seconds:

```text
RESULT: n_pos=401 n_neg=0
>>> CERTIFIED positive-definite
```

This eliminates finite Gamma cutoff as the source of the observed
near-tangency in a large Fourier band.  It does **not** alone prove the
complete-space inequality: the Fourier-band complement and its Schur
coupling still require the directed high-mode/Feshbach theorem.  In
particular this note does not mark row D closed.
