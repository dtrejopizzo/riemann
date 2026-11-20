# QRH — principal-target row quotient and the matching-height diagonal

2026-10-19. **Exact identities conditional on the source functional equation;
restricted diagonal bound. No new row-average estimate, no4/5 theorem.**

Corpus check: project rules, ROUTES-TRIED-INDEX (QRH entries and phase/FE
families), master grid and CROSSWORD-TO-D.md. New difference: specialize
the actual QRH row quotient to targetη=1 and retain its complex phase,
instead of applying a generic numerator/inverse estimate separately.
Source: Sept30 manuscript, §§4.8,7,8,10. No existing FE sign argument is
being reopened as a proof of D.

## Exact quotient, including original masks

Let χ=χ_•(u) be a nonprincipal row presentation, χ* its primitive inducing
character and Q its conductor norm. Retain every original zero mask:

    Lorig(s,χ)=Pχ(s)L(s,χ*),
    Pχ(s)=prod_(p in Eχ)(1−χ*(p)(Np)^(-s)).

The source has Eχ⊂S∪{p:p|u}, radical norm O_S(Nu). Set
Aχ=sqrt(3Q)/(2π). The primitive functional equation is

    Aχ^s Γ(s)L(s,χ*)
      = εχ Aχ^(1−s) Γ(1−s)L(1−s,barχ*), |εχ|=1.

Thus the principal-target quotient, at general independent s,w, is exactly

    Lorig(w,χ)/Lorig(s,χ)
      = εχ Aχ^(1−2w) Γ(1−w)/Γ(w)
        · Pχ(w)/Pχ(s)
        · L(1−w,barχ*)/L(s,χ*).                 (QGEN)

This identity is initially meromorphic; inequalities below are taken where
the denominator is nonzero. Gamma boundary values are understood by
continuation when needed. The conductor here is that of the primitive
character, not the raw presentation modulus.

On w=1−s, the last ratio is L(s,barχ*)/L(s,χ*). It is NOT generally1.
Finite-order Hecke characters in this family need not be real or self-dual.
The root number εχ does not remove this unknown ratio.

## Matching-height diagonal: a genuine restricted modulus bound

For fixed a∈(1/2,1), take s=a+it and w=1−a+it=1−bar s. Then

    L(1−w,barχ*)=L(bar s,barχ*)=overline{L(s,χ*)}.

Therefore(QGEN) has last factor of modulus exactly1, leaving

    |Lorig(1−bar s,χ)/Lorig(s,χ)|
      = Aχ^(2a−1) |Γ(bar s)/Γ(1−bar s)|
        · |Pχ(1−bar s)/Pχ(s)|.                 (QDIAG)

On fixed compact a-ranges inside(1/2,1), the finite deleted-product bound
from the source and Stirling yield, for every ε>0,

    |Lorig(1−bar s,χ)/Lorig(s,χ)|
       ≪ (Nu)^ε Q^(a−1/2)(1+|t|)^(2a−1).      (BDIAG)

The implied constant depends on the compact range, ε and fixed arithmetic
data, not on the row or height. At isolated zeros on the line, this is a
bound on the ratio off its undefined points, with bounded line limits;
it is not a claim of a holomorphic cancellation in two variables.

Since Q≪Nu and δ=2a−1, the conductor cost here is at most
(Nu)^(δ/2+ε), the same reflected-numerator power appearing in the
published estimates (with O(e) buffer costs on their contours). The
diagonal simplification is not itself an improvement of that exponent.

The phase remains εχ times a gamma/conductor phase times
Pχ(1−bar s)/Pχ(s) times overline{L(s,χ*)}/L(s,χ*). Neither positivity nor
cancellation in the row average follows from its modulus.

## Why this does not yet control the high integral

The actual buffered central contours in the source are

    s=a+16e+it_s, w=1−a−6e+it_w,
    w+bar s−1=10e+i(t_w−t_s).

There are two independent heights. Even as e tends to zero, the full
integral is not supported on t_w=t_s. Its kernels do not include a delta
constraint imposing this diagonal. The functional equation does not
collapse the independent integrations. Off this set the last factor in
QGEN is the two-point quotient

    L(1−w,barχ*)/L(s,χ*),

and BDIAG supplies no bound for it. In particular, taking absolute values
on the full existing contours cannot use BDIAG in place of the actual
inverse estimates. Localizing to a neighborhood would leave an error
requiring a new bound for differences or derivatives of this quotient;
no such bound was obtained here.

## Conjugate rows do not supply an automatic average

For sextic symbols, including their zero extensions,
χ_n(u^5)=overline{χ_n(u)}. Reducing valuations modulo6 gives a sixth-power-
free representative u# with valuations j→6−j, the same radical and the
conjugate row character. Its primitive conductor is the same, and root
numbers satisfy ε_(barχ*)=overline{εχ*}. These facts do not supply a
norm-shell involution preserving the weights: for squarefree u, u#=u^5
and Nu#=(Nu)^5. General valuation patterns also change the norm. The full
weights ξ(u)(Nu)^(-z)H_(1,u)(s,w,z), and any selected-slot factors, must
be transformed along with the character; they are not known to form
positive or cancelling conjugate pairs. Even conjugate scalar phases
would merely sum to twice their real part, which has no fixed sign.

## Outcome

The principal specialization gives a real simplification on one precise
matching-height diagonal: no primitive inverse loss in its modulus.
It has not produced a bound for the independent-height, weighted row
integral that controls the floor bin. The new estimate still required is
an average of the two-point quotient in QGEN with the actual root-number,
conductor, masks, local-correction and height weights retained. No estimate
of that average, and no4/5 zero-free conclusion, is proved in this memo.
