# E72.395 - Natural-height nodal system

## 1. Purpose

E72.392 absorbs the finite Fourier tail into the nodal system.  E72.394 closes the outside-zero tail
above the natural height

```text
T_L=e^L L^A.
```

Therefore the remaining compact branch is a finite nodal theorem on the natural-height zero window.
This note states the exact finite system and isolates the only remaining load-bearing assertion.

## 2. Natural-height window

Let

```text
Z(w)=xi(1/2+w)
```

and choose one representative from each pair `{w,-w}`.  Define

```text
W_L={w in Div(Z)/+- : |Im w|<=T_L},       T_L=e^L L^A.
```

This is finite for every `L`.

For an off-line contradiction, let

```text
alpha_L=max{Re w>0 : w in W_L}.
```

If there is no off-line zero in `W_L`, the compact contradiction window is empty at this `L`.  If
there is an off-line zero, define the maximal cluster

```text
A_L={a in W_L : Re a=alpha_L}.
```

## 3. Exact finite nodal system

At every node `a in W_L`, the paired finite packet equation gives

```text
Lambda_L G_x(a)
= sum_{w in W_L} K^M_{a,w}(L)G_x(w)
  + High_L(a),                                       (1)
```

where:

```text
Lambda_L=mu+e_pole-2kappa_*,
High_L(a)=sum_{w notin W_L} F_{B_a^M}(w),
```

and E72.394 gives

```text
High_L(a)=O(L^B).
```

Separating the self-pair and using E72.391--E72.392, (1) can be written as

```text
sum_{w in W_L} N^M_{a,w}(L) G_x(w) = O(L^B),          (2)
```

where

```text
N^M_{a,w}(L)
= N^infty_{a,w}(L)+T^M_{a,w}(L),
```

`K^M_{a,w}` denotes the nodal coefficient after factoring the finite paired transform through the
nodal vector `G_x(w)`.  `N^infty` is the complete-mesh zero-node matrix of E72.322--E72.324, and

```text
T^M_{a,w}=2iw R_M(a,w)/L
```

is the absorbed finite-tail matrix of E72.392.

Equation (2) is the exact finite natural-height nodal system.

## 4. Maximal block

On the maximal cluster `A_L`, E72.324 gives

```text
N^infty_{a_j,a_k}(L)
= -e^(a_jL)/(a_j+a_k) + lower exponential terms.
```

Equivalently,

```text
N^infty_A(L)
= -diag(e^(a_jL)) C_A + Low_A(L),
C_A(j,k)=1/(a_j+a_k).
```

The Cauchy determinant gives `det C_A != 0`, including the confluent variant of E72.325 when
multiplicities occur.

E72.392 gives

```text
diag(e^(-a_jL))T^M_A(L)=O(L^2/M^2).
```

Thus, for `M>=L^(1+epsilon)`,

```text
N^M_A(L)
= -diag(e^(a_jL)) [C_A+o(1)] + Low_A(L).             (3)
```

For clusters with large Cauchy condition number, the cutoff power must dominate that condition:

```text
||C_A^(-1)|| L^2/M^2=o(1).                            (4)
```

In fixed height windows this is automatic after choosing a sufficiently large polynomial power for
`M`.  In natural-height windows it becomes part of the finite geometry requirement in `NAT-NODAL`.

## 5. Remaining finite assertion

The only part not yet proved is that lower-real-part couplings from

```text
W_L \ A_L
```

are perturbative after descending real-part induction, uniformly for the natural-height window.

The proof-facing finite assertion is:

```text
NAT-NODAL:
For every L and every maximal positive-real-part cluster A_L,
the Schur complement of N^M(L) on A_L satisfies

   S_A(L)
   = -diag(e^(a_jL))[C_A+o(1)]

with inverse norm

   ||S_A(L)^(-1)|| <= C_L e^(-alpha_L L)L^B

where C_L is allowed to depend polynomially on the finite window geometry but not exponentially on L.
```

Then (2) gives

```text
G_x(a)=O(e^(-alpha_L L)L^B)
```

for every `a in A_L`.  Descending induction over the finite set of positive real parts in `W_L`
suppresses all off-line nodes in the natural-height window.

## 6. Why this is the correct endpoint

All previous non-nodal gates have now been removed:

```text
finite Fourier tail: absorbed by E72.391--E72.392;
outside high zero tail: closed by E72.394;
critical-line nodes: polynomial by E72.327;
maximal Cauchy block: invertible by E72.324--E72.325.
```

Thus the remaining theorem is not an analytic tail estimate and not a prime-sum estimate.  It is a
finite Schur-complement theorem for the natural-height Cauchy nodal matrix.

## 7. Status

```text
proved: exact finite natural-height nodal system (2);
proved: maximal block and absorbed tail structure (3);
open:   NAT-NODAL Schur-complement perturbation bound for lower-real-part couplings.
```
