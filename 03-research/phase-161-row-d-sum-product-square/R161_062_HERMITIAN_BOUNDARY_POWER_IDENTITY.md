# R161_062 — The missing identity must be a Hermitian boundary-power law

## 0. Correction to R161_061

The symplectic form proposed in R161_061 cannot itself produce the scalar gate.  For every boundary datum `b`,

    Omega(b,b)=0.                                             (0.1)

This is algebraic and contains no arithmetic information.  Moreover, if `K_T=K_T*`, the graph of `K_T` is
Lagrangian for `Omega` for every vector, not only for a first-contact vector.  Consequently isotropy of that graph
cannot imply

    Re<g,P_R C_log g+epsilon g>=0.                            (0.2)

The use of an alternating Green form in R161_061 is therefore withdrawn as a closure argument.  Its identification
of `K_T` as a selfadjoint boundary response remains valid.

## 1. The complementary boundary form

On a doubled real or complex boundary space write `b=(xi,eta)` and introduce the Hermitian boundary-power form

    B(b,b')=<eta,xi'>+<xi,eta'>,                              (1.1)

with real part understood in the complex case.  On the diagonal,

    B(b,b)=2 Re<eta,xi>.                                      (1.2)

Thus `B`, unlike `Omega`, can carry a norm or an extremal correlation.  The two forms are the antisymmetric and
symmetric polarizations of the same ordered boundary pairing:

    <eta,xi'> = (B(b,b')+Omega(b,b'))/2.                       (1.3)

This is the precise reason that both Poisson orientations have to be retained before scalar recombination.

## 2. Tate power is not to be cancelled

For the Tate response graph `j=K_Tv`,

    B_T((v,K_Tv),(w,K_Tw))
      =<K_Tv,w>+<v,K_Tw>
      =2<v,K_Tw>,                                             (2.1)

whereas its alternating form is zero.  In particular,

    B_T((v,K_Tv),(v,K_Tv))=2<v,K_Tv>.                         (2.2)

This crossed collar term is exactly the endpoint contribution which R161_032 and R161_043 track.  It must be
retained in a boundary-power balance; declaring the Tate graph Lagrangian deletes it and loses the possible sign.
Opposite parity can make a particular mixed pairing vanish, but does not make (2.2) vanish identically.

## 3. Exact compressed power identity

Use the block notation of R161_059:

    H=PAP,  B=PZP,
    X=QAP,  Y=QZP,  Ybar=QZ*P,

with `A=A*`.  No commutation of `A` and `Z` is needed for the anticommutator calculation.  Adding the two orders
gives the exact anticommutator
identity

    boxed:
    {H,B}=P{A,Z}P-Ybar*X-X*Y.                                (3.1)

Indeed,

    HB=P AZP-PAQZP,
    BH=P ZAP-PZQAP,

and addition proves (3.1).  Taking the real diagonal pairing gives

    2 Re<Hf,Bf>
      =<f,P{A,Z}Pf>
       -Re<Ybar f,Xf>-Re<Xf,Yf>.                             (3.2)

If reflection and the parity of `f` identify the two displayed real pairings with the same sign, their sum is
`2 Re<Xf,Yf>` (with the fixed parity convention absorbed in `Y`).  Formula (3.2), not the commutator formula, is
the finite boundary-power carrier.  Its exterior term is the diagonal of (1.1), so it is capable of becoming a
leakage square.

If `H>=0` and `Hf=0`, its left side vanishes and therefore

    <f,P{A,Z}Pf>
      =Re<Ybar f,Xf>+Re<Xf,Yf>.                              (3.3)

This equality is not the earlier radical tautology: it equates an interior anticommutator current to an ordered
exterior power.  It also shows what `(PC-ren)` must compute.  Merely using `[H,B]` produces the alternating form and
cannot close the diagonal gate.

## 4. Poisson--Tate completion to be proved

For phase 161, set `Z=Z_N=S_N^ren` before causal recombination and replace `P` by the physical compression followed
by primitive projection.  The insertion of that projection adds the finite Tate response (2.2).  The candidate
identity is therefore the following *power balance*, not an isotropy law:

    boxed:
    <f,P{A_M,Z_N}Pf>
      +2<v_f,K_Tv_f>
      +P_(M,N,T)^polar(f)
     =Re<Ybar_(N,T)f,X_(M,T)f>
       +Re<X_(M,T)f,Y_(N,T)f>.                               (4.1)

Here every symbol is source-defined:

- `X_(M,T)f=Q A_M f` is the exterior Weil port;
- `Y_(N,T)f=Q Z_NPf` is the ordered integer-minus-continuum Poisson history;
- `v_f` is the two-coordinate Tate forcing;
- `P^polar` is the explicit continuum part of `H_M,N^ren`, retained before compression.

Equation (3.1) proves the uncorrected bulk identity.  To promote it to (4.1), the only bookkeeping left is the
literal decomposition of `(I-Pi_T)P_T` and of `H_M,N^ren=H_M,N-L_MC_N+[X,C_N]`; no symmetry of a fictitious
operator `PC_N` is assumed.

## 5. Required orientation and acceptance test

Let `E_N=Z_N Fcal-JZ_N` and `C_N=Z_N Fcal+JZ_N`.  By R161_041,

    U_N+V_N=Z_NM Fcal-{X,E_N},
    U_N-V_N=Z_NM Fcal-{X,C_N}.                                (5.1)

The right side of (4.1) must be expanded with `E_N` in the history slot and the covariant derivative of `C_N` in
the current slot.  Using `E_N` in both slots gives the mean orientation and fails.  The acceptance identity is

    lim_(M,N) [
      <f,P{A_M,Z_N}Pf>
      +2<v_f,K_Tv_f>+P_(M,N,T)^polar(f)
    ]
     =2 Re<g,P_R C_log g+epsilon g>.                           (5.2)

At first contact the *compressed anticommutator* on the left of (3.2) vanishes.  The full-space current on the
left of (5.2) does not vanish from radicality alone; `(PC-ren)` must show that, after its polar/Tate completion, it
is precisely that compressed anticommutator rather than the uncompressed term in (3.3).  Only then does (5.2) give
the compressed scattering gate.  Notice that (5.2) is falsifiable: the factor, sign, and the `E/C` orientation are
fixed, and all polar terms occur on the left before a limit is taken.

## 6. Status

- Lagrangian/isotropy closure proposed in R161_061: **rejected (alternating diagonal is identically zero)**;
- Hermitian boundary-power form and Tate response (1.1)--(2.2): **proved algebraically**;
- exact bulk compressed anticommutator law (3.1)--(3.3): **proved**;
- corrected finite Poisson--Tate power identity (4.1): **bulk proved, primitive/polar expansion open**;
- graph-limit identification (5.2): **open**;
- row D: **open**.
