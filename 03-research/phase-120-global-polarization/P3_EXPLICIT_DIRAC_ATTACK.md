# The explicit-Dirac attack on row (d)

Status: this note fixes the non-circular closure criterion. The local
conservative pieces do **not** yet define the required global operator.

## 1. The only acceptable factorization

On the primitive core put

    P_T = ker M_- intersect ker M_+ = L_0 C_c^infinity(I_T),
    L_0 = -d^2/dt^2+1/4.

The independently constructed incoming and outgoing maps are

    X_T F = (W_Gamma F, sqrt(theta_T)F, E_+ z(F)),
    Y_T F = (sqrt(m_0)F, E_- z(F), deg z(F)),

with `z_p(F)=O_pF`. Their Gram difference is already known term by term:

    X_T^*X_T-Y_T^*Y_T=-B_nuc,T.                    (1)

Equation (1) is not positivity. An admissible closure must construct a
closed differential

    D_T : Dom(D_T) -> H_bulk,T                     (2)

from the quarter-twisted phase, the Frobenius transmission maps and the
two Tate boundary conditions, before (1) is used, and prove on
`G in C_c^infinity(I_T)` that

    D_T^*D_T = L_0 (X_T^*X_T-Y_T^*Y_T) L_0.        (3)

Then, for `F=L_0G`,

    -B_nuc,T(F,F)=||D_TG||^2.                      (4)

The formal choice

    D_T=(L_0(X_T^*X_T-Y_T^*Y_T)L_0)^(1/2)

is forbidden: its existence is equivalent to row (d).

## 2. Why D.247 plus local dilations does not yet give D_T

D.247 constructs an isometry

    U_S : closure(Ran I_S) -> closure(Ran O_S),
    U_S I_S z = O_S z.                             (5)

It does not prescribe a unitary map between the orthogonal defect
complements. A unitary dilation has the form

    U_S direct-sum V : Ran(I_S) direct-sum D_in
                       -> Ran(O_S) direct-sum D_out, (6)

where `V:D_in->D_out` is additional data. D.247's phrase "adjoining the
two defect complements gives a unitary dilation" proves existence, not a
canonical choice of `V`.

This distinction becomes load-bearing in the global attachment. The Gamma
and Tate ports have components in those defect complements. Changing `V`
changes their Redheffer feedback and hence changes the outgoing Gram. The
common half-density dilation of the contractions `C_p` fixes the orbit
states, but it does not identify the tangent defect complements in (6) with
the quarter-twisted Gamma boundary space. Therefore the composition

    "D.247 unitary dilation + Gamma dilation + Tate short"

is not yet a defined operator. Treating it as canonical would insert the
missing global polarization as an unrecorded choice.

## 3. The geometric datum that would close the gap

There is exactly one admissible way to supply the missing action: define a
single first-order Dirac operator on a specified glued object. A complete
definition must give, without reference to `B_nuc`, all of:

1. a bulk Hilbert space `H_bulk,T`;
2. a first-order differential `d_(1/4)+delta_Frob` and its closed domain;
3. trace maps onto the D.247 odd/even, degree/contact and Gamma ports;
4. transmission conditions at the common phase boundary;
5. the two exterior conditions `M_-=M_+=0`;
6. an orientation for which the Green boundary form is exactly
   `||X_TF||^2-||Y_TF||^2`.

Once these six objects are explicit, integration by parts has a binary
outcome:

    ||X_TL_0G||^2-||Y_TL_0G||^2
      = ||(d_(1/4)+delta_Frob)u_G||^2 + M_T(G).     (7)

If the transmission law gives `M_T=0`, define `D_TG` to be the displayed
bulk differential and (3) is proved. If `M_T` is nonzero or indefinite,
this route fails. It is not permissible to absorb `M_T` into a newly
defined metric.

## 4. Current verdict

The quarter twist, Gamma Markov energy, physical Frobenius weights, place
Poisson observations, common orbit dilation, compact polar potential and
D.247 four-port conservation are explicit. Items 1--4 of Section 3 for a
**single glued Dirac domain** are not. Consequently the global Green
identity is not one routine lemma away and no operator `D_T` has yet been
constructed.

The next proof object is not another inequality or finite test. It is the
domain-and-trace definition in Section 3 followed immediately by the
boundary calculation (7). No claim that row (d) is closed is allowed before
that calculation yields `M_T=0`.

## 5. The defect complements are explicit Frobenius boundary traces

The first missing part of the domain can in fact be computed. Put
`a=log p`, let `V_aF(t)=F(t-a)`, and

    O_pF=sqrt(1-exp(-a)) sum_(j>=0) exp(-ja/2)V_(ja)F.

For `F` compactly supported and `0<=r<a`, the following limit stabilizes
after finitely many terms:

    T_pF(r)
      := lim_(k->infinity) exp((r+ka)/2)O_pF(r+ka)
       = sqrt(1-exp(-a))
         sum_(ell in Z) exp((r+ell a)/2)F(r+ell a). (8)

The right side is a smooth function on `R/aZ`. Indeed replacing `r` by
`r+a` and shifting `ell` leaves the sum unchanged. Moreover

    integral_0^a T_pF(r)dr
      = sqrt(1-exp(-a)) M_+(F).                    (9)

Consequently the Tate condition `M_+(F)=0` kills only the constant Fourier
mode of `T_pF`; it does not kill the trace. The surviving canonical defect
space is

    H_p^bd = L^2_0(R/(log p)Z).                    (10)

The adjoint Frobenius orientation gives the analogous incoming trace at the
opposite end. Thus the complement map left unspecified in (6) is not an
abstract auxiliary choice: it must act on the direct sum of the spaces
`H_p^bd`, with D.247's coherent degree line separated from their mean-zero
parts.

Equations (8)--(10) also locate the error in any claim that algebraic
acyclicity leaves only two analytic boundary modes. The two Tate modes are
the constant resonances; every Frobenius cylinder contributes a mean-zero
periodic boundary trace. A valid global Dirac construction must retain and
pair these traces, not quotient them away.

This fixes the next concrete map to construct:

    U_bd : direct-sum_p H_p^bd direct-sum H_Gamma^bd
             -> direct-sum_p H_p^bd direct-sum H_Gamma^bd, (11)

induced by the common absolute boundary and compatible with D.247. Once
`U_bd` is specified geometrically, not by Gram matching, it supplies the
previously missing transmission law in Section 3 and Green's calculation
(7) becomes literal.

## 6. Canonical Bohr assembly of all prime defect boundaries

The prime part of (11) has a canonical common ambient space. Let `B^2_ap(R)`
be the Besicovitch Hilbert space, with mean inner product

    <f,g>_B = lim_(R->infinity) (1/(2R))
                integral_(-R)^R f(t) conjugate(g(t))dt.

A periodic function of period `a_p=log p`, equipped with normalized Haar
measure `dr/a_p`, embeds isometrically without an additional scalar. Its
Fourier frequencies are

    L_p^* = (2 pi/log p) Z.

If `p!=q`, then `L_p^* intersect L_q^*={0}`. Indeed a nonzero common
frequency would give

    k/log p = ell/log q,

and hence `p^ell=q^k`, impossible for distinct primes. Characters with
different frequencies are orthogonal for the Bohr mean. It follows that

    closure_B(sum_p L^2(R/(log p)Z))
       = C 1 direct-sum (direct-sum_p L^2_0(R/(log p)Z)). (12)

Thus all local constant modes are one and the same global line, while all
mean-zero Frobenius traces are canonically orthogonal. Formula (12) is the
boundary realization of D.247's rank-one degree/contact splitting; it is
not a chosen unitary extension.

For the trace (8), the normalized Fourier coefficients are explicitly

    Fourier(T_pF)(k)
      = sqrt(1-p^(-1))/(log p)
        integral_R e^(t/2)F(t)
          exp(-2 pi i k t/log p)dt.                (13)

The coefficient `k=0` is the Tate mode in (9). Equations (12)--(13)
therefore construct the entire arithmetic resonant boundary and its
coherent degree line directly from the Frobenius semigroup.

What remains in (11) is no longer an arbitrary prime-complement map. The
mean-zero prime summands carry their canonical orthogonal metric; the only
nonlocal transmission to construct is the attachment of the coherent
degree profile to the quarter-twisted Gamma boundary. This is precisely the
place where the adelic product formula, rather than a choice of defect
unitary, must enter.

## 7. The Real involution closes the nonpolar prime boundary

The adjoint return resolvent has the opposite stabilized trace

    T_p^-F(r)=sqrt(1-p^(-1)) sum_(ell in Z)
                exp(-(r+ell log p)/2)F(r+ell log p), (14)

whereas (8) is denoted `T_p^+`. Their constant coefficients are fixed
multiples of `M_-(F)` and `M_+(F)`, respectively. Let

    F^sharp(t)=conjugate(F(-t)),
    (J_p h)(r)=conjugate(h(-r)).                    (15)

Here `J_p` is the canonical Real antiunitary of the periodic orbit. A direct
change `ell -> -ell` gives

    T_p^-(F^sharp)=J_p T_p^+(F).                    (16)

In particular, on the Real test core `F^sharp=F`,

    ||T_p^-F||=||T_p^+F||.                          (17)

The maps `J_p` assemble under (12) to the Real antiunitary `J_B` of the
Bohr boundary; they fix the common constant line and preserve every
mean-zero prime summand. Thus the complete incoming and outgoing nonpolar
Frobenius boundary states have equal norm. They need not vanish, but their
difference contributes no boundary/Maslov remainder.

For the Poisson-resolvent traces (8) and (14), this resolves the nonpolar
state ambiguity left by a merely bilateral unitary dilation: the missing
identification is the pre-existing Real Tate involution, not a freely
selected map. It does not by itself identify these traces with every state
coordinate in the older Fourier--Poisson landing models. Positivity of the
interior contact defect is still carried by D.247; equation (17) proves
exactly that no extra periodic resolvent energy is lost at infinity.
