# Row D operator map

## Scope and status convention

This map records the operator content used by D.137, D.170 and D.190.  It
does not assert the row-D sign.  Statements below are marked as **PROVED**,
**ALGEBRAIC IDENTITY**, **INTERVAL CERTIFICATE**, **NUMERICAL EVIDENCE**, or
**OPEN**.

There is an important collision of notation.  In the paper,
`row-d-local-analysis.tex` calls the localized representative of
\(-B_{\rm nuc}\) by (A_T).  In D.137, (A_T) denotes instead the
normalized comparison (Y_TR_T^{-1/2}).  Below these are denoted
(Q_T) and (A_T^{\rm cmp}), respectively.

## Ambient and primitive spaces

| Symbol | Definition and type | Operator facts | Status |
|---|---|---|---|
| (I_T) | ([-T,T]) | support window | **PROVED** |
| (H_T) | (L^2(I_T)), with zero extension to (L^2(\mathbb R)) | Hilbert space | **PROVED** |
| (M_T) | (H_T\to\mathbb C^2, f\mapsto(M_-f,M_+f)), (M_\pm f=\int e^{\pm t/2}f(t)dt) | bounded, rank two for (T>0) | **PROVED** |
| (\mathcal P_T) | (\ker M_T) | closed codimension-two primitive space | **PROVED** |
| (\Pi_T) | orthogonal projection (H_T\to\mathcal P_T) | self-adjoint idempotent; (I-\Pi_T) has rank two | **PROVED** |
| (P_O,P_E,P_R) | multiplication by indicators of disjoint old, born-shell and remaining support sets | mutually orthogonal projections; (P_O+P_E+P_R=I) for a complete support partition | **PROVED** |

The support projections do not in general commute with (\Pi_T), since
cutting the support changes both Tate moments.  Thus (P_O\Pi_T) and
(P_E\Pi_T) are not projections on the primitive space.

## Complete feature factorization

For every active (n=p^k\le e^{2T}), put

\[
 a_n=k\log p,\qquad w_n=\frac{\log p}{p^{k/2}},\qquad
 J_{n,\pm}f=\frac{S_{a_n}f\pm f}{\sqrt2}
\]

on the overlap domain.  The Gamma difference feature is

\[
 (D_\infty f)(r,t)=\sqrt{\gamma_{5/4}(r)}
 (\widetilde f(t)-\widetilde f(t-r)),\qquad
 \gamma_{5/4}(r)=\frac{e^{-5r/2}}{1-e^{-2r}}.
\]

| Symbol | Definition and type | Operator facts | Status |
|---|---|---|---|
| (X_T) | (\mathcal P_T\to\mathcal X_T), (f\mapsto(D_\infty f,(\sqrt{w_n}J_{n,-}f)_n)) | closed feature map on the common form domain | **PROVED** |
| (Y_T) | (\mathcal P_T\to\mathcal Y_T), (f\mapsto(\sqrt\beta f,Q_{1/2}f,(\sqrt{w_n}J_{n,+}f)_n)) | bounded from (L^2(I_T)) to its feature target | **PROVED** |
| (R_T) | (X_T^*X_T) | positive, coercive on a fixed window, compact resolvent | **PROVED** |
| (L_T) | (Y_T^*Y_T) | positive bounded form | **PROVED** |
| (Q_T) | (R_T-L_T=-B_{{\rm nuc},T}^{\rm prim}) | self-adjoint closed form; neither positivity, contractivity nor idempotence is known globally | identity **PROVED**; sign **OPEN** |
| (A_T^{\rm cmp}) | (Y_TR_T^{-1/2}) on the supported range | compact, not in any finite Schatten class | **PROVED** |
| (K_T) | ((A_T^{\rm cmp})^*A_T^{\rm cmp}) | compact positive | **PROVED** |

The fundamental identities are

\[
B_{\rm nuc}(f,g)=\langle Y_Tf,Y_Tg\rangle-
\langle X_Tf,X_Tg\rangle,
\]

\[
Q_T=R_T^{1/2}(I-K_T)R_T^{1/2}.
\]

Consequently (Q_T\ge0\), (K_T\le I\), and

\[
\|Y_TR_T^{-1/2}\|\le1
\]

are equivalent.  This equivalence is an **ALGEBRAIC/OPERATORIAL
IDENTITY**; the inequalities are **OPEN** for arbitrary (T).

## Old/born reference Cholesky data

Split the already Tate-compressed feature maps into old and born source
variables:

\[
X=(X_0,X_E),\qquad Y=(Y_0,Y_E).
\]

| Symbol | Exact definition | Source and target | Status |
|---|---|---|---|
| (R_0) | (X_0^*X_0) | old source \(\to\) old source, positive closed form | **PROVED** |
| (L_0) | (Y_0^*Y_0) | old source \(\to\) old source, positive bounded form | **PROVED** |
| (r) | (X_0^*X_E) | born source \(\to\) old source | **PROVED** |
| (H) | (R_0^\dagger r) | reference harmonic lift, born \(\to\) old | **PROVED** on supported range |
| (\widetilde X_E) | (X_E-X_0H) | born source \(\to\) reference target | **PROVED** |
| (S_E) | (\widetilde X_E^*\widetilde X_E) | positive born reference capacity | **PROVED** |
| (\widehat X_0) | (X_0R_0^{\dagger/2}) | supported old source \(\to\) reference target | partial isometry | **PROVED** |
| (\widehat X_E) | (\widetilde X_ES_E^{\dagger/2}) | supported born source \(\to\) reference target | partial isometry, orthogonal to (\widehat X_0) | **PROVED** |
| (A_N) | (Y_0R_0^{\dagger/2}) | normalized old source \(\to\) load target | contraction exactly under the old-cell induction hypothesis | conditional on proved old cell |
| (y_N) | ((Y_E-Y_0H)S_E^{\dagger/2}) | normalized born source \(\to\) load target | complete boundary load, including Gamma/Poisson and all (p^k) | **PROVED** |

After this triangular source change the full comparison is exactly

\[
\mathcal A_N=(A_N,y_N).
\]

Its input and output defects are

\[
D_{\rm in}=I-A_N^*A_N,\qquad
D_{\rm out}=I-A_NA_N^*.
\]

The enlarged cell is positive exactly when

\[
y_N\in\mathrm{Ran}\,D_{\rm out}^{1/2},\qquad
y_N^*D_{\rm out}^\dagger y_N\le I.
\]

The definitions and equivalence are **PROVED**; the displayed range and
unit-capacity inequality are **OPEN** uniformly in (N).

## Input-return notation in the paper

The same old block is also written

\[
T_0=R_0^{\dagger/2}L_0R_0^{\dagger/2}=A_N^*A_N,
\qquad D_0=I-T_0=D_{\rm in}.
\]

The normalized centered cross is

\[
Q_c=R_0^{\dagger/2}(X_0^*X_E-Y_0^*Y_E)S_E^{\dagger/2}.
\]

For (h_e=R_0^{1/2}HS_E^{\dagger/2}e) and (q_e=Q_ce), the return load
is (u_e=D_0h_e-q_e).  The telescoping formula and return-dissipation
identities are **ALGEBRAIC IDENTITIES** under (0\le T_0\le I).  The
claim (q_e\in\mathrm{Ran}\,D_0^{1/2}) with the unit budget is
**OPEN** and is another coordinate form of the Douglas gate.

## Toeplitz--Hankel support block

Before Tate compression,

\[
P_OQ_TP_E=[P_O,Q_T]P_E
\]

because (P_OP_E=0).  The block contains the Gamma kernel, the centered
resolvent and every translation (k\log p).  It has infinite rank already
in the Gamma channel.  After Tate compression,

\[
X_{OE}^{\rm prim}=P_O\Pi_TQ_T\Pi_TP_E,
\]

and the difference from the raw block is a form perturbation of rank at
most four on finite-energy regularizations.  These statements are
**PROVED**.

The symbol (\mathfrak D) occurring in earlier Meyer-commutator notes is
not one of the D.190 Douglas blocks.  It denotes a nuclear commutator
super-operator whose trace produces row (c).  It must not be substituted
for (D_{\rm in}), (D_{\rm out}), or (Q_T).

## Exact missing theorem

For an exhaustive cell family, row D is equivalent to constructing from
the source, independently of the desired sign, a contraction

\[
v_N:E_N\longrightarrow\overline{\mathrm{Ran}\,D_{\rm out}}
\]

such that

\[
y_N=D_{\rm out}^{1/2}v_N,\qquad \|v_N\|\le1.
\]

Equivalently one may use the input-defect or raw support formulations, but
the output-defect formulation is the cleanest because D.170 proves that no
additional Gamma, Tate, or prime-power remainder survives the reference
Cholesky transform.

## Later source audits and the current Green coordinate

D.195--D.197 construct the local prime Poisson dilation explicitly.  Its
minimal boundary state is

\[
L^2(C_p)^+\oplus L^2(C_p)^-,
\]

and the image of the two-Tate primitive source is the direct sum of two
codimension-one hyperplanes, not a graph.  Hence the local Poisson
colligation is **PROVED**, while its ability to supply the global Douglas
contraction is **REFUTED**.

For the remaining operator-valued route, write the high block as (A),
its finite-to-high coupling as (C), and choose an intermediate trial
space (W) with complement (Z).  D.210 defines

\[
S_W=A_{ZZ}-A_{ZW}A_{WW}^{-1}A_{WZ},
\]

\[
G_W=C_W^*A_{WW}^{-1}C_W,
\qquad
R_W=C_Z-A_{ZW}A_{WW}^{-1}C_W.
\]

The exact Green identity is

\[
C^*A^{-1}C=G_W+R_W^*S_W^{-1}R_W.
\]

This is **PROVED** and is now the authoritative coordinate for finite
endpoint certification.  The remaining endpoint obligation is a directed
upper enclosure of the last residual term, not a scalar bound on the raw
coupling.

## Reference-spectral cutoff (D.211)

On the primitive source write

\[
Q_T=R_T-L_T,
\qquad R_T=X_T^*X_T,
\qquad L_T=Y_T^*Y_T\leq M_TI.
\]

For the finite-rank spectral projection
\(P_\Lambda={\bf1}_{[0,\Lambda)}(R_T)\), \(\Lambda>M_T\), its complement
is canonically coercive:

\[
(I-P_\Lambda)Q_T(I-P_\Lambda)
\geq(\Lambda-M_T)(I-P_\Lambda).
\]

This is **PROVED** and does not assume row D.  The closed-form Schur theorem
therefore reduces row D on each fixed window exactly to a finite Schur
complement.  Moreover the lower bound survives every internal shorting of
the high block, so D.210 gives the directed enclosure

\[
G_j\leq C^*A^{-1}C
\leq G_j+(\Lambda-M_T)^{-1}R_j^*R_j.
\]

The infinite-tail coercivity problem is thus closed in a source-defined
filtration.  The remaining global theorem is a uniform positivity estimate
for these finite Schur complements at all sufficiently large prime-power
births; it is **OPEN**.

## Restricted resolvent transfer (D.212)

Write an already positive old core as

\[
A_N^{\rm core}=\Gamma_N^{1/2}(I-K_N)\Gamma_N^{1/2},
\qquad b_N=\Gamma_N^{-1/2}\mathcal B_N.
\]

The exact price of replacing the pure-Gamma inverse by the core inverse is

\[
\mathcal B_N^*(A_N^{\rm core})^{-1}\mathcal B_N
-\mathcal B_N^*\Gamma_N^{-1}\mathcal B_N
=b_N^*K_N(I-K_N)^{-1}b_N.
\]

If \(\mu_{N,e}(S)=\|E_{I-K_N}(S)b_Ne\|^2\), this equals

\[
\int_{(0,1]}{1-d\over d}\,d\mu_{N,e}(d).
\]

These are **PROVED OPERATOR IDENTITIES**.  The pure-Gamma estimate controls
only \(\mu_{N,e}((0,1])\), and a scalar counterexample proves that total
mass cannot control this integral.  The remaining uniform theorem is a
source-defined small-defect Carleson estimate for the centered boundary
column.  D.211 encodes all dangerous layers in a finite reference-low
Schur complement together with its high harmonic lift, but does not by
itself bound their spectral mass.

## Return-orbit coordinate (D.213)

For \(K_N=A_NA_N^*\), \(D_N=I-K_N\), and the born column \(y_N\), put

\[
m_{N,k}=y_N^*K_N^ky_N.
\]

On the old-cell positive range,

\[
y_N^*D_N^\dagger y_N=\sum_{k\geq0}m_{N,k}
\]

as a monotone quadratic-form identity.  A defect-layer estimate with
\(\delta/(1+|\log\delta|)^\alpha\), \(\alpha>1\), is quantitatively
equivalent to

\[
m_{N,k}\ll[(k+1)(1+\log(k+1))^\alpha]^{-1}.
\]

This equivalence is **PROVED**.  For the large-cell theorem, the unpaid
object is the exact return of the complete centered born column, with
\(E_N\), all complete Green operators, endpoint pieces and their cross
terms retained.  Bound (4.3) of D.213 is a strong **OPEN SUFFICIENT
THEOREM**; the sharp necessary and sufficient condition remains the total
capacity budget.

## Defect-difference coordinate (D.214)

With \(u=A_N^*y_N\), \(D=I-A_N^*A_N\), and the D.175 identity
\(q=Dh-u\), one has

\[
y_N^*D_{\rm out}^\dagger y_N
=y_N^*y_N+h^*Dh-2\mathrm{Re}(h^*q)+q^*D^\dagger q.
\]

This is a **PROVED OPERATOR IDENTITY**.  The range conditions for \(y_N\),
\(u\), and \(q\) are equivalent.  Therefore factoring \(u\) would simply
restate the original Douglas gate.  The authoritative sharp target is

\[
q^*D^\dagger q\le
I-y_N^*y_N-h^*Dh+2\mathrm{Re}(h^*q).
\]

The equality kernel is the kernel of the difference between these two
finite born-space forms after D.211 shorting.
