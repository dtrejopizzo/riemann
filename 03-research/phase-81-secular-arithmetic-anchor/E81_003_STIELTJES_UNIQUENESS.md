# E81.003 - Bilateral Stieltjes uniqueness

## 1. Spectral-shift measure

Let the zeros of the bordered numerator `G_{L,N}` be `kappa_j` and the entries
of the mesh diagonal be `d_j`.  Common removable factors are cancelled with
their multiplicities.  Define

```text
nu_{L,N}=sum_j delta_{kappa_j}-sum_j delta_{d_j}.       (1.1)
```

The determinant identity gives, away from the real spectra,

```text
G'_{L,N}(z)/G_{L,N}(z)
 = int_R 1/(z-x) d nu_{L,N}(x).                        (1.2)
```

### Proof

Differentiate the logarithms of the bordered numerator and mesh denominator in
E81.002.  Each real root contributes one simple Cauchy kernel. `QED`

## 2. Bilateral projection

For real `sigma>1/2`, direct calculation gives

```text
i/(i sigma-x)-i/(-i sigma-x)
 = 2 sigma/(x^2+sigma^2).                              (2.1)
```

Hence

```text
i G'(i sigma)/G(i sigma)
-i G'(-i sigma)/G(-i sigma)
 = int_R P_sigma(x) d nu_{L,N}(x),                     (2.2)

P_sigma(x)=2 sigma/(x^2+sigma^2).                      (2.3)
```

The kernel is even.  If

```text
check(nu)(B)=nu(-B),
nu^ev=(nu+check(nu))/2,                                (2.4)
```

then the right side of (2.2) depends exactly on `nu^ev`.  The odd part of the
spectral shift is invisible to the bilateral characteristic.

Thus full residue recovery is neither required nor possible from RDI.  The
correct object is the even spectral-shift class.

## 3. Uniqueness theorem

### Theorem 3.1

Let `mu` be an even signed Borel measure on `R` satisfying

```text
int_R (1+x^2)^(-1) d|mu|(x)<infinity.                  (3.1)
```

If

```text
int_R 2 sigma/(x^2+sigma^2) dmu(x)=0                  (3.2)
```

for every `sigma` in a nonempty open interval of positive numbers, then
`mu=0`.

### Proof

Push `mu` forward under `x->x^2` to a signed measure `bar mu` on
`[0,infinity)`.  Condition (3.1) makes

```text
F(q)=int_[0,infinity) 1/(t+q) d bar mu(t)              (3.3)
```

well defined for `q>0` and holomorphic on the slit plane.  Equation (3.2) is
`2 sigma F(sigma^2)=0` on an interval.  The identity theorem gives `F=0` on
its domain.  Uniqueness of the Stieltjes transform gives `bar mu=0`.  Since
`mu` is even, its pushforward determines it, so `mu=0`. `QED`

## 4. Correct arithmetic target

Let

```text
Y_{L,N}(s)=H_L(s)-d/ds log A_{L,N}(s),                 (4.1)
```

with `A_{L,N}` from E81.002.  On the real safe axis, the exact RDI defect is

```text
int_R P_sigma d nu_{L,N} - Y_{L,N}(1/2+sigma).         (4.2)
```

After fixed-`L` convergence, write the corresponding renormalized limits as
`nu_L^ev` and `Y_L`.  Then `RDI-ANCHOR` is exactly

```text
int_R P_sigma(x) d nu_L^ev(x)-Y_L(1/2+sigma) -> 0      (4.3)
```

locally uniformly for `sigma>1/2` as `L->infinity`, together with its
holomorphic continuation to safe complex domains.

Equation (4.3) is a topology of Stieltjes convergence, not an assertion of
finite total variation.  The limiting measures may require the explicit mesh
renormalization already contained in `A_{L,N}`.

## 5. Circular inverse construction

One could define a distribution `tau_L` by declaring its Poisson transform to
be `Y_L`.  Such a definition does not prove (4.3): it merely renames the target.
An admissible arithmetic measure must instead be constructed independently
from the Gamma-prime cell functional, with its transform calculated afterward.

Theorem 3.1 then gives a useful rigidity statement:

```text
if an independently constructed even arithmetic shift tau_L has transform
Y_L, then the secular anchor is equivalent to

nu_L^ev-tau_L -> 0 in Stieltjes topology.               (5.1)
```

Coherence, cloud convergence and scalar signatures do not construct
`tau_L`; Phase 80 already supplies counterexamples to that inference.

## 6. Conservation check

The outer limit of `Y_L` is the completed zeta logarithmic derivative after
the explicit factors are restored.  Proving that it is the limit of real
finite spectral shifts gives the safe-ratio convergence whose normal-family
closure implies `Omega7`.  Therefore (4.3) is not a soft measure-convergence
lemma.  It is the force-RH arithmetic step in Stieltjes coordinates.

## 7. Status

```text
proved:
  the exact spectral-shift transform (1.2);
  the bilateral Poisson identity (2.2);
  only the even spectral shift is visible;
  uniqueness of the even shift from its Poisson transform;

corrected:
  full secular residue identification is unnecessarily strong;
  defining a target measure by inverse transform is circular;

reduced:
  RDI-ANCHOR to construction of an independent arithmetic even shift tau_L
  and proof of (5.1);

open:
  independent Gamma-prime construction of tau_L;
  Stieltjes convergence of nu_L^ev to tau_L;

next:
  derive the secular residues from the exact inhomogeneous cell equation and
  test whether it yields tau_L before taking the outer limit.
```
