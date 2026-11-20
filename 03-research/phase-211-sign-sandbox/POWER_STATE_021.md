# Estado021 — Diagnóstico acotado del balance de un átomo

Estado: PROVED dos cotas parciales exactas; NUMÉRICO el diagnóstico de cancelación; signo global OPEN. Goal activo. Papers intactos. Complementa y sustituye STATE020 como resumen vigente; todos sus resultados permanecen válidos.

## Cobertura de la forma completa

Sin ampliación en esta ronda: filas N1,2,3 completas, cono k>=10000N², ocho polos arbitrarios y bloque fijo12. El puente escalar017 exige completar TODOS N,k. No hay nueva ventana T certificada.

## Resultado exacto y alcance numérico separados

POWER_CONTACT_BALANCE_021 mantiene un único átomo, N211,k1,u31.5. PROVED: ARCH+POLAR+contactos2,3,4<−.21norma². PROVED: la suma COMPLETA de contactos q>300 está entre0 y5e−13 veces la norma². La prueba de cola usa coeficientes absolutos, unimodalidad, una cota de la derivada logarítmica y una recurrencia exacta de integrales; no enumera contactos adicionales. Root leyó la prueba y reprodujo el verificador Fraction PASS. La revisión independiente quedó aprobada en POWER_CONTACT_BALANCE_AUDIT_021.

NUMÉRICO solamente: cuadratura a45 y65 dígitos y contactos<=300 dan una suma parcial alrededor de−6.0812e−14norma². La coincidencia de precisiones NO certifica error de cuadratura. La cota racional de la cola NO convierte ese diagnóstico en un intervalo riguroso para W. No se afirma W positiva, negativa ni cero.

El diagnóstico muestra cancelación muy fina entre términos de orden1; las cotas separadas gruesas usadas aquí no deciden el signo. Esto no es un NO-GO global sobre certificados, peines finitos o desigualdades firmadas. Se detuvo la enumeración en300 para no convertir el diagnóstico en una campaña de precisión.

## Herramienta aritmética vigente de020

POWER_INVERSE_KERNEL_020, revisado en POWER_BALANCE_AUDIT_020, controla el inverso Möbius COMPLETO: H_N/4<=h_N<=7H_N/4 si logx>=(N−1)/30, para todos N>=2. Para N2, h_N positivo en toda la semirrecta. La posible parte adversa queda en un intervalo explícito; su emparejamiento con B sigue abierto.

## Próximo trabajo

Buscar una desigualdad que conserve las cancelaciones entre ARCH, polar y el peine, o controlar el emparejamiento interior del inverso completo. No extrapolar una suma parcial numérica al signo de W, ni volver a una reparación por sólo el primer contacto ya refutada. El objetivo sigue activo y no está completado ni bloqueado.
