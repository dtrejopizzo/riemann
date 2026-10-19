# R161_075 — Three different meanings of the completed zero product

## 1. The unsupported identification

R161_018 writes ZA_infinity=[Z,D_Gamma]=0 and uses it to exclude every linear PC graph limit. Commutativity of Z and D_Gamma proves [Z,D_Gamma]=0 on a common domain. It does not identify the product ZA_infinity with that commutator. That identification needs an independent definition of A_infinity, its carrier and the topology of the limit A_M -> A_infinity.

This is relevant because the finite operator A_M=M-(L_M+L_M*) is a nonzero Weil operator, whereas the functional equation also supplies a formally zero meromorphic symbol. They cannot be identified without checking their boundary interpretation.

## 2. L2 product: injectivity

Let Z be the maximal multiplication operator by z(tau)=zeta(1/2+i tau) in Fourier coordinates. Its domain consists of h in L2 with z h in L2. The zeros of z are isolated, so z is nonzero almost everywhere. Therefore

    h in Dom Z and Zh=0 => h=0.                 (2.1)

In particular, if Af is an L2 vector in Dom Z, then ZAf=0 implies Af=0. A universal such identity would make A vanish on the specified domain. Calling it a harmless zero commutator does not justify this consequence.

## 3. Distribution product: zero-supported data can survive

For a real zero gamma of z, ordinary smooth multiplication of distributions gives

    z(tau) delta_gamma=0.                       (3.1)

If the zero has multiplicity k, derivatives delta_gamma^(j) with j<k are also annihilated, by the distributional product rule. Thus ZW=0 in a distribution carrier need not imply W=0. Such a carrier is not L2, and its multiplication law does not license the Hilbert adjoints, norms or compressed-operator equations used for L2 vectors.

Equation (3.1) is only a local illustration at real zeros; it does not construct the full Weil distribution or represent off-line zeros.

## 4. Meromorphic identity: the formal Gamma–Euler symbol vanishes

Differentiating zeta(s)=chi(s)zeta(1-s) gives

    zeta'(s)/zeta(s)
      =chi'(s)/chi(s)-zeta'(1-s)/zeta(1-s).

With d_Gamma=-chi'/chi, the expression

    d_Gamma(s)+zeta'(s)/zeta(s)+zeta'(1-s)/zeta(1-s)

is identically zero as a meromorphic function. This is an algebraic statement, including cancellation of principal parts. It does not prove that the limit of two truncated prime translation operators on the critical line is the zero operator. The two Dirichlet series have disjoint initial convergence half-planes, and the contour/boundary prescriptions can carry residue contributions. Those prescriptions must be specified and justified before any operator limit is taken.

## 5. Consequence for the previous no-go

R161_018's claim that every linear PC graph limit equals a tautological zero operator is not established by its displayed argument. Its local algebraic split can be valid in a specified meromorphic interpretation without proving that the physical Weil form has the same interpretation. Conversely, an actual distributional zero product does not give an L2 zero product for free.

This does not prove that a linear PC construction closes D. It removes an overbroad exclusion. The next unresolved problem is to give compatible definitions and limits for:

    A_M f, S_N^ren A_M f, and the two separated product ports,

with one explicitly stated carrier for each. Any residue or exterior term lost in switching carriers must be retained. Strong convergence of S_N^ren alone is insufficient for convergence on the moving vector A_M f.

## Status

Proved: L2 injectivity (2.1), distributional counterexample (3.1), and the distinction from the meromorphic functional-equation identity. Not proved: a corrected physical graph-limit theorem or an annihilation of the first-contact detector. D remains open. No claim of independence or impossibility is made.
