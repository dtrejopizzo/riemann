# POWER_STATE_060 — Cono uniforme de positividad para todos los numeradores

Estado: PROVED en la región declarada; signo global OPEN. Papers intactos.

Con u=63/2, Q(s)=s/(s+u), q_n=ceil(log_2(n+1)) y J(n)=10^12(nq_n)^3, para TODO n>=1, TODO polinomio real no nulo P de grado<n y TODO entero j>=J(n),

    W[Q^j P/(s+u)^n] > ||Q^j P/(s+u)^n||².

Además la integral absoluta de la densidad desplazada a altura3 es menor que2 veces la integral real, con constante INDEPENDIENTE de n y P. Esto controla las autocorrelaciones por2exp(−3|t|)norma² y conserva TODO el peine infinito.

Fuente POWER_UNIFORM_STRIP_060.md, diez secciones. Auditoría independiente completa POWER_UNIFORM_STRIP_AUDIT_060.md APROBADA. Root leyó y verificó la prueba completa y su auditoría. Es matemática analítica, sin campaña de parámetros ni cálculo de casos aislados.

## Mecanismo y diferencia respecto054

El peso racional exacto en frecuencia inversa tiene polinomios ortogonales con una recurrencia explícita. Esto permite controlar la primera derivada de una amplitud sin fase causal por200(n+2)^(3/2)/(u sqrt(j)). Al derivar repetidamente se contabiliza el cambio de clase(n,j) a(n+3r,j−r).

La constante grandeD_n de054 sólo paga la cola de Taylor, por Cauchy en L² a altura15. Los primeros20nq_n términos se pagan con la cota de derivadas; no se exponentia una norma en dimensión fija ni se compara globalmente con una gaussiana. Así se obtiene una norma de traslación menor que1.1 a alturas±3, uniforme en n. Para polinomios complejos se usa la evaluación individual de054; el producto de la densidad se recupera después mediante Cauchy entre alturas opuestas.

La suma aritmética completa tiene módulo<2norma², ARCH>4norma² y el polar tiene módulo<norma². El balance demuestra el signo con margen. El corte pasa del enormeK(n)054 aO(n³ log³n); también basta10^12n^6.

## Lo que permanece abierto

No se prueba el segmento j<J(n), no se deduce por descenso ni por mezcla su positividad, y no se afirma un cono cuadrático uniforme.059 sólo da una condición necesaria cuadrática para esta clase de estimaciones. No se añade una ventanaT del Paper47. El resultado053 para trece polos arbitrarios permanece vigente por separado. El cierre global exige aún controlar el interior aritmético firmado.
