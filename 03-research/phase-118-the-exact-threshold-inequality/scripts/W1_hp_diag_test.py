import mpmath as mp
import W1_hp_threshold as HT
import W1_hp_lib as L

mp.mp.dps = 45
bk = HT.threshold_blocks_mp(2, 3, refine=8)
R0, L0, r, l = bk['R0'], bk['L0'], bk['r'], bk['l']
RE, LE = bk['RE'], bk['LE']
H = L.mat_solve(HT._sym(R0), r)
S_E = RE - r.transpose() * H
b_E = L0 * H - l

wA, VA = mp.eigsy(HT._sym(bk['A0']))
bproj = VA.transpose() * b_E
eps = mp.mpf('1e-14')
pen = mp.matrix(bk['dimA'], bk['dimA'])
for i in range(bk['dimC']):
    col = mp.matrix([bproj[i, j] for j in range(bk['dimA'])])
    pen += (1 / (wA[i] + eps)) * (col * col.transpose())

wS, VS = mp.eigsy(HT._sym(S_E))
Sh = mp.matrix(bk['dimA'], bk['dimA'])
for i in range(bk['dimA']):
    vi = mp.matrix([VS[k, i] for k in range(bk['dimA'])])
    Sh += (1 / mp.sqrt(wS[i])) * (vi * vi.transpose())
pen_norm_route1 = Sh * pen * Sh

diag = HT.diagnostic_Hc_correction(bk, [eps])
pen_norm_diag = diag[eps]

diff = pen_norm_route1 - pen_norm_diag
maxdiff = max(abs(diff[i, j]) for i in range(diff.rows) for j in range(diff.cols))
maxval = max(abs(pen_norm_route1[i, j]) for i in range(diff.rows) for j in range(diff.cols))
print("max|diff| =", mp.nstr(maxdiff, 6), "  max|val| =", mp.nstr(maxval, 6))
print("route1 pen_norm[0,0]=", mp.nstr(pen_norm_route1[0, 0], 20))
print("diag   pen_norm[0,0]=", mp.nstr(pen_norm_diag[0, 0], 20))
