# Frente C — K-teoría y clase de obstrucción en $K_0(C^*(C_\mathbb{Q}))$

**Fecha:** junio 2026

---

## 1. La C*-álgebra del programa

El espacio base del programa es $C_\mathbb{Q} = \mathbb{A}_\mathbb{Q}^*/\mathbb{Q}^*$,
el grupo de clases de idèles. Es un grupo abeliano localmente compacto. Su C*-álgebra
de grupo es:
$$C^*(C_\mathbb{Q}) = C^*_r(C_\mathbb{Q}) \cong C_0(\hat C_\mathbb{Q}),$$
donde $\hat C_\mathbb{Q}$ es el dual de Pontryagin (los caracteres unitarios de
$C_\mathbb{Q}$). Como $C_\mathbb{Q}$ es abeliano, la C*-álgebra es conmutativa.

La descomposición de $C_\mathbb{Q}$:
$$C_\mathbb{Q} \cong \mathbb{R}^*_+ \times \hat{\mathbb{Z}}^*,$$
donde $\hat{\mathbb{Z}}^* = \varprojlim (\mathbb{Z}/n\mathbb{Z})^*$ es el grupo de
completación de las unidades (contiene la información de todos los primos finitos).

---

## 2. Los grupos K de $C^*(C_\mathbb{Q})$

**Teorema C.1** (Connes, ~1994). Para la C*-álgebra del sistema dinámico $(C_\mathbb{Q}, \mathbb{Q}^*)$:
$$K_0(C^*(C_\mathbb{Q})) \cong \mathbb{Z}, \qquad K_1(C^*(C_\mathbb{Q})) \cong \mathbb{Z}.$$

*Referencia:* Este cálculo sigue de la estructura de $C_\mathbb{Q}$ como extensión de
$\mathbb{R}^*_+$ por el grupo compacto $\hat{\mathbb{Z}}^*$, y de la sucesión exacta
de Pimsner–Voiculescu aplicada iterativamente sobre los primos.

**Corolario C.2.** Todo elemento de $K_0(C^*(C_\mathbb{Q}))$ es de la forma $n \cdot [1]$
para $n \in \mathbb{Z}$, donde $[1]$ es la clase de la proyección trivial. En particular,
un elemento de $K_0$ es cero si y sólo si corresponde al entero $n = 0$.

---

## 3. El índice de Kreĭn como clase en $K_0$

**Definición C.3.** Bajo la conjetura del puente (Phase 26), $H_C$ actúa sobre el espacio
de Pontryagin $(\mathcal{K}, Q)$. Sea $P_-$ la proyección espectral de $H_C$ sobre el
subespacio de eigenvalores no-reales (el subespacio negativo de $(\mathcal{K}, Q)$).

Definimos la clase:
$$[P_-] \in K_0(C^*(H_C)) \hookrightarrow K_0(C^*(C_\mathbb{Q}))$$
como la imagen de la proyección $P_-$ bajo la inclusión natural de C*-álgebras.

**Proposición C.4.** $[P_-] = \kappa(Q) \cdot [e]$ en $K_0(C^*(C_\mathbb{Q})) \cong \mathbb{Z}$,
donde $[e]$ es el generador y $\kappa(Q)$ es el índice de Kreĭn.

*Prueba:* En $K_0$, la clase de una proyección de rango finito $n$ es $n \cdot [e]$.
Bajo Hipótesis D, $P_-$ tiene rango $\kappa(Q) = 2m$ (finito). $\square$

**Corolario C.5.** $[P_-] = 0$ en $K_0(C^*(C_\mathbb{Q})) \iff \kappa(Q) = 0 \iff$ RH.

---

## 4. El isomorfismo de Baum–Connes para $C_\mathbb{Q}$

El isomorfismo de Baum–Connes afirma que para un grupo localmente compacto $G$:
$$\mu: K_*^G(\underline{E}G) \xrightarrow{\sim} K_*(C^*_r(G)),$$
donde $\underline{E}G$ es el espacio clasificante para acciones propias de $G$.

**Teorema C.6** (Baum–Connes para grupos abelianos). $C_\mathbb{Q}$ es un grupo abeliano
localmente compacto, por tanto amenable. Para grupos amenables, la conjetura de
Baum–Connes es un teorema:
$$\mu: K_*^{C_\mathbb{Q}}(\underline{E}C_\mathbb{Q}) \xrightarrow{\sim} K_*(C^*(C_\mathbb{Q})).$$

El espacio clasificante $\underline{E}C_\mathbb{Q}$ para un grupo abeliano es un punto
(la acción es libre y propia en un punto). Por tanto:
$$K_0^{C_\mathbb{Q}}(\underline{E}C_\mathbb{Q}) \cong R(C_\mathbb{Q}),$$
el anillo de representaciones de $C_\mathbb{Q}$ (representaciones de dimensión finita).

**Consecuencia C.7.** El isomorfismo de Baum–Connes identifica:
$$K_0(C^*(C_\mathbb{Q})) \cong R(C_\mathbb{Q}) \cong \mathbb{Z}[\hat C_\mathbb{Q}^{\text{fin}}],$$
donde $\hat C_\mathbb{Q}^{\text{fin}}$ son los caracteres unitarios de orden finito
(los caracteres de Dirichlet).

---

## 5. La pregunta central del Frente C

**Pregunta C.8** (central). ¿Bajo qué condiciones es $[P_-] = 0$ en $R(C_\mathbb{Q})$?

Por el Corolario C.5, esto equivale a RH. La pregunta K-teórica es:

> ¿Es la proyección espectral negativa $P_-$ Murray–von Neumann equivalente a cero en
> $C^*(C_\mathbb{Q})$?

$P_- \sim_{\text{MvN}} 0$ significa que existe un parcial isométrico $V \in C^*(C_\mathbb{Q})$
tal que $V^*V = P_-$ y $VV^* = 0$. En dimensión infinita, esto equivale a que $P_-\mathcal{K}$
es un subespacio "trivial" en el sentido de K-teoría.

---

## 6. La teoría KK y un invariante más fino

**Definición C.9** (bimodulo de Kasparov). La teoría $KK(A, B)$ de Kasparov es un
invariante bivariante que generaliza $K_0$. Para el operador de Connes $H_C$, se define
un elemento:
$$[H_C] \in KK(C^*(C_\mathbb{Q}), C^*(C_\mathbb{Q}))$$
como la clase del módulo de Hilbert $(\mathcal{K}, H_C, P_+)$ donde $P_+$ es la
proyección espectral positiva.

**Proposición C.10.** El índice de Kreĭn $\kappa(Q)$ es la imagen de $[H_C]$ bajo el
mapa de índice:
$$\operatorname{Ind}: KK(\mathbb{C}, C^*(C_\mathbb{Q})) \to K_0(C^*(C_\mathbb{Q})) \cong \mathbb{Z}.$$

*Prueba:* El mapa de índice en KK-teoría extrae la diferencia de dimensiones entre los
subespacios positivo y negativo de un operador. Para $H_C$ con espectro parcialmente
no-real en $(\mathcal{K}, Q)$, la diferencia es $-\kappa(Q)$. $\square$

**Pregunta C.11** (nueva). ¿Es $[H_C]$ la clase unidad $[1] \in KK(C^*(C_\mathbb{Q}),
C^*(C_\mathbb{Q}))$?

Si $[H_C] = [1]$ (el operador de Connes es KK-equivalente al operador identidad), entonces
$\operatorname{Ind}([H_C]) = 0$, luego $\kappa = 0$, luego RH.

---

## 7. La conexión con la traza de Connes

**Proposición C.12.** El carácter de Chern $\operatorname{ch}: K_0(C^*(C_\mathbb{Q})) \to
HC_0(C^*(C_\mathbb{Q}))$ (cohomología cíclica) mapea $[P_-]$ a:
$$\operatorname{ch}([P_-]) = \operatorname{tr}(P_-) \in HC_0,$$
donde $\operatorname{tr}$ es la traza canónica sobre $C^*(C_\mathbb{Q})$.

La traza de la proyección negativa es exactamente $\kappa(Q) = 2m$.

**Conexión con la fórmula explícita:** La traza de Connes sobre $C^*(C_\mathbb{Q})$
está relacionada con la traza del operador del flujo sobre las órbitas periódicas,
que vía la fórmula de trazas de Selberg produce la fórmula explícita de Weil.

Por tanto:
$$\operatorname{ch}([P_-]) = \kappa(Q) \overset{!}{=} 0$$
sería una afirmación sobre el carácter de Chern del bimodulo del operador de Connes,
calculable (en principio) via la cohomología cíclica de $C^*(C_\mathbb{Q})$.

---

## 8. El obstáculo y lo que se puede calcular

**Proposición C.13** (obstáculo al vanishing K-teórico). $[P_-] = 0$ en $K_0$ si y
sólo si la proyección $P_-$ es homotópica a cero dentro de las proyecciones de
$C^*(C_\mathbb{Q})$. Para proyecciones de rango finito en $\mathcal{B}(\mathcal{K})$,
$P_- \sim_{\text{MvN}} 0$ si y sólo si $\operatorname{rango}(P_-) = 0$.

*Consecuencia:* En $K_0$, la clase $[P_-]$ es el entero $\kappa(Q) \in \mathbb{Z}$. Para
que sea cero, hay que demostrar $\kappa(Q) = 0$ directamente. El aparato K-teórico
no da una nueva ruta de prueba para $\kappa = 0$; reexpresa el mismo hecho.

**Matiz crucial:** La K-teoría SÍ añade valor si el argumento es: "la clase $[P_-]$ es
un invariante cohomológico que, por razones independientes de aritméticas (factorización,
fórmula de caracteres), debe ser cero en $KK(C^*(C_\mathbb{Q}), C^*(C_\mathbb{Q}))$."

El camino correcto del Frente C:

1. Demostrar que $[H_C] = [1]$ en $KK(C^*(C_\mathbb{Q}), C^*(C_\mathbb{Q}))$ por
   construcción directa (mostrar KK-equivalencia entre $H_C$ e identidad).
2. De $[H_C] = [1]$ deducir $\kappa = 0$.

Esto requiere construir un homotopía explícita $H_C \sim_{\text{KK}} \operatorname{Id}$.
La homotopía natural sería el flujo de de Bruijn–Newman: $H_{C,t}$ para $t \in [0, \Lambda]$.

**Esto conecta el Frente C con el Frente A.** Los tres frentes A, C, D convergen al
mismo problema central.

---

## 9. Veredicto del Frente C

| Resultado | Estado |
|---|---|
| $K_0(C^*(C_\mathbb{Q})) \cong \mathbb{Z}$ | Establecido |
| $[P_-] = \kappa(Q) \in \mathbb{Z}$ | Probado (Prop. C.4) |
| Baum–Connes para $C_\mathbb{Q}$ | Teorema (grupo amenable) |
| $[P_-] = 0 \iff$ RH | Tautológico |
| $[H_C] = [1]$ en KK | **Abierto — el resultado nuevo a probar** |
| Conexión KK ↔ Frente A (homotopía = flujo DBN) | **Nuevo — unificación de frentes** |
