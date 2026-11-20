# POWER_HIGHPASS_AUDIT_015 — Revisión de positividad eventual uniforme y mezcla completa

Estado: PROVED. Revisados íntegramente POWER_HIGHPASS_015.md y POWER_GEOMETRIC_TRANSFER_015.md. No se requiere cómputo numérico para sus demostraciones. Papers intactos.

## 1. Gram reescalada y uniformidad en todos los coeficientes

La sustitución tau=sqrt(k)x y b_j=a_j k^(j/2) produce exactamente el factor k^(N-1/2) delante de la norma². Ponderar por e^(eta y) sustituye s por-eta+i tau. Las dos constantes son c_eta=(u-eta)^2 y d_eta=c_eta-eta²=u(u-2eta)>0, con0<=eta<u/2. Las potencias de k, el polinomio trasladado y todos los factores de la fórmula GRAM son correctos.

Para justificar uniformidad, cada una de las N² entradas se domina independientemente de los coeficientes. Cerca de x0, escribir y=x²+c_eta/k da cociente^k<exp(-d_eta/y), y el producto exp(-d_eta/y)y^-N está acotado para y>0. Los monomios trasladados están uniformemente acotados en|x|<=1. En|x|>=1, cada entrada está dominada por C|x|^(i+j-2N), cuyo exponente es<=-2. Esto demuestra convergencia dominada, también en L¹ de las densidades matriciales.

La matriz límite es definida positiva porque su peso es estrictamente positivo fuera de0 y un polinomio no nulo no se anula casi en todas partes. En dimensión N fija, las matrices convergen en norma y sus eigenvalores mínimo/máximo quedan uniformemente acotados con el signo pertinente. Como b depende invertiblemente de a para cada k, esto prueba uniformidad en TODO numerador, incluso si sus coeficientes dependen de k o se anula el coeficiente de mayor grado. No se usó un argumento sólo de término dominante para esa parte uniforme.

## 2. Forma arquimediana

El factor m(sqrt(k)x)-.5logk converge a log(|x|/(2pi)). El bound global por log(2+|tau|) y la comparabilidad entre2/sqrt(k)+|x| y sqrt(x²+u²/k) producen C+|log y| cerca del origen. Su producto por exp(-u²/y)y^-N sigue acotado. Fuera de|x|<=1, el majorante adicional1+log|x| es integrable contra|x|^-2. Así la matriz arquimediana, después de restar .5logk veces la matriz de norma, tiene límite finito en norma. Compararla con el mínimo positivo de G0 demuestra ARCH/||f||²>=.5logk-C_N uniformemente.

Este paso no supone que la medida espectral de un numerador fijo controle los numeradores variables: la comparación matricial es lo que proporciona esa uniformidad.

## 3. Peine completo y polar

La correlación en un tiempo t>0 fijo se obtiene de las N² densidades de Fourier reescaladas. Se resta primero su límite en L¹; sólo después se usa Riemann--Lebesgue a frecuencia sqrt(k)t sobre cada densidad límite fija. La finitud de N² y el mínimo positivo de G0 justifican la convergencia uniforme en los numeradores del cociente de correlaciones. No se aplica RL directamente a una sucesión móvil sin ese control.

La matriz límite ponderada con1/2<eta<u/2 da un cociente de norma ponderada uniformemente acotado. Cauchy--Schwarz desplazado produce un majorante Cq^-eta para las correlaciones normalizadas. La serie2sum Lambda(q)q^(-eta-1/2) converge absolutamente (basta Lambda<=logq). Al separar un segmento finito y la cola dominada, se obtiene convergencia a0 del peine COMPLETO, uniformemente en P. No se truncó una contribución sin estimarla.

El polar tiene el factor exacto[-1/(4u²-1)]^k. Las evaluaciones iniciales del numerador son uniformemente acotadas en b y la norma² tiene cota inferior c_N k^(1/2-N)||b||². Por tanto el cociente polar es<=C_N k^(N-1/2)(4u²-1)^-k y tiende a0 porque u>1. Los signos alternados no son necesarios para esta cota.

Queda probado el teorema EVENTUAL: para cada N,u fijos, existe K_N independiente de P tal que W>0 sobre TODOS los subespacios Q^k V_N con k>=K_N.

## 4. Constante asintótica de numerador fijo

Para gradoD fijo, r=N-D, la integral límite sobre R es

    integral |x|^-2r exp(-u²/x²)dx=u^(1-2r)Gamma(r-1/2).

El factor Parseval1/(2pi), la escala k^(1/2-r) y |a_D|² del memo son correctos. La misma sustitución t=u²/x² da Elog|x|=logu-.5psi(r-.5); el símbolo añade-log(2pi). El peine y polar normalizados tienden a0, así ASYM es la asintótica de W completo. La razón ponderada[u/(u-2eta)]^(r-.5) también coincide con el cociente de integrales límite.

## 5. Revisión del memo de mezcla geométrica final

POWER_GEOMETRIC_TRANSFER_015 fue leído en su versión completa. Sus índices residuales coinciden con POWER_MIXTURE_AUDIT_015: el resto es Q^(K+1)fv y su denominador tiene exponente N+K en s+u, además de s+v. El espacio X=H^t(R)+L² ponderado, aunque más débil que la norma ponderadaH^s propuesta en esa auditoría, es suficiente y sus dos contracciones se verifican directamente por los multiplicadores en las rectas correspondientes.

La continuidad de W controla arch, momentos y todo el peine con sus constantes correctas. La convergencia fuerte elimina el resto y la cota uniforme de las formas prueba convergencia absoluta de la mezcla. Los pesos normalizados incorporan ||h_k||² y suman1 por la identidad separada de norma; no se confunden funciones y mezclas de formas.

En el producto de filtros todos los H_j son contracciones de X y conmutan con Q. Esto justifica Fubini absoluto y los pesos homogéneos positivos w_k del memo. La suma de pesos es1, y las normas adicionales son las correctas para una mezcla de Rayleigh.

## 6. Alcance operativo

Se obtienen DOS herramientas probadas: la mezcla completa exacta y una cola high-pass completa uniformemente positiva para cada N fijo. Juntas reducen una condición SUFICIENTE de transporte para ese N al signo de un segmento finito de bloques iniciales. No se proporciona todavía un extremo efectivo de ese segmento ni su signo en todos los N. Una mezcla puede contener términos iniciales negativos; la positividad eventual de sus términos no prueba que la suma sea no negativa. Nada en esta aprobación cierra el signo de todas las ventanas.
