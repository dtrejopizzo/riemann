# Ninguna constante de autoenergía repara la parte finita ciclotómica

Estado: **PROVED**, con revisión independiente de la prueba y de su alcance. Se estudia una forma auxiliar, no el signo de la forma completa.

## Cotejo

1. Antecedentes: `ROUND_095_A.md`, especialmente §§2–4, y el registro «Corte ciclotómico dependiente del índice» en la Parte V del índice maestro. El primero demuestra un valor negativo de J_sc; no demuestra que J_sc/A carezca de cota inferior. El segundo admite la libertad de cambiar la escala constante del corte.
2. Afirmación nueva: inf_(β∈K_Z, β≠0) J_sc(β)/A(β)=−infinito, donde K_Z es el portador entero. Esto excluye J_sc+cA PSD para toda constante real c, no sólo para c=0.
3. Operación: ponderar las dilataciones primas por 1/p, deteniendo la suma cuando su masa recíproca alcanza uno. Así A queda acotada mientras la escala mínima de los cruces tiende a infinito. Se justifica el paso de coeficientes racionales a enteros. La puerta independiente aprobó únicamente esta obstrucción de clase.
4. Conexión: cambiar el corte ε por λε, con λ>0 fijo, cambia la parte finita a J_sc−Alogλ. El resultado impide usar cualquiera de esas partes finitas como pieza PSD universal en una separación de la forma completa. No excluye otros contratérminos ni una compensación conjunta con el resto.

## 1. Formas y datos ya probados

Usar el test b=b_6 y las dilataciones D_p de `ROUND_095_A.md`. Denotar por K_R el núcleo real de las restricciones Σ_jβ_j=0, Σ_jjβ_j=0 y Σ_jβ_jv_r(j)=0 para cada primo r, siempre sobre sucesiones de soporte finito; K_Z es su subconjunto de sucesiones enteras, el portador K de 095-A. Para sucesiones de soporte finito, poner

    G(u,v)=Σ_(i,j≥1)gcd(i,j)u_i v_j,    A(u)=G(u,u),
    B(u,v)=−Σ_(i,j≥1)gcd(i,j)u_i v_j log((i+j)/gcd(i,j)),
    J_sc(u)=B(u,u).

La identidad gcd(i,j)=Σ_(d|i,d|j)φ(d) da

    A(u)=Σ_d φ(d)(Σ_(d|i)u_i)²>0 para u≠0 de soporte finito.

En efecto, si L es el mayor índice no nulo, el sumando d=L es positivo. Por tanto el cociente J_sc/A está bien definido.

Los datos de 095-A son

    A(b)=14,    J_sc(b)<3,
    A(D_p b)=14p,    J_sc(D_p b)=pJ_sc(b),
    G(D_p b,D_q b)=14 para primos distintos p,q>6,
    B(D_p b,D_q b)=−14log max(p,q)+E_pq,
    |E_pq|<1152 para esos mismos primos.

La igualdad de G usa la misma identidad gcd(pi,qj)=gcd(i,j) ya probada. Todos los cruces y diagonales son de las formas completas A y J_sc; no se omiten términos.

## 2. Selección finita de primos con masa recíproca controlada

Se necesita sólo la divergencia elemental Σ_(p primo)1/p=infinito. Una prueba suficiente es la siguiente. Si esa suma fuera finita, para todo N,

    Σ_(n≤N)1/n ≤ ∏_(p≤N)(1−1/p)^(−1)

estaría uniformemente acotada: el logaritmo del producto es a lo sumo 2Σ_(p≤N)1/p, pues −log(1−x)≤2x para 0≤x≤1/2. La desigualdad del producto se obtiene expandiendo un número finito de series geométricas positivas; incluye todos los enteros hasta N. Contradice la divergencia de la suma armónica. Eliminar un número finito de primos conserva la divergencia.

Fijar un entero Q>6. Tomar, en orden creciente, primos p>Q hasta que la suma de sus recíprocos alcance uno por primera vez; sea S_Q ese conjunto finito. Definir

    s=Σ_(p∈S_Q)1/p,    r=Σ_(p∈S_Q)1/p²,
    u=s²−r=Σ_(p≠q en S_Q)1/(pq).

Por la regla de parada,

    1≤s<1+1/Q<2,
    r≤s/Q<2/Q,
    1/2<u<4.

La cota inferior usa Q>6 y s²≥1. La suma que define u cuenta pares ordenados.

## 3. Autoenergía acotada y parte finita sin cota inferior

Poner

    γ_Q=Σ_(p∈S_Q)(1/p)D_p b.

Es un test racional no nulo de K_R; los soportes de las dilataciones son disjuntos. Al expandir ambas formas, con todos los pares ordenados,

    A(γ_Q)=14(s+u),    0<A(γ_Q)<84,
    J_sc(γ_Q)≤J_sc(b)s+(1152−14log Q)u.

Si log Q>100, el coeficiente de u es negativo. Usando s<2 y u>1/2,

    J_sc(γ_Q)<6+(1152−14log Q)/2
               =582−7log Q<0.                         (NEG)

Como A(γ_Q)<84 y el numerador acotado en (NEG) es negativo,

    J_sc(γ_Q)/A(γ_Q)<(582−7log Q)/84 → −infinito.

Para obtener tests enteros, multiplicar γ_Q por el entero M_Q=∏_(p∈S_Q)p. El vector β_Q=M_Qγ_Q es no nulo, entero y satisface las mismas restricciones lineales. Ambas energías se multiplican por M_Q², por lo que su cociente no cambia. Se concluye

    inf_(β∈K_Z, β≠0) J_sc(β)/A(β)=−infinito.

No se fija una dimensión ni se usa un barrido numérico: cada Q define un test finito por una regla exacta, cuya terminación quedó probada.

## 4. Toda corrección cA y toda escala constante del corte

Sea c real fijo y C=max(c,0). Elegir un entero Q con log Q>100+12C. Por (NEG) y A(γ_Q)<84,

    J_sc(γ_Q)+cA(γ_Q)
      ≤J_sc(γ_Q)+C A(γ_Q)
      <582−7log Q+84C<−118.

Después de multiplicar por M_Q² se obtiene un test entero negativo de J_sc+cA. Ninguna constante real c produce PSD en todo el portador.

El regularizador ya registrado satisface, para cada test finito fijo,

    Q_ε(β)=−A(β)log ε+J_sc(β)+o(1).

Para λ>0 fijo, sustituir ε por λε y mantener la sustracción A log ε da

    lim_(ε↓0)[Q_(λε)(β)+A(β)log ε]
       =J_sc(β)−A(β)logλ.

Estas son exactamente correcciones cA con c=−logλ. Por tanto ninguna elección constante de la escala del corte convierte esa parte finita en una forma PSD sobre todo el portador.

## Resultado

**Qué se probó:** J_sc no está acotada inferiormente por ninguna constante por A, incluso sobre tests enteros que anulan los dos momentos y todas las filas de valuaciones. La negatividad de 095-A no se repara eligiendo otra constante de autoenergía o una escala fija diferente del mismo corte.

**Qué falló y por qué:** con masa recíproca aproximadamente uno, las diagonales y A permanecen acotadas, pero los cruces de J_sc contienen un término negativo proporcional al logaritmo de la escala mínima. Esta es una obstrucción a la clase de reparaciones cA, no a todo contratérmino.

**Siguiente paso concreto:** una reapertura debe dar una compensación distinta, dependiente de los cruces y con identidad exacta para la forma completa. Esta prueba no la proporciona ni afirma que exista. No se decide el signo de a ni del resto a−J_sc, no se refuta J_sc≤a y no se excluyen escalas dependientes del test. No se ha dado un paso positivo sobre a al que aplicar la batería de falsificadores del objetivo; se ha refutado una reparación auxiliar. El signo global permanece abierto.
