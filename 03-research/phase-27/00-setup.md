# Phase 27 — Rigidez adélica

**Fecha:** junio 2026
**Prerrequisito:** Conjetura 26-C.2 (Teorema Puente) aceptada como hipótesis de trabajo.
**Objetivo único:** probar $\operatorname{neg.ind}(H_C) = 0$ mediante la estructura de $C_\mathbb{Q}$.

Si Phase 26 se completa (el puente se establece), el programa cambia de naturaleza:
ya no se estudian ceros de $\zeta$. Se estudia un operador en un espacio adélico.

---

## 0. El punto de partida

**Lo que Phase 26 habría establecido:**

$$\kappa(Q) = \operatorname{neg.ind}(H_C),$$

donde $Q$ es la forma de Weil, $H_C$ es el operador de escalado de Connes, y la
identidad vale en el espacio de Pontryagin $\mathcal{K} = (L^2(C_\mathbb{Q}), Q)$.

**La consecuencia:**

$$\text{RH} \iff \kappa(Q) = 0 \iff \operatorname{neg.ind}(H_C) = 0.$$

**El único problema abierto:**

$$\boxed{\operatorname{neg.ind}(H_C) = 0.}$$

---

## 1. La estructura del problema

El índice negativo de $H_C$ en $\mathcal{K}$ es el número de pares de eigenvalores
complejos (no-reales) de $H_C$. Por el Teorema Puente:

$$\operatorname{neg.ind}(H_C) = 2m = \text{número de órbitas fuera de línea.}$$

Entonces $\operatorname{neg.ind}(H_C) = 0$ equivale a: **no existen caracteres
no-unitarios en el espectro de escalado de $H_C$.**

Cada dirección negativa de $Q$ corresponde a un carácter no-unitario
$|x|^{b_j + i\gamma_j}$ (con $b_j > 0$) en el espectro de escalado.

La pregunta de Phase 27: ¿puede existir tal carácter dado la estructura aritmética de $C_\mathbb{Q}$?

---

## 2. Las cuatro sub-fases

### 27-A: Clasificación de direcciones negativas

**Objetivo:** Demostrar que cada dirección negativa de $Q$ en $\mathcal{K}$ produce
un eigenvalor complejo aislado de $H_C$.

**Herramienta:** Teorema de Kreĭn–Langer (disponible gratis del puente).

**Estado esperado:** Casi inmediato del puente; la cota "a lo sumo $\kappa$" invierte
a "exactamente $\kappa$" si cada dirección negativa tiene un eigenvalor complejo.

**Resultado esperado:** Una clasificación completa de los subespacios negativos de
$\mathcal{K}$ en términos de caracteres no-unitarios.

---

### 27-B: Interpretación adélica de los eigenvalores complejos

**Objetivo:** Demostrar que todo eigenvalor complejo $\lambda_j = \gamma_j - ib_j$ de
$H_C$ (con $b_j > 0$) corresponde a un Grössencharacter no-unitario de $C_\mathbb{Q}$.

**Definición:** Un Grössencharacter de $C_\mathbb{Q}$ de la forma
$\chi_j(x) = |x|^{b_j + i\gamma_j}$ (con $b_j > 0$) es **no-unitario**: tiene crecimiento
modular $|x|^{b_j}$ y no está en el dual unitario $\widehat{C_\mathbb{Q}}$ medido por
la medida de Haar.

**Herramienta:** Teoría de representaciones de $C_\mathbb{Q}$ (teoría de clase de campo,
Tate 1950).

**Estado esperado:** Relativamente directo de la teoría de Tate sobre adèles; el Grössencharacter
correspondiente a un cero $\rho_j$ off-line debería ser la evaluación de la función $\zeta$
en la línea $\Re(s) = 1/2 + b_j$, que no es la línea unitaria.

---

### 27-C: El principio local-global adélico

**Objetivo:** Demostrar que la existencia de un Grössencharacter no-unitario en el espectro
de $H_C$ contradice alguna propiedad global de $C_\mathbb{Q}$.

**La hipótesis de Phase 27:**

Sea $Q = Q_\infty \times \prod_p Q_p$ la factorización local de la forma de Weil
(si existe). Entonces:

$$Q_p \ge 0 \text{ para todo primo } p
\implies Q \ge 0 \text{ globalmente}
\implies \kappa(Q) = 0
\implies \operatorname{neg.ind}(H_C) = 0.$$

**La analogía:** El teorema de Hasse–Minkowski dice que una forma cuadrática $Q$ sobre
$\mathbb{Q}$ es positiva-definida globalmente sii es positiva-definida localmente (en
$\mathbb{R}$ y en $\mathbb{Q}_p$ para todo primo $p$). Si la forma de Weil $Q$ admite
un principio análogo, y si $Q_p \ge 0$ para todo $p$ (lo que seguiría de la hipótesis
de Riemann LOCAL para curvas sobre $\mathbb{F}_p$, que está PROBADA por Weil–Deligne), entonces
$Q \ge 0$ globalmente, dando RH.

**El obstáculo:** La forma de Weil $Q$ no es una forma cuadrática clásica sobre $\mathbb{Q}$
— es una forma funcional en dimensión infinita. El teorema de Hasse–Minkowski clásico no se
aplica directamente. La pregunta concreta es:

> ¿Existe un principio de Hasse–Minkowski para formas hermitianas infinito-dimensionales
> sobre $\mathbb{Q}$, y aplica a la forma de Weil $Q$?

**Relación con Wall W4-RSRP:** Phase 27 es la formulación más precisa de Wall W4-RSRP
que el programa ha producido. En lugar de "no se puede propagar información aritmética
de $\Re(s)>1$ al interior de la franja crítica", Phase 27 pregunta: "¿puede el principio
local-global (que propagaría información de los factores de Euler locales $Q_p$ a la
forma global $Q$) ser establecido para formas hermitianas infinito-dimensionales?"

---

### 27-D: Conclusión

**Objetivo:** De 27-C, deducir $\operatorname{neg.ind}(H_C) = 0$ y por ende RH.

**Lógica:** Si el principio local-global se establece y $Q_p \ge 0$ para todo $p$,
entonces $Q \ge 0$, $\kappa = 0$, $\operatorname{neg.ind}(H_C) = 0$, RH.

---

## 3. Por qué Phase 27 es diferente de Phases 21–26

**Phases 21–24:** Estrategias espectrales dentro del arco Kreĭn.
Resultado: sin cota inferior para $b_j$.

**Phase 25:** Auditoría de 15 mecanismos clásicos.
Resultado: todos fallan como Wall W4-RSRP.

**Phase 26:** El puente Kreĭn–Connes.
Resultado (condicional): κ = neg.ind($H_C$).

**Phase 27:** Usa el puente para atacar $\operatorname{neg.ind}(H_C) = 0$ con herramientas adélicas.

La diferencia crucial: Phase 27 es la **primera formulación del programa donde la herramienta
propuesta (principio local-global adélico) no existía en las fases anteriores**.

Phases 21–25 usaron herramientas disponibles: análisis funcional, teoría de ceros, Selberg CLT,
Kreĭn–Langer. Todas agotadas.

Phase 27 usa herramientas que provienen de la estructura aritmética del espacio adélico:
el principio local-global, la factorización de Euler, la teoría de representaciones de $C_\mathbb{Q}$.
Estas herramientas son nuevas en el programa.

---

## 4. El objetivo intermedio más asequible

Antes de atacar $\operatorname{neg.ind}(H_C) = 0$ directamente (equivalente a RH),
Phase 27 busca resultados intermedios que ya serían extraordinarios:

| Objetivo intermedio | Implicación directa |
|---|---|
| $\operatorname{neg.ind}(H_C) < \infty$ | Finitely many off-line zeros (Hypothesis D) |
| $\operatorname{neg.ind}(H_C) \le M$ para alguna constante $M$ | A lo sumo $M/2$ órbitas off-line |
| $\operatorname{neg.ind}(H_C) \le 10$ | A lo sumo 5 órbitas fuera de línea |
| $\operatorname{neg.ind}(H_C) = 0$ | RH |

El objetivo $\operatorname{neg.ind}(H_C) \le M$ correspondería a un teorema del tipo
"la función $\zeta$ tiene a lo sumo $M/2$ órbitas de ceros fuera de la línea crítica",
que nunca ha sido demostrado para ningún $M$ finito sin asumir restricciones adicionales.
Ya sería un resultado histórico.

---

## 5. Documentos de Phase 27

**27-A:** `phase-27/01-classification-negative-directions.md`
**27-B:** `phase-27/02-adelic-interpretation.md`
**27-C:** `phase-27/03-local-global-principle.md`
**27-D:** `phase-27/04-conclusion.md`

**Paper:** P36 (a escribir una vez que Phase 27 avance).

---

## 6. Criterio de éxito

Phase 27 tiene éxito si:
- Se establece el principio local-global para la forma de Weil (27-C), o
- Se prueba que el principio no puede establecerse en esta forma, con diagnóstico preciso.

Phase 27 falla sólo si no produce un resultado matemático concreto. Dado que los dos
resultados posibles (principio válido → RH; o diagnóstico de por qué falla → siguiente
reformulación) son ambos matemáticamente valiosos, Phase 27 no puede "fallar" en el
sentido ordinario.

---

## 7. Estado al inicio de Phase 27

| Componente | Estado |
|---|---|
| Teorema Puente (Conjetura 26-C.2) | Hipótesis de trabajo aceptada; V.1–V.4 pendientes |
| neg.ind($H_C$) = κ | Condicional al puente |
| Factorización $Q = \prod_p Q_p$ | No establecida; primer objetivo de 27-C |
| Principio local-global para $Q$ | Pregunta abierta; objetivo central de Phase 27 |
| $Q_p \ge 0$ para todo primo $p$ | Plausible (RH local para $\mathbb{F}_p$ probada); conexión a $Q_p$ no establecida |
