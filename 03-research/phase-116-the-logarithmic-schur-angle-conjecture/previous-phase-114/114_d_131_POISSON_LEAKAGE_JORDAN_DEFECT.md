# D.131 — Poisson leakage with the Jordan--Green first-chaos defect

## Verdict

Let \(P\) be the semilocal support projection, \(Q=1-P\), \(U\) the
self-dual Fourier--Poisson unitary and \(\widehat P=U^*PU\).  The supported
leakage

\[
 K_{\mathrm{leak}}=PU^*QUP=P-P\widehat PP                 \tag{0.1}
\]

is automatically positive.  Its pullback is an candid square.  It is not,
however, the completed primitive Weil form.  The exact identity is

\[
 \boxed{-B_{\mathrm{nuc}}
 =\mathcal L_{\mathrm{leak}}-\mathcal E_{\mathrm{cross}},} \tag{0.2}
\]

where \(\mathcal E_{\mathrm{cross}}\) is the Hermitian pullback of the
off-diagonal block \(Q\widehat PP\).  That block has both signs and is not
killed by the two Tate jets.

Completing the square replaces the indefinite cross block by a positive
Schur channel \(\mathcal J_P\), but with the decisive sign

\[
 \boxed{-B_{\mathrm{nuc}}
 =\mathcal L_{\mathrm{fold}}-\mathcal J_P^*\mathcal J_P.}  \tag{0.3}
\]

The Jordan--Green--beta construction has exactly the same relative sign:

\[
 \boxed{-B_{\mathrm{nuc}}
 =\mathbf B^*\mathbf B-\mathbf S^*\mathbf S.}              \tag{0.4}
\]

Here \(\mathbf S\) is the positive Jordan--Green first-chaos preparation,
containing every \(p^k\) and the Gamma constant, while \(\mathbf B\) is the
boundary differential containing the prime unit channels and the complete
Gamma oscillator.  Thus the first chaos is the positive channel that must
be subtracted from the leakage, not a second positive square that may be
added.  If \(\mathcal J_P\) were identified with \(\mathbf S\), adding it
would overshoot the target by \(2\mathbf S^*\mathbf S\).

The rational D.75 leakage is also not the Jordan covariance: their exact
Fourier multipliers differ.  Hence this attempted repair does not close D,
but it gives the requested exact defect and its sign.  No paper file is
modified.

## 1. Automatic leakage square

For every unitary \(U\) and orthogonal projection \(P\),

\[
 PU^*QUP=(QUP)^*(QUP)\geq0.                               \tag{1.1}
\]

Let \(A_T\) be the generally unsupported semilocal integrated-scaling
realization used by the corner trace and put \(M_T=PA_T\).  Then \(M_T\)
is supported, and its leakage pullback is

\[
 \begin{aligned}
 \mathcal L_T(F,G)
 &=\langle A_TF,PU^*QUPA_TG\rangle\\
 &=\langle QUM_TF,QUM_TG\rangle .                         \tag{1.2}
 \end{aligned}
\]

Consequently \(\mathcal L_T(F,F)\geq0\) without an arithmetic or spectral
hypothesis.  This is the precise contraction supplied by support.

There is a different supported realization furnished by the compact
potential \(\mathcal W_T\).  For ordinary Fourier transform its exact D.75
pullback is

\[
 \mathcal L_T^{\mathrm{rat}}(F,F)
 =\int_{\Omega_T^c}
 {|\widehat F(\tau)|^2\over(\tau^2+1/4)^2}\,d\tau .        \tag{1.3}
\]

The two primitive conditions make \(\mathcal W_TF\) compactly supported;
they do not turn (1.3) into the prime--Gamma form.

## 2. Exact corner--leakage defect

The semilocal character uses the unprojected realization \(A_T\):

\[
 \mathcal C_T(F,G)
 =\langle A_TF,(\widehat PP-P)A_TG\rangle .               \tag{2.1}
\]

At finite regularization its nuclear trace stabilizes, with all local
places included, to \(B_{\mathrm{nuc}}\).  Since

\[
 \widehat PP-P=(P\widehat PP-P)+Q\widehat PP              \tag{2.2}
\]

and \(P\widehat PP-P=-PU^*QUP\), equations (1.2)--(2.2)
give

\[
 \mathcal C_T=-\mathcal L_T+\mathcal E_T,                 \tag{2.3}
\]

where the Hermitian quadratic defect is

\[
 \mathcal E_T(F,F)
 =\operatorname {Re}\langle A_TF,Q\widehat PPA_TF\rangle. \tag{2.4}
\]

Taking the established semilocal limit proves (0.2).  It is the full
corner, not either summand separately, whose trace decomposes locally into
every prime power and the Gamma term.

The sign of (2.4) is not fixed.  On a generic two-projection angle fiber,

\[
 P=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
 \widehat P=\begin{pmatrix}c^2&cs\\cs&s^2\end{pmatrix},
 \qquad c^2+s^2=1,\quad cs\neq0,                           \tag{2.5}
\]

and for \(v=(x,y)\),

\[
 \mathcal E(v,v)=cs\operatorname {Re}(\overline yx).       \tag{2.6}
\]

This changes sign between \(y=x\) and \(y=-x\), so it cannot be the square
norm of a Jordan covariance.  The primitive approximate identity from D.75
shows that two moment equations do not impose an ambient triangularity
condition deleting these generic angle fibers.

If \(A_T\) were replaced by an already supported map, then
\(y=QA_TF=0\) and the anomaly would vanish.  But the corner would cease to
be the semilocal trace-exact realization.  This is precisely the
support-versus-trace distinction.

## 3. Completion of the cross block

Relative to \(PH\oplus QH\), write

\[
 \widehat P=\begin{pmatrix}\alpha&\beta\\\beta^*&\delta\end{pmatrix},
 \qquad K=I-\alpha\geq0.                                  \tag{3.1}
\]

The Hermitian corner is

\[
 H_{\mathrm{cor}}
 =\begin{pmatrix}-K&\beta/2\\\beta^*/2&0\end{pmatrix}.     \tag{3.2}
\]

On the generic range put

\[
 X_0=-{1\over2}K^\dagger\beta,\qquad
 S_P={1\over4}\beta^*K^\dagger\beta\geq0.                 \tag{3.3}
\]

For \(x\in PH\), \(y\in QH\), completion of the square gives

\[
 \langle(x,y),H_{\mathrm{cor}}(x,y)\rangle
 =-\|K^{1/2}(x+X_0y)\|^2+\|S_P^{1/2}y\|^2.              \tag{3.4}
\]

Thus, after pullback,

\[
 -B_{\mathrm{nuc}}
 =\underbrace{\|K^{1/2}(x+X_0y)\|^2}_{\mathcal L_{\mathrm{fold}}}
 -\underbrace{\|S_P^{1/2}y\|^2}_{\mathcal J_P^*\mathcal J_P}.
                                                                    \tag{3.5}
\]

The positive channel \(S_P\) is the conserved Schur mass of D.78--D.80.
It is not an omitted terminal remainder.  Proving

\[
 \|S_P^{1/2}y\|\leq\|K^{1/2}(x+X_0y)\|                    \tag{3.6}
\]

on the primitive A--B--C range is exactly the missing inequality.

## 4. Exact Jordan--Green--Gamma first chaos

For a prime \(p\), put

\[
 \rho_p=p^{-1/2},\qquad U_p=S_{\log p},\qquad
 A_p=\sqrt{1-\rho_p^2}(I-\rho_pU_p)^{-1}.                \tag{4.1}
\]

Then

\[
 A_p^*A_p
 =I+\sum_{k\neq0}p^{-|k|/2}S_{k\log p}.                  \tag{4.2}
\]

At a finite support cutoff define

\[
 \begin{aligned}
 \mathbf S F&=\bigl((\sqrt{\log p}\,A_pF)_p,\sqrt{m_0}F\bigr),\\
 \mathbf B F&=\bigl((\sqrt{\log p}\,F)_p,\partial_\infty F\bigr),
                                                                  \tag{4.3}
 \end{aligned}
\]

where

\[
 m_0=\log\pi-\psi(1/4)
\]

and

\[
 \|\partial_\infty F\|^2
 ={1\over2\pi}\int_{\mathbb R}
 \left(\operatorname {Re}\psi(1/4+i\tau/2)-\psi(1/4)\right)
 |\widehat F(\tau)|^2\,d\tau.                            \tag{4.4}
\]

Equations (4.2)--(4.4) yield exactly

\[
 \begin{aligned}
 \mathbf S^*\mathbf S-\mathbf B^*\mathbf B
 ={}&2\sum_{p,k\geq1}{\log p\over p^{k/2}}
       \operatorname {Re}S_{k\log p}\\
 &+m_0I-\partial_\infty^*\partial_\infty
 =B_{\mathrm{nuc}}.                                      \tag{4.5}
 \end{aligned}
\]

This includes every \(p^k\), since \(\Lambda(p^k)=\log p\), and the
complete Gamma multiplier.  In particular \(\mathbf S\) occurs with a
minus sign in \(-B_{\mathrm{nuc}}\).

The two Tate jets are unchanged:

\[
 M_+(F)=\widehat F_{\mathrm{PW}}(i/2),\qquad
 M_-(F)=\widehat F_{\mathrm{PW}}(-i/2).                  \tag{4.6}
\]

Restricting to their common kernel deletes only the polar plane; it neither
changes the signs in (4.5) nor annihilates (2.4).

## 5. The proposed second square has the wrong sign

Suppose, optimistically, that a source-defined isometry identified the
Poisson Schur channel in (3.5) with the Jordan first chaos.  Then

\[
 -B_{\mathrm{nuc}}
 =\mathcal L_{\mathrm{fold}}-\mathbf S^*\mathbf S.        \tag{5.1}
\]

Adding the positive first-chaos square gives instead

\[
 \mathcal L_{\mathrm{fold}}+\mathbf S^*\mathbf S
 =-B_{\mathrm{nuc}}+2\mathbf S^*\mathbf S.               \tag{5.2}
\]

Thus even the strongest possible identification overshoots the target by
the explicit positive defect \(2\mathbf S^*\mathbf S\).

Without that unproved identification, augmenting the raw leakage gives the
exact discrepancy

\[
 \boxed{
 (\mathcal L_T+\mathbf S^*\mathbf S)-(-B_{\mathrm{nuc}})
 =\mathcal E_T+\mathbf S^*\mathbf S.}                    \tag{5.3}
\]

Because \(\mathcal E_T\) is indefinite, (5.3) has no formal sign.  The
Jordan summand cannot be declared equal to \(-\mathcal E_T\): the former is
positive, while (2.6) proves that the latter is indefinite.

## 6. Rational-multiplier mismatch

There are two ways to place the first chaos on the D.75 potential, and
neither identifies it with the rational leakage.

If the Jordan preparation acts directly on \(u=\mathcal WF\), its pullback
has multiplier

\[
 {m_0+\sum_p\log p\,
    P_{p^{-1/2}}(e^{i\tau\log p})
  \over(\tau^2+1/4)^2},                                  \tag{6.1}
\]

where

\[
 P_\rho(e^{i\theta})
 =1+2\sum_{k\geq1}\rho^k\cos(k\theta).                  \tag{6.2}
\]

This is not the sharp rational tail
\(\mathbf1_{\Omega_T^c}(\tau)/(\tau^2+1/4)^2\) in (1.3):
(6.1) has all prime-power harmonics and no sharp spectral cutoff.

If instead one uses the graph-correct feature of D.76,
\(\mathbf S(Lu)\), then \(L\mathcal WF=F\) cancels the rational denominator
and recovers (4.5).  It is again not (1.3).

At infinity the mismatch is rigid: (1.3) decays as \(|\tau|^{-4}\), whereas
the completed Gamma boundary in \(-B_{\mathrm{nuc}}\) has multiplier

\[
 \operatorname {Re}\psi(1/4+i\tau/2)-\log\pi
 =\log|\tau|+O(1).                                      \tag{6.3}
\]

No finite combination of the rational leakage and the constant first-chaos
Gamma preparation can create (6.3); the oscillator boundary in
\(\mathbf B\) is essential and has the relative sign in (0.4).

## 7. Conclusion

The requested automatic contraction exists and its pullback is exact:

\[
 \mathcal L_T=A_T^*PU^*(1-P)UPA_T\geq0.
\]

The exact comparison is not a sum of two positive squares.  It is either

\[
 -B_{\mathrm{nuc}}=\mathcal L_T-\mathcal E_T
\]

with an indefinite cross anomaly, or, after the canonical Schur fold,

\[
 -B_{\mathrm{nuc}}
 =\mathcal L_{\mathrm{fold}}-\mathcal J_P^*\mathcal J_P.
\]

Jordan--Green--beta identifies the arithmetic content of the positive
Schur channel but confirms its negative sign in the row-D form.  The
remaining theorem is domination of that channel by the leakage, not its
addition.  This is the global contraction already isolated in D.127, now
derived from the Poisson leakage square without losing any prime power,
Gamma term, or Tate jet.
