# POWER_TWO_COPY_SCOPE_AUDIT_074

Estado: **APROBADO** POWER_TWO_COPY_SCOPE_074 tras lectura completa de siete secciones y del verificador. Reproducción independiente: **exit0/PASS**. Contraejemplo auxiliar a una implicación genérica, no al kernelPhi real ni aW. Papers intactos.

Antecedentes cotejados: índice/grid/crucigrama, SCHUR003 y THETA_TWO_COPY073. Los contraejemplos escalares anteriores no verificaban toda la hipótesis de potencial073. La diferencia declarada es legítima: conservar esa hipótesis, incluso con un potencial polinómico fuertemente convexo, y refutar su promoción automática a tres generadores.

## Jet inicial y prueba de x^6

La expansión de(M(u)+M(v))/(u+v) da la matriz de coeficientes en grados0,1,2 escrita en la fuente. Su determinante es(−beta)(alpha gamma−beta²), y la menor suma de grados en filas y columnas produce epsilon^6 por Vandermonde². La paridad elimina orden7. Si kappa4<0, la condición del signo principal es exactamente3kappa2kappa6−10kappa4²; los factores6 y120 están correctamente incluidos.

ParaV=x^6, los momentosGamma y la reflexión danm4=2a²,m6=1/6, kappa4=−a² y kappa6=1/6. El integral de Taylor inferior sobre[0,1] pruebaGamma(1/6)>3sqrtpi; la comparación racionalr²>11/14>pi/4 es correcta. Por tanto a<1/3 y el jet es positivo. Se mantiene explícitamente como un test que NO dio el contraejemplo, sin atribuirle un signo negativo inexistente.

## Potencial, modos y medias

V=A[x²/2+x^(2p)/(2p·2^(2p−2))], con los enteros declarados, es par analítico, superlineal y cumpleV″>=A yV‴>0 en todo x>0. No se cambiaV entre los tres camposAi.

Los modos son las raíces únicas dev′(x)=i. Las comparaciones en1−eta,1,2−eta,2 son estrictas y válidas:2p−2>15,2^15>20000, (p−1)eta>49 yexp49>49^4/24>40000. En particular2exp(−49)<eta, no sólo una aproximación decimal. Los modos2 y3 quedan ambos en(2−eta,2), y el primero en(1−eta,1).

La integración por partes de(x−xi) por la densidad inclinada da exactamenteE[(X−xi)(v′(X)−i)]=1/A. Los bordes y todos los términos son integrables por el potencial polinómico par. La convexidadv″>=1 produce el bound cuadrático global y el error de media<=1/sqrtA=eta. No se utiliza un desarrollo asintótico de Laplace. Así las tres medias distan menos de1/10000 de(1,2,2).

## Matriz negativa y clase exacta

En la matriz rescaladaB=A K, el denominador es i+j; por ello el error de cada entrada es<1/10000. Verificado exactamente el vector(40,−40,3): su energía enB0 es−6 y la pérdida máxima de error es6889/10000<1. Se obtiene el bound negativo estricto−53111/10000 y su división porA. Las diagonales son positivas porque las medias son positivas. El verificadorFraction reproduce esas comparaciones y terminóPASS independientemente.

El teorema073 sí se aplica aESTEV: todos sus pares de nodos positivos son definidos positivos y su media inclinada es estrictamente cóncava. El bloque3x3 negativo, por tanto, refuta exactamente la implicación «hipótesis de potencial073 ⇒ todos los bloques3x3 positivos». No refuta073, la positividad de TODOS los pares del dato real ni la posibilidad de explotar una estructura adicional específica dePhi.

No se evalúa la formaW, no se modifica su aritmética y no se obtiene una imposibilidad global. El potencial del contraejemplo es un auxiliar explícito que delimita el alcance de la herramienta de dos copias; no sustituye al kerneltheta del proyecto.
