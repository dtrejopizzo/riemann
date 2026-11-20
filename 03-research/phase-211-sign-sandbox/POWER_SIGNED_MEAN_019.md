# POWER_SIGNED_MEAN_019 — Signed mean of dilations and truncated inversion that loses positivity

Status: PROVED sign of an arithmetic mean of dilations for all N and explicit falsifier of positivity of its truncated inversion. OPEN the original mean ERR. No paper is modified.

## 1. Corpus and new reason, with declared limit

Read the project rules, LOW_TABLE018, TATE_CHAIN009 and PACKET_SCOPE009; index ROUTES-TRIED-INDEX (INV_H/K, Euler/Möbius N_018, PROOF_L_SHARP_F/J and their corrections), grid part3 and CROSSWORD-TO-D (Euler–Maclaurin and floor classes). The identities Λ*1=log, their Möbius inversion and the reformulations with factorials already belong to those routes. They are NOT presented as new tools by renaming them.

The bounded difference is to apply that grouping to the exact POSITIVE kernel of ERR018 and prove which sign it really preserves: the mean over ALL dilations has an elementary negative sign. When trying to recover the original mean, a natural positivity hypothesis on the inverse weight already fails in the first three dilates of the SAME gamma kernel, with explicit large N. The result is not a NO-GO for signed means nor a proof of the original row.

## 2. Original mean and kernel

Keep u=63/2, g_N=y^(N−1)e^-uy/(N−1)!, C_N=c_gN, c0=C_N(0), and

    E0(x)=psi_Lambda(x)−x+1, x>=1,
    H_N(x)=−(d/dx)[x^-1/2 C_N(logx)]/c0
          =x^-3/2[(1/2)rho_N(logx)−rho_N'(logx)]>0,
    rho_N=C_N/c0.

LOW018 proves

    F_N=2∫_1^infinity H_N(x)E0(x)dx,
    W[g_N]/c0=Arch_sharp[g_N]/c0−F_N.                  (ERR)

The endpoint E0(1)=0 is kept. This is the original residue, whose sign is not presumed.

## 3. Grouping by integers: exact sign before inverting

For x>=1 and n=floorx, the divisor identity gives

    Σ(m<=x)psi_Lambda(x/m)
       =Σ(q<=x)Lambda(q)floor(x/q)=log(n!).

Hence

    B(x):=Σ(m<=x)E0(x/m)=log(n!)−xH_n+n,               (B)
    H_n=Σ(j=1..n)1/j.

This B is negative for ALL x>1. At integers,

    B(n+1)−B(n)=log(n+1)−H_n<0,

because H_n>∫_1^(n+1)dt/t. Between integers its slope is−H_n. More precisely,

    B(x)<=−(1−log2)(x−1).                              (NEG)

To see it, H_n−log(n+1) increases from1−log2, since its differences are1/(n+1)−log(1+1/(n+1))>0. The slopes between integers satisfy the same comparison. This is an elementary inequality on the real grouping at the integers, not a consequence of taking absolute values of the Chebyshev error.

Integrating against H_N>0 proves the sign of an infinite SIGNED mean:

    A_N:=2∫_1^infinity H_N(x)Σ(m<=x)E0(x/m)dx
       <=−2(1−log2)J_N(1/2)<0, for ALL N>=2,          (MEAN)

where J_N(b)=∫_0^infinity e^(bt)rho_N(t)dt. We used ∫H_N(x)(x−1)dx=∫x^-1/2 C_N(logx)dx/c0=J_N(1/2), by integration by parts. All sums and integrals converge absolutely for each N: H_N decays like x^-33 times a polynomial in logx.

MEAN is a sign result on a concrete mean of dilations. It is NOT the sign of F_N: all E0(x/m) appear, not only m=1. That carrier difference is not omitted.

## 4. Which additional hypothesis the inversion would require

The correct adjoint inversion, including its Jacobian, is

    h_N(x)=Σ(m>=1)mu(m)m H_N(mx), x>=1.                (INV)

Σmu(m)H_N(mx) does not suffice: the factor m is missing. The series converges absolutely for each N, since its term is O_N(m^-32 times a polynomial in logm). Its inversion satisfies Σ(d>=1)d h_N(dy)=H_N(y), and Fubini gives exactly

    F_N=2∫_1^infinity h_N(x)B(x)dx.                    (PAIR)

If one had h_N>=0, NEG would imply F_N<=0. Even that would not suffice by itself for W>=0: one would also have to reach the negative deficit of Arch_sharp. But the inverse positivity premise is not automatic and the following proof shows an explicit failure in its most elementary local approximation.

## 5. Falsifier in the SAME gamma kernel: the first three inverses

For all N>=2^17 define

    h_N^[3](1)=H_N(1)−2H_N(2)−3H_N(3).

Then

    h_N^[3](1)<−19/256<0.                              (FAIL3)

Proof without tables. The spectral probability of g_N has second moment M2=u²/(2N−3)<1/128. For0<=t<=2,

    rho_N(t)>=1−t²M2/2>=1−2M2,
    rho_N'(t)<=0,
    (1/2)rho_N(t)−rho_N'(t)>=1/2−M2>63/128.

These are applied at log2,log3<2. Moreover H_N(1)=1/2 and1/sqrt2+1/sqrt3>2/3+1/2=7/6. Hence

    h_N^[3](1)
       <1/2−(63/128)(7/6)=−19/256.

It is not claimed that the FULL h_N is negative at1: the terms m>=4 could change the sign. FAIL3 refutes exactly the lemma «inversion by dilations preserves positivity in each prefix» for the original kernels, not for a modified model. Nor is the possibility excluded of controlling the full signed inverse weight via an additional inequality.

## 6. Genuine missing variant and why the identity above does not prove it

The information lost by recovering m=1 is the compensation between the positive and negative parts of h_N in PAIR. A valid continuation would have to keep that signed pairing with the SAME B(x)<0, or compare one-sidedly the contribution of m>=2 in MEAN with the term m=1. It cannot replace h_N by its modulus nor assume its prefixes positive.

A concrete formulation of the requirement, keeping an explicit arithmetic object, is the inequality

    2∫ h_N^+(x)[−B(x)]dx
       −2∫ h_N^−(x)[−B(x)]dx
        >=−Arch_sharp[g_N]/c0.                         (SIGNED)

By PAIR it is sufficient and exact for the sign of this row. Here SIGNED is an OPEN obligation, not a proved lemma; writing it does not by itself provide sign progress. A constructive variant must produce a one-sided bound for the second term that uses the divisor relation and the specific form of H_N, without cancelling the favourable contribution of the first. The cited Euler/Möbius/EM routes already exhausted the identity without such an inequality; FAIL3 shows why the local positivity proposal does not supply that additional hypothesis.

The original row for all N remains unresolved. Kept as a new bounded result: the MEAN sign for the mean of dilations and the falsifier FAIL3, together with the precise identification of the sign datum that the inversion does not automatically preserve.
