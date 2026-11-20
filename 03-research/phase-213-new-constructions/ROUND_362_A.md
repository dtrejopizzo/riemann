# Cola de frecuencias por debajo de la raíz con el corte móvil

Para x grande, c=1+1/log x, T=(log x)², y el mismo corredor de z de 360, sea D_z(s) la serie de Dirichlet de los coeficientes de los productos cribados de 361 (sin el multiplicador W). RH equivale a la cota O_ε(x^(1/2+ε)) para una sola integral:

    (1/(2π)) ∫_{−T}^T x^(c+it) exp(−√(1+c+it)) D_z(c+it) dt.

La raíz toma la rama de parte real positiva. El coste de TODA la cola retirada es O(x^(1−1/√2)(log x)^3), incondicional y uniforme en z. La altura T aún crece con x.

**Peso.** Para u>0 tomar w(u)=exp(−u−1/(4u))/(2√π u^(3/2)) y para u≤0 tomar cero. Su transformada de Laplace es W(s)=exp(−√(1+s)) para Re s>−1 por la integral gaussiana. Por ejemplo, tras la sustitución v=1/(2√u) se usa I(b)=∫_0^∞ exp(−v²−b²/v²)dv, con I(0)=√π/2 e I'(b)=−2I(b) por el cambio b/v, primero para b>0 real y luego por continuación. El peso es suave, de variación finita y nunca usa n>x. Además u w=w*ν con ν(du)=exp(−u)du/(2√(πu)), pues −W'/W=1/(2√(1+s)). Esta medida positiva tiene norma ponderada finita en cada abscisa σ>1/2.

**Por qué conserva el criterio.** Con este peso la identidad logarítmica de 360 conserva exactamente la misma forma, con la nueva ν. Las correcciones cuestan O_ε(A(x)x^(1/2+ε)) por la integral ponderada de ν y la suma sobre potencias superiores. Las identidades de dilatación y las dos cotas de ramas cortas y largas de 360 son independientes de la forma de w y se aplican literalmente (S_w sigue anulándose para x<1). El sentido directo bajo RH usa Mertens y sumación parcial con w de variación finita. Para el inverso, W(s)/ζ(s) es la transformada de S_w y W no se anula en Re s>1/2. Así el techo de raíz del pulso completo equivale a RH, con todos los centros y cortes de 360.

**Truncación.** En c>1 la serie es absolutamente convergente y el módulo de cada coeficiente es a lo sumo log n, por suma sobre los divisores primos de n. Por tanto |D_z(c+it)|≪(c−1)^(−2) uniformemente para 1<c≤2. La inversión de Mellin es absoluta por el decaimiento de W. La fórmula para la raíz compleja da Re √(1+c+it)≥√(|t|/2); la integral del mayorante desde T a infinito cuesta O((1+√T)exp(−√(T/2))). Como x^c=ex, sustituir T da la cota anunciada, de exponente estrictamente menor que 1/2.

**Alcance.** La integral restante se toma en la recta de convergencia absoluta. No requiere evaluar 1/ζ cerca de un cero para definirla. Falta probar cancelación dentro de |t|≤(log x)²; tomar módulos allí sólo da una cota de orden x con pérdidas logarítmicas. Este recorte es de frecuencias para el observable cribado, y no amplía el radio T del paper 47.
