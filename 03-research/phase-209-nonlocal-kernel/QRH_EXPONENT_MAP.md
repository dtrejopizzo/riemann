# QRH — exponent map and conditions for an extrapolation

2026-10-19. Algebraic computation, independently reviewed.
**PROVED as a conditional lemma; new estimates OPEN. No sign of D.**

## Scope and difference

Consulted the index (L74 and amplification families), grid and crossword.
No closed family is reopened nor is a new sieve proposed without proof.
The difference is to analyse the exact extraction of an external source now
read: equations 2.3–2.5 of the OpenAI PDF of 5Oct2026. No recurrence
is inferred by interpolating the numbers 47/48, 11/12, 7/8.

Source: https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf

## Replica lemma

Suppose, for growing D and H=D^h in an authorised range, a family
of complex numbers A_j, a signal A and a subset of J replicas with,
for all ε>0 (allowing ε-dependent constants),

    J >= H^κ D^(-ε),
    |A_j-A| <= C D H^(-δ) on each replica,
    sum_family |A_j|² <= C_ε D^(a+ε) H^b.

The constants must be uniform in D,H; h,κ,δ are fixed positive numbers.
Summing |A|²<=2|A_j|²+2|A_j-A|² over the replicas proves

    |A| <= C_ε D^(θ+ε),
    θ = (1/2)max{a+(b-κ)h, 2-2δh}.

Hence, for THIS BOUND to certify exponent 1/2+ε, it is sufficient and
algebraically necessary that

    h >= 1/(2δ),       a+(b-κ)h <= 1.

These are not necessary conditions for actual cancellation: the argument may
lose information and another control may improve it.

## Substitution into the published argument

The replicas are the rows p^6: J is of order H^(1/6)/log H and
A_(p^6)=A_1+O(D H^(-1/6)). Thus κ=δ=1/6. The bound used is
M(D,H)<=C_ε D^(1+ε)H, for H=D^(1+ϑ), 0<ϑ<=1/10.
Then a=b=1, h=1+ϑ and

    θ(h)=(1/2)max{1+5h/6,2-h/3}=11/12+5ϑ/12.

There is no rule that takes this θ as input for a next improvement.
Even granting COUNTERFACTUALLY the same bound for all h>0,
the algebraic minimum would be θ=6/7 at h=6/7. That range is not proved
by the cited result; 6/7 is not a new theorem, external or ours.

For h=3, the critical level would require the total average to be
O(D^(3/2+ε)), versus D H=D^4 at that scale. It is not claimed that such a
bound is true or feasible: it quantifies what this extraction would require.

## A precise alternative target, still OPEN

Instead of estimating the whole family, it would suffice to control only the replicas
p^6 with Np between Y/2 and Y, Y=D^(1/2), via

    sum_p |A_(p^6)(D)|² <= C_ε J D^(1+ε),
    J = #primes in the interval, of order Y/log Y.

The known error per replica is O(D/Y)=O(D^(1/2)); the lemma would give
|A_1|<=C_ε D^(1/2+ε). This target keeps the coherent signal;
the sieve over the whole family does NOT prove it. It may be as hard
as controlling the signal directly. It is not an already constructed new source.

**Update after the exact computation:** QRH_REPLICA_COHERENCE.md proves
that those two families of estimates are in fact equivalent, for
all ε>0 after renaming the exponent. The variance of the replicas is O(D)
without cancellation; all the remaining difficulty lies in their coherent mean.
The selection, by itself, contributes no new mechanism to bound it.

## The three fractions are not three iterations

Kintali 47/48 uses a probe and comparison by zero density in a
specific regime. The text of 30Sept2026 giving 7/8 additionally uses a detector with
inverse and ordinary polynomials and separate moment estimates
(introductory summary and §§17–20). This structural reading does NOT audit
its 199 pages. No common iterated transformation is identified.

For D an identity would still be missing that transfers any new
estimate to the exact lower bound of 017. No external equivalence
of D is used, nor is a control of the counterterm attributed to this lemma.
