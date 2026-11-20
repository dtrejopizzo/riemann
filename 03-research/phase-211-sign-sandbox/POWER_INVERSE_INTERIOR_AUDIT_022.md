# POWER INVERSE INTERIOR AUDIT 022

Estado: memo final §§1–5 y verificador APROBADOS. Papers intactos.

Revisados `POWER_INVERSE_INTERIOR_022.md` y `tools/power_inverse_interior_022_verify.py`. Ejecución independiente del verificador: PASS, con −2/3<h_128(1)<−33/50 y cola completa m≥65 menor que10^−10 en valor absoluto. Los decimales de diagnóstico no se usan como prueba.

## 1. Identidad y parte finita

Se mantiene exactamente el kernel020: u=63/2, d127, H_N(x)=x^−33 A_N(log x), A_N=32P_N−P_N′. La recurrencia Fraction de p_j coincide con su fórmula gamma; a_j=32p_j−(j+1)p_(j+1) son positivos, a0=1/2. Por tanto h_128(1)=Σμ(m)m^−32 A_128(log m).

La rutina de Möbius por división de prueba detecta factores cuadrados, cambia signo una vez por cada factor primo distinto y trata correctamente el factor residual y m1. No depende de una tabla externa ni de un supuesto signo de μ. La suma m≤64 se evalúa con intervalos exteriores. Los logaritmos se reducen a [1,2] y se encierran con120 términos positivos de atanh y el resto geométrico 2t^241/[241(1−t²)]. El redondeo racional exterior de cada operación conserva la inclusión, también al multiplicar por μ negativo.

## 2. Cola infinita completa

Para todos los grados 0≤j≤127, x^−32(log x)^j decrece en x≥64, porque log64>4>127/32. En consecuencia la suma desde65 está acotada por la integral desde64. La sustitución de |μ| por1 y los coeficientes positivos a_j dan un majorante absoluto de TODA la cola.

La integral I0=1/(31·64^31) y la recurrencia I_j=64^−31(log64)^j/31+(j/31)I_(j−1) son exactas. Sustituir log64<21/5 conserva la dirección porque sólo aparecen sumandos positivos. La suma racional resultante es menor que10^−10. Añadir y sustraer este bound a los extremos de la parte finita demuestra el intervalo estricto (−2/3,−33/50), sin depender del prefijo solo.

## 3. Novedad y alcance

019 sólo había certificado un prefijo negativo para órdenes grandes;020 certificó positividad del inverso completo en una región exterior y globalmente para N2.022 decide por primera vez aquí el inverso COMPLETO en un punto interior concreto. Es compatible con020: para N128 el punto log x=0 está fuera del rango exterior log x≥127/30.

El resultado refuta la hipótesis h_N(x)≥0 para todos N,x en los kernels reales de esta construcción. No prueba negatividad de F_N, del emparejamiento integrado con B, ni de W. La negatividad puntual tampoco decide la magnitud de la parte adversa frente a la cola favorable de LOCAL020. No certifica una nueva ventana T, ni descarta un control firmado completo del emparejamiento.

Revisión final: leído el memo completo y ejecutado de nuevo el certificado reforzado, PASS. La continuidad y el signo B<0 producen correctamente una contribución adversa local hB>0 a la derecha de1; no deciden el integral total. La continuidad junto con OUTER020 garantiza al menos un cambio de signo antes de log x=127/30. Estas consecuencias están aprobadas con su alcance puntual.
