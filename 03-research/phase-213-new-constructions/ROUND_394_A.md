# En el extremo cuatro todavía falta masa

**Estado: PROVED, con revisión independiente de la comparación de segundo orden, el factorκ/4 y la consecuencia lógica.**

Sean L=log x, z=L², b=log z y p_* como en 393. Bajo RH se tiene

    liminf b(p_*/z−4) ≥ 8(1+log 2)log 4.

Por tanto un techo eventual p_*≤(4+κ/b)z con κ estrictamente menor que esa constante queda descartado incondicionalmente: ese techo implicaría RH por 393 y luego contradiría el nuevo piso. En particular tampoco sirve el corte exacto 4z.

**Comparar en la misma silla.** Sea α la silla exacta de 367 para z=L²; c_b=b(α−1/2)→log 2. Bajo RH, 368 da

    log |S|=αL+log E_z(α)+O(log L).

La suma finita con cualquier último peso admisible y mayor primo ≤Kz, K=4+κ/b, satisface log |C|≤αL+Σ_{z<p≤Kz}p^(−α)+O(1) por el mayorante positivo de 393 (la desigualdad de módulos sigue válida en caso de cero). Como log E_z(α)≥Σ_{p≤z}p^(−α), basta comparar sumas de primeras potencias. Usar la misma α evita calcular el segundo término de su posición.

Poner I(T)=∫₂ᵀ t^(−α)dt/log t, manteniendo α congelada. Para T comparable a z, la suma prima hasta T e I(T) difieren en o(L/b²) por sumación parcial del PNT con resto clásico: el tramo t≤√z cuesta O(z^(1/4)log z), y más arriba el ahorro exp(−c√b) domina cualquier potencia de b. Así la diferencia de las dos sumas es I(Kz)−2I(z)+o(L/b²). Se tiene I(z)∼L/b por integración en el extremo superior y c_b→log 2.

Cambiando t=4s en I(4z), el intervalo s<2 sólo aporta O(1) (se integra desde 1/2, donde log(4s)=log 2). Contra el peso s^(−α)/log s de I(z) se introduce el multiplicador 4^(1−α)log s/(log s+log 4). La media ponderada de 1/(log s+log 4) es (1+o(1))/b: en s≤exp(b−√b) la fracción de masa es O(poly(b)exp(−c√b)), y en el resto el equivalente es uniforme. Por ello

    I(4z)−2I(z)=[−2(1+log 2)log 4+o(1)] L/b².

Finalmente I((4+κ/b)z)−I(4z)=(κ/4+o(1))L/b², por el valor uniforme del integrando en ese segmento orientado, usando exp(−c_b)→1/2. Por tanto el logaritmo del mayorante finito menos log|S| es a lo sumo

    [κ/4−2(1+log 2)log 4+o(1)] L/b².

Si el coeficiente es negativo, ni siquiera la masa absoluta permite la igualdad exacta. El término O(log L) del prefactor de la silla es despreciable a esta escala. El argumento identifica un intervalo excluido por encima de cuatro y no da un corte que alcance S.

**Registro de revisión.** Con α=1/2+c_b/b, el factor4^(1−α) es2(1−c_b log4/b+O(b^(−2))); la media del cociente log s/(log s+log4) es1−(log4+o(1))/b. Su producto da2−2(1+c_b)log4/b+o(1/b). Como I(z)∼L/b y c_b→log2, se conserva exactamente el coeficiente−2(1+log2)log4 sin requerir un segundo término para c_b. Para desplazar4z porκz/b, el integrando en4z vale(1/4+o(1))L/(zb): el factor1/2 de4^(−α) y el factor1/2 de exp(−c_b) explicanκ/4. La fórmula vale también paraκ negativo con el segmento orientado. Los errores PNT son o(L/b²), y O(log L)=o(L/b²), de modo que ninguno cambia la constante.

Para cadaκ estrictamente inferior a8(1+log2)log4 se excluye bajoRH toda representación con primo terminal≤(4+κ/b)z, para todo x suficientemente grande; dejarκ subir al umbral da el liminf indicado. El descarte incondicional es el de un techo eventual: ese techo, si existiera, sería de escala L^(2+o(1)) e implicaríaRH por393. No se deduce un piso punto a punto ni el mismo liminf sinRH, ni existencia de una representación en el extremo de la constante.
