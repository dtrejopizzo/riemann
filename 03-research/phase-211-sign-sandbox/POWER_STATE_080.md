# POWER_STATE_080 — Tres potencias arbitrarias admisibles

Estado: **PROVED**, certificado constructor FULL PASS y auditoría matemática/código aprobada. Reproducción independiente root92790 exit0/FULL PASS4096 y hash coincidente. Objetivo global del Paper47 **OPEN**; papers intactos.

## Resultado completo y fuentes

Para cualesquiera exponentes reales ai>1, la forma W es positiva en el espacio generado por hasta TRES potencias correspondientes, salvo la función nula. Para tres nodos distintos el kernel completo Kij=[M(ui)+M(uj)]/(ui+uj),ui=ai−1/2, es definido positivo; para repetidos se agrupan coeficientes. Incluye ARCH, polar y todos los contactos por la congruenciaCONE001.

Cadena de prueba:

1. BASE073: M>0,M'>0,M''<0 y M/u estrictamente decreciente.
2.079: bajo BASE, g(x)=a sqrt(x)/M(sqrt(x))−1 cóncava en un intervalo de cuadrados equivale a todos sus triples PSD; estricta concavidad da triples distintos PD.
3.078: g''<0 analíticamente para u>=63/2.
4.080: certificado continuo g''<0 en TODO[1/2,63/2], con4096panelesdyádicos fijos, jetscentrales arb256bits/cap20, Taylorgrado16 y restoCauchy racional uniforme. Constructor43260 exit0/FULL PASS.

Fuentes: `POWER_THETA_G_COMPACT_080.md` (fuente completa leída y auditada), `POWER_THETA_G_COMPACT_AUDIT_080.md`, `POWER_THREE_SECANTS_079.md`, `POWER_THREE_SECANTS_AUDIT_079.md`, apéndice078 de `POWER_STATE_077.md`.

Código: `tools/power_theta_g_compact_080_verify.py`.
SHA256 comprobado:

    640d8eb8ecf2bce7e782e08333a722171744af8fc0c9831582fcfcb796fb09bc

Resto Cauchy exacto:

    5285183618944392932503807265625/
    41901009533176678637026095660718210485846016 <10^−12.

## Novedad y límites

053 ya cubría hasta trece tasas arbitrarias>=31.5.080 añade TODOS los triples admisibles, incluyendo tasas pequeñas y mezcladas. No extiende el número de generadores ni certifica una ventana temporal nueva. Cuatro generadores, todos los órdenes y el signo global siguen OPEN. No se usa h cóncava ni herencia de BASE por los restosG_p:081 refuta esa herencia literal,082 mantiene un criterio recíproco condicional más amplio.

La historia de encierros fallidos del resto está documentada en audit080. Se conservaron malla/intervalo/precisión/margen0; la representación final de restoCauchy es distinta y fue auditada antes de su corrida. Ningún FAIL de intervalos se promovió a contraejemplo ni a prueba.
