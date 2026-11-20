# POWER_DIMENSIONAL_AUDIT_051

Estado: **APROBADO** POWER_DIMENSIONAL_CUTOFF_051 como bound de momento y ARCH, no de W. Papers intactos.

Cotejados los antecedentes de índice/crucigrama y HIGHPASS015, JOINT_SCALE016, CENTERED_CUTOFF049 y FULL_TWELVE050. La diferencia respecto de la eventualidad a dimensión fija es un corte explícito lineal en la dimensión, uniforme en TODOS los numeradores. No se presenta el cambio de coordenadas anterior como herramienta nueva.

Revisados el centrado y ambos casos de paridad: para d=n−1, el sector polinómico puro tiene grado<=d y peso j−1/2, y el sector con cos x tiene grado<=d−1 y peso j+1/2. Las paridades se intercambian al cambiar n, pero los cruces siempre son impares y se anulan incluso con coeficientes complejos. El segundo sector se omite en n=1. Las condiciones de borde a>0 se cumplen para j>=1; el momento inverso es integrable. La energía polinómica049 da d(d+2j) como majorante común. La raíz positiva y la mezcla de razones justifican GENERAL y ROOT; no se usa sólo densidad L² o un vector diagonal.

Los coeficientes normalizados decrecen con j. Verificada algebraicamente la expansión en j0=7n/6: el margen cuadrático es(49n²+10878n+7569)/3600>0 y el lado no elevado al cuadrado también es positivo. Por tanto j>=ceil(7n/6) implica r<49/20, momento inverso<1/405 y ARCH>859/800. El caso n=1 también está incluido.

Revisada la raíz general T(n,b): al poner t=2j−1, la desigualdad cuadrática tiene raíz mayor[(2n−1)+2sqrt((1+b)n(n−1))]/b. J=floor(T)+1 la supera estrictamente y satisface además bt−1>0. El margen ARCH-b tiene las orientaciones correctas por Jensen y Cauchy. Para la elección b_h se exige explícitamente h>=0; entonces sqrt(b_h)/u<1/8 y b_h/(2u²)<1/128, mientras el logaritmo supera h+1. Esto demuestra el margen ARCH pedido, sin afirmar margen completo.

## Corrección algebraica previa a integración

La primera lectura dejó pasar una errata del factor energético del segundo sector. Root la detectó y corrigió en la fuente: Degree=d−1 y a=j+1/2 dan exactamente(d−1)(d+2j+1), no(d−1)(d+2j). Revisada la corrección escrita: d(d+2j)−(d−1)(d+2j+1)=2j+1>0. El mismo majorante común sigue siendo válido; GENERAL, ROOT y todos los cortes y márgenes permanecen sin cambios. La aprobación se refiere a esta versión corregida.

## Obligaciones que permanecen

El segmento inicial dependiente de n, el polar y el peine completo no están resueltos. No puede extenderse literalmente la conclusión parcial E2 de050 a toda órbita y toda dimensión: PRIME_TRANSFER014 da un falsificador exacto de esa hipótesis. Allí n=2^17, F=(s²−1/4)/(s+u)^n pertenece a V_n y la integral D prueba E2[QF]<0. Esto no refuta el corte j>=J(n), ni una hipótesis con más contactos, ni W completo. Impide únicamente declarar positivos todos los segmentos iniciales de E2 en todo orden.

La revisión complementaria de casos sobre trece polos generales no aportó una desigualdad nueva: ZERO13 controla un subespacio de codimensión uno, pero la positividad de un vector complementario no controla su acoplamiento de Schur. Los antecedentes de Schur del índice ya contienen esta obligación. No se registra un nuevo NO-GO global ni una ampliación de cobertura W por esa observación.
