# POWER CONTACT BALANCE AUDIT 021

Estado: APROBADO con separación explícita entre pruebas exactas y diagnóstico numérico. Papers intactos.

Leídos `POWER_CONTACT_BALANCE_021.md` y `tools/power_contact_balance_021_verify.py`. Root revisó independientemente la prueba y ejecutó el verificador exacto con resultado PASS. No se repitió la cuadratura, pues no añade una certificación de error.

## 1. FAIL234 exacto

Se conserva el mismo átomo N211,k1,u63/2 y la normalización020. Para q=p^a, la expresión 2log(p)q^−32 K_Nr_N(u log q) contiene el factor de von Mangoldt correcto; en q4 se usa log2. La evaluación Horner Fraction no redondea coeficientes intermedios. La norma beta y el polar exacto coinciden con020. Las tres desigualdades ARCH<−.74, POLAR<−.36 y 0<P2+P3+P4<.89 dan estrictamente ARCH+POLAR+P2+P3+P4<−.21. Este resultado concierne a esa forma parcial real, no a W.

## 2. Cola completa exacta

La sustitución Λ(q)≤log q y el uso de coeficientes absolutos de r_N producen un majorante válido sobre todos los enteros q>300, que incluye todas las potencias primas reales. Para f_l(x)=x^−32(log x)^l, l≥1, la unimodalidad da suma≤integral+supremo. Además (log f_l)′≥−32/300 en toda la semirrecta. Desde cualquier punto máximo x0≥300, f_l(x0+t)≥f_l(x0)exp(−32t/300), por lo que supremo≤(32/300)integral. El factor total 83/75 es correcto incluso cuando el máximo está en el extremo300.

La recurrencia por partes I_l=300^−31(log300)^l/31+(l/31)I_(l−1), con I0=1/(31·300^31), tiene sólo sumandos positivos. Sustituir un extremo superior racional de log300 y multiplicar por 2K_N explica el factor166/75 del script. Se aprueba 0<Σ_(q>300)P_q<5·10^−13. La positividad estricta viene de019; la cota superior no usa signo favorable de coeficientes polinomiales.

## 3. Diagnóstico y alcance

La densidad beta usada en la cuadratura está normalizada: (2/B(3/2,N−1/2))t²(1+t²)^−N−1 dt en t>0, con τ=ut. La coincidencia de cálculos45/65 dígitos es diagnóstico NUMÉRICO, no un intervalo riguroso para ARCH. Por tanto ni la suma parcial numérica cercana a −6.08·10^−14 ni su combinación con TAIL prueba signo de W. No se certifica que W sea negativa, cero o positiva.

La novedad local respecto de020 consiste en FAIL234 y la cota analítica de toda la cola, para un único átomo. No es una nueva ruta por renombrar la suma aritmética, no es un NO-GO general para peines finitos y no certifica una nueva fila o ventana T. La cancelación completa sigue pendiente.
