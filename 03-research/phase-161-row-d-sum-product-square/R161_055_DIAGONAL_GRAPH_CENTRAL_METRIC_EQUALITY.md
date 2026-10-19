# R161_055 — Diagonal graph limit gives the central metric equality

## 1. Abstract diagonal lemma

Let E_N=Y_N-X_N be bounded on a common smooth core C. Suppose a vector F belongs to a closed common graph G, C is graph-dense in G, and for every f in C

    E_N f ->0,
    X_N f ->Xf                                             (1.1)

in H. Then there are f_j in C and N_j tending to infinity such that

    f_j ->F in G,
    E_(N_j)f_j ->0,
    X_(N_j)f_j ->XF,
    Y_(N_j)f_j ->XF.                                      (1.2)

Proof. Choose f_j graph-converging to F. For each fixed j, choose N_j larger than N_(j-1) so that the first two errors in (1.1) are below 1/j. Enlarge j if needed so the graph-limit errors are below 1/j. Since Y_N=X_N+E_N, the last convergence follows. This is the standard diagonal argument; it asserts existence of a compatible regularization, not uniform convergence for arbitrary coupled sequences.

For every orthogonal projection P,

    ||P Y_(N_j)f_j||^2-||P X_(N_j)f_j||^2 ->0.            (1.3)

Indeed both projected vectors converge to PXF. Equivalently, using d_j=E_(N_j)f_j,

    ||P(X_(N_j)f_j+d_j)||^2-||PX_(N_j)f_j||^2
      =2 Re<PX_(N_j)f_j,Pd_j>+||Pd_j||^2 ->0.             (1.4)

## 2. Application to the renormalized Poisson histories

Take

    X_N=Z_N^*J,
    Y_N=Z_N Fcal,
    E_N=E_N^ren.                                          (2.1)

R161_040 proves Y_N-X_N=E_N exactly. R161_003 proves convergence on the smooth core, while the phase-121 common zeta-Gamma graph supplies the graph closure containing a first-contact vector. Applying the lemma yields a compatible smooth/cutoff diagonal on which the two histories converge strongly to the same completed Poisson vector.

For the physical-window projection P_0,

    ||P_0 Z_(N_j)Fcal f_j||^2
      -||P_0 Z_(N_j)^*J f_j||^2 ->0.                    (2.2)

The same holds for P_L and P_R separately at the undifferentiated level, because (1.3) is valid for every fixed orthogonal projection. This does not identify a rescaled or differentiated boundary layer: both raw projected differences may simply converge to zero.

## 3. Tate corrections

Let T_j be a finite-rank correction depending continuously on the two Tate collar coordinates in the graph topology. If the same canonical correction is attached to both Poisson histories, replace X_(N_j)f_j and Y_(N_j)f_j by X_(N_j)f_j+T_jf_j and Y_(N_j)f_j+T_jf_j. Their difference remains d_j, so (1.3)-(1.4) are unchanged.

R161_009 proves that the two polar coefficients are continuous collar functionals and uniquely fixes them from the crossed Tate system. Therefore the undifferentiated central metric equality survives the canonical polar/Tate correction. No sign of the crossed Tate matrix is needed for this base equality.

## 4. What is now removed, and what remains

In the squeeze ledger of R161_054, the uncontrolled central scalar Delta_0 vanishes along a compatible common-graph diagonal. Hence a separate postulated central metric anomaly is unnecessary at order zero.

The closing norm comparison, however, concerns the covariant tangent/boundary-layer scaling. Ordinary convergence E_Nf_j->0 does not imply that a normalized derivative or projected tangent tends to zero. To finish the squeeze one must still prove that:

1. the plus and minus tangent exterior blocks converge to the same canonical Hardy norm family in reversed order;
2. the differentiated polar correction produces exactly the crossed Tate endpoint term;
3. after that correction the central tangent remainder is o(delta), not merely the undifferentiated remainder o(1).

These are now the only metric identifications left in the colligation route.

## Status

- compatible common-graph diagonal: proved abstractly and applicable to the established smooth-core/closed-graph data;
- undifferentiated central metric equality: proved along that diagonal;
- stability under the canonical finite-rank Tate correction: proved;
- differentiated tangent and common-port norm identification: open;
- D: open.
