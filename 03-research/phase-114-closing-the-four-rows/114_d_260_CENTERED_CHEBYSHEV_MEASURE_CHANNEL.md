# D.260 — The unpaid coherent port is the Mellin transform of one centered measure

## Verdict

After the two Tate channels remove the continuous synthesis, the entire
finite arithmetic part of the remaining coherent cross is the Mellin--
Stieltjes transform of the centered Chebyshev measure

\[
 d\Psi(x)-dx.
\]

Thus the infinitely many prime powers in the D.175 column \(q_N\) are not
independent after centering: they form one source-defined signed measure
channel.  Its exact distribution function is

\[
 A(x)=\Psi(x)-x+1.
\]

The sharp row-D theorem is a Green/old-defect energy inequality for this
channel with the Gamma endpoint terms adjoined.  PNT controls
\(A(x)=o(x)\) but does not provide the required sharp energy.

## 1. Exact Stieltjes representation

Let

\[
 \Psi(x)=\sum_{n\le x}\Lambda(n),
 \qquad s={1\over2}+i\tau.
\]

For \(N\ge2\), the D.175 arithmetic word and continuous synthesis are

\[
 W_N(\tau)=\sum_{n\le N}\Lambda(n)n^{-s},
 \qquad
 M_N(\tau)=\int_1^N x^{-s}\,dx
 ={N^{1-s}-1\over1-s}.                              \tag{1.1}
\]

Define the right-continuous function

\[
 A(x)=\Psi(x)-x+1,
 \qquad A(1^-)=0.                                   \tag{1.2}
\]

Then \(dA=d\Psi-dx\) on \([1,N]\), and therefore

\[
 \boxed{
 E_N(\tau):=W_N(\tau)-M_N(\tau)
 =\int_{[1,N]}x^{-s}\,dA(x).
 }                                                   \tag{1.3}
\]

This includes every prime power because the atoms of \(d\Psi\) are
exactly \(\Lambda(p^k)\delta_{p^k}\).

## 2. Integration-by-parts form

Stieltjes integration by parts, with \(A(1^-)=0\), gives

\[
 \boxed{
 E_N(\tau)
 =N^{-s}A(N)
 +s\int_1^N A(x)x^{-s-1}\,dx.
 }                                                   \tag{2.1}
\]

Formula (2.1) separates the endpoint Volterra term from the interior
centered measure.  Both terms are already present in D.175; no endpoint is
discarded.

In logarithmic coordinates \(x=e^u\),

\[
 E_N(\tau)
 =N^{-s}A(N)
 +s\int_0^{\log N}A(e^u)e^{-su}\,du.               \tag{2.2}
\]

Hence the coherent port is a truncated Fourier--Laplace transform of the
single function \(e^{-u/2}A(e^u)\), plus its exact endpoint value.

## 3. Relation to the D.175 cross

D.175 proves

\[
 q_N=R_0^{\dagger/2}(X_0^*X_E-Y_0^*Y_E)S_E^{\dagger/2},
\]

and identifies its arithmetic multiplier with \(E_N\), with the complete
Gamma and endpoint Volterra contributions retained.  Equations (1.3)--
(2.2) therefore give a source measure for the coherent part of \(q_N\).

The remaining sharp capacity is

\[
 \boxed{
 q_N^*D_N^\dagger q_N\le\mathcal M_N,
 }                                                   \tag{3.1}
\]

where \(D_N\) and \(\mathcal M_N\) are the old defect and remaining born
budget of D.214.  The positive primitive-contact defect from D.244--D.247
must be retained inside \(\mathcal M_N\); the coherent measure channel is
the nonlocal term to be transported.

## 4. Why PNT-strength bounds cannot close (3.1)

The prime number theorem gives \(A(x)=o(x)\).  Substitution in (2.1)
controls pointwise or averaged sizes of \(E_N\) only after losing the
oscillatory phase.  The capacity (3.1) instead weights \(q_N\) by the
small-defect inverse \(D_N^\dagger\) and includes its cross with the
harmonic lift.  No bound on \(\sup_{x\le N}|A(x)|\), or on an unweighted
\(L^2\)-norm of (2.2), implies (3.1) with constant one.

This also locates the Beurling falsifier: systems may share
PNT-strength estimates for their centered counting function while having
different small-defect spectral placement.  A carrying lemma must use the
adelic Fourier/Gamma transport of the measure, not only its magnitude.

## 5. The next precise theorem

Construct directly from \(dA\), the paired Gamma measure and support
geometry a map

\[
 \mathfrak V_N:\mathcal E_N
 \longrightarrow\overline{\mathrm{Ran}\,D_N}
\]

such that

\[
 q_N=D_N^{1/2}\mathfrak V_N,
 \qquad
 \mathfrak V_N^*\mathfrak V_N\le\mathcal M_N.      \tag{5.1}
\]

The map may not be defined as \(D_N^{\dagger/2}q_N\).  Formula (1.3) is
the permitted source definition; (5.1) must follow from an independent
Fourier/Poisson conservation identity.

## 6. Classification

* Stieltjes identity (1.3): **PROVED**.
* Endpoint/interior decomposition (2.1)--(2.2): **PROVED**.
* Identification of the arithmetic coherent channel in \(q_N\):
  **PROVED USING D.175**.
* PNT or unweighted norm control as a proof of sharp capacity:
  **INSUFFICIENT**.
* Source-defined Green transport (5.1): **OPEN**.
* Row D: **OPEN**.
