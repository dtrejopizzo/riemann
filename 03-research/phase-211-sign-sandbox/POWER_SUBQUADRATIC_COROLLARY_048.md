# POWER_SUBQUADRATIC_COROLLARY_048 — Extracción de una región de signo de los bounds017

Estado: **PROVED como corolario de las desigualdades auditadas017; revisión independiente APROBADA en POWER_SUBQUADRATIC_AUDIT_048.md y derivación revisada por root.** No es una desigualdad aritmética nueva ni un cierre global. Papers intactos.

## 1. Consulta previa y diferencia exacta

Leídos las reglas del proyecto, STATEMENT_001, ROUTES-TRIED-INDEX/README, grid maestro y CROSSWORD-TO-D; revisados SCALAR_BRIDGE017, QUADRATIC017, QUADRATIC_EXPLICIT017, DESCENT016, TABLE_DESCENT018, RECURRENCE_BOUNDARY036 y los estados046/047. La búsqueda específica de `subquadr`, `sub.quadr`, `loglog`, `log log N` y `log\\log N` en el índice, grid, crucigrama y archivos POWER no halló una región de esta forma ya explicitada.

La herramienta es íntegramente QUADRATIC017: no se reintenta otra prueba de la estimación por banda, ni se da otro nombre a esa ruta. Se extrae una consecuencia cuantitativa permitiendo que su parámetro c dependa de N y tienda a cero. La razón precisa que permite esta extracción es que STRIP, PRIME, ARCH y POL son desigualdades válidas para CADA c>0, N>=2 y k>=max(cN²,4N), con constantes explícitas; no se usa el enunciado eventual con N0(c) sin controlar su dependencia.

El resultado017 explicitado tenía c fijo; QUADRATIC_EXPLICIT017 cubre k>=10000N² desde N=2. Aquí la frontera es 2N²/log log N. Para cada c fijo positivo, esta frontera queda por debajo de cN² para N suficientemente grande. Es nueva cobertura explicitada de la tabla, obtenida de bounds existentes. No se declara un método nuevo, ni se afirma controlar el interior completo.

## 2. Candidato y resultado

Fije u=63/2. Para enteros N>=exp(1000000) y

    k >= 2N²/log log N,

sea f_(N,k) la función causal de transformada s^k/(s+u)^(N+k). Entonces, para la forma COMPLETA real de017,

    W[f_(N,k)] > (2/5) log N · ||f_(N,k)||².             (SUBQUADRATIC)

El enunciado cubre TODOS los órdenes de esa región no acotada y TODOS los k por encima de su frontera. No se ha evaluado numéricamente un orden N ni un contacto. El umbral es deliberadamente conservador.

## 3. Cuatro bounds exactos que se importan de017

Para cualquier c>0 bajo N>=2 y k>=max(cN²,4N), QUADRATIC017 prueba

    C(c)=1+2[exp(4/(25c))+exp(1/c)],
    |Comb[f]|/||f||² < 14C(c),
    ARCH[f]/||f||² >= (1/2)log N + log[u sqrt(c)/(2pi)] - 5,
    |Polar[f]|/||f||² < 400^(-k).

El bound de Comb suma el peine INFINITO completo usando el desplazamiento de la DENSIDAD racional conjunta; no separa dos normas temporales. El polar es el real completo y se conserva aun cuando su signo sea desfavorable. Las cuatro desigualdades son finitas y uniformes en la región indicada. No se necesita la aproximación gaussiana de017 ni pasar un límite por una suma aritmética.

## 4. Elección variable y comprobación de todas las hipótesis

Escriba L=log N>=1000000 y elija

    c_N = 2/log L > 0.

La condición del teorema es exactamente k>=c_N N². También c_N N²>=4N: basta N>=2log L, y

    N=exp L >= L²/2 >= 2L >= 2log L

para L>=1000000. La primera desigualdad usa sólo un término positivo de la serie exponencial. Se cumplen por tanto TODAS las hipótesis de los bounds017 con esta elección c_N, sin invocar ningún N0 dependiente de c.

Ahora

    exp(1/c_N)=sqrt L,
    exp(4/(25c_N))=L^(2/25)<=sqrt L,
    C(c_N)<=1+4sqrt L.

Además u sqrt(2)/(2pi)>1, usando u=63/2 y pi<4. Así

    ARCH[f]/||f||²
      > (1/2)L - (1/2)log log L - 5.

Para L>=1000000 se tiene log log L<=log L<=sqrt L. La segunda desigualdad vale desde L=16: en16 usa log16<4, y la derivada de sqrt L-log L es no negativa para L>=4. La primera sigue de log L<=L y monotonía del logaritmo.

## 5. Balance completo y margen

El bound polar es menor que1. Las estimaciones anteriores dan

    W[f]/||f||²
      > (1/2)L - (113/2)sqrt L - 20.

Ponga y=sqrt L>=1000. Entonces

    (1/10)y²-(113/2)y-20
      >=(87/2)y-20 > 0,

pues y²/10>=100y. Por tanto el último lower es estrictamente mayor que (2/5)L. Esto prueba SUBQUADRATIC con todas las constantes simbólicas y sin una campaña numérica.

## 6. Alcance frente036 y046

Esta extracción no prueba la hipótesis uniforme -o(1) sobre TODA la banda pendiente de046. Sigue quedando k<2N²/log log N y N no cubiertos por otros resultados.

Tampoco se anula RECURRENCE_BOUNDARY036. Su conclusión se refiere a la energía del cono fijo k'>=10000N'²; ampliar aquí la región de signo no convierte automáticamente el complemento de una frontera diagonal en energía evanescente. No se ha probado una estimación de ese nuevo complemento, ni se lo elimina por una cuenta de masa. La tabla completa y el signo global continúan **OPEN**; no hay nueva ventana T certificada del Paper47.
