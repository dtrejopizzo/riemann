# E72.240 - HOC3 finite certificate

## Purpose

This note packages E72.235--E72.239 into a finite certificate for the high-block odd cubic sign:

```text
HOC3: Tr(A_1^3) <= 0,
A_1=sum_{0.60L<log n<=L} A_n^+.
```

The proof is not by diagonalizing `A_1`. It uses the explicit two-mode projection:

```text
P=span_Q{0,1},      R=P^\perp,
A_1=[[B,C],[C^*,D]].
```

## Algebraic certificate

The exact block identity is:

```text
Tr(A_1^3)
= Tr(B^3)+Tr(D^3)+3Tr(BCC^*)+3Tr(DC^*C).        (BCI)
```

For the `2x2` block `B`, write:

```text
t=Tr(B),       s=Tr(B^2).
```

Then:

```text
Tr(B^3) = (3ts-t^3)/2.                           (2x2C)
```

The tail is bounded by:

```text
Tr(D^3)+3Tr(DC^*C)
<= Tr(D_+^3)+3||D_+||op ||C||_HS^2.              (TOB)
```

Therefore HOC3 follows from the scalar inequalities:

```text
t<0,
3s-t^2>0,

-[(3ts-t^3)/2 + 3Tr(BCC^*)]
>= Tr(D_+^3)+3||D_+||op||C||_HS^2.               (HOC3-CERT)
```

This is the finite certificate.

## Diagnostic

Script:

```text
E72_240_hoc3_finite_certificate.py
```

Output:

```text
E72.240 HOC3 finite certificate
PASS iff t<0, 3s-t^2>0, and lowMargin>=tailBound.
lam L tB gap lowMargin tailBound certMargin TrA13 status
 12 4.969813 -2.018045e-01 +1.007822e-01 1.094348e-02 3.860581e-03 7.082902e-03 -9.452352e-03 PASS
 16 5.545177 -1.908920e-01 +1.059321e-01 1.022382e-02 2.947212e-03 7.276605e-03 -9.305587e-03 PASS
 20 5.991465 -2.119065e-01 +1.026946e-01 1.124246e-02 2.147375e-03 9.095084e-03 -1.076469e-02 PASS
 24 6.356108 -2.375759e-01 +1.346332e-01 1.636695e-02 1.959834e-03 1.440712e-02 -1.568847e-02 PASS
 28 6.664409 -2.162864e-01 +1.264122e-01 1.386423e-02 1.679917e-03 1.218431e-02 -1.331685e-02 PASS
 32 6.931472 -1.153524e-01 +3.550938e-02 2.622823e-03 1.473216e-03 1.149606e-03 -2.110545e-03 PASS
 36 7.167038 -2.388454e-01 +1.345642e-01 1.636806e-02 8.733170e-04 1.549474e-02 -1.620182e-02 PASS
overall PASS
```

Here:

```text
gap        = 3s-t^2,
lowMargin  = -[(3ts-t^3)/2 + 3Tr(BCC^*)],
tailBound  = Tr(D_+^3)+3||D_+||op||C||_HS^2,
certMargin = lowMargin-tailBound.
```

## Reading

The finite certificate passes through the tested stable windows, including the delicate dip at
`lambda=32`:

```text
certMargin(lambda=32)=1.149606e-03 > 0.
```

The result is stronger than observing `Tr(A_1^3)<0`: it proves the sign inside the finite model by a
specific low-block/tail domination inequality.

## What Is Proved Here

This closes the high-block odd cubic sublemma in the current finite arithmetical model, conditional on
promoting the tested scalar inequalities to exact finite-cycle/asymptotic estimates:

```text
t<0,
3s-t^2>0,
lowMargin>=tailBound.
```

It does not by itself close Omega7/RH. It supplies the missing proof architecture for the odd
high-block sign in the fixed certificate package.

## Next Reduction

To make HOC3 a theorem rather than a verified certificate, prove the three scalar bounds without
numerical diagonalization:

```text
LOW1: t_B <= -a/L,
LOW2: 3s_B-t_B^2 >= b/L,
TAIL: Tr(D_+^3)+3||D_+||op||C||_HS^2 <= c/L,
```

with the resulting explicit inequality:

```text
lowMargin(L) - tailBound(L) >= eta/L > 0
```

outside finitely many windows, and verify the finite exceptional windows exactly.
