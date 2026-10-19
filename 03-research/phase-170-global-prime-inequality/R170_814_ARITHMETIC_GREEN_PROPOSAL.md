# R170_814 — Proposal for an arithmetic comparison with an interior contraction

New proposal, following the R170_812 audit.
The two definitional defects of R170_811 are repaired and an interior
energy of proved sign is built for comparison with the flux. The
proposed arithmetic comparison is NOT proved. It is not claimed that
this route is close to closing D nor that it is a new RH result.

## 1. What is kept and what is replaced

We keep the finite Poisson–Chebyshev identity and the Gamma moments. We
replace the Tate port with the correct adjoint S_N* and remove the
regularization χ_ε: all pairings are defined on Q_log by duality of
forms, as in R170_813.

We also replace the informal claim "the incoming orientation imposes a
sign" with a precise comparison against a nonnegative interior energy.
This energy has a proved sign; that it dominates the flux is a new
obligation, made explicit rather than assumed.

## 2. Data and quantifiers

Assume conditionally a primitive first contact T and a real vector F of
definite parity, F≠0, H_TF=0, H_T≥0. Let r_F be its Tate vector,
extended by zero. We fix

    N=ceil(exp(2T)),   M=N²,   δ=1,
    ρ=1−1/(2N²),      h=1−ρ>0.

The symbol ρ here denotes only the contraction factor, not a zero of
zeta. We choose an integer L such that R_L is injective on ker H_T; it
exists by the fidelity of the moments and the finite dimension of the
radical. The proposed law requires that for each first contact there be
ONE same L that works for all its definite-parity vectors. L is not
chosen separately after checking each vector's sign.

Let U=𝓕 and g=S_LF, with S_L and its adjoints defined on L²(I_T) and
extended by zero. The nonlocal test is z=S_N U g. We define

    Φ(F)=Re[a_M(F,z)−<r_F,z>].                           (1)

The test g has bounded variation and belongs to Q_log; U and S_N
preserve that space. Hence (1) is finite without requiring A_MF∈L² nor
taking limits.

On the regular kernel, its Poisson–Chebyshev representation is

    Φ(F)=Re<{X,E_N}F−L_M*E_NF−JH_{M,N}F−H_{M,N}UF,g>
                   −Re<S_N* r_F,Ug>.                    (2)

For general data, the total combination in (2) is extended via (1),
not by separately evaluating uncontrolled terms containing X. These are
the two repairs over R170_811: correct adjoint and direct definition on
the energy domain.

## 3. Interior construction of proved sign

Write C(v)=∫v(t)cosh(t/2)dt and S(v)=∫v(t)sinh(t/2)dt. Primitivity is
equivalent to C(v)=S(v)=0. Take the fixed function

    η(u)=exp(−1/(1−u²)) for |u|<1; η(u)=0 otherwise,
    η_{ρ,T}(t)=η(2t/(ρT)).

We define two smooth correctors supported on I_{ρT}:

    p(t)=η_{ρ,T}(t)cosh(t/2) / ∫η_{ρ,T}(u)cosh²(u/2)du,
    q(t)=η_{ρ,T}(t)sinh(t/2) / ∫η_{ρ,T}(u)sinh²(u/2)du.

The denominators are positive; by parity,

    C(p)=1, S(p)=0, C(q)=0, S(q)=1.

With the unitary dilation D_ρF(t)=ρ^(−1/2)F(t/ρ), set

    G_ρF=D_ρF−C(D_ρF)p−S(D_ρF)q.                        (3)

Then G_ρF is primitive, is supported on I_{ρT}, preserves the parity of
F, and belongs to the energy domain. All of this follows directly from
(3); no asymptotic estimate of the primitivity error is used.

We define the interior energy

    E_ρ(F)=a_{ρT}(G_ρF,G_ρF)/h.                         (4)

**Proved lemma.** E_ρ(F)≥0. Moreover

    h E_ρ(F)=a_T(G_ρF−F,G_ρF−F).                        (5)

Proof: the form on the smaller window coincides with that of the
extension by zero on I_T. There, G_ρF and F are primitive, a_T is
nonnegative, and F is in its radical. Hence a_T(F,G_ρF)=a_T(F,F)=0,
which proves (5) and the sign. The dilation preserves Q_log for ρ>0 and
the correctors are smooth, justifying the domains.

This argument uses nonnegativity on the contact window. By itself it
does not distinguish a FIRST contact from another nonnegative contact;
that extra datum must enter the pending comparison.

## 4. A uniform proposal with two explicit obligations

With q₀=log2/4+1/16 and R_L with δ=1, it is proposed to prove, with the
quantifiers of §2, the two inequalities

    (i)   (1−q₀)||R_LF||² ≤ Φ(F),
    (ii)  Φ(F)+E_ρ(F) ≤ 0.                              (G)

The difference from R170_811 is precise: (ii) is no longer attributed
to a verbal orientation. It asks for a comparison of the exterior
pairing (1) with the explicit interior energy (3)–(5). It is STRONGER
than Φ≤0; it has not been derived from minimality, nor is it assumed to
be true.

The parameters ρ,N,M are fixed by a recipe for every T. The same claim
must be proved at all scales, not chosen after observing a favorable
value. Nor is it claimed that the chosen recipe is optimal or that it
allows (G).

If (G) were proved, (4) would give

    0 ≤ (1−q₀)||R_LF||² ≤ Φ(F) ≤ −E_ρ(F) ≤ 0.

Hence R_LF=0 and, by injectivity on the radical, F=0: a contradiction.
The Paper 47 first contact and Theorem F of Paper 45 would then give
the global closure via the primitive route. This is a conditional
implication; no part of this note proves (i) or (ii).

## 5. Exact place where the integer identity must enter

For z defined above, set

    Ω=Re m(F,z)−Re<r_F,z>,
    ξ_d=Re<F,(τ_{log d}+τ_{−log d})z>.

Here m(F,z) is the full-line archimedean form. Exactly,

    Φ=Ω−Σ_{2≤d≤M} Λ(d)ξ_d/√d.                         (6)

The inversion Λ=μ*log allows writing the finite sum as

    Σ_{km≤M} μ(k)log(m) ξ_{km}/√(km).                   (7)

No absolute value is taken, nor are the cross terms separated. The
arithmetic part of (G) would require proving the bound interval

    Ω+E_ρ(F) ≤ Σ_{km≤M} μ(k)log(m)ξ_{km}/√(km)
                       ≤ Ω−(1−q₀)||R_LF||².             (8)

Writing (7) does NOT give (8): the signs of μ and of ξ remain
uncontrolled. In fact, at a nonzero contact with an injective detector,
the endpoints of (8) are in an incompatible order. That is the sought
contradiction, not an already established estimate. Each side of (8)
requires an independent justification using the hypotheses of the
hypothetical contact and the integers.

The interior cancellation of PC via Σ_{d|k}Λ(d)=log k is an available
datum, but it has not been proved to produce either side of that
comparison. Hence this proposal still does not satisfy the requirement
of a new proved arithmetic inequality from the R169 registry.

## 6. Criteria to continue or discard

1. Derive (ii) from an exact Green identity linking (1) with (5),
   preserving Tate, primes, and both collars. Without that identity
   there is no established reason for the proposed sign.
2. Derive (i) via divisor incidences, not merely via h_{M,N}(k)≥0 or the
   already known Gamma–Euler contraction.
3. Do not call a counterexample a positive eigenvector or a near-contact
   from Galerkin: those tests do not satisfy the hypotheses of (G).
4. Do not import tail independence or a frequency γ_q determined by the
   window; the v2 corrections of R169 still stand.

The new proved component is the explicit interior test and its energy
identity. It relates to the dilation trial R170_704; it does not turn
that trial into a sign law. The construction repairs the definition and
makes the pending variational bridge checkable, but does not certify a
solution of D nor proximity to it.
