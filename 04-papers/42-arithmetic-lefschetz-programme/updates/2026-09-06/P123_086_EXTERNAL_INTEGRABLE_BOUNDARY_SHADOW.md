# P123.086 — External boundary shadows on the integrable module sector

Date: 2026-09-06. Status: PROVED-IN-REPOSITORY at each fixed external
parameter on the two-prime carrier of P123.085. Parameterwise traces
are not asserted to constitute a distributional character.

## 1. Twisted localization on the integrable domains

For a positive-real external idele a, beta_a(x)(z)=x(a^-1 z)
maps J_V continuously to J_(aV). Indeed both boundary measures are
invariant under external dilation, and the real moment changes by at
most (1+|log a_infinity|)^d. Label weights are unchanged. The inverse
is beta_(a^-1). Define F_(V,a) to be J_V with right action twisted
by beta_a. Write E_(U,a) for the ordinary localized ideal twist.
P123.085 therefore gives canonical topological isomorphisms

    E_(U,a) tensorhat_A F_(V,b) = F_(U cap aV,ab),
    F_(V,b) tensorhat_A E_(U,a) = F_(V cap bU,ba),              (1)

in both cases by x tensor y -> x beta_(first parameter)(y).
The first follows by transporting the second factor and the balancing
algebra by beta_a; the second follows from the right-hand identity in
P123.085. Associativity is equality of actual triple products on dense
elementary tensors, extended continuously. No product isomorphism
between two F objects is used here.

## 2. Fixed boundary labels and the trace

For v=q put

    L_q(a)={gamma in Gamma: gamma a_infinity=1 and gamma a_p=1}.

The first equality is real and the second is in Q_p. These are exactly
the labels for which gamma a fixes Z_q pointwise. The real equality
shows that L_q(a) is empty or a singleton. Define L_p symmetrically.
For x in F_(V,a) set

    T_(v,a)(x)=sum_(gamma in L_v(a)) integral_(Z_v) x_gamma dmu_v. (2)

This is a continuous functional bounded by j_00(x). For a=1 the
selected label is 1, recovering P123.085.

To verify twisted centrality it is enough first to consider
c=f U_delta and x=g U_eta, with f a C_0-plus-constant coefficient.
Both products select the same total label gamma=delta eta. If this
label is selected, their integrals are

    integral f(z) g(delta^-1 z) dmu_v(z),
    integral g(z) f(a^-1 eta^-1 z) dmu_v(z).

In the first substitute z=delta w. On Z_v the fixed-label condition
implies delta w=a^-1 eta^-1 w, so these integrals agree. The sums are
absolutely integrable by the mixed sup/L1 estimates. Density and
continuity extend the equality to all c in A and x in J_V:

    T_(v,a)(c x)=T_(v,a)(x beta_a(c)).                         (3)

Thus (2) is a genuine functional on Q_A(F_(V,a)).

## 3. Rotation across the mixed tensor product

For x in E_(U,a), y in F_(V,b), the two sides of (1) carry traces
with the same external parameter ab=ba. They satisfy

    T_(v,ab)(x beta_a(y))=T_(v,ab)(y beta_b(x)).               (4)

For a coefficient pair delta,eta the left integral is
integral x_delta(z) y_eta(a^-1 delta^-1 z) dmu_v(z).
Set z=a delta w; external invariance preserves the measure. If the
total label gamma=delta eta belongs to L_v(ab), then on Z_v

    a delta w=b^-1 eta^-1 w.

The transformed integral is exactly the corresponding right integral.
Absolute convergence again permits summation. Equation (4) therefore
descends through the completed balanced tensors, and successive
rotations are coherent since each preserves the same scalar value.

## 4. Changes of lift and transpose

If a'=delta a, the gauge map from F_(V,a') to F_(V,a) is
x -> x U_delta. Its coefficient at gamma delta is x_gamma, and

    gamma a'=(gamma delta)a.

Consequently T_(v,a)(x U_delta)=T_(v,a')(x). These equalities respect
successive lift changes by the group law, without choosing a new
normalization of the trace.

The conjugate-linear transpose sends x to beta_(a^-1)(x*) and the
support to a^-1 V. Its coefficient at gamma^-1 is
conjugate(x_gamma(gamma a z)). If gamma a fixes Z_v this restricts to
conjugate(x_gamma(z)); the inverse label is selected for a^-1. Hence

    T_(v,a^-1)(beta_(a^-1)(x*))=conjugate(T_(v,a)(x)).          (5)

## 5. Normal weight and the precise remaining comparison

When L_v(a)={gamma}, the normal action along Z_v is multiplication
by n=gamma a_v in Q_v^*. Away from n=1 the actual normal dilation
calculation P123.042 yields the scalar

    w_v(n)=|n|_v^(1/2)/|1-n|_v.

The parameterwise weighted functional w_v(n) T_(v,a) has the same
cyclic and gauge identities: both sides select the same total normal
action. It also respects (5), since w_v(n^-1)=w_v(n). This records
compatibility with the previously computed transverse factor, rather
than identifying a new global operator trace. At n=1 no finite weight
is assigned by this formula; P123.042 requires a regularized test-level
operation there.

There is a separate tangential issue even away from n=1: (2) is a
fixed-parameter functional, whose label selection varies discontinuously
with a. Integrating these parameterwise values against ambient Haar
measure is not a construction of the required character. Such a
character needs the correct tangential distribution/induced realization
and its normalization, together with the normal regularization. The
boundary trace integral on the covering stratum is not silently replaced
by an integral on its quotient.

The result establishes external composition, cyclicity, gauge invariance
and transpose on a common integrable module domain. A determinant-valued
shadow, its distributional analytic comparison and mixed RR remain open.
