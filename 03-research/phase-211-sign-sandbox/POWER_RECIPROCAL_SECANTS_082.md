# POWER_RECIPROCAL_SECANTS_082 — Dos concavidades recíprocas para orden tres

Estado: **PROVED como criterio algebraico, auditoría final de mapa aprobada.** Véase `POWER_RECIPROCAL_SECANTS_AUDIT_082.md`. Identidades y signos comprobados independientemente por root e insight048. No se afirma su descarga para todos los restos G_p, preservación por Schur, ni positividad de todos los órdenes. Papers intactos.

## 1. Consulta y diferencia precisa

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D; cotejados POWER_SCHUR_003, POWER_TWO_COPY_SCOPE_074, POWER_THREE_SECANTS_079 y POWER_SCHUR_BASE_OBSTRUCTION_081.003/074 refutan inferencias desde pares o desde hipótesis genéricas de concavidad.079 prueba orden tres bajo BASE073 más una concavidad adicional;081 prueba que el resto REAL G_p no hereda esa BASE, porque su derivada puede ser negativa.

El objeto nuevo es un criterio simétrico bajo F↔1/F que NO exige F creciente ni cóncava. Dentro de la clase de pares estrictamente positivos, dos concavidades en x=u² son necesarias y suficientes para todos los triples. El criterio permite las derivadas negativas de081. No se presenta como una solución de la obligación de probar esas concavidades para los restos reales.

## 2. Definiciones y enunciado

Sea I un intervalo de números positivos, y F:I→(0,infinito) continua. Definir

    K_F(u,v)=[F(u)+F(v)]/(u+v),
    x=u², R(x)=u/F(u), S(x)=uF(u)=x/R(x).

Para nodos distintos x_i, la notación R[x1,x2] y R[x1,x2,x3] indica diferencias divididas usuales, sin un factorial adicional. Suponer que TODOS los bloques de dos nodos distintos de K_F son definidos positivos. Entonces son equivalentes:

1. Todos los bloques de tres nodos de K_F son semidefinidos positivos.
2. R y S son cóncavas en el intervalo de cuadrados I².

Para un triple distinto, la definición positiva equivale a que AMBAS diferencias divididas de orden dos sean estrictamente negativas. La concavidad estricta de ambas funciones es suficiente para todos los triples distintos definidos positivos; no se sustituye por una afirmación sobre sus derivadas segundas estrictas si sólo hay regularidad continua.

## 3. Identidad normalizada de orden dos

Para 0<u<v en I, poner x1=u²,x2=v² y Ri=R(xi). Una expansión directa da

    det K_F(u,v)
       =(u−v)²/(R1R2) · R[x1,x2] S[x1,x2].          (DET2)

En efecto, al hacer la congruencia diag(R1,R2), el numerador de su determinante es

    (R2−R1)(v²R1−u²R2)/(u+v)².

Los dos factores R2−R1 y v²R1−u²R2 no pueden ser ambos negativos: eso exigiría R2<R1 y R2/R1>v²/u²>1. Por tanto la hipótesis de pares estrictamente positivos equivale a

    R[x1,x2]>0, S[x1,x2]>0, TODOS x1<x2.             (PAIR)

En particular R y S son estrictamente crecientes. No se deduce que F sea creciente.

## 4. Secantes de un triple

Fijar 0<u<v<w en I y escribir Hi=R(ui²), (u1,u2,u3)=(u,v,w). Definir

    beta=(H2−H1)/(v²−u²)>0,
    delta_R=beta−(H3−H2)/(w²−v²),
    alpha=H1−beta u².

PAIR para S da

    alpha=[v²H1−u²H2]/(v²−u²)>0.

No se necesita la desigualdad alpha>beta uv de079: aquella expresaba que F era creciente. Los datos se parametrizan exactamente como

    H1=alpha+beta u²,
    H2=alpha+beta v²,
    H3=alpha+beta w²−delta_R(w²−v²).

Definir también

    delta_S=(S(v²)−S(u²))/(v²−u²)
             −(S(w²)−S(v²))/(w²−v²).

S(x)=x/R(x) y denominadores Hi>0 dan la identidad

    delta_S={alpha beta(w²−u²)
                −delta_R[alpha w²+beta u²v²]}/(H1H2H3). (RECIPROCAL)

Esta identidad se verifica multiplicando por H1H2H3 y sustituyendo los tres valores Hi; sólo quedan productos polinómicos.

En particular, si delta_R<=0, RECIPROCAL da delta_S>0. Ambos defectos nunca son no positivos a la vez. Esto es el punto de signo adicional que no contiene por sí sola una factorización del determinante.

## 5. Identidad normalizada de orden tres

Poner D=diag(H1,H2,H3) y T=DK_FD. Entonces

    T_ij=[ui Hj+uj Hi]/(ui+uj), T_ii=Hi.

La expansión polinómica de079, ahora sin su hipótesis BASE, da

    det T=delta_R (u−v)²(v−w)²/(u+w)²
       ·{alpha beta(w²−u²)
                  −delta_R[alpha w²+beta u²v²]}.

Usando RECIPROCAL y det T=(H1H2H3)² det K_F,

    det K_F=delta_R delta_S/(H1H2H3)
                        ·(u−v)²(v−w)²/(u+w)².       (SECANTS)

Como

    delta_R=−(w²−u²)R[u²,v²,w²],
    delta_S=−(w²−u²)S[u²,v²,w²],

se obtiene la forma simétrica

    det K_F(u,v,w)
       =Vandermonde(u,v,w)²/(H1H2H3)
          ·R[u²,v²,w²] S[u²,v²,w²],                (DET3)

donde Vandermonde(u,v,w)=(v−u)(w−u)(w−v). No queda un factor (u+w) en DET3: se cancela exactamente con (w²−u²)².

## 6. Prueba del criterio y bordes

Por PAIR todos los menores principales de orden uno y dos son positivos. Por el complemento de Schur de una diagonal, el bloque de orden tres es PSD si y sólo si su determinante es no negativo, y es PD si y sólo si su determinante es positivo.

SECANTS exige delta_R delta_S>=0. RECIPROCAL excluye que ambos sean negativos y también excluye que uno sea negativo y el otro cero. En consecuencia

    det K_F>=0  iff delta_R>=0 y delta_S>=0;
    det K_F>0   iff delta_R>0 y delta_S>0.

En términos de diferencias divididas, son exactamente las dos concavidades, o las dos desigualdades estrictas para ese triple. Imponerlas para todos los triples de un intervalo equivale a la concavidad de R y S; la continuidad permite la formulación usual sin regularidad diferencial adicional.

Si delta_R=0, RECIPROCAL da delta_S>0 y el determinante es cero. La congruencia se reduce a T=alpha·11^t+beta·(u,v,w)^t(u,v,w), de rango dos. Si delta_S=0, el caso es su imagen por F↔1/F y también tiene rango dos. Bajo PAIR estricta no ocurren ambos defectos cero simultáneamente. No se extiende el argumento alpha beta>0 a clases de pares sólo PSD sin separar sus degeneraciones.

Nodos repetidos producen columnas repetidas y matrices PSD cuando el bloque de nodos distintos lo sea. Se combinan los coeficientes: una función representada nula puede corresponder a un vector de coeficientes no nulo.

## 7. Simetría, relación con079 y alcance real

La identidad exacta

    K_(1/F)(u,v)=K_F(u,v)/[F(u)F(v)]

es una congruencia diagonal positiva. La inversión intercambia R y S, de modo que PAIR y el criterio de dos concavidades son invariantes. El criterio diferencial de pares |uF'/F|<=1 también admite derivadas negativas;081 no lo refuta.

Para F=M real, R=u/M=(1+g(x))/a. Por tanto R''=g''/a. Además

    S''(x)=[u²M''(u)+uM'(u)−M(u)]/(4u³)<0

por073. Así DET3 recupera079: dentro de BASE073 sólo falta la concavidad de g. Se conserva el compacto real pendiente de080 y no se afirma aquí su resultado.

Para F=G_p, el criterio se aplicaría SI se prueban sus pares estrictamente positivos y las dos nuevas concavidades R_p(x)=sqrt(x)/G_p(sqrt x), S_p(x)=sqrt(x)G_p(sqrt x).077 sólo prueba valores positivos;078 ofrece otro criterio suficiente condicional para pares.081 descarta exigir monotonía de G_p, pero no las dos concavidades actuales. Ni su descarga ni su preservación al repetir Schur se han demostrado aquí.

DET2 y DET3 sugieren preguntar por identidades de orden mayor, pero no se declara patrón general, positividad de cuatro generadores o cierre global. El resultado de082 es el criterio exacto de orden tres para una clase que admite funciones F no monótonas.
