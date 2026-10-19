"""P201.2: rank defect delta of the Siegel-Dyson system (3.1) over ideals.
Blocks by norm N = N(a)N(b), a,b ideals with N(a),N(b) <= X; columns (a,b);
rows k=0..t-1: sum a_{a,b} node(b)^k = 0.
generic: node(b) = sum_P ord_P(b) x_P (one variable per prime ideal; specialized to large random integers: exact lower bound of the generic rank, equal to min(t,#distinct b) by Vandermonde).
evaluated: node(b) = f(N b) with f injective (rank equal to that of log N b); f = id is used. Exact rational arithmetic."""
from fractions import Fraction
import random, itertools, json
random.seed(201)
X = 24  # floor(e^{16/5}) = floor(24.53)

def primes(n): return [p for p in range(2,n+1) if all(p%q for q in range(2,p))]

def prime_ideals(field):
    """list of (name, norm). field in {'Z','Qi','Qsqrt-5'}"""
    out=[]
    for p in primes(X):
        if field=='Z': out.append((f'p{p}',p))
        elif field=='Qi':
            if p==2: out.append(('P2',2))
            elif p%4==1: out+= [(f'P{p}',p),(f'P{p}b',p)]
            elif p*p<=X: out.append((f'({p})',p*p))
        else:  # Q(sqrt-5), disc -20
            if p in (2,5): out.append((f'P{p}',p))
            elif p%20 in (1,3,7,9): out+= [(f'P{p}',p),(f'P{p}b',p)]
            elif p*p<=X: out.append((f'({p})',p*p))
    return out

def ideals(field):
    P=prime_ideals(field); res=[((),1)]
    for name,nm in P:
        new=[]
        for exps,n in res:
            e=0; m=n
            while m<=X:
                new.append((exps+((name,e),) if e else exps, m)); e+=1; m*=nm
        res=new
    return res  # (exponents, norm)

def rank(M):
    M=[r[:] for r in M]; rk=0; cols=len(M[0]) if M else 0
    for c in range(cols):
        piv=next((i for i in range(rk,len(M)) if M[i][c]!=0),None)
        if piv is None: continue
        M[rk],M[piv]=M[piv],M[rk]
        for i in range(len(M)):
            if i!=rk and M[i][c]!=0:
                f=M[i][c]/M[rk][c]; M[i]=[a-f*b for a,b in zip(M[i],M[rk])]
        rk+=1
    return rk

def run(field,tmax=8):
    I=ideals(field); P=prime_ideals(field)
    xs={name:Fraction(random.randint(10**6,10**9)) for name,_ in P}
    gen=lambda e: sum(xs[n]*k for n,k in e)
    blocks={}
    for (ea,na),(eb,nb) in itertools.product(I,I):
        blocks.setdefault(na*nb,[]).append((ea,eb,nb))
    out={'field':field,'ideals_by_norm':{n:sum(1 for _,m in I if m==n) for n in range(1,X+1)},'t':{}}
    for t in range(1,tmax+1):
        tot=0; per={}
        for N,cols in sorted(blocks.items()):
            G=[[gen(eb)**k for ea,eb,nb in cols] for k in range(t)]
            E=[[Fraction(nb)**k for ea,eb,nb in cols] for k in range(t)]
            D=len({eb for _,eb,_ in cols}); d=len({nb for *_,nb in cols})
            rg,re=rank(G),rank(E)
            assert rg==min(t,D) and re==min(t,d)
            if rg-re: per[N]=rg-re
            tot+=rg-re
        out['t'][t]={'delta_total':tot,'blocks_nonzero':per}
    return out

if __name__=='__main__':
    R=[run(f) for f in ('Z','Qi','Qsqrt-5')]
    json.dump(R,open('p201_2_results.json','w'),indent=1,default=str)
    for r in R:
        print(r['field'],'r(n):',[r['ideals_by_norm'][n] for n in range(1,X+1)])
        print('  delta_total by t:',{t:v['delta_total'] for t,v in r['t'].items()})
    print('blocks t=2 Q(sqrt-5):',R[2]['t'][2]['blocks_nonzero'])
    print('blocks t=2 Q(i):',R[1]['t'][2]['blocks_nonzero'])
