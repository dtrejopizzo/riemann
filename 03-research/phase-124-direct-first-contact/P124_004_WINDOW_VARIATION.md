# P124.004 -- window variation at first contact

Status: `ONE-SIDED IDENTITY + OBSTRUCTION`.  Varying the support window
through the P122.002 unitary realization gives an exact crossing quotient,
including prime-power births.  The quotient has no forced sign on the
first-contact domain.  In the available domain one cannot differentiate
the Euler shift terms, and the birth terms have only collar-mass control.

## 1. Transport and domain

Let `T_* > log 2` and let `F_*` be a parity first-contact state.  Put
`f_*=U_{T_*}^{-1}F_*` on `(-1,1)`, where

\[
(U_Tf)(t)=T^{-1/2}f(t/T).
\]

The fixed form domain is

\[
\mathcal Q=\left\{f:\int\log(2+|\xi|)|\widehat f(\xi)|^2\,d\xi<\infty\right\},
\]

and `f_* in P_{T_*} cap Q` by P122.002.  Write the pulled-back Tate moments

\[
\ell_{T,\pm}(f)=\int_{-1}^1 e^{\pm Tx/2}f(x)\,dx .
\]

Choose two smooth interior bumps `b_+,b_-` such that the matrix
`\ell_{T_*,\tau}(b_\sigma)` is invertible.  After shrinking the `T`
neighborhood, the same matrix remains invertible.  Define the finite-rank
Tate correction

\[
C_Tf=f-\sum_{\sigma=\pm}a_\sigma(T,f)b_\sigma,
\qquad
\ell_{T,\pm}(C_Tf)=0.
\]

Then `T -> C_Tf` is `C^1` from `L^2` to `L^2` and from `Q` to `Q` for fixed
`f`, because the correctors are smooth.  This is an explicit version of
the P122.002 moving Tate correction.  Set

\[
f_T=C_Tf_*,
\qquad F_T=U_Tf_T.
\]

Thus `F_T` is an admissible primitive trial vector in the window `I_T`.
By unitarity, the physical value `q_T(F_T)` equals the pulled-back value
defined below on `f_T`.  No differentiability of the full form in `T` is
assumed.

Use logarithmic window time

\[
s=\log(T/T_*),\qquad T_s=T_*e^s,\qquad f_s=f_{T_s}.
\]

For `s<=0` close enough, first contact gives

\[
q_{T_s}(F_s)\ge0,\qquad q_{T_*}(F_*)=0.
\]

Consequently the left crossing quotient obeys the formal sign constraint

\[
\frac{q_{T_s}(F_s)-q_{T_*}(F_*)}{s}\le0
\qquad(s<0).
\tag{1.1}
\]

Any direct contradiction would have to prove the opposite sign for the
same quotient from the arithmetic formula below.

## 2. Exact quotient formula

For a prime power `n` write

\[
w_n={\Lambda(n)\over\sqrt n},
\qquad
\alpha_n(s)={\log n\over T_s}.
\]

On `L^2(-1,1)` define

\[
J_{\alpha,\pm}f(x)=2^{-1/2}
\mathbf1_{[-1,1-\alpha]}(x)\,[f(x+\alpha)\pm f(x)],
\qquad 0\le\alpha\le2,
\]

and

\[
B_\alpha(f)=\|J_{\alpha,-}f\|^2-\|J_{\alpha,+}f\|^2
=-2\operatorname {Re}\int_{-1}^{1-\alpha}
f(x+\alpha)\overline{f(x)}\,dx .
\tag{2.1}
\]

The pulled-back row-(d) form is

\[
\boxed{
Q_s(g)=
\int h(\xi/T_s)|\widehat g(\xi)|^2\,d\xi
-m_0\|g\|^2
+\sum_{2\le n<e^{2T_s}}w_n B_{\alpha_n(s)}(g),}
\tag{2.2}
\]

where `h(tau)=Re psi(5/4+i tau/2)-psi(5/4)`.  This is the P122.002 fixed
window form, equivalent to the phase-118 scattering realization.

Since `Q_0(f_*)=0`, the exact crossing identity is

\[
\boxed{
\frac{Q_s(f_s)}{s}
=\frac{\mathcal G_s(f_s)-\mathcal G_0(f_*)}{s}
-m_0\,\frac{\|f_s\|^2-\|f_*\|^2}{s}
+\sum_{n\in A_s\cap A_0}w_n
  \frac{B_{\alpha_n(s)}(f_s)-B_{\alpha_n(0)}(f_*)}{s}
+\mathcal B_s,}
\tag{2.3}
\]

where

\[
\mathcal G_s(g)=\int h(\xi/T_s)|\widehat g(\xi)|^2\,d\xi,
\qquad
A_s=\{n:\ 2\le n<e^{2T_s},\ \Lambda(n)\ne0\},
\]

and the birth/death contribution is

\[
\mathcal B_s=
{1\over s}
\left(
\sum_{n\in A_s\setminus A_0}w_nB_{\alpha_n(s)}(f_s)
-\sum_{n\in A_0\setminus A_s}w_nB_{\alpha_n(0)}(f_*)
\right).
\tag{2.4}
\]

Equations (2.3)--(2.4) include threshold births.  If no prime power lies at
`e^{2T_*}`, then `A_s=A_0` for all small `s` and `\mathcal B_s=0`.

## 3. What can be differentiated

The Gamma multiplier part is differentiable in logarithmic time on `L^2`.
Indeed `sup_tau |tau h'(tau)|<infinity`, as used in P122.002, so dominated
convergence gives

\[
{d\over ds}\mathcal G_s(f_*)\bigg|_{s=0}
=-\int {\xi\over T_*}h'(\xi/T_*)|\widehat{f_*}(\xi)|^2\,d\xi .
\tag{3.1}
\]

The finite-rank Tate correction is also differentiable.  If
`\dot f_0=d f_s/ds|_{s=0}`, then

\[
\ell_{T_*,\pm}(\dot f_0)
=-\dot\ell_{T_*,\pm}(f_*)
=\mp {T_*\over2}\int_{-1}^1 x e^{\pm T_*x/2}f_*(x)\,dx .
\tag{3.2}
\]

Were the whole form differentiable, the correction would contribute

\[
2\operatorname {Re}q_{T_*}(f_*,\dot f_0).
\tag{3.3}
\]

Since `\dot f_0` is generally not in `P_{T_*}`, this is a Tate-normal term,
not zero.  If, after absorbing the harmless nonzero unitary-scaling
constants into `c_+` and `c_-`,

\[
A_{T_*}f_*=c_+e^{T_*x/2}+c_-e^{-T_*x/2}
\]

in the pulled-back anti-dual convention, then

\[
q_{T_*}(f_*,\dot f_0)
=c_+\ell_{T_*,+}(\dot f_0)+c_-\ell_{T_*,-}(\dot f_0).
\tag{3.4}
\]

Thus window transport can see the existing Tate multiplier, but it does
not determine its sign or make it vanish.

## 4. Why the Euler quotient has no form derivative on `Q`

For an old active channel with `0<alpha_n(0)<2`, P122.002 proves

\[
B_{\alpha_n(s)}(g)\to B_{\alpha_n(0)}(g)
\]

uniformly for `g` in bounded subsets of `Q`, after compact inclusion into
`L^2`.  This is the continuity needed for first-contact attainment.  It is
not a differentiability statement.

The exact estimate available from the proof is only

\[
|B_\beta(g)-B_\alpha(g)|
\le
(\|J_{\beta,-}g\|+\|J_{\alpha,-}g\|)
 \|(J_{\beta,-}-J_{\alpha,-})g\|
+(\|J_{\beta,+}g\|+\|J_{\alpha,+}g\|)
 \|(J_{\beta,+}-J_{\alpha,+})g\|.
\tag{4.1}
\]

The right side is `o(1)` on bounded `Q` sets.  No rate follows.  Dividing
by `s` is therefore unjustified.

This is a real domain wall, not just a missing lemma.  The generator of
translations is a first derivative, while `Q` is only logarithmic.  There
are functions in `Q` which are not in any positive Sobolev space.  For
such functions the difference quotients of translated correlations can
fail to converge, so the Euler part has no derivative as a form on the
whole first-contact domain.

A concrete model is obtained by taking Fourier mass in narrow packets near
frequencies `N_k` with masses `a_k>0` such that

\[
\sum_k a_k\log N_k<\infty,\qquad
\sum_k a_kN_k=\infty .
\tag{4.2}
\]

Choosing the phases so that `e^{i\alpha N_k}` aligns at a fixed old
channel `alpha`, the correlation
`\langle \tau_{\alpha+h}u,\tau_\alpha u\rangle` has logarithmic form norm
finite, but its `h^{-1}` difference quotient has no finite limit along
suitable `h_k`.  To place this inside the finite-window channel, choose
two small interior intervals `I` and `I+alpha` and put one copy of `u` on
`I` and the translated copy on `I+alpha`; the cutoff endpoints then do not
move for small `h`, and `B_{\alpha+h}` contains this same translated
correlation plus terms with the same regularity.  This lies inside the
P122.002 form scale and outside the translation-generator domain.  Hence
an Euler window derivative cannot be used for an arbitrary first-contact
minimizer unless extra regularity of that minimizer is proved first.

If one assumed extra `H^1` regularity and traces, then for smooth `f` an
old channel would satisfy

\[
{d\over d\alpha}B_\alpha(f)
=-2\operatorname {Re}
\left[
\int_{-1}^{1-\alpha}f'(x+\alpha)\overline{f(x)}\,dx
-f(1)\overline{f(1-\alpha)}
\right].
\tag{4.3}
\]

But (4.3) is not available for `F_*`; P121 gives only `H^s`, `s<1/2`, for
the zero extension.

## 5. Birth terms

Suppose `n_0=e^{2T_*}` is a prime power.  Then `n_0` is not in `A_0` because
the active condition is strict, but it belongs to `A_s` for `s>0`.  Put
`\delta_s=2-\alpha_{n_0}(s)=2(1-e^{-s})=2s+O(s^2)`.  From (2.1),

\[
B_{\alpha_{n_0}(s)}(f_s)
=-2\operatorname {Re}\int_{-1}^{-1+\delta_s}
f_s(x+\alpha_{n_0}(s))\overline{f_s(x)}\,dx .
\tag{5.1}
\]

Therefore

\[
|B_{\alpha_{n_0}(s)}(f_s)|
\le
2\|f_s\|_{L^2(1-\delta_s,1)}
 \|f_s\|_{L^2(-1,-1+\delta_s)}.
\tag{5.2}
\]

The right side tends to zero for `L^2` functions, so births are continuous.
There is no universal `O(s)` estimate.  The quotient
`s^{-1}B_{\alpha_{n_0}(s)}(f_s)` depends on endpoint collar densities and
on the relative phase of the two collars.  With only `Q` regularity it can
oscillate or blow up along subsequences while still tending to zero before
division by `s`.

Thus births also supply no sign.  Positive `w_{n_0}` does not help, because
`B_alpha` is the signed difference
`||J_-f||^2-||J_+f||^2`, equivalently the negative real correlation of the
two endpoint collars.

## 6. Crossing verdict

The first-contact hypotheses give the unilateral inequality (1.1).  The
arithmetic form gives the exact quotient (2.3).  To contradict first
contact one would need, for `s<0`,

\[
{Q_s(f_s)\over s}>0
\]

or a right-hand identity incompatible with the first loss.  The available
terms do not have such a sign:

```text
Gamma scale derivative            bounded, signed multiplier not positive
Tate correction                    existing normal multiplier c, sign free
old Euler shift quotients          continuous on Q, not differentiable
prime-power births                 collar-mass o(1), no divided rate/sign
```

Consequently window variation does not force `c=0`, does not force the
two-prime flux to vanish, and does not exclude a first-contact state.

The precise next useful arrow is not a new stationary control definition.
It would have to be an arithmetic estimate strengthening one of the two
weak points above:

```text
old-channel route:
  prove a signed logarithmic difference-quotient bound for the Euler
  correlations of the actual first-contact minimizer, beyond P122.002

birth route:
  prove a one-sided endpoint collar density/phase law for the actual
  first-contact minimizer, strong enough to sign (5.1)/s
```

Either estimate would be new information.  Norm continuity of the
whitened channels, subcritical Sobolev regularity, and the scalar radical
identity do not provide it.
