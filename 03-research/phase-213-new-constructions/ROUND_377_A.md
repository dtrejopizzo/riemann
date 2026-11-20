# El bloque intermedio tiene exceso positivo y compensa el prefijo

**Estado: PROVED, con revisión independiente del desplazamiento y de la obstrucción al descarte del prefijo.**

En el corte exacto de 368 sean P_j=Σ_{k≤j}(−1)^k M_k, R_{j,K}=Σ_{j<k<K}(−1)^k M_k y K=floor(L/(2h)−L/h^(3/2)) como en 374. Para cualquier j impar en el tramo de crecimiento de 375 (o de 376), uniformemente,

    R_{j,K}=−P_j(1+O(exp(−cL/h))),     R_{j,K} ≫ x/log x.

Esto impide la estrategia de pagar la zona intermedia sola con un techo unilateral de raíz. Su compensación con el prefijo es obligatoria.

**Cota para la suma entera.** En la integral de Mellin de 368 congelar z=L² a la escala de evaluación. Desplazar de 1+1/L hasta σ=1−d, d=c₀/h, entre alturas ±2√L, con c₀ absoluto pequeño. El rectángulo está estrictamente en la región libre clásica usada en 370; allí |1/ζ|≤exp(O(h²)). Para cualquier punto del rectángulo,

    log |E_z(s)| ≤ log E_z(1−d) ≪ Σ_{p≤z} p^(−1+d) ≪ exp(2hd) log log z.

La última estimación usa Mertens y la anterior que 1−d≥0.9. La gaussiana es integrable en la vertical y en los horizontales cuesta exp(−2L+O(1)); en las colas de la recta inicial el cociente E_z/ζ es una serie absolutamente convergente de coeficientes de módulo ≤1, de modo que cuesta O(L) antes de la gaussiana. Se obtiene |S(x)|≪x exp(−c₁L/h), con c₁>0 absoluto. Esta cota por sí sola tiene exponente de potencia uno.

**Comparación.** Se tiene −P_j≥M_1−M_0≫x/L por agrupación de los pares de 375 o 376 y por el PNT en [x,2x]. Por 374, el módulo del saldo para k≥K es ≤exp((1/2+o(1))L). La identidad R_{j,K}+P_j=S−Σ_{k≥K}(−1)^k M_k y las dos cotas anteriores dan |R_{j,K}+P_j|≪x exp(−c₁L/h). Dividiendo por −P_j se absorbe L en la exponencial con c<c₁. En particular hay exceso de masa par en el bloque intermedio para cada x suficientemente grande, incluso tomando j=1. La cota relativa obtenida sigue muy por encima de la precisión de raíz necesaria para el criterio 372.

**Registro de revisión y alcance de la obstrucción.** Las cotas del contorno son uniformes y el factor exp(O(h²)) se absorbe porque L/h≫h². En las colas iniciales se usa el cociente completo E_z/ζ y sus coeficientes de módulo ≤1; no se separa en dos series con costes dependientes del corte. El piso −P_j≫x/L es uniforme en todos los j admisibles; además j<K eventualmente. Por ello R_{j,K} es positivo a toda escala suficientemente grande, no sólo en una subsucesión. Aunque retirar P_j produce formalmente un mayorante para S, el bloque restante R_{j,K} no satisface ningún techo O(x^(1/2+ε)) con ε<1/2: su piso x/log x lo impide. Esto refuta ese descarte como método para cerrar el criterio, sin refutar otras agrupaciones que conserven la compensación entre prefijo y bloque.
