# POWER_FOUR_GENERATORS_085 — Positividad para cuatro generadores arbitrarios admisibles

Estado: **PROVED, certificado constructor exit0/FULL PASS y auditoría independiente matemática/código aprobada; reproducción independiente root29132 exit0/FULL PASS16384 y hash coincidente.** Véase `POWER_FOUR_GENERATORS_AUDIT_085.md`. Cuatro generadores arbitrarios, no todos los órdenes. Papers intactos.

## 1. Obligación precisa y antecedentes

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D; leídos080,083,084 y sus revisiones.083 factoriza exactamente el determinante del kernel completo.084 prueba por Rolle que, para un dato creciente y estrictamente cóncavo f, la condición2f'f'''−3(f'')²>0 implica el signo positivo del Pfaffiano en TODOS los conjuntos de cuatro nodos, no sólo en confluencia.

Para la Phi real, poner x=u², R(x)=u/M(u), S(x)=uM(u).073/080 prueban ya R',S'>0,R'',S''<0 para u>1/2.084 identifica exactamente las dos obligaciones adicionales N_R,N_S>0, con

    T_R=2R'R'''−3(R'')²=N_R/(16M⁴u⁶),
    T_S=2S'S'''−3(S'')²=N_S/(16u⁶).

Su exterior está probado para A=u+1/2>=128. Sólo falta el intervalo1/2<=u<=127+1/2. Esta fuente comprueba ESA obligación continua con dos funciones escalares completas; no selecciona matrices ni prueba sucesivamente dimensiones mayores a tasas aisladas. El criterio, su falsificador de herencia y los restos exteriores son de084; aquí no se presentan esas identidades de nuevo como una estimación.

## 2. Funciones exactas y regularización del extremo

Usar c=M(u),d=M'(u),e=M''(u),f=M'''(u), y D=ud,E=u²e,F=u³f. Entonces

    N_R=3c²+c(−6D−6E−2F)+3D²+6DE+2DF−3E²,
    N_S=3c²+c(6D+6E+2F)−9D²−6DE+2DF−3E².          (NUMERATORS)

Se evalúan por la MISMA función entera aritmética de080,

    Z~ A[1+(A−1)zeta_deflate(A)]Gamma(A/2)pi^(−A/2),
    A=u+1/2,
    zeta_deflate(A)=zeta(A)−1/(A−1).

La constante positiva que relaciona esta expresión con∫Phi(t)e^(ut)dt no cambia M=(logZ)'. La regularización es entera en A=1 y allí la expresión vale1; no se evalúa el polo de ζ. El extremo u=1/2 sólo sirve para el encierro analítico: los exponentes de la conclusión admisible son estrictamente mayores que1.

La semántica de deflate y la exactitud por intervalos de los jets se verificaron contra la API instalada python-flint0.9.0 y documentación oficial de FLINT, como080:

- https://arblib.org/arb_poly.html
- https://flintlib.org/doc/arb_poly/_arb_poly_zeta_series.html

Los tests del valor regularizado en A=1 y la identidad ordinaria en A=2 son comprobaciones de implementación, no la prueba de esa identidad matemática. No hay truncación de la aritmética sin un error: se usa evaluación rigurosa de la función completa.

## 3. Un bound de M independiente de todos los paneles

Fijar r=1/32. Para centros c0 en[1/2,127+1/2],

    c0+r+1<=128+17/32<129+1/2.

Por monotonía de M y la fórmula aritmética en A=130,

    M(t)<=M(129+1/2)
      <1/130+1/129+(1/2)log[130/(2pi)]
      <2/129+(1/2)log27
      <2/129+33/20<2,                               (MEAN-BOUND)

para todos los parámetros reales necesarios. Se usa pi>3, psi(y)<=logy y el signo negativo del sumando aritmético para este UPPER. La desigualdad log27<33/10 se obtiene de exp(11/10)>3 mediante una suma Taylor positiva racional. Se evalúa primero un ancla de tasa mayor; no se aplica2/129 como bound racional punto a punto a tasas pequeñas.

Entonces

    Z(c0+r+1)/Z(c0)<exp[2(r+1)]=exp(33/16)<8.        (RATIO)

La última constante usa log2>2[(1/3)+(1/3)^3/3]=56/81 y3·56/81>33/16. Todas esas comparaciones son racionales en el verificador.

## 4. Disco de Cauchy y bound de los DOS numeradores

Para |z−c0|<=r, positividad y paridad de Phi dan, como080,

    |Z^(k)(z)|<=2k!Z(c0+r+1)<16k!Z(c0),
    |Z(z)−Z(c0)|<=2rZ(c0+r+1)<Z(c0)/2,
    |Z(z)|>Z(c0)/2.

Por tanto los cocientes y las derivadas logarítmicas son analíticos en todo el disco y

    |Z^(k)/Z|<32k!, k=1,2,3,4,
    |M|<32, |M'|<1100, |M''|<72000, |M'''|<8000000.

Para la última derivada se usa exactamente

    M'''=Z''''/Z−4Z'Z'''/Z²−3(Z''/Z)²
                        +12(Z'/Z)²Z''/Z−6(Z'/Z)^4.

Con los ratios32,64,192,768, el bound absoluto es7115520<8000000. Las derivadas precedentes cuestan1088<1100 y71872<72000.

Como |z|<128, poner

    C*=32, D*=128·1100,
    E*=128²·72000, F*=128³·8000000.

La misma cota sirve para AMBOS numeradores de NUMERATORS:

    |N_R|,|N_S|
      <3C*²+C*(6D*+6E*+2F*)+9D*²+6D*E*+2D*F*+3E*²
      =8901242950707612672<10^20=:B.                 (DISK-BOUND)

Esta cota incluye todas las cancelaciones como un error absoluto seguro; no es una evaluación de la forma sobre datos complejos ni un supuesto del signo buscado.

## 5. Certificado continuo fijado antes de ejecutar

La partición consiste en16384intervalos iguales de[1/2,127+1/2]. Su radio es h=127/32768 y sus centros exactos son

    c_j=[16384+(2j+1)127]/32768, j=0,...,16383.

Para CUALQUIERA de las dos funciones N(z), usar el polinomio de Taylor hasta grado40 en el centro. Cauchy y DISK-BOUND dan el error completo

    epsilon=B(h/r)^41/(1−h/r),
    h/r=127/1024,
    epsilon=10^20(127/1024)^41/(1−127/1024)<10^(−16). (TAIL)

Se usa esta fracción EXACTA, no el upper decimal10^(−16), en cada assert. Si N_k=N^(k)/k! son los coeficientes normalizados, el signo se certifica en TODO el panel al verificar

    N_0.lower−Σ_(k=1)^40 |N_k|.upper h^k−epsilon>0.   (PANEL)

Se exige PANEL para N_R y para N_S en CADA intervalo. No se usa positividad en centros como si bastara para cubrir el compacto; la cola TAIL cubre todos los puntos entre ellos y los extremos.

## 6. Implementación y estado de la corrida

Código: tools/power_four_turan_compact_085_verify.py. Parámetros fijados antes de ejecutar:512bits, cap45,16384paneles, r=1/32,B=10^20,grado40. cap45 conserva logZ hasta grado44, M hasta43 y M''' hasta40; ambos numeradores tienen precisión de serie al menos41. Se exige finitud de TODOS los coeficientes0,...,40 y el valor E0>0 antes de logE.

Sólo se calculan jets en centros reales EXACTOS. No se vuelve a usar la representación intervalar en parámetro que perdió dependencia cerca del polo en los intentos080. Los errores de las funciones especiales se mantienen como bolas rigurosas; el resto del intervalo lo paga TAIL analítica, no un jet sobre una bola ancha. Los parámetros no se modifican según valores diagnósticos.

La corrida fija61911 terminó exit0/FULL PASS: constantes analíticas y regularización, y AMBOS signos en TODOS los16384paneles. No se modificó el script durante su corrida y no se ajustó ningún parámetro. El SHA256 del verificador reproducible es

    4916689a48baf3164b8e99ff8ff7973dbd505367cf9ee46b17b7efc9845abf46.

La cota común entera impresa es8901242950707612672. La cola impresa es exactamente la fracción TAIL, no una estimación flotante. El archivo.sha256 fija la misma versión para reproducción independiente.

## 7. Empalme y conclusión completa de cuatro generadores

El certificado compacto FULL PASS combinado con OUTER-TURAN084 prueba T_R,T_S>0 en TODO u>=1/2. El criterio global de Rolle084 da Pf(A_R),Pf(A_S)>0 para cualesquiera cuatro nodos distintos ui>1/2. La factorización083 da detK>0; los menores inferiores080 completan la definitud positiva del kernel COMPLETO para CUATRO exponentes distintos A_i>1. Los exponentes repetidos se agrupan y dan una matriz redundante semidefinida positiva, con energía positiva en la función representada no nula.

La positividad incluye ARCH, polar y TODOS los contactos aritméticos por la identidad exacta del kernel de CONE001. La congruencia diagonal del mapa exterior conserva la conclusión para cualquier combinación real de cuatro potencias con exponentes>1.

El resultado NO implica cinco generadores, todos los órdenes, la envolvente lineal completa ni una nueva ventana temporal. No se modifica ningún paper. El signo global del Paper47 sigue OPEN.
