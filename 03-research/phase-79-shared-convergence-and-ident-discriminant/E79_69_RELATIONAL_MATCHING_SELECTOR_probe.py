#!/usr/bin/env python3

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
E68 = ROOT / "E79_68_sigma_aware_terminal_score_autopsy_results.json"
OUT = ROOT / "E79_69_relational_matching_selector_results.json"


def mismatch(packet1, packet2, extra1, extra2):
    m1 = abs(packet1 - extra1) / max(packet1, extra1)
    m2 = abs(packet2 - extra2) / max(packet2, extra2)
    return max(m1, m2)


def best_suffix(v1, v2, extra1, extra2):
    m = len(v1)
    best = None
    for s in range(m):
        p1 = sum(v1[s:])
        p2 = sum(v2[s:])
        cand = (mismatch(p1, p2, extra1, extra2), list(range(s, m)), p1, p2)
        if best is None or cand < best:
            best = cand
    return best


def best_pair(v1, v2, extra1, extra2, max_gap=3):
    m = len(v1)
    best = None
    for i in range(m):
        p1 = v1[i]
        p2 = v2[i]
        cand = (mismatch(p1, p2, extra1, extra2), [i], p1, p2)
        if best is None or cand < best:
            best = cand
        for j in range(i + 1, m):
            if j - i - 1 > max_gap:
                continue
            p1 = v1[i] + v1[j]
            p2 = v2[i] + v2[j]
            cand = (mismatch(p1, p2, extra1, extra2), [i, j], p1, p2)
            if cand < best:
                best = cand
    return best


def best_triple(v1, v2, extra1, extra2, max_span=4):
    m = len(v1)
    best = None
    for i in range(m):
        for j in range(i + 1, m):
            for k in range(j + 1, m):
                if k - i > max_span:
                    continue
                p1 = v1[i] + v1[j] + v1[k]
                p2 = v2[i] + v2[j] + v2[k]
                cand = (mismatch(p1, p2, extra1, extra2), [i, j, k], p1, p2)
                if best is None or cand < best:
                    best = cand
    return best


def main():
    e68 = json.loads(E68.read_text())
    active = {int(k): v for k, v in e68["active_rows"].items()}
    targets = {int(k): v for k, v in e68["target_supports"].items()}

    # extra values from E79.67 / E79.3w audited ladder
    extras = {
        8: {"1.0": 0.000525776522483, "2.0": 0.00105114185516},
        10: {"1.0": 0.000307409734913, "2.0": 0.000614678199283},
        12: {"1.0": 0.000198719668364, "2.0": 0.000397382480892},
        14: {"1.0": 0.000133017693008, "2.0": 0.000266010252359},
        16: {"1.0": 9.49775787544e-05, "2.0": 0.000189942293},
    }

    rows = []
    exact_family_hits = {"suffix": 0, "pair": 0, "triple": 0, "best_of_three": 0}
    for n in sorted(targets):
        v1 = active[n]["1.0"]
        v2 = active[n]["2.0"]
        e1 = extras[n]["1.0"]
        e2 = extras[n]["2.0"]
        suffix = best_suffix(v1, v2, e1, e2)
        pair = best_pair(v1, v2, e1, e2)
        triple = best_triple(v1, v2, e1, e2)
        families = {
            "suffix": suffix,
            "pair": pair,
            "triple": triple,
        }
        best_family_name, best_family = min(families.items(), key=lambda kv: kv[1][0])
        row = {
            "N": n,
            "target_support": targets[n],
            "suffix": {
                "mismatch": suffix[0],
                "support": suffix[1],
                "packet_sigma1": suffix[2],
                "packet_sigma2": suffix[3],
                "exact_match": suffix[1] == targets[n],
            },
            "pair": {
                "mismatch": pair[0],
                "support": pair[1],
                "packet_sigma1": pair[2],
                "packet_sigma2": pair[3],
                "exact_match": pair[1] == targets[n],
            },
            "triple": {
                "mismatch": triple[0],
                "support": triple[1],
                "packet_sigma1": triple[2],
                "packet_sigma2": triple[3],
                "exact_match": triple[1] == targets[n],
            },
            "best_family": {
                "name": best_family_name,
                "mismatch": best_family[0],
                "support": best_family[1],
                "exact_match": best_family[1] == targets[n],
            },
        }
        for name in exact_family_hits:
            if name == "best_of_three":
                exact_family_hits[name] += int(best_family[1] == targets[n])
            else:
                exact_family_hits[name] += int(families[name][1] == targets[n])
        rows.append(row)

    result = {
        "statement": "E79.69 relational matching selector against ZERO^extra",
        "source": str(E68),
        "rows": rows,
        "exact_family_hits": exact_family_hits,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
