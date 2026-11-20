# POWER CUMULATIVE AUDIT 023

Estado: APROBADOS criterio condicional, punto128 y falsificador completo129. La hipótesis universal K≥0 queda FALSIFIED. Papers intactos.

## 1. Primitiva, masa y criterio — APROBADO

Revisados `POWER_CUMULATIVE_INVERSE_022.md` (construcción de ronda023) y `tools/power_cumulative_inverse_022_verify.py`. Ejecución independiente: PASS, incluidos los intervalos completos J128(1)∈(.665,.666), K128(1)∈(.003,.004) y el certificado previo h128(1)<−.66.

La fórmula J(x)=Σμ(m)w(mx) es la integral de cola correcta: el factor m de h se cancela al integrar. La expansión finita del polinomio en log x y log m prueba convergencia absoluta uniforme en x≥1 y el decaimiento necesario. La doble serie de MASS se domina por Σd(r)w(r), convergente con d(r)≤r; así ΣJ(n)=1 se obtiene sin hipótesis de positividad.

K=J+xh=J−xJ′ da (J/x)′=−K/x². Bajo la hipótesis GLOBAL K≥0, el límite J/x→0 implica J≥0 y J(x)≥xJ(n)/n en cada [n−1,n]. La cota del promedio celular es por tanto válida.

La integración por partes de F/2=∫hB conserva B(1)=0 y el borde JB→0. Los saltos log n de B producen +log(n)J(n); las pendientes producen −H_(n−1)∫J. Todas las series convergen absolutamente. Las cotas H_(n−1)−log n≥1−log2 y H_(n−1)/(2n)≤1/4 dan la constante uniforme log2−3/4. MASS junto con J(n)≥0 implica 1−J(1)≥0. Queda aprobado el criterio condicional F≤−2(3/4−log2)(1−J(1))≤0.

## 2. Kernel y punto certificado — APROBADO

D=33P−P′ tiene coeficientes positivos por la misma recurrencia020; K=x^−32Σμ(m)m^−32D(log x+log m). La aplicación del lema exterior020 a D controla la suma COMPLETA, no prefijos. El certificado POINT usa K=J+h en x1 y suma ambas colas absolutas; sus intervalos son correctos. No da K global ni permite extrapolación en N.

Novedad limitada: el criterio usa de manera cuantitativa los promedios celulares y la masa discreta1, tolerando h negativo. Las identidades de Möbius y la integración por partes son antecedentes clásicos; la compensación aritmética interior global permanece una premisa, no una consecuencia de la reformulación.

## 3. Alcance

Ni F≤0, aun cuando se obtenga, compensa automáticamente el déficit de ARCH_sharp. El criterio y el punto128 no certifican W ni nueva ventana T. El único punto vecino129 se revisa a continuación, sin ampliar la prueba a una campaña.


## 4. Test vecino129 completo — APROBADO

Revisados `POWER_CUMULATIVE_TEST_023.md` y `tools/power_cumulative_test_023_verify.py`. Ejecución independiente PASS: −1/250<K129(1)<−1/251 y cola completa m≥65<10^−10. Las recurrencias racionales generan correctamente P129 y A129=32P129−P129′. El kernel evaluado es P+A=33P−P′, no A solo; en x1 no falta factor m ni x.

El cálculo de μ por factorización, los logaritmos atanh encerrados y Horner exterior son los mismos procedimientos auditados022. Los129 coeficientes usados son positivos. Para todos los grados j≤128, log64>4≥j/32 asegura monotonía desde64; la integral positiva desde64 domina la suma completa desde65. La recurrencia de integrales y la sustitución log64<21/5 conservan la dirección. No se infiere el signo desde el prefijo finito.

El test refuta la hipótesis UNIVERSAL K_N(x)≥0 de la construcción acumulativa. El teorema CELL permanece correcto como implicación condicional; el punto128 positivo no queda contradicho. El punto129 negativo no implica J129<0, ERR negativo ni W negativo. No descarta un criterio integrado distinto que controle la contribución adversa. No hay nueva ventana T.

Root revisó independientemente MASS, el criterio celular con saltos y bordes, OUT-K y el alcance de POINT128, coincidiendo con esta auditoría.

## 5. Adición final §7 de CUMULATIVE_INVERSE022 — APROBADA

Leída la sección final CB-ID/CB-POS/K-MASS/BOUNDARY. La fórmula J(x)=x∫_x∞K(t)t^−2dt conserva el límite en infinito y, por Fubini absoluto, da F=−2∫K C_B con C_B=−t^−2∫_1^t x dB(x). Los saltos de B están incluidos en esta integral de Stieltjes.

En celdas completas, S(n)−S(n−1)≤−a n, a=3/4−log2, implica −S(n)/n²≥a/2 para n≥2. Entre enteros, la expresión de C_B es combinación convexa de C_B(n) y H_n/2, conservando la cota inferior. En la celda inicial C_B=(1−t^−2)/2; la fórmula se usa para t<2 y no elimina el salto en2. CB-POS es correcto.

La sustitución de J en MASS da K-MASS con peso Σ_(n≤t)n/t²=floor(t)(floor(t)+1)/(2t²). La convergencia absoluta ya demostrada permite intercambiar integral y suma pese a los signos. No se convierte esa masa en una medida positiva.

Finalmente C_B(t)≤t−1 en la primera celda da 2∫_1^(1+δ)K^-C_B≤δ²sup K^- para 0<δ≤1. El valor puntual del extremo2 no altera la integral. La amortiguación cuadrática del borde no controla por sí sola la extensión de la región negativa ni el presupuesto adverso total. Se aprueban las identidades y cotas, manteniendo abierto ese balance y la compensación de ARCH_sharp. Root coincide en esta revisión independiente.
