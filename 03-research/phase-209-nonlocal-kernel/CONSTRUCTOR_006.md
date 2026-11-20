# CONSTRUCTOR_006 — FE exacta de Π y defecto explícito tras borrado

2026-10-18. Continuación constructiva. **PROVED, auditoría favorable en AUDIT_006:** identidad exacta de inversión para el término Π del kernel positivo −R; su parámetro se fija en α=1/4. Se calcula también la identidad que cambia tras eliminar primos. **No se obtiene aún la forma Q_T.**

## 0. Corpus antes de construir

Búsquedas dirigidas en índice ROUTES-TRIED-INDEX, grid y crucigrama: co-Poisson, retículas fraccionarias, Hamburger, defecto de autodualidad y portador exterior. Referencias pertinentes: SPEC005 (origen de theta eliminada), Z_CARRIER, COMPOSE_EF_001, CELL_001, transporte FE/Helson y las barreras P1.

No se propone otro argumento de identificación Hamburger ni un defecto cuadrático cuyo cero identifique ζ. No se usa una nueva factorización abstracta ni un lift de Bohr. **Razón nueva:** Π ya es un término concreto de la igualdad PSD probada en CONSTRUCTOR_005; se calcula su FE no lineal completa, con denominador y dilataciones fraccionarias, antes de intentar un enlace. La positividad de −R y la autodu­alidad clásica de theta no se venden como prueba de D. La representación Mellin del perfil m que se usa abajo es clásica; lo que se registra es su acción exacta sobre este Π y el defecto del mismo esquema borrado.

Se descartó antes de construir el pushforward finito de −R con coeficientes Möbius y traslaciones: seguiría siendo un símbolo convolutivo de P1. La existencia de un nuevo kernel PSD no elimina el motivo de esa barrera.

## 1. Perfil de defecto de masa y Poisson

Sea c(y)=y^(−1/2), τ(y)=θ(y)−1 y

`m(y)=c(y)−τ(y)`.

Para y>0,

`0<m(y)<1`, `m(y)=y^(−1/2)m(1/y)`,

`τ(1/y)=√y[1−m(y)]`.                              (1)

**Prueba.** La comparación con la integral de la gaussiana decreciente da τ(y)<c(y); por Poisson `m(y)=1−c(y)τ(1/y)<1`. La segunda identidad se obtiene sustituyendo Poisson otra vez. La tercera sigue de la definición de m en 1/y. ∎

La Mellin de m es `∫m(y)y^(α−1)dy=−Z_α` en 0<α<1/2, según CONSTRUCTOR_005. No es por sí sola un segundo puente al nodo.

## 2. El término positivo Π que se conserva

Defino para d≥2

`W_d(y)=τ(d²y)−τ(y)/d`.

El kernel ya obtenido es

`Π_α(d,e)=∫_0^∞ y^(α−1) W_d(y)W_e(y)/τ(y)dy`.

Es una integral convergente para 0<α<1/2; de hecho su convergencia en cero admite más, pero no se necesita ampliar el intervalo.

Usando τ=c−m se tiene la identidad **forward**

`W_d(y)=m(y)/d−m(d²y)`.                            (2)

La parte c cancela exactamente. No se eliminó ningún resto.

## 3. Transformación exacta: dos escalas y parámetro crítico fijo

**Teorema 1 (PROVED).** Para d,e≥2 y 0<α<1/2,

`Π_α(d,e)=1/(de) ∫_0^∞ y^((1/2−α)−1)`

` ·[m(y)−m(y/d²)][m(y)−m(y/e²)]/[1−m(y)] dy`.      (3)

**Prueba.** Cambiar y por 1/u en la definición. Por (1) y (2),

`W_d(1/u)=√u/d [m(u)−m(u/d²)]`,

`τ(1/u)=√u[1−m(u)]`.

El jacobiano y el cociente dejan la potencia u^((1/2−α)−1); renombrar u. Todas las integrales convergen y el cambio de variable es ordinario. ∎

En α=1/4 el exponente no cambia: **la inversión preserva el parámetro crítico del mismo kernel positivo**, y transforma dilataciones d² hacia delante en dilataciones d^(−2) hacia atrás, con denominador 1−m.

La representación conserva ambas escalas dentro de las diferencias. Esto no demuestra por sí solo que Π integrado a α fijo sea distinto de w(de), ni que salga de un álgebra efectiva de alturas. Esa reducción no se ha probado ni refutado aquí; sigue pendiente construir y analizar el operador efectivo, como exige O1.

### Dónde quedó el término de origen

Si se escribe directamente con tau, la misma fórmula es

`W_d(1/u)=√u/d[τ(u/d²)−τ(u)]−(1−1/d)`.

El término constante no desapareció por una aproximación: se incorporó exactamente a las diferencias de m. Por tanto no se puede identificar el rango uno v_s de −R con el polo de Q_T omitiendo esta contribución.

## 4. Borrado finito: dos perfiles distintos, no la misma autodu­alidad

Sea P>1 squarefree, `δ_P=∏_{p|P}(1−1/p)`,

`τ_P(y)=Σ_{a|P}μ(a)τ(a²y)`,

`m_P(y)=δ_P c(y)−τ_P(y)`.

La completación PSD de −R_P fue probada en CONSTRUCTOR_005 §10. Para calcular su FE, defino su perfil dual exacto

`m_P^∨(y):=y^(−1/2)m_P(1/y)`.

Por inclusión–exclusión y Poisson,

`m_P^∨(y)=−Σ_{a|P} μ(a)/a ·τ(y/a²)`, P>1,        (4)

`τ_P(1/y)=√y[δ_P−m_P^∨(y)]`.                     (5)

No se afirma que m_P o m_P^∨ sean positivos, ni que estén entre 0 y1.

La discrepancia exacta es

`Δ_P(y)=m_P^∨(y)−m_P(y)`

`=Σ_{a|P}μ(a)τ(a²y)−Σ_{a|P}μ(a)/a·τ(y/a²)−δ_P c(y)`. (6)

Tiene límites que certifican su no anulación:

`Δ_P(y)→δ_P` cuando y↓0,

`Δ_P(y)=−δ_P y^(−1/2)+o(y^(−1/2))` cuando y→∞.

En efecto τ_P(y)=δ_P c(y)+error exponencial en cero, porque la constante se cancela; y τ_P decae exponencialmente en infinito. Las mismas propiedades en (4) dan los límites duales. Por ello **el perfil borrado no es autodu­al del modo (1)**. El defecto cambia de signo entre ambos extremos; no se le atribuye un signo cuadrático.

Para d coprimo con P,

`W_d^P(y)=τ_P(d²y)−τ_P(y)/d=m_P(y)/d−m_P(d²y)`.

Su FE exacta es

`W_d^P(1/u)=√u/d[m_P^∨(u)−m_P^∨(u/d²)]`.

Por tanto el mismo cambio de variable produce

`Π_α^P(d,e)=1/(de)∫_0^∞u^((1/2−α)−1)`

` ·[m_P^∨(u)−m_P^∨(u/d²)][m_P^∨(u)−m_P^∨(u/e²)]`

` /[δ_P−m_P^∨(u)]du`.                            (7)

El denominador es estrictamente positivo por (5), ya que τ_P>0. La ley borrada sigue dando un Gram positivo, pero el perfil forward m_P y el backward m_P^∨ son distintos. Sustituir uno por el otro sin Δ_P sería una igualdad falsa.

**Especificidad precisa lograda:** la identidad *de un solo perfil* (2)–(3), con la misma m en ambas orientaciones y el par de masas τ y 1−m, usa la FE completa y falla tras el borrado por el defecto explícito (6). Esto no demuestra todavía que esa identidad produzca un signo para Q_T.

## 5. Paso de enlace concreto que queda

El kernel completo ahora tiene la fórmula probada

`−R_(1/4)=(-Z_(1/4))G_(1/2)+(-Z_(1/4))v_(1/2)v_(1/2)*+Π_(1/4)`.

La FE de Π es (3), mientras G y v tienen coeficientes explícitos de peso1/2. Un enlace útil debe construir un mapa U_T desde los tests del nodo a observables de divisibilidad y **verificar** tres identidades:

1. La contribución de `G_(1/2)` y las dos representaciones de Π deben producir el peine lineal en Λ, con todos los términos de cocientes/lcm tratados.
2. El término de origen dentro de (3) y el rango uno v deben dar exactamente el polar y su anulación bajo la restricción declarada, sin identificarlos por semejanza.
3. La parte continua restante debe dar el gamma de conductor1 con signo positivo del resto demostrado, no un símbolo libre definido para completar Q_T.

Estas no son tres supuestos nuevos que se den por hechos. Son las verificaciones concretas de un **único enlace todavía no construido**. El candidato disponible para ese cálculo es la igualdad forward/backward de Π, no una nueva lista de programas.

La mera elección `a_d=Λ(d)F(log d)/√d` no prueba esas identidades: produce una forma en evaluaciones finitas, mientras Q_T actúa sobre el dominio continuo. La elección por autocorrelaciones daría grado cuatro. No se adopta ninguna de ellas como mapa sin resolver esa diferencia.

## 6. Residuo exacto

Hay ya un kernel renormalizado positivo independiente y una FE interna calculada que distingue el perfil completo del perfil borrado. **Todavía no hay un operador K(t,t′) efectivo en el dominio de Q_T ni una identidad de su forma con −R.** No se ha demostrado que (3) convierta el signo de −R en signo del nodo.

La identidad pendiente no es «existe alguna raíz de Q_T»: debe usar (2) y (3) para producir los términos concretos del paper. Si un intento sólo invoca PSD de −R, falla el test de especificidad porque esa PSD sobrevivió al borrado; tiene que intervenir precisamente la identidad de un perfil y su defecto (6).

**Estado:** FE de Π y defecto borrado PROVED, auditoría favorable en AUDIT_006; precisión de alcance no-Hankel incorporada. Enlace Q_T OPEN, objetivo D activo. Ninguna conclusión de imposibilidad ni cierre de O1.


## Precisión de alcance del criterio de enlace — 2026-10-19

La revisión posterior del enlace (ronda011, cotejo directo conP47) corrige
la lectura de§5: las tres correspondencias allí enumeradas son un esquema
posible para calcular un candidato, NO condiciones necesarias de cualquier
prueba. Basta una identidad TOTAL, o una dominación de formas,

    a_T(F) >= K_(1/4)(U_T F) >=0,

sobre un core denso para la norma de la forma objetivo, con todos los
restos y dominios justificados. No se exige que G produzca por separado
el peine, v por separado el polar, ni Π por separado gamma. Puede haber
cancelaciones entre piezas. El paso desde el core usa continuidad en la
norma de la forma objetivo; no basta densidad L². ParaD completa deben
tratarse los sectores y términos polares segúnP47. Esta precisión no
aporta todavía la dominación ni el mapa requerido.
