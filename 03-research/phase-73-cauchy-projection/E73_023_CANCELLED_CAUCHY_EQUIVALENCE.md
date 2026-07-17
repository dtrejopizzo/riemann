# E73.023 - Cancelled Cauchy equivalence

## 1. E73 scalar atom

E73.022 rewrote the scalar dual gate as

```text
<xi,S_b>
= sum_{k in K_L} Pi(b,k) A(gamma_k),
```

where

```text
A(gamma)
=(exp(i gamma L)-1) sum_n xi_n/(gamma+d_n).
```

Here `xi` is real in the finite Hermitian CCM model.

## 2. Phase 72 cancelled Cauchy transform

E72.396 defines

```text
g_cancelled(w)
=(1-exp(wL)) sum_n xi_n/(i w-d_n).
```

At `w=i gamma`,

```text
i w-d_n = -gamma-d_n,
```

and therefore

```text
g_cancelled(i gamma)
=(1-exp(i gamma L)) sum_n xi_n/(-gamma-d_n)
=(exp(i gamma L)-1) sum_n xi_n/(gamma+d_n).
```

Thus

```text
A(gamma)=g_cancelled(i gamma).                         (1)
```

## 3. Consequence

The E73 rational-dual endpoint is not a new obstruction.  It is the E72 cancelled Cauchy projection
written in residue form:

```text
<xi,S_b>
= sum_{k in K_L} Pi(b,k) g_cancelled(k),
where k=i gamma_k.
```

Together with E73.002, this is precisely the finite Cauchy-Schur projection vector.

## 4. Correct remaining gate

The remaining natural-height theorem is:

```text
CC-PROJ:
max_{b in O_L} e^(Re b L)
|sum_{k in K_L} Pi(b,k) g_cancelled(k)| <= L^B.
```

This is the same as `NAT-PROJ`, but now:

```text
1. C_OO inverse has been removed by the residue kernel Pi(b,k);
2. critical data are identified as cancelled Cauchy values;
3. the scalar pairing is explicit and finite.
```

## 5. Status

```text
proved: E73 scalar atom equals E72 cancelled Cauchy value;
validated: E73.023 numerical check;
remaining: prove CC-PROJ through natural height.
```

This prevents duplicating gates.  E73 has not escaped `NAT-PROJ`; it has put it in its sharpest
scalar residue form.
