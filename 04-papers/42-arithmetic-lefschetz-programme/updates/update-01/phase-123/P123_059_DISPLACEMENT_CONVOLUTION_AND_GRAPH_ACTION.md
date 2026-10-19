# P123.059 — Displacement convolution and the local graph action

Status: PROVED for the local test algebra, its
involution, graph representation and relative character. This does not
construct the global mixed correspondence category or integral contact.

## 1. Composition in displacement coordinates

Let V=Q_p\{1}, with displacement y=1-x for x in Q_p^*. Multiplication
of x parameters becomes

    y odot z=y+z-yz,
    identity=0,  y^(-1)=-y/(1-y).

These formulas follow from 1-(1-y)(1-z). Thus they are the actual law
for composing the normal graphs v -> (1-y)v. Its Haar measure, using
multiplicative unit volume log p, is

    dnu(y)=log p/(1-p^-1) dy/|1-y|_p.

Let D(V) denote additive Bruhat tests compactly supported away from 1.
Transport the multiplicative test algebra through the bijection

    L(a)(y)=|1-y|_p^-1/2 a(1-y),
    L^-1(phi)(x)=|x|_p^1/2 phi(1-x).

A direct substitution gives its product

    (phi star psi)(y)
       =integral_V phi(z) psi((y-z)/(1-z)) dnu(z). (1.1)

Indeed the half-density factors in a(x)b((1-y)/x) multiply to
|1-y|_p^1/2 and cancel the prefactor in L. The integral stays in D(V)
because it is convolution on the group (V,odot) of compact tests.
Associativity therefore follows also directly from the group law and
Haar Fubini. This is not pointwise multiplication in E_p.

## 2. The correct involution retains the half-density twist

The multiplicative involution is a*(x)=overline(a(x^-1)). Its transported
involution is

    phi^sharp(y)=|1-y|_p^-1
                   overline(phi(-y/(1-y))).      (2.1)

Substituting L^-1 proves the formula, including the factor |1-y|^-1.
Hence sharp squares to identity and reverses (1.1). Dropping this
factor would instead give the ordinary group-convolution involution,
which is not the one transported by this particular half-density map.

Thus L is an exact star-algebra isomorphism between multiplicative
Bruhat convolution and (D(V),star,sharp), with the stated Haar choice.
Its inclusion as a vector space in E_p is continuous on each fixed
compact-support/local-constancy test stage. Closure of star on the
whole Banach E_p is not asserted.

## 3. Actual graph representation

On L²(Q_p) let D_x v(t)=|x|_p^-1/2 v(t/x). Define

    Pi(phi)=integral_(Q_p^*) |x|_p^1/2 phi(1-x) D_x d^*x.

This is the integrated action of the actual normal graph maps. Its
norm is bounded by the L¹ norm of L^-1(phi). Since D_x D_z=D_xz and
D_x*=D_(x^-1),

    Pi(phi star psi)=Pi(phi)Pi(psi),
    Pi(phi^sharp)=Pi(phi)*.                      (3.1)

At the unintegrated level the graph kernels compose by the same
displacement law y odot z; their half-density factors multiply because
|xz|^1/2=|x|^1/2|z|^1/2. Thus the transported product is tied to an
explicit graph action, not chosen merely to match a scalar trace.

## 4. Relative character on this composable local algebra

Let E_MN be the finite-rank normal cutoff of P123.042 and L_0=M+N.
Applying that note and P123.058 to a=L^-1(phi) gives, once L_0 is beyond
the relevant unit level,

    Tr(E_MN Pi(phi))-(L_0+1)(log p)phi(0)
       =(log p)R_p(phi)+log p/(p-1)phi(0).        (4.1)

The source-side functional on the right is therefore the relative
character of a representation preserving the local graph composition
and its correct involution. The cutoff assignment itself is not a
representation. Equation (4.1) uses local multiplicative Haar with unit
mass log p; no second tangential log p factor should be inserted.

This addresses the local composition question left by P123.058. It
does not identify the star product (1.1) with the pointwise coefficient
product of E_p, or restriction of external tests with a homomorphism.
For the full external group, P123.043 still supplies induction; its
compatibility with the global source shadow is a further comparison.

## 5. Remaining global and integral obligations

The displacement operation now has an explicit composition law,
involution, graph representation and relative trace. To obtain the
common shadow it must be realized by the graph/diagonal operation of
the repaired source category, respecting the layer attaching maps and
the integral primitive contact. A local convolution algebra is not by
itself that mixed source category. Archimedean localization, global RR
and the D sign remain unresolved.
