# E80.008 - Radical-tail cut audit

## 1. Exact decomposition

Let `k` be the full radical vector, `k_lambda` its compact/prolate
approximation, and `P_N` the Fourier cutoff.  The inherited identity is

```text
M_{L,N}P_N k_lambda
 = P_rows Q_W(k_lambda-k)
   + P_rows(Q_{W,L}-Q_W)k
   + FourierShell_{L,N}(k_lambda).                    (1.1)
```

The three summands are denoted `t^P`, `t^W`, and `t^F`.  The full radical
identity `Q_W(k,phi)=0` is unconditional because the transform of `k` vanishes
on its own complete divisor.  It gives (1.1), but it does not estimate any of
the three terms after the bordered response is applied.

## 2. Why absolute tail decay is insufficient

The selected safe response defines, after normalization, a linear functional
`Lambda_{L,N,sigma}` on row residuals.  The required statements have the form

```text
sup_{sigma in K}|Lambda_{L,N,sigma}(t^P_{L,N})| -> 0,
sup_{sigma in K}|Lambda_{L,N,sigma}(t^W_{L,N})| -> 0.    (2.1)
```

### Proposition 2.1

Norm convergence `||t_N||->0` does not imply
`Lambda_N(t_N)->0` when the response functionals are not uniformly bounded.

### Proof

Take the one-dimensional normed space, `t_N=1/N`, and
`Lambda_N(x)=Nx`.  Then `t_N->0` while `Lambda_N(t_N)=1`. `QED`

The large bordered amplification recorded in the earlier autopsy is exactly
this obstruction.  Therefore double-exponential physical tails, rapid Fourier
coefficient decay, or small row norms do not by themselves close (2.1).

## 3. A sufficient non-positive theorem

Let `X` be a locally convex space of test vectors with seminorms `p_m`.  Assume
that, for every safe compact `K`, there are `m` and `C_K` such that

```text
sup_{L,N} sup_{sigma in K}
|Lambda_{L,N,sigma}(P_rows Q_W(f))|
 <= C_K p_m(f),                                        (3.1)
```

and an analogous estimate holds for the truncated difference
`P_rows(Q_{W,L}-Q_W)f`.  Suppose also

```text
p_m(k_lambda-k) -> 0,                                  (3.2)

sup_N p_m^*(P_rows(Q_{W,L}-Q_W)k) -> 0,                (3.3)
```

where `p_m^*` is the source seminorm appearing in the second continuity
estimate.

### Theorem 3.1 - directional tail continuity

Under (3.1)--(3.3), the PROLATE and WEIL-TAIL limits in (2.1) hold locally
uniformly on the safe axis.

### Proof

Apply (3.1) to `f=k_lambda-k` and use (3.2).  Apply the analogous truncated
estimate to `k` and use (3.3).  No sign or positivity inequality enters.
`QED`

The proof-facing open theorem is therefore

```text
DIRECTIONAL-TAIL-CONTINUITY:
  prove (3.1) in a topology in which the prolate and Weil truncation tails
  converge.                                             (3.4)
```

This is stronger than estimating the two particular tails, but much weaker
than a uniform norm bound for the full bordered inverse: it controls only the
actual Weil-generated residual subspace.

## 4. Fourier term and RDP-SHELL

The Fourier term has a different mechanism.  Repeated Abel summation and the
rank-two displacement identity reduce it to shell moments.  The inherited
sufficient theorem is

```text
RDP-SHELL
  => summable control of Lambda_{L,N,sigma}(t^F_{L,N})                  (4.1)
```

on safe compact sets.  Neither (3.4) nor RDP-SHELL implies the other:
`DIRECTIONAL-TAIL-CONTINUITY` concerns physical and Weil truncation directions,
while RDP-SHELL concerns the moving Fourier collar.

## 5. Relation with RDI

RDI supplies local convergence of normalized bilateral characteristic ratios.
It does not, without an additional representation theorem, bound the response
functional on the residual space used in (3.1).  Conversely, the tail
continuity theorem does not identify the Euler--Gamma logarithmic derivative.

Thus the radical-tail front cannot be declared infrastructure already closed
by RDI.  It is a separate directional stability theorem.  Its admissible proof
method is continuity of a signed functional on the actual tail subspace, not
positivity of the Weil form and not an ambient inverse norm.

## 6. Minimal downstream cut

The downstream module is now exactly

```text
DS-1  RDP-SHELL;
DS-2  DIRECTIONAL-TAIL-CONTINUITY for PROLATE;
DS-3  DIRECTIONAL-TAIL-CONTINUITY for WEIL-TAIL;
DS-4  common cofinal diagonal with LP and RDI.            (6.1)
```

The cofinal diagonal `DS-4` is already available abstractly once the first
three limits and the LP/RDI limits have been proved.  Hence the live
mathematics is `DS-1`--`DS-3`.

## 7. Status

```text
proved:
  absolute tail smallness cannot survive an unbounded response automatically;
  the directional-tail continuity theorem;
  no positivity argument is needed for that theorem;

closed:
  classification of the downstream radical-tail cut;
  common diagonal assembly as a separate source of difficulty;

reduced:
  PROLATE and WEIL-TAIL to DS-2 and DS-3 on the actual residual subspace;

open:
  RDP-SHELL;
  DS-2 and DS-3;
  an exact representation or estimate proving (3.1) for the CCM response;

separate:
  these statements neither prove nor follow formally from RDI.
```

