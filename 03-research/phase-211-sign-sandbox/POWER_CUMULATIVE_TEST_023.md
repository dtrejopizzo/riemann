# POWER_CUMULATIVE_TEST_023 — Test dirigido del criterio relajado K=J+xh

Estado: PROVED un valor negativo del criterio relajado COMPLETO, certificado racional ejecutado. Revisión independiente aprobada en POWER_CUMULATIVE_AUDIT_023.md; verificador reproducido PASS. Un único N=129,x=1, sin campaña. Papers intactos.

## Corpus y razón nueva antes de construir

Leídos las reglas del proyecto, INVERSE_KERNEL020, INVERSE_INTERIOR022 y auditoría; búsqueda dirigida en índice ROUTES-TRIED-INDEX, grid parte3 y CROSSWORD-TO-D (cumulativo/kernel relajado/inverso Möbius). La positividad de h completo ya fue refutada022. El nuevo criterio propuesto por `signo` usa K_N=J_N+xh_N, con h_N=−J_N': K>=0 fuerza que J_N/x sea decreciente y permite un argumento acumulativo más débil que exigir h>=0. Por ello el contraejemplo022 no lo decide.

Se elige SOLO el vecino N=129,x=1, sugerido por el margen positivo pequeño de K_128(1). El certificado conservará la cola infinita completa, no el signo de un prefijo. Ningún signo de K se atribuirá automáticamente al signo de W.

## 1. Resultado

Para u=63/2, N=129, se prueba

    −1/250 <K_129(1)<−1/251<0.                           (NEG)

Así es falso el lema K_N(x)>=0 para todos N>=2,x>=1, aun conservando el inverso Möbius COMPLETO. No se afirma que J_129 sea negativo, ni que la media ERR o la forma W tengan signo negativo. Se ha refutado solamente ese criterio suficiente.

## 2. Normalizaciones y polinomio correcto

Con rho_N(t)=e^-ut P_N(t), P_N=Σp_jt^j de020, se define

    J_N(x)=Σ(m>=1)mu(m)(mx)^-1/2 rho_N(log(mx))
          =x^-32 Σ(m>=1)mu(m)m^-32 P_N(logx+logm),
    h_N(x)=−J_N'(x)=x^-33 Σ(m>=1)mu(m)m^-32 A_N(logx+logm),
    A_N=32P_N−P_N'.

La derivación pasa por la serie absolutamente convergente a N fijo. Por tanto

    K_N(x)=J_N(x)+xh_N(x)
          =x^-32 Σ(m>=1)mu(m)m^-32 [P_N+A_N](logx+logm).

En x=1 no queda ningún factor adicional de x ni m. El polinomio relevante es P_N+A_N, no A_N solo. Sus129 coeficientes son racionales positivos y su grado es128.

Si se tuviera K_N>=0 en toda la semirrecta, (J_N/x)'=−K_N/x²<=0 y J_N/x->0 en infinito forzarían J_N>=0. La prueba NEG muestra que esa premisa global no vale para la familia completa; no impide que otras desigualdades acumulativas decidan el emparejamiento.

## 3. Certificado finito y cola infinita

El verificador `tools/power_cumulative_test_023_verify.py` reconstruye P_129 y A_129 por las recurrencias racionales de020/022, calcula mu(m) por factorización entera para1<=m<=64, encierra logm por series atanh con resto geométrico y evalúa P+A con Horner intervalar y redondeo exterior. No emplea funciones especiales flotantes.

Para cada0<=j<=128,

    log64=6log2>4>=j/32,

de modo que x^-32(logx)^j decrece en x>=64. Con L=21/5>log64 y

    I_0=64^-31/31,
    I_j=64^-31 L^j/31+(j/31)I_(j−1),

se obtiene una cota racional de la COLA COMPLETA:

    |Σ(m>=65)mu(m)m^-32[P_129+A_129](logm)|
       <=Σ(j=0..128)(p_j+a_j)I_j<10^-10.

El intervalo del segmento m<=64 más ese error simétrico satisface exactamente los extremos de NEG. El verificador ejecutado da PASS. El valor aproximado−.003985845090 se da solo como orientación, no como input de la prueba.

## 4. Alcance

No hubo búsqueda de otros N ni una tabla de puntos. El resultado refuta el criterio K>=0 más débil que la positividad de h, que no estaba decidido por022. Al mismo tiempo conserva la necesidad de controlar el emparejamiento firmado o una desigualdad acumulativa distinta: K negativo en un punto no determina el signo de J, ERR, W, ni de otro objeto de signo.
