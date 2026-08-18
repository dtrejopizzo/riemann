# The canonical negabinary mixed block

## 1. Admissible digit tuples

For `r>=1`, put

`A_r=(1,-2,(-2)^2,...,(-2)^(r-1))`.

Its subset sums are all distinct and form a contiguous interval
`Delta(r)`.  This is the negabinary uniqueness theorem used in the
absolute-base Riemann--Roch proof.  If

`M_r=max{|x|:x in Delta(r)}`,

then

`2^(r-1) <= M_r < 2^(r+1)/3`

for `r>=2`.  Hence, for the spherical section module

`H_m=(H Z)_[-m,m]`,

the tuple `A_r` is an element of `H_m(r_+)` whenever `M_r<=m`.  Define

`r(m)=max{r:M_r<=m}`.

Then `r(m)=log_2(m)+O(1)`.  The definition is canonical: it uses the
distinguished absolute generator `X=-2` from
`S[X], 1+1=X+X^2`.

## 2. The rectangular family in the spherical smash

Let `A_r in H_m(r_+)` and `B_s in H_n(s_+)` be the two negabinary tuples.
For every zero--one matrix

`epsilon=(epsilon_(ij)) in {0,1}^(r*s)`,

let

`v_epsilon:r_+ smash s_+ -> 1_+`

send `(i,j)` to `1` when `epsilon_(ij)=1` and to the base point otherwise.
The Day-colimit description of the smash product gives an element

`z_epsilon=[r_+,s_+,v_epsilon,A_r smash B_s]
             in (H_m smash_S H_n)(1_+)`.

## 3. Assembly separates all matrices

Map the bounded modules to `H Z` and apply the canonical assembly map

`alpha:H Z smash_S H Z -> tilde(H Z) o H Z`.

The explicit assembly formula gives

`alpha(z_epsilon)
 = sum_(i=0)^(r-1) (-2)^i [b_i(epsilon)]`,

where

`b_i(epsilon)=sum_(j=0)^(s-1) epsilon_(ij)(-2)^j`.

View this as the Laurent polynomial

`P_epsilon(t)=sum_i (-2)^i t^(b_i(epsilon))`

modulo constants.  Terms with `b_i=0` disappear into the base point.

The polynomial determines `epsilon`.  Indeed, for every nonzero exponent
`b`, its coefficient is the subset sum of those `(-2)^i` whose rows have
value `b`; negabinary uniqueness recovers that set of row indices.  The
exponent `b` itself uniquely recovers the selected columns in each such
row.  After all nonempty rows have been recovered, the remaining row
indices are exactly the empty rows.  Thus

`P_epsilon=P_eta  implies  epsilon=eta`.

Since equality in the smash product would imply equality after assembly,
the `z_epsilon` are pairwise distinct.

### Theorem

`(H_m smash_S H_n)(1_+)` contains a canonical family of cardinality

`2^(r(m)r(n))`.

For Arakelov bounds `m_t=floor(exp(t a))` and
`n_t=floor(exp(t b))`, with `a,b>0`,

`r(m_t)r(n_t)=t^2 ab/(log 2)^2+O(t)`.

This is a canonical quadratic family of genuine elements of the
noncollapsed spherical square.  No finite field, interpolation base or
fresh prime is chosen.

## 4. Exact limitation

The theorem does not by itself compute the minimal-generator dimension of
the entire smash product.  For a non-special Gamma-set, a fixed list of
marginals can admit several joint lifts, so one generator subset need not
have a unique sum.  Therefore the elementary bound `#E<=2^dim(E)` used for
special absolute section modules cannot be applied to `H_m smash H_n`
without an additional separatedness theorem.

The block nevertheless gives an intrinsic finite perfect approximation:
the set of its matrices is the vector space `F_2^(r(m)r(n))`, and the
assembly map realizes all of its elements as distinct spherical mixed
sections.  Proving that the assembly-separated quotient is the universal
quadratic quotient, and that it agrees with derived global sections, is the
remaining Kunneth/separatedness step.

