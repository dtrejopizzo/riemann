# Más allá de la cadena: información superior y realización integral

**Primera ronda, 28/11/2026.** Tres frentes de investigación independientes, con contraste bibliográfico adversarial. La fase permanece abierta. Este documento no vuelve a certificar RH/GRH y ninguno de sus resultados necesita suponerlas.

## Resultado de la exploración

La dirección más concreta es estudiar **qué información pierde un invariante aritmético al pasar a pares, determinantes o productos binarios, y cuánto cuesta recuperar compatibilidad simultánea sobre retículos prescritos**. Hay tres manifestaciones distintas, con ejemplos demostrados. Todavía no tenemos un teorema que las identifique entre sí.

La propuesta de programa es *realización integral cuantitativa de estructuras aritméticas*. Dentro de ella, las correlaciones superiores de tipos CM ofrecen un frente geométrico; las extensiones cristalinas filtradas ofrecen un frente de teoría de números. El nombre es provisional: una nueva área exigiría teoremas propios y aplicaciones independientes, no sólo esta agrupación de preguntas.

| Frente | Resultado probado en esta ronda | Pregunta que queda |
|---|---|---|
| Tipos CM | Dos tipos del mismo campo tienen todas las correlaciones de dos y tres puntos iguales, pero una de cuatro puntos vale 1/12 en uno y 1/24 en otro. | Realizar esa diferencia mediante períodos o grados aritméticos con normalizaciones y costes controlados. |
| Retículos | Determinantes unitarios no garantizan un retículo común; incluso todas las trazas de palabras pueden ignorar un coste integral arbitrariamente grande respecto del retículo inicial. | Acotar uniformemente el coste de realizar diagramas aritméticos concretos, con twists globales y relaciones de composición. |
| Obstrucciones superiores | Un álgebra diferencial de rango fijo tiene todos los cups de H¹ nulos, pero una obstrucción ternaria de orden ℓ^N, racionalmente nula. | Encontrar o excluir este tipo de pérdida en extensiones cristalinas con graduados prescritos y obtener cotas aritméticas. |

“Probado” se refiere a las proposiciones y ejemplos delimitados en los informes, no a prioridad bibliográfica. Los tres fenómenos generales tienen antecedentes. La novedad de las preguntas específicas aún no está establecida.

## 1. La conexión más tangible: CM, reconstrucción y estructuras de Hodge

Para un tipo CM Φ en un grupo abeliano G, escribir

    T_r(g₁,…,g_r) = |G|⁻¹ Σ_x Φ(g₁x)…Φ(g_rx).

La conjugación compleja cambia Φ por 1−Φ. Al expandir el producto se obtiene que todo T_r impar depende de órdenes inferiores. En particular, **pasar de dos a tres puntos no añade información**. El primer orden que puede añadirla es cuatro; no se afirma que cuatro siempre baste para reconstruir el tipo.

El núcleo binario de dos pesos estudiado en el frente 01 depende exactamente de T₂, el dato clásico de Colmez en este caso abeliano. Por ello variar ese núcleo no recupera toda la información del tipo CM.

El ejemplo usa G=C₂×C₁₂ y los conjuntos {0,1,4,6} y {0,1,3,7}. El campo puede ser E=F(i), con F el subcampo de grado 12 de Q(ζ₇₃). No es sólo un grupo formal: ambos perfiles son tipos CM de E. La diferencia aparece en los cuatro desplazamientos 0,1,2,3 de C₁₂.

Hay además una realización inmediata en teoría de Hodge: tensorizar sobre E cuatro estructuras CM de peso uno con los tipos trasladados por esos desplazamientos. Sus números h^(p,4−p), para p=0,…,4, son respectivamente

    (2,4,12,4,2)    y    (1,8,6,8,1).

Así, los datos de pares coinciden pero los números de Hodge de esos tensores difieren. Esto utiliza formalismo tensorial clásico; no es una nueva teoría de motivos ni prueba algo sobre ciclos algebraicos. El salto pendiente es de este observable de Hodge a una identidad de períodos o grados aritméticos con control integral.

**Primer problema preciso:** determinar si las alturas de tipos CM parciales de Zhao ya distinguen este par con la normalización requerida. Si lo hacen, esa parte del programa es un antecedente que debe usarse. Si no, localizar qué información falta y construir un observable que la registre. Véase [frente 01](FRONT-01-KERNELS.md).

## 2. La conexión estructural: dinámica de matrices y coste integral

Sobre un anillo de valoración O con uniformizante π, fijar un retículo L₀ y un conjunto S de mapas. El retículo

    C_n = intersección de w⁻¹L₀ para todas las palabras w de longitud ≤n

registra las condiciones de integridad simultánea hasta profundidad n. Su coste es κ(n)=length(L₀/C_n). Si C_n=C_(n+1), el proceso estabiliza y produce el mayor retículo estable contenido en L₀. Una cota uniforme κ(n)≤B da un certificado finito de estabilización a más tardar en B.

Con A=[[1,π^−N],[0,1]] y B=[[1,0],[π^−N,1]], todos los determinantes son 1, cada mapa admite un retículo estable por separado, pero no admiten uno común: tr(AB)=2+π^−2N no es integral. Además κ(n)=2nN.

Con sólo A hay un retículo estable y el coste mínimo es N, aunque tr(A^m)=2 y det(A^m)=1 para todo m. **El dato del retículo inicial es indispensable:** los invariantes racionales de las palabras no determinan el coste respecto de él.

Edificios, productos de matrices, alturas adélicas y representaciones integrales de quivers ya estudian este entorno. La contribución posible no consiste en definir C_n, sino en obtener cotas nuevas para una familia aritmética concreta. Las flechas rectangulares y las relaciones deben especificarse; un lift theta no se convierte automáticamente en un endomorfismo.

**Primer problema preciso:** un cuadrado de dos composiciones, con cuatro retículos fijados, mapas normalizados y un mismo twist global. Comparar el coste óptimo simultáneo con el obtenido controlando cada flecha por separado, y demostrar una mejora uniforme o una obstrucción que fuerce la pérdida. Véase [frente 02](FRONT-02-COMPATIBILIDAD.md).

## 3. El frente de teoría de números: pérdidas superiores cristalinas

El modelo exterior sobre Z_ℓ con generadores a,b,c,u de grado uno y

    da=db=0,   dc=ab,   du=ℓ^N ac

tiene todos los cups de H¹ nulos, pero el triple Massey ⟨a,a,b⟩ es ±[ac] de orden exactamente ℓ^N, sin indeterminación. Racionalmente es cero. Escalar las tres entradas por ℓ^e lo anula exactamente cuando 3e≥N: el coste es ceil(N/3).

Por tanto el coste binario y el rango no controlan, en álgebras diferenciales generales, el coste superior. **No hemos realizado este modelo como cohomología de Galois o como dato cristalino.** Esa realización no puede darse por supuesta.

El objeto aritmético propuesto es c_cris: el menor e que permite realizar cuatro retículos graduados prescritos dentro de una representación cristalina filtrada, con sus tres clases de extensión adyacentes multiplicadas por π^e. Si existe la realización racional, c_cris es finito: una conjugación diagonal limpia los denominadores de los bloques superiores. El lema demuestra finitud, no una cota uniforme.

**Primer problema preciso:** fijar K/Q_ℓ y cuatro caracteres cristalinos de rango uno con pesos concretos y H¹_f no triviales; calcular c_cris para familias de clases racionalmente realizables. Buscar una fórmula exacta, una cota efectiva o un contraejemplo aritmético a una cota sólo binaria. Esto sería una aportación comprobable a teoría de números, independiente de RH. Véase [frente 03](FRONT-03-OBSTRUCCIONES.md).

## 4. Qué descarta el contraste bibliográfico

| Conexión demasiado amplia para anunciar como nueva | Antecedentes encontrados |
|---|---|
| Autocorrelación CM y alturas | Función de Colmez; [Parenti](https://arxiv.org/abs/1803.02535); alturas de tipos parciales de [Zhao](https://arxiv.org/abs/2505.06541v2). |
| Cuatro puntos distinguen datos homométricos | [Ravy](https://arxiv.org/abs/1303.3792); reconstrucción por k-decks de [Keleti–Kolountzakis](https://arxiv.org/abs/math/0603415). |
| Retículos, matroides y geometría tropical | [Khan–Maclagan](https://arxiv.org/abs/2405.03505), [Kaveh–Manon](https://arxiv.org/abs/2405.03576); [Helly para edificios](https://arxiv.org/abs/2611.17844), noviembre de 2026. |
| Crecimiento de composiciones y alturas | [Breuillard, Height Gap](https://arxiv.org/abs/0804.1391) y [joint spectral radius](https://arxiv.org/abs/2103.09089). |
| Massey y Selmer | [Ray–Sujatha](https://arxiv.org/abs/2508.17156v2), revisión de septiembre de 2026. |
| Hodge p-ádica y coherencia superior | [Wild](https://arxiv.org/abs/2610.17169), octubre de 2026; [Molin](https://arxiv.org/abs/2611.28988), noviembre de 2026; deformaciones derivadas de [Galatius–Venkatesh](https://arxiv.org/abs/1608.07236). |

El corte solicitado es 28/11/2026. Se consultaron fuentes primarias, incluyendo trabajos de octubre y noviembre de 2026. La revisión combina algunas definiciones concretas con fichas y resúmenes; **no se leyeron íntegramente todos estos trabajos ni se recorrió exhaustivamente todo arXiv**. Los registros de cada frente documentan el alcance. No encontrar una formulación exacta en estas búsquedas no certifica su ausencia en la literatura.

También descartamos un supuesto defecto local/global de menores: con las normalizaciones habituales resulta ser exactamente la altura de Plücker. Renombrarlo no produciría un invariante nuevo.

## 5. Qué podría constituir una aportación propia

La conexión entre los tres frentes es por ahora un **principio de investigación**, no una equivalencia matemática: información agregada suficiente para ciertos problemas puede perder las elecciones necesarias para estructuras superiores, y recuperar esas elecciones puede tener un coste integral independiente.

Para convertirlo en una teoría se necesitan al menos estos pasos:

1. Un objeto aritmético concreto, con equivalencias e invariancia especificadas. Los candidatos actuales son el observable CM de cuatro factores y c_cris.
2. Un teorema cuantitativo no recuperable inmediatamente de los antecedentes: por ejemplo, una fórmula de c_cris o una identidad integral de períodos de cuatro factores.
3. Un puente demostrado entre dos frentes: traducir un exponente de obstrucción en una cota de κ para un diagrama aritmético identificado, o controlar integralmente el tensor CM que distingue el ejemplo.
4. Una aplicación independiente: índices de congruencias, realización de extensiones o períodos CM. No se ha probado aquí una mejora sobre distribución de primos ni una nueva función L.

La prioridad de trabajo recomendada es **CM de cuatro factores primero**, porque ya hay un par concreto y un observable de Hodge que lo distingue; **c_cris después**, por su pregunta aritmética precisa; usar el frente de retículos como herramienta para medir las pérdidas. Antes de reivindicar novedad deben compararse los enunciados completos de los antecedentes próximos.

## 6. Expediente reproducible

- [Frente 01 y pruebas](FRONT-01-KERNELS.md); [búsquedas](bibliography/FRONT-01-SEARCH.md).
- [Frente 02 y pruebas](FRONT-02-COMPATIBILIDAD.md); [búsquedas](bibliography/FRONT-02-SEARCH-LOG.md).
- [Frente 03 y pruebas](FRONT-03-OBSTRUCCIONES.md); [búsquedas](bibliography/front03-consultas.json).
- [Comprobación exacta CM](experiments/cm_correlations.py) y [salida](experiments/cm_correlations.json): 24 pares, 576 triples, cuatro puntos y números de Hodge.
- [Comprobación del álgebra diferencial](experiments/check_massey_dga.py): signos, d², Leibniz y escala de la obstrucción. Las pruebas para todos los parámetros están en los informes; los scripts son comprobaciones auxiliares.

Esta ronda entrega ejemplos, barreras y preguntas precisas. **No entrega todavía un descubrimiento de prioridad establecida ni una nueva área constituida.** La fase 216 queda abierta con problemas que permiten decidir el siguiente avance mediante una prueba o un contraejemplo.
