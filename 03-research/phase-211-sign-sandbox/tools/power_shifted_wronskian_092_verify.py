"""One fixed polynomial in the previously certified origin jets, round092.

No new theta truncation, precision choice, or interval search. The unchanged
round087 verifier supplies every outward rational interval used below.
"""
from pathlib import Path
import runpy
from fractions import Fraction as F

BASE = Path(__file__).resolve().parent
data = runpy.run_path(str(BASE / 'power_theta_density_origin_087_verify.py'))
a, scale = data['a'], data['S']
D0 = -161280 * (6*a[1]*a[3]*a[4] - 8*a[2]**2*a[4]
                + 3*a[2]*a[3]**2)
assert D0.l > -56488961026*scale
assert D0.h < -56488961025*scale
print('PASS092: -56488961026 < D0 < -56488961025')
print('D0 lower exact:', F(D0.l, scale))
print('D0 upper exact:', F(D0.h, scale))
