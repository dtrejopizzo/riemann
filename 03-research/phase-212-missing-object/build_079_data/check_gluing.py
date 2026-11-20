"""BUILD083 diagnostic only: saved Galerkin energy is not recertified."""
import pickle
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss, legval

data = pickle.loads((Path(__file__).parent / 'vec_T0.8.pkl').read_bytes())
T = float(data['T'])
pieces = [(float(a), float(b), d) for a, b, d in data['pieces']]
coeff = np.array([float(row[0]) for row in data['vecs']['ev']])

def evaluate(t):
    t = np.asarray(t)
    result = np.zeros_like(t)
    pos = 0
    for a, b, d in pieces:
        c = coeff[pos:pos+d+1] * np.sqrt((2*np.arange(d+1)+1)/(b-a))
        pos += d+1
        mask = (a < t) & (t < b)
        result[mask] += legval(2*(t[mask]-a)/(b-a)-1, c)
    return result

for order in (64, 96):
    z, w = leggauss(order)
    def quadrature(edges):
        edges = sorted(set(edges))
        return (np.concatenate([(a+b)/2+(b-a)*z/2 for a,b in zip(edges,edges[1:])]),
                np.concatenate([(b-a)*w/2 for a,b in zip(edges,edges[1:])]))
    knots = [x for a,b,d in pieces for x in (a,b)]
    t, weights = quadrature(knots)
    ep = np.stack([np.exp(t/2), np.exp(-t/2)], axis=1)
    gram = np.array([[2*np.sinh(T), 2*T], [2*T, 2*np.sinh(T)]])
    correction = np.linalg.solve(gram, ep.T @ (weights*evaluate(t)))
    def primitive(t):
        t = np.asarray(t)
        return evaluate(t) - (np.abs(t)<T)*(np.exp(t/2)*correction[0]+np.exp(-t/2)*correction[1])
    channels = {}
    for n, mangoldt in ((2,np.log(2)), (3,np.log(3)), (4,np.log(2))):
        length = np.log(n)
        edges = [0., length] + [x for k in knots for x in (-k, length-k) if 0<x<length]
        x, weights_x = quadrature(edges)
        channels[n] = float(mangoldt/np.sqrt(n) * (weights_x @ (primitive(-x)-primitive(length-x))**2))
    print(dict(order=order, norm=float(weights @ primitive(t)**2),
               corrected_moments=(ep.T @ (weights*primitive(t))).tolist(),
               prime_channels=channels, prime_square=sum(channels.values()),
               stored_energy=str(data['out']['ev'][0])), flush=True)

# Diagnostic for the rank-three repair: does the remaining square still
# extract too much from the saved near-null vector? Not a proof of sign.
import json
import mpmath as mm
from regional_upper import build
mm.mp.dps = 60
seed = json.loads((Path(__file__).parent/'regional_seed.json').read_text())
_, test_basis = build(mm.mp,seed['degree'])
poly = np.zeros((seed['degree']+1,3))
for i,p in enumerate(test_basis):
    for j,c in enumerate(p):
        for k in range(3):
            poly[j,k] += float(c*seed['coefficients'][i][k]/seed['denominator'])
def tests(x):
    x = np.asarray(x)
    values = np.stack([np.polynomial.polynomial.polyval(x/T,poly[:,k]) for k in range(3)],axis=1)
    return values*((x>0)&(x<T))[:,None]
for order in (64,96):
    z,w = leggauss(order)
    gram_tests = np.zeros((3,3))
    pairing = np.zeros(3)
    B_value = 0.
    for n,mangoldt in ((2,np.log(2)),(3,np.log(3)),(4,np.log(2))):
        length = np.log(n)
        edges = [0.,length]+[x for k in knots for x in (k,length-k) if 0<x<length]
        x,v = quadrature(edges)
        weight = mangoldt/np.sqrt(n)
        images = np.sqrt(weight/2)*(tests(x)-tests(length-x))
        image_F = np.sqrt(weight)*(primitive(x)-primitive(length-x))
        gram_tests += images.T@(v[:,None]*images)
        pairing += images.T@(v*image_F)
        B_value += v@image_F**2
    used = pairing@np.linalg.solve(gram_tests,pairing)
    print(dict(repair_order=order,glue=B_value,rank_three_used=used,
               remaining_square=B_value-used,stored_energy=str(data['out']['ev'][0])),flush=True)
