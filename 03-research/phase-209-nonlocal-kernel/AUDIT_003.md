# AUDIT_003 — Revisión hostil de ANTICORRELATION_003

2026-10-18. Revisor independiente. Matemática pura; comprobación adicional de cuatro desigualdades racionales con Fraction exacta, sin evaluación numérica de theta.

**Veredicto: PROVED, teorema auxiliar de signo estricto. No cierre de O1 ni enlace Q_T.**

## 1. Concavidad global de theta menos uno

La fórmula D²logτ=(πy)²V−πyM es correcta y las derivaciones término a término son válidas localmente en y>0 por convergencia de todas las series derivadas.

Para y≥1/2, V≤E((n²−1)²), y el denominador de la distribución dividido por el peso n=1 es ≥1. Cada y exp(−πy(n²−1)) decrece en ese intervalo. Las desigualdades n²−1≥3(n−1) y n⁴≤16^(n−1), n≥2, producen la serie geométrica anunciada. q<1/4 implica 16q³<1/4 y suma <1/3; el resultado πyV<π/6<1≤M es correcto y estricto.

Para y≤1/2, Poisson da A=1−√y+ε y τ=y^(−1/2)A con A>0. Revisé por expansión AA''−(A')² el numerador de D²logA: los seis términos y todos sus signos son correctos. ε₂=2Σ[(πn²/y)²−πn²/y]exp(−πn²/y)>0. La cota por 2π²y^(−2)Σn⁴exp(−πn²/y) es válida.

Las funciones y^(−j)exp(−πn²/y) son crecientes en el intervalo indicado para j=0,1,5/2. Los cocientes geométricos y el factor 8√2π² para ε₂/r son correctos. Verificadas exactamente mediante fracciones racionales:

- Σ_{k=0}^{20}(157/25)^k/k! >525.
- Con q=1/525, 2q/(1−q³)<1/250.
- Con π reemplazado por 22/7, 4πq/(1−4q³)<1/40.
- Con √2 reemplazado por 99/70 y π por 22/7, 8√2π²q/(1−16q³)<11/50.

Así el numerador es estrictamente menor que −103r/25000. La prueba cubre ambos intervalos incluido el punto de unión. **Teorema 1 aprobado.**

## 2. Anticorrelación y matrices

La integral doble de la segunda derivada estrictamente negativa prueba la desigualdad de cuatro valores sin aproximaciones. Para d,e coprimos, lcm=de y se obtiene covarianza estrictamente negativa para TODO y>0. Esto supera un signo asintótico y no es la PSD genérica de una covarianza.

Para enteros coprimos dos a dos, la positividad definida de V_y se prueba evaluando una relación constante en N=1 y N=d_i, sucesos todos de probabilidad positiva. La construcción B=sI−V_y con s≥λ_max da entradas no negativas y espectro en [0,s−λ_min]; la serie de Neumann converge y sus primeros dos términos prueban positividad estricta de cada entrada de la inversa. m=1 tratado correctamente.

**Precisión editorial necesaria en §5:** afirmar explícitamente que la inversa positiva entrada a entrada se refiere a una familia de índices coprimos DOS A DOS. No basta tener algún par coprimo; tampoco es válida una afirmación de definitud estricta si se admiten índices repetidos. Dentro de la familia de §3, todas las conclusiones de §5 están probadas: integración positiva preserva definitud estricta y signo cruzado; el argumento de la inversa vuelve a aplicar.

## 3. Valoraciones primas

Las series de indicadores de p^j suman v_p y están dominadas en L² por log|N|/log p. La suma doble de covarianzas converge absolutamente: la suma de probabilidades conjuntas es E(v_pv_q)<∞ y la suma de productos de medias es E(v_p)E(v_q)<∞. Cada sumando para p≠q es estrictamente negativo. El resultado es, por tanto, estrictamente negativo.

Al sumar sobre primos con pesos log p, la cota por E(log²|N|)+(Elog|N|)² justifica el intercambio absoluto. La suma diagonal es finita por Σ_p(log p)²v_p²≤log²|N|. La identidad de varianza, su diferencia exacta y la desigualdad estricta (4) quedan probadas. El par (2,3) asegura estrictitud.

## 4. Alcance y novedad

El teorema proporciona un signo aritmético auxiliar, construido sobre una ley gaussiana discreta cuyo Poisson entra efectivamente en la prueba. No se obtuvo el signo por escribir una norma ni por asumir el signo de Q_T. La nota no afirma prioridad bibliográfica; ausencia de hit en el índice no es prueba de novedad global.

El resultado aún puede heredarse bajo cambios aritméticos; no satisface por sí solo la especificidad Euler exigida al objeto completo. Tampoco identifica altura Mellin, peso del nodo, dominio polar ni dominación del déficit gamma. Las cautelas finales son correctas y deben permanecer. No atribuir a la estructura matricial de esta covarianza una estructura de la matriz de Weil sin demostrar el mapa.

**Resultado final:** positivo auxiliar estricto verificado; el enlace con el nodo sigue OPEN. Se cumplió un hito matemático distinto y más pequeño que construir el núcleo O1 solicitado, y debe comunicarse con esa distinción.
