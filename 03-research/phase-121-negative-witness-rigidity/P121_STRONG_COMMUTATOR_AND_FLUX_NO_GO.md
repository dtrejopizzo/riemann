# P121 -- strong radical commutation and the flux-only no-go

## Status

This note closes the common-product-domain part of the qualification left
in v94 (451)--(453), for a hypothetical finite-window first-loss state.  The
sub-half-Sobolev theorem of `P121_DYADIC_RADICAL_BOOTSTRAP.md` puts that
state in a common strong domain on which the zeta observation and the
Gamma logarithmic generator commute as ordinary closed multipliers.

The result is an exact conservation law.  It does **not** prove annular
vanishing.  In fact Section 4 proves an abstract obstruction: conservation,
the Real involution and two Tate functionals alone cannot annihilate a
boundary flux.  Therefore the missing global-square theorem cannot be a
formal consequence of those three ingredients; it must use an additional
Euler-specific rigidity law for the equality state.

## 1. Operators

Let `u=E_T F` be the zero extension of a finite-window first-loss state and
write

\[
 d_\Gamma(\tau)
 =\operatorname {Re}\psi\left(\frac14+\frac{i\tau}{2}\right)
   -\log\pi .                                             \tag{1.1}
\]

Let

\[
 D_\Gamma=d_\Gamma(D),\qquad
 (\mathfrak Z u)^\wedge(\tau)
 =\zeta(\tfrac12+i\tau)\widehat u(\tau) .                 \tag{1.2}
\]

Here `mathfrak Z` is the maximal closed co-Poisson observation of v94
(431)--(432).  Since

\[
 |d_\Gamma(\tau)|\ll \log(2+|\tau|),                      \tag{1.3}
\]

the natural common product domain is

\[
 \mathcal D_{\mathfrak Z\Gamma}
 :=\left\{v:\
  \zeta(\tfrac12+i\tau)d_\Gamma(\tau)\widehat v(\tau)
  \in L^2(d\tau)\right\}.                                \tag{1.4}
\]

## 2. Strong commutation on a radical

### Theorem 2.1 -- common-domain theorem

Every finite-window first-loss state satisfies

\[
 u\in\operatorname {Dom}(\mathfrak ZD_\Gamma)
       \cap\operatorname {Dom}(D_\Gamma\mathfrak Z)       \tag{2.1}
\]

and

\[
 \boxed{
 \mathfrak ZD_\Gamma u=D_\Gamma\mathfrak Zu,
 \qquad [\mathfrak Z,D_\Gamma]u=0
 \quad\hbox{in }L^2(\mathbb R).}                          \tag{2.2}
\]

#### Proof

The dyadic radical bootstrap gives

\[
 u\in H^s(\mathbb R)\qquad(0<s<1/2).                      \tag{2.3}
\]

Choose numbers

\[
 \frac14<\frac14+\eta+\delta<s<\frac12 .                 \tag{2.4}
\]

Uniform convexity on the fixed pole-free strip gives

\[
 |\zeta(\tfrac12+i\tau)|
 \ll_\eta(1+|\tau|)^{1/4+\eta}.                          \tag{2.5}
\]

Equations (1.3)--(2.5) imply

\[
 |\zeta(\tfrac12+i\tau)d_\Gamma(\tau)|^2
 \ll (1+\tau^2)^s .                                      \tag{2.6}
\]

After multiplication by `|uhat|^2` and integration, (2.6) proves (2.1).
Both compositions in (2.1) are Fourier multiplication by the same
measurable function

\[
 \zeta(\tfrac12+i\tau)d_\Gamma(\tau),                    \tag{2.7}
\]

which proves (2.2).  QED.

### Corollary 2.2 -- closure of the strong common-domain qualification

The meromorphic identity v94 (447)

\[
 \mathfrak Z\mathcal A_\infty=[\mathfrak Z,D_\Gamma]      \tag{2.8}
\]

has, on a first-loss radical, the canonical strong right-hand side zero.
Consequently the `L2` causal boundary obtained as a graph limit of the
smooth primitive-core calculus is uniquely fixed and equals zero.

#### Proof

Take a sequence of smooth compactly supported primitive vectors converging
to `u` in `H^s`, with `s` as in (2.4).  The two Tate moment corrections are
finite rank and preserve this convergence.  Estimate (2.6) gives graph
convergence for both compositions in (2.2).  Their commutators vanish on
the approximants and hence on `u`.  Closedness proves uniqueness.  QED.

This corollary does not assign separate `L2` meanings to the divergent
global prime orientations.  It assigns a meaning to their completed joint
boundary through (2.8), which is the only combination occurring in v94.

## 3. Exact value of the incoming boundary

Let `r_epsilon` be the appropriate Tate forcing in v94 (445), and let

\[
 h=\mathcal Z_{T,+}F .                                  \tag{3.1}
\]

At the level of the common closed graph, the physical-window/incoming split
is now defined canonically in
`P121_GRAPH_RENORMALIZED_INCOMING_CURRENT.md`.  Corollary 2.2 turns its
completed boundary into

\[
 \boxed{
 \mathcal L_{T,-}(F)=-\mathcal Z_{T,+}r_\varepsilon .}   \tag{3.2}
\]

Thus the completed incoming history is neither missing nor free.  It is
fixed exactly by the two-dimensional Tate forcing.  In particular it
generally does not vanish.  This statement concerns the unique closed-graph
boundary; convergence of the individually divergent literal series (452)
is neither asserted nor needed to define it.

Equation (3.2) is a conservation equation, not annular transport.  It
contains no implication `h=0`: the amplitude `h` still has to satisfy the
observed Gamma--Tate equation v94 (445).  Substituting (3.2) back into the
global commutator only recovers `0=0`.

## 4. Conservation, Real and Tate do not kill a flux

The following elementary statement records the precise logical limit of
the preceding mechanism.

### Proposition 4.1 -- two-border flux no-go

Let `K` be an infinite-dimensional real Hilbert space, let `R` be an
orthogonal involution whose two eigenspaces are infinite dimensional, and
let `M_+`, `M_-` be two continuous linear functionals.  For either
`epsilon in {+1,-1}` there are nonzero pairs `(j_+,j_-)` satisfying

\[
 j_++j_-=0,\qquad j_-=\varepsilon Rj_+,
 \qquad M_\pm(j_+)=0 .                                  \tag{4.1}
\]

#### Proof

Choose

\[
 0\ne j_+\in\ker M_+\cap\ker M_-\cap
             \ker(R+\varepsilon I).                       \tag{4.2}
\]

The last space is infinite dimensional and intersection with two
hyperplanes is still nonzero.  Put `j_-=-j_+`.  Since
`Rj_+=-epsilon j_+`, all identities (4.1) follow.  QED.

The proposition is not a counterexample to the literal zeta equation.  It
is a type theorem: no proof which uses only

1. cancellation of the two boundary currents,
2. Real parity, and
3. the two Tate moments

can deduce that either current is zero.  Such a proof would also prove the
false abstract implication refuted by (4.1).

## 5. Consequence for the global-square programme

The map is now

\[
\begin{array}{c}
\text{sub-half Sobolev radical}\\
\Downarrow\\
\text{strong zeta--Gamma common domain}\\
\Downarrow\\
\text{exact two-border conservation (3.2)}\\
\Downarrow\quad\textbf{OPEN}\quad\\
\text{Euler-specific equality-state rigidity}\\
\Downarrow\\
h=0\Longrightarrow F=0.
\end{array}                                             \tag{5.1}
\]

The open arrow may not be filled by another conservation identity, a
parity argument, two moment equations, or a positive completion of the
boundary block.  It must use information not present in Proposition 4.1.
In the present coordinates that information can only be a genuinely
Euler-specific law on the solution of (445), beyond its scalar logarithmic
derivative.

## 6. Corpus comparison

The nearest earlier statements are v94 (447)--(453), where the physical
boundary was marked `AUDIT`, and D.240, where the dual Euler conservation
law was proved but its localized defect remained open.  The new theorem is
the common `L2` product-domain closure for an actual first-loss radical,
made possible by the phase-121 sub-half-Sobolev bootstrap.  The explicit
flux-only no-go (4.1) and the corrected map (5.1) do not occur in those
documents.

The global square and row (d) remain open.
