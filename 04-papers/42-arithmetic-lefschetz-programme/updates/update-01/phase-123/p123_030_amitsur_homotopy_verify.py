#!/usr/bin/env python3
"""Finite sign/index regression; continuity and exactness use P123.030's proof."""
from collections import Counter
from itertools import product


def differential(chain):
    out = Counter()
    for word, coefficient in chain.items():
        for i in range(len(word)+1):
            out[word[:i]+(0,)+word[i:]] += coefficient*(-1)**i
    return out


def homotopy(chain):
    out = Counter()
    for word, coefficient in chain.items():
        if word and word[0] == 0:
            out[word[1:]] += coefficient
    return out


count = 0
for length in range(7):
    for word in product(range(3), repeat=length):
        c = Counter({word: 1})
        result = homotopy(differential(c))
        result.update(differential(homotopy(c)))
        assert {w:v for w,v in result.items() if v} == {word:1}
        assert not any(differential(differential(c)).values())
        count += 1
print(f'PASS {count} augmented homotopy and d^2 identities')
print('SCOPE: polynomial augmentation model; not a topological or trace comparison test')
