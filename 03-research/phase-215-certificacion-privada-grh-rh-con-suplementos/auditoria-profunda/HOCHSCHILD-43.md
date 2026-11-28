# Paper43: cierre del frente Hochschild

Revisión directa de `main.tex`, líneas558–742 y1200–2886. Dictamen **(a)** para `prop:crossed`, `thm:excision-input`, `thm:kunneth` y `thm:shadow`, en las topologías y con la convención de bimódulos expresamente declaradas. No se extiende este dictamen a completaciones, firma, determinantes y rulings posteriores. La equivalencia Schwartz de productos se utiliza como resultado clásico citado por el manuscrito; no se rehace su demostración general.

## Excision y tensorizaciones

El punto topológico no queda reducido a excisión algebraica. La partición real de la unidad y los idempotentes finitos dan un splitting derecho continuo, con suma de seminormas controlada por la pérdida `l→2l+2`. El bloque `χ_p` retiene el valor en0: sustituirlo por una suma de shells habría sido inválido, y el texto no lo hace. La suma que define h converge absolutamente en el producto proyectivo completado. La identidad `h(ab)=h(a)b` vale también para multiplicadores del álgebra ambiente.

En excisión1678–1762, el complemento topológico produce una suma **finita** de patrones en cada grado. El primer cociente se filtra por longitud de la cola desde la primera letra L: las caras no internas a I reducen esa longitud. Sus graduados son bar reducido de I tensor un espacio completo y se contraen con h. En el segundo cociente se filtra por posición del primer I. El módulo auxiliar N tiene acción inducida desde A/I, de modo que I lo anula. Las aplicaciones Φ y Ψ son de complejos por linealidad derecha de h; el término residual de grado0 desaparece precisamente porque I·N=0. La filtración es exhaustiva en un número finito de pasos por grado y las contracciones se extienden compatiblemente; no se toma un límite infinito de operadores en un grado fijo.

Künneth1765–1846 utiliza bar de las unitizaciones y graduación por soportes. Los términos libres del tensor total son efectivamente bimódulos libres sobre la unitización tensorial. La comparación por generadores es continua y las contracciones preservan soportes. La parte mixta del cociente `C⊕I⊕J`, con IJ=0, es contractible por excisión, no descartada por intuición. Las inclusiones son las flechas de equivalencia; sus inversas no necesitan ser equivariantes. La naturalidad que requiere Koszul se demuestra por las flechas y el argumento del cono, no suponiendo equivocadamente homotopías equivariantes.

## Crossed product rápido

En2115–2392, la identificación de espacios de familias ℓ¹ con tensor proyectivo se demuestra por igualdad de seminormas y densidad de soporte finito; no se presupone nuclearidad del álgebra p-ádica. El cambio de factores A mediante α_g cuesta una potencia de H(g), absorbida por pesos rápidos. El cambio `(g,h)→(g,gh)` conserva la familia de pesos por submultiplicatividad.

La contracción de la resolución Koszul sobre Z usa sumas finitas entre0 y n: su norma de peso k es ≤`|n|p^{k|n|}≤p^{(k+1)|n|}`. Por tanto es continua en la topología realmente usada, que exige todos los pesos exponenciales. La resolución bar inducida es continuamente escindida; sus columnas son finitas en el grado exterior. La comparación por bimódulos libres preserva la etiqueta total γ.

La torsión de la componente γ es exactamente `α_γβ` a la derecha. El operador Koszul inicial es `α_p^{-1}−1`; el mapa en grado I dado por `∏_{i∈I}(−α_pi)` lo identifica con el Koszul de `α_p−1`. En efecto `(α^{-1}−1)(−α)=α−1`. La reversión1222–1235 cambia después la convención derecha por izquierda y respeta las dilataciones. No hay inversión perdida de γ.

## Complejos locales y shadow

El lema de bloques1849–1960 inserta el idempotente antes de la primera arista no concordante. Se verifican cancelaciones de caras y la pérdida de seminormas para sumar todas las componentes. Para torsión no unidad no hay bloques diagonales de shells; el único bloque del origen sobrevive como C. Para unidades distintas de1, un carácter κ con κ(u)≠1 da inverso de `z−ρ(z)` y una contracción con pérdida uniforme `l→2l`. En el lugar real se amplía por multiplicadores periódicos, o por signo, se usa homotopía central y se vuelve al ideal por excisión. La convención `A_ρ` es torsión **izquierda**, por lo que `R_z−L_z=z−ρ(z)` tiene el signo correcto.

Para torsión trivial real2539–2662, `x=sinh t` transforma la condición de caída superexponencial en la topología Schwartz. La resolución por la diferencia de coordenadas tiene división continua: cerca de la diagonal se usa la integral de la derivada; lejos, la división por x−y y sus derivadas están acotadas. El mapa a la resolución bar da en Hochschild la derivación D, con factor invertible cosh(t). Sólo el mapa final π debe ser equivariante, como efectivamente lo es.

Para shells triviales2664–2754, la contracción se construye por la primera separación de cosets. Un test de conductor M sólo requiere m≤M; indicadores de igual coset tienen suma absoluta de Fourier1. El coste es ≤16nM y se absorbe en el conductor `N'=N(n+2)+1`, uniformemente en shell j con peso2l. Por eso la contracción se extiende a la completación; la densidad de caracteres finitos sola no habría bastado.

Finalmente2756–2886: las proyecciones al grado0 y evaluación en0 son equivalencias y conmutan con dilataciones. Si la componente real de γw es distinta de1, el tensor local se contrae y sólo queda el summand escalar exterior. Si es1, las componentes finitas no triviales se evalúan en0 y las triviales permanecen, mientras el factor real aporta grados0 y1. Aplicar Koszul a las flechas equivariantes conserva equivalencias por el cono finitamente filtrado. Se obtiene exactamente `thm:shadow(a)–(e)`.

## Alcance y novedad

Este cierre descarga el pendiente topológico del primer informe07. No produce positividad de la forma de Weil: el propio cálculo deja visibles las limitaciones de la shadow, y el paper distingue su construcción homológica de la distribución de traza. La combinación explícita de álgebra semilocal, torsión por ideles y contracciones controladas es un resultado verificable que merece comparación bibliográfica; no está acreditada su prioridad. La construcción general de Hochschild de crossed products y el patrón adélico tienen antecedentes citados por el propio autor. La posibilidad de desarrollar esta parte como trabajo separado no depende de que la cadena hacia RH se cierre.
