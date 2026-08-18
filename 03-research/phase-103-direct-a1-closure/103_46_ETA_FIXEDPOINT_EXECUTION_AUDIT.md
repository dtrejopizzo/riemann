# Eta fixed-point execution audit

`eta_fixed_generator.py` now parameterizes the rational `artanh` depth.  It
uses 120 terms only for the small \(K=32\) pilot and accepts 800 terms for
the intended \(K=830\) computation, so logarithm errors are below the scale
of the \(2^{830}\) finite-sum cancellation.

An executed \(K=100,M=20\), 300-term run completed in 8.76 seconds and
13.8 MB reported peak resident memory.  It reproduced the expected initial
Stieltjes values, including \(\gamma_0\) and \(\gamma_7\), at the displayed
12-decimal scale.  This is a performance and consistency pilot; a formal
containment table against all EM intervals still needs to be emitted by the
driver.

The first attempted \(K=830,M=149\), 800-term batch did not finish within the
original interactive execution window.  No output or interval from that
abandoned run is used.
`eta_fixed_generator.py` was then changed to `log_integer_fixed`: its
`artanh` loop is entirely fixed-point integer arithmetic and cached per
integer, removing Fraction/gcd work from logarithm construction.  The
\(K=100\) consistency pilot still succeeds after this replacement.  A fresh
\(K=830,M=149\) run still did not finish within the interactive window, so
the remaining cost is the 830-by-150 large-integer power propagation and
formal-series operations, not the proved geometric tail or Fraction logs.
Subsequent optimized, recoverable executions did finish.  The resulting
certificate and a second run at \((K,T)=(850,820)\) are recorded in
`103_51_FINITE_STRONG_MARGIN_21_149_CERTIFICATE.md`; that later result
supersedes the execution status in this audit.
