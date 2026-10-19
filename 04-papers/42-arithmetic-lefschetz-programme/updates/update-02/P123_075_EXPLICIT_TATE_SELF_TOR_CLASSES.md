# P123.075 — Explicit self-Tor classes at the repaired Tate fibers

Status: PROVED for continuous relative bar homology.
This computes a nonzero part of the Tate base-change defect required
by mixed RR, not the full determinant comparison.

Use the repaired algebra A with scalar quotient e:A -> D. For a scalar
character lambda:Gamma_S -> C^* of at most height-polynomial growth,
define the continuous augmentation

    chi(a)=sum_gamma e(a)_gamma lambda(gamma).

The two Tate choices lambda(gamma)=gamma^(1/2) and gamma^(-1/2) satisfy
this growth condition. They are defined here through the repaired scalar
quotient, without asserting that they already realize the physical
external ruling functor. Let J=ker chi.

The continuously split decomposition A=C1 direct_sum J gives the
normalized reduced bar complex for C_chi tensor_A^L C_chi in the
split relative exact structure:

    B_n=J^(tensor_pi n),  B_0=C,
    d_1=0,  d_2(x tensor y)=-xy.

It is obtained from the ordinary augmented bar by removing unit
degeneracies; insertion of 1 gives their continuous contraction. Higher
boundaries multiply neighboring augmentation-ideal factors with the
usual signs. In degree one the reduced homology is therefore

    J / closure(span J²).

For each p in S_f define a continuous functional on A by

    ell_p(a)=sum_gamma v_p(gamma)e(a)_gamma lambda(gamma).

Continuity follows from |v_p(gamma)|<=log H(gamma)/log p and the rapid
seminorms. Multiplicativity of e and additivity of v_p give the exact
augmentation-derivation identity

    ell_p(ab)=chi(a)ell_p(b)+ell_p(a)chi(b).

Consequently ell_p vanishes on J² and its closure. The elements

    z_q=lambda(q)^-1 U_q-1 in J

satisfy ell_p(z_q)=1 for p=q and 0 otherwise. They define linearly
independent reduced Tor_1 classes. Moreover the maps

    C^S -> J/closure(J²),  (c_p) -> sum_p c_p[z_p],
    J/closure(J²) -> C^S,  [a] -> (ell_p(a))_p

are continuous and compose to identity. Thus the Tate self-Tor contains
an explicit split |S_f|-dimensional subspace, not only an abstract
nonvanishing assertion. All formulas also detect the same independent
classes in unreduced algebraic bar homology.

Under repaired chart maps S contained in T, the augmentations commute,
old z_p map to the same z_p, and the old ell_p remain unchanged. Each
new prime ell contributes a new class z_ell, detected by ell_ell and
annihilated by every old ell_p. This is a concrete chart-compatible
family of excess classes. It is a lower bound, not a calculation of
the complete self-Tor group: other source contributions are not excluded.

In particular the multiplication map from this derived self-tensor to
C cannot be an equivalence, since its target has no degree-one homology.
The ruling fiber comparison must retain a nontrivial relative defect.
It cannot assume the Tate character is a homological epimorphism and
then use that assumption to identify mixed composition determinants.

The next required RR calculation is the full relevant relative object,
its admissible determinant or nuclear regularization, and its natural
comparison with mixed source composition. The displayed classes specify
part of that correction and its semilocal behavior. They do not prove
its finite perfectness, compute a global determinant, or close A.8.
