# E72.282 -- Root-energy proof of VBG

**Purpose.** Prove the variance-bracket gate with exponent `beta=1`.

E72.280 reduced the bracket to

```text
VBG(beta):
sup_{0<tau_j<=H} ||S_tau_j xi_x|| = O_H(L^beta),
```

with any `beta<3/2` sufficient for the diagonal HPAC compact-root term.  This note proves VBG with
`beta=1`.

## Root energies

Let

```text
d_n=2pi n/L,
||xi||_2=1,
S_tau(d_n)=1/(tau-d_n)+1/(tau+d_n).
```

Define

```text
E_-(tau)=sum_n xi_n^2/(tau-d_n)^2,
E_+(tau)=sum_n xi_n^2/(tau+d_n)^2.
```

Then

```text
||S_tau xi|| <= sqrt(E_-(tau))+sqrt(E_+(tau)).              (RE-1)
```

It is enough to prove `E_-(tau_j),E_+(tau_j)=O_H(L^2)` at finite Weyl roots.

## Mesh lemma

Let `h=2pi/L`.  For any real `tau` and any mesh point `d_j` closest to `tau`, all other mesh points
satisfy

```text
|tau-d_n| >= (1/2)|n-j|h,        n != j.
```

Therefore

```text
sum_{n != j} |tau-d_n|^(-2) <= C L^2.                     (MESH)
```

The same estimate holds with `tau+d_n` in place of `tau-d_n`.

## Weyl-root control of the closest pole

At a finite Weyl root,

```text
sum_n xi_n/(tau_j-d_n)=0.                                  (ROOT)
```

Let `j` be a closest pole for `tau_j`.  Then

```text
|xi_j|/|tau_j-d_j|
= |sum_{n != j} xi_n/(tau_j-d_n)|
<= (sum_{n != j} xi_n^2)^(1/2)
   (sum_{n != j} |tau_j-d_n|^(-2))^(1/2)
<= C_H L.
```

Thus the closest-pole contribution satisfies

```text
xi_j^2/(tau_j-d_j)^2 <= C_H L^2.                         (NEAR)
```

For the remaining terms,

```text
sum_{n != j} xi_n^2/(tau_j-d_n)^2
<= max_{n != j} |tau_j-d_n|^(-2) sum_{n != j}xi_n^2
```

or, more sharply, by `(MESH)` and `sum xi_n^2=1`,

```text
sum_{n != j} xi_n^2/(tau_j-d_n)^2 <= C_H L^2.              (FAR)
```

Combining `(NEAR)` and `(FAR)` gives

```text
E_-(tau_j) <= C_H L^2.
```

Because `xi` is even, the finite-root relation also gives

```text
sum_n xi_n/(tau_j+d_n)=0,
```

and the same argument proves

```text
E_+(tau_j) <= C_H L^2.
```

Using `(RE-1)`,

```text
sup_{0<tau_j<=H} ||S_tau_j xi_x|| <= C_H L.
```

This is VBG with `beta=1<3/2`.

## Consequence

Together with E72.278--E72.279:

```text
mu_x^(-1)<a_s^perp,S_tau_jxi_x> -> 0
```

uniformly for fixed Cauchy compact `K` and fixed root height `0<tau_j<=H`, assuming the pole-even gap
`mu_x>=cL^2`.

Thus the **diagonal compact-root term is closed**.

What remains in the compact-root HPAC theorem is the commutator-invisibility term of E72.277, plus the
high-root tail and the final divisibility passage.

## Probe

Run:

```text
python3 E72_282_root_energy_vbg_probe.py
```

Output:

```text
E72.282 root-energy VBG probe
E_-(tau)=sum (xi_n/(tau-d_n))^2, E_+(tau)=sum (xi_n/(tau+d_n))^2.
VBG follows from ||S_tau xi|| <= sqrt(E_-)+sqrt(E_+) = O(L).
lam L roots maxE- maxE+ max||Sxi|| sqrtMaxE/L maxRootNull
 16 5.545177     7 6.030697e-03 6.030697e-03 1.018889e-01 1.400452e-02 7.903e-12
 20 5.991465     7 2.597700e-02 2.597700e-02 2.200618e-01 2.690057e-02 1.398e-12
 24 6.356108     5 2.209217e-03 2.209217e-03 5.441412e-02 7.394825e-03 3.601e-16
 28 6.664409     6 3.536163e-03 3.536163e-03 7.659785e-02 8.922868e-03 2.624e-14
 32 6.931472     8 7.881069e-04 7.881069e-04 3.001751e-02 4.050113e-03 9.327e-15
```

The numerical values are much smaller than the theorem requires; the theorem only needs the
`O_H(L)` vector bound.
