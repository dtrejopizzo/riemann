# Diagnósticos auxiliares de la segunda ronda

2026-10-18. **NUMÉRICO exploratorio, no certificado.** No se usa en ninguna
prueba de ANTICORRELATION_003 ni CONSTRUCTOR_004.

Se evaluaron momentos gaussianos con corte n²πy≤45 para orientar la prueba
de concavidad de log(θ−1)(e^x). El signo observado fue negativo; la nota003
lo sustituye por una prueba analítica uniforme. Se probaron también pequeñas
muestras de leyes con un primo excluido: no mostraron violación robusta de
la anticorrelación puncturada. Esto NO demuestra herencia ni especificidad.

Se comprobó una extensión tentadora del signo cruzado a orden de matrices:

    D_y(d,e)=y^(-1/2)(gcd(d,e)-1)/(de)-τ(y)C_y(d,e).

Con índices {2,3,5,7}, y=0.001, diagonalización en doble precisión dio un
mínimo cercano a -0.04752. Por tanto la muestra no apoya D_y PSD. No se
formula ni se usa esa dominación como lema; el test no es un NO-GO certificado.
No confundir positividad de entradas coprimas de -τC con positividad de forma.

Reproducción del diagnóstico de matrices, con Python3/numpy:

```python
import math
import numpy as np
indices=[2,3,5,7]
y=0.001
nmax=int(math.sqrt(45/(math.pi*y)))+1
def tau(k):
    return 2*sum(math.exp(-math.pi*y*k*k*n*n)
                 for n in range(1,nmax+1))
z=tau(1)
a={d:tau(d) for d in indices}
D=np.array([[(math.gcd(d,e)-1)/(d*e*math.sqrt(y))
             -tau(math.lcm(d,e))+a[d]*a[e]/z
             for e in indices] for d in indices])
print(np.linalg.eigvalsh(D))
```

Estos tests sólo impiden extrapolar las pruebas escalares a una desigualdad
operatorial no demostrada. No alteran el estado de O1.
