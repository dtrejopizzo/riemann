# AUDIT_010 — Momento espectral necesario para comprimir D_n

2026-10-19. Revisor independiente. Leído LINK_010_SPECTRAL_REGULARITY.
**Veredicto: PROVED el límite inferior y la exclusión de la clase con momento espectral s finito. Compresión unitaria general de D_n OPEN. Objetivo D activo.**

## 1. Corpus y pregunta nueva

Búsqueda dirigida en índice de regularidad, momentos espectrales, dominios fraccionarios y continuidad; revisión de LINK009 y del módulo007, además de la distinción ya registrada con la no interpolación de Paper44. No se identifica esta condición de momento en las entradas consultadas. Eso no declara prioridad global.

La diferencia de clase está escrita: se mantienen D_n sin normalizar, se permite compresión SIN ley de semigrupo y se añade una hipótesis explícita sobre la medida espectral de JA. No se traslada ilegítimamente la obstrucción de V_n ni se usan valores en todos los racionales como si ya estuvieran fijados.

## 2. Incrementos del observable finito

Sea S el soporte primo de A y L par divisible por todos esos primos. Con n=1+kL y m=n+L:

- n y m son coprimos con cada primo de S.
- gcd(n,m)=gcd(n,L)=1.
- Dividir N por n o m no cambia las valuaciones de S, por lo que D_nA=X_nA y D_mA=X_mA.

Independencia de las valuaciones da

    E_s|D_nA−D_mA|²
      =a[n^(−s)+m^(−s)−2(nm)^(−s)], a=E_s|A|²>0.

La identidad es válida también para A complejo, porque el producto cruzado contiene |A|². El componente gaussiano de la distancia es no negativo. Con h=log(m/n), nh→L y m/n→1, mientras n^s(nm)^(−s)=m^(−s)→0. Así el límite inferior anunciado es exactamente ≥2κa/L^s>0.

No se necesita regularidad gaussiana extra. Como control más fuerte opcional, su contribución dividida por h^s tiende a cero: de007, ||TD_nA||≤n^(−(s+1)/2)sqrt(Π(A)), y análogamente para m. Por tanto la distancia completa normalizada tiene de hecho límite 2κa/L^s. La versión liminf escrita es suficiente y correcta.

## 3. Compresión y teorema espectral

Para mapas fijos acotados P,J y U(t)=exp(itB) unitario C₀,

    ||D_mA−D_nA||≤||P||·||(U(h)−I)JA||.

Sólo se usa unitariedad y la ley del GRUPO ambiental. No se presupone semigrupo de las compresiones ni que P=J*. La igualdad en n=1 obliga PJ=I en una realización, pero el argumento no necesita explotarla.

Si ∫|λ|^s dμ_A<∞, para 0<s<2 se tiene

    |exp(ihλ)−1|²/|h|^s≤4|λ|^s.

El cociente tiende a cero para cada λ porque 2−s>0. Convergencia dominada da ||(U(h)−I)JA||²/|h|^s→0, contradiciendo el límite inferior positivo. Todos los exponentes y la constante de dominación son correctos.

La equivalencia con JA∉Dom(|B|^(s/2)) tiene el orden exacto: el cuadrado de la norma de |B|^(s/2) contiene |λ|^s. En α=1/4 se exige momento absoluto1/2 y se excluye Dom(|B|^(1/4)), no Dom(|B|^(1/2)) como equivalente.

## 4. Lo que queda abierto

La condición necesaria es fuerte: CADA observable algebraico no nulo debe tener imagen con momento s infinito en una compresión hipotética. No prueba que tal compresión sea imposible. Continuidad fuerte sólo exige que las diferencias tiendan a cero sin una tasa; permite el comportamiento irregular necesario aquí.

Tampoco se ha demostrado que los tests suaves de Q_T, bajo un enlace todavía no construido, deban corresponder a alguna de esas imágenes JA con regularidad espectral finita. Esa implicación requiere mapa y dominio explícitos. No se puede usar el resultado como barrera para todas las realizaciones de Q_T.

**Condición necesaria aprobada. Compresión general OPEN; no forma ni traza de Q_T construida.**
