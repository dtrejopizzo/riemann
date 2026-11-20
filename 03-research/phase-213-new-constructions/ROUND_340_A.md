# Un único subbloque aislado con los signos verdaderos ya exige RH

Para cada Y real grande tomar X=Y², I=(21Y/20,22Y/20], h=X^(−δ), y formar

    B_I(x)=Σ_{d,e∈I} μ(d)μ(e) η(log(x/(de))/h).

En la reducción 338 si ambas copias se restringen a I sólo queda este pulso. El siguiente enunciado **equivale a RH**: para δ=1/j, j≥5, y cada ε>0,

    ∫_[X,2X] |B_I(x)|² dx/x ≪_(δ,ε) h X^(1+ε)     para todo X grande.

**Por qué el bloque aislado ya basta.** Todos los pulsos están enteros en la ventana, como en 339. Para cada t real fijo el integral contra (x/X)^(−it) es exactamente h hatη(ht) [Σ_I μ(n)(n/Y)^(−it)]². Como hatη(0)≠0, Cauchy–Schwarz bajo la cota propuesta implica

    |Σ_I μ(n)n^(−it)| ≪ Y^((1+δ)/2+ε).

En particular t=0 basta. Para cada Z grande tomar Y=20Z/22; así se controla la suma entre 21Z/22 y Z. Telescopar en razón 21/22, con extremos reales y convención semiabierta, da la misma cota para Σ_{n≤Z}μ(n). Tomar j arbitrariamente grande y después elegir ε demuestra la cota de Mertens O_ν(Z^(1/2+ν)) para cada ν>0. Por sumación parcial 1/ζ se prolonga sin polos en Re s>1/2. El mismo razonamiento con un único t fijo no nulo controla los sumandos μ(n)n^(−it) y prolonga 1/ζ(s+it) en ese semiplano.

**Dirección bajo RH.** Sea D_I(t)=Σ_I μ(n)(n/Y)^(−it). Para todo ν>0, RH da |D_I(t)|≪_ν Y^(1/2+ν) uniformemente para |t|≤Y⁴. En detalle, para cada extremo usar el semientero v=⌊extremo⌋+1/2 y Perron truncado para 1/ζ(s+it), en abscisa 1+1/log Y y altura U=Y^10. Con coeficientes de módulo ≤1 el error es O(Y log Y/U) por separación de v y los enteros (en [v/2,2v] sumar los inversos de las distancias y fuera usar convergencia absoluta). Mover a Re s=1/2+ν/3. Bajo RH la cota de 326 da O((2+U+|t|)^γ) para cualquier γ>0 en esa franja; el lado vertical cuesta O(Y^(1/2+ν/3)(2U)^γ log U), y los horizontales O(Y(2U)^γ/U). Escoger γ suficientemente pequeño. Restar los dos prefijos y multiplicar por Y^(it).

Plancherel en log x da exactamente h²/(2π) veces la integral de |hatη(ht)|²|D_I(t)|⁴ en toda la recta. En |t|≤Y⁴ la cota anterior y la norma de hatη dan O(hY^(2+4ν)). En el resto usar |D_I|≪Y y el decaimiento de cualquier orden de hatη (hY⁴≥Y³ para estas δ). Elegir ν en función de ε.

**Decisión para el método.** Intentar demostrar la norma suficiente en 338 por separado en cada rectángulo de índices exigiría, ya en este rectángulo concreto, un resultado equivalente a RH. El argumento usa los signos exactos y una sola frecuencia en la dirección difícil, a diferencia del contraejemplo artificial 339. No establece que las distintas componentes del bloque completo deban cancelarse; muestra el coste lógico de desechar esa posibilidad. Es una aplicación del criterio clásico de Mertens, no un mecanismo independiente de cierre.
