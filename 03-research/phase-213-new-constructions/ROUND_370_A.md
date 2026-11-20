# Silla incondicional hasta cortes exp(C(log log x)²)

**Estado: PROVED, con [revisión independiente de la transferencia y del tramo local](AUDIT_370_PHASE.md).** Hay una constante absoluta C suficientemente grande para la que, con L=log x, uniformemente en

    C(log L)² ≤ b=log z ≤ L^(3/4),

los pulsos de anchura fija de 367–368 satisfacen S^*(x;z)<0 y Q^*(x;z)>0 para x suficientemente grande. El peso sigue siendo g(v)=exp(v/2)φ₁(v). No se supone RH.

**Cotejo y operación.** El antecedente inmediato es 367, «Sentido bajo RH» y «Control que sustituye a la difusión»: allí la silla queda junto a 1/2 y RH permite desplazar el contorno. Aquí se mueve la silla hacia 1 al aumentar el corte, dentro de una región libre de ceros incondicional. La banda útil de primos ya no tiene anchura logarítmica constante, sino 1/(1−α). 369 conserva el signo mediante capas de Dickman hasta b≥L^(3/4); el presente argumento cubre el rango adyacente y no usa una sustitución firmada de todas las capas. Es una extensión parcial del mismo observable, no una prueba de su signo en z=L² ni de la forma completa. El cotejo interno se limita a 367–369 y al registro de esos resultados en la Parte V del índice; no se afirma novedad histórica.

## 1. Silla y región libre

Poner F=1/ζ, E_z(s)=∏_{p≤z}(1−p^(−s))^(−1) y

    K(s)=Ls+(s−1/2)²/2+log E_z(s).

Sea α la única raíz real de K'(α)=0 en (1/2,1), y d=1−α, ξ=bd, u=L/b. El PNT clásico, por sumación parcial, da uniformemente

    ξ→∞,  e^ξ/ξ∼u,  ξ=log u+log log u+o(1),
    K''(α)∼Lb,   K'''(α+it)=O(Lb²)  para |t|≤1/b.

Para obtener estas estimaciones basta integrar las potencias primeras en log p: ∑ log p·p^(−α)∼e^(db)/d; las potencias superiores aportan O(1) a K' y O(1) a cada derivada fija. La masa principal procede de log p=b−O(1/d), y 1/d=b/ξ=o(b). La ecuación exacta y la estricta positividad de K'' justifican la existencia y unicidad; en α=1 la suma es O(b)=o(L), y en α=1/2 excede L. Además

    d=ξ/b ≤ O(1)/(C log L),   sqrt(b/L)→0.

Elegir C grande asegura que todo el rectángulo α≤Re s≤1+1/L, |Im s|≤2sqrt L queda en una versión interior de la región libre clásica Re s≥1−c/log(3+|Im s|). F es regular en s=1. Allí F y F' tienen cota exp(O((log L)²)), por las cotas usuales en la región libre, o por Borel–Carathéodory y Cauchy usando un margen ≍1/log L. Se usan únicamente la [región libre clásica y sus consecuencias PNT](https://www.ford126.web.illinois.edu/wwwpapers/zeros.pdf).

## 2. Pérdida de fase sin RH

En la banda b−1/d≤log p≤b, la masa ∑p^(−α) es ≍L/b. Tras r=d(b−log p), su medida normalizada es comparable a exp(−r)dr en [0,1]. La desigualdad elemental

    inf_θ ∫₀¹ exp(−r)[1−cos(θ−ωr)]dr ≳ min(ω²,1)

se sigue por comparación con la medida uniforme: el ínfimo de su integral es exactamente 1−|sinc(ω/2)|, que es ≳min(ω²,1). Aplicada con ω=t/d, implica

    log E_z(α)−log|E_z(α+it)| ≳ (L/b) min((t/d)²,1).

La transferencia a los primos es uniforme para 1/b≤|t|≤2sqrt L y usa sólo integración por partes. Integrar θ(v)−v contra v^(−α)(1−cos(t log v))/log v en [exp(b−1/d),exp b]. El PNT clásico da un error absoluto

    O((e^(db)/(db)) exp(−c₁sqrt b)(1+|t|)).

Los términos de borde cumplen la misma cota. Aquí e^(db)/(db)≍L/b; al elegir C grande, el error relativo es o(ξ^(−2)), menor que la pérdida relativa mínima en el tramo. No se requiere un teorema de primos en intervalos cortos ni sumar una partición oscilante.

Para |t|≤1/b, las fases de estos mismos primos tienen módulo ≤1, de donde la cota más precisa ≳Lb t². Por consiguiente, en todo el tramo 1/b≤|t|≤2sqrt L la pérdida es al menos

    c L/(bξ²) ≳ L^(1/4)/(log L)².

Este término domina (log L)² y, por tanto, el coste del factor zeta y de sus derivadas.

## 3. Equivalentes y signos

La integral local en |t|≤(log L)/sqrt(Lb) es gaussiana: el resto cúbico normalizado es O((log L)³sqrt(b/L))=o(1). Entre esa escala y 1/b domina la pérdida Lb t². En este tramo no se usa el techo global de zeta: como |t|/d≤1/ξ=o(1), se tiene |F(α+it)|=O(d), F'=O(1), |L_z|=O(L), |H|=O(1) y |B_z|=O(Ld). Así la cola local es despreciable sin comparar constantes desconocidas en exponentes de tamaño (log L)². El resto del segmento vertical queda dominado por la estimación de fase anterior. Al desplazar el contorno desde c=1+1/L hasta α no se cruza ningún cero. Los horizontales a ±2sqrt L y las colas en c son despreciables por exp(−2L), frente a exp(K(α))=exp(L−o(L)); además log E_z(α)=O(L/b)=o(L).

Para el pulso sin primo exterior el factor es F. Como α→1 por la izquierda,

    F(α)∼−d,
    S^*(x;z) ∼ F(α) exp(K(α))/sqrt(2πK''(α)) <0.

El factor varía relativamente o(1) en la escala local, pues d sqrt(Lb)=ξ sqrt(L/b)→∞. Para Q^* el factor de 367 es B_z=F'−F(H+L_z), con H la suma de potencias superiores y L_z=∑_{p≤z}log p·p^(−s). La ecuación de la silla da L_z(α)=L+O(1), mientras H(α)=O(1), F'(α)=O(1) y Ld→∞. Así

    B_z(α)∼−LF(α)∼Ld,
    Q^*(x;z) ∼ Ld exp(K(α))/sqrt(2πK''(α)) >0.

Todas las estimaciones son uniformes en el rango anunciado. La revisión independiente enlazada comprueba la pérdida de fase, su transferencia por el PNT y el control local de los dos factores. No hay cálculo numérico ni extrapolación de muestras; tampoco se proporciona un primer x explícito.

**Alcance y siguiente frontera.** Junto con 369 se obtiene S^*<0 para exp(C(log log x)²)≤z≤sqrt x. El corte de 368 es z=(log x)², cuyo logaritmo es 2log log x: queda fuera. Allí la silla sale de la región libre clásica disponible a las alturas necesarias. Reabrir exige controlar ese desplazamiento o sustituirlo por una identidad aritmética que conserve el signo; reducir C sin una nueva estimación no resuelve la diferencia de órdenes.
