# R170_824 — Audit of the multiscale piece

R170_823 was built on a first attempt and
corrected after this audit. No sign law is obtained.

## Verdict

The following analytic fact is accepted as a new piece: for \(a\ne0\),
the scale average

\[
 T_{a,w}=\int w(\rho)\tau_{a/\rho}\,d\rho
\]

gains as many derivatives as the smooth weight \(w\) allows. Its
compression to a finite window is Hilbert--Schmidt. When applied term by
term to the tail \(H_{M,N}^{(\rho)}\), the incidence coefficients
\(h_{M,N}(k)\) produced by \(\Lambda*1=\log\) are preserved exactly.

It is not accepted that this result proves compactness or a sign for the
real averaged collar \(\int w(\rho)H_\rho U_\rho d\rho\). In that product
both factors depend on \(\rho\), and the average does not factor. That
joint-phase analysis is left as the neighboring piece R170_825.

## Corrections made

The first version of R170_823 contained three substantial problems:

1. PC controls \(S_\rho A_\rho U_\rho\), while the flux functional
   contained \(A_\rho S_\rho U_\rho\). Since \(A_\rho\) and \(S_\rho\) do
   not commute, the term
   \(\langle v,[A_\rho,S_\rho]U_\rho g\rangle\) was added explicitly.
2. With the convention \(\tau_bf(t)=f(t+b)\), the convolution kernel is
   supported at \(u=-a/\rho\), not at \(u=a/\rho\). This was corrected to

   \[
   \kappa_{a,w}(u)=\frac{|a|}{u^2}w(-a/u)
      \mathbf1_{\{-a/u\in[\rho_0,1]\}}.
   \]

   The norm \(\|\kappa\|_2^2=|a|^{-1}\int\rho^2|w(\rho)|^2d\rho\)
   remains the same.
3. The claim that each \(P_TH_\rho U_\rho P_T\) has a bounded kernel was
   withdrawn. \(U_\rho\) is a nonlocal unitary operator; that conclusion
   does not follow from the compactness of the decoupled average.

## Verification of the admitted gain

With \(s=1/\rho\), the multiplier of \(T_{a,w}\) is the Fourier
transform of a smooth, compactly supported function:

\[
 q_{a,w}(\xi)=\int_1^{1/\rho_0}w(1/s)s^{-2}e^{-ia\xi s}ds.
\]

Integrating by parts \(j\) times proves decay \(O(|a\xi|^{-j})\).
This justifies \(L^2\to H^k\), the local \(L^2\) kernel, and the HS bound
of R170_823. It does not require derivatives of the test vector.

Subtracting against the base scale is not small in norm:
\(q_{a,w}(\xi)\to0\) while the multiplier of \(\tau_a\) has modulus one.
Hence

\[
 \|T_{a,w}-\tau_a\|\ge1.
\]

The average serves as a new, smoothed operator; not as a uniform
approximation to the original translation.

## Interface with the interior energy

Identity (24) of R170_823 is accepted after keeping four separate
blocks:

- ordered PC via the functional \(\chi^{(\rho)}\);
- the commutator \([A_\rho,S_\rho]\);
- the difference \(A_1-A_\rho\), including Gamma and primes;
- the alignment error between \(G_\rho F-F\) and the exterior test.

It is an exact interface with the nonnegative averaged interior energy for
weights \(w\ge0\). None of these four blocks yet has the required sign.
The compactness proved refers only to \(\langle H_\rho\rangle_w\), not to
the whole first block.

## Contribution to the puzzle

The piece reduces a concrete topological obstruction: pointwise
translations are not norm-continuous, but a coherent average produces
spectral decay without losing the factorization over the integers. It
remains to determine whether that decay survives in the product coupled
with \(U_\rho\), and even if it did survive, turning compactness into a
sign would require another arithmetic input.

The certified interval of Paper 47 is not extended, nor is D proved.
