# AUDIT_002 — Covarianza puncturada y Mellin

2026-10-18. Revisión independiente de CONSTRUCTOR_002 §§0–6. Fila D independiente.

**Veredicto: lemas 1–5 PROVED con sus alcances; enlace Q_T OPEN.** El propio constructor declara correctamente que no alcanzó el hito del README.

## 1. Probabilidad e identidad de divisores

La normalización τ=θ−1 es positiva y las probabilidades de divisibilidad son τ(d²y)/τ(y). X_d X_e=X_lcm. La PSD y su extensión por integración positiva son genéricas y el memo no las presenta como especificidad. Poisson para τ y para los cocientes es exacto, conservando el término de origen y las escalas fraccionarias.

La suma truncada de Λ(d)1_{d|N} está dominada por log|N| y converge a ella punto a punto; el momento cuadrático es finito bajo gaussiana. Convergencia en L² justifica la identidad de varianza como límite conjunto, sin intercambiar indebidamente una doble serie firmada.

## 2. Mellin

En cero, τ(y)=y^(−1/2)−1+error exponencial tras Poisson, por lo que q_y(d)=1/d+O_d(√y). La expansión de C_y es G₀+O(√y) y G₀=(gcd−1)/(de). En infinito las razones decrecen exponencialmente porque el menor entero no nulo del denominador tiene |N|=1. Esto prueba convergencia absoluta entrada a entrada de I_α para α>0 y PSD sobre sucesiones finitas.

La transformada separada de τ(l² y) para α>1/2 es 2π^(−α)Γ(α)ζ(2α)l^(−2α), con factor 2 correcto. El resto con denominador τ converge separadamente allí. La multiplicación por τ recupera la homogeneidad Mellin de un término a costa de perderla en el cociente: no se puede concluir una ley de peso crítico sólo por escoger α=1/4.

## 3. Renormalización

B_y=y^(−1/2)G₀+O(1) cerca de cero y decae exponencialmente en infinito. Restar y^(−1/2)G₀ en toda la semirrecta da convergencia para 0<Re α<1/2. Dividiendo en 1, la resta de la cola produce G₀/(α−1/2), signo correcto, y −4G₀ en α=1/4. La expresión dividida prolonga meromórficamente desde Re α>1/2 hasta Re α>0 con posible polo en 1/2.

La identidad R_α=I_α+H_α es exacta. H_α converge: cancelación del término y^(−1/2) en cero y potencia integrable en infinito. Ninguna positividad de H ni R se deriva de la de I. El constructor conserva explícitamente esta incógnita.

## 4. Origen y límite del signo

La descomposición por el evento N=0 es exacta:

    C⁰=(1−p₀)C×+p₀(1−p₀)u_y u_y*, u_y(d)=1−r_d.

No es lícito identificar esa dirección dependiente de escala con cosh(x/2) sin mapa de tests. Para coprimos d,e>1, la asintótica negativa de C× se sigue porque ((de)²−1)−(d²+e²−2)>0. No hay contradicción con PSD: una matriz PSD puede tener entradas cruzadas negativas.

La asociación estricta de la theta completa, revisada separadamente en POSITIVE_ASSOCIATION_002, tiene una fuente efectiva en Poisson, pero quitar el origen ya cambia su signo cruzado aun sin borrar un primo. Eso impide presentar la especificidad por borrado como prueba suficiente de un nuevo signo para el ortogonal polar.

## 5. Puertas

La familia C_y no es función universal de de, por el contraejemplo de límites (2,6) y (3,4). Esto no prueba una propiedad equivalente para I_α en un α fijado, y el memo lo distingue. Tampoco produce todavía un núcleo de alturas ni demuestra salida del álgebra efectiva en el dominio de Q_T.

No hay traducción a BR, certificado def:PD ni identidad puntual de thm:sos. Los lemas positivos de covarianza no reabren Gram como ruta al nodo: el enlace específico es el trabajo pendiente. La opción a_d=Λ(d)d^(−1/2)F(log d) es cuadrática en evaluaciones de F, pero no reproduce la dependencia de autocorrelación sin prueba adicional. La advertencia de grado cuatro al usar autocorrelaciones como coeficientes es correcta.

Resultado: construcción explícita coherente y un resto de desnormalización localizado; no positivo aritmético útil demostrado para Q_T. El revisor continúa examinando un posible signo cruzado estricto de la covarianza puncturada, que sería un lema distinto de su PSD genérica y requerirá auditoría separada.
