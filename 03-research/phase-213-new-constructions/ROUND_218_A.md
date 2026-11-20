# Cancelación obligatoria entre dos sumas ya firmadas de primos

En la muestra C_k de 217 separar TODOS los primos p≤exp(k/3) de los mayores, conservando dentro de cada grupo sus signos y todo el integral oscilatorio en u. Llamar P_k al primer grupo. Se tiene

    P_k ∼ 3^(−√k+ik) exp(k/6−ik) k^(−3/2) · H/(1/2−3i),
    H = 3 exp(−1/4)/(2√π) · ∫₀^∞ exp(−r−ir²/2)dr ≠ 0.

La equivalencia es compleja. Luego C_k−P_k∼−P_k, incondicionalmente. En efecto 217 y |γ|>14, |δ|≤1/2 dan limsup log(1+|C_k|)/k≤arctan(1/28)<1/6. El margen es mayor usando la altura verificada. 211 daba cancelación de una suma prima corta a tasa fija, en una subsucesión. 216 daba el coste de tomar módulos por primo después del integral. Aquí la señal sobrevive a AMBAS sumas firmadas (en primos y en tasas) para TODO entero suficientemente grande. El corte k/3 se escoge para que las dos fases tengan derivadas iguales en u=3.

**Coeficiente de borde.** Para L=k/3+d, definir I_k(L) como en 216 pero con el peso u^(−√k+ik−1) de 217. Sea F_k=3^(−√k+ik) exp(−ik) k^(−3/2). Se tiene, para d en compactos,

    I_k(k/3+d)/F_k = H exp(−3id)+o(1).

En efecto, en u=3exp(r/√k), du/u=dr/√k, el peso restante da 3^(−√k+ik)exp(−r+i√k r). Para cada r acotado el indicador de corte es uno eventualmente, pues log X_(k²)(u) es de orden k² allí. Por la escala y el perfil de 211,

    k c_(k²)(L;u) = u exp(−(uL/k)²/4) cos(uL)/√π + o(1)

uniformemente en r,d compactos. La envolvente previa k|c|≤Cu da dominación en todo r≥0 por C exp(−r/2) tras el cambio, para k≥4, aun con el indicador. En la rama negativa del coseno usar uL=k+√k r+r²/2+3d+o(1). Tras quitar exp(−ik) queda el integral indicado. En la rama positiva queda la oscilación adicional exp(2i√k r), multiplicada por un prefactor de módulo uno y un perfil que converge en L¹ luego de extraer esa fase (y la fase constante). Riemann–Lebesgue da o(1). Los errores son uniformes en d compacto por Taylor uniforme en r acotado y la dominación común. El factor integral de H difiere de 1 en módulo de la diferencia estrictamente menos que ∫ exp(−r)r²/2 dr=1, pues |exp(−ix)−1|<x para x>0. Esto prueba H≠0.

**Suma prima hasta el corte.** En d=log p−k/3 con −D≤d≤0 fijo, el PNT da convergencia débil de la medida exp(−k/3)Σ(log p)δ_d a exp(d)dd, en ese compacto. Multiplicar por p^(−1/2) exp(k/6)=exp(−d/2) y usar el perfil uniforme da, tras normalizar P_k por F_k exp(k/6), la contribución H∫_(−D)^0 exp((1/2−3i)d)dd. Para d<−D se usa |I_k(L)|≤C|F_k|, uniforme en L por la envolvente k|c|≤Cu y el cambio en r. Chebyshev y sumación parcial dan Σ_(p≤X)(log p)/√p≤C√X. La cola normalizada por tanto cuesta O(exp(−D/2)). Tomar D→∞ prueba la fórmula sin exigir tasa de error en PNT.

**Consecuencia para la ruta.** Estimar separadamente en módulo estos dos bloques de primos ya cuesta exp(k/6+o(k)); la meta de 217 es exp(o(k)) en una subsucesión. El término principal de P_k se obtiene de la densidad continua, con su fase compleja explícita. Restarlo puede quitar ese término, pero el o(1) relativo del PNT sólo da error o(|P_k|), insuficiente por sí solo en la escala requerida. No se ha probado control subexponencial del residuo conjunto.
