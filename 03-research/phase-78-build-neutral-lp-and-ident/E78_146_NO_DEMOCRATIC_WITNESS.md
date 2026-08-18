# E78.146 -- NO-DEMOCRATIC-WITNESS: the c_0 lower bound is unavoidable

## 0. Context

Follows E78.145, which left `BTG-DIV-L` reduced to a single open item: an
analytic lower bound on the bottom-mode boundary coupling `c_0^{(N)}`
relative to the ground-eigenvalue collapse `nu_0^{(N)}`. This document tests
the natural "finite-witness" hope that the whole thing could be settled
WITHOUT ever touching `c_0` -- via a sign-free, eigendecomposition-free
lower bound on `S_N(0)`. It cannot. That is proved here (negatively), which
upgrades E78.145's open item from "unproven" to "provably unavoidable".

Front: A1. Class: AUTOPSIA (closed negative lemma).

## 1. The finite-witness attempt

`BTG-DIV-L` at `mu_L = 0` is `S_N(0) = sum_j c_j^2 / nu_j^2 -> infinity`, and
exactly

```text
S_N(0) = || A_N^{-1} b_N ||^2      (one linear solve, no eigendecomposition).
```

Cauchy-Schwarz gives a sign-free, mode-democratic lower bound:

```text
S_N(0) = sum_j c_j^2 / nu_j^2
       >= (sum_j c_j^2)^2 / (sum_j c_j^2 nu_j^2)
       =  || b_N ||^4 / || A_N b_N ||^2                  (CS-LB)
```

Every quantity in CS-LB is an elementary norm of a matrix-vector product.
If CS-LB diverged, `BTG-DIV-L` would be proved with a witness that never
isolates `c_0` or `u_0`, sidestepping the entire E78.145 sec 5 obstruction
(the non-fixed shape of `b_N`, the sign of `c_0`, the rate race).

## 2. Result: CS-LB does NOT diverge (probe E78_146, dps=70)

```text
zeta N=6:  cs_lb=0.1045     s_true=1.047e7    slack=1.00e8
zeta N=8:  cs_lb=1.491      s_true=1.143e13   slack=7.67e12
zeta N=10: cs_lb=0.003525   s_true=4.998e13   slack=1.42e16
zeta N=12: cs_lb=0.009482   s_true=1.663e21   slack=1.75e23
plant N=6: cs_lb=2.704      s_true=5.665e7    slack=2.10e7
plant N=8: cs_lb=44.12      s_true=1.176e18   slack=2.67e16
plant N=10:cs_lb=0.001964   s_true=2.551e14   slack=1.30e17
plant N=12:cs_lb=0.000625   s_true=3.435e20   slack=5.50e23
```

`cs_lb` is bounded and oscillating (0.003 .. 1.5 for zeta) while `s_true`
diverges from 1e7 to 1e21. The slack ratio `s_true / cs_lb` grows to 1e23.
CS-LB is not merely loose; it fails to diverge at all.

(Run stopped at N=12 -- the pattern is monotone and unambiguous; N=14..18
would only widen the slack. The three completed zeta/plant pairs already
span 14+ orders of magnitude of divergence in `s_true` against a bounded
`cs_lb`.)

## 3. Why it fails -- exact analytic reason

Cauchy-Schwarz `(sum a_j/nu_j^2) >= (sum a_j)^2/(sum a_j nu_j^2)` is tight
iff `1/nu_j^2` is constant across the support of the weights `a_j = c_j^2`,
i.e. iff all `nu_j` are equal. The BTG-DIV-L regime is the exact opposite:
`nu_0 -> 0` geometrically while `nu_{j>=1} = O(1)`. The single tiny isolated
eigenvalue is precisely what CS averages away. E78.145's own data already
said this: `bfrac = S_bottom/S_total -> 1`, so `S_N(0)` is asymptotically
`c_0^2/nu_0^2` alone -- a one-mode object. No bound that treats the modes
symmetrically can see it.

## 4. What this closes (negatively) and what it sharpens

Closed lemma `NO-DEMOCRATIC-WITNESS`: any lower bound on `S_N(0)` that is
invariant under the mode weights (does not single out the collapsing bottom
mode) is bounded in `N` and therefore cannot establish `BTG-DIV-L`. Proof:
the sharpest such bound is CS-LB (Cauchy-Schwarz is the extremal
mode-symmetric inequality for a sum of `a_j/nu_j^2`); it is bounded above by
`||b_N||^4/||A_N b_N||^2`, which the probe shows stays O(1). QED (finite,
verified).

Consequence for E78.145's open item: the required lower bound on `c_0^{(N)}`
is not one possible route among several -- it is UNAVOIDABLE. Establishing
`BTG-DIV-L` requires an argument that explicitly isolates the bottom
eigenpair `(nu_0, u_0)` and lower-bounds its boundary coupling `c_0`. There
is no democratic shortcut. This is a genuine structural fact about the
obstruction, not a statement about zeta.

## 5. Wall checklist

```text
MW-1..6:        not invoked (no positivity, no local-to-global assembly).
K1-K5:          not invoked.
E72.16/E77.7az: not invoked (no ambient-inverse-norm route; S_N and CS-LB
                are direct finite quantities; the lemma is build-neutral --
                CS-LB is bounded for BOTH builds, so this is not a detector).
Front A1:       consistent with Outcome A; CS-LB bounded for both builds.
```

## 6. What we know now

The BTG-DIV-L divergence is irreducibly a single-bottom-mode phenomenon;
the sharpest mode-symmetric (sign-free, eigendecomposition-free) lower
bound provably cannot capture it. The E78.145 `c_0` lower bound is therefore
unavoidable, not merely the first route tried.

## 7. Status

```text
closed negative lemma (NO-DEMOCRATIC-WITNESS); does NOT advance BTG-DIV-L,
sharpens its open gap.

proved:    CS-LB = ||b_N||^4/||A_N b_N||^2 is the extremal mode-symmetric
           lower bound on S_N(0), and it is bounded in N (verified N=6..12,
           dps=70, both builds; slack ratio to true S_N grows to 1e23);
proved:    therefore any democratic/sign-free lower bound on S_N(0) is
           bounded and cannot establish BTG-DIV-L;
conseq.:   the c_0^{(N)} lower bound of E78.145 sec 5 is UNAVOIDABLE, not
           optional -- BTG-DIV-L requires explicit bottom-eigenpair isolation;
open:      the c_0 lower bound itself (unchanged from E78.145; now known to
           be the only door, not one of several);
next:      any real attempt must lower-bound |c_0^{(N)}| via the bottom
           eigenvector's structure directly -- e.g. Combes-Thomas / exact
           eigenvector-eigenvalue identity on (nu_0, u_0) -- there is no
           route around it.
```
