#!/usr/bin/env python3
"""Exact Decimal budget audit for the D.85 two-level endpoint certificate."""
from decimal import Decimal as D, getcontext
getcontext().prec=80

# Directed inputs are produced by the Arb verifiers; adverse endpoints only.
delta_p=D('.5'); alpha=D('1.53'); beta2=D('.0362')
g_big=(delta_p+alpha-((alpha-delta_p)**2+4*beta2).sqrt())/2
assert g_big>D('.46')

mu2=D('.0020336972824697'); eps2_2=D('8.623e-20')
low2=(mu2+g_big-((g_big-mu2)**2+4*eps2_2).sqrt())/2
g=D('.0015')
assert low2>g

eta=D('.0003');h=g-eta
ell=D('.000001746475');eps2_1=D('4.441e-24')
ell_eff=ell+eps2_1/eta
delta=D('1.27084620358308')
threshold=ell_eff/(h*(h+ell_eff))
capacity=h*h*delta/(1-h*delta)
assert delta>threshold and capacity>ell_eff

# Odd channel: one positive low mode over a .05 projected complement.
beta2_sharp=D('.000366')
g_odd=(D('.05')+alpha-((alpha-D('.05'))**2+4*beta2_sharp).sqrt())/2
mu_odd=D('0.00000813856175479');eps2_odd=D('9.741e-22')
odd_lower=(mu_odd+g_odd-((g_odd-mu_odd)**2+4*eps2_odd).sqrt())/2
assert g_odd>D('.0497') and odd_lower>0
print('PASS two-level endpoint budget')
print('big-block gap lower:',g_big)
print('v2/complement gap lower:',low2)
print('capacity threshold / lower capacity:',threshold,capacity)
print('final capacity margin:',capacity-ell_eff)
print('odd complement / final lower:',g_odd,odd_lower)
