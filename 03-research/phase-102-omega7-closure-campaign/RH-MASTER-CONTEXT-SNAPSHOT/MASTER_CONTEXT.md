# Contexto maestro del programa hacia RH

## Dictamen ejecutivo

La revisión completa no encuentra una demostración de RH ni una cadena incondicional que cierre \(\Omega_7\). Sí encuentra una columna matemática sólida, un banco importante de identidades finitas y no-go específicos, y una frontera mucho más estrecha que al comienzo del programa.

La columna defendible es

\[
\mathrm{RH}
\Longleftrightarrow
\{\text{todos los ceros de }\Xi\text{ son reales}\}
\Longleftrightarrow
\mathrm{ARP\!\!-P}
\Longleftrightarrow
\{J_N(z_0)\succeq0\text{ para todo }N\}
\Longleftrightarrow
\{\lambda_n\ge0\text{ para todo }n\}.
\]

Esta cadena localiza la dificultad; no la disminuye. Varias flechas son equivalencias de familias completas obtenidas pasando por RH, no transformaciones positivas nivel a nivel. Por eso un certificado para un corte finito, una malla o un intervalo no se propaga automáticamente a todos los índices.

La afirmación de que \(\Omega_1\)–\(\Omega_6\) están cerrados requiere una precisión decisiva. \(\Omega_1\), \(\Omega_2\), \(\Omega_3\) y \(\Omega_6\) sobreviven como equivalencias globales en los términos auditados. \(\Omega_4\) mezcla dos blanqueamientos con dominios distintos. \(\Omega_5\) demuestra continuidad al borde para cada \(N\) fijo, pero no produce la positividad interior uniforme necesaria. El único objetivo terminal sigue siendo \(\Omega_7\), aunque no todas las piezas auxiliares del trayecto constructivo están demostradas.

La corrección más útil para el reinicio es

\[
\lambda_n
=
\lambda_n^{\rm arch}+\lambda_n^{\rm prime}
\ge0
\quad\Longleftrightarrow\quad
\lambda_n^{\rm prime}\ge-\lambda_n^{\rm arch}.
\]

Paper 36 presenta en distintos lugares la dominación

\[
|\lambda_n^{\rm prime}|<\lambda_n^{\rm arch}
\]

como si fuera la desigualdad exacta de \(\Omega_7\). No lo es. Es una condición suficiente más fuerte cuando la parte arquimediana es positiva y falla ya como supuesta equivalencia para \(n=1\):

\[
\lambda_1^{\rm arch}
=1-\frac\gamma2-\log2-\frac12\log\pi
\approx-0.55412,
\qquad
\lambda_1^{\rm prime}=\gamma\approx0.57722,
\]

mientras \(\lambda_1\approx0.02310>0\). Esto no hace fácil \(\Omega_7\): por H0, demostrar la cota unilateral para todos los índices sigue teniendo fuerza-RH. Sí demuestra que los no-go obtenidos mediante valores absolutos no clausuran toda ruta aritmética. Para los índices donde \(\lambda_n^{\rm arch}\ge0\), el blanco se reduce a controlar la excursión negativa de la parte prima; para los índices donde \(\lambda_n^{\rm arch}<0\), debe conservarse el lower bound completo, que exige una contribución prima positiva suficiente.

La auditoría encuentra una segunda corrección en la misma ruta. Para

\[
f_{n,\varepsilon}(y)=y^{-1-\varepsilon}L_{n-1}^{(1)}(\log y),
\]

la integración por partes correcta es

\[
\lambda_n^{\rm prime}
=
\lim_{\varepsilon\downarrow0}
\int_1^\infty(\psi(y)-y+1)f'_{n,\varepsilon}(y)\,dy
=
\lim_{\varepsilon\downarrow0}
\left[-n+
\int_1^\infty(\psi(y)-y)f'_{n,\varepsilon}(y)\,dy\right].
\]

Paper 36 imprime el negativo de la integral con \(\psi-y\) y omite \(-n\). La representación regularizada polo–primos anterior sigue siendo utilizable; la fórmula de integración por partes y toda conclusión firmada derivada de ella deben corregirse.

## Qué representa realmente paper 36

El aporte estructural principal es la equivalencia

\[
\mathrm{ARP\!\!-P}\Longleftrightarrow\mathrm{RH}.
\]

El sentido ARP-P \(\Rightarrow\) RH usa interpolación Pick–Nevanlinna, normalidad, continuación analítica y detección de residuos no reales. El sentido RH \(\Rightarrow\) ARP-P convierte cada canal en una transformada de Cauchy de una medida positiva. La arquitectura es matemáticamente significativa porque serializa el problema en positividad de matrices finitas, pero Step 5 exige esa positividad para toda fuente y todo conjunto de nodos; ése es el input abierto.

La auditoría de la jerarquía H0–H8 deja:

| Nivel | Estado vinculante | Carga exacta |
|---|---|---|
| H0 | **DEMOSTRADO** | Conservación lógica de dificultad; no identifica por sí solo dónde está toda la fuerza. |
| H1 | **DEMOSTRADO en el caso escalar declarado** | No cubre automáticamente los canales matriciales complejos. |
| H2 | **PARCIAL** | Gershgorin cierra nodos altos y separados; compactitud más diagonal positiva no implica PSD a altura acotada. |
| H3 | **PARCIAL** | Región logarítmica y resultado casi en todo punto; no la desigualdad global de dos nodos. |
| H4 | **DEMOSTRADO como serialización** | La secuencia de determinantes caracteriza RH; no se demuestra su signo. |
| H5 | **DEMOSTRADO como equivalencia** | Ventanas positivas y ARP-P son coordenadas de la misma condición. |
| H6 | **CUALITATIVO; cuantitativo abierto** | La contraposición da algún testigo finito. La construcción explícita no domina la cola y pierde un factor \(|\kappa|\). |
| H7 | **PARCIAL** | SOS bajo RH y cierres en cajas o bandas fijas; no SOS aritmético global. |
| H8 | **PARCIAL** | Positividad a \(N\) fijo y traslación alta; falta uniformidad en \(N\) a altura fija. |

También deben retirarse o rebajarse cuatro piezas:

1. La suma aislada \(\sum_\rho(1-1/\rho)^n\) no converge, aun bajo RH; sólo la combinación simétrica que define \(\lambda_n\) es legítima.
2. Muestreo, saturación factorial y cascada de de Bruijn–Newman dependen de estimaciones uniformes todavía abiertas.
3. La realización operatorial requiere auto-adjuntez, control uniforme de fuentes e identificación de resolventes no construida dentro del manuscrito.
4. La integración por partes del kernel Laguerre tiene signo y término de borde incorrectos.
5. La asintótica de envolvente omite el término lineal \(\frac{\gamma-1}{2}n\), y la cota \(c\sqrt n\log n\) no puede incluir \(n=1\).
6. El cierre Castelnuovo/Minkowski aplica una hipótesis formulada para norma positiva a una clase obtenida con norma negativa.

Estas correcciones no destruyen la equivalencia ARP-P–RH. Impiden usar resultados auxiliares más fuertes que lo realmente probado.

## Recorrido comprimido de los nueve programas

### RH1–RH3: coeficientes, clases \(\omega\) y estadística

Se construyeron sumas de Dirichlet, descomposiciones por número de factores primos, coherencias, extremos, clasificadores y protocolos de precisión. Sobrevive la identidad de energía

\[
\left|\sum_kS_k\right|^2
=
\sum_k|S_k|^2+
\sum_{j\ne k}\Re(S_j\overline{S_k}),
\]

pero no su lectura como criterio de ceros. Liouville y controles multiplicativos aleatorios muestran que multiplicatividad, decoherencia pequeña o una ley de extremos no determinan la geometría del divisor. El puente desde un cero fuera de línea a una pendiente concreta del observable truncado tampoco fue demostrado y no apareció en el control operativo.

### RH4–RH6: matrices de picos y Weil localizado

Las covarianzas de clases responden principalmente a masa de coeficientes, conductor, soporte y selección de picos. Se retiraron la predominancia de covarianza negativa y la excepcionalidad causal de \(\omega=2\). Una Gram construida sólo con ceros es PSD por construcción y puede haber eliminado la coordenada horizontal que debía detectar.

El detector Hermite–Gauss de Weil sí deja álgebra finita y calibraciones útiles. Falta una cota conjunta uniforme en dimensión, centro, ancho, corte primo, cola de ceros y normalización. Las respuestas lineal y cuadrática observadas pertenecen a montajes distintos o exponen una especificación inconsistente; no constituyen una ley universal.

### RH7–RH8: detector calibrado, transferencia ausente

La expansión de un cuarteto perturbado y varios controles de traza son correctos para secciones fijadas. Las mallas H1/H2 y los autovalores mínimos son evidencia numérica. El paso

\[
Q_{J,\sigma,X,H}\longrightarrow Q_\infty
\]

con uniformidad simultánea es precisamente el paso capaz de excluir todo cero fuera de línea. No puede tratarse como una extrapolación rutinaria.

### RH9: geometría postulada, no construida

El programa especifica qué debería entregar una geometría útil: objeto global, diagonal, cohomología, lector espectral, triple de Lefschetz y polarización independiente. Arakelov, dinámica de escala, geometría no conmutativa, prolate/Sonin y teorías cohomológicas aportan analogías o piezas. El corpus no construye el objeto conjunto ni identifica su forma de intersección con Weil sin insertar previamente el divisor.

## Recorrido comprimido de las fases

Las fases no son más de cien cierres acumulativos. Son una genealogía con bifurcaciones, correcciones y reparametrizaciones. El arco útil es

\[
\begin{aligned}
&\text{Weil localizado y detector}
\to\text{paredes de signo}
\to\text{Hodge e índice}\\
&\to\text{Connes/CCM}
\to\text{Feshbach--Cauchy--adjugado}
\to\text{LP+IDENT}\\
&\to\text{RDI-ANCHOR}
\to\text{corriente y divisor}
\to\boxed{\text{identificación aritmética firmada abierta}}.
\end{aligned}
\]

### Fases 0–25

Se fija la forma completa de Weil, se prueban varias paredes de signo y se ensayan realizaciones de Kreĭn, calor, Carleson, de Branges y Hodge. Los resultados durables son detectores, identidades y no-go acotados. La geometría global y su polarización no se construyen. Los argumentos con número finito de defectos dependen de una hipótesis de finitud que el complemento de RH no tiene por qué satisfacer.

### Fases 26–50

CCM, momentos, de Bruijn–Newman, Selberg, Pontryagin y Hodge convierten promedios y defectos en condiciones parciales. La lección común es

\[
\text{promedio pequeño o subsucesión convergente}
\not\Rightarrow
\text{ausencia de un átomo o alineación de cada cero}.
\]

Los intentos fase→inercia prueban no-go para clases locales o tauberianas. No prueban que toda entrada diofántica no local sea imposible.

### Fases 51–75

Homotopía, Stone, métricas, GLT e índices formales no producen la flecha aritmética. Las fases 64–71 reconocen que aproximantes con ceros reales convergentes a \(\Xi\) resolverían RH por Hurwitz; esa convergencia tiene fuerza-RH. El rótulo QED de fase 65 queda superado por correcciones posteriores.

Las fases 72–75 entregan una infraestructura algebraica valiosa:

\[
\text{Feshbach}
\to\text{corriente}
\to\text{Cauchy}
\to\text{divisibilidad}
\to\text{adjugado}.
\]

Los terminales `PW-Cauchy`, `HPR-DIV`, `EG_LOCK` y `ADJ-ARITH-LOCK` son representaciones de la misma cancelación firmada, no cuatro cierres distintos.

### Fases 76–79

Aquí se separan `SAFE-LIMIT-POINT = LP + IDENT`, el problema LP se corrige a `BTG-DIV` en el verdadero \(\mu_L\), y `GAP-Z` se descompone exactamente como

\[
g_{N+2}-g_N=\mathrm{ZERO}+\mathrm{MESH}+\mathrm{BND}.
\]

Las cotas de MESH y BND están demostradas; ZERO sigue abierto y no puede acotarse sumando magnitudes de shells. Outcome A usa secciones finitas y \(\mu_{\rm ref}\), no el objeto límite en \(\mu_L\), de modo que la neutralidad de LP no está certificada.

E79.6 y los discriminantes de nube son numéricos o conjeturales. Varias firmas fueron retractadas por controles de precisión, cambio de definición o pérdida de poder discriminante. No está demostrado que `DISCRIMINANT` sea necesario, suficiente ni el único portador de fuerza-RH.

### Fases 80–101

Se prueban identidades seculares, Euler–Möbius, Abel, Feshbach de capa, determinantes bordeados, cofactores, Jacobianos, conmutadores y corrientes. Todas son coordenadas exactas útiles. Las rutas vuelven a

\[
\mathrm{RDI\!-\!ANCHOR}
\sim
\mathrm{DIRECT\!-\!BORDERED\!-\!ANCHOR}
\sim
\mathrm{LOCAL\!-\!COVARIANT\!-\!IDENT}
\sim
\mathrm{STIELTJES\!-\!IDENT}.
\]

Identificar `C_core` en un intervalo seguro ya fuerza RH por propagación Pick–Nevanlinna. `TRUE-DIVISOR-IDENT` es todavía más fuerte porque preserva soporte y multiplicidad. Las fases 94–100 cambian la representación de la carga; no la demuestran.

## Banco de resultados que sí puede reutilizarse

1. La equivalencia ARP-P–RH y la serialización escalar por jets en un punto regular.
2. El diccionario de Cayley \(w=1-1/\rho\) y el criterio completo de Li.
3. Identidades finitas de Weil localizado, Cauchy, Pick, Feshbach, shorting, adjugados, cofactores, Jacobianos, conmutadores y Abel, conservando sus dominios.
4. La descomposición exacta de GAP-Z con MESH y BND controlados.
5. En \(\Re s>1\), el producto Euler–Gamma, su derivada logarítmica y las identidades Laguerre donde la convergencia absoluta está justificada.
6. Detectores y falsadores numéricos con precisión, normalización, catálogos, trazas y semillas fijados.
7. No-go específicos: Gram cero-sólo, multiplicatividad como criterio, extrapolación finita, pseudoinversa en curva singular, matching por celdas, un nivel de momentos, productos de trazas y geometría meramente postulada.
8. La distinción indispensable entre convergencia, identificación y positividad.

## Registro mínimo de rutas que no deben repetirse

| Ruta | Razón de cierre o cuarentena |
|---|---|
| Multiplicatividad, \(\omega\), GEV, clasificadores | Controles multiplicativos y dependencia de ventana rompen la inferencia a ceros. |
| Gram o Mercer construido desde ceros | PSD tautológica; no detecta horizontalidad. |
| Li o Weil en cortes finitos | No cuantifica sobre índices o tests futuros. |
| Truncación prima positiva | El signo surge de cancelación global; las secciones finitas pueden ser negativas. |
| Cota punto a punto con valores absolutos | Pierde la fase Laguerre; no descarta el nuevo blanco unilateral. |
| Región libre o densidad de ceros | Admite al menos un cero fuera de línea, suficiente para destruir Li en índices grandes. |
| Fejér–Riesz | La no negatividad del símbolo requerida es la conclusión. |
| Kreĭn abstracto | La existencia de alguna extensión positiva no identifica el kernel aritmético. |
| Recurrencia de todas las fases | El costo de Kronecker de la formulación ensayada supera la ganancia geométrica. |
| Calor, de Branges, Herglotz, LP | En las versiones útiles reaparece real-rootedness o una condición equivalente. |
| Hodge/Lefschetz sin objeto externo | Postula la polarización que debe demostrarse. |
| Prolate o gap único | No identifica el estado base ni excluye índice negativo sin una cota equivalente a Weil. |
| Promedio, smoothing, momentos de un nivel | Pierde soporte transversal o un cero individual. |
| Nueva coordenada de RDI | No cuenta como cierre sin una identidad o desigualdad nueva. |

## Frontera matemática real

Hay un objetivo terminal y varias obligaciones internas de una ruta concreta. No deben confundirse.

| Obligación | Estado | Papel |
|---|---|---|
| \(\lambda_n\ge0\) para todo \(n\) | **ABIERTO / FUERZA-RH** | Objetivo terminal exacto. |
| \(\lambda_n^{\rm prime}\ge-\lambda_n^{\rm arch}\) | **ABIERTO / FUERZA-RH** | Forma aritmética unilateral mínima del mismo objetivo. |
| `BTG-DIV` en el verdadero \(\mu_L\) | **ABIERTO** | Obligación LP; no está probada neutralidad respecto del control fuera de línea. |
| Interfaz LP libre de \(\mu_L\) fijado | **ABIERTO** | Reparación necesaria para la formulación build-neutral. |
| `GAP-Z`, término ZERO | **ABIERTO** | Convergencia firmada; MESH y BND no la resuelven. |
| `RDI-ANCHOR` o `C_core` identificado | **ABIERTO / FUERZA-RH** | Identificación Euler–Gamma de la ruta reciente. |
| `RDP-SHELL`, PROLATE y WEIL-TAIL | **ABIERTO** | Puentes downstream; no deben atacarse antes del núcleo. |
| Geometría externa con polarización | **NO CONSTRUIDA** | Alternativa conceptual, no infraestructura disponible. |

H0 permite concluir que toda cadena suficiente contiene al menos un paso falso o de fuerza-RH. No permite concluir que contiene exactamente uno mientras las demás obligaciones sigan abiertas. Por eso la hipótesis “DISCRIMINANT es el único hito y GAP-Z es neutral” no está demostrada. `RDI-ANCHOR` es claramente de fuerza-RH; LP y GAP-Z todavía no han sido clasificados en el objeto límite correcto.

## Reinicio recomendado

### Primer carril: Li unilateral y cancelación firmada

Fijar primero, sin abreviaturas internas, la definición regularizada mediante el límite pareado

\[
\lambda_n^{\rm prime}
=
\lim_{\varepsilon\downarrow0}
\left[
\sum_{k=1}^n
\binom nk\frac{(-1)^{k-1}}{\varepsilon^k}
-
\sum_{m\ge2}\frac{\Lambda(m)}{m^{1+\varepsilon}}
L_{n-1}^{(1)}(\log m)
\right]
\]

y todos los términos de polo, Gamma y borde. En el borde la serie desnuda no es absolutamente convergente; ninguna manipulación puede separar los términos que producen la continuación finita.

El mecanismo buscado debe conservar el signo antes de estimar. Escribiendo \(f_{n,\varepsilon}(y)=y^{-1-\varepsilon}L_{n-1}^{(1)}(\log y)\), la identidad de partida corregida es

\[
\lambda_n^{\rm prime}
=
\lim_{\varepsilon\downarrow0}
\int_1^\infty(\psi(y)-y+1)f'_{n,\varepsilon}(y)\,dy
\]

seguido del lower bound exacto

\[
\lim_{\varepsilon\downarrow0}
\int_1^\infty(\psi(y)-y+1)f'_{n,\varepsilon}(y)\,dy
\ge-\lambda_n^{\rm arch}.
\]

Cuando \(\lambda_n^{\rm arch}\ge0\), esto equivale a acotar la parte negativa por \(\lambda_n^{\rm arch}\). Para este split, la fórmula exacta de la parte arquimediana y su convexidad discreta dan

\[
I_-:=\{n\ge1:\lambda_n^{\rm arch}<0\}=\{1,2,\ldots,7\}.
\]

La certificación usa

\[
\lambda_n^{\rm arch}
=1-\frac n2(\gamma+\log(4\pi))
+\sum_{r\ {\rm impar}}
\left[\left(1-\frac1r\right)^n-1+\frac nr\right]
\]

y, para \(d_n=\lambda_{n+1}^{\rm arch}-\lambda_n^{\rm arch}\),

\[
d_{n+1}-d_n
=\sum_{r\ {\rm impar}}\frac{(1-1/r)^n}{r^2}>0.
\]

Las evaluaciones por intervalos \(d_3\in(0.0062,0.0063)\), \(\lambda_7^{\rm arch}\in(-0.356,-0.355)\) y \(\lambda_8^{\rm arch}\in(0.020,0.022)\), junto con los valores negativos directos de \(n=1,2\), fijan el conjunto. En esos siete índices hay que verificar el lower bound completo y no se puede descartar la excursión prima positiva. No sirve sustituir la desigualdad por

\[
\lim_{\varepsilon\downarrow0}
\int_1^\infty|\psi(y)-y+1|\,|f'_{n,\varepsilon}(y)|\,dy,
\]

porque eso vuelve a una cota simétrica de fuerza-RH ya explorada. Tres clases candidatas actualmente identificadas, sin pretensión de exhaustividad, son una involución global entre celdas primas, una identidad de compensación polo–Gamma–primos o un principio variacional aritmético de una sola cara.

### Segundo carril: triage de LP y GAP-Z

Este carril debe ser corto. Para LP se necesita un teorema abstracto o un contraejemplo en una clase que contenga tanto la construcción zeta como un control fuera de línea y que concluya en el verdadero \(\mu_L\). Para GAP-Z se debe decidir si ZERO se controla con axiomas compartidos por ambos builds o si requiere ya una identidad Euler específica. No se autoriza otra campaña de proxies.

Los resultados posibles son suficientes para decidir inversión:

1. teorema build-neutral: la pieza queda como infraestructura;
2. contraejemplo: la formulación se retira;
3. necesidad de una propiedad aritmética separadora: la fuerza está repartida y cae la atribución exclusiva a IDENT.

### Tercer carril: RDI sólo si aparece un mecanismo

Si la ruta reciente sigue siendo necesaria, se congela una sola coordenada, preferentemente `C_core`, con orden de límites y fuente Gamma–Euler explícitos. No se desarrollan más equivalentes de `RDI-ANCHOR`. Una nueva formulación cuenta sólo si produce una estimación que la anterior no tenía. El control fuera de línea sólo es deductivo cuando pertenece a una clase de objetos completados con coeficientes, factor Gamma, ecuación funcional y regularización comparables; un cuarteto insertado a mano es sólo una prueba del detector del lado de ceros.

### Puerta bibliográfica y falsación

Antes de llamar nueva a una idea se debe escribir el enunciado sin vocabulario del repositorio, buscar por fórmula y mecanismo en fuentes primarias, y comparar hipótesis y conclusión. Esta auditoría es interna; no certifica prioridad bibliográfica.

Antes de abrir otra fase, un candidato debe:

1. fallar estructuralmente en un control aritmético fuera de línea perteneciente a una clase definida; si sólo existe un cuarteto plantado, superar esa prueba se registra como falsación heurística;
2. ser compatible con un control sobre la línea sin usar sus ceros;
3. preservar conjugación, soporte transversal y multiplicidad lineal;
4. declarar el orden de todos los límites;
5. no usar positividad de Weil, real-rootedness, un divisor ya real o una métrica adaptada;
6. aportar una identidad o desigualdad nueva, no otro proxy o cambio de coordenada.

## Criterio de avance para el próximo ciclo

No se abre una fase por cantidad de cálculos. Se abre cuando existe un nuevo grado de libertad matemático y al menos una de estas salidas:

- un lema firmado candidato con hipótesis aritméticas verificables;
- un contraejemplo que retire una obligación abierta;
- una reducción estricta que elimine una obligación sin sustituirla por un equivalente;
- una prueba build-neutral de LP o GAP-Z en el objeto límite correcto;
- una construcción geométrica externa con diagonal y polarización independientes.

Hasta entonces, el trabajo pertenece al dossier de planificación. La prioridad inmediata es reparar el blanco de paper 36 y someter la ruta unilateral a la puerta bibliográfica. Después se decide si merece desarrollo matemático o si también cae bajo un no-go ya conocido.

## Navegación

- [`PAPER36_AUDIT.md`](PAPER36_AUDIT.md): auditoría detallada de la columna del manuscrito.
- [`RH1_RH9_AUDIT.md`](RH1_RH9_AUDIT.md): balance de los nueve programas.
- [`PHASES_AUDIT.md`](PHASES_AUDIT.md): genealogía completa de fases.
- [`NO_GO_AND_RETRACTIONS.md`](NO_GO_AND_RETRACTIONS.md): paredes, circularidades y precedencia.
- [`LIVE_FRONTIER_AND_RESTART_PLAN.md`](LIVE_FRONTIER_AND_RESTART_PLAN.md): protocolo operativo del reinicio.
- [`COVERAGE_INDEX.md`](COVERAGE_INDEX.md): inventario, cobertura y tamaño.
- [`fragments/`](fragments/): auditorías de bloque que sostienen esta síntesis.
