# Una fila de diferencias finitas, con signo certificado hasta el orden 2^G

Con F de 253, G=3·10¹² y S=G² definir para n entero ≥0

    b_n=Σ_(j=0)^n (−1)^j binom(n,j) F(2+j)
       =∫₁^∞ C(x)x^(−3)(1−1/x)^n dx.

Se tiene b_n>0 para TODO 0≤n≤2^G. Además el signo global equivale a b_n≥0 eventualmente, en esta única fila que empieza siempre en 2. Aquí el entero n es un orden de diferencia, no una altura verificada ni un radio T. No se evalúan por separado los 2^G órdenes.

**Tramo cubierto por derivación.** Para n≤S−2 la diferencia con paso uno es la integral de (−1)^n F^(n)(2+u₁+...+u_n) sobre el cubo unitario. Basta 253; para n=0 usar F(2)>0. Para órdenes mayores el cubo sale del intervalo de 253 y se necesita otra estimación.

**Amortiguación en el producto beta.** Dividir b_n por B(3/2,n+1)>0. Aplicando la fórmula completa de 248, incluyendo los errores menores que 50 hasta y≥1 como en 253, cada término x^z pasa a

    L_n(z)=B(2−z,n+1)/B(3/2,n+1)=∏_(j=0)^n (j+3/2)/(j+2−z).

Se justifica integrar en la serie de ceros por convergencia absoluta con peso x^(−3). El principal de cuadrados vale 4/15. Para los ceros verificados |L_n(ρ)|≤1 y cuestan en total menos de 0.094. Para un cero por encima de G, cada factor con j+1≤G tiene en el denominador al menos √2(j+1); los otros tienen al menos j+1. El producto de (j+3/2)/(j+1) es ≤exp((1+log(n+1))/2)≤2√(n+1). Así, para S−2<n≤2^G en la cola se tiene |L_n(ρ)|≤2√(n+1)2^(−G/2)<3. Se paga esta cola con menos de 3·2.01·6.4·10^(−12). Es la supresión simultánea por G factores diferentes la que permite esta extensión de órdenes.

Para 0≤z<1/2 se tiene 0<L_n(z)≤(2/(n+2))^(1/2−z), pues log(1−v)≤−v y Σ_(j=0)^n 1/(j+2−z)≥log((n+2)/2). El coste de x^z log x es L_n(z)Σ1/(j+2−z), a lo sumo L_n(z)(1+log(n+1)). Sea v=2/(n+2). Los ceros bajos de J₂ cuestan ≤0.235 v^(1/4) y los altos ≤5·6.4·10^(−12) al tener Re(ρ/2)≤1/2. Los errores acotados cuestan ≤100√v. Por la cota unilateral de 248, los exponentes impares cuestan a lo sumo

    (2/3)[v^(1/6)+v^(3/10)+(1+log(n+1))v^(5/14)/(2 log 2)].

Para n≥10^24 estos costes adicionales en conjunto son menores que 0.001 (el término con logaritmo decrece en este rango). Así b_n/B(3/2,n+1)>0.17 en el tramo nuevo.

**Por qué una sola fila decide el signo.** Por θ(x)≤2x se tiene |b_n|≤2/(n+1). Para 1<s<2 real se puede integrar la identidad binomial en (1−1/x) y obtener F(s)=Σ_(n≥0)b_n(2−s)_n/n!, con factorial ascendente. La convergencia absoluta bajo la integral se sigue del mismo mayorante para |C| en s>1. La identidad se extiende al interior de la franja de convergencia por analiticidad. Uniformemente en compactos de 0<Re s<2, Γ(n+2−s)/Γ(n+1)=n^(1−s)+O(n^(−Re s)). Por tanto

    Γ(2−s)F(s)−Σ_(n≥1)(n b_n)n^(−s)

tiene continuación holomorfa a esa franja por la serie de errores y el término de índice n=0 tratado por separado (su contribución es Γ(2−s)b₀). Si los coeficientes son eventualmente no negativos, Landau impide un polo no real de esta serie con Re s>1/2: la abscisa está a la izquierda de, o en, 1, y tal polo exigiría una singularidad real a su derecha o en su misma abscisa. Pero F es regular en toda la semirrecta real 1/2<s≤1 y tiene un polo en cada cero a la derecha por 247. Queda excluido todo cero así. Bajo RH la positividad puntual de 248 y 253 da directamente b_n>0 para todo n. El mismo argumento de Landau aplicado con signo opuesto muestra que bajo fallo hay infinitos n de cada signo.

**Antecedentes y límite.** Las transformaciones binomiales y los criterios de Hausdorff o Báez-Duarte ya figuran en el índice. La nueva estimación es el margen para la fila del baricentro de 247, a órdenes que rebasan el dominio de derivadas de 253, por el producto beta exacto. La reducción a una fila es viable por sus polos aritméticos específicos; la positividad eventual de esa fila sigue sin probarse.
