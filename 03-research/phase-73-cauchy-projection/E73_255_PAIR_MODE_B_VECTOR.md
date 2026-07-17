# E73.255 - Pair-mode audit for the bordered quotient vector

## 1. Question

E73.254 showed that Cramer numerator smallness is not produced by a large
four-term Laplace alternation. The smallness must enter through the bordered
quotient vector

```text
b = D_Q xi_L,
```

where `D_Q` stacks two Cauchy rows for each of two critical ordinates.

The next possible simplification is row-pair parity: perhaps each gamma pair
has a forced symmetric or antisymmetric cancellation. This note tests exactly
that.

For each gamma pair `(b_0,b_1)` define

```text
b_sym  = (b_0+b_1)/sqrt(2),
b_anti = (b_0-b_1)/sqrt(2).
```

For the full four-vector define gamma-parity by Cauchy-row-parity coordinates:

```text
ss = (b00+b01+b10+b11)/2,
sa = (b00-b01+b10-b11)/2,
as = (b00+b01-b10-b11)/2,
aa = (b00-b01-b10+b11)/2.
```

If a universal parity theorem were responsible for smallness, the same parity
mode should be consistently suppressed or consistently dominant across the
tested scales and rational orders.

## 2. Result

The dominant mode is not stable.

Representative output:

```text
Pair modes
 lam      L pow  g dom  row0B  row1B   symB  antiB pairNormB cancelB domLossB
   8    4.159   0  0  sym -21.68  -21.46 -21.32 -22.61    -21.31    1.15    -0.14
   8    4.159   0  1  sym -15.76  -15.79 -15.53 -18.13    -15.53    2.37    -0.23
  10    4.605   0  0 anti -18.50  -18.51 -21.62 -18.27    -18.27    3.12    -0.22
  10    4.605   0  1 anti -14.98  -14.98 -18.22 -14.75    -14.75    3.25    -0.22
  12    4.970   0  0  sym -20.62  -20.36 -20.26 -21.20    -20.25    0.84    -0.10
  12    4.970   1  0 anti -18.32  -18.36 -20.29 -18.12    -18.12    1.97    -0.20
  16    5.545   0  0 anti -19.30  -19.81 -19.80 -19.30    -19.25    0.50     0.00
  16    5.545   0  1  sym -18.20  -19.15 -18.29 -18.52    -18.18    0.33     0.10
```

The four parity coordinates likewise switch:

```text
 lam      L pow   bMaxB  bNormB    ssB    saB    asB    aaB  maxMode
   8    4.159   0  -15.76  -15.53 -15.77 -18.37 -15.77 -18.37       ss
  10    4.605   0  -14.98  -14.75 -18.46 -14.98 -18.45 -14.98       sa
  12    4.970   0  -16.61  -16.49 -16.71 -17.76 -16.72 -17.76       ss
  16    5.545   0  -18.20  -18.18 -18.54 -18.91 -18.45 -18.59       as
```

Thus `b` is not small because one fixed parity projection kills a large
bordered vector. The rows are already at the small scale, and the surviving
dominant parity channel changes with `(L,rat_power)`.

## 3. History guard

This is not the same mechanism as:

```text
E72.390  parity gain for the finite Fourier tail;
E73.072  paired packet normalization;
E73.075  exact complete-mesh pair divisibility;
E73.233  paired commutator defect;
E73.254  Laplace/Cramer alternation.
```

Those results concern packet/tail parity or Cramer expansion. Here the object
is the quotient bordered vector `D_Q xi_L` after DD-local projection.

## 4. Verdict

Rejected:

```text
PAIR-PARITY-B:
b=D_Q xi_L is small because a fixed symmetric or antisymmetric row mode cancels.
```

Kept:

```text
BORDER-ROW-DIV:
each quotient bordered row must be proved small structurally, before any
pair-mode decomposition.
```

The next analytic theorem should therefore target rowwise quotient annihilation:

```text
for each quotient defect delta_{gamma,r},
delta_{gamma,r} xi_L = O_M(L^-M),
```

or an explicit finite identity implying this for all four rows at once. A
parity-only theorem would repeat an already-audited mechanism and would not
explain the observed data.

