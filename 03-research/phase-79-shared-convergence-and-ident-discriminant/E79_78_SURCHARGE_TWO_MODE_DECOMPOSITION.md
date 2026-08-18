# E79.78 - The surcharge side does not collapse to one scalar

**Scope:** `GAP-Z` only, post-E79.77 audit of the geometric side of the
frontier rule.  
**Class:** REDUCCION GENUINA + AUTOPSIA FRANCA.  
**What we know after this document that we did not know before:** the surcharge
does admit an exact two-mode decomposition, but unlike the mismatch side it does
**not** collapse to one mesoscopic scalar on the audited tradeoff rows. The
unit-threshold law of E79.76 is therefore genuinely asymmetric: one scalar on
the mismatch side versus a two-mode geometric cost.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Pure algebra on the audited E79.70/E79.76 family.
E72.16/E77.7az: respected. Convergence-side structure only.
Circularity: respected. No endpoint identity is imported.
```

## 1. Starting point

E79.77 collapsed the mismatch side to one sigma-rigid excess scalar `eps(S)`.
The next candid question is whether the surcharge side collapses in the same
way.

From E79.72-E79.73,

```text
surcharge(S) = -0.22 card(S) + 0.14 gaps(S) + 0.36 start(S).            (78-1)
```

Using `gaps = span - card`, this rewrites exactly as

```text
surcharge(S) = 0.36 start(S) + 0.14 span(S) - 0.36 card(S).             (78-2)
```

Equivalently,

```text
surcharge(S) = 0.36 (start(S) - card(S)) + 0.14 span(S).                (78-3)
```

So the geometric side already splits into two packet-level modes:

```text
Mode A: anchor-minus-mass  = start - card,
Mode B: span.                                                             (78-4)
```

## 2. Probe

Companion files:

```text
E79_78_surcharge_two_mode_decomposition_probe.py
E79_78_surcharge_two_mode_decomposition_results.json
```

The probe records, on the E79.76 tradeoff rows:

```text
- the exact decomposition (78-2),
- Delta_surcharge = 0.36 Delta(start-card) + 0.14 Delta(span),
- the contribution of each mode along the chosen frontier jump.         (78-5)
```

## 3. Result

The decomposition is exact on every audited row, and the tradeoff rows activate
different geometric modes:

```text
N=10:
  Delta_s = 0.06
          = 0.36 Delta(start-card) + 0.14 Delta(span)
          = -0.36 + 0.42.                                               (78-6)

N=12:
  Delta_s = 0.30
          = 0.36 Delta(start-card) + 0.14 Delta(span)
          = 0.72 - 0.42.                                                (78-7)

N=16:
  Delta_s = 0.36
          = 0.36 Delta(start-card) + 0.14 Delta(span)
          = 0.36 + 0.00.                                                (78-8)
```

So the three live tradeoff rows are not using one universal geometric
mechanism:

```text
N=10: mixed anchor/mass + span tradeoff,
N=12: mixed in the opposite direction,
N=16: pure anchor-minus-mass jump.                                      (78-9)
```

## 4. Reading

This is the key contrast with E79.77.

The mismatch side already collapsed to

```text
one sigma-rigid excess scalar |eps(S)|,                                 (78-10)
```

but the surcharge side does not collapse further on the same audited rows. It
is already exact, but genuinely two-mode:

```text
geometric cost = 0.36(start-card) + 0.14 span.                          (78-11)
```

So the easiest hope

```text
"both sides come from one common scalar, hence the unit threshold is forced"   (78-12)
```

is dead.

## 5. Consequence

This sharpens the live burden in a useful way.

What remains is **not** to find one scalar generating both sides. The actual
frontier law now reads:

```text
choose H iff the drop in |eps| pays for the two-mode geometric increment

  0.36 Delta(start-card) + 0.14 Delta(span)                             (78-13)
```

at exchange rate `1`.

So the surviving structural question is narrower and more candid:

```text
why does the common-cloud / extra-root coupling value one unit of |eps|-drop
the same as one unit of this two-mode geometric cost?                   (78-14)
```

## 6. Status

```text
proved by algebra + probe:
  the surcharge side has an exact two-mode decomposition
  0.36(start-card) + 0.14 span;

clarified:
  unlike the mismatch side, the geometric side does not collapse to one scalar
  on the tradeoff rows;

killed:
  the hope that E79.76 becomes a one-variable balance law on both sides;

open:
  explain the unit exchange rate between |eps|-reduction and this exact
  two-mode geometric increment;

next:
  inspect whether the coefficients 0.36 and 0.14 themselves are forced by a
  simpler normalization or by exact relations inside the frontier family.
```
