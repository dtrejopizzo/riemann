# E72.269 -- Pole-even HOC3/K1 probe

**Purpose.** Recheck the HOC3/K1 low-dimensional mechanism in the corrected pole-relative even
geometry.

The old HOC3/K1 probes used `setup_pair`, which removed an accidental even line. After E72.261--E72.268
the corrected geometry is:

```text
C_model = B_even^T(H_model-e_pole I)B_even,
```

with the full even sector retained. Therefore the low block is now simply

```text
P = span{even Fourier modes 0,1}
```

inside `B_even`, with no projection away from a spurious even `k`.

## Test

For the high block `A_1`, decompose:

```text
A_1 = [[B,C],[C^*,D]]
```

relative to `P + P^perp`. The same identity is used:

```text
Tr(A_1^3)
= Tr(B^3)+Tr(D^3)+3Tr(BCC^*)+3Tr(DC^*C).
```

The proof-friendly certificate is:

```text
t_B = Tr(B) < 0,
low := -[Tr(B^3)+3Tr(BCC^*)] > tail,
Tr(A_1^3) <= 0.
```

## Output

```text
E72.269 pole-even HOC3/K1 probe
Corrected geometry: full even sector, pole energy subtracted; P=span{even modes 0,1}.
lam L dim TrA3 minA maxA tB sB low sharp full margSharp margFull K1sign
 16 5.545177  41 -1.758512e-02 -2.655034e-01 +1.101089e-01 -2.438979e-01 7.049123e-02 1.856039e-02 2.954661e-03 6.268496e-03 +1.560573e-02 +1.229189e-02 NEG
 20 5.991465  49 -1.703170e-02 -2.617373e-01 +1.040691e-01 -2.408511e-01 6.866002e-02 1.777702e-02 2.470771e-03 5.471611e-03 +1.530625e-02 +1.230541e-02 NEG
 24 6.356108  57 -1.655057e-02 -2.588011e-01 +9.825926e-02 -2.408753e-01 6.702078e-02 1.722240e-02 1.954015e-03 4.450967e-03 +1.526838e-02 +1.277143e-02 NEG
```

## Reading

The low-dimensional HOC3/K1 mechanism survives the pole-even correction:

* `Tr(A_1^3)<0` in all tested corrected windows;
* `t_B<0`, so the `K1` sign mechanism remains;
* both sharp and nonspectral full tails are comfortably dominated by the low margin;
* the margin is stable rather than shrinking in the tested window.

This is important: the HOC3 low-mode dominance was not caused by the accidental even line removed by
the old helper.

## Status

Positive diagnostic in the corrected geometry. The next proof-facing step is to turn the pole-even
HOC3/K1 mechanism into the same kind of finite theorem as before:

```text
average(K1)>0,
prime-power discrepancy small,
tail_full controlled by model Schatten bounds.
```

The numerical evidence supports using the nonspectral full-tail route, without a special sharp
exception in the tested corrected windows.
