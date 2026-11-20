# POWER_THETA_DENSITY_COMPACT_AUDIT_089 — Auditoría independiente

Estado: **APROBADO / PROVED con constructor40406 exit0/FULL PASS** de las dos ramas. Reproducción independiente root87911 exit0/FULL PASS1024origen+8192resto y mismo hash; no se duplicó innecesariamente. Fuente `POWER_THETA_DENSITY_COMPACT_089.md` completa y código final leídos; diseño y literal auditados ANTES de ejecutar. Hash comprobado localmente:

    995ef292abf5a80a3d195b4e68a815e1b56f9b343531bc1c0786af682413d1aa

Papers intactos.

## 1. Dos dominios y puente

rho=tPhi(1,A,B,C); enlambda=t²,Psi=rho/t. La multiplicación común port y el cambio de variable de un Wronskiano4 dan EXACTAMENTE K=Wt(rho)=t4(2t)^6Wlambda(Psi)=64t10Wlambda(Psi). Así origenlambda[0,1/256] y restantet[1/16,1] cubren0<t<=1 sin hueco y evitan dividir por cantidades pequeñas.

Las expresiones Psi=(phi,6phi'+4lambda phi'',−2phi',−12phi''−8lambda phi''') son correctas. Se usa phi=Phi(sqrtlambda) SIN normalizar; el signo no necesita dividir porPhi0.

## 2. Mayorantes analíticos y colas completas

Las comparaciones complejas exp/cos de la fuente pagan |Phi_m|<152m4·4^−m² en|t|<=1/4, con suma geométrica<1000. Paridad holomorfa delPhi COMPLETO da phi holomorfa en el disco de lambda. Las cotas de sus derivadas por Cauchy, columnas dePsi y determinante24términos danB1e48 en|lambda|<=1/32. La cota redondeada de columnas ya basta; se corrigió un error de exponente del auditor durante el diseño, sin cambiar los parámetros del constructor.

Para la rama restante, los discos de radio1/32 alrededor de t∈[1/16,1] dan |Phi_m|<4288m4·8^−m² y |Phi|<10000. En discos interiores1/64 se obtienenp_k=10000k!64^k. Las columnas rawrho requieren como máximo(2p3+3p2,2p5+5p4,p4,p6); su producto24 es3936828360292381907930506017700508073984000000000000000000<1e60, reproducido conFraction.

Las colas m>=17 se pagan COMPLETAS por304·17⁴/4²⁸⁹ y8576·17⁴/8²⁸⁹, respectivamente. Sus razones son<1/2. Los errores de TODOS los coeficientes se acotan por epsilon32^k usando discos centrados de radio1/32 contenidos en el dominio complejo mayor. Se incorporan ANTES de derivarPsi/rho, no sólo al determinantefinal. La cola theta y la cola deTaylor del determinante son errores distintos y ambos están incluidos.

Los restos finales son1e48(1/8192)^17/(1−1/8192)<1e−18 y1e60(15/4096)^41/(1−15/4096)<1e−39; comprobados porFraction exacta. No se usan funciones muestreadas para pagar puntos intermedios.

## 3. Literal y ejecución

ORIGIN:1024bits/cap23,1024panelesdyádicoslambda, evenpartial16=[Phi16(sqrtlambda)+Phi16(−sqrtlambda)]/2. La simetrización es indispensable porque un parcialtheta NOespar. Loscentros son positivos y susqrtformal válida. Se añaden errorescoef0..22; seisderivadasmáximas dejanWprec>=17.

REST:512bits/cap47,8192panelesdyádicost, Phi16directa conerrorescoef0..46;Wprec>=41. Los dosdeterminantes se calculan por seisproductos2x2 sin divisiones. SignoLaplace(−1)^(i+j+1) correcto. Todos los coeficientes necesarios deben ser finitos; el bound superiorN0+sum|Nk|h^k+resto debe ser estrictamente negativo. Ambos dominios/extremos están cubiertos con centros/radios exactos.

Diseño, mallas, precisiones, modos y grados quedaron auditados y fijados antes del único proceso constructor40406. Terminó exit0/FULL PASS1024origen y8192resto; sinFAILni ajuste. El script no se modificó y hash arriba coincide localmente. No se ejecutó una copia adicional innecesaria mientrasrootreproduce.

## 4. Transporte global REAL-R

Leída y aprobada la sección8 final de la fuente. Un desarrollo independiente está en `POWER_THETA_DENSITY_TRANSPORT_089.md`. BRIDGE+certificados+088 dan Wt(1,A,B,C)<0 paraTODOt>0. El orden correctoECT es[1,B,A,C], conWronskianos1,B'>0,(B')²J>0,−Woriginal>0. No se presupone A'>0. Rolle en la coordenadaB prueba el determinante de densidades original estrictamente negativo paraTODOSlos cuatro nodos.

El kernelL=sinh(sqrtlambda t)/sqrtlambda esTP4 también enfilasconfluentes: seriepositiva,Cauchy–Binet,monomiales y término0..3estricto. Integración bilateralporpartes conserva losbordes;Andreief admite densidadesfirmadas porque cada término es absolutamente integrable por supercolas. F=(Z'/u,uZ',Z,u²Z)=F0(1,lambda,R,lambdaR), F0>0; la versiónconfluente da W(F)<0, exactamente−F0⁴T_R. Por tanto T_R>0 PUNTUALMENTE enTODOlambda>0, no sólo una desigualdad débil dejet.

## 5. Consecuencias y límites

090 deja de necesitar un inputthetaglobal no probado: T_Rglobal aplica sulemasecante y da h=1/bstrictconcava enTODOx>0. Junto086g_*=xbstrictconcava y078, se prueban todos los pares distintosdelkernelGp paraTODOp>0, incluidosremovibles. Esto permiteGp'negativa yno contradice081.

No se descarga la otra curvatura recíproca delresto ni Turánsuposterior, noherenciageneralSchur. NoS4transporteglobal, cinco/todoslosórdenes,T oWnuevarespecto085. El resultado estructuralGLOBAL-R4/T_Rglobal no elimina sus antecedentescertificados: es independiente delcertificado085 enparámetrou, pero depende073/077/086/088 más elcertificadofijo089.
