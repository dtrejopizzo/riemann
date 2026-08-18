# 107.46 -- Paper C primitive degree-zero audit

## 1. Purpose

`107_24` reduces Route A item A3 to a finite primitive-projection
problem, and `107_25`--`107_27` isolate the denominator of that
projection in terms of the corner contribution and exceptional
corrections.  The present note exact-audits the finite symbolic content
of that reduction.

## 2. What is audited

The verifier `107_46_paper_c_primitive_degree_zero_audit.py` checks four
exact statements.

1. For finite visible divisor data and degree data, the primitive
   coefficient
   \[
    c_T(f)=\deg_{H_T^{(1)}}(D_{f,T})/h_T
   \]
   is the unique linear correction coefficient forcing degree zero when
   \(h_T\neq0\).
2. The denominator identity
   \[
    h_T=2c_T+\varepsilon_{\rm vv}(T)+\varepsilon_{\rm hh}(T)+2\varepsilon_{\rm vh}(T)
   \]
   is audited exactly on symbolic correction packages.
3. The currently visible center types of `107_27` affect the denominator
   only through the exceptional channels \(\varepsilon_{\rm vv},
   \varepsilon_{\rm hh}, \varepsilon_{\rm vh}\), not by a direct
   structural cancellation of the corner term.
4. In the minimal corner-preserving case with vanishing correction
   package, one recovers \(h_T=2c_T\neq0\) whenever \(c_T\neq0\).

## 3. Finite shadow being tested

The audit works with the exact symbolic bookkeeping already fixed in
`107_24`--`107_27`.

1. A visible divisor is encoded by its packet, diagonal, infinity, and
   two-ruling coefficients.
2. A degree datum is encoded by the corresponding generator degrees with
   the ruling symmetry \(d_{\rm v}=d_{\rm h}\).
3. A correction package is encoded by the corner term and the three
   exceptional corrections.

The verifier checks exact rational identities in this symbolic model; it
does not rely on floating approximation.

## 4. Result

The verifier passes exactly.

It confirms that:

1. the primitive projection formula of `107_24` really is the unique
   linear degree-zero correction in the finite bookkeeping model;
2. the denominator bookkeeping of `107_25` is algebraically consistent;
3. the corner-preserving center list of `107_27` does not by type alone
   erase the corner contribution;
4. the minimal-regularization nonvanishing criterion behaves exactly as
   stated.

So the finite shadow behind A3 is now pressure-tested beyond prose.

## 5. Scope boundary

This audit still does **not** prove:

1. that the actual constructed surface has \(h_T\neq0\);
2. the numerical values of the generator-vs-polarization intersections;
3. the exact signs or magnitudes of the exceptional corrections on the
   real model;
4. the faithful transport of this divisor-level primitive projection to
   the final Picard/Jacobian realization.

Its force is exact but finite: it validates the symbolic primitive
degree-zero reduction and the correction-channel logic that the later
geometric realization must satisfy.
