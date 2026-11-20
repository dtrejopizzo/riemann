# Cuatro colas en una ventana común, incluso en colisiones parciales

Existen L₄>0 y c₄>0 tales que W(F)≥c₄||F||₂² para cualquier dato admisible en [−L₄,0] seguido por cualquier bloque racional de hasta cuatro polos reales −u_i, u_i>1/2, con multiplicidades arbitrarias. No se necesita positividad de un bloque con cinco polos. Es una aplicación de los certificados de 084–085 de POWER y de la separación de tasas de 213-198. No se estima numéricamente L₄.

**Un determinante relativo que conserva el margen en las colisiones.** Escribir M(u)=(ξ'/ξ)(u+1/2), x_i=u_i², R(x)=u/M(u), S(x)=uM(u), P=∏_{i<j}(u_i+u_j) y Δx=∏_{i<j}(x_j−x_i). Para cuatro tasas distintas, K_{ij}=(M(u_i)+M(u_j))/(u_i+u_j), G_{ij}=1/(u_i+u_j) es el Gram temporal L². Con D_f=det[1,x,f(x),xf(x)] evaluado en los cuatro x_i se tiene exactamente

    det K / det G = (∏_i 2M(u_i)) P² (D_R/Δx)(D_S/Δx).

En efecto 083–084 dan det K=D_R D_S/(P²∏R_i); el determinante de Cauchy da det G=Δu²/(P²∏2u_i), donde Δu=∏_{i<j}(u_j−u_i) y Δx=P Δu. El cociente de determinantes es invariante por cambio de base simultáneo.

**Cota compacta explícita a partir de tres derivadas.** En una caja de cuadrados J=[1/4,V²], V>1/2 fijo, para f=R,S se conocen f'>0, f''<0 y T_f=2f'f'''−3(f'')²>0 por POWER_FOUR_TURAN_084 y POWER_FOUR_GENERATORS_085. En el extremo izquierdo f'>0 por monotonía de f' y positividad interior; si f'' se anulara allí, T_f>0 daría f'''>0, incompatible con f''<0 inmediatamente a la derecha. Sean m_f=min_J |f''| y h_f=min_J T_f/(f'')², ambos positivos. Entonces

    −D_f/Δx ≥ m_f² h_f/12.

Para verlo, restar filas consecutivas (de abajo arriba), expandir por la columna constante y escribir cada diferencia como integral de su derivada. Queda una integral de un determinante con columnas [1,f',(xf)'] en tres puntos ordenados t_i∈[x_i,x_{i+1}]. Repetir el paso: quedan dos puntos z_1≤z_2 y el integrando f''(z_1)f''(z_2)[H(z_2)−H(z_1)], H=(xf)''/f''. Su opuesto es ≥m_f² h_f(z_2−z_1) por H'=−T_f/(f'')². La integral del factor z_2−z_1 es Δx/12, aplicando los mismos pasos a las columnas [1,x,x²/2,x³/6]. El mayorante inferior del determinante relativo, estrictamente positivo, es independiente de cualquier separación entre tasas.

En una base de diferencias divididas temporales los dos Gram son continuos en toda la caja, incluyendo el extremo regularizado y multiplicidades parciales o totales. El Gram L² sigue invertible por independencia de las fracciones parciales en la base de Newton de 198. Como el Gram de W es PSD por límite y su determinante relativo queda separado de cero, es definido positivo en cada colisión. Por compacidad hay un piso uniforme respecto de L² en cada caja. La cota de determinante por sí sola no es una cota inferior del menor autovalor sin control de los otros tres; ese control aquí sigue de continuidad y compacidad.

**Incorporar el dato arbitrario.** Aplicar la contradicción secuencial de 198, ahora a listas de longitud ≤4. Para las tasas acotadas se usa el piso recién probado (para ≤3 sirve 198). Para las que escapan, la cota ponderada de Hardy en σ=min(u_i)/2 es ≤3⁴ por unidad de norma. De nuevo el piso arquimediano del componente rápido tiende a infinito. Todos los cruces de 198 siguen acotados: en una caja se toman hasta tres derivadas en v. En la fórmula lenta-rápida cada derivada adicional produce sólo un factor polinomial en t o log n, absorbible en exp(Ct); en la lenta-compacta, una potencia adicional de r en la integral de 197 es integrable y el término polar regularizado es analítico en v. El piso compacto crece al reducir la longitud y absorbe, junto con el piso rápido, los tres cruces por Young. Esto demuestra el enunciado, incluyendo coeficientes complejos. El procedimiento utiliza una desigualdad diferencial específica del orden cuatro; no da un límite en el número de polos.

**Antecedentes.** 084 ya calcula el Wronskiano y usa Rolle para el determinante de nodos distintos. La cota normalizada por Δx cuantifica el margen en toda colisión en la norma L² del bloque; el nuevo dato arbitrario que precede a las cuatro colas exige además el control de los cruces de la fase 213.
