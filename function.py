# create function

"""
> com_fun = function(p,r,n,t){
+ A=p*(1+(r/n))^(n*t)
+ return(A)}
> com_fun(5000,0.05,12,10)
"""

def com_fun(p,r,n,t):
    A=p*(1+(r/n))**(n*t)
    print(A)

com_fun(5000,0.05,12,10)
