# Auditoría lógica de `36-obstruction-ledger`

## Dictamen

El manuscrito no demuestra RH: su propia Step 5, ARP-P, queda abierta y es equivalente a RH. La auditoría **sí confirma**, con las salvedades de interfaz clásica indicadas abajo, la arquitectura formal

\[
 \mathrm{ARP\!\!\text{-}P}\Longleftrightarrow\mathrm{RH}.
\]

Esto es una equivalencia condicional útil: si se estableciera ARP-P, el puente de Pick--Nevanlinna elimina los polos no reales y da RH; bajo RH, los canales son transformadas de Cauchy de medidas positivas. No convierte la positividad aritmética en algo más débil que RH.

No queda confirmada la afirmación más amplia de que “todo salvo Step 5” esté demostrado en el sentido que sugieren el resumen, el mapa de estado y el epílogo. Hay lemas y teoremas auxiliares presentados como cerrados que son sólo bosquejos, consecuencias condicionales, cálculos finitos, propuestas, o usos de una realización construida fuera del manuscrito. Algunos fallos son de tipado lógico concreto, no sólo ausencia de detalle.

Convención de esta auditoría:

| Marca | Sentido |
|---|---|
| Confirmado | La conclusión sigue de las hipótesis expresas, con un insumo clásico identificado. |
| Condicional | Correcto sólo tras añadir una hipótesis que no se ha probado aquí. |
| Parcial | Cubre un régimen finito, separado, de altura grande, casi todo punto, o una clase delimitada; no la afirmación global. |
| No confirmado | Falta una demostración, se usa un resultado declarado bosquejo, la cuantificación no está formalizada o hay una incompatibilidad de tipos. |

En particular, “cerrado en el manuscrito” no equivale a “confirmado por esta auditoría”.

## Alcance y estratificación correcta

Hay cuatro niveles que no deben intercambiarse.

1. **Cadena Step 1--15.** Construcciones y equivalencias lógicas sobre la función objetivo ya definida mediante los ceros.
2. **H0--H8.** Descomposición exploratoria de Step 5. Sus subcasos no son Steps y no prueban ARP-P salvo que cubran todos los cuantificadores.
3. **Cadena \(\Omega\).** Reexpresiones de la dificultad terminal. Varias equivalencias se obtienen pasando por RH; no son una deducción aritmética directa.
4. **Torre/realización, muestreo, cascada y rutas de cierre.** Certificados candidatos o análisis auxiliares. No deben promocionarse a prueba de Step 5.

La primera premisa no derivada de la cadena central es exactamente ARP-P. La primera premisa no derivada de la narración operatorial es aún anterior: la existencia de los operadores auto-adjuntos \(A_P^\circ\), su compatibilidad con los datos aritméticos y la convergencia de sus compresiones. El texto admite expresamente que esa construcción se hizo “elsewhere” y no se demuestra aquí (`main.tex:7675-7686`).

## Step 1--15: estado auditado

| Steps | Estado auditado | Razón y primer punto no derivado |
|---|---|---|
| 1 | Confirmado | El cambio \(s=\tfrac12+iz\), las simetrías de \(\Xi\) y la traducción de RH a realidad de ceros son correctos (`2067-2131`). |
| 2--3 | Confirmado | Para el core declarado, el decaimiento horizontal y \(N(T)=O(T\log T)\) dan convergencia normal de la serie de canales y los residuos indicados (`2133-2261`). Es una definición por el lado de ceros, no una realización aritmética. |
| 4 | Confirmado como interfaz clásica | La admisibilidad del test se verifica y el paso usa la fórmula explícita en una clase de pruebas holomorfa en tira (`2262-2399`). El primer insumo externo es precisamente esa versión de la fórmula explícita; no es una prueba nueva de una identidad de torre. |
| 5 | Abierto, correctamente rotulado | ARP-P cuantifica sobre **todo** plano fuente finito y **todo** conjunto finito de nodos (`2400-2453`). Éste es el primer input no demostrado de la cadena. |
| 6--7 | Confirmado, condicional en la torre | La identidad de Cauchy para medidas positivas y el cierre del cono PSD son correctos. Step 7 sólo dice `tower-ARP => ARP-P`; no construye tower-ARP (`8032-8164`). |
| 8 | Confirmado con el teorema matricial NP | La reducción por Cayley y el tratamiento semidefinido son adecuados si se acepta el NP matricial clásico citado (`8165-8303`). |
| 9--11 | Confirmado como consecuencia de ARP-P | El pinning evita que una sucesión de interpolantes escape por la transformación de Cayley; identidad analítica y detección de residuos dan la remoción de polos (`8188-8428`). Es una consecuencia condicional, no una prueba independiente de normalidad de la torre. |
| 12--13 | Confirmado | Las simetrías trasladan la ausencia de polos de \(\Omega_-\) al semiplano opuesto y la traducción final es Step 1 (`8429-8464`). |
| 14 | Confirmado | Bajo RH, la medida de cada canal es finita y positiva, por lo que su transformada de Cauchy tiene kernel Pick positivo (`8465-8499`). |
| 15 | Confirmado como ensamblaje | Une las dos implicaciones anteriores (`8500-8538`). |

Por tanto, la frase prudente y exacta sería: **la equivalencia estructural ARP-P--RH está cerrada, mientras que ARP-P no lo está**. Steps 9 y 11 no son “cerrados sin condición”; son teoremas condicionales correctamente formulados así en parte del texto, pero el cómputo “catorce cerrados” debe conservar esa calificación.

## La realización y la normalidad: qué está y qué no está disponible

La capa `7676-8031` contiene resultados válidos **si** se conceden auto-adjuntez, cota uniforme de fuentes y convergencia de torre. En particular:

- la cota de masa de los vectores fuente se deduce de la suma absolutamente convergente una vez que la forma de celdas y el shorting existen (`7785-7915`);
- la compacidad de medidas espectrales y el puente de Cauchy son correctos bajo esas hipótesis (`7922-8029`);
- tower-ARP es una condición de convergencia, no una consecuencia demostrada de \(\Lambda\ge0\) (`8129-8164`).

Pero el párrafo inicial de la sección presupone la construcción de \(A_P^\circ\), la forma canónica de von Mangoldt y la compatibilidad de las fuentes, y remite todo ello fuera del texto (`7675-7686`). La afirmación “\(\Lambda\ge0\) hace los \(A_P\) auto-adjuntos” no sustituye una construcción con la identidad límite

\[
 (\Phi_P^F)^*(A_P^\circ-z)^{-1}\Phi_P^F\longrightarrow G_\Xi^F.
\]

Ese límite es tower-ARP y, por la propia cadena, implicaría RH. La auditoría confirma los teoremas de la forma “si existe tal torre, entonces…”, pero no confirma que el programa ya disponga de la torre. Tampoco confirma “sólo hay una dirección divergente”: `rank-one pole isolation` demuestra sumabilidad de masas de fuentes, no una cota operatorial global de todo complemento primitivo (`7715-7771`).

## H0--H8: reconstrucción y primer corte de cada subcadena

| Nivel | Lo que realmente queda | Estado auditado / primer corte |
|---|---|---|
| H0 | Conservación de dificultad. | Confirmado, pero es modus ponens; no localiza por sí solo una brecha matemática (`2941-2950`). |
| H1 | Positividad Pick escalar de un nodo para \(M_\Xi\) en \(\Re s>1\). | Confirmado con la factorización de Hadamard simétrica. No es ARP-P de un nodo matricial: los pesos de canales tienen fase, como el propio texto reconoce (`2951-2985`). |
| H2 | Criterio suficiente de Gershgorin para nodos separados dentro de una banda fija. | Parcial y confirmado como criterio. No cubre configuraciones separadas arbitrarias ni nodos que se acumulan (`2986-3023`). |
| H3 | Desigualdad infinitesimal de dos nodos en una región logarítmica y casi en todo punto. | Parcial. PDH es una hipótesis abierta, no una clausura global (`3024-3316`). La etiqueta “closed” sólo es correcta con las regiones y cuantificadores escritos. |
| H4 | Serialización por determinantes a lo largo de una sucesión acumulante. | Confirmado como equivalencia con RH, mediante `prefix-extension` (`3657-3696`). Es una serialización, no una cota de determinantes ni un método que evite RH. |
| H5 | Positividad de ventanas \(\Longleftrightarrow\) ARP-P. | Confirmado en la clase de ventanas indicada, si se aceptan los intercambios dominados demostrados con el crecimiento de \(\psi^F\) (`3347-3374`). No descarga ninguna cuantificación de Step 5. |
| H6 | Testigo negativo finito si RH falla. | Sólo la versión cualitativa está confirmada, pues es el contrarrecíproco de ARP-P \(\Rightarrow\) RH. La versión “cuantitativa cerrada” falla como se explica abajo. |
| H7 | SOS Andreief/Vandermonde y positividad de dos nodos. | El SOS queda como programa. La clausura de banda sólo trata \(N=2\), banda compacta y altura común suficientemente grande (`4039-4054`, `4605-4667`). No justifica “todos los regímenes”. |
| H8 | Patrones de \(N\) fijo, jets y cierre de banda; después el defecto terminal. | Confirmado para \(N\) fijo, banda separada del borde y traslación común de altura suficientemente grande (`3809-4054`, `4605-4682`). El primer punto no cubierto es la uniformidad en \(N\) para una sucesión acumulante a altura fija: exactamente la condición terminal. |

### H6: incompatibilidad concreta de normalización y falta de negatividad

La Proposición `H6 quantitative reduction` tiene como término local

\[
-\eta |\kappa|\,|r(w_0)|\,|r(\overline w_0)|,
\]

porque el texto declara que **no** normaliza el canal (`3406-3464`). Sin embargo, el Teorema `H6 quantitative single-cluster witness` reemplaza ese término por

\[
-2|r(w_0)|\,|r(\overline w_0)|
\]

sin el factor \(|\kappa|\) (`3530-3555`). No se ha impuesto \(|\kappa|=1\), y la fuente puede reescalarse. La conclusión tiene, por tanto, una incompatibilidad de tipos/normalización.

Además, aun conservando \(|\kappa|\), las pruebas sólo producen

\[
 \lambda_{\min}P\leq
 \frac{-2|\kappa|,|r(w_0)|,|r(\overline w_0)|+
 B_{\rm far}\|r\|_{\rm far}^2}{\|c\|^2}.
\]

No se demuestra que el numerador sea negativo para cada configuración. El control de fase hace negativo el bloque local, pero no domina la cola. Por tanto se ha demostrado una **reducción a un testigo efectivo**: para datos locales, polos y una cota de cola dados se puede calcular un límite superior de Rayleigh. No se ha demostrado un **testigo negativo**: que ese límite sea menor que cero para cada cúmulo no real. Éste es el primer punto no justificado de H6 y basta para impedir el estado “cuantitativamente cerrado”.

### H2: el añadido de alturas acotadas es inválido

El enunciado formal de H2 agrega que “para alturas acotadas el Pick matrix es PSD por compactidad y la positividad estricta de \(\Re(\xi'/\xi)\)” (`2994-2998`). La prueba que sigue sólo trata alturas grandes y el criterio de suma de filas. La inferencia adicional es inválida: diagonales estrictamente positivas no implican que una matriz hermítica sea PSD, y compactidad sólo permitiría extraer mínimos continuos de autovalores; no prueba que esos mínimos sean no negativos. Habría que demostrar todos los menores principales, una dominación diagonal, o la positividad misma en el compacto. Ninguna de esas piezas aparece.

Por tanto H2 queda confirmado únicamente como criterio de Gershgorin de altura grande bajo la condición explícita de suma de filas. La frase de alturas acotadas debe suprimirse o pasar a ser una hipótesis por verificar; no puede usarse para ensanchar el régimen de H2.

### Jets, cierre de banda y el salto a \(N\to\infty\)

La identidad de Hadamard emparejada y la serialización por jets escalares son piezas fuertes y, en lo esencial, confirmadas (`4175-4347`). En especial, la positividad de todos los jets en **un** punto regular equivale a RH: la continuación por NP se aplica a una vecindad y detecta todo polo. Esto hace que el defecto escalar sea una reformulación legítima, pero no más fácil.

El Teorema de cierre de banda (`4605-4667`) usa compactidad tras un cambio de base Newton. Prueba positividad para \(N\) fijo y nodos de la forma

\[
z_j=t+a_j-iy_j,qquad |a_j|\le A,quad y_j\in[\tfrac12+\epsilon_0,Y],
\]

cuando \(|t|\) es suficientemente grande **dependiendo de \(N\)**. No prueba positividad en una caja fija para cualquier altura ni proporciona control de \(T^*(N)\) al tender \(N\) a infinito. Las frases “para todas las configuraciones” deben leerse con esos tres parámetros fijos; sin ellos son más fuertes que el teorema.

## Defecto terminal, muestreo y saturación

Aquí se concentran varias contradicciones de estado.

1. Hay dos objetos llamados \(\delta_N\). La Definición `terminal-defect-fixed` usa
   \(\min c^*J_Nc/(c^*G_Nc)\) y está definida para todo \(N\) porque \(G_N\succ0\) (`4880-4927`). La Definición `terminal-defect` usa \(1-\lambda_{\max}(T_N)\), con whitening por \(J_N^\infty\), y sólo existe mientras \(J_N^\infty\succ0\), esto es, hasta \(N_*(t_0)\) (`5109-5120`). No son intercambiables fuera de ese intervalo. En particular, una afirmación límite \(N\to\infty\) escrita para \(T_N\) a \(t_0\) fijo no está tipada.

2. `whitened-terminal` es una congruencia correcta bajo la hipótesis explícita \(J_N^\infty\succ0\) (`4826-4861`). `pole-pair` niega precisamente esa positividad para todo \(N\) (`4862-4879`). Por ello \(\Omega_4\) no puede figurar como equivalencia cerrada de “todo \(N\)” con \(\mathcal W_A^{-1/2}\mathcal T_\Lambda\mathcal W_A^{-1/2}\). La forma reference-whitened sí serializa el signo; el operador whitened por la parte arquimediana no lo hace globalmente.

3. `signed archimedean decomposition` está etiquetado **Proof sketch** (`5121-5176`). Sus cotas uniformes son usadas por los teoremas de muestreo. Por tanto, `leading sampling form` y, sobre todo, el `audited weighted sampling form` no son resultados completamente demostrados en el texto. El segundo además invoca concentración de minimizadores y una cota factorial que aún no está establecida (`5227-5267`).

4. `conditional saturation` afirma \(\limsup_N\lambda_{\max}(T_N)=1\) pero el objeto de la izquierda no está definido para todos los \(N\). Su prueba dice que la cola puede hacerse arbitrariamente pequeña y cita una reducción condicional y un teorema anunciado “closed modulo” contabilidad pendiente (`5268-5313`, `5495-5536`). La aproximación por interpolación de un número creciente de átomos no basta, por sí sola, para hacer pequeño el cociente de cola. El primer punto faltante es la estimación uniforme de esa cola.

5. `two-sided factorial saturation bounds` contiene un **Proof sketch**, declara que la cota superior está “closed modulo” trabajo pendiente y reconoce que el paso Turán--Remez para \(c_1(y)\) es un punto de auditoría (`5519-5546`). No puede ser usado como teorema cerrado para probar saturación, `no fixed margin`, la cascada ni una tasa de detección.

6. `root recovery` y `terminal wall as Weil positivity` también están dados como bosquejos (`5555-5615`). Este último cambia además a \(\mathsf d_N\), símbolo no definido de forma compatible con los dos \(\delta_N\), y su densidad/completitud no se demuestra. No es una nueva prueba de Weil ni una clausura de Step 5.

La conclusión auditada es: la equivalencia de signo reference-whitened con RH es válida como serialización a través del teorema escalar de jets; las leyes de tamaño, saturación factorial, falta de margen y recuperación de raíces son evidencia o reducciones condicionales, no insumos cerrados.

## Cadena \(\Omega_1\)--\(\Omega_7\)

| Enlace | Estado que declara el texto | Estado auditado |
|---|---|---|
| \(\Omega_1\) | RH \(\Leftrightarrow\) ceros de \(\Xi\) reales. | Confirmado. |
| \(\Omega_2\) | Ceros reales \(\Leftrightarrow\) ARP-P. | Confirmado como la equivalencia Step 1--15. No es un mecanismo aritmético para probar ARP-P. |
| \(\Omega_3\) | ARP-P \(\Leftrightarrow\) \(\delta_N\ge0\) para todo \(N\). | Confirmado sólo como equivalencia lógica que pasa por RH: jets escalares \(\Leftrightarrow\) RH y ARP-P \(\Leftrightarrow\) RH. No hay una derivación directa de todos los canales desde un jet escalar. |
| \(\Omega_4\) | Defecto \(\Leftrightarrow\) dominación whitening. | No confirmado para todo \(N\): confunde la forma reference-whitened, válida globalmente, con el whitening de \(J_N^\infty\), válido sólo hasta \(N_*\). |
| \(\Omega_5\) | Límite regular al borde. | Confirmada sólo la **continuidad** para cada \(N\) fijo (`5974-6004`). No se prueba positividad interior incondicional ni positividad de su límite; el paso “si hay positividad interior, entonces el límite es PSD” es condicional. Tampoco intercambia \(y\downarrow\tfrac12\) con \(N\to\infty\). |
| \(\Omega_6\) | Positividad de borde \(\Leftrightarrow\) Li--Keiper. | Confirmado sólo como equivalencia de familias completas, mediante que ambas equivalen a RH (`6005-6091`). El propio texto acierta al negar una transformación positiva nivel a nivel. |
| \(\Omega_7\) | \(\lambda_n\ge0\) para todo \(n\). | Abierto y equivalente a RH por Li. Éste sigue siendo el residuo correcto. No equivale a \(|\lambda_n^{\rm prime}|<\lambda_n^{\rm arch}\) para todo \(n\): esa reformulación ya falla en \(n=1\). |

La tabla de estado de `6130-6165` presenta \(\Omega_4\) como cerrado mientras limita simultáneamente el whitening \(J_N^\infty\) a \(N\le N_*\). Son afirmaciones incompatibles salvo que \(\Omega_4\) se reescriba exclusivamente en coordenadas reference-whitened, sin operador \(\mathcal W_A^{-1/2}\) global. También sobredeclara \(\Omega_5\): su lema prueba continuidad, no una positividad no condicional. Esto no derriba \(\Omega_3\) ni \(\Omega_6\), que son equivalencias completas obtenidas vía RH; sí impide leer \(\Omega_4\to\Omega_5\to\Omega_6\) como una cadena demostrada que transporte positividad interior hasta Li.

### Diccionario Li: qué se confirma y qué no

La identidad de Cayley

\[
w_{-i/2}(z_\rho)=1-\rho^{-1}
\]

es correcta. También es correcto que la positividad de todos los jets en la base de Li y la positividad de todos los coeficientes de Li son equivalentes porque ambas caracterizan RH. No es correcto presentarlo como una transformación finita de un criterio en el otro; el texto lo reconoce en `6060-6091`.

La reformulación de \(\Omega_7\) mediante valor absoluto en `6255-6258` no es equivalente a Li y tiene un contraejemplo interno inmediato. Con la descomposición declarada

\[
\log\xi(s)=\left[\log s-\frac{s}{2}\log\pi+\log\Gamma\!\left(\frac{s}{2}\right)\right]
+\log\bigl((s-1)\zeta(s)\bigr),
\]

la definición diferencial de Li da, para \(n=1\),

\[
\lambda_1^{\rm arch}
=1-\frac{\gamma}{2}-\log 2-\frac12\log\pi
\approx-0.55412,
\qquad
\lambda_1^{\rm prime}=\gamma\approx0.57722,
\]

pues \(\psi(1/2)=-\gamma-2\log2\) y \((s-1)\zeta(s)=1+\gamma(s-1)+O((s-1)^2)\). Por tanto

\[
\lambda_1=\lambda_1^{\rm arch}+\lambda_1^{\rm prime}
\approx0.02310>0,
\]

mientras que \(|\lambda_1^{\rm prime}|<\lambda_1^{\rm arch}\) es imposible porque su lado derecho es negativo. En general, la identidad exacta implica

\[
\lambda_n\ge0
\quad\Longleftrightarrow\quad
\lambda_n^{\rm prime}\ge-\lambda_n^{\rm arch},
\]

una desigualdad unilateral y no una cota absoluta. Si \(\lambda_n^{\rm arch}>0\), la condición más fuerte \(|\lambda_n^{\rm prime}|\le\lambda_n^{\rm arch}\) basta para Li, pero no es necesaria ni equivalente; con signo estricto tampoco coincide con el criterio no estricto. En consecuencia, las formulaciones de `6122-6125`, `6255-6258`, `6298-6303` y `6333-6336` deben sustituir la supuesta equivalencia por la desigualdad unilateral, o presentar la envolvente absoluta sólo como estrategia suficiente después de verificar por separado los índices donde la parte arquimediana no sea positiva.

La identidad de integración por partes de `6399-6401` contiene además un error independiente. Con

\[
f_{n,\varepsilon}(y)=y^{-1-\varepsilon}L_{n-1}^{(1)}(\log y),
\qquad f_{n,\varepsilon}(1)=n,
\]

la representación regularizada anterior da

\[
\lambda_n^{\rm prime}
=-
\lim_{\varepsilon\downarrow0}
\int_{1^-}^{\infty}f_{n,\varepsilon}\,d(\psi-y).
\]

Integrar por partes y usar \(\psi(1)=0\) produce

\[
\lambda_n^{\rm prime}
=
\lim_{\varepsilon\downarrow0}
\left[-n+
\int_1^\infty(\psi(y)-y)f'_{n,\varepsilon}(y)\,dy\right]
=
\lim_{\varepsilon\downarrow0}
\int_1^\infty(\psi(y)-y+1)f'_{n,\varepsilon}(y)\,dy.
\]

El manuscrito escribe el negativo de la integral con \(\psi-y\), sin el término \(-n\). Por tanto invierte el signo y pierde el borde inferior. En \(n=1\) la fórmula impresa no puede devolver \(\lambda_1^{\rm prime}=\gamma\). Si \(A_n=\int|\psi-y|\,|f'_{n,0}|\), el lower bound correcto es \(\lambda_n^{\rm prime}\ge-n-A_n\), no el derivado en el texto. El no-go de magnitud conserva su déficit de orden porque el cálculo reporta \(A_n\asymp n^2\log n\), pero ninguna conclusión firmada puede heredarse de `6399-6401`.

La ruta posterior de “envolvente” tiene un problema más severo: define

\[
O(n)=\sum_\rho(1-1/\rho)^n.
\]

Bajo RH los sumandos tienen módulo uno y, tras emparejar, tienden a \(2\), no a cero. Esta suma no converge, ni absoluta ni simétricamente, para \(n\) fijo. La combinación convergente es la de Li, \(\sum_\rho[1-(1-1/\rho)^n]\), con la regularización apropiada; no \(O(n)\) aislado. En consecuencia, la integral oscilatoria posterior, `exact reduction of the envelope bound` y las tres rutas R1--R3 (`7110-7185`) no están bien definidas tal como se escriben. El primer paso no justificado no es la estimación por fase estacionaria: es la separación de una suma divergente.

Además, la equivalencia atribuida a Bombieri--Lagarias entre RH y la cota concreta
\(|\lambda_n^{\rm prime}|=O(\sqrt n\log n)\) no se demuestra en el manuscrito. La cota basta, junto con una verificación finita, para Li positivo; la vuelta requiere un resultado adicional de asintótica de Li y no se sigue de Li por la lógica mostrada. La fórmula escrita en `7079` omite además un término lineal: con el split del manuscrito,

\[
\lambda_n^{\rm arch}
=\frac n2\log\frac n{2\pi}
+\frac{\gamma-1}{2}n
+\frac34+O(n^{-1}).
\]

El término \(\frac{\gamma-1}{2}n\) no cabe en \(O(\sqrt n\log n)\). La cota \(c\sqrt n\log n\) para la parte prima debe enunciarse sólo para \(n\ge2\), porque su lado derecho se anula en \(n=1\). Hasta que se dé una referencia y una prueba exacta para la vuelta, debe rotularse como conjetura suficiente, no como “iff RH”. La representación Laguerre en \(\Re s_0>1\) es una identidad absolutamente convergente; su límite de borde mantiene una cancelación polo--primos y no es una suma prima absoluta (`6339-6375`).

## Las siete paredes, el paraguas de Weil y los no-go

El texto tiene un paraguas adicional, la positividad de Weil, y siete paredes numeradas por el cuantificador maestro. Conviene no contar el paraguas como una octava pared.

| Obstrucción | Clasificación declarada | Auditoría |
|---|---|---|
| Paraguas de Weil | \(E(C)\): positividad de Weil \(\Leftrightarrow\) RH. | Confirmado como criterio clásico, con la clase de tests correcta. |
| Propagación aritmética | \(I(\mathcal I;C)\) para cuatro familias de métodos. | El alcance formal es sólo esas familias. El Teorema `four-way` usa “todo mecanismo clásico” y “ninguna combinación” sin definir la clase ni aportar prueba completa (`655-693`); no confirma una imposibilidad general. |
| Signo equivocado | \(I\) para cotas inferiores/de magnitud. | Es una diagnosis válida de los paradigmas enumerados; no una prohibición de toda construcción operatorial. |
| Hasse--Minkowski infinito | \(I\) para factorización local-global. | Correcta como advertencia de que no hay principio automático. La inexistencia de toda factorización útil de la parte cero no se formaliza como teorema universal. |
| Reflexión por lugar | \(I\) para el kernel OS elegido. | La indefinición del kernel exhibido es directa; sólo cierra esa reconstrucción por lugar, no cualquier forma de positividad global. |
| Cohomología/Frobenius | \(F(X;C)+S(C)\). | Sólo condicional: una polarización con brecha y Frobenius del tipo correcto sería suficiente. Cálculos en una ventana no prueban que ningún objeto global exista. |
| Signo frente a magnitud | \(I\) para funcionales que ven sólo \(|\Lambda|\). | El principio lógico es razonable dentro de esa clase. El Teorema `marginality` se enuncia sin prueba formal y presupone la realización positiva no construida en el texto (`891-920`). |
| Norma uniforme/rango uno | \(F(X;C)+E(C)\). | No confirmado como equivalencia interna: la dirección “RH implica norma primitiva uniformemente acotada” y la identidad con el kernel de Kreĭn--Langer no se prueban aquí; además dependen de objetos de la construcción externa (`1375-1443`). |

Los no-go computacionales (p-valores, ajustes de exponentes, tablas de DH, regresiones o LP) sólo prueban lo que se calculó a precisión y corte finitos. No son teoremas de imposibilidad. Las etiquetas `No-go`, `Wall` o `Theorem` no añaden cuantificadores ni sustituyen una prueba. Este punto afecta, entre otros, a `phantom transition`, los detectores DH, los márgenes de partición y los resultados llamados W4/W5.

W4 no formaliza una clase completa de “argumentos por recurrencia”, por lo que el enunciado “ninguna prueba puede proceder” excede las estimaciones de un esquema particular (`6481-6586`). W5 sí tiene un núcleo directo: una densidad \(L^1\) no puede dominar una función periódica no decadente en todas las resonancias. Pero `per-prime cutoff feasibility` no lleva demostración; viene después de una tabla numérica y afirma una constante uniforme \(c_p\le6/5\) (`6956-7026`). Es evidencia de factibilidad finita, no un lema cerrado hasta construir la densidad y demostrar la cota.

## Rutas contra \(\Omega_7\): estado y cortes

| Ruta | Resultado real | Primer punto no justificado |
|---|---|---|
| Transporte casi periódico | La comparación de escalas muestra un desbalance plausible entre recurrencia y detección. | `gauge transport` contiene “[modulo Lemma signed-arch]”, que es bosquejo; `geometric detection` importa una tasa sólo esbozada. `ceiling rigidity` no prueba que para un \(c\) fijo el supernivel ocurra exactamente en todo gauge que detecta un cero. Por ello W4 no es un no-go universal. |
| Trasplante Castelnuovo | `conditional closure` pretende que X1--X4 implican positividad. | El argumento toma \(c^*J_Nc<0\), produce \(\langle\alpha,\alpha\rangle<0\), pero X3 sólo habla de clases con \(\langle\alpha,\alpha\rangle>0\) (`6629-6656`). No puede invocarse X3 sobre \(\alpha\); la desigualdad de Hodge escrita no da la contradicción. M2 y M2-closure heredan este fallo. |
| Construcción térmica X3-G | Conjetura y plan de falsación. | \(e^D\), dominios, regularización, estado torcido, dualidad y la identidad varianza--Weil son hipotéticos (`6746-6955`). “Positividad del twist” no produce la identidad de momentos requerida. |
| Partición arquimediana | No-go \(L^1\) global por una prima; problemas finitos explorados. | Falta la prueba de factibilidad con constante uniforme y falta la equivalencia formal entre asignación global, símbolo de borde y \(\Omega_7\). |
| Envolvente Li/estacionaria | Una condición suficiente de tipo RH y una exploración numérica. | La suma \(O(n)\) aislada diverge; por tanto la reducción “sin pérdida” no está definida. El uso de datos hasta \(n=170\) no establece una envolvente. |
| Cotas puntuales de \(\psi-x\) y \(\Lambda\ge0\) término a término | Diagnóstico numérico de pérdida de fase. | Las tablas descartan las estimaciones absolutas ensayadas, no toda desigualdad de fase ni toda factorización. |

La “closure specification” y sus conjeturas son apropiadas como propuestas, pero no cuentan como una séptima demostración de una pared ni como evidencia deductiva de \(\Omega_7\).

## Cascada de de Bruijn--Newman

La cascada no está separada lógicamente del defecto terminal. Su Teorema \(\alpha5\),

\[
\lim_N t_N^*=\Lambda_{\rm dBN},
\]

usa \(\alpha4\), que a su vez usa L3 y L4. Los cortes son:

- \(\alpha3\) tiene explícitamente `Proof sketch` y no controla el vector minimizante, colisiones ni constantes uniformes (`7329-7347`). Aunque \(\alpha5\) no lo cita de forma directa, no puede llamarse teorema cerrado.
- L3 apela a “la parte superior de `two-sided`” y a un régimen no especificado; esa cota factorial no estaba demostrada (`7457-7496`).
- L4 vuelve a usar una comparación potencial y una cota de denominador sin demostrar uniformidad suficiente (`7497-7528`).
- \(\alpha4\) y \(\alpha5\) heredan esos huecos. La prueba de \(\alpha5\) afirma que el umbral factorial termina siendo menor que \(v^2\), precisamente la conclusión que depende de L3/L4.

La parte confirmada es que, si se conceden las estimaciones de detección y cola, la implicación hacia la caracterización de \(\Lambda_{\rm dBN}\) tiene la forma correcta. La validación numérica no reemplaza esas estimaciones. Por ello la cascada debe figurar como caracterización condicional/propuesta, no como resultado probado que pueda apoyar H8.

## Contradicciones internas de estatus

1. El resumen, el mapa y el epílogo dicen que hay una sola brecha; H6 cuantitativo, muestreo, saturación, cota factorial, cascada, factibilidad de partición y realización de torre muestran brechas adicionales si se los presenta como teoremas autónomos.
2. H7 aparece “partially closed”, pero el cuadro afirma “scalar level-two band positivity closed for all configurations”. El teorema sólo da \(N=2\), caja fija, banda interior y altura grande.
3. H8 se denomina “quantitatively closed” mientras el objeto que se usa en tablas, \(1-\lambda_{\max}(T_N)\), deja de estar definido después de \(N_*(t_0)\); el defecto reference-whitened es otro objeto.
4. \(\Omega_4\) se rotula cerrado globalmente y en la misma fila limita la coordenada principal a \(N\le N_*\).
5. `conditional saturation` y `no fixed margin` se enuncian como teorema/corolario, pero dependen de cotas declaradas bosquejo o “modulo” trabajo pendiente.
6. La sección de realización admite que el operador y su compatibilidad se construyeron fuera del texto, mientras el prólogo atribuye al hecho de que \(\Lambda\ge0\) la normalidad que haría funcionar la arquitectura. La implicación está condicionada; la construcción no está disponible en este manuscrito.
7. Las rutas W4, M2, X3-G y W5 mezclan teoremas, proposiciones numéricas, conjeturas y problemas dentro de párrafos que luego hablan de “unconditional by-products”. Esa etiqueta debe reservarse a lo que tiene demostración completa.

## Conclusión operativa

La parte defendible del manuscrito es una reducción formal y una equivalencia:

\[
\mathrm{ARP\!\!\text{-}P}\Longleftrightarrow\mathrm{RH}
\Longleftrightarrow
\bigl[J_N(z_0)\succeq0\ \forall N\bigr]
\Longleftrightarrow
\bigl[\lambda_n\ge0\ \forall n\bigr],
\]

donde las equivalencias de los extremos deben leerse como caracterizaciones completas, no como transformaciones finitas ni como pruebas aritméticas de la positividad. El punto abierto central permanece \(\Omega_7\).

Para que el texto pueda afirmar que las reducciones auxiliares están cerradas, habría que, como mínimo: corregir H6 y dominar su cola; separar definitivamente los dos defectos \(\delta_N\); limitar \(\Omega_4\) al rango donde su whitening existe; reemplazar los bosquejos de muestreo/saturación/cascada por pruebas sin dependencia circular; formalizar o rebajar W4/W5; reparar el signo en la clausura Castelnuovo; y trasladar la realización “elsewhere” a hipótesis explícita o a una prueba incluida. Mientras eso no ocurra, la auditoría confirma la equivalencia principal y el residuo Li, pero no confirma que el resto de la infraestructura cuantitativa esté cerrado.
