# E73.085 - Local HWIN target

## 1. Purpose

E73.084 shows that the exact HWIN budget depends strongly on the chosen zero window.  The correct
main theorem is local: it should use the finite zero window required by the Cauchy projection block,
not an arbitrary enlarged list of critical heights.

## 2. Local window

Let `Z_loc(A,L)` be the finite paired zero-node window used by the maximal Cauchy projection block for
the off-line cluster `A`.

This window is fixed before the estimate and contains only the nodes needed for the local block.
Outside-window nodes are handled by the Phase 72 outside-window and tail mechanisms.

## 3. Local HWIN

For a FAR3 evaluation node `z_k`, define:

```text
HWIN_k^loc
:= sum_{w in Z_loc(A,L)/+-}
   ( |A_L(z_k,w)||H_0(w)| + |B_L(z_k,w)||H_0(-w)| ).
```

## 4. Local theorem

The main theorem becomes:

```text
LOCAL-HWIN-5:
sum_{gamma_k in FAR3(A,L)}
W_k(A,L) HWIN_k^loc
<= C L^-5.
```

## 5. Why local is necessary

The enlarged-window experiment E73.084 shows:

```text
small local windows: Pref*HWIN = L^-11 to L^-16;
larger windows:      Pref*HWIN may approach L^-5.
```

Thus a large-window HWIN bound would mix local forcing with outside-window control.  That is not the
architecture of the Phase 72 route: outside-window terms have their own contour/tail mechanism.

## 6. Updated route

The current route is:

```text
LOCAL-HWIN-5
+ TAIL-NODAL-5
+ OUTSIDE-WINDOW-POLY
+ Tail_3<=C_tail L^-9
=> BUD-5/9
=> WCS
=> scalar WRL.
```

## 7. Status

```text
proved: complete-mesh pair ideal membership;
observed: local HWIN has sufficient slack in tested windows;
open: prove LOCAL-HWIN-5 uniformly for the natural-height local block.
```
