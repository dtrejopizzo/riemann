# D.76 — Adelic extension of the compact potential and the global colligation gate

## Status

D.75 constructs a faithful supported primitive module.  This note tensors
that module with the finite Frobenius orbit features and the complete Gamma
oscillator.  The resulting feature correspondence reproduces the exact
relative form of D.73: every prime power and the Gamma finite part occur
before any sign is taken.

The local-to-global audit is decisive.  A block-diagonal sum of supported
local compressions cannot give the required form, because a single prime
fiber has positive primitive directions.  Any correction must therefore mix
finite places with Gamma before compression.  The unique algebraic map that
such a mixing must dilate is constructed below.  Its Hilbert Julia
colligation exists exactly when the assembled A--B--C form is nonpositive on
the primitive module.  Thus abstract unitary dilation does not prove the
missing inequality; it is equivalent to it.

An explicit guard-band Hilbert--Schmidt lift is also constructed.  It solves
support and directedness, but its ordinary Fourier leakage is the rational
tail of D.75 rather than the prime--Gamma form.  Identifying its **semilocal
adelic** leakage with the exact feature correspondence is the remaining
source theorem.  No RH, zeta zero, or positivity is assumed.  The paper is
not modified.

## 1. Supported primitive source

On a window `I_T=[-T,T]`, let

\[
 X_T=\{F\in C_c^\infty(I_T):M_-(F)=M_+(F)=0\}.              \tag{1.1}
\]

D.75 gives the canonical compact potential

\[
 W_TF=-e^{-|\cdot|/2}*F,\qquad
 L W_TF=F,qquad L=D^2-\frac14,                              \tag{1.2}
\]

with

\[
 \operatorname {supp}(W_TF)\subseteq I_T.                   \tag{1.3}
\]

Thus `W_T` is injective, commutes with translation and with zero extension,
and replaces the distributional periodic frame by a supported Hilbert
coordinate without changing the source test: `F=L W_TF`.

Equip `X_T` with the graph norm transported by (1.2), strengthened by the
Gamma form when necessary.  All maps below are continuous on this common
core.

## 2. Finite-place orbit fibers

For a prime `p`, put

\[
 r_p=p^{-1/2},\qquad U_p=S_{\log p},\qquad
 A_p=\sqrt{1-r_p^2}(I-r_pU_p)^{-1}.                          \tag{2.1}
\]

The inverse is norm convergent and

\[
 A_p^*A_p-I
 =\sum_{k\ne0}p^{-|k|/2}S_{k\log p}.                        \tag{2.2}
\]

Define on the potential module

\[
 S_{p,T}(u)=\sqrt{\log p}\,A_pLu,
 \qquad B_{p,T}(u)=\sqrt{\log p}\,Lu.                       \tag{2.3}
\]

Then for `u=W_TF`,

\[
 \begin{aligned}
 \|S_{p,T}u\|^2-\|B_{p,T}u\|^2
  &=\log p\sum_{k\ne0}p^{-|k|/2}
       \langle F,S_{k\log p}F\rangle\\
  &=2\sum_{k\ge1}{\Lambda(p^k)\over\sqrt{p^k}}
       \operatorname {Re}\langle F,S_{k\log p}F\rangle.
 \end{aligned}                                               \tag{2.4}
\]

This verifies every power `p^k` on the supported module.  If `log p>2T`,
all nonzero correlations in (2.4) vanish.  Hence only

\[
 \mathcal P_T=\{p:p\le e^{2T}\}                             \tag{2.5}
\]

is needed, without truncating a nonzero local contact.

## 3. Gamma fiber

Let `partial_infinity` be the oscillator boundary derivation of D.32 and

\[
 m_0=\log\pi-\psi(1/4).                                     \tag{3.1}
\]

On the same source define

\[
 S_{\infty,T}(u)=\sqrt{m_0}\,Lu,
 \qquad B_{\infty,T}(u)=\partial_\infty Lu.                  \tag{3.2}
\]

Then

\[
 \|S_{\infty,T}u\|^2-\|B_{\infty,T}u\|^2
 =m_0\|F\|^2-\|\partial_\infty F\|^2                       \tag{3.3}
\]

and

\[
 \|\partial_\infty F\|^2
 =\int_0^\infty{e^{-r/2}\over1-e^{-2r}}
       \|F-S_rF\|^2\,dr.                                   \tag{3.4}
\]

Thus (3.3) is the full digamma phase, including the finite-part constant;
it is not a high-frequency approximation.

## 4. Exact adelic feature correspondence

Put

\[
 \begin{aligned}
 \mathbf S_Tu&=\bigl((S_{p,T}u)_{p\in\mathcal P_T},
                       S_{\infty,T}u\bigr),\\
 \mathbf B_Tu&=\bigl((B_{p,T}u)_{p\in\mathcal P_T},
                       B_{\infty,T}u\bigr).
 \end{aligned}                                               \tag{4.1}
\]

These take values in finite Hilbert direct sums on every fixed window.  By
Sections 2--3,

\[
 \boxed{
 \|\mathbf S_TW_TF\|^2-\|\mathbf B_TW_TF\|^2
 =B_{{\rm nuc},T}(F,F).}                                    \tag{4.2}
\]

Polarization gives the sesquilinear equality.  Prime and window enlargement
are compatible because inactive correlations vanish and `W_T` commutes with
zero extension.

> **Theorem 4.1 (adelic potential correspondence).**  The triple
> \[
> X_T\xrightarrow{W_T}H^1_0(I_T)
> \overset{\mathbf S_T}{\underset{\mathbf B_T}{\rightrightarrows}}
> \mathcal H_T^{\rm feat}                                  \tag{4.3}
> \]
> is a directed, source-defined correspondence whose signed Gram pullback
> is exactly `B_nuc,T`, with all `p^k` and Gamma.  This constructs the
> requested local fibers and their algebraic gluing before a sign.

The form in (4.2) is relative: the two separate cofinal norms diverge if all
primes are inserted without first fixing the support window.  D.73's exact
stabilization is therefore essential.

## 5. Why local block-diagonal compression is impossible

Suppose each place admitted a Hilbert space `K_v`, a support projection
`P_v`, a unitary `U_v` and a supported lift `M_v` with

\[
 M_v^*(U_v^*P_vU_v-P_v)M_v
 =S_v^*S_v-B_v^*B_v.                                       \tag{5.1}
\]

The left side is always negative semidefinite.  But a finite-place fiber is
not.  D.67 supplies compact primitive vectors supported just beyond the
first contact threshold for which

\[
 \|S_{2,T}u\|^2-\|B_{2,T}u\|^2>0.                           \tag{5.2}
\]

Equivalently, the local multiplier

\[
 \log p\bigl(P_{p^{-1/2}}(e^{i\tau\log p})-1\bigr)           \tag{5.3}
\]

takes positive values.  Hence (5.1) is impossible already for `p=2`.

> **Proposition 5.1 (local compression no-go).**  No orthogonal sum of
> place-by-place supported compression identities can reproduce (4.2)
> term by term.  Any successful `U_ad` must mix finite places and Gamma
> before the support projection is applied.

This does not say that Gamma cannot correct a positive prime fiber.  It says
that the correction cannot be block diagonal: the local terms must reappear
as trace components of a globally coupled operator, not as negative local
squares.

## 6. The unique global contraction and its Julia dilation

Let

\[
 \mathcal R_{B,T}=\overline{\operatorname {Ran}(\mathbf B_TW_T)},
 \qquad
 \mathcal R_{S,T}=\overline{\operatorname {Ran}(\mathbf S_TW_T)}. \tag{6.1}
\]

Because every finite-place `B_p` contains a nonzero scalar multiple of
`F=L W_TF`, the map `mathbf B_TW_T` is injective whenever `P_T` is nonempty.
There is therefore a densely defined algebraic comparison

\[
 C_{0,T}(\mathbf B_TW_TF)=\mathbf S_TW_TF.                   \tag{6.2}
\]

It is the only comparison compatible with all local labels.  Its defect is

\[
 \|C_{0,T}\mathbf B_TW_TF\|^2
 -\|\mathbf B_TW_TF\|^2
 =B_{{\rm nuc},T}(F,F).                                     \tag{6.3}
\]

Consequently

\[
 \boxed{
 C_{0,T}\text{ extends to a contraction}
 \Longleftrightarrow B_{{\rm nuc},T}|_{X_T}\le0.}            \tag{6.4}
\]

If the equivalent conditions hold, let

\[
 D_C=(I-C^*C)^{1/2},\qquad D_{C^*}=(I-CC^*)^{1/2}.            \tag{6.5}
\]

The Julia colligation

\[
 \mathcal U_C=
 \begin{pmatrix}C&D_{C^*}\\D_C&-C^*\end{pmatrix}           \tag{6.6}
\]

is unitary from `R_B direct-sum R_S` to
`R_S direct-sum R_B`.  For the supported first-summand map

\[
 \mathcal M_TF=(\mathbf B_TW_TF,0),                          \tag{6.7}
\]

the first output component is `mathbf S_TW_TF`, and hence

\[
 \mathcal M_T^*(\mathcal U_C^*P_S\mathcal U_C-P_B)\mathcal M_T
 =B_{{\rm nuc},T}.                                          \tag{6.8}
\]

After the standard stabilization identifying the two direct sums, (6.8)
has the abstract form requested in D.73.

> **Theorem 6.1 (global colligation gate).**  A Hilbert Julia unitary with
> the exact feature pullback exists if and only if the row-D inequality is
> already true on the window.  The potential functor makes the comparison
> canonical and supported, but it does not make `C_0,T` contractive.

A partial isometry does not weaken the gate: every corner of a unitary or
partial isometry is contractive.  Replacing `C_0` by the always-contractive
bounded transform

\[
 \widetilde C=C_0(I+C_0^*C_0)^{-1/2}                         \tag{6.9}
\]

changes the defect to

\[
 \|\widetilde Cx\|^2-\|x\|^2
 =-\langle x,(I+C_0^*C_0)^{-1}x\rangle,                     \tag{6.10}
\]

which is not (6.3).  It proves a different negative form and loses the
prime--Gamma trace.

## 7. A concrete guard-band supported lift

The potential module nevertheless gives a non-tautological Hilbert--Schmidt
candidate.  Let `L>T` and

\[
 I_L=[-L,L],\qquad J_{L,T}=[-L+T,L-T].                       \tag{7.1}
\]

For `u=W_TF`, define

\[
 \mathcal G_{T,L}(F)
 =|J_{L,T}|^{-1/2}C_uP_{J_{L,T}},                            \tag{7.2}
\]

where `C_u` is convolution by `u`.  Since

\[
 J_{L,T}+\operatorname {supp}u\subseteq I_L,                 \tag{7.3}
\]

the range is supported:

\[
 P_{I_L}\mathcal G_{T,L}(F)=\mathcal G_{T,L}(F).             \tag{7.4}
\]

Its kernel is `u(x-y)` on `I_L times J_(L,T)`, so

\[
 \|\mathcal G_{T,L}(F)\|_{\rm HS}^2=\|u\|_2^2.              \tag{7.5}
\]

It is faithful because `F=L u`, and it is compatible with window
enlargement after increasing the guard band.

For the ordinary real Fourier transform, its compression defect reduces to
the rational tail computed in D.75 and is not (4.2).  Replacing Fourier by
the semilocal scattering product

\[
 \Theta_T(\tau)=u_\infty(\tau)
       \prod_{p\in\mathcal P_T}{b_{p^{-1/2}}
          (e^{i\tau\log p})\over e^{i\tau\log p}}            \tag{7.6}
\]

puts every correct local phase into one unitary multiplier.  But Meyer's
Toeplitz identity then gives a difference of the two boundary Hankel
squares, together with the positive-chart and zeta nonunitarity defects of
D.45; it does not yet identify (7.2)'s single leakage norm with (4.2).

Thus (7.2) is an actual supported and faithful lift, not a specification.
The missing equality is the **adelic guard-band trace theorem**

\[
 \operatorname {Tr}\bigl(mathcal G_{T,L}(F)^*
 (U_{\rm ad}^*P_{I_L}U_{\rm ad}-P_{I_L})
 \mathcal G_{T,L}(G)\bigr)
 =B_{{\rm nuc},T}(F,G),                                    \tag{7.7}
\]

uniformly and compatibly in `L`.  The ordinary Fourier transform falsifies
(7.7); the source-defined semilocal `U_ad` required to prove it has not been
constructed.

## 8. What global mixing would have to do

Proposition 5.1 and Theorem 6.1 leave one non-circular possibility.  A
geometric `U_ad` could mix the local orbit fibers so that:

1. its **total** supported leakage is a negative norm;
2. decomposition of its nuclear trace, only after the mixing, yields the
   positive and negative local summands (2.4) and (3.3);
3. the induced first corner is `C_0,T` by the exact trace comparison;
4. contractivity of that corner follows from a source support theorem,
   rather than being assumed or defined spectrally.

Local Crofoot maps cannot supply this because they fail continuous scaling
covariance (D.38).  The only currently constructed map with the correct
global covariance is the Poisson range map, whose Hilbert range is nonclosed
(D.74).  An adelic guard-band theorem would have to combine these two
structures without taking a Moore--Penrose inverse.

## 9. Verdict

The compact potential has been extended to an exact adelic **feature
correspondence**.  Equations (2.4), (3.3) and (4.2) verify all prime powers,
Gamma, and their relative gluing.

No placewise supported unitary can realize those terms.  The global Julia
unitary exists precisely when the assembled comparison `C_0,T` is a
contraction, which is the desired row-D sign.  Therefore abstract dilation
is not a proof.

The guard-band operator (7.2) is the new concrete candidate: support,
faithfulness and Hilbert--Schmidt control are proved.  What remains is the
source construction of a semilocal `U_ad` satisfying the exact trace
identity (7.7).  Row D is not declared closed.

