"""R154 round 2: R2 sweep -- how far does the two-multiplier certificate get at 1/2 log 3?"""
import math
from lp2 import run
T3 = 0.5*math.log(3); T2 = math.log(2)
for cap in (5., 50., 500., 5000.):
    for two in (False, True):
        run(T3, [2], 20., .05, cap, two, dtau=0.02, taumax=100., ref=10)
run(T3, [2], 40., .05, 5000., True, dtau=0.02, taumax=100., ref=10)
for cap in (50., 5000.):
    run(T2, [2, 3], 20., .05, cap, True, dtau=0.02, taumax=100., ref=10)
