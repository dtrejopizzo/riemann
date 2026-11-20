# Una desigualdad local en los primos equivalente al criterio de 039

Antecedente directo: [039, barrera e interpolación](ROUND_039_A.md). Allí se interpola entre muestras contiguas y se necesita una suma acumulada o una cola infinita. Aquí se resta la interpolación homogénea entre dos muestras a distancia logarítmica macroscópica. La resta anula exactamente ambos exteriores y se invierte por comparación en los índices enteros. La equivalencia final con P47 utiliza el puente analítico de 038–039.

Para j≥2 sean i=floor(j/2), m=2j, l=4 log i, r=4 log j, u=4 log m y b=3/2. Poner
A=sinh(b(u−r))/sinh(b(u−l)), B=sinh(b(r−l))/sinh(b(u−l)). Definir un peso w sobre [i⁴,m⁴] mediante

    w(t)=A(t/i⁶−i⁶/t²)          para i⁴≤t≤j⁴,
    w(t)=B(m⁶/t²−t/m⁶)          para j⁴≤t≤m⁴.

Las dos fórmulas coinciden en j⁴. El peso es positivo en el interior y vale cero fuera de la banda. El signo global equivale a que exista C finita tal que eventualmente

    Σ_{i⁴<p<m⁴} w(p) log p ≥ ∫_{i⁴}^{m⁴} w(t) dt − C,

donde p recorre sólo los primos. La integral vale exactamente (3/2)(j²−Ai²−Bm²).

**Prueba.** Escribir T f=f(r)−Af(l)−Bf(u). T anula exp(±bs) como funciones de s. Aplicado a exp(−b|s−log t|)/√t, da cero fuera de la banda. Dentro, al desarrollar los exponenciales da exactamente w(t). Integrar la identidad sobre t>0 da la fórmula de la integral, pues antes de aplicar T la integral es (3/2)exp(s/2). La identidad puntual de 039 da por tanto T E=∫w−Σ w(n)Λ(n), interpretando E en coordenada logarítmica.

La contribución de las potencias propias es O(1) uniformemente. En la banda t≥j⁴/81, y la resta de dos términos positivos da w(t)≤1/√t≤9/j². Para X=m⁴, Chebyshev da Σ_{k≥2,p^k≤X}log p=O(√X+X^(1/3)log X)=O(j²).

Si vale el signo, 038 da |k(s)|≤k(0) y 039 da E=3k+O(1) en la semirrecta. Como A,B≤1/64 (ambas distancias al centro son ≥log 16), T E queda acotado en valor absoluto.

Recíprocamente la desigualdad local implica T E≤C. Escribir E_j=E(j⁴) en coordenada original. Elegir M≥0 que domine las muestras iniciales y tal que (1−2/64)M≥max(C,0). Para ε>0 la sucesión E_j−M−εj³ tiende a menos infinito porque E_j≤(3/2)j². En la cola, su imagen por T es ≤0, ya que Ai³+Bm³≤(1/8+8)j³/64. Un máximo positivo se alcanzaría en la cola, donde su imagen sería al menos (1−A−B) veces ese máximo. La contradicción y ε↓0 dan E_j≤M. Aplicar 039.

**Obligación pendiente.** La integral es de orden j². La demostración requiere que el déficit ponderado de los primos esté acotado por una misma constante para todas las bandas. La cancelación de las colas y la eliminación de las potencias propias son exacta y a coste acotado, respectivamente. Ninguna estima ese déficit. El argumento no certifica una ventana adicional.

## Qué ocurre al usar la identidad de divisores en esta banda

En 040 un perfil fijo perdía la cola exterior del objetivo. Aquí esa cola se eliminó y por eso hacía falta revisar la cuestión. Para j par, x=j⁴, escribir w_j(xt)=x^(−1/2)W(t). El sombrero W es continuo, positivo en (1/16,16) y cero fuera. Sus únicas esquinas están en 1/16, 1 y 16. En particular W'(1/16+)>0 por la fórmula del tramo izquierdo, y W'(1/16−)=0.

Sea f un perfil continuo firmado con soporte compacto en (0,∞), fijo para todos los j pares. Escribir Df(t)=Σ_{m≥1} f(mt). La identidad Σ_{d|n}Λ(d)=log n permite evaluar el emparejamiento con Df usando log n. **Todo minorante Df≤W de esta clase pierde al menos c_f√x en la suma normalizada sobre los primos**, para todo j par suficientemente grande, con c_f>0 que puede depender de f.

En efecto, la igualdad Df=W obligaría a
f(t)=Σ_{m≥1} μ(m)W(mt) por inversión finita en cada t>0. Para cada primo p, en t₀=1/(16p) sólo m=p,16p,256p pueden aportar un salto de derivada: los tres productos mt₀ posibles son precisamente las tres esquinas. Los dos últimos coeficientes de Möbius son cero por divisibilidad por 4. Por tanto el salto de la derivada del inverso es −pW'(1/16+)≠0. Sólo interviene un número finito de términos en un entorno de cada t₀. Hay tales esquinas arbitrariamente cerca de cero, donde f tendría que ser idénticamente cero. Esto excluye la igualdad incluso para perfiles continuos sin hipótesis de derivabilidad.

Si Df≤W, la diferencia continua tiene entonces un intervalo [a,b]⊂(0,∞) donde vale al menos η>0. Los primos en [ax,bx] cuestan, en la normalización de 044, al menos η(θ(bx)−θ(ax))/√x salvo extremos, de orden √x por el teorema de los números primos. Incluso si se pide minoración sólo en las muestras primas de todos los j pares grandes, el mismo teorema y la continuidad implican la minoración global. La constante no es uniforme sobre perfiles. Quedan fuera de este descarte perfiles dependientes de la escala y métodos que evalúen el resto firmado.

Cotejo dirigido con 040, P47 thm:band (banda móvil necesaria), fase 200 SPEC_SIGN_OBJECT_003 (anuladores de la suma por Mellin) y POWER_INTERIOR_SCALE_030 (singularidades bajo dilatación de Möbius). La prueba específica de la banda usa la colisión de sus tres esquinas y la divisibilidad por 4.

Para soportes fijados [a,b] con a>0 hay, además, una pérdida *integral* uniforme en f. Denotar por g el inverso de W anterior, y elegir I=[l,h]⊂(0,a) con ∫_I|g|>0, posible por las esquinas y continuidad. Para V=W−Df≥0, B=max(b,16), la inversión de V en I vale g y sólo suma m≤B/l. Por cambio de variable y positividad,
    
    ∫_I |g| ≤ Σ_{m≤B/l} (1/m) ∫_{mI} V ≤ H_floor(B/l) ∫_{l}^{Bh/l} V.

Esta cota evita cualquier cuestión de integrabilidad en cero. La transferencia a las muestras primas es puntual en cada perfil fijo; el argumento de continuidad no da una tasa uniforme para perfiles que cambien con j.
