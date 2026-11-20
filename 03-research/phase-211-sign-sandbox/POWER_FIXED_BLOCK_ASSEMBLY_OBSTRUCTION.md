# PSD assembly by blocks of bounded size in the power basis

Status: **PROVED analytic; mathematical and literal audits of cases approved.** No new computations nor changes to papers. Only a precise class of certificates in the original basis is excluded; the sign of matrices of arbitrary order is not decided.

## 1. Antecedents and difference of object

Consulted the project rules, ROUTES-TRIED-INDEX01–06, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; cross-searches for diagonal dominance, scaled diagonal dominance, factor-width, sparse SOS and k-local certificates. Relevant readings: POWER_CONE_001§§1–3, POWER_BRIDGE_002; R186_043§7, R186_044§3.3 and N_BUILD018/019. This literal obstruction of bounded coordinate support was not found; no world novelty of the classical instrument of sparse PSD matrices is claimed.

R186_043–044 delimit Gershgorin and M-matrix structures in other coupling blocks; they do not prove that every change of basis fails. N018 deals with computation of multipliers via identities and Cauchy–Schwarz; N019 deals with arithmetic SOS and measures on logarithmic lags. Here the exact class changes: sums of PSD matrices, each supported on at most k COORDINATES of the power basis of002. This class is not identified with all certificates.

## 2. An elementary necessary condition

Fix k>=1. If a real symmetric matrix B is PSD and is supported on S×S, |S|<=k, then

 ones^T B ones <= k tr(B).                             (LOCAL)

Indeed a decomposition of B as a sum of vv^T has each vector supported on S; Cauchy–Schwarz gives (sum_i v_i)^2<=|S|sum_i v_i². Summing proves LOCAL. No sign of the individual entries is needed.

By linearity, every decomposition C=sum_alpha B_alpha into PSD matrices of support <=k satisfies

 ones^T C ones <= k tr(C).                             (NECESSARY)

This includes finite sums and the matrix limits of such sums: NECESSARY is a closed inequality. Positive coefficients can be absorbed into B_alpha. The class is preserved under invertible diagonal congruences, because they change neither supports nor PSD.

## 3. Blocks of the SAME fixed ladder002

Use the complete kernel of001

 K(a,b)=[L(a)+L(b)]/(a+b-1),
 L(a)=1/a+1/(a-1)-(log pi)/2+psi(a/2)/2+zeta'(a)/zeta(a).

For fixed k, put n=k+1 and, for integers N>=1,

 a_j=32+2N+2j, u_j=a_j-1/2, j=0,...,k.

They are nodes of the fixed ladder a=32+m of002, not a family foreign to the bridge. The positive real representation of001 gives L(a_j)>0. For each fixed k,

 L(a_j)=.5 log N+O_k(1), uniformly j=0,...,k.        (ASYM)

This is proved without evaluating special functions: a_j/2=N+16+j integer, psi(a_j/2)=H_(N+15+j)-gamma and the integral comparisons of harmonic sums give H_(N+15+j)=log N+O_k(1). The two rational terms are O(1/N). The arithmetic tail is included:

 |zeta'(a)/zeta(a)|=sum_(m>=2)Lambda(m)m^(-a)
 <=sum_(m>=2)m^(1-a)
 <=2^(1-a)[1+2/(a-2)] ->0, a->infinity.

Thus ASYM keeps the whole complete form, without discarding the comb to obtain an unproved sign.

Normalize the block by its positive diagonal:

 C_ij=K(a_i,a_j)/sqrt[K(a_i,a_i)K(a_j,a_j)]
     =[L_i+L_j]/[u_i+u_j] * sqrt[u_i u_j/(L_i L_j)].

One has C_ii=1 exactly. ASYM and u_i/u_j->1 imply C_ij->1 for all i,j. Hence

 ones^T C ones -> n² > kn = k tr(C).

There exists a sufficiently large finite integer N for which NECESSARY fails strictly. It is not required to determine N nor to perform a search. In that real block of the ladder002 there does NOT exist a sum of PSD matrices of support <=k in the declared basis. By diagonal invariance, nor does one exist for the unnormalized block K. If a larger initial block of the ladder002 admitted a decomposition with supports of size<=k, its principal submatrix at these nodes would inherit the same property, by restriction of each PSD summand. This contradicts the above and connects the obstruction with the concrete initial blocks of the bridge002.

## 4. Diagonal dominance and scope

The case k=2 includes certificates by sums of PSD blocks of size2. Absolute scaled diagonal dominance also fails directly: if C has3 nodes and all C_ij>1/2 for i!=j, the conditions x_i>=sum_(j!=i)|C_ij|x_j with x_i>0 are incompatible upon summing them. Continuous confluence or the late blocks above produce that situation. That this criterion fails does not imply that C is indefinite.

For EVERY fixed k there appears some block of size k+1 that does not admit the declared assembly. Thus the whole ladder cannot be closed by summing only PSD certificates supported on sets of 2,4,13 or any other FIXED number of original coordinates, even allowing all such subsets and positive weights.

It has not been proved that the excluded block has a negative direction. The proof does not presuppose its PSD. General changes of basis, blocks whose size grows, Schur complements, decompositions with a dense global PSD part and other signed controls of crossings are not excluded. No failure is attributed to the existing positive results of finite dimensions; only this local assembly rule for all orders is excluded. Global W and the complete ladder remain OPEN.
