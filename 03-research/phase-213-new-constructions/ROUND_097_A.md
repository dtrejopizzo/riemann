# Ganancia máxima al permitir compuestos coprimos dos a dos

Para x real grande poner f(t)=log t log(x/t). Sea M(x) el máximo de Σ f(m) sobre subconjuntos de enteros en [2,x] coprimos dos a dos. Con S de 092 se tiene incondicionalmente

    M(x)−S(x)=3 S(x^(1/3))+O(x^(1/4) log² x) ∼ 3 x^(1/3).

Asignar cada m a su menor divisor primo p. La asignación es inyectiva en cada conjunto admisible. Los primos no asignados tienen coste f(p)≥0, luego para una cota superior de la ganancia basta sumar las ganancias positivas por primo. Si m es compuesto, m≥p². Para p≥x^(1/4), f decrece desde p² hasta x siempre que p²≤x. La mejora es entonces a lo sumo la parte positiva de f(p²)−f(p)=3 log p log(x^(1/3)/p). Es cero desde x^(1/3). Para p<x^(1/4) el total de todas las mejoras es O(x^(1/4)log²x), pues f≤log²x/4. Esto da el techo. Para el piso, tomar todos los primos hasta x, reemplazando p por p² exactamente cuando p<x^(1/3). El conjunto sigue siendo coprimo dos a dos y la mejora suma exactamente 3 S(x^(1/3)). Finalmente S(y)=∫₁ʸ θ(t)dt/t ∼ y por el teorema de los números primos.

**Implicación al signo.** M(x)≤x eventualmente equivale al signo global: implica S(x)≤x; en sentido inverso el margen bajo RH de 092 supera 1.95√x eventualmente y la ganancia de M es o(√x). Esto elimina la necesidad de reconocer primos en la formulación del máximo: sólo intervienen enteros, sus pesos y la condición gcd(m,n)=1 para cada par. El objetivo abierto es una cota combinatoria superior para ese máximo con la constante principal y el error unilateral necesarios. El modelo de 096 no respeta esta restricción. No se afirma que el reemplazo por cuadrados maximice exactamente para los primos pequeños.

**Solución exacta del máximo (auditoría).** Descomponer cada m en sus potencias primas exactas conserva coprimalidad y aumenta el peso si hay más de un factor, pues f(ab)=f(a)+f(b)−2 log a log b. Entonces cada primo elige su exponente independientemente, incluido cero. El incremento de k a k+1 es log p [log x−(2k+1)log p], decreciente en k. Los incrementos positivos siempre llevan a una potencia admisible p^(k+1)≤x. Por tanto

    M(x)=Σ_{k≥0}(2k+1) S(x^(1/(2k+1))).

Sólo hay O(log x) sumandos no nulos; los de k≥2 suman O(x^(1/5)log²x) usando S(y)=O(y) uniformemente para y≥2. La identidad determina un conjunto extremal para todo x, con elecciones equivalentes cuando un incremento es cero.
