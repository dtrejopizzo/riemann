# Un criterio aritmético unilateral en las cuartas potencias

Sea S₂=Σ_{n≥2}Λ(n)/n²=−ζ′(2)/ζ(2). El signo global de P47 equivale a la existencia de una constante finita C tal que, para todo entero j suficientemente grande y x=j⁴,

    Σ_{2≤n≤x} [1−(n/x)³] Λ(n)/n² ≤ S₂ − 3/(2x) + C/x^(3/2).

Sólo aparece una suma finita para cada j. El error permitido y el término principal son parte de la condición; la mera convergencia a S₂ no basta.

**Forma física de la traza trasladada.** En 038, la transformada inversa de 1/(t²+9/4) es exp(−3|r|/2)/3. Poner x=exp r≥1 y definir

    Q(x)=x^(−3/2) Σ_{n≤x} nΛ(n) + x^(3/2) Σ_{n>x} Λ(n)/n².

Entonces se cumple exactamente

    k(log x)=H(log x)+[(3/2)√x−Q(x)+x^(−3/2)(1/2−S₂)]/3,

donde H es la transformada inversa de m♯(t)/(t²+9/4) y está acotada por integrabilidad absoluta. En efecto, cada cos(t log n) produce dos exponenciales centradas en ±log n. La primera, con el peso del contacto, da los dos tramos de Q; la segunda da x^(−3/2)S₂. La densidad continua produce las mismas expresiones con dn en [1,∞) en lugar de las masas Λ(n); sus dos valores son (3/2)√x−x^(−3/2)/2 y x^(−3/2). La fórmula sigue primero con corte y luego por convergencia absoluta a x fijo y por 038. En particular una cota superior en k(log x) equivale, hasta una constante aditiva uniforme, a Q(x)≥(3/2)√x−C. Reordenar Q y dividir por x^(3/2) da la desigualdad del enunciado.

**Por qué bastan las cuartas potencias.** En r>0 y en el sentido de distribuciones,

    (9/4−∂ᵣ²) k = 2 cosh(r/2) − K(r)/2 − Σ_{n≥2} Λ(n)/√n · δ_{log n},

con K(r)>0 el núcleo de Lévy de P47. Esto se obtiene multiplicando la transformada al corte por 9/4+t² y pasando localmente al límite: el símbolo m aporta −K/2 fuera del origen, la corrección m♯−m aporta exp(−r/2), y la densidad del peine continuo aporta exp(r/2). Los átomos de los primos sólo disminuyen el lado derecho. Sea r_j=4 log j. Si k(r_j)≤M eventualmente, aumentar M hasta que sea no negativo. En una celda [l,h]=[r_j,r_{j+1}] la barrera

    V(r)=M+cosh(h/2)(r−l)(h−r)

domina los extremos y satisface (9/4−∂²)V≥2cosh(r/2). Por el principio del máximo débil en el intervalo, k≤V (equivalentemente usar el núcleo de Green de Dirichlet positivo para la medida diferencia). El exceso sobre M es a lo sumo cosh(h/2)(h−l)²/4, uniformemente acotado: cosh(h/2)≤(j+1)² y h−l≤4/j. Así el control de las muestras implica una cota superior finita en toda la semirrecta.

**Cierre de la equivalencia.** Si vale el signo, 038 da k(r)≤k(0) para toda r y en particular en las muestras. Recíprocamente, la desigualdad aritmética en las muestras da una cota eventual k(r)≤M′ por los dos pasos anteriores. El argumento de Landau de 038 se aplica a M′−k igual que a k(0)−k: cambiar la constante sólo cambia su Laplace por un múltiplo de 1/z. Quedan excluidos los polos en Re z>0 y se obtiene el signo por el criterio de Weil. La equivalencia no prueba la desigualdad aritmética para todos los j. Comprobar una lista finita de cuartas potencias tampoco basta.

**Interpolación puramente aritmética.** La reducción de la semirrecta a cuartas potencias también se obtiene sin distribuciones. Con y=x^(−3), el lado izquierdo de la desigualdad es P(y)=Σ(1−n³y)₊Λ(n)/n². Es convexo por ser suma localmente finita de partes positivas de funciones afines con coeficientes no negativos. Por tanto P queda debajo de la cuerda entre y_{j+1}=(j+1)^(−12) e y_j=j^(−12). El término de comparación F(y)=S₂−(3/2)y^(1/3) tiene segunda derivada y^(−5/3)/3. En esa celda su cuerda supera F a lo sumo en ||F″||∞(y_j−y_{j+1})²/8=O(j²⁰ j^(−26))=O(j^(−6)). Los errores admisibles en ambos extremos son asimismo O(j^(−6)), que es O(√y) uniformemente en la celda. Así P(y)≤F(y)+C√y en las muestras implica la misma desigualdad con otra constante en todo el intervalo. Éste es el paso elemental en el que se usa el signo de Λ.

Cotejo dirigido: el generador de POWER_CONE_001 y P47 prop:sharp son antecedentes del núcleo exponencial. Los checkpoints de la función tornillo del índice L72 usan eventos de potencias primas y otra función; no se usa su equivalencia. La fórmula de Q y el argumento de la barrera recibieron revisión independiente.

## La misma suma en potencias de cualquier exponente fijo

Sea m>0 fijo. La equivalencia del enunciado sigue siendo cierta, con los mismos pesos y la misma escala de error, al sustituir x=j⁴ por x=j^m. Para m entero arbitrariamente grande siguen siendo sumas en enteros. El exponente cuatro era suficiente para la prueba elemental por convexidad. La mejora que sigue usa la representación por ceros y por eso debe leerse como reducción analítica, fuera de una prueba exclusivamente aritmética del signo.

Sea b=3/2, w=ρ−1/2 para cada cero no trivial con multiplicidad y θ=sup Re w∈[0,1/2]. Se tiene para r≥0

    k(r)=Σ_w exp(wr)/(b²−w²).

En efecto, la factorización de Hadamard de la función entera par ξ(1/2+z), de orden uno y sin cero en z=0, da L(z)=(ξ′/ξ)(1/2+z)=Σ_{pares ±w} 2z/(z²−w²). Los factores lineales exponenciales se cancelan al emparejar y la paridad elimina cualquier término constante en L. La traza de 038 da k(0)=L(b)/b. Insertando por pares en [z k(0)−L(z)]/(z²−b²) se obtiene exactamente Σ_w 1/[(b²−w²)(z−w)] en Re z>1/2. La serie temporal propuesta converge absolutamente y localmente de manera uniforme, ya que Σ_w(1+|w|)^(−3/2)<∞ por el orden uno. Su transformada es la expresión de 038, de donde la igualdad por unicidad de Laplace.

Para 0≤h≤1, usar |exp(wh)−1|≤C min(1,|w|h)≤C√(|w|h), pues Re w≤1/2. Se obtiene la estimación que importa entre muestras:

    |k(r+h)−k(r)| ≤ C exp(θr) √h.

En r_j=m log j, las separaciones son O_m(exp(−r_j/m)). Si las muestras están acotadas superiormente, resulta en toda la semirrecta k(r)≤C_m exp(ηr) con η=max(0,θ−1/(2m)). Si θ>0, entonces η<θ. Aplicar Landau a C_m exp(ηr)−k(r), aumentando la constante en un tramo inicial. Su transformada no tiene singularidades reales en (η,∞), pues allí L es regular y el punto b es removible en la fórmula de 038. La abscisa de convergencia es a lo sumo η. En consecuencia la transformada de k es holomorfa en Re z>η, contradicción con algún polo w de L en ese semiplano. Tal polo existe por la definición de supremo si η<θ, aun cuando el supremo no se alcance. Por tanto θ=0 y vale el signo por P47. La implicación inversa se hereda de 038. La fórmula física de 039 convierte las cotas de muestras en la desigualdad finita anunciada.

El mismo argumento cuantifica qué se perdería en la malla si fallase el signo. Definir E(x)=x^(3/2)[Σ_{n≤x}(1−(n/x)³)Λ(n)/n²−S₂+3/(2x)]. Entonces E(x)=3k(log x)+O(1) uniformemente para x≥1 por la fórmula física. Para cada m fijo,

    limsup_{j→∞} log(1+max(0,E(j^m)))/log(j^m) = θ.

La cota superior sale de la serie absolutamente convergente. Si el límite superior fuese menor que θ, tomar un exponente intermedio η₁<θ que acote las muestras. La interpolación anterior acota el continuo por un múltiplo de exp(max(η₁,θ−1/(2m))r), y se repite la contradicción. Para θ=0 basta la cota superior y la no negatividad del cociente. Esta ley identifica un exponente; no determina su valor incondicionalmente. Ninguna tabla finita certifica la estimación uniforme.

## Control dentro del sandbox: límite exacto de la interpolación por convexidad

Para cada entero m>4 existen pesos aritméticos no negativos w_n para los cuales la suma de 039 con Λ reemplazada por w es *exacta* en x=j^m pero su exceso intermedio, dividido por x^(−3/2), no está acotado. Así la extensión analítica precedente no es una consecuencia de la sola positividad de los pesos.

Fijar J≥2, y_j=j^(−3m), S=(3/2)J^(−m) y F(y)=S−(3/2)y^(1/3). Sea P la interpolación lineal de F entre los y_j para j≥J, extendida por cero a y≥y_J. Es convexa decreciente, con P(0+)=S. En cada nodo y_j poner n=j^m y w_n igual al salto ascendente de P′ dividido por n; poner cero en los demás enteros. Entonces P(y)=Σ(w_n/n²)(1−n³y)₊: ambos lados tienen los mismos saltos de pendiente, son lineales entre nodos y valen cero a la derecha del último. Para cada y>0 sólo intervienen finitos términos, y al bajar y a cero la convergencia monótona da Σw_n/n²=S.

En el punto medio de cada celda, la diferencia cuerda menos F está entre el mínimo y el máximo de F″ en esa celda multiplicados por (y_j−y_{j+1})²/8. Como F″ es comparable a j^(5m) y la anchura es comparable a j^(−3m−1), el exceso dividido por √y es comparable a j^(m/2−2), que diverge. Este contramodelo prueba la optimalidad del exponente cuatro para la clase de pesos no negativos sin más restricciones. No satisface las identidades de divisores de Λ y no es un contraejemplo al signo.

El README de fase 213 restringe los mecanismos admisibles a argumentos sobre la forma explícita. Por ello la extensión a toda malla j^m mediante los ceros se registra únicamente como comparación analítica externa. El contramodelo y la interpolación en cuartas potencias son las partes elementales de este cotejo.

**También con pesos uniformemente acotados.** En cada celda gruesa [l,h] de longitud d, sumar a F un bump ε d²(min_[l,h] F″) φ((y−l)/d), con φ suave no negativa de soporte compacto en (0,1) y φ(1/2)>0. Elegir ε||φ″||∞≤1/2. Esta función modificada es convexa, coincide con F en los nodos gruesos y su segunda derivada queda entre F″/2 y 3F″/2. Interpolarla ahora linealmente en *todos* los nodos y=n^(−3), incluidos los gruesos; prolongar por cero desde y_J. Se mantiene la convexidad en el extremo porque la derivada allí, antes de la prolongación, es negativa. En cada nodo interior el salto de pendiente está acotado por el supremo de la segunda derivada en las dos celdas finas adyacentes por su longitud total: O(n⁵)O(n^(−4))=O(n). Por tanto los pesos reconstruidos por el mismo procedimiento cumplen 0≤w_n≤C_{m,J} uniformemente. La única unión con la prolongación tiene salto finito. La interpolación fina domina a la función convexa modificada y por tanto conserva al menos el exceso del bump en el punto medio grueso. La suma de pesos normalizados sigue siendo S por convergencia monótona. Incluso añadir la acotación uniforme de los pesos no salva el argumento de interpolación en mallas m>4.

## Umbral de falsificación con constante explícita y sesgo de los cuadrados

Escribir E(x)=(3/2)√x−Q(x), k₀=k(0), S₂=−ζ′(2)/ζ(2) y c♯=1/2−γ_E−log(2π). Una consecuencia necesaria del signo, en **cada** x>1, es

    E(x) ≤ 3k₀ − (c♯+1/2−S₂)x^(−3/2) − R(x),

    R(x)=x^(−1/2)[z atanh z + (log(1−z²)+z²)/(2z²)],     z=1/x.

En particular, usando E(x)=x^(3/2)[Σ_{n≤x}(1−(n/x)³)Λ(n)/n²−S₂+3/(2x)], la comparación requiere una suma finita y constantes especificadas. Una violación rigurosa en un solo x certificaría una dirección negativa por 038. A la inversa, demostrar esta desigualdad para todos los x=j⁴ suficientemente grandes basta por 039. Suprimir R(x)>0 da un umbral más débil que también bastaría para falsificar el signo si se supera. No se ha observado aquí una violación certificada.

**Evaluación del término arquimediano.** Sea b=3/2 y a_k=k+1/4. En P47 prop:sharp separar fracciones simples después de dividir el símbolo por t²+b². La transformada inversa es

    H(r)=(c♯/3) exp(−br) + Σ_{k≥1} exp(−2a_k r)/(4a_k²−b²),       r>0.

El coeficiente del primer término proviene de la extensión analítica par de m♯ en ib: [ψ(2)+ψ(1/2)]/2−log π=c♯. La separación se puede hacer en sumas parciales; los coeficientes restantes son sumables y la serie de P47 dividida por t²+b² converge en L¹ por monotonía de sus sumandos no constantes e integrabilidad del límite. Como 4a_k²−b²=(2k−1)(2k+2), tres veces la serie en r=log x suma R(x) por las series de atanh y log(1−z²). Sustituir en la fórmula física de esta ronda y usar k(r)≤k₀ da el umbral.

**Qué parte del error viene de potencias propias.** Denotar por Q_p la misma expresión que Q restringiendo n a primos, con pesos log p. Para los cuadrados, al poner y=√x, los dos tramos son y^(−3)Σ_{p≤y}p²log p y y³Σ_{p>y}log(p)/p⁴. Por el teorema de los números primos θ(y)∼y y sumación parcial, cada uno tiende a 1/3. Para los exponentes k≥3, la masa acumulada de los pesos hasta t es O(t^(1/3)): por Chebyshev, el término k=3 es O(t^(1/3)) y los restantes suman O(t^(1/4)log t). Por sumación parcial sus dos contribuciones a Q son O(x^(−1/6)). Se concluye

    Q(x)−Q_p(x)=2/3+o(1).

Por tanto, si vale el signo, limsup_{x→∞} [(3/2)√x−Q_p(x)] ≤ 3k₀+2/3. En un x finito el sesgo 2/3 no sustituye un control de error para las potencias propias. La separación de cuadrados es la clásica diferencia entre ψ y θ, aquí evaluada con el peso exacto de 039. La constante libre del criterio uniforme absorbe el sesgo: el problema pendiente queda en el término de los primos. Fórmulas y alcance revisados independientemente.

NUMÉRICO. En x=j⁴ para j=2,...,32 se evaluó la suma finita con criba hasta 1 048 576, acumulando ΣΛ(n)/n² y ΣnΛ(n) con 50 cifras decimales de trabajo. El mínimo observado de umbral completo menos E fue 0.09311636354106026, en j=20. Es un control de la fórmula sin aritmética de intervalos; no se usa en la prueba ni extrapola a otros j.

## Certificado continuo del umbral en 16≤x≤2²⁰

En todo el intervalo real [16,1048576] la diferencia entre el umbral explícito anterior y E(x) es mayor que 1/1000. Esto decide el test escalar de traza en el intervalo; la positividad de la forma completa exige más.

**Cómo se cubre el continuo.** Sean l,h extremos de celda y q=max(0,E(l),E(h)). Para y=x^(−3), P convexo, F=S₂−(3/2)y^(1/3) y E=(P−F)/√y. La cuerda de P está debajo de la cuerda de F más q veces la cuerda de √y. Esta última función es cóncava. La cota del resto de interpolación de F da así, para todo l≤x≤h,

    E(x) ≤ q + h^(13/2)(l^(−3)−h^(−3))²/24.

En efecto sup F″=h⁵/3 y 1/√y≤h^(3/2). Por la serie positiva de R se cumple R(x)≤x^(−5/2)(log 2+1/2), sumando sus coeficientes por el límite de la fórmula cerrada en x=1. El certificado verifica −16(c♯+1/2−S₂)>log 2+1/2, por lo que el umbral completo en x≥16 es al menos 3k₀.

**Reproducción.** Ejecutar con Python 3 y python-flint 0.9.0 el archivo `verify_039_interval.py` de esta carpeta. La malla tiene extremos racionales (j/32)⁴ para j=64,...,1024. Una criba entera incluye cada potencia prima con su peso log p, y los extremos de los prefijos se determinan por comparación de enteros. Arb a 160 bits encierra S₂ mediante el cociente de derivada y valor de ζ en 2, los logaritmos, ambos acumulados y los errores de interpolación. En cada celda exige con desigualdades estrictas certificadas que el máximo de ambos errores extremos y cero, más el resto, quede debajo de 3k₀−1/1000. Salida reproducida: PASS, 960 celdas, 82267 potencias primas. No se presupone signo global para este cálculo.
