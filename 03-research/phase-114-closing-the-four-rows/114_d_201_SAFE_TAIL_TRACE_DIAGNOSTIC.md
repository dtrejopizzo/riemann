# D.201 — The scalar-gap safe-tail trace budget is too crude at `T=log(6)/2`

## Verdict

After the three-block correction of D.200, a first non-directed audit tested
whether the uniform complement gap `delta=0.219` could absorb the safe-tail
coupling by the trace estimate

\[
 \kappa\le\operatorname {tr}(A_{SS}^{-1}R_{SS}).       \tag{0.1}
\]

It cannot.  In a central FFT evaluation of the complete Gamma symbol and
the contacts `2,3,4,5`, the D8/S190 split gives

\[
 \operatorname {tr}(A_{SS}^{-1}R_{SS})\approx16.03.    \tag{0.2}
\]

This is a diagnostic, not a directed lower or upper bound.  It rejects only
the proposed *crude proof strategy*.  The operator norm in D.200 can be much
smaller than the trace, and the true complement Green operator is much
stronger than the scalar lower bound on high-frequency directions.

No paper file is modified.

## 1. Computation

Use the approximate primitive Ritz frame from the exact `V_200` centre.  For
each normalized vector `v_j`, synthesize it on the physical interval, apply

\[
 G_\Gamma-m_0I-
 \sum_{n=2}^5{\Lambda(n)\over\sqrt n}
   (S_{\log n}+S_{-\log n}),                           \tag{1.1}
\]

and form the safe residual majorant

\[
 r_j=\max(\|Av_j\|^2-\lambda_j^2,0).                  \tag{1.2}
\]

The subtraction in (1.2) removes only the Ritz component; hence it is the
appropriate scalar diagnostic for `QAv_j`.  Periodization, interpolation and
grid errors are not enclosed, so the numbers below prove no sign.

The trace sums are

| slow dimension | first safe Ritz value | trace diagnostic |
|---:|---:|---:|
| 2 | `1.80e-11` | `16.26` |
| 4 | `5.58e-7` | `16.17` |
| 6 | `3.47e-3` | `16.10` |
| 8 | `5.05e-1` | `16.03` |
| 16 | `1.29` | `15.99` |
| 32 | `1.85` | `15.84` |

Thus simply enlarging the slow block does not make the trace smaller than
`0.219`.

## 2. What remains live

The trace inequality uses

\[
 \|X\|\le\operatorname {tr}X                              \tag{2.1}
\]

for a positive matrix and can lose a factor comparable to the safe rank.
The next calculation must therefore evaluate

\[
 \kappa=\|R_SA_{SS}^{-1/2}\|^2                          \tag{2.2}

by a singular-value enclosure, including its infinite Legendre tail.  If
(2.2) still exceeds the scalar gap, the correct comparison is instead

\[
 \|A_{QQ}^{-1/2}A_{QS}A_{SS}^{-1/2}\|^2,               \tag{2.3}

which retains the actual high-frequency strength of `A_QQ` rather than
replacing it by `0.219I`.

The reproducible diagnostic is

```text
python3 114_d_201_t6_safe_tail_fft_diagnostic.py
```

and writes `/tmp/t6_safe_tail_fft_diagnostic.npz`.
