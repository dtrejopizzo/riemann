"""
The Riemann zeros analysed through three signal-processing lenses.

SINGLE SIGNAL:  h(u) = sum_k cos(gamma_k * u),   u = log(x)
  - In the TIME domain (u) it has peaks/transients at u = log(p^k)
    -> the PRIMES are the 'beats' (like percussion).
  - Its CARRIER frequencies are the gamma_k -> the ZEROS are the 'tones'.
  Reading u as seconds and gamma_k as angular frequency, the signal
  sounds between gamma_1/2pi ~ 2.25 Hz and gamma_N/2pi ~ 1500 Hz: real audio.

THREE OUTPUTS:
  (1) Sound-like spectrogram (STFT): time u vs frequency. Horizontal
      lines = the tones (zeros); vertical stripes = the beats (primes).
  (2) Global FFT: the line spectrum. Peaks at f = gamma_k/2pi (the zeros).
  (3) Wavelet scalogram (Morlet, CWT): time-scale plane. The prime
      transients appear as vertical ridges; the log-frequency resolution
      separates the low zeros better.
A WAV file is also exported to listen to the zeros.
"""
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import stft
from scipy.io import wavfile

# ---------- load zeros ----------
gammas = np.loadtxt("zeros_10000.txt")
N = len(gammas)
print(f"{N} zeros. gamma_1={gammas[0]:.3f}, gamma_N={gammas[-1]:.3f}")

# ---------- build the signal h(u) = sum cos(gamma_k u) ----------
fs = 8000.0                 # 'sample rate' (u in seconds)
U_MAX = 4.5                 # covers log(x) up to x = e^4.5 ~ 90
u = np.arange(0, U_MAX, 1.0 / fs)
# vectorised block sum to keep memory bounded
h = np.zeros_like(u)
for g in gammas:
    h += np.cos(g * u)
h /= N  # normalise

# positions of the primes on the u axis
def log_prime_powers(pmax=90):
    def es_primo(n):
        if n < 2: return False
        for d in range(2, int(n**0.5)+1):
            if n % d == 0: return False
        return True
    out = []
    for p in range(2, pmax+1):
        if es_primo(p):
            k = 1
            while p**k <= pmax:
                out.append((math.log(p**k), p, k))
                k += 1
    return out
primos_u = log_prime_powers(int(math.e**U_MAX))

# ==================================================================
# (1) SOUND-LIKE SPECTROGRAM (STFT)
# ==================================================================
f_stft, t_stft, Zxx = stft(h, fs=fs, nperseg=1024, noverlap=896)
S = np.abs(Zxx)
S_db = 20 * np.log10(S + 1e-6)

fig1, ax = plt.subplots(figsize=(15, 7))
pcm = ax.pcolormesh(t_stft, f_stft, S_db, shading="gouraud", cmap="magma")
for (lu, p, k) in primos_u:
    ax.axvline(lu, color="cyan", linewidth=0.7, linestyle=":", alpha=0.6)
ax.set_ylim(0, 1600)
ax.set_title("(1) Sound-like SPECTROGRAM of the zeros: horizontal tones (zeros), vertical beats (primes)")
ax.set_xlabel("u = log(x)   (time)")
ax.set_ylabel("frequency [Hz]  (= gamma / 2pi)")
fig1.colorbar(pcm, ax=ax, label="dB")
# mark the first primes at the top
for (lu, p, k) in primos_u:
    if k == 1 and lu < U_MAX:
        ax.annotate(f"{p}", xy=(lu, 1550), color="cyan", fontsize=8, ha="center")
fig1.tight_layout()
fig1.savefig("espec_1_sonido.png", dpi=130)
print("Saved: espec_1_sonido.png")

# ==================================================================
# (2) GLOBAL FFT
# ==================================================================
H = np.fft.rfft(h * np.hanning(len(h)))
freqs = np.fft.rfftfreq(len(h), 1.0 / fs)
mag = np.abs(H)

fig2, ax = plt.subplots(figsize=(15, 6))
ax.plot(freqs, mag, color="#7c3aed", linewidth=0.8)
# mark the first zeros as frequencies
for g in gammas[:40]:
    ax.axvline(g / (2*math.pi), color="#dc2626", linewidth=0.6, linestyle="--", alpha=0.5)
ax.plot([], [], color="#dc2626", linestyle="--", label="gamma_k / 2pi (zeros)")
ax.set_xlim(0, 120)
ax.set_title("(2) FFT of the signal: the line spectrum. Each peak is a zeta zero (f = gamma/2pi)")
ax.set_xlabel("frequency [Hz]")
ax.set_ylabel("magnitude")
ax.grid(True, alpha=0.3)
ax.legend()
fig2.tight_layout()
fig2.savefig("espec_2_fft.png", dpi=130)
print("Saved: espec_2_fft.png")

# ==================================================================
# (3) WAVELET SCALOGRAM (Morlet, CWT via FFT)
# ==================================================================
def cwt_morlet(sig, scales, w0=6.0):
    n = len(sig)
    sig_ft = np.fft.fft(sig)
    freqs_ang = 2 * np.pi * np.fft.fftfreq(n, 1.0 / fs)
    out = np.empty((len(scales), n))
    for i, a in enumerate(scales):
        # Morlet in frequency: exp(-(a*w - w0)^2 / 2)
        psi = (np.pi**-0.25) * np.exp(-0.5 * (a * freqs_ang - w0)**2) * np.sqrt(a)
        conv = np.fft.ifft(sig_ft * psi)
        out[i] = np.abs(conv)
    return out

# scales -> frequencies:  f = w0 / (2 pi a)  => a = w0 / (2 pi f)
f_min, f_max = 2.0, 300.0
freqs_cwt = np.linspace(f_max, f_min, 200)
scales = 6.0 / (2 * np.pi * freqs_cwt / fs) / fs  # scale in 'seconds'
scales = (6.0) / (2 * np.pi * freqs_cwt)  # in units of u
# subsample the signal for the CWT (reduce cost)
sub = 2
hs = h[::sub]
fs_sub = fs / sub

def cwt_morlet_sub(sig, freqs_hz, w0=6.0, fsr=fs_sub):
    n = len(sig)
    sig_ft = np.fft.fft(sig)
    wang = 2*np.pi*np.fft.fftfreq(n, 1.0/fsr)
    out = np.empty((len(freqs_hz), n))
    for i, f in enumerate(freqs_hz):
        a = w0/(2*np.pi*f)          # scale at which the wavelet resonates at f
        psi = (np.pi**-0.25)*np.exp(-0.5*(a*wang - w0)**2)*np.sqrt(2*np.pi*a*fsr)
        out[i] = np.abs(np.fft.ifft(sig_ft*psi))
    return out

print("Computing Morlet CWT...")
W = cwt_morlet_sub(hs, freqs_cwt)
u_sub = u[::sub]

fig3, ax = plt.subplots(figsize=(15, 7))
pcm = ax.pcolormesh(u_sub, freqs_cwt, W, shading="gouraud", cmap="viridis")
for (lu, p, k) in primos_u:
    ax.axvline(lu, color="white", linewidth=0.6, linestyle=":", alpha=0.5)
    if k == 1 and lu < U_MAX:
        ax.annotate(f"{p}", xy=(lu, 290), color="white", fontsize=8, ha="center")
ax.set_title("(3) WAVELET SCALOGRAM (Morlet): vertical ridges at log(primes), bands at the zeros")
ax.set_xlabel("u = log(x)")
ax.set_ylabel("frequency [Hz]")
fig3.colorbar(pcm, ax=ax, label="|CWT|")
fig3.tight_layout()
fig3.savefig("espec_3_wavelet.png", dpi=130)
print("Saved: espec_3_wavelet.png")

# ==================================================================
# WAV: listen to the zeros
# ==================================================================
audio = h / np.max(np.abs(h))
audio = (audio * 0.9 * 32767).astype(np.int16)
wavfile.write("ceros.wav", int(fs), audio)
print("Saved: ceros.wav  (", len(audio)/fs, "s )")

print("\nPrime peaks (u = log p):")
for (lu, p, k) in primos_u[:8]:
    print(f"  {'log '+str(p) if k==1 else 'log '+str(p)+'^'+str(k):10s} = {lu:.4f}")
