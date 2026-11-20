# AUDIT_009 — Prueba directa del enlace por flujo logarítmico

2026-10-19. Revisor independiente. Leído LINK_009_CONTINUOUS_FLOW.
**Veredicto: PROVED teoremas1–2 en sus clases precisas. No NO-GO de O1 ni de D.**

## 1. Corpus y diferencia respecto del intento anterior

Búsqueda en índice/grid/crucigrama de interpolación, continuidad fuerte, flujo y Frobenius; lectura de Paper44 rem:nointerp y 007–008. El cambio de objeto es explícito: esta prueba trabaja con V_n en la norma positiva canónica K, no con soportes de medidas Frobenius. La componente gaussiana se incluye y se prueba que no cancela la separación aritmética. Eso admite el test sin reintentar una construcción cerrada.

**Precisión de la referencia Paper44:** continuidad débil de una familia arbitraria de medidas compactas no puede descartarse sólo porque el soporte cambie de tipo. Los tiempos log n no tienen acumulación finita, y es posible interpolar convexamente entre medidas consecutivas sin ley de semigrupo ni requisito de seguir siendo objetos Frobenius puros. Por tanto la referencia previa no debe expresarse como prohibición de TODA interpolación continua. LINK009 no depende de esa afirmación: sus pruebas nuevas usan la ley de semigrupo/un grupo unitario y un límite de normas explícito.

## 2. Vector y separación exacta

A=X₂−1/2 es Haarcentrado y |A|²=1/4 punto a punto. Para n,m impares coprimos, D_nA=X_n A y D_mA=X_m A: dividir por un impar no cambia v₂. Bajo P_s, las coordenadas de los primos de nm son independientes de v₂. Así

    E_s(V_nA conjugado(V_mA))=(nm)^(−s/2)/4,
    E_s|V_nA|²=E_s|V_mA|²=1/4.

La distancia cuadrática del factor aritmético es κ/2·[1−(nm)^(−s/2)]. La norma de K es SUMA de esta forma positiva y una norma gaussiana; no hay término de signo negativo capaz de cancelarla. La desigualdad(1) es correcta.

n_k=2k+1 y m_k=2k+3 son impares coprimos porque su máximo común divisor divide2. Su razón tiende a1 y el límite inferior de la distancia no es cero. La cota ||G_nTA||≤sqrt(Π(A)/n) de007 da que la distancia gaussiana tiende a cero. El límite de la distancia cuadrática COMPLETA es por tanto κ/2>0. No se necesita ningún cálculo numérico.

## 3. Interpolación por semigrupos C₀

Si W(log n)=V_n y W es un semigrupo C₀, escribir m/n>1 permite factorizar

    W(log m)−W(log n)=W(log n)[W(log(m/n))−I].

En los tiempos muestreados se sabe exactamente ||W(log n)||=||V_n||≤1, lo que elimina el tiempo grande log n; no hace falta una cota global sobre W. La continuidad fuerte se aplica al vector FIJO A en tiempo log(m/n)→0. Contradicción con la separación de §2. La extensión a toda reescala n^βV_n se verifica en §6.

## 4. Compresión unitaria con mapas fijos

Para V_n=P U(log n)J, con P,J acotados fijos y U unitario C₀,

    ||V_mA−V_nA||≤||P||·||(U(log(m/n))−I)JA||→0.

La unitariedad permite sacar U(log n) sin crecimiento de norma y la continuidad actúa sobre JA fijo. La contradicción no requiere invariancia de JH, reductividad, isometría de J ni P=J*. El teorema2 está probado exactamente en el alcance incluso más general que una compresión ortogonal usual. No cubre mapas que cambian con n ni mapas no acotados.

## 5. Alcance final y paso siguiente

El resultado cierra el enlace ESPECÍFICO que intenta declarar V_n, D_n o sus reescalas por potencias como valores de un semigrupo C₀; para V_n también excluye compresiones fijas de un flujo unitario. No descarta familias continuas sin ley de flujo, compresiones unitarias de D_n ni otros observables o portadores. Tampoco afecta por sí mismo una prueba del nodo basada en otro mapa.

Los resultados auxiliares positivos007 permanecen válidos. Lo que se ha eliminado es una forma concreta de importarlos al análisis de Mellin. Para continuar deben precisarse operadores, dominio, convergencia y correspondencia gamma/peine/polar; no usar el teorema espectral de un generador de V_n cuya existencia acaba de refutarse.

**Objetivo íntegro D activo y OPEN. Resultado local de enlace aprobado, sin barrera global añadida.**

## 6. Extensión final: todo semigrupo C₀ y reescalas por potencias

**PROVED.** La exclusión no necesita uniformidad de normas fuera de los tiempos muestreados.

Si S(t) es C₀ y S(log n)=V_n, entonces para los n,m del argumento

    ||V_mA−V_nA||
      ≤||S(log n)||·||(S(log(m/n))−I)A||
      ≤||(S(log(m/n))−I)A||→0,

porque EN ESOS tiempos ||S(log n)||=||V_n||≤1, independientemente del comportamiento de S en otros tiempos. Así ningún semigrupo C₀ interpola V_n, sin hipótesis extra de contracción o cota uniforme global.

Más generalmente, si W(log n)=n^βV_n para un β real fijo, definir S(t)=e^(−βt)W(t). Es un semigrupo C₀ y S(log n)=V_n, imposible por la prueba anterior. En particular D_n=n^(−s/2)V_n tampoco admite tal interpolación C₀ exacta.

Esta extensión concierne semigrupos, cuya ley permitió factorizar la diferencia. La compresión de un grupo no hereda en general esa ley. El Teorema2 para compresiones UNITARIAS de V_n permanece probado, pero no se ha excluido con este argumento una compresión unitaria de D_n o de otra reescala: su distancia m,n puede tender a cero. No trasladar automáticamente la nueva exclusión de semigrupos a las compresiones reescaladas.

El alcance sigue siendo el enlace logarítmico directo de ESTA familia, no todas las representaciones posibles del nodo. **Extensión final aprobada; D continúa OPEN.**
