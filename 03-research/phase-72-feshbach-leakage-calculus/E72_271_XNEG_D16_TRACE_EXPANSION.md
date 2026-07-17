# E72.271 -- XNEG-D16 trace expansion

**Purpose.** Convert the corrected pole-even mixed sign `XNEG` into a finite trace identity.

For degree `D=16`, the signed Chebyshev approximants used in E72.270 are polynomials:

```text
G_0 = p_0(K_0),        G_1 = p_1(K_1).
```

Thus:

```text
2 Tr(G_0G_1) = 2 sum_{r,s} a_r b_s Tr(K_0^r K_1^s).
```

This is the finite mixed-cycle form of `XNEG-pole-even-D16`.

## Coefficients

The script prints coefficients for the actual matrix powers `K_j^r`, not for powers of scaled
variables:

```text
G0_power_in_K=
-1.179618989975e-02
+6.500000000000e-01 K
-2.097100426623e+00 K^2
+2.013676678513e+01 K^4
-1.312618871919e+02 K^6
+4.960766711714e+02 K^8
-1.100880404246e+03 K^10
+1.415273246964e+03 K^12
-9.747976404373e+02 K^14
+2.781315627036e+02 K^16

G1_power_in_K=
-6.740679942716e-03
+7.000000000000e-01 K
-2.696271977086e+00 K^2
+5.825278962841e+01 K^4
-8.543742478833e+02 K^6
+7.265087141865e+03 K^8
-3.627560657941e+04 K^10
+1.049294405189e+05 K^12
-1.626125451829e+05 K^14
+1.043932388829e+05 K^16
```

Only the linear term and even powers appear. Therefore `XNEG-D16` is a finite list of mixed trace
moments:

```text
Tr(K_0^r K_1^s),        r,s in {0,1,2,4,6,8,10,12,14,16}.
```

## Verification

At `lambda=20`, cut `0.60`, in the corrected pole-even geometry:

```text
direct   = -3.4884541006299730e-02
expanded = -3.4884541006300805e-02
absDiff  = 1.076e-15
```

So the trace expansion is algebraically identical to the Chebyshev matrix evaluation.

## Proof-facing statement

The corrected mixed-sign target can be stated without mentioning Chebyshev evaluation:

```text
XNEG-pole-even-D16:
2 sum_{r,s in S} a_r b_s Tr(K_0^r K_1^s) <= 0,
S={0,1,2,4,6,8,10,12,14,16}.
```

Here `K_0,K_1` are the corrected pole-even relative prime blocks at the chosen cut.

## Status

This closes the algebraic expansion of `XNEG-D16`. The remaining theorem is the sign inequality for
that finite mixed trace polynomial, uniformly in the stable pole-even regime.
