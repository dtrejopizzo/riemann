# D.225 — Native flat/boundary Schur decomposition at \(T=\frac12\log6\)

## Verdict

The complete primitive finite space now has a source-defined directed
decomposition

\[
 V_{200}^{\rm prim}=D_{\rm bdry}\dotplus S_{\rm flat},
 \qquad \dim D_{\rm bdry}=120,\quad\dim S_{\rm flat}=78,
\]

where \(S_{\rm flat}\) consists of functions divisible by
\((1-t^2/T^2)^{60}\) and satisfies both Tate equations.  The complement
\(D_{\rm bdry}\) is constructed as the exact \(L^2\)-orthogonal complement
inside \(V_{200}^{\rm prim}\).

With the complete native Gamma/contact operator:

* \(S_{\rm flat}^*A_TS_{\rm flat}>0\);
* the Schur complement obtained by eliminating \(S_{\rm flat}\) is positive;
* the resulting \(120\)-column boundary graph is exactly
  \(A_T\)-orthogonal to the flat channel.

All three statements are **CERTIFIED BY INTERVALS**.  This completes the
finite algebra required by the route selected in D.223.  It does not yet
pay the boundary graph against the infinite tail.

## Construction

The flat frame is built in the exact rational Gegenbauer basis and the two
Tate equations are solved in Arb.  If \(F\) denotes its \(200\times78\)
matrix and \(X\) an exact primitive frame of \(V_{200}\), the boundary
coordinate matrix is obtained from

\[
 \ker(F^*X).
\]

A deterministic column-pivoted Gram--Schmidt calculation selects the frame
only.  The \(78\) orthogonality equations are then solved again as one Arb
linear system.  Thus the final matrix \(D\) satisfies

\[
 M_\pm D=0,\qquad F^*D=0
\]

as exact interval inclusions.

Put

\[
 B_F=F^*A_TF,\qquad K_D=D^*A_TD,\qquad C=D^*A_TF.
\]

The directed flat block has whitened Gershgorin lower margin

\[
 0.9999999969943472\ldots>0.
\]

After exact shorting,

\[
 K_{\rm bdry}=K_D-CB_F^{-1}C^*,
\]

the directed \(120\times120\) congruence has lower margin

\[
 0.9999986226387550\ldots>0.
\]

Finally,

\[
 D_{\rm graph}=D-FB_F^{-1}C^*
\]

satisfies

\[
 F^*A_TD_{\rm graph}=0.
\]

## Remaining three-block gate

Relative to \(D_{\rm graph}\oplus S_{\rm flat}\oplus Q\), the complete
operator is

\[
 \begin{pmatrix}
 K_{\rm bdry}&0&C_D\\
 0&B_F&C_F\\
 C_D^*&C_F^*&A_{QQ}
 \end{pmatrix}.                                      \tag{3.1}
\]

D.208 proves that the post-\(600\) raw flat action has normalized trace
below \(3.156\,10^{-27}\).  The remaining obligations are:

1. retain the finite \(200{:}600\) Green seen by \(C_F\);
2. convert the D.208 raw tail estimate into the corrected residual appearing
   after that Green solve;
3. pay \(C_D\) against the resulting flat-shorted tail Green.

Equation (3.1) is the correctly typed multilevel problem.  Positivity of its
finite diagonal blocks alone is not used as a full endpoint proof.

## Reproduction

    PYTHONPATH=/tmp/rowd-flint D225_DPS=140 \
    python3 114_d_225_t6_flat_boundary_native_schur.py

The output artifact

    /tmp/t6_flat_boundary_native_schur.npz

has SHA-256

    9dcf45886c646cae9e4c2957aa5580c22844d76c4a7e97d4e0ea2ff207aa0323

## Classification

* exact flat Tate frame: **PROVED / CERTIFIED BY INTERVALS**;
* exact boundary complement: **PROVED / CERTIFIED BY INTERVALS**;
* positivity of the flat block: **CERTIFIED BY INTERVALS**;
* positivity of the flat-shorted boundary block: **CERTIFIED BY INTERVALS**;
* post-\(600\) flat raw tail: **CERTIFIED BY INTERVALS** in D.208;
* finite \(200{:}600\) flat Green: **OPEN**;
* boundary-graph/tail Schur inequality: **OPEN**;
* full endpoint and global row D: **OPEN**.
