# R170_872 — Audit of the swap cycle against the R161 concomitant

## 0. Verdict

R170_871 correctly proves

\[
 PLQSP-PSQLP=-(PLPSP-PSPLP).                              \tag{0.1}
\]

The route interpretation `(d,m)` adds a useful arithmetic reading:
the flow observes the odd cycle `Lambda(d)-Lambda(m)` that disappears when
one forgets the intermediate point. However, (0.1) does not constitute a new
operator class.

R161_064(2.2) already identifies, for a causal synthesis `S`, the
concomitant

\[
 \mathcal K_P(S;g,w)
 =\langle Pg,PSQw\rangle-\langle Qg,SPw\rangle.            \tag{0.2}

Polarizing (0.2) between the syntheses `L` and `S`, and taking the tests
produced by the other leg, generates exactly the four blocks of (0.1). R161_057
further already shows that global conservation leaves an oriented
exterior flow and an interior moment, not their vanishing.

Hence R170_871 is a route realization of the known residue. It does not
prove the extension of the involution to the Tate port, nor does it narrow the
open door beyond the boundary-augmented class `beta_phys` of R170_869.

## 1. Literal polarization

For causal operators `L,S` and vectors `u,v`, define

\[
 \mathcal K_P(L;u,Sv)
 =\langle Pu,PLQSv\rangle-\langle Qu,LP Sv\rangle,         \tag{1.1}
\]

and the expression with `L,S` swapped. Subtracting both orientations,
the exterior terms contain

\[
 PLQSP-PSQLP,                                               \tag{1.2}

after choosing the corresponding product tests; the remaining terms are
the two readings of the compressed interior block. The global
identity `LS=SL` proves that the interior--exterior sum is zero, which is (0.1).

The exact placement of adjoints depends on whether one uses PC before or after
multiplying by `mathscr F`. R161_064 warns that moving them across
`P` creates precisely another concomitant. R170_871 preserves the order and does not
make that mistake, but it does not eliminate it either.

## 2. Comparison of open doors

R161_064 leaves open:

\[
 \mathcal C_{M,N,T}(f)
 =\text{Tate collar} +\text{Gamma} +\text{exterior square},
                                                                    \tag{2.1}
\]

and

\[
 \mathcal C_{M,N,T}(f)=0                                  \tag{2.2}

on the first-contact radical. R170_871 leaves open the extension of
the involution `d<->m` to the reflected, polar, and Tate terms, followed by
annihilation by minimality.

These tasks are the same after the dictionary:

| R170_871 | R161_057--064 |
|---|---|
| intermediate `P/Q` point of the route | support commutator |
| odd cycle `d<->m` | two causal orientations |
| flow `Phi_ext` | oriented exterior flux |
| compressed block | interior first moment/concomitant |
| extension to the port | correct Tate placement |
| annihilation at contact | first-contact annihilation |

The table is an identification of obstacles, not a proof of (2.1) or
(2.2).

## 3. What the arithmetic reading does add

The R161 formulation holds for general causal syntheses. R170_871
explains when its two orientations share exactly the same Chebyshev
face:

\[
 \sum_{d\mid k}\Lambda(d)
 =\sum_{m\mid k}\Lambda(m)=\log k.                         \tag{3.1}

Together with R170_866, sharing the column `log` at every cut
characterizes `Lambda`. This locates the arithmetic specificity within the
known concomitant.

But once (3.1) has glued the interior faces, the value of the exterior
flow is the quotient class `beta_phys`. R170_869 shows that the factored
identities do not determine that class. The route reading does
not change this fact.

## 4. Operator falsifier

Identity (0.1) holds for any operators `L,S` that commute on
the full space. One may choose a projection `P` for which

\[
 PLQSP-PSQLP\ne0.                                         \tag{4.1}

Then the interior block is its opposite. So commutativity, swap, and
global conservation do not imply zero flow.

Finite models of nilpotent shifts verify (0.1) and present
both blocks nonzero. Hence no argument using only those three
properties can close (2.2).

## 5. Next admissible piece

Another support concomitant should not be built. The missing piece must
act on the **correct Tate placement** of R161_064 and prove
one of these two statements:

1. the boundary-augmented class `beta_phys` is the restriction of a common
   positive form to two null vectors;
2. the factor swap extends to the full port as an
   involution that fixes the physical datum and changes the sign of `beta_phys`.

R170_870 shows why either would suffice. Neither is
proved in the corpus.

## 6. Status

```text
R170_871 flow identity                                    CORRECT
d<->m route cycle                                         CORRECT
new operator class                                        NO: COLLISION WITH R161_057/064
Lambda specificity within the concomitant                 LOCATED
swap/commutativity imply zero flow                        REFUTED
Tate/exterior reciprocity                                 OPEN
VIR--LB / D                                               OPEN
```
