# D.176 — Tate-centered return dissipation

## Verdict

Tate centering is stable under every exact return.  Let

\[
 R=X_0^*X_0,qquad L=Y_0^*Y_0,qquad
 T=R^{\dagger/2}LR^{\dagger/2},qquad D=I-T,         \tag{0.1}
\]

on the two-moment primitive source, and let (q) be the centered cross of
D.175.  Define

\[
 m_k=q^*T^kq,qquad d_k=m_k-m_{k+1}.                 \tag{0.2}
\]

Then

\[
 \boxed{
 d_k=q^*T^{k/2}DT^{k/2}q
 =-B_{\rm nuc}(F_k,F_k),
 \qquad F_k=R^{\dagger/2}T^{k/2}q.}                 \tag{0.3}
\]

Every (F_k) still satisfies the two exact A--B--C primitive moments.
Consequently D.133 applies at every (k), and (0.3) has the termwise
centered expansion

\[
 \boxed{
 d_k=\mathcal H_{5/4}(F_k)
 -2\int_{[1,e^{2T}]}x^{-1/2}
       \mathrm{Re}\,C_{F_k}(\log x)\,dE_\beta(x).} \tag{0.4}
\]

Here

\[
 dE_\beta=d\psi_C-dx+{\beta\over2}\delta_1,         \tag{0.5}
\]

so (0.4) contains the full Gamma place and every (p^j), while the
continuous Chebyshev main term is removed by the two Tate moments before
the next inverse is taken.

The return capacity has the exact Abel dissipation formula

\[
 \boxed{
 \sum_{k\ge0}m_k
 =\sum_{k\ge0}(k+1)d_k,}                             \tag{0.6}

provided the supported tail ((k+1)m_{k+1}) tends to zero; otherwise the
missing tail records exactly the infinite-capacity/range obstruction.
Thus the sought summable estimate is no longer an untyped decay of
abstract moments.  It is a first-moment bound for the sequence of exact
centered A--B--C dissipations along the return orbit.

## 1. The primitive space reduces every return

Let (P) be the exact rank-two projection killing
(M_-,M_+).  The actual old features are (X_0P) and (Y_0P).  Hence

\[
 R=PRP,qquad L=PLP                                  \tag{1.1}
\]

as operators on the supported primitive source.  Their functional
calculi, including (R^{\dagger/2}) and (T^{k/2}), therefore act within
(P\mathcal H).  In particular

\[
 M_\pm(F_k)=0\qquad(k\ge0).                          \tag{1.2}
\]

This is the exact reason Tate centering survives an arbitrary number of
returns.  It would fail if (R^{-1}) were replaced by an ambient scalar
inverse or if the rank-two projection were applied only to (q).

## 2. Consecutive returns are the completed defect form

Since (D=I-T) is a bounded Borel function of (T), it commutes with every
(T^{k/2}).  Therefore

\[
\begin{aligned}
 d_k
 &=q^*T^kq-q^*T^{k+1}q\\
 &=q^*T^{k/2}(I-T)T^{k/2}q.                          \tag{2.1}
\end{aligned}
\]

If (z_k=T^{k/2}q) and (F_k=R^{\dagger/2}z_k), then

\[
\begin{aligned}
 z_k^*Dz_k
 &=z_k^*R^{\dagger/2}(R-L)R^{\dagger/2}z_k\\
 &=\langle X_0F_k,X_0F_k\rangle
   -\langle Y_0F_k,Y_0F_k\rangle\\
 &=-B_{\rm nuc}(F_k,F_k).                            \tag{2.2}
\end{aligned}
\]

This proves (0.3).  Under the old-cell induction hypothesis (D\ge0),
the sequence (m_k) is decreasing and every (d_k\ge0).  No positivity of
the enlarged cell is used.

## 3. Exact centering at every level

Polarization of the two-moment identity gives, for any primitive (F,G),

\[
 \int_0^{2T}e^{a/2}
   \bigl(C_{F,G}(a)+\overline{C_{G,F}(a)}\bigr)da
 =-\int_0^{2T}e^{-a/2}
   \bigl(C_{F,G}(a)+\overline{C_{G,F}(a)}\bigr)da.   \tag{3.1}
\]

Apply this with the returned vectors (F_k) from (1.2).  The continuous
(dx) part of the prime-power synthesis is converted into the
(Q_{1/2}) Gamma-resolvent channel and the digamma index shifts from
(1/4) to (5/4), exactly as in D.133.  Hence (2.2) becomes (0.4).

The atomic part of (0.4) is explicitly

\[
 2\sum_{p^j\le e^{2T}}{\log p\over p^{j/2}}
       \mathrm{Re}\,C_{F_k}(j\log p),           \tag{3.2}
\]

and no other integer occurs.  Thus all Frobenius depths (p^j) survive
at every return, with their A--B determinant mass (\log p) and central
metric weight (p^{-j/2}).

## 4. Abel summation and the exact tail

For every (M\ge0), elementary summation by parts gives

\[
 \boxed{
 \sum_{k=0}^{M}m_k
 =\sum_{k=0}^{M}(k+1)d_k+(M+1)m_{M+1}.}              \tag{4.1}

Indeed, expand (d_k=m_k-m_{k+1}) and telescope.  All terms are positive
under (D\ge0).  If (q) has a component in (\ker D), then (m_k) has a
nondecaying component, the last term in (4.1) diverges, and the return
capacity is infinite.  If (q\in\mathrm{Dom}\,D^{-1/2}), spectral
monotone convergence gives

\[
 (M+1)m_{M+1}\longrightarrow0                       \tag{4.2}
\]

and (0.6) follows.  Conversely, finiteness of the right side of (0.6)
implies (4.2) and the required range condition.

Thus a correctly normalized final estimate may be stated as

\[
 \boxed{
 \sum_{k\ge0}(k+1)
 \left[
 \mathcal H_{5/4}(F_k)
 -2\int x^{-1/2}\mathrm{Re}\,C_{F_k}(\log x)
                \,dE_\beta(x)
 \right]
 \le \mathcal C_{\rm born}.}                        \tag{4.3}

This is equivalent to the centered (q^*D^\dagger q) term isolated in
D.175.  It is the summable estimate still to prove, but now every summand
is an exact source-derived A--B--C object and is Tate-centered before the
next return.

The accompanying verifier checks (0.3), (0.6), (4.1), the kernel-tail
case and matrix-valued boundary polarization on noncommuting finite
matrices.
