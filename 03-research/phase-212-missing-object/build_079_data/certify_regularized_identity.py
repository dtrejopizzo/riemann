"""Local positivity of J in BUILD083 (131), including epsilon R*R.

Replays the existing congruences; no reintegration and no global claim.
"""
import json
from pathlib import Path
from hashlib import sha256
from flint import arb
from certify_uniform_subspace_bound import certify

FOLDER=Path(__file__).parent


def main():
    records=[]
    for parity in ('even','odd'):
        matrix_path=FOLDER/f'real_residual_block_{parity}_95.json'
        congruence_path=FOLDER/f'real_residual_block_{parity}_95_congruence.json'
        corrector_path=FOLDER/f'frozen_corrector_{parity}_160.json'
        result=certify(matrix_path,congruence_path,corrector_path)
        assert result['scope']=='full parity' and result['parity']==parity
        matrix=json.loads(matrix_path.read_text())
        frozen=json.loads(corrector_path.read_text())
        eta=arb(1)/10**370
        y2=sum((arb(x)**2 for row in frozen['X'] for x in row),arb(0)).upper()
        u2=(arb(27)/20+(1+eta)*y2).upper()
        g=sum((arb(matrix['source_gram'][i][i]) for i in range(95)),arb(0)).upper()
        residual_bound=((g.sqrt()+u2.sqrt()/10**35)**2).upper()
        assert residual_bound<2000
        epsilon=arb(1)/10**20
        margin=(arb(result['coordinate_s_lower']).lower()-epsilon*residual_bound).lower()
        assert margin>0
        records.append(dict(parity=parity,status='PASS_POSITIVE_REGULARIZED_J',
                            matrix_sha256=sha256(matrix_path.read_bytes()).hexdigest(),
                            corrector_sha256=sha256(corrector_path.read_bytes()).hexdigest(),
                            residual_norm_squared_upper=str(residual_bound),
                            J_coordinate_margin_lower=str(margin)))
    report=dict(status='PASS_LOCAL_EXACT_IDENTITY',T='4/5',L=111,epsilon='1e-20',
                scope='identity (131) with nonnegative remainder in both primitive parity sectors at T=4/5 only',
                prerequisite='modal comparison and kernel/projection transfer in BUILD083; prior congruences replayed',
                records=records)
    (FOLDER/'regularized_identity_T4_5.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__': main()
