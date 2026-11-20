# Cancelación efectiva entre las clases de multiplicidad cerca de 4z

**Estado: PROVED, con revisión independiente del desfase angular uniforme, el peso terminal y el rango modular.**

En el corte de 395 sea C(Y) la suma firmada y A(Y) la masa absoluta, incluidos opcionalmente un peso λ∈[0,1] en el último primo en ambas sumas. Para κ fijo, Y=(4+κ/b)z, existen c>0 y x₀ tales que

    |C(Y)| ≤ A(Y) exp(−c L/b³)   (x≥x₀).

No se usa RH. Más generalmente, para todo 2≤m≤√L/b^(5/2) y cada residuo j módulo m, la masa con ω(n)≡j mod m es (A(Y)/m)(1+O(exp(−c b²))), uniformemente. El resultado estima el desequilibrio relativo; por sí solo no acota su exponente por 1/2.

**Caracteres.** Usar la silla positiva β de 395 sin el peso terminal; omitir o ponderar ese factor sólo cambia el producto positivo por un factor 1+O(1/L). En la suma gaussiana A el cambio también es relativo o(1): la demostración local de 395 en la misma vertical multiplica el integrando por (1+λp^(−s))/(1+p^(−s))=1+O(1/L) uniformemente; la integral del módulo en esa vertical es O(exp(H(β))/√(Lb)) por los mismos tres rangos de 395. Así se conserva el equivalente de A.

Para el carácter exp(iθω), 0<|θ|≤π, la falta de módulo logarítmica respecto del producto positivo domina

    c Σ_{2z<p≤3z} p^(−β) [1−cos(θ−t log p)].

Esto es la identidad del cuadrado del módulo de 395, en la vertical s=β+it; fuera de ese bloque la pérdida es también no negativa. Si |t|≤|θ|/(3b), para x grande la distancia angular a 2πℤ es ≥c|θ| en todo el bloque (también para |θ|=π); la pérdida es ≫(L/b)θ². Para |θ|/(3b)≤|t|≤2√L, en la banda fija de log(p/z) una proporción absoluta de longitud tiene distancia angular ≥c min(|t|,1), independientemente del desfase inicial. Se obtiene cortando el intervalo de fase en piezas de longitud angular comparable a uno para |t| grande, y quitando un entorno del múltiplo de 2π más próximo para |t| pequeño. Pueden retenerse subintervalos de longitud logarítmica ≫min(1,1/|t|); el PNT corto aplicado como en 395 los transfiere a masa prima ≫L/b. Resulta pérdida ≫(L/b)min(t²,1)≫Lθ²/b³. Para |t|>2√L la gaussiana da exp(−2L) sin usar los primos.

Al integrar y dividir por el equivalente positivo, el cociente del carácter respecto de A queda ≤O(√(Lb) exp(−c Lθ²/b³)). Para paridad θ=π, se absorbe el prefactor. Para la tabla modular, invertir por Fourier discreta: la suma de los m−1 errores relativos al principal está acotada por O(m√(Lb)exp(−c L/(m²b³))). En el rango anunciado el exponente negativo domina b² con constante fija, y log(m√(Lb))=O(b). Esto prueba la uniformidad.

**Registro de revisión.** En el segundo tramo de frecuencias, el intervalo de log(p/z) tiene longitud fija log(3/2); para |t|≤1 se quita un entorno angular de tamaño c|t|, no de tamaño fijo. Esto deja una proporción positiva de longitud aun con desfase θ−tb arbitrario y permite el piso1−cos≥ct² en un subintervalo de longitud logarítmica fija. Para |t|≥1 se usan piezas de longitud≍1/|t|; las más cortas tienen longitud en p≍z^(3/4), dentro del rango de PNT corto de395. El conteo de primos se aplica en una región donde el piso angular ya vale punto a punto, por lo que no necesita un error PNT menor queθ² cuandoθ es pequeño. La condición |t|≥|θ|/(3b) da entonces min(t²,1)≥cθ²/b² uniformemente para|θ|≤π. En el primer tramo, incluso paraθ=π el giro de tamaño≤(1+o(1))|θ|/3 mantiene distancia≥c|θ| de2πℤ.

El primo terminal está fuera de[2z,3z] para x grande; ponderarlo no altera los factores usados para la pérdida. Para los demás, incluidos el terminal conλ∈[0,1], |1+λa exp(iφ)|≤1+λa≤1+a, así que la pérdida adicional no es negativa. El equivalente de la masa ponderada difiere del no ponderado en O(1/L) relativo por el control de la integral absoluta de395. Por último, m²≤L/b^5 implica L/(m²b³)≥b², mientras log(m sqrt(Lb))=O(b). Reducir la constante c absorbe por tanto todos los prefactores y la suma de m−1 armónicos, uniformemente en m,j yλ. No se afirma una tasa de signo paraC ni un ahorro de potencia en x.

La pérdida obtenida es de orden L/b³ en el logaritmo para la paridad, mientras el superávit disponible en 395, a κ estrictamente por encima del umbral, es de orden L/b². Queda abierta la magnitud precisa y la orientación del residuo firmado.
