# Certified correction: the discrete convexity barrier is false

## Verdict

The proposed sufficient condition

\[
 \Delta^2D_n\ge0\qquad(n\ge1),
 \qquad D_n=2\lambda_n-\lambda_n^{\rm arch},
\tag{1}
\]

is false for the actual Riemann zeta sequence.  This is not a numerical
diagnosis.  The fixed-point interval certificate `103_51` supplies rigorous
enclosures which imply

\[
 \boxed{\quad \Delta^2D_{147}<-{120357438\over10^{12}}<0.\quad}
\tag{2}
\]

Accordingly, the second-difference inequalities in `103_52`, (22)--(23),
and their Abel pole--prime formulation in `103_54` are eliminated as
possible all-index barriers.  Their identities remain correct and identify
the exact signed cancellation responsible for the failure.

The nearby *first* differences are rigorously positive.  Thus the natural
pivot is to a first-difference barrier, or to a weighted cumulative
curvature budget which permits negative \(\Delta^2D_n\).  Neither is proved
uniformly here.

## 1. Certified input

Put

\[
 M_n:=\lambda_n^{\rm prime}+{1\over2}\lambda_n^{\rm arch}={D_n\over2}.
\tag{3}
\]

The K850 execution in `103_51` uses outward integer fixed-point arithmetic
and gives the following decimal-prefix enclosures.  In integer units of
\(10^{-12}\), write the displayed lower and upper prefixes as

\[
\begin{array}{c|cc}
n&L_n&U_n\\ \hline
147&101725183742719&101725183750268\\
148&102542819846574&102542819854615\\
149&103360395755597&103360395764159.
\end{array}
\tag{4}
\]

The print convention of the verifier is a lower floor and an upper floor.
Consequently the certified real intervals are contained in

\[
 {L_n\over10^{12}}\le M_n\le {U_n+1\over10^{12}}.
\tag{5}
\]

No floating-point computation is used in (4)--(5): these are the prefixes
of the outward intervals produced by the Hasse/eta coefficient certificate
described in `103_51`.

## 2. Exact interval proof of negative curvature

The largest possible second difference compatible with (5) is obtained by
taking the two outer terms at their upper endpoints and the middle term at
its lower endpoint.  Hence

\[
\begin{aligned}
 10^{12}\Delta^2M_{147}
 &\le (U_{149}+1)-2L_{148}+(U_{147}+1)\\
 &=103360395764160-2\cdot102542819846574
     +101725183750269\\
 &=-60178719<0.
\end{aligned}
\tag{6}
\]

Since \(D_n=2M_n\), (6) proves (2).  In particular, no qualification such
as ``eventual except for a finite range'' is available for the proposed
convexity induction unless this certified index is explicitly excluded and
handled by a different, non-convex tail theorem.

## 3. What the same certificate says about the first difference

The correction is specifically about curvature, not monotonicity.  The
same certified intervals give

\[
\begin{aligned}
 10^{12}\Delta M_{147}
 &\ge L_{148}-(U_{147}+1)=817636096305>0,\\
 10^{12}\Delta M_{148}
 &\ge L_{149}-(U_{148}+1)=817575900981>0.
\end{aligned}
\tag{7}
\]

Thus \(\Delta D_{147}>0\) and \(\Delta D_{148}>0\), despite
\(\Delta^2D_{147}<0\): the slopes decrease slightly but remain positive.
This is exactly the behavior ruled out by (1) and allowed by a
first-difference or cumulative barrier.

## 4. Corrected discrete targets

The exact recurrence of `103_52` is still

\[
 D_n=nD_1+\sum_{m=1}^{n-1}(n-m)\Delta^2D_m.
\tag{8}
\]

It shows why convexity was sufficient, but it was unnecessarily strong.
Two valid alternatives are:

1. **First-difference induction.**  Prove
   \[
   \Delta D_n\ge0\quad(n\ge n_0),\qquad D_{n_0}\ge0.
   \tag{9}
   \]
   This permits \(\Delta^2D_n<0\).  In the Abel coordinate of `103_54`,
   (9) is the exact pole--prime inequality
   \[
   \mathcal I_n^{(1)}\le{1\over2}\Delta A_n-1,
   \tag{10}
   \]
   with \(\mathcal I_n^{(1)}\) defined by the combined Abel kernel in
   `103_54`, equation (9).  The two certified tests (7) do not disprove
   this target.  They do not prove it beyond those two indices.

2. **Cumulative-curvature budget.**  If one can produce numbers
   \(b_m\ge0\) with
   \[
   \Delta^2D_m\ge-b_m
   \tag{11}
   \]
   and prove, for each desired \(n\),
   \[
   \sum_{m=1}^{n-1}(n-m)b_m\le nD_1,
   \tag{12}
   \]
   then (8) gives \(D_n\ge0\).  This explicitly admits isolated or
   oscillatory negative curvatures.  It is a genuine sufficient
   formulation, not a claimed estimate: choosing \(b_m\) or bounding the
   weighted sum remains the unsolved arithmetic task.

Both targets, if made uniform and combined with finite certificates, would
be RH-strength because they imply the strong margin.  The certificate only
selects the correct shape of a possible discrete argument; it proves no
infinite theorem.

## 5. Required status correction

* `103_52`: equations for all differences and the Fejer recurrence remain
  valid; the all-positive-curvature barrier must be marked false.
* `103_54`: the Abel identity and the pole--prime collision remain valid;
  its convexity inequality is an exact **falsified criterion**, not an open
  barrier.
* The unresolved route is now (9), (10), or a nontrivial instance of
  (11)--(12), all of which must use cancellation in the actual prime-power
  weights rather than a sign of each Laguerre lobe.

## Status

The convexity ansatz is rigorously closed negatively at \(n=147\).  The
strong-margin sequence itself is positive throughout the certified finite
range; the local obstruction is only to a proposed mechanism for extending
that positivity.  A1 and RH remain open.
