# Paper43: símbolo, forma, completaciones y rulings

Dictamen **(a)** para los teoremas de este frente, en sus hipótesis y normalizaciones declaradas. Leídos íntegramente P43:2919–5544, junto con la topología851–876 y las dependencias indicadas debajo. No se encontró un primer paso fallido. Esto no afirma prioridad bibliográfica ni deduce RH: los resultados describen una forma para S finito, sus completaciones elegidas y límites de familias específicas.

| Afirmación | Dictamen | Referencia y obligación descargada |
|---|---|---|
| Regularización, convergencia y unicidad fuera de1 | (a) | 2919–3190: sustracción en identidad; distribución soportada en1 tiene orden finito real, independiente del nivel compacto. |
| Separación de tests de igual módulo y coinvariantes | (a) | 3198–3303: un único coset local contribuye; el logaritmo p-ádico sólo se usa en1+pZp, o1+4Z2. |
| Símbolo en todas las componentes, máximo y Plancherel | (a) | 3305–3717: término conductor, paridad, constantes y Fubini absolutamente dominado. |
| Continuación meromorfa y contornos | (a) | 3720–3903: residuos∓i, sumas agrupadas O(k^-2), alturas y orientación correctas. |
| Radical, Tate, ausencia de splitting en tests | (a) | 3905–4183: ceros aislados del símbolo, traslaciones y caracteres separadores. |
| Completación fuerte y splitting ampliado | (a) | 4185–4430: dual fuerte completo, reflexividad, aniquilador trivial y densidad. |
| Rulings y fallo de extensión continua escalar | (a) | 4313–4615: dos familias que convergen al mismo par de puntos y dan límites incompatibles. |
| Firma, incluidas partes primitivas y ε-invariantes | (a) | 4617–4823: concentración ponderada, Gram diagonal dominante y codimensión finita. |
| Cono positivo propio en la completación | (a) | 4825–4891: bidegrees positivas controlan L¹ y luego la componente distribucional. |
| Álgebra Banach y determinante relativo | (a) | 4893–5083: inyectividad en L¹, control de potencias, dominio y rama de Log. |
| Pairing RR y límites | (a) | 5085–5182: exponentiación de dos formas, sin afirmar identidad de índice geométrica. |
| Cambio de S y estabilización | (a) | 5184–5350: compacto nuevo de masa1 y soporte que elimina todos los primos grandes. |
| Rulings en el límite sobre S | (a) | 5351–5544: sumación parcial de Mertens, control de diagonales y familia entre potencias primas. |

## Reconstrucciones que sostienen los dictámenes

### Símbolo y traza

En el término ramificado la suma telescópica de capas de unidades vale exactamente `−cond(κ)`, también para p=2: la capa V0 puede ser vacía y la fórmula sigue siendo válida. La paridad real cambia sólo el término sech; al usar reflexión de digamma se obtiene `logπ−Reψ(3/4+iτ/2)` para la componente impar. La integral regularizada de la componente par da `logπ−Reψ(1/4+iτ/2)`. Las identidades y el sector de la expansión asintótica concuerdan con [DLMF5.9.16](https://dlmf.nist.gov/5.9#E16), [5.7.6](https://dlmf.nist.gov/5.7#E6) y [5.11.2](https://dlmf.nist.gov/5.11#E2).

El máximo se alcanza sólo en la componente principal a τ=0: la parte real de digamma crece estrictamente con |τ| y cada factor finito tiene máximo cuando su fase es1; un carácter ramificado produce en cambio un término negativo. El intercambio de Fourier se domina cerca de0 mediante `min(2,τ²t²/2)` y fuera por caída exponencial. Sólo hay finitísimas componentes para un test dado.

La continuación meromorfa no consiste en continuar literalmente Reψ: se reemplaza por la semisuma de ψ con argumentos conjugados sobre el eje real y luego se continúa esa expresión holomorfa. Los residuos y el signo del cambio de contorno se comprobaron. Para el primo p, las caras verticales se escogen a mitad de los polos periódicos; la sumación de residuos es absolutamente convergente por la caída de la transformada del test.

### Radical y completación

Si F es ortogonal a todos los tests, en cada componente su transformada multiplicada por el símbolo anula las transformadas de C_c^∞. Estas son densas en Schwartz y en C0; el producto es L¹. Por tanto es cero. Los ceros aislados del símbolo y continuidad de la transformada fuerzan F=0. Si sólo es ortogonal a los primitivos, la forma se factoriza por los dos momentos de Tate. Trasladar un test no negativo mantiene N pero hace crecer alternativamente los dos momentos; los dos coeficientes deben ser cero.

La topología de D_A es un LF estricto: una sucesión cofinal de compactos y niveles tiene inclusiones cerradas con la topología inducida. Un acotado queda en un paso, y Arzelà–Ascoli para todas las derivadas lo hace relativamente compacto. Ésta es la propiedad Montel utilizada para identificar el bidual. La completitud del dual fuerte se demuestra directamente para redes de Cauchy; no se supone que una completación dé automáticamente una inyección en distribuciones.

La densidad de J(D_A) en `D_A'⊕C²` se deduce de su aniquilador: la primera componente se elimina mediante ortogonalidad primitiva, y la segunda por sobreyectividad de M. La acción sobre el dual sólo se afirma continua para cada H fijo; no se introduce una afirmación más fuerte de continuidad conjunta sin probarla. La topología inicial de J es estrictamente más débil que la original: las diferencias de la familia extendida F_n convergen por J y sus soportes escapan de todo compacto en la topología LF.

### Límites, firma y cono

Los tests extendidos F_n tienen L¹ exponencialmente pequeña y N acotada por `C n^-2 e^-na/2`; la segunda cota integra por partes dos veces antes de estimar. Esto da convergencia uniforme contra cualquier conjunto acotado de tests. Los picos Φ_n, en cambio, concentran su convolución exactamente en n log p y producen una contribución al menos `(log p)p^-n ||ω||²/r_n`. Con r_n=p^-2n diverge, aunque ambos argumentos convergen a los mismos rulings. Por eso la imposibilidad de extensión escalar secuencial es demostrada, no una reserva expositiva. Los límites iterados siguen siendo0; el texto distingue correctamente uniformidad, diagonal y límites iterados.

La firma no se infiere sólo de encontrar una función positiva y una negativa. Se construyen infinitas funciones con concentración espectral en intervalos disjuntos y colas ponderadas prescritas. Cauchy–Schwarz en tres regiones da las entradas fuera de diagonal. Las cotas geométricas sumables garantizan definitud de toda combinación finita e independencia lineal. Intersectar con un subespacio de codimensión2 conserva dimensión infinita. Para c=−m, el símbolo sólo se anula en un punto; ningún test no nulo puede tener transformada continua soportada allí, así que sigue habiendo definitud negativa.

### Determinante relativo y límite de Mertens

La norma de traza combina L¹ con dos pesos multiplicativos y una norma L¹ del lado Fourier. Su completación se inyecta en L¹ porque una sucesión de Cauchy tiene límites compatibles en ambas normas ponderadas: la convergencia Fourier uniforme identifica el segundo límite casi por todas partes. La serie logdet converge en el disco `|z| ||F||_1<1`, mediante una cota de potencias que usa una sola norma N, no ||F||_tr^r.

En la multiplicatividad los dos factores `1+z Fhat` y `1+z Ghat` están en el semiplano derecho; sus argumentos suman un número estrictamente entre−π yπ. Por tanto el producto no cruza el corte y Log es aditivo. Para identificar ese valor con la serie Δ_H se impone expresamente la desigualdad adicional que asegura `|z| ||H||_1<1`. No se ha construido aquí un operador con determinante de Fredholm: se trata del determinante relativo definido mediante T∘Log.

Mertens se usa sólo en su forma clásica `Σ_{r≤x}Λ(r)/r=log x+O(1)`. Sumación parcial da un error `C||φ'||_1`; para dos perfiles extendidos la derivada puede recaer en el más ancho y explica `1/max(n,m)`, no1/min. Los términos diagonales se controlan con el soporte y la caída `n^-1 e^-na e^-|t|/2`; la sumación prima añade a lo sumo un factor n. La familia alternativa centrada en log36^n tiene ancho menor que media distancia al logaritmo de cualquier entero distinto de36^n, y36^n no es potencia prima: desaparece toda contribución prima y sólo queda un término real tendiendo a0.

## Necesidad lógica y uniones

Estos resultados prueban los teoremas principales `introB`, `introC` e `introD`; la parte homológica `introH` se cerró en HOCHSCHILD-43.md. Para `introA`, la identidad smeared es una convolución escalar usando la sección homomorfa: también se leyó su prueba y `prop:hom`, líneas975–1150. La única componente de un intertwiner puede estar en a=γb; invariancia bajo p^n y caída real obligan a que su coeficiente sea constante. Así se comprueba la línea de morfismos anunciada, sin interpretar los smeared como una nueva categoría geométrica.

P44:698–724 cita exactamente la completación fuerte, densidad y seminorma de P43, en su normalización c=0. P44:1071–1138 usa esas entradas para aproximar la medida radial: el error Fourier es `min(2,ε|τ|)`, la cola es uniformemente integrable sobre acotados y los momentos convergen a `(r^{1/2},r^{-1/2})`. Esta unión queda comprobada. Las leyes de Frobenius/contacto de44 no necesitan la firma de43.

P45 usa la distribución local, las medidas y la estabilización sobre S; la completación, los rulings y el determinante de43 no son hipótesis de su comparación con Weil ni de su criterio de positividad. La firma indefinida de43 es para S **fijo** y no se transporta al límite sobre S. El propio texto lo advierte. Ningún cierre de este ledger aporta por sí solo el signo requerido por46.

## Alcance bibliográfico

Las fórmulas locales y la idea de traza de Weil tienen antecedentes explícitos. Las construcciones de completación elegida, familias incompatibles de límites y determinante relativo son verificables como están escritas; no se ha establecido su prioridad. El pairing denominado RR es, por definición, el par de exponenciales de dos formas, y el texto reconoce que no suma sus componentes ni prueba un índice de Hodge. Esta precisión impide atribuirle un resultado geométrico más fuerte que el demostrado.
