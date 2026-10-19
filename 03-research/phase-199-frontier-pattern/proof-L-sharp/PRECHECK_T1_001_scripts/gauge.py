# canonical gauge projection Π (U_001 Thm U.2.1): 𝒢̄ = closure{(1−P_1)ψ̂ : ψ ∈ L²_even(−1,1), ∫ψ=0}, ψ̂(t)=∫ψ(y)e^{−2πiyt}dy
# basis ψ = P̄_j (j=2,4,..,J), ψ̂_j(t) = (−1)^{j/2}√(2(2j+1)) j_j(2πt). ‖Πρ‖² = ‖ρ‖² − bᵀG⁻¹b (two-sided even L²(|t|>1)).
import numpy as np
from scipy.special import spherical_jn
from scipy.integrate import quad
def ghat(j,t): return (-1)**(j//2)*np.sqrt(2*(2*j+1))*spherical_jn(j,2*np.pi*t)
def project(t,rho,J,wfun_mu=None):
    js=list(range(2,J+1,2)); n=len(js)
    x,wq=np.polynomial.legendre.leggauss(400); x=(x+1)/2; wq=wq/2
    G=np.eye(n)-2*np.array([[np.sum(wq*ghat(i,x)*ghat(j,x)) for j in js] for i in js])
    Gt=np.array([ghat(j,t) for j in js])
    b=2*np.trapz(Gt*rho,t,axis=1)
    coef=np.linalg.solve(G,b); rem=b@coef        # ‖(1−Π)ρ‖² (two-sided)
    prho=rho-coef@Gt
    return dict(rem2=rem,condG=np.linalg.cond(G),prho=prho,coef=coef)
