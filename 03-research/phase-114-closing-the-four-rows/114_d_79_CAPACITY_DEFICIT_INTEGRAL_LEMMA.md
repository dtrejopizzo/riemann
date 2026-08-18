# D.79 supplement — positive deficit integral for a directed capacity bound

## Status

The capacity needed at `T=log(2)` is numerically the difference of two
nearby quantities.  This note rewrites it as a monotone positive integral.
It permits a rigorous lower certificate on a finite frequency interval;
the unintegrated tail may be discarded rather than bounded above.

## Lemma

Let `R>=0`, let `g>0`, and let `v` be a unit vector.  Put

\[
 a_g=\langle v,(R+gI)^{-1}v\rangle,
 \qquad
 \delta_g={1\over g}-a_g.                               \tag{1}
\]

Then

\[
 \delta_g
 =\left\langle v,
 {R\over g(R+gI)}v\right\rangle\geq0.                  \tag{2}
\]

Let `Q_v=I-|v><v|`.  The shorted capacity of `gQ_v+R` on `span(v)` is

\[
 \boxed{
 \operatorname{cap}_g(v;R)
 ={1\over a_g}-g
 ={g^2\delta_g\over1-g\delta_g}.}                      \tag{3}

Consequently, for `ell>0`,

\[
 \boxed{
 \delta_g>{\ell\over g(g+\ell)}
 \quad\Longrightarrow\quad
 \operatorname{cap}_g(v;R)>\ell.}                      \tag{4}

### Proof

The resolvent identity gives

\[
 {1\over g}I-(R+gI)^{-1}
 ={R\over g(R+gI)},                                     \tag{5}

which proves (2).  Set `A=R+gI`.  Since

\[
 gQ_v+R=A-g|v\rangle\langle v|,                         \tag{6}

the rank-one resolvent formula, or the one-dimensional Schur complement,
gives

\[
 \operatorname{cap}_g={1-ga_g\over a_g}={1\over a_g}-g.
                                                                    \tag{7}
\]

Substitution of `a_g=1/g-delta_g` proves (3); elementary rearrangement
proves (4).

## Fourier multiplier form

If `R` is translation invariant with nonnegative multiplier `r(tau)`,
Plancherel gives

\[
 \boxed{
 \delta_g={1\over2\pi}\int_{\mathbb R}
 |\widehat v(\tau)|^2
 {r(\tau)\over g(g+r(\tau))}\,d\tau.}                  \tag{8}

The integrand is nonnegative.  Therefore, for every `Omega>0`,

\[
 \delta_g\geq {1\over2\pi}\int_{-\Omega}^{\Omega}
 |\widehat v(\tau)|^2
 {r(\tau)\over g(g+r(\tau))}\,d\tau.                  \tag{9}

An outward-rounded lower quadrature of (9) is a valid global lower bound;
no Fourier-tail or aliasing estimate is needed.  This is the crucial
directional advantage over certifying `a_g` itself.

For a non-unit vector `w`, apply the formulas to
`v=w/||w||`; both its norm enclosure and the integral must be directed
consistently.

The scalar algebra and threshold equivalence are checked in
`114_d_79_capacity_deficit_verify.py`.

