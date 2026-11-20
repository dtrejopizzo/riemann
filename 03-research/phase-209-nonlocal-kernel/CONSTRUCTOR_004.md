# CONSTRUCTOR_004 — Cruces coprimos desnormalizados en parámetro crítico

2026-10-18. Constructor. **PROVED usando el Teorema 1 de ANTICORRELATION_003** (concavidad geométrica puncturada, aprobado en AUDIT_003). Revisión final de esta nota: AUDIT_004. No se usan ceros. El nodo sigue OPEN.

## 0. Razón nueva frente al índice y alcance

Consultados nuevamente las entradas L2_012, Helson, Tate/Poisson, SPEC005, INV_C y las búsquedas de mezcla/covarianza del índice, grid y crucigrama. También CONSTRUCTOR_002 y ANTICORRELATION_003.

No se reintenta positividad de |ζ|², una AFE, una norma Helson ni la positividad homogénea de theta. La diferencia exacta es ésta: **la covarianza entre divisores coprimos tiene contratermino principal nulo**, por lo que su desnormalización Mellin converge ya en α=1/4 y conserva signo estricto sin continuación. Esto usa la concavidad de τ=θ−1 y una cancelación exacta del límite de densidades de divisibilidad. No estaba en el cálculo genérico de CONSTRUCTOR_002, que trató G₀ sin separar sus entradas nulas.

Es un resultado sobre cruces aritméticos. No es todavía positividad cuadrática del operador del nodo, ni un kernel efectivo en el espacio de alturas. No se cuenta la PSD de una matriz de covarianza como el resultado nuevo: el resultado nuevo de esta ronda es **signo estricto de un cruce desnormalizado y convergente en el parámetro crítico**, con fórmula exacta y dependencia genuina de ambos índices.

## 1. Definición y asintótica exacta en cero

Sean θ, τ y q_y de CONSTRUCTOR_002. Para d,e≥2 coprimos, l=de y

`B_y(d,e)=τ(y)Cov_y(X_d,X_e)`

`          =τ(d²e²y)−τ(d²y)τ(e²y)/τ(y)`.

Por ANTICORRELATION_003, `B_y(d,e)<0` para todo y>0.

**Lema 1 (PROVED).** Para d,e fijos coprimos, y↓0,

`B_y(d,e)=−(1−1/d)(1−1/e)/(1−√y)+O_{d,e}(y^(−M)exp(−c_{d,e}/y))`,

para algunas constantes c>0 y M finito. En particular

`B_y(d,e)=−(1−1/d)(1−1/e)+O_{d,e}(√y)`.

**Prueba.** Poner r=√y. Poisson da, para k fijo,

`τ(k²y)=1/(kr)−1+O_k(r^(−1)exp(−π/(k²y)))`.

Sustituir los tres factores; τ(y)~1/r permite dividir sin problemas para y pequeño. La parte algebraica exacta es

`(1/(der)−1)−[(1/(dr)−1)(1/(er)−1)]/(1/r−1)`

`=−[(d−1)(e−1)/(de)]/(1−r)`.

El resto sigue siendo exponencial con una potencia fija de y. ∎

En y→∞, `B_y=O_{d,e}(exp(−c'_{d,e} y))`, pues τ(k²y)~2exp(−πk²y) y `τ(d²y)τ(e²y)/τ(y)` decae con exponente π(d²+e²−1)>0.

**Por qué cambia el cálculo crítico.** El término general `G₀(d,e)=(gcd(d,e)−1)/(de)` es cero para d,e coprimos. La parte `y^(−1/2)G₀` que obligaba a renormalizar en CONSTRUCTOR_002 desaparece exactamente, no por una cota.

## 2. Un signo Mellin real en α=1/4

Defino

`A_α(d,e)=−∫_0^∞ y^(α−1) B_y(d,e)dy`, `(d,e)=1`, d,e≥2.

**Teorema 2 (PROVED).** Para todo α>0 y cada par coprimo d,e≥2,

`0<A_α(d,e)<∞`.

En particular A_(1/4) existe como integral ordinaria estrictamente positiva. No hay continuación analítica ni sustracción de un contratermino en esta afirmación.

**Prueba.** Lema 1 da integrabilidad en cero para α>0; el decaimiento exponencial da integrabilidad en infinito. El signo es estricto en cada escala por la concavidad puncturada. ∎

Esto conserva signo al **desnormalizar**, que era la pérdida identificada en CONSTRUCTOR_002. Sólo se ha recuperado esta propiedad en los cruces coprimos; no en toda la matriz.

## 3. Dependencia genuina de dos índices, incluso después de integrar

**Teorema 3 (PROVED).** Para todo α>0,

`A_α(3,10)>A_α(2,15)>0`,

aunque ambos pares tienen producto 30. Por tanto A_α no es de la forma w(de).

**Prueba.** Sea f(x)=logτ(exp x), estrictamente cóncava. Los pares

`log(4y),log(225y)` y `log(9y),log(100y)`

tienen igual suma, y el segundo es estrictamente más próximo al punto medio. La concavidad estricta implica

`τ(9y)τ(100y)>τ(4y)τ(225y)`.

El término τ(900y) de B_y es igual para ambos pares y τ(y)>0. Así `−B_y(3,10)>−B_y(2,15)>0` para cada y. Integrar. ∎

La diferencia es estructural respecto de w(mn) del término principal de Gonek. No se usa Gonek ni su error. **No se infiere** de este teorema que una representación en alturas de A_α quede fuera de toda álgebra efectiva tras restricciones: ese operador aún no está identificado.

## 4. Mellin exacto y peso d^(−1/2)e^(−1/2)

Fijar 0<α<1/2. Sean

`Z_α=2π^(−α)Γ(α)ζ(2α)`

y

`J_α(d,e)=∫_0^∞ y^(α−1)[τ(d²y)τ(e²y)/τ(y)−(1/(de))y^(−1/2)]dy`.

La segunda integral converge: en cero el corchete es O(1); en infinito la cola sustraída es integrable para α<1/2. No se le atribuye signo.

La identidad Mellin regularizada de theta es

`∫_0^∞ y^(α−1)[τ(k²y)−k^(−1)y^(−1/2)]dy=Z_α k^(−2α)`.

Se obtiene por cambio de variable y la fórmula elemental de continuación de la Mellin de τ, dividiendo la integral en 1. No hay suma sobre ceros.

Como l=de y los contraterminos son **idénticos**, se restan exactamente y resulta

`A_α(d,e)=J_α(d,e)−Z_α(de)^(−2α)>0`.                       (1)

En α=1/4:

`A_(1/4)(d,e)=J_(1/4)(d,e)−[2π^(−1/4)Γ(1/4)ζ(1/2)]/√(de)>0`.

Así aparece un término exacto con peso **1/√(de)** sin perder el signo del cruce total. La integral J no es el gamma conductor1 del nodo y el escalar Z no lo reemplaza: identificar los factores de Γ por parecido no demostraría el enlace.

La desigualdad (1) es un enunciado verdadero entre dos cantidades explícitas. No se afirma que sea el nodo reescrito ni que su margen domine un déficit gamma en todos los tests.

## 5. Lo que sigue sin estar pagado: diagonal y mismo primo

Si gcd(d,e)>1, entonces G₀(d,e)>0 y

`τ(y)Cov_y(X_d,X_e)~y^(−1/2)G₀(d,e)`.

La integral ordinaria en α=1/4 diverge positivamente. Por ello los cruces coprimos no se pueden reunir con la diagonal en una matriz PSD crítica mediante la misma integral sin renormalizar.

Para una familia finita de potencias de primos, los bloques **entre primos distintos** tienen todos sus cruces finitos y negativos después de desnormalizar; los bloques de un mismo primo necesitan los contraterminos de CONSTRUCTOR_002. Éste es el reparto exacto, no una afirmación sobre el número de modos del nodo.

Se puede formar un laplaciano finito con pesos A_(1/4)>0 y energía `Σ A(d,e)|a_d−a_e|²≥0`; pero su diagonal sería una asignación nueva. **No se propone como certificado**: demostrar que esa diagonal es el arquimediano/polar requerido sería todo el enlace pendiente. No se cuenta esta maniobra como objeto signo obtenido.

## 6. Puertas de O1

1. **SOS/P1:** (1) no exige identidad puntual μ₀−S_T ni paga Γ mediante constante. No cae literalmente en thm:sos. Tampoco es una factorización exacta de Q_T; no se reclama superar P1 para el enlace.
2. **BR/W₂:** no se construyeron los tests y restos de BR. Este kernel de pares de divisores no se identifica con P36-4 ni con el conjunto relajado W₂. No se usa ρ1‴.
3. **Especificidad:** quitar índices de un kernel fijo conserva el signo de los índices restantes; eso NO es cambiar la ley gaussiana por la ley con un primo eliminado. Para esa ley modificada no se ha demostrado aquí ni herencia ni fallo de la anticorrelación. La completitud entra en las identidades de observables y en la marginal del apartado siguiente. El signo cruzado solo no supera el falsificador.
4. **Dominio efectivo:** A está definido para pares coprimos de índices enteros, no como operador K(t,t′) sobre todo PW_T. Falta una realización que produzca Q_T y los bloques diagonal/mismo primo. No hay conclusión sobre dominio completo, impares ni polar.

## 7. Mezcla de escalas: una cancelación exacta adicional en σ>1

Sea α=σ/2>1/2 y

`μ_α(dy)=τ(y)y^(α−1)dy/Z_α`.

Es una probabilidad. Mezclando P_y(N=n) contra μ_α, la marginal es

`P_α(N=n)=|n|^(−2α)/(2ζ(2α))`, n≠0.

Por el producto de Euler completo, las variables `Y_p=v_p(|N|)` son independientes geométricas en esta marginal. Si p≠q, la fórmula de covarianza total da la cancelación exacta

`−E_{μ_α}Cov_y(Y_p,Y_q)=Cov_{μ_α}(r_p(y),r_q(y))>0`,

`r_p(y)=E_yY_p=Σ_{j≥1}q_y(p^j)`.

El lado derecho tiene representación genuina en dos escalas:

`(1/2)∫∫[r_p(y)−r_p(z)][r_q(y)−r_q(z)] μ_α(dy)μ_α(dz)`.

Su signo también se ve directamente: la concavidad estricta de f implica que cada q_y(d) es estrictamente decreciente en y; por tanto cada r_p lo es y ambos factores de diferencias tienen igual signo para y≠z. Las integrabilidades se deducen del segundo momento de log|N| bajo la ley zeta con σ>1 y Jensen condicional.

Para una familia finita de primos y coeficientes a_p se obtiene la identidad cuadrática exacta

`Σ_p |a_p|² p^(−σ)/(1−p^(−σ))²`

`=E_{μ_α}Var_y(Σ a_pY_p)+Var_{μ_α}(Σ a_pr_p(y))`.

Ambas formas derechas son PSD, pero las entradas cruzadas de la primera son negativas y las de la segunda positivas; se cancelan **por independencia euleriana**, no por norma abstracta. Borrar un primo conserva una ley zeta condicionada con independencia en los primos restantes; para exigir todos los observables originales hay que nombrar la identidad de completitud que se pierde. La cancelación de dos primos supervivientes sola no es específica de completitud total.

### Qué falla exactamente al pasar a α=1/4

μ_α deja de ser una probabilidad: su masa en cero diverge como `∫ y^(α−3/2)dy`. No existe la fórmula de covarianza total con esa medida normalizada en α=1/4. No se la continúa como identidad de formas PSD.

**Pero los cruces desnormalizados individuales del Teorema 2 sí continúan como integrales ordinarias** porque su G₀ es cero. Así, la mezcla PSD global se rompe en la normalización/diagonal, mientras el signo de anticorrelación entre divisores coprimos sobrevive al peso crítico. Ésta es la distinción nueva y exacta que permite trabajar sobre los cruces sin anunciar un transporte de norma Helson desde σ>1.

## 8. Próximo enlace por construir

El dato utilizable es A_(1/4): signo estricto, convergencia ordinaria, dependencia de dos índices y término Mellin explícito 1/√(de). Falta obtener del mismo objeto la **diagonal renormalizada** y la realización en el dominio del nodo, con el arquimediano y el sector polar correctos.

No se ha probado que sumar los cruces pague esos términos. Tampoco se ha probado que pueda elegirse una diagonal favorable. El resultado positivo de esta nota es el cruce crítico y la identidad de mezcla en σ>1, no el cierre de O1 ni de D.

## 9. Todas las potencias de dos primos: el cruce crítico también converge

La extensión siguiente mantiene p,q fijos distintos. **No intercambia una suma sobre todos los primos con Mellin.**

**Lema 4 (PROVED).** Para y≤1/4, c=y^(−1/2)≥2 y enteros coprimos d,e≥2,

`0<−B_y(d,e)≤min(3/2, 2c/(de))`.

**Prueba.** Comparar la suma gaussiana decreciente con su integral da `τ(k²y)≤c/k`. Poisson da `τ(k²y)≥c/k−1`. En particular τ(y)≥c−1. Por el signo ya probado,

`−B=τ(d²y)τ(e²y)/τ(y)−τ(d²e²y)`

`≤c²/[de(c−1)]−(c/(de)−1)=1+c/[de(c−1)]≤3/2`.

También `−B≤τ(d²y)τ(e²y)/τ(y)≤2c/(de)`. ∎

Para p≠q primos, sean

`B_y^val(p,q)=τ(y)Cov_y(v_p(|N|),v_q(|N|))=Σ_{j,k≥1}B_y(p^j,q^k)`.

Las sumas convergen para cada y>0 y todos sus términos son negativos. Tomando `J=ceil(log_p c)`, `K=ceil(log_q c)`, el rectángulo j≤J,k≤K aporta O_pq(log²c), y fuera de él la cota `2c p^(−j)q^(−k)` da colas geométricas O_pq(1). Por tanto

`0<−B_y^val(p,q)=O_pq(1+log²(1/y))` cuando y↓0.

Cuando y≥1,

`−B_y^val(p,q)≤[Σ_j τ(p^(2j)y)][Σ_k τ(q^(2k)y)]/τ(y)`

`≤C_pq exp[−π(p²+q²−1)y]`.

La última cota sigue de la dominación gaussiana de ambas sumas por su primer término y `τ(y)≥2exp(−πy)`.

**Teorema 5 (PROVED).** Para todo α>0 y cada par fijo de primos distintos,

`A_α^val(p,q)=−∫_0^∞ y^(α−1)B_y^val(p,q)dy`

`=Σ_{j,k≥1}A_α(p^j,q^k)∈(0,∞)`.

La igualdad es Tonelli sobre términos no negativos. En particular, **el cruce de dos factores primos completos tiene signo estricto e integral ordinaria en α=1/4**, no sólo cada truncación en potencias.

Para 0<α<1/2, la fórmula (1) se suma también sin ambigüedad:

`A_α^val(p,q)=J_α^val(p,q)−Z_α/[(p^(2α)−1)(q^(2α)−1)]`,

`J_α^val(p,q):=Σ_{j,k≥1}J_α(p^j,q^k)`.

La convergencia absoluta de esta última suma se sigue de `J=A+Z_α(de)^(−2α)`, la convergencia positiva de ΣA y las dos series geométricas. En α=1/4 el término explícito es

`−Z_(1/4)/[(√p−1)(√q−1)]`.

Al multiplicar por log p·log q aparecen exactamente los factores locales críticos `log p/(√p−1)` y `log q/(√q−1)`. No se suman aquí sobre todos los p,q; esa cola global sigue pendiente.

## 10. Dos límites que no deben desaparecer al integrar

- Desnormalizar por τ cancela el factor exterior, pero **queda** el cociente `τ(d²y)τ(e²y)/τ(y)`. Sólo una parte de (1) es Mellin clásico; el kernel entero no lo es.
- El Teorema 3 prueba que A no es w(de) en el dominio de todos los enteros coprimos. Si se restringe a pares de potencias de primos distintos, el producto determina ambos factores salvo orden; en ese conjunto cualquier kernel simétrico puede etiquetarse por el producto. No usar ese etiquetado como prueba de reducción ni de evasión de Gonek: la realización efectiva en alturas sigue siendo imprescindible.

A_α tiene entradas positivas; eso **no afirma PSD de su matriz**. Tampoco B crítico con diagonal renormalizada es PSD por el signo negativo de sus cruces. Los teoremas de esta nota sólo sostienen las afirmaciones de signo e integrabilidad expresamente enunciadas.

**Revisión final AUDIT_004:** teoremas aceptados con el alcance declarado;
corregida la distinción entre quitar índices y cambiar la ley por borrado.
No quedan objeciones pendientes a las pruebas de esta nota.
