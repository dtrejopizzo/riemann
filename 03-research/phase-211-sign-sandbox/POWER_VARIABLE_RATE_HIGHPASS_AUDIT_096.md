# POWER_VARIABLE_RATE_HIGHPASS_AUDIT_096 — Auditoría independiente

Estado: **APROBADO / PROVED**, fuente `POWER_VARIABLE_RATE_HIGHPASS_096.md` leída íntegramente. Revisor mapa; root aprobó independientemente todas sus estimaciones. Sin campañas ni certificados numéricos; papers intactos.

## 1. Objetivo fijo y normalización

Cayley a tasa u transforma el MISMO exponencial normalizado de tasa u0 en H_a=sqrt(1−a²)/(1+az), a=(u−u0)/(u+u0). El vector de emparejamientos con z^j(1+z)^r es sqrt(1−a²)(1−a)^r(−a)^j. Por tanto PROJECTION es exactamente NORMA CUADRADA, no norma ni densidad espectral. xi=−a recorre todo(−1,1) cuando u>0; no se mantiene falsamente constante el objetivo al variar la tasa.

## 2. Gegenbauer y las dos paridades

Rodrigues coincide con la suma de coeficientes. Integrar k veces por partes elimina los bordes para lambda>=1 y da h_k con el factor beta correcto; D^kC_k=2^k(lambda)_k. Las dos fórmulas de valores centrales y derivada impar conservan pi,4 y las razonesGamma. El lowerGamma sqrt(x−1/2) usa Cauchy–Schwarz más Gamma(x+1/2)=(x−1/2)Gamma(x−1/2); el upper es Jensen. BASE-VALUES es holgado pero válido incluso m=0 y n=1.

En is todos los términos de C_k tienen la misma fase. Tras normalizar, las sumas con factoriales(2j)! y(2j+1)! se pagan por cosh y sinh(X)/X, incluidoX0. No se usó una cota oscilatoria sin conservar signos.

El centrado exp(−idtheta/2) divide correctamente frecuencias enteras o semienteras. E es par y O impar aun con coeficientes complejos; el cruce se anula por paridad en la integral, no por suponerlos reales. La medida circular produce exactamente4^r/pi y pesoslambda r/r+1 intercambiados según la paridad. En theta=i eta, P(xi)=xi^(d/2)T y el factor sqrt(1+s²) se paga sin perder una normalización.

## 3. Región NEAR

Las sumas de evaluaciones ortonormales se acotan por8n sqrt(r) y96n²r^(3/2)s² con el mismo exponencial. Los grados ausentes dan suma vacía; n1 no requiere una componente impar. Cauchy–Schwarz en la suma directa de ambos sectores produce CENTER-KERNEL con factor2 suficiente.

La potencia ((1+xi)/2)^(2r) cuesta exp(−3r eta/4), mientras el kernel sólo repone exp(r eta/4), por r>=1024n y s<=eta<=1. Los máximos exactos de eta e^(−r eta/2) y eta³e^(−r eta/2) dan128+41472n/r<=168.5<200. pi<4,1−xi²<=2eta y xi^d<=1 fueron incluidos. No se interpreta el extremo xi1 como un vector Hardy admisible.

## 4. Región FAR y uniformidad

El determinante exacto094, con r>=n, da el lowerGram: cada factor relativo a C=binom(2r,r) es>=j!/(2r)^j. lambda_min>=det/(trace)^(n−1) y ||v||²<=n pagan el inverso completo, sin una cota diagonal insuficiente. C>=4^r/(2r+1) y1+xi<=1+e^−1<3/2 dan exactamente FAR-GRAM, incluidos TODOS los xi negativos.

Las tres cotas logarítmicas bajo r>=1e12n³ son correctas. log(2r)<2r^(1/3) sigue del máximo de log x/x^(1/3) y e>2; sus constantes pagan n²/r^(2/3)<=1e−8. La suma de logs positivos es<r/100 y log(16/9)>1/2, por lo que el factor exponencial domina uniformemente n,r. exp(r/4)>1+r/4>=sqrt(r) completa FAR. n1 y todos los extremos de tasas quedan cubiertos sin argumento asintótico implícito.

## 5. Resultado y alcance

Se prueba A_(n,r)(xi)<=200n/sqrt(r)<=1/5000 para TODOS n>=1,r>=1e12n³,u>0 y cualquier objetivo fijo u0>0. Así la distancia del exponencial normalizado a la UNIÓN de todos esos espacios, permitiendo TODAS las tasas, es>=sqrt(4999/5000). No se afirma que cada aproximante tenga norma1: se trata de la distancia a un subespacio lineal completo, calculada mediante su proyección ortogonal.

Consultados los registros y016/029/054/060/094. La diferencia respecto de094 es la uniformidad en la tasa con objetivo temporal FIJO; respecto de016 es L² SIN peso. El cono060 está incluido por su umbral. No se trata la envolvente lineal, cruces entre bloques, mezclas de densidades ni añadir otras familias continuas iniciales. No W negativo ni imposibilidad global de cerrar W; no nueva cobertura W/T.
