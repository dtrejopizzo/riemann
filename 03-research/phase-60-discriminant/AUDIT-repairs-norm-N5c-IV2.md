# Reparación de los tres puntos 🟠: Normalización, N5c-DH, IV.2≡§V (conflación) Resolución matemática pura. La tercera (IV.2) destapó un hallazgo de fondo: **H1 sobre-afirma
"QW PSD"**, y la renormalización `/ε_0` tiene positividad de Weil (RH) horneada. --- ## 1. Normalización — RESUELTO limpio **El cabo:** `ξ̂_λ` es autovector, definido salvo escala; `ε_loc=sup|ξ̂_λ−Ξ|` no está bien
definido sin fijar escala. **Resolución:** la conclusión de la cadena es **Hurwitz**, que es **invariante por constante
no nula**: si `c_λ ξ̂_λ → Ξ` uniforme con `c_λ≠0` y `ξ̂_λ` real-rooted, entonces `Ξ` es
real-rooted (las raíces de `c_λ ξ̂_λ` = las de `ξ̂_λ` = reales). Por tanto la normalización
es **libre** y se fija canónicamente:
``` ξ̂_λ(0):= Ξ(0) (match de valor en el centro; ambas pares, valor central ≠0).
```
Concretamente `ξ̂_λ(0)=ξ_0·L/2` (residuo `k=0`), no nulo (fundamental par); se reescala `ξ`
para igualar `Ξ(0)`. Con esto:
- `ε_loc=sup|ξ̂_λ−Ξ|` queda **bien definido**.
- `Γ=sup|ξ̂_λ| = O(1)` (no `O(logλ)`): `ξ̂_λ≈Ξ`, `sup|Ξ|=O(1)` por el decaimiento gamma. **Mejora N2.**
- La conclusión RH es **independiente** de la elección (Hurwitz-invariante). **[RESUELTO]** Cabo cerrado para N2, III, Thm 2. (En III se puede usar también la
normalización `L²`; ambas son válidas y Hurwitz-invariantes.) --- ## 2. N5c-DH — RESUELTO a inputs nombrados (y corrige de paso la fuente de real-rootedness) **El cabo:** la cota `sup|ξ̂_f−Ξ_f| ≥ |Ξ_f(x₀)|>0` usa (i) `ξ̂_f` real-rooted y (ii)
convergencia en eje real `ξ̂_f(x₀)→Ξ_f(x₀)`, asumida. **Resolución de (i) — y hallazgo:** `ξ̂_DH` **ES** real-rooted, y esto **NO viene de
`Λ(n)≥0`/PF** (DH tiene `b(n)` con cambios de signo, PF falla) sino de la **realización
espectral auto-adjunta de CCM** (las raíces seculares del autovector fundamental de un
operador auto-adjunto). Empíricamente confirmado (E9b: raíces DH reales 78,…,85.73,…).
**Esto corrige la fuente de E1:** la real-rootedness vale para ζ **y** DH ⟹ no puede
depender del signo de los coeficientes ⟹ su mecanismo es Hermite–Biehler/auto-adjunto, no
Perron–Frobenius. (Consistente con la reparación E1: el contraejemplo mostró que la
positividad no la da, y aquí vemos que ni siquiera es necesaria — DH la tiene sin
positividad.) **Resolución de (ii):** la convergencia en el eje real `ξ̂_f(x₀)→Ξ_f(x₀)` en un punto
interior fijo `x₀` (bien debajo del horizonte para `λ` grande) **es** el análogo para `f`
del andamiaje E2.a + horizonte (probado para ζ, mismo mecanismo de construcción). No es
gratis pero **no es un gap nuevo**: es el andamiaje ya probado, instanciado en `f`. **[RESUELTO a dependencias nombradas]:** N5c-DH es **sólida módulo** (i) real-rootedness de
CCM [auto-adjunta, cierta para DH] + (ii) convergencia-en-eje [= andamiaje E2.a/horizonte].
La monotonía `|g(x+iy)|≥|g(x)|` es correcta. No es un gap profundo; hereda E1 (real-root) y
E2.a (eje). Baja de 🟠 a "sólida módulo andamiaje". --- ## 3. IV.2≡§V — NO hay conflación, PERO destapa que H1 sobre-afirma y `/ε_0` asume Weil≥0 **El cabo (2 partes):** (1) "dim=N(T*) pinea `g∝Ξ_T`" heurístico; (2) conflación: ¿es el
operador CCM `A_λ` la forma de Weil cruda? **Resolución de (2) — NO hay conflación:** por la fórmula explícita de Weil,
``` QW = (archimedean) − (arithmetic) = Σ_ρ g(γ_ρ) conj(g(conj γ_ρ)) [lado-ceros].
```
Las entradas `QW[m,n]=∫q_{mn}w_arch − Σ Λ(n)/√n q_{mn}` **son** la forma de Weil. ⟹ el
ground state CCM `ξ̂_λ` **ES** el minimizador de Weil. **No son operadores distintos.** El
argumento variacional es sobre el objeto correcto. **[conflación DESCARTADA]** **Resolución de (1) — refinada, no exacta:** el minimizador `g_0` es el autovector del
fondo del operador de frame `S=Σ_ρ K_{γ_ρ}⊗K_{γ_ρ}|_{PW_Ω}`. NO es exactamente `Ξ_T` a `λ`
finito; es `g_0 = Ξ_T + O(déficit)`, y `g_0 → Ξ_T` cuando `λ→∞` (el déficit
`ε_0 ~ C_0/λ² → 0`). El conteo `dim≈N(T*)` (densidad crítica, Landau–Beurling) hace el
espacio casi-nulo de baja dimensión con `Ξ_T` adentro. **Rigorizable** (análisis de déficit
de frame), pero "exactamente `Ξ_T`" es **falso a λ finito** — es límite. **HALLAZGO DE FONDO (lo importante):** como `QW = forma de Weil`,
``` QW PSD (todos ε_k≥0) ⟺ Weil-positividad en banda log λ ⟺ RH hasta altura T*.
```
Consecuencias:
- **H1 SOBRE-AFIRMA.** El memo dice "H1 prueba QW PSD incondicional vía PF". **Falso.** Perron–Frobenius da fondo **simple + autovector positivo** (estructura del ground state), **NO** da `ε_0≥0` (PSD). El signo de `ε_0` ES Weil-positividad ⟺ RH-hasta-T*. PF ≠ PSD. Si H1 probara PSD incondicional, probaría RH — imposible. **Corregir H1: PF da estructura, no positividad.**
- **La renormalización `/ε_0` (III) asume `ε_0>0` = Weil-positividad-hasta-T*** (≈RH-hasta-T*). Es decir, el "truco" que disuelve el gap exp-pequeño **tiene RH horneada** en `ε_0>0`. (Parcheable usando `/|ε_0|`, pero la estructura del fondo es RH-dependiente.) ⟹ III es condicional **también** a `ε_0>0`, además de (H-gap)+(H-lim).
- Esto **confirma y profundiza** que IV.2≡§V es el núcleo RH: no sólo el límite `ξ̂_∞=Ξ` es RH-equivalente; la **propia renormalización** que sostiene III lleva Weil-positividad. **[RESUELTO]:** conflación descartada (QW=Weil form, mismo objeto); heurístico refinado a
`g_0=Ξ_T+O(déficit)→Ξ_T` (límite, Landau–Beurling); y **destapado** que H1 sobre-afirma PSD
y que `/ε_0` asume `ε_0>0`=Weil. El relato no se cae (no hay crack lógico de conflación),
pero **la positividad de Weil aparece en más lugares de los que el cuadro admitía** (H1, III). --- ## Resumen de las tres | punto | resolución |
|---|---|
| **Normalización** | **RESUELTO**: `ξ̂_λ(0)=Ξ(0)`, Hurwitz-invariante; `Γ=O(1)` |
| **N5c-DH** | **RESUELTO a inputs**: real-rootedness (CCM auto-adjunta, no PF) + conv-eje (andamiaje E2.a) |
| **IV.2 conflación** | **descartada** (QW=Weil form); heurístico→límite; **hallazgo: H1 sobre-afirma PSD, `/ε_0` asume Weil≥0** | **Lo más valioso:** (a) la **conflación temida NO existe** — `ξ̂_λ` SÍ es el minimizador de
Weil, el relato es coherente. (b) Pero la auditoría destapó que **H1 sobre-afirma** ("PSD"
es RH, no PF) y que **la renormalización `/ε_0` asume Weil-positividad** — la RH-hardness
está más distribuida de lo que el cuadro mostraba. (c) Y se corrigió la **fuente de
real-rootedness**: es auto-adjunta/HB (vale para DH sin `Λ≥0`), **no** Perron–Frobenius —
lo que alinea con la reparación de E1.
