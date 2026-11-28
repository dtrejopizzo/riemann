# Revisión matemática de los papers 43 a 58

> **REGISTRO HISTÓRICO DE LA PRIMERA TANDA.** Sus pendientes y dictámenes globales no representan el estado vigente. La segunda auditoría resolvió numerosos puntos y demostró un fallo de caracteres en la prueba de53. Consultar [estado actualizado](../auditoria-profunda/ESTADO.md), [error53](../auditoria-profunda/ERROR-53-CARACTERES.md) y los certificados de46 enlazados desde README. Se conserva el texto inferior para trazabilidad; no debe citarse como conclusión final actual.


Papers 47 y 48 excluidos. Informe consolidado de dictámenes, uniones y conexiones matemáticas.


## Dictamen de la revisión matemática

Fecha: 28 de noviembre de 2026. Copia local del repositorio en el commit `97fb4e78d5a858baa926829a42336ae3b914e59a`; hashes individuales en `evidencia/fuentes.json`. Se excluyeron de la lectura los papers 47 y 48. Se trabajó sobre LaTeX y los registros indicados, no sobre una versión remota que pudiera cambiar durante la revisión.

**La revisión no certifica la demostración de GRH/RH de la serie. Tampoco produjo un contraejemplo confirmado a sus teoremas principales.** Hay argumentos concretos comprobados y pasos centrales que permanecen **(c), no verificados**, con sus localizadores y la comprobación necesaria para resolverlos. La mayor parte de esos pasos tiene una prueba escrita en el manuscrito: el límite es de esta auditoría, no una afirmación de que el autor haya omitido toda prueba.

Los dictámenes siguen el esquema solicitado:

- **(a) correcto como está escrito**, en el alcance que se especifica. Cuando se verifica una implicación a partir de lemas, se dice expresamente que no se certificaron todos sus antecedentes.
- **(b) incorrecto**, con primer fallo demostrado. No se obtuvo un (b) defendible para los teoremas principales. Se identifican separadamente precisiones de datos o formulación.
- **(c) no verificado**, indicando el paso exacto y lo que falta comprobar. No equivale a «falso», ni a «correcto por no haber encontrado un error».

### Resultados centrales

| Bloque | Resultado de esta revisión |
|---|---|
| 46, equivalencia entre positividad en todas las ventanas y RH | **(a)**. Se comprobaron fórmula explícita, dominio de forma y construcción del test primitivo negativo en 45. |
| 46, cotas hasta `(log 5)/2` | **(c)**. La reducción a inercia es comprobable; faltan certificados ejecutables y matrices para validar los números reportados. |
| 46, ventana `2.8022` | **(c)**. Z2 y la cota publicada Z3 se cotejaron; el filtro y las 17 verificaciones no se reproducen. Z1 no se certificó independientemente. |
| 43 | **(c)** global. Descomposición del grupo, símbolo radial y estabilización comprobados; cálculo completo de Hochschild, firma y completación no certificados. |
| 44 | **(a)** para los dos teoremas principales de composición/contacto examinados, con su rango; no aprobación automática de todos los resultados secundarios. |
| 45 | **(a)** para comparación con fórmula explícita, normalización radial y criterio primitivo. Esos resultados tienen antecedentes clásicos. |
| 50 | **(a)** para el teorema algebraico con sus hipótesis y sus inputs internos; **(c)** para certificar íntegramente su aplicación a todos los datos automórficos posteriores. |
| 49 | **(c)** para seesaw global, constante exacta en todos los conjugados y divisibilidad completa. Hay pasos parciales comprobados. |
| 51–52 | **(c)** para segundo momento, estimaciones locales y multiplicidades completos. Se verificaron varias constantes, reducciones y cierres de rango. |
| 53–54 | **(c)** para exchange, cadena automórfica, fórmula de un lift y test de valoración mínima completos. Álgebra de inyectividad y de compresión de determinantes comprobada. |
| 55 | **(c)** para existencia global de twists, Ribet/Selmer y clases impares completos. La irreducibilidad sí está explicitada; dualidad y suma de pérdidas se comprobaron en las reducciones indicadas. |
| 56 | **(c)** para los teoremas integrales completos. Se verificaron sustituciones y NM en la aplicación; NM no es condición necesaria para toda anulación, y el texto no formula tal equivalencia. |
| Uniones | Entradas centrales de la tabla de 46 cotejadas con grados de cobertura explícitos; **(c)** para certificar todas las importaciones transitivas y sus aplicaciones. |
| Novedad y conexiones | Identificados antecedentes y una conexión cuantitativa propuesta; no se certifica prioridad global ni nacimiento de un campo nuevo. |

### Observaciones que permiten mejorar el manuscrito

1. **Paper 46, línea 1766:** `omega_-` debe ser al menos `2A=5.88394705…` para el corte especificado. `5.8839` puede ser un resumen decimal, pero no una cota superior literal. El certificado debe conservar valores exactos o redondeos dirigidos. Las cotas de las dos colas son numéricamente consistentes; esto no certifica la inercia.
2. **Paper 51, línea 3961:** la absorción `f·2^(3−k)≤b^-10` necesita una relación entre k y `log b`, además de las cotas listadas localmente. La relación viene de los datos admisibles; conviene incluirla al aislar el lema. No se encontró una contradicción en la aplicación vigente.
3. **Paper 50:** su conclusión es de colongitud truncada, con término excepcional `θj`. Presentarla como una cota uniforme de todos los divisores elementales perdería una parte esencial del enunciado.
4. **Paper 56:** «para todo ℓ» no elimina las condiciones sobre pesos, ventanas y distribución de letras. NM es una condición suficiente del argumento genérico, no una caracterización necesaria de anulación. El reporte ofrece un ejemplo de rango positivo que distingue ambos conceptos.

También se descartaron objeciones que serían injustas con esta versión: la irreducibilidad residual de 55 sí está escrita; 51 sí trata la extensión de la comparación a lugares inertes y cierra el rango de corangos; la constante corregida `3x^35` de 54 sí llega a 46; y la diferencia entre los retículos de 49 y 51 sí tiene un transporte propuesto.

### Lectura de la conexión propuesta

La idea que merece aislarse es convertir divisibilidad de coeficientes theta en una cota unilateral sobre primos, comparando el tamaño de muchas formas con un límite inferior de su covolumen. El segundo momento garantiza el rango casi total; los períodos CM, los twists y los grupos de Selmer deben hacer compatibles las dos cuentas.

La serie reconoce que la ruta automórfica y su matemática se atribuyen a Levent Alpoge, mientras que la organización en tres teoremas y su presentación en esta serie son del autor de los manuscritos. Los nombres de especialistas proporcionados por el usuario se usaron para definir las tareas de los agentes; ninguno de esos investigadores participó ni avaló esta revisión.

Una línea de investigación describible sería **métodos de pendientes para retículos automorfos y divisibilidad theta**. Es una propuesta de programa, no una declaración de nueva disciplina. El capítulo de conexiones da resultados intermedios concretos que podrían validarse y desarrollarse sin depender de RH.

### Método y alcance material

Trabajaron el agente principal y tres agentes especializados: theta/Hecke/covolumen; segundo momento/traza y conexiones; Selmer/Hodge integral. Hubo relecturas cruzadas de los dictámenes positivos y de los ejemplos. La revisión no reproduce un arbitraje exhaustivo línea por línea de todos los manuscritos ni la construcción formal Lean completa.

El inventario contiene 14 fuentes, 1910 etiquetas compartidas y 3526 referencias internas explícitas con las claves reconocidas por el script. Esos números incluyen repeticiones y el volumen 58; **no son un número de teoremas verificados**. Las tablas de los capítulos explican exactamente qué fue cotejado. Las referencias que no se individualizan quedan (c).

No se ejecutaron los certificados de las ventanas finitas porque no se localizaron en los artefactos examinados. Los chequeos propios de constantes usan precisión múltiple sin intervalos y están identificados como consistencia, no como certificación. No se volvió a compilar el archivo Lean de gran escala. Los papers y el archivo sin seguimiento `06-alpoge-verification/README-mio.md` permanecieron intactos.

### Prioridades para cerrar la revisión

La certificación global exige resolver varios trabajos independientes, no sólo corregir los dos detalles editoriales: aportar las inercias reproducibles de 46; completar la auditoría de períodos y divisibilidad de 49; certificar los sistemas locales y el término principal uniforme de 51–52; comprobar exchange y test forms de 53–54; cerrar Selmer y clases impares de 55; y verificar los lemas integrales centrales de 56. Los capítulos señalan sus etiquetas precisas. Sólo después puede una comparación semántica completa de las uniones sustentar un dictamen sobre la cadena entera.


## Paper 46 Forma de Weil y certificados numéricos

Revisión de los tres puntos pedidos, sobre el `main.tex` local identificado en `evidencia/fuentes.json`. Los números de línea corresponden a ese archivo, no a páginas del PDF. **(a)** significa argumento comprobado en el alcance indicado; **(b)**, fallo localizado; **(c)**, paso no verificado. Una conclusión (c) no afirma que el enunciado sea falso.

| Punto | Dictamen | Motivo |
|---|---|---|
| Positividad de `W_T` para todo T equivalente a RH | **(a)** | Fórmula explícita, densidad en norma de forma y test primitivo negativo de paper 45. |
| Cotas `10^-18` y `2.5·10^-12` | **(c)** | Método de reducción justificable; faltan matrices y ejecución certificada que establezcan sus inercias. |
| Hechos Z1–Z3 | Z2 y la cota de Z3: **(a)**; certificación de Z1: **(c)** | Z2 se cotejó con fuente primaria; los coeficientes de Z3 coinciden con la formulación publicada. No se reprodujo la certificación del primer cero y su aislamiento. |
| Cota hasta `T=2.8022` y uso de Z1–Z3 en ella | **(c)** | El filtro y sus 17 verificaciones están reportados, no desarrollados ni reproducidos. |

### Equivalencia con RH

Las definiciones están en paper 46, líneas 248–316, y la demostración de `thm:all-support` en 5460–5505. Con la transformada `Fhat(τ)=∫F(t)e^{iτt}dt`, el símbolo es

`m(τ)=Re ψ(1/4+iτ/2)−log π`,

y cada potencia prima lleva `2Λ(n)/sqrt(n)` en el símbolo coseno. La fórmula explícita para una autocorrelación da

`W_T(F)=Σρ Φ_F(ρ) overline(Φ_F(1−barρ))`.

El término polar es `2Re(A overline B)`, no `|A|²+|B|²`. Bajo RH cada sumando es `|Φ_F(ρ)|²`. Para tests reales suaves la fórmula está en las líneas 260–271; la complejificación es válida porque la suma cruzada para dos tests reales es real al emparejar ceros conjugados.

La extensión a `D_T` no requiere suponer a priori convergencia de la suma para todo test rugoso: la densidad en norma ponderada de `lem:form-density` (457–487) y la positividad para diferencias hacen las transformadas una sucesión de Cauchy en `ell²`. La convergencia en `L²(-T,T)` identifica cada coordenada. El argumento de contracción del soporte seguido de mollificación demuestra la densidad; la continuidad de los momentos y el crecimiento logarítmico de `m` dan continuidad de la forma.

Para la recíproca revisé la prueba concreta de paper 45, `thm:sufficiency`, líneas 1403–1559. Un cero fuera de la recta produce una órbita de cuatro puntos `±z0,±bar z0`. Un polinomio anula los demás ceros de altura acotada y los puntos `±i/2`; una potencia convolutiva de un bump controla la cola. El ajuste con `α+βz0²`, posible porque `Im(z0²)≠0`, hace contribuir `−4m0` a la órbita. La cola es `O(4^-N)` con constantes independientes de N, pues `Σ m(z)/(1+|z|)²<∞`. Los tests construidos son reales, primitivos y compactamente soportados. Una ventana suficientemente grande contiene el soporte y tiene forma negativa. El soporte depende de N: no se afirma que una ventana prefijada detecte todos los ceros.

Esta equivalencia no demuestra que la forma sea positiva. Es compatible con que la prueba automórfica posterior quede sin verificar. El antecedente clásico es [Connes–Consani, apéndice C, con atribución a Yoshida](https://arxiv.org/html/2006.13771).

### Certificados en la ventana de log 5

El primer paso que no puedo certificar es paper 46, líneas **1616–1617**: las ball enclosures darían las cuatro cotas y el programa no se reproduce. El texto desarrolla la reducción, pero la tabla de pivotes (1772–1783) es el resultado que debe probarse, no un sustituto de la prueba computacional.

La proposición `prop:lowercert` (1695–1732) tiene una justificación funcional correcta: en el complemento de los primeros Legendre el operador es acotado inferiormente por `q_Y>0`; el complemento de Schur se domina por la matriz `R`; la inercia del borde con `c=0` resta exactamente una dirección negativa; con `c=−1/2` y `c=+1/2` se recuperan, respectivamente, los términos polares par e impar. Las estimaciones mediante la traza de la compresión del operador de limitación de banda también son suficientes como método.

Para completar la verificación numérica hacen falta:

1. Valores exactos o intervalos con redondeo dirigido para `T`, `s_infty`, nodos, pesos, entradas y cotas de colas.
2. Código de la cuadratura y demostración de la cota analítica del resto que efectivamente implementa.
3. Matrices certificadas o un generador reproducible de ellas, con los cuatro valores de μ.
4. Verificaciones de `q_Y>0`, invertibilidad del cambio de base, signo del bloque de borde y todos los pivotes del Schur complement, incluidas las contribuciones de las colas.

El notebook de paper 58 no contiene los parámetros identificadores de estos certificados: `193.13`, `640` o `120110026807`. Su README declara expresamente que contiene chequeos pequeños de consistencia, no prueba de los teoremas en su rango. No ejecuté esos chequeos como sustituto de las inercias ausentes.

El script `evidencia/comprobar_constantes_46.py` reproduce **con precisión múltiple, sin intervalos**, estas consistencias:

| Cantidad | Valor aproximado |
|---|---|
| `240T` | `193.132549492092…` |
| `A` | `2.94197352522362…` |
| `m(240)−A` | `0.700787608327198…` |
| `Lambda*_280` | `4.4046093678·10^-20` |
| `Lambda*_330` | `3.8625471440·10^-70` |

Las dos últimas son consistentes con las cotas impresas `4.5·10^-20` y `3.9·10^-70`; no certifican las matrices. Hay una corrección editorial necesaria en los datos de la línea 1766: si `omega_-` se emplea como cota superior definida en 1688, entonces `omega_-≥2A=5.88394705…`; **el decimal `5.8839` no es una cota superior válida**. Como resumen redondeado es admisible; como constante literal del certificado debe reemplazarse por una cota hacia arriba. No se infiere de esto que las cotas espectrales sean falsas. También `c_*=193.13` es sólo una presentación abreviada de `240T`, no su valor exacto.

### Ceros y ventana mayor

Z2 (1795–1796) usa una altura menor que la de [Platt–Trudgian, teorema 1](https://arxiv.org/pdf/2004.09765): `3·10^12 < 3 000 175 332 800`. Esta reducción de altura es correcta y no asume RH global.

Los coeficientes y rango de Z3 (1797–1798) se cotejaron con la formulación de Rosser que reproduce el artículo de [Faber–Kadiri](https://www.cs.uleth.ca/~kadiri/articles/New-Bounds-for-Psi-Math-Comp-Faber-Sept2013.pdf). Para `N(t)` definido con `γ≤t`, la versión no estricta de la desigualdad se obtiene también tomando límites derechos en las alturas de ceros. El paso `N(t)≤t log t/(2π)` para `t≥21` es correcto: la diferencia inferior impresa es positiva en 21 y creciente. La integración de Stieltjes de `lem:zerosum` conserva el término de borde con el signo correcto; descartarlo aumenta la cota.

Z1 (1790–1794) afirma simplicidad e inexistencia de otros ceros hasta 21, además de un intervalo para la primera ordenada. Es consistente con los valores clásicos, pero no he reconstruido desde los certificados originales el recuento y aislamiento: **(c)** para esa verificación independiente. Evaluar numéricamente `ζ(1/2+it)` no bastaría para descartar ceros omitidos fuera de la recta.

En `thm:margin` (1864–1890), Z1 elimina la primera pareja, Z2 convierte las contribuciones de altura intermedia en cuadrados y el recuento controla el resto por valor absoluto. Es un argumento de **cota superior** de la mínima forma, no una cota inferior. No hay una deducción válida de positividad por tender esa cota superior a cero, y el texto no la hace allí.

Para la cota **inferior** en 2.8022, el primer paso pendiente es **1915–1930**, `eq:power-window`: se anuncian un filtro compacto, 2048 filas continuas de Schur y 17 verificaciones; faltan sus fórmulas y ejecución. Z1–Z3 por sí solas no permiten comprobar el exponente `120110026807`. La sección declara que ninguna otra afirmación del paper depende de esta cota; su falta de certificación no refuta por sí misma la cadena automórfica.


## Revisión de 49, 50, 53 y 54: theta, Hecke y covolumen

Fecha: 2026-11-28. Fuente: `main.tex` de la copia local, no los papers 47–48. Las referencias de líneas son las del archivo fuente. No representa la opinión de los investigadores mencionados por el usuario.

### Alcance y dictamen

La revisión distingue la demostración de un resultado local de la verificación de todos sus antecedentes automórficos. **No certifico los papers 49, 53 y 54 completos ni la conclusión GRH.** He comprobado la estructura algebraica del paper 50 y varios pasos concretos de los otros tres. Para los enunciados cuyo desarrollo completo no he podido comprobar doy (c), y especifico qué parte queda pendiente; esto no significa que la prueba sea falsa ni que el manuscrito omita necesariamente esa parte.

| Pregunta | Dictamen | Alcance exacto |
|---|---|---|
| 50.1: `ph:thm` en `ph:eq-large` | (a) | Teorema algebraico bajo sus hipótesis impresas de §2.1; la deducción y sus desigualdades se verifican. Los inputs se comprueban en 50.2; esto no certifica las aplicaciones aritméticas de 50.3. |
| 50.2: `ph:root`, `ph:count`, `ph:av` | (a) | Los argumentos de §3 suministran estos inputs y las hipótesis numéricas de su aplicación interna se cumplen. |
| 50.3: rango utilizado después | (c) | Coinciden el enunciado citado y el resultado obtenido; verificadas las sustituciones numéricas, queda sin certificar toda la construcción aritmética de los datos y la aproximación débil de 49. |
| 49.1: seesaw independiente del twist | (c) | No verificada toda la transferencia de períodos, convergencia y descenso de tipos archimedianos. |
| 49.2: conjugados y constante exacta CS | (c) | Comprobada la aritmética de factores de área en (C4), condicionada a la fórmula clásica citada; no certificada toda la reciprocidad y normalización del vacío. |
| 49.3: divisibilidad en todos los primos | (c) | Identificado el tratamiento específico de inertes, ramificado y nivel; no verificados todos los argumentos de integralidad del kernel. |
| 53–54.1: exchange y constante absoluta | (c) | No comprobados todos los términos locales y archimedianos de `pcx:X`. |
| 53–54.2: inyectividad y factorización | (c) | La inyectividad abstracta del triángulo sí se comprueba; no todas las hipótesis automórficas que la aplican. |
| 53–54.3: Gram y valores L de un lift | (c) | Verificada la identidad de determinantes condicionada a `po:glue`; quedan sus antecedentes automórficos. |
| 53–54.4: forma test y valoración alcanzada | (c) | Verificada la deducción ultramétrica de `psm:attained` a partir de sus inputs; no todos los inputs ni la ortogonalidad a falsos lifts. |

No he identificado en esta revisión un contraejemplo que justifique (b). No convierto la falta de una auditoría completa en una acusación de ausencia de prueba.

### 50: comprobaciones matemáticas

Archivo: `04-papers/50-elementary-divisors-edge-hecke-operator/main.tex`.

#### El enunciado realmente demostrado

Líneas 335–409, `ph:thm`. El anillo es un dominio de valoración de característica cero, con (w^2=p), y el ciclo tiene (N\ge2) par, (P=p^e\ge5), (q=P^N). Se exige la condición de libertad de las aristas `ph:eq-free`. El resultado controla la colongitud **truncada** por (p^j\Lambda):

\[
\operatorname{col}(\Lambda,Y\Lambda+p^j\Lambda)\mid p^l,
\quad l\le (3c_d+\theta j)|X||H||\mathcal B|.
\]

La paráfrasis «media de divisores elementales pequeña» debe conservar la fracción excepcional (\theta) y la truncación. No es una cota uniforme independiente de (j) para todos los divisores elementales, ni asegura por sí misma que (Y) sea invertible. Esto es una precisión de interpretación, no un fallo del teorema impreso.

#### Álgebra de la deducción

* `ph:near`, líneas 449–481: la forma diagonal se puede obtener por operaciones finitas en un dominio de valoración; no se requiere un DVR. La independencia módulo el ideal maximal de las columnas de (Q) y de las columnas seleccionadas de (U) se prueba aplicando la inversa izquierda (R). El módulo al que se aplica Nakayama es finitamente generado, aun si el anillo no es noetheriano.
* `ph:fact`, líneas 543–552: la transposición y el orden son correctos. La relación (\mathsf b\rho({}^tg)={}^t\rho(g)\mathsf b), junto con la conmutación diagonal de (\Delta) y (\mathsf b), produce exactamente (A(1\otimes\mathsf b)).
* `ph:null`, líneas 554–576: el argumento de jets usa CRT y el conteo de los monomios reducidos. La condición sobre el número de puntos da independencia además de generación. Si se permite un conjunto (Z) infinito en el enunciado, basta tomar un subconjunto finito del tamaño requerido.
* `ph:depth`, líneas 578–629: las formas (z_v(y)^{P^j}) recuperan todas las coordenadas (y_{ac}). Los determinantes empleados no son cero porque sus términos son monomios distintos. La suma de pesos de los monomios da la cota (c_d|\mathcal B|).
* `ph:ends`, líneas 631–651: el paso de las valoraciones posiblemente no discretas a exponentes enteros es válido: se cuenta cuántos enteros (\delta\ge0) satisfacen (t_i\nmid w^\delta), es decir un redondeo hacia arriba. No se está suponiendo discreción de la valoración.

En líneas 706–749 se obtiene (A'={}^td'Zd). La congruencia del promedio da (\mathcal A\mathcal B\equiv p^{2Nc_0}\pmod{w^c}), no (p^{Nc_0}): el segundo factor procede de (\mathsf b\mathsf b'=p^{Nc_0}). El texto conserva ambos factores. Finalmente

\[
\det d'\det d\mid w^{\lambda+\lambda'}\mid p^{\max(\lambda,\lambda')},
\]

por (w^2=p), y esto produce el coeficiente final (3c_d). No falta un factor 2 en esa última conversión.

#### Los tres inputs

**Root** (`pe:root`, líneas 925–1025). La sustitución construye un polinomio (\bar\Phi) sobre (R/w^{\lambda+1}R) de grado (q\nu'), con coeficiente principal no nulo. Para cada representante de (\mathbb F_q) lo divide una potencia ((t-a_r)^\nu). Las diferencias (a_r-a_{r'}) son unidades; por tanto estos factores son comaximales y su producto mónico divide (\bar\Phi). El argumento de grados sigue siendo válido aunque el anillo cociente tenga divisores de cero, precisamente porque el divisor es mónico. Se concluye (\nu\le\nu'). No hace falta introducir una hipótesis de cuerpo en este paso.

**Count** (`pe:count`, líneas 1230–1251). El punto delicado es el volumen de `pe:vol`, líneas 1120–1171, que usa intercalación, el jacobiano (P^{kN}\Delta(\sigma)), y el producto de Euler. El factor obtenido es

\[
\prod_{l=1}^k\frac{q-1}{q^l-1}=[G:I]^{-1}.
\]

La construcción de empaquetado en `pe:flag` transforma el conteo de monomios de grado fijo en un volumen de dimensión (kN), usando un espesor de tamaño uno; no se está comparando directamente un conjunto de volumen cero con su número de puntos. La hipótesis (24Nk^2cP^{2r}\le\theta n) implica (x\le\theta/2\le1/2), de donde (e^x\le1+2x\le1+\theta).

**Averaging** (`pe:avg` y `pe:av`, líneas 1259–1328 y 1430–1500). El promedio se construye algebraicamente mediante trazas, no dividiendo por el orden de un grupo finito que pudiera ser no unidad. En (S1), el límite (d+k\le q) es suficiente: una forma homogénea de grado entre 2 y (q) no desaparece al reducir módulo (X_v^q-X_v); los monomios de grado (q) que se reducen a grado 1 no cancelan con términos de grado 1 de la misma forma homogénea. El submódulo (U^+) es finitamente generado porque el álgebra (\mathcal S_d) es imagen de un módulo finito libre y hay finitos vectores iniciales. Así, su uso como módulo libre en la traza es lícito sobre un dominio de valoración. Las estimaciones de pesos en `pe:wd` conservan el error (2c), suficiente para el umbral (c^*=3kc).

#### Rango interno y aplicación a 49

Líneas 1505–1517 verifican explícitamente, desde `ph:eq-large`, las condiciones de `count`, `av` y `near`. En particular

\[
P^{N/2}=\sqrt q\ge n^2>Nk(N/2+2)n+n+k,
\quad 24Nk^2(5Nc_0)P^{2r}\le\theta n.
\]

La aplicación de líneas 1519–1531 usa (n=a=xb), (r=\lceil\log_pm\rceil), (P=p^{o_0}), (N=o/o_0), (\theta=(m^2f)^{-1}). Sus dos verificaciones son (q\ge a^4) y ((Nk\log q/\theta)^5P^{3r}\le b\le a). La conclusión (3c_d\le12A_{\mathfrak l}/(mp)) tiene el factor correcto porque (A_{\mathfrak l}=aN/2).

La parte aritmética de líneas 767–831 usa, además, aproximación débil, libertad de (J), la identificación de todos los factores de la representación y la paridad de los lugares del ciclo. He leído esa reducción y no encontrado una contradicción; no he certificado aquí los antecedentes de 49 que proporcionan estos datos. Por eso la pregunta sobre **todas** las aplicaciones posteriores conserva (c).

### 49: ubicación precisa de lo pendiente

Archivo: `04-papers/49-short-forms-theorem-theta-lifts-complex-multiplication/main.tex`.

**Seesaw.** El resultado de 46 `au:seesaw` permite que el dato de cadena (\Psi) dependa del twist, pero no (c_{\rm ss}). Tampoco afirma no nulidad de los dos lados. En 49, `ps:onestep` (3983 ss.) reduce la transferencia a una única órbita; las etapas (3), (5), (6) se remiten expresamente a `pk:vanish`, `pk:coarse`, `pk:fine`. No sería legítimo señalar esas remisiones como huecos sin comprobar sus destinos. Falta en esta revisión verificar esos destinos, la convergencia absoluta al intercambiar integrales y sumas y el ensamblaje que mantiene el escalar independiente del twist.

**Constante CS.** En `ps:conj` (3845), la exigencia es exactamente (|t_\sigma|^2=\Omega^{-1}). `pk:conj` (5433) usa (t_\sigma=\sigma(\varpi_{\rm vac}/\mathsf u)c_\psi/\Omega_\sigma). La prueba de (C4), líneas 5304–5340, no se limita a citar una igualdad «hasta un algebraico»: construye (\mathsf u^{12h}=\prod_i\mu_i^{12}\Delta(\Lambda_i)) y afirma la identidad exacta de áreas. Comprobé la combinación de factores mostrada: de (\operatorname{area}|\Delta|^{1/6}=4\pi^2\operatorname{Im}\tau|\eta|^4) y del promedio (c_{CS}-\log(2\sqrt d)) resulta (2\pi^2e^{c_{CS}}/\sqrt d), como está escrito. No comprobé contra el texto íntegro de Chowla–Selberg la fórmula de partida, ni todos los transportes de diferenciales, la unidad en 2 (`pf:CS`, 6911), y la reciprocidad `pf:recip` (7111). Por ello no certifico la constante exacta final.

**Divisibilidad.** `pa:count` (2522) distingue expresamente el primo ramificado (p=d), con deducción adicional (\frac12\sum_\tau\mathrm{ded}_0(\tau)), y limita los jets a las columnas anidadas de Schur. La sustitución por nuevas direcciones de 2557 ss. da el factor (\varpi^B\prod\det(g_{\tau,h})^{\kappa_\tau(h)}); las tres clases de congruencias (a)–(c) cubren las parejas de alturas (h=1), (h\ge2,h'=1), (h,h'\ge2). Este control combinatorio no prueba por sí solo que el kernel real tenga la forma normal requerida. Quedan por verificar `pa:kernel`, el tratamiento de 2 y de los primos del nivel, y `pl:level`. El nivel (N) se trata aparte en `pa:level` (3169): no debe confundirse con una aplicación del teorema de Hecke de 50.

### 53–54: qué queda comprobado y qué no

**Exchange.** En 53 `pcx:X`, líneas 1772–1795, se exige (a=b+2e\), (q=q_V+q_{V'}\), (2q+2\le N\), (N\le2\mu_\tau+2q\), módulo no trivial y carácter con parte tame no trivial en cada primo elegido. El escalar tiene (|c|^2=C L_*(\mathfrak m,\nu,e)); no puede sustituirse por una constante universal independiente del carácter. La independencia afirmada corresponde a (C) y al vector (x). La transposición de índices de splitting en `pcx:eq-dict` (1809 ss.) sí es exacta a partir de las dos definiciones impresas. No he auditado todo el cálculo de (C), ni la prueba completa de `pcx:X`; la fórmula clásica de Rallis no sustituye esa verificación.

**Inyectividad.** `pc:tri-inj` (53, 557–580) es un argumento correcto de álgebra lineal, con las hipótesis (T1)–(T3) de `pc:triangle`. No divide por (\sigma_{i,n}) para probar inyectividad, por lo que no incurre en circularidad al deducir después que esos escalares no son cero. Lo pendiente es la realización automórfica `pc:tri` (1248) y el primer lift: no basta verificar el triángulo abstracto para certificar `au:inj` o `au:factor` de 46.

**Un lift.** En 54, `po:ss-proof` (1134–1164), (\Delta_j) es el determinante del operador de comparación **comprimido** al espacio de lifts. La identidad

\[
\det(\Theta^*\Theta)\det(\operatorname{pr}_{\mathrm{im}\Theta}U|_{\mathrm{im}\Theta})
=\det(\Theta^*U\Theta)
\]

es correcta para un (\Theta) inyectivo: se obtiene escribiendo (\Theta=QR), con (Q) isométrico y (R) invertible. No requiere que (U) preserve la imagen. Las ecuaciones de `po:glue` y `po:exchange` dan entonces la potencia (H_j(\vartheta)^{d_j}) que usa 46. No he comprobado todos los inputs de `po:glue`, incluyendo los productos generadores, las formas falsas y los tres intercambios. Dictamen global (c).

**Valoración alcanzada.** `psm:attained` (54, 8249–8296) construye (t=M^{12f}c_{{\rm vac},y}\prod B(l_\tau)^2). La elección de un coeficiente de valoración mínima en una combinación con coeficientes integrales es válida y tiene el sentido correcto. El uso de la desigualdad ultramétrica no permite inferir igualdad de una valoración individual: da exactamente la desigualdad unilateral declarada. Quedan pendientes el teorema de doce factores `psm:twelve` y todos los inputs de la construcción de los coeficientes. `psu:small` (9118) usa además integralidad y ortogonalidad de la forma test; no he certificado esta última.

**Cota archimediana.** `psu:arch` (9217) cancela (a_\sigma(z)B(z)) entre un par principal y uno plano de igual rango. La cancelación funciona si (CL), enunciado inmediatamente antes, tiene el mismo (a_\sigma(z)) para ambos pares. La prueba final de la desigualdad es correcta condicionada a (CL), a la fórmula de norma y a las cotas de tamaños; no he verificado todo el teorema 9.1 de 53 que establece (CL). El factor factorial de `psu:normL` debe conservarse: el vector de peso máximo tiene norma 1 y el monomio de Fock norma al cuadrado (\prod l_\tau!).

### Uniones revisadas

| Unión | Resultado de la comparación |
|---|---|
| 50 `ph:thm` → apéndice de 49, líneas 8639–8655 | Mismo rango, mismo (c_d), mismo término (\theta j) y mismos tres inputs. |
| 50, líneas 844–847 → 49 `pa:eldiv`, líneas 3156–3164 | Mismos (12A_{\mathfrak l}/(mp)+j_0/(m^2f)), mismo (j_0\ge0), misma colongitud truncada. |
| 54 `psu:small` → 54 `po:small` | Se conserva (fmb/k+3x^{35}); el enunciado inicial ya incorpora la constante corregida. |
| 54 `po:small` → 46 `au:hecke`, líneas 4992 ss. | 46 menciona expresamente la constante (3x^{35}), no la versión anterior. |
| 54 `po:ss-proof` → 46 `au:onelift`, líneas 4965–4980 | Coinciden la compresión, potencia (d_j), denominadores y la posibilidad de absorber un factor independiente del twist en (C_j). |
| 53 exchange → convención alternativa de 54/55 | El diccionario declarado es intercambio de índices, sin factor; no se verificaron todas las sustituciones concretas posteriores. |
| 53 triángulo → 46 `au:factor` | Depende además de igualdad de multiplicidades de 51; no certificada por este informe. |

Esta tabla **no es una auditoría exhaustiva de cada cita** de los cuatro manuscritos. Las uniones no listadas, incluida toda la dependencia de 55 para familias regulares, quedan (c).

### Literatura y novedad

La identidad de Chowla–Selberg es previa: [Chowla–Selberg, *On Epstein’s Zeta-function* (1967)](https://doi.org/10.1515/crll.1967.227.86). La teoría general de Siegel–Weil regularizada y Rallis también es previa: [Gan–Qiu–Takeda, arXiv:1207.4709](https://arxiv.org/abs/1207.4709). Estas fuentes localizadas corroboran antecedentes y no certifican las normalizaciones particulares de estos manuscritos.

El candidato más delimitado a una contribución autónoma en el bloque revisado es el teorema de 50: un promedio integral compatible con un ciclo de Frobenius y un conteo de defectos que controlan colongitudes de operadores de aristas. La conexión propuesta en 49 y 54 entre períodos CM exactos, jets integrales en todos los primos y cotas de determinantes es una arquitectura de investigación concreta. Su novedad bibliográfica y su validez global no están establecidas por esta revisión. No hay fundamento aquí para afirmar que ya se creó un campo nuevo o que esa arquitectura demuestra RH.

### Matriz solicitada de los inputs de 46

Se separa deliberadamente **concordancia del enunciado** de **validez de la demostración**. «Coincide» significa que se conservan las condiciones indicadas al comparar los pasajes señalados; no equivale a certificar todos los antecedentes. Para `inj`, `factor`, `hecke` no se efectuó una comparación literal integral de todos los apéndices.

| Input de 46 | Concordancia examinada | Demostración y rango |
|---|---|---|
| `au:seesaw` (4314) | 49 §5.1.7 desarrolla el resultado; el dato puede depender de (\vartheta), el escalar no; se conserva la ausencia de afirmación de no nulidad. | (c): transferencia de la órbita, intercambios y ensamblaje completo pendientes. |
| `au:divis` (4368) | Coincide con 49, apéndice 8533–8555: excepción (N), módulos ramificados, (\ell\nmid\mathrm NQ), (2mfb), (j_\ell=\lceil2mfa/\ell\rceil); no se afirma que (Y_{\mathfrak l}) preserve el subespacio ramificado. | (c): el componente algebraico de 50 está revisado; la forma normal de los kernels, el nivel y el ensamblaje de todas las clases de primos no. |
| `au:count` (3900) | Coincide con `pa:count` y `pa:schur`: menores de las primeras (h) columnas o entradas de Schur, (B\ge1), alturas (<n'), pérdida (fn'^3(1+\log_pB)), y término (e=0) extra para (p=d). | (c): revisada cobertura de las congruencias de direcciones; no toda la prueba de forma normal y teoría de monomios estándar. |
| `au:kernel` (4497) | Coincide con 49 apéndice 8570: (0\le j<m), todo conjugado, (\exp(x^{50}+\mathrm{rs}_j/2)). | (c): depende de reciprocidad, constante CS exacta y comparación explícita de (C_0\) con los datos. |
| `au:restrict` (4516) | Coincide con 49 apéndice 8580: norma al cuadrado, pérdida (x^{70}), ganancia (-\sum n_\tau\log N). | (c) para el resultado completo; comprobado el paso de 49, 3830–3841, **dado** branching integral: (|\sigma\bar\pi_N|^2=N) y (c_{\rm br}^2\le L^{6L}\le e^{x^{70}}). Falta certificar la construcción de branching. |
| `au:expansion` (4532) | Coincide con 49 apéndice 8587: soporte finito, integralidad sólo fuera de (N\mathrm NQ), y cota (e^{x^{60}}) sólo para twist trivial. | (c): no se revisó por completo la eliminación del gluing ni el conteo de coeficientes. |
| `au:equiv` (4584) | Coincide con 49 apéndice 8604: carácter tame, (\beta_\vartheta(u)\in K^\circ), acción por traslación derecha. Se permite dependencia de (\vartheta). | (c): falta certificar integralidad de cada componente local de (\beta_\vartheta(u)) y compatibilidad con el gluing. |
| `au:shortbasis` (4427) | Coincide con 49 apéndice 8558 y prueba 3587–3622: (c_0) entero positivo en la diferente, cota (6c_0(fn)^2). | (a), comprobado: transferencia elemental con dimensión (2fn), dual de ((2/c_0)L) contenido en (L), y selección de (n) vectores (E)-independientes. El resultado pide una base sobre (E), no una base integral del módulo (L). |
| `au:inj` (4794) | 53 identifica la deducción con `pc:tri-inj` y el triángulo automórfico. No se certificó comparación literal de todos los antecedentes. | (c) global; (a) el argumento abstracto `pc:tri-inj`, conservando (T1)–(T3). |
| `au:factor` (4850) | 46 conserva twists (m)-fold, exponentes (\vartheta^j), potencia (-\dim\mathcal T) del factor de ratios y cocientes de Gram. Falta cotejo completo de construcción de cada ratio con 53. | (c): requiere triángulo automórfico, ley adjunta e igualdad de multiplicidades (M+), además de inyectividad. |
| `au:aux` (4878) | Coincide con 53 apéndice 16275: (\gamma(1)=1), no nulidad, twists (m)-fold, integralidad fuera de (Q), norma al cuadrado (e^{2x_1^2b^2}). | (c): `pc:auxcore` (1616) proporciona explícitamente la cota intermedia (e^{2x^{201}b^2}) y generadores (e^{x^{99}b^2}); no se certificaron todos los giros del segundo retículo de lifts. |
| `au:onelift` (4965) | Concordancia comprobada con 54 §2.6: operador comprimido, (Delta_j\ne0), potencia (d_j), constante independiente del twist; véase detalle anterior. | (c) global; identidad de determinantes correcta dados `po:glue` y `po:exchange`. |
| `au:hecke` (4991) | 46 conserva la hipótesis familia regular y cita la constante corregida (3x^{35}) de 54. No se cotejaron íntegramente todos los ratios de su producto. | (c): faltan CL de 53, inputs de sharpness, ortogonalidad de test forms y condiciones de regularidad importadas de 55. |

La comprobación adicional de `au:shortbasis` usa lo siguiente. Si (\lambda_1(\Lambda^*)\ge\rho), Minkowski da un vector primitivo de (\Lambda) de longitud (\le m/\rho); proyectar ortogonalmente a ese vector y proceder por inducción da radio de recubrimiento (\le m^2/\rho). Los vectores de longitud (\le3m^2/\rho) generan el espacio real. Para el retículo hermitiano (L=E^n\cap g\widehat{\mathcal O}_E^n), unimodular, un vector no nulo tiene norma al cuadrado al menos (f), por positividad total e integralidad de (h(y,y)). Como (c_0\) pertenece a la diferente, el dual euclidiano de ((2/c_0)L) está contenido en (L). Tomar (m=2fn), (\rho=1) y multiplicar por (c_0/2) da exactamente (6c_0(fn)^2). No interviene una constante no efectiva.

### Segunda revisión crítica del alcance de (a) en 50

No hay hipótesis llamadas literalmente (H1)–(Hn) en esta versión del archivo. Para que el dictamen no oculte contexto, esta es la lista reconstruida de supuestos. Los tres inputs no reemplazan las condiciones estructurales sobre el operador.

| Hipótesis | Fuente | Cómo entra o se comprueba |
|---|---|---|
| Dominio de valoración de característica 0, (p\) no unidad, (w^2=p) | 335–337 | Permite diagonalización finita, cancelación, Kummer y reducción módulo potencias de (w). No se supone DVR ni noetherianidad. |
| (W) local, cuerpo residual (\mathbb F_q) | 337 | Da clases con diferencias unidades y reducción sobreyectiva de (GL_k(W)). |
| (N\ge2) par, (e\ge1), (P=p^e\ge5), (q=P^N), homomorfismos cíclicos (\iota_s) con congruencia módulo (p) | 337–348 | Es una hipótesis estructural, no conclusión de root/count/av. Implica (\iota_s(\mathfrak m_W)\subseteq p\mathcal O), con el argumento del factor unidad (1-y^{q-1}). |
| (k\ge2), (n\ge1), (0<2r\le k), (r) entero, representaciones alternadas estándar/dual | 350–358 | Se usa en profundidad, intercalación, conteo y bloque de parabolia. |
| (X,H) finitos, mapas de aristas, representantes (t(\varkappa)^{-1}K_r=\varkappa), (u(e)\in GL_H(\mathcal O)) | 374–380 | Necesario para tener dos restricciones y usar (u(e)^{-1}) en el casi inverso. Los casos de conjuntos vacíos tienen conclusión vacía/trivial. |
| Libertad `ph:eq-free` | 381–383 | Hace biyectiva la parametrización de aristas invertidas. No se deduce de los tres inputs; se verifica aparte en la aplicación automórfica, 823–831. |
| (f\) lineal, (Yf=fA), (\Lambda=f(\mathcal F_X)) | 401–403 | Permite trasladar la colongitud del operador abstracto al módulo imagen, que no tiene que ser libre. |
| (0<\theta\le1), (n^4\le q), ((Nk\log q/\theta)^5P^{3r}\le n) | 397–400 | Implica todas las desigualdades numéricas adicionales para los tres inputs, como se comprueba en 1505–1517. |
| `ph:root`, `ph:count`, `ph:av` y la inclusión `ph:AinC` | 661–703 | Las tres proposiciones son probadas en §3; `ph:AinC` también se prueba, en 1027–1051, usando root. No es un cuarto input externo sin demostrar. |

He vuelto a comprobar los lugares que suelen introducir hipótesis ocultas: el grado sobre el anillo con nilpotentes en root (el divisor es mónico), la finita generación de (U^+) en el promedio (proviene del álgebra finita (\mathcal S_d), no de noetherianidad), Nakayama en `ph:near` (módulo finitamente generado), y el conteo de redondeos de valoraciones en `ph:ends`. No he obtenido una corrección concreta a (a) para la formulación algebraica bajo este contexto. El resultado aplicado a todos los datos globales de 49 sigue (c); los tres inputs no prueban por sí solos la libertad de aristas, la aproximación débil ni la normalización aritmética.


## Revisión matemática de los papers 51 y 52

Fecha: 28 de noviembre de 2026. Fuentes examinadas: los `main.tex` locales de 51 y 52, los enunciados y aplicaciones correspondientes de 46 y el mapa 57. Los números de línea se refieren a esas fuentes, no a los PDF. No se leyeron 47 ni 48.

**Dictamen global: (c), no verificado.** No se ha certificado la demostración completa del segundo momento ni de sus tres entradas locales. Sí se comprobaron reducciones importantes, constantes algebraicas y varios puntos de unión. No se encontró un contraejemplo que permita clasificar el teorema principal como (b). Las verificaciones parciales que siguen no deben elevarse a una aprobación de las aproximadamente 17.000 líneas de ambos archivos.

Los referentes nombrados por el autor no participaron en esta revisión. Ésta es una revisión por un agente con tarea de análisis automorfo y fórmulas de traza.

### Dictámenes por pregunta

| Pregunta | Dictamen | Paso que queda sin certificar |
|---|---|---|
| Segundo momento `au:moment`, uniforme en rango y con constante exacta | **(c)** | Construcción y estimaciones completas de los coeficientes/Bessel, especialmente `pbe:ds`, `pbp:main`, y las entradas locales `pbm:inputs`; véanse P51:2331, 6801, 3890 y P52:926, 4192, 4223. |
| Término principal por Siegel y Poisson con todas sus constantes | **(c)** para el resultado completo; varias reducciones **(a)** indicadas debajo | La desigualdad de Siegel para los cuadrados de sumas orbitales, `pff:S`, no queda certificada sólo por verificar la fórmula de representación de números o la cancelación formal de constantes. |
| Términos restantes y exhaustividad del conteo | **(c)** para las cotas geométricas; **(a)** para el cierre del rango, condicionado a los pilares enunciados | Falta certificar íntegramente `pbg:main`, `pbc:C1`, `pbc:C2`, `pbs:S`, `pbo:O1`. No hay un rango omitido evidente de corango mayor que `n^3`: el texto contiene una reducción explícita. |
| Igualdad de multiplicidades y atribución | **(c)** para la prueba completa; alcance y atribución precisados debajo | Falta verificar íntegramente las cotas del núcleo y la identidad orbital archimediana `pbr:main`. La afirmación usada tiene proyección cuspidal y parámetros específicos; no es una invariancia general de todo el espectro. |

En esta tabla, «falta certificar» identifica el alcance de la revisión. No afirma que esos pasos carezcan de una prueba en el manuscrito: sus pruebas están escritas y requieren una auditoría adicional.

### Segundo momento y la constante del término principal

P46:4692–4706, `au:moment`, pide

\[
\sum_{s\in\overline G}\|P^*\varrho(s)P\|_{HS}^2
\le (1+9b^{-4})\frac{D_X^2}{\deg\,\operatorname{mass}_r}.
\]

P51:180–195 reproduce los mismos tres enunciados; `pb:thmB`, P51:1112–1128, los deduce de `pb:est` y la comparación de multiplicidades. La norma es Hilbert–Schmidt. No se la debe confundir con la norma operatorial, para la cual el paso a generación tendría otro contenido.

La necesidad de una constante principal próxima a uno es real. Si las imágenes de una aplicación isométrica se distribuyen en un subespacio de dimensión `d/C`, un segundo momento con constante `C` todavía puede ser compatible con esa concentración. Por eso una cota con constante absoluta arbitraria no sustituye a la escrita.

**Comprobación (a), reducción condicional de L2.** En P51:3994–4026, si se aceptan (R), (F), (S), el teorema de criba y las cotas (C0), (C1), los factores finales son

\[
(1+b^{-6})\left[(1+b^{-9})^2(1+b^{-6})+b^{-10}\right]
\le 1+b^{-4}.
\]

Esto vale para `b≥1000`; los términos distintos de uno son de orden `b^{-6}`, muy menores que `b^{-4}`. El factor `b^{-6k#A}` se recupera del término de error usando `#A≤f`. No hay una pérdida oculta de un factor absoluto en esta última deducción.

**Comprobación (a), cancelaciones de C0.** En P51:3925–3963, `pbm:const`, tomando `n=ρ+1`, `r=k+2ρ+1`, `v=(2/rd_E)^f`, se verifican las identidades de exponentes

\[
\tfrac12-k-n-2\rho(\rho+k)
=\rho-(2\rho+1)(k+\rho+\tfrac12),
\]

\[
k+n+2\rho(\rho+k)
=1+(2\rho+1)k+\rho(2\rho+1).
\]

Son precisamente los exponentes de `rd_E` y `2`. La identidad de volúmenes compactos utilizada allí se obtiene directamente de `vol U(j)=∏_{a=1}^j 2π^a/(a−1)!`. Aceptadas las masas y el covolumen indicados, queda la desigualdad escalar

\[
\mathsf L\le(1+b^{-9})(1-N^{-k})^f.
\]

Es incorrecto describir el término principal como una igualdad exacta sin corrección: el texto conserva `L` y `(1−N^{-k})^{-f}`, y absorbe su desviación en el margen explícito.

**Hipótesis de tamaño heredada que conviene explicitar.** La última estimación de (C0), P51:3961, usa `f·2^{3−k}≤b^{−10}`. No se deduce de las desigualdades enumeradas en el encabezado de `pbm:const` por sí solas: con `k,n,f` fijos, aumentar `b` preserva sus cotas superiores y hace fallar esa desigualdad. En los datos admisibles sí está disponible la información adicional `k≥x⁵/2` y `x≥(log b)¹⁰⁰`, que la garantiza. Una condición local suficiente es `k≥20 log b+4`, junto con `f≤b/1000`. Esto no refuta la aplicación a los datos del paper, pero la afirmación de suficiencia de una lista aislada de parámetros debe incorporar esa condición o citar explícitamente las cotas heredadas. Las cancelaciones algebraicas verificadas arriba no dependen de esta observación; el cierre numérico de C0 sí.

La razón exacta de masas está en P51:1336–1357, `pb:massratio`. Es compatible con el factor `2^{1-lf}` de Gan–Hanke–Yu para el género unimodular en el caso no ramificado: el factor global 2 cancela en la razón, pero `2^{-f}` no. Véanse las proposiciones 4.4–4.5 de [Gan, Hanke y Yu, *On an exact mass formula of Shimura*](https://web.math.princeton.edu/~jonhanke/Web-02/Mass-Formula-of-Shimura/shimura-mass.pdf). Esta comprobación no sustituye la auditoría de cada identificación de retículos que permite aplicar esa fórmula.

### Poisson, Siegel y las entradas locales

**(a), lema de Poisson unilateral `pbm:poisson`, P51:3661–3684.** En el grupo adélico utilizado, la periodización de una función integrable no negativa tiene coeficientes de Fourier `c_L^{-1} F̂(η)`. Si la suma absoluta de esos coeficientes es infinita la cota es trivial. Si es finita, representa una función continua, igual casi en todas partes a la periodización y acotada por dicha suma. La semicontinuidad inferior en el conjunto finito de puntos permite acercarse a cero por puntos de igualdad casi en todas partes. Esto prueba la desigualdad con el factor `1/c_L` escrito. No exige igualdad puntual de una fórmula de Poisson clásica para una función arbitraria.

**Comprobaciones de normalización de Siegel.** P52:5442–5460 obtiene correctamente los productos de medidas aditivas de covolumen uno:

\[
\operatorname{covol}(\mathcal O_E\subset\mathbb C^f)
=2^{-f}|D_E|^{1/2},\qquad
\operatorname{vol}(\widehat{\mathcal O}_E)=2^f|D_E|^{-1/2}.
\]

También usa `|D_E|=|D_{E^+}|²` cuando `E/E^+` es no ramificada en los lugares finitos. P52:5504–5513 calcula correctamente la densidad arquimediana

\[
\int_{\mathbb C^k}\delta(|x|^2-a)\,dx
=\frac{\pi^k a^{k-1}}{(k-1)!},\quad a>0.
\]

Se deduce derivando el volumen de la bola de radio `√a`; no aparece un factor 2 adicional.

El teorema de Siegel–Weil que el manuscrito invoca está expresado con medida **de masa uno** en el cociente unitario compacto, P52:5426–5440. No sería correcto insertar sin compensación una medida de Tamagawa de masa 2. El original citado es [Weil, *Sur la formule de Siegel dans la théorie des groupes classiques*](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5988-11511_2006_Article_BF02391774.pdf). Esta revisión no certificó toda la traducción de su teorema 5 a la representación de Weil y los caracteres del manuscrito; ese punto permanece (c).

**Límite concreto de la revisión:** aun aceptando esa traducción y las dos medidas anteriores, queda por demostrar el paso de la fórmula de representaciones a `pff:S`, con separación de fibras, pesos y pares de términos. Ese trabajo está en P52:4279–4556. El cálculo de la densidad no demuestra por sí solo la desigualdad de segundo momento. Las cotas de los sistemas reales y finitos dependen de los lemas de descenso, profundidad, frecuencias y suma de capas, P52:708–871 y sus pruebas posteriores; no se han certificado íntegramente.

### El rango del conteo de pares

Una objeción que **no** está justificada por la versión examinada es afirmar que el autor sólo cuenta `l≤n³` y olvida todos los demás corangos. El cierre del rango está escrito en `pbe:rank(c)`, P51:2941–2955:

\[
1\le\mathsf d,\qquad
\mathsf d^2\le(2/M)^{2if}b^{2n^3f},\qquad M/2\ge b^{18}
\ \Longrightarrow\ 18i\le n^3.
\]

Como `l≤i+1`, resulta `l≤n³` en el rango del manuscrito. Esta deducción es **(a) condicionada** a la ganancia (G), al límite de la gauge y a la integridad que da `d≥1`.

El paso de (C1) y (C2) a (C), P51:6632–6659, también es correcto como reducción. Dos términos se envían al mismo par `(t,L_{γγ′})`; el cuadrado de la cota para un término da `b^{4000n^6(l+1)f}`, que es a lo sumo `b^{kf/4}` porque `l+1≤2n³` y `k≥512000n⁹`. La suma ponderada sobre los retículos aplica entonces (C2).

Los puntos todavía abiertos en esta revisión son la demostración de (G) mediante cortes e índices (`pbg:main`, P51:8176), el conteo de marcos de (C1) (`pbc:C1`, P51:8468) y la altura y suma de subretículos de (C2) (`pbc:C2`, P51:8769). La cobertura de pares no próximos y de bloques no concordantes usa además el truncamiento y la anulación de amplitudes; no se ha certificado todo ese argumento. Por tanto no corresponde afirmar que el conteo completo sea correcto, pero tampoco señalar un rango omitido sin refutar antes esas reducciones.

### Multiplicidades y atribución

`pm:main`, P51:4299, es una comparación con:

- un dato de comparación de espacios hermitianos y niveles identificados;
- parámetros de serie discreta con separación al menos `500n³+10n⁵` entre coordenadas de signos distintos;
- grado real `f` par;
- una componente de prueba supercuspidal en un lugar finito descompuesto.

`pm:mult`, P51:4331–4343, se aplica después al idempotente `e_0`; una etiqueta irreducible en un lugar proporciona la componente cuspidal por la propiedad (G) de Green. La igualdad es para las multiplicidades de caracteres de la álgebra de Hecke especificada, en los espacios proyectados, con tipos arquimedianos fijados. La frase sin estas condiciones, «los grupos isométricos en todos los lugares finitos tienen las mismas multiplicidades», es demasiado amplia.

La comparación de clases estables `pm:classes`, P51:4729–4777, explica por qué aparece la paridad: el producto de los signos que se desean cambiar es `(-1)^{f(q−q′)}`. El argumento usa normas globales y el principio local-global hermitiano; no se obtiene de una mera identificación de los puntos adélicos finitos. La suma de integrales orbitales en P51:4819–4836 emplea además `pm:arch(b)`. La prueba completa de ésta se remite a `pbr:main`, P51:5122 y siguientes; no quedó certificada en esta revisión. También quedan pendientes las cotas globales que justifican la traza del núcleo sin truncamiento.

La atribución amplia a Labesse es razonable como antecedente de comparación y estabilidad. **No** se verificó que la proposición exacta de P51 sea una cita literal de un teorema suyo, y el manuscrito no debería presentarla así. [Labesse, *Changement de base CM et séries discrètes*](https://webusers.imj-prg.fr/~michael.harris/CBCM.pdf), introducción y teoremas 5.4–5.5, impone hipótesis de no ramificación en lugares inertes para sus resultados de multiplicidad uno y estabilidad. P51 anuncia, en cambio, una demostración específica por comparación directa y cita también la fórmula simple de Flicker–Kazhdan. No se debe eliminar esas distinciones.

### Uniones comprobadas

| Unión | Resultado de la comparación |
|---|---|
| P51 `pb:thmB` → P46 `au:moment` | Mismos tres límites, mismos factores `5b^{-4}` y `1+9b^{-4}`, y misma normalización de `D_X²/(deg mass_r)`. Comprobado como enunciado. |
| P52 `pfr:R` → P51 `pbm:inputs(R)` | Coinciden masa `(1+b^{-10})/deg_τ`, pesos y decaimiento. La identificación de la forma superior con la forma de Gram, necesaria para Siegel, figura en P52 (R-b) y en P51:3898–3900. |
| Hipótesis reales de P52 → uso en P51 | P52 exige `ρ≥10⁸`, además de otras cotas (H0)–(H5). P51:4033–4038 y P52:958–964 mencionan expresamente esa condición y su satisfacción por los datos. No basta `n≥100`, pero el uso no se limita a esa condición. La verificación completa de (H1)–(H5) queda (c). |
| P52 `pff:F` → P51 `pbm:inputs(F)` | Coinciden masa `(1+b^{-6})b^{-6k#A}`, pesos, exponente y denominador. El sistema depende del grupo intermedio `Z(A,d)`, no sólo de `T`. |
| P52 `pff:S` → P51 `pbm:inputs(S)` | Coinciden los factores `r_*²`, `(1+b^{-6})a_*`, el conjunto de valores distintos de `t` y la condición de usar la misma forma finita de (F). `T` debe contener también los lugares no unitarios de la base; está escrito en ambos. |
| P51 `pm:mult` → P46 `au:mult` | P46 pide además la álgebra esférica completa, no sólo los lugares split. P51:5021–5030, `pm:rem-full`, extiende expresamente la identidad a lugares inertes; por eso no hay discrepancia de alcance en esta versión. |
| Retículo de P51 → retículo de P49/P46 | No son idénticos. P51:1027–1110, `pb:lattice`, ofrece un transporte por una adele de norma uno y conjugación unitaria de las aplicaciones de Poincaré. La invariancia de las normas Hilbert–Schmidt bajo ese transporte sí está comprobada; la identificación íntegra de los datos originales de P49 queda a la auditoría de ese paper. |
| P51 → P53 | La comparación de multiplicidades es una entrada relevante para la cadena. Esta revisión no certificó todas las aplicaciones en P53 ni todas las reproducciones en sus apéndices. Estado (c), sin discrepancia concreta demostrada aquí. |

La reciprocidad de citas 51↔52 no prueba circularidad por sí misma: el texto separa las identidades de coordenadas y medidas, usadas por 52, de la estimación L2 que vuelve a 51. Para certificar ausencia de ciclos hay que seguir las pruebas de esos lemas de base; se comprobó el diseño de dependencias, no toda su expansión transitiva.

### Trabajo necesario para cambiar los dictámenes

Para pasar de (c) a (a) hacen falta tres verificaciones independientes y reproducibles: una de `pbe:ds` y del período estacionario `pbp:main`; otra de los sistemas locales (R), (F), (S), especialmente de la separación de fibras y de todas las estimaciones uniformes; y otra del núcleo de traza y las integrales orbitales de `pbr:main`. Para el conteo, conviene emitir certificados separados de (G), (C1) y (C2) con las desigualdades de parámetros incluidas. Las reducciones ya comprobadas indican qué constantes se deben preservar y evitan repetir objeciones que la versión actual sí trata.


## Dictamen especializado: papers 55 y 56

Fecha de revisión: 28 de noviembre de 2026. Textos: `04-papers/55-covolume-theorem-regular-families-of-twists/main.tex` (8200 líneas) y `04-papers/56-explicit-cup-exponents-local-galois-representations/main.tex` (8380 líneas), copia de trabajo local. Las referencias de línea se refieren a esos archivos, abreviados P55 y P56. No se leyeron 47 ni 48.

**Resultado global: (c), no verificado en su totalidad.** Esta revisión no establece un contraejemplo a los teoremas principales de estos dos papers. Tampoco certifica sus pruebas completas. Sí comprueba varias reducciones, descarta una objeción demasiado general sobre irreducibilidad y delimita los resultados que faltaría verificar independientemente. Una reducción correcta suponiendo sus lemas no constituye un dictamen (a) sobre el teorema final.

Se distinguen abajo dos sentidos de «falta»: un argumento ausente del manuscrito y una comprobación que esta auditoría todavía no ha completado. En los puntos (c) que siguen, el manuscrito normalmente **sí contiene** pruebas de los lemas señalados; lo pendiente es validarlas, no su mera existencia. No se atribuye este dictamen a ninguno de los matemáticos mencionados por el usuario.

### Respuestas a las preguntas de P55

| Pregunta | Dictamen | Paso concreto pendiente o resultado comprobado |
|---|---|---|
| Existencia para todo primo, `pg:I`, `pg:II`, `pg:III` | **(c)** | `pg:I` depende de la transferencia y de la comprobación local en `pga:G123`/`pga:G45`; `pg:II` del descenso `pse:step` y de los polinomios de valores L `pse:stick`; `pg:III` de los módulos de trazas y la realización por operadores auxiliares. No se ha completado una comprobación de todas esas pruebas y de todos los teoremas externos con sus hipótesis. |
| Paso Selmer → congruencias módulo potencias de ℓ | **(c)** para el argumento completo; **(a)** para la observación de que la irreducibilidad requerida está explícita | `pri:ribet(1)` exige que la imagen del bloque genere toda la álgebra de matrices. No hay que añadir esta hipótesis como si estuviera omitida. Falta certificar toda la construcción de los determinantes de filas ligadas y su realización automorfa. |
| Pérdida local `pg:loss` | **(c)** | La reducción por dualidad es comprobable; el exponente numérico depende de P56, `pki:crys`, y del caso tame. |
| Clases impares `pg:odd` | **(c)** | No se ha certificado el aniquilador `pod:annih` ni el descenso de Euler que transforma aniquilación en longitud con la constante declarada. |
| Suma sobre todos los primos | **(a) como reducción aritmética condicionada a las cotas declaradas**; **(c)** como consecuencia incondicional de la serie | La suma del término local y el cambio de unidades de valoración a logaritmo están bien planteados y se comprueban abajo. La cota para `C_odd` y las cotas locales no quedan certificadas por esa suma. |

#### 1. La irreducibilidad residual no es una hipótesis tácita

P55, definición `pg:def-summand`, líneas 563–585, exige en (M4) que para toda retícula estable suficientemente definida los `u(g)` generen `M_n(O)`. El texto explica su interpretación en las líneas 586–589. La versión exacta `pri:ribet`, líneas 2565–2588, vuelve a exigirla en (1), para el bloque `rho_pi`.

El lema `pg:burnside`, líneas 805–830, da un argumento pertinente y correcto bajo sus hipótesis:

1. Los autovalores de la inercia son distintos módulo el ideal maximal; las diferencias son unidades y los proyectores espectrales son integrales.
2. La retícula se descompone en sus líneas propias.
3. Frobenius permuta esas líneas en un ciclo completo.
4. Un subespacio estable después de cualquier extensión residual es suma de líneas propias y estable por ese ciclo: es cero o todo.
5. Burnside sobre el cuerpo residual y Nakayama sobre `O` dan la generación integral de la álgebra de matrices.
6. `phi^n` preserva cada línea y conmuta con el ciclo, por lo que es escalar.

Esta comprobación no usa que ℓ sea grande: usa que ℓ sea distinto de la característica residual del lugar auxiliar y que los autovalores sean incongruentes. La estrategia de dos primos de nivel para poder escoger el otro cuando ℓ coincide con uno aparece expresamente en `pg:rem-primes`, líneas 475–487. Queda por certificar que **todos** los sistemas automorfos que se usan tienen las etiquetas y tipos locales necesarios: eso remite a `pga:G123`, `pga:G45` y a la selección de etiquetas. No es correcto sustituir esa tarea por la afirmación «Ribet necesita irreducibilidad y aquí no se supone».

#### 2. Qué se comprobó del argumento de twists

Los lemas sobre raíces de unidad `pg:roots1` y `pg:roots`, líneas 922–990, tienen un mecanismo coherente: se compara la valoración de evaluación con la valoración de Gauss; se cuenta la contribución de raíces del polinomio sobre círculos de radio `rho_h`; el promedio truncado por 1 produce un punto sin pérdida mayor que `delta`; se especializan sucesivamente las variables. En la reducción de potencias `1≤j≤m`, escoger la raíz de mayor valoración de `(1+Y)^j-(1+x)` garantiza `v(Y)≥v(x)/j`, y no presupone `j` primo a ℓ. Este aspecto sí cubre primos pequeños.

El lema `pg:minor`, líneas 1068–1100, explica por qué los menores máximos controlan la longitud de un kernel módulo `ℓ^M`. La fórmula `sum min(M,v(d_i))` y el paso al grupo con coeficientes `K/O` cuando la longitud es menor que `M` son correctos. El resto de la existencia de la especialización útil depende del descenso de grupos de Selmer: `pse:mirror` (1780–1840), `pse:step` (1872 y siguientes), y de `pse:stick` (2051 y siguientes). **No se ha verificado íntegramente esa dependencia.** En particular, no basta verificar la especialización de polinomios para concluir la cota Selmer: primero hay que demostrar que existe un punto donde los menores poseen la valoración requerida.

#### 3. Pérdida local: reducción comprobada, exponente pendiente

P55 `pll:D2`, líneas 3314–3358, no se limita a citar una forma integral de Bloch–Kato: escribe una prueba por longitudes. Sus pasos son apropiados:

- La imagen de `H_f^1(T)` en `H^1(T/ℓ^m)` es `H_f^1(T)/ℓ^m`, porque la preimagen de un subespacio racional es saturada.
- Su longitud es `m(h_f-h_0)+len H^0(T/ℓ^m)`.
- Las dimensiones tangentes de una representación de Rham y de su dual de Tate suman `[F:Q_ℓ] rank(T)`.
- La característica de Euler local y la dualidad de Tate dan que las dos imágenes ortogonales tienen longitudes complementarias.

Esto sustenta `pll:dual` (3360–3394), sin convertir por sí solo una cota racional de Bloch–Kato en la cota integral nueva del paper.

También se comprueba el mecanismo de `pll:ribet`, líneas 3408–3446. Se toma `Y=⊕End(u_x)` con **multiplicación por la izquierda**, no con la acción por conjugación. Por eso `Y` es suma de copias de las representaciones originales. El submódulo generado por `(u_x(g)-1)_x` es estable, y las relaciones permiten definir el morfismo hacia `T/ℓ^M`. La exactitud racional de `D_cris` sobre las representaciones que se vuelven cristalinas sobre una extensión común muestra que el cociclo en ese submódulo es cristalino. La elección de la acción por la izquierda es esencial y está hecha correctamente.

Lo que no está certificado es la cota nueva de `pll:exponent`, líneas 3487–3507, tomada de P56. La clasificación final de `pg:loss` sigue siendo (c).

#### 4. Clases impares y ℓ=2

`pg:odd` (1373–1380), `pri:odd` (2313–2327) y `pod:odd` (4382–4404) tienen la misma estructura: para `e≠0` se trata de cociclos antiinvariantes por conjugación compleja con condición local ciclótica, y para `e=0` de homomorfismos no ramificados en todas partes. La segunda formulación explicita `chi^e = Z_ℓ(-e)` y que el anillo de coeficientes contiene los valores de los caracteres de Dirichlet.

El manuscrito no aplica sin explicación un resultado de Euler systems válido sólo para ℓ impar. `pod:rem-two`, líneas 4406–4416, separa los primos `ℓ≤(N+t+3)^2`, usando aniquiladores y puntos detectores, de los mayores, donde aplica el descenso. Esto responde a la objeción de cobertura formal de ℓ=2, pero no prueba el resultado: deben verificarse `pod:annih` (4879 y siguientes), `pod:detect` (4511 y siguientes), y el descenso de las secciones posteriores. En esta revisión no se certifican esos tres pasos. No hay un contraejemplo establecido aquí.

#### 5. La suma de pérdidas, con todas las unidades

P55 define, líneas 416–433,

`lambda_ℓ = v_ℓ((2b)! · (∏_{b-30h³<n≤b+30h³} n)^{h³})`,

`loc_ℓ = 4f·10^6 (m/k) (b v_ℓ(M)+lambda_ℓ)`.

Para cualquier conjunto finito de primos `T`, la fórmula del producto aplicada a **un entero positivo fijo** da

`Σ_T lambda_ℓ log ℓ ≤ log((2b)!) + 60 h^6 log(b+30h³) ≤ 3b log b`,

con las separaciones de tamaño de los datos. Asimismo `Σ_T b v_ℓ(M)log ℓ ≤ b log M ≤22b log b`. Por tanto el factor `4·10^6·(3+22)=10^8` de `pg:sums` (520–522) es correcto.

La contribución `2^{-ℓ}` es sumable, y los términos que son valoraciones de `N_ch`, `C_odd` y `h_1` se suman como logaritmos de esos enteros. Al final, la absorción del término local en el presupuesto reduce a

`2·10^8 m² ≤ x (log b)²`,

que se obtiene de `m²≤4x` y `(log b)²≥8·10^8` (P55, 525–533). No hay que sumar la cota uniforme individual sin conservar el soporte finito o la estructura factorial: esa estructura es precisamente lo que permite la suma.

Este cálculo es una verificación de la **reducción aritmética**, no de la existencia previa del entero `C_odd` con el tamaño exigido.

### Respuestas a las preguntas de P56

| Pregunta | Dictamen | Alcance |
|---|---|---|
| Exponente principal sin restricción FL, para todo ℓ | **(c)** | La deducción numérica de `pki:crys` a partir de sus proposiciones centrales se ha revisado; no se certifican todos los lemas de retículas, frames y caminatas de los que dependen. |
| NM: necesaria y suficiente | **(a)** para la identificación de su papel de hipótesis suficiente en la reducción y para su verificación aritmética en la aplicación; **(c)** para la proposición genérica completa | El paper no afirma un «si y sólo si». NM no es necesaria para que el defecto se anule; se da un ejemplo abajo. |
| Caso potencialmente cristalino tame | **(c)** | El paso de los exponentes y la especialización a los datos encajan; pendiente la certificación del tame killer `pkw:T3` y sus insumos. |
| Novedad | **(c)** | La forma fina de la cota es una candidata a contribución; no queda establecida prioridad ni validez por contraste bibliográfico limitado. |
| Consistencia con FL | **Compatible en los subcasos comprobados; (c) como comparación completa de categorías y condiciones locales** | La anulación cuando `lambda=0` concuerda con lo esperado; el propio P55 no usa FL como sustituto de su prueba integral. |

#### 6. La afirmación principal es más restringida que el título abreviado

`pki:crys` (552–623) no dice que cualquier pareja de representaciones cristalinas de pesos arbitrarios tenga el exponente anunciado. Exige (S1)–(S4), ventanas opuestas, que las letras lean espesor, y pocos saltos bajos o el caso alternativo `U'⊆[-eta,0]`. En particular, «todo ℓ» no elimina las hipótesis geométricas sobre la distribución de pesos y embeddings.

La deducción distingue:

- `ℓ≤Q`: se usa `pki:sparse` con `J=floor(log_ℓ h³)`, radio bajo `2G`, `vartheta=2K`, `M=K`.
- `ℓ>Q`, `lambda≥h³`: se usa `pki:any`, y se obtienen `b+delta<Kℓ²` y `2(G+delta)<Kℓ`.
- `ℓ>Q`, `lambda<h³`: se usa `pki:generic` con `a=2(lambda+1)`.

En el último caso el resultado es directamente una **longitud de defecto**, no necesariamente un exponente que mate cada clase con esa misma constante dividida por el rango. P55 conserva expresamente esta distinción en `pll:exponent`. No se encontró aquí el intercambio ilícito «longitud por rango → exponente uniforme».

La comprobación completa aún debe cubrir `pkf:main` (2868), los teoremas de profundización `pke:I2` (4829), `pkh:I4` (5793) y el esquema `pkd:scheme` (6882), con sus dependencias. Son pruebas escritas, pero esta auditoría no ha certificado cada una. En particular, comprobar las desigualdades 570–623 sin comprobar esos resultados no verifica el teorema.

#### 7. NM: qué significa y dónde se usa

La definición de NM en P56, 380–382, excluye múltiplos **no nulos** de ℓ en tres intervalos alrededor de `0`, `b_z` y `-b_z`, de radio `n`. El lema `pkc:free`, 6310–6321, utiliza exactamente esa exclusión para que los costes de los pasos de nivel cero sean cero en una carta no ramificada. El valor convencional de la función de coste en `y=0` es cero; no se está afirmando que la valoración ordinaria de 0 sea cero.

En la aplicación `lambda<h³`, líneas 600–607:

1. Si ℓ dividiera un entero en `(b-30h³,b+30h³]`, la potencia `h³` de ese factor forzaría `lambda≥h³`.
2. Con `a=2(lambda+1)` se tiene `n=6(a+eta+W)<13h³`.
3. Todo múltiplo no nulo de ℓ tiene valor absoluto al menos `ℓ>198G`, por lo que queda fuera del intervalo bajo y de los intervalos alrededor de `±(G+delta)`.
4. Los intervalos alrededor de `±(b+delta)` quedan dentro del intervalo factorial ampliado anterior, porque `delta+n<30h³`.

Así se comprueba NM en **ambas** clases de letras, gruesas y finas; no se presupone sin control para `G`.

NM no es necesaria para la conclusión de defecto cero. Un ejemplo de rango positivo: `F=Q_23`, `U=U'={0}`, `L=Z_23` trivial, `a=2`, `eta=1`, `W=0`, `b_z=20` en todas las letras. Aquí `e=f=1`, `ℓ≥5`, `eta≥1`, las dos ventanas contienen 0 y no hay saltos en `[-a,0)=[-2,0)`. Se cumplen `b+W+eta=21≤(23-3)·2=40` y `6(a+eta+W)=18<20`. NM falla porque `y=23` es no nulo, divisible por 23 y está a distancia 3 de 20. Así se satisfacen todas las otras hipótesis de `pki:generic(i)`. Las representaciones cristalinas con todos sus pesos cero son no ramificadas, y sus retículas también. Para cualquier emparejamiento equivarante módulo `23^m` entre esas retículas y `L`, escojamos un elemento de inercia `g` cuyo carácter ciclótomico vale `-1` módulo 23. La equivariancia da `(epsilon(g)-1)b_psi(y,l)=0`; el factor es una unidad, por lo que el emparejamiento hacia `Z/23^m(1)` es cero. En consecuencia el defecto aquí es cero, aunque falle NM. Este ejemplo refuta **la interpretación de NM como condición necesaria**, no el enunciado unilateral de `pki:generic`.

#### 8. Caso tame y dual de Tate

P56 `pki:tame` (464–474) y su repetición `pkc:tame` (6629–6638) imponen `F=Q_ℓ`, `e_0=lcm_{1≤i≤r}(ℓ^i-1)`, polinomios uniformes `K(s)` y la pertenencia del dual a la clase con `K^{-1}(s)=K(s^{-1})`. La desigualdad `ℓ>b+6(W+eta)+r²(N+1)²+2` es parte de la hipótesis.

La deducción de 6643–6681 conserva los costes: `e_0≤ℓ^{r²}`, un polinomio de grado `≤N²` para el tensor dual, `kappa=r²(N+1)²`, y un coste total de caminata acotado por `3kappa+150(eta+W+1)`. La elección de `K^{-1}` es importante: aplicar el mismo polinomio directamente al dual sin invertir inercia sería incorrecto. El texto sí hace la inversión.

La aplicación a P55, `pkd:data(iv)`, 7224–7281, usa `N=(r+t)r=6r²`, `eta=h²+1`, `W=4t`, `delta_j=j Delta+h-2t` y `p_i≥b^{10}`. La cota exigida es menor que `2b`, por lo que la separación `p_i≥b^{10}` da el rango. También se explicita `L_c^*∈C(U',K^{-1})`; no se ha encontrado una omisión de esta hipótesis en la unión.

La parte no certificada es la prueba de `pkw:T3`, líneas 7753 y siguientes, que obtiene la aniquilación integral del cokernel a partir de inercia y del polinomio monico, junto con la preparación de las cartas tame. La aritmética del exponente, aun correcta condicionalmente, no sustituye esa prueba.

### Uniones: identidad del insumo frente a prueba del insumo

| Unión | Identidad/rango comprobados | Validez del insumo |
|---|---|---|
| P46 `au:regular` → P55 `pg:main` + `pg:sums` | Sí, en la reducción de P55 535–545. R1 proviene de (a); R2 usa el cociente inverso y `|·|_iota=ℓ^{-v}`; R3 usa `beta(ℓ)=(beta_ℓ+v_ℓ(h_1))log ℓ`. No se omite `log ℓ`. | (c), por las dependencias de `pg:main` y `pg:odd`. |
| P46 R3(i),(ii) → P55 `pg:def-den`, `pg:main(c),(d)` | Los falsos lifts se definen lugar por lugar y la ortogonalidad se pide para todos esos lugares. La contribución `h_1` está añadida a la cota de pares principales. P46 4895–4912 y P55 394–411, 438–458, 460–473. | Reducción coherente; falta certificar toda la construcción del operador. |
| P55 `pg:loss` → `pll:main` → `pll:exponent` | La primera cota es por defecto dual de `L_c^*`, no de `L_c`; el factor `[E_v:Q_ℓ]` y `x_main=1`, `x_e=t` están presentes. | (c), exponente procedente de P56. |
| P55 `pll:exponent(a–d)` → P56 prueba después de `pki:crys` | Coinciden los exponentes `10^4 floor(2lambda/Q)(floor(log_ℓ h³)+1)`, `10^4 floor(2lambda/Q)m`, el caso tame y la salvedad de longitud sin exponente. P55 3487–3507; P56 624–636. | (c) para los teoremas centrales. |
| P55 (M2) → P56 `pkd:data(i–iii)` | Comprobación algebraica correcta: el dual tiene saltos `-u-1`; `delta_j=jDelta+h-2t`, ancho `4t`, radio `h²+1` contienen los saltos y la cota de multiplicidad baja se conserva. | Condicional a que las representaciones de P55 satisfagan efectivamente (M2). |
| P55 tipos tame → P56 `pkd:data(iv)` → `pki:tame` | Coinciden `N=6r²`, los polinomios uniformes y la inversión `K^{-1}`. El rango en `p_i` basta. | (c), pendiente tame killer y origen automorfo de tipos. |
| P56 genérico → aplicación de `pki:crys(d)` | NM se deriva de `lambda<h³`, con control independiente de las letras de peso G. | (a) para la verificación de hipótesis y las desigualdades; (c) para toda la prueba de `pki:generic`. |
| P55 → P54, insumo (IM) para valores L | P55 señala explícitamente P54 §3.1, y `pse:stick` es el punto que lo usa. Esta revisión no certifica (IM) ni su normalización; pertenece a la auditoría especializada de P54. | (c). |

La dependencia P55↔P56 **no muestra por sí misma una circularidad lógica**: P56 importa definiciones, la cota elemental rango→defecto y propiedades de representaciones de P55; devuelve el exponente local. Para denunciar un ciclo hay que exhibir que alguno de esos insumos de P55 depende del exponente, no sólo que ambos papers se citan.

### Novedad y comparación bibliográfica limitada

La aportación candidata de P56 es la sensibilidad de una **cota integral de defecto de compatibilidad módulo ℓ^m** a la distribución de pesos y a la escasez de letras gruesas, en vez de sólo al mayor peso. P55 explica por qué le importa: quiere un ahorro proporcional a `m/k` después de sumar sobre lugares y primos. Esa conexión con un presupuesto global de denominadores es una idea identificable, aunque su validez matemática completa siga pendiente.

No es nuevo, por sí mismo, estudiar retículas cristalinas fuera del rango Fontaine–Laffaille ni representaciones de torsión para ℓ=2. Fuentes primarias pertinentes:

- Fontaine–Laffaille, *Construction de représentations p-adiques* (1982), [texto original](https://www.numdam.org/item/10.24033/asens.1437.pdf).
- Tong Liu, *Torsion p-adic Galois representations and a conjecture of Fontaine* (2007), [publicación](https://www.numdam.org/item/?id=ASENS_2007_4_40_4_633_0).
- Tong Liu, *A note on lattices in semi-stable representations*, [preprint](https://arxiv.org/abs/0709.4523).
- Caruso–Liu, *Some bounds for ramification of p^n-torsion semi-stable representations*, [preprint](https://arxiv.org/abs/0805.4227), [texto de los autores](https://www.math.purdue.edu/~tongliu/pub/bound2.pdf).
- *Torsion representations arising from (phi, G-hat)-modules*, [preprint](https://arxiv.org/abs/1202.1858), cuyo alcance incluye p=2.

Esas referencias no verifican automáticamente el exponente de este manuscrito. Tampoco la ausencia de una cota idéntica en una búsqueda limitada demuestra prioridad. La comparación exacta exige identificar categorías de torsión, mapas y condiciones locales, y luego derivar o excluir una cota equivalente. P55 `pll:FL`, 3467–3479, reconoce que no usa el camino Fontaine–Laffaille como sustituto. En el rango donde `lambda=0`, la conclusión de anulación concuerda con la expectativa de exactitud integral, sin que eso certifique los casos de pesos grandes.

### Alcance de los registros Lean

Se inspeccionó únicamente el README de `06-alpoge-verification`. Contiene declaraciones de compilación y de axiomas, y distingue expresamente compilación de revisión matemática. No se repitió la compilación, no se inspeccionó todo el archivo Lean ni se estableció una correspondencia declaración por declaración con P55/P56. Por tanto no se usa ese README para cambiar ninguno de los (c) anteriores a (a).

### Comprobaciones prioritarias para cerrar este dictamen

1. Certificar `pkw:T3`, `pke:I2`, `pkh:I4` y `pkd:scheme`, incluyendo integridad, constantes y compatibilidad de las retículas definidas por órdenes.
2. Certificar la transferencia automorfa y los tipos locales de `pga:G123`/`pga:G45`, contrastando las hipótesis exactas de los resultados citados.
3. Certificar `pse:step` y la entrada de P54 en `pse:stick`, no sólo el lema de especialización en raíces de unidad.
4. Certificar `pod:annih`, la cantidad de puntos detectores y el descenso de Euler con su dependencia en ℓ=2.
5. Sólo después de esas verificaciones, elevar la correcta contabilidad final de pérdidas a un dictamen sobre la existencia de familias regulares para todos los datos admisibles.


## Uniones entre los papers

La tabla de inputs del final de la sección automórfica de paper 46 (5055–5095) queda cubierta por la matriz de abajo y las comprobaciones específicas enlazadas. **No queda certificada toda la red de importaciones transitivas.** Se distingue la concordancia del enunciado importado de la prueba del enunciado y del cumplimiento de sus hipótesis en cada aplicación. Una cita mutua no prueba circularidad; la coincidencia textual tampoco prueba ausencia de ella.

### Inputs enumerados por paper 46

| Input | Origen | Concordancia comprobada | Dictamen de validez global |
|---|---|---|---|
| `au:seesaw` | 49 | El escalar es independiente del twist; el dato de cadena puede depender de él. | (c), falta certificar toda transferencia e integración. |
| `au:divis` | 49, 50 | Se mantienen excepción de nivel, truncación y pérdida de colongitud; no se afirma invariancia del subespacio ramificado por cada Hecke. | (c); argumento algebraico de 50 revisado aparte. |
| `au:count` | 49 | Se conservan las columnas anidadas y la deducción adicional en el primo ramificado. | (c), forma normal del kernel y ensamblaje. |
| `au:kernel` | 49 | Todo conjugado y la cota exponencial con `rs_j/2`. | (c), normalización exacta CM y reciprocidad. |
| `au:restrict` | 49 | Norma al cuadrado, pérdida `x^70` y término de nivel. | (c), branching integral pendiente. |
| `au:expansion` | 49 | Integralidad fuera del nivel y conductor; cota de tamaño para twist trivial. | (c), gluing y conteo. |
| `au:equiv` | 49 | Carácter tame y traslación derecha conservados. | (c), integralidad local de la traslación. |
| `au:shortbasis` | 49 | Base sobre E, no necesariamente base integral; constante `6c_0(fn)^2`. | (a) para el lema de geometría de números bajo sus hipótesis. |
| `au:moment` | 51, 52 | Tres cotas y constante `1+9b^-4` coinciden. | (c), estimaciones locales y uniformidad completas pendientes. |
| `au:mult` | 51 | Los supuestos de separación y proyección están presentes; `pm:rem-full` cubre lugares inertes. | (c), identidad orbital y justificación global de traza. |
| `au:inj` | 53, 54 | Triángulo y primer lift identificados; no se hizo comparación literal integral de todas sus entradas. | (c), realización automórfica; triángulo abstracto correcto. |
| `au:factor` | 53, 54, 51 | Se conservan twists m-fold y potencias; depende de la misma comparación de multiplicidades. | (c), exchange, factores y todas las sustituciones. |
| `au:aux` | 53 | Identificado origen en `pc:twistreduct`; comparación integral de hipótesis pendiente. | (c). |
| `au:regular` | 55, 56, 54 | R1–R3, factores `log ℓ`, denominadores y falsos lifts cotejados. | (c), Selmer, exponentes integrales y clases impares. |
| `au:onelift` | 54, 53 | Determinante comprimido, potencia `d_j` y factores independientes del twist coinciden. | (c), `po:glue` y sus antecedentes. |
| `au:hecke` | 54, 53 | `3x^35` ya propagado, no versión antigua; resto de aplicaciones de CL pendiente. | (c), test integral y comparación de normas. |

Los detalles y localizadores están en [theta y Hecke](../02-theta-hecke-covolumen.md), [spanning](../03-spanning.md) y [Selmer y Hodge](../04-selmer-hodge.md).

### Uniones que requieren especial cuidado

**Rango de 50 hacia 49.** La igualdad del enunciado citado incluye la fracción excepcional y el término `θj`. No se puede reemplazar una colongitud truncada por una cota uniforme de todos los divisores elementales. Las sustituciones numéricas se verificaron; la realización aritmética de todos los datos queda (c).

**Retículos 49 y 51.** No son literalmente el mismo retículo. El manuscrito lo reconoce y proporciona transporte adélico y conjugación unitaria (`pb:lattice` de 51, 1027–1110; `au:two-lattices` de 46). La invariancia de normas Hilbert–Schmidt por ese transporte es correcta. Comprobarla no certifica por sí solo todos los datos de la construcción original de 49.

**52 hacia 51.** El rango incluye `ρ≥10^8` y condiciones H0–H5. La condición más débil `n≥100` no sería suficiente, pero la versión actual menciona y verifica el tamaño mayor en los datos. (R), (F), (S) usan las mismas medidas, masas y pesos; la auditoría completa de H1–H5 y de sus pruebas queda (c).

**56 hacia 55.** El texto distingue cuidadosamente exponente aniquilador de longitud del defecto: en un caso genérico sólo se obtiene la segunda. Los duales, cambios de pesos e inversión `K(s^-1)` de tipos tame están presentes. NM se verifica a partir de `λ<h^3` en la aplicación examinada. No se encontró la pérdida de hipótesis que sugeriría leer sólo el título «sin restricción Fontaine–Laffaille».

**43–45 hacia 46.** La fórmula explícita y el criterio primitivo sí coinciden, según [la revisión del marco de Weil](../07-rows-a-b-c.md). Esas entradas se usan para interpretar la forma y la recíproca del criterio; no aportan la positividad que la cadena automórfica pretende demostrar.

### Inventario reproducible y límites

`evidencia/auditar_fuentes.py` genera:

- `fuentes.json`: hashes SHA-256, rutas y número de líneas de los catorce fuentes 43–46, 49–58, excluidos 47–48.
- `enunciados_compartidos.json`: texto y localizador de entornos con etiquetas compartidas.
- `uniones_textuales.tsv`: igualdad tras quitar etiquetas y normalizar espacios.
- `citas_internas.tsv`: referencias bibliográficas explícitas con claves P43–P56 o Paper43–Paper56, excluidos 47–48. No detecta claves con nombres alternativos como `Companion`.

La coincidencia de etiquetas es sólo una ayuda de navegación: etiquetas genéricas pueden nombrar resultados diferentes. Las macros también pueden cambiar de significado entre archivos. Por eso un `True` en el TSV **no es un dictamen (a)**, y un `False` no es un fallo matemático. Se inspeccionaron las diferencias de los principales inputs automórficos entre 46 y 58: las observadas son sustituciones de citas externas por referencias internas, no cambios demostrados de constante o rango.

**Estado de todas las uniones no individualizadas en las tablas:** (c), no verificado. Lo pendiente es comparar el enunciado completo, sus definiciones transitivas y la verificación de hipótesis en el lugar de aplicación. El inventario no reemplaza ese trabajo. No afirmo haber revisado semánticamente cada una de las miles de referencias de estos manuscritos.

Para cerrar la red hace falta una ficha por importación con origen, destino, correspondencia de símbolos, medidas, retículos, rango y prueba de las hipótesis de aplicación. Las fichas anteriores cubren las entradas centrales que 46 enumera; no bastan para certificar la conclusión GRH.


## Conexiones matemáticas y programa de investigación

El patrón central que propone la serie es convertir **divisibilidad de coeficientes theta en una desigualdad unilateral sobre primos**, mediante la comparación entre formas cortas, generación de casi todo un espacio y un límite inferior para su covolumen. Es una conexión concreta y susceptible de producir problemas independientes. En esta revisión no quedó demostrado que esa conexión cierre la prueba de GRH, ni que constituya por sí misma un campo nuevo.

La dificultad de RH no obliga lógicamente a que su solución invente una nueva rama. Una combinación nueva y válida de herramientas conocidas también podría resolverla. La pregunta productiva es qué puente exacto aporta el trabajo, cuáles de sus piezas están demostradas y qué resultados sobreviven si se retira la conclusión sobre RH.

Fuentes internas: P57 `main.tex`, particularmente líneas 100–120, 485–640 y 833–843; cotejo con los enunciados de P46 y la revisión específica de P51/52. Las referencias a «la propuesta» describen el argumento del manuscrito, no un teorema certificado por este informe.

### El mecanismo propuesto

La primera cadena conceptual es

\[
\text{Frobenius en CM y divisibilidad local}
\longrightarrow\text{coeficientes theta integrales y pequeños}
\longrightarrow\text{retículos de formas automorfas}.
\]

La segunda cadena intenta comparar esos retículos por dos vías:

\[
\begin{array}{c}
\text{seesaw y cotas de todas las conjugadas}\to\text{cota superior de volúmenes},\\
\text{valores L, congruencias, twists y fórmula del producto}\to\text{cota inferior}.
\end{array}
\]

El segundo momento de la aplicación de Poincaré debe garantizar que la primera vía alcance una proporción `1−O(b^{-2})` de la dimensión. La comparación cancela una cantidad principal común `H_main`. El desequilibrio restante se identifica con `R_{d,q}(x)`; un criterio analítico unilateral pretende convertir su cota en ausencia de ceros.

El punto potencialmente distintivo es, por tanto, **hacer coincidir cuantitativamente la aritmética local de theta con un error en la distribución de primos**, después de cancelar términos principales grandes en determinantes. Enumerar muchas especialidades no establece ese puente: lo establecen las identidades, la independencia respecto del twist, los rangos uniformes y los errores finales.

P57:100–112 dice expresamente que las filas A–C no entran en esa deducción y que no se construye allí un teorema del índice de Hodge para esos objetos. Por eso no corresponde presentar el mecanismo como una prueba geométrica del signo de la intersección adélica. Es una ruta automorfa y aritmética hacia el signo, reinterpretada posteriormente en el marco de Weil.

### Qué conexiones ya existen

| Conexión | Antecedente | Qué tendría que añadir la serie |
|---|---|---|
| Espacios adélicos, fórmula explícita y ceros | [Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*](https://arxiv.org/abs/math/9811068) interpreta fórmulas explícitas mediante una traza no conmutativa. | Objetos o propiedades adicionales precisos; la asociación «adeles + traza + RH» no es nueva. |
| Theta CM, coeficientes algebraicos y valores L de Hecke | [Bannai–Kobayashi, *Algebraic theta functions and p-adic interpolation of Eisenstein-Kronecker numbers*](https://arxiv.org/abs/math/0610163) construye y estudia ese puente. | Divisibilidad simultánea, casos no ordinarios, constantes exactas y uniformidad requeridas por 49/54; no basta citar la existencia del puente clásico. |
| Masas de retículos hermitianos y valores L | [Gan–Hanke–Yu, *On an exact mass formula of Shimura*](https://web.math.princeton.edu/~jonhanke/Web-02/Mass-Formula-of-Shimura/shimura-mass.pdf) da fórmulas exactas con factores locales. | La combinación con los momentos, el crecimiento de rango y una cuenta completa de medidas. |
| Crecimiento arquimediano, información finita y pendientes aritméticas | El método de pendientes tiene antecedentes sistemáticos; véase [Bost, *Evaluation maps, slopes, and algebraicity criteria*](https://ems.press/books/standalone/21/408). | La realización concreta mediante aplicaciones de Poincaré y cadenas theta, con el error sobre primos como cantidad residual. La semejanza con pendientes es conceptual, no una aplicación comprobada de un teorema de Bost. |
| Comparación automorfa entre formas unitarias | [Labesse, *Changement de base CM et séries discrètes*](https://webusers.imj-prg.fr/~michael.harris/CBCM.pdf) desarrolla cambio de base, estabilidad y multiplicidad bajo condiciones precisas. | La comparación exacta para los espacios y proyectores elegidos, o una prueba independiente válida. |

La búsqueda bibliográfica realizada identifica antecedentes, pero no es una búsqueda exhaustiva de prioridad. «No encontré un resultado idéntico» no certifica novedad.

### Qué sería una contribución específica si se valida

1. **Un teorema de segundo momento uniforme con constante principal uno.** P51 requiere crecimiento simultáneo del rango, peso, campo y nivel. Si se prueba con todos esos parámetros y con un error que tiende a cero, sería un resultado concreto que puede estudiarse sin mencionar RH. La revisión de P51/52 valida algunas reducciones, no el teorema completo.
2. **Una ley de divisibilidad multivariable con acción de Frobenius sobre las plazas CM.** El contenido distintivo sería la fórmula exacta de los exponentes y su control en cada primo, no sólo la existencia de divisibilidad de coeficientes theta.
3. **Un principio de covolumen con elección de twist dependiente de cada primo.** Debe explicar por qué varias realizaciones integrales controlan un mismo objeto global, cómo se suman sus pérdidas y por qué no se mezclan retículos incompatibles.
4. **Una cancelación demostrada entre esas dos leyes que deje una suma de primos reconocible.** Ésta es la conexión más importante para el objetivo RH. Una identidad formal entre símbolos no la prueba: exige que ambos lados midan las mismas formas, los mismos retículos, las mismas normas y el mismo rango de parámetros.
5. **Un tratamiento local integral fuera del rango de Fontaine–Laffaille.** Si los exponentes de cup products de P56 son correctos en toda la generalidad afirmada, sería una contribución independiente. Su validez se decide en la revisión de P56; no se puede inferir del éxito formal de la cadena.

Estos puntos son candidatos a resultados nuevos, no resultados que este informe declare establecidos.

### Un principio abstracto que sí se puede aislar

Hay una pieza elemental que hace visible el presupuesto de errores. Sea `V` un espacio hermitiano de dimensión `d`. Supongamos que se construyen `s` vectores linealmente independientes, con `s≥(1−ε)d`, cuya norma al cuadrado es a lo sumo

\[
\exp(H-mR+E_S).
\]

Por Hadamard, el logaritmo `c` de su determinante de Gram satisface

\[
c\le s(H-mR+E_S).
\]

Supongamos también una cota inferior, para esa misma familia y sus mismos datos integrales,

\[
c+2\delta\ge d(H-E_C).
\]

Entonces, por sustitución y reordenamiento exactos,

\[
s mR\le (s-d)H+sE_S+dE_C+2\delta.
\]

Ésta es una implicación algebraica comprobada. Es un modelo condicional; no certifica que las hipótesis automorfas del manuscrito se cumplan. Muestra tres aspectos que cualquier desarrollo debe conservar:

- `ε` debe ser pequeño respecto de la magnitud de `H`; omitir `(s−d)H` es ilegítimo, en particular si `H` puede ser negativo.
- El índice `δ` es una pérdida cuantitativa y no desaparece por llamar «integrales» a las formas después de una normalización.
- Una constante en la norma por cada lift, dimensión o plaza puede convertirse en un término grande después de tomar logaritmos y determinantes.

El lenguaje de «semistabilidad» debe usarse con precisión. La cota del manuscrito para familias de rango casi total no prueba automáticamente una desigualdad de pendientes para **todos** los subespacios y subretículos. Para obtener una teoría de pendientes completa hay que formular y demostrar esas propiedades adicionales.

### Programa que permite avanzar aunque la prueba de RH quede abierta

| Proyecto | Resultado concreto exigible | Prueba de éxito |
|---|---|---|
| Modelo CM de dimensión pequeña | Fórmula de divisibilidad para una theta y un primo inerte, con período y retículo fijados | Ejemplos exactos y demostración local que incluya todos los denominadores; separar primos ordinarios y supersingulares. |
| Un solo intercambio theta | Identidad de seesaw con medidas explícitas y constante calculada | Comprobar en un caso no nulo que ambos lados y sus cambios bajo twist coinciden. |
| Un solo determinante | Relación entre un Gram y valores L, con índices de saturación | Verificar tanto la igualdad compleja como la valoración en cada primo excepcional. |
| Segundo momento en rango fijo | Estimación con término principal exacto para una familia de niveles o pesos | Comparar la constante de masa, grado formal y covolumen antes de perseguir uniformidad total. |
| Paso a rango creciente | Teorema con funciones de error explícitas en todos los parámetros | Un libro de desigualdades que muestre que el margen final sigue siendo positivo en el rango requerido. |
| Twists locales a globales | Teorema abstracto que convierta una familia de condiciones locales en una cota de índice global | Finitud, compatibilidad de los retículos y sumabilidad de pérdidas demostradas, sin suponer una base común inexistente. |
| Formalización modular | Lemas sobre normas, Gram, productos locales y dominios de parámetros | Cada resultado final lleva un inventario de axiomas y de entradas analíticas; compilar una implicación condicional no equivale a probar sus hipótesis. |

Una presentación útil de ese programa sería «métodos de pendientes para retículos automorfos y divisibilidad theta». Es una **descripción propuesta de una línea de trabajo**, no el nombre de una nueva disciplina reconocida ni una afirmación de prioridad. Su valor se mediría por teoremas independientes reproducibles, ejemplos y aplicaciones adicionales.

### Atribución y frontera de lo demostrado

P57:833–843 atribuye a Levent Alpoge la matemática organizada por los tres teoremas y el camino al semiplano libre de ceros; atribuye a la serie su organización, nombres y escritura en papers. Este informe conserva esa atribución tal como la declara el propio autor. No verifica aquí la autoría externa ni la afirmación, también presente en ese pasaje, de que exista una prueba formal completa de GRH.

Por tanto, la contribución propia que puede describirse sin exceder la evidencia es la **arquitectura expositiva y el intento de compatibilizar un marco de Weil con esa ruta automorfa**. La prioridad de cada construcción adicional y la validez matemática del puente final requieren las revisiones particulares. Una conexión prometedora puede orientar investigación incluso cuando alguno de los teoremas que pretendía usar resulte incorrecto; para desarrollar esa conexión conviene reformular explícitamente el teorema fallido, conservar las piezas válidas y medir qué conclusión más débil permiten.


## Papers 43 44 y 45 Marco de Weil

La identificación radial de row C con la fórmula explícita tiene los signos y la normalización correctos. La familia de medidas de row B satisface sus leyes principales de composición y contacto. **No queda verificado íntegramente paper 43**, en particular su cálculo topológico de complejos de Hochschild. Estas conclusiones no validan la deducción automórfica de RH: el propio paper 46 excluye 43–45 de esa deducción.

### Paper 43

No hay un único teorema principal: la introducción contiene `introA`, `introH`, `introB`, `introC` y `introD`, además de resultados de completación y determinante. El dictamen global solicitado es **(c)**, no verificado íntegramente.

| Afirmación | Dictamen y alcance |
|---|---|
| Descomposición `A_S^×=Γ_S×ker φ`, identificación de `C_S` y sección homomorfa | **(a)**, `thm:split`, línea 777; normalizar cada valoración finita produce un representante único, y la sección preserva productos. |
| Convolución de objetos smeared | **(a)** para la identidad formal dada la definición; no prueba una teoría geométrica de intersecciones sobre Spec Z. |
| Cálculo de Hochschild `thm:shadow`, línea 2800 | **(c)**: falta verificar completamente la comparación continua del crossed product con el complejo de Koszul (`prop:crossed`), las contracciones locales y su compatibilidad con las tensorizaciones completadas. |
| Fórmula del símbolo en la componente radial | **(a)**: las integrales geométricas finitas y la identidad digamma dan el símbolo usado en 45. |
| Fórmula de todas las componentes, no degeneración, firma y completación | **(c)** en conjunto: no se ha completado la auditoría de los caracteres ramificados, los argumentos de densidad dual y todas las afirmaciones topológicas de completación. |
| Estabilización al aumentar S | **(a)**: `thm:chartcomp` y `thm:colimtrace`, 5242–5335, para el sistema de proyecciones definido en el texto. |
| Límites de rulings, determinante y pairing Riemann–Roch | **(c)** en conjunto; no fueron verificados todos sus resultados auxiliares. No hay aquí un dictamen de falsedad. |

El paso preciso pendiente en `thm:shadow(a)` está en las líneas 2841–2849: se aplica `prop:crossed` en la categoría de espacios completos con la acción temperada. Para validar este resultado hay que verificar continuidad y estimaciones de las aplicaciones de comparación y homotopías en los espacios efectivamente definidos; una equivalencia algebraica no basta. Se inspeccionaron `thm:excision-input` (1678) y `thm:kunneth` (1765): contienen argumentos, no son entradas asumidas sin prueba. No he demostrado que sus construcciones sean incorrectas, ni completado la auditoría de todas sus dependencias topológicas. Por eso el dictamen es (c), no (b).

Para la estabilización sí puede darse una comprobación directa. Un nuevo primo `ℓ` aporta

`(log ℓ) Σ(k≠0) ℓ^{−|k|/2} F(δ_S(ℓ^{−k}))`.

En las unidades, el integrando regularizado es cero porque la inflación es constante en la nueva coordenada. Si `log ℓ` supera el radio del soporte, cada término restante es cero. El límite es por tanto una estabilización eventual de valores, no una convergencia espectral de operadores ni una permuta ilimitada de series.

La relación con la literatura debe formularse por resultados. La distribución de Weil y su lectura como traza no son nuevas: [Connes](https://arxiv.org/abs/math/9811068) desarrolla la realización geométrica de la fórmula explícita; [Meyer](https://arxiv.org/abs/math/0312305) calcula homología de crossed products adélicos, con objetos que deben distinguirse del álgebra y los coeficientes torcidos de este paper. El cálculo torcido semilocal propuesto aquí no queda identificado automáticamente con el resultado de Meyer, pero tampoco se ha establecido su prioridad bibliográfica. **Novedad del paquete Hochschild exacto: (c)**. El texto reconoce la independencia lógica entre sus dos construcciones y que el vínculo de coinvariantes con la densidad local no es una identificación con homología de Hochschild (introducción, 140–151).

### Paper 44

Para los dos teoremas principales expresamente formulados como `introA` e `introB`, el dictamen es **(a)** en las hipótesis indicadas; no se extiende este dictamen automáticamente a cada resultado secundario del paper.

La definición crucial es `Frob_n=μ_(c_n K_P(n))`, con `P(n)⊂S_f` y Haar de probabilidad. Los representantes y soportes están calculados en 1153–1200. Como la convolución de dos Haar de cosets en este grupo abeliano es Haar del coset producto, y `P(mn)=P(m)∪P(n)`, se obtiene `Frob_m*Frob_n=Frob_mn`. El módulo constante `1/n` recupera n. La inversa de semigrupo conserva A y reemplaza r por `1/r`; el producto con el adjunto es `μ_KA`, no siempre la unidad. Así no se introducen inversas inexistentes.

El argumento de no interpolación continua (`rem:nointerp`, 1232–1260) también es correcto. Proyectar en un primo `p≠q` da una masa puntual en `1/q` al tiempo `log q`. Las raíces por convolución y continuidad obligan a masas puntuales para todos los tiempos. Un homomorfismo continuo desde el intervalo conectado al grupo totalmente disconexo `Z_p^×` es constante, y la ley obliga a que sea 1, contradicción.

Para el contacto (`thm:frobcontact`, 1441–1510), la condición de soporte elimina todas las capas salvo `p^k` si `n=p^k`. La densidad en esa capa es `p^{-k/2}` y su volumen local es `log p`, dando exactamente `Λ(n)n^{-1/2}h(1/n)`. Para n con dos factores primos no queda ninguna capa. En el lugar real, las coordenadas finitas de `j_infty(x)` son 1; por ello el indicador exige `s^N | n−1` en cada primo ajeno a P(n). Con Haar `dx/(2|x|)` y el soporte real positivo, el cambio `x=e^{-t}` da `1/(4sinh(t/2))`. Este factor es compatible con el enunciado, sin un factor 2 perdido.

La hipótesis `P(n)⊂S_f` está activa en toda la sección, desde 1149; no falta en el teorema aunque se remita a la definición. Tampoco se puede reemplazar el contacto de funciones por `T(Frob_n)` como valor sobre una medida: el propio texto explica la falta de extensión débil continua. La terminología Frobenius es una analogía de composición, no una realización de un endomorfismo de una curva.

**Novedad:** los coeficientes de contacto son los de Weil; no son nuevos. Las leyes de cosets son consecuencias de Haar y semigrupos inversos. Puede haber una presentación particular útil del semigrupo semilocal y sus obstrucciones, pero no se ha probado prioridad de esa formulación. Comparar con [Connes–Consani–Marcolli](https://arxiv.org/abs/math/0703392), donde ya se conecta la acción de clases de ideles con correspondencias y positividad.

### Paper 45

**(a)** para el teorema de comparación `thm:comparison` y la normalización radial solicitada; **(a)** para `thm:sufficiency`, el criterio primitivo usado por 46. No se certifican por esta conclusión todos los resultados posteriores sobre radicales.

El cambio de variable tiene una convención importante: `Γ_h(w)=h(−log|w|_S)`, de modo que `λ_−(Γ_h)=Φ_h(1)` y `λ_+(Γ_h)=Φ_h(0)` (523–525). Invertir esas etiquetas por sí solo es inocuo en el término simétrico, pero deben conservarse en las identidades individuales.

En `lem:radial-trace` (582–634), el término real es

`W_infty(Γ_h)=(γ+log(4π))h(0)+∫₀∞ [e^{−t/2}/(1−e^{−2t})][h(t)+h(−t)−2h(0)e^{−t/2}]dt`.

Para comprobar la constante, sustituir `u=2t` en el símbolo da

`J(τ)=ψ(1/2)−Re ψ(1/4+iτ/2)`.

Como `ψ(1/2)=−γ−2log2`, el resultado es `logπ−Re ψ(1/4+iτ/2)`, exactamente **−m(τ)** de paper 46. El núcleo K de 45 es la mitad del K de 46, pues el primero multiplica la suma `h(t)+h(−t)`; esto no es una discrepancia de normalización.

Revisé el argumento de contorno de `lem:contour` y `thm:EF` (772–981). La simetría transforma la integral en la recta −1 en el negativo de la de la recta 2, por eso aparece `1/(πi)`, no `1/(2πi)`. Al parametrizar la recta crítica, el factor 1/2 de la derivada logarítmica gamma devuelve `1/(2π)` en la integral real. El término de Euler aporta `−Λ(n)/sqrt(n)` por cada `h(±log n)`. Las alturas elegidas evitan los ceros y hacen desaparecer las aristas horizontales. El soporte compacto vuelve finita la suma prima.

Al restar los términos, se obtiene

`T_lim(Γ_h)=Φ_h(0)+Φ_h(1)−Σρ Φ_h(ρ)`.

El producto de Mellin para `F*G†` es `Φ_F(s) overline(Φ_G(1−bar s))`; así coinciden también la fórmula hermitiana y la fórmula real que importa 46. Añadir `c h(0)` altera efectivamente la fórmula: el valor c=0 depende de la normalización previamente elegida, no queda seleccionado por un principio geométrico independiente.

**Novedad:** es una verificación de compatibilidad de normalizaciones y una exposición de la fórmula explícita clásica; no una nueva fórmula explícita. Los antecedentes directos incluyen [Connes–Consani, apéndices B, C y E](https://arxiv.org/html/2006.13771), [Meyer, interpretación espectral](https://arxiv.org/abs/math/0412277) y [Burnol, términos locales y operador conductor](https://arxiv.org/abs/math/9902080). La construcción explícita de tests pares e impares puede tener valor expositivo, pero el mecanismo de interpolar ceros y amortiguar la cola se atribuye correctamente a Yoshida/Connes–Consani.

### Uniones de rows A B C con la forma de 46

| Unión | Comprobación |
|---|---|
| 43 `thm:chartcomp`, `thm:colimtrace` → 45 `prop:colimit` | **(a)** en el caso radial y en las restricciones de soporte indicadas. |
| 43 `lem:radialtrace` → 45 `lem:radial-trace` | **(a)**, inversión del perfil compensada por la simetría de las sumas y del núcleo. |
| 44 álgebra radial → 45 convolución y momentos | **(a)**, Haar del compacto normalizado a 1. |
| 45 `thm:EF`, `thm:comparison` → 46 `comparison`, `eq:W` | **(a)**, signo, `2π`, conjugación y término polar compatibles. |
| 45 `thm:sufficiency` → 46 `thm:all-support` | **(a)**; cada test construido cabe en alguna ventana, no necesariamente una fijada de antemano. |

No hay una unión demostrada entre una positividad geométrica de Hochschild y la positividad de `W_T`: 43 no afirma tal resultado y 46 no lo usa. Esa ausencia no es un error lógico de la cadena declarada; limita la interpretación de «llevar la prueba de Weil a Spec Z».


## Alcance de los registros Lean

**Dictamen (c): esta revisión no certifica la formalización completa ni la correspondencia entre ella y los papers.** Los registros locales son evidencia documental de una compilación reportada, no una compilación repetida durante esta auditoría.

Se leyeron `06-alpoge-verification/README.md`, `scripts/AxiomCheck.lean`, `source-metadata/Statements.lean`, `source-metadata/MainTheorems.lean` y `results/axioms.log`. El archivo `README-mio.md`, que aparecía sin seguimiento de Git al empezar, no fue modificado ni utilizado.

El log contiene `riemannHypothesis : RiemannHypothesis` y reporta únicamente `propext`, `Classical.choice` y `Quot.sound` para cinco teoremas principales. El script de chequeo efectivamente pide `#print axioms` sobre esos nombres. `Statements.lean` expresa ceros de zeta excluyendo enteros negativos pares, un semiplano sin ceros para caracteres de Dirichlet salvo el polo, y ceros de L en la franja abierta. Esas fórmulas tienen el alcance que sus nombres sugieren al nivel de las expresiones visibles.

Esto no establece todavía:

1. Que las definiciones transitivas de zeta, L y `RiemannHypothesis` del entorno compilado sean exactamente las esperadas; `Statements.lean` importa Mathlib y no contiene todo ese entorno.
2. Que el log corresponda a la totalidad del árbol fuente y a los binarios cuya cadena de confianza se pretende verificar.
3. Que cada enunciado humano de 49–56 sea traducción fiel de una declaración formal, con las mismas constantes e hipótesis.
4. Que una prueba formal del resultado final valide automáticamente una prueba en prosa diferente del mismo resultado.

El README describe un archivo de aproximadamente 175.000 módulos y una compilación de gran escala. No se descargó ni reconstruyó ese archivo en esta tarea. Tampoco se ejecutaron `lake build` o un kernel independiente. Por ello no se informa «Lean verificado» como resultado de este trabajo.

La siguiente comprobación útil sería un mapa bidireccional entre los enunciados centrales de cada paper y declaraciones Lean exactas, incluyendo sus definiciones y el árbol transitivo de dependencias. Esta tarea es distinta de revisar los logs y distinta de auditar las pruebas humanas, que fue el encargo principal.

