# E81.004 - Exact two-generator formula for the secular residues

## 1. Inner displacement data

Let

```text
M=H_{N-1}-mu_N I,
D=diag(d_j),
s=(S_L(d_j))_j,
R_b=(D-d_b I)^(-1).                                   (1.1)
```

Define the two generator solutions

```text
u=M^(-1)s,
v=M^(-1)1,                                             (1.2)
```

and the two boundary scalars

```text
p=v^T R_b(s-S_b 1),
r=u^T R_b(s-S_b 1).                                    (1.3)
```

The exact rank-two displacement formula gives

```text
x=M^(-1)b
 =-(2/L)R_b(u-S_bv)
  -(4/L^2)R_b(u v^T-v u^T)R_b(s-S_b1).                (1.4)
```

## 2. Cancellation of the moving boundary denominator

Let

```text
q_j=d_j-d_b,
a_j=q_j x_j.                                           (2.1)
```

### Proposition 2.1

Put

```text
alpha_b=2/L+4p/L^2,
beta_b=-2S_b/L-4r/L^2.                                 (2.2)
```

Then the complete secular residue vector satisfies

```text
a=-alpha_b u-beta_b v.                                 (2.3)
```

### Proof

Multiplication of (1.4) by `D-d_b I` cancels `R_b`.  Moreover,

```text
(u v^T-v u^T)R_b(s-S_b1)=p u-r v.                     (2.4)
```

Hence

```text
a=-(2/L)(u-S_bv)-(4/L^2)(p u-r v),
```

which is exactly (2.3). `QED`

## 3. Recovery of the two-generator numerator

Define

```text
U(z)=sum_j u_j/(z-d_j),
V(z)=sum_j v_j/(z-d_j),
U_b=sum_j u_j/(d_j-d_b),
V_b=sum_j v_j/(d_j-d_b).                               (3.1)
```

Since `c=1-sum_j x_j=1-sum_j a_j/(d_j-d_b)`, Proposition 2.1 gives

```text
c=1+alpha_b U_b+beta_b V_b.                            (3.2)
```

Substitution into the denominator-free secular function yields

```text
G(z)
 = c-sum_j a_j/(z-d_j)
 = 1+alpha_b[U(z)+U_b]+beta_b[V(z)+V_b].               (3.3)
```

This is exactly the two-generator numerator of P76.041, now derived from the
bordered spectral-shift residues.

Differentiating gives

```text
G'(z)=alpha_b U'(z)+beta_b V'(z),                      (3.4)

G'(z)/G(z)
 = [alpha_b U'(z)+beta_b V'(z)]
   /[1+alpha_b(U(z)+U_b)+beta_b(V(z)+V_b)].             (3.5)
```

## 4. Loop theorem

### Theorem 4.1

The following finite objects are identical representations of the same
scalar function:

```text
bordered determinant ratio;
denominator-free secular function G;
rank-two displacement residue formula;
two-generator numerator.                               (4.1)
```

Consequently, constructing the spectral-shift measure from the zeros of `G`
does not provide an independent arithmetic comparison object.  It is a
nonlinear repackaging of the coupled generator quotient (3.5).

### Proof

E81.002 proves the first two identities.  Proposition 2.1 proves the residue
formula.  Equations (3.2)--(3.3) prove equality with the two-generator
numerator. `QED`

## 5. Correct remaining target

The independent object remains `E_L`.  The arithmetic step is therefore the
outer asymptotic identity

```text
i G_L'(iu)/G_L(iu)-i G_L'(-iu)/G_L(-iu)
 = H_L(s)-d/ds log A_L(s)+o_L(1),                     (5.1)
```

locally uniformly on safe complex domains, where `G_L` is first obtained as
the fixed-`L` limit of (3.3).

In generator coordinates, (5.1) asks for the joint continuum limit of

```text
alpha_b U+beta_b V,
alpha_b U'+beta_b V',                                  (5.2)
```

with numerator and denominator kept coupled.  This is the corrected
`COUPLED-LOEWNER-REM` endpoint, not a new spectral-shift shortcut.

## 6. Status

```text
proved:
  exact secular residue formula a=-alpha_b u-beta_b v;
  exact recovery of the two-generator numerator;
  the loop theorem (4.1);

closed:
  search for an independent arithmetic measure obtained merely by taking the
  zeros of the bordered determinant;

corrected:
  the spectral-shift measure is an independent finite cell object but is not
  an independent Euler--Gamma comparison object;

reduced:
  RDI-ANCHOR to the coupled generator outer limit (5.1)--(5.2);

open:
  fixed-L continuum limits of the two generator combinations;
  their outer identification with H_L;

next:
  derive a continuum equation for the coupled generator directly from
  M u=s and M v=1, retaining the inhomogeneous source.
```

