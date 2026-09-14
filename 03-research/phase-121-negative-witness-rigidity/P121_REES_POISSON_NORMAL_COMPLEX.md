# P121 -- the Rees--Poisson normal complex and the oriented Euler regulator

## Status

This note realizes the abstract orientation-Rees parameter inside the actual
source-defined Poisson comparison of row (c).  Its normal derivative is
faithful before quotienting by source motion, and the row-(b) logarithmic
Euler connection sends that derivative to the Bloch regulator of the
oriented relative `K_2` class.

No positivity or spectral zero is used.  The construction identifies the
precise horizontal lift which a first-contact state must satisfy.

## 1. The two Poisson arrows

Use the spaces and conventions of paper 42.  On the two-Tate source

\[
 \mathcal H_\cap=\{f\in\mathcal H_+:f(0)=\mathcal Ff(0)=0\}
\tag{1.1}
\]

Poisson summation is the equality

\[
 B_+f=B_-f,
 \qquad
 B_+:=Z,
 \qquad
 B_-:=\mathscr JZ\mathcal F .
\tag{1.2}
\]

Both arrows are defined before the nuclear character is taken.  Introduce
the orientation-Rees deformation

\[
 \mathcal P_z(f):=zB_-f-z^{-1}B_+f,
 \qquad z\in\mathbb G_m .
\tag{1.3}
\]

At the augmentation `z=1`, (1.3) is the ordinary Poisson difference.

### Theorem 1.1 -- faithful fixed-source normal

For every `f in H_cap`,

\[
 \mathcal P_z(f)=(z-z^{-1})Zf,                    \tag{1.4}
\]

and hence

\[
 \nu_{\rm Pois}(f)
 :=\frac12z\partial_z\mathcal P_z(f)|_{z=1}=Zf.  \tag{1.5}
\]

The normal map `nu_Pois:H_cap -> H_cup` is injective and is a topological
isomorphism onto `Z H_cap`.

#### Proof

Equation (1.2) substituted in (1.3) gives (1.4), and differentiation gives
(1.5).  Meyer's closed-range theorem says that `Z:H_+ -> H_cup` is a
topological isomorphism onto its range.  Its restriction to `H_cap` is
therefore injective and has inverse `Z^(-1)` on `Z H_cap`.  QED.

Over `C[delta]/(delta^2)`, with `z=1+delta/2`, this is the exact first-order
identity

\[
 \mathcal P_{1+\delta/2}(f)=\delta Zf.             \tag{1.6}
\]

Thus the scalar Poisson equality is not missing an unspecified normal
direction: its frozen-source conormal is the explicit vector `Zf`.

## 2. The Euler connection reads the K2 regulator

For one prime put

\[
 Z_p=(1-U_p)^{-1},
 \qquad
 \nabla_p:=Z_p\,\partial(Z_p^{-1}).                \tag{2.1}
\]

On the safe half-plane, the Mellin symbol of `nabla_p` is

\[
 \frac{de_p}{e_p}
 =\sum_{j\ge1}(\log p)p^{-j(1/2+s)}\,ds,
 \qquad e_p(s)=1-p^{-1/2-s}.                       \tag{2.2}
\]

If `K_f` is the compact Mellin--Laplace transform of `f`, (1.5) gives
`Z^(-1)nu_Pois(f)=f`.  Therefore

\[
 \boxed{
 \operatorname {Mellin}\left(
   \nabla_p Z^{-1}\nu_{\rm Pois}(f)\right)
 =K_f(s)\frac{de_p(s)}{e_p(s)}.}                  \tag{2.3}
\]

The right side is exactly the relative Bloch coordinate of

\[
 \widetilde\kappa_{p,f}=\{e_p,1+\epsilon K_f\}.   \tag{2.4}
\]

### Theorem 2.1 -- Poisson/K2 normal comparison

For every finite prime set `S`, the place-resolved logarithmic connection

\[
 \nabla_S^{\rm Eul}:=(\nabla_p)_{p\in S}           \tag{2.5}
\]

fits into the commutative diagram

\[
\begin{array}{ccc}
 \mathcal H_\cap
 &\xrightarrow{\ \nu_{\rm Pois}\ }& Z\mathcal H_\cap\\[1mm]
 \downarrow f\mapsto(\widetilde\kappa_{p,f})_{p\in S}
 &&\downarrow\nabla_S^{\rm Eul}Z^{-1}\\[1mm]
 \displaystyle\bigoplus_{p\in S}K_2^{\rm rel}(e_p)
 &\xrightarrow{\ \operatorname {bl}\ }&
 \displaystyle\bigoplus_{p\in S}
       K_f\,{de_p\over e_p}.
\end{array}                                        \tag{2.6}
\]

After tame localization at `lambda_(p,k)`, the lower row has oriented
normal coefficient `K_f(lambda_(p,k))`.  Thus the abstract Rees jet of
`P121_CENTRAL_JET_ORIENTATION_BRIDGE.md` is the logarithmic Euler image of
the concrete frozen-source Poisson normal.

#### Proof

The upper composition is (1.5), followed by `Z^(-1)`.  Formula (2.2)
computes its image under `nabla_p`; this is (2.3).  The lower composition is
the Bloch formula for (2.4), already proved in the relative `K_2`
construction.  The two expressions agree componentwise before summing over
places.  Tame localization evaluates `K_f` at the simple zero of `e_p`.
QED.

## 3. Fixed source versus source motion

The distinction is essential.  For a differentiable family `f_z`,

\[
 \frac12z\partial_z\mathcal P_z(f_z)|_{z=1}
 =Zf_1+\frac12\mathcal P_1(\dot f_1).              \tag{3.1}
\]

The first term is the frozen-source normal (1.5).  The second is tangent
source motion.  Passing immediately to Meyer's quotient erases `Z H_cap`;
in particular it erases the first term.  The oriented `K_2` lift avoids
that loss by applying the place-resolved connection before quotienting.

This gives a canonical meaning to **horizontal** in the remaining lift:
the source is held fixed by the row-(b) correspondence frame while the two
Poisson arrows are varied in their normal Rees direction.  No arbitrary
connection on the source bundle is introduced.

## 4. First-contact lift in its final form

Let `N_T=ker Delta_T` at a hypothetical first contact.  The required
statement is now the commutativity of the equality-state inclusion with the
fixed-source normal complex:

\[
 \boxed{
 F\in N_T
 \quad\Longrightarrow\quad
 \nabla_p Z^{-1}\nu_{\rm Pois}(F)
 \text{ is unramified at }e_p=0
 \quad(p\text{ cofinally}).}                       \tag{4.1}
\]

By (2.3), (4.1) is precisely

\[
 K_F\left(-\frac12+\frac{2\pi i}{\log p}\right)=0
 \quad(p\text{ cofinally}).                       \tag{4.2}
\]

The cofinal identity theorem then gives `K_F=0` and `F=0`.  Therefore (4.1)
implies absence of first contact, the global square and row (d).

What has changed is the provenance of the target.  It is no longer an
abstract demand that the antisymmetric coordinate vanish: it is the tame
ramification of the explicit fixed-source normal to the actual Poisson
equalizer, read by the actual row-(b) Euler connection.

## 5. Ledger

```text
orientation-Rees deformation of the two Poisson arrows     CONSTRUCTED
fixed-source normal = Zf                                    PROVED
faithfulness of the fixed-source normal                     PROVED
Euler connection of the normal = relative K2 regulator     PROVED
tame normal = c^(1)                                         PROVED
first-contact inclusion is unramified/horizontal            OPEN
global square and row (d)                                   OPEN
```

The last open line is the same global-square theorem, now attached to a
single source-defined diagram.  No modification of paper 42 is justified
before it is proved.
