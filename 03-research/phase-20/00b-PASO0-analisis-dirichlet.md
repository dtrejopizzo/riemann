# Phase 20 — Paso 0: análisis de la serie de Dirichlet de q^{ω(n)}

**Fecha:** 2026-06-07.
**Propósito:** Determinar rigurosamente qué singularidades controlan M_k(N) y sus fluctuaciones,
ANTES de diseñar experimentos. Esto responde a la advertencia del advisor: sin este análisis,
los Experimentos 1–3 del diseño inicial pueden estar buscando señales que matemáticamente no existen.

---

## 1. La serie de Dirichlet exacta

El producto de Euler para q^{ω(n)} es bien conocido:

```
         ∞
F_q(s) = Σ  q^{ω(n)} / n^s
        n=1

       = ∏_p  (1 + q·p^{-s} + q·p^{-2s} + ...)
         [cada primo p contribuye: ω(p^k) = 1 para k ≥ 1, y ω(1) = 0]

       = ∏_p  (1 + q·p^{-s}/(1 − p^{-s}))

       = ∏_p  (1 − p^{-s} + q·p^{-s}) / (1 − p^{-s})

       = ∏_p  (1 + (q−1)·p^{-s}) / (1 − p^{-s})
```

Factorizando con ζ(s) = ∏_p (1 − p^{-s})^{−1}:

```
F_q(s) = ζ(s) · ∏_p (1 + (q−1)·p^{-s})
```

**Verificación:** para q = 1: F_1(s) = ζ(s) · ∏_p 1 = ζ(s) ✓ (q^{ω(n)} = 1 para todo n → F_1 = ζ).

---

## 2. La factorización de Selberg–Delange

La forma que aparece en el teorema de Selberg–Delange es:

```
F_q(s) = ζ(s)^q · G_q(s)
```

donde G_q(s) es holomorfa y NO nula en Re(s) > 1/2.

Derivación explícita:

```
F_q(s) = ζ(s) · ∏_p (1 + (q−1)p^{-s})

       = ζ(s)^q · ζ(s)^{1-q} · ∏_p (1 + (q−1)p^{-s})

       = ζ(s)^q · G_q(s)
```

donde:

```
G_q(s) = ζ(s)^{1-q} · ∏_p (1 + (q−1)p^{-s})

        = ∏_p  [(1 + (q−1)p^{-s}) · (1 − p^{-s})^q]
```

(usando ζ(s)^{1-q} = ∏_p (1−p^{-s})^{q-1} en el producto de Euler).

**Propiedad clave de G_q(s):**

- Para Re(s) > 1/2, cada factor del producto es (1 + (q−1)p^{-s})(1−p^{-s})^q = 1 + O(p^{-2σ}).
- El producto converge absolutamente en Re(s) > 1/2.
- G_q no se anula en Re(s) > 1 (convergencia absoluta del Euler product).
- Bajo RH, G_q no se anula en Re(s) > 1/2.

---

## 3. La pregunta crítica: ¿dónde entran los ceros de ζ?

La fórmula de Perron da:

```
M_k(N) = Σ_{n≤N} q^{ω(n)}/n = (1/2πi) ∫_{c-i∞}^{c+i∞} F_q(s)/s · N^s ds
```

Al mover el contorno hacia la izquierda de Re(s) = 1, los residuos vienen de los POLOS de F_q(s)/s.

**¿F_q(s)/s tiene polos en los ceros no triviales ρ de ζ?**

- ζ(ρ) = 0 → ζ(s)^q tiene un CERO de orden q en ρ.
- G_q(ρ) ≠ 0 (holomorfa y no nula).
- Por tanto F_q(ρ) = ζ(ρ)^q · G_q(ρ) = 0.

**F_q tiene CEROS en ρ, NO polos.**

La fórmula de Perron recoge residuos de POLOS solamente.

→ **Los ceros no triviales de ζ NO contribuyen residuos en la fórmula de Perron para M_k(N).**

Los únicos polos son:
- s = 1 (polo de orden q = k² de ζ(s)^q): da el término principal C_k(logN)^{k²}.
- s = 0 (polo simple de 1/s): contribución pequeña, O(1).
- No hay otros.

---

## 4. Consecuencia directa: M_k(N) es MONÓTONA

Dado que q^{ω(n)}/n > 0 para todo n ≥ 1:

```
M_k(N) = Σ_{n=1}^{N} q^{ω(n)}/n   es ESTRICTAMENTE CRECIENTE en N.
```

No puede oscilar. No hay términos oscilatorios N^ρ. M_k(N) sube monotónamente hacia su asíntota.

**Las "fluctuaciones" de R_k(N) = M_k(N)/(logN)^{k²} son SIEMPRE NEGATIVAS:**

```
M_k(N) < C_k(logN)^{k²}   para todo N finito.
```

El residual R_k(N) − C_k < 0 y converge a 0 desde abajo, monótonamente.

---

## 5. Lo que controla las fluctuaciones de M_k

Las fluctuaciones de R_k(N) son la diferencia entre el funcional asintótico y el valor finito.
Esa diferencia está controlada por el desarrollo de Laurent de F_q(s)/s en s = 1:

```
F_q(s)/s = [ζ(s)^q · G_q(s)] / s

ζ(s) = 1/(s−1) + γ_E + ...   [expansión de Laurent]

→ F_q(s)/s tiene un polo de orden q = k² en s = 1.
```

El residuo completo da:

```
M_k(N) = C_k(logN)^{k²}  +  C_k^{(1)}(logN)^{k²-1}  +  ...  +  C_k^{(k²)}  +  O(N^{-δ})
```

Es decir: la expansión completa del término principal tiene k² coeficientes (uno por cada potencia
de log N de k² hasta 0). El "error" O(N^{-δ}) viene de la integral sobre la línea Re(s) = 1−δ
donde F_q es holomorfa.

**Conclusión:** la velocidad de convergencia de R_k(N) → C_k es gobernada por los coeficientes
del desarrollo de Laurent de F_q en s = 1 — no por los ceros de ζ.

---

## 6. Corrección del diseño: ¿qué hay que cambiar en Phase 20?

### Lo que NO funciona (refutado por el Paso 0)

❌ **Hipótesis C del diseño original:** "Si κ > 0, la amplitud de la oscilación de M_k(N)/(logN)^{k²}
crece más rápido que N^{-1/2}."

Esta hipótesis es incorrecta: M_k(N) es monótona (no oscila) y los ceros de ζ no aparecen como
residuos en la fórmula de Perron de M_k. La amplitud de la "oscilación" es 0 (el residual siempre
es negativo). No hay nada que medir.

❌ **Experimento 1 (análisis de fluctuaciones de M_k):** Diseñado para detectar una oscilación que
no existe. El experimento medirá la velocidad de convergencia de R_k(N) → C_k desde abajo, que
es un fenómeno de segunda capa de la expansión de Laurent en s=1. Tiene valor para Branch B
(teoría aritmética multifractal) pero NO para detectar κ > 0.

### Lo que SÍ puede ser sensible a los ceros

✅ **Experimento 3 (correlaciones multiplicativas):** La suma C_k(h,N) = Σ k^{2ω(n)}·k^{2ω(n+h)}/n
involucra el PRODUCTO de dos funciones aritméticas NO multiplicativas en n (porque el shift h rompe
la multiplicatividad). Su análisis requiere el método del círculo de Hardy–Littlewood o métodos de
criba multiplicativa. En ese contexto, los ceros de ζ SÍ aparecen a través de:

```
Σ_{p≤N} 1/p · 1/p  ~  (loglogN)²  [sin h]
Σ_{p≤N, p|n, p|(n+h)} ...         [con h: suma doble sobre primos, vía criba]
```

Pero la conexión con los ceros es más sutil: pasa por la distribución de primos en progresiones
aritméticas y el error de von Mangoldt, no directamente por los ceros como residuos de F_q.

✅ **Una versión DISTINTA de Experimento 1:** En lugar de M_k, estudiar la función:

```
Ψ_k(N) := Σ_{n≤N} q^{ω(n)} · Λ(n)
```

donde Λ(n) es la función de Mangoldt. Esta suma SÍ tiene la forma ζ'/ζ · F_q, y ahí los ceros
SÍ aparecen como polos (a través de ζ'/ζ). Esta es la dirección que conectaría genuinamente con κ.

✅ **La pregunta correcta para Ruta C:** En lugar de "¿oscila M_k?", la pregunta correcta es:

> ¿La CORRELACIÓN entre ω(n) y la función Λ(n) es sensible a κ?

Formalmente: ¿el cociente Σ_{n≤N} q^{ω(n)}·Λ(n)/n  /  (Σ_{n≤N} q^{ω(n)}/n) tiene oscilaciones
controladas por los ceros?

Este cociente sí vería los ceros porque Σ q^{ω(n)}·Λ(n)/n^s = −F_q(s) · ζ'(s)/ζ(s), y ζ'/ζ
tiene polos simples en los ceros de ζ.

---

## 7. El valor del Paso 0

**Lo que encontró:**

1. F_q(s) = ζ(s)^q · G_q(s), con G_q holomorfa y no nula en Re(s) > 1/2.
2. Los ceros ρ de ζ son CEROS de F_q (no polos) → no contribuyen residuos de Perron.
3. M_k(N) es monótona positiva → no oscila → el diseño del Experimento 1 era inválido.
4. La velocidad de convergencia de R_k → C_k está controlada por el desarrollo de Laurent en s=1.
5. La conexión con ceros requiere involucrar ζ'/ζ (Mangoldt) o sumas con shift (Exp 3 tiene potencial).

**Lo que significa:**

La Ruta C del advisor sigue siendo la mejor dirección — pero el observable debe cambiarse.
No es M_k(N) el portador de información de ceros. El portador es Σ q^{ω(n)}·Λ(n)/n.

**Lo que NO fue refutado:**

- El hecho de que los ceros están AUSENTES de M_k no quita que existan observables naturales
  de ω que sí codifiquen información de ceros. El Paso 0 cierra la puerta de M_k y abre
  la pregunta sobre objetos ω-ponderados por Λ o sobre correlaciones con shift.

---

## 8. Plan revisado para Phase 20

| Paso | Experimento revisado | Observable | Mecanismo cero |
|---|---|---|---|
| 0 | Este documento | Factorización F_q = ζ^q · G_q | Ceros son ceros de F_q (no polos) |
| 1* | Suma ω-Λ: Σ q^{ω(n)}Λ(n)/n | ω ponderado por Mangoldt | ζ'/ζ · F_q: polos en ρ |
| 2 | Short-interval ω | Distribución de ω en [N,N+H] | Negativo esperado (criba) |
| 3 | Correlaciones C_k(h,N) | Σ k^{2ω(n)}k^{2ω(n+h)}/n | Método del círculo, potencial real |
| 4 | Veredicto del puente | Síntesis | ¿Existe puente ω↔ceros? |

*El Paso 1 revisado es matemáticamente más honesto que el Experimento 1 original.*

---

*Cross-refs:* `00-PHASE20-DESIGN.md` (diseño original a corregir), `../phase-19/05-k2-from-erdjoskac.md`
(G_q(1) Euler product, consistent con G_q holomorfa), Selberg–Delange theorem (Tenenbaum, §II.5).  
*Decisión:* los Experimentos 2–3 del diseño original se conservan; el Experimento 1 se reemplaza
por la suma ω-Mangoldt.
