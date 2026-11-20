# El prefijo creciente de capas tiene signo negativo en el corte exacto

**Estado: PROVED, con revisión independiente de multiplicidades, colas y uniformidad.**

Sean L=log x, h=log L y M_k la masa gaussiana positiva de 368 sobre los productos de exactamente k primos distintos mayores que L². Existen c>0 absoluto y x₀ tales que, para x≥x₀ y 1≤k≤c√h,

    M_(k+1) ≥ 2 M_k.

Por tanto todo prefijo de longitud final impar j≤c√h+1 tiene saldo Σ_{k=0}^j (−1)^k M_k<0. Es una desigualdad entre masas en la misma escala x.

**Agrupar por cofactor.** En M_k, el tramo |log(n/x)|>2√L cuesta en total o(1), uniformemente en k: en cada banda unitaria de u=log(x/n) hay a lo sumo e x exp(−u) enteros, usando el extremo inferior de la banda para estimar ese número. La suma de pesos allí cuesta O(x exp(−2L+O(√L))). En el resto extraer el mayor primo p y poner m=n/p, Y=x/m. Tenemos log p≥(L−2√L)/k y log Y≥log p−2√L≥L/(2k). Sea D el conjunto de cofactores que así aparecen. Para cada uno la masa de todos los p anteriores es ≤C Y/log Y: para p≤√Y se usa el decaimiento gaussiano, y para p>√Y se suman bandas unitarias en log(Y/p) usando π(t)≪t/log t y ese mismo decaimiento.

**Construcción de la capa siguiente.** Para cada m∈D elegir q primo con L²<q≤exp(L/(10k)), q∤m, y r primo en [Y/q,2Y/q], r∤m. Se cumple r>q, y descartar los a lo sumo k divisores de m deja ≫Y/(q log Y) elecciones, uniformemente por el PNT diádico. El peso de mqr es ≥min_{[−log 2,0]}g>0. Por Mertens la suma de 1/q disponible es h−O(log h+log(2k))≥h/2, pues borrar los divisores de m cuesta a lo sumo k/L². Cada producto se cuenta a lo sumo k(k+1) veces al designar q y r. Así

    M_(k+1) ≥ c₁ h/[k(k+1)] Σ_{m∈D} Y/log Y
            ≥ c₂ h/[k(k+1)] (M_k−o(1)).

El error absoluto se absorbe uniformemente: formar m con los primeros k−1 primos superiores a L², todos ≤2L² por el PNT. Entonces log m=O(kh)=o(L); tomando p∈[x/m,2x/m] se obtiene M_k≥exp((1−o(1))L). Elegir c suficientemente pequeño concluye. Para k=0, M_0=g(L)=o(1), mientras M_1→∞.

**Revisión de uniformidad.** La cota log Y≥L/(2k) y la elección q≤exp(L/(10k)) aseguran r≥Y/q≥exp(2L/(5k))>q y r>L², para todos los k del rango simultáneamente. El número de candidatos r antes de descartar divisores de m es exponencial en L/k, de modo que quitar como máximo k no altera el piso uniforme. Dado el producto final, designar los dos primos distintos q,r deja determinado m: hay a lo sumo (k+1)k designaciones, independientemente de cuántos cofactores originales pudieran producirlo. El error de cola es O(exp(−L+O(sqrt L))) tras sumar sobre todos los enteros, por lo que también lo es para cada capa. Por otra parte el piso construido cumple log M_k≥L−O(kh+h), uniformemente; así absorber el o(1) no exige escoger una subsucesión dependiente de k. Finalmente puede elegirse c con c₂/c²>4 y luego x₀ común, obteniendo el factor 2 anunciado. El caso k=0 se usa sólo para emparejar M₀−M₁; los demás pares de un prefijo impar usan las desigualdades con k par y k≤j−1≤c sqrt h.

**Alcance.** A diferencia del conteo absoluto de 374, el prefijo se puede omitir en un mayorante unilateral por tener contribución favorable. Omitirlo puede perder compensación con capas superiores. El método sólo da un factor h/k² y deja abierta la zona intermedia hasta el umbral de 374. No se reclama prioridad externa para esta desigualdad de conteo.
