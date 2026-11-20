# Corrección explícita con ganancia de al menos orden log log N

Con la definición de R_N de 263 se tiene incondicionalmente

    liminf_(N→∞) R_N / log log N ≥ 1/15.

La construcción usa sólo coeficientes racionales antes de normalizar la corrección. Conserva exactamente cada potencia prima, incluso las superiores al corte auxiliar. No se afirma optimalidad de la constante ni del orden logarítmico iterado.

**Primera familia de filas.** Para un entero T grande, r=1−1/T, M=ceil(T(log T)²) y j≥1, tomar

    A_j=(1−r)r^j−2(1−r²)r^(2j),       F_j(m)=⌊j/m⌋.

La variación Σ|A_j| es ≤r+2r²≤3. El perfil infinito es exactamente

    Σ_j A_j F_j(m)=Σ_(l≥1)(r^(lm)−2r^(2lm))=r^m/(1+r^m).

Se sumaron dos series geométricas; la igualdad anterior vale también en m=1. La truncación j≤M descarta Σ_(j>M)j|A_j|=O((M+T)exp(−M/T))=o(1). En particular B=Σ_(j≤M)jA_j=r/(1+r)+o(1). Equilibrar el vector de pisos restando B F_1 y realizarlo con el promedio cíclico de 261 con techo M. Sale una combinación genuina de variación ≤2(3+|B|)≤7+o(1). Su valor entrópico es exactamente Σ_(j≤M) A_j j log j: cada acarreo es un defecto de la función j log j y la combinación de pisos equilibrada tiene esos coeficientes, salvo la corrección en j=1 que vale cero para esa función. Su valor factorial es Σ_(j≤M) A_j log(j!).

**Segunda familia con los mismos átomos.** En m≥2 la primera familia vale h_m=Σ_(j≤M)A_j F_j(m) (F_1=0 aquí). Poner L_t=mcm(1,...,t). La fila binom(L_t,1) en una potencia prima m vale 1_(m≤t), pues m divide L_t exactamente en ese caso. Así Σ_(t=2)^M (h_t−h_(t+1)) binom(L_t,1), entendido como combinación de acarreos, coincide en todos esos átomos con la primera familia. Su variación es ≤1/2+o(1): el perfil infinito r^m/(1+r^m) es decreciente desde menos de 1/2; la variación discreta de su error de truncación sobre m≥2 cuesta ≤Σ_(j>M)|A_j|⌊j/2⌋=o(1). Restar las dos familias da una relación exactamente nula en potencias primas de coste total ≤7.5+o(1).

**Ganancia de masa.** La coincidencia en potencias primas iguala los valores factoriales por factorización entera. La diferencia entre entropía y logaritmo factorial en cada fila binom(L_t,1) está entre 0 y 1, por (L_t−1)log(1+1/(L_t−1))≤1. La masa neta es, por tanto,

    Σ_(j≤M) A_j [j log j−log(j!)]+O(1) = (1/2)log T+O(1).

Para la igualdad final, Stirling da j log j−log(j!)=j−(1/2)log j+O(1). El término lineal suma B=O(1). La suma de A_j sin peso es r−2r²+o(1/T), incluyendo el corte, y Σ|A_j| |log(j/T)|=O(1): para j≤T se usa |A_j|≤5/T y Σ_(j≤T)log(T/j)≤T; para j>T basta |A_j|≤5 exp(−j/T)/T y log(j/T)≤j/T. Se obtiene Σ A_j log j=−log T+O(1).

**Argumentos permitidos y precio.** Para N grande elegir T=floor(log N/(log log N)^4). Entonces M log M≤log N, de modo que M y todos los L_t≤M! están dentro del límite N. Como log T/log log N→1, la masa dividida por la variación da el límite inferior anunciado. Para corregir cualquier error Δ en 262 basta escalar esta relación: el coste es a lo sumo (15+o(1))|Δ|/log log N. La cota de 263 exige al menos |Δ|/log(N+1). Todavía no hay una cota incondicional suficiente para |Δ| en la construcción del signo.

**Distinción.** 263 demostró existencia de relaciones de rendimiento creciente por compacidad y continuación de una serie de Dirichlet. Aquí dos familias explícitas se emparejan en los átomos mediante un perfil geométrico y mínimos comunes múltiplos, y la diferencia de masas se calcula por Stirling. Los mínimos comunes múltiplos se emplean sólo para el perfil decreciente; no se codifica la suma prima desconocida de 257.
