# Auditoría de la corrección residual031

**APROBADO.** Lectura íntegra de030,031 y CORRECTION_RESIDUE_BALANCE_031, sin ejecución numérica.

M=Q=2,s=(1,1) satisface B2. El perfil de anchura estrictamente menor que log(3/2) hace W1(m,j)=delta_mj en filas1,2 para todo j positivo. Los bumps declarados interpolan exactamente s y tienen soporte dentro(2/3,5/2). En esas filas, n>=3 no contribuye; n2 sólo contribuye a j2. Así el pairing completo de módulo2 es c2(2)v2S1/2=v2/2>0. La componenteq1 restante es también v2/2 y la suma reproduce el término original, sin contradicción con030.

Esto refuta la omisión pequeña de031§3 y su repetición§4 para la interpolación declarada. La observación de balance sin pesos es verdadera; su transferencia por multiplicación no coprima falla. La elección de interpolante es explícita, no se afirma independencia del componente respecto de toda interpolación posible. TeoremaE por aproximación de configuraciones queda intacto. Ninguna negatividadW ni imposibilidad global nueva.


## Reparación rough universal

Aprobada§5: para soporte roughQ>=2 sólo hay filas impares; con W1delta y variaciónS(j/2), la ecuación j'/2^a=j/2 tiene una única solución impar a1,j'j. Coeficiente -s_jv2/2, no hay cancelación oculta. Los puntos relevantes son localmente finitos lejos de0, así existe el bump. La conclusión exige TODOS los perfiles e interpolantes y sólo se afirma para R_Q. No se infiere para soporte mixto ni se importa TeoremaE a una restricción modificada.
