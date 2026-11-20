# En una subsucesión incondicional desaparecen las dos colas infinitas

Sea w el peso fijo de 275, h=∫w y φ=w/h. Existen escalas L→∞ con ΣΛ(n)φ(n/L)=L exactamente. En x=2L², el criterio de 281 se reduce a una suma FINITA de pares de índices ambos en

    V/(C log²(2N)) ≤ d,e ≤ C V log²(2N),      V=x/U ≍ L.

La reducción cuesta O(log^C(2N)) por muestra y conserva el presupuesto de raíz para la diagonal. En estas coordenadas los pares con mcd≥V exp(−√log(2N)) se pueden pagar incluso sumando sus módulos. El techo firmado para los demás pares sigue abierto.

**Existencia de las escalas.** Para Jφ(L)=ΣΛ(n)φ(n/L), la transformada de Mellin de Jφ(L)−L en L≥1 es Hφ(s)(−ζ'/ζ)(s)−1/(s−1) en Re s>1. El principal se cancela en 1. La función prolongada tiene un polo en el primer cero crítico, donde Hφ no se anula por 276, y es analítica en todo punto real s≥1/2. Por Landau ni ella en el dominio original de escalas (el déficit) ni su opuesta pueden tener signo eventual: la abscisa real de convergencia tendría que ser una singularidad real ≥1/2. Por continuidad de la suma localmente finita hay por tanto raíces arbitrariamente grandes del déficit. No se exige hipótesis sobre los demás ceros.

**Cancelación común a todas las muestras.** Para cada muestra y de 280 escribir H_d=(V/d)[α+β log(d/V)] para la cola afín de K_y(d) identificada en 282, con |α|+|β|≪log²(2N). Extender H_d por esa fórmula hasta d=1. Poner c₁=∫φ(u)log u du y a=α+β(log(L/V)+c₁). Definir

    K'_y(d)=K_y(d)−H_d
        +(V/L) Σ_(l≥1) [a−β log l] φ(ld/L).

Como ∑μ(d)/d=0 y ∑μ(d)log(d)/d=−1, la parte restada tiene suma de Möbius −Vβ. Por μ*1=δ y μ*log=Λ, la parte añadida tiene suma −(V/L)β Jφ(L); el término de δ vale cero para L>1. Por tanto en cada raíz las dos operaciones se compensan exactamente, incluso con α y β diferentes para cada muestra. Elegir x=2L² evita cualquier necesidad de invertir la función escalonada U=⌊√N⌋: basta que V/L esté acotado por arriba y por abajo.

**Localización y tamaño.** Por encima de max(4V,2x/Y,2L) el nuevo coeficiente es idénticamente cero. Para d<V, K_y(d)=0. En las sumas de compensación escribir log l=log(L/d)+log(ld/L). Los términos de integral en las periodizaciones de φ y φ log u dan exactamente H_d por la elección de a. El resto es

    O((V/d) log^C(2N) exp(−c√(L/d)))       (1≤d<V).

Ambos perfiles son de Gevrey dos y se aplica la periodización de 274; para L/d comparable con uno se ajusta la constante. Así la suma de módulos por debajo de V/(C₀ log²(2N)) es O(N^(−3)) eligiendo C₀ grande. En la banda finita retenida todos los coeficientes son O(log^C(2N)): esto se sigue directamente de la fórmula por conteo de los l≤2L/d y la cota de 281. Denotar por K'' los coeficientes tras ese corte inferior. Entonces T(y)=Σ μ(d)K''_y(d)+O(log^C(2N)) simultáneamente en todas las muestras. La variación cuadrática total de los coeficientes (suma de cuadrados sobre d e y) es O(V log^C(2N)).

**Pares restantes.** En el cuadrado finito superior de lado M≪V log²(2N), el número de pares con mcd≥H es a lo sumo Σ_(g≥H)⌊M/g⌋²≪M²/H para H≥2. Así se retira esa parte de la nueva matriz de Gram por suma absoluta a coste x^(1/2+o(1)) para H=V exp(−√log(2N)). Por 280–281 bastaría un techo x^(1/2+o(1)) para la suma firmada restante en una subsucesión de las raíces L. Recíprocamente RH lo daría en todas esas raíces. Las raíces auxiliares existen incondicionalmente; su existencia no demuestra el control de las correlaciones de Möbius.

**Cotejo.** 049 ya aislaba pares de factores próximos a √x y su barrera bilineal. 281–282 conservaban en la matriz de Gram dos colas de calibración hasta infinito. Lo que se obtiene aquí es una elección común de escalas y compensadores que convierte esa matriz específica en una matriz finita sin sacrificar las dos calibraciones ni la estructura de suma de cuadrados. La mera localización cerca de √x ya tenía antecedente.
