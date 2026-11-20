# Ronda 13 A — Ingeniería inversa en pequeño: la ventana ½log 4 < T < ½log 5

Idea examinada: en la ventana `½log 4 < T < ½log 5` los contactos son `n = 2, 3, 4`; la forma con peso `cΛ` es
positiva sólo en una banda estrecha de `c` alrededor de 1; buscar la *razón* (identidad exacta
«`a_T` = expresión manifiestamente no negativa») que use `c = 1`, `Λ(4) = Λ(2)`, `log 4 = 2 log 2` y
`Σ_{d|n}Λ(d) = log n` para `n ≤ 4`, con forma enunciable para todo `T`.

Veredicto: **REPETICIÓN**. Se detiene antes de derivar. Abajo, el cotejo y la única observación nueva (de
selección, no de signo).

## 1. Cotejo en primaria: qué hay en la ventana y qué es mecanismo

| Pieza | Archivo / sección | Tipo | Dónde se detiene |
|---|---|---|---|
| `thm:log5A`, `thm:log5W` (positividad hasta `½log 5`) | Paper 47 `main.tex` l. 4680–4710; apéndice `subsec:encllog5` | **certificado** (ball arithmetic, `prop:lowercert`, `thm:parityschur`) | no explica nada; cota `2.5·10⁻¹²` |
| `thm:C` (certificado explícito, `½log 3`) y Teorema C de la fase 154 | Paper 47 `thm:C`; fase 154 | certificado; «sólo forma primitiva» (fase 155, ronda 5) | primer contacto |
| Teorema A de la fase 153 (`({∞,2,3}, log 2)`) | fase 153 | mecanismo parcial (energía de Lévy, `thm:A`) | `T ≤ log 2`, sin `n = 4` |
| `prop:align` (estructura de alineación con 2 y 3 contactos; con 4: `g(x) = v_2 cos x + v_4 cos 2x`, raíz `y_0`) | Paper 47 `main_pre_cite46.tex` l. 2896 | **mecanismo de localización** del conjunto `{σ < 0}` (usa `log 4 = 2 log 2`) | localiza la parte negativa; no da signo (`prop:negtrace`: «la banda no decide») |
| Explicación nodal de la cancelación 2/3 | fase 155 ronda 5 | lectura estructural | sin desigualdad |
| Reducción de Schur, `S_{T,k}` (`λ_A > 0 ⟺ S_{T,k} ≻ 0`) | Paper 47 l. 211; fase 186 R186_025/105 | reducción exacta a dimensión finita | el signo de `S_{T,k}` es un certificado |
| Reparto por primo de la ronda 6 (cuadrado de rango uno `ℓ ≈ cos(2πt/log 2)` proyectado) | `ROUND_006_WINDOW_SPLIT_NUMERIC.md`; RULES_AVOID O1–O4 | NUMÉRICO; muere en `T = 0.70` | genérico en `c` hasta 0.69 |
| Banda en `c`, concavidad, `c* < 1` estricto, derivada `−Π(F*)` | `ROUND_006…` §10.3–10.4; 211 `ROUND_003_A.md` Prop. 2; RULES_AVOID P1 | PROVED estructural | sin signo |
| Pin de Weyl: `|1 − c*| ≤ (Λ_2 − λ_A)/min|μ_±|` | 211 `ROUND_003_A.md` Lema 3 (instancia en `½log 5 + 10⁻³`: `2·10⁻⁶`) | PROVED estructural | entradas (P1)–(P2) tan fuertes como el signo |
| **Identidad `Λ∗1 = log` en la celda**: `P_w𝔇_R = [M_x, 𝔇_R] ⟺ w ≡ 1` en potencias de primo `< R`; `Q_R^{(c)} = Q₀ − c𝒦_R` con `Q₀, 𝒦_R` libres de `Λ` | 211 `ROUND_021_A.md` Prop. 3.2 | PROVED | la ventana pedida es exactamente `R = 5`; el mecanismo sobrevive a Beurling (§3.4(ii)(c)) |
| Sándwich: ancho de la banda en `c` ≍ fondo `λ₀` | 211 `ROUND_021_A.md` Lema 3.3 | PROVED | la banda *es* el margen en otra variable |
| Controles pedidos (sólo `n = 2`, potencias de 2 — incluye `Λ(4)` —, potencias de 3, borrados `a_3`, `a_5`) | 211 `ROUND_021_A.md` §2.3, fila `R = 5` | NUMÉRICO | ya medidos |

## 2. Filtro de cuatro puntos (hostil)

1. **Antecedente más cercano.** 211 `ROUND_021_A.md` Prop. 3.2 + Lema 3.3 en `R = 5`, con 211 `ROUND_003_A.md`
   Prop. 2 y Lema 3. Ambos leídos en primaria.
2. **Objeto nuevo.** Ninguno. Cada subpregunta del encargo tiene respuesta registrada:
   - *qué degenera en `c*`*: Danskin, `0 ∈ conv Π(E_T)` en el fondo de `a_T^{(c*)}` (003_A Prop. 2); es una
     tangencia de codimensión uno, no un cuadrado que falte;
   - *por qué `c* → 1`*: pin de Weyl (003_A Lema 3) y sándwich (021_A Lema 3.3): `|1 − c*|` y el ancho de la
     banda son el margen salvo constantes;
   - *papel de `Λ(4) = Λ(2)`, `log 4 = 2 log 2`, `Σ_{d|n}Λ(d) = log n` para `n ≤ 4`*: es exactamente la Prop. 3.2 en
     `R = 5`; su efecto es **eliminar** `Λ` de la forma, no producir un signo, y vale para todo sistema de enteros
     generalizados con su propio `Λ_N`;
   - *controles*: 021_A §2.3.
3. **Por qué evitaría la dificultad.** No la evita: la dificultad registrada (021_A §3.4(i)) es que tras usar la
   identidad no queda resto; el signo es el de `Q₀ − 𝒦_R` en `V_R`, con fondo `≈ 6·10⁻⁹` en `R = 5`. Una «prueba
   estructural en la ventana» tiene que probar ese fondo, es decir, un certificado de orden finito (prohibido
   acumular) o un mecanismo para `Q₀ − 𝒦_R` que nadie ha dado.
4. **Conexión con la positividad global.** Ninguna enunciada: la versión «para todo `T`» de la identidad es la
   Prop. 3.2 para todo `R`, ya registrada y ciega a Beurling.

Patrones de RULES_AVOID: P1 (subespacio casi nulo y tangencia), S2 (paso que usa sólo divisores no falla bajo
Beurling), B3/B9. Se detiene aquí.

## 3. Observación de selección (lo único que esta ronda añade)

**Lema S (PROVED, a partir de 021_A Lema 1.1 y Lema 3.3).** Sea `T` en la ventana y `λ₀ > 0` el fondo de la forma
de la celda con `c = 1`. Entonces el conjunto `J` de `c` con forma `⪰ 0` es un intervalo cerrado que contiene
`[1 − λ₀/‖𝒦‖, 1 + λ₀/‖𝒦‖]`. *Prueba:* Lema 3.3, cota inferior. ∎

**Consecuencia (PROVED).** La premisa «toda prueba estructural está forzada a usar el valor exacto `c = 1`» es falsa
en sentido estricto: la positividad en `c = 1` implica positividad en un entorno abierto de 1, y además el máximo del
fondo está en `c* < 1` estricto (003_A Prop. 2 con `Π(e) > 0`, NUMÉRICO en el signo de `Π(e)`). Ninguna propiedad
cualitativa de la forma distingue `c = 1` de los `c` vecinos; lo que se exige es *precisión cuantitativa*
`|c − 1| ≲ λ₀`, es decir, el margen. Por tanto una identidad «forma = SOS» que se rompa exactamente en `c ≠ 1`
(caso automático de R3-i) no puede ser la razón del signo; a lo sumo una reescritura en la que el resto conserva
un margen `≍ λ₀`.

**Consecuencia para la idea (ARGUED).** La «razón en pequeño» buscada es, en esta ventana, el signo de la forma
libre de `Λ`, `Q₀ − 𝒦_5`; un mecanismo para ella tendría que usar algo de `ℕ` que Beurling no tenga (la estructura
aditiva de `{1,2,3,4}`: `4 = 2·2 = 1 + 3`, `3 = 1 + 2`) y no sólo la convolución de Dirichlet. Esto es la
exigencia S2 ya registrada; no hay operación explícita nueva.

## 4. Resultado

- Veredicto: **REPETICIÓN** de 211 `ROUND_021_A.md` (Prop. 3.2, Lema 3.3, §2.3 en `R = 5`) y 211 `ROUND_003_A.md`
  (Prop. 2, Lemas 3–4); la positividad en la ventana es certificado (`thm:log5A`), no mecanismo.
- PROVED: Lema S y su consecuencia (`c = 1` no está cualitativamente distinguido; sólo cuantitativamente, por el
  margen). Todo lo demás es CITED de los antecedentes.
- ARGUED: que la única «razón» posible en la ventana sea un mecanismo para `Q₀ − 𝒦_5` que acople la estructura
  aditiva de `{1,…,4}`.
- No se construyó nada; no se hizo cómputo.
- Siguiente operación explícita: ninguna defendible desde esta idea. El paso pendiente de 021_A («comparar la
  dirección casi nula de `Q₀ − 𝒦_R` con la preimagen por `𝔇_R` del fondo de la forma de ventana») es estructural y
  ciego a Beurling; no habilita construcción sin un ingrediente aditivo nombrado.
