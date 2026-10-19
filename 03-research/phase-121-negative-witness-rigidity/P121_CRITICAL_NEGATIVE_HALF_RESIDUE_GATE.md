# P121 -- the critical negative-half residue gate

## Status

This note computes the sharp local `H^(-1/2)` trace of the one-sided
meromorphic current.  A nonzero Cauchy residue is exactly logarithmically
divergent at that Sobolev index.  Consequently a sub-logarithmic critical
bound annihilates every critical-line residue and, by Cartwright
overdetermination, every compact-window source.

The theorem is unconditional and does not use row (d).  The audit in
Section 4 is essential: although this condition is a half derivative weaker
than the `H2`/`L2` tail condition as a function-space assertion, on the
specific meromorphic family it is **equivalent** to cancellation of the
critical residue.  It is therefore an exact detector, not an independent
intermediate estimate supplied by the equality equation.

## 1. Local model

Use the Fourier convention

\[
 \widehat f(\xi)=\int_{\mathbb R}f(x)e^{-ix\xi}\,dx,
 \qquad
 \|f\|_{H^{-1/2}}^2
 ={1\over2\pi}\int_{\mathbb R}
 (1+\xi^2)^{-1/2}|\widehat f(\xi)|^2\,d\xi.        \tag{1.1}
\]

Let `chi in C_c^infinity(R)` equal one on a neighbourhood of zero and put

\[
 c_\sigma(x)={\chi(x)\over \sigma+ix},
 \qquad 0<\sigma<1.                                \tag{1.2}
\]

### Lemma 1.1 -- critical Cauchy growth

There are constants `0<a_chi<=b_chi<infinity` such that

\[
 a_\chi\log {1\over\sigma}-b_\chi
 \le \|c_\sigma\|_{H^{-1/2}}^2
 \le b_\chi\log {1\over\sigma}+b_\chi            \tag{1.3}
\]

for all sufficiently small `sigma`.

#### Proof

Put `f_sigma(x)=1/(sigma+ix)`.  Without the cutoff,

\[
 {1\over\sigma+ix}=\int_0^\infty e^{-\sigma t}e^{-ixt}\,dt,
\]

and therefore

\[
 \widehat f_\sigma(\xi)
 =2\pi e^{\sigma\xi}\mathbf1_{(-\infty,0)}(\xi).    \tag{1.4}
\]

It follows directly that

\[
 \|f_\sigma\|_{H^{-1/2}}^2
 =2\pi\int_0^\infty
 {e^{-2\sigma t}\over\sqrt{1+t^2}}\,dt
 =2\pi\log {1\over\sigma}+O(1).                    \tag{1.5}
\]

Now write

\[
 c_\sigma=f_\sigma-g_\sigma,
 \qquad g_\sigma=(1-\chi)f_\sigma.                 \tag{1.6}
\]

The factor `1-chi` removes a fixed neighbourhood of the only singularity.
Consequently `g_sigma` is uniformly bounded in `L2(R)` for
`0<sigma<1`: on the fixed deleted neighbourhood its denominator is bounded
away from zero, while at infinity it is `O(1/|x|)`.  Hence

\[
 \sup_{0<\sigma<1}\|g_\sigma\|_{H^{-1/2}}
 \le \sup_{0<\sigma<1}\|g_\sigma\|_2<\infty.       \tag{1.7}
\]

The triangle and reverse-triangle inequalities applied to (1.5)--(1.7)
give constants `A,B>0` such that

\[
 A\sqrt{\log(1/\sigma)}-B
 \le\|c_\sigma\|_{H^{-1/2}}
 \le A^{-1}\sqrt{\log(1/\sigma)}+B.                \tag{1.8}
\]

Squaring and changing the constants gives (1.3).  Equivalently, the
force-bearing frequency range is

\[
 \int_1^{1/\sigma}{d\xi\over\xi}
 =\log {1\over\sigma}.                              \tag{1.9}
\]
QED.

Retaining the leading term gives the sharper normalized limit

\[
 \boxed{
 \lim_{\sigma\downarrow0}{1\over\log(1/\sigma)}
 \left\|{\chi(\,\cdot\,)\over\sigma+i\,\cdot}
 \right\|_{H^{-1/2}}^2=2\pi.}                       \tag{1.10}
\]

Indeed the cutoff error is uniformly bounded in `H^(-1/2)`, so its square
is `O(1)` and its cross term with the Cauchy kernel is only
`O(sqrt(log(1/sigma)))`.

The exponent is sharp: a Cauchy boundary value belongs locally to
`H^{-1/2-delta}` for every `delta>0`, but not to `H^{-1/2}`.

## 2. Residue extraction at the critical index

Let

\[
 \mathcal H_{+,T}F(z)
 =-{\zeta'\over\zeta}(\tfrac12+z)K_F(z)-Q_{+,T}(z) \tag{2.1}
\]

be the meromorphic right-tail transform of v94 (695).  The correction
`Q_(+,T)` is entire.

### Theorem 2.1 -- exact negative-half residue mass

Let `rho=1/2+i gamma` be a critical-line zero of multiplicity `m_rho`, and
choose `chi in C_c^infinity(R)` equal to one near `gamma` and supported in
an interval containing no other critical-zero ordinate.  Then

\[
 \boxed{
 \lim_{\sigma\downarrow0}{
 \left\|\chi(\,\cdot-\gamma\,)
 \mathcal H_{+,T}F(\sigma+i\,\cdot)
 \right\|_{H^{-1/2}(\mathbb R)}^2
 \over\log(1/\sigma)}
 =2\pi m_\rho^2|K_F(i\gamma)|^2.}                  \tag{2.2}
\]

Consequently

\[
 \left\|\chi(\,\cdot-\gamma\,)
 \mathcal H_{+,T}F(\sigma+i\,\cdot)
 \right\|_{H^{-1/2}}
 =o\left(\sqrt{\log(1/\sigma)}\right)
 \quad\Longleftrightarrow\quad K_F(i\gamma)=0.     \tag{2.3}
\]

In particular, a locally uniform `H^(-1/2)` bound implies (2.3).

#### Proof

Near `z=i gamma`, the Laurent expansion used in v94 (696) is

\[
 \mathcal H_{+,T}F(\sigma+i\tau)
 =-{m_\rho K_F(i\gamma)\over
       \sigma+i(\tau-\gamma)}+R_\sigma(\tau),       \tag{2.4}
\]

where the localized remainder is bounded in every fixed noncritical
Sobolev norm uniformly for small `sigma`.  Formula (1.10) gives the
normalized squared norm of the principal part.  The remainder square
divided by `log(1/sigma)` tends to zero, as does the cross term by
Cauchy--Schwarz.  This proves (2.2).  If `K_F(i gamma)=0`, the principal
part is absent and the localized family is uniformly bounded; the converse
follows directly from the positive limit in (2.2).  This proves (2.3).
QED.

### Theorem 2.2 -- finite critical-window defect mass

Let `J` be a compact ordinate interval whose endpoints are not ordinates of
critical zeros.  Choose a slightly larger compact interval `J'` containing
no critical-zero ordinates outside `J`, and choose
`chi_J in C_c^infinity(R)` equal to one on `J` and supported in the interior
of `J'`.  Then

\[
 \boxed{
 \lim_{\sigma\downarrow0}{
 \|\chi_J\mathcal H_{+,T}F(\sigma+i\,\cdot)\|_{H^{-1/2}}^2
 \over\log(1/\sigma)}
 =2\pi\sum_{\substack{\rho=1/2+i\gamma\\ \gamma\in J}}
 m_\rho^2|K_F(i\gamma)|^2.}                         \tag{2.5}
\]

Thus distinct critical poles are asymptotically orthogonal at the critical
negative-half trace scale.

#### Proof

Only finitely many critical zeros lie over `J`.  Choose disjoint local
cutoffs and use (2.4) at each of them.  For two different ordinates
`gamma != gamma'`, the leading Cauchy cross term, up to uniformly bounded
cutoff errors, is a constant multiple of

\[
 \int_0^\infty {e^{-2\sigma t}e^{i(\gamma-\gamma')t}
                    \over\sqrt{1+t^2}}\,dt.         \tag{2.6}
\]

Dirichlet's test makes (2.6) bounded as `sigma downarrow 0`, because the
phase is nonconstant.  The diagonal terms have the asymptotic (1.10).
Every cross term involving a uniformly `H^(-1/2)` remainder is
`O(sqrt(log(1/sigma)))` by Cauchy--Schwarz, and the remainder--remainder
term is `O(1)`.  Division by `log(1/sigma)` therefore kills every
off-diagonal and remainder term, leaving exactly the sum in (2.5).  QED.

### Corollary 2.2a -- the global critical-defect square is faithful

Let `J_R=[-R,R]`, moving its endpoints slightly when necessary so that they
are not critical-zero ordinates, and define the extended quadratic
functional

\[
 \mathfrak D_T^{\rm crit}(F)
 :=\sup_{R>0}\ 8\pi
 \sum_{\substack{\rho=1/2+i\gamma\ {\mathrm{simple}}\\ |\gamma|\le R}}
 |K_F(i\gamma)|^2\in[0,+\infty].                    \tag{2.6a}
\]

Then

\[
 \boxed{\mathfrak D_T^{\rm crit}(F)=0
 \quad\Longleftrightarrow\quad F=0.}               \tag{2.6b}
\]

Thus the critical antisymmetric residue carrier is not merely positive: it
is a faithful extended square on every fixed Paley--Wiener window.

#### Proof

The forward implication says that `K_F(i gamma)=0` at every simple critical
zero.  The unconditional simple-critical family has counting function
`gg R log R`, whereas a nonzero Cartwright function of type at most `T` has
only `O_T(R)` zeros.  Hence `K_F` is identically zero.  Injectivity of the
compact-support Laplace transform gives `F=0`.  The reverse implication is
immediate.  QED.

### Theorem 2.3 -- exact symmetric/antisymmetric critical split

Let `mathscr A_+` and `mathscr A_-` be the two oriented currents of v94
(419), and retain the compact window `J` and cutoff `chi_J` of Theorem 2.2.
For every parity zero mode,

\[
 \lim_{\sigma\downarrow0}{
 \|\chi_J(\mathscr A_++\mathscr A_-)
       (\sigma+i\,\cdot)\|_{H^{-1/2}}^2
 \over\log(1/\sigma)}=0,                            \tag{2.7}
\]

whereas

\[
 \boxed{
 \lim_{\sigma\downarrow0}{
 \|\chi_J(\mathscr A_+-\mathscr A_-)
       (\sigma+i\,\cdot)\|_{H^{-1/2}}^2
 \over\log(1/\sigma)}
 =8\pi\sum_{\substack{\rho=1/2+i\gamma\\ \gamma\in J}}
 m_\rho^2|K_F(i\gamma)|^2.}                         \tag{2.8}
\]

Thus the complete critical defect is a positive squared mass carried by
the antisymmetric causal port; the symmetric functional-equation port has
zero mass at this scale.

#### Proof

Equation v94 (421) identifies `mathscr A_++mathscr A_-` with the sum of
the two Gamma exterior transforms and a compact Tate term.  Its localized
boundary family is uniformly `L2`, hence uniformly `H^(-1/2)`, proving
(2.7).  At a critical zero, v94 (423)--(424) gives opposite residues
`-m_rho K_F(i gamma)` and `+m_rho K_F(i gamma)`.  Their difference
therefore has residue `-2m_rho K_F(i gamma)`.  Apply Theorem 2.2; squaring
the factor two changes `2 pi` into `8 pi`, which proves (2.8).  QED.

## 3. First-contact exclusion

### Corollary 3.1 -- critical negative-half closure criterion

Let `F` be a compact-window parity first-contact state.  Suppose the
little-o condition in (2.3) holds around every simple critical-line zero of
zeta.  Then `F=0`.

#### Proof

Theorem 2.1 gives `K_F(i gamma)=0` at every simple critical zero.  Any
unconditional positive-proportion theorem for simple critical zeros gives
a counting function `gg R log R`.  The entire Cartwright function `K_F`
has exponential type at most `T`, so a nonzero `K_F` has only `O_T(R)`
zeros in `|z|<=R`.  Thus `K_F` is identically zero, and transform
injectivity gives `F=0`.  QED.

**Citation correction.**  V94 cites X. Wu (2015) at this step.  Wu proves a
positive proportion of **distinct zeros in the full critical strip**; that
does not by itself supply the simple-critical-line family required by this
one-sided local argument.  The needed unconditional input is classical:
J. B. Conrey, *More than two fifths of the zeros of the Riemann zeta
function are on the critical line*, J. reine angew. Math. **399** (1989),
1--26, proves that more than `2/5` of all zeros are simple and on the
critical line.  Hence, with the usual ordinate count, the required family
has cardinality `gg R log R`.  The stronger recent result is not needed.  For
context only, arXiv:2608.13637 is by Levent Alpöge and Ralph Furman.  The older two-sided Hardy argument, which annihilates
every distinct zero, may continue to use Wu.

Consequently row (d) follows if every hypothetical first-contact state
satisfies the little-o condition in (2.3) at this critical family.

### Corollary 3.2 -- an obstruction is critically extensive

If `F` is nonzero, then among the simple critical zeros with
`|gamma|<=R`, all but `O_T(R)` have nonzero oriented residue:

\[
 \#\{\rho=1/2+i\gamma:\ |\gamma|\le R,\ m_\rho=1,
                 K_F(i\gamma)\ne0\}
 \gg R\log R.                                      \tag{3.1}
\]

Consequently a nonzero first-contact obstruction cannot be a finite set of
exceptional poles or a two-Tate boundary defect.  Its antisymmetric
critical carrier is extensive.

#### Proof

The simple-critical family has cardinality `gg R log R`.  A nonzero
Cartwright function of type at most `T` has only `O_T(R)` zeros in the same
disc.  Removing those ordinates leaves (3.1).  The two Tate corrections and
the compact prehistory are entire, so they have no polar coordinates with
which to cancel this carrier.  QED.

## 4. Comparison with the former Hardy target

V94 asks that the exterior arithmetic tail belong to `L2`, equivalently
that `exp(Tz) mathcal H_(+,T)F` belong to `H2(C_+)`.  Such a bound gives
uniform local `L2=H^0` boundary control and therefore implies the little-o
condition in (2.3).

The converse is false at the level of function spaces:

\[
 L^2_{\rm loc}=H^0_{\rm loc}
 \subsetneq H^{-1/2}_{\rm loc}.                    \tag{4.1}
\]

Thus Theorem 2.1 lowers the ambient regularity used to *detect* the polar
datum, but (2.2)--(2.3) show that it does not lower the logical burden:

\[
 \text{sublogarithmic critical trace}
 \quad\Longleftrightarrow\quad
 \text{oriented residue cancellation}.             \tag{4.2}
\]

Accordingly the next proof may not list the sublogarithmic estimate as a
separate open regularity lemma.  It must derive residue cancellation from a
new equality-state law.  Meromorphic continuation, the symmetric functional
equation and the completed graph current cancel opposite residues and
cannot establish (4.2) for one orientation.

The signed Green identity of phase 120 does not change this conclusion.
It is first-order in the indefinite generator `Q`; the mass (2.8) is the
positive square of its missing antisymmetric polar datum.  Adding (2.8) as
an independent correction would describe the negative defect, not prove
that the original signed form is positive.  A valid global square must make
this extensive defect vanish from the equality-state source law.
