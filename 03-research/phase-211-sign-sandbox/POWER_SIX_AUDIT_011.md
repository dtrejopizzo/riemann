# POWER_SIX_AUDIT_011 — Revisión independiente del signo global de seis polos

Estado: PROVED. Revisados POWER_SIX_GLOBAL_011.md y tools/power_six_global_011_verify.py; ejecución independiente con PASS. Papers intactos.

## 1. Base confluente y constantes escalares

La diagonal y las cinco bandas Toeplitz arch+polar usan las mismas fórmulas derivadas y verificadas anteriormente, con psi^(j)(16) hasta j5. Las sumas16..2000 y colas entre las integrales desde2001 y2000 tienen orientación correcta para cada signo alternado; la aritmética intervalar C.I conserva todos los extremos. La eliminación intervalar simétrica de AP-(3/25)I tiene seis pivotes de extremo inferior positivo. Los factores de columna/filapivote permanecen intactos en cada actualización. El certificado prueba signo de toda la matriz, incluidos términos cruzados.

Las sumas de momentos exactas AA,BB y la comparación4AA BB<1 justifican |Polar|<I. El valor m0 se calcula con los intervalos gamma,pi,log2,logpi previamente auditados y su extremo inferior supera-5373/1000.

El lower(x) de dieciséis términos de digamma es correcto y creciente. Los26 sitios del programa delimitan exactamente25 paneles que cubren[0,49] sin huecos; el salto10→12 está incluido como un panel. En cada panel la cota b*(c-lower(a))_+<9 es válida por monotonía y produce la desigualdad GLOBAL x(c-m)_+<9. El sitio49 verifica m>c y la monotonía extiende ese signo al exterior. No es una interpolación numérica de tasas.

## 2. Transporte de déficit

Con n6,u63/2,b3/25,C1,c1/20,X49,D9, la comparación exacta del script es

    b-c-D[(1+X/u²)^6-1]/X-6/(4u²)>3/500.

La regla general ya auditada implica AP[f]>(1/20)||f||² para todas las tasas>=u. El uso de la pérdida polar Bernoulli6/(4u²) es conservador respecto de eta_n exacta. La norma OBJETIVO de f se conserva en la identidad, así el resultado sigue uniforme aun cuando R0 tienda a cero por tasas grandes.

## 3. Mejora all-pass y TODOS los contactos

El argumento de Plancherel ponderado es válido porque las funciones causales racionales tienen decaimiento exponencial y sigma3u/4<min v_j. En la recta desplazada, la norma de cada multiplicador es(v+sigma)/(v-sigma)<=7. El primer modo tiene norma ponderada²<=4. Por tanto B6=4sum_(j0..5)49^j=(49^6-1)/12=1153440600 es correcto sin asumir ortogonalidad ponderada.

Las comparaciones2sqrt(B6)<68000 y sigma+1/2=193/8>24 están verificadas. Al usar Lambda(q)<=logq, se conserva el factor log y la integral decreciente de(logx)x^-24 desde2. Su fórmula exacta es2^-24[log2+2log2/23+2/23²], y log2<7/10 proporciona el majorante racional del script<1/250. Esta estimación incluye la suma infinita completa y no presupone signo favorable del peine.

Concluye W[f]>(1/20-1/250)||f||²=23/500||f||²>(1/25)||f||² para TODO espacio de seis polos reales>=31.5, con multiplicidades permitidas y sin cota superior ni separación mínima. El argumento cubre numeradores reales arbitrarios de grado<6; mezclas de hasta seis potencias exteriores son subcasos. El paso a siete o dimensión arbitraria requiere hipótesis nuevas verificadas, no está incluido en esta aprobación.
