# POWER_STATE_067 — El término positivo Selberg es esencial en el caso129

Estado: **PROVED/APROBADO**, fuente POWER_SELBERG_DROP_OBSTRUCTION_067.md y auditoría POWER_SELBERG_DROP_AUDIT_067.md; root también aprobó. Sin nuevo N, corte, precisión o campaña. Papers intactos.

## Resultado y diferencia

`POWER_SELBERG_DROP_OBSTRUCTION_067.md`, `POWER_SELBERG_DROP_AUDIT_067.md` y `POWER_STATE_067.md`: revisión independiente mapa y root, sin nuevos cálculos ni otroN. Para el MISMO gamma129,u=63/2 de061, Selberg da S=U−V y W/norma²=ARCH/norma²+polar/norma²−2U+2V. El par2·2 y la mezcla real030/Jensen prueban2V>1/243. Como061 certificó0<W/norma²<1.35·10^(−10), el criterio que descarta2V tiene valor<−1/250. Incluso retener sólo1−theta de2V exige theta<6561/(2·10^11); theta=10^(−7) ya deja ese candidato negativo.

Diferencia explícita frente055/023: no se vuelve a ofrecer la identidad Selberg ni V>=0 como avance.055 dejó abierta la falsedad del criterio fuerte W/norma²>=2V; el certificado completo posterior061 ahora lo refuta en un test ya existente. Es una obstrucción a esa pérdida positiva aislada, no a Selberg completo, métodos compensados ni signo de W. No nueva fila, ventanaT o conclusión global. Nota retrospectiva incorporada a STATE055; papers intactos.

## Obligación que permanece

El test129 conserva el signo positivo certificado061. No se obtuvo una comparación uniforme en N de U y V ni una cota nueva del interior. Una siguiente estimación debe preservar su compensación: la positividad individual de V no autoriza descartarlo sin pagar una pérdida mayor que el margen completo. La precisión relativa indicada sólo concierne a la pérdida aislada en esta misma descomposición, no impone tal precisión a toda posible prueba.

## Consulta068 — reagrupación exacta y alternativa gaussiana

Insight048 y root verificaron la reagrupación por soporte primo. Para m=p^a, a>=1, los coeficientes de μ*log² y Λ*Λ son, respectivamente, (2a−1)log²p y (a−1)log²p. Para m=p^a q^b con p distinto de q y a,b>=1, ambos son 2logp logq. Para m con al menos tres primos distintos, ambos son cero. Por tanto conservar la cancelación a m fijo devuelve exactamente Λ(m)logm y, tras dividir por logm, reconstruye S. No aparece una desigualdad nueva ni un contacto favorable adicional.

El intento de introducir cruces entre contactos distintos tampoco produjo un bound nuevo: para rho gamma decreciente, rho(log(a/b))−rho(log(ab))>=0 cuando a,b>=1. Esta comparación de núcleos sólo da la orientación superior correspondiente al sustituir productos por correlaciones; no estima la compensación con ARCH. No se supone que el operador infinito de contactos sea acotado sin amortiguación suficiente. El cambio a productos rho(loga)rho(logb) reproduce las comparaciones ya examinadas025/055. Consulta deduplicada, no NO-GO para toda comparación cruzada.

Casos auditó además el posible lower universal del funcional gaussiano G_W(v), definido por autocorrelación exp(−v t²). No se encontró una prueba ni un falsificador de G_W(v)>=0 para TODO v>0: sigue OPEN. INTERIOR_CONSTRAINT027§4 conserva todas las piezas y §5 refuta únicamente la convexidad global; GAMMA_BALANCE030§4 prueba un valor particular, no todos los parámetros. La ruta gaussiana anterior E101_038§6 tampoco aporta una positividad universal disponible para transferir.

La mezcla rho_N(t)=E exp(−Vt²), V=(u²/4)/G y G de ley Gamma(N−1/2,1), sí transferiría tal lower a toda la fila k=0. La mezcla existe también para N=1; no necesita la media EV, que sólo se usa en Jensen para N>=2. Para u>1/2 los intercambios por piezas siguen siendo finitos, incluido el polar: su promedio gaussiano es proporcional a E[sqrt(G)exp(G/(4u²))], finito pues 1/(4u²)<1. ARCH se controla por la representación temporal, con (1−rho_1(t))/t acotado cerca de0, y el peine por convergencia absoluta. No se extiende esa transferencia a k>0 ni se obtiene el lower G_W que falta.

Estos diagnósticos evitan relanzar las mismas identidades como herramientas de signo. No hubo nuevos casos numéricos, nuevo teorema para los índices ni cambios en los papers.
