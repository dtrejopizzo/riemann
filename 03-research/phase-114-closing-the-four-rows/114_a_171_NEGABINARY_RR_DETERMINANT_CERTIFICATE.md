# The negabinary Riemann--Roch determinant certificate

## 1. Finite determinant objects

Let an effective external divisor have positive logarithmic degrees `a,b`.
For an integer `t>=1`, put

`m_t=floor(exp(t a))`, `n_t=floor(exp(t b))`,

and let `r_t=r(m_t)`, `s_t=r(n_t)` be the maximal admissible negabinary
lengths of the preceding note.  The canonical mixed block is parameterized
by

`V_t=F_2^(r_t*s_t)`.

Order its coordinate basis lexicographically by `(i,j)`.  Let

`L_t^cert=det_R(R^(r_t*s_t))`

with distinguished generator the wedge of that ordered basis, and give it
the norm

`||1_t||=exp(-(log 2)^2 r_t s_t)`.

Both the vector space and the metric are canonical: one factor `log 2`
comes from each of the two absolute-base digit directions.

## 2. Normalized limit

Negabinary admissibility gives

`r_t=t a/log 2+O(1)`, `s_t=t b/log 2+O(1)`.

Therefore

`(log 2)^2 r_t s_t=t^2 ab+O(t)`.

After the real tensor normalization

`Lhat_t^cert=(L_t^cert)^(tensor 1/t^2)`,

one obtains

`-log ||1_t||_(Lhat_t^cert)=ab+O(1/t)`.

Thus the normalized determinant certificates converge isometrically to

`lambda_RR^cert(x)=R 1_x`, `||1_x||=exp(-d_1(x)d_2(x))`.

No auxiliary prime, interpolation field, exponent base or polyhedral
presentation occurs.

## 3. Polarization, contact and Green quotient

Extend the quadratic metric exponent to the external divisor group by

`F_RR(x)=d_1(x)d_2(x)`.

Its second difference is

`B_RR(x,y)=d_1(x)d_2(y)+d_2(x)d_1(y)`.

Let `lambda_C(x,y)` be the actual torsion determinant of the reduced finite
contact complexes.  Its metric exponent is

`C_Lambda(x,y)=sum_p
 (x_(p,1)y_(p,2)+x_(p,2)y_(p,1)) log p`.

Define the Green comparison line in the Picard groupoid of based normed
real lines by

`lambda_G^cert(x,y)=delta lambda_RR^cert(x,y)
                     tensor lambda_C(x,y)^(-1)`.

Then, by construction in a genuine Picard groupoid, there is a canonical
isometry

`delta lambda_RR^cert ~= lambda_C tensor lambda_G^cert`,

and its logarithmic metric identity is exactly

`B_RR=C_Lambda+G`.

Associativity, symmetry and the biextension interchange law follow from
bilinearity of the three metric exponents and preservation of the
distinguished generators.

## 4. Exact status

`L_t^cert` is a genuine determinant line of the finite relation-parameter
space whose `2^(r_t s_t)` points inject into spherical mixed sections.  The
limit proves a canonical coefficient-one RR/Green metric certificate on
the external divisor group.

It is not yet the determinant of the full derived global-section object.
That identification is equivalent to the remaining separated Kunneth
theorem: the assembly-separated negabinary block must be shown to control
the quadratic determinant of `R Gamma_S(Y_S,L(D,E))`, including all higher
smash homotopy.  The present note closes the finite determinant and metric
comparison once that identification is supplied; it does not assume it.

