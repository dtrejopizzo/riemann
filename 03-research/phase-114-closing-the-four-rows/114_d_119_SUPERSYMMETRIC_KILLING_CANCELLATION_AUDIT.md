# D.119 — Supersymmetric cancellation of the Doob killing

## Verdict

The two Tate jets admit a canonical rank-two supersymmetric presentation,
and the boson--fermion supertrace cancels the divergent Doob/Gamma killing
mode by mode.  This explains why a finite completed **character** can survive
although neither the arithmetic nor the Gamma ground-state generator has a
cofinal conservative limit.

The cancellation does not yield a positive Hilbert form on cohomology.
For an ordinary Hilbert complex, the Witten Laplacian is a sum of squares;
zero-order masses are added, never subtracted.  The completed primitive
operator is instead

\[
 L_X-(2A_X+m_0)I=-B_{{\rm nuc},X}.                    \tag{0.1}
\]

Factoring (0.1) before proving its positivity requires a negative metric in
the mass channel.  The natural factorization is therefore Pontryagin/Krein,
not Hilbert.  Promoting its primitive range to a positive Hilbert space is
equivalent to row D.

Moreover, supersymmetry fixes the index (the two jet classes) but does not
fix the first positive eigenvalue.  A finite-dimensional exact countermodel
with two cohomology classes and arbitrary gap makes this obstruction
formal.

## 1. The two elementary jet supercharges

In logarithmic coordinates let

\[
 Q_+=\partial_t-\tfrac12,
 \qquad
 Q_-=\partial_t+\tfrac12.                              \tag{1.1}
\]

Then

\[
 Q_+e^{t/2}=0,
 \qquad
 Q_-e^{-t/2}=0.                                       \tag{1.2}
\]

On compactly supported functions in Lebesgue \(L^2\),

\[
 Q_+^*=-\partial_t-\tfrac12,
 \qquad
 Q_-^*=-\partial_t+\tfrac12,                           \tag{1.3}
\]

so both even Witten Laplacians are

\[
 Q_\pm^*Q_\pm=-\partial_t^2+\tfrac14.                 \tag{1.4}
\]

The reciprocal exponentials are boundary zero modes, not \(L^2\) ground
states on the full line.  Taking \(Q_+\oplus Q_-\) packages precisely the
two Tate jets.  It does not yet contain the arithmetic contact or Gamma
oscillator.

## 2. Source-derived graph supercharge

For finite cutoff \(X\), D.117 gives the positive edge differential

\[
 (\partial_XF)_{p^k}
 =\left({\log p\over p^{k/2}}\right)^{1/2}
   (F-S_{k\log p}F)                                    \tag{2.1}
\]

together with the Gamma heat differential

\[
 (\partial_\infty F)(r)
 =g_\infty(r)^{1/2}(F-S_rF),
 \qquad
 g_\infty(r)={e^{-r/2}\over1-e^{-2r}}.                \tag{2.2}
\]

Thus

\[
 \partial_X^*\partial_X=L_X.                          \tag{2.3}
\]

The associated odd self-adjoint supercharge and Witten Laplacian are

\[
 \mathcal Q_X=
 \begin{pmatrix}0&\partial_X^*\\\partial_X&0\end{pmatrix},
 \qquad
 \mathcal Q_X^2=
 \begin{pmatrix}
 L_X&0\\0&\partial_X\partial_X^*
 \end{pmatrix}.                                       \tag{2.4}
\]

Every nonzero singular value of \(\partial_X\) occurs once in each parity.
Consequently its contribution cancels in

\[
 \operatorname{Str}(e^{-t\mathcal Q_X^2}).             \tag{2.5}
\]

This is the exact mechanism by which prime-power and Gamma modes can cancel
in a character while remaining positive in each parity separately.

## 3. What happens to the Doob killing

Let \(C_{X,R}^{\rm Doob}\) be the positive ground-state compensation of
D.118, with Gamma range truncated at \(R\).  Adding the same scalar to the
two supersymmetric partners gives

\[
 \Delta_{0,X,R}=\partial_X^*\partial_X+C_{X,R}^{\rm Doob}I,
 \qquad
 \Delta_{1,X,R}=\partial_X\partial_X^*
                    +C_{X,R}^{\rm Doob}I.             \tag{3.1}
\]

The common scalar cancels in the **difference of traces** after the paired
spectra are matched.  It does not cancel in either Hilbert quadratic form:

\[
 \langle F,\Delta_{0,X,R}F\rangle
 =\|\partial_XF\|^2+C_{X,R}^{\rm Doob}\|F\|^2.        \tag{3.2}
\]

At Gamma, the linear divergence from D.118 is therefore harmless for a
regularized supercharacter but remains a positive infinite killing in the
even energy.  Boundary/eta regularization may retain a finite anomaly; in
the present programme that anomaly is precisely the already-constructed
Gamma determinant in row C.  An anomaly in a supertrace is not a positive
norm on the primitive cohomology.

## 4. The completed counterterm cannot be a Hilbert square for free

Write

\[
 c_X=2A_X+m_0.                                         \tag{4.1}
\]

An ordinary enlarged Hilbert differential

\[
 D_X^+F=(\partial_XF,\sqrt{c_X}F)                      \tag{4.2}
\]

satisfies

\[
 (D_X^+)^*D_X^+=L_X+c_XI.                             \tag{4.3}
\]

It has the wrong sign.  The exact factorization of the completed primitive
operator uses instead

\[
 \mathbb D_XF=(\partial_XF,\sqrt{c_X}F)                \tag{4.4}
\]

in the coefficient space

\[
 \mathcal K_X=\mathcal K_{\rm edge}\oplus\mathcal H,
 \qquad
 J_X=I_{\rm edge}\oplus(-I_{\mathcal H}).              \tag{4.5}
\]

Then

\[
 \boxed{
 \mathbb D_X^*J_X\mathbb D_X=L_X-c_XI
 =-B_{{\rm nuc},X}.}                                  \tag{4.6}
\]

This identity includes every \(p^k\) and Gamma mode through \(\partial_X\).
It is a Krein square, not a Hilbert square.

On the two-jet primitive space \(\mathcal P=\ker(M_-,M_+)\), a positive
Hilbert realization of (4.6) exists if and only if

\[
 \langle F,(L_X-c_XI)F\rangle\geq0
 \quad(F\in\mathcal P),                               \tag{4.7}
\]

which is exactly row D.  Choosing the positive square root of
\((L_X-c_XI)|_{\mathcal P}\) would therefore assume the theorem rather than
prove it.

## 5. Adding the jet boundary block gives the full Pontryagin complex

Before restriction to \(\mathcal P\), the two Tate moments form

\[
 M_XF=(M_-(F),M_+(F)),
 \qquad
 C=\begin{pmatrix}0&1\\1&0\end{pmatrix}.             \tag{5.1}
\]

The full Weil form has the exact factorization

\[
 QW_X(F,F)
 =\langle\partial_XF,\partial_XF\rangle
  -c_X\|F\|^2
  +\langle M_XF,CM_XF\rangle.                         \tag{5.2}
\]

The matrix \(C\) has inertia \((1,1)\).  Hence (5.2) is naturally the square
of the extended differential

\[
 F\longmapsto(\partial_XF,\sqrt{c_X}F,M_XF)            \tag{5.3}
\]

with coefficient metric

\[
 I_{\rm edge}\oplus(-I)\oplus C.                      \tag{5.4}
\]

This Pontryagin presentation is the correct supersymmetric analogue of the
Hodge-index problem: the two jets display the boundary hyperbolic plane,
while row D asserts that after removing it no additional wrong-sign
direction remains.

Supersymmetry organizes the signs and determinant cancellations, but it
does not prove that the displayed negative index is exhausted by the Tate
boundary block.

## 6. Exact countermodel: two jet classes do not fix the gap

For any \(\varepsilon>0\), consider the finite Hilbert complex

\[
 0\longrightarrow\mathbb C^3
 \xrightarrow{\ Q_\varepsilon\ }
 \mathbb C\longrightarrow0,
 \qquad
 Q_\varepsilon(x_1,x_2,x_3)=\varepsilon x_3.          \tag{6.1}
\]

Its even and odd Laplacians have spectra

\[
 \operatorname{Spec}(Q_\varepsilon^*Q_\varepsilon)
 =\{0,0,\varepsilon^2\},
 \qquad
 \operatorname{Spec}(Q_\varepsilon Q_\varepsilon^*)
 =\{\varepsilon^2\}.                                  \tag{6.2}
\]

Thus:

* the even cohomology has dimension two;
* the nonzero spectra pair exactly;
* \(\operatorname{Str}(e^{-t\Delta})=2\) for every \(t>0\); but
* the first positive eigenvalue is \(\varepsilon^2\), which is arbitrary.

Therefore a two-jet supersymmetric index, exact spectral pairing and a
positive Witten Laplacian do not determine any prescribed spectral gap.
The same logical freedom remains after imposing detailed balance or a
monoidal grading.

## 7. Cofinal and character conclusions

At every finite cutoff, the boson--fermion construction is well typed and
positive in each parity.  In the cofinal limit:

1. paired prime and Gamma energies may be removed from a regularized
   supertrace;
2. the remaining boundary anomaly is the nuclear character already present
   in row C;
3. the even Hilbert energy still contains the positive Doob killing;
4. subtracting the completed contact mass requires the negative channel in
   (4.5); and
5. positivity of that Krein square on primitive cohomology is exactly D.

Hence supersymmetry explains the finiteness and typing of the completed
character, but it does not turn that virtual character into a positive
Hilbert metric.  No gap \(2A_X+m_0\) follows from the Witten maximum
principle, the index, or boson--fermion cancellation alone.

