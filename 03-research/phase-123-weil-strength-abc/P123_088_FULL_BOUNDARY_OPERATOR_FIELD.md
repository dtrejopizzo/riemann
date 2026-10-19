# P123.088 — Full-label boundary representation in integrable trace-class fields

Status: PROVED-IN-REPOSITORY for the two-prime
integrable boundary domain. The trace is an integrated fiber trace,
not the ordinary Hilbert-space trace of a decomposable operator.

## 1. The full crossed-product representation

Use Z_q, B_q=Z_q/Gamma, quotient measure dy and a measurable fundamental
section s:B_q->Z_q from P123.087. On H_y=ell^2(Gamma) define

    (pi_y(x) xi)(delta)
      =sum_gamma x_gamma(delta s(y)) xi(gamma^-1 delta).       (1)

This is defined for every x in the ambient rapid algebra A of P123.085,
including its coefficient constants. Each summand is a diagonal bounded
multiplier followed by a unitary permutation, hence

    ||pi_y(x)|| <= sum_gamma ||x_gamma||_infinity = p_0(x).

The series converges in operator norm uniformly in y. Matrix entries
are measurable. Directly composing the summands gives

    pi_y(x) pi_y(z)=pi_y(xz),   pi_y(x*)=pi_y(x)*,   pi_y(1)=1.

Indeed the coefficient pair gamma,eta gives
x_gamma(delta s) z_eta(gamma^-1 delta s), exactly the crossed-product
coefficient at gamma eta. The star follows either by reversing this
matrix entry or by taking the adjoint of each diagonal-permutation term.

Changing section to s'(y)=eta(y)s(y) just permutes the orbit-index
basis: the unitary (V_eta xi)(delta)=xi(delta eta) conjugates the old
formula into the new. Thus this defines an operator field independent
of the chosen frame up to specified unitary conjugacy.

## 2. The integrable source lands in a genuine trace ideal

For x in J_W, let

    b_gamma(y)=sum_delta |x_gamma(delta s(y))|.

Periodization and Tonelli yield

    integral_(B_q) sum_gamma b_gamma(y) dy
       =sum_gamma integral_(Z_q) |x_gamma| dmu_q <= j_00(x).   (2)

Thus for almost every y all these sums are finite. The gamma summand
in (1) is trace class there, with trace norm b_gamma(y): a diagonal
ell^1 sequence has that trace norm, unchanged by a unitary permutation.
Consequently (1) also converges in trace norm for almost every y and

    integral_(B_q) ||pi_y(x)||_1 dy <= j_00(x).                (3)

This supplies a continuous map from the declared integrable module into
L1 fields of trace-class operators, simultaneously uniformly bounded
in operator norm by p_0(x). Multiplication by any pi(a), a in A, remains
in this ideal on either side, with integral trace norm at most p_0(a)
times the original integral trace norm. The construction therefore
preserves the actual full-label product, unlike scalar periodization.

For clarity, the target may be defined concretely as measurable operator
fields, modulo equality almost everywhere and with the frame conjugacies
above. Its bounded algebra uses essential-supremum operator norm; its
trace ideal uses integral trace norm. No claim of ordinary trace class
on the direct-integral Hilbert space is made: over a nonatomic base,
a nonzero decomposable field generally does not have that property.

## 3. The source trace is the integrated operator trace

The diagonal entry at delta in (1) is x_1(delta s(y)), since only gamma=1
fixes an orbit index. Absolute summability from (2) justifies the diagonal
trace and its integration, giving

    integral_(B_q) Tr(pi_y(x)) dy
      =integral_(B_q) sum_delta x_1(delta s(y)) dy
      =tau_q(x).                                             (4)

In particular cyclicity with all ambient coefficients follows from
ordinary bounded/trace-class cyclicity in each fiber and the bound (3).
All labels participate in pi(x) and in its products, even though its
trace, as it must, selects the identity coefficient.

The representation is faithful on boundary restrictions: if pi_y(x)=0
for almost every y, every matrix entry vanishes. The entry in row delta
and column gamma^-1 delta is x_gamma(delta s(y)). Since Gamma is
countable, a common null set suffices for all entries. Periodization
then implies x_gamma=0 almost everywhere on Z_q for every gamma.
Continuity and full support of dmu_q imply pointwise vanishing there.
Conversely those vanishing restrictions clearly give the zero field.
This is faithfulness on the boundary quotient, not on all of J_W;
coefficients vanishing on Z_q are intentionally in the kernel.

## 4. A controlled logarithmic trace germ

For x in J_W and |z| p_0(x)<1, the trace-class logarithm in each fiber
has absolutely integrable trace, because

    integral ||pi_y(x)^n||_1 dy
        <= p_0(x)^(n-1) j_00(x).

Hence the expression

    L_q(z;x)=sum_(n>=1) (-1)^(n+1) z^n tau_q(x^n)/n
            =integral Tr log(1+z pi_y(x)) dy                  (5)

converges absolutely, locally uniformly in the stated disk. It is a
holomorphic germ with derivative at zero tau_q(x), invariant under
the section changes. Formula (5) is a rigorously defined logarithmic
trace using the represented full product. It is not declared to be
the determinant line, metric or degree demanded by A.5/A.8. In
particular exponentiating (5) alone does not establish mixed RR.

## 5. Remaining comparison

P123.087 realizes scalar boundary densities through ordinary trace-class
normal compressions after external integration. The present result
realizes all boundary labels multiplicatively in an integrated fiber
trace ideal. These are two specified constructions. Their identification
as one external normal correspondence realization is still to be proved;
sharing the scalar trace tau_q does not establish that identification.
The normal action, external covariance, regularization and determinant
comparison must be made compatible in that realization before full A
can be claimed. The construction at p is obtained by exchanging p,q.
