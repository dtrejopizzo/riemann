# R161_011 — Typed scattering audit of the product-Hardy closure

## 0. Verdict

The product regularisation is a genuine advance, but `R161_010`, Theorem 3.1 is not proved as written.  The
phase-116 Gamma--co-Poisson identity does not add the two untransformed physical ports.  Its derivation changes the
left Mellin orientation by the additive cosine transform.  After reflection to the causal orientation, the typed
first-contact equation has the form

```
g_+(F) + C_log R g_-(F) = 0,                                     (0.1)
```

up to the fixed sign determined by the parity convention, not `g_+(F)+g_-(F)=0`.  Here `C_log` is the unitary
cosine transform transported to logarithmic coordinates and `R` is logarithmic reflection.

Because `R g_-` and `g_+` are both supported in `[T,infinity)`, equation (0.1) says that the product port lies in a
cosine/Sonin gap eigenspace.  Such gap spaces are nontrivial.  Disjoint-support uniqueness therefore cannot be
used.

The route is not discarded.  It has reduced closure to a sharper new statement: the arithmetic product-port range
must have trivial intersection with the relevant Sonin eigenspace on a first-contact radical.

## 1. Where the cosine transform enters

Phase 116 proves on the primitive smooth core

```
C Z_+ = Z_+ R,                                                     (1.1)
Z_+(B_+ + B_-) = D_Gamma Z_+,                                    (1.2)
Z_+ A_infinity = [Z_+,D_Gamma].                                  (1.3)
```

Equation (1.2) is obtained by differentiating (1.1).  Thus the reflected Euler orientation reaches the common
scalar graph only after applying `C`.  The source explicitly labels its literal exterior localisation
(451)--(453) as `AUDIT`, and later proves that the canonical scalar two-contour shadow has Krein, not Hilbert,
inertia.

The sentence in `R161_010` claiming that phase 116 supplies the same commutator “with the two exterior supports
retained rather than supertraced” is therefore unsupported.  Retaining the supports retains two ports; taking the
scalar commutator composes one of them with the nonlocal scattering.

## 2. Why the tempting Fourier uncertainty shortcut does not work

Let

```
(Ug)(x)=x^(-1/2)g(log x),
C_log=U^(-1) C U.                                                  (2.1)
```

The left physical port has logarithmic support `(-infinity,-T]`.  However (1.1) first reflects it.  Hence

```
supp(R g_-) subset [T,infinity),                                  (2.2)
```

and (0.1) implies that both `R g_-` and its cosine transform have the multiplicative gap `(0,e^T)`.  This is the
Sonin situation, not the impossible situation of a compactly supported function whose Fourier transform vanishes
on an interval.  Nonzero Sonin functions exist, so support alone does not force either port to vanish.

For a parity source, the two product ports are reflected copies.  With the fixed convention absorbed into
`epsilon in {+1,-1}`, (0.1) reduces schematically to

```
(I+epsilon C_log)g_+(F)=0,
supp g_+(F) subset [T,infinity).                                  (2.3)
```

The old universal countermodel `(-c,+c)` has thus been replaced by a much more rigid but still nonzero
cosine-eigen Sonin space.

## 3. What survives

The audit does not affect:

- the finite Poisson--Chebyshev anomaly;
- polar renormalisation;
- exact exterior-port isolation;
- the product critical jet

  ```
  G_+(i gamma)=-zeta'(rho)K_F(i gamma);
  ```

- the first-contact `H^s`, `s>1/4`, boundary estimate;
- the finite collapse of the polar arithmetic residue to `n<e^(2T)`;
- the crossed two-Tate scalar matching.

What fails is only the inference from scalar conservation to the separate vanishing of the two ports.

## 4. Exact remaining theorem

Let `P_T^PC` be the source-defined map which sends a primitive first-contact state to its corrected right
product-Hardy port, and let

```
Son_T^epsilon={g in L2([T,infinity)) : C_log g=-epsilon g}.        (4.1)
```

The non-circular terminal lemma is

```
Ran(P_T^PC | first-contact radical) intersect Son_T^epsilon={0}.  (4.2)
```

Indeed, the typed graph identity places `P_T^PC F` in `Son_T^epsilon`.  If (4.2) holds, the product port vanishes;
its critical values give `K_F(i gamma)=0` at the unconditional superlinear family of simple critical zeros, and
Cartwright rigidity gives `F=0`.

This formulation is strictly more informative than an abstract two-contour Hilbertisation.  It records the extra
arithmetic range restriction supplied by `Lambda*1=log`.  A proof of (4.2) may use that restriction; declaring the
whole Sonin graph positive would be equivalent to G40 and circular.

## 5. First chamber above `0.8`

For

```
0.8<T<(log 5)/2,
```

the polar and interior arithmetic data of `P_T^PC` contain only `n=2,3,4`.  The next construction is therefore the
finite range-intersection test

```
Ran(P_T^(2,3,4) | ker(P_T A_T P_T)) intersect Son_T^epsilon={0}.  (5.1)
```

The useful output is not another scalar norm.  One must derive an additional boundary equation satisfied by
`P_T^(2,3,4)F` but not by a general Sonin eigenfunction.  The two candidates carried by the present construction
are:

1. the differentiated product law coming from `[Q,Z_+]=Z_+B_+`;
2. the arithmetic-free first collar, where the local co-Poisson observation equals `F` before the first delay
   `log 2`.

Either candidate need only force vanishing on one nonempty boundary collar.  The phase-121 infinitesimal
gap-enlargement theorem then shortens both endpoints by parity and contradicts minimal first contact.

## 6. Status correction

- `R161_010`, Theorem 3.1: **RETRACTED AS PROVED**;
- typed cosine-scattering identity: **the correct target; smooth-core germ known, physical product-port boundary
  still to be written explicitly**;
- Sonin range-intersection lemma (4.2): **OPEN**;
- row D: **OPEN**.

