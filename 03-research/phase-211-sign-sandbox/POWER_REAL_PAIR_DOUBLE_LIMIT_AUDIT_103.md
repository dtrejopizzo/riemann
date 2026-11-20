# Auditoría independiente103 — límites reales y test puntual

Estado: **PROVED / auditoría aprobada. Constructor y reproducción independiente root FULLPASS.** El test certifica signo negativo del origen límite. Papers intactos.

Fuentes revisadas: `POWER_REAL_PAIR_DOUBLE_LIMIT_103.md`, `POWER_REAL_PAIR_LIMIT_ORIGIN_DESIGN_103.md` y `tools/power_real_pair_limit_origin_103_verify.py`. Se consultaron las reglas del proyecto y los tres índices vigentes, en particular102 y su complemento099. La diferencia es decidir una condición puntual de la pareja REAL siguiente mediante límites justificados; no otra representación ni un test genérico de potenciales.

## Límites y normalizaciones

La fórmula resolvente bilateral `A_p=pD_p=R_pJ−(c/p)R_pPhi` es exacta. La fórmula B-EXACT también lo es, usando `R_pJ−J=R_pJ''/p²`. El kernel probabilístico tiene norma ponderada a lo sumo `p/(p−sigma)`; las identidades con derivadas pagan la aproximación a la identidad sin exigir una cota superexponencial uniforme en p. La primitiva doble G0 es continua para los pesos declarados y sus bordes pares proceden de la masa cero. Por tanto `A_p→J`, `B_p=(ap/c)Psi_p→K`, con valores, derivadas y momentos.

Para q positivo fijo, Green anticausal es continuo con peso sigma>q; los balances cosh conservan Neumann y paridad. Al tomar después q→0 debe normalizarse **E/q**, no E: converge a `H=G0(b0J−K)`. La positividad estricta de H y Hmass se deduce del cruce único de su fuerza. El producto gamma E converge a `(Kmass/Hmass)H`; no se supone que gamma tenga límite finito. Escalar A y B positivamente conserva el signo de U. El orden iterado p→infinito, luego q→0, basta para transferir un eventual valor positivo a parámetros p,q FINITOS; no se usa uniformidad conjunta.

## Fórmulas y literal

Las fórmulas de momentos son Fubini con integrabilidad absoluta. Expansión simbólica independiente exacta verificó

`720 I0²(K0 Hmass−Kmass H0)−P=0`.

El literal fija128 paneles en[0,2], Taylor64/cap65,512 bits y16 modos antes de datos. Los centros y semianchos son dyádicos exactos. Incluye el prefactor theta; añade a todos los coeficientes la cola completa de modos **antes** de multiplicar por t^r. Añade el resto Cauchy simétrico exacto y la cola temporal positiva completa a cada uno de I0,...,I6. Comprueba precisión y finitud. El signo principal se decide mediante P sin divisiones, acepta cualquiera de los dos signos y falla honestamente si el encierro contiene cero. Kmass/Hmass se comprueban positivos antes de cocientes auxiliares. No importa certificados ni ejecuta otra malla.

## Alcance

P>0 refutaría exclusivamente el cruce negativo/positivo propuesto de U para algunos parámetros FINITOS de la pareja REAL. P<0 sólo confirmaría el signo puntual del origen en el límite. Ningún caso demuestra signo negativo de W, cruce global, positividad de Xi ni cierre de todos los órdenes. La positividad transformada del resto ya probada099+102 permanece intacta.

Corrida del constructor autorizada después de esta revisión literal. Reproducción y resultado se incorporarán sólo tras sus salidas reales.

## Resultado certificado y reproducción

Constructor68812 y reproducción independiente root91737 terminaron exit0/PASS los128 paneles. Hash idéntico del script: `5090a71fd7dd4ae786a3f785ca8a4c32d6691cf92af912d4e5fffff9e583d080`. No se cambiaron parámetros tras datos. Los encierros Arb impresos son

- P: `[-3.1683047444094325e−13 ± 2.16e−30]`;
- U_lim(0): `[-1.35855717857699839e−6 ± 8.09e−24]`.

La prueba son los asserts intervalares outward, incluidas las colas completas, no una lectura flotante. El signo es estrictamente NEGATIVO. Por los límites iterados también existen q positivos suficientemente pequeños y, para cada q elegido suficientemente pequeño, p finitos suficientemente grandes con U_original(0)<0; los umbrales no se explicitan. Esto sólo confirma la orientación del origen en ese régimen. No demuestra cruce global, positividad de Xi, propagación, nuevo signo W ni falsificador. No se ejecutan tests adicionales.

## Extensión analítica posterior — pareja límite completa

**APROBADA, sin nuevos cómputos.** Con b=Kmass/Jmass, H''=bJ−K y K''=aPhi−J. Para r>0, F=H−rK satisface

`D⁴F=(b+r)D²J−raD²Phi−aPhi+J`.

Es una combinación no trivial de la familia par Chebyshev4 de102: el coeficiente de J es1. Si H/K tuviera una estación positiva, F tendría una raíz de multiplicidad al menos2. Dos aplicaciones del lema Rolle par con bordes superexponenciales darían al menos4 raíces positivas de D⁴F, contando multiplicidades, frente al máximo3 de Chebyshev4. No se supone que la concavidad estricta implique derivada estricta: se excluye directamente la estación.

Poner I(t)=int_t^infinito(s−t)Phi(s)ds. Como tau=J/Phi decrece hacia0, para tau(t)<=a/2 se tiene K(t)>=aI(t)/2; además H(t)<=b int_t^infinito(s−t)J(s)ds<=b tau(t)I(t). Así H/K→0. Positividad de H,K y ausencia de estaciones fijan (H/K)'<0 en TODO t>0.

El cociente Hmass/Kmass es un promedio estricto de H/K bajo K. Por tanto U_lim=K−(Kmass/Hmass)H tiene exactamente un cruce positivo simple, negativo/positivo. La masa cero y ese cruce implican Xi_lim=G0 U_lim>0, par y con bordes correctos. Esto decide la pareja límite global, y en particular el signo de origen que el certificado anterior verificó independientemente. No se obtiene por continuidad el cruce GLOBAL para parámetros p,q finitos; éste sigue pendiente. La cronología del único test103 se conserva y no se ejecutan más tests.

## Extensión analítica — todos los q positivos en la pareja (J,K)

**APROBADA.** Fijar q>0, d=q ZK(q)/ZJ(q)>0, E_q=Gq(dJ−qK)>0. Para r>0 y F=E_q−rK, cálculo directo da

`(D²−q²)F''=(d+r)J''−raPhi''+a(rq²−q)Phi+(q−rq²)J`.

La combinación EVEN4 no es nula porque d+r>0. Si (E_q/K)' se anulase en un t positivo, elegir r=E_q(t)/K(t)>0 produciría una raíz doble F. Rolle par D² añade una raíz positiva, y Rolle ponderado Lq añade otra, incluidos multiplicidades y bordes: al menos4 frente al máximo3. Luego la derivada del cociente nunca se anula. Para CADA t fijo depende continuamente de q>0 (Green con supercolas y denominadores positivos). Como E_q/q→H en C1 y (H/K)'<0, es negativa para q pequeño; la conexión de(0,infinito) y la ausencia de ceros fijan su signo negativo para TODOq>0. No se requiere uniformidad en t para este argumento.

Promedio estricto bajo K: ZE_q(0)/ZK(0) está dentro del rango de E_q/K. Así U_q=K−[ZK(0)/ZE_q(0)]E_q tiene exactamente un cruce simple negativo/positivo y Xi_q=G0U_q>0 para TODOq>0. Se elimina la restricción q→0 del resultado final para la pareja(J,K), pero todavía se trata de p→infinito: NO se infiere cruce global para ningún p finito ni una nueva cobertura W.

## Puente exacto al p finito y obligación distinta

**Identidades y monotonías APROBADAS.** Con lambda=p²c/(ap−c), beta c=a lambda y beta p−p²=lambda. Las ecuaciones y los bordes dan exactamente `beta D_p+p²Psi_p=lambda K`, y `LpPsi_p=J−lambda K`. La transformada en z=p da d_*(p)=p/lambda, por tanto `Psi_p=(lambda/p)E_*(p)`. La monotonía103 todosq implica (Psi_p/K)'<0 y (D_p/K)'>0 para TODO p,t>0 FINITO. Este puente exacto no supone estabilidad del cruce bajo límites.

Para E=E_(p,q), poner A=d lambda/beta, B=dp²/beta+q, gamma=massPsi/massE y alpha=gamma q−q²>0 (residuo positivo102). Entonces LqE=AK−BPsi y, para U=Psi−gamma E,

`LpLqU=J''−a(lambda+gamma A)Phi+[lambda−q²+gamma(A+B)]J−lambda alpha K`.

El coeficiente de K usa Ap²−Blambda=−qlambda. Chebyshev4 para la familia MIXTA[K,J,Phi,J''] bastaría para excluir una raíz doble de U por dos lemas Rolle ponderados, pero NO se deduce de EVEN4 de102. La hipótesis sigue abierta, conservando antecedentes093/095. Bajo ella, masa cero y U no nulo impondrían un único cruce. Su orientación no procede del límite: un cruce positivo/negativo haría Xi=G0U estrictamente negativa, contradiciendo incluso la cota no estricta R_next=d z ZXi/ZE>=0 obtenida de099+102 por el bloque auxiliar PSD. Para z distinto de q se aplica directamente la congruencia de Schur; en z=q basta continuidad. La estrictitud adicional ya registrada no es necesaria para esta orientación. La orientación sería negativo/positivo. Sin el input mixto no se afirma positividad Xi finita ni nuevo W. No se lanzó certificado adicional.

Lectura literal final de103§11 aprobada: puente exacto, fuerza mixta y criterio únicamente SUFICIENTE. Se conservan expresamente los antecedentes093/095 y la obligación intermedia abierta; no queda auditoría pendiente de ese apéndice.

## Tres prefijos globales de la familia mixta

**APROBADO, sin cómputos.** Para f=A K+B Phi+C J, `D²f=AaPhi−AJ+B D²Phi+C D²J` pertenece a EVEN4 y no es trivial salvo A=B=C=0. Tres raíces positivas de f, contando multiplicidades, producirían al menos cuatro de D²f por Rolle par y bordes, contradicción. Esto prueba Chebyshev extendido de dimensión3 para[K,Phi,J].

Sean tau=J/Phi y kappa=K/Phi=tau(K/J). Ambos son positivos y estrictamente decrecientes hacia0. S=kappa'/tau'>0 satisface `W(Phi,J,K)=Phi³(tau')²S'`, que nunca se anula por la propiedad confluyente. S' tiene signo fijo. Si fuese positivo, kappa/tau sería el promedio de S en la cola con medida−tau'(s)ds, estrictamente mayor que S(t); entonces (kappa/tau)'=tau'(S−kappa/tau)/tau>0, contradiciendo(K/J)'<0. Por tanto S'<0 y d²kappa/dtau²=S'/tau'>0. En el orden[K,J,Phi], los primeros tres Wronskianos son positivos: K>0, W(K,J)=−J²(K/J)'>0 y W(K,J,Phi)=−W(Phi,J,K)>0. Sólo el cuarto Wronskiano de la familia mixta sigue abierto; no se infiere de estos prefijos.
