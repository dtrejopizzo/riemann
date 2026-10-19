# R170_827 — Multiscale matrix over the radical

Continuation of R170_823--826. This note compresses the
complete multiscale identity to the radical of a hypothetical first contact.
The result is an exact finite spectral criterion, with a canonical positive
metric given by the Gamma moments. The vanishing of the radical is not yet
obtained: the full PC matrix still needs to be oriented.

## 1. The finite space and its faithful metric

Let \(T\) be a primitive first contact and

\[
 Z:=\ker H_T,\qquad d:=\dim Z<\infty .                         \tag{1}
\]

We do not fix a parity. The operator \(J\) leaves \(Z\) invariant, but the
conjugated operators \(U_\rho=D_\rho^*\mathscr F D_\rho\) that appear in
the multiscale identity will not be used as though they preserved each
parity sector. We choose a basis \(F_1,\ldots,F_d\) of all of \(Z\) and, as
Paper 47 allows, a single \(L\) such that

\[
 R_L|_Z:Z\longrightarrow\mathbb C^L
 \quad\hbox{is injective}.                                    \tag{2}
\]

We define the Gram matrix

\[
 B_{ij}:=\langle R_LF_j,R_LF_i\rangle .                         \tag{3}
\]

Then \(B=B^*>0\). Indeed, if \(F=\sum_jx_jF_j\),

\[
 x^*Bx=\|R_LF\|^2,
\]

and (2) makes this number strictly positive when \(x\ne0\). This
observation removes an important ambiguity: on \(Z\), proving
\(R_LF=0\) is already equivalent to proving \(F=0\). Hence no matrix
manipulation can take that vanishing as an innocuous intermediate
hypothesis.

For each \(F\in Z\), the Tate vector \(r_F\) of the weak equation depends
linearly on \(F\). The following also depend linearly on \(F\):

\[
 g_F=S_LF,\quad G_\rho F,\quad
 \delta_\rho F=G_\rho F-F,\quad
 z_{\rho,F}=S_\rho U_\rho g_F,\quad
 \mathcal R_{\rho,F}=\delta_\rho F-(1-\rho)z_{\rho,F}.           \tag{4}
\]

Here \(S_L=R_L^*R_L+JR_L^*R_LJ\) is the test smoother built with the same
truncation \(L\); it is not the rectangular operator \(R_L\) of (2).

## 2. Compression of the full identity

We fix
\(N=\lceil e^{2T}\rceil\), \(M=N^2\), as in R170_819, and fix
\(w\ge0\), real, smooth, with compact support in an admissible
contraction interval, and \(\int w=1\). The left-hand side of (24) of
R170_823 defines on \(Z\) the real quadratic form

\[
 q_{\rm ms}(F):=
 \int w(\rho)\bigl(\Phi_\rho(F)+
                    \mathcal E^{\rm int}_\rho(F)\bigr)\,d\rho . \tag{5}
\]

Its complex polarization defines a Hermitian form \(k_{\rm ms}(F,G)\).
Let

\[
 K_{ij}:=k_{\rm ms}(F_j,F_i),\qquad K=K^*.                      \tag{6}
\]

This definition does not presuppose that each operator summand on the
right-hand side is self-adjoint. Equivalently, one can insert \(F_j,F_i\)
into the sesquilinear version of (24), form a raw matrix \(K^{\rm raw}\),
and take

\[
 K=\frac{K^{\rm raw}+K^{{\rm raw}*}}2.                          \tag{7}
\]

Taking only real parts entry by entry before transposing would not be a
correct Hermitization.

Let \(P=P^*\) be the matrix of the exterior form
\(F\mapsto\int w(\rho)\Phi_\rho(F)d\rho\). By definition of the left-hand
side,

\[
 \boxed{\ K=P+E\ },                                            \tag{8}
\]

where

\[
 E_{ij}=\int \frac{w(\rho)}{1-\rho}\,
 a_M(\delta_\rho F_j,\delta_\rho F_i)\,d\rho,\qquad E\succeq0,  \tag{9}
\]

The positivity in (9) uses all its hypotheses: \(\delta_\rho F\) is
primitive and supported in \(I_T\), \(a_M=a_T\) on that data because
\(M\ge e^{2T}\), \(H_T\ge0\), \(w\ge0\), and \(1-\rho>0\).

On the other hand, let \(Q=Q^*\) be the joint Hermitization of the four
complete lines on the right-hand side of (24). Its raw form is

\[
\begin{aligned}
 \mathfrak q^{\rm raw}(F,G)={}&
 \int w(\rho)\,
   \chi_{G_\rho F}^{(\rho)}(S_LG)\,d\rho\\
 &+\int w(\rho)\,
   \langle G_\rho F,[A_\rho,S_\rho]U_\rho S_LG\rangle\,d\rho\\
 &+\int w(\rho)\,
   \langle G_\rho F,(A_1-A_\rho)S_\rho U_\rho S_LG\rangle\,d\rho\\
 &+\int\frac{w(\rho)}{1-\rho}\,
   a_M(\delta_\rho F,\mathcal R_{\rho,G})\,d\rho,              \tag{10}
\end{aligned}
\]

\[
 \mathfrak q(F,G)=\tfrac12\bigl(
 \mathfrak q^{\rm raw}(F,G)+
 \overline{\mathfrak q^{\rm raw}(G,F)}\bigr),
 \qquad Q_{ij}=\mathfrak q(F_j,F_i).                            \tag{11}
\]

The compressed and polarized identity (24) states exactly

\[
 \boxed{\ Q=K=P+E.\ }                                          \tag{11a}
\]

Hence \(Q\) is the full PC matrix; it is not a residual that could be
added back to \(E\). If one wishes to isolate the exterior part, it is
\(P=Q-E\).

In the first line of (10), the averaged PC identity must preserve, before
Hermitizing,

\[
 \{\rho X,E_\rho\}-L_\rho^*E_\rho-JH_\rho-H_\rho U_\rho
 \quad\hbox{and}\quad
 -\langle S_\rho^*r_F,U_\rho S_LG\rangle.                     \tag{12}
\]

Thus (10)--(11a) contain the two orientations of the collar, the Tate
port, the order commutator, the joint Gamma--primes defect

\[
 A_1-A_\rho=m(D)-m(D/\rho)-(L_1+L_1^*)+(L_\rho+L_\rho^*),       \tag{13}
\]

where \(A_1:=A_\rho|_{\rho=1}=A_M\) and \(L_1:=L_\rho|_{\rho=1}=L_M\);
the subscript \(1\) denotes the scale, not an arithmetic cutoff equal to
one,

and the alignment error. Omitting any of them would produce a matrix
different from the multiscale identity.

Formulas (8) and (11a) are not a new piece called \(\Phi+E\). Their
useful content is that (i) the obligation restricted to \(Z\) is
represented by a Hermitian matrix of size \(d\), though computing its
entries still requires certifying integrals and radical data, (ii) (9)
separates the part whose sign is indeed proved, and (iii) PC, Tate,
commutators, and alignment are kept together in the matrix \(Q\) of
(10)--(13).

## 3. Parity: permitted use and non-permitted use

Since \(H_T\) commutes with \(J\), the abstract decomposition

\[
 Z=Z_+\oplus Z_-                                               \tag{14}
\]

does hold. One can evaluate (5) on a vector \(F\in Z_+\) or \(F\in Z_-\),
and the Tate identities Paper 47 proves for that parity can be used
there. What does not follow is that each operator in (10), in particular
\(U_\rho\), leaves those subspaces invariant, or that \(K\) is
block-diagonal with respect to (14). That is why the following criterion
is formulated for the full matrix. A splitting \(K=K_+\oplus K_-\) would
only be legitimate after proving \([K,J|_Z]=0\) for the complete form,
including Tate, correctors, and alignment.

## 4. Self-adjointness and size of the averaged collar

R170_825 writes, for \(a>0\),

\[
 C_{a,w}:=\int w(\rho)\tau_{a/\rho}U_\rho\,d\rho
          =q_{a,w}(D)J,                                        \tag{15}
\]

\[
 q_{a,w}(\xi)=\int\eta(s)
 e^{i[\theta(s\xi)-as\xi]}\,ds,\qquad \eta\in\mathbb R.       \tag{16}
\]

From \(u_\infty(-\xi)=\overline{u_\infty(\xi)}\) we can choose
\(\theta(-\xi)=-\theta(\xi)\) modulo the relevant constant phase, and

\[
 q_{a,w}(-\xi)=\overline{q_{a,w}(\xi)}.                         \tag{17}
\]

Since \((q(D)J)^*=\overline q(-D)J\), (17) proves

\[
 \boxed{\ C_{a,w}=C_{a,w}^*\quad(w\ \hbox{real}).\ }           \tag{18}
\]

Consequently, \(P_TC_{a,w}P_T\) is self-adjoint and Hilbert--Schmidt. The
exact arithmetic sum is also self-adjoint term by term when the isolated
coupled collar is considered:

\[
 \mathcal C_{M,N,w}:=
 P_T\int w(\rho)H_\rho U_\rho\,d\rho P_T.                       \tag{19}
\]

The bound of R170_825 gives

\[
 \|\mathcal C_{M,N,w}\|_{\rm HS}
 \le\sum_{N<k\le MN}\frac{h_{M,N}(k)}{\sqrt k}
       \mathcal C_T(\log k,w).                                  \tag{20}
\]

If \(s_j\) are its singular values, then

\[
 s_j(\mathcal C_{M,N,w})\le
 \frac{\|\mathcal C_{M,N,w}\|_{\rm HS}}{\sqrt j},             \tag{21}
\]

since \(j s_j^2\le\sum_{n\le j}s_n^2\). Its eigenvalues are real and obey
the same bound in modulus, ordered by modulus. This quantifies the
available compactness. It does not imply that the operator is trace
class: \(\ell^2\) for the singular values does not imply \(\ell^1\). It
also does not fix the sign of its eigenvalues nor that of \(Q\), where the
collar is coupled to the other lines of (10).

There is also a quantitative finite-dimensional consequence. Let \(P_Z\)
be the orthogonal projection of \(L^2(I_T)\) onto \(Z\), and consider any
realization of the collar between subspaces of the window, in particular
\(P_Z\mathcal C_{M,N,w}|_Z\). By the characterization of singular numbers
and (20), for every \(r\ge0\),

\[
 s_{r+1}(P_Z\mathcal C_{M,N,w}|_Z)
 \le s_{r+1}(\mathcal C_{M,N,w})
 \le\frac1{\sqrt{r+1}}
 \sum_{N<k\le MN}\frac{h_{M,N}(k)}{\sqrt k}
       \mathcal C_T(\log k,w).                                  \tag{21a}
\]

Equivalently, there exists an operator of rank at most \(r\) whose
operator distance to that compression does not exceed the last term of
(21a). This allows the collar to be enclosed by a low-rank part and a
controlled tail. The other blocks of \(Q\) have not all been proved
compact nor subjected to an analogous bound; hence (21a) does not
certify the full matrix \(K\).

Even within the first line of (10), (20) directly controls only the
isolated collar. Indeed,

\[
 G_\rho F=F+\delta_\rho F
\]

separates a contribution with a fixed left vector, which does factor
through \(\int wH_\rho U_\rho d\rho\), and another with
\(\delta_\rho F\) depending on \(\rho\), which does not factor and
requires an additional estimate. (20) is not automatically transferred to
the whole matrix entry of \(Q\).

## 5. Exact finite spectral criterion

Metric (3) removes the basis dependence. We define

\[
 \widehat K=B^{-1/2}KB^{-1/2},\qquad
 \widehat P=B^{-1/2}PB^{-1/2},\qquad
 \widehat E=B^{-1/2}EB^{-1/2},\qquad
 \widehat Q=B^{-1/2}QB^{-1/2}=\widehat K.                      \tag{22}
\]

These are Hermitian matrices and

\[
 \widehat K=\widehat P+\widehat E,
 \qquad \widehat E\succeq0.                                   \tag{23}
\]

For \(F=\sum x_jF_j\ne0\), the generalized ratio is

\[
 \frac{q_{\rm ms}(F)}{\|R_LF\|^2}
 =\frac{x^*Kx}{x^*Bx}.                                         \tag{24}
\]

By the min--max principle,

\[
 \boxed{
 q_{\rm ms}(F)\le0\ \hbox{for all }F\in Z
 \quad\Longleftrightarrow\quad
 \lambda_{\max}(\widehat K)\le0 .}                            \tag{25}
\]

More generally, the best constant \(\gamma\) in

\[
 q_{\rm ms}(F)\le\gamma\|R_LF\|^2\qquad(F\in Z)              \tag{26}
\]

is exactly \(\gamma=\lambda_{\max}(\widehat K)\). Hence the sought joint
cancellation reduces, without loss, to enclosing the largest eigenvalue of
a finite matrix.

This reduction is computable in a precise sense: given a certified basis
of \(Z\), the moments \(R_LF_i\), the Tate vectors \(r_{F_i}\), and
rigorous bounds for the integrals in (9)--(13), interval arithmetic can
enclose \(B^{-1/2}KB^{-1/2}\) and decide (25) when the interval of the
extremal eigenvalue does not cross zero. The HS bound (20) can control the
part of the collar that has fixed external data; the part with
\(G_\rho F-F\) and the other blocks require separate estimates.

## 6. What sign is proved and what datum is missing

There are two positivity results available, but they belong to different
identities. In the multiscale interface (8), the interior energy
satisfies \(E\succeq0\). In the compressed identity of Paper 47, the
Gamma--Euler contraction satisfies

\[
 \Delta_{N,L}=R_L^*(I-D_{N,L})R_L
 \succeq(1-q_0)R_L^*R_L,                                      \tag{27}
\]

and hence its matrix over \(Z\) is at least \((1-q_0)B\). But
\(\Delta_{N,L}\) does not appear in (24) of R170_823 with the same
functional and the same arguments. It is not legitimate to add (27) to
(8), nor to use it to orient \(P\) or \(Q\), until a joint identity is
derived that contains both quantities with their exact signs.

Moreover, not even (25) alone forces \(R_LF=0\). Since \(B>0\), for every
\(F\ne0\) in \(Z\) we already have \(\|R_LF\|^2>0\), and a nonpositive
form can perfectly well coexist with that positive norm. To force the
vanishing would require a second genuine estimate in the same functional;
for instance, an independent identity implying

\[
 q_{\rm ms}(F)\ge c\|R_LF\|^2\quad(c>0)                         \tag{28}
\]

together with (25). (28) has not been proved. It is only the exact form
of the datum that would close the argument.

The matrix map of the contradiction sought before the average can also be
seen directly. The two inequalities that would close the radical are

\[
 \boxed{
 P-(1-q_0)B\succeq0,
 \qquad
 P+E\preceq0.}                                                  \tag{28a}
\]

The first is the matrix version of the claim that the exterior return
dominates the Gamma--Euler reserve; the second is the desired multiscale
upper bound. If both were proved, then

\[
 (1-q_0)B\preceq P\preceq-E\preceq0,                            \tag{28b}
\]

which contradicts \(B>0\) when \(Z\ne0\). This diagram clarifies the
exact interface between the two routes, but it contributes neither of the
two inequalities in (28a). In particular, (27) alone only orients the
reserve; it does not prove that the exterior form \(P\) dominates it.

The missing datum for the upper bound can be expressed as an orientation
of the exterior part, or equivalently of the full PC matrix:

\[
 \widehat P\preceq-\widehat E
 \quad\Longleftrightarrow\quad
 \widehat Q=\widehat K\preceq0.                                \tag{29}
\]

Condition (29) gives (25); an additional strict inequality linked to
\(B\) is still needed to obtain the contradiction that annihilates the
radical. Neither the self-adjointness of the collar, nor its
Hilbert--Schmidt character, nor \(\Lambda*1=\log\) separately prove (29).
The advantage of (22)--(25) is that they pinpoint exactly which finite
object must be estimated without losing the correlations between PC,
Tate, Gamma, the two collars, and the alignment.

## 7. Scope

The new piece is the intrinsic normalization by the faithful Gram matrix
\(B\), the self-adjointness of the real averaged collar, and the finite
spectral equivalence (25), together with the singular-value control
(21). The reduction allows a rigorous matrix audit of any proposed
cancellation and avoids two shortcuts: separating parities without
proving invariance of the full form, or converting Hilbert--Schmidt into
trace class or into positivity.

In the current state, the matrix does not force the vanishing. The next
mathematically decisive step is to estimate the full PC matrix
\(\widehat Q=\widehat K\) — preferably via an identity that also inserts
(27) into the same functional — and check whether it satisfies (29) with
the necessary positive margin relative to \(B\). The certified range of
Paper 47 is not extended, nor is D or RH proved.

Finally, this reduction does not yet use the dynamical minimality of the
first contact, that is, the loss of nonnegativity over every larger
window. The same matrices can be formed for any null mode of a window
with \(H_T\ge0\). Hence they constitute a finite audit of the radical, but
do not yet satisfy Paper 47's requirement of distinguishing the first
contact from a formal spectral zero or from a positive eigenvector.
