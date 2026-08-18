# E80.006 - Minimal convergence requirements behind GAP-Z

## 1. Exact role of GAP-Z

For fixed `L`, let

```text
g_N(sigma)=2 Re(i T'_{L,N}(i sigma)/T_{L,N}(i sigma)),
sigma>1/2.                                             (1.1)
```

The proved three-way decomposition has the form

```text
g_{N+2}-g_N=ZERO_N+MESH_N+BND_N,                       (1.2)
```

where `MESH_N=O_K(N^-2)` and `BND_N=O_K(N^-3)` locally uniformly on every
safe compact `K`.  GAP-Z asks for

```text
sum_N sup_{sigma in K}|ZERO_N(sigma)|<infinity.         (1.3)
```

Condition (1.3) is sufficient for local uniform convergence of `g_N`.  This
note decides whether it is logically necessary.

## 2. Absolute increment summability is stronger than convergence

### Proposition 2.1

There is a uniformly convergent sequence of holomorphic functions whose
successive sup-norm increments are not summable.

### Proof

On any domain take the constant functions

```text
f_N=(-1)^N/N.                                          (2.1)
```

Then `f_N->0` uniformly, but

```text
|f_{N+1}-f_N|=1/N+1/(N+1),                             (2.2)
```

whose series diverges. `QED`

Therefore GAP-Z, as an absolute variation statement for the isolated ZERO
piece, is not a necessary condition for the convergence half of IDENT.

## 3. A weaker holomorphic criterion

### Theorem 3.1 - normal-family convergence criterion

Let `D` be a domain and let `(f_N)` be a locally bounded sequence of
holomorphic functions on `D`.  Suppose there is a set `S subset D` with an
accumulation point in `D` such that `f_N(s)` converges for every `s in S`.
Then `f_N` converges locally uniformly on `D` to a holomorphic function.

### Proof

Local boundedness makes the family normal.  Every subsequence has a locally
uniformly convergent subsubsequence.  Any two sublimits agree on `S`, hence on
`D` by the identity theorem.  Thus there is only one possible sublimit.  If the
full sequence failed to converge locally uniformly, a subsequence staying a
fixed distance from that limit on some compact would possess a convergent
subsubsequence, a contradiction. `QED`

Put

```text
F_{L,N}(s)=d/ds log C_{L,N}(s),  Re s>1.                (3.1)
```

This is holomorphic because `C_{L,N}` is holomorphic and zero-free there.
Applied to the sequence `(F_{L,N})`, Theorem 3.1 replaces absolute shell
variation by

```text
VITALI-Z:
  (a) local boundedness of the finite logarithmic derivatives on Re s>1;
  (b) pointwise convergence on a safe set with an interior accumulation
      point.                                           (3.2)
```

`VITALI-Z` is sufficient for fixed-`L` convergence.  As an abstract
convergence hypothesis it is strictly weaker than absolute variation, by
Proposition 2.1.  No converse failure is asserted here specifically for the
CCM family without constructing such a family.

## 4. One-point reduction under coherent positive increments

For the Poisson kernel

```text
P_sigma(x)=2 sigma/(x^2+sigma^2),                       (4.1)
```

consider increments

```text
h_k(sigma)=int P_sigma(x) d mu_k(x),                    (4.2)
```

where each signed measure has the symmetric coherent form

```text
mu_k=epsilon_k(-delta_{-b_k}+delta_{-a_k}
                         +delta_{a_k}-delta_{b_k}),
0<a_0<=a_k<b_k.                                        (4.3)
```

### Proposition 4.1

If `sum_k h_k(sigma_0)<infinity` at one `sigma_0>0`, then
`sum_k h_k(sigma)` converges locally uniformly for `sigma>0`.

### Proof

Direct calculation gives

```text
P_sigma(a)-P_sigma(b)
 = 2 sigma(b^2-a^2)/((a^2+sigma^2)(b^2+sigma^2)).       (4.4)
```

Hence, on `sigma in [alpha,beta]`, the ratio of (4.4) to the same expression
at `sigma_0` is

```text
(sigma/sigma_0)
 ((a^2+sigma_0^2)(b^2+sigma_0^2))
 /((a^2+sigma^2)(b^2+sigma^2)).                        (4.5)
```

For `a>=a_0` and `b>=a`, this ratio is bounded by a constant depending only on
`alpha,beta,sigma_0,a_0`.  Since every `h_k` is nonnegative, the Weierstrass
test proves the assertion. `QED`

This is a genuine one-point reduction, but only after theorem-grade coherence
and a uniform exclusion of atoms from the origin.  The available archive does
not prove those hypotheses for the isolated `ZERO_N` cloud differences.

## 5. Consequence for the work allocation

There are now three nested convergence targets:

```text
GAP-Z      => absolute local variation of the isolated ZERO increments;
VITALI-Z   => normality plus pointwise convergence on a uniqueness set;
CONV-Z     => local uniform convergence of the total finite derivative.

GAP-Z => VITALI-Z => CONV-Z,                            (5.1)
```

and neither converse follows formally.  Downstream IDENT uses `CONV-Z`, not
the absolute variation asserted by GAP-Z.  Thus GAP-Z is infrastructure only
in the precise sense that it is one sufficient route to the needed convergence;
it is not the arithmetic identification and it is not the minimal convergence
hypothesis.

The proof-facing replacement is:

```text
MIN-CONV:
  prove either GAP-Z, or prove VITALI-Z directly for the bilateral
  logarithmic derivatives.                            (5.2)
```

This replacement preserves build-neutrality.  It does not use a zeta-only
signature and cannot imply the arithmetic anchor by itself.

## 6. Status

```text
proved:
  GAP-Z is sufficient but not necessary for finite-section convergence;
  the VITALI-Z criterion;
  a one-point Poisson summability theorem under coherent symmetric shifts;

closed:
  the minimality audit of GAP-Z;

reduced:
  the convergence front from the single mandatory target GAP-Z to the
  disjunction GAP-Z or VITALI-Z;

open:
  GAP-Z itself;
  alternatively, local boundedness and uniqueness-set convergence in VITALI-Z;
  coherence for the actual isolated ZERO cloud;

next:
  audit whether the mu-free disk-intersection front supplies VITALI-Z or is a
  logically separate LP obligation.
```
