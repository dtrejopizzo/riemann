# P123.033 — unit subtraction, conductor test and finite-place distribution

Date: 2026-09-05. Status: PROVED for the explicitly normalized unit
functional and its conductor values. Comparison with the common-carrier
shadow and the imported cutoff normalization is not asserted.

## 1. State the normalization rather than hiding a counterterm

Continue P123.032. For a scalar Bruhat test f on the positive-real
normalized global group, define

    L_p^unit(f)=(log p) integral_(Z_p^*)
          [f(j_p(u))-f(1)] / |1-u|_p d^*u,          (1.1)

where d^*u has total mass 1. Local constancy makes the numerator zero
on a neighborhood of 1, so this is an ordinary convergent integral.
This chooses the extension whose value on a constant unit test is zero.
A different extension could add c_p f(1); no cutoff theorem has yet
identified its normalization with (1.1).

Set L_p=L_p^off+L_p^unit. For radial tests the unit part vanishes, so
P123.032's prime formula is unchanged. For ramified tests it contributes
nontrivially, as the following exact check shows.

## 2. Filtration computation

Write U=Z_p^*, U_r=1+p^r Z_p for r>=1 and U_0=U. Haar probability
satisfies vol(U_r)=1/((p-1)p^(r-1)). For u!=1,

    |1-u|_p^-1
      =1+sum_(r>=1) (p^r-p^(r-1)) 1_(U_r)(u).      (2.1)

For tests constant on cosets of U_a the difference in (1.1) vanishes
on U_a; hence only r<a matters when integrating that difference.
Let P_r denote averaging over U_r on functions of U, with P_0 averaging
over all U and P_a=id on these finite-level functions. Their normalized
convolution operator associated to the difference kernel is

    Q_a = sum_(r=0)^(a-1) (P_r-id).                 (2.2)

Indeed each coefficient in (2.1), multiplied by vol(U_r), is 1.
The factor log p is omitted in Q_a and restored in (1.1).

If chi is a nontrivial continuous character of U of conductor exponent
a, meaning it is trivial on U_a but not on U_(a-1) (with U_0=U),
then P_r chi=0 for 0<=r<a, by translation invariance of Haar measure.
Consequently

    integral_U (chi(u)-1)/|1-u|_p d^*u = -a.        (2.3)

For the trivial character the integral is zero. This handles p=2 as
well: U_1=U_0 there, so no nontrivial conductor-one character exists.
For f with f(j_p(u))=c chi(u) and f(1)=c, the unit packet is
-a(log p)c. This is a derived value of the defined distribution, not
an assumed conductor correction.

## 3. Continuity and stabilization including units

On unit level a>=1, (2.2) yields

    |L_p^unit(f)| <= 2a(log p)||f||_infinity.

If f ignores the p-unit coordinate, the integrand in (1.1) is zero:
a unit local idele has real coordinate 1 and all other unit coordinates 1.
Thus only the finite set S_0 of unit coordinates on which f depends
can contribute a unit term. Combining this with P123.032, on a fixed
real support [-T,T] the total finite-place distribution involves only

    S_0 union {p : p<=exp(T)}.

The place sum therefore stabilizes exactly on every compact-support,
finite-unit-level test step and is continuous there. The linear
inductive-limit property gives a continuous functional on the declared
scalar Bruhat space. This still gives no estimate for spatial or spectral
cutoffs in the nuclear representation.

## 4. Match the radial convention to the actual Meyer source

The local repository copy of Meyer's corrected paper gives

    W_p(g)=(log p) sum_(k>=1)
                   [p^-k g(p^-k)+g(p^k)]

in its equation labelled eq:Wp. Substituting

    g(x)=x^-1/2 h(log x)

gives exactly P123.032 equation (2.3). This explicitly checks the
half-density change of test convention on the radial sector. It does
not import a ramified character theorem or a common-carrier realization.

Primary source: [Meyer, corrected source](../../00-references/papers-nuevos/C/arXiv-math0412277v3),
introductory equations eq:Wp and eq:Winfty; see also
[Meyer, arXiv version 3](https://arxiv.org/abs/math/0412277v3).

## 5. Remaining comparison

The nonunit weights, unit subtraction, conductor values and prime-set
limit now form a specified finite-place scalar distribution. The missing
proof must identify the chosen unit counterterm with the actual cutoff
normalization and realize the whole distribution as the diagonal shadow
of A. The archimedean principal value, its Gamma constant and the Tate
terms remain separate obligations. This note supplies no RR or D sign.

The companion verifier checks (2.2) and its conductor-layer eigenvalues
on exact finite unit groups. These are finite algebra checks; the proofs
of convergence and continuity are above.
