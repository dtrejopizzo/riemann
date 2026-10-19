# R161_063 — Exact nested-compression decomposition of the Poisson--Tate power

## 1. Three orthogonal blocks

Let `P=P_T` be physical compression and `Pi=Pi_T<=P` the primitive projection.  Put

    R=P-Pi,          Q=I-P,          I=Pi+R+Q.              (1.1)

Thus `R` is the two-dimensional Tate block and `Q` is the true exterior.  Let `A=A*`, let `Z` preserve the finite
common core (commutation is not required), and define on `Pi H`

    H=Pi A Pi,       B=Pi Z Pi.                              (1.2)

For `f in Pi H`, set the oriented ports

    x_R=R A f,       y_R=R Z f,       ybar_R=R Z* f,
    x_Q=Q A f,       y_Q=Q Z f,       ybar_Q=Q Z* f.          (1.3)

## 2. Exact identity

Insertion of (1.1), exactly as in R161_062(3.1), gives

    boxed:
    2 Re<Hf,Bf>
      =<f,Pi{A,Z}Pi f>
       -P_R(f)-P_Q(f),                                      (2.1)

where

    P_R(f)=Re<ybar_R,x_R>+Re<x_R,y_R>,                       (2.2)

    P_Q(f)=Re<ybar_Q,x_Q>+Re<x_Q,y_Q>.                       (2.3)

Proof: use `I-Pi=R+Q` in

    {H,B}=Pi{A,Z}Pi
      -Pi Z(R+Q)A Pi-Pi A(R+Q)Z Pi

and take the real diagonal pairing.  Orthogonality of `R` and `Q` gives (2.1)--(2.3), with no mixed Tate/exterior
term.

If `H>=0` and `f` is a first-contact radical, `Hf=0`, hence

    boxed:
    <f,Pi{A,Z}Pi f>=P_R(f)+P_Q(f).                           (2.4)

This is the exact finite power balance forced by radicality.

## 3. Typing audit: the diagonal Tate block is not the crossed collar

The first-contact equation gives `x_R=RAf=r_f`, the Tate forcing.  However R161_009 does **not** identify `RZf`
with the crossed response `K_Tv_f`.  Its collar current occurs in the canonical product-port pullback

    y=Z* g,       R y=Tau_T P_T Z* g,                         (3.1)

of R161_022.  This second vector depends linearly on `f` through `g`, but it is not `Zf`.  Therefore the claim

    P_R(f)=2<v_f,K_Tv_f>                                    (3.2)

made in the first version of this note was ill-typed and is withdrawn.  The convention-free diagonal expression
(2.2) remains exact, but it is not the established Tate collar.

For the correctly typed mixed pair `(f,y)`, the endpoint term is instead

    Re<r_f,Ry>=Re<v_f,G_TCv_f>.                              (3.3)

After multiplication by the parity sign `epsilon`, R161_032 turns (3.3) into `||r_f||^2`.  Thus the crossed Tate
power belongs to a **mixed Hermitian polarization**, not to the diagonal anticommutator (2.1).

## 4. Consequence for the diagonal target

Take now

    A=A_M,             Z=Z_N=S_N^ren.                        (4.1)

The finite bulk term is

    I_(M,N,T)(f):=<f,Pi{A_M,Z_N}Pi f>.                        (4.2)

At finite `M`, (2.1), rather than its radical specialization (2.4), gives

    I_(M,N,T)(f)-P_R(f)-P_Q(f)
      =2 Re<H_Mf,B_Nf>,                                      (4.3)

where `H_M=Pi A_MPi` and `B_N=Pi Z_NPi`.  The right side tends to zero only after the common-graph convergence
`A_M -> A_infinity` is combined with the first-contact equation `Pi A_infinity Pi f=0`; it is not zero at a fixed
finite `M`.

The formerly proposed identification

    P_Q(f)=2 Re<g_(M,N,T),
                   P_R^ext C_log g_(M,N,T)+epsilon g_(M,N,T)>
              +Rem_(M,N,T)(f)                                (4.4)

has no justification because its left side uses `Z_Nf`, while its right side uses the product port `g(f)`.  It is
withdrawn.  Any valid successor must use the mixed pair `(f,Z_N* g(f))` from the outset.

Equation (4.3) is narrower than the proposal in R161_062: the primitive/Tate part is now an exact theorem, and the
only unresolved calculation is the identification of the genuine exterior power `P_Q` with the compressed
scattering power.  No assertion that the global current (4.2) vanishes has been made.

## 5. Correct mixed compression identity

Let `y=Z* g(f)` and decompose

    Af=Pi Af+r+ell,       y=Pi y+Ry+Qy.                       (5.1)

On a first-contact radical `Pi Af=0`, hence the literal orthogonal decomposition is

    boxed:
    Re<Af,y>=Re<r,Ry>+Re<ell,Qy>.                             (5.2)

This is exactly the first two terms in R161_022(3.3).  Adding the functional-equation exterior defect `d` gives
the third term and reconstructs the full extremal correlation.  Therefore (5.2) by itself is the already audited
canonical-pullback decomposition, not a new vanishing law.

The surviving target is consequently sharper: the two adjointed `(PC-ren)` orientations must annihilate the
complete mixed power

    Re<r,Ry>+Re<ell,Qy>+Re<d,y>,                              (5.3)

without merely reconstructing `Re<y,w>`.  This is the exterior reciprocity already isolated in R161_022; the
diagonal anticommutator does not prove it.

## 6. Status

- exact three-block boundary-power identity (2.1)--(2.4): **proved**;
- isolation of the Tate and true exterior powers without mixed terms: **proved**;
- diagonal identification of `RZ_Nf` with the crossed collar: **rejected / ill-typed**;
- correctly typed mixed Tate pairing (3.3): **proved by R161_009 and R161_022**;
- mixed decomposition (5.2): **proved, but coincides with the audited pullback decomposition**;
- annihilation of the complete mixed power (5.3): **open / terminal**;
- row D: **open**.
