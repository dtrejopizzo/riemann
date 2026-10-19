# P123.066 — A relative completed resolution of the source diagonal

Status: PROVED for the explicitly split exact structure
below. This constructs a derived diagonal complex, not its determinant,
nuclear realization or general nonsplit excision.

Let A be one of the repaired unital Fréchet algebras. Consider complete
Fréchet A-bimodules and those short exact sequences that split by a
continuous linear map after forgetting the A actions. This is the exact
structure used here. The splitting need not be a bimodule map.

For a complete Fréchet space V, the bimodule

    F(V)=A tensor_pi V tensor_pi A

is projective for these admissible surjections. A bimodule map from F(V)
is determined by its continuous linear restriction to 1 tensor V tensor 1.
Lift that restriction using the given continuous linear section, then
extend by the left and right A actions. Completed projective tensor
universality proves continuity. The resulting map is an actual lift.

Define the augmented completed bar resolution

    B_n(A)=A tensor_pi A^(tensor_pi n) tensor_pi A, n>=0,
    B_0(A) -> A by multiplication.

Its boundary merges adjacent factors with alternating signs:

    d(a_0 tensor ... tensor a_(n+1))
      =sum_(j=0)^n (-1)^j a_0 tensor ... tensor
                        (a_j a_(j+1)) tensor ... tensor a_(n+1).

Continuity follows from multiplication and the projective topology.
The usual cancellation of consecutive mergers gives d²=0. Inserting
1 as the first factor gives a continuous linear homotopy h, with
h_(−1)(a)=1 tensor a. Expanding the alternating sums proves

    d h+h d=id

on the augmented complex. The identities extend from elementary tensors
by density. Each kernel is closed, and d onto that kernel has the
continuous section given by the restriction of h. Hence this is an
admissibly exact resolution by the relative projectives F(A^tensor n).
Its exactness is established in the stated topology, not inferred from
algebraic bar exactness.

For a complete bimodule M, apply the completed balanced diagonal tensor
to this resolution. The resulting continuous Hochschild chain complex
has terms

    C_n(A,M)=M tensor_pi A^(tensor_pi n)

and boundary

    b(m tensor a_1 tensor ... tensor a_n)
      =m a_1 tensor a_2 tensor ... tensor a_n
       +sum_(j=1)^(n-1) (-1)^j m tensor ... tensor
                           (a_j a_(j+1)) tensor ... tensor a_n
       +(-1)^n a_n m tensor a_1 tensor ... tensor a_(n-1).

The term identification follows by moving the two outer A factors of
the bar resolution into M using balancing; inserting outer units gives
the continuous inverse. Thus this complex computes the diagonal derived
tensor with respect to the chosen split exact structure. Comparison of
projective resolutions follows by successively lifting along the
admissible surjections onto kernels; the same lifting constructs the
comparison homotopies. No other exact structure is being substituted.

Its reduced degree-zero homology is exactly the source quotient of
P123.065:

    M / closure(im b_1)=Q_A(M).

The closure is explicit. Unreduced homology can be non-Hausdorff; neither
closed boundaries in every degree nor finite-dimensional homology is
asserted. A continuous cyclic functional on M gives a continuous chain
map to its scalar target concentrated in degree zero, since it kills b_1.
This gives a derived-complex recipient for the existing source trace
whenever its domain and the A action meet those hypotheses.

For bounded complexes of bimodules as in P123.064, totalize this bar
complex with the internal differential and the Koszul sign. Each total
degree has only finitely many summands because the internal complex is
bounded. Tensoring a continuously split sequence of coefficient spaces
with any fixed complete space preserves its explicit splitting, so the
construction is compatible with such sequences degreewise and with
bounded mapping cones. This does not prove that replacing A by a quotient
algebra satisfies Hochschild excision: that changes all bar factors and
requires an additional theorem.

This resolves the construction of a continuous relative derived diagonal
complex. The target is still a generally unbounded Fréchet complex,
not a proved perfect determinant object or nuclear trace object as
required by A.5. Cyclic derived comparison across composed bimodules,
algebra-extension excision, geometric localization and mixed RR remain
necessary for full A. The explicitly split convention must be compared
with the geometric coefficient category before using this complex there.
