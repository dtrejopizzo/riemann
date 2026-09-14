# P124.001 -- joint Gamma--Euler variation

Status: `OBSTRUCTION + NEXT ARROW`.  The joint first variation of the
literal phase-120 state system is well typed on the first-contact domain,
but it gives no new Tate or flux law.  It is exactly the already known
primitive radical equation, and its non-primitive extension only recovers
the existing Tate multiplier.

## 1. Fixed-window setup

Fix `T>log 2`, write `I_T=(-T,T)`, and let

\[
\mathcal P_T=\{F:\ \langle F,e^{t/2}\rangle_{I_T}
=\langle F,e^{-t/2}\rangle_{I_T}=0\}.
\]

The closed first-contact form domain is the primitive Gamma form domain
used in P122.002.  For the calculation start from smooth bumps compactly
supported in the interior of `I_T`.  Choose two fixed interior bumps
`b_+,b_-` for which the matrix

\[
(\langle b_\sigma,e^{\tau t/2}\rangle)_{\sigma,\tau=\pm}
\]

is invertible.  Subtracting the corresponding linear combination of
`b_+,b_-` preserves compact interior support and enforces the two Tate
moments.  This is the regular primitive core used below.  P122.002 then
passes the identity to the first-contact minimizer by the closed form
topology and polarization.  The smooth representers `e^{\pm t/2}` are not
used as compact-support correctors.

Use the literal phase-120 source maps in the physical finite-window
convention:

\[
x_p=O_{p,T}F,\qquad
(I-r_pV_{\log p,T})x_p=s_pF,
\]

and

\[
u_n=R_nF,\qquad
(-\partial_t^2+4\alpha_n^2)u_n=4\alpha_n^2F,
\quad \alpha_n=n+\frac14.
\]

A variation of the source is transported jointly:

\[
\delta x_p=O_{p,T}\phi,\qquad
\delta u_n=R_n\phi .
\]

Here `V_{\log p,T}` is the truncated shift on `I_T`, equivalently zero
extension, whole-line shift, and restriction back to the finite window.
This convention retains the activation and tail terms of the sharp window;
`O_{p,T}` is not replaced by a whole-line resolvent whose exterior tail is
discarded afterwards.  The state variables are not independent variations.

The on-shell signed action is

\[
\mathcal S_T(F)=
\sum_n I_n(F,R_nF)+(\theta_T-m_0)\|F\|^2
-\sum_p(\log p)\|O_{p,T}F\|^2.
\]

By P3_LITERAL_STATE_SYSTEM, this is exactly

\[
\mathcal S_T(F)=q_T(F)=-B_{{\rm nuc},T}(F,F)
\]

on the primitive window.

## 2. Complete first variation

All pairings below use the convention that `q_T` is Hermitian and linear in
the second argument.  The Frechet differential of the real quadratic
action is therefore `2 Re q_T(F,phi)`.  Equivalently, the displayed
complex identities give the representing sesquilinear form before taking
real parts.

For a regular primitive direction `phi`, the Gamma part gives

\[
\delta I_n(F,R_nF)[\phi]
=2\operatorname {Re}\alpha_n^{-1}\langle F-R_nF,\phi\rangle .
\]

Indeed the `delta u_n` terms cancel against the Euler equation for the
oscillator.  If this is derived by Green's formula, the whole-line
`H^1` minimizer supplies no independent endpoint condition; the boundary
terms are exactly the terms killed by the oscillator equation.

The prime part gives

\[
\delta\{-\log p\,\|O_{p,T}F\|^2\}[\phi]
=-2\operatorname {Re}(\log p)\langle O_{p,T}F,O_{p,T}\phi\rangle .
\]

Writing the truncated shift equation against the adjoint merely rewrites
this as an `O_{p,T}^*O_{p,T}` term.  The activation/collar contributions
of the sharp shift are contained in that adjoint operator; no separate
sign or transmission condition is produced by the differentiation.

Hence the full transported source variation is

\[
\boxed{
\frac12\,\delta\mathcal S_T(F)[\phi]
=
\operatorname {Re}\Big(
\sum_n\alpha_n^{-1}\langle F-R_nF,\phi\rangle
+(\theta_T-m_0)\langle F,\phi\rangle
-\sum_p(\log p)\langle O_{p,T}F,O_{p,T}\phi\rangle
\Big)
=\operatorname {Re}q_T(F,\phi).}
\tag{2.1}
\]

All sums are first read on the regular core with finite support window and
then by the closed form limit.  P122.002 supplies the compact-whitened
continuity needed at prime births; no raw-`L2` continuity is used.

## 3. Substitution of a first-contact minimizer

Let `F_*` be the parity first-contact state supplied by P122.002.  Then

\[
q_{T_*}\ge 0,\qquad q_{T_*}(F_*,F_*)=0.
\]

For a nonnegative closed Hermitian form, equality in the quadratic value
implies orthogonality to the form domain.  Therefore

\[
\boxed{q_{T_*}(F_*,\phi)=0\qquad(\phi\in \mathcal P_{T_*}\cap\mathcal Q).}
\tag{3.1}
\]

Combining (2.1) and (3.1) gives

\[
\delta\mathcal S_{T_*}(F_*)[\phi]=0
\qquad(\phi\in \mathcal P_{T_*}\cap\mathcal Q).
\tag{3.2}
\]

This is the precise point where the candidate loses information: (3.2) is
not by itself a new boundary identity.  It is the first-contact radical
equation `P_T A_T P_TF_*=0` written through the literal state variables.
This does not make the polarized identity useless in every later argument:
a special choice of test direction, combined with an independent
arithmetic estimate, could still force a boundary condition.  The present
joint variation supplies no such extra estimate.

If `psi` is not primitive and `phi=P_Tpsi`, (3.1) becomes

\[
\langle A_TF_*,P_T\psi\rangle=0.
\]

Equivalently,

\[
A_TF_*=c_+e^{t/2}+c_-e^{-t/2}
\quad\text{in the anti-dual of the closed form domain.}
\tag{3.3}
\]

After fixing parity this is exactly the known Tate forcing line

\[
r_\eta(t)=c(e^{t/2}+\eta e^{-t/2}),\qquad \eta=\pm1.
\tag{3.4}
\]

The scalar `c` is a Lagrange multiplier for the two primitive constraints.
Stationarity on the primitive tangent space gives no equation for it.
Thus the joint Gamma--Euler source variation does not prove `c=0`.

## 4. Boundary and flux verdict

P121 gives the graph-renormalized incoming current

\[
\mathcal L^{\rm gr}_{T,-}(F_*)=-\mathcal Z_{T,+}r_\eta.
\tag{4.1}
\]

P122.019 and P122.029 prove that a nonzero `c` creates literal activation
jumps, and that critical Lions--Magenes transmission across one seam is
equivalent on the Tate line to `c=0`.  The variation above does not place
the current (4.1) in `H^{1/2}` or `H^{1/2}_{00}`.  It therefore cannot
activate the P122.019/P122.029 gate.

The same obstruction appears in the two-prime Green complex.  P122.028
shows that the harmonic extension between two prime fibres has constant
flux

\[
j=\frac{E_{q,T}\mathfrak h_{F_*}-E_{p,T}\mathfrak h_{F_*}}
        {\log(q/p)}
\]

and energy

\[
\mathcal E_{p,q}^{\rm eff}(F_*)
=\frac{\|(E_{q,T}-E_{p,T})\mathfrak h_{F_*}\|^2}{\log(q/p)}.
\]

The transported first variation allows only endpoint changes induced from
one source variation `phi`.  It does not vary the two endpoint fibres
independently, and it does not identify the scalar nullity of `q_T` with
`\mathcal E_{p,q}^{\rm eff}=0`.  Consequently it proves neither zero flux
nor prime-seam matching.

The first candidate is therefore tautological in the exact required sense:

```text
joint variation of F, x_p, u_n
        = real derivative of the reduced on-shell form q_T
first-contact equality
        = q_T(F_*, phi)=0 on primitive directions
non-primitive rewrite
        = existing Tate multiplier r_eta
new c=0 or zero-flux law
        NOT OBTAINED
```

## 5. Boundary-variation continuation

This note does not introduce a stationary boundary-control principle.  Such
a principle would be an extra source law, not a consequence of the joint
on-shell variation above.

The admissible continuation is to vary the actual support window and use
only identities already attached to the windowed form.  In that setting the
available first-contact input is a one-sided crossing inequality for
transported primitive trial vectors, not stationarity of artificial
controls.  P124.004 carries out that calculation with `U_T`, finite-rank
Tate correction and prime-power births.

The remaining useful possibility for the polarized identity is narrower:
a special primitive test `G` may still matter if it comes with an
independent arithmetic estimate or limiting theorem that signs a boundary
term.  Without that added estimate, `q_T(F_*,G)=0` is only the radical
identity in another coordinate.
