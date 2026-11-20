# Estado020 — Inverso completo positivo fuera de un intervalo y balance pendiente

Estado: PROVED resultados parciales auditados; signo global OPEN. Goal activo. Papers intactos. Sustituye STATE019 como resumen vigente.

## Cobertura de W sin cambios

El puente escalar017 sigue siendo suficiente: completar W>=0 para TODOS N,k a u31.5 cerraría el signo de todos los datos mediante el puente fuerte. Están probadas filas N1,2,3 para todo k y el cono k>=10000N². Ocho polos arbitrarios y bloque confluente12 siguen vigentes. Esta ronda no prueba una nueva entrada W ni amplía ventanas T.

## Resultado positivo sobre el inverso COMPLETO

POWER_INVERSE_KERNEL_020 demuestra H_N/4<=h_N<=7H_N/4 para TODOS N>=2 y logx>=(N−1)/30. Usa A_N(logx), polinomio de coeficientes positivos, para acotar la SUMA COMPLETA de Möbius por sum_(m>=2)m^-2<=3/4. No infiere signo de un prefijo.

Para N2 prueba además h_2>=H_2/[2zeta(32)]>H_2/4 en TODA la semirrecta. La fórmula exacta conserva el signo de la derivada de1/zeta32. Por tanto cualquier parte negativa del inverso para N arbitrario está localizada en [1,exp((N−1)/30)). La cola del emparejamiento con B<0 es favorable y su magnitud se expresa mediante integrales gamma incompletas. La magnitud adversa interior sigue abierta; no se deduce de ello W>=0.

## Primer contacto: obstrucción cuantitativa real

POWER_SIGNED_BALANCE_020 estudia un solo átomo N211,k1,u31.5. Una cota analítica de ARCH por Euler/digamma trasladada y Jensen da ARCH/norma²<−.74; evaluación racional exacta da0<P2/norma²<.075, y el polar es negativo. Así ARCH+POLAR+P2<−.66norma². El resto de contactos es positivo por019 y NO se omite de W. Esto refuta únicamente la reparación con el primer contacto en ese caso; no demuestra W negativa ni imposibilidad de varios contactos.

Root leyó ambas pruebas y reprodujo los dos verificadores Fraction con PASS. POWER_BALANCE_AUDIT_020 contiene la revisión independiente completa, aprobada. No se modificaron papers.

## Próximo paso concreto

Conservar la suma firmada restante para el balance de k1 y controlar el emparejamiento interior de h_N con B. Se autorizó un diagnóstico numérico pequeño en el MISMO átomo211 para decidir si cotas separadas de componentes podrían bastar; sus valores no se incorporan como teoremas ni como signo de W. No se lanza una campaña de nuevos órdenes.

El objetivo global continúa activo. Las obstrucciones ya registradas no equivalen a un bloqueo externo ni a una refutación de la forma real. Todo resultado debe seguir distinguiendo signo de un kernel, de un término aritmético y de la forma completa.
