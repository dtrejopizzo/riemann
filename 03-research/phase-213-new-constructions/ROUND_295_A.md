# Un corte próximo a la raíz equilibra el bloque sin primo grande a precisión de raíz

Para los coeficientes b_t de 292 sea S_t(x,y)=Σ_(n≤x; P⁺(n)≤y)b_t(n). Para todo x suficientemente grande y cada t∈[1,2] existe un corte y=y(x,t) en [√(x/48),√(x/2)] tal que

    |S_t(x,y)| ≪ √x/log x.

La constante es uniforme. Por tanto el criterio unilateral integrado de 292 se puede aplicar sólo a los enteros que tienen algún primo >y(x,t). El corte depende de la frecuencia y puede tomarse como el primer salto de negativo a no negativo. El sumatorio de ese complemento continúa abierto.

**Identidad al mover el corte.** Fijar z=2 o 48, y=√(x/z), L=log x. En la serie de b_t quitar cada factor (1−u_p p^(−s))² para p>y, multiplicando por su inverso. Hasta x sólo hacen falta los términos de grado uno y dos en esos primos, pues y³>x. El término sin corrección es el sumatorio completo, O_R(x/L^R) por 294. La corrección de un primo es 2Σ_(m≤x/y)b_t(m)Σ_(y<p≤x/m)u_p. Es O_z(x/L³) por el cálculo de momentos de 294: aquí no se impone coprimalidad a m y p, y log y/L permanece acotado lejos de 0 y 1. El término de p² cuesta O_z(√x), pues su multiplicador es 3u_p² y su cofactor m≤z.

Para los dos primos distintos queda 4Σ_(m≤z)b_t(m)Σ_(y<p<q; pq≤x/m)u_pu_q. Uniformemente en t, la masa ponderada de primos sobre intervalos en [y,zy] se reemplaza por du/log u con error O_(z,R)(√x/L^R), por el PNT en las dos clases módulo 3 y sumación parcial. Aplicarlo primero a la sección vertical y luego a la horizontal de la región hiperbólica; la función de longitud ponderada de la sección es monótona y O_z(√x/L), por lo que los errores son O_z(x/L³) tomando R grande. Se puede contar pares ordenados, retirar la diagonal a coste O_z(√x) y dividir por dos. Para las dos densidades, 1/log p y 1/log q valen (2/L)(1+O_z(1/L)). El área ordenada es y²(R log R−R+1) con R=z/m. Se obtiene

    S_t(x,√(x/z)) = (8x/L²) K_t(z) + O_z(x/L³),
    K_t(z)=Σ_(m≤z) (b_t(m)/m)[log(z/m)−1+m/z].

**Dos signos certificados.** K_t(2)=log 2−1/2>0. Para z=48, el cálculo intervalar de verify_295.py encierra la misma suma finita en 1024 celdas cerradas que cubren [1,2]. Usa los valores locales exactos 1,−2u_p,u_p²,0 y aritmética de intervalos con 35 cifras. La ejecución verifica K_t(48)<−1/25 en cada celda. Por tanto el bloque pasa de negativo a positivo entre los cortes indicados, uniformemente para todo x grande.

**Tamaño real de un salto.** Al admitir p en ese rango se añaden los términos con primo máximo p. Los de exponente dos cuestan O(1), pues el cofactor es ≤48. Para el exponente uno queda b_t(p) por la suma de b_t(m) en m≤x/p con todos los primos <p. El sumatorio completo hasta x/p es O(√x/log² x) por 294. Para descontar m con un primo q≥p, observar que m/q≤x/p²≤48, y para x grande tal q es único y simple. Hay O(√x/log x) posibles q por Chebyshev, y el cofactor aporta sólo una constante absoluta. Así el salto es O(√x/log x). Empezar en el extremo inferior y elegir el primer corte con valor no negativo demuestra el enunciado. La regla es medible en t por ser una elección entre un número finito de desigualdades continuas. Tanto tomar la parte positiva como integrar conservan el presupuesto al retirar este bloque. El resultado no afirma que los dos bloques se anulen en un mismo corte.
