# POWER BALANCE AUDIT 020

Estado: APROBADOS SIGNED_BALANCE020 e INVERSE_KERNEL020, con los alcances delimitados a continuación. Papers intactos.

## Restricción de novedad y de alcance

Se conservan los antecedentes auditados en POWER_SIGNED_AUDIT_019: Euler/Möbius y Λ*1=log no son una prueba nueva de signo; Descartes es una herramienta clásica. La nueva frontera específica de autocorrelación019 sí prueba signo del peine de k=1 para N≤211, pero no el de la forma W completa. La media negativa B019 y el prefijo inverso negativo no deciden el kernel inverso completo.

Esta ronda exige verificar por separado las normalizaciones y el balance de las tres contribuciones reales ARCH, peine y polar, o un emparejamiento firmado completo que lo controle. No se aceptará trasladar el signo de un portador a otro sin la desigualdad correspondiente. La tabla completa y nuevas ventanas T permanecen abiertas mientras no se pruebe su condición suficiente.

## SIGNED_BALANCE020 — APROBADO

Revisados `POWER_SIGNED_BALANCE_020.md` y `tools/power_signed_balance_020_verify.py`; ejecución independiente PASS. La integral de Euler del resto de ψ tiene módulo ≤(1/2)∫(a+t)^−2dt=1/(2a). Las cuatro traslaciones desde 1/4 hasta 17/4 conservan el signo menos de los recíprocos. En x=T², log(A+x), −a/[2(A+x)] y cada −b/(b²+x) son cóncavas; Jensen suministra la cota superior U con E T²=3u²/[4(2N−3)]. La normalización es la de ARCH real, sin polar incorporado.

La norma beta y K_N son correctos; el factor −2Λ(2)2^−1/2 de peine y 2^−u=2^−31/√2 producen exactamente (log2/2^31)K_Nr_N(u log2). El evaluador Horner conserva extremos Fraction sin redondeo intermedio. Se certifican ARCH/norma<−.74 y 0<P2/norma<.075 en N211,k1,u31.5. El polar es estrictamente negativo, por lo que la forma real conservando sólo contacto2 es menor que −.66 veces la norma.

Alcance: obstrucción nueva y concreta al balance mediante el primer contacto en esta columna. No es una nueva fila positiva de W. Todos los contactos restantes son favorables por019 y siguen pendientes de magnitud conjunta; no hay conclusión W<0 ni prohibición de reparación mediante varios contactos. La fórmula general U se prueba para N variable, pero sólo se certifica FAIL2 en el punto declarado.


## INVERSE_KERNEL020 — APROBADO

Leídos `POWER_INVERSE_KERNEL_020.md` y `tools/power_inverse_kernel_020_verify.py`; ejecución independiente PASS. La fórmula gamma de p_j y el cociente (j+1)p_(j+1)/p_j≤u son correctos. Por tanto A_N=(u+1/2)P_N−P_N′ tiene todos sus coeficientes estrictamente positivos y grado N−1; H_N=x^−33 A_N(log x) conserva la normalización de019.

La comparación de cada monomio da A(t+l)/A(t)≤exp(dl/t). Para log x≥d/30, la serie COMPLETA de Möbius se domina por Σ_(m≥2)m^−2≤3/4. Esto prueba H/4≤h≤7H/4 sin ninguna inferencia desde prefijos. La expansión finita de A también justifica que h sea x^−33 por un polinomio, con coeficiente principal positivo A_d/ζ(32).

Para N=2, Σμ(m)log(m)m^−32=−M′(32)=−D(32)/ζ(32), de modo que la fórmula H2 tiene el signo menos correcto. La cota D(32)≤Σm^−31 y 1008D<1/4 dan h2≥H2/[2ζ(32)]>H2/4 en toda la semirrecta. La serie y sus derivadas necesarias son absolutamente convergentes.

LOCAL conserva la dirección: B<0 y h≥H/4 implican 2hB≤−(a0/2)H(x−1) en la cola. La integración por partes de esa cola tiene correctamente el término positivo (X−1)w(X). La parte adversa del emparejamiento queda localizada en [1,exp((N−1)/30)], sin que se haya demostrado que su magnitud esté compensada.

## Conclusión de la ronda

Resultado nuevo de signo: positividad del kernel Möbius COMPLETO en la región exterior explícita para todo N, y global para N=2. Resultado nuevo de balance: el primer contacto solo no repara el átomo N211,k1. Ninguno prueba una nueva entrada positiva de la forma W que no estuviera cubierta, ni una nueva fila o ventana T. La cota del emparejamiento interior y la magnitud favorable del resto del peine permanecen abiertas; no son sustituidas por las identidades.
