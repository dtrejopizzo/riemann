# TEST_KINKS_001 step 4 (diagnostic): exponential resummation of the jet series, K_m^exp(ω) = 2 Re[J0 e^{iku0}/(m a + ik)],
# a = h'(λ)/h(λ) (= Fourier transform of μ(m)h(λ)e^{ma(u−u0)}1_{u<u0}); compared with Δr_out as in the analysis script.
import json,os,numpy as np
from pathlib import Path
SP=os.environ['SP']; HERE=Path(__file__).parent; D=json.load(open(f'{SP}/ed1/exterior_decomp_v2_OMX48_NP900.json'))
JT=json.load(open(HERE/'TEST_KINKS_001_data'/'jets.json'))
mu=15; lam=np.sqrt(mu); SC=1e35
om=np.array(D['omega']); R=np.array([[float(x) for x in r] for r in D['rho']])*SC; C={k:R[:,i] for i,k in enumerate(D['cols'])}
dr_out=C['p']-C['pro04']-C['pro8+']-C['inner_res']; mob=[0,1,-1,-1,0,-1,1,-1,0,0,1,-1,0,-1,1,1]
h0=float(JT['p']['h(λ)'])*SC; a=float(JT['p']["h'(λ)"])/float(JT['p']['h(λ)']); k=2*np.pi*lam*om
mdl=sum(2*np.real(mob[m]*h0*np.exp(1j*k*lam/m)/(m*a+1j*k)) for m in range(2,15) if mob[m])
out={}
for A,B in [(1,2),(2,4),(4,8),(8,48)]:
    s=(om>A)&(om<B); t=dr_out[s]; y=mdl[s]
    out[f'({A},{B})']={'relL2':float(np.sqrt(np.sum((t-y)**2)/np.sum(t**2))),'corr':float(t@y/np.sqrt(t@t*(y@y))),'rms model':float(np.sqrt(np.mean(y**2))),'rms Δr_out':float(np.sqrt(np.mean(t**2)))}
print(json.dumps(out,indent=1)); json.dump(out,open(HERE/'TEST_KINKS_001_data'/'resum.json','w'),indent=1)
