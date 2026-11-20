# LINK_010 — Regularidad necesaria para una compresión de D_n

2026-10-19. Constructor principal. **PROVED, revisión independiente favorable en AUDIT_010.md.**
No se construye el enlace Q_T ni se descarta una compresión general.

## Clase y consulta previa

Consultados índice de rutas (incluido archivo06), corpus209, grid maestro y
crucigrama: no se reutiliza la exclusión de compresiones V_n como si cubriera
D_n. La pregunta nueva conserva las amplitudes n^(−s/2) y añade una hipótesis
explícita de regularidad espectral sobre vectores aritméticos finitos. La prueba
de009 sólo daba distancias que ahora tienden a cero; aquí se calcula su tasa.
No se usa un teorema de extensión positiva ni se supone que compresiones
hereden una ley de semigrupo.

## 1. Incrementos de orden exacto en una sucesión

Usar H_alpha de007, s=2alpha en(0,1) y kappa>0. Sea A no nulo en el álgebra
finita de observables de divisibilidad, centrado por E_1 A=0. Sea S el conjunto
finito de primos que aparecen en sus índices y L un entero positivo par divisible
por todos ellos (por ejemplo 2 veces su producto). Tomar

    n_k=1+kL,  m_k=n_k+L,  h_k=log(m_k/n_k).

Entonces n_k,m_k son coprimos entre sí y con S. Dividir por ellos no cambia
las valuaciones de S: D_n A=X_n A y D_m A=X_m A. Si a=E_s|A|²>0,

    E_s|D_n A−D_m A|²
      =a[n^(−s)+m^(−s)−2(nm)^(−s)].

La positividad de las dos componentes de la norma de007 implica

    liminf_k ||D_m A−D_n A||² / h_k^s >= 2 kappa a/L^s >0.       (1)

En efecto n h_k→L, m/n→1, mientras n^s(nm)^(−s)→0. No se necesita
calcular la componente gaussiana: no puede restar a la cota.
La estricta positividad de a resulta de la independencia lineal de los
indicadores finitos en la ley P_s, ya probada en005.

## 2. Teorema de regularidad necesaria

Supónganse mapas acotados fijos J:H_alpha→K y P:K→H_alpha, un grupo
unitario fuertemente continuo U(t)=exp(itB), y

    P U(log n)J=D_n,   n>=1.                                    (2)

No se exige P=J*, ni J isométrico. Para todo A anterior, la medida espectral
positiva mu_A(E)=||1_E(B)JA||² satisface necesariamente

    integral |lambda|^s dmu_A(lambda)=infinito.                  (3)

Prueba. Si ese momento fuera finito, el teorema espectral daría

    ||[U(h)−I]JA||²/h^s
      = integral |exp(ih lambda)−1|²/h^s dmu_A(lambda) →0.

Se aplica convergencia dominada: para0<s<2,
|exp(ix)−1|²<=4|x|^s y el cociente puntual tiende a cero.
Pero unitariedad y(2) implican

    ||D_m A−D_n A|| <= ||P|| ||[U(log(m/n))−I]JA||,

en contradicción con(1). Esto prueba(3).

Equivalente: JA no pertenece a Dom(|B|^(s/2)) para NINGÚN observable
aritmético finito no nulo centrado. En alpha=1/4, se excluye el momento
espectral absoluto1/2, o dominio Dom(|B|^(1/4)). Es esencial no confundir
el orden del momento con la potencia del dominio.

## 3. Alcance para el enlace buscado

Se descarta la clase de enlaces(2) que además lleve siquiera uno de esos
observables a un vector con momento espectral s finito; en particular,
una identificación que los lleve todos a vectores espectralmente suaves.
El mero grupo C0 NO exige ese momento: no hay contradicción para una
compresión con imágenes suficientemente irregulares. La compresión general
de D_n continúa OPEN.

Tampoco se ha probado que un mapa de los tests suaves de Q_T deba invertir
esta correspondencia o enviar un observable A de este tipo a un vector suave.
Tal afirmación requiere un mapa concreto y su dominio. No se usa este
resultado para excluir todas las representaciones de Q_T ni para pagar gamma,
peine o polo. D permanece OPEN; goal íntegro activo.
