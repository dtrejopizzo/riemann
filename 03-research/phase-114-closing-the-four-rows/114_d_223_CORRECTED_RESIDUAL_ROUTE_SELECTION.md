# D.223 — Corrected-residual falsifier and route selection

## Verdict

D.222 proves that the exact Green on the orthogonal band \(200{:}260\)
costs at most \(0.09\) of the old safe budget.  The remaining theorem is

\[
 R_W^*R_W\le0.134139\,B.                             \tag{0.1}
\]

Two numerical falsifiers were applied before attempting a large interval
calculation.

1. On a calibrated QR projection of the fixed D.222 corrected source, the
   binary64 residual norm at cutoff \(260\) has centre about \(0.3057\).
   The projected centres at cutoffs \(320,400,600\) are approximately
   \(0.2778,0.2553,0.2218\).  These numbers are **HEURISTIC**: the Green
   correction was not recomputed at the larger cutoffs.
2. A direct FFT attempt to recompute the finite Green at larger cutoffs
   fails its mandatory calibration.  The safe block, which Arb whitens to
   identity, is returned with numerical spectrum ranging from
   \(3.75\,10^{-4}\) to \(4.39\,10^4\).  The resulting capacity numbers are
   therefore **REJECTED**, not evidence about (0.1).

The conclusion is methodological and rigorous: a raw uniform-grid FFT
cannot certify the corrected residual, and the unflattened fixed-cutoff
projection does not display enough numerical margin to justify a costly
interval implementation at \(260\).

The active local route is therefore the source-defined endpoint-flat
multilevel decomposition of D.205--D.208, combined with the exact Green
identity of D.210.  It retains endpoint logarithms analytically and already
has a certified post-\(600\) tail trace below \(3.156\,10^{-27}\) on the
flat safe channel.

## 1. What the first falsifier computes

Let \(F_W=S-WE^{-1}C^*\) be the exact finite-Green corrected source of
D.222.  It satisfies

\[
 W^*A_TF_W=0.                                        \tag{1.1}
\]

The script D.223 applies the complete Gamma/contact multiplier to \(F_W\)
on a full-line FFT chart and removes measured polynomial projections by QR,
not by ill-conditioned normal equations.  The resulting centres are

\[
\begin{array}{c|cccc}
\text{cutoff}&260&320&400&600\\ \hline
\lambda_{\max}&
0.30570&0.27778&0.25528&0.22179 .
\end{array}                                          \tag{1.2}
\]

Because the source \(F_W\) is held fixed, (1.2) is not the Galerkin residual
obtained after recomputing the Green at each larger cutoff.  It cannot prove
failure of (0.1).  It does show that ordinary Legendre projection pays the
endpoint boundary layer slowly.

## 2. Why the large-cutoff FFT is discarded

D.224 constructs the correct primitive orthogonal trial spaces by the
two-by-two Tate Gram solve and attempts to recompute the Green for increasing
cutoffs.  Before reading any capacity it compares its measured safe block
with the exact Arb whitening from D.222.  The calibration error is enormous:

\[
 \mathrm{spec}(B_{\rm FFT})
 \subset[3.75\,10^{-4},4.39\,10^4],
\]

where the correct whitened block is the identity up to directed errors below
\(10^{-14}\).  Endpoint cancellation and aliasing therefore dominate the
computed form.

The script now terminates after this failed calibration and labels its output

    D224 REJECTED: FFT calibration does not resolve the exact safe block

No capacity value from that run is retained.

## 3. Selected next theorem

Let \(S_{\rm flat}\) be the exact two-Tate primitive endpoint-flat space of
D.207, and let \(D_{\rm bdry}\) be its finite complement inside
\(V_{200}^{\rm prim}\).  D.208 already proves, after whitening the flat safe
block,

\[
 \mathrm{tr}
 \bigl(R_{600}A_TS_{\rm flat}B_{\rm flat}^{-1}
       S_{\rm flat}^*A_TR_{600}\bigr)
 <3.156\,10^{-27}.                                  \tag{3.1}
\]

The next directed construction must combine:

1. the exact finite Green on the band \(200{:}600\);
2. the corrected residual, not the raw action;
3. the post-\(600\) estimate (3.1);
4. the finite boundary channel \(D_{\rm bdry}\);
5. the final Schur budget seen by the original two delicate directions.

The target remains the exact D.221 capacity \(\rho_6\le0.7\).  Endpoint
flatness is an analytic device for proving that capacity; it does not change
the row-D form or redefine the safe space.

The fresh directed artifacts have hashes

    3bdb0a69503221fe3fb77cbb0b6a06a3b2f49d1444219a186bff98c5dab20ff5  t6_flat60_safe_arb.npz
    bb5f22735f199159933ec9f916da27d525f9d780aaf7237e6febd6c538cf54b5  t6_flat60_plancherel_tail_arb.npz

## 4. Classification

* D.222 finite Green capacity \(\le0.09\): **CERTIFIED BY INTERVALS**;
* values in (1.2): **HEURISTIC / NUMERICAL FALSIFIER**;
* D.224 large-cutoff FFT capacities: **REJECTED BY CALIBRATION**;
* post-\(600\) endpoint-flat tail (3.1): **CERTIFIED BY INTERVALS** in D.208;
* assembly of the flat finite Green and boundary channel: **OPEN**;
* corrected residual inequality (0.1): **OPEN**;
* endpoint and global row D: **OPEN**.
