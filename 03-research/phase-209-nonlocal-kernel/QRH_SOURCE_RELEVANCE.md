# QRH — relevancia para el contratermino de017

2026-10-19. Lectura focal por constructor y revisor independiente.
**EXTERNAL CLAIM / OPEN transfer**, no validación integral de los preprints.

## Fuentes y versiones leídas

- Shiva Kintali, *A Short Proof of the Quasi-Riemann Hypothesis*, 7Oct2026,
  27 páginas: https://shivakintali.github.io/papers/QRH.pdf .
  Thm1 afirma región libre Re s>47/48 para las familias declaradas.
- OpenAI, *The Quasi-Riemann Hypothesis*, 5Oct2026, PDF actual, 47 páginas:
  https://raw.githubusercontent.com/openai/math/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf .
  Thm1.1 afirma Re s>11/12; 7/8 es otro documento citado, no este teorema.

L74 ya registraba el segundo enfoque; se corrige la entrada desactualizada.
La formalización completa en Lean y una presunta barrera3/4 no fueron
verificadas aquí y no se usan como hechos. No se repite una ruta cerrada:
se examinan herramientas e hipótesis de estas fuentes solicitadas.

## Herramientas concretas que sí aparecen

OpenAI Prop3.1 controla un segundo momento de sumas de Möbius torcidas.
Prop5.2 y Lem5.3 completan índices cúbicos, aplican criba cuadrática y
transfieren estimaciones por inversión de Möbius e iteración. Las cotas
son superiores, promediadas sobre familias, con dependencia de derivadas
de los tests. No son una cota inferior de la forma del paper47.

Kintali Lem3–4 y §3.3 controlan un probe mediante reflexión theta y energía
balanceada. Lem7 compara probe y señal con ahorro1/4800 en el régimen
de contradicción beta_*>47/48. La comparación usa clasificación por ceros
y densidad de ceros; el numerador se controla como no nulo en Re s>11/12.
No está justificado continuar ese bootstrap hasta1/2.

Las exclusiones finitas de primos S forman parte explícita de ambos
mecanismos. Sus normas positivas o estimaciones aisladas no seleccionan
por sí solas el producto completo exigido por nuestro enlace.

## Comparación exacta con017

017 requiere, para cada ventana y cada test par polar libre,

    E_pos(F) >= (A_T-C0)||F||².

Ninguno de los lemas identificados representa este déficit mediante las
familias estimadas ni aporta una dominación con la orientación requerida.
La aplicación posible consiste en construir esa identidad aritmética;
no basta importar el enunciado de región libre o la positividad de una norma.

Incluso concediendo una estimación E(x)=psi(x)-x=O(x^theta log^B x),
theta>1/2, la integración por partes del término fluctuante involucra

    E(x)x^(-3/2)[c_F'(log x)-c_F(log x)/2].

Su estimación absoluta hasta X=e^(2T) tiene escala
X^(theta-1/2)log^B X, además del borde inferior. Para theta=11/12
es exp(5T/6), y para47/48 es exp(23T/24), con factores de test/logs.
Esto no es una fuente de signo ni una cota relativa al casi núcleo.
Es insuficiencia de esta aplicación directa, NO un NO-GO de otros enlaces.

## Resultado de la consulta

Toolbox de transferencia de cancelación potencialmente reutilizable;
no se identificó un control del contratermino017. No se integran estos
resultados externos como teoremas probados en paper47. No se cierra D,
no se crea una construcción018 y no se afirma una imposibilidad general.


## Contexto de publicación: Quanta19Oct2026

https://www.quantamagazine.org/ai-proved-the-quasi-riemann-hypothesis-what-happens-now-20261019/

Quanta distingue el manuscrito de30Sept (7/8) y el de5Oct (11/12).
Reporta formalización Lean del primero y lectura favorable por expertos;
no presenta el segundo como formalizado. Es atribución periodística:
esta sesión no ejecutó el verificador ni auditó integralmente las pruebas.
El README primario de30Sept confirma el título y el umbral7/8.
El artículo destaca la selección de una familia metapléctica y la síntesis
de técnicas existentes. No procede descartar una aplicación a D sólo
porque use herramientas conocidas; se necesita identificar su enlace.
La extrapolación cuantitativa solicitada se analiza por separado en
QRH_EXPONENT_MAP.md: lema de réplicas probado, mejora crítica OPEN.
