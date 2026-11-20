# Positividad estricta de la forma completa hasta T=6/5

El resultado principal es W_T(f)≥exp(−6000000001)||f||₂² para 0<T≤6/5. Primero se demuestra la construcción en 26/25; el último apartado verifica los parámetros de 6/5. Las dos instancias reúnen 22 comprobaciones escalares con Arb.

Con los datos incondicionales Z1–Z3 del paper 47, para toda prueba admisible de soporte [−26/25,26/25] se tiene

    W_T(f) ≥ exp(−700000001) ||f||₂².

Es una cota de demostración, de tamaño deliberadamente conservador. Se obtiene en la norma original y cubre cualquier dimensión. Se detalla la aplicación de 174 porque su mayorante polinomial sin más no paga el margen a esta altura.

**Densidad aritmética.** En la normalización dν=b(τ)dτ usar b=f_w/(2π) de (fw), para un corte par suave, monótono en u≥0, uno hasta 2.10 y cero desde 2.12. El peine tiene sólo 2,3,4,5,7,8 con suma de 2Λ(n)/√n menor que 6.343. Para el error arquimediano ∫(1−w)K cos se tiene cota global ∫_{2.10}^∞K<1.43 por la serie geométrica de K, y por partes 2K(2.10)/|τ|<1.43/|τ|. El término polar cuesta ≤8sinh(1.06)<10.2, o por partes ≤4[2cosh(1.06)−1]/|τ|<9/|τ|. Así b≥−4 por C₀>−5.373. Para |τ|≥R=5000, el menorante m(τ)≥log(|τ|/(2π))−1/|τ|−1/(2τ²) del paper da b≥1/20. La extensión es exacta hasta 2.10.

**Fuga explícita de Plancherel.** Para funciones de soporte [−T,T], la fracción de masa Fourier fuera de [−Ω,Ω], Ω=2R, es al menos η=exp(−1800(1+TR)). He aquí una cuenta para estos T,R. Para g limitada a [−Ω,Ω] en frecuencia, ||g||₂=1, usar |g^(n)|≤√(Ω/π) Ω^n por Cauchy–Schwarz. En [T,2T] hay un subconjunto de medida ≥T/2 donde |g|≤√(2/T)||g||_{L²([T,2T])}. Elegir n=ceil(64(1+ΩT)) nodos con separación T/(8n) por selección sucesiva. En [−T,T] la suma de módulos de los coeficientes de interpolación es ≤(24n)^(n−1)2^(n−1)/(n−1)! ≤256^n. El resto es ≤√(Ω/π)(3eΩT/n)^n <1/(4√T), por la fórmula integral de diferencias divididas (también para g compleja). Si la masa interior es ≥1/2, el supremo interior es ≥1/(2√T), así que la fracción de masa exterior de g es ≥256^(−2n)/32. Si la masa interior es menor la cota es inmediata. Aplicar a g la proyección de f sobre las frecuencias [−Ω,Ω]: fuera de [−T,T], g coincide con g−f, de norma total igual a la raíz de la fuga de frecuencia. Para ||f||₂=1 se deduce una fuga ≥256^(−2n)/64 ≥η, también si g=0.

**Máscara.** Fijar m=20000000, H=20000000000 y φ=1−(1−sinc(τ/H)^16)^m. Su radio de Fourier es 16m/H=.016<2.10−2T. Poner u=1−sinc(τ/H)^16 y a=8R²/(3H²). En |τ|≤R se tiene u≤a por Bernoulli y Taylor. En |τ|≥2R se tiene u≥2a: para |v|=|τ|/H≤1/10, 1−sinc²v≥v²/4 y 1−(1−v²/4)^8≥(7/4)v²; para 1/10≤|v|≤2 usar monotonía de sinc y después |sinc v|≤1/2. Reservar la mitad de b en |τ|>G/2 para la cola, siendo G=3·10¹². La densidad b restante sigue ≥1/40 fuera de R. La parte (1−φ)b restante aporta por tanto, por unidad de ∫|f̂|², al menos
    a^m(2^mη/40−4) ≥ exp(−700000000).
En efecto a>exp(−32) y m log 2−1800(1+TR)>10, por lo que el paréntesis es mayor que uno.

**Corrección espectral a la altura efectiva.** Usar la variante atómica de 172 con un corte especial χ: convolucionar la indicatriz de [−5,5] con dos uniformes de radio 1/4 y N=10¹⁰ uniformes de radio 1/N, todas de masa uno. χ=1 al menos hasta |u|=3.5 y tiene soporte en [−6.5,6.5]. Su regularidad finita (superior a cuatro derivadas) basta para las sumas y la identidad distribucional local. Para |δ|≤1/2,
    |χ̂(s+iδ)| ≤ 10 exp(6.5/2) min(1,4/|s|)^2 min(1,N/|s|)^N.
Esto se obtiene factor a factor usando para una uniforme de radio h los dos mayorantes exp(h|δ|) y exp(h|δ|)/(h|s|). Cada corrección por un cero de 172 es la diferencia de la semisuma de las dos traslaciones complejas y la traslación real, dividida por 2π. En particular su valor absoluto cuesta ≤10⁵(1+|s|)^(−2) min(1,N/|s|)^N, s=τ−γ. Sólo hay correcciones para |γ|>G por Z2.

Por Z1 y Z3 hay ≤100 log(3+|j|) ordenadas con multiplicidades por intervalo [j,j+1) de extremos enteros (restar los dos términos principales de Z3 por el teorema del valor medio y sumar sus dos errores; para |j|<3 usar Z1). Sumando el mayorante anterior se obtiene |C(τ)|≤10⁹ log(3+|τ|). Por ejemplo agrupar por l≤|τ−γ|<l+1, l entero ≥0: a lo sumo cuatro intervalos unitarios, de peso de conteo ≤400[log(3+|τ|)+log(3+l)], y sumar (1+l)^(−2). En |τ|≤G/2 se gana además el factor 100^(−N) ya que N/|τ−γ|≤1/150. Así ||C|| en esa región es menor que exp(−700000002). En |τ|>G/2,
    φ |C| ≤ m(H/|τ|)^16 10⁹ log(3+|τ|) < 1/1000,
por monotonía del mayorante y sustitución de G/2. Allí φ<1/2 y la mitad reservada de b multiplicada por 1−φ es ≥1/80, que paga todo el costo.

**Cierre en esta ventana.** La medida mezclada de 173 tiene los datos exactos en |u|<2T por el margen de soporte .016. Los átomos retenidos con peso φ son positivos. Las estimaciones anteriores dan, como desigualdad de formas tras integración (no como desigualdad puntual de densidades), el margen anunciado por Plancherel. La extensión del núcleo suave al dominio es la de 173. Esto cubre también T menores por inclusión de soportes. No hay paso a T arbitrario.

**Reproducción aritmética.** Ejecutar `python3 verify_175.py` desde esta carpeta con python-flint. Once comprobaciones escalares con bolas Arb a 160 bits pasan. El script verifica constantes y márgenes; la justificación de las desigualdades funcionales está en la prueba anterior. Los cortes w (aritmético, radio 2.12) y χ (espectral, radio 6.5) son distintos.

**Comparación de ventanas.** En el paper 47 son pertinentes thm:log5A y thm:log5W. En fase 211, ROUND_026_A, teorema 26A.2, certifica λ_A hasta 207/200 en el subespacio primitivo. Aquí se obtiene λ_W>0 en 26/25 para la forma completa de (W), que implica también λ_A>0. Se cruza el contacto (log 8)/2 y el peine considerado incluye 8=2³.

**Frontera real del corpus y ampliación a T=6/5.** El índice l.10974 registra la reproducción completa de rStation45 en ambas paridades hasta (log 11)/2≈1.1989476364. Por tanto el primer cálculo en T=1.04 es una prueba alternativa con margen explícito. El siguiente cambio de parámetros SÍ sobrepasa esa frontera:

    T=6/5, R=50000, m=180000000, H=150000000000, k=16,
    φ=1−(1−sinc(τ/H)^(2k))^m,  G=3·10¹²,  N=10¹⁰.

Usar corte aritmético uno hasta 2.46 y cero desde 2.50. Al peine anterior se suman 9 y 11: su masa total es <8.53. La cota de cola 4 exp(−2.46/2)/(1−exp(−2·2.46)) es <1.2 y también acota el coeficiente de variación de la corrección arquimediana. La masa polar es <13 y su coeficiente de variación <12. Así b≥−5 siempre y b≥1/20 más allá de R por el mismo menorante para m(τ). El radio 2km/H=.0384 es menor que 2.46−2T=.06. El corte χ de la parte espectral sigue siendo uno hasta 3.5, suficiente para la ventana ampliada.

En fuga tomar ahora Ω=100000 y n=64(1+ΩT). Los mismos cálculos dan η≥exp(−1800(1+TR)). Para u=1−sinc(v)^(2k), a=kR²/(3H²), se tiene u≤a en la banda baja; para |v|≤1/10, u≥(k/4)(1−1/400)^(k−1)v²≥(k/5)v². En |τ|≥2R eso es mayor que 2a y la parte |v|≥1/10 se cubre como antes. Además a>exp(−32) y m log 2−1800(1+TR)>10. El margen integrado tras la reserva alta es ≥a^m(2^mη/40−5)>exp(−6000000000). La corrección en baja es <exp(−6000000002); en alta el techo m(2H/G)^(2k)10⁹log(3+G) es <1/1000. El resto de la prueba no depende de esos parámetros. En consecuencia,

    W_T(f) ≥ exp(−6000000001) ||f||₂²   para todo 0<T≤6/5.

El verificador incluye las dos elecciones de parámetros. Esta ampliación es local y no implica uniformidad del procedimiento al llevar T a infinito.
