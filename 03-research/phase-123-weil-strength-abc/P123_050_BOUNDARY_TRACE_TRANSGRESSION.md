# P123.050 — Source boundary traces and an explicit transgression identity

Date: 2026-09-05. Status: PROVED on the compact test crossed-product
algebras specified below. Extension to the full rapid topology and
comparison with the Weil relative character remain open.

## 1. A source test domain with convergent boundary integrals

Take S_f={p,q}. Use coefficients smooth and compactly supported in the
real logarithmic coordinate and Bruhat (locally constant, compactly
supported) in the two finite coordinates, with finitely many Gamma
labels. Let A_c be this crossed-product algebra on X^+, B_c the analogous
algebra C_c^infinity(R) crossed_alg Gamma on the double-zero set, and
I_c=ker(A_c -> B_c). The section s=chi_p chi_q of P123.049 preserves
these domains.

An element of I_c vanishes on a neighborhood of the double-zero set
within its compact support: the finite coordinates have a uniform
local-constancy level. Thus its restriction to either single-zero
stratum has compact support away from the remaining finite zero.

Define two functionals on I_c, with multiplicative Haar giving each
unit group measure one:

    tau_q(a)=integral_R integral_(Q_p^*)
                       a_1(t,x_p,0) d^*x_p dt,
    tau_p(a)=integral_R integral_(Q_q^*)
                       a_1(t,0,x_q) d^*x_q dt.   (1.1)

Here a_1 is the identity Gamma coefficient. These integrals are finite.
They vanish on the generic ideal, whose coefficients vanish on both
single-zero strata. They are traces, and more strongly

    tau_p([A_c,I_c])=tau_q([A_c,I_c])=0.          (1.2)

To prove this, expand the identity coefficient of a mixed product.
For each pair of inverse labels, change variables by the corresponding
Gamma dilation on the stratum. The measure dt d^*x is invariant; the
factor from I_c guarantees integrability. The reversed product has the
same integral. All label sums here are finite.

These are actual source traces with an explicit domain. They are not
being identified with the external-test distributions W_p and W_q.

## 2. Evaluate the attaching defect

Let gamma=p^m q^n and b=g U_gamma, c=h U_eta in B_c. The shell formula
of P123.049 gives zero trace unless eta=gamma^-1. In that case, put

    J(g,h;gamma)=integral_R g(t)h(t-log gamma)dt.

On the q-zero stratum, the missing p-adic shells have multiplicative
measure max(m,0). On the p-zero stratum the missing q-adic shells have
measure max(n,0). Consequently

    tau_q(omega(b,c))=-max(m,0) J(g,h;gamma),
    tau_p(omega(b,c))=-max(n,0) J(g,h;gamma).      (2.1)

Subtracting the reversed defect uses the same integral, by real
translation, and yields the bilinear functionals

    c_q(b,c)=tau_q(omega(b,c)-omega(c,b))
            =-m J(g,h;gamma),
    c_p(b,c)=tau_p(omega(b,c)-omega(c,b))
            =-n J(g,h;gamma).                   (2.2)

For noninverse labels both expressions are zero. Thus the layer
correction has now been evaluated in a source trace, not merely listed
as a formal element of the ideal.

## 3. Prove the cyclic identities on the quotient test algebra

Define the invariant quotient trace and label derivations on B_c by

    tau_B(b)=integral_R b_1(t)dt,
    delta_p(g U_(p^m q^n))=m g U_(p^m q^n),
    delta_q(g U_(p^m q^n))=n g U_(p^m q^n).

The label exponents add under multiplication, so both deltas are
derivations, and tau_B delta_p=tau_B delta_q=0. Equation (2.2) is
equivalently

    c_q(b,c)=-tau_B(delta_p(b)c),
    c_p(b,c)=-tau_B(delta_q(b)c).                 (3.1)

Trace cyclicity and tau_B delta=0 prove antisymmetry c(b,c)=-c(c,b).
Expanding the derivation of a product proves directly

    c(ab,c)-c(a,bc)+c(ca,b)=0,

where the repeated letter c in this display denotes the third algebra
argument when inside parentheses. More unambiguously, for arguments
x,y,z the identity is

    c(xy,z)-c(x,yz)+c(zx,y)=0.                   (3.2)

Hence these are cyclic 1-cocycles on B_c. They can be nonzero as
functionals: take inverse p labels and h(t)=g(t+log p) with real nonzero
g to get c_q=-integral g². Nonzero functional does not by itself prove
a nonzero cyclic-cohomology class.

## 4. A weighted Stokes identity in the real direction

Let a=log p, b=log q and delta_log=a delta_p+b delta_q. Multiplication
by t is a multiplier on the compact test domain, and crossed convolution
gives

    [t,g U_gamma]=(log gamma)g U_gamma.

Thus delta_log=[t,-]. Define the finite first-moment functional

    eta(z)=integral_R t z_1(t)dt.

A direct change of variables for inverse labels shows

    eta(xy-yx)=tau_B(delta_log(x)y).

Combining this identity with (3.1) gives the exact relation

    (log p)c_q(x,y)+(log q)c_p(x,y)
                   =-eta(xy-yx).                (4.1)

The weighted sum is therefore the negative Hochschild coboundary of
the real first-moment functional on this domain. This is a concrete
compatibility relation between the two boundary trace corrections and
the real translation direction. The coefficients correspond to the
valuation of the nonzero coordinate in each boundary integral; they
must not be silently relabelled as the orbit-volume factors of W_p.

## 5. What has and has not descended

The attaching defect now has genuine trace evaluations, cyclic identities
and the explicit relation (4.1). Since tau_p and tau_q vanish on the
generic ideal, their evaluation respects the difference between the two
chart decompositions in P123.049. Mixed centrality (1.2) also supplies
the lift-independence required there for relative degree-one boundaries.

These results concern the stated compact test domain. Neither integration
over a noncompact real axis nor its first moment is bounded by the
supremum coefficient seminorms of the full rapid C_0 algebra. We therefore
do not extend these traces or eta to that topology without an additional
integrability domain. Most importantly, the comparison identifying these
source trace operations with the regularized external character is still
needed; equations (2.2) and (4.1) do not establish it automatically.

This supplies explicit source transgression data for the next comparison,
without claiming full shadow excision, mixed RR or the D sign.
