# Revisión de 49, 50, 53 y 54: theta, Hecke y covolumen

Fecha: 2026-11-28. Fuente: `main.tex` de la copia local, no los papers 47–48. Las referencias de líneas son las del archivo fuente. No representa la opinión de los investigadores mencionados por el usuario.

> **Actualización de la auditoría profunda:** este archivo conserva el dictamen PRELIMINAR. Sus pendientes no son el estado final. Véase [THETA.md](auditoria-profunda/THETA.md), con pruebas y obligaciones incrementales. Allí se cerró la instanciación aritmética de P50 (HE01), se reconstruyeron la constante CM exacta, la divisibilidad de P49 en todos los primos, la cota alcanzada de P54 y la fórmula de norma de rango uno. Se corroboró además un fallo concreto de caracteres en P53 `pcu:product`, líneas 3351–3360, y un fallo funcional en la acotación Hilbert de los slices. El error de caracteres y su impacto se documentan en [ERROR-53-CARACTERES.md](auditoria-profunda/ERROR-53-CARACTERES.md). Las reconstrucciones no certifican cada línea literal ni GRH; THETA precisa las reparaciones menores y las obligaciones de normalización aún no cotejadas.

## Alcance y dictamen preliminares

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

En la revisión preliminar no se había identificado un contraejemplo que justificara (b). Este punto quedó superado por los fallos de P53 documentados en la actualización anterior; las tablas siguientes se conservan como registro de la primera etapa.

## 50: comprobaciones matemáticas

Archivo: `04-papers/50-elementary-divisors-edge-hecke-operator/main.tex`.

### El enunciado realmente demostrado

Líneas 335–409, `ph:thm`. El anillo es un dominio de valoración de característica cero, con (w^2=p), y el ciclo tiene (N\ge2) par, (P=p^e\ge5), (q=P^N). Se exige la condición de libertad de las aristas `ph:eq-free`. El resultado controla la colongitud **truncada** por (p^j\Lambda):

\[
\operatorname{col}(\Lambda,Y\Lambda+p^j\Lambda)\mid p^l,
\quad l\le (3c_d+\theta j)|X||H||\mathcal B|.
\]

La paráfrasis «media de divisores elementales pequeña» debe conservar la fracción excepcional (\theta) y la truncación. No es una cota uniforme independiente de (j) para todos los divisores elementales, ni asegura por sí misma que (Y) sea invertible. Esto es una precisión de interpretación, no un fallo del teorema impreso.

### Álgebra de la deducción

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

### Los tres inputs

**Root** (`pe:root`, líneas 925–1025). La sustitución construye un polinomio (\bar\Phi) sobre (R/w^{\lambda+1}R) de grado (q\nu'), con coeficiente principal no nulo. Para cada representante de (\mathbb F_q) lo divide una potencia ((t-a_r)^\nu). Las diferencias (a_r-a_{r'}) son unidades; por tanto estos factores son comaximales y su producto mónico divide (\bar\Phi). El argumento de grados sigue siendo válido aunque el anillo cociente tenga divisores de cero, precisamente porque el divisor es mónico. Se concluye (\nu\le\nu'). No hace falta introducir una hipótesis de cuerpo en este paso.

**Count** (`pe:count`, líneas 1230–1251). El punto delicado es el volumen de `pe:vol`, líneas 1120–1171, que usa intercalación, el jacobiano (P^{kN}\Delta(\sigma)), y el producto de Euler. El factor obtenido es

\[
\prod_{l=1}^k\frac{q-1}{q^l-1}=[G:I]^{-1}.
\]

La construcción de empaquetado en `pe:flag` transforma el conteo de monomios de grado fijo en un volumen de dimensión (kN), usando un espesor de tamaño uno; no se está comparando directamente un conjunto de volumen cero con su número de puntos. La hipótesis (24Nk^2cP^{2r}\le\theta n) implica (x\le\theta/2\le1/2), de donde (e^x\le1+2x\le1+\theta).

**Averaging** (`pe:avg` y `pe:av`, líneas 1259–1328 y 1430–1500). El promedio se construye algebraicamente mediante trazas, no dividiendo por el orden de un grupo finito que pudiera ser no unidad. En (S1), el límite (d+k\le q) es suficiente: una forma homogénea de grado entre 2 y (q) no desaparece al reducir módulo (X_v^q-X_v); los monomios de grado (q) que se reducen a grado 1 no cancelan con términos de grado 1 de la misma forma homogénea. El submódulo (U^+) es finitamente generado porque el álgebra (\mathcal S_d) es imagen de un módulo finito libre y hay finitos vectores iniciales. Así, su uso como módulo libre en la traza es lícito sobre un dominio de valoración. Las estimaciones de pesos en `pe:wd` conservan el error (2c), suficiente para el umbral (c^*=3kc).

### Rango interno y aplicación a 49

Líneas 1505–1517 verifican explícitamente, desde `ph:eq-large`, las condiciones de `count`, `av` y `near`. En particular

\[
P^{N/2}=\sqrt q\ge n^2>Nk(N/2+2)n+n+k,
\quad 24Nk^2(5Nc_0)P^{2r}\le\theta n.
\]

La aplicación de líneas 1519–1531 usa (n=a=xb), (r=\lceil\log_pm\rceil), (P=p^{o_0}), (N=o/o_0), (\theta=(m^2f)^{-1}). Sus dos verificaciones son (q\ge a^4) y ((Nk\log q/\theta)^5P^{3r}\le b\le a). La conclusión (3c_d\le12A_{\mathfrak l}/(mp)) tiene el factor correcto porque (A_{\mathfrak l}=aN/2).

La parte aritmética de líneas 767–831 usa, además, aproximación débil, libertad de (J), la identificación de todos los factores de la representación y la paridad de los lugares del ciclo. He leído esa reducción y no encontrado una contradicción; no he certificado aquí los antecedentes de 49 que proporcionan estos datos. Por eso la pregunta sobre **todas** las aplicaciones posteriores conserva (c).

## 49: ubicación precisa de lo pendiente

Archivo: `04-papers/49-short-forms-theorem-theta-lifts-complex-multiplication/main.tex`.

**Seesaw.** El resultado de 46 `au:seesaw` permite que el dato de cadena (\Psi) dependa del twist, pero no (c_{\rm ss}). Tampoco afirma no nulidad de los dos lados. En 49, `ps:onestep` (3983 ss.) reduce la transferencia a una única órbita; las etapas (3), (5), (6) se remiten expresamente a `pk:vanish`, `pk:coarse`, `pk:fine`. No sería legítimo señalar esas remisiones como huecos sin comprobar sus destinos. Falta en esta revisión verificar esos destinos, la convergencia absoluta al intercambiar integrales y sumas y el ensamblaje que mantiene el escalar independiente del twist.

**Constante CS.** En `ps:conj` (3845), la exigencia es exactamente (|t_\sigma|^2=\Omega^{-1}). `pk:conj` (5433) usa (t_\sigma=\sigma(\varpi_{\rm vac}/\mathsf u)c_\psi/\Omega_\sigma). La prueba de (C4), líneas 5304–5340, no se limita a citar una igualdad «hasta un algebraico»: construye (\mathsf u^{12h}=\prod_i\mu_i^{12}\Delta(\Lambda_i)) y afirma la identidad exacta de áreas. Comprobé la combinación de factores mostrada: de (\operatorname{area}|\Delta|^{1/6}=4\pi^2\operatorname{Im}\tau|\eta|^4) y del promedio (c_{CS}-\log(2\sqrt d)) resulta (2\pi^2e^{c_{CS}}/\sqrt d), como está escrito. No comprobé contra el texto íntegro de Chowla–Selberg la fórmula de partida, ni todos los transportes de diferenciales, la unidad en 2 (`pf:CS`, 6911), y la reciprocidad `pf:recip` (7111). Por ello no certifico la constante exacta final.

**Divisibilidad.** `pa:count` (2522) distingue expresamente el primo ramificado (p=d), con deducción adicional (\frac12\sum_\tau\mathrm{ded}_0(\tau)), y limita los jets a las columnas anidadas de Schur. La sustitución por nuevas direcciones de 2557 ss. da el factor (\varpi^B\prod\det(g_{\tau,h})^{\kappa_\tau(h)}); las tres clases de congruencias (a)–(c) cubren las parejas de alturas (h=1), (h\ge2,h'=1), (h,h'\ge2). Este control combinatorio no prueba por sí solo que el kernel real tenga la forma normal requerida. Quedan por verificar `pa:kernel`, el tratamiento de 2 y de los primos del nivel, y `pl:level`. El nivel (N) se trata aparte en `pa:level` (3169): no debe confundirse con una aplicación del teorema de Hecke de 50.

## 53–54: qué queda comprobado y qué no

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

## Uniones revisadas

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

## Literatura y novedad

La identidad de Chowla–Selberg es previa: [Chowla–Selberg, *On Epstein’s Zeta-function* (1967)](https://doi.org/10.1515/crll.1967.227.86). La teoría general de Siegel–Weil regularizada y Rallis también es previa: [Gan–Qiu–Takeda, arXiv:1207.4709](https://arxiv.org/abs/1207.4709). Estas fuentes localizadas corroboran antecedentes y no certifican las normalizaciones particulares de estos manuscritos.

El candidato más delimitado a una contribución autónoma en el bloque revisado es el teorema de 50: un promedio integral compatible con un ciclo de Frobenius y un conteo de defectos que controlan colongitudes de operadores de aristas. La conexión propuesta en 49 y 54 entre períodos CM exactos, jets integrales en todos los primos y cotas de determinantes es una arquitectura de investigación concreta. Su novedad bibliográfica y su validez global no están establecidas por esta revisión. No hay fundamento aquí para afirmar que ya se creó un campo nuevo o que esa arquitectura demuestra RH.

## Matriz solicitada de los inputs de 46

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

## Segunda revisión crítica del alcance de (a) en 50

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
