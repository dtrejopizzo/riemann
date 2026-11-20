# CONSTRUCTOR_005 — Completación positiva exacta de −R_α

2026-10-18. Constructor único. Matemática pura. **PROVED, auditoría final favorable en AUDIT_005 §11:** para 0<α<1/2, el kernel renormalizado **−R_α es definido positivo sobre toda familia finita de divisores distintos d≥2**, no sólo entre primos distintos. Se construye una descomposición exacta de su diagonal, bloques del mismo primo y cruces. **No se ha probado un enlace con Q_T. La fila D sigue OPEN.**

## 0. Corpus check y razón nueva escrita

Leídos las reglas del proyecto, README209 y auditorías, índice ROUTES-TRIED-INDEX (README, entradas recientes 209 y familias), residuos 06, P1_BBSTAR, SPEC005, grid maestro y crucigrama. Búsqueda adicional dirigida: `renormal.*covarian`, `masa faltante`, `Haar.*theta`, `Mellin.*profini`, `gcd.*zeta`, `covarian.*renormal`. No se identificó esta identidad en las entradas consultadas; esto no es declaración de prioridad global.

Choques: R183_008 (Gram semilocal gcd), Helson/Bohr, SPEC005 C-hom, P1 y certificados de la propia forma. **Razón nueva exacta:** se conserva el kernel R ya definido; no se sustituye por un Gram favorable. Una identidad algebraica de covarianzas y la Mellin de una *diferencia firmada* de masas producen su diagonal renormalizada y prueban **−R**, con signo prefijado, como suma PSD. La positividad clave es `−2π^(−α)Γ(α)ζ(2α)>0` en 0<2α<1, obtenida sin ceros. El espacio profinito se usa sólo para demostrar positividad de una matriz explícita sobre finitos divisores; no se propone el lift de Bohr como fuente de signo de Q_T.

La diferencia frente a CONSTRUCTOR_002 es que allí R=I+H tenía H firmado sin control. Aquí se cambia la identidad de comparación, conservando exactamente R y todos sus contraterminos. La diferencia frente a una norma genérica es la **igualdad explícita con el kernel renormalizado antes fijado**, no la mera existencia de alguna raíz.

## 1. Definiciones conservadas

`τ(y)=Σ_{n∈Z\{0}}exp(−πn²y)`, `c(y)=y^(−1/2)`.

`q_d(y)=τ(d²y)/τ(y)`, `X_d(N)=1_{d|N}` bajo `P_y(N=n)=exp(−πn²y)/τ(y)`.

Para d,e≥2 y l=lcm(d,e):

`B_y(d,e)=τ(y)[q_l(y)−q_d(y)q_e(y)]`,

`G_1(d,e)=1/l−1/(de)`,

`D_y(d,e)=c(y)G_1(d,e)−B_y(d,e)`.

Para 0<α<1/2:

`R_α(d,e)=∫_0^∞ y^(α−1)[B_y(d,e)−c(y)G_1(d,e)]dy`.

La convergencia entrada a entrada fue probada en CONSTRUCTOR_002: el corchete es O(1) en cero y O(y^(−1/2)) en infinito. Se fija el mismo esquema de sustracción; no se cambia una diagonal a voluntad.

Escribir s=2α∈(0,1) y

`Z_α=2π^(−α)Γ(α)ζ(2α)`.

**Signo elemental:** ζ(s)<0 para 0<s<1, pues la serie alternada η(s)=Σ_{n≥1}(−1)^(n−1)n^(−s) es positiva y `ζ(s)=η(s)/(1−2^(1−s))`. Por ello **Z_α<0**. Sólo se usa un valor real, no información sobre ceros.

## 2. El espacio aritmético: leyes geométricas sobre valuaciones finitas

Sea S cualquier conjunto finito de primos. Para t>0, defino P_t sobre `(v_p)_{p∈S}∈N_0^S` por independencia y

`P_t(v_p=j)=(1−p^(−t))p^(−tj)`.

Para d soportado en S, `E_t X_d=d^(−t)` y `E_t X_dX_e=lcm(d,e)^(−t)`. Las leyes son compatibles al ampliar S, pero la prueba sólo usa conjuntos finitos.

Para un polinomio de divisibilidad

`A(N)=Σ_{d∈E}a_d X_d(N)`, E finito,

defino `μ_t(A)=E_t A=Σ a_d d^(−t)`. En particular μ_1 es la media de divisibilidad uniforme (Haar sobre cilindros profinitos).

**Advertencia:** P_s para s<1 no es una probabilidad zeta normalizable sobre los enteros positivos. Es una ley sobre las finitas valuaciones observadas. No se intercambia un producto infinito con una serie divergente de enteros.

## 3. Identidad algebraica exacta antes de integrar

Defino un funcional firmado sobre el álgebra finita de observables de divisibilidad:

`ν_y(H)=c(y)E_1H−τ(y)E_yH`.

No se afirma que ν_y sea positivo; de hecho D_y puede ser indefinido al mezclar varios primos. No se necesita una medida global ν_y sobre los enteros.

**Lema 1 (PROVED).** Para todo A de soporte finito,

`D_y(A):=Σ conjugate(a_d)a_e D_y(d,e)`

`=ν_y(|A−μ_1(A)|²)+τ(y)|E_yA−μ_1(A)|²`.             (2)

**Prueba.** El primer miembro es `c Var_1(A)−τ Var_y(A)`. Expandir el primer término derecho:

`ν_y(|A−μ_1|²)=c Var_1(A)−τ[Var_y(A)+|E_yA−μ_1|²]`.

Sumar el segundo término. Es una identidad de complejos y sus módulos; no se ha usado signo. ∎

El punto de esta comparación es que el centro μ_1 es constante en y. No se resta la media gaussiana dentro del funcional firmado al integrar.

## 4. Mellin del defecto de masa: signo y fórmula exactos

**Lema 2 (PROVED).** Para k≥1 y 0<α<1/2,

`∫_0^∞ y^(α−1)[c(y)/k−τ(k²y)]dy=−Z_α k^(−2α)`.       (3)

**Prueba.** Para k=1, Poisson da `c−τ=1−c τ(1/y)`, que es O(1) en cero y O(c) en infinito. La integral converge. Dividir en y=1 y comparar con la continuación elemental de `∫ τ(y)y^(α−1)dy` desde α>1/2 da `−Z_α`. También puede tomarse esa continuación como definición de la Mellin regularizada: los términos sustraídos coinciden exactamente. Para k general cambiar u=k²y; el corchete se vuelve `u^(−1/2)−τ(u)` y aparece k^(−2α). ∎

Para un observable H de álgebra finita, expandirlo como combinación finita de X_k, incluyendo X_1=1. Como `ν_y(X_k)=c/k−τ(k²y)`, se obtiene

`∫_0^∞ y^(α−1)ν_y(H)dy=−Z_α E_sH`, s=2α.            (4)

Cada integral de esta expansión converge absolutamente; no se necesita que ν_y sea positivo antes de integrar. Si H≥0 en las valuaciones finitas, el miembro derecho es no negativo. Esta es la fuente de signo que faltaba al analizar la diferencia firmada.

## 5. Completación PSD de todo el kernel renormalizado

**Teorema 3 (PROVED).** Para 0<α<1/2 y A=Σ a_dX_d de soporte finito,

`−R_α(A)= (−Z_α) E_s|A−μ_1(A)|²`

`          +∫_0^∞ y^(α−1)τ(y)|E_yA−μ_1(A)|²dy ≥0`.   (5)

**Prueba.** Integrar (2). La primera integral es (4) aplicada a H=|A−μ_1|². La segunda converge: en cero, para cada d fijo, `q_d=1/d+O_d(√y)`, así que la diferencia de medias es O_A(√y), y el integrando sin potencia es O_A(√y). En infinito, q_d es acotado y τ decae exponencialmente. Ambas formas derechas tienen signo por `−Z_α>0` y positividad de P_s. ∎

Para índices distintos d≥2, la forma es **definida positiva**. Si el primer término fuera cero, A=μ_1(A) en todos los patrones de valuaciones finitas, pues P_s les da probabilidad positiva. En N=1 se obtiene μ_1=0. Evaluando sucesivamente en los índices de E en orden creciente, `A(d)=Σ_{e∈E,e|d}a_e` obliga por inducción a cada a_d=0. Por tanto un vector de coeficientes no nulo da primer término estrictamente positivo.

### Kernel completamente explícito

Defino

`H_s(d,e)=lcm(d,e)^(−s)−d^(−s)/e−e^(−s)/d+1/(de)`,

`Π_α(d,e)=∫_0^∞ y^(α−1)τ(y)[q_d(y)−1/d][q_e(y)−1/e]dy`.

Entonces

`−R_α=(−Z_α)H_s+Π_α`.                               (6)

Además,

`H_s=G_s+v_s v_s*`,

`G_s(d,e)=lcm(d,e)^(−s)−(de)^(−s)`,

`v_s(d)=d^(−s)−d^(−1)`.

G_s es la covarianza de los indicadores bajo P_s y Π_α es el Gram explícito de sus desviaciones gaussianas respecto de la media Haar. Así

`−R_α=(−Z_α)G_s+(−Z_α)v_s v_s*+Π_α`,                 (7)

con tres formas PSD identificadas y sin término restante firmado.

**Caso crítico α=1/4:** s=1/2, `−Z_α=−2π^(−1/4)Γ(1/4)ζ(1/2)>0`. La identidad paga exactamente la diagonal y los bloques del mismo primo del kernel R que ya estaba definido. No identifica ese escalar gamma-zeta con el arquimediano de Q_T.

## 6. Resultado previo de bloque, ahora explicado y reforzado

El argumento siguiente fue encontrado antes de (5) y sirve como control independiente para potencias de un primo.

La concavidad puncturada implica q_y(p)<1/p. Poisson da, para u>0,

`τ(u)−τ(p²u)<u^(−1/2)(1−1/p)`.

En efecto el defecto respecto del lado derecho es

`u^(−1/2)[τ(1/u)−p^(−1)τ(1/(p²u))]<0`.

Por tanto las masas gaussianas de cada cascarón de valuación,

`w_j=τ(p^(2j)y)−τ(p^(2j+2)y)`,

están estrictamente dominadas por `c(1−1/p)p^(−j)`, las masas de cP_1. Para cualquier observable de una valuación, la covarianza no normalizada es

`mass·Var(A)=min_z Σ_j mass_j|A_j−z|²`.

Esta expresión crece al aumentar cada masa; de ahí D_y≥0 en cada bloque de un primo, antes de integrar. Es estricta para observables no constantes. En varios primos, esa dominación de masas puede fallar y D_y no es PSD en cada escala. **La identidad (5) usa la positividad de la Mellin integrada de ν, no una dominación falsa punto a punto.**

## 7. Enlace con los cruces y con el producto de Euler

Para potencias de primos distintos, G_s(d,e)=0 porque lcm=de. Por (7), los cruces críticos positivos de −R calculados en CONSTRUCTOR_004 son

`(−Z_α)v_s(d)v_s(e)+Π_α(d,e)`.

Ambos términos son positivos entrada a entrada, pues v_s(d)>0 en 0<s<1 y `q_d−1/d<0` por concavidad puncturada. Esto reproduce su signo sin asignar una diagonal de laplaciano artificial.

Para potencias del mismo primo, G_s es exactamente la covarianza de su distribución geométrica de parámetro p^(−s). Así la completación no es sólo entrada a entrada: da los bloques de covarianza correctos dentro de la misma fórmula.

La identidad (5) usa aritmética de todos los enteros y sus densidades de divisibilidad; P_s incorpora el producto euleriano sobre los primos observados. **Especificidad para Q_T no obtenida:** el §10 prueba que quitar finitos primos produce una ley condicionada que conserva esta positividad, con otra masa y otra theta. La fórmula no demuestra que la positividad de Q_T para conductor1 se transfiera ni identifica qué término del enlace fallaría. El cálculo de ese enlace sigue siendo necesario.

## 8. Dominio y alcance: qué se logró, qué no

Se obtuvo una **completación positiva exacta del kernel aritmético renormalizado −R_α sobre c_00 de divisores**, con todos los modos de ese espacio algebraico incluidos. Su completación de Hilbert se puede definir mediante (5), pero todavía no se ha construido un operador no compacto de alturas en el dominio requerido por O1.

No se afirma que la norma así definida sea equivalente a una norma de coeficientes prefijada, ni que una serie infinita sobre todos los primos pertenezca al dominio. No se integra una suma global sin control de colas.

No se ha identificado un mapa U_T de los tests del nodo tal que `Q_T(F)=−R_(1/4)(U_TF)+resto positivo`, ni una dominación equivalente demostrada. La covarianza geométrica, el término v_s y Π_α no son por definición el gamma, el peine y el polo del paper. No se los etiqueta así por analogía.

Por tanto el objetivo auxiliar de esta ronda **sí está resuelto**: signo de R (negativo definido) y completación positiva genuina del objeto conservado. El objetivo principal D continúa activo. El residuo concreto es una realización de (7) sobre los tests F, con identidad exacta de los términos y dominio/colas, que vincule este objeto distinto a Q_T sin introducir su raíz cuadrada ni asumir su signo.

## 9. Puertas del programa

- **thm:sos:** (5) no paga el peine puntual por μ₀−S_T ni pide al arquimediano una constante. No cae en ese enunciado por forma. Tampoco se ha construido un certificado de def:PD para Q_T.
- **P1:** la identidad positiva corresponde a R, objeto definido independientemente por una integral renormalizada; no a una raíz abstracta de Q_T. Si se propone U_T, debe demostrarse su enlace, no su existencia abstracta.
- **W₂/BR:** no se han construido los tests/restos de esos esquemas. El kernel de índices enteros no se presenta como kernel efectivo de alturas por mero cambio de nombre.
- **Ecuación funcional:** Poisson interviene en convergencia y en la Mellin completa; no se usa una identidad asintótica de Gonek ni se suprime un resto.
- **Sector polar:** la aparición del rango uno v_s es explícita. No se ha demostrado que corresponda a cosh(x/2); no se elimina ni se identifica sin mapa.

**Estado final del constructor: PSD COMPLETION PROVED para −R_α (0<α<1/2), auditoría final favorable. Enlace con Q_T y fila D: OPEN, trabajo activo.**

## 10. Test de especificidad: la completación también sobrevive a borrar primos

Sea P>1 squarefree, `δ_P=∏_{p|P}(1−1/p)` y

`τ_P(y)=Σ_{n≠0,(n,P)=1}exp(−πn²y)=Σ_{a|P}μ(a)τ(a²y)`.

Su masa principal es δ_P c(y); el término constante desaparece porque `Σ_{a|P}μ(a)=0`. Para índices d,e coprimos con P, definimos q_d^P, B_y^P como antes usando τ_P y

`R_α^P(d,e)=∫_0^∞ y^(α−1)[B_y^P(d,e)−δ_P c(y)G_1(d,e)]dy`.

Las integrales convergen para 0<α<1/2: en cero la cancelación es incluso exponencial; en infinito basta la cola y^(−1/2). El centro μ_1 sigue siendo Σa_d/d en los índices supervivientes.

Para `ν_y^P=δ_P c E_1^P−τ_P E_y^P`, donde P_t^P fija v_p=0 para p|P y conserva las otras geométricas, la inclusión–exclusión y (3) dan

`∫_0^∞ y^(α−1)ν_y^P(X_k)dy`

`=−Z_α k^(−s)∏_{p|P}(1−p^(−s))=−Z_α^P E_s^P X_k`,

`Z_α^P:=Z_α∏_{p|P}(1−p^(−s))<0`, `(k,P)=1`.

Repitiendo exactamente el Lema 1:

`−R_α^P(A)=(−Z_α^P)E_s^P|A−μ_1(A)|²`

`            +∫_0^∞ y^(α−1)τ_P(y)|E_y^P A−μ_1(A)|²dy ≥0`.

Es definida positiva en familias finitas distintas de índices d≥2 coprimos con P. Los indicadores que contienen primos borrados son nulos en esta ley y no se cuentan como direcciones estrictas.

**Resultado del test:** la positividad auxiliar completa es **heredada por toda eliminación finita** con su theta y densidad correspondientes. El teorema de §5 sigue siendo válido e independiente, pero su signo por sí solo no separa la forma de conductor1 del falsificador. La premisa extra del enlace debe usar la FE autodual completa de θ_Z y la identidad de su arquimediano/polo; no basta usar esta completación PSD.

Esta conclusión no se usa como NO-GO general: un enlace específico que falle para τ_P todavía podría servir. Debe construirse explícitamente, incluyendo el defecto de autodualidad, en vez de inferirlo de (5).
