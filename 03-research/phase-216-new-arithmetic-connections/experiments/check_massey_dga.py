"""Exact integral checks for the exterior DGA of FRONT-03. No Galois realization asserted."""
import json
from pathlib import Path

def add(x, y):
    z = dict(x)
    for k,v in y.items(): z[k] = z.get(k,0)+v
    return {k:v for k,v in z.items() if v}

def scale(x,n): return {k:n*v for k,v in x.items() if n*v}

def mul(x,y):
    z={}
    for i,a in x.items():
        for j,b in y.items():
            if i&j: continue
            inversions=sum(1 for p in range(4) for q in range(4) if i>>p&1 and j>>q&1 and p>q)
            z=add(z,{i|j:a*b*(-1)**inversions})
    return z

def differential(x,L):
    dg=[{}, {}, {3:1}, {5:L}]
    out={}
    for mask,coef in x.items():
        bits=[i for i in range(4) if mask>>i&1]
        for pos,g in enumerate(bits):
            prefix=sum(1<<i for i in bits[:pos])
            suffix=sum(1<<i for i in bits[pos+1:])
            out=add(out,scale(mul(mul({prefix:1},dg[g]),{suffix:1}),coef*(-1)**pos))
    return out

def check(p,N):
    L=p**N
    basis=[{i:1} for i in range(16)]
    for x in basis: assert differential(differential(x,L),L)=={}
    for i,x in enumerate(basis):
        for y in basis:
            assert differential(mul(x,y),L)==add(mul(differential(x,L),y),scale(mul(x,differential(y,L)),(-1)**i.bit_count()))
    assert differential({10:1},L)=={7:L} # b u -> L a b c
    assert differential({12:1},L)=={11:1} # c u -> a b u
    assert differential({4:1},L)=={3:1}
    assert differential({8:1},L)=={5:L}
    for mask in [3,5,9,6]: assert differential({mask:1},L)=={}
    minimum=next(e for e in range(N+1) if p**(3*e)%L==0)
    assert minimum==(N+2)//3
    return {'prime':p,'N':N,'minimal_simultaneous_scale':minimum,'d_squared_basis_checks':16,'leibniz_basis_pair_checks':256}

if __name__=='__main__':
    results=[check(p,N) for p in [2,3,5] for N in range(1,7)]
    target=Path(__file__).with_name('massey-dga-resultados.json')
    target.write_text(json.dumps({'scope':'Finite exact algebra checks; general proof in FRONT-03; no arithmetic realization.', 'cases':results},indent=2)+'\n')
    print(f'PASS: {len(results)} cases, 288 d² and 4608 Leibniz checks; scale ceil(N/3).')
