# P123.052 — External action and gauge multipliers on the integrable source

Date: 2026-09-05. Status: PROVED for the two-prime integrable domain of
P123.051. This supplies an A/C compatibility, not all of row A.

## 1. Normalized external action preserves the new domain

For S_f={p,q}, a normalized external element is h=(s,u_p,u_q) in
H_S=R times Z_p^* times Z_q^*. Its coefficient action is

    beta_h f(t,x_p,x_q)=f(t-s,u_p^-1 x_p,u_q^-1 x_q).

It fixes Gamma labels. Boundary multiplicative measures are invariant,
and the real moment weights satisfy

    (1+|t+s|)^d <= (1+|s|)^d(1+|t|)^d.

Thus the I_kd and B_kd seminorms of P123.051 increase by at most
(1+|s|)^d. The cutoff chi=1_Zp 1_Zq is invariant under both unit
coordinates. Consequently beta_h s_section=s_section beta_h on the
quotient, where s_section denotes the linear extension, and

    beta_h omega(b,c)=omega(beta_h b,beta_h c).

It follows from the explicit product on I_int plus B_int that beta_h
is a continuous star automorphism of A_int. Its inverse is beta_(h^-1).
The action is strongly continuous: on dense compact tests this follows
from real translation continuity and finite-coordinate local constancy;
the displayed locally uniform bounds extend it to the completion.

## 2. Integrated action on the same completed source

For a smooth compact-real, finite-unit-level external test f define

    Theta(f)a=integral_(H_S) f(h) beta_h(a) dh.

The strong continuous integrand and compact support define the integral
in each of the complete Fréchet spaces I_int, B_int and A_int. With
the direct-sum graph seminorm A_kd on A_int,

    A_kd(Theta(f)a)
       <= A_kd(a) integral |f(s,u)|(1+|s|)^d ds du.

Fubini and beta_h beta_k=beta_hk give

    Theta(f*g)=Theta(f)Theta(g).

Restriction, inclusion and the linear section of the integrable source
extension intertwine this action. Theta(f) is an integrated linear
operator; it is not itself asserted to be an algebra automorphism or
a Hilbert trace-class operator.

## 3. Gauge labels act as continuous multipliers

The unitaries U_gamma of the original repaired unital algebra need not
belong to A_int, which has C_0 coefficients, but their left and right
multiplications preserve A_int continuously. For a=i+s_section(b),

    U_gamma a
      = U_gamma i
        +(alpha_gamma(chi)-chi) alpha_gamma(b) U_gamma
        +s_section(U_gamma b).                  (3.1)

In (3.1), the notation alpha_gamma(b) U_gamma includes the shift of every
label of b by gamma. The middle term is in I_int: its restriction to
the double-zero set is zero. On each boundary its absolute shell measure
is bounded by |v_p(gamma)|+|v_q(gamma)|, and its real translation has
the moment bound of P123.051. These estimates give continuity for every
fixed gamma, and bounds growing at most as a power of H(gamma) at each
fixed graph seminorm. Left multiplication of i has the same translation
bound. On the right,

    a U_gamma=i U_gamma+s_section(b U_gamma),

so only the rapid label weight changes. The inverse multipliers are
U_(gamma^-1), and their products obey the original Gamma group law.

Hence Ad(U_gamma) is a continuous star automorphism of A_int. Combining
this with normalized beta_h extends the action to unnormalized external
lifts and retains the exact identity

    beta_(gamma h)=Ad(U_gamma) beta_h.           (3.2)

This proves preservation of the integrability domain under changes of
lift. It does not insert U_gamma as an element of the nonunital A_int.

## 4. Trace covariance and the real first moment

The source boundary traces tau_p,tau_q are invariant under beta_h by
invariance of dt d^*x. The quotient trace tau_B is also invariant.
The first-moment functional transforms by the explicit formula

    eta(beta_h b)=eta(b)+s tau_B(b).              (4.1)

This follows by t -> t+s in its absolutely convergent integral.
Since tau_B annihilates commutators, the coboundary eta(xy-yx) is
invariant. Thus the transgression identity of P123.050–051 is compatible
with the external action, despite eta itself having a translation term.
All statements hold on the completion by its defining integrability
and the estimates above.

## 5. Remaining categorical requirements

The integrable trace domain is now stable under external action and
gauge multipliers, with an integrated convolution action and compatible
source transgression. It is therefore not an unrelated trace-only
completion. Nevertheless the unital bimodule tensor theorem of P123.019
cannot be transferred to this nonunital algebra just by replacing its
name: its required unital enlargement or multiplier-module formulation
must be specified and proved. Semilocal changes of S and the integral
contact comparison also remain necessary. No full A, B or C closure
is asserted by these fixed-S action estimates.
