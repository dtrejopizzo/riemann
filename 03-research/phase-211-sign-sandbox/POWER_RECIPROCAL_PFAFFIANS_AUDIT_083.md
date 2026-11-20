# POWER_RECIPROCAL_PFAFFIANS_AUDIT_083 — Auditoría independiente

Estado: **APROBADO / PROVED como identidad algebraica en todos los órdenes.** Fuente `POWER_RECIPROCAL_PFAFFIANS_083.md`, lectura completa. Auditor mapa; root aprobó independientemente. Papers intactos.

## Verificaciones de signos y factores

Con D=diag(u),E=diag(R),A=A_R y T=EKE, ambas identidades DISPLACEMENT se verifican entrada por entrada, incluidas diagonales. UPDATE tiene el signo correcto con Pf([[0,a],[-a,0]])=a: la forma de rango2 es descomponible, el Pfaffiano es afín en su parámetro y la derivada en0 del cuadrado fija el coeficiente Pf(V)b^tV^−1a.

En tamaño par, el determinante de DA+re^t y UPDATE para DAD+ru^t−ur^t contienen exactamente el mismo factor1+e^tA^−1D^−1r. Las congruencias pagan detD y productoR una sola vez. Resulta detK=Pf(A_R)Pf(A_S)/productoR. La extensión desde A invertible es legítima: para nodos distintos, R_i=u_i produce la matriz de Schur invertible. Su fórmula clásica es la Proposición2.2, ecuación(2.7), de Okada, https://arxiv.org/html/1706.01029; cotejada directamente. No se presenta esa fórmula clásica como un resultado original. Tras despejar denominadores la extensión a nodos coincidentes es continua.

En tamaño impar, los cofactores v_i=(−1)^(i+1)Pf(A sin i) satisfacen Av=0 y el borde FINAL tiene Pf=b^tv. adj(A)=vv^t se extiende correctamente al rango menor; n=1 usa Pfvacía=1. adj(DA)=detD·adj(A)D^−1 produce ODD-DET con el orden correcto de los factores. La congruencia Q=[[I,u],[0,1]] suma ru^t−ur^t, por lo que BORDER no invierte signo. Los bordes r=Ee y D^−1r pagan respectivamente productoR y detD. De nuevo no queda ningún producto u extra en detK. Esto cubre también matrices singulares.

Ambos factores cambian por el mismo signo al permutar nodos, de modo que el producto final es invariante. n=1,2,3 recuperan las normalizaciones previas; no se usan esos casos para extrapolar la prueba general.

## Antecedentes y alcance

Consultados los tres registros y003/074/079/081/082. Se acepta la atribución explícita a álgebra clásica de Pfaffianos, Cayley/Knuth y Cauchy–Schur; no se reclama prioridad mundial. La especialización nueva respecto del corpus organiza el determinante del kernel completo mediante A_R,A_S en todos los tamaños, sin quitar aritmética ni componentes.

Esto es una IDENTIDAD, no una desigualdad firmada nueva para la Phi real. Para PSD deben controlarse los productos de Pfaffianos de TODOS los subconjuntos principales; un determinante total positivo no basta. Los signos de los Pfaffianos en órdenes arbitrarios no están probados. No hay cobertura W nueva, orden4 resuelto ni ventanaT nueva; el objetivo global sigue OPEN.


## Apéndice clásico añadido — revisión posterior

Leído íntegro el apéndice de interpolación/Rolle/Hankel. La especialización par de Ishikawa–Okada–Tagawa–Zeng Theorem1.1(b) y el límite impar con fultimo=uultimo conservan sigma_k y el borde final de unos. El orden dominante2k−1 y el cofactor final positivo justifican el límite. La identidad clásica fue cotejada en la primaria enlazada; no se reclama novedad.

La jerarquía Dk,j≠0 asegura Chebyshev extendido mediante Rolle ponderado, con regularidadC^(2k−1) suficiente. Derivar k veces el sistema polinomial elimina la primera mitad y da las cuentas de ceros par/impar. La traslación de base y la inversión de columnas producen exactamente TAYLOR-HANKEL y sus factoriales. La condición adicional de momentos positivos desplazados de mu_m=(−1)^m a_(m+1) da los signos indicados por factorización de filas/columnas. Es sólo una condición suficiente NO verificada para los cocientes reales R,S; no se hereda de la positividad deJ/K. No hay descarga de Pfaffianos superiores.
