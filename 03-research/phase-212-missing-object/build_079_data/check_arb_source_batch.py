"""Compare a full-degree batched source against the preserved real column."""
import json
from pathlib import Path
from hashlib import sha256
from time import perf_counter
import mpmath as mm
from flint import arb,ctx
from frozen_corrector import reconstruct
from arb_source_integral import from_endpoints,load_source
from arb_source_batch import build_sources


def main():
    folder = Path(__file__).parent
    ctx.dps = 500
    mm.iv.dps = 400
    frozen_path = folder/'frozen_corrector_even_160.json'
    frozen = json.loads(frozen_path.read_text())
    built = reconstruct(mm.iv,frozen,selected=[0])
    column = [from_endpoints(x._mpi_) for x in built['U_physical'][0]]
    kernel_file = folder/'kernel_polynomial_certificate.json'
    kernel = [arb(x) for x in json.loads(kernel_file.read_text())['coefficients']]
    archive = folder/'real_source_even_0.json.gz'
    meta,reference = load_source(archive)
    assert meta['frozen_corrector_sha256'] == sha256(frozen_path.read_bytes()).hexdigest()
    start = perf_counter()
    result = build_sources([column],kernel,1)[0]
    elapsed = perf_counter()-start
    checked = 0
    radius = arb(0)
    for (_,_,source),(_,_,old) in zip(result,reference):
        for p,q in zip(source,old):
            pc,qc = p.coeffs(),q.coeffs()
            for j in range(max(len(pc),len(qc))):
                actual = pc[j] if j<len(pc) else arb(0)
                expected = qc[j] if j<len(qc) else arb(0)
                assert actual.overlaps(expected)
                radius = max(radius,actual.rad())
                checked += 1
    assert radius < arb('1e-180')
    report = dict(status='PASS_SOURCE_CROSSCHECK',input_degree=111,kernel_degree=384,
                  decimal_digits=500,columns=1,coefficient_comparisons=checked,
                  maximum_radius=str(radius),assembly_seconds=elapsed,
                  frozen_corrector_sha256=sha256(frozen_path.read_bytes()).hexdigest(),
                  reference_sha256=sha256(archive.read_bytes()).hexdigest(),
                  scope='source assembly only; no new matrix or sign certificate')
    (folder/'arb_source_batch_check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__': main()
