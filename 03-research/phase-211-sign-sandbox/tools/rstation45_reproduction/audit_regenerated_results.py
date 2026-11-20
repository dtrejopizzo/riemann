"""Audit regenerated outputs only; does not replace the analytic proof audit."""
from pathlib import Path
import hashlib
import argparse
import numpy as np
from flint import arb, ctx

root = Path(__file__).resolve().parent
ctx.prec = 256
parser = argparse.ArgumentParser()
parser.add_argument('--parity', choices=['even', 'odd', 'both'], default='both')
selection = parser.parse_args().parity
for tag, parity, core in [('even', '+', 7), ('odd', '-', 6)]:
    if selection != 'both' and selection != tag:
        continue
    path = root / 'scratch' / (
        f'log11_{tag}_K400_N500_clean_sharp_family_500_850_full{400-core}_q8000_arb_256.npz'
    )
    with np.load(path, allow_pickle=False) as data:
        for key, expected in [('N', 500), ('precision', 256), ('qf', 8000),
                              ('family_m', 350)]:
            assert int(data[key]) == expected, (path, key)
        assert arb(str(data['endpoint_value'])) == arb(11)
        assert bool(data['clean'])
        assert str(data['parity']) == parity
        assert str(data['cache_prefix']) == 'log11'
        assert str(data['base_source']) == f'log11_{tag}_K400_safe_base_arb_256.npz'
        assert str(data['family_source']) == f'scratch/log11_{tag}_K400_N500_yukawa_500_850_parseval_arb_256.npz'
        assert str(data['householder_source']) == f'log11_{tag}_R280_N500_verified_graph_arb_256.npz'
        for key in ['Hmin', 't400', 'tqf']:
            assert arb(str(data[key])).lower() > 0, (path, key)
        assert data['pivots'].shape == (core,)
        for value in data['pivots']:
            assert arb(str(value)).lower() > 0
        perm = [int(value) for value in data['perm']]
        assert sorted(perm) == list(range(core))
        raw = data['S']
        assert raw.shape == (core, core)
        matrix = [[arb(str(raw[i, j])) for j in perm] for i in perm]
        for k in range(core):
            pivot = matrix[k][k]
            assert pivot.lower() > 0, (path, k, pivot)
            for i in range(k + 1, core):
                for j in range(i, core):
                    value = matrix[i][j] - matrix[i][k]*matrix[j][k]/pivot
                    matrix[i][j] = matrix[j][i] = value
        print(tag, 'REGENERATED OUTPUT AUDIT PASS', 'last pivot', pivot)
    print(path.name, hashlib.sha256(path.read_bytes()).hexdigest())
print(selection, 'REGENERATED OUTPUT AUDIT COMPLETE; analytic and execution provenance audits remain required')
