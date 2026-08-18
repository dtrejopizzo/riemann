# E93.002 - Direct closure theorem

## 1. Statement

Assume `DIRECT-BORDERED-ANCHOR` on a directed family satisfying the finite
resolution condition.  Then `Omega7` holds.

## 2. Proof

E80.002 proves

```text
E_L(s)/E_L(s_*)
 ->[xi(s)/xi(s_*)]^2                                 (2.1)
```

locally uniformly on `Re s>1` as `L->infinity`.
Combining (2.1) with E93.001(2.3) gives

```text
C_(L_alpha,N_alpha)(s)/C_(L_alpha,N_alpha)(s_*)
 ->[xi(s)/xi(s_*)]^2.                                (2.2)
```

On the real safe axis, (2.2) is `SR-SAFE`.  Every finite bilateral
characteristic is even and real-rooted.  Its normalized canonical product
satisfies the safe-axis domination theorem of P76.031.  Hence the family is
normal on the full plane, every sublimit is the normalized square of `xi`,
and Hurwitz excludes every nonreal zero of the limit.

Thus all zeros of `xi` are on the critical line, equivalently all Li--Keiper
coefficients are nonnegative. `QED`

## 3. Inputs not used

The proof does not use

```text
fixed-L convergence;
GAP-Z;
VITALI-Z;
LP;
BTG-DIV;
RDP-SHELL;
PROLATE or WEIL-TAIL;
endpoint eigenline dominance.                        (3.1)
```

These remain possible routes for constructing the same safe ratio, but they
are not hypotheses of the direct closure theorem.

## 4. Status

```text
proved:
  DIRECT-BORDERED-ANCHOR implies SR-SAFE, Omega7 and RH;

open:
  DIRECT-BORDERED-ANCHOR itself.
```

