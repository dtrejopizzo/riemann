# Ronda 28, memo A — Estado extremal del problema de peso libre no negativo

Todo lo que sigue es NUMÉRICO (doble precisión, Galerkin de Legendre de P47 eq:Aform, SDP con SCS; bases 30 y 40).
Los scripts y salidas están en la carpeta temporal de trabajo `pbp_dual/` (`dual.py`, `analyze.py`, `an_T_N.txt`,
`crho_T_N.csv`). El cómputo quedó interrumpido antes de la lectura; este memo recoge sólo lo que las salidas muestran.

## Problema

`V*_T⁺ = max_{w ≥ 0} λ_min(a^w_T)` sobre `P_T`. Variable dual: estado mixto `ρ*` de traza 1 en el autoespacio inferior,
con `c_ρ*(log n) = 0` donde `w*_n > 0` y `c_ρ*(log n) ≥ 0` donde `w*_n = 0` (signo según la convención del script).
KKT verificadas en `T = 1.6`, base 40: `max|c_ρ*|` sobre `w* > 0` igual a `1.1e-10`; complementariedad `2.3e-11`.

## T = 1.6, base 40 (`V*_T⁺ = 0.00862`)

| n | v_n | w*_n | w*/v |
|---|---|---|---|
| 2 | 0.980 | 0.853 | 0.87 |
| 3 | 1.269 | 0.919 | 0.72 |
| 4 | 0.693 | 0.432 | 0.62 |
| 5 | 1.440 | 0.721 | 0.50 |
| 6 | 0 | 0.042 | — |
| 7 | 1.471 | 0.471 | 0.32 |
| 8 | 0.490 | 0.280 | 0.57 |
| 9 | 0.732 | 0 | 0 |
| 10 | 0 | 0.170 | — |
| 11 | 1.446 | 0.135 | 0.09 |
| 12 | 0 | 0.147 | — |
| 13 | 1.423 | 0.009 | 0.006 |
| 14–24 | — | 0 | — |

- El conjunto `{n : w*_n > 0}` NO es el de las potencias de primos: contiene 6, 10, 12 y excluye 9, 16, 17, 19, 23.
  La lectura «el óptimo reproduce el patrón de los primos» (hecha sobre los diez primeros valores de 212-26-A) es falsa.
- El peso óptimo se apoya en `n ≤ 13` y es cero en la capa superior de la ventana.
- `ρ*` tiene rango 2: una componente impar y una par, con pesos `0.503` y `0.497`, frecuencia media `≈ 6.7` en ambas,
  8–9 nodos, pico en `|t| ≈ 0.88`. Equivale a un solo test complejo `G = (F_par + iF_impar)/√2` con `c_ρ* = Re c_G`.
- `c_ρ*(u)` cambia de signo en `u = 0.24, 0.693, 1.107, 1.387, 1.613, 1.800, 1.947, 2.080, 2.307, 2.400, 2.493, 2.573, 3.2`:
  salvo el primero y el último, son `log n` para `n = 2,…,8, 10,…,13`. Entre contactos oscila con espaciado
  decreciente; `c_ρ*″(0) ≈ −49.6`; mínimo `−0.654`.
- Cosenos principales del soporte de `ρ*` con `span{Π_T(M∗φ_j)}` (10 funciones): `0.999, 0.983`; con el control sin `M`:
  `0.962, 0.936`; con un subespacio aleatorio de dimensión 10: `0.477, 0.352` (`dim P_T = 38`). No discrimina.

## T = 2.4, base 40

No convergido: en esa base el cociente de Rayleigh del peso verdadero sobre `X_δ` da `4.8e-5` en vez de un valor
diminuto. La tabla muestra pesos positivos en 6, 12, 15, 20, 21, 28, 36, 50 y pesos nulos en muchas potencias de primo;
no se usa.

## Lectura

- El estado extremal es un paquete de frecuencia `≈ 6.7`, cerca de donde el multiplicador arquimediano cambia de signo,
  cuya autocorrelación se anula en los `log n` chicos. Sin fórmula candidata.
- No aparece el patrón de los primos en el soporte del peso óptimo.
- OPEN: comportamiento para `T ≥ 2` con bases que resuelvan el borde; si `w*_n/v_n → 1` a `n` fijo.
