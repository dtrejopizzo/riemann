# R170_877 — PC cancellation of the derivation defect and extraction obstruction

## 0. Result

Comparing the two orientations of the factor swap has two
distinct levels.

1. **Before causal extraction**, all Chebyshev defects and the
   second jets cancel within PC. Only the swap-even physical defect
   remains:
   \[
   \mathfrak O=SA_L-LA_S
   =(S-L)\mathcal M+LS^*-SL^*.                             \tag{0.1}
   \]
2. **After extraction**, the swap is no longer defined. The
   integer orientation uses
   \[
   h_S=(PS^*P)^{-1}b,                                     \tag{0.2}
   \]
   but the swapped orientation would require
   \[
   h_L=(PL^*P)^{-1}b.                                     \tag{0.3}
   \]
   Since \(\Lambda(1)=0\), `L` has no identity component and
   `PL^*P` is strictly triangular/nilpotent in the finite causal model;
   it is not invertible.

Hence there is no involution of the extracted Tate port that literally
realizes the factor swap. The sign law must be formulated before
inverting `PS^*P`, and the result then transported through the only
invertible causal orientation.

## 1. Two oriented PC identities

For a causal synthesis `B` set

\[
 K_B:=-[X,B].                                              \tag{1.1}
\]

In particular,

\[
 K_S=\sum_{n\le N}{\log n\over\sqrt n}\tau_{\log n},
 \qquad
 K_L=\sum_{n\le N}{\Lambda(n)\log n\over\sqrt n}
                         \tau_{\log n}.                    \tag{1.2}
\]

Define

\[
 D_K:=K_S-K_L.                                             \tag{1.3}
\]

The two oriented hyperbolas are

\[
 H_{L,S}=LS-K_S,\qquad H_{S,L}=SL-K_L.                     \tag{1.4}
\]

Since `LS=SL`, one has exactly

\[
 \boxed{H_{L,S}-H_{S,L}=-D_K.}                            \tag{1.5}
\]

## 2. Complete cancellation of `D_K`

In the difference of the `X/E` blocks of the two PC identities there appears

\[
 X_S-X_L=(S-L)\mathcal M-D_K-JD_K\mathscr F.              \tag{2.1}
\]

The difference of the hyperbolic branches

\[
 -JH\mathscr F-H                                          \tag{2.2}
\]

contributes, by (1.5),

\[
 +JD_K\mathscr F+D_K.                                     \tag{2.3}
\]

Equations (2.1) and (2.3) cancel `D_K` and its reflected copy with no
residue. The remaining block satisfies

\[
 -L^*E_S\mathscr F+S^*E_L\mathscr F=LS^*-SL^*,            \tag{2.4}
\]

using

\[
 E_B\mathscr F=B-JB\mathscr F,\qquad
 L^*J=JL,\qquad S^*J=JS,\qquad LS=SL.                     \tag{2.5}
\]

Summing (2.1)--(2.4) leaves precisely (0.1). Thus PC produces no
additional arithmetic residue when comparing orientations.

## 3. The cancellation survives differentiation

For the antidiagonal derivation of R170_847,

\[
 K_{B,-}=2K_B+K_B^{(2,\partial)}.                          \tag{3.1}
\]

Set `D_K,-=K_S,--K_L,-`. The derivative of (2.1) contains
`-D_K,--J D_K,- Fcal`, while the derivative of (2.3) contains the
opposites. Hence the terminal atoms and the full second jet also
cancel. This is the two-orientation version of
R170_856(0.2), (3.3)--(3.4).

Retaining `D_K,-` after this sum would repeat the partial cancellation
that R170_856 corrected.

The only defect before renormalizing is

\[
\boxed{
\begin{aligned}
 \partial_-\mathfrak O={}&
 (S+L)\dot{\mathcal M}-(\dot S+\dot L)\mathcal M\\
 &+\dot S L^*-S\dot L^*+\dot L S^*-L\dot S^*.
                                                               \tag{3.2}
\end{aligned}}
\]

It is swap-even: swapping `L,S` leaves (3.2) fixed. It also contains a
bare copy of `dot M` coming from the unit term of `S` and from
`Lambda(1)=0`; hence it cannot vanish as an operator identity.

The continuum `C_N` is canonically attached to the integer comb `S_N`; the
corpus does not build a continuum `C_Lambda` for `L_N`. If a symmetric
extension is forced using the same `C_N` on both legs, the renormalized
version adds

\[
 -\mathcal P_C(A_L)-\mathcal P_C(A_S),\qquad
 \mathcal P_C(A):=C\dot A-\dot C A.                        \tag{3.3}
\]

This formula is conditional on that new choice. If the physical
renormalization is kept only on the integer leg, the term is

\[
 -\mathcal P_C(A_L).                                       \tag{3.4}
\]

No variant vanishes formally; the first is not canonical without
constructing `C_Lambda`.

## 4. No-symmetric-extraction theorem

On the bounded window, order the translations by causal direction.
Then

\[
 S=I+N_S,                                                  \tag{4.1}
\]

with `N_S` strictly triangular. Hence `PS^*P` has identity diagonal
and is invertible on the window; this is the inversion of R170_849--853.

By contrast,

\[
 L=N_L,                                                    \tag{4.2}
\]

because its coefficient at `n=1` is `Lambda(1)=0`. Every translate of `L^*`
shifts by at least `log 2` in the same direction. By support, if
`m log 2>2T`,

\[
 (PL^*P)^m=0.                                              \tag{4.3}
\]

for some `m`, so that

\[
 \boxed{PL^*P\text{ is not invertible.}}                   \tag{4.4}
\]

Hence (0.3) does not exist in general. Causal extraction irreversibly
distinguishes the leg with unit coefficient. This asymmetry uses an
exact value of integer arithmetic, not merely positivity or support on
prime powers.

## 5. New minimal form of the law

The exterior vanishing cannot be proved by comparing two already
extracted ports. The comparison must be carried out in the PC complex
prior to inversion, where (3.2)--(3.4) are exact, and only then apply
the causal resolvent `C^{-1}=(PS^*P)^{-1}` of the integer orientation.

The remaining door reduces to showing that, on a first-contact
vector, the boundary-augmented class of

\[
 \boxed{
 \partial_-\mathfrak O-\mathcal P_C(A_L)}                 \tag{5.1}
\]

coincides with `-beta_phys`. A bilateral version with
`-P_C(A_L)-P_C(A_S)` would require first building the continuum of the
swapped leg. If (5.1) comes out of the full PC identity,
then its sum with the exterior Wronskian of R170_853 vanishes before
extraction and causal inversion transports that vanishing to the
physical port.

Equality (5.1) remains open; it now has all Chebyshev terms,
`K2`, and atoms cancelled, and it does not require a nonexistent inverse.

## 6. Status

```text
difference of hyperbolas = -D_K                            PROVED
complete PC cancellation of D_K and its reflection          PROVED
cancellation of the second jet and atoms under differentiation PROVED
residual swap-even defect, equation (3.2)                   PROVED
polar continuum of the swapped leg                           NOT CANONICAL
PL*P invertible after the swap                               REFUTED
exact origin Lambda(1)=0 of the obstruction                  PROVED
pre-extraction law (5.1)                                      FORMULATED / OPEN
VIR--LB / D                                                   OPEN
```
