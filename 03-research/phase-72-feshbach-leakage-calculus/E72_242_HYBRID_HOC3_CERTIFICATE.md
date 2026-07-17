# E72.242 - Hybrid HOC3 certificate

## Purpose

E72.241 showed that the fully nonspectral tail bound works except at the delicate `lambda=32` window.
This note packages the practical proof strategy:

```text
stable windows: use the nonspectral full-tail bound;
finite delicate windows: use the sharp D_+ certificate.
```

## Certificate

With `P=span_Q{0,1}`, `R=P^\perp`, and `A_1=[[B,C],[C^*,D]]`, define:

```text
lowMargin = -[Tr(B^3)+3Tr(BCC^*)].
```

The stable nonspectral tail is:

```text
tailFull = ||D||op(Tr(D^2)+3||C||_HS^2).
```

The sharp finite tail is:

```text
tailSharp = Tr(D_+^3)+3||D_+||op||C||_HS^2.
```

The hybrid certificate uses:

```text
tailUsed =
  tailSharp,  lambda=32,
  tailFull,   otherwise.
```

## Diagnostic

Script:

```text
E72_242_hybrid_hoc3_certificate.py
```

Output:

```text
E72.242 hybrid HOC3 certificate
Use nonspectral full tail except declared sharp finite windows.
lam L low tailUsed mode margin TrA13 status
 12 4.969813 1.094348e-02 7.593378e-03 full  3.350105e-03 -9.452352e-03 PASS
 16 5.545177 1.022382e-02 6.002100e-03 full  4.221717e-03 -9.305587e-03 PASS
 20 5.991465 1.124246e-02 4.826362e-03 full  6.416098e-03 -1.076469e-02 PASS
 24 6.356108 1.636695e-02 4.250174e-03 full  1.211678e-02 -1.568847e-02 PASS
 28 6.664409 1.386423e-02 3.962054e-03 full  9.902178e-03 -1.331685e-02 PASS
 32 6.931472 2.622823e-03 1.473216e-03 sharp 1.149606e-03 -2.110545e-03 PASS
 36 7.167038 1.636806e-02 2.139203e-03 full  1.422885e-02 -1.620182e-02 PASS
overall PASS
```

## Reading

The high-block odd cubic sublemma now has two proof routes:

```text
Sharp:
  prove E72.240 with D_+.

Hybrid:
  prove the nonspectral full-tail estimate in the stable/asymptotic regime,
  verify sharp finite exceptional windows.
```

The hybrid route is preferable for a written proof because the stable bound uses only:

```text
||D||op, Tr(D^2), ||C||_HS^2,
```

not a spectral positive projection.

## Next Exact Target

Promote the stable part to explicit scalar bounds:

```text
LOW:
  -[(3t_Bs_B-t_B^3)/2 + 3Tr(BCC^*)] >= c_low/L,

TAIL:
  ||D||op(Tr(D^2)+3||C||_HS^2) <= c_tail/L,

with c_low > c_tail.
```

Then handle the finite exceptional set by the sharp certificate.
