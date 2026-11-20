# POWER_DEFICIT_AUDIT_013 — Revisión del límite de la envolvente puntual en ocho polos

Estado: PROVED para la clase declarada. Revisados POWER_DEFICIT_LIMIT_013.md y tools/power_deficit_limit_013_verify.py; ejecución independiente con PASS. Papers intactos.

## 1. Dos certificados exactos

La evaluación del vector racional de ocho coordenadas usa las bandas AP previamente derivadas, ahora con psi^(j)(16) hasta j7. Las sumas16..2000 y las integrales de cola desde2001/2000 tienen orientación correcta. La suma intervalar de TODAS las parejas v_i v_j conserva las correlaciones de intervalo de manera conservadora, y certifica0<Rayleigh<1/25. No se requiere ni se calcula una eigenenergía numérica para esta cota. Cualquier b válido para todo el bloque necesariamente satisface b<=lambda_min<=ese Rayleigh<1/25.

La cota de m(4) suma exactamente k0..31 de la serie positiva y acota los omitidos usando x/[4a_k³]. Para k>=32, comparar la suma con integral desde31 de(x+1/4)^-3 produce exactamente el término x/[8(125/4)^2]. El extremo superior mzero.hi es el pertinente. El resultado m(4)<-2/5 y la comparación racional(2/5)[(1+16/u²)^8-1]>1/20 fueron reejecutados y son correctos.

## 2. Fallo de la mejor pérdida puntual DIRECTA

Para cualquier c>=0, evaluar en x16 ya da

    L8(c):=sup_(x>=0)(c-m(sqrtx))_+[(1+x/u²)^8-1]>1/20.

Esto usa exactamente la envolvente uniforme del filtro; puede aproximarse puntualmente al hacer todas las tasas nuevas arbitrariamente grandes. No se presupone que un numerador de grado siete pueda concentrar toda su probabilidad en x16. El coste L8 se refiere a la clase que DESCARTA esa restricción espectral y sustituye la pérdida por su supremo puntual independientemente del vector.

Como b<1/25, aun concediendo coste polar cero y c0, b-c-L8(c)<1/25-1/20<0. Por ello falla no sólo separar máximos como D*K, sino también emplear la mejor envolvente puntual directa de esta clase. La restricción 'descarta la ganancia positiva' es decisiva para identificar qué se ha excluido.

## 3. Caso D*K y alcance

Si además se usan X,D, cualquier X válido debe ser>16 y D>16*(2/5). La monotonía de[(1+x/u²)^8-1]/x produce DK8>1/20. Esta versión particular del fallo es coherente con §2; mejorar los paneles o las constantes no la supera.

El resultado no proporciona un vector AP negativo: el test usado tiene AP POSITIVA. Tampoco demuestra W negativo, ni que sea imposible un teorema de ocho polos. Quedan fuera de la clase las estimaciones que conserven la medida racional, las ganancias positivas, el acoplamiento polar o los filtros específicos. La auditoría aprueba exactamente esa delimitación y ninguna conclusión global mayor.
