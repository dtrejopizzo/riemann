from mpmath import mp,mpf,pi,sqrt,exp,log,factorial
mp.dps=50
def fuchs(mu,n=4):
    c=2*pi*mu; return 4*sqrt(pi)*8**n/factorial(n)*c**(n+mpf(1)/2)*exp(-2*c)
data=[("P47",5,3.10e-12),("Mori15even",15,2.3979e-70),("Mori20Gal",20,1.09899e-96)]
for nm,mu,v in data:
    f=fuchs(mu); print(nm,mu,"fuchs",mp.nstr(f,4),"ratio",mp.nstr(v/f,4),"log(v)/mu",mp.nstr(log(v)/mu,6))
print("slope 15->20:", mp.nstr((log(1.09899e-96)-log(2.3979e-70))/5,6),"4pi=",mp.nstr(4*pi,6),"incl. power corr:",mp.nstr((log(fuchs(20))-log(fuchs(15)))/5,6))
print("slope 5->15:", mp.nstr((log(2.3979e-70)-log(3.10e-12))/10,6))
for mu in [5,8.3729,10,12,15,16,17,19,23,25,27,29,31,32]:
    f=4.6*fuchs(mu); print(mu, "T=",mp.nstr(log(mu)/2,5),"pred",mp.nstr(f,4),"bits",mp.nstr(-log(f,2),5),"GalN~2.3ac",int(2.3*log(mu)/2*2*pi*mu))
