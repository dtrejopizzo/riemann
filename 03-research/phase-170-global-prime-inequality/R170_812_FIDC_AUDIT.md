# R170_812 — Audit of the FIDC proposal

Direct review of R170_811 and of the Paper 47
formulas, section "A sum--product identity". The entire proof of
Theorem F of Paper 45 is not re-audited here.

## Verdict

The proposal contains a precise working idea — pairing the divisor
identity with a test that observes Gamma moments — but its original
formulation does not justify the meaning of "exterior flux" it
attributes to it. There is a wrong adjoint in the Tate subtraction, an
inoperative regularization under the original definition of S_L, and
two signs still without proof. It is not validated as an arithmetic
law, nor refuted for the real data: a counterexample to its
first-contact hypothesis would require exhibiting such a contact. Its
definition is corrected here and what it exactly measures is proved.

The corrected version is in R170_813. It is not presented as progress
on the sign: fixing an object does not prove the inequalities required
of it.

## 1. The adjoint of the Tate port

We use the inner product linear in the first argument. Let U=𝓕. From
the manuscript's definitions one derives

    U*=U, U²=I, Uτ_a=τ_{−a}U,
    U S_N*=S_N U,       U A_M=A_M U.                    (1)

The last equality uses that m is even and that L_M+L_M* is the
symmetric sum of translations. Hence, for data in the regular kernel
and any g,

    <S_N A_M U F,g> = <A_M F,S_N U g>.                  (2)

If r is the Tate vector extended by zero, the term that exactly
subtracts its contribution is

    <S_N* r,U g> = <r,S_N U g>,                        (3)

not <S_N r,U g>. The original flux, when the pairings are defined,
therefore satisfies

    Flux_original
      = Re<A_M F−r,S_N U g>
          + Re<r,(S_N−S_N*)U g>.                      (4)

The second term is not an exterior collar of A_M F−r and does not
vanish by unitarity or by parity. U does not in general commute with
the reflection J. The substitution S_N→S_N* at the port is necessary
for the proposed exterior interpretation; it does not by itself prove
either sign.

## 2. The regularization does not do what was expected

In Paper 47, R_L has domain L²(I_T). Its adjoint and S_L take values in
that same space. After extension by zero, g=S_LF is supported on I_T.
If χ_ε=1 on I_T, then χ_ε g=g exactly for every ε. There is no
approximation to a new boundary, nor are jumps smoothed.

If the intention was to extend the sum of exponentials beyond the
window, a different operator from the adjoint R_L* had to be defined.
That convention cannot be changed mid-calculation. R170_813 uses the
original adjoint and removes the redundant limit via duality of forms.

Moreover, the PC identity is initially proved on Schwartz functions. It
is not justified to evaluate its four terms with X separately on a
vector that only has finite logarithmic energy. The total combination
does have a continuous extension, made precise in R170_813.

## 3. What actually remains on the exterior

For M≥exp(2T), the weak equation of the primitive contact says that
A_M F−r annihilates every finite-energy test supported on I_T. The
corrected flux is its evaluation on h=S_N U S_LF, which in general is
NOT supported on the window. This is the exact exterior interaction.

The local equation does not control its sign. For example, the two
operators A_±=[[0,±1],[±1,0]], compressed to the first coordinate, have
the same nonnegative zero block and the same r=0, but their response on
the second coordinate to F=(1,0) has opposite signs. This is a
counterexample to an inference from the local equation, not to the
arithmetic problem nor to every possible consequence of minimality
between windows.

No admissible window variation was found whose quotient or derivative
is this flux. In particular, FIDC− remains a conjecture; the word
"incoming" does not supply the missing variational argument.

## 4. Positive incidence is not energy positivity

The identity Σ_{d|k}Λ(d)=log k exactly cancels the interior
coefficients of the hyperbola H_{M,N}. This is indeed preserved in the
revision. But h_{M,N}(k)≥0 does not fix the sign of a pairing between
oscillating functions. A shift with a positive coefficient can already
have Re<τ_a f,f><0: two translated bumps with opposite signs show this.

There is an additional simplification: if log N≥2T and F,g are
supported on I_T, then <J H_{M,N}F,g>=0. Each term is shifted outside
the window and the reflection does not bring it back into it. The term
containing H_{M,N} U F, however, does not vanish: U F does not have
that support. The two cannot be treated as the same positive-sign
boundary.

The reserve (1−q₀)||R_LF||² belongs to the operator R_L*(I−D)R_L.
R170_811 does not prove that the corrected flux dominates that
operator. That is the new inequality still missing, not a consequence
of PC.

## 5. Primitive bridge: an existing dependency, not another new lemma

Paper 47, lemma `lem:firstcontact`, already uses the continuity of the
primitive bound and refers to Paper 45 for the equivalence with RH. In
the current Paper 45 file, the relevant result is located at
`thm:sufficiency` (Theorem F) and `rem:sufficiency`: a zero off the line
produces smooth primitive tests of negative form.

Hence, accepting that corpus theorem, excluding every primitive first
contact would suffice for RH and then for full positivity. It is not
necessary for every complete null vector to be primitive. The warning
about that vector remains correct for a DIRECT argument with the polar
Schur complement, but it is not an additional gap in the global
primitive route. The "11.3" numbered reference from Paper 47 must be
checked against the version: in the current TeX, (11.3) also appears as
an equation label.

## 6. Checks and scope

`python3 verify_fidc_orientation.py` builds a finite unitary involution
with U S*=S U and U A=A U. With f,r,g real and of even parity, it
checks (2)–(4). The omitted Tate term is approximately −3.804956, while
the algebraic errors are below 8e−15. It also checks a negative pairing
of a shift with a positive coefficient.

The model is NOT a certified discretization of zeta nor a first-contact
vector. Its purpose is to rule out the incorrect algebraic cancellation,
even under parity, and to check the correctness of the adjoint.

The audit is focused and analytic. No supposed contact tests on
approximate eigenvectors were run: a small λ in Galerkin does not
certify a real contact nor refute a law restricted to contacts. Nor was
a full audit of Paper 45 or all of Paper 47 performed.
