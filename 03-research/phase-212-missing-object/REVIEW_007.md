# Revisión de la ronda 7 (`ROUND_007_A.md`, `ROUND_007_B.md`, `ROUND_007_C.md`)

Ninguna candidata pasa la puerta. Signo global: OPEN. Se rederivaron los lemas marcados PROVED que se
citan abajo; el resto conserva la etiqueta del memo.

## R7-a. Cotas de contacto por potencial (ROUND_007_A, Lema 1.1 y Teorema 2.1)

- Lema 1.1, rederivado: para `φ > 0`, `v F(t)F(s) = (v/2)[(φ(s)/φ(t))F(t)² + (φ(t)/φ(s))F(s)²] −
  (v/2)φ(t)φ(s)(F(t)/φ(t) − F(s)/φ(s))²`. Vale igual con emparejamientos (`T < log p`) y con cadenas. Si `φ`
  cambia de signo entre órbitas el potencial sigue siendo `≥ 0`. PROVED.
- Teorema 2.1, rederivado: si cada contacto se acota por un potencial `V_p ≥ 0`, el resto es
  `Arch − ∫ΣV_pF² ⪯ Arch`, que tiene fondo negativo sobre `P_T` para `T` por encima del umbral arquimediano
  (Paper 47 cor:Tarch, CITED; umbral en `[0.58, 0.60]`). La clase muere antes de `0.60`, con cualquier número
  de primos, cualquier `φ_p`, `θ_p(t,s)` y `W_p(t)`. PROVED relativo a la cita. Independiente del peso.
- Consecuencia: la hipótesis «emparejamiento frente a cadena» no explica el umbral `0.695–0.70` de la clase
  DIR, que no pertenece a esta clase (sus piezas conservan el contacto junto con energía de núcleo).
- Ecuación de `ℓ`: vector propio superior de `Y₃ − Y₂` para el par obstructor. PROVED en la discretización,
  ARGUED en el continuo. Sin fórmula mientras el par no se resuelva. Circular como regla previa (J3).

## R7-b. Predicados de etapa (ROUND_007_B, Lemas 1 y 2)

- Lema 1, rederivado: si `𝒫_k(Q)` es «`Q + R_k ∈ 𝒦`» con `𝒦` cono convexo y el paso debe valer para toda
  `Q`, tomando `Q = −R_k` se obtiene `R_{k+1} − R_k − Π_n ∈ 𝒦`; el recíproco es la suma en el cono. La
  inducción es un reparto local por contactos. PROVED.
- Lema 2 (inercia acotada con paso uniforme): PROVED en dimensión finita, ARGUED para la forma.
- Las seis direcciones examinadas caen en entradas cerradas (clasificación ARGUED): §O, L6, BARRIER_W_001,
  lem:degen y §P, R162_802 / R162_2701 / R5-d, P122_018, J3.
- Sin excluir: paso dependiente de la historia con un dato de etapa de fórmula propia. Sin objeto.

## R7-c. Canal de producto (ROUND_007_C)

- Lema, rederivado: con `A(ξ) = Σ a_n n^{−1/2+iξ}`, `a_n` reales y `g` real par,
  `Σ a_m a_n (mn)^{−1/2} g(log m − log n) = (1/2π)∫ĝ|A|²` y
  `Σ a_m a_n (mn)^{−1/2} g(log mn) = (1/2π)∫ĝ Re A²`. PROVED.
- El canal con signo no depende de la aritmética; el canal aritmético no tiene signo. Repetición de
  R161_034 y de K2–K3. Lectura del término que pierde el signo con `c = 2`: ARGUED.
- Reapertura: la ya escrita en R161_034 §0.

## Lo que la ronda deja en pie

- NUMÉRICO sin fórmula: reparto de dos posiciones hasta `T ≈ 0.695`; déficit de un cuadrado pasado el umbral.
- Por encima del umbral arquimediano ninguna pieza que acote los contactos por arriba sirve: los contactos
  deben aportar positivamente en las direcciones negativas de `Arch`.
