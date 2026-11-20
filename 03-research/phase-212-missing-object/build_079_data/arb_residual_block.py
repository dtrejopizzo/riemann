"""Validated principal block of BUILD083 (69), retaining every mixed term.

Default: first eight even low coordinates, same frozen 16-mode corrector.
The odd sector uses its own frozen corrector and the odd reflected action.
Positive LDL certifies this principal block only, never the full 95-block.
"""
import argparse
import json
from pathlib import Path
from hashlib import sha256
from time import perf_counter
import mpmath as mm
from flint import arb,arb_poly,ctx
from frozen_corrector import reconstruct
from polynomial_source import pieces
from arb_source_integral import (from_endpoints,load_source,prepare,Moments,
                                 approximate_inner,check_known)
from arb_residual_diagonal import legendre
from arb_moment_convolution import functional
from arb_native_gram import pairings
from arb_source_batch import build_sources

FOLDER = Path(__file__).parent


class ArbContext:
    mpf = staticmethod(arb)
    sqrt = staticmethod(lambda x: arb(x).sqrt())
    log = staticmethod(lambda x: arb(x).log())
    @property
    def pi(self): return arb.pi()
    @property
    def euler(self): return arb.const_euler()


def ldl(matrix):
    n = len(matrix)
    L = [[arb(int(i==j)) for j in range(n)] for i in range(n)]
    D = []
    for i in range(n):
        pivot = matrix[i][i]-sum((L[i][k]**2*D[k] for k in range(i)),arb(0))
        D.append(pivot)
        if not pivot > 0: return False,D
        for j in range(i+1,n):
            L[j][i] = (matrix[j][i]-sum((L[j][k]*L[i][k]*D[k] for k in range(i)),arb(0)))/pivot
    return True,D


def integrate(sources,T,degree=512,maximum=111):
    count = len(sources)
    assert count and sources[0]
    assert all(len(source) == len(sources[0]) for source in sources)
    # All sources come from pieces() at the same exact T and therefore share
    # exact contact endpoints; overlap of balls alone would not establish this.
    basis = [legendre(T,n) for n in range(maximum+1)]
    B = [[arb(0) for _ in range(count)] for _ in basis]
    G = [[arb(0) for _ in range(count)] for _ in range(count)]
    errors = [arb(0) for _ in range(count)]
    moments = Moments()
    for piece,(a,b,_) in enumerate(sources[0]):
        local = []
        for i,source in enumerate(sources):
            f,e,length = prepare(source[piece][2],a,b,T,degree,piece==0,piece==len(source)-1)
            local.append(f)
            errors[i] += e**2
        tests = [p(arb_poly([a,b-a])) for p in basis]
        moment_block,gram_block = pairings(local,tests,moments)
        for i in range(count):
            for n in range(maximum+1): B[n][i] += length*moment_block[n,i]
            for j in range(i,count):
                value = length*(gram_block[i,j]+gram_block[j,i])/2
                G[i][j] += value
                if i != j: G[j][i] += value
        print('Integrated piece',piece,flush=True)
    errors = [e.upper().sqrt().upper() for e in errors]
    assert all(G[i][i].upper() >= 0 for i in range(count))
    norms = [G[i][i].upper().sqrt().upper() for i in range(count)]
    for n in range(maximum+1):
        for i in range(count): B[n][i] += arb(0,errors[i])
    for i in range(count):
        for j in range(i,count):
            error = (errors[i]*norms[j]+errors[j]*norms[i]+errors[i]*errors[j]).upper()
            G[i][j] += arb(0,error)
            G[j][i] = G[i][j]
    return B,G,errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--columns',type=int,default=8)
    parser.add_argument('--parity',choices=('even','odd'),default='even')
    parser.add_argument('--source-method',choices=('direct','batch'),default='direct')
    args = parser.parse_args()
    count = args.columns
    parity = args.parity
    assert 1 <= count <= 95
    ctx.dps = 500
    mm.iv.dps = 400
    check_known()
    start = perf_counter()
    frozen_path = FOLDER/f'frozen_corrector_{parity}_160.json'
    frozen = json.loads(frozen_path.read_text())
    assert frozen['degree'] == 111 and frozen['N'] == 95 and frozen['T'] == '4/5'
    assert frozen['parity'] == parity
    print('Reconstructing',count,'real columns',flush=True)
    built = reconstruct(mm.iv,frozen,selected=range(count))
    U = [[from_endpoints(x._mpi_) for x in u] for u in built['U_legendre']]
    physical = [[from_endpoints(x._mpi_) for x in u] for u in built['U_physical']]
    W = [{n:from_endpoints(x._mpi_) for n,x in w.items()} for w in built['W']]
    assert len(W) == 16 and all(len(u)==112 for u in U)
    kernel_record = json.loads((FOLDER/'kernel_polynomial_certificate.json').read_text())
    assert kernel_record['degree'] == 384
    kernel = [arb(x) for x in kernel_record['coefficients']]
    if args.source_method == 'batch':
        sources = build_sources(physical,kernel,1 if parity=='even' else -1)
        print('Assembled',count,'sources with shared matrices',flush=True)
    else:
        native = ArbContext()
        sources = []
        for i,f in enumerate(physical):
            assembled = pieces(native,f,kernel,1 if parity=='even' else -1)
            sources.append([(a,b,[arb_poly(p) for p in s]) for a,b,s in assembled])
            print('Assembled source',i,flush=True)
    # Independent old interval construction and native one enclose the same
    # coefficients of column 0. Agreement is a cross-check, not the proof.
    if parity == 'even':
        meta,old = load_source(FOLDER/'real_source_even_0.json.gz')
        assert meta['frozen_corrector_sha256'] == sha256(frozen_path.read_bytes()).hexdigest()
        for (_,_,source),(_,_,reference) in zip(sources[0],old):
            for p,q in zip(source,reference):
                pc,qc = p.coeffs(),q.coeffs()
                for j in range(max(len(pc),len(qc))):
                    assert (pc[j] if j<len(pc) else arb(0)).overlaps(qc[j] if j<len(qc) else arb(0))
    B,GV,errors = integrate(sources,arb(4)/5)
    delta = [[sum((coefficient*B[n][i] for n,coefficient in w.items()),arb(0))
              for i in range(count)] for w in W]
    criterion = [[arb(0) for _ in range(count)] for _ in range(count)]
    theta = arb(1)/10**20
    rho = arb(1783)/500
    for i in range(count):
        for j in range(i,count):
            # Both expressions enclose the same exact symmetric S entry.
            S = sum((U[i][n]*B[n][j]+U[j][n]*B[n][i] for n in range(112)),arb(0))/2
            gamma = GV[i][j]-sum((B[n][i]*B[n][j] for n in range(96)),arb(0))
            GU = sum((u*v for u,v in zip(U[i],U[j])),arb(0))
            defect = sum((row[i]*row[j] for row in delta),arb(0))
            value = S-rho*(1+theta)*gamma-8*(1+theta)*defect-GU/10**35-4*GV[i][j]/10**187
            assert value.is_finite()
            criterion[i][j] = criterion[j][i] = value
    positive,pivots = ldl(criterion)
    prior_overlap = None
    prior_path = FOLDER/f'real_residual_block_{parity}_8.json'
    if count >= 8 and prior_path.exists():
        prior = json.loads(prior_path.read_text())
        assert prior['frozen_corrector_sha256'] == sha256(frozen_path.read_bytes()).hexdigest()
        prior_overlap = all(criterion[i][j].overlaps(arb(prior['criterion'][i][j]))
                            for i in range(8) for j in range(8))
        assert prior_overlap
    report = dict(status='POSITIVE_PRINCIPAL_BLOCK' if positive else 'LDL_INDETERMINATE',
                  scope=f'first {count} {parity} low coordinates plus the infinite high space; not global positivity',
                  count=count,parity=parity,T='4/5',decimal_digits=500,kernel_degree=384,smooth_log_degree=512,
                  moment_method='native_hankel_convolution_and_matrix_products',
                  source_method=args.source_method,
                  prior_eight_block_overlap=prior_overlap,
                  frozen_corrector_sha256=sha256(frozen_path.read_bytes()).hexdigest(),
                  criterion=[[str(x) for x in row] for row in criterion],
                  pivots=[str(x) for x in pivots],moments=[[str(x) for x in row] for row in B],
                  source_gram=[[str(x) for x in row] for row in GV],
                  moment_errors=[str(x) for x in errors],seconds=perf_counter()-start)
    destination = FOLDER/f'real_residual_block_{parity}_{count}.json'
    if args.source_method == 'batch':
        destination = FOLDER/f'real_residual_block_{parity}_{count}_batch.json'
    base_destination = destination
    serial = 1
    while destination.exists():
        destination = base_destination.with_name(f'{base_destination.stem}_run{serial}.json')
        serial += 1
    destination.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ('criterion','moments','source_gram','moment_errors')},indent=2))


if __name__ == '__main__':
    main()
