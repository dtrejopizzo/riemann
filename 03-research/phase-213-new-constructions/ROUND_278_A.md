# La parte con divisores pequeños ya satisface la cota de raíz

Para el escalar E de 275–277 usar U=⌊√N⌋, Y=U/(C log²(2N)). Existe un peso real explícito B, igual a R en los enteros de la banda, con soporte [Y/2,U]. Tomar D=Y/(K log²(2N)) con K fijo suficientemente grande. Entonces incondicionalmente

    E(x)=−Σ_(l≤U/D) Σ_(D<d≤U/l) μ(d)log(d) B(ld) + O(U log⁵(2N)).

Sólo aparecen O(log⁴(2N)) valores del cofactor l en el término pendiente. El signo de 275 equivale a una COTA SUPERIOR de orden x^(1/2+ε), para cada ε>0, de la doble suma escrita sin el signo menos. La cantidad de enteros d de sus sumas interiores sigue siendo grande.

**Peso de banda.** Para y≤U multiplicar la función continua T de 276 por un corte que vale cero hasta Y/2 y uno desde Y, de orden Gevrey dos como el de 274; para y>U poner B=0. La extensión es suave en U: T(y)=w(y/x)=0 en el intervalo abierto (U,x), y T es suave a ambos lados. En [Y/2,Y] la estimación de 276 da |B|≪N^(−4) tomando C suficientemente grande desde el principio. Así ΣΛ(n)B(n)=E+O(N^(−2)), e ∫B=O(U log³(2N)) por 277.

**Distribución en progresiones.** Para todo entero k≥0 la construcción de 274 satisface

    ||B^(k)||₁ ≤ x log⁴(2N) C₁^(k+1)(k!)² Y^(−k).

En detalle, |S^(k)(t)|≪x log²(2N) C₂^(k+1)(k!)²/t^(k+1) en t≥U/4, y S es cero más abajo. En efecto en la parte de inversión hay O(x/t) sumandos en la escala d/x≤2/t; si se deriva el corte se está en t comparable con U. Lo mismo vale para los correctores por la cota de sus amplitudes. En T(y)=Σ_l S(ly) cada derivada da l^k y la suma restante cuesta Σ_(l≤2x/y)1/l. Multiplicar por el corte en y comparable con Y e integrar usando ∫_(Y/2)^U dy/y≪log(2N) da la norma indicada.

La integración por partes optimizada de 274 da |B̂(ξ)|≪x log⁴(2N) exp(−c√(Y|ξ|)). Por periodización, para cada entero 1≤d≤D y cualquier residuo a,

    |Σ_(n≡a mod d) B(n)−(1/d)∫B| ≪ N^(−5)/d.

La constante K se escoge para absorber x log⁴(2N) en la suma de frecuencias distintas de cero. El error es uniforme en a porque sus factores de fase tienen módulo uno.

**Separación aritmética.** Usar la identidad elemental Λ(n)=−Σ_(d|n)μ(d)log d. Para d≤D evaluar la progresión a=0 con la cota anterior. Sale el término −(∫B)Σ_(d≤D)μ(d)log(d)/d más error O(N^(−4)). Incluso por suma absoluta de log(d)/d, el término principal es O(U log⁵(2N)). Para d>D intercambiar las dos sumas finitas y escribir n=ld. Esto prueba el enunciado. A diferencia del equilibrio relativo de 277, la contribución de TODOS los divisores d≤D en esta identidad tiene ya una cota absoluta de raíz con factores logarítmicos. No se ha probado esa precisión para los divisores restantes. El empleo del suavizado para acortar una suma ya figura en 047; aquí se aplica a la progresión de múltiplos dentro de la banda aritmética, con la integral firmada de 277 como término principal.
