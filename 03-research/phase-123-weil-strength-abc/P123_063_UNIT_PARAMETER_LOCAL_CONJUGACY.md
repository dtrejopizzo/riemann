# P123.063 — Include the original power map in the local trace conjugacy

Date: 2026-09-06. Status: PROVED on the fixed smaller ball specified below.
This removes the parameter restriction excluding t=1 in P123.062, not
the restriction to a neighborhood of the identity.

Fix a>=1 for odd p and a>=2 for p=2, and put B=p^a Z_p. For every
t in Z_p define H_t(z)=log(1+tz)/t on B, with H_0(z)=z. Writing
z=p^a w gives

    H_t(p^a w)=p^a H_(t p^a)(w).

The parameter t p^a satisfies P123.062 uniformly for all t in Z_p.
Consequently H_t is a bijective Haar-preserving isometry B -> B and

    H_t(F_n(t,z))=n H_t(z),  n>=1.

These identities now include t=1 and F_n(1,z)=(1+z)^n-1, the original
power map in the identity coordinate. The ball B is independent of t
and n, and every F_n maps it into itself. The half-density pushforward
operators on L²(B) are therefore conjugate to dilation isometries by
the same U_t for all arithmetic n. Composition and adjoints are
transported exactly as in P123.062.

For N>=a let E_(a,N) project onto functions on B constant modulo p^N.
It is the position/Fourier projection with position p^a Z_p and frequency
p^-N Z_p, of rank p^(N-a). Since H_t permutes its equal-measure cells,
U_t commutes with E_(a,N). Thus for every t in Z_p,

    Tr(E_(a,N) V_t,n E_(a,N))
      = |n|_p^(1/2) min(p^(N-a), |1-n|_p^-1).

The formula follows either by rescaling to Z_p or by P123.042 with
M=-a. In particular at n=p^k, k>=1, this trace is p^-k/2 at both t=0
and t=1, for all N>=a. This is a local trace comparison between the
actual power map and its normal dilation, not only between parameters
near zero.

The primitive unit contact remains the complex of P123.061 under both
specializations. However shrinking the analytic neighborhood loses
information about primitive points outside 1+B; it does not transport
their global finite-orbit determinant. The analytic logarithm also
does not detect integral vertical torsion. Hence this local conjugacy
must not be promoted to the missing mixed RR or a global power-map
trace identity. Those comparisons remain necessary for B/C.
