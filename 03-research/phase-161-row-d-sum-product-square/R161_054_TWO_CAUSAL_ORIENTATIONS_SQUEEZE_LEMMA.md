# R161_054 — Two causal orientations and the unitary squeeze mechanism

> **SCOPE CORRECTION (R161_056).** The abstract flux and squeeze lemmas are valid. Their proposed application to the covariant tangent of `theta_N` does not reach the critical jet: that tangent has the mean orientation. Thus the finite PC application in Sections 3--4 remains only an acceptance proposal and currently lacks the required common-port reverse identification.

## 1. Three-block flux identity

Let

    H=H_L direct_sum H_0 direct_sum H_R

with orthogonal projections P_L,P_0,P_R, and let U be unitary. For x in H put y=Ux. Then

    ||y_R||^2-||x_R||^2
      =||x_L||^2-||y_L||^2
       +||x_0||^2-||y_0||^2.                         (1.1)

This is just ||y||=||x|| with the three blocks separated. It is the finite conservative Green identity of the Poisson colligation.

If the corrected central blocks have equal norm,

    ||x_0||=||y_0||,                                  (1.2)

then

    ||y_R||^2-||x_R||^2=||x_L||^2-||y_L||^2.          (1.3)

One causal orientation with x_L=0 gives

    ||y_R||^2-||x_R||^2=-||y_L||^2<=0.                (1.4)

The reflected/Fourier orientation, applied to the same corrected physical port with input and output reversed, gives

    ||y_R||^2-||x_R||^2=+||x_L^opp||^2>=0.            (1.5)

If (1.4) and (1.5) concern the same scalar norm difference, both sides vanish. This is the two-orientation squeeze:

    ||y_R||=||x_R||,
    y_L=0,
    x_L^opp=0.                                        (1.6)

When the right compression is y_R=lambda x_R with |lambda|=1, unitary compression rigidity then gives the full scattering equation. Equivalently, in the canonical Hardy deformation the two inequalities give both signs of the norm slope and force the Gamma/Sonin excess to zero.

## 2. Why using the same central block is load-bearing

Two unrelated causal realizations always give two inequalities, but they compare different norms and cannot be squeezed. The role of finite Poisson is to identify their undifferentiated histories:

    Z_N Fcal=Z_N^*J+E_N.                               (2.1)

The role of covariant differentiation is to compare their tangents without differentiating the source. The role of Lambda*1=log and PC-ren is to express that tangent through the same finite Euler data. The role of the polar/Tate calculation is to make (1.2) true after compression: it must show that the two central norm changes differ exactly by crossed endpoint terms which cancel on a parity first-contact state.

Without (1.2), (1.1) contains the uncontrolled scalar

    Delta_0=||x_0||^2-||y_0||^2.                       (2.2)

Assigning Delta_0=0 from the completed commutator is invalid: the commutator gives a central amplitude equation, while (2.2) is a difference of finite metrics. The equality must be obtained before the graph limit, with the polar layer retained.

## 3. Application to the finite Poisson multiplier

Take U=U_N=M_(theta_N) from R161_052 and x=x_N(F) from R161_053. Then y=U_Nx is the Fourier-oriented history, and

    y-x=(E_N^ren F)^hat.                                (3.1)

The three blocks are the left exterior, physical window, and right exterior Hardy/support pieces. Equation (1.1) is exact for every finite N. No limiting support assertion is needed.

After covariant differentiation, the metric tangent is the real phase current

    q_N=(1/i)theta_N'/theta_N,                         (3.2)

whose division-free form contains the two coherent K_N^ren orientations and the Gamma connection. Substitution K_N=L_MS_N-H_(M,N) brings in Lambda*1=log. Thus the derivative of (1.1) is the natural quadratic carrier for PC-ren.

## 4. Exact finite acceptance statement

Let the superscripts plus/minus denote the two causal realizations before Poisson recombination, and let C_N^Tate(F) denote the canonical finite polar/crossed-Tate endpoint vector fixed by R161_009. A closing calculation must prove:

1. the corrected central metric identity

       Delta_(0,N)^plus(F)-Delta_(0,N)^minus(F)
          =2 Re <C_N^Tate(F), endpoint_N(F)>;            (4.1)

2. on a parity first-contact state, the right side of (4.1) is exactly the difference of the two Tate norm changes, so the fully corrected central metrics agree;
3. the right exterior norms in the two orientations are the same canonical product-port norms N_T(0) and N_T(delta), in reversed order;
4. all graph remainders are o(delta) uniformly in the finite cutoff needed before N tends to infinity.

Then the plus orientation gives N_T(0)-N_T(delta)>=0 and the minus orientation gives N_T(delta)-N_T(0)>=0. Hence equality holds, R161_015 gives

    E_T^PC(F)=0,

and the proved critical/Gamma rigidity closes D.

## 5. Status

- exact three-block unitary flux identity: proved;
- abstract two-orientation squeeze: proved;
- identification of the two finite histories by Poisson and of their covariant tangent by PC: proved from R161_052-R161_053;
- central metric equality after polar/crossed-Tate correction (4.1): open;
- common-port and uniform graph identifications in items 3-4: open;
- D: open.

The remaining calculation is now a finite metric identity, not an assertion that a central amplitude equation equals an exterior projection.
