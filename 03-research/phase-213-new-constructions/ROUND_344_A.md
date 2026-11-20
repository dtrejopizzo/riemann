# Qué términos compensan el rectángulo aislado

En el observable A_h de 338 usar D=2√X y P,L de 342. Para cada primer índice d≤D llamar fila completa a la suma sobre todos los e≤D y todos los k, manteniendo los dos pulsos W_x(kde)−2W_x(2kde) y los coeficientes μ(d)μ(e). Entonces para X grande:

* Antes de retirar los productos pequeños, **cada fila con √X≤d≤2√X es exactamente cero**, uniformemente para X≤x≤2X.
* Después de imponer de>P, la suma de los valores absolutos de los saldos de todas esas filas es O_B(X^(−B)) para cada B fijo. Así el rectángulo difícil de 340 tiene un complemento explícito en sus propias filas que lo compensa, aun antes de integrar.
* En C_h de 342 se pueden imponer a la vez la nueva restricción de filas y la poda por cocientes de 342. Sólo queda estudiar filas L<d<√X con e≤D, de>P y cociente reducido de altura >X^ρ, además de la copia con límites escalados. Aquí ρ<1/6−7δ/6 y δ=1/j, j≥16.

**Filas completas.** Para cualquiera de los dos pulsos y un d fijo, agrupar por m=ek. El coeficiente interior es Σ_{e|m,e≤D}μ(e). Si d≥2X/D, todo m que alcanza el soporte cumple m≤2X/d≤D. También m>1 para X grande pues d≤2√X y el soporte de ambos pulsos exige dm≥Xe^(−h)/2. Por inversión de Möbius el coeficiente se anula para cada m individual. Esto incluye el intervalo I_Y del rectángulo 340; allí los términos con e∈I_Y pueden ser grandes, y los demás e de la misma fila dan exactamente su negativo. La cancelación usa los signos aritméticos y vale separadamente en los dos pulsos antes del recorte.

**Restaurar el recorte.** Para de≤P, la suma de los dos pulsos en k de 338 cuesta O_N(X^(−(N−1)δ/4)) por pareja, por Poisson con cancelación de las integrales. Como hay O(X) parejas, los errores se pueden sumar en módulo incluso por filas. Tras exigir de>P las cotas d,e>L son automáticas. En la copia x/4 todos los límites de índices se dividen por dos, incluido 2X/D, y el del producto por cuatro. Las dos familias de filas se retiran con el mismo ahorro arbitrario.

**Compatibilidad con los cocientes.** Después de retirar estas filas, a cociente r/s fijo el intervalo J de 342 se intersecta con gr<√X. La segunda copia tiene exactamente el intervalo J/2. La cancelación de densidades y la cota para la variación de cada pulso recortado permanecen válidas. Esto justifica la poda conjunta sin suponer que dos conjuntos pequeños tengan intersección pequeña.

**Qué queda de la identidad.** Para las filas restantes el cociente m puede superar D. El saldo exacto pasa a −Σ_{e|m,e>D}μ(e); si D<m≤2D sólo queda −μ(m). Por ello la anulación demostrada para las filas superiores no se extiende formalmente a todo el bloque. Es inversión elemental de divisores; la aportación respecto de 340 y 343 es identificar los compensadores en el observable completo y verificar que sobreviven los dos recortes de 342. El signo global sigue abierto.
