# Hard-edge correction and fixed-window collapse

## Purpose

This note repairs the lower-endpoint geometry in `103_03` and records an
exact cancellation which is available on every fixed interval.  It does not
prove the A1 inequality.  Its role is to separate a genuine finite-window
cancellation from the still-open, expanding-range cancellation.

Write
\[
 N=n-1,\qquad K_n(u)=e^{-u}L_N^{(2)}(u),\qquad
 G_N(u)=e^{-u}L_N^{(1)}(u).
\]
The zeros of \(L_N^{(2)}\) are denoted by
\(0<\xi_{N,1}<\cdots<\xi_{N,N}\).

## 1. A fixed positive lower endpoint cannot precede every zero

The assertion \(T_8<\xi_{N,1}\) for fixed \(T_8>0\) and all sufficiently
large \(N\) is false.  An elementary, fully explicit bound already proves
this.

> **Lemma 1 (exact hard-edge upper bound).**  For every \(N\ge1\),
> \[
> \boxed{\quad \xi_{N,1}\le {6\over\sqrt{N+3}}.\quad}                 \tag{1}
> \]
> Consequently \(\xi_{N,1}<T_8\) once \(N>36/T_8^2-3\).

*Proof.*  Normalize \(L_N^{(\alpha)}\) by its value at zero and write its
zeros as \(x_1,\ldots,x_N\).  Comparing the first two coefficients gives
\[
 \sum_i{x_i}^{-1}={N\over\alpha+1},\qquad
 \sum_{i<j}(x_ix_j)^{-1}
 ={N(N-1)\over2(\alpha+1)(\alpha+2)}.
\]
Therefore
\[
 \sum_i{x_i}^{-2}
 ={N(N+\alpha+1)\over(\alpha+1)^2(\alpha+2)}.
\]
The largest summand is at least the average, so
\[
 {1\over x_1^2}\ge {N+\alpha+1\over(\alpha+1)^2(\alpha+2)}.
\]
Set \(\alpha=2\).  This is (1). \(\square\)

For orientation, the actual fixed-window count has the standard hard-edge
form
\[
 r_N(B):=\#\{j:\xi_{N,j}\le B\}
 ={2\over\pi}\sqrt{NB}+O_B(1)\qquad(B>0\ \hbox{fixed}).              \tag{2}
\]
The factor \(2\) is essential.  It follows either from the
Mehler--Heine/Bessel scaling or directly from the Laguerre differential
equation after the Liouville substitution
\[
 v(u)=u^{3/2}e^{-u/2}L_N^{(2)}(u),\qquad
 v''+\left({N+3/2\over u}-{1\over4}-{3\over4u^2}\right)v=0.
\]
Its Prüfer phase on \([0,B]\) is \(2\sqrt{NB}+O_B(1)\), and division by
\(\pi\) gives (2).  Formula (2) is explanatory only; Lemma 1 alone is
enough for the endpoint correction.

Hence the correct first lobe in the integral beginning at \(T_8\) is
\[
 (T_8,\xi_{N,r_N(T_8)+1}),
\]
not \((T_8,\xi_{N,1})\).  All zeros after that first truncated lobe, and
the final sign-definite ray after \(\xi_{N,N}\), are unchanged.

## 2. Exact collapse of the fixed arithmetic window

Let \(a=\log2\) and let \(b\ge a\) be fixed and not the logarithm of a
prime power.  Then the fixed-window correlation has the exact finite form
\[
\boxed{
\begin{aligned}
 I_N(a,b)&:=\int_a^b(\psi(e^u)-e^u)K_n(u)\,du\\
 &=\sum_{2\le m\le e^b}\Lambda(m)
       \bigl(G_N(\log m)-G_N(b)\bigr)\\
 &\quad-L_{N+1}^{(1)}(a)+L_{N+1}^{(1)}(b).
\end{aligned}}                                                       \tag{3}
\]
The endpoint convention is the one in `103_01`: a jump at \(a\) is
included.  A term with \(\Lambda(m)=0\) is harmless, so the displayed
finite sum needs no separate integer-endpoint convention at \(b\).

*Proof.*  The derivative identities are
\[
 G_N'(u)=-K_n(u),\qquad {d\over du}L_{N+1}^{(1)}(u)=-L_N^{(2)}(u).
\]
On \([a,b]\), the step function \(\psi(e^u)\) equals the sum of its jumps
\(\Lambda(m)\) with \(\log m\le u\).  Interchanging this finite sum with
the integral yields
\[
 \int_a^b\psi(e^u)K_n(u)\,du
 =\sum_{2\le m\le e^b}\Lambda(m)\int_{\log m}^bK_n(u)\,du
 =\sum_{2\le m\le e^b}\Lambda(m)(G_N(\log m)-G_N(b)).
\]
Also
\[
 \int_a^be^uK_n(u)\,du=\int_a^bL_N^{(2)}(u)\,du
 =L_{N+1}^{(1)}(a)-L_{N+1}^{(1)}(b).
\]
Subtracting proves (3). \(\square\)

Taking \(b=T_8\), formula (3) is exactly the finite-data term occurring
in `103_01`, Corollary 3.  It makes visible a cancellation that the absolute
bound in `103_02` suppresses.  In particular, fixed-argument Laguerre
asymptotics give
\[
 L_N^{(1)}(u)=O_u(N^{1/4})\qquad(u>0\ \hbox{fixed}),
\]
and therefore
\[
 \boxed{\ I_N(\log2,T_8)=O_{T_8}(N^{1/4}).\ }                         \tag{4}
\]
This is sharper than the previously used absolute estimate
\(O_{T_8}(N^{3/4})\).  Equation (3), not a pointwise envelope, is the
reason: the \(\asymp\sqrt N\) hard-edge lobes telescope against a step
function having only finitely many jumps in a fixed window.

## 3. What this does and does not repair

The contribution (4) is negligible against the reserve
\(q(n)\asymp n\log n\).  Thus the omitted hard-edge lobes neither account
for the reserve margin nor furnish the missing A1 cancellation.  They are
already absorbed into finite arithmetic data.

The open integral starts at a fixed endpoint but then ranges through
\([T_8,4N]\), where the number of prime-power jumps grows exponentially
with the endpoint.  The finite interchange used in (3) remains an identity
there, but supplies no uniform sign: its resulting Laguerre coefficients
are exactly the sign-changing coefficients of the original direct
certificate.  Consequently this correction removes a false geometric
claim and sharpens the fixed term; it does not bypass the RH-strength
transport/positivity gate.

## 4. Dependence audit

* `103_03` required correction only in its statement of the first lobe and
  its claim that the entire oscillatory region lies above \(T_8\).  Its bulk
  width estimates, which are used for \(u\asymp N\), are unaffected.
* `103_05` constructs its competitor from zeros in \([2N,3N]\).  Since
  \(T_8\) is fixed, that interval lies above \(T_8\) for large \(N\); its
  no-go proof is unaffected.
* `103_01` and `103_04` remain algebraically correct.  Formula (3) merely
  evaluates their already finite low-window term without an absolute-value
  loss.
