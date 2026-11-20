# AUDIT_001 — Revisión hostil de la especificación O1

2026-10-18. Revisor independiente. Fila D independiente. Matemática pura.
Estado: revisión inicial en §§1–7; revisión final del constructor y de la síntesis en §8. Completada.

## 1. Corpus consultado y decisión inicial

Leídos las reglas del proyecto, README209, CONTROL_001, README208; índice README (familias y entradas 204–207), 06_OPEN_RESIDUES (W₂ y hojas BR), búsquedas dirigidas en grid maestro y crucigrama; CELL_001 §8–10 y AUDIT_207_001 §B; P1_BBSTAR_001; SPEC_SIGN_OBJECT_005; R185_005B §1–3; BARRIER_X_001 §3 y corrección AUDIT_197_HOSTILE_3 §c; Paper 47 main.tex def:PD, thm:sos y rem:sosatoms.

**ARGUED: especificación admisible como examen de O1 ya abierto.** La razón nueva escrita es concreta: núcleo efectivo no reducible a multiplicador más reflexión funcional, sin colapso a peso del producto mn. No equivale a poseer un candidato ni un lema nuevo. Las puertas del README evitan repetir Gonek, Gram y factorización de la forma objetivo.

## 2. thm:sos: alcance exacto

**CITED / verificado contra el enunciado.** thm:sos exige simultáneamente una identidad puntual

    Σ_i |D_i(t)|² = μ₀ − Σ_n v_n cos(t log n)

más positividad de la forma arquimediana menos μ₀ en P_T. La contradicción para T≥½log3 compara μ₀≥Σv_n≥0.9802 con fondo arquimediano ≤0.311. No usa las frecuencias concretas del D_i; la extensión a frecuencias reales está incorporada al paper.

No es un teorema contra toda identidad de normas. P1_BBSTAR distingue: ampliar espacio y restringir B*B da de inmediato (Bι)*(Bι); demostrar que existe alguna raíz es reformular el objetivo, mientras construir una raíz de una clase especificada puede tener contenido. Con parte positiva definida libre y representación multiplicadora se llega a def:PD, no a una imposibilidad de existencia de certificados. Una construcción explícita en esa clase seguiría necesitando probar el certificado: clasificarlo no lo refuta.

**Puerta aprobada**, con esta cautela: estar fuera de thm:sos no implica estar fuera de def:PD ni aportar signo. Un B*B genérico positivo para todo dato no pasa por ello la puerta aritmética; su enlace con Q_T es toda la dificultad. No convertir el mero lema de norma en el hito sustantivo.

## 3. Tres nociones distintas de dos variables

1. Kernel efectivo K(t,t′) de un operador en alturas de Mellin.
2. Forma diagonal de dos variables W₂ de P36-4 registrada en el índice.
3. W₂=𝔄−Q^hyp−𝓡−C̄ de R185_005B: conjunto relajado de restos en el esquema (M2).

La coincidencia de notación o número de variables no produce traducción entre ellos. **CITED:** BR sólo se aplica después de dar tests admisibles, identidad de colas, sentencia aritmética de la clase 𝔐 y modelo de restos. En (M2) necesita cotas inferiores por coordenada o el régimen ba/sup indicado. La hoja ρ1‴ requiere demostrar precisamente el fallo pertinente de esas hipótesis; no es una salida automática para núcleos integrales. Las sentencias conjuntas (Λ,Γ) y ciertos objetos operatoriales figuran fuera de 𝔐; eso tampoco les da positividad.

**Puerta aprobada.** Ningún candidato está todavía traducido a ese esquema.

## 4. Paridad y Gonek

**CITED:** la paridad de Kronecker preserva defectos determinados por distribución de valores de cocientes FE bajo rotaciones de toro. Su consecuencia de antipodalidad exige clase admisible cerrada bajo el giro de signos. AUDIT_197_HOSTILE_3 corrige expresamente que la clase entera 𝓘 del memo original no lo es. No citar esa obstrucción como teorema para todo kernel. Un kernel con correlaciones entre alturas puede perder la invariancia; debe calcularse, no suponerse.

**CITED:** Gonek en CELL_001 calcula la componente escalar de J mediante fase estacionaria y da peso w(2πmn) más error. No caracteriza toda forma de peso ½: tal lectura sería demasiado amplia. Con a=Λ, Λ*Λ no es Λ·d. El signo de su término principal para w≥0 es heredado por datos no negativos y no paga el error; w indefinida no tiene signo establecido. Para un nuevo K hacen falta fórmula exacta, dominio y restos, no sólo que la expresión inicial use dos alturas.

## 5. Borrado: prueba lógica exigible

Definir b^(p)(p^k)=0, b^(p)(n)=Λ(n) en el resto. Si p<e^(2T), hay dato interior cambiado; en n=p falla Λ*1=log por log p. El fallo es identificación, no signo.

**PROVED, lógica elemental:** para refutar una deducción por transferencia hacen falta todas sus premisas heredadas y un dato que viole la conclusión. Por tanto no es necesario que un candidato se vuelva negativo al borrar cualquier primo interior, ni que toda premisa falle para todo p,T. Basta localizar, para los borrados relevantes a la deducción propuesta, la hipótesis aritmética exacta que evita la transferencia. Una norma genérica puede seguir positiva tras el borrado y acompañarse de una identidad específica que falle: esa posibilidad es legítima, pero el trabajo se concentra en demostrar dicha identidad sin asumir el signo objetivo.

Pedir fallo para TODO primo interior es una condición de diseño más fuerte, no una necesidad lógica universal. No exigirlo como teorema de barrera. Para p>e^(2T) el objetivo es idéntico en esa ventana; ninguna distinción local es exigible. Las premisas globales sí pueden distinguir esos datos sin contradicción.

## 6. CONTROL_001

**PROVED:** con Fourier unitaria, la proyección a transformadas de L²([-T,T]) tiene núcleo sinc sin(T(t−u))/(π(t−u)). Para a∈L∞ real el integral del producto de sincs con a converge absolutamente por Cauchy–Schwarz, y P_T M_a P_T restringe a la misma forma multiplicadora en su imagen. También en el subespacio polar. La extensión al símbolo no acotado está prudentemente formulada como restricción de forma y no reclama el integral.

El control es correcto y útil. La condición que excluye es «novedad por escribir un kernel»; no demuestra que toda forma no local sea multiplicadora ni que la falta de conmutación ambiente desaparezca siempre tras la restricción.

## 7. Veredicto inicial

README209 y CONTROL_001: **aprobados con las precisiones de §§2–5**. O1 sigue OPEN. No se ha obtenido un mecanismo de signo ni un nuevo NO-GO. La revisión final deberá comprobar en el candidato qué hipótesis de SOS, PD, BR o paridad aplica realmente; no inferirlo de su nombre. Dominio completo, enlace exacto, restos, ventana continua y sector quedan pendientes hasta que haya construcción.

## 8. Revisión final de CONSTRUCTOR_001 y SYNTHESIS

**Veredicto: aprobado, PROVED para la clase declarada; NO CANDIDATE para O1.** No se obtuvo signo del nodo. La síntesis conserva correctamente este límite.

- **§4 / J. PROVED.** En intervalo simétrico, |χ_t|=1 y χ_tχ_−t=1 hacen J unitario e involutivo, luego autoadjunto. La extensión libre desde (0,A) mediante f(−t)=±χ_−t f(t) verifica Jf=±f y ambos autoespacios infinitos.
- **Lema 4.1. PROVED.** La representación por fibras {t,−t} convierte el álgebra en multiplicadores matriciales. En medida no atómica un multiplicador matricial no nulo no es compacto: elegir columna no nula en conjunto de medida positiva y particionarlo da imágenes ortogonales uniformemente alejadas de cero. Vale para clausura en norma, como dice el memo. No se afirma clausura fuerte, que es otra operación.
- **Teorema 4.2. PROVED.** Aproximación compacta por rango finito, intersección de V₋ con ker R y L de codimensión finita, y estimación −1+ε son exactas. E sigue siendo cerrado infinito-dimensional. No se necesitan vectores ortonormales dentro del ideal, ni información aritmética. El signo negativo es inequívoco.
- **Lema 5.1. PROVED.** La transformada del ortogonal h tiene crecimiento exponencial lineal en radio. Jensen con centro no nulo acota el número de ceros por O(r), incompatible con los ≥exp(r/3) puntos log n en el disco interior para r grande. La unicidad de Fourier da h=0. P_b es acotado en el intervalo y no nulo casi en todas partes; el argumento del adjunto multiplicador prueba densidad del ideal sin requerir inversa acotada.
- **Corolario 5.2. PROVED.** Para el mapa continuo a espacio finito-dimensional, la imagen del ideal denso es subespacio denso y por tanto toda la imagen. Existen las preimágenes finitas empleadas para corregir aproximaciones y conservar restricciones. La continuidad de la forma da valor negativo dentro del ideal restringido. El enunciado no reclama infinitas direcciones negativas dentro de ese ideal, aunque podrían extraerse por argumentos adicionales innecesarios.
- **§6. PROVED / alcance correcto.** El fracaso ocurre ya en Λ; por tanto no hay candidato positivo que someter al test de eliminación ni enlace que auditar. El generador nulo da dominio nulo, no especificidad útil. Cambiar arbitrariamente la dependencia b↦C_b no altera la obstrucción mientras cada C_b siga compacto.

**Dos precisiones editoriales de alcance, sin afectar pruebas.** (i) En §8 «dominio aritmético de codimensión infinita» debe leerse para dominios lineales cerrados: si el dominio es una variedad no lineal, codimensión y densidad requieren definición y no se sigue aquí tal condición necesaria. La formulación universal válida es que el dominio de positividad no puede contener un subespacio cerrado de codimensión finita ni el ideal denso declarado con sólo finitísimas restricciones. (ii) En §7, una positividad heredada no refuta por sí sola una identidad de enlace específica que falle al borrar: esa identidad aún podría aportar contenido (§5 de esta auditoría). El constructor no construye tal identidad ni afirma un NO-GO general para ella; así leído, la tabla es cribado de propuestas genéricas, no teorema sobre toda conjugación.

**SYNTHESIS: aprobada.** I+J≥0 se sigue de la descomposición en V₊ y V₋ y la corrección I no compacta. Es ejemplo genérico sin enlace aritmético, no candidato. La salida no compacta sólo es condición necesaria dentro del ansatz y dominio ambiente elegidos; no condición de todo O1.

Resultado final: un control elemental de compresiones y un NO-GO funcional elemental para J+compacto sobre los dominios grandes especificados. Ningún avance demostrado hacia el signo por sí mismo; ninguna clausura de O1, ninguna transferencia al nodo global PW_T con colas. El hito inicial de núcleo positivo específico no fue alcanzado.
