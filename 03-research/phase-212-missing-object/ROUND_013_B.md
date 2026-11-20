# Ronda 13, memo B: el peso como caso de igualdad de una positividad (Gram, Schur, cuadrado completado)

## 0. Propuesta examinada

Las rondas 6–12 dejan una observación, sin rango de teorema. Los objetos con signo manifiesto no ven el peso:
el cuadrado de Sonin, el canal de cocientes `∫ĝ|A|²`, los cuadrados de fuga, las discrepancias reticulares y la
incertidumbre logarítmica. Los objetos que ven el peso no tienen signo: el canal de productos `∫ĝ Re A²`, el
conmutador de borde, la cola de hipérbola y la parte prima de Sonin. La única pieza que ve el peso exacto es
(PC) de R161_001 Teor. 3.1:

  `S_N A_M 𝓕 = {X,E_N} − L_M^*E_N − J H_{M,N} − H_{M,N}𝓕`,

y lo ve como una igualdad que se rompe (defecto interior `δ_a(k) = Σ_{d|k}a(d) − log k`).

La propuesta es combinar un objeto firmado y ciego con uno no firmado que vea el peso, de modo que el peso
entre como el **caso de igualdad** de una positividad. Formatos examinados:

- (a) Gram, Cauchy–Schwarz o complemento de Schur `[[Q1,B],[B*,Q2]] ⪰ 0`, con `Q1`, `Q2` ciegos y `B` portador
  del peso.
- (b) Cuadrado completado `‖u − Lv‖²`, con `L` el operador de von Mangoldt.
- (c) Interpolación en `c`, lema S y dualidad.

## 1. Cotejo hostil en primaria (antes de derivar)

| Formato | Antecedente más cercano (leído) | Resultado del cotejo |
|---|---|---|
| (a) Schur con bloque cruzado aritmético | **R170_861** §§0–1 (factorización (0.3)): si `A − D*G⁻¹D = H` con `G > 0`, la extensión es una congruencia triangular de `H ⊕ G`, y su positividad es la de `H`. La aplicación explícita es a `D ∈ {E, H_{M,N}, S(q)A(r), 𝒞_PC}`. Ver también `ANNEX_170_FILES_3.md` T1/T4 y `RULES_AVOID` I5. | Repetición literal: «colocar `H_{M,N}` en el bloque cruzado no crea energía». |
| (a) Cauchy–Schwarz con `Λ∗1 = log` | R170_841 §4.2 (`RULES_AVOID` I2): con la probabilidad `Λ(d)/log k` se obtiene `|β_Λ|² ≤ (log k)Σ_Λ`. | La cota es par y `β_Λ` es impar (`β(12) < 0`). Repetición. |
| (a) Versión invertida, determinante lorentziano | Fase 135 (transferencia de Hodge, condicional en `h⁰`); R160_C7_R1 §§5–6 (`RULES_AVOID` M1, N1). | La clase lorentziana se reduce al enunciado original (Prop. 6.2). |
| (a) Determinantes 2×2 de tipo Turán o Pfaffiano | POWER_RECIPROCAL_PFAFFIANS_083, POWER_FOUR_TURAN_084 (memoria de selecciones rechazadas, las reglas del proyecto). | El producto pfaffiano es negativo. Repetición. |
| (a) Gram de capas | POWER_GRAM_SLICES_OBSTRUCTION, ANNEX_211_GRAM_HYPERBOLIC (`RULES_AVOID` D16). | Gram de capas Λ-libres. Repetición. |
| (b) Cuadrado completado | R170_854 §6.3 (toda completación por cuadrados del corriente graduado es indefinida o da el canal de cocientes); R170_860–861 (congruencia); `RULES_AVOID` I5 (`Σ(Λ(n)/√n)‖F − U_nF‖²` deja una constante divergente); I2 (`γ = Λ log − Λ∗Λ` choca con Selberg, 850–851); Q3 / R161_034. | Repetición. |
| Término lineal de (a) y (b) | (OR) de R161_002 §2: `Re⟨R F, S_N𝓕F⟩ = ⟨A_M G, S_N^*S_N G⟩`. Su positividad sobre todo `L²` es el problema mismo. | L161.3 orientado sigue OPEN (`RULES_AVOID` U2). No lo cierra este formato (§2). |
| (c) | Interpolación `a_c` afín en el peso: ciega (`RULES_AVOID` B8, W-lin). Dualidad `Θ_T = max_c λ_A`: B10. Lema S: reformula el signo como existencia de un multiplicador (B3). Douglas: EQUIV (R161_002 §4). | Repetición. |

Los cotejos ya dan repetición en los tres formatos. Para que la detención sea precisa, y no sólo textual, el §2
prueba la razón común en el formato (a) más general.

## 2. Por qué el «caso de igualdad» no transporta signo

**Lema 1 (dicotomía del bloque; PROVED).** Sea `𝕳 = [[Q1, B],[B*, Q2]]` sobre `P_T ⊕ 𝒦`, con `Q2 ≥ g_0 > 0`, y
supongamos `Q1 − B Q2⁻¹ B* = a_T`.

- (i) Si la positividad de `𝕳` se prueba escribiendo `𝕳 = V*V` con `V = [u, v]` construido a partir de `F`,
  entonces `a_T(F) = ‖(1 − Π_v)u(F)‖²`, donde `Π_v` es la proyección sobre el rango de `v`.
- (ii) Si `𝕳 ⪰ 0` no se prueba así, entonces `𝕳 ⪰ 0` equivale a `a_T ⪰ 0` (R170_861 (0.3)).

*Prueba.* (ii) es (0.3). Para (i), el complemento de Schur de un Gram es el cuadrado del residuo de la
proyección ortogonal: `‖u‖² − ⟨u, v(v*v)⁻¹v*u⟩ = ‖(1 − Π_v)u‖²`. ∎

En el caso (i), el formato es una factorización `a_T = ‖w‖²` con `w = (1 − Π_v)u`. Es la factorización de
Douglas (EQUIV) salvo que `w` tenga fórmula propia, y su signo es el de un único cuadrado, válido para todo peso.

**Lema 2 (homogeneidad; PROVED).** Escribamos `u = u_0 + u_Λ`, con `u_0` libre de `Λ` y `u_Λ` lineal en el peso, y
supongamos `v` libre de `Λ`. Bajo `Λ ↦ cΛ`, el lado firmado vale `A_0 + 2cX + c²Y`, con
`Y = ‖(1 − Π_v)u_Λ‖²`. En cambio, `a_T(cΛ) = Arch − cP` es afín en `c`.

- La identidad para todo `c` exige `Y = 0`. Entonces `X = 0` y el peso desaparece.
- La identidad en `c = 1` sola exige `Y = Arch − P − A_0 − 2X`. El término cuadrático en el peso tiene que
  coincidir con una expresión lineal.

*Prueba.* Desarrollar el cuadrado. `Y = 0` implica `(1 − Π_v)u_Λ = 0`, y entonces el término cruzado se anula. ∎

Así, (a) con `B` afín se reduce a (b). Con `B` lineal es par en `Λ`: es el análogo del Teor. 1.1 de R161_002, y
la inversión global `Λ ↦ −Λ` deja el lado firmado igual.

**Lema 3 (el término cuadrático es el canal de cocientes; PROVED).** Para `L_M = Σ_{d≤M} Λ(d) d^{−1/2} τ_{log d}`:

- el coeficiente de `τ_{log(a/b)}` en `L_M^*L_M`, con `gcd(a,b) = 1` y `a, b > 1`, es `Λ(a)Λ(b)/√(ab)` (con
  `a, b ≤ M`);
- el coeficiente en `r = 1` es `Σ_{n≤M} Λ(n)²/n`, que diverge como `½ log² M`.

*Prueba.* Hay que tener `ak` y `bk` potencias de primos con `a`, `b` coprimos. Si `k > 1`, entonces `k = p^i` y
`a`, `b` serían potencias de `p`, contra la coprimalidad. Luego `k = 1`. ∎

Por lo tanto, el término `L*L` de (b) no contiene ninguna suma de divisores `Σ_{d|k}Λ(d)`. La relación
`Λ∗1 = log` gobierna los productos `L S_N`, es decir el soporte de `H_{M,N}`, y no los cocientes. La premisa de
(b), «identificar `L*L` aplicando `Λ∗1 = log` dos veces», es falsa. Lo que aparece es el canal de cocientes de Q3
con la constante divergente de I5.

**Controles (regla R3-i).**

- **Con `c = 2`.** `‖(1 − Π_v)u‖² ≥ 0` sigue valiendo, porque es un cuadrado de vectores para todo peso. Si la
  batería E (CITED) da una dirección negativa de `a_T(2Λ)`, lo que falla es la igualdad.
- **Con el borrado de una potencia de primo.** Mismo caso: el cuadrado es indiferente.
- **Con Beurling.** `L*L` y el cuadrado siguen definidos; sólo falta `E_N`, que no entra en el lado firmado.

Ningún paso firmado nombrado deja de ser `≥ 0` bajo estos controles: el lado firmado es ciego por construcción.
**Corrección de alcance:** esto no excluye una prueba para Λ. Puede fallar únicamente la identificación
con a_T en el control. Un Gram con fórmula propia e identificación exacta demostrada sin suponer el
signo objetivo sería un certificado válido. Sólo se transfiere positividad al falsificador cuando
sobrevive toda la cadena de igualdad y desigualdad, incluidos los términos adicionales.
En la rama (ii), el único paso firmado es la propia `a_T ⪰ 0`. Para invertir el bloque hace falta `Q2⁻¹`. Si
`Q2` contiene la forma, es J3; si `Q2` es Λ-libre, se cae en (i) o en la congruencia de R170_861.

**Pruebas de R161_002 §6.** Formalmente no se aplican, porque ninguna variante pasa la puerta. En el formato (b):

- La prueba de inversión de `Λ(2)` cambia `Y` en los cocientes `2/q`, de orden cuadrático. No cambia el
  defecto interior `−2 log 2` en `k = 2`, que vive en los productos.
- La prueba de dos puntos exige el coeficiente lineal `2 log 2/√2`, que sólo aporta `X`, el apareamiento (OR).

## 3. Veredicto

- **Formatos concretos examinados: repetición, sin candidata nueva.** Se retira la exclusión general de
  toda identidad Gram, de Schur o de cuadrado completado con lado positivo definido para todo peso.
  Los Lemas 1(i)–(ii) no excluyen una construcción independiente ni una identidad específica de Λ.
  En el operador L_M concreto del Lema 3, el término cuadrático en `Λ` es
  el canal de cocientes, donde `Λ∗1 = log` no actúa (Lema 3). Patrones B3, B9 y J3.
- **Etiquetas.** Lemas 1–3: PROVED. Antecedentes R170_841, R170_854, R170_861, R160_C7_R1, R161_002 y los memos
  083/084: CITED. Ruptura bajo `c = 2` sólo en la igualdad: PROVED, condicionado a la batería E (CITED). Signo
  global de `a_T`: OPEN.
- **Operación que reabriría la clase.** Un `𝕳 ⪰ 0`, Gram o no presentado como Gram, de fórmula propia y con
  positividad demostrada independientemente, junto con la identidad completa de su Schur con a_Λ.
  Bajo `c = 2` puede fallar esa identidad; no se exige que falle la positividad del bloque. El único
  candidato de fuente conocido es la clase infinitamente divisible o de Pick (`RULES_AVOID` M4, ARGUED), y falta
  un `𝕳` explícito. No lo propongo.
