# E72.360 - Log-derivative projector identity

## 1. Purpose

E72.359 gives a local double-residue certificate for `CFIR-DIV`, but it still names the local zeros.
This note gives the contour version using `Z'/Z`.  It is the bridge from local ideal membership to a
global finite-window identity of the same type as the explicit formula.

## 2. What `Z'/Z` can and cannot project

Let `a` be a zero of `Z` of multiplicity `m`, and let `F` be holomorphic near `a`.  Then

```text
Res_{z=a} F(z) Z'(z)/Z(z) dz = m F(a).
```

This extracts only the value `F(a)`, with multiplicity weight.  It does not extract higher Hermite
coefficients from holomorphic test functions.  Therefore:

```text
simple zeros:
  Z'/Z contour sums are enough.

multiple zeros:
  use the 1/Z principal-part projectors of E72.359,
  or allow local meromorphic dual tests with prescribed poles.
```

This distinction is load-bearing.  A proof that uses only holomorphic `Z'/Z` tests proves the
simple-zero version of the divisor block, not the full Hermite multiplicity statement.

## 3. Two-variable log-derivative projector

For simple zeros, define

```text
L_{a,0;b,0}[Delta]
:= Res_{z=a} Res_{w=b}
   Delta(z,w)
   Z'(z)/Z(z) Z'(w)/Z(w) dz dw.                      (1)
```

Therefore:

```text
Delta in (Z(z),Z(w))
```

locally at a simple pair `(a,b)` if and only if

```text
L_{a,0;b,0}[Delta]=0.
```

For multiple zeros, the correct projectors remain the E72.359 projectors

```text
Pi_{a,r;b,s}[Delta]
= Res Res (z-a)^{m-r-1}(w-b)^{n-s-1}
  Delta(z,w)/(Z(z)Z(w)) dz dw.
```

Equivalently one may use `Z'/Z` only after multiplying by meromorphic local dual tests whose principal
parts encode the missing Hermite derivatives.  Those tests are local algebra data, not global
holomorphic test functions.

## 4. Finite-window contour sum

Let `Omega_T` be a zero-avoiding contour enclosing a finite Xi-zero window.  For any holomorphic
two-variable kernel `Delta(z,w)` on a neighborhood of the window,

```text
(1/(2pi i)^2) int_{Omega_T} int_{Omega_T}
 Delta(z,w) A(z)B(w) Z'(z)/Z(z) Z'(w)/Z(w) dw dz
```

equals the finite double sum over simple zeros inside the window:

```text
sum_{a,b in W_T} m_a m_b Delta(a,b) A(a)B(b)
```

For multiple zeros, replace this by the E72.359 `1/Z` projectors or by meromorphic local dual tests.

Thus the simple-zero part of `CFIR-DIV` is equivalent to the vanishing, up to polynomial error, of a
finite family of such double contour sums.  The full Hermite statement still uses E72.359.

## 5. Root-free formulation

Instead of naming each zero locally, one may state the window certificate as:

```text
For every pair of holomorphic test functions A,B on a simple-zero window,

  (1/(2pi i)^2) int int
  Delta_CFIR(z,w) A(z)B(w) Z'/Z(z) Z'/Z(w) dw dz
  = O_T(L^B).
```

This is root-free at the proof level for simple windows: the contour encloses the window, and the
zeros enter only as residues of `Z'/Z`.  For multiple windows, the root-free statement must be made
with the principal-part projectors of E72.359.

## 6. Why this matters

The node-blind identity `Delta=0` is false by E72.355.  For simple zeros, the local divisor identity

```text
Delta in (Z(z),Z(w))
```

is exactly equivalent to saying all `Z'/Z` double-residue probes vanish.  For multiplicities, the
same role is played by the finite principal-part projectors.  This is the right place to use the
completed explicit formula again in the simple-zero channel:

```text
Z'/Z = polar + archimedean - prime Dirichlet series.
```

The next analytic proof can therefore attack `CFIR-DIV` by expanding these double contour sums into
finite archimedean-prime terms and checking whether the Feshbach equation cancels them before any
absolute values are taken.

## 7. Status

```text
proved: for simple zeros, CFIR-DIV is equivalent to finite-window double Z'/Z contour identities;
corrected: holomorphic Z'/Z tests do not recover higher Hermite multiplicity slots;
open: use E72.359 principal-part projectors for multiplicities;
open: expand the simple-zero CFIR double contour using the completed explicit formula and prove cancellation.
```
