# R170_803 — Boundary, repair, and response: a proof that demands the transport

Appendix D.1 and bridge C.1 of
[Freedman, 2606.29555v1](https://arxiv.org/abs/2606.29555v1) were
checked against lemmas 6.28/8.1/8.4 of [Three
Gates](https://arxiv.org/abs/2609.20367v1) and the rank/polar-capacity
conditions of Paper 47. The external certificates were not run, nor
was the whole operator chain validated.

Freedman explicitly separates a Mellin prefix from the Volterra tail.
It adds a trace for that prefix and studies a positive repair
`K+R*DR`. The bridge toward the de Branges evaluation remains a
separate obligation. This confirms that removing the boundary by
changing the quotient space does not remove its cost in the original
form.

## 1. Minimal counterexample to an inadmissible transfer

`K=diag(-1,1)`, `R=(1,0)` and `D=1` satisfy

    K+R*DR=diag(0,1)≥0,

but K is not positive. If a map J satisfies

    W=J*KJ,

the repair only proves

    W+(RJ)*D(RJ)≥0.

To recover W one must prove `RJ=0`, an additional budget that absorbs
that term, or another identity that cancels it exactly. This example
refutes the general inference; it does not aim to refute the whole
Freedman manuscript, which distinguishes its pending bridge.

## 2. Not even positivity on the kernel guarantees a bounded repair

In `ℓ²(N)⊕C`, let `A=diag(n⁻²)`, `b=(n⁻¹)` and

    K = [[A,b],[b*,0]],       R(x,t)=t.

K is bounded and self-adjoint; on ker R it is positive. If a scalar
repair d≥0 made K+dR*R positive, its compressions to the first N
coordinates would have Schur complement `d−b_N*A_N⁻¹b_N=d−N≥0`. This is
impossible for every N. Each compression admits a repair, but their
costs diverge. The problem is `b∉Ran A^(1/2)`.

Switching to a transported norm can make a different map bounded; one
must check that returning to the original form preserves domain, norm,
and cost. This is a concrete check of the infinite complement.

## 3. Residual identity useful for building an arithmetic comparator

Let there be a real or complex extension of the complete form

    W(x,y)=<x,Bx>+2 Re<x,Gy>+<y,Cy>,     B≥b I>0.

The exact reduced form is `S=C−G*B⁻¹G`. For any candidate response X₀,
we define `R₀=G−BX₀`. Then

    S=C−X₀*BX₀−X₀*R₀−R₀*X₀−R₀*B⁻¹R₀.                 (E)

Proof: substitute G=BX₀+R₀ and expand; all four terms come from the
same form. For unbounded operators this is first interpreted on a
common core where the expressions exist, or on the domain of B^(1/2),
requiring B⁻¹/²R₀ to be defined.

The inequality that a divisor-based construction must prove is

    C−X₀*BX₀−2 Re(X₀*R₀) ≥ R₀*B⁻¹R₀.                 (P)

There is no loss or separation of the polar term: B,G,C must be
extracted from the complete form. The right-hand side is nonnegative
and grows if the residual touches directions of small energy. A small
error in the ordinary norm is not enough near the contact.

## 4. Cancellation with error: what the proposed response must preserve

In the model `A=M_a−β|1><1|`, `J=∫a⁻¹`, `δ=1−βJ>0`, suppose now that
`g=Ax+e`, not that the equality is exact. Setting `θ=∫x` and `η=∫e/a`,
we obtain

    m_g=∫g/a=δθ+η,
    D=|m_g|²/(Jδ)
     =δ|θ|²/J+2 Re(θ conj η)/J+|η|²/(Jδ).              (F)

The final term reveals exactly the hidden loss incurred when using an
approximate identification of the row. η cannot be discarded merely
because it is small in absolute terms. Bounding that term requires
control over η/√δ; making it tend to zero requires η=o(√δ). An
arithmetic identity forcing η=0 would indeed eliminate that cost, but
we have not proved that the residual of the Weil operator satisfies
it.

## Scope for Paper 47

(E) and (F) are elementary Schur formulations, not new RH theorems.
They serve as an exact validation interface for the candidate
response: the next substantive work is to construct X₀ and prove (P)
using the integers, or to annihilate the residual moment that appears
in (F). Importing a positive repair or a contraction in another metric
does not substitute for that proof. Paper 47 already contains rank
conditions compatible with this requirement; these formulas make
explicit the cost of an approximation.
