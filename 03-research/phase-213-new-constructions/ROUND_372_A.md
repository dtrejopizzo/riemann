# Exponentes de las dos excursiones en el corte móvil exacto

**Estado: PROVED, deducción revisada independientemente, incluidas las hojas terminales y la cola de la convolución.**

Sea S(x)=S^*(x;(log x)²) de 368 y Θ el supremo de las partes reales de los ceros no triviales. Si Θ>1/2, para cada signo e=±1,

    limsup log(1+max(e S(x),0))/log x = Θ.

En particular para cada 1/2<σ<Θ hay valores arbitrariamente grandes con S(x)>x^σ y otros con S(x)<−x^σ. El antecedente 365 da oscilaciones en un promedio difusivo, 361 congela el corte y 368 transporta una hipótesis de signo. Aquí se transporta una cota unilateral de potencia hasta el promedio, conservando su exponente cuando a tiende a cero.

**Transferencia.** Si e S(t)≤C t^σ eventualmente, 1/2<σ<1, el árbol de 368 aplicado a e S^* deja hojas grandes acotadas por C(x/D)^σ; para las pequeñas vale la misma cota en módulo por el decaimiento gaussiano, incluso cuando el corte final se hereda. La constante de las hojas pequeñas es uniforme en el corte: basta sustituir sus coeficientes por 1 y usar que la suma gaussiana es O_(σ,t₀)(t^σ) para 0<t≤t₀. La unicidad del producto D en el árbol y sus pesos positivos dan uniformemente para (log x)²≤z≤4(log x)² el techo C' x^σ E_z(σ)=x^(σ+o(1)). La suma sobre las posibles hojas pequeñas infinitas converge absolutamente por E_z(σ)<∞. En efecto log E≪z^(1−σ)log z=o(log x).

Congelar z=2v², v=log x, y aplicar la convolución de 368 de varianza av−1. Para |u−v|≤v/5 el techo en escala e^u cuesta, tras desnormalizar, a lo sumo exp(v[σ+η+a(σ+η−1/2)²/2]) por el momento exponencial de la normal, para cada η>0 fijo y v grande. En el complemento se usa el control absoluto de colas de 368 para a suficientemente pequeño. Explícitamente |S^*(e^u;z)|≪e^u para todo u al sumar sobre todos los enteros por intervalos diádicos y usar la gaussiana. Tras convolucionar el observable normalizado y desnormalizar el resultado, la cola cuesta O(exp(v[1+a/8]) P(|N((av−1)/2,av−1)|>v/5)). Su exponente superior es

    1+a/8−(1/5−a/2)²/(2a)+o(1),

que es negativo para a suficientemente pequeño, por ejemplo 0<a<1/1000.

Elegir un cero ρ con β>σ. Cuando a→0, Re Φ_a(ρ)→β, mientras σ+a(σ−1/2)²/2→σ. Fijar a pequeño y luego η pequeño para mantener una separación estricta. Las excursiones de ambos signos del promedio difusivo sin etiqueta, demostradas al final de 368 por el cálculo de 365, contradicen ese techo. Esto prueba el menorante para cada signo, aun si Θ=1 o el supremo no se alcanza.

**Mayorante.** Para Θ<σ<1, desplazar la integral de Mellin fija de 368 a Re s=σ. Allí |E_z(s)|≤exp(o(log x)); 1/ζ tiene crecimiento polinómico uniforme en la banda entre σ y 2. Para este último hecho aplicar Borel–Carathéodory a log ζ en discos centrados en 2+it de radio exterior 2−(Θ+σ)/2 e interior 2−σ, a alturas |t|≥4: la parte real está acotada por O(log(2+|t|)) por crecimiento polinómico de ζ y el valor central es acotado. En el compacto restante 1/ζ es regular. La gaussiana hace converger la integral y anula los horizontales, de donde |S(x)|≤x^(σ+o(1)). Para Θ=1 basta el control absoluto anterior. Esto concluye la identidad.

La fórmula cuantifica la obstrucción si falla RH. Deja pendiente una cota aritmética unilateral de exponente 1/2+o(1) en este corte. La revisión independiente comprobó además los radios de Borel–Carathéodory y la separación de exponentes al escoger primero a y después η. No se requiere que Θ se alcance ni que los ceros sean simples.
