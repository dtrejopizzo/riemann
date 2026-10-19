# P123.076 — Complete scalar Tate self-tensor via a continuous Koszul model

Status: PROVED over the scalar rapid label algebra D_S.
Comparison with the full source self-tensor remains a separate problem.

Write S_f={p_1,...,p_r}, r>=1, and identify a label with its exponent
vector e in Z^r. The height satisfies

    (1/2)sum_i |e_i|log p_i <= log H(product p_i^e_i)
                                  <=sum_i |e_i|log p_i.

Thus the defining rapid seminorms of D_S are equivalent to all weighted
l¹ norms sum_e |c_e| exp(k||e||_1). The Laurent series sum_e c_e z^e
identifies D_S topologically with holomorphic functions on (C^*)^r,
with uniform convergence on compact polyannuli. In one direction the
weighted l¹ estimates give uniform convergence with all local holomorphic
derivatives. Conversely, Cauchy coefficient estimates on a strictly larger
polyannulus bound the weighted l¹ sum by a compact supremum times the
convergent sum of exp(-||e||_1). Varying polyannuli gives both topologies.
This also proves uniqueness and surjectivity of the Laurent realization.

Fix lambda=(lambda_1,...,lambda_r) in (C^*)^r. Evaluation in coordinate i
defines a continuous projection E_i f=f(z with z_i=lambda_i). Division
defines the continuous operator

    Q_i f=(f-E_i f)/(z_i-lambda_i),

with the removable value at z_i=lambda_i. To see continuity on a compact
polyannulus, use a slightly larger one containing lambda_i and a small
closed disk around it. Off that disk the denominator is bounded away
from zero; on a smaller disk, the Cauchy derivative estimate bounds the
quotient. These estimates use only a larger compact supremum seminorm.
They give

    (z_i-lambda_i)Q_i=1-E_i,
    Q_i((z_i-lambda_i)f)=f.

Operators for different coordinates commute. These identities split the
one-coordinate augmented Koszul sequence continuously. Successively
applying them in all coordinates contracts the augmented full Koszul
complex onto evaluation at lambda. Equivalently, after resolving one
coordinate its remaining coefficient space is the same holomorphic
algebra in r-1 coordinates, with the displayed continuous section and
division; induction yields a finite continuous contraction. Hence

    K_lambda=K_D(z_1-lambda_1,...,z_r-lambda_r)

is a continuously split resolution of C_lambda by finite free D-modules,
in degrees -r,...,0. It computes derived tensors in the relative split
exact structure already used in P123.066.

For another character mu, tensoring with C_mu gives the explicit finite
Koszul complex on constants mu_i-lambda_i. If mu=lambda all differentials
vanish, so

    Tor_k^D(C_lambda,C_lambda)=exterior^k C^r,
                         0<=k<=r,

and the groups vanish above r. If mu!=lambda, one constant is nonzero;
wedge insertion in that coordinate divided by the constant contracts
the complex. All mixed Tor groups then vanish. These are complete
calculations over D, not merely degree-one lower bounds.

For the two Tate characters lambda_i^-=p_i^-1/2 and lambda_i^+=p_i^1/2,
put B=C_lambda^- direct_sum C_lambda^+. The mixed summands vanish and

    B tensor_D^L B
       ~= exterior^*(C^r)_- direct_sum exterior^*(C^r)_+

with exterior degree k in cohomological degree -k and zero differential.
Multiplication to B is identity on the two degree-zero summands and
zero on the others. Its cone is therefore represented by the two copies
of exterior^k C^r in degrees -k-1, for 1<=k<=r. In particular this
specific scalar excess object is perfect, with a completely specified
finite determinant line. No scalar norm or arithmetic degree of that
line is inferred solely from the existence of the finite complex.

Under addition of a prime, the Koszul model adds its new coordinate and
the self-Tor model adds one exterior generator. Thus the comparison
retains the growing excess, rather than falsely treating the character
map as a homological epimorphism. The degree-one basis agrees, after
normalization by lambda_i, with the classes detected in P123.075.

The full source A has maps D -> A -> D splitting identity. Their
augmented bar maps show that this scalar self-Tor contribution is a
retract of the full source calculation at each Tate augmentation.
They do not show that the other summand vanishes. Accordingly the
perfect scalar model is now available for the mixed RR comparison,
but perfectness or a determinant for the entire full-source defect,
its ruling normalization and the mixed RR equality remain unproved.
