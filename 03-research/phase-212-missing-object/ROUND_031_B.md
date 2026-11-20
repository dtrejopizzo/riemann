# Ronda 031 B — Primitividad como cota cuantitativa y generación del bloque negativo por traslaciones en log ℕ

Objeto: `a^w_T(F) = Arch(F) − Σ_{n≥2} w_n c_F(log n)` sobre `P_T = {F ∈ L²(−T,T) : ∫F e^{±t/2} = 0}`
(P47 `eq:form`, `thm:A`, `rem:Kprim`; matrices de Galerkin de `free_weight_scripts/forms.py`, auditado contra
el paper). (PBP_T): `Tr(ρ·Arch) ≥ 0` para todo estado `ρ` sobre `P_T` con `Tr(ρ C_n) = 0`, `2 ≤ n < e^{2T}`,
donde `C_n` es la forma `F ↦ c_F(log n)`. Script: `free_weight_scripts/block_span_031B.py`.

## Cotejo (filtro de cuatro puntos)

1. **Antecedente más cercano.** (a) Fase 204 (índice, l. 9330): en `E_N`, `N ≈ 4T`, la positividad par se
   reduce a la inercia de una matriz explícita Toeplitz−Hankel; «el peine cancela todas las direcciones
   negativas salvo una». (b) P211-11B, `ROUND_011_B` (índice, l. 6432): ensamblaje de Schur en dos bloques
   bajo/alto, NO-GO NUMÉRICO («do not retry two-block LM/HI Schur … K-uniform»). (c) R160_M2_R1 Thm 4.1
   (dualidad fuerte: (PBP_T) ⟺ existe peso libre `w` con `a^w_T ⪰ 0`) y 212-26-A (`V*_T > 0` NUMÉRICO).
   (d) 212-30-B (la primitividad no se convirtió en cota; condición de reapertura: desigualdad de tipo
   Paley–Wiener con el tipo y los ceros en `±i/2`). (e) I6 (índice, l. 4823/4889): cota de dimensión del
   bloque negativo desde datos aritméticos, ABIERTO. `ROUND_031_A.md` no existía al empezar.
2. **Qué sería nuevo.** (i) Valor cuantitativo exacto de la primitividad (paso 1). (ii) La lectura del lado
   estado: «las `C_n` comprimidas generan las simétricas del bloque» como mecanismo de anulación de `ρ` en
   el bloque, y su comparación con sistemas sin `log ℕ` (paso 2).
3. **Por qué evitaría el antecedente.** (b) trabaja con la forma `a_T` del peso verdadero; aquí el peso es
   libre y se mide sólo la geometría de la familia `{C_n}` en el bloque (rango y condicionamiento).
4. **Conexión global.** Dualidad débil (PROVED, una línea): si `a^w_T ⪰ 0` para algún `w` y `ρ` es
   admisible, `Tr(ρ Arch) = Tr(ρ a^w_T) ≥ 0`. Luego cualquier `w` construido desde la generación del bloque
   da (PBP_T), y de ahí sólo CONDITIONAL a la rigidez 212-30-A.

Resultado adelantado: (1) cota PROVED y óptima, que vale exactamente dos direcciones; (2) la generación del
bloque se cumple con pocos `n`, también con los `n` impares, así que no es propiedad del retículo; el
mecanismo se reduce a un ensamblaje de Schur bajo/complemento con condicionamiento que decae deprisa:
NO-GO de selección por repetición de (b) y (c).

## 1. Problema modelo sin peine: cuánto vale la primitividad

**1.1 Núcleos.** Con `F̂(τ) = ∫F(t)e^{iτt}dt`, `F̂ ∈ PW_T` y el núcleo reproductor
`k_z(τ) = sin(T(τ − z̄))/(π(τ − z̄))`. Las condiciones de `P_T` son `F̂(±i/2) = 0`, es decir `F ⊥ e^{±t/2}`:
`‖k_{±i/2}‖² = sinh T/π`, `⟨k_{i/2}, k_{−i/2}⟩ = T/π`; independientes para todo `T > 0` (Gram
`(sinh²T − T²)/π² > 0`). `P_T` es de codimensión 2 en `L²(−T,T)`, invariante por `t ↦ −t`, con una
condición par (`cosh(t/2)`) y una impar (`sinh(t/2)`).

**1.2 Proposición (PROVED; min–max de Courant–Fischer).** Sean `λ_1 ≤ λ_2 ≤ …` los autovalores de Arch en
`L²(−T,T)` y `λ_k^P` los de Arch en `P_T`. Entonces `λ_k ≤ λ_k^P ≤ λ_{k+2}`; por paridad, separadamente
`λ_k^{ev} ≤ λ_k^{ev,P} ≤ λ_{k+1}^{ev}` y lo mismo en el sector impar. En particular
`n_−(Arch|P_T) ≥ n_−(Arch|L²) − 2` y `λ_1^P ≤ λ_3`.
La primitividad vale, como cota de índice, a lo sumo **dos direcciones** (una par, una impar) en todo `T`.

**1.3 Régimen (ARGUED con concentración de Landau–Widom CITED).** El número de direcciones de baja
frecuencia en `|τ| ≤ τ* = 6.2898` es el número de Shannon `(2T)(2τ*)/2π = 2Tτ*/π ≈ 4.00·T`; como
`m(τ) < 0` sólo allí, `n_−(Arch|L²) ≈ 4T + O(log T)` y `λ_1, λ_3 → m(0) = −5.372` cuando `T → ∞`
(los primeros prolatos concentran su masa en `|τ| ≪ 1`). Así:
- `T ≲ 0.6`: las dos condiciones son todo el bloque bajo; la primitividad lo cierra (P47 `thm:index`:
  `λ^P > 0` para `T ≤ 0.58`). Es el único régimen donde decide el signo.
- `T` grande: quita 2 de `≈ 4T` direcciones y el autovalor mínimo en `P_T` tiende a `m(0)`: la
  ganancia en la cota inferior de `∫m dμ` es `o(1)`. No hay cota de «masa en baja frecuencia» mejor que
  la del prolato, salvo las dos dimensiones.

**1.4 NUMÉRICO** (Legendre `N = 24–40`, cuadratura 240; los valores de `P_T` reproducen `thm:index`):

| T | `n_−` en L² | 3 menores en L² | `n_−` en P_T | 3 menores en P_T |
|---|---|---|---|---|
| 0.6 | 2 | −1.946, −0.473, 0.031 | 1 | −0.007, 0.293, 0.613 |
| 0.9 | 4 | −2.471, −0.900, −0.377 | 2 | −0.424, −0.116, 0.205 |
| 1.2 | 5 | −2.863, −1.222, −0.668 | 3 | −0.732, −0.408, −0.087 |
| 1.6 | 6 | −3.265, −1.573, −0.966 | 4 | −1.066, −0.706, −0.384 |

La caída del índice es exactamente 2 en los cuatro casos: la cota 1.2 se alcanza. `λ_1^P` queda entre
`λ_2` y `λ_3` del espacio completo. **Consecuencia:** la condición de reapertura de 212-30-B («Paley–Wiener
con los ceros en `±i/2`») tiene respuesta cerrada: lo máximo que dan los ceros es la Prop. 1.2, y para el
déficit `1.498` de 212-30-B, que vive en `π/log 2 < |τ| < 6.29`, aportan `o(1)` cuando `T → ∞`.

## 2. Las condiciones Φ(log n) = 0 sobre el bloque negativo

**2.1 Planteo preciso.** Sean `B` el autoespacio de Arch|P_T con autovalores `< 0` (dim `d`), `C` su
complemento en `P_T` (Arch ≥ `γ ≥ 0` en `C`). Un estado `ρ ⪰ 0`, `Tr ρ = 1`, se escribe en bloques
`ρ_BB, ρ_BC, ρ_CC`, y `Tr(ρ C_n) = Tr(ρ_BB C_n^{BB}) + 2 Tr(ρ_BC C_n^{CB}) + Tr(ρ_CC C_n^{CC})`.

**2.2 Corrección del conteo propuesto.** «Si las `C_n^{BB}` generan las simétricas del bloque, `Tr(ρC_n)=0`
fuerza `ρ_BB = 0`» es falso: las condiciones acoplan `ρ_BB` con `ρ_BC` y `ρ_CC`, y `C` tiene dimensión
infinita, de modo que el cociente «condiciones / dimensión» no tiene sentido sobre el portador completo.
Además (PROVED) Arch y todas las `C_n` conmutan con `t ↦ −t` (simetrización de `c_F`) y `P_T` es
invariante: las `C_n^{BB}` sólo pueden generar las matrices **par-diagonales** del bloque, de dimensión
`d_e(d_e+1)/2 + d_o(d_o+1)/2`; la parte par–impar de `ρ` es invisible para Arch y para las condiciones.

**2.3 Enunciado correcto (PROVED, elemental).** Si existe `w` real con
(a) `Arch^{BB} − Σ w_n C_n^{BB} ⪰ α`, (b) `Arch^{CC} − Σ w_n C_n^{CC} ⪰ β`, (c) `‖Σ w_n C_n^{BC}‖² ≤ αβ`,
con `α, β > 0`, entonces `a^w_T ⪰ 0` y (PBP_T) vale en ese `T` (Schur + dualidad débil). Como `|c_F(u)| ≤ ‖F‖²`,
`‖C_n‖ ≤ 1` y (b)–(c) se siguen de `‖w‖_1 ≤ γ − β` y `‖w‖_1² ≤ αβ`. Si las `C_n^{BB}` generan las
par-diagonales con menor valor singular no nulo `σ_min`, el `w` de norma mínima que resuelve
`Σ w_n C_n^{BB} = Arch^{BB} − αI` cumple `‖w‖_2 ≤ ‖Arch^{BB} − αI‖_F/σ_min`. Luego
`(PBP_T) ⟸ [generación par-diagonal] + [‖Arch^{BB}−αI‖_F·√(#n)/σ_min ≤ mín(γ − β, √(αβ))]`.
Es exactamente un ensamblaje de Schur bajo/complemento con peso libre: por la dualidad fuerte (antecedente c)
es una condición suficiente para el problema de 212-26-A, no un mecanismo nuevo para el signo.

## 3. Comprobación numérica (T = 0.9, 1.2, 1.6; con todos los n y sólo con los impares)

| T | `d` (par, impar) | #n (impares) | rango | `σ_min` no nulo todos / impares | `‖w‖_1` mín. norma | λ_min(a^w_T) |
|---|---|---|---|---|---|---|
| 0.6 | 1 (1,0) | 2 (1) | 1 = 1 | 0.199 / 0.075 | 0.37 / 0.76 | **+0.034 / +0.037** |
| 0.9 | 2 (1,1) | 5 (2) | 2 = 2 | 0.365 / 0.076 | 1.37 / 8.3 | **+0.008** / −2.03 |
| 1.2 | 3 (2,1) | 10 (5) | 4 = 4 | 0.014 / 0.0058 | 5.4 / 24.7 | −0.82 / −6.67 |
| 1.6 | 4 (2,2) | 23 (11) | 6 = 6 | 0.0013 / 0.00038 | 14.7 / 16.9 | −4.21 / −3.96 |

(`α = 0.05`; el rango iguala siempre la dimensión par-diagonal; el bloque `BB` queda en `0.05` por
construcción y el fallo está todo en `CC`, que antes del peso tenía mínimo `0.205, 0.100, 0.001`.)
Lecturas (NUMÉRICO):
- La generación del bloque se cumple ya con los primeros `n` y **también sin los múltiplos de 2**: no
  distingue `log ℕ` de los impares (ni, por el mismo motivo, de un sistema tipo Beurling con
  `≥ d(d+1)/2` traslaciones genéricas). La «totalidad» buscada es genérica.
- `σ_min` cae `0.365 → 0.014 → 0.0013` entre `T = 0.9` y `1.6` (≈ un factor 10 cada 0.4 en `T`), y el
  `w` que cancela el bloque destruye el complemento desde `T = 1.2`. El `w` de norma mínima no es el óptimo
  (212-26-A obtiene `V*_T > 0` con SDP), pero esto muestra que la generación sin control del acople no da
  nada: toda la información está en (b)–(c), que es el acople bajo/alto ya registrado (antecedente b).
- El número de condiciones (`≈ e^{2T}`) frente a `d(d+1)/2 ≈ 8T²` no entra: el rango satura en la
  dimensión par-diagonal con muy pocos `n`, y el resto de las condiciones sólo mejora el condicionamiento,
  sin estructura propia de `log ℕ` visible en estos `T`.

## 4. Veredicto

- **PROVED:** Prop. 1.2 (la primitividad vale a lo sumo 2 en el índice y `λ_1 ≤ λ_1^P ≤ λ_3`), óptima
  (NUMÉRICO: se alcanza en `T = 0.6–1.6`); paridad de la familia (2.2); criterio suficiente de Schur (2.3).
- **ARGUED:** la ganancia en `ínf ∫m dμ` es `o(1)` para `T → ∞` (concentración prolata); la primitividad
  no ayuda a recuperar el déficit `1.498` de 212-30-B.
- **NO-GO de selección (paso 2):** «las `C_n` comprimidas generan el bloque negativo» es una reformulación
  del dual de peso libre (R160 Thm 4.1 / 212-26-A) en forma de Schur bajo/complemento (P211-11B). La
  generación es genérica (vale con impares) y no usa el retículo; la dificultad entera es el acople con el
  complemento, cuyo condicionamiento `σ_min` decae deprisa en `T`.
- **Cuánto falta y dónde:** para (PBP_T) en `T ≥ 1.2` haría falta un `w` con `‖Σ w_n C_n^{CC}‖ ≤ γ(T)`
  (`γ(1.6) ≈ 0.001`) y a la vez cancelación del bloque, cuyo coste en `‖w‖` crece como `1/σ_min`. Ningún
  argumento de conteo da eso; tendría que salir de una estructura de `log ℕ` que distinga los enteros de
  los impares en el acople `C_n^{BC}`, `C_n^{CC}`, no en el bloque.
- **Condición de reapertura:** una cota de `‖Σ w_n C_n^{CC}‖` para el `w` que cancela el bloque, mejor
  que `‖w‖_1`, que use la aritmética (y falle con los impares o con Beurling).

Registro sugerido para la Parte V del índice (no editado aquí): «212-31-B — Primitividad cuantitativa y
generación del bloque negativo por `{C_n}`: Prop. de entrelazamiento PROVED (vale 2 direcciones); generación
genérica (vale sin múltiplos de 2) NUMÉRICO; NO-GO de selección por reducción a Schur bajo/complemento
con peso libre; detalle en ROUND_031_B.md, `free_weight_scripts/block_span_031B.py`.»
