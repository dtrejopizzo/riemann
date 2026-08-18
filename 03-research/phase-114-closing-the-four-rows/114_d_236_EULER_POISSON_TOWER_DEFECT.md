# D.236 — Exact Euler--Poisson defect for one prime tower

## Verdict

Every complete prime-power tower in the localized row-D operator admits an
exact source-defined Poisson-resolvent factorization.  If

\[
 U_p=S_{\log p}\quad\hbox{on }L^2(\mathbb R),
 \qquad r_p=p^{-1/2},
\]

then

\[
 V_p=\sqrt{1-r_p^2}\,(I-r_pU_p)^{-1}
\]

is bounded and

\[
 \boxed{
 V_p^*V_p
 =I+\sum_{k\geq1}p^{-k/2}
       (S_{k\log p}+S_{-k\log p}).
 }                                                     \tag{0.1}
\]

Consequently the complete finite-place contribution of the prime (p) is

\[
 \boxed{
 -\sum_{k\geq1}{\log p\over p^{k/2}}
   (S_{k\log p}+S_{-k\log p})
 =\log p\,(I-V_p^*V_p).
 }                                                     \tag{0.2}
\]

After zero-extension compression to (I_T), terms with
(k\log p\geq2T) vanish as quadratic-form cross terms, so (0.2) is
exactly the finite prime-power sum occurring in the localized operator,
with the usual null-set convention at a threshold.

Thus all powers of a fixed prime are not independent boundary channels:
they are the Taylor coefficients of one canonical Euler--Poisson state
operator.  This supplies a new source-level colligation candidate.  It
does **not** by itself prove row D.  The operator (V_p) is generally an
expansion, not a contraction, and summing the two sides of (0.2) over
primes introduces large diagonal terms which cancel only after the full
prime--Gamma assembly.  The missing theorem remains a contractive
factorization of that completed, centered assembly after support shorting.

## 1. Resolvent identity

Let (U) be unitary and (0<r<1).  The norm-convergent Neumann series
gives

\[
 (I-rU)^{-1}=\sum_{j\geq0}r^jU^j,
 \qquad
 (I-rU^*)^{-1}=\sum_{j\geq0}r^jU^{*j}.              \tag{1.1}
\]

The scalar Poisson identity extends by continuous functional calculus:

\[
 \begin{aligned}
 &(I-rU)^{-1}+(I-rU^*)^{-1}-I\\
 &\hspace{12mm}=(1-r^2)(I-rU^*)^{-1}(I-rU)^{-1}.
 \end{aligned}                                      \tag{1.2}
\]

Indeed, multiplying both sides by the commuting factors
((I-rU^*)) and ((I-rU)) reduces both numerators to (1-r^2).
Combining (1.1) and (1.2) yields

\[
 (1-r^2)(I-rU^*)^{-1}(I-rU)^{-1}
 =I+\sum_{k\geq1}r^k(U^k+U^{*k}).                  \tag{1.3}
\]

Taking (U=U_p) and (r=r_p) proves (0.1), and subtracting (0.1)
from the identity proves (0.2).

## 2. Localization and all prime powers

Let (J_T:L^2(I_T)\to L^2(\mathbb R)) be extension by zero.  For
(f,g\in L^2(I_T)),

\[
 \langle J_Tf,U_p^kJ_Tg\rangle=0
 \quad\hbox{if } k\log p\geq2T,                    \tag{2.1}
\]

apart from a null endpoint when equality holds.  Hence compression of
(1.3) gives

\[
 J_T^*V_p^*V_pJ_T
 =I+\sum_{1\leq k<2T/\log p}p^{-k/2}
 J_T^*(S_{k\log p}+S_{-k\log p})J_T.               \tag{2.2}
\]

Multiplication by (log p), followed by summation over
(p<e^{2T}), reproduces every and only (n=p^k<e^{2T}), with coefficient

\[
 (\log p)p^{-k/2}=\Lambda(p^k)/\sqrt{p^k}.          \tag{2.3}
\]

No prime-only truncation and no mixed integer is introduced.

## 3. Why a scalar sign gauge cannot replace the resolvent state

The idempotence of the reduced contact
(Lambda(p^k)=\log p) might suggest assigning the same negative phase to
every power of the monoidal generator.  This is impossible in a unitary
realization.  More precisely, let (U) be unitary and (v\ne0).  There is
no identity

\[
 \langle v,U^kv\rangle=-\|v\|^2
 \qquad(k\geq1).                                    \tag{3.1}
\]

For (k=1), equality in Cauchy--Schwarz forces (Uv=-v); then
(U^2v=v), contradicting (3.1) at (k=2).  Therefore a monoidal
prime action cannot generate the reduced contact through a one-state sign
flip.  The logarithmic Euler resolvent in (0.1), rather than a scalar
gauge, is the correctly typed state realization of the whole tower.

## 4. Local passive realization and its limitation

The Möbius function

\[
 b_r(z)={z-r\over1-rz}                               \tag{4.1}
\]

is a scalar inner function and has the standard unitary one-state
realization.  Its denominator (1-rz) is the same Euler resolvent appearing
in (V_p).  Thus each prime tower separately has a canonical passive
dilation before any zeta zero or spectral sign is mentioned.

However, (0.2) is a **difference** between the identity channel and the
Poisson output energy.  Moreover

\[
 \|V_p\|^2={1+r_p\over1-r_p}>1.                     \tag{4.2}
\]

Thus the direct sum of the local passive systems does not furnish the
sharp D.190 Douglas contraction after localization and old-core shorting.
The completed colligation must also contain:

1. the Gamma/continuous channel;
2. the scalar and resolvent corrections;
3. the two Tate compression terms;
4. the cancellation of the prime-diagonal terms introduced in (0.2);
5. compatibility with old/born support projections.

Assuming that this completed transfer function is inner would be the
causal-scattering circularity identified in D.234.  The admissible next
step is instead to insert (0.1) into the exact D.175 centered column and
determine whether the prime-diagonal terms cancel algebraically against the
Gamma/continuous harmonic lift before the old defect inverse is taken.

## 5. Epistemic classification

* Euler--Poisson identity (0.1)--(0.2): **PROVED OPERATOR IDENTITY**.
* Exact localization and recovery of all (p^k): **PROVED**.
* Impossibility of a one-state constant sign gauge: **PROVED**.
* Passive realization of each local Euler denominator: **PROVED/STANDARD**.
* Contractivity of the completed prime--Gamma colligation: **OPEN**.
* Sharp Douglas inequality, row D and RH consequence: **OPEN**.
