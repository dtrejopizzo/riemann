# 106.196 — The shared Gamma--Euler--polar boundary pushout

## 1. Purpose

The finite Tate pages of 106.169 have two common boundary values,

\[
 v\longmapsto (R_SJ_Sv,R_Sv),                              \tag{1}
\]

while 106.172 constructs the canonically normalized archimedean boundary
vector \(v_\infty\) with

\[
 \|v_\infty\|^2=\kappa_\infty
 =\gamma+\sum_p\sum_{k\ge2}\frac{\log p}{p^k}.             \tag{2}
\]

This note glues those data before Hilbert completion.  The construction
is a genuine pushout: the finite and infinite pages are constrained to
have one shared boundary value.  Eliminating the archimedean boundary
variable gives an explicit positive graph metric.  Its coefficient is
\(\kappa_\infty^{-1}\), forced by (2).

The construction closes the algebraic/nuclear boundary-pushout problem.
It does not by itself identify the resulting positive object with CCM
degree one; that is a separate derived comparison.

## 2. The archimedean boundary row

Let \(\mathscr K\) be the common real Cauchy coefficient Hilbert space of
106.154 and 106.169.  Let \(\mathscr H_\infty\) and \(v_\infty\) be as in
106.172(12)--(13).  Define

\[
 B_\infty:\mathscr K\longrightarrow
 \mathscr A_\infty:=\mathscr H_\infty\widehat\otimes\mathscr K,
 \qquad B_\infty F=v_\infty\otimes F.                     \tag{3}
\]

The formula is meaningful on the complete common coefficient module,
not only on the Hardy coordinate used to discover it.  Its adjoint is
the partial inner product

\[
 \beta_\infty:=B_\infty^*:
 \mathscr A_\infty\longrightarrow\mathscr K.              \tag{4}
\]

### Lemma 2.1 — Exact boundary covariance

\[
 \boxed{
 \beta_\infty B_\infty=\kappa_\infty I_\mathscr K.}        \tag{5}
\]

Consequently \(\beta_\infty\) is surjective and its minimum-norm right
inverse is

\[
 \boxed{
 \beta_\infty^\dagger=\kappa_\infty^{-1}B_\infty.}        \tag{6}
\]

#### Proof

For \(F,G\in\mathscr K\),

\[
 \langle B_\infty F,B_\infty G\rangle
 =\langle v_\infty,v_\infty\rangle\langle F,G\rangle
 =\kappa_\infty\langle F,G\rangle.                        \tag{7}
\]

This is (5).  The range of \(B_\infty\) is the orthogonal complement of
\(\ker\beta_\infty\), so (6) is the Moore--Penrose inverse. \(\square\)

## 3. Hodge-equivariant shared boundary

Double the archimedean boundary page and put

\[
 \mathscr A_\infty^{(1)}=\mathscr A_\infty\oplus\mathscr A_\infty,
 \qquad
 J_\infty(a_0,a_1)=(-a_1,a_0).                             \tag{8}
\]

On the boundary double \(\mathscr K^{(1)}=\mathscr K\oplus\mathscr K\),
put

\[
 J_{\rm bd}(F_0,F_1)=(-F_1,F_0).                           \tag{9}
\]

For a finite prime set \(S\), let \(\mathscr V_S,J_S,g_S,R_S\) be the
Tate data of 106.169 and define

\[
 \partial_{T,S}v=(R_SJ_Sv,R_Sv).                          \tag{10}
\]

Then

\[
 \partial_{T,S}J_S=J_{\rm bd}\partial_{T,S}.              \tag{11}
\]

Let

\[
 \beta_\infty^{(1)}(a_0,a_1)
 =(\beta_\infty a_0,\beta_\infty a_1).                    \tag{12}
\]

It likewise satisfies

\[
 \beta_\infty^{(1)}J_\infty
 =J_{\rm bd}\beta_\infty^{(1)}.                          \tag{13}
\]

The generic Hodge-plane embedding of 106.169 is

\[
 \Gamma_S(F_0,F_1)
 =\sum_{p\in S}\alpha_p
   \bigl(a_p\otimes F_0+c_pb_p\otimes F_1\bigr).           \tag{13a}
\]

Its adjoint is exactly the Tate boundary double:

\[
 \boxed{\Gamma_S^*=\partial_{T,S}.}                        \tag{13b}
\]

Indeed, the two components of \(\Gamma_S^*v\) are
\(\sum_p c_p\alpha_px_p=R_SJ_Sv\) and
\(\sum_p\alpha_py_p=R_Sv\).  Moreover

\[
 \Gamma_S^*\Gamma_S=C_SI,
 \qquad C_S=\sum_{p\in S}\frac{\log p}{p}.                \tag{13c}
\]

Define the co-diagonal boundary injection

\[
 d_{\rm bd,S}:\mathscr K^{(1)}\longrightarrow
 \mathscr V_S\oplus\mathscr A_\infty^{(1)},
 \qquad
 d_{\rm bd,S}F=(\Gamma_SF,B_\infty^{(1)}F).                \tag{13d}
\]

Equations (5) and (13c) give

\[
 \boxed{
 d_{\rm bd,S}^*d_{\rm bd,S}
 =(C_S+\kappa_\infty)I.}                                  \tag{13e}
\]

Under Abel regularization, 106.172 proves

\[
 \operatorname {FP}_{s\downarrow1/2}C_s
 +\kappa_\infty=0.                                        \tag{13f}
\]

Thus the co-diagonal is precisely the matched primitive--Gamma boundary:
its finite part is null.  No scalar normalization is being chosen in the
construction below.

### Definition 3.1 — Shared-boundary pushout

The finite-level pushout is the orthogonal model of the Hilbert cokernel
of \(d_{\rm bd,S}\):

\[
 \boxed{
 \mathscr P_S
 =\ker\left(
   \partial_{T,S}\oplus\beta_\infty^{(1)}:
   \mathscr V_S\oplus\mathscr A_\infty^{(1)}
   \longrightarrow\mathscr K^{(1)}ight),}               \tag{14}
\]

where the displayed row acts by
\((v,a)\mapsto\partial_{T,S}v+\beta_\infty^{(1)}a\).
Equations (11) and (13) show immediately that \(\mathscr P_S\) is
preserved by \(J_S\oplus J_\infty\).

Indeed, (13b) gives

\[
 \mathscr P_S=\ker d_{\rm bd,S}^*
 =\bigl(\operatorname {Ran}d_{\rm bd,S}\bigr)^\perp,       \tag{14a}
\]

so it represents
\((\mathscr V_S\oplus\mathscr A_\infty^{(1)})/
\operatorname {Ran}d_{\rm bd,S}\) without changing the quotient metric.

This is not the orthogonal sum excluded by 106.189.  The two pages share
the constraint (14) before either page is eliminated.

## 4. Canonical minimal pushout and its metric

The kernel in (14) contains the irrelevant free summand
\(\ker\beta_\infty^{(1)}\).  Short it orthogonally and retain the
minimum-norm representative.  By (6), it is the graph

\[
 \boxed{
 \mathscr P_S^{\min}
 =\left\{
 \left(v,-\kappa_\infty^{-1}
       (B_\infty\oplus B_\infty)\partial_{T,S}v\right):
 v\in\mathscr V_S
 \right\}.}                                                \tag{15}
\]

### Theorem 4.1 — Exact positive pushout metric

Under the graph identification \(\mathscr P_S^{\min}\simeq\mathscr V_S\),
the inherited metric is

\[
 \boxed{
 \begin{aligned}
 g_{\rm po,S}(v,w)
 &=g_S(v,w)\\
 &\quad+\kappa_\infty^{-1}
  \bigl(
   \langle R_SJ_Sv,R_SJ_Sw\rangle_\mathscr K
   +\langle R_Sv,R_Sw\rangle_\mathscr K
  \bigr).
 \end{aligned}}                                            \tag{16}
\]

It is positive definite.  The complex structure \(J_S\) is unitary for
\(g_{\rm po,S}\), and

\[
 \Omega_{\rm po,S}(v,w):=g_{\rm po,S}(J_Sv,w)             \tag{17}
\]

is alternating and nondegenerate.

#### Proof

For \(b=(b_0,b_1)\in\mathscr K^{(1)}\), (5) gives

\[
 \left\|
  \kappa_\infty^{-1}(B_\infty\oplus B_\infty)b
 \right\|^2
 =\kappa_\infty^{-1}(\|b_0\|^2+\|b_1\|^2).               \tag{18}
\]

Substitute \(b=\partial_{T,S}v\) in the direct-sum metric to obtain
(16).  Its first term is already positive definite.  Equation (11),
unitarity of \(J_{\rm bd}\), and \(J_S^2=-I\) show that the two boundary
squares are exchanged by \(J_S\), so \(J_S\) is unitary.  The standard
compatible-complex-structure calculation then proves the claims about
(17). \(\square\)

The coefficient in (16) cannot be adjusted: it is the inverse Schur
coefficient of \(B_\infty^*B_\infty=\kappa_\infty I\).  The direct
boundary coefficient, before shorting, is
\(C_S+\kappa_\infty\), whose Abel finite part is exactly zero by (13f).
This reconciles the inverse coefficient in the quotient metric with the
direct coefficient in the primitive--Gamma cancellation.

## 5. Cofinal compatibility and normalized scaling

If \(S\subset T\), extension by zero gives

\[
 \iota_{S,T}:\mathscr V_S\longrightarrow\mathscr V_T.      \tag{19}
\]

The local metric, complex structure, and both boundary values are
unchanged:

\[
 \begin{aligned}
 g_T(\iota_{S,T}v,\iota_{S,T}w)&=g_S(v,w),\\
 J_T\iota_{S,T}&=\iota_{S,T}J_S,\\
 \partial_{T,T}\iota_{S,T}&=\partial_{T,S}.
 \end{aligned}                                             \tag{20}
\]

### Theorem 5.1 — Functorial global algebraic polarization

The maps (19) induce polarized isometries

\[
 (\mathscr P_S^{\min},g_{\rm po,S},J_S)
 \hookrightarrow
 (\mathscr P_T^{\min},g_{\rm po,T},J_T).                  \tag{21}
\]

Consequently

\[
 \mathscr P_{\rm fin}:=\varinjlim_S\mathscr P_S^{\min}    \tag{22}
\]

has a faithful positive metric, a nondegenerate alternating form, and a
compatible complex structure.

The common normalized coefficient flow \(V_t\) of 106.154 acts on every
coefficient entry.  It commutes with \(R_S,J_S,B_\infty\), and hence acts
unitarily on (16).  Its weight-one lift \(e^{t/2}V_t\) scales
\(g_{\rm po}\) and \(\Omega_{\rm po}\) by \(e^t\).

#### Proof

Equations (20) inserted in (16) give (21).  Every nonzero element of the
algebraic limit lies at a finite level where (16) is definite.  The flow
claims follow term by term and extend by the same identities. \(\square\)

## 6. Inclusion of the Gamma spin interior and polar boundary

The positive Gamma degree-one interior of 106.195(16) may be tensored
with \(\mathscr K\) and added to (22); its normalized flow is unitary.
This does not undo the non-free coupling, because the scalar Gamma and
repeated-winding finite part has already entered through the shared
boundary row (14).  The \(H^0/H^2\) polar plane is retained in degrees
zero and two, with determinant (11) of 106.195, rather than inserted as a
positive degree-one summand.

Thus the graded source object has:

* finite root/Tate degree one with literal prime coefficients;
* the shared primitive--Gamma boundary (14);
* the positive Gamma spin interior;
* the polar \(H^0/H^2\) determinant boundary;
* a positive weight-one polarization on its algebraic degree one.

## 7. What remains for CCM

The pushout itself is now explicit.  The remaining map is the derived
localization

\[
 H^1_{\rm Ros}\longrightarrow\mathscr P_{\rm fin}         \tag{23}
\]

obtained from the CCM restriction cone, the primitive Eulerian projector
of 106.174, and the dense jet observation of 106.175.  Two statements are
still needed:

1. its kernel is zero after quotienting the CCM restriction range;
2. the pullback of \(\Omega_{\rm po}\) is the already descended
   alternating form \(\Omega_{\rm Ros}\).

The first is a derived kernel identity, not merely scalar sampling.  The
second is a chain-level Green identity.  If both hold, the source metric
(16) descends to a faithful Hilbert majorant on separated CCM degree one;
the normalized flow is already unitary and the alternating form is
bounded and nondegenerate.  The criteria of 106.191 are then satisfied.

## 8. Status

Proved without RH or zero input:

* the common Gamma--Euler boundary row and its exact normalization;
* the non-free shared-boundary pushout;
* its canonical shorting and explicit positive metric (16);
* compatibility with Hodge conjugacy, adjoining primes, and normalized
  real scaling;
* incorporation of the positive Gamma interior and polar determinant
  page with the correct cohomological parity.

Still required:

* construction of (23) on the complete CCM cyclic cone;
* proof of its derived injectivity;
* proof of the alternating-form/Green identity.
