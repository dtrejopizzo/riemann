# Medir el umbral del bloque lejano en una escala individual

En las notaciones de 162–164, para constantes fijas C₀ grande y η pequeño,

    cXH ≤ N_X(H) ≤ CXH,    C₀ log X ≤ H ≤ ηX.

La cota superior gana el logaritmo de 163 hasta separaciones de orden logarítmico. La herramienta externa al argumento de casilleros es la desigualdad clásica de criba superior de Selberg. A continuación se detalla la uniformidad necesaria en el salto.

**Criba de pares.** En p,q≤AX con A fijo, fijar h=q−p>0. Para h impar sólo interviene un par con p=2. Para h par cribar n(n+h) en n≤AX por primos ℓ≤z=X^(1/20). Las raíces módulo ℓ son ν(ℓ)=2 salvo que ℓ divida h, caso en que ν(ℓ)=1. Los conteos en un módulo libre de cuadrados l tienen error O(ν(l)), por clases individuales. La desigualdad superior de Selberg da CX/G(z) más O(z⁶), donde G(z)=Σ_{l≤z} μ²(l)∏_{ℓ|l}ν(ℓ)/(ℓ−ν(ℓ)). Para el error basta la forma cuadrática en los pesos λ_l de Selberg: |λ_l|≤∏_{ℓ|l}(1−ν(ℓ)/ℓ)^(−1)≪log²(2z), por la fórmula de los pesos óptimos y Mertens. La doble suma de errores está dominada por z² log⁴(2z) max_{l≤z²}ν(l)≪z⁶. Los pares con algún primo ≤z cuestan O(z).

Para acotar G por abajo, expandir el producto de Euler de 1+ν(ℓ)/(ℓ−ν(ℓ)) hasta ℓ≤z^δ. Al normalizar sus términos como probabilidades sobre l, la esperanza de log l es Σ ν(ℓ)log ℓ/ℓ≤Cδ log z por Chebyshev. Con δ fijo pequeño al menos la mitad del producto tiene l≤z por Markov. Por Mertens el producto completo es ≫log² z / M(h), con M(h)=∏_{ℓ|h}(1+3/ℓ): el factor excepcional en cada ℓ>2 cambia la razón por (ℓ−2)/(ℓ−1) y su inversa es ≤1+3/ℓ. El primo 2 cuesta una constante fija. Además Σ_{h≤H}M(h)≤H∏_ℓ(1+3/ℓ²)=O(H) al expandir por divisores. Así el peso total Σ log p log q sobre pares distintos en |p−q|≤H es O_A(XH), incluso para H pequeño. Basta multiplicar el conteo por O(log² X), absorbiendo z⁶+z por salto.

**Signo local y cruce.** El argumento del rectángulo positivo de 163 sigue dando ≫XH. El coste de todos los productos negativos es ahora O(XH(H/X)²) por Lipschitz y criba; elegir η pequeño. Esto prueba ambas cotas uniformes. Escribir E_X=∫₁² S(Xv)²dv y T_X=max(C₀log X,(E_X−D_X)_+/X). Sea H_X el ínfimo de los H en [C₀log X,ηX] con F_X(H)≤0. Entonces H_X≍T_X: la identidad F_X=E_X−D_X−N_X da el inferior usando N_X≤CXH y el superior usando N_X≥cXH. Para X grande hay sitio en el intervalo porque E_X=o(X²) por 164. El superior garantiza además el signo para TODOS los H≥C' T_X hasta ηX. No se presupone monotonía del bloque con signo.

**La igualdad de 164.** Si 0<α=2Θ−1<1, el mayorante E_X=O(X^(2Θ)) da negatividad estricta en H=M X^α con M fijo suficientemente grande. Para H=X^α mismo, si ningún cero alcanza Θ, la fórmula absoluta de 164 da U(x)=o(x^Θ) por convergencia dominada de los coeficientes, y el mismo resultado para S porque Θ>1/2. Entonces F_X(X^α)<0 eventualmente. Para supremo alcanzado y prefactor uno esta prueba no decide el signo. En particular la medida local del cruce no demuestra que T_X sea subpolinómico; eso requeriría controlar el exceso E_X−D_X.

**Cotejo.** Los casilleros de 163 sólo daban un techo O(XH log X), que no permitía comparar el cruce con el exceso de energía mediante constantes uniformes. El uso aquí de la criba de pares es clásico; la comparación cuantitativa concierne al bloque de 162. No es un nuevo método para limitar la parte real de los ceros.
