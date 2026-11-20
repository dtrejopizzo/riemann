# POWER_THREE_SECANTS_AUDIT_079 — Auditoría independiente

Estado: **APROBADO / PROVED como implicación y converso bajo BASE073.** Fuente: `POWER_THREE_SECANTS_079.md`. Revisor mapa; revisión independiente root e insight comunicada en la misma sesión. Papers intactos.

## Antecedentes y diferencia

Leídos las reglas del proyecto, los tres registros obligatorios y los antecedentes003,073–078. Los falsificadores003/074 siguen vigentes: BASE sola no basta para tres nodos. La entrada nueva es la comparación exacta de secantes de g(x)=a sqrt(x)/M(sqrt(x))−1. Convierte su concavidad local en condición suficiente y necesaria para todos los bloques de tres, bajo BASE; no se limita al jet confluyente074. No necesita077 ni concavidad de h=1/b.

## Comprobaciones algebraicas y signos

Para 0<u<v<w, beta=(g2−g1)/(v²−u²)>0, delta=beta−(g3−g2)/(w²−v²), alpha=1+g1−beta u². La congruencia diagonal positiva indicada en la fuente da exactamente T_ij=1+(ui gj+uj gi)/(ui+uj).

Se reprodujeron por expansión simbólica exacta DET, CONC y GAP; las factorizaciones impresas constituyen la prueba y no dependen de esa comprobación. En particular:

- M creciente da alpha>beta uv>0; no hace falta alpha>=1 ni concavidad entre0 y u².
- D2=w(alpha−beta uv)+beta uv(u+v)>0, incluso si w>u+v.
- La concavidad de M da delta<=delta_conc con la orientación impresa.
- delta_crit−delta_conc=beta(w−u)uvw(alpha+beta u²)(alpha+beta v²)/[(alpha w²+beta u²v²)(v+w)D2]>0.

Así delta>0 implica determinante positivo; los menores de dos puntos positivos de073 completan la definición positiva. Si delta=0, T=alpha 11^t+beta uu^t es PSD de rango2. El caso débil beta=0 y los nodos repetidos están separados correctamente; la positividad estricta se refiere a funciones no nulas.

Para el converso no se presupone delta>=0: alpha>beta uv sigue vigente; si delta<0, las llaves de DET son positivas y el determinante es negativo. Por tanto todos los bloques3 PSD equivalen a la concavidad de g en el intervalo de cuadrados, dentro de BASE. No se ha inferido esa concavidad de los pares.

## Aplicación y obligación restante

BASE está probada para la Phi real por073. La cola078 g''<0 para u>=63/2 ya da triples estrictamente positivos allí, mediante esta prueba analítica. Esa cobertura ya estaba contenida en053 (trece polos arbitrarios); no se registra como nueva región W.

Para los exponentes admisibles ai=ui+1/2>1, sólo queda verificar la curvatura real en **1/2<u<63/2**. No hace falta resolver 0<u<1/2 para este objetivo. h cóncava deja de ser obligación del criterio3, aunque su resultado exterior078 permanece válido. No se afirma signo compacto, todos los triples admisibles, órdenes superiores ni una ventana temporal nueva.
