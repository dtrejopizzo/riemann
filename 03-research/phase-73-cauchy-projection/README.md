# Phase 73 - Cauchy projection gate

## Entry point

Phase 72 reduced the transformed compact branch to a finite natural-height nodal system.

Closed before entering this phase:

```text
SFREQ / D2BV at natural height                         [E72.388--E72.389]
finite Fourier tail as Cauchy nodal operator           [E72.390--E72.392]
outside high zero tail above T_L=e^L L^A               [E72.394]
natural-height nodal system                            [E72.395]
Cauchy-Schur projection formulation                    [E72.396]
```

The remaining finite identity is:

```text
NAT-PROJ:
max_{a in O_L} e^(Re a L)
 |(C_OO^(-1) C_OK G_K)_a| <= L^B.
```

Here:

```text
O_L={shifted zero representatives in W_L with Re w>0},
K_L={shifted zero representatives in W_L with Re w=0},
W_L={|Im w|<=e^L L^A}/+-,
C_OO(a,b)=1/(a+b),
C_OK(a,k)=1/(a+k),
G_K(k)=G_x(k).
```

If `NAT-PROJ` holds, E72.396 gives off-line nodal suppression.  E72.326 then propagates this to
`PW-Cauchy`, and the compact route continues to `NZ-MSD`, scalar WRL, and Omega7.

## Phase 73 objective

Prove `NAT-PROJ`, or reduce it to an even sharper finite identity involving only the CCM pole-even
equation and the critical-line divided-difference structure of `G_x`.

The first task is to understand whether `C_OO^(-1)C_OKG_K` has an algebraic cancellation caused by:

```text
1. the pole-even Cauchy numerator;
2. critical-line divided differences;
3. finite Weyl root relations;
4. Hermite interpolation on the Cauchy kernel.
```

## Current endpoint after E73.039

The phase reduced `NAT-PROJ` to a scalar positive covering estimate.

Closed reductions:

```text
E73.023: cancelled Cauchy values equal the Phase 72 critical data;
E73.026: confluent Hermite coordinates remove cluster-coordinate blow-up;
E73.031: absolute geometry alone cannot overcome e^(alpha L);
E73.033: universal Hermite moment cancellation is not present;
E73.036: positive factor budget is sufficient and survives the incoherent-ceiling audit;
E73.037: Hermite kernel has an explicit Taylor-Cauchy bound;
E73.038: finite Cauchy transform has an exact numerator divisor;
E73.039: mesh-root covering implies the positive factor budget;
E73.040: absolute root-derivative covering is too weak;
E73.041: signed variation root covering does not improve the final budget;
E73.043: global product decoupling is too lossy;
E73.044: WCS mass is concentrated on very few critical nodes;
E73.045: dominant-node split gives the next finite certificate format;
E73.046: geometry-only dominant selection fails;
E73.047: arithmetic dominant selection is the current target;
E73.048: finite-divisor far proxy selects the dangerous nodes;
E73.049: FAR-DNS is the current theorem target;
E73.050: FAR top-3 remains stable as the critical window grows;
E73.051: FAR top-3 tail is tiny in tested windows;
E73.052: FAR3 is the current finite certificate form;
E73.053: global quotient tail bound fails;
E73.054: nodewise rational FAR3 certificate is the current endpoint;
E73.055: executable FAR3-nodewise verifier validates tested windows;
E73.056: finite certificate schema records the current sharp endpoint;
E73.057: effective budget exponents are measured;
E73.058: BUD-5/9 is the current uniform theorem target;
E73.059: FAR3 main smallness comes from C_x, not geometry;
E73.060: CMAIN-10 is the current main-term target;
E73.061: CMAIN comes from denominator-numerator exponent gap;
E73.062: DEN-GAP-10 is the current arithmetic target;
E73.063: absolute L1 Cauchy bound is too weak;
E73.064: SIGNED-CMAIN is the current arithmetic core.
```

The current sufficient chain is now:

```text
BUD-5/9
=> FAR3-nodewise
=> FAR3
=> FAR-DNS
=> ADNS
=> DNS
=> WCS
=> PFD
=> DATA-HERM
=> CC-PROJ
=> NAT-PROJ
=> scalar WRL.
```

Here `WCS` is the direct weighted Cauchy smallness estimate:

```text
e^(alpha L) sum_{gamma_k in K_L}
G_theta,m(a,i gamma_k)
|1-exp(i gamma_k L)|
|C_x(i gamma_k)|
<= L^B,
```

where `G_theta,m` is the explicit Taylor-Cauchy Hermite kernel bound from E73.037.

Thus the remaining theorem is no longer a matrix inverse statement.  It is a finite scalar weighted
Mellin-Cauchy estimate involving:

```text
1. Hermite geometry of a hypothetical off-line cluster;
2. mesh phase |1-exp(i gamma L)|;
3. finite Cauchy spectral defect |C_x(i gamma)|.
```

The finite Cauchy divisor remains useful diagnostically, but E73.040--E73.041 show that proving the
gate through a separate root-distance covering theorem does not currently simplify the problem.

The newest finite certificate format is `ADNS`: choose a small set of dominant critical nodes using
structural arithmetic divisor data plus the geometric-mesh envelope, certify those nodes directly,
and control the complement by a coarser tail estimate.

E73.046 shows that the purely geometric-mesh choice does not capture the dangerous nodes.  The
dominant selector must use structural arithmetic data, such as the finite divisor of `P_x` in
`C_x=P_x/D_x`, while still avoiding direct sorting by the final WCS terms.  This is the `ADNS`
target of E73.047.

E73.048 identifies the working proxy: dangerous nodes are far from the numerator divisor
`Div(P_x)`.  The current target is therefore `FAR-DNS`: rank critical nodes by

```text
e^(alpha L)G_theta,m(a,i gamma)|1-exp(i gamma L)| dist(-gamma,Div(P_x)).
```

E73.050--E73.052 refine this to `FAR3`: use the top three FAR nodes as the main certificate and
prove the remaining positive tail is small.

E73.053 rejects a global quotient bound for the tail.  E73.054 keeps the surviving form: certify
each WCS term by the finite rational identity `C_x=P_x/D_x`, with FAR selecting the three main
nodes and explicit budgets for the remaining positive tail.

E73.055 implements this as an executable verifier, and E73.056 abstracts it into a finite
certificate schema.  The remaining theorem is the uniform production of budgets whose total is
bounded by `L^B`.

E73.057--E73.058 sharpen this to the candidate uniform budget:

```text
Main_3(A,L) <= C_main L^(-5),
Tail_3(A,L) <= C_tail L^(-9).
```

E73.059--E73.060 split the main estimate into:

```text
Pref_k(A,L) <= C_pref L^5,
|C_x(-gamma_k)| <= C_cauchy L^-10
```

on the three FAR-selected nodes.  The second inequality, `CMAIN-10`, is now the load-bearing
arithmetic divisibility statement for the main term.

E73.061--E73.062 rewrite `CMAIN-10` as the finite product inequality:

```text
|D_x(-gamma_k)| >= C_gap^(-1) L^10 |P_x(-gamma_k)|
```

on FAR3 nodes.  This `DEN-GAP-10` statement is the current arithmetic core.

E73.063 shows that `DEN-GAP-10` cannot come from the positive L1 ceiling
`sum |xi_n|/|t-d_n|`: the signed Cauchy value is smaller by about `1e-7` to `1e-11`.
E73.064 therefore identifies the current core as `SIGNED-CMAIN`, a cancellation theorem for the
finite CCM pole-even vector evaluated at the FAR3 nodes.

E73.065 identifies this cancellation exactly as a rowspace proximity theorem.  If

```text
E_x=H_x-mu_x I,
E_x xi_x=0,
k_t(n)=1/(t-d_n),
```

then self-adjointness and simplicity give:

```text
dist(k_t,Row(E_x))=|<xi_x,k_t>|=|C_x(t)|.
```

Thus the signed Cauchy cancellation is equivalent to saying that the dangerous Cauchy rows are
almost in the rowspace of the finite CCM operator.

E73.066 refines the target.  The previous split `PREF-5 + CMAIN-10` is sufficient but slightly
over-strong as a standalone asymptotic demand.  The sharp main theorem is the weighted rowspace
statement:

```text
ROW-MAIN-5:
sum_{gamma_k in FAR3(A,L)}
Pref_k(A,L) dist(k_{-gamma_k},Row(H_x-mu_x I))
<= C_main L^-5.
```

The current sufficient chain is therefore:

```text
ROW-MAIN-5 + Tail_3<=C_tail L^-9
=> BUD-5/9
=> FAR3-nodewise
=> FAR3
=> FAR-DNS
=> ADNS
=> DNS
=> WCS
=> PFD
=> DATA-HERM
=> CC-PROJ
=> NAT-PROJ
=> scalar WRL.
```

E73.068--E73.069 correct the numerical gauge.  The rowspace lemma and `ROW-MAIN-5` use the exact
ground eigenline of `H_x`; the earlier symmetric pole-even vector is diagnostic only.  With the exact
eigenline, the tested FAR3 weighted terms lie between `L^-6` and `L^-10`, leaving slack relative to
the `L^-5` main budget.

E73.070 connects `ROW-MAIN-5` back to the transformed eigenvector equation of E72.317--E72.319.
It proves that the packet estimate

```text
PACKET-ROW-5:
sum_{gamma_k in FAR3(A,L)}
Pref_k(A,L)Gap_x^-1
( |ZPacket_x(i gamma_k)|+|TailPacket_x(i gamma_k)| )
<= C L^-5
```

implies `ROW-MAIN-5`.  It also computes the closed Mellin formula for
`M_{B_z^infty}(w)`, reducing the zero packet to three explicit Cauchy packet sums.

E73.071 verifies that closed Mellin formula against direct quadrature with relative error below
`9e-14` in the tested cases.

E73.072 corrects the packet endpoint to the paired normalization used by E72.334--E72.340:

```text
Pair_z^M(w)=M_z^M(w)+M_z^M(-w).
```

The paired finite equation is:

```text
Lambda_L G_x(z)=sum_{w in Div(Z)/+-} Pair_z^M(w).
```

This gives the finite balanced endpoint `BALANCED-PACKET-ROW-5`.

E73.073--E73.074 show that the complete-mesh paired packet is tiny precisely when the finite Cauchy
divisor is tiny.  E73.075 proves the exact reason:

```text
Pair_z^infty(w)=A_L(z,w)H_0(w)+B_L(z,w)H_0(-w).
```

Therefore the complete-mesh packet belongs to the divisor ideal `(H_0(w),H_0(-w))`.  The current
remaining theorem is now the finite-tail version:

```text
TAIL-PAIR-DIV:
Pair_z^tail(w) is small enough, or has the same Cauchy-divisor structure, in the weighted FAR3
budget.
```

E73.076 imports E72.391--E72.392 to resolve the structure of that tail: the finite Fourier tail is an
explicit lower-order operator on the same nodal vector `G_x(w)`.  Thus the current endpoint is:

```text
EXACT-PAIR-DIV + TAIL-ABSORB + FAR3-NODAL-BUDGET
=> BALANCED-PACKET-ROW-5
=> ROW-MAIN-5
=> scalar WRL.
```

`EXACT-PAIR-DIV` is now proved.  `TAIL-ABSORB` is already proved in Phase 72 under polynomial active
cutoff.  The remaining theorem is the uniform `FAR3-NODAL-BUDGET`.

E73.077 measures the coefficient-weighted divisor terms from E73.075 and shows that the budget is
strong on critical nodes but not on arbitrary control frequencies.  E73.078 therefore rewrites the
remaining budget as the finite explicit estimate:

```text
FACTOR-MAIN-5:
sum_{gamma_k in FAR3(A,L)}
W_k(A,L)
sum_{w in Z_T/+-}
( |A_L(z_k,w)||H_0(w)| + |B_L(z_k,w)||H_0(-w)| )
<= C L^-5.
```

Together with the tail nodal estimate imported from E72.391--E72.392, this is the current sharp
finite identity target.

E73.080--E73.081 audit the coefficient denominators.  Because the evaluation line has
`Re z=sigma>0` while zero-window nodes have `Re w=0`, there is no true diagonal singularity:

```text
|w-z|>=sigma,
|w+z|>=sigma.
```

Thus `FACTOR-MAIN-5` can be attacked through the simpler shifted-strip estimate:

```text
UNIFORM-FACTOR:
sum_k W_k e^(sigma L)
sum_{w in Z_T/+-} ( |H_0(w)|+|H_0(-w)| )
<= C L^-5.
```

E73.082 shows that this blind `H_0` window sum is too crude when the critical window is enlarged:
small selected windows have cancellation around `L^-13` to `L^-17`, but larger windows can degrade to
about `L^-8`.  E73.083 therefore restores the exact coefficient weights and names the current sharp
target:

```text
WEIGHTED-HWIN-5:
sum_{gamma_k in FAR3(A,L)}
W_k(A,L)
sum_{w in Z_T/+-}
( |A_L(z_k,w)||H_0(w)| + |B_L(z_k,w)||H_0(-w)| )
<= C L^-5.
```

E73.084 shows that the weighted HWIN target must be local.  On three-node local windows,
`Pref*HWIN` is around `L^-11` to `L^-16`; on enlarged windows it can approach the `L^-5` threshold.
E73.085 therefore defines:

```text
LOCAL-HWIN-5:
sum_{gamma_k in FAR3(A,L)}
W_k(A,L) HWIN_k^loc
<= C L^-5,
```

where `Z_loc(A,L)` is the finite zero window used by the local Cauchy projection block.  Outside
nodes remain assigned to the outside-window/tail mechanisms from Phase 72.

E73.079 audits this mechanism against the earlier program.  The one-sided factor formula was already
proved in E72.320, and finite-tail nodal absorption was already proved in E72.391--E72.392.  The new
Phase 73 contribution is narrower:

```text
pairing w with -w cancels the H_0(z) obstruction and leaves exact ideal membership
Pair_z^infty(w) in (H_0(w),H_0(-w)).
```

This distinction matters because raw Mellin divisibility was already falsified in E72.36--E72.37.

E73.086 tests whether the local window in E73.084 was an optimistic selection.  It compares four
rules:

```text
prefix, tau-near, eval-near, far-set.
```

The result separates the two variables.  The good window is `tau-near`, i.e. local to the off-line
cluster height; the `eval-near` and `far-set` windows, local to the dangerous FAR3 rows, can lose the
`L^-5` margin.  Thus `Z_loc(A,L)` is not the FAR3 set.

E73.087 makes this canonical:

```text
Z_loc(A,L) = paired critical zero-node window nearest the off-line cluster height interval I_A,
             with the fixed Hermite/confluent size required by the maximal Cauchy block.
```

The active theorem is therefore a two-window estimate:

```text
LOCAL-HWIN-5 on Z_loc(A,L)
+ FAR3-WCS on D_3(A,L)
+ outside-window/tail absorption
=> scalar WRL.
```

E73.088 introduces the local root-locking mechanism.  For the finite Cauchy transform

```text
C(t)=sum_n xi_n/(t-d_n),     H_0(i gamma)=-i C(-gamma),
```

root proximity gives the exact finite estimate:

```text
|H_0(i gamma)| <= dist(-gamma,Div(C)) sup |C'|.
```

The probe shows that the root-locked nodes have huge slack, while companion nodes require their own
residual estimate.  E73.089 therefore proves the conditional local theorem:

```text
LOCK-UNIF + COMP-UNIF + FAR3 row budget
=> LOCAL-HWIN-5.
```

The remaining local analytic content is no longer an unstructured HWIN bound.  It is the pair:

```text
LOCK-UNIF: uniform proximity of local critical nodes to finite Cauchy roots, with derivative control;
COMP-UNIF: residual control for the fixed companion nodes of the local Hermite block.
```

E73.090 measures the exact sufficient `LOCK+COMP` budget from E73.089:

```text
4(1+e^(sigma L))/sigma
* (sum_{gamma_k in FAR3} W_k)
* (N_lock+N_comp).
```

Even with this crude coefficient bound, the tested budget remains below `L^-5`:

```text
worst tested sufficient exponent: L^-6.524.
```

E73.091 then rewrites the local endpoint as a finite rational certificate.  With

```text
C_x(t)=P_x(t)/D_x(t),
```

locked nodes contribute:

```text
Delta_x(gamma) M_x(gamma),
```

and companion nodes contribute the exact residual:

```text
Q_x(gamma)=|P_x(-gamma)|/|D_x(-gamma)|.
```

The new local gate is:

```text
LOCK-COMP-BUD:
4(1+e^(sigma L))/sigma * S_FAR(A,L) * N_LC(A,L)
<= C L^-5.
```

and E73.091 proves:

```text
LOCK-COMP-BUD => LOCAL-HWIN-5.
```

E73.092 assembles the current global finite gate:

```text
GATE-73(A,L):
1. LOCK-COMP-BUD(A,L);
2. TAIL-LC-BUD(A,L);
3. OUT-FAR(A,L);
4. FAR3 nodewise rational bounds for the three main WCS rows.
```

It proves:

```text
GATE-73(A,L) => scalar WRL at scale L.
```

The exact frontier is now:

```text
Uniform GATE-73 for all natural-height off-line cluster boxes.
```

The Mellin spectral divisor itself is no longer hidden:

```text
Pair_z^infty(w) in (H_0(w),H_0(-w))
```

exactly, and the finite-packet correction is the explicit tail nodal operator from E72.391--E72.392.

E73.093 checks the local tail budget:

```text
e^(sigma L)L^2/M^2 S_FAR(A,L) sum_{w in Z_loc}|w||G_x(w)|.
```

It is controlled by the same `N_LC(A,L)` because:

```text
G_x(w)=(1-e^(wL))H_0(w),        |1-e^(wL)|<=2.
```

E73.094 proves:

```text
TAIL-LC-BUD:
C_K e^(sigma L)L^2/M^2 S_FAR(A,L)Wloc(A,L)N_LC(A,L)
<= C_tail L^-5
=> local TAIL-NODAL-5.
```

Thus the complete-mesh packet and the local finite-tail packet are both controlled by the same finite
rational nodal budget `N_LC`, with the tail gaining the explicit factor `L^2/M^2`.

E73.095 measures the finite FAR3 complement:

```text
OUT-FAR_fin(A,L)
=
sum_{gamma_k in K_L \ D_3(A,L)}
W_k(A,L)|P_x(-gamma_k)|/|D_x(-gamma_k)|.
```

The worst tested exponent is:

```text
OUT-FAR_fin = L^-10.504.
```

E73.096 defines:

```text
OUT-FAR(A,L)=OUT-FAR_fin(A,L)+OUT-HIGH(A,L),
```

where `OUT-HIGH` is the natural-height high-zero tail already proved in E72.394.  Therefore the
current finite gate has only four named pieces:

```text
LOCK-COMP-BUD;
TAIL-LC-BUD;
OUT-FAR;
FAR3 main nodewise rational bounds.
```

E73.097 measures the last piece.  The three FAR3 main terms are:

```text
T_k(A,L)
=
W_k(A,L)|P_x(-gamma_k)|/|D_x(-gamma_k)|.
```

The worst tested main exponent is:

```text
FAR3 main = L^-5.930.
```

E73.098 names the final finite main certificate:

```text
FAR3-MAIN-RAT:
sum_{gamma_k in D_3(A,L)}
W_k(A,L)|P_x(-gamma_k)|/|D_x(-gamma_k)|
<= C_main L^-5.
```

E73.099 consolidates the endpoint:

```text
GATE-73(A,L)
= LOCK-COMP-BUD
+ TAIL-LC-BUD
+ OUT-FAR
+ FAR3-MAIN-RAT.
```

and proves:

```text
GATE-73(A,L) => scalar WRL at scale L.
```

The exact remaining theorem is:

```text
Uniform GATE-73 for every natural-height off-line cluster box.
```

E73.100 implements the first unified verifier for `GATE-73`.  It checks:

```text
LOCK <= L^-5,
TAIL <= L^-5,
OUT  <= L^-9,
MAIN <= L^-5.
```

The tested finite boxes all pass:

```text
worst LOCK = L^-6.524,
worst TAIL = L^-8.245,
worst OUT  = L^-10.504,
worst MAIN = L^-5.930.
```

E73.101 records the scope audit:

```text
closed: exact Mellin pair divisibility;
closed: finite tail as explicit nodal operator;
closed: high zero tail by E72.394;
finite verified: GATE-73 in the low natural-height harness;
open: Uniform GATE-73.
```

The limiting gate in the current verifier is `FAR3-MAIN-RAT`.

E73.102 decomposes the limiting main terms as:

```text
T_k = FAR_k Q_k,
FAR_k=W_k(A,L)dist(-gamma_k,Div(P_x)),
Q_k=|C_x(i gamma_k)|/dist(-gamma_k,Div(P_x)).
```

This identifies the correct analytic target:

```text
WEIGHTED-FAR-SLOPE:
sum_{gamma_k in D_3(A,L)} FAR_k Q_k <= C_main L^-5.
```

E73.104 checks and rejects the cruder proof route:

```text
sum FAR_k * max Q_k.
```

The direct weighted sum passes, but the max-slope split can fail in low windows.  Thus the next
uniform theorem must preserve the three-row weighting.

E73.105 measures the normalized weighted budgets:

```text
b_k=L^5 FAR_k Q_k,          C_main=sum_{D_3} b_k.
```

The tested range stays below:

```text
C_main < 0.18.
```

E73.106 states the interval box certificate for the remaining main theorem.  On a natural cluster
box `B`, compute interval enclosures for:

```text
W_k(B,L),       R_k=dist(-gamma_k,Div(P_x)),       Q_k=|P_x|/(|D_x|R_k).
```

Certify the FAR3 set by interval separation of FAR scores, or subdivide the box if the selected set
can change.  Then prove:

```text
sum_{k in S} L^5 W_k(B,L)|P_x(-gamma_k)|/|D_x(-gamma_k)| <= 1
```

for every possible selected set `S`.  This gives `FAR3-MAIN-RAT` on the box.

E73.107 probes this box certificate by sampling corners and center.  In the tested boxes:

```text
alpha in [0.15,0.25],
tau within +/-0.50,
```

the selected set remains:

```text
{30.4,32.9,37.6}
```

and the worst sampled budget is:

```text
CmainMax < 0.25.
```

E73.108 isolates the next rigorous technical lemma:

```text
HERM-BOX:
certified interval enclosures for G_theta,m(a,i gamma) over cluster boxes.
```

Once `HERM-BOX` is implemented, E73.106 becomes a true interval proof of `FAR3-MAIN-RAT` on each
box.

E73.109 implements a first conservative HERM-BOX probe:

```text
sup_B G <= max_grid G + 4 Lip_grid radius.
```

All tested boxes pass with:

```text
CmainUp <= 0.252,
max enclosure inflation <= 1.030.
```

E73.110 states the rigorous derivative certificate replacing the finite-difference Lipschitz
constant.  It uses only lower bounds for:

```text
|a|,     |i gamma-a|,     |1/(i gamma-a)+1/(2a)|
```

on each subbox and then applies the mean value theorem.  This makes `HERM-BOX` a finite interval
arithmetic problem.

E73.111 implements the analytic derivative enclosure from E73.110.  The tested boxes still pass:

```text
CmainUp <= 0.255.
```

One conservative wide box admits an extra possible row due to enclosure looseness, but the budget
still passes.  E73.112 therefore replaces strict FAR3 set stability by the robust possible-set
certificate:

```text
P_3(B,L)={rows that can be top-three by interval FAR scores},
sum of the three largest B_k^+ over P_3(B,L) <= 1.
```

This proves `FAR3-MAIN-RAT` on the box without needing unnecessary subdivision.

E73.113 implements this possible-set certificate.  It computes:

```text
P_3(B,L),
the three largest B_k^+ over P_3(B,L),
```

using the derivative Hermite enclosures.  All tested boxes pass:

```text
budget <= 0.255 < 1.
```

Some boxes have four possible rows:

```text
{21.0,30.4,32.9,37.6},
```

but the three-largest budget still passes, so the certificate avoids unnecessary subdivision.

## Current endpoint after E73.187

The later part of Phase 73 moved from FAR3 Cauchy budgets to the intrinsic
characteristic-node formulation of the Weyl-Feshbach scalar branch.

Closed reductions:

```text
E73.178: SDI-node is equivalent to characteristic nodal vanishing;
E73.179: the two-row Cauchy plane gives an exact finite Schur system;
E73.180: the principal cell splits exactly into model and prime parts;
E73.181: the principal residual is an explicit formula residual;
E73.182: the archimedean cell has a closed finite-frequency + WR-series form;
E73.183: the WR-series tail has a Taylor derivative certificate;
E73.184: the certificate extends to arbitrary finite Taylor order;
E73.185: grouped-frequency derivatives sharpen the WR-tail certificate;
E73.186: the principal residual is exactly a transverse Schur residual;
E73.187: the transverse vector is order one and spread, so the remaining
         smallness is model-prime matching, not projection smallness.
E73.188: the eigen-equation branch is exact but circular as a proof;
E73.189: the anti-circular packet is Cauchy-Dirichlet:
         B_perp(0)=B_perp(L)=0 and Q_w eta_w=0.
E73.190: the packet has an exact one-dimensional convolution form and
         Cauchy derivative identity A_a'=D-aA_a;
E73.191: the first endpoint derivative is a rank-one source;
E73.192: the naive ramp split is rejected because it creates a large
         artificial cancellation;
E73.193: a balanced ramp r_* with F_L[r_*]=0 removes the rank-one source
         without changing the model-prime functional.
E73.194: double-zero packets admit an exact second-Abel identity
         F_L[B]=int_0^L K_L(t)B''(t)dt.
E73.195: the same endpoint has a finite-frequency certificate using the
         closed WR series and exact prime-power samples.
E73.196: existing absolute WR tail bounds are safe but too conservative
         by 7--12 powers of L at the final residual scale;
E73.197: the signed grouped-frequency WR tail is derived and verified
         against direct summation.
```

The clean current chain is:

```text
TRANS-SCRCE-vector + CPINV
=> H0-DIV_R
=> characteristic-node vanishing / stable divisor identification
=> scalar WRL
=> Omega7.
```

The current theorem to prove is:

```text
TRANS-SCRCE-vector:
for every fixed Cauchy compact K and every R,

sup_{w in K}
||Q_w(H_model,L-Prime_L)(I-P_w)xi_L||_2 <= C_R L^(-R)

after the normalizing exponent required by CPINV.
```

Here:

```text
Q_w        = the two Cauchy rows {q_w,q_-w};
P_w        = orthogonal projection onto their row plane;
xi_L       = the exact ground eigenvector of H_L;
H_model,L  = archimedean/free model operator;
Prime_L    = H_model,L-H_L.
```

E73.187 rules out the soft projection explanation:

```text
||P_w xi_L||       ~ 0       at characteristic nodes,
||(I-P_w)xi_L||    ~ 1,
Q_w H_model xi_perp and Q_w Prime xi_perp are ordinary size,
their signed difference is tiny.
```

E73.188 shows that the exact identity

```text
Q_wH_L(I-P_w)xi_L
=(mu_L I-Q_wH_LQ_w^*(Q_wQ_w^*)^-1)Q_wxi_L
```

is only a consistency branch.  It cannot prove the theorem, because it uses
`Q_wxi_L`, the quantity the divisor theorem is meant to make small.

The anti-circular target is therefore:

```text
TRANS-CELL:
for eta_w=(I-P_w)xi_L, Q_w eta_w=0,

Q_wH_model,L eta_w
=Q_wPrime_L eta_w + O_R(L^-R).
```

Equivalently, for each row,

```text
A_L[B^perp_{j,w}]
-
sum_{p^k<=e^L}(log p)p^(-k/2)B^perp_{j,w}(klog p)
=O_R(L^-R),

B^perp_{j,w}(y)=q_jQ_L(y)eta_w,
B^perp_{j,w}(0)=B^perp_{j,w}(L)=0.
```

This avoids the old Sonin/prolate/Feshbach global wall because it is not a
global positivity, norm, or generic Dirichlet packet bound: it is a two-row
finite Cauchy-Schur model-prime matching identity tied to the characteristic
scalar node.  The Phase 72 audit matters here: E72.337 already showed how
Dirichlet-Cauchy packet calculus works, but generic packet bounds were not the
closure.  The new input is the simultaneous pair of Cauchy moment constraints
`Q_w eta_w=0`.

E73.190 rewrites this packet as

```text
B_a(y)=1/L int_0^(L-y)
 [A_a(t+y)E(-t)+A_a^#(t+y)E(t)]dt,

A_a'(r)=D(r)-aA_a(r).
```

The first endpoint derivative is not zero automatically:

```text
B_a'(0)=-(2/L)(sum_m q_a(m))(sum_n eta_n).
```

E73.192 shows that subtracting the naive ramp `y(1-y/L)` is not proof-facing:
the ramp and remainder are much larger than the final residual and cancel.
E73.193 fixes this by choosing a balanced ramp

```text
r_*(y)=r_0(y)+c_Lr_1(y),
F_L[r_*]=0,
r_*(0)=0, r_*'(0)=1, r_*(L)=0.
```

Thus the current sharp endpoint is:

```text
BAL-DOUBLE-ZERO:
For the balanced packet B_a^bal,

B_a^bal(0)=0,      (B_a^bal)'(0)=0,      B_a^bal(L)=0,

F_L[B_a^bal]
=A_L[B_a^bal]
 -sum_{p^k<=e^L}(log p)p^(-k/2)B_a^bal(klog p)
=O_R(L^-R).
```

This is equivalent to `TRANS-CELL`, but removes the rank-one endpoint source
inside the same finite functional, so no separate large ramp cancellation has
to be proved.

For double-zero packets E73.194 defines the exact signed second primitive

```text
K_L(t)=int_t^L (y-t)W_L(y)dy
 -sum_{p^k:klogp>=t}(log p)p^(-k/2)(klogp-t),
```

where

```text
W_L(y)=e^(y/2)+e^(-y/2)-e^(y/2)/(2sinh y).
```

Then

```text
F_L[B]=int_0^L K_L(t)B''(t)dt
```

provided `B(0)=B'(0)=B(L)=0`.  Polynomial double-zero tests verify this
identity to `1e-9` or better.  Direct nested quadrature on the oscillatory
balanced packets is currently conditioning-limited and should not be used as a
proof certificate at the final residual scale.

The current sharp endpoint is therefore:

```text
SECOND-ABEL:
int_0^L K_L(t)(B_a^bal)''(t)dt = O_R(L^-R).
```

This is not the old E72.49 PNT endpoint route: we are not bounding `K_L` by a
classical PNT error.  The finite signed kernel is kept exactly, and the
remaining theorem is an orthogonality between `K_L` and the very special
Cauchy-balanced transverse curvature.

Because direct nested quadrature of `int K_LB''` is ill-conditioned at the
true residual scale, E73.195 gives the certificate format to use:

```text
B_a(y)=sum_omega c_omega e^(i omega y)
      +y sum_omega l_omega e^(i omega y),

F_L[B_a^bal]=F_L[B_a]
=A_L^closed[{c_omega,l_omega}]
 -sum_{p^k<=e^L}(log p)p^(-k/2)B_a(klogp).
```

This finite-frequency evaluation reaches the correct residual scale in the
tested windows once the WR series is taken deep enough.  The remaining proof
implementation should replace floating truncation by the rigorous WR tail
bounds of E73.183--E73.185 and interval arithmetic for the finite frequency
coefficients.

E73.196 shows that the coefficient-absolute WR tail bounds from E73.184--185
are not sharp enough by themselves for the final certificate.  The correct
tail is signed.  For each frequency,

```text
T_R(B)
=sum_omega c_omega [S_1(R,omega)-S_0(R)]
 +sum_omega l_omega S_2(R,omega),
```

where

```text
S_1(R,omega)=sum_{r>=R}(1-e^{-(2r+1/2-iomega)L})/(2r+1/2-iomega),
S_2(R,omega)=sum_{r>=R}
 (1-e^{-a_rL}(1+a_rL))/a_r^2,
a_r=2r+1/2-iomega.
```

E73.197 verifies this signed grouped form against direct WR-tail summation to
about `L^-20--L^-22`.  The next certificate step is to evaluate `S_1-S_0` and
`S_2` by complex interval special functions, instead of taking absolute values
termwise.

E73.198 gives that special-function evaluation.  With

```text
a_r(omega)=2r+1/2-iomega,
b_r=2r+1,
```

the paired algebraic tails are

```text
D_1(R,omega)=sum_{r>=R}[1/a_r(omega)-1/b_r]
            =1/2[psi(R+1/2)-psi(R+1/4-iomega/2)],

D_2(R,omega)=sum_{r>=R}1/a_r(omega)^2
            =1/4 psi_1(R+1/4-iomega/2).
```

The omitted endpoint exponentials have elementary geometric bounds.  Therefore
the proof-facing tail is no longer a long numerical summation:

```text
T_R(B)
=sum_omega c_omega D_1(R,omega)
 +sum_omega l_omega D_2(R,omega)
 + exponentially small correction.
```

E73.199 packages this into the finite-frequency certificate

```text
F_L[B_a^bal]=F_L[B_a]=A_L^digamma[B_a]-P_L[B_a],
```

where `P_L` is the exact finite prime-power sum.  The remaining implementation
target is `INTERVAL-FF-CERT`: enclose the finite coefficients and the complex
digamma values by intervals with total width below the transverse budget.

E73.200 splits this certificate before the final cancellation.  It shows that
`A_L[B_a]` and `P_L[B_a]` are typically of size `L^-1--L^-4`, while the final
residual is `L^-18--L^-22`.  Thus the large relative errors in E73.199 are not
a tail-formula failure; they are the expected result of assembling a 17--20
power cancellation in floating arithmetic.

E73.201 repeats the finite-frequency assembly with 100-digit arithmetic.  The
certificate changes at the same scale as the E73.199 residual in several rows,
confirming that the next proof-facing object must intervalize the whole finite
certificate, not just the digamma tail.

E73.202 states the resulting full interval theorem.  The certificate must
enclose:

```text
1. the exact finite matrix entries;
2. the ground eigenline xi via residual + spectral gap;
3. the Cauchy projection eta_w;
4. the packet coefficients c_omega,l_omega;
5. the complete scalar A_L^digamma-P_L.
```

If the final interval for every admissible row lies in `|z|<=M L^-R`, then the
finite `TRANS-CELL` budget follows directly from the E73.199 identity.

E73.203 tests the first naive way to fill this certificate: use the existing
double eigensolver and certify the ground line by Davis-Kahan.  This fails for
the expected reason.  The ground gap is about `L^-20--L^-22`, comparable with
the floating eigen residual, so the transported eigenline radius is enormous.
This is a certification failure, not a mathematical failure of `TRANS-CELL`.

E73.204 therefore replaces the eigenline source by a bordered Krawczyk
certificate for the nonlinear system

```text
(H-mu I)xi=0,        ell^*xi=1.
```

The corrected full interval route is now:

```text
closed-form interval matrix entries
=> bordered eigenline interval [xi]
=> Cauchy projection interval [eta_w]
=> packet coefficient intervals
=> interval for A_L^digamma-P_L
=> TRANS-CELL.
```

E73.205 audits the bordered system with the legacy double matrix.  As expected,
the bordered condition number is about `L^20`, so the double residual is far too
large and the correction step is useless.  This gives a precise demand: the
matrix/eigenpair residual must be computed at least about 20 powers of `L`
below the desired eigenline radius.

E73.206 builds the finite matrix entries directly from the closed
finite-frequency/digamma formula:

```text
H_mn=A_L^digamma[Q_mn]-P_L[Q_mn].
```

On small windows this high-precision entry engine agrees with the legacy
quadrature matrix at the expected double floor, validating the entry-mode
normalization.

E73.207 then uses these closed high-precision entries with `mp.eigsy`.  The
bordered residual drops more than 100 powers of `L` below the gap.  Thus the
E73.203 obstruction was purely a double-precision certification obstruction:
the bordered eigenline certificate is viable once the closed entries are
outward-rounded.

E73.208 turns this into a Krawczyk budget.  With `Y=J_0^(-1)` it uses the
sufficient inequality

```text
step + ||Y|| epsH + ||Y||(epsH+2rho)rho < rho.
```

In the tested windows, `epsH` around `L^-47--L^-54` is admissible, leaving
ample room relative to the 100-digit centers.

E73.209 converts this operator budget into a per-entry target:

```text
r_entry <= epsH/dim.
```

For the tested windows this is roughly `L^-49--L^-56`.  The next proof-facing
implementation is therefore an outward-rounded closed-entry enclosure below
that per-entry radius.

E73.210 handles the only non-elementary part of that entry enclosure.  The
digamma tail is enclosed by the Bernoulli asymptotic expansions for `psi` and
`psi_1` at

```text
z=R+1/4-iomega/2,     R=80.
```

With `K=12` Bernoulli terms, the resulting `D_1/D_2` radius is already about
`10^7` times smaller than the per-entry target in the tested windows.  E73.216
shows that `K=16` tolerates sector constants of size about `10^17`, so `K=16`
is the preferred proof-facing setting.

E73.211 audits the finite elementary pieces.  Even with a crude 80-decimal
rounding model, the finite elementary sums have about `10^39--10^40` slack
relative to the per-entry targets.  Therefore neither the special-function tail
nor finite elementary rounding appears to be the limiting obstruction.

E73.212 packages the current finite-entry result:

```text
BALL-ENTRY-CERT
=> per-entry radius target
=> Krawczyk matrix budget
=> bordered eigenline interval.
```

The package is implementation-conditional: it requires replacing the rounding
audit by real outward-rounded complex ball arithmetic.

E73.213 implements `BALL-ENTRY-CERT v0` as a component-radius certificate.  It
checks every entry against the E73.209 per-entry target using:

```text
R_entry=R_digamma+R_round+R_exp_tail.
```

The certificate passes in the tested windows with slack about `10^7`, dominated
by the analytic Bernoulli `psi/psi_1` tail.  Extra stress at larger windows
keeps the same pattern: the worst entry is `(0,0)` and finite rounding remains
far below the special-function radius.

E73.215 replaces the heuristic finite-rounding audit by native complex-ball
propagation for the elementary pieces (`exp_int`, `y_exp_int`, finite WR head,
and prime samples).  The elementary ball radii are about `L^-138--L^-156`,
again far below the target.  Therefore `BALL-ENTRY-CERT` is now reduced to the
formal Bernoulli remainder lemma for `psi/psi_1`.

E73.216 quantifies the remaining Bernoulli sector constant.  The certificate
survives `C_sec~10^17` at `K=16`, so the exact normalization/citation of the
sectorial remainder can be handled with enormous margin.

E73.217 feeds the actual `BALL-ENTRY-CERT` matrix radius into the bordered
Krawczyk inequality.  The inclusion closes in the tested windows.  With
`C_sec=1`, the certified eigenpair radius is about `L^-50--L^-56`; even after
inflating the Bernoulli sector constant to `C_sec=10^6`, it remains about
`L^-41--L^-46`.

The local chain now reaches:

```text
BALL-ENTRY-CERT
=> bordered Krawczyk eigenline [xi,mu]
=> Cauchy projection [eta_w]
=> next: final scalar TRANS-CELL interval.
```

E73.218 propagates the certified eigenline ball through the Cauchy projection
`eta_w=(I-P_w)xi`.  Since `P_w` is the explicit orthogonal projection onto the
two Cauchy rows, `||I-P_w||=1`; the numerical audit confirms no logarithmic
loss in the tested windows.  Thus the radius carried into the final scalar
functional is the same radius certified by the bordered Krawczyk step.

E73.219 propagates this radius through the scalar functional
`C_a(eta)=q_aHeta`, using

```text
rad(C_a)
<= ||q_aH_0||rho_eta
 + ||q_a||epsH||eta_0||
 + ||q_a||epsHrho_eta.
```

The tested windows show no scalar radius blow-up.  Even with the inflated
Bernoulli-sector budget `C_sec=10^6`, the total scalar radius is at least about
15 decimal orders smaller than the displayed scalar center.  Thus the local
finite chain has reached:

```text
BALL-ENTRY-CERT
=> bordered Krawczyk eigenline [xi,mu]
=> Cauchy projection [eta_w]
=> scalar TRANS-CELL radius budget.
```

The remaining finite certification step is now sharper: evaluate the scalar
center itself by outward-rounded closed finite-frequency arithmetic, rather
than by the legacy matrix center used in the E73.219 diagnostic.

E73.220 performs the corresponding closed-center check.  It evaluates
`A_L^digamma-P_L` directly and compares it to `q_aHeta`.  The exponents match,
but the relative discrepancy reaches `2.4e-2` in the most delicate row.  This
confirms that the proof-facing center must be the closed finite-frequency
center itself, with its own outward arithmetic radius, not the legacy matrix
center.

E73.221 audits the numerical stability of that closed center by comparing
`dps=80,100,140`.  The `dps=80` displacement is already only about
`L^-116--L^-132`, and the `dps=100` displacement is about `L^-145--L^-164`.
This is far below the E73.219 scalar radii.  Therefore the final center task is
not more precision; it is wrapping the existing closed finite-frequency
operations in formal outward complex-ball arithmetic.

E73.222 rewrites the proof-facing center as a finite linear functional:

```text
C_a = sum_omega c_omega W_omega
    + sum_omega l_omega V_omega
    + E_exp.
```

This turns the outward-center problem into two explicit finite audits:
coefficient balls for `c_omega,l_omega` and weight balls for
`W_omega,V_omega`.  It is the center-side analogue of the scalar radius
formula in E73.219.

E73.223 closes the coefficient side.  For each frequency,

```text
c_omega=u_omega eta,       l_omega=v_omega eta,
rad(c_omega)<=||u_omega||rho_eta,
rad(l_omega)<=||v_omega||rho_eta.
```

The tested coefficient radii are negligible: even with `C_sec=10^6`, the worst
relative coefficient radius is about `7.6e-26`.  The remaining center-side
piece is therefore the weight-ball audit for `W_omega,V_omega`.

E73.224 checks the amplification of those coefficient balls by the exact
closed-center weights.  It computes

```text
W_omega=(A_L^digamma-P_L)[e^(iomega y)],
V_omega=(A_L^digamma-P_L)[y e^(iomega y)]
```

by definition and measures

```text
sum |W_omega|rad(c_omega)+sum |V_omega|rad(l_omega).
```

Even with `C_sec=10^6`, the worst tested ratio to the scalar center is about
`1.6e-14`.  Thus the center interval now has one remaining finite audit:
formal radii for `W_omega,V_omega` themselves.

E73.225 audits those weight radii.  For the unit modes
`e^(iomega y)` and `y e^(iomega y)`, the radius is split into finite rounding,
Bernoulli `psi/psi_1` remainder, and exponentially small endpoint tail.  Even
with `C_sec=10^6`, the resulting weighted contribution is only about
`L^-67--L^-77`, with ratio about `4.5e-47` to the conservative coefficient
l1 scale.  Thus the weight-radius side is not the bottleneck; the dominant
finite uncertainty remains the E73.219 eigenline/projection scalar radius.

E73.227 replaces the E73.225 finite-rounding audit for `W_omega,V_omega` by
native complex-ball propagation.  The finite elementary/prime radius is only
`L^-138--L^-156`, far below the Bernoulli `psi/psi_1` remainder.  Thus the
weight-radius side is formally reduced to the same special-function sector
lemma already isolated for BALL-ENTRY-CERT.

E73.229 proves the finite-window Bernoulli sector lemma.  Euler-Maclaurin gives
the `psi/psi_1` remainders in the E73.210 normalization, and the only sector
loss is

```text
C_sec >= max_z (|z|/Re z)^(2K+1).
```

For the tested windows at `K=16`, this constant is about `1.11`, while the
audits already survive `C_sec=10^6`.

E73.228 assembles the complete finite scalar ledger:

```text
R_total=R_etaH+R_coeff+R_weight.
```

The full row-by-row audit corrects the preliminary dominant-term reading:
`R_coeff` dominates the total, followed by `R_etaH`, while `R_weight` is far
smaller.  The worst inflated-sector ratio remains tiny:

```text
R_total/|C_a| = 1.7e-14.
```

So the finite local scalar interval is executable and stable in the tested
windows.  E73.230 below removes the remaining closed-route bookkeeping issue;
the remaining gap is the uniform theorem, not a hidden finite-radius blow-up.

E73.230 separates the proof-facing closed route from the matrix-route
cross-check.  In the closed coefficient/weight representation, one should use

```text
R_closed=R_coeff+R_weight+R_product,
```

not `R_etaH+R_coeff+R_weight`, since `R_etaH` and `R_coeff` both transport the
same `eta` uncertainty through different coordinate systems.  The authoritative
closed scalar wrapper has worst inflated-sector ratio

```text
R_closed/|C_a| = 1.6e-14.
```

Thus the finite-window scalar interval wrapper is closed; the remaining open
problem is the uniform production of these certificates in `L` and admissible
windows.

E73.231 stress-tests the closed wrapper beyond the certified windows using an
explicitly extrapolated `rho_eta`.  It is not a proof, but it shows no visible
coefficient/weight blow-up up to `lambda=18`; the visible bottleneck remains
uniform production of the certified eigenline radius and the arithmetic center
cancellation.

E73.232 states the resulting uniform theorem target:

```text
UCT-FF:
|C_a^0(L,N,w)|+R_closed(L,N,w) <= A L^(-M)
```

for all admissible rows/windows after choosing the finite parameters.  The
factorized sufficient conditions are:

```text
U1 uniform eigenline/coefficient radius;
U2 polynomial coefficient-map/weight growth;
U3 uniform weight-radius bound;
U4 uniform center cancellation.
```

The finite interval machinery makes U2--U3 technical.  The load-bearing open
math is U1 and especially U4, the finite critical source divisibility theorem
already identified by E73.161.

E73.233 derives a canonical identity for U4:

```text
qH(I-P)xi=<[I-P,H]q*+mu(I-P)q*,xi>.
```

The numerical audit certifies the identity and shows that the defect vector is
not norm-small: `||D_q||` is around `L^-1.47--L^-4.54`, while the scalar center
is around `L^-14.98--L^-21.68`.  So the easy commutator-norm route is dead.
The correct remaining theorem is a paired commutator cancellation against the
CCM ground vector, not an operator-norm estimate and not a pseudoinverse
rowspace statement.

E73.234 expands that identity and removes a possible ambiguity.  Since each
`q_a^*` already lies in the Cauchy row plane, `(I-P)q_a^*=0`, hence

```text
[I-P,H]q_a^*+mu(I-P)q_a^*=(I-P)Hq_a^*.
```

This is exactly the adjoint of the E73.180 principal residual
`rho_a=q_aH(I-P)`.  Therefore the paired commutator route and the
SCRCE-principal route are the same theorem, not two independent closures.  The
remaining U4 statement is the explicit finite residual estimate `APR-U4`:

```text
|A_L[B_{a,w}]-P_L[B_{a,w}]
 - sum_k A_ak(w) q_k xi_L| <= A_M L^(-M).
```

E73.235 shows that this `APR-U4` residual is exactly the closed eta-packet
center already used by E73.222--E73.230:

```text
q_aHxi - (A(w)Qxi)_a = q_aH(I-P)xi
```

and therefore

```text
APR-U4
<=> ETA-DIV:
sum c_omega(eta)W_omega + sum l_omega(eta)V_omega = O_M(L^-M),
Q_w eta=0.
```

The numerical check compares the principal residual, the eta-matrix residual,
and the coefficient/weight center; all agree within the already measured
finite assembly error.  This leaves a single finite divisibility target in
coefficient/weight coordinates.

E73.236 extracts the first exact coefficient divisibility from the endpoint
zeros of the eta-packet.  Since every frequency is `2*pi*n/L`,

```text
B(0)=0, B(L)=0
=> sum c_omega=0, sum l_omega=0.
```

Therefore the center is invariant under constant gauges:

```text
W_omega -> W_omega-alpha,
V_omega -> V_omega-beta.
```

The probe verifies these moment identities and gauge invariance.  This is only
the first quotient layer, but it is a genuine finite divisibility relation
inside ETA-DIV.

E73.237 connects ETA-DIV to the balanced second-Abel endpoint in coefficient
language.  The derivative moment is

```text
B'(0)=sum iomega c_omega+sum l_omega
     =-(2/L)(sum q_a)(sum eta).
```

Subtracting `B'(0)r_*`, where `F_L[r_*]=0`, preserves the center and gives a
balanced packet with

```text
B^bal(0)=0, (B^bal)'(0)=0, B^bal(L)=0.
```

Thus the current finite endpoint is

```text
BSA-DIV:
int_0^L K_L(t)(B^bal)''(t)dt = O_M(L^-M),
```

with `(B^bal)''` written explicitly in terms of `c_omega,l_omega` and the
balanced-ramp curvature.  This is now the non-matrix finite identity to attack.

E73.238 rewrites BSA-DIV as a finite curvature weight quotient:

```text
sum c_omega U^bal_omega + sum l_omega Z^bal_omega = O_M(L^-M),
```

where

```text
U^bal_omega=U_omega-iomega R_*,
Z^bal_omega=Z_omega-R_*,
R_*=int K_L r_*'' = F_L[r_*]=0.
```

The probe confirms that this quotient pairing equals the original center at
arithmetic floor.  This does not prove decay; it fixes the exact finite object
for the next proof attempt: signed orthogonality between the Cauchy-balanced
coefficient vector and the curvature quotient weights.

E73.239 audits whether the endpoint moment rows already explain that
orthogonality.  They do not.  After projecting the weights away from

```text
sum c_omega, sum l_omega,
```

the residual pairing is still essentially the full center.  Adding the
derivative row as if it were an annihilating constraint creates a large
artificial term because `B'(0)` is not zero before the balanced ramp.  Therefore
the next genuine target is not more endpoint bookkeeping but an
eigen-equation-induced coefficient relation:

```text
EIG-COEFF:
finite relations satisfied by eta_w=(I-P_w)xi_L whose annihilator contains
the curvature quotient weights up to O_M(L^-M).
```

E73.240 audits the first apparent eigen-coefficient relation:

```text
QH(I-P)xi=(mu I-A)Qxi.
```

This identity is exact, but it is the circular branch from E73.188: the right
side uses `h=Qxi`, whose smallness is the divisor statement the route is trying
to prove.  Therefore the acceptable target is sharpened to `CURV-COB`: the
curvature quotient source must be represented as a structured coefficient
coborder modulo fixed endpoint residual slots, without using `h` small,
pseudoinverses, or rowspace projection.

E73.241 identifies the curvature source row.  The coefficient/weight source
is `q_aH_L` modulo finite assembly, and on the transverse vector
`eta=(I-P_w)xi_L` it is exactly the residual row:

```text
Src_{a,w}eta = q_aH_L(I-P_w)xi_L = rho_a xi_L.
```

The tempting primitive `q_a^*` only gives `q_aH_L eta=q_aE eta`, putting `E`
on `eta` rather than on `xi`; this is the circular transverse branch again.
Thus `CURV-COB` must be a structured left-coborder for `rho_a`, not a trivial
coborder for `q_aH_L`.

E73.242 tests the first fixed primitive module for that coborder:

```text
P_deg=span{D^k q_j^*: j=1,2, 0<=k<=deg}.
```

This polynomial Cauchy module improves row norm as degree increases but leaves
the scalar residual pairing at the same scale as the original center.  The
full ambient rowspace baseline is also shown to be tautological.  Therefore
`CURV-COB` needs a richer fixed module containing rational
Loewner/divided-difference denominators, not just polynomial multiples of the
Cauchy rows.

E73.243 tests that richer idea with fixed geometric rational denominators:

```text
D^k q_j^*/(D^2+beta^2)^m,
beta in {|w|, 2pi/L, 1}.
```

This improves row-norm residuals but does not reduce the scalar pairing; in
some rows it worsens it.  Therefore natural geometric denominators are not the
missing coborder.  The primitive module must be derived from the symbolic
partial-fraction structure of the actual CCM/Loewner cell, not selected by
scale heuristics.

E73.244 tests the first module actually inherited from the local
divided-difference ideal:

```text
DD_L(±gamma,d), DD_L(±gamma,d)/(d^2-gamma^2)^m,
d^2DD_L(±gamma,d), d^4DD_L(±gamma,d).
```

It improves row-norm residuals but still leaves the scalar pairing at the
center scale.  Thus direct module enlargement is not closing `CURV-COB`.  The
next object must be the canonical quotient defect of `rho_a` modulo the
generated DD-local image, paralleling E73.163--E73.167.

E73.245 constructs that quotient:

```text
M_DD={Y^*E : Y in P_DD},
delta_a=rho_a-Proj_{M_DD}rho_a.
```

In trusted small windows the rank of `M_DD` is stable (`rank=5`), and the
quotient defect carries essentially the whole scalar pairing:

```text
delta_a xi_L ~= rho_a xi_L.
```

Thus the current sharp endpoint is `CURV-QUOT-DIV`: prove the quotient pairing
is rapidly small.  The next work is symbolic rank/coordinate certification for
this finite quotient, not further ad hoc module enlargement.

E73.246 performs that first coordinate audit.  For two critical nodes and two
Cauchy rows, the quotient defect packet has stable rank `4` in the trusted
windows after the DD-local generated image is removed.  Therefore

```text
delta_a xi_L = theta_a · z_Q
```

is the current finite endpoint.  The sharpened theorem is:

```text
QUOT-COORD-DIV:
theta_a(L,w) · z_Q(L,w) = O_M(L^-M).
```

The proof must now derive symbolic quotient coordinates and their
super-polynomial orthogonality.  It must not use full rowspace projection,
the transverse eigen-branch `h=Q_w xi_L`, or further ad hoc module enlargement.

E73.247 replaces the SVD quotient chart by physical pivot coordinates.  If
`D_Q` is the quotient defect packet and `J` is a four-column pivot set, then

```text
D_Q xi_L = D_Q[:,J] z_J,
z_J = xi_J + D_Q[:,J]^{-1}D_Q[:,R]xi_R.
```

Thus `QUOT-COORD-DIV` is sharpened to:

```text
PIV-QUOT-DIV:
z_J(L,w)=O_M(L^-M).
```

The audit shows moderate pivot condition exponents and rapidly small `z_J` in
the trusted windows.  This does not prove the theorem, because the pivot rule is
still numerical, but it gives an algebraizable finite identity: prove the
physical coordinate cancellation `xi_J + T_J xi_R`.

E73.248 audits possible symbolic pivot rules.  The simple physical rules
`NORM4`, `SYMPAIR`, and `EDGECORE` are not uniformly reliable; they can choose
ill-conditioned coordinates in the first trusted window.  The stable rule is
the maximal quotient minor:

```text
J_*(L,w) in argmax_{|J|=4} |det D_Q[:,J]|.
```

This gives the current finite endpoint:

```text
MAXMIN-NONDEG:
|det D_Q[:,J_*]| >= L^{-B},

MAXMIN-PIV-DIV:
xi_{J_*}+D_Q[:,J_*]^{-1}D_Q[:,R_*]xi_{R_*}=O_M(L^-M).
```

This is a minor statement inside the DD-local quotient, not the old Phase 72
rowspace-minor route.

E73.249 applies Cauchy-Binet to the quotient packet:

```text
Vol_Q^2 = det(D_QD_Q^*) = sum_{|J|=4}|det D_Q[:,J]|^2.
```

Therefore

```text
max_J |det D_Q[:,J]| >= Vol_Q / sqrt(binomial(n,4)).
```

So `MAXMIN-NONDEG` follows from the Gram-volume lower bound

```text
GRAM-NONDEG:
Vol_Q >= L^{-B}.
```

The remaining endpoint is now split cleanly:

```text
1. quotient-volume nondegeneracy: GRAM-NONDEG;
2. spectral Mellin divisibility: MAXMIN-PIV-DIV, i.e. z_{J_*}=O_M(L^-M).
```

E73.250 factors `GRAM-NONDEG` into Gram-Schmidt increments.  For quotient rows
`d_1,...,d_4`,

```text
Vol_Q = prod_j dist(d_j, span(d_1,...,d_{j-1})).
```

The audit shows polynomial-scale row norms and angle sines.  Thus
`GRAM-NONDEG` is now reduced to the finite row-independence theorem:

```text
QROW-INDEP:
dist(d_j, span(d_1,...,d_{j-1})) >= L^{-B}
```

for a suitable ordering of the four DD-local quotient rows.

E73.251 opens the remaining coordinate cancellation.  For the maximal-minor
pivot set `J_*`,

```text
M_J = D_Q[:,J_*]^{-1}D_Q,
z_{J_*}=M_J xi_L.
```

The coordinate rows `m_j` show large cancellation against the absolute ceiling,
and low endpoint moments do not explain the effect.  The sharpened target is:

```text
COORD-ROW-DIV:
m_j = Y_j^*E + O_M(L^-M)
```

for structured `Y_j` derived from the DD-local quotient construction.  This is
equivalent to `MAXMIN-PIV-DIV`, but it must be proved structurally, not by full
rowspace projection or adjugate fitting.

E73.252 audits the first possible structured proof: project the coordinate rows
`m_j` against the combined DD-local generated image from the two critical nodes.
This does not reduce the scalar pairing:

```text
resPairMaxB ~= zMaxB.
```

Thus the original DD-local module has already done all it can do.  The missing
identity must be a second-layer quotient-coordinate coborder:

```text
COORD-COB2:
m_j = Y_j^*E + O_M(L^-M),
```

where `Y_j` is built from the quotient denominator `D_J^{-1}` and the finite
projection data, not from the first DD-local primitive module alone.

E73.253 replaces the search for the second-layer coborder by an exact Cramer
numerator identity.  With

```text
D_J = D_Q[:,J_*],
b=D_Qxi_L,
```

define `N_j` by replacing the `j`-th column of `D_J` by `b`.  Then

```text
z_j = N_j / det(D_J).
```

Thus the hard divisibility is now the explicit determinant statement:

```text
CRAMER-NUM-DIV:
N_j = O_M(L^-M) det(D_J).
```

With `MAXMIN-NONDEG`, this is equivalent to `MAXMIN-PIV-DIV`.  The current
finite endpoint is therefore a quotient bordered-minor numerator identity.

E73.254 expands each Cramer numerator by Laplace:

```text
N_j = sum_a (D_Qxi_L)_a Cof_{a,j}(D_J).
```

The audit shows no large four-term alternating cancellation: `altGainB` is
small in the tested windows.  Thus the numerator smallness must enter primarily
through the bordered vector

```text
b=D_Qxi_L,
```

with cofactor/denominator sizes controlled by the nondegeneracy side.  This
rejects an `ALT-CRAMER` mechanism analogous to the older Phase 72 alternating
rank certificate.

E73.255 tests the first possible structural simplification for that bordered
vector: parity inside each two-row Cauchy packet.  For each gamma pair it forms

```text
b_sym=(b_0+b_1)/sqrt(2),        b_anti=(b_0-b_1)/sqrt(2),
```

and also the four gamma-parity by row-parity coordinates `ss,sa,as,aa`.
The dominant mode is not stable: examples switch from `ss` to `sa` to `as`
and `aa` across the tested `(L,rat_power)` cases.  Therefore the smallness of

```text
b = D_Q xi_L
```

is not produced by a fixed symmetric or antisymmetric row cancellation.  This
separates the current quotient problem from the already-used parity mechanisms
in E72.390 and E73.072--E73.075.

The current endpoint is now:

```text
QROW-INDEP
=> GRAM-NONDEG
=> MAXMIN-NONDEG,

BORDER-ROW-DIV:
for each quotient defect row delta_{gamma,r},
delta_{gamma,r} xi_L = O_M(L^-M),

MAXMIN-NONDEG + BORDER-ROW-DIV
=> CRAMER-NUM-DIV
=> MAXMIN-PIV-DIV
=> CURV-QUOT-DIV
=> scalar WRL.
```

Rejected:

```text
PAIR-PARITY-B.
```

Kept:

```text
BORDER-ROW-DIV.
```

E73.256 corrects the scalar role of the DD-local quotient.  Since

```text
M_DD={Y^*E},        E=H_L-mu_L I,        E xi_L=0,
```

every exact row in `M_DD` pairs to zero with `xi_L`.  Hence

```text
delta_a xi_L
=(rho_a-Proj_{M_DD}rho_a)xi_L
=rho_a xi_L.
```

The quotient projection can change row geometry, coordinate rank, and maximal
minor selection, but it cannot be an independent scalar cancellation mechanism.
The scalar side of the proof is therefore exactly the E73.180--E73.181
principal residual, equivalently E73.234 `APR-U4`:

```text
rho_a xi_L
= A_L[B_{a,w}] - P_L[B_{a,w}]
  - sum_k (A^model_{ak}(w)-A^prime_{ak}(w))H_k(w).
```

The revised endpoint is:

```text
Nondegeneracy:
QROW-INDEP => GRAM-NONDEG => MAXMIN-NONDEG.

Scalar annihilation:
APR-U4 / principal residual:
rho_a xi_L = O_M(L^-M).

Combined:
MAXMIN-NONDEG + APR-U4
=> CRAMER-NUM-DIV
=> MAXMIN-PIV-DIV
=> CURV-QUOT-DIV
=> scalar WRL.
```

The numerical variations of `delta_a xi_L` under high `rat_power` are now
classified as conditioning artifacts: the SVD basis for `M_DD` amplifies the
floating residual `E xi_L`.  They are not exact quotient structure.

E73.257 rejects the next possible over-strong shortcut.  The condition

```text
Q_w eta=0
```

does imply the endpoint/Dirichlet structure already used in E73.189--E73.193,
but it does not force the scalar residual.  On the whole Cauchy kernel,

```text
||q_aH_L|_{ker Q_w}||
```

is larger than the actual value `|q_aH_L(I-P_w)xi_L|` by factors around
`L^11` to `L^19` in the tested windows.  Thus the scalar theorem cannot be a
generic estimate for all packets with `B(0)=B(L)=0`.

Rejected:

```text
KER-Q-DIV:
Q_weta=0 alone implies q_aH_Leta=O_M(L^-M).
```

The current scalar target is:

```text
EIGEN-KER-DIV:
H_Lxi_L=mu_Lxi_L,
eta_w=(I-P_w)xi_L,
Q_weta_w=0
  =>
q_aH_Leta_w=O_M(L^-M).
```

In coefficient language this is still the E73.235 finite divisibility:

```text
q_aH_Leta_w
= sum_omega c_omega(eta_w)W_omega
 +sum_omega l_omega(eta_w)V_omega
 +E_exp,
```

but the cancellation must use the eigenvector origin of `eta_w`, not merely
the two Cauchy constraints.

E73.258 audits whether the eigenvector origin gives an autonomous transverse
eigen-residual theorem.  With

```text
E=H_L-mu_L I,        P=P_w,        R=I-P,
eta_w=Rxi_L,
```

the exact projected identity is

```text
R E eta_w = - R E P_wxi_L.
```

Thus transverse residual smallness is forced by the Cauchy-plane component
`P_wxi_L`, equivalently by `h=Q_wxi_L`.  Using that as the proof source would
repeat the E73.188 circular branch.  Numerically, the stable rows show
`transResB ~= forceB`; at larger sizes the equality is obscured by the floating
eigen-residual floor.

Rejected:

```text
TRANS-EIG-AUTO:
eta_w is autonomously small-residual in ker Q_w, independently of h=Q_wxi_L.
```

The scalar target remains the explicit finite coefficient identity:

```text
ETA-DIV:
sum_omega c_omega(eta_w)W_omega
+sum_omega l_omega(eta_w)V_omega
+E_exp
=O_M(L^-M),
```

proved from the explicit Gamma-prime construction of `H_L`, not from abstract
projection algebra alone.

E73.259 records the exact finite adjugate/determinant detector for the same
scalar theorem.  For

```text
E_L=H_L-mu_LI,        E_Lxi_L=0,        dim ker E_L=1,
```

the reduced adjugate satisfies

```text
Adj_red(E_L)=scale * xi_Lxi_L^*.
```

Therefore, for the transverse residual row

```text
rho_{a,w}=q_aH_L(I-P_w),
```

one has

```text
rho_{a,w}Adj_red(E_L)
=scale*(rho_{a,w}xi_L)xi_L^*.
```

Thus `ETA-DIV` is equivalent to the normalized finite adjugate identity:

```text
ETA-ADJ:
rho_{a,w}Adj_red(H_L-mu_LI)
=O_M(L^-M)||Adj_red(H_L-mu_LI)||.
```

Equivalently, all row-replacement determinant defects for replacing a row of
`E_L` by `rho_{a,w}` must be `O_M(L^-M)` relative to the reduced cofactor
scale.  This is a detector, not a forcer: Phase 72 already showed that
adjugate/cofactor constructions become tautological if the adjugate is built
from the unknown null vector.  Its value here is to give a zero-free finite
identity exactly equivalent to the coefficient form:

```text
ETA-DIV <=> ETA-ADJ.
```

E73.260 expands `ETA-ADJ` into row-replacement determinants.  For every row
index `i`,

```text
det ReplaceRow(E_L;i,rho_{a,w})
= (rho_{a,w}Adj_red(E_L))_i
= scale*(rho_{a,w}xi_L)*conjugate(xi_{L,i}).
```

Consequently,

```text
||det ReplaceRow(E_L;*,rho_{a,w})||_2 / |scale|
= |rho_{a,w}xi_L|.
```

This is the determinant-only certificate equivalent to `ETA-DIV`.  The direct
double `slogdet` audit matches stable rows, but becomes ill-conditioned by
`lambda=16`, where the cofactor scale and singular gap exceed naive double
precision.  Thus a proof-facing verifier must use either:

```text
1. interval row-replacement determinants; or
2. the bordered-Krawczyk certified eigenline plus the reduced-adjugate formula.
```

E73.261 executes the second route as a finite certified budget.  Since the
normalized reduced-adjugate defect satisfies

```text
||rho Adj_red(E_L)|| / ||Adj_red(E_L)|| = |rho xi_L|,
```

the `ETA-ADJ` radius is exactly the scalar radius already propagated in
E73.219 from:

```text
BALL-ENTRY-CERT
=> bordered Krawczyk [xi_L]
=> Cauchy projection [eta_w]
=> q_aH_Leta_w.
```

The tested finite windows have very large radius slack.  Even with
`Csec=1e6`, the normalized `ETA-ADJ` radius is around `L^-42` to `L^-48`,
while the centers are around `L^-15` to `L^-21`.

Thus the finite certification pipeline is no longer the bottleneck.  The
remaining mathematical theorem is the uniform center decay:

```text
UNIF-ETA:
|q_aH_L(I-P_w)xi_L| <= A_M L^-M
```

equivalently `ETA-DIV`, `ETA-ADJ`, or `ETA-DET`, proved from the explicit
Gamma-prime construction.

E73.262 freezes this frontier and audits it against the earlier program.  The
only non-rejected proof target left is the eigenline-induced curvature
orthogonality in the balanced second-Abel form:

```text
int_0^L K_L(t)((B_{a,w,L}^{eta})^bal)''(t)dt = O_M(L^-M).
```

Endpoint moments, rowspace/cofactor tests, parity modes, quotient projections,
and generic `ker Q_w` constraints have all been audited as normal forms or
detectors, not forcing mechanisms.  The missing input must come from the actual
finite eigen-equation `(H_L-mu_LI)xi_L=0`, formulated as `EIG-COEFF`.

E73.263 rewrites the same target as a fixed Cauchy-Schur commutator residual:

```text
q_aH_L(I-P_w)xi_L
= [q_aH_L-q_aH_LQ_w^*(Q_wQ_w^*)^(-1)Q_w]xi_L
= -q_a[H_L,P_w]xi_L.
```

In the split `H_L=H_L^A-H_L^P`, the remaining theorem is the paired
archimedean-prime cancellation:

```text
q_aH_L^A(I-P_w)xi_L - q_aH_L^P(I-P_w)xi_L = O_M(L^-M).
```

This is still not a proof, but it identifies the exact non-circular row whose
pairing must be forced by the Gamma-prime eigenline equation.

E73.264 tests whether this can be strengthened to a row-level approximation
`rho^A ~= rho^P`, or whether the cancellation occurs only after pairing with
`xi_L`.  This decides whether the next analytic theorem is a Schur-row theorem
or a genuinely eigenline-paired transport theorem.

The result rejects row-level convergence: `pairRel` is tiny, but `rowDiffRel`
is not and reaches `0.605` in the tested range.  Thus the remaining theorem is
genuinely paired:

```text
<rho^A-rho^P,xi_L>=O_M(L^-M),
```

not `rho^A-rho^P=O_M(L^-M)` in norm.

E73.265 moves the projector from the right to the left.  The left-projected
matching

```text
q_aR_wH_L^Axi_L-q_aR_wH_L^Pxi_L=0
```

is exact by the eigenline equation and `q_aR_w=0`.  The actual center is the
difference of the two transport defects:

```text
T_X=q_aH_L^XR_wxi_L-q_aR_wH_L^Xxi_L=q_a[H_L^X,R_w]xi_L,
```

so the final theorem is the commutator transport matching

```text
q_a[H_L^A,R_w]xi_L-q_a[H_L^P,R_w]xi_L=O_M(L^-M).
```

E73.266 audits the tempting rank-two expansion

```text
q_aH_LR_wxi_L=(mu_L e_a-q_aH_LQ_w^*(Q_wQ_w^*)^(-1))Q_wxi_L.
```

The identity is exact, but it collapses to the circular E73.240 branch because
it uses `Q_wxi_L` as the input.  It is therefore a detector only; the surviving
non-circular target remains the commutator transport matching of E73.265.

E73.267 expands that surviving target to the cell level.  With `Q_y(m,n)` the
finite CCM cell matrix,

```text
q_a[H_L^P,R_w]xi_L
=sum_{p^k<=e^L}(log p)p^(-k/2)q_aQ_{klog p}R_wxi_L,
```

and

```text
q_a[H_L^A,R_w]xi_L
=mathcal A_L[y -> q_aQ_yR_wxi_L].
```

Thus the remaining theorem is the finite signed cell identity:

```text
mathcal A_L[q_aQ_yR_wxi_L]
-sum_{p^k<=e^L}(log p)p^(-k/2)q_aQ_{klog p}R_wxi_L
=O_M(L^-M).
```

E73.268 identifies this cell identity with the earlier coefficient and
second-Abel normal forms:

```text
CELL-CTM <=> COEFF-ETA <=> SECOND-ABEL.
```

Thus the current frontier is a single scalar theorem written in three exact
languages, not three independent conditions.

E73.269 records the master finite identity theorem.  It consolidates the final
equivalent forms:

```text
UNIF-ETA
<=> CELL-CTM
<=> COEFF-ETA
<=> SECOND-ABEL
<=> COMM-TRANSPORT.
```

The remaining load-bearing theorem is:

```text
S_{a,w,L}=q_aH_L(I-P_w)xi_L=O_M(L^-M)
```

uniformly, with `S_{a,w,L}` equivalently given by the cell, coefficient,
second-Abel, or commutator-transport formulas.

E73.270 audits the surviving Loewner/displacement input against earlier Phase
72 and Phase 73 work.  The exact identity

```text
Q_y=2cos(yD)-(2/L)D(sin(yD))[J]
```

can be inserted into the master scalar, but E72.55/E72.58 already rule out the
two tempting shortcuts: separate absolute bounds on the cosine/Loewner pieces
and literal rank-one endpoint suppression.  The admissible theorem is therefore
the coupled Loewner master divisibility:

```text
F_L[
  2q_acos(yD)R_wxi_L
  -(2/L)q_aD(sin(yD))[J]R_wxi_L
]=O_M(L^-M),
```

preferably after the E73.192 ramp subtraction, where the remaining packet has a
double zero and the second-Abel form can be attacked by integration by parts.

E73.271 converts the coupled Loewner/second-Abel target into the non-circular
row quotient where the eigenline can be used correctly.  For

```text
E_L=H_L-mu_LI,       rho_a=q_aH_LR_w,
M_L^{sym}={Y^*E_L : Y in P_L^{sym}},
Delta_a=rho_a-Proj_{M_L^{sym}}rho_a,
```

one has exactly

```text
q_aH_LR_wxi_L=Delta_axi_L
```

because the projected part is a left coborder and annihilates `xi_L`.  The
remaining theorem is therefore the curvature quotient divisibility estimate

```text
Delta_axi_L=O_M(L^-M)
```

with `Delta_a` computed from exact symbolic quotient coordinates, not by a
pseudoinverse tuned against `xi_L` and not via the circular variable `Q_wxi_L`.

E73.272 applies the correction already proved in E73.256 to the E73.271
quotient language.  Since every exact row in a left-coborder module

```text
M={Y^*E_L},        E_Lxi_L=0
```

pairs to zero with `xi_L`, quotienting cannot create scalar cancellation:

```text
(rho_a-Proj_Mrho_a)xi_L=rho_axi_L.
```

Thus the quotient branch remains useful for nondegeneracy, pivot selection,
and finite coordinate certification, but the scalar theorem is still the
principal residual

```text
APR-U4:
q_aH_LR_wxi_L=O_M(L^-M).
```

The next analytic attack must prove APR-U4 directly in one of its equivalent
forms: cell, coefficient, commutator transport, or balanced second-Abel /
coupled Loewner.

E73.273 records the admissibility lemma for the only remaining possible
source of cancellation, `EIG-COEFF`.  Any exact linear relation obtained from
the eigenline equation is a left-coborder:

```text
T_Lxi_L=0 from E_Lxi_L=0  =>  T_L=Y_L^*E_L.
```

Such a coborder annihilates `xi_L` automatically and has no scalar content
unless it decomposes the principal residual as

```text
q_aH_L(I-P_w)=Y_{a,w}^*(H_L-mu_LI)+r_{a,w}
```

with a fixed symbolic primitive and an explicit residual satisfying

```text
r_{a,w}xi_L=O_M(L^-M).
```

Thus the next real proof object is not another projection or moment relation:
it is a symbolic coborder-plus-residual identity derived from the coupled
Loewner second-Abel formula.

E73.274 adapts the E73.162 coefficient-defect architecture to the corrected
APR-U4 residual.  The principal row is

```text
rho_a=q_aH_L(I-P_w)=q_aH_L-A_aQ_w,
```

so the desired symbolic identity is

```text
rho_a=Y_{a,w}^*(H_L-mu_LI)+r_{a,w},
and r_{a,w}xi_L=O_M(L^-M).
```

The proposed next target is not the old polynomial/rational/DD-local module
already rejected, but a coupled Loewner-principal module built from the exact
identity

```text
Q_y=2cos(yD)-(2/L)D(sin(yD))[J]
```

and the balanced second-Abel functional.  The immediate falsifier is a
source-coordinate audit: construct the APR source basis and coefficient action
before any pairing with `xi_L`, then see whether only named endpoint/Loewner
residual slots remain.

E73.275 runs the first falsifier for E73.274.  It tests polynomial Cauchy,
DD-local, CL-action, and DD+CL primitive proxies for

```text
rho_a=q_aH_L(I-P_w)=Y^*(H_L-mu_LI)+r.
```

The CL-action proxy includes `H_Lq_j^*`, archimedean action, prime action, and
their `D^2` variants.  It improves some row geometry but does not close the
APR coborder: the residual pairing remains the principal center, as predicted
by left-coborder invariance, and the residual row is still much larger than
the scalar center.  Therefore the missing object is not action-generated
primitive vectors; it must be a source-coordinate construction using the
balanced second-Abel curvature slots.

E73.276 checks that source-coordinate construction.  The adjoint source row of
the coefficient curvature functional is

```text
Src_a=sum W_omega u_omega+sum V_omega v_omega,
```

where `c_omega=u_omega eta` and `l_omega=v_omega eta`.  The probe verifies the
exact collapse

```text
Src_a=q_aH_L.
```

The balanced second-Abel version gives the same row because the ramp is
neutral.  Therefore curvature coordinates alone do not create a new mechanism;
they exactly rewrite APR.  The remaining task is sharper:

```text
q_aH_LR_w=Y_{a,w}^*(H_L-mu_LI)+r_{a,w}
```

with `Y_{a,w}` symbolic and `r_{a,w}` in named residual slots whose pairing
with `xi_L` is proved small.

E73.277 records the resulting residual-slot theorem.  Since every left
coborder row has the form `Y^*(H_L-mu_LI)` and annihilates `xi_L`, any pure
quotient or projection by left coborders leaves the APR scalar unchanged:

```text
(rho_{a,w}-Proj_M rho_{a,w})xi_L=rho_{a,w}xi_L.
```

Therefore a non-tautological proof must exhibit

```text
rho_{a,w}=Y_{a,w}^*(H_L-mu_LI)+r_{a,w}
```

where `Y_{a,w}` is a fixed symbolic primitive and `r_{a,w}` is a named
residual class with a direct scalar estimate.  The audit against older program
material shows that Sonin/prolate/Feshbach/Loewner are already explored
languages here, not standalone closure mechanisms.  The only named residual
slot currently surviving is the canonical three-dimensional `cauchy0` quotient
from E73.163--E73.167:

```text
QUOT-CRIT-DIV:
e^(alpha L)|<P_{Q,L}Pi_A,G_K>| <= L^B.
```

The next meaningful theorem is the APR-to-cauchy0 bridge: prove that the APR
principal residual descends to that same quotient, then prove the signed
quotient Cauchy divisor estimate there.

E73.278 tests this bridge directly and rejects the pure `cauchy0` reduction.
The APR row

```text
rho_j(w)=q_jH_L(I-P_w)
```

fits into the canonical E73.163 source coordinates, but its scalar center is
not carried by the three-dimensional `cauchy0` quotient alone.  In trusted
rows, `quot/center` ranges from tiny to enormous, and the complementary
sector is often order one or larger relative to the true center.  Therefore
APR-U4 is a coupled canonical-sector cancellation, not the old pure
`cauchy0` quotient theorem.

The next target is now:

```text
COUPLED-APR-QUOT:
prove that the fixed canonical source-space class [rho_j(w)] in S_L/M_L
pairs with xi_L by O_M(L^(-M)), retaining cauchy0, rational, and endpoint
sectors together.
```

E73.279 tests this full canonical quotient and rejects it as well.  The class
in `S_L/M_L` is not the small object: both the quotient part and the generated
part can be many orders larger than the true APR center.  The small center is
an interference between generated and residual canonical sectors.  Therefore
the next target is not a quotient theorem but a coupled pairing theorem:

```text
COUPLED-PAIR:
rho_j(w)=S_Lc_{j,w},
c_{j,w}=m_{j,w}+u_{j,w},  m_{j,w} in M_L,
and
<xi_L,S_Lm_{j,w}>+<xi_L,S_Lu_{j,w}>=O_M(L^(-M)).
```

Equivalently, with `ell_L(c)=<xi_L,S_Lc>`, prove that the fixed APR
coefficient vector lies in a finite near-kernel of `ell_L` generated by the
canonical action graph.  Quotienting away the generated sector is now known to
destroy the cancellation.

E73.280 tests this near-kernel formulation directly.  For APR coefficient
vectors `c_{j,w}` one has

```text
dist(c_{j,w},ker ell_L)
= |ell_L(c_{j,w})|/(||ell_L|| ||c_{j,w}||)
~ 1e-8 to 1e-10
```

in the tested windows, while `ell_L` on the generated and orthogonal pieces is
much larger and cancels by phase.  The current proof-facing theorem is now:

```text
APR-NEARKER:
ell_L(c_{j,w})=O_M(L^(-M))
```

for the canonical APR coefficient vector, preserving the generated/residual
interference.  The next task is to derive a symbolic finite near-kernel
identity involving the canonical action matrix, `c_{j,w}`, and `ell_L`.

E73.281 corrects this interpretation.  In exact mesh algebra, generated
columns satisfy

```text
ell_L(E_Lp)=<xi_L,E_Lp>=<E_Lxi_L,p>=0.
```

The large generated pairings seen in E73.279--E73.280 are coordinate-fit
contamination, not mathematical signal.  Even `imageRel` around `1e-6` is far
too crude when the APR scalar is around `L^-20`.  The corrected proof-facing
object is the exact source complex:

```text
P_L --E_L--> S_L --ell_L--> C,
ell_L E_L=0.
```

The next task is to build exact symbolic source coordinates for APR rows and
the generated image, by partial fractions or another exact representation,
before making quotient or near-kernel claims.

E73.282 tests whether the current canonical source basis can be repaired by
adding more rational and endpoint atoms.  It cannot: increasing the basis
causes rank collapse and worsens the scalar reconstruction.  The issue is not
just missing atoms; it is redundancy and ill-conditioning in the fitted source
coordinates.  The next proof-facing target is therefore:

```text
EXACT-SRC:
derive a minimal symbolic partial-fraction source basis S_L^ex and primitive
basis P_L^ex such that

E_L P_L^ex = S_L^ex A_L^ex
```

entrywise, with no least-squares coordinate error.  Only then can the exact
complex

```text
P_L^ex --E_L--> S_L^ex --ell_L--> C
```

be used to formulate a clean quotient theorem for APR.

E73.283 identifies the exact source basis that avoids the rational-coordinate
contamination: the finite frequency packet space of the CCM cells.  Since

```text
q_nn(y)=2(1-y/L)cos(d_n y),
q_mn(y)=(sin(d_m y)-sin(d_n y))/(pi(n-m)),
```

every packet

```text
B_{a,eta}(y)=q_aQ_yeta
```

has an exact expansion

```text
B_{a,eta}(y)
=sum_omega c_omega e^(iomega y)
 +y sum_omega l_omega e^(iomega y),
omega in {±d_n}.
```

Thus the corrected exact source space is the frequency space `F_L`, not the
ill-conditioned rational `d`-basis.  The endpoint returns, cleanly and
exactly, to

```text
APR-FREQ:
sum_omega c_omega(R_wxi_L)W_omega
+sum_omega l_omega(R_wxi_L)V_omega
=O_M(L^(-M)).
```

This is the same scalar as `APR-U4`, `CELL-CTM`, and `COEFF-ETA`, now in a
coordinate system with no least-squares error.  The remaining theorem is the
signed frequency divisibility statement `FREQ-DIV`.

E73.284 tests whether `FREQ-DIV` follows from higher frequency moment
annihilation.  It does not.  The only exact small moments are the endpoint
ones already proved in E73.236:

```text
sum c_omega=0,
sum l_omega=0.
```

Higher derivative moments are not small; `B'(0)` is the rank-one endpoint
source from E73.190 and survives.  Thus the only justified weight gauges are
constant shifts:

```text
W_omega -> W_omega-alpha_L,
V_omega -> V_omega-beta_L.
```

The current endpoint is therefore `GAUGE-FREQ-DIV`: prove the Gamma-prime
frequency pairing after removing only these constant gauges.

E73.285 probes the gauged weights themselves.  After subtracting constants,
the weights are not small and not naively smooth:

```text
||W'|| ~ L^(1.3--1.5),
||V'|| ~ L^(2.0--2.2).
```

The observed structure is instead a block cancellation:

```text
sum c_omega W'_omega
~ - sum l_omega V'_omega
```

to relative scale `1e-12--1e-15` in the probe.  The individual basis-weight
quadrature does not resolve the final APR center, so this is diagnostic, not
an interval certificate.  The refined target is:

```text
BLOCK-FREQ-DIV:
sum c_omega W'_omega
= -sum l_omega V'_omega + O_M(L^(-M)).
```

The next required object is an exact closed formula for `W_omega,V_omega`
strong enough to prove this c/l block cancellation.

E73.286 tests the tempting discrete derivative bridge

```text
V_omega ?= (1/i)D_omega W_omega
```

on the mesh frequencies.  It fails: finite-difference derivative error is
order one and the resulting discrete integration-by-parts pairing is ordinary
size, not APR-small.  The formal continuous identity may still hold for a
closed function `W(omega)`, but the mesh derivative is not proof-facing.  The
next object must be exact closed formulas for `W_omega,V_omega`, including
both archimedean and prime parts.

E73.287 derives and verifies those formulas.  The finite prime weights are:

```text
W^P_omega=sum_{p^k<=e^L}(log p)p^(-k/2)e^(i omega klog p),
V^P_omega=sum_{p^k<=e^L}(log p)p^(-k/2)(klog p)e^(i omega klog p).
```

The archimedean weights are elementary exponential integrals plus the
`1/(2sinh y)` series:

```text
W^A_omega=I_0(1/2+iomega)+I_0(-1/2+iomega)
          -sum_{r>=0}I_0(-(2r+1/2)+iomega),

V^A_omega=I_1(1/2+iomega)+I_1(-1/2+iomega)
          -sum_{r>=0}I_1(-(2r+1/2)+iomega).
```

The raw `W` formula differs from the reference by a constant gauge only, which
is invisible because `sum c_omega=0`; the gauged error is at numerical floor.
The current fully explicit endpoint is now `BLOCK-FREQ-DIV` with these
closed weights.

E73.288 refines the coefficient side.  In the exact cell expansion,
off-diagonal cells contribute only to `c`, while diagonal cells contribute to
both `c` and `l`.  The exact identity is:

```text
l_omega=-c^diag_omega/L.
```

Therefore `BLOCK-FREQ-DIV` is equivalent to:

```text
DIAG-OFF-FREQ-DIV:
sum c^off_omega W'_omega
+sum c^diag_omega (W'_omega - V'_omega/L)
=O_M(L^(-M)).
```

This is the current sharp finite identity: closed weights from E73.287,
exact diagonal/off-diagonal coefficients from the CCM cell formulas.

E73.289 checks whether `U'=W'-V'/L` is generated by `W'` through a simple
weight relation.  It is not: the affine/conjugate fit has relative error
around `0.4--0.6`.  But for the APR coefficient pair the two block pairings
cancel to relative scale `1e-13--1e-15`:

```text
<c^off,W'> + <c^diag,U'> = APR-small.
```

The endpoint is therefore a dual coefficient-weight identity:

```text
PAIR-DUAL-FREQ-DIV:
<c^off_{a,w},W'>
= -<c^diag_{a,w},U'> + O_M(L^(-M)).
```

This cannot be proved from weights alone; the Gamma-prime eigenline equation
must enter the coefficient split.

E73.290 removes the last coefficient bookkeeping from this endpoint.  Define

```text
W^odd_j = W'_{d_j}-W'_{-d_j},
U^even_j = U'_{d_j}+U'_{-d_j}.
```

For the Cauchy row `r_j=q_a(d_j)`, the exact residual kernel is

```text
K_b
= r_b U^even_b
  + sum_{j != b} r_j (W^odd_j-W^odd_b)/(2 i pi (n_b-n_j)).
```

Then the diagonal/off-diagonal identity is exactly

```text
<c^off,W'>+<c^diag,U'> = sum_b (R_w xi_L)_b K_b.
```

The probe verifies this equality at numerical floor.  It also tests whether
`K` is killed by the two-dimensional Cauchy plane.  It is not: the residual
outside the Cauchy plane carries essentially the full pairing.  Therefore the
old `cauchy0` endpoint remains rejected, and the current proof-facing target is

```text
KERNEL-FREQ-DIV:
sum_b (R_w xi_L)_b K_{a,w,L}(b)=O_M(L^(-M)).
```

This is the cleanest current form of scalar WRL: closed weights, an explicit
finite Hilbert-transform-like mesh kernel, and the projected Gamma-prime
eigenvector.  The next required theorem is not a projection theorem, but a
commutator/eigenline identity forcing this specific residual pairing to be
flat.

E73.291 identifies this frequency kernel with the existing Schur-commutator
row.  More precisely,

```text
K = qH_L + alpha q_w + beta q_-w,
```

where the two extra rows are only the constant closed-weight gauges.  Since
`eta=R_wxi_L` satisfies `Q_weta=0`,

```text
sum_b eta_bK_b = qH_LR_wxi_L = -q[H_L,P_w]xi_L.
```

Therefore `KERNEL-FREQ-DIV` is not a new independent gate: it is the
closed-weight coordinate form of the Schur-Commutator Eigenline Cancellation
from E73.263.  The route has one remaining theorem, now with two equivalent
proof-facing languages:

```text
Schur form:    q[H_L,P_w]xi_L=O_M(L^(-M)).
Frequency form:
sum_b (R_wxi_L)_b[
  q_b U^even_b
  + sum_{j != b} q_j(W^odd_j-W^odd_b)/(2 i pi(n_b-n_j))
]=O_M(L^(-M)).
```

The next analytic attack should prove this paired commutator cancellation
directly; a row-norm estimate or a pure Cauchy projection theorem has already
been ruled out.

E73.292 rewrites the same endpoint in Loewner form.  Set

```text
F_j=W^odd_j,
Lambda_F(j,b)=(F_j-F_b)/(d_j-d_b), j != b,
Lambda_F(j,j)=0,
M_U=diag(U^even_j).
```

Then

```text
K = qM_U - (1/(iL))q Lambda_F,
```

and the remaining theorem is equivalently

```text
Directional Loewner Eigenline Cancellation:
q( M_U-(1/(iL))Lambda_F )R_wxi_L=O_M(L^(-M)).
```

The vector identity is verified at roundoff in E73.292.  This is now the
most analytic normal form of the scalar WRL gate: a diagonal derivative term
plus an off-diagonal divided-difference commutator, paired with the transverse
Gamma-prime eigenline.

E73.293 tests the tempting one-symbol closure where `U^even` would be the
Loewner diagonal of `W^odd`.  This is false.  The exact differential identity

```text
dW_omega/domega=iV_omega
```

shows that the Loewner diagonal accounts only for `-V^even/L`, while

```text
U^even=W^even-V^even/L.
```

Hence the correct normal form is two-symbol:

```text
K = qM_{W^even}-(1/(iL))q Lambda_{W^odd}^{full},
```

with the full Loewner diagonal

```text
Lambda_{W^odd}^{full}(j,j)=d/domega(W_omega-W_-omega)|_{omega=d_j}.
```

The remaining theorem is therefore:

```text
Two-Symbol Loewner Eigenline Cancellation:
q[ M_{W^even}-(1/(iL))Lambda_{W^odd}^{full} ]R_wxi_L=O_M(L^(-M)).
```

This correction matters: neither the even diagonal nor the odd Loewner term is
separately the proof object.  The endpoint is their signed coupling.

E73.294 closes the algebraic loop: the two-symbol operator reconstructs the
original CCM cell pointwise in `y`.  For

```text
W_y^even(d)=2cos(dy),
W_y^odd(d)=2i sin(dy),
```

one has exactly

```text
M_{W_y^even}-(1/(iL))Lambda_{W_y^odd}^{full}=Q_y.
```

The diagonal gives `2(1-y/L)cos(d_jy)`, and the off-diagonal gives

```text
(sin(d_jy)-sin(d_by))/(pi(n_b-n_j)).
```

After applying the Gamma-prime functional, this is precisely `H_L`.  Hence
the recent forms are all the same endpoint:

```text
two-symbol Loewner form
= finite CCM cell form
= closed frequency-weight form
= Schur-commutator row
= master scalar S_{a,w,L}.
```

The remaining irreducible finite theorem is:

```text
Directional Cell Eigenline Cancellation:
F_L[y -> q_aQ_yR_wxi_L]=O_M(L^(-M)),
```

equivalently,

```text
q_a[H_L,P_w]xi_L=O_M(L^(-M)).
```

This is now the clean endpoint of the Phase 72/73 scalar WRL gate.

E73.295 packages the endpoint as a phase-free finite adjugate identity.  With

```text
rho_{a,w}=q_aH_L(I-P_w),
E_L=H_L-mu_LI,
Adj_red(E_L)=c_Lxi_Lxi_L^*
```

for the simple ground channel, one has

```text
|rho_{a,w}xi_L|
= ||rho_{a,w}Adj_red(E_L)|| / ||Adj_red(E_L)||.
```

Thus the final finite identity can be stated without choosing an eigenvector
phase:

```text
FINAL-ETA-ADJ:
||q_aH_L(I-P_w)Adj_red(H_L-mu_LI)||
<= A_M L^(-M)||Adj_red(H_L-mu_LI)||.
```

This is equivalent to the Directional Cell Eigenline Cancellation above.  It is
a detector/certificate, not a forcer: the proof must estimate it from the
explicit Gamma-prime entries, not by projecting onto `Row(E_L)` or by using
`Q_wxi_L` as small input.

E73.296 closes one tempting shortcut after the adjugate package: the Cauchy
principal compression

```text
A=QH_LQ^*(QQ^*)^(-1)
```

does not force the defect.  Although

```text
QH_LR_wxi_L=(mu_LI-A)Qxi_L
```

is exact, the matrix `mu_LI-A` is not small or structurally singular in the
tested stable windows; for `lambda=16,20`, its norm and least singular value
are positive powers of `L`.  Thus the smallness again lives in the specific
vector `Qxi_L`, which is the circular input already rejected.  The rank-two
compression remains a detector only.

E73.297 rewrites the second-Abel endpoint with all ramp bookkeeping absorbed
into one explicit curvature operator.  For

```text
B(y)=qQ_yR_wxi_L,
B^bal(y)=B(y)-B'(0)y(1-y/L),
```

one has exactly, for the full neutral ramp `r_*=r_0+c_Lr_1`,

```text
(B^bal)''(y)=q[Q_y''+alpha_L(y)J]R_wxi_L,
alpha_L(y)=(2/L)[-2/L+c_L(2-6y/L)],
J=11^T.
```

Thus the same endpoint is:

```text
CURV-ABEL:
int_0^L K_L(t) q[Q_t''+alpha_L(t)J]R_wxi_L dt
=O_M(L^(-M)).
```

This is equivalent to `FINAL-ETA-ADJ`, but it is the cleanest second-Abel
analytic form: the boundary/ramp source is now the explicit rank-one
curvature correction `alpha_L(t)J`.

E73.298 audits the next tempting shortcut: whether the balanced curvature
row family

```text
y -> q[Q_y''+alpha_L(y)J]R_w
```

is controlled by a fixed small number of modes.  The answer is no as a
uniform forcer.  Some sampled row families are mildly compressible, but the
actual scalar direction can remain largely outside the leading four or eight
row singular modes; representative `scalarProj8` residuals are `0.75--0.92`.
This matches the earlier E72.94/E72.95 lesson: the endpoint is not explained
by low moments or low rank.  `CURV-ABEL` remains a signed full-kernel
orthogonality theorem to prove from the explicit Gamma-prime/eigenline
structure.

E73.299 records a sign correction for the simple ramp.  E73.301 supersedes it
for the actual neutral ramp of E73.193.  The correct contribution is:

```text
(B^bal)''=q[Q_y''+alpha_L(y)J]eta,
alpha_L(y)=(2/L)[-2/L+c_L(2-6y/L)].
```

The derivation is `Q_0'=-(2/L)J` and
`r_*''(y)=-2/L+c_L(2-6y/L)`.  The earlier constant-only correction was
incomplete because it silently set `c_L=0`.  The final endpoint and the
E73.298 no-low-rank conclusion survive after the full correction.

E73.300 propagates the sign correction into the quotient language.  The
proof-facing row is now canonically

```text
q int_0^L K_L(t)[Q_t''+alpha_L(t)J]dt R_w.
```

This still collapses to the same source row `qH_L` under the adjoint
coefficient representation, so it is not a new mechanism by itself.  Its use
is to give the corrected local representative for any future symbolic quotient
proof of the same scalar theorem.

E73.301 gives the final neutral-ramp curvature correction:

```text
alpha_L(t)=(2/L)[-2/L+c_L(2-6t/L)].
```

E73.302 then records the weight-level collapse:

```text
R_*=int_0^L K_L(t)r_*''(t)dt=F_L[r_*]=0.
```

Thus the local `alpha_L(t)J` term is necessary for endpoint-free integration
by parts, but it contributes no new global frequency weight.  The final
frequency endpoint remains the original signed `W_omega,V_omega` pairing
against the Cauchy-Schur coefficients.

E73.303 rewrites that final frequency endpoint as a one-symbol distribution
identity.  Since `dW/domega=iV`,

```text
sum c_omega W_omega+sum l_omega V_omega
= <T_eta,W>,

T_eta=sum c_omega delta_omega
     +i sum l_omega delta'_omega.
```

This is not the rejected finite-difference integration by parts of E73.286;
the derivative is the exact distributional derivative at the frequency
support.  A moment audit shows that only `<T,1>` is small, while `<T,omega>`
and `<T,omega^2>` are much larger than the center.  So the current endpoint is
now:

```text
prove <T_{R_wxi_L},W_L>=O_M(L^(-M))
```

from the Gamma-prime/eigenline structure, not from low moments.

E73.304 removes the remaining coefficient-map layer.  The distribution is
directly:

```text
T^diag=sum_b r_b eta_b(delta_{d_b}+delta_{-d_b})
       -(i/L)sum_b r_b eta_b(delta'_{d_b}+delta'_{-d_b}),

T^off=sum_{j != b} r_j eta_b /(2 i pi(n_b-n_j))
      [delta_{d_j}-delta_{-d_j}-delta_{d_b}+delta_{-d_b}].
```

Pairing this closed distribution with the single symbol `W_L` gives exactly
the E73.290 `K-DIAGOFF` kernel and hence the final scalar.  This is the most
explicit current endpoint:

```text
prove <T^diag_{a,w,L}+T^off_{a,w,L},W_L>=O_M(L^(-M)).
```

E73.305 rewrites the off-diagonal term by a mesh Hilbert product rule.  With

```text
A_{jb}=1/(2 i pi(n_b-n_j)),
```

the off-diagonal pairing is exactly:

```text
sum_j W^odd_j [r_j(A eta)_j+eta_j(A r)_j].
```

So the endpoint is a three-term signed cancellation:

```text
sum_j eta_j r_j U^even_j
+sum_j W^odd_j r_j(A eta)_j
+sum_j W^odd_j eta_j(A r)_j
=O_M(L^(-M)).
```

The probe shows none of the three terms is individually small enough; the
smallness is the same load-bearing cancellation in a product-rule normal form.
