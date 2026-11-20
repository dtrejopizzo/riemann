# La escala que alcanza la región de Vinogradov–Korobov

**Estado: PROVED, con revisión independiente de la deducción y de las dos referencias primarias.**

Corolario de 370 y su auditoría. Sean L=log x, h=log L, b=log z y D=h^(5/3)(log h)^(1/3). Para una constante absoluta C suficientemente grande, los equivalentes y los signos S*<0, Q*>0 de 370 valen uniformemente en CD≤b≤L^(3/4) para x suficientemente grande.

Sólo hay dos usos de la antigua restricción b≥Ch². En el rectángulo de altura 2√L la anchura libre de ceros disponible es al menos c h^(−2/3)(log h)^(−1/3). La silla tiene d=1−α≤2h/b, mediante la misma sumación parcial real que en 370. Con C grande queda un margen de al menos la mitad de la franja. Las cotas exp(O(h²)) para F,F' se mantienen: en el disco centrado en 1+1/h+it se puede tomar radio exterior 1/h más tres cuartos de la anchura disponible e interior 1/h más cinco octavos. El argumento de Borel–Carathéodory de 370 y Cauchy conservan así margen, para |t|≥3; a alturas acotadas basta compacidad y la regularidad de F en 1. El valor de log ζ en el centro se controla por la serie de Euler, pues Re s=1+1/h. [Ford, teorema 1 y ecuación (1.1)](https://arxiv.org/html/1910.08205v5).

Para la fase, aplicar el resto clásico de Vinogradov–Korobov para θ en P≤y≤z, log P=b−1/d∼b. En AUDIT_370_PHASE el error relativo a la masa M queda acotado por

    O((1+2√L) exp(−c' b^(3/5)(log b)^(−1/5))).

La función en el exponente es creciente en este rango. En b=CD su cociente por h tiende a C^(3/5)(5/3)^(−1/5). Aumentando C el error es O(exp(−h)), menor que la pérdida mínima de orden ξ^(−2), ξ=bd=O(h). Esto completa la transferencia oscilatoria. Todos los errores gaussianos restantes de 370 dependen sólo de b/L≤L^(−1/4), de ξ→∞ y de las cotas de contorno ya verificadas. Se utiliza específicamente la estimación para θ del [teorema 1.4, ecuación (1.8), de Johnston y Yang](https://arxiv.org/html/2204.01980v2); su factor (log y)^(1.801) se absorbe reduciendo la constante positiva c' del exponente.

La mejora proviene de estimaciones externas conocidas aplicadas al observable de 368. Para el objetivo b=2h, la distancia de la silla a 1 tiende a 1/2. Ninguna mejora de las constantes en estas dos estimaciones salva esa diferencia de orden.

**Registro de revisión.** Se verificaron independientemente el ajuste d≤anchura/2, los radios anidados de Borel–Carathéodory, la sustitución del resto PNT en AUDIT_370_PHASE y el límite de b^(3/5)(log b)^(−1/5)/h. Las referencias enlazadas contienen respectivamente la región de orden (log |t|)^(−2/3)(log log |t|)^(−1/3) y el resto para θ requerido, con autores y números de enunciado correctos. No se modifica el techo superior b≤L^(3/4) ni se alcanza el corte de 368.
