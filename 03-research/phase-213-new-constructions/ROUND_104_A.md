# Basta la banda prima superior a cualquier potencia fija menor que uno

Para 0<a<1 fijo, sean y=x^a y
     
    E_a(x)=Σ_{y<p≤x} log p log(x/p) − [x−y−y log(x/y)].

El signo global equivale a E_a(x)≤0 eventualmente, incluso para a arbitrariamente cercano a uno pero fijo. Bajo RH E_a(x)≤−(1.953−o(1))√x. Para a≥1/2 los conjuntos de múltiplos ≤x de los distintos primos admitidos son disjuntos. Esto localiza el criterio sin una condición auxiliar sobre la suma retirada.

**Corte en la raíz.** Para F(x)=S(x)−x se tiene exactamente F(x)−E_a(x)=F(y)+(1−a)log x [θ(y)−y]. Si a=1/2, el PNT cuantitativo clásico θ(y)−y=O(y/log³y) y su integral dan F(x)−E_a(x)=o(√x) incondicionalmente. Bajo RH la cota clásica θ(y)−y=O(√y log²(2y)) y 092 dan el mismo o(√x) para cada a<1. Así 092 prueba la implicación directa con margen.

**Vuelta para a>1/2.** La estimación incondicional del corte anterior no alcanza aquí. Poner Θ=sup Reρ y P(s)=Σ_p(log p)p^(−s). En Re s>1/2, P es meromorfa pues difiere de −ζ'/ζ en una serie holomorfa (las potencias de orden ≥2). En Mellin sobre x≥1, F y θ−id tienen transformadas respectivamente P(s)/s²−1/(s−1) y P(s)/s−1/(s−1). Ambas son regulares en s=1 por el residuo unitario de P. La escala x^a sustituye s por s/a con factor 1/a, y log x da la derivada negativa. Por tanto la transformada de E_a es regular en el semieje real s>1/2; las contribuciones del prefijo centrado son holomorfas en Re s>max(1/2,aΘ). Si Θ>1/2 hay un cero con Reρ>max(1/2,aΘ) por definición de supremo. En él sobrevive el polo de P(s)/s², incluso si Θ no se alcanza. Una cota superior eventual E_a≤0 contradice Landau para −E_a, pues forzaría holomorfía en Re s>1/2. Esta vuelta sirve también para a≤1/2 y para un techo O(√x) mediante el mismo argumento.

**Comparación.** En 075–076 el peso U(x/p) trae su propia oscilación de orden raíz, y el bloque fijo puede retener el criterio. Aquí el peso es log(x/p), el centro es la integral elemental en la banda, y el corte se mueve con x según una ley prescrita. El argumento no permite que a tienda a uno con x ni prueba la desigualdad aritmética en ninguna de estas bandas.
