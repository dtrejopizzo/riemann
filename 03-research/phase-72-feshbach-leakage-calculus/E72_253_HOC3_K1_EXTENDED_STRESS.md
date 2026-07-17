# E72.253 - HOC3/K1 extended stress

## Purpose

E72.242 and E72.246 identify `lambda=32` as a delicate finite window for HOC3 and the `K1` average.
This note stress-tests the same mechanism beyond the original `lambda<=36` range.

## Diagnostic

Script:

```text
E72_253_hoc3_k1_extended_stress.py
```

Output:

```text
E72.253 HOC3/K1 extended stress
tailFull=||D||op(TrD2+3||C||HS2); no D_+ except comparison to lambda=32.
lam L dim low tailFull margin TrA13 K1avg primeAvg sumBetaK1 status
 32 6.931472  72 2.622823e-03 3.211498e-03 -5.886749e-04 -2.110545e-03 +3.211312e-03 +2.400028e-03 +1.153524e-01 FAIL
 36 7.167038  80 1.636806e-02 2.139203e-03 +1.422885e-02 -1.620182e-02 +4.216685e-03 +4.388385e-03 +2.388454e-01 PASS
 40 7.377759  88 6.578564e-03 2.356156e-03 +4.222407e-03 -6.433001e-03 +4.169053e-03 +3.113086e-03 +1.909378e-01 PASS
 48 7.742402 104 1.112509e-02 2.735418e-03 +8.389674e-03 -1.070992e-02 +2.667868e-03 +2.699692e-03 +2.038057e-01 PASS
 56 8.050703 120 1.487985e-02 2.552198e-03 +1.232765e-02 -1.446539e-02 +2.475122e-03 +2.513533e-03 +2.252258e-01 PASS
```

## Reading

The nonspectral tail bound fails at `lambda=32`, as already observed, but the full HOC3 cubic is still
negative there. The sharp finite certificate remains needed for this exceptional window.

Beyond `lambda=32`, the nonspectral bound recovers and remains positive through `dim=120`.

The `K1` prime-power average remains positive:

```text
sumBetaK1 > 0
```

through the extended range.

## Consequence

The working HOC3 proof package is strengthened:

```text
finite exception:
  lambda=32 by sharp D_+ certificate;

stable range:
  nonspectral tail bound + positive K1 average.
```

No new late failure appears up to `lambda=56`, `dim=120`.
