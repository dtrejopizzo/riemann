# Row D two-projection audit

## Question

Can the coupling

\[
C=P_OQ_TP_E=[P_O,Q_T]P_E
\]

be controlled by the exact off-diagonal identity for two orthogonal
projections?

## Typing audit

* (P_O) is an orthogonal support projection. **PROVED.**
* (P_E) is an orthogonal support projection and (P_OP_E=0).
  **PROVED.**
* In general (P_E\ne I-P_O); with a complete support split,
  (I-P_O=P_E+P_R). **PROVED.**
* (Q_T=-B_{{\rm nuc},T}) is a self-adjoint closed form operator.  It is
  not idempotent.  It is not known to be positive or contractive; its
  positivity is row D. **PROVED typing; sign OPEN.**
* (Q_T) is a difference of positive Grams,
  (Q_T=X_T^*X_T-Y_T^*Y_T).  This is a Krein compression, not a Hilbert
  projection. **ALGEBRAIC IDENTITY.**
* (\Pi_T) is an orthogonal projection, but does not commute with the
  support projections. **PROVED.**

Hence the pair ((P_O,Q_T)) is not a pair of projections.

## Exact uncompressed calculation

Put (P=P_O), (E=P_E), and (R=I-P-E).  On a common algebraic core,

\[
CC^*=PQEQP.
\]

Since (I-P=E+R),

\[
\begin{aligned}
PQ(I-P)QP
 &=PQ^2P-PQPQP\\
 &=PQ^2P-(PQP)^2,
\end{aligned}
\]

and therefore

\[
\boxed{
CC^*=PQ^2P-(PQP)^2-PQRQP.
}
\tag{TP1}
\]

Writing (A=PQP), comparison with the projection defect gives the exact
residual

\[
\boxed{
CC^*-(A-A^2)=P(Q^2-Q)P-PQRQP.
}
\tag{TP2}
\]

The last term is negative semidefinite.  The first term has no known sign:
the scalar polynomial (\lambda(\lambda-1)) changes sign on ((0,1)).
It vanishes exactly for a projection and is nonpositive for a positive
contraction.  Neither property is available for (Q_T).

Similarly,

\[
C^*C=EQP QE,
\]

and no complementary defect identity follows without an idempotence or
contraction law for (Q_T).

## Tate compression residual

Let (F_T=I-\Pi_T).  The primitive operator is

\[
Q_T^{\rm prim}=\Pi_TQ_T\Pi_T
=Q_T-F_TQ_T-Q_TF_T+F_TQ_TF_T.
\]

Thus

\[
C^{\rm prim}=P_OQ_T^{\rm prim}P_E=C+\Delta_T,
\]

where

\[
\Delta_T=P_O(-F_TQ_T-Q_TF_T+F_TQ_TF_T)P_E.
\]

On finite-energy regularizations (\Delta_T) has rank at most four, but

\[
C^{\rm prim}(C^{\rm prim})^*
=CC^*+C\Delta_T^*+\Delta_TC^*+\Delta_T\Delta_T^*.
\tag{TP3}
\]

The cross terms in (TP3) have no fixed sign.  Therefore Tate compression
does not repair (TP2); it adds a finite-rank but indefinite residual to an
already infinite-rank boundary block.

## Comparison with the actual Douglas defects

The defects in D.170/D.190 are not (A-A^2) for (A=P_OQ_TP_O).  After
reference Cholesky normalization they are

\[
D_{\rm in}=I-A_N^*A_N,
\qquad D_{\rm out}=I-A_NA_N^*.
\]

The old-cell induction proves (A_N) is a contraction, so Julia--Halmos
constructs these defect channels.  But the new boundary load (y_N) is
external to the Julia colligation.  The missing statement remains

\[
y_N=D_{\rm out}^{1/2}v_N,qquad \|v_N\|\le1.
\]

Defining (v_N=D_{\rm out}^{\dagger/2}y_N) would assume the range and norm
claims to be proved.

## Verdict and next structurally distinct candidate

The two-projection mechanism is **IMPOSSIBLE AS A DIRECT CLOSURE** for the
precise reason (TP2): (Q_T) is not a projection, and the residual contains
(P(Q_T^2-Q_T)P) with no source-known sign.  Making (Q_T) a positive
contraction would be at least as strong as the missing row-D inequality.

The next structurally distinct candidate is not another projection
calculation.  It is to construct the boundary map (v_N) from a genuine
Poisson/scattering colligation for the normalized comparison (A_N), or
equivalently to identify (y_N) as a Hankel operator with a source-defined
Schur-class symbol.  This route must use the arithmetic Poisson
self-duality/Gamma coupling in a way that fails for Beurling surrogate
systems; PNT-strength estimates alone cannot provide the exact constant
one.

**Resultado C:** The commutator cannot be controlled by the
projection/defect mechanism because (Q_T) is neither a projection nor a
known contraction; the exact obstruction is
(P_O(Q_T^2-Q_T)P_O-P_OQ_TP_RQ_TP_O), plus the finite-rank indefinite Tate
residual (TP3).  The next structurally distinct candidate is a
source-defined Poisson/Hankel scattering colligation for (A_N) whose
defect input is exactly (y_N).

