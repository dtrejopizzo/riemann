# Phase 60 — E5: el violador L_DH. RESULTADOS (honesto, inconcluso) **Fecha:** 2026-06-16 · **Código:** `E5_ldh_violator.py`, `E5b_*`, `E5c_dispersion_profile.py` ## Objetivo
Testear el mapa a RH (Eslabon 2): el operador CCM es auto-adjunto -> espectro REAL siempre;
L_DH tiene un cero OFF-line (85.699+0.3085i), que un autovalor real no puede igualar -> la
convergencia DEBE romperse. Buscabamos el testigo numerico de "convergencia <=> RH". ## Lo construido (real, primero en el programa)
- Engine CCM parametrizado en forma de Fourier (a, conductor, coeficientes, polo).
- Operador CCM de **L_DH**: arquimediano a=3/4, conductor 5, sin polo (f entera), coeficientes b(n) = -f'/f (soporte denso en todo n), κ_DH=0.284079.
- **Gate ζ PASA** en el engine nuevo: raiz exacta 14.1347 y, a altura 85, el cero on-line de ζ 84.7355 reproducido (disp 3e-4 sobre N=44..60). ## Resultado decisivo: NEGATIVO / inconcluso **E5b** (convergencia en N del autovalor): L_DH dispersa 0.13 en H=85.7 vs ~0.03 en control
H=48 — peor, pero el control no quedo plano. **E5c** (perfil de dispersion vs altura, el test limpio): la dispersion de L_DH **NO tiene
pico localizado en los ceros off-line (85.7, 114)**. Crece **suave y monotona con la altura**
(0.005 en H=24 -> 0.1 en H=80 -> 16 en H=120). En H=84,86 es 0.04, *menor* que en H=74-80. Por criterio pre-registrado: crecimiento suave con H = resolucion/truncacion, **no** firma
del cero off-line. **El testigo numerico de "convergencia <=> RH" NO queda establecido a λ=3.7.** ## Caveats que invalidan una conclusion fuerte (declarados)
1. **λ=3.7 demasiado chico para L_DH:** b(n) denso truncado en n<=13 es burdo; explica la degradacion suave con la altura. La region H>100 esta directamente sin resolver.
2. ~~a=3/4 NO validado~~ **CERRADO (E5d):** el arquimediano a=3/4 se valido sobre L(χ_-4) (caracter impar real mod 4, Euler, RH-true): ceros 6.0209, 10.2438, 12.9881, 16.3426 reproducidos a ~1e-6 (limitado por los valores de referencia, no el engine). Por tanto el operador de L_DH usa un arquimediano CORRECTO y el resultado negativo de E5 es real.
3. **Metrica probablemente equivocada:** por Thm 1.1(iii) el cero off-line seria un autovalor FALTANTE (invisible al espectro real), no uno de alta dispersion. Diagnostico correcto: |ξ̂_{λ,N}(85.699+0.3085i)| (que no puede anularse) vs Ξ_DH(ahi)=0, y su no-convergencia a 0. ## Estado del mapa tras E5
- Mecanismo matematico **intacto como teorema** (Hurwitz + Thm 1.1(iii)): aproximantes con solo raices reales no convergen a Ξ_DH (cero complejo). No depende del experimento.
- Demostracion numerica del mecanismo: **abierta**. Requiere (a) validar a=3/4 sobre L(χ4); (b) λ grande con L_DH resuelto hasta H~85 (arith sums grandes + mpmath); (c) el diagnostico del determinante complejo (E6), no la dispersion. ## Honesto
No hubo victoria. Se construyo el instrumento correcto y el experimento decisivo salio
inconcluso a parametros accesibles, con un caveat de validacion (a=3/4) que hay que cerrar
antes de cualquier afirmacion. El siguiente paso real es E6 (determinante complejo) tras
validar a=3/4 — no seguir forzando la metrica de dispersion.
