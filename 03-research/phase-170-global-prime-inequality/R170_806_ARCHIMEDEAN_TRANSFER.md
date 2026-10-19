# R170_806 — Exact transport to the common-complement model

Local construction for audit; does not prove RH.

## Result

The archimedean block of Paper 47 does indeed contain exactly the form
`b` of R170_805, with coefficient one. What remains is an explicit
compact integral operator and a scalar shift. No kernel comparison with
multiplicative loss is required. The primes and the polar term
transport in the same identity, without minimizing them separately.

Let L=2T and let U be the unitary transformation

    f(x)=sqrt(L) F(L(x−1/2)),       0<x<1.

We write

    k(v)=exp(−v/2)/(1−exp(−2v)),
    h_L(v)=L k(Lv)−1/(2v),        h_L(0)=L/4,
    (H_L f)(x)=∫_0^1 h_L(|x−y|) f(y)dy,
    a_L=γ_E+log(2πL).

The form of R170_805 is precisely

    b[f]=¼∬ |f(x)−f(y)|²/|x−y| dxdy
         +∫ −½log(x(1−x)) |f(x)|²dx.

Then the original archimedean term satisfies the exact identity

    A_T[F] = b[f] − a_L ||f||² − ⟨H_L f,f⟩.                 (1)

Here A_T denotes only the archimedean term, not the sum of prime
coefficients called A_T in R170_301.

## Proof and domain

By the digamma formula of R170_301,

    A_T[F]=m(0)||F||²+∫_0^∞ k(v)||F−S_vF||²dv,
    m(0)=−γ_E−π/2−3log2−logπ.

Let E_T[F]=A_T[F]−m(0)||F||² denote the Lévy energy without its
constant. Extending F by zero gives, after U,

    E_T[F]=½∬ Lk(L|x−y|)|f(x)−f(y)|²dxdy
      +∫ [K(Lx)+K(L(1−x))]|f(x)|²dx,

with

    K(z)=∫_z^∞ k(v)dv=atanh(exp(−z/2))+atan(exp(−z/2)).

We subtract b. The remaining difference part is

    ½∬ h_L(|x−y|)|f(x)−f(y)|²
    =∫ [∫ h_L(|x−y|)dy]|f(x)|²dx − ⟨H_Lf,f⟩.

For 0<x<1, the quantity

    K(Lx)+½log x+∫_0^x h_L(v)dv

is constant: its derivative is zero. The limit x→0 is
log2+π/4−½log L, since K(z)+½log z→log2+π/4.
Adding the two endpoint contributions,

    E_T[F]=b[f]+[2log2+π/2−log L]||f||²−⟨H_Lf,f⟩.

Adding m(0) produces (1). One can first work with smooth functions of
interior support. Since h_L is continuous on [0,1], H_L is self-adjoint
Hilbert–Schmidt. The difference between the two forms is bounded. The
identity also follows directly from the integrals for every datum of
finite energy; their energy domains coincide. For data outside that
domain, the archimedean term equals +∞ in the extended sense and the
original inequality is automatic, since the prime and polar terms are
finite.

It is not claimed that h_L has a fixed sign. Its value at zero follows
from k(v)=1/(2v)+1/4+O(v). A checkable bound, if needed to approximate
it, is ||H_L||≤2∫_0^1 |h_L(v)|dv. This bound is not used in (1).

## Full identity, preserving the arithmetic

Set d_n=log n/L, a_n=Λ(n)/sqrt(n), and let V_d be the compressed
translation on L²(0,1), (V_df)(x)=f(x−d), extended by zero. We define

    J_L=Σ_{2≤n<exp(L)} a_n(V_{d_n}+V_{d_n}*),
    c_L(x)=sqrt(L) cosh(L(x−1/2)/2),
    s_L(x)=sqrt(L) sinh(L(x−1/2)/2).

The form whose positivity Paper 47 seeks is exactly

    W_T[F]= b[f] − a_L||f||² − ⟨H_Lf,f⟩ − ⟨J_Lf,f⟩
            +2|⟨f,c_L⟩|²−2|⟨f,s_L⟩|².                 (2)

Hence no prime correlation or polar cross term is lost. In particular,
(2) preserves the exact values of Λ and the distances log n. The
formula is uniform as an identity for every L>0; this does not
constitute a uniform sign bound.

## How the R170_805 result enters

Let the intervals be Iν=(aν,aν+ε), S their union, and Qν the projection
onto the zero-average functions supported on Iν. With the Δν of
R170_805, we write

    P_S[f]=Σν [log(1/(2ε))−Δν] ||Qνf||²,
    R_S[f]=r[f]−P_S[f] ≥ 0,
    l₀[f]=(log2+½)||f||²−½|∫f|².

Thus (2) has the exact decomposition

    W_T[F]=R_S[f]+P_S[f]+l₀[f]
      −a_L||f||²−⟨H_Lf,f⟩−⟨J_Lf,f⟩
      +2|⟨f,c_L⟩|²−2|⟨f,s_L⟩|².                     (3)

Only R_S is guaranteed nonnegative. (3) allows applying the
simultaneous capacity while keeping a single complement and all
interactions in the rest. It does not allow replacing b by its
conditioned minimum while leaving intact terms that still depend on the
complement: the minimization must be done over the joint expression.

A concrete caution: the scalar term inside l₀−a_L I can be negative.
Hence discarding R_S and then minimizing the rest without proving
coercivity can produce −∞. The capacity bound alone does not authorize
that step. Likewise, the positive repair of one block does not prove
positivity of the unrepaired block.

## Precise residual and scope of the progress

With

    K_L=a_L I+H_L+J_L−2|c_L⟩⟨c_L|+2|s_L⟩⟨s_L|,

the remaining problem is b−K_L≥0. Since b=l₀+r≥log2 I, this is also
equivalent to

    sup spec(b^(−1/2) K_L b^(−1/2)) ≤ 1.                 (4)

(4) is only a reformulation; it is not a new arithmetic law. Its
operational usefulness here is that it specifies every residual of the
transport: there is no abstract archimedean block left to identify nor
a pending congruence for that block. The prime interaction, the
rank-two polar term, and the common complement remain part of the same
sign problem.

The progress proved is (1)–(3), which transports the capacity lemma
exactly to the real problem. Bound (4), an extremal annihilation, or
the global closure of Paper 47 have not been proved. For a next Schur
step, these exact blocks must be preserved and the residual controlled
in the inverse metric of the eliminated block, as explained in
R170_803; capacity alone does not pay for that residual.
