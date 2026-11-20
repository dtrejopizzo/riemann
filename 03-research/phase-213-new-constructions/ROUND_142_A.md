# Frecuencia de los cruces del nivel crítico

Para todo h>0 fijo y todo Z suficientemente grande hay un cruce de H(x)=Σ_{r≤x}μ(r)/√r−1/ζ(1/2) dentro de [Z,Z^(1+h)]. En particular el último cruce D admisible en 141, con 2D log D≤X, satisface log D/log X→1. El enunciado es incondicional y no presupone ceros simples ni cotas para sus residuos individuales a grandes alturas.

**Localización por un contorno finito.** Sea U(t)=H(exp t) para t≥0 y cero para t<0. Su transformada de Laplace en σ>1/2 es L(s)=1/[sζ(1/2+s)]−1/[sζ(1/2)]. Se prolonga meromórficamente y es regular en el origen. Fijar una anchura relativa 0<δ<1. Para t normal de media T y varianza cT, Iτ=E[U(t)exp(−iτt)] es la integral vertical en Re s=3/4 de

    L(s) exp(T(s−iτ)+(cT/2)(s−iτ)²) ds/(2πi).

Se deduce por Fourier de la gaussiana y Fubini usando exp(−3t/4)U(t) integrable. La parte física |t−T|>δT cuesta O(exp(−T)) al tomar c suficientemente pequeño, por |U(t)|≪exp(t/2) para t≥0 y Cauchy–Schwarz como en 115.

Los polos en la tira −2≤Re s≤3/4 son precisamente z=ρ−1/2 con multiplicidad; el primer cero trivial correspondería a −5/2. Su tasa en el promedio es

    fτ(z)=b+(c/2)(b²−(γ−τ)²),    z=b+iγ.

Para cada τ fijo se alcanza el máximo, pues |b|≤1/2. Si existe b>0, fijar uno y tomar c pequeño. Si max f₀≥0, centrar τ en la ordenada de un maximizador gana cγ²/2>0; si max f₀<0, centrar en el polo con b>0 da una tasa positiva. En un abierto de frecuencias max fτ>max(0,max f₀); elegir τ evitando los empates entre polos distintos. Para igual γ la tasa aumenta estrictamente con b cuando c<1, y para γ diferentes sólo hay una frecuencia de empate por pareja. Si todos los polos están en la recta b=0, tomar τ exactamente igual a la ordenada de uno: el máximo es único como punto, de tasa cero, y max f₀<0. En ambos casos el polo dominante puede tener multiplicidad.

Para estas dos frecuencias, 0 y τ, fijar una altura G grande libre de polos en el borde, que incluya todos los maximizadores. En la recta derecha, fuera de [−G,G], el módulo de L está uniformemente acotado por convergencia absoluta y el exponente gaussiano permite hacer el coste O(exp(−T)). Desplazar sólo el segmento finito hasta Re s=−2. Allí la tasa es a lo sumo −2+2c<−1. En los lados horizontales toda la tasa es <−1 al aumentar G. Las constantes del contorno fijo pueden depender de G; no se envía G a infinito después de tomar residuos. Para un polo de orden m el término es su exponencial por un polinomio en T de grado m−1: el coeficiente líder contiene el coeficiente principal de Laurent por (1+c(z−iτ))^(m−1)/(m−1)!, no nulo. Por unicidad del máximo y finitud, |Iτ| domina estrictamente a |I₀| y al error de las colas físicas para T grande, también cuando su tasa es cero.

Los pesos no negativos 1±cos(τt+φ), con fase elegida para obtener I₀±|Iτ|, producen promedios de signos opuestos incluso tras cortar a [(1−δ)T,(1+δ)T]. Allí U toma ambos signos. Elegir T=(1+h/2)log Z y δ con ambos extremos estrictamente dentro de [log Z,(1+h)log Z]. Se obtiene un cruce interior del escalón, con el error de salto de 141.

**Consecuencia para la banda pendiente.** Sea B la solución real de 2B log B=X. Aplicar el resultado a Z=B^(1/(1+h)). Para todo X suficientemente grande hay un cruce D entre B^(1/(1+h)) y B. Como h>0 es arbitrario y log B/log X→1, el último D(X) tiene el exponente anunciado. Por 141 la contribución normalizada de r≤D(X) es √π/(4ζ(1/2))+O(X^(−1/2+o(1))). En la obligación unilateral restante puede retenerse sólo D(X)<r≤10X log X. No se obtiene una banda de razón fija ni una cota para su suma.

**Cotejo.** 115 usa la separación de tasas gaussianas para series absolutamente sumables de exponenciales. 133 la aplica a una fórmula explícita de ψ. Para H se trabaja con el recíproco de ζ y un rectángulo fijo después de elegir la frecuencia: así no hace falta suponer que la serie de residuos de 1/ζ sea absolutamente sumable. Se responde a la falta de una tasa para los cortes en 141.
