# POWER_STATE_077 — Signo real uniforme del resto Schur regularizado

**Actualización080:** el compacto admisible de g quedó certificado en `POWER_THETA_G_COMPACT_080.md`, auditado en `POWER_THETA_G_COMPACT_AUDIT_080.md` y resumido en `POWER_STATE_080.md`: TODOS los triples de potencias ai>1 tienen signo positivo completo. Las menciones siguientes de compacto pendiente describen el estado histórico de esta ronda; h y los órdenes superiores no quedan descargados por080.

Estado: **PROVED/APROBADO** por prueba analítica y certificado compacto completo del constructor, con auditoría de código. Reproducción independiente compacta root36038 terminada exit0/FULL PASS; hash coincidente. Papers intactos; signo global OPEN.

## Resultado

Fuentes: POWER_THETA_REMAINDER_077.md, POWER_THETA_RATIO_OUTER_077.md y POWER_THETA_RATIO_COMPACT_077.md. Auditoría integrada: POWER_THETA_REMAINDER_AUDIT_077.md.

ConservarPhi,Z,M,Phi_u,H_u de073/075. Para TODO u>0, c=M(u),a=M′(0),beta=u²a/(ua−c), definir

    J(x)=integral_|x|∞ yPhi(y)dy,
    F_u(x)=J(x)−betaPhi_u(x).

Entonces F_u tiene exactamente UN cero positivo SIMPLE, es negativo antes y positivo después. Su masa total es0. Para TODOS u,z>0,

    T_u(z)=Z(z)−[Z(0)/H_u(0)+z²/c]H_u(z)>0,
    G_u(z)=c²T_u(z)/(uzH_u(z))>0.

G_u es el resto exacto F1−R_u/z de075, conR_u=uc²/(ua−c)>0. La afirmación es uniforme en ambos parámetros positivos; no es una selección finita de pivotes o nodos.

## Nueva desigualdad local y prueba del signo

Para p=V′,q=V″,r=V‴,V=−logPhi, se probaron en TODO x>0

    C=p³+xp²q−pq−xpr+xq²>0,
    N=(xq−p)C′−xrC>0.

Así L=(xq−p)/C decrece estrictamente hacia0. La integración por partes y el borde realwPhi->0 expresanR(x)^−1 como promedio de cola deL contra−(wPhi)′>0, w=1+xq/p. Esto prueba queR=(p+xq)/(x−pJ/Phi) crece estrictamente hacia infinito, descargando la hipótesis de la prueba condicional.

El forzante deF tiene dos momentos nulos y patrón+−+. Interpolación convexa entre sus dos cruces daF(0)<0 por el Green con signo negativo; la representación anticausal da cola positiva. El conteo de Rolle con multiplicidades limita a cuatro ceros globales y fuerza el único cruce positivo simple. Masa cero y el crecimiento de cosh pruebanT yG positivos.

## Evidencia reproducible

Exterior x>=1: prueba analítica con margen de primer modo y TODA la cola theta. VerificadorFraction power_theta_ratio_outer_077_verify.py, tresPASS reproducidos independientemente por root. Es un certificado de todo un cuadrante, no una malla de puntos.

Compacto: origen0..1/16 medianteV6<0 yREG en1024 paneles; resto1/16..1 con modelosTaylor2 deC,N en8192 paneles fijos. Constructor1589 terminóexit0/PASS. Script power_theta_local_077_verify.py auditado completo; SHA256

    896902cf8ac1f504eb1357b6edc3048a9316094afd9b8ac5597aaff4a81a70ee.

Root36038 terminó su reproducción independiente exit0/FULL PASS en el origen y los8192 paneles restantes, con hash coincidente. La primera evaluación intervalar directa insuficiente falló por dependencia; la versiónTaylor conserva dominios/mallas y añade las derivadas y restos necesarios, sin cambiar la hipótesis para forzar el signo.

## Diferencia y obligación pendiente

075 sólo construíaPhi_u positiva;076 formuló el defecto y dejó su cruce abierto.077 prueba una propiedad diferencial específica de la MISMA Phi que controla el resto, no una iteración genérica de073. El auxiliar074 no satisface por supuesto estas nuevas desigualdades locales y no contradice el resultado.

G_u(z)>0 sobre la recta NO implica que[G_u(z_i)+G_u(z_j)]/(z_i+z_j) seaPSD. No se obtuvo todavía positividad de tres generadores, de todos los órdenes, una tabla completa o una ventana temporal nueva. Los cruces del kernel del resto siguen siendo la obligación concreta siguiente; signo global OPEN.

## Corolario anclado auxiliar

ConN(u)=M(u)/u yB(u)=[a/N(u)−1]/u², se tieneB>0, B′<0 y2B+uB′>0. La última desigualdad viene deN′<0; B′<0 se deduce del valor removible

    G_u(u)=−aB′(u)/[B(u)(2B(u)+uB′(u))]>0.

Por elloF=uB tiene|uF′/F|<1 y todos sus pares de kernel son definidos positivos. El complemento deSchur exacto

    K_M(u,v)−N(u)N(v)/a=[uN(u)vN(v)/a]K_F(u,v)

prueba la matriz anclada{0,u,v}, para u,v>0 distintos. El nodo0 es sólo la extensión auxiliar: corresponde aa_orig=1/2, fuera de los datos de potencias admisiblesa_orig>1. No hay tres pruebasW admisibles en ese corolario. Tampoco se demuestra positividad del kernelG ni de tres nodos positivos arbitrarios.

## Apéndice078 — Dos curvaturas suficientes y tramos exteriores analíticos

Derivación de casos e insight048, **APROBADA** por root y revisión independiente de mapa en POWER_THETA_CURVATURE_AUDIT_078.md. No se crea otra fuente de reformulaciones. Las estimaciones exteriores siguientes no son una nueva región de signo W; el compacto inicial continúa pendiente.

Poner x=u² y, usando sólo en este apéndice primas para derivadas respecto de x,

    b(x)=B(sqrt x), h(x)=1/b(x), g(x)=x b(x).

Una condición suficiente para TODOS los pares del kernel del resto G_p, en cualquier pivote positivo p, es la doble concavidad

    h''(x)<=0, g''(x)<=0, TODOS x>0.                    (CURVATURE-OPEN)

Esto es más que los valores G_p(z)>0 ya probados077. En efecto, con P=p², definir

    C_P(x)=[b(P)-b(x)]/[x b(x)-P b(P)].

077 prueba b decreciente y xb creciente, por lo que C_P>0 y su singularidad en x=P es removible. Álgebra exacta da

    G_p(z)=[a/B(p)]z C_P(z²),
    C_P'(x)=-b(P)b(x)²
       ·[h(x)-h(P)-(x-P)h'(x)]/[x b(x)-P b(P)]²,
    [xC_P(x)]'=b(P)
       ·[g(x)-g(P)-(x-P)g'(x)]/[x b(x)-P b(P)]².

Las desigualdades de rectas tangentes de CURVATURE-OPEN implicarían C_P'<=0 y(xC_P)'>=0, incluidos los valores removibles por continuidad. Luego|zG_p'/G_p|<=1, exactamente la condición mixta de CONE001 para todos los pares positivos del kernel G_p. Para pasar de ahí a un paso Schur se conserva además el residuo positivo R_p/z; su kernel es R_p/(zw), de rango uno positivo. No se afirma que las dos concavidades se preserven automáticamente al iterar.

### Identificación de la obligación ya conocida y de la segunda curvatura

Con v=a u/M(u), r=uM'(u)/M(u), t=-u²M''(u)/M(u), los resultados073/077 dan v>1,0<r<1,t>0. Las derivadas exactas son

    g''(x)=v[2r²-r+t-1]/(4u^4),
    h''(x)=v[(r-1)(2r+v-3)-(v-1)t]
                         /[4u²(v-1)^3].

Por tanto g''<=0 es PRECISAMENTE la obligación de jet ya registrada en STATE074,

    t<=(1-r)(1+2r),

y no se presenta como una desigualdad recién descubierta. La segunda concavidad exige

    t>=(1-r)(3-v-2r)/(v-1).

Esta última es automática y estricta si v+2r>=3, por ejemplo si v>=3. No hay prueba aquí de esa comparación en todo el compacto inicial.

### Primera curvatura: g''<0 para todo u>=63/2

Escribir A=u+1/2>=32, c=M(u), d=M'(u), e=M''(u) y

    P_j(A)=sum_(n>=2)Lambda(n)(log n)^j n^(-A).

Las series absolutas reales de CONE001 dan

    c=1/A+1/(A-1)-logpi/2+psi(A/2)/2-P_0,
    d=-1/A²-1/(A-1)²+psi_1(A/2)/4+P_1,
    e=2/A³+2/(A-1)³+psi_2(A/2)/8-P_2.

Comparar con integrales las series de poligamma prueba psi_1(y)>=1/y, psi_1(y)<=1/y+1/y² y psi_2(y)>=-1/y²-2/y³. Conservar sus cancelaciones en d+ue da

    d+ue>=-3/(4A²)+A/(A-1)³+P_1-uP_2
          >1/(4A²)-uP_2.

Lambda(n)(log n)^j<=(log n)^(j+1)<=n^(j+1) permite el majorante completo

    P_j(A)<=2^(j+1-A)[1+2/(A-j-2)], j=0,1,2.

Las cotas de P_0, AP_1 y A³P_2 decrecen desde A=32: la derivada logarítmica de la potencia A^m por2^(-A) es a lo sumo3/A-log2<0, y la del corchete es negativa. En32,

    P_0<=2^(-31)·16/15<1/100,
    AP_1<=32·2^(-30)·31/29<1/100,
    A³P_2<=32³·2^(-29)·15/14=15/229376<1/4.

Así d+ue>0. La cota superior de psi_1 también da d<1/(2A)+P_1 y por ello ud<51/100. De psi(y)>=log y-1/y,

    c>=log[A/(2pi)]/2+1/(A-1)-P_0
      >log5/2-1/100>3/4.

Aquí A/(2pi)>=56/11>5 por pi<22/7, y log5>124/81>38/25 por dos términos positivos de atanh con argumento2/3. Se obtiene

    Delta=c²+ucd+u²ce-2u²d²
          =c²+cu(d+ue)-2(ud)²
          >9/16-2(51/100)²=423/10000>0.

Finalmente la derivada exacta es

    g''(x)=-a Delta/(4u³c³)<0, TODOS u>=63/2.

No se separa el signo de componentes para concluir W: sólo se prueba esta curvatura auxiliar concreta. No se certificó una matriz ni se eligieron nuevos órdenes gamma.

### Segunda curvatura: h''<0 para todo u>=128

Primero se obtiene el bound del dato REAL a=M'(0)>1/25, sin integrar momentos theta. CONE001 fija M(15/2)=L(8). Las cotas auditadas gamma<3/5, logpi<23/20 y psi(4)=11/6-gamma dan

    L(8)>13/42-P_0(8).

Fuente explícita de esas constantes: POWER_FOUR_GLOBAL_009§4 y su verificación racional. Gamma<H32-log32<3/5 usa log2>693/1000, obtenido de tres términos positivos de atanh con argumento1/3. La cota logpi<23/20 usa pi<22/7 y la suma positiva sum_(k=0)^6(23/20)^k/k!>22/7. Son desigualdades racionales ya auditadas, no nuevas evaluaciones de parámetros.

Para n>=1, log n<=sqrt n: el máximo de(log x)/sqrt x es2/exp1<1. Así Lambda(n)<=sqrt n y la comparación suma-integral, conservando todos los términos, prueba

    P_0(8)<=sum_(n>=2)n^(-15/2)
       <=2^(-15/2)(1+4/13)<85/11648<1/105.

Se usó1/sqrt2<5/7. Por tanto L(8)>3/10. La concavidad estricta073 y M(0)=0 implican

    a>M(15/2)/(15/2)>1/25.

Para u>=128, la fórmula real de M, psi(y)<=log y, P_0>=0 y pi>3 dan

    M(u)<log(u/5)/2+2/(u-1/2).

En efecto(u+1/2)/(2pi)<u/5 para u>5/2. En u=128,

    (3/2)log(128/5)+6/(128-1/2)
       <99/20+4/85<128/25,

porque128/5<27 y log3<11/10. La diferencia

    u/25-(3/2)log(u/5)-6/(u-1/2)

es estrictamente creciente para u>=128: su derivada es mayor que1/25-3/256>0. De ahí3M(u)<u/25<a u para TODOS u>=128, esto es v>3. La fórmula exacta de h'' prueba entonces

    h''(x)<0, TODOS u>=128.

Este tramo mejora el bound preliminar más conservador u>=1024, que no se presenta como otra construcción. Todos los umbrales proceden de desigualdades analíticas explícitas, sin malla ni certificado adicional.

### Compacto inicial y alcance

Queda g'' en0<u<63/2 y h'' en0<u<128. Antes de un eventual certificado habría que regularizar el origen: b(0)=-kappa4/(6a), b'(0)=kappa4²/(36a²)-kappa6/(120a), mientras h''(0) depende también de kappa8. La positividad individual de cumulantes o la concavidad de M no suministran esas comparaciones mixtas.

Una coordenada exacta para buscar una prueba nueva usa J de076 y

    K(x)=int_|x|^infinito (y-|x|)[aPhi(y)-J(y)]dy>0.

La positividad sigue del único cruce negativo/positivo y masa nula de aPhi-J: la integral de cola de ese peso es positiva para todo x>0, así K'<0 y K(infinito)=0. Si Z_J,Z_K son sus transformadas bilaterales, entonces Z_J=Z'/u y u²Z_K=aZ-Z_J, por lo que b(u²)=Z_K(u)/Z_J(u). Las concavidades requeridas son comparaciones entre DOS leyes inclinadas distintas;073 no las prueba por separado para cada ley. No se declara aquí un bound nuevo para esas comparaciones compactas, un cierre del kernel G ni nueva cobertura de W.
