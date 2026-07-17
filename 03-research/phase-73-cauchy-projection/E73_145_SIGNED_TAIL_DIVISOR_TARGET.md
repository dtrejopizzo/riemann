# E73.145 - Signed Tail Divisor Target

Date: 2026-07-12.

## 1. What E73.143--144 changed

E73.142 gave a clean finite theorem:

```text
two-row invertibility + paired-packet smallness => LDIV_17.
```

E73.143 shows that demanding

```text
Pair^M small separately,
TailPair small separately
```

is too strong.

E73.144 shows the active finite packet almost proves `LDIV_17` by itself,
but one asymptotic transition row remains below the margin.

Therefore the correct theorem must retain the signed finite-tail
contribution.

## 2. Exact signed target

For each critical divisor node `w`, choose two rows `z_1,z_2` and define

```text
M_L(w)=
 [ A_L(z_1,w)  B_L(z_1,w) ]
 [ A_L(z_2,w)  B_L(z_2,w) ].
```

The exact complete/finite relation is

```text
Pair_z^infty(w)=Pair_z^M(w)+TailPair_z^M(w).
```

Thus

```text
[H_0(w),H_0(-w)]^T
 =
 M_L(w)^(-1)
 [
   Pair_{z_1}^M(w)+TailPair_{z_1}^M(w)
   Pair_{z_2}^M(w)+TailPair_{z_2}^M(w)
 ].
```

The load-bearing target is:

```text
SIGNED-TAIL-LDIV_17:

|| M_L(w)^(-1)
 [
   Pair_{z_1}^M(w)+TailPair_{z_1}^M(w)
   Pair_{z_2}^M(w)+TailPair_{z_2}^M(w)
 ] ||_1
<= C L^-17.
```

## 3. Why this is not tautological

It would be tautological to evaluate `TailPair` as

```text
Pair^infty - Pair^M
```

and then substitute the divisor formula for `Pair^infty`.

The non-circular proof must use the finite-tail formula from the Phase 72
packet calculus:

```text
TailPair_z^M(w)
= sum_n TailCell_z(w;n) xi_n,
```

with `TailCell` expressed by the explicit inactive mesh rows of
E72.349/E72.390--392.

The theorem to prove is therefore a signed row identity:

```text
M_L(w)^(-1)
(
 active packet row + inactive tail row
)
```

has small pairing with `xi_L`.

## 4. Current proof shape

The remaining analytic proof should have three pieces:

```text
INV_3:
||M_L(w)^(-1)|| <= C L^3.

TAIL-ROW-FORM:
TailPair_z^M(w) is the explicit inactive-mesh row applied to xi_L,
with no divisor substitution.

SIGNED-CANCELLATION:
after applying M_L(w)^(-1), the active row plus inactive row has
pairing O(L^-17) with xi_L.
```

Then:

```text
SIGNED-TAIL-LDIV_17
=> LDIV_17
=> CSV_17
=> Uniform GATE-73.
```

## 5. Next computation

The next verifier must compute the inactive tail row directly from
`tail_basis_row` / `p_infty-p_active`, not by subtracting from the divisor
identity.  It should report:

```text
active forced margin,
tail forced margin,
signed active+tail forced margin.
```

This will distinguish true signed-tail cancellation from accidental
smallness of the complete-mesh divisor.
