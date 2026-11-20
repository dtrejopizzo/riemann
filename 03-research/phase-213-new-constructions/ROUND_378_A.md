# Una capa grande en cada escala y el límite de los momentos de multiplicidad

**Estado: PROVED, con revisión independiente del piso uniforme y de la clase abstracta de la obstrucción.**

Sea L=log x, h=log L y 0<c<1/2 fijo. Para k=ceil(cL/h)+O(1), la masa M_k del corte exacto satisface log M_k=(1−c+o(1))L en **cada** x suficientemente grande, también si elegimos k par o impar a voluntad. El techo es 374. Para el piso reservamos el mayor primo.

Escribir z=L² y N=π(4z)−π(2z)≫z/h. Para todo 1≤k≤ceil(cL/h)+O(1), tomar m como producto de k−1 primos distintos entre 2z y 4z. Entonces log m≤(2c+o(1))L y Y=x/m≥exp((1−2c−o(1))L). Uniformemente hay ≫Y/L primos p∈[Y,2Y]. Cada mp tiene peso gaussiano ≥min_{[−log 2,0]}g>0, y p>4z es el único primo grande, de modo que todos los productos de esta construcción son distintos. Para k≥2 obtenemos

    M_k ≫ (x/L) binom(N,k−1)/(4z)^(k−1)
        ≥ (x/L) (C/((k−1)h))^(k−1).

Para k=1 basta el PNT en [x,2x]. El piso es ≥exp((1−c−o(1))L) simultáneamente para todas esas capas porque log(kh)≤h+O(1). En particular el limsup de 374 para una cola de cualquiera de las dos paridades es un límite.

**Consecuencia para intentos de reconstrucción por momentos.** Fijar j=floor(h)+2, d=floor(cL/h). En las capas k=j+i, 0≤i≤d, alterar las masas positivas en ±A(−1)^i binom(d,i), con A=exp((1−c−η)L), 0<η<1/2−c. El mismo piso uniforme vale hasta j+d: j=o(L/h), y su prueba sólo usa k≤(c+o(1))L/h. Como 2^d=exp(o(L)), ambas elecciones preservan la no negatividad para todo x grande. Dejan intactas las capas fuera del bloque y todos los momentos de grado <d, pues la diferencia finita de orden d anula todo polinomio de grado menor. En cambio los saldos de paridad difieren en módulo en 2 A 2^d.

Así, con sólo las masas exteriores, la no negatividad y esos momentos exactos, ningún estimador del saldo firmado tiene error absoluto de escala raíz uniforme para todas las secuencias compatibles: alguna de las dos tiene error ≥A2^d. Las perturbaciones modelan datos de capas, no nuevos conjuntos de primos. Para una prueba aritmética se pueden usar las relaciones de divisibilidad entre productos, que esta perturbación no impone. La obstrucción concierne a reconstrucción en módulo y no prueba una imposibilidad general de mayorantes unilaterales para ζ.

**Registro de revisión.** El primo reservado satisface log p≥(1−2c−o(1))L, de modo que supera 4L² uniformemente y permite recuperar m de cada producto sin multiplicidades. El PNT en [Y,2Y] es uniforme para todos los Y≥exp((1−2c−o(1))L), y el denominador log Y puede sustituirse por L para el piso. La cota de capa permanece uniforme hasta (c+o(1))L/h; por eso incluye j+d, sin identificar erróneamente j=O(h) con un O(1). Para cada paridad se toma el primer k de esa paridad no menor que el umbral, a distancia a lo sumo 1, lo que prueba el límite de las colas. Finalmente A·binom(d,i)≤exp((1−c−η+o(1))L) es o(M_(j+i)) uniformemente. La identidad de momentos es exacta para los polinomios en k=j+i, no sólo para monomios en i; ambos datos perturbados son compatibles y su separación de paridad es exactamente 2A2^d. La conclusión no requiere realizar estas secuencias como masas de enteros.
