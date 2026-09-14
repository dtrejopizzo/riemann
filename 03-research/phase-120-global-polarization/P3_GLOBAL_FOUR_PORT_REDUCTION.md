# Global four-port reduction after place-Poisson resummation

Status: exact algebraic reduction on the common form core. The signed
Gamma--degree Green commutator is now proved in
`P3_GLOBAL_SCATTERING_GREEN_IDENTITY.md`. The positive bulk identity in
Section 4 remains open and is now exactly the global-square step.

## 1. What is reused and what is new

D.244--D.247 already construct the conservative torsion-normalized
prime-tangent colligation

    ||E_- z||^2 + ||deg z||^2
      = ||E_+ z||^2 + sum_p (log p)||z_p||^2,        (1)

where `deg z=sum_p sqrt(log p) z_p`. D.248--D.252 correctly prove that the
relative Euler score cannot be closed prime by prime. Free or symmetric Fock
space is also rejected by D.142/D.194 because of factorial descent and the
wrong contact defect.

Phase 120 adds three exact pieces:

1. the quarter twist and `m_0` come from one Hardy determinant;
2. `C_n=n^(-1/2)V_(log n)` has one simultaneous half-density dilation;
3. the full `p`-tower is the Poisson observation of `C_p`, on the same type of
   exponential carrier as the Gamma Markov resolution.

This does not make a local relative score positive. It supplies the common
carrier needed to perform the global wiring required by D.252.

## 2. Physical prime states

For a compactly supported profile `F`, put

    C_p=p^(-1/2)V_(log p),
    z_p(F)=O_p E_TF
          =sqrt(1-p^(-1))(I-C_p)^(-1)E_TF.

Only primes with `log p<2T` are retained. The contact output in (1) is then
exactly the place-Poisson load:

    sum_p (log p)||z_p(F)||^2
      =sum_p (log p)||O_pE_TF||^2.                  (2)

The construction is before `B_nuc`; its Neumann expansion produces all
`p^j`, including `4` as the second return of `C_2`.

Identity (1) is a Gram identity and therefore remains valid for
Hilbert-valued `z_p`. Applying it to (2) gives

    prime_load(F)
      =||E_-z(F)||^2+||deg z(F)||^2-||E_+z(F)||^2. (3)

## 3. Exact elimination of every local contact port

The place-Poisson factorization is

    -B_nuc,T(F,F)
      =||W_Gamma E_TF||^2+theta_T||F||^2
       -m_0||F||^2-prime_load(F),                  (4)

where `theta_T=sum_(p<exp(2T))log p`. Substitution of (3) into (4) yields
the exact reduced score

    -B_nuc,T(F,F)
      = [||W_Gamma E_TF||^2+theta_T||F||^2
         +||E_+z(F)||^2]
        -[m_0||F||^2+||E_-z(F)||^2
          +||deg z(F)||^2].                        (5)

This is the decisive reduction: all independent reduced-contact outputs have
cancelled by a source-side conservation law. Only the common Gamma phase,
the even/odd global tangent ports, the single degree port and the polar load
remain.

## 4. The positive wiring identity

For primitive `F`, write uniquely

    F=(-d^2/dt^2+1/4)G,
    G in C_c^infinity,

using the compact polar-potential lemma. Construct, from the quarter-twisted
Gamma Markov states and the simultaneous half-density dilation, a bulk map
`W_bulk` satisfying

    ||W_Gamma F||^2+theta_T||F||^2+||E_+z(F)||^2
      =m_0||F||^2+||E_-z(F)||^2+||deg z(F)||^2
       +||W_bulk G||^2.                              (6)

Equation (6) is stronger than the signed Green commutator, which is now
proved exactly. It must be the positive-square identity of the common
derived pushout. Its
boundary orientation and every coefficient are already fixed by Sections
1--3. There is no scalar to choose and no local contact left to estimate.

If (6) is proved, (5) gives immediately

    -B_nuc,T(F,F)=||W_bulk G||^2>=0,

including `T=(1/2)log 5`, and the same identity passes to the cofinal closed
form if the bulk energies are monotone.

## 5. Exact failure modes

The construction fails, rather than being retuned, if:

- the D.247 identity does not tensorize with the physical Poisson states;
- the degree port in (6) is not the boundary trace of the common phase
  extension;
- closing the Gamma Markov form creates an additional boundary/Maslov term;
- the two compact polar conditions do not remove all external source ports;
- finite-window zero extension loses an outgoing return edge.

No further eigenvalue sweep or scalar-gap estimate is relevant to (6).
