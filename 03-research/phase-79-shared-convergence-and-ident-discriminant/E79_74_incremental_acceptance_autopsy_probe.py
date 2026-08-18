#!/usr/bin/env python3

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
E68 = ROOT / "E79_68_sigma_aware_terminal_score_autopsy_results.json"
E69 = ROOT / "E79_69_relational_matching_selector_results.json"
OUT = ROOT / "E79_74_incremental_acceptance_autopsy_results.json"


def infer_extra(row, sigma_key):
    best = None
    for picks in itertools.product([0, 1], repeat=3):
        xs = []
        for fam, pick in zip(["suffix", "pair", "triple"], picks):
            cand = row[fam]
            packet = cand[sigma_key]
            mismatch = cand["mismatch"]
            xs.append(packet * (1 - mismatch) if pick == 0 else packet / (1 - mismatch))
        spread = max(xs) - min(xs)
        if best is None or spread < best[0]:
            best = (spread, xs)
    return sum(best[1]) / 3.0


def subset_score(subset, arr1, arr2, extra1, extra2):
    packet1 = sum(arr1[i] for i in subset) if subset else 0.0
    packet2 = sum(arr2[i] for i in subset) if subset else 0.0

    def rel(packet, extra):
        if packet == 0.0 or extra == 0.0:
            return 1.0 if packet != extra else 0.0
        return abs(packet - extra) / max(packet, extra)

    mismatch = max(rel(packet1, extra1), rel(packet2, extra2))

    if subset:
        inds = sorted(subset)
        card = len(inds)
        start = inds[0]
        span = inds[-1] - inds[0] + 1
        gaps = span - card
    else:
        card = start = gaps = 0

    score = mismatch - 0.22 * card + 0.14 * gaps + 0.36 * start
    return {
        "score": score,
        "mismatch": mismatch,
        "cardinality": card,
        "gaps": gaps,
        "start": start,
    }


def free_greedy(arr1, arr2, extra1, extra2):
    current = []
    trace = []
    while True:
        current_score = subset_score(current, arr1, arr2, extra1, extra2)["score"]
        best = None
        for j in range(len(arr1)):
            if j in current:
                continue
            cand = sorted(current + [j])
            rec = subset_score(cand, arr1, arr2, extra1, extra2)
            gain = current_score - rec["score"]
            if best is None or gain > best["gain"]:
                best = {"gain": gain, "add": j, "support": cand, "after": rec}
        if best is None or best["gain"] <= 0:
            break
        trace.append(best)
        current = best["support"]
    return current, trace


def terminal_anchor_greedy(arr1, arr2, extra1, extra2):
    current = [len(arr1) - 1]
    trace = []
    while True:
        current_score = subset_score(current, arr1, arr2, extra1, extra2)["score"]
        best = None
        for j in range(max(current)):
            if j in current:
                continue
            cand = sorted(current + [j])
            rec = subset_score(cand, arr1, arr2, extra1, extra2)
            gain = current_score - rec["score"]
            if best is None or gain > best["gain"]:
                best = {"gain": gain, "add": j, "support": cand, "after": rec}
        if best is None or best["gain"] <= 0:
            break
        trace.append(best)
        current = best["support"]
    return current, trace


def main():
    d68 = json.loads(E68.read_text())
    d69 = json.loads(E69.read_text())
    rows69 = {str(row["N"]): row for row in d69["rows"]}

    rows_out = []
    free_exact = 0
    anchored_exact = 0

    for n_str, row in d68["active_rows"].items():
        arr1 = row["1.0"]
        arr2 = row["2.0"]
        rel_row = rows69[n_str]
        extra1 = infer_extra(rel_row, "packet_sigma1")
        extra2 = infer_extra(rel_row, "packet_sigma2")
        target = d68["target_supports"][n_str]

        free_support, free_trace = free_greedy(arr1, arr2, extra1, extra2)
        anchored_support, anchored_trace = terminal_anchor_greedy(arr1, arr2, extra1, extra2)

        free_exact += int(free_support == target)
        anchored_exact += int(anchored_support == target)

        rows_out.append(
            {
                "N": int(n_str),
                "target_support": target,
                "extra_sigma1": extra1,
                "extra_sigma2": extra2,
                "free_greedy": {
                    "support": free_support,
                    "exact": free_support == target,
                    "final": subset_score(free_support, arr1, arr2, extra1, extra2),
                    "trace": free_trace,
                },
                "terminal_anchor_greedy": {
                    "support": anchored_support,
                    "exact": anchored_support == target,
                    "final": subset_score(anchored_support, arr1, arr2, extra1, extra2),
                    "trace": anchored_trace,
                },
            }
        )

    result = {
        "statement": "E79.74 incremental acceptance autopsy",
        "sources": [str(E68), str(E69)],
        "summary": {
            "num_rows": len(rows_out),
            "free_greedy_exact_count": free_exact,
            "terminal_anchor_exact_count": anchored_exact,
        },
        "rows": rows_out,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
