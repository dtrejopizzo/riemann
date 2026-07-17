# E73.089 - Local HWIN from root-locking and companion residual

## 1. Purpose

This note turns E73.087--E73.088 into the precise sufficient theorem for `LOCAL-HWIN-5`.

The point is to avoid the false statement:

```text
all local nodes are small by root proximity.
```

The tested block has two mechanisms:

```text
1. root-locked local nodes;
2. companion nodes small by residual cancellation.
```

## 2. Finite Cauchy notation

Let

```text
C(t)=sum_n xi_n/(t-d_n),
H_0(i gamma)=-i C(-gamma).
```

Let `R(C)` be the finite real root set of `C`.

For a local critical node `gamma`, define:

```text
Delta(gamma):=dist(-gamma,R(C)),
M(gamma):=sup{|C'(t)| : t lies between -gamma and its nearest root}.
```

## 3. Root-locking lemma

**Lemma 89.1.**  For every local node whose interval to the nearest Cauchy root contains no pole,

```text
|H_0(i gamma)| <= Delta(gamma) M(gamma).
```

*Proof.*  Let `r` be the nearest root of `C`.  Then `C(r)=0`.  By the fundamental theorem of
calculus,

```text
C(-gamma)-C(r)=int_r^{-gamma} C'(t) dt.
```

Taking absolute values gives:

```text
|C(-gamma)| <= |-gamma-r| sup_[r,-gamma] |C'(t)|.
```

Since `|H_0(i gamma)|=|C(-gamma)|`, the claim follows.  `□`

## 4. Coefficient lemma

**Lemma 89.2.**  Fix `sigma>0`.  If `z=sigma+i eta` and `w=i gamma`, then:

```text
|A_L(z,w)|+|B_L(z,w)| <= 4(1+e^(sigma L))/sigma.
```

*Proof.*  On the critical line `|e^(wL)|=|e^(-wL)|=1`, and `|e^(zL)|=e^(sigma L)`.  Therefore the
numerators in `A_L` and `B_L` are each bounded by:

```text
2+2e^(sigma L).
```

Also:

```text
|w-z|>=sigma,
|w+z|>=sigma.
```

Adding the two coefficient bounds gives the displayed estimate.  `□`

## 5. Split local window

Decompose the canonical window:

```text
Z_loc(A,L)=Z_lock(A,L) union Z_comp(A,L).
```

`Z_lock` contains the nodes satisfying the root-proximity theorem.  `Z_comp` contains the fixed
finite companion nodes required for Hermite/confluent stability.

Define:

```text
N_lock(L)
:=
sum_{w=i gamma in Z_lock/+-}
(
 Delta(gamma)M(gamma)+Delta(-gamma)M(-gamma)
),
```

and:

```text
N_comp(L)
:=
sum_{w in Z_comp/+-}
(|H_0(w)|+|H_0(-w)|).
```

## 6. Sufficient theorem for LOCAL-HWIN

**Theorem 89.3.**  Suppose that, uniformly for every natural-height off-line cluster `A`,

```text
sum_{gamma_k in D_3(A,L)} W_k(A,L)
<= S_FAR(A,L),
```

and:

```text
e^(sigma L) S_FAR(A,L) (N_lock(L)+N_comp(L)) <= C_sigma L^-5.
```

Then `LOCAL-HWIN-5` holds.

*Proof.*  By Lemma 87.2 and Lemma 89.2:

```text
HWIN_k^loc
<=
C_sigma e^(sigma L)
sum_{w in Z_loc/+-}(|H_0(w)|+|H_0(-w)|).
```

On `Z_lock`, Lemma 89.1 bounds the nodal sum by `N_lock(L)`.  On `Z_comp`, it is bounded by
`N_comp(L)` by definition.  Hence:

```text
HWIN_k^loc <= C_sigma e^(sigma L)(N_lock(L)+N_comp(L)).
```

Multiplying by `W_k(A,L)` and summing over `D_3(A,L)` gives:

```text
sum_{gamma_k in D_3} W_k HWIN_k^loc
<=
C_sigma e^(sigma L) S_FAR(A,L)(N_lock(L)+N_comp(L)).
```

The assumed budget is `O(L^-5)`.  This is `LOCAL-HWIN-5`.  `□`

## 7. What remains genuinely open

The theorem isolates the two analytic tasks:

```text
LOCK-UNIF:
prove Delta(gamma)M(gamma) is small on the root-locked local nodes.

COMP-UNIF:
prove the fixed companion residual N_comp(L) is small enough for the same budget.
```

This is strictly sharper than blind HWIN: it does not ask for arbitrary enlarged windows and it does
not identify the FAR3 rows with the local divisor nodes.

## 8. Current route

The route is now:

```text
EXACT-PAIR-DIV
+ LOCK-UNIF
+ COMP-UNIF
+ FAR3-WCS
+ outside-window/tail absorption
=> scalar WRL.
```

E73.088 validates the finite calculus and shows the split is necessary in the present harness.
