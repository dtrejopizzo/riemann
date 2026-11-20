# POWER_R12_AUDIT_049 — Corte efectivo y primer transporte restringido

Estado: **APROBADO** CENTERED_CUTOFF049 y R12_TRANSPORT049. Resuelve R12 para el primer movimiento desde V12, con c=1/2500. No certifica W completo ni iteración. Papers intactos.

Antecedentes cotejados: índice/crucigrama, PRIME_TRANSFER014 y auditoría, GEOMETRIC_TRANSFER015, QUADRATIC017, BLOCK007 y ENDPOINT048. La hipótesis restringida seguía OPEN. La diferencia efectiva es un corte analítico uniforme en todos los numeradores, seguido del certificado exhaustivo de los únicos trece índices restantes. No se utiliza el falsificador universal de orden enorme para descartar esta restricción.

## Corte analítico

La transformación z=exp(2ix), y=sin x y el centrado exp(−11ix) son exactos, incluso para coeficientes complejos. Los sectores cos x R(y), S(y) tienen paridades opuestas y grados10/11; sus cruces integran cero tanto en norma como en momento inverso. El jacobiano da precisamente exponentes j+1/2 y j−1/2. La razón total es mezcla positiva de las razones sectoriales.

Revisadas las dos integraciones por partes: el operador polinómico simétrico tiene eigenvalores n(n+2a+1), y los bordes de ambas fórmulas se anulan bajo a>0. De aquí 2ar<=1+2sqrt(rD). Los coeficientes normalizados decrecen en j; el sector de grado10 queda dominado por el de grado11. Para todo j>=14 resulta27r<=1+2sqrt(429r). La comprobación16129/400>0 sitúa su raíz positiva debajo de49/20. Por tanto E(tau^−2)<1/405 uniformemente, sin una hipótesis asintótica de dimensión.

El lower global de digamma usado existe con prueba explícita en Paper47, main.tex:505, lem:mbounds(ii): integración por partes del kernel g con g'>0 y variación total1/2. Jensen y Cauchy tienen la orientación correcta y dan ARCH>859/800. El contacto2 cuesta menos de una norma² y el polar efectivo048 cuesta a lo sumo3(9/62)^j. Esto supera1/2500 para toda la cola j>=14.

## Certificado finito

Leído íntegro power_r12_finite_segment_049_verify.py y reproducido independientemente con python3: **PASS para los trece bloques1,...,13**, exit0. La ampliación de007 usa bandas0..24, sumas de potencias2..25 y los mismos restos racionales explícitos. Son suficientes para las imágenes de dimensión ambiente12+j<=25. C_j reproduce exactamente los coeficientes de(1+z)^j; omitir2^−j no altera el signo. El error de operador<10^−8 se paga contra C_jᵀC_j, no contra la identidad de las coordenadas originales. Los LDL racionales verifican todos los cruces y todos los pivotes. No se usan autovalores flotantes.

## Mezcla y alcance

Para cada v finito>=u, r=1−u²/v² pertenece a[0,1). La identidad de densidades es |G_v|²=(1−r)sum r^j|Q^(j+1)F|². ARCH y contacto2 se suman por convergencia absoluta; las normas fuertes de015 acotan uniformemente las energías de la órbita. El multiplicador Q es contracción en Sobolev no ponderado y en L² exponencial con eta entre1/2 y u/2. El polar se verifica separadamente por la serie escalar exacta (1−r)sum r^j(−1/3968)^(j+1)=−1/(4v²−1). No se necesita uniformidad cuando v tiende a infinito.

Cada término de la mezcla de E2−c norma² es positivo, incluidos j=1..13 y toda la cola. Así R12 es válida para todos los v finitos>=u desde la base EXACTA V12, a c=1/2500, también inferior al margen base007. El caso v=u es r=0. La ganancia no incluye los demás contactos: su cota007 no se ha transportado. Tampoco se conserva automáticamente la hipótesis sobre bases intermedias al mover un segundo polo. El alcance declarado en R12_TRANSPORT049 es correcto.
