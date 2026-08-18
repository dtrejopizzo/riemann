# D.146 — Exact Hurwitz--Lerch summation of the finite Gamma block

## Verdict

On every finite Legendre subspace, the **entire** quarter-shift Gamma
oscillator can be summed in closed form.  No oscillator truncation, tail
atom or Fourier quadrature is necessary.

Let (D) be differentiation in the Legendre basis
((P_0,\ldots,P_{N-1})), let

\[
 W=\mathrm{diag}\,\left({1\over2m+1}\right)_{m=0}^{N-1},
 \qquad
 S=\mathrm{diag}\,\left(\sqrt{2m+1}\right)_{m=0}^{N-1},       \tag{0.1}
\]

and define the normalization

\[
 \mathcal N_T(M)={T\over2}SMS.                         \tag{0.2}
\]

The polynomial resolvent is

\[
 Q(x)=x(I+xD)^{-1}
 =\sum_{r=0}^{N-1}(-1)^rx^{r+1}D^r.                  \tag{0.3}
\]

From (Q) and the two endpoint derivative vectors one obtains finite
matrix polynomials

\[
 R(x)=\sum_{r=1}^{2N}R_rx^r,qquad
 S_\partial(x)=\sum_{r=2}^{2N}S_rx^r,                \tag{0.4}
\]

specified in Section 2.  If (b_j=2j+\tfrac12=2(j+\tfrac14)), then the
exact matrix of the positive Gamma difference form is

\[
\boxed{
 \begin{aligned}
 \mathsf G_{\Gamma,N}(T)
 =-\mathcal N_T\sum_{r=2}^{2N}{T^{-r}\over2^r}
 \bigg[&\zeta\left(r,{1\over4}\right)R_r\\
 &+e^{-T}\Phi\left(e^{-4T},r,{1\over4}\right)S_r
 \bigg].
 \end{aligned}}                                      \tag{0.5}
\]

Here (Phi) is the Lerch transcendent.  The potentially divergent
(r=1) coefficient cancels **exactly** against (2b_j^{-1}I) before the
sum is taken.  At (T=\tfrac12\log5), the Lerch argument is simply

\[
 e^{-4T}={1\over25},qquad e^{-T}={1\over\sqrt5}.     \tag{0.6}
\]

Formula (0.5) turns the remaining (T=\tfrac12\log5) low-block problem
into a finite interval-matrix congruence involving rational integers,
(log5), Hurwitz zeta and a rapidly convergent Lerch series.  It also
explains the tiny numbers seen after the stable D.145 correction: the
finite oscillator lower models approach the exact matrix through a
positive tail, and the decisive margins are differences of large endpoint
terms.  Hundreds of digits may be required at (N=80) or (170); a
double-precision centre is not evidence.

The formula is proved below and independently verified on finite matrices.
It does not yet assert the directed positivity of the final constrained
block.  The paper is not modified.

## 1. Finite polynomial resolvent

On polynomials of degree below (N), (D^N=0).  Therefore

\[
 (I+xD)^{-1}=\sum_{r=0}^{N-1}(-xD)^r,                \tag{1.1}
\]

which proves (0.3).  The (n)-th column of (Q(1/k)) is exactly the
coefficient vector of the polynomial (Q_n) in D.145 satisfying

\[
 Q_n'+kQ_n=P_n.                                      \tag{1.2}
\]

Let

\[
 \epsilon=(1,-1,1,-1,\ldots)^t,qquad
 q^-(x)=Q(x)^t\epsilon.                               \tag{1.3}
\]

Thus (q_n^-(x)=Q_n(-1)).

For (0\leq s\leq m), the endpoint derivatives are

\[
 P_m^{(s)}(1)={(m+s)!\over2^ss!(m-s)!},qquad
 P_m^{(s)}(-1)=(-1)^{m+s}P_m^{(s)}(1).                \tag{1.4}
\]

Define the vector polynomials

\[
\begin{aligned}
 a_m(x)&=\sum_{s=0}^{m}P_m^{(s)}(-1)x^{s+1},\\
 b_m(x)&=\sum_{s=0}^{m}P_m^{(s)}(1)x^{s+1}.           \tag{1.5}
\end{aligned}
\]

Repeated integration by parts, which terminates because (P_m) is a
polynomial, gives the exact endpoint integral

\[
 \int_{-1}^{1}P_m(u)e^{-k(u+1)}\,du
 =a_m(k^{-1})-e^{-2k}b_m(k^{-1}).                     \tag{1.6}
\]

This is the finite-series version of the scaled-Bessel formula (0.4) in
D.145.

## 2. The two matrix polynomials

Set

\[
\begin{aligned}
 R(x)&=2WQ(x)-a(x)q^-(x)^t
      +\bigl(2WQ(x)-a(x)q^-(x)^t\bigr)^t,\\
 S_\partial(x)&=b(x)q^-(x)^t+\bigl(b(x)q^-(x)^t\bigr)^t.  \tag{2.1}
\end{aligned}
\]

The stable triangular integral of D.145 then says, as an **identity of
finite matrices**,

\[
 E_b(T)=\mathcal N_T\left(
 R((bT)^{-1})+e^{-2bT}S_\partial((bT)^{-1})
 \right),                                             \tag{2.2}
\]

where (E_b(T)) has entries

\[
 \int_{-T}^T\!\int_{-T}^T
 \phi_m(x)e^{-b|x-y|}\phi_n(y)\,dx\,dy.              \tag{2.3}
\]

The degrees in (0.4) follow immediately: (Q,a,b) have degree at most
(N), so their boundary products have degree at most (2N).

The first coefficient is

\[
 R_1=4W.                                              \tag{2.4}
\]

Indeed the boundary products begin in degree two and the first coefficient
of (Q) is the identity.  Hence

\[
 \mathcal N_T(T^{-1}R_1)=2I.                          \tag{2.5}
\]

Equation (2.5) is the exact cancellation of the (2/b) term:

\[
 {2\over b}I-E_b(T)
 =-\mathcal N_T\sum_{r=2}^{2N}T^{-r}b^{-r}
 \left(R_r+e^{-2bT}S_r\right).                       \tag{2.6}
\]

The notation in (2.6) means that the exponential multiplies only the
(S_r) coefficient, as in (2.2).

## 3. Summing every oscillator

For (r>1),

\[
 \sum_{j\geq0}b_j^{-r}
 =2^{-r}\zeta\left(r,{1\over4}\right).               \tag{3.1}
\]

Moreover

\[
\begin{aligned}
 \sum_{j\geq0}e^{-2b_jT}b_j^{-r}
 &=e^{-T}2^{-r}
 \sum_{j\geq0}{(e^{-4T})^j\over(j+1/4)^r}\\
 &=e^{-T}2^{-r}
 \Phi\left(e^{-4T},r,{1\over4}\right).              \tag{3.2}
\end{aligned}
\]

Substituting (3.1)--(3.2) into (2.6) proves (0.5).  Every sum is absolutely
convergent because (r\geq2).  Thus the interchange of the finite matrix
sum with the oscillator sum is justified entry by entry.

## 4. Exact completed low block

The Fourier multiplier represented by (0.5) is

\[
 \mathrm{Re}\,\psi(1/4+i\tau/2)-\psi(1/4).      \tag{4.1}
\]

Consequently the completed archimedean matrix is

\[
 \mathsf G_{\Gamma,N}(T)-m_0I,
 \qquad
 m_0=\log\pi-\psi(1/4)
 =\log\pi+\gamma+{\pi\over2}+3\log2.                \tag{4.2}
\]

For (T=\tfrac12\log5), the active finite contacts are (n=2,3,4).
Their matrices are the exact polynomial integrals (4.1) of D.145 with
coefficients

\[
 {\log2\over\sqrt2},qquad
 {\log3\over\sqrt3},qquad
 {\log2\over2}.                                      \tag{4.3}
\]

Subtracting those three symmetric contact matrices from (4.2), and then
eliminating the two exact moment columns (4.2) of D.145, gives the exact
finite constrained block.  A rigorous LDL congruence of that matrix,
together with the already directed prolate-complement estimate, is a full
certificate for this endpoint.  Formula (0.5) ensures that no unmeasured
Gamma tail remains outside that congruence.

## 5. Precision and interval evaluation

The coefficients in (1.4) grow factorially while their final combinations
in (0.5) remain moderate.  Therefore the safe evaluation order is:

1. construct the integer coefficient tensors (R_r,S_r) exactly;
2. evaluate the scalar Hurwitz--Lerch factors as directed intervals;
3. accumulate the matrix at precision exceeding the largest cancellation;
4. eliminate the two moment columns by an interval QR or by an exact
   two-column graph parametrization; and
5. certify the final symmetric matrix with interval LDL, including the
   accumulated entry radii.

At (N=40), a 100-digit accumulation is already insufficient: intermediate
terms can exceed (10^{147}).  This observed cancellation is consistent
with the factorial endpoint derivatives and is why a high-precision centre
and an explicit radius are mandatory.
