# POWER_THETA_DENSITY_COMPACT_089 — Signo global del Wronskiano real R4 por densidades

**Auditoría independiente:** `POWER_THETA_DENSITY_COMPACT_AUDIT_089.md` aprobada; constructor40406 FULL PASS, reproducción independiente root87911 exit0/FULL PASS1024+8192 y hash coincidente. Desarrollo de transporte independiente: `POWER_THETA_DENSITY_TRANSPORT_089.md`.

Estado: **PROVED, certificado constructor y reproducción independiente root87911 exit0/FULL PASS; auditoría matemática y código aprobadas.** Los objetos, dominios, colas y parámetros se fijaron y auditaron antes de implementar y ejecutar. Se prueba el transporte del LADO_R por densidades; no S4 ni una nueva cobertura W respecto085. Papers intactos.

## 1. Objeto y antecedentes

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D; releídos077,083–088.087 decide el Wronskiano R4 en el origen y088 su exterior t>=1. Faltaba el compacto0<t<1 de la MISMA Phi. La condición puntual de densidades es más fuerte que la curvatura transformada ya probada085: no se hereda desde ella.

Conservar las cuatro densidades

    rho=(tPhi,(tPhi)'',−Phi',−Phi'''),
    K(t)=W_t(rho1,rho2,rho3,rho4).

Como rho=tPhi·(1,A,B,C),

    K(t)=(tPhi)^4 W_t(1,A,B,C).

No se divide numéricamente por Phi ni por t. Para el origen poner lambda=t² y phi(lambda)=Phi(sqrt(lambda)), SIN normalizar por Phi(0). Las cuatro densidades divididas por t son

    Psi=[phi,6phi'+4lambda phi'',−2phi',−12phi''−8lambda phi'''].

Aquí las primas de phi son respecto de lambda. Las identidades exactas de Wronskianos dan

    K(t)=64t^10 W_lambda(Psi)(t²).                  (BRIDGE)

Por tanto se fijan dos obligaciones complementarias: W_lambda(Psi)<0 en0<=lambda<=1/256, y K<0 en1/16<=t<=1. Su unión cubre0<t<=1 y evita la cancelación de orden10 en el origen.

## 2. Bound complejo theta para la rama de origen

Si |t|<=1/4, entonces

    Re exp(2t)>=exp(−1/2)cos(1/2)>1/2.

Basta exp(1/2)<5/3, cos(1/2)>7/8 y(3/5)(7/8)>1/2. El primer bound se deduce de e<87/32<25/9 y el segundo de la serie alternante de cos. Además |exp(2t)|<2 y |exp(5t/2)|<2: para el segundo usar exp(1/2)<5/3 y exp(1/8)<8/7.

Así cada modo satisface en ese disco

    |Phi_m(t)|<152m⁴4^(−m²),

usando pi<4, pi Re exp(2t)>3/2 y exp(3/2)>4. La suma queda acotada por1000: la razón consecutiva de m⁴4^(−m²) es<=16/4³<1/2 y por ello152Σ<=76<1000.

La paridad analítica de Phi da una función phi holomorfa en un entorno del disco|lambda|<=1/16, con

    |phi(lambda)|<1000.

Para |lambda|<=1/32, Cauchy con radio1/32 da

    |phi^(k)(lambda)|<=1000k!32^k.

En el Wronskiano de Psi, las filas son derivadas de órdenes0,...,3. Con P_k=1000k!32^k, las cuatro cotas máximas exactas de columnas son

    [P3,18P4+P5/8,2P4,36P5+P6/4]
      =[196608000,956301312000,50331648000,338228674560000].

El bound por las24permutaciones es menor que10^48. Se puede usar el mismo B_origin=10^48 en TODO |lambda|<=1/32.

## 3. Partición y aproximación completa del origen

Se fijan1024paneles iguales de[0,1/256], con centros positivos exactos y radio h_lambda=1/524288. En cada centro se usa Taylor de W_lambda(Psi) hasta grado16, con disco r_lambda=1/64. Todos esos discos quedan en|lambda|<=5/256<1/32. El error completo de Taylor es

    R_origin=10^48(1/8192)^17/(1−1/8192)<10^(−18).

Se fijan precisión1024bits y cap de phi23: el determinante necesita coeficientes hasta grado16 y derivadas de phi hasta orden22, porque la cuarta columna de Psi contiene phi''' y se deriva tres veces al formar el Wronskiano.

Para evaluar jets usar EXACTAMENTE

    phi16(lambda)=[Phi16(sqrt(lambda))+Phi16(−sqrt(lambda))]/2,

donde Phi16 retiene modos1,...,16. El promedio es esencial: un parcial theta individual no es par, y su composición con sqrt no sería analítica enlambda=0. La función phi16 sí lo es; los centros son positivos, de modo que las series formales de sqrt tienen rama real definida.

La cola COMPLETA en|lambda|<=1/16 queda acotada por

    epsilon_origin=304·17⁴/4^289,

pues desde m=17 la razón es<=(18/17)^4/4^35<1/2. El promedio de las dos colas no añade un factor2. En cada centro, Cauchy con radio1/32 da error de coeficiente de phi de orden k a lo sumo epsilon_origin32^k. Se añade esa bola a TODOS los coeficientes0,...,22 ANTES de formar Psi, sus derivadas y el determinante. No se sustituye esta cola por una comprobación de paridad o por precisión flotante.

## 4. Bound complejo theta para la rama restante

Sean c0∈[1/16,1] y |z−c0|<=1/32. Entonces

    Re z∈[1/32,33/32], |Im z|<=1/32,
    |y|=|pi exp(2z)|<32, Re y>5/2,
    |exp(5z/2)|<16.

Para los uppers bastan exp(33/16)<8 y exp(165/64)<16, ambas comparaciones con log2>56/81. Para Re y, usar pi>3, exp(2Re z)>1 y cos(1/16)>511/512. De ahí

    |Phi_m(z)|<4288m⁴8^(−m²),
    |Phi(z)|<10000.

El coeficiente4288 es4·16·(64+3); exp(5/2)>8 paga el decaimiento. La suma se acota por una geométrica, con razón inicial16/8³<1/2.

En el disco interior |z−c0|<=1/64, Cauchy con radio1/64 conserva el disco exterior y da

    |Phi^(k)(z)|<=p_k=10000k!64^k.

Como |z|<2, las cotas máximas de columnas del Wronskiano rawrho son

    [2p3+3p2,2p5+5p4,p4,p6].

Sus24productos quedan por debajo de10^60. Por tanto B_rest=10^60 es un bound uniforme de|K| en cada disco interior.

## 5. Partición y cola de la rama restante

Se fijan8192paneles iguales de[1/16,1], con radio h_t=15/262144. El radio Cauchy para K es r_t=1/64, de modo que h_t/r_t=15/4096. Se usa Taylor de grado40 con error completo

    R_rest=10^60(15/4096)^41/(1−15/4096)<10^(−39).

La precisión es512bits, capPhi47: la cuarta densidad es−Phi''' y su tercera fila derivada usa Phi^(6), por lo que el coeficiente40 necesita Phi hasta grado46.

Se evalúa Phi16 DIRECTAMENTE como función de t. No hace falta simetrizar en esta rama sin sqrt. La cola completa en todos los discos exteriores es

    epsilon_rest=8576·17⁴/8^289,

con razón consecutiva desde17 menor que1/2. Se añade a cada coeficiente k=0,...,46 el error de Cauchy epsilon_rest32^k ANTES de derivar las densidades y formar el Wronskiano.

## 6. Asserts de signo y parámetros fijados antes de ejecutar

Para CUALQUIERA de las dos ramas, los coeficientes C_k del determinante están normalizados por k!. Se certifica el signo negativo en cada panel por

    C0.upper+Σ_(k=1)^degree |Ck|.upper h^k+Remainder<0.

Se exigen todos los coeficientes finitos y la precisión formal necesaria (al menos17 para origen y41 para resto). No se pasa de valores centrales negativos a un intervalo sin el resto. Las bolas de la cola theta se incorporan a los jets de phi/Phi, separadamente del resto de Taylor del determinante.

Los dos dominios, sus1024/8192paneles, las precisiones1024/512, los grados16/40, caps23/47,16modos y las colas quedan fijados por estas derivaciones antes de implementar o ejecutar. No hubo FAIL ni cambio de un parámetro después de ejecutar. Ningún signo se obtuvo por una búsqueda de mallas o rangos.

## 7. Resultado reproducible

Código estable: tools/power_theta_density_compact_089_verify.py. Usa series reales Arb con las dos precisiones y caps declaradas, añadiendo las bolas de cola a TODOS los coeficientes antes de derivar. El determinante se calcula por expansión de Laplace en las primeras dos filas: seis productos de menores2x2, sin divisiones. Se verifica precisión formal al menos17/41 y finitud de todos los coeficientes necesarios.

La corrida constructor40406 terminó exit0 y FULL PASS:

    ORIGIN:1024/1024paneles,W_lambda(Psi)<0 en[0,1/256];
    REST:8192/8192paneles,W_t(rho4)<0 en[1/16,1].

Ejecutar

    python3 03-research/phase-211-sign-sandbox/tools/power_theta_density_compact_089_verify.py

SHA256 de la versión exacta que terminó, no modificada durante su ejecución:

    995ef292abf5a80a3d195b4e68a815e1b56f9b343531bc1c0786af682413d1aa.

El archivo.sha256 fija la misma versión para reproducción. Las colas theta y los dos restos Cauchy se imprimen como fracciones exactas. No hubo evaluación de signos diagnósticos ni ajustes después de resultados: las dos obligaciones continuas fueron las predeclaradas en este mismo archivo.

## 8. Empalme, Rolle y transporte global del lado R

BRIDGE y ambos certificados prueban W_t(1,A,B,C)<0 en0<t<=1.088 aporta el mismo signo para TODOt>=1. Por tanto

    W_t(1,A,B,C)<0 para TODOt>0.                    (GLOBAL-R4)

086 ya da B'>0 y J=(A'/B')'>0. Con E=(C'/B')', la identidad Darboux de087 implica(E/J)'>0 para TODOt>0. En el orden(1,B,A,C), los Wronskianos iniciales tienen signos1,B'>0,(B')²J>0 y−Woriginal>0. No se presupone un signo de A'.

Para probar el signo del determinante de evaluación, usar la coordenada z=B(t). Si una combinación no nula a+bB+cA+dC tuviera cuatro ceros, Rolle daría al menos dos ceros a cA_zz+dC_zz. Dividir por A_zz=J/B'>0 deja c+d(E/J), que tiene a lo sumo un cero por su monotonía estricta, salvo c=d=0. En ese borde una función afín en B no admite cuatro ceros sin anularse idénticamente. Así el determinante no se anula en la cámara de cuatro nodos positivos ordenados; su signo confluente GLOBAL-R4 lo fija estrictamente negativo en el orden original(1,A,B,C). Multiplicar las filas por t_iPhi(t_i)>0 conserva el signo de las cuatro densidades rho.

El kernel

    L(lambda,t)=sinh(sqrt(lambda)t)/sqrt(lambda)
                =Σ_(m>=0)lambda^m t^(2m+1)/(2m+1)!

tiene menores de tamaño4 positivos para nodos positivos ordenados. La prueba es la de086, ahora con cuatro filas: Cauchy–Binet sobre truncamientos produce productos de determinantes de monomios con exponentes estrictamente crecientes, positivos por Rolle y sus Wronskianos. El término m=0,1,2,3 garantiza estricta positividad. Lo mismo vale para las filas confluentes de derivadas0,...,3 enlambda, por los Wronskianos de lambda^m. La convergencia de las series y sus derivadas es localmente uniforme.

La integración por partes bilateral, con bordes superexponenciales nulos, da

    LT(rho)=(Z',u²Z',uZ,u³Z).

Dividir por u>0 y poner lambda=u² produce funciones

    F=(Z'/u,uZ',Z,u²Z)
      =2∫_0^infinito L(lambda,t)rho(t)dt.

Andreief —expansión de determinantes y Fubini— transporta el signo negativo del determinante de densidades a detF para cuatro nodos lambda positivos. También su versión confluente da W_lambda(F)<0. Cada término es absolutamente integrable por las colas superexponenciales de Phi y sus derivadas, aun después de las derivadas del kernel sobre compactos de lambda>0.

Como F0=Z'/u>0 y

    F=F0·(1,lambda,R(lambda),lambda R(lambda)),

se obtiene en particular

    W_lambda(1,lambda,R,lambda R)<0,
    2R'R'''−3(R'')²>0 para TODOlambda>0.            (REAL-R-TURAN)

La identidad del último Wronskiano es exactamente la de084. Así el lado R tiene ahora una prueba global por las densidades de la MISMA Phi, independiente del certificado en parámetro u de085. No se ha quitado una contribución de la forma completa ni usado positividad de un kernel ajeno.

## 9. Alcance exacto

El resultado es GLOBAL-R4 y el transporte REAL-R-TURAN del LADO_R para todos los parámetros positivos. No trata las cuatro densidades del lado S ni demuestra una regla de herencia a niveles superiores. La base de tres densidades086 y el nuevo Wronskiano de cuatro se verificaron separadamente; no se sustituyó ese dato por la concavidad genérica refutada084.

La positividad W de cuatro generadores085 permanece válida, pero este resultado no amplía su cobertura admisible, no prueba cinco generadores, todos los órdenes ni una ventana temporal. Su aporte es la comparación de densidades que explica y transporta estructuralmente uno de los dos signos recíprocos. El objetivo global del paper permanece OPEN; papers intactos.
