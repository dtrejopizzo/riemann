# Para cerrar el puente bastaría el signo eventual sobre cada rayo diádico fijo

Fijar u=63/2 y llamar W_(N,k) a la forma del átomo de 205. Las siguientes afirmaciones son equivalentes:

* Todos los ceros no triviales están en la línea crítica (equivalentemente, signo global del paper 47).
* Para cada r=p/2^j>0, con p entero positivo y j≥0, W_(N,floor(rN))≥0 para todo N suficientemente grande, con umbral que puede depender de r.

En particular, para la implicación hacia el signo global no hace falta demostrar uniformidad al dejar crecer k/N. La obligación sigue siendo probar una afirmación para TODAS las pendientes diádicas, sin un techo fijo. La condición se puede debilitar a probar eventual no negatividad en los múltiplos del par (2^j,p) por cada tal par.

**Fórmula y separación.** Para z=ρ−1/2, poner x=−z². La identidad 201 para el dato real da exactamente

    W_(N,k)=Σ_ρ (u²+x)^(−N) [x/(u²+x)]^k.

En efecto F(−z)F(z) es el sumando. Los ceros críticos dan valores positivos; cada punto no real tiene su conjugado con igual multiplicidad. Para una pendiente r>0 la magnitud del sumando a k=rN es exp(N H_r(x)), donde

    H_r(x)=−log|u²+x| + r log|x/(u²+x)|.

A partir de cualquier cero fuera de la línea, su x_* es no real (Z1 excluye altura cero). Tomar r_*=|x_*|/u². En la semirrecta positiva el máximo de t^r/(u²+t)^(1+r) está en t=r u² por derivación. Como |u²+x_*|<u²+|x_*|, se tiene H_{r_*}(x_*)>sup_{t>0} H_{r_*}(t). Por continuidad la desigualdad estricta subsiste en un intervalo abierto de pendientes. Esto no presupone que ese mismo x_* maximice sobre los demás ceros.

**Elegir un solo par dominante.** Uniformemente para r en un compacto de ese intervalo, H_r(x)→−∞ cuando |γ|→∞, pues |u²+x| crece como γ² y x/(u²+x)→1. Quedan sólo finitos candidatos al máximo. Las rectas H_r(x) y H_r(y) son idénticas sólo si |u²+x|=|u²+y| y |x|=|y|. Estas distancias a dos puntos reales determinan x salvo conjugación. Evitar las finitas intersecciones entre rectas distintas y tomar un subintervalo compacto no degenerado J en el que sólo un par no real x,conj(x) maximiza, separado uniformemente del resto por una brecha η>0. El resto tras retirar ese par, en suma absoluta, es O(exp(N H_r(x)−(N−1)η)) para k/N=r∈J: extraer N−1 potencias y sumar exp(H_r(y)) sobre ceros, uniformemente finito por comparación con Σ(1+γ²)⁻¹ y Z3. El valor exp(H_r(x)) está acotado arriba y abajo en J.

**Un rayo fijo detecta el fallo.** Escribir α=arg(1/(u²+x)) y β=arg(x/(u²+x)). El cociente que define β es no real, ya que su parte imaginaria es u² Im(x)/|u²+x|². Elegir q=2^j suficientemente grande para que haya dos enteros consecutivos p,p+1 con ambas razones respecto de q en J. No pueden cumplirse simultáneamente qα+pβ=0 y qα+(p+1)β=0 módulo 2π. Fijar uno con θ=qα+pβ distinto de cero módulo 2π. En (N,k)=(q l,p l) el par dominante aporta su multiplicidad por 2 exp(NH_{p/q}(x)) cos(lθ). Para infinitos l hay cos(lθ)≤−1/2: si la rotación es periódica, algún vértice del polígono regular tiene esa propiedad y se repite; si es irracional, usar densidad en el círculo. En esa subsucesión la brecha exponencial domina el resto y W_(N,k)<0. Esto contradice el eventual signo en UN rayo diádico fijo. Bajo RH todos los sumandos son cuadrados no negativos, probando la recíproca.

**Relación con el corpus.** 017 y 205 trabajan sobre la tabla escalar exacta. Las rondas 142–143 ya usan separación de exponentes y un máximo espectral finito en una familia gaussiana diferente. Aquí el máximo sobre todo el semieje crítico se calcula exactamente para la función racional, el dato inicial fuera de la línea crea un intervalo abierto de pendientes y dos numeradores diádicos vecinos evitan resonancia en un solo rayo. No se ha demostrado el eventual signo para pendientes arbitrarias. La ronda 205 sí lo prueba simultáneamente hasta r=10¹⁹. La reformulación no demuestra que exista una pendiente con signo negativo para los ceros verdaderos.

**Patrón en cada fila bajo la hipótesis de un cero fuera de la línea.** En el mismo J, hay un entero fijo B tal que cada bloque de B enteros consecutivos k con k/N∈J contiene un valor negativo para todo N suficientemente grande. Para las fases θ+jβ existe B tal que, para todo θ inicial, alguno de 0≤j<B da cos(θ+jβ)<−1/4. Si β/(2π) es racional, el período contiene al menos tres puntos uniformes pues β no es 0 ni π; si es irracional, las traslaciones del arco abierto cubren el círculo y compacidad da una subcubierta finita. El término dominante en cada k tiene fase Nα+kβ y la brecha es uniforme en J, lo que prueba la afirmación. B y J pueden depender del espectro hipotético. Se revisó independientemente la comparación estricta y la dominancia uniforme.
