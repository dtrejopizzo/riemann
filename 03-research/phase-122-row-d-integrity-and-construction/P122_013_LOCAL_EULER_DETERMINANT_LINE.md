# P122 -- a local Euler determinant line with rank-one curvature

## Status

`IMPORTED FRAMEWORK + PROVED SPECIALIZATION` as a local Hermitian
construction.  The Toeplitz--Hankel identity and determinant line over the
restricted Grassmannian are classical; the exact degree-one Euler
specialization, arithmetic normalization and port audit are derived here.
`CANDIDATE BUILDING BLOCK`, not a global `D_candidate` and not a proof of
row (d).

A degree-one Euler factor canonically defines an oriented Hermitian line
whose Chern Hessian is the rank-one root functional.  What is potentially
new is its proposed role in D, not the underlying operator or
Grassmannian formulas.  It is constructed before `B_nuc`, changes to its
dual under port reversal, and has higher rank for a shifted degree-two
factor.

The unresolved global theorem is stated exactly in Section 6.

Classical sources for the imported framework are Brown--Halmos,
*Algebraic Properties of Toeplitz Operators*, J. Reine Angew. Math. 213
(1964), 89--102, <https://doi.org/10.1515/crll.1964.213.89>, and the
restricted-Grassmannian determinant-line framework of Pressley--Segal and
Segal--Wilson; see <https://pmihes.centre-mersenne.org/articles/10.1007/BF02698802/>.

## 1. Source data

Let

\[
 H_+=H^2(S^1)=\ell^2(\mathbb N_0),\qquad
 S e_j=e_{j+1},qquad 0<r<1,
\]

and attach to the degree-one local factor `(1-rz)^(-1)` its logarithmic
connection

\[
 A_r={rS\over1-rS}=\sum_{n\ge1}r^nS^n.             \tag{1.1}
\]

For the prime `p`, `r=p^(-1/2)` and the arithmetically normalized connection
is `(log p)A_r`.  Nothing in this definition uses the Weil form, its sign,
or a first-contact vector.

Put

\[
 \ell_r(h)=\sum_{j\ge0}r^{j+1}h_j.                 \tag{1.2}
\]

This is a bounded linear functional on `H_+`.

## 2. Toeplitz--Hankel factorization

Let

\[
 \phi_r(z)={rz\over1-rz}=\sum_{n\ge1}r^nz^n.
\]

Then `A_r=T_(phi_r)`.  If `P_+` is the Hardy projection, define

\[
 H_{\bar\phi_r}=(1-P_+)M_{\bar\phi_r}P_+:
 H_+\longrightarrow H_- .                          \tag{2.1}
\]

In the bases `z^j`, `j>=0`, and `z^(-k)`, `k>=1`, its matrix is

\[
 (H_{\bar\phi_r})_{k,j}=r^{k+j}.                   \tag{2.2}
\]

It is therefore rank one and

\[
 \|H_{\bar\phi_r}h\|^2
 ={1\over1-r^2}|\ell_r(h)|^2.                      \tag{2.3}
\]

The elementary Toeplitz product identity gives

\[
 C_r:=A_r^*A_r-A_rA_r^*
     =H_{\bar\phi_r}^*H_{\bar\phi_r}
     ={1\over1-r^2}\ell_r^*\ell_r.                \tag{2.4}
\]

This reproves Theorem 1.1 of
`P121_LOCAL_HANKEL_ROOT_OBSERVABLE_AUDIT.md` and identifies the positive
operator as a Hardy-polarization defect.

## 3. The Hermitian line

For `h in H_+`, form the rank-one Hilbert--Schmidt operator

\[
 Z_h:H_+\longrightarrow H_-,\qquad
 Z_hx=\langle x,e_0\rangle H_{\bar\phi_r}h.         \tag{3.1}
\]

Its graph is in the big chart of the restricted Grassmannian.  Pull the
dual tautological determinant line on that chart back along
`h -> graph(Z_h)`.  In the standard graph frame its canonical metric is

\[
 \|s_r(h)\|_{L_r}^2
 ={1\over\det(1+Z_h^*Z_h)}
 ={1\over1+\Phi_r(h)},\qquad
 \Phi_r(h)={|\ell_r(h)|^2\over1-r^2}.              \tag{3.2}
\]

Thus this is literally a determinant line, not a name assigned to an
arbitrary positive form.  With the convention
`Theta=-partial bar-partial log ||s||^2`, its Chern curvature is

\[
 \Theta_{r,h}(u,\bar v)
 ={1\over(1+\Phi_r(h))^2}
 {\ell_r(u)\over\sqrt{1-r^2}}
 \overline{{\ell_r(v)\over\sqrt{1-r^2}}}.         \tag{3.3}
\]

In particular, at the undeformed Hardy polarization,

\[
 \Theta_{r,0}(h,\bar h)=\langle h,C_rh\rangle
 ={1\over1-r^2}|\ell_r(h)|^2\ge0,                 \tag{3.4}
\]

and the curvature has complex rank one everywhere.

This metric is not selected by matching `B_nuc`.  Formulae (3.1)--(3.2) are
forced by the graph determinant of the off-diagonal Hardy block of the
logarithmic derivative of the local Euler factor.

For arithmetic normalization replace `A_r` by `(log p)A_r`; then

\[
 \Theta_{p,0}(h,\bar h)
 ={(\log p)^2\over1-p^{-1}}
   \left|\sum_{j\ge0}p^{-(j+1)/2}h_j\right|^2.     \tag{3.5}
\]

The connection itself retains the required linear coefficients
`(log p)p^(-n/2)`; the square in (3.5) appears only after taking Hermitian
curvature.

## 4. Orientation and the port-swap test

Reversing the Hardy polarization exchanges `A_r` and `A_r^*`.  Therefore

\[
 A_rA_r^*-A_r^*A_r=-C_r.                           \tag{4.1}
\]

Assign `L_r` to the positive causal port and its Hermitian dual `L_r^vee`
to the negative port.  Port reversal exchanges these two lines and sends
their curvature to its negative.  Thus the antisymmetric datum exists
before scalar supertrace and cannot factor through the port-symmetric
quotient of P122.005.

This gives a canonical answer to the first falsifier in
`P122_D_SPECIFICATION.md`: the sign-changing object is the oriented
determinant line of the Hardy polarization defect.

## 5. Degree is detected before comparison

For a product of distinct local factors, put

\[
 \phi(z)=\sum_{a=1}^d{r_az\over1-r_az}.
\]

The Hankel matrix of `H_(bar phi)` is a sum of `d` geometric rank-one
matrices.  Its range is contained in the span of the `d` geometric vectors,
and has rank `d` when the nonzero `r_a` are distinct.  The corresponding
graph-determinant construction therefore has curvature rank `d` at the
undeformed polarization.

For `xi(s+a)xi(s-a)` the two radii
`p^(-1/2-a)` and `p^(-1/2+a)` are distinct for `a ne 0`, so the local
curvature is generically rank two.  The zeta factor has rank one.  This
distinction is intrinsic to the source Euler degree and is present before
any comparison with the analytic target.  Davenport--Heilbronn has no
Euler-factor input from which (1.1) can be assembled, so the construction
is unavailable there.

## 6. What this constructs, and what it does not

For every active prime this note constructs:

```text
degree-one Euler factor
  -> oriented Hardy polarization defect
  -> Hermitian line L_p
  -> positive rank-one Chern curvature.
```

This discharges locally three requirements of D: source provenance,
orientation before trace, and a nonflat positive Hermitian square.  It also
passes two essential synthetic falsifiers.

It does not yet assemble the global line or prove its equality law.  The
physical first-contact equations provide two history vectors `h_(p,+)` and
`h_(p,-)` and only the cross-port norm relation

\[
 \|A_ph_{p,+}\|=\|A_p^*h_{p,-}\|.                 \tag{6.1}
\]

They do not place one vector in both terms of the commutator.  Consequently
(6.1) does not imply

\[
 \Theta_p(h_{p,+},\bar h_{p,+})=0.                 \tag{6.2}
\]

Identifying the histories would be the already missing annular transport
law.  Tensoring the local lines does not repair this: curvatures add, but
reciprocity alone supplies no trivialization compatible with their
Hermitian metrics.

P122.014 makes this warning exact: the naive tensor/dual determinant line
has curvature `q_T`, so its semipositivity is equivalent to row (d).  The
local line may only be used inside a new source trivialization or
central-extension law, not as another positive-lift factorization.

The exact remaining construction problem is now geometric rather than
merely formal:

> Construct a global oriented determinant line `L_T` whose restrictions are
> the `L_p`, including the Gamma and Tate boundary factors, and prove from
> its source complex that a primitive first-contact section is metrically
> flat.  Its local positive curvature would then force every active
> rank-one root coordinate to vanish.

Until that global line and flatness theorem exist, `L_p` is a verified local
building block and must not be advertised as row D.
