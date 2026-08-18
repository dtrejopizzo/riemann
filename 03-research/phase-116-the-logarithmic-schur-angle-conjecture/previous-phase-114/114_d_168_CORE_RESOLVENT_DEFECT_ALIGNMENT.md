# D.168 — Core-resolvent defect alignment

## Verdict

The integer-cell Gram, the pure-Gamma Dirichlet-to-Neumann capacity, and
the Tate-cancelled coefficient (1/2) do **not**, by themselves, propagate
positivity from one cell to the next.  There is an independent alignment
datum with the almost-isometric defect modes of the old core.

Write the old primitive core in Gamma coordinates as

\[
 A_N^{\rm core}=\Gamma_N^{1/2}(I-K_N)\Gamma_N^{1/2},
 \qquad0\le K_N\le I,                                \tag{0.1}
\]

where (K_Nle I) is exactly the induction hypothesis.  For a boundary
vector (e), put

\[
 z_N(e)=\Gamma_N^{-1/2}\mathcal B_Ne.                \tag{0.2}
\]

Then the exact core shorting is

\[
 \boxed{
 \langle\mathcal B_Ne,(A_N^{\rm core})^\dagger
                 \mathcal B_Ne\rangle
 =\langle z_N(e),(I-K_N)^\dagger z_N(e)\rangle.}      \tag{0.3}
\]

D.167 controls (|z_N(e)|^2) with leading coefficient (1/2), but
that does not control (0.3).  If (K_N) has an eigenvalue (1-epsilon),
a fixed component of (z_N(e)) in the corresponding direction is
amplified by (epsilon^{-1}).

The exact noncircular induction invariant is therefore the defect-Carleson
estimate

\[
 \boxed{
 \sup_{e\ne0}
 {\|(I-K_N)^{\dagger/2}z_N(e)\|^2\over\|e\|^2}
 \le\left({1\over2}+o(1)\right)\log N.}              \tag{0.4}
\]

Equivalently, for every spectral projection
(E_N([1-\epsilon,1])), one needs the scale-sensitive alignment

\[
 \|E_N([1-\epsilon,1])z_N\|^2
 \lesssim\epsilon\log N                              \tag{0.5}
\]

uniformly down to the smallest positive defect.  Equation (0.5) is the
precise endpoint-flat/jets theorem now being targeted.  It is stronger
than unweighted integer-cell orthogonality and weaker than a global lower
bound for (A_N^{\rm core}).

## 1. Exact resolvent reduction

On the closure of the Gamma form range, (0.1) gives

\[
 (A_N^{\rm core})^\dagger
 =\Gamma_N^{-1/2}(I-K_N)^\dagger\Gamma_N^{-1/2}.      \tag{1.1}
\]

Substitution of (0.2) proves (0.3).  The difference from pure-Gamma
shorting is

\[
\begin{aligned}
 &\langle z_N,[(I-K_N)^\dagger-I]z_N\rangle\\
 &\qquad=\int_{[0,1)}{\lambda\over1-\lambda}
             \,d\langle E_N(\lambda)z_N,z_N\rangle, \tag{1.2}
\end{aligned}
\]

with a separate range condition at (lambda=1).  Thus only the spectral
mass of (z_N) near one matters; no estimate on the rest of the old core
is needed.

Dyadically decomposing (1-lambda) in (1.2) shows that (0.5), with a
summable improvement across dyadic shells, implies (0.4).  Conversely,
(0.4) implies

\[
 \|E_N([1-\epsilon,1])z_Ne\|^2
 \le\epsilon\left({1\over2}+o(1)\right)
                \log N\,\|e\|^2,                    \tag{1.3}
\]

so the alignment condition is not an artefact of the proof.

## 2. Why the existing data do not imply alignment

The D.164 Gram determines

\[
 z_N^*\Gamma_N z_N
 \quad\hbox{or, after D.167,}\quad z_N^*z_N,          \tag{2.1}
\]

but it contains no spectral information about the relative position of
(operatorname {Ran}z_N) and the defect eigenspaces of (K_N).
The following two-dimensional model has every property used by a naive
induction:

\[
 \Gamma=I,qquad
 K_\epsilon=\begin{pmatrix}1-\epsilon&0\\0&0\end{pmatrix},qquad
 z=\begin{pmatrix}1\\0\end{pmatrix}.                \tag{2.2}
\]

It satisfies (0\le K_\epsilon\le I) and (|z|=1), independently of
(epsilon), while

\[
 z^*(I-K_\epsilon)^{-1}z=\epsilon^{-1}.              \tag{2.3}
\]

Hence no function of (V_N,H_N), the Gamma boundary capacity and the
inequality (K_N\le I) can bound the full core inverse.  An induction
which inserts the pure-Gamma inverse in place of the core inverse is
circular.

## 3. The jets formulation of the missing estimate

Let (v) be a normalized eigenvector of (K_N) with eigenvalue
(1-epsilon), and let

\[
 F_v=\Gamma_N^{-1/2}v.                                \tag{3.1}
\]

By construction (F_v) satisfies both Tate moments.  The coefficient of
(z_N(e)) along (v) is

\[
 \langle v,z_N(e)\rangle
 =\langle F_v,\mathcal B_Ne\rangle.                  \tag{3.2}
\]

Section 2 of D.167 removes the continuous part of (3.2) exactly by
(M_\pm(F_v)=0).  Thus (0.5) reduces to a bound for the prime-discrepancy
sampling of an almost-null primitive vector.  In spatial terms it is an
endpoint trace estimate; in Fourier terms it is a Carleson embedding for
the centered Dirichlet polynomial (E_N=W_N-M_N).

The desired sharp statement is

\[
 \boxed{
 \int_{[1-\epsilon,1]}
 |\langle F_\lambda,\mathcal B_Ne\rangle|^2d\mu_N(\lambda)
 \le C\epsilon\,\mathfrak c_N\|e\|^2,}              \tag{3.3}
\]

where (mathfrak c_N<(1-o(1))\log N) leaves the D.166 boundary
capacity.  It uses exactly the two primitive moments and no global gap.

## 4. Viable next routes

There are two correctly typed ways to prove (3.3).

1. **Endpoint-flat resolvent.**  Prove that the spectral subspace
   (E_N([1-epsilon,1])) has an endpoint-flat frame whose order grows
   faster than the logarithmic effective dimension.  The coupling in
   (3.2) then acquires a power of the cell width, while its change of frame
   is controlled by the defect (epsilon).

2. **Centered Dirichlet Carleson embedding.**  Regard (E_N(\tau)) as a
   multiplier from the de Branges/Paley--Wiener defect space of (K_N).
   Establish (3.3) directly as a Carleson measure estimate.  This avoids
   a global lower spectral gap and is invariant under the A--B--C
   realization.

The first route is finite and compatible with D.159--D.160; the second is
the natural global theorem.  Neither follows from D.164 alone.

The ancillary `114_d_168_defect_alignment_verify.py` checks (0.3), (1.2),
the counter-scaling (2.3), and the necessity estimate (1.3) in finite
dimension.
