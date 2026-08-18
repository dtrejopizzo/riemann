#!/usr/bin/env python3
"""Directed projected-complement gap at T=log(2), degree 23.

This reuses the audited D.77 assembly through the D.79 exact shift mesh, but
uses the moderate B/4 tail anchor and lifts only the numerically isolated
lowest even/odd Ritz vector.  Floating eigendata are preconditioners only;
the final congruence and Gershgorin disks are Arb balls.
"""
from pathlib import Path
import os
import base64,struct
import numpy as np

_cap=Path(__file__).with_name('114_d_85_capacity_arb_prototype.py').read_text()
_v1=_cap.split("V_B85 = '''",1)[1].split("'''",1)[0]
_ana=Path(__file__).with_name('114_d_85_fixed_vector_analytic_verify.py').read_text()
_v2=_ana.split("V2_B85='''",1)[1].split("'''",1)[0]
_vo=_ana.split("ODD_B85='''",1)[1].split("'''",1)[0]
v1half=np.array(struct.unpack('<480d',base64.b85decode(_v1.encode())))
v2half=np.array(struct.unpack('<480d',base64.b85decode(_v2.encode())))
oddhalf=np.array(struct.unpack('<480d',base64.b85decode(_vo.encode())))

d79 = Path(__file__).with_name("114_d_79_stable_projected_tangency_verify.py")
driver = d79.read_text()
driver = driver.replace(
    's = source_path.read_text()',
    's = source_path.read_text()\n'
    's = s.replace("DEG = 9", "DEG = 23")'
)
driver = driver.replace('CTAIL=arb("80.625")', 'CTAIL=arb("80.125")')
chosen_degree = os.environ.get("D84_DEG")
if chosen_degree:
    driver = driver.replace('"DEG = 23"', f'"DEG = {int(chosen_degree)}"')
# D.77 recomputes these h-dependent polynomial tables inside every resolvent
# only because degree 9 made that cost negligible.  At degree 23 hoist them
# once per cell type; this is an algebraically identical mechanical rewrite.
hoist = r'''
    deriv_mats = {}
    for order in range(0, DEG+1):
        factor = (2/h)**order
        deriv_mats[order] = [[factor*poly_inner(LCOEFF[i], derivative(LCOEFF[j], order))
                              for j in range(D)] for i in range(D)]
    scale0 = (2/h).sqrt()
    basis_left = [scale0*poly_endpoint(p, -1) for p in LCOEFF]
    basis_right = [scale0*poly_endpoint(p, 1) for p in LCOEFF]
    basis_d_left = [scale0*(2/h)*poly_endpoint(derivative(p, 1), -1) for p in LCOEFF]
    basis_d_right = [scale0*(2/h)*poly_endpoint(derivative(p, 1), 1) for p in LCOEFF]
'''
driver = driver.replace(
    's = s.replace("DEG = 9", "DEG = 23")',
    's = s.replace("DEG = 9", "DEG = 23")\n'
    'old="""        # Physical derivative matrices in the orthonormal Legendre basis.\\n'
    '        deriv_mats = {}\\n'
    '        for order in range(0, DEG+1):\\n'
    '            factor = (2/h)**order\\n'
    '            deriv_mats[order] = [[factor*poly_inner(LCOEFF[i], derivative(LCOEFF[j], order))\\n'
    '                                  for j in range(D)] for i in range(D)]\\n"""\n'
    's=s.replace("    residual_rows = []\\n", "    residual_rows = []\\n"+' + repr(hoist) + ')\n'
    's=s.replace(old, "")\n'
    'old2="""        scale0 = (2/h).sqrt()\\n'
    '        basis_left = [scale0*poly_endpoint(p, -1) for p in LCOEFF]\\n'
    '        basis_right = [scale0*poly_endpoint(p, 1) for p in LCOEFF]\\n'
    '        basis_d_left = [scale0*(2/h)*poly_endpoint(derivative(p, 1), -1) for p in LCOEFF]\\n'
    '        basis_d_right = [scale0*(2/h)*poly_endpoint(derivative(p, 1), 1) for p in LCOEFF]\\n"""\n'
    's=s.replace(old2, "")'
)

custom = r'''
projected_lower = {}
odd_mode=__import__('os').environ.get('D84_ODD_GAP','0')=='1'
parities=(("odd",-1),) if odd_mode else (("even",1),("odd",-1))
for name, sign in parities:
    print(f"CERTIFY lifted projected {name} block dim={DIM_HALF}", flush=True)
    block = parity_block(sign)
    center = np.array([[float(x.mid()) for x in row] for row in block])
    evals, evecs = np.linalg.eigh(center)
    print(f"RITZ {name}: first={evals[0]:.17g}, next={evals[1]:.17g}", flush=True)
    if __import__("os").environ.get("D84_RITZ_ONLY", "0") == "1":
        np.save("/tmp/d84_"+name+"_degree"+str(DEG)+".npy", center)
        raise SystemExit(0)
    high_mode=__import__('os').environ.get('D84_HIGH_GAP','0')=='1' or odd_mode
    vecs=[oddhalf] if odd_mode else ([v1half,v2half] if high_mode else [evecs[:,0]])
    lift = arb("1.0") if high_mode else arb("0.01")
    target = arb("0.05") if odd_mode else (arb("0.50") if high_mode else arb("0.00130"))
    for i in range(DIM_HALF):
        for j in range(i, DIM_HALF):
            z = lift*sum((arb(repr(float(vv[i])))*arb(repr(float(vv[j]))) for vv in vecs),arb(0))
            block[i][j] += z
            if i != j: block[j][i] += z
        block[i][i] -= target
    approx = np.array([[float(x.mid()) for x in row] for row in block])
    chol = np.linalg.cholesky(approx)
    sinv = np.linalg.inv(chol)
    sinv[np.triu_indices(DIM_HALF, 1)] = 0.0
    sball = arb_mat([[arb(repr(float(sinv[i, j]))) for j in range(DIM_HALF)]
                     for i in range(DIM_HALF)])
    pre = sball*arb_mat(block)*sball.transpose()
    disks=[]
    for i in range(DIM_HALF):
        rad=sum((abs(pre[i,j]) for j in range(DIM_HALF) if i != j),arb(0))
        disks.append(pre[i,i]-rad)
    least=min(disks,key=lambda z:z.lower())
    assert least > 0
    projected_lower[name]=target
    print(f"PASS lifted {name}: raw Ritz={evals[0]:.17g}, "
          f"next={evals[1]:.17g}, gap > {target}; disk={least}", flush=True)
    if high_mode:raise SystemExit(0)
'''

needle = 'stop = s.index("# Cross/high residuals for off-cell kernels.")'
injection = (
    'p0=s.index("projected_lower = {}")\n'
    'p1=s.index("# Cross/high residuals for off-cell kernels.")\n'
    f's=s[:p0]+{custom!r}+"\\n"+s[p1:]\n'
)
driver = driver.replace(needle, injection + needle)
exec(compile(driver, str(d79)+"::D84-driver", "exec"))
