# Ronda 20, memo B — La identidad de radical de `M` como una sola relación lineal entre el símbolo y los pesos

Nota estructural y modesta. No es un intento de signo. Notación de P47 y de la ronda 7:
`a_T(F) = Arch(F) − Σ_n v_n c_F(log n)`, `v_n = 2Λ(n)/√n`, `c_F(u) = ∫F(t)F(t−u)dt`, `P_T = {∫F e^{±t/2} = 0}`.
`W_*`, `D^W`, `K_Pó`, `M = −K_Pó″ + ¼K_Pó`, `X_T` como en `phase-160-row-d-infinite-T/R160_M4_R1.md` y `ROUND_019_A.md` §2.

## Filtro de cuatro puntos

1. **Antecedente más cercano.** `R160_M4_R1.md` (Teorema A, Lema 2(a): `W_*(K_Pó,·) = 0`, l.18–37, l.74, l.88–89);
   P46 §11 (Thm 11.3, Def–Thm 11.7, Thm 11.11: radical de `I_∞`); P47 `def`/`lem:ext-mob`/`thm:ext-half`/
   `prop:ext-gauge` (main.tex l.9880–9975: el gauge `𝒢_T` es radical de `𝒲`); P47 `thm:inertia-split` (l.3614–3640);
   `phase-200-sign-object/LEMMA_I3_001.md` (I.3-a: `A_RR(c) = (1−c)C`); `ROUND_019_A.md` §3, (3.1);
   índice maestro l.3537 (clase canónica K, radical `𝓝_∞`) y l.5551 (G7D-R162_2101: «casi-núcleo = radical
   truncado (Pólya)»).
2. **Lo nuevo.** Ninguna construcción. Sólo: (a) la identidad escalar `Arch_*(M) = Σ_n v_n c_M(log n)` escrita
   explícitamente con su tabla de signos; (b) la observación de qué identidades aritméticas entran en ella,
   comparada con el gauge de Guo/P47.
3. **Por qué no repite.** No pretende pasar el filtro como constructora; es un puntero preciso.
4. **Conexión con la positividad global.** Ninguna directa (ver §4).

## §1 La identidad

**Enunciado (CITED: R160_M4_R1 Lema 2(a); P46 Thm 11.3, 11.11).** Para `M` en `D^W`, con `A(M) = B(M) = 0`
(momentos `∫M e^{±t/2}`, que se anulan porque `Φ_M(0) = Φ_M(1) = 0`):

    (R)   Arch_*(M) := (1/2π)∫ m(τ)|M̂(τ)|² dτ  =  Σ_{n≥2} v_n c_M(log n),

`m(τ) = Re ψ(¼ + iτ/2) − log π` (P47 eq:symbol). Es el caso diagonal de `W_*(M,G) = 0 ∀G`.

**Lectura clásica (PROVED como lectura; incondicional).** `(R)` es la fórmula explícita de Weil
(P46 Thm 11.3) evaluada en el test autocorrelación `M ⋆ M`, cuya transformada de Mellin es
`Φ_M(s)Φ_M(1−s)` con `Φ_M(s) = s(1−s)ξ(s)`. `M` es la imagen del núcleo de Pólya bajo el operador
`−∂² + ¼` (que en Mellin multiplica por `s(1−s)` y mata el polo y el término en `0, 1`), y `K_Pó` es el
test cuyo transformado es la función completada misma (`Φ_{K_Pó} = ξ`, Def–Thm 11.7). El lado espectral
de la fórmula es la suma sobre ceros de `Φ_M(ρ)Φ_M(1−ρ)`, y cada sumando es `0` por la propia definición
de `ρ`: no se usa ninguna información sobre su ubicación. El lado geométrico es `(R)`.

**Qué identidades entran (PROVED como inventario).** En una sola línea: (i) producto de Euler (la suma de
primos con `Λ` exacta, vía `−ζ′/ζ`); (ii) ecuación funcional (simetría `ξ(s) = ξ(1−s)`, equivalente a la
inversión de theta `θ(1/x) = √x θ(x)`, Poisson sobre `ℤ`); (iii) el factor arquimediano `Γ(s/2)π^{−s/2}`
(el símbolo `m`). Las tres entran juntas, sobre un vector concreto, porque `Φ_{K_Pó} = ξ` las contiene
todas.

## §2 Perfil de `c_M` y tabla (NUMÉRICO)

Cuadratura en `[−6,6]`, paso `10^{−4}`, derivadas analíticas, `n ≤ 9` en theta, paridad de `M`.
`‖M‖² ≈ 97.47`.

- **Signo de `c_M(u)` (función sólo del núcleo, no de la aritmética).** `c_M(0) > 0`; ceros en
  `u ≈ 0.240` y `u ≈ 0.738`; negativa en `(0.240, 0.738)`, positiva en `u > 0.738` (sin más cambios de signo
  detectados hasta `u = 4`, donde `c_M ≈ 10^{−130}`). `log 2 = 0.693` cae en la ventana negativa,
  `log 3 = 1.099` en la positiva. **La alternancia 2 (−), 3 (+) no continúa**: todos los `n ≥ 3` dan `+`.
- **Decaimiento.** `c_M(log n) ≈ e^{−(2π−o(1))n}` por la desigualdad `e^{2t} + n²e^{−2t} ≥ 2n`
  (ROUND_019_A §2(c)); observado `c_M(log 11)/c_M(log 13) ≈ 7·10^4`.

| `n` | `c_M(log n)` | `v_n c_M(log n)` | suma parcial |
|---|---|---|---|
| 2 | −9.765 | −9.572 | −9.572 |
| 3 | +6.066 | +7.695 | −1.877 |
| 4 | +0.2346 | +0.1626 | −1.715 |
| 5 | +3.7·10⁻³ | +5.3·10⁻³ | −1.7095 |
| 7 | +2.7·10⁻⁷ | +4.0·10⁻⁷ | −1.7095 |
| 8 | +1.6·10⁻⁹ | +8·10⁻¹⁰ | |
| 9 | +8.4·10⁻¹² | +6·10⁻¹² | |
| 11, 13, 16 | 10⁻¹⁶, 10⁻²¹, 10⁻²⁹ | | |

`P(M) := Σ v_n c_M(log n) ≈ −1.7095` (ROUND_019_A dio −1.698, cuadratura más gruesa), luego por `(R)`
`Arch_*(M) ≈ −1.71 < 0`. La identidad cierra en tres términos (2, 3, 4) a `10⁻²`; el resto es
doble-exponencialmente pequeño. El cierre es una cancelación `n = 2` contra `n = 3` con `Arch` negativo
(coherente con F2: `Arch` tiene direcciones negativas en `P_T`).

## §3 Controles

Para un peso `w`, el defecto en `M` es `δ(w) := Arch_*(M) − Σ w_n c_M(log n) = −Σ (w_n − v_n) c_M(log n)`
(PROVED, resta de `(R)`), y `a^w_T(X_T) = δ(w) + O(e^{cT}e^{−πe^{2T}})` (ROUND_019_A (3.1)).

- `cΛ`: `δ = (1−c)P(M) = (1−c)Arch_*(M)`; `c = 2`: `+1.71`. Es exactamente el patrón `A_RR(c) = (1−c)C` de
  LEMMA_I3_001 I.3-a, con `C` restringido a `span{M}`.
- Borrar `p^k`: `δ = v_{p^k} c_M(k log p)`: `p = 2`: `−9.57`; `p = 3`: `+7.69`; `4`: `+0.16`; cualquier `n ≥ 3`:
  positivo. Así, entre los borrados simples, sólo el de `2` hace de `X_T` un testigo negativo.
- Beurling (mover un generador `log 2 → u`): `δ` cambia en `v_2(c_M(log 2) − c_M(u))` más los cambios en
  potencias/productos; signo fijado por la posición de `u` respecto de `0.240`/`0.738`.

El paso que falla es siempre el mismo: `(R)`, es decir `M` deja de ser radical. El signo del defecto lo fija
el perfil del núcleo `c_M`, no la aritmética.

## §4 Qué da esto; qué se sabe

1. **Ya conocido (CITED).** `M` (y `K_Pó`, `K_Pó′`) en el radical de la forma completa: P46 Thm 11.11,
   R160_M4_R1 Teorema A/Lema 2(a), índice l.3537, l.5551. El escalamiento `(1−c)` del bloque radical:
   LEMMA_I3_001 I.3-a. La conclusión «la cercanía a cero de `X_T` es propiedad del radical, no del signo»:
   ROUND_019_A §3.
2. **`X_T` y el gauge `𝒢_T`.** `M` **no** es un elemento de `𝒢_T` (P47 l.9881): `𝒢_T` son funciones
   soportadas en `[−1/λ, 1/λ]` del lado multiplicativo cuyo transporte `Φ_φ` (Mellin `ζ(s)𝓜φ(s)`) se
   anula fuera de `(−∞, −T]`; su pertenencia al radical (Guo Lema 4.4) usa **sólo** `Λ∗1 = log`
   (rem:ext-killing (ii)) y el polo, **no** la ecuación funcional. `M` en cambio es divisible por `ξ`
   (R160 Teorema C: tasa máxima `e^{−πe^{2|t|}}` en el radical ξ-divisible), soportado en toda la recta, y
   su pertenencia al radical usa Euler + EF + Γ juntos. Ambos son subespacios del mismo radical de `𝒲`;
   son elementos distintos. (ARGUED: no comprobé si `M` es límite de gauges trasladados; la diferencia de
   identidades usadas sugiere que no.)
3. **Respuesta a la pregunta de O3/O12.** Sí: `X_T` es, en el corpus, el único vector **dentro de `P_T`** en el
   que Euler, EF y Γ entran en una sola identidad exacta (con error `e^{−πe^{2T}}`). (PC) de la fase 161 las
   tiene como identidad de operadores pero sin test en la ventana (ROUND_002_A §(4)); el gauge `𝒢_T` las
   tiene en un radical sin EF. Esto es un puntero, no un objeto: la identidad es **escalar en una dirección**.
4. **¿Descomposición `a_T(F) = (≥ 0) + (radical)` vía la imagen de `M`?** No. Las funciones del radical
   soportadas en la ventana son sólo casi-nulas (la cota B(i) es positiva solo como cota superior; un radical
   exacto en `P_T` daría `a_T = 0` exacto, excluido por P47 `cor:void`/`thm:finmod`, CITED). La «imagen de `M`
   restringida a la ventana» es, por traslaciones y cortes, una familia de vectores casi radicales de
   dimensión efectiva `O(T)` (106_09 Thms 2–3: matrices casi radicales de cortes de `K, K′, K″`), no densa
   en `P_T`; el complemento es todo `P_T` salvo esas direcciones, y sobre él la forma es la que hay que firmar.
   Escribir `F = (proyección sobre casi-radical) + resto` es la descomposición de Schur de LEMMA_I3_001 /
   `thm:parityschur`: ya hecha, sin signo. No propongo construcción: no pasa el filtro.

**Veredicto.** Todo ya está en el corpus salvo la tabla de `c_M` y el inventario «Euler + EF + Γ en un vector de
`P_T`, frente a sólo `Λ∗1` en `𝒢_T`». Salida: puntero (R160 Teor. A, P46 Thm 11.11, P47 prop:ext-gauge,
LEMMA_I3_001 I.3-a, ROUND_019_A §3). Sin ruta nueva; nada que añadir al índice salvo esta nota de cotejo.

**Para el revisor.** Re-derivar: (a) `A(M) = B(M) = 0` desde `Φ_M(0) = Φ_M(1) = 0`; (b) que `(R)` es la fórmula
explícita en `M ⋆ M` sin término polar y sin uso de ubicación de ceros; (c) los ceros de `c_M` en `0.240`,
`0.738` (cuadratura independiente); (d) la afirmación 2 de §4 (`M ∉ 𝒢_T` y qué identidades usa cada radical).
