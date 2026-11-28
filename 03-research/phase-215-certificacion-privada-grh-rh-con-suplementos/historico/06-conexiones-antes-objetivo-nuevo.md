> **Actualización V2:** cualquier referencia de esta ficha al antiguo fallo global de caracteres53 queda retirada. El dictamen vigente y el nuevo inventario de reparaciones están en el reporte final V2. Esta ficha conserva el programa temático, no un aval externo.

# Conexiones matemáticas y programa de investigación

El patrón central que propone la serie es convertir **divisibilidad de coeficientes theta en una desigualdad unilateral sobre primos**, mediante la comparación entre formas cortas, generación de casi todo un espacio y un límite inferior para su covolumen. Es una conexión concreta y susceptible de producir problemas independientes. En esta revisión no quedó demostrado que esa conexión cierre la prueba de GRH, ni que constituya por sí misma un campo nuevo.

La dificultad de RH no obliga lógicamente a que su solución invente una nueva rama. Una combinación nueva y válida de herramientas conocidas también podría resolverla. La pregunta productiva es qué puente exacto aporta el trabajo, cuáles de sus piezas están demostradas y qué resultados sobreviven si se retira la conclusión sobre RH.

Fuentes internas: P57 `main.tex`, particularmente líneas 100–120, 485–640 y 833–843; cotejo con los enunciados de P46 y la revisión específica de P51/52. Las referencias a «la propuesta» describen el argumento del manuscrito, no un teorema certificado por este informe.

## El mecanismo propuesto

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

## Qué conexiones ya existen

| Conexión | Antecedente | Qué tendría que añadir la serie |
|---|---|---|
| Espacios adélicos, fórmula explícita y ceros | [Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*](https://arxiv.org/abs/math/9811068) interpreta fórmulas explícitas mediante una traza no conmutativa. | Objetos o propiedades adicionales precisos; la asociación «adeles + traza + RH» no es nueva. |
| Theta CM, coeficientes algebraicos y valores L de Hecke | [Bannai–Kobayashi, *Algebraic theta functions and p-adic interpolation of Eisenstein-Kronecker numbers*](https://arxiv.org/abs/math/0610163) construye y estudia ese puente. | Divisibilidad simultánea, casos no ordinarios, constantes exactas y uniformidad requeridas por 49/54; no basta citar la existencia del puente clásico. |
| Masas de retículos hermitianos y valores L | [Gan–Hanke–Yu, *On an exact mass formula of Shimura*](https://web.math.princeton.edu/~jonhanke/Web-02/Mass-Formula-of-Shimura/shimura-mass.pdf) da fórmulas exactas con factores locales. | La combinación con los momentos, el crecimiento de rango y una cuenta completa de medidas. |
| Crecimiento arquimediano, información finita y pendientes aritméticas | El método de pendientes tiene antecedentes sistemáticos; véase [Bost, *Evaluation maps, slopes, and algebraicity criteria*](https://ems.press/books/standalone/21/408). | La realización concreta mediante aplicaciones de Poincaré y cadenas theta, con el error sobre primos como cantidad residual. La semejanza con pendientes es conceptual, no una aplicación comprobada de un teorema de Bost. |
| Comparación automorfa entre formas unitarias | [Labesse, *Changement de base CM et séries discrètes*](https://webusers.imj-prg.fr/~michael.harris/CBCM.pdf) desarrolla cambio de base, estabilidad y multiplicidad bajo condiciones precisas. | La comparación exacta para los espacios y proyectores elegidos, o una prueba independiente válida. |

La búsqueda bibliográfica realizada identifica antecedentes, pero no es una búsqueda exhaustiva de prioridad. «No encontré un resultado idéntico» no certifica novedad.

## Qué sería una contribución específica si se valida

1. **Un teorema de segundo momento uniforme con constante principal uno.** P51 requiere crecimiento simultáneo del rango, peso, campo y nivel. Si se prueba con todos esos parámetros y con un error que tiende a cero, sería un resultado concreto que puede estudiarse sin mencionar RH. La auditoría profunda posterior reconstruyó sus mecanismos locales, conteos, Bessel, covolumen y masas, con correcciones locales explícitas que preservan las cotas; véase SPANNING.md. La clasificación externa de Green y los datos ambientales siguen siendo entradas identificadas, no teoremas reprobados desde cero.
2. **Una ley de divisibilidad multivariable con acción de Frobenius sobre las plazas CM.** El contenido distintivo sería la fórmula exacta de los exponentes y su control en cada primo, no sólo la existencia de divisibilidad de coeficientes theta.
3. **Un principio de covolumen con elección de twist dependiente de cada primo.** Debe explicar por qué varias realizaciones integrales controlan un mismo objeto global, cómo se suman sus pérdidas y por qué no se mezclan retículos incompatibles.
4. **Una cancelación demostrada entre esas dos leyes que deje una suma de primos reconocible.** Ésta es la conexión más importante para el objetivo RH. Una identidad formal entre símbolos no la prueba: exige que ambos lados midan las mismas formas, los mismos retículos, las mismas normas y el mismo rango de parámetros.
5. **Un tratamiento local integral fuera del rango de Fontaine–Laffaille.** Si los exponentes de cup products de P56 son correctos en toda la generalidad afirmada, sería una contribución independiente. Su validez se decide en la revisión de P56; no se puede inferir del éxito formal de la cadena.

La prioridad bibliográfica de estos puntos no está establecida. El estado matemático debe leerse individualmente: varios mecanismos del segundo momento fueron reconstruidos; el intercambio y la cadena de covolumen presentan el fallo de caracteres documentado en ERROR-53-CARACTERES.md.

## Un principio abstracto que sí se puede aislar

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

## Programa que permite avanzar aunque la prueba de RH quede abierta

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

## Atribución y frontera de lo demostrado

P57:833–843 atribuye a Levent Alpoge la matemática organizada por los tres teoremas y el camino al semiplano libre de ceros; atribuye a la serie su organización, nombres y escritura en papers. Este informe conserva esa atribución tal como la declara el propio autor. No verifica aquí la autoría externa ni la afirmación, también presente en ese pasaje, de que exista una prueba formal completa de GRH.

Por tanto, la contribución propia que puede describirse sin exceder la evidencia es la **arquitectura expositiva y el intento de compatibilizar un marco de Weil con esa ruta automorfa**. La prioridad de cada construcción adicional y la validez matemática del puente final requieren las revisiones particulares. Una conexión prometedora puede orientar investigación incluso cuando alguno de los teoremas que pretendía usar resulte incorrecto; para desarrollar esa conexión conviene reformular explícitamente el teorema fallido, conservar las piezas válidas y medir qué conclusión más débil permiten.


## Balance tras la auditoría profunda: qué conservar y qué rediseñar

El cierre de [HOCHSCHILD-43.md](auditoria-profunda/HOCHSCHILD-43.md) aporta una pieza separable del objetivo RH: el cálculo de complejos torcidos del crossed product semilocal rápido. Su contenido no es sólo una analogía verbal. Se exhiben contracciones continuas con pérdidas explícitas de peso y conductor, y una equivalencia que distingue la torsión real trivial de la no trivial. Esta construcción permite investigar qué información aritmética conserva esa homología y cuál descarta. Su resultado de insensibilidad muestra, a su vez, por qué no basta identificar esa shadow con una intersección positiva.

El frente51/52 aporta otra conexión concreta: un promedio orbital de Siegel, la geometría de pares de marcos y la reproducción de coeficientes de series discretas se combinan para controlar un segundo momento casi óptimo. Los pesos cambian a lo largo de la torre de Heisenberg y los módulos se cancelan exactamente. La uniformidad se sostiene mediante dos mecanismos distintos: ganancia de profundidad y control de frecuencias. El cálculo exacto de masas y covolúmenes evita que aparezca una constante absoluta por cada dimensión. Estas verificaciones están documentadas en SPANNING.md, incluidas las reparaciones del cutoff p-ádico, del orden de multiplicación en FJ y del exponente homogéneo del tubo. Sería razonable extraer un teorema autónomo de este frente y someterlo a revisión externa especializada antes de usarlo como parte de una conclusión sobre RH.

Una tercera conexión, reconstruida por el frente de multiplicidades, es el uso conjunto de integridad y análisis L² para forzar finitud: después de regularizar la integral orbital, sus coeficientes de caracteres son enteros; Bessel/Peter–Weyl limita su suma cuadrática; por eso sólo finitos coeficientes pueden ser no nulos. Es un mecanismo matemático concreto que merece comparación con otras pruebas de fórmulas de caracteres. Aquí no se afirma que sea nuevo: la novedad exigiría identificar exactamente qué regularización, hipótesis y fórmula no están en la literatura.

El fallo [ERROR-53-CARACTERES.md](auditoria-profunda/ERROR-53-CARACTERES.md) cambia la prioridad del programa. Antes de comparar determinantes hay que hacer compatibles los caracteres de las representaciones de Weil bajo producto y restricción. No basta añadir un factor escalar: un carácter no trivial depende de los elementos de los grupos. El proyecto inmediato es formular una identidad de intercambio con los caracteres correctos, verificar que sus espacios de origen y destino son los que usa la cadena, y recalcular su dependencia del twist. Sólo después puede preguntarse si el covolumen inferior sigue controlando el mismo retículo que las formas cortas superiores.

Así, las dos direcciones con resultados intermedios auditables son el cálculo homológico semilocal y el segundo momento cuantitativo de Poincaré. El puente decisivo entre divisibilidad theta y cotas sobre primos sigue siendo un programa condicionado a reparar las identidades de intercambio y sus consecuencias. No hay evidencia suficiente para bautizar una nueva rama ya establecida, pero sí un conjunto de problemas matemáticos precisos que pueden desarrollarse sin presuponer la conclusión RH.


La revisión ulterior [FORMA-COMPLETACION-43.md](auditoria-profunda/FORMA-COMPLETACION-43.md) reconstruyó además el símbolo completo, la firma, las completaciones, los rulings y el determinante relativo. Un resultado conceptual especialmente útil es la demostración de que aproximaciones a los mismos rulings pueden dar valores diagonales0, positivos o divergentes para la forma escalar; en el límite sobre S, unas familias lentas dan1 y otras dan0. Esto delimita exactamente qué tendría que añadir una futura teoría de intersección: una elección intrínseca de dominio/topología o de regularización que seleccione la pairing, y un principio de signo compatible con ella. Las construcciones presentes no dan ese principio, y sus propios contraejemplos impiden obtenerlo simplemente prolongando la forma escalar por continuidad. Es una restricción matemática comprobada para cualquier desarrollo posterior del marco.
