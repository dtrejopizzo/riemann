# El salto en el corte neutral es positivo y menor que la raíz

**Estado: PROVED, con revisión independiente de la orientación del salto y del ahorro bajo raíz.**

En la notación de 386, al subir el umbral y a través de un primo p con v=log(x/p²)=κ log z y κ en un compacto interior de (0,1), el salto de W es

    W(p)−W(p−) ∼ J (x/p)/log(x/p) >0

uniformemente. En particular hay un único cruce en la banda de 386 (posible meseta de valor cero). El error al retirar el grupo elegido resulta

    |W(y)| ≤ (2J exp(−1/4)+o(1)) √x exp(E/4)/L
            = √x L^(exp(γ)/2−1+o(1)) = o(√x).

En la primera desigualdad basta tomar un lado del salto, sin interpolación.

**Cofactor del salto.** Los términos que dejan W tienen mayor primo exactamente p. Quitarlo cambia el signo, de modo que el salto es la suma firmada en escala X=x/p de m con todos sus primos en (z,p), incluidos m=1 y el peso g(log(X/m)). Completar hasta todos los m sin primos ≤z da S^*(X;z), de módulo ≪X exp(−c log X/log log X) por el contorno congelado de 384, ya que log X∼L/2. De lo añadido, los m con un primo q≥p y algún otro factor tienen m≥pz=X z^(1−κ), luego masa absoluta ≪X exp(−c(log z)²) por la cola de 375. Los restantes son los primos q≥p, que aportan signo menos. Aquí p=X exp(−v), y la masa de primos menores que p cuesta ≪X exp(−c v²); se puede completar a todos los primos a precisión o(X/log X). El PNT y la gaussiana dan para éstos (J+o(1))X/log X, por la sustitución de 379. Restar el saldo añadido da el salto positivo anunciado. Los dos márgenes gaussianos son uniformes al separar κ de 0 y de 1.

**Localización del primo del cruce.** En el intervalo v=E/2−1/2±1 de 386 todos los saltos son positivos al aumentar y. Los valores pre y post del salto del cruce son O(X/log X), por signos y el equivalente uniforme. El perfil aditivo de 386 rige para ambos, incluido el límite izquierdo con el mismo v por uniformidad. Esto fuerza v=E/2−1/2+o(1) en el primo del cruce. Si hay meseta cero, basta un extremo. Sustituir X=√x exp(v/2), log X∼L/2. Mertens y log z=2log L dan la segunda expresión como cota superior con exponente indicado, estrictamente menor que raíz porque exp(γ)<2.

**Registro de revisión.** Al aumentar y se retiran términos de signo −μ(m), por lo que W(p)−W(p−) tiene signo +μ(m) en la suma del cofactor. La suma completa S^*(X;z) es pequeña, y lo añadido para completarla contiene primos solos con signo negativo: restarlos da +JX/log X. Los otros términos añadidos tienen m≥pz=Xz^(1−κ); su cola O(X exp(−c(log z)²)) es o(X/log X) uniformemente si κ se separa de1. La omisión de primos q<p es igualmente o(X/log X) al separar κ de0. Todos los saltos de la banda son por tanto estrictamente positivos para x grande, de modo que hay un único cruce salvo una meseta cero. Cada lado tiene módulo a lo sumo el salto, sin interpolar masas. La localización aditiva de386 en el primo del cruce da exp(v/2)=exp(E/4−1/4)(1+o(1)); junto con log X∼L/2 produce la constante2J exp(−1/4) anunciada. El ahorro √x L^(exp(γ)/2−1+o(1)) es o(√x) porque exp(γ)<2.

**Alcance.** Los dos productos finitos adyacentes del corte 386 encierran el saldo verdadero, con separación o(√x). La orientación se obtiene de W creciente: antes del cruce C=S−W≥S, después C≤S. Se transfiere así cualquier estimación unilateral a escala raíz con error aditivo o(√x); falta estimar alguno de esos productos.
