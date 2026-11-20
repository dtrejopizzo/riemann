# Dos sectores de primos simples se compensan en su media con signo

Sea P_h el observable de primos simples de 353. Para X grande fijar log y=log X/(20 log log X). Dividir P_h=U_h+V_h según que el cofactor m de pm tenga todos sus primos ≤y (incluido m=1) o al menos uno mayor que y. Entonces, uniformemente para 0<h≤1,

    ∫_[X,2X] U_h dx/x ∼ e^(−γ) X(1−e^(−h))/log y,
    ∫_[X,2X] V_h dx/x ∼ −e^(−γ) X(1−e^(−h))/log y.

La segunda equivalencia afirma una compensación real entre sectores enteros de la suma de 353. Se mide la media lineal sobre centros; el segundo momento completo queda abierto.

**Media del sector liso.** Por integración exacta de cada indicatriz, la primera integral es la integral en v de 0 a h de

    Σ_{m liso} μ(m)[θ(2Xe^(−v)/m)−θ(Xe^(−v)/m)].

Para m≤√X el teorema de los números primos con error relativo O_A((log X)^(−A)) da el término principal Xe^(−v)/m, con esa precisión relativa, uniformemente en v. La suma de los pesos absolutos 1/m sobre los m libres de cuadrados lisos cuesta O(log y) por el producto de Mertens. Para m>√X usar θ(t)≪t y la cota de Rankin con α=1/log y:

    Σ_{m>√X, liso} μ²(m)/m ≤ X^(−α/2)∏_{p≤y}(1+p^(−1+α)) ≪ (log X)^(−10) log y.

En efecto p^α−1≪α log p para p≤y y Σ_{p≤y} log p/p≪log y. La misma cola permite completar el término principal. Queda el producto exacto ∏_{p≤y}(1−1/p)∼e^(−γ)/log y. Los errores se integran sobre longitud h y 1−e^(−h) es comparable a h en todo el rango.

**Media del sector complementario.** Para el sumatorio completo B(t)=Σ_{pm≤t}μ(m)log p se tiene B(t)≪_A t/(log t)^A para cada A fijo. En efecto por la identidad de 353 es la suma de −Σ_{n≤t}μ(n)log n y −Σ_{k≥2,p^k≤t}(log p)M(t/p^k). El primer término tiene ese ahorro por la estimación clásica de Mertens M(t)≪_A t/(log t)^A y sumación parcial. En el segundo, para p^k≤√t se aplica el mismo ahorro a M(t/p^k) y se suma la serie convergente Σ_{k≥2,p}(log p)/p^k. Para p^k>√t el coste absoluto es O(t^(7/8)), pues Σ_{k≥2,p}(log p)/(p^k)^(3/4)<∞. Por tanto la media completa es ∫_0^h [B(2Xe^(−v))−B(Xe^(−v))]dv ≪_A hX/(log X)^A. Restar la primera equivalencia da la segunda.

**Decisión para la ruta.** En h=X^(−δ) con δ≤1/16, estos dos valores medios por separado ya exceden el presupuesto de norma √(hX)X^ε log X para ε suficientemente pequeño. No cabe sumar las normas de los dos sectores para cerrar 353. Un paso que conserve la compensación podría, por ejemplo, centrar ambos sectores en cada bloque diádico, pero aquí sólo se controla la media completa con ahorro logarítmico y no sus fluctuaciones ni la media a escala de raíz. Mertens y Rankin son insumos clásicos; la separación se registra como diagnóstico específico para la obligación sobre primos simples de 353.
