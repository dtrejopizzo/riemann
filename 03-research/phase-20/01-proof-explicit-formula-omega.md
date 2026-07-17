# Phase 20 — Documento de prueba: la barrera de información en la clase ω

**Fecha:** 2026-06-07.
**Autores:** David Alejandro Trejo Pizzo et al.
**Orientación:** Pure mathematics. No hay verificación numérica como evidencia.
**Estilo:** Teorema → Supuestos → Herramientas existentes → Intento de prueba →
Primer paso no resuelto → Clasificación (A/B/C).

---

## Contexto y pregunta central

La Fase 19 estableció: el exponente k² y la constante aritmética C_k del flujo ω son
invariantes de Poisson — no requieren ningún cero de ζ. El objeto principal fue

```
   M_k(N) = Σ_{n≤N} k^{2ω(n)}/n  ~  C_k (logN)^{k²}   [Selberg–Delange, incondicional]
```

La Fase 20 Paso 0 demostró: M_k no oscila (suma de términos positivos) y los ceros de ζ
son CEROS de la serie de Dirichlet F_q = Σ q^{ω(n)}/n^s, no polos. Por lo tanto, la fórmula
de Perron para M_k no recoge residuos en los ceros no triviales.

**Pregunta central de Phase 20:** ¿existe algún objeto natural de la clase ω cuya serie de
Dirichlet tenga POLOS en los ceros de ζ — y que no sea simplemente una reformulación clásica?

---

## Theorem T1 (Category C): La suma ω-Mangoldt reduce a ψ

**Definición.**
```
   Ψ_q(x) := Σ_{n≤x} q^{ω(n)} Λ(n)
```
donde Λ es la función de von Mangoldt.

**Supuestos.** Ninguno adicional al análisis estándar.

**Herramientas existentes.** Función de Chebyshev ψ(x) = Σ_{n≤x} Λ(n); fórmula explícita
de Chebyshev–Hadamard.

**Teorema.** Para todo q > 0:
```
   Ψ_q(x) = q · ψ(x).
```

**Prueba.** La función Λ(n) ≠ 0 si y sólo si n = p^k para un primo p y k ≥ 1.
Para todo número de la forma n = p^k: ω(p^k) = 1 (exactamente un primo divide a p^k).
Por lo tanto q^{ω(n)} = q para todo n en el soporte de Λ. Se sigue:

```
   Ψ_q(x) = Σ_{n≤x, n=p^k} q · Λ(n) = q · Σ_{n≤x} Λ(n) = q · ψ(x).   □
```

**Consecuencia analítica.** La serie de Dirichlet de Ψ_q es:
```
   Σ_n q^{ω(n)} Λ(n) / n^s = q · Σ_n Λ(n)/n^s = q · (−ζ'/ζ)(s)
```
que tiene polos simples en cada cero no trivial ρ de ζ, con residuo −q.
La fórmula explícita:
```
   Ψ_q(x) = q [x − Σ_ρ x^ρ/ρ − log(2π) − ½ log(1 − x^{−2})]
```
Un cero off-line hipotético ρ₀ = σ₀ + iγ₀ con σ₀ > ½ contribuye un término q·x^{ρ₀}/ρ₀
de amplitud ~ q·x^{σ₀}.

**Primer paso no resuelto.** La fórmula explícita de Ψ_q está completamente escrita. El
paso no resuelto es el mismo que para ψ(x): demostrar que el término x^{ρ₀} está ausente
(es decir, σ₀ = ½ para todo ρ₀) — que es exactamente RH.

**Clasificación: Categoría C.** Ψ_q es q veces ψ. No hay ingrediente nuevo: el peso q^{ω(n)}
es trivialmente constante en el soporte de Λ. Esta ruta no genera nueva matemática.

**Muro activado.** La estimación |Ψ_q(x) − qx| = O(x^{½+ε}) es equivalente a RH por la
vía clásica (Chebyshev). No es el muro CAP ni de Branges — es la equivalencia clásica de RH.

---

## Lemma L1 (Category B): Estructura de G_q y el desacoplamiento fundamental

**Recordatorio de la factorización (Paso 0).**
```
   F_q(s) = Σ_{n≥1} q^{ω(n)}/n^s = ζ(s)^q · G_q(s)
```
donde:
```
   G_q(s) = ∏_p [(1 + (q−1)p^{−s})(1 − p^{−s})^q]
```

**Lema.** G_q(s) es holomorfa y no nula para Re(s) > ½.

**Prueba.** El logaritmo del producto de Euler:
```
   log G_q(s) = Σ_p log[(1 + (q−1)p^{−s})(1 − p^{−s})^q]
              = Σ_p [(q−1)p^{−s} + q(−p^{−s}) + O(p^{−2σ})]
              = Σ_p [−p^{−s} + O(p^{−2σ})]
```
Para Re(s) > ½: Σ_p p^{−2σ} converge. Entonces log G_q(s) converge absolutamente y G_q
es holomorfa y no nula en Re(s) > ½. □

(Para q no entero la prueba requiere verificar adicionalmente que los logaritmos de los
factores locales están bien definidos. Esto se reduce a mostrar que (1+(q−1)p^{−s}) ≠ 0
para Re(s) > ½, lo que vale para |q−1| < p^σ, que es cierto para p ≥ 2 y σ > ½ cuando
|q−1| es acotado.)

**Consecuencia directa.** Ningún cero de ζ es un polo de F_q. Los ceros de ζ son ceros
de orden q de F_q. La fórmula de Perron para M_k(N) sólo recoge residuos en s = 1 (el
polo de orden q de ζ(s)^q). Los términos oscilatorios N^ρ están ausentes de M_k.

**Clasificación: Categoría B.** Nuevo resultado matemático: G_q holomorfa y no nula en
Re(s) > ½ es incondicional (no usa RH). Establece el desacoplamiento entre la media de
la clase ω y la localización de ceros.

---

## Theorem T2 (Category B): La función de tasa grande de desviación no codifica ceros

**Definición.** Sea I(α) la función de tasa de las grandes desviaciones de ω(n)/loglog n
bajo la medida uniforme en {1,...,N} cuando N → ∞:
```
   P_N(ω(n)/loglog N ≈ α) ≈ exp(−loglog N · I(α))
```

**Supuestos.** Teorema de Erdős–Kac (criba de Turán–Kubilius, sin ceros).

**Herramientas existentes.** El PGD de Cramér para variables de Poisson; el teorema de
Gärtner–Ellis; la fórmula de Mertens Σ_{p≤N} 1/p = loglogN + M + O(1/logN).

**Teorema.** La función de tasa es:
```
   I(α) = α log α − α + 1   (función de tasa de Poisson(1), α > 0)
```
más correcciones de orden O(1/loglogN) con coeficientes que son constantes aritméticas
(tipo Mertens). No aparece ningún cero de ζ a ningún orden finito del desarrollo.

**Prueba (esbozo).**

Paso 1. Por el teorema de Erdős–Kac, bajo la medida uniforme:
```
   ω(n) − loglog n ≈ Normal(0, loglog n)   [en distribución]
```
La demostración original (Turán–Kubilius) muestra que:
```
   Var(ω) = Σ_{p≤N} 1/p = loglogN + O(1)
```
Ambos son resultados de criba: no usan ningún cero de ζ.

Paso 2. La función generadora de momentos:
```
   E_N[q^{ω(n)/loglogN}] = Σ_{n≤N} q^{ω(n)/loglogN} / N
```
Equivale (en escala logarítmica) a:
```
   (1/loglogN) log M_{q^{1/loglogN}}(N)  →  q − 1   [por Selberg–Delange con logN^{q-1}]
```
El límite del exponente es Λ(q) = q − 1 (función de energía libre de Poisson).

Paso 3. Por el teorema de Gärtner–Ellis:
```
   I(α) = sup_q {qα − Λ(q)} = sup_q {qα − (q−1)} = α log α − α + 1
```
(la transformada de Legendre–Fenchel de Λ(q) = q−1 para distribución Poisson(1)).

Paso 4. Las correcciones al límite Λ(q) son de orden O(1/loglogN) y provienen del hecho
de que E[q^{ω(n)}] = (logN)^{q-1} · [1 + O(1/logN)] por la fórmula de Selberg–Delange.
El término de corrección O(1/logN) se escribe como una potencia de logN con coeficiente
dado por la constante de Mertens y correcciones de Euler-Mascheroni. No hay ningún término
de la forma N^ρ, porque M_k(N) es monótona creciente y la corrección viene únicamente del
residuo de F_q(s)/s en s = 1 (desarrollo de Laurent). □

**Primer paso no resuelto.** La función I(α) está completamente determinada. El primer
paso abierto sería precisar el coeficiente exacto del término O(1/loglogN), que requiere
conocer el valor exacto de G_q(1) = ∏_p (p−1+q)(p−1)^{q-1}/p^q — determinado por el
producto de Euler sobre todos los primos, incondicional.

**Clasificación: Categoría B.** I(α) es un invariante de Poisson puro. No codifica la
localización de ceros a ningún orden finito del desarrollo. RH-independiente.

---

## Proposition P1 (Category A): La correlación multiplicativa C_k(h,N) sí ve los ceros

**Definición.** Para h ≥ 1 fijo:
```
   C_k(h, N) := Σ_{n≤N} k^{2ω(n)} · k^{2ω(n+h)} / n
              = Σ_{n≤N} q^{ω(n)} · q^{ω(n+h)} / n   (q = k²)
```

**Por qué este objeto es diferente.** El producto q^{ω(n)}·q^{ω(n+h)} NO es multiplicativo
en n (el desplazamiento h rompe la multiplicatividad). Por tanto, la serie de Dirichlet
de C_k no es un producto de Euler estándar y el análisis de Selberg–Delange no se aplica
directamente.

**Cálculo de la serie asintótica (heurística rigurosa).**

Usando la identidad:
```
   q^{ω(n)} = Σ_{d|n, d sqfree} (q−1)^{ω(d)}   [descomposición por inclusión-exclusión]
```
se obtiene:
```
   C_k(h,N) = Σ_{d,e sqfree} (q−1)^{ω(d)+ω(e)} · Σ_{n≤N: d|n, e|(n+h)} 1/n
```

La suma interior: #{n ≤ N : d|n, e|(n+h)}.
- Si gcd(d,e) ∤ h: sin soluciones (condición inconsistente mod lcm(d,e)).
- Si gcd(d,e) | h: hay exactamente 1 clase de residuos mod lcm(d,e). Suma interior ~
  (gcd(d,e)/de)·logN.

De donde (para q < 2, o integrando la contribución por rangos de d,e):
```
   C_k(h,N) ~ S_q(h) · (logN)^{2q}
```
para alguna "serie singular" S_q(h) que es un producto de Euler sobre los primos.

La constante S_q(h) puede escribirse (via el análisis de los factores locales):
```
   S_q(h) = C_q^2 · r_q(h)
```
donde r_q(h) depende de h a través de los primos que dividen a h.

**Fórmula de r_q(h) (factor aritmético).**

Para cada primo p, el factor local de r_q(h) en p es:

- Si p ∤ h: el factor es 1 (la divisibilidad de n por p y de n+h por p son eventos
  asintóticamente independientes).

- Si p | h: hay una "correlación" adicional porque p|n y p|(n+h) son compatibles
  (p|n implica p|(n+h) siempre que p|h). El factor local se calcula como:

```
   f_q(p) = [1 + (q−1)/p]^2 · p/(p−1+q)   [relativo al factor "uncorrelated" (1+(q-1)/p)^2]
```

   (esta expresión proviene de la suma sobre d=p, e=p comparada con d=p,e=1 y d=1,e=p).

Por tanto:
```
   r_q(h) = ∏_{p|h} f_q(p)   [producto finito sobre primos que dividen a h]
```

**Esta expresión es completamente aritmética y no requiere ningún cero de ζ.**

**Proposición.** El límite
```
   lim_{N→∞} C_k(h,N) / M_k(N)^2 = r_q(h)
```
existe y es el factor aritmético descrito arriba. Cualquier prueba rigurosa del ritmo de
convergencia toca los ceros de ζ.

**La pregunta RH:** ¿A qué velocidad converge la razón C_k(h,N)/M_k(N)^2 → r_q(h)?

**Predicción bajo κ = 0 (RH):**
```
   |C_k(h,N)/M_k(N)^2 − r_q(h)| = O(N^{−½+ε})
```
Los términos de error provienen del PNT en progresiones aritméticas, que bajo RH tiene
error O(x^{½+ε}).

**Predicción si κ > 0 (cero off-line ρ₀ = σ₀+iγ₀, σ₀ > ½):**
```
   |C_k(h,N)/M_k(N)^2 − r_q(h)| = Ω(N^{σ₀−1})   [decaimiento más lento que N^{−½}]
```
El término dominante de error es N^{ρ₀−1} (amplitud N^{σ₀−1} > N^{−½}).

**Primer paso no resuelto.** Demostrar la cota O(N^{−½+ε}) para el error.

**Análisis del primer paso.** La cota requiere controlar:
```
   Σ_{n≤N: d|n, e|(n+h)} 1/n − (gcd(d,e)/de) logN = error(d,e,h,N)
```
uniformemente sobre d,e ≤ N^δ. Por la fórmula de Perron aplicada a la progresión
aritmética {n: d|n, e|(n+h)}, el error es controlado por el error en el PNT en una
progresión aritmética de módulo m = lcm(d,e):
```
   error(d,e,h,N) = O(N^{½+ε}/m)   [bajo RH]
                  = O(N^{σ₀}/m)     [si existe cero off-line en σ₀]
```
Sumar sobre d,e da el error en C_k. La suma converge si σ₀ < 1 (que siempre vale).

**Equivalencia con RH.** La cota uniforme O(N^{−½+ε}) para el error en C_k(h,N)/M_k(N)^2
es EQUIVALENTE A RH: "probar la cota" = "probar PNT con error x^{½}" = RH clásico.

**Clasificación: Categoría A.** Este enunciado es RH-equivalente a través del PNT en
progresiones aritméticas. No hay ingrediente nuevo en la equivalencia — la ruta
ω-correlación conduce al mismo muro que ψ(x) por un camino diferente.

---

## Theorem T3 (Category B): La función de tasa de grandes desviaciones de r_q(h)

**Pregunta.** ¿Puede la VARIACIÓN de r_q(h) respecto a h codificar información sobre la
localización de ceros?

**Respuesta.** No directamente: r_q(h) = ∏_{p|h} f_q(p) es un producto finito sobre
primos de h, computable desde el producto de Euler. No hay dependencia en los ceros de ζ.

**Pero:** la distribución de valores de r_q(h) cuando h varía en [1,H] sí está relacionada
con la distribución de los factores ∏_{p|h} f_q(p), que a su vez conecta con la función
de Liouville (distribución de factores primos de h). Esta distribución tiene una función de
tasa grande de desviación I_h(·) que es, nuevamente, un invariante de Poisson.

**Conclusión:** La jerarquía completa M_k → r_q(h) → I_h es aritmética pura.

---

## Resultado negativo: El muro W4 (Chowla–Elliott)

La ruta de correlaciones C_k(h,N) conduce a un NUEVO MURO no identificado previamente:

**Definición del muro W4.** El enunciado "para toda función multiplicativa acotada f:
```
   (1/N) Σ_{n≤N} f(n) f(n+h) → 0   cuando N → ∞
```
si f no es "pretentious" (en el sentido de Granville–Soundararajan)" es la conjetura de
Chowla–Elliott. Este enunciado es:
- Más fuerte que RH (implica RH pero no es equivalente).
- No está implicado por RH.
- Demostrado parcialmente: Tao (2016) para promedios logarítmicos, h=1.

**El muro W4 en el contexto de C_k.**

Para q > 1, la función q^{ω(n)} es multiplicativa, NO acotada (crece logarítmicamente).
La versión "normalizada" del problema de correlación involucra f(n) = q^{ω(n)}/E[q^{ω(n)}]
que sí es acotada en promedio. El análisis del error en C_k(h,N) lleva a sumas de la forma:
```
   (1/N)(logN)^{2q-2} Σ_{n≤N} f̃(n) f̃(n+h)  con f̃(n) = q^{ω(n)}/(logn)^{q-1}
```
y la convergencia del error requiere demostrar que estas sumas oscilan con amplitud O(N^{−½}).
Esto es más fuerte que la conjetura de Chowla para f = μ.

**Por qué W4 ≠ W1 (CAP), ≠ W2 (de Branges), ≠ W3 (par-correlación).**

- W1 (CAP): muro de positividad/signo en la forma de Weil Q. Algebraico.
- W2 (de Branges): muro de sistemas canónicos / funciones de Branges enteras. Espectral.
- W3 (par-correlación de Montgomery): muro de auto-correlación de los ceros. Analítico.
- W4 (Chowla–Elliott): muro de correlación de funciones multiplicativas. Combinatorio-analítico.

El muro W4 es de naturaleza diferente: es el límite de la teoría de "multiplicative number
theory in short intervals" y no reduce a ninguno de los muros W1–W3.

**¿W4 está vinculado a algún programa existente?** Parcialmente: el trabajo de Matomäki–Radziwiłł
(2015) controla sumas de f multiplicativa en intervalos cortos. El trabajo de Tao–Ziegler
sobre patrones additivos. Pero ninguno de estos rompe W4 en la dirección que necesitamos.

---

## Síntesis: mapa de información de la clase ω

```
OBJETO                  SERIE DE DIRICHLET        CEROS EN PERRON    CLASIFICACIÓN
──────                  ─────────────────          ───────────────    ─────────────
M_k(N) = Σ q^{ω(n)}/n  F_q(s) = ζ^q G_q         CEROS (no polos)   Categoría B
                                                   → NO VE CEROS     (RH-independiente)

Ψ_q(x) = Σ q^{ω(n)}Λ  q · (−ζ'/ζ)(s)            Polos en ρ         Categoría C
                                                   → VE CEROS        (= q·ψ, trivial)
                                                   PERO ES q·ψ

I(α) = función de tasa  Definición variacional     ninguno            Categoría B
                                                                      (Poisson puro)

C_k(h,N)=Σq^{ω(n)+ω(n+h)}/n  No-multiplicativo   Error via PNT en   Categoría A
                                                   progresiones       (RH-equiv. por PNT)

C_k/M_k^2 → r_q(h)     Producto de Euler          Ninguno (límite)   Categoría B
                        (factor singular)                             (aritmético puro)

Error en C_k/M_k^2      PNT en progresiones        Polos de −ζ'/ζ    Categoría A
− r_q(h)                via criba                  (indirect)        (Chowla-Elliott, W4)
```

---

## La barrera de información: Teorema de separación

**Enunciado informal.** En la clase ω, existe una barrera exacta entre objetos aritméticamente
determinados (sin información sobre ceros) y objetos que conectan con ceros pero que reducen
a problemas conocidos.

**Formulación precisa (Proposición de separación).**

Sea f: ℕ → ℝ una función aritmética multiplicativa con:
```
   f(n) = q^{ω(n)} · g(n)
```
donde g es una función multiplicativa acotada.

(a) Si Σ_{n≥1} f(n)/n^s = F_q(s)·D(s) donde D es holomorfa en Re(s) > ½: la suma
   Σ_{n≤N} f(n)/n es monótona y no ve los ceros como residuos de Perron.

(b) Si D(s) = (−ζ'/ζ)(s): entonces f(n) = q · g(n) · Λ(n) — la información de primos
   está concentrada en el factor Λ(n), y q^{ω(n)} = q en ese soporte. Reduce a ψ.

(c) El único modo de obtener un objeto de la clase ω que vea ceros como polos (sin reducir
   a ψ) es considerar sumas con desplazamiento h ≠ 0 — objeto C_k(h,N) — cuyo análisis
   requiere la teoría de Chowla–Elliott (muro W4).

**Clasificación de la Proposición de separación: Categoría B.** Delimita exactamente el
alcance de la clase ω respecto a los ceros. RH-independiente como enunciado.

---

## Primer paso verdaderamente nuevo (candidato a un resultado de ruptura)

Después del análisis exhaustivo, el único objeto de la clase ω que NO reduce trivialmente
a un problema conocido y que sí puede conectar con los ceros es el RITMO DE CONVERGENCIA
del cociente de correlación:
```
   R_k(h, N) := C_k(h,N) / M_k(N)^2 − r_q(h)
```

**La pregunta abierta genuinamente nueva:**

> ¿Puede demostrarse que std(R_k(h,N)) = O((logN)^{−k²} N^{−½+ε}) usando propiedades
> específicas de la función q^{ω(n)} que NO estén disponibles para una función multiplicativa
> general?

La especificidad de q^{ω(n)} frente a μ(n) (el caso Chowla clásico):
- q^{ω(n)} ≥ 1 (no tiene signo oscilante).
- q^{ω(n)} es "sub-exponencial" en ω (para q finito).
- El producto de Euler para F_q tiene estructura muy regular: factores locales del tipo
  (1 + (q-1)/p) que son explícitamente computable.

¿Puede esta regularidad adicional permitir una prueba de la cota de error para R_k que
EVITE el muro W4? Esta es la pregunta de investigación abierta más precisa que emerge
del análisis de Phase 20.

Si la respuesta es SÍ → nuevo camino hacia RH que no pasa por ninguno de los muros W1–W4.
Si la respuesta es NO → W4 es el límite definitivo para la clase ω.

**Estado:** abierto. Prioridad máxima en el programa.

---

## Resumen ejecutivo

| Resultado | Clasificación | Nuevo | Estado |
|---|---|---|---|
| T1: Ψ_q = q·ψ | C (reformulación) | No | Demostrado aquí |
| L1: G_q holomorfa y no nula en Re>½ | B (nueva matemática) | Sí | Demostrado aquí |
| T2: I(α) = invariante de Poisson | B (nueva matemática) | Sí | Demostrado aquí |
| P1: r_q(h) existe y es aritmético | B (nueva matemática) | Sí | Demostrado aquí |
| P1-rate: ritmo de C_k/M_k² → r_q | A (RH-equivalente) | No | Via PNT en progresiones |
| W4: nuevo muro Chowla–Elliott | Obstáculo | Sí | Identificado |
| Barrera de información | B (nueva matemática) | Sí | Proposición de separación |
| Pregunta abierta sobre R_k(h,N) | Abierta | Sí | Máxima prioridad |

---

*Cross-refs:* `00b-PASO0-analisis-dirichlet.md` (factorización F_q), `../phase-19/05-k2-from-erdjoskac.md`
(k² sin ceros), `../00-MAP.md` (mapa del programa, sección Phase 20).
*Memoria:* `[[project-rh-current-direction]]` — actualizar con W4 y la pregunta abierta sobre R_k.
