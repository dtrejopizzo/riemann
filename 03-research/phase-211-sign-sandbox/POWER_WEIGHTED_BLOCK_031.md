# POWER_WEIGHTED_BLOCK_031 — Prefijo ponderado adverso y recuperación real en4

Estado: **PROVED**, revisión independiente por mapa aprobada y verificador PASS reproducido. Tasa FIJA u=63/2. Con X0=225/64=(15/8)²:

    int_1^X0 G_N H<−3/1000       para TODOS N>=2^24,
    int_1^4 G_N H>3/200          para TODOS N>=2^22,
    int_X0^4 G_N H>9/500         para TODOS N>=2^24.        (REAL)

No son valores totales de W. Resto del balance y signo global OPEN. Papers intactos. No se continúa una campaña de contactos.

## 1. Corpus y razón nueva

Leídos las reglas del proyecto, INTERIOR_SCALE030 y su auditoría; identidad JOINT-G, primitiva ponderada I_* y error gamma local. Consultados índice ROUTES-TRIED-INDEX, grid maestro y CROSSWORD-TO-D.md sobre medias ponderadas, primitivas, Euler/Möbius y bloques030. Las primitivas de H y x²H refutadas030 NO son el objeto aquí.

La diferencia es incorporar el PRIMER contacto siguiente, q3, en la primitiva ponderada por G_*=(3/2)x^(-1/2), y comprobar si su signo puede servir al emparejamiento real. La premisa universal I_*>=0 falla ya tras ese contacto. Pero, antes de pivotar, se extrae una recuperación CUANTITATIVA del bloque gamma real, uniforme en N y a tasa fija. No se certifican dimensiones aisladas ni se usa otro modelo en lugar de G_N.

Se evalúan sólo un prefijo adverso motivado dentro de(3,4), con extremo cuadrado racional X0, y el extremo4 que completa la celda del contacto3. El contacto4 está en el extremo y su contribución integral es exactamente0. No se genera una lista de signos para más contactos.

## 2. Peso real y primitiva correcta

Conserve030:

    G_N(x)=x^(-1/2)[(3/2)rho_N(logx)−rho_N'(logx)]>0,
    H(x)=1+[log((x+1)/(x−1))+c−1−2Psi_1(x)]/x²,
    c=−gamma−log(4pi), Psi_1(x)=sum_(q<=x)qLambda(q),
    W[g_N]/norm²=int_1^infty G_N(x)H(x)dx.

La primitiva en estudio es

    I_*(X)=int_1^X G_*(x)H(x)dx, G_*=(3/2)x^(-1/2).

Integrando cada escalón aritmético, con TODO contacto q<=X,

    I_*(X)=3(sqrtX−1)+(c−1)(1−X^(-3/2))+(3/2)J(X)
       −2sum_(q<=X)Lambda(q)/sqrtq
       +2X^(-3/2)sum_(q<=X)qLambda(q),                  (I)
    J(X)=int_1^X x^(-5/2)log((x+1)/(x−1))dx.

Cada contacto de extremo q=X cancela exactamente entre las dos sumas. No se omite un salto con valor favorable o adverso.

Para z=sqrtX>1, la integración por partes030 da la forma cerrada

    J(X)=(8/3)(1−1/z)−[2/(3z³)]log((X+1)/(X−1))
        +(2/3)log((z+1)/(2(z−1)))
        −(4/3)arctan((z−1)/(z+1)).                       (J)

En X0, z15/8 y el argumento arctan es7/23. En X4, z2 y el argumento es1/3. Las dos fórmulas contienen sólo constantes con intervalos racionales explícitos, no una cuadratura numérica.

## 3. Qué ocurre tras el contacto3

En ambos extremos sólo contribuyen q2 y q3 (q4 tiene coeficiente0 en X4). Sus valores reales son Lambda(2)=log2,Lambda(3)=log3. El certificado exacto prueba

    I_*(225/64)<−1/250,
    I_*(4)>1/50.                                        (WEIGHTED)

Se usan 140/99<sqrt2<99/70 y265/153<sqrt3<97/56, comprobadas elevando al cuadrado. Las cotas negativas se obtienen con los recíprocos menores; las positivas con los recíprocos mayores, conservando la dirección correcta de cada término −2Lambda(q)/sqrtq.

Como orientación, sin usarlos en la prueba, los valores son aproximadamente−.0047659 y+.0251073. WEIGHTED refuta exactamente la premisa «la primitiva ponderada I_* es no negativa para todo X». No refuta el signo de W ni autoriza a ignorar el intervalo de recuperación posterior.

## 4. Transferencia uniforme a G_N REAL, sin otro N certificado

Por030, para y real,

    |rho_N(y)−1|<=M2_N y²/2,
    |rho_N'(y)|<=M2_N |y|,
    M2_N=u²/(2N−3).

En1<=x<=4 se tiene logx<=log4<7/5. Luego

    |G_N(x)−G_*(x)|
      <=M2_N[(3/4)(logx)²+logx]<3M2_N.                  (G-ERROR)

También

    int_1^4 |H(x)|dx<10.                               (H-NORM)

Para probarlo se acota la longitud por3, la parte constante por(23/5)(3/4), el kernel logarítmico por2log2<7/5, el contacto2 por4log2 int_2^4 x^(-2)dx<7/10 y el contacto3 por6log3 int_3^4 x^(-2)dx<11/20. Su suma es9.1<10. El valor del contacto4 en el extremo no altera la integral.

Así para CUALQUIER X<=4,

    |int_1^X(G_N−G_*)H|<30u²/(2N−3).                    (ERROR)

A tasa FIJA u63/2, el mayorante es <1/200 para TODOS N>=2^22 y <1/1000 para TODOS N>=2^24. No hay un barrido o un certificado individual por N: se usa una función explícita decreciente de N.

Combinar ERROR y WEIGHTED da los dos primeros bounds REAL. Para N>=2^24, restarlos sobre la MISMA función gamma real prueba la recuperación

    int_X0^4 G_NH>3/200+3/1000=9/500.

En particular el prefijo real adverso no desaparece al incorporar el dato gamma: para todo N del rango declarado persiste un aporte negativo. El bloque extendido lo compensa cuantitativamente antes de llegar a4.

## 5. Relación con el factor real y obligación global

Escriba R_N=G_N/G_*=rho_N−(2/3)rho_N', con rho evaluada en logx. En intervalos finitos,

    int_1^X G_NH=R_N(X)I_*(X)−int_1^X I_*(x)dR_N(x).

En toda la semirrecta el término de borde se anula, por el decaimiento gamma y el crecimiento a lo sumo polinómico de I_*, y se obtiene W/norm²=−int I_*dR_N. Esta identidad no es una nueva desigualdad de signo. El constructor paralelo analiza la forma y la variación del factor real R_N en POWER_GAMMA_WEIGHT_031.md; no se supone que sea monótono desde1.

WEIGHTED demuestra por qué aun una propiedad favorable de R_N necesita comparar intervalos: I_* tiene una región adversa real. REAL suministra una compensación concreta, pero no dice que todos los bloques admitan el mismo patrón ni que sumar bloques positivos cierre la forma.

No se amplía aquí la lista de contactos. El próximo requisito es una desigualdad de emparejamiento que use el factor gamma y controle las contribuciones adversas de TODOS los contactos frente a las favorables, conservando el peso completo. Sólo el bloque hasta4 queda resuelto. El resto int_4^infty G_NH sigue abierto, y no puede reemplazarse automáticamente por una cola positiva de otra representación sin contabilidad de los cambios de truncamiento.

## 6. Evidencia

Verificador: tools/power_weighted_block_031_verify.py, Fraction e intervalos exactos; PASS. Comprueba las dos desigualdades de WEIGHTED, los coeficientes de G-ERROR/H-NORM y los umbrales analíticos. La uniformidad en TODOS N de REAL se prueba arriba. No se afirma W total negativo ni positivo, una nueva ventanaT ni cierre global. Papers intactos.
