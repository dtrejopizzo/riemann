# E79.84 - The first bridge from small `|c|` to cloud coherence is near-perfect residual balance

**Scope:** `DISCRIMINANT`, first structural bridge candidate between E79.5 and
E79.6.  
**Class:** REDUCCION GENUINA.  
**What we know after this document that we did not know before:** the first
nontrivial bridge between the codimension-one near-closure regime

```text
|c_N| = |1 - sum_j x_j| << 1                                            (84-1)
```

and spectral-cloud coherence is not a trivial residue sign condition. It is a
much sharper package-level fact:

```text
the secular residues r_j := q_j x_j
have almost perfectly balanced positive and negative total mass on the zeta
ladder, while the planted off-line controls do not.                      (84-2)
```

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / IDENT side only.
MW-3:  respected. No per-prime/local-to-global assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No uniform gap hypothesis.
K1-K5: respected. Uses only the exact secular data already certified in phase 78.
E72.16/E77.7az: respected. This is an IDENT-side discriminant reduction, where
  build separation is admissible.
Circularity: respected. The residues come from the finite secular equation,
  independent of the target arithmetic derivative.
```

## 1. Why this is the right next question

E79.83 sharpened E79.5 honestly:

```text
small |c_N| is a robust zeta-only regime,
but it is not a monotone scalar convergence law.                         (84-3)
```

So the next structural question is unavoidable:

```text
what feature of the secular package sits between small |c_N| and
M_N * x single-signedness?                                               (84-4)
```

The exact secular equation already names the obvious candidate:

```text
sum_j r_j / (z-d_j) = c_N,   r_j := q_j x_j,   q_j = d_j - d_{b,N}.     (84-5)
```

If `c_N` is tiny, then the residue package itself must be highly constrained.

## 2. Probe

The audit uses the same finite-section transfer data as E79.83, but now reads
the residue package directly.

For each section it forms:

```text
r_j := q_j x_j,                                                          (84-6)
R_net := |sum_j r_j| / sum_j |r_j|,                                      (84-7)
R_pm  := (sum_{r_j>0} |r_j|) / (sum_{r_j<0} |r_j|).                      (84-8)
```

Interpretation:

```text
R_net ~ 0     means strong cancellation of the residue package as a whole,
R_net ~ 1     means one sign dominates completely,
R_pm  ~ 1     means positive and negative masses are nearly balanced.    (84-9)
```

The same audited ladder is used:

```text
zeta,
plant at gamma1 = 14.134725..., beta=0.30,
plant at gamma2 = 21.022039..., beta=0.30.                              (84-10)
```

## 3. Result

The zeta-side residue package is extraordinarily balanced.

### Zeta

On the audited sections `N=8,10,12`, one finds:

```text
N= 8:  |c_N| ~ 3.93e-7,   R_net ~ 5.76e-12,   R_pm ~ 1.0,
N=10:  |c_N| ~ 4.56e-9,   R_net ~ 2.67e-14,   R_pm ~ 1.0,
N=12:  |c_N| ~ 1.29e-7,   R_net ~ 1.46e-16,   R_pm ~ 1.0.              (84-11)
```

So on the zeta ladder the package is not merely mixed-sign. It is almost
perfectly balanced in total positive/negative mass.

### Planted off-line at gamma1

The first planted falsifier behaves very differently:

```text
N= 8:  |c_N| ~ 18.31,   R_net ~ 1.0,      R_pm ~ 0.0,
N=10:  |c_N| ~  2.32,   R_net ~ 0.541,    R_pm ~ 0.298,
N=12:  |c_N| ~ 11.78,   R_net ~ 0.211,    R_pm ~ 0.651.               (84-12)
```

So the package is not near-balanced, and at `N=8` it is actually one-signed.

### Planted off-line at gamma2

The second planted falsifier confirms the same structural split:

```text
N= 8:  |c_N| ~  3.98,   R_net ~ 0.631,    R_pm ~ 4.43,
N=10:  |c_N| ~  1.78,   R_net ~ 0.321,    R_pm ~ 0.514,
N=12:  |c_N| ~ 145.99,  R_net ~ 1.0,      R_pm ~ 0.0.                 (84-13)
```

Again there is no trace of the zeta-side near-perfect balance.

## 4. Reading

This is the first real bridge candidate between E79.5 and E79.6.

The naive bridge would have been:

```text
small |c_N|  <=>  all residues share one sign.                          (84-14)
```

That is false. On the zeta ladder the residues are mixed-sign.

What survives is subtler and stronger:

```text
small |c_N| travels with a nearly exact positive/negative balance of the
residue package.                                                        (84-15)
```

That matters because the cloud is not built from one residue at a time, but
from the whole rational package

```text
sum_j r_j/(z-d_j).                                                      (84-16)
```

So a balanced-sign package is exactly the kind of object that can force a
coherent near-symmetric cloud, whereas a one-sided or badly unbalanced package
naturally drives the planted sign-mixing seen in E78.154 and E79.83.

## 5. What this does and does not prove

This note does **not** yet prove:

```text
small |c_N|  <=>  residual balance  <=>  M_N * x single-signed          (84-17)
```

as a theorem.

But it does reduce the gap materially:

```text
E79.5 is no longer isolated from E79.6.
The first plausible bridge object is now named and numerically sharp:
the near-perfect signed mass balance of r_j = q_j x_j.                  (84-18)
```

So the remaining burden is much smaller than before.

## 6. Consequence

After E79.84, the discriminant front sharpens to:

```text
small |c_N|
  -> near-perfect signed balance of the residue package
  -> coherent near-symmetric spectral cloud
  -> M_N * x single-signed.                                             (84-19)
```

The last two arrows are still open, but they are now attached to a concrete
finite object rather than to a slogan.

So the next honest move is one of:

```text
1. derive the first arrow directly from the secular identity;
2. derive the second arrow by analyzing how balanced r_j shape the roots of
   sum_j r_j/(z-d_j)=c_N;
3. or falsify this bridge on a wider off-line harness if it breaks.      (84-20)
```

## 7. Status

```text
proved by audit:
  the zeta-side small-|c_N| regime comes with near-perfect signed mass
  balance of the secular residue package;

proved by audit:
  two planted off-line controls fail that balance strongly;

clarified:
  the bridge from E79.5 to E79.6 is not a one-sign residue law, but a
  package-level positive/negative balance law;

reduced:
  the live discriminant burden from the vague pair (small |c_N|, coherence)
  to the sharper triple
    (small |c_N|, residual balance, coherence);

open:
  prove that residual balance is the mechanism producing cloud coherence;

next:
  attack the root geometry of the balanced secular package instead of mining
  more packet-side observables.
```
