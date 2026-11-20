# Correction of the residual cancellation in L2_BUILD_031

Status: **PROVED by exact computation; literal audits approved.** No numerical data, with a corrective notice added to the historical file 031; papers untouched.

## 1. Antecedent and corrected claim

Read: the project rules, ROUTES-TRIED-INDEX/README.md and 06_OPEN_RESIDUES_DEAD_SUBROUTES.md (R9), grid R162_2300_MASTER_GRID, CROSSWORD-TO-D, P47 problem (S), P48 problem (S), L2_BUILD_030 and N_BUILD_022. The exact antecedent is

 `03-research/phase-188-closing-D/L2_BUILD_031_RESIDUE_BALANCED_SUBSPACE.md`.

Its section 1 defines (B_Q) through constant blocks whose length is a multiple of the modulus. The UNWEIGHTED sum of a Ramanujan sum over a complete block does vanish. The parenthetical remark already labels ARGUED its extension to the full pairing and warns that multiplying the index by n only transports balance if p does not divide n. However, section 3 presents as an identity the omission of all components of modulus p^b<=Q on (B_Q). Here that omission is refuted in the full pairing defined in 030, with an explicitly admissible smooth interpolation. Neither Theorem E nor the sign of the actual form is refuted.

## 2. All objects fixed

Take M=Q=2, q_Q=2, I={1,2} and s1=s2=1. This is a single balanced block (B_Q): one even class and one odd class with the same weight. Choose the norm-1 profile with

 0<2T0<log(3/2).

Its autocorrelation c0 is supported in [-2T0,2T0] and c0(0)=1. Hence for m=1,2 and EVERY integer j>=1,

 W1(m,j)=c0(log(m/j))=delta_mj.

Indeed, the minimal nonzero logarithmic distance between one of 1,2 and another positive integer is log(3/2).

Fix S smooth with compact support in (2/3,5/2), with S(1)=S(2)=1. For example, if eta(x)=exp(1-1/(1-x^2)) for |x|<1 and 0 outside, take

 S(x)=eta(12(x-1))+eta(12(x-2)).

It is C_infinity, equals 1 at both integers and equals 0 at ALL integers j>=3; it thus interpolates the whole sequence s, extended by 0 outside {1,2}. No interpolation at non-integer points is presupposed without being declared.

## 3. Full component of modulus 2

In the Ramanujan decomposition of 030, for a positive integer j define

 T_q(j)=c_q(j) sum_(n>=1,q|n) (v_n/n)S(j/n),
 v_n=2Lambda(n)/sqrt(n), v1=0.

This formula comes from the exact identity sum_(q|n)c_q(j)=n*1_(n|j). The compact support of S, away from 0, makes each sum finite for fixed j. The pairing of the component q is

 P_q=sum_(m=1)^2 s_m sum_(j>=1)W1(m,j)T_q(j)
    =T_q(1)+T_q(2).

For j=1,2 and n>=3 one has j/n<=2/3 and S(j/n)=0. For n=2, S(1/2)=0 and S(2/2)=S(1)=1. Therefore there are no other contributions to q=2:

 T_2(1)=0,
 T_2(2)=c_2(2)*(v2/2)*S(1)=v2/2,
 P_2=v2/2=log(2)/sqrt(2)>0.

Here c2(j)=(-1)^j. The original block has sum_(k=1)^2 c2(k)=0, but the multiplication n=2 gives sum_(k=1)^2 c2(2k)=2. The pairing computation above is stronger than this observation: it also fixes S, W1, all n and all indices that can contribute; it leaves no hidden cancellation from other powers of 2.

As a control, the q=1 component of these two rows is also v2/2; together they reproduce the exact n=2 term of V on the vector s. The result is not a comparison of isolated components with ARCH.

## 4. Correction and scope

The identity of section 3 of 031 must keep the small components; it cannot delete them merely by (B_Q). The same correction applies to the sentences of its section 4 that attribute that cancellation to (B_Q). The proof of Theorem E by approximation of configurations uses only continuity and short blocks in the logarithmic coordinate: it remains valid and does NOT depend on Ramanujan. Nor does the trivial cancellation of sums over complete residue systems without the other weights change.

The general interpolation of 030 section 3 was already labelled ARGUED; this example shows that the smooth choice declared here does not supply the intended cancellation. It is not claimed that every conceivable interpolation gives the same individual component; precisely, a universal cancellation claim needs additional hypotheses. The total identities of 030 and problem (S) are not modified.

This note gives neither a negative value of W nor a new global obstruction: it corrects a concrete local algebraic step that cannot be used to eliminate arithmetic components of the full pairing. The historical file 031 keeps its original text and receives a notice pointing to this audited correction.


## 5. Universal repair on rough support: only the zero vector

**PROVED, restricted scope; audits of the main argument, cases and map.** Let Q>=2 and s finite in R_Q, with support <=M. Suppose its modulus-2 component vanishes for ALL allowed profiles and ALL compactly supported smooth interpolants S of the sequence. Choosing 2T0<log((M+1)/M) makes W1(m,j)=delta_mj for m<=M and EVERY j>=1. All j in the support are odd. In the q2 pairing, varying S by a bump at the non-integer point x=j/2 isolates the coefficient -s_j v2/2: a coincidence j'/2^a=j/2 would force j'=2^(a-1)j; since j' is odd, a=1 and j'=j. The bump can avoid the integers and the other relevant ratios (locally finite), preserving the prescribed interpolation. Universal vanishing forces s_j=0 for each j. Thus adding rough support does NOT repair the universal cancellation except on the null space.

This collapse is not extended to mixed support: the ratios j/2^a collide inside dyadic rays. Examples for profiles so narrow that W1 is the identity do not decide the requirement over ALL profiles. In particular, for support up to 4 the identity of all columns needs width<log(5/4); width<log2 is not enough. No general collapse result is recorded here. The original Theorem E remains intact; a new restriction to the exact kernel of components would require a new approximation proof.
