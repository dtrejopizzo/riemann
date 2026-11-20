# POWER_CONTACT_OSCILLATION_AUDIT_065

Estado: **APROBADO** POWER_CONTACT_OSCILLATION_065 tras lectura completa. Prueba analítica; no requiere tests numéricos. Autocorrelación y signo de cola, no signo de W. Papers intactos.

Se cotejaron índice/grid/crucigrama, ARITHMETIC_DIFFERENCES019 y su auditoría, DESCENT016 y las referencias de oscilación/Descartes.019 sólo decide la columna k=1. La diferencia actual es un conteo exacto para TODOS N,k mediante momentos nulos y filtros exponenciales unilaterales. No se presenta Rolle o un principio nodal genérico como mecanismo de signo de la forma completa.

## Perfil y momentos

PROFILE tiene todos sus factores correctos: derivar2k introduce u^(2k), que cancela esa potencia del denominador de C_(N+k), dejando u^(2N−1). El factor factoriald!,2^(d+1), el signo(−1)^k y el coeficiente principal unitario son correctos. COEFF resulta de cancelar los factoriales del cociente a_(j+ell)/a_j; la suma termina antes de cualquier factorial descendente nulo en el denominador.

La transformada tau^(2k)/(u²+tau²)^(N+k) tiene exactamente el cero requerido en0 y es integrable, incluso en N=1. El perfil temporal tiene todos los momentos absolutos y por ello ZERO-MOMENTS se deduce legítimamente. K(0)>0 se obtiene de la integral espectral positiva. El argumento del polinomio producto de los cambios de signo usa sólo momentos de grado inferior a2k y cuenta cambios reales, no meros ceros tangenciales.

Revisada también la adición explicativa de root al inicio de§3: paraN=1 yk=1,2,3, aplicar(1−D)^(2k) a p_k, multiplicar por(−1)^k y dividir por el valor en0 produce exactamente1−x,1−5x/3+x²/3 y1−11x/5+4x²/5−x³/15. El factor común exp(−x) y la normalización por K(0) son correctos. Son ejemplos algebraicos del perfil, sin afirmación adicional sobreW ni alteración de la prueba general.

## Lema unilateral y simplicidad

Fubini preserva todos los momentos nulos indicados bajo cada filtro, no sólo al completar un par simétrico. g'=f−ug implica que un cero de g con f distinto de0 es simple. Si coinciden un cero de g y un cero simple de f, existe g″ allí y vale f′, no nulo: el cero sería doble. La inducción supone ya que TODOS los ceros de f son simples; sin esa hipótesis no bastaría el argumento de simplicidad. La fuente la conserva explícitamente.

El cero adicional de h'=exp(ut)f antes del primer cero seleccionado de h está bien justificado: h tiende a0 en−infinito, vale0 en ese cero y no es idénticamente0 entre ambos. Elegir un punto de valor no nulo y usar ambos extremos de valor límite0 da un extremo interior no nulo. No se aplica formalmente Rolle en un punto infinito. Los ceros heredados de multiplicidades y los ceros intermedios están en intervalos disjuntos; la cuenta da al menosm ceros de h′ si h tiene m contados con multiplicidad. También se aplica a cualquier colección finita, excluyendo infinitos ceros. El filtro reflejado usa el borde opuesto correctamente.

El posible cúspide en0 del caso base no es un cero, pues K(0)>0. Todos sus ceros están en regiones analíticas. Tras la primera convolución la función es C1; las coincidencias de ceros en0 admiten las derivadas locales usadas. No hay intervalos de anulación: la ecuación diferencial los propagaría hacia f, contradiciendo sus ceros finitos simples. El decaimiento exponencial por polinomio preserva las convergencias y el borde ponderado.

## Base, propagación y último cero

En N=1 el perfil positivo tiene un polinomio de grado k. Paridad y momentos fuerzan al menos2k cambios globales; el grado permite a lo sumok raíces positivas. Quedan exactamentek raíces positivas distintas. Como ese polinomio tiene grado k, todas son simples y no admite raíces adicionales de mayor multiplicidad. Sus reflejos negativos son simples y0 no es raíz.

C_1=e_+*e_- con la normalización1/(2u) es exacta. Aplicar los dos filtros sucesivamente conserva los2k ceros y momentos; al terminar cada par se recupera la autocorrelación par del siguiente N. Esto prueba el conteo para todo N sin suponer paridad en el paso intermedio.

La cota p_d^(ell)/p_d<= (d/x)^ell usa coeficientes positivos y vale también cuando ell>d, con derivada cero. La expansión binomial limita|r−p|/p por(1+d/x)^(2k)−1. Para x>=4kd, exp(1/2)<2 deja r estrictamente positivo, incluso en el extremo. Por tanto la mayor raíz es ESTRICTAMENTE menor que4kd. El resultado no sustituye la cota más fina019 en k=1.

## Cola y alcance

El signo final de K es(−1)^k; el factor negativo del peine lo cambia a(−1)^(k+1). La cola desde u logq>=4kd conserva ese signo. Para u>1/2 converge absolutamente y contiene infinitas potencias de2 de peso positivo, por lo que su suma tiene signo estricto. El caso k=0 está separado y no se interpreta como transición.

No se estima la magnitud de esa cola frente al prefijo, ARCH y polar. No hay nueva fila de signo W, ventana temporal ni conclusión global. La aprobación se refiere exactamente al patrón de raíces y al signo declarado del complemento aritmético.
