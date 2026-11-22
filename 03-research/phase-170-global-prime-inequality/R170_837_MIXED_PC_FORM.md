# R170_837 — Mixed PC form: maximal construction, exact incompatibility, and two-window datum

Continuation of R170_835--836. Status: the finite
difference--sum polarization is built and expanded in both orientations.
It is exactly the mixed Green form already isolated in R161_056--057,
with the concomitant support audited in R161_063--065. It cannot have at
once \(+D_\Delta\), \(-\mathcal S_{\rm can}\), and a literally common
residual as identities obtained only by polarizing PC. Three
incompatibilities are proved: common residual, test slot, and
minimality. The next minimal datum is necessarily a form between two
windows; it is constructed at the end as a finite PC--collar pairing.

Paper 46 is not modified, nor is D proved.

## 0. Verdict

Set, on the regular kernel and with the polar renormalization included,

\[
 Z_N=S_N^{\rm ren},\qquad
 E_N=Z_N\mathscr F-JZ_N,\qquad
 C_N=Z_N\mathscr F+JZ_N,
 \tag{0.1}
\]

\[
 K_N=-[X,Z_N],\qquad
 \mathcal J_N=K_N\mathscr F-JK_N
              =Z_N\mathcal M\mathscr F-\{X,C_N\}.
 \tag{0.2}
\]

When the Euler cutoff \(M\) is introduced, we will always use the
renormalized hyperbola defined by the identity

\[
 \widetilde H_{M,N}:=L_MZ_N-K_N.                     \tag{0.2a}
\]

This definition keeps the polar continuum inside the equality and avoids
identifying it with the crude tail \(H_{M,N}=L_MS_N-K_N^{\rm raw}\).

For a sesquilinear form \(q\), we write

\[
 \operatorname{Herm}_{F,G}q(F,G)
 ={1\over2}\bigl(q(F,G)+\overline{q(G,F)}\bigr).
 \tag{0.3}
\]

The only direct polarization that puts the difference \(E_N\) in one slot
and the jet of the complementary sum \(C_N\) in the other is, given a
linear test \(T_L\),

\[
 \boxed{
 \mathfrak M_{N}^{\varepsilon}[T_L](F,G)
 :=\operatorname{Herm}_{F,G}
 \langle E_NF,\mathcal J_NT_LG\rangle,
 \qquad F,G\in Z_\varepsilon .}
 \tag{0.4}
\]

To try to see the moments of Paper 46 one must take

\[
 T_L=S_L:=R_L^*R_L+JR_L^*R_LJ.                     \tag{0.5}
\]

Form (0.4) is finite, oriented, and derived, not postulated. It
preserves the two Poisson histories, the polar continuum, and, upon
physical compression, the two Tate scalars and the four support blocks.
It also admits an exact Euler--hyperbola rewriting. But the actual
expansions are

\[
 \mathfrak M_N^\varepsilon[S_L]
 =-\mathfrak S^{\rm phys}_N[\,I,S_L\,]
   +\mathfrak R_N^{\rm H}[S_L],                       \tag{0.6}
\]

and

\[
 \mathfrak M_N^\varepsilon[S_L]
 =\mathfrak E_{M,N,L}^{\rm mix},                     \tag{0.7}
\]

where (0.6) has a **crossed Hardy metric** between the port of \(F\) and
the port of \(S_LG\), while (0.7) is the indefinite concomitant support of
R161_057 and R161_065. In (0.7)

\[
 D_\Delta=R_L^*(I-D_{N,L})R_L                         \tag{0.8}
\]

does not appear as the leading term. The collar identity that produces
(0.8) uses a different slot, \(G_LF=R_L^*R_LF\), and not the conjugated
port that produces \(\mathcal S_{\rm can}\).

More decisively, if forms
\(\mathfrak B_{M,N,L}^\varepsilon\) and **the same** residual
\(\mathfrak R_{M,N,L}^\varepsilon\) existed with

\[
 \mathfrak B=D_\Delta+\mathfrak R,
 \qquad
 \mathfrak B=-\mathcal S_{\rm can}+\mathfrak R,
 \tag{0.9}
\]

then, subtracting the two equalities,

\[
 \boxed{D_\Delta+\mathcal S_{\rm can}=0\quad\hbox{in }Z_\varepsilon.}
 \tag{0.10}
\]

Since both forms are nonnegative and \(D_\Delta\succ0\) when
\(R_L|_{Z_\varepsilon}\) is injective, (0.10) implies
\(Z_\varepsilon=0\). Hence (0.9) is not a pending bookkeeping identity:
**it is already the complete vanishing theorem**. It cannot be deduced
from an algebraic polarization that holds in models with a nontrivial
first contact.

Minimality introduces another type incompatibility. A form on
\(Z_T\times Z_T\) at a fixed window only uses \(H_T\ge0\) and
\(H_TF=0\). The right-hand information of the first contact lives in a
second window and in a second vector \(F_\delta\):

\[
 \lambda_\delta\langle F_\delta,E_TF\rangle
 =\langle\xi_F^\delta,F_\delta|_{C_\delta}\rangle,
 \qquad C_\delta=I_{T+\delta}\setminus I_T .          \tag{0.11}
\]

Thus, no nontrivial minimality term can be added to (0.4) without
changing its type. The next minimal piece must be a form between
\(Z_T\) and the states at \(T+\delta\), not another form on \(Z_T\).

## 1. Non-duplication audit

### 1.1. R161_052--081

The complete sequence was reviewed. The relevant point of each note is:

| Note | Result restricting the current construction |
|---|---|
| R161_052 | The finite unitary coligation is valid; its tangent derives the Poisson difference and has the average orientation. |
| R161_053 | The source lift is canonical; its covariant tangent still has the average orientation. |
| R161_054 | The two-orientation squeeze requires both to compare the same port and the same central metric. |
| R161_055 | The order-zero metric equality holds on a graph diagonal; it does not control the tangent nor the boundary layer. |
| R161_056 | \(E_N\) derives to \(U_N+V_N\); the critical jet \(U_N-V_N\) derives from the sum \(C_N\). |
| R161_057 | The mixed \(E_N\)--\(C_N\) form has an exact decomposition into four ports; the wrong-side reciprocity remains. |
| R161_058 | The double commutator is positive, but its vanishing is equivalent to preserving the radical. |
| R161_059 | The compression of a globally commuting pair produces crossed exterior products, not a square. |
| R161_060 | Substituting PC literally into those products reconstructs the exterior correlation; it neither signs it nor annihilates it. |
| R161_061 | The Tate symplectic form is alternating and its diagonal is always zero. |
| R161_062 | The Hermitian power does have a diagonal, but requires the correct placement of the collar. |
| R161_063 | The diagonal anticommutator uses \(RZ_NF\), not the proved collar \(\Tau PZ_N^*g(F)\); the type is incorrect. |
| R161_064 | The correctly typed mixed power reduces to the support concomitant. |
| R161_065 | That concomitant is exactly \(\langle g,[P,S]w\rangle\), already audited and indefinite. |
| R161_066 | The oriented Laurent vanishing attempt was formulated. |
| R161_067 | The Laurent attempt is circular or shifts the conclusion to an unproved convergence. |
| R161_068 | The faithful Gamma--Euler energy is proved, but radicality does not annihilate it. |
| R161_069 | A faithful factorization through the null operator would already be the closure; the first formulation mixed global and compressed kernels. |
| R161_070 | The correctly typed finite detector and the exact collar are obtained. |
| R161_071 | The test \(S_LF\) gives the balance \(0=2c_{N,L}+Q_{N,L}\). |
| R161_072 | That balance recomposes the original equation and works for arbitrary positive weights. |
| R161_073 | The stabilized inverse and the matrix kernel test are legitimate, but a posteriori. |
| R161_074 | The residual certificate gives a rigorous upper bound; it does not build the strict margin. |
| R161_075 | The \(L^2\), distributional, and meromorphic carriers cannot be identified without a limit law. |
| R161_076 | The physical Weil operator stabilizes locally; the Poisson composition examines a moving region. |
| R161_077 | The renormalized continuum is canonical only modulo a Tate line. |
| R161_078 | The renormalized tail converges on smooth primitive sources, without a vanishing law. |
| R161_079 | Convergence extends weakly to \(L^2\) sources, but not to a Hardy metric. |
| R161_080 | The Gamma residues escape the weak topology; extracting them requires two scales. |
| R161_081 | \(Q_{N,L}<0\) on eigenvectors with \(\lambda\ge0\); any sign not using an additional mode of contact fails F1. |

In particular, (0.4) is not a new form under another name: it is the
sesquilinear polarization of the object of R161_056--057. R161_063--065
already prove that changing it to a Hermitian power, placing the collar a
posteriori, or taking the support concomitant does not create a second
law.

### 1.2. R162_2302

The renormalized weak limit vanishes for **every** primitive source by
the functional equation. Hence it does not distinguish the first
contact. The only finite appearance of \(\Lambda*1=\log\) is in the
cross term of the product orientation; taking the weak limit first erases
precisely that defect. It is also verified that invariance under the
Volterra operator is equivalent to triviality of the radical. Neither of
these two facts will be used as though it were a new law.

### 1.3. Paper 46

The following are used literally:

\[
 S_NA_M\mathscr F
 =\{X,E_N\}-L_M^*E_N-JH_{M,N}-H_{M,N}\mathscr F,       \tag{1.1}
\]

\[
 H_{M,N}=\sum_{k>N}{h_{M,N}(k)\over\sqrt k}\tau_{\log k}
 \quad(M\ge N),                                      \tag{1.2}
\]

\[
 R_LB_N=D_{N,L}R_L-\mathcal E_{N,L},                 \tag{1.3}
\]

and

\[
 D_\Delta=R_L^*(I-D_{N,L})R_L
 \succeq(1-q_0)R_L^*R_L.                             \tag{1.4}
\]

Paper 46 further notes that the square of (1.1) is invariant under
reversal of the Weil sign and that the collar balance contains no new
sign. The Vanishing Problem expressly requires arithmetic, orientation,
and minimality in the decisive step.

### 1.4. R170_823--836

| Note | Relevant restriction |
|---|---|
| R170_823--826 | Multiscale PC preserves all blocks and smooths the collars; compactness does not give a sign. |
| R170_827--828 | The matrix compression on the radical is exact; two inequalities in the same functional are still missing. |
| R170_829--830 | \(D_\Delta\) admits no interior lift; an exterior lift must satisfy a new Green equation. |
| R170_831--833 | The Gamma--Euler response of the exterior columns is computed, but the Tate port on columns is not determined. |
| R170_834 | The Hardy port produced by the source is canonical; its transfer to arbitrary columns is not. |
| R170_835 | The column Gram matrix and the residuals are explicit; the source port does not factor universally through finite \(R_L\). |
| R170_836 | The mixed form with a common residual was a specification, not a construction. |

The joint audit leaves exactly two distinct carriers: the moment test
that produces (1.4), and the product port that produces
\(\mathcal S_{\rm can}\). Form (0.4) does not identify them.

## 2. Exact construction of the mixed polarization

### 2.1. Difference, sum, and jet

Let

\[
 a_N(F)=Z_N\mathscr FF,\qquad d_N(F)=JZ_NF.            \tag{2.1}
\]

Then

\[
 e_N(F):=a_N(F)-d_N(F)=E_NF,\qquad
 c_N(F):=a_N(F)+d_N(F)=C_NF.                          \tag{2.2}
\]

The two exact differentiations are

\[
 K_N\mathscr F+JK_N=Z_N\mathcal M\mathscr F-\{X,E_N\},
 \tag{2.3}
\]

\[
 \boxed{K_N\mathscr F-JK_N
 =Z_N\mathcal M\mathscr F-\{X,C_N\}.}               \tag{2.4}
\]

The first is the tangent of the difference and has the average
orientation. The second is the critical jet. That is why (0.4), and not a
diagonal form in \(E_N\), is the maximal oriented polarization obtained
from these data.

This claim must be distinguished from a "polarization of zero." The two
oriented PC equations can be written as operator equations. To show the
polar part without abbreviating it, set

\[
 C_N^{\rm pol}:=S_N-Z_N,\qquad
 E_N^{\rm pol}:=C_N^{\rm pol}\mathscr F-JC_N^{\rm pol},
 \tag{2.5a}
\]

\[
 K_N^{\rm pol}:=-[X,C_N^{\rm pol}],\qquad
 H_{M,N}^{\rm pol}:=L_MC_N^{\rm pol}-K_N^{\rm pol},
 \tag{2.5b}
\]

and define the fully explicit block

\[
\begin{aligned}
 \mathcal P_{M,N}^{\rm pol}:={}&
 \{X,E_N^{\rm pol}\}-L_M^*E_N^{\rm pol}
 -JH_{M,N}^{\rm pol}-H_{M,N}^{\rm pol}\mathscr F\\
 &-C_N^{\rm pol}A_M\mathscr F .                       \tag{2.5c}
\end{aligned}
\]

The raw PC for \(S_N\), minus the same linear decomposition for
\(C_N^{\rm pol}\), gives

\[
 \mathsf{PC}_{M,N}^{+}:=
 Z_NA_M\mathscr F-
 (\{X,E_N\}-L_M^*E_N-J\widetilde H_{M,N}
                  -\widetilde H_{M,N}\mathscr F
                  +\mathcal P_{M,N}^{\rm pol})=0.       \tag{2.5d}
\]

and its reflected copy \(\mathsf{PC}_{M,N}^{-}=0\). Any literal
polarization of the two complete sides has the form

\[
 \operatorname{Herm}\langle U\mathsf{PC}_{M,N}^{+}F,
                                V\mathsf{PC}_{M,N}^{-}G\rangle=0.
                                                               \tag{2.5e}
\]

By itself it cannot produce a positive leading term. To obtain a nonzero
form one must preserve an order before recombining the two sides. The
canonical order fixed by R161_056 is exactly (0.4): the Poisson
difference in one slot and the derivative of the sum in the other. Moving
other terms to left or right only changes what is called "leading" and
what is called "residual"; it does not constitute a second identity.
This is the logical reason why demanding a common residual has content
and cannot be satisfied by renaming terms.

In a sector \(JF=\varepsilon F\), \(S_L\) preserves parity. Parity is not
used to erase any tail: it only fixes the order of the two Tate ports
upon compression.

### 2.2. The polar continuum and the two Tate ports

The notation \(Z_N=S_N^{\rm ren}\) means that the polar continuum is
subtracted **before** forming \(E_N,C_N,K_N\). For a first-contact
source,

\[
 A_MF=r_F+\ell_F,
 \qquad r_F\in\operatorname{span}\{e^{-t/2},e^{t/2}\},
 \qquad \ell_F=Q_TA_MF,                                  \tag{2.5}
\]

and the two compressed orientations are

\[
 P_TS_N^{\rm ren}\ell_F
 =\Delta_{N,T}^R\ell_F-e^{-t/2}a_-(\ell_F),            \tag{2.6}
\]

\[
 P_TJS_N^{\rm ren}J\ell_F
 =\Delta_{N,T}^L\ell_F-e^{t/2}a_+(\ell_F),             \tag{2.7}
\]

\[
 a_-(\ell)=\int_{-\infty}^{-T}e^{y/2}\ell(y)\,dy,
 \qquad
 a_+(\ell)=\int_T^\infty e^{-y/2}\ell(y)\,dy.        \tag{2.8}
\]

Thus, expanding (0.4) after compression literally preserves
\(\Delta^R,\Delta^L,a_-,a_+\). \(a_\pm\) is not replaced by zero, by
complete moments, nor by an arbitrary extension of the Tate vector. The
Hardy correction of those ports is the source-canonical one of R161_009
and R161_015. This does not turn it into a functional on the Gamma
columns of R170_829, as R170_834 proves.

## 3. Finite Hardy reading: what the complementary sum actually produces

### 3.1. Polarized Green

For \(F,G\) in the regular kernel, the elementary identity

\[
 \boxed{
 \operatorname{Herm}_{F,G}\langle e_N(F),Xc_N(G)\rangle
 =\operatorname{Herm}_{F,G}
 \bigl(\langle a_N(F),Xa_N(G)\rangle
       -\langle d_N(F),Xd_N(G)\rangle\bigr)}          \tag{3.1}
\]

is obtained by expanding the four pairs. The cross terms cancel only
after Hermitization. This is the sesquilinear version of R161_042 and
uses no limits.

Let \(P_-,P_0,P_+\) be the projections onto
\((-\infty,-T),(-T,T),(T,\infty)\). Define

\[
\begin{aligned}
 \mathfrak S_N^{\rm phys}(F,G)
 :={}&\operatorname{Herm}_{F,G}\{
 \langle P_+a_N(F),(X-T)P_+a_N(G)\rangle\\
 &\hspace{37mm}+
 \langle P_-d_N(F),(-X-T)P_-d_N(G)\rangle\},          \tag{3.2}
\end{aligned}
\]

\[
\begin{aligned}
 \mathfrak S_N^{\rm wrong}(F,G)
 :={}&\operatorname{Herm}_{F,G}\{
 \langle P_-a_N(F),(-X-T)P_-a_N(G)\rangle\\
 &\hspace{37mm}+
 \langle P_+d_N(F),(X-T)P_+d_N(G)\rangle\},           \tag{3.3}
\end{aligned}
\]

\[
\begin{aligned}
 \Phi_N(F,G):={}&\operatorname{Herm}_{F,G}\{
 \langle P_+a_N(F),P_+a_N(G)\rangle
 +\langle P_-d_N(F),P_-d_N(G)\rangle\\
 &-\langle P_-a_N(F),P_-a_N(G)\rangle
 -\langle P_+d_N(F),P_+d_N(G)\rangle\},              \tag{3.4}
\end{aligned}
\]

and

\[
 \mathfrak G_{0,N}(F,G)=\operatorname{Herm}_{F,G}
 \{\langle P_0a_N(F),XP_0a_N(G)\rangle
  -\langle P_0d_N(F),XP_0d_N(G)\rangle\}.             \tag{3.5}
\]

Separating the three supports in (3.1) gives exactly

\[
 \boxed{
 \operatorname{Herm}\langle E_NF,XC_NG\rangle
 =\mathfrak S_N^{\rm phys}(F,G)
  -\mathfrak S_N^{\rm wrong}(F,G)
  +T\Phi_N(F,G)+\mathfrak G_{0,N}(F,G).}              \tag{3.6}
\]

On the diagonal, the first two forms of (3.2)--(3.3) are nonnegative.
Neither global unitarity nor the central order-zero equality annihilates
\(\mathfrak S_N^{\rm wrong}\), \(\Phi_N\), or
\(\mathfrak G_{0,N}\).

### 3.2. Complete expansion of the constructed form

From (0.2),

\[
\begin{aligned}
 \mathfrak M_N^\varepsilon[T_L](F,G)
 ={}&\operatorname{Herm}\langle E_NF,
             Z_N\mathcal M\mathscr FT_LG\rangle\\
 &-\operatorname{Herm}\langle E_NF,XC_NT_LG\rangle
  -\operatorname{Herm}\langle E_NF,C_NXT_LG\rangle . \tag{3.7}
\end{aligned}
\]

Applying (3.6) to the middle term,

\[
 \boxed{
 \mathfrak M_N^\varepsilon[T_L]
 =-\mathfrak S_N^{\rm phys}[I,T_L]
   +\mathfrak R_N^{\rm H}[T_L],}                     \tag{3.8}
\]

where the residual, literally and without separate estimates, is

\[
\begin{aligned}
 \mathfrak R_N^{\rm H}[T_L](F,G)
 :={}&\operatorname{Herm}\langle E_NF,
             Z_N\mathcal M\mathscr FT_LG\rangle
 -\operatorname{Herm}\langle E_NF,C_NXT_LG\rangle\\
 &+\mathfrak S_N^{\rm wrong}[I,T_L](F,G)
 -T\Phi_N[I,T_L](F,G)-\mathfrak G_{0,N}[I,T_L](F,G).
                                                               \tag{3.9}
\end{aligned}
\]

The notation \([I,T_L]\) means the cross polarization with \(F\) in the
first slot and \(T_LG\) in the second, followed by (0.3). When refining
the \(P_0\) block into primitive and Tate, (2.6)--(2.8) are terms of
(3.9); they have not been removed. The Tate term generated by
\(XT_LG\) has opposite parity in the placement of R161_043 and vanishes
when it appears literally. The rest of the two Tate ports remains.

The leading term of (3.8) is positive on the diagonal only when
\(T_L=I\). For \(T_L=S_L\) it is a cross correlation:

\[
 \mathfrak S_N^{\rm phys}[I,S_L](F,F),                 \tag{3.10}
\]

not the norm \(\mathfrak S_N^{\rm phys}(F,F)\). Even for
\(T_L=I\), identifying its limit with \(\mathcal S_{\rm can}\) requires
the common-port theorem that R161_054--055 leave open. Hence (3.8) does
not prove

\[
 \mathfrak M=-\mathcal S_{\rm can}+\mathfrak R^{\rm H}.
 \tag{3.11}
\]

It proves a finite version with the histories of (2.1), the four blocks,
and all the terms of (3.9).

## 4. Euler--hyperbola reading: why \(D_\Delta\) does not appear

Recall the renormalized hyperbola (0.2a), defined so that the polar part
is not lost,

\[
 \widetilde H_{M,N}:=L_MZ_N-K_N.                     \tag{4.1}
\]

Then

\[
 \mathcal J_N
 =(L_MZ_N-\widetilde H_{M,N})\mathscr F
  -J(L_MZ_N-\widetilde H_{M,N}),                     \tag{4.2}
\]

and the second exact expansion of (0.4) is

\[
\boxed{
\begin{aligned}
 \mathfrak M_N^\varepsilon[T_L](F,G)
 ={}&\operatorname{Herm}\langle E_NF,
       (L_MZ_N\mathscr F-JL_MZ_N)T_LG\rangle\\
 &-\operatorname{Herm}\langle E_NF,
       (\widetilde H_{M,N}\mathscr F-J\widetilde H_{M,N})T_LG
       \rangle .                                             \tag{4.3}
\end{aligned}}
\]

We denote by \(\mathfrak E_{M,N,L}^{\rm mix}\) the right-hand side of
(4.3) when \(T_L=S_L\). With this definition, (0.7) is exactly (4.3),
not the introduction of an additional residual.

Here are the two orientations of \(H_{M,N}\), the polar correction
contained in (4.1), \(E_N\), and, after compression, the collars of
(2.6)--(2.8). This is the complete Euler reading of the mixed form.

The detector of Paper 46 instead comes from

\[
 R_LB_N=D_{N,L}R_L-\mathcal E_{N,L}.                 \tag{4.4}
\]

Its polarization gives

\[
\begin{aligned}
 \langle F,D_\Delta G\rangle
 ={}&\langle R_LF,R_LG\rangle
 -\operatorname{Herm}_{F,G}\langle R_LF,R_LB_NG\rangle\\
 &-\operatorname{Herm}_{F,G}\langle R_LF,\mathcal E_{N,L}G\rangle.
                                                               \tag{4.5}
\end{aligned}
\]

The slots of (4.3) and (4.5) are distinct:

```text
E--C form:        E_N F       against  (K_N Fcal-JK_N) T_L G
Gamma collar:     R_L F       against  R_L B_N G and E_(N,L)G
Hardy port:       G_bi F      against  W_bi G_bi G
```

There is no identity in PC that turns the first line into the second or
the third. Choosing \(T_L=S_L\) brings in the moment test, but turns
(3.2) into the port of \(S_LG\). Choosing \(T_L=I\) preserves the port of
\(G\), but removes the mechanism that produces \(R_L^*R_L\). This is the
exact slot incompatibility.

Adding (4.5) to (4.3) by definition would produce a form with
\(+D_\Delta\), but it would no longer be a polarization derived from the
two PC equations; and its Hardy residual would change by \(D_\Delta\).
That violates precisely the common-residual condition.

## 5. Common-residual incompatibility theorem

**Theorem 5.1.** Let \(Z_\varepsilon\) be a supposed first-contact
radical and choose \(L\) so that \(R_L|_{Z_\varepsilon}\) is injective.
Suppose there exist sesquilinear forms
\(\mathfrak B,\mathfrak R\) on \(Z_\varepsilon\) such that

\[
 \mathfrak B(F,G)=\langle F,D_\Delta G\rangle+
                    \mathfrak R(F,G),                \tag{5.1}
\]

\[
 \mathfrak B(F,G)=-\langle W_{\rm bi}^{1/2}\mathcal G_{\rm bi}F,
                           W_{\rm bi}^{1/2}\mathcal G_{\rm bi}G\rangle
                    +\mathfrak R(F,G).                \tag{5.2}
\]

Then \(Z_\varepsilon=\{0\}\).

**Proof.** Subtracting (5.2) from (5.1) gives

\[
 \langle F,D_\Delta G\rangle
 +\langle W_{\rm bi}^{1/2}\mathcal G_{\rm bi}F,
          W_{\rm bi}^{1/2}\mathcal G_{\rm bi}G\rangle=0.
 \tag{5.3}
\]

On the diagonal,

\[
 \|(I-D_{N,L})^{1/2}R_LF\|^2
 +\|W_{\rm bi}^{1/2}\mathcal G_{\rm bi}F\|^2=0.      \tag{5.4}
\]

Both terms are nonnegative. Since \(I-D_{N,L}\succ0\), the first
annihilates \(R_LF\), and the injectivity of \(R_L|_{Z_\varepsilon}\)
gives \(F=0\).
∎

The theorem does not say that the closure is impossible. It says that
constructing (5.1)--(5.2) with a common residual **is exactly
constructing the closure**. It cannot be presented as an intermediate
formal identity nor verified separately by estimating two errors. The
literalness of the residual is the part carrying all the mathematical
force.

## 6. Exact entry of \(\Lambda*1=\log\) and the falsifying-weight test

Let \(a(d)\) be a weight system and

\[
 L_M^a=\sum_{d\le M}{a(d)\over\sqrt d}\tau_{\log d},
 \qquad H_{M,N}^a=L_M^aS_N-K_N.                       \tag{6.1}
\]

For \(k\le N\le M\), the coefficient of \(H_{M,N}^a\) is

\[
 \delta_a(k):=\sum_{d\mid k}a(d)-\log k.              \tag{6.2}
\]

Set

\[
 \mathcal D_a^{\le N}
 =\sum_{k\le N}{\delta_a(k)\over\sqrt k}\tau_{\log k}.
 \tag{6.3}
\]

Then

\[
 H_{M,N}^a=\mathcal D_a^{\le N}+H_{M,N}^{a,>N}.        \tag{6.4}
\]

In the PC identity, the interior defect appears literally as

\[
 \boxed{-J\mathcal D_a^{\le N}
        -\mathcal D_a^{\le N}\mathscr F.}             \tag{6.5}
\]

\(L_M^{a*}E_N\), the corresponding polar block, and the tail \(k>N\) also
change. Term (6.5) is the distinguished block because it is the only one
supported on \(k\le N\) and it vanishes coefficient by coefficient for
\(a=\Lambda\).

For \(a=\Lambda\), (6.2) is zero for each \(k\le N\), by
\(\Lambda*1=\log\), and (6.5) disappears coefficient by coefficient. For
\(a=\Lambda\mathbf1_{d\ge5}\), an isolated translation, Type I weights,
or a finite modification, (6.5) reappears. This is the exact
cancellation required; it is not a bound.

There is, however, a second crucial fact. The mixed jet (0.2) is defined
with \(K_N\), which does not depend on \(a\). Substituting

\[
 K_N=L_M^aS_N-H_{M,N}^a,                               \tag{6.6}
\]

the variation of \(L_M^aS_N\) cancels exactly against the complete
variation of \(H_{M,N}^a\). Hence

\[
 \boxed{\mathfrak M_N^\varepsilon[T_L]
 \text{ is independent of }a
 \text{ after the exact recombination (6.6).}}   \tag{6.7}
\]

This explains why R161_060 and R161_065 recover a tautology: the full
mixed polarization returns to the Chebyshev jet \(K_N\) and forgets which
weights were used to factor it.

The arithmetic is load-bearing only if the projection of interior
coefficients

\[
 \mathbf P_{\le N}^{\rm coeff}H_{M,N}^\Lambda=0.       \tag{6.8}
\]

is used **before** (6.6). That projection is not a Hilbert operation on
the Hardy port; it is an operation on the finite algebra of
translations. To record the falsifier without hiding it, define the
monitor

\[
\boxed{
 \mathfrak A_{a;M,N,L}^\varepsilon(F,G)
 :=-\operatorname{Herm}_{F,G}
 \langle E_NF,
 (J\mathcal D_a^{\le N}
  +\mathcal D_a^{\le N}\mathscr F)S_LG\rangle .}      \tag{6.9}
\]

Then

\[
 \mathfrak A_{\Lambda;M,N,L}^\varepsilon=0             \tag{6.10}
\]

exactly, while for falsifying weights (6.9) does not vanish in general.
The monitor gives no sign when it equals zero; it only prevents a
weight-blind proof from being announced as arithmetic. A form satisfying
requirement 4 must use (6.8) to transform a residual, not merely rewrite
(6.6).

## 7. Minimality: incompatibility with a fixed-window form

### 7.1. The interior derivative is zero

We use here the exact displacement identity of R162_101, not a formal
derivation of the Euler jumps.

Let \(T_*\) be the first contact and \(F\in Z_{T_*}\). For every
admissible curve \(\gamma(s)\in\mathcal P_{T_*}\),

\[
 \mathfrak a_{T_*}(\gamma(s))
 =\mathfrak a_{T_*}(\gamma(s)-F).                     \tag{7.1}
\]

In particular, every transport toward a smaller window, corrected to
remain primitive, has linear term exactly zero. There is no boundary
trace that could be added to (0.4); in the available domain not even
pointwise traces of \(F\) at \(\pm T\) exist.

The Hardy slope

\[
 -N_{+,F}'(0+)=2\int_T^\infty(t-T)|\mathcal G_+F(t)|^2dt
 \tag{7.2}
\]

is a displacement derivative of the **exterior gauge**. It is not the
derivative of the spectral window \(T\mapsto H_T\). Identifying them
would be precisely the inverse law one wants to prove.

### 7.2. The right-hand information uses a different window

The correct realization of right-hand minimality is the collar identity
of R162_405.

For \(T'=T_*+\delta\), let \(F_\delta\) be a negative ground state,

\[
 H_{T'}F_\delta=\lambda_\delta F_\delta,
 \qquad \lambda_\delta<0.                              \tag{7.3}
\]

Let \(E_TF\) be the zero extension and let
\(C_\delta=I_{T'}\setminus I_{T_*}\). The exact exterior residual is

\[
 \xi_F^\delta
 =\left.\bigl(\mathcal MF-(B_{T'}+B_{T'}^*)F-r_F\bigr)
   \right|_{C_\delta}.                                \tag{7.4}
\]

The collar identity between windows is

\[
 \boxed{
 \lambda_\delta\langle F_\delta,E_TF\rangle
 =\langle\xi_F^\delta,F_\delta|_{C_\delta}\rangle.}  \tag{7.5}
\]

This is the only signed right-hand minimality input available: for the
contact vector selected as the limit from the right, the pairing in (7.5)
has the sign of \(\lambda_\delta\). But the second argument belongs to
\(\mathcal P_{T+\delta}\), not to \(Z_T\), and its collar profile is not
determined by \(F\). Dividing by \(\delta\) or by \(\lambda_\delta\) does
not produce a form in \(F\): it only normalizes (7.5).

Hence:

\[
 \boxed{
 \text{a form }\mathfrak B_{M,N,L}^\varepsilon:Z_T\times Z_T\to\mathbb C
 \text{ cannot contain right-hand minimality nontrivially}.}
 \tag{7.6}
\]

To do so one must change the type to a form between two windows. This
also explains the spectral falsifier of R161_081: every term depending
only on \(H_TF=0\) and \(H_T\ge0\) transports to modes that are not first
contacts.

## 8. Next minimal datum constructed

The construction above shows that the next datum must simultaneously
preserve:

1. the collar residual \(\xi_F^\delta\), where minimality lives;
2. finite PC before recombining \(K_N=L_MS_N-H_{M,N}\), where (6.8)
   lives;
3. the true state \(F_\delta\) of the larger window;
4. the polar part and the two Tate ports.

This can be typed without postulating a sign. For a source \(F\in Z_T\),
define \(\widetilde F=E_TF\) on the line and

\[
 \mathfrak P_{M,N}^{\rm ren}
 :=\{X,E_N\}-L_M^*E_N-J\widetilde H_{M,N}
                 -\widetilde H_{M,N}\mathscr F
                 +\mathcal P_{M,N}^{\rm pol},         \tag{8.1}
\]

so that the renormalized PC reads

\[
 \mathfrak P_{M,N}^{\rm ren}=Z_NA_M\mathscr F         \tag{8.2}
\]

on the common kernel. Since \(\mathscr F^2=I\), define the **two-window
PC--collar datum**

\[
\boxed{
 \mathfrak C_{M,N;T,\delta}^\varepsilon(F,F_\delta)
 :=\left\langle
  1_{C_\delta}\mathfrak P_{M,N}^{\rm ren}\mathscr F\widetilde F,
  F_\delta|_{C_\delta}\right\rangle .}               \tag{8.3}
\]

By (8.2), it has the two **literally equal** readings

\[
\boxed{
\begin{aligned}
 \mathfrak C_{M,N;T,\delta}^\varepsilon(F,F_\delta)
 &={\left\langle
  1_{C_\delta}Z_NA_M\widetilde F,
  F_\delta|_{C_\delta}\right\rangle}\\
 &={\left\langle
  1_{C_\delta}
  (\{X,E_N\}-L_M^*E_N-J\widetilde H_{M,N}
                 -\widetilde H_{M,N}\mathscr F
                 +\mathcal P_{M,N}^{\rm pol})
  \mathscr F\widetilde F,
  F_\delta|_{C_\delta}\right\rangle}.
                                                               \tag{8.4}
\end{aligned}}
\]

If \(M\ge e^{2(T+\delta)}\), the first line places
\(A_M\widetilde F=r_F+\xi_F^\delta\) into the collar, with the
contributions that \(Z_N\) transports from both sides.
The second preserves the Poisson difference, the polar continuum, the two
orientations of \(H_{M,N}\), and the two Tate ports. For weights \(a\),
the second line acquires exactly block (6.5); for
\(a=\Lambda\), this vanishes by (6.10). No limit has been taken.

The new form (8.3) does contain minimality because its second argument
is the state \(F_\delta\) of (7.3). It is not a form on the fixed
radical, it does not yet have a known sign, and it does not by itself
produce \(D_\Delta\) nor \(\mathcal S_{\rm can}\). Its advantage is more
modest and exact: it is the first carrier in this chain that can
simultaneously use (6.5) and (7.5) without erasing either through
recombination or a weak limit.

The new obligation, now correctly typed, is to compare the first line of
(8.4) with the collar residual of (7.5) and isolate the interior part of
\(\widetilde H_{M,N}\) **before** applying (6.6). Only an identity of
that kind could transport the sign
\(\lambda_\delta<0\) toward the moments \(R_LF\). Defining that
comparison as \(D_\Delta+\mathcal S_{\rm can}\) would again be (5.3) and
does not count.

## 9. Ledger

```text
finite polarization E_N -- C_N                               PROVED
correct orientation: difference in one slot, sum in the other PROVED
sesquilinear Green and four blocks                            PROVED
polar continuum before limits                                 PROVED / PRESERVED
two discrepancies and two Tate scalars                        PROVED / PRESERVED
finite Hardy expansion (3.8)--(3.9)                            PROVED
Hardy leading term for T_L=S_L                                 PROVED CROSSED / FALSE AS S_can
identification of the finite port with the canonical port      OPEN
Euler--hyperbola expansion (4.3)                                PROVED
appearance of +D_Delta within that expansion                    FALSE
separate collar identity defining D_Delta                       PROVED
same slot simultaneously produces D_Delta and S_can             FALSE WITH AVAILABLE TYPES
literally common residual implies Z=0                           PROVED
construction of the common residual from formal PC              FALSE / WOULD BE THE CLOSURE
cancellation delta_Lambda(k)=0 via Lambda*1=log                 PROVED / EXACT
defect for falsifying weights                                   PROVED / (6.5),(6.9)
E--C polarization after recombining, sensitive to Lambda        FALSE / WEIGHT-BLIND
interior window derivative with new datum                       FALSE / LINEAR TERM 0
right-hand minimality within Z_T x Z_T                          FALSE / WRONGLY TYPED
collar identity between T and T+delta                           PROVED
two-window PC--collar datum (8.3)                                PROVED / EXACT
sign of (8.3) and transport to R_LF                              OPEN
form sought with +D_Delta, -S_can, and common residual           FALSE AS A FORMAL CONSEQUENCE;
                                                               OPEN AS A CLOSURE THEOREM
D and the global inequality                                     OPEN
```

The central piece sought is not missing due to an unfinished expansion.
The maximal expansion is (0.4), and R161_057/R161_065 already describe
its residue. What is missing is an arithmetic law between windows that
turns the signed collar (7.5) into a closed statement about
\(R_LF\), using the vanishing of (6.5) before (6.6) recombines it.
