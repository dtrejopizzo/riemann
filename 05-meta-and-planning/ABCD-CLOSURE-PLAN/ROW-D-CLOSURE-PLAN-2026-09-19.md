# Plan de cierre de la fila D — 2026-09-19

*Lead: Fable 5.1. Insumos: barrido del corpus por cuatro agentes Sonnet (catálogo de rutas, material
Connes, inventario 134–149, analogías examinadas) y una auditoría hostil Opus de `R149_001`
(registrada en `R149_002_HOSTILE_AUDIT.md`). Todo lo que sigue cita archivo; nada se reconstruye.*

---

## 0. Estado en una página

* Filas A, B, C: WEIL-STRENGTH-COMPLETE (Papers 43–45). Fila D: **sin etiqueta, sin signo**.
* Fase 149 (haz aditivo, ruta de Deligne): ronda 1 entregada, **auditoría hostil hecha (2026-09-19)**.
  Veredictos: D.59 STANDS (es Hölder `‖·‖_∞ ≤ ‖·‖_{2k}`, no Weil I 3.2); D.60 STANDS con D.60.7
  rebajado de alcance; **D.61.10 DOWNGRADE** ("no hay transporte" es falso: Parseval sobre `χ` y
  Goldston–Montgomery transportan momentos; lo que no cruza es la estructura polar/positiva);
  **(P149) DOWNGRADE**: es la conjetura de `k`-tuplas de Hardy–Littlewood en traje de Deligne, no un
  objeto nuevo. Reparaciones mínimas listadas en `R149_002` §5. Faltan `R149_003` (reparaciones) y
  `R149_005` (decisión), ambas cortas.
* Paper 46: Partes I–III cerradas; Parte IV (fases 145–149) pendiente de decisión del dueño.

## 1. Lo que ya existe y NO se reconstruye

Inventario verificado (agente Sonnet, 2026-09-19; detalle en Paper 46 §23 y los `R1xx_005`):
clase canónica `K` y dualidad `σ_K` (PROVED, §11–12); teorema de transferencia 12.3 condicional a
`h⁰` y su versión de traza 12.3-B4 incondicional (§20.17); método T1 (uniforme en el cuerpo) y T2
(debe usar el producto de Euler; falla para Epstein `Ξ_Q`) (§18); **teorema del defecto de marco**
(ningún `h⁰` sobre `D^W` satisface (a),(b′),(c); `s* = 0.99846…`; vale también sobre una curva
donde RH es teorema: el defecto es del cono, no de los ceros) (§19.7, §21); diagonal de Frobenius
computada, indefinida, ciega a los ceros; "Spec Z es terminal, no hay `Z[π]`" (§22.17);
anillo de Galois inerte en `ζ` (147); efectividad mixta = condición tropical, cono sin cambio (148);
haz aditivo: extracción D.59, muro `c = 1/2`, `κ(d) = d/φ(d)`, "los exponentes suman en el cuadrado
aditivo y restan en el multiplicativo" (149, D.61.8–9: la idea buena de la fase).

Abiertos vivos que importan: (36) *una clase sobre el cuadrado que cargue un dato de FASE
(unimodularidad de las raíces locales) y no una magnitud*; O-148.2 = O-149.5 (un núcleo sobre el
cuadrado con pareo finito no nulo entre clases de fibra e invariancia diagonal); (P145′) mecanismo
con `𝔈 ≠ D^W`.

## 2. Las seis conclusiones invariantes del corpus (por qué el signo nunca llega)

1. La magnitud no ve el signo; sólo la coherencia de fase de `cos(t log n)` (fase 60, 136; NG-F1).
2. Toda positividad incondicional es una cota INFERIOR; RH es una cota SUPERIOR (05-MASTER-CLOSING VII).
3. La aritmética de `Re s > 1` no se propaga a la banda; ningún primo "posee" un cero (MW-2, NG-B1).
4. No hay `+` sobre las correspondencias: sólo el semigrupo `{π^n}` (145–148; Thm 22.17).
5. No existe el sitio aritmético con `H¹`, Frobenius y forma positiva (MW-5); fila D ≡ RH dos veces (113, 118).
6. T1 ∧ T2: uniforme en `K` y esencialmente Euler; todo lo construido es `Ξ_a`-uniforme o restatement.

Catálogo completo de 57 rutas con veredicto: informe del agente (2026-09-19) volcado en §7 abajo
en forma comprimida; fuente primaria `NO-GO-LIST.md`, `ROW-D-MAP-2026-09-13b.md`,
`PHASE_136_MAP_SYNTHESIS_AND_PLAN.md`.

## 3. Diagnóstico del lead (nuevo, 2026-09-19)

**3.1 Los cinco muros son uno, y tiene nombre clásico.** Los "dos cuadrados" de D.61.10 son los dos
cocientes del cuadrado adélico: el **aditivo** `A/Q` (solenoide compacto; sus puntos racionales son
el haz de Farey `e(na/q)` de la fase 149 y su dirección arquimediana es el haz `n^{it}`), y el
**multiplicativo** `A/Q^×` (espacio de clases de adeles de Connes, sitio de escala). El único puente
incondicional entre ambos es la dualidad Fourier–Mellin de la tesis de Tate: Poisson sobre `Q ⊂ A`
⇒ ecuación funcional (= dualidad de Poincaré). El "dato de fase" del abierto (36) ya existe para
`GL(1)`: son los **factores ε locales** `ε_v(s,χ_v,ψ_v)`, unimodulares, cuyo producto es el número
raíz (fórmula del producto). Lo que falta no es el dato: es cómo el dato constriñe ceros.

**3.2 De la Vallée Poussin es Deligne con `k = 1` sobre el haz arquimediano.** `3+4cos θ+cos 2θ =
2(1+cos θ)² ≥ 0` es el cuadrado de Rankin; el polo en `s = 1` es el bloque de coinvariantes a priori;
Landau da la región `1 − c/log t`. Su optimalidad para **sistemas de primos de Beurling**
(Diamond–Montgomery–Vorhauer, 2006: existen sistemas con producto de Euler, `Λ ≥ 0`, polo, y ceros
en `1 − c/log t`) demuestra que positividad + polo + producto de Euler NO alcanzan `β ≤ 1 − δ`:
hace falta la estructura ADITIVA de `Z` (la que produce Poisson y la ecuación funcional).
**Consecuencia: tercer teorema de método T3** — toda prueba de `β ≤ 1−δ` debe separar `Z` de un
sistema de Beurling; un sistema de Beurling es un **falsificador nuevo** (con Euler, sin `+`),
complementario de `Ξ_Q` (con `+`/ecuación funcional, sin Euler) y de `Ξ_a` (Euler no unimodular).
Chequeo de corpus: `Vorhauer` 1 aparición incidental (E101_089); "Beurling primes" 0. **NUEVO.**

**3.3 El único transporte incondicional del cuadrado aditivo a los ceros es Vinogradov–Korobov**, y
transporta magnitud: energía aditiva de la curva de momentos (teorema del valor medio de Vinogradov;
hoy decoupling) ⇒ `|ζ(1+it)| ≪ (log t)^{2/3}` ⇒ región `1 − c/(log t)^{2/3}(log log t)^{1/3}`.
Es consistente con la conclusión 1: la energía llega a los ceros sólo a través de `|ζ|`. El objeto
nuevo debe hacer llegar energía aditiva a los ceros **a través de la fase**, no de la magnitud.

**3.4 La finitud no es lo esencial en Deligne.** Weil I 3.2 usa la finitud de `H¹_c` sólo para saber
que el bloque de los ceros es NUMERADOR (holomorfo) y no aporta singularidades; Landau sólo necesita
que la primera singularidad real de la `L` de la familia sea el polo a priori. Reformulación sin
finitud del Lema Faltante 5.3 (Doc 106): *la contribución de los ceros a la serie de la familia debe
ser holomorfa a la izquierda del polo a priori* — equivalentemente (auditor R149_002 §3):
**promover la serie singular de densidad a divisor polar.** Sobre `F_q` lo hace Künneth + filtración
de pesos sobre `H_c(X×X)`; sobre `Z` nadie.

**3.5 Las conjeturas de Weil se probaron por cuatro vías y el corpus transpuso dos.**

| vía | mecanismo central | transposición en el corpus |
|---|---|---|
| Hasse–Weil 1948 | anillo de correspondencias, Rosati/Castelnuovo–Severi | fases 107–148: negativo (no hay `+`) |
| Deligne 1974 (Weil I) | potencias tensoriales, Landau, coinvariantes de la monodromía, extracción | fase 149: negativo ((P149) = `k`-tuplas) |
| **Laumon 1987** (Weil II vía Fourier) | **transformada de Fourier ℓ-ádica** (transporte `+`/`×`), fase estacionaria (monodromía local en `∞`), **sumas de Gauss unimodulares** `|g| = √q`, fórmula del producto de los ε | **0 apariciones** (`Laumon`, `Gauss sum`, `Hasse–Davenport`: 0) |
| **Kedlaya 2006** (p-ádica, misma arquitectura) | Fourier en cohomología rígida | **0 apariciones** |
| Bombieri–Stepanov (curvas) | función auxiliar, Riemann–Roch, `deg div f = 0` | sólo como auditoría (116) |

La vía de Laumon es la única cuyo mecanismo central es exactamente lo que la fila D dice que falta:
un transporte entre el cuadrado aditivo y el multiplicativo cuya pureza se reduce a un **dato de fase
unimodular** (sumas de Gauss). Es el candidato lateral número uno.

## 4. Candidatos laterales, rankeados, con chequeo de corpus

**L1 — Ruta de Laumon sobre `Z`: la transformada de Fourier como transporte entre cuadrados.**
Sobre `F_q`: `FT_ψ(L_χ) = g(χ,ψ)·L_{χ̄}` — los caracteres multiplicativos son autovectores de la
Fourier aditiva con autovalor de módulo `√q`; la pureza de `FT` (Katz–Laumon) y la fase estacionaria
reducen los pesos de un haz arbitrario a sumas de Gauss. Sobre `Z`: `FT` sobre el haz `A/Q` es la
ecuación funcional de `L(s,χ)` con número raíz `τ(χ)/√q`; la "fase estacionaria en `∞`" es el factor
Gamma (el bloque polar `K` de las filas A–C); la "pureza de `FT`" en su forma débil es D.59.3
(ATRH ⟹ GRH), trivial. Lo que hay que averiguar, y es la **prueba ácida**: (a) dónde exactamente
usa Laumon la finitud (constructibilidad de `FT(F)`, semicontinuidad de Deligne) y si ese uso es
sustituible por holomorfía (3.4); (b) si la deducción "pesos arbitrarios ⇐ sumas de Gauss" tiene
un avatar "ceros de `ζ` ⇐ números raíz de `L(s,χ)`" — hoy no se conoce ninguno; (c) Kedlaya como
segunda instancia independiente de la misma arquitectura. Riesgo: la finitud reaparece en la
constructibilidad. Gates: `Ξ_a` (raíces `p^{±a}` rompen `|g|=√q`: el candidato debe fallar ahí),
`Ξ_Q` (sin Euler, sin sumas de Gauss), Beurling (sin `+`, sin Fourier). **Fase 150.**

**L2 — Cota superior sin positividad: Dolgopyat y el principio de incertidumbre fractal.**
Bourgain–Dyatlov (Ann. Math. 2018) prueban para toda superficie hiperbólica convexo-cocompacta una
banda libre de resonancias `Re s < 1/2 − β` más allá del umbral unitario, sin positividad: un estado
resonante no puede concentrarse en el conjunto atrapado a la vez en posición y frecuencia. Es el
único mecanismo conocido que produce una **cota superior** (conclusión 2) sobre partes reales de
ceros de una zeta dinámica con infinitos ceros. Para la superficie modular las resonancias son
exactamente `ρ/2` (polos de `φ(s) = ξ(2s−1)/ξ(2s)`): RH ⟺ resonancias en `Re s = 1/4`. El
mecanismo falla literalmente (δ = 1, sin fractalidad); la pregunta lateral es si la **rigidez
aritmética** (Hecke; Lindenstrauss) sustituye a la fractalidad para los estados resonantes
`E*(z,ρ/2)`. Dolgopyat mismo es un mecanismo de **no coherencia de fase** (UNI) — conclusión 1.
Baladi–Vallée lo probaron para el operador de Gauss cerca de `Re s = 1`. Corpus: `Dyatlov`,
`Dolgopyat`, `Baladi`, `fractal uncertainty`, `Lindenstrauss`: **0**. **Fase 151** (chequeo de
literatura + un enunciado (P151) preciso o muerte rápida).

**L3 — El "mismo cuadrado" ya existente: operador de transferencia de Mayer y funciones de período de
Lewis–Zagier.** Un solo objeto carga el `+` (Farey, `x ↦ x+1`, `SL₂(Z)`) y el `×` (`ζ(2s)` en el
determinante de Fredholm); los ceros de `ζ` son parámetros de autovalor 1 (períodos de la serie de
Eisenstein); la ecuación de tres términos `ψ(x) = ψ(x+1) + (x+1)^{−2s}ψ(x/(x+1))` es un transporte
`+`/`×` a nivel de autofunciones. Predicción del lead, verificada a mano: la positividad de
Perron–Frobenius del operador real es magnitud y por dominación da sólo `Re ρ ≤ 1` (conclusión 1,
como debe ser). Lo no-magnitud es la ecuación de tres términos. Corpus: `Lewis`, `period function`,
`Gauss map`: 0; `Mayer` 1; Knauf (cadena de Farey, `ζ(s−1)/ζ(s)`, ferromagnética) 1 (CAND-3: falla
Lee–Yang). Barato. **Fase 152**, una ronda.

**L4 — Calibración de Beurling (T3).** No es ruta: es el falsificador que faltaba (3.2). Se
incorpora como gate obligatorio desde la fase 150 y como teorema de método en Paper 46 §18.

**L5 — Cierre honesto de (P149).** Registrar que es la conjetura de `k`-tuplas (auditor §4);
O-149.5 se fusiona con O-148.2. No perseguir.

**Descartados tras chequeo (con razón):** Taylor–Wiles (patching = familia libre sobre el álgebra
del grupo ⇒ fibra en `χ = 1`: es la fase 147 en otro lenguaje, inerte en `ζ`); Kudla (números de
intersección aritméticos = valores/derivadas de Eisenstein, no ceros); Lee–Yang (ceros de Fisher en
la temperatura: sin teorema; CAND-3); Kesten/Haagerup/grafos de Ramanujan (finitud o Plancherel
local; "temperado" ≠ ceros globales); Maass–Selberg/Eisenstein (alcanza sólo `Re s = 1`,
Shahidi); Rankin–Selberg hacia Ramanujan (acota parámetros locales `α_p`, no ceros: Deligne sobre
`Q` ya existe y es Kim–Sarnak).

## 5. Circuito (mismo que 138–149: constructor + auditor hostil; matemática pura)

| fase | contenido | entregables | gates |
|---|---|---|---|
| 149 (cierre) | `R149_003` reparaciones (i)–(vi) de `R149_002` §5; `R149_004` confirmación; `R149_005` decisión: D.61.8–9 finding; D.61.10 reescrito; (P149) = `k`-tuplas | tres archivos cortos; `PLAN.md`; Paper 46 Parte IV si el dueño lo decide | FATAL |
| **150** | **T3 + Laumon**: (0) CORPUS_CHECK; (1) T3 con la construcción DMV como falsificador formal `ζ_P`; (2) lectura técnica de Laumon 1987 §§ pureza de `FT`, fase estacionaria, uso de la finitud; Kedlaya 2006 en paralelo; (3) diccionario `F_q → Z` (tabla como §3.5); (4) enunciado (P150): el avatar sobre `Z` de "pureza de `FT` ⇐ sumas de Gauss", o teorema de imposibilidad con el punto exacto donde la finitud es insustituible | `R150_000…005` | `Ξ_a`, `Ξ_Q`, `ζ_K`, **Beurling** |
| 151 | Dolgopyat / FUP: resonancias de la superficie modular; qué sustituye a la fractalidad; (P151) o muerte | `R151_000…005` | ídem |
| 152 | Mayer / Lewis–Zagier: la ecuación de tres términos como transporte; ¿alguna desigualdad no-magnitud en `s = ρ/2`? | `R152_000…003` (una ronda) | ídem |
| 153 | Síntesis: o bien un objeto con las cinco propiedades (§6), o cierre de D en el mapa con T1–T3 y Parte IV | decisión del dueño | — |

Reglas vigentes: numérica sólo para identidades; nunca reetiquetar; "lo que vale crea el objeto, no
lo rodea"; toda idea pasa por CORPUS_CHECK antes de construirse.

## 6. Criterio de éxito (qué cierra D) y criterio de cierre negativo

Cierra D un objeto `𝒪` sobre el cuadrado adélico tal que: (1) es un cuadrado (positividad de
Rankin, estable por torcedura); (2) su divisor polar está determinado por datos locales
(`κ`, `𝔖`, factores ε) — la serie singular promovida a polo; (3) la contribución de los ceros es
holomorfa a la izquierda de ese polo (3.4); (4) lee fase: falla para `Ξ_a`; (5) usa `+` y `×`:
falla para `Ξ_Q` y para todo sistema de Beurling; y (6) es uniforme en el cuerpo (T1).
Si las fases 150–152 terminan con teoremas de imposibilidad, D se cierra en el mapa con T1, T2, T3
y la reformulación 3.4 como enunciado exacto del muro, y se escribe la Parte IV del Paper 46.

## 7. Catálogo comprimido de rutas muertas (para no repetir)

(a) Hilbert–Pólya/operador: OS-reflexión (NG-E5, NG-E1), autovectores distribucionales (NG-C3),
Bost–Connes KMS (Thm 161.9), triples espectrales CCM (CAND-1, abierto pero cada mecanismo cerrado:
NG-66/67/68/69), foliaciones de Deninger (136 C), ocho paradigmas de positividad (P7–P13: todos
RH-equivalentes, "capstone del signo equivocado"), caos multiplicativo (N7).
(b) Weil/forma explícita: λ_min (NG-A8, NG-E2), Cauchy–Schwarz global (NG-E3), formas relativas
(NG-E4), peine puntual (NG-E6), Carleson (NG-F1), Cesàro (NG-62), HR cuaterniónica (NG-62b),
Frobenius `J`-lineal (NG-63), MW-1, RH-PROOF fase 65 (refutado en 137).
(c) Connes–Consani: prolate arquimediano (probado, sólo `∞`), RR absoluto (=CAP), sitio aritmético
(MW-5), `Δ→Σ` no transfiere (137 D.13-γ abierto), Deninger–Morishita (NG-107).
(d) Arakelov/Hodge: transcripción de Weil (107_241), forma `Q` (33), `h⁰_RR⁺` (NG-113 O1–O3),
divisibilidad por `ξ` (NG-110), fila d ≡ RH (113, 118), Toeplitz/Hankel (NG-118), Schur log
(NG-116), `c_N` (NG-117), clase `K`/transferencia (135–144: restatements), T1/T2 (138–139), modelo
`E/F_2` (145), forma de grado (146), diagonal (146), anillo de Galois (147), efectividad mixta (148).
(e) `F_q`: Weng (CAND-2), toy tropical `C_p×C_p` (41/125), fase 145.
(f) Analítico: Hasse–Minkowski (NG-C1, MW-3), positividad de familias (item 5, abierto/riesgo),
Rankin–Selberg `Γ·Γ ≥ 0` (M1: reduce, no resuelve), 15 mecanismos clásicos (NG-B1, MW-2),
Kurasov–Sarnak (=Lee–Yang), anclas de borde (=CAP), índice de integralidad (=Deninger), 149.
(g) Otros: anatomía multiplicativa S1, jerarquía ω/BRW S2 (RH-independientes).

## 8. Re-examen del lead (segunda pasada, 2026-09-19) — novedad y valor, sin venderse nada

Pedido del dueño: volver a razonar si esto es nuevo, si no está en el corpus, y si vale la pena.

**8.1 Novedad frente al corpus (verificada por grep, 2026-09-19).** Laumon, Kedlaya, sumas de Gauss,
Hasse–Davenport, Dyatlov, Dolgopyat, Baladi, incertidumbre fractal, Lindenstrauss, Lewis, funciones de
período, mapa de Gauss, primos de Beurling: **0 apariciones** (Vorhauer: 1, incidental). "Weil II": 5
archivos, ninguno sobre la prueba vía Fourier. Mayer: 1, contexto motívico. Superficie modular y
determinante de dispersión: 0. **Pero** el Doc 106 (fase 36) ya contiene: (a) "la maquinaria que
garantiza que los polos no se mueven es la finitud cohomológica"; (b) la **Forma B**: "finitud +
racionalidad (presupuesto de índice) en lugar de positividad"; (c) el Problema 5.4 (¿es autónomo el
lado aritmético de la fórmula de Weil en dos variables sobre `p_1p_2`?); (d) "vacuidad de la familia
Rankin–Selberg de `ζ`". Por tanto mi 3.4 es un **refinamiento** de la Forma B (finitud → holomorfía
del bloque de ceros a la izquierda del polo a priori; Landau no necesita finitud), no una idea nueva.
El descarte de Rankin–Selberg→Ramanujan ya estaba en el corpus.

**8.2 Laumon (L1), reconsiderado a la baja.** Lo que Laumon cambia respecto de Deligne es *dónde se
computa el bloque de coinvariantes*: localmente en `∞` (fase estacionaria, transformadas de Fourier
locales, sumas de Gauss) en vez de globalmente (haz de Lefschetz, monodromía grande). Lo que Laumon
**no** cambia, por lo que el lead recuerda de la estructura de la prueba y debe confirmarse en la
fuente: sigue usando Rankin (potencias tensoriales), Landau y la **racionalidad** de la `L` de la
familia. Sobre `Z` el bloque de coinvariantes ya está computado (serie singular, `κ`, fase 149): la
ganancia de Laumon ataca una parte que **no es el muro**. El muro es 3.4 (holomorfía / racionalidad
del bloque de ceros) y Laumon lo hereda intacto. Valor real de L1: el diccionario (arcos mayores =
parte puntual de `FT`; monodromía local en `∞` = factor Gamma = bloque polar `K` de las filas A–C;
serie singular = pesos de la parte puntual), que conecta por primera vez el bloque polar con la serie
singular. **Reclasificado: ronda 0 de diccionario (un constructor, un auditor), no fase completa;
expectativa: reubica el muro, no lo quita.**

**8.3 Bourgain–Dyatlov (L2).** Es el único mecanismo con la forma correcta (cota superior sin
positividad) y es nuevo. Pero: la incertidumbre fractal exige `δ < 1`; la superficie modular tiene
`δ = 1` y la banda `β(δ) → 0`; los estados resonantes en `ρ/2` son las series de Eisenstein
`E*(z,ρ/2)` y su no-concentración fuera de la recta es desconocida; la QUE de Eisenstein sobre la
recta (Luo–Sarnak) usa cotas de `ζ` (circular). Probabilidad baja. **Reclasificado: chequeo de
literatura de una ronda, exploratorio.**

**8.4 Mayer / Lewis–Zagier (L3).** Es un objeto con `+` y `×`, pero es una realización espectral de
`ζ(2s)` vía la superficie modular: pertenece a la familia (a) Hilbert–Pólya del catálogo. La
positividad de Perron–Frobenius es magnitud (dominación ⇒ `Re ρ ≤ 1`, verificado). Que los ceros sean
parámetros de autovalor 1 se obtiene construyendo la función de período **con** `ζ`: restatement, la
misma lección que "Connes (1999) no construye un operador autoadjunto". **Probable RESTATEMENT; una
ronda barata o nada.**

**8.5 Beurling / T3 (L4).** Nuevo en el corpus, barato, y es un teorema de método genuino: convierte la
conclusión invariante 4 ("no hay `+`") en un enunciado con clase de contraejemplos concreta
(Diamond–Montgomery–Vorhauer): producto de Euler + `Λ ≥ 0` + polo no bastan para `β ≤ 1−δ`. Cierra el
triángulo de falsificadores: `Ξ_a` (Euler no unimodular), `Ξ_Q` (`+` sin Euler), Beurling (Euler sin
`+`). **Vale la pena; se hace primero.**

**8.6 Veredicto honesto.** Tras la segunda pasada, ninguno de L1–L3 es una apuesta creíble para
producir el signo; su valor es afilar el muro. El objetivo estructuralmente correcto sigue siendo
3.4/Forma B: hacer holomorfo el bloque de ceros a la izquierda del polo a priori, y la fase 149 ya
mostró (D.62.2) que en el haz aditivo eso es de fuerza RH. La evidencia acumulada del corpus apunta a
que D se cierra **en el mapa**, con T1, T2, T3 y 3.4 como enunciado exacto del muro, y la Parte IV del
Paper 46. Circuito revisado: **150 = T3 (una ronda) + ronda 0 del diccionario de Laumon; 151 =
decisión del dueño** entre cerrar D en el mapa o gastar rondas exploratorias en L2/L3.

## 9. Tercera pasada (2026-09-19): "no puede ser imposible" — qué se puede hacer de verdad

**9.1 Hallazgo de corpus que cambia el mapa.** Fase 114 / Paper 42 (`certificates/row_d_log2`, reproducido y
diagnosticado en fase 118 `W4_CERTIFIED_RANGE.md`): `A_T ≥ 0` sobre todo `P_T` para `0 < T ≤ log 2` —
positividad de Weil **con los primos 2 y 3 acoplados al bloque arquimediano**, certificada en Arb; margen
final `8.63·10⁻⁸`; el endpoint `½·log 5` (tres contactos) fue intentado y **retirado**. El límite no es
numérico (precisión y cuadratura con 5–10× de holgura): es la delgadez del margen — la cascada
exponencial `V₊` de NG-62b vista desde el certificado. Fase 119 cerró con la compuerta DH. Por tanto "el
teorema de signo más pequeño no gratuito" **ya existe** en el corpus, y su extensión mide exactamente el muro.

**9.2 Reformulación cuantitativa del muro (verificada a mano).** Sobre `P_T`, la cota trivial es
`A_T ≥ −C e^{T}‖F‖²` (`Σ_{n≤e^{2T}} Λ(n)/√n ≍ e^{T}`), que equivale a `β ≤ 1`. Cualquier
`λ_min(A_T) ≥ −C e^{aT}` con `a < 1` equivale a la banda `β ≤ (1+a)/2`; `a = 0` (o subexponencial) es RH.
Es la forma "λ_min" de NG-62 (crecimiento secular `λ^{2β−1}`): la negatividad de la forma de Weil en
soporte `T` crece exactamente como el peor cero. Nada nuevo, pero fija la escala: **cada primo añadido al
certificado cuesta un factor exponencial de margen, y ningún certificado finito puede alcanzar `a<1`.**

**9.3 Lo que descarté en esta pasada, con la razón.** Familias `{ζ_{K_d}}` (ζ es sumando constante: Deligne
no prueba la pureza de un sumando constante); familia cuadrática `{L(s,χ_d)}` con serie de Dirichlet
múltiple de grupo de Weyl (polos a priori existen, pero la fibra `d = □` es ζ y su polo en `w = ½` queda
dominado por el polo de familia en `w = 1`; el gran cribado cuadrático excluye los cuadrados); haz
arquimediano `t` con el teorema del valor medio de Montgomery–Vaughan (mismo muro `c = ½`: la familia
computable por Parseval tiene tamaño `≥ N^k` y la extracción se anula; Guth–Maynard es progreso en la
conjetura de valores grandes, i.e. en (P149) arquimediano, y da densidad, no RH); Goldbach promedio con
ahorro de potencia (Bhowmik–Ruzsa) = error de PNT integrado; universalidad de Voronin / Bagchi (RH ⟺
auto-aproximación: reformulación); interpolación de Fourier con ceros (Bondarenko–Radchenko–Seip) y
Radchenko–Viazovska (no asumen RH; la realidad de los nodos reduce a de Branges); Burgess (no hay suma
completa sobre `Z`). **Régimen liso:** todo método incondicional de cancelación (Vinogradov, van der
Corput, Vaughan, restricción) opera cuando la frecuencia es ≥ la longitud; RH vive en frecuencia fija y
longitud `→ ∞`, donde `n^{-iγ}` es constante por bloques y la suma es `ψ(N) − N` mismo. Ese es el muro en
una frase, y es un enunciado de método (T4 candidato).

**9.4 Qué se puede hacer, honestamente.**
(i) **Teoremas de método nuevos**: T3 (Beurling), T4 (régimen liso: toda cancelación conocida exige
frecuencia ≥ longitud), T5 (no-extracción: toda cota de momentos obtenida por ortogonalidad `L²` tiene
tamaño de familia ≥ longitud de fibra y extrae la cota trivial). Los tres son demostrables en una ronda y
convierten el mapa de no-gos en teoremas.
(ii) **Extender el certificado** de `log 2` a `½·log 5` (tres contactos) corrigiendo el intento retirado: un
teorema real, asistido por computadora, no una ruta; su valor es medir la caída del margen frente a la
predicción `e^{-cT}`.
(iii) **La única avenida creativa que no colapsa por construcción**: el cuadrado del sitio de escala de
Connes–Consani con la Forma B (finitud/holomorfía en lugar de positividad), es decir MW-5 — abierto hace
décadas; el corpus ya tiene el diccionario. Si el dueño quiere "crear el objeto", es este; no hay atajo.
**Recomendación**: hacer (i) en la fase 150, decidir (ii) según presupuesto, y no abrir (iii) sin una idea
concreta para la parte puntual/lisa del cuadrado.

## 10. Después del cierre en el mapa (2026-09-19, noche): el puente y los mecanismos no analizados

**10.1 Fase 151 (T6) cerrada.** Toda familia con fibras como sumandos no negativos tiene, por
Pringsheim–Landau, abscisa `≥ 2kβ_max`: el "puente" de Deligne sobre `Z` es el teorema mismo en cada `k`
(restatement de Thm 26.4 + Cor 27.10a; nuevo sólo el Lema 2.4). Corrección del auditor, hallazgo de registro:
la positividad espectral `⟨Hf,f⟩ = Σλ_j|⟨f,e_j⟩|²` también es una suma no negativa; **el eje es sumando vs
numerador**. Deligne funciona porque los ceros de las fibras entran en la fórmula de trazas de la familia con
signo de numerador (cohomología impar). Sobre `Z` el único mecanismo de signo de numerador es de la Vallée
Poussin, y su profundidad `1/log γ` está fijada por el mar arquimediano (Doc 111 §3.2, fase 37; cuantificado
en `R151_005` §2.2: penalización `(P(0)−a_0)(½)log γ`, cota de Fejér `a_1 ≤ 2a_0`).

**10.2 Barrido del corpus, catorce mecanismos que no son positividad (agente Sonnet, 2026-09-19).**
ANALIZADOS y cerrados: suma-producto/combinatoria aditiva (150), ecuaciones diferenciales aritméticas /
prismático (15, M6), dinámica de ceros dBN (33, 70: reducido a la identidad q-resolvente, abierto pero
mapeado), probabilístico/Cramér/Harper (12–13, 19: escapa al capstone, choca con N7), funtorialidad de
Langlands (30), caos cuántico/Berry–Keating (53, 67), interpolación de Fourier (35/101), universalidad de
Voronin–Bagchi (35/102: RUTA CERRADA). **NUNCA ANALIZADOS**: (1) principio de incertidumbre fractal /
Dolgopyat / brechas de resonancias (0); (2) espacios de Berkovich globales sobre `Z` (Poineau; el propio
corpus lo marca como hueco: "No Berkovich space over Spec Z … anywhere"); (3) rigidez de medidas del
semigrupo `×p` (Furstenberg, Rudolph, Lindenstrauss: 0–1); (4) métodos modelo-teóricos (0); (5) funciones
auxiliares / trascendencia / Pila–Wilkie (0; el único "Stepanov" del corpus es un homónimo).
Lax–Phillips: 9 apariciones, como coligación, no como teoría de dispersión de la superficie modular;
Eisenstein/estado resonante: 0–2.

**10.3 Lo que un enfoque nuevo tiene que ser, por lo probado.** O bien un mecanismo de signo de numerador con
penalización arquimediana acotada (ninguno conocido), o bien un mecanismo que no sea positividad. Los cinco
de 10.2 son los únicos candidatos no analizados; ninguno tiene hoy un enunciado formulado que produzca el
signo. **Fase 152 = ronda 0 de factibilidad** sobre (1) y (2), con criterio de muerte previo; (3)–(5) en
reserva.

**10.4 Fase 152, ronda 0 (cerrada la misma noche).** Veredicto del auditor, aceptado: *ningún camino
encontrado; ninguna imposibilidad probada*. De registro: Prop A.4 (la serie de ramas del mapa de Gauss tiene
abscisa `Re s = ½`: la ruta Dolgopyat por sumas de ramas es MW-2 en forma dinámica) y Prop B.3 (la teoría del
potencial en el árbol `M(Z)` es por rama, ciega al acoplamiento entre lugares donde vive el signo). Retirados:
Cor A.5 (sobre el disco de Mayer una cota tipo Dolgopyat SÍ es enunciable), "fase 16 ya cubre esto"
(exagerado), Q6 (error de categoría). Quedan formulados y nuevos en el corpus: **(P152.1)** cota tipo
Dolgopyat para el operador de Mayer continuado vía la ecuación de tres términos de Lewis–Zagier (forma lógica
correcta, sin método; falla la compuerta arquimediana como está); **(P152.2)** núcleo de diferencias sobre la
recta de Berkovich `A^{1,an}_Z`, con el test barato decisivo de ceguera a Beurling; (P152.3) higiene.
Recomendación: una sola ronda acotada sobre el test de (P152.2); (P152.1) al §28.3 del Paper 46.
