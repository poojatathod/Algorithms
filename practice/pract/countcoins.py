def countcoins(n):
    if n==0:
        return 0
    sol=1+countcoins(n-1)
    if n>=29:
        sol1=1+countcoins(n-29)
        sol=min(sol,sol1)
    if n>=50:
        sol2=1+countcoins(n-50)
        sol=min(sol,sol2)
    return sol




print "Enter a value of n: "
n=input()
op=countcoins(n)
print op
