# V1.1' exact computation: M_T^X(g) per SPEC_201 §C.1, rank and certified nonnegative rank.
# Entries are rationalized (den 2^40) from mpmath values of v_n^X g(log(m/k)); kappa swept on a mesh
# (constants + random rational per-cell values). Rank/r_+ computed EXACTLY in Q on those rationals.
import json, math, random, itertools
from fractions import Fraction as F
import mpmath as mp
mp.mp.dps=30
random.seed(201)
def Q(x): return F(int(mp.nint(mp.mpf(x)*2**40)),2**40)
def mangoldt(n):
    for p in range(2,n+1):
        if n%p==0:
            m=n
            while m%p==0: m//=p
            return mp.log(p) if m==1 else 0
    return 0
def comb_Lambda(N,c=1,drop=()):
    out={}
    for n in range(2,N+1):
        L=mangoldt(n)
        if L and not any(n%p==0 for p in drop): out[n]=c*L
    return out
LQ=json.load(open('/home/trabajo/Documentos/research/riemann/03-research/phase-200-sign-object/LEMMA_E_EPSTEIN_001_data/lambdaQ_exact.json'))
def comb_epstein(N):
    out={}
    for n,d in LQ.items():
        n=int(n)
        if n<=N:
            s=sum(mp.mpf(F(v).numerator)/F(v).denominator*mp.log(int(p)) for p,v in d.items())
            if s!=0: out[n]=s
    return out
def comb_DH(N):
    s5=mp.sqrt(5); kap=(mp.sqrt(10-2*s5)-2)/(s5-1)
    CHI={1:(1,0),2:(0,1),3:(0,-1),4:(-1,0),0:(0,0)}
    a=lambda n: CHI[n%5][0]+kap*CHI[n%5][1]
    B={}
    for n in range(2,N+1):
        B[n]=a(n)*mp.log(n)-sum(a(d)*B[n//d] for d in range(2,n) if n%d==0)
    return {n:b for n,b in B.items() if b!=0}
def comb_beurling(N):
    # synthetic Beurling primes (FAMILIES_A §4 rule): 2,3,5.1,7.05,11.03,13.02 ; prime powers
    P=[2,3,5.1,7.05,11.03,13.02]; out={}
    for p in P:
        k=1
        while p**k<=N+1e-12: out[p**k]=mp.log(p); k+=1
    return out
def gfam(T,coef):
    def g(x):
        t=x/(2*T)
        if abs(t)>=1: return mp.mpf(0)
        return (1-t*t)**2*sum(c*mp.legendre(2*j,t) for j,c in enumerate(coef))
    return g
def build(comb,T,g,kap):
    N=int(mp.floor(mp.e**(2*T)))
    rows=[(k,n) for n in sorted(comb) for k in range(1,N+1) if k*n<=N+1e-9]
    cols=[(m,e) for e in (-1,0,1) for m in range(1,N+2)]
    M={}
    for (k,n) in rows:
        for (m,e) in cols:
            if abs(m-k*n-e)<1e-12:
                val=2*comb[n]/mp.sqrt(n)*g(mp.log(mp.mpf(m)/k))-kap(m,k)
                q=Q(val)
                if q>0: M[((k,n),(m,e))]=q
    return rows,cols,M
def rank(A):
    A=[r[:] for r in A]; r=0
    if not A: return 0
    nc=len(A[0])
    for c in range(nc):
        p=next((i for i in range(r,len(A)) if A[i][c]!=0),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        for i in range(len(A)):
            if i!=r and A[i][c]!=0:
                f=A[i][c]/A[r][c]; A[i]=[a-f*b for a,b in zip(A[i],A[r])]
        r+=1
    return r
def solve_nonneg(cols_vecs,target):
    # exact: find lambda>=0 with sum lambda_i v_i = target (v_i independent): least-squares via normal eqs
    k=len(cols_vecs); G=[[sum(a*b for a,b in zip(cols_vecs[i],cols_vecs[j])) for j in range(k)] for i in range(k)]
    h=[sum(a*b for a,b in zip(cols_vecs[i],target)) for i in range(k)]
    A=[G[i]+[h[i]] for i in range(k)]
    for c in range(k):
        p=next(i for i in range(c,k) if A[i][c]!=0); A[c],A[p]=A[p],A[c]
        for i in range(k):
            if i!=c: f=A[i][c]/A[c][c]; A[i]=[a-f*b for a,b in zip(A[i],A[c])]
    lam=[A[i][k]/A[i][i] for i in range(k)]
    ok=all(sum(lam[i]*cols_vecs[i][r] for i in range(k))==target[r] for r in range(len(target)))
    return lam if ok and all(l>=0 for l in lam) else None
def block_cert(B):
    # B: list of rows (3 columns). Returns (rank, size of exact nonneg factorization found)
    r=rank(B)
    if r==0: return 0,0
    C=[[row[j] for row in B] for j in range(len(B[0]))]
    nz=[j for j in range(len(C)) if any(C[j])]
    for S in itertools.combinations(nz,r):
        if rank([[C[j][i] for j in S] for i in range(len(B))])<r: continue
        if all(solve_nonneg([C[j] for j in S],C[t]) is not None for t in nz if t not in S):
            return r,r     # B = B[:,S] * H, H>=0 exact  => r_+ = r
    return r,len(nz)       # fallback: B = B * I
def analyse(comb,T,g,kap,scale=None):
    rows,cols,M=build(comb,T,g,kap)
    if scale: M={key:v*scale(key[0]) for key,v in M.items()}
    Mat=[[M.get((r,c),F(0)) for c in cols] for r in rows]
    R=rank(Mat)
    # block decomposition by j = m - e
    blocks={}
    for (r,c) in M: blocks.setdefault(c[0]-c[1],set()).add(r)
    up=0; br=0; offblock=0
    for (r,c) in M:
        if c[0]-c[1]!=r[0]*r[1]: offblock+=1
    for j in blocks:
        bc=[(j+e,e) for e in (-1,0,1)]
        B=[[M.get((r,c),F(0)) for c in bc] for r in sorted(blocks[j])]
        rr,ss=block_cert(B); br+=rr; up+=ss
    return dict(N=len(rows),ncols=len(cols),nnz=len(M),rank=R,sum_block_rank=br,rplus_lower=R,rplus_upper=up,
                I=up-R,offblock=offblock,support=sorted([[list(a),list(b)] for a,b in M]))
