# 114.a.47 — I7: the contact shadow is necessarily nonfaithful

> **Dynamic refinement (`a_70`).** The faithful preimage is now constructed
> as Picard-decorated diagonal spans. Their contact functor has exactly the
> nonfaithful shadow proved here. Only an undecorated cycle lift remains open.

```
+--------------------------------------------------------------------------+
| INPUT       The literal Haran-square sheaves M_n constructed in a_46.   |
| COLLAPSE    M_{p^a}=M_{p^b}; every label with >=2 primes maps to zero.   |
| CONSEQUENCE n -> M_n cannot itself be the correspondence algebra.        |
| REQUIRED    Gamma_n must retain a label/operator direction invisible to  |
|             its derived diagonal contact LDelta^*Gamma_n=M_n.            |
| OPEN        H7-CYCLE-LIFT remains the exact geometric gate.              |
+--------------------------------------------------------------------------+
```

## 1. Classification of contact shadows

Recall from `a_46` that

\[
 \mathcal M_n=\bigotimes_{p\mid n}(i_p)_*\underline{\mathbb F_p}.
 \tag{1.1}
\]

### Theorem 1.1

The isomorphism class of `M_n` is completely classified as follows:

\[
 [\mathcal M_n]=
 \begin{cases}
  [\underline{\mathbb Z}],&n=1,\\
  [(i_p)_*\underline{\mathbb F_p}],&n=p^k,\\
  [0],&n\text{ has at least two distinct prime divisors}.
 \end{cases}                                             \tag{1.2}
\]

In particular, `M_{p^a}=M_{p^b}` for every `a,b>=1`, and all labels with at
least two prime factors have the same zero shadow.

### Proof

Formula (1.1) contains one factor for each *distinct* prime. Repeated tensor
powers of the same prime skyscraper are canonically that skyscraper, whereas
two different prime supports have zero tensor product. This is exactly
Theorem 2.1 of `a_46`. QED.

## 2. Faithfulness obstruction

### Corollary 2.1

The symmetric monoidal map

\[
 (\mathbb N^\times,\cdot)\longrightarrow
 (\operatorname{Iso}(\operatorname{Sh}(Y)),\otimes),
 \qquad n\longmapsto[\mathcal M_n]                     \tag{2.1}
\]

is not faithful. Consequently one cannot define the desired geometric
correspondences by `Gamma_n:=M_n`.

This does **not** obstruct a cycle lift. It says precisely that diagonal
intersection is allowed to forget information: distinct cycles `Gamma_n`
must remain distinguishable before applying `LDelta^*`, even though

\[
 L\Delta^*\Gamma_{p^a}\simeq\mathcal M_p,
 \qquad
 L\Delta^*\Gamma_n\simeq0
 \quad(n\text{ not a prime power}).                    \tag{2.2}
\]

The faithful Witt operators of `a_36` already provide the missing label and
composition data operatorially. H7-CYCLE-LIFT therefore has the sharp form:
construct a geometric correspondence category on the Haran square and a
faithful monoidal family `Gamma_n` whose diagonal-contact functor has exactly
the nonfaithful shadow (1.2). Merely decorating `M_n` by an external operator
would restate the problem, not solve it geometrically.

`a_61`/`a_66` supply a faithful abstract unit-torsor pre-shadow `T_n` on the
literal square. H7-PRIME-REG is needed for its completed-lattice realization.
Its typed normal/contact interpretation is supplied by `a_67`--`a_69`.
Decorated-span convolution is supplied by `a_70`; only the stronger
undecorated cycle lift remains open.

## 3. Verification scope

`114_a_47_i7_contact_shadow_verify.py` exhaustively checks the classification,
monoidal law and explicit collisions on finite ranges. These computations
verify the finite arithmetic model; they do not construct H7-CYCLE-LIFT.
