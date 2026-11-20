# POWER_BRIDGE_002 — Puente de potencias a PW_N en norma fuerte

Estado: PROVED, revisado independientemente en POWER_AUDIT_002.md y POWER_PACKET_SCOPE_AUDIT_009.md. No afirma positividad de matrices de todos los órdenes. Papers intactos.

## Antecedentes y diferencia

Leídos las reglas del proyecto, POWER_CONE_001, propuesta de potencias, índice README (familia exterior/Pick y registro P211), grid partes 3/5, crucigrama (entradas exterior y gauge), y definiciones ext/univ del Paper 47. La novedad concreta respecto de la propuesta es resolver su requisito de densidad en norma de forma mediante un espacio de Sobolev fraccionario ponderado, sin suponer densidad L² suficiente. No se propone un nuevo principio Pick ni se reintenta una identidad como prueba de signo.

## 1. Espacio puente

Fije s=3/4, t=1/4. Para datos reales rho en X>1 escriba

    g(y)=exp(5y/4) rho(exp y), y>0,
    ||rho||B=||g||H^t(0,infinito).

Se usa la norma intrínseca de Gagliardo. Se invoca aquí el lema estándar de extensión cero para Sobolev fraccionario, no una herramienta nueva: la extensión por cero de H^t(0,infinito) a H^t(R) es acotada para 0<t<1/2; su término de frontera es la desigualdad de Hardy fraccionaria ∫|g(y)|² y^(-2t)dy ≤ C||g||H^t². No se exige g(0)=0. El término cruzado del seminorma de la extensión es exactamente (1/t)∫|g(y)|²y^(-2t)dy.

Sea h(y)=Zrho(exp y) en y>0 y cero fuera. Entonces

    exp(sy)h(y)=Σ(n>=1)n^(-5/4) g(y+log n).

Las traslaciones hacia la izquierda sobre la semirrecta son contracciones para la norma intrínseca H^t: se restringen tanto la integral simple como el doble integral de diferencias. Por sumabilidad de n^(-5/4),

    ||exp(s·)h||H^t(0,infinito) ≤ zeta(5/4)||rho||B.

Multiplicar por exp(-sy) en la semirrecta es acotado en H^t; luego extender por cero. Se obtiene simultáneamente

    ||h||H^t(R)+||exp(s·)h||L²(0,infinito) ≤ C||rho||B.        (B1)

Por log(2+|tau|)≤C(1+|tau|²)^t, B1 controla la norma arquimediana de forma. Además

    |c_h(log n)|≤n^(-s)||exp(s·)h||²L²,

por Cauchy–Schwarz tras desplazar. La suma del peine converge y está acotada por 2ΣLambda(n)n^(-5/4)||exp(s·)h||². Los dos momentos son continuos por Cauchy–Schwarz, pues s>1/2. Todas estas estimaciones admiten versión bilineal. En consecuencia la forma exterior completa Q es una forma bilineal continua en B:

    |Q(rho,sigma)| ≤ C ||rho||B ||sigma||B.                    (B2)

Esta norma controla separadamente todos los términos del Paper 47; no depende de cancelaciones ni de signo supuesto.

## 2. Todo dato PW_N pertenece a B

Si rho=Fourier(h)|_(1,infinito), con h de PW_N, integrar dos veces por partes da

    |rho(X)|+|rho'(X)|≤C_h X^(-2), X>=1.

Esto sigue también para rho' porque xh(x) es C² dentro de [-N,N], se anula en extremos, y sus derivadas laterales son finitas. Los posibles términos de frontera de la segunda integración son O(X^-2).

Para g resulta |g(y)|≤Ce^(-3y/4), |g'(y)|≤Ce^(y/4). Si 0<delta<1, partir en R=log(1/delta) demuestra

    ∫_0^infinito |g(y+delta)-g(y)|²dy ≤ C delta^(3/2).

En (0,R) se usa la cota de derivada; en (R,infinito) se usan las amplitudes. Por la caracterización mediante diferencias, integrar contra delta^(-1-2t) demuestra g∈H^t para t<3/4, en particular t=1/4. La extensión cero solo requiere t<1/2 y añade O(delta), también integrable. Así PW_N⊂B para cada N finito.

## 3. Densidad constructiva de potencias con exponentes >=32

Primero aproxime g∈H^t(0,infinito) por g_j suaves en [0,infinito), de soporte compacto. No es preciso anularlas en 0. Esta es densidad estándar obtenida por extensión, corte y convolución; cada operación converge en H^t.

Fije B=32-5/4=123/4 y una de esas g_j. La función q(x)=x^(-B)g_j(-log x) para 0<x≤1 se prolonga suavemente por cero cerca de x=0. Elija polinomios P_k que aproximen q en C¹([0,1]). Se construyen aproximando q' uniformemente por polinomios e integrando, ajustando el valor en 0. Entonces

    g_jk(y)=e^(-By)P_k(e^(-y)) → g_j(y) en H¹(0,infinito),

porque el error y su derivada son acotados por C epsilon_k e^(-By). Por tanto convergen en H^t. Al devolver la ponderación,

    rho_jk(X)=Σ_n p_kn X^(-(B+5/4+n)).

Todos los exponentes son exactamente 32+n, n entero no negativo. Una selección diagonal da rho_k→rho en B. Por B1/B2, convergen tanto las imágenes Zrho_k en norma log-Fourier y momentos como cada término de Q; Q[rho_k]→Q[rho].

**Teorema puente:** la envolvente real finita de X^-a, a>=32, es densa para todos los datos PW_N en una norma en la que la forma universal exterior completa es continua. Los aproximantes no necesitan pertenecer a PW_N: la continuidad se prueba en el espacio ambiente B y el límite sí pertenece a PW_N.

No se corrigen momentos ni borde del dato rho: las condiciones del paper se imponen a su preimagen h compacta, no a rho en X=1. Imponer a cada aproximante ser la transformada de una función de soporte compacto sería un requisito adicional innecesario para pasar una desigualdad Q>=0. La propiedad correcta es aproximar todas las integrales, incluidos los momentos polares de Zrho; B1/B2 lo hacen explícitamente.

## 4. Consecuencia condicional precisa y límite

Si se demuestra positividad de TODOS los tamaños finitos del kernel de potencias, incluso restringiendo a la escalera fija a=32+n, la densidad anterior implica Q>=0 sobre cada PW_N. La positividad sobre cada plano de dos potencias no basta: las aproximaciones polinómicas usan un número creciente de términos con signos arbitrarios. Tampoco este argumento produce coercividad respecto de distancia al gauge ni constante polinómica; solo permite transferir no negatividad.

## 5. Verificación independiente de polarización

Para a,b>1, u=a-1/2,v=b-1/2, la parte polar bilineal sobre e^-uy,e^-vy es exactamente

    P_ab=1/[(a-1)b]+1/[a(b-1)].

El kernel propuesto en POWER_CONE_001 usa en su lugar

    R_ab=[1/a+1/(a-1)+1/b+1/(b-1)]/(a+b-1).

Estas expresiones coinciden exactamente: al multiplicar por a(a-1)b(b-1)(a+b-1), ambas dan (a+b-1)(2ab-a-b). Para a=2,b=3, ambas son 7/12. Por tanto no encuentro error en el término polar cruzado de POWER_CONE_001. Las partes arquimediana y peine también se polarizan con el denominador u+v mediante la identidad Re[(u-iτ)^(-1)(v+iτ)^(-1)]=[u/(u²+τ²)+v/(v²+τ²)]/(u+v). La densidad y continuidad B1/B2 son independientes de este cálculo escalar.

## 6. Puente directo más sencillo a todo test compacto

El paso por PW_N no es necesario para transferir no negatividad. Dado un test real suave compacto F, trasládelo para obtener h con soporte en (0,L). La forma completa es invariante por traslación. Defina en y>0

    u(y)=Σ(n>=1)mu(n)n^(-1/2)h(y+log n),
    rho(exp y)=exp(-y/2)u(y).

Las sumas son finitas: n≤exp L, y cada sumando es suave hasta y=0 y se anula para y≥L. Así G(y)=exp(sy)u(y) es suave de soporte compacto en la semirrecta, pertenece a B, y

    Zrho(exp y)=Σ(k,n>=1)mu(n)(kn)^(-1/2)h(y+log(kn))=h(y),

por Σ(n|m)mu(n)=1_(m=1). No aparece ningún límite aritmético en esta inversión. La densidad de §3 aproxima este rho por combinaciones de X^(-(32+n)) en norma B; sus imágenes convergen a h en todas las piezas de la forma.

Por tanto basta probar que, para cada m, la matriz K_ij=(L(32+i)+L(32+j))/(63+i+j), 0≤i,j≤m, es semidefinida positiva. Eso da no negatividad de la forma completa sobre todos los tests suaves compactos, y por densidad usual de la forma sobre todos los dominios de ventana. En particular da el signo sobre los subespacios primitivos. No se usa gauge, coercividad, ninguna equivalencia externa ni reducción espectral. El nuevo objetivo concreto es la positividad de una única escalera de matrices finitas explícitas. Ese signo sigue OPEN aquí.
