# R183.002 — The conjecture as a restricted Hilbert--Schmidt contraction

> **Restoration R183.014, posterior to the following note:** if
> M_phi* A_S M_phi is trace class, the RHC limit exists for any
> strong exhaustion by finite-rank projections and coincides with that
> trace. Under this hypothesis, Corollary 1.1 is restored. No additional
> compatibility with the physical cutoff is required.

> **CORRECTION R183.012.** Identity (1.2) holds for each finite cutoff.
> This file did not build an exhaustion `E_R` compatible with the
> semilocal cutoff, nor did it prove that the limit of the difference of two
> divergent quantities is Connes--Consani's localized trace. Hence
> Corollary 1.1, (4.1), and `RET` are **UNPROVED** as physical limits. The
> rigorous formulation retained is the localized trace of R183.012(2.2).

## 0. Result

Semilocal sufficiency does not require the local quotient \(u_S^*\) to be
inner. That global condition was refuted by Connes--Consani. For a test
\(h_1\), only a comparison of two Hilbert--Schmidt norms is needed. The
comparison preserves \(h_1\)'s support and the two Tate conditions.

Here we prove the exact equivalence and expose its block defect. The
restricted inequality remains open.

## 1. Two-norm identity

Let \(\mathcal H=L^2(\widehat{C_{\mathbb Q,S}})\), let \(P\) be the
projection of the modular half-axis used by the quantized calculus, and let
\(u=u_S\) be the Tate unitary. Set

\[
 A_S={1\over2}u^*[2P-I,u]=u^*Pu-P.                       \tag{1.1}
\]

Let \(M_\phi\) be multiplication by
\(\phi=\mathcal F_C(h_1)\). Let \(E_R\) be an exhaustion by finite-trace
projections compatible with the semilocal formula's cutoff. Set
\(M_{\phi,R}=M_\phi E_R\).

### Theorem 1. `PROVED`

\[
 \boxed{
 \operatorname{Tr}(M_{\phi,R}^*A_SM_{\phi,R})
 =\|PuM_{\phi,R}\|_{\mathrm{HS}}^2
  -\|PM_{\phi,R}\|_{\mathrm{HS}}^2.
 }                                                        \tag{1.2}
\]

**Proof.** By cyclicity of the trace,

\[
 \operatorname{Tr}(M_\phi^*u^*PuM_\phi)
 =\operatorname{Tr}((PuM_\phi)^*(PuM_\phi)),
\]

and likewise for \(P\). `QED`

The two norms without \(E_R\) need not be finite. Only their renormalized
difference has a limit fixed by the trace formula. They are not separated
after removing the cutoff.

### Corollary 1.1. `WITHDRAWN`

For *The Scaling Hamiltonian*'s sign convention, Weil's inequality for
\(h=h_1*h_1^*\) is equivalent to

\[
 \boxed{
 \lim_{R\to\infty}
 \bigl(\|Pu_SM_{\phi,R}\|_{\mathrm{HS}}^2
       -\|PM_{\phi,R}\|_{\mathrm{HS}}^2\bigr)\le0.
 }                                                        \tag{RHC}
\]

Here \(h_1\) must have the prescribed support and satisfy the two Tate
moments. The family `(RHC)` over all supports is D.

## 2. It is strictly weaker than innerness

Connes--Consani's global condition is

\[
 Pu=PuP,                                                  \tag{2.1}
\]

equivalent to \(u^*\) being inner and to \(A_S\preceq0\) on all of
\(\mathcal H\). This fails for each local factor.

By contrast, `(RHC)` only compares the renormalized quadratic average of
\(Pu\) and \(P\) on the particular column \(M_\phi\). It does not imply (2.1)
when \(\phi\) varies within a single finite-type Paley--Wiener space. Hence
the innerness no-go does not refute `(RHC)`.

## 3. Block defect

Write \(Q=I-P\) and decompose

\[
 u=\begin{pmatrix}a&c\\b&d\end{pmatrix},
 \quad
 a=PuP,\ c=PuQ,\ b=QuP,\ d=QuQ.                         \tag{3.1}
\]

Unitarity gives

\[
 A_S=
 \begin{pmatrix}
 -b^*b&a^*c\\
 c^*a&c^*c
 \end{pmatrix}.                                          \tag{3.2}
\]

If \(M_{\phi,R}=\binom{M_P}{M_Q}\) by rows, then

\[
\begin{aligned}
 \operatorname{Tr}(M_\phi^*A_SM_\phi)
 ={}&-\|bM_P\|_{\mathrm{HS}}^2
     +\|cM_Q\|_{\mathrm{HS}}^2\\
 &+2\operatorname{Re}\operatorname{Tr}
       (M_P^*a^*cM_Q).                                   \tag{3.3}
\end{aligned}
\]

The first piece has the desired sign; the second has the opposite sign;
the third preserves the orientation. Separating them by absolute values loses
the problem. They must be recombined via Poisson into a single square.

## 4. Physical representation

Conjugating by \(\mathcal F_C^{-1}\):

* \(P\) becomes multiplication by
  \(1_{\{|x|\ge1\}}\) on \(C_{\mathbb Q,S}\);
* \(M_\phi\) becomes convolution \(C_{h_1}\);
* \(u\) becomes the additive Fourier operator followed by inversion,
  per Connes--Consani Lemma 2.3.

Thus `(RHC)` is

\[
 \boxed{
 \lim_{R\to\infty}\left(
 \|1_{|x|\ge1}\,U_S C_{h_1}E_R\|_{\mathrm{HS}}^2
 -\|1_{|x|\ge1}\,C_{h_1}E_R\|_{\mathrm{HS}}^2
 \right)\le0,
 }                                                        \tag{4.1}
\]

with the semilocal regularization understood. The support hypothesis controls
\(C_{h_1}\)'s propagation; Poisson controls \(U_S\); unique factorization
produces R183.001's rough gap.

This is the correct version of where the two tunnels meet.

## 5. A return law that would suffice

A sufficient identity, stronger than `(RHC)` but still restricted to the
admissible tests, would be to build a source operator \(Z_{q,h_1}\) such
that

\[
 \boxed{
 \|PM_{\phi,R}\|_{\mathrm{HS}}^2-
 \|Pu_SM_{\phi,R}\|_{\mathrm{HS}}^2
 =\|Z_{q,h_1,R}\|_{\mathrm{HS}}^2+o_R(1),
 }                                                        \tag{RET}
\]

`RET` must follow from decomposing \(\mathbb Q_S\) into units by
elements of \(M_S\) and from Poisson on the self-dual lattice. It cannot be
defined by taking the root of the left-hand side.

In terms of (3.3), `RET` must jointly absorb
\(\|cM_Q\|^2\) and the oriented term
\(2\operatorname{Re}\operatorname{Tr}(M_P^*a^*cM_Q)\) into the output
\(bM_P\). This is the precise exterior return law.

## 6. Status

```text
finite two-norm identity (1.2)                        PROVED
RHC converges and equals Weil for the test             UNPROVED
global innerness                                       REFUTED/CITED
RHC is refuted by the innerness failure                 FALSE
oriented block decomposition (3.3)                       PROVED
physical representation (4.1)                            PROVED/CITED
return source factor (RET)                               OPEN
row D                                                     OPEN
```
