# D.116 — Bost--Connes KMS contact and the central-temperature obstruction

## Status

The Bost--Connes modular flow has the correct energy generator
\(H\epsilon_n=(\log n)\epsilon_n\).  In the Gibbs range \(\beta>1\), the
mean energy is

\[
 -\partial_\beta\log\zeta(\beta)
 =\sum_{n\geq2}\Lambda(n)n^{-\beta}.
\]

Locally this is the complete prime-power tower, and formally at
\(\beta=1/2\) it has the desired central weights
\(\Lambda(n)/\sqrt n\).  Thus modular thermodynamics explains why a
logarithmic Euler derivative produces von Mangoldt rather than divisor
counts.

It does not provide the row-D positive form.

* The Gibbs state is trace-class only for \(\beta>1\); at \(\beta=1/2\)
  the Bost--Connes KMS state is type III and has infinite total energy.
* Modular variance/Dirichlet energy is positive, but its coefficient is
  \(\Lambda(n)\log n\), not \(\Lambda(n)\).
* Time invariance makes distinct energy eigenoperators orthogonal.  Hence
  the KMS two-point matrix is diagonal in prime-power depth, whereas row D
  needs \(p^{-|r-s|/2}\).
* The finite-prime Bost--Connes flow has neither the Gamma determinant nor
  the Poisson duality exchanging the two Tate jets.

The local KMS factors and the quarter-shift oscillator can be placed in a
common modular standard form, but the required logarithmic contact remains
a renormalized first derivative/supercharacter, not a positive covariance.
Passing to its primitive quotient is again the unitarizability problem of
D.115.

No zeta zero or sign of \(B_{\rm nuc}\) is used.  The paper is not modified.

## 1. Bost--Connes time evolution

In the standard Bost--Connes system let \(\mu_n\) be the isometry associated
to \(n\in\mathbb N^\times\).  The time evolution is

\[
 \sigma_t(\mu_n)=n^{it}\mu_n.                           \tag{1.1}
\]

In the canonical low-temperature representation,

\[
 H\epsilon_n=(\log n)\epsilon_n,qquad e^{itH}\epsilon_n=n^{it}\epsilon_n.
                                                                  \tag{1.2}
\]

For \(\beta>1\), the Gibbs partition function and state are

\[
 Z(\beta)=\mathrm{Tr}(e^{-\beta H})=\zeta(\beta),
 \qquad
 \varphi_\beta(x)={\mathrm{Tr}(e^{-\beta H}x)\over\zeta(\beta)}.
                                                                  \tag{1.3}
\]

For \(0<\beta\leq1\), there is instead a unique high-temperature KMS state
of type III; formula (1.3) is unavailable because \(e^{-\beta H}\) is not
trace class.

## 2. The KMS relation fixes the half-density weights

The KMS identity applied to \(\mu_n,\mu_n^*\) gives, at every temperature
where the state exists,

\[
\begin{aligned}
 \varphi_\beta(\mu_n\mu_n^*)
 &=\varphi_\beta(\mu_n^*\sigma_{i\beta}(\mu_n))\\
 &=n^{-\beta}\varphi_\beta(\mu_n^*\mu_n)
 =n^{-\beta}.                                           \tag{2.1}
\end{aligned}
\]

Thus the central normalization \(n^{-1/2}\) is intrinsic to the KMS state
at \(\beta=1/2\), even though no Gibbs trace exists there.

However, KMS states are invariant under \(\sigma_t\).  Therefore

\[
 \varphi_\beta(\mu_m\mu_n^*)
 =(m/n)^{it}\varphi_\beta(\mu_m\mu_n^*)
\]

for every \(t\), and hence

\[
 \boxed{
 \varphi_\beta(\mu_m\mu_n^*)=0\quad(m\ne n).}          \tag{2.2}
\]

At one prime the KMS depth matrix is diagonal.  It does not equal the
Szegő/OS covariance

\[
 p^{-|r-s|/2},                                          \tag{2.3}
\]

whose off-diagonal entries are essential for all prime-power correlations.
The latter arises from the coherent OS vector and its dilation in D.114,
not from the gauge/time-invariant KMS two-point function.

## 3. Mean energy gives exactly the von Mangoldt tower

In the Gibbs range,

\[
\begin{aligned}
 \varphi_\beta(H)
 &={\sum_{n\geq1}(\log n)n^{-\beta}\over\zeta(\beta)}\\
 &=-{\zeta'(\beta)\over\zeta(\beta)}
 =\sum_{n\geq2}\Lambda(n)n^{-\beta}.                  \tag{3.1}
\end{aligned}
\]

For one prime,

\[
 Z_p(\beta)={1\over1-p^{-\beta}},qquad
 -\partial_\beta\log Z_p(\beta)
 ={(\log p)p^{-\beta}\over1-p^{-\beta}}
 =\sum_{k\geq1}(\log p)p^{-k\beta}.                   \tag{3.2}
\]

At \(\beta=1/2\), every local factor is finite and (3.2) is

\[
 \sum_{k\geq1}{\Lambda(p^k)\over\sqrt{p^k}}.           \tag{3.3}
\]

Thus the modular logarithmic derivative does produce \(\Lambda\), not
\(d(n)\).  Globally, however,

\[
 \sum_n n^{-1/2}=\infty,qquad
 \sum_p{(\log p)p^{-1/2}\over1-p^{-1/2}}=\infty.       \tag{3.4}
\]

There is no normalized Gibbs energy at the central temperature.  The
nuclear test-function pairing of row C can renormalize/smear (3.3), but it
is not a KMS probability expectation.

## 4. Positive variance has the wrong contact degree

Thermodynamic convexity gives

\[
 \mathrm{Var}_\beta(H)
 =\partial_\beta^2\log Z(\beta)
 =\sum_{n\geq2}\Lambda(n)(\log n)n^{-\beta}>0.         \tag{4.1}
\]

Locally,

\[
 \mathrm{Var}_{\beta,p}(H_p)
 ={(\log p)^2p^{-\beta}\over(1-p^{-\beta})^2}
 =\sum_{k\geq1}k(\log p)^2p^{-k\beta}.                 \tag{4.2}
\]

The same occurs for the positive modular Dirichlet form

\[
 \mathcal E_\beta(x)=
 \varphi_\beta(\delta(x)^*\delta(x)),qquad
 \delta(\mu_n)=i(\log n)\mu_n.                         \tag{4.3}
\]

It is positive because it is a square, but it contains \((\log n)^2\).
The desired Lefschetz contact contains one reduced \(\log p\), independent
of the power \(k\).  That reduced degree belongs to the cyclotomic contact
of A--B, not to modular variance.

Hence the two available thermodynamic operations separate:

\[
 \begin{array}{c|c|c}
 &\text{coefficient}&\text{positivity}\\\hline
 -\partial_\beta\log Z&\Lambda(n)n^{-\beta}
   &\text{mean/scalar, not a Gram}\\
 \partial_\beta^2\log Z&\Lambda(n)\log n\,n^{-\beta}
   &\text{positive variance}.
 \end{array}                                             \tag{4.4}
\]

There is no KMS identity turning the first row into the positive quadratic
form required by D while keeping its coefficient.

## 5. Gamma is a determinant, not the BC Gibbs factor

The real contribution used in A--C is governed by

\[
 m_\infty(\tau)=log\pi-operatorname{Re}
 \psi(1/4+i\tau/2).                                    \tag{5.1}
\]

It is the logarithmic derivative of the zeta-regularized determinant of
the quarter-shift oscillator

\[
 A_\infty e_j=(j+1/4)e_j.                              \tag{5.2}
\]

The ordinary thermal partition of this oscillator is

\[
 \mathrm{Tr}(e^{-xA_\infty})
 ={e^{-x/4}\over1-e^{-x}},                             \tag{5.3}
\]

whose normalized mean energy is

\[
 {1\over4}+{1\over e^x-1}.                             \tag{5.4}
\]

Equation (5.4) is not the digamma finite part (5.1).  Recovering (5.1)
requires the heat-kernel integral and determinant renormalization of
D.17/D.94, not merely adjoining a Gibbs oscillator to the finite BC
system.

Thus a modular standard form can contain both local positive systems, but
the exact Gamma normalization remains a renormalized determinant channel.

## 6. The two Tate jets and central duality

The BC time evolution is multiplicative and finite-adelic.  It does not
contain the additive Fourier transform which exchanges

\[
 f(0)\quad\text{and}\quad\widehat f(0),                 \tag{6.1}
\]

nor the Poisson exact sequence producing the two polar characters.
Consequently the primitive conditions must still be imported from the
adelic Poisson core of D.115.

The completed functional equation exchanges \(s\) and \(1-s\), but the
KMS modular conjugation at inverse temperature \(\beta\) implements the
Tomita reflection for the modular group \(\sigma_{\beta t}\); it does not
identify the KMS systems at \(\beta\) and \(1-\beta\).  In particular, the
finite BC partition function has no Gamma factor and no internal
\(\beta\leftrightarrow1-\beta\) symmetry.

At \(\beta=1/2\), the formal duality is fixed but the Gibbs partition
diverges.  Analytic continuation of \(\zeta(1/2)\) cannot be used as a
partition function: a partition function is a positive trace, whereas the
continued value is not the trace of \(e^{-H/2}\).

## 7. Modular standard form does not unitarize the Poisson quotient

Every faithful KMS state has a Hilbert GNS standard form and a self-adjoint
modular Liouvillean.  For the high-temperature BC state this Hilbert space
is positive.  Its spectral differences are generated by
\(\log m-\log n\), and its invariant two-point functions obey (2.2).

The row-C odd object is instead the Poisson cokernel

\[
 \mathcal H_-^0=\mathcal H_-/Z\mathcal H_\cap.          \tag{7.1}
\]

There is no constructed isometric embedding of (7.1) into the BC KMS GNS
space which simultaneously:

1. retains the off-diagonal kernel (2.3);
2. turns the mean contact (3.1) into a quadratic character;
3. includes the Gamma determinant (5.1);
4. kills both Tate jets (6.1).

If such an embedding with the correct supercharacter existed, its
primitive Gram would be \(-B_{\rm nuc}\), and its positivity would close D.
The modular Hilbert space by itself has a different covariance and cannot
serve as that embedding.

## 8. Outcome

The KMS audit gives a precise division of labour:

\[
 \begin{array}{c|c}
 \text{BC modular generator}&\log n\\
 \text{log partition mean}&\Lambda(n)n^{-\beta}\\
 \text{KMS range weight}&n^{-\beta}\\
 \text{positive variance}&\Lambda(n)\log n\,n^{-\beta}\\
 \text{KMS two-point depth kernel}&\text{diagonal}\\
 \text{required depth kernel}&p^{-|r-s|/2}\\
 \text{Gamma/Tate duality}&\text{external Poisson--oscillator data}.
 \end{array}
\]

At \(\beta=1/2\), the first derivative has the right formal coefficients
but is not a finite state expectation; the positive second derivative has
the wrong coefficients.  Therefore a Bost--Connes KMS state does not supply
the adelic Markov conditional expectation missing in D.114--D.115.

A further viable pivot would have to combine the local KMS logarithmic
mean with the OS coherent dilation **before** taking the Poisson cokernel,
and prove that the resulting renormalized modular correspondence is a
completely positive map.  Complete positivity of that renormalized map is
not implied by KMS and is the next exact property to audit.

