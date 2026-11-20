# Separación por congruencias de los divisores cercanos y coste mínimo de rango

En el filtro de 288 fijar un primo impar P. Para d≥1 asignar la marca multiplicativa

    c(d)=(d/P^v mod P, v mod 2),    v=v_P(d),

en el grupo (ℤ/Pℤ)^× × ℤ/2ℤ. En la definición original de Q añadir el indicador c(d)c(e)=c(n) dentro de la suma; seguir poniendo cero fuera de los libres de cuadrados. Llamar Q_P al resultado. Si κ≤√3 P entonces Q_P≥μ punto por punto en n≤N y

    Σ_(n≤N)(Q_P(n)−μ(n)) ≪ √N/log log N,

con constante independiente de P. Para κ≤P se obtiene exactamente μ. Así se pueden tomar anchuras de potencia con P comparable a κ. La construcción intercambia resolución en logaritmos por resolución en clases aritméticas.

**Prueba.** Tras cambiar e por n/e, la marca exige c(d)=c(e). Con las notaciones de 288, por cancelación en el grupo se exige c(a)=c(b). Como a,b son coprimos y libres de cuadrados, la paridad de v_P impide que exactamente uno contenga P. Por tanto ambos son unidades y a≡b mod P. En sentido inverso esas dos condiciones bastan. Un término activo con a<b tiene h=b−a múltiplo de P y h√m<κ. Para κ≤√3 P sólo queda h=P y m=1 ó 2. Si m=2, a y b deben ser impares pero su diferencia P es impar. Los términos restantes tienen signo positivo y sólo afectan a n=a(a+P), una pareja no ordenada como máximo por n. Si κ≤P ni siquiera esa pareja es activa.

Para sumar el exceso usar los primos hasta z=c log N como en 288. Para p≠P hay dos clases en que p divide a(a+P); para p=P sólo hay una. El promedio del producto truncado es ≤2∏_(p≤z)(1−1/p), pues sólo se cambia a lo sumo un factor y P≥3. Acotar el resto de período como en 288 prueba la uniformidad. La marca equivale por ortogonalidad a un promedio de 2(P−1) caracteres del grupo, insertando χ(c(d))χ(c(e)) sobreline(χ(c(n))) en la expresión original. La corrección del factor P es necesaria si P divide n.

**Cuánto cuesta suprimir la barrera semiprima.** Considerar cualquier regla cuyo valor sobre n=pq con p≠q primos grandes sea

    1+(1/2)Wδ(log(p/q))⟨v_p,v_q⟩,

con vectores unitarios reales en dimensión r; se permite añadir después cualquier corrección que sólo aumente ese valor hasta mayorar μ. Las marcas iguales/distintas constituyen un caso, tomando vectores de la base ortonormal. Si C r log N≤κ≤N^(1/4), la suma de excesos del mayorante en los semiprimos es ≫κ√N/(r log²N). Por tanto para κ=N^α un rango N^o(1) no basta en esta clase de reglas.

Dividir [.6√N,.8√N] en cajas de longitud ≤κ/10 y comparable con κ como en 289. Dentro de cada caja Wδ≥1/2. Para k primos en una caja, su matriz de Gram tiene traza k y rango ≤r, de donde Σ_(i,j)⟨v_i,v_j⟩²≥k²/r. Además Σ_(i,j)⟨v_i,v_j⟩≥0, por ser el cuadrado de la norma de la suma. Como |u|≥u² para |u|≤1, la suma de las partes positivas de las entradas es ≥k²/(2r). Quitar la diagonal y pasar a pares no ordenados da ≥k²/(4r)−k/2. Sobre esos pares con producto escalar positivo el exceso forzado es al menos un cuarto del producto escalar. Sumar las cajas y aplicar Cauchy al número de primos por caja, usando sólo el PNT ordinario, da el piso indicado. Fuera de las cajas el exceso final es no negativo.

**Alcance para el signo.** Para 1≤κ≤N^(1/4) se puede escoger P impar con κ≤P≪κ+1 y obtener incluso igualdad puntual usando O(κ+1) caracteres. Se puede trabajar también con P<κ≤√3 P y un mayorante de coste de raíz. El piso de rango muestra que una compresión a pocos vectores manteniendo esa precisión requeriría un mecanismo diferente en los semiprimos. La restricción de congruencias evita el exceso de 289; no da todavía una estimación firmada de la suma de Q_P ni amplía la ventana T.
