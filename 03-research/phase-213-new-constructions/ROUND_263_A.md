# Corregir una unidad de masa a coste que tiende a cero

En los binomiales enteros de argumento superior n≤N de 262, llamar R_N al máximo de |Σa_i e_i| entre combinaciones que valen exactamente cero en cada potencia prima y tienen Σ|a_i|≤1. Entonces

    R_N → ∞,       R_N ≤ log(N+1).

En consecuencia, para N≥6 el coste mínimo de corregir un error escalar Δ sin alterar una sola potencia prima es exactamente |Δ|/R_N. El precio por unidad tiende a cero incondicionalmente. La demostración cualitativa no proporciona una tasa inferior de crecimiento de R_N.

**Un ejemplo concreto.** A las cuatro filas binom(p,1) para p=5,7,11,13 restar la fila binom(15,6) y dividir por cinco. La combinación tiene variación uno y es nula en cada potencia prima: binom(15,6)=5005=5·7·11·13, y cada primo del producto entra por el acarreo en m=p (todos tienen p²>15). Su masa es [Σ e(p,1)−e(15,6)]/5, entre 0.43082 y 0.43083. Con las filas de 262 se obtenía |log(1728/3125)|/3<0.198. El ejemplo sólo certifica un piso para el óptimo.

**Reformulación dual.** Sea A la matriz de acarreos con filas binomiales y columnas potencias primas. R_N es la distancia en norma suprema del vector e a la imagen de A. Es la dualidad finita de la norma cociente: los funcionales que se anulan sobre la imagen son las combinaciones buscadas. Ampliar N conserva cada testigo añadiendo ceros, pues una fila anterior tampoco carga potencias mayores; R_N es creciente en sentido no estricto. El vector de columna z_m=Λ(m) produce log binom(n,k). La cota 0≤e−log binom≤log(n+1) de 262 da el techo.

**Consecuencia de un precio que no bajara.** Si R_N estuviera acotado por C, para cada N existirían z_m tales que H(n)=Σ z_m⌊n/m⌋ cumple, con D(n)=n log n−H(n) y D(0)=0,

    |D(n)−D(k)−D(n−k)|≤C   (n≤N).

El promedio cíclico de 261 se aplica a cualquier función escalar con ese defecto. Da |D(j)−c_N j|≤2C para c_N=D(N)/N. Como D(1)=0, |c_N|≤2C. En cada argumento fijo H(n) queda acotado uniformemente en N. Las coordenadas z_(p^a) también: H(n)−H(n−1) suma z_m sobre los divisores primarios de n, de donde se recuperan sucesivamente en n=p^a. Extraer una subsucesión diagonal en todos los coeficientes y en c_N produce un H global con H(n)=n log n−cn+O(1).

**Contradicción en el origen.** Definir b(n)=H(n)−H(n−1)−log n. Es aditiva para factores coprimos y acotada, por la última estimación. En particular Σ_p sup_(a≥1)|b(p^a)|<∞: para cualquier conjunto finito de primos elegir potencias con valores positivos casi máximos, omitiendo los que no contribuyen. El valor de b en su producto acota uniformemente la suma; repetir con los valores negativos.

Para Re s>1 se tiene

    Σ b(n)n^(−s)=ζ(s) Σ_p (1−p^(−s)) Σ_(a≥1) b(p^a)p^(−as).

El factor después de ζ es holomorfo en Re s>0 por convergencia uniforme en compactos. En 0<s<1 real está acotado en módulo por Σ_p sup_a|b(p^a)|, ya que los pesos de cada serie geométrica suman p^(−s)≤1. Como ζ es regular en 0, esta continuación queda acotada al tender s a 0 por la derecha.

Por otra parte, Σ_(j≤n)b(j)=H(n)−log(n!)=(1−c)n−(1/2)log n+O(1), por Stirling. La misma fórmula para el extremo real t≥1 vale con error O(1). Por Mellin de la suma parcial la continuación anterior es

    (1−c)s/(s−1)−1/(2s)+s∫₁^∞ O(1)t^(−s−1)dt.

La última integral multiplicada por s es acotada para s real positivo. Hay por tanto divergencia al acercarse a cero, en contradicción con el cálculo por aditividad. Esto demuestra el crecimiento no acotado de R_N.

**Alcance para el signo.** Dado un ajuste en los átomos, la corrección óptima de su error concreto de masa ya tiene precio exacto, y es asintóticamente más barata que repetir una relación fija. Pero R_N≤log(N+1): esta mejora, por sí sola, no reduce el exponente de un error mayor que la raíz por una potencia fija. Permanece abierta la estimación conjunta de coste del ajuste y tamaño del error de masa para el peso de 257.
