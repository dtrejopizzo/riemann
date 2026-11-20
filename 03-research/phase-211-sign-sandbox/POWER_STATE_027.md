# Estado027 — Balance exterior completo y restricción gamma interior

Estado: resultados parciales PROVED, auditoría independiente aprobada; signo global OPEN. Sustituye STATE026. Goal activo, papers intactos.

## Contribución conjunta exterior

POWER_DISCRETE_BALANCE_027 da una fórmula exacta por pisos del peso Omega y demuestra Omega(t)>=ell−(4logt+9)/t, ell=1+gamma/2−log(4pi)/2>1/50. En particular Omega>.009 para t>=4096 salvo singularidades logarítmicas integrables. Combinado con el corte uniforme026 y el kernel gamma real, prueba positividad y cotas de magnitud para TODA la cola conjunta int_T^infinito K_N Omega cuando T>=max(4096,exp(tau_N)).

Para N129 se obtiene 0<R=int_4096^infinito K129 Omega<10^-36. Por tanto W[g129]/norma²=int_1^4096 K129 Omega+R, con el primer término aún sin signo. La cola positiva no aporta una corrección significativa al presupuesto grueso026. El déficit .15 de aquel presupuesto no es un déficit interior real demostrado.

Las identidades sum K(n)=3/2 y sum K(nx)=x^-32D_N(logx) son restricciones exactas por inversión, no pruebas de signo por sí solas. No se afirma convergencia uniforme de Omega hacia ell: los picos logarítmicos la impiden.

## Mezcla real y peso del resto

POWER_INTERIOR_CONSTRAINT_027 usa la mezcla de calor conocida018, rho_N(t)=E exp(−V_N t²), V_N=(u²/4)/G, G~Gamma(N−1/2,1). Conserva todas las piezas de W por Tonelli con magnitudes finitas.

Con m_N=EV_N, el peso positivo específico L_N(a)=E(V_N−a)_+−(m_N−a)_+ da exactamente rho_N(t)−exp(−m_N t²)=t^4 int exp(−at²)L_N(a)da. Para N>=3 su masa es Var(V_N)/2; en N2 la masa es infinita pero la representación sigue válida para t distinto de cero.

La comparación con la gaussiana de igual segundo momento tiene sentido SUPERIOR estricto para ARCH_sharp, por concavidad. Para la forma completa, Wgamma−Wgaussiana(m_N)=int L_N(a)G_W''(a)da. No se obtuvo el signo de esa integral. La premisa de convexidad global del funcional gaussiano real es falsa: G_W''(a)<0 para TODO a>=65536, mediante cotas elementales. Esto no prueba que W ni el resto específico sean negativos.

## Verificación, cobertura y continuación

POWER_JOINT_AUDIT_027 aprueba ambos memos, incluidas normalizaciones, Fubini/Tonelli, singularidades y excepción N2. Root leyó las pruebas y reprodujo ambos verificadores exactos: PASS. Los scripts comprueban constantes; la uniformidad proviene de los argumentos analíticos.

No hay nueva cobertura W ni ventana T: siguen filas N1,2,3 para todo k, cono k>=10000N², ocho polos arbitrarios y bloque fijo12. El puente escalar017 sigue requiriendo todos N,k. No basta una mezcla positiva con curvatura firmada ni otra cola favorable diminuta.

La siguiente búsqueda prioriza una desigualdad del interior real y una posible fila N4 completa mediante ARCH exacto, peso de autocorrelación mejorado y polar alternado, previa consulta del corpus. No se considera logrado el objetivo ni existe bloqueo externo.
