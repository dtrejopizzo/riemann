# Heat-flow Newman gate audit

## Purpose

The Fourier and Jensen gates point to another classical deformation: the
heat-flow family associated to the completed function.  This document states
what that route would need in order to close A1 and separates it from the
known forward real-rootedness phenomenon.

## Heat-flow family

Let
\[
  H_t(z)=\int_0^\infty e^{t u^2}\Phi(u)\cos(zu)\,du,
\]
where \(\Phi\) is the even theta-derived kernel for \(\Xi\).  With the
standard normalization,
\[
  H_0(z)=\Xi(z).
\]

The parameter \(t\) is the heat-flow time in Fourier variables.  Multiplying
the Fourier kernel by \(e^{t u^2}\) corresponds to evolving the entire
function by a heat-type equation in the \(z\)-variable, with the sign
convention fixed by the displayed formula.

## Closing theorem

The heat-flow route closes A1 if it proves
\[
  H_0=\Xi
  \quad\hbox{has only real zeros}.
\tag{1}
\]

Equivalently, it may prove a stronger theorem:
\[
  H_t\hbox{ has only real zeros for every }t\ge0.
\tag{2}
\]

Then \(\Xi\) belongs to the Laguerre--Pólya class, Li positivity follows, and
A1 follows through the phase-102 assembly.

## What the forward theorem does not give

A theorem of the form
\[
  H_t\hbox{ has only real zeros for all sufficiently large }t
\tag{3}
\]
does not imply (1).  Real-rootedness can be created by forward heat flow.
To close A1 one needs to push the real-rootedness threshold down to
\[
  t=0.
\]

Thus the following implication is not valid:
\[
  \hbox{eventual real-rootedness under heat flow}
  \Longrightarrow
  \hbox{RH}.
\]

The missing input is a backward-in-time preservation theorem or an exact
threshold bound placing the real-rootedness threshold at or below zero.

## Newman-threshold formulation

Equivalently, define a threshold \(\Lambda\) such that the heat-flow member
has only real zeros exactly for
\[
  t\ge\Lambda.
\]

Then the heat-flow route closes A1 exactly if it proves
\[
  \Lambda\le0.
\tag{4}
\]

Any result proving only
\[
  \Lambda\le c
\]
with \(c>0\) leaves a gap between \(0\) and \(c\).  That gap is precisely the
RH/A1 obstruction in heat-flow coordinates.

Similarly, a lower bound
\[
  \Lambda\ge0
\]
shows sharpness of the problem but does not prove A1.  Together with (4) it
would locate the threshold at zero, but (4) remains the required closing
inequality.

## Relation to Jensen and total positivity

The heat-flow route is a deformation version of the Laguerre--Pólya gate:

\[
  \Lambda\le0
  \Longrightarrow
  H_0=\Xi\in{\rm LP}
  \Longrightarrow
  \lambda_n\ge0
  \Longrightarrow
  A1.
\]

Jensen cofinal hyperbolicity is another route to the same middle statement
\[
  \Xi\in{\rm LP}.
\]

The two routes differ in method, not in final load.  Both must prove the
critical time or cofinal limit directly from Euler--Gamma data.

## Eliminated class

The following proof pattern is eliminated:

1. prove real-rootedness of \(H_t\) for large positive \(t\);
2. use continuity of zeros as \(t\downarrow0\);
3. infer real-rootedness of \(H_0\).

Step 2 is invalid without excluding zero collisions and departures from the
real axis in the interval down to \(0\).  That exclusion is exactly the
threshold theorem \(\Lambda\le0\).

## Viable theorem

The heat-flow gate remains viable only as:

Prove from Euler--Gamma data that the real-rootedness threshold of the
heat-flow deformation satisfies
\[
  \Lambda\le0.
\]

This is an RH-strength theorem.  If proved independently, it closes Omega7.

## Status

Closed as an audit of the heat-flow route.  Eventual real-rootedness and
positive-time bounds do not close A1.  The exact live target is the
threshold inequality \(\Lambda\le0\).
