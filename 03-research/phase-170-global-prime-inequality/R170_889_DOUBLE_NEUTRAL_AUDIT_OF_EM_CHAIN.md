# R170_889 — Double neutral audit of the EM chain

## 0. Protocol

The chain R170_884--888 was submitted to two independent reviews. The
second classified each objection as confirmed, refuted, or undecided,
without presupposing that an error had to be found.

This criterion is adopted for subsequent audits: trying to falsify a
statement does not create a presumption that it is false. A
downgrade in status requires a contradictory derivation or a counterexample.

### 0.1 Permanent double-control rule

Every audit marked as critical will be reviewed twice before
changing the status of a piece. Both reviews must reconstruct the
type of the objects, the hypotheses, and the algebraic chain; it is not enough for
the second to repeat the verdict of the first.

Each objection receives exactly one of these statuses:

1. **confirmed**, with a derived contradiction, a counterexample, or a
   necessary hypothesis explicitly identified as missing;
2. **refuted**, when the reconstruction shows that the original
   statement was correct;
3. **undecided**, when information is lacking to prove or refute it;
4. **no defect found**, when both reviews verify the piece
   within its stated scope.

`Undecided` is not equivalent to `false`, and mere inability to derive a
statement via one particular route does not invalidate the statement nor other
routes. A piece is only downgraded by reproducible mathematical evidence.
If the objection is refuted, the record must explicitly restore the
valid status of the piece. A correct audit may conclude that everything
audited is fine.

## 1. Classification

### A. Frozen identity of R170_886

**CONFIRMED.** The equality

\[
 \mathfrak W_{\rm ext}+(h,P\mathcal P_{C,A_M}F)
 =W(e_{\rm EM},A_MF)                                     \tag{1.1}
\]

is correct for `P,h,F` frozen. It was further checked on 300 finite
matrix models. The audit of the moving branch does not invalidate it.

### B. Range criterion

**CONFIRMED WITH A CAVEAT.** The equivalence

\[
 \omega_{\rm EM}\in\overline{\operatorname{Ran}H_T}
 \Longleftrightarrow
 (\omega_{\rm EM},F)=0\quad(F\in\ker H_T)                \tag{1.2}
\]

is Fredholm and does not prove the orthogonality. However, the explicit
formula for `omega_EM` remains a constructive contribution: it identifies
the exact arithmetic source that would need to be factored, with no
pseudo-inverse.

### C. Connection of the moving branch

**CONFIRMED.** To compare (1.1) with minimality one needs `chi_e`,
`A_M dot F`, `dot P`, and `dot R_T`. R170_887 computes them in the
fixed ambient trivialization. They complement (1.1); they do not refute it.

### D. Parity wall

**CONFIRMED.** `dot lambda` is quadratic and even, while the EM
functional is linear and odd. The latter cannot be identified with the
former nor inherit its sign from minimality alone. This does not prove that EM is
nonzero; it proves that an additional odd identity is needed.

### E. Z_N ledger of R170_888

**CONFIRMED UNDER ITS HYPOTHESES.** It is obtained by literally substituting
R170_856(9.4) into the moving Hellmann--Feynman derivative. It requires
REG/C1, cutoffs fixed within a chamber, and a consistent derivation
convention. It keeps the tails, and the sign belongs only to the sum.

## 2. Additional correction from the second audit

The Wronskian with ordinary derivatives is not invariant under a
moving orthogonal change. In `R^2`, take `e=e_1`, `v=e_2` constant and a
rotation with `dot U e_1=e_2`, `dot U e_2=-e_1`. Initially `W(e,v)=0`, while
the Wronskian of `Ue,Uv` equals `2` at the origin.

The invariant version uses a metric connection

\[
 \nabla=\partial_s+\Gamma_s,
 \qquad \Gamma_s^*=-\Gamma_s,                            \tag{2.1}
\]

and

\[
 W_\nabla(e,A_MF)=(\nabla e,A_MF)-(e,\nabla(A_MF)).       \tag{2.2}
\]

R170_887 was corrected on this point. Its ordinary formulas remain
valid in the fixed ambient trivialization.

The total ledger of R170_888 is indeed gauge-invariant because it represents
`dot lambda`: the changes of `dot A` and `dot Pi` cancel. Its
individual lines are not.

## 3. Verdict

```text
R170_886(0.2), frozen identity                            VALIDATED TWICE
explicit source omega_EM                                  VALID AND USEFUL
range criterion as a new proof                             NO; IT IS FREDHOLM
moving completion R170_887                                 VALIDATED TWICE
ordinary invariance under a moving gauge                    REFUTED AND CORRECTED
Z_N ledger R170_888                                         VALIDATED TWICE
covariant vanishing / VIR--LB / D                           OPEN
```
