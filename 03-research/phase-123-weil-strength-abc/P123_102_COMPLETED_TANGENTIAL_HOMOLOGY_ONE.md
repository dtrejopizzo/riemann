# P123.102 — Exact degree-one diagonal homology in the nuclear completion

Date: 2026-09-06. Status: PROVED-IN-REPOSITORY in degrees zero and
one for S=S(Y) of P123.101. An explicit continuous linear filling proves
the degree-one boundary image closed. Higher degrees remain uncomputed.

Use normalized completed Hochschild chains
C_n=S tensorhat_pi (S/C1)^(tensorhat_pi n), with the usual boundary.
The scalar quotient drops the trivial Fourier character. These are
explicit weighted Fourier spaces by P123.101. We work directly with
this normalized complex; no comparison with another exact structure
is implicit. Since S is commutative, d_1=0 and H_0=S.

## 1. Tangential map and a continuous section

Let D=partial_t and put tau_0=2pi/(log q), chi_0(t,u)=exp(i tau_0 t).
Define

    pi_1(m tensor [b])=m D b,
    u_chi=chi^-1 tensor [chi],
    s_1(h)=(h/(i tau_0)) u_(chi_0).                         (1)

Continuity follows from the product and derivative estimates of P123.101.
Leibniz gives pi_1 d_2=0, and pi_1 s_1=identity. Thus at least one
complete tangential S-module survives in H_1. We now prove it is all
of H_1, not just a split submodule.

## 2. Explicit character relations with fillings

For characters alpha,beta set

    B_(alpha,beta)=(alpha beta)^-1 tensor [alpha] tensor [beta].

Expanding the degree-two boundary gives

    d_2 B_(alpha,beta)=u_beta-u_(alpha beta)+u_alpha.         (2)

Here u_1=0 in normalized chains. For d>=1 put
P_d(chi)=sum_(r=1)^(d-1) B_(chi^r,chi), so
d_2 P_d(chi)=d u_chi-u_(chi^d).

Define Q_k with d_2 Q_k=k u_(chi_0)-u_(chi_0^k) for all integers k:
for k>=1 take P_k(chi_0), for k=0 take zero, and for k=-l<0 take

    Q_(-l)=P_l(chi_0^-1)-l B_(chi_0,chi_0^-1).

Let chi=(tau,kappa) and let d be the order of kappa. Then d<=c(kappa)
and (1) of P123.101 gives chi^d=chi_0^k for the integer
k=d tau/tau_0. Consequently

    F_chi=(P_d(chi)-Q_k)/d,
    d_2 F_chi=u_chi-(tau/tau_0)u_(chi_0).                   (3)

This also handles nontrivial characters with tau=0: their finite-order
class has an explicit filling, rather than being discarded by an
unjustified division by the real frequency.

## 3. Conductor estimates permit completion

We have d<=W(chi) and |k|<=C W(chi). For 1<=r<=d,

    W(chi^r)<=(1+r|tau|)c(kappa)<=C W(chi)^2.

Every character power of chi_0 appearing in Q_k has weight at most
C W(chi). Therefore, in the degree-two projective seminorm with weight
exponent m on each factor, equations (2)–(3) imply the deliberately
non-sharp bound

    ||F_chi||_(m,2)<=C_m W(chi)^(5m+2).                    (4)

Indeed each P_d term has weights bounded by W(chi)^(2m),
W(chi)^(2m), W(chi)^m, and there are at most W(chi) terms; the Q_k
terms have polynomially smaller bounds, including the coefficient l.
Dividing by d cannot increase these bounds.

For a Fourier basis tensor eta tensor [chi] define

    H_1(eta tensor [chi])=eta chi F_chi,                     (5)

where multiplication acts on the first factor. Submultiplicativity of
W and (4) bound its output by
C_m W(eta)^m W(chi)^(6m+2). Choosing input exponent 6m+2 in both
variables proves that (5) extends to a continuous linear map
H_1:C_1->C_2 on the completed Fourier spaces. No uncontrolled passage
from finite unit levels is used.

Since eta tensor [chi]=eta chi u_chi, equation (3) gives on the dense
Fourier tensors, and hence on all C_1,

    d_2 H_1=identity-s_1 pi_1.                              (6)

## 4. Exact homology and finite-level compatibility

The inclusion im d_2 subset ker pi_1 follows from Leibniz. Conversely
if pi_1(z)=0, equation (6) gives z=d_2 H_1(z). Hence

    im d_2=ker pi_1,
    H_1(C_*) is topologically S dt.                         (7)

The image is closed, and H_1 restricted to ker pi_1 is a continuous
linear right inverse to d_2 onto that image. The quotient identification
uses the continuous section s_1. We identify the output h of pi_1 with
h dt, so this is the physical tangential coordinate of P123.099.

The map pi_1 commutes with inclusions of all finite unit levels: it is
the same derivative D and multiplication on each level. All characters
and powers used in a filling F_chi stay at the level of kappa (chi_0
has trivial unit character). Thus the formula is also compatible with
the finite-level domains. Its polynomial estimates are what permit
the common completion, beyond the earlier homology-only statements.

This proves that the nuclear smooth completion retains precisely the
tangential excess in degree one, unlike the continuous C(Y) topology
of P123.097. It does not prove vanishing of H_n for n>=2, a full finite
perfect diagonal representative, convergence of moving determinant
families, or the normal/arithmetic mixed RR. Those remain obligations.
