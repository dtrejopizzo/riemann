# P123.005 — strict rational-label sheaf and generic completion

## Status

`PROVED-IN-REPOSITORY` for the strict sheaf of nuclear Frechet dagger
algebras on the Zariski base and for identification of its completed generic
stalk with `C_Q`.

This theorem concerns the rational correspondence labels.  Extending its
action to an infinite crossed product of Bruhat--Schwartz coefficients is a
separate open gate.

## 1. Local unit groups

For a finite set `S` of rational primes let

```text
U_S=Spec Z minus S,
Gamma_S^+={q in Q_+^x : v_p(q)=0 for p not in S}.
```

Thus `Gamma_S^+` is the positive part of the group of units of
`Z[S^-1]`.  If `S subset S'`, then `U_(S') subset U_S` and
`Gamma_S^+ subset Gamma_(S')^+`, exactly as required for restriction of
correspondence labels.

Use the symmetric height `H` of P123.003 and define

```text
C_S={c in C_Q : supp(c) subset Gamma_S^+}.             (1.1)
```

Restriction from `U_S` to `U_(S')` is extension by zero along the displayed
group inclusion, equivalently the literal inclusion `C_S -> C_(S')`.

## 2. Local topology theorem

### Proposition 2.1

Every `C_S` is a closed unital nuclear Frechet dagger subalgebra of `C_Q`.
Every restriction map is an isometric closed embedding for all defining
seminorms.

### Proof

The support condition in (1.1) is the intersection of the kernels of the
continuous coordinate functionals outside `Gamma_S^+`, so it is closed.
The group `Gamma_S^+` contains `1` and is closed under multiplication and
inversion; hence convolution, the unit and dagger restrict.

Completeness and the Frechet property follow from closedness in `C_Q`.
The nuclearity proof of P123.003 applies verbatim: the bonding inclusion
from weight `k+4` to weight `k` has nuclear norm bounded by
`sum_(q in Gamma_S^+)H(q)^-4`, which is no larger than the convergent
all-rational sum.  Restriction does not change any coefficient or weight,
so it is isometric, and its range is the closed support subspace.  QED.

## 3. Strict sheaf theorem

### Theorem 3.1

The assignment

```text
U_S |-> C_S                                             (3.1)
```

is a sheaf in the category of nuclear Frechet spaces with continuous
dagger-algebra maps.  More precisely, for every finite Zariski cover

```text
U_S=union_i U_(S_i),
```

the usual sheaf diagram is a strict equalizer diagram of locally convex
spaces.

### Proof

The cover identity is equivalent to

```text
intersection_i S_i=S.                                  (3.2)
```

All `C_(S_i)` embed in `C_T`, where `T=union_i S_i`.  A compatible tuple is
therefore one sequence `c` whose support lies in every `Gamma_(S_i)^+`.
Unique factorization gives

```text
intersection_i Gamma_(S_i)^+
 =Gamma_(intersection_i S_i)^+
 =Gamma_S^+.                                           (3.3)
```

Hence `c` is the restriction of a unique element of `C_S`.  This proves
the algebraic sheaf condition.

Topologically, the equalizer carries the subspace topology inherited from
the finite product.  Every component uses the same seminorms `p_k`, and a
compatible tuple has identical coordinates in all components.  Projection
to any component and the diagonal restriction are continuous and inverse
on the equalizer.  The equalizer identification is therefore a
homeomorphism, hence strict.  Every Zariski open of `Spec Z` is
quasi-compact, so arbitrary covers reduce to finite subcovers.  Dagger and
convolution commute with all maps.  QED.

This argument proves topological descent directly.  It does not obtain it
by sheafifying vector spaces and then assuming completion commutes with
equalizers.

## 4. Generic stalk and all-prime completion

Let

```text
C_eta^fp=colim_(S finite) C_S,                          (4.1)
```

where `fp` means finite prime support of the label group, not finite
support of the coefficient sequence.  Equip this union with the seminorms
induced by `p_k`.

### Theorem 4.1

The Hausdorff completion of `C_eta^fp` for all `p_k` is canonically `C_Q`:

```text
completion(C_eta^fp)=C_Q.                              (4.2)
```

The isomorphism preserves convolution, unit and dagger.

### Proof

Every finitely supported rational sequence belongs to some `C_S`, because
only finitely many primes divide the numerators and denominators of its
labels.  For `c in C_Q`, truncate it to the finite set `H(q)<=N`.  Properness
of the height makes this set finite, and for every fixed `k` the discarded
tail tends to zero in `p_k`.  Hence `C_eta^fp` is dense in `C_Q`.

Conversely, a Cauchy net for all `p_k` converges in the projective limit of
the weighted `l^1` spaces, which is `C_Q` by Theorem 3.1 of P123.003.
Continuity of convolution and dagger extends the corresponding operations
uniquely.  QED.

## 5. Meaning for the A1 bridge

We now have a precise local/global object:

```text
finite-prime Zariski localization:  sheaf C_S
generic finite-prime stalk:         C_eta^fp
all-prime analytic completion:      C_Q.
```

This closes strict topological descent for the label algebra and explains
why `C_Q` itself should not be declared the value of an ordinary Zariski
sheaf on every open.

The imported crossed-product trace ideal has local sections

```text
S(A_S) rtimes Gamma_S.
```

At finite group-label support it is a module over the algebraic part of
`C_S`.  An infinite `C_S`-action does not automatically preserve
Bruhat--Schwartz compact support at nonarchimedean places.  Therefore the
next gate is not another descent proof.  It is:

> construct a complete semilocal test-function module on which `C_S` acts
> continuously, contains the algebraic crossed product as a dense trace
> ideal, and has a diagonal trace compatible with restriction.

Until that module is built, A1 is closed for labels and open for the full
kernel/trace ideal.

