# POWER_INTERIOR_CONSTRAINT_027 — Mezcla gamma real, resto positivo de Jensen y dirección de curvatura

Estado: PROVED representación positiva del resto, desigualdad estricta para ARCH_sharp y refutación analítica de convexidad global del funcional gaussiano completo. Revisión independiente APROBADA y verificador reproducido. OPEN signo del emparejamiento interior. Papers intactos.

## 1. Corpus y diferencia precisa

Leídos las reglas del proyecto, LOW_TABLE018, TATE_CHAIN009, PACKET_SCOPE009, ARCH_CELL026 y UNIFORM_CUTOFF026; búsquedas de Gaussian/heat mixture/convexidad en índice ROUTES-TRIED-INDEX, grid maestro y crucigrama. La mezcla de calor gamma ya se usó en018 para probar C_N>0 y C_N'<0: NO se atribuye novedad a esa representación conocida. Las rutas genéricas de heat trace o semigrupos también están registradas y no se relanzan.

La diferencia específica es imponer esa mezcla REAL al kernel interior, construir un peso positivo para su resto respecto de la gaussiana de igual segundo momento, y comprobar la dirección de la desigualdad que aportaría Jensen. Se prueba una desigualdad genuina, pero su dirección ARCH_sharp es SUPERIOR, no inferior. Para la forma completa se identifica una curvatura firmada y se refuta una premisa concreta de convexidad mediante una cota elemental en todo un rango. No se presenta esa refutación como imposibilidad de otras desigualdades para la mezcla específica.

## 2. Restricción gamma exacta del test real

Mantenga u=63/2, N>=2, rho_N(t)=C_N(t)/C_N(0). La mezcla de calor de018, normalizada, es

    rho_N(t)=E exp(−V_N t²),
    V_N=beta/G, beta=u²/4,
    G~Gamma(b,1), b=N−1/2.                             (MIX)

En particular V_N tiene densidad positiva

    p_N(v)=beta^b v^(-b−1)exp(−beta/v)/Gamma(b), v>0,
    m_N=E V_N=beta/(b−1)=u²/[4(N−3/2)].

Esto no permite elegir una mezcla arbitraria para fabricar K: la ley está completamente fijada por N y u. La densidad normalizada de la forma gaussiana que tiene autocorrelación exp(−vt²) corresponde al test de norma uno phi_v(y)=(4v/pi)^(1/4)exp(−2vy²), sobre toda la recta.

Si G_W(v)=W[phi_v], se cumple exactamente

    W[g_N]/||g_N||²=E G_W(V_N).                         (WG)

La permutación es legítima pieza por pieza: el término de Lévy después de extraer C0 es no negativo; el peine en magnitud y el polar también. Tonelli identifica sus esperanzas con las del rho_N=e^-u|t| por polinomio, que son finitas porque u>1/2. No se integra una identidad formal condicionada ni se sustituye una suma infinita por su valor regularizado.

## 3. Un peso positivo PROPIO del resto de la mezcla

Ponga delta_N(t)=rho_N(t)−exp(−m_Nt²)>=0. Es estrictamente positiva para t!=0 porque V_N no es constante y v↦exp(−vt²) es estrictamente convexa.

Defina el resto de funciones bisagra

    L_N(a)=E(V_N−a)_+−(m_N−a)_+,
    L_N(a)>=0.

De forma explícita,

    L_N(a)=∫_0^a(a−v)p_N(v)dv, a<=m_N,
    L_N(a)=∫_a^infinito(v−a)p_N(v)dv, a>=m_N.

Taylor con resto integral, o la representación de una función convexa mediante bisagras, prueba

    delta_N(t)=t^4∫_0^infinito exp(−at²)L_N(a)da.        (GAP)

Éste es un peso positivo explícito que conserva la restricción gamma; delta_N(t)/t^4 es completamente monótona en t². Para N>=3 tiene masa finita

    ∫L_N(a)da=Var(V_N)/2
      =u^4/[32(N−3/2)²(N−5/2)].

En N=2 esta masa es infinita, pero GAP sigue siendo válida para t!=0 por Tonelli y el primer momento finito. No se utiliza una varianza inexistente en ese extremo.

## 4. Una desigualdad estricta: la reducción a la varianza da el sentido incorrecto para ARCH_sharp

La forma sharp normalizada sobre una gaussiana es

    A_sharp(v)=d_*+∫_0^infinito K_sharp(t)(1−e^-vt²)dt,
    d_*=psi(5/4)−logpi,
    K_sharp(t)=2e^(-5t/2)/(1−e^-2t)>0.

Por tanto A_sharp''(v)=−∫K_sharp(t)t^4e^-vt²dt<0. Integrando MIX, o directamente delta_N>0, se obtiene la desigualdad estricta de TODA la familia

    ARCH_sharp[g_N]/||g_N||²
      =E A_sharp(V_N)<A_sharp(E V_N).                  (UPPER)

Así el lema propuesto como posible ayuda «la mezcla gamma queda acotada INFERIORMENTE por la gaussiana con igual segundo momento» es falso para ARCH_sharp: ocurre estrictamente lo contrario. UPPER es una cota superior real, no un certificado inferior del déficit interior. Esto no refuta una comparación distinta que conserve también ERR.

## 5. Curvatura completa: qué falta después de conservar TODA la cancelación

La forma completa gaussiana se escribe, con K(t) el Lévy original,

    K(t)=2e^(-t/2)/(1−e^-2t)=e^(t/2)/sinh t,
    v_q=2Lambda(q)/sqrt(q), C0=psi(1/4)−logpi,

    G_W(v)=C0+∫K(t)(1−e^-vt²)dt
       +4∫_0^infinito cosh(t/2)e^-vt²dt
       −Σ(q>=2)v_q e^-v(logq)².

Su segunda derivada es

    R(v):=G_W''(v)
      =4∫cosh(t/2)t^4e^-vt²dt
        −∫K(t)t^4e^-vt²dt
        −Σ(q>=2)v_q(logq)^4e^-v(logq)².                 (CURV)

Todas esas integrales y series convergen para v>0. GAP y Tonelli por cada pieza con signo fijo dan la identidad exacta

    W[g_N]/||g_N||²−G_W(m_N)=∫_0^infinito L_N(a)R(a)da. (JOINT-GAP)

El intercambio en JOINT-GAP es absoluto por piezas: 0<=delta_N(t)<=min(rho_N(t),m_Nt²). La segunda cota controla el factor K(t)=O(1/t) en0; la primera controla el infinito, el polar y la suma de contactos mediante el decaimiento exponencial gamma. No se necesita finitud de ∫L_N cuando N=2 para estos intercambios. El polar es la única contribución favorable en CURV; ARCH y el peine son desfavorables. El peso positivo L_N no convierte por sí solo esa curvatura firmada en un lower bound.

## 6. Falsificador analítico de convexidad completa, sin certificados puntuales

La hipótesis «G_W es convexa en toda la semirrecta» es FALSA para la forma aritmética original. De hecho

    G_W''(v)<0 para TODO v>=65536.                      (FAIL-CONVEX)

Prueba. La fórmula K(t)=e^(t/2)/[2sinh(t/2)cosh(t/2)] y e^(t/2)>=cosh(t/2) implican K(t)>=1/[2sinh(t/2)]. Para0<t<=1 se tiene sinh(t/2)<=t; por ejemplo, cosh(s)<2 para0<=s<=1/2 e integración da esa cota. Por tanto K(t)>=1/(2t). Si v>=2,

    −∫K(t)t^4e^-vt²dt
      <=−[1−(v+1)e^-v]/(4v²)<−1/(8v²).

Se usó (v+1)e^-v<=3e^-2<1/2. Para el polar, cosh(t/2)<=e^(t/2) y t/2<=vt²/2+1/(8v) dan

    4∫cosh(t/2)t^4e^-vt²dt
      <=3sqrt(pi)·2^(3/2)e^(1/(8v))v^(-5/2)
      <24v^(-5/2).

Las cotas sqrt(pi)<2,2^(3/2)<3 y e^(1/(8v))<8/7 bastan para el último número. El término de primos en CURV es no positivo y no se omite con un signo favorable inventado. Si sqrt(v)>=256,

    R(v)<v^-2[−1/8+24/256]<0.

Esto prueba FAIL-CONVEX sobre un rango infinito del MISMO funcional. No se concluye que JOINT-GAP sea negativo para la ley específica L_N, ni que una envolvente convexa más fina sea imposible: la ley gamma distribuye masa en todo a>0 y hay que conservarla.

## 7. Obligación interior que permanece y alcance

MIX y GAP proporcionan restricciones reales adicionales a la masa y al signo exterior de K. Permiten reescribir el interior como una integral con peso positivo explícito L_N, en vez de permitir K arbitrarios que violen la autocorrelación. Pero no se obtuvo una desigualdad que haga no negativa la suma de G_W(m_N) y JOINT-GAP.

La continuación válida tendría que controlar unilateralmente la parte negativa de R CONTRA ESTA ley L_N, o aportar una comparación conjunta distinta que use su forma inversa gamma. No basta aplicar Jensen con el sentido incorrecto a ARCH_sharp ni suponer convexidad global del funcional completo, ambas premisas refutadas aquí. Tampoco se deduce signo de todas las combinaciones de g_N aunque se decidieran todas estas diagonales.

Se registran como resultados la desigualdad UPPER para todos N, el peso positivo GAP y FAIL-CONVEX con rango explícito. No hay nueva cobertura W ni modificación de papers.


## 8. Transferencia de los falsificadores inversos a gaussianas individuales

**PROVED analítico; revisiones matemática y literal aprobadas.** No se atribuye novedad a MIX de§2. La diferencia frente al falsificador de convexidad de§6 es usar la LINEALIDAD exacta de los inversos Möbius, con Fubini absoluto, no Jensen ni una comparación entre valores de W. Dedup dirigido en índices/grid/crucigrama y fuentes019–023,027,030,039–040 no halló este corolario explicitado. Sin nuevos valores, parámetros calculados o certificados.

Para a>0 y x>=1 definir

 w_a(x)=x^(-1/2)exp[-a(log x)^2],
 H_a(x)=-w_a'(x)=x^(-3/2)exp[-a(log x)^2](1/2+2a log x)>0,
 J_a(x)=sum_(m>=1)mu(m)w_a(mx),
 h_a(x)=sum_(m>=1)mu(m)mH_a(mx),
 K_a(x)=J_a(x)+x h_a(x).

Para cada a>0 y x>=1 las series son absolutas: la gaussiana en log m domina cualquier potencia de m y los factores polinomiales en log m. Así se consideran INVERSOS COMPLETOS, no prefijos. Las funciones en a son medibles por sus sumas parciales.

La ley positiva FIJA V_N de§2 da w_N(x)=E w_(V_N)(x), donde w_N=x^(-1/2)rho_N(log x). Para N=128 o129, E V_N es finita. Diferenciar bajo la esperanza es legítimo para x fijo en un compacto de[1,infinito): el derivado se domina por C(1+V_N), integrable. Luego

 H_N(x)=E H_(V_N)(x).

Para pasar a h en x1, aplicar Tonelli primero a términos NO NEGATIVOS:

 E sum_(m>=1)|mu(m)|mH_(V_N)(m)
 <=sum_(m>=1)mH_N(m)<infinito.                        (ABS-H)

La última suma converge porque H_N(m)=m^(-33)A_N(log m), A_N un polinomio finito. Análogamente,

 E sum_(m>=1)|mu(m)|w_(V_N)(m)
 <=sum_(m>=1)w_N(m)<infinito,                         (ABS-J)

pues w_N(m)=m^(-32)P_N(log m). Fubini absoluto, con TODOS los signos de mu, prueba

 h_N(1)=E h_(V_N)(1),
 J_N(1)=E J_(V_N)(1),
 K_N(1)=E K_(V_N)(1).                                (INV-MIX)

Ahora se reutilizan exactamente los resultados completos previos, sin recalcularlos:

 POWER_INVERSE_INTERIOR_022: h_128(1)<-33/50<0,
 POWER_CUMULATIVE_TEST_023: K_129(1)<-1/251<0.

Si h_a(1) fuera no negativa para TODO a>0, su esperanza bajo la ley V_128 no podría ser negativa. Por INV-MIX existe por tanto a_h>0 con h_(a_h)(1)<0. El mismo argumento bajo V_129 da a_K>0 con K_(a_K)(1)<0.

Los parámetros a_h y a_K pueden ser DISTINTOS. No se ha calculado ninguno, ni probado que una misma gaussiana tenga ambos signos. Quedan refutadas las dos hipótesis UNIVERSALES gaussianas h_a(x)>=0 y K_a(x)>=0 para todos a>0,x>=1, cada una ya en el punto x1. Una existencia en la familia gaussiana no se deduce de un prefijo: utiliza el certificado gamma COMPLETO y el intercambio absoluto de la ley real.

No se infiere ERR negativa, W negativa ni negatividad del kernel de calor aritmético H_A-P deE101036. Tampoco se refuta la representación Stieltjes de N(x). Los presupuestos firmados de022–024 continúan siendo objetivos legítimos; lo refutado son esas dos premisas de positividad inversa uniforme. La forma gaussiana completa y su signo no son aquí el funcional transferido. Papers intactos.
