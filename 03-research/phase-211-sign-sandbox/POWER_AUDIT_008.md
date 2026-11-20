# POWER_AUDIT_008 — Auditoría del patrón contrario de contactos bajos

Estado: PROVED, revisión independiente de POWER_PRIME_PATTERN_FALSIFIER_008.md. Papers intactos.

## 1. Vector y momentos exactos

Para n131072 y u63/2, g=y^(n-1)e^(-uy) tiene g(0)=g'(0)=0 y el decaimiento requerido para integrar dos veces por partes. Así f=(D²-1/4)g tiene transformada Laplace (n-1)!(s²-1/4)/(s+u)^n, sin términos de borde ni distribuciones adicionales. Los dos momentos son exactamente cero. El grado2 del numerador es menor que n y el vector pertenece al espacio confluente declarado.

La densidad espectral es la Student racional de base multiplicada por (tau²+1/4)^2, no por un factor de signo incierto. La fórmula beta da M2=u²/(2n-3), M4=3u^4/[(2n-3)(2n-5)], M6=15u^6/[(2n-3)(2n-5)(2n-7)]. Como u²<1024 y cada denominador es mayor que n, sus cotas por128 son correctas. El denominador de la reponderación es >=1/16, por lo que

    E_f tau²<=16M6+8M4+M2
               <15/131072+192/131072+1024/131072
               =1231/131072<1/100.

No se usa aproximación asintótica ni factorización de factoriales gigantes.

## 2. Déficit de la forma sin peine

La serie de m y la cota de denominadores producen m(tau)-m(0)<17tau², porque sum a_k^-3<=64+104/125 y un cuarto de esta cota es menor que17. La identidad de psi1/4 da m(0)=-gamma-pi/2-3log2-logpi<-4; las desigualdades elementales propuestas incluso dan <-9/2. Por tanto ARCH/||f||²<-383/100, y el polar cero conserva esa negatividad para ARCH+POLAR.

## 3. Contactos y obligación de cola

Para un vector real, Parseval y la paridad de su densidad espectral identifican c_f(t)/||f||² con el promedio de cos(tau t). La desigualdad cos x>=1-x²/2 da c_f(t)/||f||²>1-t²/200. Como logq<=10log2<10 para q<=1024, todas esas autocorrelaciones son mayores que1/2. Cada contacto primo-potencia no nulo de ese segmento aporta por tanto signo estrictamente negativo; los enteros con Lambda0 no aportan.

La desigualdad TAIL del memo sigue exactamente de W>=0, AP<-383/100 y la cota estricta de los contactos bajos: la cola tendría que superar 383/100+sum_(2<=q<=1024)Lambda(q)q^-1/2. Se afirma únicamente como obligación necesaria, no como estimación ya probada. La convergencia absoluta del peine está justificada por autocorrelación exponencial por polinomio y tasa31.5.

## 4. Alcance aprobado

El test muestra dentro de la misma familia que el patrón de reparación por contactos bajos de WITNESS006 no es universal. No demuestra negatividad de W, no contradice el certificado completo V12 y no es un nuevo teorema general de negatividad de subpeines. La cola por encima1024 permanece sin signo evaluado. La etiqueta PROVED es apropiada exactamente para vector, polar nulo, déficit AP y efecto de cada contacto declarado.
