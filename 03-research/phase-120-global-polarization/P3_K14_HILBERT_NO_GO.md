# K_(1/4): ordinary Hilbert trace no-go

Status: proved obstruction to a Gram realization. The transmission itself
is now constructed as the unitary determinant scattering in
`P3_GLOBAL_SCATTERING_GREEN_IDENTITY.md`. This file is not paper text.

## 1. The determinant boundary multiplier

The quarter determinant scattering is

    b_infty(tau)=pi^(-i tau)
      Gamma(1/4+i tau/2)/Gamma(1/4-i tau/2),

and its logarithmic boundary derivative is

    a_infty(tau)=g_Gamma(tau)-m_0
      =Re psi(1/4+i tau/2)-log pi.                  (1)

At `tau=0`, `a_infty(0)=-m_0<0`. By the digamma asymptotic,

    a_infty(tau)=log(|tau|/(2 pi))+O(tau^(-2)),

so it is positive for all sufficiently large `|tau|`. Hence (1) changes
sign.

## 2. Consequence for K_(1/4)

There is no Hilbert-space operator `K` on a dense translation-invariant core
whose boundary Gram is (1):

    K^*K=M_(a_infty).                                (2)

Indeed every `K^*K` is positive, whereas a multiplier is positive exactly
when its symbol is nonnegative almost everywhere. The sign change contradicts
(2).

Equivalently, `b_infty` is boundary-unitary but not a one-sided inner
transfer with the required orientation: its meromorphic continuation has
upper-half-plane poles at `tau=i(2n+1/2)`. Thus a causal Hilbert Calderon
operator cannot realize its signed connection.

## 3. Correct type of the transmission

The Gamma boundary must remain the paired determinant relation

    (free connection, Markov delay),

with its Real opposite orientation, in a Krein/Pontryagin boundary space.
Only after it is Redheffer-coupled to the matrix-valued degree/contact system
may an ordinary positive external defect emerge. The positive map
`W_Gamma` constructs the Markov reservoir but is not, by itself, the signed
degree--Gamma transmission.

Therefore equation (13) of `P3_LITERAL_STATE_SYSTEM.md` is a placeholder of
the wrong Hilbert type if interpreted as a Gram map. The admissible object is
the unitary determinant scattering `K_(1/4)=M_(b_infty)`. Its signed
connection is recovered by

    K_(1/4)^*QK_(1/4)-Q=M_(g_Gamma-m_0),

not by `K_(1/4)^*K_(1/4)`. In a one-sided port presentation the equivalent
object is a `J`-unitary boundary relation

    K_(1/4)^J : H_degree direct-sum H_Gamma^-
                  -> H_degree direct-sum H_Gamma^+, (3)

whose two Gamma components are kept paired and whose Potapov--Ginzburg
transform is taken only after D.247 has supplied the contact ports.

## 4. What is and is not closed

The obstruction and the correct operator class are fixed. The bilateral
unitary and its zero-residual global Green elimination are constructed in
`P3_GLOBAL_SCATTERING_GREEN_IDENTITY.md`. What remains is conversion of that
signed commutator into the positive primitive square by the matrix-valued
degree/contact completion.
