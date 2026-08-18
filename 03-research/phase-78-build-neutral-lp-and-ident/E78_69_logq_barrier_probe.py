#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
SRC = HERE / "E78_68_logq_scalar_results.json"


def barrier(theta: float) -> float:
    return -math.log(math.cos(theta))


def summarize(values: list[float]) -> dict[str, float | int | None]:
    if not values:
        return {"count": 0, "min": None, "median": None, "max": None}
    vals = sorted(values)
    mid = len(vals) // 2
    med = vals[mid] if len(vals) % 2 else 0.5 * (vals[mid - 1] + vals[mid])
    return {"count": len(vals), "min": vals[0], "median": med, "max": vals[-1]}


def build_rows(rows: list[dict[str, object]]) -> dict[str, object]:
    out = []
    margins = []
    barriers = []
    gains = []
    max_recon_error = 0.0
    for row in rows:
        a = float(row["re_delta_ell"])
        b = abs(float(row["wrapped_im_delta_ell"]))
        gain = float(row["scalar_gain"])
        if b >= math.pi / 2:
            raise ValueError("wrapped phase left the admissible cosine sector")
        bnd = barrier(b)
        margin = a - bnd
        reconstructed_gain = 1.0 - math.exp(-(margin + bnd)) * math.cos(b)
        recon_error = abs(gain - reconstructed_gain)
        max_recon_error = max(max_recon_error, recon_error)
        margins.append(margin)
        barriers.append(bnd)
        gains.append(gain)
        out.append(
            {
                "sigma": row["sigma"],
                "N": row["N"],
                "to_N": row["to_N"],
                "re_delta_ell": a,
                "wrapped_im_delta_ell_abs": b,
                "angular_barrier": bnd,
                "barrier_margin": margin,
                "scalar_gain": gain,
                "reconstruction_error": recon_error,
            }
        )
    return {
        "rows": out,
        "summary": {
            "angular_barrier": summarize(barriers),
            "barrier_margin": summarize(margins),
            "scalar_gain": summarize(gains),
        },
        "max_reconstruction_error": max_recon_error,
    }


def main() -> None:
    src = json.loads(SRC.read_text())
    result = {
        "statement": (
            "Barrier form of the old-old logq gain: "
            "1-exp(-a)cos(b)>0 iff a > -log cos(|wrap(b)|) when |wrap(b)|<pi/2."
        ),
        "sources": {"logq_scalar": str(SRC)},
        "builds": {
            "zeta": build_rows(src["builds"]["zeta"]["rows"]),
            "plant": build_rows(src["builds"]["plant"]["rows"]),
        },
    }
    out_path = HERE / "E78_69_logq_barrier_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
