# Auditoría profunda de la deducción analítica de paper 46

Estado: primera tanda reconstruida. Se auditó el argumento de las líneas 2492–3274 y 5107–5408, además del principio de alturas 3386–3511 y las reducciones elementales 4190–4308 y 4626–4788. Este registro separa las implicaciones comprobadas de los teoremas automórficos que aún deben suministrar sus premisas.

## Gran criba y detección de ceros

La variante citada como `an:thm-HB` se cotejó con el facsímil del **corolario 2, p.238**, de [Heath-Brown, A mean value estimate for real character sums](https://matwbn.icm.edu.pl/ksiazki/aa/aa72/aa7234.pdf). Permite coeficientes complejos arbitrarios y suma sobre caracteres reales primitivos de conductor ≤Q, con coste `(QN)^ε(Q+N)` y suma de `|a_n1 a_n2|` para producto cuadrado. No se confundió con el corolario 1, restringido a índices squarefree. Estado: entrada publicada cotejada; no se reprobó el teorema clásico desde sus fundamentos.

Reconstrucción de `an:prop-density`:

1. Para `χ=ξχ_d`, con d primo y d∤N, la componente en d es primitiva y no trivial. El conductor primitivo contiene d; los factores omitidos al pasar a módulo Nd provienen de N. Por eso inclusión-exclusión sobre e|N da una constante que depende sólo de N en Pólya–Vinogradov. El producto no es principal, de modo que L es entera.
2. La identidad exacta para el resto de truncación se obtiene de `s∫_Z∞S(u)u^{-s-1}du−S(Z)Z^{-s}`. Reemplazar S(u) por S(u)−S(Z) es correcto incluso con Z real no entero.
3. En el producto por el mollifier, `b_1=1` y `b_n=0` para `1<n≤Y`, pues `Y≤Z`. El largo es ≤YZ=X. La cota `|b_n|≤τ(n)` es uniforme en d, ξ y s.
4. La detección usa la media de la función holomorfa g, seguida de Cauchy–Schwarz, en un disco de radio θ/2. El disco queda en el rectángulo fijo porque todo cero está a la izquierda de 1. No se intercambia una cantidad de ceros con una cantidad de caracteres: se detecta al menos un cero por primo malo, que es justamente el objeto contado.
5. En el término de error, el ahorro es `e1=θ(2−θ)/4≥3θ/8` para `0<θ<1/2`. El factor X al sumar sobre primos se ha incluido.
6. En la gran criba, escribir `n_i=k u_i²` con k squarefree y quitar la restricción squarefree para obtener una cota superior lleva a `Σ k^{−α}(Σ u^{−α})²`, `α=1+θ−2ε>1`. Para k≤Y el término es `Y^{1−α}/k`; para k>Y la cola es `O(Y^{1−α})`. El factor log Y está presente y la extensión a sumas infinitas converge.
7. El exponente antes de absorber el logaritmo es `1−θ²/4+(2+θ/2)ε`; dado `θ<1/2`, el logaritmo se absorbe en el margen hasta `3ε`. Con `ε=θ²/32` el exponente es `1−5θ²/32 < 1−θ²/8`. Las constantes pueden depender de θ; θ se fija antes de X.
8. Integrar sobre el rectángulo y sumar sobre el número finito φ(N) de ξ conserva el ahorro. La comparación con `X/(φ(N)log X)` permite elegir d en cualquier clase coprima fija.

**Dictamen local:** `an:prop-density` y `an:cor-choice` están comprobados a partir de las entradas clásicas declaradas. No necesitan hipótesis de no anulación global de los twists ni GRH. El primo elegido puede depender de la caja y del cero que se quiere descartar.

## Transformada y lema de Landau

`an:lem-R` (2547–2589): la integración de `1/n−1/x` produce `D_q(s)/(s(s−1))`. El polo doble principal se cancela al restar `log x/φ(q)`. El numerador restante se anula en s=1 por la definición de c_q. El residuo en ρ es

`(n_q(ρ)−n_q^K(ρ))/(φ(q)ρ(1−ρ))`.

El signo es correcto: el logaritmo derivado de los twists aparece con signo positivo en D y se divide por `ρ(ρ−1)`. Pueden cancelarse polos; el texto no afirma que cada cero produzca necesariamente uno.

`an:prop-pnt` (2594–2630): para moduli fijos, un cero real excepcional aporta `t^β1`, β1<1 fijo, que sí es absorbible en `t exp(−c√log t)` para t suficientemente grande. La cola de la integral converge. La holomorfía de la transformada en 1 obliga a que el límite constante de R sea cero. No se usa aquí una uniformidad en d que el PNT no proporcione.

`an:lem-landau` (2636–2682): f≥0 sólo después de v0; la integral inicial restante es entera. Si la abscisa de convergencia σc excede β, una continuación holomorfa en σc permitiría expandir en un disco centrado en σc+1. Tonelli sobre los coeficientes no negativos extendería la convergencia a σc−δ, contradicción. La meromorfía y la hipótesis de polos reales simples convierten la singularidad en polo simple con residuo positivo para Ψ, negativo para F. El argumento no excluye polos complejos por un razonamiento de signos local: los excluye al garantizar holomorfía en el semiplano de convergencia.

`an:thm-criterion` (2842–2874): se elige primero un d cuyo conjunto de twists no tiene ceros en la caja que contiene ρ y el segmento real [β,1). Ello hace no negativos todos los residuos reales posibles a la derecha de β. Se excluye la alternativa de polo real negativo de Landau, y después el residuo en ρ no puede cancelarse con el de un twist. El orden de cuantificadores es correcto: la premisa se exige para todo d de la clase; la prueba usa uno que depende de ρ. **Dictamen: comprobado como implicación.**

## Existencia de datos y sus rangos

Se reconstruyó `an:lem-behrend`: no hay acarreo porque cada combinación convexa entera tiene dígitos menores que la base `Λ0H`; ambas codificaciones están en [0,o). La congruencia se vuelve igualdad y la estricta convexidad de una esfera fuerza igualdad de los tres vectores. El caso degenerado de base 1 sólo tiene un vector y no causa excepción.

En `an:prop-sparse`, la parte 2-ádica de g tiene orden exactamente `2^s`, por la valoración de `(1+2^v w')^{2^j}−1` con v≥4. Para ℓ=2 se usa el orden de 4 módulo `3^c`; para ℓ impar, elevar al cuadrado elimina signos y Behrend fuerza e1=e2=e3. La fórmula de lifting-the-exponent produce la contradicción `2^s≤(ℓ+1)i<(L+1)l0≤2^s`. No se está suponiendo que ℓ sea coprimo a todo q1: sólo a q', como exige la definición.

`an:lem-windows` usa moduli `Q≤W^A≤(log y1)^A`; Siegel–Walfisz se aplica en ambos extremos. El intervalo en p es multiplicativo, no un intervalo corto aditivo que exigiera otro teorema. El coste de potencias primas es menor que el término principal porque `√y2≥e^W`.

La construcción `an:thm-data` cumple D1–D8 para cada entero x suficientemente grande, con parámetros fijos:

- Las potencias mínimas de 2 y 3 dan m y r en los intervalos declarados.
- El redondeo de b a múltiplo de q1x1 altera log b en menos de 1; redondear x1 hacia abajo conserva la desigualdad de los seis logaritmos.
- La densidad del conjunto de lugares pierde `x^{ε/2}` y una potencia fija de log x; ésta es absorbida por el otro `x^{ε/2}`. El entero n depende de ε, que ya está fijo.
- Los h_K+1 intervalos de primos son disjuntos. Igualdad de dos clases de ideales da `p_i bar p_j` principal y un generador integral; la norma compleja es el producto positivo p_i p_j, sin necesidad de escoger todos los primos principales.
- Para N se necesita un generador de norma N en E, no en K. La representación como suma de dos cuadrados basta porque i∈E.

Se revisaron las desigualdades S1–S7. Sus márgenes provienen de `log x≥10^14 C_P`, `log b≤x^{1/100}`, `x^{10^6}≤x1` y `x1^{10^6}≤b`. En particular, la relación que necesita 51 para absorber `f2^{3−k}` sí está disponible. La existencia analítica toma como entrada que C0(q0,d) es finito e independiente de los datos; esa propiedad específica del kernel de49 fue comprobada posteriormente en THETA, CJ08 (`pz:C0` y su absorción). No puede omitirse de la lista de entradas.

## Producto con twist dependiente del primo

`au:product` y `au:twistprime` (3403–3511) fueron reconstruidos completamente como resultados abstractos. Los isomorfismos de campos son abstractos, no continuos; `overline(Q_ℓ)` y C son algebraicamente cerrados de característica cero y grado de trascendencia del continuo. Esto permite extender embeddings de campos de números y mover un elemento trascendente para contradecir una cota uniforme de valoración.

En la prueba de `au:twistprime`, los dos cambios de base u y u' corresponden a iota y a bar-iota; **sirven al mismo twist θ_iota** porque el índice se define simultáneamente para todos los twists permitidos. Éste es un punto necesario y sí está incluido en la definición. Tomar determinantes da el coste `2δ`, no δ. La conjugación compleja no conmuta con un automorfismo arbitrario σ: el texto usa correctamente `σ'=cσc`. La cota de la Gram conjugada proviene de Cauchy–Schwarz en la potencia exterior y de Fischer/Hadamard, manteniendo el factor de volumen al cuadrado.

**Dictamen:** principio abstracto comprobado. Quedan aparte la construcción de la twisted lattice concreta y las cotas de altura del cociente de determinantes que deben dar 53–56.

## Ensamblaje final

Las reducciones de Short Forms y Spanning de 46 son correctas **si se suministran I1–I7 con exactamente el alcance declarado**:

- El redondeo `g_ℓ=floor(gain_ℓ−err_ℓ)` hace integral el producto después de multiplicar por cB, con la dirección correcta de la valoración.
- La constante del seesaw se cancela antes de estimar. La cota archimediana de cB se multiplica por 2 porque se acota norma al cuadrado.
- El índice de una unión se controla por matrices de bloques; la definición permite familias de tamaño arbitrario y el coste no se multiplica indebidamente por ese tamaño.
- `au:onetranslate` es una aplicación de Cauchy–Schwarz a la media conjugada de BB*. `au:few` es una iteración que reduce la codimensión; la desigualdad inicial obliga a `ρ=2dim V/(5dim W)≤1`, por lo que el redondeo del número de pasos está controlado.
- Restringir a la parte ramificada cuesta como máximo número de traducciones por codimensión de la fuente; el error b^-8 queda dentro del presupuesto final b^-2.

Para el teorema de covolumen, el ensamblaje 5014–5052 también es correcto como implicación de `inj`, `aux`, `factor`, `regular`, `onelift`, `hecke` y `mult`: el coste de los auxiliares de rango ≤4d/b² se absorbe y se conserva el signo `−H_main`. No se da por verificada ninguna de esas entradas nuevas por esta deducción.

Finalmente `an:lem-rem` identifica exactamente la suma de primos. En `an:lem-hmain` la cota positiva del término principal permite reemplazar nH por dH; sin esa positividad el argumento sería inválido. La cota se prueba en el texto, usando `Λ_K≤2Λ`, `floor(n/ν)≥n/(2ν)` y `log(M/Ω)≥20log b`.

La cancelación entrega `m rem≤fa(log b)^5`. Para pasar a R, el factor `#Φ_a/#Φ_b` se conserva y cuesta log b. El PNT se aplica sólo en x1, enormemente mayor que x, con q0,d fijos. La transición de x entero a y real cuesta O(1/x), menor que la escala buscada. Elegir `q0=18480q` y eliminar los factores de Euler añadidos, cuyos ceros tienen parte real 0, da el semiplano. La ecuación funcional del carácter primitivo da el otro lado de la franja.

**Conclusión de esta tanda:** se comprueba la implicación de los tres teoremas automórficos, válidos para los datos construidos, a GRH para Dirichlet y RH, bajo las entradas clásicas señaladas y la finitud de C0. El trabajo pendiente está ahora localizado en obtener rigurosamente esas premisas y sus uniones; no en una supuesta inferencia de RH a partir de chequeos de ventanas finitas.


## Cancelación de ganancias y ventana del nivel: relectura para las uniones

Se cotejaron directamente `def:au-hmain` y `au:gains`,46:3804–3883. En el caso inerte, Λ_K(p^e) es2logp para e impar y0 para e par; en el ramificado d, la normalización v(π_d)=1/2 produce logd. Esto coincide con los conjuntos I_p y la normalización p-ádica usados por49. Un primo no split es primo a q₁, de modo que el partner u(−p^e) está definido en todos los sumandos no nulos. Para p≥x₁, y/p^e≤a/x₁≤κ anula cada parte positiva. No hay una cola de primos descartada sin estimar.

Al multiplicar los gains por2logp y sumar, la identidad de `au:cancel` elimina exactamente los dos paquetes finitos: el de los lugares de κ y el de Pa. Se conservan los factores m,k y #Pa; no se utiliza el signo del remainder para esta igualdad. Stirling con resto superior1+(log a)/2 y logΩ=−1−c₁+log(2π/rd) cancela c₁ en la diferencia s∞(a)−s_main. La cota inferior de logN en `au:level` deja aG+(15/2)a logb+m(1+(log a)/2), dominado por(23+15/2+1)a logb<32a logb con los tamaños ya comprobados. Ésta es la razón precisa por la que la misma ventana de N sirve en la aplicación de Short Forms; la cota superior de N se usa separadamente en la razón de dimensiones de Spanning.

Esta comprobación descarga el contenido y las normalizaciones de la importación `au:gains` en49. No descarga por sí sola las construcciones theta que han de realizar esas ganancias; su auditoría es THETA/UNIONES-THETA.
