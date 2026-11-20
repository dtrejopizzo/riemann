# Cuánto futuro admite el baricentro usando sólo los primos ya conocidos

Para cada primo p, formar D(x)=x²C(x) de 247. Si D(p)>0, llamar H(p) a la raíz positiva de

    D(p)+hD'_+(p)−θ(p)h²=0.

Poner H(p)=0 si D(p)≤0. Esta longitud se calcula con los tres momentos primos hasta p. Para 0≤h<min(H(p),p), el baricentro en p+h sigue siendo estrictamente positivo incluso si se retira cualquier subconjunto de los primos en (p,p+h]. En efecto la expresión cuadrática es exactamente lo que aportan los primos hasta p, y cada primo nuevo r aporta (p+h−r)(3r−p−h)log r≥0. Si el primo siguiente está a distancia menor que H(p), el margen en p basta para pasar ese hueco.

Sea Θ=sup Re ρ. Se tiene

    limsup_(p primo→∞) log(1+H(p))/log p = (1+Θ)/2.

En particular, SIN asumir RH hay primos arbitrariamente grandes desde los cuales el signo está garantizado en todo el tramo 0≤h≤0.41 p^(3/4), aun descartando todos los primos nuevos. Para probar RH bastaría demostrar el techo aritmético H(p)≤p^(3/4+o(1)) para todos los primos grandes. La dirección del techo importa: radios excesivamente largos también revelarían una falla del signo global.

**Cálculo del radio.** En un tramo sin entradas D'_+(x)=4Σ_(r≤x) r log r−2xθ(x). Bajo RH la estimación de 235 y sumación parcial dan D'_+(x)=O(x^(3/2)log²x); el término continuo se cancela. Por 247, 4/15−0.094+o(1)≤C(x)/√x≤4/15+0.094+o(1). Dividir la fórmula de la raíz por x^(3/4), usando θ(x)∼x, da

    H(x)/x^(3/4)=sqrt(C(x)/√x)+o(1).

Aquí se extiende la misma definición a inicios reales. En particular 0.41<H(p)/p^(3/4)<0.61 para todo primo suficientemente grande bajo RH. Sin hipótesis, para cada ε>0, la cota de 235 para θ(x)−x da D'_+=O_ε(x^(1+Θ+ε)) y C(x)=O_ε(x^(Θ+ε)) por sumación parcial con k de 247, cuya integral es cero. La fórmula cuadrática da H≪|D'_+|/θ+√(max(D,0)/θ), de exponente a lo sumo (1+Θ)/2 en el límite superior, pues Θ≤1.

**Radios inferiores cuando hay ceros a la derecha.** Para cada 1/2<d<Θ la función continua C(x)/x^d es no acotada en ambos sentidos arbitrariamente lejos. En caso de techo o piso eventual aplicar Landau a A x^d±C(x) eventualmente no negativa: su transformada tiene un polo no real a la derecha de d y ningún polo real allí por 247. Entre excursiones negativas y positivas elegir máximos locales x→∞ con C(x)≥x^d. Un primo no puede ser tal máximo: la derivada de C(x)/x^d tiene allí un salto estrictamente ascendente debido al primo entrante. Por tanto D'(x)=(2+d)D(x)/x>0 en esos máximos.

Para 0≤h≤L=x^((1+d)/2)/2, los primos hasta x aportan al menos D(x)−θ(x)L²>0, pues D(x)≥x^(2+d) y θ(x)≤2x. El primer primo p>x está a distancia O(x^(5/8)) por el teorema de intervalos cortos usado en 238. En consecuencia p−x=o(L). Congelar ahora los primos en p conserva el margen hasta x+L: el primo recién incorporado sólo aporta cantidades no negativas en ese tramo. Así H(p)≥L−(p−x) para esos primos, que dan exponente inferior (1+d)/2. Haciendo d↑Θ y juntando con el caso RH se obtiene la identidad.

**Alcance.** Se obtiene una sucesión incondicional de bloques positivos y un criterio superior sobre su robustez. La positividad de bloques excepcionales no da una inducción perpetua de primo a primo. Falta demostrar que los tres momentos parciales no producen radios de exponente superior a 3/4.
