# Hasta dónde llega la negatividad del bloque lejano

Usar D_X,N_X(H) de 162–163, y llamar F_X(H) al bloque integrado |p−q|>H. Existen constantes b,c>0 tales que, incondicionalmente, si

    X exp(−b log X/log log X) ≤ H ≤ X/log X,

entonces F_X(H)≤−cXH para X suficientemente grande. El extremo inferior es menor que X/(log X)^k para cada k fijo, aunque mayor que X^α para cada α<1 fijo. El avance sobre 162 es que la distancia relativa puede decrecer a esta tasa.

**Suma suavizada.** Para U(x)=Σ_q Λ(q)K(x/q) vale la fórmula
    U(x)=−Σ_ρ mρ B(ρ)x^ρ+O(x^(−1/4)).
Aquí se suman ceros distintos. Mover la inversión de B(s)(−ζ'/ζ)(s) a Re s=−1/4 como en 156 y 160. No quedan polos reales en la tira: B es entera y B(1)=0. El crecimiento polinómico en horizontales buenas y la cota del producto de uniformes de 160 dan convergencia absoluta y uniforme de Σ mρ |B(ρ)|. Más precisamente la cola por encima de altura T cuesta O(exp(−c₁√T)) para T grande por el conteo de ceros y el decaimiento del producto, absorbiendo factores polinomiales.

La región clásica libre de ceros de De la Vallée Poussin da β≤1−a/log(3+|γ|) para alguna a>0. Tomar T=(log x)². En los ceros bajos se gana exp(−c₂ log x/log log x) al acotar x^β; en los altos la cola de coeficientes gana exp(−c₁ log x). Por 161 pasar de U a S, la suma sobre primos simples, cuesta O(√x). Así |S(x)|≤C x exp(−b log x/log log x), para b>0 que se puede disminuir. En [X,2X] se conserva esta cota con X y eventualmente una constante mayor. Como F_X(H)=∫₁² S(Xv)²dv−D_X−N_X(H), el minorante N_X(H)≥c₀XH de 163 domina el cuadrado uniformemente en el rango indicado. Esto prueba el techo negativo sin suponer RH.

**Qué significaría llevarlo a potencias fijas.** Sea Θ el supremo de las partes reales de los ceros no triviales. Para 0<α<1 y H=X^α:

- Si α>2Θ−1, entonces F_X(H)≤−cXH eventualmente. En efecto, la fórmula absoluta anterior da directamente U=O(x^Θ) y también S=O(x^Θ) pues Θ≥1/2.
- Si α<2Θ−1, entonces F_X(H)>0 para infinitas escalas diádicas. Si fuera eventualmente ≤0, 163 daría ∫₁² S(Xv)²dv=O(X^(1+α)log X). Por Cauchy–Schwarz diádico el Mellin de S sería holomorfo en Re s>(1+α)/2. Existe un cero a la derecha por definición de Θ, y el más a la derecha de esa misma ordenada conserva un polo en el integrando de 162. Contradicción.

No se decide el caso de igualdad. Con la convención de añadir el extremo 1 al conjunto de exponentes que dan negatividad eventual, el ínfimo es exactamente 2Θ−1. En particular demostrar el signo distante para un único exponente fijo α<1 ya obligaría a una franja libre de ceros de anchura (1−α)/2 junto a Re s=1. El resultado incondicional sólo usa la región clásica de anchura decreciente con la altura. No se debe tratar la transición a H polinomial como una mejora rutinaria del recorte.
