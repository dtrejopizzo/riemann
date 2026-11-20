# AUDIT_004 — Control del Mellin coprimo desnormalizado

2026-10-18. Revisión independiente del insight y del memo final CONSTRUCTOR_004.

**Veredicto final: PROVED para los signos, identidades e integrabilidades declarados. Enlace con Q_T y especificidad completa OPEN.**

## 1. Asintótica exacta

Sean d,e≥2 coprimos fijos, l=de, c=y^(−1/2), r=√y y A=(d−1)(e−1)/(de)>0. Poisson implica

    τ(k²y)=c/k−1+O_k(c exp(−π/(k²y)))

para cada k fijo. Sustituyendo en B_y=τ(l²y)−τ(d²y)τ(e²y)/τ(y), y usando τ(y)~c,

    B_y(d,e)=−A c/(c−1)+O_{d,e}(c exp(−π/(l²y)))
             =−A/(1−√y)+error exponencial con factor c.

El cálculo del numerador es exacto para los términos sin error:

    (c/(de)−1)(c−1)−(c/d−1)(c/e−1)=−A c.

Por tanto B_y→−A y

    C_y(d,e)=−A√y/(1−√y)²+O_{d,e}(exp(−π/(l²y)))
             ~−A√y.

Esto refina el O(√y) de CONSTRUCTOR_002 y muestra la cancelación automática del coeficiente G₀ coprimo. **PROVED.**

## 2. Mellin directo

Por ANTICORRELATION_003, B_y=τ(y)C_y es estrictamente negativo para todo y>0 en esos índices. Es acotado en cero y decrece exponencialmente en infinito. Luego

    J_α(d,e)=∫_0^∞ y^(α−1)B_y(d,e)dy

converge absolutamente para Re α>0, define allí función holomorfa y satisface J_α<0 para α>0 real. En particular α=1/4 es admisible directamente. No se resta contratermino coprimo porque G₀(d,e)=0. **PROVED.**

Para pares con gcd(d,e)>1,

    B_y=y^(−1/2)G₀−A/(1−√y)+error exponencial,
    G₀=(gcd(d,e)−1)/(de)>0.

La integral sin resta sólo converge cerca de cero para Re α>1/2. No extender el resultado directo a diagonal ni a potencias del mismo primo. Su continuación regularizada sigue siendo R_α de CONSTRUCTOR_002 y su signo no queda probado aquí.

## 3. Lenguaje y alcance

B elimina el normalizador exterior de la covarianza, pero conserva el cociente τ(d²y)τ(e²y)/τ(y). No es un kernel theta libre de denominadores. Su primer término tiene Mellin clásico Γ(α)ζ(2α)l^(−2α) para Re α>1/2; el segundo es no lineal. En α=1/4 la DIFERENCIA se integra directamente para pares coprimos, mientras separar ambos términos requiere sus continuaciones.

«Signo Mellin crítico parcial» es admisible sólo si significa este parámetro α=1/4 y se conserva la distinción con el peso efectivo del nodo. No demuestra homogeneidad n^(−1/2) del kernel entero, ni cancela diagonal, gamma o polar de Q_T. Tampoco prueba una desigualdad cuadrática para coeficientes arbitrarios a partir de entradas negativas: los productos conjugado(a_d)a_e pueden cambiar de signo.

**Positivo auxiliar:** −J_α(d,e)>0 para pares coprimos y α>0 real, con cancelación exacta del término de divergencia. **Enlace con Q_T: OPEN.**

## 4. Extensión revisada a valoraciones completas de dos primos

**PROVED para primos fijos p≠q.** No se limita a una potencia de cada primo.

Para c=y^(−1/2)≥2, la comparación integral de la gaussiana decreciente y Poisson dan c−1≤τ(y)≤c. Más generalmente, δ_k=τ(k²y)−c/k pertenece a [−1,0]. La identidad algebraica

    B_y(d,e)=δ_de+
      [cδ_1/(de)−cδ_e/d−cδ_d/e−δ_dδ_e]/(c+δ_1)

vale para índices coprimos. Por tanto

    |B_y(d,e)|≤1+[c(1/de+1/d+1/e)+1]/(c−1)≤9/2<5.

Además −B_y≤τ(d²y)τ(e²y)/τ(y)≤2c/(de). Luego

    0<−τ(y)Cov_y(v_p,v_q)
       =Σ_{j,k≥1}(−B_y(p^j,q^k))
       ≤Σ_{j,k≥1}min(5,2c p^(−j)q^(−k))
       =O_{p,q}(log² c).

Para la última cota, cortar J=ceil(log_p c), K=ceil(log_q c). El rectángulo aporta ≤5JK. Cada cola se acota geométricamente por O_{p,q}(cp^(−J))+O_{p,q}(cq^(−K))=O_{p,q}(1). Como c≥2, el término constante queda absorbido por log²c.

Para y≥1, S_p(y)=Σ_j τ(p^(2j)y)=O_p(exp(−πp²y)); esto se obtiene sumando los pesos gaussianos de los múltiplos de las potencias de p, o dominando primero cada suma theta y luego la cola geométrica en j. Como τ(y)≥2exp(−πy),

    0<−τ(y)Cov_y(v_p,v_q)
       ≤S_p(y)S_q(y)/τ(y)
       =O_{p,q}(exp(−π(p²+q²−1)y)).

La desigualdad usada conserva el signo porque todos los B cruzados son negativos. Estas cotas justifican la transformada

    L_α(p,q)=−∫_0^∞ y^(α−1)τ(y)Cov_y(v_p,v_q)dy>0

para α>0 real, convergente absolutamente y holomorfa para Re α>0. En α=1/4 no requiere resta. Tonelli para el integrando positivo permite sumar TODAS las potencias y escribir L_α=Σ_{j,k}(−J_α(p^j,q^k)).

No se ha sumado sobre TODOS los primos con pesos Λ, ni se ha controlado la diagonal p=q. La constante de la cota depende de p,q y no implica uniformidad suficiente para esa suma. La extensión produce un signo Mellin estricto de interacción entre dos factores primos completos, no el signo de una forma arbitraria del nodo.

## 5. Revisión final del memo CONSTRUCTOR_004

Revisados todos los apartados, incluida la extensión de potencias y la mezcla en σ>1. **Aprobados** con la precisión de borrado comunicada al coordinador y corregida por él.

- **Lema 1 y Teorema 2:** asintótica, convergencia y signo coinciden con §§1–2 de esta auditoría.
- **Teorema 3:** para suma fija, la concavidad estricta aumenta el producto de τ al acercar ambos argumentos logarítmicos. (3,10) es más equilibrado que (2,15), lo que prueba A(3,10)>A(2,15). Es no dependencia del producto en el dominio de enteros coprimos indicado. No es por sí solo una afirmación sobre la restricción a potencias de primos, ni sobre operadores en alturas.
- **Fórmula Mellin §4:** el cambio z=k²y da el factor k^(−2α) exacto. La regularización de τ tiene residuo 1 en α=1/2 y coincide con 2π^(−α)Γ(α)ζ(2α). Los contraterminos de las dos partes son iguales para l=de; restarlos produce A=J−Z(de)^(−2α), signo y factor 2 correctos. En α=1/4 aparece exactamente 1/√(de) en ese término, mientras el kernel completo conserva el cociente no homogéneo.
- **Mezcla §7:** para α>1/2, τ(y)y^(α−1)/Z_α es probabilidad y la marginal sobre enteros no nulos es |n|^(−2α)/(2ζ(2α)). Las valoraciones primas son independientes geométricas bajo esa marginal por factorización absolutamente convergente. Covarianza total prueba la cancelación exacta de los dos cruces. Cada q_y(d) es estrictamente decreciente porque f'(x+2log d)−f'(x)<0; sus sumas r_p también lo son. La integral doble de diferencias es estrictamente positiva. Todos los segundos momentos son finitos para σ=2α>1; la identidad cuadrática de varianzas y el factor p^(−σ)/(1−p^(−σ))² son correctos. No se continúa una identidad PSD por debajo de σ=1.
- **Lema 4:** la nueva cota 3/2 mejora la 5 de esta auditoría y es correcta: −B≤c²/[de(c−1)]−c/de+1=1+c/[de(c−1)]≤3/2. No requiere que la cota inferior c/de−1 sea positiva. El mínimo con 2c/(de) conserva validez.
- **Teorema 5 y fórmula por potencias:** cortes J,K y colas son los de §4. Tonelli produce la suma positiva de A. Para J, la identidad entrada a entrada J=A+Z(de)^(−2α), la suma positiva finita de A y las dos series geométricas garantizan convergencia absoluta. El término explícito es exactamente Z_α/[(p^(2α)−1)(q^(2α)−1)] con signo menos en A. En α=1/4 aparecen los denominadores √p−1 y √q−1; no se infiere por ello convergencia sobre todos los primos.

**Precisión sobre borrado.** Quitar índices del kernel fijo conserva sus signos ya probados. Cambiar la ley gaussiana eliminando múltiplos de un primo es otra operación: el signo de anticorrelación de esa ley modificada no está probado aquí. El memo y la síntesis deben conservar esa diferencia; no presentar la herencia como un teorema para la medida alterada.

**SYNTHESIS, segunda ronda: aprobada.** Comunica un resultado auxiliar firmado en todas las escalas y en Mellin α=1/4 sin resta coprima. Conserva diagonal, mismo primo, polar, dominio efectivo y enlace Q_T como pendientes. Positividad de A entrada a entrada no es PSD ni paga por sí sola ningún modo del nodo. Con estos límites, todo lo etiquetado PROVED queda sostenido por las pruebas revisadas.
