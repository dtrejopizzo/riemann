# Doc 131 -- Phase 44: Hodge-Witt e inercia visible

**Programa:** Hipotesis de Riemann -- ruptura creativa posterior a Phase 43.  
**Fecha:** junio 2026.  
**Autor:** David Alejandro Trejo Pizzo + Codex.  
**Estatus:** documento de arranque. No prueba RH. Define un marco nuevo, prueba lemas internos y fija puentes/deseos con estatus explicito.

---

## 0. Contrato de la nueva etapa

La libertad matematica vive en la definicion. La disciplina vive en el teorema.

Usaremos cuatro etiquetas obligatorias:

- **[DEFINICION-NUEVA]** libertad total: se define un objeto, una categoria, una algebra, una geometria.
- **[TEOREMA]** probado dentro del marco declarado.
- **[PUENTE]** conexion con zeta/RH, con su estatus real.
- **[DESEO]** objetivo no probado. Un deseo no es una verguenza; es el motor declarado.

Regla de oro de Phase 44: ningun resultado se llamara "hacia RH" si solo reempaqueta positividad de Weil, continuidad uniforme, Hadamard, Connes-Consani, Deninger, de Branges, Lee-Yang, Li, Jensen, Nyman-Beurling o una equivalencia conocida. Si el puente es condicional, se dice condicional.

---

## 1. Diagnostico operativo: que hipotesis hay que romper

Las fases 0--43 dejaron un mapa muy preciso. El muro no es falta de datos; es falta de un objeto que lea **inercia** sin ponerla como input.

Tabla de diseno:

| No-go / muro | Hipotesis que lo alimenta | Ruptura propuesta |
|---|---|---|
| MW-1, positividad de Weil equivale a RH | el objeto final es una positividad escalar | cambiar el codominio a una clase de Witt/inercia; positividad sera consecuencia, no definicion |
| MW-2, propagacion desde Re(s)>1 | se intenta empujar informacion aritmetica de una frontera a la franja | construir un objeto de dos bordes, donde primos y arquimediano son fronteras simultaneas |
| MW-3, Hasse-Minkowski infinito | positividad local implica positividad global | no pedir positividad local; pedir una ley de frontera en el grupo de Witt |
| MW-4, signo equivocado | herramientas incondicionales dan cotas inferiores | buscar un mecanismo de **exclusion de inercia negativa**, no una cota inferior de valor |
| MW-7 / Hadamard | las propiedades verificables no ven posiciones de ceros | exigir test NC4: bajo `no RH`, el objeto existe y falla visiblemente |
| Phase 43 / Deninger | la polarizacion usa el analogo de Hasse | exigir una polarizacion pre-RH: definida antes de saber donde estan los ceros |

**Decision de Phase 44.** Abandonamos como objeto primario la desigualdad `Q >= 0`. El nuevo objeto primario es una **clase de defecto en un grupo de Witt**, porque la inercia es lo que todos los programas necesitaban y ninguno podia leer sin circularidad.

---

## 2. La nueva algebra: objetos Hodge-Witt con falla visible

### 2.1. Objeto Hodge-Witt finito

**[DEFINICION-NUEVA]** Un **objeto Hodge-Witt finito** es una quintupla

`X = (V, q, L, F, B)`

donde:

1. `V` es un espacio vectorial real de dimension finita.
2. `q: V x V -> R` es una forma bilineal simetrica no degenerada.
3. `L: V -> V` es un operador de Lefschetz abstracto.
4. `F` es una filtracion finita creciente, llamada filtracion aritmetica.
5. `B` es un dato de borde: una descomposicion formal `B = B_infty - sum_p B_p`, no necesariamente positiva localmente.

El **defecto de inercia** de `X` es

`Def(X) = [q|P(X)] in W(R)`,

donde `P(X)` es el subespacio primitivo definido por `L` y `W(R)` es el grupo de Witt real. Identificamos `W(R) ~= Z` por la signatura.

### 2.2. Polarizacion visible

**[DEFINICION-NUEVA]** Una familia `X_theta` de objetos Hodge-Witt, parametrizada por deformaciones `theta` de los ceros, tiene **polarizacion visible** si:

1. `X_theta` existe para deformaciones on-line y off-line.
2. La definicion de `(V,q,L,F,B)` no usa como input la conclusion "todos los ceros estan en la recta".
3. Si aparece un paquete off-line `rho = 1/2 + b + i gamma`, con `b != 0`, entonces existe un vector primitivo `v_rho in P(X_theta)` tal que `q(v_rho,v_rho) < 0`.
4. La falla no es "el espacio deja de existir"; la falla es un vector negativo visible.

Esto es el test NC4 convertido en axioma de diseno.

### 2.3. Puente de frontera

**[DEFINICION-NUEVA]** Una familia Hodge-Witt tiene **ley de frontera explicita** si existe una identidad formal

`partial Def(X) = B_infty - sum_p B_p`

en un grupo abeliano de bordes `A`, compatible con truncaciones finitas y estable por agregar sumandos hiperbolicos.

La palabra importante es **formal**: no se exige positividad local de `B_p`. Phase 6 ya mostro que eso falla.

---

## 3. Teoremas internos: pequenos, duros y utiles

### Teorema 1 -- Ceguera de los valores escalares

**[TEOREMA]** Ningun invariante que factorice solo por la traza de una forma simetrica real puede decidir el indice negativo.

**Prueba.** En `R^2`, las formas

`q_0 = diag(1,1)` y `q_1 = diag(3,-1)`

tienen la misma traza, `tr(q_0)=tr(q_1)=2`. Pero `neg.ind(q_0)=0` y `neg.ind(q_1)=1`. Por lo tanto cualquier invariante que vea solo la traza toma el mismo valor en ambas y no puede decidir el indice negativo. QED.

**Lectura.** Este es el esqueleto algebraico de P43: el valor/traza es autonomo; la inercia no.

### Teorema 2 -- La clase de Witt si lee inercia

**[TEOREMA]** Sea `q` una forma simetrica no degenerada sobre un espacio real de dimension fija `n`. Su clase de Witt, junto con `n`, determina su indice negativo.

**Prueba.** Por la ley de inercia de Sylvester, `q` es congruente a `diag(1,...,1,-1,...,-1)` con `p` signos positivos y `m` negativos. La clase de Witt real es la signatura `sig(q)=p-m`. Como `n=p+m`, se obtiene

`m = (n - sig(q))/2`.

Luego `neg.ind(q)=m` queda determinado por `([q],n)`. QED.

**Lectura.** La inercia no se lee en valores escalares tipo traza, pero si en el codominio correcto: `W(R)`.

### Teorema 3 -- Necesidad de falla visible

**[TEOREMA]** En este marco, una polarizacion que deja de estar definida para toda deformacion off-line no puede ser una prueba no circular de RH.

**Prueba.** Por definicion, una polarizacion visible exige existencia tanto on-line como off-line y falla por vector negativo visible. Si la estructura solo existe en el mundo on-line, entonces su existencia ya contiene la conclusion que se queria probar: no separa "RH implica estructura" de "estructura implica RH". Por lo tanto falla el criterio de polarizacion visible. QED.

**Lectura.** Esto formaliza la leccion de Phase 43: no basta con "si el espacio es Kahler-Riemann entonces hay positividad"; hay que construir el espacio antes de saber RH.

### Teorema 4 -- Puente Hodge-Witt condicional a RH

**[TEOREMA / PUENTE CONDICIONAL]** Supongamos que existe una familia Hodge-Witt visible `X_zeta` asociada a la funcion zeta, con estas propiedades:

1. `X_zeta` esta definida sin asumir RH.
2. La positividad de Hodge-Witt vale para todo vector primitivo: `q(v,v) >= 0` para `v in P(X_zeta)`.
3. Cada paquete off-line produce un vector primitivo negativo visible, como en 2.2(3).

Entonces RH es verdadera.

**Prueba.** Si `no RH`, existe un paquete off-line. Por visibilidad, hay un vector primitivo `v_rho` con `q(v_rho,v_rho)<0`. Esto contradice la positividad primitiva de (2). Luego no hay paquetes off-line. QED.

**Estatus.** El teorema es correcto, pero el puente es condicional. Lo no probado es la existencia de `X_zeta` con definicion zero-independiente y positividad primitiva externa. Este es exactamente el punto dificil.

---

## 4. La conjetura nueva, formulada sin falsa victoria

### Conjetura 131.A -- Polarizacion Hodge-Witt pre-RH

**[DESEO]** Existe una familia Hodge-Witt `X_zeta` asociada a `Spec Z` tal que:

1. Se construye desde el espacio desnudo: flujo, primos, borde arquimediano, filtracion aritmetica.
2. No usa la localizacion de los ceros para definir `q`, `L`, la metrica transversal ni la medida.
3. Su defecto `Def(X_zeta)` esta definido en `W(R)` antes de imponer RH.
4. Bajo `no RH`, el objeto no colapsa: aparece una clase negativa visible.
5. La ley de frontera explicita recupera la formula explicita de Weil como sombra escalar.

**[PUENTE]** Si ademas se prueba positividad Hodge-Witt primitiva por una razon geometrica externa, entonces Teorema 4 da RH.

**[DESEO honesto]** La dificultad no es escribir la conjetura. La dificultad es construir una polarizacion que no copie el patron de Deninger-eliptica, donde la metrica usa Hasse como input.

---

## 5. Tres rutas de trabajo, ordenadas por riesgo

### Ruta I -- Toy model de un paquete off-line

**Objetivo.** Construir `X(b,gamma)` para un unico cuadruplo off-line y verificar que el vector negativo aparece en `W(R)` con la escala correcta.

**Salida esperada.**

- [TEOREMA] Formula local: `Def(X(b,gamma)) = -2` o una clase equivalente por paquete conjugado.
- [PUENTE] Comparar con Phase 26/96: localizacion del indice negativo en `K_off`.
- [FALSADOR] Si el defecto depende de datos absorbibles como en Doc 98, la ruta muere temprano.

### Ruta II -- Morishita desnudo + polarizacion no metrica

**Objetivo.** Tomar el espacio desnudo de Morishita (flujo + orbitas + transversal profinito) y buscar una polarizacion en `W(R)` que no requiera estructura Kahler leafwise clasica.

La idea es no pedir hojas complejas. Pedir una **polarizacion de Witt sobre el complejo de bordes**:

`C^0(F) -> C^1(F) -> C^2(F)`

con una forma simetrica en cohomologia reducida. Esto rompe la hipotesis "las hojas deben ser Kahler" del no-go Deninger.

**[DEFINICION-NUEVA]** Una **polarizacion Witt-profinita** es una forma simetrica en cohomologia de un complejo de espacios profinitos filtrados que:

1. es estable por refinamiento de filtracion;
2. tiene ley de frontera explicita;
3. admite test de falla visible bajo paquetes off-line.

**[DESEO]** Probar un teorema de indice tipo Hodge para esta polarizacion, no desde Kahler sino desde exactitud/profinitez/filtracion.

### Ruta III -- Categoria de bordes y exact triangle aritmetico

**Objetivo.** Construir una categoria triangulada `D_Ari` con un triangulo formal

`Finite primes -> Archimedean boundary -> Zero cohomology ->`

y una forma simetrica functorial en el termino de cohomologia.

**[PUENTE]** La formula explicita seria la traza del borde de este triangulo. RH no seria una positividad de la traza; seria la desaparicion de la parte negativa de la clase de Witt del termino medio.

**[DESEO]** Encontrar el axioma que fuerza `Def(X_zeta)=0` sin convertirlo en RH por definicion.

---

## 6. Falsadores obligatorios

Una Phase 44 sana tiene que poder morir. Estos son los falsadores:

1. **Falsador F1 -- absorcion.** Si el defecto off-line lider es absorbible en el cierre de la clase admisible, como ocurrio con `g*` en Doc 98, la ruta I no sirve.
2. **Falsador F2 -- metrica Hasse.** Si la polarizacion Witt-profinita solo se define imponiendo el analogo de `|xi|^2=q`, caemos en Phase 43: circularidad por inercia.
3. **Falsador F3 -- traza solamente.** Si el nuevo objeto solo produce numeros `T_lambda` o valores escalares equivalentes, cae por Teorema 1.
4. **Falsador F4 -- positividad local.** Si requiere `B_p >= 0` por primo, cae por Phase 6.
5. **Falsador F5 -- limite uniforme.** Si el ultimo paso es `sup_X |lambda_min(Q_X)-lambda_min(Q_infty)| -> 0`, sin estructura adicional, cae por MW-6.

---

## 7. Primeros problemas concretos

### Problema 131.1 -- Calculo Witt del cuadruplo

Construir explicitamente la forma simetrica minimal para un paquete off-line

`rho, 1-rho, conjugates`

y calcular su clase en `W(R)`. Comparar con el signo de la segunda variacion ya documentado en Phase 28 y con el indice de Pontryagin de Phase 26.

### Problema 131.2 -- NC4 para polarizaciones candidatas

Toda polarizacion nueva debe pasar el test:

- existe bajo `no RH`;
- no usa cero-localizacion como input;
- produce vector negativo visible si `b != 0`;
- no se limita a decir "la metrica no existe".

### Problema 131.3 -- Borde profinito

Definir un complejo de bordes sobre el transversal profinito de Morishita que tenga cohomologia no trivial y una forma simetrica natural. El objetivo es reemplazar "hojas Kahler" por "bordes profinitos con dualidad de Witt".

### Problema 131.4 -- Sombra escalar

Probar que la traza/sombra escalar de `Def(X_zeta)` recupera la formula explicita conocida. Si no recupera la formula explicita, el objeto no toca zeta. Si solo recupera la formula explicita y nada de inercia, no sirve.

---

## 8. Veredicto de arranque

**[TEOREMA]** Los Teoremas 1--4 son validos dentro del marco definido.

**[PUENTE]** El puente a RH es condicional a una construccion nueva: una polarizacion Hodge-Witt pre-RH con falla visible. Esto todavia no existe.

**[DESEO]** Construir esa polarizacion. Si existe, cambia el juego porque lee inercia antes de positividad. Si no existe, Phase 44 aun habra probado algo: que incluso el codominio Witt cae en el cuantificador maestro.

**Frase guia.** No buscamos otra forma positiva. Buscamos el objeto anterior a la positividad, aquel que sigue existiendo cuando RH falla y nos muestra donde sangra.

