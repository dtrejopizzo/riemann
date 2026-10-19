"""NUMERICO: contribution of the two known off-line quadruples of Z_Q (LEMMA_E argcount, t<30) to D at T=8/5;
bound for higher off-line zeros by sup|h|; limit symbol of D on modulated indicators (Thm 13.1(a))."""
import numpy as np
from witness import h
D = -3.479097
tot = 0
for s, t in [(0.932969697485414, 15.6682495312785), (0.937666906700399, 29.9833952351555)]:
    gm = complex(t, -(s - 0.5)); q = 2 * (h(gm)[0] + h(gm.conjugate())[0]).real; on = 4 * h(t)[0].real; tot += q
    print('rho=%.6f+%.6fi quadruple %.6f ; on-line equivalent %.6f ; excess %.2e' % (s, t, q, on, q - on))
print('known off-line total %.6f = %.3f %% of D' % (tot, 100 * tot / D))
tt = np.linspace(30, 3000, 30000); ht = np.concatenate([np.abs(h(x)) for x in np.array_split(tt, 30)])
print('sup_{t>30}|h(t)| = %.2e ; int_30^inf |h| dt ~ %.4f' % (ht.max(), np.trapz(ht, tt)))
for d in (0.3, 0.5, 0.7):
    tq = np.linspace(30, 300, 2701); hq = np.abs(np.concatenate([h(tq - 1j * d), h(tq + 1j * d)])); print('sup_{30<t<300}|h(t +- %.1fi)| = %.2e' % (d, hq.max()))
# Thm 13.1(a) check: limit symbol phi(lambda) for D=-20, from Lambda_def contacts (values from COSH_DEFECT / lemma13 (1))
import importlib.util, sys
