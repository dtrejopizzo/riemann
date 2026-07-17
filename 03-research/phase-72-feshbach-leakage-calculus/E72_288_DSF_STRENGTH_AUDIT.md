# E72.288 -- DSF strength audit

**Purpose.** Audit whether the Dirichlet-symbol floor of E72.287 is merely technical or RH-strength.

E72.287 gives the sufficient route:

```text
DSF-O2:
-2 inf_omega Re P_L(omega) = O(L^2),

P_L(omega)=sum_{n<=e^L} Lambda(n)n^(-1/2+i omega).
```

This is a clean scalar statement, but it is not obviously easier than the original arithmetic
obstruction.

## Relation to the logarithmic derivative

Formally,

```text
sum_n Lambda(n)n^(-s) = -zeta'(s)/zeta(s).
```

Thus `P_L(omega)` is the cutoff version of

```text
-zeta'(1/2-i omega)/zeta(1/2-i omega).
```

The explicit formula for such a cutoff contains zero terms of the form

```text
e^{(rho-(1/2-i omega))L}/(rho-(1/2-i omega))
```

up to smoothing and endpoint factors.  If there is an off-critical zero

```text
rho=beta+i gamma,       beta>1/2,
```

then around `omega=-gamma` the zero term has size roughly

```text
e^{(beta-1/2)L}.
```

Depending on phase and smoothing, this can contribute a negative excursion to `Re P_L(omega)` much
larger than `L^2`.

## Consequence

The scalar floor

```text
-inf_omega Re P_L(omega) = O(L^2)
```

should be treated as an RH-strength arithmetic theorem, not as a harmless PNT-level estimate.

This does **not** invalidate E72.287.  It means E72.287 is useful as a reduction:

```text
DSF-O2 => APCB => upper complement => compact-root HPAC.
```

But proving DSF-O2 directly by standard prime-number estimates would likely run into the same
zero-resonance wall already identified in E72.15--E72.16.

## How to keep the route honest

There are now two possible APCB routes:

```text
1. Strong scalar route:
   prove DSF-O2 for P_L(omega).
   This is simple to state but likely RH-strength.

2. Compressed autocorrelation route:
   prove APCB directly for the finite even compressed operator.
   This may be weaker than DSF because the compression discards many bad full-line symbol directions.
```

The numerical gap supports route 2:

```text
lambda_max(Delta_arith)_+/L^2  ~ 0.13--0.16,
symbol floor/L^2               ~ 1.26--1.84.
```

The full-line symbol bound is an order of magnitude looser.  Therefore the finite compressed structure
may contain extra smoothing that DSF throws away.

## Updated reading

`DSF-O2` is a valid sufficient scalar target, but it should not be promoted as the main proof route
unless a genuinely new argument appears.  The better next target is the **compressed APCB theorem**
itself:

```text
lambda_max(
 -sum_{n<=e^L} Lambda(n)n^(-1/2) B_even^TQ_{log n}B_even
)_+
= O(L^2),
```

using the finite interval/even compression rather than the full-line symbol floor.
