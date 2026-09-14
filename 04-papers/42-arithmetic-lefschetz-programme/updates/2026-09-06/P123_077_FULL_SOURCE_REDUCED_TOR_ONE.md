# P123.077 — Full-source reduced Tate Tor in degree one

Date: 2026-09-06. Status: PROVED for the original repaired rapid C_0
source of P123.019. This does not assert higher-degree excision or the
same result for stronger integrable topologies without further estimates.

Let e:A -> D and j:D -> A be the split coefficient-unitization maps,
I=ker e, and let chi=lambda composed with e be a Tate augmentation.
Write J=ker chi and m=ker(lambda:D -> C). As complete vector spaces,

    J=I direct_sum j(m).

The ideal I has the two-sided approximate identity of P123.031: compact
coefficient cutoffs u_alpha at the identity label, of seminorm at most
one in every rapid p_k, with u_alpha i -> i. Since u_alpha and i both
belong to J, every i in I belongs to closure(span J²).

Multiplicativity of e shows that e(J²) is contained in span m², and
multiplicativity of j shows j(m²) is contained in span J². Using the
continuous direct decomposition above, these two inclusions give the
exact closed-subspace identity

    closure(span J²)=I direct_sum j(closure(span m²)).

In detail the right side is contained in the left by the approximate
identity and the section. Conversely its quotient is detected by the
continuous map J -> m/closure(m²), which kills every product in J².
The kernel of that map is exactly the displayed right side. Therefore

    J/closure(J²) ~= m/closure(m²)               (1)

is a topological isomorphism, with inverse induced by j. The quotients
are precisely the reduced degree-one normalized bar homologies of
P123.075. Thus the geometric coefficient ideal introduces no additional
reduced degree-one self-Tor at this augmentation in this topology.

For completeness, the scalar quotient in (1) is explicitly C^r, with
r=|S_f|. Under the holomorphic Laurent realization of P123.076, successive
coordinate division writes every f vanishing at lambda as

    f=sum_i (z_i-lambda_i) g_i.

If all first derivatives at lambda vanish, differentiate this identity
at lambda to obtain g_i(lambda)=0 for each i. Hence f lies in m².
Conversely every element of m² has zero first derivatives. These derivative
functionals are continuous, so m² already has closed linear span equal
to their common kernel in m. The normalized classes z_i/lambda_i-1
and the logarithmic derivatives lambda_i partial_i give inverse linear
coordinates on that quotient. They coincide with the label valuation
derivations and classes in P123.075.

Consequently

    reduced Tor_1^A(C_chi,C_chi) ~= C^r

with exactly the previously identified prime-coordinate basis. The
comparison and basis commute with repaired semilocal charts and the
addition of new prime coordinates. This is now an equality, rather than
the lower bound proved before the complement calculation.

The closure in (1) is essential to the argument: an approximate identity
proves approximation by products, not by itself an exact algebraic
factorization or a bounded contraction of the full relative bar complex.
Therefore neither unreduced Tor_1 nor higher Tor groups are identified
by this proof. A determinant comparison needs a genuine controlled
derived object, not just this reduced degree-one calculation. The next
remaining source-excision problem is in those higher/strict terms.
