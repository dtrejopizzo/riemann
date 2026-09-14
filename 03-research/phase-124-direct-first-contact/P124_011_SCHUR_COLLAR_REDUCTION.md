# P124.011 -- Schur reduction of the Tate collar at first contact

Status: `EXACT REDUCTION / COLLAR IS A CONCRETE CROSSBLOCK, NOT YET CONTROLLED`.

This note translates the D.190 Schur/Douglas block calculus into the actual
phase-124 objects

\[
        q_T(F,G)=\langle L_TF,G\rangle,
        \qquad L_T=P_T\mathscr A_TP_T,
        \qquad
        J_+(F)=\langle\rho_{+,T},F\rangle .         \tag{0.1}
\]

The result is a sharp reduction.  The Tate collar is a genuine
primitive--Tate crossblock.  A Schur complement would control it exactly if
one had positivity of the primitive space enlarged by the relevant Tate
port.  But the positivity already proved at first contact is only
`q_T>=0` on primitives.  It does not include this augmented block, and the
missing range condition is precisely the desired collar cancellation on the
first-contact radical.

No zero/RH input is used.  No new paper file is touched.

## 1. The collar as the primitive--Tate column

Let

\[
        \phi_+(t)=e^{t/2},\qquad \phi_-(t)=e^{-t/2},
        \qquad \mathcal P_T=\{M_+(F)=M_-(F)=0\}.
\]

P124.005 gives the exact primitive collar formula

\[
        J_+(F)=M_+(\mathscr A_TF)
              =\langle\rho_{+,T},F\rangle,
        \qquad F\in\mathcal P_T,                   \tag{1.1}
\]

where

\[
        \rho_{+,T}=P_T(e^{t/2}\Phi_{+,T}).          \tag{1.2}
\]

Equivalently, in the block matrix of the unprojected closed form
`mathscr A_T` relative to

\[
        \mathcal P_T\oplus \operatorname{span}\{\phi_+,\phi_-\},
\]

`rho_(+,T)` is the primitive component of the column paired with the Tate
port `phi_+`:

\[
        P_T\mathscr A_T^*\phi_+=\rho_{+,T}.         \tag{1.3}
\]

Thus the desired first-contact conclusion is not a hidden regularity
statement.  It is the vanishing of a concrete crossblock on the primitive
nullspace:

\[
        J_+(F_*)=0
        \quad\Longleftrightarrow\quad
        \langle\rho_{+,T},F_*\rangle=0.             \tag{1.4}
\]

In a parity branch this is exactly `c=0` by P124.005(3.6).

## 2. First-contact spectral split

At a first contact, P122.002 supplies

\[
        L_T\ge0,
        \qquad L_TF_*=0
        \quad\text{for some }0\ne F_*\in\mathcal P_T. \tag{2.1}
\]

In the compactly whitened realization of P122.002, the zero eigenspace

\[
        K_T:=\ker L_T                                      \tag{2.2}
\]

is finite-dimensional and isolated from the positive part.  Let
`Pi_K` be the orthogonal projection onto `K_T`, and write

\[
        \rho_{+,T}=\rho_K+\rho_R,
        \qquad
        \rho_K=\Pi_K\rho_{+,T},
        \qquad
        \rho_R=(I-\Pi_K)\rho_{+,T}.                 \tag{2.3}
\]

Then the first-contact collar is exactly

\[
        J_+(F_*)=\langle\rho_K,F_*\rangle
        \qquad(F_*\in K_T).                         \tag{2.4}
\]

Consequently,

\[
\boxed{
        J_+(F)=0\text{ for every first-contact radical }F\in K_T
        \quad\Longleftrightarrow\quad
        \rho_K=0.}
        \tag{2.5}
\]

This is the first Schur range condition.  It is also the form-range
condition

\[
        \rho_{+,T}\in\overline{\operatorname{Ran} L_T}.
        \tag{2.6}
\]

The stronger estimate

\[
        |\langle\rho_{+,T},F\rangle|^2
        \le C_T q_T(F,F)                            \tag{2.7}
\]

is equivalent to the stronger form condition

\[
        \rho_{+,T}\in\operatorname{Ran}L_T^{1/2},   \tag{2.8}
\]

with best constant, taken on `K_T^perp`,

\[
        C_T^{\rm best}=\|L_T^{\dagger/2}\rho_{+,T}\|^2 .
        \tag{2.9}
\]

Thus any proof of (2.7) already contains the collar
annihilation (2.5).

## 3. The exact Schur complement

Adjoin one scalar Tate port to the primitive form and define, for a real
number `d`,

\[
        \mathcal M_{+,d}(F,z)
        =q_T(F,F)+2\operatorname{Re}\,\overline z\,
          \langle\rho_{+,T},F\rangle+d|z|^2.        \tag{3.1}
\]

This is the principal two-block test for the primitive space plus the
`phi_+` collar port.  The standard closed-form Schur/Douglas theorem gives

\[
\boxed{
        \mathcal M_{+,d}\ge0
        \Longleftrightarrow
        \rho_K=0
        \text{ and }
        d\ge\langle L_T^\dagger\rho_R,\rho_R\rangle .}
        \tag{3.2}
\]

Equivalently, there is a contraction/factorization

\[
        \rho_{+,T}=L_T^{1/2}h,
        \qquad \|h\|^2\le d,                        \tag{3.3}
\]

with `h=L_T^{\dagger/2}\rho_R` at the sharp value.  Formula (3.2) is D.190
with

\[
        A_O=L_T|_{K_T^\perp},
        \qquad X_{OE}=\rho_R,
        \qquad B_E=d,                               \tag{3.4}
\]

and with the range obstruction `rho_K=0` made explicit.

The equality conditions are equally rigid.  If (3.2) holds, then a null
vector `(F,z)` of `mathcal M_(+,d)` satisfies

\[
        L_T^{1/2}F+z h=0,                            \tag{3.5}
\]

and

\[
        (d-\|h\|^2)z=0.                              \tag{3.6}
\]

Its component in `K_T` is free only because `rho_K=0`; it does not carry
collar current.  If `z=0`, the null vectors are exactly the first-contact
radicals in `K_T`, and their collar vanishes by the range condition.  If
`z\ne0`, equality also forces the scalar Schur complement to be sharp:

\[
        d=\langle L_T^\dagger\rho_R,
                \rho_R\rangle .                    \tag{3.7}
\]

Thus Schur equality does not produce a hidden first-contact law.  It states
precisely the law one needs: no projection of `rho_(+,T)` onto `ker L_T`,
plus the finite positive budget (3.7) on the range part.

## 4. Relation with D.190 and the causal blocks

D.190 proves the exact causal identity

\[
        P_OQ_TP_E=[P_O,Q_T]P_E,                     \tag{4.1}
\]

and the sharp Douglas criterion

\[
        X_{OE}=A_O^{1/2}C_{OE},
        \qquad C_{OE}^*C_{OE}\le B_E                \tag{4.2}
\]

if and only if the old-plus-shell block of the target form is positive.
For the collar test, the role of the shell is not a newly born spatial
cell.  It is the finite Tate port.  The crossblock is not approximate:

\[
        X_{O,E_+}=\rho_{+,T}.                       \tag{4.3}
\]

Therefore D.190 translates into the Schur complement (3.2).  The two-Tate
projection affects only the finite Tate block and the two columns
`rho_(+,T),rho_(-,T)`; it does not alter the infinite primitive operator
`L_T` except through the already imposed primitive compression.

What is already proved is the first-contact primitive positivity
`L_T>=0`.  What is not proved is positivity of the enlarged matrix

\[
        \begin{pmatrix}
        L_T&\rho_{+,T}\\
        \rho_{+,T}^*&d
        \end{pmatrix}.                              \tag{4.4}
\]

Positivity of (4.4) is exactly equivalent to the range condition and Schur
budget in (3.2).  In particular, if `rho_K\ne0`, no choice of finite `d`
can make (4.4) positive: taking `F in K_T` leaves a zero diagonal primitive
entry and a nonzero cross term.

This is why the D.190 theorem cannot be used here as a free estimate.  Its
constant-one factorization would prove the collar cancellation, but only
because it already includes the missing range condition.

## 5. Why the positive reference energy does not close the collar

Phase 120 and P122.002 use the decomposition

\[
        q_T(F,F)=\mathcal R_T(F,F)-\|\mathcal W_TF\|^2, \tag{5.1}
\]

where `mathcal R_T` is the positive Gamma/antisymmetric reference energy.
The reference energy gives ordinary Cauchy bounds for any continuous collar
functional:

\[
        |J_+(F)|^2\le C_R\,\mathcal R_T(F,F).       \tag{5.2}
\]

At first contact, however,

\[
        q_T(F_*,F_*)=0
        \quad\Longleftrightarrow\quad
        \mathcal R_T(F_*,F_*)=\|\mathcal W_TF_*\|^2, \tag{5.3}
\]

not `mathcal R_T(F_*,F_*)=0`.  Thus (5.2) leaves a live residual exactly at
first contact.  Passing from (5.2) to the needed estimate

\[
        |J_+(F)|^2\le C_Tq_T(F,F)                   \tag{5.4}
\]

is the same shorting problem as D.190:

\[
        B_E-X^*A_O^\dagger X\ge0.                  \tag{5.5}
\]

The positive reference carré-du-champ controls the ambient block before the
load `W_T^*W_T` is subtracted.  The collar route needs the already-shorted
primitive block after that subtraction.  This is precisely the residual
identified in D.190, not a consequence of the proved reference positivity.

## 6. Verdict

The collar is a concrete D.190 crossblock:

\[
        X_{O,E_+}=\rho_{+,T}=P_T(e^{t/2}\Phi_{+,T}). \tag{6.1}
\]

At first contact, the exact obstruction is its kernel projection

\[
        \Pi_{\ker L_T}\rho_{+,T}.                   \tag{6.2}
\]

The desired `c=0` conclusion on a parity branch is equivalent to the
vanishing of (6.2) on that branch.  A Schur/Douglas estimate would prove it
if one could establish positivity of the primitive-plus-Tate augmented
block, or equivalently the range condition
`rho_(+,T) in Ran L_T^(1/2)`.  But that is not supplied by the positivity
already proved in phases 118--123.  The known positive reference energy
bounds `rho` before shorting; first contact lives exactly at the point
where the reference energy equals the load energy and can remain nonzero.

So the next admissible theorem is now sharply identified: prove the
specific range/shorting statement for the actual collar column
`rho_(+,T)`, not a generic leakage bound and not the D.190 constant-one
factorization assumed as a black box.
