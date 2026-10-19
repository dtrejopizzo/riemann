# R170_830 — Audit of the exterior Gamma--Euler bridge

R170_829 was built on a first attempt and then audited. It does not prove the sign of the bridge.

## Verdict

The interface of R170_829 is correct and contributes a structural
obstruction: the Gamma--Euler reserve cannot be realized by an operator
whose image stays within the window. Every valid lift must cross the
boundary and preserve both its orientations, the Gamma multiplier, and
the Tate port.

The direct subtraction between the flux and the reserve does not count as
progress; it is an identity. The additional content is the lift equation,
the exclusion of all the natural interior candidates, and the explicit
form of an exterior candidate that leaves a concrete Green obligation.

## Verified factors and signs

Over the radical,

\[
 D_\Delta=B+\tfrac12Q^{(1)},
\]

because Paper 47 proves

\[
 2\langle F,\Delta F\rangle
 =2\|R_LF\|^2+Q_{N,L}(F),
 \qquad Q_{N,L}=-2\langle R_LF,D_{N,L}R_LF\rangle.
\]

Hence \(D_\Delta\succ0\) on \(Z\): \(I-D_{N,L}\succ0\) and \(R_L|_Z\)
is injective. It was also verified that

\[
 P-D_\Delta=R_{GE}=Q-E-D_\Delta
              =Q-E-B-\tfrac12Q^{(1)}.
\]

There is no hidden sign in this equality. The sufficient condition
\(R_{GE}\succeq0\) implies the desired lower bound, but it is neither
proved nor necessary when the slack in \(D_\Delta\) compensates a
negative part.

## Verified exterior equation

With

\[
 (\Lambda z)(F)=\langle F,A_1z\rangle-\langle r_F,z\rangle,
\]

a canonical lift should satisfy

\[
 \operatorname{Herm}(\Lambda Y_L)=D_\Delta.
\]

If \(Y_LF\) is supported in \(I_T\), the weak equation gives
\(\Lambda Y_LF=0\). This excludes \(R_L^*CR_L\), \(G_L\), \(JG_LJ\),
\(S_L\), and the interior syntheses coming from the adjoint of the
collar. The contradiction with \(D_\Delta\succ0\) is exact.

The candidate

\[
 (\iota_+c)(t)=\mathbf1_{t>T}\sum_{m\le L}b_mc_me^{-a_mt},
 \qquad Y_+=\iota_+(I-D)R_L,
\]

does cross the boundary and belongs to the logarithmic domain despite the
jump. But the identity \(R_LB_N=D_NR_L-\mathcal E_{N,L}\) does not
compute \(\Lambda\iota_+\): the action of \(m(D)\), the jump
contribution, and Tate are missing. R170_829 neither rules them out nor
assigns them a sign.

## Scope

The piece reduces the following construction to a precise question:
obtain an exterior Green formula for the exponential tails that evaluates
\(\Lambda\iota_+\) and its reflection, and compare it with
\(I-D_{N,L}\). If the formula produces exactly \(D_\Delta\), the bridge is
realized; if it produces a remainder, that remainder must be kept in the
full matrix.

The equivalent inequality

\[
 R_{GE}\succeq-[D_\Delta-(1-q_0)B]
\]

remains exactly the missing bound, not an available estimate. The
certified range is not extended, nor is D proved.
