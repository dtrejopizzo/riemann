#!/usr/bin/env python3
"""Exact checks for the span/derived/Witt H7-DEN-TRANS no-go."""

from math import gcd

from sympy import gcdex, primerange


print("A. Distinct residue characteristics force a common apex to zero")
primes = tuple(primerange(2, 30))
for i, p in enumerate(primes):
    for q in primes[i + 1:]:
        u, v, common = (int(value) for value in gcdex(p, q))
        assert common == 1
        assert u * p + v * q == 1
        # In any common unital apex p*1=q*1=0, hence this Bezout sum kills 1.
print("  Bezout gives 1=0 for every tested p!=q")

print("\nB. Derived tensor homology over Z")
for p in primes:
    for q in primes:
        tor_order = gcd(p, q)
        if p == q:
            assert tor_order == p
            # H_0 and H_1 of [F_p --0--> F_p] are both F_p.
        else:
            assert tor_order == 1
            inverse = pow(p, -1, q)
            assert p * inverse % q == 1
            # [F_q --p--> F_q] is acyclic.
print("  cross-prime Tor_0=Tor_1=0; same-prime H_0=H_1=F_p")

print("\nC. Finite Witt truncations never invert their characteristic")
for p in primes[:5]:
    for length in range(1, 6):
        modulus = p**length
        assert gcd(p, modulus) != 1
        try:
            pow(p, -1, modulus)
        except ValueError:
            pass
        else:
            raise AssertionError("p cannot be a unit modulo p^n")
print("  p is noninvertible in every Z/p^nZ tested")

print("\nD. Inverting p destroys residue reduction")
for p in primes[:5]:
    # The formal relation p*(1/p)=1 would reduce to 0*x=1 in F_p.
    assert p % p == 0
    assert 1 % p == 1
    try:
        pow(p, -1, p)
    except ValueError:
        pass
    else:
        raise AssertionError("Q_p cannot reduce 1/p to F_p")
print("  no unital reduction Q_p -> F_p can extend Z_p -> F_p")

print("\nVERDICT: H7 DEN-TRANS SPAN/DERIVED/WITT NO-GO CHECKS PASS")
