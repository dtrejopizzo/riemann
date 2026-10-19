# Phase 104 — Closure document

## Verdict

Phase 104 is closed without a proof of A1 and without a proof
of the Riemann Hypothesis. Its permanent result is an adversarial
delimitation of the problem: it identifies several exactly
equivalent formulations, proves numerous stop-gates with witnesses, and
withdraws all claims that confused an equivalence with a new bound.

The literal front remains

\[
 \boxed{
 \int_{\log2}^{T_n}
   (\psi(e^u)-e^u)e^{-u}L_{n-1}^{(2)}(u)\,du
 \le {3\over4}A_n+1-L_n^{(1)}(\log2),\qquad n\ge150.}
                                                               \tag{A1}
\]

With A0 and the finite certificates, A1 implies
(\lambda_n\ge0) for all (n), and by Li's criterion implies RH.
There is no unconditional argument in this phase that proves (A1).

## 1. Preserved exact chain

Define

\[
 E(u)=\psi(e^u)-e^u,\qquad
 K_n(u)=e^{-u}L_{n-1}^{(2)}(u),
\]

\[
 R_n(T)=-\int_T^\infty E(u)K_n(u)\,du,
 \qquad A_n=\lambda_n^{\rm arch}.
\]

The compact--tail identity is

\[
 C_n^{1/4}(T)
 ={3\over4}A_n-n-\int_0^T E(u)K_n(u)\,du
 =\lambda_n-{1\over4}A_n-R_n(T).                         \tag{1}
\]

Since (E(u)=-e^u) on (0<u<\log2), the term (-n) cancels
exactly with the prime-free boundary. Thus (1) gives

\[
 C_n^{1/4}(T)
 ={3\over4}A_n+1-L_n^{(1)}(\log2)
 -\int_{\log2}^T E(u)K_n(u)\,du.                         \tag{2}
\]

The bound A0 controls the tail. Hence (C_n^{1/4}(T_n)\ge0), i.e.
A1, delivers (\lambda_n\ge0). This chain is proved; the sign of the
compact integral is not.

## 2. Permanent gains

1. **Exact normalization.** All boundaries, signs, and
   prime--pole regularizations were fixed. The erratum for the term (-n) is
   binding.
2. **Cofinal cutoff.** As the cutoff is widened, the sufficient condition
   approaches (4\lambda_n>A_n); the constants (2002/501) are not an
   intrinsic coercivity.
3. **Weakened quantifier.** If RH is false, Li's coefficients have
   exponential excursions of both signs on syndetic sets.
   Subexponential barriers on blocks of unbounded length suffice.
4. **Height localization.** For the deep threshold (e^{\sqrt X}),
   the high tail is controlled and any possible failure is concentrated in
   zeros of height (O(X^{1/4})).
5. **Isolated interior factor.** The Deep limit satisfies

   \[
    \Omega_X\to0
    \iff B_{\rm Blaschke}\equiv1
    \iff \mathrm{RH}.                                    \tag{3}
   \]
6. **Local detector.** The Poisson--Jensen defect is exactly the
   Green potential of the interior factor; it detects any zero on the right
   without loss.
7. **Final resolvent gate.** The global generator of tower
   exchanges does not exist in the Abel regime, and the scalar crossed term is zero.
   The triangular Mecke identity was indeed proved, but it is a bilinear
   circulation and not the linear prime--pole source (B_{n,s}).

## 3. Families closed as autonomous mechanisms

Ruled out, always with an explicit identity or witness, were
routes based solely on:

* pointwise PNT/Vinogradov--Korobov bounds and absolute values;
* local positivity, PSD, PF2/TP2, SOS or completely monotone measures;
* Selberg--Riccati without a new signed input;
* first- or second-order Markov/Stein/Palm;
* linear filters, Fejér and block averages;
* translation-invariant resolvents and the scalar tower resolvent;
* local Euler factorizations, Möbius or positive Landau;
* Jensen, Cartan, Turán or Blaschke used only as detectors;
* continuous PNT, known zero-free regions, zero density or
  verification up to finite height.

These gates do not prove A1 to be false. They prove that these sources of
information do not supply the missing sign.

## 4. Two targets that must not be confused

### A1

A1 is a sequence of inequalities, one for each (n\ge150). If

\[
 J_n(U)=\int_{\log2}^{U}E(u)K_n(u)\,du,\qquad
 q_n={3\over4}A_n+1-L_n^{(1)}(\log2),                    \tag{4}
\]

one must prove

\[
 J_n(T_n)\le q_n\quad\hbox{for all }n\ge150.           \tag{5}
\]

It is not, by itself, a statement of convergence in (n).

### Deep limit

For (S_X=e^{\sqrt X}),

\[
 \Omega_X={1\over H_X}\sum_{n\le X}{1\over n}
 \mathbf1_{\{\lambda_n+\log(n+1)\le-S_X\}}.             \tag{6}
\]

Here there is indeed a literal limit:

\[
 \boxed{\Omega_X\longrightarrow0.}                      \tag{7}
\]

Under RH the observable ends up being exactly zero. If there is a zero
off the line, its liminf is positive. Proving (7) for the ordinary primes
would also prove RH, but Phase 104 did not obtain that limit.

## 5. Handoff to Phase 105

Phase 105 begins with a reproducible graphical representation of (4)--(7):

* the cumulative curve (J_n(U)), its barrier (q_n) and the forbidden region;
* the difference between the arithmetically computable segment and the
  complete effective cutoff;
* the behavior of (\Omega_X) in the on-line case and in an off-line
  control quartet.

The new phase inherits no positivity assumption nor any
resolvent certificate from Phase 104.

## Final status

* **Proved:** identities, equivalences, cutoffs, localizations,
  detectors and stop-gates recorded in the phase README.
* **Not proved:** A1 for all (n\ge150), (\Omega_X\to0) for the
  ordinary primes, the absence of the interior Blaschke factor, and RH.
* **Forbidden to cite:** Phase 104 as a proof of RH.
