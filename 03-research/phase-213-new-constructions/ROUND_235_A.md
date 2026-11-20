# Sólo los primeros η log q modos del orden original detectan el exponente completo

Para q primo, S_q(m)=Σ_(q<p≤2q)(log p) exp(2πim(p−q)/q). Para CADA η>0 fijo,

    lim_(q→∞) log(1+q^(−1/2) max_(1≤m≤η log q)|S_q(m)|)/log q = B,

donde B=sup |Re ρ−1/2|. Se puede tomar cualquier q entero grande en este enunciado. Si B>0, en todo intervalo diádico suficientemente alto hay entre esos modos uno con módulo ≥q^(1/2+B−o(1)). Por tanto bastaría controlar simultáneamente sólo O(log q) sumas sobre los primos en su orden verdadero en una subsucesión. La prueba no exige que el resto de modos tenga poca energía; extrae una señal suficiente enteramente dentro de la banda corta.

**Techo auxiliar.** Poner β*=1/2+B. Para cada ξ>0 se tiene |θ(x)−x|≪_ξ x^(β*+ξ), incluso si el supremo no se alcanza. En efecto, en un semientero Y con altura de truncación T de orden Y, la fórmula explícita truncada de von Mangoldt da ψ(Y)=Y−Σ_(|γ|≤T)Y^ρ/ρ+O(log²(2Y)) (puede escogerse altura buena en [Y,2Y]). En la versión con error dependiente de distancia a una potencia prima, la distancia a todo entero es ≥1/2, de modo que el término extra es O(log Y). Z3 da Σ1/|ρ|≪log²(2Y). Pasar al punto general cuesta O(log Y), y las potencias ≥2 cuestan O(√Y log² Y). Por partes contra exp(2πim(x−q)/q), la integral del continuo es cero para m entero no nulo y

    |S_q(m)| ≪_ξ (1+|m|)q^(β*+ξ).

Esto da el techo requerido y el caso B=0 con el 1 añadido.

**Filtro fijo y regularización ajustable.** Si B>0 fijar un cero derecho ρ₀=β₀+iγ₀ y 1/2<σ<β₀. Usar los factores de 230 para obtener una MEDIDA compleja μ de variación finita, masa uno y soporte en [0,1/10]. Su transformada bilateral en w anula todos los ρ−ρ₀ no nulos con Re ρ≥σ y también 1−ρ₀, añadiendo un factor finito. No usar todavía la última convolución suave de 230. Fijar ℓ=1/10. En la variable física x, sea b_n la densidad del punto 1.3 más la suma de n uniformes independientes en [−ℓ/(2n),ℓ/(2n)]. Está en [1.25,1.35] y su transformada Fourier en ciclos cumple

    |b̂_n(ξ)|≤min(1,n/(πℓ|ξ|))^n.

Poner Z_n=∫ x^(ρ₀−1)b_n(x)dx→1.3^(ρ₀−1)≠0 por concentración (varianza ℓ²/(12n)). Regularizar en variable logarítmica con f_n=μ*[exp(ρ₀v)b_n(exp v)/Z_n]. Esta función tiene integral uno y conserva todas las anulaciones. Sus derivadas hasta orden dos tienen normas L¹ polinomiales en n: al derivar la convolución de cajas se pueden derivar dos factores como diferencias de medidas de variación 2n/ℓ, y las demás cajas tienen masa uno. Cambiar de variable en un compacto y multiplicar por la exponencial conserva el techo.

El test para los primos es W_n(y)=(1+y)^(−ρ₀) f_n(log(1+y)) con y=(p−q)/q. Tiene soporte en un compacto interior de (0,1) porque 1.35 exp(1/10)<2. Su media en [0,1] es cero por el blanco 1−ρ₀. Se puede escribir como integral, contra μ(dw)/Z_n, de exp(−ρ₀w)b_n((1+y)exp(−w)). Tras trasladar y reescalar, esto da para los coeficientes de la extensión periódica

    |Ŵ_n(m)| ≤ C min(1,n/(πℓ|m|))^n,   ||W_n||∞≤Cn.

Las constantes pueden depender del cero y de σ, pero quedan fijas al crecer q.

**Señal en el test.** La fórmula explícita de 230, derivada como distribución en log x, da para los átomos dψ el principal dx y los términos −exp(ρ log x)dlog x con multiplicidades. Integrar el test W_n((x−q)/q). El continuo desaparece exactamente. El término de ρ₀ es −mult(ρ₀)q^ρ₀ por masa uno y los restantes con β≥σ se anulan. El resto es O(q^σ poly(n)): usar dos derivadas en la transformada de f_n y el conteo por intervalos unitarios; los ceros triviales suman O(poly(n)) en este compacto trasladado. Al dejar sólo primos el error es O(n√q log² q). Por tanto para n comparable a log q,

    Σ_(q<p≤2q) log p W_n((p−q)/q) = −mult(ρ₀)q^ρ₀ + o(q^β₀).

**Truncación en frecuencia.** Tomar K=floor(η log q), n=floor(πℓK/4). Para |m|>K la cota de coeficientes es ≤C(K/(4|m|))^n. Multiplicar por el techo auxiliar para S_q(m) y sumar: la cola cuesta O_ξ(q^(β*+ξ) K² 4^(−n)). Existe una constante absoluta c>0 tal que es O_ξ(q^(β*+ξ−cη)) para q grande. El cero ρ₀ puede escogerse tan cerca de β* como se quiera: elegir β*−β₀<cη/3 y ξ<cη/3 hace esta cola o(q^β₀). En los modos guardados la suma de módulos de coeficientes cuesta O(K) y el modo cero se anula. Por la fórmula anterior el máximo de |S_q(m)| para 1≤m≤K es ≳q^β₀/K, usando S_q(−m)=conjugado(S_q(m)). Llevar β₀ a β* prueba el límite inferior para TODO q grande, sin intercambiar el límite en q con una elección móvil de cero.

**Alcance.** 233 pagaba por ortogonalidad todos los modos por encima de √q. Aquí se demuestra que un hipotético fallo debe verse ya en los primeros η log q, con la forma original de las sumas. Es una reducción de dónde buscar una cota, no una estimación de cancelación de esas sumas. El número de modos sigue creciendo; no se deduce la afirmación para una lista fija.
