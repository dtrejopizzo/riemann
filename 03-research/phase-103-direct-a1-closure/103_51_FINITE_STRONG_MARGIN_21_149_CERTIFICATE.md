# Finite strong-margin certificate for 21 through 149

## Theorem

For every integer \(21\le n\le149\),

\[
 \lambda_n^{\rm prime}+\frac12\lambda_n^{\rm arch}>0.
\]

Equivalently,

\[
 2\lambda_n-\lambda_n^{\rm arch}>0
 \qquad(21\le n\le149).
\]

Together with the rational certificates already recorded for \(n\le20\),
this proves the finite strong-margin range through \(149\).  It is a finite
certificate, not a proof of the uniform A1 inequality and not a proof of
RH.

## Certified inputs

Let

\[
 q(t)=t\zeta(1+t),\qquad d(t)=\frac{1-2^{-t}}t.
\]

`103_44` proves that the quotient of the Hasse truncation at \(K\) encloses
the coefficient of \(q\), after widening, by

\[
 \left|[t^m](q-q_K)\right|
 \le {\bigl(27+9\log(K+1)\bigr)2^{m-K}\over K+1}.       \tag{1}
\]

`tools/eta_fixed_generator.py` forms the finite Hasse weights exactly over
the denominator \(2^K\).  Every logarithm is enclosed by a rational
`artanh` series, and all subsequent operations use outward integer
fixed-point arithmetic at scale \(10^{500}\).  The triangular division

\[
 d(t)q_K(t)=\eta_K(1+t)                                  \tag{2}
\]

is performed before (1) is added.  This order matters: the constant term
inside (2) is the constant term of \(q_K\), while the returned exact
constant \(q(0)=1\) is installed only after all nonconstant coefficients of
\(q_K\) have been computed.

For \(p(t)=\log q(t)=\sum_{j\ge1}p_jt^j\), the verifier uses the exact
coefficient recurrence

\[
 p_n=q_n-\frac1n\sum_{k=1}^{n-1}k p_kq_{n-k}.             \tag{3}
\]

The two parts of the margin are then reconstructed from the finite
identities

\[
 \lambda_n^{\rm prime}
 =\sum_{k=1}^n n{n-1\choose k-1}p_k,                      \tag{4}
\]

\[
 \lambda_n^{\rm arch}
 =1-\frac n2\bigl(\gamma+\log(4\pi)\bigr)
 +\sum_{k=2}^n {(-1)^k\over2^k}{n\choose k}(2^k-1)\zeta(k).
                                                                    \tag{5}
\]

The intervals for \(\log(4\pi)\) are inherited from the rational verifier
of `217`; each \(\zeta(k)\) is enclosed by a rational partial sum and the
integral-test tail.  Thus (1)--(5) contain no floating-point input.

## Executions and cross-check

The production driver is
`tools/fixed_margin_eta_21_149.py`.  Two complete executions were made with
different truncation and logarithm depths:

\[
 (K,T)=(830,800),\qquad (K,T)=(850,820).
\]

Each execution emitted exactly 129 rows, one for every \(21\le n\le149\),
and every integer lower endpoint was positive.  Comparing the two output
tables gave zero mismatches in the lower and upper decimal prefixes at
twelve places.  In both runs the smallest lower endpoint in the range was
at \(n=21\), with

\[
 \lambda_{21}^{\rm prime}+\frac12\lambda_{21}^{\rm arch}
 >5.128680391459.                                         \tag{6}
\]

At the other endpoint the enclosure has the displayed prefix

\[
 103.360395755597
 <\lambda_{149}^{\rm prime}+\frac12\lambda_{149}^{\rm arch}
 <103.360395764160.                                       \tag{7}
\]

The sign claim itself uses the exact fixed-point integer lower endpoints,
not the displayed decimal prefixes.  The second parameter set is an
independent truncation sign check of the same analytic formula; each run is
separately enclosed by (1), and neither replaces that outward-error proof.

The exact commands are

```bash
python3 tools/fixed_margin_eta_21_149.py --top 149 --first 21 --K 830 --terms 800
python3 tools/fixed_margin_eta_21_149.py --top 149 --first 21 --K 850 --terms 820
```

For the complete textual outputs produced during this audit, the SHA-256
digests were respectively

```text
0fc00bcef692a780bac4e0fdf97d8c506903cc53fea46306eb2c96bbe678121b
0f3fd007d21872795a168c30eb070637ef17be2fe2128eba4806139ab57da276
```

## Scope

This removes the finite input gap \(21\le n\le149\) requested by the
proposed threshold \(150\).  It does **not** certify that the separate
conditional asymptotic estimates have effective constants starting exactly
at \(150\); that effectivity audit remains distinct.  The master obstruction
is still the unconditional, uniform A1 inequality (or an equivalent
RH-strength mechanism) for the infinite range.
