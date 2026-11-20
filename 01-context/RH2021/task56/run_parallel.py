
import sys, os, time, pickle, json
sys.path.insert(0, "/workspace/ead8dad7-2c8b-48d6-bfcb-911508844481")
import multiprocessing as mp_mod
import ldh_worker t_lo_global = 0.0
t_hi_global = 4600.0
block_size = 100.0
step = 0.5
dps_scan = 30
dps_final = 50 blocks = []
t = t_lo_global
while t < t_hi_global: t_end = min(t + block_size, t_hi_global) blocks.append((t, t_end, step, dps_scan, dps_final)) t = t_end
blocks_reversed = list(reversed(blocks)) n_workers = 8
results = {}
t0 = time.time() partial_file = "/workspace/ead8dad7-2c8b-48d6-bfcb-911508844481/ldh_partial.pkl"
log_file = "/workspace/ead8dad7-2c8b-48d6-bfcb-911508844481/ldh_run.log" def log(msg): with open(log_file, "a") as f: f.write(f"[{time.time()-t0:7.1f}s] {msg}\n") f.flush() # Clear log
open(log_file, "w").close()
log(f"Starting {len(blocks)} blocks with {n_workers} workers") ctx = mp_mod.get_context("fork")
with ctx.Pool(processes=n_workers) as pool: futures = [] for i, b in enumerate(blocks_reversed): futures.append((i, pool.apply_async(ldh_worker.find_zeros_in_block_v2, (b,)))) completed = 0 for i, fut in futures: try: res = fut.get() results[i] = res completed += 1 block = blocks_reversed[i] total_so_far = sum(len(v) for v in results.values()) log(f"block {i+1}/{len(blocks)} done [{block[0]:.0f},{block[1]:.0f}]: " f"{len(res)} zeros, completed={completed}, total_zeros={total_so_far}") # Save partial periodically if completed % 5 == 0 or completed == len(blocks): with open(partial_file, "wb") as f: pickle.dump({"results": results, "blocks_reversed": blocks_reversed}, f) log(f"saved partial after {completed} blocks") except Exception as e: log(f"block {i} FAILED: {e}") results[i] = [] with open(partial_file, "wb") as f: pickle.dump({"results": results, "blocks_reversed": blocks_reversed}, f) log(f"DONE. Total elapsed: {time.time()-t0:.1f}s, total zeros: {sum(len(v) for v in results.values())}")
