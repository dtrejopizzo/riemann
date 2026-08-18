# D.187 — De Branges--Douglas audit of the exact low residual

## Theorem proved

Let

\[
 Q_T=-B_{\rm nuc}^{\rm prim}\big|_{[-T,T]}             \tag{0.1}
\]

with the exact two Tate jets imposed before every splitting.  Use either
the regional factorization of D.137 or the zero-extension factorization of
D.182.  They give the same (Q_T); the latter adds the same positive
killing to reference and load.

For an old/born decomposition write

\[
 Q_T=
 \begin{pmatrix}Q_{00}&q\\q^*&Q_{EE}\end{pmatrix},
 \qquad Q_{00}\geq0.                                  \tag{0.2}
\]

Then the following are equivalent:

\[
\begin{array}{ll}
\text{(i)}&Q_T\geq0;\\
\text{(ii)}&q\in\operatorname {Ran}Q_{00}^{1/2}
 \text{ and }
 Q_{EE}-q^*Q_{00}^{\dagger}q\geq0;\\
\text{(iii)}&q=Q_{00}^{1/2}C
 \text{ for a Douglas factor }C
 \text{ with }C^*C\leq Q_{EE}.
\end{array}                                             \tag{0.3}
\]

The Tate-centered discrepancy

\[
 E_N(\tau)=
 \sum_{n\leq N}{\Lambda(n)\over\sqrt n}e^{-i\tau\log n}
 -{N^{1/2-i\tau}-1\over1/2-i\tau}                    \tag{0.4}
\]

is part of the actual cross (q), not an external load.  Projecting
(0.4) to a prolate low band and measuring it in the primitive Green metric
is exactly the corresponding compression of the middle term in (0.3).
Therefore the exact Douglas estimate required after D.182/D.185 is not a
consequence of zero-extension coercivity: it is the Schur form of the
remaining row-D positivity.

More globally, let the old/born cells exhaust the primitive test space and
include every intermediate point in each cell.  Assuming the proved
initial seed, the family of sharp Schur budgets (0.3) for all cells is
equivalent to

\[
 Q_T\geq0\quad\text{for every }T,                     \tag{0.5}
\]

and hence, by the Weil criterion, to RH.  Conversely RH implies every
budget in (0.3).  This is an exact equivalence, not a proof of (0.3).

The canonical de Branges route gives the same acceptance test.  For

\[
 \boldsymbol\Xi(z)=\xi(1/2-iz),\qquad
 E_a(z)=\boldsymbol\Xi(z+ia),                         \tag{0.6}
\]

the de Branges kernel is positive for every (a>0) if and only if RH.
The classical zero strip proves this only for (a\geq1/2).  Passing the
kernel inequality through all (0<a<1/2) to the central Green form is
precisely the missing statement.  Thus de Branges supplies no independent
low-block estimate unless one constructs, from A--B--C, a positive
canonical Hamiltonian across that missing interval.

No location of a zeta zero is assumed.  The paper is not modified.

## 1. Exact generalized Schur--Douglas lemma

Let (A\geq0), let (B=B^*), and consider

\[
 M=\begin{pmatrix}A&X\\X^*&B\end{pmatrix}.           \tag{1.1}
\]

If (M\geq0), then (X^*u=0) for every (u\in\ker A): apply positivity
to ((tu,v)) and vary real and imaginary (t).  Hence

\[
 \operatorname {Ran}X\subset
 \overline{\operatorname {Ran}A^{1/2}}.              \tag{1.2}
\]

On finite cells, or whenever the relevant range is closed, Douglas'
lemma gives (X=A^{1/2}C).  Completing the square yields

\[
 \langle (u,v),M(u,v)\rangle
 =\|A^{1/2}u+Cv\|^2
 +\langle v,(B-C^*C)v\rangle.                        \tag{1.3}
\]

Thus (M\geq0) if and only if (B-C^*C\geq0), equivalently

\[
 B-X^*A^\dagger X\geq0.                              \tag{1.4}
\]

For nonclosed range, (1.2) is replaced by the form-domain condition
(Xv\in\operatorname {Dom}A^{\dagger/2}), and (1.4) is interpreted as a
closed quadratic form.  This is exactly the output-capacity formulation
of D.170 and the actual-cross formulation of D.179.

Applying (1.1)--(1.4) to (0.2) proves (0.3).  No estimate has entered: the
Douglas factor exists with the required norm exactly when the enlarged
signed form is positive.

## 2. Why the (\sqrt N) Green gain does not pay the Schur budget

D.182 changes the regional features by

\[
 R\longmapsto R+P_N,\qquad
 L\longmapsto L+P_N,\qquad P_N\geq0,                 \tag{2.1}
\]

where (P_N) is the common zero-extension boundary killing.  D.185 proves

\[
 R+P_N\geq A_NI,\qquad A_N\gg\sqrt N.                \tag{2.2}
\]

But

\[
 I-(R+P_N)^{-1/2}(L+P_N)(R+P_N)^{-1/2}
 =(R+P_N)^{-1/2}(R-L)(R+P_N)^{-1/2}.                 \tag{2.3}
\]

Congruence preserves inertia.  Hence (2.2) makes the normalized defect
small but cannot determine its sign.  In particular the common killing in
(\widehat J_{n,+}) and (\widehat J_{n,-}) cannot be used once as
coercivity and then omitted from the boundary load.

The crude Green estimate gives only

\[
 \langle q,(R+P_N)^{-1}q\rangle
 \leq A_N^{-1}\|q\|^2.                               \tag{2.4}
\]

The actual (q) contains the same opening contacts and the centered
(E_N).  Neither D.185's PNT information nor the two Tate moments prove a
unit bound for the right side of (2.4).  The resonant countermodel of
D.185 proves logical insufficiency of precisely those two inputs.  Exact
multiplicative correlation, not additional ambient coercivity, is needed.

## 3. The exact low-band statement

Two Green operators must be distinguished.  D.185 controls the positive
reference Green

\[
 G_{\rm ref}=\widehat{\mathcal R}_T^{-1}=O(N^{-1/2}), \tag{3.0}
\]

whereas the Schur capacity uses the old signed/defect Green
(Q_{00}^\dagger), equivalently (D_{\rm out}^\dagger) after the D.170
normalization.  There is no order comparison deriving the second bound
from (3.0): such an order would already assert positivity of the signed
defect.  This reference-versus-defect distinction is the precise residual
after the common-killing estimate.

Let (P_{\rm lo}=P_{\rm lo}(T,R)) be the primitive prolate projection and
let (G_{00}=Q_{00}^\dagger) on the supported old range.  If (q_N) is
the old--born cross after the reference harmonic lift, define

\[
 \operatorname {Cap}_{\rm lo}(N,R)
 =q_N^*P_{\rm lo}G_{00}P_{\rm lo}q_N.                \tag{3.1}
\]

This formula includes:

* the projection of every (p^k\)-label occurring in (0.4);
* the continuous Chebyshev subtraction;
* the complete Gamma/Poisson channel through (G_{00}); and
* the exact rank-two Tate shorting performed before (P_{\rm lo}).

It is not enough to estimate (3.1) in isolation.  With the D.184 notation,
the actual obligation is

\[
 {\|y_{\rm hi}\|^2\over1-\rho^2}
 +\operatorname {Cap}_{\rm lo}
 +\operatorname {Cap}_{\rm cross}\leq1.             \tag{3.2}
\]

Once the high and cross terms are fixed, (3.2) is the corresponding
compression of (1.4).  A de Branges inequality strong enough to prove
(3.2) on every cell would therefore prove (0.5); a bound for (3.1) alone
need not be RH-equivalent and cannot close the Schur budget by itself.

## 4. What de Branges does and does not add

For (a>0), put

\[
 \Theta_a(z)={E_a^\#(z)\over E_a(z)}
 ={\xi(1/2-a-iz)\over\xi(1/2+a-iz)}.                 \tag{4.1}
\]

The following statements are equivalent:

\[
\begin{array}{cl}
 E_a\text{ is Hermite--Biehler}
 &\Longleftrightarrow |\Theta_a(z)|<1
   \quad(\operatorname {Im}z>0),\\
 &\Longleftrightarrow
 {1-\Theta_a(z)\overline{\Theta_a(w)}
  \over2\pi i(\overline w-z)}\geq0
 \quad\text{as a kernel}.                            \tag{4.2}
\end{array}
\]

The kernel in (4.2) provides a Douglas/de Branges--Rovnyak contraction
after its positivity is known.  It does not prove its own positivity.
Moreover

\[
 \mathrm {RH}
 \Longleftrightarrow
 E_a\text{ is Hermite--Biehler for every }a>0
 \Longleftrightarrow
 -{\boldsymbol\Xi'\over\boldsymbol\Xi}
 \text{ is Herglotz}.                                \tag{4.3}
\]

The unconditional half-plane (a\geq1/2) is separated from the desired
central boundary by the whole interval (0<a<1/2).  Neither the two zeros
at (z=\pm i/2) removed by Tate shorting nor the finite Dirichlet
polynomial (E_N) analytically continues positivity across this interval.
Those jets only remove the polar characters (s=0,1).

At the central boundary the infinitesimal de Branges kernel is

\[
 K_0^{(1)}(z,w)={1\over\pi}
 {\boldsymbol\Xi'(z)\boldsymbol\Xi(\overline w)
 -\boldsymbol\Xi(z)\boldsymbol\Xi'(\overline w)
 \over\overline w-z}.                                \tag{4.4}
\]

Its positivity is another exact form of (0.5).  Using (4.4) to bound
(3.2) without first deriving it from a source-positive Hamiltonian would
therefore assume the required sign.

## 5. Cell exhaustion and exact RH equivalence

Let (\mathcal P_T) be the two-Tate primitive compact-support space.
The inclusions (\mathcal P_T\subset\mathcal P_{T'}) are cofinal in the
global primitive test space.  Start from any proved positive seed and
split each subsequent support cell into old and born variables.

If (0.3) holds throughout every cell, the generalized Schur lemma gives
(Q_T\geq0) inductively for every (T).  Conversely, if every (Q_T) is
positive, every block compression is positive and (0.3) follows.  Hence

\[
 \boxed{
 \text{all exact directed Douglas budgets}
 \Longleftrightarrow Q_T\geq0\ (T>0)
 \Longleftrightarrow\mathrm {RH}.}                   \tag{5.1}
\]

The final equivalence is Weil's positivity criterion, using the A--B--C
nuclear explicit formula and the two primitive Tate conditions.

Equation (5.1) does not make the directed route circular: a source theorem
may still prove all budgets without referring to zeros.  It states the
acceptance test.  What de Branges does not provide for free is the needed
source theorem.

## 6. Minimum unresolved datum

There are two equivalent minimal targets.

1. **Directed form.**  Prove (3.2), including the exact (E_N), Gamma and
   Tate terms, on every opening cell from multiplicative path/correlation
   structure.
2. **Canonical-system form.**  Construct from periodic--Witt--Poisson
   A--B--C data a positive Hamiltonian (H_a\geq0) realizing (E_a) for
   every (0<a<1/2), without defining (H_a) from the zeros or from the
   positive spectral part of (B_{\rm nuc}).

The two formulations have the same acceptance condition (5.1).  The
large zero-extension coercivity, the prolate finite rank and the two jets
type the first target correctly but do not prove it.
