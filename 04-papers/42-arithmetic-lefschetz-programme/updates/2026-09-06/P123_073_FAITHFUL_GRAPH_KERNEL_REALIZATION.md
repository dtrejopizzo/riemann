# P123.073 — Faithful graph kernels for the repaired local source

Date: 2026-09-06. Status: PROVED as a continuous kernel realization at
fixed S, with exact composition and lift identities. Geometric sheaf
descent, derived diagonal pullback and mixed RR remain unproved.

Let X=X_S be the original additive semilocal space and A=A_S^u of
P123.019. For b=(b_gamma) in A and an invertible external idele a,
define the row measure

    K_(b,a)(x,dy)=sum_gamma b_gamma(x)
                            delta_(a^-1 gamma^-1 x)(dy).

This is a finite complex Radon measure for each x, since its total
variation is bounded by p_0(b). Acting on bounded continuous functions,

    T_(b,a)f(x)=sum_gamma b_gamma(x)f(a^-1 gamma^-1 x)

is a bounded continuous function and ||T_(b,a)||<=p_0(b). Uniform
absolute convergence proves continuity. This does not assert that the
kernel is a smooth density or a trace-class operator.

Each summand is localized on the graph y=a^-1 gamma^-1 x in X times X.
Although these graphs can accumulate, the declared rapid coefficients
give uniformly summable row measures; no locally finite graph sum or
proper quotient action is required for this definition.

The realization is faithful for each fixed a. If T_(b,a)=0, its row
measure annihilates C_0(X) and is therefore zero. At every x with nonzero
real coordinate the points a^-1 gamma^-1 x are distinct as gamma varies.
The mass of each singleton is consequently b_gamma(x), even if other
atoms accumulate there. Thus b_gamma vanishes wherever the real coordinate
is nonzero. That set is dense in X, so continuity gives b_gamma=0
everywhere. This proves b=0, including its constant coefficient parts.

Kernel composition is absolutely justified by
sum_(gamma,delta)||b_gamma||||c_delta||<infinity. Direct substitution gives

    T_(b,a) T_(c,d)=T_(b beta_a(c),ad),

where beta_a is external coefficient dilation. In detail the coefficient
of label gamma delta is b_gamma(x)c_delta(a^-1 gamma^-1 x), precisely
the repaired crossed multiplication of b with beta_a(c). Hence the
isomorphism E_(beta_a) tensor_A E_(beta_d) -> E_(beta_ad) is realized
by composition of these actual kernels. The diagonal unit is T_(1,1).

Left and right multiplication on the kernel sector reproduce the twisted
bimodule actions:

    T_(c,1)T_(b,a)=T_(cb,a),
    T_(b,a)T_(c,1)=T_(b beta_a(c),a).

For a gauge lift gamma a, the exact relation is

    T_(b,gamma a)=T_(b U_gamma,a).

Indeed multiplying the label of b by gamma shifts its graph by exactly
gamma^-1. This realizes the corrected lift isomorphism geometrically,
not by an element missing from the coefficient algebra.

For finite direct sums retain the matrix/sector indices; do not identify
different abstract summands merely because their kernel operators have
the same image. The intertwiner maps and differentials of P123.064 act
by right coefficient multiplication on those indexed sectors. Their
chain and tensor identities hold through the faithful realization above.
This gives a kernel interpretation of that fixed-source dg construction.

The topology on a sector is its original coefficient Fréchet topology,
with continuous injection into bounded kernel operators. The proof does
not claim the inverse is continuous in operator norm, or that this norm
defines the required completion. Nor does it identify operator adjoint
with geometric transpose: half-density and measure choices must be
included before making that separate comparison.

This supplies concrete localization on the actual square X times X for
the existing graph sectors and their composition. It does not establish
the geometric coefficient category on the arithmetic square required by
A.1, Morita descent of all mixed objects, a derived diagonal restriction
of these potentially singular kernels, or their determinant/trace
comparison. Those remaining requirements must not be inferred from a
faithful bounded-operator representation alone.
