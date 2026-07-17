#!/usr/bin/env python3
"""
reproduce.py — Full reproduction script for:
"The ω-Class Decomposition of Dirichlet Polynomials:
 A New Framework for the Lindelöf Hypothesis"

Author: D. Torres
Requirements: numpy, matplotlib
Usage: python reproduce.py [--quick]   (--quick uses only N=10^4)

Generates:
  figures/fig1_alpha_B_trend.pdf
  figures/fig2_crossover.pdf
  figures/fig3_peak_to_mean.pdf
  figures/fig4_resonance.pdf
  figures/fig5_theorem1_verification.pdf
  figures/fig6_four_panel_summary.pdf
  results/computation_results.json
"""

import os
import sys
import json
import time
import argparse
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# ══════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ══════════════════════════════════════════════════════════════════════════

OUTDIR_FIG = os.path.join(os.path.dirname(__file__), 'figures')
OUTDIR_RES = os.path.join(os.path.dirname(__file__), 'results')
os.makedirs(OUTDIR_FIG, exist_ok=True)
os.makedirs(OUTDIR_RES, exist_ok=True)

# Plotting style
plt.rcParams.update({
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'legend.fontsize': 10,
    'figure.figsize': (7, 5),
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
})

# ══════════════════════════════════════════════════════════════════════════
# CORE ENGINE
# ══════════════════════════════════════════════════════════════════════════

def compute_omega(N):
    """
    Compute ω(n) for all n ≤ N using smallest-prime-factor sieve.
    Returns: omega[n], spf[n] arrays (1-indexed, omega[0]=omega[1]=0).
    Complexity: O(N log log N).
    """
    spf = np.zeros(N + 1, dtype=np.int32)  # smallest prime factor
    omega = np.zeros(N + 1, dtype=np.int32)

    # Sieve of Eratosthenes variant
    for p in range(2, N + 1):
        if spf[p] == 0:  # p is prime
            spf[p] = p
            omega[p] = 1
            for multiple in range(2 * p, N + 1, p):
                if spf[multiple] == 0:
                    spf[multiple] = p
                # Count distinct prime factors
                omega[multiple] += 1

    # Fix: the sieve above counts each prime factor once, but we need
    # to handle composite numbers whose omega wasn't set by the loop.
    # Actually, the loop above correctly increments omega for each prime p
    # dividing n. Let's verify and recompute properly.

    # Recompute omega properly using SPF factorization
    omega_correct = np.zeros(N + 1, dtype=np.int32)
    for n in range(2, N + 1):
        m = n
        last_p = 0
        count = 0
        while m > 1:
            p = spf[m]
            if p != last_p:
                count += 1
                last_p = p
            m //= p
        omega_correct[n] = count

    return omega_correct, spf


def compute_omega_fast(N):
    """
    Faster ω(n) computation: increment omega[n] for each prime p | n.
    """
    omega = np.zeros(N + 1, dtype=np.int32)
    is_prime = np.ones(N + 1, dtype=bool)
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(N**0.5) + 1):
        if is_prime[p]:
            # Mark composites
            is_prime[p*p::p] = False
            # Increment omega for all multiples of p
            omega[p::p] += 1

    # Handle primes > sqrt(N)
    for p in range(int(N**0.5) + 1, N + 1):
        if is_prime[p]:
            omega[p::p] += 1

    return omega


def make_t_grid(N, sparse_factor=1):
    """
    Create grid of t-values in [N/10, N] with spacing ~ π/log(N).
    sparse_factor > 1 reduces grid density.
    """
    dt = np.pi / np.log(N) * sparse_factor
    t_start = N / 10.0
    t_end = float(N)
    n_t = int((t_end - t_start) / dt) + 1
    t_array = np.linspace(t_start, t_end, n_t)
    return t_array, dt


def compute_S_k(t_array, N, omega, k_max=None):
    """
    Compute S_k(t; N) = Σ_{ω(n)=k} n^{-1/2-it} for each k and t.

    Returns: dict {k: S_k_array} where S_k_array has shape (len(t_array),)
    """
    if k_max is None:
        k_max = int(np.max(omega[2:N+1]))

    n_vals = np.arange(2, N + 1, dtype=np.float64)
    n_inv_sqrt = n_vals ** (-0.5)
    log_n = np.log(n_vals)
    omega_vals = omega[2:N+1]

    # Precompute masks
    masks = {}
    for k in range(1, k_max + 1):
        masks[k] = (omega_vals == k)

    n_t = len(t_array)
    S_k = {k: np.zeros(n_t, dtype=np.complex128) for k in range(1, k_max + 1)}

    for i_t, t in enumerate(t_array):
        phases = -t * log_n
        n_it = np.exp(1j * phases)
        terms = n_inv_sqrt * n_it  # a_n = 1 for ζ

        for k in range(1, k_max + 1):
            if np.any(masks[k]):
                S_k[k][i_t] = np.sum(terms[masks[k]])

        if (i_t + 1) % 5000 == 0:
            print(f"  Progress: {i_t+1}/{n_t} t-values computed")

    return S_k


def compute_statistics(S_k, k_max):
    """
    From S_k dict, compute D, E, (1+r), B(N), etc.
    """
    n_t = len(S_k[1])

    # D = Σ_k S_k
    D = np.zeros(n_t, dtype=np.complex128)
    for k in range(1, k_max + 1):
        D += S_k[k]

    D_sq = np.abs(D) ** 2

    # E = Σ_k |S_k|²
    E = np.zeros(n_t)
    Sk_sq = {}
    for k in range(1, k_max + 1):
        Sk_sq[k] = np.abs(S_k[k]) ** 2
        E += Sk_sq[k]

    # (1+r) = |D|² / E
    one_plus_r = D_sq / np.maximum(E, 1e-30)

    # B(N) = max over k and t of |S_k|²
    B_N = 0.0
    k_star = 1
    per_class = {}
    for k in range(1, k_max + 1):
        max_Sk_sq = float(np.max(Sk_sq[k]))
        mean_Sk_sq = float(np.mean(Sk_sq[k]))
        R_k = max_Sk_sq / mean_Sk_sq if mean_Sk_sq > 0 else 0

        per_class[k] = {
            'mean_Sk_sq': mean_Sk_sq,
            'max_Sk_sq': max_Sk_sq,
            'R_k': R_k,
        }

        if max_Sk_sq > B_N:
            B_N = max_Sk_sq
            k_star = k

    return {
        'D_sq': D_sq,
        'E': E,
        'one_plus_r': one_plus_r,
        'Sk_sq': Sk_sq,
        'B_N': float(B_N),
        'k_star': int(k_star),
        'max_1pr': float(np.max(one_plus_r)),
        'mean_1pr': float(np.mean(one_plus_r)),
        'per_class': per_class,
    }


def run_computation(N, sparse_factor=1, k_max=None):
    """
    Full pipeline: sieve → grid → class sums → statistics.
    """
    print(f"\n{'='*60}")
    print(f"Computing N = {N:,}")
    print(f"{'='*60}")

    t0 = time.time()

    print("  Sieving ω(n)...")
    omega = compute_omega_fast(N)
    K_N = int(np.max(omega[2:N+1]))
    if k_max is None:
        k_max = K_N
    print(f"  K_N = {K_N}")

    print(f"  Building t-grid (sparse_factor={sparse_factor})...")
    t_array, dt = make_t_grid(N, sparse_factor)
    n_t = len(t_array)
    print(f"  Grid: {n_t} points, dt = {dt:.4f}")

    print("  Computing class sums S_k(t)...")
    S_k = compute_S_k(t_array, N, omega, k_max)

    print("  Computing statistics...")
    stats = compute_statistics(S_k, k_max)

    alpha_B = np.log(stats['B_N']) / np.log(N)

    elapsed = time.time() - t0
    print(f"  Done in {elapsed:.1f}s")
    print(f"  B(N) = {stats['B_N']:.4f}")
    print(f"  k* = {stats['k_star']}")
    print(f"  α_B = {alpha_B:.4f}")
    print(f"  max(1+r) = {stats['max_1pr']:.4f} ≤ K_N = {K_N}")

    # Verify Theorem 1
    assert stats['max_1pr'] <= K_N + 0.01, \
        f"Theorem 1 VIOLATED: max(1+r) = {stats['max_1pr']} > K_N = {K_N}"
    print(f"  ✓ Theorem 1 verified: {stats['max_1pr']:.3f} ≤ {K_N}")

    return {
        'N': N,
        'K_N': K_N,
        'k_max': k_max,
        'n_t': n_t,
        'sparse_factor': sparse_factor,
        'B_N': stats['B_N'],
        'k_star': stats['k_star'],
        'alpha_B': float(alpha_B),
        'max_1pr': stats['max_1pr'],
        'mean_1pr': stats['mean_1pr'],
        'per_class': stats['per_class'],
        'runtime_s': elapsed,
        't_array': t_array,
        'one_plus_r': stats['one_plus_r'],
        'Sk_sq': stats['Sk_sq'],
        'D_sq': stats['D_sq'],
        'E': stats['E'],
    }


# ══════════════════════════════════════════════════════════════════════════
# PHASE RESONANCE ANALYSIS
# ══════════════════════════════════════════════════════════════════════════

def analyze_resonance(t_peak, N, omega, k_target=3):
    """
    Decompose S_k at its peak by size bins.
    Returns bin contributions, phases, and Rayleigh statistic.
    """
    n_vals = np.arange(2, N + 1, dtype=np.float64)
    n_inv_sqrt = n_vals ** (-0.5)
    log_n = np.log(n_vals)
    omega_vals = omega[2:N+1]

    mask_k = (omega_vals == k_target)
    n_k = n_vals[mask_k]
    terms = n_inv_sqrt[mask_k] * np.exp(-1j * t_peak * log_n[mask_k])

    # Size bins
    bins = [(10, 100), (100, 1000), (1000, 10000), (10000, 100000),
            (100000, N + 1)]
    results = []
    for lo, hi in bins:
        bin_mask = (n_k >= lo) & (n_k < hi)
        count = int(np.sum(bin_mask))
        if count == 0:
            continue
        contribution = np.sum(terms[bin_mask])
        results.append({
            'bin': f'[{lo}, {hi})',
            'count': count,
            'contribution': contribution,
            'magnitude': float(np.abs(contribution)),
            'phase': float(np.angle(contribution)),
        })

    # Rayleigh statistic
    contributions = np.array([r['contribution'] for r in results])
    magnitudes = np.array([r['magnitude'] for r in results])
    total = np.sum(contributions)
    rayleigh = np.abs(total) / np.sum(magnitudes)

    # Amplification
    coherent = float(np.abs(total) ** 2)
    incoherent = float(np.sum(magnitudes ** 2))
    amplification = coherent / incoherent if incoherent > 0 else 0

    return {
        'bins': results,
        'rayleigh_R': float(rayleigh),
        'amplification': float(amplification),
        'Sk_sq': float(np.abs(np.sum(terms)) ** 2),
    }


# ══════════════════════════════════════════════════════════════════════════
# FIGURE GENERATION
# ══════════════════════════════════════════════════════════════════════════

def fig1_alpha_B_trend(all_results):
    """Figure 1: α_B vs N with threshold lines."""
    fig, ax = plt.subplots(figsize=(7, 5))

    Ns = [r['N'] for r in all_results]
    alphas = [r['alpha_B'] for r in all_results]
    k_stars = [r['k_star'] for r in all_results]

    # Color by dominant k
    colors = ['#2196F3' if k == 2 else '#FF5722' for k in k_stars]

    ax.scatter(Ns, alphas, c=colors, s=100, zorder=5, edgecolors='black',
               linewidths=0.5)

    # Connect with dashed line
    ax.plot(Ns, alphas, 'k--', alpha=0.5, linewidth=1)

    # Threshold lines
    ax.axhline(y=0.310, color='green', linestyle=':', linewidth=1.5,
               label=r'Bourgain: $\alpha < 0.310$')
    ax.axhline(y=0.500, color='orange', linestyle=':', linewidth=1.5,
               label=r'Convexity: $\alpha < 0.500$')
    ax.axhline(y=0.0, color='red', linestyle=':', linewidth=1.5,
               label=r'Lindelöf: $\alpha \to 0$')

    # Model fit (1/log log N) — only k=2 regime
    k2_mask = [k == 2 for k in k_stars]
    if sum(k2_mask) >= 2:
        Ns_k2 = [N for N, m in zip(Ns, k2_mask) if m]
        N_fit = np.logspace(np.log10(min(Ns_k2)), np.log10(5e5), 100)
        alpha_fit = 0.98 / np.log(np.log(N_fit))
        ax.plot(N_fit, alpha_fit, 'b-', alpha=0.3, linewidth=2,
                label=r'Model: $0.98 / \ln\ln N$')

    # Annotations
    for N, a, k in zip(Ns, alphas, k_stars):
        ax.annotate(f'$k^*={k}$', (N, a),
                    textcoords="offset points", xytext=(10, 5),
                    fontsize=9)

    ax.set_xscale('log')
    ax.set_xlabel('$N$')
    ax.set_ylabel(r'$\alpha_B(N) = \log B(N) / \log N$')
    ax.set_title(r'Empirical Exponent $\alpha_B(N)$ with Improvement Thresholds')
    ax.legend(loc='upper right', fontsize=9)
    ax.set_ylim(-0.05, 0.55)
    ax.grid(True, alpha=0.3)

    fig.savefig(os.path.join(OUTDIR_FIG, 'fig1_alpha_B_trend.pdf'))
    fig.savefig(os.path.join(OUTDIR_FIG, 'fig1_alpha_B_trend.png'))
    plt.close(fig)
    print("  → fig1_alpha_B_trend saved")


def fig2_crossover(all_results):
    """Figure 2: S₂ vs S₃ maxima showing crossover."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    Ns = [r['N'] for r in all_results]
    S2_max = [r['per_class'].get(2, {}).get('max_Sk_sq', 0) for r in all_results]
    S3_max = [r['per_class'].get(3, {}).get('max_Sk_sq', 0) for r in all_results]

    # Left: absolute values
    ax1.plot(Ns, S2_max, 'bo-', label=r'$\max|S_2|^2$', linewidth=2, markersize=8)
    ax1.plot(Ns, S3_max, 'r^-', label=r'$\max|S_3|^2$', linewidth=2, markersize=8)
    ax1.set_xscale('log')
    ax1.set_xlabel('$N$')
    ax1.set_ylabel(r'$\max|S_k|^2$')
    ax1.set_title('Class Sum Maxima')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Right: ratio
    ratios = [s2 / s3 if s3 > 0 else np.inf for s2, s3 in zip(S2_max, S3_max)]
    ax2.plot(Ns, ratios, 'ks-', linewidth=2, markersize=8)
    ax2.axhline(y=1.0, color='red', linestyle='--', linewidth=1.5,
                label='Crossover line')
    ax2.set_xscale('log')
    ax2.set_xlabel('$N$')
    ax2.set_ylabel(r'$\max|S_2|^2 / \max|S_3|^2$')
    ax2.set_title('$k{=}2$ to $k{=}3$ Dominance Transition')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    # Shade crossover region
    ax2.axvspan(8e4, 1.5e5, alpha=0.15, color='red',
                label='Crossover region')

    fig.tight_layout()
    fig.savefig(os.path.join(OUTDIR_FIG, 'fig2_crossover.pdf'))
    fig.savefig(os.path.join(OUTDIR_FIG, 'fig2_crossover.png'))
    plt.close(fig)
    print("  → fig2_crossover saved")


def fig3_peak_to_mean(all_results):
    """Figure 3: Peak-to-mean ratio R_k by class."""
    # Use the largest N result
    r = all_results[-1]
    N = r['N']
    k_max = r['k_max']

    ks = list(range(1, k_max + 1))
    R_ks = [r['per_class'].get(k, {}).get('R_k', 0) for k in ks]
    max_vals = [r['per_class'].get(k, {}).get('max_Sk_sq', 0) for k in ks]
    mean_vals = [r['per_class'].get(k, {}).get('mean_Sk_sq', 0) for k in ks]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Left: R_k bar chart
    colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(ks)))
    bars = ax1.bar(ks, R_ks, color=colors, edgecolor='black', linewidth=0.5)
    ax1.set_xlabel(r'$\omega$-class $k$')
    ax1.set_ylabel(r'$R_k = \max|S_k|^2 / \langle|S_k|^2\rangle$')
    ax1.set_title(f'Peak-to-Mean Ratio ($N = {N:,}$)')
    ax1.set_yscale('log')
    ax1.grid(True, alpha=0.3, axis='y')

    # Add value labels
    for bar, val in zip(bars, R_ks):
        if val > 0:
            ax1.text(bar.get_x() + bar.get_width() / 2, val * 1.1,
                     f'{val:.1f}', ha='center', va='bottom', fontsize=9)

    # Right: max vs mean
    x = np.arange(len(ks))
    width = 0.35
    ax2.bar(x - width/2, mean_vals, width, label=r'$\langle|S_k|^2\rangle$',
            color='#64B5F6', edgecolor='black', linewidth=0.5)
    ax2.bar(x + width/2, max_vals, width, label=r'$\max|S_k|^2$',
            color='#EF5350', edgecolor='black', linewidth=0.5)
    ax2.set_xticks(x)
    ax2.set_xticklabels([f'$k={k}$' for k in ks])
    ax2.set_ylabel(r'$|S_k|^2$')
    ax2.set_title(f'Large Sieve Gap ($N = {N:,}$)')
    ax2.set_yscale('log')
    ax2.legend()
    ax2.grid(True, alpha=0.3, axis='y')

    fig.tight_layout()
    fig.savefig(os.path.join(OUTDIR_FIG, 'fig3_peak_to_mean.pdf'))
    fig.savefig(os.path.join(OUTDIR_FIG, 'fig3_peak_to_mean.png'))
    plt.close(fig)
    print("  → fig3_peak_to_mean saved")


def fig4_resonance(resonance_data):
    """Figure 4: Phase resonance decomposition."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    bins = resonance_data['bins']
    labels = [b['bin'] for b in bins]
    mags = [b['magnitude'] for b in bins]
    phases = [b['phase'] for b in bins]

    # Left: magnitude bar chart
    colors = plt.cm.plasma(np.linspace(0.2, 0.8, len(bins)))
    ax1.barh(range(len(bins)), mags, color=colors, edgecolor='black',
             linewidth=0.5)
    ax1.set_yticks(range(len(bins)))
    ax1.set_yticklabels(labels, fontsize=9)
    ax1.set_xlabel('$|\\text{contribution}|$')
    ax1.set_title(f'$S_3$ Bin Decomposition at Peak')
    ax1.grid(True, alpha=0.3, axis='x')

    # Right: polar plot of contributions
    ax2 = fig.add_subplot(122, projection='polar')
    for i, b in enumerate(bins):
        ax2.annotate('', xy=(b['phase'], b['magnitude']),
                     xytext=(0, 0),
                     arrowprops=dict(arrowstyle='->', color=colors[i],
                                     linewidth=2))
        ax2.plot(b['phase'], b['magnitude'], 'o', color=colors[i],
                 markersize=8)

    # Add resultant
    total = sum(b['contribution'] for b in bins)
    ax2.annotate('', xy=(np.angle(total), np.abs(total)),
                 xytext=(0, 0),
                 arrowprops=dict(arrowstyle='->', color='red',
                                 linewidth=3))
    ax2.set_title(f'Phase Alignment (R = {resonance_data["rayleigh_R"]:.3f})',
                  pad=20)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTDIR_FIG, 'fig4_resonance.pdf'))
    fig.savefig(os.path.join(OUTDIR_FIG, 'fig4_resonance.png'))
    plt.close(fig)
    print("  → fig4_resonance saved")


def fig5_theorem1_verification(all_results):
    """Figure 5: Theorem 1 verification — max(1+r) vs K_N."""
    fig, ax = plt.subplots(figsize=(7, 5))

    Ns = [r['N'] for r in all_results]
    max_1pr = [r['max_1pr'] for r in all_results]
    K_Ns = [r['K_N'] for r in all_results]

    x = np.arange(len(Ns))
    width = 0.35

    ax.bar(x - width/2, max_1pr, width, label=r'Observed $\max(1{+}r)$',
           color='#42A5F5', edgecolor='black', linewidth=0.5)
    ax.bar(x + width/2, K_Ns, width, label=r'Bound $K_N$',
           color='#EF5350', edgecolor='black', linewidth=0.5)

    ax.set_xticks(x)
    ax.set_xticklabels([f'$10^{{{int(np.log10(N))}}}$' if N in [1e4, 1e5]
                        else f'{N/1000:.0f}k' for N in Ns])
    ax.set_xlabel('$N$')
    ax.set_ylabel('Value')
    ax.set_title('Theorem 1 Verification: $(1{+}r) \\leq K_N$')
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')

    # Add gap percentages
    for i, (m, K) in enumerate(zip(max_1pr, K_Ns)):
        gap = (K - m) / K * 100
        ax.text(i, max(m, K) + 0.15,
                f'{gap:.0f}\\% gap', ha='center', fontsize=9)

    fig.savefig(os.path.join(OUTDIR_FIG, 'fig5_theorem1_verification.pdf'))
    fig.savefig(os.path.join(OUTDIR_FIG, 'fig5_theorem1_verification.png'))
    plt.close(fig)
    print("  → fig5_theorem1_verification saved")


def fig6_four_panel_summary(all_results, resonance_data):
    """Figure 6: Four-panel summary figure."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # Panel A: α_B trend
    ax = axes[0, 0]
    Ns = [r['N'] for r in all_results]
    alphas = [r['alpha_B'] for r in all_results]
    k_stars = [r['k_star'] for r in all_results]
    colors = ['#2196F3' if k == 2 else '#FF5722' for k in k_stars]
    ax.scatter(Ns, alphas, c=colors, s=80, zorder=5, edgecolors='black',
               linewidths=0.5)
    ax.plot(Ns, alphas, 'k--', alpha=0.5, linewidth=1)
    ax.axhline(y=0.310, color='green', linestyle=':', linewidth=1.5,
               label='Bourgain')
    ax.axhline(y=0.500, color='orange', linestyle=':', linewidth=1.5,
               label='Convexity')
    ax.set_xscale('log')
    ax.set_ylabel(r'$\alpha_B$')
    ax.set_title('(a) Empirical Exponent')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel B: Crossover
    ax = axes[0, 1]
    S2_max = [r['per_class'].get(2, {}).get('max_Sk_sq', 0) for r in all_results]
    S3_max = [r['per_class'].get(3, {}).get('max_Sk_sq', 0) for r in all_results]
    ax.plot(Ns, S2_max, 'bo-', label=r'$k=2$', linewidth=2, markersize=7)
    ax.plot(Ns, S3_max, 'r^-', label=r'$k=3$', linewidth=2, markersize=7)
    ax.set_xscale('log')
    ax.set_ylabel(r'$\max|S_k|^2$')
    ax.set_title('(b) $k{=}2 \\to k{=}3$ Crossover')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # Panel C: R_k at largest N
    ax = axes[1, 0]
    r = all_results[-1]
    ks = list(range(1, r['k_max'] + 1))
    R_ks = [r['per_class'].get(k, {}).get('R_k', 0) for k in ks]
    cs = plt.cm.viridis(np.linspace(0.2, 0.8, len(ks)))
    ax.bar(ks, R_ks, color=cs, edgecolor='black', linewidth=0.5)
    ax.set_xlabel(r'$k$')
    ax.set_ylabel(r'$R_k$')
    ax.set_title(f'(c) Peak-to-Mean Ratio ($N={r["N"]:,}$)')
    ax.set_yscale('log')
    ax.grid(True, alpha=0.3, axis='y')

    # Panel D: Theorem 1 verification
    ax = axes[1, 1]
    max_1pr = [r['max_1pr'] for r in all_results]
    K_Ns = [r['K_N'] for r in all_results]
    x = np.arange(len(Ns))
    width = 0.35
    ax.bar(x - width/2, max_1pr, width, label=r'$\max(1{+}r)$',
           color='#42A5F5', edgecolor='black', linewidth=0.5)
    ax.bar(x + width/2, K_Ns, width, label=r'$K_N$',
           color='#EF5350', edgecolor='black', linewidth=0.5)
    ax.set_xticks(x)
    ax.set_xticklabels([f'{N/1000:.0f}k' for N in Ns], fontsize=9)
    ax.set_xlabel('$N$')
    ax.set_title('(d) Theorem 1 Verification')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3, axis='y')

    fig.tight_layout()
    fig.savefig(os.path.join(OUTDIR_FIG, 'fig6_four_panel_summary.pdf'))
    fig.savefig(os.path.join(OUTDIR_FIG, 'fig6_four_panel_summary.png'))
    plt.close(fig)
    print("  → fig6_four_panel_summary saved")


# ══════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description='Reproduce computations for the ω-class decomposition paper')
    parser.add_argument('--quick', action='store_true',
                        help='Quick mode: only N=10^4')
    args = parser.parse_args()

    print("=" * 60)
    print("ω-Class Decomposition — Reproduction Script")
    print("=" * 60)

    # Define computation parameters
    if args.quick:
        configs = [
            (10_000, 1),
        ]
    else:
        configs = [
            (10_000, 1),
            (50_000, 2),
            (100_000, 5),
            (150_000, 5),
        ]

    # Run computations
    all_results = []
    for N, sf in configs:
        result = run_computation(N, sparse_factor=sf)
        all_results.append(result)

    # ── Phase resonance analysis ──────────────────────────────────────
    # Use the largest N
    r_last = all_results[-1]
    N_last = r_last['N']

    print("\nAnalyzing phase resonance...")
    omega = compute_omega_fast(N_last)

    # Find the peak t for k=k_star
    k_star = r_last['k_star']
    t_peak_idx = np.argmax(r_last['Sk_sq'][k_star])
    t_peak = r_last['t_array'][t_peak_idx]

    resonance = analyze_resonance(t_peak, N_last, omega, k_target=k_star)
    print(f"  Rayleigh R = {resonance['rayleigh_R']:.3f}")
    print(f"  Amplification = {resonance['amplification']:.2f}×")

    # ── Generate figures ──────────────────────────────────────────────
    print("\nGenerating figures...")
    fig1_alpha_B_trend(all_results)
    if len(all_results) >= 2:
        fig2_crossover(all_results)
    fig3_peak_to_mean(all_results)
    fig4_resonance(resonance)
    fig5_theorem1_verification(all_results)
    fig6_four_panel_summary(all_results, resonance)

    # ── Save JSON results ─────────────────────────────────────────────
    print("\nSaving results...")

    # Strip large arrays for JSON
    json_results = []
    for r in all_results:
        jr = {k: v for k, v in r.items()
              if k not in ('t_array', 'one_plus_r', 'Sk_sq', 'D_sq', 'E')}
        json_results.append(jr)

    output = {
        'computation_results': json_results,
        'resonance_analysis': {
            'N': N_last,
            'k_target': k_star,
            't_peak': float(t_peak),
            'rayleigh_R': resonance['rayleigh_R'],
            'amplification': resonance['amplification'],
            'Sk_sq_at_peak': resonance['Sk_sq'],
        },
        'thresholds': {
            'lindelof': 0.0,
            'bourgain': 0.3095,
            'convexity': 0.5,
        },
        'theorems_verified': {
            'theorem_1': all([r['max_1pr'] <= r['K_N'] + 0.01
                             for r in all_results]),
        },
    }

    with open(os.path.join(OUTDIR_RES, 'computation_results.json'), 'w') as f:
        json.dump(output, f, indent=2)
    print("  → computation_results.json saved")

    # ── Summary ───────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"\n{'N':>10} | {'K_N':>4} | {'B(N)':>8} | {'k*':>3} | {'α_B':>8} | {'max(1+r)':>9}")
    print("-" * 55)
    for r in all_results:
        print(f"{r['N']:>10,} | {r['K_N']:>4} | {r['B_N']:>8.2f} | "
              f"{r['k_star']:>3} | {r['alpha_B']:>8.4f} | {r['max_1pr']:>9.3f}")

    print(f"\nFigures saved to: {OUTDIR_FIG}/")
    print(f"Results saved to: {OUTDIR_RES}/")
    print("\nDone.")


if __name__ == '__main__':
    main()
