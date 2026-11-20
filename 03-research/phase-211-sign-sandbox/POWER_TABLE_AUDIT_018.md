# POWER TABLE AUDIT 018 — revisión independiente

Estado: APROBADO, con alcance delimitado. Fecha: 2026-11-05. Papers intactos.

## 1. Filas N=2 y N=3

Revisado `POWER_TABLE_DESCENT_018.md` y ejecutado su verificador exacto `tools/power_table_descent_018_verify.py`: PASS. La revisión independiente de root coincide.

Para todos u≥63/2 y k≥0, ambas filas satisfacen W[f_Nk]>||f_Nk||²/8. La normalización es f_Nk(s)=s^k/(s+u)^(N+k). La recurrencia exacta es a_Nk=a_N,k+1+u²a_N+1,k. Por tanto quedan certificadas las primeras y segundas diferencias estrictas de la fila N=1; no se deducen diferencias de órdenes superiores.

Se comprobaron: monotonía archimedeana en k por covarianza; A20=d−ud′>2/5 y A30=d−ud′+u²d″/3>3/20; razones ponderadas uniformes R2=4641/11 y R3=15658881/1331 en el extremo u=63/2, decrecientes en u; costes del peine completo menores que .003 y 1/60; polar de N=2 en valor absoluto menor que .26 y polar negativo de N=3 menor que .001. Las sumas resultantes exceden 1/8. La paridad del polar de N=3 es esencial y está usada correctamente.

## 2. Presupuesto de la fila baja

Revisado y aprobado `POWER_LOW_TABLE_018.md`. No aporta un signo nuevo: cuantifica exactamente el presupuesto absoluto de la ruta E0 ya existente.

Con E0(x)=ψΛ(x)−x+1, E0(1)=0 y C_N la autocorrelación positiva decreciente, la integración por partes da

F_N=(2/C_N(0))∫₀∞ E0(eᵗ)e^(−t/2)(C_N(t)/2−C_N′(t))dt.

El término +1 y el extremo x=1 son correctos. Bajo la hipótesis |E0(x)|≤Ax^θ, 0≤θ<u+1/2, el presupuesto exacto es D_N(θ)=2+2θJ_N(θ−1/2), con J_N(b)=∫₀∞e^(bt)C_N(t)/C_N(0)dt. Se verifican D_N(0)=2; el límite 1/(1/2−θ) si θ<1/2; el crecimiento de orden √N si θ=1/2; y de orden √N(1−(θ−1/2)²/u²)^(−N) si θ>1/2. El último régimen usa las cotas bilaterales por cosh y exige θ−1/2<u. No se ha obtenido control firmado del residuo.

## 3. Falsificador exacto de la inferencia estructural

Este modelo no es la forma aritmética W. Demuestra que recurrencia, identidades de filtros y las regiones positivas certificadas no bastan, por sí solas, para completar la tabla.

Fijar u₀=63/2, ε=1/100 y la probabilidad arcoseno ν(dq)=dq/(π√(q(1−q))). Sea μ=2ν−εδ₁/₂. La forma sobre funciones racionales causales reales es

V[f]=2||f||²−εu₀|F(iu₀)|².

Con q=τ²/(u₀²+τ²) y F₁(s)=1/(s+u₀), equivale a integrar |F/F₁|² contra μ/(2u₀). Para la tabla de polo u₀,

b_Nk=∫q^k(1−q)^(N−1)dμ,   a^V_Nk=b_Nk/(2u₀^(2N−1)).

La identidad puntual q+(1−q)=1 da exactamente la misma recurrencia de Pascal y las identidades complementarias/binomiales. Las identidades geométricas convergentes también se conservan. No se postula ninguna identidad gamma o de von Mangoldt para V.

### 3.1. Márgenes de bloques y filas

En cualquier espacio racional de m≤12 polos v_j≥u₀, incluidos polos repetidos, la base de Malmquist da

Σ_j|φ̂_j(iu₀)|²=Σ_j 2v_j/(v_j²+u₀²)≤m/u₀.

Cauchy implica V[f]≥(2−εm)||f||²≥47||f||²/25. Así conserva, con margen mayor, todos los certificados de bloques de hasta doce polos, incluidos todos sus cruces y los ocho polos arbitrarios.

También conserva las tres filas completas para cualquier polo v≥u₀. Escribir q_v=u₀²/(v²+u₀²)≤1/2. La razón del término evaluado respecto de la norma es

[2u₀v/(v²+u₀²)] q_v^k(1−q_v)^(N−1)/(B(k+1/2,N−1/2)/π).

El primer factor es ≤1. Para N=1, c_k=binom(2k,k)/4^k≥2^(−k) da razón ≤1. Para N=2 el máximo es ≤2: k=0 directamente; para k≥1 el modo k/(k+1)≥1/2 permite maximizar en q=1/2. Para N=3 la cota es 8/3: k=0 directamente; k=1 da 64/27<8/3; k≥2 vuelve a maximizar en 1/2. En q=1/2 los cocientes consecutivos son (k+N)/(2k+1), con máximo en k=N−1 o N. Luego los márgenes son respectivamente 1.99, 1.98 y 2−(8/3)ε, todos mayores que los certificados reales. Las correspondientes desigualdades de diferencias se conservan.

### 3.2. Cono positivo y positividad eventual

Sea h(q)=q^k(1−q)^(N−1), d=h(1/2). Como ν≥dq/2,

∫h dν≥(1/2)∫h dq≥(1/2)(3/4)^k8^(−N),

integrando q∈[3/4,7/8]. Si k≥6N, (∫h dq)/d≥(3/2)^k/2^(2N+1)>1. Por ello el cociente del átomo negativo respecto de la masa ν es ≤2 y V/||f||²≥2−2ε=1.98. En particular se conserva todo el cono N≥2, k≥10000N² y su margen 49/50.

Para cada orden fijo, el átomo evaluado tras Q^k decrece exponencialmente, mientras la norma decrece sólo como potencia de k. La afirmación es uniforme en cualquier espacio fijo de numeradores de dimensión finita. Por tanto también se conserva la positividad eventual de cada fila/espacio fijo. No se afirma que V reproduzca el crecimiento logarítmico preciso de W.

### 3.3. Entrada interior negativa explícita

Tomar N=n+1, k=n. Entonces

4^n b_Nk=2c_n−ε,   c_n=binom(2n,n)/4^n.

La inducción c_n≤1/√(n+1) sigue de c_(n+1)/c_n=(2n+1)/(2n+2): la desigualdad cuadrada necesaria tiene diferencia 3n+2>0. Con n=201²=40401,

2c_n≤2/√40402<2/201<1/100.

Por tanto b_40402,40401<0, y también a^V_40402,40401<0. Esta entrada queda fuera de los bloques finitos y del cono certificado.

## 4. Conclusión de alcance

Filas 2 y 3: nuevo signo positivo efectivo de toda la fila. LOW_TABLE: presupuesto exacto de una ruta anterior, sin signo adicional. Modelo μ: obstrucción lógica a completar la tabla mediante sólo las identidades y regiones ya probadas; no contraejemplo a W ni a la positividad buscada. La distinción pendiente debe usar información adicional de la forma aritmética concreta. Ninguno de estos resultados certifica por sí solo una nueva ventana T.
