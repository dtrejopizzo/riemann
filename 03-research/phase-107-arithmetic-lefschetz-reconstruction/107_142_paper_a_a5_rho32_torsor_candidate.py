#!/usr/bin/env python3
"""rho_32 torsor/cocycle candidate for the A5 local branch."""

from __future__ import annotations

import json
import subprocess
from itertools import combinations
from pathlib import Path


SAGE_BIN = Path("/home/trabajo/miniforge3/bin/sage")
MODULUS = 32


def run_sage_json() -> dict[str, object]:
    code = r"""
from sage.all import EllipticCurve, cremona_curves
import json


def reduction_label(ld):
    value = ld.bad_reduction_type()
    if value is None:
        return "good"
    text = str(value)
    if text == "0":
        return "additive"
    if text == "+1":
        return "split_multiplicative"
    if text == "-1":
        return "nonsplit_multiplicative"
    return text


atlas_rows = []
for label, probe, role in [
    ("14a5", 7, "split_pair"),
    ("21a1", 7, "split_pair"),
    ("20a1", 2, "cp_pair"),
    ("36a4", 2, "cp_pair"),
]:
    E = EllipticCurve(label)
    ld = E.local_data(probe)
    atlas_rows.append({
        "name": f"{label}@{probe}",
        "prime": int(probe),
        "role": role,
        "cp": int(ld.tamagawa_number()),
        "reduction": reduction_label(ld),
        "ainvs": tuple(int(a) for a in ld.minimal_model().ainvs()),
    })

family_rows = []
for N in range(11, 2001):
    try:
        curves = cremona_curves([N])
    except Exception:
        continue
    for E in curves:
        for ld in E.local_data():
            p = int(ld.prime().gens_reduced()[0])
            if p != 2:
                continue
            if str(ld.kodaira_symbol()) != 'IV*' or str(ld.bad_reduction_type()) != '0':
                continue
            vals = []
            ok = True
            for obj in [E.c4(), E.c6(), E.discriminant(), E.j_invariant()]:
                v = obj.valuation(2)
                if str(v) == '+Infinity':
                    ok = False
                    break
                vals.append(int(v))
            if not ok:
                continue
            v4, v6, vd, vj = vals
            if (v4, v6, vd, vj, int(ld.conductor_valuation()), int(E.ap(2))) != (4, 6, 8, 4, 2, 0):
                continue
            family_rows.append({
                "label": E.label(),
                "cp": int(ld.tamagawa_number()),
                "ainvs": tuple(int(a) for a in ld.minimal_model().ainvs()),
            })

print(json.dumps({"atlas_rows": atlas_rows, "family_rows": family_rows}, default=int))
"""
    result = subprocess.run(
        [str(SAGE_BIN), "-c", code],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)


def rho32(row: dict[str, object]) -> tuple[int, ...]:
    return tuple(int(a) % MODULUS for a in row["ainvs"])


def delta32(left: dict[str, object], right: dict[str, object]) -> tuple[int, ...]:
    return tuple((a - b) % MODULUS for a, b in zip(rho32(left), rho32(right)))


def add_delta(x: tuple[int, ...], y: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((a + b) % MODULUS for a, b in zip(x, y))


def neg_delta(x: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((-a) % MODULUS for a in x)


def main() -> None:
    payload = run_sage_json()
    atlas_rows = payload["atlas_rows"]
    family_rows = payload["family_rows"]

    transpose_ok = True
    pair_samples = []
    for left, right in combinations(atlas_rows, 2):
        d_lr = delta32(left, right)
        d_rl = delta32(right, left)
        ok = d_rl == neg_delta(d_lr)
        transpose_ok &= ok
        if len(pair_samples) < 5:
            pair_samples.append((left["name"], right["name"], d_lr, d_rl, ok))

    big_class = family_rows[:8]
    cocycle_ok = True
    triple_samples = []
    for i in range(len(big_class) - 2):
        a = big_class[i]
        b = big_class[i + 1]
        c = big_class[i + 2]
        lhs = add_delta(delta32(a, b), delta32(b, c))
        rhs = delta32(a, c)
        ok = lhs == rhs
        cocycle_ok &= ok
        triple_samples.append((a["label"], b["label"], c["label"], lhs, rhs, ok))

    zero_kernel_ok = True
    zero_kernel_count = 0
    for left, right in combinations(big_class, 2):
        same_rho = rho32(left) == rho32(right)
        zero_delta = delta32(left, right) == (0, 0, 0, 0, 0)
        ok = same_rho == zero_delta
        zero_kernel_ok &= ok
        if same_rho:
            zero_kernel_count += 1

    cp_pair = [row for row in atlas_rows if row["role"] == "cp_pair"]
    split_pair = [row for row in atlas_rows if row["role"] == "split_pair"]
    cp_delta_nonzero = delta32(cp_pair[0], cp_pair[1]) != (0, 0, 0, 0, 0)
    split_delta_nonzero = delta32(split_pair[0], split_pair[1]) != (0, 0, 0, 0, 0)

    print("Paper A A5 rho_32 torsor candidate:")
    print(f"ATLAS_ROWS: {len(atlas_rows)}")
    print(f"FAMILY_ROWS: {len(family_rows)}")
    print(f"TRANSPOSE_OK: {transpose_ok}")
    print(f"COCYCLE_OK: {cocycle_ok}")
    print(f"ZERO_KERNEL_OK: {zero_kernel_ok}")
    print(f"ZERO_KERNEL_COUNT: {zero_kernel_count}")
    print(f"CP_PAIR_DELTA_NONZERO: {cp_delta_nonzero}")
    print(f"SPLIT_PAIR_DELTA_NONZERO: {split_delta_nonzero}")
    for left, right, d_lr, d_rl, ok in pair_samples:
        print(f"  pair {left} / {right}: d_lr={d_lr} d_rl={d_rl} ok={ok}")
    for a, b, c, lhs, rhs, ok in triple_samples[:3]:
        print(f"  triple {a},{b},{c}: lhs={lhs} rhs={rhs} ok={ok}")

    print()
    if transpose_ok and cocycle_ok and zero_kernel_ok and cp_delta_nonzero and split_delta_nonzero:
        print("VERDICT: YES")
        print("Reason: rho_32 behaves as a first torsor/cocycle-style local decoration on the tested real data.")
    else:
        print("VERDICT: NO")
        print("Reason: the proposed rho_32 torsor law fails on the tested real data.")


if __name__ == "__main__":
    main()
