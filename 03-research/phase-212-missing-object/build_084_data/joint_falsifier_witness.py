"""One N=256 control: all star planes positive, a joint test for 1.1 Lambda.

The floating eigensolve only proposes dyadic coordinates. --verify checks
the saved coordinates directly with Arb and does not rerun an eigensolve.
"""
import argparse
import json
from pathlib import Path
from flint import arb, arb_mat, ctx


def matrices(n):
    logs = [arb(0)]+[arb(j).log() for j in range(1,2*n+3)]
    xlogx = lambda j: j*logs[j]
    h = [xlogx(j+2)-2*xlogx(j+1)+xlogx(j) for j in range(2*n+1)]
    constant = -arb.const_euler()-(2*arb.pi()).log()
    mangoldt = [arb(0) for _ in range(n+1)]
    composite = [False]*(n+1)
    for p in range(2,n+1):
        if composite[p]:
            continue
        for j in range(p*p,n+1,p):
            composite[j] = True
        power = p
        while power <= n:
            mangoldt[power] = logs[p]
            power *= p
    prefix = [arb(0)]
    for j in range(1,n+1):
        prefix.append(prefix[-1]+mangoldt[j]/j)
    arch = [[arb(0) for _ in range(n)] for _ in range(n)]
    comb = [[arb(0) for _ in range(n)] for _ in range(n)]
    for i in range(1,n+1):
        arch[i-1][i-1] = constant+xlogx(i+1)-xlogx(i)-h[2*i]/2
        for j in range(i+1,n+1):
            arch[i-1][j-1] = arch[j-1][i-1] = -(h[i+j]+h[j-i-1])/2
            comb[i-1][j-1] = comb[j-1][i-1] = prefix[j//i]-prefix[j//(i+1)]
    return arb_mat(arch), arb_mat(comb), [logs[j+1]-logs[j] for j in range(1,n+1)]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--verify',action='store_true')
    parser.add_argument('--refresh-report',action='store_true')
    args = parser.parse_args()
    assert not args.refresh_report or args.verify
    ctx.dps = 100
    n, denominator_power = 256, 40
    target = Path(__file__).with_name('joint_scaled_witness_256.json')
    arch, comb, ell = matrices(n)
    scale = arb(11)/10
    scaled = arch-scale*comb
    if args.verify:
        saved = json.loads(target.read_text())
        assert saved['N']==n and saved['denominator_power']==denominator_power
        numerators = saved['circuit_numerators']
        assert len(numerators)==n-2 and all(isinstance(v,int) for v in numerators)
        diagnostic = saved.get('proposal_eigenvalue')
    else:
        import numpy as np
        from scipy.linalg import null_space, eigh
        matrix = np.array([[float(scaled[i,j]) for j in range(n)] for i in range(n)])
        constraints = np.array([[1.0]*n,[float(v) for v in ell]])
        basis = null_space(constraints)
        values, vectors = eigh(basis.T@matrix@basis,subset_by_index=[0,0])
        diagnostic = float(values[0])
        if diagnostic >= 0:
            print(json.dumps({'status':'INCONCLUSIVE_NUMERICAL_BLOCK','N':n,'minimum':diagnostic}))
            return
        proposal = basis@vectors[:,0]
        numerators = [int(round(float(v)/float(ell[0]-ell[1])*2**denominator_power))
                      for v in proposal[2:]]

    # Exactly primitive by the circuit identity, not by a numerical tolerance.
    d = ell[0]-ell[1]
    coeff = [arb(0) for _ in range(n)]
    for k, integer in enumerate(numerators,start=3):
        gamma = arb(integer)/2**denominator_power
        coeff[0] += gamma*(ell[1]-ell[k-1])
        coeff[1] += gamma*(ell[k-1]-ell[0])
        coeff[k-1] = gamma*d
    column = arb_mat([[v] for v in coeff])
    norm2 = (column.transpose()*column)[0,0]
    energy = (column.transpose()*scaled*column)[0,0]
    physical_energy = (column.transpose()*(arch-comb)*column)[0,0]
    assert norm2 > 0
    assert energy < 0, str(energy)
    assert physical_energy > 0, str(physical_energy)
    first = [arb(0) for _ in range(n)]
    first[0], first[1], first[2] = ell[1]-ell[2],ell[2]-ell[0],d
    first_column = arb_mat([[v] for v in first])
    interactions = {}
    for label, matrix, total in [('scaled',scaled,energy),
                                  ('physical',arch-comb,physical_energy)]:
        pivot = (first_column.transpose()*matrix*first_column)[0,0]
        assert pivot > 0
        coupling = (first_column.transpose()*matrix*column)[0,0]
        square = coupling**2/pivot
        diagonal_sum = arb(0)
        for k, integer in enumerate(numerators,start=3):
            left,right = ell[1]-ell[k-1],ell[k-1]-ell[0]
            gkk = (left**2*matrix[0,0]+right**2*matrix[1,1]+d*d*matrix[k-1,k-1]
                    +2*left*right*matrix[0,1]+2*d*(left*matrix[0,k-1]+right*matrix[1,k-1]))
            assert gkk > 0
            diagonal_sum += (arb(integer)/2**denominator_power)**2*gkk
        interactions[label] = {
            'first_pivot':pivot.str(60),
            'first_square':square.str(60),
            'schur_remainder':(total-square).str(60),
            'circuit_diagonal_sum':diagonal_sum.str(60),
            'circuit_cross_sum':(total-diagonal_sum).str(60),
        }
    report = {
        'status':'PASS_NEGATIVE_JOINT_CONTROL',
        'N':n,
        'mangoldt_scale':'11/10',
        'denominator_power':denominator_power,
        'circuit_numerators':numerators,
        'proposal_eigenvalue':diagnostic,
        'energy_scaled':energy.str(60),
        'energy_physical_same_test':physical_energy.str(60),
        'norm_squared':norm2.str(60),
        'Rayleigh_scaled':(energy/norm2).str(60),
        'Rayleigh_physical_same_test':(physical_energy/norm2).str(60),
        'interactions':interactions,
        'moments':'exactly zero by the F_k parametrization; not inferred from interval overlap',
        'window':'T=log(257)/2 after a common centering translation',
        'limitation':'negative only for scaled weights; no negative claim for Lambda',
    }
    if not args.verify or args.refresh_report:
        target.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({key:value for key,value in report.items() if key!='circuit_numerators'},indent=2))


if __name__=='__main__':
    main()
