# Un promedio positivo de Liouville con varianza uniformemente acotada

Sea U(u)=e^(−u/2)L(e^u), extendida por cero a u<0, y c=1.25·10^(−25). En cada T=log x tomar la densidad par de masa uno

    w_T(y)=Z_T^(−1) sinc(3y)^4 exp(−y²/(2cT)),     sinc(t)=sin(t)/t.

Su varianza es ≤1/12 para todo T y tiende a 1/12 al crecer T. Sin suponer RH,

    ∫ w_T(y) U(T+y) dy = 1/ζ(1/2) + O(exp(−10^(−25) T)).

En particular el promedio completo es negativo para toda escala suficientemente grande. Se puede cortar a |y|≤3√c T y renormalizar sin alterar el resultado. Se obtiene así una suma finita con pesos positivos sobre los términos de Liouville. No se da un comienzo numérico del régimen asintótico.

**Masa y dispersión.** Z_T tiende por convergencia dominada a ∫sinc(3y)^4dy>0. En la variable t, ∫sinc(t)^4dt=2π/3 por Parseval de la función triangular, mientras que ∫t²sinc(t)^4dt=π/2, usando sin⁴t=[4(1−cos2t)−(1−cos4t)]/8 y ∫(1−cos(kt))/t² dt=π|k|. Escalar por 3 da varianza 1/12. Multiplicar por una función decreciente de y² y renormalizar sólo puede reducir su media (comparar dos copias independientes); el corte simétrico tiene la misma propiedad. Por tanto ya antes del límite hay al menos 11/12 de la masa en |y|≤1.

**Control espectral del promedio.** Denotar M_T(s)=∫w_T(y)e^(sy)dy. La Fourier de sinc(3y)^4, en frecuencia angular, es integrable y se anula fuera de [−12,12] por convolución de cuatro indicadores. Al integrar la gaussiana en la representación inversa, para T grande se obtiene

    |M_T(σ+iτ)| ≪ √T exp((cT/2)(σ²−max(|τ|−12,0)²)).

Las derivadas de cualquier orden fijo obedecen la misma cota salvo un factor polinómico en T para s en un compacto fijo, por derivación de la exponencial gaussiana. M_T(0)=1 exactamente.

Como en 145 invertir la transformada R(s)=ζ(1+2s)/[(1/2+s)ζ(1/2+s)] contra exp(Ts) M_T(s) en la recta σ=.54, por Fourier y Fubini. Cortar a una altura G libre de polos entre 2.99·10¹² y 3·10¹² y desplazar hasta −1/4. En las colas derechas y en los lados horizontales el desplazamiento de 12 en la frecuencia conserva un exponente menor que −.01 antes de factores polinómicos. El borde izquierdo cuesta O(exp(−.24T)). Todo cero incluido está en la recta crítica por Z2 del paper 47 y tiene |γ|>14 por Z1. Su contribución es a lo sumo un polinomio fijo en T por exp(−cT(|γ|−12)²/2). La tasa negativa tiene magnitud mayor que 2.5·10^(−25), así que la suma finita cabe en el error enunciado, con multiplicidades permitidas. El polo real aporta exactamente 1/ζ(1/2).

Para el corte físico usar |U(T+y)|≤exp((T+y)/2) y sinc⁴≤1. El coste fuera de |y|≤3√c T es ≪√T exp((1/2+c/8)T) veces una cola normal cuyo argumento es al menos (3−√c/2)√T. Resulta O(exp(−3T)) para esta c y T grande. La masa retirada al normalizar es igualmente exponencialmente pequeña.

**Alcance.** 131 emplea sinc⁴ para eliminar errores de suelos con un peso impar y una escala aritmética aditiva. Aquí se aplica una densidad par de baja frecuencia a la variable logarítmica del promedio completo de Liouville. La gaussiana controla la transformada en la franja compleja y hace finita la media frente al crecimiento elemental de U. La varianza acotada se refiere a la distribución de escalas, no a un soporte logarítmico fijo; se conserva una cola hasta distancias proporcionales a T en la versión finita. Este peso suprime la señal no verificada en la demostración, por lo que su negatividad no implica la negatividad para el peso puramente gaussiano de 144.
