# P123.067 — Double-bar cyclic comparison for twisted correspondences

Status: PROVED as a continuous double-complex symmetry
and an algebraic quasi-isomorphism zigzag for the indicated completed
chain spaces. No strict topological quasi-isomorphism claim is inferred.

Let A be a repaired unital algebra and M=E_beta, N=E_eta. Form the
first-quadrant bicomplex

    D_(r,s)(M,N)=M tensor_pi A^tensor r tensor_pi N tensor_pi A^tensor s.

The horizontal boundary is the two-sided bar boundary in the block
M,A,...,A,N: its first term acts on M on the right, its last term acts
on N on the left, and middle terms multiply adjacent A factors, with
signs (-1)^j for j=0,...,r. The vertical boundary is the same bar
boundary in the cyclic block N,A,...,A,M: it acts on N on the right
and on M on the left. Boundaries are zero when their bar length is zero.
All maps are continuous. The two boundaries commute, because actions
on opposite sides of a bimodule commute. With total boundary

    d=d_h+(-1)^r d_v

their mixed terms cancel and d²=0. Each total degree is a finite sum
of complete Fréchet spaces.

Rotating the two blocks and multiplying by (-1)^(rs) gives

    D_(r,s)(M,N) -> D_(s,r)(N,M),
    m tensor a_1...a_r tensor n tensor b_1...b_s
      -> (-1)^(rs) n tensor b_1...b_s tensor m tensor a_1...a_r.

Rotation exchanges d_h and d_v. For a horizontal boundary the sign
after rotation is (-1)^((r-1)s), equal to (-1)^(rs+s); for a vertical
boundary it is (-1)^(r+r(s-1))=(-1)^(rs). These are exactly the signs
of the rotated total differential. Thus this is a continuous chain
isomorphism and its square is identity.

Augment the horizontal bar to the completed balanced tensor M tensor_A N.
The resulting vertical complex is the Hochschild complex
C_*(A,M tensor_A N) of P123.066, since its two endpoint operations are
the outer right N and left M actions. This augmentation is a continuous
map from the total double-bar complex.

For fixed s, the horizontal augmented bar is continuously contractible
as a complex of underlying spaces. To see this, identify M as a free
right A-module by m -> beta^-1(m). In these coordinates the contraction
inserts the free right-module unit before its coefficient, exactly as
the contracted bar resolution in P123.066. Tensoring with the trailing
A factors preserves this displayed linear contraction. The completed
balanced augmentation is identified with N in the same coordinates.
Thus horizontal homology is zero in positive degree and is the stated
balanced tensor in degree zero.

The first-quadrant filtration of the total complex consequently proves
that augmentation is an algebraic quasi-isomorphism of these completed
chain spaces. Convergence requires no infinite-degree summation: every
total degree has finitely many filtration pieces. Rotating first and
using N as a free right module gives the second augmentation. We obtain
the explicit continuous zigzag

    C_*(A,M tensor_A N) <- Tot D(M,N)
         ~= Tot D(N,M) -> C_*(A,N tensor_A M),

whose augmentation arrows induce isomorphisms on algebraic homology.
The filtration argument alone does not prove that those isomorphisms
preserve quotient homology topologies or are equivalences for every
strict exact structure. In particular no closure of all boundaries is
silently assumed.

Finite direct sums of the twisted modules have the same argument
componentwise. Bounded complexes use the additional internal degrees
and Koszul signs; the internal filtration is finite in each total degree,
so the same augmentation argument applies. This supplies a derived
cyclic comparison for the objects constructed in P123.064 at the stated
level. In degree zero its rotation agrees with P123.065.

For A.5, this still needs a suitable topological target where the zigzag
is an admissible equivalence and where the demanded determinant or
nuclear trace is defined. Algebra-extension excision, geometric descent,+and mixed RR are not consequences of the block rotation. They remain
separate requirements before row A can be declared complete.
