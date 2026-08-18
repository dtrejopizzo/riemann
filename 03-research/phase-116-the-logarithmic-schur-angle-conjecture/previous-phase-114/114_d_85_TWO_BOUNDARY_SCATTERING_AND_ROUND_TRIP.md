# D.85 — Two-boundary scattering cohomology and the round-trip colligation

## Status

D.84 asks for a two-boundary scattering complex and identifies a phase
versus modulus mismatch: the conservative state evolves by `T`, while the
Schur tower evolves by `|T|=(T*T)^(1/2)`.  This note constructs both the
coefficient complex and a canonical round-trip colligation.

The round trip is a real advance.  Alternating the unitary colligation and
its adjoint, while closing the intermediate channel, gives state transition
`C=T*T`.  Its two output channels have moduli
`D_T C^m` and `D_T C^(m+1/2)` and therefore realize exactly the even and odd
Schur layers.  The phase/modulus typing problem is solved.

The negative primitive input still does not land in this colligation.  Its
exact initial residual is

\[
 r_0=2D_Tp-C^{1/2}Vq=2L_-.
\]

The desired sign becomes `||r_0||^2>=||C^(1/2)Vq||^2`.  Conservation does
not imply that estimate; on the positive Halmos graph `r_0=0` while the
right side is nonzero.

The two-strip coefficient complex is also explicit.  Its nonpolar
cohomology is Meyer's Frechet cokernel `V`, and the annulus forcing is a
class in the associated landing Hom-complex.  At fixed cutoff it can be
removed algebraically using `D_T^(-1)`, but the inverse is unbounded in the
directed prolate limit; it is not a bounded coboundary in the required
topological category.

The induced duality on `H^1=V` is the unconditional Paugam--Tate Krein
pairing, with swap blocks, not a definite form.  The periodic Yoneda
category of row A supplies actual section objects and positive ordered
frames, but no dagger-positive trace compatible with von Mangoldt contact:
the contact functional has a negative `2 by 2` Gram determinant on
`{1,delta_p}`.  Hence it does not select a positive polarization of `V`.

No RH, zero-selected polarization or Pick existence is used.  The paper is
not modified.

## 1. The two-strip boundary complex

Let `U_+` and `U_-` be the Frechet half-strip section spaces of D.42 and
let `W_epsilon` be their common meromorphic overlap.  Define the Cech
scattering differential

\[
 d_\gamma:\mathcal U_+\oplus\mathcal U_-
 \longrightarrow\mathcal W_\epsilon,
 \qquad
 d_\gamma(u_+,u_-)=u_- -\gamma^{-1}u_+.                    \tag{1.1}
\]

Its kernel is the Gamma line

\[
 \mathcal L_\gamma=\ker d_\gamma.                          \tag{1.2}
\]

On that kernel, the polar boundary map is

\[
 \operatorname {ev}_{\rm pol}:\mathcal L_\gamma
 \longrightarrow\mathbb C^2,
 \qquad
 (u_+,u_-)\longmapsto(u_+(1),u_-(0)).                       \tag{1.3}
\]

The primitive line is the derived kernel, which here is the ordinary closed
kernel,

\[
 \mathcal L_\gamma^0
 =\ker(\operatorname {ev}_{\rm pol})\subseteq\ker d_\gamma.
                                                                  \tag{1.4}
\]

Thus the two Tate jets are an explicit polar quotient of the boundary
gluing object; they are not the whole scattering state.

The Poisson characteristic map is

\[
 \sigma_\zeta:\mathcal L_\gamma^0\longrightarrow E,
 \qquad
 \sigma_\zeta(u_+,u_-)=\zeta(s)u_+(s)=\zeta(1-s)u_-(s).    \tag{1.5}
\]

Put it in degrees `0,1`:

\[
 \boxed{
 C_{\rm sc}=[\mathcal L_\gamma^0
             \xrightarrow{\sigma_\zeta}E].}               \tag{1.6}
\]

D.42 proves that `sigma_zeta` is a strict closed embedding of Frechet
spaces.  Hence

\[
 H^0(C_{\rm sc})=0,
 \qquad
 H^1(C_{\rm sc})=E/\sigma_\zeta(\mathcal L_\gamma^0)=V.    \tag{1.7}
\]

Equations (1.1)--(1.7) are the requested two-boundary scattering complex:
the Gamma transition glues the charts, (1.3) removes the two polar states,
and the Poisson characteristic produces the nonpolar cohomology.

## 2. The landing Hom-complex and the annulus class

Let `J` be the primitive defect-frame representation and `K` the Schur
observability representation.  On continuous operator cochains define

\[
 \begin{aligned}
 C_{\rm land}^0&=\mathcal L(J,K),\\
 C_{\rm land}^1&=\mathcal L(J,K),\\
 \delta X&=S_KX-XS_J,                                     \tag{2.1}
 \end{aligned}
\]

where `S_J,S_K` are the two sequence shifts.  The cutoff-annulus forcing of
D.81 is the cocycle

\[
 \mathfrak b(F)
 =[L_-,D_R(\Theta_R)\Theta_R^j]R_{\rm src}(F)              \tag{2.2}
\]

written in sequence coordinates.  Its landing class is

\[
 [\mathfrak b]\in H^1(C_{\rm land})
 =C_{\rm land}^1/\delta C_{\rm land}^0.                    \tag{2.3}
\]

D.83 proves that its local one-sided Hankel component is not a coboundary:
the zero-time feedthrough lies outside the range of the Hardy shift
derivation.  D.84 shows that the scalar global mean of that feedthrough
vanishes, but not the full annulus class.

There is a natural trace/character morphism from (2.1) to (1.6).  At the
coefficient level, a class is zero precisely when its representative `c`
belongs to the Poisson range,

\[
 c\in\sigma_\zeta(\mathcal L_\gamma^0).                    \tag{2.4}
\]

By D.41--D.42, (2.4) has the explicit two-chart divisibility criterion

\[
 {c\over\zeta(s)}\in\mathcal U_+,
 \qquad
 {c\over\zeta(1-s)}\in\mathcal U_-,
 \qquad
 \operatorname {ev}_{\rm pol}=0.                           \tag{2.5}
\]

Thus the forcing is a genuine cohomology class unless (2.5) is proved for
its complete prime--Gamma coefficient.  No spectral evaluation is needed
to state this criterion.

## 3. The round-trip colligation

Write the Fourier--Poisson unitary as

\[
 \mathcal U=\begin{pmatrix}T&G\\H&R\end{pmatrix}:
 PH\oplus QH\longrightarrow PH\oplus QH.                  \tag{3.1}
\]

Start with a state `z in PH`.  Apply `U` with zero input:

\[
 z\longmapsto(Tz,Hz).                                      \tag{3.2}
\]

Close the output channel and apply `U*` to `(Tz,0)`:

\[
 (Tz,0)\longmapsto(T^*Tz,G^*Tz).                           \tag{3.3}
\]

Put

\[
 C=T^*T,
 \qquad a(z)=Hz,
 \qquad b(z)=G^*Tz.                                       \tag{3.4}
\]

The round-trip map

\[
 \mathcal R_{\rm rt}:z\longmapsto(Cz,a(z),b(z))            \tag{3.5}
\]

is an isometry.  Indeed, unitarity gives

\[
 \begin{aligned}
 H^*H&=I-C,\\
 (G^*T)^*(G^*T)
 &=T^*GG^*T=C-C^2,                                        \tag{3.6}
\end{aligned}
\]

and therefore

\[
 C^2+H^*H+T^*GG^*T=I.                                    \tag{3.7}
\]

Let

\[
 D_T=(I-C)^{1/2},
 \qquad D_C=(I-C^2)^{1/2}.                                \tag{3.8}
\]

Then

\[
 \boxed{D_T=(I+C)^{-1/2}D_C.}                             \tag{3.9}
\]

Thus the Julia defect of the round-trip state `C` contains exactly the
one-step Toeplitz defect, with no choice of phase.

## 4. Exact parity realization of the Schur tower

Let

\[
 H=V_HD_T,
 \qquad
 G^*T=V_GD_TC^{1/2}                                      \tag{4.1}
\]

be the two polar decompositions.  At round-trip state `C^m z`, the two
outputs have moduli

\[
 \begin{aligned}
 |a(C^mz)|&=D_TC^mz,\\
 |b(C^mz)|&=D_TC^{m+1/2}z.                                \tag{4.2}
 \end{aligned}
\]

The D.80 Schur layers are

\[
 K_jz={1\over2}D_TC^{j/2}z,
 \qquad j\ge1.                                            \tag{4.3}
\]

They split exactly as

\[
 \begin{aligned}
 K_{2m+1}z&={1\over2}V_G^*b(C^mz),&&m\ge0,\\
 K_{2m+2}z&={1\over2}V_H^*a(C^{m+1}z),&&m\ge0.            \tag{4.4}
 \end{aligned}
\]

Thus `K_+` is a fixed compression of the complete round-trip output: take
half of every `b` channel and of every `a` channel except the initial
`a(z)`.  Summing (4.4) gives

\[
 \sum_{j\ge1}\|K_jz\|^2={1\over4}\langle z,Cz\rangle.    \tag{4.5}
\]

This resolves the phase/modulus mismatch of D.84.  The single-pass
conservative output is not the Schur tower, but the doubled round-trip
output is.

## 5. Exact initial landing residual

Return to the Halmos source coordinates `(p,q)` and put

\[
 z=Vq.                                                      \tag{5.1}
\]

Completion of the Hermitian corner gives

\[
 L_-(p,q)=D_Tp-{1\over2}C^{1/2}z.                          \tag{5.2}
\]

Therefore the exact preparation residual for the round-trip state is

\[
 \boxed{
 r_0(p,q)=2D_Tp-C^{1/2}z=2L_-(p,q).}                       \tag{5.3}
\]

By (4.5), the desired domination is

\[
 \boxed{
 \|r_0(p,q)\|^2\ge\|C^{1/2}z\|^2.}                       \tag{5.4}
\]

The round-trip conservation law does not imply (5.4).  On the positive
Halmos graph

\[
 p={1\over2}D_T^{-1}C^{1/2}z                              \tag{5.5}
\]

one has `r_0=0` while the right side of (5.4) is nonzero.

At every fixed regularized cutoff, (5.5) removes the forcing algebraically.
In the directed Fourier--Poisson limit, the largest eigenvalues of `C`
tend to `1`, so `D_T^(-1)` is unbounded.  Hence the annulus class can be an
algebraic coboundary at finite level without being a bounded coboundary in
the Frechet/directed landing complex (2.1).  This is the topological
content of the prolate obstruction.

For the actual primitive A--B--C source, (5.4) is exactly

\[
 B_{\rm nuc}(F,F)\le0.                                    \tag{5.6}
\]

Thus the round trip solves the output typing, but leaves one sharply
identified input-preparation theorem.

## 6. Hermitian form on nonpolar cohomology

Reflection exchanges the two strip charts and, with complex conjugation,
induces the Tate real involution on

\[
 H^1(C_{\rm sc})=V.                                       \tag{6.1}
\]

Paugam's unconditional antisymmetric pairing

\[
 \psi:V\widehat\otimes V\longrightarrow\mathbb C(1)       \tag{6.2}
\]

combines with conjugation to give the Hermitian form

\[
 H_P(v,w)=\psi(v,C_{\rm real}w).                           \tag{6.3}
\]

This form is nondegenerate and scaling covariant, but not source-positive.
On a reflected partner pair its matrix is

\[
 \boxed{
 J_{\rm swap}=\begin{pmatrix}0&1\\1&0\end{pmatrix},}     \tag{6.4}
\]

with eigenvalues `+1` and `-1`.  Thus the two-boundary complex reproduces
the Paugam/Krein swap blocks of D.43; constructing the complex does not
select a positive half.

The ordinary positive boundary `L^2` norm also does not help: D.41 proves
that the closure of the Poisson range is all of boundary `L^2`, so its
Hilbert cokernel is zero.

## 7. Audit of periodic Yoneda positivity

Row A constructs the enriched Yoneda category of actual periodic sections
and a canonical ordered extremal frame.  The real frame realization has an
ordinary positive Euclidean form.  However, the construction is symmetric
monoidal, not a dagger/C-star category with a positive trace realizing the
row-C contact.

This distinction is forced algebraically.  Let `ell` be the nuclear contact
functional

\[
 \ell(\delta_n)=\Lambda(n).                                \tag{7.1}
\]

If it were a positive star-functional on the unital Dirichlet convolution
algebra, its Gram kernel would be

\[
 K(m,n)=\ell(\delta_m^*\!\star\delta_n)=\Lambda(mn)         \tag{7.2}
\]

under the real self-adjoint convention for the basis.  On
`{delta_1,delta_p}` this is

\[
 \boxed{
 \begin{pmatrix}
 0&\log p\\
 \log p&\log p
 \end{pmatrix},}                                          \tag{7.3}
\]

whose determinant is

\[
 - (\log p)^2<0.                                          \tag{7.4}
\]

Equivalently, positivity together with `ell(1)=0` would force `ell=0` by
Cauchy--Schwarz, contradicting `ell(delta_p)=log p`.

Therefore the periodic Yoneda realization does not provide a hidden
star-positive trace compatible with the contact.  Its positive ordered
frames certify dimensions and determinants, while the passage to the
nuclear character is necessarily graded/relative.  Adding the Gamma chart
completes the character but does not turn (7.3) into a local positive state;
the sign is the global row-D comparison.

## 8. What new datum would suffice

The constructions isolate a precise possible enhancement of row A.  It
would have to be a dagger realization

\[
 \mathcal R_\dagger:\mathsf A_{\rm per}
 \longrightarrow\mathsf{Hilb}_{\rm strip}                 \tag{8.1}
\]

with all of the following properties:

1. its two boundary fibers realize (1.1)--(1.5), not only the ordered
   extremal frames;
2. its round-trip output is the parity decomposition (4.4);
3. its preparation morphism sends the primitive source to states satisfying
   (5.4) for a categorical isometry/coisometry reason;
4. its supertrace, rather than an ordinary positive trace, is the exact
   prime--Gamma character.

Condition 3 is the genuinely new polarization datum.  It is not present in
enriched Yoneda, Day convolution, the ordered-frame functor, or Paugam
duality.  Conditions 1,2 and 4 are now already typed by the constructions
above.

## 9. Conclusion

The two-boundary scattering complex is explicit and has nonpolar
cohomology `V`.  Its annulus forcing is a landing cohomology class; finite
algebraic removal uses an inverse which becomes unbounded in the directed
limit.  Its natural Hermitian duality is Krein, not definite.

The round-trip colligation solves the phase/modulus problem completely:
its two outputs are exactly the odd and even Schur layers.  The remaining
defect is the initial residual `r_0=2L_-`, and its required domination is
row D.  Periodic Yoneda supplies no automatic positive trace capable of
proving that domination.  A new dagger preparation morphism satisfying
(5.4) is the next noncircular construction target.

