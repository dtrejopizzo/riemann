# R170_813 — Corrected divisor–collar flux and sign obligations

Replaces the flux definition of R170_811 in line with
R170_812. The following definition and identities are justified; the
sign inequalities remain proposals, not proved.

## 1. Definition with no boundary regularization

Let Q_log be the space of functions of L²(R) with

    ∫ log(2+|τ|) |F̂(τ)|² dτ < ∞.

The full line form a_M associated with
A_M=m(D)−(L_M+L_M*) is continuous on Q_log×Q_log. The translations are
bounded on Q_log; so is U=𝓕, because its multiplier is unimodular and
its reflection preserves the even weight. A_MF∈L² is not required.

We fix δ=1 so as not to leave another quantifier implicit. For T>0,
N=ceil(exp(2T)), M=N² and a finite number L of moments, we take R_L and
S_L exactly as in Paper 46, with their outputs extended by zero. For a
primitive contact vector F, let r be its Tate vector and set

    g=S_LF,             h=S_N U g,
    e_{M,F}(v)=a_M(F,v)−<r,v>,        v∈Q_log,
    Flux_corr(F)=Re e_{M,F}(h).                            (A)

g is a finite sum of exponentials on I_T, extended by zero. It has
bounded variation and its transform decays as O(1/|τ|), so g∈Q_log.
Consequently h∈Q_log and (A) is a well-defined finite number. e_{M,F}
is a continuous conjugate-linear functional in v.

The weak equation and M≥exp(2T) give

    e_{M,F}(v)=0 if v∈Q_log is supported on I_T.          (B)

Thus (A) measures an exterior interaction in the sense of forms,
without claiming that e_{M,F} is always an L² function or a pointwise
boundary value.

## 2. Proved transport identity

On the kernel of regular data, PC and the intertwining relations give

    Flux_corr(F)
      = Re <{X,E_N}F−L_M*E_NF−JH_{M,N}F−H_{M,N}UF, g>
          − Re <S_N* r,Ug>.                              (C)

For data in Q_log, the sum of the first pairing is understood via its
joint extension a_M(F,S_NUg). Separate continuity of the four terms
containing X is not claimed. This convention is fixed before expanding
and makes (C) equivalent to (A), not to an arbitrary regularization.

Compared with the initial proposal,

    Flux_original−Flux_corr = Re <r,(S_N−S_N*)Ug>.         (D)

Term (D) has no known sign and must be subtracted, not discarded.

For smooth F with compact interior support, there is also an ordinary
exterior formula. With K from Paper 46 and t outside I_T,

    (A_MF)(t)=−(1/2)∫_{I_T} K(|t−s|)F(s)ds
             −Σ_{2≤d≤M} Λ(d)/√d [F(t+log d)+F(t−log d)].

In that case, if the local equation with r holds, (A) is the pairing of
that expression with h over R\I_T. For a general contact vector the
definition via forms is kept; that additional regularity, or absolute
convergence of an exterior expansion, is not assumed gratuitously.

## 3. Two separate obligations, not an acquired sign

A possible continuation of FIDC would be to prove, for every
hypothetical first contact and some L injective on its radical,

    Flux_corr(F) ≥ (1−q₀)||R_LF||²,                       (P+)
    Flux_corr(F) ≤ 0,                                    (P−)
    q₀=log2/4+1/16.

Neither of these two claims follows from (A)–(D). In particular:

- (P+) requires a new comparison between the exterior response and the
  Gamma–Euler reserve. Positive divisor weights are not enough.
- (P−) requires constructing an admissible window variation and
  proving that its balance equals exactly the value (A). The local
  equation (B) does not give this, because h is not an interior test.

It is not claimed that the scales M=N² and δ=1 are optimal or even
allow those signs. Their choice produces a specific proposal that must
be justified or abandoned, not a theorem about the primes.

If both obligations were proved with the same quantifiers, R_LF=0; the
injectivity on the radical would exclude F≠0. The Paper 46 primitive
first contact and Theorem F of Paper 45 would give the global
conditional closure. This dependency does not need to assume that a
complete contact is primitive. Neither obligation has been proved.

## 4. Next decisive check

Before extensive computation, an exact variational formula for (P−) or
an effective arithmetic comparison for (P+) must be obtained. If
neither appears, the flux should not be called "outward oriented" as if
the sign were geometrically automatic.

Numerical testing of a frequency or a near-eigenvector can serve as a
diagnostic, but it does not decide these claims, which are restricted
to the first contact. Falsifiers must preserve the hypotheses they
intend to refute. The R170_812 audit leaves the object corrected and
the obligations localized; it does not certify that this route is close
to resolving D.
