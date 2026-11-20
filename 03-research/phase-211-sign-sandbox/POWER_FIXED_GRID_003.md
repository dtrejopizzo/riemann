# POWER_FIXED_GRID_003 — Escalera fija, eliminación completa y seis casos certificados

Estado: PROVED (identidad de eliminación, órdenes 1–6 y falsificador algebraico). OPEN (control uniforme de todos los órdenes). Papers intactos.

## 1. Antecedentes y razón nueva

Consultados ROUTES-TRIED-INDEX/README.md:393,655 y entradas de rondas 001–002; NODE_001:195; grid part3:12, part5:7 y MASTER_GRID, entradas recientes; CROSSWORD-TO-D, entradas recientes; POWER_BRIDGE_002, POWER_CONE_001 y POWER_THREE_002. La eliminación Schur/Pick es conocida, no se vende como objeto nuevo. La diferencia frente al rango alto de ronda 002 es la escalera FIJA a_j=32+j, que posee el puente denso probado en revisión independiente. Se calcula una transformación exacta del dato completo (no separado en Gamma, prime, polar) y se certifican sus seis primeros pasos por aritmética racional con restos explícitos.

## 2. Eliminación exacta que conserva todas las cancelaciones

Sea s_j=63/2+j, L_j=L(32+j), K_ij=(L_i+L_j)/(s_i+s_j). Ponga

    x_j=j/(63+j), q_j=(L_j-L_0)/(L_j+L_0).

Entonces K es congruente por una diagonal estrictamente positiva con

    B_ij=(1-q_i q_j)/(1-x_i x_j).

En efecto K_ij=w_i w_j B_ij, donde

    w_i=(L_i+L_0)(1-x_i)/(2 sqrt(L_0 s_0)).

No se elimina por separado ninguna componente del dato: L incluye las tres piezas y sus cancelaciones exactas. La identidad polar cruzada de POWER_THREE_002 §1 sigue aplicada.

Para r=0,1,..., defina alpha_r=q_r^(r), con q_j^(0)=q_j. Si |alpha_r|<1 y los denominadores 1-alpha_r q_j^(r) son no nulos,

    q_j^(r+1) = [(q_j^(r)-alpha_r)/(1-alpha_r q_j^(r))]
                 /[(x_j-x_r)/(1-x_j x_r)],  j>r.             (E)

Cada paso de eliminación, cuando está definido, es una congruencia diagonal real invertible de la matriz restante con (1-q_i^(r+1)q_j^(r+1))/(1-x_i x_j). Prueba: aplicar las transformaciones fraccionarias Q=(q-alpha)/(1-alpha q), X=(x-x_r)/(1-x_r x); ambas mandan el pivote a cero. El nuevo núcleo es congruente al anterior; al restar la fila/columna del pivote 1, su complemento es

    X_i X_j [1-(Q_i/X_i)(Q_j/X_j)]/(1-X_i X_j).

La transformación del denominador a los x originales sólo introduce factores diagonales positivos. Los factores procedentes de 1-alpha_r q_j^(r) pueden tener signo arbitrario fuera del régimen positivo; basta que sean no nulos para conservar inercia por congruencia. Si la matriz es positiva definida, sus diagonales implican |q_j^(r)|<1, de modo que esos factores son positivos y no nulos automáticamente. Como x_j>x_r para j>r, dividir por X_i no altera la inercia. Por inducción la matriz de orden n es positiva definida exactamente cuando los primeros n parámetros están definidos y |alpha_r|<1. Esta es una identidad algebraica finita, sin hipótesis de extensión analítica.

## 3. Caso A=32 y órdenes hasta seis, certificados exactamente

El archivo `tools/power_fixed_grid_003.py` usa únicamente enteros y `fractions.Fraction` para la prueba. No llama a funciones especiales numéricas ni a aritmética flotante para certificar. Los seis parámetros satisfacen los siguientes intervalos, con extremos racionales de denominador 10^20:

| r | numerador inferior | numerador superior |
|---|---:|---:|
|0|0|0|
|1|51259972990094569363|51259972990094569364|
|2|-25992254732307031752|-25992254732307031751|
|3|31593841033126355467|31593841033126355468|
|4|-25282748230749984903|-25282748230749984902|
|5|29837716612495345653|29837716612495345654|

Todos están estrictamente en (-1,1). Independientemente, la eliminación LDL intervalar da estos pivotes, con extremos de denominador 10^30:

| r | numerador inferior | numerador superior |
|---|---:|---:|
|0|27353961447421353405359957407|27353961447421353405359957408|
|1|4849334253718313144169652|4849334253718313144169653|
|2|3982421698012363219073|3982421698012363219074|
|3|6513628495257110139|6513628495257110140|
|4|18108703084109592|18108703084109593|
|5|70566563152624|70566563152625|

En particular queda probado P3 para A=32,h=1; el tercer pivote es mayor que 3.982421698e-9. También queda probado signo para toda mezcla real de las seis potencias X^-32,...,X^-37. No es una afirmación meramente numérica: cada intervalo es racional y deriva de series con resto.

### Fuentes de los intervalos

* log x: reducir x a [1,2] mediante potencias de dos; usar 120 términos de 2 atanh((x-1)/(x+1)); resto <=2t^241/[241(1-t²)].
* pi: fórmula de Machin 16atan(1/5)-4atan(1/239), 100 términos alternados, error del siguiente término.
* gamma: H_1000-log1000-1/2000+Σ_{k=1}^{12}B_{2k}/(2k1000^{2k}); error en valor absoluto <=|B_26|/(26*1000^26), por el resto de Euler–Maclaurin para la función digamma. Se usa B_26=8553103/6.
* psi entero/semientero: psi(m)=H_{m-1}-gamma, psi(m+1/2)=-gamma-2log2+2Σ_{k=1}^m1/(2k-1).
* zeta y zeta': sumar n<=50 y acotar colas por las integrales de x^-a y (log x)x^-a; son decrecientes en ese rango. Así la certificación no necesita tablas de primos ni Λ.
* Cada operación redondea los extremos hacia afuera a múltiplos de 10^-60. El programa imprime únicamente intervalos racionales como certificado final.

Comando reproducible: `python3 03-research/phase-211-sign-sandbox/tools/power_fixed_grid_003.py`.

## 4. Falsificador: todos los pares y la monotonía NO bastan para tres

No se puede extrapolar POWER_CONE_001 mediante el lema «L creciente y L(s)/s decreciente implican signo a todo orden». Considere los tres sitios y valores racionales

    s=(1,5/3,3), L=(1,3/2,121/79).

L aumenta estrictamente y L/s disminuye estrictamente; por tanto cada par pasa exactamente el criterio de POWER_CONE_001. La matriz completa es

    [1,       15/16,      50/79;
     15/16,   9/10,       1437/2212;
     50/79,   1437/2212,  121/237].

Sus tres menores principales de orden dos son 27/1280, 2059/18723 y 916539/24464720, todos positivos. Sin embargo

    det K=-332001/391435520<0.

En coordenadas de eliminación, x=(0,1/4,1/2), q=(0,1/5,21/100), alpha_1=4/5 pero alpha_2=-665/332, fuera del intervalo permitido. Es un falsificador algebraico al paso de pares a triples, NO al dato L del paper.

## 5. Residuo exacto y criterio de avance

El nuevo objetivo concreto es controlar (E) para los valores reales L(32+j), demostrando |alpha_r|<=1 para todo r. Las seis verificaciones no prueban una ley de alternancia ni una cota uniforme 0.6; sólo muestran los seis pasos declarados. La recurrencia conserva todo el dato aritmético, pero todavía no se ha obtenido un resto de signo que se preserve al aplicarla. Toda afirmación uniforme requiere esa pieza nueva. La hipótesis de dos puntos por sí sola está explícitamente falsificada por §4.
