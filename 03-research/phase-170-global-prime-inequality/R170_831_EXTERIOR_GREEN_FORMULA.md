# R170_831 — Exterior Gamma--Euler formula and Tate typing defect

Continuation of R170_829--830. Status: exterior response
formula proved; the lift equation is not closed.

## 0. Result

The action of \(A_1=m(D)-(L_M+L_M^*)\) on a cut exponential tail can be
computed exactly within the window. The jump does not produce a delta: it
produces the well-known logarithmic collar potential, which belongs to
\(L^2(I_T)\). For the right tail only the prime orientation entering from
the right survives; for the reflected tail the opposite orientation
survives.

However, the functional

\[
 (\Lambda z)(F)=\langle F,A_1z\rangle-\langle r_F,z\rangle
\tag{0.1}
\]

of R170_829 is not yet defined for exterior \(z\): the weak equation
defines \(r_F\in\operatorname{span}\{e^{t/2},e^{-t/2}\}\) only on
\(I_T\). The corpus determines its coefficients via collar currents, but
does not define a pairing of that restricted vector with a tail on
\(I_T^c\). This typing defect is the exact obligation preceding

\[
 \operatorname{Herm}(\Lambda Y_+)=D_\Delta.                    \tag{0.2}
\]

## 1. No duplication: corpus inventory

This note does not re-attribute novelty to the following results.

1. Paper 47, §"The archimedean multiplier as a Lévy exponent", proves
   \[
   m(\tau)=C_0+\int_0^\infty(1-\cos \tau u)K(u)\,du,
   \quad K(u)=2\sum_{j\ge0}e^{-(2j+1/2)u},                    \tag{1.1}
   \]
   and Paper 47 §"Compressed collars" / R161_070--071 / R170_702 prove
   \(R_LB_N=D_{N,L}R_L-\mathcal E_{N,L}\) and the exact balance
   \(Q_{N,L}=-2\langle R_LF,D_{N,L}R_LF\rangle\) on the radical.
2. P121_EXACT_TATE_COLLAR_LOCALIZATION and
   P121_RESOLVED_TATE_COLLAR_INTEGRAL already convert Gamma and the two
   prime orientations into scalar currents \(J_\pm(F)\), resolve their
   logarithmic potentials, and determine the coefficients of \(r_F\) by
   an invertible crossed Tate matrix. They do not prove that these
   currents vanish.
3. R161_006 already separates the exterior Poisson port into a
   one-sided discrepancy and a Tate scalar of the opposite tail.
   R161_009 identifies the polar corrections of the Hardy ports with the
   crossed Tate currents. The global vector identity required there
   remains open.
4. R162_404, Theorem 4.1, already computes the off-diagonal Gamma
   kernel, \(\kappa(x)=-\sum_{j\ge0}e^{-a_j|x|}\), and inserts it into a
   Brown--Halmos identity. Its §5 identifies the polar layer with the
   exterior Hankel operator and its §6 proves that the exterior test is a
   reparametrization of the weak equation: at first contact, the polar
   jets vanish multiplied by \(\lambda=0\). The formula of §2 below is a
   direct specialization of that kernel to the concrete candidate of
   R170_829, not a new kernel.
5. P122_028 builds the finite two-prime Green complex; P122_029 shows
   that critical transmission requires a trace condition that the scalar
   equation does not supply. P124_011 identifies the Tate collar as a
   Schur crossblock and localizes the still-open rank condition.
6. R170_829--830 prove that every lift of \(D_\Delta\succ0\) must leave
   the window and propose \(Y_+=\iota_+(I-D)R_L\). They do not compute
   \(\Lambda\iota_+\).

The new contribution of this note is: (i) writing the complete response
of \(A_1\) for that \(\iota_+\) and its reflection, with its domain and
its jump; (ii) proving that (0.1), as written, lacks a canonical exterior
Tate port; and (iii) giving the exact matrix equation that remains once
that port is chosen.

## 2. Response of a right tail

Let \(a>0\),

\[
 z_a^+(s)={\bf1}_{(T,\infty)}(s)e^{-as},\qquad
 \ell_d={\Lambda(d)\over\sqrt d},\qquad
 L_M=\sum_{2\le d\le M}\ell_d\tau_{\log d},                 \tag{2.1}
\]

with the convention of Paper 47, \((\tau_bz)(t)=z(t+b)\).

### Lemma 2.1 (right exterior Green)

The tail \(z_a^+\) belongs to the domain of the operator \(m(D)\). For
almost every \(t\in I_T\),

\[
 \boxed{
 (A_1z_a^+)(t)=
 -{1\over2}\int_{T-t}^{\infty}K(u)e^{-a(t+u)}\,du
 -e^{-at}\sum_{\substack{2\le d\le M\\t>T-\log d}}
       \Lambda(d)d^{-a-1/2}.}                                 \tag{2.2}
\]

In particular, if \(F\in L^2(I_T)\), then

\[
 \langle F,A_1z_a^+\rangle
 =\langle F,g_{a,M}^+\rangle_{I_T},                            \tag{2.3}
\]

where \(g_{a,M}^+\) is the right-hand side of (2.2).

**Proof.** The transform of \(z_a^+\) decays like
\(O((a+|\tau|)^{-1})\). Since \(m(\tau)=O(\log(2+|\tau|))\), we have
\(m\widehat z_a^+\in L^2\), hence \(z_a^+\in\operatorname{dom}m(D)\).
For \(t<T\), the constant term and the identity term of (1.1) do not
connect the supports. Only \(z(t+u)\) survives in the cosine, giving the
first term of (2.2). Moreover \(L_M^*z_a^+(t)=0\) on \(I_T\), while

\[
 (L_Mz_a^+)(t)=e^{-at}\sum_{t>T-\log d}
 \Lambda(d)d^{-a-1/2}.
\]

This proves (2.2). The function obtained lies in \(L^2(I_T)\), as can
also be seen from the jump bound in §3, and hence (2.3) holds by
density. ∎

For a column \(c=(c_m)_{m\le L}\), put \(q_m=b_mc_m\). Then

\[
 \left.A_1\iota_+c\right|_{I_T}
 =\sum_{m\le L}q_mg_{a_m,M}^+.                                \tag{2.4}
\]

The prime sum of (2.2), paired with \(F\), is literally the right collar

\[
 -\sum_{d\le M}\Lambda(d)d^{-a-1/2}
   \int_{\max(-T,T-\log d)}^T e^{-at}\overline{F(t)}\,dt,     \tag{2.5}
\]

with the corresponding conjugate convention. This recovers the same
truncated geometry as \(\mathcal E_{N,L}\); it is not replaced by a
complete moment.

## 3. The jump: logarithm, not delta

Since \(K(u)=u^{-1}+O(1)\) as \(u\downarrow0\), (2.2) gives

\[
 (m(D)z_a^+)(t)
 =-{e^{-aT}\over2}\log {1\over T-t}+O(1),
 \qquad t\uparrow T.                                         \tag{3.1}
\]

The term \(O(1)\) may depend on \(a,T\), but it is uniform on a terminal
subinterval. Hence the jumped trace generates a logarithmic singularity,
belonging to \(L^p_{\rm loc}\) for every \(p<\infty\), and not a delta
mass. This agrees with the logarithmic order character of \(m(D)\) and
with the potentials \(A_T,B_T\) of
P121_RESOLVED_TATE_COLLAR_INTEGRAL. Treating the exponential as an
eigenvector through the indicator would omit precisely (3.1).

## 4. Reflected orientation

Let \(z_a^-=Jz_a^+={\bf1}_{(-\infty,-T)}e^{as}\). Since \(m\) is even,
\(Jm(D)J=m(D)\), and \(JL_MJ=L_M^*\). Hence

\[
 \boxed{g_{a,M}^-(t):=(A_1z_a^-)(t)=g_{a,M}^+(-t).}           \tag{4.1}
\]

Here \(L_M^*\) survives, not \(L_M\), and the logarithm appears when
approaching \(-T\) from the right. An extension compatible with
reflection must use both columns; a single tail does not preserve both
orientations of the collar.

## 5. Typing defect of the Tate port

### Lemma 5.1 (the weak equation does not define the exterior pairing)

The information

\[
 r_F(t)=\alpha_F e^{-t/2}+\beta_F e^{t/2},\qquad t\in I_T,    \tag{5.1}
\]

does not determine \(\langle r_F,z\rangle\) for a function \(z\) supported
on \(I_T^c\).

**Proof.** Two global extensions of each character that agree on
\(I_T\) can differ by any admissible function supported on \(I_T^c\).
Their pairing with an exterior tail changes in general. The weak
equation only proves equalities against window tests, so it does not
distinguish these extensions. The zero extension produces the value zero
by disjointness of supports; extension by the global characters produces
nonzero integrals (and for \(e^{t/2}\) against certain tails it even
requires \(a>1/2\)). Both have the same restriction (5.1). ∎

P121 fixes \((\alpha_F,\beta_F)\) from \(J_\pm(F)\), and R161_009
constructs canonical polar corrections for its Hardy ports. Neither of
these results declares that (0.1) is the \(L^2(\mathbb R)\) pairing with
a global extension of (5.1). Adopting such a declaration would be a new
transmission law, precisely the kind of datum that P122_029 marks as
open.

Hence the claim of R170_830 that \(Y_+\) belongs to the logarithmic
domain is correct, but that is not enough for \(\Lambda Y_+\) to be
defined: the second term of (0.1) still needs typing.

## 6. Matrix equation after choosing a port

Define the already-computed response operator

\[
 \Gamma_{+,M}:\mathbb C^L\longrightarrow Z^*,\qquad
 (\Gamma_{+,M}c)(F)=
 \left\langle F,\sum_{m\le L}b_mc_mg_{a_m,M}^+\right\rangle. \tag{6.1}
\]

Let \(\Theta_+:\mathbb C^L\to Z^*\) be any additional exterior Tate
port, explicitly specified. Then the candidate of R170_829 satisfies
exactly

\[
 \Lambda_+Y_+
 =(\Gamma_{+,M}-\Theta_+)(I-D_{N,L})R_L,                      \tag{6.2}
\]

and the Green obligation is

\[
 \boxed{
 \operatorname{Herm}\!\left[(\Gamma_{+,M}-\Theta_+)
 (I-D_{N,L})R_L\right]
 =R_L^*(I-D_{N,L})R_L.}                                      \tag{6.3}
\]

For two orientations the reflected copy of (6.2) is added, with its own
port \(\Theta_-\). Formulas (2.2), (4.1) compute the whole Gamma--Euler
block of (6.3). What remains is no longer "the action of \(m(D)\)" nor a
mysterious boundary distribution: it is (a) choosing and justifying
\(\Theta_\pm\) from the existing crossed currents and (b) proving the
resulting matrix equality over all of \(Z\).

Choosing the zero extension, \(\Theta_\pm=0\), is mathematically
possible but does not follow from the weak equation nor from the causal
ports of the corpus. Even with that choice, (6.3) would be a new
identity and does not follow from the collar formula
\(R_LB_N=D_NR_L-\mathcal E_N\).

## 7. Status

```text
domain of the cut tails for m(D)                         PROVED
right and left Gamma--Euler response                     PROVED
jump = logarithmic singularity, no delta                 PROVED
identification with the known truncated collars          PROVED
exterior Tate port determined by the weak equation       FALSE
canonical choice Theta_± compatible with P121/R161        OPEN
Herm(Lambda Y)=D_Delta                                    OPEN
global inequality / D                                     OPEN
```
