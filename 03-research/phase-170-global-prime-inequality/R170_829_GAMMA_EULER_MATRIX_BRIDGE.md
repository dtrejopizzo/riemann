# R170_829 — Gamma--Euler matrix bridge to the multiscale flux

Continuation of R170_827--828. This note inserts the
Gamma--Euler reserve into the same matrix compression of the exterior
flux. The insertion produces an exact identity with a transport
remainder, but does not prove that this remainder is positive. In
particular, it does not identify the Gamma detector with the multiscale
collar.

## 1. The two forms over the complete radical

Let

\[
 Z=\ker H_T,\qquad g_F=S_LF,\qquad
 z_{\rho,F}=S_\rho U_\rho g_F,
 \qquad \bar z_F=\int w(\rho)z_{\rho,F}\,d\rho .                \tag{1}
\]

As in R170_827, a single \(L\) is chosen for which \(R_L|_Z\) is
injective. \(Z\) is not decomposed by parity: although \(JZ=Z\), it has not
been proved that \(U_\rho\) preserves the sectors of \(J\).

For \(F\in Z\), we write

\[
 e_F^{(1)}(z)=\langle F,A_1z\rangle-\langle r_F,z\rangle .       \tag{2}
\]

The exterior quadratic form of R170_827 is exactly

\[
 p(F)=\int w(\rho)\Re e_F^{(1)}(z_{\rho,F})\,d\rho
     =\Re e_F^{(1)}(\bar z_F).                                  \tag{3}
\]

The test \(g_F=S_LF\) belongs to the form domain. The weak equation of the
radical, with \(A_1=A_M\) and the cutoff chosen so as to represent the
form in the window, gives

\[
 e_F^{(1)}(g_F)=0.                                               \tag{4}
\]

Hence the exterior content of \(P\) is a transport defect:

\[
 \boxed{\ p(F)=\Re e_F^{(1)}(\bar z_F-g_F).\ }                  \tag{5}
\]

This localizes the difficulty. The averaged orbit
\(S_\rho U_\rho S_LF\) leaves the class of tests on which (4) annihilates
the functional; the remaining value is precisely the exterior flux.

On the other hand, the Gamma--Euler reserve is

\[
 d(F)=\langle F,\Delta_{N,L}F\rangle
 =\langle R_LF,(I-D_{N,L})R_LF\rangle,                           \tag{6}
\]

and satisfies

\[
 d(F)\ge(1-q_0)\|R_LF\|^2.                                     \tag{7}
\]

Let \(P,D_\Delta,B\) be the Hermitian matrices, in an arbitrary basis of
all of \(Z\), obtained by polarizing (3), (6), and
\(\|R_LF\|^2\), respectively. Then

\[
 D_\Delta-(1-q_0)B\succeq0,\qquad B\succ0.                     \tag{8}
\]

## 2. The equation an exterior lift must solve

Subtracting (3) and (6) does not explain how the detector reaches the
exterior port. Let \(\mathcal W_{\rm ext}\) be a common class of global
tests on which \(A_1z\), the pairing with \(F\), and the Tate port are
defined, and set

\[
 \Lambda:\mathcal W_{\rm ext}\to Z^*,\qquad
 (\Lambda z)(F)=\langle F,A_1z\rangle-\langle r_F,z\rangle .     \tag{9}
\]

For \(Y:Z\to\mathcal W_{\rm ext}\), let

\[
 \mathcal L(Y)(F,G)=\frac12\{(\Lambda(YG))(F)
                 +\overline{(\Lambda(YF))(G)}\}.                \tag{10}
\]

A genuine Gamma--Euler lift would be an operator built from moments and
collars, not obtained by a posteriori inversion of the matrix, that
solved

\[
 \boxed{\ \mathcal L(Y_L)(F,G)
 =\langle R_LG,(I-D_{N,L})R_LF\rangle\quad(F,G\in Z).\ }        \tag{11}
\]

Equivalently,

\[
 \boxed{\ \operatorname{Herm}[\Lambda Y_L]=D_\Delta.\ }        \tag{12}
\]

This is a finite-rank equation, but it is not automatically solvable: the
columns of \(\Lambda Y_L\) must belong to
\({\rm Ran}(\Lambda)\subset Z^*\), and only its Hermitian part is fixed.

There is an immediate obstruction for purely interior candidates. If
\(z\) is an admissible test supported in the window, the weak equation
gives

\[
 \Lambda z=0.                                                    \tag{13}
\]

Thus, every \(Y\) whose image stays in that space satisfies
\(\mathcal L(Y)=0\). This includes the natural interior syntheses
\(R_L^*CR_L\), \(G_L\), \(JG_LJ\), \(S_L\), and their compositions that
remain window tests. None of these can satisfy (11), since
\(D_\Delta\succ0\) on \(Z\).

The collar identity suggests using \(\mathcal E_{N,L}\), but this takes
values in \(\mathbb C^L\). Its adjoint again synthesizes an interior
test, so that \(\mathcal E_{N,L}^*CR_L\) again falls under (13). An
extension that crosses the boundary is needed. An explicit candidate is

\[
 (\iota_+c)(t)=\mathbf1_{(T,\infty)}(t)
       \sum_{m\le L}b_mc_me^{-a_mt},\qquad
 Y_+F=\iota_+(I-D_{N,L})R_LF.                                  \tag{14}
\]

The analogous left tail uses \(J\iota_+\); a combination of both would be
needed to preserve the two orientations. However, the collar identity
only computes \(R_LB_NF\), not \(\Lambda\iota_+c\). It does not determine
the jump terms at \(t=T\), their image under \(m(D)\), or the Tate port.
Hence it does not imply \(\mathcal L(Y_+)=D_\Delta\). That equality would
require an exterior Green formula that is not yet proved.

The available multiscale operator is

\[
 Y_{\rm ms}F=\bar z_F-g_F.                                      \tag{15}
\]

Equations (3)--(5) give \(\mathcal L(Y_{\rm ms})=P\). The obligation can
then be written as

\[
 \operatorname{Herm}[\Lambda(Y_L-Y_{\rm ms})]=D_\Delta-P.      \tag{16}
\]

Constructing the exterior tails of \(Y_L\) and proving (11) would be a
genuine bridge; the following identity only records exactly the defect of
the multiscale candidate.

## 3. Exact remainder for the multiscale candidate

We define the Gamma--Euler transport form

\[
 \mathscr R_{\rm GE}(F):=
 \Re e_F^{(1)}(\bar z_F-g_F)-d(F),                              \tag{17}
\]

and denote by \(R_{\rm GE}=R_{\rm GE}^*\) its complex polarization on
\(Z\). From (5) one obtains the exact matrix identity

\[
 \boxed{\ P-D_\Delta=R_{\rm GE}.\ }                            \tag{18}
\]

In particular,

\[
 \boxed{\ P-(1-q_0)B
 =R_{\rm GE}+\bigl[D_\Delta-(1-q_0)B\bigr].\ }                 \tag{19}
\]

The second matrix on the right-hand side is positive. Hence

\[
 R_{\rm GE}\succeq0                                             \tag{20}
\]

is a sufficient condition for the desired inequality
\(P-(1-q_0)B\succeq0\). It is neither an already-oriented equality nor a
necessary condition: a negative part of \(R_{\rm GE}\) could be
compensated by the diagonal slack in (8).

## 4. Expansion preserving PC and the two kinds of collar

Identity (24) of R170_823 and the notation of R170_827 give

\[
 P=Q-E,                                                         \tag{21}
\]

where \(E\succeq0\) is the averaged interior energy and \(Q\) is the
joint Hermitization of the four lines

\[
\begin{aligned}
 \mathfrak q^{\rm raw}(F,G)={}&
 \int w\,\chi_{G_\rho F}^{(\rho)}(S_LG)\,d\rho\\
 &+\int w\,\langle G_\rho F,[A_\rho,S_\rho]U_\rho S_LG\rangle\,d\rho\\
 &+\int w\,\langle G_\rho F,(A_1-A_\rho)S_\rho U_\rho S_LG\rangle\,d\rho\\
 &+\int {w\over1-\rho}\,
 a_M(\delta_\rho F,\mathcal R_{\rho,G})\,d\rho .              \tag{22}
\end{aligned}
\]

The first line of (22), before Hermitizing, preserves

\[
 \{\rho X,E_\rho\}-L_\rho^*E_\rho-JH_\rho-H_\rho U_\rho,
 \qquad -\langle S_\rho^*r_F,U_\rho S_LG\rangle .              \tag{23}
\]

Thus both orientations of the collar, the Tate port, the order
commutator, the primitivity correctors, and

\[
 A_1-A_\rho=m(D)-m(D/\rho)
 -(L_1+L_1^*)+(L_\rho+L_\rho^*).                                \tag{24}
\]

remain. Substituting (21) into (18) gives another exact version of the
bridge:

\[
 \boxed{\ R_{\rm GE}=Q-E-D_\Delta.\ }                           \tag{25}
\]

To also exhibit the scale-one Gamma--Euler collar, let \(Q^{(1)}\) be the
matrix obtained by polarizing \(Q_{N,L}\) of Paper 47. The identity
\(2d(F)=2\|R_LF\|^2+Q_{N,L}(F)\) on the radical implies

\[
 \boxed{\ D_\Delta=B+\tfrac12Q^{(1)},\qquad
 R_{\rm GE}=Q-E-B-\tfrac12Q^{(1)}.\ }                           \tag{26}
\]

Here \(Q^{(1)}\) must literally preserve

\[
\begin{aligned}
 Q_{N,L}(F)={}&2\Re\langle R_LF,R_LB_N^*F\rangle
 -2\Re\langle R_LF,\mathcal E_{N,L}F\rangle\\
 &-\Re\mathfrak m_T(F,S_LF)+\Re\langle r_F,S_LF\rangle .       \tag{27}
\end{aligned}
\]

In particular, the backward moment \(R_LB_N^*F\) remains truncated and the
exterior collar \(\mathcal E_{N,L}\) is not replaced by complete moments.
Formulas (22)--(27) place the multiscale collar and the scale-one collar
in the same matrix, but do not identify them.

## 5. Why the collar identity does not close the transport

The exact identity

\[
 R_LB_N=D_{N,L}R_L-\mathcal E_{N,L}                              \tag{28}
\]

acts on \(B_NF\). Applied in (6), it produces

\[
 d(F)=\|R_LF\|^2
 -\Re\langle R_LF,R_LB_NF\rangle
 -\Re\langle R_LF,\mathcal E_{N,L}F\rangle .                    \tag{29}
\]

By contrast, the exterior vector of (5) is

\[
 \bar z_F-g_F=
 \int w(\rho)S_\rho U_\rho S_LF\,d\rho-S_LF.                  \tag{30}
\]

There is no rule in (28) for transporting \(R_LS_\rho U_\rho S_LF\):
\(B_N\) does not appear alongside that vector, \(S_\rho\) changes with
\(\rho\), and \(U_\rho\) is nonlocal. Inserting (28) as though it
commuted through those operators would eliminate precisely the terms
(23)--(24) and would be a false identity. Nor can the average be replaced
by scale one: R170_823 proves that the average of translations minus the
base translation has norm at least one in the global space.

Hence (25), or equivalently (26), is the exact remainder left over when
the reserve is inserted into the exterior functional. No additional
identity reducing it to a positive form has been found.

## 6. Sign, compactness, and the first contact

The pieces with a proved sign are only

\[
 E\succeq0,\qquad D_\Delta-(1-q_0)B\succeq0.                   \tag{31}
\]

This does not orient (25), since there both are subtracted from \(Q\).
The coupled averaged collar contained in \(Q\) has Hilbert--Schmidt
compression by R170_825, but the other lines of (22), and in particular
the scale defect (24) and the alignment, have not been absorbed into a
compact operator with a sign. Moreover, over the finite space \(Z\) every
matrix is compact; invoking compactness after compressing does not
discriminate the sign of \(R_{\rm GE}\).

The minimality of the first contact contributes \(H_T\ge0\), the weak
equation (4), and the positivity of the interior energy used in (31). It
does not by itself contribute an inequality for the exterior test (30).
Extracting more would require a boundary- or window-variation formula
identifying flux (5) with the one-sided derivative of the form at the
first contact; such a formula is not proved in R170_823--828 nor in the
collar identities of Paper 47.

## 7. Result

The Gamma--Euler reserve can be inserted without loss into the full
multiscale matrix. The operator obligation is (11), and the defect of the
available candidate is given by (25)--(26). These formulas preserve
\(S_\rho\), \(U_\rho\), Tate, both orientations of the collar,
\(A_1-A_\rho\), the correctors, and the alignment.

The closure would be proved if \(R_{\rm GE}\succeq0\) were established, or
more generally

\[
 R_{\rm GE}\succeq-\bigl[D_\Delta-(1-q_0)B\bigr].              \tag{32}
\]

Inequality (32) is exactly equivalent to
\(P-(1-q_0)B\succeq0\); hence it must not be assumed as an intermediate
estimate. This note delivers the bridge and isolates its remainder, but
does not prove (32), the vanishing of the radical, D, nor RH.
