# CONSTRUCTOR_007 — Módulo de contracciones aritméticas del kernel −R

2026-10-18. Constructor. **PROVED, revisión final favorable en AUDIT_007:** representación multiplicativa por contracciones en la completación canónica de −R_α, con defecto positivo explícito y normalización crítica. No es todavía una representación de la forma Q_T.

## 0. Corpus y razón nueva escrita

Consultados índice, grid y crucigrama por contracciones, isometrías, Frobenius, módulos y semigrupos de dilataciones. Entradas pertinentes: L2_016, L2_025–027, BUILD_R1_001 X1.0 (normas y ángulos entre datos exteriores, NO-GO como signo), INV_D (dilataciones unitarias y carácter), P1_BBSTAR y CELL_001.

No se reintenta una cota de ángulo entre r y D_nr ni se afirma que una dilatación unitaria genere signo. **Razón nueva:** el espacio de Hilbert es el del kernel independiente −R_α recién identificado; la aritmética de divisibilidad y la gaussiana definen dos acciones que se entrelazan exactamente. El defecto no se estima por normas separadas: se calcula como una integral positiva con multiplicador explícito `1−q_n`. La ley isométrica del primer factor exige conservar cada primo observado. Esto cambia el objeto y la hipótesis respecto de las rutas indicadas, sin demostrar por sí solo un enlace al gamma del nodo.

## 1. Dominio y norma positiva ya probada

Sean s=2α∈(0,1), C_α=−Z_α>0. Sobre el álgebra de observables finitos de divisibilidad, tomo representantes **Haarcentrados**

`𝒜₀={A=Σ finite a_d X_d : E_1A=0}`,

permitiendo X_1=1 para centrar. Para este dominio, CONSTRUCTOR_005 da

`𝒦_α(A)=−R_α(A)=C_α E_s|A|²+Π_α(A)`,

`Π_α(A)=∫_0^∞ y^(α−1)τ(y)|E_yA|²dy`.

La condición de centro hace converger Π en cero. Defino 𝓗_α como la completación de 𝒜₀ para 𝒦_α. No se identifica esta completación con el dominio de Q_T.

Puede realizarse sin asumir clausurabilidad de operadores auxiliares: cerrar en el producto de Hilbert la imagen

`A ↦ (√C_α A, y↦E_yA)`

en `L²(P_s) ⊕ L²(y^(α−1)τ(y)dy)`. La norma de esa imagen es exactamente 𝒦_α.

## 2. Acción de divisibilidad y memoria geométrica

Para n≥1, defino

`(D_nA)(N)=1_{n|N} A(N/n)`;

sobre generadores, `D_nX_d=X_(nd)`. Entonces `D_mD_n=D_(mn)`.

**Lema 1 (PROVED).** Para t>0 y A finito,

`E_t(D_nA)=n^(−t)E_tA`,

`E_t|D_nA|²=n^(−t)E_t|A|²`.

Es memoria geométrica de las valuaciones bajo P_t: condicionando v_p≥v_p(n), la diferencia tiene la misma ley independiente. En particular D_n conserva 𝒜₀ porque `E_1D_nA=(E_1A)/n=0`.

En la gaussiana puncturada,

`E_y(D_nA)=q_n(y)E_(n²y)A`, `q_n(y)=τ(n²y)/τ(y)`.

Esto sale del cambio N=nM en la suma; es exacto y no usa fase estacionaria.

## 3. Contracción normalizada y defecto positivo

Defino `V_n=n^(s/2)D_n`. Su acción en el factor aritmético L²(P_s) es isométrica por el Lema 1. En el factor gaussiano, para f(y)=E_yA, actúa

`(G_nf)(y)=n^(s/2)q_n(y)f(n²y)`.

Cambio u=n²y da

`Π_α(V_nA)=∫_0^∞ u^(α−1)τ(u)q_n(u/n²)|E_uA|²du`.

**Teorema 2 (PROVED).** V_n se extiende a una contracción en 𝓗_α, `V_mV_n=V_(mn)`, y sobre el núcleo algebraico

`𝒦_α(A)−𝒦_α(V_nA)`

`=∫_0^∞ u^(α−1)τ(u)[1−q_n(u/n²)]|E_uA|²du ≥0`.   (1)

Para n>1, la concavidad puncturada da q_n(z)<1/n para todo z>0, de modo que

`𝒦_α(A)−𝒦_α(V_nA) ≥(1−1/n)Π_α(A)`.              (2)

No se necesita (2) para la contracción: q_n≤1 ya basta. La cota estricta ofrece el defecto explícito.

**Prueba.** Restar las dos normas; el término C_α E_s|A|² cancela por la isometría exacta. La representación multiplicativa es algebraica y se conserva al extender por continuidad. ∎

En α=1/4, la normalización es `V_n=n^(1/4)D_n`. Esto corresponde a una ley de normas n^(−1/2) antes de normalizar, no debe confundirse con un coeficiente n^(−1/2) que se haya identificado ya en Q_T.

## 4. Adjunto en el factor gaussiano: cálculo exacto

Sobre `ℒ_α=L²(y^(α−1)τ(y)dy)`, el operador G_n es acotado y

`(G_n* g)(u)=n^(−s/2)g(u/n²)`,

`G_n*G_n f(u)=q_n(u/n²)f(u)`.

**Prueba.** En el producto interno de G_nf con g, cambiar u=n²y; el factor τ(y)q_n(y) se vuelve τ(u), y la potencia deja n^(−s/2). ∎

Por tanto `I−G_n*G_n` es exactamente el multiplicador positivo de (1). Además `‖G_n‖≤1/√n` para n>1 y `G_mG_n=G_(mn)` por cancelación telescópica de los cocientes de τ.

**Cautela:** no se identifica el adjunto de V_n en 𝓗_α con una restricción del adjunto del producto de factores. La imagen cerrada puede ser sólo invariante, no reductora. Las identidades de norma y de semigrupo no requieren esa identificación.

## 5. Borrado de un primo: qué identidad aritmética falla

En la ley P_s^P de CONSTRUCTOR_005 §10, si p|P entonces X_p=0 casi seguramente. En particular `D_pA=0` como observable de esa ley, mientras para A≠0

`p^(−s)E_s^P|A|²>0`.

Por ello la isometría normalizada de D_p del Lema 1 **no existe con esa misma ley borrada y el mismo primo p**. Para n coprimo con P, la memoria geométrica sigue valiendo y no se exige distinguir esas acciones supervivientes.

Esto identifica una propiedad conjunta que exige todos los primos: la acción isométrica normalizada del factor aritmético para **cada** n≥1, entrelazada con la gaussiana completa. No prueba todavía que esa propiedad obligue al signo de Q_T ni que un cociente por acciones nulas no genere otro módulo positivo.

## 6. Conexión exacta con la FE ya calculada

El factor gaussiano utiliza τ y Π, cuya inversión completa fue probada en CONSTRUCTOR_006. En α=1/4 el cambio de escala y↔1/y conserva el parámetro y transforma los incrementos de τ en diferencias de m entre y y y/d². Las acciones D_n de este memo son compatibles con las dilataciones enteras que aparecen allí.

No se ha demostrado que esa inversión actúe como una involución unitaria cerrada sobre 𝓗_α que conjugue V_n con un operador adjunto concreto. La fórmula del adjunto gaussiano, por sí sola, no proporciona tal involución global. Éste es un paso verificable adicional, y no se lo sustituye por la FE de un símbolo multiplicador.

## 7. Residuo de enlace y alcance

Ahora se dispone de:

- norma positiva independiente −R_α;
- una representación explícita de todos los enteros por contracciones;
- un factor aritmético isométrico con exponente s=1/2 en el caso crítico;
- defectos gaussianos positivos calculados exactamente;
- una FE de Π y un defecto de un perfil que falla tras el borrado.

Falta identificar una forma o traza de estas acciones, definida y convergente sobre todos los tests F del nodo, que dé exactamente el gamma y el peine de Q_T, y tratar su polo. Ninguna traza se da por existente, ni se importa una identidad de carácter cuyo signo sea el objetivo mismo.

Las desigualdades (1)–(2) son resultados positivos del módulo construido; **no se etiquetan como desigualdad de Q_T**. No cierran D ni O1. Constituyen un objeto más específico que una covarianza aislada y dejan un enlace concreto por construir: la inversión de §6 y una identidad de forma sobre el portador del paper.

## 8. Límite adicional de especificidad: estructura de monoide

La memoria geométrica y las leyes de norma de D_n, tomadas aisladamente,
usan sólo la estructura multiplicativa y la norma n. La desigualdad
q_n<1/n vale también para un factor de escala real n>1. Por ello una parte
del cálculo puede formalizarse en otros monoides con normas; no se afirma
que el módulo de contracciones solo distinga la aritmética de todos los
enteros frente a sistemas de Beurling.

Las igualdades adicionales que aquí sí se deben conservar son la realización
de los observables por divisibilidad efectiva de enteros, la identidad con
el R renormalizado concreto y la FE de un único perfil de CONSTRUCTOR_006.
No se ha probado que esas igualdades produzcan la forma de Q_T. El test del
primo borrado en §5 localiza una identidad que falla en esa ley, pero no
constituye una batería completa de especificidad para el enlace final.


## Actualización de dominio — continuación015

CONSTRUCTOR_015_DOMAIN_AND_CONE resuelve con otra sucesión la cuestión
que aquí quedó abierta: H=L²(P_s)⊕V y el operador T de007 no es clausurable.
El vectorvertical fuerte proviene de likelihoodtilts sobre primosaltos,
no de la sucesiónprimorial divergente de008. No se afirmaV=todoGaussian
ni invariancia porla FE ambiental; el enlaceQ sigueOPEN. AUDIT_015 favorable.
