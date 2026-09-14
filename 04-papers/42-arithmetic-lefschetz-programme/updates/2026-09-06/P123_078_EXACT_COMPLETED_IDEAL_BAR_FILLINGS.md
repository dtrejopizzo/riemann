# P123.078 — Exact fillings in the completed reduced bar of the rapid ideal

Date: 2026-09-06. Status: PROVED for the rapid C_0 ideal of P123.019,
also after completed projective tensor with a Fréchet space. Continuous
linear splitting and full-source excision are not assumed.

Let I be that ideal, with increasing submultiplicative seminorms p_k.
Its approximate identity u_alpha from P123.031 satisfies p_k(u_alpha)<=1
for every k, and left multiplication L_(u_alpha) converges strongly to
identity. Define the nonunital reduced bar with

    B_n(I)=I^(tensor_pi n), n>=1, B_0=0,
    b'(x_1 tensor ... tensor x_n)
       =sum_(j=1)^(n-1) (-1)^(j-1) x_1 tensor ... tensor
                         x_j x_(j+1) tensor ... tensor x_n.

Write q_k for the corresponding increasing projective seminorms in
each degree. Insertion h_alpha(z)=u_alpha tensor z has
q_k(h_alpha z)<=q_k(z). Cancellation of adjacent multiplication terms
gives the exact identity

    b' h_alpha+h_alpha b'=L_(u_alpha) tensor id^(tensor(n-1)). (1)

The right side converges strongly to identity on B_n(I). Indeed this
holds on elementary tensors, and the maps are uniformly bounded in
each q_k, so it extends by density. This much alone proves only density
of boundaries in cycles. The following construction gives exactness.

Fix a cycle z in B_n(I). Set r_0=z. Inductively choose alpha_j so that
for every k<=j,

    q_k((1-L_(u_alpha_j) tensor id)r_j)<=2^(-j-1).

There are finitely many conditions at each step, so strong convergence
permits the choice. Put

    y_j=h_alpha_j r_j,
    r_(j+1)=r_j-b' y_j.

By (1), r_(j+1)=(1-L_(u_alpha_j) tensor id)r_j; it is again a cycle
because b'²=0. For every fixed k, q_k(r_j)<=2^-j for all sufficiently
large j. The insertion estimate gives the same eventual bound for
q_k(y_j). Consequently y=sum_(j>=0)y_j converges in the complete space
B_(n+1)(I), and continuity plus telescoping yields

    b'y=z-lim_j r_j=z.

Thus every cycle is an actual boundary in every positive bar degree.
In degree one the argument also proves actual completed-tensor
surjectivity of multiplication I tensor_pi I -> I; it does not claim
that each element is one algebraic product.

The boundary image equals the kernel of the next continuous boundary,
so it is closed. Surjection from B_(n+1)(I) onto this closed Fréchet
kernel is open by the Fréchet open mapping theorem; hence the bar
complex is strictly exact in the topological sense. The selection of
alpha_j depends on z. No continuous linear contracting homotopy or
linear section is supplied by this construction.

For any complete Fréchet space V, repeat the argument on
V tensor_pi B_n(I), inserting u_alpha immediately after the V factor.
Use a countable increasing cofinal family of projective seminorms.
Insertion has the same bound, the identity (1) is unchanged, and strong
convergence follows from elementary tensors and uniform bounds. The
same diagonal geometric-series construction fills every cycle exactly.
Thus strict exactness persists after tensoring with any such V.

This gives the completed ideal-bar acyclicity needed for an excision
argument, substantially stronger than the degree-one closure calculation
in P123.077. It does not itself identify the full-source Tate bar complex
with its scalar quotient: that requires the relative word filtration
and comparison maps. Nor does strict exactness automatically mean
admissibility in the continuously linearly split exact structure of
P123.066. That distinction must be respected when translating the result
into the determinant or trace category required by A.
