# POWER_SHIFTED_WRONSKIAN_092 — Cero real del determinante de eliminación

Estado: **PROVED; lectura final y auditoría independiente aprobadas.** Véase `POWER_SHIFTED_WRONSKIAN_AUDIT_092.md`. Se reutiliza el único certificado puntual087 sin modificarlo. No nuevo truncamiento theta, malla, precisión o parámetro explorado. Papers intactos. El resultado sólo limita una carta de eliminación invertible: no contradice el signo de W ni demuestra un polo inevitable de la solución o de todos los coeficientes de una ODE alternativa.

## 1. Diferencia y consulta de antecedentes

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README, R162_2300_MASTER_GRID y CROSSWORD-TO-D, y las fuentes077,087–090.087 decidió el Wronskiano original de cuatro densidades en el origen;089 probó su signo global.090 no permite heredar el siguiente signo sólo de una desigualdad de Turán. El objeto nuevo aquí es el determinante **de la eliminación de dos incógnitas**, con su identidad exacta como Wronskiano desplazado. Se comprueba una premisa concreta de esa eliminación usando jets ya certificados, no otro caso de la forma W.

## 2. Objeto y determinante exacto

Todas las derivadas de esta sección son en t>0. Fijar

    w=t Phi, v=−Phi', L=D_t²,
    p=V', V=−logPhi, A=w''/w, B=v/w,
    k=B'>0, J=(A'/k)'>0,
    b=k'/k, j=J'/J, m=2w'/w.

077 controla k,J estrictamente positivos. Sea a=M'(0)>0,c=1/a y K''=v−cw, con K(0)=K(infinito)=0. Para F=K/w,

    F''+m F'+AF=s, s=B−c.

El operador mónico que anula(1,B,A) es

    D3=D³−(2b+j)D²+(b²+bj−b')D.

Escribir H=m+2b+j. La sustitución de la ODE da exactamente

    Y=D3F=T0+UF'+Vc F,
    T0=k−Hs,
    U=Hm+b²+bj−b'−m'−A,
    Vc=HA−A'.

Entonces Y'−T0'−Us=(U'−mU+Vc)F'+(Vc'−AU)F. La inversión de este sistema2×2 exige

    Delta=U(Vc'−AU)−Vc(U'−mU+Vc) != 0.

La identidad exacta relevante es

    Delta=−W_t(w'',v'',w'''')/[w³ k² J].          (SHIFT)

Prueba: los homogéneos de f''+mf'+Af=0 son h1=1/w,h2=t/w y W(h1,h2)=w^−2. La transformación(h,h')→(D3h,(D3h)') tiene determinante−Delta. Por eliminación de filas del Wronskiano,

    W(D3h1,D3h2)=W(1,B,A,h1,h2)/W(1,B,A).

Aquí W(1,B,A)=k²J. Multiplicar las cinco columnas por w aporta w^−5; mover las columnas(1,t) delante requiere seis transposiciones, signo positivo. Expandir sus dos primeras filas deja W(w'',v'',w''''). Así W(D3h1,D3h2)=W(w'',v'',w'''')/(w^5 k²J)=−Delta/w², lo que prueba SHIFT.

## 3. Origen: sólo los intervalos ya certificados087

Escribir Phi(t)=Phi(0) sum a_r t^(2r), a0=1. Por paridad y cambio lambda=t²,

    Wshift(t)=W_t(w'',v'',w'''')
             =8 Phi(0)³ t^6 [D0+O(t²)],

    D0=det [[6a1,−24a2,120a2],
            [20a2,−120a3,840a3],
            [84a3,−672a4,6048a4]]
       =−161280(6a1a3a4−8a2²a4+3a2a3²).

Los factores de las filas son derivadas normalizadas correctamente: para tres funciones impares t f_i(t²), W_t=8t^6 W_lambda(f_i). Sólo se necesitan derivadas pares de Phi hasta orden8;087 ya certificó hasta10 con TODA la cola theta y el prefactor pi exp(5t/2).

El verificador092 importa mediante runpy el verificador087 **sin editarlo** y evalúa únicamente el polinomio precedente con su misma aritmética racional outward. Obtiene y verifica exactamente

    −56488961026 < D0 < −56488961025.

Por continuidad analítica, Wshift(t)<0 para todo t>0 suficientemente pequeño. No se asigna un radio no certificado a esa vecindad.

## 4. Exterior con resto controlado, no sólo un principal formal

Poner y=pi exp(2t). Los bounds completos de088, válidos para t>=1,y>=21, dan

    |V^(r)(t)−2^r y| <=65, r=1,...,6.            (JET)

En efecto el primer modo es un producto de exp(−y+9t/2) por(1−3/(2y)). Las derivadas del logaritmo de este último factor se acotan por 2^r sum n^(r−1)/14^n<2^r, y088 acota por2E<1 las derivadas hasta6 del logaritmo de la corrección de TODOS los modos restantes. El término lineal9t/2 sólo afecta r=1, donde también sobra65.

Tras factorizar Phi en las tres columnas, Wshift/Phi³ es un polinomio P(t,p1,...,p6), con p_r=V^(r). Se define explícitamente como el determinante de las filas0,1,2 de derivadas de

    g1=t(p1²−p2)−2p1,
    g2=p1³−3p1p2+p3,
    g3=t(p1^4−6p1²p2+3p2²+4p1p3−p4)−4g2,

donde la derivación formal es Dt=1,Dp_r=p_(r+1). El grado en t es<=2 y el grado total en los p_r es<=9. Su parte homogénea de grado9 es W(t p1²,p1³,t p1^4), exactamente

    −2p1^6(2p1²p2+t p1²p3−t p1p2²−t²p2³).

Al sustituir p_r=2^r y+e_r se concluye

    P=4096(2t²−1)y^9+Q(t,y,e1,...,e6),

donde cada monomio de Q tiene grado en y<=8 y grado en t<=2. Ésta es una identidad polinómica, no una aproximación numérica. Definir la constante finita explícita

    Cstar=sum |coeficiente de Q| ·65^(grado total en e).

Por JET, para t>=1,y>=21,

    |Q| <= Cstar t² y^8.

Como 2t²−1>=t², si y>Cstar/4096 entonces P>0. Existe por tanto una cola completa en la que **Wshift>0**. No se necesita calcular un umbral óptimo ni examinar puntos; Cstar queda definido por un polinomio finito exacto y el resto incluye todos los modos theta mediante JET.

## 5. Consecuencia precisa y límites

Wshift es continuo, negativo cerca0 y positivo eventualmente. Tiene al menos un cero t*>0. Como w,k,J son estrictamente positivos allí, SHIFT implica Delta(t*)=0.

Por consiguiente, las fórmulas de eliminación que dividen por Delta no están definidas globalmente como una carta invertible. **Esto no demuestra que sus coeficientes tengan polos no removibles**: sus numeradores pueden también anularse. La función real K sigue siendo suave, y siguen disponibles otras cartas, operadores, particiones o argumentos sin esa división. No se excluye una prueba de signo por esos medios. No nuevo signo de W, número de generadores, T o todos los órdenes.

Matización adicional aprobada: las dos imágenes Y1=D3(1/w),Y2=D3(t/w) son suaves y satisfacen W(Y1,Y2)=−Delta/w². Este Wronskiano no es idénticamente cero, pero tiene un cero interior. No puede existir una ODE homogénea mónica de orden2, con coeficientes continuos en TODA la semirrecta, que contenga simultáneamente ambas imágenes: si Y''=beta Y'+alpha Y, la identidad elemental W'=beta W impide un cero aislado o parcial de un Wronskiano no idénticamente nulo. Esto excluye remover globalmente todos los coeficientes de la ecuación universal común conservando esas dos soluciones; no excluye cancelaciones para la solución particular K, una ecuación inhomogénea distinta, otro orden o representación.

Verificación reproducible: `python3 tools/power_shifted_wronskian_092_verify.py` desde phase211. El script imprime los extremos racionales y ejecuta los asserts anteriores; no altera087.
