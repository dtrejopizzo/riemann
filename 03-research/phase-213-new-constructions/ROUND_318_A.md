# Corte en X^(2/3) con error cuadrático medio suficiente para el signo global

Fijar la escala diádica X, V=X^(2/3), H=ceil(X^(1/6)) y D=X^o(1), D≥2. Mantener fijos en [X,2X] los pesos g de 317, con q=⌊D⌋+1. Para x en ese intervalo sea I(x,t) el promedio, en j=0,…,H−1, de

    Σ_(D<n≤floor(x/V)−j) g(n) C_t(x/n).

Entonces uniformemente en 0≤t≤2,

    (X^(−1)∫_X^(2X) |C_t(x)+I(x,t)|² dx)^(1/2) ≪_ε X^(1/2+ε).

Todos los argumentos de I están entre X^(2/3) y x/D. En particular el signo global equivale a que la media en x y t∈[1,2] de (−I(x,t))₊ sea O_ε(X^(1/2+ε)) en todas las escalas diádicas. Esta reducción sustituye la garantía puntual de 317 por una garantía cuadrática media; el criterio de suficiencia no necesita control puntual.

**Eliminar el término de borde.** La media completa de g contra C_t ya cumple el techo puntual por 317. Escribir G(u)=Σ_(d≤D)μ(d) r_q(u/d), donde r_q(v)=⌊v⌋ mod q en [0,q−1]. Para N=⌊x/V⌋−j la cola omitida es Σ_(m≤x/N)c_t(m)[G(x/m)−G(N)] (extremo con igualdad aporta cero). Para m≤V es válida para todos los j. Los m adicionales están en un tramo de longitud O(1+HV²/X), que cuesta O_ε(X^(1/2+ε)) por |G|≤qD y |c_t(m)|≪_ε m^ε. En cada término d, al promediar G(N) sobre H enteros consecutivos, el período qd tiene media (q−1)/2. El error de un período parcial es O(q²d/H). Sumado en d y multiplicado por |C_t(V)|≪_ε V^(1+ε), cuesta O_ε(X^(1/2+ε)). Así la cola sólo requiere acotar en media cuadrática

    E(x)=Σ_(m≤V)c_t(m) Σ_(d≤D)μ(d)[r_q(x/(dm))−(q−1)/2].

**Frecuencias de los residuos.** La serie de Fourier de r_q(v) centrada tiene coeficientes O(q/|h|) en los modos no nulos exp(2πi h v/q), por variación total en un período. Agrupar las frecuencias h/(qdm) como fracciones reducidas a/b con signo en a. Se tiene b≤qDV. Para d fijo y b dado, escribir m=j b/gcd(b,qd); entonces |h|=|a|j qd/gcd(b,qd)≥|a|j. Por la suma armónica, incluso truncando los modos, el módulo total para cada a/b es O_ε(X^ε/|a|), pues D,q son subpotenciales. La suma de cuadrados de esos coeficientes es O_ε(V X^ε). Dos frecuencias distintas distan al menos (qDV)^(−2).

Para una suma finita con separación Δ, su cuadrado integrado sobre un intervalo de longitud X está acotado por O(X+1/Δ) veces la suma de cuadrados: mayorar la indicatriz por un múltiplo de sinc²((x−3X/2)/M), con sinc(u)=sin(πu)/(πu) y M≥2 max(X,1/Δ); su transformada triangular suprime los pares distintos. Aplicar esta cota a las sumas de Fejér de las series de los residuos y pasar al límite por Fatou (los saltos forman un conjunto nulo). Por tanto

    X^(−1)∫ |E|² ≪_ε (1+V²/X)V X^ε ≪_ε X^(1+ε).

La compensación es entre frecuencias de residuos a lo largo de la escala x. El promedio de los extremos N es esencial en esta prueba: sin él queda el producto G(⌊x/V⌋)C_t(V), que el argumento no controla a escala de raíz.

**Por qué basta la media en x.** La parte positiva es 1-Lipschitz, y Cauchy–Schwarz permite sustituir la media de (−I)₊ por la de (C_t)₊ con error de raíz. Bajo RH el techo puntual de 317 basta. Si hubiera un cero exterior, elegir como en 292 un promedio suave no negativo en frecuencia que conserve un polo del cociente con un solo denominador de 317. Llamar A(x) al sumatorio promediado; el techo diádico integrado para (C_t)₊ implica X^(−1)∫ A₊≪_ε X^(1/2+ε). Por suma de bloques el Mellin de A₊ es holomorfo en Re s>1/2. El Mellin de A es regular en el eje real de ese semiplano y tiene el polo exterior. Por tanto el Mellin de la parte negativa A₋=A₊−A sería regular en todo ese eje real y tendría un polo no real allí a su derecha respecto a la recta crítica. Landau para A₋≥0 impide esto. Queda sin probar el techo de la parte negativa del bloque intermedio.

La gran criba para frecuencias separadas es clásica. Aquí se aplica a las fracciones de los residuos después de agrupar denominadores coincidentes y compensar los extremos; no se atribuye novedad al principio de separación en sí.
