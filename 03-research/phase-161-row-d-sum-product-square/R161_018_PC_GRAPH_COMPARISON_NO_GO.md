# R161_018 — Comparison of the `(PC-ren)` graph limit with the scattering defect

**Domain audit — R161_075.** The identification ZA_infinity=[Z,D_Gamma]=0 and the resulting universal exclusion of linear graph limits are not established by the argument below. L2 multiplication, distributional multiplication and meromorphic continuation have different zero-product implications. In particular the physical limit of A_M and its compatibility with multiplication by Z need a separate proof. Read the old no-go conclusion as unproved pending that domain comparison, not as an established impossibility theorem.

## 0. Verdict

The graph-limit comparison requested at the end of `R161_017` can be completed exactly. It gives a no-go for the
**linear** scattering route.

The renormalized Poisson--Chebyshev limit is the completed full commutator

```
zeta A_infinity=[zeta,D_Gamma]=0,                                (0.1)
```

whereas the germ `zeta W_epsilon^0` is the product-regularized exterior port after the prehistory has been removed.
Splitting the full current into prehistory plus exterior tail gives an identity in which these two terms cancel
tautologically. Consequently `(PC-ren)` does not imply

```
zeta W_epsilon^0=0.                                              (0.2)
```

Asserting (0.2) from the vanishing full commutator would discard the interior/incoming component and is exactly the
compression error already isolated in phase 121.

Thus the linear product-port scattering route is exhausted. Any surviving phase-161 proof must retain a
finite-parameter quadratic defect before the completed commutator collapses to zero. This returns the load-bearing
problem to the reverse Markov/Hardy norm balance of `R161_016`, now with a proved reason why a linear graph split
cannot replace it.

## 1. Full currents and their physical split

Let `u=E_TF`. Write the two full Euler currents as

```
B_+u=q_++h_+,
B_-u=q_-+h_-,                                                    (1.1)
```

where:

- `q_+` is the compact right-current prehistory used to define `Q_+`;
- `q_-` is its parity-reflected posthistory, with transform `Q_-`;
- `h_+` is supported in `[T,infinity)`;
- `h_-` is supported in `(-infinity,-T]`.

The full operator and the scattering bracket are respectively

```
A_infinity u=D_Gamma u-B_+u-B_-u,                                (1.2)
w_epsilon:=D_Gamma u-q_+-q_-.                                   (1.3)
```

Substitution of (1.1) gives the elementary but load-bearing identity

```
w_epsilon=A_infinity u+h_++h_-.                                 (1.4)
```

On `I_T`, the two exterior tails vanish and (1.4) reduces to the first-contact forcing statement in `R161_017`.

## 2. Product regularization of the split

Let `Z` denote the completed co-Poisson multiplier `zeta(1/2+iD)`, with the left orientation transported by the
functional equation. The product ports are precisely the two regularized exterior terms:

```
P_epsilon(F):=Z h_+ + (left functional-equation transport of h_-). (2.1)
```

In Mellin coordinates this is

```
P_epsilon(F)(z)=G_+(z)+chi(s)G_-(z).                              (2.2)
```

Theorem 2.1 of `R161_017` proves

```
P_epsilon(F)=zeta(s)W_epsilon(F).                                (2.3)
```

Applying the completed co-Poisson calculus to (1.4) gives instead

```
zeta W_epsilon
 =Z A_infinity u+P_epsilon(F).                                  (2.4)
```

Comparing (2.3) and (2.4) yields

```
Z A_infinity u=0.                                                (2.5)
```

This is not a new equality-state consequence. It is exactly the meromorphic Gamma--co-Poisson identity

```
Z A_infinity=[Z,D_Gamma]=0,                                     (2.6)
```

because `Z` and `D_Gamma` are scalar Fourier multipliers on their common graph.

**Theorem 2.1 (linear split tautology; PROVED).** The exact scattering-defect identity of `R161_017` and the full
completed commutator contain the same information after the split (1.1). Their comparison reduces identically to
`P_epsilon=P_epsilon`; it supplies no equation setting either exterior port to zero.

## 3. Polar corrections do not change the conclusion

Let `theta_+`, `theta_-` be the canonical exterior corrections and write

```
h_+^0=h_+-theta_+,
h_-^0=h_--theta_-,
w_epsilon^0=w_epsilon-theta_+-theta_-.                           (3.1)
```

Then (1.4) becomes

```
w_epsilon^0=A_infinity u+h_+^0+h_-^0.                            (3.2)
```

Multiplication by the completed zeta factor gives

```
zeta W_epsilon^0
 =Z A_infinity u+P_epsilon^0(F).                                (3.3)
```

But `R161_017` gives `P_epsilon^0=zeta W_epsilon^0`, and the remaining term is again (2.6). Hence the canonical Hardy
gauge fixes the port representative and its norm, but cannot turn the zero full commutator into zero separated
ports.

This also explains why matching the two polar residues in `R161_009` is necessary but not sufficient: residue
matching removes the scalar pole; it does not annihilate the full incoming/prehistory function.

## 4. Relation with finite `(PC-ren)`

For finite `N,M`, the exact identity is

```
S_N^ren A_M Fcal=R_(M,N)^ren.                                   (4.1)
```

On a common smooth graph, `S_N^ren` tends to `Z`. After applying (4.1) to `Fcal u` and passing to the completed
limit, its linear left side is

```
Z A_infinity u=0.                                                (4.2)
```

Therefore every **linear** limit of `(PC-ren)` lands in the tautology proved above. The possible new information is
confined to a quantity which is lost in that limit, for example:

1. a normalized finite defect norm;
2. an oriented mixed pairing before the two histories recombine;
3. a derivative of the finite Hilbert metric with the physical ports reversed.

The first unweighted norm is sign-blind by `R161_002`; the direct metric derivative has the wrong sign by
`R161_016`. The remaining admissible object is consequently the reverse, Tate-centred Markov pullback, or an
equivalent oriented finite mixed pairing which proves its defect identity.

## 5. Exact no-go statement

**Corollary 5.1 (no linear PC closure; PROVED).** No argument using only

```
(PC-ren) -> Z A_infinity u=0,
```

the first-contact equation, parity, and the matched polar coefficients can prove the separated scattering identity
`P_epsilon^0(F)=0`. Such a proof would have to delete the nonzero prehistory/incoming summand in (3.2), or assume the
desired exterior vanishing.

This no-go is limited and constructive: it does not exclude a quadratic finite-parameter identity. It says exactly
which operation must not be performed too early—taking the completed linear graph limit.

## 6. Revised terminal target

The phase-161 terminal statement is now:

> **Quadratic reverse-scattering theorem (OPEN).** Construct, before `N -> infinity` and `delta -> 0`, a
> Tate-centred source map from the joint Euler--Gamma Julia innovations to the canonical product Hardy port such
> that on a first-contact state
> 
> ```
> N_T(delta)-N_T(0)=Q_(T,delta)(F)+o(delta),
> Q_(T,delta)(F)>=0.
> ```

This gives the missing upper bound `E_T^PC(F)<=0`. The opposite causal inequality is already `R161_015`, so equality
forces the port and then `F` to vanish.

## 7. Status

- exact comparison of the scattering defect with the completed PC graph: **PROVED**;
- linear graph split as a closure mechanism: **REJECTED by tautology**;
- polar correction as a cure for the linear split: **REJECTED**;
- necessity of retaining a finite quadratic/oriented defect: **PROVED**;
- quadratic reverse-scattering theorem: **OPEN**;
- row D: **OPEN**.
