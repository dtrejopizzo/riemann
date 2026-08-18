#!/usr/bin/env python3

import json
from pathlib import Path
from math import sqrt


ROOT = Path(__file__).resolve().parent
RAY = ROOT / "E79_56_ray_amplitude_autopsy_results.json"
PACKET = ROOT / "E79_44_multisigma_coupled_packet_results.json"
SPARSE = ROOT / "E79_3W_terminal_sparse_packet_results.json"
OUT = ROOT / "E79_57_ray_packet_decoupling_results.json"


def corr(xs, ys):
    mx = sum(xs) / len(xs)
    my = sum(ys) / len(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    denx = sum((x - mx) ** 2 for x in xs)
    deny = sum((y - my) ** 2 for y in ys)
    return num / sqrt(denx * deny)


def main():
    ray = json.loads(RAY.read_text())
    packet = json.loads(PACKET.read_text())
    sparse = json.loads(SPARSE.read_text())

    zeta_ray = {row["N"]: row for row in next(c for c in ray["cases"] if c["label"] == "zeta")["rows"]}
    zeta_packet = next(c for c in packet["cases"] if c["label"] == "zeta")["rows"]
    zeta_sparse = {row["N"]: row for row in next(c for c in sparse["cases"] if c["label"] == "zeta")["rows"]}

    rows = []
    for row in zeta_packet:
        n = row["N"]
        ray_row = zeta_ray[n]
        packet_rule = row["rules"]["mean-L0.0-M0.0"]
        sparse_rule = zeta_sparse[n]["sigmas"]["1.0"]["packets"]["W4-K3"]
        rows.append(
            {
                "N": n,
                "abs_rho": ray_row["abs_rho"],
                "N_abs_rho": ray_row["N_abs_rho"],
                "packet_mean_mismatch": float(packet_rule["mean_mismatch"]),
                "packet_size": packet_rule["size"],
                "packet_mismatch_sigma_1.0": float(packet_rule["mismatches"]["1.0"]),
                "sparse_minus_abs": abs(float(sparse_rule["minus"])),
                "sparse_mismatch": float(sparse_rule["mismatch"]),
                "sparse_N2_abs_minus": float(sparse_rule["N2_abs_minus"]),
            }
        )

    abs_rho = [r["abs_rho"] for r in rows]
    result = {
        "statement": "E79.57 ray-amplitude vs packet diagnostic audit",
        "sources": [str(RAY), str(PACKET), str(SPARSE)],
        "rows": rows,
        "correlations_against_abs_rho": {
            "packet_mean_mismatch": corr(abs_rho, [r["packet_mean_mismatch"] for r in rows]),
            "packet_mismatch_sigma_1.0": corr(abs_rho, [r["packet_mismatch_sigma_1.0"] for r in rows]),
            "sparse_minus_abs": corr(abs_rho, [r["sparse_minus_abs"] for r in rows]),
            "sparse_mismatch": corr(abs_rho, [r["sparse_mismatch"] for r in rows]),
            "sparse_N2_abs_minus": corr(abs_rho, [r["sparse_N2_abs_minus"] for r in rows]),
        },
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
