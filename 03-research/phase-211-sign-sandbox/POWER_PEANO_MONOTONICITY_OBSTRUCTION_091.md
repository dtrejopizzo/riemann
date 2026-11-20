# POWER_PEANO_MONOTONICITY_OBSTRUCTION_091 — El kernel de Peano no es monótono

Estado: **PROVED; fuente y revisión independiente aprobadas.** Véase `POWER_PEANO_MONOTONICITY_AUDIT_091.md`. Se refuta un criterio suficiente muy específico para el menor anclado: la monotonía global de Pi(s)/s para todos los conjuntos de cuatro nodos. El fallo ocurre para la MISMA Phi real y nodos suficientemente próximos a cualquier t0>0. No se refuta el signo de la integral final, el nuevo determinante, una implicación alternativa desde R4 ni W. Papers intactos; sin campañas.

## 1. Consulta y diferencia precisa

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D; cotejados065 y086–090. La búsqueda de Peano, prefijos de cofactores y monotonía de este kernel no encontró este objeto en el corpus ni en los tres registros.

La propuesta nueva usaba el cruce único de zeta=v−cw y su momento nulo para pagar el determinante con una primitiva positiva K. El objetivo era deducir su signo de una monotonía de Pi/s. Aquí se prueba que esa monotonía falla localmente para los datos reales, aunque el sistema previo de cuatro densidades sea ECT. Es un NO-GO del criterio de monotonía declarado; no de la estrategia de integración por partes ni de toda estimación de compensación.

## 2. Datos reales y representación integral exacta

Poner w(t)=tPhi(t), v(t)=−Phi'(t), a=M'(0)>0 y c=1/a. En esta fuente K designa la primitiva IMPAR positiva

    zeta=v−cw,
    K(t)=int_t^infinito(s−t)zeta(s)ds, t>=0,
    K''=zeta, K(0)=0.

No es la K PAR de078. Todas las colas pertinentes decaen más rápido que cualquier exponencial. Las identidades de momentos reales dan

    int_0^infinito s zeta(s)ds=0.

En efecto int s v=int Phi y int s w=int s²Phi=a int Phi, sobre la semirrecta. Por077, B=v/w=p/t es estrictamente creciente, así zeta tiene un solo cruce de negativo a positivo; llamarlo b. Esta representación y ese cruce no se presentan como un nuevo resultado.

Fijar cuatro nodos positivos t1<t2<t3<t4. Definir los cofactores de la última columna

    ell_i=(−1)^(i+4)det[(w(t_j),v(t_j),w''(t_j))]_(j≠i),
    Pi(s)=sum_(i=1)^4 ell_i(s−t_i)_+.

La expansión por esa columna y Fubini dan exactamente

    det[w,v,w'',K]_(t1,t2,t3,t4)
       =sum_i ell_i K(t_i)=int_0^infinito zeta(s)Pi(s)ds.

Es lícito intercambiar la suma finita y la integral: Pi crece a lo sumo linealmente y zeta tiene las colas declaradas. Usando el momento nulo,

    det[w,v,w'',K]
       =int_0^infinito s zeta(s)
                   [Pi(s)/s−Pi(b)/b]ds.             (PEANO)

Una función Pi(s)/s decreciente daría signo no positivo en PEANO; una creciente daría signo no negativo. La propuesta examinada necesitaba una de esas monotonías globales, para TODOS los conjuntos de nodos. Se demuestra a continuación que ninguna es cierta.

## 3. El Wronskiano real de tres funciones es positivo

Las identidades086 son

    v/w=B=p/t,
    w''/w=A=p²−q−2p/t,
    k=B'>0, J=(A'/B')'>0.

Por tanto, en el orden de columnas que se usa aquí,

    W3(t)=W(w,v,w'')(t)
          =w(t)³ W(1,B,A)(t)
          =w(t)³ B'(t)²J(t)>0, TODO t>0.           (REAL-W3)

No se usa el orden(1,A,B), cuyo signo sería el opuesto. Esta comprobación fija los signos de los cofactores y no presupone ningún nuevo dato de cinco columnas.

## 4. Lema de Taylor para cuatro nodos equiespaciados

Fijar CUALQUIER t0>0 y tomar

    t_i=t0+(i−1)epsilon, i=1,2,3,4, epsilon>0.

Para tres offsets fijos r1<r2<r3, la expansión de Taylor de las filas da

    det[(w,v,w'')(t0+r_j epsilon)]_(j=1)^3
      =epsilon³ W3(t0)
          ·Vandermonde(r1,r2,r3)/(0!1!2!)+O(epsilon^4).

La suavidad real permite el resto indicado. Los primeros órdenes no nulos usan derivadas de órdenes0,1,2, cuya suma es3. El determinante de sus coeficientes es la Vandermonde de los offsets y las columnas de derivadas producen precisamente W3. Los términos repetidos de menor orden se anulan.

Al omitir respectivamente los offsets0,1,2,3 del conjunto(0,1,2,3), las Vandermonde son

    2, 6, 6, 2.

Dividir por0!1!2!=2 y añadir los signos de cofactor da

    (ell_1,ell_2,ell_3,ell_4)
      =epsilon³ W3(t0)(−1,3,−3,1)+O(epsilon^4).      (COFACTORS)

El factor no es epsilon³W3/2: el2 de los offsets adyacentes ya cancela el factorial. No se normalizaron los cofactores por una Vandermonde global.

## 5. Dos intervalos con derivadas de signos opuestos

Fuera de los nodos, derivar la expresión de Pi da

    (Pi(s)/s)'=[sum_(t_i<s)ell_i t_i]/s².          (PREFIX)

En(t1,t2) el numerador es

    ell_1t_1=−t0W3(t0)epsilon³+O(epsilon^4)<0

para epsilon suficientemente pequeño. En(t2,t3) el numerador es

    ell_1t_1+ell_2t_2
       =2t0W3(t0)epsilon³+O(epsilon^4)>0.

Ambos signos son estrictos por t0>0 y REAL-W3. Así, para TODO t0>0, existe epsilon0(t0)>0 tal que para0<epsilon<epsilon0,

    Pi(s)/s decrece estrictamente en(t1,t2),
    Pi(s)/s crece estrictamente en(t2,t3).

En particular no es monótona globalmente, en ninguno de los dos sentidos. Es una prueba de existencia analítica de familias de nodos; no se eligieron ni buscaron nodos numéricos.

## 6. Alcance exacto y residuo vivo

El resultado usa la Phi REAL, no sólo una clase auxiliar: REAL-W3 ya está probado086. Tampoco necesita refutar el ECT R4 real089, que permanece válido. La cancelación ∫s zeta=0 y el cruce único continúan siendo herramientas correctas; lo que falla es sustituir el problema por monotonía global de Pi/s para todos los nodos.

La integral PEANO aún podría tener el signo requerido mediante compensación entre los intervalos donde Pi/s sube y baja, una comparación con la posición y masa del cruce b, o un kernel distinto. Nada de lo demostrado decide ese signo. No se afirma que el dato R4 sea insuficiente para TODOS los argumentos posibles ni que el dato de cinco columnas sea imposible. El menor anclado y T_h de la Phi real siguen OPEN.

No cambia la positividad W ya probada085 ni el paso S_G''<0 real090. No se obtiene un nuevo contraejemplo W, un cierre global ni una campaña de certificados.
