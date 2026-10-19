# R161_056 — The finite unitary phase has the wrong tangent

## 1. Chain-rule audit

Work in the s variable and put

    A=Z_N(s),  B=Z_N(1-s),  e=Au-B.

Use the coherent orientations of R161_036:

    U=-Z_N'(s)u=-A'u,
    V=-Z_N'(1-s).

Because differentiation of B=Z_N(1-s) gives

    B'= -Z_N'(1-s)=V,

we have

    e'=A'u+Au'-B'=-U+Au'-V,

and therefore

    U+V=-e'+Au'.                                      (1.1)

This is the exact mean identity already obtained in R161_036 and R161_041.

Now consider the unimodular quotient

    theta=Au/B.

Its logarithmic derivative is

    theta'/theta=A'/A+u'/u-B'/B.                       (1.2)

On the Poisson locus Au=B, multiplication by B turns (1.2) into

    B theta'/theta=A'u+Au'-B'=e'.                     (1.3)

Off that locus the equality has the corresponding finite defect terms, but its leading orientation is unchanged. Thus the unitary phase tangent differentiates the Poisson difference. It controls the mean U+V after the Gamma correction; it does not control U-V.

## 2. The critical difference belongs to the complementary sum

Define

    c=Au+B.

Then

    c'=A'u+Au'+B'=-U+Au'+V,

so

    boxed: U-V=-c'+Au'.                                (2.1)

Equation (2.1) is the closing critical jet. At a zeta zero its limit is the nonzero multiple of zeta' described in R161_036-R161_037.

The key structural fact is that c is an additive sum of the two histories. It is not a unit-modulus quotient and does not define a unitary multiplication colligation. Therefore the exact Toeplitz-Hankel defect of R161_052 cannot be transferred to the critical jet merely by covariant differentiation.

## 3. Consequences for R161_052--R161_055

1. The finite multiplier theta is genuinely unimodular and its Toeplitz-Hankel leakage identities remain correct.
2. The canonical lift x_N and (U_N-I)x_N=E_N^ren F remain correct.
3. The diagonal graph argument proving equality of undifferentiated metrics remains correct.
4. The proposed identification of the unitary phase tangent with the coherent critical difference is false.
5. The two-orientation squeeze would still close D if an independent PC/Tate calculation identified the reverse exterior norms, but the unitary quotient does not supply that identification.

Thus the new colligation organizes the base Poisson transport but does not solve the terminal differentiated boundary problem. The simultaneous object still required is a quadratic Green identity mixing the small difference e with the complementary sum c, exactly as isolated in R161_041-R161_044.

## 4. Status

- sign and chain-rule audit: proved;
- base unitary colligation: retained;
- unitary tangent as critical jet: rejected;
- mixed e--c Green identity with polar/Tate boundary sign: open;
- D: open.
