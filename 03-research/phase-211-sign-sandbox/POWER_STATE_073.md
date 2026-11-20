# POWER_STATE_073 — Avance positivo: todos los pares de potencias

Estado: **PROVED/APROBADO**. Fuentes POWER_THETA_HAZARD_COMPACT_073.md y POWER_THETA_TWO_COPY_073.md; revisión independiente POWER_THETA_AUDIT_073.md, constructor y root. Verificador tools/power_theta_compact_073_verify.py reproducido por constructor, root y mapa: exit0/PASS en4096paneles fijos. Sin campaña de parámetros. Papers y phase103 intactos.

## Compacto cerrado

La obligación abierta de phase103/103_43 era V'''(t)>0 para0<t<1/4, con V=−logPhi y la MISMA Phi positiva de CONE001. Se verifica más fuertemente la cuarta derivada de logPhi negativa enTODO[0,1/4] por intervalos racionales, reteniendo m1..4 y una cola explícita para TODOSm>=5 en cada una de las cinco derivadas. La paridad fuerza(logPhi)'''(0)=0. Integrar el signo certificado y pegar la prueba exterior10343 demuestra V'''>0 para TODOt>0.

No se promueve un prefijo theta como suma completa. El certificado usa aritmética outward70dígitos, Machin y Taylor racionales, y una malla única fijada antes de ejecutar.

## Consecuencia para la forma completa

Para el tilt bilateral exp(ux)Phi(x), poner M(u)=E_uX=L(u+1/2). El argumento de DOS copias demuestra M''(u)<0 y M(u)−uM'(u)>0 para TODOu>0. En coordenadas de CONE001, para a>b>1,

    1<L(a)/L(b)<(a−1/2)/(b−1/2).

Por el criterio exacto de dos generadores, la matriz

    K_ij=[L(a_i)+L(a_j)]/(a_i+a_j−1)

es definida positiva para exponentes distintos a,b>1. Es la forma real COMPLETA, con ARCH, polar y TODOS los contactos, no una componente positiva aislada. La congruencia diagonal del mapa exterior conserva el signo para cualquier combinación real c1X^(−a)+c2X^(−b).

Para a=b la matriz es semidefinida positiva porque ambos generadores coinciden; la función representada no nula tiene energía estrictamente positiva, mientras el vector redundante que representa cero tiene energía cero.

## Diferencia y límite

El antiguo a,b>=32 de CONE001§5 queda superado PARA PARES por todos a,b>1. Se conserva ese resultado como antecedente histórico, sin editarlo. La nueva prueba usa el compacto theta específico más una desigualdad condicional de dos copias; no presupone la positividad de la forma ni usa únicamente logconcavidad genérica.

No demuestra tres generadores, matrices de todos los órdenes, la envolvente lineal completa ni una nueva ventana temporal. Las comparaciones polinómicas de cinco tilts de10343 son obligaciones distintas. El signo global sigue OPEN.
