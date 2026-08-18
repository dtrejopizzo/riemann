#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PHASE77 = HERE.parent / "phase-77-weyl-limit-point"


def load_json(name: str):
    return json.loads((PHASE77 / name).read_text())


def build_case_rows(build: str):
    q_identity = load_json("E77_5y_q_functional_identity_results.json")
    schur = load_json(f"E77_5aa_schur_logt_functional_{build}.json")

    qmap = {(row["sigma"], row["N"]): row for row in q_identity["cases"][0]["rows"]}
    out = []
    for row in schur["cases"][0]["qrows"]:
        sigma = row["sigma"]
        N = row["N"]
        qrow = qmap[(sigma, N)]
        q_ext = qrow["Q_external_component"]
        q_logt = row["Q_logT_reconstructed"]
        q_t0 = row["Q_t0"]
        q_theta = row["Q_theta"]
        q_ref = row["Q_reference"]

        relcoup = abs(q_ref) / (abs(q_ext) + abs(q_t0) + abs(q_theta))
        logt_cancel = abs(q_ref) / (abs(q_ext) + abs(q_logt))
        schur_compression = (abs(q_ext) + abs(q_logt)) / (
            abs(q_ext) + abs(q_t0) + abs(q_theta)
        )
        triangle_slack = (abs(q_t0) + abs(q_theta) - abs(q_logt)) / (
            abs(q_ext) + abs(q_t0) + abs(q_theta)
        )
        reconstruction = logt_cancel * schur_compression

        out.append(
            {
                "sigma": sigma,
                "N": N,
                "mod4": row["mod4"],
                "Q_reference": q_ref,
                "Q_ext": q_ext,
                "Q_logT": q_logt,
                "Q_t0": q_t0,
                "Q_theta": q_theta,
                "RELCOUP": relcoup,
                "LOGT_CANCEL": logt_cancel,
                "SCHUR_COMPRESSION": schur_compression,
                "TRIANGLE_SLACK": triangle_slack,
                "reconstruction": reconstruction,
                "reconstruction_error": abs(relcoup - reconstruction),
            }
        )
    return out


def summarize(rows):
    sigmas = sorted({row["sigma"] for row in rows}, key=float)
    by_sigma = {}
    for sigma in sigmas:
        bucket = [row for row in rows if row["sigma"] == sigma]
        by_sigma[sigma] = {
            "min_relcoup": min(row["RELCOUP"] for row in bucket),
            "max_relcoup": max(row["RELCOUP"] for row in bucket),
            "min_logt_cancel": min(row["LOGT_CANCEL"] for row in bucket),
            "max_logt_cancel": max(row["LOGT_CANCEL"] for row in bucket),
            "min_schur_compression": min(row["SCHUR_COMPRESSION"] for row in bucket),
            "max_schur_compression": max(row["SCHUR_COMPRESSION"] for row in bucket),
            "min_triangle_slack": min(row["TRIANGLE_SLACK"] for row in bucket),
            "max_triangle_slack": max(row["TRIANGLE_SLACK"] for row in bucket),
        }
    return by_sigma


def main():
    result = {
        "statement": (
            "Exact factorization RELCOUP = LOGT_CANCEL * SCHUR_COMPRESSION, "
            "with TRIANGLE_SLACK = 1 - SCHUR_COMPRESSION"
        ),
        "sources": {
            "q_identity": str(PHASE77 / "E77_5y_q_functional_identity_results.json"),
            "schur_zeta": str(PHASE77 / "E77_5aa_schur_logt_functional_zeta.json"),
            "schur_plant": str(PHASE77 / "E77_5aa_schur_logt_functional_plant.json"),
        },
        "builds": {},
    }
    for build in ("zeta", "plant"):
        rows = build_case_rows(build)
        result["builds"][build] = {
            "rows": rows,
            "summary_by_sigma": summarize(rows),
            "max_reconstruction_error": max(row["reconstruction_error"] for row in rows),
        }

    out_path = HERE / "E78_18_relcoup_factor_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
