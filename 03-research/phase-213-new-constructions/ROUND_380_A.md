# Saldo del sector con exactamente dos primos grandes

**Estado: PROVED, con revisión independiente de ambas sustituciones PNT y de la suma firmada de Taylor.**

Con las definiciones de 379 y a fijo en (0,1), sea S_d el saldo con exactamente d primos mayores que y=exp(b), b=L^a. Entonces

    S_2 ∼ J x P(0) log(L/b)/L,     S_2/|S_1| ∼ log(L/b),
    P(t)=∏_{z<p≤y}(1−p^(−1+t)),   z=L².

Por tanto el sector d=2 excede en un factor divergente al de d=1. El conjunto d≥3 compensa a d=2 en primer orden, por 377 y 379. La suma de d=1,2 todavía tiene saldo positivo de exponente uno.

**Densidad semiprima.** Escribir n=mpq y contar p,q>y en orden con factor 1/2. Las diagonales cuestan O(Y/y) a Y=x/m pues g(log(Y/p²))≪Y/p². Como en 379, descartar m>exp(L/4) cuesta O(x exp(−L/(4b)+O(log L))) usando que los semiprimos distintos tienen representación no ordenada única. Para m≤exp(L/4), limitar p,q a [y,exp(2L)]: todo producto omitido excede exp(2L), con coste gaussiano O(Y exp(−cL²)) al contar por enteros. Reemplazar ambas medidas primas por dt/log t da error O(Y L² exp(−c√b)). En efecto, fijado un factor r, integrar por partes usando |π(t)−li(t)|≪t exp(−c√b) en ese intervalo. Bordes e integral de derivada cuestan O((Y/r)exp(−c√b)), ya que exp(−u)g(u) es acotada y ∫exp(−u)|g'(u)|du es finita. La masa recíproca del otro factor cuesta O(L) tanto para primos como para densidad continua. La suma sobre m amplifica estos errores por una potencia de L.

En las variables log p,log q, con D su suma, la densidad continua despojada de exp(D) es

    H(D)=(1/2)∫_b^(D−b) dv/[v(D−v)]=log((D−b)/b)/D,     D>2b.

Los extremos superiores exp(2L) son inactivos en |u|=|log Y−D|≤√L. Las colas de la integral continua son O(Y exp(−cL)) usando el mayorante H(D)≪1 para D>2b. Queda x veces la suma con peso μ(m)/m de la integral de exp(−u)g(u) H(L−log m−u).

**Sumación firmada de una densidad analítica.** En el disco complejo |D−L|≤L/2 la rama real de H se prolonga y |H|≪H(L) por su fórmula. En log m≤L/4, |u|≤√L, Taylor hasta grado N−1 tiene resto O_N(H(L)(|log m+u|/L)^N). En módulo Σ_m (1/m) exp((log m)/b)≤exp(O(log log y))≤L^C con C absoluto, por el producto finito y p^(1/b)≤e. De ahí un coste del resto O_N(H(L)L^C(b/L)^N) tras integrar la gaussiana. Elegir N fijo según a para que sea o(H(L)P(0)), pues P(0)≫L^(−1). En cada término polinómico extender a todos los m y u cuesta un error menor que cualquier potencia negativa de L por Rankin con margen 1/(2b) y por la gaussiana.

Los momentos firmados de log m son las derivadas de P en cero. En |t|≤1/b se cumple |P(t)|≪P(0) al integrar la derivada logarítmica O(b) como en 379, válida también en el disco complejo. Cauchy da |P^(i)(0)|≪_i P(0)b^i. Por tanto los términos de Taylor de orden i≥1 dan O_i(H(L)P(0)(b/L)^i), mientras el constante es J H(L)P(0). Esto prueba el equivalente. El cálculo conserva las cancelaciones del cofactor antes de comparar los dos sectores.

**Registro de revisión.** Cada reemplazo primo tiene error O((Y/r)exp(−c sqrt b)); el otro factor sólo introduce su masa recíproca, por lo que se pueden realizar las dos sustituciones secuencialmente, una contra la medida prima y otra contra la continua. Sus bordes cumplen la misma cota por sup exp(−u)g(u)<∞. La diagonal y los productos repetidos tienen coeficiente ordenado a lo sumo1, y su coste O(Y/y) es despreciable después de sumar cofactores. En el disco |D−L|≤L/2, D y D−b permanecen alejados de0, lo que fija una rama holomorfa de la fórmula de H y justifica Cauchy. Para los momentos de (log m+u)^i se expande el binomio y se usan tanto las derivadas de P como los momentos gaussianos fijos; no se sustituyen las derivadas firmadas por momentos absolutos. N es fijo una vez fijado a<1 y absorbe el factor L^C porque (b/L)^N=L^(−N(1−a)). La extensión de cada momento fuera de log m≤L/4 tiene error exp(−cL/b+O_N(log L)), incluso con los factores (log m)^i, por Rankin con margen1/(2b). Todas estas cotas son uniformes en los cofactores, sin afirmar uniformidad para a→1.
