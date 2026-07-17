
import sys, os, time, pickle
sys.path.insert(0, '/workspace/321f0eeb-097c-4d58-9349-fa9ad588875f')
os.chdir('/workspace/321f0eeb-097c-4d58-9349-fa9ad588875f')
from lchi5_module import scan_interval
from multiprocessing import Pool T_START = 2499.4 # start slightly before last bracket end to avoid missing
T_END = 4500.0
H = 0.1
CHUNK = 25.0 # width of each task
DPS = 15 tasks = []
t = T_START
while t < T_END: tasks.append((t, min(t+CHUNK, T_END), H, DPS)) t += CHUNK print(f"Created {len(tasks)} tasks; total interval {T_START}-{T_END}", flush=True) t0 = time.time()
all_brackets = []
with Pool(8) as p: for i, res in enumerate(p.imap_unordered(scan_interval, tasks)): all_brackets.extend(res) elapsed = time.time()-t0 print(f"[{elapsed:7.1f}s] done {i+1}/{len(tasks)} (+{len(res)} brackets, total {len(all_brackets)})", flush=True) # Save partial result with open('brackets_2500_4500_partial.pkl', 'wb') as f: pickle.dump(all_brackets, f) # Sort and dedupe by midpoint
all_brackets.sort(key=lambda ab: ab[0])
with open('brackets_2500_4500.pkl', 'wb') as f: pickle.dump(all_brackets, f)
print("Done in", time.time()-t0, "s; total new brackets:", len(all_brackets))
