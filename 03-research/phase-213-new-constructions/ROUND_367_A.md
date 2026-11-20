# Criterio de positividad con una gaussiana fija para el producto completo cribado

Sea φ_V la densidad normal centrada de varianza V. Definir Q^*(x;z) con los mismos coeficientes doblemente cribados que 360, usando el peso fijo exp(u/2)φ_1(u), u=log(x/n). Entonces

    RH ⇔ Q^*(x;z)>0 para todo x suficientemente grande
          y todo (log x)²≤z≤4(log x)².

La anchura del peso es una sola constante. Se vuelve a usar el corredor de cortes: la implicación inversa siguiente no se afirma con el solo corte z=(log x)².

**Sentido bajo RH.** Escribir L=log x, z=kL², 1≤k≤4. El exponente de la integral es ahora K(s)=Ls+(s−1/2)²/2+log E_z(s). Como en 366 hay una silla real s₀=1/2+(log(2√k)+o(1))/log z, con K''(s₀)∼L log z, uniformemente en k. En efecto Σ log p/(p^σ−1)∼2√k e^(−c)L a σ=1/2+c/log z. El análisis local en |t|≤1/log z es el mismo: K'''=O(L log²z), B_z/L→−1/ζ(1/2) en la escala 1/√K'', y la pérdida real del producto es ≫K''t². El término principal de Q^* es por ello

    [−L/ζ(1/2)] exp(K(s₀))/√(2πK''(s₀)).

**Control que sustituye a la difusión.** Para 1/log z≤|t|≤2√L se tiene uniformemente

    log E_z(s₀)−log|E_z(s₀+it)| ≫ (L/log z) min(t²,1).

Basta la suma de p^(−s₀)(1−cos(t log p)) en z/2≤p≤z. En la variable log p el intervalo tiene longitud log 2. Si |t|≤1, quitar la parte a distancia angular <c|t| de los múltiplos de 2π deja un subintervalo de longitud absoluta fija. Si |t|≥1, dividir el intervalo en piezas de longitudes comparables a 1/|t| (usar una sola para alturas acotadas); en cada pieza de longitud angular comparable a uno queda una subpieza de longitud comparable donde la distancia angular a 2πℤ supera una constante pequeña. Así se retiene longitud total ≫z en la variable p en intervalos de longitud ≫z/(1+|t|)≫z^0.74. Por el teorema de primos en intervalos cortos cada uno contiene ≫longitud/log z primos (se pueden subdividir los más largos). La estimación anunciada da pérdida ≥c L/log³z en todo el tramo intermedio. [Guth y Maynard, corolario 1.3](https://arxiv.org/abs/2405.20552)

Bajo RH, en s₀≤Re s≤1+1/L y |Im s|≤2√L, B_z=F'−F(H+L_z) cuesta a lo sumo exp(O((log L)²)), con notación de 361. Para |t|>4 aplicar Borel–Carathéodory a log ζ en el disco centrado en 2+it de radio 3/2−(s₀−1/2)/4; no hay polos ni ceros. La parte real superior es O(log(3+|t|)) por crecimiento polinómico, y el valor central es acotado con la rama de Euler. En el disco interior hasta abscisa 1/2+(s₀−1/2)/2 resulta un techo O(log(3+|t|)/(s₀−1/2)); Cauchy en discos menores controla también la derivada de F. En alturas acotadas basta la meromorfía y la distancia a la línea crítica, usando que F es regular en 1. La suma H de potencias superiores se acota ya por su serie en Re s≥s₀ y L_z es polilogarítmico en x. Por tanto la pérdida del producto finito domina a B_z en todo el tramo intermedio. Mover el contorno hasta s₀ sin cruzar ceros bajo RH. En los horizontales a ±2√L la gaussiana aporta exp(−2L), suficiente contra x^c, E_z=exp(o(L)) y el techo anterior. Las colas en c cuestan todavía menos por convergencia absoluta. El equivalente local es así el de la suma completa, estrictamente positivo eventualmente.

**Recíproco por el semigrupo gaussiano.** Para cada corte congelado z, el observable normalizado e^(−v/2)Q^*(e^v;z) es la convolución en v de φ_1 con la medida atómica de pesos b_z(n)/√n en log n. Convolucionarlo con φ_(av−1), usando en cada evaluación v un parámetro numérico fijo av−1>0, produce exactamente e^(−v/2)Q_a(e^v;z) de 364. La identidad es absoluta por |b_z(n)|≤log n. Fijar z=2v². Para |u−v|≤v/5 se tiene u²≤z≤4u², por lo que el dato normalizado de anchura uno es positivo allí bajo la hipótesis, para v grande.

Fuera de esa zona su módulo es ≪(1+u)e^(u/2) para u≥0, por suma absoluta con el peso gaussiano (agrupar log n en intervalos unitarios). Para u<0 es O(e^u), por la cola gaussiana. Con cualquier 0<a<1/1000 fijo, la integral exterior contra φ_(av−1)(u−v) cuesta O_a(exp(−c_a v)), c_a>0: completar el cuadrado inclina el centro en a v/2+O(1), y la pérdida de la cola más próxima es al menos exp(−(1/5−a/2)²v/(2a)+O_a(1)), contra exp(v/2+av/8) y un polinomio. Se obtiene e^(−v/2)Q_a(e^v;2v²)≥−o(1).

Si existiera un cero fuera de la recta, escoger a>0 suficientemente pequeño para que viole la exclusión parabólica. La prueba de excursiones de 365 se aplica con z=2(log x)²: sólo cambia por factor fijo la estimación de variación del corte en bloques, y los factores evaluados en ρ con β>1/2 siguen entre x^(−o(1)) y x^o(1). Da valores negativos de tamaño x^(1/2+c) para algún c>0, contradiciendo la desigualdad anterior. Esto concluye la equivalencia.

**Límite.** 146 usa sinc y una varianza variable para otro observable; 363 requería módulo y cota de tamaño, y 366 positividad para parámetros difusivos tendientes a cero. Aquí se pide sólo el signo a anchura fija, para el corredor completo de cortes. La prueba del sentido directo usa RH al mover el contorno; la positividad incondicional del pulso fijo permanece abierta.
