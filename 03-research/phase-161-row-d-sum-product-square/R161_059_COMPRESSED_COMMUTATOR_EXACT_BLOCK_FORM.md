# R161_059 — Exact block form of the compressed commuting pair

## 1. Compression identity

Let P be an orthogonal projection, Q=I-P, let A=A* and let Z be bounded on a common core. Assume the full-space commutation

    AZ=ZA.                                                (1.1)

On PH put

    H=PAP,   B=PZP,
    X=QAP,   Y=QZP,   Ybar=QZ*P.                         (1.2)

Then

    boxed: [H,B]=Ybar* X-X*Y.                            (1.3)

Proof. Insert Q=I-P:

    HB=PAPZP
      =PA(ZP-QZP)
      =PZAP-PAQZP
      =PZPAP+PZQAP-PAQZP
      =BH+Ybar*X-X*Y.

This is an exact finite block identity. It shows that compression of a commuting global pair creates a crossed product of the exterior A-port and the two orientations of the exterior Z-history.

Similarly,

    [H,B*]=Y*X-X*Ybar.                                  (1.4)

## 2. Evaluation on a radical vector

If H>=0 and Hf=0, then

    HBf=[H,B]f=Ybar*Xf-X*Yf,                            (2.1)

and

    HB*f=[H,B*]f=Y*Xf-X*Ybar f.                         (2.2)

The positive double commutator of R161_058 is

    <f,[B*,[H,B]]f>
      =<Bf,HBf>+<B*f,HB*f>.                             (2.3)

Substitution of (2.1)-(2.2) expresses it as four crossed exterior pairings. It is not the norm of Xf, Yf or Ybar f separately. In particular, global commutation does not give a negative exterior square; it gives the indefinite products in (1.3)-(1.4).

## 3. Reflection

If JAJ=A, JP=PJ and JZJ=Z*, reflection exchanges Y and Ybar and preserves X up to the parity of the source. On a parity radical vector it therefore exchanges the two positive terms of (2.3), reproducing R161_058(2.1). It does not change their sign and does not make either crossed product in (1.3) vanish.

## 4. Tate projection

For the primitive compression replace P by the physical projection followed by the orthogonal primitive projection Pi. The same insertion of I=Pi+(I-Pi) inside the physical window adds finite-rank Tate blocks to (1.3). R161_009 determines their coefficients, and R161_043 kills the Xf source-derivative Tate pairing when it occurs literally. The bulk crossed products Ybar*X-X*Y remain.

Thus the Tate correction removes normal coordinates but does not transform the compressed commutator into a square.

## 5. Consequence for PC-ren

For the phase-161 choices, Xf is the exterior Weil image, while Yf and Ybar f are the two one-sided Poisson histories. Formula (1.3) is the operator version of the exterior ordering remainder in R161_023, R161_044 and R161_057.

The desired identity

    0=<f,[B*,[H,B]]f>+D_N^Gamma(F)                       (5.1)

does not follow from full-space commutation plus radicality. A proof from PC-ren must add a relation identifying the crossed products in (1.3) with a negative Gamma/polar boundary form. This relation is exactly the missing quadratic exterior reciprocity; the block expansion does not manufacture it.

## 6. Status

- compressed commutator formula (1.3)-(1.4): proved;
- exact identification of its crossed exterior ports: proved;
- reduction to a negative square from commutation/reflection/Tate alone: rejected;
- additional PC-ren exterior reciprocity: open;
- D: open.
