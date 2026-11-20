"""Quantitative L2 lower bound from a validated residual principal block.

Count 95 covers the entire stated parity; a smaller count covers only its
tested low directions plus the infinite high complement, at T=4/5.
"""
import argparse
import json
from pathlib import Path
from hashlib import sha256
from flint import arb,arb_mat,ctx


def certify(matrix_path,congruence_path,corrector_path):
    paths = list(map(Path,(matrix_path,congruence_path,corrector_path)))
    matrix,certificate,frozen = [json.loads(p.read_text()) for p in paths]
    assert certificate['matrix_sha256'] == sha256(paths[0].read_bytes()).hexdigest()
    assert matrix['frozen_corrector_sha256'] == sha256(paths[2].read_bytes()).hexdigest()
    assert matrix['T'] == frozen['T'] == '4/5' and frozen['N'] == 95 and frozen['degree'] == 111
    assert matrix['kernel_degree'] == 384
    ctx.dps = 500
    count = matrix['count']
    assert 1 <= count <= 95
    assert len(matrix['criterion']) == len(matrix['source_gram']) == count
    assert len(certificate['preconditioner_dyadic']) == count
    assert all(len(row)==count for row in matrix['criterion']+matrix['source_gram']+certificate['preconditioner_dyadic'])
    assert all(matrix['criterion'][i][j] == matrix['criterion'][j][i]
               for i in range(count) for j in range(count))
    M = arb_mat([[arb(x) for x in row] for row in matrix['criterion']])
    P = arb_mat([[arb(tuple(x)) for x in row] for row in certificate['preconditioner_dyadic']])
    assert all(P[i,j].rad()==0 for i in range(count) for j in range(count))
    # Replay the certificate rather than trusting its PASS label or margins.
    B = P*M*P.transpose()
    margins = [(B[i,i].lower()-sum((B[i,j].abs_upper() for j in range(count) if i!=j),arb(0))).lower()
               for i in range(count)]
    delta = min(margins)
    assert delta > 0
    Pnorm2 = sum((P[i,j]**2 for i in range(count) for j in range(count)),arb(0)).upper()
    s = (delta/Pnorm2).lower()
    assert len(frozen['X']) == 16 and all(len(row)==95 for row in frozen['X'])
    y2 = sum((arb(row[i])**2 for row in frozen['X'] for i in range(count)),arb(0)).upper()
    g = sum((arb(matrix['source_gram'][i][i]) for i in range(count)),arb(0)).upper()
    assert g >= 0
    eta = arb(1)/10**370
    E2 = arb(27)/20
    U2 = (E2+(1+eta)*y2).upper()
    ell = ((1+eta).sqrt()*y2.sqrt()+8*(g.sqrt()+U2.sqrt()/10**35)).upper()
    bound = min(arb(1)/16,(s/(E2+2*ell**2)).lower()).lower()
    assert bound > 0
    return dict(status='PASS_UNIFORM_BOUND',T='4/5',parity=frozen['parity'],low_count=count,
                scope='full parity' if count==95 else f'first {count} low directions plus infinite high complement',
                matrix_sha256=certificate['matrix_sha256'],
                congruence_sha256=sha256(paths[1].read_bytes()).hexdigest(),
                corrector_sha256=matrix['frozen_corrector_sha256'],
                coordinate_s_lower=str(s),coupling_norm_upper=str(ell),
                L2_lower_bound=str(bound),source_trace_upper=str(g),decimal_digits=500)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('matrix',type=Path)
    parser.add_argument('congruence',type=Path)
    parser.add_argument('corrector',type=Path)
    args = parser.parse_args()
    report = certify(args.matrix,args.congruence,args.corrector)
    args.matrix.with_name(args.matrix.stem+'_uniform_bound.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__': main()
