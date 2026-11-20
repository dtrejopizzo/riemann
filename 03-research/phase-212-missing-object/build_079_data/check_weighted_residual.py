"""Apply certified residual weights to un-certified floating matrices.

Positive outputs remain NUMERICAL_ONLY because R*R and blocks lack enclosures.
"""
import json
from pathlib import Path
import numpy as np

p=Path(__file__).parent
records=[]
for bo,ro,rho in [(160,256,1783/500),(192,128,1573/1000)]:
    for parity in ('even','odd'):
        with np.load(p/f'blocks_{parity}_{bo}.npz') as data:
            P,K,D,X=[data[k] for k in ('P','K','D','Z')]
            degree=int(data['degree'])
        S=P-D.T@X-X.T@D+X.T@K@X
        defect=D-K@X
        source=p/f'residual_{parity}_{bo}_{ro}.npz'
        if not source.exists() and bo==160:
            source=p/f'residual_{parity}_256.npz'  # Original baseline run.
        with np.load(source) as data:
            gram=data['gram']
        diagnostic=S-rho*gram-8*(defect.T@defect)
        eig=np.linalg.eigvalsh((diagnostic+diagnostic.T)/2)
        records.append(dict(parity=parity,degree=degree,block_order=bo,outer_order=ro,
                            rho=rho,minimum=float(eig[0]),negative_count=int(np.sum(eig<0)),
                            first_eigenvalues=eig[:4].tolist()))
report=dict(status='NUMERICAL_ONLY',full_sign_certificate=False,records=records)
(p/'weighted_residual_diagnostic.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
