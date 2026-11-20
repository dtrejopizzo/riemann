# Ronda 14, A — linealizar el canal de cocientes: independencia de los primos, polarización y transporte desde el canal de productos

Notación del brief común y de `ROUND_013_C.md`. Para un peso real `w = (w_n)` se escribe `A_w(ξ) = Σ w_n n^{−1/2} n^{iξ}`,
`ĝ = |F̂|⁴ ≥ 0`, `Q(w) = ∫ĝ|A_w|²` (canal de cocientes, coeficiente `w_a w_b/√(ab)` en el retardo `log(a/b)`),
`P(w) = ∫ĝ Re A_w²` (canal de productos). Controles `𝒞 = {2Λ, Λ con una potencia de primo borrada, Beurling}`.

**Resultado.** Ninguna candidata pasa la puerta. Se prueban tres lemas de clase: la linealización existe siempre y es
la polarización, cuyo resto es ciego al peso o cuya parte afín es circular (Lema P). La independencia de los primos,
por factorización única, impide que una suma de traslaciones con coeficientes ciegos lleve el canal de productos al de
cocientes (Lema U). El canal de cocientes no se obtiene como canal de productos de otro objeto con una identidad de
Dirichlet que siga siendo exacta (Lema Q). (ii) y (iii) se reducen a R161_034/035 y a I2/I5. No queda operación nueva
con objeto escrito.

Lectura en primaria: RULES_AVOID §§I (I2, I5), Q (R7-c), R (R1, R2), S–W; ROUND_013_B §§0–1; ROUND_013_C §§0–1;
ROUND_010_A (a través de RULES_AVOID T2). Para las fases 106, 161 y 170 la lectura es la de los anexos por archivo
`ANNEX_161_FILES_1–3.md` y `ANNEX_170_FILES_3.md`, que contienen R170_841, 851, 854, 856 y 860–861, además del índice
`ROUTES-TRIED-INDEX/README.md` (INV_E, INV_F, INV_I, INV_J, BB_001). Esta lectura es indirecta, y no se releyeron
enteros R161_034/035 ni 106_109.

## 0. Filtro de cuatro puntos

1. **Antecedente más cercano.** ROUND_013 (RULES_AVOID W3): el término cuadrático vive en el canal de cocientes, y
   allí `Λ∗1 = log` no actúa. R161_034 y RULES_AVOID Q3 (R7-c): el canal de cocientes no ve la aritmética y el de
   productos no tiene signo. RULES_AVOID R1: el concomitante de borde producto→cociente está cerrado (R161_035,
   057–065). I2: `γ = Λ log − Λ∗Λ` choca con Selberg (R170_851). I5: `Σ(Λ(n)/√n)‖F − U_nF‖²` da una constante
   divergente, y completar el cuadrado `D*G⁻¹D` es congruencia pura (R170_860–861). INV_J_001 (índice): las
   correlaciones aditivas `Λ(n)Λ(n+h)`, la gran criba y la correlación de pares están cerradas por J3 (H_sparse).
2. **Afirmación nueva.** No hay objeto nuevo. Lo nuevo son tres enunciados de clase (Lemas P, U y Q), que dicen por
   qué el canal de cocientes no admite una linealización exacta con contenido.
3. **Por qué evitaría la dificultad.** No la evita, la localiza. La observación del encargo (independencia de los
   primos) se usa, pero **en contra** del transporte: es precisamente lo que impide la cancelación de los términos
   espurios (Lema U).
4. **Enlace global.** Ninguno. En la única clase donde la identidad existe (Lema P, (a)), su existencia equivale a
   `a_T ≥ 0`.

La puerta no se pasa. El resto del memo prueba los cierres de clase, como pide el punto 3 del encargo.

## 1. Lema P (polarización): la linealización existe siempre y no tiene contenido

**Lema P.** Sea `u_w` afín en `w` y sea `Q(w) = ‖L w‖²` su parte cuadrática, con `L` lineal.
(a) Para todo peso fijo `B` vale `Q(w) = 2⟨Lw, LB⟩ − ‖LB‖² + ‖L(w − B)‖²`, para **todo** `w`. Por lo tanto «lineal en
    el peso + resto ≥ 0» existe siempre: el resto es `≥ 0` para todo peso de `𝒞` (ciego) y es nulo sólo en `w = B`.
(b) Si `R(w)` es un resto manifiestamente no negativo, es decir `R(w) = ‖Vw + v_0‖²` con `V`, `v_0` independientes de
    `w`, y `Q − R` es afín, entonces `V*V = L*L`, luego `V = UL` con `U` una isometría parcial sobre `Ran L`, y `R ≥ 0`
    vale para todo peso. El resto es ciego (patrones B3/B9).
(c) Si `u_0` puede contener la función aritmética `Λ` como dato fijo (es decir `B = Λ`), una identidad
    `a_T(F) = ‖u_0(F) + u_Λ(F)‖²` existe si y sólo si `a_T ≥ 0` en `P_T`: basta tomar `u_0 = a_T^{1/2}F − u_Λ`.
    Es J3 (circular).

*Prueba.* (a) es el desarrollo del cuadrado. (b): se igualan las partes cuadráticas y se aplica la factorización de
Douglas (RULES_AVOID W2). (c): una dirección es inmediata y la otra es la raíz cuadrada de un operador positivo. ∎
PROVED.

**Consecuencia.** La distinción «peso / sin peso» es formal mientras `u_0` pueda codificar valores de `Λ`. Bajo cada
control de `𝒞` lo que se rompe en (a) es la **igualdad** con la forma, no el signo del resto: el resto sigue siendo
`‖L(w − Λ)‖² ≥ 0`. Por la regla R3-i, esto no es una razón del signo. Para `c = 2`, además, W1 muestra que romperse
en `c ≠ 1` no tiene valor probatorio.

## 2. Lema U (independencia de los primos contra el transporte producto→cociente)

Clase `𝒯`: operadores sobre medidas en el eje de retardos de la forma `𝒮 = Σ_j γ_j τ_{β_j} J^{ε_j}`, con
`ε_j ∈ {0,1}`, coeficientes `γ_j` y desplazamientos `β_j` reales **sin peso** (no dependen de `w`), la familia
posiblemente infinita, aplicados a la medida de productos `μ_×(w) = Σ_N (w∗w)(N) N^{−1/2} δ_{log N}`. Se pide
`𝒮μ_×(Λ) = μ_÷^{off}(Λ) + (lineal en Λ)`, con `μ_÷^{off} = Σ_{a≠b, (a,b)=1} Λ(a)Λ(b)(ab)^{−1/2} δ_{log(a/b)}`.

**Lema U.** Ningún `𝒮 ∈ 𝒯` realiza esto. Sea `N = pq` con `p ≠ q` primos. Si `𝒮` lleva la masa de `log(pq)` a
`±log(p/q)`, entonces existen `j` con `β_j = −2 log p` o `β_j = −2 log q` (para `ε_j = 0`; con `J` es simétrico).
Esos mismos `j` llevan la masa `(Λ∗Λ)(p'q)` a `log(p'q/p²)` para todo primo `p' ≠ p, q`. Por factorización única,
`p'q/p²` es un cociente coprimo `a/b` con `b = p²` y `a = p'q`, compuesto con dos factores primos distintos, de modo
que `Λ(a) = 0` y el coeficiente de cocientes en ese punto es nulo. Además ningún otro par `(N', j')` aterriza en el
mismo punto con masa que lo cancele: la masa de productos de `Λ` sólo vive en `N'` con a lo sumo dos factores primos,
y `N' e^{β_{j'}} = p'q/p²` con `β_{j'}` otro desplazamiento de la misma forma `±2 log r`, o con otro `β`, fija `N'`
por factorización única salvo si `j' = j`. Para que el término espurio sea «lineal en Λ» haría falta que
`(Λ∗Λ)(p'q) = 2 log p' log q` fuera lineal en `Λ` con coeficientes sin peso para todos los `p'`, lo cual es de nuevo
el problema de partida. ∎
PROVED para `𝒯` con desplazamientos de la forma `±2 log r` y para combinaciones finitas arbitrarias (un número finito
de `β_j` no alcanza los infinitos retardos `log(p/q)`). ARGUED para familias infinitas con `β_j` arbitrarios: falta
escribir el control de la sumabilidad.

**Lectura.** La observación del encargo es correcta (la aplicación `(a,b) ↦ a/b` es inyectiva sobre los pares
coprimos, y `ab ↦ {a,b}` lo es también para `ab` libre de cuadrados con dos factores). Pero la aplicación
`log(pq) ↦ log(p/q)` no es afín en el retardo, y las traslaciones sólo realizan aplicaciones afines. La independencia
de los primos impide entonces que los términos espurios se cancelen. Multiplicar por una ventana no mueve el soporte.
`𝓕` envía masas puntuales a funciones casi periódicas: para volver al eje de retardos hay que aplicar `𝓕` de nuevo, y
la composición es afín o de convolución. La inclusión de `𝓕` y de la multiplicación por ventana en la clase es ARGUED.

**Relación con R1.** R161_035 y 057–065 cierran el **concomitante de borde** (`⟨g,[P,S]w⟩`, sin signo). El Lema U
cubre una clase disjunta, la de los transportes de soporte por involuciones y traslaciones. La pregunta del encargo
sobre `J` y `𝓕` queda dentro de `𝒯` (ARGUED para `𝓕`), y es NO-GO.

## 3. Lema Q (dualidad `TT*` y extensión a ℚ_{>0}): el canal de cocientes no es el de productos de otro objeto exacto

(a) Para un único polinomio de Dirichlet, `L*L` y `LL*` son ambos la multiplicación por `|A|²`, porque el operador es
    normal. La dualidad `‖T‖ = ‖T*‖` de la gran criba cambia frecuencias por puntos de muestreo, pero el núcleo
    `TT*` es `Σ w_n² n^{i(t−t')}`, diagonal en `n`. Por lo tanto no aparece ningún canal de productos. PROVED, y
    elemental. Las cotas de gran criba sólo dan cotas superiores (INV_J J2).
(b) Si se extiende el peso a ℚ_{>0} por `w(1/n) = w(n)`, con `B = A + Ā`, se obtiene `B² = A² + 2|A|² + Ā²`, de modo
    que el canal de cocientes es `½(∫ĝ B² − 2∫ĝ Re A²)`. Las identidades de Dirichlet (`Λ∗1 = log`, Selberg
    `Λ log + Λ∗Λ = μ∗log²`) actúan en el anillo de Dirichlet sobre ℕ. En el álgebra de grupo de ℚ_{>0} no hay
    análogo de `1`, porque `1∗1` diverge en todo punto. En particular, `(Λ_ℚ ∗ Λ_ℚ)(1) = 2Σ Λ(n)²/n` es la diagonal
    divergente de W3. PROVED para la divergencia. Que no exista otra identidad exacta en el álgebra de grupo es ARGUED.
(c) Renormalización de la diagonal. Restar `Σ_{n≤X}Λ(n)²/n` es exactamente el «cuadrados − constante» de I5
    (R170_201/301, falsificador `a_2 = 100`). Repetición.

## 4. Candidatas del encargo, una por una

| Cand. | Veredicto | Motivo |
|---|---|---|
| (i) inyectividad + retículo aditivo | NO-GO de selección | Lema U. Las condiciones `a ≡ b`, `a − b = h` introducen `Λ(n)Λ(n+h)`, cerrado por INV_J J3 (H_sparse) |
| (ii) `|−ζ'/ζ|²` frente a `(ζ'/ζ)'`, Selberg transportado por `J`/`𝓕` | NO-GO en `𝒯` | `(ζ'/ζ)² − (ζ'/ζ)'` pertenece al canal de productos (`Λ∗Λ`, `Λ log`); su transporte es el Lema U; Selberg sin signo, I2 (R170_851) |
| (iii) `TT*`, gran criba, dualidad | NO-GO | Lema Q(a); con extensión a ℚ_{>0}, Lema Q(b) |
| (iv) polarización / cuadrado completado | tautológico | Lema P; R170_854 §6.3, 860–861 |

## 5. Veredicto

- Ninguna candidata pasa la puerta de cuatro puntos. NO-GO de clase: Lema P (PROVED), Lema U (PROVED en la clase
  finita y en la de desplazamientos `±2 log r`, ARGUED en general y con `𝓕`), Lema Q (PROVED en (a) y en la
  divergencia de (b)).
- La independencia de los primos no linealiza el canal de cocientes; trabaja en contra de cualquier transporte desde
  el canal de productos.
- Única operación explícita que no queda cubierta: un transporte **no afín en el retardo**, por ejemplo una
  reindexación `log N ↦ log(a/b)` que dependa de la factorización de `N`. Como operador sobre `F` no está en la
  clase de traslaciones, y no se conoce una realización ciega al peso. Sin objeto escrito: OPEN. Antes de cualquier
  intento debe cotejarse con D («cambio (m,n) → (m+n,m−n)», POWER_GRAM_SLICES §17), que es su pariente aditivo.

## 6. Lo que un revisor debe rederivar

1. El Lema P(b): Douglas, y que `R` sea afín-cuadrático en `w`.
2. El Lema U: la no cancelación de `log(p'q/p²)` por factorización única. Comprobar el caso `p' = q`
   (`N = q²`, `(Λ∗Λ)(q²) = log² q`, que cae en `log(q²/p²)`; también allí el coeficiente de cocientes es
   `Λ(q²)Λ(p²) ≠ 0`, y hay que verificar que ese único punto no rescata la clase: el coeficiente queda fijado por un
   solo `j` y no se repite para todos los `p'`).
3. La extensión del Lema U a `𝓕` y a familias infinitas: es ARGUED.
