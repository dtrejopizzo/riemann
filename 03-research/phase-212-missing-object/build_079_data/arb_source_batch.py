"""Shared linear polynomial source operator for T=4/5, formula (70).

This module is for subsequent executions. It does not alter running jobs.
"""
from math import comb,factorial
from flint import arb,arb_mat,arb_poly


def arch_matrix(T,degree,kernel,sigma):
    K = len(kernel)-1
    height = degree+K+2
    powers = [T**j for j in range(degree+K+2)]
    H = arb_mat([[powers[m+j+1]/(m+j+1) for m in range(degree+1)] for j in range(K+1)])
    L = arb_mat([[(kernel[l+j]*comb(l+j,l)*((-1)**l+sigma)) if l+j<=K else arb(0)
                  for j in range(K+1)] for l in range(K+1)])
    low = L*H
    A = arb_mat(height,degree+1)
    for n in range(K+1):
        for m in range(degree+1): A[n,m] = -low[n,m]
    facts = [factorial(j) for j in range(height)]
    for m in range(degree+1):
        for k in range(1,K+1,2):
            n = m+k+1
            A[n,m] -= 2*kernel[k]*arb(facts[m]*facts[k])/facts[n]
    constant = -arb.const_euler()-(2*arb.pi()*T).log()
    harmonic = arb(0)
    for m in range(degree+1):
        if m: harmonic += arb(1)/m
        A[m,m] += constant+harmonic
        for j in range(m):
            A[m-1-j,m] -= powers[j+1]/(2*(j+1))
            A[j,m] -= sigma*(-1)**j*powers[m-j]/(2*(m-j))
    return A


def translation(degree,offset,slope):
    powers = [offset**j for j in range(degree+1)]
    return arb_mat([[comb(m,j)*powers[m-j]*slope**j if j<=m else arb(0)
                     for m in range(degree+1)] for j in range(degree+1)])


def build_sources(columns,kernel,sigma):
    assert columns and sigma in (-1,1)
    degree = len(columns[0])-1
    assert all(len(column)==degree+1 for column in columns)
    count = len(columns)
    T = arb(4)/5
    F = arb_mat([[column[m] for column in columns] for m in range(degree+1)])
    base = arch_matrix(T,degree,kernel,sigma)*F
    height = degree+len(kernel)+1
    logs = [[arb_poly([factor(m)*column[m] for m in range(degree+1)]) for factor in (
                 lambda m: arb(sigma*(-1)**m-1)/2,
                 lambda m: -arb(1)/2,
                 lambda m: -arb(sigma*(-1)**m)/2)] for column in columns]
    lengths = [arb(n).log() for n in (2,3,4)]
    weights = [arb(p).log()/arb(n).sqrt() for n,p in ((2,2),(3,3),(4,2))]
    edges = [arb(0),T-lengths[0],lengths[1]-T,lengths[2]-T,lengths[0],T]
    assert all(a<b for a,b in zip(edges,edges[1:]))
    shifts = []
    for length,weight in zip(lengths,weights):
        for offset,slope,factor in ((length,1,1),(-length,1,1),(length,-1,sigma)):
            active = []
            for a,b in zip(edges,edges[1:]):
                argument = offset+slope*(a+b)/2
                if argument > 0 and argument < T: active.append(True)
                elif argument < 0 or argument > T: active.append(False)
                else: raise ArithmeticError('Unresolved contact activity')
            if any(active):
                shifts.append((active,translation(degree,offset,slope)*F*(-factor*weight)))
    result = [[] for _ in columns]
    for piece,(a,b) in enumerate(zip(edges,edges[1:])):
        current = [[base[m,i] for i in range(count)] for m in range(height)]
        for active,shift in shifts:
            if active[piece]:
                for m in range(degree+1):
                    for i in range(count): current[m][i] += shift[m,i]
        for i in range(count):
            polynomial = arb_poly([row[i] for row in current])
            result[i].append((a,b,[polynomial,*logs[i]]))
    return result
