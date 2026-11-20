# QRH — exact replica operator and coherent channel

2026-10-19. **PROVED: decomposition, variance control and internal
equivalence of estimates. OPEN: critical selective estimate. No sign of D.**

## Corpus and explicit difference

Consulted: the project rules, the ROUTES-TRIED-INDEX index (L74 and QRH entry), grid
R162_2300_MASTER_GRID and CROSSWORD-TO-D.md. Starting point:
QRH_EXPONENT_MAP.md and OpenAI, PDF of 5Oct2026, §§2.2 and 3.
The difference is to compute the operator of the p^6 selection, not to
re-apply the sieve over the whole family. No new source of sign
nor a construction of another family is proposed. The following conclusions
are algebraic and use only elementary ideal counting.

## Domain and exact replica

We work in the fixed field K=Q(sqrt(-3)) and with the ideals, symbols and
zero extensions of the PDF. Having fixed the finite character ν, the finite
set S and W∈C_c^∞((0,∞)), let

    A = A_1(D) = Σ_(n,S)=1 μ(n)ν(n)W(Nn/D),
    P_D = {p∉S prime ideal: Y/2<Np≤Y},    Y=sqrt(D),
    J = #P_D.

For D sufficiently large J>0 (the published argument even uses
J≈Y/log Y); no quantitative lower estimate of J is needed
for the following normalised identities. All averages are
uniform over P_D. The symbol identity χ_n(p^6)=1_(p∤n) proves
exactly

    A_(p^6)(D) = A − B_p(D),
    B_p(D) = Σ_(n,S)=1,p|n μ(n)ν(n)W(Nn/D)
           = −ν(p) Σ_(m,S)=1,p∤m μ(m)ν(m)W(Np Nm/D).

The last equality includes the condition p∤m: without it the formula would be
incorrect for m divisible by p. No signed sum has been estimated.

## Uniform bound and variance (PROVED)

Let supp W⊂[u,v]⊂(0,∞). Ideal counting in this fixed field gives
#{m:Nm≤X}≤C_K X for X≥1. In the last sum only ideals with
Nm≤vD/Np≤2v sqrt(D) appear. Since |μν|≤1,

    |B_p(D)| ≤ C_(K,W) sqrt(D).

The constants may depend on the fixed character, S and W; they are uniform
in D and p. In particular, writing barB=J^(-1)Σ_p B_p,

    |barB|² ≤ C D,
    Var(B) := J^(-1)Σ_p |B_p−barB|²
            = J^(-1)Σ_p|B_p|²−|barB|² ≤ C D.

This controls the variance at the required scale without sieve or cancellation.

## Decomposition of the operator (PROVED)

In C^J with squared norm J^(-1)Σ|z_p|², let P be the orthogonal projection
onto the constant vector 1. The replica vector is R=A1−B. Then

    PR=(A−barB)1,         (I−P)R=−(B−barB1),
    E_sel(D):=J^(-1)Σ_p |A_(p^6)(D)|²
              = |A−barB|² + Var(B).

The term still uncontrolled is the CONSTANT channel, not the variance.
A bound on the row differences, even a perfect one, does not bound this
channel: adding z1 to all rows leaves all differences invariant.
This observation only describes the algebraic loss; it is not a no-go for
using additional arithmetic structure.

## Exact scope of the proposed estimate (PROVED)

The following two families of estimates, each required for
all ε>0 and allowing ε to be renamed, are equivalent:

    (i) E_sel(D) ≪_ε D^(1+ε),
    (ii) |A_1(D)| ≪_ε D^(1/2+ε).

Indeed, pointwise in D,

    E_sel(D) ≤ 2|A|² + 2 C D,
    |A|² ≤ 2 E_sel(D) + 2 C D.

The second inequality follows from A=A_(p^6)+B_p and averaging; the first
is the reverse inequality of the same type. ε is renamed when passing between
amplitude and energy. Thus, selecting the replicas does not turn the
critical estimate into a mere control of fluctuations between rows.
Nor does it make it false: both estimates remain OPEN here.

## What was attempted and what is missing

The exact operator was computed and Var(B) was controlled via the explicit
arithmetic sum for B_p. This leaves |A−barB|², with |barB|≪sqrt(D).
No new identity or estimate controlling that coherent
component was obtained. The published bound for ALL rows up to H=D^(1+ϑ) does not
cover the replicas of height N(p^6)≈D^3. Even granting the same bound
DH at H=D^3, dividing by J≈sqrt(D)/log D would give D^(7/2)log D for the
mean energy, very far from D^(1+ε).

Hence the selective target is an exact formulation of the problem
of cancellation of A_1 at that scale, with an auxiliary variance already controlled;
not a new proof of that cancellation. No impossibility of
improving it is claimed, nor is any external equivalence of D invoked. Also still pending
is an identity connecting such cancellation with the counterterm 017.

## Independent review

The review verified the identity with p∤m, the uniform counting, the
orthogonal decomposition and both implications. Its precision on
the quantifiers of ε was incorporated: no equivalence
with the same fixed ε is claimed. Favourable review with this scope; the coherent
component and the uncentred estimate remain OPEN.

## Continuation: direct attack on the coherent mean

C_D=A_1−barB is examined. The
same external object is kept, with the same fixed W,ν,S; a generic
Möbius decomposition is not relaunched as if it were a new route for D.

Put a_n=μ(n)ν(n)W(Nn/D) and
r_D(n)=#{p∈P_D:p|n}. Interchanging the finite sums gives exactly

    C_D = Σ_n a_n w_D(n),       w_D(n)=1−r_D(n)/J.

Always 0≤w_D≤1. If D>(8v)², no ideal of the support Nn≤vD can
be divisible by three distinct primes of the block: their product would have
norm greater than D^(3/2)/8>vD. Thus r_D≤2 and w_D≥1−2/J.
The mask does not contribute a new oscillating factor to μ(n)ν(n).

A formula at shorter scales with the SAME W is also obtained:

    B_p(D)=−ν(p)A_1(D/Np)+O_(K,W)(1).

Indeed, removing p∤m from the exact sum adds only m=pℓ with
Nℓ≤vD/(Np)²≤4v, a set bounded independently of D,p.
Hence

    C_D=A_1(D)+(1/J)Σ_p ν(p)A_1(D/Np)+O(1).

This identity does not bound the first term. Improving the sums at
scale D/Np≈√D reduces the approximation error to A_1; it does not prove
new cancellation of the term at scale D.

Finally, expanding the square gives

    |C_D|² = Diag_D + Off_D,
    Diag_D=Σ_n |a_n|² w_D(n)² ≪ D,
    Off_D=Σ_(n≠m) a_n conjugate(a_m) w_D(n)w_D(m).

The diagonal bound uses |μν|≤1, bounded W, ideal counting and w_D≤1.
Off_D is real by pairing of the indices and Off_D≥−Diag_D.
The critical bound would require Off_D≪_ε D^(1+ε), as an upper bound
for all ε>0, allowing it to be renamed when passing to the amplitude.
**That cross-term bound has not been proved.** The control of the
variance between replicas does not supply it: it keeps the same constant channel.

Outcome of this continuation: formulas and diagonal verified, without a
new critical estimate of C_D. No general impossibility is declared, nor
a closure of a route by mere reformulation, nor progress on the sign of D.
