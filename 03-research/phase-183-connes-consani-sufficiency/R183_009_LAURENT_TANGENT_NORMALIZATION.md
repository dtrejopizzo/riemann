# R183.009 — The finite part is a tangent pairing, not a norm

## 0. Result

The agreement between R183.006 and D.244--D.247 is structural. Adding a prime \(p\) to the semilocal set changes the fiber residue by \(p/(p+1)\); its logarithmic derivative is \(\log p/(p+1)\), exactly the opposite of D.244's coordinate \(x_p\).

However, the Laurent finite part represents the pairing between the Fourier-even tangent and the dual central state, as in D.245. D.247's contraction compares the norms of the Fourier-even and -odd tangents. Going from the first-order pairing to the second-order norm requires the local Fisher operator and, after support compression, its global short. This comparison is exactly the open step; the coefficient agreement does not resolve it.

## 1. Variation of the semilocal residue

Recall

\[
 C_S={1\over\zeta(2)}\prod_{p\in S_f}(1+p^{-1})^{-1}. \tag{1.1}
\]

If \(p\notin S_f\), then

\[
 {C_{S\cup\{p\}}\over C_S}
 =(1+p^{-1})^{-1}={p\over p+1}.                    \tag{1.2}
\]

Introduce a local deformation

\[
 \rho_p(s)=(1+p^{-1-s})^{-1}.                      \tag{1.3}
\]

Then

\[
 \rho_p(0)={p\over p+1},
 \qquad
 {\rho_p'(0)\over\rho_p(0)}={\log p\over p+1}.     \tag{1.4}
\]

D.244 defines

\[
 x_p=-{\log p\over p+1}.                            \tag{1.5}
\]

Hence

\[
 \boxed{-x_p=\left.\partial_s\log\rho_p(s)\right|_{s=0}.} \tag{1.6}
\]

This equality proves that the coligation's degree coordinate is the logarithmic connection of the semilocal residue.

## 2. Normalization of the central states

D.244's local central state has norm

\[
 a_p=1-p^{-2}.                                      \tag{2.1}
\]

The local Laurent residue measure is \(\rho_p(0)=p/(p+1)\). They are related by the positive congruence

\[
 \rho_p(0)=t_p^2a_p,
 \qquad
 t_p^2={p^3\over(p-1)(p+1)^2}.                     \tag{2.2}
\]

For a squarefree set \(J\), set \(t_J=\prod_{p\in J}t_p\). The tensor congruence \(v_J\mapsto t_Jv_J\) transports D.244's central metric to the Laurent residue metric. Since \(t_p\) does not depend on \(s\), the logarithmic connection (1.6) is unchanged by this congruence.

Hence the difference in normalizations is not the obstacle: an explicit diagonal transport exists.

## 3. First order versus second order

D.244 computes, for the local tangent \(d_{p,+}\) and the central state \(\sigma_p\),

\[
 {\langle d_{p,+},\sigma_p\rangle\over\|\sigma_p\|^2}
 =x_p.                                               \tag{3.1}
\]

This is a first-order quantity in \(\log p\). D.245 proves that the full prime score is

\[
 \text{score}_p
 =2\,d_{p,+}(\sigma_p^*)^{-1},                      \tag{3.2}
\]

i.e. a tangent--dual-state pairing. The finite part (1.6) belongs exactly to this level.

By contrast, D.244 obtains

\[
 \|d_{p,+}\|^2=\|d_{p,-}\|^2
 ={(\log p)^2(p-1)\over2p^2},                      \tag{3.3}
\]

and D.247 builds its contraction by comparing sums of those norms. This is a quadratic, second-order datum.

There is no universal constant \(c\) such that pairing (3.1) equals \(c\|d_{p,+}\|^2\) for every \(p\): its ratio is

\[
 {(-x_p)\over\|d_{p,+}\|^2/a_p}
 ={2\over\log p}.                                   \tag{3.4}
\]

The required normalization depends on \(p\). It is precisely the inverse Fisher normalization of D.244(4.7).

## 4. The local Fisher operator

Define on the prime channel

\[
 J_p=\sqrt{2\over\log p}.                           \tag{4.1}
\]

Then (3.4) can be written as an equality of local forms between the score and the normalized tangent. But the global assembly \(J=\bigoplus_pJ_p\) is not innocuous:

1. it is bounded, but \(J_p\to0\), so its inverse is unbounded and
   its Hilbertian range is not closed;
2. it commutes with each prime's orbit, but does not allow uniformly
   recovering the tangent from the score;
3. after support compression, its rank loss produces
   boundary terms;
4. those terms must be combined with Gamma and the two Tate ports.

Applying Cauchy--Schwarz locally to pairing (3.2) would replace the
oriented equality by an estimate and would lose the constant one
required by Theorem M.

## 5. The missing central--tangent column

The correct comparison must simultaneously preserve the central state and its tangent. For a finite set of places, formally define

\[
 \mathbb C_S f=
 \begin{pmatrix}
  \Sigma_S f\\
  (J_pe_{p,-}f)_{p\in S}\\
  d_S(f)
 \end{pmatrix},
 \qquad
 \mathbb T_S f=
 \begin{pmatrix}
  \Sigma_S f\\
  (J_pe_{p,+}f)_{p\in S}\\
  c_S(f)
 \end{pmatrix},                                     \tag{5.1}
\]

where \(d_S\) is D.247's degree port and \(c_S\) its contact port. D.247's conservative identity controls the last two blocks; D.245 identifies the polarization between the first and second with the score.

The required object is a unitary dilation \(\mathbb U_S\) satisfying

\[
                 \mathbb U_S\mathbb C_S=\mathbb T_S \tag{5.2}
\]

including the central--tangent polarizations, not merely the equality of their diagonal Gram matrices. Afterward, D.246's Gaussian state and its tangent must be added.

Equality (5.2) at the finite local level is an extension of D.247's partial isometry. Its existence does not follow from D.247 because the central entries may introduce a transversal defect. That defect must be computed before claiming a unitary extension.

## 6. Logical status

* Semilocal variation (1.2)--(1.6): **PROVED**.
* Congruence of central metrics (2.2): **PROVED**.
* Identification of Laurent with D.245's pairing: **PROVED** at the level of local coefficients.
* Distinction between first/second order and the Fisher factor (3.4): **PROVED**.
* Global transport via \(J\): **PROVED BOUNDED**, but not bounded
  below and with an unbounded inverse.
* Central--tangent extension (5.2): **OPEN**.
* Support/Gamma/Tate comparison: **OPEN**.
* Row D: **OPEN**.
