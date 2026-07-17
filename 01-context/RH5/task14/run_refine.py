
import sys, os, time, pickle
sys.path.insert(0, '/workspace/321f0eeb-097c-4d58-9349-fa9ad588875f')
os.chdir('/workspace/321f0eeb-097c-4d58-9349-fa9ad588875f')
import mpmath as mp
from lchi5_module import Z
from multiprocessing import Pool def fast_refine_secant(args): a, b, target_dps, maxiter = args mp.mp.dps = target_dps + 5 a = mp.mpf(a); b = mp.mpf(b) za = Z(a); zb = Z(b) eps = mp.mpf(10)**(-target_dps) c = (a+b)/2 for _ in range(maxiter): if zb == za: c = (a+b)/2 else: c = a - za*(b-a)/(zb-za) if not (a < c < b): c = (a+b)/2 if (b - a) < eps * max(abs(c), mp.mpf(1)): break zc = Z(c) if abs(zc) < eps * mp.mpf(10): return mp.nstr(c, target_dps+2, strip_zeros=False) if (zc > 0) == (za > 0): a, za = c, zc else: b, zb = c, zc return mp.nstr(c, target_dps+2, strip_zeros=False) def refine_chunk(args): brackets, target_dps, maxiter = args mp.mp.dps = target_dps + 5 out = [] for (a, b) in brackets: s = fast_refine_secant((a, b, target_dps, maxiter)) out.append(s) return out with open('brackets_first_5000.pkl','rb') as f: all_b = pickle.load(f)
print(f"Total brackets to refine: {len(all_b)}", flush=True) TARGET_DPS = int(os.environ.get('TARGET_DPS', '15'))
MAXITER = int(os.environ.get('MAXITER', '7'))
CHUNK_SIZE = int(os.environ.get('CHUNK_SIZE', '25')) # Build chunks
chunks = []
for ci in range(0, len(all_b), CHUNK_SIZE): bs = all_b[ci:ci+CHUNK_SIZE] chunks.append((bs, TARGET_DPS, MAXITER)) print(f"Chunks: {len(chunks)}, chunk_size={CHUNK_SIZE}, target_dps={TARGET_DPS}, maxiter={MAXITER}", flush=True) t0 = time.time()
results = []
with Pool(8) as p: for i, res in enumerate(p.imap(refine_chunk, chunks)): results.append(res) elapsed = time.time()-t0 flat = sum((len(r) for r in results), 0) print(f"[{elapsed:7.1f}s] chunk {i+1}/{len(chunks)} done; total refined: {flat}", flush=True) if i % 5 == 0 or i == len(chunks)-1: with open(f'zeros_partial_dps{TARGET_DPS}.pkl', 'wb') as f: pickle.dump([z for chunk in results for z in chunk], f) flat_results = [z for chunk in results for z in chunk]
print(f"Total refined: {len(flat_results)} in {time.time()-t0:.1f}s")
flat_results.sort(key=lambda s: mp.mpf(s))
with open(f'zeros_Lchi5_N{len(flat_results)}_dps{TARGET_DPS}.pkl', 'wb') as f: pickle.dump(flat_results, f)
print(f"Saved zeros_Lchi5_N{len(flat_results)}_dps{TARGET_DPS}.pkl")
