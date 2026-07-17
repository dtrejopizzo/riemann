# E72.266 -- Lambda=16 pole-even sharp BSE

**Purpose.** Isolate the transition window left by the corrected pole-even LM8 architecture.

E72.263--E72.265 give a homogeneous rational LM8 envelope for the stable pole-even windows from
`lambda=20` onward in the tested range. The window `lambda=16` is different:

* exact BSE passes;
* the homogeneous envelope is too loose.

Therefore `lambda=16` should be handled by a sharp finite certificate, not by forcing the stable
majorant to cover it.

## Computation

Using the corrected pole-relative even geometry:

```text
C_model = B_even^T(H_model-e_pole I)B_even,
```

the two block energies are:

```text
E0  = 4.9308800876772851e-01
E1  = 4.3045211897669328e-01
BSE = 9.2354012774442173e-01
```

Against the target:

```text
TARGET = 9.4089999999999996e-01
slack  = +1.7359872255578224e-02
```

So the finite transition window has real numerical margin.

## Spectral budget

The dominant contributions are negative eigenmodes. For `K1`, the leading negative mode alone
contributes:

```text
eigenvalue = -5.3100683678857852e-01
contribution = 2.8196826071621206e-01
```

For `K0`, the leading negative mode contributes:

```text
eigenvalue = -3.6079691592140534e-01
contribution = 1.3017441453839762e-01
```

Thus the transition certificate is genuinely spectral/sharp; a coarse polynomial envelope loses too
much in this window.

## Formal certificate target

To make this window paper-level, one should certify one of:

```text
1. interval enclosures for all entries of K0,K1 plus interval eigenvalue/BSE enclosure;
2. rational enclosure of the characteristic polynomials plus Sturm isolation of the eigenvalues;
3. a low-mode/tail certificate using the listed dominant modes and a Schatten tail bound.
```

The required certified inequality is:

```text
BSE_16 <= 0.923541 < 0.9409.
```

With the observed slack `0.01736`, an interval certificate at `1e-4`--`1e-3` scale would be more than
enough.

## Status

This is a sharp floating finite-window certificate, not yet a formal interval proof. It is sufficient
to define the finite target precisely and to justify separating `lambda=16` from the stable LM8
majorant.
