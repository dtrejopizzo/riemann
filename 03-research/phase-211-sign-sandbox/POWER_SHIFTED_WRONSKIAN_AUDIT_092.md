# POWER_SHIFTED_WRONSKIAN_AUDIT_092 — Auditoría independiente

Estado: **APROBADO / PROVED para la carta de eliminación declarada.** Fuente `POWER_SHIFTED_WRONSKIAN_092.md` y código leídos íntegros. Revisor mapa reprodujo exit0/PASS092, con los mismos intervalos de087 sin cambiarlo. Papers intactos; sin nueva campaña.

## Identidad SHIFT y ecuación

El operadorD3 es mónico con núcleo(1,B,A): su coeficienteD² es−(log(k²J))'=−(2b+j), y el coeficienteD indicado coincide con la factorización ponderada. SustituirF''=s−mF'−AF da exactamenteT0,U,Vc y la matriz2×2 impresa; su determinante es−Delta para la aplicación(h,h')→(D3h,(D3h)'). Los dos homogéneos1/w,t/w tienenWronskianw^−2.

La identidadDarbouxW(D3h1,D3h2)=W(1,B,A,h1,h2)/W(1,B,A) se obtiene eliminando las primeras tres columnas por filas. W(1,B,A)=k²J>0. Elfactorcomúnw de cinco columnas paga w^−5; mover(1,t) delante sonseistransposicionespositivas. Las doscolumnaspolinomialesdejanW(w'',v'',w4), porloqueSHIFTcondenominadorw³k²J ysignonegativo es exacta.

## Signo cerca del origen

Normalizar por tPhi y cambiarlambda=t² da Wshift=8t6Phi³Wlambda; por ello el término inicial es8Phi0³t6D0. Los factoresk! en la matriz3×3 son correctos. Se reprodujo simbólicamente D0=−161280(6a1a3a4−8a2²a4+3a2a3²).

El script092 importa087 intacto y sólo aplica este polinomio a sus intervalosracionales completos. La reproducción mapa exit0 verifica−56488961026<D0<−56488961025 y los mismos extremosracionales. No se cambia precisión, modos ocola de087. La expansión analítica decide una vecindad existente del origen sin asignarle radio.

## Exterior con toda la cola

088 da |Vj−2^jy|<=65 simultáneamentej1..6,uniformeent>=1: el término−9t/2 sólo afectaV1; las serieslog y correccióntheta completa pagan el resto. Los trescocientesdedensidad g1,g2,g3 de la fuente son correctos, incluidos−4g2 enw4/Phi.

Wshift/Phi³=W(g1,g2,g3) es polinomio finito en t y jetsV1..6, con tgrado<=2 y gradojets<=9. Su partegrado9 proviene sólo de(t p1²,p1³,t p1⁴); se reprodujo independientemente su expresión exacta. Sustituir pj=2^jy+ej produce el término4096(2t²−1)y9, también reproducido exacto; todos los demás términos tienen ygrado<=8. Cstar queda definido por una suma FINITA explícita de coeficientes, con |ej|<=65. Así |resto|<=Cstar t²y8 sin suponer un asintótico sinerror. y→infinito fuerza signo positivo eventualmente, sin umbral optimizado ni muestras.

## Cero real y alcance universal preciso

Por continuidad Wshift cambia de signo y tiene un cero interior; w,k,J>0 allí danDelta=0. Falla la inversión GLOBAL de esa carta, aunque numeradoresparticulares podrían también anularse. No se declara un polo inevitable deK ni de cualquier ODE alternativa.

La adiciónAbel es correcta y más precisa: Y1=D3(1/w),Y2=D3(t/w) son suaves y W=−Delta/w² no es idénticamente cero pero tiene cero interior. Cualquier ODEhomog2mónica concoefcontinuos que contuvieraAMBASimágenes obligaría W'=betaW y W=W0exp∫beta; imposible. Esto excluye una extensiónregularcomún deESAecuaciónuniversal conservandoambassoluciones, no una cancelación para la particularK, otra representación/gauge/orden o una ecuacióninhomogdistinta.

Consulta077/087–090 y los tresregistros distingue este Wronskiano desplazado de los signos ya probados. No hay nuevoWnegativo, menorancladodecidido, coberturaW/Tniobstrucciónglobal. El sistema original/otrascartas siguen disponibles.
# Reproducción adicional root

Root reprodujo el intervalo estricto `-56488961026 < D0 < -56488961025` reutilizando directamente los intervalos racionales completos de087. También expandió independientemente el determinante exterior con derivación formal: grado en `t` a lo sumo2, grado total en los jets a lo sumo9 y coeficiente de `y^9` exactamente `4096(2t^2-1)`. Ambas comprobaciones terminaron con PASS. Son verificaciones de las obligaciones fijas de esta prueba, no una exploración de parámetros.

