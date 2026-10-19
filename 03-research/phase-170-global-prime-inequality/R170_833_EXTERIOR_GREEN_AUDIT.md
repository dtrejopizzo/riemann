# R170_833 — Audit of the exterior formula R170_831

Verdict: **valid as a response formula and as a
domain obstruction; not yet a closed Green identity nor a sign law**.

## 1. Checks

For

\[
 z_a^+(s)={\bf1}_{s>T}e^{-as},\qquad a>0,
\]

we have \(\widehat z_a^+(\tau)=O(|\tau|^{-1})\). Since
\(m(\tau)=O(\log(2+|\tau|))\), it follows that
\(m\widehat z_a^+\in L^2\); hence the tail belongs to the domain of
\(m(D)\).

With

\[
 K(u)=2\sum_{j\ge0}e^{-(2j+1/2)u},
\]

the separation of supports eliminates the diagonal terms and leaves

\[
 (m(D)z_a^+)(t)
 =-\frac12\int_{T-t}^{\infty}K(u)e^{-a(t+u)}\,du,
 \qquad |t|<T.
\]

The convention \((\tau_bz)(t)=z(t+b)\) gives exactly the prime orientation
of R170_831; the adjoint does not enter from the right tail. Since
\(K(u)=u^{-1}+O(1)\), the singularity at \(T\) is logarithmic and belongs
to \(L^2(I_T)\). No delta appears. Reflection correctly exchanges
\(L_M\) and \(L_M^*\).

## 2. Non-duplication check

The off-diagonal kernel formula is already in R162_404 §4. The Gamma,
prime, and Tate collars are already resolved in phase 121; the finite
Green complex and the transmission obstruction are in P122_028–029; the
Schur rank condition is in P124_011. R170_831 cites them and only
specializes the kernel to the candidate \(\iota_+\). It must not be
presented as the discovery of a new exterior operator.

The useful additional information is the type check. The radical equation
defines

\[
 r_F\in \operatorname{span}\{e^{-t/2},e^{t/2}\}\subset L^2(I_T),
\]

but does not define its pairing with a tail supported outside
\(I_T\). The zero extension and the extension by the global characters
agree inside the window and give different exterior ports. Hence
\(\langle r_F,z_{\rm ext}\rangle\) cannot be used before an additional
law is specified.

## 3. Logical limit

Introducing \(\Theta_\pm\) parametrizes all choices of the Tate port, but
does not construct the canonical choice. Nor does it prove

\[
 \operatorname{Herm}(\Lambda Y_L)=D_\Delta.
\]

In particular, choosing \(\Theta_\pm=0\) because the supports are
disjoint is a possible convention, not a consequence of the complete
energy. If it were used to close the sign, one would be introducing the
transmission condition that P122_029 identifies as missing.

## 4. Next admissible obligation

The next piece must derive \(\Theta_\pm\) from an identity already
defined in the global space, or reformulate the flux in a boundary
quotient where the dependence on the extension cancels. Afterward it will
be necessary to prove that the resulting boundary term:

1. Hermitizes as \(D_\Delta\) or with a useful sign remainder;
2. uses the minimality of the first contact;
3. uses \(\Lambda*1=\log\) in the line that fixes the sign;
4. does not transport to the corpus's falsifiers.

R170_831 passes the formula and domain check. The state of D does not
change.
