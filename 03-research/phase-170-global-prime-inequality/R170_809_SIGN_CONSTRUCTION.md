# R170_809 — Preserved reserve and response inequality

This note's own construction. The two independent
attempts requested stopped due to usage limits before delivering
results. This note is not attributed to an independent verification.

**Status:** form inequality proved at each scale; the global sign
inequality is not proved. The construction implements the reserve
required by R170_808 and preserves the arithmetic in the remaining
block. No bibliographic novelty is claimed for the Schur method used.

## 1. Operators and a quantified reserve

We use R170_806 in full, in L²(0,1), with L=2T:

    W=b−K_L,
    K_L=a_L I+H_L+J_L−2|c_L><c_L|+2|s_L><s_L|,
    a_L=γ_E+log(2πL).

We split (0,1) into M equal intervals. P is the orthogonal projection
onto their normalized indicators and Q=I−P. For y in QH each cell
average is zero, including the global average. R170_805 gives

    b[y] ≥ λ_M ||y||²,       λ_M=log M+γ_E−1/2.          (1)

The cell indicators have finite energy: the logarithmic boundary
singularities are integrable, and the interior jump gives local
integrals of the type ∫∫(u+v)⁻¹du dv, also finite. Hence P and Q
preserve the form domain. The restriction to QH is a closed, densely
defined form; B is interpreted as its associated self-adjoint
operator.

Indeed, l₀[y]=(log2+1/2)||y||² and r[y] has lower bound
[log(M/2)−(1−γ_E)]||y||². The entire b is retained; R_S is not
discarded. Also b≥log2 I, so λ_M could be improved by taking the
maximum with log2, though this is not needed for the choice below.

Let h_L be the regular kernel of R170_806 and define the finite
quantities

    hbound_L=2∫_0^1 |h_L(v)|dv,
    pbound_L=2Σ_{2≤n<exp L} Λ(n)/√n,
    κ_L=max(0, a_L+hbound_L+pbound_L+2sinh(L/2)−L).

Then K_L≤κ_L I. To see this, ||H_L||≤hbound_L by Schur,
||J_L||≤pbound_L by contraction of the translations, and
||s_L||²=sinh(L/2)−L/2. The rank-one term −2|c_L><c_L| is nonpositive.
These bounds are used only to guarantee the coercivity of the
complement; the arithmetic blocks are not replaced by them in the rest
of the argument.

For any g>0, choosing an integer

    M > exp(κ_L+g−γ_E+1/2)

guarantees that the operator B associated with the restriction of W to
QH satisfies

    B≥g_M I,       g_M=λ_M−κ_L>g.                       (2)

This is a valid recipe for any fixed L, without RH, but its size may
be enormous. It does not constitute a uniform sign certificate for the
remaining block.

## 2. Extension that exactly preserves the reserve

On E=PH we define the positive invertible matrix

    D=P b⁻¹ P|E,
    V=b⁻¹ P D⁻¹ : E→H.

The inverse b⁻¹ exists because b≥log2 I. D is positive definite on the
finite space E. We have PV=I_E and bV=P D⁻¹. Hence

    b[Vx,y]=0 for y∈QH in the form domain,
    b[Vx]=<x,D⁻¹x>.

Vx is the unique extension minimizing b with Px=x. In particular, it
is not assumed that minimizing W is equivalent to minimizing b: the
arithmetic difference is explicitly preserved below. Every f of finite
energy is written uniquely as f=Vx+y, x=Pf, Py=0.

We define

    C=D⁻¹−V* K_L V,
    A=Q K_L V : E→QH.

Both are bounded; Vx is even in the domain of the operator b. The
exact expansion of the complete form is

    W[Vx+y]=<x,Cx>−2 Re<y,Ax>+B[y].                    (3)

In A, the prime translations, H_L, the shift, and both polar channels
appear together. The norm of their sum is not replaced by the sum of
norms, nor is an interaction between sources eliminated.

## 3. Inequality obtained and exact cost

From (2) and (3), completing a single square, we obtain

    W[Vx+y] ≥ <x,(C−A*A/g_M)x>
                       +g_M ||y−Ax/g_M||².            (4)

The remainder omitted when writing ≥ is exactly B[y]−g_M||y||²≥0. This
is a proved inequality, with every quantity defined, that avoids the
−∞ minimum of R170_808.

The loss-free minimization is

    inf_{Py=0} W[Vx+y]=<x,(C−A*B⁻¹A)x>.               (5)

The difference between the upper debit of (4) and the exact one of (5)
is

    A*(g_M⁻¹ I−B⁻¹)A ≥ 0.                             (6)

Hence the finite condition C−A*A/g_M≥0 is sufficient for W≥0. That
condition has not been proved for every L. Nor has the exact condition
C−A*B⁻¹A≥0 been proved for every L. Writing (5) does not prove its
sign.

## 4. Audit of the method's limit

At a possible contact with f=Vx+y and W[f]=0, (5) exactly preserves
the cost of the complement. If Ax has a component outside the
eigenspace of B with eigenvalue g_M, the additional cost (6) is
strictly positive in that direction. Estimate (4) can then lose
precisely the margin that is needed. Increasing M does not prove that
this cost stays below the critical gap, nor that it vanishes.

The construction still does not use the divisor identity to obtain a
sign: it employs the exact values of Λ in A and C, but having those
values in a matrix does not prove an arithmetic inequality about it.
The bounds of (1)–(2) work equally well for many altered weights, so
they cannot by themselves exclude the corpus's falsifiers.

The contribution of this attempt is the explicit combination of the
window capacity with a harmonic extension that keeps all sources in A,
and inequality (4). It is a certification tool at each scale, not the
global input required by R169. The requested global problem remains
unsolved; it is not replaced by the finite sufficient condition.
