# POWER FRONTIER AUDIT 036

Estado: RECURRENCE_BOUNDARY036 y MOVING_BALANCE036 APROBADOS. Papers intactos.

## 1. Corpus y diferencia exigida

Reconsultados índice de rutas, grid y crucigrama y los antecedentes DESCENT_AUDIT016, TABLE_AUDIT018 y SIGNED_TRANSFORM035. La ley beta y la expansión binomial ya existían016; el borde fijo tenía energía que tendía a0, sin resolver el interior.018 prueba que recurrencias, regiones positivas y eventualidad no bastan por sí solas.035 añade datos reales finitos y una ley específica, sin control del promedio aritmético móvil.

036 requiere por tanto una nueva cota de ENERGÍA de la forma real, no sólo una probabilidad o una urna renombrada. La conclusión acotada no se registra como imposibilidad global de otras fronteras o nuevas estimaciones firmadas.

## 2. Frontera diagonal completa — APROBADA

Revisado `POWER_RECURRENCE_BOUNDARY_036.md`. La recurrencia normalizada tiene pesos alpha/S y beta/S; iterarla da la beta-binomial exacta con j incrementos de N. Las normas beta incluyen correctamente u^(1−2N)/(2π). La expansión finita conserva todas las partes de W, incluido el polar.

INV se obtiene exactamente de E[(1−Q)^−1|J]=(S+L−1)/(beta+J−1) y requiere N≥2. En el cono parabólico N+j≤sqrt((k+L)/C), de modo que el momento inverso domina su masa con el signo correcto. Los casos de conjunto vacío y parte positiva están tratados. La masa del cono es O(L^−1/2).

SYMBOL trasladaψ hasta5/4, resta un recíproco positivo y usa resto EulerB1≤.4. Se conserva una cota SUPERIOR ARCH≤H_L mediante Jensen y Eτ²=u²(k′+.5)/(N′−1.5), uniformemente en toda la frontera. Los bounds reales017 de peine y polar son ambos<.001 y W>.98 en el cono, con exactamente sus hipótesis. Así0≤C_L≤M_L(H_L+.002)=O(logL/√L), no sólo un resultado sobre su norma.

FRONT es finita y exacta, por lo que R_L=A_start−C_L converge al valor original sin necesidad de integrabilidad uniforme del complemento. El ejemplo positivo211,1 reutiliza032 como resto real no nulo; no es otra evaluación ni un contraejemplo de signo. Esta cota sobre TODO el cono parabólico creciente es distinta del borde fijo016.

## 3. Frontera detenida — APROBADA con alcance separado

Cada camino tiene el peso creciente factorial declarado, independiente del orden; contar sólo caminos que evitan el cono produce STOP-WEIGHT y una identidad finita de primeras llegadas más resto. Bajo Q≤1/3,2^(r−j) es una supermartingala no negativa. Al tocar el cono, r−j≥CN²−k porque C(N+j)²−j≥CN². La desigualdad maximal y el límite monótono dan SURVIVAL con probabilidad beta positiva. No se infiere de esa masa un límite de energía detenida.

La región034 fija N′≤17 es inaccesible desde N≥18 y la recurrencia positiva no disminuye N ni k. Por tanto estos datos no suministran el lower firmado del complemento. El resultado localiza exactamente la obligación y refuta la supresión de ese resto en ESTE esquema; no prueba un no-go global ni nuevo signo W/T. Root coincide independientemente en todos estos pasos.


## 4. Ventana energética de componentes reales — APROBADA

Revisados `POWER_MOVING_BALANCE_036.md` y `tools/power_moving_balance_036_verify.py`; ejecución independiente PASS. Las leyes de energía polar/prima se obtienen por la MISMA mezcla finita gamma, conservando todos los contactos. Son positivas normalizadas; no son leyes del funcional firmado total.

La integral beta reconstruye exactamente a_mr^m y Qtilde como mezcla binomial. Para r63/62, el máximo tau1/64, valor lambda3969/3968, curvaturaalpha(64/63)² y p(tau)=1/32 son exactos. El intervalo normalizador de radio63/(128√d) tiene masa al menos189lambda^d/(256√d). La cola gaussiana del peso y Hoeffding binomial, junto con |p′|<3, dan CONCENTRATION con el exponente1024/35721. No se usa una aproximación normal ni sólo un punto estacionario.

El polar de S_j es exactamente4(r^(j+1)−s^(j+1)). Con delta_v≤a_m/d y m≤d se domina su peso por C0a_mr^m. La integral Laplace normalizada da P_N≥2A_d(r)/31 y por tanto el factor polarDOM3969. La fórmula gamma y las cotas Jensen de la razón gamma validan la fase exponenciallambda^N.

CHEB está demostrado para la Lambda real: las valoraciones del binomio central se dominan por las potencias primas hasta2n y su tamaño≥4^n/(2n+1). El extremo32 y la derivada positiva prolongan psi≥x/2−16 a toda la semirrecta. La integración por partes tiene el borde w(1)=1 y produce Pi≥Lplus−31≥P/2−33. El umbral monotónicoN≥2^20 garantiza P>132 y Pi≥P/4 sin evaluar W.

Para el upper, psi≤xlogx y w_j decreciente dan2∫(t+1)e^(t/2)S_j; las sumas gamma producen el factor4[1+(j+1)/31]r^(j+1). La dominación aritmética resultante15876[1+(d+1)/31]Qtilde es correcta y su prefactor polinomial es vencido por CONCENTRATION. Así AMBAS energías reales concentran m/d→1/32, y sus fases exponenciales coinciden. No se deduce Pi/P→1 ni una precisión del residuo por esa coincidencia.

La ventana C√d tiene energía relativa de ambos componentes que tiende a0, aunque la ley normativa P_d tenga esa escala. Los perfiles ARCH permanecen uniformemente acotados porque e^−ut≤S_j≤1. Se demuestra por tanto que no se pueden descartar por separado las colas energéticas por un argumento de masa035. Una compensación DENTRO del funcional firmado antes de promediar no queda refutada ni localizada por estas leyes separadas.

## 5. Cierre de alcance

La ronda aporta cotas nuevas de energía: todo el cono parabólico en una frontera diagonal y la banda lineal de los dos componentes reales bajo la ley gamma. Ninguna es otra identificación beta o una identidad de recurrencia promovida a signo. Delimitan procedimientos concretos que omiten un resto real, sin cerrar el objetivo por dificultad ni declarar imposibles otras fronteras o compensaciones. No hay nuevo signo W, nueva cobertura o ventana T. Root coincide independientemente en ambos memos y en el verificador de constantes.
