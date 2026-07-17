import time
from engine_cache import get_matrices
for lam,N in [(15.0,20),(17.0,20),(19.0,22),(21.0,22)]:
    t=time.time(); get_matrices(lam,N,'zeta',dps=40)
    print(f"built lam={lam} N={N} in {time.time()-t:.0f}s", flush=True)
