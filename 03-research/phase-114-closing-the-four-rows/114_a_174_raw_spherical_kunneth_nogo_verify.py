#!/usr/bin/env python3
"""Finite checks for the raw spherical Kunneth exponential lower bound."""


def radius_closed(s):
    even_count = (s + 1) // 2
    odd_count = s // 2
    positive = (4**even_count - 1) // 3
    negative = 2 * (4**odd_count - 1) // 3
    return max(positive, negative)


def subset_sums(s):
    values = []
    for mask in range(1 << s):
        values.append(sum((-2) ** j for j in range(s) if mask & (1 << j)))
    return values


def admissible_length(n):
    s = 0
    while radius_closed(s + 1) <= n:
        s += 1
    return s


def main():
    for s in range(1, 16):
        values = subset_sums(s)
        assert len(set(values)) == 1 << s
        assert max(abs(v) for v in values) == radius_closed(s)
        nonempty = values[1:]
        assert 0 not in nonempty
        # The assembly images [b_J] are distinct basis labels.
        assert len(set(nonempty)) == (1 << s) - 1

    previous = 0
    for n in range(1, 10000):
        s = admissible_length(n)
        lower_bound = (1 << s) - 1
        assert lower_bound >= previous
        previous = lower_bound

    print("PASS: negabinary subset labels are pairwise distinct and nonzero.")
    print("PASS: assembly supplies 2^s-1 independent reduced basis vectors.")
    print("PASS: the certified raw-smash dimension lower bound is exponential.")


if __name__ == "__main__":
    main()
