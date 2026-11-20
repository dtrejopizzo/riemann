# Ronda 15, memo B: acoplar primos distintos en el reparto por bloques, y matrices GCD como acople

Resumen. Se pone a prueba en la puerta una fuente de positividad que acopla primos distintos y no es
exponencial en el peso. Hay dos variantes: (i) un reparto conjunto por pares o triples de primos, con un
bloque cruzado (2,3) construido a partir de las casi coincidencias `2^a ≈ 3^b`, y la jerarquía de niveles que
induce; (ii) la positividad de las matrices GCD (Smith, totientes de Jordan), de las sumas de tipo Gál y del
Gram de Nyman–Báez-Duarte usada como acople. Ambas variantes quedan como repetición. (i) es la Observación 4.3
(«blocks») de `phase-159-row-d-two-front-construction/G2_B8_R5.md`; su nivel exacto es la forma misma (J3).
Además, el par obstructor de la ronda 6 no es un problema de marginales cuánticos (§2). En (ii), restringida a
las potencias de primos, la factorización de Smith se separa por primos más un término de rango uno (Lema 2,
PROVED). Por eso no puede llevar el acople entre `log 2` y `log 3`. Usa sólo divisores, así que es ciega a los
controles (S2, Lema T). Se registra una observación que la ronda 6 no menciona: el umbral `0.695–0.70` del
reparto DIR coincide con la entrada del contacto `4 = 2²` (NUMÉRICO/ARGUED, §4).

Lectura en primaria: `ROUND_006_WINDOW_SPLIT_NUMERIC.md` §§1–10; `RULES_AVOID.md` O–X; `ROUND_014_B.md`;
`G2_B8_R5.md` §§2–5 (Teorema D, Lema 2.1, Observación 4.3, §5 «cross-prime interference»);
`phase-45-fredholm/135-two-prime-theorem-positivity-for-pure.md` §0; `phase-122-*/P122_028_TWO_PRIME_FINITE_GREEN_COMPLEX.md`
§3. Grep en `03-research` e índice de «gcd», «Smith», «Gál», «Nyman», «Báez», «marginal», «compatib»,
«two-prime», «dos primos». Aciertos pertinentes: los cuatro archivos anteriores; `R184_010_THEOREM_L_STAR.md`
l.117 (forma de Franel `Σ c_q c_{q′} gcd(q,q′)²/(12qq′)`); `MAP_1_WALLS_AND_MASTER_DOCS.md` NG-A5, NG-B4,
CIR-3, CIR-6 (Beurling–Nyman y Báez-Duarte: reformulaciones, distancia circular). Los demás aciertos
usan las palabras de paso (lectura por línea, ARGUED). No releí completos REVIEW_006 ni las fases 188.

## 0. Filtro de cuatro puntos

1. **Antecedente más cercano.** `G2_B8_R5.md` Observación 4.3: «primes grouped into blocks with one LK piece per
   block. Theorem D and Lemma 2.1 hold verbatim with `Q_B = Σ_{p∈B}Q_p` … The single block `{2,3}` is `𝔞_T`
   itself». Y §5: la positividad en `(T_loc, log 2]` es una interferencia entre los valores de **una** función
   definida positiva `c_F` en `log 2` y en `log 3` («necessarily cross-prime»). Para el bloque cruzado `X`:
   `ROUND_006` §10.2 (transferencia mínima, rango uno, sin fórmula) y `RULES_AVOID` O3 (partes con signo sin
   regla: reparto vacío). Para dos primos con acople explícito: Doc 135 de la fase 45 (los datos de Weil se suman
   y el soporte mixto `p^a q^b` tiene masa nula) y P122_028 (energía efectiva de dos primos `‖y−x‖²/log(q/p)`).
   Para (ii): `R184_010` (forma de Franel con gcd), NG-B4/CIR-3 (Nyman), NG-A5 (Báez-Duarte), `RULES_AVOID` S2.
2. **Lo nuevo propuesto.** Un bloque conjunto `q_{23}` cuyo término cruzado es un operador escrito desde las
   casi coincidencias `9/8, 4/3, 3/2, 32/27, 256/243`, y una jerarquía por niveles de pares y triples. Para (ii),
   la matriz GCD como término cruzado.
3. **¿Evita la dificultad?** No.
   - (i) Si el bloque conjunto tiene que ser `⪰ 0` y la ventana sólo ve 2 y 3 (y 4), ese bloque es `a_T` (o
     `a_T` menos una parte arquimediana). El nivel exacto es el enunciado mismo (J3). Con un `X` explícito pero
     sin una identidad que lo haga firmado, se recae en O3.
   - (ii) Entre potencias de primos distintos, la positividad GCD no acopla nada salvo el divisor 1 (Lema 2), y
     no usa `Λ` ni la estructura aditiva.
4. **Enlace global.** Habría que dar una identidad
   `a_T = Σ_B q_B + (cuadrados)`, con `q_B ⪰ 0` escrito sin resolver el problema y con bloques de tamaño
   acotado, válida para todo `T`. Con bloques de tamaño acotado y `T → ∞`, la ventana contiene cada vez más
   primos por bloque. El Teorema D (dual de máximo) vale con bloques, y las pruebas explícitas de la ronda 4
   excluyen todo agrupamiento con al menos ocho bloques que toquen `S_0` para `T ≥ 1.50` (Observación 4.3,
   PROVED allí). No tengo ninguna identidad que conecte con el signo global.

Por la regla del filtro, el memo se detiene aquí en cuanto a construcción. Lo que sigue fija el cierre y las
dos precisiones.

## 1. Jerarquía por bloques (repetición; el nivel exacto es circular)

**Proposición 1 (PROVED, corolario directo de G2_B8_R5 Teorema D + Observación 4.3).** Sea `𝔅` una partición de
los primos con contactos en `[0,2T]` en bloques `B`. El reparto por bloques (una pieza LK, o DIR con potencial
libre, por bloque) existe si y sólo si `Φ^𝔅_T := inf Φ_T[(σ_B)] ≥ 0`. Aquí el ínfimo recorre las familias de
estados indexadas por bloques; en la clase DIR rige además la restricción de igual densidad de `ROUND_006` §5,
que es ARGUED allí y no se rederiva. Si `𝔅` es más fina que `𝔅′`, entonces `Φ^𝔅_T ≤ Φ^{𝔅′}_T`. Para la
partición trivial (un solo bloque) se tiene `Φ_T = λ_A(T)`, el fondo de `a_T` sobre `P_T`.

*Prueba.* La monotonía sale de que una familia indexada por `𝔅′` induce una familia indexada por `𝔅`, repitiendo
el estado de cada bloque grueso en sus bloques finos, y de que `max` sobre más copias del mismo `ε` no cambia. El
último caso es la familia igual (paso 5 del Teorema D). ∎

Consecuencia. «La jerarquía de nivel `k` es exacta para ventanas con a lo sumo `k` primos» es cierto y no dice
nada: en ese nivel el certificado es `a_T ⪰ 0`. El certificado de nivel `k` es manifiestamente no negativo sólo
si cada `q_B` lo es por una fórmula propia; sin ella es J3. Paso que se rompe en los controles: ninguno. El
reparto es comb-general (G2_B8_R5 §6, F4) y certifica exactamente cuando el fondo es `≥ 0` (`ROUND_006` §6). Con
`2Λ`, el borrado o Beurling simplemente no existe, sin que un resto firmado cambie de signo. Es el patrón de
`ROUND_013_A` W1.

## 2. ¿Es la falla un problema de marginales compatibles? (no en sentido cuántico)

**Proposición 2 (estructura del dual; ARGUED, sobre la dualidad DIR de `ROUND_006` §5, que no está probada en el
continuo).** El dual del reparto DIR es un par `(Y_2, Y_3)` de estados sobre el **mismo** espacio `L²(I)` con
igual densidad diagonal `ρ_{Y_2} = ρ_{Y_3}`. El reparto conjunto (un solo bloque) es el caso `Y_2 = Y_3`. La
brecha entre los dos niveles es la brecha entre «misma diagonal» y «mismo estado».

No hay producto tensorial ni sistema conjunto del que `Y_2` e `Y_3` sean marginales parciales. La
«compatibilidad» relevante es la igualdad, no la existencia de una extensión. El problema de marginales
cuánticos (extensión común de estados reducidos) no se aplica tal cual. La lectura correcta es la del Teorema D:
la parte arquimediana cobra `max_p ε_{σ_p}`, un funcional sublineal. La jerarquía natural no va por número de
primos sino por la clase de transferencia permitida:

| transferencia entre piezas | restricción dual | estado |
|---|---|---|
| sólo potencial `W_p(t)` | igual densidad diagonal | DIR, falla en `T ≥ 0.70` (NUMÉRICO) |
| potencial + núcleo de salto `θ_p ∈ [0,1]` | lo anterior + `max` puntual de `D_p` | es DIR (`ROUND_006` §5) |
| forma arbitraria `X` | `Y_2 = Y_3` | vacío, es el objetivo (O3) |
| `X` de rango uno con `ℓ` dado | intermedio | `ROUND_006` §10.2: `ℓ` sin fórmula |

Un nivel intermedio con `X` restringido a núcleos concentrados en los retardos `log(3^b/2^a)` es una elección de
`ℓ`. No tengo la fórmula, y el `ℓ` óptimo medido se parece a `cos(2πt/log 2)` proyectado (`ROUND_006` §10.2),
no a un objeto en `log(9/8)` o `log(4/3)`. OPEN, sin candidato.

## 3. Matrices GCD y afines como acople (repetición y ceguera)

**Lema 2 (PROVED).** Sea `σ > 0` y `J_{2σ}(d) = d^{2σ} Π_{p|d}(1 − p^{−2σ})`. Para `m, n` en
`𝒫 = {p^a : p primo, a ≥ 1} ∪ {1}`:

`gcd(m,n)^{2σ}/(mn)^σ = (mn)^{−σ} Σ_{d|m, d|n} J_{2σ}(d)`.

Restringida a `𝒫`, esta descomposición es la suma de un término de rango uno (`d = 1`,
`(mn)^{−σ}`) y de bloques por primo (`d = p^j`, `j ≥ 1`, que sólo tocan las potencias de `p`).

*Prueba.* La identidad es la de Smith (`Σ_{d|k} J_{2σ}(d) = k^{2σ}`, CITED/clásica, con `k = gcd(m,n)`). Si `m`
y `n` son potencias de primos distintos, el único divisor común es `1`. ∎

Lectura. Entre `2^a` y `3^b` el acople GCD es sólo el rango uno `(2^a 3^b)^{−σ}`, que no depende de que
`2^a/3^b` esté cerca de 1. Es una positividad multiplicativa, «por primo más una constante», del tipo 𝔖
ampliado. No ve las casi coincidencias. Además no contiene `Λ`. Bajo `cΛ` el lado firmado no cambia. Bajo el
borrado de `p^k` se quita una fila y columna de una matriz `⪰ 0`. Bajo Beurling vale la misma identidad de Smith
en el semigrupo libre (ARGUED: requiere factorización única del sistema). Entonces el Lema T de `ROUND_013_C`
excluye que el signo salga de ahí (`RULES_AVOID` S2: «un paso que use sólo divisores no falla bajo Beurling»).

- Las sumas GCD de tipo Gál, Bondarenko–Seip y Aistleitner–Berkes–Seip son **cotas superiores** de formas
  `Σ c_m c_n gcd(m,n)^{2σ}/(mn)^σ`. No aportan un signo inferior para una forma con peso negativo (ARGUED; no
  releídas en primaria). Su papel en el corpus es el de Franel en `R184_010`.
- El Gram de Nyman–Báez-Duarte de `{θ/n}`: sus entradas llevan gcd/lcm, pero el criterio es una distancia a un
  subespacio, es decir una reformulación. Ya está en el índice: NG-B4, CIR-3 (circular), NG-A5, CIR-6. No se
  reintenta.

## 4. Observación sobre el umbral de la ronda 6 (NUMÉRICO/ARGUED, sin rederivar)

El reparto DIR alcanza el techo hasta `T ≈ 0.69` y falla entre `0.695` y `0.70` (`ROUND_006` §§8.1, 10.2).
Por otro lado, el contacto `log 4` entra en la forma exactamente cuando `2T > log 4`, es decir para `T > log 2 = 0.6931`.
Por tanto el primer fallo del reparto **por primo** aparece cuando la pieza del primo 2 empieza a llevar dos
contactos (`log 2` y `log 4`). No aparece en una configuración nueva entre 2 y 3. `ROUND_006` §10.4 y el
análisis de bandas (§9.3, banda `≳ 1.2` con `θ_2 = 0`, contacto `log 4`) son compatibles con esto, pero no lo
afirman. Mientras no se pruebe, la lectura «la falla exige acoplar 2 con 3» del encargo es una hipótesis y no un
hecho de la ronda 6. El par obstructor podría ser una interacción interna 2-ádica (`log 2` frente a `log 4`)
mediada por el reparto con 3. No hay prueba en ninguna dirección.

## 5. Veredicto

- (i) Repetición de G2_B8_R5 Observación 4.3 y §5, y de `ROUND_006` §10.2 / O3. La jerarquía por bloques es
  monótona y su nivel exacto es la forma (Proposición 1, PROVED dado el Teorema D). La falla no es un problema
  de marginales cuánticos (Proposición 2, ARGUED). NO-GO de selección.
- (ii) La positividad GCD/Smith se separa por primos más un rango uno sobre las potencias de primos (Lema 2,
  PROVED). Es ciega a los tres controles (ARGUED para Beurling). Nyman/Báez-Duarte están en el índice. NO-GO de
  selección.
- Signo global de `a_T`: OPEN. No tengo una idea nueva defendible dentro de este encargo.
- Siguiente operación explícita, la más barata: decidir si el umbral DIR `0.695–0.70` es la entrada de `v_4`.
  Para eso se rehace el modo `transfer` de la ronda 6 en `T = 0.70, 0.72` con el término de `4` quitado (control
  de borrado) y con el término de `4` asignado a una tercera pieza propia. Si sin `v_4` el reparto por primo
  2 | 3 vuelve a alcanzar el techo, el obstáculo es intraprimo (potencias), no un acople 2–3, y el residuo
  «Hadamard que acople primos distintos» pierde su apoyo numérico.
