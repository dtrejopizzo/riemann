"""Validated first diagonal of BUILD083 (69), from the fixed real source.

A positive diagonal is not a positive-definite matrix certificate.
"""
import json
from hashlib import sha256
from math import comb
from pathlib import Path
from time import perf_counter
import mpmath as mm
from flint import arb,arb_poly,ctx
from frozen_corrector import reconstruct
from arb_source_integral import load_source,from_endpoints,prepare,Moments,check_known

FOLDER = Path(__file__).parent


def legendre(T,n):
    return arb_poly([((-1)**(n+j)*comb(n,j)*comb(n+j,j))/T**j
                     for j in range(n+1)])*((2*n+1)/T).sqrt()


def source_moments(source,T,maximum=111,degree=512):
    basis = [legendre(T,n) for n in range(maximum+1)]
    moments = Moments()
    result = [arb(0) for _ in basis]
    error_squared = arb(0)
    powers = ((0,0),(1,0),(0,1))
    for i,(a,b,s) in enumerate(source):
        local,error,length = prepare(s,a,b,T,degree,i==0,i==len(source)-1)
        change = arb_poly([a,length])
        for n,p in enumerate(basis):
            test = p(change)
            pairing = arb(0)
            for f,(left,right) in zip(local,powers):
                pairing += sum((v*moments.get(k,left,right)
                                for k,v in enumerate((test*f).coeffs())),arb(0))
            result[n] += length*pairing
        error_squared += error**2
        print('Projected piece',i,flush=True)
    error = error_squared.upper().sqrt().upper()
    return [b+arb(0,error) for b in result],error


def main():
    ctx.dps = 500
    mm.iv.dps = 400
    check_known()
    archive = FOLDER/'real_source_even_0.json.gz'
    meta,source = load_source(archive)
    previous = json.loads((FOLDER/'real_source_integral.json').read_text())
    assert previous['source_sha256'] == sha256(archive.read_bytes()).hexdigest()
    assert meta['column_index'] == 0 and meta['parity'] == 'even' and meta['kernel_degree'] == 384
    frozen_path = FOLDER/'frozen_corrector_even_160.json'
    assert meta['frozen_corrector_sha256'] == sha256(frozen_path.read_bytes()).hexdigest()
    frozen = json.loads(frozen_path.read_text())
    assert frozen['degree'] == 111 and frozen['N'] == 95 and frozen['T'] == '4/5'
    start = perf_counter()
    B,error = source_moments(source,arb(4)/5)
    built = reconstruct(mm.iv,frozen,physical=False,selected=[0])
    U = [from_endpoints(x._mpi_) for x in built['U_legendre'][0]]
    W = [{n:from_endpoints(x._mpi_) for n,x in w.items()} for w in built['W']]
    assert len(U) == len(B) == 112 and len(W) == 16
    assert all(b.is_finite() for b in B)
    GV = arb(previous['enclosure'])
    gamma = GV-sum((b*b for b in B[:96]),arb(0))
    S = sum((u*b for u,b in zip(U,B)),arb(0))
    delta = [sum((value*B[n] for n,value in w.items()),arb(0)) for w in W]
    delta_squared = sum((d*d for d in delta),arb(0))
    GU = sum((u*u for u in U),arb(0))
    theta = arb(1)/10**20
    rho = arb(1783)/500
    criterion = (S-rho*(1+theta)*gamma-8*(1+theta)*delta_squared
                 -GU/10**35-4*GV/10**187)
    report = dict(status='ENCLOSED',scope='only coordinate diagonal 0 of (69); not a PSD matrix certificate',
                  parity='even',column_index=0,decimal_digits=500,
                  source_sha256=previous['source_sha256'],
                  moments=[str(b) for b in B],moment_truncation_error=str(error),
                  GV=str(GV),Gamma_tail=str(gamma),S_XK=str(S),GU=str(GU),
                  solve_defect_squared=str(delta_squared),criterion_diagonal=str(criterion),
                  criterion_strictly_positive=bool(criterion > 0),seconds=perf_counter()-start)
    (FOLDER/'real_residual_diagonal.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ('moments',)},indent=2))


if __name__ == '__main__':
    main()
