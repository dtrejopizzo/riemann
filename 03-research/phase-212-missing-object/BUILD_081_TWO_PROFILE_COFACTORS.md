# Construcción 081 — Cancelación de dos perfiles por cofactores

Estado: diseño explícito, pendiente de revisión; signo global OPEN.

Sean g0=Q(1_I M), g1=Q(1_I M′), perfiles primitivos explícitos. Sean l0=0,l1=log2,l2=log3 y U_l los desplazamientos causales comprimidos. Definir

    D F(t)=det [[g0(t),g1(t),F(t)],
               [U_l1 g0(t),U_l1 g1(t),U_l1 F(t)],
               [U_l2 g0(t),U_l2 g1(t),U_l2 F(t)]].

El determinante es lineal en F. Expandiendo la última columna,

    D F=c0 F+c1 U_l1 F+c2 U_l2 F,
    c0=(U_l1 g0)(U_l2 g1)−(U_l2 g0)(U_l1 g1),
    c1=(U_l2 g0)g1−g0(U_l2 g1),
    c2=g0(U_l1 g1)−(U_l1 g0)g1.

Se tiene Dg0=Dg1=0 exactamente, incluso en nodos y degeneraciones del determinante. No se divide por ningún menor.

Definir C=Σ_{j=0}²||c_j||∞, α=1/[2(1+C)], W=α Q D Q, V=JW. Entonces ||W||<1/2 y Wg0=Wg1=0. Los perfiles y coeficientes son BV compactos; para F del núcleo suave, WF pertenece al dominio logarítmico de J.

Para Z_jF=Q(c_j U_lj F), el cuadrado y el residuo son

    ||VF||²=α²Σ_{i,j=0}² b(Z_iF,Z_jF),
    ρ(F)=Arch(F)−2Re<F,LF>−α²Σ_{i,j=0}²b(Z_iF,Z_jF).

No se descartan cruces. La identidad a_T=||V||²+ρ es exacta en el núcleo; no se afirma ρ≥0.

## Arimética y riesgo de degeneración

Los retardos 2 y 3 participan juntos, pero los valores de Λ no aparecen en D. Multiplicar cada fila por un peso aritmético sólo multiplica D por el producto de los pesos. Esto no es un acoplamiento que explique el signo ni separa el reescalado de Λ. Es una limitación explícita de este diseño.

Si un retardo deja toda su fila fuera de I, la fila es cero y el determinante se anula. En particular para 2T≤log3 el operador D es cero. Una extracción cero no se interpreta como positividad del residuo.

El diseño se ensaya para comprobar si anular dos perfiles resuelve el exceso de extracción visto en BUILD080. La anulación de una familia finita no constituye por sí sola una prueba global.

## Revisión y ensayo

Las fórmulas, signos de cofactores, anulación y dominio fueron revisados independientemente. Se precisó supp(DF)⊂(-T+log3,T). La proyección final Q puede extender el soporte, pero no cambia la anulación de los perfiles.

NUMÉRICO: el test par guardado T=0.8 produce ||WF||²=9.4765538142759e−5 (Gauss64), 9.4765538142757e−5 (Gauss96). La suma de supremos de cofactores fue muestreada: C≈1698.39301. No se certificaron estos supremos ni el valor guardado de la forma. Como este último es ≈5.2943e−12, el primer canal sigue siendo excesivo. La cancelación de dos perfiles no mejora este diagnóstico frente al corrector de un perfil.

No se propone resolverlo aumentando mecánicamente el número de perfiles. La lección del ensayo es que anular perfiles explícitos por separado no reproduce necesariamente las cancelaciones del vector casi nulo. Una suma coherente sobre pares de retardos conservaría cruces entre pares, a diferencia de sumar sus normas, pero no se ha escrito aún una elección de coeficientes que firme el residuo.
