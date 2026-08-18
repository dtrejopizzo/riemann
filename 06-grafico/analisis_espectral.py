"""
Los ceros de Riemann analizados con tres lentes de procesamiento de senal.

SENAL UNICA:  h(u) = sum_k cos(gamma_k * u),   u = log(x)
  - En el dominio del TIEMPO (u): tiene picos/transitorios en u = log(p^k)
    -> los PRIMOS son los 'golpes' (como percusion).
  - Sus frecuencias PORTADORAS son los gamma_k -> los CEROS son los 'tonos'.
  Interpretando u como segundos y gamma_k como frecuencia angular, la senal
  suena entre gamma_1/2pi ~ 2.25 Hz y gamma_N/2pi ~ 1500 Hz: audio real.

TRES SALIDAS:
  (1) Espectrograma tipo sonido (STFT): tiempo u vs frecuencia. Lineas
      horizontales = los tonos (ceros); rayas verticales = los golpes (primos).
  (2) FFT global: el espectro de linea. Picos en f = gamma_k/2pi (los ceros).
  (3) Escalograma wavelet (Morlet, CWT): plano tiempo-escala. Los transitorios
      de los primos aparecen como crestas verticales; la resolucion log-frecuencia
      separa mejor los ceros bajos.
Ademas se exporta un WAV para escuchar los ceros.
"""
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import stft
from scipy.io import wavfile

# ---------- cargar ceros ----------
gammas = np.loadtxt("zeros_10000.txt")
N = len(gammas)
print(f"{N} ceros. gamma_1={gammas[0]:.3f}, gamma_N={gammas[-1]:.3f}")

# ---------- construir la senal h(u) = sum cos(gamma_k u) ----------
fs = 8000.0                 # 'sample rate' (u en segundos)
U_MAX = 4.5                 # cubre log(x) hasta x = e^4.5 ~ 90
u = np.arange(0, U_MAX, 1.0 / fs)
# suma vectorizada por bloques para no reventar memoria
h = np.zeros_like(u)
for g in gammas:
    h += np.cos(g * u)
h /= N  # normalizar

# posiciones de los primos en el eje u
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
# (1) ESPECTROGRAMA TIPO SONIDO (STFT)
# ==================================================================
f_stft, t_stft, Zxx = stft(h, fs=fs, nperseg=1024, noverlap=896)
S = np.abs(Zxx)
S_db = 20 * np.log10(S + 1e-6)

fig1, ax = plt.subplots(figsize=(15, 7))
pcm = ax.pcolormesh(t_stft, f_stft, S_db, shading="gouraud", cmap="magma")
for (lu, p, k) in primos_u:
    ax.axvline(lu, color="cyan", linewidth=0.7, linestyle=":", alpha=0.6)
ax.set_ylim(0, 1600)
ax.set_title("(1) ESPECTROGRAMA tipo sonido de los ceros: tonos horizontales (ceros), golpes verticales (primos)")
ax.set_xlabel("u = log(x)   (tiempo)")
ax.set_ylabel("frecuencia [Hz]  (= gamma / 2pi)")
fig1.colorbar(pcm, ax=ax, label="dB")
# marcar primeros primos arriba
for (lu, p, k) in primos_u:
    if k == 1 and lu < U_MAX:
        ax.annotate(f"{p}", xy=(lu, 1550), color="cyan", fontsize=8, ha="center")
fig1.tight_layout()
fig1.savefig("espec_1_sonido.png", dpi=130)
print("Guardado: espec_1_sonido.png")

# ==================================================================
# (2) FFT GLOBAL
# ==================================================================
H = np.fft.rfft(h * np.hanning(len(h)))
freqs = np.fft.rfftfreq(len(h), 1.0 / fs)
mag = np.abs(H)

fig2, ax = plt.subplots(figsize=(15, 6))
ax.plot(freqs, mag, color="#7c3aed", linewidth=0.8)
# marcar los primeros ceros como frecuencia
for g in gammas[:40]:
    ax.axvline(g / (2*math.pi), color="#dc2626", linewidth=0.6, linestyle="--", alpha=0.5)
ax.plot([], [], color="#dc2626", linestyle="--", label="gamma_k / 2pi (ceros)")
ax.set_xlim(0, 120)
ax.set_title("(2) FFT de la senal: el espectro de linea. Cada pico es un cero de zeta (f = gamma/2pi)")
ax.set_xlabel("frecuencia [Hz]")
ax.set_ylabel("magnitud")
ax.grid(True, alpha=0.3)
ax.legend()
fig2.tight_layout()
fig2.savefig("espec_2_fft.png", dpi=130)
print("Guardado: espec_2_fft.png")

# ==================================================================
# (3) ESCALOGRAMA WAVELET (Morlet, CWT via FFT)
# ==================================================================
def cwt_morlet(sig, scales, w0=6.0):
    n = len(sig)
    sig_ft = np.fft.fft(sig)
    freqs_ang = 2 * np.pi * np.fft.fftfreq(n, 1.0 / fs)
    out = np.empty((len(scales), n))
    for i, a in enumerate(scales):
        # Morlet en frecuencia: exp(-(a*w - w0)^2 / 2)
        psi = (np.pi**-0.25) * np.exp(-0.5 * (a * freqs_ang - w0)**2) * np.sqrt(a)
        conv = np.fft.ifft(sig_ft * psi)
        out[i] = np.abs(conv)
    return out

# escalas -> frecuencias:  f = w0 / (2 pi a)  => a = w0 / (2 pi f)
f_min, f_max = 2.0, 300.0
freqs_cwt = np.linspace(f_max, f_min, 200)
scales = 6.0 / (2 * np.pi * freqs_cwt / fs) / fs  # escala en 'segundos'
scales = (6.0) / (2 * np.pi * freqs_cwt)  # en unidades de u
# submuestrear la senal para la CWT (aliviar costo)
sub = 2
hs = h[::sub]
fs_sub = fs / sub

def cwt_morlet_sub(sig, freqs_hz, w0=6.0, fsr=fs_sub):
    n = len(sig)
    sig_ft = np.fft.fft(sig)
    wang = 2*np.pi*np.fft.fftfreq(n, 1.0/fsr)
    out = np.empty((len(freqs_hz), n))
    for i, f in enumerate(freqs_hz):
        a = w0/(2*np.pi*f)          # escala tal que la wavelet resuena en f
        psi = (np.pi**-0.25)*np.exp(-0.5*(a*wang - w0)**2)*np.sqrt(2*np.pi*a*fsr)
        out[i] = np.abs(np.fft.ifft(sig_ft*psi))
    return out

print("Calculando CWT Morlet...")
W = cwt_morlet_sub(hs, freqs_cwt)
u_sub = u[::sub]

fig3, ax = plt.subplots(figsize=(15, 7))
pcm = ax.pcolormesh(u_sub, freqs_cwt, W, shading="gouraud", cmap="viridis")
for (lu, p, k) in primos_u:
    ax.axvline(lu, color="white", linewidth=0.6, linestyle=":", alpha=0.5)
    if k == 1 and lu < U_MAX:
        ax.annotate(f"{p}", xy=(lu, 290), color="white", fontsize=8, ha="center")
ax.set_title("(3) ESCALOGRAMA WAVELET (Morlet): crestas verticales en log(primos), bandas en los ceros")
ax.set_xlabel("u = log(x)")
ax.set_ylabel("frecuencia [Hz]")
fig3.colorbar(pcm, ax=ax, label="|CWT|")
fig3.tight_layout()
fig3.savefig("espec_3_wavelet.png", dpi=130)
print("Guardado: espec_3_wavelet.png")

# ==================================================================
# WAV: escuchar los ceros
# ==================================================================
audio = h / np.max(np.abs(h))
audio = (audio * 0.9 * 32767).astype(np.int16)
wavfile.write("ceros.wav", int(fs), audio)
print("Guardado: ceros.wav  (", len(audio)/fs, "s )")

print("\nPicos de primos (u = log p):")
for (lu, p, k) in primos_u[:8]:
    print(f"  {'log '+str(p) if k==1 else 'log '+str(p)+'^'+str(k):10s} = {lu:.4f}")
