# POWER_PARTICULAR_TAIL_095 — Cola analítica del Wronskiano particular

Estado: **PROVED por las estimaciones analíticas siguientes; auditoría independiente aprobada.** Véase `POWER_PARTICULAR_TAIL_AUDIT_095.md`. No nueva evaluación theta, certificado compacto, parámetro explorado ni malla. Papers intactos. Se prueba el signo requerido del Wronskiano PARTICULAR para todo t>=64, no para todo t>0 ni para una nueva ventana T del Paper47.

## 1. Datos, consulta y diferencia frente088/092

Consultados las reglas del proyecto, README ROUTES-TRIED-INDEX, R162_2300_MASTER_GRID y CROSSWORD-TO-D, y077/078/087–094.088 controla el Wronskiano original de cuatro densidades.092 muestra que la eliminación universal mediante Delta no es globalmente invertible.093 verifica el signo de la solución particular en una vecindad no cuantificada del origen. Aquí se utiliza la selección integral de ESA solución particular para probar una cola completa; no se invierte Delta y no se diferencia un equivalente real sin resto.

Phi es la densidad theta REAL, par, positiva y de supercolas, y

    w=tPhi, v=−Phi', a=M'(0)>1/25, c=1/a<25,
    zeta=v−cw,
    K(t)=integral_t^infinito(s−t)zeta(s)ds.

La desigualdad a>1/25 es el ancla real078, no una aproximación de los momentos. K(0)=0 por el momento exacto integral_0^infinito t zeta(t)dt=0. Su extensión impar es suave y K''=zeta. El objeto es

    Wpart(t)=W_t(w,v,w'',K).

## 2. Control complejo completo del logaritmo theta

En el strip mayor Re z>=2, |Im z|<=1/8, escribir y=pi exp(2z),Y=|y|. Las cotas elementales pi>3,exp4>54 y cos(1/4)>31/32 dan

    Y>162, Re y>(31/32)Y>156.

La función se factoriza exactamente

    Phi(z)=pi exp(5z/2)(2y−3)exp(−y)[1+Rtheta(z)],
    Rtheta=sum_(m>=2)m²(2m²y−3)/(2y−3) exp[−(m²−1)y].

Como Y>162, el factor racional tiene módulo menor que2m^4. Los términos m^4 exp[−156(m²−1)] tienen razones sucesivas menores que1/2: desde m=2, (1+1/m)^4<6 y el incremento del exponente es por lo menos780. Por tanto TODA la cola satisface

    |Rtheta|<64 exp(−468)<2^(−462)<2^(−460).

Esto incluye todos los modos m>=2; no se los descarta. La serie log(1+Rtheta) es holomorfa y de módulo menor que2^(−459). En cada disco de radio1/32 alrededor de Re z>=3,|Im z|<=1/16, se permanece en el strip mayor. Cauchy da

    |[log(1+Rtheta)]'|<32*2^(−459)<1,
    |[log(1+Rtheta)]''|<2*32²*2^(−459)<1.

Ni 2y−3 ni1+Rtheta se anulan. Definir el logaritmo derivado p(z)=−Phi'(z)/Phi(z), sin necesitar una elección global del logaritmo de Phi. Para el primer modo,

    p_first=2y−9/2−6/(2y−3),
    p_first'=4y+24y/(2y−3)².

En el strip interior Re z>=3,|Im z|<=1/16 se concluye

    |p−2y|<6, |p'|<=5Y, Re p>=Y, |p|>=Y.        (COMPLEX)

La última comparación usa Re(2y)>=2Y cos(1/8), cos(1/8)>127/128 y Y>162. Así todos los cocientes utilizados a continuación son holomorfos en ese strip.

## 3. Representación horizontal e integración por partes con resto

Para z en el strip interior,

    K(z)=integral_0^infinito [1−cs(z+s)]Phi(z+s)ds. (HORIZONTAL)

En z real resulta de integrar por partes el término−Phi' en la definición de K. La identidad se extiende al strip por holomorfía: las integrales horizontales convergen uniformemente en compactos por Re y>0 y las supercolas theta.

Fijando z y s>=0, COMPLEX implica

    |Phi(z+s)/Phi(z)|
       <=exp[−integral_0^s Y exp(2r)dr]
       <=exp(−Ys).

Sea H0(z)=integral_0^infinito Phi(z+s)ds. La integración por partes exacta, con borde nulo en infinito, da

    H0(z)/Phi(z)=1/p(z)
      −integral_0^infinito [Phi(z+s)/Phi(z)]p'(z+s)/p(z+s)² ds.

Aquí |p'(z+s)/p(z+s)²|<=5/[Y exp(2s)]<=5/Y. Por tanto

    |H0/Phi−1/p|<=5/Y².

El segundo término de HORIZONTAL se controla conservando su estructura completa:

    |K/Phi−H0/Phi|
      <=25 integral_0^infinito s(|z|+s)exp(−Ys)ds
      =25|z|/Y²+50/Y³.

Como Y>50,

    |K/Phi−1/p|< (6+25|z|)/Y².                 (IBP-REM)

Es un bound de funciones holomorfas en un strip, no sólo un O real. Permite controlar derivadas por Cauchy sin diferenciar informalmente un resto asintótico.

## 4. Tres errores de columnas y sus derivadas hasta orden3

Fijar t real>=4 y y0=pi exp(2t). En el disco |z−t|<=1/32 se tiene

    (15/16)y0<Y<(16/15)y0,
    |z|<t+1.

Se usan las cotas exp(−1/16)>15/16 y exp(1/16)<16/15. Al dividir todas las columnas por Phi, la regla de factor común del Wronskiano da

    Wpart/Phi(t)^4=W_t[t,p,t(p²−p')−2p,K/Phi].

Comparar con el modelo de funciones analíticas

    [t,q,tq²,1/q], q(z)=2pi exp(2z).

La primera columna es exacta. Para la segunda, COMPLEX da |p−q|<6. Para la tercera,

    |t(p²−p')−2p−tq²|
       <=[35|z|+6]Y
       <200(1+t)y0.

En esta estimación t dentro de la función analítica significa z; el t real sólo nombra el centro. Se usaron |p+q|<5Y,|p'|<=5Y,|p|<3Y. Para la cuarta, IBP-REM y

    |1/p−1/q|<=3/Y²

dan

    |K/Phi−1/q|<200(1+t)y0^(−2).

Cauchy en el disco fijo de radio1/32 controla las derivadas0,...,3 de TODOS estos errores. Con

    H=200*3!*32³=39321600,

los módulos de las entradas de las columnas de error, en cualquier fila de derivadas0,...,3 del Wronskiano, son respectivamente menores que

    H, H(1+t)y0, H(1+t)y0^(−2).                (COL-ERR)

Los bordes de los discos son admisibles porque se trabaja en un entorno del strip cerrado; alternativamente se obtiene el mismo bound por límite de radios menores. No se deriva ningún O sin control.

## 5. Determinante modelo y resto finito explícito

En el centro real, las cuatro columnas modelo y sus derivadas hasta orden3 tienen entradas acotadas en módulo por

    [t,16y0,512t y0²,4/y0].

En efecto q'=2q y las derivadas de tq² son4y0²[4^r t+r4^(r−1)],r<=3, acotadas por512t y0² para t>=4. El cálculo polinómico exacto del determinante modelo es

    W[t,q,tq²,1/q]
      =−128q²(6t²+4t−1)
      <=−3072t²y0².                            (MODEL)

No se usan valores theta para esta identidad. Expandir multilinealmente en los tres errores COL-ERR produce siete términos. Cada determinante se acota por24veces el producto de los máximos de sus columnas. Usando1+t<=2t,t>=4,y0>=1, los tres términos con un error suman como máximo445440H t³y0; los tres con dos errores,26304H²t³y0; y el de tres errores,96H³t³y0. En consecuencia

    |Wpart/Phi^4−Wmodelo|<C t³y0,
    C=10^6(1+H)³,
    445440H+26304H²+96H³<C<2^98.                (DET-REM)

Las últimas desigualdades son aritmética entera: H+1<2^26 y10^6<2^20. Se conserva el efecto simultáneo de los errores; no se extrapola el signo de columnas separadas.

## 6. Umbral analítico y resultado

La función y0/t=pi exp(2t)/t es estrictamente creciente para t>1/2. En t=64, usando exp1>2,

    y0>2^128,
    C*64<2^104,
    y0>C*64.

Así y0>Ct para TODO t>=64. MODEL y DET-REM dan entonces

    Wpart(t)/Phi(t)^4<−3071t²y0²<0,
    W_t(tPhi,−Phi',(tPhi)'',K)<0 para TODO t>=64. (TAIL-PARTICULAR)

El número64 se obtiene sólo de los mayorantes anteriores y potencias enteras, sin evaluar el determinante en puntos ni ajustar un umbral a signos observados.

## 7. Alcance y obligación restante

093 verifica este mismo signo cerca0; la presente prueba verifica toda la cola t>=64. Permanece abierto el intervalo intermedio. No se infiere que los sistemas de cuatro densidades preserven el signo por mera inversión de D², ni que la carta Delta de092 sea regular; esta prueba evita esa carta y usa directamente la solución particular seleccionada por sus bordes.

El parámetro t aquí es la variable temporal interna de las densidades theta, **no una nueva ventana T**. No se afirma positividad para cinco generadores ni todos los órdenes, ni ampliación de la cobertura de W. Una prueba global del signo particular seguiría siendo necesaria para la aplicación correspondiente. No se crea un verificador numérico: sólo se usan las identidades y desigualdades analíticas explícitas anteriores.
