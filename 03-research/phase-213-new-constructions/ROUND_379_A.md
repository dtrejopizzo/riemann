# Signo de todo el sector con un único primo por encima de una segunda escala

**Estado: PROVED, con revisión independiente del producto de Laplace y de los errores para cada a fijo en (0,1).**

Con L=log x, z=L², b=L^a, y=exp b y 0<a<1 fijo, restringir S de 368 a los enteros con exactamente un factor primo >y. Los demás factores primos pueden formar cualquier subconjunto de (z,y]. Entonces el saldo del sector satisface

    S_uno ∼ −J (x/L) ∏_{z<p≤y}(1−1/p) ∼ −J (x/L) log z/b,
    J=∫ exp(−u)g(u)du.

En particular la compensación se efectúa aquí entre todas las multiplicidades pequeñas simultáneamente, para cada x grande. 378 usaba sólo un intervalo de primos del cofactor y un conteo absoluto en una capa prescrita.

**Separación del primo grande.** Escribir n=mp, p>y, con m divisor del producto de primos de (z,y]. El signo es −μ(m). Para Y=x/m vale Σ_p g(log(Y/p))≪Y para todo Y>0 por suma diádica sobre todos los enteros. En m>exp(L/2) se pierde por tanto O(x exp(−L/(2b)+O(log L))) incluso en módulo: insertar (m/exp(L/2))^(1/b) en la suma recíproca y usar ∏(1+p^(−1+1/b))≤exp(O(log L)) por Mertens. Este error es menor que el principal.

Si m≤exp(L/2), limitar a |u|=|log(Y/p)|≤√L cuesta O(Y exp(−cL)) en módulo, por el mismo conteo diádico. Allí p>y automáticamente para x grande. El PNT clásico con resto relativo O(exp(−c√L)) reemplaza la suma por

    Y ∫_{|u|≤√L} exp(−u)g(u)/(L−log m−u) du

con error O(Y exp(−c'√L)). En efecto, integrar por partes contra π(t)−li(t) en [Y exp(−√L),Y exp(√L)]; los términos de borde y la integral se acotan usando ∫exp(−u)|g'(u)|du<∞. Sumar los errores sobre m cuesta un factor exp(O(log L)).

**Mantener el signo al sumar los cofactores.** Representar el inverso del denominador D=L−log m−u mediante ∫₀^∞ exp(−Dt)dt. Se puede cortar en 1/b con error O(exp(−L/(3b))) por término pues D≥L/3. En 0≤t≤1/b extender la suma de m a todos los divisores cuesta, después de retirar el factor x, a lo sumo exp(−L/(2b)+O(log L)): aplicar otra vez Rankin a Σ_{m>exp(L/2)} m^(−1+t) con margen 1/b, usando p^(t+1/b)≤exp(2). El factor exp(ut) se integra contra exp(−u)g(u), con momentos exponenciales uniformemente acotados. Queda la integral en t con peso exp(−Lt), factor gaussiano integrado y producto

    P(t)=∏_{z<p≤y}(1−p^(−1+t)).

Es positivo y decreciente en este intervalo. Además |(log P)'|≪Σ_{p≤y} (log p)/p≪b, pues p^t≤e y p>z. Para t=v/L con v fijo resulta P(t)/P(0)→1. El factor integrado en u converge a J y está uniformemente acotado. Al cambiar a v=Lt, la dominación por C exp(−v) y L/b→∞ dan el equivalente anunciado, con el signo menos del primo distinguido. Mertens da el último equivalente. Los errores absolutos anteriores son despreciables incluso después de dividir por P(0)/L.

La parte con cero primos >y también cuesta O(x exp(−L/(2b)+O(log L))) más O(x exp(−cL)) separando m en torno a exp(L/2) y usando el peso gaussiano para m pequeño (el primer coste usa g(log(x/m))≪x/m). Por 377 la parte con al menos dos primos >y ha de compensar el saldo negativo en primer orden: el pulso completo es O(x exp(−cL/h))=o(xP(0)/L), y el sector con cero primos grandes también es o(xP(0)/L). No se obtiene el signo del residuo de esa compensación.

**Registro de revisión.** La factorización n=mp es única, pues se exige exactamente un primo >y y todos los factores son distintos. Para m≤exp(L/2) y |u|≤sqrt L, se cumple p≥exp(L/2−sqrt L)>y y D≥L/3, uniformemente en m para cada a<1 fijo. El error al cortar la integral de Laplace es O(x exp(−L/(3b)+O(log L))); al extender los cofactores en 0≤t≤1/b, Rankin con margen 1/b usa p^(t+1/b)≤e² y da el error indicado. Después de dividir por el principal, todos estos errores tienden a cero porque L/b=L^(1−a)≫log L. Para la convergencia dominada, P(t)/P(0)≤1 y |log(P(v/L)/P(0))|≪bv/L→0 para cada v fijo. El momento gaussiano completo es exp((t−1/2)²/2), acotado uniformemente en 0≤t≤1/b, y su valor en t=0 es J=exp(1/8). Esto justifica la dominación por C exp(−v), también tras el recorte en u. Las estimaciones son uniformes en los cofactores y en t; no se afirma uniformidad cuando a=a(x) tiende a1.
