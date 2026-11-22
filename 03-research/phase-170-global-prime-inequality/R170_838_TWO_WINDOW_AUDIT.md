# R170_838 — Audit of the two-window PC--collar datum

Audit of R170_837, in particular §§7--8.
R170_837 and Paper 46 are not modified.

## 0. Verdict

The collar identity of §7 is correct, with two necessary clarifications:
the sign is only fixed for the normalized vector selected as the limit
from the right and after choosing its phase, and all pairings must be
read in the carrier of forms, not as pointwise products of unbounded
operators.

The form of §8,

\[
 \mathfrak C_{M,N;T,\delta}(F,F_\delta)
 =\left\langle 1_{C_\delta}Z_NA_ME_TF,
                   F_\delta|_{C_\delta}\right\rangle,
 \tag{0.1}
\]

is a valid formal rewriting of PC-ren on the regular kernel. It can also
be given a weak definition under a continuity hypothesis that R170_837
does not state. But (0.1) **does not literally contain the signed
minimality pairing**

\[
 \langle\xi_F^\delta,F_\delta|_{C_\delta}\rangle
 =\lambda_\delta\langle F_\delta,E_TF\rangle .
 \tag{0.2}
\]

The filter \(Z_N\) is placed after \(A_M\) and before restriction to the
collar. Isolating (0.2) gives exactly

\[
\boxed{
 \mathfrak C_{M,N;T,\delta}(F,F_\delta)
 =\lambda_\delta\langle F_\delta,E_TF\rangle
  +\mathcal R^{\rm Tate}_{T,\delta}(F,F_\delta)
  +\mathcal R^{Z}_{M,N;T,\delta}(F,F_\delta),}
 \tag{0.3}
\]

where

\[
 \mathcal R^{\rm Tate}_{T,\delta}
 =\langle r_F,F_\delta|_{C_\delta}\rangle,
 \qquad
 \mathcal R^{Z}_{M,N;T,\delta}
 =\left\langle1_{C_\delta}(Z_N-I)A_ME_TF,
                    F_\delta|_{C_\delta}\right\rangle .
 \tag{0.4}
\]

Neither of these two residuals has a sign. The second is nonlocal: it
depends on \(A_ME_TF\) outside \(C_\delta\), and hence depends on \(M\)
even once \(A_ME_TF|_{C_\delta}\) has already stabilized. This is the
exact defect that prevents asserting that the cancellation
\(\delta_\Lambda=0\) and the minimality sign live in the same scalar.

There is also a decisive duplication. R162_406 already carried out the
step that R170_837 presents as the "new obligation": it wrote
\(\xi_F^\delta\) via the compressed Chebyshev identity
\(B_{T'}^*Z_{T'}=K_{T'}\), exactly localized the use of
\(\Lambda*1=\log\), separated the \(R_LF\) part from the residual, and
proved that this rewriting adds no relation. R162_407--408 reinforce the
no-go. Hence (8.3) does not advance G1.5; it packages PC and the
existence of \(F_\delta\), but does not couple them through a new
identity.

The correct status of (8.3) is:

```text
PC equality on the regular kernel                        CORRECT
extension to the real first-contact domain                NOT PROVED IN R170_837
extraction of the signed minimality identity               FALSE WITHOUT (0.4)
simultaneous use of delta_Lambda=0 and the sign in one scalar FALSE
new progress relative to R162_406                          NO / REPACKAGED
transport of the sign to R_LF                               NO-GO FOR THESE DATA
```

## 1. Conventions and types

### 1.1. Fourier, reflection, and shifts

The conventions of Paper 46 are

\[
 \tau_a f(t)=f(t+a),\qquad V_af(t)=f(t-a)=\tau_{-a}f(t),
 \qquad \mathscr F=u_\infty(D)J,
 \tag{1.1}
\]

\[
 \mathscr F^*=\mathscr F^{-1}=\mathscr F,\qquad
 \mathscr F^2=I,\qquad J\tau_aJ=\tau_{-a}.
 \tag{1.2}
\]

With these conventions, the step from R170_837 (8.2) to its first
reading in (8.4) is algebraically correct:

\[
 Z_NA_M\mathscr F\,\mathscr F E_TF=Z_NA_ME_TF.
 \tag{1.3}
\]

This does not use the fact that \(A_M\) commutes with \(\mathscr F\); it
only uses that the two adjacent copies of \(\mathscr F\) cancel. There is
also no reflection error between \(L_M+L_M^*\) and \(B_{T'}+B_{T'}^*\):
the former uses \(\tau_{\log d}\) and \(\tau_{-\log d}=V_{\log d}\),
while the latter is its compression to \(I_{T'}\).

### 1.2. Correct spaces

R170_837's notation mixes two objects called \(Z\):

- \(Z_N=S_N^{\rm ren}\) is the renormalized Müntz operator on the line;
- \(Z_T\), in §§7--8, is meant to denote the radical of the window.

To avoid a collision that becomes substantive in §8, we write

\[
 N_T:=\ker H_T\subset\mathcal P_T,\qquad
 N_T^\varepsilon=\{F\in N_T:JF=\varepsilon F\}.
 \tag{1.4}
\]

The arguments of (8.3) are not two vectors of the same space. The actual
type is

\[
 F\in N_T^\varepsilon\cap\mathcal Q_{\log},\qquad
 F_\delta\in\mathcal P_{T'}^\varepsilon\cap\operatorname{dom}H_{T'},
 \qquad T'=T+\delta,
 \tag{1.5}
\]

with

\[
 H_{T'}F_\delta=\lambda_\delta F_\delta,\qquad
 \lambda_\delta<0.
 \tag{1.6}
\]

Here \(E_TF\) is the zero extension of \(F\) from \(I_T\) to the line and
\(1_{C_\delta}F_\delta\) is the zero extension of its restriction to the
collar. R162_404 Lemma 1.2 proves that multiplying by indicators of
intervals is bounded on \(\mathcal Q_{\log}\); this is the correct
justification for the cutoffs.

### 1.3. The weak pairing missing in R170_837

A first-contact vector is only in the form domain. In general
\(A_ME_TF\in L^2\) is not available, and the terms with \(X\) in PC
cannot be paired separately. R170_813 already corrected exactly this
point for the exterior flux.

The robust definition of (0.1) must be

\[
 \mathfrak C_{M,N;T,\delta}(F,F_\delta)
 :=\left\langle A_ME_TF,
        Z_N^*1_{C_\delta}F_\delta\right\rangle_{
           \mathcal Q_{\log}',\mathcal Q_{\log}}.
 \tag{1.7}
\]

This requires proving that the adjoint of the renormalized operator
\(Z_N\) preserves \(\mathcal Q_{\log}\). For the raw finite comb this is
immediate; for the continuous counterterm the corresponding bound must be
cited or proved. R170_837 does not do this. On the Schwartz kernel, (1.7)
coincides with (0.1) and there is no problem.

The second line of R170_837 (8.4) can only be read as the pairing of the
**complete sum**

\[
 \{X,E_N\}-L_M^*E_N-J\widetilde H_{M,N}
 -\widetilde H_{M,N}\mathscr F+\mathcal P_{M,N}^{\rm pol}.
 \tag{1.8}
\]

Separating its five pairings on a first-contact vector is not justified.

### 1.4. Where the sign actually exists

R162_405 uses the real pairing. In a complex Hilbert space, the phrase
"has the sign of \(\lambda_\delta\)" needs a choice of phase. Let
\(G\in N_T^\varepsilon\) be the normalized limit of a subsequence of
ground states \(F_\delta\), and choose the phases so that

\[
 \langle F_\delta,E_TG\rangle>0,\qquad
 \langle F_\delta,E_TG\rangle\longrightarrow1.
 \tag{1.9}
\]

Then, and only for this selected \(G\),

\[
 \langle\xi_G^\delta,F_\delta|_{C_\delta}\rangle<0
 \quad\hbox{for small \(\delta\)}.
 \tag{1.10}
\]

For an arbitrary \(F\) of the radical, the overlap in (0.2) may be zero,
negative, or, without fixing a phase, complex. R170_837 (7.2) must
restrict its sign statement to (1.9).

## 2. Audit of renormalized PC

Set

\[
 Z_N=S_N-C_N^{\rm pol},\qquad K^Z_N=-[X,Z_N],\qquad
 \widetilde H_{M,N}=L_MZ_N-K^Z_N.
 \tag{2.1}
\]

The algebraic PC identity holds for every convolution operator that
preserves the kernel. Applied directly to \(Z_N\), it gives

\[
 Z_NA_M\mathscr F
 =\{X,E_N\}-L_M^*E_N-J\widetilde H_{M,N}
  -\widetilde H_{M,N}\mathscr F.
 \tag{2.2}
\]

This is precisely PC-ren of R161_003 §3.

The correction that R170_837 calls \(\mathcal P_{M,N}^{\rm pol}\) is
defined by

\[
\begin{aligned}
 \mathcal P_{M,N}^{\rm pol}
 ={}&\{X,E_N^{\rm pol}\}-L_M^*E_N^{\rm pol}
      -JH_{M,N}^{\rm pol}-H_{M,N}^{\rm pol}\mathscr F\\
    &-C_N^{\rm pol}A_M\mathscr F .
\end{aligned}
 \tag{2.3}
\]

But the right-hand side is exactly "PC for \(C_N^{\rm pol}\), minus PC
for \(C_N^{\rm pol}\)." Hence

\[
 \boxed{\mathcal P_{M,N}^{\rm pol}=0}
 \tag{2.4}
\]

on the common kernel. It is not an additional polar port. The polar
layer is still present, but it is inside
\(Z_N,E_N,K_N^Z,\widetilde H_{M,N}\). Keeping (2.3) expanded can serve
as a ledger, but it adds no term to (2.2).

With

\[
 K_N^S=-[X,S_N],\quad K_N^{\rm pol}=-[X,C_N^{\rm pol}],
 \quad H^{\rm raw}_{M,N}=L_MS_N-K_N^S,
 \tag{2.5}
\]

we have

\[
 K_N^S=K_N^Z+K_N^{\rm pol},\qquad
 H^{\rm raw}_{M,N}=\widetilde H_{M,N}+H_{M,N}^{\rm pol}.
 \tag{2.6}
\]

This last equality is what allows one to see again the cancellation of
raw coefficients. It must not be confused with (2.4).

## 3. The equality \(A_ME_TF=r_F+\xi_F^\delta\) in the collar

R170_837's claim under (8.4) is correct under precise hypotheses. By the
definition in R162_405,

\[
 \xi_F^\delta
 =\left.(\mathcal ME_TF-(B_{T'}+B_{T'}^*)E_TF-r_F)
   \right|_{C_\delta},
 \tag{3.1}
\]

where \(r_F\in\operatorname{span}\{e^{-t/2},e^{t/2}\}\) is extended by
the same exponential formula. If

\[
 M\ge e^{2T'},
 \tag{3.2}
\]

every translation that can act between two points of \(I_{T'}\) is
already in \(L_M+L_M^*\). The remaining translations do not see
\(E_TF\) inside \(I_{T'}\). Hence, in \(\mathcal Q_{\log}'(C_\delta)\),

\[
 \boxed{1_{C_\delta}A_ME_TF=r_F|_{C_\delta}+\xi_F^\delta.}
 \tag{3.3}
\]

This is not a pointwise equality for a general \(F\). The correct
reading is an equality of distributions or forms. If (3.2) does not
hold, the cutoff residual

\[
 \rho_M^\delta
 =1_{C_\delta}\bigl[(B_{T'}+B_{T'}^*)-(L_M+L_M^*)\bigr]E_TF
 \tag{3.4}
\]

appears. The decisive point is that (3.3) only identifies the restriction
of \(A_ME_TF\). It does not authorize

\[
 1_{C_\delta}Z_NA_ME_TF
 \stackrel{\rm false}{=}Z_N1_{C_\delta}(r_F+\xi_F^\delta),
 \tag{3.5}
\]

nor, even less, its replacement by \(\xi_F^\delta\). \(Z_N\) does not
commute with projection onto the collar.

## 4. Exact expansion of R170_837's datum

Let

\[
 g_{M,T}(F):=A_ME_TF,\qquad f_{\delta,c}:=1_{C_\delta}F_\delta.
 \tag{4.1}
\]

In regime (3.2), inserting \(Z_N=I+(Z_N-I)\) before using (3.3) gives

\[
\begin{aligned}
 \mathfrak C_{M,N;T,\delta}(F,F_\delta)
 & =\langle1_{C_\delta}g_{M,T}(F),f_{\delta,c}\rangle
   +\langle1_{C_\delta}(Z_N-I)g_{M,T}(F),f_{\delta,c}\rangle\\
 & =\langle\xi_F^\delta,f_{\delta,c}\rangle
   +\langle r_F,f_{\delta,c}\rangle
   +\langle1_{C_\delta}(Z_N-I)g_{M,T}(F),f_{\delta,c}\rangle.
\end{aligned}
 \tag{4.2}
\]

Identity R162_405 (2.2) converts only the first term:

\[
 \langle\xi_F^\delta,f_{\delta,c}\rangle
 =\lambda_\delta\langle F_\delta,E_TF\rangle.
 \tag{4.3}
\]

This gives (0.3)--(0.4). Equivalently, by duality,

\[
 \mathcal R^Z_{M,N;T,\delta}
 =\left\langle g_{M,T}(F),(Z_N^*-I)f_{\delta,c}\right\rangle.
 \tag{4.4}
\]

This formula exhibits the carrier incompatibility: the minimality test is
\(f_{\delta,c}\), while PC-ren changes it to \(Z_N^*f_{\delta,c}\).

### 4.1. Exact dependence on \(N\)

Since

\[
 Z_N-I=\sum_{2\le n\le N}n^{-1/2}\tau_{\log n}-C_N^{\rm pol},
 \tag{4.5}
\]

the residual is

\[
\begin{aligned}
 \mathcal R^Z_{M,N;T,\delta}
 ={}&\sum_{2\le n\le N}{1\over\sqrt n}
 \left\langle1_{C_\delta}\tau_{\log n}g_{M,T}(F),
                  f_{\delta,c}\right\rangle\\
 &-\left\langle1_{C_\delta}C_N^{\rm pol}g_{M,T}(F),
                  f_{\delta,c}\right\rangle.
\end{aligned}
 \tag{4.6}
\]

By (1.1), the first term evaluates \(g_{M,T}(F)\) at points shifted
outside the collar. The polar continuum also integrates data that are not
in the collar. Thus \(N\) is neither a decorative parameter nor does it
disappear after (3.3).

### 4.2. Exact dependence on \(M\)

For \(M\ge e^{2T'}\), the **restriction**
\(g_{M,T}(F)|_{C_\delta}\) stabilizes and satisfies (3.3). However,
\(g_{M,T}(F)\) outside \(I_{T'}\) keeps changing as \(M\) increases: new
translates of \(E_TF\) arise on the exterior. Since (4.6) reads exactly
those values, \(\mathcal R^Z\) and \(\mathfrak C\) do not stabilize in
\(M\) under assumption (3.2) alone.

Hence there is no canonical quantity in R170_837, independent of the
cutoffs, that can be identified with the sign of (4.3).

## 5. The cancellation \(\delta_\Lambda=0\)

For weights \(a(d)\), the raw defect is

\[
 \delta_a(k)=\sum_{d\mid k}a(d)-\log k,
 \qquad
 \mathcal D_a^{\le N}=\sum_{k\le N}{\delta_a(k)\over\sqrt k}
                         \tau_{\log k}.
 \tag{5.1}
\]

The claim of absence of low coefficients in
\(H_{M,N}^{a,\rm raw}=L_M^aS_N-K_N^S\) requires

\[
 M\ge N.
 \tag{5.2}
\]

R170_837 §8 only imposes \(M\ge e^{2T'}\); this does not imply (5.2) if
\(N\) is independent. For the same computation to cover the whole
compressed comb of the larger window and exhibit the Chebyshev
cancellation, the clean regime is

\[
 \boxed{N\ge\lceil e^{2T'}\rceil,\qquad M\ge N.}
 \tag{5.3}
\]

With (5.3),

\[
 \delta_\Lambda(k)=0\quad(k\le N)
 \tag{5.4}
\]

is exact. In the renormalized identity this is seen by expanding

\[
 H_{M,N}^{a,\rm raw}
 =\widetilde H_{M,N}^{a}+H_{M,N}^{a,\rm pol}
 \tag{5.5}
\]

before recombining. It is not an identity on the pairing
\(\mathfrak C\), and it cancels neither \(\mathcal R^{\rm Tate}\) nor
\(\mathcal R^Z\).

In particular, there are two facts on the same page but not in the same
slot:

```text
delta_Lambda=0      lives in the coefficients of the raw hyperbola
lambda_delta<0      lives in <xi_F^delta, F_delta|C_delta>
mathfrak C          contains <Z_N A_M E_TF, F_delta|C_delta>
```

The third line does not identify the first two.

## 6. Exact residual when attempting to reach \(R_LF\)

R162_406 Proposition 4.1 already carried out the requested separation. In
the right collar there is an injective map
\(\ell_L:\mathbb C^L\to C^\infty([T,\infty))\), with coefficients
independent of \(\Lambda\), such that

\[
 \xi_F^\delta=-\ell_L(R_LF)+\xi_F^{>L}
 \qquad\hbox{in }C_\delta^+.
 \tag{6.1}
\]

After extending by parity to the two collars,

\[
\boxed{
 \lambda_\delta\langle F_\delta,E_TF\rangle
 =-\langle\ell_L^\varepsilon(R_LF),f_{\delta,c}\rangle
  +\underbrace{\langle\xi_F^{>L},f_{\delta,c}\rangle}_
      {\mathcal R^{>L}_{T,\delta}(F,F_\delta)}.}
 \tag{6.2}
\]

This is the exact residual that prevents transporting the minimality sign
to \(R_LF\). It contains:

- the tail of Gamma moments \(j>L\);
- the Euler translates of values of \(F\) in the interior;
- the Tate vector \(r_F\);
- in the prime-power threshold regime, the reflected germ of the
  boundary;
- the unknown profile \(F_\delta|_{C_\delta}\) against which all of this
  is paired.

If one insists on using carrier (0.1), the complete identity is

\[
\boxed{
 \mathfrak C_{M,N;T,\delta}(F,F_\delta)
 =-\langle\ell_L^\varepsilon(R_LF),f_{\delta,c}\rangle
  +\mathcal R^{\rm tot}_{M,N,L;T,\delta}(F,F_\delta),}
 \tag{6.3}
\]

with

\[
 \mathcal R^{\rm tot}
 =\mathcal R^{>L}+\mathcal R^{\rm Tate}+\mathcal R^Z.
 \tag{6.4}
\]

There is no sign bound nor vanishing of (6.4). Moreover, (6.2) is a
single scalar inequality against an unknown collar profile; even if the
residuals of (0.4) were eliminated, it does not force the vanishing of
the vector \(R_LF\in\mathbb C^L\).

The parameter \(L\) does not even appear in definition (0.1). It enters
only when decomposing \(\xi_F^\delta\) as in (6.1). Hence (8.3) is not
yet a bridge to the detector of Paper 46.

## 7. Comparison with the corpus

### 7.1. R162_101

R162_101 proves that the inward variation has linear term exactly zero
and that right-hand minimality gives negative states in different
windows. Its Lemma 5 selects a limiting vector of the radical, but does
not give an equation on an arbitrary \(F\). R170_837 §7 is consistent
with this result.

### 7.2. R162_405

R162_405 proves exactly (4.3), characterizes right-hand minimality as
non-extendability, and proves in its Theorem 5.1 that the sign of the
collar does not restrict \(R_LF\). It also proves the covariant version

\[
 (\lambda_\delta-\lambda)\langle F_\delta,E_TF\rangle
 =\langle\xi_F^\delta,F_\delta|_{C_\delta}\rangle
 \tag{7.1}
\]

on windows at a positive level. This is the F1 falsifier that prevents
attributing the closure to the sign of (4.3).

### 7.3. R162_406: exact duplicate of the task announced in §8

R162_405 §7 proposed G1.5: apply the compressed Chebyshev identity to the
collar residual and decide whether \(\Lambda*1=\log\) connects it to
\(R_LF\). R162_406 carried out that task:

1. computed \(\xi_F^\delta\) in the three threshold regimes;
2. used \(B_{T'}^*Z_{T'}=K_{T'}\) and exactly localized the cancellation
   at the threshold atom;
3. obtained (6.1);
4. proved that in a finite collar the coefficients of the Gamma moments
   are independent of \(\Lambda\);
5. showed that the Euler coefficient \(-\zeta'/\zeta(s_m)\) only appears
   when pairing over the whole exterior \((T,\infty)\), not over
   \(C_\delta\);
6. concluded that the Chebyshev rewriting is an automorphism of the
   compressed algebra and adds no relation.

Hence the "new obligation" of R170_837's last paragraph has already been
decided negatively in the corpus. The omission of R162_406 from its
non-duplication audit changes the novelty verdict.

The homonymous operators must also be distinguished:

- \(Z_{T'}\) in R162_404--406 is the **raw compressed comb**, unipotent
  and invertible on \(I_{T'}\);
- \(Z_N\) in R170_837 is the **renormalized full-line operator**.

The compressed inverse and the identity \(B_{T'}^*Z_{T'}=K_{T'}\) cannot
be carried over to the \(Z_N\) of (0.1) without proof.

### 7.4. R162_407--408

R162_407 proves right-hand lower bounds, but they are covariant at the
spectral level and weight-blind; they do not deliver the margin needed by
(6.2). R162_408 identifies, via Schur--Feshbach, the signed scalar as a
collar energy \(Q_\delta(G,G)\) and proves that its scale depends on the
boundary germ of \(\xi_G\). It also rules out a universal inequality
between boundary jets and \(R_LG\). These later results make the
conclusion stronger: the residual of (6.2) is not a pending bookkeeping
detail.

## 8. Specific corrections to R170_837

1. In §7.2, replace "the pairing has the sign of
   \(\lambda_\delta\)" with the normalized, phase-fixed version of
   (1.9)--(1.10).
2. In §8, replace \(F\in Z_T\) with
   \(F\in N_T^\varepsilon\cap\mathcal Q_{\log}\) and declare the type of
   \(F_\delta\) from (1.5)--(1.6).
3. Define (8.3) weakly via (1.7), or explicitly restrict the
   construction to the Schwartz kernel. Do not separately expand the
   terms with \(X\) in the form domain.
4. Record that \(\mathcal P_{M,N}^{\rm pol}=0\) on the kernel by PC
   applied to the polar counterterm. The polar layer remains inside the
   renormalized operators.
5. Keep \(M\ge e^{2T'}\) for (3.3). Add \(M\ge N\) for the claim
   \(\delta_\Lambda(k)=0\), and use (5.3) if one wants to cover the whole
   comb of the larger window.
6. Replace "(8.3) contains minimality" with expansion (0.3)--(0.4).
7. Replace "first carrier" with "PC pairing filtered against a state of
   the larger window." It is not new relative to R162_405--406 and does
   not literally preserve the signed scalar.
8. Add (6.2)--(6.4) as the ledger of the residual separating the sign
   from \(R_LF\).
9. Record R162_406 as a prior decision on G1.5 and R162_407--408 as
   relevant subsequent corpus.

## 9. Corrected ledger

```text
§7.1: interior variation with zero linear term                PROVED
§7.2: collar identity between T and T+delta                   PROVED
sign for every F of the radical                                FALSE
sign for the limit G, normalized and phase-fixed                PROVED
typing F in N_T and F_delta in P_(T+delta)                      CORRECTABLE

Fcal^2=I and the PC-ren step to Z_N A_M E_TF                    CORRECT
tau/V/reflection convention                                     CORRECT
PC-ren for Z_N on the common kernel                              PROVED
P_pol as an additional nonzero block                             FALSE / P_pol=0
extension of (8.3) to the first-contact domain                   NOT PROVED IN R170_837

A_M E_TF=r_F+xi_F^delta in the collar                            PROVED IN Q' IF M>=e^(2T')
passing Z_N through the restriction to the collar                 FALSE
(8.3) = signed minimality pairing                                FALSE
exact residual Tate + (Z_N-I)                                    PROVED, (0.3)--(0.4)
stabilization in M of the complete form                           FALSE
dependence on N                                                   EXPLICIT, (4.6)

delta_Lambda(k)=0                                                 PROVED IF M>=N
clean joint scale                                                 N>=e^(2T'), M>=N
delta_Lambda=0 and lambda_delta<0 in the same scalar               FALSE

separation xi=-ell_L(R_LF)+xi^(>L)                                ALREADY PROVED IN R162_406
residual preventing the sign on R_LF                              xi^(>L), plus Tate and R^Z in (8.3)
Chebyshev comparison of G1.5                                      ALREADY DONE / NO-GO R162_406
mathematical novelty of (8.3)                                      NO / REPACKAGED
transport of the sign to R_LF with these data                      NO-GO
D                                                                 OPEN
```

The correction does not invalidate the PC identity nor the collar
identity. It invalidates the claim that (8.3) already makes them coexist
in the same signed carrier. The step that is still missing would have to
annihilate or sign-control the total residual (6.4). R162_406--408 show
that such control is not obtained from PC, Chebyshev, and minimality
alone.
