# R170_834 — Canonical Tate port: Hardy range, exterior ambiguity, and exact quotient

Continuation of R170_829--833. Status: the Hardy
port of an arithmetic source is indeed canonical; it does not induce a
canonical Tate port on the arbitrary exponential columns of R170_829. The
bilateral sum does not remove the ambiguity either. An exact quotient
exists, but it loses precisely the Tate directions and does not close the
bridge.

## 0. Verdict

Let

\[
 Z=\ker H_T,\qquad
 r_F=\alpha_F e^{-t/2}+\beta_F e^{t/2}\quad (t\in I_T),
 \qquad \mathcal A F=(\alpha_F,\beta_F).
 \tag{0.1}
\]

The inventory and computations of this note prove the following.

1. R161_009 and R161_015 canonically fix the polar corrections of the
   **Hardy ports produced by a source** of first contact. They do not fix
   the value of \(\langle r_F,z\rangle\) for every exterior test
   \(z\).
2. There are two natural and explicit continuations of the existing data:
   the continuation by the global characters and the boundary form given
   by the Hardy reproducing kernel. They give different matrices already
   on two Gamma exponents. Hence the corpus does not select a unique
   \(\Theta_\pm\) on \(\operatorname{Ran}\iota_\pm\).
3. Even imposing reflection and parity, a covariant exterior modification
   changes the bilateral pairing. Cancellation of the extension
   dependence is **false**.
4. The only intrinsic quotient is modulo
   \(\operatorname{Ran}{\cal A}^*\). Equivalently, the form is well
   defined when compressed to
   \(Z_0=\ker{\cal A}\). On \(Z_0\) one obtains an explicit matrix
   residual, but it is not proved to be zero nor to have a sign.

In particular, the typing defect of R170_831 is not repaired by declaring
that the Hardy correction is the Tate term of the weak equation. That
declaration would be a new transmission law.

## 1. Non-duplication check and correction of the historical map

The following facts were already in the corpus and are used without
claiming novelty.

- P121_EXACT_TATE_COLLAR_LOCALIZATION, (5.1)--(5.3), determines
  \((\alpha_F,\beta_F)\) via the currents \(J_\pm(F)\) and the crossed
  matrix
  \[
   C_T=\begin{pmatrix}2T&2\sinh T\\2\sinh T&2T\end{pmatrix},
   \qquad C_T{\cal A}F=(J_+(F),J_-(F)).             \tag{1.1}
  \]
- P121_RESOLVED_TATE_COLLAR_INTEGRAL evaluates \(J_\pm\) and proves that
  the two Tate moments of \(F\) do not annihilate them.
- R161_006 separates each exterior Poisson port into a one-sided
  discrepancy and a Tate scalar of the opposite tail.
- R161_009 identifies the polar residues of the Hardy ports produced by
  the source with those crossed currents. R161_015 fixes the right
  corrector vector via
  \[
  \Theta_T(s)={e^{-T(s-1)}\over s},\qquad \Theta_T(1)=1,
  \tag{1.2}
  \]
  the Hardy reproducing kernel shifted to the endpoint.
- R161_010 is not a valid closure: R161_011 reintroduces the
  cosine/reflection scattering that had been omitted. R161_018
  provisionally rejects the linear limit and asks for a finite quadratic
  defect, but R161_075 corrects the scope of that no-go: the
  identification between the physical limit and the zero meromorphic
  product is not proved. R161_019 proves rigidity via Gamma poles
  **conditional** on the physical scattering.
- P122_029 proves that a transmission law must supply the boundary
  pairing; Lions--Magenes regularity does not produce it.
- R162_404 localizes the polar layer in the exterior Hankel operator, but
  at first contact the exterior test of that construction loses the
  polar jets multiplied by the zero eigenvalue.
- R170_829 formulates \(\operatorname{Herm}(\Lambda Y)=D_\Delta\), and
  R170_831 fully computes the Gamma--Euler part
  \(\Gamma_{\pm,M}\). This note only decides what can be extracted from
  the already-existing Tate data.

## 2. Two natural extensions that do not coincide

Set, as in Paper 47 and R170_702,

\[
 a_m=2m+\tfrac12,\qquad
 b_m=\sqrt{a_m}\,e^{-a_m(T+\delta)},\qquad m\ge1,
 \tag{2.1}
\]

and

\[
 z_c^+(t)={\bf1}_{t>T}\sum_{m\le L}b_mc_me^{-a_mt},
 \qquad z_c^-=Jz_c^+.
 \tag{2.2}
\]

All the \(a_m\) are greater than \(1/2\), so that the following pairings
converge absolutely.

### 2.1. Continuation by the global characters

If (0.1) is extended literally to the whole line, the right tail gives

\[
 \Theta_+^{\rm char}(c)(F)
 =\alpha_F\sum_{m\le L}\overline{b_mc_m}\,
   {e^{-(a_m+1/2)T}\over a_m+1/2}
 +\beta_F\sum_{m\le L}\overline{b_mc_m}\,
   {e^{-(a_m-1/2)T}\over a_m-1/2}.                 \tag{2.3}
\]

The left tail exchanges the two lines:

\[
 \Theta_-^{\rm char}(c)(F)
 =\alpha_F\sum_{m\le L}\overline{b_mc_m}\,
   {e^{-(a_m-1/2)T}\over a_m-1/2}
 +\beta_F\sum_{m\le L}\overline{b_mc_m}\,
   {e^{-(a_m+1/2)T}\over a_m+1/2}.                 \tag{2.4}
\]

This is a perfectly well-defined choice compatible with reflection. It is
not a consequence of the weak equation: the global characters are not
\(L^2(\mathbb R)\) vectors, and only their restriction to \(I_T\) appears
in Paper 47.

### 2.2. The boundary form of the canonical Hardy port

On the right half-line, the Tate evaluation functional is

\[
 \ell_+(z)=\int_T^\infty z(t)e^{-t/2}\,dt.          \tag{2.5}
\]

Its reproducing vector normalized to have transform equal to one at the
pole is \(e^T{\bf1}_{t>T}e^{-t/2}\), exactly (1.2) in Laplace
coordinates. On (2.2),

\[
 \ell_+(z_c^+)=\sum_{m\le L}\kappa_m c_m,
 \qquad
 \kappa_m=b_m{e^{-(a_m+1/2)T}\over a_m+1/2}.       \tag{2.6}
\]

Reflection gives the same line \(\kappa\) on the left. Let
\(p_+(F),p_-(F)\) be the two canonical polar residues of R161_009. In the
convention where the complete residues are the resolved currents,
\(p(F)=(J_+(F),J_-(F))=C_T{\cal A}F\); any change of order only conjugates
the following formulas by the exchange matrix.

The Hardy kernel then defines a canonical boundary form **on the range of
ports**:

\[
 \Theta_+^{\rm H}(c)(F)=p_+(F)\,\overline{\ell_+(z_c^+)},
 \qquad
 \Theta_-^{\rm H}(c)(F)=p_-(F)\,\overline{\ell_-(z_c^-)}.
 \tag{2.7}
\]

Formula (2.7) is useful and does not contain an arbitrary profile. But it
is a form built from the source port's residue and the Hardy metric; it
is not the pairing of the continuation of \(r_F\) with \(z_c^\pm\).

### 2.3. Exact incompatibility

Write

\[
 \kappa_m^-:=b_m{e^{-(a_m+1/2)T}\over a_m+1/2},\qquad
 \kappa_m^+:=b_m{e^{-(a_m-1/2)T}\over a_m-1/2}.    \tag{2.8}
\]

Then

\[
 {\kappa_m^+\over\kappa_m^-}
 =e^T{a_m+1/2\over a_m-1/2}.                       \tag{2.9}
\]

The ratio depends on \(m\). For \(L\ge2\), no fixed change of basis in
the two-dimensional Tate space can transform the single Hardy line
\(\kappa^-\) into the two lines
\((\kappa^-,\kappa^+)\) of the character continuation. Hence

\[
 \boxed{\Theta_\pm^{\rm char}\ne\Theta_\pm^{\rm H}
 \quad\hbox{in general}.}                                    \tag{2.10}
\]

Both constructions use only already-fixed data and both respect
reflection. Their discrepancy proves that these requirements do not
determine the port required by R170_831.

## 3. The bilateral sum does not remove the freedom

Non-uniqueness is not merely the comparison between two gauges. Let
\(E_0\) be any linear, reflection-compatible extension of the restricted
Tate space. Take
\(h\in C_c^\infty((T,\infty))\) and define

\[
 H\phi_-=h,\qquad H\phi_+=Jh,
 \qquad \phi_\mp=e^{\mp t/2}|_{I_T}.              \tag{3.1}
\]

Then \(H\phi_\pm\) vanishes on \(I_T\),
\(JH\phi_-=H\phi_+\), and
\(E_\lambda=E_0+\lambda H\) is another extension with the same
restrictions and the same reflection covariance.

For a right tail,

\[
 \langle E_\lambda r_F-E_0r_F,z_c^+\rangle
 =\lambda\alpha_F\langle h,z_c^+\rangle.          \tag{3.2}
\]

One can choose \(h\) so that this last product is nonzero. If
\(F\) has parity \(\varepsilon\), then
\(\beta_F=\varepsilon\alpha_F\). For the bilateral test of the same
parity,

\[
 z_c^{(\varepsilon)}=z_c^++\varepsilon Jz_c^+,
 \tag{3.3}
\]

the total variation is

\[
 \langle (E_\lambda-E_0)r_F,z_c^{(\varepsilon)}\rangle
 =2\lambda\alpha_F\langle h,z_c^+\rangle,          \tag{3.4}
\]

not zero in general. Thus, reflection and the bilateral sum duplicate the
ambiguity in the compatible branch; they do not cancel it.

## 4. The maximal quotient where the port is indeed intrinsic

In a basis of \(Z\), represent \({\cal A}:Z\to\mathbb C^2\) by the matrix
of the coefficients \((\alpha,\beta)\). Every modification of an exterior
extension changes the port, on the \(L\) columns, by a matrix of the form

\[
 \delta\Theta={\cal A}^*K,
 \qquad K:\mathbb C^L\to\mathbb C^2.             \tag{4.1}
\]

Conversely, using two functions \(h\) as in (3.1), one obtains those
lines arbitrarily over any finite, linearly independent family of
tails. Hence the maximal quotient independent of the extension is

\[
 Z^*/\operatorname{Ran}{\cal A}^*.                            \tag{4.2}
\]

Its concrete dual realization is

\[
 Z_0:=\ker{\cal A}
 =\{F\in Z:r_F=0\}.                              \tag{4.3}
\]

Let \(P_0\) be the projection of \(Z\) onto \(Z_0\). For any choice of
\(\Theta_\pm\), any synthesis
\(C_\pm:Z\to\mathbb C^L\), and the computed responses
\(\Gamma_{\pm,M}:\mathbb C^L\to Z^*\) of R170_831, we have

\[
\boxed{
 P_0\operatorname{Herm}\!\left[
  (\Gamma_{+,M}-\Theta_+)C_+
 +(\Gamma_{-,M}-\Theta_-)C_-
 \right]P_0
 =P_0\operatorname{Herm}\!\left[
  \Gamma_{+,M}C_++\Gamma_{-,M}C_-
 \right]P_0.}                                      \tag{4.4}
\]

This is the valid cancellation of the extension dependence. It is not a
cancellation over all of \(Z\): it eliminates exactly the directions in
which the Tate forcing lives.

## 5. Resulting matrix and explicit residual

For the candidate of R170_829 take

\[
 C_+=(I-D_{N,L})R_L,                              \tag{5.1}
\]

and let \(C_-\) be its reflected copy; if the same Gamma coordinates are
used, reflection is already incorporated into \(\Gamma_{-,M}\) and one
may set \(C_-=C_+\).

In a basis \(F_1,\ldots,F_d\) of \(Z\), the Hardy choice (2.7) has
entries

\[
 (\Theta_+^{\rm H})_{im}=p_+(F_i)\kappa_m,
 \qquad
 (\Theta_-^{\rm H})_{im}=p_-(F_i)\kappa_m,          \tag{5.2}
\]

with the conjugations shifted if the opposite convention for the linear
argument of the inner product is used. Define

\[
 M_{\rm H}:=\operatorname{Herm}\!\left[
  (\Gamma_{+,M}-\Theta_+^{\rm H})C_+
 +(\Gamma_{-,M}-\Theta_-^{\rm H})C_-
 \right]                                           \tag{5.3}
\]

and

\[
 \boxed{{\cal R}_{\rm H}:=M_{\rm H}-D_\Delta.}     \tag{5.4}
\]

Formulas (2.2), (4.1) of R170_831 compute every entry of
\(\Gamma_{\pm,M}\); (1.1), (2.6), and (5.2) compute the whole Hardy
block; and Paper 47 computes

\[
 D_\Delta=R_L^*(I-D_{N,L})R_L.                    \tag{5.5}
\]

Hence (5.4) is a fully specified finite residual, not a symbol for an
unknown term. The corpus does not contain an identity proving

\[
 {\cal R}_{\rm H}=0,
 \qquad {\cal R}_{\rm H}\succeq0,
 \quad\hbox{or}\quad {\cal R}_{\rm H}\preceq0.      \tag{5.6}
\]

Moreover, replacing the Hardy choice with the character continuation
changes (5.4) by the explicit finite-rank block

\[
 {\cal R}_{\rm char}-{\cal R}_{\rm H}
 =-\operatorname{Herm}\!\left[
  (\Theta_+^{\rm char}-\Theta_+^{\rm H})C_+
 +(\Theta_-^{\rm char}-\Theta_-^{\rm H})C_-
 \right].                                           \tag{5.7}
\]

Its rank is at most four after Hermitizing. There is no reason for it to
vanish, and (2.9) shows that its lines are already different before
compression.

In the canonical quotient, the surviving residual is

\[
 \boxed{
 {\cal R}_0=P_0\left(
 \operatorname{Herm}[\Gamma_{+,M}C_++\Gamma_{-,M}C_-]
 -D_\Delta\right)P_0.}                              \tag{5.8}
\]

The equality \({\cal R}_0=0\) remains **open**. Even if proved, it would
only control \(Z_0\); it does not force \({\cal A}F=0\) for the remaining
vectors.

## 6. Exact relation to the phase 161 scattering goal

R170_829 and the quadratic theorem requested by R161_018 belong to the
same structural class: both must preserve, before the completed linear
limit, both orientations, the product
\(\Lambda*1=\log\), the polar terms, and the quadratic metric.

They are not the same theorem in the current state.

- R161_018 asks for a norm variation of the **canonical product port
  produced by the source**, in order to obtain the physical scattering;
  R161_019 would then close via the lattice of Gamma poles.
- R170_829 asks for transporting the positive detector \(D_\Delta\)
  through the arbitrary exponential columns \(\iota_\pm C_\pm\).
- It has not been proved that \(\iota_\pm C_\pm F\) is the derivative,
  the scattering reverse, or the Tate projection of the product port of
  R161_015. Discrepancy (2.10) is precisely the missing interface datum.

Hence there is only a proved structural analogy, not an equivalence. An
equivalence would require a source map defined before the limit that
simultaneously identified the Hardy evaluation, the Gamma columns, and
the collar \(D_\Delta\). Building that map would be the new theorem, not
a formal consequence of phases 161 or 170.

## 7. Ledger

```text
Hardy polar port of the source                          PROVED / CANONICAL
continuation by global characters                       DEFINED, NOT FORCED
Hardy port as <r_F,z_ext>                                FALSE AS A DEDUCTION
uniqueness of Theta_± on Ran(iota_±)                     FALSE
bilateral cancellation of the ambiguity                  FALSE
quotient modulo Ran(A*) / compression to ker(A)          PROVED
Hardy matrix M_H and residual R_H                        COMPUTED EXACTLY
Herm[(Gamma-Theta)C]=D_Delta over all of Z               OPEN
projected equality R_0=0                                 OPEN
equivalence with reverse scattering of R161_018          NOT PROVED / FORMALLY FALSE
D and the global inequality                              OPEN
```

The next piece must not be another choice of \(\Theta_\pm\). It must be a
quadratic source--port map that derives one of the matrices (5.3) from
the finite Poisson--Chebyshev identity and proves its relation to
\(D_\Delta\). Without that map, choosing between (2.3) and (2.7) amounts
to imposing the very transmission law one wants to prove.
