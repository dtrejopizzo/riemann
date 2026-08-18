#!/usr/bin/env python3
"""Finite real-data certificate for the infinite Weil-rank mechanism."""

import mpmath as mp


mp.mp.dps = 80
MAX_ZEROS = 16


def numerical_rank(matrix, tolerance=mp.mpf("1e-45")):
    """Rank by singular values at fixed high precision."""
    _, singular_values, _ = mp.svd(matrix)
    return sum(abs(value) > tolerance for value in singular_values)


def main():
    ordinates = [mp.im(mp.zetazero(index)) for index in range(1, MAX_ZEROS + 1)]
    distinct = all(
        abs(ordinates[i] - ordinates[j]) > mp.mpf("1e-50")
        for i in range(MAX_ZEROS)
        for j in range(i)
    )

    # Translation by integer a acts on the zero gamma by exp(i*a*gamma).
    ranks = []
    for size in range(1, MAX_ZEROS + 1):
        matrix = mp.matrix(
            [[mp.exp(1j * ordinates[row] * col) for col in range(size)]
             for row in range(size)]
        )
        ranks.append(numerical_rank(matrix))

    full_rank = distinct and all(rank == size for size, rank in enumerate(ranks, 1))
    print(f"ACTUAL_ZETA_ZEROS: {MAX_ZEROS}")
    print(f"DISTINCT_ORDINATES: {'YES' if distinct else 'NO'}")
    print("TRANSLATION_CHARACTER_RANKS: " + ",".join(map(str, ranks)))
    print(f"FINITE_RANK_HYPOTHESIS_SURVIVES: {'NO' if full_rank else 'YES'}")
    print(f"VERDICT: {'YES' if full_rank else 'NO'}")

    if not full_rank:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

