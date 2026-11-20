"""Generate and preserve one real corrected source, without a sign claim."""
import gzip
import json
from hashlib import sha256
from pathlib import Path
from time import perf_counter
import mpmath as mm
from frozen_corrector import reconstruct
from polynomial_source import rational, pieces, source_value

FOLDER = Path(__file__).parent


def pack(x):
    """Exact dyadic interval endpoints; no decimal rounding on persistence."""
    return [list(endpoint) for endpoint in x._mpi_]


def unpack(ctx,x): return ctx.make_mpf(tuple(tuple(endpoint) for endpoint in x))


def verify_archive(ctx,path):
    """Read gzip/JSON and check every binary endpoint survives reconstruction."""
    data = json.loads(gzip.decompress(Path(path).read_bytes()))
    count = 0
    for a,b,source in data['pieces']:
        for encoded in [a,b]+[x for poly in source for x in poly]:
            assert pack(unpack(ctx,encoded)) == encoded
            count += 1
    return count


def main():
    c = mm.iv
    c.dps = 400
    parity,column = 'even',0
    path = FOLDER/f'frozen_corrector_{parity}_160.json'
    frozen = json.loads(path.read_text())
    start = perf_counter()
    built = reconstruct(c,frozen,selected=[column])
    print('Column reconstructed',flush=True)
    kernel_record = json.loads((FOLDER/'kernel_polynomial_certificate.json').read_text())
    assert kernel_record['degree'] == 384
    kernel = [rational(c,x) for x in kernel_record['coefficients']]
    source = pieces(c,built['U_physical'][0],kernel,1)
    print('Source assembled',flush=True)
    widths = [x.b-x.a for _,_,s in source for p in s for x in p]
    assert max(widths) < c.mpf('1e-180')
    values = []
    T = c.mpf(4)/5
    for a,b,s in source:
        value = source_value(c,s,(a+b)/2,T)
        assert value.b-value.a < c.mpf('1e-180')
        values.append(str(value))
    encoded = [[pack(a),pack(b),[[pack(x) for x in p] for p in s]] for a,b,s in source]
    # Verify that constructing intervals from endpoint tuples preserves every bit.
    decoded = [(unpack(c,a),unpack(c,b),[[unpack(c,x) for x in p] for p in s])
               for a,b,s in encoded]
    for (a,b,s),(aa,bb,ss) in zip(source,decoded):
        assert a._mpi_ == aa._mpi_ and b._mpi_ == bb._mpi_
        assert all(x._mpi_ == y._mpi_ for p,q in zip(s,ss) for x,y in zip(p,q))
    artifact = dict(format='mpmath dyadic endpoint tuples',mpmath_version=mm.__version__,
                    parity=parity,column_index=column,kernel_degree=384,interval_dps=400,
                    frozen_corrector_sha256=sha256(path.read_bytes()).hexdigest(),pieces=encoded)
    data = gzip.compress(json.dumps(artifact,separators=(',',':')).encode(),mtime=0)
    target = FOLDER/'real_source_even_0.json.gz'
    target.write_bytes(data)
    count = verify_archive(c,target)
    report = dict(status='PASS',scope='one A384 U column, not the full Gram or sign matrix',
                  parity=parity,column_index=column,kernel_degree=384,input_degree=111,
                  pieces=len(source),max_polynomial_degree=max(len(p)-1 for _,_,s in source for p in s),
                  coefficient_width_bound=str(max(widths)),midpoint_values=values,
                  seconds=perf_counter()-start,artifact=target.name,
                  archive_intervals_verified=count,
                  artifact_sha256=sha256(data).hexdigest())
    (FOLDER/'real_source_check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='midpoint_values'},indent=2))


if __name__ == '__main__':
    main()
