# QRH — exact absolute-convergence mean of the principal-target quotient

2026-10-19. **PROVED from finite residue-character orthogonality, CRT and
lattice counting. No moving-contour error bound, no4/5 conclusion.**

## Corpus and new difference

Read project rules, ROUTES-TRIED-INDEX (QRH and Ramanujan/FE families), master
grid and CROSSWORD-TO-D.md. This computes a previously unspecified mean
for the actual principal-target QRH quotient. It is not a Ramanujan
identity for the Weil comb or a claim that a generic FE quotient is
positive. Difference: retain the exact zero extensions in averaging the
external quotient before taking absolute values. No paper is changed.

## Setting

K=Q(sqrt(-3)), O its integer lattice. Fix S containing primes above6.
Write Q=Np. All L-functions below have the original row zero extension
χ_u(n)=χ_n(u) and omit S. Let

    R_u(s,w)=L^S(w,χ_u)/L^S(s,χ_u), Re s>1, Re w>1.

Average over nonzero elements with Nu≤U,(u,S)=1, with all unit factors
included, and normalize by their count. Denote that limit M_all.
Alternatively impose vp(u)≤5 for all p∉S and normalize by the count of
these sixth-power-free rows; denote that limit M_6free. Principal rows
are allowed in these means; they cause no singularities in this domain.
This is not an average over zero-defined bins or with the additional
weights ξ(u), (Nu)^(-z), H_(1,u), slot factors or kernel phases of the
high expansion.

## Local means, including divisibility masks

For p∉S the sextic residue character on(O/p)^× has order6. Its extension
χ_p(u) is zero if p|u. Uniform residues therefore give, for every k≥1,

    E χ_p(u)^k = 0             if6 does not divide k,
                  c_p         if6 divides k.

For unrestricted rows c_p=1−Q^(-1). For sixth-power-free rows the
conditional probability of p∤u is

    c_p=(1−Q^(-1))/(1−Q^(-6)).

Conditioning on vp(u)<6 preserves uniformity on the unit residues, hence
the same character orthogonality. The local quotient expansion is

    (1−χ_p(u)Q^(-s))/(1−χ_p(u)Q^(-w))
       =1+(1−Q^(w−s)) sum_(k≥1)χ_p(u)^k Q^(-kw).

Consequently its local average is exactly

    D_p(s,w)=1+c_p(1−Q^(w−s))Q^(-6w)/(1−Q^(-6w)).       (LOC)

In particular the mask factor c_p must not be suppressed: averaging
unimodular character values only would be the wrong row measure.

## Existence of row measures and finite-prime independence

For any fixed ideal modulus, planar lattice counting makes residues
asymptotically uniform in the disks Nu≤U. CRT implies independence for
every fixed finite collection of local residue conditions. Restricting
(u,S)=1 simply conditions finitely many independent primes.

For the sixth-power-free condition one must also control the infinite
sieve tail; CRT alone is insufficient. If p^6|u, then Q≤U^(1/6).
Since O is principal, the lattice p^6 is a rotation/dilation of O and

    #{0<Nu≤U:p^6|u} ≪ U/Q^6+sqrt(U)/Q^3+1.

The number of prime ideals of norm≤X is O_K(X), using ideal counting
alone. Thus for any fixed L, the number of rows divisible by p^6 for
some Q>L is at most

    O_K(U L^(-5)+sqrt(U)L^(-2)+U^(1/6)).

Dividing by U and taking limsup gives O_K(L^(-5)), tending to zero.
The denominator density is positive:

    prod_(p∈S)(1−Q^(-1)) prod_(p∉S)(1−Q^(-6)) >0

relative to the full lattice count. Finite-prime CRT may therefore be
passed to the infinite sixth-free condition. This proves the stated
conditional local law and independence, not merely a formal Euler model.

## Infinite quotient mean (PROVED)

In the absolute-convergence domain,

    R_u(s,w)=sum_(n,m prime to S) μ(n)χ_(nm)(u)/(Nn)^s(Nm)^w.

The series is bounded uniformly in u by the convergent positive series
sum_n |μ(n)|(Nn)^(-Re s) sum_m(Nm)^(-Re w). Its tails are uniform,
locally uniformly for Re s,Re w>1. For each fixed pair(n,m), finite CRT
and the preceding sieve argument give its row mean. It vanishes unless
nm is a sixth power; when it is, each prime dividing nm contributes c_p.
Termwise averaging is therefore justified by this uniform summability.
Multiplying the local sums gives

    M_all(s,w)=prod_(p∉S) D_p(s,w), c_p=1−Q^(-1),
    M_6free(s,w)=prod_(p∉S) D_p(s,w),
                  c_p=(1−Q^(-1))/(1−Q^(-6)).           (MEAN)

These products converge locally uniformly in the stated domain, since
D_p−1=O(Q^(-6Re w)+Q^(-Re s−5Re w)) on compact subsets.
The expressions equal1 at s=w, as required by the exact quotient.

For comparison, deleting the divisibility mask altogether would give
ζ_K^S(6w)/ζ_K^S(s+5w). The actual normalizer is that diagonal product
with a nontrivial convergent correction: setting A=Q^(-6w),
B=Q^(-s−5w), the correction factor is

    1+(1−c_p)(B−A)/(1−B).

This follows algebraically from(LOC), not from continuation of the row
average beyond its proved domain.

## Analytic product domain versus averaging domain

The right side of(MEAN), considered ONLY as an Euler product, is normally
convergent and holomorphic on

    6 Re w>1, Re s+5 Re w>1.

Indeed these are sufficient summability inequalities for D_p−1 above;
the first also keeps every1−Q^(-6w) denominator nonzero. This domain
contains the central floor-bin real positions s≈.51,w≈.49. It does NOT
justify exchanging row averaging with analytic continuation of R_u. The
mean identity has been proved only where Re s,Re w>1.

## Exact centering and unresolved estimate

One can now define R_u−M_6free(s,w) with ZERO limiting unweighted mean
in the absolute-convergence domain. This identifies an arithmetic main
term before absolute values. The argument supplies no useful quantitative
rate uniform in moving Euler moduli, row bins, conductor or independent
complex heights. Fixed-modulus CRT and a uniform summable tail justify
existence, not the required power saving after contour moves.

The actual QRH high expansion has all the extra weights excluded above.
They must be inserted and controlled explicitly; a zero-conditioned bin
need not have the unweighted local distribution. Analytically continuing
the Euler product on the right of(MEAN), if possible, would not prove
that the row averages or errors continue with it. Neither this main term
nor the earlier matching-height modulus bound proves cancellation of the
independent-height floor integral. The4/5 goal remains unproved.


## Fidelity correction: the actual fixed character kills this raw mean

The unweighted(MEAN) is NOT an identified main term of the actual high
integrand. Source§6.1 chooses ξ modulo b*, the squarefree product of S,
nonprincipal at each prime factor. Source§7 specifies that the u-sum
includes ALL unit factors of sixth-power-free elements, not just a primary
representative. Consequently the admissible residue classes at S are the
full unit classes. The normalized average of ξ over them is zero.

For any fixed finite Euler product of R_u, its dependence on u is through
residues at primes OUTSIDE S. CRT makes these independent of the S-unit
residues. Thus multiplying by ξ(u) makes its limiting mean zero. For
sixth-power-free rows the same assertion follows by first imposing the
condition at finitely many primes outside S, then using the tail estimate
above. Since |ξ|≤1, the same uniform absolute-convergence series tails
used for(MEAN) justify passage to the full quotient. Therefore

    lim average_u ξ(u)R_u(s,w)=0, Re s>1, Re w>1,

for BOTH row measures defined above. This conclusion uses the source's
actual unit-factor convention; it would require a fresh check if rows
were restricted to smaller ray classes on which ξ became constant.

A fixed finite product of the additional H_(1,u) local factors does not
change this vanishing in the sixth-free measure. Indeed, source7.6 gives
its row dependence through j=vp(u)∈{0,...,5} and
ρ=χ_p(u/p^j). These depend on u modulo p^6, outside S; the constants in
the local expression are fixed. The finite local product is bounded for
fixed parameters in the source's initial convergence region, so the same
finite CRT argument applies. The following additional initial-domain estimate justifies passage to
the full H product for sixth-free rows. Pointwise convergence alone
would not suffice.

The raw normalizer(MEAN) therefore supplies only an unweighted diagnostic.
It should NOT be subtracted from the actual ξ-weighted floor sum as if it
were its main term. Even the proved ξ-weighted zero limit is not a
power-saving estimate: the actual floor-bin restriction, moving moduli,
independent complex heights and local/slot corrections remain to be
controlled. The bin depends on row L-functions and need not preserve CRT
independence. No estimate for that weighted, binned floor sum is proved.


## Full actual correction on the initial lines: uniform-tail upgrade

Restrict now to sixth-power-free rows and Re s,Re w,Re z>1. The source's
local identities7.11–7.17 give a stronger UNIFORM tail than their estimates
near the reflected contours. At p|u, D=W=0; inspecting j=1,...,5 in7.11,
the non-negligible J_j exponents have respective upper bounds

    −Re s−Re w,
    3/2−3Re s,
    max(2−3Re s−Re w,2−4Re s),
    5/2−4Re s−Re w,
    3−6Re s.

All J_j terms are strictly below−3/2 or below−2. However the COMMON
term in7.11 contains V^(1_(j≤1)): for j≥2 it has exponent
1−Re s−Re w, which can be arbitrarily close to−1. It must be retained;
it prevents a fixed−5/4 bound throughout the whole initial domain.
The R terms are smaller there. At p∤u,7.17 cancels the leading term−D and leaves, in particular,
DW with exponent−Re s−Re w<−2 and still smaller terms. The local
1−R,1−V,1−D denominators are uniformly bounded away from zero. Hence,
on every compact subset of this domain, and uniformly in all sixth-free
u and all their unit phases,

    |H_(1,u),p(s,w,z)−1| ≤ C_K (Np)^(-1−ε_K),
    ε_K=min{1/4, (inf_K Re s+inf_K Re w−2)/2}>0.

Ideal counting gives sum_(Np>L)(Np)^(-1−ε_K)=O_K(L^(-ε_K)).
Thus the H product converges
UNIFORMLY IN u, with a uniform bound and uniform tail. The quotient R_u
also has uniformly convergent Euler/Dirichlet tails on the stated compact
sets. Finite CRT followed by this uniform limit now proves

    lim_(U→∞) average_(u sixth-free,Nu≤U,(u,S)=1)
         ξ(u) R_u(s,w) H_(1,u)(s,w,z) = 0,
    Re s,Re w,Re z>1.                              (ACTUAL-INITIAL)

For each FIXED Z and fixed slot system, the correctionH_(1,u),Z of16.3
is a FINITE sum of finite local replacements G_p times products of H_p
at the unselected primes. All selected primes lie outside S. Their local
j,ρ dependence is still on residues modulo p^6; local denominators are
bounded on the initial domain. The same uniform-tail argument applies
term by term and the same zero mean holds with H_(1,u),Z. Constants here
may depend on the fixed Z and slot system. No uniform estimate as Z moves
is asserted. This uses the quotient-free definition16.3, not a division
by possibly vanishing H_p.

This is the actual ξ-weighted correction, but only its initial-domain,
unbinned mean. The norm weight (Nu)^(-z) in the high expansion, fixed-ray
components if further imposed, and the restriction by zero-defined bins
are not removed by a claim about this unweighted limiting mean. A limiting
mean zero is not an identity making the actual weighted sum zero. Nothing
here supplies a power-saving rate, independent-height contour control,
or an estimate of the continued floor-bin integral.
