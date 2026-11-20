"""Full rigorous W sign at ONE fixed atom; all quantities normalized by norm^2."""
from fractions import Fraction as F
from power_contact_decision_032_contacts import prime,polar,tail,C
from power_arch_exact_032_verify import ARCH
partial=ARCH+polar+prime
assert partial.lo>F(34,10**16)
assert partial.hi+tail<F(45,10**16)
# Positivity of every omitted contact is the analytical theorem019:
# chi211 < (1+sqrt(8*211-11))/2 < 21 < (63/2)log2.
assert 21*21-21-(2*211-3)>0
assert C.log2.lo>F(2,3)
if __name__=='__main__':
 print('PASS: ONE atom N211,k1,u63/2 has 3.4e-15 < W/norm^2 < 4.5e-15.')
 print('ARCH exact EM8/CUT32; every prime-power<=512 enclosed; ENTIRE remaining tail positive and bounded.')
