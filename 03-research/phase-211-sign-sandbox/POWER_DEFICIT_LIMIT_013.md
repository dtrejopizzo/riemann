# POWER_DEFICIT_LIMIT_013 — Límite exacto del transporte separable por déficit puntual en orden ocho

Estado: PROVED (NO-GO de una clase precisa de estimaciones). No es un contraejemplo al signo ni al transporte que conserve acoplamientos. Papers intactos.

## 1. Clase declarada y razón nueva

Consultados índice/grid/crucigrama por deficit limit, pointwise deficit, separable transport y discarded positive gain; revisados POWER_FOUR_GLOBAL_009, POWER_SIX_GLOBAL_011 y el criterio general de transporte. Esta nota identifica dónde deja de bastar el mecanismo que cerró los casos de dimensión pequeña. No reintenta ni clasifica otras rutas del paper.

Fije u=63/2, n=8. La clase considerada transporta desde la base confluente usando:

1. Una constante escalar b tal que AP[f0]>=b||f0||² para TODO numerador de grado menor que ocho.
2. Un objetivo c>=0.
3. La envolvente uniforme R/R0<=(1+x/u²)^8, x=tau².
4. Descarta toda ganancia en frecuencias m>=c y acota la pérdida negativa independientemente de la distribución espectral del numerador.
5. Acota la variación polar por una pérdida no negativa independiente.

La estimación de 011 usa además X,D con m>=c para x>=X y x(c-m)_+<=D, y el producto D K8, K8=[(1+X/u²)^8-1]/X. Se probará que NI optimizar X,D,c,b hasta sus valores verdaderos puede cerrar esta clase en orden ocho. No se excluyen estimaciones que retengan la ganancia positiva o la medida espectral racional.

## 2. Un vector racional da b<1/25

En la base Laguerre ortonormal de ocho polos u, tome

    v=(169,-310,405,-460,460,-405,310,-169).

Es un vector racional explícito de dimensión ocho. Su cociente arch+polar satisface estrictamente

    0<AP[v]/||v||²<1/25.                                 (B8)

El verificador tools/power_deficit_limit_013_verify.py calcula las ocho bandas Toeplitz mediante la fórmula Gamma+polar ya probada. Las derivadas psi^(j)(16), j<=7, se encierran sumando potencias racionales hasta 2000 y usando colas integrales. Gamma, pi y logaritmos usan los intervalos racionales de fixed_grid_003. La evaluación del vector es intervalar exacta, sin calcular autovalores numéricos para certificar.

Un único cálculo de descubrimiento de autovector produjo el vector anterior por redondeo; no interviene en la prueba final ni hubo un barrido de tasas. Por el principio variacional, cualquier b válido en el punto 1 de la clase declarada debe satisfacer b<1/25.

## 3. Una frecuencia exige pérdida mayor que 1/20

Se prueba exactamente

    m(4)<-2/5.                                           (M4)

Para verificarlo, use m(0)=-gamma-pi/2-3log2-logpi con los intervalos anteriores, y sume los primeros 32 términos positivos de digamma a x=16. La cola es a lo sumo

    (x/4)Σ_{k>=32}(k+1/4)^-3
       <=x/[8(125/4)^2].

El extremo superior racional obtenido es menor que -2/5. La comparación no depende de una gráfica ni de una aproximación redondeada de m.

Por otra parte la desigualdad racional

    (2/5)[(1+16/u²)^8-1]>1/20                            (LOSS)

es verificada exactamente. Para cualquier c>=0, (M4) implica que la menor constante de pérdida obtenible usando SOLAMENTE la envolvente puntual uniforme satisface

    sup_{x>=0}[(1+x/u²)^8-1](c-m(sqrt x))_+
       >(2/5)[(1+16/u²)^8-1]>1/20.

La envolvente es realmente el supremo puntual de R/R0 cuando todos los polos nuevos tienden a infinito. Por tanto no existe una envolvente puntual uniforme estrictamente menor que la usada aquí para todos los polos v_j>=u. No se afirma que un numerador racional de grado siete pueda concentrarse arbitrariamente en esa frecuencia: precisamente esa restricción de medida es información que la clase declarada descarta.

### Teorema para la pérdida puntual DIRECTA

Defina, sin separar el producto en dos constantes,

    L8(c)=sup_{x>=0}(c-m(sqrt x))_+[(1+x/u²)^8-1].

Para CUALQUIER c>=0, la evaluación x=16 ya prueba L8(c)>1/20. Combinando con (B8), para todo b válido y toda pérdida polar p_loss>=0,

    b-c-L8(c)-p_loss <1/25-1/20=-1/100.

Por tanto también queda excluida la estimación que optimiza directamente el producto puntual completo. El NO-GO no se limita a la separación D K8 ni a una partición particular de paneles. Es la sustitución de la integral negativa por un supremo puntual independiente del numerador, descartando la ganancia positiva, la que produce el obstáculo.

## 4. Imposibilidad de optimizar las constantes del criterio D K8

Toda elección válida X,D debe tener X>16, pues m(4)<0<=c. Además

    D>=16(c-m(4))>16*(2/5).

La convexidad de x->(1+x/u²)^8-1, que se anula en cero, da

    K8>=[(1+16/u²)^8-1]/16.

Por (LOSS), D K8>1/20. Incluso concediendo pérdida polar CERO, el margen máximo del criterio es

    b-c-D K8 <1/25-1/20=-1/100<0.

Por tanto el criterio no puede certificar orden ocho, aunque se optimicen todos los paneles, colas, cotas de gamma o constantes de la parte negativa. El mismo fracaso vale para la versión con la mejor pérdida puntual exacta en lugar del producto D K8.

## 5. Interpretación operativa y límites

Este resultado evita una prolongación indefinida de optimizaciones de constantes dentro de la misma estimación separable. En orden ocho debe retenerse alguna información descartada: ganancia en las frecuencias m>=c, distribución espectral del numerador, acoplamiento con el polar, filtros específicos de las tasas o contribución aritmética favorable.

NO se prueba AP[v]<0: el vector del certificado tiene AP POSITIVA. Tampoco se prueba W[v]<0, ni se excluye un transporte global de signo más fino. El fallo pertenece a la estimación que sustituye el coste por su peor valor puntual independientemente del vector.

Comando: `python3 03-research/phase-211-sign-sandbox/tools/power_deficit_limit_013_verify.py`. Verifica (B8), (M4) y (LOSS) mediante enteros y Fraction; no contiene funciones especiales numéricas, optimizadores ni coma flotante.
