# Horizontal modulation does not add an equality-state law

## 1. Candidate

Translation of the source would multiply each residue coordinate by a
factor depending on the horizontal position of the zero, but support
saturation prevents translating a first-contact vector inside the same
window.  A tempting substitute is multiplication by an exponential:

\[
 (M_\sigma F)(t)=e^{\sigma t}F(t),                 \tag{1.1}
\]

which preserves the support window and shifts the compact Laplace transform,

\[
 K_{M_\sigma F}(z)=K_F(z-\sigma).                  \tag{1.2}
\]

One might hope to polarize the radical equation against the family
`M_sigma F`, analytically continue in `sigma`, and separate critical and
off-critical residue orbits.  This note shows that the resulting identity
is exactly radicality evaluated on an analytic family of tests.  It adds no
constraint on `K_F`.

## 2. Tate correction

Let

\[
 \mathcal P_T=\ker M_-\cap\ker M_+
\]

be the physical primitive space.  Choose once and for all
`u_-,u_+ in L^2(I_T)` such that the matrix

\[
 \bigl(M_\eta u_\nu\bigr)_{\eta,\nu\in\{-,+\}}
\]

is invertible.  It defines a bounded finite-rank projection `Pi_T` onto
`P_T`.  For a fixed compact-window source put

\[
 G_\sigma:=\Pi_T M_\sigma F.                       \tag{2.1}
\]

For complex `sigma`, `G_sigma` is an entire `L^2(I_T)`-valued family, and
every member is primitive.  Its Laplace transform is

\[
 K_{G_\sigma}(z)=K_F(z-\sigma)
   -c_-(\sigma)K_{u_-}(z)-c_+(\sigma)K_{u_+}(z),   \tag{2.2}
\]

with entire scalar correctors `c_+/-` determined solely by the two Tate
moments.

## 3. Exact collapse

### Theorem 3.1 -- analytic-test-family no-go

Let `F` be a first-contact radical for the nonnegative compressed form
`q_T`.  Then

\[
 q_T(F,G_\sigma)=0                                 \tag{3.1}
\]

for every complex `sigma` for which the sesquilinear convention makes the
evaluation holomorphic (and, equivalently, for all real `sigma` followed
by analytic continuation).  Every derivative at `sigma=0` is already a
special case of

\[
 q_T(F,G)=0\qquad(G\in\mathcal P_T).               \tag{3.2}
\]

Consequently (3.1), rewritten through (1.2)--(2.2) in residue coordinates,
cannot imply the vanishing of an individual critical or off-critical
coordinate unless that conclusion already follows from the full radical
equation (3.2).

#### Proof

At first contact the compressed operator is nonnegative and `F` lies in
its kernel.  Cauchy--Schwarz for the semidefinite form gives (3.2).  Since
`G_sigma` belongs to `P_T`, (3.1) follows immediately.  Differentiating the
entire family merely substitutes the primitive tests

\[
 \left.\partial_\sigma^kG_\sigma\right|_{\sigma=0}
 =\Pi_T(t^kF)
\]

into (3.2).  No new equation is produced.  QED.

### Corollary 3.2

Horizontal analytic continuation of (3.1) cannot be used as a residue
selector.  Any argument which extracts `K_F(i gamma)=0` from it must contain
an additional growth, sign, boundary or source law not supplied by first
contact.

## 4. Relation to the existing selector no-go

The nonlinear-polarizer theorem already forbids a same-window source which
preserves almost all critical coordinates while modifying off-line ones.
The present calculation closes an earlier stage: even the canonical
support-preserving analytic family `exp(sigma t)F`, after exact Tate
correction, supplies no extra equality.  It is not a hidden way around the
Cartwright selector obstruction.

## 5. Verdict

The modulation family is useful as a coordinate system for the existing
radical equation, but it is not the missing nonlinear Euler equality law.
The live source must act before scalar polarization or must impose a
condition not valid for every primitive test family.
