# E73.235 - APR coefficient collapse and the finite divisibility target

Date: 2026-07-14.

## 1. Purpose

E73.234 proves that U4 is the adjoint form of the Cauchy-principal residual:

```text
APR-U4:
|A_L[B_{a,w}^{xi}]-P_L[B_{a,w}^{xi}]
 - sum_k A_ak(w) q_k xi_L| <= A_M L^(-M).
```

This note removes the principal subtraction from the formula.  It shows that
APR-U4 is exactly the closed eta-packet center already intervalized in
E73.222--E73.230.

The result is not another reformulation.  It identifies the finite
divisibility condition that remains:

```text
eta_w=(I-P_w)xi_L lies in ker Q_w,
and the explicit formula cell applied to the eta-packet is rapidly small.
```

## 2. Principal subtraction equals eta replacement

Let

```text
Q=Q_w,       P=Q^*(QQ^*)^(-1)Q,       R=I-P,
eta=Rxi.
```

The Cauchy-principal action is

```text
A(w)=QH_LQ^*(QQ^*)^(-1).
```

For row `a`,

```text
(A(w)Qxi)_a
= q_aH_LQ^*(QQ^*)^(-1)Qxi
= q_aH_LPxi.
```

Therefore

```text
q_aH_Lxi - (A(w)Qxi)_a
= q_aH_L(I-P)xi
= q_aH_Leta.                                      (1)
```

Since `H_L=H_model,L-Prime_L`, (1) is exactly:

```text
A_L[B_{a,w}^{xi}]-P_L[B_{a,w}^{xi}]
-sum_k A_ak(w)q_kxi
= A_L[B_{a,w}^{eta}]-P_L[B_{a,w}^{eta}],          (2)
```

where

```text
B_{a,w}^{eta}(y)=q_a Q_L(y)eta.
```

Thus the principal residual has already been converted into the closed
eta-packet center in E73.220--E73.230.

## 3. Finite coefficient form

The eta-packet has the finite expansion

```text
B_{a,w}^{eta}(y)
= sum_omega c_omega e^(iomega y)
 + y sum_omega l_omega e^(iomega y).
```

The closed residual is

```text
C_{a,w}
= sum_omega c_omega W_omega
 + sum_omega l_omega V_omega
 + E_exp.                                        (3)
```

Here `W_omega,V_omega` are the explicit Gamma-prime weights from E73.222.

Equation (2) proves:

```text
APR-U4
<=> rapidly small coefficient/weight sum (3)
```

under the exact Cauchy annihilation constraint

```text
Q_w eta=0.                                      (4)
```

## 4. The finite divisibility statement

The remaining theorem is now:

```text
ETA-DIV:
For eta_w=(I-P_w)xi_L, whose coefficient vector satisfies Q_w eta_w=0,
the finite coefficient/weight sum

sum_omega c_omega(eta_w) W_omega
+sum_omega l_omega(eta_w) V_omega

is O_M(L^-M) for all M.
```

This is the same U4 content, but it has no matrix shorthand left.  It is a
finite divisibility problem for:

```text
1. the coefficient maps eta -> (c_omega,l_omega);
2. the two exact Cauchy constraints Q_w eta=0;
3. the Gamma-prime weights W_omega,V_omega.
```

## 5. Why this is the correct endpoint

The old routes tried to prove smallness by:

```text
rowspace projection,
pseudoinverse reconstruction,
Cauchy-plane eigen branch,
commutator norm.
```

E73.234--E73.235 show that all of those collapse to the same scalar:

```text
C_{a,w}=q_aH_L(I-P_w)xi_L.
```

The only non-circular proof can therefore use extra structure not visible in
generic Hilbert geometry.  In the current coordinates, that structure is the
finite coefficient divisibility forced by `Q_w eta=0`.

## 6. Status

```text
proved: APR principal residual = closed eta-packet coefficient sum;
proved: U4 = ETA-DIV finite coefficient/weight divisibility;
next: derive algebraic consequences of Q_w eta=0 on the coefficient vector
      (c_omega,l_omega) and test whether they explain the rapid cancellation.
```

