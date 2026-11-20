# POWER_INTERIOR_AUDIT_017 — Revisión de la tabla escalar, fila completa y cono cuadrático

Estado: PROVED los resultados específicos revisados abajo; signo de TODA la tabla escalar todavía OPEN. Papers intactos.

## 1. Corpus y novedad relativa

Se revisaron índice/grid/crucigrama y los antecedentes E0/E_gamma: Paper47 lem:wit-conc, prop:Egamma-exact y rem:critical; phase188/L2_BUILD_008_GROUND_STATE_AND_T0, L2_BUILD_009_ARITHMETIC_INPUT_FOR_T0 y N_BUILD_013_E_GAMMA_C_COLLAPSES. La cadena Tate de008/009 concentra en frecuencia0 y recupera ese mismo umbral C0+4; no aportaba holgura nueva. La filaN1 actual se desplaza a frecuencias crecientes al aumentar k, y el cono k~cN² tiene centro u sqrt(cN) y ancho finito. Su control uniforme de TODA la suma aritmética mediante desplazamiento de densidad, no de normas temporales separadas, cambia un punto esencial del argumento anterior.

Los instrumentos Bernstein tienen antecedentes locales concretos en phase114/114_d_180_BERNSTEIN_DIRECTED_ENDPOINT_GATE§1 y phase72/E72_259_RATIONAL_BERNSTEIN_LM8_CERTIFICATE. La elevación de grado y los coeficientes positivos no son nuevos. No se encontró en esos antecedentes el puente de densidades racionales hacia átomos monomiales con conservación explícita del polar. La novedad se acota a esa aplicación exacta, no a un principio general de polinomios positivos.

## 2. Puente escalar017: revisión FORMAL aprobada

POWER_SCALAR_BRIDGE_017 fue leído completo. Para P real de grado<M, S(x)=P(i sqrtx)P(-i sqrtx) es un polinomio real no negativo en x>=0, con todos los cruces ya incluidos. La fórmula R(q) respecto del peso común F1 tiene grado<=M-1 y se prolonga no negativa a[0,1]; si gradoP=M-1, el valor final es exactamente el cuadrado de su coeficiente principal, con los factores de u cancelados correctamente.

La expansión Bernstein de gradoD es EXACTA. El bound uniforme l(l-1)/(2D) del cociente de factoriales descendentes se prueba por condicionamiento sobre no repetición: las dos probabilidades difieren a lo sumo por la probabilidad de alguna colisión. D>=grado garantiza que esa condición tenga probabilidad positiva. Por tanto el umbral explícito D>C_R/epsilon sí produce coeficientes estrictamente positivos, incluidos los extremos.

Cada factor q^j(1-q)^(D-j)|F1|² es la densidad de un múltiplo positivo del átomo h_(D+1-j,j), cuyo índiceN siempre es>=1. La identidad racional en x se evalúa legítimamente en x=-1/4 porque u>1 y no hay polo allí. Multiplicar por2 produce EXACTAMENTE la igualdad de polares, aunque q sea negativo en ese punto. Las sumas de contactos de cada función son absolutamente convergentes y la identidad es finita; no se intercambia un límite deD con una serie sin majorante.

Así W[f]+epsilon W[f1] es una suma de valores atómicos con coeficientes positivos. Si TODOS los átomos tienen signo no negativo, epsilon->0 implica W[f]>=0. No hace falta uniformidad de las normas de los átomos ni aproximación fuerte de las funciones. El argumento también extrae un átomo negativo finito de cualquier dirección negativa hipotética como declara el memo.

Conclusión: a diferencia de una mera lista de diagonales positivas, esta familia especial de TODOS los pares(N,k) sí controla matrices completas mediante una representación cónica de DENSIDADES que retiene sus cruces. No se afirma eso de una sola fila, un cono parcial o una unión de vectores. La obstrucción de momentos016 permanece correcta porque allí se aproximaban funciones, no estas combinaciones de autocorrelaciones. Los antecedentes114/72 fueron agregados explícitamente al memo principal.

## 3. Toda la filaN1: certificado revisado y reproducido

POWER_INTERIOR_017§§1–6 y tools/power_interior_017_verify.py: APROBADOS; script ejecutado con PASS. La generadora de normas ponderadas es la integral geométrica exacta1/[2sqrt((1-z)(a²-b²z))]. Sus coeficientes y la desigualdad c_(k-j)c_j<=c_k por Vandermonde producen el cociente(u-eta)/(u-2eta), uniforme en TODO k. Con eta15 su máximo para u>=31.5 es11.

La monotonía arquimediana por covariance reponderada y la cota psi16-logpi>3/2 son correctas. El polar exacto tiene factor alternado y su peor magnitud normalizada está acotada por63/496 usando c_k>=2^-k. El peine COMPLETO se controla por2sqrt11<7, Lambda<=q y suma q^-14; el coste105/(13*2^14)<1/2000 conserva todos los contactos. La resta final es42547/31000>4/3.

Queda demostrado W[h_(1,k)]>(4/3)||h_(1,k)||² para TODOS k>=0,u>=31.5. Es una fila infinita genuina; no prueba las filas N>=2.

## 4. WRN adicional: constante efectiva por fila, sin umbral en k

INTERIOR017§7 también está APROBADO. Expandir(tau²+b²)^k y aplicar beta da los factores y potenciasa^(1-2N) declarados. El cociente de coeficientes beta se factoriza exactamente como[c_(k-l)c_l/c_k]B_l^(N), con B_l^(N)=prod_(r0..N-2)(2l+2r+1)/(2r+1). Vandermonde elimina sólo el corchete y deja una serie positiva convergente para rho<1.

El operador prod(2rho d/drho+2r+1)/(2r+1) sobre(1-rho)^-1 reproduce esa serie exactamente; por tanto S_N es racional y calculable mediante finitas operaciones. Para N1 recupera la cota anterior. WRN controla el peine completo uniformemente en k para cada N, pero su dependencia creciente en N no es una prueba del signo de todas las filas ni contradice los lowerbounds de pesos de016.

## 5. Cono cuadrático: auditoría de STRIP y de su constante

POWER_QUADRATIC_017 fue leído íntegramente. La identidad de módulo tras y=sqrt(x²+1) es exacta: el denominador tiene cuadrado(u²+y²)^2-4u². El jacobiano principal<=2 y M<=2k dan exp(kT²/100) con la constante correcta. Bajo la densidad real,T tiene beta(N-.5,k+.5).

La parteT<=4N/k cuesta exp(4/(25c)). En la otra parte, cambiar el peso por(1-T)^(-k/100) da la beta con a'=.99k+.5. La razón de normales se acota por exp(N²/k)(100/99)^N: el upperGamma sale de psi<=log, y el lowerGamma de Jensen de x^b, con b=N-.5>=1.5. Markov del momento enteroN da(50/99)^N. El producto(5000/9801)^N<1 y k>=cN² producen la constante declarada.

La cota inferior beta de la región pequeña se obtiene integrando T∈[N/(2k),N/k], con T^(N-1.5) creciente y(1-N/k)^k>=exp(-2N). El majorante de esa región es(4/u)A^N r^k(2k/N)^(N-.5)e^(2N). Para k/N>=4, log(2k/N)<k/N y18^N<3^k justifican la cota< (4/u)(9r)^k<1. Todas las desigualdades son válidas para N>=2,k>=max(cN²,4N).

La densidad racional es holomorfa en la franja sin polos y sus lados verticales desaparecen por O(|z|^-2N). El desplazamiento da CORR con C(c)e^(-|t|). Esto NO es una norma temporal ponderada uniforme deF; desplaza el producto analítico completo de la densidad y no contradice016.

## 6. Cono cuadrático: peine completo, polar y signo eventual

CORR domina toda la suma por2C(c)sum Lambda(q)q^-1.5<14C(c); el majorante converge y su constante es válida por comparación integral. La fórmula beta de Elog y los bounds psi(x)>=logx-1/x,psi(x)<=logx dan ARCH>=.5logN+log(u sqrt(c)/(2pi))-5. Se añadió al memo un apéndice con la demostración elemental del lower m>=log(|tau|/(2pi))-4, propuesta por el coordinador y revisada desde la variación total de x/(x²+t²). Así ese input no queda como cita sin probar.

La magnitud polar normalizada tiene el factor y la beta exactos del memo. El mismo lower beta de§5 y9/3968<1/400 dan POL<400^-k. Queda demostrada positividad eventual para P1 en TODO el cono k>=cN²,N>=N0(c), con un N0 explícitamente acotable. No se presupone signo favorable de contactos y no se han omitido sus colas.

## 7. Perfil gaussiano y paso a TODA la serie

La representación Gamma independiente X,Y es correcta. En el evento de cocientes dentro de[1/2,3/2], el resto cuadrático Taylor tiene esperanzaO(N^-1/2) después de multiplicar por la escala sqrtN. El lineal deX también esO(N^-1/2). El complemento tiene probabilidadO(N^-2) por cuartos momentos; Cauchy--Schwarz y E tau²=O(N) dan el mismo error. La función característica Gamma exacta produce la amplitud exp(-u²ct²/8), con errorO_T(N^-1/2). Su constante y el centro mu_N son correctos.

Para pasar la aproximación a la serie completa se usa CORR independiente de GAUSS y el majorante gaussiano sumable. Separar contactos finitos y dos colas uniformemente sumables justifica ALL aun cuando mu_N oscile. No se declara desaparecida la serie modulada.

La precisión más fuerte inicialmente mencionada para el símbolo no es necesaria. Se sustituyó por el bound ya demostrado en Paper47,lem:mbounds: |m-log(|tau|/(2pi))|<=1/|tau|+1/(2tau²). Como E tau^-2=O1/N, su esperanza esO(N^-1/2), suficiente para PROFILE. El signo y factor2 de la contribución aritmética en PROFILE coinciden con W=ARCH+POLAR+Comb.

## 8. Alcance final aprobado

La tabla escalar COMPLETA sería suficiente por el nuevo puente Bernstein. Se han probado su filaN1 y una región cuadrática eventual, no TODA la tabla. En particular ninguno de estos resultados certifica una ventana adicional del Paper47 más allá del rango ya declarado: para trasladarlos a todos los tests falta completar aquella condición suficiente. No se afirma una prueba de signo para todos los numeradores en el cono cuadrático ni una extensión deT a partir de estas familias particulares.

## 9. Extensión SEPARADA auditada: cono explícito desdeN2

POWER_QUADRATIC_EXPLICIT_017.md y tools/power_quadratic_explicit_017_verify.py fueron revisados por separado y el script se ejecutó con PASS. La bandaeta15<u/2 es admisible. La identidad de módulo tiene a400/441, y las dos estimaciones DIFERENTES del factor son correctas: exp(5kT²) para la parteT pequeña, y(1-T)^(-k/2) para la cola conservando la convexidad del logaritmo original. No se usa la primera cota demasiado débil exp(5kT) en la cola.

El umbral32N/k produce exp(64/125)<=125/61. La razón normalizadora beta es<=exp(N²/k)2^N y Markov del momentoN aporta(1/8)^N, dejando exp(1/10000)(1/4)^N<=625/9999. El jacobiano principal es<2 al dividir en|x|>=eta. En la región complementaria, el prefactor2eta/u, A441/341, r200/341 y la cota beta inferior de017 tienen sus factores correctos. Para t=k/N>=100, t/4-log(2t) es creciente y su valor inicial supera logA+2; por tanto el crecimiento restante es<exp(k/4). La desigualdad log(5/3)>1/2 y r<3/5 dejan una contribución<exp(-k/4)<1/100. Esto da integral desplazada normalizada<5 y CORR15 para todo t.

La cola infinita de contactos es<1/1000 usando Lambda<=q y suma q^-14. Para ARCH, k/N>=10000N implica sqrt(k/N)>100; pi<4 y e<3 dan u*100/8>3^5>exp5, así el lower global de017 produce ARCH>.99. El polar400^-k es<.001 en todo el dominio. La resta final>.988>.98 es correcta.

Queda aprobado W>(49/50)||f||² para TODOS N>=2,k>=10000N²,u31.5,P1. Es una región escalar explícita y no un teorema para todos los numeradores de cada bloque. Tampoco decide la parte restante de la tabla escalar ni, por sí sola, una nueva ventanaT del Paper47. Esta extensión no sustituye ni modifica las hipótesis del teorema principal de§§5–7.
