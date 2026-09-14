# P122 -- naive global determinant assembly is exactly the target form

## Status

`PROVED-IN-REPOSITORY` as a no-go theorem.  The local line of P122.013 is a
valid new source object, but merely tensoring all positive source lines and
dualizing all negative source lines produces a determinant curvature whose
semipositivity is exactly row (d).  That assembly is a geometric packaging
of the known positive-minus-positive factorization, not its proof.

This prevents the local construction from silently restarting the retired
phase-120 positive-lift programme.

## 1. Universal graph-determinant calculation

Let `V` and `W` be complex Hilbert spaces and let `J:V -> W` be bounded.
For `F in V`, define a rank-one Hilbert--Schmidt graph coordinate

\[
 Z_Fx=\langle x,e_0\rangle JF.                     \tag{1.1}
\]

Pulling the dual tautological determinant line back along
`F -> graph(Z_F)` gives the metric

\[
 \|s(F)\|^2={1\over\det(1+Z_F^*Z_F)}
            ={1\over1+\|JF\|^2}.                  \tag{1.2}
\]

At the undeformed point its Chern curvature is

\[
                         \Theta_0(u,\bar v)
                         =\langle Ju,Jv\rangle.    \tag{1.3}
\]

Thus the graph-determinant functor turns any already constructed Gram
column into its quadratic form.  It does not determine a comparison
between two different columns.

## 2. Application to the balanced Weil factorization

On the primitive compact-window space, the audited factorization is

\[
 q_T(F)=-B_{\rm nuc,T}(F,F)
       =\|X_TF\|^2-\|Y_TF\|^2,                    \tag{2.1}
\]

where the columns may be taken in the balanced, seam or causal-storage
coordinates of phases 119--120.  All such choices are related by proved
isometries on their stated source ranges.

Let `L_(X,T)` and `L_(Y,T)` be their graph-determinant lines from (1.2), and
form the oriented virtual line

\[
                 L_T^{\rm vir}=L_{X,T}\otimes L_{Y,T}^{\vee}. \tag{2.2}
\]

Curvature is additive under tensor product and changes sign under duality,
so

\[
 \Theta_{L_T^{\rm vir},0}(F,\bar F)
 =\|X_TF\|^2-\|Y_TF\|^2=q_T(F).                  \tag{2.3}
\]

Consequently

\[
 L_T^{\rm vir}\text{ semipositive at the base point}
 \quad\Longleftrightarrow\quad q_T\ge0.            \tag{2.4}
\]

For every `T`, (2.4) is precisely the finite-window row-(d) assertion.
Taking the cofinal system gives the original Weil positivity criterion.

## 3. Why first-contact null curvature is insufficient

At first contact a nonzero hypothetical `F_*` satisfies

\[
 q_{T_*}(F_*)=0,
 \qquad \|X_{T_*}F_*\|=\|Y_{T_*}F_*\|.            \tag{3.1}
\]

By (2.3), `F_*` is a null curvature direction of the virtual determinant
line.  This says only that two nonzero positive curvatures cancel.  It does
not imply

\[
 X_{T_*}F_*=0,
 \qquad Y_{T_*}F_*=0.                              \tag{3.2}
\]

A two-dimensional model, `X=Y=I`, has identically zero virtual curvature
and arbitrarily many nonzero states, so no determinant-line formalism can
infer (3.2) from (3.1) alone.

## 4. Consequences for P122.013

The local Euler line remains useful because it is not obtained from an
arbitrary factorization: its graph coordinate is forced by the
degree-one Euler logarithmic connection, it changes to the dual under port
swap, and its rank distinguishes degree one from the shifted pair.

But the following continuation is forbidden:

```text
tensor the known Gamma positive lines
  with the dual local Euler lines
  -> observe that their virtual curvature is q_T
  -> assert semipositivity or flatness.
```

The last assertion is row (d) by (2.4).  Calling it a Quillen positivity,
Calderon contraction, determinant stability or Hodge metric does not change
the equivalence.

The only admissible continuation must add a theorem not present in (2.1):

1. a source-derived determinant **trivialization** whose anomaly formula
   forces the two-port equality before taking curvature;
2. a nonabelian central-extension law which constrains the oriented local
   lines beyond their scalar tensor product; or
3. a genuine Hodge/Riemann--Roch theorem on a newly constructed global
   carrier, with hypotheses verified independently of (2.3).

## 5. Updated construction boundary

P122.013 solves the local orientation/curvature problem.  This note proves
that the global operation cannot be ordinary tensor assembly.  The open
object must therefore contain additional global morphism data:

\[
 \boxed{\text{local determinant lines}
   +\text{ source trivialization/central extension law}
   +\text{ Gamma--Tate anomaly theorem}.}          \tag{5.1}
\]

Only the first term in (5.1) currently exists.  The other two, not the
formal determinant line itself, are the mathematical content still needed
for D.
