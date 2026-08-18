# D.27 — Audit of the Szego tower at the central weight

## Result

The Lorentzian Szego spaces of D.20--D.21 are correct finite Hodge spaces,
but they cannot be the comparison target for the nuclear form of rows B--C.
They use the Szego parameter `r_n=n^(-1)`, whereas the central Tate
normalization fixed by row C requires `r_n=n^(-1/2)`.  The change is not a
convention: it changes a summable tail into the critical divergent Euler
boundary.

## 1. General normalized Szego vector

For `0<r<1`, put

```text
h_r(z)=sqrt(1-r^2)/(1-rz)=a_r 1 + R_r,
a_r=sqrt(1-r^2),       ||R_r||^2=r^2.               (1.1)
```

For a finite label set `S`, the proof of the primitive Hodge inequality in
D.20 uses

```text
||R_S||^2 <= ||R_S||_HS^2 = sum_(n in S) r_n^2.     (1.2)
```

Thus its uniform contraction is controlled by the square sum of the
Szego parameters.

## 2. Weight used by the finite theorem

D.20 sets

```text
r_n=n^(-1),
```

so

```text
sum_(n=p^k) r_n^2
 =sum_p sum_(k>=1) p^(-2k)
 =sum_p 1/(p^2-1)<1.                                (2.1)
```

This proves the uniform primitive gap recorded there.  The argument and
its equality case are valid for that auxiliary form.

## 3. Weight forced by B--C

The self-dual metric character is

```text
w_(1/2)(Gamma_n)=n^(-1/2).
```

For the prime tower `n=p^k`, row C therefore contains

```text
Lambda(n)/sqrt(n) = (log p) p^(-k/2).               (3.1)
```

The exact periodic Poisson identity D.23 consequently uses

```text
r_p=p^(-1/2),
```

whose `k`-th Fourier coefficient is `r_p^k=p^(-k/2)`.  If one instead
labels every prime power separately, the corresponding Szego parameter is

```text
r_(p^k)=p^(-k/2)=n^(-1/2).                          (3.2)
```

At this parameter, (1.2) becomes

```text
sum_p sum_(k>=1) r_(p^k)^2
 =sum_p sum_(k>=1)p^(-k)
 =sum_p 1/(p-1)=infinity.                           (3.3)
```

The divergence already occurs in the first-prime layer by divergence of
`sum_p 1/p`.

## 4. No isometric comparison to D.20

Suppose a comparison sends the torsor label `n` to the D.20 Szego vector
and preserves the row-C central contact coefficient.  The coefficient of
the first winding would have to be simultaneously `n^(-1)` (D.20) and
`n^(-1/2)` (row C).  They differ for every `n>1`.  Hence no such
term-by-term isometry exists.

Equivalently, replacing `n^(-1)` by the required `n^(-1/2)` destroys the
uniform Hilbert--Schmidt contraction on which the Hodge proof rests.

### Corollary

The comparison obligations (D.20 (16), D.21 (9)) cannot be fulfilled for
the displayed auxiliary Szego form.  D.20--D.21 remain independent finite
Lorentzian models, not approximants of `B_nuc`.

## 5. Correct consequence

The critical divergence (3.3) is the same divergence cancelled by the
matched Gamma--Euler finite part.  Therefore the correct approximants must
join the ordinary-prime vacuum and the Gamma boundary **before** taking
the norm or inertia.  No primewise Hilbert--Schmidt estimate can prove D at
the central weight.

The admissible finite object is the paired difference of D.23,

```text
B_P(F,F)=||S_P F||^2-||B_P F||^2,                   (5.1)
```

with the common divergent vacuum retained until the archimedean
renormalization is applied.  A finite Hodge theorem for (5.1) must be
proved by a joint Schur complement or a signed global transfer.  The
subcritical theorem D.20 cannot supply it by continuity because the
contraction constants tend through the critical divergence, not to a
number below one.

