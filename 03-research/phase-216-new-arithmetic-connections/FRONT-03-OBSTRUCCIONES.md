# Frente 03 — Coste integral de coherencia superior

Corte bibliográfico: **28/11/2026**. Trabajo independiente de RH y de la certificación de fase 215. Resultado inicial: controlar cup products no controla automáticamente el coste integral de obstrucciones ternarias. La conexión general Massey–Selmer–deformaciones ya tiene antecedentes; no la presentamos como nueva.

## 1. Filtro de novedad: conexiones que ya existen

| Propuesta demasiado amplia | Antecedente primario localizado |
|---|---|
| Relacionar Massey con Selmer | Ray–Sujatha, *Massey products and the Iwasawa theory of fine Selmer groups*, [arXiv:2508.17156v2](https://arxiv.org/abs/2508.17156v2), revisión 8/9/2026. El resumen relaciona operaciones superiores, invariante μ y deformaciones ordinarias. |
| Usar obstrucciones superiores para deformaciones de Galois | Galatius–Venkatesh, *Derived Galois deformation rings*, [arXiv:1608.07236](https://arxiv.org/abs/1608.07236). |
| Anulación de triples Massey de Galois definidos | Minač–Tân, *Triple Massey products vanish over all fields*, [arXiv:1412.7611](https://arxiv.org/abs/1412.7611). La anulación con coeficientes mod p no es un nuevo objetivo. |
| Conectar Hodge p-ádica y completaciones unipotentes | Ruth Wild, *p-adic Hodge theory of unipotent completions revisited*, [arXiv:2610.17169](https://arxiv.org/abs/2610.17169), 12/10/2026. Emplea la construcción bar y condiciones de Rham, semiestables y cristalinas. |
| Condiciones potencialmente semiestables en deformaciones derivadas | Douglas Molin, *On derived Galois deformation rings in characteristic 0 and a conjecture of Venkatesh*, [arXiv:2611.28988](https://arxiv.org/abs/2611.28988), 21/11/2026. |

Se inspeccionaron fichas y resúmenes primarios para identificar estas colisiones, no las demostraciones completas. Su alcance basta para rechazar las afirmaciones amplias de novedad; no basta para certificar que un presupuesto integral específico sea nuevo. Las consultas sin resultados no prueban ausencia de bibliografía.

La dirección delimitada que proponemos es **medir cuántas potencias de ℓ cuesta convertir compatibilidad racional de extensiones cristalinas en compatibilidad integral, manteniendo graduados y clases adyacentes prescritos**. Todavía requiere comparación completa con deformaciones integrales y modelos bar/sintómicos.

## 2. Modelo probado: cup nulo y coste ternario arbitrario

Sea O=Z_ℓ, con ℓ cualquier primo, y N≥1. Definimos la álgebra diferencial graduada

    A_N = exterior_O(a,b,c,u),
    |a|=|b|=|c|=|u|=1,
    da=db=0,   dc=ab,   du=ℓ^N ac.

Se usa el álgebra exterior, con cuadrados cero también para ℓ=2. El diferencial se extiende por Leibniz graduada. Es coherente: d²c=0 y d²u=−ℓ^N a²b=0, y preserva las relaciones exteriores.

**Proposición (PROVED en este modelo; prioridad no reivindicada).**

1. H¹(A_N)=O[a]⊕O[b], y todos los cup products H¹×H¹→H² son cero.
2. ⟨[a],[a],[b]⟩ está definido, tiene indeterminación cero y es ±[ac]. Esta clase tiene orden exactamente ℓ^N.
3. Después de tensorizar con Q_ℓ, ese triple contiene cero.
4. Escalar simultáneamente las tres entradas por ℓ^e hace que el triple contenga cero si y sólo si 3e≥N. El coste mínimo es ceil(N/3).

**Prueba.** Un elemento αa+βb+γc+δu es cerrado si γab+δℓ^N ac=0. La libertad del módulo implica γ=δ=0, y no hay fronteras en grado 1. El único producto potencialmente no nulo de a,b es ab=dc. Así todos sus cup products se anulan.

En grado 2 las bases son ab,ac,au,bc,bu,cu. Los cuatro primeros son cerrados y

    d(bu)=ℓ^N abc,     d(cu)=abu.

Estas imágenes son independientes en el módulo libre de grado 3. Las fronteras de grado 2 son O·ab+O·ℓ^N ac. Por tanto

    H²(A_N) = (O/ℓ^N)[ac] ⊕ O[au] ⊕ O[bc].

Escoger primitivas 0 para a² y c para ab da representante±ac del triple. Su indeterminación [a]H¹+H¹[b] es cero por el cálculo de cup products. Su orden es exactamente ℓ^N; racionalmente ac=d(ℓ^−N u).

Para las entradas escaladas, las primitivas 0 y ℓ^(2e)c producen representante±ℓ^(3e)ac. La indeterminación sigue siendo cero. Esta clase se anula exactamente cuando 3e≥N.

**Consecuencia.** En álgebras diferenciales integrales generales no hay una cota del coste ternario que dependa sólo del anulador de los cup products y del número de generadores. Aquí el coste binario es cero y siempre hay cuatro generadores, mientras el coste ternario crece sin cota. Incluso existe solución racional ternaria.

La existencia de cup nulo y Massey no nulo es clásica; el modelo explicita la pérdida integral y no se reivindica como descubrimiento nuevo. **No se afirma que A_N provenga de un grupo de Galois o una representación cristalina.** Por eso no contradice los teoremas de anulación mod p para grupos de Galois absolutos. Tampoco refuta 56: muestra que prolongar sus cotas binarias a obstrucciones superiores exige un argumento adicional.

El script [check_massey_dga.py](experiments/check_massey_dga.py) comprueba signos, d² y los exponentes en ejemplos. La prueba para todo N es la anterior.

## 3. La cuestión de coherencia

Tres clases x,y,z de grado 1 requieren primero primitivas

    du=xy,     dv=yz.

Después deben elegirse de modo que exista w con

    dw=xv+uz.

El lado derecho es cerrado porque d(xv+uz)=−xyz+xyz=0. La primera pregunta es binaria; la segunda exige compatibilidad de dos elecciones. Cambiar u,v modifica la obstrucción por la indeterminación de Massey. Matar los dos cups no proporciona w ni controla sus denominadores.

Ésta es la interpretación conocida mediante matrices triangulares de tamaño 4: primera superdiagonal x,y,z, segunda superdiagonal las primitivas, esquina final la compatibilidad ternaria. La variable que proponemos estudiar es el **coste integral de completar ese sistema bajo condiciones cristalinas**, no la mera existencia racional.

## 4. Un objeto candidato sin escoger un modelo de cochains

Fijar una extensión finita K/Q_ℓ, un anillo de coeficientes O con uniformizador π, cuatro retículos T0,T1,T2,T3 de G_K cuyos Vi=Ti⊗Frac(O) son cristalinos, y clases

    ξ_i ∈ H¹(K,Hom_O(T_(i+1),T_i)),   i=0,1,2,

cuyas imágenes racionales pertenecen a H¹_f. Se fijan las identificaciones de los graduados con los Ti.

Para e≥0 pedir una representación integral M con filtración saturada de cuatro pasos, graduados Ti, representación racional cristalina y clases adyacentes π^e ξ_i. Definir

    c_cris(T0,T1,T2,T3; ξ0,ξ1,ξ2)
      = menor e que permite esa realización,

con valor ∞ si no existe. «Saturada» significa que los cocientes son libres sobre O. Se minimiza sobre realizaciones, no sobre una elección arbitraria de primitivas. La definición es invariante bajo isomorfismos de los datos graduados.

No se identifica automáticamente este número con un Massey en un supuesto sub-DGA «cristalino»: para eso hay que construir o citar un modelo derivado compatible con la condición local de Bloch–Kato. Esa identificación es una obligación de investigación.

**Lema de finitud (PROVED bajo hipótesis explícita).** Si existe una representación cristalina racional filtrada con esos graduados racionales y clases adyacentes racionales, entonces c_cris es finito.

**Prueba.** Elegir desdoblamiento vectorial y bases de los Ti. Mediante cambios racionales de desdoblamiento en la primera superdiagonal se puede hacer que los cociclos adyacentes sean los representantes integrales elegidos de ξ_i: las clases racionales coinciden, por lo que sus diferencias son cobordes racionales. Estos cambios sólo alteran además los bloques superiores.

Las matrices de G_K son triangulares superiores por bloques. Por continuidad y compacidad de G_K, sus bloques superiores tienen denominadores uniformemente acotados. Conjugar por D_e=diag(1,π^e,π^(2e),π^(3e)), como escalares sobre los bloques, multiplica el bloque (i,j), i<j, por π^((j−i)e) en D_e^−1ρD_e. Para e suficientemente grande todas las entradas son integrales. Los bloques diagonales preservan los Ti y las inversas son integrales por triangularidad. El retículo directo es estable, su filtración estándar es saturada y las clases adyacentes son exactamente π^e ξ_i. La representación racional es isomorfa a la inicial, luego sigue siendo cristalina.

El lema no proporciona un presupuesto uniforme en los pesos. El coste depende inicialmente de una realización racional y sus denominadores; ésta es precisamente la dificultad cuantitativa.

## 5. Preguntas para desarrollar matemática nueva

**Q1 — pérdida binaria frente a superior.** Bajo hipótesis explícitas sobre K, rangos y pesos Hodge–Tate, ¿hay una cota de c_cris en términos de los exponentes binarios de 56 más un invariante de saturación ternaria? Si los pesos y cups no bastan, construir una familia cristalina que lo demuestre y localizar el dato adicional necesario. No se conjetura sin evidencia una cota sólo en los pesos.

**Q2 — potencias y límites.** ¿Cómo se relaciona c_cris con realizaciones módulo π^n que proceden de un mismo retículo cristalino? La existencia por separado para cada n no sustituye compatibilidad de reducción. El resultado debe explicar el paso al límite y su coste uniforme.

**Q3 — longitud de la filtración.** Para cinco o más graduados, ¿qué presupuesto controla la realización integral cuando desaparecen todas las obstrucciones racionales? La suma de anuladores cup no basta por motivos formales; hay que controlar elecciones y operaciones superiores.

**Q4 — aplicación distinta de RH.** En una familia de deformaciones ordinarias o Selmer, ¿una cota de c_cris limita el índice entre extensiones racionalmente realizables y realizaciones integrales? La relación con Massey ya existe: la contribución potencial sería una desigualdad explícita nueva, comparada con Ray–Sujatha y la teoría derivada.

## 6. Primer ensayo aritmético y criterio de éxito

Comenzar con cuatro caracteres cristalinos de rango 1 sobre K fijo y pesos fijos. Elegir clases en los H¹_f pertinentes, verificando que esos grupos no sean nulos. Separar imposibilidad racional, posibilidad racional con coste cero y posibilidad racional con coste positivo. Calcular extensiones, retículos y compatibilidad de longitud 4 en una categoría integral adecuada al rango elegido.

Un resultado útil sería una fórmula exacta de c_cris para una familia no trivial o un contraejemplo aritmético a una cota sólo binaria. Después hay que comparar esa fórmula con antecedentes completos. Hasta entonces el estado es **objeto propuesto, lema de finitud y modelo de obstrucción probado**, no un nuevo teorema de Hodge p-ádica.

## 7. Dictamen de novedad

- **EXISTENTE/CITED:** Massey–Galois, Massey–Selmer, deformaciones derivadas y Hodge unipotente.
- **PROVED AQUÍ, sin reivindicar prioridad:** modelo A_N y coste ceil(N/3); finitud condicional por conjugación diagonal.
- **CANDIDATO:** presupuesto integral de realizaciones cristalinas filtradas con graduados fijados, comparando pérdidas binarias y superiores.
- **OPEN:** realización aritmética de coste superior no controlado por el dato binario, cotas uniformes útiles, identificación con modelos derivados integrales y aplicaciones nuevas.
- **PRIORIDAD NO ESTABLECIDA:** las búsquedas no certifican que la definición o pregunta no aparezca con otro lenguaje en la bibliografía hasta 28/11/2026.

Registro de consultas: [front03-consultas.json](bibliography/front03-consultas.json).
