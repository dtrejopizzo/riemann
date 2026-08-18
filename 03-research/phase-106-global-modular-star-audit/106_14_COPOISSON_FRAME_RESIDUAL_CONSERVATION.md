# 106.14 — Co-Poisson frame residual conservation and the Gamma dimension gate

## Purpose

Document 106.12 constructs moving truncated co-Poisson vectors whose fixed
prolate angle levels satisfy

\[
 d_4\asymp\lambda^9e^{-4\pi\lambda^2},\qquad
 d_8\asymp\lambda^{17}e^{-4\pi\lambda^2},\qquad
 d_4/d_8\asymp\lambda^{-8}.
 \tag{1}
\]

This note tests whether all the low modes, rather than one model vector, can
select the semilocal Weil ground branch.  The answer supplied by the present
inputs is negative for two exact reasons.

1. A lower frame bound on the negative spectral subspace and the aggregate
   operator residual obey a sharp conservation identity.  Adding modes
   multiplies useful overlap and negative residual by the same amount.
2. Gamma coercivity combined with the known \(O(\lambda)\) norm of the
   prime--pole perturbation controls an
   \(O(Le^{C\lambda})\)-dimensional space, whereas the prolate family has only
   \(M_L\asymp2\lambda^2\) vectors.

Moreover, every complete co-Poisson transform vanishes at every zeta zero,
including a hypothetical off-line zero.  Its truncation sees that evaluation
channel only through the same exterior leakage that creates its residual.

These statements do not prove that the actual negative spectral subspace is
nonzero, or that a lower frame bound fails under RH, where that subspace is
zero.  They show that the desired branch estimate does not follow from the
available prolate leakage, Gamma coercivity and absolute prime--pole norm.

Throughout,

\[
 I_L=[-L/2,L/2],\qquad \lambda=e^{L/2}.
 \tag{2}
\]

## 1. Exact many-vector residual inequality

Let \(A\) be a lower-semibounded self-adjoint compact-resolvent operator on
\(\mathcal H\), and put

\[
 P_-={\bf1}_{(-\infty,0)}(A),\qquad
 \mathcal N=\operatorname {Ran}P_-.
 \tag{3}
\]

For \(q_1,\ldots,q_M\in\operatorname {Dom}(A)\), define

\[
 Q:\mathbb C^M\to\mathcal H,\quad Qc=\sum_{j=1}^Mc_jq_j,
 \qquad D=AQ,
 \tag{4}
\]

If \(\mathcal N\ne\{0\}\), define the negative-space lower frame bound

\[
 a_-(Q):=\inf_{\substack{v\in\mathcal N\\\|v\|=1}}
             \|Q^*v\|_{\ell^2}^2.
 \tag{5}
\]

Positivity of (5) already implies \(\dim\mathcal N\le M\).  If
\(\mathcal N=\{0\}\), every statement below about the negative branch is
vacant and no frame constant is needed.

### Theorem 1 — Frame--residual conservation

Assume \(\mathcal N\ne\{0\}\).  If \(a_-(Q)>0\), then

\[
 \boxed{
 \sigma(A|_{\mathcal N})\subset
 \left[-\frac{\|D^*P_-\|}{\sqrt{a_-(Q)}},0\right).
 }
 \tag{6}
\]

In particular, if \(\epsilon_0<0\) is the least eigenvalue of \(A\),

\[
 \boxed{
 |\epsilon_0|\sqrt{a_-(Q)}
 \le\|D^*P_-\|\le\|D\|.
 }
 \tag{7}
\]

For an orthonormal negative eigenbasis \((\phi_\ell)\), one has the exact
Hilbert--Schmidt identity

\[
 \boxed{
 \begin{aligned}
 \mathcal R_{-,\mathrm{HS}}^2
 &:=\sum_{j=1}^M\|P_-Aq_j\|^2\\
 &=\sum_{\epsilon_\ell<0}\epsilon_\ell^2
   \sum_{j=1}^M|\langle\phi_\ell,q_j\rangle|^2.
 \end{aligned}}
 \tag{8}
\]

Consequently,

\[
 \boxed{
 \mathcal R_{-,\mathrm{HS}}^2
 \ge a_-(Q)\sum_{\epsilon_\ell<0}\epsilon_\ell^2
 \ge a_-(Q)\epsilon_0^2.
 }
 \tag{9}
\]

#### Proof

The space \(\mathcal N\) reduces \(A\).  For
\(v\in\mathcal N\cap\operatorname {Dom}(A)\), apply the frame inequality to
\(Av\in\mathcal N\):

\[
 a_-(Q)\|Av\|^2
 \le\|Q^*Av\|^2
 =\|D^*v\|^2
 \le\|D^*P_-\|^2\|v\|^2.
 \tag{10}
\]

The spectral theorem proves (6), and a ground eigenvector gives (7).
Expanding each \(P_-Aq_j\) in the negative eigenbasis and using

\[
 \langle\phi_\ell,Aq_j\rangle
 =\epsilon_\ell\langle\phi_\ell,q_j\rangle
 \tag{11}
\]

proves (8) by Parseval.  Equation (5) then gives (9).  \(\square\)

### Corollary 2 — Fixed negativity forces frame collapse at the residual
scale

If, along a cofinal sequence,

\[
 \epsilon_{0,L}\le-c<0,
 \tag{12}
\]

then every finite family \(Q_L\) satisfies

\[
 \boxed{
 a_-(Q_L)\le c^{-2}\mathcal R_{-,\mathrm{HS}}(Q_L)^2.
 }
 \tag{13}
\]

Thus proving

\[
 \mathcal R_{-,\mathrm{HS}}(Q_L)/\sqrt{a_-(Q_L)}\to0
 \tag{14}
\]

already excludes the fixed negative branch.  It is not a gain obtained by
using many modes.  On a single negative eigenvector the equality is
pointwise:

\[
 \boxed{
 \sum_j|\langle\phi_0,Aq_j\rangle|^2
 =\epsilon_0^2\sum_j|\langle\phi_0,q_j\rangle|^2.
 }
 \tag{15}
\]

## 2. Exact finite-frame no-go in the full radical

Let \(\mathfrak W\) be the complete polarized Weil form on an admissible
dense domain \(\mathcal D\subset L^2(\mathbb R)\), and let

\[
 \mathcal R=\{r\in\mathcal D:\mathfrak W(r,g)=0
                  \text{ for every }g\in\mathcal D\}
 \tag{16}
\]

be its polarized radical.  The complete co-Poisson range lies in
\(\mathcal R\).

### Theorem 3 — A finite radical frame misses a negative direction

Let \(S\subset\mathcal R\) be finite-dimensional, and let \(P_S\) be the
\(L^2\)-orthogonal projection onto \(S\).  If
\(\mathfrak W(h,h)<0\), then

\[
 h_S:=h-P_Sh\ne0,\qquad h_S\perp S,
 \qquad
 \boxed{\mathfrak W(h_S,h_S)=\mathfrak W(h,h)<0.}
 \tag{17}
\]

#### Proof

Since \(P_Sh\in\mathcal R\), both mixed terms and the quadratic radical term
vanish after expanding \(\mathfrak W(h-P_Sh,h-P_Sh)\).  If \(h_S=0\), then
\(h\in\mathcal R\), contradicting its negative form value.  \(\square\)

This is an exact full-space result.  The subtracted vector need not remain
compactly supported.  Semilocally, the same argument survives only when the
aggregate truncation defect, including the inverse conditioning of the
moving Gram matrix, tends to zero.  Controlling that aggregate defect is
already part of the missing branch theorem.

The statement is pointwise in the finite-dimensional space \(S\).  It
therefore applies without change to any sequence \(S_L\subset\mathcal R\)
whose finite dimensions tend to infinity: for each \(L\), there is a
negative admissible vector exactly orthogonal to all of \(S_L\).  What does
not follow is compact support of those orthogonalized vectors in the
semilocal window.

## 3. Co-Poisson annihilation of an off-line evaluation channel

For every complete co-Poisson vector \(F=\mathcal E(f)\) covered by 106.12,

\[
 \widehat F(z)
 =\zeta\!\left(\tfrac12-iz\right)\Psi_f(z).
 \tag{18}
\]

It therefore vanishes at the parameter \(z_\rho\) associated with every
nontrivial zero, whether or not that zero lies on the critical line.

Let \(K_{L,z}\) be the Paley--Wiener Riesz vector on \(I_L\), normalized by

\[
 \langle g,K_{L,z}\rangle=\widehat g(z).
 \tag{19}
\]

If \(a=|\operatorname {Im}z|>0\),

\[
 \|K_{L,z}\|^2=\frac{\sinh(aL)}a.
 \tag{20}
\]

Put \(q_{f,L}=P_LF\) and \(r_{f,L}=(1-P_L)F\).  At \(z_\rho\), (18) gives

\[
 \boxed{
 \langle q_{f,L},K_{L,z_\rho}\rangle
 =-\widehat r_{f,L}(z_\rho).
 }
 \tag{21}
\]

Consequently, for every finite moving family,

\[
 \boxed{
 \sum_{j=1}^{M_L}
 \left|\left\langle q_{j,L},
    \frac{K_{L,z_\rho}}{\|K_{L,z_\rho}\|}\right\rangle\right|^2
 =\frac{\sum_{j=1}^{M_L}|\widehat r_{j,L}(z_\rho)|^2}
        {\|K_{L,z_\rho}\|^2}.
 }
 \tag{22}
\]

If all weighted tail evaluations are at most \(\tau_L\) and
\(M_L\asymp2\lambda^2\), the right side is

\[
 O\!\left(\lambda^2\tau_L^2e^{-aL}\right).
 \tag{23}
\]

Equation (22) concerns the divisor evaluation channel; it does not claim
that its Riesz vector is an eigenvector of \(A_L\).  The corresponding exact
statement for actual negative eigenvectors is (8)--(15).  Both descriptions
show the same geometry: the complete radical is blind to an off-line
channel, and truncation sees it only through leakage.

## 4. Why the \(d_4/d_8\) hierarchy does not select the branch

The fixed low modes compare the first two eigenvalues of the constrained
**angle form**.  They do not supply a Weil-operator residual.  Even if one
adds the stronger assumptions

\[
 \|A_Lq_{j,L}\|\le\delta_{j,L},
 \tag{24}
\]

Theorem 1 gives only

\[
 |\epsilon_{0,L}|
 \le\frac{(\sum_j\delta_{j,L}^2)^{1/2}}
              {\sqrt{a_-(Q_L)}}.
 \tag{25}
\]

Under a fixed negative branch, (15) forces the numerator's projection onto
that branch to be exactly \(|\epsilon_{0,L}|\) times the denominator.  The
common defect, including \(d_4\) or \(d_8\), cancels from the quotient.

There are two incompatible prolate regimes.

- A fixed number of low modes has the double-exponential defects (1), but
  cannot frame a negative space whose dimension has not already been
  bounded.
- The full Slepian family has \(M_L\asymp2\lambda^2\) modes.  Fixed-order
  \(d_4,d_8\) asymptotics are not uniform over that growing family, and no
  aggregate Weil residual at their scale has been proved.

Thus \(d_4/d_8\asymp\lambda^{-8}\) is a genuine angle-operator hierarchy,
not a proved ground/next-eigenvalue hierarchy for \(A_L\).

## 5. Gamma coercivity and the dimension mismatch

### Theorem 4 — The available coercivity controls only exponentially many
negative modes

Let \(A_L=G_L+B_L\) on \(L^2(I_L)\).  Assume

\[
 \langle G_Lf,f\rangle
 \ge c_0\int_{\mathbb R}\log(2+|t|)|\widehat f(t)|^2
                 \frac{dt}{2\pi}-C_0\|f\|^2,
 \tag{26}
\]

and \(\|B_L\|\le b_L\).  Put

\[
 T_L=\exp\!\left(\frac{2(C_0+b_L)}{c_0}\right).
 \tag{27}
\]

Then

\[
 \boxed{
 \dim\operatorname {Ran}{\bf1}_{(-\infty,0)}(A_L)
 \le\frac{2LT_L}{\pi}.
 }
 \tag{28}
\]

#### Proof

For every unit \(v\) in the negative spectral subspace,
\(\langle A_Lv,v\rangle\le0\).  Hence

\[
 c_0\int\log(2+|t|)|\widehat v(t)|^2\frac{dt}{2\pi}
 \le C_0+b_L.
 \tag{29}
\]

With an immaterial enlargement of \(T_L\), this implies

\[
 \int_{|t|>T_L}|\widehat v(t)|^2\frac{dt}{2\pi}\le\frac12.
 \tag{30}
\]

Let \((v_j)_{j=1}^d\) be orthonormal in the negative space and let
\(\Pi_{T_L}\) be the Fourier band projection.  Then

\[
 \frac d2
 \le\sum_{j=1}^d\|\Pi_{T_L}v_j\|^2
 \le\operatorname {Tr}(P_{I_L}\Pi_{T_L}P_{I_L})
 =\frac{LT_L}{\pi}.
 \tag{31}
\]

This proves (28).  \(\square\)

For the completed semilocal Weil operator, the Riemann--Siegel multiplier
has (26), while the known absolute estimate for the prime block and polar
rank-two block is

\[
 b_L=O(\lambda).
 \tag{32}
\]

Thus Theorem 4 gives only

\[
 \boxed{\dim\mathcal N_L=O\!\left(Le^{C\lambda}\right).}
 \tag{33}
\]

A positive lower frame bound requires \(\dim\mathcal N_L\le M_L\).  To make
the trace estimate fit \(M_L\asymp2\lambda^2\), one would need

\[
 T_L=O(\lambda^2/L).
 \tag{34}
\]

Gamma coercivity at that bandwidth is only \(O(\log\lambda)\), whereas the
known perturbation norm is \(O(\lambda)\).  Hence (34) cannot follow from
(26) and the absolute bound (32).

This is a limitation of the inputs, not a lower bound on the actual negative
index.  In particular, (33) does not prove
\(\dim\mathcal N_L>M_L\).

## 6. Binding consequence

The many-vector proposal reduces to an exact dichotomy.

- Under RH, \(\mathcal N_L=\{0\}\), and its lower frame question is vacuous.
- Under a fixed negative branch, every complete co-Poisson mode annihilates
  the corresponding divisor channel and every truncated family satisfies
  the conservation obstruction (9), (13), and (15).

Therefore

\[
 \frac{\mathcal R_{-,\mathrm{HS}}(Q_L)}
      {\sqrt{a_-(Q_L)}}\longrightarrow0
 \tag{35}
\]

is not supplied by the prolate ladder.  By Theorem 1, it is itself a theorem
excluding the fixed negative branch.

The scale audit identifies what a new input must do.  On the candidate
negative space, a signed coupled ordinary-prime--Gamma estimate must lower
the **effective** perturbation from \(O(\lambda)\) to the logarithmic scale
required by \(T_L=O(\lambda^2/L)\), and must simultaneously prove a
quantitative angle to the moving co-Poisson span.  Neither statement follows
from Poisson summation, fixed-order Slepian leakage, or abstract frame
theory.

No assertion here proves that such a signed estimate is impossible.  The
result is that the current \(d_4/d_8\), \(M_L\asymp2\lambda^2\), and
\(O(\lambda)\) inputs cannot prove it, together with the exact residual
identity that every successor must beat.
