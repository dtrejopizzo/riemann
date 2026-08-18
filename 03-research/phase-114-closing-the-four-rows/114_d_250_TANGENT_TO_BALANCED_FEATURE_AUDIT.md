# D.250 — Audit of the tangent-to-balanced-feature transport

## Verdict

The conservative tangent colligation D.247 does not act directly on the
balanced Hilbert features \(W_{p,\pm}\) of D.237.  The exact intertwining
filters can be computed, and the odd one has a boundary zero at
\(U_p=-1\), where the balanced reference feature is nonzero.  Hence there
is no bounded inverse transporting the D.247 contraction to the D.137
feature inequality.

This prevents a false closure of row D.  It also identifies the missing
channel exactly: the central/free-delay and contact ports of the full
colligation must be retained in the transfer comparison.  The tangent
block alone loses a genuine boundary mode.

## 1. Odd-channel intertwiner

Use

\[
 h=I-rU,\qquad
 W_- =c_-h^{-1}(I-U),\qquad
 c_-^2={Lr(1+r)\over2(1-r)}
\]

from D.237, and

\[
 d_-={Lr\over2}h^{-1}(U^*-U)
\]

from D.245.  Since

\[
 U^*-U=(I-U)(I+U^*),
\]

one has

\[
 \boxed{
 d_-=W_-T_-,
 \qquad
 T_-={Lr\over2c_-}(I+U^*).
 }                                                   \tag{1.1}
\]

At \(U=-1\),

\[
 T_-(-1)=0,\qquad W_-(-1)={2c_-\over1+r}\ne0.       \tag{1.2}
\]

Therefore \(T_-\) is not bounded below on the unitary spectrum and has no
bounded inverse on the balanced reference feature range.

## 2. Even-channel intertwiner

D.237 gives

\[
 W_+=c_+h^{-1}(I-sU),
\]

where \(s=s_p\in[-1,1]\), while D.245 gives

\[
 d_+={Lr\over2}h^{-1}(U+U^*-2r).
\]

Thus

\[
 \boxed{
 d_+=W_+T_+,\qquad
 T_+={Lr\over2c_+}
 {U+U^*-2r\over I-sU}.
 }                                                   \tag{2.1}
\]

The numerator vanishes at the two unit-circle points satisfying
\(\operatorname{Re}U=r\).  The balanced symmetric feature is strictly
positive there.  Hence this channel also loses modes and cannot be inverted
uniformly.

## 3. Exact Gram comparison

For every source vector \(F\),

\[
 \begin{aligned}
 \|d_-F\|^2&=\langle F,T_-^*R_-T_-F\rangle,\\
 \|d_+F\|^2&=\langle F,T_+^*R_+T_+F\rangle,
 \end{aligned}                                      \tag{3.1}
\]

where \(R_\pm=W_\pm^*W_\pm\).  The balanced prime score is instead

\[
 R_+-R_-=L(P_r-I).                                  \tag{3.2}
\]

Consequently the D.247 signed tangent Gram is not (3.2), nor a common
congruence of (3.2):

\[
 T_+^*R_+T_+-T_-^*R_-T_-
 \ne C^*(R_+-R_-)C                                 \tag{3.3}
\]

for a boundedly invertible common \(C\).  The zeros in (1.2) and (2.1)
prove the obstruction.

The first-order identity D.245 remains exact because it pairs \(d_+\) with
the dual central state rather than squaring \(d_+\).  What fails is the
attempt to transfer the **norm contraction** by inverting the tangent
filters.

## 4. Correct enlarged transfer target

The conservative identity D.247 contains four types of ports:

\[
 (\text{odd tangent},\text{degree})
 \longrightarrow
 (\text{even tangent},\text{contact}).
\]

At the blind modes of \(T_\pm\), the degree/contact ports are nonzero.
Therefore the correctly typed transfer comparison must keep the full
colligation and prove that, after the local Euler/Blaschke realization,

\[
 \begin{aligned}
 \text{balanced reference }X_T
 &\simeq
 \text{odd tangent}\oplus\text{degree state},\\
 \text{balanced load }Y_T
 &\simeq
 \text{even tangent}\oplus\text{contact state},
 \end{aligned}                                      \tag{4.1}
\]

with the Gamma ports of D.249 included and with equality of Grams after
the source-defined state-space elimination.

Equation (4.1), not an inverse of \(T_\pm\), is the next algebraic target.
If a residual remains after eliminating the central ports, it is the exact
local obstruction to the global D.190 transfer theorem.

## 5. Classification

* Intertwining filters (1.1) and (2.1): **PROVED IDENTITIES**.
* Loss of the \(U=-1\) odd mode and the
  \(\operatorname{Re}U=r\) even modes: **PROVED**.
* Bounded invertible transport of the tangent contraction to
  \(W_{p,\pm}\): **IMPOSSIBLE**.
* First-order tangent--dual score identity: **UNAFFECTED AND PROVED**.
* Full four-port state-space comparison (4.1): **OPEN**.
* Row D: **OPEN**.
