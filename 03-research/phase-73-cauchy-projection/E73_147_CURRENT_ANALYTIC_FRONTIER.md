# E73.147 - Current Analytic Frontier

Date: 2026-07-12.

## 1. What is now proved

The following finite algebra is proved:

```text
Pair_z^infty(w)=A_L(z,w)H_0(w)+B_L(z,w)H_0(-w).
```

For two rows this gives

```text
[H_0(w),H_0(-w)]^T
=M_L(w)^(-1)[Pair_{z_1}^infty(w),Pair_{z_2}^infty(w)]^T.
```

Therefore:

```text
INV_a + signed paired-packet bound at exponent 17+a
=> LDIV_17
=> CSV_17.
```

This is a genuine finite local divisor forcing theorem.  It does not use
global determinant convergence, strong resolvent convergence, or Weil
positivity.

## 2. What is numerically supported

The coefficient inverse is polynomial:

```text
||M_L(w)^(-1)|| <= approximately L^3
```

in the calibrated rows.

The active packet alone often reaches margin `17`, and the signed inactive
tail improves several rows.  The mechanism is therefore not empty.

## 3. What is not closed

The uniform theorem is not yet proved.

The too-strong route

```text
Pair^M small separately and TailPair small separately
```

fails.

The correct route is signed:

```text
M_L(w)^(-1)(active row + inactive tail row) xi_L = O(L^-17).
```

This is still open as an analytic estimate.

## 4. The next load-bearing lemma

The next lemma must be stated in row form, not in packet-value form:

```text
Signed Row Divisor Lemma.
For every standard-box critical node w there are two admissible rows z_1,z_2
such that

||
M_L(w)^(-1)
[
 R_{z_1,w}^{active}+R_{z_1,w}^{tail}
 R_{z_2,w}^{active}+R_{z_2,w}^{tail}
]
xi_L
||_1
<= C L^-17.
```

Here `R^{tail}` is the explicit inactive-mesh row `p_infty-p_active`, not
the divisor identity substituted backward.

## 5. Proof strategy

The proof should not take absolute values of active and tail rows
separately.  It should use:

```text
1. INV_3: elementary lower bound on det M_L(w).
2. Tail row formula: explicit inactive mesh sum with parity gain.
3. Eigen-row cancellation: apply the finite CCM equation to the combined
   active+inactive row after the two-row inverse.
4. Manifest finite rows: absorb low lambda and transition failures into
   the existing E73.120 manifest.
```

If this lemma is proved uniformly on the standard boxes, the chain is:

```text
Signed Row Divisor Lemma
=> LDIV_17
=> CSV_17
=> Uniform GATE-73
=> scalar WRL.
```
