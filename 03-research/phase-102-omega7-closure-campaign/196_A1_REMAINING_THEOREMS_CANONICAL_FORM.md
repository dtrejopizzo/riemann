# A1 remaining theorems in canonical form

## Purpose

After `187`--`195`, the A1 obstruction has been reduced to a small number
of exact theorem statements.  This file records those statements in one
place and separates them from routes that have already been shown
insufficient.

This is not a closure proof.  It is the current canonical list of theorems
whose proof would close A1, and therefore Omega7 through the phase assembly.

## A1 target

For \(n\ge8\), compact A1 is
\[
\boxed{
  C_n(T_n)
  =
  \lambda_n
  -
  {1\over4}\lambda_n^{\rm arch}
  -
  R_n(T_n)
  \ge0.
}
\tag{1}
\]

Together with the finite certificate for \(1\le n\le7\), A0, and the
boundary-limit reduction, (1) closes Omega7 by Li.

## Theorem A: direct compact core

Prove directly
\[
\boxed{
  C_n(T_n)\ge0
  \qquad(n\ge8).
}
\tag{2}
\]

Equivalent current forms include:

1. the original signed Laguerre compact core;
2. the lobe-balance inequality from `145`;
3. the raised-balance hierarchy from `146`;
4. the finite jet certificate from `147`--`148`;
5. the diagonal recurrence certificates from `183`--`190`.

The most explicit diagonal finite form is
\[
\boxed{
  \mathcal A_n+\Pi_n+
  \sum_{m\le e^{T_n}}\Lambda(m)\Xi_n(m)\ge0
  \qquad(n\ge9),
}
\tag{3}
\]
plus \(C_8^\ast\ge0\).

## Theorem B: absolute diagonal domination

Choose an explicit envelope
\[
  |E(e^u)|\le R(u)
  \qquad(0\le u\le T_n).
\]

Prove the uniform weighted \(L^1\) domination
\[
\boxed{
  \mathcal B_n
  \ge
  \int_0^{T_n}R(u)e^{-u}|\mathcal H_n(u)|\,du
  \qquad(n\ge9).
}
\tag{4}
\]

Using the sign-partition certificate of `193`, this is equivalent to
\[
\boxed{
  \sup_{n\ge9}\left(W_n(R)-\mathcal B_n\right)\le0.
}
\tag{5}
\]

This theorem is sufficient, not intrinsic: it closes A1 by an absolute
estimate and discards signed cancellation.

The terminal part of this theorem is sharpened by `201` and `207`.  For a
relative PNT envelope \(A\exp(-\eta(u))\), the A0 cutoff at the preceding
index gives only
\[
  \mathcal T_n
  \le
  {n^2\over12(n-1)^2}B_{n-1}
  \log {1+T_n\over1+T_{n-1}}.
\]
Thus even the terminal Laguerre interval requires either a cutoff-ratio
comparison against \(\mathcal B_n\), one extra decay surplus, or a sharper
signed argument; A0 alone does not prove Theorem B.

`208` evaluates this cutoff-ratio loss for canonical Vinogradov--Korobov
cutoffs and shows that the terminal load is only \((5/72)\log n+O(1)\).
This removes a terminal-scale explosion for that cutoff policy, but it does
not prove Theorem B.

`209` explains why: the recurrence archimedean forcing has
\[
  D_n^{\rm arch}=-{1\over2}\log n+O(1),
\]
so \(1+\frac34D_n^{\rm arch}\) is eventually negative.  Therefore the
positive weights \(w_{n,k}\) do not make \(\mathcal B_n\) a positive
reserve.  At this point in the chronology the absolute route still needed
a full lower bound for \(\mathcal B_n\) and control of the cumulative mixed
\(L^1\) loads; `219` later collapses the mixed structure, and `221` then
rules out the resulting VK absolute route by bulk scale.

`210` identifies the large-\(n\) coefficient
\[
  \Gamma_{\mathcal B}
  =
  {\Delta_8^\ast\over16}
  +{1\over2}\sum_{k=8}^{\infty}
  {1+\frac34D_k^{\rm arch}\over k(k+1)}
\]
for the base budget:
\[
  \mathcal B_n=\Gamma_{\mathcal B}n^2+O(n\log n).
\]
Thus terminal absorption for canonical VK cutoffs is reduced to the sign
and effective evaluation of \(\Gamma_{\mathcal B}\).  This does not by
itself control the non-terminal cumulative kernel, whose raw mixed form is
treated in `211`, `218`, and finally collapsed in `219`.

`211` isolates those mixed loads.  On \((T_j,T_{j+1})\), the cumulative
kernel contains degrees \(k-1\) with \(k\) running up to \(n-1\), while the
local A0 cutoff is calibrated at the \(j\)-scale.  Hence Theorem B also
requires a uniform off-diagonal Laguerre \(L^1\) theorem, or a signed
replacement for the absolute estimate.

`212` evaluates the infinite archimedean part of \(\Gamma_{\mathcal B}\) by
telescoping:
\[
  \Gamma_{\mathcal B}
  =
  {1+\Delta_8^\ast\over16}
  -{3\over64}(\lambda_8^{\rm arch}-\lambda_7^{\rm arch}).
\]
Thus the terminal large-\(n\) budget coefficient is positive exactly when
\[
  \Delta_8^\ast
  >
  {3\over4}(\lambda_8^{\rm arch}-\lambda_7^{\rm arch})-1
  =
  -0.7175270082\ldots .
\]
This reduces the terminal budget sign to a finite compact-base inequality,
but it still leaves that inequality and the non-terminal cumulative load
unproved.

`213` sharpens the finite-base inequality further.  Substituting
\[
  \Delta_8^\ast=C_8(T_8)-C_7(T_7)
\]
into the formula for \(\Gamma_{\mathcal B}\) cancels the finite
archimedean difference and gives
\[
  \Gamma_{\mathcal B}={I_7(T_7)-I_8(T_8)\over16}.
\]
Thus the terminal large-\(n\) budget coefficient is positive exactly when
\[
  I_7(T_7)>I_8(T_8).
\]
This is a compact signed arithmetic base comparison, not a consequence of
the finite Li certificate by itself.

`214` expands this comparison into a finite prime-power certificate:
\[
\begin{aligned}
  16\Gamma_{\mathcal B}
  &=
  \sum_{m\le e^{T_7}}\Lambda(m)
  [\Phi_7(\log m,T_7)-\Phi_8(\log m,T_8)]\\
  &\quad
  -
  \sum_{e^{T_7}<m\le e^{T_8}}\Lambda(m)\Phi_8(\log m,T_8)
  -\Psi_7(T_7)+\Psi_8(T_8)
\end{aligned}
\]
when \(T_8\ge T_7\), with elementary endpoint formulae for all
\(\Phi,\Psi\).  Thus the positive-budget case is finite once the base
cutoffs are fixed.

`215` shows that the positive-budget case follows from the ordinary base
condition if the auxiliary \(T_7\) is normalized small.  For
\[
  0<T_7\le\min(\log2,1/130),
\]
one has \(I_7(T_7)>-1\).  If \(C_8^\ast\ge0\), then
\[
  I_8(T_8)\le -8+{3\over4}\lambda_8^{\rm arch}<-{29\over4},
\]
so \(I_7(T_7)>I_8(T_8)\) and hence \(\Gamma_{\mathcal B}>0\).  Thus the
separate terminal budget sign gate is absorbed into the still-open base
certificate \(C_8^\ast\ge0\).

`216` expands that base certificate:
\[
  C_8^\ast\ge0
  \Longleftrightarrow
  \Psi_8(T_8)
  -
  \sum_{m\le e^{T_8}}\Lambda(m)\Phi_8(\log m,T_8)
  \ge
  8-{3\over4}A_8.
\]
This is a finite prime-power inequality once \(T_8\) is fixed.  A finite
strong-margin proof
\[
  \lambda_8\ge {1\over2}A_8
\]
would also imply \(C_8^\ast\ge0\) by the A0 tail bound.

`217` executes this finite strong-margin alternative.  The extended
rational Euler--Gamma/Stieltjes verifier proves
\[
  \lambda_8-{1\over2}\lambda_8^{\rm arch}
  >
  1.455305710633246144455217.
\]
Therefore A0 gives \(C_8^\ast>0\), and with `215` the sign
\(\Gamma_{\mathcal B}>0\) is closed.  The remaining terminal task is the
finite effective threshold of `220`; the non-terminal absolute task is
then collapsed by `219` and obstructed for VK envelopes by `221`.

`219` carries out the cancellation in the cumulative mixture.  The
telescoping identity gives
\[
  \mathcal H_n(u)=-L_{n-1}^{(2)}(u)
  \qquad(T_8<u<T_n),
\]
and the only exceptional pieces are fixed degree-7 corrections on
\((0,T_7)\) and \((T_7,T_8)\).  Hence the raw mixed off-diagonal
obstruction is closed.  The absolute route is now reduced to the collapsed
single-Laguerre weighted \(L^1\) theorem
\[
  \mathcal B_n\ge W_n(\varepsilon),
\]
where \(W_n\) is the three-piece expression in `219`.

`220` sharpens the terminal-threshold statement.  With
\[
  \Theta_n=
  {n^2\over12(n-1)^2}B_{n-1}
  \log{1+T_n\over1+T_{n-1}},
\]
the terminal interval is controlled exactly by
\[
  \mathfrak D_n=\mathcal B_n-\Theta_n\ge0.
\]
Moreover `217` and `215` give the explicit lower bound
\[
  \Gamma_{\mathcal B}>{25\over64},
\]
while canonical VK cutoffs give \(\Theta_n=O(\log n)\).  Hence terminal
absorption is closed for all sufficiently large \(n\).  What remains
terminally is the finite rational threshold certificate for
\(\mathfrak D_n\ge0\) below an explicit \(N_0\).

`218` shows that the raw mixed \(L^1\) theorem cannot be obtained by the crude
combination of local A0 decay and the elementary Laguerre bound.  On
\((T_j,T_{j+1})\), A0 supplies \((1+u)^{-(j+1)}\), while an off-diagonal
term \(L_{k-1}^{(2)}\) costs \((1+u)^{k-1}\), leaving
\[
  (1+u)^{k-j-2}.
\]
This crude route is superseded by `219`: the needed cancellation in the
cumulative mixture is exact, so the raw off-diagonal mixed obstruction is
closed rather than estimated term-by-term.

`221` shows that this collapsed absolute route is still too expensive for
canonical VK envelopes.  In the bulk \(u\asymp n\), Plancherel--Rotach
gives absolute Laguerre mass with exponential factor \(e^{u/2}\), while VK
relative decay is only subexponential in \(n\).  Thus
\(W_n(\varepsilon)\) is exponential for VK envelopes, whereas
\(\mathcal B_n=O(n^2)\).  The absolute VK route is therefore ruled out as
a closure mechanism for A1.

`222` returns to the signed balance route with the telescoped kernel.  In
the integrated identity, all jumps after \(T_8\) vanish, leaving only the
two endpoint jumps \(T_7,T_8\).  The current signed finite target is
\[
  \mathcal A_n+\Pi_n^{\rm tel}
  +\sum_{m\le e^{T_n}}\Lambda(m)\Xi_n^{\rm tel}(m)\ge0
  \qquad(n\ge9).
\]

`223` shows that this signed target cannot be closed by a symmetric
envelope for \(B(U)\).  Such an envelope again produces an absolute
\(L^1\) load, now for \(L_{n-1}^{(3)}\), and VK-scale decay loses to the
Laguerre bulk.  The signed route therefore needs genuine prime-power sign
correlation.

`224` records the logical strength of Theorem C below: the strong margin,
together with the finite \(1\le n\le7\) certificate, implies all Li
coefficients are nonnegative and hence RH by Li's criterion.  It remains a
valid closure route, but it is not a consequence of the size estimates
already available in A0/VK form.

`225` consolidates the decision: the symmetric absolute VK route is
discarded.  The remaining active targets are the signed finite inequality
from `222`, a one-sided tail theorem, strong margin, comparative
Loewner--Schur positivity, or the global half-plane theorem.

`226` removes the integrated \(B\)-layer from the signed target.  Direct
expansion of \(\psi(e^u)\) gives the equivalent finite inequality
\[
  \mathcal A_n-P_n+\sum_{m\le e^{T_n}}\Lambda(m)\Omega_n(m)\ge0,
\]
where every \(\Omega_n(m)\) is an endpoint expression in
\(e^{-u}L_{n-1}^{(1)}\) plus fixed degree-7 corrections.  This is the
current smallest signed prime-power target.

`227` uses the strict small-\(T_7\) normalization \(0<T_7<\log2\) to remove
the \(\log m<T_7\) prime block from that target.  The direct signed
certificate now has only two arithmetic regimes: \(T_7\le\log m<T_8\) and
\(T_8\le\log m\).

`228` rewrites the high regime as a single signed correlation:
\[
  \mathcal P_n^{\rm high}
  =
  e^{-T_n}L_{n-1}^{(1)}(T_n)\Psi_{[T_8,T_n]}
  -
  \sum_{e^{T_8}\le m\le e^{T_n}}
  {\Lambda(m)\over m}L_{n-1}^{(1)}(\log m).
\]
Thus the remaining high-block theorem is a prime-power/Laguerre
correlation estimate.

`229` combines `226`--`228` into a single direct signed target.  The only
moving arithmetic transform left is
\[
  \sum_{m\le e^{T_n}}{\Lambda(m)\over m}
  L_{n-1}^{(1)}(\log m),
\]
with all nonmoving arithmetic corrections confined to the fixed base
window \(\log m<T_8\).

`230` removes the last notational layer: with
\[
  S_n(T)=\sum_{m\le e^T}{\Lambda(m)\over m}
  L_{n-1}^{(1)}(\log m),
\]
A1 is exactly the one-transform inequality
\[
  S_n(T_n)
  \le
  E(e^{T_n})e^{-T_n}L_{n-1}^{(1)}(T_n)
  +1-L_n^{(0)}(T_n)
  +{3\over4}\lambda_n^{\rm arch}-n.
\]

`231` gives the partial-summation equivalent of the high-block transform:
\[
  \mathcal C_n^{\rm high}
  =
  A_8(T_n)L_{n-1}^{(1)}(T_n)
  +\int_{T_8}^{T_n}A_8(u)L_{n-2}^{(2)}(u)\,du.
\]
Thus the same frontier can be read as a signed weighted-discrepancy
theorem for \(A_8(u)-(u-T_8)\).

`232` records that a two-sided envelope for \(E_8^\sharp\) cannot close the
weighted-discrepancy form: it again gives an absolute \(L^1\) Laguerre load
in the bulk.

`233` packages the same single transform at a fixed cutoff:
\[
  \mathcal S_T(z)
  =
  {z\over(1-z)^2}
  \sum_{m\le e^T}{\Lambda(m)\over m^{1/(1-z)}}.
\]
For fixed \(T\), coefficient positivity is ordinary holomorphic
coefficient positivity.  A1 still needs those coefficients along the
moving diagonal \(T=T_n\).

`234` identifies the weighted-Mertens discrepancy with the ordinary
Chebyshev error:
\[
  E_8^\sharp(u)
  =
  e^{-u}E(e^u)-e^{-T_8}E(e^{T_8})
  +
  \int_{T_8}^{u}e^{-t}E(e^t)\,dt.
\]
Thus the partial-summation frontier is another signed
Chebyshev--Laguerre coordinate, not an independent positivity mechanism.

`235` computes the exact moving-cutoff derivative:
\[
  C_n'(T)=-(\psi(e^T)-e^T)e^{-T}L_{n-1}^{(2)}(T)
\]
between prime-power jumps, while the jumps themselves cancel.  Therefore
fixed-cutoff positivity transfers to the moving cutoff \(T_n\) only through
a signed integral theorem.

`236` records the zero-side margin audit.  From
\[
  C_n(T_n)=\lambda_n-{1\over4}\lambda_n^{\rm arch}-R_n(T_n),
\]
Li positivity or critical-line support alone is not the internal compact A1
statement.  A zero-side or explicit-formula route still needs strong
margin, one-sided tail placement, or an equivalent compact margin theorem.

`237` identifies cutoff transfer with the same one-sided tail gate:
\[
  R_n(T_n)\le\lambda_n-{1\over4}\lambda_n^{\rm arch}.
\]
Thus neither fixed-cutoff positivity nor full-cutoff/Li positivity moves to
the compact cutoff without signed tail information or strong margin.

`238` writes the same condition in compensation variables:
\[
  C_n(T_n)=M_n+\delta_n,\qquad
  M_n=\lambda_n-\frac12\lambda_n^{\rm arch},\quad
  \delta_n=\frac14\lambda_n^{\rm arch}-R_n(T_n)\ge0.
\]
The tail route must prove \(\delta_n\ge -M_n\) whenever the strong margin
excess \(M_n\) is negative.

`239` gives the quantitative ladder: if
\[
  \lambda_n\ge\kappa_nA_n,\qquad R_n(T_n)\le\rho_nA_n,
\]
then A1 is exactly \(\kappa_n-\rho_n\ge1/4\).  This interpolates between
the strong-margin route and one-sided tail improvements.

`240` normalizes the same condition by defining
\[
  d_n={(-M_n)_+\over A_n},\qquad s_n={\delta_n\over A_n}.
\]
Compact A1 is exactly \(s_n\ge d_n\).

`241` packages the tail surplus into the generator
\[
  \Delta_T={1\over4}\mathcal A-\mathcal R_T.
\]
A0 gives \([z^n]\Delta_{T_n}\ge0\), but A1 needs the comparative diagonal
bound
\[
  [z^n]\Delta_{T_n}\ge-[z^n](\mathcal L-\tfrac12\mathcal A).
\]
The cutoff derivative is
\[
  {d\over dT}[z^n]\Delta_T
  =
  -E(e^T)e^{-T}L_{n-1}^{(2)}(T),
\]
so any surplus-improvement theorem is again a signed
Chebyshev--Laguerre transfer theorem.

`242` gives the Loewner cone decomposition
\[
  \mathfrak Q^{\mathcal C,T}
  =
  \mathfrak Q^{\mathcal M}
  +
  \mathfrak Q^{\Delta,T}.
\]
On \(p_n=1-z^n\),
\[
  {1\over2}\mathfrak Q^{\mathcal C,T_n}(p_n,p_n)
  =
  M_n+\delta_n
  =
  C_n(T_n).
\]
Thus a one-dimensional Loewner check is just A1; a structural proof must
prove domination or Schur innovation on a larger space before reading the
diagonal.

`243` refines the same target by decomposing
\[
  \mathfrak Q^{\mathcal M}
  =
  \mathfrak Q^{\mathcal M}_+
  -
  \mathfrak Q^{\mathcal M}_-.
\]
It is enough to prove
\[
  \mathfrak Q^{\Delta,T_n}\succeq\mathfrak Q^{\mathcal M}_-
\]
on a finite comparison space containing \(1-z^n\).  On the one-dimensional
test this is exactly \(\delta_n\ge-M_n\).

`244_A0_TAIL_IMPROVEMENT_REQUIREMENT.md` normalizes the same target as the
exact improvement over A0.  With
\[
  \eta_n={1\over4}-{R_n(T_n)\over A_n},
  \qquad
  d_n=\max\left(0,{1\over2}-{\lambda_n\over A_n}\right),
\]
A0 is \(\eta_n\ge0\), while A1 is exactly
\[
  \eta_n\ge d_n.
\]
Equivalently, the signed tail must satisfy
\[
  \int_{T_n}^{\infty}
    E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du
  \ge
  \left(d_n-{1\over4}\right)A_n.
\]

`245` separates the terminal finite threshold from A1.  The terminal
asymptotic sign is closed after `217`, but a numerical \(N_0\) requires the
declared cutoff policy, cutoff-ratio bounds, \(B_{n-1}\) bounds, base
intervals, archimedean summand intervals, and a finite interval check for
\(\mathfrak D_n\ge0\).  This does not replace the signed compact theorem.

`246` separates the global half-plane route from compact A1.  The global
theorem
\[
  \Re{\xi'\over\xi}(s)\ge0\qquad(\Re s>1/2)
\]
would close Omega7 through RH/Li, but it gives only \(d_n\le1/2\) in the
deficit notation of `240`.  With A0 giving only \(s_n\ge0\), compact A1
still needs \(s_n\ge d_n\).

`247` isolates a sufficient special point of the ladder:
\[
  \lambda_n\ge {1\over4}A_n,\qquad R_n(T_n)\le0.
\]
This gives \(d_n\le1/4\) and \(s_n\ge1/4\), hence \(s_n\ge d_n\).  It is
still RH-strength and still requires a signed tail theorem.

`248` defines the quarter-margin generator
\[
  \mathcal Q_{1/4}=\mathcal L-{1\over4}\mathcal A.
\]
Coefficient positivity of \(\mathcal Q_{1/4}\) for \(n\ge8\) implies
\(\lambda_n\ge0\) for all \(n\) after the finite low-index certificate, so
it is already RH-strength by Li's criterion.

`249` writes the signed tail condition \(R_n(T_n)\le0\) as a Laguerre-zero
tail partition:
\[
  \sum_j\sigma_{n,j}\mathcal E_{n,j}\ge0.
\]
A0 gives only the weaker lower bound \(-A_n/4\), so this remains a genuine
one-sided lobe-compensation theorem.

`250` shows that this sign cannot be recovered from a symmetric envelope
\(|E(e^u)|\le W(u)\) alone: the tail functional is odd under
\(E\mapsto-E\), while the envelope data are unchanged.

`251` fixes the literal RDI-to-Li bridge.  It is enough to prove local
uniform convergence near \(z=0\) of RDI logarithmic derivatives to
\[
  {z\over(1-z)^2}{\xi'\over\xi}\!\left({1\over1-z}\right)
\]
with nonnegative approximating coefficients, because Cauchy's formula then
passes to each \(\lambda_n\).  Alternatively, locally uniform convergence
of real-rooted approximants to the true \(\Xi\) gives RH by Hurwitz.
The real-ray no-go in `310` shows why the convergence must be complex local
uniform convergence: \(F_N(z)=z/(1+N^2z^2)\) tends to \(0\) pointwise on the
real axis while its linear coefficient remains \(1\).

`252` records that zero comparative Schur coupling is degenerate: if
\(b_n=0\), then the Schur innovation equals \(2C_n(T_n)\).  Hence that
case is non-circular only when A1 has already been proved by another signed
mechanism.

`253` writes the global half-plane theorem as a disk Herglotz measure:
\[
  H_\xi(z)=2{\xi'\over\xi}\!\left({1\over1-z}\right)
  =
  \int_{\partial\mathbb D}{\zeta+z\over\zeta-z}\,d\nu_\xi(\zeta),
  \qquad \nu_\xi\ge0.
\]
If constructed non-circularly, this measure excludes interior poles and
therefore off-critical zeros, closing Omega7 through RH/Li.  It still does
not prove compact A1 unless paired with the margin-tail bridge.

`254` writes the signed tail through the explicit formula:
\[
  I_n(T)
  =
  -2\Re\sum_{\Im\rho>0}{\Phi_{n,T}(\rho)\over\rho}
  -\mathcal T_{n,T}.
\]
Thus the nonpositive-tail theorem is a one-sided phase theorem for the
zero sum, not a modulus estimate.

`255` introduces the correlation slack \(h_n\):
\[
  R_n(T_n)\le {1\over4}A_n-h_n.
\]
The sharp pointwise condition is \(h_n\ge(-M_n)_+\), equivalently
\(s_n\ge d_n\).

`256` records the exact dual-cone audit for this pointwise condition.  A
smoothed theorem of the form
\[
  \sum_{n\ge8}K_\alpha(n)C_n(T_n)\ge0
\]
does not close A1 unless every coordinate mass \(\delta_N\) belongs to the
positive cone generated by the kernels \(K_\alpha\), or unless an
independent coefficient-extraction theorem is supplied.  Thus Abel, Laplace,
Fejer, heat, and averaged positivity routes must carry a positive inverse;
bare positivity of a transform is not enough.

`257` specializes this pointwise obstruction to the tail--margin slack.
Averaged, density-one, cofinal, or purely asymptotic information about
\[
  h_n-(-M_n)_+
\]
does not imply compact A1 unless it is converted into the effective
pointwise inequality \(h_n\ge(-M_n)_+\), with finite exceptional indices
certified separately.

`258` gives the matching zero-side warning for the explicit-formula tail
phase: critical-line support fixes the location of the measure but does not
determine the sign of the oriented incomplete-Laguerre moment required for
\(R_n(T_n)\le0\) or \(s_n\ge d_n\).

`259` gives the sharpened Fejer/log-density closure theorem.  If the
positive increment measure \(\nu_g\) is constructed and
\[
  \int F_n\,d\nu_g
  \ge
  \left({1\over2}+\eta\right)\log n-O(1)
\]
for some \(\eta>0\), then the strong margin holds for all large \(n\), and
the remaining range is finite.  A lower logarithmic boundary density
coefficient \(a>1/2\) implies the displayed Fejer bound.  Thus this route is
now reduced to a positive increment measure plus a lower density theorem,
not merely Abel logarithmic growth.

## Theorem C: strong margin

Prove
\[
\boxed{
  \lambda_n\ge {1\over2}\lambda_n^{\rm arch}
  \qquad(n\ge8).
}
\tag{6}
\]

Equivalently,
\[
\boxed{
  [z^n]\left(\mathcal L(z)-{1\over2}\mathcal A(z)\right)\ge0
  \qquad(n\ge8).
}
\tag{7}
\]

Together with A0,
\[
  R_n(T_n)\le {1\over4}\lambda_n^{\rm arch},
\]
(6) implies (1).

Bare global Toeplitz/Schoenberg positivity gives only \(\lambda_n\ge0\),
not (6).

In increment-measure coordinates, Theorem C is equivalently the Fejer
margin
\[
\boxed{
  n\int_{\partial\mathbb D}F_n\,d\nu_g
  \ge
  \lambda_n^{\rm arch}
  \qquad(n\ge8),
}
\tag{8}
\]
provided the positive increment measure \(\nu_g\) has first been
constructed non-circularly.

The constant audit in `205` refines the logarithmic-density version of this
target.  Since
\[
  \lambda_n^{\rm arch}={1\over2}n\log n+O(n),
\]
it would be enough asymptotically to prove
\[
  \int F_n\,d\nu_g\ge {1\over2}\log n+O(1)
\]
with effective constants for \(n\ge8\).  A local density lower bound
\[
  {d\nu_g\over dm}(e^{i\theta})
  \ge
  a\log {e\over|\theta|}-O(1),
  \qquad a>{1\over2},
\]
would supply this leading margin.

However, `206` shows that the Abel logarithm of
\(\mathcal G_+(r)\) does not imply the Fejer lower bound by itself: Fejer
kernels have moving zeros.  Theorem C therefore requires either a direct
Fejer lower bound, a lower log-density theorem, or an anti-concentration
theorem excluding mass hiding near those moving zeros.
The conditional theorem in `259` makes this effective: a positive increment
measure and an explicit bound
\[
  \int F_n\,d\nu_g
  \ge
  \left({1\over2}+\eta\right)\log n-B_F
\]
give strong margin for
\[
  n\ge
  \max\left(N_A,N_F,
  \left\lceil\exp\left({B_A+B_F\over\eta}\right)\right\rceil\right),
\]
with only a finite interval left.  Thus Theorem C is now reduced to
constructing \(\nu_g\) and proving that explicit Fejer/log-density lower
bound.
The analytic Fejer/log constant in this reduction is closed in `260`:
\[
  \int_{\partial\mathbb D}F_nL\,dm
  =
  H_{n-1}-{n-1\over n}
  \ge
  \log n-1.
\]
Thus a lower density \(h(\theta)\ge aL(\theta)-B_h\), \(a>1/2\), supplies
the constants \(B_F=a+B_h\) and \(\eta=a-1/2\).
The archimedean upper input is fixed in `262`:
\[
  A_n=\lambda_n^{arch}\le {1\over2}n\log n+3n
  \qquad(n\ge2),
\]
so \(B_A=3\) and \(N_A=2\) are available for the effective threshold.
If that lower density is proved only on a local arc
\(|\theta|\le\theta_0\), `263` gives the required global Fejer bound after
replacing \(B_h\) by
\[
  B_h^\ast=
  \max\{B_h,\ a(-\log(2\sin(\theta_0/2)))_+\}.
\]
So the real open input is local logarithmic density with coefficient
\(a>1/2\), together with a globally positive measure decomposition.
The resulting threshold is recorded in `264`:
\[
  N_\infty=
  \max\left(
    2,
    \left\lceil
    \exp\left({3+a+B_h^\ast\over a-1/2}\right)
    \right\rceil
  \right).
\]
Above \(N_\infty\), strong margin plus A0 gives A1; below it the task is a
finite interval certificate.
The exact finite certificate is recorded in `261`: for every
\(8\le n<N_\infty\), either rigorous intervals must prove
\[
  \lambda_n^- - {1\over2}A_n^+\ge0,
\]
or a direct compact-A1 interval must prove
\[
  C_n(T_n)^-\ge0.
\]
This is a pointwise finite check, not an averaged substitute.
The coefficient budget in `265` gives the matching upper restriction:
because
\[
  \mathcal G_+(r)
  =
  {1\over2}\log {1\over1-r}+O(1),
\]
any positive logarithmic lower density \(h\ge aL-B_h\) must have
\[
  a\le1.
\]
Thus the Fejer density theorem, if true, must land in the exact window
\[
  {1\over2}<a\le1.
\]
The alternative Abel-transfer route is isolated in `266`.  For
\[
  D_{n,\alpha}=(P_{1-1/n}-\alpha F_n)_+,
\]
one has
\[
  \int F_n\,d\nu_g
  \ge
  {1\over\alpha}
  \left(
    \int P_{1-1/n}\,d\nu_g-\int D_{n,\alpha}\,d\nu_g
  \right).
\]
Since \(\int P_{1-1/n}\,d\nu_g=\log n+O(1)\) in the Euler--Gamma
normalization, Abel transfer closes the Fejer margin only if the defect
has logarithmic coefficient \(d\) satisfying
\[
  {1-d\over\alpha}>{1\over2}.
\]
For \(\alpha=1\), this is \(d<1/2\), an anti-concentration theorem near the
moving Fejer zeros.
The constant-threshold ledger in `291` makes this explicit for arbitrary
\(0<\alpha<2\).  If
\[
  \int(P_{1-1/n}-\alpha F_n)_+\,d\nu_g
  \le d_\alpha\log n+B_D,
  \qquad d_\alpha<1-\alpha/2,
\]
and the Abel lower bound is effective, then
\[
  q_\alpha={1-d_\alpha\over\alpha}>{1\over2}
\]
and strong margin holds for all
\[
  n\ge
  N_\infty(\alpha)=
  \max\left(N_0,2,\left\lceil
  \exp\left({3+B_\alpha\over q_\alpha-1/2}\right)\right\rceil\right).
\]
Below this threshold, the exact remaining task is the finite certificate
of `261`.
The geometric version in `292` defines
\[
  B_{n,\tau}=\{F_n<\tau P_{1-1/n}\}
\]
and proves
\[
  D_{n,\alpha}
  \le
  P_n{\bf1}_{B_{n,\tau}}
  +(1-\alpha\tau)_+P_n{\bf1}_{B_{n,\tau}^c}.
\]
Thus the defect theorem follows from a Poisson-weighted bad-set estimate
\[
  \int_{B_{n,\tau}}P_n\,d\nu_g\le b_\tau\log n+B_B
\]
with
\[
  b_\tau+(1-\alpha\tau)_+<1-\alpha/2.
\]
This is the current most local anti-concentration form of the Abel route.
`293_FEJER_POISSON_BAD_SET_GEOMETRY_GATE.md` shows that \(B_{n,\tau}\)
contains windows of
radius \(\sqrt{\tau}/(2n)\) around every nontrivial \(n\)-th root of unity.
Therefore this bound is not a formal small-set estimate; it must be an
arithmetic anti-concentration theorem for the actual increment measure.
The sufficient local-window version is
`311_BAD_SET_CARLESON_WINDOW_SUFFICIENT_CONDITION.md`: if the actual
measure obeys
\[
  \nu_g(I_{n,k}(\tau))\le { \rho_\tau\log n+B_\tau\over n}
\]
on all \(1/n\)-scale root windows and
\[
  C_\tau'\rho_\tau<1-{1\over2\tau}
  \qquad(\tau>1/2),
\]
then the bad-set estimate of `292` follows and the Abel threshold of `291`
becomes effective.  Thus this subroute is reduced to a concrete
Carleson-window anti-concentration theorem for \(\nu_g\).
`296_WEIGHTED_CARLESON_BAD_SET_GATE.md` gives the sharper weighted version:
it is enough to prove
\[
  \sum_{k=0}^{n-1}{n\,\nu_g(I_{n,k}(\tau))\over1+\kappa(k)^2}
  \le \beta_\tau\log n+B_\tau,
\]
with \(C_\tau\beta_\tau<1-1/(2\tau)\).  This matches the Poisson weight and
does not over-control windows far from \(1\).
`297_CENTRAL_FLOOR_WEIGHTED_BUDGET_GATE.md` adds the corresponding
compatibility budget.  If the local log-density coefficient is \(a\), a
viable weighted proof at \(\tau\) must fit
\[
  aK(\tau)\le C_\tau\beta_\tau<1-{1\over2\tau}.
\]
Thus some of the bad-set allowance is already consumed by the central
window before nontrivial-root concentration is considered.
`316_CENTRAL_FLOOR_COMPATIBILITY_WINDOW.md` checks that this budget is not
vacuous in the live range \(a\le1\): at \(\tau=3/2\),
\[
  K(3/2)<{2\over3}
  =
  1-{1\over2(3/2)},
\]
so \(aK(3/2)\) stays strictly below the optimized target for every
\(a\le1\).
Thus the central floor narrows but does not by itself close or refute the
Abel-defect route.
`314_BAD_SET_CENTRAL_WINDOW_LOG_MASS_FLOOR.md` adds the matching necessary
budget at the central window: because \(F_n(1)/P_{1-1/n}(1)\to1/2\), every
usable \(\tau>1/2\) puts a \(1/n\)-scale neighborhood of \(1\) inside
\(B_{n,\tau}\).  If \(h\ge aL-B\) locally, this forces a lower coefficient
\[
  b_\tau\ge a\,{2\over\pi}\arctan c_\tau
\]
for any central scale \(c_\tau\) with the scaling ratio below \(\tau\).
`294_LOCAL_DENSITY_NOT_BAD_SET_ANTI_CONCENTRATION_NO_GO.md` shows that the
local-density route does not supply this theorem: a positive measure can
retain a local logarithmic lower density near \(1\) while sparse atoms at
moving Fejer zeros force arbitrarily large Poisson-weighted bad-set mass.
`295_BOUNDED_DENSITY_BAD_SET_ZERO_COEFFICIENT_GATE.md` records the harmless
case: if \(d\nu=h\,dm\) with \(0\le h\le H\), then
\[
  \int_{B_{n,\tau}}P_{1-1/n}\,d\nu\le H,
\]
so bounded density contributes no logarithmic bad-set coefficient.  The
remaining Abel-defect obstruction is therefore in the singular or
unbounded-density part of the actual increment measure.
The model calibration in `312_LOG_KERNEL_ABEL_DEFECT_MODEL_LEDGER.md`
shows that the canonical log-density itself has an explicit defect
constant:
\[
  \int(P_{1-1/n}-\alpha F_n)_+L\,dm
  =
  \kappa_\alpha\log n+o_\alpha(\log n).
\]
Thus the live Abel route is narrowed to controlling the non-log-kernel
Euler--Gamma remnant; the log-density model is computable, but not a proof
for the actual measure.

`315_LOG_KERNEL_DEFECT_OPTIMIZATION_LEDGER.md` optimizes this model
comparison against the threshold \(1-\alpha/2\).  The pure log-kernel model
has positive leading margin; for example at \(\alpha=3/4\),
\[
  \kappa_\alpha\approx0.3520355633,\qquad
  1-\alpha/2-\kappa_\alpha\approx0.2729644367.
\]
Thus the Abel-to-Fejer route remains numerically viable after the canonical
logarithmic component is removed; the live input is a remnant bad-set
estimate.

`325_EG_REMAINDER_BAD_SET_CERTIFICATE_SCHEMA.md` turns that live input into
an effective certificate.  If
\[
  d\nu_g=aL\,dm+d\rho,
\]
then the route closes once the log-kernel defect is certified with
coefficient \(\kappa_\alpha^+\), the remnant satisfies either a direct
defect estimate or a weighted bad-set estimate with coefficient
\(e_\alpha\), and
\[
  a\kappa_\alpha^+ + e_\alpha<1-\alpha/2.
\]
At that point `291` supplies the explicit strong-margin threshold and
`261` supplies the finite remainder.

`328_POISSON_LOWER_NOT_LOG_DOMINATION_NO_GO.md` shows that the Abel lower
bound does not imply the log-kernel decomposition.  The model
\(\nu=\delta_1\) has
\[
  \int P_{1-1/n}\,d\nu=2n-1\ge\log n,
\]
but cannot satisfy \(\nu\ge aL\,dm\) for any \(a>0\), because arcs away
from \(1\) with \(L>0\) have zero \(\nu\)-mass.  Thus the Fejer route needs
a separate domination theorem for \(\nu_g\), or a direct defect estimate
for the full measure.

`324_FINITE_TOEPLITZ_BLOCKS_NOT_HERGLOTZ_GATE.md` records the matching
global-route finite-check obstruction.  For each fixed \(N\), all Toeplitz
blocks \(T_L\), \(L\le N\), can be positive while \(T_{N+1}\) is
indefinite, by placing one large Hermitian mode at \(\pm(N+1)\).  Thus a
Herglotz/RDI closure needs infinite Toeplitz positivity, a positive
boundary measure, or a limiting theorem with actual coefficient
convergence; finite Toeplitz evidence does not prove Omega7 or compact A1.

`313_DIRECT_A1_TERMWISE_SIGN_OBSTRUCTION.md` records the corresponding
direct-route audit.  In the high prime-power block the coefficients are
\[
  \Omega_n(m)
  =
  e^{-T_n}L_{n-1}^{(1)}(T_n)
  -
  e^{-\log m}L_{n-1}^{(1)}(\log m).
\]
Since \(e^{-u}L_{n-1}^{(1)}(u)\) has alternating Laguerre lobes, these
coefficients are not of one sign.  Therefore direct A1 cannot be closed by
termwise positivity of prime powers; it needs signed global compensation.
`298_LAGUERRE_LOBE_BLOCK_COMPENSATION_GATE.md` gives the minimal block
form of that compensation.  Partitioning the high block by the sign of
\(G_{n-1}(T_n)-G_{n-1}(u)\), the direct certificate becomes
\[
  H_n^+-H_n^-+B_n^{\rm base}\ge0.
\]
Thus any direct proof must prove oriented lobe dominance; bounding
\(H_n^++H_n^-\) is not enough.

`299_LOBE_BLOCK_PARTIAL_SUMMATION_GATE.md` rewrites the same lobe blocks
by exact partial summation.  Each block becomes an explicit main term plus
a signed Chebyshev-error integral, and the direct route is equivalent to
an oriented discrepancy inequality over those lobes.

`329_DIRECT_A1_ORIENTED_CHEBYSHEV_MINIMAL_THEOREM.md` states that
equivalent direct theorem in its terminal form:
\[
  \sum_jH_{n,j}^{\rm err}
  \ge
  -B_n^{\rm base}-\sum_jH_{n,j}^{\rm main}.
\]
It also rules out the naive monotonicity proof.  A nonnegative increasing
prime-power measure can still put mass in negative Laguerre lobes, so
positivity of \(\Lambda\) and monotonicity of \(\psi\) do not imply the
oriented inequality.

`320_TAIL_LOBE_ONE_SIDED_ENVELOPE_CRITERION.md` gives the corresponding
tail-side sufficient form.  Lower envelopes for
\(E(e^u)=\psi(e^u)-e^u\) on positive lobes of
\(K_n=e^{-u}L_{n-1}^{(2)}\), together with upper envelopes on negative
lobes, imply compact A1 at \(n\) once their oriented lower bound satisfies
\[
  \mathcal L_n\ge\left(d_n-\frac14\right)A_n.
\]
This is the constructive version of the symmetric-envelope no-go: useful
tail envelopes must be one-sided and matched to the Laguerre signs.

`322_TAIL_LOBE_INTERVAL_CERTIFICATE_SCHEMA.md` makes this criterion
auditable.  A pointwise certificate must isolate all tail zeros of
\(L_{n-1}^{(2)}\), enclose the positive lobe weights, prove the oriented
one-sided bounds for \(E(e^u)\), and compare the resulting rigorous lower
bound against \((d_n-1/4)A_n\).  By the finite/cofinal no-goes, this closes
all A1 only if it covers every \(n\ge8\), or if it is paired with an
effective threshold and complete finite remainder.

`326_TAIL_LOBE_STEP_ENVELOPE_EFFECTIVE_REDUCTION.md` makes the bounded-lobe
part finite.  Since \(\psi(e^u)-e^u\) decreases between prime-power
logarithms and jumps upward by \(\Lambda(m)\), the exact lower and upper
constant envelopes on a bounded lobe are obtained by checking only the
right endpoints before jumps, the left endpoints after jumps, and the lobe
endpoints.  Thus bounded lobes are finite arithmetic data; the remaining
tail input is the final-ray one-sided weighted theorem and the usual
all-index or effective-threshold coverage.

`327_FINAL_RAY_ABSOLUTE_COST_GATE.md` gives a valid way to handle that last
ray by an ordinary two-sided PNT/VK envelope, but only as an explicit
negative cost after the bounded lobes have been certified arithmetically:
\[
  \mathcal R_{n,\infty}(W)=
  \int_{\xi_{n,*}}^\infty W(u)e^{-u}|L_{n-1}^{(2)}(u)|\,du.
\]
The pointwise certificate then requires bounded-lobe surplus minus this
cost to dominate \((d_n-1/4)A_n\).

`321_DIRECT_TAIL_LOBE_TRANSFER_GATE.md` prevents a circular shortcut between
these two lobe languages.  The identity
\[
  {d\over du}\bigl(G_{n-1}(T_n)-G_{n-1}(u)\bigr)
  =
  e^{-u}L_{n-1}^{(2)}(u)
\]
links the compact direct carrier to the tail carrier algebraically, but not
positively.  Direct lobe dominance and tail lobe dominance are equivalent
only after the full compact identity is used; that equivalence cannot itself
prove A1.

The positive-inverse no-go in `270` shows that Abel or Poisson lower bounds
do not themselves provide the required Fejer lower theorem.  Any positive
combination of radial Poisson kernels is strictly positive at the
nontrivial \(N\)-th roots of unity, while \(F_N\) vanishes there.  Therefore
Theorem C must include a direct Fejer lower bound, a local density theorem,
or anti-concentration against the moving zero set of \(F_N\).
The explicit spike model in `281` sharpens this point: a finite positive
measure can satisfy
\[
  \int P_{1-1/N_j}\,d\nu\gg\log N_j
\]
on a cofinal sequence while
\[
  \int F_{N_j}\,d\nu=O(1),
\]
by placing mass \((\log N_j)/N_j\) at the nontrivial \(N_j\)-th root where
\(F_{N_j}\) vanishes.  Thus radial \(\mathcal G_+\)-scale information does
not imply Fejer margin or local absolutely continuous log-density.
The necessary localization form is `272`: using
\[
  F_n(e^{i\theta})\le \min\left(n,{\pi^2\over n\theta^2}\right),
\]
any Fejer lower bound of order \(\log n\) forces logarithmic localized mass
near \(\zeta=1\).  The unified distribution form is `273`:
\[
  \int F_n\,d\nu_g
  =
  \int_0^n\nu_g\{F_n\ge t\}\,dt.
\]
Thus Theorem C is equivalent to proving
\[
  \int_0^n\nu_g\{F_n\ge t\}\,dt\ge {A_n\over n}
  \qquad(n\ge8),
\]
or proving this eventually plus the finite certificate of `261`.

The finite-certificate qualification is made explicit in `277`: the
certificates of `148`, `190`, `230`, and the finite Fejer remainder `261`
are pointwise arithmetic proofs only after an effective infinite-range input
is available.  To close all \(n\ge8\), one must either prove the relevant
certificate uniformly for every \(n\), or prove an explicit threshold
\(N_\infty\) and then verify every remaining \(8\le n<N_\infty\) with
outward-rounded finite arithmetic.

The subsequential variant is excluded in `278`: a cofinal or density-one
family of certified indices is still not A1 unless every omitted coordinate
is reached by propagation, positive reconstruction, or the same
effective-threshold plus finite-remainder mechanism.

## Theorem D: one-sided tail

Prove
\[
\boxed{
  R_n(T_n)
  \le
  \lambda_n-{1\over4}\lambda_n^{\rm arch}
  \qquad(n\ge8).
}
\tag{9}
\]

By (1), this is exactly A1 in tail coordinates.  A useful strengthening is
the tail--margin correlation of `255`, written with a separate slack
\(h_n\):
\[
  R_n(T_n)
  \le
  {1\over4}\lambda_n^{\rm arch}-h_n,
  \qquad
  h_n\ge
  \left({1\over2}\lambda_n^{\rm arch}-\lambda_n\right)_+
\tag{10}
\]
whenever the strong margin is not already known.

Global Li positivity and the A0 absolute tail bound do not imply (9).

In zero coordinates, `254` rewrites the signed tail as
\[
  I_n(T_n)
  =
  -2\Re\sum_{\Im\rho>0}
    {\Phi_{n,T_n}(\rho)\over\rho}
  -\mathcal T_{n,T_n}.
\]
Thus the one-sided tail theorem is equivalently a one-sided phase
inequality for the explicit-formula zero sum, not a modulus estimate.
The separation in `258` adds that even critical-line support of the zero
measure is not enough proof data for this phase inequality: it fixes the
domain of the ordinates, but the compact tail theorem is an oriented
weighted moment bound against
\[
  \Re\left({\Phi_{n,T_n}(1/2+i\gamma)\over1/2+i\gamma}\right).
\]
Thus any closure through zero support must add this one-sided moment theorem
or return through a global RH/Li route outside the compact A1 budget.
The lobe/phase duality in `274` shows that this is the same obligation as
the signed Laguerre-lobe inequality of `249`: if
\[
  \Phi_{n,T}(\rho)=\sum_j\sigma_{n,j}\Phi_{n,j}(\rho),
\]
then summing the lobe explicit formula gives the zero-phase inequality.
Therefore a tail proof must provide signed lobe correlation or signed
zero-phase control; unsigned lobe bounds and zero-modulus estimates do not
combine into Theorem D.
The positive/negative phase-lobe balance in `280` makes the remaining
signed theorem explicit.  If
\[
  q_{n,T}(\gamma)=
  \Re\left({\Phi_{n,T}(1/2+i\gamma)\over1/2+i\gamma}\right)
  =
  q^+_{n,T}(\gamma)-q^-_{n,T}(\gamma),
\]
and \(P^\pm_{n,T}=\int q^\pm_{n,T}\,d\mu_\zeta\), then
\[
  I_n(T)=2(P^-_{n,T}-P^+_{n,T})-\mathcal T_{n,T}.
\]
Thus the full tail route needs
\[
  P^-_{n,T_n}-P^+_{n,T_n}
  \ge
  {1\over2}\left(
    \mathcal T_{n,T_n}+\left(d_n-{1\over4}\right)A_n
  \right).
\]

## Theorem E: comparative Loewner--Schur order

Construct the completed forms
\[
  \mathfrak Q^{\mathcal L},\qquad
  \mathfrak Q^{\mathcal A},\qquad
  \mathfrak Q^{\mathcal R,T}
\]
with the normalizations of `195`, and prove
\[
\boxed{
  \left(
  \mathfrak Q^{\mathcal L}
  -
  {1\over4}\mathfrak Q^{\mathcal A}
  -
  \mathfrak Q^{\mathcal R,T_n}
  \right)(1-z^n,1-z^n)
  \ge0
  \qquad(n\ge8).
}
\tag{11}
\]

A stronger version is positivity of the same comparative form on a finite
subspace containing \(1-z^n\).

This theorem is not implied by
\[
  \mathfrak Q^{\mathcal L}\succeq0.
\]
It is a genuine order comparison against the archimedean quarter and the
moving tail form.
The cofinality audit in `276` adds that any finite-subspace Loewner proof
must test the actual A1 direction \(p_n=1-z^n\), or positively reconstruct
\(p_np_n^*\) from the tested rank-one forms.  Positivity on unrelated
subspaces or dense-looking families does not imply the diagonal
\(\mathfrak Q^{\mathcal C,T_n}(p_n,p_n)\ge0\).

## Global route

A separate route is to prove the global half-plane theorem
\[
\boxed{
  \Re{\xi'\over\xi}(s)\ge0
  \qquad(\Re s>1/2).
}
\tag{12}
\]

By `175`, this is equivalent to RH and therefore closes Omega7 through Li.
But by `181`, `189`, and `192`, it does not by itself close the internal
compact A1 budget unless accompanied by Theorem C, D, E, or a direct proof
of Theorem A.

The Herglotz version in `253` gives the exact non-circular global target:
construct a positive boundary measure for
\[
  H_\xi(z)=2{\xi'\over\xi}\!\left({1\over1-z}\right)
\]
before using zero support.  Defining the measure from critical-line zeros
would be circular.
The radial Abel no-go in `290` adds that positivity or logarithmic growth
of \(H_\xi(r)\) on \(0<r<1\) is not enough: a Herglotz proof must control
\(\Re H_\xi(re^{i\theta})\) for all angles, equivalently every Toeplitz
block of \(g_m\).
The centered Fejer no-go in `300` adds the diagonal analogue: positivity of
all centered Fejer/Li sums does not imply Toeplitz positivity.  Full
translated Fejer or Carathéodory positivity is still the required global
measure theorem.
The completion criterion in `275` fixes the project-level logic: any
non-circular proof of the global half-plane/Herglotz/RDI route closes
Omega7 externally, but it does not satisfy the explicit compact A1
deliverable unless it is supplemented by \(C_n(T_n)\ge0\), \(s_n\ge d_n\),
or one of the equivalent compact routes listed above.  Conversely, proving
compact A1 closes Omega7 through the existing phase assembly.

## Insufficient routes already isolated

The following data do not close A1 by themselves:

1. A0 absolute tail control without a one-sided sign;
2. global Li positivity \(\lambda_n\ge0\) without margin;
3. Toeplitz/Schoenberg positivity without the archimedean diagonal margin;
4. two-sided PNT envelopes without the \(L^1\) domination (4);
5. diagonal cumulative weights \(w_{n,k}>0\) without sign control of
   \(\mathcal H_n\);
6. integrating by parts in the diagonal balance while omitting cutoff jumps;
7. formal Schur complements without proving positivity of the comparative
   form first;
8. zero-coupling Schur blocks, since `252` shows their innovation is just
   \(2C_n(T_n)\);
9. symmetric envelopes for \(E(e^u)\), since `250` shows the tail
   functional is odd under \(E\mapsto-E\);
10. smoothed positivity or averaged transforms without positive
    reconstruction of coordinate masses, since `256` shows A1 is a
    pointwise dual-cone condition;
11. averaged, cofinal, density-one, or purely asymptotic slack bounds
    without pointwise conversion, since `257` shows they do not imply
    \(h_n\ge(-M_n)_+\) at every index.
12. radial Abel/\(\mathcal G_+\)-scale spikes without Fejer
    anti-concentration, since `281` gives a positive finite measure with
    logarithmic Poisson spikes but bounded matching Fejer tests.
13. Abel defect bounds with the wrong leading constant: by `291`, in the
    natural Euler--Gamma normalization the defect coefficient must satisfy
    \(d_\alpha<1-\alpha/2\).  A weaker bound leaves the Fejer coefficient
    \(\le1/2\), so it cannot beat the archimedean margin.

## Status

Closed as the canonical theorem list after the `187`--`195` reductions.

A1 remains open.  Omega7 remains open inside this phase until at least one
of Theorems A--E, or the global theorem (12), is proved non-circularly.
