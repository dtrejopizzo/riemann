# E78.20 - Balanced denominator as the exact side condition for LOGT-CANCEL

**Run:** 2026-07-18.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.19 reduced the live residual to

```text
LOGT-CANCEL_N
 = N^2 |C_N-C_{N+2}| / (|Q_ext,N| + |Q_logT,N|).          (BD-1)
```

So the remaining denominator issue is now completely explicit:

```text
when is |Q_ext| + |Q_logT| comparable to one resolved component?
```

This note records the exact comparability condition and audits it on the
certified rows.

## 2. Exact comparability lemma

Define

```text
RATIO_N := |Q_logT,N| / |Q_ext,N|,                         (BD-2)
```

whenever `Q_ext,N != 0`. Then

```text
|Q_ext,N| + |Q_logT,N|
 = |Q_ext,N| (1 + RATIO_N).                               (BD-3)
```

Therefore any two-sided ratio control

```text
0 < m <= RATIO_N <= M < infinity                          (BD-4)
```

implies the exact denominator comparability

```text
(1+m)|Q_ext,N| <= |Q_ext,N|+|Q_logT,N| <= (1+M)|Q_ext,N|. (BD-5)
```

Symmetrically,

```text
(1+1/M)|Q_logT,N| <= |Q_ext,N|+|Q_logT,N|
                  <= (1+1/m)|Q_logT,N|.                   (BD-6)
```

So the denominator side condition for E78.19 is nothing more and nothing less
than:

```text
BALANCED-DENOMINATOR:
  prove a cofinal two-sided bound on |Q_logT|/|Q_ext|.
```

If `(BD-4)` holds, then `(BD-1)` is equivalent up to fixed constants to

```text
N^2 |C_N-C_{N+2}| / |Q_ext,N|                             (BD-7)
```

or to the same ratio with `|Q_logT,N|` downstairs.

## 3. Probe audit

Companion:

```text
E78_20_balanced_denominator_probe.py
E78_20_balanced_denominator_results.json
```

The probe reads the certified E77.5y rows and computes

```text
|Q_logT|/|Q_ext|,    (|Q_ext|+|Q_logT|)/|Q_ext|,
(|Q_ext|+|Q_logT|)/|Q_logT|.
```

### Zeta

At `sigma=1.0`, the audited rows satisfy

```text
0.7103 <= |Q_logT|/|Q_ext| <= 1.0706,                     (BD-8)
1.7103 <= denominator/|Q_ext| <= 2.0706.                 (BD-9)
```

At `sigma=3.0`,

```text
0.6918 <= |Q_logT|/|Q_ext| <= 1.0389,                     (BD-10)
1.6918 <= denominator/|Q_ext| <= 2.0389.                 (BD-11)
```

So on the healthy zeta rows, the denominator is already tightly comparable to
either resolved component.  In particular, it never comes from a collapse of
one side against the other.

### Planted build

At `sigma=1.0`, the same ratio ranges over

```text
0.3433 <= |Q_logT|/|Q_ext| <= 37.03,                      (BD-12)
```

and at `sigma=3.0`,

```text
0.2140 <= |Q_logT|/|Q_ext| <= 1.7344.                     (BD-13)
```

So the plant does not preserve a stable balanced-denominator regime.

## 4. Consequence for the live target

Combining E78.19 with `(BD-5)` gives the exact implication:

```text
SECTION-LAG-CURVATURE
+ BALANCED-DENOMINATOR
=> LOGT-CANCEL-COFINAL.                                   (BD-14)
```

This is not a fake strengthening; it is just the algebraic content of
`LOGT-CANCEL` written in the right variables.

The important point is that E78.19 and E78.20 are complementary:

```text
E78.19 identifies the exact numerator;
E78.20 identifies the exact denominator side condition.
```

Together they replace the old opaque mismatch target by a clean pair:

```text
weighted curvature of C_N
+ balanced ratio |Q_logT|/|Q_ext|.
```

## 5. Candid reading

This is still not a closure theorem.  It does **not** prove a cofinal ratio
bound; it only names the exact side condition and shows that the certified zeta
rows already sit in a very balanced regime.

That matters because it tells us what to pursue next:

```text
the denominator is not a mysterious large-scale object anymore;
the remaining work is to derive the ratio control from the exact shell/Schur
identities, not from empirical boundedness tables.
```

## 6. Status

```text
proved:
  BALANCED-DENOMINATOR is the exact side condition needed to turn E78.19's
  curvature target into LOGT-CANCEL-COFINAL;

proved:
  any cofinal two-sided bound on |Q_logT|/|Q_ext| yields constant-factor
  comparability of the denominator to either resolved component;

observed:
  the audited zeta rows already satisfy a tight balanced-denominator regime,
  roughly 0.69 <= |Q_logT|/|Q_ext| <= 1.07 on sigma in {1,3};

observed:
  the planted build does not preserve a comparably stable ratio regime;

reduced:
  the live front to SECTION-LAG-CURVATURE plus BALANCED-DENOMINATOR;

next:
  derive the ratio control from the exact shell/cell formulas for
  Q_ext and Q_logT, rather than from tables alone.
```
