# Fase 124 — primer ataque a la exclusión aritmética del primer contacto

Fecha: 2026-09-09. Objetivo: investigar la vía directa con menos
dependencias. No requiere terminar A, crear otra teoría geométrica ni
editar los papers.

## 1. Blanco operativo

Partir de un hipotético primer contacto T_* > log 2 y un estado primitivo
no nulo F de paridad definida. Se dispone de q_(T_*) >= 0 y de la ecuación
variacional de radical sobre el dominio primitivo. Hay que demostrar que
esa situación es incompatible con los datos aritméticos.

En la ruta R/S, las obligaciones pendientes son:

1. **Anular la fuente Tate.** El corriente entrante existente cumple
   L_(T,-)^gr(F) = -Z_(T,+) r_eta, donde
   r_eta(t) = c(exp(t/2) + eta exp(-t/2)), eta = +/-1.
   La transmisión crítica fuerza c=0 por P122.019/P122.029. Debemos
   demostrar la transmisión, o directamente c=0, desde la ecuación
   aritmética del estado.
2. **Excluir el estado homogéneo.** Después de c=0, demostrar la relación
   entre canales necesaria para aplicar la rigidez de primera celda.
   La candidata es (E_(p,T)-E_(q,T)) h_F = 0 para dos primos activos
   distintos, con los dominios y condiciones de P122.020.

La energía conocida

```
E_eff(F) = ||(E_(q,T)-E_(p,T)) h_F||^2 / log(q/p)
```

no necesita recalcularse. Una extensión armónica tiene flujo constante,
que puede ser distinto de cero. La nueva prueba debe controlar el flujo.

## 2. Primera candidata: variación conjunta de la fuente Gamma–Euler

Usar el sistema literal de fase 120, conservando en conjunto los estados
de retardo primo, los estados del oscilador Gamma y el perfil coherente de
grado. No variar independientemente estados que ya están determinados
por F.

El primer cálculo buscará una identidad de borde obtenida al variar la
fuente F y propagar esa variación a todos los estados mediante sus
ecuaciones. Las variaciones se corregirán para mantener las dos
condiciones primitivas. El signo de q en el primer contacto permite usar
su ecuación de radical; no permite suponer el signo de términos de borde
separados.

Orden concreto:

1. Escribir los operadores que transportan la variación de F a cada
   estado y el término de grado. Trabajar inicialmente en un núcleo
   regular con soporte interior y declarar su relación con el dominio
   cerrado del minimizador.
2. Hacer la variación de la acción FIRMADA completa. Mantener los términos
   de borde de las traslaciones truncadas, de Gamma y de las correcciones
   Tate; no eliminar ninguno por analogía con un operador local.
3. Probar el paso al estado de primer contacto. Si se regulariza F,
   estimar el residuo de la ecuación y la convergencia en la topología
   necesaria para el término de borde. No suponer H^(1/2) en este paso.
4. Determinar si la identidad contiene una relación adicional que fuerce
   c=0 o el flujo cero. Señalar la propiedad aritmética exacta que la
   produce. Si solo recupera la ecuación de radical o una factorización
   equivalente, no cuenta como cierre de una obligación.

Este es un candidato de investigación, no una identidad ya demostrada.
No basta que la acción sea estacionaria: un punto estacionario de una
acción firmada no tiene por ello todos sus términos positivos o nulos.

## 3. Resultados de la primera tentativa y decisión

| Resultado | Acción siguiente |
|---|---|
| Se obtiene c=0 con prueba válida en el dominio del minimizador | Conservar esa prueba y concentrar la siguiente tarea en el estado homogéneo; no seguir buscando regularidad más fuerte innecesaria. |
| Se obtiene una ley que fuerza el pegado bajo c=0 | Conservarla y atacar exclusivamente la anulación Tate. |
| Se excluye F directamente sin R/S | Usar esa demostración; R/S no se agregan como obligaciones extra. |
| Solo se reproduce la ecuación de radical o el detector conocido | Registrar brevemente dónde desaparece la información; no multiplicar nuevas versiones de la misma candidata. |
| Hay una obstrucción concreta de dominio o un contraejemplo | Delimitar la clase refutada y diseñar una modificación que cambie esa hipótesis. No declarar imposible la vía entera. |

Un resultado solo para dos primos es un test de la candidata, no una
exclusión para todas las ventanas. La posterior prueba debe incluir todos
los canales activos, ambos sectores de paridad y los umbrales de
nacimiento pertinentes.

## 4. Alternativa dentro de la misma fase

Si la variación no produce una ley nueva, atacar directamente la
desigualdad firmada sobre el sistema completo. La identidad

```
q_T(F) = ||X_T F||^2 - ||Y_T F||^2
```

permite formular una cota de dominación. El avance tendría que ser una
estimación aritmética que la demuestre, con constante suficiente y dominio
completo. Construir un operador cuya contractividad sea equivalente a
la cota no la prueba.

Que un objetivo tenga fuerza-RH no es un veto. La distinción es entre
demostrar la desigualdad desde los datos y asumirla en otra notación.
Consultar los no-go existentes solo para comprobar sus hipótesis exactas.

## 5. Cierre de la ruta

La cadena de cierre será:

```
base certificada + primer contacto alcanzado
  + nueva ley aritmética demostrada
  -> exclusión de una primera pérdida de signo
  -> q_T >= 0 para todas las ventanas finitas
  -> dominio suficiente del criterio de Weil
  -> RH.
```

El último paso exige usar las normalizaciones, densidad y continuidad del
criterio correspondiente; no exige construir una intersección geométrica
de A. No hace falta un margen positivo uniforme en T si se demuestra el
signo en cada ventana y la clase de tests obtenida ya es suficiente.

## 6. Disciplina de trabajo

- No repetir el certificado log 2, los detectores de fase 121, la energía
  de dos primos ni la identificación del espacio crítico de borde.
- No deducir transmisión de una regularidad subcrítica ni de un cálculo
  que impone la propia condición de transmisión.
- No descartar una prueba analítica porque trabaje sobre minimizadores;
  sí exigir una demostración independiente de cada consecuencia usada.
- No confundir una identidad global firmada con un teorema de signo.
- Mantener como máximo una candidata principal y una alternativa.
- Guardar únicamente las pruebas, obstrucciones y cálculos que cambien
  una obligación. No modificar papers ni convertir cada paso en una
  memoria extensa.

Primer entregable pendiente: la variación conjunta y su identidad de
borde, con dominio justificado y un veredicto sobre su capacidad para
anular la fuente Tate o el flujo. Ninguna de esas anulaciones queda
probada por abrir esta fase.

## 7. Continuación seleccionada (2026-09-12)

Tras P124.013--014 la obligación de Gate R se enuncia sin minimizador:

```
Sigma(T) = B_T - X_T^* L_T^{-1} X_T >= 0   para toda ventana T < T_q,
```

con `X_T` la columna del colar `rho_{\pm,T}` (P124.005) y `B_T` el bloque
Tate del formulario de Weil completo (P124.013 (2.3)).  Es una desigualdad
`2x2` sobre objetos explícitos, en el rango donde `L_T > 0`.

El falsador `Xi_a` la viola antes de su primer contacto, y `zeta` no la violó
en el rango explorado.  La separación entre ambos es la unimodularidad de las
raíces locales (`p^{-1/2}` frente a `p^{-1/2\pm a}`).  Por lo tanto la única
candidata principal admisible sigue siendo una ley de unitariedad local, ahora
con la obligación de producir **simultáneamente** Gate R (vía `Sigma`) y
Gate S; el reparto "R blando, S aritmético" queda cerrado.
