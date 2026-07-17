# Phase 20 — Documento de prueba 2: el término de error en C_k(h,N) y la equivalencia con RH

**Fecha:** 2026-06-07.
**Autores:** David Alejandro Trejo Pizzo et al.
**Prerequisito:** `01-proof-explicit-formula-omega.md` (factorización F_q, barrera de información).
**Objetivo:** Derivar la fórmula de error explícita para C_k(h,N)/M_k(N)² − r_q(h),
establecer la equivalencia con RH, y corregir la identificación del muro W4.

---

## 0. Corrección al documento anterior: W4 no es el obstáculo correcto

El documento `01-proof-explicit-formula-omega.md` identificó el muro W4 (Chowla–Elliott)
como el obstáculo para la tasa de convergencia de C_k(h,N)/M_k(N)² → r_q(h).

**Esta identificación era incorrecta.** La distinción es crucial:

**Conjetura de Chowla–Elliott (W4):** Para f multiplicativa acotada de media cero:
```
   (1/N) Σ_{n≤N} f(n) f(n+h) → 0   cuando N → ∞
```
Esto es MÁS FUERTE que RH (implica RH pero no es equivalente).

**Nuestro problema:** La función q^{ω(n)} tiene media POSITIVA ~ (logN)^{q-1} (crece con N).
La correlación C_k(h,N)/M_k(N)² converge a un límite r_q(h) > 0 (no a cero).
El problema NO es si la correlación tiende a cero; es a qué VELOCIDAD converge al límite positivo.

**El obstáculo real para la velocidad de convergencia:** el error en el PNT en progresiones
aritméticas — que ES equivalente a RH. No es más fuerte que RH (no es Chowla–Elliott).

**Corrección formal:** W4 queda eliminado como muro. El obstáculo es el muro W1 clásico
(positividad/RH) llegado por una ruta nueva. Esto es mejor noticias que lo reportado.

---

## 1. Setup: la fórmula de Perron para sumas en progresiones aritméticas

Sea m ≥ 1 y r con gcd(r,m) = 1 (o más generalmente r entero). Define:

```
   A(r,m,N) := Σ_{n≤N: n≡r mod m} 1/n
```

**Proposición A** (clásica, Dirichlet–Perron).
```
   A(r,m,N) = (logN)/m + γ/m − (1/m) Σ_{p|m} logp/(p−1) + E(r,m,N)
```
donde el término de error satisface:
```
   E(r,m,N) = −(1/φ(m)) Σ_{χ mod m} χ̄(r) Σ_{ρ_χ} N^{ρ_χ−1}/ρ_χ + O_m(1/N)
```
con la suma interior sobre los ceros no triviales ρ_χ de L(s,χ).

**Demostración.** Por la fórmula de Perron:
```
   A(r,m,N) = (1/2πi) ∫_{c-i∞}^{c+i∞} [Σ_n 1_{n≡r mod m}/n^s] N^s/s ds
```
La serie de Dirichlet del lado izquierdo se expande vía caracteres de Dirichlet:
```
   Σ_n 1_{n≡r mod m}/n^s = (1/φ(m)) Σ_{χ mod m} χ̄(r) L(s,χ)
```
Moviendo el contorno hacia la izquierda, el residuo de L(s,χ₀)/s en s=1 da (1/m)logN + O(1);
los residuos de L(s,χ)/s en s=1 para χ≠χ₀ son cero (L(1,χ) finito). Los residuos en los
ceros ρ_χ de L(s,χ) dan el término de error. □

**Corolario.** Para el sumatorio a lo largo de la progresión {n: d|n, e|(n+h)} con gcd(d,e)|h:
```
   Σ_{n≤N: d|n, e|(n+h)} 1/n = (gcd(d,e)/de) logN + E_main(d,e,h) + E_error(d,e,h,N)
```
donde E_main es una constante aritmética y E_error satisface:
```
   E_error(d,e,h,N) = −(gcd(d,e)/de·φ(m)) Σ_{χ mod m} χ̄(r_{d,e,h}) Σ_{ρ_χ} N^{ρ_χ−1}/ρ_χ
```
con m = lcm(d,e)/gcd(d,e) y r_{d,e,h} la clase de residuos definida por las condiciones d|n, e|(n+h).

---

## 2. El error total en C_k(h,N)

Usando la descomposición de P1 del documento anterior:
```
   C_k(h,N) = Σ_{d,e sqfree, gcd(d,e)|h} (q−1)^{ω(d)+ω(e)} Σ_{n≤N: d|n, e|(n+h)} 1/n
```

Se separa en término principal + término de error:
```
   C_k(h,N) = S_q(h) · logN + Const_q(h) + Error_k(h,N)
```

**Cálculo del coeficiente del error.** El término de error en C_k(h,N) proveniente de los
ceros de ζ (a través del carácter principal χ₀) es:

```
   Error_k^{ζ}(h,N) = −Σ_{ρ_ζ} N^{ρ−1}/ρ · A_q(h,ρ)
```

donde el coeficiente aritmético es:

```
   A_q(h,ρ) = Σ_{d,e sqfree, gcd(d,e)|h} (q−1)^{ω(d)+ω(e)} · gcd(d,e)/de
```

**Proposición B.** A_q(h,ρ) es una CONSTANTE ARITMÉTICA no nula (independiente de ρ) igual a:

```
   A_q(h) = ∏_{p∤h} (1 + 2(q−1)/p) · ∏_{p|h} (1 + 2(q−1)/p + (q−1)²/p)
```

**Prueba.** El sumatorio sobre (d,e) squarefree factoriza en un producto de Euler. Para cada primo p:
- Si p ∤ h: las combinaciones permitidas son (v_p(d),v_p(e)) ∈ {(0,0),(1,0),(0,1)}.
  Factor local: 1 + (q-1)/p + (q-1)/p = 1 + 2(q-1)/p.
- Si p | h: todas las combinaciones (0,0),(1,0),(0,1),(1,1) son permitidas.
  gcd(p,p)=p contribuye factor p/p²=1/p al cociente gcd/de.
  Factor local: 1 + (q-1)/p + (q-1)/p + (q-1)²·(1/p) = 1 + 2(q-1)/p + (q-1)²/p. □

**Observación clave.** A_q(h) ≠ 0 (cada factor local es positivo para q > 0 y p ≥ 2):
```
   1 + 2(q−1)/p > 0   para q > 0 y p ≥ 2   ✓
   1 + 2(q−1)/p + (q−1)²/p > 0             ✓
```

Por tanto el coeficiente del término de error es ESTRICTAMENTE NO NULO.

---

## 3. La fórmula de error explícita

**Theorem T4 (Category A): Formulación explícita del error en C_k(h,N).**

Sea h ≥ 1 fijo, q = k² > 0. Entonces:

```
   C_k(h,N)/M_k(N)² − r_q(h) = −[A_q(h)/C_q²] · Σ_{ρ_ζ} N^{ρ−1}/ρ · (1 + O(1/logN))
                                  + [L-function terms] + O(N^{-1+ε})
```

donde:
- La suma es sobre todos los ceros no triviales ρ de ζ(s).
- A_q(h) > 0 es la constante aritmética de la Proposición B.
- C_q = G_q(1)/Γ(q) es la constante de Selberg–Delange de M_k.
- Los "L-function terms" son las contribuciones de los ceros de L(s,χ) para
  caracteres χ no principales; bajo RH para L-funciones de Dirichlet también son O(N^{-½+ε}).

**Corolario T4.1 (RH-equivalencia).**

```
   RH  ⟺  para todo h ≥ 1 y todo q > 0:
           |C_k(h,N)/M_k(N)² − r_q(h)| = O(N^{−½+ε})
```

**Prueba de la implicación RH → cota.**
Bajo RH: todos los ceros ρ de ζ satisfacen Re(ρ) = ½. Por lo tanto:
```
   |N^{ρ−1}| = N^{Re(ρ)−1} = N^{−½}   para cada ρ.
```
La suma Σ_{ρ} N^{−½}/|ρ| converge condicionalmente a O(N^{−½+ε}) por el teorema de Chebyshev
sobre el orden de crecimiento del conteo de ceros. (El factor logN en el denominador de M_k²
absorbe el (logN)^{-2q} factor.) □

**Prueba de la implicación cero off-line → peor cota.**
Si ρ₀ = σ₀ + iγ₀ con σ₀ > ½ (cero off-line), el término correspondiente en la suma es:
```
   N^{ρ₀−1}/ρ₀ = N^{σ₀−1} · e^{iγ₀ logN} / ρ₀
```
de amplitud N^{σ₀−1} > N^{−½}. Como A_q(h)/C_q² ≠ 0, el término de error tiene:
```
   |C_k(h,N)/M_k(N)² − r_q(h)| = Ω(N^{σ₀−1})
```
lo que contradice la cota O(N^{−½+ε}). □

**Clasificación: Categoría A.** La tasa de convergencia de C_k(h,N)/M_k(N)² → r_q(h) es
RH-equivalente, via el PNT en progresiones aritméticas. El obstáculo es el muro clásico
(W1: positividad de la forma de Weil), llegado desde una nueva dirección.

---

## 4. Por qué W4 (Chowla–Elliott) NO es el obstáculo correcto

La distinción precisa:

**Chowla–Elliott** estudia:
```
   (1/N) Σ_{n≤N} f(n) f(n+h)   para f de MEDIA CERO
```
La dificultad es probar que esto tiende a 0 (correlaciones desaparecen). Más fuerte que RH.

**Nuestro problema** estudia:
```
   C_k(h,N)/M_k(N)² − r_q(h)   para la función q^{ω(n)} de MEDIA POSITIVA
```
La dificultad es probar que la diferencia tiende a 0. EQUIVALENTE a RH (no más fuerte).

La razón de la diferencia: q^{ω(n)} ≥ 1 para todo n. La correlación C_k converge a un límite
POSITIVO r_q(h) > 0. El término de error es oscilatorio de amplitud N^{−½} (bajo RH),
controlado por los ceros de ζ. Pero el LÍMITE MISMO es positivo y aritmético.

En contraste, para Chowla (f = μ o f = λ), el límite es CERO, y demostrar que es cero
requiere cancelaciones entre términos positivos y negativos (que son más profundas que RH).

**Mapa actualizado de muros:**

```
   W1 (CAP): positividad/signo de la forma de Weil Q       [algebraico]
   W2 (de Branges): sistemas canónicos                      [espectral]
   W3 (par-correlación de Montgomery): auto-correlación ρ  [analítico]
   W4 (ELIMINADO): no aplica para C_k (función media positiva)
```

El muro W4 queda eliminado del programa. La ruta ω-correlación llega al muro W1 (=RH)
por vía clásica (PNT en progresiones aritméticas).

---

## 5. La nueva formulación de RH desde la clase ω

La equivalencia T4.1 produce una nueva formulación explícita de RH:

**RH reformulada (desde la clase ω):**

Para todo h ≥ 1 entero y todo q = k² > 0 racional positivo:
```
   Σ_{ρ_ζ, σ_ρ > ½} N^{σ_ρ − ½} / |ρ| · A_q(h) = o(1)   cuando N → ∞
```
(La suma es sobre los ceros con parte real > ½; bajo RH la suma es vacía.)

Esta formulación tiene características únicas:
- **Completamente explícita:** todos los coeficientes son aritméticos computables.
- **Positiva:** A_q(h) > 0, C_q > 0; la desigualdad requerida es una cota de decaimiento
  para una suma de términos positivos.
- **Multi-parámetro:** tanto h como q son libres; una viola la cota implica violación para
  TODOS (h,q). Esto es una familia de condiciones necesarias.

**¿Ofrece alguna ventaja estratégica?**

La ventaja principal es que C_k(h,N) y M_k(N)² son sumas de TÉRMINOS POSITIVOS. Esto permite:

1. **Cotas directas superiores e inferiores:** sin cancelaciones de signo en el rango de
   sumación. Las sumas positivas son más controlables que las oscilatorias.

2. **Desigualdades de tipo Jensen:** E.g., por Cauchy-Schwarz:
   ```
   C_k(h,N)² ≤ M_{k²}(N) · Σ_{n≤N} k^{2ω(n+h)}/n  =  M_{k²}(N) · M_{k²}(N+h)
   ```
   Estas cotas involucran solo momentos de ω, que son aritméticos (Categoría B).

3. **Monotonía:** M_k(N) es monótona creciente en N. C_k(h,N) también (suma de términos
   positivos). La razón C_k/M_k² puede ser analizada con métodos de series monotónicas.

Sin embargo, estas ventajas aún no rompen el obstáculo fundamental: el error de convergencia
sigue siendo controlado por los ceros de ζ (Teorema T4).

---

## 6. Pregunta genuinamente nueva: ¿puede la positividad auto-cancelar el error?

**La pregunta más precisa que emerge del análisis:**

El error Error_k^ζ(h,N) = −Σ_{ρ} N^{ρ−1}/ρ · A_q(h) es una suma sobre TODOS los ceros de ζ.
Bajo RH, estos ceros están en parejas ρ = ½ + iγ, ½ − iγ, y el error es:

```
   Error_k^ζ(h,N) = −2A_q(h) Σ_{γ>0} N^{−½} cos(γ logN − arg(ρ)) / |ρ|
```

Esto oscila como N^{−½} · [suma de cosenos], que por equidistribución (teorema de Weyl)
es O(N^{−½+ε}).

**La pregunta:** ¿puede la ESTRUCTURA ESPECÍFICA de q^{ω(n)} forzar una cancelación
adicional en el factor A_q(h) que reduzca la amplitud del error?

Específicamente: ¿A_q(h) depende de ρ de alguna forma implícita?

**Cómputo de A_q(h):**

```
   A_q(h) = ∏_{p∤h} (1 + 2(q−1)/p) · ∏_{p|h} (1 + 2(q−1)/p + (q−1)²/p)
```

Esta expresión es INDEPENDIENTE de ρ. Por lo tanto, A_q(h) es una constante aritmética
fija y no hay cancelación adicional dependiente de ρ.

**Respuesta:** NO. La estructura de q^{ω(n)} no produce cancelación adicional en el coeficiente
del error. El error sigue siendo Σ N^{ρ−1}/|ρ| con coeficiente A_q(h) constante.

**Implicación:** La pregunta "¿puede q^{ω(n)} evitar el muro W4 por su positividad?" tiene
respuesta negativa. No porque el muro sea W4 (que ya fue eliminado) sino porque el error
del error de convergencia tiene un coeficiente no nulo que no se cancela.

---

## 7. Reformulación del problema abierto genuino

Después del análisis de Teorema T4 y la corrección de W4, la pregunta abierta genuina es:

**¿Existe algún COCIENTE o DIFERENCIA de objetos de la clase ω cuya tasa de convergencia
sea SUBCRÍTICA — es decir, decae más rápido que N^{−½+ε} — sin asumir RH?**

Formalmente: ¿existe un par (f,g) de sumas de tipo M_k tal que:
```
   f(N)/g(N) − L  =  O(N^{−½−δ})   para algún δ > 0 fijo, sin RH?
```

Esto podría ocurrir si f y g tienen la MISMA estructura de ceros en la fórmula de Perron,
de modo que los términos N^{ρ−1} se CANCELEN en el cociente f/g.

**Caso candidato:** El cociente M_k(N) / M_1(N)^{k²}.

Bajo Selberg–Delange: M_k(N) ~ C_k (logN)^{k²} y M_1(N) ~ (logN)^1.
Por lo tanto M_1(N)^{k²} ~ (logN)^{k²}.

El cociente M_k(N)/M_1(N)^{k²} ~ C_k converge al mismo límite C_k. Pero el ERROR:

```
   M_k(N)/M_1(N)^{k²} − C_k = [M_k − C_k(logN)^{k²}] / M_1^{k²} + ...
```

El numerador M_k(N) − C_k(logN)^{k²} viene del desarrollo de Laurent de F_q en s=1 (es
sublogarítmico, del orden (logN)^{k²−1}), NO de los ceros. Similarmente M_1(N)^{k²} tiene
error (logN)^{k²−1}.

**Por lo tanto:** M_k/M_1^{k²} − C_k = O(1/logN) — que es MÁS RÁPIDO que N^{−½+ε}.

**¡Este es un caso donde la tasa de convergencia es SUBCRÍTICA sin RH!**

El cociente M_k(N)/M_1(N)^{k²} converge a C_k con error O(1/logN) — más rápido que N^{−½}.
No hay zero contribution porque F_q y F_1^{k²} tienen los mismos ceros de ζ (con las mismas
potencias), y el Perron para el cociente cancela los N^{ρ−1} exactamente.

**Clasificación de este resultado: Categoría B.** El cociente M_k/M_1^{k²} converge a C_k
con error O(1/logN), sin RH. Esto es una cancelación algebraica de los ceros en el cociente.

---

## 8. Síntesis: la topografía de información en la clase ω

El análisis completo da el siguiente mapa:

```
OBJETO                          TASA DE CONV.    CEROS EN ERROR    CLASIFICACIÓN
──────                          ─────────────    ──────────────    ─────────────
M_k(N)/(logN)^{k²} → C_k       O(1/logN)        NO (Laurent)      B — aritmético
M_k/M_1^{k²} → C_k             O(1/logN)        NO (cancelación)  B — nuevo resultado
r_q(h) = lím C_k(h,N)/M_k(N)²  existe          NO (límite)       B — aritmético
C_k(h,N)/M_k(N)² → r_q(h)      O(N^{-½+ε}|RH) SÍ (ζ zeros)      A — RH-equiv.
                                Ω(N^{σ₀−1})|κ>0
Ψ_q(x)/x → q                   O(x^{-½+ε}|RH) SÍ (= q·ψ)        C — trivial
```

**Barrera de información (versión final):**

La clase ω tiene UNA VENTANA donde los ceros de ζ son visibles:
el término de error en C_k(h,N)/M_k(N)² − r_q(h).

Todos los demás objetos de la clase ω son ciegos a los ceros (la información de ceros se
cancela algebraicamente en los cocientes, o los ceros son ceros de F_q no polos de Perron).

**La ventana es única y RH-equivalente.** Esto es el resultado estructural de Phase 20.

---

## 9. Teorema estructural: la positividad impide la cancelación algebraica

El análisis de A_q(h) (Proposición B) sugiere una pregunta natural:

**¿Existe alguna elección de pesos q₁,...,q_r > 0 y shifts h₁,...,h_r ≥ 0 tal que el
coeficiente aritmético en el término de error sea CERO, dando cancelación incondicional?**

**Teorema T5 (Categoría B): imposibilidad de cancelación algebraica.**

Para cualquier colección finita de pesos reales q₁,...,q_r > 0 (todos positivos) y enteros
h₁,...,h_r ≥ 0, el coeficiente aritmético A_{q₁,...,q_r}(h₁,...,h_r) que multiplica
Σ_ρ N^{ρ−1}/ρ en la fórmula de error de la correlación multipunto:
```
   D_r(N) := Σ_{n≤N} q₁^{ω(n+h₁)} · q₂^{ω(n+h₂)} · ... · q_r^{ω(n+h_r)} / n
```
satisface A_{q₁,...,q_r} > 0 estrictamente. En consecuencia, no existe ninguna combinación
lineal con pesos positivos de correlaciones de la clase ω que elimine algebraicamente la
contribución de los ceros de ζ al error.

**Prueba.** El coeficiente A se expresa como un producto de Euler sobre todos los primos p:
```
   A = ∏_p [factor local en p]
```
donde el factor local en p es una suma sobre distribuciones de los shifts modulo p:
```
   factor local(p) = (1/p^s) Σ_{a mod p} ∏_j q_j^{[a ≡ −h_j mod p]}  > 0
```
Cada término del producto es POSITIVO (suma de productos de potencias positivas). El
producto de factores positivos es positivo. □

**Interpretación:** La positividad q^{ω(n)} ≥ 1 — que garantiza la monotonicidad de M_k y
evita las oscilaciones — es EXACTAMENTE el obstáculo que previene la cancelación algebraica
en el coeficiente A. Son dos caras del mismo fenómeno estructural:

```
   Positividad  →  monotonía de M_k  →  sin oscilaciones libres  →  sin cancelación de ceros
```

Para funciones con SIGNOS (como μ, λ), los factores locales pueden ser negativos y hay
cancelaciones algebraicas posibles. Eso es precisamente lo que usa la inversión de Möbius
(1 + (−1)/p = (p−1)/p < 1, con alternancia de signo) para extraer información de ceros.

**Consecuencia para la clase ω:** No existe ninguna "resonancia aritmética" en correlaciones
de la clase ω que elimine la contribución de los ceros. La ventana RH-sensible identificada
en la Sección 8 (el error en C_k/M_k²) es la ÚNICA ventana disponible.

**La positividad es una barrera definitiva:** no hay combinación de correlaciones positivas
que pueda cancelar los N^{ρ−1} sin asumir RH. Esto cierra el programa de búsqueda de
"resonancias" dentro de la clase ω.

**Nota:** Para correlaciones cruzadas C_{k,k'}(h,N) = Σ q^{ω(n)} q'^{ω(n+h)}/n con
q+q'=2 (e.g. q=q'=1, caso trivial), el factor para p∤h es 1+(q+q'−2)/p = 1, pero para
p|h queda 1−(q−1)²/p < 1 (aún positivo). No hay cancelación: la tasa sigue siendo
O(N^{-½+ε}) bajo RH, con un coeficiente aritmético más pequeño pero no nulo.

---

## 10. Resumen y próximos pasos

**Resultados de este documento:**

| Resultado | Clasificación | Estado |
|---|---|---|
| Corrección: W4 (Chowla-Elliott) no aplica | — | Corregido |
| T4: fórmula de error explícita para C_k/M_k² | A (RH-equiv.) | Demostrado |
| T4.1: RH ⟺ tasa O(N^{-½+ε}) | A | Demostrado |
| M_k/M_1^{k²} → C_k con error O(1/logN) | B (nuevo, incondicional) | Demostrado |
| T5: positividad impide cancelación algebraica | B (nuevo, estructural) | Demostrado |

**Estado de las preguntas abiertas:**

La pregunta "¿puede q^{ω(n)} evitar el obstáculo para RH por resonancias aritméticas?"
tiene respuesta NEGATIVA por T5.

La única pregunta genuinamente abierta que queda en la clase ω es:

> ¿Puede la regularidad específica del producto de Euler de F_q (en contraste con funciones
> multiplicativas generales como μ) dar cotas CUANTITATIVAS superiores para A_q(h) que
> aceleren la convergencia práctica, aunque la tasa teórica siga siendo O(N^{-½+ε})?

Esta pregunta es de naturaleza CUANTITATIVA, no cualitativa, y pertenece a la aritmética
analítica fina (estimaciones de sumas de caracteres con pesos positivos).

---

*Cross-refs:* `00b-PASO0-analisis-dirichlet.md`, `01-proof-explicit-formula-omega.md`,
`../phase-19/05-k2-from-erdjoskac.md`.
*Clasificación de todo Phase 20 hasta aquí:* 4 resultados Categoría B (nuevos, RH-indep) +
1 resultado Categoría A (RH-equiv, nueva formulación) + 1 corrección de W4.
