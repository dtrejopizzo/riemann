# Estado031 — Alternancia real de bloques y presupuesto global inicial

Estado: resultados parciales PROVED y auditados. Sustituye STATE030. Goal activo; signo global OPEN; papers intactos.

## Prefijo adverso y recuperación a tasa fija

POWER_WEIGHTED_BLOCK_031 conserva la representación W[g_N]/norma²=int G_N H de030. Para u=63/2 fijo demuestra:

    int_1^(225/64) G_N H <−3/1000, TODOS N>=2^24;
    int_1^4 G_N H >3/200, TODOS N>=2^22;
    int_(225/64)^4 G_N H >9/500, TODOS N>=2^24.

Los contactos2 y3 se incluyen exactamente. El contacto4, situado en el extremo, tiene contribución integral nula allí. La primitiva ponderada I_*(X)=int_1^X(3/2)x^-1/2H tiene valor negativo en225/64 y positivo en4. Los certificados racionales de esos extremos, combinados con un error gamma uniforme30u²/(2N−3), prueban los rangos completos en N; no hay campaña por órdenes.

Esto refuta el criterio I_*>=0 universal y demuestra una recuperación cuantitativa real. Ninguna integral parcial negativa es un contraejemplo a W total. El complemento desde4 hasta infinito permanece pendiente.

## Factor gamma con variación controlada

POWER_GAMMA_WEIGHT_031 estudia R_N(t)=rho_N(t)−(2/3)rho_N'(t), de modo que G_N(x)=(3/2)x^-1/2R_N(logx). Para TODOS N>=2 a tasa fija, R parte de1, tiene un único máximo T_N<2/3 y tiende a0. Con M2=u²/(2N−3),

    0<R_N(T_N)−1<=2M2/9,
    TV(R_N)<=1+4M2/9.

La unicidad usa la logconcavidad025; la cota de localización reutiliza Jensen026. Una barrera Riccati demuestra q''<0 para q=−rho'/rho, lo que afina el sobrepaso. Todo se refiere a la función gamma real.

Integración por partes preservando TODOS los contactos da

    W[g_N]/norma²=−int_0^infinito I_*(exp t)R_N'(t)dt
      >=int_(T_N)^infinito I_*(exp t)[−R_N'(t)]dt−M2.

La rama creciente termina antes del primer contacto y su costo adverso TOTAL es<=M2, de orden1/N. En el complemento el peso−R_N' es positivo, pero I_* tiene valores negativos reales: el signo de su promedio ponderado sigue abierto. Esta desigualdad cuantifica una parte del balance global; no declara resuelto el resto por cambiar de representación.

## Evidencia, cobertura y continuación

POWER_WEIGHTED_AUDIT_031 aprueba ambas pruebas. Root leyó los textos, revisó la identidad y las desigualdades de variación, y reprodujo el verificador exacto de bloques: PASS. El argumento de variación es analítico y no necesita recorrer parámetros.

No se amplía la cobertura de W total ni las ventanas T. A u31.5 siguen filas1..5 para todo k y cono k>=10000N²; resta N>=6 debajo del cono. Las regiones029 con u creciente mantienen su alcance separado y su obstrucción específica de puente.

La próxima obligación es una desigualdad aritmética firmada para el promedio de I_* contra la medida gamma real de la rama descendente, o un mecanismo diferente que controle todos los contactos. Enumerar otros bloques positivos y negativos no sustituiría esa obligación.
