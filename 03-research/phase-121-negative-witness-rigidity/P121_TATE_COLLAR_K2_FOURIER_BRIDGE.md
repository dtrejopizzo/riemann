# P121 -- the Tate-collar Fourier realization of the oriented K2 residue

## Status

This note constructs an exact bridge between two objects which had so far
been kept in separate ledgers:

* the physical left/right Tate collars of a compact-window state; and
* the tame coefficient `K_F(lambda_(p,k))` of the oriented relative `K_2`
  class.

The bridge is an elementary Fourier--Stieltjes identity.  It uses no Weil
sign, no critical zero, and no division by zeta.  It does not by itself
prove that the residue vanishes.  Its value is that the remaining
orientation-Rees lift can now be formulated entirely on a physical boundary
profile.

## 1. Complete collar profiles

Let `F in L^2(-T,T)`, extended by zero, and for `sigma in {+1,-1}` put

\[
 \begin{aligned}
 R_\sigma(a)&=\int_{T-a}^{T}e^{\sigma t/2}F(t)\,dt,\\
 L_\sigma(a)&=\int_{-T}^{-T+a}e^{\sigma t/2}F(t)\,dt,
 \end{aligned}
 \qquad 0\leq a\leq2T.                         \tag{1.1}
\]

Both profiles are absolutely continuous and

\[
 \begin{aligned}
 dR_\sigma(a)&=e^{\sigma(T-a)/2}F(T-a)\,da,\\
 dL_\sigma(a)&=e^{\sigma(-T+a)/2}F(-T+a)\,da.
 \end{aligned}                                    \tag{1.2}
\]

Write

\[
 K_F(w)=\int_{-T}^{T}F(t)e^{-wt}\,dt.              \tag{1.3}
\]

### Theorem 1.1 -- collar/Laplace dictionary

For every complex `z`,

\[
 \boxed{
 \begin{aligned}
  \int_0^{2T}e^{-za}\,dR_\sigma(a)
    &=e^{-zT}K_F(-z-\sigma/2),\\
  \int_0^{2T}e^{-za}\,dL_\sigma(a)
    &=e^{-zT}K_F(z-\sigma/2).
 \end{aligned}}                                    \tag{1.4}
\]

#### Proof

For the first identity set `t=T-a`; for the second set `t=-T+a`.
Using (1.2) gives respectively

\[
 e^{-zT}\int_{-T}^{T}F(t)e^{(z+\sigma/2)t}\,dt,
 \qquad
 e^{-zT}\int_{-T}^{T}F(t)e^{(-z+\sigma/2)t}\,dt,
\]

which are the two expressions in (1.4).  No boundary trace of `F` is used.
QED.

## 2. The local Euler divisor is a collar Fourier mode

Take the positive Tate character and put

\[
 \lambda_\omega=-\frac12+i\omega.
\]

Theorem 1.1 at `sigma=+1` gives

\[
 \boxed{
 \begin{aligned}
 K_F(\lambda_\omega)
   &=e^{-i\omega T}\int_0^{2T}e^{i\omega a}\,dR_+(a),\\
 K_F(\lambda_\omega)
   &=e^{ i\omega T}\int_0^{2T}e^{-i\omega a}\,dL_+(a).
 \end{aligned}}                                    \tag{2.1}
\]

If `F` is primitive, then `R_+(0)=L_+(0)=0` and
`R_+(2T)=L_+(2T)=M_+(F)=0`.  Integration by parts therefore yields, for
`omega != 0`,

\[
 \boxed{
 \begin{aligned}
 K_F(\lambda_\omega)
   &=-i\omega e^{-i\omega T}
       \int_0^{2T}e^{i\omega a}R_+(a)\,da,\\
 K_F(\lambda_\omega)
   &= i\omega e^{ i\omega T}
       \int_0^{2T}e^{-i\omega a}L_+(a)\,da.
 \end{aligned}}                                    \tag{2.2}
\]

For a prime `p` and an integer `k`, the simple local Euler divisor is

\[
 \lambda_{p,k}=-\frac12+\frac{2\pi i k}{\log p}.
                                                               \tag{2.3}
\]

Consequently the oriented tame coefficient constructed in
`P121_ORIENTED_K2_LOCALIZATION_EXACTNESS.md` is exactly a Fourier mode of
either complete Tate-collar profile:

\[
 c^{(1)}_{p,k}(F)=K_F(\lambda_{p,k}).                \tag{2.4}
\]

This is a source-side equality.  The points (2.3) are zeros of the known
local factor `1-p^(-1/2-s)`, not critical zeros of the completed zeta
function.

## 3. Compatibility with the universal orientation-Rees character

Let `eta` be the orientation-Rees variable.  The physical localized pair is

\[
 \bigl(-K_F(\lambda_{p,k}),K_F(\lambda_{p,k})\bigr).
\]

The universal character therefore becomes

\[
 \operatorname {Reg}^{\rm or}_{p,k}(F;\eta)
   =(\eta-\eta^{-1})K_F(\lambda_{p,k}).             \tag{3.1}
\]

Equations (2.1)--(2.2) realize the coefficient of (3.1) as an ordinary
Fourier mode of a physical boundary object.  In particular,

\[
 \frac12\eta\partial_\eta
 \operatorname {Reg}^{\rm or}_{p,k}(F;\eta)|_{\eta=1}
 =K_F(\lambda_{p,k})                               \tag{3.2}
\]

is not an abstract conormal coordinate: it is the collar mode (2.1).

### Corollary 3.1 -- cofinal collar faithfulness

Let `P` be an unbounded set of primes.  For a primitive state `F`, the
following are equivalent:

1. `c^(1)_(p,1)(F)=0` for every `p in P`;
2. the right-collar transform in (2.1) vanishes at
   `omega_p=2 pi/log p` for every `p in P`;
3. `K_F` is identically zero;
4. `F=0` almost everywhere on `(-T,T)`.

#### Proof

The equivalence of 1 and 2 is (2.4).  As `p` tends to infinity through
`P`, `omega_p` tends to zero.  The points
`-1/2+i omega_p` are distinct and accumulate at the finite point `-1/2`.
Since `K_F` is entire, the identity theorem proves 3.  Laplace injectivity
proves 4, and the reverse implications are immediate.  QED.

This cofinal statement avoids the aliasing present for one fixed prime: all
harmonics of one period determine only the periodization of a collar longer
than that period.

## 4. Exact remaining source law

The former lift problem can now be stated without critical divisors or
Meyer quotients:

> **Tate-collar orientation law.**  A first-contact state has zero
> Fourier--Stieltjes transform (2.1) at the first local Euler frequency of
> a cofinal family of primes.

Once this law is proved, Corollary 3.1 gives `F=0`; first contact is
impossible and the global square follows by the already established
first-contact reduction.

The present note proves the dictionary needed for that law.  It does not
deduce the law from the scalar first-contact equation.  The next source
calculation must act on the whole collar profile `a -> R_+(a)` before the
Gamma integral and the prime samples in `J_+(F)` are collapsed to one
number.

## 5. Ledger

```text
complete physical Tate-collar profile                    CONSTRUCTED
collar Laplace transform = compact-source K_F             PROVED
local K2 tame coefficient = collar Fourier mode           PROVED
compatibility with orientation-Rees normal                PROVED
cofinal collar faithfulness                               PROVED
first contact annihilates the cofinal collar modes         OPEN
global square and row (d)                                 OPEN
```
