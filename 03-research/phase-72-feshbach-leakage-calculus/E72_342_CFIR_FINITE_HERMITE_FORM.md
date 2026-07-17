# E72.342 -- CFIR as a finite Hermite form

**Purpose.** Turn the balanced finite-window target of E72.341 into a precise finite Hermite identity.
This is the form in which the remaining analytic theorem can be attacked without outside-zero tails,
absolute prime bounds, or hidden smoothness assumptions.

## 1. Finite zero window and jet map

Fix a zero-pair representative window

```text
W_T={(a_j,m_j): 1<=j<=J},
```

where `a_j` is a shifted zero representative of `Z(w)=xi(1/2+w)` and `m_j` is its multiplicity.  Define
the Hermite jet map

```text
J_T F := { F^(p)(a_j)/p! : 1<=j<=J, 0<=p<m_j }.
```

All constants below may depend on this fixed window but not on `L`.

## 2. Complete-mesh finite interpolation operator

Let `Pair_z^infty(w)` be the complete-mesh paired packet from E72.321.  Away from `z=+-w`,

```text
Pair_z^infty(w)=K_L(z,w)G_x(w),
```

with

```text
K_L(z,w)
= [ w(1+e^(zL))(1-e^(-wL))
    + z(1-e^(zL))(1+e^(-wL)) ]/(w^2-z^2).            (1)
```

On the diagonal `z=w` and in confluent cases, the operator is defined by the original removable
integral value

```text
Pair_z^infty(w)=M_z(w)+M_z(-w),
```

then differentiated in the Hermite sense.  This convention reproduces

```text
Pair_a^infty(a)=[L+sinh(aL)/a]G_x(a)
```

for a simple node.

Define the finite Hermite interpolation operator `I_T^H` by

```text
(I_T^H G)(z)
:= sum_{j=1}^J m_j Pair_z^infty(a_j),
```

with diagonal and confluent values interpreted by the removable/Hermite convention above.

## 3. The nodal Hermite matrix

Define the finite matrix

```text
H_T(L) J_TG := J_T[ Lambda_LG - I_T^H G ].            (2)
```

For simple nodes this has entries

```text
H_T(a,a)=Lambda_L - L - sinh(aL)/a,
H_T(a,b)=-K_L(a,b),              a != b.
```

For multiplicities, the entries are the corresponding confluently differentiated removable values:

```text
H_T[(j,p),(k,q)]
= coefficient of G_x^(q)(a_k)/q!
  in (1/p!) partial_z^p [ Lambda_LG_x(z)-I_T^HG_x(z) ]|_{z=a_j},
```

with every diagonal/confluent coefficient computed from the original removable integral formula, not
by differentiating a singular quotient blindly.

The leading maximal-real-part block of `H_T(L)` is exactly the E72.324--E72.325 block

```text
-diag(e^(a_jL)) C_conf,

C_conf[(j,p),(k,q)]
= (-1)^(p+q) binom(p+q,p)/(a_j+a_k)^(p+q+1).          (3)
```

Thus this finite matrix is already known to be invertible at the leading exponential scale on every
maximal off-line cluster.

## 4. Signed window tail in closed form

Write the finite packet split as

```text
F_z^M(w)=Pair_z^infty(w)-TailPair_z^M(w).
```

From E72.333, for a tail index `|m|>M` and active `n`,

```text
M_{m,n}(w)
=(1-e^(wL))[Phi_w(d_m)-Phi_w(d_n)]/[pi(n-m)],
Phi_w(d)=d/(w^2+d^2).
```

Since `Phi_{-w}=Phi_w`,

```text
M_{m,n}(w)+M_{m,n}(-w)
= [2-e^(wL)-e^(-wL)]
   [Phi_w(d_m)-Phi_w(d_n)]/[pi(n-m)].                (4)
```

Therefore the finite signed window tail is

```text
Tail_T^M(z)
= sum_{j=1}^J m_j sum_{|m|>M} (1-e^(zL))/(iz-d_m)
   sum_{n active} xi_n
   [2-e^(a_jL)-e^(-a_jL)]
   [Phi_{a_j}(d_m)-Phi_{a_j}(d_n)]/[pi(n-m)].         (5)
```

This is a single explicit signed series.  It is not to be replaced by the sum of absolute values.

E72.343 strengthens (5): the signed series equals complete closed mesh minus active finite mesh, so
`Tail_T^M` has a fully finite formula.

## 5. CFIR finite Hermite theorem

E72.341 gives

```text
Rem_T^M(z)=Lambda_LG_x(z)-(I_T^HG_x)(z)+Tail_T^M(z).
```

Applying `J_T` yields the exact finite vector identity

```text
J_T Rem_T^M
= H_T(L)J_TG_x + J_T Tail_T^M.                       (6)
```

Thus the current analytic endpoint can be stated as the finite Hermite assertion:

```text
CFIR-H:
|| H_T(L)J_TG_x + J_T Tail_T^M || <= C_T L^B.         (7)
```

By (3), `CFIR-H` implies exponential suppression of all off-line Hermite jets in the window, after the
standard descending maximal-real-part induction of E72.324--E72.326.

## 6. Non-circular version

The expression in (7) must not be proved by identifying it with `J_T Rem_T^M` and estimating an
outside zero sum.  The non-circular finite object is obtained by substituting the transformed
Feshbach equation before zero expansion:

```text
Def_CFIR,T
:= J_T[
   T_W02(z)[xi] - T_WR(z)[xi] - T_Prime(z)[xi]
   - 2kappa_*G_x(z)
   - I_T^H G_x(z)
   + Tail_T^M(z)
].
```

Using E72.317--E72.321, this equals the left side of (7).  Hence the proof target is:

```text
FINITE-CFIR:
||Def_CFIR,T|| <= C_TL^B,                             (8)
```

where every term is a finite archimedean/prime/Fourier expression plus the signed tail (5).  This is
the finite explicit identity to prove.  After E72.343, the signed tail itself is finite.

## 7. Status

```text
proved: CFIR reduces to the finite Hermite vector identity (6);
proved: the window tail has the signed coefficient formula (5), collapsed to a finite expression in
        E72.343;
proved: the leading off-line block of H_T(L) is the invertible confluent Cauchy block;
open: prove FINITE-CFIR directly from the coupled transformed Feshbach operator, not from the
      outside zero sum.
```
