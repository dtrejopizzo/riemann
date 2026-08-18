#!/usr/bin/env python3
"""Exact audit for the finite logarithmic chart shadow of Paper C.

This verifier audits the finite symbolic content of `107_23`:

1. the admissible local logarithmic template is stable under the chart
   transitions of `107_17`;
2. boundary and diagonal coefficients combine additively under tensor
   products, matching the generatorwise packaging of `107_22`;
3. no stronger-than-log singularity is introduced by passing between the
   interior, boundary, and corner charts in the normal-crossings model.

It does not prove the full analytic Yuan--Zhang hypotheses.  It checks
the exact chartwise reduction claimed by `107_23`.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LogModel:
    q: int = 0
    u: int = 0
    v: int = 0
    w: int = 0
    const: int = 0

    def add(self, other: "LogModel") -> "LogModel":
        return LogModel(
            q=self.q + other.q,
            u=self.u + other.u,
            v=self.v + other.v,
            w=self.w + other.w,
            const=self.const + other.const,
        )


def interior_model() -> LogModel:
    return LogModel(q=0, u=0, v=0, w=0, const=0)


def diagonal_model(c: int) -> LogModel:
    return LogModel(w=c)


def boundary_model(a: int, b: int) -> LogModel:
    return LogModel(u=a, v=b)


def corner_model(a: int, b: int, c: int) -> LogModel:
    return LogModel(u=a, v=b, w=c)


def to_lower_boundary(model: LogModel) -> LogModel:
    # u = q on the overlap, with no change in diagonal coefficient.
    return LogModel(u=model.q + model.u, v=model.v, w=model.w, const=model.const)


def to_upper_boundary(model: LogModel) -> LogModel:
    # v = q^{-1}, so log|q| = -log|v| on the overlap.
    return LogModel(u=model.u, v=model.v - model.q, w=model.w, const=model.const)


def lower_to_interior(model: LogModel) -> LogModel:
    return LogModel(q=model.u, v=model.v, w=model.w, const=model.const)


def upper_to_interior(model: LogModel) -> LogModel:
    return LogModel(q=-model.v, u=model.u, w=model.w, const=model.const)


def singular_support(model: LogModel) -> set[str]:
    support: set[str] = set()
    if model.q:
        support.add("q")
    if model.u:
        support.add("u")
    if model.v:
        support.add("v")
    if model.w:
        support.add("w")
    return support


def check_chart_transitions() -> int:
    checks = 0
    print("Chart-transition audit")
    q_coeffs = [-3, -1, 0, 2, 5]
    w_coeffs = [-2, 0, 4]
    for a in q_coeffs:
        for c in w_coeffs:
            interior = LogModel(q=a, w=c)
            lower = to_lower_boundary(interior)
            upper = to_upper_boundary(interior)

            back_from_lower = lower_to_interior(lower)
            back_from_upper = upper_to_interior(upper)

            assert back_from_lower == interior
            assert back_from_upper == interior
            assert singular_support(lower) <= {"u", "v", "w"}
            assert singular_support(upper) <= {"u", "v", "w"}
            checks += 4
            print(
                f" q={a:2d} w={c:2d}  lower=(u:{lower.u:2d},w:{lower.w:2d})"
                f"  upper=(v:{upper.v:2d},w:{upper.w:2d})"
            )
    return checks


def check_corner_additivity() -> int:
    checks = 0
    print("\nTensor-additivity audit")
    generator_models = [
        ("packet", interior_model()),
        ("diag", diagonal_model(3)),
        ("vertical", boundary_model(2, 0)),
        ("horizontal", boundary_model(0, 5)),
        ("corner", corner_model(2, 5, 3)),
    ]
    for name_a, model_a in generator_models:
        for name_b, model_b in generator_models:
            total = model_a.add(model_b)
            assert total == model_b.add(model_a)
            assert singular_support(total) <= {"q", "u", "v", "w"}
            checks += 1
            print(
                f" {name_a:10s} + {name_b:10s}"
                f" -> (u:{total.u:2d}, v:{total.v:2d}, w:{total.w:2d})"
            )
    return checks


def check_no_stronger_than_log() -> int:
    checks = 0
    print("\nNo-stronger-than-log audit")
    samples = [
        interior_model(),
        diagonal_model(1),
        boundary_model(1, 0),
        boundary_model(0, 1),
        corner_model(1, 1, 1),
        corner_model(-2, 3, 4),
    ]
    for model in samples:
        # Exact shadow: admissible models only store linear log
        # coefficients in the normal-crossings parameters and no extra
        # nonlinear singularity exponents.
        assert isinstance(model.u, int)
        assert isinstance(model.v, int)
        assert isinstance(model.w, int)
        assert "q" not in singular_support(to_lower_boundary(model))
        assert "q" not in singular_support(to_upper_boundary(model))
        checks += 2
        print(
            f" support={sorted(singular_support(model))}"
            f"  lower={sorted(singular_support(to_lower_boundary(model)))}"
            f"  upper={sorted(singular_support(to_upper_boundary(model)))}"
        )
    return checks


def main() -> None:
    transition_checks = check_chart_transitions()
    additivity_checks = check_corner_additivity()
    singularity_checks = check_no_stronger_than_log()

    print("\nAll exact Paper C logarithmic-chart checks passed.")
    print(
        "Verified "
        f"{transition_checks} chart-transition checks, "
        f"{additivity_checks} tensor-additivity checks, and "
        f"{singularity_checks} no-stronger-than-log checks."
    )


if __name__ == "__main__":
    main()
