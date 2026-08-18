# D.149 — The rank-two primitive defect and the correct Feshbach certificate

## Verdict

Let \(L_N\) be the first \(N\) Legendre modes on \([-T,T]\), and let

\[
 \mathcal P_T=\ker M_-\cap\ker M_+
\]

be the two-Tate primitive space.  Eliminating two Legendre coefficients,
as in D.148, certifies the compression on

\[
 V_N=L_N\cap\mathcal P_T,qquad \dim V_N=N-2.          \tag{0.1}
\]

It does **not** yield a low/high decomposition whose complementary space is
contained in \(L_N^\perp\).  There is a rank-two primitive defect.  Hence
the directed positivity of D.148 and the Legendre-complement estimate of
D.93 cannot by themselves prove positivity on the whole primitive space.

The correct finite space is instead

\[
 W_N=P_TL_N\subset\mathcal P_T,                        \tag{0.2}
\]

where \(P_T\) is the exact Tate orthogonal projector.  Under the verified
nondegeneracy condition \(L_N\cap\operatorname {Ran}M^*=0\),
\(\dim W_N=N\), and

\[
 \boxed{W_N^\perp\cap\mathcal P_T=L_N^\perp\cap\mathcal P_T.}       \tag{0.3}
\]

Thus D.93 applies to the complement of (0.2), but the finite compression
must include the two additional projected polar directions.

For a self-adjoint primitive operator \(A_T\), a complete endpoint
certificate then consists of three directed inequalities:

1. a complement gap \(Q A_T Q\ge\delta Q\), \(\delta>0\);
2. the exact finite matrix \(B=S^*A_TS\) on a synthesis
   \(S:\mathbb C^N\to W_N\);
3. a residual enclosure \(\widetilde R\ge S^*A_TQA_TS\) satisfying

\[
 \boxed{B-\delta^{-1}\widetilde R\ge0.}                \tag{0.4}
\]

Equation (0.4), not positivity of \(B\) alone, proves \(A_T\ge0\) on the
whole primitive space.  This note proves the criterion and gives the exact
residual matrix that remains to be enclosed at \(T=\frac12\log5\).
No sign is assumed, and the paper is not modified.

## 1. Tate projector and the two finite spaces

Let \(H=L^2([-T,T])\), and let

\[
 M:H\longrightarrow\mathbb C^2,qquad
 MF=(M_-(F),M_+(F)).                                    \tag{1.1}
\]

The moment Gram matrix is

\[
 \mathsf G_T=MM^*=
 \begin{pmatrix}2\sinh T&2T\\2T&2\sinh T\end{pmatrix}>0,           \tag{1.2}
\]

so the primitive orthogonal projector is

\[
 P_T=I-M^*\mathsf G_T^{-1}M.                           \tag{1.3}
\]

Let \(\Phi_N:\mathbb C^N\to H\) synthesize the normalized Legendre
basis, and put \(J_N=M\Phi_N\).  Then

\[
 V_N=\Phi_N\ker J_N,                                   \tag{1.4}
\]

which is the graph-eliminated space used in D.148.  If \(J_N\) has rank
two, its dimension is \(N-2\).

The synthesis of the correct low space is

\[
 S_N=P_T\Phi_N.                                        \tag{1.5}
\]

Its Gram matrix is explicit:

\[
 G_N=S_N^*S_N=I_N-J_N^*\mathsf G_T^{-1}J_N.            \tag{1.6}
\]

It is positive definite precisely when
\(L_N\cap\operatorname {Ran}M^*=0\).  In the present problem
\(\operatorname {Ran}M^*=\operatorname {span}(e^{-t/2},e^{t/2})\),
and no nonzero linear combination of these exponentials is a polynomial
on an interval.  Hence (1.6) is strictly positive for every finite \(N\).

## 2. The rank-two defect

The inclusion \(V_N\subset W_N\) follows from (1.3): if \(v\in V_N\),
then \(P_Tv=v\).  Their dimensions are \(N-2\) and \(N\), respectively.
Thus

\[
 \dim(W_N\ominus V_N)=2.                               \tag{2.1}
\]

Equivalently, the primitive orthogonal complement of \(V_N\) has two
directions with nonzero low Legendre projection.  They are the projected
polar directions.  Therefore

\[
 \mathcal P_T\cap V_N^\perp
 \not\subset L_N^\perp.                                \tag{2.2}
\]

This is why shorting two coordinates and then invoking a bound on
\(L_N^\perp\) leaves an unmeasured rank-two sector.

By contrast, if \(y\in\mathcal P_T\), then for every \(x\in L_N\),

\[
 \langle y,P_Tx\rangle=\langle P_Ty,x\rangle=\langle y,x\rangle.
\]

Consequently \(y\perp W_N\) if and only if \(y\perp L_N\), proving
(0.3).

## 3. Feshbach inequality in a nonorthogonal finite frame

Work now in the Hilbert space \(H_0=\mathcal P_T\).  Let \(A\) be the
self-adjoint operator associated with the closed primitive quadratic form,
and assume \(W=\operatorname {Ran}S\subset\operatorname {Dom}A\), with
\(S:\mathbb C^N\to H_0\) injective.  Put

\[
 G=S^*S,qquad P=SG^{-1}S^*,qquad Q=I-P,qquad B=S^*AS.              \tag{3.1}
\]

Assume the directed complement estimate

\[
 QAQ\ge\delta Q,qquad\delta>0.                        \tag{3.2}
\]

For \(x=Sc\in W\) and \(y\in QH_0\), completion of the square gives

\[
\begin{aligned}
 \langle A(x+y),x+y\rangle
 &\ge c^*Bc+2\operatorname {Re}\langle QASc,y\rangle
       +\delta\|y\|^2\\
 &\ge c^*Bc-\delta^{-1}\|QASc\|^2.                  \tag{3.3}
\end{aligned}
\]

Therefore, if an interval matrix \(\widetilde R\) satisfies

\[
 c^*\widetilde Rc\ge\|QASc\|^2
 \quad(c\in\mathbb C^N),                              \tag{3.4}
\]

then (0.4) implies \(A\ge0\).  This proves the stated Feshbach
certificate without assuming that \(W\) reduces \(A\).

If \(AS\) is Hilbert-valued, the exact residual Gram is

\[
\begin{aligned}
 R&=S^*AQAS\\
  &=S^*A^2S-BG^{-1}B.                                  \tag{3.5}
\end{aligned}
\]

Formula (3.5) follows from \(P=SG^{-1}S^*\).  It is positive
semidefinite because it is \((QAS)^*(QAS)\).

If \(A=P_T\widetilde A P_T\) is obtained by primitive compression of a
full-space multiplier, then

\[
 R=S^*\widetilde A P_T\widetilde A S-BG^{-1}B
 \le S^*\widetilde A^2S-BG^{-1}B.                     \tag{3.6}
\]

Thus the right side of (3.6) is a safe residual majorant.  It is computable
from the squared complete multiplier and contains, without separation,
every \(p^k\) and the full Gamma factor.

## 4. Application at the first critical endpoint

At \(T=\frac12\log5\), the active contacts are exactly \(2,3,4\).
D.91 and D.93 give the directed lower bound

\[
 \langle Ay,y\rangle\ge0.219\,\|y\|^2
 \qquad(y\in L_{170}^\perp).                           \tag{4.1}
\]

By (0.3), this applies to the complement of
\(W_{170}=P_TL_{170}\) inside the primitive space.  A complete endpoint
proof therefore requires:

* augmenting the D.148 finite compression by the two directions
  \(W_{170}\ominus V_{170}\);
* enclosing the squared-multiplier residual in (3.6); and
* proving (0.4) by a directed congruence.

The full Hurwitz--Lerch Gamma matrix of D.147 closes the linear Gamma block,
but not the squared-multiplier residual.  D.148 is consequently a rigorous
certificate on \(V_{170}\), not yet a certificate for the complete endpoint.

